"""Minimax-search sparse witnesses, then exact-check the best families.

This explores one 2-point witness per filter on the 5-bit weight-three shell
(10 universe points, 16 anchors). The heuristic uses sampled endpoint pairs
only to choose constructions; every reported cover value is verified over
all 1,048,576 ordered endpoint pairs.
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
SAMPLES = 30_000
STARTS = 32
SWEEPS = 4


def literal_generators(anchor: int) -> list[int]:
    return [
        sum(1 << i for i, point in enumerate(UNIVERSE)
            if ((point >> bit) & 1) == ((anchor >> bit) & 1))
        for bit in range(N)
    ]


def exact_cover(witnesses: list[int], left: np.ndarray, right: np.ndarray,
                common: np.ndarray) -> tuple[int, int, int]:
    endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    cover_code = np.zeros(PAIR_COUNT, dtype=np.uint16)
    for anchor_index, (anchor, extra) in enumerate(zip(ANCHORS, witnesses)):
        accepted = np.zeros(ENDPOINT_COUNT, dtype=np.bool_)
        for literal in literal_generators(anchor):
            accepted |= (np.bitwise_and(endpoints, literal) == literal)
        accepted |= (np.bitwise_and(endpoints, extra) == extra)
        covers = accepted[left] & accepted[right] & ~accepted[common]
        cover_code |= covers.astype(np.uint16) << anchor_index

    masks = {int(x) for x in np.unique(cover_code) if int(x)}
    maximum = max(x.bit_count() for x in masks)
    target = (1 << len(ANCHORS)) - 1
    if target in masks:
        return 1, maximum, len(masks)

    has_superset = np.zeros(1 << len(ANCHORS), dtype=np.bool_)
    has_superset[list(masks)] = True
    all_masks = np.arange(1 << len(ANCHORS), dtype=np.uint32)
    for bit in range(len(ANCHORS)):
        no_bit = all_masks[(all_masks & (1 << bit)) == 0]
        has_superset[no_bit] |= has_superset[no_bit | (1 << bit)]
    if any(has_superset[target ^ mask] for mask in masks):
        return 2, maximum, len(masks)

    array = np.fromiter(masks, dtype=np.uint16)
    pair_unions = np.unique(np.bitwise_or(array[:, None], array[None, :]))
    if any(has_superset[target ^ int(union)] for union in pair_unions):
        return 3, maximum, len(masks)
    return 4, maximum, len(masks)  # verified cover number is at least four


def main() -> None:
    numpy_rng = np.random.default_rng(20260927)
    py_rng = random.Random(20260927)
    candidates = [sum(1 << i for i in pair)
                  for pair in combinations(range(U_SIZE), 2)]

    sample_left = numpy_rng.integers(0, ENDPOINT_COUNT, size=SAMPLES, dtype=np.uint16)
    sample_right = numpy_rng.integers(0, ENDPOINT_COUNT, size=SAMPLES, dtype=np.uint16)
    sample_common = np.bitwise_and(sample_left, sample_right)
    endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    coverage = np.zeros((len(ANCHORS), len(candidates), SAMPLES), dtype=np.bool_)

    for a, anchor in enumerate(ANCHORS):
        base = np.zeros(ENDPOINT_COUNT, dtype=np.bool_)
        for literal in literal_generators(anchor):
            base |= (np.bitwise_and(endpoints, literal) == literal)
        for c, extra in enumerate(candidates):
            accepted = base | (np.bitwise_and(endpoints, extra) == extra)
            coverage[a, c] = (
                accepted[sample_left]
                & accepted[sample_right]
                & ~accepted[sample_common]
            )

    ranked: dict[tuple[int, ...], tuple[int, int]] = {}
    for _ in range(STARTS):
        choice = [py_rng.randrange(len(candidates)) for _ in ANCHORS]
        counts = np.sum(coverage[np.arange(len(ANCHORS)), choice], axis=0, dtype=np.uint8)
        for _ in range(SWEEPS):
            changed = False
            for anchor_index in py_rng.sample(range(len(ANCHORS)), len(ANCHORS)):
                base_counts = counts - coverage[anchor_index, choice[anchor_index]].astype(np.uint8)
                best_score = (int(counts.max()), int(np.square(counts.astype(np.uint16)).sum()))
                best_choices = [choice[anchor_index]]
                for candidate_index in range(len(candidates)):
                    trial = base_counts + coverage[anchor_index, candidate_index].astype(np.uint8)
                    score = (int(trial.max()), int(np.square(trial.astype(np.uint16)).sum()))
                    if score < best_score:
                        best_score = score
                        best_choices = [candidate_index]
                    elif score == best_score:
                        best_choices.append(candidate_index)
                replacement = py_rng.choice(best_choices)
                if replacement != choice[anchor_index]:
                    choice[anchor_index] = replacement
                    counts = base_counts + coverage[anchor_index, replacement].astype(np.uint8)
                    changed = True
            if not changed:
                break
        score = (int(counts.max()), int(np.square(counts.astype(np.uint16)).sum()))
        ranked[tuple(choice)] = score

    best_candidates = sorted(ranked, key=lambda choice: ranked[choice])[:4]
    left = np.repeat(endpoints, ENDPOINT_COUNT)
    right = np.tile(endpoints, ENDPOINT_COUNT)
    common = np.bitwise_and(left, right)
    best_result = None
    for choice in best_candidates:
        witnesses = [candidates[index] for index in choice]
        cover, maximum, patterns = exact_cover(witnesses, left, right, common)
        result = (cover, maximum, patterns, choice)
        if best_result is None or (cover, -maximum) > (best_result[0], -best_result[1]):
            best_result = result
        if cover >= 3:
            break

    assert best_result is not None
    cover, maximum, patterns, choice = best_result
    chosen_points = [
        [UNIVERSE[i] for i in range(U_SIZE) if candidates[index] >> i & 1]
        for index in choice
    ]
    print(
        f"N={N}; |U|={U_SIZE}; anchors={len(ANCHORS)}; exact_pairs={PAIR_COUNT}; "
        f"sampled_pairs={SAMPLES}; starts={STARTS}; sweeps={SWEEPS}; "
        f"best_exact_cover={cover}; maximum_single_pair={maximum}/{len(ANCHORS)}; "
        f"distinct_cover_masks={patterns}"
    )
    print(f"selected_extra_witnesses={chosen_points}")
    print(
        "Note: sampling affected construction choice only; the reported exact cover "
        "was computed over every ordered endpoint pair."
    )


if __name__ == "__main__":
    main()
