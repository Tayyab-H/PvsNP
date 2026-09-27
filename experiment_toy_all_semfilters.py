"""Exact tiny-universe cover computation for all semi-filters above anchors.

Here ``U`` consists of the 3-bit strings of weight at least 2 (four points),
and anchors are the strings of weight at most 1. We enumerate every monotone
family F of subsets of U with empty set excluded and U included, retain all
filters above each anchor, and compute the minimum list of pairs covering
that complete finite family.
"""

from itertools import product


N_BITS = 3
U_WORDS = [x for x in range(1 << N_BITS) if x.bit_count() >= 2]
ANCHORS = [x for x in range(1 << N_BITS) if x.bit_count() <= 1]
M = len(U_WORDS)
SET_COUNT = 1 << M
FULL_U = SET_COUNT - 1


def is_upset(family):
    if family & 1:  # the empty subset of U is included
        return False
    if not ((family >> FULL_U) & 1):
        return False
    for s in range(SET_COUNT):
        if (family >> s) & 1:
            for t in range(SET_COUNT):
                if (s & t) == s and not ((family >> t) & 1):
                    return False
    return True


def upsets():
    return [f for f in range(1 << SET_COUNT) if is_upset(f)]


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


def family_has(family, subset):
    return bool((family >> subset) & 1)


def forced_closure(anchor, pairs):
    """Least upward family above the anchor preserving every supplied pair."""
    current = set(anchor_generators(anchor))

    def add_supersets(members):
        expanded = set(members)
        for s in members:
            for t in range(SET_COUNT):
                if (s & t) == s:
                    expanded.add(t)
        return expanded

    current = add_supersets(current)
    while True:
        additions = {
            e & h for e, h in pairs
            if e in current and h in current
        }
        expanded = add_supersets(current | additions)
        if expanded == current:
            return current
        current = expanded


def minimum_cover(coverage, target):
    # Remove zero and dominated coverage sets; a superset is always at least
    # as useful as a subset in an unweighted set-cover instance.
    masks = sorted(set(mask for mask in coverage if mask), key=int.bit_count, reverse=True)
    masks = [mask for i, mask in enumerate(masks)
             if not any(mask != other and (mask & other) == mask
                        for other in masks[:i])]

    # Iterative deepening DFS with a maximum-gain lower bound.
    def search(chosen, covered, limit):
        if covered == target:
            return chosen
        if len(chosen) >= limit:
            return None
        remaining = target & ~covered
        max_gain = max((mask & remaining).bit_count() for mask in masks)
        if max_gain == 0:
            return None
        lower = (remaining.bit_count() + max_gain - 1) // max_gain
        if len(chosen) + lower > limit:
            return None
        # Branch on the uncovered filter with the fewest covering masks.
        bits = [1 << i for i in range(target.bit_length()) if (remaining >> i) & 1]
        pivot = min(bits, key=lambda b: sum(bool(mask & b) for mask in masks))
        choices = [mask for mask in masks if mask & pivot]
        choices.sort(key=lambda mask: (mask & remaining).bit_count(), reverse=True)
        for mask in choices:
            result = search(chosen + [mask], covered | mask, limit)
            if result is not None:
                return result
        return None

    for limit in range(1, len(masks) + 1):
        result = search([], 0, limit)
        if result is not None:
            return result
    return None


def main():
    all_upsets = upsets()
    filters = []
    filters_by_anchor = {}
    for a in ANCHORS:
        generators = anchor_generators(a)
        accepted = [f for f in all_upsets
                    if all(family_has(f, g) for g in generators)]
        filters_by_anchor[a] = accepted
        filters.extend((a, f) for f in accepted)

    pair_coverages = []
    pairs = list(product(range(SET_COUNT), repeat=2))
    for e, h in pairs:
        inter = e & h
        coverage = 0
        for i, (_a, family) in enumerate(filters):
            if family_has(family, e) and family_has(family, h) \
                    and not family_has(family, inter):
                coverage |= 1 << i
        pair_coverages.append(coverage)

    # Check the exact closure characterization for every pair and anchor:
    # a pair violates every filter above a iff its preservation closure
    # forces the forbidden empty set.
    for pair_index, (e, h) in enumerate(pairs):
        coverage = pair_coverages[pair_index]
        for anchor in ANCHORS:
            index = next(i for i, record in enumerate(filters)
                         if record[0] == anchor)
            count = len(filters_by_anchor[anchor])
            direct = all((coverage >> i) & 1
                         for i in range(index, index + count))
            closure_forces_empty = 0 in forced_closure(anchor, [(e, h)])
            assert direct == closure_forces_empty

    target = (1 << len(filters)) - 1
    solution = minimum_cover(pair_coverages, target)
    max_coverage = max(pair_coverages, key=int.bit_count)
    assert max_coverage != target  # certifies that no one-pair cover exists
    if solution:
        combined = 0
        for mask in solution:
            combined |= mask
        assert combined == target
    print(f"truth_table_bits={N_BITS}; |U|={M}; anchors={len(ANCHORS)}")
    print(f"all_upsets={len(all_upsets)}; anchored_semfilters={len(filters)}")
    print(f"closure_criterion_verified_for={len(pairs)*len(ANCHORS)} pair-anchor cases")
    print(f"pair_universe={len(pairs)}; max_filters_hit_by_one_pair={max_coverage.bit_count()}; "
          f"min_cover={len(solution) if solution else 'none'}")
    if solution:
        for mask in solution:
            index = pair_coverages.index(mask)
            e, h = pairs[index]
            e_words = [U_WORDS[i] for i in range(M) if (e >> i) & 1]
            h_words = [U_WORDS[i] for i in range(M) if (h >> i) & 1]
            print(f"  E={e_words}; H={h_words}; filters_hit={mask.bit_count()}")
        missed = [i for i in range(len(filters)) if not (solution[0] & (1 << i))]
        print("  filters_missed_by_first_pair=" + repr([
            {"anchor": ANCHORS[filters[i][0]], "family_mask": filters[i][1]}
            for i in missed
        ]))


if __name__ == "__main__":
    main()
