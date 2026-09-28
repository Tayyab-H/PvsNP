# C-302 - Raw owner-mask rank cannot yield the superlinear state bound

Date: 28 September 2026  
Classification: **INVARIANT FILTER / NEGATIVE CALIBRATION.** This tests C-281's proposed algebraic-rank branch. It retires rank of individual owner masks and affine dimension of safe hybrids as standalone routes; it does not prove a new q bound.

## Claim

An owner mask is a Boolean function on the `N` truth-table addresses, hence a vector in `GF(2)^N`. The linear span of any collection of such masks has dimension at most `N`. Therefore a lower bound on the rank of individual owner-mask vectors, even if tight, cannot by itself imply the desired `q>N^(1+epsilon)` for any fixed `epsilon>0`. It could contribute only through an additional theorem charging multiple independent mask families or their selection/synchronization cost to the native state count.

Affine dimension of the *safe hybrids* is no better as a generic substitute. In C-257's parity-lock promise, every compatible output splice is an even-parity table, so its hybrid lies in the even-parity subspace. That subspace has affine/linear dimension `N-1`; every even table is itself an accepted low anchor and therefore occurs as a diagonal proof/context hybrid. Yet the promise has a native cover with `q=4N-4`. Thus a nearly full-dimensional safe-hybrid family is compatible with linear q in the artificial calibration.

The parity construction is not the actual `SIZE(s1)` class. It falsifies only a promise-generic inference from large mask/hybrid rank to superlinear q. Any actual-promise algebraic argument must use the circuit-description structure of `SIZE(s1)` and the way a small grammar selects compatible owner masks. Merely attaching `GF(2)` rank to the N-bit masks loses that structure.

## Proof of the calibration point

C-257's low side is the even-parity subspace. For each even anchor `w`, completeness supplies an accepting finite proof. Cut that proof at any state occurrence into a context and a replacement proof. Their compatible join is the original output proof; its full support fixes `w`, so its canonical completion is `w`. As `w` ranges over all even tables, the set of safe canonical hybrids contains the entire even-parity subspace. Its dimension is `N-1`, while the explicit native list uses `4N-4` pairs. Soundness keeps all these hybrids safe.

## Research consequence

Retire raw `GF(2)` rank and hybrid affine dimension as standalone superlinear-q measures. A viable algebraic route must bind **selection** of owner masks to the circuit descriptions and to q shared states, while preserving the C-257 parity and C-258 repeated-block calibrations. No such bound is known. After C-301's ODDFACTOR route filter and this rank test, the next mechanism is the full-promise near-linear-cover attack/global circuit-description coherence, not another owner-mask count.

The actual lower bound remains `q=N-o(N)`. No `N^(1+o(1))` cover, superlinear q lower bound, Gap-MCSP exponent improvement, or P-vs-NP proof follows.

## Dependencies

- `research/C281_NATIVE_CYLINDER_GRAMMAR_AND_OWNER_MASK_FRONTIER_2026-09-27.md`
- `research/C257_PARITY_CODE_SPLICE_LOCKING_CALIBRATION_2026-09-27.md`
- `research/C258_REPEATED_BLOCK_NATIVE_COVER_2026-09-27.md`
