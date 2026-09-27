"""Exact four-rule certificate for the 4-bit weight-at-most-one anchors.

Anchors are 0000 and the four unit vectors; U contains the other 11 words.
The endpoint list is a concrete model found by
experiment_relay_cover_boolean_cube.py. This file verifies it by explicitly
computing the full preservation closure for all five anchors.
"""

from __future__ import annotations

from itertools import combinations


N = 4
ANCHORS = (0, 1, 2, 4, 8)
UNIVERSE = frozenset(set(range(1 << N)) - set(ANCHORS))

ENDPOINTS = (
    (frozenset({3, 5, 7, 9, 10, 11, 14, 15}),
     frozenset({6, 7, 10, 12, 14, 15})),
    (frozenset({3, 6, 10, 14, 15}),
     frozenset({5, 7, 9, 10, 11, 12, 13, 14, 15})),
    (frozenset({3, 5, 6, 7, 10, 13, 14, 15}),
     frozenset({3, 6, 9, 10, 11, 12, 14})),
    (frozenset({3, 5, 6, 7, 9, 11, 12, 13}),
     frozenset({10, 14, 15})),
)


def subsets() -> list[frozenset[int]]:
    pts = sorted(UNIVERSE)
    return [frozenset(c) for r in range(len(pts) + 1) for c in combinations(pts, r)]


ALL_SUBSETS = subsets()


def matching_generators(anchor: int) -> list[frozenset[int]]:
    return [frozenset(x for x in UNIVERSE if ((x >> i) & 1) == ((anchor >> i) & 1))
            for i in range(N)]


def closure_rounds(anchor: int) -> tuple[bool, list[list[int]]]:
    generators = matching_generators(anchor)
    closure = {s for s in ALL_SUBSETS if any(g <= s for g in generators)}
    fired: set[int] = set()
    rounds: list[list[int]] = []
    while True:
        newly = [r for r, (e, h) in enumerate(ENDPOINTS)
                 if r not in fired and e in closure and h in closure]
        if not newly:
            break
        rounds.append(newly)
        for r in newly:
            fired.add(r)
            meet = ENDPOINTS[r][0] & ENDPOINTS[r][1]
            closure.update(s for s in ALL_SUBSETS if meet <= s)
    return frozenset() in closure, rounds


def main() -> None:
    results = {a: closure_rounds(a) for a in ANCHORS}
    for anchor, (derives_empty, rounds) in results.items():
        print(f"anchor={anchor:04b}; rounds={rounds}; derives_empty={derives_empty}")
    assert all(derives_empty for derives_empty, _ in results.values())
    print("verified_universal_four_rule_cover=True; universe_size=11; anchors=5")


if __name__ == "__main__":
    main()
