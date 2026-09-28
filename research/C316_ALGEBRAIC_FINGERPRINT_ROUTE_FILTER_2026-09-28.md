# C-316 - Algebraic fingerprints: exact-difference and equality-sketch limits

Date: 28 September 2026  
Classification: **SCOPED ROUTE FILTER.** This rules out compressed multiplicative fingerprints that detect every table difference, and gives a dimension bound for linear equality sketches separating the OPS promise. It is not a lower bound on native fusion size.

## 1. Exact-difference algebra fingerprints

Let `X` be an address set of size `N`, and let

```text
B = F_2^X
```

be the algebra of all functions `X -> F_2`, with pointwise addition and multiplication. For each `x in X`, let `delta_x` be the indicator of address `x`. The `delta_x` are pairwise orthogonal idempotents and `sum_x delta_x = 1`.

Suppose a finite family of unital `F_2`-algebra homomorphisms

```text
phi_t : B -> A_t
```

has finite-dimensional commutative `F_2`-algebra targets, and its product map

```text
Phi : B -> product_t A_t
```

detects every difference of truth tables: `f != g` implies `Phi(f) != Phi(g)`. Then

```text
sum_t dim_F2(A_t) >= N.
```

**Proof.** Exact difference detection makes `Phi` injective, so `Phi(delta_x) != 0` for every `x`. The images `e_x = Phi(delta_x)` remain pairwise orthogonal idempotents. They are linearly independent: if `sum_x c_x e_x = 0`, multiplying by `e_y` gives `c_y e_y = 0`, hence `c_y = 0`. The product target therefore has dimension at least `N`, and its dimension is `sum_t dim_F2(A_t)`.

In particular, if each target is a field, its only idempotents are `0` and `1`. Since the images of the `delta_x` are orthogonal and sum to `1`, exactly one maps to `1`. Thus every scalar-valued algebra homomorphism is evaluation at a single address. A family of scalar multiplicative fingerprints that detects every difference must include all `N` addresses.

This is an exact obstruction to replacing all-address equality checking by a lower-dimensional *multiplicative* fingerprint. It does not apply to arbitrary nonlinear summaries or to a separator that only needs to distinguish selected pairs.

## 2. Linear equality sketches for the OPS promise

Let

```text
L : F_2^N -> F_2^d
```

be linear. Consider an equality-sketch separator that accepts a table `z` when `L(z) = L(w)` for some witness `w in SIZE(s1)`, and is required to reject every `z not in SIZE(s2)`. The zero table belongs to `SIZE(s1)`, so soundness implies

```text
ker(L) subseteq SIZE(s2).
```

Writing `r = rank(L)`, rank-nullity and standard circuit-description counting give

```text
2^(N-r) = |ker(L)| <= |SIZE(s2)| <= 2^(O(s2 log(s2+n))),
```

and therefore

```text
d >= r >= N - O(s2 log(s2+n)).
```

For the OPS parameters `N = 2^n`, `s2 = N^beta`, and fixed `0 < beta < 1`, this is

```text
d >= N - O(N^beta log N) = N - o(N).
```

This bound concerns linear sketches used through equality with a low witness. It does not rule out nonlinear separators, other uses of sketches, or arbitrary fusion covers.

## 3. Cost of explicit gate-by-coordinate evaluation

For a size-`s1` Boolean circuit `C`, direct evaluation at `r` addresses instantiates each circuit gate once per address, using `O(r s1)` scalar gate operations. For the scalar-valued homomorphisms classified above, exact detection of every table difference requires all `N` address evaluations. Running `C` at those addresses explicitly therefore costs

```text
O(N s1) = O(N^(1+beta) / log N)
```

under the OPS scaling `s1 = N^beta/(c log N)`. This is `N^(1+beta-o(1))`, not `N^(1+o(1))`, for fixed positive `beta`.

This is the count for that direct evaluator, not a lower bound on every algorithm for evaluating a circuit or on the native fusion measure. The dimension lemma for general algebra targets does not by itself imply this gate-count bound. Neither result proves that every low/high separator must materialize these coordinates.

## 4. Scope and status

The exact-difference lemma excludes a low-dimensional algebra-homomorphic fingerprint family; scalar homomorphisms reduce to address evaluations. The linear-sketch lemma forces near-full rank for the stated equality-separator interface. The direct evaluator then has gate-by-coordinate cost `O(N s1)`.

These claims do **not** provide a full-promise cover, a superlinear lower bound on its minimum size, a lower bound on the actual fusion measure, or a P-vs-NP result. The C-314 hard-block selector remains unresolved. No central state, model, or queue file is changed by this report.
