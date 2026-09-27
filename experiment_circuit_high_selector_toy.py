"""Exact n=3 audit of selector images against shared Boolean circuits.

Circuits use free variables, complemented variables, and constants, together
with AND/OR gates of fan-in two and NOT gates of fan-in one. A state records
the set of truth tables available as signals after a gate sequence, so
identical states can be merged while retaining arbitrary fanout and sharing.
The experiment is finite and makes no asymptotic circuit-complexity claim.
"""

from __future__ import annotations

from itertools import combinations_with_replacement

from experiment_formula_high_selector_toy import (
    exact_formula_classes,
    min_inconsistent_rows,
)


def circuit_classes(n: int, max_gates: int) -> tuple[list[set[int]], list[int]]:
    domain = 1 << n
    full = (1 << domain) - 1
    leaves = {0, full}
    for i in range(n):
        positive = sum(1 << x for x in range(domain) if (x >> i) & 1)
        leaves.update((positive, full ^ positive))

    states = {frozenset(leaves)}
    at_most = set(leaves)
    classes = [set(at_most)]
    state_counts = [len(states)]

    for _gate_count in range(1, max_gates + 1):
        next_states: set[frozenset[int]] = set()
        for state in states:
            signals = sorted(state)
            for left, right in combinations_with_replacement(signals, 2):
                for output in (left & right, left | right):
                    if output not in state:
                        next_states.add(state | {output})
            for signal in signals:
                output = full ^ signal
                if output not in state:
                    next_states.add(state | {output})
        states = next_states
        for state in states:
            at_most.update(state)
        classes.append(set(at_most))
        state_counts.append(len(states))

    return classes, state_counts


def main() -> None:
    n = 3
    row_count = 1 << n
    classes, state_counts = circuit_classes(n, max_gates=4)
    for gates, (low, states) in enumerate(zip(classes, state_counts)):
        if gates:
            high = [f for f in range(1 << row_count) if f not in low]
            sizes = sorted(
                min_inconsistent_rows(f, tuple(sorted(low)), row_count)[0]
                for f in high
            )
            profile = (
                f"; high_tables={len(high)}; min={sizes[0]}; "
                f"median={sizes[len(sizes)//2]}; max={sizes[-1]}"
            ) if high else "; all_tables_in_class=True"
        else:
            profile = ""
        print(
            f"n={n}; circuit_gates<={gates}; "
            f"low_tables={len(low)}; exact_gate_states={states}"
            f"{profile}; all_exact=True"
        )

    n = 4
    circuit, state_counts = circuit_classes(n, max_gates=4)
    formula_exact = exact_formula_classes(n, max_gates=4)
    formula_cumulative: set[int] = set()
    for gates, (circuit_functions, states, formula_layer) in enumerate(
        zip(circuit, state_counts, formula_exact)
    ):
        formula_cumulative.update(formula_layer)
        if circuit_functions != formula_cumulative:
            raise AssertionError(
                f"n=4 circuit/formula classes differ at {gates} gates"
            )
        print(
            f"n={n}; circuit_gates<={gates}; "
            f"low_tables={len(circuit_functions)}; exact_gate_states={states}; "
            "matches_formula_class=True"
        )


if __name__ == "__main__":
    main()
