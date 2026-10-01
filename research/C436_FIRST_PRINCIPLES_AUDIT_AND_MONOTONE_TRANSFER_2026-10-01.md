# C-436 — First-principles audit: the missing quantity is reusable membership work

**Purpose.** This is a first-principles synthesis of the cumulative project record through C-435, followed by an ordinary-OPS transfer audit of the spread-matching monotone lower bound already studied in the native C-261/C-266 line. It is a synthesis of the durable state, claim ledger, open obligations, and model; it does not independently re-prove every older report. The goal is to identify what the completed work actually says about the next proof attempt, without restarting the prior native matching route.

## 1. Exact target

Let `N=2^n`, and let `CC(f)` count total fan-in-two AND/OR/NOT gates with unrestricted fanout. For a universal constant `c>=1`, set

```text
s1 = N^beta/(c log2 N),        s2 = N^beta.
L_N = { f : CC(f)<=s1 },       H_N = { f : CC(f)>s2 }.
```

A separator is any *total* Boolean function `C:{0,1}^N->{0,1}` with `C=1` on `L_N` and `C=0` on `H_N`; its behavior on the middle band is unrestricted. Define

```text
SepCC(N,beta) = min { CC(C) : C is such a total separator }.
```

The OPS target is one fixed `epsilon>0` such that, for every sufficiently small fixed `beta>0`, no circuit family of size `N^(1+epsilon)` separates the promise (equivalently, the lower bound holds infinitely often under the paper's asymptotic convention). The theorem uses a universal `c`; its proof instantiates `c=10`. This precise lower bound implies `NP` is not in `P/poly` by OPS Theorem 1.4. Therefore this project is not looking for a missing estimate of certificate count: it is looking for a proof of a major unrestricted circuit lower bound.

## 2. First-principles audit of the cumulative results

The project has repeatedly established strong *semantic* constraints on valid separators, then found that these constraints do not force enough gates under unrestricted reuse. The reliable ordinary-circuit frontier is still

```text
CC(C) >= N - O(N^beta log N) - 1
```

with C-406's additive logarithmic refinement. This is essentially a bound on the number of relevant input coordinates. It does not charge the additional computation after all coordinates have been exposed.

| Line of attack | What is proved or learned | Why it stops short |
|---|---|---|
| Input support, safe cylinders, certificate width | A valid accepting cylinder cannot contain a High completion; each separator must depend on almost all table bits. | Fan-in-two circuits can expose all `N` bits with `O(N)` gates. Support has only a linear ceiling. |
| Hamming margin, anchors, local sensitivity, certificate counts | Low circuits have a patching margin of order `N^beta/polylog N`; many Low tables require many accepting regions. | Region count, boundary size, and certificate volume do not charge how one shared DAG generates their union. Sparse/co-sparse tails already have `O(N)` shared thresholds. |
| Samples, anti-checkers, minimax, version spaces | Every High table has a short semantic anti-checker; conditional selector synthesis works under `NP subseteq P/poly`. | Existence is not synthesis. Deriving a selector from an arbitrary one-bit separator is itself the hard transfer, and the middle band prevents naive robustification. |
| Restrictions and promise embeddings | Some subpromises have easy induced labels; an encoder can carry the hard computation itself. | A hard output set is not a hard decision trace. The complete separator must remain hard after its entire map is exposed. |
| Transcript fibers, cut rank, generic communication | These model sharing explicitly and produce valid total-gate inequalities. | The output potential is at most linear; identity readout leaves an arbitrary post-read decoder. Full cut rank is attained by an `N-1`-gate circuit. |
| Formulas, comparator circuits, cycle rank | Nontrivial restricted-model bounds and exact unfolding/transfer inequalities are available. | No compiler preserves ordinary shared-gate cost at the required scale. OPS needs fixed `epsilon` as `beta` tends to zero; a gain proportional to `beta` is insufficient. |
| Source-hardness transfers | Composition accounts for every generator and postprocessor gate; exact OPS threshold nesting requires a source gap exceeding `cD` after padding to `D` table-input bits. | Current HI parameters miss this ratio; oracle and implicit results do not automatically become ordinary truth-table circuits. |
| Fusion, cyclic closure, native states | The native target has extensive exact closure, counterexample, and compiler audits. | Its `rho>=N-o(N)` target is a distinct measure; no proved transfer yields the ordinary OPS total-gate bound. |

Four repeated calibrations are decisive against generic incidence arguments: parity, repeated-block equality, sparse parity-check systems with linear total incidence, and simple globally generated block relations all admit `O(N)` shared implementations. These examples falsify the proposed charge, not the GapMCSP lower-bound goal.

The common obstruction can be stated without metaphor: **all the information-counting arguments stop at what the separator must represent; none bounds the cost of evaluating that representation as a reusable Boolean DAG.** A wire, address, constraint, certificate, or gate occurrence is not an independent unit of computation when subcomputations may be shared.

## 3. Paired upper-bound audit

There is an exact full-promise separator: enumerate all `K=2^{O(N^beta)}` descriptions of circuits of size at most `s1`, compare the input table against each candidate truth table, and OR the equality tests. It handles every YES and NO table and leaves the middle band unrestricted. Its direct cost is `O(NK)=O(N*2^{O(N^beta)})` total gates (and `O(NK)` fan-in-two wires); hardwired description bits and construction time are separate. Prefix tries can still have `Theta(NK)` nodes for a general list, and no smaller bound for this special list has been proved. Thus this is a correctness-complete upper attempt, not a near-linear construction.

This upper bound also clarifies the challenge: the separator must recognize the union of all Low truth tables. It need not reconstruct a witness or run this enumeration. Any lower proof that says it must do so is invalid unless it proves that necessity for every extension and every shared circuit.

## 4. Ordinary-OPS transfer audit of the existing spread-matching line

Anup Rao's current ECCC TR26-129 revision proves an `exp(Ω(sqrt(n)))` monotone-circuit lower bound for detecting bipartite perfect matchings in `n`-vertex graphs, using a spread-matching lemma ([primary report, revision 5](https://eccc.weizmann.ac.il/report/2026/129/)). The project has already transferred this source hardness to the native cyclic model and extensively audited candidate LowExt maps in C-261–C-310. C-436 does not claim that source result or reopen the retired native map constructions. The bounded question here is whether this source can transfer to an *ordinary OPS separator* through a costed table map.

### Proposed transfer, stated precisely

This is distinct from the prior native transfer. C-261/C-266 unroll the cyclic monotone state system into a monotone matching circuit and obtain source hardness for `CycAnd`; C-263 and later audits identify the missing LowExt map and kill specific direct encodings. That source-model result does not constrain arbitrary ordinary OPS separators. In this cycle, the direct witness-verification truth table is checked only as a possible ordinary promise map, and it fails because its output function is polynomial-size on both source outcomes.

To use it against ordinary OPS separators, one would need a map `G -> T_G in {0,1}^N`, plus a fixed orientation, such that:

1. every graph with a perfect matching maps to an OPS-YES table, and every graph without one maps to an OPS-NO table (or vice versa), with no middle-band outputs;
2. a fan-in-two generator for `T_G` and any output processing cost `R(n)` are explicitly counted; and
3. composition with an *arbitrary*, possibly nonmonotone OPS separator produces a circuit in a class to which the matching lower bound applies.

The composition cost is sharing-safe: if `T_G` is generated in `R` gates and the separator uses `S` gates, the source predicate has an ordinary circuit of `R+S+O(1)` gates. This does not put that circuit in the monotone class.

### Proof attempt and decisive obstruction

The Rao theorem lower-bounds monotone circuits. OPS separators may use NOT gates. Even if the table generator is monotone in the graph-edge variables, the composed circuit can be nonmonotone because its separator is. There is no cost-preserving monotone simulation for arbitrary circuits that would turn this composition into a monotone matching circuit. A dual-rail encoding supplies both each edge bit and its complement; monotonicity in those independent rails does not restore monotonicity in the original edge variables, so Rao's theorem cannot be invoked.

The natural direct verifier table also fails the promise test. Encode a candidate matching as `z` using `D=Theta(n log n)` bits and let `T_G(z)` indicate whether it is a valid perfect matching of the hardwired graph `G`. This predicate has a polynomial-in-`n` circuit for every `G` (check the listed edges and that each vertex appears once). Since `N=2^D`, for every fixed `beta>0` its size is eventually below `N^beta/(cD)`. Thus the entire image is Low, whether `G` has a perfect matching or not; it supplies no High side. Complementing `T_G` does not help, since the complement also has a polynomial-in-`n` circuit and is Low at this domain scale. More generally, “matching exists” versus “no matching” does not make a simple witness-verification truth table uniformly jump past `N^beta`; every promised source instance must satisfy the required YES or NO cutoff, not just a randomly selected or worst-case subfamily.

There is also no ordinary-circuit source contradiction available here: perfect matching has polynomial-size general circuits from its polynomial-time algorithm. A valid embedding followed by an arbitrary separator yields a general circuit for matching, which is consistent with that upper bound. Exponential monotone complexity alone cannot rule it out.

**Conclusion of test.** The Rao lower bound is not a lower bound on OPS separators and the verifier encoding above is not a promise-preserving reduction. This retires this direct ordinary-OPS transfer, not the matching theorem, all possible encodings, the already-recorded native theorem, or the OPS goal. Any revived version must first prove that separator composition stays in the hard source model, or use a source with a matching lower bound for unrestricted circuits. No such source is presently available in this project.

## 5. What “the missing idea” would have to do

The evidence does not support a hidden elementary charge based on more anchors, more sensitive coordinates, or more sampled witnesses. A viable new mechanism must meet all four conditions simultaneously:

1. **Promise-forced:** it applies to every total extension of Low/High labels and uses no prescribed answer in the middle band.
2. **Sharing-aware:** its gate-growth inequality holds operation by operation for an arbitrary acyclic fan-in-two DAG with free reuse, NOT gates, and arbitrary semantic endpoints.
3. **Superlinear range:** it has a value forced by the actual Low/High predicate that exceeds `N^(1+epsilon)` for one fixed `epsilon` as `beta` tends to zero. Support and one-cut rank cannot meet this condition because their maxima are `N` and `N/2` respectively.
4. **Transfer-complete:** if it starts from another source problem, the complete table generator, address logic, postprocessor, and separator are composed in ordinary gates, and the known source lower bound applies to that exact composed model.

The research target can therefore be phrased as **reusable membership work**: prove that every DAG deciding membership in the circuit-size gap must create enough new distinguishable residual behavior after its input features are reusable. “Residual behavior” is only a target description, not a proved potential. The next attempt must define a numerical invariant on actual gate functions and prove both its bounded growth under AND/OR/NOT and its superlinear output requirement. If either inequality restates the separator lower bound or assumes that candidates are checked separately, reject it.

One concrete screening path is to analyze a candidate invariant on (i) `AND_i(x_i OR y_i)` and repeated-block equality (full-rank, linear-size outputs), (ii) parity and sparse parity-check maps (global reuse), and (iii) an explicit full-promise separator. It must survive those tests before any GapMCSP-specific proof is attempted. This is a research specification, not a theorem or a claimed breakthrough.

## 6. First-principles verdict and frontier

The cumulative work has narrowed the problem: it is not lack of examples, certificate lower bounds, input sensitivity, or proof-tree size. It is an unrestricted shared-circuit lower bound for the partial Boolean function whose required labels are exactly the Low and High truth-table sets. The OPS magnification theorem says that the desired bound would prove `NP not subseteq P/poly`. It is reasonable to push for a proof, but the project has not uncovered evidence that ZFC decidability or a short diagonal argument will make one emerge automatically. The honest missing step is currently the main complexity-theoretic obstacle itself.

**Strongest verified statement:** C-435's arbitrary-sharing cut-rank inequality and C-403/C-406's near-linear ordinary gate floor. C-436 adds no lower bound.

**Frontier unchanged:** ordinary lower bound `N-O(N^beta log N)-1` plus C-406 refinement; OPS `N^(1+epsilon)` open; exact complete separator `O(N*2^(O(N^beta)))`; native `rho>=N-o(N)` separate. No near-linear full-promise construction, no P-vs-NP proof.

### Primary literature checked

- Oliveira, Pich, Santhanam, [Hardness Magnification near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4.
- Rao, [Monotone circuit lower bounds from spread matchings](https://eccc.weizmann.ac.il/report/2026/129/), revision 5, 3 September 2026.
- Chen, Hirahara, Oliveira, Pich, Rajgopal, Santhanam, [Beyond Natural Proofs: Hardness Magnification and Locality](https://doi.org/10.1145/3538391), JACM 2022. This explains why many lower-bound techniques that extend to small fan-in oracle gates cannot yield the desired magnification consequence by direct adaptation; it is a methodological barrier, not an impossibility theorem for every route here.
