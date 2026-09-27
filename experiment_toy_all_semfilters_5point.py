"""Enumerate all semi-filters for a five-point threshold-promise toy model.

U is the set of 4-bit strings of weight at least 3 (five points); anchors
have weight at most 2. All upward-closed families on P(U) are generated from
their antichains of minimal members. The program finds all anchored filters,
exhaustively checks every pair, and searches exact one- and two-pair covers.
"""

from itertools import product


N_BITS = 4
U_WORDS = [x for x in range(1 << N_BITS) if x.bit_count() >= 3]
ANCHORS = [x for x in range(1 << N_BITS) if x.bit_count() <= 2]
M = len(U_WORDS)
SET_COUNT = 1 << M
FULL_U = SET_COUNT - 1


def antichains():
    elements = list(range(SET_COUNT))

    def visit(index, chosen):
        if index == len(elements):
            if chosen:
                yield tuple(chosen)
            return
        x = elements[index]
        yield from visit(index + 1, chosen)
        if x and all((x & y) != x and (x & y) != y for y in chosen):
            chosen.append(x)
            yield from visit(index + 1, chosen)
            chosen.pop()

    yield from visit(0, [])


def family_from_minima(minima):
    family = 0
    for superset in range(SET_COUNT):
        if any((superset & minimum) == minimum for minimum in minima):
            family |= 1 << superset
    return family


def anchor_generators(anchor):
    generators = []
    for bit in range(N_BITS):
        subset = 0
        for i, word in enumerate(U_WORDS):
            if ((word >> bit) & 1) == ((anchor >> bit) & 1):
                subset |= 1 << i
        assert subset
        generators.append(subset)
    return generators


def main():
    all_families = [family_from_minima(a) for a in antichains()]
    assert len(all_families) == 7579
    anchored = []
    for anchor in ANCHORS:
        generators = anchor_generators(anchor)
        anchored.extend((anchor, family) for family in all_families
                        if all((family >> g) & 1 for g in generators))

    pairs = list(product(range(SET_COUNT), repeat=2))
    coverage = []
    best_index = 0
    best_count = -1
    for pair_index, (e, h) in enumerate(pairs):
        inter = e & h
        cover = 0
        for i, (_anchor, family) in enumerate(anchored):
            if ((family >> e) & 1) and ((family >> h) & 1) and not ((family >> inter) & 1):
                cover |= 1 << i
        coverage.append(cover)
        count = cover.bit_count()
        if count > best_count:
            best_count, best_index = count, pair_index

    target = (1 << len(anchored)) - 1
    if best_count == len(anchored):
        min_cover = 1
        solution = [best_index]
    else:
        solution = None
        for i, first in enumerate(coverage):
            missing = target & ~first
            for j, second in enumerate(coverage):
                if (second & missing) == missing:
                    solution = [i, j]
                    break
            if solution:
                break
        min_cover = 2 if solution else None

    print(f"truth_table_bits={N_BITS}; |U|={M}; anchors={len(ANCHORS)}")
    print(f"all_valid_semfilters_on_U={len(all_families)}; anchored_filter_instances={len(anchored)}")
    print(f"pair_universe={len(pairs)}; max_filters_hit_by_one_pair={best_count}; "
          f"min_cover={'1' if min_cover == 1 else '2' if min_cover == 2 else '>=3'}")
    if solution:
        for i in solution:
            e, h = pairs[i]
            e_words = [format(U_WORDS[j], f"0{N_BITS}b") for j in range(M) if (e >> j) & 1]
            h_words = [format(U_WORDS[j], f"0{N_BITS}b") for j in range(M) if (h >> j) & 1]
            print(f"  E={e_words}; H={h_words}; filters_hit={coverage[i].bit_count()}")
            fully_hit_anchors = []
            for anchor in ANCHORS:
                indices = [j for j, (a, _f) in enumerate(anchored) if a == anchor]
                if all((coverage[i] >> j) & 1 for j in indices):
                    fully_hit_anchors.append(format(anchor, f"0{N_BITS}b"))
            print(f"    all_filters_for_anchors={fully_hit_anchors}")
        combined = 0
        for i in solution:
            combined |= coverage[i]
        assert combined == target


if __name__ == "__main__":
    main()
