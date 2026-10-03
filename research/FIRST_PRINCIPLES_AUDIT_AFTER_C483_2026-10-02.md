# First-principles audit after C-483

Date: 2 October 2026  
Purpose: turn the accumulated route closures into a disciplined next approach. This is a synthesis, not a new lower bound.

## C-484 addendum: restrictions expose a hard ceiling, not the missing surplus

C-484 formalizes one natural attempt to get beyond support: cut table coordinates into a fixed set A and its complement, then force distinct residual functions using Low/High pairs with a common completion. This gives an exact all-extension inequality, S >= (log2 chi(G_A)-1)/2, while respecting total gates and arbitrary sharing. First principles immediately cap it: A has at most N bits, so no one-cut coloring can force more than about N/2 gates. Moreover, a selector circuit can encode exponentially many distinct cofactors in O(log M) gates. These are not technical parameter failures; they show that residual diversity is the wrong charged object.

The useful lesson is to separate **information in residual labels** from **cost of jointly selecting and computing them**. Any future multi-cut theory must define a joint object computable from the whole DAG, prove a gate-by-gate budget that does not charge reused gates multiple times, and derive a superlinear value from the actual forced Low/High relation. The paired construction remains exact Low-description enumeration at O(N*2^(O(N^beta)); no near-linear full-promise separator appears. C-484 changes neither quantitative frontier nor the OPS magnification target. Full proof and canaries: [C-484](C484_COFACTOR_CONFLICT_GRAPH_AND_SELECTOR_OBSTRUCTION_2026-10-02.md).

## C-485 addendum: the hard-ensemble route is conditional on cryptography

C-485 instantiates the C-481 distributional sufficient condition under nonuniform PRF security. If evaluation circuits use O(lambda^d) gates, taking lambda=N^delta with delta*d<beta makes every PRF table Low at the exact s1 threshold. A proposed polynomial-size full-promise separator would distinguish these tables from uniform with near-unit advantage, and its query/test resources are polynomial in lambda. This is a parameter-checked conditional implication, not an unconditional PRF construction or a new MCSP-vs-PRF principle. Nonuniform security is essential. The outstanding proof task is to establish a comparable Low ensemble without assuming its pseudorandomness, or to leave the distribution route for an all-extension gate inequality or an exact source reduction. The unconditional quantitative frontier is unchanged.

## C-486 addendum: strong efficient samplers imply a PRG, but the exact route is weaker

If the Low ensemble is generated from m=Theta(N^beta) random description bits in poly(m) time and is negligibly indistinguishable from uniform against every nonuniform poly(m)-size test, then its output length N=m^(1/beta+o(1)) makes it a standard PRG. That strong formulation imports one-way functions. It does not subsume the separator-specific distribution route: that route needs to rule out near-unit distinguishing by the target separator class, not establish negligible security against all polynomial tests or provide an efficient sampler. Thus efficient sampler search is cryptographic-strength, while a nonconstructive or weaker ensemble route remains open. This is a scope distinction, not a new lower bound.

## 1. State the actual mathematical object

Let N=2^n and let L_t be the set of N-bit truth tables whose Boolean functions on n address bits have ordinary fan-in-two circuit complexity at most t. At the OPS thresholds, set

    s1 = floor(N^beta/(10n)),    s2 = N^beta.

We seek the minimum total AND/OR/NOT gate count over **all** total Boolean circuits F on the N table bits satisfying

    T in L_s1  => F(T)=1,
    CC(T)>s2  => F(T)=0.

Values on the middle band are unconstrained. A lower bound for one canonical predicate, one hard YES distribution, or one restricted source is not a lower bound on this minimum unless a theorem transfers it to every valid extension.

The magnification target has the exact quantifiers: a universal constant c and one fixed epsilon>0 such that for every sufficiently small fixed beta>0, ordinary circuits of size N^(1+epsilon) do not solve Gap-MCSP[2^(beta n)/(c n),2^(beta n)]. Oliveira--Pich--Santhanam show this would imply NP not-subset P/poly. The commonly audited project setting uses c=10. No report in this project has established the required lower bound.

## 2. What the accumulated evidence actually says

The strongest ordinary lower bound in the durable record is the near-linear essential-input/support bound

    N - O(N^beta log N),

with C-406's additive logarithmic reconvergence refinement. It proves almost all table coordinates matter. It does not prove that reading and reducing them costs more than O(N) gates: a fan-in-two DAG can share partial aggregates, and a population count is a direct O(N)-gate example.

The complete upper bound remains exact Low-description enumeration at

    O(N * 2^(O(N^beta)))

total gates. It satisfies every promised endpoint, but no near-linear shared implementation has been found. The native rho_GapMCSP >= N-o(N) statement is a different computational measure and does not compile to ordinary total gates without a proved compiler.

The locality barrier is method-specific. It identifies limits on specified locality-based weak-lower-bound/magnification methods; it is not an impossibility theorem for all ordinary-circuit proofs. No universal barrier, and no P-vs-NP proof, has been found.

## 3. Why the repeated approaches stopped at the linear scale

The failed routes fall into a few structural classes, not hundreds of unrelated mistakes:

1. **Information and support.** Essential variables, balanced sketches, fibers, certificate width, entropy, and residual counts show how much input information is relevant. Their natural ceiling is N bits. They do not count the computation used to turn that information into the correct label.
2. **Local witnesses and geometry.** Anchors, repair balls, sparse restrictions, anti-checkers, block traces, and witness multiplicity can be tested or generated by shared O(N)-scale circuits. A count of many objects is not a count of distinct gates.
3. **Statistics of a selected YES family.** The C-480 trace-family route did not produce the spread needed for approximation; C-481 then exposed cheap affine dual checks for its polynomial-trace ensemble, C-482 found an ANF-degree test, and C-483 found a Hamming-weight test for a high-degree Kasami ensemble. Each cheap test distinguishes only its selected family from uniform; it may reject other Low tables and accept High tables. This is not the full promise.
4. **Alternate models or canonical extensions.** Formula, fixed-depth, local-oracle, native paid-state, fusion, and fixed canonical-predicate lower bounds require an explicit compiler or a proof that every allowed extension inherits them. That transfer has not been established.
5. **Reduction attempts.** A hard image table is insufficient. A useful map E must put every source YES table in L_s1 and every source NO table above s2, compute the entire N-bit output with a charged multi-output circuit, and leave a source lower-bound margin after composition.

C-483 sharpens one practical screening rule: high algebraic degree and cryptographic nonlinearity do not protect a family from a shared global statistic. Any new distribution must first be attacked by weight/histogram tests, affine checks, ANF degree, repeated-block tests, sparse parity checks, and simple block relations. Passing these tests still would not prove it fools all N^(1+epsilon)-gate circuits.

## 4. What is missing, stated without assuming non-shareability

There is no known elementary identity saying that completeness over all size-s1 tables costs superlinear gates. The unresolved theorem is itself an unrestricted circuit lower bound for the minimum extension size. “The witnesses cannot be shared” would simply restate the gap and is not an acceptable premise.

The exact missing quantity is **post-read decision work**: after the N input bits are available, what forces an arbitrary shared AND/OR/NOT DAG to spend more than a linear number of distinct gates to include every Low codeword and exclude every table above s2? Input entropy is at most N; a useful proof must charge computation beyond that information bound. Any proposed potential must be defined on the actual DAG, count each gate/state once, prove its update bound for AND, OR, and NOT, tolerate arbitrary fan-out and merges, and have a superlinear output value forced solely by the promise endpoints.

The clean alternative is a promise-saturated reduction. If a source function h has a multi-output map E with h(x)=1 => E(x) in L_s1 and h(x)=0 => CC(E(x))>s2, then every valid F gives h=F(E(x)); hence CC(h)<=CC(E)+CC(F)+O(1). This handles arbitrary middle labels and arbitrary sharing. The missing pieces are an explicit E with the exact endpoint guarantees and a proved lower bound for h that exceeds the full cost of E by N^(1+epsilon). No such map is currently in the ledger.

## 5. Productive next research cycle

Prioritize one of these two routes and require a proof obligation before expanding it:

* **Direct shared-DAG charge:** work on the gate-faithful rectangle/state graph for the actual Low x High relation. Find an invariant over distinct states whose potential does not multiply by path count at merges. For each operation, show the exact recurrence. First test it on parity, repeated blocks, sparse checks, and simple global block relations. If its endpoint value is only O(N), retire it as a superlinear mechanism.
* **Promise-saturated hard source:** choose one explicit source h and map E, then prove endpoint membership and the full ordinary multi-output gate cost before investigating source hardness. Reject the map immediately if an easy syndrome, weight, or block selector computes h.

Keep a paired full-promise upper search alive, but demand an actual gate saving over description enumeration. Do not spend another cycle improving an ensemble statistic, certificate count, or alternate-model bound unless it changes one of these proof obligations.

## 6. Assessment

The project has learned useful negative information: many intuitive notions of “more structure” are computable with shared linear-size circuits, and many hard-subfamily tests do not address universal Low completeness. It has **not** found a hidden theorem or a proof-level breakthrough. The most plausible route is not a more elaborate count of witnesses; it is a theorem that converts the full endpoint constraints into superlinear post-read computation, or a fully costed source reduction that makes that computation unavoidable.

The C-483 cycle itself changes no quantitative frontier. The research goal stays active; no claim of P != NP is made.

## Primary references

* I. C. Oliveira, J. Pich, and R. Santhanam, [“Hardness Magnification Near State-of-the-Art Lower Bounds,” Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/).
* L. Chen et al., [“Beyond Natural Proofs: Hardness Magnification and Locality”](https://eccc.weizmann.ac.il/report/2019/168/).
* Canteaut, Charpin, and Dobbertin's almost-bent Kasami result and C-483's weight calculation are recorded with exact scope in [C-483](C483_KASAMI_AFFINE_ORBIT_WEIGHT_TEST_2026-10-02.md).
