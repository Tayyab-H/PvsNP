"""Exact check of a two-variable 2-SAT counterexample to contractibility."""
from itertools import product


def satisfies(x: int, y: int) -> bool:
    # F = (x OR y) AND (NOT x OR NOT y)
    return bool((x or y) and ((not x) or (not y)))


vertices = {bits for bits in product((0, 1), repeat=2) if satisfies(*bits)}
edges = set()
for u in vertices:
    for v in vertices:
        if sum(a != b for a, b in zip(u, v)) == 1:
            edges.add(tuple(sorted((u, v))))

# A 1-dimensional cubical complex with these vertices has no 2-cells.
assert vertices == {(0, 1), (1, 0)}
assert not edges
assert len(vertices) == 2
assert len(edges) == 0
assert len(vertices) - len(edges) == 2  # beta_0 = 2

print(f"satisfying_vertices={sorted(vertices)}")
print(f"cubical_edges={sorted(edges)}")
print("connected_components=2; beta_0=2; complex is not contractible")
