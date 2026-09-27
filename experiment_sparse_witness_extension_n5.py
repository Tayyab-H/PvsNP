"""Extend a two-pair 4-bit witness design to a six-anchor weight-two shell."""

from __future__ import annotations

import random
from itertools import combinations


N = 5
UNIVERSE = [x for x in range(1 << N) if x.bit_count() == 2]
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 1]
U_SIZE = len(UNIVERSE)
ENDPOINT_COUNT = 1 << U_SIZE


def literal_generators(anchor: int) -> list[int]:
    result = []
    for bit in range(N):
        result.append(sum(
            1 << i for i, point in enumerate(UNIVERSE)
            if ((point >> bit) & 1) == ((anchor >> bit) & 1)
        ))
    return result


def witness_pair_mask(pair: tuple[int, int]) -> int:
    return sum(1 << UNIVERSE.index(point) for point in pair)


def exact_cover(generators: list[list[int]]) -> tuple[int, int, list[tuple[int, int, int]]]:
    accepted = [
        [any((g & endpoint) == g for g in family)
         for endpoint in range(ENDPOINT_COUNT)]
        for family in generators
    ]
    target = (1 << len(ANCHORS)) - 1
    pair_masks: set[int] = set()
    max_pair = 0
    examples: dict[int, tuple[int, int]] = {}
    for left in range(ENDPOINT_COUNT):
        for right in range(ENDPOINT_COUNT):
            common = left & right
            coverage = 0
            for a in range(len(ANCHORS)):
                if accepted[a][left] and accepted[a][right] and not accepted[a][common]:
                    coverage |= 1 << a
            if coverage:
                pair_masks.add(coverage)
                examples.setdefault(coverage, (left, right))
                max_pair = max(max_pair, coverage.bit_count())

    dp = [len(ANCHORS) + 1] * (target + 1)
    dp[0] = 0
    predecessor: list[tuple[int, int] | None] = [None] * (target + 1)
    for old in range(target + 1):
        for cover in pair_masks:
            new = old | cover
            if dp[new] > dp[old] + 1:
                dp[new] = dp[old] + 1
                predecessor[new] = (old, cover)
    cover_list = []
    current = target
    while current:
        step = predecessor[current]
        assert step is not None
        old, cover = step
        left, right = examples[cover]
        cover_list.append((left, right, cover))
        current = old
    return dp[target], max_pair, cover_list


def show_set(mask: int) -> list[int]:
    return [UNIVERSE[i] for i in range(U_SIZE) if mask >> i & 1]


def main() -> None:
    # The first five are the optimized 4-bit pattern, now viewed in the
    # 5-bit weight-two universe; the sixth extends it with {23,35}.
    extras = {
        0: (6, 9),
        1: (6, 9),
        2: (6, 10),
        4: (6, 12),
        8: (3, 10),
        16: (6, 24),
    }
    generators = []
    for anchor in ANCHORS:
        literals = literal_generators(anchor)
        extra = witness_pair_mask(extras[anchor])
        assert extra.bit_count() == 2
        assert all(g.bit_count() >= 4 for g in literals)
        generators.append(literals + [extra])

    cover, max_pair, decomposition = exact_cover(generators)
    print(
        f"n={N}; |U|={U_SIZE}; anchors={ANCHORS}; exact_cover={cover}; "
        f"maximum_single_pair_coverage={max_pair}/{len(ANCHORS)}; "
        f"endpoint_pairs={ENDPOINT_COUNT**2}"
    )
    print(f"special_pairs={extras}")
    for left, right, covered in decomposition:
        print(
            f"  E={show_set(left)}; H={show_set(right)}; "
            f"covered={[ANCHORS[i] for i in range(len(ANCHORS)) if covered >> i & 1]}"
        )

    rng = random.Random(20260925)
    random_histogram: dict[int, int] = {}
    random_max_pair = 0
    for _ in range(6):
        random_generators = []
        for anchor in ANCHORS:
            literals = literal_generators(anchor)
            pair = tuple(rng.sample(UNIVERSE, 2))
            random_generators.append(literals + [witness_pair_mask(pair)])
        random_cover, random_pair_cap, _ = exact_cover(random_generators)
        random_histogram[random_cover] = random_histogram.get(random_cover, 0) + 1
        random_max_pair = max(random_max_pair, random_pair_cap)
    print(
        f"six_random_one-extra_families: exact_cover_histogram="
        f"{dict(sorted(random_histogram.items()))}; "
        f"largest_single_pair_coverage={random_max_pair}/{len(ANCHORS)}"
    )


if __name__ == "__main__":
    main()
