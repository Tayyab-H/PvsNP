"""Exact toy audit of counterexample-selector certificates.

Enumerate De Morgan formulas by binary-gate count and compute the smallest
row set inconsistent with a lower formula class. The n=3 profiles are
exhaustive over all high tables; the n=4 profiles are exhaustive at cutoffs 2
and 4.
Literals and constants are free leaves; binary AND/OR gates are counted, so
this is a formula model without internal sharing. It is not a general-circuit
Gap-MCSP result.
"""

from __future__ import annotations

from itertools import combinations, product


def exact_formula_classes(n: int, max_gates: int) -> list[set[int]]:
    domain = 1 << n
    full = (1 << domain) - 1
    leaves = {0, full}
    for i in range(n):
        pos = sum(1 << x for x in range(domain) if (x >> i) & 1)
        leaves.add(pos)
        leaves.add(full ^ pos)
    exact = [leaves]
    for gates in range(1, max_gates + 1):
        values: set[int] = set()
        for left_gates in range(gates):
            right_gates = gates - 1 - left_gates
            for a, b in product(exact[left_gates], exact[right_gates]):
                values.add(a & b)
                values.add(a | b)
        exact.append(values)
    return exact


def min_inconsistent_rows(f: int, candidate_functions: tuple[int, ...],
                          row_count: int) -> tuple[int, int]:
    disagreements = {f ^ g for g in candidate_functions}
    assert 0 not in disagreements, "high table must not be in candidate class"
    # A row subset is a selector image that must hit every candidate's
    # disagreement set. The first mask in increasing cardinality is optimal.
    order = sorted(range(1 << row_count), key=lambda q: (q.bit_count(), q))
    for q in order:
        if all(q & d for d in disagreements):
            return q.bit_count(), q
    raise AssertionError("the full row set must distinguish a high table")


def exhaustive_selector_profile(
    n: int, cutoff: int
) -> tuple[int, list[int], int, int]:
    """Compute exact selector sizes for every high table in a small cube."""
    import numpy as np

    row_count = 1 << n
    exact = exact_formula_classes(n, cutoff)
    low: set[int] = set()
    for layer in exact:
        low.update(layer)
    all_tables = np.arange(1 << row_count, dtype=np.uint16)
    low_tables = np.fromiter(low, dtype=np.uint16, count=len(low))
    is_low = np.zeros(1 << row_count, dtype=bool)
    is_low[low_tables] = True
    sizes = np.zeros(1 << row_count, dtype=np.uint8)
    selector_masks = np.zeros(1 << row_count, dtype=np.uint16)

    for q in range(1, row_count + 1):
        for rows in combinations(range(row_count), q):
            allowed = np.zeros(1 << q, dtype=bool)
            low_patterns = np.zeros(len(low_tables), dtype=np.uint8)
            patterns = np.zeros(len(all_tables), dtype=np.uint8)
            for j, row in enumerate(rows):
                low_patterns |= (((low_tables >> row) & 1).astype(np.uint8) << j)
                patterns |= (((all_tables >> row) & 1).astype(np.uint8) << j)
            allowed[low_patterns] = True
            new = (sizes == 0) & (~is_low) & (~allowed[patterns])
            sizes[new] = q
            selector_masks[new] = sum(1 << row for row in rows)
        if np.all(sizes[~is_low]):
            break
    high_sizes = np.sort(sizes[~is_low])
    if not len(high_sizes) or high_sizes[-1] == 0:
        raise AssertionError("full row set must certify every high table")
    max_size = int(high_sizes[-1])
    max_examples = np.flatnonzero((sizes == max_size) & (~is_low))
    return len(low), high_sizes.tolist(), int(max_examples[0]), int(
        selector_masks[max_examples[0]]
    )


def main() -> None:
    n = 3
    row_count = 1 << n
    exact = exact_formula_classes(n, max_gates=6)
    cumulative: set[int] = set()
    classes: list[set[int]] = []
    for cutoff, layer in enumerate(exact):
        cumulative.update(layer)
        classes.append(set(cumulative))
        if cutoff in (1, 2, 3, 4, 5, 6):
            candidates = tuple(sorted(cumulative))
            high = [f for f in range(1 << row_count) if f not in cumulative]
            if not high:
                print(f"n={n}; formula_gates<={cutoff}; all_tables_in_class=True")
                break
            sizes_and_masks = [
                min_inconsistent_rows(f, candidates, row_count) for f in high
            ]
            sizes = sorted(size for size, _ in sizes_and_masks)
            median = sizes[len(sizes) // 2]
            print(
                f"n={n}; formula_gates<={cutoff}; low_tables={len(candidates)}; "
                f"high_tables={len(high)}; min_selector_rows={sizes[0]}; "
                f"median={median}; max={sizes[-1]}; all_exact=True"
            )

    for low_cutoff, high_cutoff in ((1, 3), (2, 4), (2, 5), (3, 5)):
        low_candidates = tuple(sorted(classes[low_cutoff]))
        high = [f for f in range(1 << row_count)
                if f not in classes[high_cutoff]]
        sizes = sorted(
            min_inconsistent_rows(f, low_candidates, row_count)[0]
            for f in high
        )
        print(
            f"gap_formula_cutoffs=({low_cutoff},{high_cutoff}); "
            f"low_tables={len(low_candidates)}; high_tables={len(high)}; "
            f"promise_selector_rows_min={sizes[0]}; "
            f"median={sizes[len(sizes)//2]}; max={sizes[-1]}; all_exact=True"
        )

    for cutoff in (2, 4):
        low_count, high_sizes, example, qmask = exhaustive_selector_profile(
            n=4, cutoff=cutoff
        )
        print(
            f"n=4; formula_gates<={cutoff}; "
            f"low_tables={low_count}; high_tables={len(high_sizes)}; "
            f"min={high_sizes[0]}; median={high_sizes[len(high_sizes)//2]}; "
            f"max={high_sizes[-1]}; all_exact=True"
        )
        if cutoff == 4:
            exact = exact_formula_classes(n=4, max_gates=cutoff)
            low: set[int] = set()
            for layer in exact:
                low.update(layer)
            rows = [i for i in range(16) if (qmask >> i) & 1]
            q_bits = [1 << i for i in rows]
            near_miss_patterns = {
                (example ^ g) & qmask for g in low
            }
            if 0 in near_miss_patterns:
                raise AssertionError("selector set admitted a low formula")
            if not set(q_bits) <= near_miss_patterns:
                raise AssertionError("a one-row deletion lacks a low completion")
            completion_layers = exact_formula_classes(n=4, max_gates=6)
            completion_class: set[int] = set()
            partial_min = None
            partial_completions = 0
            for gates, layer in enumerate(completion_layers):
                completion_class.update(layer)
                matches = [
                    g for g in completion_class
                    if ((example ^ g) & qmask) == 0
                ]
                if matches:
                    partial_min = gates
                    partial_completions = len(matches)
                    break
            if partial_min is None:
                raise AssertionError("the critical shadow needs a completion")
            print(
                f"critical_shadow_example=0x{example:04x}; rows={rows}; "
                f"private_one_error_patterns={len(set(q_bits) & near_miss_patterns)}/"
                f"{len(rows)}; every_deletion_realizable=True; "
                f"partial_formula_min={partial_min}; "
                f"completions_at_min={partial_completions}"
            )


if __name__ == "__main__":
    main()
