"""Check the cube-containment meaning of a resolution step on small CNFs.

Clauses are tuples of signed variable indices. A cube is the set of complete
assignments falsifying the clause. This checks a familiar proof-complexity
correspondence on small cases; it is not a new theorem.
"""

from itertools import product


def all_nontautological_clauses(n: int):
    # For each variable: absent, positive, or negative.
    for choices in product((0, 1, -1), repeat=n):
        yield frozenset((i + 1) * sign for i, sign in enumerate(choices) if sign)


def falsifies(clause: frozenset[int], assignment: tuple[int, ...]) -> bool:
    return all(assignment[abs(lit) - 1] != (lit > 0) for lit in clause)


def check_resolution_containment(n: int) -> int:
    clauses = tuple(all_nontautological_clauses(n))
    assignments = tuple(product((False, True), repeat=n))
    checked = 0
    for pivot in range(1, n + 1):
        for left_tail in clauses:
            if pivot in left_tail or -pivot in left_tail:
                continue
            left = left_tail | {pivot}
            for right_tail in clauses:
                if pivot in right_tail or -pivot in right_tail:
                    continue
                right = right_tail | {-pivot}
                resolvent = left_tail | right_tail
                for assignment in assignments:
                    if falsifies(resolvent, assignment):
                        assert falsifies(left, assignment) or falsifies(right, assignment)
                checked += 1
    return checked


def demo_unsat_cover() -> None:
    # (x or y), (!x or y), (x or !y), (!x or !y)
    # resolve the first pair to y, the second pair to !y, then to the empty clause.
    assignments = tuple(product((False, True), repeat=2))
    clauses = (
        frozenset((1, 2)),
        frozenset((-1, 2)),
        frozenset((1, -2)),
        frozenset((-1, -2)),
    )
    assert all(any(falsifies(clause, a) for clause in clauses) for a in assignments)

    # The falsifying cube of each resolvent is contained in the union of its parents.
    resolutions = [
        (frozenset((2,)), clauses[0], clauses[1]),
        (frozenset((-2,)), clauses[2], clauses[3]),
        (frozenset(), frozenset((2,)), frozenset((-2,))),
    ]
    for child, left, right in resolutions:
        for a in assignments:
            if falsifies(child, a):
                assert falsifies(left, a) or falsifies(right, a)


def main() -> None:
    for n in range(1, 5):
        print(f"n={n}: checked {check_resolution_containment(n)} pivot-clause pairs")
    demo_unsat_cover()
    print("PASS: resolution steps give valid falsifying-cube cover containments")


if __name__ == "__main__":
    main()
