"""Search for small shared circuits matching the antipodal selector sample.

The formula theorem in Idea 114 excludes all De Morgan formulas through
2m-2 gates. This exact SAT encoding asks whether a general acyclic Boolean
circuit with fanout (AND/OR fan-in two, NOT fan-in one, complemented input
literals and constants free) can match the same partial table with at most
2m-2 gates. Unused slots are allowed, so a g-slot solution represents every
circuit of size at most g. Any SAT witness is independently re-evaluated.

An UNSAT result is solver evidence for this finite instance, not a theorem
about all m. The script intentionally does not infer an all-m circuit bound.
"""

from __future__ import annotations

from z3 import And, Bool, BoolVal, If, Int, Not, Or, Solver, sat


def sample(m: int) -> tuple[int, list[int], list[int]]:
    """Return input width, selector rows, and their F_m labels."""
    if m < 3:
        raise ValueError("m must be at least 3")
    n = m + 1
    all_one = (1 << m) - 1
    y_values = [y for y in range(1 << m) if y.bit_count() <= 1]
    y_values += [y for y in range(1 << m) if (all_one ^ y).bit_count() <= 1]
    rows = sorted({(1 + 2 * y) for y in y_values if y.bit_count() <= 1} |
                  {(2 * y) for y in y_values if (all_one ^ y).bit_count() <= 1})
    labels = [int((row >> 1) in (0, all_one)) for row in rows]
    return n, rows, labels


def bool_select(index, values):
    return Or(*[And(index == i, value) for i, value in enumerate(values)])


def synthesize(
    m: int, gates: int, timeout_ms: int = 30_000, symmetry_break: bool = False
) -> tuple[str, dict | None, tuple[int, list[int], list[int]]]:
    n, rows, labels = sample(m)
    solver = Solver()
    solver.set(timeout=timeout_ms)
    # The initial wires are the two constants followed by both polarities of
    # every input bit; these literal sources are free, as in the project
    # circuit enumerator. Every later wire is one gate output.
    initial_values = [[BoolVal(False) for _ in rows], [BoolVal(True) for _ in rows]]
    for bit in range(n):
        initial_values.append([BoolVal(bool((row >> bit) & 1)) for row in rows])
        initial_values.append([BoolVal(not bool((row >> bit) & 1)) for row in rows])

    wires = list(initial_values)
    gate_records = []
    for gate in range(gates):
        source_count = len(wires)
        op = Int(f"op_{gate}")  # 0=AND, 1=OR, 2=NOT
        left = Int(f"left_{gate}")
        right = Int(f"right_{gate}")
        solver.add(op >= 0, op <= 2, left >= 0, left < source_count)
        solver.add(right >= 0, right < source_count)
        if symmetry_break:
            # Commutative gates have one canonical operand order. NOT's second
            # selector is semantically unused and can be fixed to a dummy wire.
            solver.add(If(op == 2, right == 0, left <= right))
        output = [Bool(f"g{gate}_r{j}") for j in range(len(rows))]
        for j in range(len(rows)):
            lhs = bool_select(left, [wire[j] for wire in wires])
            rhs = bool_select(right, [wire[j] for wire in wires])
            solver.add(output[j] == If(op == 0, And(lhs, rhs),
                                       If(op == 1, Or(lhs, rhs), Not(lhs))))
        wires.append(output)
        gate_records.append((op, left, right))

    output_wire = Int("output_wire")
    solver.add(output_wire >= 0, output_wire < len(wires))
    if symmetry_break:
        # In an output-minimal circuit, no active gate computes a signal already
        # available on the sample: that gate could be bypassed. Work backward
        # from the selected output to mark the active cone, leaving padding
        # gates unconstrained so all sizes <= the bound remain represented.
        active = [None] * gates
        base = len(initial_values)
        for gate in range(gates - 1, -1, -1):
            target = base + gate
            dependencies = [output_wire == target]
            for later in range(gate + 1, gates):
                op_later, left_later, right_later = gate_records[later]
                uses_target = Or(
                    left_later == target,
                    And(op_later != 2, right_later == target),
                )
                dependencies.append(And(active[later], uses_target))
            active[gate] = Or(*dependencies)
            for prior in range(base + gate):
                differs_on_sample = Or(*[
                    wires[base + gate][row_index] != wires[prior][row_index]
                    for row_index in range(len(rows))
                ])
                solver.add(If(active[gate], differs_on_sample, True))
    for j, label in enumerate(labels):
        selected = bool_select(output_wire, [wire[j] for wire in wires])
        solver.add(selected == BoolVal(bool(label)))

    result = solver.check()
    if result != sat:
        status = str(result)
        if status == "unknown":
            status += f" ({solver.reason_unknown()})"
        return status, None, (n, rows, labels)

    model = solver.model()
    record = {
        "output_wire": model.eval(output_wire).as_long(),
        "gates": [],
    }
    for op, left, right in gate_records:
        record["gates"].append((
            model.eval(op).as_long(),
            model.eval(left).as_long(),
            model.eval(right).as_long(),
        ))
    return "sat", record, (n, rows, labels)


def verify_witness(n: int, rows: list[int], labels: list[int], record: dict) -> None:
    all_rows = rows
    signals = [[0 for _ in all_rows], [1 for _ in all_rows]]
    for bit in range(n):
        positive = [((row >> bit) & 1) for row in all_rows]
        signals.extend((positive, [1 - x for x in positive]))
    for op, left, right in record["gates"]:
        out = []
        for j in range(len(rows)):
            a = signals[left][j]
            b = signals[right][j]
            out.append((a & b) if op == 0 else (a | b) if op == 1 else (1 - a))
        signals.append(out)
    actual = signals[record["output_wire"]]
    if actual != labels:
        raise AssertionError(f"solver witness failed direct verification: {actual} != {labels}")


def main() -> None:
    for m in (3, 4):
        threshold = 2 * m - 1
        for gates in (threshold - 1, threshold):
            status, witness, (n, rows, labels) = synthesize(m, gates)
            print(f"m={m}; inputs={n}; gate_bound={gates}; Q_size={len(rows)}; "
                  f"status={status}; rows={rows}; labels={labels}")
            if witness is not None:
                verify_witness(n, rows, labels, witness)
                print(f"  independently_verified_circuit={witness}")



if __name__ == "__main__":
    main()
