"""Search a higher-chromatic coded graph lift under literal generators.

There are 16 anchors on the 5-bit weight-three shell. A fixed graph contains
K4 and gives every other anchor degree two. Each anchor gets matching literal
generators plus one 2-point code-union witness per incident graph edge. The
graph-only profile argument would force independent anchor sets; arbitrary
literal and mixed witnesses may defeat it. Each sampled code assignment is
checked against all 1,048,576 ordered endpoint pairs.
"""

from __future__ import annotations

import random
from itertools import combinations

import numpy as np


N = 5
UNIVERSE = [x for x in range(1 << N) if x.bit_count() == 3]
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 2]
M = len(ANCHORS)
ENDPOINT_COUNT = 1 << len(UNIVERSE)
PAIR_COUNT = ENDPOINT_COUNT * ENDPOINT_COUNT
TARGET = (1 << M) - 1


GRAPH_EDGES = set(combinations(range(4), 2))
for i in range(4, M):
    j = i - 4
    GRAPH_EDGES.add(tuple(sorted((i, j % 4))))
    GRAPH_EDGES.add(tuple(sorted((i, (j + 1) % 4))))
GRAPH_EDGES = sorted(GRAPH_EDGES)
NEIGHBORS = [[j for a, j in GRAPH_EDGES if a == i]
             + [a for a, j in GRAPH_EDGES if j == i]
             for i in range(M)]


def literal_generators(anchor):
    return [sum(1 << i for i, point in enumerate(UNIVERSE)
                if ((point >> bit) & 1) == ((anchor >> bit) & 1))
            for bit in range(N)]


def exact_pair_masks(codes, include_graph=True):
    endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    left = np.repeat(endpoints, ENDPOINT_COUNT)
    right = np.tile(endpoints, ENDPOINT_COUNT)
    common = np.bitwise_and(left, right)
    coverage = np.zeros(PAIR_COUNT, dtype=np.uint16)
    families = []
    for ai, anchor in enumerate(ANCHORS):
        family = literal_generators(anchor)
        if include_graph:
            for neighbor in NEIGHBORS[ai]:
                family.append(codes[ai] | codes[neighbor])
        families.append(family)
        accepted = np.zeros(ENDPOINT_COUNT, dtype=np.bool_)
        for witness in family:
            accepted |= (np.bitwise_and(endpoints, witness) == witness)
        covers = accepted[left] & accepted[right] & ~accepted[common]
        coverage |= covers.astype(np.uint16) << ai
    return coverage, families


def has_superset_table(masks):
    has = np.zeros(1 << M, dtype=np.bool_)
    has[masks] = True
    all_masks = np.arange(1 << M, dtype=np.uint32)
    for bit in range(M):
        no_bit = all_masks[(all_masks & (1 << bit)) == 0]
        has[no_bit] |= has[no_bit | (1 << bit)]
    return has


def cover_witness(codes):
    masks = np.unique(codes)
    masks = masks[masks != 0]
    if not masks.size or int(np.bitwise_or.reduce(masks)) != TARGET:
        return None, masks, None
    if TARGET in masks:
        flat = int(np.flatnonzero(codes == TARGET)[0])
        return 1, masks, [(flat // ENDPOINT_COUNT, flat % ENDPOINT_COUNT, TARGET)]
    has = has_superset_table(masks)
    for first in masks:
        missing = TARGET ^ int(first)
        if has[missing]:
            second = next(int(m) for m in masks if int(m) & missing == missing)
            return 2, masks, [
                (int(np.flatnonzero(codes == first)[0]) // ENDPOINT_COUNT,
                 int(np.flatnonzero(codes == first)[0]) % ENDPOINT_COUNT, int(first)),
                (int(np.flatnonzero(codes == second)[0]) // ENDPOINT_COUNT,
                 int(np.flatnonzero(codes == second)[0]) % ENDPOINT_COUNT, second),
            ]

    # If the profile family is large, exact triple checking by quadratic
    # enumeration is not the best next step. A certified absence of a
    # one/two-cover is already a finite positive obstruction.
    if len(masks) > 1500:
        return 3, masks, None
    pair_unions = set()
    for i, first in enumerate(masks):
        for second in masks[i:]:
            pair_unions.add(int(first) | int(second))
    for union in pair_unions:
        missing = TARGET ^ union
        if has[missing]:
            a, b = next((int(x), int(y)) for x in masks for y in masks
                        if (int(x) | int(y)) == union)
            c = next(int(m) for m in masks if int(m) & missing == missing)
            result = []
            for mask in (a, b, c):
                flat = int(np.flatnonzero(codes == mask)[0])
                result.append((flat // ENDPOINT_COUNT, flat % ENDPOINT_COUNT, mask))
            return 3, masks, result
    return 4, masks, None


def main(trials=30):
    rng = random.Random(20260924)
    code_pool = [sum(1 << i for i in pair)
                 for pair in combinations(range(len(UNIVERSE)), 2)]
    seen = set()
    histogram = {}
    examples = []
    single_example = None
    for trial in range(trials):
        codes = tuple(code_pool[:M]) if trial == 0 else tuple(rng.sample(code_pool, M))
        if codes in seen:
            continue
        seen.add(codes)
        pair_codes, families = exact_pair_masks(codes)
        cover, masks, witness = cover_witness(pair_codes)
        if cover is None:
            histogram["not_individually_coverable"] = histogram.get("not_individually_coverable", 0) + 1
            continue
        histogram[f"at_least_{cover}" if cover in (3, 4) and witness is None else str(cover)] = histogram.get(f"at_least_{cover}" if cover in (3, 4) and witness is None else str(cover), 0) + 1
        if cover == 1 and single_example is None:
            single_example = (trial, codes, witness, families)
        if cover >= 3 and len(examples) < 3:
            examples.append((trial, codes, cover, len(masks), witness, families))
    print(f"universe={len(UNIVERSE)}; anchors={M}; graph_edges={len(GRAPH_EDGES)}; graph_min_degree={min(map(len,NEIGHBORS))}; trials={trials}; exact_pairs_per_trial={PAIR_COUNT}; cover_histogram={dict(sorted(histogram.items()))}")
    if single_example is not None:
        trial, codes, witness, families = single_example
        literal_codes, _ = exact_pair_masks(codes, include_graph=False)
        literal_cover, literal_masks, _ = cover_witness(literal_codes)
        left, right, _ = witness[0]
        common = left & right
        points = lambda mask: [UNIVERSE[i] for i in range(len(UNIVERSE)) if mask >> i & 1]
        print(f"one_pair_example=trial{trial}; code_sizes={[c.bit_count() for c in codes]}; literal_only_cover_lower_bound={literal_cover}; literal_only_max_profile={max(int(m).bit_count() for m in literal_masks)}/{M}; E={points(left)}; H={points(right)}; intersection={points(common)}")
        literal_profile = []
        for ai, anchor in enumerate(ANCHORS):
            literals = literal_generators(anchor)
            left_gen = next((j for j, g in enumerate(families[ai]) if left & g == g), None)
            right_gen = next((j for j, g in enumerate(families[ai]) if right & g == g), None)
            left_label = f"literal{left_gen}" if left_gen is not None and left_gen < len(literals) else f"edge{left_gen-len(literals)}"
            right_label = f"literal{right_gen}" if right_gen is not None and right_gen < len(literals) else f"edge{right_gen-len(literals)}"
            literal_ok = (any(left & g == g for g in literals)
                          and any(right & g == g for g in literals)
                          and not any(common & g == g for g in literals))
            if literal_ok:
                literal_profile.append(anchor)
            print(f"  anchor={anchor}; E={left_label}; H={right_label}; intersection_accepts={any(common & g == g for g in families[ai])}")
        print(f"  literal_only_profile={literal_profile}")
    for trial, codes, cover, mask_count, witness, families in examples:
        print(f"positive_toy_trial={trial}; cover_at_least={cover}; profiles={mask_count}; anchor_code_sizes={[c.bit_count() for c in codes]}")
        if witness:
            for left, right, profile in witness:
                p = lambda mask: [UNIVERSE[i] for i in range(len(UNIVERSE)) if mask >> i & 1]
                print(f"  E={p(left)}; H={p(right)}; covered={[ANCHORS[i] for i in range(M) if profile >> i & 1]}")


if __name__ == "__main__":
    main()
