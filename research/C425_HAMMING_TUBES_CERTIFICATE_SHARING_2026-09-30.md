# C-425 - Hamming tubes are sound, but certificate multiplicity does not charge shared gates

**Status:** The low-circuit Hamming margin gives a complete semantic separator and an exact safe certificate family. It does not give a small circuit: the direct implementation still enumerates all Low tables. A linear-size population counter recognizes a sound exponential subfamily while representing exponentially many certificates through shared gates. This kills certificate multiplicity as a route to a superlinear total-gate lower bound. No quantitative frontier changes.

## 1. OPS target and threshold convention

Write `N=2^n`. Oliveira–Pich–Santhanam define `Gap-MCSP[s1,s2]` with YES tables of circuit size at most `s1` and NO tables of size **greater than** `s2`. Their Theorem 1.4 states: there is a universal constant `c>=1` such that, if there is one fixed `epsilon>0` for which, for every sufficiently small fixed `beta>0`,

`Gap-MCSP[N^beta/(c n), N^beta]` has no fan-in-two Boolean circuit of at most `N^(1+epsilon)` gates,

then `NP` is not contained in `P/poly`. The theorem counts gates; the proof instantiates the YES threshold with denominator `10n`. Circuit sizes are integers, so the exact NO convention is `CC(f)>N^beta`, equivalently `CC(f)>=floor(N^beta)+1`. The repository’s shorthand `CC>=ceil(N^beta)` differs by one gate only when `N^beta` is an integer; none of the estimates below rely on this boundary. Sources: [OPS, Theorem 1.4 and Definition 2.4](https://theoryofcomputing.org/articles/v017a011/), [published article text](https://dokk.org/library/theoryofcomputing_v017a011).

The set in the promise is not specified on the middle band. This distinction is used below: a separator may accept tables of complexity strictly between the two thresholds.

## 2. Mechanism: the Hamming tube around Low

Let `s1=floor(N^beta/(10n))`, `tau2=N^beta`, and let `L={g:CC(g)<=s1}`. There is a constant `A`, depending only on the fixed two-input gate basis, such that for every table `g` and every set `E` of `d` addresses,

`CC(g xor 1_E) <= CC(g)+A(nd+n+1)`.

**Proof.** For each `x in E`, a minterm on its `n` address bits tests whether the table input is at coordinate `x`. Shared input negations and an OR of these minterms compute `1_E` using `O(nd+n)` fan-in-two gates. XORing this correction mask with `g` costs a constant number of additional gates. This construction counts gates only; its wire and indexed-description costs are separate.

Choose `r=floor((tau2-s1)/(4An))`, decreasing it by a fixed constant if necessary. For all sufficiently large `n`, every `w` within Hamming distance `r` of a table in `L` has complexity strictly below `tau2`, by the displayed patching bound. Therefore

`T_r={w : min_{g in L} d_H(w,g)<=r}`

is the 1-set of a valid full-promise separator: it accepts every Low table and rejects every table with `CC(w)>tau2`. It is a semantic separator, not a claimed low-cost one. Its correctness uses no reconstruction of a witness by a deciding circuit.

## 3. Attempted gate charge and decisive obstruction

A proposed charge was to count safe accepting certificates separately and then charge their number to gates. This fails for two independent, exact reasons.

First, if an `S`-gate fan-in-two circuit has `v` essential inputs, its reachable gate-input graph is connected and has at most `2S` edges, so `v<=S+1`. There are only `3^v` partial assignments on those essential inputs. Hence the number of distinct 1-certificates is at most `3^(S+1)`, and a certificate-count argument alone can yield at most `S>=log_3(K)-1`. Since there are at most `3^N` partial assignments on the whole input, this generic route cannot prove a superlinear lower bound in the `N`-bit model.

Second, the following explicit shared circuit realizes exponentially many safe certificates with only linear total gates.

Set `u=floor(s1/(8n))`, which is `Theta(N^beta/n^2)` for fixed `beta>0`. Every table of weight at most `u` has a minterm DNF with at most `O(un+n)<s1` gates. Every table with at most `u` zeroes has the dual CNF and is also Low. Thus

`W_u={w: wt(w)<=u or N-wt(w)<=u}`

is entirely inside the YES set. The predicate for `W_u` is computable with `O(N)` total fan-in-two gates and `O(N)` wires: use a carry-save population-count tree. Each full adder replaces three bit signals by two, so at most `N` full adders reduce the count to `O(log N)` bits; each full adder and the final comparisons use `O(1)` and `O(log N)` gates, respectively. The dense side can count zeroes with another such tree. Fan-out, wires, and gate count are distinguished; no description-bit or construction-time cost is being relabeled as gates.

For each `u`-element support `S`, the table with ones exactly on `S` is Low. Any accepting subcube of the exact filter `1_{W_u}` that contains this table can leave free only coordinates in `S`: freeing a zero outside `S` permits an extension of weight `u+1`, which is neither sparse nor dense when `N>2u+1`. Such a cube contains at most one weight-`u` table. Therefore any subcube cover of `W_u` needs at least `binom(N,u)` cubes, yet the population-count DAG uses `O(N)` gates to recognize the entire set. For fixed `beta<1`,

`log_2 binom(N,u)=Theta(N^beta/n)`.

This is an explicit reusable computation defeating any rule that charges one gate, or a fixed positive number of gates, per safe cube/certificate. Its exponential certificate family is not a lower bound against the whole program; it refutes this mechanism.

The earlier checks remain live canaries against local charges: parity uses `O(N)` gates; repeated-block equality uses `O(N)`; `m` sparse parity checks with `L` incidences use `O(L+m)`; and simple globally generated blocks use `O(N+T)`. These checks are detailed in C-424.

## 4. Paired attempt to construct a full-promise separator

The Hamming tube gives an explicit complete construction if all Low centers are enumerated. The number `M` of distinct Low tables is at most the number of fan-in-two circuits of size `s1`, namely

`M <= 2^(O(s1 log(s1+n))) = 2^(O(N^beta))`

for each fixed `beta>0`. For each hardwired center `g`, compare `w` with `g`, count the mismatches, and accept if the count is at most `r`; OR the `M` results. A population-count threshold has `O(N)` gates per center. The resulting valid separator has `O(NM)` total gates and `O(NM)` wires; a standard indexed gate-list takes `O(NM log(NM))` description bits. Enumerating all circuit descriptions, evaluating each on all `N` addresses, and emitting the indexed gate list takes `O(NM(s1+log(NM)))` elementary construction time; duplicate truth tables may be retained. This time is not counted as gates. The middle band is accepted whenever it lies within the tube. The bound is `O(N 2^(O(N^beta)))`, the existing exact-enumeration scale, not a near-linear separator.

A stronger attempted compression, making the answer depend only on Hamming weight, is impossible. At weight `N/2` (take even `N`), the table `w(x)=x_1` is Low and has exactly that weight. The layer has `binom(N,N/2)` members, while the total number of circuits of size at most `tau2` is at most `2^(O(N^beta log N))=2^{o(N)}` for fixed `beta<1`. Thus that same weight layer contains a High table. A weight-only predicate cannot separate them. Hamming distance supplies a margin but does not reveal how to recognize all circuit-generated centers.

## 5. Barriers and originality

The Hamming patching inequality is elementary and established in this project’s prior work (C-49); the tube separator and population-count certificate counterexample are project derivations here, not claims from the literature. OPS’s theorem already uses anti-checkers and carefully charges the circuit that constructs them; it does not furnish an unconditional lower bound for an arbitrary ordinary separator. The locality barrier of Chen et al. concerns specified hardness-magnification frontiers and extensions of particular lower-bound techniques to local oracle circuits; it is not a theorem that rules out every global proof. See [Chen et al., ECCC TR19-168, Section 5](https://eccc.weizmann.ac.il/report/2019/168/download/). The recent [Goldberg-Juvekar-Kabanets result, ECCC TR26-091](https://eccc.weizmann.ac.il/report/2026/091/) studies implicit MCSP and full-support PAC learning under cryptographic and proof-complexity assumptions; its instance is a sampler circuit describing labeled examples, not the explicit length-N truth table in ordinary Gap-MCSP. It supplies no unconditional total-gate lower bound for this target. Nothing here bypasses the locality barrier or improves on OPS.

## 6. Quantitative frontier and changed target

**Strongest proved statement in this cycle:** every table within `Theta(N^beta/n)` Hamming distance of a Low table is below the NO threshold; the union of those balls is a valid full-promise separator. It has the direct enumeration upper bound `O(N 2^(O(N^beta)))`. An `O(N)` shared population counter accepts a sound Low subfamily with at least `binom(N,u)` safe certificates, proving certificate multiplicity is not a gate charge.

**No frontier change:** ordinary total-gate lower bound remains `S>=N-O(N^beta log N)-1` with C-406’s additive logarithmic refinement; the OPS `N^(1+epsilon)` target remains open. Native `rho_GapMCSP>=N-o(N)` remains separate. Exact full-promise upper remains `O(N 2^(O(N^beta)))`. No conclusion changes for paid AND states, OR operations, wires, description bits, construction time, arbitrary-endpoint native fusion, or semi-filter extensions. No P-vs-NP result follows.

**Changed next target:** retire O-245’s certificate-multiplicity route. Any new mechanism must attach cost to the *gate-to-gate computation that recognizes the whole Low family*, with an operation-wise recurrence valid under fan-out and a superlinear output requirement. It must survive the population-count counterexample and the parity, repeated-block, sparse-check, and global-relation canaries. A potential satisfying both conditions has not yet been found.