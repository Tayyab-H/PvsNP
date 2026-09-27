"""Compare final and preseed supports for disjoint rules in saved covers.

The preseed closure omits all disjoint rules, preventing empty-set feedback from
making a later seed appear to activate independently.
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
    for script_name in CASES:
        data = runpy.run_path(str(ROOT / script_name), run_name="relay_data")
        n = data["N"]
        universe = frozenset(data["UNIVERSE"])
        pairs = tuple(
            (frozenset(left), frozenset(right))
            for left, right in data["ENDPOINTS"]
        )
        meets = tuple(left & right for left, right in pairs)
        carriers = sorted(
            {frozenset()} | {x for pair in pairs for x in pair} | set(meets),
            key=lambda x: (len(x), tuple(sorted(x))),
        )
        low = set(data["ANCHORS"])
        high = set(universe) - low
        assert set(data["UNIVERSE"]) == high
        assert low | high == set(range(1 << n))

        print(f"{script_name}: n={n}; rules={len(pairs)}; "
              f"low={len(low)}; high={len(high)}")
        disjoint_count = 0
        disjoint_joint_supports: list[set[int]] = []
        disjoint_preseed_supports: list[set[int]] = []
        nonseed_pairs = tuple(
            pair for pair, meet in zip(pairs, meets) if meet
        )
        for rule_index, ((left, right), meet) in enumerate(zip(pairs, meets)):
            if meet:
                continue
            disjoint_count += 1
            left_support: set[int] = set()
            right_support: set[int] = set()
            preseed_left_support: set[int] = set()
            preseed_right_support: set[int] = set()
            for anchor in range(1 << n):
                generators = [
                    frozenset(
                        x for x in universe
                        if ((x >> bit) & 1) == ((anchor >> bit) & 1)
                    )
                    for bit in range(n)
                ]
                closure = direct_carrier_closure(
                    generators, pairs, carriers, (1 << n) - 1
                )
                preseed_closure = direct_carrier_closure(
                    generators, nonseed_pairs, carriers, (1 << n) - 1
                )
                if left in closure:
                    left_support.add(anchor)
                if right in closure:
                    right_support.add(anchor)
                if left in preseed_closure:
                    preseed_left_support.add(anchor)
                if right in preseed_closure:
                    preseed_right_support.add(anchor)

            joint = left_support & right_support
            preseed_support = preseed_left_support & preseed_right_support
            assert not (joint & high), (script_name, rule_index, joint & high)
            disjoint_joint_supports.append(joint)
            assert not (preseed_support & high), (
                script_name, rule_index, preseed_support & high
            )
            disjoint_preseed_supports.append(preseed_support)
            print(
                f"  disjoint_rule={rule_index}; left_support={len(left_support)}/32; "
                f"right_support={len(right_support)}/32; "
                f"low_covered={len(joint & low)}/{len(low)}; "
                f"first_seed_low={len(preseed_support & low)}/{len(low)}; "
                f"first_premises={len(preseed_left_support)}/"
                f"{len(preseed_right_support)}; "
                f"first_high_spill={len(preseed_left_support & high)}/"
                f"{len(preseed_right_support & high)}; "
                f"first_seed_anchors={sorted(preseed_support & low)}; "
                f"left_high_spill={len(left_support & high)}; "
                f"right_high_spill={len(right_support & high)}; "
                f"high_overlap={len(joint & high)}"
            )
        assert disjoint_count > 0
        covered = set().union(*disjoint_joint_supports)
        assert low <= covered, (script_name, low - covered)
        first_covered = set().union(*disjoint_preseed_supports)
        assert low <= first_covered, (script_name, low - first_covered)


if __name__ == "__main__":
    main()
