"""Map the number of disjoint seeds among 5-rule n=5 radius-two covers."""

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
    for required in range(1, 6):
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            SOLVE(
                N,
                5,
                ANCHORS,
                symmetry_break=True,
                minimum_disjoint_rules=required,
            )
        output = capture.getvalue()
        status = "sat" if "sat_status=sat" in output else "unsat"
        if status == "unsat":
            print(f"minimum_disjoint_rules={required}; status=unsat")
            continue
        assert "verified_universal_cover=True" in output
        pairs = []
        for line in output.splitlines():
            if line.lstrip().startswith("rule") and " E=" in line:
                left = set(literal_eval(line.split("E=", 1)[1].split("; H=", 1)[0]))
                right = set(literal_eval(line.split("H=", 1)[1].split("; intersection=", 1)[0]))
                pairs.append((left, right))
        actual = sum(not (left & right) for left, right in pairs)
        assert actual >= required
        print(f"minimum_disjoint_rules={required}; status=sat; actual={actual}")


if __name__ == "__main__":
    main()
