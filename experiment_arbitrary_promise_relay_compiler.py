"""Stress-test circuit-to-relay compilation on arbitrary finite promises.

Unlike the parity demo, this samples sparse high sets too, so some literal
slices can be empty.  It checks only the promise obligations: accept Y and
reject Z; values outside Y union Z are unconstrained.
"""

from __future__ import annotations

import random

from experiment_relay_proof_contexts import direct_carrier_closure


def compile_circuit(n: int, high: frozenset[int], gates: list[tuple[str, int, int]],
                    output: int) -> tuple[tuple[frozenset[int], frozenset[int]], ...]:
    """Compile an AND/OR/NOT circuit (input nodes 0..n-1) into relay pairs."""
    carrier: list[frozenset[int]] = []
    dual_nodes: list[tuple[str, int, int] | tuple[str, int]] = []
    dual_index: list[tuple[int, int]] = []

    # Each input has positive and negative dual-rail signals.
    for i in range(n):
        pos = frozenset(z for z in high if (z >> i) & 1)
        neg = frozenset(z for z in high if not ((z >> i) & 1))
        p_id, q_id = len(carrier), len(carrier) + 1
        carrier.extend((pos, neg))
        dual_nodes.extend((("input", i), ("input", i)))
        dual_index.append((p_id, q_id))

    def add(op: str, a: int, b: int | None = None) -> int:
        node = len(carrier)
        if op == "and":
            assert b is not None
            carrier.append(carrier[a] & carrier[b])
            dual_nodes.append((op, a, b))
        elif op == "or":
            assert b is not None
            carrier.append(carrier[a] | carrier[b])
            dual_nodes.append((op, a, b))
        else:
            raise ValueError(op)
        return node

    # The two entries at each original wire are its positive and negative rails.
    rails = list(dual_index)
    for op, a, b in gates:
        ap, an = rails[a]
        if op == "not":
            rails.append((an, ap))
            continue
        bp, bn = rails[b]
        if op == "and":
            rails.append((add("and", ap, bp), add("or", an, bn)))
        elif op == "or":
            rails.append((add("or", ap, bp), add("and", an, bn)))
        else:
            raise ValueError(op)

    out, _ = rails[output]
    pairs: list[tuple[frozenset[int], frozenset[int]]] = []
    for node, desc in enumerate(dual_nodes):
        op = desc[0]
        if op == "and":
            _, a, b = desc
            pairs.append((carrier[a], carrier[b]))
        elif op == "or":
            _, a, b = desc
            pairs.extend(((carrier[a], high), (carrier[b], high)))
    # This is the terminal empty-carrier test on the high promise.
    pairs.append((carrier[out], high))
    return tuple(pairs)


def circuit_value(n: int, gates: list[tuple[str, int, int]], output: int,
                  x: int) -> bool:
    values = [bool((x >> i) & 1) for i in range(n)]
    for op, a, b in gates:
        if op == "not":
            values.append(not values[a])
        elif op == "and":
            values.append(values[a] and values[b])
        else:
            values.append(values[a] or values[b])
    return values[output]


def main() -> None:
    rng = random.Random(20260924)
    checked = 0
    sparse_cases = 0
    for n in range(2, 6):
        for _ in range(150):
            gates: list[tuple[str, int, int]] = []
            for _ in range(rng.randrange(1, 9)):
                upper = n + len(gates)
                op = rng.choice(("and", "or", "not"))
                a = rng.randrange(upper)
                b = rng.randrange(upper) if op != "not" else 0
                gates.append((op, a, b))
            output = n + len(gates) - 1
            truth = {x for x in range(1 << n)
                     if circuit_value(n, gates, output, x)}
            if not truth or truth == set(range(1 << n)):
                continue
            other = set(range(1 << n)) - truth
            low = frozenset(x for x in truth if rng.random() < 0.65)
            high = frozenset(x for x in other if rng.random() < 0.65)
            if not low:
                low = frozenset((rng.choice(tuple(truth)),))
            if not high:
                high = frozenset((rng.choice(tuple(other)),))
            pairs = compile_circuit(n, high, gates, output)
            endpoints = tuple(side for pair in pairs for side in pair)
            meets = tuple(left & right for left, right in pairs)
            all_carriers = tuple(dict.fromkeys((frozenset(), *endpoints, *meets)))
            for anchor in low | high:
                generators = [
                    frozenset(z for z in high
                              if ((z >> i) & 1) == ((anchor >> i) & 1))
                    for i in range(n)
                ]
                closure = direct_carrier_closure(
                    generators, pairs, all_carriers, (1 << n) - 1
                )
                accepts = frozenset() in closure
                assert accepts == (anchor in low), (
                    n, gates, output, low, high, anchor, accepts
                )
            if any(not any(((z >> i) & 1) == b for z in high)
                   for i in range(n) for b in (0, 1)):
                sparse_cases += 1
            checked += 1
    print(f"promise_instances={checked}; sparse_empty_slice_instances={sparse_cases}; exact=True")


if __name__ == "__main__":
    main()
