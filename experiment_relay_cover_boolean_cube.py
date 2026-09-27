"""Search for a two-rule universal cover of two extreme Boolean anchors.

The SAT model asks whether the n=3 relay certificate for anchors 0^n,1^n
extends to n=4. One rule must be a disjoint seed; the other may fire from
the forced coordinate slices and insert an intersection that enables it.
Any model is then checked by explicit preservation closure.
"""

from __future__ import annotations

from z3 import And, Bool, If, Implies, Not, Or, Solver, Sum, sat


def solve_dimension(n: int) -> None:
    anchors = [0, (1 << n) - 1]
    universe = [x for x in range(1 << n) if x not in anchors]
    point_index = {x: i for i, x in enumerate(universe)}
    u_size = len(universe)
    subset_count = 1 << u_size

    def matching_slices(anchor: int) -> list[list[int]]:
        return [[point_index[x] for x in universe
                 if ((x >> bit) & 1) == ((anchor >> bit) & 1)]
                for bit in range(n)]

    e = [[Bool(f"e_{n}_{r}_{u}") for u in range(u_size)] for r in range(2)]
    h = [[Bool(f"h_{n}_{r}_{u}") for u in range(u_size)] for r in range(2)]
    solver = Solver()

    def base(anchor: int, endpoint: list) -> object:
        alternatives = []
        for sl in matching_slices(anchor):
            alternatives.append(And(*(endpoint[u] for u in sl)))
        return Or(*alternatives)

    def disjoint(rule: int) -> object:
        return And(*(Not(And(e[rule][u], h[rule][u])) for u in range(u_size)))

    def relay_subset(source: int, target: list) -> object:
        return And(*(Implies(And(e[source][u], h[source][u]), target[u])
                     for u in range(u_size)))

    for anchor in anchors:
        derivations = []
        for seed in range(2):
            relay = 1 - seed
            seed_disjoint = disjoint(seed)
            direct = And(seed_disjoint, base(anchor, e[seed]), base(anchor, h[seed]))
            relay_fires_from_base = And(base(anchor, e[relay]), base(anchor, h[relay]))
            seed_enabled_after_relay = And(
                Or(base(anchor, e[seed]), relay_subset(relay, e[seed])),
                Or(base(anchor, h[seed]), relay_subset(relay, h[seed])),
            )
            via_relay = And(seed_disjoint, relay_fires_from_base, seed_enabled_after_relay)
            derivations.extend([direct, via_relay])
        solver.add(Or(*derivations))

    status = solver.check()
    print(f"n={n}; anchors={anchors}; universe={u_size}; rules=2; sat_status={status}")
    if status != sat:
        return

    model = solver.model()
    endpoint_masks = []
    for rule in range(2):
        emask = sum(1 << u for u in range(u_size) if model.eval(e[rule][u], model_completion=True))
        hmask = sum(1 << u for u in range(u_size) if model.eval(h[rule][u], model_completion=True))
        endpoint_masks.append((emask, hmask))
        print(f"  rule{rule}: E={[universe[u] for u in range(u_size) if emask >> u & 1]}; H={[universe[u] for u in range(u_size) if hmask >> u & 1]}; intersection={[universe[u] for u in range(u_size) if (emask & hmask) >> u & 1]}")

    def closure_reaches_empty(anchor: int) -> bool:
        generators = [sum(1 << point_index[x] for x in universe
                          if ((x >> bit) & 1) == ((anchor >> bit) & 1))
                      for bit in range(n)]
        closure = {s for s in range(subset_count)
                   if any(s & g == g for g in generators)}
        changed = True
        while changed:
            changed = False
            additions = set()
            for emask, hmask in endpoint_masks:
                if emask in closure and hmask in closure:
                    meet = emask & hmask
                    additions.update(s for s in range(subset_count) if s & meet == meet)
            new = additions - closure
            if new:
                closure.update(new)
                changed = True
                if 0 in closure:
                    return True
        return 0 in closure

    checked = [closure_reaches_empty(a) for a in anchors]
    print(f"explicit_closure_by_anchor={dict(zip(anchors, checked))}; verified_universal_two_rule_cover={all(checked)}")


def solve_rule_count(
    n: int,
    rule_count: int,
    anchors: list[int] | None = None,
    symmetry_break: bool = False,
    timeout_ms: int | None = None,
) -> None:
    """SAT search for an arbitrary rule list, unrolled through its least fixed point."""
    anchors = anchors if anchors is not None else [0, (1 << n) - 1]
    universe = [x for x in range(1 << n) if x not in anchors]
    point_index = {x: i for i, x in enumerate(universe)}
    u_size = len(universe)
    e = [[Bool(f"ge_{n}_{rule_count}_{r}_{u}") for u in range(u_size)]
         for r in range(rule_count)]
    h = [[Bool(f"gh_{n}_{rule_count}_{r}_{u}") for u in range(u_size)]
         for r in range(rule_count)]
    solver = Solver()

    def base(anchor: int, endpoint: list) -> object:
        return Or(*(And(*(endpoint[point_index[x]] for x in universe
                          if ((x >> bit) & 1) == ((anchor >> bit) & 1)))
                    for bit in range(n)))

    def subset_of_intersection(source: int, target: list) -> object:
        return And(*(Implies(And(e[source][u], h[source][u]), target[u])
                     for u in range(u_size)))

    def disjoint(rule: int) -> object:
        return And(*(Not(And(e[rule][u], h[rule][u])) for u in range(u_size)))

    fired = {
        a: [[Bool(f"fire_{n}_{rule_count}_{a}_{r}_{t}")
             for t in range(rule_count + 1)] for r in range(rule_count)]
        for a in anchors
    }
    for a in anchors:
        for r in range(rule_count):
            solver.add(Not(fired[a][r][0]))
        for t in range(rule_count):
            for r in range(rule_count):
                active_e = Or(base(a, e[r]), *(
                    And(fired[a][k][t], subset_of_intersection(k, e[r]))
                    for k in range(rule_count)))
                active_h = Or(base(a, h[r]), *(
                    And(fired[a][k][t], subset_of_intersection(k, h[r]))
                    for k in range(rule_count)))
                solver.add(fired[a][r][t + 1] ==
                           Or(fired[a][r][t], And(active_e, active_h)))
        solver.add(Or(*(And(disjoint(r), fired[a][r][rule_count])
                        for r in range(rule_count))))

    if symmetry_break:
        # Pair endpoints and rule labels are interchangeable. Normalize each
        # pair orientation and order rules by their concatenated endpoint mask.
        keys = []
        for r in range(rule_count):
            emask = Sum([If(e[r][u], 1 << u, 0) for u in range(u_size)])
            hmask = Sum([If(h[r][u], 1 << u, 0) for u in range(u_size)])
            solver.add(emask <= hmask)
            keys.append(emask * (1 << u_size) + hmask)
        for r in range(rule_count - 1):
            solver.add(keys[r] <= keys[r + 1])

    if timeout_ms is not None:
        solver.set(timeout=timeout_ms)
    status = solver.check()
    print(f"generic_rules={rule_count}; n={n}; anchors={anchors}; universe={u_size}; symmetry_break={symmetry_break}; sat_status={status}")
    if status != sat:
        return
    model = solver.model()
    endpoint_masks = []
    for r in range(rule_count):
        emask = sum(1 << u for u in range(u_size)
                    if model.eval(e[r][u], model_completion=True))
        hmask = sum(1 << u for u in range(u_size)
                    if model.eval(h[r][u], model_completion=True))
        endpoint_masks.append((emask, hmask))
        print(f"  rule{r}: E={[universe[u] for u in range(u_size) if emask >> u & 1]}; H={[universe[u] for u in range(u_size) if hmask >> u & 1]}; intersection={[universe[u] for u in range(u_size) if (emask & hmask) >> u & 1]}")

    # Independently check the exact closure on the O(m)-sized support family:
    # empty, each endpoint, and each pair intersection. Upward closure is
    # handled by subset tests, as in the global-support recurrence.
    support = {0}
    for emask, hmask in endpoint_masks:
        support.update((emask, hmask, emask & hmask))
    checked = []
    for anchor in anchors:
        gens = [sum(1 << point_index[x] for x in universe
                    if ((x >> bit) & 1) == ((anchor >> bit) & 1))
                for bit in range(n)]
        closure = {s for s in support if any(s & g == g for g in gens)}
        fired = [False] * rule_count
        round_number = 0
        while True:
            newly = [r for r, (emask, hmask) in enumerate(endpoint_masks)
                     if not fired[r] and emask in closure and hmask in closure]
            if not newly:
                break
            round_number += 1
            print(f"  anchor={anchor}; closure_round={round_number}; newly_fired_rules={newly}")
            for r in newly:
                fired[r] = True
                meet = endpoint_masks[r][0] & endpoint_masks[r][1]
                closure.update(s for s in support if s & meet == meet)
        checked.append(0 in closure)
    print(f"explicit_closure_by_anchor={dict(zip(anchors, checked))}; verified_universal_cover={all(checked)}")


if __name__ == "__main__":
    solve_dimension(3)
    solve_dimension(4)
    solve_rule_count(4, 3)
    solve_rule_count(5, 3)
    solve_rule_count(5, 4)
    solve_rule_count(6, 4)
    solve_rule_count(6, 5)
