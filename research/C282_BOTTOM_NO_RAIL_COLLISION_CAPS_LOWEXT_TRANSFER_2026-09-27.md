# C-282 — Bottom-NO rail collision attempt (withdrawn)

Date: 27 September 2026  
Original classification: ROUTE-KILL. **Withdrawn by C-283; do not rely on this report's original conclusion.**

## Original claim and exact failure

The original argument selected a high completion `z0` above the bottom NO image `P=phi(0)`, then claimed that every YES low code `e(w)` conflicts with a rail of `P` because `w!=z0`. The selected differing coordinate need not be pinned in `P`: `P` may leave it blank. Monotonicity carries only pinned rails, so the proposed collision detector can reject a YES input.

The abstract counterexample is `phi(0)=empty`, `phi(1)=e(w)` for a one-bit monotone source, with `w` low and any disjoint high table `z0`. The one-hot order conditions hold, but the collision detector is zero on both inputs.

## Superseding result

C-283 proves the corrected decomposition. With `P=phi(0)` having d holes and `K(P)={w in SIZE(s1):P<=e(w)}`, collisions on pinned coordinates and code tests restricted to the holes give a source separator of AND-cost at most `a+(N-d)+|K(P)| max(d-1,0)`. Since `|K(P)|<=2^d`, a transfer seeking `q>N^(1+epsilon)` needs `d >= (1+epsilon)log2 N-log2(log N)-O(1)`.

C-266/C-267 remain valid conditional cyclic-source and parameter results. C-282 does not close Route A, does not change actual `q=N-o(N)`, and has no P-vs-NP consequence. See `research/C283_BOTTOM_BASELINE_HOLES_COUNTEREXAMPLE_AND_REPAIR_2026-09-27.md`.
