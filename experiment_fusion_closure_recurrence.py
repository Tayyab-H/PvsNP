"""Cross-check the finite-state recurrence against explicit upward closure.

This is a small semantic verification on a six-point universe, not evidence
for an asymptotic bound. It exhausts every one-rule pair and checks a fixed
seed of two-rule lists for both sparse-cube anchors.
"""

from __future__ import annotations

import random


N = 3
WORDS = list(range(1, 7))  # remove 000 and 111
POINT_INDEX = {word: i for i, word in enumerate(WORDS)}
SUBSET_COUNT = 1 << len(WORDS)
ANCHORS = (0, 7)


def all_upsets() -> list[int]:
    return [
        sum(1 << s for s in range(SUBSET_COUNT) if s & g == g)
        for g in range(SUBSET_COUNT)
    ]


UPSET = all_upsets()
RULES = [(e, h) for e in range(SUBSET_COUNT) for h in range(e, SUBSET_COUNT)]


def literal_slices(anchor: int) -> list[int]:
    return [
        sum(
            1 << POINT_INDEX[word]
            for word in WORDS
            if ((word >> i) & 1) == ((anchor >> i) & 1)
        )
        for i in range(N)
    ]


BASES = []
SLICES = []
for anchor in ANCHORS:
    slices = literal_slices(anchor)
    SLICES.append(slices)
    base = 0
    for g in slices:
        base |= UPSET[g]
    BASES.append(base)


def explicit_closure_has_empty(anchor_index: int, rule_indices: tuple[int, ...]) -> bool:
    closure = BASES[anchor_index]
    rules = [RULES[i] for i in rule_indices]
    while True:
        old = closure
        for e, h in rules:
            if (closure >> e) & 1 and (closure >> h) & 1:
                closure |= UPSET[e & h]
        if closure & 1:
            return True
        if closure == old:
            return False


def recurrence_has_empty(anchor_index: int, rule_indices: tuple[int, ...]) -> bool:
    rules = [RULES[i] for i in rule_indices]
    consequences = [e & h for e, h in rules]
    left_support = [
        [j for j, t in enumerate(consequences) if t & ~e == 0]
        for e, _ in rules
    ]
    right_support = [
        [j for j, t in enumerate(consequences) if t & ~h == 0]
        for _, h in rules
    ]
    slices = SLICES[anchor_index]
    left_seed = [any(g & ~e == 0 for g in slices) for e, _ in rules]
    right_seed = [any(g & ~h == 0 for g in slices) for _, h in rules]

    active = [False] * len(rules)
    strict_rounds = 0
    while True:
        updated = [
            (left_seed[i] or any(active[j] for j in left_support[i]))
            and (right_seed[i] or any(active[j] for j in right_support[i]))
            for i in range(len(rules))
        ]
        if updated == active:
            break
        assert all(not old or new for old, new in zip(active, updated))
        active = updated
        strict_rounds += 1
        assert strict_rounds <= len(rules)
    return any(on and consequences[i] == 0 for i, on in enumerate(active))


def main() -> None:
    checked = 0
    for rule_index in range(len(RULES)):
        one = (rule_index,)
        for anchor_index in range(len(ANCHORS)):
            e, h = RULES[rule_index]
            if e & h == 0:
                left_seed = any(g & ~e == 0 for g in SLICES[anchor_index])
                right_seed = any(g & ~h == 0 for g in SLICES[anchor_index])
                assert not (left_seed and right_seed)
            assert explicit_closure_has_empty(anchor_index, one) == recurrence_has_empty(
                anchor_index, one
            )
            checked += 1

    rng = random.Random(20260926)
    two_rule_trials = 100_000
    for _ in range(two_rule_trials):
        choice = tuple(sorted(rng.sample(range(len(RULES)), 2)))
        for anchor_index in range(len(ANCHORS)):
            assert explicit_closure_has_empty(anchor_index, choice) == recurrence_has_empty(
                anchor_index, choice
            )
            checked += 1

    def encode(points: set[int]) -> int:
        return sum(1 << POINT_INDEX[p] for p in points)

    known_pairs = (
        (encode({1, 3}), encode({2, 4, 5, 6})),
        (encode({1, 3, 4, 5}), encode({1, 2, 3, 6})),
    )
    known_indices = tuple(RULES.index(tuple(sorted(pair))) for pair in known_pairs)
    assert all(
        recurrence_has_empty(anchor_index, known_indices)
        for anchor_index in range(len(ANCHORS))
    )

    for anchor_index in range(len(ANCHORS)):
        slices = SLICES[anchor_index]
        shared_first = RULES.index(tuple(sorted((slices[0], slices[1]))))
        final_merge = RULES.index(tuple(sorted((slices[0] & slices[1], slices[2]))))
        assert not recurrence_has_empty(anchor_index, (shared_first,))
        assert recurrence_has_empty(anchor_index, (shared_first, final_merge))

    print(f"PASS: {checked:,} explicit-closure/least-fixed-point comparisons")
    print("PASS: fixed-point iteration used at most q strict rounds")
    print("PASS: no empty-consequence rule activates from literal seeds alone")
    print("PASS: a shared two-literal intersection saves one rule for either anchor")
    print("PASS: known sparse-cube two-pair universal cover derives empty at both anchors")


if __name__ == "__main__":
    main()
