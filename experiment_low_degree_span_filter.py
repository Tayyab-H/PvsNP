"""Finite Reed-Muller feature-span checks for an affine semi-filter family.

This probes filters of the form
    F_a = {S subset U : phi_d(a) is in aff_F2(phi_d(S))},
where phi_d lists all Boolean monomials of degree at most d.
The asymptotic counting proof is in the research audit; this script checks
small truth-table cubes and never treats the finite data as that proof.
"""

from itertools import combinations
import random


def features(dimension, degree):
    monomials = [
        sum(1 << i for i in support)
        for k in range(degree + 1)
        for support in combinations(range(dimension), k)
    ]
    return tuple(
        sum(1 << j for j, monomial in enumerate(monomials)
            if point & monomial == monomial)
        for point in range(1 << dimension)
    )


def span_basis(vectors):
    basis = {}
    for vector in vectors:
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = vector
                break
            vector ^= basis[pivot]
    return tuple(sorted(basis.items(), reverse=True))


def in_span(basis, vector):
    for pivot, row in basis:
        if (vector >> pivot) & 1:
            vector ^= row
    return vector == 0


def affine_basis(points, phi):
    points = tuple(points)
    if not points:
        return None
    base = phi[points[0]]
    return base, span_basis(phi[p] ^ base for p in points[1:])


def affine_contains(hull, point, phi):
    if hull is None:
        return False
    base, basis = hull
    return in_span(basis, phi[point] ^ base)


def check_instance(dimension, degree, excluded, seed):
    phi = features(dimension, degree)
    cube = tuple(range(1 << dimension))
    excluded = frozenset(excluded)
    universe = tuple(x for x in cube if x not in excluded)
    full_hull = affine_basis(cube, phi)
    high_hull = affine_basis(universe, phi)

    # A small excluded set must not change the Reed-Muller evaluation span.
    assert len(high_hull[1]) == len(full_hull[1])

    # Every matching truth-table-bit generator must put its low anchor in
    # the affine hull of the surviving high tables in that coordinate slice.
    for anchor in excluded:
        for coordinate in range(dimension):
            bit = (anchor >> coordinate) & 1
            generator = tuple(
                x for x in universe if ((x >> coordinate) & 1) == bit
            )
            assert affine_contains(affine_basis(generator, phi), anchor, phi)

    rng = random.Random(seed)
    for attempts in range(1, 1001):
        left, right = [], []
        for point in universe:
            (left if rng.getrandbits(1) else right).append(point)
        left_hull = affine_basis(left, phi)
        right_hull = affine_basis(right, phi)
        if (left_hull is not None and right_hull is not None
                and len(left_hull[1]) == len(full_hull[1])
                and len(right_hull[1]) == len(full_hull[1])):
            # Both sides are members of every F_a, while their empty
            # intersection is not. This pair defeats the tested filter family.
            assert set(left).isdisjoint(right)
            assert set(left).union(right) == set(universe)
            for anchor in excluded:
                assert affine_contains(left_hull, anchor, phi)
                assert affine_contains(right_hull, anchor, phi)
            return attempts
    raise AssertionError("failed to find a two-part full feature-span partition")


def main():
    # Degree two in an eight-bit toy cube has 37 evaluation coordinates,
    # enough to make the Reed-Muller span test nontrivial while keeping the
    # exact finite check inexpensive.
    dimension, degree = 8, 2
    trials = []
    for anchor in range(1 << dimension):
        trials.append((anchor,))

    rng = random.Random(20260923)
    all_points = tuple(range(1 << dimension))
    for _ in range(512):
        size = 2 + rng.randrange(2)
        trials.append(tuple(sorted(rng.sample(all_points, size))))

    total_partition_attempts = 0
    for index, excluded in enumerate(trials):
        total_partition_attempts += check_instance(
            dimension, degree, excluded,
            seed=(dimension << 24) + (degree << 16) + index,
        )

    print(
        f"dimension={dimension}; degree={degree}; "
        f"excluded_sets={len(trials)}; partition_trials={total_partition_attempts}"
    )
    print("all tested high-table sets retain the full Reed-Muller affine span")
    print("all tested matching coordinate slices contain their low anchor in span")
    print("one disjoint full-span pair captures every tested feature-span filter")


if __name__ == "__main__":
    main()
