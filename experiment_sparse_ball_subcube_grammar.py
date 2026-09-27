"""Compare relay-generated proof contexts with all high-free subcubes."""

from __future__ import annotations

import runpy
import re
from pathlib import Path

from experiment_relay_proof_contexts import add_minimal, direct_carrier_closure


ROOT = Path(__file__).resolve().parent
CASES = (
    "weight_two_ball_n4_m2.txt",
    "experiment_weight_one_anchor_cover4.py",
    "experiment_weight_one_anchor_cover5_six_rules.py",
    "experiment_sparse_ball_native_n5_witness.py",
    "experiment_sparse_ball_canonical_selector_witness.py",
    "experiment_sparse_ball_multiple_disjoint_witness.py",
)


def signed_context(anchor: int, coordinate_mask: int, n: int) -> int:
    """Encode selected literals as bits (2*i + anchor[i])."""
    out = 0
    for i in range(n):
        if (coordinate_mask >> i) & 1:
            out |= 1 << (2 * i + ((anchor >> i) & 1))
    return out


def context_support(context: int, anchors: set[int], n: int) -> set[int]:
    fixed = {
        i: (context >> (2 * i + 1)) & 1
        for i in range(n)
        if ((context >> (2 * i)) | (context >> (2 * i + 1))) & 1
    }
    assert all(not (((context >> (2 * i)) & 1) and
                    ((context >> (2 * i + 1)) & 1)) for i in range(n))
    return {
        a for a in anchors
        if all(((a >> i) & 1) == bit for i, bit in fixed.items())
    }


def high_free_contexts(n: int, high: set[int], low: set[int]):
    result = []
    # Each coordinate is unset, fixed to 0, or fixed to 1.
    for code in range(3 ** n):
        q, context = code, 0
        for i in range(n):
            digit, q = q % 3, q // 3
            if digit:
                context |= 1 << (2 * i + digit - 1)
        support = context_support(context, low | high, n)
        if support and not (support & high):
            result.append((context, support & low))
    return result


def minimum_cover(contexts: list[tuple[int, set[int]]], low: set[int]) -> int:
    """Exact branch-and-bound set cover on the tiny n=5 instance."""
    by_anchor = {
        a: [i for i, (_, s) in enumerate(contexts) if a in s]
        for a in low
    }
    assert all(by_anchor.values())
    best = len(low) + 1

    def visit(covered: frozenset[int], chosen: int) -> None:
        nonlocal best
        if covered >= low:
            best = min(best, chosen)
            return
        if chosen >= best:
            return
        remaining = low - set(covered)
        a = min(remaining, key=lambda x: sum(
            bool(contexts[i][1] - set(covered)) for i in by_anchor[x]
        ))
        options = sorted(
            by_anchor[a],
            key=lambda i: len(contexts[i][1] - set(covered)),
            reverse=True,
        )
        for i in options:
            gain = contexts[i][1] - set(covered)
            if gain:
                visit(frozenset(set(covered) | contexts[i][1]), chosen + 1)

    visit(frozenset(), 0)
    return best


def trace_case(script_name: str) -> None:
    if script_name.endswith(".txt"):
        rows = (ROOT / script_name).read_text(encoding="utf-8").splitlines()
        n = 4
        low = {x for x in range(1 << n) if x.bit_count() <= 2}
        high = set(range(1 << n)) - low
        pairs = tuple(
            (frozenset(map(int, e.split(", ")) if e else ()),
             frozenset(map(int, h.split(", ")) if h else ()))
            for e, h in re.findall(r"rule\d+: E=\[(.*?)\]; H=\[(.*?)\]", "\n".join(rows))
        )
    else:
        data = runpy.run_path(str(ROOT / script_name), run_name="relay_data")
        n = data["N"]
        low = set(data["ANCHORS"])
        high = set(data["UNIVERSE"])
        pairs = tuple((frozenset(e), frozenset(h)) for e, h in data["ENDPOINTS"])
    points = low | high
    meets = tuple(e & h for e, h in pairs)
    seeds = [i for i, meet in enumerate(meets) if not meet]
    core = tuple(pair for i, pair in enumerate(pairs) if i not in seeds)
    core_meets = tuple(meets[i] for i in range(len(pairs)) if i not in seeds)
    carriers = sorted(
        {frozenset()} | {x for pair in pairs for x in pair} | set(meets),
        key=lambda x: (len(x), tuple(sorted(x))),
    )

    for anchor in sorted(points):
        generators = [
            frozenset(x for x in high
                      if ((x >> bit) & 1) == ((anchor >> bit) & 1))
            for bit in range(n)
        ]
        direct = direct_carrier_closure(
            generators, pairs, carriers, (1 << n) - 1
        )
        assert (frozenset() in direct) == (anchor in low), (
            script_name, anchor, anchor in low
        )

    # The static high-free cylinder family is the benchmark target.
    all_hf = high_free_contexts(n, high, low)
    cover_number = minimum_cover(all_hf, low)
    zero_slices = [
        {x for x in high if ((x >> i) & 1) == 0} for i in range(n)
    ]
    zero_overlap_edges = [
        (i, j) for i in range(n) for j in range(i + 1, n)
        if zero_slices[i] & zero_slices[j]
    ]
    print(f"{script_name}: n={n}; low={len(low)}; high={len(high)}; "
          f"high_free_cylinders={len(all_hf)}; min_cylinder_cover={cover_number}; "
          f"zero_slice_overlap_edges={len(zero_overlap_edges)}/{n*(n-1)//2}")

    generated_by_seed: dict[int, set[int]] = {seed: set() for seed in seeds}
    top_layer_splits: dict[int, set[tuple[int, int, bool, bool]]] = {
        seed: set() for seed in seeds
    }
    top_weight = max(a.bit_count() for a in low)
    top_context_width = n - top_weight
    for anchor in sorted(points):
        generators = [
            frozenset(x for x in high
                      if ((x >> bit) & 1) == ((anchor >> bit) & 1))
            for bit in range(n)
        ]
        contexts = {carrier: set() for carrier in carriers}
        base_contexts = {carrier: set() for carrier in carriers}
        for carrier in carriers:
            for bit, generator in enumerate(generators):
                if generator <= carrier:
                    contexts[carrier].add(1 << bit)
                    base_contexts[carrier].add(1 << bit)
        changed = True
        while changed:
            changed = False
            for (left, right), meet in zip(core, core_meets):
                for left_context in tuple(contexts[left]):
                    for right_context in tuple(contexts[right]):
                        merged = left_context | right_context
                        for carrier in carriers:
                            if meet <= carrier:
                                changed |= add_minimal(contexts[carrier], merged)
        for seed in seeds:
            left, right = pairs[seed]
            for lc in contexts[left]:
                for rc in contexts[right]:
                    if (anchor in low and anchor.bit_count() == top_weight
                            and (lc | rc).bit_count() == top_context_width):
                        expected_zeros = ((1 << n) - 1) ^ anchor
                        assert (lc | rc) == expected_zeros, (
                            script_name, seed, anchor, lc, rc
                        )
                        top_layer_splits[seed].add((
                            lc.bit_count(), rc.bit_count(),
                            lc not in base_contexts[left],
                            rc not in base_contexts[right],
                        ))
                    signed = signed_context(anchor, lc | rc, n)
                    support = context_support(signed, points, n)
                    assert not (support & high), (script_name, seed, anchor, signed)
                    if anchor in low:
                        generated_by_seed[seed].add(signed)

    generated_union = set().union(*generated_by_seed.values())
    supports = [(ctx, context_support(ctx, low, n)) for ctx in generated_union]
    assert set().union(*(s for _, s in supports)) >= low
    print(f"  generated_signed_contexts={len(generated_union)}; "
          f"contexts_that_cover_low={sum(bool(s) for _, s in supports)}")
    for seed, contexts in generated_by_seed.items():
        cover = [ctx for ctx in contexts if context_support(ctx, low, n)]
        seed_support = set().union(*(context_support(ctx, low, n) for ctx in cover))
        left, right = pairs[seed]
        left_zero = [i for i, g in enumerate(zero_slices) if g <= left]
        right_zero = [i for i, g in enumerate(zero_slices) if g <= right]
        assert not any((i, j) in zero_overlap_edges
                       or (j, i) in zero_overlap_edges
                       for i in left_zero for j in right_zero)
        print(f"  seed={seed}; signed_contexts={len(cover)}; "
              f"low_union={len(seed_support)}/{len(low)}; "
              f"base_zero_literals=({left_zero},{right_zero}); "
              f"top_layer_split_patterns={sorted(top_layer_splits[seed])}")
    if n <= 6:
        print("  smallest high-free contexts:", sorted(
            (mask.bit_count(), mask) for mask, _ in all_hf
        )[:8])


def main() -> None:
    for case in CASES:
        trace_case(case)


if __name__ == "__main__":
    main()
