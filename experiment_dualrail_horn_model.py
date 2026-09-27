"""Test the relay's monotone Horn computation on paired literal inputs.

Each endpoint contributes a clause over y[i,b].  Non-disjoint rules define a
positive Horn least fixed point on endpoint flags; disjoint rules are terminal
tests.  On valid paired inputs y[i,b] = [x_i=b], this must equal the anchor
classifier.  The same circuit is monotone on all 2N-bit inputs.
"""

from __future__ import annotations

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CASES = (
    "experiment_weight_one_anchor_cover4.py",
    "experiment_weight_one_anchor_cover5_six_rules.py",
    "experiment_basis_exception_contexts.py",
    "experiment_sparse_ball_native_n5_witness.py",
    "experiment_sparse_ball_canonical_selector_witness.py",
    "experiment_sparse_ball_multiple_disjoint_witness.py",
)


def relay_value(y: int, n: int, endpoints: tuple[frozenset[int], ...],
                shadows: tuple[frozenset[tuple[int, int]], ...],
                rules: tuple[tuple[int, int, frozenset[int], bool], ...]) -> bool:
    active = {
        j for j, shadow in enumerate(shadows)
        if any((y >> (2 * i + b)) & 1 for i, b in shadow)
    }
    core = tuple(r for r in rules if not r[3])
    changed = True
    while changed:
        changed = False
        for left_i, right_i, meet, _ in core:
            if left_i in active and right_i in active:
                for j, endpoint in enumerate(endpoints):
                    if meet <= endpoint and j not in active:
                        active.add(j)
                        changed = True
    return any(
        left_i in active and right_i in active
        for left_i, right_i, _, is_seed in rules if is_seed
    )


def main() -> None:
    for case in CASES:
        data = runpy.run_path(str(ROOT / case), run_name="dualrail_data")
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
        shadows = tuple(
            frozenset(lit for lit, literal_slice in slices.items()
                      if literal_slice <= endpoint)
            for endpoint in endpoints
        )
        rules = tuple(
            (2 * r, 2 * r + 1, e & h, not bool(e & h))
            for r, (e, h) in enumerate(pairs)
        )

        full_outputs = tuple(
            relay_value(y, n, endpoints, shadows, rules)
            for y in range(1 << (2 * n))
        )
        # Local upward checks imply monotonicity over the whole Boolean cube.
        for y, value in enumerate(full_outputs):
            for bit in range(2 * n):
                if not ((y >> bit) & 1):
                    assert not value or full_outputs[y | (1 << bit)], (
                        case, y, bit
                    )

        for anchor in range(1 << n):
            y = sum(1 << (2 * i + ((anchor >> i) & 1)) for i in range(n))
            assert relay_value(y, n, endpoints, shadows, rules) == (anchor in low), (
                case, anchor, y
            )

        core = tuple(r for r in rules if not r[3])
        seeds = tuple(r for r in rules if r[3])
        head_incidences = sum(
            sum(meet <= endpoint for endpoint in endpoints)
            for _, _, meet, _ in core
        )
        clause_gates = sum(max(0, len(shadow) - 1) for shadow in shadows)
        closure_gates = len(endpoints) * (len(core) + head_incidences)
        terminal_gates = 0 if not seeds else 2 * len(seeds) - 1
        gate_bound = clause_gates + closure_gates + terminal_gates
        print(
            f"{case}: m={m}; paired_inputs={1 << n}; "
            f"all_dualrail_inputs={1 << (2*n)}; monotone=True; "
            f"promise_exact=True; fanin2_gate_bound={gate_bound} "
            f"(clauses={clause_gates}, closure={closure_gates}, "
            f"terminal={terminal_gates})"
        )


if __name__ == "__main__":
    main()
