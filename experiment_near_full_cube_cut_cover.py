"""Verify logarithmic cut covers for the weight-at-most-(n-2) toy."""

from __future__ import annotations

from experiment_relay_proof_contexts import direct_carrier_closure


def construct(n: int):
    assert n >= 2
    anchors = tuple(x for x in range(1 << n) if x.bit_count() <= n - 2)
    universe = tuple(x for x in range(1 << n) if x.bit_count() >= n - 1)
    zero_slices = tuple(
        frozenset(x for x in universe if ((x >> i) & 1) == 0)
        for i in range(n)
    )
    cut_count = (n - 1).bit_length()
    pairs = []
    for t in range(cut_count):
        left_coords = [i for i in range(n) if ((i >> t) & 1) == 0]
        right_coords = [i for i in range(n) if ((i >> t) & 1) == 1]
        left = frozenset().union(*(zero_slices[i] for i in left_coords))
        right = frozenset().union(*(zero_slices[i] for i in right_coords))
        pairs.append((left, right))
    return anchors, universe, tuple(pairs)


def verify(n: int) -> None:
    anchors, universe, pairs = construct(n)
    all_ones = (1 << n) - 1
    high_single_zero_points = [all_ones ^ (1 << i) for i in range(n)]
    signatures = [
        tuple(point in endpoint for pair in pairs for endpoint in pair)
        for point in high_single_zero_points
    ]
    assert len(set(signatures)) == n
    carriers = sorted(
        {frozenset()} | {x for pair in pairs for x in pair}
        | {left & right for left, right in pairs},
        key=lambda x: (len(x), tuple(sorted(x))),
    )
    points = set(anchors) | set(universe)
    for anchor in sorted(points):
        generators = [
            frozenset(x for x in universe
                      if ((x >> i) & 1) == ((anchor >> i) & 1))
            for i in range(n)
        ]
        closure = direct_carrier_closure(
            generators, pairs, carriers, (1 << n) - 1
        )
        assert (frozenset() in closure) == (anchor in anchors), (
            n, anchor, anchor in anchors
        )
    assert all(not (left & right) for left, right in pairs)
    print(
        f"n={n}; low_weight<=n-2; anchors={len(anchors)}; "
        f"high_points={len(universe)}; rules={(n - 1).bit_length()}; "
        f"distinct_single_zero_endpoint_signatures={len(set(signatures))}; "
        "all_low_and_high_closures_verified=True"
    )


def main() -> None:
    for n in range(2, 13):
        verify(n)


if __name__ == "__main__":
    main()
