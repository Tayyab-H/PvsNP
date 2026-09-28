# C-290 - Audit of the Rao-clique LowExt transfer comparison

Date: 28 September 2026  
Classification: **PROOF AUDIT / ROUTE REOPENED, NOT A BREAKTHROUGH.**  
Scope: correct C-287's parameter and transfer comparisons and state the exact remaining window.

## 1. Make the promise disjoint, then retain the canonical-table obstruction

Rao's clique promise has YES graphs containing a `k`-clique and NO graphs containing no `ell`-clique, with `k>ell`. The initial C-287 choice `k=ceil(2*eta_0*ell)` did not ensure `k>ell` when the theorem constant `eta_0` is small. This is repaired in C-287 to `k=2*ell`, `ell=ceil(D*(ln m)^2)`, and `m=N^2`. For sufficiently large `N`, this satisfies `ell<k`, `ln m < eta_0*ell < k`, and `k*ell=2*ell^2 <= eta_0*m`. The YES/NO promise is now disjoint.

The directional Rao approximation and canonical-table proof in C-287 remain valid with this repaired choice. In particular, set

```text
L0 = (m/(k*ell))^(t/3),
A_map = L0/4,
t = eta_1^2*(ell-1)/ln m.
```

Then `ln L0=(eta_1^2/3+o(1))*ell`; the clique amplification threshold remains `theta_C=Theta(log^3(N)/N^2)`, and the patching radius is at most one for sufficiently large `N`. Therefore no valid C-125 map has AND cost `a<=A_map`. This obstruction is retained, now with a valid promise parameterization.

## 2. The transfer comparison in C-287 pointed the wrong way

C-287 then used cyclic unrolling to obtain

```text
CycAnd(f) >= sqrt(L0/C),
```

for an absolute constant `C`. This is a **lower** bound on cyclic complexity. The route-kill conclusion needed an upper bound `CycAnd(f)<=A_map`. Since `sqrt(L0/C)<A_map`, the displayed inequality does not establish that upper bound. Thus the implication in the old C-287 Section 5 was invalid.

The sound conclusions are:

1. every valid C-125 map for this source has `a>A_map`;
2. composition gives `rho_GapMCSP >= CycAnd(f)-a`;
3. a positive transfer remains possible if `CycAnd(f)>a>A_map` and a map in that interval is constructed.

The clique/C-125 route is reopened. Its bottleneck is the actual position of `CycAnd(f)` relative to `A_map`, plus construction of a sufficiently cheap map.

## 3. A monotone color-coding upper bound leaves the interval unresolved

A monotone upper bound for the promise distinguisher is obtained by detecting an exact `k`-clique. Choose a family `H` of maps `h:[m]->[k]` such that every `k`-set is injectively colored by at least one map. Such a family exists with

```text
|H| <= e^k * O(k*ln m):
```

for a fixed `k`-set, a uniformly random map is injective with probability `k!/k^k >= e^(-k)`; choosing that many independent maps and applying a union bound over at most `m^k` sets proves existence.

For a fixed `h`, compute colorful clique existence by the monotone dynamic program

```text
D[S,v] = OR over u with h(u) in S minus {h(v)} of (D[S minus {h(v)},u] AND x_uv),
```

with singleton-color base cases. It uses `O(2^k*m^2)` AND gates. The OR over all colorings therefore gives

```text
CycAnd(f) <= exp(O(k))*poly(m).
```

More explicitly, `ln U <= (1+ln 2)k + 2 ln m + O(ln k + ln ln m)`. Since `k=2*ell`, this is `(2+2 ln 2)*ell+o(ell)`. The map-cost floor has logarithm `(eta_1^2/3+o(1))*ell`; Rao's `eta_1` is a sufficiently small constant, so this color-coding bound is above `A_map` and does not close the interval. This is only a limitation of the available estimate; it does not prove that the true `CycAnd(f)` exceeds `A_map`.

## 4. Current bracket and discriminating next steps

The proved bracket is

```text
sqrt(L0/C) <= CycAnd(f) <= exp(O(k))*poly(m),
a > L0/4 for every valid C-125 map.
```

The lower bound is below the encoder floor; the color-coding upper bound is above it. Nothing here determines whether `CycAnd(f)>A_map`, and no useful LowExt map has been built. No positive Gap-MCSP lower-bound transfer follows yet.

The next clique-specific work is limited to resolving this exact interval: either give a quantified cyclic upper bound at most `A_map` (which would retire this transfer), or construct a C-125 map with `A_map<a<CycAnd(f)` and quantify the difference. A source lower bound alone, or reversing the unrolling inequality, cannot settle the comparison.

Rao's primary source states the monotone clique gap theorem and its admissible parameter conditions in Theorem 8 and proves it in Section 4: [*Monotone Circuit Lower Bounds from Spread Matchings*, ECCC TR26-129 rev. 5](https://eccc.weizmann.ac.il/report/2026/129/revision/5/download). The actual Gap-MCSP bound remains `q=N-o(N)`; this audit is not a P-vs-NP result.