"""Search small weight-at-most-two promise balls with valid S_n symmetry.

For each n, anchors are truth tables of weight at most two and the high
universe is their complement. Coordinate permutations preserve this family,
so the relay SAT model may safely use its S_n lex leaders. Every SAT cover is
checked by the solver wrapper's direct support-closure verifier; UNSAT remains
solver status without a proof trace.
"""

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
    for n in (3, 4, 5):
        anchors = [x for x in range(1 << n) if x.bit_count() <= 2]
        print(f"dimension={n}; anchors={len(anchors)}; universe={2**n-len(anchors)}")
        for rules in range(1, n + 3):
            output_buffer = io.StringIO()
            with contextlib.redirect_stdout(output_buffer):
                SOLVE(n, rules, anchors, symmetry_break=True)
            output = output_buffer.getvalue()
            sat = "sat_status=sat" in output
            print(f"  rules={rules}; sat={sat}", flush=True)
            if sat:
                assert "verified_universal_cover=True" in output, output
                path = ROOT / f"weight_two_ball_n{n}_m{rules}.txt"
                path.write_text(output, encoding="utf-8")
                print(f"  exact_closure_witness={path}")
                break
        else:
            print(f"  no_cover_through={n+2}")


if __name__ == "__main__":
    main()
