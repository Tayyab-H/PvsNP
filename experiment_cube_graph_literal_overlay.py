"""Exact fusion covers for graph-edge filters with/without cube literals."""

from __future__ import annotations

from collections import deque


N = 3
POINTS = list(range(1 << N))
ANCHORS = POINTS[:]
ENDPOINTS = 1 << len(POINTS)
TARGET = (1 << len(ANCHORS)) - 1


def generators(anchor: int, mode: str) -> list[int]:
    out = []
    if mode in {"literals", "combined"}:
        for bit in range(N):
            out.append(sum(1 << x for x in POINTS if ((x >> bit) & 1) == ((anchor >> bit) & 1)))
    if mode in {"edges", "combined"}:
        for other in POINTS:
            if (anchor ^ other).bit_count() == 1:
                out.append((1 << anchor) | (1 << other))
    return out


def exact(mode: str) -> tuple[int, int, tuple[int, int] | None]:
    sig = [0] * ENDPOINTS
    for e in range(ENDPOINTS):
        for a in ANCHORS:
            if any(e & g == g for g in generators(a, mode)):
                sig[e] |= 1 << a
    profiles = set()
    witness = {}
    for e in range(ENDPOINTS):
        for h in range(ENDPOINTS):
            p = sig[e] & sig[h] & ~sig[e & h]
            if p:
                profiles.add(p)
                witness.setdefault(p, (e, h))
    distance = {0: 0}
    queue = deque([0])
    while queue:
        covered = queue.popleft()
        if covered == TARGET:
            break
        for p in profiles:
            nxt = covered | p
            if nxt not in distance:
                distance[nxt] = distance[covered] + 1
                queue.append(nxt)
    cover = distance.get(TARGET, -1)
    pair = None
    if cover == 1:
        p = next(p for p in profiles if p == TARGET)
        pair = witness[p]
    elif cover == 2:
        for p in profiles:
            q = next((q for q in profiles if p | q == TARGET), None)
            if q is not None:
                pair = (witness[p], witness[q])  # type: ignore[assignment]
                break
    return len(profiles), cover, pair


def show_endpoint(mask: int) -> list[int]:
    return [x for x in POINTS if mask >> x & 1]


def main() -> None:
    for mode in ("literals", "edges", "combined"):
        profile_count, cover, witness = exact(mode)
        print(f"mode={mode}; anchors={len(ANCHORS)}; universe={len(POINTS)}; profiles={profile_count}; exact_cover={cover}")
        if witness is not None:
            if cover == 1:
                print(f"  E={show_endpoint(witness[0])}; H={show_endpoint(witness[1])}")
            else:
                for e, h in witness:
                    print(f"  E={show_endpoint(e)}; H={show_endpoint(h)}")


if __name__ == "__main__":
    main()
