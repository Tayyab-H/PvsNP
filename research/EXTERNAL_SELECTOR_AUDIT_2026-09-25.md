# External audit: anti-checker selector lower bounds — 25 September 2026

## Sources checked

- Joshua Christl, [P vs NP — Lean proofs and research](https://joshua.plus/lean/p/p-vs-np/), public project-status page accessed 25 September 2026. This is a research workbench page, not a peer-reviewed paper; its Lean status labels and repository theorems were not independently inspected here.
- Oliveira, Pich, and Santhanam, [Hardness Magnification Near State-of-the-Art Lower Bounds](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and Lemma 4.1 (primary source).
- Clay Mathematics Institute, [P vs NP](https://www.claymath.org/millennium/p-vs-np/), still listed under “Unsolved” on the page checked.

## Independent convergence on the selector obstruction

The Lean workbench page reports all of the following in its selector section:

1. A linear shared-circuit support lower bound for selectors, from collecting input coordinates feeding gates and direct input outputs.
2. An exact “fiber anti-cover” characterization equivalent to selector validity, and a theorem that agreement inside a fixed selector-output fiber with a low circuit cannot produce a hard table.
3. Failure of additive anchor-sensitivity charging because one shared gate or input can serve many anchors; deduplicating sensitive coordinates returns only the linear support ceiling.
4. A constant-gate full-query selector when the allowed number of addresses reaches the whole truth-table domain.
5. The general direct-selector superlinear lower bound remains open in that workbench; it states a stronger progression-robust variant for its own encoded-length route.

Items 1–3 align with this project's C-34/C-38 and C-63 analyses. In particular, C-63 is an exact reformulation, not a novel lower-bound theorem. The full-query counterexample is parameter-sensitive: OPS uses \(t=N^{10\beta}\), and we choose \(\beta<1/10\), so the required list is sublinear in N. One must keep this budget restriction explicit.

The workbench's progression-robust target should not be silently imported into the OPS route. Under the OPS conditional lemma, assuming \(NP\subseteq P/poly\) yields a selector at every sufficiently large arity for every sufficiently small fixed beta. Therefore an infinitely-often selector lower bound at any infinite set of arities suffices for contradiction, provided the lower-bound theorem holds throughout a small beta interval so beta can be selected after the assumed exponent k is fixed. This exact quantifier repair is C-65.

## Reassessment and next move

The selector-fiber identity, additive coordinate support, and per-anchor sensitivity are now low-value targets: the first is definitional, the second gives only a linear bound, and repeated anchor costs can reuse shared wiring. Do not try to amplify them by summing over anchors or output fibers without a new gate-ownership theorem.

The next meaningful target remains a **non-coordinate, promise-specific invariant of the shared selector circuit** that forces superlinear size when it outputs a sublinear anti-checker for every high table. It must exploit simultaneous avoidance of the full \(SIZE(s_1)\) trace family. The two-constant priority example and C-64 fixed-menu construction remain mandatory counterchecks.

No proof of P vs NP or new superlinear selector theorem was found in this audit.
## Short-list refinement from the project ledger

C-48 supplies a more focused sufficient target than the full OPS output budget: under $NP\subseteq P/poly$, it constructs valid selectors with $O(s_1\log(s_1+n))$ addresses and size $N^{1+O(\beta)}$. Therefore only this short-output selector class needs a superlinear lower bound for the conditional contradiction. C-49 adds relative trace distance $\Omega(1/n^2)$ at that list length. This strengthens the *certificate geometry* and narrows the output class; it does not solve the shared-routing circuit lower bound. The project has recorded this as S-2/C-66.