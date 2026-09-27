"""Verify a universal pairwise relay upper bound for weight-one anchors.

On U={x: wt(x)>=2}, anchors are all a with wt(a)<=1. For every coordinate
pair {i,j}, C_ij={x: x_i=0 or x_j=0} contains a matching zero-slice for
every anchor. Intersecting all C_ij leaves only words of weight at most one,
so a relay chain of binom(n,2)-1 pair rules derives the empty set.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


def verify_dimension(n: int) -> None:
    if n < 3:
        raise ValueError("n must be at least three")
    anchors = [x for x in range(1 << n) if x.bit_count() <= 1]
    universe = set(range(1 << n)) - set(anchors)
    clauses = [
        {x for x in universe if ((x >> i) & 1) == 0 or ((x >> j) & 1) == 0}
        for i, j in combinations(range(n), 2)
    ]

    for anchor in anchors:
        generators = [
            {x for x in universe if ((x >> i) & 1) == ((anchor >> i) & 1)}
            for i in range(n)
        ]
        assert all(any(g <= clause for g in generators) for clause in clauses)

    running = set(universe)
    intersections = []
    for clause in clauses:
        running &= clause
        intersections.append(set(running))
    assert not intersections[-1]

    pair_rules = len(clauses) - 1
    assert pair_rules == comb(n, 2) - 1
    print(
        f"n={n}; anchors={len(anchors)}; universe={len(universe)}; "
        f"coordinate_pair_clauses={len(clauses)}; relay_rules={pair_rules}; "
        "verified_for_all_anchors=True"
    )


if __name__ == "__main__":
    for dimension in range(3, 11):
        verify_dimension(dimension)
