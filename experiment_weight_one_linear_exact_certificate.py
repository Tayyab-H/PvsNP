"""Verify a 2n-4-rule universal cover for weight-at-most-one anchors.

Let Z_i={x:x_i=0}, O_i={x:x_i=1}, all restricted to U={x:wt(x)>=2}.
The circuit states are
    A_i = Z_1 & ... & Z_i,
    F_i = {x: wt(x_1,...,x_i)<=1}.
Then F_2=Z_1 | Z_2 and
    F_i = F_{i-1} & (Z_i | A_{i-1})   (i>=3).
Each displayed intersection is one relay rule; unions are free by upward
closure. The A_i states needed through A_{n-1} cost n-2 rules, and the F_i
updates cost n-2, for 2n-4 rules total.

The verifier checks the exact preservation closure for every anchor, not just
the set identities on the full Boolean cube.
"""

from __future__ import annotations


def verify(n: int) -> None:
    assert n >= 3
    anchors = [x for x in range(1 << n) if x.bit_count() <= 1]
    universe = [x for x in range(1 << n) if x.bit_count() >= 2]
    index = {x: i for i, x in enumerate(universe)}

    def point_set(predicate) -> int:
        return sum(1 << index[x] for x in universe if predicate(x))

    zero = [point_set(lambda x, i=i: ((x >> i) & 1) == 0) for i in range(n)]
    one = [point_set(lambda x, i=i: ((x >> i) & 1) == 1) for i in range(n)]

    # A_i: zero on the first i coordinates. F_i: at most one 1 in that prefix.
    a_state = {i: point_set(lambda x, i=i: (x & ((1 << i) - 1)).bit_count() == 0)
               for i in range(2, n)}
    f_state = {i: point_set(lambda x, i=i: (x & ((1 << i) - 1)).bit_count() <= 1)
               for i in range(2, n + 1)}

    rules: list[tuple[int, int]] = [(zero[0], zero[1])]  # derives A_2
    for i in range(3, n + 1):
        if i < n:
            rules.append((a_state[i - 1], zero[i - 1]))  # derives A_i
        rules.append((f_state[i - 1], zero[i - 1] | a_state[i - 1]))

    assert len(rules) == 2 * n - 4
    assert f_state[n] == 0  # U omits all words of weight at most one.

    support = {0}
    for e, h in rules:
        support.update((e, h, e & h))

    for anchor in anchors:
        generators = [zero[i] if ((anchor >> i) & 1) == 0 else one[i]
                      for i in range(n)]
        closure = {s for s in support if any((s & g) == g for g in generators)}
        fired = [False] * len(rules)
        while True:
            newly = [r for r, (e, h) in enumerate(rules)
                     if not fired[r] and e in closure and h in closure]
            if not newly:
                break
            for r in newly:
                fired[r] = True
                meet = rules[r][0] & rules[r][1]
                closure.update(s for s in support if (s & meet) == meet)
        assert 0 in closure, f"n={n}; anchor={anchor:0{n}b}"

    print(
        f"n={n}; anchors={len(anchors)}; universe={len(universe)}; "
        f"rules={len(rules)}; exact_closure_all_anchors=True"
    )


if __name__ == "__main__":
    for dimension in range(3, 13):
        verify(dimension)
