"""Find the best anchor-balanced distribution over toy semi-filters.

For each finite threshold-promise toy geometry, enumerate every semi-filter
above every anchor. Solve the linear program that minimizes the largest
probability with which one ordered pair (E,H) violates a sampled filter.
This is the fractional-cover dual of the exact all-semi-filter cover search.

The computation is exact at the incidence-matrix level; HiGHS solves the LP
in floating point, so reported objective values are numerical certificates,
not rational proofs.
"""

from itertools import product

import numpy as np
from scipy.optimize import linprog


def antichains(set_count):
    elements = list(range(set_count))

    def visit(index, chosen):
        if index == len(elements):
            if chosen:
                yield tuple(chosen)
            return
        x = elements[index]
        yield from visit(index + 1, chosen)
        if x and all((x & y) != x and (x & y) != y for y in chosen):
            chosen.append(x)
            yield from visit(index + 1, chosen)
            chosen.pop()

    yield from visit(0, [])


def family_from_minima(minima, set_count):
    family = 0
    for superset in range(set_count):
        if any((superset & minimum) == minimum for minimum in minima):
            family |= 1 << superset
    return family


def run_model(n_bits, min_weight, anchors_max_weight):
    words = [x for x in range(1 << n_bits) if x.bit_count() >= min_weight]
    anchors = [x for x in range(1 << n_bits)
               if x.bit_count() <= anchors_max_weight]
    m = len(words)
    set_count = 1 << m
    all_families = [family_from_minima(a, set_count)
                    for a in antichains(set_count)]

    anchored = []
    for anchor in anchors:
        generators = []
        for bit in range(n_bits):
            subset = 0
            for i, word in enumerate(words):
                if ((word >> bit) & 1) == ((anchor >> bit) & 1):
                    subset |= 1 << i
            assert subset
            generators.append(subset)
        valid = [family for family in all_families
                 if all((family >> g) & 1 for g in generators)]
        anchored.extend((anchor, family) for family in valid)

    # One row per ordered pair; one column per anchor/semi-filter instance.
    pairs = list(product(range(set_count), repeat=2))
    cover = np.zeros((len(pairs), len(anchored)), dtype=np.uint8)
    for pi, (e, h) in enumerate(pairs):
        inter = e & h
        for fi, (_anchor, family) in enumerate(anchored):
            cover[pi, fi] = (
                ((family >> e) & 1)
                and ((family >> h) & 1)
                and not ((family >> inter) & 1)
            )

    # Minimize t subject to every pair covering at most t probability mass.
    a_ub = np.column_stack((cover.astype(float), -np.ones(len(pairs))))
    b_ub = np.zeros(len(pairs))
    a_eq = np.zeros((len(anchors), len(anchored) + 1))
    b_eq = np.full(len(anchors), 1 / len(anchors))
    for i, (anchor, _family) in enumerate(anchored):
        a_eq[anchors.index(anchor), i] = 1
    result = linprog(
        np.r_[np.zeros(len(anchored)), 1.0],
        A_ub=a_ub, b_ub=b_ub,
        A_eq=a_eq, b_eq=b_eq,
        bounds=[(0, None)] * len(anchored) + [(0, 1)],
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)

    weights = result.x[:-1]
    uniform = np.full(len(anchored), 1 / len(anchored))
    uniform_max = float(np.max(cover @ uniform))
    active = np.flatnonzero(result.x[-1] - cover @ weights < 1e-7)
    support = np.flatnonzero(weights > 1e-8)
    support_pair_count = cover[:, support].sum(axis=1)
    max_support_hits = int(support_pair_count.max())
    support_is_uniform = np.allclose(weights[support], 1 / len(anchors), atol=1e-8)
    per_anchor_support = {}
    for i in support:
        anchor, _family = anchored[i]
        per_anchor_support[anchor] = per_anchor_support.get(anchor, 0) + 1

    print(
        f"bits={n_bits}; |U|={m}; anchors={len(anchors)}; "
        f"anchored_filters={len(anchored)}; ordered_pairs={len(pairs)}"
    )
    print(f"uniform_anchor_filter_distribution_max_pair_mass={uniform_max:.9f}")
    print(f"exact_selected_support_max_pair_hits={max_support_hits}/{len(anchors)}; "
          f"equal_mass_support={support_is_uniform}")
    print(f"LP_minimax_max_pair_mass={result.fun:.9f}; support_size={len(support)}; "
          f"active_pairs={len(active)}")
    print("positive_support_per_anchor=" + str(sorted(per_anchor_support.items())))
    dual_value = float(b_eq @ result.eqlin.marginals)
    print(f"LP_primal_residual_max={np.max(np.abs(a_eq @ result.x - b_eq)):.3g}; "
          f"LP_dual_value={dual_value:.9f}")

    def fmt_set(subset):
        return "{" + ",".join(format(words[j], f"0{n_bits}b")
                               for j in range(m) if (subset >> j) & 1) + "}"

    for i in support:
        anchor, family = anchored[i]
        minima = []
        for subset in range(1, set_count):
            if not ((family >> subset) & 1):
                continue
            if all(not ((family >> (subset ^ (1 << bit))) & 1)
                   for bit in range(m) if (subset >> bit) & 1):
                minima.append(subset)
        print(f"  mass={weights[i]:.9f}; anchor={format(anchor, f'0{n_bits}b')}; "
              f"minimal_members={[fmt_set(x) for x in minima]}")


def main():
    # Exact instances previously used in the audit.
    run_model(n_bits=3, min_weight=2, anchors_max_weight=1)
    run_model(n_bits=4, min_weight=3, anchors_max_weight=2)


if __name__ == "__main__":
    main()
