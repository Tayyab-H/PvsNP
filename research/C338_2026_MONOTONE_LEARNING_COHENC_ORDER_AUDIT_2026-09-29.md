# C-338 - 2026 monotone example hardness still does not supply a C-125 map

Date: 29 September 2026  
Route: test whether recent monotone circuit learning and partial-MCSP hardness gives the remaining positive CohEnc transfer.  
Classification: **NEW LITERATURE / EXACT MAP-ORDER AUDIT; NO POSITIVE TRANSFER.**

## 1. Result checked

Cavalar, de Rezende, Gray, and Santhanam (arXiv:2607.12331, July 2026) prove under randomized ETH that (i) PAC-learning size-n monotone formulas by much larger monotone circuits takes quasipolynomial time, and (ii) approximating partial monotone circuit size from labelled examples is hard. Their Theorem 1.2 separates example sets consistent with a size-n monotone formula from sets with no nontrivial correlation with size-n^c monotone circuits. The input is a succinct list/distribution of examples; it is not a signed-rail map into a full truth-table Gap-MCSP promise.

Primary source: [arXiv:2607.12331](https://arxiv.org/abs/2607.12331), especially Theorem 1.2 and its monotone circuit-formula gap construction.

## 2. Direct C-125 translation fails by rail order

Let E be a consistent set of labelled examples on m of the N truth-table addresses. The natural partial rail vector is

    P[j,b] = 1 iff (address j, label b) belongs to E.

If a low circuit w fits E, then P is a subvector of its one-hot table code:

    P <= e(w).

C-125 needs the reverse inequality on YES inputs, e(w) <= Phi(YES). Thus the sample vector cannot serve directly.

The obvious upper-envelope repair sets both rails at every unobserved coordinate. Then every fitting low code is below the vector, but any unobserved coordinate is rail-conflicted. No consistent one-hot high code can be above this YES-style vector, so the NO high-completion condition fails. This is a pointwise order conflict, not a problem with the source's sample count.

Counting does make the NO side easy in isolation: if m=o(N), a consistent partial assignment has 2^(N-m) completions, while |SIZE(s2)|=2^(o(N)); hence it has high completions. That fact does not repair the YES order: choosing a consistent completion of P gives a code above P, not one below a monotone map that dominates a low code.

## 3. Reversing the input order does not fix monotonicity

The property "some size-s low monotone circuit fits the current examples" is downward-closed as examples are added. If input bits instead mark omitted examples, the property becomes monotone in those omission bits. But recovering the retained sample set from the omission bits uses negation, so the natural sample-to-rail map is no longer monotone in the source variables. The learning theorem supplies no alternative monotone rail map, no AND-cost upper bound for such a map, and no positive difference CycAnd(f)-CohEnc(f).

A successful adaptation would need an additional construction that simultaneously:

1. activates both polarities over a sufficiently broad YES-conflict support using monotone functions of the source input;
2. leaves every NO image consistent and below at least one high completion;
3. pays fewer AND gates than the source's cyclic decision complexity by a positive superlinear margin.

The paper establishes none of these map properties. Its conditional sample-agreement hardness remains useful for learning/approximation, but it does not change the unconditional Gap-MCSP fusion bound or instantiate Route A.

## 4. Disposition

This closes only the direct example-list adaptation of the July 2026 result. It does not rule out a witness-dependent C-125 map from a different monotone source. Keep O-167/O-168 primary; reopen this paper only if an explicit asymmetric rail construction or source-decoding separation is found. The proved Gap-MCSP lower bound remains N-o(N).
