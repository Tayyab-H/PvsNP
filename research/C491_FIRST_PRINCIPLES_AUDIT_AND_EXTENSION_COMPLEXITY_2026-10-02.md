# C-491 — First-principles audit: the minimum-extension problem is the target

**Date:** 2 October 2026  
**Status:** project-wide audit and correction of an encoding-cost overgeneralization; no new lower-bound theorem.

## 1. Start from the quantified statement

Let `N=2^n`, `s1=floor(N^beta/(10n))`, and `s2=N^beta`, for a fixed small `beta>0`. Define

```text
Y = {T in {0,1}^N : CC_n(T) <= s1}
Z = {T in {0,1}^N : CC_n(T) > s2}.
```

A valid full-promise separator is any total Boolean function `F` satisfying

```text
Y subseteq F^(-1)(1) subseteq {0,1}^N minus Z.
```

The middle band has no prescribed labels. The exact ordinary-circuit target is therefore

```text
SepCC(Y,Z) = min { CC_N(F) : F total and Y subseteq F^(-1)(1) subseteq complement(Z) }.
```

The OPS magnification premise is that one fixed `epsilon>0` works for every sufficiently small fixed `beta>0`, with `SepCC(Y,Z)>N^(1+epsilon)`. The paper states a universal constant `c` in the low threshold `2^(beta*n)/(c*n)`; its proof instantiates the displayed `10*n` denominator used in this repository. Under those quantifiers, the theorem implies `NP` is not contained in `P/poly`. This is already a major unrestricted-circuit lower bound, not a routine completion of the existing linear floor. [OPS, Theorem 1.4 and proof](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)

## 2. First-principles audit of the accumulated attempts

The reports from C-1 through C-490 are most informative when grouped by what they actually measure.

1. **Input information reaches the linear scale.** Essential support, sketches, cylinders, and one-cut communication views show that nearly all table coordinates can matter. But a fan-in-two DAG reads and combines `N` inputs with `O(N)` gates; parity is the calibration example. No amount of coordinate dependence alone supplies a superlinear gate charge.
2. **Counts and entropy describe sets, not the cost of recognizing them.** Circuit counting bounds the Low codebook by `2^(O(N^beta))`, and useful endpoint pairs can match weight, balance, or other statistics. A repeated-block equality circuit still separates many such pairs in `O(N)` gates. Counts need a theorem connecting them to distinct gates after arbitrary sharing.
3. **A certificate is not the separator's computation.** Anti-checkers exist for High tables, but generic completions of their partial traces can be middle-band or High. Since the separator may label the middle freely, querying it on such a completion does not decide whether a Low extension exists. C-464 gives an explicit middle-band cylinder with both types of completion.
4. **A hard selected family is not the full promise.** Affine, junta, sparse-parity-check, global-block, spectral, and other families have cheap shared recognizers or fail to cover all Low tables. A lower bound for one canonical extension likewise does not lower-bound `SepCC`, which minimizes over every legal choice of middle labels.
5. **A source reduction must pay to create its hard tables.** Formula, fixed-depth, comparator, paid-state, fusion, and cyclic-closure results use different resources. They affect ordinary total gates only through a proved compiler or a costed reduction. The same warning applies to description length, wire count, and runtime.
6. **The upper bound remains an exact but expensive construction.** Enumerate every size-`s1` circuit, compare its truth table with the input, and OR the matches. This is a full-promise separator of `O(N*2^(O(N^beta)))` total gates. It supplies no near-linear compression.

These are not proofs that the missing theorem is impossible. They identify a repeated interface failure: arguments force many relevant bits, labels, or witnesses, but do not bound the number of distinct reusable gates needed to realize *every* legal extension of the endpoint relation.

## 3. Exact test of the partial-table route

For a partial table `p` on address set `Q`, define

```text
Ext_s(p) = 1 iff there is a circuit C of size at most s with C|Q = p.
```

This is an existential projection of the Low codebook. It is not, by itself, a Gap-MCSP instance on a complete table: a completion of a Low-free partial trace can be middle-band, and a different completion can be High. A total separator is unconstrained on the former. Thus the generic operation “fill the stars and query F” has no valid correctness implication.

Suppose a proposed reduction instead gives an ordinary addressable bit generator `G(z,a)` with `R` total gates, where `a` is the `n`-bit table address and `G(z,a)=T_z(a)`. Assume it promises

```text
source YES -> CC_n(T_z) <= s1,
source NO  -> CC_n(T_z) > s2.
```

**Addressable-generation cost lemma.** If there is even one source NO input, then `R > s2` (up to a fixed additive constant for the circuit's constant convention).

**Proof.** Fix that source input `z` and hardwire it into `G`. The resulting `n`-input circuit computes `T_z(a)` with at most `R+O(1)` gates. Thus `CC_n(T_z)<=R+O(1)`. Since the reduction requires `CC_n(T_z)>s2`, it follows that `R+O(1)>s2`. This is a lower bound on the cost of one addressable table bit, not the cost of feeding the whole table into `F`.

To compose the reduction with an `S`-gate separator, one must provide all `N` bits `G(z,a)` to its input. Directly evaluating the bit circuit separately at all addresses costs `O(NR)+S+P`. A smaller shared batch implementation is possible only if an explicit compiler for this particular `G` is supplied and all its gates are counted. Thus without such a compiler, a source lower bound `H` gives only `S>=H-O(NR)-P` for this addressable representation.

This is a resource boundary for **addressable** encodings, not an OPS lower bound. Since `s2=N^beta` is much smaller than the target `N^(1+epsilon)`, the per-table lower bound does not rule out a useful reduction. The gate bound for generating the whole input to `F` is a separate cost and can be as large as `O(NR)` without a batch compiler.

Do not extend this lemma to an arbitrary materialized multi-output circuit `E(z)` that produces all `N` table bits at once. After fixing `z`, an `n`-input circuit for `T_z(a)` still needs to select the `a`-indexed output wire; a fan-in-two multiplexer can cost `O(N)`. Therefore the valid generic bound is only `CC_n(T_z)<=R+O(N)`, which gives no restriction when `s2=N^beta<N`. The materialized map does compose with `F` at cost `R+S+P`, but a proof must establish the High property independently or charge a more structured output router. If the outputs select among `r` computed signals through an address router of `q` gates, C-417 gives `CC_n(T_z)<=q+c_mux*r+O(1)`, so High forces `q+c_mux*r+O(1)>s2`. The High label alone does not force `R>s2` for a general multi-output map.

**Novelty and accounting correction.** The addressable-generator inequality is already in C-416. The distinction between addressable and materialized outputs, including the output-routing counterexample and router-cost refinement, is already in C-417 and C-467. C-491 rederived these boundaries during the audit; it contributes no new reduction theorem. An initial formulation that applied `R>s2` to every materialized multi-output map, and charged only `R+S+P` for pointwise evaluation of an addressable generator, would be false. Both errors have been corrected here and in the state summaries.

The boundary also explains the completion-entropy result in C-416: high-entropy random filling tends to miss the Low codebook, while correlated low-entropy filling can always generate parity, repeated blocks, sparse checks, or simple global-block tables. Neither entropy nor number of stars pays for `E` or for a separator's shared gates.

## 4. Hostile constructions and limits of the mechanism

- **Parity/affine sources:** their truth tables have `O(n)`-gate descriptions and affine identities have `O(N)`-gate shared tests. C-490's fixed check `h(x)=x_1*x_2`, conditioned on its opposite shell syndrome, gives a zero-error separator for that selected Low/High pair.
- **Repeated blocks:** equality to block representatives costs `O(N)` gates; a sparse two-coordinate check costs `O(1)` after conditioning the High shell on a violation.
- **Simple global block relations:** a fixed four-coordinate rectangle parity check costs `O(1)` and defeats a source restricted to `u(a) XOR v(b)`.
- **Arbitrary partial completions:** C-464 proves a short anti-checker cylinder can contain a middle point and a true High table. This defeats the generic completion-query bridge, not every possible encoding.
- **Full promise:** the exact Low-description enumerator remains `O(N*2^(O(N^beta)))`. A selected-family recognizer or a balanced-image checker does not accept every Low table and reject every High table.

These are counterexamples to specific mechanisms and source choices. None is a counterexample to the existence of an unconditional OPS lower bound.

## 5. Changed research model

The useful central object is not a chosen recognizer, certificate, or input-query schedule. It is the **minimum-extension function** `SepCC(Y,Z)`. Every proposed proof must do one of two things:

* establish a representation-independent lower bound that applies to every total fan-in-two extension, and charge each AND/OR/NOT gate once despite arbitrary fan-out, reuse, and DAG merges; or
* construct one complete extension with a real gate bound, which would refute the corresponding proposed lower bound.

For a source reduction, write the cost for the actual representation. A materialized multi-output map composes at `R+S+P`, but its high-table property needs an independent proof or a charged address router. An addressable bit generator costs up to `O(NR)+S+P` by direct evaluation; a lower batch cost needs a proved compiler. In either case, its YES and NO images must be promised and the source lower bound must exceed the complete composed cost by the target margin. A partial-table predicate is useful only if such an encoding is proved; hiding the same circuit-consistency decision in `E` is not progress.

This revises the next research choice. Do not refine entropy, balance, static signatures, or anti-checker length as standalone quantities: the repository already has exact limits or counterexamples for them. Test a new mechanism only if it changes the minimum-extension problem itself—either by an operation-wise total-DAG invariant with a superlinear forced value, or by a complete near-linear separator. Keep fusion/native results separate unless a compiler gives all ordinary gate costs.

## 6. Frontier and claim status

**Strongest proved project statement:** valid separators depend on `N-O(N^beta log N)` essential table bits, with the recorded C-406 refinement. This is a support statement and gives only the existing linear ordinary-gate floor; it is not a superlinear total-gate bound. C-490's balanced complement lift and high-shell counting theorem are exact subfamily results. The addressable-generator inequality is already C-416, while the multi-output routing distinction is already C-417/C-467; C-491 adds no theorem to either.

**Strongest construction:** a correct full-promise separator of `O(N*2^(O(N^beta)))` gates by Low-circuit enumeration.

**Quantitative effect:** none. No `N^(1+epsilon)` OPS lower bound, no near-linear full-promise separator, no native `rho` improvement, and no P-vs-NP proof. The fixed-epsilon OPS target would imply `NP` not in `P/poly`; this makes it a meaningful but exceptionally strong subgoal. The locality barrier constrains specified proof techniques and oracle/locality models, not every possible ordinary-circuit argument; no barrier escape is claimed.

## Primary reference

Oliveira, Pich, and Santhanam, [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4, Lemma 4.1, and Section 4.1.
