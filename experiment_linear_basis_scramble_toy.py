"""Check one-pair collapse under every invertible 3-bit linear basis change.

The toy promise has low anchors of weight at most one and high points of
weight at least two. For each GL(3,2) transform, the transformed coordinates
define the forced literal slices. The exact universal one-pair criterion is:
the endpoints are disjoint and each contains a matching generator at every
anchor. This is a diagnostic for the proposed fast-basis-scrambling route.
"""

from __future__ import annotations

from itertools import product


N = 3
ANCHORS = tuple(x for x in range(1 << N) if x.bit_count() <= 1)
UNIVERSE = tuple(x for x in range(1 << N) if x.bit_count() >= 2)


def apply_matrix(rows: tuple[int, ...], word: int) -> int:
    result = 0
    for bit, row in enumerate(rows):
        result |= ((row & word).bit_count() & 1) << bit
    return result


def invertible(rows: tuple[int, ...]) -> bool:
    images = {apply_matrix(rows, x) for x in range(1 << N)}
    return len(images) == (1 << N)


def mask(points: set[int], index: dict[int, int]) -> int:
    return sum(1 << index[x] for x in points)


def evaluate_basis(rows: tuple[int, ...]) -> tuple[int, int]:
    encoded_anchors = tuple(apply_matrix(rows, a) for a in ANCHORS)
    encoded_universe = tuple(apply_matrix(rows, x) for x in UNIVERSE)
    index = {x: i for i, x in enumerate(encoded_universe)}
    generators = []
    for anchor in encoded_anchors:
        generators.append([
            mask({x for x in encoded_universe
                  if ((x >> bit) & 1) == ((anchor >> bit) & 1)}, index)
            for bit in range(N)
        ])

    full = (1 << len(ANCHORS)) - 1
    endpoint_masks = range(1 << len(UNIVERSE))
    one_pair_count = 0
    first_witness = None
    for left, right in product(endpoint_masks, repeat=2):
        if left & right:
            continue
        if all(
            any((generator & left) == generator for generator in gens)
            and any((generator & right) == generator for generator in gens)
            for gens in generators
        ):
            one_pair_count += 1
            if first_witness is None:
                first_witness = (left, right)
    assert (first_witness is not None) == (one_pair_count > 0)
    return one_pair_count, full


def direct_cover_check(
    generators: list[list[int]],
    rules: tuple[tuple[int, int, int], ...],
) -> bool:
    all_subsets = range(1 << len(UNIVERSE))
    for gens in generators:
        closure = {s for s in all_subsets
                   if any((s & gen) == gen for gen in gens)}
        changed = True
        while changed:
            additions = set()
            for e, h, meet in rules:
                if e in closure and h in closure:
                    additions.update(s for s in all_subsets
                                     if (s & meet) == meet)
            updated = closure | additions
            changed = updated != closure
            closure = updated
        if 0 not in closure:
            return False
    return True


def find_two_rule_cover(
    rows: tuple[int, ...],
) -> tuple[tuple[int, int, int], tuple[int, int, int]] | None:
    encoded_anchors = tuple(apply_matrix(rows, a) for a in ANCHORS)
    encoded_universe = tuple(apply_matrix(rows, x) for x in UNIVERSE)
    index = {x: i for i, x in enumerate(encoded_universe)}
    generators = [
        [mask({x for x in encoded_universe
               if ((x >> bit) & 1) == ((anchor >> bit) & 1)}, index)
         for bit in range(N)]
        for anchor in encoded_anchors
    ]
    full = (1 << len(ANCHORS)) - 1
    endpoint_masks = range(1 << len(UNIVERSE))
    rules = [(e, h, e & h) for e, h in product(endpoint_masks, repeat=2)]

    def initial_support(carrier: int) -> int:
        result = 0
        for ai, gens in enumerate(generators):
            if any((carrier & gen) == gen for gen in gens):
                result |= 1 << ai
        return result

    for first in rules:
        e1, h1, k1 = first
        for second in rules:
            e2, h2, k2 = second
            carriers = {0, e1, h1, k1, e2, h2, k2}
            supports = {carrier: initial_support(carrier)
                        for carrier in carriers}
            changed = True
            while changed and supports[0] != full:
                changed = False
                for e, h, meet in (first, second):
                    gained = supports[e] & supports[h]
                    if not gained:
                        continue
                    for carrier in carriers:
                        if (carrier & meet) == meet:
                            updated = supports[carrier] | gained
                            if updated != supports[carrier]:
                                supports[carrier] = updated
                                changed = True
            if supports[0] == full:
                witness = (first, second)
                assert direct_cover_check(generators, witness)
                return witness
    return None


def main() -> None:
    matrices = [rows for rows in product(range(1 << N), repeat=N)
                if invertible(rows)]
    assert len(matrices) == 168
    collapse_counts = []
    for rows in matrices:
        count, _ = evaluate_basis(rows)
        collapse_counts.append(count)
    distribution = {
        count: collapse_counts.count(count)
        for count in sorted(set(collapse_counts))
    }
    print(f"invertible_matrices={len(matrices)}; one_pair_profile_counts="
          f"{distribution}")
    print(f"bases_with_one_pair_cover="
          f"{sum(count > 0 for count in collapse_counts)}/{len(matrices)}")
    one_pair_bases = {rows for rows, count in zip(matrices, collapse_counts)
                      if count > 0}
    remaining = [rows for rows in matrices if rows not in one_pair_bases]
    witnesses = {rows: find_two_rule_cover(rows) for rows in remaining}
    two_pair_bases = [rows for rows, witness in witnesses.items()
                      if witness is not None]
    print(f"bases_with_no_one_pair_but_two_rule_cover="
          f"{len(two_pair_bases)}/{len(remaining)}")
    two_disjoint_profiles = [
        rows for rows, witness in witnesses.items()
        if witness is not None and witness[0][2] == 0 and witness[1][2] == 0
    ]
    one_disjoint_seed = [
        rows for rows, witness in witnesses.items()
        if witness is not None
        and sum(rule[2] == 0 for rule in witness) == 1
    ]
    print(f"of_those_with_two_disjoint_profile_pairs="
          f"{len(two_disjoint_profiles)}/{len(remaining)}")
    print(f"of_those_with_one_disjoint_seed_and_one_relay="
          f"{len(one_disjoint_seed)}/{len(remaining)}")
    if len(two_pair_bases) != len(remaining):
        print("first_basis_without_two_rule_cover="
              f"{next(rows for rows in remaining if witnesses[rows] is None)}")
    elif two_pair_bases:
        print(f"sample_two_rule_basis={two_pair_bases[0]}; "
              f"sample_rules={witnesses[two_pair_bases[0]]}")


if __name__ == "__main__":
    main()
