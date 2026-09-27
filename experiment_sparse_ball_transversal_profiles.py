"""Compute anchor-wise high-free transversal profiles for the n=5 GL sample.

This is the inexpensive geometry-only side of
experiment_sparse_ball_basis_scramble_n5.py. It uses the exact same seeded
matrix sample and reports, for each anchor, the antichain of minimal coordinate
sets whose cylinder misses the high universe. No relay-cover claim is made.
"""

from __future__ import annotations

import random
from collections import Counter


N = 5
ANCHORS = tuple(x for x in range(1 << N) if x.bit_count() <= 2)
RNG = random.Random(20260924)


def apply(rows: tuple[int, ...], value: int) -> int:
    return sum(((row & value).bit_count() & 1) << i
               for i, row in enumerate(rows))


def is_invertible(rows: tuple[int, ...]) -> bool:
    return len({apply(rows, x) for x in range(1 << N)}) == (1 << N)


def sample_matrices(count: int) -> list[tuple[int, ...]]:
    selected: set[tuple[int, ...]] = {tuple(1 << i for i in range(N))}
    while len(selected) < count:
        rows = tuple(RNG.randrange(1 << N) for _ in range(N))
        if is_invertible(rows):
            selected.add(rows)
    return sorted(selected)


def minimal_transversals(anchor: int, universe: tuple[int, ...]) -> set[int]:
    good = []
    for coordinates in range(1 << N):
        if all(any(((x ^ anchor) >> i) & 1
                   for i in range(N) if (coordinates >> i) & 1)
               for x in universe):
            good.append(coordinates)
    return {
        q for q in good
        if not any(p != q and (p & q) == p for p in good)
    }


def main() -> None:
    for index, rows in enumerate(sample_matrices(6)):
        anchors = tuple(sorted(apply(rows, a) for a in ANCHORS))
        universe = tuple(x for x in range(1 << N) if x not in set(anchors))
        counts = []
        size_profiles = []
        for anchor in anchors:
            transversals = minimal_transversals(anchor, universe)
            counts.append(len(transversals))
            size_profiles.append(tuple(sorted({q.bit_count() for q in transversals})))
        print(
            f"sample={index}; rows={rows}; row_weights="
            f"{tuple(row.bit_count() for row in rows)}; anchors={anchors}; "
            f"minimal_transversal_counts={tuple(counts)}; "
            f"count_distribution={dict(sorted(Counter(counts).items()))}; "
            f"size_profiles={tuple(size_profiles)}"
        )


if __name__ == "__main__":
    main()
