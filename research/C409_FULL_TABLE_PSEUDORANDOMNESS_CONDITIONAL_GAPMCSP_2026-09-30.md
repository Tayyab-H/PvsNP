# C-409 — Full-table pseudorandomness conditionally rules out small Gap-MCSP separators

**Status:** a proved conditional implication, not an unconditional lower bound. It supplies an explicit distributional mechanism that controls arbitrary sharing: a small separator would distinguish low-circuit PRF truth tables from uniform truth tables. The local-PRG method is established prior art; this is a parameter-matched application to the OPS gap and does not change the unconditional frontier.

## Exact target parameters

Let `N=2^n`, `s1=N^beta/(c n)`, and `s2=N^beta`, where OPS Theorem 1.4 has a universal constant `c` and its proof gives the concrete choice `c=10`. A promised YES table has circuit size `<=s1`; a promised NO table has circuit size `>=s2`; the middle is unconstrained. The magnification quantifiers are one fixed `epsilon>0` and every sufficiently small fixed `beta>0`. A lower bound excluding size-`N^(1+epsilon)` separators at these thresholds implies `NP` is not contained in `P/poly`.

## Conditional theorem

Fix `epsilon>0` and `0<beta<1`. Suppose a distribution `D_n` over `N`-bit truth tables satisfies:

1. Every table in the support of `D_n` has an `n`-input circuit of size at most `L(n)`.
2. `D_n` is indistinguishable from the uniform distribution `U_N` by nonuniform fan-in-two circuits of at most `N^(1+epsilon)` gates, with distinguishing advantage less than `1/3` for all sufficiently large `n`.

If `L(n)<=N^beta/(c n)` eventually, then no size-`N^(1+epsilon)` circuit separates the OPS `Gap-MCSP[s1,s2]` promise for this `beta`.

In particular, if `D_n` is the truth-table distribution of a PRF on `n`-bit inputs keyed by `k=n^2` bits, each keyed function is evaluable by `poly(n)` gates. Thus every fixed `0<beta<1` eventually satisfies the Low threshold. Security against nonuniform truth-table distinguishers of size `2^((1+epsilon)n)` would therefore rule out the Gap-MCSP separator for every such fixed `beta`.

## Proof

Assume a valid separator `A` of size at most `N^(1+epsilon)` exists. It accepts every table in the support of `D_n`, since those tables are Low. A uniformly random `N`-bit table is High with probability `1-o(1)`: the number of circuits of size below `s2` is at most

`(s2+1)(3(n+s2+2)^2)^s2 = 2^(O(s2 log(n+s2))) = 2^(O(N^beta n)) = 2^o(N)`

for each fixed `beta<1`. Therefore `A` rejects a uniform table with probability `1-o(1)`, because every promised NO table must be rejected. Consequently `A` distinguishes `D_n` from `U_N` with advantage `1-o(1)`, contradicting condition 2. This proof treats `A` as an arbitrary circuit; it does not assume it extracts a circuit description, enumerates witnesses, checks addresses separately, or preserves caller history.

The key-length calibration is exact: with `k=n^2`, the target distinguisher size is `2^((1+epsilon)sqrt(k))`. A PRF assumption providing security up to `2^(k^alpha)` for any fixed `alpha>1/2` is stronger than this size bound asymptotically. This is only a parameter comparison; this cycle does not prove a reduction from one-way functions to the required full-table security notion.

## Adversarial checks and cheapest attacks

- **Affine/parity generator:** if `D_n` is uniform over affine functions, the tables are Low, but a circuit can check that every first derivative is constant (equivalently, test all affine parity constraints) in `O(N log N)` gates. This distinguishes it from uniform and is much smaller than `N^(1+epsilon)`. Sparse parity-check and simple global XOR generators fail similarly when they expose linear relations.
- **Repeated blocks:** a generator that repeats each output bit across address blocks is Low, but a circuit checks block equality in `O(N)` gates. C-258 and C-408 give additional repeated-block counterchecks.
- **Random tables:** the circuit-count estimate above shows that the uniform side is High except with probability `2^{-N+o(N)}`; this estimate is the required NO-distribution audit, not a finite experiment.
- **Key search:** for a `k=n^2`-bit key, straight exhaustive key search costs `2^k` candidate trials, far above `N^(1+epsilon)=2^((1+epsilon)n)`. This removes the immediate brute-force distinguisher but does not establish PRF security; any faster distinguisher remains possible unless excluded by the stated assumption.

## Resource and scope audit

- **Separator:** total Boolean gates `N^(1+epsilon)`; a circuit description takes `O(N^(1+epsilon) log N)` bits. The assumption covers unrestricted fanout and sharing.
- **Distribution sampler:** a PRF oracle adversary can obtain the complete table with `N` queries and then run `A`; its work is `O(N+|A|)=O(N^(1+epsilon))`. The PRF evaluation circuit with a fixed key has `poly(n)` gates, below `s1` for every fixed `beta>0` eventually. Sampler work and separator gates are distinct measures.
- **Uniform side:** generating and presenting `U_N` takes `N` random bits; the separator's correctness is used only on promised High inputs.
- **Native fusion:** no paid-AND, OR-rule, semantic-endpoint, wide-seed, cycle, or semi-filter extension bound follows. There is no ordinary-to-native compiler.
- **Near-linear full-promise upper attempt:** the distance-to-constant separator still omits dense low tables; exact circuit enumeration still costs `O(N*2^(O(N^beta)))`. C-409 yields no upper bound.

## Literature, originality, and frontier effect

Cheraghchi, Kabanets, Lu, and Myrisiotis already give a general MCSP lower-bound framework from local PRGs: if a generator fools the separator class and every output truth table is locally computable, a separator would accept the generator outputs but reject almost every uniform table. Their applications yield strong lower bounds for formulas and restricted-depth circuits, not unrestricted circuits at the OPS exponent. C-409 is the direct general-circuit, exact-gap specialization of that known framework, with a key-length parameterization that aligns `N=2^n` and `N^(1+epsilon)` security; it is not claimed as a new PRG principle.

This is also consistent with the natural-proofs/locality picture: a separator for Low versus random High is itself an efficient distinguisher for any sufficiently secure distribution supported on Low tables. The security assumption is substantially stronger than standard polynomial-time PRF security in parameter `n`; the `k=n^2` choice merely makes the scale comparison possible. No unconditional generator with this security is constructed here.

**Exact frontier effect:** conditional on the stated full-table PRF security, the ordinary OPS separator lower bound follows for any fixed `epsilon` covered by that security, for every fixed `0<beta<1` with `poly(n)<=s1`. This supplies OPS's “one fixed epsilon, every sufficiently small beta” premise and therefore conditionally implies `NP` is not contained in `P/poly`. The security assumption itself is not proved. Unconditionally, `S>=N-O(N^beta log N)-1` and C-406's additive `E(C)+gamma log_2N-O(1)` refinement remain the strongest recorded bounds; the `N^(1+epsilon)` OPS target and native `rho_GapMCSP>=N-o(N)` remain open.

### Primary sources checked

- Oliveira, Pich, Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and the OPS gap parameters.
- Cheraghchi, Kabanets, Lu, Myrisiotis, [*Circuit Lower Bounds for MCSP from Local Pseudorandom Generators*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol132-icalp2019/LIPIcs.ICALP.2019.39/LIPIcs.ICALP.2019.39.pdf), especially the local-PRG framework in Section 1.2.
- Chen, Hirahara, Oliveira, Pich, Rajgopal, Santhanam, [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://arxiv.org/abs/1911.08297), for the method-level locality barrier. This conditional distribution argument is not an unconditional lower-bound technique that bypasses the barrier.
