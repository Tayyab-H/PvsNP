"""Check the coordinate-dependent fusion identity and a common-core example."""

from __future__ import annotations

import random
from itertools import combinations, product


def antichains(n: int):
    top = (1 << n) - 1
    vertices = list(range(1, top + 1))
    comparable = {
        x: sum(
            1 << j
            for j, y in enumerate(vertices)
            if (x & y) == x or (x & y) == y
        )
        for x in vertices
    }

    def visit(available: int, selected: tuple[int, ...]):
        if not available:
            if selected:
                yield selected
            return
        bit = available & -available
        x = vertices[bit.bit_length() - 1]
        rest = available ^ bit
        yield from visit(rest, selected)
        yield from visit(rest & ~comparable[x], selected + (x,))

    yield from visit((1 << len(vertices)) - 1, ())


def accepted_sets(n: int, minima: tuple[int, ...]) -> list[int]:
    return [
        subset
        for subset in range(1 << n)
        if any((subset & witness) == witness for witness in minima)
    ]


def product_weights(n: int, p: tuple[float, ...]) -> list[float]:
    weights = []
    for subset in range(1 << n):
        w = 1.0
        for i, pi in enumerate(p):
            w *= pi if (subset >> i) & 1 else 1.0 - pi
        weights.append(w)
    return weights


def main() -> None:
    rng = random.Random(20260924)
    n = 4
    records = [(mins, accepted_sets(n, mins)) for mins in antichains(n)]
    filters = [accepted for _mins, accepted in records]
    checked = 0
    worst_error = 0.0
    for _ in range(12):
        p = tuple(rng.uniform(0.05, 0.95) for _ in range(n))
        p2 = tuple(x * x for x in p)
        w = product_weights(n, p)
        w2 = product_weights(n, p2)
        for accepted in filters:
            aset = set(accepted)
            q = sum(w[e] for e in accepted)
            q2 = sum(w2[e] for e in accepted)
            defect = q * q - q2
            direct = sum(
                w[e] * w[h]
                for e in accepted
                for h in accepted
                if (e & h) not in aset
            )
            worst_error = max(worst_error, abs(defect - direct))
            assert defect >= -1e-12
            assert abs(defect - direct) < 1e-12
            checked += 1
    print(f"coordinate_bias_identity_checks={checked}; worst_error={worst_error:.3g}; PASS")

    face_checks = 0
    for minima, accepted in records:
        if len(minima) < 2:
            continue
        a, b = min(combinations(minima, 2), key=lambda pair: (pair[0] | pair[1]).bit_count())
        a_only = a & ~b
        b_only = b & ~a
        i = (a_only & -a_only).bit_length() - 1
        j = (b_only & -b_only).bit_length() - 1
        base = (a | b) & ~(1 << i) & ~(1 << j)
        assert base not in accepted
        p = tuple(
            1.0 if (base >> k) & 1 else 0.5 if k in (i, j) else 0.0
            for k in range(n)
        )
        weights = product_weights(n, p)
        weights2 = product_weights(n, tuple(x * x for x in p))
        q = sum(weights[e] for e in accepted)
        q2 = sum(weights2[e] for e in accepted)
        assert abs((q * q - q2) - 0.125) < 1e-12
        face_checks += 1
    print(f"minimum-union_OR-face_checks={face_checks}; defect=1/8; PASS")

    # Search a small coordinate-bias grid for every four-point semi-filter.
    # This is a lower bound on the true product-bias supremum, not an optimizer.
    best = [(-1.0, None) for _ in records]
    for p in product((0.0, 0.25, 0.5, 0.75, 1.0), repeat=n):
        w = product_weights(n, p)
        w2 = product_weights(n, tuple(x * x for x in p))
        for j, (_mins, accepted) in enumerate(records):
            q = sum(w[e] for e in accepted)
            q2 = sum(w2[e] for e in accepted)
            defect = q * q - q2
            if defect > best[j][0]:
                best[j] = (defect, p)
    nonprincipal = [
        (best[j][0], mins, best[j][1])
        for j, (mins, _accepted) in enumerate(records)
        if len(mins) > 1
    ]
    floor, minima, vector = min(nonprincipal, key=lambda item: item[0])
    print(
        f"n=4 product_bias_grid_points=625 nonprincipal_filters={len(nonprincipal)} "
        f"minimum_sampled_peak={floor:.9g}; minima={minima}; bias={vector}"
    )

    # Two minimal witnesses share N-2 fixed core points and have separate tips.
    # Uniform bias dilutes the defect over the growing core; a vector bias can
    # pin that core and leave only the two tip coordinates random.
    for size in (5, 10, 20, 50):
        p = (size - 1) / size
        uniform_peak = 2 * p ** (2 * size - 2) * (1 - p) ** 2
        selective_bias_defect = 1.0 / 8.0
        print(
            f"N={size}: uniform_peak={uniform_peak:.9g}; "
            f"coordinate_selective_defect={selective_bias_defect:.6g}"
        )
    print("PASS: fixing the common core at bias 1 and setting both tips to 1/2 gives defect 1/8.")


if __name__ == "__main__":
    main()
