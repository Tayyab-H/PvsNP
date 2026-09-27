# C-274 - Small conflict support forces the map to pay almost the source lower bound

Date: 27 September 2026  
Classification: **GLOBAL-STRUCTURAL (necessary condition on C-125 maps).**  
Route: A, exact LowExt transfer from a monotone promise function.

## Theorem

Let `f:{0,1}^M -> {0,1}` be monotone, with at least one YES input. Let `phi` be a monotone signed-rail map with `a` AND gates satisfying C-125:

```text
f(x)=1 => e(w_x) <= phi(x) for some w_x in SIZE(s1),
f(x)=0 => phi(x) <= e(z_x) for some z_x outside SIZE(s2).
```

Write `N=2^n` for the table length, and let

```text
S = { i in [N] : some YES image phi(x) activates both rails at i },
delta = |S|.
```

There is an absolute constant `K` for point-minterm patching such that, whenever

```text
s1 + K n (delta+1) <= s2,
```

the source has an ordinary monotone circuit with at most

```text
a + N - delta - 1
```

AND gates. In particular,

```text
CycAnd(f) <= a + N - delta - 1.
```

Consequently every C-125 map obeys the dichotomy

```text
delta > floor((s2-s1)/(K n))-1
or
a >= CycAnd(f) - N + delta + 1.
```

## Proof

For every YES input `x`, select a low witness `w_x`. The YES set of a monotone Boolean promise is upward closed. For two YES inputs `x,y`, their join `x OR y` is YES, and monotonicity of `phi` gives

```text
e(w_x) <= phi(x) <= phi(x OR y),
e(w_y) <= phi(y) <= phi(x OR y).
```

If `w_x[i] != w_y[i]`, both signed rails at coordinate `i` occur in `phi(x OR y)`. Hence `i in S`. All selected witnesses therefore agree outside `S`; fix one YES input `x0` and its witness `w0`.

Define

```text
g(x) = AND_{i notin S} phi_{i,w0[i]}(x).
```

Every YES input activates all these fixed rails, so `g(x)=1` on YES inputs. Suppose a NO input `x` also had `g(x)=1`. Its high completion `z_x` must agree with `w0` at every coordinate outside `S`, because `phi(x)<=e(z_x)` and the corresponding `w0[i]` rail is present.

Patch `w0` on the `delta` coordinates in `S` to obtain `z_x`: an equality minterm for each patched address, followed by a disjunction, gives a fan-in-two circuit of size at most `K n(delta+1)` beyond the circuit for `w0`. Thus

```text
CC(z_x) <= s1 + K n(delta+1) <= s2,
```

contradicting the high-completion condition. Therefore `g` is a separator for `f`. It uses the `a` AND gates of `phi` plus `N-delta-1` AND gates to conjoin the fixed rails. This proves the bound.

For the dichotomy, if `delta` is at most `floor((s2-s1)/(K n))-1`, the patch inequality holds and rearranging gives `a >= CycAnd(f)-N+delta+1`. Otherwise the conflict support exceeds that threshold.

## Consequence for matching transfer

For Rao's promise `MATCH_v`, C-266 gives `CycAnd(MATCH_v)>=exp(c sqrt(v))`. Under `v=A(log N)^2`, this is `N^{c sqrt(A)-o(1)}` (with the logarithm base absorbed into `c`). Choose `A` so this exceeds `N^{1+epsilon}`. A C-125 map with `a < CycAnd(MATCH_v)-N` must then have

```text
delta = Omega((s2-s1)/log N) = Omega(N^beta/log N)
```

for fixed `0<beta<1` and the project parameters. This is much stronger than C-127's `Omega(log N)` conflict-support requirement. It does not rule out such broad support: the same `delta` is still `o(N)`, and map outputs can share gates across all coordinates.

## Scope and next test

This is a necessary-condition theorem for a source map; it does not improve the actual fusion lower bound. It strengthens the common-baseline obstruction C-269: a map cannot hide its YES witness variation inside a patchable global set of fewer than about `s2/log N` coordinates and still have AND-cost below the source lower bound minus `N`.

Next test broad-conflict architectures directly. For a candidate map, track for each YES input the active conflict set, its union `S`, and whether the NO high completions can remain consistent after those conflicts activate. In particular, distinguish a large global union of conflicts from many conflicts activated together on one YES input; C-274 only lower-bounds the union.

No map satisfying the remaining large-conflict condition has been constructed. The actual fusion bound remains `q=N-o(N)`.
