# C-427 - Robust fiber aggregation has no generic sharing compiler

Date: 30 September 2026  
Status: O-247 retired as a generic route; promise-specific transfer remains unproved; **no quantitative frontier change**

## 1. Exact robustification statement

Take the deep-Low block `F` from C-231, of size `m=Theta(s1*log(s1+n))=Theta(N^beta)`. Every completion of a projected anchor in `SIZE(s1/4)` is Low. For any full OPS separator `C(p,u)`, define

```text
R_C(p) = AND_{u in {0,1}^F} C(p,u).
```

For a deep-Low projection `p`, all fibers are YES, so `R_C(p)=1`. If `p` has a High completion, separator correctness gives `C(p,u)=0` for that completion, hence `R_C(p)=0`. This is a correct induced-promise separator. The proof uses no assumption about how C treats other middle-band tables.

The direct circuit makes `2^m` copies of C plus an AND tree, costing `O(2^m*S+2^m)` gates for an S-gate C. This is far too large. Unrestricted fanout alone gives no compression of the universal quantifier.

## 2. Why a generic fast compiler is not a viable assumption

Suppose there were a uniform compiler which, for every Boolean circuit `C(x,y)` with `k(n)` quantified bits, outputs a circuit for `forall y C(x,y)` with size polynomial in `|C|+|x|+k`. For any language `L` in coNP, write

```text
x in L  iff  forall y in {0,1}^{poly(|x|)}  R(x,y),
```

where `R` is a polynomial-time predicate. Its polynomial-size verifier circuits, followed by this compiler, would give polynomial-size circuits for every language in coNP. Thus `coNP subseteq P/poly`; by complement closure, `NP subseteq P/poly`, and the Karp-Lipton theorem collapses PH to its second level ([Karp-Lipton, STOC 1980](https://dl.acm.org/doi/10.1145/800141.804678)). This is not a contradiction, but it shows that generic polynomial-overhead universal aggregation is itself a major complexity result, not a routine circuit-sharing lemma.

This implication does **not** rule out a compiler for the narrower class of valid GapMCSP separators: no reduction from arbitrary coNP verifier circuits to valid separators has been proved. It only rules out treating a general compiler as a harmless default. Conversely, no valid-separator family with a proved exponential robustification blowup has been constructed here. O-247 therefore supplied no useful lower bound on S and is retired rather than left as an assumed non-shareability principle.

## 3. Gate-elimination transfer test

Carmosino, Dang, and Jackman make several specific gate-elimination proofs constructive: their refuters find errors for undersized DeMorgan circuits computing XOR and MUX, and their affine refuter finds a subspace on which a small circuit is constant ([primary preprint](https://arxiv.org/abs/2604.23958)). These are valuable proof-as-algorithm results, but they do not furnish a general lower bound for a promise separator. The methods exploit a fixed explicit target and a tailored simplification invariant. XOR has a linear lower bound `3(n-1)` in the stated basis; MUX and affine-disperser bounds also scale linearly with their input parameters.

For GapMCSP, an error witness must be a Low table rejected by C or a High table accepted by C. The former has a short circuit-description witness and is NP-verifiable. The latter requires ruling out every circuit of size at most `s2`, a coNP condition; the middle band has no required label. The gate-elimination refuter cannot simply certify that a proposed table is High. C-426's block also does not supply the missing explicit target: every filling of its safe block is Low. Enlarging the block admits High fillings, but then C may depend on those bits and the C-426 cylinder argument no longer forces an error.

This is a failed transfer, not a barrier theorem. It is distinct from Chen et al.'s locality barrier, which constrains specified lower-bound techniques that extend to local oracle gates; it does not rule out all global circuit arguments ([primary paper](https://eccc.weizmann.ac.il/report/2019/168/download/)).

## 4. Countertests and exact accounting

The projected separator `C_B` from C-426 is a complete separator on which this robustification is free whenever the quantified block is among its ignored inputs: `R_{C_B}=C_B`. Thus an exponential cofactor blowup is not universal for valid separators. On the other hand, parity, repeated-block equality, sparse parity checks, and simple global block relations still have direct shared readouts of `O(N)`, `O(N)`, `O(L+r)`, and `O(N+T)` gates, respectively; these defeat incidence-based charges but are not complete GapMCSP separators.

The C-426 projected-Low separator remains the strongest complete construction in this cycle, at `O(N*2^(O(N^beta)))` total gates, `O(N*2^(O(N^beta)))` wires, and gate-list descriptions of `O(N*2^(O(N^beta))*log(N*2^(O(N^beta))))` bits. No smaller full-promise construction was found. Native fusion q, paid AND states, OR operations, semantic endpoints, wide seeds, cycles, and semi-filter extensions are untouched.

## 5. Frontier and next direction

O-247 is closed: robustification is semantically valid, its naive cost is exponential in the fiber width, and a generic sharing compiler would imply `NP subseteq P/poly`; the promise-specific version has neither a compiler nor a lower-bound counterexample. Do not revisit it without a concrete separator-specific structural identity.

**No frontier change:** ordinary lower bound `S>=N-O(N^beta log N)-1` with C-406's additive logarithmic refinement; OPS `N^(1+epsilon)` target open with the exact thresholds and quantifiers audited in C-426; exact full-promise upper `O(N*2^(O(N^beta)))`; native `rho>=N-o(N)` separate. The next route must provide its own gate inequality and a valid full-promise construction/counterconstruction before any hardness claim is promoted.
