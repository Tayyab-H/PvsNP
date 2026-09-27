"""Tiny LP checks for a game-theoretic SAT/UNSAT margin."""

from itertools import product

import numpy as np
from scipy.optimize import linprog


def clause_family(n: int):
    for choices in product((0, 1, -1), repeat=n):
        yield frozenset((i + 1) * sign for i, sign in enumerate(choices) if sign)


def falsifies(clause: frozenset[int], assignment: tuple[bool, ...]) -> bool:
    return all(assignment[abs(lit) - 1] != (lit > 0) for lit in clause)


def margin(n: int, clauses: tuple[frozenset[int], ...]) -> float:
    assignments = tuple(product((False, True), repeat=n))
    # Maximize t subject to each assignment having weighted violation >= t.
    # linprog minimizes, so negate t and encode t - weighted_violations <= 0.
    rows = []
    for assignment in assignments:
        violations = [float(falsifies(c, assignment)) for c in clauses]
        rows.append([-v for v in violations] + [1.0])
    objective = [0.0] * len(clauses) + [-1.0]
    equality = [[1.0] * len(clauses) + [0.0]]
    result = linprog(
        objective,
        A_ub=np.asarray(rows),
        b_ub=np.zeros(len(rows)),
        A_eq=np.asarray(equality),
        b_eq=np.asarray([1.0]),
        bounds=[(0.0, None)] * len(clauses) + [(0.0, None)],
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    return result.x[-1]


def main() -> None:
    examples = {
        "satisfiable": (frozenset((1, 2)),),
        "unique satisfying assignment": (frozenset((1,)), frozenset((2,))),
        "contradictory units": (frozenset((1,)), frozenset((-1,))),
        "four-cube cover": (
            frozenset((1, 2)), frozenset((1, -2)),
            frozenset((-1, 2)), frozenset((-1, -2)),
        ),
    }
    for name, clauses in examples.items():
        value = margin(2, clauses)
        print(f"{name}: optimized violation margin {value:.6f}")

    # Exhaust all CNFs over the 2-variable non-tautological clause family.
    atoms = tuple(clause_family(2))
    checked = 0
    for mask in range(1 << len(atoms)):
        clauses = tuple(atoms[j] for j in range(len(atoms)) if mask & (1 << j))
        assignments = tuple(product((False, True), repeat=2))
        unsat = all(any(falsifies(c, a) for c in clauses) for a in assignments)
        if not clauses:
            unsat = False
        value = margin(2, clauses) if clauses else 0.0
        assert (value > 1e-8) == unsat
        if unsat:
            assert value + 1e-8 >= 1.0 / len(clauses)
        checked += 1
    print(f"PASS: margin sign matched satisfiability for {checked} two-variable CNFs")


if __name__ == "__main__":
    main()
