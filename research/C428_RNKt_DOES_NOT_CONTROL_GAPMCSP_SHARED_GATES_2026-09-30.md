# C-428 — Nondeterministic description complexity does not control GapMCSP gate cost

Date: 30 September 2026  
Status: a precise description-threshold mechanism is disproved on the actual OPS promise; **no circuit lower-bound frontier change**

## 1. Target and exact thresholds

Let `N=2^n`. The OPS magnification target is one fixed `epsilon>0` such that, for every sufficiently small fixed `beta>0`, every ordinary circuit separating

```text
YES: CC(f) <= N^beta/(10n)
NO:  CC(f) > N^beta
```

The target is for every such separator to have more than `N^(1+epsilon)` gates.

These strict integer endpoints match the paper's Definition 2.4: YES has size at most `s1`, NO has size strictly greater than `s2`; the first NO size is `floor(N^beta)+1`. The published theorem states this form with a universal constant `c>=1` in the YES denominator (`N^beta/(cn)`) and high threshold `N^beta`; its proof instantiates `10n`. It quantifies `exists epsilon > 0, for every sufficiently small beta > 0`, with that same epsilon. Such a lower bound implies `NP not-subset P/poly` ([Oliveira–Pich–Santhanam, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)).

The current ordinary lower frontier remains `N-O(N^beta log N)-1` plus C-406's additive logarithmic refinement. The exact full-promise separator remains `O(N 2^(O(N^beta)))` gates. Native `rho>=N-o(N)` is separate.

## 2. Candidate mechanism: charge gates through randomized nondeterministic description length

The proposed scalar potential was `kappa(f)=rnKt(f)`, the randomized nondeterministic time-bounded Kolmogorov complexity of the **entire N-bit truth-table string**. The intended bridge was:

```text
all OPS-YES tables have kappa below a threshold T(N),
all OPS-NO tables have kappa above T(N).
```

If true, it would turn the circuit-size gap into a description-complexity gap and might make shared computation chargeable through compression. The bridge is false. In fact, the two sides overlap in the reverse order by a superpolynomial margin.

### Theorem C-428

For every fixed `0<beta<1`, for infinitely many `N=2^n` there are an OPS-YES table `y_N` and an OPS-NO table `z_N` such that

```text
CC(y_N) <= N^beta/(10n),       rnKt(y_N) >= Omega(N^beta/n),
CC(z_N) >= N/n > N^beta,       rnKt(z_N) <= 2^((log N)^gamma) = N^o(1),
```

for any one fixed `0<gamma<1`. Thus neither monotone scalar threshold on `rnKt` can accept every OPS-YES input and reject every OPS-NO input. The result is about this proposed mechanism; it is not a lower bound on ordinary separator circuits.

### Proof

**High-`rnKt` YES tables.** Put `t=floor(N^beta/(40n^2))`. For every `t`-element set `A` of the `N=2^n` addresses, let `y_A` be the truth table of the OR of the `t` minterms for addresses in `A`. A minterm uses `n` literals, and the shared input negations plus the OR use at most `t(n+O(1))+O(n)` gates, which is at most `N^beta/(10n)` for sufficiently large `N`. Distinct `A` give distinct tables. Hence there are

```text
binom(N,t) = 2^(Omega(t log(N/t))) = 2^(Omega(N^beta/n))
```

OPS-YES strings.

For every `k`, at most `2^(O(k))` strings have `rnKt<=k`. To see this, fix a random tape: at most `2^(O(k))` program/time pairs of description-plus-log-time at most `k` can each uniquely specify at most one output string. If a string has `rnKt<=k`, it is specified on at least a `2/3` fraction of the tapes. Averaging the number of strings specified per tape gives the same `2^(O(k))` bound on the number of such strings. Taking `k=a N^beta/n` for a sufficiently small constant `a>0`, fewer than `binom(N,t)` strings can have `rnKt<=k`. At least one of the constructed YES tables therefore has `rnKt=Omega(N^beta/n)`.

**Very-low-`rnKt` NO tables.** Goldberg, Hu, Lu, Lyu, and Oliveira prove that for every `gamma>0` there is a sequence `x_N` with `rnKt(x_N)<=2^((log N)^gamma)` for all sufficiently large `N`, and for infinitely many powers of two `N`, `x_N` is the truth table of a function on `log N` input bits requiring ordinary circuits of size at least `N/log N` ([ECCC TR25-215, Lemma 4.22](https://eccc.weizmann.ac.il/report/2025/215/download), with oracle `O` chosen empty). Since `N/log N>N^beta` eventually for each fixed `beta<1`, these are OPS-NO tables. Also `2^((log N)^gamma)=o(N^beta/n)` for every fixed `beta>0` and `gamma<1`.

The YES counting argument gives a YES value of `rnKt` larger than the cited NO value on the same sufficiently large power-of-two lengths. Any decreasing cutoff of the intended form `rnKt<=T` that accepts that YES must accept the NO as well.

For the opposite, increasing cutoff, let `r0=rnKt(0^N)<=n+O(1)`, by printing the all-zero table in time `O(N)`. The counting bound above says only `2^(O(n))=poly(N)` strings have `rnKt<=r0`. But at most `2^(O(N^beta log N))=2^o(N)` tables have circuit size at most `N^beta`, so there are `2^N-2^o(N)` OPS-NO tables. In particular some NO table `z'_N` has `rnKt(z'_N)>r0`. An increasing cutoff that accepts `0^N` must also accept `z'_N`. This proves failure in both monotone orientations. The NO construction from Lemma 4.22 is established primary literature; the same-length promise overlap and the two cutoff obstructions are the project refinement.

## 3. Countertests for generic interaction charges

The requested shared computations are useful calibration tests. They all read the complete input and defeat gate charges based only on constraint count, support size, or repeated influence:

| Predicate on an N-bit input | Cheapest shared implementation | What it refutes |
|---|---:|---|
| Parity of all bits | `N-1` XOR gates; `O(N)` in AND/OR/NOT | Sensitivity or full-support charges |
| Equality of `k` repeated blocks of length `L` | `O(kL)=O(N)` comparisons and an AND tree | Charges per repeated coordinate relation |
| `m` sparse parity checks with `I=O(N)` total incidences | `O(I+m)=O(N)` XOR and combine gates | Charges per check or incidence |
| Blocks obeying a simple shared rule, such as copy/complement or a fixed low-cost recurrence | Compute the shared seed relation once and verify coordinates in `O(N+R)` gates, where `R` is rule cost | Charges based on expanded, duplicated descriptions |

With a basis without XOR, each XOR can be replaced by a constant-size AND/OR/NOT gadget, preserving the `O(N)` bounds. These are counterexamples to generic charging rules, not full-promise GapMCSP separators. No one of these predicates is claimed to implement the Low/High labeling.

## 4. Paired full-promise separator attempt

The rnKt-threshold separator `1[rnKt(f)<=T]` fails by Theorem C-428. A hybrid that handles low-rnKt strings by circuit-complexity search and uses the threshold elsewhere still has to resolve the same circuit-synthesis predicate on those strings; no sharing identity was found to reduce that work.

For the requested near-linear construction attempt, I instantiated the published OPS anti-checker pipeline as a conditional full-promise separator. Under `NP subseteq P/poly`, their Lemma 4.1 constructs, from the whole truth table `f`, a list of `t=2^(10 beta n)=N^(10 beta)` addresses such that if `f` is High, every size-`s1` circuit disagrees with `f` on at least one listed address. Feed the list and the corresponding input labels `f(y_i)` to a circuit for Succinct-MCSP. A Low `f` is accepted because its circuit matches every sample; a promised High `f` is rejected because the anti-checker guarantees no size-`s1` circuit matches all listed labels. The middle band needs no behavior. Exact total-gate accounting in the OPS proof is: selector `N^(1+k beta)` gates for a constant `k`; formatter plus table lookups `O(tN)=O(N^(1+10 beta))` gates; and a Succinct-MCSP circuit of size `m^ell`, where `m=N^(10 beta) poly(n)` and `ell` is the fixed exponent supplied by `NP subseteq P/poly`. Taking beta sufficiently small makes all three terms at most `N^(1+epsilon/3)`, giving a total `N^(1+epsilon)` full-promise separator. In a fan-in-two DAG, wires are O(total gates plus input/output wires); gate-list description bits and circuit-construction time are separate measures.

This is a genuine conditional construction from the primary OPS proof, not an unconditional upper bound and not a new result. Its selector is exactly where the assumed `NP subseteq P/poly` is used. The direct unconditional implementation still enumerates all Low circuits:

The explicit exact fallback is enumeration. List all `K=2^(O(s1 log(s1+n)))=2^(O(N^beta))` circuits of size at most `s1`, test equality of each output truth table with the input using `O(N)` gates, then OR the equality bits. It accepts every YES and rejects every NO. Accounting separately:

```text
ordinary total gates:     O(N K) = O(N 2^(O(N^beta)))
wires:                    O(N K)
gate-list description:    O(N K log(NK)) bits
direct construction time: separate; not counted as circuit gates
```

This is a correct unconditional full-promise separator but not a near-linear one. No `O(N^(1+o(1)))` unconditional full-promise separator or native cover was constructed in this cycle.

## 5. Model and barrier audit

The theorem and enumeration above concern ordinary fan-in-two total gates with free fanout. Wire count and gate-list description are not gate count. Native fusion's paid AND states, OR operations, endpoint encodings, wide seeds, arbitrary semantic endpoints, cycles, and every required semi-filter extension are not compiled here; no `q^2` AND-only unrolling is treated as a total-gate compiler. The native `rho` frontier is unchanged.

The locality barrier is not needed for this negative result and does not rule out arbitrary global arguments. The OPS magnification theorem remains an implication from the stated ordinary-circuit lower bound, not a proof of it. The 2025 rnKt theorem is established literature; Theorem C-428 is a straightforward promise-parameter transfer plus a counting refinement; no P-vs-NP claim follows.

## 6. Mechanism change and exact frontier effect

Retire monotone scalar Kolmogorov-description thresholds as a way to distinguish OPS YES from OPS NO. They are not a gate potential: the promise contains high-`rnKt` YES tables and low-`rnKt` NO tables, while low-`rnKt` YES tables and high-`rnKt` NO tables also exist.

The next live mechanism is a promise-preserving hard-predicate embedding, stated without requiring a separator to print descriptions or witnesses. Find an explicit map `T` and Boolean predicate `h` such that every `T(x)` is promised, the promise label equals `h(x)`, and the complete ordinary-gate accounting proves that any separator of `S` gates computes `h` with at most `R(N,S)` gates while an unconditional theorem gives `CC(h)>R(N,N^(1+epsilon))`. Direct tests already rule out the simplest versions: safe coordinate cylinders are entirely Low (C-426); linear codeword slices reduce to a zero-test (C-420); balanced block-constant slices have easy induced separators (C-419). Any successor must escape all three and prove the map/overhead inequality, not assume a particular separator algorithm.

**Strongest proved statement this cycle:** for each fixed `beta<1`, OPS-YES includes tables of `rnKt=Omega(N^beta/log N)`, while infinitely many OPS-NO tables have `rnKt=N^o(1)`; counting also supplies a high-`rnKt` OPS-NO table above the all-zero YES table's `rnKt`. Thus both monotone rnKt cutoffs fail.  
**Quantitative frontier:** unchanged: ordinary `N-O(N^beta log N)-1` plus C-406's additive logarithmic term; OPS `N^(1+epsilon)` open; exact full-promise upper `O(N 2^(O(N^beta)))`; native `rho>=N-o(N)` separate.
