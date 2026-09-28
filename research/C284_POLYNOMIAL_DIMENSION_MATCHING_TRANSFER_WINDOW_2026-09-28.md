# C-284 — Polynomial-dimension matching source window for C-125

Date: 28 September 2026  
Classification: **CONDITIONAL-TRANSFER.**  
Scope: exact parameter geometry only; no source map is constructed.

## The source and target parameters

Use Rao's monotone gap-matching source on bipartite graphs with side size `v`. There are `M=Theta(v^2)` edge inputs, and the source cyclic AND lower bound from C-266 is

```text
L(v) >= exp(c sqrt(v))
```

for a constant `c>0`. The C-125 composition gives `q>=L(v)-a(N)` for a monotone rail map of AND cost `a(N)`.

For a prescribed exponent `epsilon>0`, the exact sufficient comparison is

```text
exp(c sqrt(v)) - a(N) > N^(1+epsilon).
```

If `a(N)<=N^eta`, it suffices that `c sqrt(v)>max(1+epsilon,eta) ln N` with a fixed margin, as in C-267. In particular, any polynomial source dimension `v=N^delta`, for fixed `delta>0`, makes `L(v)=exp(Omega(N^(delta/2)))`, which dominates every fixed polynomial in N.

## YES completion cost

Encode a perfect matching as the truth-table indicator of its `Theta(v)` edge addresses among the `M=Theta(v^2)` edge positions, with all other table coordinates fixed to zero. By the sparse-support interpolation lemma (C-275), this completion has circuit size

```text
O(v log N / log v).
```

For `v=N^delta`, this is `O(v/delta)`. It fits `s1=N^beta/(c0 log N)` whenever `delta<beta`, with any fixed margin. The table can be padded to the full `N` coordinates without changing the asymptotic cost.

## High palette count

For a proposed witness-profile map, one can simultaneously choose `r=N^delta` disjoint balanced address classes `S_1,...,S_r`, each of size `Theta(N/r)`, whose indicator tables all lie outside `SIZE(s2)`, provided

```text
delta < 1-beta.
```

Indeed, a uniformly chosen balanced class has

```text
log2 binom(N, N/r) = Theta((N/r) log r)
                       = Theta(N^(1-delta) log N)
```

possible values, while

```text
log2 |SIZE(s2)| = O(s2 log(s2+log N)) = O(N^beta log N).
```

The former exponent dominates the latter exactly when `1-delta>beta`; a union bound over `r=N^delta` classes is negligible. Thus for every fixed `0<beta<1`, any

```text
0 < delta < min(beta,1-beta)
```

simultaneously gives: (i) low matching-witness tables of size at most `s1`; (ii) a superpolynomial cyclic source lower bound; and (iii) a polynomial-size palette of distinct high completion codes.

## What this removes, and what remains

This removes the need to keep the hard source dimension polylogarithmic merely to fit YES witnesses or manufacture many high codes. If a C-125 map on this family had `a(N)=N^{O(1)}`, its transfer would yield `q>N^{1+epsilon}` for every fixed `epsilon` eventually. The outstanding requirements are unchanged and are the actual obstacle:

1. every YES graph must activate a full one-hot code of a small matching-incidence table;
2. every NO image must remain below some high completion;
3. the rail map must have AND cost below `L(v)-N^{1+epsilon}`;
4. the map outputs must not expose a short decoder for the source.

C-279's scalar-rank palette still fails item 4: its adjacent-rank decoder makes `L-a=O(r)`, even if `r` is scaled polynomially. The bottom-hole correction C-283 adds another necessary condition: any useful bottom-NO map with a compatible low witness must leave `Omega_beta(s2)` table positions unpinned. No construction meeting the four requirements is known. The actual fusion bound remains `q=N-o(N)`.

## Conclusion

The hard-source dimension can be polynomial in N across the full fixed-beta range. The remaining issue is structural map validity and AND-cost, not parameter slack. This is a conditional parameter upgrade, not a q lower bound or a P-vs-NP result.

Primary source for the matching lower bound: Rao, [*Monotone Circuit Lower Bounds from Spread Matchings*, ECCC TR26-129 rev. 5](https://eccc.weizmann.ac.il/report/2026/129/revision/5/download). The cyclic conversion and C-125 arithmetic are detailed in `research/C266_CYCLIC_MATCHING_LOWEXT_AND_SYNCHRONIZATION_AUDIT_2026-09-27.md`.
