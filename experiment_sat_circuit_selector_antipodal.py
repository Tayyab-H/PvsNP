"""CNF synthesis of shared circuits for the antipodal selector sample.

This is an independent SAT encoding of the partial-circuit search in
experiment_circuit_selector_antipodal.py. Inputs include free signed literals
and constants. Each topologically ordered gate is AND, OR, or NOT; arbitrary
fanout is allowed. The default query is m=5 with at most eight gates.

The optional conflict budget makes an inconclusive run explicit. A SAT model
is independently simulated on every sample row before it is reported.
"""

from __future__ import annotations

import argparse

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver


def selector_sample(m: int) -> tuple[int, list[int], list[int]]:
    if m < 3:
        raise ValueError("m must be at least 3")
    n = m + 1
    all_one = (1 << m) - 1
    low = [y for y in range(1 << m) if y.bit_count() <= 1]
    high = [y for y in range(1 << m) if (all_one ^ y).bit_count() <= 1]
    rows = sorted([1 + 2 * y for y in low] + [2 * y for y in high])
    labels = [int((row >> 1) in (0, all_one)) for row in rows]
    return n, rows, labels


class CircuitCNF:
    def __init__(self, m: int, gates: int):
        self.m = m
        self.gates = gates
        self.n, self.rows, self.labels = selector_sample(m)
        self.pool = IDPool()
        self.clauses: list[list[int]] = []
        self.wires: list[list[int | bool]] = []
        self.ops: list[list[int]] = []
        self.lefts: list[list[int]] = []
        self.rights: list[list[int]] = []
        self.gate_outputs: list[list[int]] = []
        self.output_choices: list[int] = []
        self._build()

    def var(self, *key: object) -> int:
        return self.pool.id(key)

    def exactly_one(self, lits: list[int]) -> None:
        self.clauses.extend(
            CardEnc.equals(lits=lits, bound=1, vpool=self.pool,
                          encoding=EncType.pairwise).clauses
        )

    def _selected_value(self, selectors: list[int], sources: list[int | bool],
                        out: int) -> None:
        # Exactly one selector is true. Under that selector, constrain out to
        # equal the corresponding signal value on this row.
        for select, source in zip(selectors, sources):
            if isinstance(source, bool):
                self.clauses.append([-select, out if source else -out])
            else:
                self.clauses.append([-select, -out, source])
                self.clauses.append([-select, out, -source])

    def _build(self) -> None:
        q = len(self.rows)
        # Free constants and signed literals are source wires.
        self.wires.extend(([False] * q, [True] * q))
        for bit in range(self.n):
            pos = [bool((row >> bit) & 1) for row in self.rows]
            self.wires.extend((pos, [not value for value in pos]))

        for gate in range(self.gates):
            previous = len(self.wires)
            op = [self.var("op", gate, kind) for kind in range(3)]
            left = [self.var("left", gate, source) for source in range(previous)]
            right = [self.var("right", gate, source) for source in range(previous)]
            self.exactly_one(op)
            self.exactly_one(left)
            self.exactly_one(right)
            # For a NOT gate, the unused second input has one canonical value.
            self.clauses.append([-op[2], right[0]])
            self.clauses.extend([[-op[2], -right[k]]
                                 for k in range(1, previous)])
            # Commutative symmetry: binary-gate input indices are ordered.
            for i in range(previous):
                for j in range(i):
                    self.clauses.append([-left[i], -right[j], op[2]])

            out_bits = [self.var("signal", gate, row_i) for row_i in range(q)]
            for row_i in range(q):
                left_value = self.var("selected-left", gate, row_i)
                right_value = self.var("selected-right", gate, row_i)
                self._selected_value(left, [wire[row_i] for wire in self.wires], left_value)
                self._selected_value(right, [wire[row_i] for wire in self.wires], right_value)
                z = out_bits[row_i]
                a, b = left_value, right_value
                # AND: z <-> a&b; OR: z <-> a|b; NOT: z <-> !a.
                self.clauses.extend([
                    [-op[0], -a, -b, z],
                    [-op[0], a, -z],
                    [-op[0], b, -z],
                    [-op[1], a, b, -z],
                    [-op[1], -a, z],
                    [-op[1], -b, z],
                    [-op[2], a, -z],
                    [-op[2], -a, z],
                ])
            self.wires.append(out_bits)
            self.ops.append(op)
            self.lefts.append(left)
            self.rights.append(right)
            self.gate_outputs.append(out_bits)

        self.output_choices = [self.var("output", i) for i in range(len(self.wires))]
        self.exactly_one(self.output_choices)
        for row_i, label in enumerate(self.labels):
            for choice, wire in zip(self.output_choices, self.wires):
                signal = wire[row_i]
                if isinstance(signal, bool):
                    if signal != bool(label):
                        self.clauses.append([-choice])
                else:
                    self.clauses.append([-choice, signal if label else -signal])

    def decode_and_verify(self, model: list[int]) -> dict:
        true_vars = {literal for literal in model if literal > 0}
        chosen = lambda literals: next(i for i, lit in enumerate(literals) if lit in true_vars)
        initial = [[0] * len(self.rows), [1] * len(self.rows)]
        for bit in range(self.n):
            pos = [((row >> bit) & 1) for row in self.rows]
            initial.extend((pos, [1 - value for value in pos]))
        signals = initial
        gates = []
        for gate in range(self.gates):
            kind = chosen(self.ops[gate])
            left = chosen(self.lefts[gate])
            right = chosen(self.rights[gate])
            gates.append((kind, left, right))
            a_values, b_values = signals[left], signals[right]
            if kind == 0:
                out = [a & b for a, b in zip(a_values, b_values)]
            elif kind == 1:
                out = [a | b for a, b in zip(a_values, b_values)]
            else:
                out = [1 - a for a in a_values]
            signals.append(out)
        output = chosen(self.output_choices)
        actual = signals[output]
        if actual != self.labels:
            raise AssertionError(f"decoded model fails direct check: {actual} != {self.labels}")
        return {"output_wire": output, "gates": gates}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, default=5)
    parser.add_argument("--gates", type=int, default=None)
    parser.add_argument("--conflicts", type=int, default=2_000_000)
    parser.add_argument("--solver", default="cadical195")
    args = parser.parse_args()
    gate_bound = args.gates if args.gates is not None else 2 * args.m - 2
    problem = CircuitCNF(args.m, gate_bound)
    print(f"m={args.m}; rows={len(problem.rows)}; gate_bound={gate_bound}; "
          f"variables={problem.pool.top}; clauses={len(problem.clauses)}; "
          f"solver={args.solver}; conflict_budget={args.conflicts}", flush=True)
    with Solver(name=args.solver, bootstrap_with=problem.clauses) as solver:
        solver.conf_budget(args.conflicts)
        status = solver.solve_limited(expect_interrupt=True)
        if status is True:
            witness = problem.decode_and_verify(solver.get_model())
            print(f"status=sat; independently_verified_witness={witness}")
        elif status is False:
            print("status=unsat; solver_result_only; no proof certificate emitted")
        else:
            print("status=unknown; conflict budget exhausted or solver interrupted")


if __name__ == "__main__":
    main()
