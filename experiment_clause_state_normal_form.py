"""Verify that relay acceptance factors through endpoint-clause flags.

For each endpoint C, its initial flag is the clause that is true when at
least one anchor-matching literal slice is contained in C. Given those 2m
flags, non-disjoint rule closure and the terminal-seed test are determined.
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
        high = frozenset(data["UNIVERSE"])
        low = set(data["ANCHORS"])
        endpoints = tuple(
            frozenset(side) for pair in data["ENDPOINTS"] for side in pair
        )
        pairs = tuple(
            (frozenset(e), frozenset(h)) for e, h in data["ENDPOINTS"]
        )
        core = tuple((e, h) for e, h in pairs if e & h)
        seeds = tuple((e, h) for e, h in pairs if not (e & h))
        carriers = sorted(
            {frozenset()} | set(endpoints)
            | {e & h for e, h in pairs},
            key=lambda c: (len(c), tuple(sorted(c))),
        )

        def clause_state(anchor: int) -> int:
            generators = [
                frozenset(x for x in high
                          if ((x >> i) & 1) == ((anchor >> i) & 1))
                for i in range(n)
            ]
            return sum(
                (1 << j)
                for j, endpoint in enumerate(endpoints)
                if any(generator <= endpoint for generator in generators)
            )

        def decoded_from_state(state: int) -> bool:
            active = {
                endpoint for j, endpoint in enumerate(endpoints)
                if (state >> j) & 1
            }
            changed = True
            while changed:
                changed = False
                for e, h in core:
                    if e in active and h in active:
                        meet = e & h
                        for endpoint in endpoints:
                            if meet <= endpoint and endpoint not in active:
                                active.add(endpoint)
                                changed = True
            return any(e in active and h in active for e, h in seeds)

        state_class: dict[int, bool] = {}
        realized: dict[int, list[int]] = {}
        for anchor in range(1 << n):
            state = clause_state(anchor)
            decoded = decoded_from_state(state)
            assert decoded == (anchor in low), (case, anchor, state, decoded)
            if state in state_class:
                assert state_class[state] == (anchor in low), (
                    case, anchor, state, state_class[state]
                )
            state_class[state] = anchor in low
            realized.setdefault(state, []).append(anchor)

            generators = [
                frozenset(x for x in high
                          if ((x >> i) & 1) == ((anchor >> i) & 1))
                for i in range(n)
            ]
            direct = direct_carrier_closure(
                generators, pairs, carriers, (1 << n) - 1
            )
            assert ((frozenset() in direct) == decoded), (
                case, anchor, state, decoded, frozenset() in direct
            )

        low_states = sum(is_low for is_low in state_class.values())
        high_states = len(state_class) - low_states
        print(f"{case}: rules={len(pairs)}; endpoint_flags={len(endpoints)}; "
              f"realized_states={len(realized)}; "
              f"low_states={low_states}; high_states={high_states}; "
              f"largest_state_fiber={max(map(len, realized.values()))}")


if __name__ == "__main__":
    main()
