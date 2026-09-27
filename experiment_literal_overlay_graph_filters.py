"""Exact test of graph-edge witnesses under the matching-literal overlay.

Six anchor strings index a cycle C6. Each anchor receives all matching
coordinate-literal generators on the weight-three 5-bit shell, plus a 2-point
generator for each incident cycle edge. A random injection maps cycle vertices
to six shell points. For every assignment, all 1,048,576 ordered endpoint
pairs are checked exactly. This directly tests whether literals destroy the
graph chromatic-cover lower bound on a small toy.
"""

from __future__ import annotations

import random
from itertools import combinations

import numpy as np


N = 5
UNIVERSE = [x for x in range(1 << N) if x.bit_count() == 3]
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 1]
GRAPH_EDGES = [(i, (i + 1) % len(ANCHORS)) for i in range(len(ANCHORS))]
ENDPOINT_COUNT = 1 << len(UNIVERSE)
PAIR_COUNT = ENDPOINT_COUNT * ENDPOINT_COUNT
TARGET = (1 << len(ANCHORS)) - 1


def literal_generators(anchor):
    return [sum(1 << i for i, point in enumerate(UNIVERSE)
                if ((point >> bit) & 1) == ((anchor >> bit) & 1))
            for bit in range(N)]


def exact_cover_number(token_assignment):
    endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    left = np.repeat(endpoints, ENDPOINT_COUNT)
    right = np.tile(endpoints, ENDPOINT_COUNT)
    common = np.bitwise_and(left, right)
    codes = np.zeros(PAIR_COUNT, dtype=np.uint8)
    families = [literal_generators(a) for a in ANCHORS]
    for i, j in GRAPH_EDGES:
        witness = (1 << token_assignment[i]) | (1 << token_assignment[j])
        families[i].append(witness)
        families[j].append(witness)
    for ai, family in enumerate(families):
        accepted = np.zeros(ENDPOINT_COUNT, dtype=np.bool_)
        for witness in family:
            accepted |= (np.bitwise_and(endpoints, witness) == witness)
        covers = accepted[left] & accepted[right] & ~accepted[common]
        codes |= covers.astype(np.uint8) << ai

    masks = np.unique(codes)
    masks = masks[masks != 0]
    if TARGET in masks:
        flat = int(np.flatnonzero(codes == TARGET)[0])
        return 1, max(int(m).bit_count() for m in masks), len(masks), (flat // ENDPOINT_COUNT, flat % ENDPOINT_COUNT), families

    supersets = np.zeros(1 << len(ANCHORS), dtype=np.bool_)
    supersets[masks] = True
    all_masks = np.arange(1 << len(ANCHORS), dtype=np.uint8)
    for bit in range(len(ANCHORS)):
        no_bit = all_masks[(all_masks & (1 << bit)) == 0]
        supersets[no_bit] |= supersets[no_bit | (1 << bit)]
    if any(supersets[TARGET ^ int(mask)] for mask in masks):
        return 2, max(int(m).bit_count() for m in masks), len(masks), None, families

    pair_unions = {int(x) | int(y) for x in masks for y in masks}
    if any(supersets[TARGET ^ union] for union in pair_unions):
        return 3, max(int(m).bit_count() for m in masks), len(masks), None, families
    return 4, max(int(m).bit_count() for m in masks), len(masks), None, families


def main(trials=25):
    rng = random.Random(20260924)
    assignments = []
    canonical = tuple(range(len(ANCHORS)))
    assignments.append(canonical)
    while len(assignments) < trials:
        candidate = tuple(rng.sample(range(len(UNIVERSE)), len(ANCHORS)))
        if candidate not in assignments:
            assignments.append(candidate)

    histogram = {}
    best = None
    for assignment in assignments:
        cover, cap, masks, pair, families = exact_cover_number(assignment)
        histogram[cover] = histogram.get(cover, 0) + 1
        row = (cover, -cap, assignment, cap, masks, pair, families)
        if best is None or row < best:
            best = row
    assert best is not None
    print(f"universe={len(UNIVERSE)}; anchors={len(ANCHORS)}; graph=C6; trials={trials}; exact_endpoint_pairs_per_trial={PAIR_COUNT}; cover_histogram={dict(sorted(histogram.items()))}")
    print(f"best_cover={best[0]}; maximum_single_pair={best[3]}/{len(ANCHORS)}; distinct_profiles={best[4]}; token_assignment={best[2]}")
    if best[5] is not None:
        left, right = best[5]
        common = left & right
        point_list = lambda mask: [UNIVERSE[i] for i in range(len(UNIVERSE)) if mask >> i & 1]
        print(f"  E={point_list(left)}; H={point_list(right)}; intersection={point_list(common)}")
        literal_only_profile = []
        for ai, family in enumerate(best[6]):
            literal_count = len(literal_generators(ANCHORS[ai]))
            base = literal_generators(ANCHORS[ai])
            literal_only_ok = (any(left & g == g for g in base)
                               and any(right & g == g for g in base)
                               and not any(common & g == g for g in base))
            if literal_only_ok:
                literal_only_profile.append(ANCHORS[ai])
            def source(endpoint):
                for j, generator in enumerate(family):
                    if endpoint & generator == generator:
                        return f"literal[{j}]" if j < literal_count else f"graph_edge[{j - literal_count}]"
                return None
            left_source = source(left)
            right_source = source(right)
            print(f"  anchor={ANCHORS[ai]}; E_witness={left_source}; H_witness={right_source}; intersection_accepts={any(common & g == g for g in family)}")
        print(f"  literal_only_covered_anchors={literal_only_profile}")


if __name__ == "__main__":
    main()
