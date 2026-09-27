"""Exact cover search for cylinder-generated semi-filters on a tiny universe.

U is the set of 4-bit strings of Hamming weight at least 2. Anchors have
weight at most 1. For each anchor a and width k, F_a is generated upward
from every nonempty set {u in U : u[J] = a[J]} with 1 <= |J| <= k.

The script enumerates every ordered pair (E,H) and computes exactly which
filters it violates, then solves the resulting 5-element set-cover problem.
"""

from itertools import combinations


N_BITS = 4
U = [x for x in range(1 << N_BITS) if x.bit_count() >= 2]
ANCHORS = [x for x in range(1 << N_BITS) if x.bit_count() <= 1]
FULL_COVER = (1 << len(ANCHORS)) - 1


def generator_masks(anchor, width):
    out = set()
    coords = range(N_BITS)
    for r in range(1, width + 1):
        for fixed in combinations(coords, r):
            mask = 0
            for index, u in enumerate(U):
                if all(((u >> j) & 1) == ((anchor >> j) & 1) for j in fixed):
                    mask |= 1 << index
            if mask:
                out.add(mask)
    return sorted(out)


def membership_masks(width):
    all_sets = range(1 << len(U))
    memberships = []
    for anchor in ANCHORS:
        generators = generator_masks(anchor, width)
        memberships.append([
            any((w & g) == g for g in generators)
            for w in all_sets
        ])
    return memberships


def main():
    for width in range(1, N_BITS + 1):
        mem = membership_masks(width)
        coverage_masks = set()
        best_hit = -1
        best_pair = None
        for e in range(1 << len(U)):
            for h in range(1 << len(U)):
                inter = e & h
                covered = 0
                for a_idx in range(len(ANCHORS)):
                    if mem[a_idx][e] and mem[a_idx][h] and not mem[a_idx][inter]:
                        covered |= 1 << a_idx
                if covered:
                    coverage_masks.add(covered)
                    hit_count = covered.bit_count()
                    if hit_count > best_hit:
                        best_hit = hit_count
                        best_pair = (e, h, covered)

        # Dynamic program over the 2^|Y| possible subsets of filters.
        distance = [None] * (FULL_COVER + 1)
        distance[0] = 0
        predecessor = [None] * (FULL_COVER + 1)
        for state in range(FULL_COVER + 1):
            if distance[state] is None:
                continue
            for coverage in coverage_masks:
                nxt = state | coverage
                if distance[nxt] is None:
                    distance[nxt] = distance[state] + 1
                    predecessor[nxt] = (state, coverage)

        best = best_pair
        E = [U[i] for i in range(len(U)) if (best[0] >> i) & 1]
        H = [U[i] for i in range(len(U)) if (best[1] >> i) & 1]
        hit_anchors = [ANCHORS[i] for i in range(len(ANCHORS))
                       if (best[2] >> i) & 1]
        print(f"k={width}; |U|={len(U)}; anchors={len(ANCHORS)}; "
              f"distinct_nonzero_pair_covers={len(coverage_masks)}; "
              f"max_filters_hit={best_hit}; min_cover={distance[FULL_COVER]}")
        print(f"  max_pair E={E}, H={H}, hit_anchors={hit_anchors}")

        if distance[FULL_COVER] is not None:
            cover = []
            state = FULL_COVER
            while state:
                prev, mask = predecessor[state]
                cover.append(mask)
                state = prev
            print("  cover_masks=" + repr(list(reversed(cover))))


if __name__ == "__main__":
    main()
