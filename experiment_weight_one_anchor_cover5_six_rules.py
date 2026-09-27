"""Save and verify the six-rule 5-bit weight-one-anchor cover certificate.

The exact SAT search found this endpoint list. This verifier uses the exact
support-set preservation recurrence (empty set, endpoints, intersections),
which is sufficient because upward closure is checked by subset inclusion.
"""

from __future__ import annotations


N = 5
ANCHORS = (0, 1, 2, 4, 8, 16)
UNIVERSE = tuple(x for x in range(1 << N) if x not in ANCHORS)
INDEX = {x: i for i, x in enumerate(UNIVERSE)}

ENDPOINTS = (
    ({5, 7, 9, 12, 13, 14, 15, 17, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29},
     {6, 7, 10, 12, 14, 15, 18, 19, 20, 22, 23, 24, 26, 27, 28, 30}),
    ({3, 5, 6, 7, 17, 18, 19, 20, 21, 22, 23, 26, 27, 28, 29},
     {5, 6, 9, 10, 12, 13, 14, 17, 18, 20, 21, 22, 24, 25, 26, 28, 29, 30}),
    ({5, 6, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 29},
     {3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 23, 30}),
    ({3, 5, 6, 19, 24, 27, 30},
     {3, 7, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 31}),
    ({3, 15, 19, 24, 27, 30},
     {5, 6, 17, 18, 20, 21, 22, 26, 28, 29, 31}),
    ({5, 7, 12, 14, 15, 19, 20, 22, 23, 24, 27, 28, 30},
     {3, 5, 6, 9, 10, 11, 17, 18, 19, 24, 25, 26, 27, 31}),
)


def mask(points: set[int]) -> int:
    assert points <= set(UNIVERSE)
    return sum(1 << INDEX[x] for x in points)


RULE_MASKS = tuple((mask(e), mask(h)) for e, h in ENDPOINTS)
SUPPORT = {0}
for e, h in RULE_MASKS:
    SUPPORT.update((e, h, e & h))


def generators(anchor: int) -> list[int]:
    return [mask({x for x in UNIVERSE
                  if ((x >> i) & 1) == ((anchor >> i) & 1)})
            for i in range(N)]


def verify_anchor(anchor: int) -> tuple[bool, list[list[int]]]:
    closure = {s for s in SUPPORT if any((s & g) == g for g in generators(anchor))}
    fired: set[int] = set()
    rounds = []
    while True:
        newly = [j for j, (e, h) in enumerate(RULE_MASKS)
                 if j not in fired and e in closure and h in closure]
        if not newly:
            break
        rounds.append(newly)
        for j in newly:
            fired.add(j)
            meet = RULE_MASKS[j][0] & RULE_MASKS[j][1]
            closure.update(s for s in SUPPORT if (s & meet) == meet)
    return 0 in closure, rounds


def main() -> None:
    results = {a: verify_anchor(a) for a in ANCHORS}
    for anchor, (empty, rounds) in results.items():
        print(f"anchor={anchor:05b}; rounds={rounds}; derives_empty={empty}")
    assert all(empty for empty, _ in results.values())
    print(
        f"verified_six_rule_cover=True; anchors={len(ANCHORS)}; "
        f"universe={len(UNIVERSE)}; support_sets={len(SUPPORT)}"
    )


if __name__ == "__main__":
    main()
