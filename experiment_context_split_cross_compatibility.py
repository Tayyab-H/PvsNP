"""Audit cross-anchor compatibility of first-seed context splits."""

from __future__ import annotations

import runpy
from pathlib import Path

from experiment_relay_proof_contexts import add_minimal


ROOT = Path(__file__).resolve().parent
CASES = (
    "experiment_sparse_ball_native_n5_witness.py",
    "experiment_sparse_ball_canonical_selector_witness.py",
    "experiment_sparse_ball_multiple_disjoint_witness.py",
)


def high_cylinder(anchor: int, mask: int, high: set[int], n: int) -> frozenset[int]:
    return frozenset(
        x for x in high
        if all(((x >> i) & 1) == ((anchor >> i) & 1)
               for i in range(n) if (mask >> i) & 1)
    )


def analyze(case: str) -> None:
    data = runpy.run_path(str(ROOT / case), run_name="relay_data")
    n = data["N"]
    low = set(data["ANCHORS"])
    high = set(data["UNIVERSE"])
    pairs = tuple((frozenset(e), frozenset(h)) for e, h in data["ENDPOINTS"])
    meets = tuple(e & h for e, h in pairs)
    seeds = [r for r, meet in enumerate(meets) if not meet]
    core = tuple(pair for r, pair in enumerate(pairs) if r not in seeds)
    core_meets = tuple(meets[r] for r in range(len(pairs)) if r not in seeds)
    carriers = sorted(
        {frozenset()} | {x for pair in pairs for x in pair} | set(meets),
        key=lambda x: (len(x), tuple(sorted(x))),
    )
    candidates_by_seed: dict[
        int, dict[
            tuple[frozenset[int], frozenset[int]],
            tuple[int, int, int, frozenset[int], frozenset[int]],
        ]
    ] = {
        seed: {} for seed in seeds
    }
    covered: set[int] = set()

    for anchor in sorted(low):
        generators = [
            frozenset(x for x in high
                      if ((x >> i) & 1) == ((anchor >> i) & 1))
            for i in range(n)
        ]
        contexts = {carrier: set() for carrier in carriers}
        for carrier in carriers:
            for i, generator in enumerate(generators):
                if generator <= carrier:
                    contexts[carrier].add(1 << i)
        changed = True
        while changed:
            changed = False
            for (left, right), meet in zip(core, core_meets):
                for lc in tuple(contexts[left]):
                    for rc in tuple(contexts[right]):
                        combined = lc | rc
                        for carrier in carriers:
                            if meet <= carrier:
                                changed |= add_minimal(contexts[carrier], combined)

        for seed in seeds:
            left, right = pairs[seed]
            found = False
            for lc in contexts[left]:
                for rc in contexts[right]:
                    a_side = high_cylinder(anchor, lc, high, n)
                    b_side = high_cylinder(anchor, rc, high, n)
                    assert not (a_side & b_side), (case, anchor, seed, lc, rc)
                    candidates_by_seed[seed].setdefault(
                        (a_side, b_side), (anchor, lc, rc, a_side, b_side)
                    )
                    found = True
            if found:
                covered.add(anchor)
    assert covered == low, (case, low - covered)

    total = sum(map(len, candidates_by_seed.values()))
    print(f"{case}: low={len(low)}; high={len(high)}; "
          f"seeds={seeds}; unique_context_splits={total}")
    # Within one seed, every left context is sound for E and every right
    # context is sound for H, so cross intersections must vanish. The
    # informative diagnostic is whether contexts from *different* seeds
    # cross, which is not implied by endpoint disjointness.
    for s in seeds:
        for t in seeds:
            left_by_cylinder = {
                record[3]: record for record in candidates_by_seed[s].values()
            }
            right_by_cylinder = {
                record[4]: record for record in candidates_by_seed[t].values()
            }
            left_family = tuple(left_by_cylinder.values())
            right_family = tuple(right_by_cylinder.values())
            arcs = [
                (left, right, left[3] & right[4])
                for left in left_family
                for right in right_family
                if left[3] & right[4]
            ]
            print(f"  seed {s} left vs seed {t} right: "
                  f"cylinders={len(left_family)}x{len(right_family)}; "
                  f"crossing_pairs={len(arcs)}")
            for left, right, points in arcs[:2]:
                a_anchor, a_lc, _, _, _ = left
                b_anchor, _, b_rc, _, _ = right
                print(f"    high={sorted(points)}; "
                      f"left_anchor={a_anchor:0{n}b}/" 
                      f"left_literals={[i for i in range(n) if a_lc >> i & 1]}; "
                      f"right_anchor={b_anchor:0{n}b}/" 
                      f"right_literals={[i for i in range(n) if b_rc >> i & 1]}")
            if len(arcs) > 2:
                print(f"    ... {len(arcs) - 2} further unique context pairs")


def main() -> None:
    for case in CASES:
        analyze(case)


if __name__ == "__main__":
    main()
