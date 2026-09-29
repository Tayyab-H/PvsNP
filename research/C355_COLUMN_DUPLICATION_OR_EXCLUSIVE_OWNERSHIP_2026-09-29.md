# C-355 - A proof either duplicates a column core or exposes an exclusive owner block

Date: 29 September 2026  
Route: strengthen C-350 for the one-suffix family in C-354 by tracking leaf-occurrence ancestry, not only support width.  
Classification: **EXACT PROOF-TREE DICHOTOMY + LARGE LOW CODE CALIBRATION; NO q IMPROVEMENT.**

## 1. Column-relative duplication/ownership dichotomy

Let `C0={(p,u0):p in {0,1}^m}` be the varying column in C-354, with `r=2^m` coordinates. Let `Pi` be any finite accepting proof tree for an anchor `z_mu`, and let S be its output support. Soundness says every completion of S is in `SIZE(s2)`, so at most `kappa_square(s2)` coordinates of S are free. Therefore

```text
M = |Var(S) intersect C0| >= r-kappa_square(s2).
```

For each column coordinate a in `Var(S)`, consider all its leaf occurrences in Pi and let `lca(a)` be their lowest common ancestor. For a tree node v, put

```text
mass(v) = |{a in C0 : lca(a) lies in the subtree rooted at v}|.
dup(v)  = |{a in C0 : lca(a)=v}|.
```

Coordinates counted by `dup(v)` for an internal rule node occur in both child proof subtrees. Every supported column coordinate has exactly one LCA, so the node masses partition the M coordinates.

**Dichotomy.** For sufficiently large M, at least one of the following holds:

1. (**Duplicated core**) Some rule occurrence v has `dup(v) >= M/4`. At least M/4 column coordinates are used with the same anchor sign in both side subproofs of this occurrence.
2. (**Exclusive owner cut**) Some state occurrence has a replacement proof P and outside context K such that
   ```text
   M/8 < |(Var(P) minus Var(K)) intersect C0| <= M/2,
   |Var(K) intersect C0| >= M/2.
   ```

**Proof.** If case 1 fails, every node has `dup(v)<M/4`. Start at the proof root, whose mass is M, and follow a child of maximum mass while that child has mass greater than M/2. This process terminates. At the last node v, `mass(v)>M/2` and both child masses are at most M/2. Since

```text
mass(v) = dup(v) + mass(left(v)) + mass(right(v)),
```

the two child masses sum to more than M/4, so the larger child has mass greater than M/8 and at most M/2. Call this child subtree P. A variable whose LCA lies in P has all its occurrences inside P and is absent from the outside context K; these are exactly the variables of P that are not in K. Every supported variable whose LCA lies outside P has an occurrence outside P, so it appears in K. Hence the displayed owner and context counts follow. Since `M/8>1` for large M, P is rooted at a rule state, not a seed leaf. QED.

This repairs one gap in C-350: if the tree has no large duplicated core, the balanced cut has a genuinely nonempty, linear-size owner mask on the critical column. The alternative is explicit: large support overlap must be concentrated at some rule occurrence.

## 2. It applies to all accepted low masks in the slice

For fixed sufficiently small beta, there is a family F of `2^(Omega(s1))` functions `mu:{0,1}^m->{0,1}` such that every `z_mu` is in `SIZE(s1)` and distinct masks have Hamming distance

```text
Delta >= 2^(m-d) >> kappa_square(s2).
```

One construction is the binary Reed-Muller code `RM(d,m)`. It has dimension `D=sum_{j=0}^d binomial(m,j)` and minimum distance `2^(m-d)`. A degree-at-most-d polynomial has an O(D)-size De Morgan circuit: compute all degree-at-most-d monomials once using a shared conjunction DAG, then XOR the selected monomials using O(D) gates. Choose d maximal so this circuit cost is at most `s1/2`; the extra O(n) gates for the suffix equality test then keep every `z_mu` in `SIZE(s1)`. For fixed small beta, `D=Theta_beta(s1)` and `d/m` is a small positive constant. Then `|F|=2^D`, and `(1-beta)(1-d/m)>beta` ensures `Delta/kappa_square(s2)->infinity`.

Choosing one accepting proof per `z_mu` and applying the dichotomy assigns every codeword either to a state with an exclusive owner cut or to a rule occurrence with a duplicated core. Refining the second case by its two child-state labels gives at most `q^3` buckets; the first has at most q buckets. Thus some state or fixed parent/child triple is assigned at least `|F|/(2q^3)` codewords. For any polynomial q this is still superpolynomially many masks.

## 3. Why the dichotomy is not yet a state lower bound

The high-distance code and the large bucket do not ensure a compatible cross-anchor splice. In the exclusive-owner case, contexts for different masks may fix opposite signs on the other's owner set, making every cross-pair inconsistent. In the duplicated-core case, the two children may likewise disagree across anchors and block substitution. Full supports are the extreme example: they keep cross-anchor pairs incompatible regardless of family size.

The code family also does not force a `kappa_square(s2)`-scale owner cube by cardinality. The low family has logarithmic size `Theta(s1)`, while the sound size-s2 mask class has logarithmic size `O(s2 log s2)=O(s1 n^2)` at these parameters. Thus the state bucket can contain many low anchors while still lying far below the number of safe masks allowed by soundness. The missing charge must quantify how the q-rule grammar realizes the sign-conflict pattern or the duplicated cores across this large bucket.

## 4. Updated proof target

For a large state/triple bucket from Section 2, prove one of:

- many compatible cross-anchor joins whose owner masks contain a high-complexity prefix codeword or a forbidden C-320 splice; or
- a lower bound on rules needed to maintain pairwise conflicts on the duplicated/owned column coordinates while covering all low codewords.

This is a concrete refinement of O-210. It preserves C-258's linear equality calibration: there, the grammar may realize the conflict alternative cheaply on the repeated-block subpromise. The actual full-promise lower bound remains `N-o(N)`; C-355 proves no superlinear q bound and constructs no full-promise cover.

## 5. Post-hoc calibration of the chosen Reed-Muller family (C-358)

The specific family used above has an O(N)-size membership circuit: compute the algebraic-normal-form coefficients of the one-suffix column by the fast Boolean Möbius transform, check that every coefficient above degree d vanishes, and check that the other N-r table bits are zero. Its size is O(N+r log r)=O(N). The accepted family lies in `SIZE(s1)`, so C-109 converts this separator into an O(N)-rule native cover against the actual high set. Thus this Reed-Muller bucket cannot itself yield a q lower bound. C-355's tree dichotomy remains valid, but the code-family application is retired as a lower-bound route; see `research/C358_REED_MULLER_BUCKET_HAS_LINEAR_NATIVE_SUBPROMISE_COVER_2026-09-29.md`.
