r"""Verify the directed-cycle relay certificate on punctured Boolean cubes.

For U={0,1}^n\{0^n,1^n}, the two extreme anchors force their matching
coordinate slices.  Each directed-cycle clause B_i = (x_i=0) or
(x_{i+1}=1) is in both anchor closures.  Intersecting the B_i around the
cycle leaves only the two removed constant strings, hence the empty set in U.

This finite verifier checks the sequential preservation-closure derivation;
the accompanying proof in ideas.md gives the all-n argument and matching
leaf lower bound.
"""

from __future__ import annotations


def verify_dimension(n: int) -> None:
    if n < 2:
        raise ValueError("n must be at least two")
    universe = set(range(1 << n)) - {0, (1 << n) - 1}
    anchors = (0, (1 << n) - 1)

    def matching_slices(anchor: int) -> list[set[int]]:
        return [
            {x for x in universe if ((x >> i) & 1) == ((anchor >> i) & 1)}
            for i in range(n)
        ]

    clauses = [
        {x for x in universe
         if ((x >> i) & 1) == 0 or ((x >> ((i + 1) % n)) & 1) == 1}
        for i in range(n)
    ]
    intersections = []
    running = set(universe)
    for clause in clauses:
        running &= clause
        intersections.append(set(running))

    # Every clause is already in both anchored closures through one forced slice.
    for anchor in anchors:
        generators = matching_slices(anchor)
        assert all(any(g <= clause for g in generators) for clause in clauses)

        # The first pair creates B_0 intersect B_1; later rules relay the
        # previous intersection against the next clause.
        available = list(generators)
        first = clauses[0] & clauses[1]
        assert any(s <= clauses[0] for s in available)
        assert any(s <= clauses[1] for s in available)
        available.append(first)
        assert first == intersections[1]
        for i in range(2, n):
            prior = intersections[i - 1]
            assert any(s <= prior for s in available)
            assert any(s <= clauses[i] for s in available)
            new = prior & clauses[i]
            assert new == intersections[i]
            available.append(new)
        assert intersections[-1] == set()

    print(
        f"n={n}; universe={len(universe)}; anchors={len(anchors)}; "
        f"relay_rules={n - 1}; final_intersection={len(intersections[-1])}; "
        "verified_for_both_anchors=True"
    )


if __name__ == "__main__":
    for dimension in range(2, 13):
        verify_dimension(dimension)
