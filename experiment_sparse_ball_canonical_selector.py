"""Test whether a fixed canonical certificate selector admits 5 relay rules.

For each wt<=2 anchor, retain only the first three zero-coordinate slices.
These are always a high-free certificate. A SAT cover under these restricted
generators would show the network can route one certificate per anchor, rather
than needing every minimal transversal in the root antichain.
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
FORCED_BITS = {
    a: set([i for i in range(N) if ((a >> i) & 1) == 0][:N - 2])
    for a in ANCHORS
}
assert all(len(bits) == N - 2 for bits in FORCED_BITS.values())


def main() -> None:
    print("searching 5-rule cover for one canonical high-free triple per anchor",
          flush=True)
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        SOLVE(
            N,
            5,
            ANCHORS,
            symmetry_break=False,
            forced_bits_by_anchor=FORCED_BITS,
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
    data_path = ROOT / "experiment_sparse_ball_canonical_selector_witness.py"
    source = [
        '"""Saved cover from the one-canonical-context restricted search."""',
        "N = 5",
        f"ANCHORS = {tuple(ANCHORS)!r}",
        f"UNIVERSE = {tuple(x for x in range(1 << N) if x not in set(ANCHORS))!r}",
        f"FORCED_BITS_BY_ANCHOR = { {a: tuple(sorted(bits)) for a, bits in FORCED_BITS.items()}!r}",
        "ENDPOINTS = (",
    ]
    source.extend(
        f"    (frozenset({tuple(e)!r}), frozenset({tuple(h)!r})),"
        for e, h in endpoint_pairs
    )
    source.extend((")", ""))
    data_path.write_text("\n".join(source), encoding="utf-8")
    print(f"saved_witness_data={data_path}")


if __name__ == "__main__":
    main()
