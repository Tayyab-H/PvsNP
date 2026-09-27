"""Cross-check the first-seed-normal-form SAT encoding on the n=5 toy."""

from __future__ import annotations

import contextlib
import io
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parent
N = 5
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 2]
SOLVE = runpy.run_path(
    str(ROOT / "experiment_relay_cover_pysat.py"),
    run_name="relay_solver_module",
)["solve"]


def main() -> None:
    for required in (1, 2, 3):
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            SOLVE(
                N,
                5,
                ANCHORS,
                symmetry_break=True,
                minimum_disjoint_rules=required,
                first_seed_normal_form=True,
            )
        output = capture.getvalue()
        status = "sat" if "sat_status=sat" in output else "unsat"
        if status == "sat":
            assert "verified_universal_cover=True" in output
        print(f"first_seed_normal_form=True; minimum_seeds={required}; "
              f"status={status}")


if __name__ == "__main__":
    main()
