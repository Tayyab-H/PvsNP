# C-460 — First-principles project audit after C-459

**Date:** 1 October 2026  
**Scope:** cumulative ordinary Gap-MCSP work through C-459, read from the exact promise and resource model.  
**Status:** research diagnosis and priority reset; no new lower bound, full-promise near-linear separator, or P-vs-NP proof.

## 1. Start with the object the proof must control

Let `N=2^n`, and let `L_t` be the set of truth tables of `n`-input Boolean functions having fan-in-two AND/OR/NOT circuit size at most `t`. With the OPS thresholds

```text
s1 = N^beta/(c log_2 N),       s2 = N^beta,
```

a valid total separator is any Boolean function `F:{0,1}^N -> {0,1}` such that

```text
L_s1 subseteq F^(-1)(1) subseteq L_s2.
```

The second inclusion follows because promised NO tables have complexity greater than `s2`; behavior in the middle band is unrestricted. Define

```text
GapSep(N,beta) = min { CC_N(F) : L_s1 subseteq F^(-1)(1) subseteq L_s2 },
```

where `CC_N` counts total fan-in-two AND/OR/NOT gates on the `N` table inputs. This is the direct target. No lower bound for one chosen separator, the exact characteristic function of `L_s1`, or a restricted model implies a bound on this minimum without an additional theorem.

OPS Theorem 1.4 asks for one fixed `epsilon>0` such that `GapSep(N,beta)>N^(1+epsilon)` for every sufficiently small fixed `beta>0` (with the paper's constant and rounding conventions). This would imply `NP not subseteq P/poly`, a stronger conclusion than `P != NP`. The implication is a sufficient magnification route, not an equivalence. The fact that this target is open does not logically guarantee that a short missing argument exists; the proposed lower bound itself may be as difficult as the nonuniform class separation it would establish.

## 2. What the accumulated work has actually established

The project history is not empty, but its strongest contributions are calibrations of the gap rather than exponent progress.

| Evidence class | Proved or tested result | Why it stops short |
|---|---|---|
| Input exposure | Every separator has `N-O(N^beta log N)` essential table inputs and at least that many gates up to constants/additive refinements (C-403, C-406). | There are only `N` input coordinates. This pays for reading/dependence, not for the additional computation needed to classify the whole codebook. |
| Formula/reconvergence transfer | OPS formula hardness forces logarithmic gate-to-gate reconvergence in the near-linear regime (C-406). | Unfolding loses exponentially in cycle rank; the resulting surplus is only logarithmic and is swallowed by the support slack. |
| Coarse function statistics | Support, degree, cut rank, transcript fibers, certificate counts, and local sensitivity have exact bounds or explicit calibrations (C-423–C-429, C-435–C-457). | Linear-size circuits can have all inputs essential, maximal algebraic degree, sparse acceptance, large rank, or shared local/global checks. These quantities do not capture the full Low/High labels. |
| One-sided recognition | An `O(N log N)` circuit can reject every actual High table while accepting substantial structured Low families (C-457). | It misses even a simple Low family. Soundness is cheap; completeness over *all* Low circuit tables is the hard obligation. |
| Robustness | Changing `r` table entries changes circuit complexity by `O(r log N)` gates, so separators obey forced neighborhood conditions (C-458). | C-459 gives an `O(N log N)` separator for an unrelated promise with the same two radii. Radii and repair counts alone do not charge gates. |
| Source reductions | Composition budgets, endpoint failures, decoder leakage, and parameter mismatches are proved in C-430–C-455. | No map has simultaneously preserved exact OPS YES/NO endpoints, avoided a cheap source-output decoder, and left `N^(1+epsilon)` source-hardness after all generator and postprocessing gates. Serial-query costs are only compiler upper bounds. |
| Restricted models and proof systems | Formula, comparator, monotone, locality, and QBF/refutation routes were checked against their actual transfer directions. | Their bounds do not transfer to arbitrary ordinary shared DAGs without a proved compiler or an exact promise-preserving restriction. Native fusion `rho` is a separate model. |

Parity, repeated-block equality, sparse parity-check systems, simple global block relations, and population counting serve as important hostile examples. They show that input count, incidence, number of local constraints, and robust patchability are not themselves shared-gate charges. They do **not** refute a Gap-MCSP separator lower bound.

## 3. The common obstruction, stated without a new label

Almost every failed route did one of two things:

1. It proved a semantic fact about which tables `F` must accept or reject, but had no inequality charging that fact to gates in an arbitrary reusable DAG.
2. It proved a lower bound in a restricted model or for a source function, but lacked a costed, endpoint-correct transfer to every valid OPS separator.

The unfilled proof obligation is therefore precise: exploit the *joint arrangement* of all size-`s1` circuit tables inside all size-`s2` circuit tables, and show that every Boolean extension recognizing that sandwich uses superlinear total gates even with arbitrary fan-out and arbitrary middle-band labels. A new potential is useful only if it has both halves: an operation-wise gate bound for every AND/OR/NOT DAG, and a superlinear value forced by this exact sandwich. Renaming “non-shareability,” counting more anchors, or refining the Hamming radii supplies neither half.

The paired construction remains exact enumeration of all Low circuit descriptions, costing `O(N*2^(O(N^beta)))` total gates. No near-linear full-promise construction has been found. Consequently the direct lower-bound frontier remains `N-O(N^beta log N)` with C-406's additive logarithmic reconvergence refinement; the OPS exponent target and native `rho>=N-o(N)` remain open and separate.

## 4. Revised research method

The next cycles should be judged by two concrete outcomes, not by the novelty of their terminology:

**Direct route.** State a theorem about `GapSep(N,beta)` itself. It must quantify over every total extension and count ordinary total gates. Identify a property that distinguishes the full Low codebook from High tables, prove how every AND/OR/NOT gate can change the property under unrestricted reuse, and prove the output value is `N^(1+epsilon)` for one common `epsilon` and all sufficiently small fixed `beta`. Attack it immediately with parity, repeated-block equality, sparse checks, global block relations, and the C-457/C-459 calibrations. Retire the mechanism if either inequality fails.

**Transfer route.** Give a fully specified hard source `g_m` and a multi-output table generator `G_m`. Prove the two implications `g_m(y)=1 => CC(G_m(y))<=s1` and `g_m(y)=0 => CC(G_m(y))>s2`; then count every generator, decoder, router, separator, and postprocessor gate. The source lower bound must exceed the complete composition by `N^(1+epsilon)` with the OPS quantifiers. Do not infer table hardness from a hard witness or source description, and do not assume a separator reconstructs a circuit or witness.

At each cycle, also search for a genuine full-promise separator below the enumeration upper bound. Such a construction would change the target itself; a sound incomplete filter would only calibrate it. Keep ordinary gate count, paid native states, OR operations, wires, description bits, and runtime separate.

This is a research filter rather than a new lower-bound theorem. Its first-principles conclusion is that the project should now spend effort on a concrete extension theorem or a complete separator construction, not on another generic statistic. If neither can be made precise, record that as a stop condition for that branch and redirect effort rather than sharpening it repeatedly.

## 5. Barriers and originality

OPS is the primary source for the exact magnification implication and its quantifiers. Chen et al.'s locality barrier is a method-specific obstruction: it rules out certain locality-respecting proof techniques, not every proof of the ordinary circuit lower bound. C-454 already translates the relevant AC0 reduction obstruction to the OPS parameter scale. Neither the locality barrier nor natural-proofs discussion is a universal impossibility theorem.

The present audit is a synthesis and priority correction, not a claim of novelty in circuit complexity. The new fact of this cycle is C-459's explicit falsification of “robust neighborhoods alone imply a gate charge”; the rest consolidates proved obligations and counterexamples into a sharper research standard.

### Primary sources

- Oliveira, Pich, Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*, Theorem 1.4 and Theorem 1.5](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://eccc.weizmann.ac.il/report/2019/168/download).
- Ren, Williams, [ECCC TR26-118](https://eccc.weizmann.ac.il/report/2026/118/download), source route already audited in C-437–C-442.

**Exact status:** no quantitative improvement over the frontier above; no near-linear full-promise separator; no OPS lower bound; no native-model transfer; no P-vs-NP proof.
