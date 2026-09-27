"""Five-input stress test for critical trace holes in a small formula class.

The exact low class is all De Morgan formulas with at most five AND/OR gates.
This script measures realized restrictions and missing labelings on selected
row sets, then counts holes whose complete one-bit neighborhood is realized.
It is a finite formula experiment, not a circuit lower bound or an exhaustive
search over every row subset.
"""

from __future__ import annotations

import random

import numpy as np

from experiment_formula_high_selector_toy import exact_formula_classes


def trace_profile(values: np.ndarray, rows: tuple[int, ...]) -> tuple[int, int, int]:
    signatures = np.zeros(len(values), dtype=np.uint32)
    for j, row in enumerate(rows):
        signatures |= (((values >> row) & 1).astype(np.uint32) << j)
    realized = np.zeros(1 << len(rows), dtype=bool)
    realized[signatures] = True
    holes = np.flatnonzero(~realized)
    critical = holes
    for j in range(len(rows)):
        critical = critical[realized[critical ^ (1 << j)]]
    return int(realized.sum()), len(holes), len(critical)


def greedy_trace_rows(values: np.ndarray, row_count: int, q: int) -> tuple[tuple[int, ...], list[int]]:
    bits = np.stack([((values >> row) & 1).astype(np.uint32)
                     for row in range(row_count)], axis=1)
    signatures = np.zeros(len(values), dtype=np.uint32)
    remaining = set(range(row_count))
    rows: list[int] = []
    counts: list[int] = []
    for _ in range(q):
        best_count = -1
        best_row = -1
        best_signatures: np.ndarray | None = None
        for row in sorted(remaining):
            candidate = (signatures << 1) | bits[:, row]
            count = len(np.unique(candidate))
            if count > best_count:
                best_count, best_row, best_signatures = count, row, candidate
        if best_signatures is None:
            raise AssertionError("greedy row selection failed")
        signatures = best_signatures
        rows.append(best_row)
        counts.append(best_count)
        remaining.remove(best_row)
    return tuple(rows), counts


def main() -> None:
    n = 5
    row_count = 1 << n
    cutoff = 5
    exact = exact_formula_classes(n, cutoff)
    low_set = set().union(*exact)
    values = np.fromiter(sorted(low_set), dtype=np.uint32, count=len(low_set))
    print(f"n={n}; formula_cutoff={cutoff}; low_functions={len(low_set)}")

    even = tuple(row for row in range(row_count) if row.bit_count() % 2 == 0)
    print(f"even_parity_Q={even}; trace_holes_critical={trace_profile(values, even)}")
    for extra in (1, 2, 4, 7):
        rows = tuple(sorted(even + (extra,)))
        print(f"even_parity_plus_{extra}_Q={rows}; trace_holes_critical={trace_profile(values, rows)}")

    rng = random.Random(20260925)
    for q in range(12, 18):
        records = []
        for _ in range(10):
            rows = tuple(sorted(rng.sample(range(row_count), q)))
            records.append(trace_profile(values, rows))
        print(
            f"seeded_random_q={q}; samples=10; "
            f"trace_minmax=({min(r[0] for r in records)},{max(r[0] for r in records)}); "
            f"hole_minmax=({min(r[1] for r in records)},{max(r[1] for r in records)}); "
            f"critical_total={sum(r[2] for r in records)}; "
            f"critical_max={max(r[2] for r in records)}"
        )

    rng = random.Random(20260924)
    q17_records = [
        trace_profile(values, tuple(sorted(rng.sample(range(row_count), 17))))
        for _ in range(24)
    ]
    print(
        f"seeded_random_q=17; samples=24; "
        f"trace_minmax=({min(r[0] for r in q17_records)},{max(r[0] for r in q17_records)}); "
        f"hole_minmax=({min(r[1] for r in q17_records)},{max(r[1] for r in q17_records)}); "
        f"critical_total={sum(r[2] for r in q17_records)}; "
        f"critical_max={max(r[2] for r in q17_records)}"
    )

    greedy_rows, counts = greedy_trace_rows(values, row_count, q=17)
    greedy_profile = trace_profile(values, greedy_rows)
    print(f"greedy_rows={greedy_rows}; trace_counts_by_step={counts}")
    print(f"greedy_q=17; trace_holes_critical={greedy_profile}")


if __name__ == "__main__":
    main()
