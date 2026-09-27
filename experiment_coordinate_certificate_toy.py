"""Exact toy check for coordinate-cylinder certificate semi-filters.

Universe: the weight-two strings in {0,1}^4.
Anchors: the weight-zero and weight-one strings.
For r=1 and r=2, enumerate all endpoint pairs and verify that one pair
covers every anchor-filter instance. This is only a small finite example.
"""

from itertools import combinations


N = 4
U_WORDS = [word for word in range(1 << N) if word.bit_count() == 2]
ANCHORS = [word for word in range(1 << N) if word.bit_count() <= 1]
SET_COUNT = 1 << len(U_WORDS)
FULL_U = SET_COUNT - 1


def certificate(anchor, coordinates):
    return sum(
        1 << index
        for index, word in enumerate(U_WORDS)
        if all(((word >> i) & 1) == ((anchor >> i) & 1)
               for i in coordinates)
    )


def anchored_filters(r):
    result = []
    for anchor in ANCHORS:
        certificates = [
            certificate(anchor, coordinates)
            for coordinates in combinations(range(N), r)
        ]
        assert all(certificates)
        family = 0
        for subset in range(SET_COUNT):
            if any((subset & cert) == cert for cert in certificates):
                family |= 1 << subset
        result.append(family)
    return result


def main():
    for r in (1, 2):
        filters = anchored_filters(r)
        full_anchor_mask = (1 << len(filters)) - 1
        max_coverage = 0
        full_covering_pair = None

        for left in range(SET_COUNT):
            for right in range(SET_COUNT):
                intersection = left & right
                covered = 0
                for index, family in enumerate(filters):
                    if (
                        ((family >> left) & 1)
                        and ((family >> right) & 1)
                        and not ((family >> intersection) & 1)
                    ):
                        covered |= 1 << index
                max_coverage = max(max_coverage, covered.bit_count())
                if covered == full_anchor_mask:
                    full_covering_pair = (left, right)
                    break
            if full_covering_pair is not None:
                break

        assert full_covering_pair is not None
        assert max_coverage == len(filters)
        print(f"PASS: r={r}; one pair covers all {len(filters)} "
              "anchor filters")


if __name__ == "__main__":
    main()
