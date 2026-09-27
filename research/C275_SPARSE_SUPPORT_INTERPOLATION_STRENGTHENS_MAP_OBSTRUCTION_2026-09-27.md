# C-275 - Shared block decoders raise the necessary conflict support to order s2

Date: 27 September 2026  
Classification: **GLOBAL-STRUCTURAL (strengthening of C-274).**  
Route: A, exact LowExt transfer.

## Sparse-support interpolation lemma

For every `A subseteq {0,1}^n` of size `k>=2`, its indicator `1_A` has an ordinary fan-in-two Boolean circuit of size

```text
O(k n / log k).
```

Proof: let `t=floor(log2 k)` and partition the n input bits into `r=ceil(n/t)` blocks of at most t bits. For each block, generate all `2^t<=k` pattern indicators by recursively splitting each partial minterm on the next bit; this costs `O(k)` gates per block. For each `a in A`, AND the r block indicators matching its address, costing `O(r)` gates per point. OR the k resulting exact-address indicators. The total is `O(rk)=O(k n/log k)`. For `k=0,1`, a constant or one equality minterm suffices. All NOT gates for bit complements can be shared.

Consequently, if two truth tables `w,z` differ on a set of at most k coordinates, then

```text
CC(z) <= CC(w) + O(k n/log k + n),
```

by computing the indicator of their difference set and XORing it with w. This improves the separate-minterm patch bound `O(kn)` used in C-274.

## Strengthened C-125 obstruction

Let `phi` be a monotone map for an upward-closed source promise, with AND cost a, satisfying the C-125 low-YES/high-NO one-hot conditions. As in C-274, let S be the union of coordinates conflicted on some YES image, and `delta=|S|`. Join any two YES inputs: every pair of chosen low witnesses agrees outside S. Fix one witness `w0`; all YES images contain its rails outside S.

If a NO input's high completion z extends all those common rails, it agrees with w0 outside S and differs only on at most delta positions. Therefore, whenever

```text
s1 + O(delta n/log delta + n) <= s2,
```

that completion is actually in `SIZE(s2)`, a contradiction. For fixed `0<beta<1`, `s2=N^beta`, and `s1=N^beta/(c0 log N)`, we have `log delta=Theta(log N)` when `delta` is a constant fraction of s2. Choosing a sufficiently small constant `c_beta>0` shows:

```text
delta <= c_beta s2  =>  CycAnd(f) <= a + N - delta - 1.
```

The circuit is the AND of the fixed `w0` rails outside S, exactly as in C-274. Hence any transfer whose map saves more than N AND gates against the source lower bound must have

```text
delta = Omega_beta(s2) = Omega_beta(N^beta),
```

not merely `Omega(s2/log N)`. More generally the forbidden patchable threshold is the largest k for which `s1+O(k n/log k)<=s2`.

## Implication and limits

For Rao's matching lower bound with `v=A(log N)^2`, choosing A so `CycAnd(MATCH_v)>N^{1+epsilon}` means any map with `a<CycAnd(MATCH_v)-N` must globally conflict on Omega(N^beta) truth-table coordinates. This is on the order of `log |SIZE(s1)|` for the project parameters. It is a stronger design constraint on the reduction than C-127 and C-274.

The argument still measures the **union** of conflict positions across all YES inputs. That union may be Omega(N^beta) even if each individual YES input activates very few conflicts. A broad union is not ruled out, and no lower bound on q follows unless one also charges map gates or proves that the conflicts must be activated in a source-detectable way. Next test whether source inputs can distribute conflicts over many witness codes at sub-source AND cost.

No LowExt map, q improvement, or P-vs-NP proof is obtained. The actual fusion lower bound remains `q=N-o(N)`.
