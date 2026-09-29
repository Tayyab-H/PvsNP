# C-331 — PCP commitment is not an observable register in the native game

Date: 28 September 2026  
Route: attempt a PCP-based near-linear verifier for the low-circuit promise.  
Classification: **PROMISING QUANTIFIER VIEW; NO VALID NATIVE COMPILATION.**

## The tempting quantifier conversion

Membership in the low side has the form “there exists a circuit description d such that for every address a, C_d(a)=w_a.” A PCP for the corresponding NP language gives a proof π with perfect completeness and soundness below one: for a YES table, one proof is accepted on every random string; for a NO table, every proof has at least one rejecting random string. As a logical statement, this is exactly

    exists π, for every random string r, V(w,π,r)=1.

Replacing random challenges by adversarial universal choices would make soundness exact while preserving completeness. The basic PCP theorem supplies logarithmic randomness and a constant number of proof queries, but this fact alone is not a small native cover. [Arora et al., “Proof Verification and the Hardness of Approximation Problems”](https://www.researchwithrutgers.org/en/publications/proof-verification-and-hardness-of-approximation-problems/).

## Why the q-state game does not store π

In the C-319 recurrence, each input table determines one least-fixed-point activation vector. A parent state reads only whether a predecessor is active; it cannot read which winning action was selected at that predecessor. The chosen action in a positional strategy is therefore not a writable, observable proof bit.

If several verifier contexts merge at one state representing proof bit π_i, its selected action is shared, but the successor state no longer knows which verifier context must continue. If contexts remain separate, their copies can make inconsistent choices for π_i. Support annotations do not repair this: C-306 proves that every support matching the same complete table is pairwise compatible, and the recurrence does not inspect support provenance.

This reproduces the same synchronization obstacle as C-329’s lane-specific OR witness, now in the form of a global PCP oracle. A direct expansion stores verifier-context/proof-position pairs and gives no near-linear state bound. Neither the PCP quantifier pattern nor a short random seed is a lower-bound-preserving compiler into the native support grammar.

## Model consequence

For the exact game, positional action choices and activation ranks are proof artifacts, not data registers: downstream equations see only the final Boolean state-activation vector. A viable witness-based construction therefore needs a mechanism that makes one globally chosen auxiliary bit both exclusive and readable by every context, while preserving soundness of every compatible support product. No such mechanism has been built here. The remaining constructive route must encode coherence in the state-level activation vector itself or avoid circuit-witness verification altogether.

## Disposition

Close the direct PCP-to-native-game conversion. It does not construct a cover, prove a state lower bound, or yield a P-vs-NP result. The useful lesson is specific: randomized verification can turn “some proof passes most challenges” into an exact ∃π∀r relation, but it does not solve the native grammar’s proof-commitment and readout problem. Continue O-181 only with a construction or lower-bound argument about the observable activation vector and compatible context/proof products.
