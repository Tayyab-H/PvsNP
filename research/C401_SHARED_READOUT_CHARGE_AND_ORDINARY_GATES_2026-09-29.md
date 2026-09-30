# C-401 — Share-aware readout charges for ordinary Gap-MCSP circuits

Date: 29–30 September 2026  
Status: exact threshold audit and counterexample cycle; **no lower-bound improvement**

## 1. Target and magnification quantifiers

Let `N=2^n`. The Oliveira–Pich–Santhanam (OPS) theorem uses the promise

```text
YES: CC(f) <= s1 = 2^(beta*n)/(c*n) = N^beta/(c log_2 N)
NO:  CC(f) >= s2 = 2^(beta*n)       = N^beta,
```

for a universal constant `c>=1`. Its quantifiers are: if there is one fixed `epsilon>0` such that, for every sufficiently small fixed `beta>0`, no fan-in-two Boolean circuit with at most `N^(1+epsilon)` gates separates the YES and NO sets, then `NP` is not contained in `P/poly`. The middle band has no required output. The proof's anti-checker lemma and parameter choice exhibit the thresholds with `c=10`; the theorem statement permits a universal `c`. Thus the requested uniform-in-small-fixed-beta target matches the theorem. Any one beta sequence, a beta-dependent epsilon tending to zero, or a size bound on another resource does not meet it. See OPS, [Theorem 4 and Lemma 4.1](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).

OPS counts ordinary Boolean circuit gates (fan-in two, unbounded depth); it does not count wires, nonuniform description bits, or runtime as gates. Its contrapositive constructs near-linear anti-checkers assuming `NP subseteq P/poly`; that conditional upper construction is not an unconditional separator or a lower bound.

## 2. Mechanism tested: charge the shared computation of a constraint readout

Raw witness or incidence counting does not respect reuse. The candidate replacement is the following precise interface.

For a binary matrix `H` with `N` columns, let `B(H)` be the minimum number of fan-in-two AND/OR/NOT gates in a circuit that outputs the **entire** vector `Hx` over `GF(2)` on input `x in {0,1}^N`. Fanout is unrestricted and every internal gate is counted once, however many times its value is reused. This is an ordinary total-gate measure. Define `L(H)` analogously for XOR straight-line circuits; it is a narrower model and cannot silently replace `B(H)`.

A possible transfer theorem would need to exhibit, for each small fixed `beta`, a matrix `H_beta` and a restriction/relabeling of the Gap-MCSP input cube with both properties:

1. the restricted promise separator is forced to output `H_beta x` (or a relation from which all its bits can be recovered) for every separator, regardless of its internal representation; and
2. `B(H_beta) >= N^(1+epsilon+delta)` for fixed `epsilon,delta>0`, while the reduction circuit obeys `B(H_beta) <= N^delta*S + O(N)` when the separator has `S` gates. Then `S=Omega(N^(1+epsilon))`.

If these properties were proved, the conclusion would be an ordinary total-gate lower bound and OPS would apply. They are not assumptions in this report. The cycle tests whether either property follows from “many inconsistencies,” witness diversity, or local constraints. It does not.

### Proof attempt and decisive counterconstructions

The natural first claim, `gate work >= total support/incidence of the constraints`, is false even when the output must decide whether all listed constraints hold. The sharp failure is sharing a running parity: constraints

```text
p_j = x_1 XOR x_2 XOR ... XOR x_j,  j=1,...,N,
```

have total expanded input incidence `N(N+1)/2`, but all `N` parities are computed with `N-1` XOR gates by `p_1=x_1`, `p_j=p_(j-1) XOR x_j`. Their conjunction or disjunction adds only `O(N)` gates. In an AND/OR/NOT basis, each XOR costs a constant number of gates, so the ordinary total remains `O(N)`. The incidence argument is therefore defeated by a concrete unrestricted-fanout DAG.

The requested calibration families also have shared linear-size readouts:

- **Parity:** one parity of `N` bits costs `N-1` XOR gates, hence `O(N)` ordinary gates. A charge based on the number of bits involved gives no superlinear cost.
- **Repeated-block equality:** for `k` blocks of length `L`, test `x_(i,j)=x_(0,j)` for all `i>0,j` and AND the comparisons. This uses `O(kL)=O(N)` ordinary gates with unrestricted reuse of the reference block.
- **Sparse parity checks:** if there are `Theta(N)` checks, bounded row weight, and `O(N)` total incidences (as in a bounded-degree LDPC-style check system), compute every syndrome bit with `O(N)` XOR gates and combine them in `O(N)` more gates. The number of failed checks is not a gate charge.
- **Simple global block relations:** if each block is the seed block or its bitwise complement according to a known alternating block flag, recover/use the seed once and compare every coordinate against its predicted value. This takes `O(N)` gates. For a relation whose expanded equations all repeat a common parity of the seed, compute that parity once and reuse it; an apparent `Theta(N^2)` expanded support can again collapse to `O(N)` work.

These are counterexamples to additive local-incidence charging, not counterexamples to the full Gap-MCSP lower-bound program. None is claimed to encode the entire YES set.

### Does the share-aware replacement help?

Replacing incidence by `B(H)` correctly accounts for arbitrary sharing **if the computation really must output the full syndrome**. But it exposes two independent missing theorems:

* The separator has one output bit. No argument shows that an arbitrary promise separator must compute or expose all syndrome bits. Repeating the separator on many modified inputs costs many copies; that does not give the required size-preserving readout.
* Even the narrower explicit-linear-map problem is difficult. Alon–Karchmer–Wigderson note that no explicit `n x n` matrix was known to require superlinear XOR-circuit size in unrestricted depth; their `Omega(n log n)` result is for depth two. A 2025 result gives `5n-o(n)` additive complexity for an explicit GF(2) operator, still linear. A 2026 note by Raz describes proving superlinear size lower bounds for explicit linear functions as a long-standing open problem. Random matrices have large linear-circuit complexity by counting, but that does not produce a small-circuit truth-table subfamily plus a separator-to-syndrome reduction. See the [primary AKW paper](https://www.tau.ac.il/~nogaa/PDFS/Publications/Linear%20circuits%20over%20GF%282%29.pdf), [Sergeev 2025](https://www.mathnet.ru/php/archive.phtml?jrnid=mzm&option_lang=eng&paperid=14541&wshow=paper), and [Raz, ECCC TR26-008](https://eccc.weizmann.ac.il/report/2026/008/).

Moreover, `L(H)` is not an ordinary-gate lower bound: Boolean circuits may use nonlinear gates, and a proof must lower-bound `B(H)` or prove a valid conversion. We found no such conversion for arbitrary separators. The share-aware mechanism is therefore a well-defined diagnostic, but its Gap-MCSP readout lemma is unproved and its known linear examples sit exactly at the current scale. Treating either missing theorem as a “non-shareability principle” would merely rename the target.

**Changed mechanism check: a scalar zero-test for a low-dimensional linear subfamily.** To avoid the multi-output/readout gap, try making the separator's restriction equal the one-bit predicate `Zero_V(x)=1 iff x in V`, for a linear space `V` contained in the low set. This still does not furnish a uniform OPS exponent by a counting argument. There are at most `2^(O(N^beta))` low-circuit descriptions at the threshold, so any such `V` has dimension at most `O(N^beta)`. The total number of ambient `d`-dimensional subspaces is at most `2^(O(d(N-d)))=2^(O(N^(1+beta)))`. By contrast, the number of fan-in-two circuits of size `N^(1+epsilon)` is `2^(O(N^(1+epsilon) log N))`. Whenever fixed `beta<epsilon`, circuit-description entropy already exceeds this entire family of candidate zero-tests; counting cannot force any one of them above the OPS size threshold. This does **not** prove a small circuit for every `Zero_V`, or rule out a structural lower bound. It closes only the proposed entropy route and leaves the harder compatibility/readout issue intact: a useful `V` must lie inside the actual low set, and every promised high-side point used by the restriction must stay outside the middle band.

## 3. Full-promise separator attempt

There is an unconditional, explicit but enormous full-promise separator: enumerate all `K` syntactic fan-in-two circuit descriptions of size at most `s1`; hardwire each candidate's truth table; for each candidate test equality with the input truth table using `O(N)` gates; OR the `K` equality tests. This accepts every YES table and rejects every NO table (and may reject the middle band). Since

```text
log_2 K = O(s1 log(s1+n)) = O(N^beta),
```

the total Boolean gate count is `O(N 2^(O(N^beta)))`. A standard explicit gate-list encoding may use another `O(log(KN))` bits per gate to specify wire indices, so its description is at most `O(KN log(KN))` bits; description bits are not included in OPS gate size. This is a valid full-promise upper construction, but it is not near-linear and does not weaken the OPS target. Runtime for constructing the circuit is not being conflated with either resource.

The OPS conditional anti-checker construction is the known near-linear route under `NP subseteq P/poly`, with beta chosen sufficiently small as a function of the fixed target epsilon. It does not furnish an unconditional near-linear separator. No near-linear full-promise separator or native cover was constructed in this cycle.

## 4. Model audit and barriers

The present target counts total ordinary Boolean gates. It does not count wires, and free fanout is exactly why a value can be shared. Native fusion count `q`, paid AND states, free/unbounded ORs, semantic endpoint descriptions, and ordinary total gates are separate measures. In particular, the project compiler's `q^2` AND-only unfolding is **not** a `q^2` total-gate compilation when wide ORs and endpoint encodings are charged. No native-to-ordinary transfer is used here; the native full-promise frontier stays `q >= N-o(N)`.

No new native cover is claimed in this cycle. Earlier C-400 is only a subpromise construction. Any future native upper bound must use one pair list that preserves **every** required proper semi-filter extension, with arbitrary semantic endpoints, wide seeds, unrestricted reuse, and cycles; checking only YES/NO truth tables would not suffice.

The locality barrier of Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam concerns direct extensions of particular weak lower-bound techniques: magnification often yields circuits augmented with bounded-fan-in oracle gates, and some techniques also handle those local oracles. It is not a theorem that ordinary Gap-MCSP circuits of size `N^(1+epsilon)` exist, nor a barrier to every nonlocal proof strategy. See their [primary paper](https://arxiv.org/abs/1911.08297), especially the locality-barrier section. OPS's exact parameter implication remains valid.

OPS also report that the magnification-level lower bound is already known for `U2` formulas of near-quadratic size, and give a separate unconditional near-quadratic `U2`-formula lower bound for Gap-MCSP at their Theorem 1.5 parameters. This confirms substantial progress in a tree model, but a formula lower bound does not imply a lower bound for circuits with arbitrary fanout: unfolding a shared DAG can expand by depth. The distinction is exactly the resource under study here. These results are established formula bounds, not a new ordinary-circuit result. See [OPS, Theorems 1.4–1.5 and discussion](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).

**2025 distinguishers / uniform-magnification lead.** Atserias and Müller construct sparse, strongly explicit code-like distinguishers and prove a separate theorem: if, for some fixed `eta>0` and `sigma(ell)<=2^(o(ell))`, the approximate problem `N^(-eta)-MCSP[sigma]` has no `P`-uniform circuits of size `N^(1+eta+o(1))`, then `P != NP^⊕P`. They explain why this uniform result can avoid the known locality barrier. This is a useful new literature lead, but it does not instantiate the requested OPS bound:

1. At OPS parameters `s1=N^beta/(c log N)=2^(beta*n)/(c*n)` for a fixed `beta>0`, `s1` is `2^(Theta(n))`, not `2^(o(n))`; taking `beta_n -> 0` would miss the OPS quantifier.
2. The theorem concerns `P`-uniform circuits, not arbitrary nonuniform separators.
3. The approximation promise rejects every table far from the low class, whereas Gap-MCSP leaves the whole middle band unconstrained. A lower bound for this stricter approximation task does not transfer to the easier gap task without a promise-preserving reduction.

There is a useful quantitative bridge fact but not the missing reduction. If `CC(f)>=s2` and a size-`s1` circuit differs from `f` on `k` table positions, patch those positions with `k` address minterms, each of size `O(n)`. Then `s2 <= s1+O(kn)`, so `k=Omega(N^beta/n)` and the high side is far from the low class by a fraction `Omega(N^(beta-1)/n)`. Thus, for any fixed `0<eta<beta`, every high table is NO for approximation radius `N^(-(1-beta+eta))` eventually. However, the resulting `sigma=s1` still violates the distinguisher theorem's subexponential-in-`n` hypothesis, and the middle-band and uniformity mismatches remain. See Atserias–Müller, [Simple general magnification of circuit lower bounds](https://arxiv.org/abs/2503.24061) and [the primary manuscript](https://www.cs.upc.edu/~atserias/papers/magnification/magnification.pdf).

## 5. Cycle result and next changed mechanism

**Strongest proved statement this cycle:** the incidence-to-gates charging rule is false; the prefix-parity DAG is an explicit quadratic-incidence/linear-gate counterexample. Share-aware syndrome circuit complexity fixes the accounting error but does not transfer from a one-bit promise separator. The exhaustive `O(N 2^(O(N^beta)))` construction is a correct full-promise separator upper bound.

**Quantitative frontier:** unchanged. No `epsilon>0` is established for ordinary circuits, no full-promise near-linear separator/cover is known, and no P-vs-NP separation follows.

**Mechanism change:** discontinue raw witness, failed-check, support-incidence, and low-dimensional-subspace entropy charges. A viable next attempt must identify a single Boolean output predicate on a restricted Gap-MCSP subcube whose unrestricted **ordinary** circuit complexity has a proven superlinear lower bound, and prove that every promise separator restricts to exactly that predicate with only explicitly charged overhead. The immediate obstruction is not a need to count more witnesses; it is the missing all-separators restriction theorem. Keep the OPS anti-checker route separate: a decision circuit is not presumed to output a circuit description or a witness list.

No finite experiment can establish this asymptotic statement; none was run or used in the proof.
