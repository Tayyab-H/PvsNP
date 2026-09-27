"""Cross-check column sorting against full S_n lex leaders on small n."""

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


def status(output: str) -> str:
    if "sat_status=sat" in output:
        return "sat"
    if "sat_status=unsat" in output:
        return "unsat"
    raise AssertionError("solver output has no conclusive status")


def run(n: int, rules: int, mode: str) -> str:
    anchors = [x for x in range(1 << n) if x.bit_count() <= n - 2]
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        SOLVE(
            n,
            rules,
            anchors,
            symmetry_break=(mode == "full"),
            near_full_column_symmetry=(mode == "column"),
            minimum_disjoint_rules=1,
            first_seed_normal_form=True,
        )
    output = capture.getvalue()
    (ROOT / f"near_full_cube_n{n}_m{rules}_{mode}sym_solver.txt").write_text(
        output, encoding="utf-8"
    )
    return status(output)


def main() -> None:
    comparisons = []
    for n in range(3, 8):
        upper = (n - 1).bit_length()
        for rules in range(1, upper):
            full = run(n, rules, "full")
            column = run(n, rules, "column")
            assert full == column, (n, rules, full, column)
            comparisons.append((n, rules, full))
            print(f"n={n}; rules={rules}; full_Sn={full}; "
                  f"column_sort={column}; matched=True", flush=True)
    (ROOT / "near_full_symmetry_crosscheck.txt").write_text(
        "\n".join(f"n={n}; rules={m}; status={s}" for n, m, s in comparisons)
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
