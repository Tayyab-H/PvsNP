"""Counterexample-guided search for >2 covers in the 16-anchor toy.

Variables choose one 2-point minimal witness for each of 16 literal-anchored
filters on U={5-bit strings of weight 3}. For each candidate assignment,
all 1,048,576 ordered endpoint pairs are checked exactly. If two pairs cover
all anchors, a SAT clause excludes every witness assignment for which that
same pair-of-pairs still covers all anchors. A candidate with no 2-cover is
then an exact finite positive construction; solver exhaustion would instead
certify a two-pair cover for every assignment in this toy model.
"""

from __future__ import annotations

from itertools import combinations

import numpy as np
from z3 import Bool, Or, PbEq, Solver, sat


N = 5
UNIVERSE = [x for x in range(1 << N) if x.bit_count() == 3]
ANCHORS = [x for x in range(1 << N) if x.bit_count() <= 2]
U_SIZE = len(UNIVERSE)
ENDPOINT_COUNT = 1 << U_SIZE
PAIR_COUNT = ENDPOINT_COUNT * ENDPOINT_COUNT
TARGET = (1 << len(ANCHORS)) - 1


def literal_generators(anchor: int) -> list[int]:
    return [
        sum(1 << i for i, point in enumerate(UNIVERSE)
            if ((point >> bit) & 1) == ((anchor >> bit) & 1))
        for bit in range(N)
    ]


def pair_covers_anchor(anchor_index: int, witness_index: int,
                       endpoint_pair: tuple[int, int],
                       base_accept: np.ndarray,
                       candidates: list[int]) -> bool:
    left, right = endpoint_pair
    common = left & right
    witness = candidates[witness_index]
    left_ok = bool(base_accept[anchor_index, left]) or (witness & left) == witness
    right_ok = bool(base_accept[anchor_index, right]) or (witness & right) == witness
    common_ok = bool(base_accept[anchor_index, common]) or (witness & common) == witness
    return left_ok and right_ok and not common_ok


def exact_cover_codes(choice: list[int], candidates: list[int],
                      base_accept: np.ndarray, left: np.ndarray,
                      right: np.ndarray, common: np.ndarray) -> np.ndarray:
    endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    codes = np.zeros(PAIR_COUNT, dtype=np.uint16)
    for a, witness_index in enumerate(choice):
        witness = candidates[witness_index]
        accepted = base_accept[a] | (np.bitwise_and(endpoints, witness) == witness)
        covers = accepted[left] & accepted[right] & ~accepted[common]
        codes |= covers.astype(np.uint16) << a
    return codes


def find_two_covers(codes: np.ndarray, masks: np.ndarray,
                    limit: int = 16) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    best_superset = np.full(1 << len(ANCHORS), -1, dtype=np.int32)
    best_superset[masks] = masks.astype(np.int32)
    all_masks = np.arange(1 << len(ANCHORS), dtype=np.uint32)
    for bit in range(len(ANCHORS)):
        no_bit = all_masks[(all_masks & (1 << bit)) == 0]
        missing = best_superset[no_bit]
        sources = best_superset[no_bit | (1 << bit)]
        best_superset[no_bit] = np.where(missing >= 0, missing, sources)

    unique_codes, first_indices = np.unique(codes, return_index=True)
    examples = {
        int(code): (int(index) // ENDPOINT_COUNT, int(index) % ENDPOINT_COUNT)
        for code, index in zip(unique_codes, first_indices) if int(code) != 0
    }
    ordered_masks = sorted((int(mask) for mask in masks), key=lambda x: (x.bit_count(), x))
    found: list[tuple[tuple[int, int], tuple[int, int]]] = []
    seen: set[tuple[int, int]] = set()
    for first in ordered_masks:
        first = int(first)
        need = TARGET ^ first
        second = int(best_superset[need])
        if second < 0:
            continue
        key = tuple(sorted((first, second)))
        if key in seen:
            continue
        seen.add(key)
        found.append((examples[first], examples[second]))
        if len(found) >= limit:
            break
    return found


def find_three_cover(masks: np.ndarray) -> tuple[int, int, int] | None:
    pair_unions = np.unique(np.bitwise_or(masks[:, None], masks[None, :]))
    present = np.zeros(1 << len(ANCHORS), dtype=np.bool_)
    present[masks] = True
    has_superset = present.copy()
    all_masks = np.arange(1 << len(ANCHORS), dtype=np.uint32)
    for bit in range(len(ANCHORS)):
        no_bit = all_masks[(all_masks & (1 << bit)) == 0]
        has_superset[no_bit] |= has_superset[no_bit | (1 << bit)]
    for raw in pair_unions:
        first_two = int(raw)
        need = TARGET ^ first_two
        if has_superset[need]:
            a, b = first_two, None
            for x in masks:
                for y in masks:
                    if (int(x) | int(y)) == first_two:
                        a, b = int(x), int(y)
                        break
                if b is not None:
                    break
            third = next(int(mask) for mask in masks if (int(mask) & need) == need)
            assert b is not None
            return a, b, third
    return None


def endpoint_pair_for_code(codes: np.ndarray, code: int) -> tuple[int, int]:
    flat = int(np.argmax(codes == code))
    return flat // ENDPOINT_COUNT, flat % ENDPOINT_COUNT


def point_list(mask: int) -> list[int]:
    return [UNIVERSE[i] for i in range(U_SIZE) if mask >> i & 1]


def main(max_iterations: int = 1000) -> None:
    endpoints = np.arange(ENDPOINT_COUNT, dtype=np.uint16)
    left = np.repeat(endpoints, ENDPOINT_COUNT)
    right = np.tile(endpoints, ENDPOINT_COUNT)
    common = np.bitwise_and(left, right)
    candidates = [sum(1 << i for i in pair)
                  for pair in combinations(range(U_SIZE), 2)]

    base_accept = np.zeros((len(ANCHORS), ENDPOINT_COUNT), dtype=np.bool_)
    for a, anchor in enumerate(ANCHORS):
        for literal in literal_generators(anchor):
            base_accept[a] |= (np.bitwise_and(endpoints, literal) == literal)

    choice_vars = [
        [Bool(f"w_{a}_{c}") for c in range(len(candidates))]
        for a in range(len(ANCHORS))
    ]
    solver = Solver()
    for row in choice_vars:
        solver.add(PbEq([(var, 1) for var in row], 1))

    cuts = 0
    seen_clauses: set[tuple[int, ...]] = set()
    for iteration in range(max_iterations + 1):
        status = solver.check()
        if status != sat:
            print(
                f"N={N}; |U|={U_SIZE}; anchors={len(ANCHORS)}; "
                f"candidate_witnesses_per_anchor={len(candidates)}; "
                f"blocking_clauses={cuts}; solver_status={status}; "
                "all assignments are certified to have a two-pair cover"
            )
            return
        model = solver.model()
        choice = [next(c for c, var in enumerate(row) if model.eval(var, model_completion=True))
                  for row in choice_vars]
        codes = exact_cover_codes(choice, candidates, base_accept, left, right, common)
        masks = np.unique(codes)
        masks = masks[masks != 0]
        two_pairs = find_two_covers(codes, masks)
        if not two_pairs:
            triple = find_three_cover(masks)
            selected = [
                point_list(candidates[c]) for c in choice
            ]
            print(
                f"N={N}; |U|={U_SIZE}; anchors={len(ANCHORS)}; "
                f"blocking_clauses={cuts}; no_two_pair_cover=PASS; "
                f"three_pair_cover={triple is not None}; "
                f"distinct_pair_masks={len(masks)}; witnesses={selected}"
            )
            if triple is not None:
                for code in triple:
                    e, h = endpoint_pair_for_code(codes, code)
                    print(
                        f"  E={point_list(e)}; H={point_list(h)}; "
                        f"covered={[ANCHORS[a] for a in range(len(ANCHORS)) if code >> a & 1]}"
                    )
            return

        new_clauses = 0
        last_codes = None
        for endpoints_to_block in two_pairs:
            clause_items = []
            for a, row in enumerate(choice_vars):
                for c, var in enumerate(row):
                    if not pair_covers_anchor(a, c, endpoints_to_block[0], base_accept, candidates) \
                            and not pair_covers_anchor(a, c, endpoints_to_block[1], base_accept, candidates):
                        clause_items.append((a * len(candidates) + c, var))
            if not clause_items:
                print(
                    f"universal_two_pair_certificate_found_at_iteration={iteration}; "
                    f"all assignments preserve a two-pair cover"
                )
                return
            clause_key = tuple(sorted(index for index, _ in clause_items))
            if clause_key in seen_clauses:
                continue
            seen_clauses.add(clause_key)
            solver.add(Or(*(var for _, var in clause_items)))
            new_clauses += 1
            last_codes = tuple(endpoints_to_block)
        if new_clauses == 0:
            raise AssertionError("A returned two-cover generated no new clause")
        cuts += new_clauses
        if (iteration + 1) % 10 == 0:
            print(
                f"cegis_iterations={iteration + 1}; blocking_clauses={cuts}; "
                f"last_endpoint_pairs={last_codes}",
                flush=True,
            )

    print(
        f"search_limit_reached={max_iterations}; assignments remain; "
        "this is not a proof of impossibility"
    )


if __name__ == "__main__":
    main()
