"""Check the affine-orbit unisolvent-pair construction in small cubes.

For d with 2d < N, the Hamming balls B0={x: |x|<=d} and
B1={x: |x|>=N-d} are disjoint sets of D=sum_{j<=d} C(N,j) points.
Both are unisolvent for degree-at-most-d Boolean polynomials. A uniformly
random affine automorphism sends each fixed excluded point uniformly over
the cube, so the union bound predicts a transform avoiding A whenever
2*|A|*D < 2^N.

The experiment checks the construction and literal-generator memberships on
seeded small instances. The asymptotic claim is proved in the project audit.
"""

from itertools import combinations
from math import comb
from random import Random


def masks_of_degree(n: int, d: int) -> list[int]:
    return [m for k in range(d + 1) for m in range(1 << n) if m.bit_count() == k]


def feature(x: int, monomials: list[int]) -> int:
    value = 0
    for j, monomial in enumerate(monomials):
        if x & monomial == monomial:
            value |= 1 << j
    return value


def rank(vectors: list[int]) -> int:
    pivots: dict[int, int] = {}
    for value in vectors:
        v = value
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)


def random_invertible(n: int, rng: Random) -> list[int]:
    while True:
        rows = [rng.randrange(1 << n) for _ in range(n)]
        if rank(rows) == n:
            return rows


def affine_image(x: int, rows: list[int], offset: int) -> int:
    y = 0
    for i, row in enumerate(rows):
        bit = ((row & x).bit_count() & 1) ^ ((offset >> i) & 1)
        y |= bit << i
    return y


def find_pair(n: int, d: int, excluded: set[int], rng: Random, trials: int = 500):
    ball = [x for x in range(1 << n) if x.bit_count() <= d]
    complement_ball = [x ^ ((1 << n) - 1) for x in ball]
    for _ in range(trials):
        rows = random_invertible(n, rng)
        offset = rng.randrange(1 << n)
        left = {affine_image(x, rows, offset) for x in ball}
        right = {affine_image(x, rows, offset) for x in complement_ball}
        if not (left & right or left & excluded or right & excluded):
            return left, right
    return None


def check_instance(n: int, d: int, excluded: set[int], rng: Random) -> bool:
    monomials = masks_of_degree(n, d)
    dimension = len(monomials)
    pair = find_pair(n, d, excluded, rng)
    if pair is None:
        return False
    left, right = pair
    if left & right or left & excluded or right & excluded:
        return False
    left_vectors = [feature(x, monomials) for x in left]
    right_vectors = [feature(x, monomials) for x in right]
    if len(left) != dimension or len(right) != dimension:
        return False
    if rank(left_vectors) != dimension or rank(right_vectors) != dimension:
        return False

    universe = set(range(1 << n))
    high = universe - excluded
    for anchor in excluded:
        anchor_feature = feature(anchor, monomials)
        if rank(left_vectors + [anchor_feature]) != dimension:
            return False
        if rank(right_vectors + [anchor_feature]) != dimension:
            return False
        for i in range(n):
            literal = {x for x in high if ((x >> i) & 1) == ((anchor >> i) & 1)}
            literal_vectors = [feature(x, monomials) for x in literal]
            if rank(literal_vectors + [anchor_feature]) != rank(literal_vectors):
                return False
    return True


def main() -> None:
    rng = Random(20260923)
    checks = 0
    for n, d in [(4, 1), (5, 1), (6, 1), (6, 2), (7, 2)]:
        dimension = sum(comb(n, j) for j in range(d + 1))
        assert 2 * d < n
        max_excluded = ((1 << n) - 1) // (2 * dimension)
        cases = []
        for m in range(1, min(max_excluded, 2) + 1):
            for excluded_tuple in combinations(range(1 << n), m):
                cases.append(set(excluded_tuple))
                if len(cases) >= 48:
                    break
            if len(cases) >= 48:
                break
        for excluded in cases:
            if not check_instance(n, d, excluded, rng):
                raise AssertionError((n, d, excluded))
            checks += 1
        print(
            f"N={n}, d={d}, D={dimension}, tested A sets={len(cases)}, "
            f"2|A|D<2^N: {2 * max(map(len, cases), default=0) * dimension < (1 << n)}"
        )
    print(f"passed {checks} seeded excluded-set instances")


if __name__ == "__main__":
    main()
