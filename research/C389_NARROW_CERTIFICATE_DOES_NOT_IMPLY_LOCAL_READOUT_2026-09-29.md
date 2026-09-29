# C-389 - Narrow certificates do not imply a narrow-only readout

Date: 29 September 2026  
Route: test the inference from C-387 localization to a local-seed LFP by constructing an explicit feature-map/readout countermodel.  
Classification: **PROVED NON-IMPLICATION IN THE ABSTRACT MONOTONE SEED MODEL; ENDPOINT REALIZATION OPEN.**

## 1. The proposed inference

C-387 proves that many clauses selected in C-368 certificates are globally narrow and have few true literals at each Reed-Muller anchor. The tempting next step is to keep only those seed coordinates and set every globally wide seed coordinate to zero. Monotonicity guarantees that this modification preserves rejection of all high inputs: it only lowers the signature. The uncertain part is completeness: does the narrowed signature still activate the readout on the low anchors?

C-389 gives a minimal counterexample to that inference from certificate sparsity and monotonicity alone.

## 2. Feature-map countermodel

Take an abstract table input w in {0,1}^N. Give the readout these consistent seed clauses:

\[
A_i(w)=w_i\quad (i=1,\ldots,N),\qquad
B(w)=w_1\lor\cdots\lor w_N.
\]

The A_i are width-one clauses; B has width N. Define the monotone decoder

\[
G(a_1,\ldots,a_N,b)=b\land\bigwedge_{i=1}^N a_i.
\]

The induced predicate is

\[
G(A_1(w),\ldots,A_N(w),B(w))=1
\quad\Longleftrightarrow\quad
w=1^N.
\]

Thus it separates the abstract promise with low set {1^N} and high set {0,1}^N minus {1^N}.

At f=1^N, the minimal true seed set in signature space contains all N+1 coordinates: omitting any a_i or b makes G zero on that 0/1 signature. Its seed-CNF is

\[
\left(\bigwedge_{i=1}^N w_i\right)\land
\left(\bigvee_{i=1}^N w_i\right),
\]

whose model set is exactly {1^N}. The N narrow clauses each have one f-true literal; the wide clause has N f-true literals. Hence the certificate has a near-full family of sparse narrow clauses, yet its minimal monotone seed certificate still requires the wide seed coordinate.

If B is forced to zero, the readout rejects f. The high rejection is preserved, but low completeness is lost. This shows precisely why C-387's clause localization does not by itself produce a local-only decoder. In this example B is logically redundant in the table-space CNF after all A_i are imposed, but remains essential to G on the abstract signature cube. C-368's minimality is in seed-signature space, so that distinction matters.

## 3. Transfer boundary

Every seed predicate in the example is an OR of consistent signed table literals, and G is a simple monotone function. However, this is only a countermodel to the implication from C-368/C-370 plus monotonicity. It is **not** claimed to be a valid C-319 endpoint list for the actual high universe: C-319 couples each seed predicate to the same endpoint sets that determine consequences and predecessor containment. No endpoint realization or actual Gap-MCSP promise is supplied here.

So the example does not show that wide features are essential in every native cover, nor that they are essential in some actual native cover. It shows that a local-seed reduction requires a genuinely new endpoint-sensitive argument; it cannot be inferred from per-anchor sparse certificates alone.

## 4. Next proof obligation

For an actual C-319 list Q, let J be the global narrow seed positions and define the truncated readout by evaluating G_Q with all coordinates outside J set to zero. It is automatically sound on high tables by monotonicity. Prove that it still accepts a sufficiently rich low family (or all of SIZE(s1)); otherwise identify an endpoint-realizable cover where it fails. Any construction in the relaxed monotone game model is only a hostile calibration until the joint endpoint/seed/predecessor constraints are realized.

Checkpoint: C-387 remains a proved localization theorem, but q is still N-o(N). No full-promise cover, superlinear lower bound, or P-vs-NP proof follows from this countermodel.
