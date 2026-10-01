# C-438 - Range Avoidance exposes an aggregate oracle-transfer budget

## Mechanism

Let a source function `L_m` have ordinary circuit complexity at least `h_m`. Suppose an oracle computation for `L_m` makes at most `Q_m` adaptive queries to a promise problem `U`. Its deterministic-control circuit has `D_m` gates, including query generation, answer routing, and the final output. Assume each query is mapped by an ordinary multi-output circuit of `R_m` gates to an `N_m`-bit OPS instance, and a `B_m`-gate postprocessor converts the separator answer to the `U` answer. Every query on the correct oracle path must lie in `U`'s promise (the smartness condition), and the reduction must map it to the correct promised side:

```text
U-YES -> CC(table) <= N_m^beta/(c log_2 N_m)
U-NO  -> CC(table) > N_m^beta.
```

If an OPS separator has `S_m` gates, serially substituting one copy per adaptive query gives an ordinary circuit for `L_m` of size at most

```text
D_m + Q_m (R_m + S_m + B_m).
```

The proof is literal circuit composition: compute the next query from the source input and previous separator answers, generate its table, apply the separator, and feed the answer to the next stage. Inductively, each simulated answer is correct, so the run follows the original smart path and never needs separator behavior outside the promise. It makes no assumption about how the separator shares gates internally. If each query position has its own fixed target size and reduction, replace the product by the sum of the per-query costs. Path-dependent target lengths need a separately proved, costed length-selection or padding map. This is a total-gate count; wires, description bits, and construction time are separate measures.

**Scope correction from C-439:** this is an upper bound for the serial-substitution compiler, not a lower bound on every joint implementation and not proof that costs of query calls are additive. If the bound is below `h_m`, that compiler yields a contradiction. If it is not, the transfer remains open: a joint circuit may share work across related queries, and circuit-size direct sum is false in general (see C-439).

## What the source paper contributes, and what it does not

Ren-Williams prove a function in `E^{prMA}/1` with circuit complexity `Omega(2^m/m)`. Their reconstruction branch uses smart `prMA` queries testing whether a small circuit encodes a valid satisfying assignment with a specified next prefix; PCP verification turns this into the promise-MA interface. The canonical `prMA` query is a verifier circuit `A(w,r)`, with YES when some witness accepts for every random string and NO when every witness accepts with probability at most one half. See [ECCC TR26-118](https://eccc.weizmann.ac.il/report/2026/118/), especially its bounded-query reconstruction and prMA definition.

This structure is a plausible reduction target, but the paper supplies no map from those prefix-existence queries to the exact OPS truth-table gap. Also, membership in `E^{prMA}` only supplies an exponential-time source computation. A generic circuit unrolling of its deterministic control is not known here to cost less than `Omega(2^m/m)`. Both `D_m` and the query transformations must be costed; a proof that all query costs add is not available and cannot be assumed.

## Strongest counterconstruction to the naive map

The obvious table, `T_q(w,r)=A_q(w,r)` (or the local PCP verifier table), has a polynomial-size circuit on both YES and NO queries: it evaluates the same verifier. At target lengths where that polynomial is below `N^beta/(c log N)`, both outcomes map to Low. It does not encode the existential prefix bit as High versus Low. Taking the existential OR is the hard step; putting a solved answer into a constant table makes both answers Low, while generating a high table on the NO side would require a separate hardness-encoding theorem. Range Avoidance starts with a hard truth table to find a missing output; it does not provide this reverse low/high encoding.

Parity, repeated-block equality, sparse parity-check systems with `O(N)` total incidence, and simple global block relations all admit `O(N)` shared readouts. They refute generic charges based on witness width, number of local checks, or constraint incidence. They do not refute the aggregate transfer lemma, which is conditional on an actual promise-preserving reduction.

## Paired full-promise construction

Let `s1=floor(N^beta/(c log_2 N))` and list the `K` descriptions of circuits of size at most `s1`, where `K<=2^(O(s1 log(N+s1)))=2^(O(N^beta))`. For each description `d`, build

```text
E_d(x) = AND_{i<N} [x_i = C_d(i)],     Sep(x) = OR_d E_d(x).
```

This uses `O(NK)` two-input gates, accepts every Low table, and rejects every High table; it is allowed to reject the middle band. This is an explicit total-gate full-promise upper bound. The attempted compression was to share coordinate comparisons using a fingerprint or a trie over circuit descriptions. A fingerprint with false positives can accept a High table, and a trie only shares the prefixes actually present; neither gives a worst-case bound below `O(NK)` for all descriptions. No near-linear shared implementation was found.

## Status and quantitative effect

**Project-proved:** the serial query-substitution upper bound above. It refines C-437 by explicitly accounting for deterministic control and the cost of this particular one-copy-per-query compiler. It does not prove query-cost additivity or a lower bound on joint implementations; circuit direct sum is false in general (C-439).

**Open:** an exact promise-preserving one-table map for the source's prefix-existence computation, or a source-specific joint compiler whose full ordinary-gate cost is below `a*2^m/m`. The serial-substitution bound itself has not been shown below that threshold, and it is not necessary for every possible joint compiler.

**Frontier unchanged:** ordinary `N-O(N^beta log N)-1` plus C-406; OPS `N^(1+epsilon)` open with one fixed epsilon for every sufficiently small fixed beta; exact full-promise upper `O(N*2^(O(N^beta)))`; native `rho>=N-o(N)` separate. This is a transfer accounting lemma, not a GapMCSP lower bound or a P-vs-NP proof.

The exact OPS thresholds are those of [Oliveira-Pich-Santhanam, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf): YES `2^(beta n)/(c n)`, NO `>2^(beta n)`, and the magnification premise requires a common positive epsilon for every sufficiently small fixed beta. For the first-principles correction to the additivity interpretation and the revised single-table-map target, see [C-439](C439_FIRST_PRINCIPLES_AUDIT_AND_JOINT_COMPOSITION_2026-10-01.md).
