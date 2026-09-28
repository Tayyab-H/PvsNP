# C-283 — Bottom-baseline holes defeat the C-282 collision proof

Date: 27 September 2026  
Classification: **COUNTEREXAMPLE** to the C-282 proof step and route closure.

## Finding

C-282 claims that if a bottom NO image lies below a high one-hot code `e(z0)`, then every YES low code `e(w)` creates a two-rail collision somewhere in the YES image. The proof uses `w != z0` to select a differing coordinate, then assumes the bottom image already contains the `z0` rail there. That last assertion is false for a partial rail vector: the bottom image may leave that coordinate empty.

Let `P = phi(0)` and write `p_j` for the set of rails active at coordinate `j`. Since `P <= e(z0)`, each `p_j` is either empty or `{z0[j]}`. If a YES witness `w` differs from `z0` only at coordinates where `p_j` is empty, monotonicity does not force any opposite rail into `phi(x)`. Thus the collision predicate in C-282 may reject a YES input.

## Minimal counterexample to the claimed implication

Take a one-bit monotone promise `f(x)=x`, with low table `w=1` and a disjoint high table `z0=0`. Define `phi(0)=empty` and `phi(1)=e(1)`. This is coordinatewise monotone; the NO image is below `e(z0)` and the YES image contains `e(w)`. Yet no image has a two-rail collision, so `OR_j(phi_(j,0) AND phi_(j,1))` is identically zero and does not separate `f`.

The example satisfies the abstract one-hot order conditions used in C-125; it is a counterexample to the asserted *collision-detector derivation*. It is not an OPS parameter instance and does not refute the C-125 composition theorem or exhibit a hard source map.

## Corrected bottom-image decomposition

Let `P=phi(0)` and assume the C-125 conditions. Define the set of low tables compatible with the bottom partial vector by

```text
K(P) = { w in SIZE(s1) : P <= e(w) }.
```

Let `J` be the pinned coordinates and `H` the `d` holes of `P`. Use the separator

```text
G(x) = OR_(j in J) (phi_(j,0)(x) AND phi_(j,1)(x))
       OR OR_(w in K(P)) AND_(j in H) phi_(j,w[j])(x).
```

For YES `x`, choose its low witness `w`. If `P` and `e(w)` are inconsistent, their conflict is on a pinned coordinate, and monotonicity carries both rails into `phi(x)`. If they are consistent, `w in K(P)` and `e(w)<=phi(x)`, so the hole-coordinate term accepts. For NO `x`, monotonicity gives `P<=phi(x)<=e(z_x)`, so the high completion `z_x` agrees with every pinned bit of `P`. No pinned collision occurs. If a `w in K(P)` matched `z_x` on all holes, it would also agree on all pinned coordinates and hence equal `z_x`, contradicting that `w` is low and `z_x` is high. Thus no hole-coordinate term accepts; `G` separates the source.

If the map has `a` AND gates and `K=|K(P)|`, the direct implementation costs at most

```text
a + (N-d) + K max(d-1,0)
```

AND gates: one per pinned-coordinate collision, and at most `d-1` per low-code test on the holes; pinned rails are already supplied by `P` and the ORs are free in this measure. Therefore

```text
CycAnd(f) <= a + (N-d) + K max(d-1,0).
```

This repairs the proof by identifying the bypass precisely: YES witnesses compatible with the bottom partial image need not collide and must instead be handled through the family `K(P)`. C-282's claimed universal bound `a+N` follows only when `K(P)=empty` (or under another condition that makes every YES witness collide), not from the stated C-125 hypotheses. The hole-sensitive bound is stronger than the coarse `a+N+K(N-1)` version.

Let `d(P)` be the number of coordinates at which `P` has neither rail. Because `P` is consistent, it pins one bit at every other coordinate, so

```text
K <= min(|SIZE(s1)|, 2^d(P)).
```

Consequently any C-125 transfer that aims to certify `q>N^(1+epsilon)` through `q>=L-a` must satisfy

```text
N-d + K max(d-1,0) > N^(1+epsilon).
```

Since `K<=2^d`, this forces `d >= (1+epsilon)log2(N)-log2(log N)-O(1)`. This is only a necessary condition on the map's bottom image; it neither constructs a map nor bounds the actual q. It does show exactly why a nearly complete baseline restores the C-282 collision argument, while a reduction that evades it must leave enough holes for its compatible low-code family to carry the hardness.

## Stronger gap-sensitive hole requirement

If `K(P)` is nonempty, choose `w in K(P)` and the high completion `z0` of `P` at the bottom NO input. Both extend P, so they differ only on its d holes. If they differ on t<=d addresses, sparse-support interpolation changes `w` into `z0` using `O(t n/log(t+1)+n)` gates. Thus

```text
CC(z0) <= s1 + O(d n/log(d+1)+n).
```

For the OPS gap `s1=s2/(c0 n)` and fixed `0<beta<1`, this contradicts `CC(z0)>s2` whenever `d<=c_beta s2`, for a sufficiently small constant `c_beta>0`. Hence every useful map with even one bottom-compatible low code must leave `d=Omega_beta(s2)=Omega_beta(N^beta)` coordinates unpinned. This is the same scale as C-275's broad YES-conflict support condition, but it concerns the single bottom NO cylinder and follows from its simultaneous low and high completions. Combined with the exact separator bound, a target `q>N^(1+epsilon)` also requires `K(d-1)>N^(1+epsilon)-N+d`.

## Hostile check and route consequence

C-279 passes the hole requirement in the most extreme way: its bottom image is empty, so `d=N` and every low table is compatible with the baseline. It is still quantitatively useless because adjacent rank predicates expose a source decoder of only `O(log^2 N)` AND gates. Thus a large bottom-compatible family is necessary in some transfers but does not solve the hard selection/decoding problem. A surviving map must use the holes to carry many low-code choices without exposing a short decoder, while every NO image retains a high completion.


C-282's claim that the exact C-125 interface can certify at most `N` states is withdrawn. C-266/C-267's cyclic matching lower bound and parameter arithmetic remain valid conditional ingredients. Route A remains open at the original obligation: construct a low-AND monotone map satisfying C-125, or derive a new bound controlling the number and structure of low completions compatible with its bottom NO image. The corrected inequality only caps transfers when `K(P)` is small; it gives no useful cap when `K(P)` is large. The actual native bound remains `q=N-o(N)`.

## Proof audit note

The order distinction matters. `e(w)<=u` is the C-125 low-code witness relation. `u<=e(w)` says that `w` is a completion of the partial rail vector `u`. A bottom NO image may have many low completions in the second sense while having no low code below it in the first sense. A high completion alone does not rule those out.
