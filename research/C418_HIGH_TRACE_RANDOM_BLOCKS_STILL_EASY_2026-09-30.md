# C-418 - A high-threshold random block trace is still easy

**Status:** proved a stronger random-block avoidance lemma and an exact promise-preserving routed family. For each fixed `beta<1`, any fixed `gamma<1-beta` works, and the induced selector costs `O(M^gamma)`; the construction therefore does not yield a lower bound for a full-promise separator. The ordinary and native quantitative frontiers are unchanged.

## 1. Calibrated target

Let `M=2^d` be the truth-table input length. OPS Theorem 1.4 uses a universal constant `c>=1`, low threshold `s1=M^beta/(c d)`, and real high threshold `tau2=M^beta`; NO means `CC(f)>tau2`, equivalently at least `floor(tau2)+1` gates. The theorem requires one fixed `epsilon>0` to work for every sufficiently small fixed `beta>0`. Its proof instantiates the denominator as `10d`. This report uses the concrete thresholds

```text
s1 = floor(M^beta/(10d)),    s2 = floor(tau2)+1  [first integer NO size].
```

The theorem below holds for every fixed `0<beta<1` and every fixed `0<gamma<1-beta`; the square-root choice `gamma=1/2` is a convenient special case for `beta<1/2`. It is only about an induced subpromise and does not establish the OPS lower-bound premise.

## 2. Mechanism: entropy of a balanced partition against all sub-high circuits

Fix `0<gamma<1-beta`, set `q=2^floor(gamma*d)` and `r=M/q`, so `q` blocks divide the `M` table coordinates into equal blocks of size `r`. Choose a uniformly random labeled balanced partition `P=(B_1,...,B_q)`. Its block-constant tables are

```text
V_P = { f_y : y in {0,1}^q },     f_y(a)=y_j when a in B_j.
```

### Theorem

For every fixed `0<beta<1`, every fixed `0<gamma<1-beta`, and all sufficiently large `d`, there is a partition `P` such that every nonconstant `f in V_P` has `CC(f)>=s2=floor(tau2)+1`, hence `CC(f)>tau2`. The two constant tables have circuit size at most one, hence are YES for large `d`. The constructed representative-equality test accepts the constants and rejects every nonconstant trace, so it separates the formal induced promise (`CC<=s1` versus `CC>tau2`). Thus this is an easy restricted trace with an exact promise-preserving source map.

```text
YES: y=0^q or y=1^q,
NO:  y is nonconstant.
```

### Proof

The number of fan-in-two AND/OR/NOT circuits on `d` inputs with fewer than `s2` gates is at most

```text
2^(O(s2 log(s2+d))) = 2^(O(M^beta d)).
```

Fix any nonconstant truth table `f` of weight `w`. If `r` does not divide `w`, it cannot be block-constant. Otherwise write `w=kr`, where `1<=k<=q-1`. Under a uniformly random balanced partition,

```text
Pr[f is constant on every block] = binom(q,k)/binom(M,w)
                              <= (M+1) 2^(-(M-q) H_2(w/M)).
```

Since `w/M` lies in `[1/q,1-1/q]`, binary entropy is at least `H_2(1/q)`. With `q=Theta(M^gamma)`,

```text
(M-q) H_2(1/q) = Theta(M^(1-gamma) log M).
```

Union-bounding over all nonconstant truth tables represented by circuits of size `<s2` gives failure probability at most

```text
2^(O(M^beta d) + log(M+1) - (M-q)H_2(1/q)) = o(1),
```

because `1-gamma>beta` is fixed. Thus some partition has no nonconstant block-constant table of circuit size `<s2`. This proves the claim. The proof counts ordinary total gates and places no restriction on depth or reuse. For example, `gamma=1/2` gives the square-root case for every fixed `beta<1/2`; choosing `gamma=(1-beta)/2` works for every fixed `beta<1`.

## 3. Exact paired-family construction and the decisive counterconstruction

Fix the partition from the theorem. For source input `z in {0,1}^{q-1}`, define a multi-output map with

```text
E_P(z)[a] = 0       if a in B_1,
            z_j     if a in B_(j+1),  1<=j<q.
```

This map has no internal gates when constants and output wires are free; otherwise it needs `O(1)` gates for the zero constant. Its `M` output wires repeat the `q-1` source bits according to the fixed partition. If `z=0`, the output is `0^M`, an OPS-YES table. If `z!=0`, at least one block is one and `B_1` is zero, so the output is nonconstant and, by the theorem, OPS-NO. Thus every output is promised and

```text
GapMCSP(E_P(z)) = 1 iff z=0.
```

The source label is just NOR of `q-1` bits, computable in `O(q)` gates. More directly, on the entire block-constant subpromise, a separator reads one representative from each block and accepts iff all representatives are equal. This is an `O(q)=O(M^gamma)` total-gate circuit. It is exact on both promised sides of the induced promise, permits arbitrary gate reuse, and never reconstructs a table description.

More generally, let an `R`-gate shared encoder compute the `q` block values `v_1(z),...,v_q(z)` and then route each value across its block. The induced label is `1` exactly when all `v_j(z)` are equal, so the source label has a circuit of at most `R+O(q)` gates, independently of `M`. If the first block is fixed to zero, the label is simply `NOR(v_2,...,v_q)` and has the same bound. This is a formal limit on this transfer architecture: the routing expansion from `q` signals to `M` table bits does not make the induced decision harder.

This is the strongest counterconstruction to the proposed block-trace mechanism: the entropy argument can make every nonconstant trace maximally separated at the OPS threshold, but the resulting labels still have a shared readout using only one bit per block. Repeated anchors do not force additional work.

## 4. Adversarial examples and the boundary of the result

- **Parity:** the full address-parity table has `O(d)` gates and is OPS-YES for large `d`. It cannot be a nonconstant member of this `V_P`, by the theorem, so it lies outside the selected slice. This is not a contradiction; it shows why the easy slice readout is not a full-promise separator.
- **Repeated-block equality:** this is the selected slice itself. Equality of all entries within each block can be checked in `O(M)` gates on arbitrary tables, while the induced label is decided in `O(q)` gates. Equality counts do not give a superlinear charge.
- **Sparse parity checks:** checking a collection of blockwise linear constraints costs at most linear in the number of table incidences when written directly; shared parity trees can reduce repeated work. The block-trace theorem gives no independent gate charge for those constraints.
- **Simple global block relations:** if block values are generated by a small circuit on source bits, the image label can often be computed on those shared values. The theorem says only that nonconstant table outputs are High; it does not say the induced labeling function is hard.

For a concrete sparse-check test, let `H` be any binary `m x k` matrix with `m<=q-1`, and map `z` to the block pattern `(0,Hz,0,...,0)` using the first `m` variable blocks. Every nonzero syndrome gives a nonconstant table and is OPS-NO; zero syndrome gives `0^M`, an OPS-YES table. The source label is `Hz=0`, computable by the same parity network used by the encoder plus an OR/NOR over its `m` outputs, at `O(nnz(H)+m)` gates with no density assumption beyond the displayed incidence count. Sparse checks therefore do not make this image hard by themselves. As an even simpler global relation, put one source bit on a single block and zero on all others: the two outputs are Low and High, but the label is that one bit and costs one gate (or a wire/complement).

These are counterexamples to the mechanism as a route to superlinear full-promise work, not counterexamples to `P != NP` or to a future Gap-MCSP lower bound.

## 5. Resource audit and native-model boundary

- **Ordinary total gates:** the restricted-promise readout uses `O(q)` gates. The source map uses `R=0` internal gates, or `O(1)` if constants are charged. A separator of `S` gates composed with this multi-output map gives a source circuit of `S+O(1)` gates under the standard gate-count convention.
- **AND and OR gates:** the representative equality test uses `O(q)` AND/OR/NOT gates; it makes no claim about a paid-AND-only measure.
- **Wires:** the map has `M` output incidences. Its outputs repeatedly name source wires or a constant; unrestricted fanout is essential to the zero-internal-gate description.
- **Description bits:** naming the selected partition and its output routing can cost `O(M log q)` bits in a direct encoding. That is separate from gate count. This proof gives existential nonuniform partitions; it does not provide a succinct or polynomial-time construction of `P`.
- **Runtime:** materializing `E_P(z)` takes `Theta(M)` time just to write its output. No claim charges this as circuit gates or provides an efficient uniform partition search.
- **Native fusion:** no semantic endpoint construction, paid-AND count, OR-operation count, cyclic-closure potential, or semi-filter extension is proved. This ordinary multi-output map does not imply any bound on `rho_GapMCSP`; arbitrary endpoints, wide seeds, reuse, and cycles remain untouched.

## 6. Paired full-promise separator attempt

The `O(q)` representative test fails on full Gap-MCSP because it rejects promised low tables outside `V_P`, including address parity. Testing block constancy and then recognizing the two constant patterns therefore is not sound for the full promise. The exact full-promise construction still compares the input against every circuit table of size at most `s1`, costing `O(M * 2^(O(M^beta)))` total gates. No near-linear full-promise separator was constructed.

## 7. Literature, originality, and barrier audit

This is a project-derived strengthening of the elementary balanced-partition estimate in C-408: the union bound is taken over circuits below `s2`, rather than only circuits below `s1`, and the block count can be any `q=M^gamma` with `gamma<1-beta` (about `sqrt(M)` is one special case). It is not presented as a new general circuit-lower-bound technique or as a literature-priority claim. The construction proves a cheap induced trace, not a lower bound on a full separator.

Known MCSP lower bounds that are much stronger than the present near-linear frontier are for restricted models: the coin-problem method gives exponential lower bounds for fixed-depth `AC^0[p]`, while local-PRG methods give near-cubic De Morgan formula bounds and near-quadratic arbitrary-basis formula/branching-program bounds. Those results do not establish an unrestricted total-gate `M^(1+epsilon)` lower bound, and the present restriction argument does not extend them to general circuits.

If the OPS Theorem 1.4 premise were established with its quantifiers, it would imply `NP` is not contained in `P/poly`, hence `P != NP`. This report establishes no part of that premise. The result is neither a bypass nor a contradiction of the locality barrier: the cited barrier concerns limitations on specified lower-bound methods that localize to small-fan-in circuits with powerful local oracle gates. This counting restriction derives no Gap-MCSP separator lower bound.

## 8. Frontier and next mathematical lesson

**No frontier change.** The ordinary lower bound remains `S>=M-O(M^beta log M)-1` with C-406's additive logarithmic refinement; OPS `M^(1+epsilon)` remains open. The native target remains separately `rho_GapMCSP>=M-o(M)`. The exact full-promise upper remains `O(M*2^(O(M^beta)))`.

The learned restriction on future mechanisms is precise: a promised image with many High outputs, high distance between labels, or a large repeated-block pattern family is not enough. Its induced label function must itself require many total gates after all reusable source signals are visible. C-417's open O-239 route is therefore closed for balanced block-constant maps: their label reduces to equality or a small predicate on the block values. Continue O-239 only for non-block-constant maps with a proved hard source label and exact promise preservation.

### Primary sources checked

- Oliveira, Pich, and Santhanam, [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and its proof.
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://arxiv.org/abs/1911.08297), for the technique-specific locality-barrier framework.
- Pich, [*Localizability of the Approximation Method*](https://arxiv.org/abs/2212.09285), for the scope of one established localizability limitation.
- Golovnev et al., [*AC0[p] Lower Bounds against MCSP via the Coin Problem*](https://eccc.weizmann.ac.il/report/2019/018/).
- Cheraghchi et al., [*Circuit Lower Bounds for MCSP from Local Pseudorandom Generators*](https://eccc.weizmann.ac.il/report/2019/022/).
