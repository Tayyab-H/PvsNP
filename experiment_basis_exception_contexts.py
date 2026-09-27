"""Inspect proof-context antichains in the 5-rule basis-scramble witness."""

from __future__ import annotations


N = 4
ANCHORS = (0, 3, 5, 9, 14)
UNIVERSE = tuple(x for x in range(1 << N) if x not in ANCHORS)
ENDPOINTS = (
    (frozenset({1, 4, 6, 7, 8, 12, 13, 15}),
     frozenset({1, 2, 4, 6, 8, 10, 11, 12})),
    (frozenset({2, 4, 6, 7, 8, 10, 11, 12, 13, 15}),
     frozenset({1, 2, 4, 6, 7, 10, 11, 15})),
    (frozenset({1, 2, 7, 8, 10, 11, 12, 13, 15}),
     frozenset({4, 6})),
    (frozenset({1, 2, 4, 6, 7, 8, 10, 12, 15}),
     frozenset({1, 6, 7, 11, 13, 15})),
    (frozenset({1, 4, 6, 8, 12, 13}),
     frozenset({2, 4, 6, 7, 10, 11, 15})),
)


def add_minimal(bucket: set[int], candidate: int) -> bool:
    if any((old & candidate) == old for old in bucket):
        return False
    bucket.difference_update(
        old for old in tuple(bucket) if (old & candidate) == candidate
    )
    bucket.add(candidate)
    return True


def main() -> None:
    endpoint_pairs = tuple((frozenset(e), frozenset(h)) for e, h in ENDPOINTS)
    intersections = tuple(e & h for e, h in endpoint_pairs)
    carriers = sorted(
        {frozenset()} | {x for pair in endpoint_pairs for x in pair}
        | set(intersections), key=lambda x: (len(x), tuple(sorted(x)))
    )
    per_anchor = []
    for anchor in ANCHORS:
        generators = [
            frozenset(x for x in UNIVERSE
                      if ((x >> bit) & 1) == ((anchor >> bit) & 1))
            for bit in range(N)
        ]
        contexts = {carrier: set() for carrier in carriers}
        for carrier in carriers:
            for bit, generator in enumerate(generators):
                if generator <= carrier:
                    contexts[carrier].add(1 << bit)

        changed = True
        while changed:
            changed = False
            for (left, right), meet in zip(endpoint_pairs, intersections):
                for q in tuple(contexts[left]):
                    for r in tuple(contexts[right]):
                        for carrier in carriers:
                            if meet <= carrier:
                                changed |= add_minimal(contexts[carrier], q | r)

        # Check every subset of initial generators against direct closure.
        for selected in range(1 << N):
            closure = {
                carrier for carrier in carriers
                if any((selected & (1 << bit)) and generator <= carrier
                       for bit, generator in enumerate(generators))
            }
            changed = True
            while changed:
                additions = set()
                for left, right in endpoint_pairs:
                    if left in closure and right in closure:
                        meet = left & right
                        additions.update(carrier for carrier in carriers
                                         if meet <= carrier)
                updated = closure | additions
                changed = updated != closure
                closure = updated
            for carrier in carriers:
                represented = any((q & selected) == q
                                  for q in contexts[carrier])
                assert represented == (carrier in closure), (
                    anchor, selected, carrier, represented, carrier in closure
                )
        assert contexts[frozenset()]
        per_anchor.append(contexts)

    for anchor, contexts in zip(ANCHORS, per_anchor):
        root_contexts = sorted(contexts[frozenset()],
                               key=lambda x: (x.bit_count(), x))
        patterns = [tuple(i for i in range(N) if q & (1 << i))
                    for q in root_contexts]
        print(f"anchor={anchor:04b}; root_patterns={patterns}; "
              f"root_sizes={sorted({q.bit_count() for q in root_contexts})}")
    for index, meet in enumerate(intersections):
        active = [a for a, contexts in zip(ANCHORS, per_anchor)
                  if contexts[meet]]
        instances = sum(len(contexts[meet]) for contexts in per_anchor)
        print(f"rule={index}; meet={sorted(meet)}; support={active}; "
              f"minimal_context_instances={instances}")
    print("all_generator_subsets_match_direct_closure=True")


if __name__ == "__main__":
    main()
