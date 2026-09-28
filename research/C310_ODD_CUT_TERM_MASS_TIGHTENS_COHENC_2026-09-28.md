# C-310 - Odd-cut mass of one matching term removes the smallness barrier

Date: 28 September 2026  
Classification: **PROVED PARAMETER SHARPENING / ODDFACTOR ENCODER LOWER BOUND.** A direct odd-cut term-mass lemma lets the C-308 argument use a constant-fraction sunflower parameter `r=Theta(v)`, so `r=o(v)` and the final DNF agreement theorem are unnecessary. Every ODDFACTOR C-125 map has `a+N-1 > exp(Omega(v^(1/3)/log^(2/3)v))`. This is a reconstruction lower bound, not an OPS fusion lower bound or P-vs-NP proof.

## 1. Exact mass of a short matching term on odd cuts

Let `M` be a matching of `ell<v` edges in `K_(v,v)`. Under `D0`, choose a uniformly random vertex coloring of odd total parity and include each bipartite edge whose endpoints have equal colors. The event `t_M=1` imposes one equality on each of `ell` disjoint vertex pairs. There are `2^(2v-ell)` colorings satisfying those equalities. The `2v-2ell` unpaired vertices are nonempty, so exactly half of those assignments make the total coloring odd. Since there are `2^(2v-1)` odd colorings in total,

```text
Pr_D0[t_M=1] = 2^(-ell).
```

Therefore any matching-DNF of width at most `w<v` that contains at least one term has D0 acceptance probability at least `2^(-w)`. An empty term only increases this probability to one.

This is stronger for the present purpose than the general DNF agreement cap: if a one-sided separator is zero on D0 and its approximating matching-DNF has D0 false-positive probability below `2^(-w)`, then that DNF must be identically zero.

## 2. Paid-AND approximation at constant `r/v`

Use C-308's shared-DAG approximation with sunflower error `eps_sun=v^(-10w)`. At one binary AND node, there are at most `v^(6w)` distinct matching terms of width at most `2w`; plucking therefore creates D0 false positives with probability at most `v^(-4w)`. The matching sunflower lemma gives

```text
r <= C0*w^3*log^2(v),
q := e*r/v,
```

for a universal constant `C0`. After deleting terms wider than `w`, the D1 false-negative probability per paid AND node is at most `q^(w+1)/(1-q)`, provided `q<1`. Thus an acyclic circuit with `A` paid AND nodes has simultaneous directional errors

```text
delta0 <= A*v^(-4w),
delta1 <= A*q^(w+1)/(1-q).
```

Only `q<1` is needed here. In contrast with C-308's use of the `o(v)`-small DNF agreement theorem, the term-mass argument permits `r` to be a sufficiently small constant fraction of `v`.

## 3. Apply the term-mass bound to a C-125 map

Choose a sufficiently small universal constant `c>0` and set

```text
w = floor(c*v^(1/3)/(log v)^(2/3)).
```

Then `q<=1/16` for all sufficiently large `v`. Suppose a valid C-125 ODDFACTOR map `Phi` has `a` AND gates and `a+N-1<=16^w`. Its approximation has

```text
delta0(Phi) <= (16/v^4)^w < 2^(-2w),
delta1(Phi) <= 16^w*(1/16)^(w+1)/(1-1/16) = 1/15.
```

If both polarity rails at one truth-table coordinate have matching terms, their union contains at most `2w` edges and has an isolated vertex. At least `2^(-2w)` of odd-cut colorings make both terms true. Outside the simultaneous D0 error set, both approximating rails lie below the exact rails, contradicting C-125's one-hot high completion. Hence every coordinate has at most one rail polarity in the approximant.

On any perfect matching outside the `1/15` D1 exception, a complete low table survives in the approximant. Thus every coordinate has one fixed available polarity, giving a common table `b in SIZE(s1)`. The exact conjunction

```text
Q(G) = AND_j Phi_(j,b_j)(G)
```

rejects every odd-cut NO input and accepts at least `14/15` of D1. It uses `a+N-1` paid AND gates.

Now approximate `Q` with the same parameters. Since its AND count is at most `16^w`, the D0 false-positive mass is at most `(16/v^4)^w<2^(-w)`, and its D1 false-negative mass is at most `1/15`. The approximant is a matching-DNF of width at most `w`. Because `Q=0` on D0, the approximant accepts D0 with probability below `2^(-w)`. By the exact term-mass lemma in Section 1, it has no term and is identically zero. But it must accept at least `14/15-1/15=13/15` of D1. Contradiction.

Therefore

```text
a + N - 1 > 16^w
  = exp(Omega(v^(1/3)/(log v)^(2/3))).
```

This bound applies to arbitrary NO-active C-125 rails. It removes both the `r=o(v)` restriction and C-308's `gamma>0` slack in the exponent parameter.

## 4. Comparison and limits

Cavalar et al.'s matching-sunflower lemma supplies the approximation step; their paper states its main lower bound in total circuit size and also records the optimization in terms of the sunflower parameter. C-310's additional step is the explicit D0 mass calculation for a single short matching term, used to exclude every term rather than invoke the DNF agreement cap. [Primary paper](https://eccc.weizmann.ac.il/report/2025/102/revision/1/download)

At `v=(log N)^K` for fixed `K>3`, `w/log N -> infinity`, so the map lower bound is superpolynomial in `N`. However, it still does not construct an encoder below exact `CycAnd(ODDFACTOR)`, prove a positive transfer margin, or change the actual `rho_GapMCSP=N-o(N)` bound. The live task remains to find an all-input C-125 map with a strict decision/reconstruction gap, or move to a source whose one-sided distributional separator is provably cheaper than exact monotone decision.

