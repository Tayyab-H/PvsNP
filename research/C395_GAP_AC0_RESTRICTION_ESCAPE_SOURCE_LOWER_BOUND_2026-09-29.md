# C-395 - Local restrictions force unbounded escape sources in polynomial-size native covers

Date: 29 September 2026  
Route: compose the exact C-393 escape-source compiler with the local-restriction proof for small-depth MCSP separators, using the project's actual low/high thresholds.  
Classification: **PROVED PROMISE-SPECIFIC AC0 LOWER BOUND AND NATIVE PARAMETER DICHOTOMY; NO SUPERLINEAR q BOUND.**

## 1. Promise and result

Let the truth-table length be `N=2^n`, fix `0<beta<1`, and take the project's thresholds

```text
s1 = N^beta / (c log N),
s2 = N^beta,
```

for any fixed constant `c>0`. A separator accepts every table of circuit size at most `s1` and rejects every table of circuit size greater than `s2`; its behavior in between is unrestricted.

**Theorem 1 (gap-preserving AC0 restriction bound).** Fix a depth `d>2`. For every fixed

```text
0 < a < min{ beta/4, (1-beta)/(2(d-2)), 1/(2(d-1)) },
```

and all sufficiently large `N`, no depth-`d` AC0 circuit of size at most `exp(N^a)` separates this promise.

The proof uses the locally computable restriction lemma of Cheraghchi, Kabanets, Lu, and Myrisiotis (CKLM), but replaces their exact-MCSP counting step with a count at the project's high threshold `s2`. Thus the thresholds and unconstrained middle interval are handled explicitly; this is not an unqualified transfer from exact MCSP.

## 2. Proof of Theorem 1

Assume that a depth-`d` separator `C` has size `S<=exp(N^a)`. CKLM's local-restriction lemma supplies a restriction `rho` with `m` star coordinates such that the restricted output is constant and

```text
m >= N / O((log S)^(d-2)) - log S.
```

The fixed restriction pattern is locally computable: the table `f0` agreeing with its fixed bits and setting every star to zero has a circuit of size

```text
lambda = d log N * O_tilde((log S)^3) = N^(3a+o(1)).
```

Since `a<beta/4`, we have `lambda < s1` for sufficiently large `N`. Therefore `f0` is a YES table and the constant value of `C` on the restriction subcube must be 1.

The star positions give `2^m` distinct completions. The number of tables with circuit size at most `s2` is at most the number of circuit descriptions,

```text
|SIZE(s2)| <= 2^(O(s2 log(s2+n))) = 2^(N^(beta+o(1))).
```

The two restrictions on `a` involving `d` ensure

```text
m >= N^(1-a(d-2)-o(1)) >> N^beta log N.
```

Hence `2^m>|SIZE(s2)|`, so at least one completion has circuit size greater than `s2`. It is a NO table, but `C` is constant 1 on the entire restricted subcube. Contradiction.

The structural restriction lemma is CKLM, *Circuit Lower Bounds for MCSP from Local Pseudorandom Generators*, Lemma 29 and its proof of Theorem 28. Their exact-MCSP proof counts circuits at the local threshold `lambda`; the argument above instead counts circuits at `s2`, while the all-zero completion remains below `s1`. The strict exponent margins above absorb the lemma's polylogarithmic factors.

## 3. AC0 compiler for the C-393 normal form

Let a valid C-319 cover have `q` rules, `m0` empty-carrier roots, and `v=q-m0` nonroot candidates. After the C-393 normalization, let `k` be the number of distinct one-sided escape-source carriers. Each macro-round computes, for each candidate rule `i`,

```text
d_i = (a_i OR OR_{u in L_i} x_u)
      AND (b_i OR OR_{u in R_i} x_u),
```

then forms the upward closure of the true `d_i` values. The fixed seed clauses `a_i,b_i` are ORs of signed truth-table literals. In AC0, each side expression is one unbounded-fan-in OR gate, each `d_i` is one AND gate, and each carrier's upward-closure bit is one OR gate. Thus a macro-round has constant depth (OR-AND-OR) and O(q) gates; there are at most `k+1` macro-rounds by C-393. Root terminal tests add only constant depth and O(q) gates.

Consequently the exact separator computed by Q has an AC0 implementation of depth `O(k+1)` and size polynomial in `q,N` (indeed O(q(k+1)) gates in the unbounded-fan-in gate-count convention, with polynomially many wires for polynomial q). This circuit agrees with Q on every table, including the unrestricted middle region.

## 4. Native consequence

Fix `beta`, and suppose a family of valid full-promise C-319 covers has `q<=N^A` for some fixed `A`. If its escape-source count `k` were bounded by a fixed `K` on infinitely many input lengths, the compiler above would give polynomial-size AC0 separators of one fixed depth on that subsequence. Theorem 1 rules this out. Therefore

```text
for every fixed A,K, all sufficiently large N satisfy:
  every valid Q with q<=N^A has k(Q)>K.
```

In particular, every polynomial-state family of valid covers has `k(Q)=omega(1)`. Equivalently, any family with bounded escape-source count must have superpolynomially many native rules. This is the first proved OPS-specific lower bound on the C-393 escape-source parameter.

## 5. Scope and next obligation

This does **not** imply `q>N^(1+epsilon)`: a near-linear cover may have a slowly growing number of escape sources. Nor does `A_cap<=m0+(k+1)v` become a lower bound; C-393 remains an upper compiler. The new theorem rules out the bounded-k endpoint of the construction space and supplies an exact promise-specific route for testing quantitative lower bounds on k.

Next derive a growing-depth version with explicit dependence on `d` and the CKLM restriction parameters. A rate such as `k>=Omega(log N/log log N)` would be materially stronger, but it is **not proved here**. Any such extension must audit the uniform dependence of the pseudorandom restriction lemma on a depth that grows with `N`.

The native q checkpoint remains `N-o(N)`. No full-promise near-linear construction or P-vs-NP proof follows.
