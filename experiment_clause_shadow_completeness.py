"""Finite audit of which literal clauses endpoint carriers can realize.

For a consistent set S of literals, form its smallest endpoint carrier
C_S = union_{(i,b) in S} B_{i,b}, where B_{i,b} is the high-universe slice.
The endpoint's actual clause profile consists of every literal slice contained
in C_S.  The density lemma predicts that this profile is exactly S whenever
the face avoiding S still contains a high point.
"""

from __future__ import annotations

import itertools
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CASES = (
    "experiment_weight_one_anchor_cover4.py",
    "experiment_weight_one_anchor_cover5_six_rules.py",
    "experiment_basis_exception_contexts.py",
    "experiment_sparse_ball_native_n5_witness.py",
    "experiment_sparse_ball_canonical_selector_witness.py",
    "experiment_sparse_ball_multiple_disjoint_witness.py",
)


def main() -> None:
    first_data = None
    for case in CASES:
        data = runpy.run_path(str(ROOT / case), run_name="clause_shadow_data")
        if first_data is None:
            first_data = data
        n = data["N"]
        high = frozenset(data["UNIVERSE"])
        excluded_count = (1 << n) - len(high)
        slices = {
            (i, b): frozenset(x for x in high if ((x >> i) & 1) == b)
            for i in range(n)
            for b in (0, 1)
        }
        exact_by_width: dict[int, int] = {}
        extra_by_width: dict[int, int] = {}
        profile_images: set[frozenset[tuple[int, int]]] = set()

        # None/0/1 per coordinate enumerates all 3^n consistent literal sets.
        for assignment in itertools.product((None, 0, 1), repeat=n):
            selected = frozenset(
                (i, b) for i, b in enumerate(assignment) if b is not None
            )
            carrier = frozenset().union(*(slices[lit] for lit in selected))
            profile = frozenset(
                lit for lit, literal_slice in slices.items()
                if literal_slice <= carrier
            )
            profile_images.add(profile)
            width = len(selected)
            if profile == selected:
                exact_by_width[width] = exact_by_width.get(width, 0) + 1
            else:
                extra_by_width[width] = extra_by_width.get(width, 0) + 1
                assert selected < profile, (case, selected, profile)

        safe_width = max(
            (q for q in range(n) if (1 << (n - q - 1)) > excluded_count),
            default=-1,
        )
        print(
            f"{case}: n={n}; consistent_clause_sets={3**n}; "
            f"excluded_tables={excluded_count}; "
            f"density_safe_width<={safe_width}; "
            f"distinct_profiles={len(profile_images)}; "
            f"exact_by_width={dict(sorted(exact_by_width.items()))}; "
            f"extra_literals_by_width={dict(sorted(extra_by_width.items()))}"
        )

    assert first_data is not None
    n = first_data["N"]
    high = frozenset(first_data["UNIVERSE"])
    point = next(iter(high))
    slices = tuple(
        frozenset(x for x in high if ((x >> i) & 1) == b)
        for i in range(n)
        for b in (0, 1)
    )
    assert min(map(len, slices)) >= 2
    empty_profile_carrier = frozenset()
    singleton_profile_carrier = frozenset((point,))
    assert all(not (s <= empty_profile_carrier) for s in slices)
    assert all(not (s <= singleton_profile_carrier) for s in slices)
    premises = singleton_profile_carrier
    assert not (premises & premises <= empty_profile_carrier)
    assert premises & premises <= singleton_profile_carrier
    print(
        "same-profile residue witness: premise and both consequents have "
        "empty clause profile, but intersection inclusion changes "
        "(False -> True)"
    )


if __name__ == "__main__":
    main()
