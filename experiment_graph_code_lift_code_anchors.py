"""Test whether distance-three anchors resist literal-assisted graph fusion.

Anchors are the eight words of a shortened [7,3,4] simplex code, hence have
minimum distance three. The ten-point universe is a balanced subset of the
6-bit weight-two shell. A K4-core graph supplies 2-point union witnesses for
its edges; every filter also contains all matching coordinate literals.
Each sampled injection of graph tokens is checked against all 1,048,576
ordered endpoint pairs.
"""

from __future__ import annotations

import random
from itertools import combinations

import numpy as np


N = 6
COLUMNS = (1, 2, 3, 4, 5, 6)
ANCHORS = [sum(((x & col).bit_count() & 1) << i
               for i, col in enumerate(COLUMNS)) for x in range(8)]
UNIVERSE = [sum(1 << i for i in pair) for pair in
            ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0),
             (0, 3), (1, 4), (2, 5), (0, 2))]
M = len(ANCHORS)
ENDPOINT_COUNT = 1 << len(UNIVERSE)
PAIR_COUNT = ENDPOINT_COUNT * ENDPOINT_COUNT
TARGET = (1 << M) - 1


assert len(set(ANCHORS)) == M
assert min((a ^ b).bit_count() for a, b in combinations(ANCHORS, 2)) == 3
assert all(any((u >> i) & 1 for u in UNIVERSE)
           and any(not ((u >> i) & 1) for u in UNIVERSE) for i in range(N))

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


def exact_pair_codes(tokens, include_literals=True, include_edges=True):
    endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    left = np.repeat(endpoints, ENDPOINT_COUNT)
    right = np.tile(endpoints, ENDPOINT_COUNT)
    common = np.bitwise_and(left, right)
    codes = np.zeros(PAIR_COUNT, dtype=np.uint8)
    families = []
    for ai, anchor in enumerate(ANCHORS):
        family = literal_generators(anchor) if include_literals else []
        if include_edges:
            family.extend(tokens[ai] | tokens[j] for j in NEIGHBORS[ai])
        families.append(family)
        accepted = np.zeros(ENDPOINT_COUNT, dtype=np.bool_)
        for witness in family:
            accepted |= (np.bitwise_and(endpoints, witness) == witness)
        covers = accepted[left] & accepted[right] & ~accepted[common]
        codes |= covers.astype(np.uint8) << ai
    return codes, families


def superset_table(masks):
    table = np.zeros(1 << M, dtype=np.bool_)
    table[masks] = True
    all_masks = np.arange(1 << M, dtype=np.uint32)
    for bit in range(M):
        no_bit = all_masks[(all_masks & (1 << bit)) == 0]
        table[no_bit] |= table[no_bit | (1 << bit)]
    return table


def cover_status(codes):
    masks = np.unique(codes)
    masks = masks[masks != 0]
    if not masks.size or int(np.bitwise_or.reduce(masks)) != TARGET:
        return None, masks, None
    if TARGET in masks:
        flat = int(np.flatnonzero(codes == TARGET)[0])
        return 1, masks, [(flat // ENDPOINT_COUNT, flat % ENDPOINT_COUNT, TARGET)]
    has = superset_table(masks)
    for first in masks:
        missing = TARGET ^ int(first)
        if has[missing]:
            second = next(int(m) for m in masks if int(m) & missing == missing)
            result = []
            for mask in (int(first), second):
                flat = int(np.flatnonzero(codes == mask)[0])
                result.append((flat // ENDPOINT_COUNT, flat % ENDPOINT_COUNT, mask))
            return 2, masks, result
    pair_unions = {int(a) | int(b) for a in masks for b in masks}
    for union in pair_unions:
        missing = TARGET ^ union
        if has[missing]:
            first, second = next((int(a), int(b)) for a in masks for b in masks
                                 if int(a) | int(b) == union)
            third = next(int(m) for m in masks if int(m) & missing == missing)
            result = []
            for mask in (first, second, third):
                flat = int(np.flatnonzero(codes == mask)[0])
                result.append((flat // ENDPOINT_COUNT, flat % ENDPOINT_COUNT, mask))
            return 3, masks, result
    return 4, masks, None


def main(trials=100):
    rng = random.Random(20260924)
    code_pool = [sum(1 << i for i in pair)
                 for pair in combinations(range(len(UNIVERSE)), 2)]
    histogram = {}
    positive = None
    first_one = None
    for trial in range(trials):
        tokens = tuple(rng.sample(code_pool, M))
        codes, families = exact_pair_codes(tokens)
        cover, masks, witness = cover_status(codes)
        key = "not_individually_coverable" if cover is None else ("at_least_4" if cover == 4 else str(cover))
        histogram[key] = histogram.get(key, 0) + 1
        if cover is not None and cover >= 3 and positive is None:
            positive = trial, tokens, cover, len(masks), witness, families
        if cover == 1 and first_one is None:
            first_one = trial, tokens, codes, families
    print(f"anchors={M}; anchor_min_distance=3; universe={len(UNIVERSE)}; graph_edges={len(GRAPH_EDGES)}; trials={trials}; exact_pairs_per_trial={PAIR_COUNT}; cover_histogram={dict(sorted(histogram.items()))}")
    if positive is not None:
        trial, tokens, cover, profile_count, witness, families = positive
        print(f"first_cover_lower_bound={cover}; trial={trial}; profiles={profile_count}; token_sizes={[t.bit_count() for t in tokens]}")
        if witness:
            fmt = lambda mask: [UNIVERSE[i] for i in range(len(UNIVERSE)) if mask >> i & 1]
            for left, right, profile in witness:
                print(f"  E={fmt(left)}; H={fmt(right)}; covered={[ANCHORS[i] for i in range(M) if profile >> i & 1]}")
    if first_one is not None:
        trial, tokens, codes, families = first_one
        literal_codes, _ = exact_pair_codes(tokens, include_edges=False)
        literal_cover, literal_masks, _ = cover_status(literal_codes)
        flat = int(np.flatnonzero(codes == TARGET)[0])
        left, right = flat // ENDPOINT_COUNT, flat % ENDPOINT_COUNT
        common = left & right
        fmt = lambda mask: [UNIVERSE[i] for i in range(len(UNIVERSE)) if mask >> i & 1]
        print(f"first_one_pair_trial={trial}; literal_only_cover={literal_cover}; literal_profiles={len(literal_masks)}")
        print(f"  E={fmt(left)}; H={fmt(right)}; intersection={fmt(common)}")
        if literal_cover == 1:
            literal_flat = int(np.flatnonzero(literal_codes == TARGET)[0])
            literal_left = literal_flat // ENDPOINT_COUNT
            literal_right = literal_flat % ENDPOINT_COUNT
            literal_common = literal_left & literal_right
            overlaid_profile = int(codes[literal_flat])
            print(f"literal_only_witness: E={fmt(literal_left)}; H={fmt(literal_right)}; intersection={fmt(literal_common)}; after_graph_overlay_covers={[ANCHORS[i] for i in range(M) if overlaid_profile >> i & 1]}")
            for ai, anchor in enumerate(ANCHORS):
                lits = literal_generators(anchor)
                ew = [i for i, g in enumerate(lits) if g & literal_left == g]
                hw = [i for i, g in enumerate(lits) if g & literal_right == g]
                iw = [i for i, g in enumerate(lits) if g & literal_common == g]
                blocked_edges = [j for j in NEIGHBORS[ai]
                                 if (tokens[ai] | tokens[j]) & literal_common == (tokens[ai] | tokens[j])]
                print(f"  literal_anchor={anchor:06b}; E_coordinates={ew}; H_coordinates={hw}; intersection_coordinates={iw}; graph_witnesses_in_intersection={blocked_edges}")
        for ai, anchor in enumerate(ANCHORS):
            def accepted_witnesses(endpoint):
                return [("lit", bit) for bit in range(N)
                        if literal_generators(anchor)[bit] & endpoint == literal_generators(anchor)[bit]] + [
                    ("edge", j) for j in NEIGHBORS[ai]
                    if (tokens[ai] | tokens[j]) & endpoint == (tokens[ai] | tokens[j])]
            a_wits, b_wits = accepted_witnesses(left), accepted_witnesses(right)
            i_wits = accepted_witnesses(common)
            print(f"  anchor={anchor:06b}; E_witnesses={a_wits}; H_witnesses={b_wits}; intersection_witnesses={i_wits}")


if __name__ == "__main__":
    main()
