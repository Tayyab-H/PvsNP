# C-350 - Every wide accepting support has a balanced state cut

Date: 29 September 2026  
Route: Q207; extract a state occurrence with substantial context and replacement supports from each accepting certificate.  
Classification: **EXACT STRUCTURAL LEMMA; NO STATE-CAPACITY BOUND YET.**

## 1. Certificate width supplied by soundness

Let `D` be a finite accepting proof tree for a low table `w`, with output support `S`. Write `m=|Var(S)|`. Every completion of `S` is accepted by the same output proof, so soundness implies

```text
Cube(S) subseteq SIZE(s2).
```

Consequently `N-m <= kappa_square(s2)`, where `kappa_square(s2)` is the maximum number of free coordinates in a subcube contained in `SIZE(s2)`. Thus `m >= N-kappa_square(s2)`. At the OPS parameters, C-230 gives `kappa_square(s2)=Theta(s2 log s2)=o(N)` for fixed `beta<1`.

## 2. Balanced-cut lemma

**Lemma.** If `m>=8`, every such proof tree has a marked state occurrence with context support `K` and replacement proof support `P` satisfying

```text
|Var(P)| in (m/4,m/2],       |Var(K)| >= m/2,
K union P = S.
```

In particular, both the context and replacement subproof mention `Omega(N)` coordinates at OPS scale.

**Proof.** Start at the output root, mark its whole subtree as the current replacement proof, and let `K` be the support of all leaves outside that subtree. Initially `Var(K)=empty` and the current subtree has all `m` variables. While the current subtree has more than `m/2` variables, inspect the two side subproofs of its root. Their variable sets have union equal to the current subtree's variable set. Follow the side with more variables; it contains at least half of the current set. The other side is added to the context. Stop at the first occurrence whose current subtree has at most `m/2` variables. Immediately before this step it had more than `m/2`, so the selected child has more than `m/4` variables. The outside context and the current subtree together have support exactly `S`; hence the context has at least `m-|Var(P)| >= m/2` variables. Since `m>=8`, the selected child is not a seed leaf, so the marked occurrence is a state. QED.

Choosing one accepting proof and one such occurrence for each table in a finite low family `F` assigns every table to one of the q states. Therefore some state is a balanced-cut occurrence for at least `|F|/q` anchors. This is an exact reuse statement with both sides large; it does not assume that the cover evaluates a circuit.

## 3. Why the lemma does not yet force a splice

The lemma controls `Var(K)` and `Var(P)`, but not their overlap. The owner mask is

```text
mu(K,P)=Var(P) minus Var(K),
```

and can still be empty even when both supports mention a linear fraction of all coordinates. Nor does balanced width imply that `K_u` is compatible with `P_v` for distinct anchors `u,v`. If compatible, C-281 says the entire joined cylinder is low; if incompatible, substitution yields no table. C-320 rules out owner masks near a common split and its complement, but the balanced-cut lemma gives no reason that a selected mask enters either ball.

There is a direct syntactic reason for the overlap problem. An internal rule may admit the same predecessor support family on both sides. A proof can then use two copies of a support `S`; cutting into one copy leaves the other copy in the context. At deeper cuts inside that copy, the context still contains all of `S`, so the owner mask can be empty even at a balanced state occurrence. This is consistent with the idempotent support product `S union S=S`; it does not itself give a complete sound cover, but it defeats any inference from balanced widths alone to a nontrivial mask.

The hostile constructions fit this result. C-257's parity grammar and C-258's repeated-block grammar both have linear-size covers and therefore have balanced cuts for many anchors; their algebraic/equality synchronization makes the resulting joins safe or incompatible. Thus a large balanced-cut load alone is not a lower bound.

There is a quantitative gap in trying to choose the C-320 split near one of these masks. For a fixed pair at distance `d_fg`, each hybrid is produced by `2^(N-d_fg)` masks, and at most `M(T)=|SIZE(T)|` hybrids are low. Hence the number of globally bad splits is bounded by

```text
K^2 * M(T) * 2^(N-d),
```

where `d` is the code's minimum distance. For any binary code of K words, the average pairwise distance is at most `N*K/(2(K-1))`, so `d<=N/2+o(N)` when K grows. With `T=N^gamma`, the displayed bound can be as large as `2^(N/2+o(N))`, whereas a radius-`Theta(N^gamma/n)` ball has only `2^(O(N^gamma))` masks. Thus the existing global union bound does not guarantee a good C-320 split inside a ball around a support-generated owner mask. This is a limitation of that argument, not evidence that every such ball is bad.

## 4. The remaining state-capacity obligation

For an explicit code family `F subseteq SIZE(s1)`, the desired next lemma is: if one state is a balanced cut for too many anchors in `F`, then some cross-pair of its context and replacement supports is compatible and has an owner mask in C-320's forbidden neighborhood. The parameter must charge the support *grammar* that generates these pairs, not merely support width, state reuse, or mask count. Alternatively, explicitly construct a q-state grammar that keeps every high table out while covering all low tables.

This lemma is only the extraction step for Q207. It produces no superlinear q lower bound, no full-promise near-linear cover, and no P-vs-NP proof. The proved lower bound remains `q >= N-o(N)`.
