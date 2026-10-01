# C-439 - First-principles audit: the gap is shared computation, and query costs are not additive

**Purpose and audit scope.** This cycle reviews the durable claim ledger and current synthesis through C-438, checks the recent C-436--C-438 arguments and their primary sources, and changes the next research target accordingly. It does not independently re-prove every historical report. The aim is to identify what the accumulated work forces us to conclude and what the next proof must actually establish.

## 1. Fix the target before choosing a proof

Let `N=2^n`, use total fan-in-two AND/OR/NOT gates with unrestricted fanout, and let

```text
s1 = N^beta/(c log_2 N),       s2 = N^beta,
L = {f : CC(f)<=s1},            H = {f : CC(f)>s2}.
```

`SepCC(N,beta)` is the minimum gate size of any **total** Boolean function that accepts all of `L` and rejects all of `H`; the middle band is unconstrained. The OPS magnification theorem uses one universal `c` and requires one fixed `epsilon>0` such that for every sufficiently small fixed `beta>0`, no size-`N^(1+epsilon)` circuit separates this promise. Its thresholds are `2^(beta n)/(c n)` and `2^(beta n)`, and this lower bound implies `NP not subseteq P/poly` ([OPS, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)).

This is a **sufficient route** to `P != NP`, and a stronger conclusion than `P != NP`: the reverse implication is not known. Thus the project should keep OPS as its chosen magnification target, but must not mistake it for the only logical form a P-vs-NP proof could take. A direct uniform proof that SAT is not in polynomial time would bypass this stronger nonuniform target; no such route has yet supplied a proof here.

## 2. What the cumulative record establishes

The strongest ordinary gate floor remains `N-O(N^beta log N)-1`, with C-406's additive logarithmic refinement. This essentially charges dependence on almost every truth-table bit. It does not charge the work of combining those bits after they are exposed. On the upper side, enumerate the `K=2^(O(N^beta))` descriptions `d` of Low circuits and use

```text
E_d(x) = AND_{i<N} [x_i = C_d(i)],       Sep(x) = OR_d E_d(x).
```

This accepts every Low table, rejects every High table, and leaves the middle band arbitrary, at `O(NK)=O(N*2^(O(N^beta)))` total fan-in-two gates and wires. No near-linear full-promise separator has been constructed. All C-439 composition inequalities count ordinary total AND/OR/NOT gates. Wire count/fanout, output-routing bits, gate-list description length, uniform construction time/runtime, and native fusion measures (paid AND states, OR operations, endpoints, and `rho`) are separate resources; no gate/compiler bound is inferred by conflating them.

Across C-1--C-438, support, safe cylinders, margins, anchors, certificate counts, anti-checkers, transcript fibers, cut rank, restrictions, and source reductions repeatedly constrain the promise's geometry or a restricted model. Their proved output charges stop at linear scale, fail to transfer through unrestricted sharing, or fail the exact low/high promise map. Comparator and native fusion/cyclic results remain useful in their own measures, but neither supplies an ordinary shared-DAG compiler. Parity, repeated-block equality, sparse parity-check constraints with linear incidence, and simple global block relations are mandatory attacks on any generic witness-width or incidence charge; each has a compact shared readout. This is a synthesis of ledger results, not a claim that every old proof has been re-audited line by line.

The fundamental missing object is therefore concrete: a superlinear **total-gate** lower bound for every total extension of this partial Boolean function, or a valid near-linear extension. Any proof that the separator reconstructs witnesses, checks every address separately, or preserves a particular history must establish that necessity for arbitrary DAGs; the project has not done so.

## 3. Correction to the C-438 composition interpretation

For a source computation with deterministic-control size `D_m` and adaptive queries `j`, if query `j` has a promise-preserving table generator of `R_{m,j}` gates, an OPS separator of `S_{N_j}` gates, and answer postprocessing of `B_{m,j}` gates, literal query-by-query substitution gives the valid **upper bound**

```text
D_m + sum_j (R_{m,j}+S_{N_j}+B_{m,j}).
```

If this particular circuit construction is smaller than a source lower bound, it yields a contradiction. The displayed sum is not a lower bound on all joint implementations, and it is not a necessary budget for a contradiction. A compiler can reuse gates across related queries.

This distinction is forced by a standard Boolean-circuit counterexample. By counting, some `n x n` matrix `A` over `GF(2)` has single-vector map `x -> Ax` requiring `Omega(n^2/log n)` circuit size. Yet on `n` vectors at once, `(x_1,...,x_n) -> (Ax_1,...,Ax_n)` is matrix multiplication `AX` and has an `O(n^2.38)` circuit, asymptotically below `n` copies of the single-map lower bound. Barak, Braverman, Chen, and Rao give this example explicitly ([paper](https://mbraverm.princeton.edu/files/directsum.pdf)). The example is about Boolean circuit size and directly refutes a generic copy-additivity principle. It does **not** refute the serial-substitution upper bound or any source-specific transfer whose joint structure is separately analyzed.

Consequently, C-438 remains a correct accounting lemma but not evidence that every oracle query necessarily incurs a fresh full separator cost. The project has to either prove a source-specific joint lower-cost compiler bound or stop treating query multiplicity as an unavoidable charge.

## 4. Strongest attack on the current source map

Ren and Williams prove near-maximum ordinary circuit hardness `Omega(2^m/m)` for a function in `E^{prMA}/1`; the source computation uses smart promise-MA queries that test prefix existence for a short circuit encoding a satisfying assignment ([ECCC TR26-118](https://eccc.weizmann.ac.il/report/2026/118/)). This is a promising source because its lower-bound model matches ordinary circuits. The straightforward table of local PCP-verifier outcomes has polynomial-size circuits in its query/witness parameters on both query outcomes. Whenever that circuit size is below the OPS YES cutoff, both sides map Low; this construction therefore does not encode the existential answer as a Low/High gap. It is a failure of this encoding, not an impossibility theorem for all source maps.

There is also a threshold-nesting issue: a naive encoding whose cutoff only distinguishes existence of a circuit of size at most `s` from nonexistence above `s` supplies no further soundness by itself. OPS requires a gap between `N^beta/(c log N)` and `N^beta`, a factor of order `log N`. Repeated-copy amplification cannot be assumed to bridge that factor because unrestricted circuit direct sum is false. No one-table map or source-specific joint compiler has been built, so this route remains open rather than disproved.

## 5. Revised lead: compress the whole source computation into one promise instance

The next source-transfer attempt should target a **single-table promise-preserving reduction**, not infer an additive cost for a list of oracle queries. Precisely, for a source-hard Boolean function `g_m` with `CC(g_m)>=h_m`, seek an ordinary multi-output circuit `G_m` of `J_m` total gates and a `B_m`-gate output decoder such that, for every source input `x`,

```text
g_m(x)=1  =>  CC(G_m(x)) <= N_m^beta/(c log N_m),
g_m(x)=0  =>  CC(G_m(x)) > N_m^beta.
```

The generator cannot use the unknown source answer or uncharged `prMA` oracle replies. For each sufficiently small fixed `beta`, if such a map exists, composing it with an OPS separator gives a source circuit of size `J_m+B_m+N_m^(1+epsilon)+O(1)`. The same fixed `epsilon` must work for all such `beta`; if the displayed size is below `h_m` on the source-hard lengths, it contradicts the source lower bound. This construction pays once for the joint encoding and once for the separator, automatically allowing all sharing inside the table generator. Its hardest obligation is the exact promise: **every** source YES must yield Low and **every** source NO must yield High, with the logarithmic threshold gap. This is a concrete theorem target, not a claim that an encoder exists.

Attack it immediately with the existing calibration cases and their cheapest shared readouts: parity is accumulated with `O(N)` XOR operations (each XOR has constant fan-in-two AND/OR/NOT cost); repeated-block equality compares representatives using `O(N)` gates; a sparse parity-check system with total incidence `L` can compute all checks in `O(L)` gates, hence `O(N)` when `L=O(N)`; simple copied, complemented, or linearly related blocks can be generated and checked by evaluating the shared seed/relations once. These refute generic incidence and per-block charges, not the one-table promise map. Any proposed amplification by copies must also be tested against the matrix-product direct-sum example. Any proposed local-verifier encoding must prove the NO table exceeds `N^beta`; verifier-locality or witness entropy does not do this. A counterexample to one encoding retires that encoding only, not the OPS program.

If no costed single-table map is found, the alternate direct proof obligation is unchanged but should be stated without proxy language: prove `SepCC(N,beta)>N^(1+epsilon)` for the exact promise and quantifiers, by a gate invariant whose recurrence is proved for each AND/OR/NOT operation under arbitrary fanout and whose required output value is itself proved superlinear for every total extension. The invariant must survive parity, equality, sparse checks, global block relations, and `AND_i(x_i OR y_i)`. No current candidate meets both the recurrence and output-value requirements.

## 6. Barriers, originality, and frontier

The Chen--Hirahara--Oliveira--Pich--Rajgopal--Santhanam locality barrier is a restriction on a broad family of locality-based magnification techniques, not an impossibility theorem for every global or source-specific argument ([primary report](https://eccc.weizmann.ac.il/report/2019/168/)). The direct-sum counterexample above is established literature. C-439's contribution is a correction to the interpretation of C-438 and a revised project priority, not a new asymptotic lower bound or a novel direct-sum theorem. Existing OPS thresholds and implication are confirmed against the primary paper; the Ren--Williams source claim is confirmed against its ECCC report.

**Strongest statement this cycle:** serial query substitution gives a correct circuit-size upper bound; copy-additivity is false for unrestricted Boolean circuits; the exact Low-description full-promise separator costs `O(N*2^(O(N^beta)))`.

**Quantitative frontier unchanged:** ordinary lower bound `N-O(N^beta log N)-1` plus C-406 refinement; OPS `N^(1+epsilon)` remains open with one fixed epsilon for every sufficiently small fixed beta; full-promise upper `O(N*2^(O(N^beta)))`; native `rho>=N-o(N)` remains a separate measure. No near-linear upper, new ordinary lower bound, or P-vs-NP proof was obtained.
