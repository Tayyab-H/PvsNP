# C-412 - Small-circuit patch balls force YES flatness, but do not charge gates

Date: 30 September 2026

**Status:** proved a promise-safe local-neighborhood constraint for every separator; failed to turn it into a total-gate lower bound. A linear-size sparse-table recognizer is the strongest counterconstruction to a generic local-flatness charge. No quantitative frontier changes.

## 1. Exact setting

Let N=2^n, s1=N^beta/(10n), and s2=N^beta, with fixed 0<beta<1. Use the OPS promise convention: YES tables have circuit size at most s1 and NO tables have size at least s2; the separator's output on the middle band is unrestricted. Circuits here are ordinary fan-in-two AND/OR/NOT DAGs with unrestricted fanout, and the measure is total gates. OPS Theorem 1.4 asks for one fixed epsilon>0 such that, for every sufficiently small fixed beta>0, no N^(1+epsilon)-gate separator exists.

## 2. A precise mechanism candidate: forced Hamming-flat neighborhoods

For a table f and a set R of truth-table addresses, write f_R=f XOR 1_R, where 1_R is the indicator of R. If f has a circuit of size at most floor(s1/2), then

    CC(f_R) <= CC(f) + |R| n + n + 3.

To see this, build one n-literal minterm for each address in R using n-1 AND gates, OR the minterms using |R|-1 OR gates, negate the n input variables once, and XOR the resulting sparse correction with f using four AND/OR/NOT gates. This is an explicit total-gate construction; it does not charge one separate table read per address.

Set

    r = floor((floor(s1/2) - n - 3)/n).

For every |R|<=r, the displayed circuit has size at most s1. Thus every valid separator h obeys

    B_r(C_{floor(s1/2)}) subseteq h^{-1}(1) subseteq C_{<s2},

where C_t is the set of truth tables of circuit size at most t and B_r is Hamming distance at most r in the N truth-table coordinates. Endpoint rounding can be adjusted to the equivalent integer OPS promise convention. Asymptotically r=Theta(N^beta/n^2). In particular, h is identically one on the entire r-dimensional coordinate subcube obtained by varying any fixed set R of at most r positions around any sufficiently small anchor f. All Boolean finite differences over GF(2) of positive order at most r vanish at each such anchor.

This is stronger than a single-anchor observation and respects the free middle band: only modifications that are proved to remain YES are forced to be accepted.

## 3. Gate-charge attempt and the decisive obstruction

The candidate potential was

    Phi_r(g)= number of pairs (f,R) with CC(f)<=floor(s1/2), |R|<=r, and g(f XOR 1_R)=1.

Every valid separator has Phi_r(h)=|C_{floor(s1/2)}| times sum_{j=0}^r binom(N,j). Topologically numbering each circuit's gates gives |C_{floor(s1/2)}|<=2^(O(s1 log(s1+n)))=2^(O(N^beta)); each gate chooses a type and two predecessors from O(s1+n) possibilities. Also sum_{j=0}^r binom(N,j)<=2^(O(r log(N/r)))=2^(O(N^beta/n)). The required gate-charge step would be a useful upper bound on Phi_r(g) in terms of the total gates of g, stable under each allowed DAG operation. No such bound follows from this definition: the one-NOT-gate function g(x)=NOT x_a already counts every pair with center f=0 and a not in R, giving at least sum_{j=0}^r binom(N-1,j)=2^(Theta(N^beta/n)) pairs. One gate's output can therefore affect exponentially many potential incidences. Further, log Phi_r(h) is at most O(N^beta); even the unsupported ideal estimate S>=log Phi_r would stay below the existing linear bound. Counting accepted points, local derivatives, anchors, or incidences therefore supplies neither a bounded-growth potential nor the target superlinear gate charge.

The strongest direct calibration is an O(N)-gate Hamming-weight threshold. Let k=floor(s1/(8n)) and use

    h_sparse(x)=1 iff wt(x)<=k+r.

Every accepted table has a minterm circuit of size at most (k+r)n+n<s1 for sufficiently large n, so h_sparse rejects every promised NO table. It accepts the full radius-r Hamming ball around every table of weight at most k; these centers themselves have circuit size below s1/2. A carry-save population count followed by comparison computes h_sparse with O(N) fan-in-two gates. It is not a full-promise separator: it rejects dense YES tables such as parity. It is, however, an explicit counterexample to charging a huge family of locally forced sparse neighborhoods as independent gate work.

This does not refute a theorem using the full, structured family C_{floor(s1/2)}. The missing statement would have to exploit that circuit-generated family beyond its local balls. No such gate-potential bound is proved here, and asserting one would merely rename the hard lower bound. The local-flatness mechanism is retired as a standalone route.

## 4. Requested cheap-sharing attacks

- **Parity:** parity on n address bits has an O(n)-gate circuit. Since its complexity is far below s1 for large n, every table obtained by toggling at most r truth-table positions remains YES by the patch construction and must be accepted. This forces a large local YES neighborhood around a dense structured table, but gives no additive gate charge.
- **Repeated-block equality:** for N=bm bits arranged as b copies of an m-bit block, checking equality of all copies to the first takes O(N) fan-in-two gates. The N-m equality constraints cannot be charged independently as fresh table scans.
- **Sparse parity checks:** a parity-check family with O(N) total nonzero incidences has an O(N)-gate syndrome/readout circuit. If checks are nested prefixes, their expanded incidence is Theta(N^2), but all prefixes are computed by one shared XOR chain using O(N) gates; a final linear number of comparisons remains O(N).
- **Simple global block relations:** if block j is a copy of a base bit, or is generated by a shared prefix parity of base bits, compute the base relation once and compare the N output positions in O(N) total gates. This defeats charges based on block multiplicity or repeated use of a global statistic.

These are counterexamples to generic local-constraint and per-incidence charges. None is a counterexample to the full Gap-MCSP lower-bound program, and none is a full-promise separator.

## 5. Paired full-promise separator construction attempt

For every circuit description D of size at most s1, hardwire its full N-bit truth table and test whether the input f equals it. OR the equality tests:

    Sep(f)= OR_{D: size(D)<=s1} AND_{a in {0,1}^n} [f(a)=D(a)].

This accepts every YES table and rejects every NO table; it may reject the middle band. There are K=2^(O(s1 log(s1+n)))=2^(O(N^beta)) candidate descriptions. Each equality test costs O(N) total gates, and the outer OR costs O(K), so the explicit ordinary total-gate upper bound is O(N 2^(O(N^beta))). The truth tables are hardwired into the circuit; construction time and description size are not being counted as gates. Batching all candidate reads does not remove the K-way consistency disjunction. No near-linear full-promise separator was constructed.

## 6. Literature, originality, and frontier

The exact magnification quantifiers and the universal constant denominator come from Oliveira-Pich-Santhanam, Theorem 1.4; their proof instantiates 10n. The Chen-Hirahara-Oliveira-Pich-Rajgopal-Santhanam locality barrier applies to specified weak models with small-fan-in oracle gates and to particular lower-bound methods. It is not a theorem about arbitrary ordinary total-gate separators. C-411's Theorem 59 transfer only rules out the stated fixed-menu parameter range. Neither result supplies the missing gate charge for this mechanism. The neighborhood statement above is a project derivation; it is not claimed as a new complexity lower bound.

**Strongest proved statement:** every separator accepts the radius-r Hamming neighborhood of every table of circuit size at most floor(s1/2), where r=Theta(N^beta/n^2), and rejects every table in the OPS NO set. The proof is the explicit sparse-address patch circuit above.

**Exact quantitative effect:** none. The ordinary lower bound remains S>=N-O(N^beta log N)-1, with C-406's additive logarithmic refinement. The OPS N^(1+epsilon) target remains open. Native rho_GapMCSP>=N-o(N) remains separate; this acyclic ordinary-circuit argument says nothing about paid AND states, OR operations, wires, endpoint width, wide seeds, unrestricted native reuse, cycles, or required semi-filter extensions. The explicit full-promise upper remains O(N 2^(O(N^beta))).

### Primary sources

- Oliveira, Pich, and Santhanam, [Hardness Magnification near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4.
- Chen, Hirahara, Oliveira, Pich, Rajgopal, and Santhanam, [Beyond Natural Proofs: Hardness Magnification and Locality](https://drops.dagstuhl.de/storage/00lipics/lipics-vol151-itcs2020/LIPIcs.ITCS.2020.70/LIPIcs.ITCS.2020.70.pdf), Theorem 59 and Corollary 61.
- Exact project threshold and locality parameter audit: [C-411](C411_TARGET_SCALE_STATIC_ANTICHECKER_MENU_LOCALITY_OBSTRUCTION_2026-09-30.md).
