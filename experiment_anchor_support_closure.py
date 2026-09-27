"""Exhaustively cross-check the global anchor-support closure identity.

For a fixed pair list, this computes all per-anchor preservation closures in
two ways: directly over every subset of U, and jointly over just the endpoint
sets, pair intersections, and the empty set. Every ordered pair is checked in
the four-point and five-point toy geometries used in the project audit.
"""

from itertools import combinations, product
import random


def anchor_generators(words, anchor, n_bits):
    generators = []
    for bit in range(n_bits):
        subset = 0
        for i, word in enumerate(words):
            if ((word >> bit) & 1) == ((anchor >> bit) & 1):
                subset |= 1 << i
        assert subset
        generators.append(subset)
    return generators


def direct_closure(anchor_gens, pairs, set_count):
    closure = 0
    for generator in anchor_gens:
        for superset in range(set_count):
            if (superset & generator) == generator:
                closure |= 1 << superset
    while True:
        additions = 0
        for e, h in pairs:
            if ((closure >> e) & 1) and ((closure >> h) & 1):
                inter = e & h
                for superset in range(set_count):
                    if (superset & inter) == inter:
                        additions |= 1 << superset
        updated = closure | additions
        if updated == closure:
            return closure
        closure = updated


def global_support_closure(all_generators, pairs, set_count):
    anchors = len(all_generators)
    full_anchors = (1 << anchors) - 1
    relevant = {0}
    for e, h in pairs:
        relevant.update((e, h, e & h))
    relevant = sorted(relevant)
    supports = {s: 0 for s in relevant}

    for ai, generators in enumerate(all_generators):
        for s in relevant:
            if any((s & g) == g for g in generators):
                supports[s] |= 1 << ai

    while True:
        updated = supports.copy()
        for s in relevant:
            for e, h in pairs:
                if ((s & (e & h)) == (e & h)):
                    updated[s] |= supports[e] & supports[h]
        if updated == supports:
            return supports, relevant
        supports = updated


def check_geometry(n_bits, min_weight, max_anchor_weight):
    words = [x for x in range(1 << n_bits) if x.bit_count() >= min_weight]
    anchors = [x for x in range(1 << n_bits)
               if x.bit_count() <= max_anchor_weight]
    set_count = 1 << len(words)
    all_generators = [anchor_generators(words, a, n_bits) for a in anchors]
    universe = list(range(set_count))
    pairs = list(product(universe, repeat=2))

    rule_lists = [(pair,) for pair in pairs]
    if n_bits == 3:
        rule_lists.extend(combinations(pairs, 2))
    else:
        rng = random.Random(20260923)
        for _ in range(2048):
            rule_lists.append(tuple(rng.sample(pairs, rng.randint(2, 5))))

    for rules in rule_lists:
        supports, relevant = global_support_closure(
            all_generators, rules, set_count
        )
        for ai, generators in enumerate(all_generators):
            direct = direct_closure(generators, rules, set_count)
            for subset in relevant:
                direct_has = (direct >> subset) & 1
                global_has = (supports[subset] >> ai) & 1
                assert direct_has == global_has, (
                    n_bits, rules, anchors[ai], subset, direct_has, global_has
                )

    print(f"bits={n_bits}; |U|={len(words)}; anchors={len(anchors)}; "
          f"ordered_pairs={len(pairs)}; rule_lists={len(rule_lists)}; "
          f"result=all checks pass")


def main():
    check_geometry(3, 2, 1)
    check_geometry(4, 3, 2)


if __name__ == "__main__":
    main()
