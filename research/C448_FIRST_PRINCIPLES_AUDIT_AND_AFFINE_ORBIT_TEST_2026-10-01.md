# C-448 — Integrated first-principles audit and affine-orbit normalization test

**Date:** 1 October 2026  
**Status:** synthesis of the current repository plus one new, fully costed normalization attempt. No P-vs-NP proof and no quantitative frontier change.

## 1. The exact question

Let `N=2^n`, let `L_t` denote the set of truth tables of `n`-input fan-in-two Boolean circuits with at most `t` AND/OR/NOT gates, and set

```text
s1 = N^beta/(c n),          s2 = N^beta,
L  = L_s1,                  H = {T : CC(T)>s2}.
```

The ordinary separator target is

```text
SepCC(N,beta) = min { CC(F) : L ⊆ F^{-1}(1) and F^{-1}(1) ⊆ L_s2 }.
```

This formula is the right first-principles object: a separator must accept every Low table and reject every High table, while its values in the middle band are free. No witness, circuit description, or mismatch address is required as output. OPS magnification needs one fixed `epsilon>0` such that for every sufficiently small fixed `beta>0`, `SepCC(N,beta)>N^(1+epsilon)`; Theorem 1.4 then gives `NP not⊆P/poly`. Its one-common-`epsilon` quantifier is essential. [Oliveira–Pich–Santhanam, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf).

The current ordinary lower bound remains `N-O(N^beta log N)-1`, with C-406's logarithmic reconvergence refinement. The exact full-promise upper bound remains `O(N·2^{O(N^beta)})`, obtained by enumerating all Low-circuit descriptions and checking their full tables. The native fusion frontier `rho_GapMCSP≥N-o(N)` concerns a separate measure; no ordinary-gate compiler closes that gap.

## 2. What the accumulated evidence actually says

The rows below consolidate existing project results; they do not claim to re-prove every historical report. They identify whether a route lacks a proof, fails a transfer, or measures the wrong resource.

| Route family | Established result | Exact point where it stops |
|---|---|---|
| Input support, subcubes, sensitivity, Hamming margins (C-403, C-406, C-426) | Nearly all `N` table inputs are essential; fan-in-two size is at least `N-O(N^beta log N)-1`; formula structure adds only a logarithmic surplus in the audited range. | These charge how many input bits matter, not the superlinear work of combining them. Their natural information ceilings are linear. |
| Certificates, pivots, anti-checkers, local constraints (C-421–429) | High tables admit semantic mismatch evidence; fibers and local patterns obey useful restrictions. | Correctness does not make the circuit emit its evidence. Transcript cells can be made singletons with `O(N)` copy gates before an unrestricted decoder; local certificate counts do not price that decoder. |
| Communication, rank, DAG-KW, rectangle potentials (C-159, C-232, C-435, C-447) | Gate-path protocols preserve shared circuit states; the partial promise's rectangle DAG is equivalent to ordinary separator circuits up to terminal overhead. Cut rank yields a valid but linear ceiling. | Communication bits and coordinate covers forget internal gate semantics; rectangle area duplicates shared states along paths. This is a representation of the original lower bound, not an easier model. |
| Comparator/formula/constant-depth lower bounds (C-406, C-434; recent Korten TR26-221) | Promise-specific comparator lower bound `N^(1+0.455 beta)` is proved; formula and constant-depth methods yield stronger bounds in their own models. | Comparator exponent shrinks with `beta`; fan-out is restricted. Formula unrolling can cost `2^mu`. Korten's recent parity theorem is for constant-depth De Morgan circuits and does not bound arbitrary-depth separators. No justified normalization puts a small arbitrary DAG in those models. [Korten, ECCC TR26-221](https://eccc.weizmann.ac.il/report/2026/221/). |
| Source-hardness reductions (C-430–442) | Composition inequalities with all generator and decoder gates paid are valid; C-442's predecoding lemma is general. Some source lower bounds are near-maximum. | Candidate tables are Low on both sides, the source answer is cheaply decodable from the table, the source hardness is for the wrong circuit model, or the certified gap misses OPS's threshold ratio. Query-by-query addition is only an upper bound; unrestricted circuits can share work jointly. |
| Logic/proof complexity (C-443–445) | The endpoints have exact `exists-description/forall-address` versus `forall-description/exists-mismatch` polarity. Short refutations define an NP subset of High. | Standard interpolation has the proof-to-circuit direction; no hard refutable High family or arbitrary-separator-to-proof implication has been established. Per-description refutation is not a valid universal certificate. |
| Native cyclic fusion (C-74 onward) | A separate cyclic/closure measure has meaningful `N-o(N)` lower bounds under its stated endpoint, reuse, and cycle rules. | `q^2` paid-AND unrolling is not a `q^2` total-gate compiler; rank/support routing can raise binary-DAG cost to `O(q^3/log q)`. Native and ordinary targets remain distinct. |

### First-principles synthesis

These are not hundreds of independent proofs that P versus NP is unusually resistant. Most failures group into three repeated debts:

1. **Promise debt:** a reduction or argument must be right on *every* required Low and High input. Hard witnesses, one chosen circuit, or a correct answer on only part of the source domain do not suffice.
2. **Sharing debt:** any per-candidate, per-address, per-query, per-certificate, or per-copy charge must survive arbitrary reuse. A sum of separate costs is not a lower bound on a joint circuit.
3. **Quantifier/model debt:** the OPS consequence is a fixed positive exponent for all small fixed `beta`, against ordinary total gates with unrestricted fan-out. A beta-dependent gain, formula lower bound, comparator result, or native-closure theorem does not meet that statement without a proved compiler.

The failures are therefore not evidence that no proof exists. They do show that support size, local richness, entropy, certificate width, and short communication cannot be renamed into a superlinear gate charge. Any new invariant must have (i) a numerical value on actual gate functions, (ii) a proved AND/OR/NOT growth rule valid with unrestricted fan-out, and (iii) a value greater than `N^(1+epsilon)` forced by the Low/High sandwich for every valid extension. Any reduction must instead pay the complete table generator, address circuitry, source-query simulation, and decoder while preserving both endpoints.

## 3. New mechanism tested: address-affine orbit symmetrization

**Idea.** Low and High circuit-complexity classes are nearly invariant under affine changes of the truth-table address: precomposing an `n`-input truth table by `x↦Ax+b` changes circuit size by at most `O(n^2)` gates. Perhaps a separator can first be replaced by an affine-invariant separator and then analyzed using its orbit structure.

Write `G=AGL(n,2)` and let `(g·T)(x)=T(g^{-1}x)`. For each fixed `beta>0`, take `n` sufficiently large that `s1>K n²`. There is an absolute constant `K` such that

```text
CC(g·T) ≤ CC(T)+K n^2,
CC(T)  ≤ CC(g·T)+K n^2,
```

because each affine input bit can be computed from the `n` address bits with `O(n)` XOR gates, and XOR has a constant-size AND/OR/NOT implementation. Define the shrunken endpoint cores

```text
L^- = L_{floor(s1)-K n^2},
H^+ = {T : CC(T)>s2+K n^2}.
```

For any separator `F` of `(L,H)`, define

```text
F_G(T) = AND_{g∈G} F(g·T).
```

On every `T∈L^-`, every orbit member is in `L`, so all terms are `1`. On every `T∈H^+`, every orbit member is in `H`, so all terms are `0`. Reindexing the product proves `F_G` is invariant under all of `G`. This is a valid separator for the cores; the proof uses no assumed witness behavior.

**Gate cost.** An affine address transformation is just a permutation of the `N` input wires to a copy of `F`, so it takes no Boolean gates under the stated total-gate measure. The explicit construction has

```text
CC(F_G) ≤ |G|·CC(F)+(|G|-1),
|G| = 2^n |GL(n,2)| = 2^{n^2+n+O(1)} = Θ(N^{n+1}).
```

Thus this direct normal form multiplies the separator size by `Theta(N^{n+1})`, far too expensive for the near-linear target. Restricting to translations still has `|G|=N`, and the complement symmetrization from C-447 is the constant-size special case with cost `2S+O(N)`.

**Counterchecks.** Affine invariance by itself is not a gate lower bound: parity of the `N` table bits is invariant under every permutation of the table coordinates and has an `O(N)` circuit. C-160 is stronger as a promise calibration: its complement-closed two-tail Hamming promise has a fully permutation-invariant `O(N log N)` separator while matching many generic richness and stability statistics. Those are counterexamples to the *mechanism*, not to the actual Gap-MCSP promise. The orbit symmetrization proves no invariant separator lower bound and constructs no full-promise separator.

**Requested construction canaries for generic locality/constraint charges.** These do not refute the orbit lemma itself; they test the recurring inference that many local constraints, correlated blocks, or visible violations force many gates.

* Repeated-block equality, `E(T)=AND_{i<N/2}[T_i=T_{i+N/2}]`, costs `O(N)` gates: one constant-size XOR/equality test per pair and one AND reduction.
* For a fixed sparse parity-check matrix `H` with `M` nonzero entries and `r` rows, checking `HT=0` over `GF(2)` costs `O(M+r)` gates: compute each row parity, then AND the zero tests. In particular, `M,r=O(N)` gives a linear-size checker. This claim is only for sparse `H`; dense checks are not covered.
* A block generated by a simple global relation can also be checked linearly. For example, for `A,B∈{0,1}^{N/2}`, the relation `B_i=A_i XOR A_{i+1 mod N/2}` is verified with `O(N)` gates. More generally, any supplied relation circuit with `O(N)` total gates gives an `O(N)` consistency check.

These are counterexamples to generic constraint-count/local-violation charging, not counterexamples to Gap-MCSP: no claim is made that these predicates separate every required Low table from every required High table. The decisive missing step remains connecting endpoint correctness to the cost of an arbitrary shared separator.

**Disposition.** Retire direct orbit averaging as a route to a near-linear normal form. This does not rule out a more efficient, structure-aware symmetrization; no such compiler has been proved. The failure is an explicit group-size cost, not a universal barrier theorem.

## 4. Near-linear full-promise construction attempt

The natural exact construction remains

```text
F(T) = OR_{d: |d|≤s1} AND_{a∈{0,1}^n} [T[a]=Eval(d,a)].
```

It accepts every Low table and rejects every High table and uses `O(N·2^{O(N^beta)})` total gates. Shared address decoding or a prefix trie does not remove the existential disjunction over all descriptions; no worst-case factoring to `N^(1+o(1))` was found. Affine orbit averaging above is not an upper-bound improvement. A small circuit for the full promise remains possible, but none has been constructed here.

## 5. Barriers, literature, and originality

The Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam locality barrier applies to particular magnification techniques that extend to small-fan-in oracle circuits; it explains why those methods cannot directly meet their magnification target. It is not a proof that every nonlocal, global, or source-specific route is impossible. [Primary paper, JACM 2022](https://doi.org/10.1145/3538391).

The September 30 Korten result provides a fresh top-down method for constant-depth parity lower bounds. Its high-entropy projection argument is a possible source of tools, but current separators have arbitrary depth; the repository contains no cost-preserving reduction from that general DAG model to fixed depth. ECCC TR26-222's random-linear-code discrepancy results concern list decoding/list recovery; no embedding of those code families into the exact Low/High promise or separator relation is present. These reports add no OPS bound in their current form. [Korten, ECCC TR26-221](https://eccc.weizmann.ac.il/report/2026/221/), [Doron et al., ECCC TR26-222](https://eccc.weizmann.ac.il/report/2026/222/).

The DAG-KW equivalence, cut-rank limitation, affine slice failure, source predecoding budget, comparator gap lower bound, and native/ordinary separation are existing project results, not new discoveries of C-448. C-448 contributes an integrated dependency audit and a proved cost calculation for one new orbit-normalization attempt.

## 6. Exact effect and next research choice

**Strongest proved statements used:** ordinary separator size `N-O(N^beta log N)-1` plus the C-406 logarithmic refinement; comparator promise lower bound `N^(1+0.455 beta)` for each fixed `beta<1/2`; native `rho_GapMCSP≥N-o(N)` in its separate model. The exact total-gate upper bound is `O(N·2^{O(N^beta)})`.

**Quantitative frontier:** unchanged. No common-fixed-`epsilon` ordinary lower bound, no near-linear full-promise separator, and no P-vs-NP proof has been obtained.

**Decision:** do not start another generic state-capacity, entropy, or symmetry lemma. The most productive next attack is to revisit the *source-map* route only if an encoder can make both endpoint implications true without revealing the source label through an `O(N)` decoder or paying the source hardness in the generator. In parallel, a direct invariant is admissible only after an explicit gate recurrence and a promise-derived superlinear output value are both written down. The present audit has not produced that missing object; the objective remains open.

The exact source-map target is as follows. Let `(A,B)` be a source promise on `m`-bit strings with partial Boolean function `h` (one on `A`, zero on `B`), and define `CC_{A,B}(h)` as the minimum total gate count of a circuit agreeing with `h` on `A∪B`. Let `G:{0,1}^m→{0,1}^N` be a multi-output table generator computable by one shared circuit of `g` gates. Require `x∈A ⇒ G(x)∈L_{s1}` and `x∈B ⇒ CC(G(x))>s2`. Then every valid Gap-MCSP separator `F` induces `h(x)=F(G(x))` on `A∪B`, with a circuit of at most `CC(F)+g` gates. Consequently `CC_{A,B}(h)≤CC(F)+g`; a source lower bound `CC_{A,B}(h)>N^{1+ε}+g` would force `CC(F)>N^{1+ε}`. The map must preserve both endpoints for every source-promise input, and its generator cost is paid in full. This is a precise transfer criterion, not a construction: the project currently has no such map and no source lower bound meeting this budget.
