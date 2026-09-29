# C-321 - Activation-profile ceiling and the transition-readout frontier

Date: 28 September 2026  
Route: Q181 / C-319 exact state game.  
Classification: **RE-AUDIT; SUBSUMED BY C-76/C-221/C-260; NO NEW q RESULT.**

## 0. Novelty audit and disposition

The factorization through seed features and the linear ceiling for feature-only separation are not new claims in this project. C-76 already factors the closure through the seed vector and bounds low-side seed certificates; C-221 proves the low/high pair-separation condition and the universal `2N` signed-literal ceiling; C-260 gives the certificate/blocker duality for the same monotone readout. This note is retained as an independent re-derivation and a convenient consolidated reference, not as a new theorem or frontier advance. Q182 should be closed as redundant. The root-broadcast fact in C-322 is separate from this audit.

## 1. Factor the exact game through its seed profile

Fix a q-pair list Q. Let

```text
phi_Q(w) = (A_1(w), B_1(w), ..., A_q(w), B_q(w)) in {0,1}^{2q}
```

be the seed profile of table w. Regard the predecessor sets as fixed and feed an arbitrary vector v in `{0,1}^{2q}` into the C-319 recurrence. Its output defines a Boolean function `G_Q(v)`, with the least fixed point taken from all-zero state bits. Then

```text
Accept_Q(w) = G_Q(phi_Q(w)).
```

The function `G_Q` is monotone: if `v <= v'`, induction on the fixed-point rounds gives `x_i^t(v) <= x_i^t(v')` for every state and round, and hence the same inequality for the output.

## 2. Pair-separation consequence

If Q is a valid Gap-MCSP separator, then for every low table `f in SIZE(s1)` and every high table `z notin SIZE(s2)`,

```text
phi_Q(f) not<= phi_Q(z).
```

Otherwise monotonicity gives `1=Accept_Q(f)=G_Q(phi_Q(f)) <= G_Q(phi_Q(z))=Accept_Q(z)=0`, a contradiction. Therefore at least one of the 2q seed clauses must be true on f and false on z.

This is a necessary condition on the first-layer features, independent of how the states are connected.

## 3. Why feature separation alone stops at the linear floor

The 2N unit tests

```text
L_(j,b)(w) = [w_j = b],   j in [N], b in {0,1},
```

separate every pair of distinct truth tables: choose a differing coordinate and the polarity matching f. Hence the minimum number of signed-literal disjunctions needed merely to separate every low/high pair is at most 2N. Since Q supplies 2q seed clauses, a lower bound that uses only this pair-separation requirement can never force more than `q >= N`.

Likewise, counting seed profiles or observing that the first layer distinguishes tables cannot by itself prove a superlinear state bound: with 2N singleton features, the profile already records the complete truth table. Any remaining lower-bound force must come from the restricted way the transition graph combines the profile bits, together with the endpoint-incidence constraints tying seed clauses to predecessor relations.

This does not say that 2N features yield a valid native cover. It only retires first-layer distinguishability, profile count, and profile injectivity as standalone sources of a bound above N.

## 4. Small certificates of the transition readout

For an arbitrary seed profile v, the transition readout has a positive certificate of size at most 2q and a negative certificate of size at most q, measured in seed coordinates.

- If the output is 1, take a least-fixed-point proof from an active empty-consequence root. For each reached state and each of its two obligations, select either a true seed coordinate or a predecessor activated at an earlier round. At most two seed coordinates are selected per state. Fixing those coordinates to 1 preserves the proof by induction on activation round.
- If the output is 0, let I be the inactive states at the least fixed point. Every empty-consequence state lies in I. For each i in I, at least one endpoint factor is false; choose one such side. Its seed coordinate is 0 and all predecessors on that side remain in I. Fixing these at most q seed coordinates to 0 keeps I closed against activation, so the output stays 0.

These certificate bounds describe the readout but do not improve q: their widths scale with q, and the feature map still has 2q coordinates. They also show why replacing the state graph by an unrestricted monotone readout would lose the very structural information needed for a superlinear result.

## 5. Updated frontier

The candidate target is now more specific than “activation-profile complexity”: prove a lower bound on the *transition readout* `G_Q` under the realizable feature maps `phi_Q`, using the fact that both come from the same endpoint pairs and compatible-support product. A theorem that sees only the seed feature family has an absolute `2N` test ceiling. A theorem that treats `G_Q` as an arbitrary monotone function is too permissive. The missing invariant must charge their joint realizability inside the exact least-fixed-point graph.

Mandatory tests remain C-257 parity, C-258 repeated equality, C-307 LDPC/local constraints, C-317 safe cylinders, and C-281 owner masks. C-320 constrains some cross-splice masks but does not force the graph to generate a forbidden one. Actual `rho_GapMCSP` remains `N-o(N)`; no near-linear full-promise cover or P-vs-NP result follows.
