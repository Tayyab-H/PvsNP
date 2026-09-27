"""Small exhaustive checks of the binary Bose--Burton blocking bound.

This only checks N <= 4.  It is an implementation sanity check, not a proof;
the general lower bound is the Bose--Burton theorem.
"""

from itertools import combinations


def parity(x: int) -> int:
    return x.bit_count() & 1


def rank_gf2(rows: tuple[int, ...]) -> int:
    basis = {}
    for value in rows:
        x = value
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis)


def codimension_d_kernels(n: int, d: int) -> list[frozenset[int]]:
    """Return nonzero vectors in each distinct codimension-d kernel."""
    kernels = set()
    for rows in combinations(range(1, 1 << n), d):
        if rank_gf2(rows) != d:
            continue
        kernel = frozenset(
            x for x in range(1, 1 << n)
            if all(parity(row & x) == 0 for row in rows)
        )
        kernels.add(kernel)
    return sorted(kernels, key=lambda k: (len(k), tuple(sorted(k))))


def verify(n: int, d: int) -> tuple[int, int]:
    points = tuple(range(1, 1 << n))
    flats = codimension_d_kernels(n, d)
    bound = (1 << (d + 1)) - 1

    # The nonzero points of a fixed (d+1)-dimensional vector subspace attain it.
    candidate = frozenset(
        x for x in points if x >> (d + 1) == 0
    )
    assert len(candidate) == bound
    assert all(candidate & flat for flat in flats)

    # Exhaust every set smaller than the claimed minimum for these small cases.
    for size in range(bound):
        for chosen in combinations(points, size):
            chosen_set = set(chosen)
            if all(chosen_set & flat for flat in flats):
                raise AssertionError(
                    f"smaller blocker found: n={n}, d={d}, set={chosen}"
                )
    return bound, len(flats)


def main() -> None:
    cases = [(2, 1), (3, 1), (3, 2), (4, 1), (4, 2)]
    for n, d in cases:
        bound, count = verify(n, d)
        print(f"N={n}, d={d}: minimum {bound}; checked {count} distinct kernels")
    print("PASS: all tested minima match 2^(d+1)-1")


if __name__ == "__main__":
    main()
