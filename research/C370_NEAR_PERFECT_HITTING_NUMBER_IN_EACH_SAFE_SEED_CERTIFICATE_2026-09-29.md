# C-370 - Safe seed certificates have near-full literal-support hitting number

Date: 29 September 2026  
Route: refine C-368 by studying the variable supports of literals that are true at a fixed accepted table.  
Classification: **EXACT CERTIFICATE STRUCTURE; MANY DISJOINT SPARSE WITNESSES; NO q IMPROVEMENT YET.**

## 1. True-literal hypergraph of a certificate

Fix a C-319 cover with q state pairs, a low table `f` accepted by the cover, and a sufficient seed certificate `S_f` as in C-368. Let its m nonconstant seed clauses be `C_1,...,C_m`, with `m<=2q`. For each clause define

\[
E_j(f)=\{a\in[N]:\text{the literal on }w_a\text{ in }C_j\text{ is true at }f\}.
\]

Every `E_j(f)` is nonempty. Form the hypergraph `H_f` on the N table coordinates with these m edges. Write `h=log2 |SIZE(s2)|`.

## 2. Hitting-number lower bound

If `X` hits every edge `E_j(f)`, fix the coordinates in X to their values in f. Each clause retains at least one f-true literal, so every completion of the other coordinates satisfies the certificate CNF. The cone is sound and contains at most `|SIZE(s2)|=2^h` tables. Therefore

\[
2^{N-|X|}\le 2^h,
\qquad |X|\ge N-h.
\]

Thus the transversal number satisfies `tau(H_f)>=N-h=N-o(N)`. This is a support-sensitive strengthening of the clause-count argument: every set of fewer than `N-h` coordinates misses all f-true literals of at least one certificate clause.

## 3. A support-size hierarchy and a matching

For an integer `k>=1`, let `t_k` be the number of certificate edges of size at most k. Put

\[
\delta_k=(2m)^{-1/(k+1)}.
\]

Sample each table coordinate independently into a set R with probability `1-delta_k`. Every edge of size greater than k is missed with probability at most `delta_k^(k+1)=1/(2m)`. The expected number of missed large edges is at most 1/2; adding one vertex from each missed edge gives a hitting set for the large-edge subfamily of expected size at most `(1-delta_k)N+1/2`. Hence its transversal number is at most `(1-delta_k)N+1`. Hit each of the `t_k` small edges separately and combine the hitting sets. Since `tau(H_f)>=N-h`,

\[
t_k+(1-\delta_k)N+1\ge N-h,
\qquad
t_k\ge \delta_k N-h-1.
\tag{1}
\]

This holds for every k. For polynomial m, choosing `k=ceil(log2(2m))` gives `delta_k>=1/2`, so at least `N/2-h-1` certificate clauses have at most `O(log m)` f-true literals. If `m=O(N)` and `h=O(N^beta log N)` with fixed `beta<1/2`, choosing `k=1` in (1) gives at least `Omega(sqrt(N))` clauses with a singleton f-true support. More generally, for fixed k and `m=O(N)`, `t_k>=c_k N^(1-1/(k+1))-h-1` for a constant `c_k>0` depending only on the hidden constant in m=O(N).

The logarithmic-size subfamily itself has transversal number at least `N/2-h-1`. A maximal pairwise-disjoint collection of these edges has a union hitting every small edge, so its size nu obeys

\[
\nu\ge\frac{N/2-h-1}{\lceil\log_2(2m)\rceil}.
\]

For polynomial q this supplies `Omega(N/log N)` pairwise coordinate-disjoint certificate clauses, each with at most `O(log N)` literals true at that table. These support bounds do not themselves charge state reuse.

## 4. Hostile calibration and scope

For the repeated-fiber family of C-369, the common equality CNF has two clauses per equality pair. At a valid table each clause has a singleton f-true support, and the supports collectively hit essentially all coordinates. This makes the hitting-number conclusion tight at the clause level and is compatible with C-258's separate linear native subcover. It does not claim that this CNF is the seed certificate extracted from the C-258 graph. C-257's artificial parity universe also causes no conflict: when the sound accepted region has size about `2^(N-1)`, h is about N and the lower bound is vacuous, as it should be.

This proves a structural fact about each certificate, not a state lower bound. It does not say the disjoint supports are private across different anchors, that their clauses force different states, or that a compatible C-281 splice exists. The next step is to relate these near-disjoint f-true support systems across a high-distance low-circuit family to positional state reuse and endpoint incidence. Any charging theorem must still survive the C-258 equality and C-257 parity calibrations.

## 5. Checkpoint

- Every sound certificate cone has true-literal support hitting number at least `N-log2|SIZE(s2)|`: **proved**.
- It contains at least `(N/2-h-1)/ceil(log2(2m))` pairwise-disjoint f-true supports of size at most `ceil(log2(2m))`: **proved**.
- This implies a superlinear q bound or a full-promise near-linear cover: **no**.
- Actual native lower bound remains `rho_GapMCSP>=N-o(N)`.
