# C-229 — Universal-circuit certificate grammar: where near-linear sharing fails

Date: 27 September 2026  
Scope: attempt the opposite-direction construction required by the new research priority. This identifies the exact synchronization problem in the direct low-circuit witness grammar; it gives neither a near-linear cover nor a lower bound.

## Desired Boolean specification

For a truth table w, Gap-MCSP low membership has the witness form

\[
\exists d\in\mathcal D_{s_1}\quad\forall k\in[N],\quad w_k=C_d(x_k),
\]

where \(d\) describes a circuit of size at most \(s_1\), and \(x_k\) is the address of table coordinate k. In positive proof-grammar notation this is

\[
\bigvee_{d\in\mathcal D_{s_1}}\ \bigwedge_{k=1}^N [w_k=C_d(x_k)].
\]

Every accepting derivation can choose one d and then expose N signed table literals. Implementing each description separately gives the familiar O(N times number-of-descriptions) construction; a direct pairwise-intersection chain realizes it, but it is exponentially larger than the target.

## Proposed sharing and its failure point

The natural compression is to share coordinate-check states across descriptions, or to use a universal-circuit evaluator once for many d. The proof grammar's AND node combines E- and H-side supports independently. If two descriptions d,d' reach a shared state, the grammar also generates cross-combinations of their side supports. Those supports need not correspond to one common description. Unless the mixed support either has opposing table literals or confines every extension to SIZE(s2), the closure accepts a hybrid table with no verified low-circuit witness.

Adding d to the state label prevents that mix but restores description-indexed copies. Removing d from the state label saves states but drops the global witness-coherence condition. A canonical representative per low truth table would not solve this by itself: one still must compile the adaptive map from w to its representative and keep that selection consistent across all N coordinate checks.

This diagnosis is exact for this construction attempt, but it is not an impossibility theorem. A different proof grammar might synchronize descriptions implicitly through carriers or seed geometry. C-227 gives the precise audit for any such proposal: examine every context-support/replacement-support cross-product, then prove each consistent union has no high extension.

## Near-linear target and next viable question

A useful construction would compile the existential description and all N checks with q=O(N polylog N) native rules while preserving a single shared d across the checks. The direct verifier has N times description-size evaluation cost in ordinary circuits, while the closure grammar appears to need an explicit description tag to preserve coherence. No compression of that tag has been found.

The next mathematical question is whether actual circuit descriptions admit a *semantic state quotient*: two partial descriptions may share a closure state exactly when every cross-combination of their unfinished evaluation obligations remains extendible to one low circuit, or is already excluded by contradictory table literals. Prove a near-linear bound for that quotient (upper-bound route), or prove that its required number of classes is superlinear (lower-bound route). Do not count syntactic descriptions unless distinct semantic obligations are proved.

**Status:** candidate upper-bound architecture rejected at the unsupported sharing step; exact missing invariant identified. No near-linear native cover, superlinear lower bound, or P-vs-NP result follows.
