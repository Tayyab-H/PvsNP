# C-424 - Actual High tables still defeat local pivot extraction

**Status:** a stronger counterconstruction makes the rejected table genuinely OPS-High and the pivot circuit globally sound (it accepts no High table), while preserving the vanishing pivot probability. The construction is not a full Gap-MCSP separator because it rejects most Low tables. This shows that the pivot argument must use full Low-side completeness in addition to local endpoint behavior; computing and charging the pivot strategy would still be necessary. A second, certificate-cover counting attempt is rigorous but yields only `S=Omega(N^beta/polylog N)`, weaker than the known linear floor. No quantitative frontier changes.

## 1. Exact target

Let `N=2^n`, `s1=floor(N^beta/(10n))`, and `tau2=N^beta`, for fixed `0<beta<1`. OPS defines YES by `CC<=N^beta/(c n)` and NO by `CC>tau2`; with integer circuit sizes, the first NO size is `s2=floor(tau2)+1` (which equals `ceil(tau2)` unless `tau2` is an integer). The theorem uses a universal denominator constant `c` (the proof instantiates 10): if one fixed `epsilon>0` works so that for every sufficiently small fixed `beta>0`, `Gap-MCSP[N^beta/(c n),tau2]` has no ordinary fan-in-two circuit of at most `N^(1+epsilon)` gates, then `NP` is not in `P/poly`. See [OPS, Theorem 1.4 and Definition 2.4](https://theoryofcomputing.org/articles/v017a011/). The YES side must accept **every** table of circuit size at most `s1`; the NO side must reject every table with `CC>=s2`; the middle band is free.

## 2. Actual-High pivot counterconstruction for a sound but incomplete filter

This sharpens C-423. It uses a genuinely high table, satisfies soundness on the entire High set, and shows why the missing completeness condition cannot be omitted.

### Hard table

Choose a fixed `alpha` with `beta<alpha<1`, let `k=floor(alpha n)`, and set `m=2^k=Theta(N^alpha)`. Let `B` be the address subcube whose first `n-k` address bits are zero; thus `|B|=m`. The number of `k`-input circuits of size at most `s` is `2^(O(s log(s+k)))`. Set `s=c 2^k/k` for a sufficiently small constant c; because `log(s+k)=Theta(k)`, fewer than `2^(2^k)` functions have circuits of this size. Hence some Boolean function `q` on k bits has `CC(q)=Omega(2^k/k)=Omega(N^alpha/n)`. Define `f` to equal `q` on `B` and zero outside `B`. Restricting a circuit for `f` to the prefix defining `B` computes `q` without increasing gate count, so

`CC(f) >= CC(q) = Omega(N^alpha/n) > N^beta = tau2`

for all sufficiently large `n`. Thus `f` is genuinely OPS-High.

### Many low endpoints and one exceptional endpoint

Choose `T` to be a set of `t=floor(N^beta/(1000 n^2))` addresses outside `B`, and choose one more address `p` outside `B union T`. Let `A0` be all addresses outside `B union T union {p}`. For every `S subseteq T`, define the table `g_S` to be one on `A0 union S` and zero elsewhere; let `h` be the singleton table supported on `{p}`. There are `2^t+1` distinct endpoints.

Each `g_S` has a circuit consisting of (i) the simple prefix test for `B`, (ii) a list of at most `t+1` point tests for `T union {p}`, and (iii) at most `t` point tests for `S`. A point test on `n` input bits costs `O(n)` fan-in-two gates. Thus `CC(g_S)<=O(tn+n)<s1`; also `CC(h)=O(n)<s1`. The endpoint entropy is `log |L|=t+o(1)=O(N^beta)`.

### A linear-size filter and its pivot law

On an arbitrary input table `w`, set

`C(w) = [AND_{a in A0} w_a  AND  NOR_{b in B} w_b  AND  NOT(w_p)]  OR  [w_p AND NOR_{i != p} w_i]`.

This uses `O(N)` total gates and wires, and its accepting set is exactly `L`. An indexed gate-list description takes `O(N log N)` bits and can be generated in `O(N log N)` time; neither is being counted as gates. Every accepted table is Low: the first branch fixes all coordinates except `T`, so it has a circuit of size `O(tn+n)<s1`; the second branch accepts only `h`. Consequently `C(w)=0` for every OPS-High table, not just for `f`.

Now walk from `f` to a uniformly chosen endpoint in `L={g_S:S subseteq T} union {h}` by flipping the differing coordinates in a uniformly random order. For a generic endpoint `g_S`, let `b=|supp(q)|<=m` and `a=|A0|=N-m-t-1`. The second branch is disabled along the path because `p` stays zero. The first branch becomes true when the last of its required changes has occurred: all `a` coordinates in `A0` have changed from zero to one and all `b` one-coordinates of `q` in `B` have changed to zero. The pivot is the last coordinate among these `a+b` required positions, hence

`Pr[pivot in B | endpoint g_S] = b/(a+b) <= m/a = O(N^(alpha-1)).`

For endpoint `h`, the pivot lies in `supp(q) union {p}=D_h`, so it is hit with probability one. Averaging over the `2^t+1` endpoints gives

`Pr[pivot in D_h] <= O(N^(alpha-1)) + 1/(2^t+1) = o(1).`

Thus even an actual-High table, a globally sound `O(N)` circuit filter, low endpoints of OPS size, and a uniform random path do not force a constant anti-checker probability.

**Exact limitation:** `C` is not a Gap-MCSP separator. For example, it rejects `0^N`, which is Low. It proves that actual High hardness plus global soundness is insufficient for pivot coverage; a valid separator's completeness on the *entire* Low class is the remaining condition. It is not a counterexample to OPS magnification or to a theorem that uses full completeness.

## 3. Repeated pattern tests and gate accounting

| Pattern | Cheapest relevant shared computation | Consequence for a gate charge |
|---|---|---|
| Parity | `N-1` XOR operations, `4N+O(1)` AND/OR/NOT gates, `O(N)` wires; indexed description `O(N log N)` bits. | Expanded prefix incidences do not count total gates. |
| Repeated-block equality | For `N=kd`, compare each block to one shared representative and OR the mismatches: `O(N)` gates/wires. | Repeated copies do not require independent comparison circuits. |
| Sparse parity checks | `m` checks with `L` incidences use `O(L+m)` gates/wires, including the syndrome reduction. | Per-check or per-incidence charges need to account for shared parity DAGs. |
| Simple global block relations | Compute `T` seed-transform gates once, compare all `N` positions using shared predictions: `O(N+T)` gates/wires. | Reusing one global relation across blocks is real gate sharing. |

These do not recognize the full `SIZE(s1)` set and are not full-promise separators. `C` above is itself an `O(N)` sound filter for a structured low subfamily, not a solution to the full promise.

## 4. Second mechanism attempted: certificates as a subcube cover

For any valid separator `C`, every accepting computation has a 1-certificate: a partial assignment to input table bits that forces `C=1`. Its cylinder is contained in `C^{-1}(1)`, which by High-side soundness lies inside `SIZE(<s2)`. Circuit counting gives

`|SIZE(<s2)| <= 2^(O(s2 log(s2+n))) = 2^(O(N^beta n))`.

Therefore every such accepting cylinder has at most `O(N^beta n)` free coordinates and fixes at least `N-O(N^beta n)` table bits. This is a real structural constraint on every separator certificate, with no assumption on a witness description or a particular decision algorithm.

It does not yield superlinear gates. A size-`s1` subfamily `G` of size `2^(Theta(N^beta/n^2))` can be obtained by taking arbitrary truth tables on `k0` variables with `(k0+1)2^k0 <= s1/4`, lifting them to `n` variables, and retaining an error-correcting subcode of relative distance at least `1/4`. Each member has a minterm DNF below `s1`, and any accepting cylinder of dimension `O(N^beta n)=o(N)` contains at most one member of `G`. Hence at least `|G|` distinct 1-certificates are needed. But a circuit with `S` fan-in-two gates depends on at most `S+1` input coordinates, so it has at most `3^(S+1)` distinct partial assignments on its essential inputs. This gives only

`S >= Omega(log |G|) = Omega(N^beta/n^2)`,

far below the established `N-o(N)` scale. The obstruction is exact: certificate width is nearly `N`, but the forced Low family has only sublinear description entropy; certificate counting alone cannot charge repeated DAG work.

## 5. Paired complete-separator attempt

The sound filter `C` may be ORed with the exact Low-membership circuit obtained by enumerating every Low circuit description and comparing its full truth table to `w`. This is complete and sound on the full promise, but `C` adds no coverage because its accepted set is already contained in Low. With `M=2^(O(N^beta))` distinct Low tables, exact enumeration costs `O(NM)=O(N 2^(O(N^beta)))` total gates and wires. Description bits and time to construct the circuit are separate. No near-linear full-promise separator was constructed.

## 6. Literature and originality audit

- The OPS fixed-`epsilon`/small-fixed-`beta` quantifiers and `N^beta/(c n)` to `N^beta` thresholds are as stated in the primary theorem. The project has not improved them.
- The locality barrier of Chen et al. is technique-specific; this path argument is nonlocal and the counterexample neither bypasses nor strengthens that barrier. See [ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/).
- The 2026 result on implicit Gap-MCSP and full-support PAC learning is conditional and takes a sampler circuit as input; it is a different input model from an explicit truth table and supplies no ordinary total-gate lower bound here. See [Goldberg, Juvekar, and Kabanets, ECCC TR26-091](https://eccc.weizmann.ac.il/report/2026/091/).
- Hirahara and Nanashima's 2026 sharp Pessiland characterization studies agnostic-learning approximation and identifies partial MCSP as a future question; it does not establish a lower bound for the ordinary full-truth-table Gap-MCSP separator. See [ECCC TR26-052](https://eccc.weizmann.ac.il/report/2026/052/).
- The high-table construction and incomplete sound filter are project constructions. They are not claimed as a published result or a valid full Gap-MCSP separator.

## 7. Frontier and changed next target

**Strongest proved change:** the C-423 first-pivot failure persists with an actual OPS-High table and a globally sound `O(N)` filter that accepts `2^t+1` Low tables; the pivot probability for one Low table is `O(N^(alpha-1))+2^-t=o(1)`. The construction fails exactly full Low completeness. A separate certificate-cover proof extracts large accepting cylinders but gets only `Omega(N^beta/n^2)` from raw certificate entropy.

**Changed next target:** retire endpoint-path pivots unless the mechanism can use complete Low coverage as a mathematical resource. The next direct formulation is the gate cost of a *sound-complete subcube-cover DAG*: its 1-certificates must cover every table in `SIZE(s1)`, while every certificate cylinder stays inside `SIZE(<s2)`. Any proof must charge how the DAG generates and reuses those certificates, beyond their count or width. Test any proposed charge against the four shared patterns above; do not assume certificates are disjoint.

**Quantitative frontier unchanged:** ordinary total-gate lower bound remains `S>=N-O(N^beta log N)-1` with C-406's additive logarithmic refinement; OPS `N^(1+epsilon)` open. Native `rho_GapMCSP>=N-o(N)` remains separate. Exact unconditional full-promise upper remains `O(N*2^(O(N^beta)))`. No paid-AND, OR-operation, wire, description-bit, runtime, arbitrary-endpoint, cycle, or semi-filter-extension bound changes. No P-vs-NP result follows.
