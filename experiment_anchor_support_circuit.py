"""Check the firing-rule circuit representation of support closure.

For each sampled finite pair list, compute the closure directly and compare
it with the m-round circuit recurrence that tracks which listed pairs have
fired. This is a finite validation of the compilation used in Proposition
21.5 of the project audit.
"""

from itertools import combinations, product
import random


def generators(words, anchor, n_bits):
    result = []
    for bit in range(n_bits):
        subset = 0
        for i, word in enumerate(words):
            if ((word >> bit) & 1) == ((anchor >> bit) & 1):
                subset |= 1 << i
        assert subset
        result.append(subset)
    return result


def direct_empty(gens, rules, set_count):
    closure = 0
    for g in gens:
        for s in range(set_count):
            if (s & g) == g:
                closure |= 1 << s
    while True:
        added = 0
        for e, h in rules:
            if ((closure >> e) & 1) and ((closure >> h) & 1):
                k = e & h
                for s in range(set_count):
                    if (s & k) == k:
                        added |= 1 << s
        updated = closure | added
        if updated == closure:
            return bool(closure & 1)
        closure = updated


def firing_circuit_empty(gens, rules, set_count):
    intersections = [e & h for e, h in rules]
    fired = [False] * len(rules)

    def active(s, fired_flags):
        if any((s & g) == g for g in gens):
            return True
        return any(fired_flags[q] and (s & k) == k
                   for q, k in enumerate(intersections))

    for _ in range(len(rules)):
        next_fired = list(fired)
        for q, (e, h) in enumerate(rules):
            if active(e, fired) and active(h, fired):
                next_fired[q] = True
        fired = next_fired
    return active(0, fired)


def check_geometry(n_bits, min_weight, max_anchor_weight):
    words = [x for x in range(1 << n_bits) if x.bit_count() >= min_weight]
    anchors = [x for x in range(1 << n_bits)
               if x.bit_count() <= max_anchor_weight]
    set_count = 1 << len(words)
    all_gens = [generators(words, a, n_bits) for a in anchors]
    universe = list(range(set_count))
    pairs = list(product(universe, repeat=2))

    rule_lists = [(p,) for p in pairs]
    if n_bits == 3:
        rule_lists.extend(combinations(pairs, 2))
    else:
        rng = random.Random(20260923)
        for _ in range(2048):
            rule_lists.append(tuple(rng.sample(pairs, rng.randint(2, 5))))

    for rules in rule_lists:
        for gens in all_gens:
            direct = direct_empty(gens, rules, set_count)
            compiled = firing_circuit_empty(gens, rules, set_count)
            assert direct == compiled, (n_bits, rules, gens, direct, compiled)

    print(f"bits={n_bits}; |U|={len(words)}; anchors={len(anchors)}; "
          f"rule_lists={len(rule_lists)}; result=all pass")


def main():
    check_geometry(3, 2, 1)
    check_geometry(4, 3, 2)


if __name__ == "__main__":
    main()
