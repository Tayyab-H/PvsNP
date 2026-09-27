# C-216 — Column-deficit profile for a shared Q-signature state

Date: 27 September 2026

## Statewise theorem

Fix the C-190 coordinate set `Q`, with `k=|Q|`. At a valid rect-DAG state `v`, let `A_v × B_v` be its product rectangle, `K_v` its descendant output coordinates, `P_v=K_v∩Q`, and `T_v=K_v\Q`, with `t_v=|T_v|`. Let `r_v` count Q-signatures `σ` for which both `A_v∩Y_σ` and `B_v∩Z_σ` are nonempty. Put

`M2 = |SIZE(s2)|`, `Z = {0,1}^N \ SIZE(s2)`, and `Δ_v=|Z\B_v|`.

**Profile lemma.**

\[
r_v 2^{N-k-t_v} \le M_2+\Delta_v.
\]

Equivalently, for `r_v>0`,

\[
\log_2 r_v+(N-k-t_v)\le \log_2(M_2+\Delta_v).
\]

**Proof.** For each of the `r_v` common signatures `σ`, choose `w_σ∈A_v∩Y_σ` and consider the cylinder

\[
C_\sigma=\{z:z|_Q=\sigma,\ z|_{T_v}=w_\sigma|_{T_v}\}.
\]

These cylinders are disjoint and each has `2^(N-k-t_v)` members. Any high table in `C_σ∩B_v` would agree with `w_σ` on `P_v` (because it has the same full Q-signature) and on `T_v`, hence on every descendant output coordinate. That violates correctness of `v`. Thus every high point in their union lies in `Z\B_v`; at most `M2` points in the union are non-high. Therefore `Δ_v ≥ r_v 2^(N-k-t_v)-M2`, giving the claim.

The argument also shows why the exact common-signature count matters: `r_v` is a count of signatures present on **both** sides, while the root count is the number of distinct low Q-traces.

## Root specialization and C-212 scale

At the root, `B_root=Z`, so `Δ_root=0`. Since `N-k>log2(M2)` in the OPS parameters, every low Q-signature has a high completion with the same Q-values. Hence `r_root=r_Q=|π_Q(Y)|`, and

\[
t_{root}\ge N-k+\log_2 r_Q-\log_2 M_2.
\]

This strengthens C-215's simpler `r=1` completion argument by the additive term `log2(r_Q)`. C-212 gives `log2(r_Q)=Ω(s1 log n)` for the C-190 choice of `Q`; this is still lower order than the `O(s2 n)` circuit-count term `log2(M2)`, so the asymptotic root support remains `N-o(N)`. If the root exposes only `p=|P_root|` Q-coordinates, the corresponding total-support statement is

\[
|K_{root}|\ge N-\log_2 M_2+\log_2 r_Q-(k-p).
\]

Thus unused Q coordinates consume the trace-diversity gain one-for-one. This is an exact support/exit tradeoff, not a superlinear state bound.

## Transition audit

The excluded-column quantity is monotone down every protocol edge because a child column side is a subset of its parent's. At an Alice-owned split, both children retain `B_u`, so `Δ_v=Δ_u` for either child. Each child therefore obeys the same budget

\[
r_v2^{N-k-t_v}\le M_2+\Delta_u.
\]

At a Bob-owned split, the two column sides partition `B_u`; hence

\[
\Delta_{v_0}+\Delta_{v_1}=|Z|+\Delta_u.
\]

Applying the profile to both children yields

\[
r_{v_0}2^{N-k-t_{v_0}}+r_{v_1}2^{N-k-t_{v_1}}
\le 2M_2+|Z|+\Delta_u.
\]

Since each child tail support is contained in the parent tail support, this also implies

\[
(r_{v_0}+r_{v_1})2^{N-k-t_u}\le 2M_2+|Z|+\Delta_u.
\]

This is the strongest direct transition inequality obtained from the cylinder count. Its Bob-side right-hand side contains `|Z|`, which is essentially `2^N`; for states whose omitted-tail count is small it gives little. At Alice nodes the same deficit is available independently to both children, so summing child inequalities double-counts it. These are the precise failures of the scalar-profile aggregation.

The natural scalar `log r_v + N-k-t_v - log(M2+Δ_v)` is nonpositive at every state, but neither its node sum nor its variation along paths is bounded usefully by DAG size: Alice splits duplicate the same deficit across children; Bob splits partition columns, but the complement of one child's column side is off-path for pairs taking that child. C-80/C-160 continue to rule out summing those off-path masses without a parent-conditioned charging argument.

## Literature boundary checked this turn

Carmosino, Dang, and Jackman's STACS 2026 paper proves that the XOR simple-extension problem is in polynomial time and identifies MUX as a candidate for hardness of a different total simple-extension problem. This is useful evidence about the distinction between partial-function completion and complete-table circuit size, but supplies neither a reduction to the C-75 sparse-envelope separator nor a state-merging lower bound. Primary source: [*Simple Circuit Extensions for XOR in PTIME*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.23).

## Disposition

C-216 sharpens a local support constraint by using signature multiplicity and makes the Alice/Bob transition arithmetic explicit. The Alice equation duplicates the column-deficit allowance, while the Bob equation pays an additive `|Z|`; neither yields a global superlinear bound. O-141 remains open. The required standard rect-DAG transfer threshold is unchanged: `S_rect > N^(3+3ε)/log N` to imply `rho_prom > N^(1+ε)` under `S_rect=O(q^3/log q)`. No actual-promise superlinear bound or P-vs-NP proof follows.
