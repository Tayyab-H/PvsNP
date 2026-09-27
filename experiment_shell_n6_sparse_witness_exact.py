"""Exact arbitrary-endpoint cover of a structured family on the 6-bit shell.

The universe is the 15 strings of weight two; each of seven anchors (weight
zero or one) receives all matching literal generators and one 2-point
minimal witness. The 2^30 ordered endpoint pairs are evaluated in NumPy
chunks so the search remains memory bounded.
"""

from __future__ import annotations

from itertools import combinations

import numpy as np


N = 6
UNIVERSE = [x for x in range(1 << N) if x.bit_count() == 2]
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 1]
ENDPOINT_COUNT = 1 << len(UNIVERSE)
BLOCK_ROWS = 128


def literal_generators(anchor: int) -> list[int]:
    return [
        sum(1 << i for i, point in enumerate(UNIVERSE)
            if ((point >> bit) & 1) == ((anchor >> bit) & 1))
        for bit in range(N)
    ]


def point_pair(points: tuple[int, int]) -> int:
    return sum(1 << UNIVERSE.index(point) for point in points)


def exact_cover() -> tuple[int, int, list[tuple[int, int, int]], int]:
    extras = {
        0: (3, 5),
        1: (9, 17),
        2: (6, 10),
        4: (5, 20),
        8: (18, 24),
        16: (17, 20),
        32: (33, 34),
    }
    endpoint_values = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    accepted = []
    for anchor in ANCHORS:
        base = np.zeros(ENDPOINT_COUNT, dtype=np.bool_)
        for literal in literal_generators(anchor):
            base |= (np.bitwise_and(endpoint_values, literal) == literal)
        extra = point_pair(extras[anchor])
        accepted.append(base | (np.bitwise_and(endpoint_values, extra) == extra))

    cover_examples: dict[int, tuple[int, int]] = {}
    max_pair = 0
    total_pairs = ENDPOINT_COUNT * ENDPOINT_COUNT
    for start in range(0, ENDPOINT_COUNT, BLOCK_ROWS):
        stop = min(start + BLOCK_ROWS, ENDPOINT_COUNT)
        left = np.repeat(np.arange(start, stop, dtype=np.uint16), ENDPOINT_COUNT)
        right = np.tile(endpoint_values, stop - start)
        common = np.bitwise_and(left, right)
        cover_code = np.zeros(left.size, dtype=np.uint8)
        for anchor_index, accept in enumerate(accepted):
            covers = accept[left] & accept[right] & ~accept[common]
            cover_code |= covers.astype(np.uint8) << anchor_index
        values = np.unique(cover_code)
        for raw in values:
            code = int(raw)
            if code == 0 or code in cover_examples:
                continue
            local = int(np.argmax(cover_code == raw))
            cover_examples[code] = (start + local // ENDPOINT_COUNT,
                                    local % ENDPOINT_COUNT)
        max_pair = max(max_pair, max(int(code).bit_count() for code in values))

    target = (1 << len(ANCHORS)) - 1
    dp = [len(ANCHORS) + 1] * (target + 1)
    predecessor: list[tuple[int, int] | None] = [None] * (target + 1)
    dp[0] = 0
    for old in range(target + 1):
        if dp[old] > len(ANCHORS):
            continue
        for code in cover_examples:
            new = old | code
            if dp[new] > dp[old] + 1:
                dp[new] = dp[old] + 1
                predecessor[new] = (old, code)

    decomposition = []
    state = target
    while state:
        step = predecessor[state]
        assert step is not None
        old, code = step
        left, right = cover_examples[code]
        decomposition.append((left, right, code))
        state = old
    return dp[target], max_pair, decomposition, len(cover_examples)


def endpoint_points(mask: int) -> list[int]:
    return [UNIVERSE[i] for i in range(len(UNIVERSE)) if mask >> i & 1]


def main() -> None:
    cover, max_pair, decomposition, distinct_patterns = exact_cover()
    print(
        f"N={N}; |U|={len(UNIVERSE)}; anchors={len(ANCHORS)}; "
        f"endpoint_pairs={ENDPOINT_COUNT**2}; exact_cover={cover}; "
        f"max_single_pair_coverage={max_pair}/{len(ANCHORS)}; "
        f"distinct_nonzero_pair_cover_masks={distinct_patterns}"
    )
    for left, right, code in decomposition:
        print(
            f"  E={endpoint_points(left)}; H={endpoint_points(right)}; "
            f"covered={[ANCHORS[i] for i in range(len(ANCHORS)) if code >> i & 1]}"
        )


if __name__ == "__main__":
    main()
