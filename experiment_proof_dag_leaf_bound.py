"""Exhaustively check proof-DAG certificates on the four-point filter toy."""

from itertools import chain, product


U = {"011", "101", "110", "111"}
POINTS = tuple(sorted(U))
POINT_BIT = {point: 1 << index for index, point in enumerate(POINTS)}
ALL_SETS = tuple(range(1 << len(POINTS)))
ANCHORS = tuple(a for a in map("".join, product("01", repeat=3)) if a.count("1") <= 1)


def point_mask(points):
    result = 0
    for point in points:
        result |= POINT_BIT[point]
    return result


GENERATORS = {
    anchor: tuple(
        point_mask(point for point in POINTS if point[coordinate] == anchor[coordinate])
        for coordinate in range(3)
    )
    for anchor in ANCHORS
}


def is_subset(left, right):
    return left & right == left


def close_and_trace(anchor, rules):
    """Return a first empty-rule proof, or None if empty is not derived."""
    closure = {
        candidate
        for candidate in ALL_SETS
        if any(is_subset(generator, candidate) for generator in GENERATORS[anchor])
    }
    first_time = {candidate: 0 for candidate in closure}
    fired_at = {}
    clock = 1
    root = None

    while True:
        changed = False
        for rule_index, (left, right) in enumerate(rules):
            if rule_index in fired_at:
                continue
            if left not in closure or right not in closure:
                continue
            fired_at[rule_index] = clock
            clock += 1
            intersection = left & right
            new_sets = [
                candidate
                for candidate in ALL_SETS
                if is_subset(intersection, candidate) and candidate not in closure
            ]
            for candidate in new_sets:
                closure.add(candidate)
                first_time[candidate] = fired_at[rule_index]
            if new_sets:
                changed = True
            if intersection == 0 and 0 in new_sets:
                root = rule_index
                break
        if root is not None or not changed:
            break

    if root is None:
        return None

    proof_rules = set()
    leaf_generators = set()

    def prove_rule(rule_index):
        if rule_index in proof_rules:
            return
        proof_rules.add(rule_index)
        firing_time = fired_at[rule_index]
        left, right = rules[rule_index]
        for endpoint in (left, right):
            if first_time[endpoint] == 0:
                choices = [
                    coordinate
                    for coordinate, generator in enumerate(GENERATORS[anchor])
                    if is_subset(generator, endpoint)
                ]
                assert choices, "initial upward-closure membership needs a generator"
                leaf_generators.add(choices[0])
                continue

            endpoint_time = first_time[endpoint]
            witnesses = [
                prior
                for prior, (prior_left, prior_right) in enumerate(rules)
                if prior in fired_at
                and fired_at[prior] <= endpoint_time
                and is_subset(prior_left & prior_right, endpoint)
            ]
            assert witnesses, "noninitial membership needs a fired intersection"
            witness = min(witnesses, key=lambda prior: fired_at[prior])
            assert fired_at[witness] < firing_time, "proof edges must point to earlier firings"
            prove_rule(witness)

    prove_rule(root)
    leaves = [GENERATORS[anchor][coordinate] for coordinate in sorted(leaf_generators)]
    assert leaves
    leaf_intersection = leaves[0]
    for leaf in leaves[1:]:
        leaf_intersection &= leaf

    assert leaf_intersection == 0, (
        f"leaf generators had nonempty intersection: anchor={anchor}, rules={rules}, "
        f"root={root}, leaves={leaf_generators}, intersection={leaf_intersection}"
    )
    assert len(proof_rules) <= len(rules)
    assert len(leaf_generators) <= len(proof_rules) + 1
    return len(proof_rules), len(leaf_generators)


def main():
    all_pairs = tuple(product(ALL_SETS, repeat=2))
    rule_lists = chain(((pair,) for pair in all_pairs), product(all_pairs, repeat=2))
    tested = 0
    empty_proofs = 0
    maximum_rules = 0
    maximum_leaves = 0

    for rules in rule_lists:
        for anchor in ANCHORS:
            tested += 1
            proof = close_and_trace(anchor, rules)
            if proof is None:
                continue
            empty_proofs += 1
            maximum_rules = max(maximum_rules, proof[0])
            maximum_leaves = max(maximum_leaves, proof[1])

    print(f"anchors={len(ANCHORS)}; rule_lists=65792; cases={tested}")
    print(f"empty_derivations={empty_proofs}; maximum_proof_rules={maximum_rules}; maximum_generator_leaves={maximum_leaves}")
    print("all traced certificates have empty leaf intersection and at most k+1 leaves for k rule nodes")


if __name__ == "__main__":
    main()
