"""Check the linear intersection-count DP for the weight-at-most-one set.

For each i, A_i is the set of strings with zero 1s in the first i bits, and
B_i is the set with exactly one 1 in the first i bits. The recurrence uses
three intersections per new coordinate; unions are free in D_cap.
"""

from __future__ import annotations


def verify_dimension(n: int) -> None:
    cube = set(range(1 << n))
    zero = [{x for x in cube if not ((x >> i) & 1)} for i in range(n)]
    one = [{x for x in cube if (x >> i) & 1} for i in range(n)]

    no_one = zero[0]
    exactly_one = one[0]
    intersections = 0
    for i in range(1, n):
        next_no_one = no_one & zero[i]
        next_exactly_one = (exactly_one & zero[i]) | (no_one & one[i])
        intersections += 3
        no_one, exactly_one = next_no_one, next_exactly_one

    result = no_one | exactly_one
    target = {x for x in cube if x.bit_count() <= 1}
    assert result == target
    assert intersections == 3 * (n - 1)
    print(
        f"n={n}; target_size={len(target)}; binary_intersections={intersections}; "
        "verified_target=True"
    )


if __name__ == "__main__":
    for dimension in range(2, 13):
        verify_dimension(dimension)
