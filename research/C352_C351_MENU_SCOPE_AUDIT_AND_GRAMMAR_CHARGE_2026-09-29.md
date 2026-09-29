# C-352 - C-351 does not bound an arbitrary replacement menu

Date: 29 September 2026  
Route: audit the proposed C-351 to C-336 state-capacity step against the exact quantifiers.  
Classification: **SCOPE CORRECTION; NO q LOWER BOUND.**

## 1. The quantifiers in C-351

Fix a one-hole context support `K` for state `i`, let

```text
R = [N] minus Var(K),
O_a = R minus Var(P_a),
kappa = kappa_square(s2),
```

and let each `P_a` be a proof support for state `i` matched by a low anchor `w_a`, with `K union P_a` consistent. Soundness gives `|O_a| <= kappa`. If, in addition, `P_a union P_b` is consistent, then every disagreement of `w_a,w_b` on `R` must be omitted by at least one support, so

```text
dist(w_a restricted to R, w_b restricted to R) <= |O_a union O_b| <= 2*kappa.
```

The second premise is essential. Individual compatibility with `K` does not imply compatibility between two replacements.

## 2. Why a multi-hole product does not supply that premise

For holes `1,...,h`, let `P_(j,a)` be alternatives at hole `j`. A Cartesian product is usable when each selected tuple satisfies

```text
K union P_(1,a1) union ... union P_(h,ah)
```

is consistent. This constrains supports chosen at **different holes** in one tuple. It never places two alternatives from the same hole into one tuple. Therefore it does not imply

```text
P_(j,a) union P_(j,b) is consistent
```

for alternatives `a,b` at one fixed hole. C-351 cannot bound the size or projected diameter of that same-hole menu merely from the existence of a multi-hole product.

There is one special case: if the same state label occurs at two independently replaceable holes and a proposed product explicitly includes every cross-pair of a common menu, then those cross-pairs are compatible by the product premise. C-351 can be applied to that pairwise-compatible family relative to a fixed context. This is conditional on the repeated-state/product structure and gives no bound on how many such contexts the grammar can generate.

The coordinatewise compatibility rule is exact. For a hole menu `M_j` and coordinate `t`, let `V_j(t)` be the set of signs 0 or 1 that occur in some support in `M_j`. A complete product across distinct holes is compatible only if, for every `j != k`, no opposite signs occur in `V_j(t)` and `V_k(t)`. Thus one hole may have arbitrary internal conflicts; across holes, all mentioned signs must agree. The product premise separates conflicts by hole but does not limit the menu inside a single part.

## 3. Exact geometry-only counterexample

Let `F` be any finite family of distinct low tables, with each `w` in `SIZE(s1)` and `s1 <= s2`. Take the empty context and, for each `w`, the complete signed support

```text
P_w = ell(w) = {(a,w_a): a in [N]}.
```

Each support cylinder is the singleton `{w}`, hence is contained in `SIZE(s2)`. For distinct tables `u,v`, `P_u union P_v` contains opposite literals at a differing coordinate and is inconsistent. Thus the context has `|F|` individually sound replacement cylinders, while no two replacements satisfy C-351's mutual-consistency premise. The projected-diameter statement is vacuous for this menu, regardless of its size.

This is a counterexample to a **geometry-only capacity inference** for arbitrary F. It is not a construction of a small full-promise C-319 cover. There is, however, a real restricted-family calibration: for `Rep_(d,r)`, C-258 gives a native cover with `q=2N+2d-1`, and C-326 computes the exact output predicate

```text
AND_j ( OR_(a in {0,1}) AND_t [w_(j,t)=a] ).
```

On a diagonal anchor, each accepting proof chooses its repeated value `a` for each block and includes the literal at every copy. Its support is exactly `ell(w)`, so distinct anchors have pairwise-incompatible complete supports. Thus a linear native grammar generates this menu on that subpromise. A capacity theorem must use the obligation to cover all of `SIZE(s1)`, not menu geometry alone.

## 4. Corrected frontier

C-351 remains a valid exact constraint on compatible replacement pairs. C-352 rules out using it as a general bound on same-hole menu size or as an automatic consequence of C-336. The grammar itself is already characterized: C-245 gives the marked proof/context antichain recurrences, and C-260 gives the certificate/blocker dual and compatible-join law. The missing theorem is quantitative: charge the joint generation of those proof/context joins and blocker maps, or give a sound full-promise near-linear cover. Merely recounting supports, contexts, or their pairwise conflicts does not do this: an endpoint's seed family can be an arbitrary disjunction of table literals, and repeated anchor-specific cylinders are allowed by soundness. C-353 integrates this correction with the repeated-block fingerprint route.

The target checkpoint is unchanged: `rho_GapMCSP = N-o(N)` is the recorded lower bound; no superlinear bound, full-promise near-linear cover, positive transfer margin, or P-vs-NP proof has been obtained.

## 5. Required checkpoint

1. Actual Gap-MCSP lower bound improved beyond `N-o(N)`: **No**.  
2. Valid near-linear full-promise cover constructed: **No**.  
3. State-sensitive synchronization theorem for the exact C-319 game: **No**.  
4. Positive CohEnc transfer margin constructed: **No**.  
5. General reconstruction-to-decision compiler proved: **No**.

The next phase remains the exact support-language generation problem in Q209/O-209. C-352 is a quantifier correction and a route filter, not a breakthrough.
