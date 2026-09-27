"""Finite checks for q-ary generalized Reed--Muller affine-orbit pairs.

The check uses F_3.  For the reduced total-degree feature space on F_3^N,
the lower set of exponent vectors |e|<=d and a corresponding lower set of
evaluation points give an information set.  Coordinatewise x -> -x reverses
the chosen alphabet levels, producing a disjoint second information set when
2d < N(q-1).  Random affine maps are sampled until both sets avoid A.

The code tests the finite-field linear algebra and coordinate-slice anchor
membership.  It is evidence for the construction, not its proof or a P-vs-NP
result.
"""

from itertools import product
from random import Random


Q = 3
LEVELS = (1, 0, 2)  # -LEVELS[k] == LEVELS[Q - 1 - k] in F_3


def rank_mod_q(rows: list[tuple[int, ...]], q: int | None = None) -> int:
    if q is None:
        q = Q
    if not rows:
        return 0
    matrix = [[x % q for x in row] for row in rows]
    row_count = len(matrix)
    col_count = len(matrix[0])
    pivot_row = 0
    for col in range(col_count):
        pivot = next((r for r in range(pivot_row, row_count) if matrix[r][col]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inv = pow(matrix[pivot_row][col], -1, q)
        matrix[pivot_row] = [(x * inv) % q for x in matrix[pivot_row]]
        for r in range(pivot_row + 1, row_count):
            factor = matrix[r][col]
            if factor:
                matrix[r] = [(x - factor * y) % q for x, y in zip(matrix[r], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def exponent_vectors(n: int, degree: int) -> list[tuple[int, ...]]:
    return sorted(
        (e for e in product(range(Q), repeat=n) if sum(e) <= degree),
        key=lambda e: (sum(e), e),
    )


def feature(point: tuple[int, ...], exponents: list[tuple[int, ...]]) -> tuple[int, ...]:
    return tuple(
        _monomial_value(point, e)
        for e in exponents
    )


def _monomial_value(point: tuple[int, ...], exponent: tuple[int, ...]) -> int:
    value = 1
    for x, e in zip(point, exponent):
        value = (value * pow(x, e, Q)) % Q
    return value


def lower_set_points(n: int, degree: int) -> list[tuple[int, ...]]:
    return [tuple(LEVELS[k] for k in indices)
            for indices in product(range(Q), repeat=n)
            if sum(indices) <= degree]


def random_invertible(n: int, rng: Random) -> list[list[int]]:
    while True:
        matrix = [[rng.randrange(Q) for _ in range(n)] for _ in range(n)]
        if rank_mod_q([tuple(row) for row in matrix]) == n:
            return matrix


def affine_image(point: tuple[int, ...], matrix: list[list[int]], offset: tuple[int, ...]):
    n = len(point)
    return tuple(
        (sum(matrix[i][j] * point[j] for j in range(n)) + offset[i]) % Q
        for i in range(n)
    )


def find_pair(n: int, degree: int, excluded: set[tuple[int, ...]], rng: Random, trials=500):
    base = lower_set_points(n, degree)
    other = [tuple((-x) % Q for x in point) for point in base]
    for _ in range(trials):
        matrix = random_invertible(n, rng)
        offset = tuple(rng.randrange(Q) for _ in range(n))
        left = {affine_image(x, matrix, offset) for x in base}
        right = {affine_image(x, matrix, offset) for x in other}
        if not (left & right or left & excluded or right & excluded):
            return left, right
    return None


def check_case(n: int, degree: int, excluded: set[tuple[int, ...]], rng: Random) -> bool:
    exponents = exponent_vectors(n, degree)
    dimension = len(exponents)
    pair = find_pair(n, degree, excluded, rng)
    if pair is None:
        return False
    left, right = pair
    if left & right or left & excluded or right & excluded:
        return False
    left_features = [feature(x, exponents) for x in left]
    right_features = [feature(x, exponents) for x in right]
    if len(left) != dimension or len(right) != dimension:
        return False
    if rank_mod_q(left_features) != dimension or rank_mod_q(right_features) != dimension:
        return False

    universe = set(product(range(Q), repeat=n))
    high = universe - excluded
    for anchor in excluded:
        anchor_feature = feature(anchor, exponents)
        if rank_mod_q(left_features + [anchor_feature]) != dimension:
            return False
        if rank_mod_q(right_features + [anchor_feature]) != dimension:
            return False
        for i in range(n):
            literal = [x for x in high if x[i] == anchor[i]]
            literal_features = [feature(x, exponents) for x in literal]
            if rank_mod_q(literal_features + [anchor_feature]) != rank_mod_q(literal_features):
                return False
    return True


def run_family(q: int, levels: tuple[int, ...], specifications, seed: int) -> int:
    global Q, LEVELS
    Q = q
    LEVELS = levels
    rng = Random(seed)
    checked = 0
    for n, degree, trials, exhaustive_singletons, cap_size in specifications:
        dimension = len(exponent_vectors(n, degree))
        qn = Q ** n
        pair_limit = (qn - 1) // (2 * dimension)
        a, b = divmod(degree, Q - 1)
        slice_distance = (Q - b) * (Q ** (n - a - 2))
        max_excluded = min(pair_limit, slice_distance - 1)
        universe = list(product(range(Q), repeat=n))
        if exhaustive_singletons:
            cases = [{point} for point in universe]
        else:
            largest = min(max_excluded, cap_size)
            cases = []
            for _ in range(trials):
                m = rng.randint(1, largest)
                cases.append(set(rng.sample(universe, m)))
        for excluded in cases:
            if not check_case(n, degree, excluded, rng):
                raise AssertionError((q, n, degree, excluded))
            checked += 1
        largest_m = max(map(len, cases))
        print(
            f"q={Q}, N={n}, d={degree}, D={dimension}, cases={len(cases)}, "
            f"max |A|={largest_m}, 2|A|D<q^N={2 * largest_m * dimension < qn}, "
            f"slice distance={slice_distance}"
        )
    return checked


def main() -> None:
    checked = run_family(
        3,
        (1, 0, 2),
        [(3, 1, 27, True, 1), (4, 1, 80, False, 99),
         (4, 2, 80, False, 99), (5, 2, 80, False, 99)],
        23092026,
    )
    checked += run_family(
        5,
        (1, 2, 0, 3, 4),
        [(3, 1, 40, False, 20), (4, 1, 40, False, 20),
         (4, 2, 40, False, 20)],
        23092027,
    )
    print(f"passed {checked} q-ary seeded/exhaustive cases")


if __name__ == "__main__":
    main()
