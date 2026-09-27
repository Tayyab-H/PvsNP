# C-223 — Adaptive circuit signatures cross a search-MCSP boundary

Date: 27 September 2026  
Scope: continue the C-115/C-222 adaptive-signature branch of C-75. This formalizes what an explicit adaptive selector would buy and which extra output structure it imposes compared with a general shared DAG. It proves no unrestricted DAG or fusion lower bound.

## Setup

Let `N=2^n`, `Y=SIZE(s1)`, and `Z={0,1}^N minus SIZE(s2)`, with `s1=N^beta/(c n)`, `s2=N^beta`, and fixed `0<beta<1`. A circuit description has `O(s1 log(s1+n))` bits in a standard fan-in-two encoding. Let `S` be a Boolean circuit whose input is the N-bit truth table `w` and whose output is a description `d(w)` of a circuit of size at most `s1`.

Call `S` an exact low-table selector if, for every `w in Y`, `C_{d(w)}(x)=w_x` for every `x in {0,1}^n`. No requirement is imposed on the description selected for `w` outside `Y`.

## Selector-to-separator lemma

If an exact low-table selector has Boolean circuit size `R`, then the promise `(Y,Z)` has a separator circuit of size

`O(R + N s1 log(s1+n))`.

**Proof.** Compose `S` with a universal circuit for descriptions of size at most `s1`. For each of the N addresses `x`, make one copy of that universal evaluator with `x` fixed, compare its output to the input bit `w_x`, and AND the N equalities. The resulting circuit `V(w)` accepts every `w in Y` by selector correctness. If `z in Z` were accepted, then `z` would equal the truth table of a circuit of size at most `s1<s2`, contradicting `z in Z`. Thus `V` is a separator. A standard universal circuit for size-`s1` fan-in-two circuits costs `O(s1 log(s1+n))`; N copies plus S and the N comparisons give the bound. Malformed selector outputs can be mapped to a fixed default circuit without changing the argument.

At the OPS parameters, `N s1 log(s1+n)=O(N^(1+beta))` (up to constants). Therefore an `R=N^gamma` selector would imply `S_rect=O(N^max(gamma,1+beta))` and, by the existing reverse transfer, `rho_prom=O(N^max(gamma,1+beta))`. This is a useful upper bound if such a selector is constructed, but it is not near-linear for fixed beta and does not contradict every target `rho_prom>N^(1+epsilon)` when `epsilon<beta`.

## Why the converse does not follow

A separator circuit decides one promise bit: it is 1 on `Y` and 0 on `Z`. It need not output a circuit for an accepted table, choose a canonical description, or distinguish among the many descriptions of the same table. Turning that decision object into a circuit description is a search-to-decision step. The exact classical MCSP search-to-decision question is itself a long-standing open problem; see Ilango, *The Minimum Formula Size Problem is (ETH) Hard*, [SIAM J. Comput.](https://doi.org/10.1137/22M1481579), which explicitly distinguishes the open MCSP search-to-decision problem from the formula result proved there.

**Recent-literature check.** Hirahara and Ilango's FOCS 2025 paper proves NP-hardness of constant-factor approximate MCSP under deterministic quasipolynomial-time nonadaptive reductions, conditional on three assumptions including subexponentially secure non-interactive witness-indistinguishable proofs for SAT and strong circuit lower bounds. It also discusses oracle barriers to MCSP search-to-decision. This is important meta-complexity context, but it is conditional and does not supply an unconditional selector lower bound or a rect-DAG lower bound for this OPS promise. See the [authors' FOCS 2025 paper](https://www.rahulilango.com/papers/MCSP-Proceedings-2025.pdf).

This is not an equivalence theorem: the C-75 separator is a **gap** separator and may be an arbitrary extension on medium-complexity tables, while standard MCSP decision oracles concern a specified threshold. The literature fact only warns that no generic self-reduction should be assumed. A proof of selector hardness would not automatically lower-bound all rect-DAGs; it would attack the stronger task of producing a low-circuit witness.

## Consequence for the C-115 adaptive signature

The C-115 signature is selected from the internal wires of a circuit computing `w`. A selector that outputs the full circuit description (or explicit wire circuits plus a lookup) lets one instantiate that witness, but is a search-MCSP-style task. C-222 rules out only a fixed menu of address partitions; C-222-A shows that the sparse-indicator witness subfamily has an efficient adaptive support selector. Neither result yields a lower bound on an adaptive selector for all of `Y`.

More importantly, an arbitrary rect-DAG need not synthesize `C_{d(w)}`. It may route input tables through local rectangle predicates and share residual search states without ever naming a circuit. Thus the implication chain is one-way:

`small exact selector -> separator of size O(R+N s1 log(s1+n)) -> rho_prom upper bound`.

No converse is proved. Selector lower bounds cannot substitute for O-141's product-hull-safe state-reuse theorem.

## Disposition

This is a route filter, not a breakthrough. Keep two independent targets:

1. For a falsification upper bound, try to construct a near-linear rect-DAG directly; do not insist on a circuit selector.
2. For a lower bound, charge residual separator/state reuse across arbitrary product hulls; do not infer it from fixed-menu size or search-MCSP difficulty.

The established transfer chain remains `rho_prom <= O(S_rect) <= O(q^3/log q)`. No actual-promise superlinear lower bound, improved compiler, or P-vs-NP proof follows from C-223.
