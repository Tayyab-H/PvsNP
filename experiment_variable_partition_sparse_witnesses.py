"""Exact cover search with anchor-dependent partitions and sparse witnesses."""

from __future__ import annotations

import random
from itertools import product


def cover_number(cover_masks: set[int], m: int) -> int:
    target = (1 << m) - 1
    dp = [m + 1] * (target + 1)
    dp[0] = 0
    for mask in range(target + 1):
        if dp[mask] == m + 1:
            continue
        for cover in cover_masks:
            new_mask = mask | cover
            if dp[new_mask] > dp[mask] + 1:
                dp[new_mask] = dp[mask] + 1
    return dp[target]


def exact_cover(filters: list[tuple[int, int]]) -> tuple[int, int]:
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

    return cover_number(cover_masks, m), max_coverage


def exact_literal_cover(
    words: list[int], anchors: list[int], filters: list[tuple[int, int]], n: int
) -> tuple[int, int]:
    literals = {
        (coordinate, value): sum(
            1 << index for index, word in enumerate(words)
            if ((word >> coordinate) & 1) == value
        )
        for coordinate in range(n)
        for value in (0, 1)
    }
    covers: set[int] = set()
    max_coverage = 0
    for (left_coordinate, left_value), (right_coordinate, right_value) in product(
        literals, repeat=2
    ):
        left = literals[(left_coordinate, left_value)]
        right = literals[(right_coordinate, right_value)]
        inter = left & right
        covered = 0
        for i, (a, b) in enumerate(filters):
            e_ok = (left & a) == a or (left & b) == b
            h_ok = (right & a) == a or (right & b) == b
            z_ok = (inter & a) == a or (inter & b) == b
            if e_ok and h_ok and not z_ok:
                covered |= 1 << i
        if covered:
            covers.add(covered)
            max_coverage = max(max_coverage, covered.bit_count())
    return cover_number(covers, len(anchors)), max_coverage


def main() -> None:
    rng = random.Random(20260924)
    n = 8
    anchors: list[int] = []
    for candidate in rng.sample(range(1 << n), 1 << n):
        if all((candidate ^ old).bit_count() >= 3 for old in anchors):
            anchors.append(candidate)
        if len(anchors) == 9:
            break
    anchor_set = set(anchors)
    words = [word for word in range(1 << n) if word not in anchor_set]
    trials = 35
    for left_size in (2, 3, 4):
        for witness_size in (2, 3):
            histogram: dict[int, int] = {}
            literal_histogram: dict[int, int] = {}
            min_max_pair_seen = len(anchors)
            literal_max_pair_seen = 0
            best_filters = None
            for _ in range(trials):
                filters = []
                for anchor in anchors:
                    while True:
                        left_coords = sum(1 << c for c in rng.sample(range(n), left_size))
                        right_coords = ((1 << n) - 1) ^ left_coords
                        left_points = [
                            idx for idx, word in enumerate(words)
                            if all(((word >> c) & 1) == ((anchor >> c) & 1)
                                   for c in range(n) if (left_coords >> c) & 1)
                        ]
                        right_points = [
                            idx for idx, word in enumerate(words)
                            if all(((word >> c) & 1) == ((anchor >> c) & 1)
                                   for c in range(n) if (right_coords >> c) & 1)
                        ]
                        if len(left_points) >= witness_size and len(right_points) >= witness_size:
                            break
                    a = sum(1 << idx for idx in rng.sample(left_points, witness_size))
                    b = sum(1 << idx for idx in rng.sample(right_points, witness_size))
                    assert a and b and not (a & b)
                    filters.append((a, b))
                cover, pair_max = exact_cover(filters)
                literal_cover, literal_pair_max = exact_literal_cover(words, anchors, filters, n)
                histogram[cover] = histogram.get(cover, 0) + 1
                literal_histogram[literal_cover] = literal_histogram.get(literal_cover, 0) + 1
                min_max_pair_seen = min(min_max_pair_seen, pair_max)
                literal_max_pair_seen = max(literal_max_pair_seen, literal_pair_max)
                if best_filters is None or (cover, -pair_max) > best_filters[0]:
                    best_filters = ((cover, -pair_max), filters)
            print(
                f"n={n}; |U|={len(words)}; anchors={len(anchors)}; "
                f"left_block={left_size}; right_block={n-left_size}; "
                f"witness_size={witness_size}; trials={trials}; "
                f"all_pairs_cover_histogram={dict(sorted(histogram.items()))}; "
                f"literal_pair_cover_histogram={dict(sorted(literal_histogram.items()))}; "
                f"smallest_max_all_pair_coverage={min_max_pair_seen}; "
                f"largest_literal_pair_coverage={literal_max_pair_seen}",
                flush=True,
            )


if __name__ == "__main__":
    main()
