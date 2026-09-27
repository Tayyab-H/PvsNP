"""Exact small checks for fusion covers by q-ary coordinate-slice filters.

For a full product universe [q]^n, each anchor a is accepted by an endpoint
when the endpoint contains a whole coordinate slice x_i=a_i. The script
exhaustively computes the exact fusion cover for q=2,3 and n=2, then checks
the four-rectangle construction on a larger q=3,n=3 product.
"""

from __future__ import annotations

from collections import deque
from itertools import product


def exact_small(q: int, n: int) -> tuple[int, int, int, list[int]]:
    points = list(product(range(q), repeat=n))
    anchors = points
    m = len(anchors)
    target = (1 << m) - 1
    count = 1 << len(points)

    # For each endpoint, record the anchors for which it contains at least
    # one matching coordinate slice.
    signatures = [0] * count
    slices: list[list[int]] = []
    for a in anchors:
        a_slices = []
        for i in range(n):
            mask = 0
            for j, x in enumerate(points):
                if x[i] == a[i]:
                    mask |= 1 << j
            a_slices.append(mask)
        slices.append(a_slices)
    for endpoint in range(count):
        for ai, a_slices in enumerate(slices):
            if any(endpoint & sl == sl for sl in a_slices):
                signatures[endpoint] |= 1 << ai

    profiles = set()
    profile_witness = {}
    for left in range(count):
        for right in range(count):
            profile = signatures[left] & signatures[right] & ~signatures[left & right]
            if profile:
                profiles.add(profile)
                profile_witness.setdefault(profile, (left, right))

    # Shortest path over profile unions gives the exact set-cover number.
    distance = {0: 0}
    queue = deque([0])
    while queue:
        covered = queue.popleft()
        if covered == target:
            break
        for profile in profiles:
            new = covered | profile
            if new not in distance:
                distance[new] = distance[covered] + 1
                queue.append(new)
    cover = distance.get(target, -1)
    pair = []
    if cover == 2:
        for first in profiles:
            second = next((p for p in profiles if first | p == target), None)
            if second is not None:
                pair = [first, second]
                break
    if pair:
        point_names = list(product(range(q), repeat=n))
        for p in pair:
            left, right = profile_witness[p]
            print(f"  witness_profile={[anchors[i] for i in range(m) if p >> i & 1]}; E={[point_names[i] for i in range(len(point_names)) if left >> i & 1]}; H={[point_names[i] for i in range(len(point_names)) if right >> i & 1]}")
    return len(profiles), max(p.bit_count() for p in profiles), cover, pair


def verify_checkerboard_two_cover(q: int, n: int) -> list[int]:
    points = list(product(range(q), repeat=n))
    anchors = points
    split = q // 2
    r, rbar = set(range(split)), set(range(split, q))
    c, cbar = set(range(split)), set(range(split, q))

    def endpoint_signature(endpoint: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
        accepted = set()
        for a in anchors:
            if any({x for x in points if x[i] == a[i]} <= endpoint for i in range(n)):
                accepted.add(a)
        return accepted

    e1 = {x for x in points if x[0] in r or x[1] in c}
    h1 = {x for x in points if x[0] in rbar or x[1] in cbar}
    e2 = {x for x in points if x[0] in r or x[1] in cbar}
    h2 = {x for x in points if x[0] in rbar or x[1] in c}
    p1 = (endpoint_signature(e1) & endpoint_signature(h1)) - endpoint_signature(e1 & h1)
    p2 = (endpoint_signature(e2) & endpoint_signature(h2)) - endpoint_signature(e2 & h2)
    assert not p1 & p2
    covered = p1 | p2
    assert covered == set(anchors)
    return [len(p1), len(p2)]


def main() -> None:
    for q in (2, 3):
        profiles, max_profile, cover, _ = exact_small(q, 2)
        sizes = verify_checkerboard_two_cover(q, 3)
        print(f"q={q}; n=2; exact_profiles={profiles}; max_profile={max_profile}; exact_cover={cover}; n3_two_profile_sizes={sizes}")


if __name__ == "__main__":
    main()
