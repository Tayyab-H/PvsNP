"""Compare relay proof contexts with minimal high-free coordinate certificates.

For anchor a and coordinate set Q, the common matching slice contains a high
point x exactly when x agrees with a on every coordinate in Q. Thus empty
proof contexts must hit every difference support a xor x for x in U. This
script checks that necessary condition and measures how many available
minimal high-free certificates the relay program actually selects.
"""

from __future__ import annotations

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def add_minimal(bucket: set[int], candidate: int) -> bool:
    if any((old & candidate) == old for old in bucket):
        return False
    bucket.difference_update(
        old for old in tuple(bucket) if (old & candidate) == candidate
    )
    bucket.add(candidate)
    return True


def context_antichains(data: dict) -> list[set[int]]:
    n = data["N"]
    anchors = tuple(data["ANCHORS"])
    universe = frozenset(data["UNIVERSE"])
    pairs = tuple((frozenset(e), frozenset(h)) for e, h in data["ENDPOINTS"])
    meets = tuple(e & h for e, h in pairs)
    carriers = sorted(
        {frozenset()} | {x for pair in pairs for x in pair} | set(meets),
        key=lambda x: (len(x), tuple(sorted(x))),
    )
    result = []
    for anchor in anchors:
        generators = [
            frozenset(x for x in universe
                      if ((x >> bit) & 1) == ((anchor >> bit) & 1))
            for bit in range(n)
        ]
        contexts = {carrier: set() for carrier in carriers}
        for carrier in carriers:
            for bit, generator in enumerate(generators):
                if generator <= carrier:
                    contexts[carrier].add(1 << bit)
        changed = True
        while changed:
            changed = False
            for (left, right), meet in zip(pairs, meets):
                for q in tuple(contexts[left]):
                    for r in tuple(contexts[right]):
                        for carrier in carriers:
                            if meet <= carrier:
                                changed |= add_minimal(contexts[carrier], q | r)
        roots = contexts[frozenset()]
        assert roots, (anchor, "saved cover fails to derive empty")
        result.append(roots)
    return result


def minimal_high_free_sets(n: int, anchor: int, universe: tuple[int, ...]) -> set[int]:
    high_free = []
    for q in range(1 << n):
        if all(any(((point ^ anchor) >> bit) & 1 for bit in range(n)
                   if (q >> bit) & 1) for point in universe):
            high_free.append(q)
    return {
        q for q in high_free
        if not any(p != q and (p & q) == p for p in high_free)
    }


def run(script_name: str) -> None:
    data = runpy.run_path(str(ROOT / script_name), run_name="relay_data")
    n = data["N"]
    anchors = tuple(data["ANCHORS"])
    universe = tuple(data["UNIVERSE"])
    root_families = context_antichains(data)
    print(f"{script_name}: anchors={len(anchors)} rules={len(data['ENDPOINTS'])}")
    for anchor, roots in zip(anchors, root_families):
        transversals = minimal_high_free_sets(n, anchor, universe)
        assert all(
            all(any(((point ^ anchor) >> bit) & 1
                    for bit in range(n) if (q >> bit) & 1)
                for point in universe)
            for q in roots
        ), (script_name, anchor, "a root context is not high-free")
        chosen_minimal = roots & transversals
        forced = data.get("FORCED_BITS_BY_ANCHOR")
        selected_root_count = None
        if forced is not None:
            selected_mask = sum(1 << bit for bit in forced[anchor])
            selected_roots = {
                q for q in roots if (q & selected_mask) == q
            }
            assert selected_roots, (
                script_name, anchor, "restricted selector lacks a root proof"
            )
            selected_root_count = len(selected_roots)
        root_sizes = sorted({q.bit_count() for q in roots})
        transversal_sizes = sorted({q.bit_count() for q in transversals})
        print(
            f"  anchor={anchor:0{n}b}; contexts={len(roots)} sizes={root_sizes}; "
            f"minimal_high_free={len(transversals)} sizes={transversal_sizes}; "
            f"contexts_that_are_minimal_high_free={len(chosen_minimal)}"
            + (f"; roots_usable_from_selected={selected_root_count}"
               if selected_root_count is not None else "")
        )
    print("all_root_contexts_hit_every_high_point_difference=True")


def main() -> None:
    for name in (
        "experiment_basis_exception_contexts.py",
        "experiment_weight_one_anchor_cover4.py",
        "experiment_weight_one_anchor_cover5_six_rules.py",
        "experiment_sparse_ball_native_n5_witness.py",
        "experiment_sparse_ball_canonical_selector_witness.py",
    ):
        run(name)


if __name__ == "__main__":
    main()
