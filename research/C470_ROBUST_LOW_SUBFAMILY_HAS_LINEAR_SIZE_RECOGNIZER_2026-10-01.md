# C-470 — a robust Low subfamily has a linear-size one-sided recognizer

**Status:** proved counterconstruction to geometry-only gate charges. It is not a full Gap-MCSP separator and does not change the lower-bound frontier.

## 1. Exact claim

Put `N=2^n`, fix a constant `0<beta<1/2`, and use the project's normalization `c=10` of the OPS low threshold (the same argument works for any fixed positive theorem constant):

```text
s1 = floor(N^beta/(10n)),     s2 = N^beta.
```

There are constants `a,b>0` and, for all sufficiently large `N`, a set `C_N` of `2^{Theta(s1)}` truth tables and two radii

```text
r_in  = floor(a*s1/n) = Theta(N^beta/n^2),
r_out = floor(b*s2/n) = Theta(N^beta/n),
```

such that:

1. every `c in C_N` has `CC_n(c) <= s1`;
2. every table at distance at most `r_in` from `C_N` has complexity at most `s1`, so every valid OPS separator is forced to accept those inner balls;
3. every table at distance at most `r_out` from `C_N` has complexity at most `s2`;
4. the predicate `F_N(T)=1 iff dist_H(T,C_N)<=r_out` has an ordinary fan-in-two AND/OR/NOT circuit of `O(N)` gates and rejects every actual OPS-High table;
5. the one-set has size `2^{Theta(N^beta)}` and is the disjoint union of radius-`r_out` balls around `C_N`.

Thus an exponentially large-in-`s1` family of genuinely Low anchors, the Hamming thickening every separator is forced to accept around these slack anchors, a larger sound thickening with support `2^{Theta(N^beta)}`, and rejection of **every** High table coexist with only `O(N)` total gates. The extra outer-ball points lie in the unconstrained middle band and are not claimed to be forced positive.

## 2. Construction of the Low anchors

Choose an absolute constant `c_mux` so a mux tree with `k` constant leaves costs at most `c_mux*k` gates. Let `k` be the largest power of two at most `s1/(4*c_mux)`, and put `L=N/k`. Regard the N table coordinates in their natural lexicographic order as `k` consecutive blocks of length `L`.

For each `q in {0,1}^k`, define `c_q` to be constant `q_j` on block j. Its table circuit reads the `log k` most significant address bits and uses a mux tree with the `q_j` as constant leaves. Hence `CC_n(c_q)<=c_mux*k<=s1/4` (absorbing fixed small-size overhead for large N). The `2^k` tables are distinct. Their minimum pairwise Hamming distance is exactly `L`.

## 3. Robustness and the High endpoint

If two n-input truth tables differ at `t` addresses, a circuit for one can be patched into a circuit for the other with at most `c_patch*t*(n+1)+O(1)` extra gates: form equality minterms for the changed addresses and XOR their disjunction with the old output. This is the standard address-patching bound.

Choose `a,b>0` small enough that

```text
c_mux*k + c_patch*r_in*(n+1) + O(1) < s1,
c_mux*k + c_patch*r_out*(n+1) + O(1) < s2,
```

for the radii above. This is possible because `k=Theta(s1)` and `s1=o(s2)`. Every inner-ball table is therefore Low, while every table in an outer ball has complexity at most `s2`. If `CC_n(T)>s2`, then `dist_H(T,C_N)>r_out`; otherwise patching would give `CC_n(T)<=s2`. The outer-radius detector rejects the entire actual High set. Only the `r_in` balls are forced positive by the promise; outer-ball labels outside them may lie in the middle band.

For fixed `beta<1/2`,

```text
L=N/k=Theta(n*N^(1-beta))  >>  r_out=Theta(N^beta/n),
```

so `2r_out<L` for sufficiently large N. The outer-radius balls around distinct codewords are disjoint.

## 4. O(N)-gate recognizer with unrestricted sharing

For each input block j, compute its Hamming weight `w_j`. A balanced tree of binary adders computes all block weights using `O(L)` gates per block: at level i there are `L/2^i` adders of width `O(i)`, and `sum_i (L/2^i)*O(i)=O(L)`. Across all blocks the cost is `O(N)`.

The nearest block-constant codeword chooses the majority bit in each block. Its distance is

```text
d(T,C_N) = sum_{j=1}^k min(w_j, L-w_j).
```

Each minimum costs `O(log L)` gates; summing the k values and comparing with `r_out` costs `O(k log N)`. Since `k=Theta(N^beta/n)`, this is `O(N^beta)`, below `O(N)`. The full circuit therefore has `O(N)` total gates. This count includes all arithmetic gates; no table ROM, free computation, or uncharged conditional execution is used. The hardwired block grouping only specifies which primary input wires feed each adder.

Because `2r_out<L`, the accepting set is exactly `2^k` disjoint Hamming balls. For fixed beta,

```text
log2 |F_N^{-1}(1)| = k + log2(sum_{i<=r_out} binom(N,i)) = Theta(N^beta),
```

using `r_out=Theta(N^beta/n)` and `log(N/r_out)=Theta(n)`. Thus its support is `2^{-N+Theta(N^beta)}` as a fraction of the full cube. The smaller, promise-forced inner-ball union has logarithmic size `Theta(s1)` for this particular anchor family.

## 5. Strong counterexample and exact limitation

This is **not** a full OPS separator. The one-bit function `T(a)=a_0` (the least significant address bit) is a Low table, but it alternates inside every length-L block. Its distance from every block-constant codeword is `N/2`, so `F_N(T)=0` for large N. The construction recognizes one structured robust Low subfamily and rejects all High tables, but it omits many Low circuits.

The decisive obstruction is therefore completeness over the whole class of `s1`-gate functions. This counterconstruction refutes any proposed gate lower bound that uses only the number of robust Low anchors `2^{Theta(s1)}`, their forced inner radius, an `O(N)`-recognizable larger neighborhood of support `2^{Theta(N^beta)}`, and global rejection of High tables. It does **not** refute a mechanism that uses the full algebraic and compositional diversity of all Low circuit tables, and it is not a near-linear full-promise separator.

## 6. Barrier and originality check

The ingredients here are standard: a repetition code, Hamming-ball thickening, address patching, and binary population counts. The project-specific result is the exact parameter fit: an `O(N)` ordinary circuit accepts balls forced positive around many genuine OPS-Low tables, accepts a larger sound neighborhood with support `2^{Theta(N^beta)}`, and rejects the entire OPS-High set. No claim of a new coding-theory theorem is made.

This is not a hardness-magnification locality-barrier theorem. Oliveira et al.'s primary paper describes that barrier as a limitation on adapting existing weak-model lower-bound techniques when magnification targets have efficient small-fan-in-oracle circuits. C-470 instead falsifies a proposed geometry-only lower-bound mechanism with a direct circuit construction; it neither extends nor resolves that barrier. See [Oliveira et al., ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/).

## 7. Next mechanism, not a sharper version of the failed one

Retire robust-anchor geometry as a standalone charge. The next direct attempt must use circuit-completeness closure: it must exploit that every size-`s1` circuit table is accepted, including mutually incompatible representations such as address parities, muxes, sparse and dense tables, and blockwise relations. State a gate-by-gate invariant for an arbitrary shared DAG that depends on this closure, or pair it with a complete separator construction. Do not infer a cost from anchor count or Hamming volume again.

## 8. Paired complete-separator construction attempt

Complete the one-sided recognizer by OR-ing equality tests against every distinct Low table. Equivalently, enumerate every size-`s1` circuit description, compute its N-bit table, and test equality with the input. This accepts every promised YES and rejects every High table (indeed, it accepts only Low tables). With `K=2^{O(s1 log(n+s1))}=2^{O(N^beta)}` descriptions, direct fan-in-two implementation costs `O(NK)` gates up to absorbed polynomial factors. Allowing radius-r balls around each Low anchor preserves High rejection by the patch bound but has the same enumerative scale. This is a complete separator construction, but it does not approach near-linear size and gives no improvement over the durable upper bound.

## 9. Frontier effect

No change. The ordinary lower bound remains `N-O(N^beta log N)` with the C-406 additive logarithmic reconvergence refinement. Exact full-promise enumeration remains `O(N*2^(O(N^beta)))`. No fixed-epsilon OPS lower bound, native-`rho` transfer, or P-vs-NP proof follows. C-470 is a proved counterconstruction and a sharper statement of the missing completeness obligation.
