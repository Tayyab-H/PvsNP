# C-298 - Subgraph-lifted odd-cut consensus and its matching-fiber obstruction

Date: 28 September 2026

Classification: **NEW MONOTONE TEMPLATE / EXACT AFFINE ROUTE NO-GO.** This tests a way to remove the vacuous all-rails-on-YES behavior of C-294 while preserving high NO completions. The construction is monotone and NO-sound for arbitrary cut labels. For affine cut labels, it cannot cover all minimal YES inputs with high labels.

## 1. Setup

Use bipartite ODDFACTOR on sides L,R of size v, with edge set E(G). A cut class [T]={T,T^c}, |T| odd, is compatible with G when no present edge crosses it. Write

    C(G) = { [T] : E(G) intersect delta(T) = empty }.

ODDFACTOR(G)=0 exactly when C(G) is nonempty. Assign every cut class a table z_[T] outside SIZE(s2).

For coordinate j and bit b, define the lifted-consensus rail

    D_(j,b)(G)=1 iff there is an edge set H subseteq E(G)
                such that C(H) is nonempty and
                z_[T](j)=b for every [T] in C(H).

The quantifier over H is over subgraphs of the current input, not over supergraph completions.

## 2. Exact monotonicity and NO soundness

If G is a subgraph of G', any H witnessing D_(j,b)(G) also witnesses D_(j,b)(G'). Thus every rail is monotone.

If G is NO, then C(G) is nonempty. For every H subseteq G, C(G) is a subset of C(H): every cut un-crossed by G is also un-crossed by H. Hence, if D_(j,b)(G)=1, all cuts in C(G) have bit b. For any compatible T, the output at coordinate j therefore pins only z_[T](j). Consequently

    D(G) <= e(z_[T]) for every [T] in C(G),

and the NO high-completion condition holds.

The empty compatible-cut family on YES inputs causes no vacuous universal truth here: a YES rail is active only if some *subgraph* H has a nonempty compatible-cut family with a unanimous label.

## 3. Equivalent formula and its cost

For a cut class [T], let X_S(G)=OR_(e in S) x_e. The definition is equivalent to

    D_(j,b)(G)
      = OR over [T] with z_[T](j)=b
          AND over [T'] with z_[T'](j)=1-b
              X_(delta(T') minus delta(T))(G).

Indeed, from a unanimous subgraph H choose [T] in C(H). H avoids delta(T) and crosses every oppositely labelled T', so it contains an edge in delta(T') minus delta(T). Conversely, if the displayed term for T is true, take H=G minus delta(T); then T is compatible with H and every oppositely labelled cut is crossed by H.

This gives a direct AND-count upper bound of at most

    sum over j,b,[T]:z_[T](j)=b  max(0, |{[T']:z_[T'](j)=1-b}| - 1).

This bound is generally enormous; the semantic construction by itself has no useful cost guarantee.

## 4. Exact test on a minimal YES input

Let M be a perfect matching, regarded as its edge set, and put B_M(T)=delta(T) intersect M. The formula gives the following exact criterion:

    D_(j,b)(M)=1
    iff there is [T] with z_[T](j)=b such that for every oppositely
       labelled [T'], B_M(T') is not a subset of B_M(T).

Equivalently, starting from a cut T compatible with H, the matching must contain an edge that crosses each oppositely labelled T' but does not cross T.

A particularly strong obstruction follows. If oppositely labelled cuts T,T' have the same matching boundary B_M(T)=B_M(T'), then neither polarity can be produced from any H subseteq M: whenever H avoids delta(T), it also avoids delta(T'). Such a pair blocks every candidate cut in the formula with that boundary.

In fact the criterion reduces exactly to singleton-boundary fibers. If a candidate T activates rail b and e is any edge in B_M(T), then every cut U with B_M(U)={e} must also have label b; otherwise B_M(U) is an opposite-labelled subset of B_M(T), contradicting the criterion. Conversely, if all cuts with B_M(U)={e} have label b, choose the singleton cut U={u} for the left endpoint u of e. Its boundary is {e}; every odd cut boundary is nonempty, so no oppositely labelled cut has boundary contained in {e}. Thus

    D_(j,b)(M)=1 iff some e in M has z_[U](j)=b for every cut U with B_M(U)={e}.

The value on such a monochromatic fiber is necessarily the label of the singleton cut consisting of its left endpoint. This is a sharper nonlinear test than the lower-cone formulation: every coordinate needs at least one whole monochromatic fiber in every perfect matching.

## 5. Affine cut labels fail on all minimal YES inputs

Consider one coordinate labelled by

    z_[T](j) = c_j + |T intersect A_j| mod 2,

where |A_j| is even, so the label is invariant under replacing T by T^c.

If a matching M has an edge uv with exactly one endpoint in A_j, toggle both endpoints:

    T' = T symmetric-difference {u,v}.

Then T' is still odd, B_M(T')=B_M(T), and z_[T'](j)=1-z_[T](j). The equal-boundary obstruction above implies

    D_(j,0)(M)=D_(j,1)(M)=0.

If A_j is a union of whole matching pairs, the coordinate has at least one active rail on M. When A_j is empty the label is constant c_j. When A_j contains a matched pair uv, take T={u} and H=M minus {uv}. The odd cuts compatible with H have matching boundary exactly {uv}; since A_j is a union of pairs, they all receive label c_j+1.

Thus this affine coordinate has any active rail on M exactly when A_j is a union of pairs of M. A C-125 YES image must contain one rail at every coordinate for every perfect matching, so each A_j would have to be a union of pairs in **every** perfect matching of K_(v,v). Every nonempty proper vertex set has a crossing bipartite edge, and every edge extends to a perfect matching. Therefore only A_j=empty or A_j=V can pass this condition. In either case z_[T](j) is independent of T (for A_j=V, |T| is odd).

If all coordinates are of these two forms, every cut has the same fixed table R. The lifted-consensus map itself outputs exactly e(R) on every input, so it cannot supply a low YES table while using R as a high NO completion. If extra witness rails W are added and vanish on NO, then on NO the output remains e(R), while on every YES a low table w != R forces some opposite rail W_(j,1-R_j) to fire. The OR of all such rails computes ODDFACTOR with the map's AND cost. Hence the extra witness layer inherits the source decision hardness and gives no transfer margin.

This is an exact route-kill for the **affine-label lifted-consensus map itself**. If all its coordinates have collapsed to one fixed high table R, appending NO-vanishing witness rails does not help: their opposite-R OR separates YES from NO and inherits source hardness. This does not rule out a mixed construction where nontrivial affine consensus rails and witness rails jointly cover matching inputs, nor arbitrary nonlinear labels or C-125 maps. C-299 later closes the lifted-consensus map for nonlinear labels as well, but still leaves such general witness sidecars open.

## 6. Nonlinear frontier exposed by the exact criterion

For a nonlinear coordinate label z_j on odd cuts, every perfect matching M still requires at least one monochromatic lower cone:

    some odd S subseteq M such that z_j is constant on
    { [T] : B_M(T') subseteq S for the odd boundary B_M(T') }.

In particular, if every singleton-boundary fiber { [T] : B_M(T)={e} } is bichromatic, then no rail at that coordinate is active on M and no complete low table is possible there.

This gives a concrete nonlinear search filter. Random labels are unlikely to have such large monochromatic cones; structured labels must be checked against every perfect matching and against the finite-envelope decoders C-295/C-297. Even a label family passing the cone test still needs a low AND-cost implementation and high codewords for every cut.

## 7. Checkpoint and next obligation

C-298 supplies a monotone, NO-sound lift and an exact matching-input criterion, then rules out the affine family at the low-witness coverage step. It does not produce a useful CohEnc separation, change the actual fusion bound q=N-o(N), construct an N^(1+o(1)) cover, or prove P != NP.

The next sharply scoped question is whether a nonconstant Boolean labeling of odd cuts can have a monochromatic lower cone for every perfect matching while the N-coordinate label vectors remain high and admit a low-cost lifted map. Track this as O-174. Preserve C-258/C-281 and the low/high envelope decoders as hostile checks.

## References

- Cavalar, Goeos, Riazanov, Sofronova, and Sokolov, [Monotone Circuit Complexity of Matching, ECCC TR25-102](https://eccc.weizmann.ac.il/report/2025/102/revision/1/download), Theorem 2 (ODDFACTOR monotone hardness used as the source-side obstruction).
- Babai, Gal, and Wigderson, [Superpolynomial Lower Bounds for Monotone Span Programs](https://people.cs.uchicago.edu/~laci/papers/span1.pdf), for the linear GF(2) span-program representation and the span-program/monotone-circuit separation.
- Earlier cut-consensus and ODDFACTOR boundary analyses: C-288, C-294, and C-297.
