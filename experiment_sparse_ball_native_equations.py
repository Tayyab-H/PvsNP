"""Rewrite the five-rule witness as anchor-dependent Boolean equations."""

from __future__ import annotations

import runpy


data = runpy.run_path("experiment_sparse_ball_native_n5_witness.py")
n = data["N"]
universe = tuple(data["UNIVERSE"])
anchors = tuple(data["ANCHORS"])
pairs = tuple((frozenset(e), frozenset(h)) for e, h in data["ENDPOINTS"])
meets = tuple(e & h for e, h in pairs)


def literal_support(endpoint: frozenset[int]) -> list[str]:
    return [
        f"x{i}={b}"
        for i in range(n)
        for b in (0, 1)
        if {x for x in universe if ((x >> i) & 1) == b} <= endpoint
    ]


def dependencies(endpoint: frozenset[int]) -> list[int]:
    return [j for j, meet in enumerate(meets) if meet <= endpoint]


for j, (left, right) in enumerate(pairs):
    print(
        f"rule={j}; meet={sorted(meets[j])}; disjoint={not meets[j]}; "
        f"E_literals={literal_support(left)}; E_from_rules={dependencies(left)}; "
        f"H_literals={literal_support(right)}; H_from_rules={dependencies(right)}"
    )

print("anchor truth-set profiles over the full Boolean cube:")
for j, (left, right) in enumerate(pairs):
    fired_on = []
    for anchor in range(1 << n):
        flags = [False] * len(pairs)

        def base(endpoint: frozenset[int]) -> bool:
            return any(
                {x for x in universe if ((x >> i) & 1) == ((anchor >> i) & 1)}
                <= endpoint
                for i in range(n)
            )

        for _ in range(len(pairs)):
            old = flags[:]
            for r, (e_set, h_set) in enumerate(pairs):
                active_e = base(e_set) or any(
                    old[k] and meets[k] <= e_set for k in range(len(pairs))
                )
                active_h = base(h_set) or any(
                    old[k] and meets[k] <= h_set for k in range(len(pairs))
                )
                flags[r] = flags[r] or (active_e and active_h)
        if flags[j]:
            fired_on.append(anchor)
    weight_profile = {
        w: sum(x.bit_count() == w for x in fired_on) for w in range(n + 1)
    }
    if not meets[j]:
        assert set(fired_on) == set(anchors), (
            "disjoint rule must accept exactly low anchors",
            fired_on,
            anchors,
        )
    print(f"  rule={j}; fires={len(fired_on)}/32; weight_profile={weight_profile}; "
          f"anchors={fired_on}")
print("equation: fire_j(a) = (E_literal_j(a) OR predecessor fires) AND "
      "(H_literal_j(a) OR predecessor fires); solve by least fixed point")

print("single-rule ablations:")
for removed in range(len(pairs)):
    remaining = tuple(pair for j, pair in enumerate(pairs) if j != removed)
    remaining_meets = tuple(e & h for e, h in remaining)
    carriers = sorted(
        {frozenset()} | {x for pair in remaining for x in pair}
        | set(remaining_meets),
        key=lambda x: (len(x), tuple(sorted(x))),
    )
    missing = []
    for anchor in anchors:
        generators = [
            {x for x in universe if ((x >> i) & 1) == ((anchor >> i) & 1)}
            for i in range(n)
        ]
        closure = {
            carrier for carrier in carriers
            if any(generator <= carrier for generator in generators)
        }
        changed = True
        while changed:
            changed = False
            for (left, right), meet in zip(remaining, remaining_meets):
                if left in closure and right in closure:
                    for carrier in carriers:
                        if meet <= carrier and carrier not in closure:
                            closure.add(carrier)
                            changed = True
        if frozenset() not in closure:
            missing.append(anchor)
    print(f"  removed_rule={removed}; uncovered_anchors={missing}")
