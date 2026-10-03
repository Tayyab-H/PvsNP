# First-principles audit after C-487

**Date:** 2 October 2026  
**Purpose:** consolidate the mathematical lessons through C-487 and set the next research test without restarting the project.

## 1. The exact problem

For \(N=2^n\), fixed \(0<\beta<1\), let

\[
L_{\mathrm{low}}=L_{\lfloor N^\beta/(10n)\rfloor},\qquad
L_{\mathrm{high}}=\{T:\mathrm{CC}_n(T)>N^\beta\}.
\]

The ordinary target is

\[
\mathrm{GapSep}(N,\beta)
=\min\{\mathrm{CC}_N(F):F=1\text{ on }L_{\mathrm{low}},
F=0\text{ on }L_{\mathrm{high}}\}.
\]

The values of \(F\) on the middle band are unrestricted. A lower bound for one chosen extension, one chosen Low family, a restricted circuit model, or a proposed algorithm does not lower-bound this minimum unless a valid transfer is proved. OPS magnification requires one fixed \(\epsilon>0\) that works for every sufficiently small fixed \(\beta>0\); the resulting statement implies \(\mathrm{NP}\not\subseteq\mathrm{P/poly}\).

## 2. Verified quantitative frontier

* The ordinary lower bound remains \(N-O(N^\beta\log N)\) essential inputs, with the C-406 refinement. This is an information/support statement, not a superlinear gate bound.
* Exact enumeration gives a complete ordinary separator of \(O(N2^{O(N^\beta)})\) gates.
* There is no proved \(N^{1+\epsilon}\) lower bound for every total extension, no near-linear full-promise separator, and no P-vs-NP proof.
* The native \(\rho\), fusion, and cyclic-closure questions are distinct; no ordinary-gate theorem transfers to them without a proved compiler.

## 3. What the accumulated failures mean

The experiments and proofs are better grouped by the resource they measure than by topic:

1. **Information available from the input.** Support, balanced sketch width, certificate width, entropy deficits, residual cofactors, and local query paths can reach the near-\(N\) information scale. C-474 and C-484 prove explicit caps; selector circuits and arbitrary shared reductions show why counts cannot simply be summed into gates.
2. **Recognizable structure in a selected YES family.** Affine checks, ANF degree, Hamming weight, block equality, sparse checks, and global statistics often have \(O(N)\)-gate shared tests. They retire particular ensembles, not all separators. C-487 strengthens this warning: even \(2^{\Theta(N^\beta)}\) Low tables with \(\Theta(N^\beta)\) bits of entropy can be recognized by a repeated-block test.
3. **One-sided recognition.** A sound test that rejects every High table may still reject Low tables outside its chosen subfamily. Universal completeness over all of \(L_{\mathrm{low}}\) is the difficult endpoint.
4. **Other computational models and source maps.** Formula, fixed-depth, local-query, native paid-state, and canonical-extension results need a cost-preserving compiler or a proof that every total extension inherits their lower bound. A source reduction must map every source YES to Low and every source NO to High, then pay all multi-output generation and postprocessing gates.

The common missing step is not a justified “non-shareability” rule. It is a theorem charging *post-read computation* in every shared AND/OR/NOT DAG, or a fully costed reduction/distribution theorem that forces such computation. Descriptions, witnesses, local constraints, and truth-table entropy are not themselves gates.

## 4. C-487's exact distributional route

If \(D\) is supported on \(L_{\mathrm{low}}\), any valid separator accepts \(D\) with probability one. Under a uniform \(N\)-bit table, it accepts with probability at most

\[
|L_{\lfloor N^\beta\rfloor}|/2^N
\le 2^{-N+O(N^\beta\log N)}
=2^{-N+o(N)}.
\]

Therefore an ensemble \(D_{n,\beta}\) that keeps every \(N^{1+\epsilon}\)-gate circuit's distinguishing advantage bounded away from one proves the desired lower bound. The gap may depend on fixed \(\beta\). This argument fully handles arbitrary sharing and middle labels. It does not assume the separator outputs a witness.

The premise is the hard theorem. Shannon–Lupanov synthesis supplies a decisive calibration: all Boolean functions on \(k\approx\log(s_1\log s_1)\) selected address bits have circuit size below \(s_1\); their family has \(2^{\Theta(s_1\log s_1)}=2^{\Theta_\beta(N^\beta)}\) members, yet repeated-block equality recognizes it with \(O(N)\) gates. A specified random-DAG sampler also passes an \(O(N\log N)\) essential-variable test on 96-99.75% of toy samples at \(n=6,8,10\); this is finite evidence only and the tested \(s=\Theta(n)\) is below the fixed-\(\beta\) OPS regime. High entropy is therefore not a replacement for computational indistinguishability.

### Security-parameter correction

C-486 correctly showed that negligible indistinguishability against every polynomial-size test is cryptographic. C-487 sharpens the quantifier: a uniform polynomial-time generator that is indistinguishable by **all polynomial degrees** even to a constant gap yields a weak one-way function by inverter verification, and standard hardness amplification applies. Negligibility is not needed for that consequence.

For one fixed \(\beta\), however, the separator criterion only concerns size \(N^{1+\epsilon}=m^{(1+\epsilon)/\beta+o(1)}\), one fixed polynomial degree in the seed length. A family indexed by \(\beta\) whose allowed degree changes with \(\beta\) is not one generator secure against every polynomial-size attacker. We have no amplification from this single bounded-size regime to standard OWF security. Keep this distinction in future sampler arguments.

## 5. Literature and barrier scope

The exact OPS theorem is established. The original paper's Theorem 1.4 states the fixed-\(\epsilon\), sufficiently-small-\(\beta\) magnification and its proof uses the \(1/(10n)\) low threshold. C-487's ensemble uses the classical Shannon–Lupanov upper bound; neither fact is claimed as new.

Razborov–Rudich is a conditional obstruction for broad constructive natural-property proofs under cryptographic assumptions; it is not an unconditional theorem that no separator proof can work. Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam's locality barrier concerns specified weak lower-bound methods that remain strong in the small-fan-in oracle models produced by magnification. It is method-specific, not a universal impossibility theorem. This project has not proved that the C-487 distribution criterion escapes either barrier; it has only isolated the exact parameterized pseudorandomness statement required.

## 6. Next actions that change the mathematics

1. Test the uniform small-circuit-description ensemble against concrete weight, affine, ANF, repeated-block, sparse-check, and global-relation tests. The C-487 \(k\)-junta ensemble is a hostile calibration, not a result about uniform circuit descriptions.
2. If a candidate survives those tests, prove a circuit-size indistinguishability theorem at the exact degree \(q_\beta=(1+\epsilon)/\beta+o(1)\). Passing tests is not evidence of a general circuit lower bound.
3. In parallel, continue the direct all-extension route only with a potential defined on distinct DAG gates, an operation-wise recurrence for AND, OR, and NOT, and a superlinear value forced by both promise endpoints. Parity, repeated blocks, sparse checks, and simple global relations remain mandatory counterexamples.
4. Keep the complete enumeration upper \(O(N2^{O(N^\beta)})\) as the paired construction baseline; any claimed saving must count gates, wires, description bits, and synthesis runtime separately.

## 7. Conclusion

The project has not found a missing elementary lemma or a proof-level breakthrough. It has established that input-information arguments naturally stop at \(N\), and that entropy-rich Low families can still have linear-size shared tests. The remaining obstacle is genuinely a computation-cost question under unrestricted sharing. The work remains active; all quantitative frontiers above are unchanged.

### Primary references

* [Oliveira, Pich, Santhanam, Hardness Magnification Near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4.
* [Lupanov, On the Possibilities of Synthesis of Circuits out of Various Elements](https://www.mathnet.ru/php/archive.phtml?jrnid=tm&option_lang=rus&paperid=1277&wshow=paper), 1958.
* [Chen et al., Beyond Natural Proofs: Hardness Magnification and Locality](https://eccc.weizmann.ac.il/report/2019/168/).
* [Razborov and Rudich, Natural Proofs](https://doi.org/10.1006/jcss.1997.1494).
* [Goldreich, Foundations of Cryptography, weak-to-strong one-way functions, Sec. 2.3](https://www.wisdom.weizmann.ac.il/~/oded/foc-vol1.html).
