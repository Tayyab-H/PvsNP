"""A linear-rule relay with exponentially many minimal seed contexts.

The low set is a product of k two-bit OR clauses.  The high universe is its
complement, so every satisfying minterm is a high-free cube.  A chain of
intersection endpoints computes the conjunction, and one terminal disjoint
seed accepts exactly the low set.
"""

from __future__ import annotations

from itertools import product

from experiment_relay_proof_contexts import direct_carrier_closure
from experiment_relay_context_normal_form import add_minimal, compatible_union


def main() -> None:
    for k in range(2, 7):
        n = 2 * k
        all_points = frozenset(range(1 << n))
        low = frozenset(
            x for x in all_points
            if all(((x >> (2 * i)) & 1) or ((x >> (2 * i + 1)) & 1)
                   for i in range(k))
        )
        high = all_points - low
        clauses = tuple(
            frozenset(
                x for x in high
                if ((x >> (2 * i)) & 1) or ((x >> (2 * i + 1)) & 1)
            )
            for i in range(k)
        )
        prefixes = [clauses[0]]
        for i in range(1, k - 1):
            prefixes.append(prefixes[-1] & clauses[i])
        # Rule list: prefix conjunctions, followed by one terminal disjoint seed.
        pairs = tuple(
            [(prefixes[i - 1], clauses[i]) for i in range(1, k - 1)]
            + [(prefixes[-1], clauses[-1])]
        )
        m = len(pairs)
        endpoints = tuple(side for pair in pairs for side in pair)

        # The endpoint clause shadows are exactly the k pair clauses and empty
        # shadows for intermediate prefix carriers.
        expected_shadows = []
        for endpoint in endpoints:
            if endpoint in clauses:
                i = clauses.index(endpoint)
                expected_shadows.append(frozenset(((2 * i, 1), (2 * i + 1, 1))))
            else:
                expected_shadows.append(frozenset())
        for j, endpoint in enumerate(endpoints):
            actual = frozenset(
                (i, b) for i in range(n) for b in (0, 1)
                if frozenset(x for x in high if ((x >> i) & 1) == b) <= endpoint
            )
            assert actual == expected_shadows[j], (k, j, actual, expected_shadows[j])

        # Full carrier closure agrees with the product-of-clauses low set.
        carriers = sorted(
            {frozenset()} | set(endpoints)
            | {left & right for left, right in pairs},
            key=lambda c: (len(c), tuple(sorted(c))),
        )
        for anchor in range(1 << n):
            generators = [
                frozenset(x for x in high
                          if ((x >> i) & 1) == ((anchor >> i) & 1))
                for i in range(n)
            ]
            closure = direct_carrier_closure(
                generators, pairs, carriers, (1 << n) - 1
            )
            assert (frozenset() in closure) == (anchor in low), (k, anchor)

        # Core-only minimal contexts, then the terminal seed's antichain.
        slices = {
            (i, b): frozenset(x for x in high if ((x >> i) & 1) == b)
            for i in range(n) for b in (0, 1)
        }
        contexts = [
            {frozenset(((i, b),)) for i in range(n) for b in (0, 1)
             if slices[i, b] <= endpoint}
            for endpoint in endpoints
        ]
        core_rules = tuple(
            r for r, (left, right) in enumerate(pairs) if left & right
        )
        changed = True
        while changed:
            changed = False
            for r in core_rules:
                left, right = pairs[r]
                meet = left & right
                for p in tuple(contexts[2 * r]):
                    for q in tuple(contexts[2 * r + 1]):
                        merged = compatible_union(p, q)
                        if merged is None:
                            continue
                        for j, endpoint in enumerate(endpoints):
                            if meet <= endpoint and add_minimal(contexts[j], merged):
                                changed = True

        seed_r = m - 1
        seed_terms = set()
        for p in contexts[2 * seed_r]:
            for q in contexts[2 * seed_r + 1]:
                merged = compatible_union(p, q)
                if merged is not None:
                    add_minimal(seed_terms, merged)
        assert len(seed_terms) == 2**k, (k, len(seed_terms), seed_terms)
        assert {len(term) for term in seed_terms} == {k}, (k, seed_terms)
        for anchor in range(1 << n):
            term_accept = any(
                all(((anchor >> i) & 1) == b for i, b in term)
                for term in seed_terms
            )
            assert term_accept == (anchor in low), (k, anchor)

        print(
            f"k={k}; N={n}; rules={m}; low_anchors={len(low)}; "
            f"minimal_seed_contexts={len(seed_terms)}=2^{k}; "
            f"context_width={k}; all_{1<<n}_anchors_verified=True"
        )


if __name__ == "__main__":
    main()
