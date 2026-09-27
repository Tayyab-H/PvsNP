"""Exact toy check of the support-intersection graph cover bound."""
from fractions import Fraction

supports = [
    {0, 1, 2},
    {2, 3, 4},
    {4, 5, 6},
    {6, 7, 8},
    {9, 10, 11},
]
colors = [0, 1, 0, 1, 0]  # a proper 2-coloring of a path plus an isolate
assert len(supports) == len(colors)

adjacency = [set() for _ in supports]
for i in range(len(supports)):
    for j in range(i + 1, len(supports)):
        if supports[i] & supports[j]:
            adjacency[i].add(j)
            adjacency[j].add(i)
            assert colors[i] != colors[j]

pairs = []
for color in sorted(set(colors)):
    A, B, C = set(), set(), set()
    class_indices = [i for i, c in enumerate(colors) if c == color]
    class_supports = [supports[i] for i in class_indices]
    assert all(not (class_supports[i] & class_supports[j])
               for i in range(len(class_supports))
               for j in range(i + 1, len(class_supports)))
    for support in class_supports:
        x, y, z = sorted(support)
        A.add(x)
        B.add(y)
        C.add(z)
    pairs.append((A | B, B | C))

for i, support in enumerate(supports):
    E, H = pairs[colors[i]]
    mass_E = Fraction(len(E & support), len(support))
    mass_H = Fraction(len(H & support), len(support))
    mass_intersection = Fraction(len(E & H & support), len(support))
    assert mass_E > Fraction(1, 2)
    assert mass_H > Fraction(1, 2)
    assert mass_intersection <= Fraction(1, 2)

print(f"measures={len(supports)}; support_graph_edges={sum(map(len, adjacency)) // 2}; colors={len(pairs)}")
print(f"cover_pairs={len(pairs)}; every selected majority filter is violated exactly")
print(f"point_overlap_max=2; support_size=3; degree_bound<=3*(2-1)=3; chromatic_bound<=4")
