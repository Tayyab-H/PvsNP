# C-227 — Native certificate grammar and the exact splice law

Date: 27 September 2026  
Scope: begin the new global-sharing/readout programme from the exact fusion recurrence. This proves the certificate grammar and a necessary condition for safe splicing. It does not prove that a small cover is spliceable into a high-complexity table.

## 1. Native seed grammar

Fix a q-rule list and its C-67/C-75 recurrence. Let

\[
\Lambda=[N]\times\{0,1\},\qquad \ell(x)=\{(k,x_k):k\in[N]\}.
\]

For each rule i and side S in {E,H}, let \(I_i^S\subseteq\Lambda\) be the seed labels whose matching slices lie in that endpoint, and let \(D_i^S\subseteq[q]\) be the predecessor states whose carriers lie in it. On a table x, the side predicate is

\[
P_i^S(x)=\bigvee_{\lambda\in I_i^S}[\lambda\in\ell(x)]\ \vee\ \bigvee_{j\in D_i^S}x_j(x),
\qquad x_i=P_i^E\wedge P_i^H
\]

with the least fixed point taken from the all-zero state vector.

A finite proof tree rooted at state i is defined recursively: at the i-node choose, independently for each side S, either a seed label \(\lambda\in I_i^S\), making it a leaf, or a predecessor \(j\in D_i^S\), attaching a proof tree rooted at j. Its support \(\mathrm{supp}(D)\subseteq\Lambda\) is the set of seed labels at its leaves. Repeated labels are kept only once.

**Exactness.** State i activates on x if and only if there is a finite proof tree D rooted at i with \(\mathrm{supp}(D)\subseteq\ell(x)\). Forward direction follows by induction on the first activation round: each of the two satisfied side disjunctions supplies either a true seed leaf or an earlier active predecessor. Reverse direction follows by induction on tree height. Therefore cycles in the fixed rule graph cause no circular proof: only finite, rank-decreasing unfoldings witness the least fixed point.

Let \(\mathcal S_i\) be all supports of finite proof trees rooted at i and let

\[
\mathcal C_i=\min_{\subseteq}\mathcal S_i
\]

be its inclusion-minimal certificate antichain. For each side define

\[
\mathcal A_i^S=\{\{\lambda\}:\lambda\in I_i^S\}\ \cup\ \bigcup_{j\in D_i^S}\mathcal C_j.
\]

Then the exact grammar is

\[
\boxed{\mathcal C_i=\min_{\subseteq}\{a\cup b:a\in\mathcal A_i^E,\ b\in\mathcal A_i^H\}.}
\]

For the output family \(O\) of empty-carrier states,

\[
\mathcal C_{\rm out}=\min_{\subseteq}\bigcup_{i\in O}\mathcal C_i,
\qquad h_Q(x)=1\iff (\exists C\in\mathcal C_{\rm out})\ C\subseteq\ell(x).
\]

This is the desired explicit interpretation: each rule takes the pairwise union-product of its E- and H-side proof supports; alternatives are union of families; cycles permit recursive reuse but only finite proof trees contribute to the least fixed point. The antichains can be enormous, so this is a semantic normal form, not an efficient enumeration algorithm.

## 2. What reuse *does* force

The local E/H product law is exact: every E-side support a and every H-side support b combine into the valid state-i proof support \(a\cup b\). They need not have come from the same accepting derivation. A second exact operation is proof-tree substitution. If an accepting proof D contains an occurrence of state i, remove that occurrence's subtree and replace it by any other finite proof D' rooted at i. The resulting tree is a valid accepting proof, with support

\[
K\cup C',
\]

where K is the leaf support of D outside the removed occurrence and \(C'=\mathrm{supp}(D')\). This is the native closure analogue of context substitution at a shared DAG node. It is unconditional at the proof-syntax level; it does not say that the new support is satisfiable by a truth table.

The same-state Boolean function is also monotone in the *unconstrained* dual-rail seed vector. Hence if an arbitrary seed vector activates i, every coordinatewise larger vector activates i. This is not a useful table-level join law: legal table vectors \(\ell(x)\) are one-hot on each coordinate, and \(\ell(x)\vee\ell(y)\) generally contains both signs and is not any table.

This gives a precise context/subproof product at every state i. Let \(\mathcal K_i\) contain every outside-context leaf support K from an accepting proof having a chosen occurrence of i, and let \(\mathcal S_i\) contain every leaf support C of a finite proof rooted at i. Then

\[
\boxed{K\in\mathcal K_i,\ C\in\mathcal S_i\quad\Longrightarrow\quad K\cup C\in\mathcal S_{\rm out}.}
\]

The quantifiers are genuinely cross-context: K and C can come from unrelated low-table derivations. This is stronger and more useful than saying that two derivations happen to share i. It also exposes the missing invariant: a successful cover must make every pair in this context/subproof product either rail-inconsistent or nearly full-coordinate.

## 3. Exact splice-soundness condition

Call a support C **consistent** if it contains at most one of (k,0),(k,1) for every k. Its table cylinder is

\[
\mathrm{Cyl}(C)=\{x:C\subseteq\ell(x)\}.
\]

For any successful Gap-MCSP cover, every accepted table is outside the high set Z. Therefore every consistent output-proof support C obeys

\[
|\mathrm{Cyl}(C)|=2^{N-r(C)}\le M_2,
\qquad r(C)=|\{k:(k,b)\in C\text{ for some }b\}|,
\]

and consequently

\[
\boxed{r(C)\ge N-\log_2 M_2.}
\]

This recovers the C-221-A wide-certificate floor directly for every proof tree, including every splice. Now take two accepting derivations D,D' sharing a state occurrence i. Substitution yields an accepted hybrid whenever its support K union C' is consistent. If it is consistent, the hybrid fixes all but at most \(\log_2 M_2\) truth-table coordinates. If the union is inconsistent, the formal proof splice has no table model. These are the two exact obstructions to turning “shared state” into a high-table contradiction:

1. opposite rails collide in the mixed context/subproof support; or
2. the splice remains consistent but fixes at least \(N-\log_2 M_2\) coordinates, leaving a cylinder small enough to contain only non-high tables.

Thus the new theorem target is concrete: force a pair of derivations and a shared occurrence whose substituted supports are consistent and whose union fixes fewer than \(N-\log_2 M_2\) distinct coordinates. That immediately gives a high table accepted by the cover. Merely proving that two derivations share a state does not.

At an empty-output root i, the context is empty, so there is an especially concrete cross-product test. Let \(\mathcal A_i^E\) and \(\mathcal A_i^H\) be all finite side-support families for the two endpoints (including predecessor proofs). Every pair \((a,b)\in\mathcal A_i^E\times\mathcal A_i^H\) is itself an output certificate. Hence every consistent pair must jointly pin at least \(N-\log_2M_2\) coordinates. Every low table routed through root i has some such pair with \(a\cup b\subseteq\ell(w)\). This is a native product-hull condition on side supports, not merely on the selected pairings seen in individual proofs. A lower-bound attack can now study, root by root, whether a small recursive grammar can encode all low tables while every cross-pair of side supports is contradictory or nearly full-coordinate.

## 4. Why the current step is not yet a global lower bound

The number of low tables is too small in logarithmic terms. A ranked proof DAG has at most q rule vertices and 2q side obligations, but its tree unfolding can be exponential. Pigeonholing state names across tables does not control which occurrence/context is shared, whether the cross-support is consistent, or how many distinct coordinates the splice fixes. The antichain \(\mathcal C_i\) records minimal supports but discards the occurrence context K needed for substitution. Any useful global potential must therefore track triples

\[
(i,\ \text{context support }K,\ \text{state-i subproof support }C)
\]

or a compressed semantic equivalent, and must bound both opposite-rail conflicts and coordinate footprint. Simply counting \(\mathcal C_i\), its widths, or state visits repeats known insufficient arguments.

## 5. Calibration: near-full-cube relay toy

The open solver logs are finite-model calibrations, not evidence about Gap-MCSP. For anchors of weight at most n-2 and the n+1-point universe consisting of the all-ones vector and its n single-zero neighbors, the independent cut-cover construction uses \(\lceil\log_2 n\rceil\) rules. The existing search encoded arbitrary endpoints and all anchors, with the first-seed normal form. The recorded UNSAT instances include n=7, q=1,2 under full S_n symmetry (90,075/443,008 and 176,044/891,437 variables/clauses respectively), and n=8, q=1,2 without symmetry breaking (7,479/35,132 and 20,919/91,435). This is consistent with the explicit logarithmic upper bound and warns against using anchor abundance or a small high universe alone as a sharing lower bound. The CNF results are limited to these instances and their stated encoding; they do not establish a scalable theorem.

## 6. Next proof work

1. The support families \(\mathcal K_i,\mathcal S_i\) and the output-root side cross-product are now explicit; find a compressed semantic state invariant for them.
2. Search for an OPS-specific low-circuit subfamily on which every small q-state grammar forces a context/subproof pair with a consistent, low-footprint splice.
3. Attack both sides of the compatibility condition: prove conflict/near-full footprint is unavoidable, or construct a compact cover that exploits it.
4. Keep the near-linear cover search live. C-229's direct circuit-description grammar loses global witness identity when states are shared; look for a semantic quotient of partial circuit descriptions. Any lower-bound potential must survive C-228 and C-80/C-121/C-134/C-160/C-161/C-213, plus the one-anchor/fractional-cover ceilings.

**Status:** exact certificate grammar and splice-soundness criterion proved from the C-67 recurrence. No forced splice for the actual low-circuit class, no superlinear \(\rho\) bound, and no P-vs-NP proof obtained.

## C-230 clarification: the exact safe-splice threshold

The bound `r(C)>=N-log2(M2)` above is a valid coarse consequence of counting. For the sharp semantic condition, let `kappa_square(s2)` be the maximum dimension of a full truth-table subcube contained in SIZE(s2). Then every consistent certificate must satisfy `N-r(C)<=kappa_square(s2)`, and a splice contradicts soundness once it leaves more than kappa_square coordinates free. By C-230, this parameter is Theta(s2 log s2) for fixed-beta OPS scales. Use kappa_square in the strongest formulation of O-151.
