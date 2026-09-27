"""Enumerate p-biased fusion defects for every semi-filter on at most 4 points.

This is a finite diagnostic for the identity/profiles in Audit Proposition 18.15.
It does not estimate asymptotic cover numbers.
"""

from __future__ import annotations

def enumerate_minimal_antichains(n: int):
    """Yield nonempty antichains of nonempty subsets, as lists of subsets."""
    top = (1 << n) - 1
    vertices = list(range(1, top + 1))
    comparable = {}
    for x in vertices:
        comparable[x] = sum(
            1 << j
            for j, y in enumerate(vertices)
            if (x & y) == x or (x & y) == y
        )

    def visit(available: int, selected: tuple[int, ...]):
        if not available:
            if selected:
                yield selected
            return
        bit = available & -available
        index = bit.bit_length() - 1
        x = vertices[index]
        rest = available ^ bit
        yield from visit(rest, selected)
        yield from visit(rest & ~comparable[x], selected + (x,))

    yield from visit((1 << len(vertices)) - 1, ())


def accepted_layer_counts(n: int, minima: tuple[int, ...]) -> list[int]:
    counts = [0] * (n + 1)
    for subset in range(1 << n):
        if any((subset & witness) == witness for witness in minima):
            counts[subset.bit_count()] += 1
    return counts


def q_from_layers(counts: list[int], basis: tuple[float, ...]) -> float:
    return sum(count * weight for count, weight in zip(counts, basis))


def accepted_probability(family: int, n: int, p: float) -> float:
    total = 0.0
    for subset in range(1 << n):
        if (family >> subset) & 1:
            k = subset.bit_count()
            total += p**k * (1.0 - p) ** (n - k)
    return total


def labels(sets: list[int], n: int) -> list[str]:
    return ["".join(str(i) for i in range(n) if (x >> i) & 1) or "∅" for x in sets]


def main() -> None:
    grid = [i / 200 for i in range(1, 200)]
    for n in range(1, 6):
        antichains = list(enumerate_minimal_antichains(n))
        nonprincipal = []
        bases = []
        for p in grid:
            p2 = p * p
            bases.append((
                tuple(p**k * (1.0 - p) ** (n - k) for k in range(n + 1)),
                tuple(p2**k * (1.0 - p2) ** (n - k) for k in range(n + 1)),
            ))
        for minima in antichains:
            if len(minima) == 1:
                continue  # one minimal member generates a principal filter
            counts = accepted_layer_counts(n, minima)
            profile = []
            for p, (basis, basis2) in zip(grid, bases):
                q = q_from_layers(counts, basis)
                q2 = q_from_layers(counts, basis2)
                profile.append(q * q - q2)
            best = max(range(len(grid)), key=profile.__getitem__)
            nonprincipal.append((profile[best], grid[best], minima))
        if nonprincipal:
            value, p, minima = min(nonprincipal)
            print(
                f"n={n}: semifilters={len(antichains)} nonprincipal={len(nonprincipal)} "
                f"minimum_grid_max_defect={value:.9g} at_p={p:.3f} "
                f"extremal_minimal_members={labels(list(minima), n)}"
            )
        else:
            print(f"n={n}: semifilters={len(antichains)} nonprincipal=0")

    # Independently verify the defect identity by enumerating endpoint pairs.
    n, p = 4, 0.37
    checked = 0
    for minima in enumerate_minimal_antichains(n):
        if len(minima) == 1:
            continue
        family = 0
        for subset in range(1 << n):
            if any((subset & witness) == witness for witness in minima):
                family |= 1 << subset
        direct = 0.0
        for e in range(1 << n):
            pe = p**e.bit_count() * (1 - p) ** (n - e.bit_count())
            for h in range(1 << n):
                if ((family >> e) & 1) and ((family >> h) & 1) and not ((family >> (e & h)) & 1):
                    ph = p**h.bit_count() * (1 - p) ** (n - h.bit_count())
                    direct += pe * ph
        q = accepted_probability(family, n, p)
        q2 = accepted_probability(family, n, p * p)
        assert abs(direct - (q * q - q2)) < 1e-12
        checked += 1
    print(f"identity_direct_pair_checks={checked}; n={n}; p={p}; PASS")


if __name__ == "__main__":
    main()
