# C-266 to C-270 - matching-to-LowExt and global synchronization audit

Date: 27 September 2026  
Scope: continue at C-261/C-265 under the revised success criterion. A result is major only if it changes the actual fusion bound, gives a full-promise near-linear cover, supplies a near-lossless hard-source transfer, or proves a global sharing theorem.

## C-266 - Rao matching hardness survives native cyclic least-fixed-point semantics

**Classification: GLOBAL-STRUCTURAL.**

Let `v` be even, with `M=Theta(v^2)` edge variables, and let `MATCH_v` be 1 on bipartite graphs with a perfect matching and 0 on graphs with no matching of size `v/4`; the middle promise band is unrestricted. Rao's 2026 theorem gives an ordinary monotone fan-in-two circuit lower bound `exp(c sqrt(v))` for this promise, for a constant `c>0`.

Here is the proof-theoretic cycle audit. A cyclic intersection construction with `q` paid intersections can be written with one state `X_i` per intersection. Free union expressions are flattened into ORs of edge variables and intersection states. Under the published inflationary semantics, on a fixed graph input the update is

```text
X_i(t+1) = X_i(t) OR ((A_i OR OR_{j in P_i} X_j(t))
                       AND
                       (B_i OR OR_{j in Q_i} X_j(t)))
```

where `A_i,B_i` are ORs of input edge variables (possibly empty), and `P_i,Q_i` are subsets of the `q` states. The all-zero initialization and inflationarity imply that each state changes from 0 to 1 at most once, so the fixed point is reached in at most `q` strict rounds. Unroll those rounds. Each update has one AND gate and ORs with at most `M+q+1` terms; replacing each OR by a fan-in-two OR tree gives an ordinary monotone circuit of size

```text
S <= C q^2 (M+q)
```

for an absolute constant `C`. It agrees with the cyclic construction on every graph, including the promise band. Therefore Rao's lower bound applies to the unrolled separator:

```text
exp(c sqrt(v)) <= C q^2 (Theta(v^2)+q).
```

For sufficiently large `v`, this implies `q >= exp(c' sqrt(v))` for a smaller constant `c'>0` (for example, take `c'=c/4` after absorbing polynomial factors). Thus `CycAnd(MATCH_v) >= exp(Omega(sqrt(v)))` in the native cyclic model.

What does fail if one tries to apply Rao's approximation proof directly to a cyclic presentation is the topological gate induction: its approximant for an AND gate is built from already-defined approximants of its two children. A cycle supplies no such order, and an error can return to its own premise. The finite unrolling repairs this logically, but loses a polynomial factor in the number of paid states. This is a proved cyclic analogue, not an assumption that acyclic monotone lower bounds automatically transfer.

Sources: Rao, [*Monotone Circuit Lower Bounds from Spread Matchings*, ECCC TR26-129 rev. 5](https://eccc.weizmann.ac.il/report/2026/129/revision/5/download); cyclic definition and convergence lemma in Cavalar-Oliveira, [*Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://arxiv.org/abs/2503.14117), Section 2.5, especially the inflationary update and convergence-in-`q`-rounds lemma.

## C-267 - Exact LowExt parameter window

**Classification: CONDITIONAL-TRANSFER.**

Assume the exact C-125/C-126 map conditions: a monotone map `phi` of AND-cost `a(N)` sends every YES matching input above the one-hot code of some `w in SIZE(s1)`, and sends every NO input below the one-hot code of some `z outside SIZE(s2)`. Then

```text
q >= CycAnd(MATCH_v) - a(N) >= exp(c' sqrt(v)) - a(N).
```

Set `v=ceil(A (ln N)^2)` and suppose `a(N) <= N^eta`. For any fixed target `epsilon>0`, the transfer gives `q>N^(1+epsilon)` whenever

```text
c' sqrt(A) > max(1+epsilon, eta)
```

with a fixed positive margin. More exactly, if `c' sqrt(A) >= max(1+epsilon,eta)+delta`, then for sufficiently large `N`, the lower-bound term dominates both `N^(1+epsilon)` and `a(N)` by a polynomial factor. If `a=polylog(N)`, any positive `eta` may be used and it suffices that `c' sqrt(A)>1+epsilon`.

The graph has `M=Theta(v^2)=Theta(log^4 N)` edge inputs. Consequently a completion family with size `poly(v)` fits `s1=N^beta/(c0 log N)` for every fixed `beta>0`, eventually. This removes the small-beta parameter obstacle *conditional on the map*. The independent NO-side obligation remains: every NO image must have a completion outside `SIZE(s2)`; merely excluding low completions does not control medium completions.

No `phi` meeting these resource conditions has been constructed. In particular, the inequality above is not an actual `q` lower bound for Gap-MCSP.

## C-268 - Ilango partial-MCSP hardness is not the needed monotone LowExt reduction

**Classification: ROUTE-KILL (direct transplant only).**

Ilango proves under ETH that full truth-table partial-MCSP is not solvable in `N^{o(log log N)}` time. The reduction starts from Bipartite Permutation Independent Set and encodes the existence of a suitable permutation as existence of a small monotone read-once formula for a constructed partial function. The theorem is algorithmic ETH-hardness; it is not a monotone many-one map from a source monotone function to `LowExt_{s1}` with a small AND-cost. It also does not assert that NO instances' partial tables have a completion outside unrestricted `SIZE(s2)`.

The relevant proof idea is circuit-description synchronization: optimal OR formulas can encode permutations, and reverse gate elimination constrains optimal extensions. This suggests looking for a source whose witness circuits have many structured optimal descriptions. But the exact required bridge still has three separate missing properties: monotonicity of every partial-table rail as a function of source edges, a bound on the map's AND gates (not its running time or output length), and a high completion on each source NO. ETH-hardness of MCSP* gives none of these for free.

Primary source: Ilango, [*Constant Depth Formula and Partial Function Versions of MCSP are Hard*, ECCC TR20-183](https://eccc.weizmann.ac.il/report/2020/183/), especially the full-table input definition and the permutation-to-optimal-read-once-formula reduction in Section 1.3. This retires only direct reuse of that reduction as the C-125 map.

## C-269 - Common fully pinned hard baselines cannot use easy witness masks

**Classification: ROUTE-KILL (structured baseline template only).**

Consider a proposed `phi` with a NO instance `G0` whose image contains the complete one-hot code `e(z)` of a common hard table `z`. For a YES instance `G1`, suppose a witness matching `M` yields a low table `w_M` with `e(w_M) <= phi(G1)`. Every coordinate in

```text
D_M = {j : z[j] != w_M[j]}
```

must then have the rail opposite to `z[j]` activated in `phi(G1)`. If the construction makes `D_M`'s indicator computable by a circuit of size `d_M`, then `z = w_M XOR 1_{D_M}` has a circuit of size at most `s1+d_M+O(1)`. Hence this cannot be a valid high baseline when `d_M+O(1) <= s2-s1`.

This formally rules out the natural block-lift repair of C-263 in which each matching edge activates a structured block and the selected matching's changed-coordinate set is a succinct union of those blocks. It does **not** rule out partial NO images: if `phi(G0)` leaves many coordinates unspecified, the high completion's values there need not be recoverable from `w_M` or the activated rails. The remaining LowExt construction must hide the hard information in those unpinned coordinates while still ensuring that every YES has a low completion and every NO has a high one.

## C-270 - Compatibility synchronization object survives the equality calibration but yields no charge

**Classification: CALIBRATION.**

Define `P_i` as proof supports rooted at state `i` and `K_i` as one-hole accepting contexts at `i`. A state induces a relation on pairs of low descriptions `(d,d')` whenever some context matching `G(d)` and proof matching `G(d')` have a consistent union. For every such join, the support cylinder lies wholly in `SIZE(s2)`. Add the set of output blockers hitting each join; this gives a grammar-generated compatibility/proof/blocker tensor, stronger than row counts or a single state signature.

I tried to turn it into the requested dichotomy by charging each state for (a) the number of independently selectable context/proof pairs it admits and (b) the number of incompatible description pairs it must exclude. The first quantity is capped by the `SIZE(s2)` splice entropy only when choices have private coordinate regions; C-247 already shows that private regions are not automatic. The second quantity is not a cost measure: arbitrary semantic endpoints can encode many exclusions in one rule. The hostile equality case is decisive: the repeated-block family has exponentially many low descriptions and a safe native equality-fingerprint cover of `2N+2d-1` pairs (C-258), so the whole tensor can synchronize many reused descriptions at linear cost.

Therefore any surviving synchronization theorem must identify a property of the **full** `SIZE(s1)` language that cannot be implemented by the C-258 coordinate fingerprint, then lower-bound the representation cost of that property in the q-rule grammar. No such property or lower bound has been proved. This candidate is not yet a global sharing theorem.

## Checkpoint after five claims

The actual promise fusion lower bound has not changed: `q=N-o(N)`. C-266 is source-model progress with an explicit cyclic proof; C-267 solves the parameter arithmetic conditional on a map. C-268 and C-269 eliminate direct or structured transfers, while C-270 confirms that compatibility counts do not beat the equality fingerprint. The qualitatively new live implication on the primary route is still a **near-polylog-cost monotone LowExt map with high NO completions**; on the native route it is a **full-class synchronization complexity theorem that charges semantic exclusions despite arbitrary endpoints**.

## Bounded secondary audits

### Terminal-specific BPHP refinement: generic answer splitting is too expensive

The target mismatch DAG's sink preimage is a product set of source pairs. A source sink refiner must split that whole rectangle into sets carrying one fixed violated BPHP clause. For a fixed pair of pigeons, equality of their two input halves only identifies a collision whose hole value varies across the rectangle; it does not identify one fixed clause. The valid answer rectangles therefore have to fix the common hole string as well as the pigeon pair.

If the hole description has `n0` bits, the direct answer-rectangle cover uses `O(m^2 2^{n0})` labelled rectangles per sink. At the source parameter `n0=K(log N)^4`, that cover number is `N^{Theta(K log^3 N)}`, while the source lower bound is only `N^{Theta(K^{1/4})}`. This already makes naive enumeration useless. Further, a rectangle cover does **not** automatically compile to a binary rect-DAG: arbitrary unions of rectangles need not remain rectangles. If a sink preimage contains one broad pair-collision rectangle with all `2^{n0}` hole values, any valid refiner needs at least `2^{n0}` distinct clause-labelled sinks. Thus the broad-sink case is decisively too costly, but the actual C-75 sink preimages may be narrower. A useful theorem must establish that narrower structure and construct an honest binary DAG; totality alone supplies neither. The C-256 static-decoder obstruction remains, and no sink-localization theorem is known.

### Closure compiler: worklist sparsity is not yet a circuit compiler

For a fixed support graph, the closure can be evaluated by an input-dependent worklist in `O(qN+E)` word-RAM operations, where `E<=2q^2` is the number of state-support incidences. This is not an ordinary circuit bound. A direct synchronous circuit recomputes support ORs for up to q rounds and costs `O(qE+q^2N)`; repeated squaring does not help because the update `x -> x OR ((A x) AND (B x))` is nonlinear and composing its q-output circuit duplicates its internal gates at every squaring level.

An oblivious worklist remains a candidate: if its q state activations and E support-incidence events can be compacted/routed by an ordinary circuit using `O((qN+E) polylog q)` gates, then the closure gets a near-quadratic (for q>=N) compiler. No such routing construction is established here. Dynamic random writes into the per-state side-seen flags are exactly where a naive sorting-network or mux implementation can reintroduce a factor q; invoking a RAM-to-circuit simulation without accounting for these wires would be invalid. No compiler improvement or q consequence follows.

## Updated route order

1. Continue Route A only through a concrete global-validity encoding, not source hardness alone. First attempt should exploit partial signed rails and block summaries while explicitly excluding all unintended low completions.
2. Continue Route B only with a full-class object beyond pair counts, certificate widths, and semantic endpoint description length; mandatory countercheck is C-258.
3. For Route C, seek sink-specific hole localization; otherwise retire the common-translate/BPHP arm.
4. For Route D, either give an explicit oblivious routing circuit with every state/edge wire counted or close the worklist route. The generic q^2 AND-count compiler and q^3 binary-gate compiler remain the reference baselines.

## References

- Rao, [*Monotone Circuit Lower Bounds from Spread Matchings*, ECCC TR26-129 rev. 5](https://eccc.weizmann.ac.il/report/2026/129/revision/5/download).
- Cavalar and Oliveira, [*Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://arxiv.org/abs/2503.14117).
- Ilango, [*Constant Depth Formula and Partial Function Versions of MCSP are Hard*, ECCC TR20-183](https://eccc.weizmann.ac.il/report/2020/183/).
- Beame and Whitmeyer, [*Multiparty Communication Complexity of Collision-Finding and Cutting Planes Proofs of Concise Pigeonhole Principles*, ICALP 2025](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.21/LIPIcs.ICALP.2025.21.html).
