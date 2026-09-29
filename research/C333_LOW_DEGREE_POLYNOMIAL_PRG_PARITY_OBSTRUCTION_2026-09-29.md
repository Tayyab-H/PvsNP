# C-333 — Low-degree polynomial truth tables fail as generic PRGs for the native game

Date: 29 September 2026  
Route: Q192 / instantiate an explicit low-circuit source for C-319.  
Classification: **EXACT GENERATOR ROUTE-KILL; PROMISE-SPECIFIC PRG QUESTION REMAINS OPEN.**

## 1. Candidate source

Write the `N=2^n` table coordinates as elements of `F=GF(2^n)`. Choose a uniformly random polynomial `p` of degree below `K` and output

```text
g_p(x) = Tr_{F/F_2}(p(x)),       x in F.
```

For any `K` distinct addresses, their field evaluations are independent uniform elements by the Vandermonde map; applying the nonzero linear trace preserves independent unbiased bits. Thus the output distribution is exactly `K`-wise independent.

For fixed coefficients, Horner evaluation uses `K-1` field multiplications and additions. Field multiplication has an `O(n^2)` Boolean circuit, so each output table has circuit complexity `O(K n^2)`. Taking `K=Theta(s1/n^2)` places every output in `SIZE(s1)` while keeping the seed length `Kn=Theta(s1/n)=N^(beta+o(1))<N` in the project regime.

## 2. Parity obstruction for generic readouts; endpoint caveat

The map from the `Kn` coefficient bits to the `N` output bits is linear over `F_2`. Its image is therefore a binary linear code of dimension at most `Kn<N`. There is a nonzero vector `a in F_2^N` orthogonal to every output, so

```text
Pr_p[ <a,g_p> = 0 ] = 1,
Pr_U[ <a,U> = 0 ] = 1/2.
```

The **abstract C-319 equation syntax** can compute parity with O(N) states. For selected coordinates `i=1,...,r`, let `u_i,v_i` denote even/odd prefix parity and let `ell_(i,b)=[w_i=b]`. Set `u_0=1,v_0=0` and

```text
u_i = (u_(i-1) AND ell_(i,0)) OR (v_(i-1) AND ell_(i,1))
v_i = (u_(i-1) AND ell_(i,1)) OR (v_(i-1) AND ell_(i,0)).
```

Each conjunction is one state with a predecessor on one side and the signed-literal seed on the other; each two-term OR is one state with both predecessor sets equal to the two term states. Two rails therefore use six states per coordinate. Two base states and one output root give at most `6r+3<=6N+3` states. Selecting the rail `a·w=0` distinguishes the polynomial source from uniform with advantage `1/2`. Thus a PRG theorem meant to fool every abstract positive alternating system of `q>=6N+3` states is impossible for this source. This construction establishes an abstract readout only; it does not construct legal endpoints over the actual OPS high-table universe.

C-257 independently gives a 4r-4-pair realization of parity on an artificial even/odd promise. That construction is a required hostile calibration, but its high universe is the odd-parity set, not the actual high-table universe `U= {z: CC(z)>s2}`. We have not shown that the abstract parity readout is realizable by endpoints over this actual U. In addition, parity is not a sound Gap-MCSP separator because it rejects many low circuits. Therefore this is a no-go only for a **generic** PRG against unrestricted abstract game readouts; it does not rule out a PRG theorem exploiting actual endpoint incidence and full-promise soundness.

## 3. Why the clause-wise argument does not rescue it

Each C-319 state has two consistent signed-literal seed clauses. A clause of width `r` is false on a uniform table with probability `2^-r`; under `K`-wise independence its false probability is also `2^-r` for `r<=K` and at most `2^-K` for `r>K`. Hence clauses wider than `R=ceil(log2(8q/epsilon))` may be replaced by true with total error at most `epsilon/4` under either source, by a union bound over `2q` clauses.

The remaining short clauses can jointly inspect as many as `min(N,2qR)` table coordinates. To make their entire truth vector exactly uniform by the standard k-wise-independence guarantee, independence order must reach this union size, not merely `R`. The polynomial source then has local circuit cost `O(min(N,2qR)n^2)`, which is `O(N n^2)` once `q=Theta(N)` and therefore exceeds `s1=N^(beta+o(1))`.

This joint-order requirement is real for the unrestricted game syntax: an acyclic q-state chain can make its root the conjunction of q seed features, so marginally uniform features do not determine the output distribution. Such a chain need not be a sound Gap-MCSP cover; it witnesses only why generic clause-wise fooling is insufficient.

## 4. Revised target and limits

The low-degree polynomial source is closed as a generic construction. Any next PRG attempt must either:

1. use nonlinear low-circuit outputs and prove they fool the relevant state games; or
2. exploit completeness and soundness of an actual Gap-MCSP separator to rule out parity-like and other generic distinguishers, then establish seed-profile indistinguishability specifically for sound separators.

The second route is close to the original native lower-bound problem and is not supplied by k-wise independence alone. No superlinear q lower bound, near-linear cover, positive CohEnc margin, or P-vs-NP proof follows. Actual `q=N-o(N)` is unchanged. Preserve C-257 parity as a mandatory hostile check for any future source.
