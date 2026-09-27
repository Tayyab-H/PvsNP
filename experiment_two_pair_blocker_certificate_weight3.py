"""Find a witness-independent 2-pair cover certificate on the toy shell.

For N=5, U={x:|x|=3}, and anchors |a|<=2, search for two endpoint pairs
which each are accepted via literals for every anchor, whose intersections
contain no literal generator and share fewer than two universe points. Such
a pair of intersections avoids every possible single 2-point special witness
per anchor, proving a universal two-pair cover for all 45^16 assignments.
"""

from __future__ import annotations


N = 5
UNIVERSE = [x for x in range(1 << N) if x.bit_count() == 3]
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 2]
FULL_ANCHORS = (1 << len(ANCHORS)) - 1


def literal_generators(anchor: int) -> list[int]:
    return [
        sum(1 << i for i, point in enumerate(UNIVERSE)
            if ((point >> bit) & 1) == ((anchor >> bit) & 1))
        for bit in range(N)
    ]


def endpoint_literal_mask(endpoint: int) -> int:
    mask = 0
    for anchor_index, anchor in enumerate(ANCHORS):
        if any((generator & endpoint) == generator
               for generator in literal_generators(anchor)):
            mask |= 1 << anchor_index
    return mask


def point_list(mask: int) -> list[int]:
    return [UNIVERSE[i] for i in range(len(UNIVERSE)) if mask >> i & 1]


def main() -> None:
    endpoints = range(1 << len(UNIVERSE))
    literal_masks = [endpoint_literal_mask(endpoint) for endpoint in endpoints]
    universal = [endpoint for endpoint in endpoints
                 if literal_masks[endpoint] == FULL_ANCHORS]
    safe_intersections: dict[int, tuple[int, int]] = {}
    for left in universal:
        for right in universal:
            common = left & right
            if literal_masks[common] == 0:
                safe_intersections.setdefault(common, (left, right))

    certificate = None
    for first, pair1 in safe_intersections.items():
        for second, pair2 in safe_intersections.items():
            if (first & second).bit_count() < 2:
                certificate = (first, pair1, second, pair2)
                break
        if certificate is not None:
            break

    if certificate is None:
        intersections = list(safe_intersections)
        min_overlap = min(
            ((a & b).bit_count() for i, a in enumerate(intersections)
             for b in intersections[i + 1:]),
            default=None,
        )
        print(
            f"N={N}; |U|={len(UNIVERSE)}; anchors={len(ANCHORS)}; "
            f"universal_literal_endpoints={len(universal)}; "
            f"safe_literal_intersections={len(safe_intersections)}; "
            f"minimum_pairwise_safe_intersection_overlap={min_overlap}; "
            f"witness_independent_two_pair_certificate=NOT_FOUND"
        )
        return
    first, (e1, h1), second, (e2, h2) = certificate
    assert (first & second).bit_count() < 2
    for anchor in ANCHORS:
        assert all(any((g & endpoint) == g for g in literal_generators(anchor))
                   for endpoint in (e1, h1, e2, h2))
        assert not any((g & first) == g for g in literal_generators(anchor))
        assert not any((g & second) == g for g in literal_generators(anchor))

    print(
        f"N={N}; |U|={len(UNIVERSE)}; anchors={len(ANCHORS)}; "
        f"universal_literal_endpoints={len(universal)}; "
        f"safe_literal_intersections={len(safe_intersections)}"
    )
    print(
        f"pair1: E={point_list(e1)}; H={point_list(h1)}; "
        f"intersection={point_list(first)}"
    )
    print(
        f"pair2: E={point_list(e2)}; H={point_list(h2)}; "
        f"intersection={point_list(second)}"
    )
    print(f"common_intersection={point_list(first & second)}; PASS")
    print(
        "Therefore, for every assignment of one 2-point special witness per "
        "anchor, at least one of these two pairs covers each filter."
    )


if __name__ == "__main__":
    main()
