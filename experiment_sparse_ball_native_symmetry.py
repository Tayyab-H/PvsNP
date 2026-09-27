"""Exact native-basis relay search with valid S_5 symmetry breaking.

The anchor ball wt<=2 is invariant under coordinate permutations, so the
existing solver's coordinate-permutation lex leaders are sound here. This is
not sound for a generic scrambled sample and is intentionally restricted to
the native basis.
"""

from __future__ import annotations

import contextlib
import io
import runpy
from ast import literal_eval
from pathlib import Path


N = 5
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 2]
ROOT = Path(__file__).resolve().parent
SOLVE = runpy.run_path(
    str(ROOT / "experiment_relay_cover_pysat.py"),
    run_name="relay_solver_module",
)["solve"]


def main() -> None:
    print(f"native_weight_two_anchors={len(ANCHORS)}; symmetry_group=S_{N}")
    for rule_count in range(1, 9):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            SOLVE(N, rule_count, ANCHORS, symmetry_break=True)
        output = buffer.getvalue()
        sat = "sat_status=sat" in output
        print(f"rules={rule_count}; sat={sat}", flush=True)
        if sat:
            assert "verified_universal_cover=True" in output, output
            witness_path = ROOT / f"sparse_ball_native_n5_m{rule_count}.txt"
            witness_path.write_text(output, encoding="utf-8")
            endpoint_pairs = []
            for line in output.splitlines():
                if line.lstrip().startswith("rule") and " E=" in line:
                    left = line.split("E=", 1)[1].split("; H=", 1)[0]
                    right = line.split("; H=", 1)[1].split("; intersection=", 1)[0]
                    endpoint_pairs.append((literal_eval(left), literal_eval(right)))
            assert len(endpoint_pairs) == rule_count
            data_path = ROOT / "experiment_sparse_ball_native_n5_witness.py"
            data = [
                '"""Saved exact-closure-verified n=5 weight-at-most-two cover."""',
                "N = 5",
                f"ANCHORS = {tuple(ANCHORS)!r}",
                f"UNIVERSE = {tuple(x for x in range(1 << N) if x not in set(ANCHORS))!r}",
                "ENDPOINTS = (",
            ]
            data.extend(
                f"    (frozenset({tuple(left)!r}), frozenset({tuple(right)!r})),"
                for left, right in endpoint_pairs
            )
            data.extend((")", ""))
            data_path.write_text("\n".join(data), encoding="utf-8")
            print(f"witness={witness_path}")
            print(f"witness_data={data_path}")
            print(output)
            return
    print("no_cover_through_8_rules=True")


if __name__ == "__main__":
    main()
