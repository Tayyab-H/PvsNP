"""Tiny counterexamples to deciding SAT from one modular solution count."""

from itertools import product


def count_models(n: int, clauses: tuple[tuple[int, ...], ...]) -> int:
    total = 0
    for assignment in product((False, True), repeat=n):
        sat = all(
            any(assignment[abs(lit) - 1] == (lit > 0) for lit in clause)
            for clause in clauses
        )
        total += sat
    return total


def main() -> None:
    examples = [
        (2, ((-1, -2),), 3),  # exactly 3 satisfying assignments, modulus 3
        (1, (), 2),           # exactly 2 satisfying assignments, modulus 2
    ]
    for n, clauses, prime in examples:
        models = count_models(n, clauses)
        assert models > 0
        assert models % prime == 0
        print(f"n={n}, models={models}, modulus={prime}, residue=0 despite SAT")

    # A single satisfying assignment can also disappear modulo any prime > 1.
    unique = count_models(2, ((1,), (-1, 2)))
    assert unique == 1
    assert unique % 2 != 0
    print("PASS: modular zero is not an UNSAT certificate")


if __name__ == "__main__":
    main()
