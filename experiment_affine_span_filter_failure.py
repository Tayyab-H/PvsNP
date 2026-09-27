"""Finite check of a rejected affine-span semi-filter family."""

from itertools import combinations
import random


def affine_hull(points, dimension):
    points = tuple(points)
    if not points:
        return None
    base = points[0]
    basis = {}
    for point in points[1:]:
        vector = point ^ base
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = vector
                break
            vector ^= basis[pivot]
    return base, tuple(sorted(basis.items(), reverse=True))


def affine_rank(points, dimension):
    hull = affine_hull(points, dimension)
    return 0 if hull is None else len(hull[1])


def contains(hull, point):
    if hull is None:
        return False
    base, basis = hull
    residual = point ^ base
    for pivot, vector in basis:
        if (residual >> pivot) & 1:
            residual ^= vector
    return residual == 0


def find_full_span_partition(universe, dimension, rng):
    for attempts in range(1, 1001):
        left, right = [], []
        for point in universe:
            (left if rng.getrandbits(1) else right).append(point)
        if (affine_rank(left, dimension) == dimension
                and affine_rank(right, dimension) == dimension):
            return tuple(left), tuple(right), attempts
    raise AssertionError("a full-span partition should be easy to find in this toy")


def check_excluded_set(dimension, excluded):
    cube = range(1 << dimension)
    universe = tuple(point for point in cube if point not in excluded)
    rng = random.Random((dimension << 16) + sum((x + 1) ** 3 for x in excluded))

    # Every anchor in the excluded set lies in the affine hull of each matching
    # coordinate slice of the dense high-table universe.
    for anchor in excluded:
        for coordinate in range(dimension):
            bit = (anchor >> coordinate) & 1
            slice_points = tuple(
                point for point in universe
                if ((point >> coordinate) & 1) == bit
            )
            hull = affine_hull(slice_points, dimension)
            assert contains(hull, anchor)
            assert affine_rank(slice_points, dimension) == dimension - 1

    left, right, attempts = find_full_span_partition(universe, dimension, rng)
    left_hull = affine_hull(left, dimension)
    right_hull = affine_hull(right, dimension)
    assert len(set(left).intersection(right)) == 0
    assert set(left).union(right) == set(universe)
    assert affine_rank(left, dimension) == dimension
    assert affine_rank(right, dimension) == dimension

    # For each excluded anchor a, F_a={S: a in aff(S)} contains every required
    # literal slice and both partition sides, but excludes their empty
    # intersection. Hence this one pair captures every filter in the family.
    for anchor in excluded:
        assert contains(left_hull, anchor)
        assert contains(right_hull, anchor)
        assert not contains(None, anchor)
    return attempts


def main():
    dimension = 4
    checks = 0
    total_attempts = 0
    for excluded_size in (1, 2, 3):
        for excluded in combinations(range(1 << dimension), excluded_size):
            total_attempts += check_excluded_set(dimension, excluded)
            checks += 1
    print(f"dimension={dimension}; excluded_sets={checks}; partition_trials={total_attempts}")
    print("all anchors' literal slices span their coordinate hyperplanes")
    print("one disjoint full-span pair captures every affine-span filter")


if __name__ == "__main__":
    main()
