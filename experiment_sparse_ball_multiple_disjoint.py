"""Search for a 5-rule n=5 radius-two cover with at least two disjoint seeds."""

from __future__ import annotations

import contextlib
import io
import runpy
from ast import literal_eval
from pathlib import Path


ROOT = Path(__file__).resolve().parent
N = 5
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 2]
SOLVE = runpy.run_path(
    str(ROOT / "experiment_relay_cover_pysat.py"),
    run_name="relay_solver_module",
)["solve"]


def main() -> None:
    print("searching native n=5, 5 rules, at least 2 disjoint seeds",
          flush=True)
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        SOLVE(
            N,
            5,
            ANCHORS,
            symmetry_break=True,
            minimum_disjoint_rules=2,
        )
    output = capture.getvalue()
    print(output)
    if "sat_status=sat" not in output:
        return
    assert "verified_universal_cover=True" in output
    endpoint_pairs = []
    for line in output.splitlines():
        if line.lstrip().startswith("rule") and " E=" in line:
            left = line.split("E=", 1)[1].split("; H=", 1)[0]
            right = line.split("H=", 1)[1].split("; intersection=", 1)[0]
            endpoint_pairs.append((literal_eval(left), literal_eval(right)))
    assert len(endpoint_pairs) == 5
    disjoint_count = sum(not (set(left) & set(right))
                         for left, right in endpoint_pairs)
    assert disjoint_count >= 2
    path = ROOT / "experiment_sparse_ball_multiple_disjoint_witness.py"
    lines = [
        '"""Exact-closure-verified n=5 cover with multiple disjoint seeds."""',
        f"N = {N}",
        f"ANCHORS = {tuple(ANCHORS)!r}",
        f"UNIVERSE = {tuple(x for x in range(1 << N) if x not in set(ANCHORS))!r}",
        "ENDPOINTS = (",
    ]
    lines.extend(
        f"    (frozenset({tuple(left)!r}), frozenset({tuple(right)!r})),"
        for left, right in endpoint_pairs
    )
    lines.extend((")", ""))
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"multiple_disjoint_witness={path}; disjoint_rules={disjoint_count}")


if __name__ == "__main__":
    main()
