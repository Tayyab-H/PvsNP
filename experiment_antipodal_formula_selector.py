"""Verify an exact formula selector theorem on n=4 and n=5.

Let F(a,y)=1 iff y is 0^m or 1^m, with a an irrelevant input. A polarity
argument gives formula size 2m-1. A boundary sample of 2m+2 rows excludes all
smaller formulas, while 2m+2 disjoint two-row disagreement sets lower-bound
every selector image. This script checks the finite trace and witness claims
for m=3,4; the proof in New Model.MD is for all m>=3.
"""

from __future__ import annotations

from itertools import combinations

from experiment_formula_high_selector_toy import exact_formula_classes


def table_mask(n: int, predicate) -> int:
    return sum(1 << row for row in range(1 << n) if predicate(row))


def project(table: int, rows: tuple[int, ...]) -> int:
    return sum(((table >> row) & 1) << j for j, row in enumerate(rows))


def antipodal_family(m: int) -> tuple[int, tuple[int, ...], tuple[tuple[int, int], ...]]:
    """Return F, its boundary selector Q, and the disjoint mismatch pairs."""
    if m < 3:
        raise ValueError("the two radius-one endpoint neighborhoods must be disjoint")
    n = m + 1
    all_one = (1 << m) - 1

    def f_on_row(row: int) -> bool:
        y = row >> 1
        return y == 0 or y == all_one

    table = table_mask(n, f_on_row)
    low_cluster = tuple(y for y in range(1 << m) if y.bit_count() <= 1)
    high_cluster = tuple(y for y in range(1 << m) if (all_one ^ y).bit_count() <= 1)
    rows = tuple(sorted((1 + 2 * y for y in low_cluster), key=int)) + tuple(
        sorted(2 * y for y in high_cluster)
    )
    # Coordinates are disjoint and rows are emitted in the convention used to
    # index the projection; sorting globally is needed for stable comparison.
    rows = tuple(sorted(rows))
    pairs = tuple(sorted((2 * y, 2 * y + 1) for y in (*low_cluster, *high_cluster)))
    return table, rows, pairs


def mismatch_witness(m: int, y: int) -> int:
    """Build the low formula that differs from F on the x0-fiber over y."""
    all_one = (1 << m) - 1
    weight = y.bit_count()
    if y == 0:
        true_y = {all_one}
    elif y == all_one:
        true_y = {0}
    elif weight == 1 or weight == m - 1:
        true_y = {0, y, all_one}
    else:
        raise ValueError("y must lie within distance one of an endpoint")

    return table_mask(m + 1, lambda row: (row >> 1) in true_y)


def main() -> None:
    for m in (3, 4):
        n = m + 1
        threshold = 2 * m - 1
        f, rows, pairs = antipodal_family(m)
        exact = exact_formula_classes(n, threshold - 1)
        low = set().union(*exact)
        target = project(f, rows)
        traces = {project(g, rows) for g in low}
        if target in traces:
            raise AssertionError("the boundary labeling must be a trace hole")
        if len(rows) != 2 * m + 2 or len(set(rows)) != len(rows):
            raise AssertionError("the boundary sample has the wrong size")

        for y in (*[z for z in range(1 << m) if z.bit_count() <= 1],
                  *[z for z in range(1 << m)
                    if ((1 << m) - 1 ^ z).bit_count() <= 1]):
            witness = mismatch_witness(m, y)
            if witness not in low:
                raise AssertionError("an analytic low witness is absent from exact enumeration")
            mismatch = f ^ witness
            expected_pair = (1 << (2 * y)) | (1 << (2 * y + 1))
            if mismatch != expected_pair:
                raise AssertionError("a witness must differ exactly on its two-row fiber")

        if len(pairs) != 2 * m + 2 or len(set(r for pair in pairs for r in pair)) != 2 * len(pairs):
            raise AssertionError("the disagreement pairs must be pairwise disjoint")
        if any(not any((pair[0] == row or pair[1] == row) for row in rows)
               for pair in pairs):
            raise AssertionError("the proposed selector must hit every mismatch pair")
        if any(project(g, rows) == target for g in low):
            raise AssertionError("the selector must reject every low formula")

        # Minimum selector image: the disjoint pairs force 2m+2 rows, and the
        # explicit boundary sample attains that bound.
        print(
            f"m={m}; input_bits={n}; low_gate_cutoff={threshold-1}; "
            f"low_functions={len(low)}; target_table=0x{f:0{(1<<n)//4}x}; "
            f"Q={rows}; Q_size={len(rows)}; target_restriction=0x{target:x}; "
            f"disjoint_two_row_witnesses={len(pairs)}; "
            f"exact_formula_selector_image={2*m+2}"
        )


if __name__ == "__main__":
    main()
