"""Exact cover search for sparse anchored subsets of complementary cylinders."""

from __future__ import annotations

import random
from itertools import product


def exact_cover_number(cover_masks: set[int], target: int) -> int:
    best = [target.bit_count() + 1] * (target + 1)
    best[0] = 0
    for cover in cover_masks:
        for old in range(target + 1):
            if best[old] <= target.bit_count():
                nxt = old | cover
                best[nxt] = min(best[nxt], best[old] + 1)
    return best[target]


def exact_cover(minima: list[tuple[int, int]]) -> tuple[int, int]:
    m = len(minima)
    target = (1 << m) - 1
    cover_masks = set()
    max_coverage = 0
    for code in product((0, 1, 2), repeat=m):
        left = right = 0
        for choice, (a, b) in zip(code, minima):
            if choice == 1:
                left |= a
                right |= b
            elif choice == 2:
                left |= b
                right |= a
        inter = left & right
        covered = 0
        for i, (a, b) in enumerate(minima):
            e_ok = (left & a) == a or (left & b) == b
            h_ok = (right & a) == a or (right & b) == b
            z_ok = (inter & a) == a or (inter & b) == b
            if e_ok and h_ok and not z_ok:
                covered |= 1 << i
        if covered:
            cover_masks.add(covered)
            max_coverage = max(max_coverage, covered.bit_count())
    return exact_cover_number(cover_masks, target), max_coverage


def main() -> None:
    rng = random.Random(20260924)
    n = 8
    words = [w for w in range(1 << n) if w.bit_count() == 2]
    anchors = [a for a in range(1 << n) if a.bit_count() <= 1]
    left_block = (1 << 4) - 1
    right_block = ((1 << n) - 1) ^ left_block
    cylinders = []
    for anchor in anchors:
        left = sum(
            1 << index for index, word in enumerate(words)
            if all(((word >> k) & 1) == ((anchor >> k) & 1)
                   for k in range(n) if (left_block >> k) & 1)
        )
        right = sum(
            1 << index for index, word in enumerate(words)
            if all(((word >> k) & 1) == ((anchor >> k) & 1)
                   for k in range(n) if (right_block >> k) & 1)
        )
        assert left.bit_count() >= 4 and right.bit_count() >= 4
        cylinders.append((left, right))

    trials_per_size = 100
    for witness_size in (2, 3, 4):
        histogram: dict[int, int] = {}
        min_max_pair = len(anchors)
        max_cover_seen = 0
        for _ in range(trials_per_size):
            minima = []
            for left, right in cylinders:
                left_points = [i for i in range(len(words)) if (left >> i) & 1]
                right_points = [i for i in range(len(words)) if (right >> i) & 1]
                a = sum(1 << i for i in rng.sample(left_points, witness_size))
                b = sum(1 << i for i in rng.sample(right_points, witness_size))
                assert a and b and not (a & b)
                minima.append((a, b))
            cover, pair_max = exact_cover(minima)
            histogram[cover] = histogram.get(cover, 0) + 1
            min_max_pair = min(min_max_pair, pair_max)
            max_cover_seen = max(max_cover_seen, cover)
        print(
            f"n={n}; |U|={len(words)}; anchors={len(anchors)}; "
            f"witness_size={witness_size}; trials={trials_per_size}; "
            f"cover_histogram={dict(sorted(histogram.items()))}; "
            f"largest_cover={max_cover_seen}; smallest_max_pair_coverage={min_max_pair}"
        )


if __name__ == "__main__":
    main()
