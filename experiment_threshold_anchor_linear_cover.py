"""Build and verify a universal relay cover for low-Hamming-weight anchors.

For anchors of weight at most k and universe points of weight greater than k,
the prefix-count recurrence gives a cover with at most (2k+1)(n-1) pair rules.
This script checks the recurrence as an actual preservation-closure certificate,
not merely as a set identity.
"""

from __future__ import annotations

def cover_and_verify(n: int, k: int) -> None:
    # Keeping k <= n-2 ensures every matching coordinate slice meets U.
    assert n >= 2 and 0 <= k <= n - 2
    anchors = [x for x in range(1 << n) if x.bit_count() <= k]
    universe = [x for x in range(1 << n) if x.bit_count() > k]
    point_index = {x: i for i, x in enumerate(universe)}
    u_size = len(universe)

    # State S[i][j]: universe points with exactly j ones among the first i bits.
    states: dict[tuple[int, int], int] = {}
    for i in range(n + 1):
        prefix_mask = (1 << i) - 1
        for j in range(min(i, k) + 1):
            states[i, j] = sum(
                1 << point_index[x]
                for x in universe
                if (x & prefix_mask).bit_count() == j
            )

    slices = {
        (i, b): sum(
            1 << point_index[x]
            for x in universe
            if ((x >> i) & 1) == b
        )
        for i in range(n)
        for b in (0, 1)
    }

    # Each branch of S[i,j] = (S[i-1,j] & Z_i) | (S[i-1,j-1] & O_i)
    # is one intersection rule. The union is free under upward closure.
    rules: list[tuple[int, int]] = []
    for i in range(2, n + 1):
        for j in range(min(i, k) + 1):
            if j <= min(i - 1, k):
                rules.append((states[i - 1, j], slices[i - 1, 0]))
            if j >= 1:
                rules.append((states[i - 1, j - 1], slices[i - 1, 1]))

    # Every possible result needed in this finite closure is an endpoint,
    # a rule intersection, or the empty set. Upward closure is checked by
    # subset tests over this support family.
    support = {0}
    for e, h in rules:
        support.update((e, h, e & h))

    checked = []
    for anchor in anchors:
        generators = [
            slices[i, (anchor >> i) & 1]
            for i in range(n)
        ]
        closure = {s for s in support if any((s & g) == g for g in generators)}
        fired = [False] * len(rules)
        while True:
            newly = [
                r for r, (e, h) in enumerate(rules)
                if not fired[r] and e in closure and h in closure
            ]
            if not newly:
                break
            for r in newly:
                fired[r] = True
                meet = rules[r][0] & rules[r][1]
                closure.update(s for s in support if (s & meet) == meet)
        checked.append(0 in closure)

    expected_bound = (2 * k + 1) * (n - 1)
    assert len(rules) <= expected_bound
    assert all(checked), (n, k, checked)
    print(
        f"n={n}; k={k}; anchors={len(anchors)}; universe={u_size}; "
        f"rules={len(rules)}; bound={expected_bound}; "
        f"verified_universal_cover=True"
    )


if __name__ == "__main__":
    for dimension in range(2, 9):
        for threshold in range(dimension - 1):
            cover_and_verify(dimension, threshold)
