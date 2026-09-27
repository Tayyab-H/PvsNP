"""Measure the initial-support separations forced by relay soundness.

If a low anchor's initially active carriers are a subset of a high anchor's,
monotonicity of closure forces the high anchor to derive empty too. Hence the
carrier predicates must separate every low/high pair. This script computes
the exact minimum number of distinct carrier predicates needed for that
necessary separation on saved small covers.
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


def minimum_cover_size(covers: list[int], full: int) -> tuple[int, tuple[int, ...]]:
    # Exact branch-and-bound over pair-coverage masks. Pick an uncovered pair
    # with the fewest available carrier predicates at each step.
    useful = [(i, c) for i, c in enumerate(covers) if c]
    by_pair: list[list[tuple[int, int]]] = [[] for _ in range(full.bit_length())]
    for i, cover in useful:
        pending = cover
        while pending:
            bit = pending & -pending
            by_pair[bit.bit_length() - 1].append((i, cover))
            pending ^= bit
    best = len(useful) + 1
    best_choice: tuple[int, ...] = ()
    seen: dict[int, int] = {}

    def search(covered: int, choice: tuple[int, ...]) -> None:
        nonlocal best, best_choice
        if covered == full:
            if len(choice) < best:
                best, best_choice = len(choice), choice
            return
        if len(choice) >= best or seen.get(covered, best + 1) <= len(choice):
            return
        seen[covered] = len(choice)
        missing = full ^ (full & covered)
        selected = set(choice)
        # Choose the uncovered pair with the fewest not-yet-selected covers.
        pending = missing
        chosen_options = None
        while pending:
            bit = pending & -pending
            options = [i for i, _ in by_pair[bit.bit_length() - 1]
                       if i not in selected]
            if chosen_options is None or len(options) < len(chosen_options):
                chosen_options = options
                if len(options) <= 1:
                    break
            pending ^= bit
        if not chosen_options:
            return
        for i in chosen_options:
            search(covered | covers[i], choice + (i,))

    search(0, ())
    if best > len(useful):
        raise AssertionError("carrier predicates failed to separate a low/high pair")
    return best, best_choice


def main() -> None:
    for case in CASES:
        data = runpy.run_path(str(ROOT / case), run_name="relay_data")
        n = data["N"]
        universe = frozenset(data["UNIVERSE"])
        low = tuple(data["ANCHORS"])
        high = tuple(set(range(1 << n)) - set(low))
        pairs = tuple((frozenset(e), frozenset(h))
                      for e, h in data["ENDPOINTS"])
        carriers = tuple(sorted(
            {frozenset()} | {x for pair in pairs for x in pair}
            | {e & h for e, h in pairs},
            key=lambda x: (len(x), tuple(sorted(x))),
        ))
        initial: dict[int, set[frozenset[int]]] = {}
        generators_by_anchor: dict[int, list[frozenset[int]]] = {}
        for anchor in low + high:
            generators = [
                frozenset(x for x in universe
                          if ((x >> bit) & 1) == ((anchor >> bit) & 1))
                for bit in range(n)
            ]
            generators_by_anchor[anchor] = generators
            initial[anchor] = {
                carrier for carrier in carriers
                if any(generator <= carrier for generator in generators)
            }

        pair_index = {(x, y): i for i, (x, y) in enumerate(
            itertools.product(low, high)
        )}
        covers: list[int] = []
        sizes: list[int] = []
        for carrier in carriers:
            low_support = [x for x in low if carrier in initial[x]]
            high_support = {y for y in high if carrier in initial[y]}
            mask = 0
            for x in low_support:
                for y in high:
                    if y not in high_support:
                        mask |= 1 << pair_index[x, y]
            covers.append(mask)
            sizes.append(mask.bit_count())
        full = (1 << (len(low) * len(high))) - 1
        minimum, chosen = minimum_cover_size(covers, full)
        # Upper-bound the relaxed pair-separation problem by using the 2n
        # literal slices themselves as candidate carrier predicates.
        literal_carriers = {
            (bit, value): frozenset(
                x for x in universe if ((x >> bit) & 1) == value
            )
            for bit in range(n) for value in (0, 1)
        }
        literal_covers: list[int] = []
        for literal in literal_carriers.values():
            support = {
                anchor for anchor in low + high
                if any(generator <= literal
                       for generator in generators_by_anchor[anchor])
            }
            mask = 0
            for x in low:
                if x in support:
                    for y in high:
                        if y not in support:
                            mask |= 1 << pair_index[x, y]
            literal_covers.append(mask)
        literal_minimum, _ = minimum_cover_size(literal_covers, full)
        noncontainment = all(
            not (other <= carrier)
            for (i, b), carrier in literal_carriers.items()
            for (j, c), other in literal_carriers.items()
            if (i, b) != (j, c)
        )
        print(f"{case}: rules={len(pairs)}; carriers={len(carriers)}; "
              f"low_high_pairs={len(low)*len(high)}; "
              f"max_pairs_separated_by_one={max(sizes, default=0)}; "
              f"min_carriers_for_all_pair_separation={minimum}; "
              f"chosen_carrier_sizes={[len(carriers[i]) for i in chosen]}; "
              f"literal_slice_noncontainment={noncontainment}; "
              f"min_literal_cuts={literal_minimum}")


if __name__ == "__main__":
    main()
