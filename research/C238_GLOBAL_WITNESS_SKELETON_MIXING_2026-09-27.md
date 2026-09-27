# C-238 — Cross-mixing whole witness skeletons

Date: 27 September 2026  
Scope: strengthen single-occurrence splicing to a global product across a full ranked activation strategy. If two tables admit the same acyclic witness topology, the E-side seed witnesses from one and H-side witnesses from the other combine into a valid proof DAG. The result is exact but its immediate topology-counting route fails at the active q scales.

## 1. Ranked witness skeleton

Fix a q-rule closure. For a table x accepted at an output rule, the least-fixed-point ranks yield a finite proof DAG with at most one vertex per activated rule state. At each vertex i and each side S in {E,H}, choose one witness:

- a seed label lambda in the rule's S seed set with lambda in Lambda(x); or
- a predecessor state j in the S predecessor set with rank(j)<rank(i).

The predecessor choices form an acyclic graph. Forget the identities of seed labels but retain the active state set and every chosen predecessor edge or seed-slot marker. Call this the witness skeleton tau. A realization of tau on x fills each seed slot by a true signed literal.

## 2. Global cross-mixing proposition

Suppose x and y are accepted, and both have realizations of the same witness skeleton tau, with seed fillings a_x and a_y. Form a mixed support

    S_EH(x,y) = {E-side seed labels chosen by a_x}
                 union {H-side seed labels chosen by a_y}.

Keep the common predecessor edges of tau. If S_EH(x,y) is consistent, then it is the support of a finite accepting proof DAG: prove states in reverse topological order; each E obligation uses x's selected witness and each H obligation uses y's. Therefore every table z with S_EH(x,y) subset Lambda(z) is accepted. For a sound Gap-MCSP closure,

    Q(S_EH(x,y)) subset SIZE(s2).

The reverse mix S_HE(x,y), using H witnesses from x and E witnesses from y, obeys the same conclusion whenever consistent. This is a global product law across all state occurrences in the skeleton, not a single-node substitution. It needs the common predecessor topology; equality of active-state sets alone is insufficient because mixing different predecessor edges can create cycles.

## 3. Relation to the selector profile

For repeated anchors w_g,w_h, if the mixed support above is consistent, its canonical completion is a source-selecting hybrid on the coordinates where g and h differ. By C-236, that hybrid must be in SIZE(s2), so the induced disagreement mask belongs to L_{g,h}. Thus each shared skeleton induces an E-seed/H-seed product whose compatible mask image is restricted to at most |SIZE(s2)| profiles.

The proposition avoids having to select one particular occurrence path in an unfolded proof tree. It also makes the relevant global object explicit: a closure assigns low anchors to ranked witness skeletons, and each skeleton has two families of seed fillings whose cross-products must remain low or rail-inconsistent.

## 4. Topology count and the first failed implication

For a fixed q-rule list, a crude count of skeletons is at most

    q * 2^q * (q+1)^(2q) = 2^(O(q log q)),

by choosing an output root, an active state subset, and for each side either a seed slot or one of at most q predecessor states. This ignores acyclicity and so is a valid upper bound.

At the target frontier q is already at least linear in N, while the repeated-anchor family has only 2^(Theta(s2)) members with s2=N^beta=o(N). The skeleton count is vastly larger than the anchor family, so pigeonholing anchors into one skeleton gives no information. A small q does not force two low tables to share a witness topology by counting alone. Counting proof trees is even weaker because a q-state cyclic grammar can have exponentially many unfoldings.

The next useful route is therefore not raw skeleton counting. One would need a structural restriction on the skeletons realizable by one fixed rule list, or a direct theorem that a skeleton class large enough to cover all low circuits has a dangerous E/H cross-product. Conversely, an upper-bound construction could try to encode a circuit description in a witness skeleton; it must still make all N truth-table checks use the same description. This is precisely the synchronization issue from C-229.

## 5. Hostile checks and status

- **C-228:** isolated positives may have disjoint singleton certificates; common skeleton cross-products need not generate any nonmember.
- **C-234 equality cover:** repeated-block anchors can share a scan skeleton whose compatible mixtures stay diagonal and low.
- **C-235/C-236:** every compatible mixed support is an interval/cylinder inside SIZE(s2), and its disagreement selector lies in the safe mask family.
- **C-237:** the safe mask family contains Theta(s2 n)-dimensional cubes, so this global product does not improve the local width threshold by itself.

**Proved:** common-skeleton E/H cross-mixing yields an accepted support whenever consistent; the soundness and selector consequences follow. **Not proved:** any q-dependent limit on the number/structure of skeletons, a superlinear fusion lower bound, a near-linear full-promise cover, or P != NP.
