"""Search punctured block cylinders with exact cover enumeration by witnesses."""

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


def evaluate(minima_by_anchor: list[tuple[int, int]]) -> tuple[int, int]:
    anchor_count = len(minima_by_anchor)
    target = (1 << anchor_count) - 1
    covers = set()
    max_pair_coverage = 0
    # 0 = omit anchor; 1/2 = assign its first/second witness to the left.
    for choices in product((0, 1, 2), repeat=anchor_count):
        left = right = 0
        for choice, (a, b) in zip(choices, minima_by_anchor):
            if choice == 1:
                left |= a
                right |= b
            elif choice == 2:
                left |= b
                right |= a
        intersection = left & right
        covered = 0
        for index, (a, b) in enumerate(minima_by_anchor):
            left_accepts = ((left & a) == a) or ((left & b) == b)
            right_accepts = ((right & a) == a) or ((right & b) == b)
            overlap_accepts = ((intersection & a) == a) or ((intersection & b) == b)
            if left_accepts and right_accepts and not overlap_accepts:
                covered |= 1 << index
        if covered:
            covers.add(covered)
            max_pair_coverage = max(max_pair_coverage, covered.bit_count())
    return exact_cover_number(covers, target), max_pair_coverage


def main() -> None:
    n = 6
    words = [w for w in range(1 << n) if w.bit_count() == 2]
    anchors = [a for a in range(1 << n) if a.bit_count() <= 1]
    partitions = [
        mask for mask in range(1 << n)
        if mask.bit_count() == n // 2 and (mask & 1)
    ]
    trials = 500
    for mode in ("fixed", "anchor_dependent"):
        rng = random.Random(20260924 + (mode == "anchor_dependent"))
        histogram: dict[int, int] = {}
        max_cover_seen = 0
        max_pair_seen = 0
        min_pair_seen = len(anchors)
        best_example = None
        for _ in range(trials):
            minima = []
            punctures = []
            for anchor in anchors:
                left_block = 0b000111 if mode == "fixed" else rng.choice(partitions)
                right_block = ((1 << n) - 1) ^ left_block
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
                assert left.bit_count() >= 3 and right.bit_count() >= 3
                left_points = [i for i in range(len(words)) if (left >> i) & 1]
                right_points = [i for i in range(len(words)) if (right >> i) & 1]
                x, y = rng.choice(left_points), rng.choice(right_points)
                punctures.append((x, y))
                left_minimum = left & ~(1 << x)
                right_minimum = right & ~(1 << y)
                for coordinate in range(n):
                    literal = sum(
                        1 << index for index, word in enumerate(words)
                        if ((word >> coordinate) & 1) == ((anchor >> coordinate) & 1)
                    )
                    witness = left_minimum if (left_block >> coordinate) & 1 else right_minimum
                    assert witness & ~literal == 0
                minima.append((left_minimum, right_minimum))
            # The witnesses remain nonempty, disjoint, and anchored.
            assert all(a and b and not (a & b) for a, b in minima)
            cover, pair_coverage = evaluate(minima)
            histogram[cover] = histogram.get(cover, 0) + 1
            if cover > max_cover_seen:
                max_cover_seen = cover
                best_example = punctures
            max_pair_seen = max(max_pair_seen, pair_coverage)
            min_pair_seen = min(min_pair_seen, pair_coverage)

        print(
            f"mode={mode}; n={n}; |U|={len(words)}; anchors={len(anchors)}; "
            f"trials={trials}; cover_histogram={dict(sorted(histogram.items()))}; "
            f"largest_cover={max_cover_seen}; pair_coverage_range="
            f"[{min_pair_seen},{max_pair_seen}]"
        )
        if best_example is not None:
            print(f"sample_punctures_at_largest_cover={best_example}")


if __name__ == "__main__":
    main()
