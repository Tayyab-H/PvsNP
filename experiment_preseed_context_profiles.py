"""Trace proof contexts before any disjoint seed can feed back empty."""

from __future__ import annotations

import runpy
from pathlib import Path

from experiment_relay_proof_contexts import add_minimal, direct_carrier_closure


ROOT = Path(__file__).resolve().parent
CASES = (
    "experiment_sparse_ball_native_n5_witness.py",
    "experiment_sparse_ball_canonical_selector_witness.py",
    "experiment_sparse_ball_multiple_disjoint_witness.py",
)


def trace(script_name: str) -> None:
    data = runpy.run_path(str(ROOT / script_name), run_name="relay_data")
    n = data["N"]
    low = set(data["ANCHORS"])
    high = set(data["UNIVERSE"])
    universe = frozenset(high)
    pairs = tuple(
        (frozenset(left), frozenset(right))
        for left, right in data["ENDPOINTS"]
    )
    meets = tuple(left & right for left, right in pairs)
    disjoint_indices = [i for i, meet in enumerate(meets) if not meet]
    nonseed_pairs = tuple(
        pair for i, pair in enumerate(pairs) if i not in disjoint_indices
    )
    carriers = sorted(
        {frozenset()} | {x for pair in pairs for x in pair} | set(meets),
        key=lambda x: (len(x), tuple(sorted(x))),
    )

    first_seed_sets: dict[int, set[int]] = {
        rule: set() for rule in disjoint_indices
    }
    root_contexts: dict[tuple[int, int], set[int]] = {}
    for anchor in sorted(low | high):
        generators = [
            frozenset(
                x for x in universe
                if ((x >> bit) & 1) == ((anchor >> bit) & 1)
            )
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
            for (left, right), meet in zip(nonseed_pairs,
                                           [meets[i] for i in range(len(meets))
                                            if i not in disjoint_indices]):
                for left_context in tuple(contexts[left]):
                    for right_context in tuple(contexts[right]):
                        merged = left_context | right_context
                        for carrier in carriers:
                            if meet <= carrier:
                                changed |= add_minimal(contexts[carrier], merged)

        for selected in range(1 << n):
            direct = direct_carrier_closure(
                generators, nonseed_pairs, carriers, selected
            )
            for carrier in carriers:
                represented = any(
                    (context & selected) == context
                    for context in contexts[carrier]
                )
                assert represented == (carrier in direct), (
                    script_name, anchor, selected, carrier
                )

        for rule in disjoint_indices:
            left, right = pairs[rule]
            lcontexts = contexts[left]
            rcontexts = contexts[right]
            if not lcontexts or not rcontexts:
                continue
            first_seed_sets[rule].add(anchor)
            combined: set[int] = set()
            for q in lcontexts:
                for r in rcontexts:
                    add_minimal(combined, q | r)
            assert combined
            for context in combined:
                for point in high:
                    if all(
                        ((point >> bit) & 1) == ((anchor >> bit) & 1)
                        for bit in range(n) if (context >> bit) & 1
                    ):
                        raise AssertionError(
                            (script_name, rule, anchor, context, point)
                        )
            root_contexts[(anchor, rule)] = combined

    low_cover = set().union(*(first_seed_sets[r] for r in disjoint_indices))
    assert low <= low_cover, (script_name, low - low_cover)
    assert not (low_cover & high)
    print(f"{script_name}: rules={len(pairs)}; disjoint_seeds={disjoint_indices}")
    for rule in disjoint_indices:
        anchors = first_seed_sets[rule]
        counts = [len(root_contexts[(a, rule)]) for a in anchors]
        min_sizes = [
            min(mask.bit_count() for mask in root_contexts[(a, rule)])
            for a in anchors
        ]
        print(
            f"  seed={rule}; first_support={len(anchors)}; "
            f"low_support={len(anchors & low)}/{len(low)}; "
            f"context_count_range={(min(counts), max(counts))}; "
            f"min_context_size_range={(min(min_sizes), max(min_sizes))}"
        )


def main() -> None:
    for script_name in CASES:
        trace(script_name)


if __name__ == "__main__":
    main()
