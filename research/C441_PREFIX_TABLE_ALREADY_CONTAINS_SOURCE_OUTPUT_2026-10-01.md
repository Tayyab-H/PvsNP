# C-441 - Full prefix-table generation already pays the source-hardness cost

## The mechanism being tested

C-440 rejects the generic claim that a hard canonical witness makes its prefix-extension table hard. A stronger question is whether the **actual** Ren--Williams history prefix table could still transfer its near-maximum source lower bound to OPS GapMCSP. The relevant source lemma has a useful exact property: the lexicographically largest satisfying assignment `alpha` of `C_x` has a prefix of length `r'` encoding the correct query-count history, and the next `ell` bits equal the output `g_m(x)` of the source machine. Moreover, any satisfying assignment sharing that first `r'`-bit prefix has the same output ([Ren--Williams, Lemma 3.2, pp. 9--10](https://eccc.weizmann.ac.il/report/2026/118/download)).

## Prefix table and decoder

For the source lower bound, take `g_m` to be the Boolean output of the machine (equivalently, apply Lemma 3.2 with `ell=1`). Set `L=r'+ell`. For every binary string `p` of length at most `L`, define

```text
T_x(p) = 1  iff  some satisfying assignment of C_x has prefix p.
```

There are `K=2^(L+1)-1` such prefixes. Pad to `N=2^(L+1)` table positions. The entire `N`-bit table contains the lexicographically largest feasible prefix of length `L`, and therefore contains `g_m(x)` in a fixed output position.

This decoding uses only `O(N)` total fan-in-two gates. Regard the `T_x(p)` values as the extendability labels on a complete binary prefix tree. Set the root's selected flag to 1. For each internal prefix `p`, select its right child if `T_x(p1)=1`, and otherwise select its left child:

```text
selected(p1) = selected(p) AND T_x(p1)
selected(p0) = selected(p) AND NOT T_x(p1).
```

On selected nodes `T_x(p)=1`, so at least one child is extendable until depth `L`. These recurrences select the lexicographically largest satisfying prefix. There are `O(N)` tree nodes and constant work per node; the designated output bit is an OR of the selected leaves with that bit equal to 1. Call this decoder `D_N`, with `CC(D_N)=B_N=O(N)`.

## Source-budget lemma

Let `g_m` have ordinary circuit complexity at least `h_m`. Suppose an ordinary multi-output circuit `G_m` with `J_m` gates generates the full table `T_x` from `x`. Since `D_N(G_m(x))=g_m(x)`, composition gives

```text
J_m + B_N >= h_m,
```

up to a fixed additive constant. If a promise-preserving OPS map also made the separator output `g_m(x)` (up to a NOT gate), then a size-`S_N` separator gives the other composition bound `J_m+S_N+O(1) >= h_m`.

Combining them, any source-hardness contradiction of the form `J_m+S_N<h_m` could only occur when

```text
S_N < B_N + O(1) = O(N).
```

Therefore this complete-prefix-table transfer cannot prove the OPS target `S_N>N^(1+epsilon)` for any fixed epsilon: the source output can already be recovered from the table using only linear-size decoding, and the source lower bound forces the generator to have spent all but `O(N)` of the available hardness budget. This is a **route-specific budget obstruction**, not a lower bound or upper bound on `SepCC`, and not an impossibility theorem for other maps.

The argument counts ordinary total fan-in-two gates only. It does not identify gate count with table-output wires, router description bits, uniform construction time, or native fusion states. It also does not assume that a separator reconstructs a witness: the reconstruction is a separate `O(N)` decoder for this particular all-prefix table.

## Paired promise attacks and current upper bound

Even the promised Low/High mapping for `T_x` is unproved. C-440 supplies a unique-witness table that is always Low and a one-query history with both satisfiable `phi(z)=z_1` and unsatisfiable `phi(z)=0` yielding Low prefix tables. The actual multi-query `C_x` family could have additional structure, but no outcome-dependent gap has been established.

The paired complete separator remains exact Low-description enumeration. With `K_0=2^(O(N^beta))` Low descriptions `d`, use `E_d(x)=AND_{i<N}[x_i=C_d(i)]` and `Sep(x)=OR_d E_d(x)`, for `O(NK_0)` total gates and wires. No near-linear implementation is known.

## Status and frontier

**Project-proved:** the all-prefix table for the source's encoded history has an `O(N)` decoder for the hard output. Any generator `G_m` for that table must satisfy `CC(G_m)+O(N)>=CC(g_m)`. Thus the source-transfer composition through this table has no hardness budget to establish a superlinear separator lower bound.

**Not proved:** no OPS Low/High map for `T_x`; no source-specific lower or upper bound on `CC(T_x)` for the actual `C_x`; no lower bound on OPS separators from this budget lemma.

**Frontier unchanged:** ordinary `N-O(N^beta log N)-1` plus C-406 refinement; OPS `N^(1+epsilon)` remains open with one common epsilon for every sufficiently small fixed beta; exact full-promise upper `O(N*2^(O(N^beta)))`; native `rho>=N-o(N)` separate. No P-vs-NP breakthrough.
