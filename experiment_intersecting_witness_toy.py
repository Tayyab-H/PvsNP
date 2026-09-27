"""Exhaustive toy search over pairwise-intersecting witness antichains.

The universe is the weight-two shell in {0,1}^4 and anchors are the four
weight-one strings. Each filter receives one two-point witness inside each
of its four literal generators. The witnesses are pairwise intersecting
with empty total intersection. All 81 possible selected families are
checked against every ordered endpoint pair.
"""

from itertools import combinations, product


N = 4
U_WORDS = [word for word in range(1 << N) if word.bit_count() == 2]
ANCHORS = [word for word in range(1 << N) if word.bit_count() == 1]
SET_COUNT = 1 << len(U_WORDS)
TARGET = (1 << len(ANCHORS)) - 1


def witness_options(anchor):
    per_coordinate = []
    for coordinate in range(N):
        literal_points = [
            index for index, word in enumerate(U_WORDS)
            if ((word >> coordinate) & 1)
            == ((anchor >> coordinate) & 1)
        ]
        per_coordinate.append([
            sum(1 << index for index in pair)
            for pair in combinations(literal_points, 2)
        ])

    options = []
    for certificates in product(*per_coordinate):
        if not all(
            left & right
            for left, right in combinations(certificates, 2)
        ):
            continue
        common = certificates[0]
        for certificate in certificates[1:]:
            common &= certificate
        if common == 0:
            options.append(certificates)
    return options


def filter_membership(certificates):
    return [
        any((subset & certificate) == certificate
            for certificate in certificates)
        for subset in range(SET_COUNT)
    ]


def has_one_pair_cover(config):
    membership = [filter_membership(certificates)
                  for certificates in config]
    for left in range(SET_COUNT):
        for right in range(SET_COUNT):
            intersection = left & right
            if all(
                membership[index][left]
                and membership[index][right]
                and not membership[index][intersection]
                for index in range(len(ANCHORS))
            ):
                return True
    return False


def main():
    options = [witness_options(anchor) for anchor in ANCHORS]
    assert all(len(anchor_options) == 3 for anchor_options in options)
    configs_checked = 0
    for config in product(*options):
        for certificates in config:
            common = certificates[0]
            for certificate in certificates[1:]:
                common &= certificate
            assert common == 0
        assert has_one_pair_cover(config)
        configs_checked += 1

    assert configs_checked == 81
    print(
        f"PASS: all {configs_checked} pairwise-intersecting witness "
        "families have a one-pair cover"
    )


if __name__ == "__main__":
    main()
