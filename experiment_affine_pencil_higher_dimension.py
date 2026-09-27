"""Verify the coordinate-blocker cover for affine line pencils in AG(3,4)."""

from __future__ import annotations

from itertools import product


def gf4_mul(x: int, y: int) -> int:
    a0, a1 = x & 1, (x >> 1) & 1
    b0, b1 = y & 1, (y >> 1) & 1
    c0 = (a0 & b0) ^ (a1 & b1)
    c1 = (a0 & b1) ^ (a1 & b0) ^ (a1 & b1)
    return c0 | (c1 << 1)


def directions() -> list[tuple[int, int, int]]:
    """Represent each one-dimensional subspace by first-nonzero entry 1."""
    result: set[tuple[int, int, int]] = set()
    for vector in product(range(4), repeat=3):
        if vector == (0, 0, 0):
            continue
        first = next(value for value in vector if value)
        inverse = {1: 1, 2: 3, 3: 2}[first]
        result.add(tuple(gf4_mul(value, inverse) for value in vector))
    return sorted(result)


def projection(word: int) -> tuple[int, int, int]:
    return word & 3, (word >> 2) & 3, (word >> 4) & 3


def main() -> None:
    q = 4
    all_points = list(product(range(q), repeat=3))
    anchors = all_points
    anchor_words = {x | (y << 2) | (z << 4) for x, y, z in anchors}
    universe = [word for word in range(1 << 8) if word not in anchor_words]
    point_words = {
        p: sum(1 << i for i, word in enumerate(universe) if projection(word) == p)
        for p in all_points
    }

    direction_list = directions()
    line_masks: dict[tuple[int, int, int], list[int]] = {}
    literal_masks: dict[tuple[int, int, int], list[int]] = {}
    for p in anchors:
        masks = []
        for v in direction_list:
            line_points = {
                tuple(x ^ gf4_mul(s, coordinate) for x, coordinate in zip(p, v))
                for s in range(q)
            }
            mask = sum(point_words[x] for x in line_points)
            assert mask
            masks.append(mask)
        assert len(masks) == 21
        line_masks[p] = masks

        anchor_word = p[0] | (p[1] << 2) | (p[2] << 4)
        literals = [
            sum(1 << i for i, word in enumerate(universe)
                if ((word >> bit) & 1) == ((anchor_word >> bit) & 1))
            for bit in range(8)
        ]
        assert all(literals)
        literal_masks[p] = literals

    covered: set[tuple[int, int, int]] = set()
    checked = 0
    for t in range(q):
        left = sum(point_words[p] for p in all_points if p[0] != t and p[1] != t)
        right = sum(point_words[p] for p in all_points if p[2] != t)
        common = left & right
        covered_count = 0
        for p in anchors:
            if t in p:
                continue
            e3 = next(mask for v, mask in zip(direction_list, line_masks[p])
                      if v == (0, 0, 1))
            e1 = next(mask for v, mask in zip(direction_list, line_masks[p])
                      if v == (1, 0, 0))
            assert e3 & left == e3
            assert e1 & right == e1
            for generator in line_masks[p] + literal_masks[p]:
                assert generator & common != generator
                checked += 1
            covered.add(p)
            covered_count += 1
        print(f"t={t}: covered_anchors={covered_count}")

    assert covered == set(anchors)
    print(
        f"AG(3,4); |U|={len(universe)}; anchors={len(anchors)}; "
        f"directions_per_anchor={len(direction_list)}; blocker_pairs={q}; "
        f"generator_rejections_checked={checked}; PASS"
    )


if __name__ == "__main__":
    main()
