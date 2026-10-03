# C-469 - the average-MCSP route is established, but its exact transfer is blocked

**Status:** primary-literature and parameter audit. It identifies an existing magnification framework for the C-465 viewpoint, but does not produce an OPS lower bound or a near-linear separator.

## 1. Project implication, with exact endpoints

Let `N=2^n`, `s1=floor(N^beta/(10n))`, and `s2=N^beta`. If `F` is any total OPS separator, define

```text
A_F(T) = 0  if F(T)=0,
         ?  if F(T)=1.
```

For exact threshold MCSP at `s1`, this is a zero-error average solver: it never says 0 on a table of complexity at most `s1`, and its only ordinary answer is 0. Since every circuit of size at most `s2` has one of `2^{O(s2 log(n+s2))}=2^{O(N^beta n)}` descriptions, a uniform table is High with probability `1-2^{-N+O(N^beta n)}`. The separator rejects every such High table, so

```text
Pr_uniform[A_F(T) != ?] >= 1 - 2^{-N+O(N^beta n)}.
```

This is much stronger success than the constant-success average-solvers used in the magnification literature. It is a one-way implication: a general `NO/?` average solver can abstain on promised High inputs and need not extend to a full OPS separator.

## 2. Established theorem found in the literature

Oliveira and Santhanam define zero-error average MCSP computation by a device that never errs and answers on a nontrivial fraction of uniform truth tables; their appendix gives the stronger convention of answering on at least `1-1/n` of inputs. Their Theorem 27 states, for a typical circuit class `C` and a constructible threshold `n <= s(n) <= 2^{o(n)}`, that if MCSP at threshold `s(n)` requires `C`-circuits of size `Omega(N^delta)` on average for some fixed `delta>0`, then a language in NP requires `C`-circuits of size `2^{Omega(n)}` on lengths `m=Theta(n*s(n)*log s(n))`. Their Theorem 5 gives a formula-specialized result for threshold `2^{sqrt(n)}`. Sources: [ECCC TR18-139 page](https://eccc.weizmann.ac.il/report/2018/139/) and [paper PDF](https://eccc.weizmann.ac.il/report/2018/139/download).

The OPS hardness-magnification theorem is the more direct source for the project target: one fixed `epsilon>0` and every sufficiently small fixed `beta>0` at the gap `N^beta/(10n)` versus `N^beta` imply `NP not-subset P/poly`. See [Oliveira, Pich, and Santhanam, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/).

## 3. Exact transfer audit

The C-465 solver has the right *zero-error and density shape* for average MCSP, but the known results do not supply the missing proof:

1. For fixed `beta>0`, `s1=2^{beta*n}/(10n)=2^{Theta(n)}`, not `2^{o(n)}`. Thus it is outside Theorem 27's stated threshold range. A varying sequence `beta(n)->0` could make `s1=2^{o(n)}`, but the project has no lower bound for **all** average solvers at that variable threshold; the fixed-beta separator hypothesis only excludes full separators, a smaller device class.
2. Theorem 27 is an implication from an average-case **lower bound** to NP circuit lower bounds. The existence of `A_F` is an upper bound for a special solver if a small separator exists. It gives no unconditional lower bound against all `NO/?` solvers.
3. Completing an arbitrary average solver into a full promise separator by brute force on its abstention set can cost `2^{O(N^beta)}` descriptions, so no near-linear completion compiler follows.
4. The related Hirahara--Santhanam proposition uses thresholds of the form `2^k/k^{omega(1)}` under its stated rescalings. Setting `k=beta*n` at fixed OPS beta leaves the OPS denominator only `Theta(n)`, not `k^{omega(1)}`. The exact transfer previously audited in C-466 remains absent.

The route is therefore not a forgotten theorem that solves this target. The useful research possibility is narrower: prove a new average-case lower bound for the special dense, zero-error `NO/?` property induced by separators, or prove a costed reduction from such an average solver to a full-promise separator. Neither is established here, and the second would need to avoid exponential abstention completion.

## 4. Paired full-promise upper attempt

No new circuit construction emerged from the average-solver reduction. The unconditional full-promise separator still enumerates all `K=2^{O(N^beta)}` Low circuit descriptions and compares the input table to each; the direct ordinary-gate cost is `O(NK)`. The `NO/?` device is not a full separator, and the average magnification theorem does not construct one. No near-linear full-promise upper was found.

## 5. Claim classification and exact frontier

- **Published:** the Oliveira--Santhanam average-MCSP hardness-magnification theorem and its threshold `s(n)<=2^{o(n)}`; the OPS fixed-epsilon Gap-MCSP magnification theorem.
- **Project-proved:** an OPS separator yields a zero-error average MCSP solver with success `1-2^{-N+O(N^beta n)}` by circuit counting.
- **Not proved:** average-case hardness for all such solvers at OPS fixed-beta thresholds, a near-linear solver-to-separator compiler, or a new P-vs-NP consequence beyond OPS.
- **Mechanism verdict:** retain average MCSP as a precise lens and source of possible new reductions. Do not list it as an independent shortcut or claim C-465 as a new magnification theorem.

The ordinary gate lower bound remains `N-O(N^beta log N)` with C-406's additive logarithmic reconvergence refinement. The exact full-promise upper remains `O(N*2^(O(N^beta)))`. OPS's common-fixed-epsilon target, native `rho>=N-o(N)`, and P-vs-NP remain open.
