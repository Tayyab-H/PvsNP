"""Build a linear-rule relay for parity via a monotone dual-rail circuit.

The high universe is even-parity strings and the accepted anchors are
odd-parity strings.  A monotone circuit over paired literal inputs computes
odd parity.  Each AND gate becomes one intersection rule; each OR gate becomes
two rules using the always-active top carrier.  The test checks full closure
and extracts the exponentially large high-free seed frontier.
"""

from __future__ import annotations

from itertools import product

from experiment_relay_proof_contexts import direct_carrier_closure
from experiment_relay_context_normal_form import add_minimal, compatible_union


def main() -> None:
    for n in range(2, 7):
        all_points = frozenset(range(1 << n))
        high = frozenset(x for x in all_points if x.bit_count() % 2 == 0)
        low = all_points - high
        nodes: list[tuple[str, int, int] | tuple[str, int, int]] = []
        literals = {}
        for i in range(n):
            for b in (0, 1):
                literals[i, b] = len(nodes)
                nodes.append(("lit", i, b))

        def gate(op: str, a: int, b: int) -> int:
            nodes.append((op, a, b))
            return len(nodes) - 1

        # Maintain positive and negative rails for parity on each prefix.
        positive, negative = literals[0, 1], literals[0, 0]
        for i in range(1, n):
            x0, x1 = literals[i, 0], literals[i, 1]
            p0, p1 = gate("and", positive, x0), gate("and", negative, x1)
            n0, n1 = gate("and", positive, x1), gate("and", negative, x0)
            positive, negative = gate("or", p0, p1), gate("or", n0, n1)

        carriers: list[frozenset[int]] = []
        for node in nodes:
            op, a, b = node
            if op == "lit":
                carriers.append(frozenset(
                    x for x in high if ((x >> a) & 1) == b
                ))
            elif op == "and":
                carriers.append(carriers[a] & carriers[b])
            else:
                carriers.append(carriers[a] | carriers[b])

        pairs = []
        for node_id, (op, a, b) in enumerate(nodes):
            if op == "and":
                pairs.append((carriers[a], carriers[b]))
            elif op == "or":
                pairs.append((carriers[a], high))
                pairs.append((carriers[b], high))
        # Ensure the final output carrier is a named tracked endpoint.
        pairs.append((carriers[positive], high))
        m = len(pairs)
        endpoints = tuple(side for pair in pairs for side in pair)
        all_carriers = sorted(
            {frozenset()} | set(carriers) | set(endpoints)
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
                generators, tuple(pairs), all_carriers, (1 << n) - 1
            )
            assert (frozenset() in closure) == (anchor in low), (n, anchor)

        # First-seed core contexts, represented as minimal antichains.
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
        terminal = set()
        for r, (left, right) in enumerate(pairs):
            if left & right:
                continue
            for p in contexts[2 * r]:
                for q in contexts[2 * r + 1]:
                    merged = compatible_union(p, q)
                    if merged is not None:
                        add_minimal(terminal, merged)

        assert len(terminal) == 1 << (n - 1), (n, len(terminal))
        assert {len(term) for term in terminal} == {n}, (n, terminal)
        for term in terminal:
            assert not any(
                all(((z >> i) & 1) == b for i, b in term) for z in high
            ), (n, term)
        for anchor in range(1 << n):
            term_accept = any(
                all(((anchor >> i) & 1) == b for i, b in term)
                for term in terminal
            )
            assert term_accept == (anchor in low), (n, anchor)

        print(
            f"N={n}; relay_rules={m}; odd_anchors={len(low)}; "
            f"minimal_seed_cubes={len(terminal)}=2^{n-1}; "
            f"cube_width={n}; full_closure_all_{1<<n}_anchors=True"
        )


if __name__ == "__main__":
    main()
