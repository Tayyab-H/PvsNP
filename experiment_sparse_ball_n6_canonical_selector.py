"""Try a six-rule n=6 cover from one canonical zero-four-set per anchor."""

from __future__ import annotations

import contextlib
import io
import runpy
from ast import literal_eval
from pathlib import Path


N = 6
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


def main() -> None:
    print("testing n=6, six rules, first four zero coordinates per anchor; "
          "coordinate symmetry disabled", flush=True)
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        SOLVE(
            N,
            6,
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
    assert len(endpoint_pairs) == 6
    data_path = ROOT / "experiment_sparse_ball_n6_canonical_witness.py"
    source = [
        '"""Saved six-rule n=6 radius-two canonical-selector cover."""',
        f"N = {N}",
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
