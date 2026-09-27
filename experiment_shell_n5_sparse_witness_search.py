"""Search structured one-witness filters on the 5-bit weight-two shell.

Every candidate found by the greedy search is verified against all ordered
endpoint pairs in the 10-point universe. NumPy is used only to batch that
finite exact verification.
"""

from __future__ import annotations

import random
from itertools import combinations

import numpy as np


N = 5
UNIVERSE = [x for x in range(1 << N) if x.bit_count() == 2]
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 1]
U_SIZE = len(UNIVERSE)
ENDPOINT_COUNT = 1 << U_SIZE
PAIR_COUNT = ENDPOINT_COUNT * ENDPOINT_COUNT


def literal_generators(anchor: int) -> list[int]:
    return [
        sum(1 << i for i, point in enumerate(UNIVERSE)
            if ((point >> bit) & 1) == ((anchor >> bit) & 1))
        for bit in range(N)
    ]


def endpoint_pair_axes() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    left = np.repeat(endpoints, ENDPOINT_COUNT)
    right = np.tile(endpoints, ENDPOINT_COUNT)
    common = np.bitwise_and(left, right)
    return left, right, common


def packed_bits(array: np.ndarray) -> int:
    packed = np.packbits(array, bitorder="little")
    return int.from_bytes(packed.tobytes(), "little")


def prepare_pair_coverage(
    left: np.ndarray, right: np.ndarray, common: np.ndarray,
) -> tuple[list[list[int]], list[list[int]]]:
    extra_witnesses = [
        sum(1 << i for i in pair)
        for pair in combinations(range(U_SIZE), 2)
    ]
    all_endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    per_anchor: list[list[int]] = []
    for anchor in ANCHORS:
        literals = literal_generators(anchor)
        base = np.zeros(ENDPOINT_COUNT, dtype=np.bool_)
        for literal in literals:
            base |= (np.bitwise_and(all_endpoints, literal) == literal)

        candidate_coverages = []
        for extra in extra_witnesses:
            accepted = base | (np.bitwise_and(all_endpoints, extra) == extra)
            covers_pair = (
                accepted[left]
                & accepted[right]
                & ~accepted[common]
            )
            candidate_coverages.append(packed_bits(covers_pair))
        per_anchor.append(candidate_coverages)
    return per_anchor, extra_witnesses


def exact_cover_for_family(
    witness_choices: list[int], extra_witnesses: list[int],
    left: np.ndarray, right: np.ndarray, common: np.ndarray,
) -> tuple[int, int, list[tuple[int, int]]]:
    all_endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    coverage = np.zeros(PAIR_COUNT, dtype=np.uint8)
    for anchor_index, (anchor, witness_index) in enumerate(zip(ANCHORS, witness_choices)):
        base = np.zeros(ENDPOINT_COUNT, dtype=np.bool_)
        for literal in literal_generators(anchor):
            base |= (np.bitwise_and(all_endpoints, literal) == literal)
        extra = extra_witnesses[witness_index]
        accepted = base | (np.bitwise_and(all_endpoints, extra) == extra)
        covers_pair = accepted[left] & accepted[right] & ~accepted[common]
        coverage |= covers_pair.astype(np.uint8) << anchor_index

    cover_masks = {int(value) for value in np.unique(coverage) if int(value) != 0}
    target = (1 << len(ANCHORS)) - 1
    max_pair = max(mask.bit_count() for mask in cover_masks)
    dp = [len(ANCHORS) + 1] * (target + 1)
    dp[0] = 0
    predecessor: list[tuple[int, int] | None] = [None] * (target + 1)
    for old in range(target + 1):
        if dp[old] > len(ANCHORS):
            continue
        for cover in cover_masks:
            new = old | cover
            if dp[new] > dp[old] + 1:
                dp[new] = dp[old] + 1
                predecessor[new] = (old, cover)

    decomposition = []
    current = target
    while current:
        step = predecessor[current]
        assert step is not None
        old, cover = step
        endpoint_pair_index = int(np.flatnonzero(coverage == cover)[0])
        decomposition.append((endpoint_pair_index // ENDPOINT_COUNT,
                              endpoint_pair_index % ENDPOINT_COUNT))
        current = old
    return dp[target], max_pair, decomposition


def greedy_family(
    pair_coverage: list[list[int]], rng: random.Random,
) -> list[int]:
    remaining_pairs = (1 << PAIR_COUNT) - 1
    unchosen = set(range(len(ANCHORS)))
    chosen = [0] * len(ANCHORS)
    while unchosen and remaining_pairs:
        best = None
        best_count = PAIR_COUNT + 1
        tie_list = []
        for anchor_index in unchosen:
            for witness_index, coverage in enumerate(pair_coverage[anchor_index]):
                intersection = remaining_pairs & coverage
                count = intersection.bit_count()
                if count < best_count:
                    best_count = count
                    tie_list = [(anchor_index, witness_index, intersection)]
                elif count == best_count:
                    tie_list.append((anchor_index, witness_index, intersection))
        best = rng.choice(tie_list)
        anchor_index, witness_index, remaining_pairs = best
        chosen[anchor_index] = witness_index
        unchosen.remove(anchor_index)
    if unchosen:
        for anchor_index in unchosen:
            chosen[anchor_index] = rng.randrange(len(pair_coverage[anchor_index]))
    return chosen


def greedy_minimize_maxcap(
    pair_coverage: list[list[int]], rng: random.Random,
) -> tuple[list[int], int]:
    """Greedily choose witnesses to minimize the largest common covered subset."""
    order = list(range(len(ANCHORS)))
    rng.shuffle(order)
    selected: list[int | None] = [None] * len(ANCHORS)
    intersections = {0: (1 << PAIR_COUNT) - 1}
    max_cap = 0

    for anchor_index in order:
        best_score = len(ANCHORS) + 1
        best_tie = PAIR_COUNT + 1
        best_choices: list[tuple[int, int]] = []
        for witness_index, candidate_bits in enumerate(pair_coverage[anchor_index]):
            score = max_cap
            for subset, common_bits in intersections.items():
                if common_bits & candidate_bits:
                    score = max(score, subset.bit_count() + 1)
            full_key = (1 << len(order)) - 1
            prior_full = intersections.get(full_key)
            tie = ((prior_full & candidate_bits).bit_count()
                   if prior_full is not None else candidate_bits.bit_count())
            if score < best_score or (score == best_score and tie < best_tie):
                best_score = score
                best_tie = tie
                best_choices = [(witness_index, tie)]
            elif score == best_score and tie == best_tie:
                best_choices.append((witness_index, tie))
        witness_index, _ = rng.choice(best_choices)
        candidate_bits = pair_coverage[anchor_index][witness_index]
        old_items = list(intersections.items())
        for subset, common_bits in old_items:
            intersections[subset | (1 << anchor_index)] = common_bits & candidate_bits
        selected[anchor_index] = witness_index
        max_cap = best_score

    assert all(choice is not None for choice in selected)
    return [int(choice) for choice in selected], max_cap


def main(searches: int = 120) -> None:
    left, right, common = endpoint_pair_axes()
    pair_coverage, extra_witnesses = prepare_pair_coverage(left, right, common)
    rng = random.Random(20260926)
    best_choice = None
    best_exact_cover = 0
    best_cap = len(ANCHORS) + 1
    best_decomposition = []
    histogram: dict[int, int] = {}

    for trial in range(searches):
        choice = greedy_family(pair_coverage, rng)
        exact, cap, decomposition = exact_cover_for_family(
            choice, extra_witnesses, left, right, common
        )
        histogram[exact] = histogram.get(exact, 0) + 1
        if (exact, -cap) > (best_exact_cover, -best_cap):
            best_choice = choice
            best_exact_cover = exact
            best_cap = cap
            best_decomposition = decomposition
        if exact >= 3:
            break

    mincap_trials = 24
    mincap_best_cap = len(ANCHORS) + 1
    mincap_best_exact = 0
    for _ in range(mincap_trials):
        choice, predicted_cap = greedy_minimize_maxcap(pair_coverage, rng)
        exact, cap, decomposition = exact_cover_for_family(
            choice, extra_witnesses, left, right, common
        )
        if (exact, -cap) > (mincap_best_exact, -mincap_best_cap):
            mincap_best_exact = exact
            mincap_best_cap = cap
        if (exact, -cap) > (best_exact_cover, -best_cap):
            best_choice = choice
            best_exact_cover = exact
            best_cap = cap
            best_decomposition = decomposition
        if exact >= 3:
            break

    assert best_choice is not None
    selected = [
        [UNIVERSE[i] for i in range(U_SIZE) if extra_witnesses[w] >> i & 1]
        for w in best_choice
    ]
    print(
        f"N={N}; |U|={U_SIZE}; anchors={len(ANCHORS)}; "
        f"endpoint_pairs={PAIR_COUNT}; greedy_trials={trial + 1}; "
        f"best_exact_cover={best_exact_cover}; max_single_pair={best_cap}/{len(ANCHORS)}"
    )
    print(f"random_greedy_cover_histogram={histogram}")
    print(
        f"minimax_greedy_trials={mincap_trials}; best_exact_cover={mincap_best_exact}; "
        f"best_max_single_pair={mincap_best_cap}/{len(ANCHORS)}"
    )
    print(f"selected_extra_witnesses={selected}")
    for left_mask, right_mask in best_decomposition:
        print(
            f"  E={[UNIVERSE[i] for i in range(U_SIZE) if left_mask >> i & 1]}; "
            f"H={[UNIVERSE[i] for i in range(U_SIZE) if right_mask >> i & 1]}"
        )


if __name__ == "__main__":
    main()
