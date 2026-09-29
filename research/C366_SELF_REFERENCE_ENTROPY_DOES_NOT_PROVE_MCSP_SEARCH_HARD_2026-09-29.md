# C-366 — Incompressibility does not by itself make MCSP search hard

Date: 29 September 2026  
Route: audit an information-theoretic/self-reference argument for MCSP and circuit lower bounds, motivated by the project's foundations-first directive.  
Classification: **LITERATURE PROOF AUDIT; VALID NONCOMPUTABLE EXAMPLE, INVALID SEARCH-HARDNESS INFERENCE; NO q IMPROVEMENT.**

## 1. The claim under audit

The arXiv preprint *On the Incompressibility of Truth With Application to Circuit Complexity* (v4, December 2025) uses Shannon counting and Kolmogorov complexity, then proposes that MCSP search requires superpolynomial-size circuits because a search circuit would have to encode shortest descriptions of all truth tables. It further suggests this as a route to \(P\ne NP\). The paper also defines a family from prefixes of Chaitin's \(\Omega\) and claims the usual \(\Omega(2^n/n)\) circuit lower bound.

These are two distinct arguments. The \(\Omega\)-prefix argument is valid as a noncomputable existence construction. The entropy argument for MCSP search does not follow.

## 2. What the \(\Omega\)-prefix argument really proves

Let \(T_n\) be the first \(2^n\) bits of a fixed Chaitin halting probability \(\Omega_U\), and define the \(n\)-input Boolean function whose truth table is \(T_n\). Prefix incompressibility gives
\[
K(T_n)\ge 2^n-O(1).
\]
If a circuit of size \(s\) computes that function, encode the circuit in \(O(s\log s)\) bits. A fixed program, given this encoding and \(n\), can enumerate all \(2^n\) inputs, evaluate the circuit, and print \(T_n\). Therefore
\[
2^n-O(1)\le K(T_n)\le O(s\log s)+O(\log n),
\]
which implies \(s=\Omega(2^n/n)\). This is a sound Kolmogorov-complexity proof of a Shannon-scale lower bound for this particular family.

It is not an effective explicit hard family in the usual complexity-theoretic sense: its truth-table bits are bits of an uncomputable \(\Omega_U\). It supplies no efficiently computable family in NP or P and no P-vs-NP consequence. It also reaches the familiar near-maximum Shannon scale, rather than a new lower bound for efficiently specified functions.

## 3. The missing step in the MCSP-search entropy argument

Let \(T\) be an \(N\)-bit truth table. A search procedure receives \(T\) as input and outputs a circuit description for \(T\), when one exists below the requested threshold. The proposed entropy contradiction treats the descriptions output on all \(T\)'s as if they had to be stored in the fixed description of the search circuit.

That is not a valid information bound. The output may depend on the \(N\) input bits. A small circuit can output high-entropy strings when those strings are supplied as input: the identity map \(I(T)=T\) has \(N\) input and output bits and uses only wires, yet ranges over every incompressible \(N\)-bit string. Producing an object from an input that already contains its information does not compress that input.

For MCSP search, the search circuit's description length bounds the complexity of the *map* \(T\mapsto C_T\); it does not bound the unconditional Kolmogorov complexity of every \(C_T\) in its range. The Shannon count says most truth tables have no small circuit. It does not say that a polynomial-size function on the truth-table bits cannot identify a small circuit on the low-complexity subset. Establishing that would itself require a search lower bound, not an entropy accounting identity.

The distinction is particularly sharp here:

- For \(T_n\) derived from \(\Omega\), a short circuit for \(T_n\), together with a fixed decoder, would print an uncomputable prefix without being given that prefix. Incompressibility applies.
- For MCSP search, the input already is \(T\). A search circuit can use those bits in computing its output. The same Kolmogorov argument has no contradiction to apply.

The preprint's proposed implication “MCSP search has no polynomial circuit, therefore \(P\ne NP\)” has a valid conditional premise: if \(P=NP\), the polynomially verifiable circuit-witness relation can be searched in polynomial time by the standard NP search-to-decision self-reduction. But the claimed superpolynomial lower bound for that search map is not proved by the entropy argument.

## 4. Consequence for the C-319 activation-code idea

An activation vector \(X_Q(w)\) is computed from the table \(w\); it is not an advice string that must encode \(w\) without access to \(w\). Therefore a hypothetical decoder extracting a small-circuit description from \(X_Q(w)\) cannot be ruled out by counting the information in circuit descriptions against the fixed description length of \(Q\). The table remains available as the decoder's source of information.

This does not construct an activation-code decoder. The real obligation remains computational: produce a valid circuit on every low table and preserve full-promise soundness, within the C-319 state/readout budget. Ren-Santhanam's relativized separation of MCSP decision from even approximate search blocks a generic relativizing decision-to-search argument, but it does not exclude a specific nonrelativizing construction.

## 5. Checkpoint and next use

- No lower bound on the C-319 state count follows from this entropy/self-reference line.
- The valid \(\Omega\)-family is not a P/NP witness because it is uncomputable.
- Retire the inference from “many incompressible outputs” to “a small search circuit must encode all outputs in its own description.” Any future self-reference argument must isolate a string whose information is not already present in the input, or give a formal diagonal/fixed-point construction that forces this.
- The broader goal remains active: prove a q-sensitive lower bound for the actual promise or construct a full-promise near-linear cover. The proved bound remains \(\rho_{\mathrm{GapMCSP}}\ge N-o(N)\).

## Sources

- Luke Tonon, [On the Incompressibility of Truth With Application to Circuit Complexity](https://arxiv.org/html/2511.21738v4), arXiv:2511.21738v4 (28 December 2025), Sections 2–4. The preprint contains both the \(\Omega\)-prefix argument and the unsupported MCSP-search entropy inference audited above.
- Hanlin Ren and Rahul Santhanam, [A Relativization Perspective on Meta-Complexity](https://eccc.weizmann.ac.il/report/2021/089/download), ECCC TR21-089 (2021), Theorem 1.13 and Section 3.1: a relativized world where MCSP is in P but search-MCSP is hard, even for approximate search.
