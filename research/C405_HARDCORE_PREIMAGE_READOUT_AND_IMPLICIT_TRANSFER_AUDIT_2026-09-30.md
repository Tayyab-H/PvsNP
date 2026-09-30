# C-405 - Hard-core preimage readout and the implicit-to-explicit gap

**Status:** a precise conditional mechanism makes a sampler's total label function hard against arbitrary shared circuits; no transfer to an ordinary Gap-MCSP separator. OPS and native frontiers do not change.

## 1. Exact ordinary-circuit target

Let N=2^n be the number of truth-table input bits. Oliveira-Pich-Santhanam, Theorem 1.4, gives a universal constant c >= 1: if there is one fixed epsilon > 0 such that, for every sufficiently small fixed beta > 0,

    GapMCSP[2^(beta n)/(c n), 2^(beta n)] is not in Circuit[N^(1+epsilon)],

then NP is not a subset of Circuit[poly]. Since n=log_2(N), the thresholds are s1=N^beta/(c log_2(N)) and s2=N^beta. The universal quantifier is over every sufficiently small fixed beta, with the same epsilon. The published theorem states universal c; its proof uses the concrete constant 10. This is the only ordinary-gate magnification target used here. [OPS, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)

The ordinary model below is fan-in-two AND/OR/NOT total gate count, with unrestricted fanout and free wires. Description length, number of wires, runtime, and native fusion states are separate measures.

## 2. Candidate mechanism: hard-core preimage opacity

This is a fully specified way in which a compact sampler can expose the complete input distribution while the induced total Boolean function still requires a large circuit. The charge is a reduction to prediction hardness, not a claim that each address or intermediate result must be recomputed.

Assume a family of permutations P_m from m-bit strings to m-bit strings, with Boolean circuit size p(m). Let H_m(x,z) be the Goldreich-Levin bit, the inner product of x and z modulo 2. Assume H_m is hard-core for the map G_m(x,z)=(P_m(x),z) against nonuniform circuits of size at most t(m): every such predictor A has

    Pr_(x,z)[A(P_m(x),z) = H_m(x,z)] <= 1/2 + eta(m),

for some eta(m) < 1/2. This is the standard hard-core predicate setup, with the random challenge z included in the input. Define a sampler E_m using uniform branch bit a and uniform x,z in {0,1}^m:

* if a=0, output ((0,P_m(x),z), H_m(x,z));
* if a=1, output ((1,x,z), 0).

Its first component has full support on {0,1}^{2m+1}: P_m is a permutation, so branch 0 covers every address with prefix 0, and branch 1 covers every address with prefix 1. Labels are consistent. The induced total function is

    f_m(0,y,z) = H_m(P_m^(-1)(y),z),   f_m(1,y,z) = 0.

The sampler circuit has size at most p(m)+O(m).

**Theorem (conditional gate charge).** If an arbitrary AND/OR/NOT circuit D of S gates computes f_m, then

    S > t(m) - p(m) - O(1).

**Proof.** Compose D with P_m and hardwire the leading zero: A(x,z)=D(0 concatenated with P_m(x) concatenated with z). This predictor has at most S+p(m)+O(1) gates and predicts H_m(x,z) perfectly. If that sum were at most t(m), it would violate the hard-core condition, since 1 > 1/2+eta(m). The proof places no restriction on topology, fanout, reuse, or internal semantics of D. QED.

This establishes a genuine mechanism for the stated sampler family. The explicit table has L=2^(2m+1) bits. If the hard-core condition holds up to t(m)=2^(delta m) for some fixed 0<delta<2, then this table is high for OPS threshold L^beta whenever fixed beta < delta/2, after absorbing polynomial p(m). A merely subexponential bound t(m)=2^(m^alpha), alpha<1, does not suffice for any fixed positive beta, because m^alpha=o(m). The exponential hardness needed to meet the exact Gap-MCSP threshold is a strong additional assumption.

## 3. Adversarial tests and counterconstruction

The mechanism is a sufficient cryptographic condition, not a universal law about shared computation. These standard easy readouts refute any attempt to charge gates solely from global dependence, many constraints, or repeated use. They do not refute the conditional hard-core theorem.

* **Parity:** m-bit parity uses 4(m-1) AND/OR/NOT gates through a two-input XOR implementation. Reusing prefix parities can reduce repeated work; counting expanded incidences overcharges it.
* **Repeated-block equality:** compare corresponding bits by XNOR and AND the results, using O(m) gates for two m-bit blocks.
* **Sparse parity checks:** for a check matrix with O(N) nonzero entries in total, compute all row parities and their conjunction with O(N) XOR-basis gates, hence O(N) AND/OR/NOT gates.
* **Simple global block relations:** if blocks are copies of a seed block or are seed blocks XORed with public masks, generate or reuse each predicted bit and check the O(N) positions in O(N) gates. No linear bound is asserted for a general dense relation matrix; its actual circuit complexity must be charged.

The sharp counterexample to a seed-entropy argument is padding: replace E_m(x,z) by E'_m(x,z,w)=E_m(x,z), with arbitrary extra random bits w. Support and f_m are unchanged. Seed length, sample count, and address coverage alone therefore have zero lower-bound force. The hard-core hypothesis is the part doing the work.

## 4. Why this is not yet a Gap-MCSP lower bound

The theorem lower-bounds the circuit for one total function f_m derived from a sampler. It does not lower-bound a separator on the L-bit truth-table input. It supplies no low-table counterpart and no map whose images are all promised with a hard YES/NO trace. The exact composition fact remains: if phi maps k-bit strings to N-bit tables with circuit cost T, every image is promised, and its promise label equals F(x), then any S-gate separator gives Ckt(F) <= S+T+O(1). The hard-core sampler above does not furnish such a phi. One hard NO table is not a hard decision problem.

There is also a representation transfer cost. For a sampler E from r-bit seeds to m-bit addresses and labels, with consistent labels and full support, one safe explicitization enumerates all 2^r seeds once, records one label for every address, then fills the 2^m-bit table. Its deterministic runtime is 2^r poly(|E|,r,m)+2^m. A circuit that performs this complete conversion has an exhaustive-search construction of size at most 2^O(r) poly(2^m,|E|,m). These are upper bounds on conversion resources, not lower bounds on f_m, and must not be conflated with the S gates of a separator.

For the hard-core construction itself, a per-address inversion lower bound is false. Enumerate all pairs (x,z), compute P_m(x) and the Goldreich-Levin bit, sort the resulting address-label pairs, and stream them as the table; fill every (1,y,z) cell with 0. This materializes all L=2^(2m+1) bits in O(L poly(m)) time, without computing P_m inverse separately for any address. It is a counterexample to per-address inversion charging, not to the circuit lower bound for f_m and not a full-promise separator construction.

TR26-091 gives NP-hardness for **implicit** Gap-ImpMCSP under crypto/proof-complexity assumptions, with sampler circuits using polynomially many random bits and polynomial domain length. It does not state the short-seed condition or an explicit-table map of the source-size needed for OPS. Its Theorem 40 assumes subexponentially secure iO and NIWI, plus absence of infinitely-often subexponentially-optimal proof systems. [Goldberg-Juvekar-Kabanets, TR26-091](https://eccc.weizmann.ac.il/report/2026/091/download/)

In that reduction, source formula length is q, while explicit truth-table length is 2^(a(q)+ell(lambda(q))) for polynomially large a, ell, and lambda. Even if exhaustive generation is polynomial in table length, composing an N^(1+epsilon)-size separator with this exponentially long output only yields an exponential-size circuit in q, not the polynomial-size SAT circuits contradicted by OPS. Two bridges are missing: the correct circuit-hardness exponent relative to the truth-table domain, and a promise-preserving reduction with the source/output size relation needed for a P/poly consequence.

## 5. Paired full-promise separator attempt

Let M <= 2^O(s1 log(s1+n)) = 2^O(N^beta) be the number of size-at-most-s1 circuit descriptions on n=log_2(N) inputs.

**Fixed-sample accelerator attempt.** If a low table and a high table differ at d truth-table addresses, start with the low circuit and XOR its output with the OR of the d equality minterms. Each address minterm costs O(log N) gates, so the patched circuit has size at most s1+O(d log N). Since a high table needs size at least s2, every high/low pair differs on d=Omega((s2-s1)/log N)=Omega(N^beta/log N) coordinates. Try choosing a fixed random query set Q of k truth-table positions, then accepting when the input agrees on Q with some size-s1 circuit. Every YES table passes; soundness would follow if Q hit the disagreement set of every high/low pair.

There are at most 2^N possible high tables and M low-circuit descriptions. For any fixed pair, the probability a uniform k-subset Q misses its disagreement set is at most exp(-kd/N). Using only d=Omega(N^beta/log N), the straightforward union bound gives a sufficient sample size O(N^(2-beta) log N), which exceeds N for fixed beta<1 and so gives no useful sublinear guarantee. Even if a suitable Q were available, a direct circuit for "matches some low description on Q" costs O(kM) gates. Sampling alone neither supplies the universal query set nor compiles the M-way existential search into a small shared circuit. This closes this fixed-sample construction only. It is not a lower bound against input-dependent anti-checkers or other full-promise separators.

Enumerate these M truth tables y_1,...,y_M. For each j, test equality with the input table using N signed literals and an AND tree, then OR the M equality bits. This accepts every promised YES table, rejects every promised NO/high table, and has

    O(NM) = O(N * 2^O(N^beta))

total gates. It is a valid nonuniform full-promise separator; it is not near-linear. Per comparator there are N coordinate tests, at most N NOT gates and N-1 AND gates; the final OR tree has M-1 OR gates. Thus each gate type and the wire count are O(NM). A standard indexed-gate description uses O(NM log(NM)) bits. A direct uniform constructor can enumerate the M descriptions, simulate each on N addresses in O(MNs1) time, and emit the O(NM)-gate separator. These are separate bounds: the gate count excludes description bits and construction time. A trie or shared-prefix DAG can save work for structured candidate tables, but no universal compression bound for this low-circuit set has been proved. No near-linear separator construction was found in this cycle.

## 6. Barrier and originality audit

The hard-core predicate construction is standard cryptographic reasoning; Goldreich and Levin's STOC 1989 theorem supplies the challenge-bit predicate for one-way functions. The 2026 implicit-MCSP paper already develops related sampler-based hardness. The project-specific refinement here is the exact full-support completion, arbitrary shared-circuit gate inequality, and explicit accounting of why neither implicit NP-hardness nor subexponential sampler hardness meets fixed-beta OPS thresholds. This is not claimed as a new complexity theorem. [Goldreich-Levin, STOC 1989](https://doi.org/10.1145/73007.73010)

The hardness-magnification locality barrier of Chen et al. identifies that some magnified MCSP variants have efficient circuits augmented with small-fanin oracles, while several existing weak-model lower-bound techniques extend to such oracle circuits. It is technique-specific, not a proof that the ordinary total-gate target is impossible. This sampler-to-table mechanism uses global preimage access and supplies no local-oracle lower-bound method, so it neither evades nor contradicts that barrier. [Chen et al., *Beyond Natural Proofs: Hardness Magnification and Locality*](https://doi.org/10.1145/3538391)

## 7. Quantitative effect and changed next mechanism

**Strongest proved statement this cycle:** under the stated hard-core-permutation assumption, every total circuit for the sampler-defined full-support function has more than t(m)-p(m)-O(1) gates. This is a conditional function lower bound, not an unconditional separator bound.

**Exact frontier effect:** none. Ordinary Gap-MCSP remains S >= N-O(N^beta log N)-1 = (1-o(1))N; the required N^(1+epsilon) OPS lower bound remains open. Native rho remains N-o(N), and no N^(1+o(1)) full-promise separator/cover is known.

**Route decision:** do not extend the subspace/restriction route by merely counting anchors or hardening the same linear trace. Next investigate two explicit bridge obligations: (i) a polynomial-source-length, all-promised map into explicit Gap-MCSP with a hard label function, and (ii) security/lower bounds of at least 2^(delta m) for fixed delta>0, rather than 2^(m^o(1)). In parallel, search for a full-promise separator that exploits shared candidate structure and prove its total-gate bound. No native fusion or cyclic-closure inference is made.
