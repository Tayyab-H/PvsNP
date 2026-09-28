# C-301 - Short-term overlap forces one global polarity in every ODDFACTOR C-125 map

Date: 28 September 2026  
Classification: **PROVED QUANTITATIVE MAP LOWER BOUND / ROUTE FILTER.** This applies to every monotone C-125 map for bipartite ODDFACTOR, with arbitrary NO-active rails and shared gates. It rules out polynomial-cost maps at the selected polylogarithmic source scale. It does not provide a positive Gap-MCSP transfer.

## 1. Setup and the correct approximation theorem

Let `Phi` be a monotone multi-output map on the edges of `K_(v,v)`, with `2N` signed truth-table rails, satisfying the C-125 conditions:

```text
Odd(G)=1 => some w in SIZE(s1) has e(w) <= Phi(G),
Odd(G)=0 => some z outside SIZE(s2) has Phi(G) <= e(z).
```

Here `e(w)` is the complete one-hot rail encoding. Let `a` be the number of distinct binary AND gates in the shared acyclic DAG. Flatten every free-OR region over the `v^2` input edges and the `a` AND outputs. With all rail roots retained, this gives a fan-in-two monotone circuit of size

```text
S_phi = O((a+N+1)(v^2+a+N)).
```

Use Cavalar et al.'s distribution `D=(D0+D1)/2`, where `D1` is uniform over perfect matchings of `K_(v,v)` and `D0` is the odd-cut distribution. Every `D1` input is an ODDFACTOR YES instance; every `D0` input is an ODDFACTOR NO instance.

The matching-sunflower approximation is gatewise, so one approximant is assigned per node of the shared DAG and each of the `2N` output roots reads its already-defined node. There is no output-count multiplier. Cavalar et al. state the approximation as part of a proof for circuits computing Match, but the gate transformation and its error analysis use only the circuit topology and the distribution; they do not use what function the output computes. Thus the same construction applies to our arbitrary monotone rail circuit. For a width parameter `w` with `S_phi <= 2^w`, it gives matching-DNF rails, each term containing at most `w` edges. Its directional error events are:

```text
E1 = {some rail has Phi=1 and Phi_tilde=0 on D1},
E0 = {some rail has Phi=0 and Phi_tilde=1 on D0}.
```

Writing `r <= C0 w^3 log^2(v)` for the DNF smallness bound and `q=e r/v`, the gatewise proof gives

```text
Pr_D0[E0] <= 2^w v^(-w),
Pr_D1[E1] <= 2^w * q^w/(1-q),       when q<1.
```

For the first inequality, a gate's plucking error is at most `v^(-w)` on `D0`. For the second, deleting terms wider than `w` costs at most
`sum_(ell=w)^(2w) r^ell (e/v)^ell <= q^w/(1-q)` per gate: there are at most `r^ell` terms of size `ell`, and each is contained in a uniform perfect matching with probability at most `(e/v)^ell`. Summing local error events over the shared DAG charges at most `S_phi <= 2^w` gates, not `2N` separate circuits.

## 2. Opposite short terms force compatible NO mass

Fix a coordinate `j`. Suppose `Phi_tilde_(j,0)` contains a matching term `A` and `Phi_tilde_(j,1)` contains a matching term `B`, each with at most `w` edges. Let `J=A union B`, viewed on all `2v` bipartite vertices. It has at most `2w` edges. For `w<v/4`, at most `4w< v` vertices are incident to an edge, so `J` has an isolated vertex; in particular, it has a component of odd cardinality.

An odd-cut coloring makes both terms true exactly when it is constant on every component of `J`. There are `c` components, so `2^(c-1)` such colorings have odd total parity: the isolated odd component makes parity nonconstant as a function of its component color. Since `D0` samples uniformly from the `2^(2v-1)` odd colorings, the compatible probability is

```text
2^(c-1)/2^(2v-1) = 2^(c-2v) >= 2^(-2w),
```

where `c >= 2v-|E(J)| >= 2v-2w`. Every compatible coloring's odd-cut graph contains all edges of `J`, so both approximant rails fire. On the good `D0` event, `Phi_tilde<=Phi`; the exact map would then have both opposite rails true. That contradicts `Phi(G)<=e(z)` for a complete one-hot high code. Therefore

```text
Pr_D0[E0] >= 2^(-2w)
```

whenever both rail polarities have terms. Thus the explicit error inequality `Pr_D0[E0] < 2^(-2w)` rules out opposite-polarity terms at every coordinate. This uses only C-125 NO one-hot consistency, not a lift factorization or NO-vanishing sidecar.

## 3. Choose a width where every estimate is quantitative

Set

```text
w = floor(v^(1/3)/log(v)).
```

For all sufficiently large `v`, `w` grows, `w<v/4`, and
`r <= C0 w^3 log^2(v) = O(v/log(v)) = o(v)`. Hence `q=e r/v=O(1/log(v))`, so eventually `q<=1/16`. For any circuit of size at most `2^w`, the simultaneous directional errors satisfy

```text
delta0 := Pr_D0[E0] <= (2/v)^w,
delta1 := Pr_D1[E1] <= (2q)^w/(1-q).
```

In particular,

```text
delta0 / 2^(-2w) <= (8/v)^w = o(1),
delta1 / 2^(-2w) <= (8q)^w/(1-q) = o(1).
```

So `delta0 < 2^(-2w)` for all sufficiently large `v`, and no coordinate has approximant terms of both polarities. The same estimates give `delta1=o(1)`.

## 4. One low table is forced on almost every matching

At each coordinate at most one rail approximant has any term. At least one does: choose any perfect matching outside `E1`; its C-125 low witness `u` has every rail of `e(u)` true in `Phi`, hence also in `Phi_tilde` on the good directional event `Phi<=Phi_tilde`. Therefore each coordinate has exactly one available polarity; call the resulting table `b`.

For every perfect matching outside `E1`, any C-125 low witness `u` must use the only available polarity at every coordinate, so `u=b`. Thus `b in SIZE(s1)`, and the original map has every `b`-rail true on at least a `1-delta1` fraction of perfect matchings.

Define the monotone source circuit

```text
Q(G) = AND over j in [N] of Phi_(j,b_j)(G).
```

It accepts at least `1-delta1` of `D1`. On every `D0` input, C-125 gives `Phi<=e(z)` for a high table `z`; since `b` is low, `b!=z`, so at a differing coordinate the selected `b`-rail is zero. Hence `Q=0` on all of `D0`. Its agreement with ODDFACTOR on `D` is at least `1-delta1/2=1-o(1)`.

## 5. Quantitative contradiction and encoder lower bound

The circuit `Q` has size at most

```text
T = O((a+N+1)(v^2+a+N)) = O(X^2),
X := a+N+v^2+1.
```

Suppose `T<=2^w` for the explicit width in Section 3. Apply Cavalar et al.'s approximation theorem to `Q` with this same `w`. It yields a matching-DNF with `r=O(v/log v)=o(v)` and directional error `o(1)`. Since `Q` agrees with ODDFACTOR on `D` with probability `1-o(1)`, that DNF also agrees with ODDFACTOR with probability `1-o(1)`. But Cavalar et al.'s DNF agreement lemma bounds agreement with matching on `D` by `1/2+o(1)`, and `Odd=Match` on the support of `D`. Contradiction. Therefore

```text
T > 2^floor(v^(1/3)/log(v)),
a + N + v^2 + 1 >= Omega(2^(v^(1/3)/(2 log(v)))).       (C301)
```

Constants hidden by `Omega` absorb the circuit-flattening constant and rounding. In particular, for `v=(log N)^K` with any fixed `K>3`,
`v^(1/3)/log(v) = (log N)^(K/3)/Theta(log log N) = omega(log N)`. Thus the lower bound on `a+N+v^2+1` is superpolynomial in `N`: no polynomial-cost C-125 ODDFACTOR map exists at this source scale, including maps whose rails remain active on NO inputs.

## 6. Scope and research consequence

The decisive mechanism is **compatible-NO mass of paired short terms**. A pair of opposite matching terms has common odd-cut NO mass at least `2^(-2w)`; the correct odd-cut approximation has a smaller global false-positive budget at the selected width. This converts local term overlap into global polarity, then into a source separator.

This is a strong lower bound on `CohEnc`, not a positive transfer. It does not establish `CohEnc << CycAnd`; no near-lossless transfer follows. The actual fusion bound remains `q=N-o(N)`. No `rho_GapMCSP>N^(1+epsilon)` result, `NP not subset P/poly`, or P-vs-NP proof follows. C-300's earlier Rao-distribution route-kill is withdrawn; C-301 uses Cavalar et al.'s matching/odd-cut distribution directly.

## References

- Cavalar, Goeos, Riazanov, Sofronova, and Sokolov, [Monotone Circuit Complexity of Matching, ECCC TR25-102 rev. 1](https://eccc.weizmann.ac.il/report/2025/102/revision/1/download), Lemma 3 (gatewise approximation), Lemma 4 (DNF agreement), and Section 3.3 (ODDFACTOR transfer).
- C-125 reconstruction measure and transfer definition: `research/C288_ODDFACTOR_COHENC_AND_NATIVE_RECONSTRUCTION_BOUNDARY_2026-09-28.md`.
