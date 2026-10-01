# C-446 — First-principles audit and a gate-path view of shared work

**Date:** 1 October 2026  
**Scope:** audit through C-445, with direct checks of the ordinary-circuit frontier, source-budget results, certificate routes, restricted-model transfers, and the accumulated native/ordinary distinction.  
**Status:** a sharper formulation and a tested model for where sharing lives; no superlinear lower bound or near-linear full-promise separator.

## 1. Reduce the target to its exact mathematical object

Let `N=2^n`, and let `L_t` be the set of `N`-bit truth tables computable by an `n`-input fan-in-two circuit with at most `t` gates. For the OPS promise, `s1=N^β/(c n)` and `s2=N^β`; YES is `L_s1` and NO is the set of tables with complexity **greater than** `s2`.

The hardness-magnification quantifiers are: there is one universal constant `c≥1`; if there exists one fixed `ε>0` such that **for every sufficiently small fixed `β>0`**, `Gap-MCSP[2^(βn)/(c n),2^(βn)]` requires circuits of size greater than `N^(1+ε)`, then `NP⊄Circuit[poly]`. The same `ε` must work throughout that range of `β`; proving a separate `ε(β)` for each `β` is not the stated trigger. This is a worst-case ordinary-circuit lower bound for the promise problem, and the output claim is the nonuniform separation `NP⊄P/poly`. See OPS, Theorem 1.4, [Theory of Computing 17 (2021)](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf).

For any total Boolean function `F` on the `N` table bits, its accepting set `A=F^{-1}(1)` is a valid separator exactly when

```text
L_s1 ⊆ A ⊆ L_s2.
```

Therefore the target is precisely

```text
GapSep(N,s1,s2) = min { CC_N(1_A) : L_s1 ⊆ A ⊆ L_s2 },
```

where `CC_N` counts total fan-in-two AND/OR/NOT gates on the `N`-bit input. **Proof:** a valid separator accepts every member of `L_s1` and cannot accept any table of complexity greater than `s2`; conversely, any set in this interval gives a valid separator, with arbitrary labels in the middle. This is the minimum circuit size over *all* valid extensions. Lower-bounding only `1_{L_s1}` or `1_{L_s2}` would not suffice.

Counting descriptions gives `|L_s2| ≤ 2^{O(s2 log(N+s2))}=2^{O(N^β n)}=2^{o(N)}` for each fixed `β<1`. Conversely, minterm DNFs show that `L_s1` already contains all tables with support size at most `r=Theta(N^β/n^2)`, giving at least `binom(N,r)=2^{Theta(N^β/n)}` forced positive inputs. Thus every valid extension is sparse, but must contain a structured set of exponentially many positives. Sparsity and positive-set size alone do not determine its circuit complexity.

The exact full-promise construction remains the OR over every size-`s1` circuit description of its full `N`-coordinate agreement test. It costs `O(N·2^{O(N^β)})` gates. No near-linear full-promise extension has been constructed.

## 2. What the accumulated approaches establish—and where each stops

| Line of work | Verified content | Exact obstruction to the OPS exponent |
|---|---|---|
| Essential inputs, subcubes, sensitivity (C-403, C-426) | Every separator depends on `N-O(N^β n)` table bits; this yields `S≥N-O(N^β n)-1`. | It pays for dependence on the `N` input coordinates, not the computation that combines them. A readout floor cannot exceed the linear scale. |
| Formula transfer and reconvergence (C-406) | `S≥E(C)+μ(C)-1`, and OPS formula hardness forces `μ=Omega(log N)` in the near-linear regime. | The additive cycle surplus is logarithmic, swallowed by the `O(N^β n)` input-support slack. |
| Certificates, pivots, anti-checkers (C-421–425) | High tables have short semantic anti-checkers; accepting certificates must stay inside `L_s2`; the actual-High pivot counterexample isolates the missing use of full Low completeness. | A separator need not output the anti-checker. Certificate counts give at most `O(N^β polylog N)`-scale lower bounds, while population counters share exponentially many certificates with `O(N)` gates. The middle-band freedom prevents turning a Low anti-checker into a separator certificate. |
| Gate transcripts, fibers, rank, local constraints (C-426–429, C-435) | The DAG and communication statements are correctly charged for reuse; cut rank gives `R≤2S+1`. | Rank has dimension ceiling `R≤N/2`; an `N-1`-gate predicate attains full balanced cut rank. An identity front end can make local transcript fibers singletons while leaving arbitrary post-read computation. |
| Code/source embeddings and hardness magnification (C-420, C-430–433, C-436–442) | Costed composition and the predecoding budget are rigorous. Several published source lower bounds are strong in their own models. | The induced label is often easy, the output table leaks the source bit through an `O(N)` decoder, or the certified gap fails the OPS ratio. Serial query costs are upper bounds, not lower bounds, because joint sharing can save gates. |
| Formula, comparator, monotone, and native models (C-434, C-436, C-319 onward) | Restricted models expose genuine lower bounds; the native closure record maintains `ρ≥N-o(N)` with arbitrary endpoints, reuse, cycles, and semi-filter extensions as specified there. | Comparator gains depend on `β` and do not lift to arbitrary fan-out DAGs; monotone hardness is lost under unrestricted negations; formula unfolding pays exponentially in reconvergence. Native `ρ` is a different measure, with no cost-preserving ordinary-gate bridge. |
| Logic and feasible interpolation (C-443–445) | The exact endpoints are `∃d∀i` for YES and `∀d∃i` for NO. The all-descriptions mismatch list is too long; proof-certified High subsets are a valid transfer lemma. | NO is coNP, standard interpolation has proof-to-circuit direction, and no hard certified pair is instantiated. Per-circuit refuters do not certify the universal condition. |

The shared diagnosis is now precise: semantic objects, witness counts, and local constraints do not charge **new gates in the Boolean function of the full table**. This does not show all lower-bound routes fail. It says any successful direct proof must extract more than input dependence, certificate width, cut information, or the existence of a selector. Any successful source route must preserve the exact Low/High promise and leave more than `N^(1+ε)` gates of source-hardness after paying for generation and decoding.

## 3. A more precise target: surplus beyond input support

For a separator circuit `C`, let `E(C)` be the number of essential table inputs and `S(C)` its total gate count. Define the residual

```text
Delta(C) = S(C) - E(C) + 1.
```

The connected output-cone graph gives `S(C)≥E(C)-1`, so `Delta(C)≥0`. C-403 supplies `E(C)≥N-O(N^β n)`. C-406 strengthens this structurally: if `μ(C)` is the gate-to-gate cycle rank, then `Delta(C)≥μ(C)`, and its formula transfer forces only `μ(C)=Omega(log N)` in the stated near-linear range.

This isolates the missing charge. Since `E(C)≤N`, an OPS lower bound `S(C)>N^(1+ε)` requires `Delta(C)>N^(1+ε)-N+1`. More precisely, if C-403 gives `E(C)≥N-a_N` for an explicit `a_N=O(N^β n)`, it suffices to prove

```text
Delta(C) > N^(1+ε) - N + a_N + 1
```

for every valid extension. This is not a literal post-read layer—DAG gates have no canonical time cut—but it is an exact measure of gates beyond the support floor. Current results force only logarithmic surplus in the near-linear regime. The target is therefore a promise-forced superlinear surplus, not another refinement of the support count.

Calibration is important: `AND_i(x_i OR y_i)` has all `N` inputs essential and only `N-1` gates, so `Delta=0`; parity has an `O(N)` circuit and `Delta=O(N)`. Neither is a GapMCSP separator. No general interaction or reconvergence statistic can exceed the needed scale on every Boolean function; the proof has to use the Low/High sandwich.

## 4. Fresh shared-work model: a gate-path protocol for Low versus High

Let `L=L_s1` and `H={y:CC(y)>s2}`. For every pair `(x,y)∈L×H`, define the valid output coordinates as `{i:x_i≠y_i}`. A valid separator `C` gives a deterministic gate-path protocol for this relation:

1. Alice holds `x`, Bob holds `y`; each locally evaluates the same separator DAG on their own table.
2. Start at the output gate, whose values differ (`1` on `x`, `0` on `y`).
3. At a NOT gate, descend to its input, which must also differ. At an AND gate, if the values are `(1,0)`, Bob selects an input that is `0` on `y`; if they are `(0,1)`, Alice selects an input that is `0` on `x`. At an OR gate, if the values are `(1,0)`, Alice selects an input that is `1` on `x`; if they are `(0,1)`, Bob selects an input that is `1` on `y`. The chosen child always has different values at the two endpoints.
4. The path ends at a primary table bit `i` with `x_i≠y_i`.

The path moves down the acyclic gate graph, so it visits at most `S(C)` gate states. Shared subcircuits are literally shared protocol states. This is a correct conversion from every separator; it does not assume that the separator itself outputs a witness.

This is a model for attacking gate reuse, not yet a lower bound. If one forgets that each state is a **one-sided Boolean gate function** and remembers only the pair sets on which its endpoint values differ, the model collapses: the root relation is covered by the `N` coordinate-disagreement sets, and an OR tree combines them in `O(N)` states. That relaxation is too weak. Conversely, if every state is required to be an arbitrary Boolean function on one table input, state complexity is just ordinary circuit complexity under another name. The useful middle ground would need a semantic progress measure on gate states that preserves one-sided gate composition, is bounded per AND/OR/NOT gate even with fan-out, and is forced to be superlinear by `L×H`.

Standard communication cost cannot supply that measure: a party can always send its `N`-bit table and the other party can find a differing coordinate, so communication is at most `N`. The gate-path formulation asks about the number and reuse pattern of distinct intermediate states, not the number of communicated bits. A gate-state lower bound for this specific relation remains open.

## 5. Strong construction test: a random affine slice is too easy or too costly

I tested whether a small affine family of tables can give a hard source trace. Fix one Low table `g` and choose a uniformly random `m`-dimensional linear subspace `U⊆F_2^N`. Circuit counting gives `|L_s2|≤2^{O(N^β n)}`. For any fixed nonzero vector `v`,

```text
Pr[v∈U] = (2^m-1)/(2^N-1) ≤ 2^{m-N+1}.
```

By a union bound, if `N-m > log2 |L_s2| + O(1)`, there is a choice of `U` for which `(g+U)∩L_s2={g}`. On this affine slice, the promise forces acceptance only at `g` and rejection at every other point; the induced partial function has the simple extension `y↦[y=0]`, using `O(m)` gates. It has no hard source label.

To encode the slice as `E(y)=g+My`, a generic dense `N×m` generator costs `O(Nm)` fan-in-two XOR/AND/OR gates. Taking `m` large enough to evade the singleton-label argument drives this map cost toward quadratic in `N`; taking `m` small leaves an easy singleton trace. This kills the naive random-affine-slice construction, not all succinct nonlinear maps. It pinpoints the requirement: a useful source family must have a **nontrivial, hard-shaped intersection** with `L_s1` while its other promised points lie in `H`, and the generator must leave a superlinear hardness margin after composition.

## 6. Current literature through 1 October 2026

The newest relevant results I checked do not change the unrestricted full-promise frontier:

- Korten's 30 September result uses Karchmer–Wigderson ideas to prove exponential lower bounds for parity at every fixed constant De Morgan depth. It supplies a useful top-down method in that restricted-depth setting, not a lower bound for unrestricted-depth GapMCSP separators. [ECCC TR26-221](https://eccc.weizmann.ac.il/report/2026/221/)
- Golovnev and Gurumukhani study local decision trees and prove strong bounds for an oblivious restricted variant; sufficiently strong general local-tree bounds would imply improved circuit lower bounds, but the conditional bridge is not an ordinary GapMCSP separator bound. [ECCC TR26-195](https://eccc.weizmann.ac.il/report/2026/195/)
- Rao proves `exp(Ω(sqrt(n)))` monotone lower bounds for bipartite perfect matching. This does not survive composition with an arbitrary nonmonotone separator; the project-specific model audit in C-436 remains applicable. [ECCC TR26-129](https://eccc.weizmann.ac.il/report/2026/129/)
- The constructive gate-elimination papers audited in C-445 yield refuters only at linear explicit-circuit thresholds, far below `s2=2^(βn)`.

These works are promising tools for restricted circuits and lower-bound methodology. None establishes the common-`ε`, sufficiently-small-`β` ordinary total-gate bound required by OPS.

## 7. Research decision after the audit

Retire as standalone mechanisms: input-support growth, certificate count/width, local incidence count, one-cut rank, generic K-W communication, direct mismatch enumeration, standard feasible interpolation, source maps whose table reveals the source output cheaply, and generic random affine restrictions. Their exact counterexamples or budget failures are recorded above and in C-403–445; do not reopen them by changing notation.

Keep two sharply stated avenues:

1. **Direct gate-surplus route:** prove a superlinear lower bound on `Delta(C)` for every Boolean extension with `L_s1⊆C^{-1}(1)⊆L_s2`, or construct a gate-state progress measure with the required per-operation and endpoint bounds. It must survive arbitrary DAG reuse and all middle-band extensions.
2. **Hard trace route:** give one explicit multi-output map `E` with cost `J`, prove `g(y)=1 ⇒ E(y)∈L_s1` and `g(y)=0 ⇒ E(y)∈H`, and show `CC(g)>J+N^(1+ε)` for a common fixed `ε` and all sufficiently small fixed `β`. Any decoder or query simulation is charged. It must avoid a singleton/easy trace and the C-442 predecoding trap.

The first avenue is the more direct target. The gate-path protocol gives a concrete language for its states, but the relaxed pair-cover model has an `O(N)` solution and no superlinear state measure has been proved. The next cycle should begin by testing a specific Karchmer–Wigderson/top-down potential against the full pair relation and the parity/repeated-block/sparse-check calibrations; if it reduces to communication bits or arbitrary pair covers, retire it immediately. Keep the hard-trace route as a backup only if a concrete succinct family is found.

**Frontier unchanged:** ordinary `S≥N-O(N^β n)-1` plus C-406's logarithmic surplus; OPS `S>N^(1+ε)` remains open with one fixed `ε>0` for every sufficiently small fixed `β>0`; exact full-promise upper `O(N·2^{O(N^β)})`; native `ρ≥N-o(N)` remains separate. No P-vs-NP proof or breakthrough has been obtained.
