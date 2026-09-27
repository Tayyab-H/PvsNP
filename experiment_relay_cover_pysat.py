"""Independent CNF/PySAT encoding of universal semi-filter relay covers.

This reproduces the least-fixed-point constraints from
experiment_relay_cover_boolean_cube.py without routing the formula through
Z3's SMT layer. Endpoints are arbitrary subsets of U. A rule fires once both
endpoints are initially supported by matching slices or contain an
intersection produced by an already-fired rule.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import combinations, count, permutations

from pysat.solvers import Solver


@dataclass
class Cnf:
    names: dict[str, int] = field(default_factory=dict)
    clauses: list[list[int]] = field(default_factory=list)
    _ids: object = field(default_factory=count)

    def new(self, name: str) -> int:
        var = next(self._ids) + 1
        self.names[name] = var
        return var

    def add(self, clause: list[int]) -> None:
        if any(-lit in clause for lit in clause):
            return
        self.clauses.append(clause)

    def equivalent_and(self, out: int, inputs: list[int]) -> None:
        if not inputs:
            self.add([out])
            return
        for lit in inputs:
            self.add([-out, lit])
        self.add([out] + [-lit for lit in inputs])

    def equivalent_or(self, out: int, inputs: list[int]) -> None:
        if not inputs:
            self.add([-out])
            return
        for lit in inputs:
            self.add([-lit, out])
        self.add([-out] + inputs)

    def clause_var(self, name: str, literals: list[int]) -> int:
        out = self.new(name)
        self.equivalent_or(out, literals)
        return out

    def lex_leq(self, left: list[int], right: list[int], label: str) -> None:
        assert len(left) == len(right)
        prefix = self.new(f"lex_prefix_{label}_0")
        self.add([prefix])
        for i, (a, b) in enumerate(zip(left, right)):
            # If all earlier bits agree, forbid the first differing pair 1,0.
            self.add([-prefix, -a, b])
            nxt = self.new(f"lex_prefix_{label}_{i + 1}")
            # nxt <-> prefix AND (a == b).
            self.add([-nxt, prefix])
            self.add([-nxt, -a, b])
            self.add([-nxt, a, -b])
            self.add([-prefix, a, b, nxt])
            self.add([-prefix, -a, -b, nxt])
            prefix = nxt


def solve(
    n: int,
    rule_count: int,
    anchors: list[int],
    solver_name: str = "cadical195",
    symmetry_break: bool = False,
    forced_bits_by_anchor: dict[int, set[int]] | None = None,
    minimum_disjoint_rules: int | None = None,
    first_seed_normal_form: bool = False,
    near_full_column_symmetry: bool = False,
) -> None:
    if symmetry_break and forced_bits_by_anchor is not None:
        raise ValueError(
            "coordinate-permutation symmetry is invalid for an arbitrary "
            "anchor-dependent generator selector"
        )
    if near_full_column_symmetry and symmetry_break:
        raise ValueError(
            "use either full coordinate symmetry or near-full column symmetry"
        )
    if near_full_column_symmetry:
        expected_anchors = {
            x for x in range(1 << n) if x.bit_count() <= n - 2
        }
        if n < 2 or set(anchors) != expected_anchors:
            raise ValueError(
                "near-full column symmetry requires all anchors of weight "
                "at most n-2"
            )
    universe = [x for x in range(1 << n) if x not in set(anchors)]
    if near_full_column_symmetry:
        full = (1 << n) - 1
        expected_universe = {full} | {full ^ (1 << i) for i in range(n)}
        if set(universe) != expected_universe:
            raise ValueError("unexpected near-full high universe")
    point_index = {x: i for i, x in enumerate(universe)}
    u_size = len(universe)
    cnf = Cnf()

    e = [[cnf.new(f"e_{r}_{u}") for u in range(u_size)] for r in range(rule_count)]
    h = [[cnf.new(f"h_{r}_{u}") for u in range(u_size)] for r in range(rule_count)]

    def base(anchor: int, endpoint: list[int], label: str) -> int:
        terms = []
        for bit in range(n):
            if (forced_bits_by_anchor is not None
                    and bit not in forced_bits_by_anchor[anchor]):
                continue
            slice_points = [
                endpoint[point_index[x]] for x in universe
                if ((x >> bit) & 1) == ((anchor >> bit) & 1)
            ]
            term = cnf.new(f"slice_{label}_{bit}")
            cnf.equivalent_and(term, slice_points)
            terms.append(term)
        out = cnf.new(f"base_{label}")
        cnf.equivalent_or(out, terms)
        return out

    # inc_e[k][r] means intersection(rule k) is a subset of endpoint E_r.
    inc_e = [[cnf.new(f"inc_e_{k}_{r}") for r in range(rule_count)]
             for k in range(rule_count)]
    inc_h = [[cnf.new(f"inc_h_{k}_{r}") for r in range(rule_count)]
             for k in range(rule_count)]
    for k in range(rule_count):
        for r in range(rule_count):
            e_conditions = []
            h_conditions = []
            for u in range(u_size):
                e_conditions.append(cnf.clause_var(
                    f"e_sub_{k}_{r}_{u}", [-e[k][u], -h[k][u], e[r][u]]
                ))
                h_conditions.append(cnf.clause_var(
                    f"h_sub_{k}_{r}_{u}", [-e[k][u], -h[k][u], h[r][u]]
                ))
            cnf.equivalent_and(inc_e[k][r], e_conditions)
            cnf.equivalent_and(inc_h[k][r], h_conditions)

    disjoint = []
    for r in range(rule_count):
        d = cnf.new(f"disjoint_{r}")
        point_conditions = [cnf.clause_var(
            f"disjoint_at_{r}_{u}", [-e[r][u], -h[r][u]]
        ) for u in range(u_size)]
        cnf.equivalent_and(d, point_conditions)
        disjoint.append(d)

    if minimum_disjoint_rules is not None:
        if not 1 <= minimum_disjoint_rules <= rule_count:
            raise ValueError("minimum_disjoint_rules must be in [1, rule_count]")
        clause_size = rule_count - minimum_disjoint_rules + 1
        for indices in combinations(range(rule_count), clause_size):
            cnf.add([disjoint[r] for r in indices])

    if near_full_column_symmetry:
        # The high universe consists of 1^n and one point u_i per coordinate,
        # where u_i has its unique zero at i. Coordinate permutations fix 1^n
        # and permute the u_i. Sorting their endpoint-membership columns gives
        # one representative from every S_n orbit without n! lex leaders.
        full = (1 << n) - 1
        for i in range(n - 1):
            left_point = full ^ (1 << i)
            right_point = full ^ (1 << (i + 1))
            left_column = []
            right_column = []
            for r in range(rule_count):
                left_column.extend((
                    e[r][point_index[left_point]],
                    h[r][point_index[left_point]],
                ))
                right_column.extend((
                    e[r][point_index[right_point]],
                    h[r][point_index[right_point]],
                ))
            cnf.lex_leq(
                left_column, right_column, f"near_full_column_{i}"
            )
    elif symmetry_break:
        # These transformations preserve the instance: swap E/H within a
        # rule, permute rule labels, and permute coordinates simultaneously
        # in anchors/universe. Lex leaders retain at least one orbit model.
        for r in range(rule_count):
            cnf.lex_leq(e[r], h[r], f"endpoint_orientation_{r}")
        for r in range(rule_count - 1):
            cnf.lex_leq(e[r] + h[r], e[r + 1] + h[r + 1], f"rule_order_{r}")
        identity = tuple(range(n))
        all_endpoint_vars = [var for r in range(rule_count) for var in e[r] + h[r]]
        for p_idx, perm in enumerate(permutations(range(n))):
            if perm == identity:
                continue
            image = []
            for r in range(rule_count):
                for endpoint in (e[r], h[r]):
                    for x in universe:
                        y = sum(((x >> i) & 1) << perm[i] for i in range(n))
                        image.append(endpoint[point_index[y]])
            cnf.lex_leq(all_endpoint_vars, image, f"coord_perm_{p_idx}")

    fired = {
        a: [[cnf.new(f"fired_{a}_{r}_{t}") for t in range(rule_count + 1)]
            for r in range(rule_count)]
        for a in anchors
    }
    for a in anchors:
        for r in range(rule_count):
            cnf.add([-fired[a][r][0]])
        base_e = [base(a, e[r], f"{a}_e_{r}") for r in range(rule_count)]
        base_h = [base(a, h[r], f"{a}_h_{r}") for r in range(rule_count)]

        for t in range(rule_count):
            for r in range(rule_count):
                e_sources = [base_e[r]]
                h_sources = [base_h[r]]
                for k in range(rule_count):
                    qe = cnf.new(f"q_e_{a}_{k}_{r}_{t}")
                    qh = cnf.new(f"q_h_{a}_{k}_{r}_{t}")
                    cnf.equivalent_and(qe, [fired[a][k][t], inc_e[k][r]])
                    cnf.equivalent_and(qh, [fired[a][k][t], inc_h[k][r]])
                    e_sources.append(qe)
                    h_sources.append(qh)
                active_e = cnf.new(f"active_e_{a}_{r}_{t}")
                active_h = cnf.new(f"active_h_{a}_{r}_{t}")
                cnf.equivalent_or(active_e, e_sources)
                cnf.equivalent_or(active_h, h_sources)
                fire_now = cnf.new(f"fire_now_{a}_{r}_{t}")
                fire_sources = [active_e, active_h]
                if first_seed_normal_form:
                    # Disjoint rules are terminal outputs: they cannot feed
                    # empty-set closure back into the relay subnetwork.
                    fire_sources.append(-disjoint[r])
                cnf.equivalent_and(fire_now, fire_sources)
                cnf.equivalent_or(fired[a][r][t + 1],
                                  [fired[a][r][t], fire_now])

        triggers = []
        for r in range(rule_count):
            trigger = cnf.new(f"seed_trigger_{a}_{r}")
            if first_seed_normal_form:
                end_e_sources = [base_e[r]]
                end_h_sources = [base_h[r]]
                for k in range(rule_count):
                    qe = cnf.new(f"terminal_q_e_{a}_{k}_{r}")
                    qh = cnf.new(f"terminal_q_h_{a}_{k}_{r}")
                    cnf.equivalent_and(
                        qe, [fired[a][k][rule_count], inc_e[k][r]]
                    )
                    cnf.equivalent_and(
                        qh, [fired[a][k][rule_count], inc_h[k][r]]
                    )
                    end_e_sources.append(qe)
                    end_h_sources.append(qh)
                end_active_e = cnf.new(f"terminal_active_e_{a}_{r}")
                end_active_h = cnf.new(f"terminal_active_h_{a}_{r}")
                cnf.equivalent_or(end_active_e, end_e_sources)
                cnf.equivalent_or(end_active_h, end_h_sources)
                cnf.equivalent_and(
                    trigger, [disjoint[r], end_active_e, end_active_h]
                )
            else:
                cnf.equivalent_and(
                    trigger, [disjoint[r], fired[a][r][rule_count]]
                )
            triggers.append(trigger)
        cnf.add(triggers)

    print(
        f"backend={solver_name}; n={n}; rules={rule_count}; anchors={len(anchors)}; "
        f"universe={u_size}; symmetry_break={symmetry_break}; "
        f"restricted_generators={forced_bits_by_anchor is not None}; "
        f"first_seed_normal_form={first_seed_normal_form}; "
        f"variables={max(cnf.names.values())}; clauses={len(cnf.clauses)}"
    )
    with Solver(name=solver_name, bootstrap_with=cnf.clauses) as solver:
        sat_status = solver.solve()
        print(f"sat_status={'sat' if sat_status else 'unsat'}")
        if not sat_status:
            return
        model = set(solver.get_model())

    def value(var: int) -> bool:
        return var in model

    endpoint_sets = []
    for r in range(rule_count):
        er = {universe[u] for u in range(u_size) if value(e[r][u])}
        hr = {universe[u] for u in range(u_size) if value(h[r][u])}
        endpoint_sets.append((er, hr))
        print(f"  rule{r}: E={sorted(er)}; H={sorted(hr)}; intersection={sorted(er & hr)}")

    # Independent exact support-closure check, as in Proposition 21.4.
    masks = []
    for er, hr in endpoint_sets:
        emask = sum(1 << point_index[x] for x in er)
        hmask = sum(1 << point_index[x] for x in hr)
        masks.append((emask, hmask))
    support = {0}
    for emask, hmask in masks:
        support.update((emask, hmask, emask & hmask))
    checked = []
    for a in anchors:
        generators = [sum(1 << point_index[x] for x in universe
                          if ((x >> i) & 1) == ((a >> i) & 1))
                      for i in range(n)
                      if (forced_bits_by_anchor is None
                          or i in forced_bits_by_anchor[a])]
        closure = {s for s in support if any((s & g) == g for g in generators)}
        fired_now = [False] * rule_count
        rounds = []
        while True:
            newly = [r for r, (emask, hmask) in enumerate(masks)
                     if not fired_now[r] and emask in closure and hmask in closure]
            if not newly:
                break
            rounds.append(newly)
            for r in newly:
                fired_now[r] = True
                meet = masks[r][0] & masks[r][1]
                closure.update(s for s in support if (s & meet) == meet)
        ok = 0 in closure
        checked.append(ok)
        print(f"  anchor={a}; closure_rounds={rounds}; derives_empty={ok}")
    print(f"verified_universal_cover={all(checked)}")


if __name__ == "__main__":
    solve(5, 5, [0, 1, 2, 4, 8, 16], symmetry_break=True)
