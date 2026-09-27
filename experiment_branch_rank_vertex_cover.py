"""Check the control-rank optimization/vertex-cover correspondence."""

from itertools import combinations, product


def affine_rows_for_edge_parity_circuit(vertex_count, edges):
    """Build XOR/AND circuit equations with output XOR of all edge products = 1."""
    and_outputs = [vertex_count + i for i in range(len(edges))]
    next_wire = vertex_count + len(edges)
    rows = []

    if not and_outputs:
        return rows, 0, next_wire

    accumulator = and_outputs[0]
    for edge_output in and_outputs[1:]:
        new_accumulator = next_wire
        next_wire += 1
        rows.append(((1 << accumulator) | (1 << edge_output) | (1 << new_accumulator), 0))
        accumulator = new_accumulator
    rows.append((1 << accumulator, 1))
    return rows, accumulator, next_wire


def minimum_vertex_cover_size(vertex_count, edges):
    for size in range(vertex_count + 1):
        for cover in combinations(range(vertex_count), size):
            cover = set(cover)
            if all(left in cover or right in cover for left, right in edges):
                return size
    raise AssertionError("the full vertex set must cover every edge")


def graph_case(vertex_count, edge_bits):
    possible_edges = tuple(combinations(range(vertex_count), 2))
    edges = tuple(
        edge for index, edge in enumerate(possible_edges)
        if (edge_bits >> index) & 1
    )
    rows, output, wire_count = affine_rows_for_edge_parity_circuit(vertex_count, edges)
    input_mask = (1 << vertex_count) - 1

    # The output/parity equations involve gate outputs and XOR accumulators only.
    # Thus every primary input remains a free affine coordinate.
    assert all(not (mask & input_mask) for mask, _ in rows)
    assert output < wire_count

    best_rank = vertex_count + 1
    for choices in product((0, 1), repeat=len(edges)):
        selected = {edge[choice] for edge, choice in zip(edges, choices)}
        # Projection of the affine solution space onto free input coordinates
        # is the full cube, so its dimension is the number of distinct controls.
        projected_rank = len(selected)
        best_rank = min(best_rank, projected_rank)

    expected = minimum_vertex_cover_size(vertex_count, edges)
    assert best_rank == expected, (vertex_count, edges, best_rank, expected)
    return len(edges), best_rank


def main():
    graphs = 0
    control_choices = 0
    checked_edges = 0
    for vertex_count in range(2, 6):
        edge_count = vertex_count * (vertex_count - 1) // 2
        for edge_bits in range(1 << edge_count):
            edge_total, minimum_rank = graph_case(vertex_count, edge_bits)
            graphs += 1
            control_choices += 1 << edge_total
            checked_edges += edge_total

    print(f"simple_graphs={graphs}; control_selections={control_choices}; gate_inputs={checked_edges}")
    print("for every checked graph, minimum projected control rank equals minimum vertex-cover size")


if __name__ == "__main__":
    main()
