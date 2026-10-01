# C-451 - signed-rail monotone lift: exact sharing control, no new lower bound

**Date:** 1 October 2026  
**Question:** Can monotone-circuit methods control an ordinary Gap-MCSP separator while preserving unrestricted DAG reuse?  
**Result:** An exact constant-factor translation is proved. The legal signed encodings form an antichain, so monotonicity alone supplies no forced relation between Low and High labels. The lift is a useful model normalization, not a lower-bound mechanism. No quantitative frontier changes.

## 1. Exact mechanism and gate accounting

Use fan-in-two AND/OR gates, unary NOT gates, free wires/fan-out, and free constants. Let an ordinary separator `F` have `A` AND gates, `O` OR gates, and `U` NOT gates. Replace every ordinary signal `v` by a pair `(v+,v-)`, intended to represent `(v, NOT v)`. The input variables are the `2N` independent rails `x_i+`, `x_i-`.

For each source gate use the following monotone construction:

| Source gate | Positive rail | Negative rail |
|---|---|---|
| `v = a AND b` | `a+ AND b+` | `a- OR b-` |
| `v = a OR b` | `a+ OR b+` | `a- AND b-` |
| `v = NOT a` | `a-` | `a+` |

The NOT row swaps wires and creates no gate. Induction over a topological order proves that on every legal encoding
`e(T) = ((T_i, 1-T_i))_{i=1}^N`, the positive output of the resulting monotone circuit `G` is `F(T)`. Fan-out is preserved: every source node remains one shared pair of nodes; no tree unfolding or recomputation is used.

The construction uses exactly `A+O` monotone AND gates and `A+O` monotone OR gates, hence `2(A+O) <= 2 CC(F)` internal gates. It uses zero NOT gates. Conversely, a monotone circuit with `M` internal AND/OR gates on the signed rails becomes an ordinary circuit on `N` table inputs by generating the `N` negative rails with at most `N` NOT gates, so its ordinary cost is at most `M+N`. Wires, fan-out, circuit-description bits, and construction runtime are separate measures; none is silently charged as a gate.

For the promise, define `SepCC(N,beta)` as the minimum ordinary size of a total extension satisfying `L_s1 subseteq F^-1(1) subseteq L_s2`, and define `SepMC_signed(N,beta)` as the minimum monotone internal-gate count on signed rails whose values on legal encodings satisfy the same inclusions. Then

```text
SepMC_signed(N,beta) <= 2 SepCC(N,beta)
SepCC(N,beta) <= SepMC_signed(N,beta) + N.
```

Thus a signed-rail lower bound above `2 N^(1+epsilon)` would imply the ordinary OPS lower bound at exponent `epsilon`; an ordinary lower bound above `N^(1+epsilon)` gives a signed-rail lower bound above `N^(1+epsilon)-N`. Constant factors and the additive `N` do not change existence of a fixed positive exponent. This precisely preserves the relevant shared-computation measure, but does not itself improve it.

## 2. Why the monotonicity route stalls

The set of legal encodings is an antichain in the coordinatewise order on `{0,1}^{2N}`. If `T != U`, choose a coordinate where they differ. One encoding has rail pair `(1,0)` and the other `(0,1)`, so neither full encoding is coordinatewise below the other. Therefore any assignment of Boolean labels to legal encodings is consistent with some monotone function: take the upward closure of the encodings labeled 1. Monotonicity imposes no order constraint between any distinct legal tables, including a Low table and a High table.

There is a concrete monotone extension: for each distinct table `T` in `L_s1`, form the minterm
`m_T = AND_i (x_i+ if T[i]=1 else x_i-)`, and output `OR_{T in L_s1} m_T`. On legal encodings this accepts exactly `L_s1`, so it accepts every required YES and rejects every required NO. It is a full-promise separator. The straightforward unshared DNF implementation uses `Theta(N |L_s1|)` gates; the known sparse-support count makes this superpolynomial for every fixed beta, but this is only the cost of this implementation, not a lower bound on other extensions. The example exhibits the issue: order-theoretic monotonicity is free on the legal slice; only circuit size of the chosen extension remains hard.

Known monotone lower bounds cannot be imported merely because of this lift. A source map `x -> e(T_x)` usually makes the negative rails `1-T_x[i]` nonmonotone in the source variables. The composition of a monotone signed-rail separator with that map need not be monotone in source inputs. In particular, Rao's exponential monotone lower bound for bipartite perfect matching does not constrain an arbitrary ordinary separator without a promise-preserving map and a monotonicity-preserving composition; the project's C-436 matching transfer already identifies these missing conditions. The locality barrier for hardness magnification is technique-specific and is not a blanket obstruction, but this lift does not evade it or produce the needed ordinary-gate charge. [Rao, ECCC TR26-129, revision 5](https://eccc.weizmann.ac.il/report/2026/129/), [Chen et al., ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/).

## 3. Adversarial canaries: cheapest shared computations

These examples test proposed generic charges. None is a counterexample to the full Gap-MCSP separator requirement.

* **Parity:** parity of `N` table bits uses `O(N)` AND/OR/NOT gates by replacing each XOR with `(a AND NOT b) OR (NOT a AND b)`. The signed-rail lift costs at most twice the source AND/OR count. A claim that negative information or global dependence alone forces superlinear monotone work fails.
* **Repeated-block equality:** compare paired bits using `(a AND b) OR (NOT a AND NOT b)`, then AND the comparisons. Two blocks of length `m` cost at most `6m-1` gates. Shared block structure does not force extra cost per address beyond linear.
* **Sparse parity-check systems:** for total incidence `I` across `q` checks, each weight-`d` parity costs at most `5(d-1)` gates and combining the checks costs `q-1`; total is `O(I+q)`. If `I=O(N)`, consistency is decided in `O(N)` gates.
* **Simple global block relations:** divide the `N` input bits into blocks and require each coordinate to obey a fixed relation of arity at most `d`. Checking all listed relations costs `O(I+q)`, where `I` is their total incidence and `q` their number; if the relation system has `O(N)` total incidence, the checker has `O(N)` gates. This includes repeated blocks and blocks obtained by coordinatewise XORs of a bounded number of seed blocks.

The strongest obstruction here is structural rather than a finite counterexample: every legal signed codeword is incomparable, and the monotone DNF gives a valid exact extension for the actual promise. The canaries then rule out only charges from parity, local consistency, or simple global structure. They do not rule out a new lower bound exploiting the circuit-codebook geometry.

## 4. Paired full-promise separator attempt

The exact separator `F_enum(T)=1` iff some circuit description `d` of size at most `s1` computes `T` is full-promise correct: it accepts every Low table and rejects every table of complexity greater than `s2` (indeed every table not in `L_s1`). There are at most `D=2^{O(s1 log(N+s1))}` such descriptions. For each description, compare all `N` table bits with its output table and OR the resulting equality tests. A direct fan-in-two implementation costs `O(ND)=O(N 2^{O(N^beta)})` gates for fixed `beta`; the signed-rail monotone DNF above gives the same scale. Sharing identical subcomputations may improve particular instances, but no bound compressing this full enumeration to near-linear size is proved. This is an explicit full-promise construction attempt, not evidence that the enumeration bound is optimal.

## 5. Quantifiers, literature, and exact status

For `N=2^n`, the OPS theorem uses `s1=2^(beta n)/(c n)=N^beta/(c log_2 N)` and `s2=2^(beta n)=N^beta`, with one universal `c>=1`. Its trigger is a single fixed `epsilon>0` such that for every sufficiently small fixed `beta>0`, the promise problem has no circuits of size `N^(1+epsilon)`; it implies `NP not-subset P/poly`. The same epsilon must survive as beta decreases. [Oliveira, Pich, Santhanam, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf).

The signed-rail transform is an elementary exact simulation, not a new monotone lower-bound method. The literature does contain strong monotone lower bounds, including the 2026 spread-matching theorem, but they apply to a monotone source function. The signed promise slice has no order structure among legal points, and arbitrary source composition can reintroduce NOT dependence. The CHOPRS locality result rules out specified locality-based magnification adaptations, not all direct, nonlocal, or promise-specific arguments. No result found here yields the required common-fixed-epsilon lower bound.

**Strongest proved statement in this cycle:** arbitrary sharing is preserved by an exact signed-rail monotone lift with internal-gate blow-up at most 2, and the promise becomes a monotone extension problem on an antichain. **Failed transfer:** the antichain means monotonicity itself forces no Low/High relation; existing source monotone lower bounds do not transfer. **Frontier:** unchanged. The ordinary bound remains `N-O(N^beta log N)-1`, with C-406's logarithmic reconvergence refinement; the common-fixed-epsilon OPS bound remains open; the exact full-promise upper remains `O(N 2^{O(N^beta)})`; native `rho >= N-o(N)` remains a separate measure. No P-vs-NP result follows.

## 6. Next research action

Retire signed-rail monotonicity as a standalone route. Reuse it only if a future construction supplies a monotone source map whose legal table encodings preserve source order and satisfy both exact Gap-MCSP endpoints, or if a new signed-slice lower-bound technique proves a size lower bound beyond the equivalent ordinary-circuit problem. Otherwise return to the primary target: a directly proved property of every total extension that charges reusable AND/OR/NOT gates superlinearly, or an unrestricted-circuit hard source with a fully costed promise map. The route must quantify all output semantics, gate types, fan-out, and generator cost; counts of witnesses, discrepancies, or clauses remain insufficient.
