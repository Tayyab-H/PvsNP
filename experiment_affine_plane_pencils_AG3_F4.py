"""Verify the three-pair coordinate-blocker cover for affine plane pencils in AG(3,4)."""

from __future__ import annotations

from itertools import product


def gf4_mul(x: int, y: int) -> int:
    a0, a1 = x & 1, (x >> 1) & 1
    b0, b1 = y & 1, (y >> 1) & 1
    c0 = (a0 & b0) ^ (a1 & b1)
    c1 = (a0 & b1) ^ (a1 & b0) ^ (a1 & b1)
    return c0 | (c1 << 1)


def dot(x: tuple[int, int, int], y: tuple[int, int, int]) -> int:
    value = 0
    for a, b in zip(x, y):
        value ^= gf4_mul(a, b)
    return value


def normals() -> list[tuple[int, int, int]]:
    result = set()
    inverses = {1: 1, 2: 3, 3: 2}
    for vector in product(range(4), repeat=3):
        if vector == (0, 0, 0):
            continue
        first = next(x for x in vector if x)
        result.add(tuple(gf4_mul(x, inverses[first]) for x in vector))
    return sorted(result)


def projection(word: int) -> tuple[int, int, int]:
    return word & 3, (word >> 2) & 3, (word >> 4) & 3


def main() -> None:
    q = 4
    points = list(product(range(q), repeat=3))
    anchor_words = {x | (y << 2) | (z << 4) for x, y, z in points}
    universe = [word for word in range(1 << 8) if word not in anchor_words]
    point_masks = {
        p: sum(1 << i for i, word in enumerate(universe) if projection(word) == p)
        for p in points
    }
    normal_list = normals()
    assert len(normal_list) == 21

    plane_masks: dict[tuple[int, int, int], list[int]] = {}
    literal_masks: dict[tuple[int, int, int], list[int]] = {}
    for p in points:
        planes = []
        for normal in normal_list:
            value = dot(normal, p)
            planes.append(sum(
                point_masks[x]
                for x in points
                if dot(normal, x) == value
            ))
        assert all(planes)
        plane_masks[p] = planes

        word = p[0] | (p[1] << 2) | (p[2] << 4)
        literals = [
            sum(1 << i for i, table in enumerate(universe)
                if ((table >> bit) & 1) == ((word >> bit) & 1))
            for bit in range(8)
        ]
        assert all(literals)
        literal_masks[p] = literals

    covered: set[tuple[int, int, int]] = set()
    checked = 0
    for t in range(3):  # d-r+2 = 3 for d=3, r=2
        left = sum(point_masks[p] for p in points if p[0] != t)
        right = sum(point_masks[p] for p in points if p[1] != t)
        common = left & right
        count = 0
        for p in points:
            if p[0] == t or p[1] == t:
                continue
            x0_plane = next(mask for normal, mask in zip(normal_list, plane_masks[p])
                            if normal == (1, 0, 0))
            x1_plane = next(mask for normal, mask in zip(normal_list, plane_masks[p])
                            if normal == (0, 1, 0))
            assert x0_plane & left == x0_plane
            assert x1_plane & right == x1_plane
            for generator in plane_masks[p] + literal_masks[p]:
                assert generator & common != generator
                checked += 1
            covered.add(p)
            count += 1
        print(f"t={t}: covered_anchors={count}")

    assert covered == set(points)
    print(
        f"AG(3,4), affine_plane_pencils; |U|={len(universe)}; anchors={len(points)}; "
        f"planes_per_anchor={len(normal_list)}; blocker_pairs=3; "
        f"generator_rejections_checked={checked}; PASS"
    )


if __name__ == "__main__":
    main()
