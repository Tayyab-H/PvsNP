"""Exact trace-geometry audit for maximal four-variable formula selectors.

Enumerates all De Morgan formulas with at most four AND/OR gates, identifies
high truth tables whose minimum exclusion set has eight rows, and measures how
many eight-bit labelings are realized by the low class on each selected row
set. This is a finite formula experiment, not a circuit lower bound.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

import numpy as np

from experiment_formula_high_selector_toy import exact_formula_classes


def project_tables(tables: np.ndarray, rows: tuple[int, ...]) -> np.ndarray:
    out = np.zeros(len(tables), dtype=np.uint16)
    for j, row in enumerate(rows):
        out |= (((tables >> row) & 1).astype(np.uint16) << j)
    return out


def formula_expressions(n: int, max_gates: int) -> list[dict[int, str]]:
    """Return one expression for every exactly-gate-count truth table."""
    domain = 1 << n
    full = (1 << domain) - 1
    leaves = {0: "0", full: "1"}
    for i in range(n):
        positive = sum(1 << x for x in range(domain) if (x >> i) & 1)
        leaves[positive] = f"x{i}"
        leaves[full ^ positive] = f"~x{i}"
    layers = [leaves]
    for gates in range(1, max_gates + 1):
        expressions: dict[int, str] = {}
        for left_gates in range(gates):
            right_gates = gates - 1 - left_gates
            for left, left_expr in layers[left_gates].items():
                for right, right_expr in layers[right_gates].items():
                    expressions.setdefault(left & right, f"({left_expr}&{right_expr})")
                    expressions.setdefault(left | right, f"({left_expr}|{right_expr})")
        layers.append(expressions)
    return layers


def main() -> None:
    n = 4
    row_count = 1 << n
    cutoff = 4
    exact = exact_formula_classes(n, cutoff)
    low_set = set().union(*exact)
    low = np.fromiter(sorted(low_set), dtype=np.uint16)
    all_tables = np.arange(1 << row_count, dtype=np.uint16)
    is_low = np.zeros(1 << row_count, dtype=bool)
    is_low[low] = True
    sizes = np.zeros(1 << row_count, dtype=np.uint8)
    chosen_masks = np.zeros(1 << row_count, dtype=np.uint16)

    for q in range(1, row_count + 1):
        for rows in combinations(range(row_count), q):
            low_patterns = project_tables(low, rows)
            realized = np.zeros(1 << q, dtype=bool)
            realized[low_patterns] = True
            patterns = project_tables(all_tables, rows)
            new = (sizes == 0) & (~is_low) & (~realized[patterns])
            sizes[new] = q
            chosen_masks[new] = sum(1 << row for row in rows)
        if np.all(sizes[~is_low]):
            break

    high = ~is_low
    max_size = int(sizes[high].max())
    max_tables = np.flatnonzero(high & (sizes == max_size))
    if max_size != 8:
        raise AssertionError(f"expected eight-row maximum, got {max_size}")

    by_q: dict[int, list[int]] = {}
    for table in max_tables:
        qmask = int(chosen_masks[table])
        by_q.setdefault(qmask, []).append(int(table))

    holes_by_distance: Counter[int] = Counter()
    hole_count_histogram: Counter[int] = Counter()
    max_distance_histogram: Counter[int] = Counter()
    critical_partials = set()
    for qmask, tables in by_q.items():
        rows = tuple(i for i in range(row_count) if (qmask >> i) & 1)
        low_patterns = set(map(int, project_tables(low, rows)))
        all_patterns = set(range(1 << len(rows)))
        holes = all_patterns - low_patterns
        if not holes:
            raise AssertionError("selected Q must have at least one excluded pattern")
        hole_count_histogram[len(holes)] += 1
        for table in tables:
            target = int(project_tables(np.array([table], dtype=np.uint16), rows)[0])
            critical_partials.add((qmask, target))
            if target not in holes:
                raise AssertionError("the high table's restriction must be a hole")
            distances = Counter((target ^ p).bit_count() for p in holes)
            neighbor_count = sum(
                1 for bit in range(len(rows)) if target ^ (1 << bit) in low_patterns
            )
            if neighbor_count != len(rows):
                raise AssertionError("minimal selector must realize every private neighbor")
            holes_by_distance.update(distances)
            max_distance_histogram[max(distances)] += 1

    # For comparison, scan every eight-row set and find how close its trace is
    # to realizing every labeling. This is only 12,870 projections of 3,302
    # functions and is small enough to do exactly.
    all_q_holes: Counter[int] = Counter()
    min_holes = 1 << 8
    min_hole_qs: list[tuple[int, ...]] = []
    for rows in combinations(range(row_count), 8):
        patterns = set(map(int, project_tables(low, rows)))
        holes = (1 << 8) - len(patterns)
        all_q_holes[holes] += 1
        if holes < min_holes:
            min_holes = holes
            min_hole_qs = [rows]
        elif holes == min_holes:
            min_hole_qs.append(rows)

    affine_best_q_count = 0
    for rows in min_hole_qs:
        traces = set(map(int, project_tables(low, rows)))
        holes = set(range(1 << len(rows))) - traces
        differences = {min(holes) ^ hole for hole in holes}
        weights = Counter(word.bit_count() for word in differences)
        if (
            len(differences) == 8
            and all((a ^ b) in differences for a in differences for b in differences)
            and weights == Counter({0: 1, 4: 6, 8: 1})
        ):
            affine_best_q_count += 1

    # Among the row sets with the fewest omitted patterns, test every omitted
    # labeling for the defining criticality condition: deleting any one row
    # must expose a low-formula completion.
    best_q_critical: list[tuple[tuple[int, ...], int]] = []
    best_q_hole_distances: Counter[int] = Counter()
    for rows in min_hole_qs:
        low_patterns = set(map(int, project_tables(low, rows)))
        holes = set(range(1 << len(rows))) - low_patterns
        for target in holes:
            all_deletions_realizable = True
            for deleted in range(len(rows)):
                shorter_rows = rows[:deleted] + rows[deleted + 1:]
                shorter_target = (target & ((1 << deleted) - 1)) | (
                    (target >> (deleted + 1)) << deleted
                )
                shorter_patterns = set(map(int, project_tables(low, shorter_rows)))
                if shorter_target not in shorter_patterns:
                    all_deletions_realizable = False
                    break
            if all_deletions_realizable:
                best_q_critical.append((rows, target))
                best_q_hole_distances.update(
                    (target ^ other).bit_count() for other in holes
                )

    # A partial table's own one-row minimality does not imply that an arbitrary
    # total completion has globally minimum selector size: other rows may
    # provide a different, smaller exclusion set. Exhaust all completions to
    # test whether these best-trace partials admit a genuinely maximum-tau
    # total extension.
    extension_max_tau_histogram: Counter[int] = Counter()
    extension_min_tau_histogram: Counter[int] = Counter()
    partials_with_max_extension = 0
    first_max_extension: tuple[tuple[int, ...], int, int, int] | None = None
    for rows, target in best_q_critical:
        free_rows = tuple(row for row in range(row_count) if row not in rows)
        base = sum(((target >> j) & 1) << row for j, row in enumerate(rows))
        completion_taus = []
        for assignment in range(1 << len(free_rows)):
            table = base | sum(
                ((assignment >> j) & 1) << row
                for j, row in enumerate(free_rows)
            )
            completion_taus.append(int(sizes[table]))
        local_max = max(completion_taus)
        local_min = min(completion_taus)
        extension_max_tau_histogram[local_max] += 1
        extension_min_tau_histogram[local_min] += 1
        if local_max == max_size:
            partials_with_max_extension += 1
            if first_max_extension is None:
                for assignment in range(1 << len(free_rows)):
                    table = base | sum(
                        ((assignment >> j) & 1) << row
                        for j, row in enumerate(free_rows)
                    )
                    if int(sizes[table]) == max_size:
                        first_max_extension = (rows, target, table, int(sizes[table]))
                        break

    print(f"n={n}; formula_cutoff={cutoff}; low_functions={len(low_set)}")
    print(
        f"maximum_selector_rows={max_size}; high_tables={len(max_tables)}; "
        f"distinct_selected_Q={len(by_q)}; distinct_critical_partials={len(critical_partials)}"
    )
    print(f"selected_Q_hole_count_histogram={dict(sorted(hole_count_histogram.items()))}")
    print(f"selected_Q_target_hole_distance_histogram={dict(sorted(holes_by_distance.items()))}")
    print(f"selected_Q_max_hole_radius_histogram={dict(sorted(max_distance_histogram.items()))}")
    print(f"all_8_row_Q_hole_count_histogram={dict(sorted(all_q_holes.items()))}")
    print(f"best_8_row_Q_hole_count={min_holes}; number_of_Q={len(min_hole_qs)}")
    print(f"best_Qs_with_affine_[8,3,4]_code_holes={affine_best_q_count}")
    print(f"example_best_Q={min_hole_qs[0]}")
    print(
        f"best_Q_critical_partials={len(best_q_critical)}; "
        f"best_Qs_with_critical_partial={len({q for q, _ in best_q_critical})}"
    )
    print(
        f"best_Q_critical_target_hole_distance_histogram="
        f"{dict(sorted(best_q_hole_distances.items()))}"
    )
    print(
        f"critical_partial_max_extension_tau_histogram="
        f"{dict(sorted(extension_max_tau_histogram.items()))}"
    )
    print(
        f"critical_partial_min_extension_tau_histogram="
        f"{dict(sorted(extension_min_tau_histogram.items()))}"
    )
    print(f"critical_partials_with_tau_{max_size}_extension={partials_with_max_extension}")
    if first_max_extension:
        rows, target, table, tau = first_max_extension
        low_patterns = set(map(int, project_tables(low, rows)))
        holes = set(range(1 << len(rows))) - low_patterns
        differences = {target ^ hole for hole in holes}
        difference_weights = Counter(word.bit_count() for word in differences)
        is_affine_linear_coset = (
            len(differences) == 8
            and all((a ^ b) in differences for a in differences for b in differences)
            and difference_weights == Counter({0: 1, 4: 6, 8: 1})
        )
        print(
            f"example_best_Q_max_extension=Q{rows}; target=0x{target:02x}; "
            f"total_table=0x{table:04x}; tau={tau}; "
            f"Q_is_even_parity_inputs={sum(row.bit_count() % 2 == 0 for row in rows) == 8}"
        )
        if table == 0x8181:
            print(
                "  total_function_formula=((~x0&~x1&~x2)|(x0&x1&x2)); "
                "formula_gates=5; x3 is unused"
            )
        print(
            f"example_hole_patterns={[f'0x{x:02x}' for x in sorted(holes)]}; "
            f"hole_distance_from_target="
            f"{dict(sorted(Counter((target ^ h).bit_count() for h in holes).items()))}; "
            f"affine_[8,3,4]_linear_code_coset={is_affine_linear_coset}; "
            f"difference_codeword_weights={dict(sorted(difference_weights.items()))}"
        )
        expression_layers = formula_expressions(n, 3)
        free_rows = tuple(row for row in range(row_count) if row not in rows)
        print("private_deletion_formula_witnesses:")
        for deleted, row in enumerate(rows):
            shorter_rows = rows[:deleted] + rows[deleted + 1:]
            shorter_target = (target & ((1 << deleted) - 1)) | (
                (target >> (deleted + 1)) << deleted
            )
            matches = [
                g for g in low_set
                if int(project_tables(np.array([g], dtype=np.uint16), shorter_rows)[0])
                == shorter_target
            ]
            witness = next(
                (g for layer in expression_layers for g in layer if g in matches), None
            )
            if witness is None:
                raise AssertionError(f"no low formula witness after deleting row {row}")
            gate_count = next(
                k for k, layer in enumerate(expression_layers) if witness in layer
            )
            print(f"  row={row}: {expression_layers[gate_count][witness]}; gates={gate_count}")
    if best_q_critical:
        rows, target = best_q_critical[0]
        full_table = sum(((target >> j) & 1) << row for j, row in enumerate(rows))
        print(
            f"example_best_Q_critical_partial=Q{rows}; target=0x{target:02x}; "
            f"zero_filled_total_table=0x{full_table:04x}; "
            f"minimum_selector_rows={int(sizes[full_table])}"
        )


if __name__ == "__main__":
    main()
