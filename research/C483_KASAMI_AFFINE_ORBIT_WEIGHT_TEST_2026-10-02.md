# C-483 - high-degree Kasami tables still have an O(N)-gate global test

Date: 2 October 2026  
Status: proved obstruction to one distributional witness family; no frontier change.

## Question and candidate mechanism

C-482 ruled out the polynomial-trace ensemble because of a low algebraic-degree signature. This cycle tests a different candidate: a cryptographically nonlinear, high-degree trace component, randomly relabeled by affine bijections of its address bits. The proposed hardness intuition is that high degree and an affine orbit may hide the table's structure.

The mechanism under test is an exact global moment: Hamming weight. If a candidate family has only a constant number of possible weights, a shared population-count circuit can recognize that signature in linear total-gate size. This gives a concrete, fan-out-safe upper bound on the test itself. It does not provide a lower bound for a complete GapMCSP separator.

## Family and theorem

Let n>=5 be odd, N=2^n, i=(n-1)/2, and

    d = 2^(2i) - 2^i + 1.

Then gcd(i,n)=1. Let f(x)=Tr_{2^n/2}(x^d), viewed as a Boolean function on n bits after fixing any basis of GF(2^n). Let A range over the affine bijections of GF(2)^n and let D_n be the distribution of truth tables of f composed with A.

**Theorem.** Every table in D_n is computable by an ordinary fan-in-two AND/OR/NOT circuit of O(n^3) gates and has weight in

    W_n = { N/2, N/2 - 2^((n-1)/2), N/2 + 2^((n-1)/2) }.

There is a deterministic ordinary circuit Q_n of O(N) total gates that accepts every table in D_n and accepts a uniform N-bit table with probability O(N^(-1/2)). Thus D_n is almost perfectly distinguishable from uniform by an O(N)-gate test, despite its high algebraic degree and random affine address change.

### Proof

The Kasami exponent x -> x^(2^(2i)-2^i+1), for odd n and gcd(i,n)=1, is a known almost-bent power permutation. For every nonzero output component, its Walsh coefficients belong to {0, +2^((n+1)/2), -2^((n+1)/2)}. In particular, for f and its zero-frequency Walsh coefficient

    W_f(0) = sum_x (-1)^f(x) = N - 2 wt(f),

we obtain wt(f) in W_n. Composition with an affine bijection merely permutes the N truth-table entries, so it preserves the weight. The binary weight of d is i+1=(n+1)/2, and the standard degree formula for Kasami trace components gives algebraic degree (n+1)/2.

To compute f, use a polynomial-basis representation of GF(2^n). A field multiplication has an O(n^2)-gate implementation by polynomial multiplication and reduction; repeated squaring and multiplication compute x^d with O(n) such operations; the trace is a linear map. The affine input map costs O(n^2) gates. This gives O(n^3) total gates, with XORs compiled into constant-size AND/OR/NOT circuits. For every fixed beta>0, O(n^3) <= floor(N^beta/(10n)) for all sufficiently large n, so every member is OPS-Low at that beta.

The test Q_n computes wt(T) using a carry-save population-count network. A 3:2 compressor replaces three bits in one column by a sum bit and a carry bit, reducing the total number of live bits by one. Repeating this leaves two rows after O(N) compressors; one final ripple-carry addition and three O(log N)-bit comparisons check membership in W_n. Every compressor and comparator uses O(1) fan-in-two AND/OR/NOT gates per bit, so total gates and wires are O(N). A gate-list encoding uses O(N log N) bits under the usual O(log N)-bit gate-address convention; the network can be printed in O(N log N) bit time. It uses no witness reconstruction, address-by-address circuit search, or native fusion assumption.

For a uniform table U, each exact-weight layer has size at most binom(N,N/2), and Stirling's estimate gives binom(N,N/2)/2^N=O(N^(-1/2)). Therefore Pr[Q_n(U)=1] <= 3 binom(N,N/2)/2^N=O(N^(-1/2)), while Pr[Q_n(D_n)=1]=1.

## Strongest counterconstruction and scope

The strongest attack is the O(N)-gate population counter itself. It defeats the intended conclusion that a high-degree cryptographic component, after random affine address changes, might serve as a hard-YES distribution. The distinguisher does not enumerate the affine orbit or recover the field representation; it checks one shared aggregate of the complete input.

Q_n is not a full-promise GapMCSP separator in either direction:

* It rejects the Low table AND_n, whose truth table has weight 1, so it fails YES completeness.
* Each of the three accepted exact-weight layers has 2^(N-o(N)) tables. For fixed beta<1, circuit counting gives at most 2^(O(N^beta log N)) tables of size at most s2=N^beta. Thus each layer contains tables of complexity greater than s2, and Q_n accepts NO tables, so it fails soundness too.

The usual canaries explain why this only retires an invariant-based witness, not the larger program. Parity is computed with O(N) shared XOR gates. Repeated-block equality is checked against one representative block with O(N) gates. A family specified by sparse parity checks with L total incidences is checked in O(L) gates, hence O(N) when L=O(N). Fixed simple relations among blocks can likewise be checked coordinatewise with O(N) total gates. These are counterexamples to charges based on many constraints, repeated witnesses, or visible global relations; none is a full-promise separator.

The paired full-promise upper attempt remains exact Low-description enumeration. Enumerating all size-s1 circuits and comparing their N-bit outputs gives O(N*2^(O(N^beta))) total gates. No near-linear full-promise construction emerged in this cycle.

## Resource and model accounting

* Candidate table circuit: O(n^3) ordinary AND/OR/NOT gates; its truth-table string has N=2^n bits.
* Random affine seed: log |AGL(n,2)|=n^2+O(n) bits; sampling an invertible matrix by rejection has constant expected trials. Materializing the whole table costs O(N n^3) elementary evaluation operations. These are seed and generation costs, not the circuit size of Q_n.
* Distinguisher: O(N) total gates and O(N) wires; O(N log N) gate-list bits and O(N log N) construction bit time in a direct uniform encoding. Evaluating it in a streaming RAM scan also takes O(N) bit operations; this runtime is not the gate-size measure.
* No implication is made about paid-AND states, fusion OR operations, native covers, or runtime under a different model.

## Literature, barrier, and originality

Canteaut, Charpin, and Dobbertin's primary 1999 paper lists the Kasami exponents as proven almost-bent power permutations for odd dimension and gives the exponent-weight degree criterion. The classical Walsh fact is established cryptographic/coding-theory literature, not a new result here. The project-specific deduction is that this particular OPS-Low affine-orbit family is separated from uniform truth tables by the explicit linear-size population-count circuit.

The Chen et al. locality barrier concerns specified locality-based lower-bound methods combined with magnification. This cycle is an ordinary global-statistic circuit upper bound for a candidate distribution; it neither bypasses nor strengthens that barrier. No universal barrier is claimed. The OPS magnification threshold remains the audited one: for a universal constant c, one fixed epsilon>0 and every sufficiently small fixed beta, a lower bound against ordinary circuits of size N^(1+epsilon) for Gap-MCSP[2^(beta n)/(c n), 2^(beta n)] would imply NP not subseteq P/poly. This cycle proves no such bound.

This report's weight test is an elementary, project-specific obstruction to one witness family, not a new Boolean-function theorem or an originality claim about Kasami functions.

## Exact frontier effect and next move

**Strongest proved statement this cycle:** an affine orbit of an odd-dimensional Kasami trace component is supported on three exact Hamming weights and is distinguished from uniform N-bit strings with advantage 1-O(N^(-1/2)) by an O(N)-gate ordinary circuit; its members have O(n^3) gates and therefore lie below s1 for every fixed beta>0 and large enough n.

**Frontier unchanged:** ordinary separator lower bound N-O(N^beta log N), with C-406's additive logarithmic reconvergence refinement; exact full-promise upper O(N*2^(O(N^beta))); fixed-epsilon OPS N^(1+epsilon) target open; separate native rho_GapMCSP>=N-o(N) target unchanged. No near-linear full-promise separator and no P-vs-NP proof.

**Research lesson:** algebraic degree and cryptographic nonlinearity do not make a truth-table distribution hard when a constant-size statistic survives. More broadly, any statistic computable by a shared O(N)-gate aggregator can explain structure only up to the linear scale. The next lower-bound attempt should return to the exact all-extension Low x High relation and prove a merge-stable charge on distinct ordinary DAG gates; do not keep swapping one recognizable Low ensemble for another. The next requested project-wide first-principles synthesis should use C-483 together with the previous route closures, rather than restart the literature review.

## References

* A. Canteaut, P. Charpin, and H. Dobbertin, “A New Characterization of Almost Bent Functions,” FSE 1999, LNCS 1636, pp. 186–200. [Primary paper](https://www-roc.inria.fr/secret/Anne.Canteaut/Publications/Canteaut_Charpin_Dobbertin99b.pdf).
* I. C. Oliveira, J. Pich, and R. Santhanam, “Hardness Magnification Near State-of-the-Art Lower Bounds,” Theory of Computing 17 (2021), Theorem 1.4. [Primary paper](https://www.theoryofcomputing.org/articles/v017a011/).
* L. Chen et al., “Beyond Natural Proofs: Hardness Magnification and Locality,” ECCC TR19-168. [Primary report](https://eccc.weizmann.ac.il/report/2019/168/).
