"""Toy check of disjoint sparse majority witnesses from Hamming spheres.

This tests the finite combinatorics used in Corollary 18.7. Random k-flips
are not certified high-circuit-complexity truth tables; the script makes no
such claim.
"""
import random

SEED = 20260923
N = 4096
ANCHORS = 5
RADIUS = 16
SUPPORT_SIZE = 469  # strictly greater than the 468 threshold

rng = random.Random(SEED)
anchors = [tuple(rng.randrange(2) for _ in range(N)) for _ in range(ANCHORS)]
supports = []
used = set()

for anchor in anchors:
    support = set()
    while len(support) < SUPPORT_SIZE:
        point = list(anchor)
        for i in rng.sample(range(N), RADIUS):
            point[i] ^= 1
        point = tuple(point)
        if point not in used:
            support.add(point)
    assert len(support) == SUPPORT_SIZE
    assert not (support & used)
    used.update(support)
    supports.append(support)

max_disagreements = 0
for anchor, support in zip(anchors, supports):
    disagreements = [sum(point[i] != anchor[i] for point in support) for i in range(N)]
    max_disagreements = max(max_disagreements, max(disagreements))
    assert all(2 * count < SUPPORT_SIZE for count in disagreements)

# Give each distinct support point one of the three parts. For each measure,
# all three parts must stay strictly below half; this induces a violating pair.
color = {point: rng.randrange(3) for support in supports for point in support}
part_counts = []
for support in supports:
    counts = [sum(color[point] == c for point in support) for c in range(3)]
    assert all(2 * count < SUPPORT_SIZE for count in counts)
    a, b, c = counts
    assert 2 * (a + b) > SUPPORT_SIZE
    assert 2 * (b + c) > SUPPORT_SIZE
    assert 2 * b < SUPPORT_SIZE
    part_counts.append(counts)

assert 468 < SUPPORT_SIZE
print(f"seed={SEED}; truth_table_length={N}; anchors={ANCHORS}; radius={RADIUS}")
print(f"support_size={SUPPORT_SIZE}; supports_pairwise_disjoint={len(used) == ANCHORS * SUPPORT_SIZE}")
print(f"coordinatewise_anchor_majority_verified={len(supports)} / {ANCHORS}; max_disagreements={max_disagreements}")
print(f"three-part violating pair verified={len(part_counts)} / {ANCHORS}; first_part_counts={part_counts[0]}")
print("Random flips are a toy combinatorial model, not a circuit-complexity certificate.")
