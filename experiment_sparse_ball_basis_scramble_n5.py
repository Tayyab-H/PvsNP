"""Sample fast 5-bit basis changes of the weight-at-most-two anchor ball.

The 16 anchors are the truth tables of weight at most two in this toy; the
high universe is their 16-point complement. A linear encoding turns the
anchor family into a small sparse-vector code. The general SAT closure model
searches arbitrary endpoints, without coordinate-permutation symmetry
breaking, and independently verifies every SAT cover.
"""

from __future__ import annotations

import contextlib
import io
import random
import runpy
from pathlib import Path


N = 5
ANCHORS = tuple(x for x in range(1 << N) if x.bit_count() <= 2)
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


def solve_status(anchors: tuple[int, ...], rule_count: int) -> tuple[bool, str]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        SOLVE(N, rule_count, list(anchors), symmetry_break=False)
    output = buffer.getvalue()
    is_sat = "sat_status=sat" in output
    assert not is_sat or "verified_universal_cover=True" in output, output
    return is_sat, output


def main() -> None:
    matrices = sample_matrices(6)
    counts = {m: 0 for m in range(1, 7)}
    over_six = 0
    for index, rows in enumerate(matrices):
        encoded_anchors = tuple(sorted(apply(rows, a) for a in ANCHORS))
        tested = []
        for rules in range(1, 7):
            sat_status, output = solve_status(encoded_anchors, rules)
            tested.append(rules)
            print(f"progress: matrix={index}; rules={rules}; "
                  f"sat={sat_status}", flush=True)
            if sat_status:
                counts[rules] += 1
                xor_cost = sum(max(0, row.bit_count() - 1) for row in rows)
                (ROOT / f"basis_scramble_n5_sample{index}_m{rules}.txt").write_text(
                    output, encoding="utf-8"
                )
                print(f"sample={index}; rows={rows}; row_weights="
                      f"{tuple(row.bit_count() for row in rows)}; "
                      f"naive_xor_cost={xor_cost}; anchors="
                      f"{encoded_anchors}; first_sat_rules={rules}; "
                      f"solver_unsat_before={tested[:-1]}")
                break
        else:
            over_six += 1
            print(f"sample={index}; rows={rows}; anchors={encoded_anchors}; "
                  f"solver_unsat_rules={tested}")
    print(f"sampled_matrices={len(matrices)}; first_sat_distribution="
          f"{counts}; no_sat_through_6={over_six}")


if __name__ == "__main__":
    main()
