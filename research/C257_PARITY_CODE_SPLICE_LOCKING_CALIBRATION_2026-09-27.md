# C-257 — A dense parity-code calibration for native splicing

Date: 27 September 2026  
Scope: test whether high-side density, maximal certificate width, many anchors, and state reuse alone force a high-complexity splice in the native C-74 closure. They do not. This is an exact artificial-model construction, not a result about Gap-MCSP.

## 1. Promise

Fix `N >= 3`, let the universe of high objects be the odd-parity strings

\[
U=\{z\in\{0,1\}^N:\ z_1\oplus\cdots\oplus z_N=1\},
\]

and let the low anchors be all even-parity strings. For an anchor `w`, the initial generators in the native closure are

\[
L_{w,k}=U\cap\{z:z_k=w_k\},\qquad k\in[N].
\]

The high side is very dense: every partial assignment fixing fewer than `N` coordinates has an odd-parity completion. In particular it realizes every assignment on any proper coordinate subset.

For `1<=i<N` and `b in {0,1}`, write

\[
P_{i,b}=\{z\in U:z_1\oplus\cdots\oplus z_i=b\}.
\]

## 2. A linear native fusion list

Use the following listed endpoint pairs `(E,H)`; all endpoints are subsets of `U`.

1. **Base (2 rules):** for each `b`, `(P_{1,b},U)`.
2. **Prefix transitions (4(N-2) rules):** for each `i=2,...,N-1` and `c,a in {0,1}`, `(P_{i-1,c}, U intersect {z:z_i=a})`.
3. **Empty outputs (2 rules):** for each `c`, `(P_{N-1,c}, U intersect {z:z_N=c})`.

The total is `2+4(N-2)+2=4N-4` pairs.

### Completeness on every even anchor

Fix even `w`. The base rule with `b=w_1` fires because `L_{w,1}=P_{1,b}` is an initial generator and is contained in both endpoints. Thus the closure contains a set `G_1 subseteq P_{1,w_1}`.

Inductively, suppose it contains `G_{i-1} subseteq P_{i-1,c}`, where `c=w_1 xor ... xor w_{i-1}`. The transition rule indexed by `(i,c,a=w_i)` has both endpoints in the upward-closed family: the first contains `G_{i-1}`, and the second is exactly the initial generator `L_{w,i}`. Its intersection is added, giving a generated set

\[
G_i=P_{i-1,c}\cap\{z\in U:z_i=w_i\}\subseteq P_{i,c\oplus w_i}.
\]

At `i=N-1`, this yields a generated subset of `P_{N-1,c}` for the parity `c` of the first `N-1` bits. Since `w` is even, `c=w_N`. The corresponding output rule has both endpoints in the closure: the first contains that generated subset and the second is `L_{w,N}`. Their intersection is

\[
U\cap\{z_1\oplus\cdots\oplus z_N=0\}=\varnothing.
\]

So every even anchor derives the empty set.

### Soundness on every odd high object

Fix `z in U` as anchor. Every initial generator `L_{z,k}` contains `z`. Upward closure preserves this property, and the intersection of two sets containing `z` still contains `z`. Hence every set generated at every stage contains `z`, so the closure never derives the empty set. This argument is independent of the particular listed pairs.

Thus the list is a valid native cover of the even/odd promise with `q=4N-4`.

## 3. Exact certificate and splice consequences

By the finite-proof characterization of the C-67 recurrence (C-227), any consistent output-proof support `C` is sound only if no odd string extends it. If `C` leaves even one coordinate free, that coordinate can be set to make the total parity odd. Therefore every consistent output certificate fixes all `N` coordinates. For a proof accepted on an even anchor `w`, its support is exactly the full assignment `ell(w)`.

Every consistent context/subproof splice is again an output proof. Its support must therefore fix all `N` coordinates and name a unique completion. Soundness forces that completion to be even. In this model, splicing can combine derivations, but it cannot produce a forbidden odd object.

The one-anchor literal-slice obstruction is also exactly linear: intersecting the `N` matching slices gives the empty set, while every proper subfamily has an odd completion. Thus the high side has maximal proper-subcube richness, every accepting certificate has full width, and there are `2^(N-1)` low anchors, yet a linear-size native closure handles the promise.

## 4. What this falsifies, and what it leaves open

This construction rules out a generic theorem of the form

> dense/shattered high side + full-width output certificates + many low anchors + state reuse => a high hybrid.

It also rules out charging state reuse using only certificate width, high-side shattering, or anchor abundance. The missing property must use the *specific structure and low description complexity* of `SIZE(s1)`, or show that those low circuits fail to possess the parity model's global invariant.

The example does **not** satisfy the actual low-side condition `Y=SIZE(s1)`, and its linear upper bound is not a superlinear lower-bound toy. It is a hostile calibration of the splice implication, not progress toward a P-vs-NP proof. The proof gives no lower bound on the minimum `q` for this toy beyond what separate arguments establish.

## 5. Revised next theorem target

For actual low circuits, a useful splicing theorem must establish more than compatibility. It must show that a small closure cannot make every compatible cross-context join land back inside the low class by a compact global invariant (parity is the toy example). Candidate actual-promise distinctions to test are:

- low circuits are closed under bounded local switching, but not under arbitrary blockwise switching once the total description budget exceeds `s2`;
- the parity toy has a linear sufficient statistic, whereas low-circuit membership requires a globally consistent short *circuit description*;
- spliced hybrids may preserve all local constraints while losing the existence of one common circuit description.

The proof obligation is to turn that last distinction into a quantified statement over the full context/proof grammar, with an explicit `q` cost. C-228, C-234, C-236, and C-247 remain hostile checks. No OPS lower bound, superlinear native-cover bound, or P-vs-NP proof follows here.
