"""Verify rank-parameter branching for affine controls of AND gates.

This experiment checks the known Rank Vertex Cover reduction used by the
project's affine/AND SAT formulation. It is finite evidence for this code,
not a complexity proof; the general branching proof is recorded in the audit.
"""

from itertools import combinations, product
import random


def reduce_vector(vector, basis):
    for pivot, row in basis:
        if (vector >> pivot) & 1:
            vector ^= row
    return vector


def add_to_basis(vector, basis):
    reduced = reduce_vector(vector, basis)
    if reduced == 0:
        return None
    pivot = reduced.bit_length() - 1
    result = sorted((*basis, (pivot, reduced)), reverse=True)
    return result


def in_span(vector, basis):
    return reduce_vector(vector, basis) == 0


def vector_rank(vectors):
    basis = []
    for vector in vectors:
        updated = add_to_basis(vector, basis)
        if updated is not None:
            basis = updated
    return len(basis)


def rank_cover(vectors, edges):
    """Return a minimum-rank edge cover by branching on uncovered edges."""
    full_rank = vector_rank(vectors)
    total_nodes = 0

    def decision(budget):
        nonlocal total_nodes

        def visit(basis):
            nonlocal total_nodes
            total_nodes += 1
            uncovered = next(
                ((left, right) for left, right in edges
                 if not in_span(vectors[left], basis)
                 and not in_span(vectors[right], basis)),
                None,
            )
            if uncovered is None:
                cover = {
                    left if in_span(vectors[left], basis) else right
                    for left, right in edges
                }
                assert all(
                    in_span(vectors[left], basis)
                    or in_span(vectors[right], basis)
                    for left, right in edges
                )
                assert all(in_span(vectors[v], basis) for v in cover)
                assert vector_rank([vectors[v] for v in cover]) <= len(basis)
                return cover
            if len(basis) >= budget:
                return None

            left, right = uncovered
            for vertex in dict.fromkeys((left, right)):
                extended = add_to_basis(vectors[vertex], basis)
                assert extended is not None
                result = visit(extended)
                if result is not None:
                    return result
            return None

        return visit([])

    for budget in range(full_rank + 1):
        cover = decision(budget)
        if cover is not None:
            optimum = vector_rank([vectors[v] for v in cover])
            assert optimum == budget, (vectors, edges, budget, optimum)
            return optimum, cover, total_nodes
    raise AssertionError("the full ground set is always a vertex cover")


def brute_rank_cover(vectors, edges):
    best = len(vectors) + 1
    for subset_bits in range(1 << len(vectors)):
        chosen = {v for v in range(len(vectors)) if (subset_bits >> v) & 1}
        if all(left in chosen or right in chosen for left, right in edges):
            best = min(best, vector_rank([vectors[v] for v in chosen]))
    assert best <= vector_rank(vectors)
    return best


def graph_from_bits(vertex_count, bits):
    possible = tuple(combinations(range(vertex_count), 2))
    return tuple(edge for index, edge in enumerate(possible)
                 if (bits >> index) & 1)


def main():
    # Uniform matroid / ordinary Vertex Cover special case.
    identity_graphs = 0
    for vertex_count in range(2, 6):
        edge_count = vertex_count * (vertex_count - 1) // 2
        identity = tuple(1 << i for i in range(vertex_count))
        for edge_bits in range(1 << edge_count):
            edges = graph_from_bits(vertex_count, edge_bits)
            got, _, _ = rank_cover(identity, edges)
            expected = brute_rank_cover(identity, edges)
            assert got == expected, (vertex_count, edges, got, expected)
            identity_graphs += 1

    # Exhaust all binary vector representations on four vertices and every
    # simple graph on those vertices. This includes zero, duplicate, and
    # dependent control vectors.
    represented_cases = 0
    for vectors in product(range(4), repeat=4):
        edge_count = 6
        for edge_bits in range(1 << edge_count):
            edges = graph_from_bits(4, edge_bits)
            got, _, _ = rank_cover(vectors, edges)
            expected = brute_rank_cover(vectors, edges)
            assert got == expected, (vectors, edges, got, expected)
            represented_cases += 1

    rng = random.Random(20260923)
    random_cases = 0
    for _ in range(1000):
        vertex_count = rng.randint(2, 8)
        dimension = rng.randint(1, 6)
        vectors = tuple(rng.randrange(1 << dimension)
                        for _ in range(vertex_count))
        edges = tuple(edge for edge in combinations(range(vertex_count), 2)
                      if rng.random() < 0.4)
        got, _, _ = rank_cover(vectors, edges)
        expected = brute_rank_cover(vectors, edges)
        assert got == expected, (vectors, edges, got, expected)
        random_cases += 1

    print(f"identity_graphs={identity_graphs}")
    print(f"all_F2_vector_representations_on_4_vertices={represented_cases}")
    print(f"random_matroid_representations={random_cases}")
    print("rank-branch solver matched exhaustive minimum on every case")


if __name__ == "__main__":
    main()
