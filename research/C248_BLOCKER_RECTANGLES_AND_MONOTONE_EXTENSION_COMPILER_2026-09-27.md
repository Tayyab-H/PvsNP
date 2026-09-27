# C-248 — Blocker rectangles and a quadratic monotone-extension compiler

Date: 27 September 2026  
Route: O-153, exact coupling of high-side blockers to global state sharing.  
Status: proved semantic rectangle decomposition and an unbounded-fan-in compiler; no superlinear fusion lower bound or P-vs-NP proof.

## 1. Setup

Use the C-242 least-fixed-point recurrence on the signed seed alphabet

\[
\Lambda=[N]\times\{0,1\}.
\]

For a seed set \(X\subseteq\Lambda\), let \(a_i^S(X,t)\) be the disjunction of the seeds in side \(S\in\{E,H\}\) present in \(X\) and the predecessor states on that side active by round \(t\). Then

\[
x_i^{(0)}(X)=0,\qquad
x_i^{(t+1)}(X)=a_i^E(X,t)\wedge a_i^H(X,t).
\]

There are \(q\) states and a set \(O\) of empty-carrier output states. On a legal table \(w\in\{0,1\}^N\), write

\[
\ell(w)=\{(k,w_k):k\in[N]\}.
\]

Let \(Y=\mathrm{SIZE}(s_1)\) and \(Z=\{0,1\}^N\setminus\mathrm{SIZE}(s_2)\). A successful closure has an active output state on every \(w\in Y\), and no active output state on any \(z\in Z\).

## 2. Every state induces a rectangle in the low/high pair space

For state \(i\), define its semantic row and column sets

\[
A_i=\{w\in Y:i\text{ is active on }\ell(w)\},\qquad
B_i=\{z\in Z:i\text{ is inactive on }\ell(z)\},
\]

and its pair rectangle \(R_i=A_i\times B_i\subseteq Y\times Z\).

This factorization is exact because state activity is a predicate of one table at a time. In particular it gives the native product-hull law:

\[
(w,z),(w',z')\in R_i
\quad\Longrightarrow\quad
(w,z'),(w',z)\in R_i.
\]

For every low/high pair, some output state is active on the low table and inactive on the high table. Thus

\[
Y\times Z=\bigcup_{i\in O}R_i.
\]

Every high table is inactive at every output state, so each output rectangle has the common column set \(Z\); only its low row set varies.

## 3. Exact blocker decomposition of a state rectangle

For a signed seed \(\lambda=(k,b)\), define the mismatch rectangle

\[
M_\lambda=\{w\in Y:w_k=b\}\times\{z\in Z:z_k=1-b\}.
\]

For each \((w,z)\in R_i\), the state \(i\) is active on \(w\) and inactive on \(z\). Since inactivity means at least one of its two sides fails on \(z\), choose such a blocked side \(S\). The same side has a witness on \(w\), because \(i\) is active there. If the witness is a seed \(\lambda\), then \((w,z)\in M_\lambda\). If it is a predecessor state \(j\), then \(j\) is active on \(w\) and inactive on \(z\), so \((w,z)\in R_j\). Therefore

\[
R_i\subseteq
\bigcup_{S\in\{E,H\}}
\left(
 \bigcup_{\lambda\in I_i^S}M_\lambda
 \;\cup\;
 \bigcup_{j\in D_i^S}R_j
\right),
\]

where \(I_i^S\) and \(D_i^S\) are the seed and predecessor supports on side \(S\).

Following predecessor rectangles terminates after at most \(q\) steps: on the low table, each selected predecessor was active strictly earlier than the state it witnesses. A terminal seed rectangle is a genuine signed mismatch. This is the blocker-path lemma expressed as a recursive rectangle cover.

This gives a direct native sharing statement: reuse of state \(i\) automatically shares the *whole* rectangle \(A_i\times B_i\), including all cross-pairs. A proof cannot treat two visits to \(i\) as unrelated pair-specific events. This sharpens the object O-153 should charge, but it does not yet bound how much of \(Y\times Z\) one state rectangle can cover while its recursive exits remain safe.

## 4. A quadratic compiler to unbounded-fan-in monotone circuits

The least closure stabilizes after at most \(q\) strict state additions. Unroll the recurrence for exactly \(q\) rounds. For each round \(t\), state \(i\), and side \(S\), create one unbounded-fan-in OR gate for

\[
\bigvee_{\lambda\in I_i^S}X_\lambda
\;\vee\;
\bigvee_{j\in D_i^S}x_j^{(t)},
\]

then one AND gate combining the two sides for \(x_i^{(t+1)}\). The final output is the OR of the output-state signals at round \(q\). Constants handle empty ORs.

This is a monotone circuit on the \(2N\) signed-seed variables. It has at most

\[
3q^2+1
\]

gates when **unbounded-fan-in gates are charged by gate count and their input wires are not charged**. On legal encodings \(\ell(w)\), its output is 1 for every \(w\in Y\) and 0 for every \(z\in Z\). Thus it is a monotone extension of the actual Gap-MCSP promise.

Let \(\mathrm{MExt}_{\infty}(Y,Z)\) be the minimum gate count of such an unbounded-fan-in monotone extension over the signed encoding. Every successful \(q\)-state closure proves

\[
\mathrm{MExt}_{\infty}(Y,Z)\le 3q^2+1,
\qquad
q\ge \sqrt{(\mathrm{MExt}_{\infty}(Y,Z)-1)/3}.
\]

This is an exact one-way transfer. A lower bound \(\mathrm{MExt}_{\infty}>N^{2+2\varepsilon+\delta}\) would imply \(q>N^{1+\varepsilon}\) for fixed \(\delta>0\) and all sufficiently large \(N\), up to constants.

### Cost-model boundary

The compiler has up to

\[
O\!\left(q^2(N+q)\right)
\]

gate-input incidences, since each of the \(q\) rounds repeats the seed and predecessor lists for all \(q\) states. At the live regime \(q\ge N-o(N)\), this is \(O(q^3)\). Therefore this does **not** improve the standard bounded-fan-in / wire-sensitive compiler, and it must not be cited as an \(O(q^2)\)-size ordinary Boolean circuit. It identifies a lower-bound target in a different, explicitly defined model.

The converse is not established: an arbitrary monotone extension circuit need not obey the fusion rule-incidence syntax or be realizable as a native closure with comparable \(q\).

## 5. Why the rectangle identity alone does not prove a lower bound

Every disjoint promise \(Y,Z\subseteq\{0,1\}^N\) has the trivial signed-mismatch cover

\[
Y\times Z=\bigcup_{k\in[N],\ b\in\{0,1\}}M_{(k,b)}.
\]

Consequently, neither the fact that each \(R_i\) is a rectangle, nor rectangle area, nor the number of possible terminal mismatch labels yields a superlinear charge. The hard part is the recursive *two-sided routing*: one fixed collection of state rectangles must factor every cross-pair and route it through legal seed/predecessor supports, with the same least-fixed-point semantics on each individual table.

There is also a one-state native counterexample to rectangle-area arguments (this is only a generic promise calibration, not the actual Gap-MCSP promise). Take

\[
Y=\{0,1\}^N\setminus\{0^N,1^N\},\qquad Z=\{0^N,1^N\}.
\]

Use one rule with endpoints \(E=\{1^N\}\) and \(H=\{0^N\}\). For a mixed table \(w\), choose \(k_1,k_0\) with \(w_{k_1}=1\) and \(w_{k_0}=0\). Its matching high-side slices are \(L_{w,k_1}=\{1^N\}\subseteq E\) and \(L_{w,k_0}=\{0^N\}\subseteq H\), so the rule derives the empty intersection. On \(0^N\), no seed enters E; on \(1^N\), no seed enters H, so both promised high tables are rejected. Thus \(q=1\) while \(R_1=Y\times Z\) contains almost every low/high pair. For \(z=0^N\), the blocker route exits on a 1-coordinate of \(w\); for \(z=1^N\), it exits on a 0-coordinate. The cross-pair law mixes *pairs* \((w,z)\), not pieces of the two truth tables into a new hybrid table. Hence even a huge shared rectangle does not itself force a dangerous splice.

The existing hostile calibrations survive unchanged:

- C-80/C-121/C-134/C-160/C-161/C-213 prevent a generic pairwise mismatch or state-count charge from exceeding the easy O(N)-scale cases.
- C-228 has many easy anchors and expensive readout without forcing a dangerous splice.
- C-234's diagonal equality cover keeps cross-block joins safe by fingerprinting the repeated description.
- C-247's product-entropy budget remains only \(O(s_2n)=o(N)\); the rectangle decomposition supplies no missing q-sensitive aggregation.
- C-230's safe-cylinder bound and C-246's certificate-count ceiling are not improved.

So the exact product-hull law is a cleaner statement of the needed global sharing invariant, not yet an invariant with a quantitative q lower bound.

## 6. Literature boundary

Austrin and Risse prove SoS proof-size lower bounds for MCSP and analogous results for minimum monotone circuit size of monotone Boolean slice functions. The signed encodings \(\ell(w)\) do lie on one Hamming slice. Indeed, from any monotone extension \(F_Q\), one can define a monotone slice function that agrees with \(F_Q\) on weight-\(N\) inputs, is 0 below that slice, and 1 above it; threshold gates can enforce those outside values. But the Austrin–Risse theorem lower-bounds the **SoS refutation size** of claims that particular slice functions have small circuits. It does not lower-bound the circuit size of an arbitrary promise separator or yield a contradiction from the existence of \(F_Q\). A transfer would need to turn a small native closure/readout into a sufficiently small SoS refutation of a hard circuit-size claim, and no such map is known here. [Austrin–Risse, CCC 2023](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2023.31); [paper definition and monotone-slice results](https://drops.dagstuhl.de/storage/00lipics/lipics-vol264-ccc2023/LIPIcs.CCC.2023.31/LIPIcs.CCC.2023.31.pdf).

Hardness magnification gives conditional motivation for a strong small-model bound on Gap-MCSP, but its cited theorem concerns ordinary bounded-fan-in circuit lower bounds at a different quantitative threshold; it is not a transfer for \(\mathrm{MExt}_{\infty}\). [Oliveira–Pich–Santhanam, *Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/).

## 7. Next exact obligation

The native route is now phrased as a recursive rectangle system with these constraints:

1. the output rectangles cover all of \(Y\times Z\);
2. each state rectangle has the full cross-product property;
3. every rectangle is covered by its rule's legal mismatch exits and predecessor rectangles;
4. every pairwise route terminates by low-side activation rank;
5. all rectangles come from one shared q-rule list, whose incidence vocabulary is only \(O(qN+q^2)\).

Prove that these five conditions force \(q>N g(N)\) for some unbounded \(g\), or construct a near-linear family satisfying them for the full actual promise. Area, ordinary biclique-cover number, path length, and total incidence counts alone do not meet that obligation. The first targeted experiment should classify when many high columns can share one state rectangle without forcing unsafe mixed low truth-table endpoints; it must pass the diagonal equality cover and the easy O(N) promise tests before any asymptotic claim is made.

No superlinear \(q\) lower bound, near-linear actual-promise cover, or P-vs-NP proof follows from C-248.
