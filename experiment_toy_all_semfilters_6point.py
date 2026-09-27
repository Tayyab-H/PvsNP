"""Search one- and two-pair all-filter covers on a six-point toy universe.

U is the set of 5-bit strings of weight at least four, and anchors have
weight at most two. The preservation-closure theorem tests every semi-filter
implicitly, so there is no need to enumerate the enormous monotone-family
space on six points.
"""

from itertools import combinations


N_BITS = 5
WORDS = [x for x in range(1 << N_BITS) if x.bit_count() >= 4]
ANCHORS = [x for x in range(1 << N_BITS) if x.bit_count() <= 2]
POINTS = len(WORDS)
SET_COUNT = 1 << POINTS


def generators(anchor):
    result = []
    for bit in range(N_BITS):
        subset = 0
        for i, word in enumerate(WORDS):
            if ((word >> bit) & 1) == ((anchor >> bit) & 1):
                subset |= 1 << i
        assert subset
        result.append(subset)
    return result


UP = []
for subset in range(SET_COUNT):
    up = 0
    for superset in range(SET_COUNT):
        if (superset & subset) == subset:
            up |= 1 << superset
    UP.append(up)

BASE = []
for anchor in ANCHORS:
    closure = 0
    for g in generators(anchor):
        closure |= UP[g]
    BASE.append(closure)


def empty_derived(base, rules):
    closure = base
    while True:
        updated = closure
        for e, h, inter in rules:
            if ((closure >> e) & 1) and ((closure >> h) & 1):
                updated |= UP[inter]
        if updated == closure:
            return bool(closure & 1)
        closure = updated


def main():
    # A rule with comparable endpoints adds an intersection already present
    # whenever its antecedents hold, so it can be deleted from any cover list.
    rules = []
    for e in range(SET_COUNT):
        for h in range(e + 1, SET_COUNT):
            if (e & h) == e or (e & h) == h:
                continue
            rules.append((e, h, e & h))

    one_pair_masks = []
    for rule in rules:
        mask = 0
        for ai, base in enumerate(BASE):
            if empty_derived(base, [rule]):
                mask |= 1 << ai
        one_pair_masks.append(mask)

    all_anchors = (1 << len(ANCHORS)) - 1
    best_one = max(one_pair_masks, key=int.bit_count)
    print(f"bits={N_BITS}; |U|={POINTS}; anchors={len(ANCHORS)}; "
          f"valid_incomparable_rules={len(rules)}")
    print(f"max_anchors_covered_by_one_pair={best_one.bit_count()}/{len(ANCHORS)}")

    def fmt_subset(subset):
        return "{" + ",".join(format(WORDS[i], f"0{N_BITS}b")
                               for i in range(POINTS) if (subset >> i) & 1) + "}"

    def fmt_anchors(mask):
        return [format(ANCHORS[i], f"0{N_BITS}b")
                for i in range(len(ANCHORS)) if (mask >> i) & 1]

    if best_one == all_anchors:
        i = one_pair_masks.index(best_one)
        print(f"one_pair={rules[i]}")
        return

    for i, first in enumerate(rules):
        for j in range(i + 1, len(rules)):
            second = rules[j]
            covered = 0
            for ai, base in enumerate(BASE):
                if empty_derived(base, (first, second)):
                    covered |= 1 << ai
            if covered == all_anchors:
                for rule in (first, second):
                    one_mask = one_pair_masks[rules.index(rule)]
                    e, h, _ = rule
                    print(f"pair=({fmt_subset(e)},{fmt_subset(h)}); "
                          f"anchors_hit={len(fmt_anchors(one_mask))}/{len(ANCHORS)}; "
                          f"hits={fmt_anchors(one_mask)}")
                print("two_pair_cover=all anchors; minimum=2")
                return

    print("two_pair_cover=none")


if __name__ == "__main__":
    main()
