"""Extract minimal proof-context frontiers for the first disjoint seed.

Non-disjoint rules generate context antichains for endpoint activation.  A
terminal disjoint seed combines one left and one right context; every resulting
compatible cube must be high-free.  This checker compares their union directly
with full relay acceptance on every anchor in six saved witnesses.
"""

from __future__ import annotations

import runpy
from pathlib import Path

from experiment_relay_proof_contexts import direct_carrier_closure
from experiment_relay_context_normal_form import add_minimal, compatible_union, face


ROOT = Path(__file__).resolve().parent
CASES = (
    "experiment_weight_one_anchor_cover4.py",
    "experiment_weight_one_anchor_cover5_six_rules.py",
    "experiment_basis_exception_contexts.py",
    "experiment_sparse_ball_native_n5_witness.py",
    "experiment_sparse_ball_canonical_selector_witness.py",
    "experiment_sparse_ball_multiple_disjoint_witness.py",
)


def main() -> None:
    for case in CASES:
        data = runpy.run_path(str(ROOT / case), run_name="seed_frontier_data")
        n = data["N"]
        high = frozenset(data["UNIVERSE"])
        low = frozenset(data["ANCHORS"])
        pairs = tuple((frozenset(e), frozenset(h)) for e, h in data["ENDPOINTS"])
        endpoints = tuple(side for pair in pairs for side in pair)
        m = len(pairs)
        slices = {
            (i, b): frozenset(x for x in high if ((x >> i) & 1) == b)
            for i in range(n) for b in (0, 1)
        }
        contexts = [
            {frozenset(((i, b),)) for i in range(n) for b in (0, 1)
             if slices[i, b] <= endpoint}
            for endpoint in endpoints
        ]

        changed = True
        while changed:
            changed = False
            for r, (left, right) in enumerate(pairs):
                meet = left & right
                if not meet:  # terminal seeds do not feed the core
                    continue
                li, ri = 2 * r, 2 * r + 1
                for p in tuple(contexts[li]):
                    for q in tuple(contexts[ri]):
                        merged = compatible_union(p, q)
                        if merged is None:
                            continue
                        for j, endpoint in enumerate(endpoints):
                            if meet <= endpoint and add_minimal(contexts[j], merged):
                                changed = True

        seed_terms: list[set[frozenset[tuple[int, int]]]] = []
        for r, (left, right) in enumerate(pairs):
            if left & right:
                continue
            terms: set[frozenset[tuple[int, int]]] = set()
            for p in contexts[2 * r]:
                for q in contexts[2 * r + 1]:
                    merged = compatible_union(p, q)
                    if merged is not None:
                        add_minimal(terms, merged)
            assert all(not face(high, term) for term in terms), (case, r, terms)
            seed_terms.append(terms)

        carriers = sorted(
            {frozenset()} | set(endpoints)
            | {left & right for left, right in pairs},
            key=lambda c: (len(c), tuple(sorted(c))),
        )
        pairs_union = tuple(pairs)
        for anchor in range(1 << n):
            terms_accept = any(
                all(((anchor >> i) & 1) == b for i, b in term)
                for terms in seed_terms for term in terms
            )
            generators = [
                frozenset(x for x in high
                          if ((x >> i) & 1) == ((anchor >> i) & 1))
                for i in range(n)
            ]
            full = direct_carrier_closure(
                generators, pairs_union, carriers, (1 << n) - 1
            )
            assert terms_accept == (frozenset() in full), (case, anchor)
            assert terms_accept == (anchor in low), (case, anchor)

        all_terms = [term for terms in seed_terms for term in terms]
        widths = [len(term) for term in all_terms]
        print(
            f"{case}: rules={m}; core_contexts={sum(map(len, contexts))}; "
            f"terminal_seeds={len(seed_terms)}; "
            f"minimal_seed_cubes={len(all_terms)}; "
            f"min_width={min(widths, default=0)}; "
            f"max_width={max(widths, default=0)}; "
            f"high_free=True; exact_all_{1<<n}_anchors=True"
        )


if __name__ == "__main__":
    main()
