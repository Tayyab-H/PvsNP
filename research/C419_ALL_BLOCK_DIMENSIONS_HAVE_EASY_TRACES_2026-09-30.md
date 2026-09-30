# C-419 - Every balanced block dimension has an easy induced trace

**Status:** proved by combining the C-408 and C-418 partition theorems. For every fixed OPS-small `beta<1/2` and every fixed block exponent `gamma in (0,1)`, some balanced block-constant slice has an exact induced-promise separator of `M^(gamma+o(1))` gates. This closes the full balanced-block dimension range as a route to a hard trace. It does not change the full-promise frontier.

## 1. Parameters and statement

Let `M=2^d`, `s1=floor(M^beta/(10d))`, and `s2=ceil(M^beta)`, using OPS's concrete gap. Fix `0<beta<1/2` and any fixed `0<gamma<1`. Set

```text
m = 2^floor(gamma*d),    r=M/m.
```

Partition the `M` table coordinates into `m` equal blocks `B_1,...,B_m`; a block-constant table is determined by a pattern `y in {0,1}^m`.

### Theorem

For every such fixed pair `(beta,gamma)` and all sufficiently large `d`, there is a balanced partition for which the entire induced OPS promise on block-constant tables has a fan-in-two AND/OR/NOT separator of size `O(m log^2 m) = M^(gamma+o(1))`.

## 2. Proof by a complete two-case split

### Case A: `gamma <= beta`

Since `beta<1/2`, we have `gamma<=beta<1-beta`. Apply C-418 with the same `beta` and `gamma`. Its circuit-count versus partition-entropy union bound gives a partition for which every nonconstant block-constant table has circuit complexity at least `s2`. The two constant tables are YES. The induced promise is therefore exactly “all `m` block values equal” versus “not all equal.” Reading one representative coordinate per block and testing equality costs `O(m)` gates. This also covers the boundary `gamma=beta`.

### Case B: `gamma > beta`

Apply C-408 with the same parameters. Its balanced-partition argument gives a partition with these two properties:

1. Every low block-constant table is within fewer than `5s1` table entries of `0^M` or `1^M`.
2. Every block-constant table within `6s1` entries of either constant table has circuit complexity `<s2`.

For pattern `y`, distance to the nearer constant is `r * min(wt(y),m-wt(y))`. Thus the induced promise is separated by

```text
T_P(y)=1 iff r * min(wt(y),m-wt(y)) <= 6s1.
```

A sorting network and threshold comparison use `O(m log^2m)` gates. The middle band of the original promise remains unrestricted: the proof only guarantees acceptance of every induced YES and rejection of every induced NO.

The two cases cover every `gamma in (0,1)`. Since `m=M^(gamma+o(1))` and fixed `gamma<1`, the separator is sublinear in `M` (up to the displayed polylogarithmic factor).

## 3. Mechanism tested against sharing

The proposed mechanism was that making many repeated table coordinates depend on a smaller pattern vector might force a separator to spend additional work after seeing the entire table. The two cases eliminate that inference:

- For `gamma<=beta`, the entropy argument can force all nonconstant traces to the High side, but then one representative per block decides the induced label.
- For `gamma>beta`, the low traces may be more numerous, but the full induced promise is separated by distance from the two constant patterns.

The complete restricted-promise readout never pays once per repeated coordinate. This conclusion permits arbitrary gate reuse and does not assume witness reconstruction, address enumeration, or preservation of caller history.

## 4. Adversarial constructions and limits

- **Parity:** parity on the full address has `O(d)` gates, so it is Low for large `d`. It is not a nonconstant member of the selected slice in Case A; in Case B it lies outside the block-constant slice in the chosen C-408 partition. Thus neither restricted separator decides the full promise.
- **Repeated-block equality:** this is exactly the block-constant geometry. In Case A its label is equality of representatives; in Case B its label is the stated Hamming threshold. Checking all within-block equalities on an arbitrary input costs `O(M)` gates, still not a superlinear charge.
- **Sparse parity-check relations:** in Case A, generate `m-1` block values as a syndrome `Hz` and fix one block to zero. Zero syndrome maps to `0^M` (YES); nonzero syndrome maps to a nonconstant block table (High). The source label `Hz=0` is computed by the encoder's parity network plus a NOR of syndrome bits, `O(nnz(H)+m)` gates. In Case B, any source label induced through block values can be computed by the block-pattern generator followed by the `O(m log^2m)` Hamming-threshold selector; counting sparse incidences separately does not charge additional readout work.
- **Simple global block relations:** shared copies or parities of a small source vector feed the block values once, then the Case A representative test uses those values. In Case B the threshold circuit reads the values directly. Signal reuse removes any charge based on repeated incidences.

These counterexamples close the balanced-block mechanism only. They do not provide a near-linear separator for arbitrary truth tables and do not refute a future unrestricted Gap-MCSP lower bound.

## 5. Resource audit

- **Total gates:** `O(m)` in Case A and `O(m log^2m)` in Case B.
- **AND, OR, NOT:** all counts are included in those total-gate bounds. No paid-AND-only or native-fusion claim follows.
- **Wires:** the embedding has `M` output incidences, repeating each block value `r` times. Fanout and gate size are distinct measures.
- **Description:** directly naming the partition and router can require `O(M log m)` bits. The existence proof is nonuniform; no efficient deterministic partition search is proved.
- **Runtime:** materializing an `M`-bit table takes `Theta(M)` time to write the output. This is separate from gate count.
- **Native fusion:** no semantic endpoint, wide-seed, unrestricted-reuse, cyclic-closure, or all-semi-filter-extension argument is made. Native `rho_GapMCSP` is untouched.

## 6. Full-promise separator attempt

An explicit near-linear full-promise candidate is: test whether the input is block-constant (compare every table bit with its block representative, costing `O(M)` gates), then apply the appropriate induced-slice selector. The total is `O(M+q log^2q)=O(M)` for every fixed `gamma<1`, but it is incorrect: it rejects the Low address-parity table, which is outside the chosen block-constant slice. The restricted readouts therefore cannot be extended to the full promise by a membership gate. The exact all-input separator still tests equality with each circuit table of size at most `s1`, at `O(M*2^(O(M^beta)))` total gates. No valid near-linear full-promise separator was found.

## 7. Literature, scope, and originality

This is a synthesis of the project-derived C-408 and C-418 arguments, not a claim of a new general circuit lower-bound technique or literature priority. OPS Theorem 1.4 remains calibrated at low threshold `M^beta/(c d)` and high threshold `M^beta`; its proof uses `c=10`, and the magnification implication requires one fixed `epsilon>0` for every sufficiently small fixed `beta`. Nothing here proves that premise. Established superlinear MCSP bounds against `AC^0[p]`, formulas, and branching programs are model-restricted and do not transfer to unrestricted total-gate circuits. The locality barrier for specified lower-bound methods remains technique-specific; these restriction lemmas derive no full-promise lower bound and neither bypass nor contradict it.

## 8. Quantitative frontier

**No frontier change.** Ordinary full-promise lower bound remains `S>=M-O(M^beta log M)-1` with C-406's additive logarithmic refinement. The OPS `M^(1+epsilon)` premise remains open. Native `rho_GapMCSP>=M-o(M)` remains separate. The exact full-promise upper remains `O(M*2^(O(M^beta)))`.

**Route decision:** retire balanced equal-block restrictions for every fixed block dimension exponent `gamma in (0,1)`. A viable paired-family route must use non-block-constant tables and prove that the induced source label remains hard after all shared signals are available.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4.
- Project derivations: [C-408](C408_RANDOM_BLOCK_SUBSPACE_TRACE_2026-09-30.md) and [C-418](C418_HIGH_TRACE_RANDOM_BLOCKS_STILL_EASY_2026-09-30.md).
- Golovnev et al., [*AC0[p] Lower Bounds against MCSP via the Coin Problem*](https://eccc.weizmann.ac.il/report/2019/018/); Cheraghchi et al., [*Circuit Lower Bounds for MCSP from Local Pseudorandom Generators*](https://eccc.weizmann.ac.il/report/2019/022/).
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://arxiv.org/abs/1911.08297), and Pich, [*Localizability of the Approximation Method*](https://arxiv.org/abs/2212.09285), for technique-specific locality limitations.
