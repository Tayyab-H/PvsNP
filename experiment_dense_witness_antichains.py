"""Search dense random witness families inside anchor literal slices.

Each anchored semi-filter is the upward closure of one random dense subset
inside each literal generator. For every sample, all ordered endpoint pairs
are enumerated and the exact cover number of the selected five filters is
computed. This is a finite stress test, not an asymptotic lower bound.
"""

from itertools import combinations
import random


N = 4
U_WORDS = [word for word in range(1 << N) if word.bit_count() >= 2]
ANCHORS = [word for word in range(1 << N) if word.bit_count() <= 1]
SET_COUNT = 1 << len(U_WORDS)
TARGET = (1 << len(ANCHORS)) - 1
TRIALS = 20
SEED = 20260924


def literal_slices():
    result = []
    for anchor in ANCHORS:
        row = []
        for coordinate in range(N):
            row.append(sum(
                1 << index
                for index, word in enumerate(U_WORDS)
                if ((word >> coordinate) & 1)
                == ((anchor >> coordinate) & 1)
            ))
        result.append(row)
    return result


def exact_cover_size(cover_masks):
    reachable = {0}
    for depth in range(1, len(ANCHORS) + 1):
        next_reachable = {
            old | cover
            for old in reachable
            for cover in cover_masks
        }
        if TARGET in next_reachable:
            return depth
        reachable |= next_reachable
    return None


def one_trial(rng, slices):
    certificates = []
    for row in slices:
        anchor_certificates = []
        for generator in row:
            points = [
                index for index in range(len(U_WORDS))
                if (generator >> index) & 1
            ]
            chosen = [index for index in points if rng.random() < 0.5]
            if not chosen:
                chosen = [rng.choice(points)]
            anchor_certificates.append(sum(1 << index for index in chosen))
        unique = set(anchor_certificates)
        minimal = [
            cert for cert in unique
            if not any(other != cert and (other & cert) == other
                       for other in unique)
        ]
        certificates.append(minimal)

    # membership[W] is the bitset of filters containing W.
    membership = [0] * SET_COUNT
    for anchor_index, row in enumerate(certificates):
        anchor_bit = 1 << anchor_index
        for subset in range(SET_COUNT):
            if any((subset & cert) == cert for cert in row):
                membership[subset] |= anchor_bit

    cover_masks = set()
    max_pair_coverage = 0
    for left in range(SET_COUNT):
        left_members = membership[left]
        if not left_members:
            continue
        for right in range(SET_COUNT):
            covered = left_members & membership[right] & ~membership[left & right]
            covered &= TARGET
            if covered:
                cover_masks.add(covered)
                max_pair_coverage = max(
                    max_pair_coverage, covered.bit_count()
                )

    return exact_cover_size(cover_masks), max_pair_coverage


def main():
    rng = random.Random(SEED)
    slices = literal_slices()
    histogram = {}
    max_cover = 0
    worst_pair_coverage = len(ANCHORS)

    for _ in range(TRIALS):
        cover, pair_coverage = one_trial(rng, slices)
        histogram[cover] = histogram.get(cover, 0) + 1
        max_cover = max(max_cover, cover)
        worst_pair_coverage = min(worst_pair_coverage, pair_coverage)

    print(
        f"TRIALS={TRIALS}; N={N}; |U|={len(U_WORDS)}; "
        f"anchors={len(ANCHORS)}; seed={SEED}"
    )
    print(f"exact_cover_size_histogram={dict(sorted(histogram.items()))}")
    print(f"largest_cover_size_seen={max_cover}")
    print(f"smallest_max_pair_coverage_seen={worst_pair_coverage}/{len(ANCHORS)}")


if __name__ == "__main__":
    main()
