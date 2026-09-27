# C-254 — Partial-support hazard boundary

Date: 27 September 2026  
Route: test whether C-253's profile-fibre localization strengthens on the monotone lattice of partial table assignments.  
Status: exact hazard-cylinder lemma proved; the chain argument does not charge q.

## 1. Partial activation semantics

A consistent support `C` is a partial assignment to table coordinates. Define `A_j(C)=1` if some finite proof rooted at state j has all its signed seed literals in C. This is monotone in C. On a complete table x, `A_j(ell(x))` agrees with the C-74/C-75 least-fixed-point activation predicate.

Using the C-252 conflict relation G and seed/state incidence set S, call C hazardous if either

- `A_j(C)=A_k(C)=1` for some `(j,k) in G`, or
- `A_j(C)=1` and `(ell,b) in C` for some `(j,ell,b) in S.

## 2. Theorem: every hazardous partial support is a low-only cylinder

If C is hazardous, every complete table extending C belongs to `SIZE(s2)`. Consequently,

\[
2^{N-|\mathrm{dom}(C)|}\le |\mathrm{SIZE}(s_2)|,
\qquad
|\mathrm{dom}(C)|\ge N-\log_2|\mathrm{SIZE}(s_2)|.
\]

### Proof

If C activates a conflict pair `(j,k) in G`, then every completion preserves the finite proof supports witnessing both activations. The corresponding empty output root has j and k as opposite-side predecessors, so it activates on every completion. If C activates a state j and fixes an incident seed literal `(ell,b)`, every completion preserves both the state proof and the direct seed at the root defining that incidence; that empty output root also activates. Soundness places all such completions in `SIZE(s2)`. The cylinder has `2^(N-|dom(C)|)` tables, giving the bound. \(\square\)

For every low complete table w, C-252 ensures `ell(w)` is hazardous. Since hazard is monotone under adding matching literals, along any chain that reveals the coordinates of w in any order, the first hazardous prefix has at least `N-log2|SIZE(s2)|` fixed coordinates. This recovers the near-full certificate width as a boundary-location statement for the profile readout.

## 3. A corrected witness-support charge, and its ceiling

Counting state-on events alone does not locate the first hazardous prefix: it may be the final raw marker literal that completes an active-state/literal incidence. But the C-252 readout gives a separate, valid support-size bound. Choose a readout term witnessing that a low table w is accepted. If the term is an edge `(j,k) in G`, choose finite least-rank activation proofs for j and k. If it is an incidence `(j,ell,b) in S`, choose a least-rank proof for j and include the marker literal `(ell,b)`. In the union of these proof DAGs, ranks strictly decrease along predecessor edges. There are at most q distinct state labels, and each visited state needs at most one witness for each of its two sides. The support therefore contains at most 2q seed literals, plus at most one readout marker literal. It is a consistent hazardous support C contained in ell(w).

Combining this with the hazard-cylinder theorem gives

\[
N-\log_2|\mathrm{SIZE}(s_2)|\le |\mathrm{dom}(C)|\le 2q+1,
\qquad
q\ge \frac{N-\log_2|\mathrm{SIZE}(s_2)|-1}{2}.
\]

This is a legitimate linear lower bound from the conflict readout and its witness DAG. It does not improve the project's existing `q >= N-o(N)` certificate floor. In particular, the earlier claim that the first-hazard argument itself yielded no q-bound was too strong; the corrected bound comes from compressing a *selected readout witness*, not from counting activation events on an arbitrary coordinate-order chain. A single activated state need not have a short support independent of q: the general bound here is at most 2q seed literals for a selected finite witness.

Nor does averaging over coordinate orders improve the bound directly. A state may have many incomparable minimal supports, and different low inputs may postpone its activation to different ranks; the C-252 forbidden-pattern condition constrains the union cylinders only after a hazard occurs. The selected-witness bound above recovers at most a linear q floor, while the existing C-03/C-243 certificate-width result is stronger.

## 4. What would be needed next

A useful strengthening would aggregate selected witness-DAG supports for the same state or state pair across many low anchors, while controlling how their supports overlap and how raw marker literals are charged. No such aggregation theorem is obtained here; the partial-assignment route gives no superlinear state bound.

C-254 proves no near-linear full-promise cover and no P-vs-NP separation.

## 5. Magnification side-route check

For a truth table on n input bits, changing h entries of a circuit-computed table can be implemented by adding h point-indicator circuits, at O(n) gates each. Hence if s1<s2 and z is outside SIZE(s2), then its Hamming distance from SIZE(s1) is greater than (s2-s1)/O(n). With table length N=2^n and s2=N^alpha, this is a fraction N^{-(1-alpha)}/polylog(N).

Thus, for any eta>1-alpha, the exact Gap-MCSP NO set is contained in the eta-approximate-MCSP NO set for the same low set (the approximate promise asks to reject every table at distance at least N^{-eta}). A circuit for the approximate promise would solve the exact gap promise, so an exact-gap circuit lower bound transfers to that stronger approximate problem.

This does not finish the target. Atserias?Muller (2025), Theorems 9 and 11, turn suitable approximate sparse-problem lower bounds into NP not subset NC1, or a uniform separation P != NP^oplusP, respectively; neither conclusion alone is P != NP. The route would require a matching formula/uniform-circuit lower bound plus an additional bridge to the requested separation. Do not substitute these endpoints for the P-vs-NP objective. Source: https://arxiv.org/html/2503.24061.

