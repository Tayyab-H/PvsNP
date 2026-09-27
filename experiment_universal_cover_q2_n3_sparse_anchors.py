"""Exact universal semi-filter cover number for the sparse-anchor 3-cube toy.

Unlike profile tests of one chosen filter per anchor, this uses the exact
preservation closure: a pair list covers every semi-filter above an anchor
iff its closure from the forced coordinate slices reaches the empty set.
"""

from __future__ import annotations

from itertools import combinations


N = 3
ALL_WORDS = list(range(1 << N))
ANCHORS = [0, (1 << N) - 1]
POINTS = [x for x in ALL_WORDS if x not in ANCHORS]
POINT_INDEX = {x: i for i, x in enumerate(POINTS)}
SUBSET_COUNT = 1 << len(POINTS)


def make_upsets() -> list[int]:
    return [sum(1 << s for s in range(SUBSET_COUNT) if s & g == g)
            for g in range(SUBSET_COUNT)]


UPSET = make_upsets()
BASE = []
for a in ANCHORS:
    gens = [sum(1 << POINT_INDEX[x] for x in POINTS if ((x >> i) & 1) == ((a >> i) & 1))
            for i in range(N)]
    closure = 0
    for g in gens:
        closure |= UPSET[g]
    BASE.append(closure)

RULES = [(e, h) for e in range(SUBSET_COUNT) for h in range(e, SUBSET_COUNT)]


def derives_empty(anchor_index: int, rule_indices: tuple[int, ...]) -> bool:
    closure = BASE[anchor_index]
    rules = [RULES[i] for i in rule_indices]
    changed = True
    while changed:
        changed = False
        for e, h in rules:
            if (closure >> e) & 1 and (closure >> h) & 1:
                new = closure | UPSET[e & h]
                if new != closure:
                    closure = new
                    changed = True
                    if closure & 1:
                        return True
    return bool(closure & 1)


def main(max_rules: int = 2) -> None:
    target_list = None
    for size in range(1, max_rules + 1):
        tested = 0
        for choice in combinations(range(len(RULES)), size):
            tested += 1
            if all(derives_empty(ai, choice) for ai in range(len(ANCHORS))):
                target_list = choice
                print(f"exact_universal_cover={size}; candidate_pairs={len(RULES)}; lists_checked_at_minimum={tested}")
                for idx in choice:
                    e, h = RULES[idx]
                    print(f"  E={[POINTS[i] for i in range(len(POINTS)) if e >> i & 1]}; H={[POINTS[i] for i in range(len(POINTS)) if h >> i & 1]}")
                return
        print(f"no_universal_cover_of_size={size}; lists_checked={tested}")
    print(f"no_cover_found_up_to={max_rules}")


if __name__ == "__main__":
    main()

