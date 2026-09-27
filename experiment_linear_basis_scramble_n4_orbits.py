"""Solve the 4-bit simplex-anchor basis scramble by hypercube orbits.

There are 840 unordered bases of F_2^4. Hypercube automorphisms (coordinate
permutations and bit flips) preserve the universal-cover problem, reducing the
exact SAT audit to the orbit representatives generated below. For each class,
search arbitrary endpoints for increasing rule counts; every SAT witness is
checked by the independent exact-closure routine in experiment_relay_cover_pysat.py.
"""

from __future__ import annotations

import contextlib
import io
import runpy
from itertools import combinations, permutations
from pathlib import Path


N = 4
ROOT = Path(__file__).resolve().parent
SOLVE = runpy.run_path(
    str(ROOT / "experiment_relay_cover_pysat.py"),
    run_name="relay_solver_module",
)["solve"]
COORDINATE_PERMUTATIONS = tuple(permutations(range(N)))


def independent(vectors: tuple[int, ...]) -> bool:
    span = {0}
    for vector in vectors:
        if vector in span:
            return False
        span |= {x ^ vector for x in tuple(span)}
    return len(span) == (1 << N)


def permute_point(point: int, permutation: tuple[int, ...]) -> int:
    return sum(((point >> i) & 1) << permutation[i]
               for i in range(N))


def canonical_orbit_key(anchor_set: frozenset[int]) -> tuple[int, ...]:
    return min(
        tuple(sorted(permute_point(point, permutation) ^ translation
                     for point in anchor_set))
        for permutation in COORDINATE_PERMUTATIONS
        for translation in range(1 << N)
    )


def orbit_representatives() -> list[frozenset[int]]:
    unordered_bases = [basis for basis in combinations(range(1, 1 << N), N)
                       if independent(basis)]
    assert len(unordered_bases) == 840
    representatives: dict[tuple[int, ...], frozenset[int]] = {}
    for basis in unordered_bases:
        anchors = frozenset((0, *basis))
        representatives.setdefault(canonical_orbit_key(anchors), anchors)
    assert len(representatives) == 14
    return [representatives[key] for key in sorted(representatives)]


def solve_status(anchors: frozenset[int], rule_count: int) -> tuple[bool, str]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        SOLVE(N, rule_count, sorted(anchors), symmetry_break=False)
    output = buffer.getvalue()
    is_sat = "sat_status=sat" in output
    assert not is_sat or "verified_universal_cover=True" in output, output
    return is_sat, output


def high_free_certificate_profile(anchors: frozenset[int]) -> tuple[int, ...]:
    """Min fixed coordinates making an anchor's entire face low (outside U)."""
    profile = []
    for anchor in sorted(anchors):
        min_fixed = N + 1
        for count in range(N + 1):
            for fixed in combinations(range(N), count):
                face = {
                    point for point in range(1 << N)
                    if all(((point >> bit) & 1) == ((anchor >> bit) & 1)
                           for bit in fixed)
                }
                if face <= anchors:
                    min_fixed = min(min_fixed, count)
        assert min_fixed <= N
        profile.append(min_fixed)
    return tuple(profile)


def main() -> None:
    representatives = orbit_representatives()
    counts = {m: 0 for m in range(1, 6)}
    over_five = 0
    for index, anchors in enumerate(representatives):
        tested = []
        for rules in range(1, 6):
            sat_status, _ = solve_status(anchors, rules)
            tested.append(rules)
            if sat_status:
                counts[rules] += 1
                print(f"orbit={index}; anchors={tuple(sorted(anchors))}; "
                      f"high_free_certificate_profile="
                      f"{high_free_certificate_profile(anchors)}; "
                      f"first_sat_rules={rules}; solver_unsat_before="
                      f"{tested[:-1]}")
                break
        else:
            over_five += 1
            print(f"orbit={index}; anchors={tuple(sorted(anchors))}; "
                  f"high_free_certificate_profile="
                  f"{high_free_certificate_profile(anchors)}; "
                  f"solver_unsat_rules={tested}")
    print(f"unordered_bases=840; hypercube_orbits={len(representatives)}; "
          f"first_sat_distribution={counts}; no_sat_through_5={over_five}")


if __name__ == "__main__":
    main()
