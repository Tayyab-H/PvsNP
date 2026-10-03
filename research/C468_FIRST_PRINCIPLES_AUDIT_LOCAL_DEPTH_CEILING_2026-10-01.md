# C-468 - first-principles audit: local decision depth cannot see post-read gate work

**Status:** exact model reduction and a proved limitation of the local-depth route. No new ordinary circuit lower bound, no near-linear full-promise separator, and no change to the P-vs-NP frontier.

## 1. Exact target

Write `N=2^n`, `s1=floor(N^beta/(10n))`, and `s2=N^beta`. A separator is any total fan-in-two AND/OR/NOT circuit `F:{0,1}^N->{0,1}` satisfying

```text
CC_n(T)<=s1  => F(T)=1,
CC_n(T)>s2   => F(T)=0.
```

The middle band is unconstrained. Equivalently, with `L={T:CC_n(T)<=s1}` and `R=F^{-1}(0)`, `R` is disjoint from `L`, and `F` must reject every table above `s2`. Circuit counting gives `|L_{s2}|<=2^{O(N^beta n)}`, so a uniform table is High with probability `1-2^{-N+O(N^beta n)}`. The direct unresolved quantity is the minimum **total gate count** over all such extensions, with arbitrary DAG reuse.

## 2. A precise local-state mechanism, and its proved limit

An `ell`-local semi-oblivious decision tree has a fixed set `A_i` of at most `ell` input coordinates at each level `i`; the query at that level may depend on the prior answers but is a Boolean function of `x|_{A_i}`. This is the decision-tree view of Valiant's sequential intermediate-bit model: each new state bit can use all earlier state bits and a fixed small set of raw input bits.

Every `S`-gate fan-in-two circuit computing a one-bit function `R` gives a semi-oblivious 2-local tree of depth at most `S+1`: topologically order the gates; at level `i`, query the value of gate `i`. Once prior gate outputs are fixed along a path, this query is a function of the at most two primary-input coordinates entering that gate. A final level reads the output if needed. Fan-out is preserved as access to all earlier state bits. Thus a lower bound `D` on the minimum depth of such trees implies `S>=D-1`.

There is a direct Low-completion adversary bound. Along any feasible path of depth `d`, all query answers constrain at most `q<=2d` distinct table coordinates. Choose any assignment to those coordinates satisfying the path's local constraints. A minterm DNF realizes those `q` prescribed table bits with at most `q*n+n+O(1)` gates: share the negated address literals and use one address minterm per prescribed one. Hence, if `2dn+n+O(1)<=s1`, a Low truth table follows that same path. No accepting path of a tree computing `R` can then have that depth, because `R` rejects every Low table. Therefore

```text
depth(semi-oblivious 2-local tree for R) > (s1-n-O(1))/(2n)
                                      = Omega(N^beta/n^2).
```

This path argument is valid under adaptive choice of the local Boolean query: feasibility supplies a satisfying assignment on the union of queried coordinates, and the interpolating Low table reproduces every query answer on the path.

**Why this does not control superlinear gates.** Every Boolean function of `N` variables, including every separator, has an oblivious 1-local coordinate-query tree of depth at most `N`: query all input bits, then label the leaf with the output. Thus decision-tree depth on the separator's actual `N` input bits can never exceed `N`. The local-tree simulation forgets the cost of the final leaf decoder and duplicates shared circuit states across exponentially many paths. It cannot certify an `N^(1+epsilon)` gate lower bound. The interpolation bound above is also dominated by the existing `N-o(N)` gate floor.

## 3. Counterconstruction and model check

The cheapest shared computations defeat any charge based only on how many local constraints, input incidences, or read steps appear:

* `PARITY_N` uses `N-1` XOR gates (or `O(N)` AND/OR/NOT gates) and has a coordinate-query tree of depth `N`.
* Repeated-block equality and sparse parity checks combine many local constraints with `O(N)` total gates when their total incidence is `O(N)`.
* Simple globally generated block relations can compute all block features once and reuse them, again at linear total cost for linear-size generators.

These are tests of generic charges, not full-promise separators: none accepts every Low truth table and rejects every OPS-High table. `AND_N` is a still simpler calibration: it has a depth-`N` coordinate tree and `N-1` gates. So a near-maximal local depth bound only reaches the linear scale.

The paired full-promise construction attempt remains exact Low-circuit enumeration. There are `K=2^{O(N^beta)}` Low descriptions; evaluating and comparing candidate truth tables gives `O(NK)` ordinary gates in the direct implementation. Repeated circuit fragments may be shareable, but no worst-case compiler reducing this to `N^(1+o(1))` is proved. The upper attempt still handles every promised YES and NO; its cost is exponential in `N^beta`.

### Resource accounting

| Resource | Accounting in this cycle |
|---|---|
| Ordinary total gates | `S` counts every AND, OR, and NOT gate in the actual separator. This is the OPS measure. |
| OR operations | Included in `S`; no OR tree or branch merge is free. |
| Reusable circuit states | A topological listing has at most one state bit per gate, `t=S`. Fan-out lets later gates reuse earlier bits. The decision-tree depth is not the number of tree nodes. |
| Local-tree paths/leaves | Not ordinary circuit gates. The tree can have exponentially many nodes, and its leaf labels can encode the full truth table of the output function. |
| Wires/fan-out | Uncharged by the standard total-gate measure. The real DAG uses at most two incoming gate pins per fan-in-two gate; arbitrary fan-out is permitted. |
| Description bits | Not gates. The count `K=2^{O(N^beta)}` refers to low-circuit descriptions; describing a particular gate DAG takes additional bits but does not change its gate count. |
| Runtime/materialization | Not the circuit-size measure. The direct enumerator's `O(NK)` is a gate upper bound; a RAM/runtime claim alone would not imply it. |
| Native paid-AND states `rho` | A separate fusion/least-fixed-point model. No compiler from this 2-local tree or its depth to `rho` is established. |

The local-tree proof is therefore only a lower-bound transfer through a *relaxation*: it can show a minimum tree depth is no greater than the circuit's gate count, but it does not preserve the cost of all distinct path nodes or the circuit's post-read decoder. A proposed quadratic paid-AND unrolling, if used in a later native argument, would not be an ordinary total-gate compiler without a separate construction and wire/OR accounting.

## 4. Literature transfer audit

Golovnev and Gurumukhani, ECCC TR26-195 (19 September 2026), prove strong lower bounds for **oblivious** local decision trees. Their single-output sumset-disperser theorem gives depth at least `m^2/(m+C ell^2 log m)` on `m` variables; for fixed `ell=2` this is only `m-O(log m)`. Their multi-output theorem gives depth `n-o(n)` on `n` input bits in its stated range. These are explicit-function bounds in a restricted tree model. They do not apply directly to the unknown separator extension `R`, and even a near-maximal depth bound at `m=N` is only linear in the number of truth-table inputs. The paper's superlinear-circuit consequences use separate Valiant/series-parallel or log-depth parameter translations; they are not a generic conversion from a one-output `N`-variable local-tree bound to `N^(1+epsilon)` unrestricted gates.

The proved limitation is route-specific, not a barrier to all circuit lower bounds. A costed embedding of an explicit hard disperser into the exact Gap-MCSP promise could still be useful, but it must meet both endpoint thresholds and leave a composition budget; C-467's addressability audit explains why a free multi-output table label does not meet that requirement.

Primary source: [Golovnev and Gurumukhani, "Sumset Structure in Local Computation," ECCC TR26-195](https://eccc.weizmann.ac.il/report/2026/195/download), especially Theorems 1-2, Sections 2-3, and the open problems in Section 8.

## 5. First-principles synthesis and next research filter

### Relation to earlier project work

This is a route-closure and synthesis, not a new lower-bound mechanism. C-429 already showed with gate-transcript fibers and an identity front end that input exposure/decision geometry does not charge post-read decoding; C-460 stated the same missing total-DAG extension inequality. C-466 established the coordinate-query version of the accepting-path interpolation argument. C-468 extends that query calculation to arbitrary 2-local predicates and checks it against the recent local-tree paper, but the quantitative bound changes only by a constant factor and the core post-read obstruction was already identified. Do not count this as independent frontier progress or continue restating the same obstruction.

The accumulated failures now divide cleanly:

1. **Information/readout is essentially exhausted.** Essential-input counting gives `N-O(N^beta n)` relevant inputs, and the direct circuit graph gives a linear gate floor. Query width, local path constraints, certificate counts, support size, degree, Hamming volume, and raw incidence do not charge additional shared gates.
2. **The missing cost is post-read computation.** Here “post-read” is only shorthand: ordinary circuits have every primary input available from the start, so no sequential read phase is assumed. After accounting for the linear-scale input dependence/wiring floor, the circuit can still spend arbitrarily many gates transforming and reusing summaries. A coordinate-query tree sees only `N` answers and gives its leaf decoder for free. Any successful direct mechanism must charge actual DAG state transitions beyond input access, including reuse, without counting a shared state once per path.
3. **The source-transfer obligation is separate.** A hard explicit function helps only if a table map has exact OPS-Low and OPS-High endpoints, and generator + separator + postprocessor gates stay below the source lower bound. Locality or oracle hardness alone does not meet that budget.
4. **The complete upper-bound obligation is separate.** Exact enumeration proves an upper bound, but no near-linear full-promise separator is known. Sound incomplete filters do not suffice.

The local-state translation is therefore retained as a model audit, not as the next lower-bound mechanism. Do not pursue larger local-depth bounds for the same one-output separator: the universal `N` query cap makes that objective incapable of proving superlinear gates. The next candidate must either (a) lower-bound the size/transition complexity of a shared DAG computing the exact partial function, with an operation-wise gate charge, or (b) produce an endpoint-correct hard-source map with all circuit costs included. No non-shareability axiom is assumed. This narrows the search space; it does not identify an easier theorem and is not evidence that a proof is imminent.

## 6. Quantitative status

The ordinary bound remains `S>=N-O(N^beta log N)` from essential inputs, with C-406's additive logarithmic reconvergence refinement. The exact full-promise upper remains `O(N*2^(O(N^beta)))`. OPS still asks for one fixed `epsilon>0` that works for every sufficiently small fixed `beta>0`; no such lower bound or near-linear full-promise separator is established. Native `rho_GapMCSP>=N-o(N)` is separate. No P-vs-NP result follows.
