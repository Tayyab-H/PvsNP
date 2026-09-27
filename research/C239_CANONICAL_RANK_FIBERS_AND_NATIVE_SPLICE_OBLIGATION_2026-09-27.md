# C-239 — Canonical rank fibers and the native splice obligation

Date: 27 September 2026  
Scope: continue the native cyclic-closure programme from C-227/C-238. The result is a canonical witness skeleton for each two-sided support-rank profile and an exact state-local compatibility/coverage obligation. A proof audit shows that the state activation-rank vector alone is insufficient; after correction, the profile count is still too large for a lower bound.

## 1. Canonical ranks and witnesses

For state i, side S in {E,H}, let `I_i^S` be matching signed-literal seeds and `D_i^S` its predecessor states. For anchor x, let `tau_i(x)` be the first least-fixed-point activation round, or infinity. Put

```text
alpha_i^S(x) = min( {0 : some literal in I_i^S is true on x}
                    union {tau_j(x) : j in D_i^S} ),
```

where the minimum of an empty set is infinity. The exact rank equation from C-233 is

```text
tau_i(x) = 1 + max(alpha_i^E(x), alpha_i^H(x)),
```

with `1+infinity=infinity`.

For each active i and side S, choose a deterministic witness: if `alpha_i^S=0`, mark a seed slot; otherwise choose the least-index j in `D_i^S` with `tau_j=alpha_i^S` and mark edge i→j. Every chosen edge strictly decreases rank. Choose the least-index active empty-carrier rule as root.

**Canonical side-rank-skeleton theorem.** The augmented profile `alpha(x)=(alpha_i^E(x),alpha_i^H(x))_{i=1}^q` determines the selected root, active states, predecessor edges, and seed-slot markers. Therefore two accepted anchors with the same side-rank profile have the same acyclic skeleton. If x supplies every E-side seed slot and y supplies every H-side seed slot, and the mixed support is consistent, reverse-topological induction proves an accepting proof DAG. Its entire support cylinder is accepted and soundness puts it in `SIZE(s2)`. The reverse E/H mix also works when consistent.

The activation-rank vector alone does **not** determine this skeleton. Here is a two-rule endpoint-realizable counterexample in the actual closure semantics. Let `N>=4`, let x be `0^N`, let y have bit 3 equal to 1 and all other bits 0, and set `U={0,1}^N minus {x,y}`. Put `L_(k,b)=U intersect {z:z_k=b}`. Define `E_1=L_(1,0)`, `H_1=L_(2,0)`, and `T_1=E_1 intersect H_1`; x and y activate state 1 at rank 1. Now define `E_2=T_1 union L_(3,0)`, `H_2=T_1`, so `T_2=T_1`. On x, the E side of state 2 has a rank-0 seed because `L_(3,0)` matches; on y it has no matching seed and uses predecessor 1 at rank 1. The H side uses predecessor 1 at rank 1 on both. Thus `tau(x)=tau(y)=(1,2)` but their E-side witness topologies differ.

To check the seed claims, U deletes only two points, so all coordinate half-slices are nonempty. For each coordinate k, the slice matching y has a point outside `E_2`: if k=1 choose z_2=z_3=1; if k=2 choose z_1=z_3=1; if k=3 choose z_1=z_2=1; if k>=4 choose z_1=z_2=z_3=1 and z_k=0. These choices can be completed to a point of U matching y at k and lying outside both T_1 and L_(3,0). Thus no y-matching seed lies in E_2. No x- or y-matching half-slice is contained in H_2=T_1 either: for k=1 or 2 set the other of bits 1,2 to 1; for k>=3 set bits 1 and 2 to 1. State 1 is therefore the only rank-1 support for both sides of state 2 on y and for its H side on x. This pair list is not a successful cover; it shows that the recurrence and endpoint geometry alone do not let tau determine the skeleton.

The valid global product law is therefore indexed by a common side-rank profile (or, more generally, any common witness skeleton), not by an activation-rank fiber alone. The counterexample is not a successful Gap-MCSP cover, so it does not rule out additional restrictions from global success; no such restriction has been proved.

## 2. Count audit: canonicalization does not improve the exponent

For a fixed rule list Q, every side-rank profile is a deterministic function of the seed signature `sigma(x)=(a_i(x),b_i(x))_{i=1}^q`, because the predecessor graph is fixed and the least-fixed-point ranks are uniquely determined by those 2q Boolean inputs. Thus the rank-canonical convention partitions anchors into at most `2^(2q)` fibers, each with one selected skeleton. This counts only the canonical skeletons selected by this rule, not all possible witness topologies counted in C-238. It is a recurrence-specific cover of the accepting anchors, but it still gives no pigeonhole at the active q>=N−o(N) scale: `2^(2q)` is much larger than the `2^(Theta(s2))` repeated-anchor family for fixed OPS beta<1. The failed activation-rank-only count would have been `(q+1)^q`, but the endpoint-realizable example above shows it does not index a canonical skeleton.

The miss is localized: a q-state recurrence might induce many distinct profiles on its low anchors. For the repeated family `w_g(p,u)=g(u)` with `2^k=Theta(s2)`, the seed vocabulary itself can distinguish every g using one signed-literal predicate per suffix input u; since q is already at least N−o(N), the available 2q seed predicates exceed this `Theta(s2)` description dimension. This is only a seed-signature observation, not a construction of a successful pair list: endpoint containment and empty-root soundness remain decisive. It does show that a profile-pigeonhole proof must use those geometric constraints, not just the number of low descriptions. Progress now needs either a restriction on rank profiles realizable by one legal endpoint-containment system, or a direct q-sensitive theorem for the compatible E/H products within fibers.

## 3. Exact state semantic obligation

Use C-227 notation: `K_i` is the family of outside-context supports obtained by marking an occurrence of i in a finite accepting proof; `P_i` is the family of finite proof supports rooted at i. Substitution gives an output proof on support `K union C` for every `K in K_i`, `C in P_i`.

For consistent support A, let `dom(A)` be its fixed coordinates and `free(A)` the coordinates in `[N]` outside `dom(A)`. Let `kappa=kappa_square(s2)`, the largest dimension of a full subcube inside `SIZE(s2)` (C-230). Soundness implies the exact conflict-or-cover law

```text
for every K in K_i and C in P_i:
    either K union C is rail-inconsistent,
    or |free(K) intersect free(C)| <= kappa.
```

When the union is consistent, its cylinder is accepted and contained in `SIZE(s2)`; its free coordinates are exactly the displayed intersection. Equivalently, for every coordinate set J of size `kappa+1`, no compatible context/proof pair can both leave all of J free.

This is a precise semantic obligation for a reused state. It does not yet bound q: compatible cross-families can avoid a dangerous join through rail conflicts or coordinate coverage, and no known extremal argument charges this avoidance to the number of closure states.

## 4. Near-linear cover attempt: residual descriptions

Tried partitioning the truth-table address space into blocks. After checking blocks `B_1,...,B_t`, the correct residual object for table w is

```text
D_t(w) = { d : C_d has size s1 and agrees with w on B_1,...,B_t }.
```

Acceptance requires `D_N(w)` nonempty. Keeping d explicitly gives the known description-indexed grammar. Resetting the choice of d independently on each block admits blockwise hybrids whose pieces come from different circuits. A compressed construction must update residual description families while preserving their *joint nonemptiness*. No near-linear representation/update rule emerged; the naive description universe already has size `2^(O(s1 log(s1+n)))`, before residual subsets are represented.

This is a failed construction attempt, not an impossibility theorem. It sharpens C-229's synchronization obstruction. C-234 remains the hostile check: the diagonal repeated-block subpromise has an O(N) equality cover, so block coherence alone cannot prove hardness for the full promise.

## 5. Literature boundary

Austrin–Risse prove SoS degree/size lower bounds for MCSP encodings and an analogous monotone-circuit result for monotone slice functions, using CSP incidence expansion and local substitutions. This is a prompt for overlap-sensitive constructions, not a theorem about native fusion readout: the paper gives no transfer to this closure or to the actual `SIZE(s1)` versus `CC>s2` promise. Source: [CCC 2023 paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2023.31).

## 6. Status and next target

**Proved:** the two-sided min–max support-rank profile canonically determines a ranked witness skeleton; equal-side-rank accepted inputs obey C-238's whole-skeleton cross-product; every shared state obeys the C-227 conflict-or-cover condition with C-230's sharp subcube parameter.

**Failed:** the activation-rank vector alone does not determine the skeleton; the valid side-rank key yields at most `2^(2q)` canonical skeleton fibers, but this remains too large for anchor pigeonholing; the residual-description route has no compact update; generic block arguments fail the C-234 equality-cover check.

**Next theorem target:** exploit restrictions on seed-signature patterns imposed by legal endpoints, or prove a q-sensitive extremal theorem for context/proof families obeying conflict-or-cover. In parallel, seek a compact residual-description representation that preserves one globally consistent circuit. Keep the actual-promise near-linear-cover search active.

No superlinear fusion lower bound, near-linear full-promise cover, or P-vs-NP proof follows from C-239.

## 7. Artificial-model check: monotone clique promise misses the width regime

The clique-versus-complete-(k−1)-partite promise is a tempting global-sharing toy because its monotone circuit lower bounds quantify the cost of preserving one global witness (a k-clique) against many local obstructions. It does not meet the requested certificate calibration. A positive clique certificate fixes only `binom(k,2)` edge bits; its cylinder contains every supergraph of that clique, so it leaves `N-binom(k,2)` coordinates free and remains entirely on the YES side. The C-230/Gap-MCSP regime instead requires every accepting cylinder to have at most `kappa_square(s2)=o(N)` free coordinates. Making the toy exact by requiring all nonedges to be fixed introduces negative rails and removes the monotone-circuit lower-bound transfer. So this is a useful failed artificial model, not a candidate reduction.

Learning: a monotone lower bound alone does not supply the dense-high-side / narrow-safe-cylinder condition. Any artificial model intended to validate C-239 must preserve both properties simultaneously, or it will not test the obstruction relevant to Gap-MCSP. For the classical monotone clique lower-bound literature, see Razborov's primary paper: [1985 article](https://www.mathnet.ru/php/archive.phtml?jrnid=dan&option_lang=eng&paperid=9192&wshow=paper).
