"""Search coordinated row/column incidence designs for hard fusion covers.

Each anchor (p,q) gets two minimal witnesses: a sparse subset of row p and
a sparse subset of column q.  The 3^M witness-orientation enumeration is exact
for the resulting two-minimum filters (see Proposition 18.21).
"""

from __future__ import annotations

import random
from itertools import product


def exact_cover(filters: list[tuple[int, int]]) -> tuple[int, int, int]:
    m = len(filters)
    target = (1 << m) - 1
    cover_masks: set[int] = set()
    max_coverage = 0
    for orientation in product((0, 1, 2), repeat=m):
        left = right = 0
        for choice, (a, b) in zip(orientation, filters):
            if choice == 1:
                left |= a
                right |= b
            elif choice == 2:
                left |= b
                right |= a
        inter = left & right
        covered = 0
        for i, (a, b) in enumerate(filters):
            e_ok = (left & a) == a or (left & b) == b
            h_ok = (right & a) == a or (right & b) == b
            z_ok = (inter & a) == a or (inter & b) == b
            if e_ok and h_ok and not z_ok:
                covered |= 1 << i
        if covered:
            cover_masks.add(covered)
            max_coverage = max(max_coverage, covered.bit_count())

    # Exact set-cover dynamic program over the 2^M anchor masks.
    infinity = m + 1
    dp = [infinity] * (target + 1)
    dp[0] = 0
    for covered in range(target + 1):
        if dp[covered] == infinity:
            continue
        for pair_mask in cover_masks:
            union = covered | pair_mask
            if dp[union] > dp[covered] + 1:
                dp[union] = dp[covered] + 1
    return dp[target], max_coverage, len(cover_masks)


def make_family(
    rng: random.Random,
    side: int,
    m: int,
    witness_size: int,
    anchors: list[tuple[int, int]] | None = None,
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    if anchors is None:
        anchors = rng.sample(list(product(range(side), repeat=2)), m)
    filters: list[tuple[int, int]] = []
    for p, q in anchors:
        row_columns = [x for x in range(side) if x != q]
        column_rows = [x for x in range(side) if x != p]
        a = sum(1 << (p * side + x) for x in rng.sample(row_columns, witness_size))
        b = sum(1 << (x * side + q) for x in rng.sample(column_rows, witness_size))
        assert a and b and not (a & b)
        filters.append((a, b))
    return anchors, filters


def main() -> None:
    rng = random.Random(20260924)
    cases = [
        # (grid side, anchors, witness size, trials)
        (4, 7, 2, 120),
        (5, 8, 2, 100),
        (5, 8, 3, 100),
        (6, 9, 3, 40),
    ]
    for side, m, k, trials in cases:
        histogram: dict[int, int] = {}
        best_cover = 0
        best_pair_max = m
        witness_pairs = set()
        best_family: tuple[list[tuple[int, int]], list[tuple[int, int]]] | None = None
        for _ in range(trials):
            anchors, filters = make_family(rng, side, m, k)
            cover, pair_max, num_masks = exact_cover(filters)
            histogram[cover] = histogram.get(cover, 0) + 1
            witness_pairs.add(num_masks)
            if (cover, -pair_max) > (best_cover, -best_pair_max):
                best_cover, best_pair_max = cover, pair_max
                best_family = anchors, filters
        print(
            f"grid={side}x{side}; anchors={m}; witness_size={k}; trials={trials}; "
            f"cover_histogram={dict(sorted(histogram.items()))}; "
            f"best_cover={best_cover}; best_pair_max={best_pair_max}; "
            f"distinct_pair_cover_masks={len(witness_pairs)}",
            flush=True,
        )
        if best_family is not None:
            anchors, filters = best_family
            print("best_anchors=" + repr(anchors), flush=True)
            print("best_witnesses=" + repr(filters), flush=True)


if __name__ == "__main__":
    main()
