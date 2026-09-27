"""Exhaustively check the cut-cover / graph-coloring identity for shared-core filters."""

from __future__ import annotations

from itertools import combinations


def chromatic_number(n: int, edges: list[tuple[int, int]]) -> int:
    adjacency = [0] * n
    for u, v in edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    for colors in range(1, n + 1):
        assignment = [-1] * n

        def place(vertex: int) -> bool:
            if vertex == n:
                return True
            forbidden = {
                assignment[w]
                for w in range(n)
                if ((adjacency[vertex] >> w) & 1) and assignment[w] >= 0
            }
            for color in range(colors):
                if color in forbidden:
                    continue
                assignment[vertex] = color
                if place(vertex + 1):
                    return True
                assignment[vertex] = -1
            return False

        if place(0):
            return colors
    raise AssertionError("n colors always suffice")


def minimum_cut_cover(edge_count: int, cut_masks: list[int]) -> int:
    target = (1 << edge_count) - 1
    best = [edge_count + 1] * (1 << edge_count)
    best[0] = 0
    for covered in range(1 << edge_count):
        if best[covered] > edge_count:
            continue
        for cut in cut_masks:
            nxt = covered | cut
            if best[nxt] > best[covered] + 1:
                best[nxt] = best[covered] + 1
    return best[target]


def main() -> None:
    checked = 0
    for n in range(2, 6):
        possible_edges = list(combinations(range(n), 2))
        graphs = 1 << len(possible_edges)
        for graph_mask in range(graphs):
            edges = [
                edge for index, edge in enumerate(possible_edges)
                if (graph_mask >> index) & 1
            ]
            if not edges:
                continue
            cuts = []
            for side in range(1 << n):
                mask = 0
                for index, (u, v) in enumerate(edges):
                    if ((side >> u) ^ (side >> v)) & 1:
                        mask |= 1 << index
                cuts.append(mask)
            cover = minimum_cut_cover(len(edges), cuts)
            chi = chromatic_number(n, edges)
            predicted = (chi - 1).bit_length()
            assert cover == predicted, (n, edges, cover, chi)
            checked += 1
    print(f"shared-core graph instances checked={checked}; exact cut-cover=ceil(log2 chi); PASS")


if __name__ == "__main__":
    main()
