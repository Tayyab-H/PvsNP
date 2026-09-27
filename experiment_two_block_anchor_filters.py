"""Check two-block anchored filters on constant-weight promise toys."""

from __future__ import annotations

import random
from itertools import product


def exact_cover_size(cover_masks: set[int], target: int) -> int:
    reachable = {0}
    for depth in range(1, target.bit_count() + 1):
        reachable = {old | cover for old in reachable for cover in cover_masks}
        if target in reachable:
            return depth
    raise AssertionError("every filter has a two-witness covering pair")


def analyze(n: int, words: list[int], anchors: list[int], choices: tuple[int, ...]):
    u_size = len(words)
    set_count = 1 << u_size
    target = (1 << len(anchors)) - 1
    filters = []
    for anchor, left_coords in zip(anchors, choices):
        right_coords = ((1 << n) - 1) ^ left_coords
        left_witness = sum(
            1 << idx for idx, word in enumerate(words)
            if all(((word >> k) & 1) == ((anchor >> k) & 1)
                   for k in range(n) if (left_coords >> k) & 1)
        )
        right_witness = sum(
            1 << idx for idx, word in enumerate(words)
            if all(((word >> k) & 1) == ((anchor >> k) & 1)
                   for k in range(n) if (right_coords >> k) & 1)
        )
        assert left_witness and right_witness
        for coordinate in range(n):
            literal = sum(
                1 << idx for idx, word in enumerate(words)
                if ((word >> coordinate) & 1) == ((anchor >> coordinate) & 1)
            )
            witness = left_witness if (left_coords >> coordinate) & 1 else right_witness
            assert witness & ~literal == 0
        filters.append((left_witness, right_witness))

    membership = [0] * set_count
    for index, (left_witness, right_witness) in enumerate(filters):
        bit = 1 << index
        for subset in range(set_count):
            if (
                (subset & left_witness) == left_witness
                or (subset & right_witness) == right_witness
            ):
                membership[subset] |= bit

    covers = set()
    max_pair_coverage = 0
    for left in range(set_count):
        left_members = membership[left]
        for right in range(set_count):
            covered = left_members & membership[right] & ~membership[left & right]
            covered &= target
            if covered:
                covers.add(covered)
                max_pair_coverage = max(max_pair_coverage, covered.bit_count())
    return exact_cover_size(covers, target), max_pair_coverage


def run_case(n: int, exhaustive: bool, sample_count: int = 0) -> None:
    words = [w for w in range(1 << n) if w.bit_count() == 2]
    anchors = [a for a in range(1 << n) if a.bit_count() <= 1]
    partitions = [
        mask for mask in range(1, 1 << n)
        if mask.bit_count() == n // 2
        and (n % 2 == 1 or mask & 1)
    ]
    all_choices = product(partitions, repeat=len(anchors))
    if exhaustive:
        assignments = list(all_choices)
    else:
        rng = random.Random(20260924 + n)
        assignments = [
            tuple(rng.choice(partitions) for _ in anchors)
            for _ in range(sample_count)
        ]

    histogram: dict[int, int] = {}
    largest_cover = 0
    max_pair_seen = 0
    for choices in assignments:
        cover, max_pair = analyze(n, words, anchors, choices)
        histogram[cover] = histogram.get(cover, 0) + 1
        largest_cover = max(largest_cover, cover)
        max_pair_seen = max(max_pair_seen, max_pair)

    print(
        f"n={n}; |U|={len(words)}; anchors={len(anchors)}; "
        f"assignments={len(assignments)}; exhaustive={exhaustive}; "
        f"cover_histogram={dict(sorted(histogram.items()))}; "
        f"largest_cover={largest_cover}; largest_pair_coverage_seen={max_pair_seen}"
    )


def main() -> None:
    run_case(n=4, exhaustive=True)
    run_case(n=5, exhaustive=False, sample_count=12)


if __name__ == "__main__":
    main()
