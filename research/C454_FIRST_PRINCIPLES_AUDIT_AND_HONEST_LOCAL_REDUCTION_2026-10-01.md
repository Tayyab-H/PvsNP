# C-454 — first-principles audit and the exact locality boundary

**Date:** 1 October 2026  
**Question:** What can a rigorously stated local-dependence mechanism say about shared computation for the OPS Gap-MCSP promise, and what does it teach us about the project’s unresolved lower bound?  
**Result:** A primary theorem of Allender–Ilango–Vafa rules out every nonuniform AC0 many-one reduction from PARITY to the exact OPS gap, for each fixed sufficiently small beta. Its disjoint-perturbation proof gives a precise sharing-safe obstruction for honest NC0 table generators. This is a reduction barrier, not an ordinary circuit lower bound for a Gap-MCSP separator. The project-wide quantitative frontier is unchanged.

## 1. The exact object, without a canonical middle-band answer

For a table `T` of length `N=2^n`, let `CC(T)` be minimum fan-in-two AND/OR/NOT gate count. Write

```text
s1 = floor(N^beta/(c n)),    s2 = floor(N^beta),
YES = {T : CC(T) <= s1},     NO = {T : CC(T) > N^beta}.
```

The harmless floor convention can be changed by constant-size threshold adjustments. The middle band is unspecified. A separator is any total Boolean function `F:{0,1}^N -> {0,1}` satisfying `F(T)=1` on YES and `F(T)=0` on NO. Thus the direct target is the minimum ordinary total-gate complexity over **all** such extensions. No witness, circuit description, or fixed answer on the middle band is part of the definition.

OPS Theorem 1.4 uses one universal constant `c` and states that if one fixed `epsilon>0` works for every sufficiently small fixed `beta>0`, then the gap problem has no size-`N^(1+epsilon)` circuit and `NP` is not contained in `P/poly`. The theorem counts total ordinary Boolean gates, with arbitrary depth and fan-out. Its conclusion is stronger than `P != NP`. The current proved ordinary floor is still `N-O(N^beta log N)-1` (with the C-406 refinement); the requested common-fixed-epsilon surplus is open. [OPS, Theorem 1.4 and Definition 2.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).

## 2. A precise mechanism for local source maps

The mechanism is **disjoint-perturbation majority stability**. It charges no gates to source constraints; instead it uses the fact that each output table bit of a local map can notice only a bounded number of disjoint source perturbations.

Let `Pi=(Y,NO)` be a promise on `m`-bit strings. Its zero block sensitivity at a NO input `x` is the maximum `r` for which there are pairwise-disjoint coordinate sets `B_1,...,B_r` such that `x^{B_j}` is in `Y` for every `j`; `x^{B_j}` denotes flipping exactly the coordinates in `B_j`.

**Lemma (Allender–Ilango–Vafa, honest NC0 form).** Fix depth `d` and a function `eta(theta)=o(theta)`. Suppose a nonuniform NC0 many-one reduction maps every length-`m` source input to `(T_x,theta_m)`, with one common threshold `theta_m` for all inputs of that length, and each output bit of `T_x` depends on at most `2^d` source bits. If `theta_m >= log log m` and the reduction maps source YES to `CC(T)<=eta(theta_m)` and source NO to `CC(T)>theta_m`, then for all sufficiently large `m`, every NO input has zero block sensitivity less than `2^(d+1)+1`.

**Proof.** Suppose a NO input `x` has `r=2^(d+1)+1` disjoint YES perturbations `B_j`. Let `D_j` compute `T_{x^{B_j}}`; each has at most `eta(theta_m)` gates. For an address `a` of the target table, the output bit `T_x[a]` depends on a set `W_a` of at most `2^d` source coordinates. Since the `B_j` are disjoint, at most `2^d` of them intersect `W_a`. For every other `j`, locality gives `T_{x^{B_j}}[a]=T_x[a]`. Therefore the majority of `D_1(a),...,D_r(a)` equals `T_x[a]`, simultaneously for every address `a`. A fan-in-two circuit for the majority table uses at most `r eta(theta_m)+2r` gates. Since `eta(theta)=o(theta)` and `theta_m` grows, this is less than `theta_m` for all sufficiently large `m`, contradicting the NO endpoint. The copies may share in a smaller implementation; summing their sizes is already a valid upper bound. This proof neither reconstructs a witness nor assumes an address checker beyond the input table of the reduction.

The conclusion is a constant bound depending on map depth, **not** a superlinear gate lower bound on the OPS separator. This is the central scope restriction.

## 3. Exact instantiation at OPS thresholds

For each fixed `0<beta<1` and table arity `n`, set `z=2^(beta n)` and `theta_n=floor(z)`. Define

```text
eta_beta(t) = floor(2 beta t/(c log_2 t))  for t>=2.
```

Then `eta_beta(t)=o(t)`. For large `n`, `theta_n>=z/2` and `log_2(theta_n)<=beta n`, so

```text
eta_beta(theta_n) >= floor(z/(c n)) = s1,
theta_n <= z.
```

Consequently every OPS-YES table is an `eta_beta(theta_n)`-GapMCSP YES instance, and every OPS-NO table (`CC(T)>z`) is an `eta_beta(theta_n)`-GapMCSP NO instance (`CC(T)>theta_n`). The threshold `theta_n` is fixed within each table length, as required for an honest reduction. Thus any AC0 many-one reduction from PARITY to the fixed-beta OPS promise would give a reduction from PARITY to `eta_beta(theta)`-GapMCSP for an `o(theta)` function. Allender–Ilango–Vafa's Theorem 1 rules this out. Their proof handles the parameter field and reduces AC0 maps to the needed local form; the corollary does not assume every reduction is already NC0. [Allender, Ilango, and Vafa, Theorem 1 and Lemma 6](https://people.cs.rutgers.edu/~allender/papers/ilango.vafa.pdf).

**Established result / project corollary:** for every fixed sufficiently small `beta`, PARITY has no nonuniform AC0 many-one reduction to the OPS promise at that beta. This is a direct parameter translation of published work, not a new lower bound and not evidence that a general ordinary source map is impossible.

## 4. Required canaries and cheapest shared computations

These examples test what block sensitivity does and does not buy. Each has many disjoint repairs, so the local-map theorem applies; each also has a linear-size ordinary checker, so the theorem cannot be reinterpreted as a general computation-cost charge.

| Source promise | Disjoint repairs at a NO input | Cheapest relevant shared computation |
|---|---|---|
| `m`-bit PARITY, YES = odd | At an even input, each singleton flip is a disjoint YES block; `bs_0=m`. | An XOR chain computes parity in `m-1` XOR gates, hence `O(m)` AND/OR/NOT gates. |
| Repeated-pair equality, YES iff `u_i=v_i` for all `i` | At the input with every pair unequal, flipping each pair is a disjoint YES block; `bs_0=m`. | Compute each equality and combine them in `O(m)` gates. |
| Disjoint width-three parity checks, YES iff every local XOR is zero | Give each check the pattern `100`; flipping its first coordinate fixes it, yielding one disjoint singleton repair per check. | Compute all constant-width checks and their conjunction in `O(m)` gates. |
| Global repeated-block relation, YES iff `x^j=x^1 xor r_j` for fixed masks `r_j` | Set every later block to the complement of its required value; flipping each whole later block repairs it independently. | Compare each block against the shared reference and mask in `O(m)` gates. |

These are counterexamples to the inference “many repairs or local constraints force large computation.” They are **not** counterexamples to the lemma, whose claim is only that a bounded-locality source map cannot turn such a high-block-sensitivity promise into the required growing circuit-size gap. They are also not hard source problems.

The strongest warning about relaxing the model is already in C-417: a two-gate multi-output map can route one source bit to either the all-zero table or a fixed High table by encoding the table in its `N` output-wire choices. Its gate count does not include the `Theta(N)`-bit router description. This defeats gate-only accounting for vector-output maps, but is not a useful hard-source reduction. Gates, wires, description bits, and construction time remain distinct.

## 5. Paired attempt to construct a full-promise separator

The exact Low-description enumerator accepts `T` iff some fan-in-two circuit of size at most `s1` computes it. It accepts every YES and rejects every NO, with arbitrary middle-band behavior. If `K=2^(O(s1 log(s1+n)))=2^(O(N^beta))` descriptions are enumerated and each candidate is compared against all `N` bits, the total cost is `O(N 2^(O(N^beta)))` ordinary gates. This is still the best unconditional full-promise upper construction in the project. The local-map theorem supplies no compression of that enumeration: it rules out one source-reduction architecture, not a full-table separator. The OPS anti-checker construction gives a near-linear separator **under** `NP subseteq P/poly`, as expected from the contrapositive of magnification; it is not an unconditional improvement. No near-linear full-promise separator was found in this cycle.

## 6. First-principles synthesis across the project

The attempts fall into three classes, and the distinction matters:

1. **Semantic necessity:** a separator must depend on almost every table bit; Low/High interpolation, endpoint perturbations, and exact promise restrictions establish this. They yield the near-linear floor but not more than linear gate work.
2. **Representation proxies:** support, certificate counts, description entropy, local incidence, block sensitivity, communication rank, symmetry, and many structured witnesses can all coexist with `O(N)` shared circuits or have a linear ceiling. They can falsify a proposed mechanism, but do not charge arbitrary reusable DAG gates.
3. **Actual computation cost:** an ordinary separator has one output and unrestricted intermediate sharing. This is the only resource measured by OPS. Every source-map proposal must preserve both endpoints and leave the strict budget `CC(source) > generator + N^(1+epsilon) + postprocessor`; every direct proof must show an operation-wise gate-growth bound and a superlinear value forced by the full promise. Neither obligation has been discharged.

The new literature result sharpens the map route's boundary: **a successful parity-based encoding must be nonlocal**. It does not explain how arbitrary-depth sharing should be charged. Chen et al.'s locality barrier is different: it describes why certain weak-model lower-bound techniques transfer to magnification reductions with local oracle gates. Neither result is a universal barrier to ordinary-circuit lower bounds. [Chen et al., *Beyond Natural Proofs: Hardness Magnification and Locality*](https://doi.org/10.1145/3538391).

**What appears to be missing:** not a forgotten count of constraints, nor a need to increase repetition. The missing theorem remains a promise-forced superlinear lower bound on reusable ordinary gate work, or a costed nonlocal reduction whose hard-source margin survives its generator. The evidence does not establish that such a theorem is impossible; it does show that local structure and shallow encodings do not supply it. OPS proves a route to `NP not subseteq P/poly`, which is stronger than the original `P != NP` goal, so a direct uniform route would be a distinct objective rather than an interchangeable weaker version.

**Next research filter:** before developing any new statistic, write (i) its value on an arbitrary total separator DAG, (ii) the exact change under AND, OR, and NOT with unrestricted fan-out, (iii) why every full-promise extension has a superlinear terminal value, and (iv) its parity/equality/sparse-check/global-relation counterexamples. For a reduction, state the map's locality/description model and exact `generator + separator` margin first. If either endpoint or the gate budget is unproved, classify it as a route diagnostic, not progress on the quantitative frontier.

## 7. Claim status and frontier

- **Published:** OPS Theorem 1.4; Allender–Ilango–Vafa's non-hardness theorem for `o(theta)`-GapMCSP under AC0 many-one reductions; Chen et al.'s technique-specific locality barrier.
- **Project-derived corollary:** fixed-beta OPS thresholds are an `o(theta)` GapMCSP target, so PARITY cannot reduce to them via nonuniform AC0 many-one maps.
- **Countertests:** all four required structured promises have many disjoint repairs but linear-size checkers; C-417's two-gate routed map shows why output labels need separate accounting.
- **Failed transfer:** bounded locality does not model arbitrary ordinary reductions or the separator itself.
- **Quantitative effect:** none. Ordinary lower bound stays `N-O(N^beta log N)-1` plus C-406's refinement; the common-fixed-epsilon OPS target remains open; exact full-promise upper remains `O(N 2^(O(N^beta)))`; native `rho>=N-o(N)` is separate. No P-vs-NP proof or near-linear unconditional full-promise separator has been obtained.

### Primary literature

- Allender, Ilango, Vafa, [*The Non-Hardness of Approximating Circuit Size*](https://people.cs.rutgers.edu/~allender/papers/ilango.vafa.pdf), Theorem 1, Lemma 6, and Definitions 2–3.
- Oliveira, Pich, Santhanam, [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and Definition 2.4.
- Chen, Hirahara, Oliveira, Pich, Rajgopal, Santhanam, [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://doi.org/10.1145/3538391).