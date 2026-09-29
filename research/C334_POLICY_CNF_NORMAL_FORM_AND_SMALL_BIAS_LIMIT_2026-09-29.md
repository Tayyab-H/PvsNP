# C-334 — Policy CNFs sharpen the game normal form, but generic small-bias fooling still loses

Date: 29 September 2026  
Route: Q193 / test a parity-hidden low-circuit source against the exact policy language.  
Classification: **EXACT ACCEPTANCE NORMAL FORM + PARAMETER FILTER; NO q IMPROVEMENT.**

## 1. A low-circuit source that removes the C-333 parity witness

Naor–Naor construct an epsilon-biased sample space on N Boolean coordinates with seed length `O(log N+log(1/epsilon))`; given the seed and coordinate, the output bit is computable in polylogarithmic time. For `epsilon=N^{-c}`, fixing a seed therefore gives a truth table in `SIZE(polylog N)`, hence in `SIZE(s1)` for every fixed project beta and sufficiently large N. Every nonempty parity of the output has bias at most epsilon, so the linear-code parity distinguisher from C-333 is gone. See the [primary paper](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/bias.pdf), Theorem 3.2.

This is a genuine improvement over the trace-polynomial source for parity tests. It does not yet fool the alternating readout or the actual endpoint-realizable sound covers.

## 2. Exact policy-CNF normal form

Fix an accepted table w and a positional winning strategy from an empty root in the C-319 reachability game. For each state-side obligation used by the strategy, record either:

1. a fixed predecessor state; or
2. the fact that the corresponding whole seed clause is true.

The selected transition graph is well-founded by the attractor rank of w. Let `Sigma` be this fixed rooted strategy and let `R_Sigma` be the set of tables satisfying every seed clause on which Sigma stops. Then `R_Sigma` is a CNF region with at most `2q` clauses. For every table in `R_Sigma`, the same fixed transitions still terminate, and each seed-stop clause still has at least one true literal; thus Sigma wins throughout the entire region. Conversely each accepted table supplies such a strategy. Therefore

```text
Accept_Q = union over rooted well-founded policies Sigma of R_Sigma,
```

where each `R_Sigma` is a conjunction of at most `2q` seed clauses. This keeps the seed disjunction intact instead of selecting one witness literal, as C-329 did for its policy-cube form. Raw strategies number at most `q (q+2)^(2q)`: for each of 2q state-side obligations, choose unused, a seed stop, or one of at most q predecessors. However, a region depends only on the subset of the fixed 2q seed clauses used at stops. Thus there are at most `2^(2q)` distinct regions, regardless of how many transition policies induce each one.

For a sound full-promise cover, each satisfiable `R_Sigma` lies inside `SIZE(s2)`. A CNF with m clauses that is satisfied by w has at least `2^(N-m)` satisfying assignments: choose one w-true literal per clause, fix those at most m coordinates, and leave all others free. Hence `m >= N-log2 |SIZE(s2)| = N-o(N)`. Since `m<=2q`, this only gives `q >= (N-o(N))/2`, weaker than the current `N-o(N)` floor. The normal form is exact; this direct count is not a breakthrough.

## 3. Test of known small-bias / limited-independence bounds

Each distinct policy region is a CNF with at most `2q` clauses, and the acceptance set is a union of at most

```text
M = 2^(2q)
```

such regions. Bazzi's theorem says k-wise independence fools an m-clause CNF to error `O(m^2.2 2^(-sqrt(k)/10))`; see the [primary SIAM paper](https://epubs.siam.org/doi/10.1137/070691954). To fool each policy region to `epsilon/M` and then union-bound over all policies requires

```text
k = O(log^2(Mq/epsilon)) = O(q^2).
```

At `q=Theta(N)`, this exceeds N, so the generic limited-independence guarantee collapses to full-universe control and does not retain a low-circuit source. The estimate is a limitation of this per-region-plus-union-bound argument, not a lower bound against all PRGs; a direct PRG for the shared union of policy CNFs could behave differently.

## 4. What remains open

The useful distinction is now between (a) a parity-hidden low-circuit distribution, which exists explicitly, and (b) a distribution that fools the **union of all sound policy regions** with parameters that keep every output below s1. The live target is either a PRG/shrinkage theorem for this shared policy-CNF union that exploits strategy overlap and actual endpoint incidence, or a direct q lower bound for sound covers. A generic per-clause or per-policy union bound pays too much. Actual `q=N-o(N)` is unchanged; no full-promise cover, positive CohEnc margin, reconstruction compiler, or P-vs-NP proof follows.
