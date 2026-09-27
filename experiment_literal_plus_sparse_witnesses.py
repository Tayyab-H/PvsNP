"""Exact endpoint-cover search for literal filters plus random minimal witnesses."""

from __future__ import annotations

import random
from collections import Counter
from itertools import combinations


N = 4
UNIVERSE = [x for x in range(1 << N) if x.bit_count() == 2]
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 1]
U_SIZE = len(UNIVERSE)


def literal_generators(anchor: int) -> list[int]:
    out = []
    for bit in range(N):
        mask = 0
        for i, point in enumerate(UNIVERSE):
            if ((point >> bit) & 1) == ((anchor >> bit) & 1):
                mask |= 1 << i
        out.append(mask)
    return out


def minimal_extra_candidates(size: int, literals: list[int]) -> list[int]:
    candidates = []
    for indices in combinations(range(U_SIZE), size):
        witness = sum(1 << i for i in indices)
        # At equal size, excluding an exact duplicate makes this a distinct
        # inclusion-minimal witness alongside the literal generators.
        if size == 3 and witness in literals:
            continue
        candidates.append(witness)
    return candidates


def exact_cover_number(
    generators: list[list[int]],
) -> tuple[int, int, tuple[int, int] | None, tuple[tuple[int, int], tuple[int, int]] | None]:
    endpoint_count = 1 << U_SIZE
    accepted = [
        [any((witness & endpoint) == witness for witness in family)
         for endpoint in range(endpoint_count)]
        for family in generators
    ]
    anchor_count = len(generators)
    pair_covers: set[int] = set()
    pair_endpoints: dict[int, tuple[int, int]] = {}
    max_coverage = 0
    full_pair = None
    for left in range(endpoint_count):
        for right in range(endpoint_count):
            common = left & right
            cover = 0
            for a in range(anchor_count):
                if accepted[a][left] and accepted[a][right] and not accepted[a][common]:
                    cover |= 1 << a
            if cover:
                pair_covers.add(cover)
                pair_endpoints.setdefault(cover, (left, right))
                max_coverage = max(max_coverage, cover.bit_count())
                if cover == (1 << anchor_count) - 1 and full_pair is None:
                    full_pair = (left, right)

    target = (1 << anchor_count) - 1
    dp = [anchor_count + 1] * (target + 1)
    dp[0] = 0
    for old in range(target + 1):
        for cover in pair_covers:
            new = old | cover
            dp[new] = min(dp[new], dp[old] + 1)
    two_pair_cover = None
    if dp[target] == 2:
        for first in pair_covers:
            second = target ^ first
            if second in pair_endpoints:
                two_pair_cover = (pair_endpoints[first], pair_endpoints[second])
                break
    return dp[target], max_coverage, full_pair, two_pair_cover


def optimized_one_extra_search(samples: int = 100_000) -> None:
    """Search witness assignments that minimize the best single-pair coverage."""
    endpoint_count = 1 << U_SIZE
    endpoints = [(left, right) for left in range(endpoint_count)
                 for right in range(endpoint_count)]
    candidates = [sum(1 << i for i in indices)
                  for indices in combinations(range(U_SIZE), 2)]
    coverage_bits: list[list[int]] = []

    for anchor in ANCHORS:
        literals = literal_generators(anchor)
        base = [any((witness & endpoint) == witness for witness in literals)
                for endpoint in range(endpoint_count)]
        choices = []
        for extra in candidates:
            bits = 0
            for pair_index, (left, right) in enumerate(endpoints):
                common = left & right
                left_ok = base[left] or (extra & left) == extra
                right_ok = base[right] or (extra & right) == extra
                common_ok = base[common] or (extra & common) == extra
                if left_ok and right_ok and not common_ok:
                    bits |= 1 << pair_index
            choices.append(bits)
        coverage_bits.append(choices)

    rng = random.Random(20260925)
    best_cap = len(ANCHORS) + 1
    best_choice = None
    pair_universe = (1 << len(endpoints)) - 1
    for _ in range(samples):
        choice = [rng.randrange(len(candidates)) for _ in ANCHORS]
        intersections = [0] * (1 << len(ANCHORS))
        intersections[0] = pair_universe
        cap = 0
        for subset in range(1, 1 << len(ANCHORS)):
            low = subset & -subset
            anchor_index = low.bit_length() - 1
            intersections[subset] = (
                intersections[subset ^ low] & coverage_bits[anchor_index][choice[anchor_index]]
            )
            if intersections[subset]:
                cap = max(cap, subset.bit_count())
        if cap < best_cap:
            best_cap = cap
            best_choice = choice
            if cap == 1:
                break

    assert best_choice is not None
    chosen = [candidates[i] for i in best_choice]
    generators = [literal_generators(a) + [w] for a, w in zip(ANCHORS, chosen)]
    exact, measured_cap, _, decomposition = exact_cover_number(generators)
    assert decomposition is not None if exact == 2 else True
    if decomposition is not None:
        two_pair_endpoints = [
            (
                [UNIVERSE[i] for i in range(U_SIZE) if left >> i & 1],
                [UNIVERSE[i] for i in range(U_SIZE) if right >> i & 1],
            )
            for left, right in decomposition
        ]
    else:
        two_pair_endpoints = None
    print(
        f"optimized_one_extra_search: samples={samples}; best_max_single_pair="
        f"{best_cap}/{len(ANCHORS)}; exact_cover={exact}; "
        f"anchor_specific_extra_pairs="
        f"{[[UNIVERSE[i] for i in range(U_SIZE) if w >> i & 1] for w in chosen]}; "
        f"verified_max_single_pair={measured_cap}; two_pair_cover={two_pair_endpoints}"
    )


def run(trials: int = 100) -> None:
    rng = random.Random(20260924)
    histograms: dict[tuple[int, int], Counter[int]] = {
        (size, count): Counter() for size in (2, 3) for count in (1, 2, 3)
    }
    caps_by_cover: dict[tuple[int, int], dict[int, Counter[int]]] = {
        (size, count): {} for size in (2, 3) for count in (1, 2, 3)
    }
    max_seen = {(size, count): 0 for size in (2, 3) for count in (1, 2, 3)}

    for size in (2, 3):
        for count in (1, 2, 3):
            first_family = None
            first_pair = None
            hard_example = None
            for _ in range(trials):
                generators = []
                for anchor in ANCHORS:
                    literals = literal_generators(anchor)
                    extras = rng.sample(minimal_extra_candidates(size, literals), count)
                    generators.append(list(dict.fromkeys(literals + extras)))
                if first_family is None:
                    first_family = generators
                cover, pair_cap, pair, two_pairs = exact_cover_number(generators)
                if first_pair is None:
                    first_pair = pair
                if cover == 2 and hard_example is None:
                    hard_example = (generators, pair_cap, two_pairs)
                histograms[(size, count)][cover] += 1
                caps_by_cover[(size, count)].setdefault(cover, Counter())[pair_cap] += 1
                max_seen[(size, count)] = max(max_seen[(size, count)], pair_cap)

            assert first_family is not None and first_pair is not None
            left, right = first_pair
            common = left & right
            print(
                f"extra_size={size}; count={count}; sample_E="
                f"{[UNIVERSE[i] for i in range(U_SIZE) if left >> i & 1]}; "
                f"sample_H={[UNIVERSE[i] for i in range(U_SIZE) if right >> i & 1]}; "
                f"sample_intersection="
                    f"{[UNIVERSE[i] for i in range(U_SIZE) if common >> i & 1]}"
                )
            if hard_example is not None:
                family, cap, decomposition = hard_example
                print(f"  first_cover_two_case: largest_single_pair={cap}/5")
                assert decomposition is not None
                for E, H in decomposition:
                    mask = 0
                    for a, gens in enumerate(family):
                        if (any((g & E) == g for g in gens)
                                and any((g & H) == g for g in gens)
                                and not any((g & E & H) == g for g in gens)):
                            mask |= 1 << a
                    print(
                        f"    E={[UNIVERSE[i] for i in range(U_SIZE) if E >> i & 1]}; "
                        f"H={[UNIVERSE[i] for i in range(U_SIZE) if H >> i & 1]}; "
                        f"covered_anchors={[ANCHORS[a] for a in range(len(ANCHORS)) if mask >> a & 1]}"
                    )

    print(f"universe={UNIVERSE}; anchors={ANCHORS}; endpoint_pairs={1 << (2 * U_SIZE)}")
    for size in (2, 3):
        for count in (1, 2, 3):
            print(
                f"extra_minimal_witnesses_per_anchor={count}; witness_size={size}; "
                f"exact_cover_histogram={dict(sorted(histograms[(size, count)].items()))}; "
                f"single_pair_caps_by_cover="
                f"{ {cover: dict(sorted(caps.items())) for cover, caps in caps_by_cover[(size, count)].items()} }; "
                f"largest_single_pair_coverage={max_seen[(size, count)]}/{len(ANCHORS)}"
            )


if __name__ == "__main__":
    run()
    optimized_one_extra_search()
