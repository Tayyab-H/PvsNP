# C-249 — Bi-blocked output-root normal form

Date: 27 September 2026  
Route: O-153, strengthen the high-blocker analysis at accepting roots.  
Status: proved root normalization and a fixed-witness escape law for the actual dense high side; no q lower bound.

## 1. Dense high-side premise

Write

\[
Y=\mathrm{SIZE}(s_1),\qquad U=\{0,1\}^N\setminus\mathrm{SIZE}(s_2).
\]

For the active OPS regime \(s_2=2^{\beta n}\), \(N=2^n\), and fixed \(0<\beta<1\), circuit counting gives

\[
|\mathrm{SIZE}(s_2)|\le 2^{O(s_2\log(s_2+n))}=2^{o(N)}.
\]

Every signed coordinate half-cube has size \(2^{N-1}\), so for all sufficiently large \(n\),

\[
U\cap\{z:z_k=b\}\ne\varnothing
\quad\text{for every }k\in[N],\ b\in\{0,1\}.
\]

In fact, \(|\mathrm{SIZE}(s_2)|<2^{N-2}\) gives the stronger two-coordinate shattering premise used in C-240. The one-coordinate consequence is enough for the normalization below.

## 2. Nondegenerate output-root lemma

Consider any successful q-state closure whose rule i has endpoints \(E_i,H_i\subseteq U\) and carrier \(T_i=E_i\cap H_i\). An output state has \(T_i=\varnothing\). On input \(w\), let \(\tau_i(w)\) be its least activation round.

**Lemma.** For every accepted low table \(w\in Y\), some active output state i of minimum activation rank among active output states has

\[
E_i\ne\varnothing\quad\text{and}\quad H_i\ne\varnothing.
\]

**Proof.** At round \(\tau_i(w)\), each side of i has a true source. If, say, \(E_i=\varnothing\), no literal seed can be that source: every matching high-side slice \(U\cap\{z:z_k=w_k\}\) is nonempty and therefore is not a subset of the empty endpoint. A predecessor source j would have \(T_j\subseteq E_i=\varnothing\), hence \(T_j=\varnothing\); it would be an active output state at a strictly earlier round, contrary to the choice of i. Thus \(E_i\ne\varnothing\); the same argument gives \(H_i\ne\varnothing\). Self-support cannot be an earlier witness because activation rank is strictly increasing along a proof edge. \(\square\)

Let \(O^+=\{i:T_i=\varnothing, E_i\ne\varnothing,H_i\ne\varnothing\}\). The lemma shows that deleting output roots outside \(O^+\) preserves completeness on Y; soundness is preserved because these are still empty-carrier states. Thus every successful cover has an equivalent output list in which each root has two nonempty, disjoint endpoint sets.

## 3. Each normalized root has both kinds of fixed high blocker

Fix \(i\in O^+\). Choose

\[
z_E\in E_i,\qquad z_H\in H_i.
\]

These are distinct high tables because \(E_i\cap H_i=\varnothing\). The table \(z_E\) blocks the entire H side of rule i: no H-side seed slice can be contained in \(H_i\), since that slice contains \(z_E\notin H_i\); and no predecessor carrier contained in \(H_i\) can contain \(z_E\). Symmetrically, \(z_H\) blocks the entire E side. Thus the semantic blocker set of every normalized output root contains at least one fixed witness of each side orientation.

This strengthens the generic statement “each high table blocks at least one side.” At each useful output root, both blocker orientations occur among actual high tables, and the witnesses \(z_E,z_H\) are independent of which low anchor uses that root.

## 4. Coupling with C-240: root-to-escape law

The high side U two-wise shatters coordinates in this parameter regime. C-240 therefore gives the following normal form for direct seed vocabularies at an empty root:

- if both sides have direct seed literals, they are exactly one complementary pair \((k,b),(k,1-b)\);
- otherwise at least one side has no direct seed literal.

Every finite accepting proof of an empty root must enter at least one predecessor carrier. In the complementary-literal case, the root's one coordinate chooses the mandatory escape side: if \(w_k=b\), an H predecessor is required; if \(w_k=1-b\), an E predecessor is required. In a seedless-side case, a predecessor on that side is mandatory for every accepted anchor.

The fixed witnesses from Section 3 turn this into a pair-space statement. If an accepted low \(w\) exits from root i through an H predecessor j, then \((w,z_E)\in R_j\), where the same \(z_E\in E_i\) blocks H for every such w. An E-predecessor exit gives \((w,z_H)\in R_j\). Thus each normalized root maps its low row set, by at most one direct seed coordinate and its predecessor edges, into lower-rank state rectangles paired with fixed high witnesses.

## 5. Why this still does not charge q

This normal form eliminates a degenerate case: a chosen accepting root cannot rely on an empty endpoint or on an empty seed slice in the actual dense high universe. It also pins down the first predecessor layer more tightly than an arbitrary high blocker map.

It does not bound the number of predecessor states or their row sets. One root may feed many states; one predecessor rectangle may serve many low anchors; and the same fixed high witness may be reused throughout the row. C-95/C-240's escape-source obstruction remains. The generic one-rule example from C-248 is also consistent with the lemma: its two endpoints are nonempty, but its high universe does not two-wise shatter coordinates and its root has many direct seed literals. Therefore the lemma does not smuggle an actual-promise lower bound out of that toy.

No superlinear q bound follows from “both endpoints nonempty,” from the two fixed blockers, or from the one-coordinate root selector. To get a q-charge, one must still show that the root-to-escape relation cannot cover all of \(\mathrm{SIZE}(s_1)\) with linearly many states while preserving the full cross-join safety of C-242/C-247.

## 6. Next test

For each normalized output root i, define its two fixed blocker columns \((z_E(i),z_H(i))\), its direct-seed selector (if present), and the first-predecessor row families on the mandatory escape sides. Seek a global charge on this root-to-escape incidence system. The theorem must use more than the number of roots, selector coordinates, or high witnesses: those are all at most O(q). It must couple the escape family to compatible context/proof joins or give an explicit full-promise near-linear construction. Preserve C-80/C-121/C-134/C-160/C-161/C-213 and C-228/C-234 as hostile checks.

No actual-promise superlinear fusion bound, near-linear cover, or P-vs-NP proof is established by C-249.
