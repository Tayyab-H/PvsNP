"""Exhaust all one-extra-pair choices over the five-anchor six-point toy."""

from __future__ import annotations

from itertools import combinations, product

from experiment_literal_plus_sparse_witnesses import (
    ANCHORS,
    UNIVERSE,
    exact_cover_number,
    literal_generators,
)


def main() -> None:
    endpoint_count = 1 << len(UNIVERSE)
    endpoints = [(left, right) for left in range(endpoint_count)
                 for right in range(endpoint_count)]
    extras = [sum(1 << i for i in pair)
              for pair in combinations(range(len(UNIVERSE)), 2)]
    per_anchor: list[list[int]] = []

    for anchor in ANCHORS:
        literals = literal_generators(anchor)
        base = [any((g & endpoint) == g for g in literals)
                for endpoint in range(endpoint_count)]
        choices = []
        for extra in extras:
            covered_pairs = 0
            for pair_index, (left, right) in enumerate(endpoints):
                common = left & right
                left_ok = base[left] or (extra & left) == extra
                right_ok = base[right] or (extra & right) == extra
                common_ok = base[common] or (extra & common) == extra
                if left_ok and right_ok and not common_ok:
                    covered_pairs |= 1 << pair_index
            choices.append(covered_pairs)
        assert all(choices)
        per_anchor.append(choices)

    pair_intersections: dict[tuple[int, int], list[list[int]]] = {}
    for i, j in combinations(range(len(ANCHORS)), 2):
        pair_intersections[(i, j)] = [
            [per_anchor[i][wi] & per_anchor[j][wj] for wj in range(len(extras))]
            for wi in range(len(extras))
        ]

    four_subsets = []
    for missing in range(len(ANCHORS)):
        chosen = [i for i in range(len(ANCHORS)) if i != missing]
        four_subsets.append((missing, chosen))

    counts = {"one_pair": 0, "two_pairs": 0, "no_four_anchor_pair": 0}
    first_examples: dict[str, tuple[tuple[int, ...], list[list[int]]]] = {}
    for choice in product(range(len(extras)), repeat=len(ANCHORS)):
        has_four = False
        has_one = False
        for missing, (i, j, k, l) in four_subsets:
            common_four = (
                pair_intersections[(i, j)][choice[i]][choice[j]]
                & pair_intersections[(k, l)][choice[k]][choice[l]]
            )
            if common_four:
                has_four = True
                if common_four & per_anchor[missing][choice[missing]]:
                    has_one = True
                    break

        if has_one:
            counts["one_pair"] += 1
        elif has_four:
            counts["two_pairs"] += 1
            first_examples.setdefault("two_pairs", (choice, []))
        else:
            counts["no_four_anchor_pair"] += 1
            first_examples.setdefault("no_four_anchor_pair", (choice, []))

    print(f"candidate_assignments={len(extras)}^{len(ANCHORS)}")
    print(f"assignment_class_counts={counts}")
    for label, (choice, _) in first_examples.items():
        generators = [
            literal_generators(anchor) + [extras[w]]
            for anchor, w in zip(ANCHORS, choice)
        ]
        exact, max_pair, _, _ = exact_cover_number(generators)
        chosen_points = [
            [UNIVERSE[i] for i in range(len(UNIVERSE)) if extras[w] >> i & 1]
            for w in choice
        ]
        print(
            f"example={label}; special_witnesses={chosen_points}; "
            f"exact_cover={exact}; max_single_pair={max_pair}/{len(ANCHORS)}"
        )


if __name__ == "__main__":
    main()
