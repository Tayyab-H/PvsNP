# C-271 - Near-linear cover attempt via circuit-description quotients

Date: 27 September 2026  
Route: full-promise `SIZE(s1)` versus complement-`SIZE(s2)` fusion cover.  
Classification: **ROUTE-KILL (explicit-description and independent-block constructions only).**

## Attempt

Try to keep one circuit witness coherent across all N truth-table addresses while sharing the local checks. Let `D_s1` be the set of legal circuit descriptions of size at most `s1`; a direct universal verifier is

```text
OR_{d in D_s1} AND_{k in [N]} [w[k] = C_d(k)].
```

Its AND count is at most `N |D_s1|`. Standard description counting gives

```text
|D_s1| <= 2^{O(s1 log(s1+n))}.
```

For `s1=N^beta/(c n)`, fixed `0<beta<1`, and `n=log_2 N`, this is `2^{O(N^beta)}`. Thus the explicit description-indexed verifier is far above `N^(1+o(1))`.

The proposed quotient is to merge descriptions that compute the same restriction on each address block, then reuse the block-check state across all descriptions in that class. This saves local evaluation work but loses the global witness identity: after two histories merge, a later block may use a restriction supplied by a different circuit. The resulting table is an independent block hybrid, not necessarily in `SIZE(s2)`. This is exactly the coherence condition in C-229.

## Gate-level semantic quotient test

If the quotient state records the exact truth-table function of each candidate subcircuit of size at most t, then it must distinguish all such functions that matter to future gate compositions. Even at small t, sparse-indicator functions give `2^{Theta(t)}` distinct restrictions on a shattered coordinate family (C-212); with t growing as a positive power of N, one-state-per-function storage is superpolynomial and cannot meet `N^(1+o(1))`. This lower bound is only against the proposed explicit semantic-state table. It does not rule out a more algebraic representation that shares many different gate functions without naming each one.

Canonicalizing the *whole* circuit by its output function also does not solve the recognition task. A canonical label is useful only after the input table has been checked against all N output bits, and the verifier still has to ensure that the same latent circuit generates every address. Enumerating canonical labels pays `|SIZE(s1)|`; forgetting the label gives the same cross-description splice as above.

## Block recursion test

For R independent address blocks, selecting a size-s1 circuit independently on each block costs a mux of `R s1+O(R log R)` gates. Since `s2=Theta(n s1)`, soundness allows only `R=O(n)` such independent choices. A trivial base for arbitrary table pieces requires `R=N^(1-beta+o(1))`, so independent cofactor recursion cannot reach it. This reproduces and sharpens the exact soundness-budget obstruction C-265; recursive levels do not help because their leaf-choice counts multiply.

## Route disposition

This kills three concrete implementations only:

1. enumerate circuit descriptions and verify all addresses;
2. merge descriptions by local block restrictions but allow independent later witnesses;
3. recursively split into independent size-s1 cofactors until the leaves become arbitrary.

The surviving upper-bound question is whether there is a compact **global** semantic object that represents the set of all circuit descriptions and their simultaneous outputs without enumerating descriptions or permitting cross-description hybrids. No such object is constructed. No `N^(1+o(1))` cover is found, and the actual lower bound remains `q=N-o(N)`.

## Research-state links

The description-coherence obstruction is C-229; the independent-cofactor budget is C-265; fixed-menu restrictions are C-222; mandatory equality and parity calibrations are C-258 and C-257. This report provides a route filter, not a new lower bound.
