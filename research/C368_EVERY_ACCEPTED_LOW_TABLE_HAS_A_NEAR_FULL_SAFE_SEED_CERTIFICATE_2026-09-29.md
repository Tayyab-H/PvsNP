# C-368 - Every accepted low table has a near-full safe seed certificate

Date: 29 September 2026  
Route: derive a direct consequence of C-319 monotone seed-signature readout, then test whether it can charge state sharing.  
Classification: **EXACT CERTIFICATE-CONE LEMMA; LINEAR CERTIFICATE FLOOR; NO q IMPROVEMENT.**

## 1. Exact setup

For a fixed C-319 list \(Q\) with \(q\) state pairs, let

\[
\sigma_Q(w)=(A_1(w),B_1(w),\ldots,A_q(w),B_q(w))\in\{0,1\}^{2q}
\]

be the seed-signature vector. By the exact recurrence in C-319, there is a fixed monotone Boolean function \(G_Q\) such that

\[
\operatorname{Accept}_Q(w)=G_Q(\sigma_Q(w)).
\]

Each nonconstant coordinate of \(\sigma_Q\) is an OR of a consistent set of signed literals of the explicit truth table \(w\); an all-universe endpoint can instead give a constant-true coordinate.

## 2. Minimal true seed certificate

Fix any low table \(f\in\mathrm{SIZE}(s_1)\) accepted by \(Q\). Since \(G_Q(\sigma_Q(f))=1\), choose an inclusion-minimal set

\[
S_f\subseteq\{j:\sigma_Q(f)_j=1\}
\quad\text{such that}\quad
G_Q(\mathbf 1_{S_f})=1.
\]

Remove from \(S_f\) any constant-true seed coordinates, and let \(m_f\) be the number of remaining seed clauses. Define the CNF

\[
\Phi_f(w)=\bigwedge_{j\in S_f\text{ nonconstant}}\sigma_Q(w)_j.
\]

If \(\Phi_f(w)=1\), then every nonconstant coordinate selected in \(S_f\) is 1 on \(w\), and every removed constant coordinate is also 1. Thus \(\sigma_Q(w)\ge \mathbf 1_{S_f}\) coordinatewise. Monotonicity gives \(G_Q(\sigma_Q(w))=1\). Soundness of the cover therefore implies

\[
\{w:\Phi_f(w)=1\}\subseteq\mathrm{SIZE}(s_2).
\]

So each accepted low table has a *sound monotone certificate cone*: a satisfiable CNF made only from seed clauses, whose every satisfying completion has circuit size at most \(s_2\).

## 3. Counting the certificate clauses

Any satisfiable CNF with \(m\) clauses on \(N\) Boolean variables has at least \(2^{N-m}\) satisfying assignments. To see this, fix one satisfying assignment and choose one true literal from each clause. Fix the variables appearing among these at most \(m\) selected literals to their values in that assignment. Every clause remains true, leaving at least \(N-m\) variables free.

Apply this to \(\Phi_f\). Its satisfying set is contained in \(\mathrm{SIZE}(s_2)\), so

\[
2^{N-m_f}\le |\mathrm{SIZE}(s_2)|,
\]

and hence

\[
m_f\ge N-\log_2|\mathrm{SIZE}(s_2)|
=N-O(s_2\log(s_2+n))
=N-o(N).
\]

Because \(m_f\le 2q\), this independently gives \(q\ge \tfrac12N-o(N)\). The project already has the stronger native bound \(q\ge N-o(N)\), so this does not improve the numerical checkpoint.

## 4. What the lemma adds to the selector model

The conclusion is stronger than raw signature capacity: for every low table, not merely some accepted input, *any minimal monotone seed certificate that suffices for acceptance* must contain almost \(N\) nonconstant seed clauses. The graph cannot certify a low table through a short list of seed predicates and then let the remaining clauses be irrelevant.

This still does not give a superlinear state bound. A state pair supplies two seed coordinates, and a graph with \(q=\Theta(N)\) has enough coordinates to furnish a near-full certificate. Also, different anchors may use different large certificates, and the C-319 recurrence may share states among their derivations. The count does not say how many distinct certificates one state or one state pair can safely support.

The central follow-up is therefore a *state-sensitive certificate-sharing theorem*: if many low anchors' minimal certificates reuse the same root-free state sides, either the corresponding C-281 context/proof cross-products generate a C-320-forbidden high splice, or the rule graph pays additional states. Any such theorem must survive C-257 parity and C-258 repeated-equality covers. This is a sharpened formulation of the missing forcing step, not a proof that the forcing step holds.

## 5. Literature and transfer boundary

The result uses only the exact C-319 factorization and a CNF model-count argument. It does not extract a circuit description. The literature confirms that decision-to-search is a substantive gap for scalar MCSP; the formula search-to-decision theorem relies on tree-specific leaf weighting and does not automatically transfer to shared states. Multi-output search-to-decision is a different promise and does not repair the scalar gap without a parameter-preserving reduction; C-361 already rules out the direct output-index serialization.

Primary references: [Oliveira, Pich, and Santhanam, *Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/) for the exact Gap-MCSP magnification target; [Ilango, *The Minimum Formula Size Problem is (ETH) Hard*](https://epubs.siam.org/doi/10.1137/22M1481579) for the nonrelativizing formula search-to-decision result; [Ilango, Loff, and Oliveira, *NP-Hardness of Circuit Minimization for Multi-Output Functions*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2020.22) for the distinct multi-output setting.

## 6. Checkpoint

- A near-full safe seed certificate exists for each accepted low table: **proved**.
- Its width gives only \(q\ge N/2-o(N)\), weaker than the current \(N-o(N)\): **no q improvement**.
- A shared-state capacity bound or forced C-320 splice: **not proved**.
- A full-promise near-linear cover or a P-vs-NP proof: **not obtained**.

The actual native lower bound remains \(\rho_{\mathrm{GapMCSP}}\ge N-o(N)\).
