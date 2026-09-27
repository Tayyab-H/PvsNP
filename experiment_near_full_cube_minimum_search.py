"""Solver-check whether fewer than log2(n) rules beat the cut construction."""

from __future__ import annotations

import contextlib
import io
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOLVE = runpy.run_path(
    str(ROOT / "experiment_relay_cover_pysat.py"),
    run_name="relay_solver_module",
)["solve"]


def main() -> None:
    for n in range(3, 11):
        anchors = [x for x in range(1 << n) if x.bit_count() <= n - 2]
        cut_count = (n - 1).bit_length()
        for rules in range(1, cut_count):
            capture = io.StringIO()
            with contextlib.redirect_stdout(capture):
                SOLVE(
                    n,
                    rules,
                    anchors,
                    near_full_column_symmetry=True,
                    minimum_disjoint_rules=1,
                    first_seed_normal_form=True,
                )
            output = capture.getvalue()
            status = "sat" if "sat_status=sat" in output else "unsat"
            if status == "sat":
                assert "verified_universal_cover=True" in output
            evidence = ROOT / f"near_full_cube_n{n}_m{rules}_solver.txt"
            evidence.write_text(output, encoding="utf-8")
            print(f"n={n}; rules={rules}; status={status}; "
                  "first_seed_normal_form=True; "
                  "near_full_column_symmetry=True; "
                  f"saved={evidence.name}", flush=True)


if __name__ == "__main__":
    main()
