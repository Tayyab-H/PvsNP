"""Exact cover search for affine point-pencil filters with literal anchors."""

from __future__ import annotations

from itertools import product


def normalized_directions(q: int) -> list[tuple[int, int]]:
    directions = set()
    for a, b in product(range(q), repeat=2):
        if a == b == 0:
            continue
        if a:
            inv = pow(a, -1, q)
        else:
            inv = pow(b, -1, q)
        directions.add(((a * inv) % q, (b * inv) % q))
    return sorted(directions)


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


def analyze(q: int, anchor_count: int) -> None:
    points = [(x, y) for x in range(q) for y in range(q)]
    anchors = [(x, x * x % q) for x in range(anchor_count)]
    assert len(set(anchors)) == anchor_count
    universe = [p for p in points if p not in set(anchors)]
    point_index = {p: i for i, p in enumerate(universe)}
    directions = normalized_directions(q)
    filters: list[list[int]] = []

    for anchor in anchors:
        line_masks = []
        for a, b in directions:
            value = (a * anchor[0] + b * anchor[1]) % q
            mask = 0
            for point, index in point_index.items():
                if (a * point[0] + b * point[1]) % q == value:
                    mask |= 1 << index
            assert mask
            line_masks.append(mask)
        filters.append(line_masks)

    # Verify that every Boolean one-hot literal on every affine form/value
    # contains a line generator for each anchor.
    literal_checks = 0
    for anchor, line_masks in zip(anchors, filters):
        for a, b in directions:
            anchor_value = (a * anchor[0] + b * anchor[1]) % q
            for value in range(q):
                matching_side = 0
                for index, point in enumerate(universe):
                    bit = int((a * point[0] + b * point[1]) % q == value)
                    anchor_bit = int(anchor_value == value)
                    if bit == anchor_bit:
                        matching_side |= 1 << index
                assert any((line & matching_side) == line for line in line_masks)
                literal_checks += 1

    # Cache endpoint acceptance masks; many witness orientations give the same set.
    accepted_cache: dict[int, int] = {}

    def accepted_by(mask: int) -> int:
        cached = accepted_cache.get(mask)
        if cached is not None:
            return cached
        result = 0
        for anchor_index, lines in enumerate(filters):
            if any((line & mask) == line for line in lines):
                result |= 1 << anchor_index
        accepted_cache[mask] = result
        return result

    # Exact search by the ordered generator pair used by each covered filter.
    # There are 1 + k(k-1) states per filter: unused, or distinct generators
    # assigned to left and right. Shrinking arbitrary endpoints to those unions
    # preserves rejection, so this computes the unrestricted optimum.
    m = len(filters)
    state_lists = [[None] + [(i, j) for i in range(len(lines))
                             for j in range(len(lines)) if i != j]
                   for lines in filters]
    cover_masks: set[int] = set()
    max_coverage = 0
    full_pair = None
    assignment_count = 1
    for states in state_lists:
        assignment_count *= len(states)

    assignments_examined = 0
    for assignment in product(*state_lists):
        assignments_examined += 1
        left = right = 0
        for anchor_index, state in enumerate(assignment):
            if state is None:
                continue
            left_line, right_line = state
            left |= filters[anchor_index][left_line]
            right |= filters[anchor_index][right_line]
        intersection = left & right
        covered = accepted_by(left) & accepted_by(right) & ~accepted_by(intersection) & ((1 << m) - 1)
        if covered:
            cover_masks.add(covered)
            max_coverage = max(max_coverage, covered.bit_count())
            if covered == (1 << m) - 1 and full_pair is None:
                full_pair = (left, right, intersection, assignment)
                break

    print(
        f"AG(2,{q}); anchors={anchor_count}; |U|={len(universe)}; "
        f"minimal_lines_per_filter={q+1}; anchor_literal_checks={literal_checks}; "
        f"orientation_assignments={assignment_count}; "
        f"assignments_examined={assignments_examined}; "
        f"distinct_pair_cover_masks={len(cover_masks)}; "
        f"max_pair_coverage={max_coverage}; "
        f"exact_cover_number={exact_cover_number(cover_masks,m)}"
    )
    if full_pair is not None:
        left, right, intersection, assignment = full_pair
        decode = lambda mask: [point for index, point in enumerate(universe) if (mask >> index) & 1]
        print("full_pair_left=" + repr(decode(left)))
        print("full_pair_right=" + repr(decode(right)))
        print("full_pair_intersection=" + repr(decode(intersection)))
        print("chosen_line_indices=" + repr(assignment))


def main() -> None:
    analyze(q=3, anchor_count=3)
    analyze(q=5, anchor_count=4)
    analyze(q=5, anchor_count=5)


if __name__ == "__main__":
    main()
