"""Verify sorting-network covers for every Hamming threshold toy.

Use zero-slice generators as the input wires of a Batcher bitonic sorting
network. Each comparator contributes one AND/intersection rule; its OR output
is a free upward union. The descending output wire at position n-k-1 is the
set of strings with at least n-k zero bits, i.e. weight at most k. On the
promise universe wt(x)>k this wire is empty. Every anchor of weight <=k
activates a true circuit proof using its matching zero slices.

The script independently checks the exact preservation closure for every
anchor, with all matching literal slices present.
"""

from __future__ import annotations


def bitonic_network(inputs: list[int]) -> tuple[list[int], list[tuple[int, int]]]:
    wires = inputs[:]
    rules: list[tuple[int, int]] = []

    def compare(i: int, j: int, ascending: bool) -> None:
        left, right = wires[i], wires[j]
        rules.append((left, right))
        low, high = left & right, left | right
        if ascending:
            wires[i], wires[j] = low, high
        else:
            wires[i], wires[j] = high, low

    def merge(lo: int, length: int, ascending: bool) -> None:
        if length <= 1:
            return
        half = length // 2
        for i in range(lo, lo + half):
            compare(i, i + half, ascending)
        merge(lo, half, ascending)
        merge(lo + half, half, ascending)

    def sort(lo: int, length: int, ascending: bool) -> None:
        if length <= 1:
            return
        half = length // 2
        sort(lo, half, True)
        sort(lo + half, half, False)
        merge(lo, length, ascending)

    sort(0, len(wires), False)
    return wires, rules


def verify_dimension(n: int) -> None:
    assert n >= 2
    network_size = 1 << (n - 1).bit_length()

    for k in range(n - 1):  # k <= n-2 keeps all forced slices nonempty.
        anchors = [x for x in range(1 << n) if x.bit_count() <= k]
        universe = [x for x in range(1 << n) if x.bit_count() > k]
        index = {x: i for i, x in enumerate(universe)}

        def mask(predicate) -> int:
            return sum(1 << index[x] for x in universe if predicate(x))

        zero_slices = [mask(lambda x, i=i: ((x >> i) & 1) == 0)
                       for i in range(n)]
        one_slices = [mask(lambda x, i=i: ((x >> i) & 1) == 1)
                      for i in range(n)]
        wires, rules = bitonic_network(zero_slices + [0] * (network_size - n))
        target = mask(lambda x: x.bit_count() <= k)
        output_wire = wires[n - k - 1]
        assert output_wire == target == 0

        support = {0}
        for e, h in rules:
            support.update((e, h, e & h))

        for anchor in anchors:
            generators = [zero_slices[i] if ((anchor >> i) & 1) == 0
                          else one_slices[i] for i in range(n)]
            closure = {s for s in support
                       if any((s & g) == g for g in generators)}
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
            assert 0 in closure, (n, k, anchor)

        print(
            f"n={n}; k={k}; anchors={len(anchors)}; universe={len(universe)}; "
            f"network_wires={network_size}; pair_rules={len(rules)}; "
            "verified_universal_cover=True"
        )


if __name__ == "__main__":
    for dimension in range(2, 9):
        verify_dimension(dimension)
