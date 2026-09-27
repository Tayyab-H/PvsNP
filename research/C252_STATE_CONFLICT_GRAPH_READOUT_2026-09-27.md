# C-252 — State-conflict graph readout normal form

Date: 27 September 2026  
Route: O-153, aggregate the C-251 one-sided/paired support signatures by their root predecessor states.  
Status: exact global readout theorem proved; its direct circuit transfer matches, but does not improve, the existing quadratic unrolling bound.

## 1. State activation predicates

Fix a sound q-state C-74/C-75 closure on N-bit tables. Let `Y = SIZE(s1)`, `L = SIZE(s2)`, and `U = {0,1}^N \ L`. For each state `j in [q]`, let

\[
A_j=\{x:\text{state }j\text{ is active on }x\}
\]

under the least fixed point. Every activation has a finite proof. By C-243, if `z in U intersect A_j`, then `z in T_j = E_j intersect H_j`.

For every empty-carrier output root `i`, define its predecessor sets

\[
P_i=\{j:T_j\subseteq E_i\},\qquad R_i=\{k:T_k\subseteq H_i\}.
\]

Let `G` be the union of `P_i x R_i` over empty roots i. Let `S` contain each triple `(j, ell, b)` for which an empty output root has direct seed `U intersect {z : z_ell = b} subset E_i` and `j in R_i`, or has that seed on its H side and `j in P_i`.

## 2. Theorem: conflict/readout factorisation

Define the Boolean readout

\[
F(x)=\bigvee_{(j,k)\in G}(A_j(x)\land A_k(x))
\;\lor\;
\bigvee_{(j,\ell,b)\in S}(A_j(x)\land[x_\ell=b]).
\]

Then

\[
Y\subseteq\{x:F(x)=1\}\subseteq L.
\]

Moreover, G has at most q^2 ordered pairs. Since S is a set of triples (state, coordinate, polarity), it has at most 2qN incidences. Thus this depth-two readout has at most q^2+2qN terms; in the OPS regime q=Omega(N), this is O(q^2).

### Proof

**Every readout term is high-free.** Suppose (j,k) in P_i x R_i for an empty root i and a high table z activates both j and k. C-243 puts z in T_j subset E_i and T_k subset H_i, contradicting E_i intersect H_i = T_i = empty. Hence A_j intersect A_k subset L.

Suppose instead `(j, ell, b) in S` comes from a seed on the E side and an H-side predecessor j. A high table z with `z_ell = b` lies in the seed half-cube and therefore in `E_i`; if it also activates j, C-243 gives z in `T_j subset H_i`, again a contradiction. The H-seed case is symmetric. Every disjunct of F is therefore contained in L.

**Every accepted low table triggers a term.** Fix w in Y, and choose a normalized empty output root i active on w, as in C-249. In the fixed-point recurrence, each of the E and H side tests has a witness: either a matching direct seed literal or an active predecessor in P_i or R_i. C-240's two-coordinate shattering excludes simultaneous matching direct seeds on both sides. If both witnesses are predecessors j,k, then (j,k) in G and F(w)=1. If one witness is a matching seed and the other a predecessor j, then (j,ell,b) in S and again F(w)=1. At least one predecessor is required at an empty root, so these cases exhaust the possibilities. Thus Y subset F^{-1}(1). QED.

## 3. Conflict-graph interpretation

Make a left and right copy of the q state vertices, with an edge `j_L k_R` for every pair in G. For any high table, the active-state profile contains no such edge: it is a bipartite independent set. In addition, a high table cannot activate a state and simultaneously match a literal incidence in S. Every low table's profile either contains a conflict edge or has an active-state/literal incidence.

This quotient aggregates exponentially many proof supports into at most `q^2` state-pair interactions. It makes the global cross-root object finite and explicit: low tables violate a high-side independence condition on the activation profile, with literal-labeled exceptions for direct seeds.

## 4. Exact limitation

The readout is not a new separation by itself. The A_j are the original cyclic least-fixed-point predicates, not independent inputs. Unrolling them for q rounds costs O(q^2) unbounded-fan-in gates. The readout has q^2+2qN terms, which is O(q^2) in the relevant OPS range q=Omega(N), matching rather than improving C-248's gate-count scale. Nor does the fact that high activation profiles are independent sets bound how many truth tables share one profile: a profile fibre may be large, and no fibre-size or VC-dimension theorem follows from the graph alone.

The new proof obligation is now sharper: exploit the *joint geometry of the activation fibres and the conflict graph* for the actual low/high circuit promise. Candidate target: show that a q-state least-fixed-point map whose high fibres avoid all conflict and seed incidences cannot cover all of Y unless q is superlinear, or construct a near-linear cover. The graph edge count, independent-set count, and depth-two readout size alone do not do this.

No superlinear state lower bound, near-linear full-promise cover, or P-vs-NP proof follows from C-252.

## 5. Literature calibration

Cavalar and Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems* (2025), prove the exact identity between fusion cover complexity and cyclic intersection complexity in their general finite discrete setting (Theorem 3). This confirms that the C-74/C-75 closure is not a heuristic surrogate: it is an exact form of the target cover method. C-252's state-conflict graph is a derived readout normal form inside that framework, not a new complexity measure or transfer theorem. Their graph-complexity objects are input-set/rectangle constructions; do not identify them with this q-vertex state-conflict graph. The paper's general characterization and graph results do not supply the missing quantitative lower bound for the actual Gap-MCSP promise. Source: https://arxiv.org/abs/2503.14117.

