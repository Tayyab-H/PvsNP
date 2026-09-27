"""Trace anchor-dependent minimal leaf contexts through saved relay covers.

This explores a refinement of raw rule fanout. A context is the set of
coordinate literals used as leaves in a derivation of a carrier. For each
carrier and anchor, the script keeps the inclusion-minimal contexts generated
by the exact preservation recurrence. It analyzes the saved n=4 and n=5
weight-one toy covers; this is finite diagnostic evidence only.
"""

from __future__ import annotations

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def add_minimal(bucket: set[int], candidate: int) -> bool:
    """Insert a bitmask unless a subset already proves the same carrier."""
    if any((old & candidate) == old for old in bucket):
        return False
    dominated = {old for old in bucket if (old & candidate) == candidate}
    bucket.difference_update(dominated)
    bucket.add(candidate)
    return True


def direct_carrier_closure(
    generators: list[frozenset[int]],
    endpoint_pairs: tuple[tuple[frozenset[int], frozenset[int]], ...],
    carriers: list[frozenset[int]],
    selected_bits: int,
) -> set[frozenset[int]]:
    closure = {
        carrier for carrier in carriers
        if any((selected_bits & (1 << bit)) and generator <= carrier
               for bit, generator in enumerate(generators))
    }
    changed = True
    while changed:
        changed = False
        for left, right in endpoint_pairs:
            if left in closure and right in closure:
                meet = left & right
                for carrier in carriers:
                    if meet <= carrier and carrier not in closure:
                        closure.add(carrier)
                        changed = True
    return closure


def trace_cover(script_name: str) -> None:
    data = runpy.run_path(str(ROOT / script_name), run_name="relay_data")
    n = data["N"]
    anchors = tuple(data["ANCHORS"])
    universe = frozenset(data["UNIVERSE"])
    endpoint_pairs = tuple(
        (frozenset(e), frozenset(h)) for e, h in data["ENDPOINTS"]
    )
    intersections = tuple(e & h for e, h in endpoint_pairs)
    carriers = sorted(
        {frozenset()} | {x for pair in endpoint_pairs for x in pair}
        | set(intersections),
        key=lambda x: (len(x), tuple(sorted(x))),
    )

    per_anchor: list[dict[frozenset[int], set[int]]] = []
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
            for (left, right), meet in zip(endpoint_pairs, intersections):
                left_contexts = tuple(contexts[left])
                right_contexts = tuple(contexts[right])
                for left_context in left_contexts:
                    for right_context in right_contexts:
                        merged = left_context | right_context
                        for carrier in carriers:
                            if meet <= carrier:
                                changed |= add_minimal(contexts[carrier], merged)

        # Independent small-domain check: every subset of initial literal
        # generators induces a direct closure matching the context antichains.
        for selected_bits in range(1 << n):
            direct = direct_carrier_closure(
                generators, endpoint_pairs, carriers, selected_bits
            )
            for carrier in carriers:
                represented = any(
                    (context & selected_bits) == context
                    for context in contexts[carrier]
                )
                assert represented == (carrier in direct), (
                    script_name, anchor, selected_bits, carrier,
                    represented, carrier in direct,
                )
        per_anchor.append(contexts)

    empty = frozenset()
    assert all(contexts[empty] for contexts in per_anchor), script_name
    print(f"{script_name}: anchors={len(anchors)} rules={len(endpoint_pairs)} "
          f"carriers={len(carriers)}")
    for anchor, contexts in zip(anchors, per_anchor):
        roots = sorted(contexts[empty], key=lambda mask: (mask.bit_count(), mask))
        sizes = sorted({mask.bit_count() for mask in roots})
        rendered = [
            "".join(str(i) for i in range(n) if (mask >> i) & 1)
            for mask in roots
        ]
        print(f"  anchor={anchor:0{n}b}; root_context_count={len(roots)}; "
              f"minimal_sizes={sizes}; coordinate_patterns={rendered}")

    for rule_index, meet in enumerate(intersections):
        active = [i for i, contexts in enumerate(per_anchor)
                  if contexts[meet]]
        pattern_count = sum(len(per_anchor[i][meet]) for i in active)
        print(f"  rule={rule_index}; closure_support={len(active)}/"
              f"{len(anchors)} anchors; anchor_context_instances="
              f"{pattern_count}")


def main() -> None:
    trace_cover("experiment_weight_one_anchor_cover4.py")
    trace_cover("experiment_weight_one_anchor_cover5_six_rules.py")
    trace_cover("experiment_sparse_ball_native_n5_witness.py")
    trace_cover("experiment_sparse_ball_canonical_selector_witness.py")


if __name__ == "__main__":
    main()
