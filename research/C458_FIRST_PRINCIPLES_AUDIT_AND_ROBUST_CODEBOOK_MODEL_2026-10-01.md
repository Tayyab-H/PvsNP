# C-458 — First-principles audit and robust codebook model

**Date:** 1 October 2026  
**Scope:** cumulative ordinary Gap-MCSP work through C-457, with a focused primary-literature check.  
**Status:** one elementary robustness lemma and a research-model update; no new superlinear lower bound, no near-linear full-promise separator, and no P-vs-NP proof.

## 1. The exact mathematical target

Let `N=2^n`, and let `CC(T)` be the minimum number of fan-in-two AND/OR/NOT gates computing the `n`-input function whose truth table is `T`. For the OPS thresholds

```text
s1 = 2^(beta*n)/(c*n) = N^beta/(c log_2 N),
s2 = 2^(beta*n)        = N^beta,
```

the promised YES tables have `CC(T)<=s1` and promised NO tables have `CC(T)>=s2` (with the paper's integer-rounding convention). A valid separator is an arbitrary total Boolean circuit `F` on the `N` table bits satisfying

```text
{T : CC(T)<=s1}  subseteq  F^(-1)(1)  subseteq  {T : CC(T)<s2}.
```

Its answer on the middle band is free. OPS prove that if there is one fixed `epsilon>0` such that, for every sufficiently small fixed `beta>0`, this promise has no fan-in-two circuit of size at most `N^(1+epsilon)`, then `NP` is not contained in `P/poly`. The paper has a universal constant `c` and instantiates `c=10` in the proof. This is a sufficient route to `P != NP`, and its conclusion is stronger than `P != NP`; it is not an equivalence. [OPS, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)

The quantity the direct route must lower-bound is therefore the **minimum total-gate complexity over every total extension of this partial function**. A proof for only the canonical cutoff, a sound one-sided test, or a particular algorithm does not suffice.

## 2. What the cumulative project has actually proved

### Essential-input floor

If `F` ignores `r` table coordinates, fix any promised YES table `T`. Flipping any subset of those `r` coordinates leaves `F(T)=1`; none of the resulting `2^r` distinct tables can be promised NO. Circuit counting gives at most `2^(O(s2 log(s2+n)))=2^(O(N^beta log N))` tables of circuit size below `s2`. Hence

```text
r = O(N^beta log N),       E(F) >= N-O(N^beta log N),
```

where `E(F)` is the number of essential table inputs. This is a proof about the whole promise, but it prices input dependence, not the gates that combine those inputs.

### Reconvergence refinement

C-406 unfolds the output-ancestor DAG into a De Morgan formula, charging a factor `2^mu` where `mu` is the gate-to-gate cycle rank. The published OPS formula lower bound then forces `mu=Omega(log N)` for near-linear separators and yields `S >= E(F)+gamma log_2 N-O(1)` for fixed `beta<1/2` and `gamma<1-2 beta`. This is sharing-aware, but its total-gate gain is additive logarithmic. It does not approach `N^(1+epsilon)`.

### One-sided sound tests are cheap

C-457 gives an explicit `O(N log N)` circuit that rejects every actual High table and accepts all sufficiently sparse/co-sparse tables and an entire low-degree Reed-Muller family. It has all `N` inputs essential, a sparse one-set, and ANF degree `N-O(N^beta log N)`. Yet it rejects the Low function

```text
g(x) = AND_(j=1)^(d+1) (x_(2j-1) XOR x_(2j)),
```

which has `O(n)` gates and lies outside the accepted subclasses. This is not a counterexample to the OPS lower bound. It demonstrates that soundness, essentiality, support size, degree, and a menu of broad Low families do not supply completeness for every small circuit.

### Exact full-promise upper bound

Enumerating all `M=2^(O(s1 log(s1+n)))=2^(O(N^beta))` descriptions of size at most `s1`, comparing each candidate truth table with all `N` input bits, and OR-ing the equality tests gives a full-promise separator of `O(N 2^(O(N^beta)))` total gates. This is a valid complete upper bound; its wires, description size, and construction time are separate resources. No near-linear full-promise separator has been produced in this project.

## 3. A precise robustness lemma: thickened codebooks

Let `dist(T,T')` be Hamming distance between truth tables. There is a universal constant `K` such that

```text
|CC(T)-CC(T')| <= K (n+1) dist(T,T').
```

**Proof.** If `T` and `T'` differ at `r` addresses, take a circuit for either one and toggle those `r` output locations. A minterm recognizing one fixed `n`-bit address costs `O(n)` fan-in-two gates; XORing or otherwise toggling the `r` minterms costs `O(r)` additional gates. This gives `CC(T')<=CC(T)+K r(n+1)`. Reversing the roles gives the absolute-value bound.

Consequently, for sufficiently large `n`, every valid separator is forced to accept the whole Hamming neighborhood of a safely smaller Low core and reject the whole neighborhood of a safely larger High core. For example, with constants chosen from `K`,

```text
B_floor(s1/(4K(n+1)))({T : CC(T)<=s1/2})  subseteq F^(-1)(1),
B_floor(s2/(2K(n+1)))({T : CC(T)>=2s2})  subseteq F^(-1)(0).
```

The inequalities follow directly from the patching bound: a table in the first ball has circuit size at most `s1`, and one in the second ball has circuit size greater than `s2`.

This reframes the promise as **robust membership in a succinct circuit codebook**. It is an exact implication of the promise, not a lower-bound mechanism yet. Ball volume, number of centers, or local repair multiplicity cannot be converted into total DAG gates without an additional proved operation-wise charge. Parity, repeated-block equality, sparse parity checks, and simple global block relations remain linear-size shared counterchecks to generic constraint-count arguments.

## 4. First-principles diagnosis of the stalled approaches

The attempts differ in tools, but the missing step is stable:

1. Counting, support, algebraic degree, certificate counts, anchors, transcript fibers, communication ranks, and local repair counts describe the promise or a representation of it. None so far gives a superlinear lower bound on the total gates of an arbitrary shared AND/OR/NOT DAG.
2. A one-bit separator is not required to reconstruct a circuit description, enumerate witnesses, reveal caller history, or check addresses one at a time. Those are properties of proposed algorithms, not consequences of promise correctness.
3. Source reductions fail unless both promise endpoints hold and the full generator, table-side decoder, separator, router, and postprocessor costs leave a hardness margin. Cheaply decodable tables often spend the source hardness needed for the contradiction.
4. Restricted measures and native fusion counts do not become ordinary total-gate bounds without an explicit compiler inequality.
5. C-457 makes the quantifier failure concrete: a sound recognizer can be exceptionally simple while omitting even an explicit Low circuit. The universal `for every size-s1 circuit` completeness condition is doing the real work.

The project should stop searching for an unproved scalar called “non-shareability.” A surviving direct mechanism must specify a potential `Phi(F)`, prove `Phi(F)<=a*CC(F)+b` for every fan-in-two DAG with unrestricted reuse, and prove `Phi(F)>=N^(1+epsilon)` for every valid extension. A source mechanism must instead prove exact endpoints and a composition budget with a strict superlinear source-hardness margin. Until one side of one of these inequalities is proved, it is a conjectural lens, not progress on the exponent.

## 5. Literature check and scope of barriers

- OPS Theorem 1.4 has exactly the common-fixed-`epsilon`, every-sufficiently-small-fixed-`beta` quantifiers used above. Its Theorem 1.5 gives a near-quadratic formula lower bound, matching why the project’s formula-to-DAG transfer gains logarithmic reconvergence but not a superlinear total-gate floor. [OPS PDF](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)
- The locality barrier is method-specific: certain magnification problems have small circuits with small-fan-in oracle gates, so lower-bound techniques that continue to hold in those oracle models cannot simply be magnified. It does not rule out every ordinary-circuit proof. [Chen et al., ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/download)
- The natural-proofs barrier is not a blanket obstruction here. OPS discuss how magnification can bypass that barrier in relevant settings; the decisive problem remains proving the required circuit lower bound for the promise.
- A relevant 2025 primary preprint proves the total `XOR`-Simple Extension problem is in polynomial time under the studied gate measures, extending the known ease of `OR`-Simple Extension. This independently supports C-452’s conclusion that exact simple-extension recognition is not itself an OPS gap amplifier. It does not rule out other source reductions. [Carmosino, Dang, and Jackman, arXiv:2511.16903](https://arxiv.org/abs/2511.16903)

## 6. Research direction and decision

The genuine missing object is not an undiscovered fact about parity or an omitted cost of an address check. It is a theorem about **residual shared computation for robust circuit-codebook membership**, or a cheaper exact decision procedure for that membership problem. The project has not found either.

The most useful model update is therefore:

> **Robust codebook boundary model.** A separator must accept neighborhoods of all safely small circuit tables and reject neighborhoods of all safely large circuit tables. The only useful lower-bound evidence is a property of the complete shared computation that distinguishes these two thickened codebooks and has a proved total-gate charge. Local structure may generate counterexamples and restrictions, but is not itself the charge.

This is a research hypothesis/organizing model, not a theorem that the boundary has high circuit complexity. I recommend using it to screen future work, while keeping the OPS direct target as a proxy rather than treating it as the only possible route to `P != NP`: OPS’s conclusion is the stronger `NP not subseteq P/poly`. Do not add another code family or another scalar statistic unless it produces either an operation-wise gate inequality or a full-promise construction.

**Strongest proved statement this audit:** `CC(F)>=N-O(N^beta log N)` with C-406’s additive `Omega(log N)` reconvergence refinement, plus the exact thickened-codebook containment above.  
**Paired upper:** exact full-promise enumeration `O(N 2^(O(N^beta)))`.  
**Quantitative effect:** none. OPS’s common-fixed-`epsilon` lower bound, native `rho>=N-o(N)`, a near-linear unconditional full-promise separator, and `P != NP` remain open.
