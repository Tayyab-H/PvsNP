# C-465 - First-principles audit and the average-case MCSP consequence

**Date:** 1 October 2026  
**Status:** cumulative evaluation plus a proved density/average-case implication. No improvement to the circuit frontier.

## 1. Exact question

Let `N=2^n`, `tau=N^beta`, and use the OPS parameters

```text
s1 = tau/(10n),     YES: CC_n(T)<=s1,
                    NO:  CC_n(T)>tau.
```

The middle band is unrestricted. For integer circuit complexity, the tables not in the formal NO set have complexity at most `floor(tau)`. A total separator is exactly a fan-in-two AND/OR/NOT circuit `F` satisfying

```text
1[CC(T)<=s1] <= F(T) <= 1[CC(T)<=floor(tau)]  for every N-bit table T.
```

OPS show that if one fixed `epsilon>0` gives a lower bound `N^(1+epsilon)` for every sufficiently small fixed `beta`, then `NP` is not contained in `P/poly`. This is a strong sufficient route to `P!=NP`, not an equivalence with `P!=NP`. The cited theorem uses the `10n` denominator and strict `CC>tau` NO endpoint. [OPS, Theorem 1.4 and Definition 2.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)

## 2. New exact consequence: every small separator solves MCSP on almost all random tables

Circuit-description counting gives a constant `a` such that the number of `n`-input functions of circuit size at most `floor(tau)` is at most

```text
K_tau <= 2^(a*tau*log_2(n+tau)).
```

Since `beta<1` is fixed, `tau*log(n+tau)=O(N^beta*n)=o(N)`. Thus a uniformly random N-bit table is formally NO with probability at least

```text
1 - 2^(-N + O(N^beta*n)).
```

This remains true inside any cylinder fixing `m` entries. For a fixed partial assignment `rho` on `m` coordinates and a uniformly random completion `T`,

```text
Pr[CC_n(T)<=floor(tau) | T extends rho]
    <= min(1, 2^(a*tau*log_2(n+tau) - (N-m))).
```

In particular, if `m=O(tau)`, almost every completion is a formal NO, independent of the values fixed by `rho`.

Now let `F` be any valid separator and define an algorithm for ordinary `MCSP[s1]` with an abstention symbol `?`:

```text
A_F(T) = 0  if F(T)=0,
         ?  if F(T)=1.
```

It never errs. If `CC(T)<=s1`, then `F(T)=1` and `A_F` abstains. If `F(T)=0`, the table cannot be Low, so the correct threshold-MCSP answer is NO. Its success probability under a uniform truth table is exactly `Pr[F(T)=0]`, and

```text
Pr[F(T)=1] <= K_tau/2^N <= 2^(-N+O(N^beta*n)).
```

Therefore every separator of size `S` induces, with no meaningful gate overhead, a zero-error average-case `MCSP[s1]` solver of size `S` whose success is `1-2^(-N+O(N^beta*n))`. Equivalently, `R_F={T:F(T)=0}` is a dense property of truth tables, disjoint from every circuit of size at most `s1`, and computable by the same circuit family.

This is a **sufficient lower-bound route**: it would suffice to prove that no `N^(1+epsilon)`-size circuit can be a zero-error average solver of this strength at the OPS low thresholds. This solver specification is weaker than full promise separation, so excluding all such solvers is a stronger lower-bound theorem. The reverse implication is not proved: an average solver may abstain on some promised High tables, so it need not be a Gap-MCSP separator.

## 3. Test: random completion is maximally uninformative

The cylinder bound also kills a randomized version of C-464's completion query. If a candidate certificate fixes only `O(tau)` table entries, a uniformly random filling is High with probability `1-2^(-N+O(tau*n))`, no matter whether the original table was Low or High. A valid separator therefore outputs zero on such a random query with overwhelming probability for either source case. Random completion does not retain the label of the original table.

This is stronger than the deterministic middle-completion counterexample in C-464, but it still does not rule out a carefully constructed completion, a promised-query gadget, or a non-black-box reduction. It identifies the exact failure: the ambient truth-table cube is an overwhelmingly High sea, so an unstructured completion query loses the exceptional low-table information.

## 4. First-principles synthesis of the cumulative record

| Obligation | Strongest verified result | What remains missing |
|---|---|---|
| Direct ordinary-gate lower bound | C-403 forces `N-O(N^beta*n)` essential inputs and hence linear total gates. | Gates beyond the `N` input-coordinate floor. |
| Control arbitrary DAG sharing | C-406 unfolds the DAG to a formula with a `2^mu` factor and forces only `Omega(log N)` gate-to-gate reconvergence in the near-linear regime. | A promise-forced superlinear gate charge that survives unrestricted fan-out. |
| Semantic/geometric invariants | Support, degree, rank, Hamming robustness, local repairs, and certificate lengths have been paired with linear-size counterexamples or incomplete filters (C-435, C-456-C-459, C-462). | A statistic whose value is forced for every total extension and whose gate cost is charged under reuse. |
| Anti-checker search | C-464 proves an `O(N^beta)` anti-checker cylinder can contain both a middle table and an actual NO table. C-465 shows random fillings are almost always NO even for cylinders unrelated to the input label. | Queries forced to YES/NO, or a separator-independent way to use the certificate. |
| Source transfer | Composition is sharing-safe when endpoints are exact, but prior maps leak the source label, fail an endpoint, or spend the lower-bound margin on generation/decoding (C-441-C-455). | A hidden-label map with both endpoints and `hardness > generator + separator + postprocessing`. |
| Complete upper bound | Exact low-description enumeration is a valid `O(N*2^(O(N^beta)))` total-gate separator. | A proved shared-gate compression or a near-linear full-promise separator. |
| Native fusion model | The separate native frontier remains `rho_GapMCSP >= N-o(N)`. | No ordinary compiler follows from paid-AND unrolling; arbitrary endpoints, wide seeds, reuse, cycles, and all semi-filter extensions must remain explicit. |

These are several different obstacles. The most repeated failure is semantic information without an arbitrary-sharing gate inequality, but source transfer, middle-band labels, codebook compression, and native-to-ordinary transfer are independent obligations. A short omitted counting lemma is unlikely to cross all of them at once.

The current worktree also contains the audited Gemini salvage file. Its valid native-model result is the C-125 Universal Decoder inequality `CycAnd(f)<=a+M*delta+N`, where `a` is the map's paid-AND cost, `M` is the number of selected Low-witness restrictions on their varying coordinates, and `delta` is the number of such coordinates. This closes the low-diversity transfer branch: if `M*delta` is small relative to source complexity, the map itself spends the margin. The high-diversity branch remains open because many output patterns do not by themselves imply many shared AND states. The exact single/multi-hole consistency and owner-mask splice criteria are also valid, but a simple owner mask is an assumption, and proof-tree leaves do not count distinct reusable closure rules. These are native-model facts; no compiler transfers them to ordinary total gates. They leave the active ordinary target unchanged. See [Gemini salvaged results](../Gemini/GEMINI_SALVAGED_RESULTS.md).

## 5. What the literature check changes

The implication from a separator to a dense, useful property is a direct project derivation, not a new natural-proofs theorem. Hirahara and Santhanam establish close equivalences between average-case MCSP easiness and natural properties for parameter ranges and quantifiers stated in their paper. Their result makes this a recognized lens, but no automatic converse turns an average solver into a full-promise separator, and the middle-band endpoints and every constant rescaling must be checked before importing their theorem. [Hirahara-Santhanam, *On the Average-Case Complexity of MCSP and Its Variants*, Proposition 12](https://drops.dagstuhl.de/storage/00lipics/lipics-vol079-ccc2017/LIPIcs.CCC.2017.7/LIPIcs.CCC.2017.7.pdf)

The natural-proofs barrier is conditional and technique-specific. It does not rule out the OPS lower bound, but it warns that an efficiently constructible dense property against circuit functions is exactly the kind of object that pseudorandom functions can obstruct. [Razborov-Rudich framework as discussed by OPS](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf); [Chen et al., locality barrier](https://eccc.weizmann.ac.il/report/2019/168/download)

## 6. First-principles judgment and next research filter

There is no evidence that one hidden elementary fact has been overlooked. OPS's target would establish the nonuniform separation `NP not subseteq P/poly`, which is stronger than merely `P!=NP`. The productive conclusion is not that the problem cannot be solved; it is that the project must seek a genuinely new bridge at one of three interfaces:

1. **Average-case route:** prove a fixed-epsilon lower bound for zero-error average-case `MCSP[s1]` at the OPS scale. The solver task allows abstention and only requires high success on uniform inputs; ruling out that larger class of solvers is a stronger lower-bound claim than ruling out separators, but it suffices.
2. **Direct-DAG route:** prove a promise-forced surplus over the `N-O(N^beta*n)` essential-input floor for every total extension, with an operation-wise bound valid under arbitrary sharing.
3. **Reduction route:** encode an NP-hard source into the Low/High codebooks with the source answer hidden from the generator, exact endpoint preservation, and all multi-output and decoder gates charged.

Do not return to uniform random filling, generic certificate length, local inconsistency counts, or a canonical extension alone. Pair each new lower-bound attempt with a full-promise separator construction and state whether it improves total gates, paid AND states, wires, description bits, or runtime.

**Strongest result this cycle:** the cylinder density inequality and its zero-error average-MCSP consequence.  
**Quantitative frontier:** unchanged. Ordinary lower bound `N-O(N^beta*log N)`; complete upper bound `O(N*2^(O(N^beta)))`; OPS common-fixed-epsilon target open; native `rho` separate. No P-vs-NP proof.
