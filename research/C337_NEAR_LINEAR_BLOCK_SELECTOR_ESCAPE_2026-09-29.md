# C-337 - A near-linear block selector blocks the C-336 product inference

Date: 29 September 2026  
Route: O-167/O-168; test whether the C-336 independent-menu obstruction by itself forces extra states.  
Classification: **EXACT RESTRICTED-FAMILY COVER / NO FULL-PROMISE RESULT.**

## 1. Parameters and local anchors

Let N=2^n, s2=N^beta, and s1=s2/(c0*n), for fixed 0<beta<1. Take k=K*n disjoint address subcubes S_1,...,S_k, each of dimension u, with

```text
M = |S_b| = 2^u = lambda*s1*log(s1),   u=(beta+o(1))*n.
```

Here K is a sufficiently large fixed constant and lambda>0 is a fixed small constant. Lupanov synthesis gives an arbitrary u-input pattern circuit of size O(2^u/u)=O(lambda*s1), since u is asymptotic to log(s1), which is asymptotic to beta*n. To support it on a particular address subcube also requires an equality test on the fixed address bits. This costs O(n) gates, not merely O(log k) in general. Since s1 grows faster than n, each one-block table is still in SIZE(s1) after choosing lambda small. This corrects the omitted fixed-suffix selector cost in the C-336 parameter description without changing its conclusion.

The total number of coordinates in these subcubes is

```text
k*M = Theta(K*lambda*s2*log N) = o(N).
```

By circuit counting, the all-block product contains a high table when K*lambda is chosen large enough: (2^M-1)^k > |SIZE(s2)|. Every nonzero pattern choice in one designated block remains a low anchor in SIZE(s1).

## 2. A global at-most-r selector

Fix r=R*n<k, with R>0 a sufficiently small fixed constant. Let Y_r be the set of tables that are zero outside P=union_b S_b and are nonzero on at most r of the subcubes. Every table in Y_r is in SIZE(s2): synthesize each active block separately, test its fixed address subcube, and OR the r outputs. The circuit size is

```text
O(r*lambda*s1 + r*n) = O((R*lambda/c0)*s2) + O(n^2).
```

Choose constants with margin so this is at most s2 for all sufficiently large N. Thus no high table is in Y_r.

There is a signed-literal monotone circuit recognizing exactly Y_r. Let zero(z_j) denote the signed rail asserting that table bit z_j is zero. Compute

```text
C_out = AND_{j outside P} zero(z_j)
Z_b   = AND_{j in S_b} zero(z_j).
```

The condition "at most r blocks are nonzero" is "at least k-r of the Z_b values are 1." A fixed Batcher sorting network on the k bits Z_b computes this threshold using O(k*log^2(k)) comparators, hence O(k*log^2(k)) paid AND gates (OR gates are free in A_cap). Conjoin its threshold output with C_out.

The outside-zero check uses N-k*M-1 AND gates and the k block-zero checks use k*(M-1). Together these are N-k-1; the final conjunction and sorting network add O(k*log^2(k)). Therefore

```text
A_cap(Y_r, Z_high) <= N + O(k*log^2(k))
                    = N + O(log(N)*log^2(log(N))),
```

where Z_high is the set of tables with circuit complexity greater than s2. Every signed-literal half-cube meets Z_high, since SIZE(s2) has size 2^o(N), which is less than 2^(N-1). By the C-307 compiler, this gives a valid native cover for Y_r versus Z_high with

```text
q <= N + O(log(N)*log^2(log(N))).
```

The C-307 transfer is essential: the displayed object is not merely a heuristic block test; its AND budget yields a native pair list under the exact cover semantics.

## 3. What this does and does not refute

The selector accepts every one-block low anchor and every combination using at most R*log(N) active blocks. It rejects every tuple with all K*log(N) blocks active, including the large independent product used in C-336. So the C-336 product constraint alone cannot force a superlinear q-charge: a sound system can expose each individual menu while using a single global activity selector to suppress their full product at linear cost.

This is **not** a full-promise cover. It rejects low tables whose support is outside P, including many parity-like tables, and it rejects repeated nonzero block patterns when they occupy more than r blocks. In particular, it does not pass C-257 parity or C-258 repeated-equality as a separator for those promises. It only passes the C-307 compiler check and demonstrates one legal product-avoidance mechanism.

The result therefore gives neither q>=N*g(N) nor an N^(1+o(1)) cover of all SIZE(s1) versus all Z_high. It also does not prove that an arbitrary q-state game for the full promise can be reduced to this selector architecture. The remaining theorem must show that covering every low circuit makes all possible global selectors more expensive than this restricted block test, or construct a selector broad enough to accept parity, repeated descriptions, and all other low circuits within near-linear q.

## 3.1. A stronger selector still misses a tiny shared relation

A natural extension accepts tables whose k block rows use at most d distinct patterns, rather than only at most r nonzero rows. This includes repeated block patterns. It also has a near-linear signed monotone implementation: compute all pairwise row-equality flags using O(k^2*M) AND gates. For each d-element set R of row indices, form the condition that every row equals some representative in R, and OR over all R. The additional AND cost is O(k*binom(k,d)); OR fan-in is free in A_cap. Thus

```text
A_cap <= N + O(k^2*M + k*binom(k,d)).
```

Take k=K*n and d=R*n with 0<R<K. The entropy bound gives binom(k,d) <= N^(eta+o(1)), where eta=K*H_2(R/K). Choose R small enough that eta<1. Since M=Theta(s2), k^2*M=N^beta*polylog(N)=o(N), so this selector also has N+o(N) AND gates. Its accepted tables lie in SIZE(s2): d arbitrary u-bit patterns cost O(d*lambda*s1), and the block-to-prototype assignment costs only O(k*log(k)+n). C-307 again gives a restricted native cover. This family includes the repeated-equality pattern on these selected blocks while rejecting a typical independent tuple, which has k distinct rows.

Even the prototype selector misses a very small shared relation. Choose k=2^ell and make row b equal to the minterm [the first ell suffix bits equal b]. The k rows are all distinct, but the entire table on the selected subcubes is generated by one circuit of size O(n): test the common fixed suffix and compare the block prefix with the first ell free suffix bits. Because d<k, the prototype selector rejects this low table. Thus block activity and prototype count both fail to capture the relevant notion of coherence. A viable selector must recognize profiles generated by a small shared circuit relation, not just sparse activity or repeated rows; that is the original synchronization problem in a more concrete form.

## 4. Checkpoint

1. Actual Gap-MCSP fusion lower bound beyond N-o(N): **no**.
2. Near-linear full-promise cover: **no**; only the restricted family Y_r has one.
3. State-sensitive synchronization theorem for all low tables: **no**.
4. Positive CohEnc transfer / reconstruction compiler: **no**.

Disposition: keep C-336 as a valid multi-hole splice theorem, but retire "forbidden independent product implies q growth" unless it includes a proof that the all-low coverage condition rules out global selectors of the kind above.
