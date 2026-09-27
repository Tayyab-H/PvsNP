"""Verify a context-face normal form for finite relay witnesses.

For a relay endpoint C, contexts are consistent partial assignments P with
the high slice B_P contained in C.  The least context grammar starts at the
literal slices contained in endpoints and combines compatible contexts along
the original relay rules.  We replace each endpoint by the union of its
generated context faces plus a small set of point witnesses preserving every
rule-to-endpoint inclusion and every rule-pair nonemptiness bit.
"""

from __future__ import annotations

import runpy
from pathlib import Path

from experiment_relay_proof_contexts import direct_carrier_closure


ROOT = Path(__file__).resolve().parent
CASES = (
    "experiment_weight_one_anchor_cover4.py",
    "experiment_weight_one_anchor_cover5_six_rules.py",
    "experiment_basis_exception_contexts.py",
    "experiment_sparse_ball_native_n5_witness.py",
    "experiment_sparse_ball_canonical_selector_witness.py",
    "experiment_sparse_ball_multiple_disjoint_witness.py",
)


def compatible_union(left: frozenset[tuple[int, int]],
                     right: frozenset[tuple[int, int]]) -> frozenset[tuple[int, int]] | None:
    fixed = dict(left)
    if any(i in fixed and fixed[i] != b for i, b in right):
        return None
    return left | right


def face(universe: frozenset[int], context: frozenset[tuple[int, int]]) -> frozenset[int]:
    return frozenset(
        x for x in universe
        if all(((x >> i) & 1) == b for i, b in context)
    )


def add_minimal(bucket: set[frozenset[tuple[int, int]]],
                candidate: frozenset[tuple[int, int]]) -> bool:
    """Keep only inclusion-minimal contexts, which cover the largest cubes."""
    if any(old <= candidate for old in bucket):
        return False
    bucket.difference_update(old for old in tuple(bucket) if candidate <= old)
    bucket.add(candidate)
    return True


def active_endpoints(
    anchor: int,
    universe: frozenset[int],
    endpoint_sets: tuple[frozenset[int], ...],
    endpoint_pairs: tuple[tuple[frozenset[int], frozenset[int]], ...],
    n: int,
) -> set[int]:
    slices = tuple(
        frozenset(x for x in universe if ((x >> i) & 1) == b)
        for i in range(n) for b in (0, 1)
    )
    active = {
        j for j, endpoint in enumerate(endpoint_sets)
        if any(slices[2 * i + ((anchor >> i) & 1)] <= endpoint
               for i in range(n))
    }
    changed = True
    while changed:
        changed = False
        for r, (left, right) in enumerate(endpoint_pairs):
            li, ri = 2 * r, 2 * r + 1
            if li in active and ri in active:
                meet = left & right
                for j, endpoint in enumerate(endpoint_sets):
                    if meet <= endpoint and j not in active:
                        active.add(j)
                        changed = True
    return active


def main() -> None:
    for case in CASES:
        data = runpy.run_path(str(ROOT / case), run_name="context_nf_data")
        n = data["N"]
        universe = frozenset(data["UNIVERSE"])
        pairs = tuple((frozenset(e), frozenset(h)) for e, h in data["ENDPOINTS"])
        endpoint_sets = tuple(side for pair in pairs for side in pair)
        m = len(pairs)
        slices = {
            (i, b): frozenset(x for x in universe if ((x >> i) & 1) == b)
            for i in range(n) for b in (0, 1)
        }

        # Least fixed point of all proof contexts at each named endpoint.
        contexts = [
            {frozenset(((i, b),)) for i in range(n) for b in (0, 1)
             if slices[i, b] <= endpoint}
            for endpoint in endpoint_sets
        ]
        changed = True
        while changed:
            changed = False
            for r, (left, right) in enumerate(pairs):
                li, ri = 2 * r, 2 * r + 1
                left_contexts = tuple(contexts[li])
                right_contexts = tuple(contexts[ri])
                meet = left & right
                for p in left_contexts:
                    for q in right_contexts:
                        merged = compatible_union(p, q)
                        if merged is None:
                            continue
                        for j, endpoint in enumerate(endpoint_sets):
                            if meet <= endpoint and merged not in contexts[j]:
                                contexts[j].add(merged)
                                changed = True

        # Recompute the same grammar while discarding contexts dominated by a
        # subset. A smaller context covers every anchor covered by its superset.
        minimal_contexts = [
            {frozenset(((i, b),)) for i in range(n) for b in (0, 1)
             if slices[i, b] <= endpoint}
            for endpoint in endpoint_sets
        ]
        changed = True
        while changed:
            changed = False
            for r, (left, right) in enumerate(pairs):
                li, ri = 2 * r, 2 * r + 1
                left_contexts = tuple(minimal_contexts[li])
                right_contexts = tuple(minimal_contexts[ri])
                meet = left & right
                for p in left_contexts:
                    for q in right_contexts:
                        merged = compatible_union(p, q)
                        if merged is None:
                            continue
                        for j, endpoint in enumerate(endpoint_sets):
                            if meet <= endpoint and add_minimal(
                                minimal_contexts[j], merged
                            ):
                                changed = True
        expected_minimal = [
            {p for p in bucket if not any(q < p for q in bucket)}
            for bucket in contexts
        ]
        assert minimal_contexts == expected_minimal, (
            case, minimal_contexts, expected_minimal
        )
        for full_bucket, min_bucket in zip(contexts, minimal_contexts):
            assert set().union(*(face(universe, p) for p in full_bucket)) == set().union(
                *(face(universe, p) for p in min_bucket)
            ), (case, "dominated-face")
        for anchor in range(1 << n):
            for full_bucket, min_bucket in zip(contexts, minimal_contexts):
                full_hit = any(
                    all(((anchor >> i) & 1) == b for i, b in p)
                    for p in full_bucket
                )
                minimal_hit = any(
                    all(((anchor >> i) & 1) == b for i, b in p)
                    for p in min_bucket
                )
                assert full_hit == minimal_hit, (case, anchor, "support-antichain")

        # One retained high point per false inclusion and per nonempty rule meet.
        witnesses: set[int] = set()
        for r, (left, right) in enumerate(pairs):
            meet = left & right
            if meet:
                witnesses.add(min(meet))
            for endpoint in endpoint_sets:
                if not meet <= endpoint:
                    witnesses.add(min(meet - endpoint))

        normalized = []
        for j, endpoint in enumerate(endpoint_sets):
            generated_faces = set().union(
                *(face(universe, p) for p in minimal_contexts[j])
            )
            retained = {z for z in witnesses if z in endpoint}
            replacement = frozenset(generated_faces | retained)
            assert replacement <= endpoint, (case, j, replacement - endpoint)
            for lit, literal_slice in slices.items():
                assert (literal_slice <= replacement) == (literal_slice <= endpoint), (
                    case, j, lit
                )
            normalized.append(replacement)
        normalized_endpoints = tuple(normalized)
        normalized_pairs = tuple(
            (normalized_endpoints[2 * r], normalized_endpoints[2 * r + 1])
            for r in range(m)
        )

        # Check all static transition bits, not merely anchor outputs.
        for r, (left, right) in enumerate(pairs):
            old_meet = left & right
            new_left, new_right = normalized_pairs[r]
            new_meet = new_left & new_right
            assert bool(old_meet) == bool(new_meet), (case, r, "meet")
            for j in range(2 * m):
                assert (old_meet <= endpoint_sets[j]) == (
                    new_meet <= normalized_endpoints[j]
                ), (case, r, j, "inclusion")

        # Check endpoint closure and the original direct carrier closure on all inputs.
        original_carriers = sorted(
            {frozenset()} | set(endpoint_sets)
            | {left & right for left, right in pairs},
            key=lambda c: (len(c), tuple(sorted(c))),
        )
        normalized_carriers = sorted(
            {frozenset()} | set(normalized_endpoints)
            | {left & right for left, right in normalized_pairs},
            key=lambda c: (len(c), tuple(sorted(c))),
        )
        for anchor in range(1 << n):
            old_active = active_endpoints(anchor, universe, endpoint_sets, pairs, n)
            new_active = active_endpoints(
                anchor, universe, normalized_endpoints, normalized_pairs, n
            )
            assert old_active == new_active, (case, anchor, old_active, new_active)
            generators = [
                frozenset(x for x in universe
                          if ((x >> i) & 1) == ((anchor >> i) & 1))
                for i in range(n)
            ]
            old_full = direct_carrier_closure(
                generators, pairs, original_carriers, (1 << n) - 1
            )
            new_full = direct_carrier_closure(
                generators, normalized_pairs, normalized_carriers, (1 << n) - 1
            )
            assert (frozenset() in old_full) == (frozenset() in new_full), (
                case, anchor, "empty-closure"
            )

        print(
            f"{case}: rules={m}; endpoints={2*m}; "
            f"contexts={sum(map(len, contexts))}; "
            f"minimal_contexts={sum(map(len, minimal_contexts))}; "
            f"max_contexts_per_endpoint={max(map(len, contexts))}; "
            f"point_witnesses={len(witnesses)} <= {2*m*m+m}; "
            f"exact_shadow_and_rule_tensor=True; all_{1<<n}_anchors=True"
        )


if __name__ == "__main__":
    main()
