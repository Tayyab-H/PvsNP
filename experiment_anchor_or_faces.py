"""Extract minimum-union OR faces from the anchored literal-cylinder toy."""

from __future__ import annotations

from itertools import combinations

import experiment_coordinate_certificate_toy as toy


def minimal_members(family: int) -> list[int]:
    accepted = [w for w in range(toy.SET_COUNT) if (family >> w) & 1]
    return [
        w for w in accepted
        if not any(v != w and (v & w) == v for v in accepted)
    ]


def or_faces(minima: list[int], family: int, minimum_union_only: bool):
    pairs = list(combinations(minima, 2))
    best_union_size = min((a | b).bit_count() for a, b in pairs)
    faces = set()
    for a, b in pairs:
        if minimum_union_only and (a | b).bit_count() != best_union_size:
            continue
        for i in range(len(toy.U_WORDS)):
            if not ((a >> i) & 1) or ((b >> i) & 1):
                continue
            for j in range(len(toy.U_WORDS)):
                if not ((b >> j) & 1) or ((a >> j) & 1):
                    continue
                base = (a | b) & ~(1 << i) & ~(1 << j)
                if not ((family >> base) & 1):
                    faces.add((base, i, j))
    return faces


def covers(family: int, left: int, right: int) -> bool:
    intersection = left & right
    return bool((family >> left) & 1) and bool((family >> right) & 1) and not bool(
        (family >> intersection) & 1
    )


def main() -> None:
    for r in (1, 2):
        filters = toy.anchored_filters(r)
        co_singleton_memberships = sum(
            bool((family >> (toy.FULL_U ^ (1 << i))) & 1)
            for family in filters
            for i in range(len(toy.U_WORDS))
        )
        minima = [minimal_members(f) for f in filters]
        min_faces = [or_faces(m, f, True) for m, f in zip(minima, filters)]
        all_faces = [or_faces(m, f, False) for m, f in zip(minima, filters)]

        def loads(per_anchor):
            result: dict[tuple[int, int, int], int] = {}
            for faces in per_anchor:
                for face in faces:
                    result[face] = result.get(face, 0) + 1
            return result

        min_face_load = loads(min_faces)
        all_face_load = loads(all_faces)

        # Measure maximum coverage among canonical OR-face endpoint pairs.
        face_pair_coverage = []
        for base, i, j in all_face_load:
            left, right = base | (1 << i), base | (1 << j)
            face_pair_coverage.append(sum(covers(f, left, right) for f in filters))
        max_face_coverage = max(face_pair_coverage, default=0)

        # Compare with the best completely unrestricted pair on this tiny toy.
        best_pair = None
        max_arbitrary_coverage = -1
        for left in range(toy.SET_COUNT):
            for right in range(toy.SET_COUNT):
                coverage = sum(covers(f, left, right) for f in filters)
                if coverage > max_arbitrary_coverage:
                    max_arbitrary_coverage = coverage
                    best_pair = (left, right)
        left, right = best_pair
        compatible_face_counts = []
        for faces in all_faces:
            compatible = 0
            for base, i, j in faces:
                x, y = base | (1 << i), base | (1 << j)
                if (x & left) == x and (y & right) == y:
                    compatible += 1
                elif (x & right) == x and (y & left) == y:
                    compatible += 1
            compatible_face_counts.append(compatible)
        print(
            f"r={r}; anchors={len(filters)}; min_union_faces={len(min_face_load)}; "
            f"all_witness_OR_faces={len(all_face_load)}; "
            f"largest_face_load={max(all_face_load.values())}; "
            f"best_OR_face_pair_coverage={max_face_coverage}/{len(filters)}; "
            f"best_arbitrary_pair_coverage={max_arbitrary_coverage}/{len(filters)}; "
            f"best_pair=({left:#x},{right:#x}); "
            f"covered_filters_with_compatible_OR_face="
            f"{sum(c > 0 for c in compatible_face_counts)}/{len(filters)}; "
            f"co_singletons_already_accepted="
            f"{co_singleton_memberships}/{len(filters) * len(toy.U_WORDS)}"
        )
        assert all(min_faces)
        assert all(all_faces)
        assert max_face_coverage <= max_arbitrary_coverage


if __name__ == "__main__":
    main()
