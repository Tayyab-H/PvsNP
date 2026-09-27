# C-221 — Seed-feature separation versus closure readout

Date: 27 September 2026  
Scope: sharpen the native fusion lower-bound target after C-220. This is a proved structural lemma and route filter, not a superlinear bound.

## Setup

Let `Y=SIZE(s1)`, `Z={0,1}^N minus SIZE(s2)`, and let a successful fusion list have `q` pairs. Its two seed predicates per pair are clauses `C_j(x)=OR_{(k,b) in S_j} [x_k=b]`, so there are at most `m=2q` clauses. Write `sigma_Q(x)` for their truth vector. The least-fixed-point output `h_Q(sigma)`—whether some empty-carrier rule activates—is monotone in `sigma`: the rule equations use positive ORs and ANDs and iteration starts at zero. Success means `h_Q(sigma(w))=1` for every `w in Y` and `h_Q(sigma(z))=0` for every `z in Z`.

## Theorem: seed predicates already separate every promised pair

For every `(w,z) in Y x Z`, there is a seed clause `C_j` with `C_j(w)=1` and `C_j(z)=0`.

**Proof.** If no such clause existed, then every 1-coordinate of `sigma_Q(w)` would also be 1 in `sigma_Q(z)`, so `sigma_Q(w)<=sigma_Q(z)` coordinatewise. Monotonicity would imply `1=h_Q(sigma_Q(w))<=h_Q(sigma_Q(z))=0`, a contradiction. This does not require unfolding a closure path.

For a clause `C_j`, its zero set `B_j={x:C_j(x)=0}` is a subcube: all selected signed literals are fixed false. Thus the seed family covers `Y x Z` by the oriented subcube cuts `(Y minus B_j) x (Z intersect B_j)`. Let `kappa(Y,Z)` be the minimum number of such subcube cuts covering every ordered pair in `Y x Z`. Every successful q-pair fusion list satisfies `2q >= kappa(Y,Z)`.

## Exact ceiling of feature-only arguments

For any disjoint `Y,Z subseteq {0,1}^N`, the `2N` signed-literal clauses cover all pairs: for `w!=z`, choose a differing coordinate `k` and literal `[x_k=w_k]`. Hence `kappa(Y,Z)<=2N`. For the OPS promise, `kappa(Y,Z)>=N-log2(M2)`, where `M2=|SIZE(s2)|`: fix any `w in Y` and let `J_w={j:C_j(w)=1}`. Every high `z` must falsify at least one clause in `J_w`, so `AND_(j in J_w) C_j` has at most `M2` satisfying assignments. It is satisfied by `w`; choosing one true literal per clause leaves a subcube of at least `2^(N-|J_w|)` assignments. Therefore `|J_w|>=N-log2(M2)`, and the global family has at least that many clauses.

Under the canonical OPS parameters `s2=N^beta` and `s1=N^beta/(c n)`, the standard circuit-description count gives `log2(M2)=O(s2 log(s2+n))=O(N^beta n)=o(N)` for fixed `0<beta<1`. So the feature-cover interval is `[N-O(N^beta n),2N]`: it is genuinely pinned to linear scale, rather than merely having a weak asymptotic lower bound.

This recovers the linear seed-count floor but proves that **pairwise seed-feature separation alone cannot yield a superlinear q lower bound**: the universal signed-literal family uses 2N features. A superlinear result must charge how the closure/readout combines these features, not merely how many seed clauses distinguish pairs, anchors, or mismatch coordinates.

## Refined model language

The C-75 object factors into two stages:

1. **Feature map:** `sigma_Q(x)` consists of `2q` ORs of signed table literals. Pairwise correctness forces `sigma_Q(Y)` to be order-separated from `sigma_Q(Z)` (`sigma_Q(w) not<= sigma_Q(z)`). Feature dimension alone has a universal `2N` solution.
2. **Closure readout:** a positive least-fixed-point program with `q` paired AND rules maps those feature vectors to 1 on `Y` and 0 on `Z`. It must pair supports, reuse predecessor carriers, and avoid activating an empty carrier on any high table. This is the part not captured by the subcube-cut cover.

Thus O-141 is sharpened: find an OPS-specific lower bound on the **readout/closure interaction cost beyond the linear seed-cut cover**, or exhibit a compact readout that gives a near-linear successful cover. Counting clauses, mismatch supports, or low/high pairs alone cannot deliver the target. The known `q -> S_rect=O(q^3/log q)` loss and `N^(3+3epsilon)/log N` separator threshold are unchanged. No superlinear `q`, `S_rect`, or P-vs-NP bound follows.

## C-221-A: wide minimal activation certificates

Let `U` be an inclusion-minimal set of seed indices with `h_Q(1_U)=1`, and suppose the clause conjunction `Phi_U=AND_(j in U) C_j` is satisfiable by at least one truth table. Every table satisfying `Phi_U` has seed vector at least `1_U`, so monotonicity forces the closure output to 1 there. Success therefore implies that `Phi_U` has no high-complexity model and has at most `M2` models. At any satisfying table, choose one true literal from each nonconstant clause; fixing those literals leaves a subcube of size at least `2^(N-|U|)` inside `Phi_U`. Tautological clauses do not reduce the model set and can be omitted from this count. Hence every such realizable minimal activation certificate has `|U|>=N-log2(M2)`.

Every low table contains one of these wide certificates, while every high table contains none. This is stronger than merely saying each low/high pair has a separating seed feature: it describes the monotone readout's certificate hypergraph. But width alone again gives only `q>= (N-log2(M2))/2`, since there are 2q seed indices. A useful next theorem must lower-bound the number/overlap/readout complexity of a family of wide, clause-consistent certificates that covers all low circuit tables and excludes every high one. The certificate statement is proved; such a global bound is not.

