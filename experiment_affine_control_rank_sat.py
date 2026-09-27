"""End-to-end checks for SAT parameterized by projected affine control rank."""

from itertools import combinations
import random

from experiment_affine_control_rank_fpt import add_to_basis, in_span, rank_cover


def affine_parameterization(variable_count, equations):
    """Return an affine base point, nullspace directions, and wire row vectors."""
    basis = {}
    for mask, rhs in equations:
        while mask:
            pivot = mask.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = (mask, rhs)
                break
            other, value = basis[pivot]
            mask ^= other
            rhs ^= value
        else:
            if rhs:
                return None

    for pivot in sorted(basis):
        mask, rhs = basis[pivot]
        for higher in sorted(basis):
            if higher > pivot and (basis[higher][0] >> pivot) & 1:
                other, value = basis[higher]
                basis[higher] = (other ^ mask, value ^ rhs)

    free = [i for i in range(variable_count) if i not in basis]
    base = 0
    for pivot, (_, rhs) in basis.items():
        if rhs:
            base |= 1 << pivot

    directions = []
    for parameter, variable in enumerate(free):
        direction = 1 << variable
        for pivot, (mask, _) in basis.items():
            if (mask >> variable) & 1:
                direction |= 1 << pivot
        directions.append(direction)

    row_vectors = []
    for wire in range(variable_count):
        row_vectors.append(sum(
            ((direction >> wire) & 1) << parameter
            for parameter, direction in enumerate(directions)
        ))
    return base, tuple(directions), tuple(row_vectors)


def projected_patterns(base, directions, row_vectors, controls):
    """Enumerate the affine image on controls using 2^rank image vectors."""
    columns = []
    for parameter in range(len(directions)):
        column = sum(
            ((row_vectors[wire] >> parameter) & 1) << position
            for position, wire in enumerate(controls)
        )
        updated = add_to_basis(column, columns)
        if updated is not None:
            columns = updated
    image_basis = [row for _, row in columns]
    offset = sum(((base >> wire) & 1) << position
                 for position, wire in enumerate(controls))
    patterns = {
        offset ^ _xor_selected(image_basis, combination)
        for combination in range(1 << len(image_basis))
    }
    assert len(patterns) == 1 << len(image_basis)
    return patterns, len(image_basis)


def _xor_selected(vectors, bits):
    value = 0
    for i, vector in enumerate(vectors):
        if (bits >> i) & 1:
            value ^= vector
    return value


def affine_sat_with_controls(variable_count, equations, and_gates):
    """Find a minimum-rank control cover, then solve each affine slice."""
    rows = list(equations)
    nonlinear = []
    for left, right, output in and_gates:
        if left == right:
            rows.append(((1 << left) ^ (1 << output), 0))
        else:
            nonlinear.append((left, right, output))

    affine = affine_parameterization(variable_count, rows)
    if affine is None:
        return False, 0, 0
    base, directions, row_vectors = affine
    edges = sorted({tuple(sorted((left, right)))
                    for left, right, _ in nonlinear})
    optimum, cover, branch_nodes = rank_cover(row_vectors, edges)

    controls = tuple(sorted({
        left if left in cover else right
        for left, right, _ in nonlinear
    }))
    patterns, projected_rank = projected_patterns(
        base, directions, row_vectors, controls
    )
    assert projected_rank == optimum

    for pattern in patterns:
        fixed = {wire: (pattern >> position) & 1
                 for position, wire in enumerate(controls)}
        candidate_rows = list(rows)
        candidate_rows.extend((1 << wire, value)
                              for wire, value in fixed.items())
        for left, right, output in nonlinear:
            if left in fixed:
                control, other = left, right
            else:
                assert right in fixed
                control, other = right, left
            if fixed[control] == 0:
                candidate_rows.append((1 << output, 0))
            else:
                candidate_rows.append(((1 << output) ^ (1 << other), 0))
        if affine_parameterization(variable_count, candidate_rows) is not None:
            return True, optimum, branch_nodes
    return False, optimum, branch_nodes


def brute_sat(variable_count, equations, and_gates):
    for assignment in range(1 << variable_count):
        if not all((assignment & mask).bit_count() % 2 == rhs
                   for mask, rhs in equations):
            continue
        if all(((assignment >> output) & 1) ==
               (((assignment >> left) & 1) & ((assignment >> right) & 1))
               for left, right, output in and_gates):
            return True
    return False


def main():
    rng = random.Random(20260923)
    classifications = {"SAT": 0, "UNSAT": 0}
    for case in range(2500):
        variable_count = rng.randint(1, 8)
        equations = [
            (rng.randrange(1 << variable_count), rng.randrange(2))
            for _ in range(rng.randint(0, 9))
        ]
        and_gates = [
            tuple(rng.randrange(variable_count) for _ in range(3))
            for _ in range(rng.randint(0, 7))
        ]
        expected = brute_sat(variable_count, equations, and_gates)
        found, _, _ = affine_sat_with_controls(
            variable_count, equations, and_gates
        )
        assert found == expected, (case, variable_count, equations,
                                   and_gates, expected, found)
        classifications["SAT" if expected else "UNSAT"] += 1

    # A family with many AND gates but a one-dimensional control cover.
    large_cases = []
    for gate_count in (8, 64, 256):
        input_count = gate_count + 1
        outputs = tuple(input_count + i for i in range(gate_count))
        variable_count = input_count + gate_count
        equations = [(sum(1 << output for output in outputs), 1)]
        gates = [(0, i + 1, outputs[i]) for i in range(gate_count)]
        found, rank, nodes = affine_sat_with_controls(
            variable_count, equations, gates
        )
        assert found and rank == 1 and nodes <= 3
        large_cases.append((gate_count, rank, nodes))

    print(f"random_systems={sum(classifications.values())}")
    print(f"SAT={classifications['SAT']} UNSAT={classifications['UNSAT']}")
    print(f"large_shared_control_cases={large_cases}")
    print("parameterized solver matched exhaustive oracle on every small system")


if __name__ == "__main__":
    main()
