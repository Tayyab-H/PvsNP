"""Sample 4-bit linear basis changes and solve exact universal cover sizes.

For each invertible transform of the weight-at-most-one anchor set, the
PySAT encoding searches arbitrary endpoints for one, then two, then three
relay rules. Symmetry breaking is disabled because most transforms do not
preserve coordinate permutations. Any SAT witness is independently checked
by the source verifier's exact preservation closure.
"""

from __future__ import annotations

import contextlib
import io
import random
import runpy
from pathlib import Path


N = 4
ANCHORS = tuple(x for x in range(1 << N) if x.bit_count() <= 1)
RNG = random.Random(20260924)
ROOT = Path(__file__).resolve().parent
SOLVE = runpy.run_path(
    str(ROOT / "experiment_relay_cover_pysat.py"),
    run_name="relay_solver_module",
)["solve"]


def apply(rows: tuple[int, ...], value: int) -> int:
    return sum(((row & value).bit_count() & 1) << i
               for i, row in enumerate(rows))


def is_invertible(rows: tuple[int, ...]) -> bool:
    return len({apply(rows, x) for x in range(1 << N)}) == (1 << N)


def sample_matrices(count: int) -> list[tuple[int, ...]]:
    selected: set[tuple[int, ...]] = {tuple(1 << i for i in range(N))}
    while len(selected) < count:
        rows = tuple(RNG.randrange(1 << N) for _ in range(N))
        if is_invertible(rows):
            selected.add(rows)
    return sorted(selected)


def solve_status(rows: tuple[int, ...], rule_count: int) -> tuple[bool, str]:
    transformed_anchors = [apply(rows, a) for a in ANCHORS]
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        SOLVE(N, rule_count, transformed_anchors, symmetry_break=False)
    output = buffer.getvalue()
    is_sat = "sat_status=sat" in output
    assert "verified_universal_cover=True" in output or not is_sat, output
    return is_sat, output


def main() -> None:
    matrices = sample_matrices(20)
    counts = {1: 0, 2: 0, 3: 0, 4: 0, ">4": 0}
    for index, rows in enumerate(matrices):
        found = False
        tested_rules = []
        for rules in (1, 2, 3, 4):
            sat_status, output = solve_status(rows, rules)
            tested_rules.append(rules)
            if sat_status:
                counts[rules] += 1
                found = True
                xor_cost = sum(max(0, row.bit_count() - 1) for row in rows)
                print(f"sample={index}; rows={rows}; row_weights="
                      f"{tuple(row.bit_count() for row in rows)}; "
                      f"naive_xor_cost={xor_cost}; first_sat_rules={rules}; "
                      f"solver_unsat_before={tested_rules[:-1]}")
                if rules == 1:
                    assert "verified_universal_cover=True" in output
                break
        if not found:
            counts[">4"] += 1
            print(f"sample={index}; rows={rows}; solver_unsat_rules="
                  f"{tested_rules}")
    print(f"sampled_matrices={len(matrices)}; first_cover_counts={counts}")


if __name__ == "__main__":
    main()
