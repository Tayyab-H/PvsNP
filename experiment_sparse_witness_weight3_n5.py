"""Exact cover search for sparse witnesses on a larger constant-weight toy.

Universe: all 5-bit strings of weight three (10 points). Anchors: all strings
of weight at most two (16 points). Each filter contains every matching
literal generator and one anchor-specific 2-point minimal witness. Every
family is checked against all 1,048,576 ordered endpoint pairs.
"""

from __future__ import annotations

import random
from itertools import combinations

import numpy as np


N = 5
UNIVERSE = [x for x in range(1 << N) if x.bit_count() == 3]
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 2]
U_SIZE = len(UNIVERSE)
ENDPOINT_COUNT = 1 << U_SIZE
PAIR_COUNT = ENDPOINT_COUNT * ENDPOINT_COUNT


def literal_generators(anchor: int) -> list[int]:
    return [
        sum(1 << i for i, point in enumerate(UNIVERSE)
            if ((point >> bit) & 1) == ((anchor >> bit) & 1))
        for bit in range(N)
    ]


def exact_pair_cover(witnesses: list[int], left: np.ndarray, right: np.ndarray,
                     common: np.ndarray) -> tuple[int, int, int, tuple | None]:
    all_endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    accepted_by_anchor = []
    for anchor, extra in zip(ANCHORS, witnesses):
        accepted = np.zeros(ENDPOINT_COUNT, dtype=np.bool_)
        for literal in literal_generators(anchor):
            accepted |= (np.bitwise_and(all_endpoints, literal) == literal)
        accepted |= (np.bitwise_and(all_endpoints, extra) == extra)
        accepted_by_anchor.append(accepted)

    cover_code = np.zeros(PAIR_COUNT, dtype=np.uint16)
    for i, accepted in enumerate(accepted_by_anchor):
        covers = accepted[left] & accepted[right] & ~accepted[common]
        cover_code |= covers.astype(np.uint16) << i
    masks = {int(x) for x in np.unique(cover_code) if int(x)}
    maximum = max(mask.bit_count() for mask in masks)
    target = (1 << len(ANCHORS)) - 1
    if target in masks:
        return 1, maximum, len(masks), None

    has_superset = np.zeros(1 << len(ANCHORS), dtype=np.bool_)
    has_superset[list(masks)] = True
    all_masks = np.arange(1 << len(ANCHORS), dtype=np.uint32)
    for bit in range(len(ANCHORS)):
        without_bit = all_masks[(all_masks & (1 << bit)) == 0]
        has_superset[without_bit] |= has_superset[without_bit | (1 << bit)]

    # Two endpoint pairs cover all anchors iff one pair mask and a second
    # available pair mask jointly cover the target.
    if any(has_superset[target ^ mask] for mask in masks):
        best_mask = max(masks, key=int.bit_count)
        partner_mask = next(mask for mask in masks if (mask | best_mask) == target)
        best_index = int(np.argmax(cover_code == best_mask))
        partner_index = int(np.argmax(cover_code == partner_mask))
        endpoint_pairs = (
            (best_index // ENDPOINT_COUNT, best_index % ENDPOINT_COUNT, best_mask),
            (partner_index // ENDPOINT_COUNT, partner_index % ENDPOINT_COUNT, partner_mask),
        )
        return 2, maximum, len(masks), endpoint_pairs

    pair_unions = {a | b for a in masks for b in masks}
    if any(has_superset[target ^ union] for union in pair_unions):
        return 3, maximum, len(masks), None

    return 4, maximum, len(masks), None  # exact value is at least four


def main(trials: int = 80) -> None:
    endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    left = np.repeat(endpoints, ENDPOINT_COUNT)
    right = np.tile(endpoints, ENDPOINT_COUNT)
    common = np.bitwise_and(left, right)
    candidate_witnesses = [
        sum(1 << i for i in pair)
        for pair in combinations(range(U_SIZE), 2)
    ]
    rng = random.Random(20260926)
    histogram: dict[int, int] = {}
    max_seen: dict[int, int] = {}
    caps_by_cover: dict[int, dict[int, int]] = {}
    example = None
    for trial in range(trials):
        chosen = [rng.choice(candidate_witnesses) for _ in ANCHORS]
        cover, maximum, patterns, endpoint_pairs = exact_pair_cover(chosen, left, right, common)
        histogram[cover] = histogram.get(cover, 0) + 1
        max_seen[cover] = max(max_seen.get(cover, 0), maximum)
        if cover >= 3 and example is None:
            example = (trial, chosen, cover, maximum, patterns, endpoint_pairs)
        caps = caps_by_cover.setdefault(cover, {})
        caps[maximum] = caps.get(maximum, 0) + 1
        if cover == 2 and example is None:
            example = (trial, chosen, cover, maximum, patterns, endpoint_pairs)

    print(
        f"N={N}; |U|={U_SIZE}; anchors={len(ANCHORS)}; "
        f"endpoint_pairs={PAIR_COUNT}; random_families={trials}; "
        f"cover_histogram={histogram}; max_single_pair_by_cover={max_seen}; "
        f"single_pair_cap_counts={caps_by_cover}"
    )
    if example is not None:
        trial, chosen, cover, maximum, patterns, endpoint_pairs = example
        chosen_points = [
            [UNIVERSE[i] for i in range(U_SIZE) if witness >> i & 1]
            for witness in chosen
        ]
        print(
            f"first_nontrivial_cover: trial={trial}; cover={cover}; "
            f"max_single_pair={maximum}/{len(ANCHORS)}; "
            f"distinct_pair_cover_masks={patterns}; witnesses={chosen_points}"
        )
        if endpoint_pairs is not None:
            for left_mask, right_mask, mask in endpoint_pairs:
                print(
                    f"  E={[UNIVERSE[i] for i in range(U_SIZE) if left_mask >> i & 1]}; "
                    f"H={[UNIVERSE[i] for i in range(U_SIZE) if right_mask >> i & 1]}; "
                    f"covered={[ANCHORS[i] for i in range(len(ANCHORS)) if mask >> i & 1]}"
                )


if __name__ == "__main__":
    main()
