"""Target a six-rule cover for the n=6 radius-two anchor ball."""

from __future__ import annotations

import runpy


SOLVE = runpy.run_path(
    "experiment_relay_cover_pysat.py", run_name="relay_solver_module"
)["solve"]
N = 6
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 2]


for rule_count in (5, 6):
    print(f"start dimension={N}; anchors={len(ANCHORS)}; rules={rule_count}; "
          "valid_coordinate_symmetry=True", flush=True)
    SOLVE(N, rule_count, ANCHORS, symmetry_break=True)
