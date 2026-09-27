# C-279 — A valid rank-coded LowExt map collapses to a short source decoder

Date: 27 September 2026  
Classification: **CALIBRATION.** Scope: two-block rank-state maps.  
Route: A4, input-dependent NO images.

## Source with an exponential cyclic lower bound

Let `m` be even and let each bipartite graph have `m` vertices on each side. Put

```text
h = m/2 + 1,
F(G1,G2) = 1 iff nu(G1) + nu(G2) >= 2h = m+2.
```

On the diagonal `G1=G2=G`, this is exactly `nu(G)>=h`. Such a circuit distinguishes perfect matchings from graphs with no matching of size `m/2`; Rao's spread-matching theorem gives ordinary monotone size `exp(Omega(sqrt(m)))`, and the C-266 cyclic unrolling gives

```text
L(m) := CycAnd(F) >= exp(c sqrt(m))
```

for a constant `c>0`.

## High-code palette

Let `N=2^n`, `s2=N^beta` for fixed `0<beta<1`, and partition the table addresses into `m` nearly equal disjoint classes `S_1,...,S_m`. They can be chosen so that every indicator table

```text
z_t(i) = 1 iff i is in S_t
```

lies outside `SIZE(s2)`. Indeed, the number of size-`s2` circuits is `2^{O(s2 log(s2+n))}`, while a uniformly random balanced class has `binom(N, floor(N/m))` possibilities and

```text
log2 binom(N, floor(N/m)) = Theta((N/m) log m)
                         >> s2 log(s2+n)
```

because `m=Theta(log^2 N)` and `beta<1`. A union bound over the `m` classes proves simultaneous existence.

## Map definition and order check

Write `a=nu(G1)` and `b=nu(G2)`. For each `t in {1,...,m}`, define the monotone predicate

```text
R_t(G1,G2) = [a >= t] AND [b >= m+1-t].
```

For each address `i`, set the dual rails to

```text
phi_(i,1) = OR_{t : i in S_t} R_t,
phi_(i,0) = OR_{t : i not in S_t} R_t.
```

Every rail is monotone. If `a+b < m+1`, no `R_t` is active and `phi=0`. If `a+b=m+1`, exactly one is active, namely `R_a`, so `phi=e(z_a)`, a complete high code. If `a+b>=m+2`, the active indices form the interval

```text
[m+1-b, a],
```

which contains at least two consecutive indices `t,t+1`. Since `S_t` and `S_(t+1)` are disjoint, at every address at least one of `z_t(i),z_(t+1)(i)` is zero. The active palette codes therefore set the zero rail at every coordinate, so

```text
e(0^N) <= phi(G1,G2).
```

The all-zero table belongs to `SIZE(s1)`. Thus every YES input contains a low code. Every NO input either maps to zero, which lies below some high code, or maps to `e(z_a)` with `z_a` high. In particular, the NO images vary with the input and the map satisfies both C-125 order conditions. No assumption that the YES image itself is a legal table is used.

## Exact cost audit: the map exposes a short decoder

Choose any address `i_t in S_t`. Disjointness of the address classes gives

```text
phi_(i_t,1) = R_t.
```

So every rank predicate `R_t` is directly readable from one output rail. The source is exactly

```text
F = OR_{t=1}^{m-1} (R_t AND R_(t+1)).
```

If `a_map` is the map's AND cost, composing this `m-1`-gate decoder with the map yields a monotone circuit for `F` with at most `a_map + m-1` AND gates. Hence

```text
a_map >= CycAnd(F) - (m-1),
CycAnd(F) - a_map <= m-1 = O(log^2 N).
```

The source lower bound is almost entirely spent in the map. This construction cannot produce a superlinear native-fusion lower bound, even though it is a valid asymmetric LowExt map with input-dependent high NO codes. The decisive failure is low-dimensional state decoding: a yes instance is exactly where two neighboring rank states coexist.

## Route update

This demonstrates that the variable-NO interface required by C-278 is feasible; it does not prove that arbitrary variable-NO maps are expensive. Rank-only palettes fail because their source is decoded by `O(m)` pairwise state tests. A surviving Route A construction must encode many witness-specific NO states without exposing a small state-pair decoder, while keeping its map AND-cost below `L(m)-N^(1+epsilon)`. This also sharpens Route B's target: the relevant object is not the number of NO profiles but whether their compatibility pattern admits a compact global decoder.

The actual Gap-MCSP fusion lower bound remains `q=N-o(N)`. No P-vs-NP result follows.

**Source reference:** Anup Rao, [*Monotone Circuit Lower Bounds from Spread Matchings*, ECCC TR26-129 rev. 5](https://eccc.weizmann.ac.il/report/2026/129/revision/5/download), Theorem 1 and Corollary 2. The cyclic extension used above is the explicit unrolling recorded in C-266/C-276.
