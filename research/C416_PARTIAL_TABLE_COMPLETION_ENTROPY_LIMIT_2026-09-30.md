# C-416 - High-entropy completion cannot preserve partial-table YES instances

**Status:** proved sampler limitation; failed transfer to a shared-gate lower bound.  
**Date:** 30 September 2026.  
**Ordinary frontier:** unchanged.  
**Native fusion frontier:** unchanged.

## 1. Question and proposed mechanism

Can a reduction from a partial truth-table problem to ordinary Gap-MCSP fill the unspecified entries at random, relying on the fact that only a small number of complete tables have low circuit complexity?

The proposed mechanism is a **completion-entropy bottleneck**. It bounds the probability that a completion sampler lands in the low-circuit set. The statement is exact for uniform filling and extends to any sampler with bounded point probabilities. It controls the reduction's sampling distribution; it does not charge gates to an ordinary separator.

## 2. Exact circuit-counting statement

Let `d` be the number of input variables and let `M=2^d` be the truth-table length. Circuits are ordinary acyclic, single-output Boolean circuits with fan-in-two AND/OR and unary NOT gates; allowing constants changes only fixed factors. Let `Low_s` be the set of truth tables computed by circuits of at most `s` gates.

For some absolute constant `A` depending only on the fixed basis,

```text
|Low_s| <= 2^(A (s+1) log_2(d+s+2)).
```

**Proof.** Number gates in topological order. At gate `j`, choose one of a fixed number of gate types and at most two predecessors from the `d` input nodes, constants, and earlier gates. This gives at most `B(d+s+2)^(2s)` descriptions for a circuit with at most `s` gates, for a basis-dependent constant `B`; selecting the output wire and summing over sizes `0,...,s` adds at most a further polynomial factor in `d+s+2`. Taking base-two logarithms gives the bound. Different descriptions can compute the same table, so this is an upper bound on distinct low tables.

At the concrete OPS parameters, set

```text
s1 = floor(M^beta/(10d)),   s2 = M^beta,
```

for a fixed `0<beta<1`. Then

```text
log_2 |Low_s1| <= O(s1 log(s1+d+2)) = O(M^beta).
```

Indeed, for fixed `beta`, `log_2(s1+d+2)=beta*d+O(log d)`. The hidden constant is independent of `d` (and may depend on the fixed basis). The published OPS magnification theorem uses a universal constant `c` in the low threshold `M^beta/(c d)`; its proof instantiates `10d`. Its quantifiers require one fixed `epsilon>0` and the lower bound for every sufficiently small fixed `beta>0`.

Now let `p` be a partial table in `{0,1,*}^M` with `u` stars. It has exactly `2^u` completions. If `X` is uniform on these completions, then

```text
Pr[X in Low_s1] = |Low_s1 intersect Comp(p)| / 2^u
                  <= min(1, |Low_s1| / 2^u).
```

Consequently, if a partial-MCSP YES instance is defined by the existence of at least one `Low_s1` completion, uniform filling reaches a low completion with probability at least `2/3` only if

```text
u <= log_2 |Low_s1| + log_2(3/2) = O(M^beta).
```

More generally, let `D_p` be any distribution over completions with point probabilities bounded by `2^-h` (min-entropy at least `h`). Then

```text
Pr_{X~D_p}[X in Low_s1] <= |Low_s1| 2^-h.
```

Thus success probability at least `2/3` requires `h <= log_2 |Low_s1|+log_2(3/2)`. For `t` independent uniform completions followed by an OR of their low-completion events, the union bound gives success probability at most `t |Low_s1|/2^u`. This last statement is only about that sampler-and-OR architecture; it is not a `t`-fold gate lower bound.

## 3. Attack with the required shared-computation examples

The lemma passes each example as a counting statement, but each also exposes why completion entropy is not a general gate charge.

| Family | Explicit cheap realization | What it says about the mechanism |
|---|---|---|
| Parity / affine parity | Each `a·x xor b` has an AND/OR/NOT circuit of `O(d)` gates. | An all-star partial table can be completed by choosing `a,b` and generating the parity table; the sampler has only `d+1` random seed bits, regardless of the `M` output bits. Uniformly choosing all `M` bits almost never lands in this family, but the correlated sampler succeeds with probability one. |
| Repeated-block equality | For `d=k+r`, fix a `k`-bit prefix `x` and set `T_z(x,y)=z_x` for every `r`-bit suffix `y`. A hardwired multiplexer for `z` gives `O(2^k)` gates. | This is a repeated-block low family of `2^(2^k)` tables with a seed of `2^k` bits. Uniform filling over the `2^d` output bits is exponentially unlikely to hit it; copying each seed bit across its block hits it exactly. |
| Sparse parity checks | Set `T_z(x,y)=z_x xor PARITY(y)`. For every suffix edge, `T_z(x,y) xor T_z(x,y xor e_j)=1`, a weight-two check. | The entire table is determined by the base block `z` and one global parity rule. There are many local constraints, but they do not imply independently paid gates or high sampler entropy. The fixed table has an `O(2^k+d)` circuit. |
| Simple global block relations | More generally, `T_z(x,y)=z_x xor h(y)` for a simple `h` (or `z_x` on repeated blocks) has a circuit of `O(2^k+CC(h)+d)` gates. | Correlations across exponentially many entries let one seed determine every block. A pointwise-entropy argument sees only the sampler's support; it cannot infer the cost of producing or distinguishing these tables. |

For the last two explicit families choose `k=floor(beta*d/2)` and `r=d-k`. Then `2^k+d = M^(beta/2)+d = o(M^beta/d)`, so every table in the family is below the OPS low threshold for all sufficiently large `d`, for each fixed `beta>0`. The parity suffix makes the sparse checks explicit; using `h=0` gives repeated blocks. These are ordinary total-gate upper bounds for the generated tables, not lower bounds on a separator.

There is also a cheap shared computation on the complete table that defeats a proposed charge by local-constraint count. For an explicit table `T`, test whether it is an affine parity by checking, for every coordinate `i` and every address `x`, that `T(x) xor T(x xor e_i)` equals `T(0) xor T(e_i)`. This condition is equivalent to affine parity, and all checks cost `O(Md)=O(M log M)` AND/OR/NOT gates. For repeated blocks, compare each entry `T(x,y)` with the representative `T(x,0)` and AND the comparisons, using `O(M)` gates. For the sparse family `T_z(x,y)=z_x xor PARITY(y)`, check each suffix edge equation `T(x,y) xor T(x,y xor e_j)=1`; there are `O(Md)` such checks and they take `O(M log M)` gates even with direct computation. Unlimited fanout allows each table bit to feed all incident checks. These are subpromise recognizers: they reject other valid Low tables, so they are not full Gap-MCSP separators. They do prove that the number of parity constraints or incidences alone does not force `M^(1+epsilon)` total gates for any fixed `epsilon>0`.

The decisive counterexample to a broad entropy claim is simple: on the all-star partial table, choose a random seed `z` and output `T_z`. This is a valid completion sampler, and every output is low, even though `u=M >> M^beta`. Its point probabilities have min-entropy at most the seed length, which is consistent with the theorem. If a reduction has a witness or can construct a correlated low completion, the uniform-completion obstruction says nothing against it. Conversely, if the reduction uses high-entropy samples, the bound applies regardless of whether samples are processed by a shared circuit.

Parity, repeated blocks, sparse checks, and global block relations do not refute the OPS lower-bound program. They refute only the proposed inference from the number of unspecified table bits, or the number of constraints, to an unavoidable amount of ordinary computation.

## 4. Attempt to turn it into an OPS proof, and the failure point

The intended transfer would need a reduction from a source problem to partial tables with both of these properties:

1. On every source YES input, the partial table has a low completion, and the target separator can be tested through the chosen completion procedure with adequate completeness.
2. On every source NO input, the resulting total table is OPS-NO, meaning its circuit complexity is at least `s2=M^beta` (the middle band remains unconstrained).

The completion-density lemma supplies neither condition. It only says a **high-min-entropy** sampler is unlikely to find any low completion. A reduction can use a low-entropy, source-aware correlated sampler, so `u` alone cannot force failure. More fundamentally, no circuit inequality connects `u`, sampler entropy, or the count of possible completions to the total gates of an arbitrary one-bit separator. We did not assume the separator reconstructs a description, enumerates witnesses, checks addresses separately, or preserves caller history.

The 2026 `f-SEP*` problem asks whether *any* completion is a simple extension of a fixed base function. That predicate is not itself the statement that a completion has circuit complexity at most `s1`; nor does a negative `f-SEP*` instance imply complexity at least `s2`. C-415 already gives explicit linear-size negative extensions. The entropy lemma may only be applied after a separate reduction proves an OPS-compatible low-completion characterization, with the correct promise on both sides.

**Failure classification:** rigorous obstruction to uniform/high-min-entropy totalization with many stars; no lower bound on total gates, wires, OR gates, paid AND states, descriptions, runtime, or fusion `rho`.

## 5. Paired attempt at a full-promise separator

For a complete `M`-bit input, the exact separator remains: enumerate every size-`s1` circuit, compare its full truth table to the input, and OR the equality results. It accepts all YES tables and rejects all NO tables; middle inputs may receive either answer. With

```text
K = |Low_s1| <= 2^(O(M^beta))
```

this explicit fan-in-two construction uses `O(M K) = O(M 2^(O(M^beta)))` gates. A universal evaluator can share the definition of a circuit and a truth-table address, but this direct implementation still has to combine the equality results for all candidate descriptions and all `M` positions. We found no representation-independent compression of that OR to `M^(1+o(1))` gates. Its description length and uniform construction time are separate costs; this report establishes no improvement to any of them.

This is a valid full-promise upper bound, not a near-linear separator. The low-family samplers above cover particular subfamilies only and do not accept every low table while rejecting every high table.

## 6. Literature, originality, and barrier audit

- **Established:** OPS Theorem 1.4 gives the exact magnification quantifiers: a universal constant `c`, low threshold `2^(beta*d)/(c d)`, high threshold `2^(beta*d)`, and one fixed `epsilon>0` for every sufficiently small fixed `beta>0`. The proof uses `10d` in its concrete construction. The only fact used here beyond elementary counting is the standard circuit-description upper bound `2^(O(s log(s+d)))`.
- **Established:** Carmosino, Dang, and Jackman's STACS 2026 `f-SEP*` definition is existential completion of a partial truth table for an exact simple-extension predicate. That is structurally related to, but not identical with, a partial-MCSP YES label.
- **New project-level application, elementary:** the low-table count gives the explicit min-entropy ceiling above for random totalization of a partial-MCSP existential-low-completion predicate. This is not a new circuit lower bound or a new asymptotic theorem about unrestricted reductions.
- **Failed transfer:** the bound depends on the completion distribution's largest atom. Correlated samplers from parity, repeated blocks, sparse parity checks, or simple block relations can have very low entropy and always output Low tables. The partial-completion count does not charge downstream shared gates.
- **Locality:** this argument neither constructs a localized oracle computation nor uses one. It therefore does not bypass or strengthen the hardness-magnification locality barrier of Chen et al.; that barrier is technique-specific and is not a theorem about every ordinary circuit lower-bound method.

## 7. Exact quantitative effect and next distinct mechanism

**No frontier change.** The ordinary total-gate lower bound remains `S >= M-O(M^beta log M)-1`, with C-406's additive logarithmic refinement. The OPS `M^(1+epsilon)` target remains open. The native full-promise target `rho_GapMCSP >= M-o(M)` is separate and unchanged. The explicit full-promise separator remains `O(M 2^(O(M^beta)))` gates. No conversion among total gates, wires, description bits, runtime, paid AND states, OR operations, endpoint widths, or cyclic fusion closure is proved.

The next mechanism must act on the completed table and the separator's output computation directly. Specifically, test a **deterministic paired-family embedding**: construct source-indexed low and high tables so that their separator labels recover a specified hard Boolean function, while proving the table maps and postprocessor together cost less than the hardness lower bound. This differs from counting partial completions; it must include parity/repetition/sparse-check/global-relation countertests and prove ordinary total-gate cost under unrestricted reuse. If the high family cannot be proved `CC>=M^beta`, close that embedding quickly rather than rephrasing an entropy barrier. Keep the exact enumeration separator as the upper calibration.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and Section 4.1.
- Carmosino, Dang, and Jackman, [*Simple Circuit Extensions for XOR in PTIME*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.23/LIPIcs.STACS.2026.23.html), definition of `f-SEP*` and reduction discussion.
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://doi.org/10.1145/3538391), for the scope of the locality barrier.
