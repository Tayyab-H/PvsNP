# C-442 - First-principles reassessment: charge the semantic jump

**Date:** 1 October 2026  
**Status:** project synthesis plus a proved composition lemma; no new Gap-MCSP lower bound.

## Scope and exact target

This audit reconciles the durable `CLAIM_LEDGER.md`, `CURRENT_STATE.md`, `New Model.MD`, `BARRIER_AUDIT.md`, `GOAL.md`, `IDEA_QUEUE.md`, `OPEN_OBLIGATIONS.md`, and the C-439--C-441 reports. The older ledger is used as the index of prior results; this report does not re-prove every historical lemma. The claims below marked project-proved retain their individual reports as the proof record.

For `N=2^n`, an ordinary separator is any fan-in-two AND/OR/NOT circuit, with arbitrary fanout, that outputs 1 on every table `f` with

```text
CC(f) <= s1 = N^beta/(c log_2 N)
```

and 0 on every table with

```text
CC(f) > s2 = N^beta.
```

Its value on the middle band is unconstrained. The OPS magnification premise asks for one fixed `epsilon>0` such that, for every sufficiently small fixed `beta>0`, no such separator has at most `N^(1+epsilon)` gates. Its theorem implies `NP not subseteq P/poly`, hence `P != NP`; the reverse implication is not known. The theorem's exact quantifiers and the universal denominator `c` are in [Oliveira--Pich--Santhanam, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).

The durable ordinary frontier remains `S >= N-O(N^beta log N)-1`, with C-406's additive logarithmic refinement. The exact full-promise separator remains `O(N*2^(O(N^beta)))`. The native fusion target `rho >= N-o(N)` is a different measure and does not transfer automatically. No quantitative frontier changes in this cycle.

## A general predecoding-budget lemma

This is the strongest new statement of the cycle. It generalizes the C-441 obstruction beyond prefix tables.

Let `g_m` be a source Boolean function with `CC(g_m) >= h_m`. Let `G_m` be an ordinary multi-output circuit of `J_m` gates mapping source inputs `x` to an `N`-bit table `T_x`. Suppose there is an ordinary decoder `D_N` of `B_N` gates such that

```text
D_N(T_x) = g_m(x) for every x.
```

Then

```text
h_m <= J_m + B_N + O(1).                 (1)
```

If the range of `G_m` is OPS-promised with label `g_m(x)` and a separator of size `S_N` is correct on that range, composition also gives

```text
h_m <= J_m + S_N + O(1).                 (2)
```

**Proof.** Compose `G_m` with `D_N` for (1), and compose `G_m` with the separator for (2). Both are ordinary circuits; every gate of the generator and postprocessor is charged. From (1), `J_m >= h_m-B_N-O(1)`. Thus (2) cannot contradict the source lower bound using only these inequalities once `S_N >= B_N+O(1)`. The conclusion is route-specific: it does not bound `S_N`, and extra information about the generator or source could support a different argument.

For C-441's complete prefix-extension table, the prefix trie decodes the lexicographically largest satisfying assignment and hence the Ren--Williams source output using `B_N=O(N)` gates. Therefore this table cannot turn the `Omega(2^m/m)` source lower bound into an OPS separator lower bound above linear size by plain source composition: the generator is already forced to have size at least `h_m-O(N)`. This is stronger and more decisive than asking only whether the table's YES and NO circuit complexities have a gap. See [Ren--Williams, ECCC TR26-118](https://eccc.weizmann.ac.il/report/2026/118/) and [C-441](C441_PREFIX_TABLE_ALREADY_CONTAINS_SOURCE_OUTPUT_2026-10-01.md).

## What the accumulated attempts say from first principles

Across the durable project record, the repeated mismatch is between **what the promise forces semantically** and **what ordinary DAG gates cost after reuse**.

| Attempt family | What survives scrutiny | Where the desired charge fails |
|---|---|---|
| Support, cylinders, anchors, and sensitivity | A separator must depend on almost all table coordinates; projected Low cylinders quantify the remaining slack. | Reading and aggregating `N` bits costs only `O(N)` gates. The OPS target is above that scale. |
| Counts, certificates, anti-checkers, transcript fibers | Short anti-checkers exist for individual High tables; gate transcripts have precise local structure. | Existence is not synthesis from the separator. Certificates can have length `N`, fibers can be singletons after an `O(N)` identity front end, and a gate can serve many constraints. The middle band also prevents treating every rejection witness as a zero-certificate. |
| Restrictions, codes, and source hardness | Promise-preserving composition correctly charges a generator, separator, and postprocessor. Several source lower bounds are real in their native models. | Tested slices often have easy induced labels; other routes change monotonicity/fanout/model. When a table cheaply reveals the source label, (1) shows the generator consumes the source-hardness budget. |
| Formula/comparator/native fusion bounds | These models permit substantial lower bounds and expose sharing as a measurable resource. | Formula unfolding pays exponentially in reconvergence; comparator bounds do not apply to arbitrary DAGs; fusion-to-DAG conversions lose powers. No low-loss transfer to the ordinary total-gate target has been proved. |
| Logic, diagonalization, and foundations | They clarify the quantifiers and the difference between truth, provability, and finding witnesses. | Self-reference does not remove a universal quantifier over circuits or make a SAT counterexample easy to verify. Oracle independence and natural/locality barriers limit specified proof methods; neither proves independence or rules out all proofs. |
| Full-promise algorithms | Enumerating all Low descriptions gives an exact separator and handles every promised input. | The present gate count is `O(N*2^(O(N^beta)))`; no near-linear implementation is known. |

The model-level lesson is not that all methods fail. It is that a lower bound for this promise needs one of two concrete bridges: (i) a quantity forced by **every** valid total extension whose growth is bounded under each AND/OR/NOT operation despite arbitrary fanout and whose output value is superlinear; or (ii) a source map whose exact promise is proved and whose ordinary generation cost leaves more than `N^(1+epsilon)` gates of source-hardness margin for the separator. "Many constraints," "many witnesses," or "large description entropy" does not provide either bridge without a gate inequality.

## Counterconstruction checks

These are attacks on generic charging mechanisms, not counterexamples to the Gap-MCSP lower-bound program.

* **Parity:** one parity of `N` input bits uses `O(N)` fan-in-two gates. Many repeated parity demands can reuse subcomputations; incidence count need not equal paid gates.
* **Repeated-block equality:** on a block-constant restriction, comparing one representative per block costs `O(q)` gates, independent of the number of repeated table coordinates. C-418/C-419 prove exact easy induced separators for all balanced-block dimensions in their stated parameter ranges.
* **Sparse parity checks:** a family with `L` total incidences can be evaluated with `O(L)` gates after replacing each XOR by a constant-size AND/OR/NOT circuit. `O(N)` total incidence therefore gives an `O(N)` shared computation, not a superlinear charge.
* **Simple global block relations:** equality, parity, and fixed finite Boolean combinations of shared block signals can be evaluated once and reused. Large output multiplicity or a long list of local checks does not force a separate gate payment for each check.

These constructions show why the next mechanism must account for the actual DAG functions and their fanout. They do not produce a separator for the full promise and do not imply an upper bound below the exact enumeration construction.

## Reassessing what may be missing

The record does **not** support the claim that a small overlooked counting trick, a ZFC axiom, or a new name for circuit sharing is enough. It identifies a precise missing implication: from the promise's global semantic constraints to a superlinear lower bound on the reusable computation that recognizes those constraints. In source-transfer language, the missing object is an output-hidden, exact Gap-MCSP reduction with a certified gate budget; C-441 closes the obvious all-prefix encoding because the table itself has a linear-size source decoder.

There is also a strategic correction. OPS is an exceptionally strong sufficient route to `P != NP`: it would rule out `NP subseteq P/poly`. Since `P != NP` alone is not known to imply that nonuniform separation, working only on OPS may overshoot the requested theorem. Keep OPS as the user's quantitative primary target, but allow a separate direct uniform SAT route if it develops a genuinely different proof obligation; do not label the two goals equivalent. The standard foundational survey treats ZFC independence as an open metamathematical question, not an established obstruction ([Aaronson, *Is P Versus NP Formally Independent?*](https://www.scottaaronson.com/papers/indep.pdf)). A 2024 preprint titled *On P=NP Either False or Independent of ZFC* explicitly presents its key independence step as a conjecture, so it supplies no P-vs-NP theorem or usable independence result ([arXiv:2404.00468](https://arxiv.org/abs/2404.00468)).

The locality barrier likewise remains technique-specific. It explains why several lower-bound methods that extend to small-fan-in oracle circuits cannot establish selected magnification frontiers; it is not a theorem that every possible ordinary-circuit proof is blocked ([Chen et al., ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/)).

## Next research action

Retire the complete prefix-extension table as a source-hardness route: its easy decoder alone consumes the full source lower-bound margin above `O(N)`. Preserve C-440/C-441 as counterexamples. For the next source attempt, apply the predecoding-budget audit **before** analyzing the promise gap:

1. Specify one ordinary multi-output generator `G_m` and prove the exact OPS YES/NO image conditions, including the free middle band.
2. Search for any direct decoder `D_N(T_x)=g_m(x)` and give its total fan-in-two gate cost. If `B_N=O(N)` and the intended separator is superlinear, do not use that source-composition route unless an additional, independent budget argument changes the inequality.
3. Prove an explicit upper bound `J_m` with `h_m-J_m>N_m^(1+epsilon)` for a common fixed `epsilon`; no oracle answers or source label may be hidden in `G_m`.
4. Pair the map with the direct gate-semantic route: any proposed potential must be evaluated gate by gate under unrestricted reuse and forced by every valid extension.

If no map survives steps 1--3, shift the next cycle to a direct promise-forced DAG invariant or an independent uniform SAT proof attempt, rather than sharpening the same prefix, query-additivity, support, or incidence argument. The OPS and P-vs-NP frontiers remain unchanged.
