"""Check the affine-grid collapse with all literal generators present."""

from __future__ import annotations

from itertools import product


def gf4_mul(x: int, y: int) -> int:
    """Multiply in GF(4)=GF(2)[t]/(t^2+t+1), using two-bit labels."""
    a0, a1 = x & 1, (x >> 1) & 1
    b0, b1 = y & 1, (y >> 1) & 1
    c0 = (a0 & b0) ^ (a1 & b1)  # t^2 = t + 1
    c1 = (a0 & b1) ^ (a1 & b0) ^ (a1 & b1)
    return c0 | (c1 << 1)


def projection(word: int) -> tuple[int, int]:
    return word & 3, (word >> 2) & 3


def line_holds(point: tuple[int, int], anchor: tuple[int, int], direction: int) -> bool:
    x, y = point
    ax, ay = anchor
    if direction == 0:  # vertical line x=ax
        return x == ax
    slope = direction - 1  # remaining directions have slopes 0,1,2,3
    return y ^ gf4_mul(slope, x) == ay ^ gf4_mul(slope, ax)


def main() -> None:
    q = 4
    x_levels = {1, 2}
    y_levels = {1, 2}
    anchors = [(x, y) for x, y in product(sorted(x_levels), sorted(y_levels))]
    anchor_words = {(x | (y << 2)) for x, y in anchors}
    universe_words = [word for word in range(1 << 8) if word not in anchor_words]
    point_masks = {
        point: sum(1 << i for i, word in enumerate(universe_words)
                   if projection(word) == point)
        for point in product(range(q), repeat=2)
    }
    full_mask = (1 << len(universe_words)) - 1

    left = sum(point_masks[(x, y)] for x in x_levels for y in range(q))
    right = sum(point_masks[(x, y)] for x in range(q) for y in y_levels)
    intersection = left & right
    assert intersection

    line_generator_count = 0
    literal_generator_count = 0
    for anchor in anchors:
        line_masks = [
            sum(1 << i for i, word in enumerate(universe_words)
                if line_holds(projection(word), anchor, direction))
            for direction in range(q + 1)
        ]
        assert all(mask for mask in line_masks)
        line_generator_count += len(line_masks)

        # E and H contain the vertical and horizontal generators at anchor.
        assert (line_masks[0] & left) == line_masks[0]
        assert (line_masks[1] & right) == line_masks[1]
        assert all((mask & intersection) != mask for mask in line_masks)

        anchor_word = anchor[0] | (anchor[1] << 2)
        for coordinate in range(8):
            anchor_bit = (anchor_word >> coordinate) & 1
            literal = sum(1 << i for i, word in enumerate(universe_words)
                          if ((word >> coordinate) & 1) == anchor_bit)
            assert literal
            literal_generator_count += 1
            assert (literal & intersection) != literal

    assert left and right
    print(
        f"AG(2,4); |U|={len(universe_words)}; anchors={len(anchors)}; "
        f"line_generators={line_generator_count}; "
        f"literal_generators={literal_generator_count}; "
        f"left_size={left.bit_count()}; right_size={right.bit_count()}; "
        f"intersection_size={intersection.bit_count()}; PASS"
    )

    # A stronger three-pair check for every projected anchor in AG(2,4).
    all_anchors = list(product(range(q), repeat=2))
    all_anchor_words = {x | (y << 2) for x, y in all_anchors}
    all_universe_words = [word for word in range(1 << 8) if word not in all_anchor_words]
    all_point_masks = {
        point: sum(1 << i for i, word in enumerate(all_universe_words)
                   if projection(word) == point)
        for point in product(range(q), repeat=2)
    }
    all_mask = (1 << len(all_universe_words)) - 1
    blockers = [(0, 0), (1, 1), (2, 2)]
    covered_anchors: set[tuple[int, int]] = set()
    checked_line_generators = 0
    checked_literal_generators = 0

    for ax, by in blockers:
        vertical_removed = sum(all_point_masks[(ax, y)] for y in range(q))
        horizontal_removed = sum(all_point_masks[(x, by)] for x in range(q))
        endpoint_left = all_mask ^ vertical_removed
        endpoint_right = all_mask ^ horizontal_removed
        common = endpoint_left & endpoint_right

        for anchor in all_anchors:
            x, y = anchor
            if x == ax or y == by:
                continue
            line_masks = [
                sum(1 << i for i, word in enumerate(all_universe_words)
                    if line_holds(projection(word), anchor, direction))
                for direction in range(q + 1)
            ]
            assert all(line_masks)
            assert (line_masks[0] & endpoint_left) == line_masks[0]
            assert (line_masks[1] & endpoint_right) == line_masks[1]
            assert all((line & common) != line for line in line_masks)
            checked_line_generators += len(line_masks)

            anchor_word = x | (y << 2)
            for coordinate in range(8):
                anchor_bit = (anchor_word >> coordinate) & 1
                literal = sum(
                    1 << i for i, word in enumerate(all_universe_words)
                    if ((word >> coordinate) & 1) == anchor_bit
                )
                assert literal and (literal & common) != literal
                checked_literal_generators += 1
            covered_anchors.add(anchor)

    assert covered_anchors == set(all_anchors)
    print(
        f"three_pair_all_anchor_check=AG(2,4); anchors={len(all_anchors)}; "
        f"blocker_pairs={len(blockers)}; checked_line_generators={checked_line_generators}; "
        f"checked_literal_generators={checked_literal_generators}; PASS"
    )


if __name__ == "__main__":
    main()
