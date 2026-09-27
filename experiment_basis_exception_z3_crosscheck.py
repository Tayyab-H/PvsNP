"""Independent Z3 encoding for the exceptional 4-bit four-rule search.

This mirrors the semantic closure recurrence without using the PySAT/CNF
implementation. It checks whether four arbitrary endpoint-pair rules can
derive the empty set for anchors {0,3,5,9,14} over their complement.
"""

from __future__ import annotations

from z3 import And, Bool, Implies, Not, Or, Solver, sat, unsat


N = 4
ANCHORS = (0, 3, 5, 9, 14)
UNIVERSE = tuple(x for x in range(1 << N) if x not in ANCHORS)
RULES = 4


def check() -> None:
    solver = Solver()
    e = [[Bool(f"e_{r}_{u}") for u in range(len(UNIVERSE))]
         for r in range(RULES)]
    h = [[Bool(f"h_{r}_{u}") for u in range(len(UNIVERSE))]
         for r in range(RULES)]

    def base(anchor: int, endpoint: list) -> object:
        terms = []
        for bit in range(N):
            positions = [u for u, point in enumerate(UNIVERSE)
                         if ((point >> bit) & 1) == ((anchor >> bit) & 1)]
            terms.append(And(*(endpoint[u] for u in positions)))
        return Or(*terms)

    inc_e = [[Bool(f"inc_e_{k}_{r}") for r in range(RULES)]
             for k in range(RULES)]
    inc_h = [[Bool(f"inc_h_{k}_{r}") for r in range(RULES)]
             for k in range(RULES)]
    for k in range(RULES):
        for r in range(RULES):
            solver.add(inc_e[k][r] == And(*[
                Implies(And(e[k][u], h[k][u]), e[r][u])
                for u in range(len(UNIVERSE))
            ]))
            solver.add(inc_h[k][r] == And(*[
                Implies(And(e[k][u], h[k][u]), h[r][u])
                for u in range(len(UNIVERSE))
            ]))

    disjoint = [And(*[Not(And(e[r][u], h[r][u]))
                      for u in range(len(UNIVERSE))])
                for r in range(RULES)]

    for anchor in ANCHORS:
        base_e = [base(anchor, e[r]) for r in range(RULES)]
        base_h = [base(anchor, h[r]) for r in range(RULES)]
        fired = [[Bool(f"f_{anchor}_{r}_{t}")
                  for t in range(RULES + 1)] for r in range(RULES)]
        for r in range(RULES):
            solver.add(Not(fired[r][0]))
        for t in range(RULES):
            for r in range(RULES):
                active_e = Or(base_e[r], *[
                    And(fired[k][t], inc_e[k][r]) for k in range(RULES)
                ])
                active_h = Or(base_h[r], *[
                    And(fired[k][t], inc_h[k][r]) for k in range(RULES)
                ])
                solver.add(fired[r][t + 1] == Or(
                    fired[r][t], And(active_e, active_h)
                ))
        solver.add(Or(*[
            And(disjoint[r], fired[r][RULES]) for r in range(RULES)
        ]))

    status = solver.check()
    print(f"z3_status={status}; anchors={ANCHORS}; universe={len(UNIVERSE)}; "
          f"rules={RULES}; variables={len(solver.assertions())} assertions")
    if status == unsat:
        print("no_four_rule_cover=True")
    elif status == sat:
        model = solver.model()
        for r in range(RULES):
            left = [UNIVERSE[u] for u in range(len(UNIVERSE))
                    if model.eval(e[r][u], model_completion=True)]
            right = [UNIVERSE[u] for u in range(len(UNIVERSE))
                     if model.eval(h[r][u], model_completion=True)]
            print(f"rule={r}; E={left}; H={right}; intersection="
                  f"{sorted(set(left) & set(right))}")
    else:
        print(f"unknown_reason={solver.reason_unknown()}")


if __name__ == "__main__":
    check()
