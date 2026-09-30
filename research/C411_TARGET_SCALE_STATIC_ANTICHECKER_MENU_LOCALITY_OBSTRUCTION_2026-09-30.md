# C-411 — Locality obstructs target-scale fixed anti-checker menus

**Status:** proved parameterized no-go for one static-menu route, by reduction to the published locality theorem. This is not a lower bound against ordinary Gap-MCSP circuits and does not affect the adaptive OPS selector.

## Statement

Let `N=2^n`, fix constants `kappa>=1`, `beta>0` with `kappa*beta<1`, and use the concrete OPS gap

```text
s1 = 2^(beta*n)/(10n),       s2 = 2^(beta*n).
```

Suppose a proposed nonuniform menu `Y_n={Y_1,...,Y_L}` has

```text
L <= N^(2-delta),       |Y_i| <= N^(kappa*beta),
```

for a fixed `0<delta<2`, and for every truth table `f` with circuit complexity greater than `s2`, some `Y_i` is an anti-checker against every circuit of size at most `s1`:

```text
for every C of size <= s1, there is y in Y_i with C(y) != f(y).
```

If

```text
delta > (3*kappa + 2)*beta,
```

then no such menu exists for all sufficiently large `n`.

For the OPS anti-checker list exponent `kappa=10`, this rules out every static menu of size `N^(2-delta)` whenever `delta>32 beta`. In particular, any fixed positive exponent saving `delta` is impossible for all sufficiently small fixed `beta<delta/32`.

## Proof

Let `SC_n` be the NP language for Succinct-MCSP consistency: given a list of address/label pairs and unary bounds `s1,t`, accept iff some `n`-input circuit of size at most `s1` matches every pair. Its input length for `t=N^(kappa*beta)` is

```text
m = O(n + s1 + t*n) = N^(kappa*beta + o(1)),
```

because `kappa>=1` and `t*n` dominates the unary circuit-size field up to subexponential factors.

Build an oracle formula `F_n` whose root is an AND of `L` oracle calls to `SC_n`. The `i`-th query hardwires the addresses in `Y_i` and uses the corresponding truth-table input bits `f(y)` as the labels. No Boolean computation is needed to project these fixed coordinates; repeated coordinates may simply occur as repeated formula inputs. If `|Y_i|<t`, use a variable-length encoding or pad by consistent repeated samples. Each oracle gate has fan-in at most `m`.

If `CC(f)<=n^c`, then eventually `n^c<=s1`, so `f` itself witnesses every query and `F_n(f)=1`. If `CC(f)>s2`, the assumed menu contains an anti-checker `Y_i`; no circuit of size `s1` fits that list, so its oracle call rejects and `F_n(f)=0`. Therefore `F_n` computes the promise problem `MCSP[n^c,2^(beta*n)]`; its output on the middle band is immaterial.

There is one oracle on each root-to-leaf path, so adaptivity is `1`. Under the published `SIZE_3` oracle-formula measure, a fan-in-`m` oracle whose inputs are leaves contributes at most `m^3`. Thus

```text
SIZE_3(F_n) <= L*m^3 + O(L)
             <= N^(2-delta + 3*kappa*beta + o(1)).
```

The locality theorem of Chen, Hirahara, Oliveira, Pich, Rajgopal, and Santhanam states that for every constants `epsilon_loc>0` and `alpha>2`, `MCSP[n^c,2^((epsilon_loc/alpha)*n)]` has no oracle formula of `SIZE_3<=N^(2-epsilon_loc)` and adaptivity `o(log N/log log N)`. If `delta>(3*kappa+2)*beta`, choose

```text
2*beta < epsilon_loc < delta - 3*kappa*beta,
alpha = epsilon_loc/beta > 2.
```

Then the locality theorem applies to exactly `MCSP[n^c,2^(beta*n)]`, while the assumed menu formula has the forbidden `SIZE_3` and adaptivity bounds. Contradiction. This proves the claim.

## Attacks, limits, and relation to earlier work

- The construction charges an entire menu query by its locality-aware oracle fan-in. It does not charge a separate `N`-gate multiplexer per label; C-410 already shows arbitrary batched readout can be done in `O((N+q)log^3(N+q))` ordinary gates, and fixed menu addresses are direct formula leaves.
- The exponent `3*kappa*beta` comes from the published `SIZE_3` measure and the `N^(kappa*beta)` sample length. The extra `2*beta` is the strict `alpha>2` condition in the locality theorem. The proof does not rule out menus with `delta <= (3*kappa+2)*beta`, larger menus, or adaptive selectors.
- Parity, repeated-block equality, sparse parity checks, and simple global block relations remain easy truth-table functions; they do not falsify the combinatorial menu premise by themselves. The contradiction instead guarantees that some hard table defeats every proposed menu in this parameter regime. This existence is nonconstructive.
- OPS's original static Anti-Checker Hypothesis, with much shorter sets, is already refuted by the same locality paper's Corollary 61. C-411 extends that route-specific obstruction to fixed-`beta` OPS scales and states the parameter loss explicitly. It is an application of published Theorem 59, not a new locality lower-bound technique.
- Nothing here implies that an arbitrary one-bit separator computes or outputs an anti-checker menu. The theorem only rules out the assumed static family; it says nothing about adaptive list generation or the selector-to-separator transfer.

## Full-promise upper attempt and frontier effect

The oracle formula above is an obstruction argument, not an ordinary Boolean circuit separator. Replacing each NP oracle by a polynomial-size circuit under `NP subseteq P/poly` does not provide a near-linear circuit: the exponent of that verifier is uncontrolled, and the stated implication is not an unconditional upper bound. Exact circuit enumeration remains `O(N*2^(O(N^beta)))`; no full-promise near-linear separator is obtained.

**Exact quantitative frontier:** unchanged. The ordinary total-gate lower bound remains `N-O(N^beta log N)-1`, with C-406's additive refinement. The OPS `N^(1+epsilon)` target and native `rho_GapMCSP>=N-o(N)` remain open. No paid-AND, OR, unrestricted-circuit, wire, description, runtime, or cyclic-closure bound follows.

### Primary sources

- Chen, Hirahara, Oliveira, Pich, Rajgopal, and Santhanam, [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol151-itcs2020/LIPIcs.ITCS.2020.70/LIPIcs.ITCS.2020.70.pdf), Theorem 59 and Corollary 61. Theorem 59 supplies the `SIZE_3` oracle-formula lower bound; the menu-to-oracle-formula construction and parameter inequality above are project derivations.
- Oliveira, Pich, and Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and Lemma 4.1 for the target thresholds and `kappa=10` anti-checker length.
