# C-327 - Succinct matching audit: logarithmic independence is below the needed width

Date: 28 September 2026  
Route: bounded-independence secondary audit from the C-319 continuation directive.  
Classification: **PARAMETER ROUTE-KILL FOR k=O(log N); NO SOURCE TRANSFER.**

## Question and construction

Take the matching source on `K_(v,v)` and set `v` to a power of two, so it can be identified with a permutation domain of size `2^m`. Kaplan, Naor, and Reingold construct `k`-wise `delta`-dependent permutation families with description length `O(k log v + log(1/delta))`; each permutation is a perfect matching. Thus for `v=polylog(N)`, the requested choice `k=O(log N)` does have a polylogarithmic seed description. The construction itself is not the obstruction.

Concretely, set `v=2^m` within a constant factor of `(log N)^K`, take `k=ceil(log N)`, and choose `delta=N^-10`. The seed length is `O(log N * loglog N)`, and the family is explicit. It reproduces every fixed matching-term containment probability of width at most `k` to additive error at most `delta`.

The low-witness circuit requirement is already met in the project parameterization: C-308 bounds the matching-indicator witness tables by `O(v log N/log v)` gates, which is polylogarithmic in N when v is polylogarithmic. This source-side property is independent of the pseudorandom seed. It does not repair the width mismatch or produce an all-input C-125 map.

For a fixed `ell`-edge matching term `T`, the event `T subseteq M` under a uniform perfect matching is a conjunction of `ell` specified values of the permutation. Exact `ell`-wise independence preserves its probability `1/(v)_ell`; almost independence preserves it up to the stipulated statistical error. Under the odd-cut distribution, a matching term of width `ell<v` has exact mass `2^(-ell)` (C-310), and this event depends on the colors of its `2ell` endpoints. These are the local probabilities used by the matching-sunflower approximation.

## Required independence order

C-310 uses matching-DNF width

```text
w = Theta(v^(1/3) / (log v)^(2/3)),
```

and obtains a source lower bound `exp(Omega(w))`. For `v=(log N)^K`,

```text
w/log N = Theta((log N)^(K/3-1) / (loglog N)^(2/3)).
```

The source bound can dominate `N^(1+epsilon)` only with a fixed margin when `K>3`; then `w=omega(log N)`. At `K=3`, `w=o(log N)` and `exp(Omega(w))=N^(o(1))`, too small for the intended polynomial transfer. Therefore a `k=O(log N)` family falls short of the width needed for the only audited parameter range that could beat the linear barrier. One needs at least `k>=w` for matching-term containment probabilities, and up to `2w`-wise control for the raw cut-coordinate event.

Taking `k=Theta(w)` would still give `polylog(N)` description length by the Kaplan-Naor-Reingold bound when `v=polylog(N)` and `log(1/delta)` is polylogarithmic. But this does not finish a derandomization: the approximant is a DNF with many terms, so preservation of each term probability alone does not preserve the probability of their union. A complete transfer would need a sufficiently small `delta` together with an error accounting for all terms and for the sunflower-plucking steps. More decisively for this project, it would still supply no new all-input C-125 encoder or positive reconstruction/decision margin. Under the directive to stop this experiment unless both source hardness and a new encoder architecture survive, the larger-k variant is not pursued here.

## Disposition

The requested logarithmic-wise family is succinct but too weak for the sunflower width at a parameter that could yield superlinear transfer. This closes only the `k=O(log N)` pseudorandom-matching experiment, not the matching source itself and not the native Gap-MCSP route. No CohEnc construction, q improvement, near-linear full-promise cover, or P-vs-NP proof follows. The actual fusion lower bound remains `q=N-o(N)`.

Primary sources: Kaplan, Naor, and Reingold, [*Derandomized Constructions of k-Wise (Almost) Independent Permutations*](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/kwise.pdf), Theorem 5.9; Cavalar et al., [*Monotone Circuit Complexity of Matching*](https://eccc.weizmann.ac.il/report/2025/102/revision/1/download), Matching Sunflower Lemma; project derivation C-310, `research/C310_ODD_CUT_TERM_MASS_TIGHTENS_COHENC_2026-09-28.md`.
