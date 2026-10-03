# C-457 — a near-linear sound test can cover diverse Low families and still miss Low

**Date:** 1 October 2026  
**Question:** Does the C-456 algebraic obstruction disappear if we require the counterexample to be sound against the *entire* OPS High set and accept several genuine Low families?  
**Result:** No. There is an explicit `O(N log N)` ordinary circuit whose accepting set is entirely Low, which accepts every sufficiently sparse/co-sparse table and every truth table of sufficiently low algebraic degree, has all `N` input bits essential, has sparse support and ANF degree `N-o(N)`, yet rejects an explicit `O(n)`-gate Low table. This is a sound but incomplete separator. It proves that soundness, broad structured completeness, and the coarse C-456 invariants still do not price shared gates; full completeness on all Low tables is the decisive missing condition.

## 1. Parameters and two genuine Low subfamilies

Let `N=2^n`, `s1=N^beta/(c n)`, `s2=N^beta`, and fix sufficiently small constant `0<beta<1/2`. Choose a constant `alpha>0` so that

```text
H_2(alpha) < beta,       alpha < 1-beta,       alpha < 1/2.
```

Let `d=floor(alpha n)` and `M=sum_(j=0)^d binom(n,j)`. Then `M=2^(H_2(alpha)n+o(n))=N^(H_2(alpha)+o(1))`.

**Low-degree family.** Every `n`-variable Boolean function whose algebraic normal form has degree at most `d` uses at most `M` monomials. Compute each monomial by at most `n-1` AND gates and combine the terms with XOR gates; one XOR uses a constant number of ordinary fan-in-two AND/OR/NOT gates. Thus

```text
CC(f) = O(n M) = N^(H_2(alpha)+o(1)) poly(n) < s1
```

for all sufficiently large `n`.

**Sparse/co-sparse family.** Set `k=floor(s1/(4(n+1)))`. A truth table of Hamming weight at most `k` has a DNF with at most `k` address minterms, each using `O(n)` gates, and is Low. A table whose complement has weight at most `k` has the dual CNF and is also Low.

## 2. One ordinary circuit recognizes their union soundly

On an arbitrary input table `T` of length `N`, define

```text
Q(T) = [wt(T)<=k] OR [wt(T)>=N-k] OR [T belongs to RM(d,n)].
```

The first two predicates are computed by a binary population counter and comparisons to constants, using `O(N log N)` fan-in-two gates. To test Reed–Muller membership, apply the fast Möbius transform to the `N` truth-table entries; it computes all ANF coefficients with `nN/2` XOR operations. Test that every coefficient indexed by a monomial of degree greater than `d` is zero, using `O(N)` additional gates. Each XOR expands to a constant-size AND/OR/NOT circuit. Therefore

```text
CC(Q) = O(N log N).
```

Every accepted table is Low by Section 1, so `Q(T)=0` on **every** formal OPS High table (`CC(T)>N^beta`). In fact, the circuit rejects the stronger auxiliary set `CC(T)>=N^beta` too, including an integral equality boundary. This statement covers the full actual High set, not a sampled or artificial NO family.

Its accepting set is sparse. The sparse/co-sparse part has at most `2 sum_(j<=k) binom(N,j)=2^(O(k log(N/k)))` members; the Reed–Muller code has `2^M` members. Since `k log(N/k)=O(N^beta)` and `M=N^{H_2(alpha)+o(1)}<N^beta`,

```text
|Q^(-1)(1)| <= 2^(O(N^beta log N)).
```

Consequently C-456's Reed–Muller argument also gives `deg_GF(2)(Q)>=N-O(N^beta log N)`.

## 3. Essentiality and a concrete missed Low table

The circuit `Q` depends on every table coordinate. The Reed–Muller code has minimum nonzero weight `2^(n-d)=N^(1-alpha+o(1))`, which is much larger than `k+1` because `alpha<1-beta`. For any coordinate `i`, choose a weight-`k` table `T` with `T[i]=0`. It is outside the Reed–Muller code and accepted by the sparse arm. The table `T+e_i` has weight `k+1`, is still below the Reed–Muller minimum distance, and is neither sparse nor co-sparse; it is rejected. Hence flipping coordinate `i` changes `Q`.

Despite its soundness and rich acceptance set, `Q` is not a full-promise separator. Let `m=d+1` and define the address function

```text
g(x_1,...,x_n) = AND_(j=1)^m (x_(2j-1) XOR x_(2j)).
```

The parity constraints use disjoint pairs, so `g` has exactly `N/2^m= N^(1-alpha+o(1))` satisfying addresses and an `O(n)`-gate circuit. It is Low. Its algebraic degree is `m>d`, so its truth table is not in `RM(d,n)`; its weight is larger than `k` and smaller than `N-k`. Therefore `Q(tt(g))=0`, violating Low completeness.

This example is an **incompleteness witness**, not a counterexample to an OPS lower bound. The full promise requires acceptance of this table and every other Low table, including small circuits with high ANF degree and non-extreme weight.

## 4. What the construction teaches about the lower-bound target

The partial separator has, simultaneously:

- total ordinary gates `O(N log N)` with fan-in two and arbitrary reuse;
- all `N` essential table inputs;
- sparse acceptance set of size at most `2^(O(N^beta log N))`;
- ANF degree `N-O(N^beta log N)`;
- sound rejection of every promised High table;
- completeness for all sparse/co-sparse Low tables and the full `RM(d,n)` Low family.

Thus a lower bound for arbitrary **sound one-sided recognizers** of these shapes, or one based only on support, degree, essentiality, and membership in one rich low-code family, cannot give the OPS superlinear bound. The remaining semantic burden is exactly the universal Low-completeness quantifier: arbitrary small circuits need not be sparse, co-sparse, low-degree, or members of a single efficiently recognizable family.

This does not establish that checking the union of all Low families is hard; it only rules out treating a few high-entropy subclasses as though they forced that check. It also provides no compiler to the native cyclic fusion measure.

## 5. Paired full-promise construction and frontier

No full-promise near-linear separator was found. Exact enumeration still accepts iff some size-`s1` circuit matches all `N` table entries, with gate cost `O(N 2^(O(N^beta)))`.

**Strongest result this cycle:** an explicit `O(N log N)` sound incomplete separator accepts the specified large Low families and rejects all High tables, while exhibiting all C-456 coarse features. **Quantitative effect:** none. The ordinary lower bound remains `N-O(N^beta log N)-1` plus C-406's additive refinement; the common-fixed-`epsilon` OPS target remains open; native `rho>=N-o(N)` is separate; no P-vs-NP proof.

**Next mechanism:** do not add more low code families one at a time. A surviving proof must either lower-bound arbitrary shared circuits for the exact full Low/High sandwich or discover a uniform structural decomposition of *all* `s1`-size circuits whose complete membership test has a provable gate lower bound. The second route is substantive only if the decomposition/checker is constructed, not assumed.
