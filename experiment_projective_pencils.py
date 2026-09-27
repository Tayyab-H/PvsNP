"""Exact fusion-cover search for point-pencil filters in small projective planes."""

from __future__ import annotations

from itertools import product


def normalize(vector: tuple[int, int, int], q: int) -> tuple[int, int, int] | None:
    for value in vector:
        if value % q:
            inverse = pow(value % q, -1, q)
            return tuple((x * inverse) % q for x in vector)
    return None


def projective_points(q: int) -> list[tuple[int, int, int]]:
    return sorted({
        normalize(v, q)
        for v in product(range(q), repeat=3)
        if any(v)
    })


def exact_cover_number(cover_masks: set[int], m: int) -> int:
    target = (1 << m) - 1
    dp = [m + 1] * (target + 1)
    dp[0] = 0
    for mask in range(target + 1):
        if dp[mask] == m + 1:
            continue
        for cover in cover_masks:
            new_mask = mask | cover
            if dp[new_mask] > dp[mask] + 1:
                dp[new_mask] = dp[mask] + 1
    return dp[target]


def analyze(q: int) -> None:
    points = projective_points(q)
    lines = projective_points(q)  # dual coefficient vectors
    p_index = {point: i for i, point in enumerate(points)}
    v = len(points)
    line_masks = []
    pencils: list[list[int]] = [[] for _ in points]
    for line_index, normal in enumerate(lines):
        mask = 0
        for point_index, point in enumerate(points):
            if sum(a * b for a, b in zip(normal, point)) % q == 0:
                mask |= 1 << point_index
                pencils[point_index].append(line_index)
        line_masks.append(mask)

    # Each endpoint's membership mask records which point-pencils it accepts.
    universe_count = 1 << v
    accepted = [0] * universe_count
    for subset in range(universe_count):
        for point_index, incident_lines in enumerate(pencils):
            if any((subset & line_masks[line]) == line_masks[line] for line in incident_lines):
                accepted[subset] |= 1 << point_index

    target = (1 << v) - 1
    pair_masks: set[int] = set()
    max_pair_coverage = 0
    witness_pair = None
    for left in range(universe_count):
        left_accepted = accepted[left]
        for right in range(universe_count):
            covered = left_accepted & accepted[right] & ~accepted[left & right] & target
            if covered:
                pair_masks.add(covered)
                size = covered.bit_count()
                if size > max_pair_coverage:
                    max_pair_coverage = size
                    witness_pair = (left, right, covered)

    # Geometry sanity checks: every pair of points lies on exactly one line;
    # every pencil has q+1 distinct line generators.
    assert all(len(pencil) == q + 1 for pencil in pencils)
    assert all(mask.bit_count() == q + 1 for mask in line_masks)
    anchor_compatible_colorings = []
    for coloring in range(1 << v):
        valid = True
        for point_index, incident_lines in enumerate(pencils):
            anchor_bit = (coloring >> point_index) & 1
            if not any(
                all(((coloring >> x) & 1) == anchor_bit
                    for x in range(v) if (line_masks[line] >> x) & 1)
                for line in incident_lines
            ):
                valid = False
                break
        if valid:
            anchor_compatible_colorings.append(coloring)
    print(
        f"PG(2,{q}); points={v}; lines={len(lines)}; "
        f"generators_per_filter={q+1}; endpoint_sets={universe_count}; "
        f"distinct_pair_cover_masks={len(pair_masks)}; "
        f"max_pair_coverage={max_pair_coverage}; "
        f"exact_cover_number={exact_cover_number(pair_masks, v)}; "
        f"literal_coordinate_colorings={len(anchor_compatible_colorings)}; "
        f"distinct_anchor_codes_possible={len(set(tuple((coloring >> p) & 1 for coloring in anchor_compatible_colorings) for p in range(v)))}"
    )
    if witness_pair:
        left, right, covered = witness_pair
        print(
            f"max_pair left_size={left.bit_count()}; right_size={right.bit_count()}; "
            f"intersection_size={(left & right).bit_count()}; "
            f"covered_points={[i for i in range(v) if (covered >> i) & 1]}"
        )


def main() -> None:
    analyze(2)
    analyze(3)


if __name__ == "__main__":
    main()
