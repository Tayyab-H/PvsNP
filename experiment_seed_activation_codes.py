"""Encode each anchor by the seed-side endpoints active preseed.

This checks the exact decoder supplied by the first-seed normal form:
an anchor is low iff some disjoint seed has both endpoints active in the
closure generated using only non-disjoint rules.
"""

from __future__ import annotations

import runpy
from pathlib import Path

from experiment_relay_proof_contexts import direct_carrier_closure


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
        data = runpy.run_path(str(ROOT / case), run_name="relay_data")
        n = data["N"]
        universe = frozenset(data["UNIVERSE"])
        low = set(data["ANCHORS"])
        high = set(range(1 << n)) - low
        pairs = tuple(
            (frozenset(e), frozenset(h)) for e, h in data["ENDPOINTS"]
        )
        seeds = [r for r, (e, h) in enumerate(pairs) if not (e & h)]
        core = tuple(pair for pair in pairs if pair[0] & pair[1])
        carriers = sorted(
            {frozenset()} | {x for pair in pairs for x in pair}
            | {e & h for e, h in pairs},
            key=lambda x: (len(x), tuple(sorted(x))),
        )
        profiles: dict[tuple[frozenset[int], frozenset[int]], list[int]] = {}
        for anchor in range(1 << n):
            generators = [
                frozenset(x for x in universe
                          if ((x >> bit) & 1) == ((anchor >> bit) & 1))
                for bit in range(n)
            ]
            closure = direct_carrier_closure(
                generators, core, carriers, (1 << n) - 1
            )
            left_active = frozenset(r for r in seeds if pairs[r][0] in closure)
            right_active = frozenset(r for r in seeds if pairs[r][1] in closure)
            profile = (left_active, right_active)
            profiles.setdefault(profile, []).append(anchor)
            decoded_low = bool(left_active & right_active)
            assert decoded_low == (anchor in low), (
                case, anchor, left_active, right_active, decoded_low,
            )

        low_profiles = sum(any(x in low for x in xs) for xs in profiles.values())
        high_profiles = sum(any(x in high for x in xs) for xs in profiles.values())
        print(f"{case}: seeds={seeds}; distinct_activation_codes={len(profiles)}; "
              f"low_codes={low_profiles}; high_codes={high_profiles}")
        if len(seeds) > 1:
            for (left, right), anchors in sorted(
                profiles.items(),
                key=lambda item: (len(item[0][0]) + len(item[0][1]),
                                  tuple(item[0][0]), tuple(item[0][1])),
            ):
                if len(left) > 1 or len(right) > 1 or left & right:
                    print(f"  L={sorted(left)} R={sorted(right)}; "
                          f"anchors={len(anchors)}; "
                          f"low={sum(x in low for x in anchors)}; "
                          f"high={sum(x in high for x in anchors)}")


if __name__ == "__main__":
    main()
