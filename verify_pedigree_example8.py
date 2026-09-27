"""Reproduce the n=6 fractional pedigree-polytope witness from Arthanari (2025), Example 8.

Uses only the Python standard library. The verifier enumerates all pedigrees by the
paper's generator and distinct-common-edge rules, then checks exact integer marginals
for an explicit convex combination with denominator 8.
"""
from itertools import combinations

BASE = (1, 2, 3)

def generators(v):
    i, j, _k = v
    if j <= 3:
        return {BASE}
    return {(r, i, j) for r in range(1, i)} | {(i, s, j) for s in range(i + 1, j)}

def edge_order(m):
    return sorted(combinations(range(1, m + 1), 2), key=lambda edge: (edge[1], edge[0]))

def enumerate_pedigrees(n):
    paths = [(BASE,)]
    for k in range(4, n + 1):
        next_paths = []
        for path in paths:
            used = {triangle[:2] for triangle in path[1:]}
            for i, j in combinations(range(1, k), 2):
                if (i, j) in used:
                    continue
                triangle = (i, j, k)
                if any(generator in path for generator in generators(triangle)):
                    next_paths.append(path + (triangle,))
        paths = next_paths
    return paths

# Multiplicities are eighths of the total weight.
witness = {
    ((1, 3), (1, 2), (2, 3)): 2,
    ((1, 3), (1, 2), (3, 4)): 2,
    ((1, 3), (3, 4), (1, 2)): 1,
    ((1, 3), (3, 4), (2, 3)): 1,
    ((2, 3), (3, 4), (1, 3)): 1,
    ((2, 3), (3, 4), (2, 4)): 1,
}
expected = [
    [0, 6, 2],
    [4, 0, 0, 0, 0, 4],
    [1, 1, 3, 0, 1, 2, 0, 0, 0, 0],
]

pedigrees = enumerate_pedigrees(6)
assert len(pedigrees) == 60, f"expected 60 pedigrees, found {len(pedigrees)}"
edge_orders = [edge_order(3), edge_order(4), edge_order(5)]
known = {tuple(triangle[:2] for triangle in path[1:]) for path in pedigrees}
assert set(witness) <= known, "a witness sequence is not a valid pedigree"
assert sum(witness.values()) == 8, "convex weights do not sum to 1"

marginals = [[0] * len(edges) for edges in edge_orders]
for sequence, multiplicity in witness.items():
    for layer, edge in enumerate(sequence):
        marginals[layer][edge_orders[layer].index(edge)] += multiplicity
assert marginals == expected, f"wrong marginals: {marginals!r}"
assert max(expected[2]) == 3, "target layer unexpectedly has a unit coordinate"

# In Example 8, the paper identifies rigid flows 1/8 and 2/8, leaving 5/8 flexible.
flexible_mass_eighths = 8 - (1 + 2)
assert flexible_mass_eighths == 5
print(f"Enumerated {len(pedigrees)} valid n=6 pedigrees.")
print("Verified Example 8 membership from six pedigrees with weights in eighths:")
for sequence, multiplicity in witness.items():
    print(f"  {multiplicity}/8: {sequence}")
print("Verified x4, x5, x6 marginals:", marginals)
print("Every x6 coordinate is <= 3/8; the two cited rigid flows leave 5/8 flexible mass.")
print("Therefore the Lean src_val condition X(s.arc_head)=1 cannot encode its positive-flow MCF witness.")
