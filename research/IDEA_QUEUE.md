# Idea queue

Ranked by direct progress toward O-1, the slightly superlinear unrestricted circuit lower bound.

## Primary target clarification

The exact minimum target is \(D(Y\mid\mathcal B)>N^{1+\epsilon}\) in the OPS magnification quantifiers. The current \(\rho\)-cover route is a stronger sufficient condition because \(\rho\) characterizes cyclic intersection complexity and \(\rho\le D_\cap\le D\). Do not spend further time refining a restricted semi-filter family unless the result yields a lower bound on the unrestricted acyclic complexity. The low-side coordinate trace reaches \(N-o(N)\); the attempted complement-side symmetric bound was false because the cube can contain gap/high tables. Its corrected interpolation bound is only \(\Omega(N^\beta/n^2)\).

## Q32 Ã¢â‚¬â€ Static anchor-distance marginal potential (refuted, 26 September 2026)

**Exact state.** C-67 represents a q-pair list by a least fixed point on q rule bits. Each rule needs a witness for both endpoint sides; each initial witness predicate is a disjunction of signed truth-table bits (C-68). The endpoint-containment network is arbitrary semantic data.

**Candidate tested.** For partial list Q and anchor w, let \(\delta_Q(w)\) be the minimum number of extra pairs needed to derive empty. It is at most \(N-1\) and is one-pair-Lipschitz (C-69). C-03 gives \(\delta_{\varnothing}(w)\ge N-\log_2M_2-1=N-o(N)\) for every low anchor. A tempting sufficient lemma was to find a probability measure \(\mu\) on low anchors for which every semantic pair p and every partial Q satisfy \(\mathbb E_\mu[\delta_Q-\delta_{Q\cup\{p\}}]\le N^{-\epsilon}\). Telescoping would force at least \(N^{1+\epsilon-o(1)}\) pairs.

**Refutation (C-73).** For every \(\mu\), choose one minimum literal-slice certificate \(S_w\) per anchor. Each has \(N-o(N)\) coordinates. Averaging over coordinate pairs finds \(\{k,\ell\}\) contained in such a certificate for \(1-o(1)\) of the \(\mu\)-mass; one of its four sign patterns has mass at least \(1/4-o(1)\). The literal-pair rule for that pattern saves exactly one rule on every such anchor. Thus the maximum initial marginal at \(Q=\varnothing\) is at least \(1/4-o(1)\), for every \(\mu\). No static anchor distribution can satisfy the proposed \(N^{-\epsilon}\) marginal bound.

**Learning.** \(\delta_Q\) remains a valid distance, but its additive average credits one shared first intersection separately to a constant fraction of anchors. Any replacement must measure reuse of intermediate intersections rather than demand tiny per-pair progress. The sparse-cube cascade and C-72 remain useful checks. The finite script only validates the recurrence on a toy.

## Q33 Ã¢â‚¬â€ Charge shared intersection states, not anchor savings (active)

The Q32 refutation exhibits a common rule \(p=(G_{k,b},G_{\ell,c})\) that saves one operation for at least \(1/4-o(1)\) of any weighted anchor family. This is legitimate sharing, not a contradiction of the target. Seek a potential on the global collection of generated intersections or on the proof DAG that charges each shared state once, while still forcing a large total number of distinct states before every low anchor is refuted.

**Block amplification attempt.** For a k-coordinate block, computing all \(2^k\) pattern intersections costs \((k-1)2^k\) pairs. This gives the shared first step for k=2, but merging two blocks requires pattern-specific intersections; direct recursion reaches \(2^{2k}\) rules for two blocks and an exponential pattern table at the top. Taking unions of all pattern states restores U and loses anchor information. Restricting to low-anchor patterns gives at most \(M_1\) states, still exponential in \(N^\beta\).

**Next proof question.** Find a way to combine block states without pattern enumeration or union-collapse, or prove that no such compression is possible for arbitrary semantic endpoints. Any claimed lower bound must account for the endpoint description being free.

## Q1   Joint anchor-support capacity (stronger subroute; active only if it yields acyclic progress)

**Idea.** For each endpoint set X in a pair list, let A_X^t be anchors whose closure has derived X by stage t. Proposition 21.4 gives an exact recurrence using at most 3m+1 endpoint/intersection support sets. Bound how much a fixed pair can increase support of the empty set, even when endpoints are arbitrary and rules are reused.

**Why it may constrain arbitrary circuits.** The recurrence exactly represents the all-semi-filter cover process; the published fusion theorem identifies its minimum rule count with cyclic intersection complexity.

**Likely barrier.** Arbitrary endpoint subsets encode nonlocal information without description cost; an entropy bound on their encodings is invalid.

**Smallest validating theorem.** A uniform global rule-sharing bound on both promise sides strong enough to imply \(\rho(Y,\mathcal B)+\rho(Z,\mathcal B)>N^{1+\epsilon}\); this sum already lower-bounds the acyclic circuit size through the AND/OR decomposition.

**Immediate attack.** Derive the bound from support-set signatures, then try to falsify it with arbitrary adversarial endpoints. Stop if the argument only re-proves a more elaborate version of the coordinate leaf bound.

## Q2   Fractional dual over noncanonical semi-filters

**Idea.** Find a distribution on anchored semi-filters such that every endpoint pair violates at most N^(-1-epsilon) mass. The set-cover dual would force at least N^(1+epsilon) pairs.

**Why it may constrain arbitrary circuits.** It ranges over all endpoint pairs rather than a selected solver syntax.

**Likely barrier.** Pairs can be chosen after the distribution; balanced partitions defeat simple measure-threshold filters. Existing canonical, majority, and feature-span distributions have short covers.

**Smallest validating theorem.** A uniform pair-violation bound for every n and every allowed beta.

**Immediate attack.** Test a Hamming-ball family F_a={S:mu_a(S)>1/4} with an arbitrary disjoint partition of U, and compare ball support size against the number of low anchors.

**Result.** C-10 completes this attack. These threshold families are valid semi-filters under the actual definition (upward closed, nonempty, and excluding empty). Circuit counting makes all supports large, and a random partition balances every mu_a at once. One pair then violates every selected F_a. This rules out a fractional dual supported on this Hamming-ball family, not all fractional duals. See DEAD_ENDS.md, "Hamming-ball threshold filters have a one-pair cover."

## Q3   Adaptive anti-checker selector lower bound

**Idea.** Lower-bound the multi-output circuit that reads a truth table $f$ and returns a short sample anti-checking every smaller circuit whenever $CC(f)>s_2$. OPS construct such a selector of size $N^{1+O(\beta)}$ under $NP\subseteq Circuit[poly]$ and combine it with a succinct-MCSP decider to solve Gap-MCSP.

**Why it may help.** This is a semantic object attached to the truth table, not a presumed internal representation of a SAT solver. A lower bound on the selector could be a distinct sufficient route to $NP\not\subseteq P/poly$.

**Counterexample-first result.** Any fixed sample $Q$ of at most $2^{10\beta n}$ points fails by counting (C-15). Sparse hard truth tables and a hypergeometric union bound show that every valid selector needs $q\ge 2^{\eta s_2/n}$ distinct samples (C-18), strengthening C-17's $q\ge(1-o(1))N^{1-10\beta}$ bound. This remains only a range lower bound: the output has $tn$ address bits, with $tn\gg s_2/n$, so output wiring alone can realize enough distinct samples. It does not prove superlinear circuit size.
**Likely barrier.** The required adaptive map is itself a near-linear circuit lower-bound target. OPS show it exists under $NP\subseteq Circuit[poly]$; proving that no near-linear selector exists in the required exponent/parameter regime would already force the separation. Chen et al. refute a static Anti-Checker Hypothesis at different thresholds and with a bounded candidate family; this does not refute the OPS selector, whose range may have up to $2^{tn}$ samples. C-18 independently gives a quantitative OPS-parameter range obstruction but still does not lower-bound selector size. A bound on output length, range size, or restricted selector syntax does not suffice.

**Smallest validating theorem.** For some $\delta>0$ and every sufficiently small fixed $\beta>0$, no circuit family of size $N^{1+\delta}$ computes a valid selector for the OPS parameters. Audit its quantifiers against the $k$ in Lemma 4.1 before claiming it implies the theorem; alternatively prove the exact O-1 separator lower bound directly.

**Immediate attack.** Treat each sample as a transversal of the error sets $E_D(f)=\{x:f(x)\ne D(x)\}$ for all circuits $D$ of size at most $s_1$. C-20 shows that minimum error-set size plus a generic random hitting-set argument only gives a vacuous $O(nN)$ sample bound. C-19 shows positive-hit counts alone are also too weak: a sorting network finds every positive coordinate of a sparse table in $O(Nn^3)$ size. A useful invariant must exploit the structured overlap of the error sets conditional on the full truth table and constrain the full queried label pattern, especially selected zeros that block every small circuit.
## Q4   Time-slice / communication invariant

**Idea.** Partition an arbitrary circuit or computation into regions and lower-bound information crossing the cut for the MCSP promise.

**Why it may constrain arbitrary circuits.** A decomposition theorem could apply to any circuit, independently of gate labels.

**Likely barrier.** Decompositions may have large boundaries or lose sharing; a useful bound may already imply major circuit lower bounds.

**Smallest validating theorem.** Every size-S separator induces a protocol of cost f(S), and Gap-MCSP has a matching protocol lower bound.

**Immediate attack.** Try truth-table block partitions and search for small protocols; reject this direction if they fail to see circuit complexity.

## Q5   Logic / proof-system route

**Idea.** Convert a hypothetical SAT decider into a sound proof/refutation mechanism and prove a proof-length lower bound.

**Why it may constrain arbitrary algorithms.** A general decider might be transformed into a proof-producing machine by a uniform verifier construction.

**Likely barrier.** UNSAT certificates need not be short; a proof-system lower bound needs a bridge from deciders without assuming NP=coNP.

**Smallest validating theorem.** A polynomially checkable, polynomially sized refutation system for every UNSAT instance from any hypothetical P SAT decider, then a superpolynomial lower bound for that system.

**Immediate attack.** Construct the refutation transformation and audit certificate length before attempting lower bounds.

## Q6   Resource-bounded diagonalization

**Idea.** Build a self-referential NP language whose verified computation defeats each polynomial SAT solver.

**Why it may constrain arbitrary algorithms.** Enumerate clocked machines and diagonalize semantically.

**Likely barrier.** Constructing the diagonal instance or tableau costs more than the clock; an EXP diagonal is not automatically in NP.

**Smallest validating theorem.** A time-preserving, NP-verifiable fixed-point construction with polynomial overhead.

**Immediate attack.** Expand instance length and verification time symbolically; discard constructions with superpolynomial overhead.

## Q7   Feasible SAT circuit error witnesses plus Extended Frege lower bounds

**Idea.** Pich and Santhanam give a conditional route: if Extended Frege is not polynomially bounded and S^1_2 proves that a polynomial-time function witnesses an error for every polynomial-size circuit that fails to solve SAT, then P != NP. Their theorem lists feasible anti-checkers as a separate sufficient condition; it also links non-provability of suitable circuit lower bounds to P != NP under explicit average-case hardness and learning assumptions.

**Why it may constrain arbitrary algorithms.** The route reasons about all polynomial-size circuits for SAT and uses proof-theoretic self-provability, rather than a fixed solver architecture.

**Likely barrier.** The needed EF non-boundedness is a major open proof-complexity statement. The antichecker condition is also formalized in S^1_2; standard-model existence alone is not enough for their theorem.

**Smallest validating theorem.** First reconstruct the exact theorem and show that the hypothesized polynomial-time SAT decider would yield the required feasible error-witness function with the paper's exact formalization. Then the unresolved core is EF non-p-boundedness (or a weaker condition sufficient for their theorem).

**Immediate attack.** Prove the standard-model search step: given a purported SAT circuit C, finding an input on which C errs is an NP search problem if SAT is in P, so P=NP would make it polynomial-time solvable. Then check whether this yields the paper's stronger S^1_2-provability requirement; do not assume it does. Compare this route's open EF obligation with O-1 before allocating more effort.

**Source.** Pich and Santhanam, [Towards P != NP from Extended Frege lower bounds](https://arxiv.org/abs/2312.08163), especially the circuit-witnessing condition in the abstract and Theorem 1.

## Q8   Escape the locality barrier with a nonlocal semantic invariant

**Idea.** Identify which part of Gap-MCSP's global low-circuit-existence predicate remains hard when a candidate circuit is augmented with small fan-in oracle gates for local properties. Then prove a lower bound using an invariant that genuinely sees this nonlocal remainder.

**Why it may constrain arbitrary algorithms.** The final target remains an unrestricted circuit lower bound; locality is a diagnostic for why known weak lower-bound techniques fail, not a restriction placed on the target circuit.

**Likely barrier.** The locality result only rules out direct adaptations of specified lower-bound techniques; it is not an impossibility theorem for all proof methods. An invariant that forgets input-wide circuit consistency will be vulnerable to the same local-oracle simulation.

**Smallest validating theorem.** A target-specific lower bound that survives the local-oracle extension and, with exponent slack, transfers back to the OPS circuit threshold.

**Immediate attack.** Reconstruct the exact oracle gate from the locality paper and test whether the project coordinate/closure invariants are already computable by it. If they are, change the object being measured rather than adding more filter variants.

**Source.** Chen et al., [Beyond Natural Proofs: Hardness Magnification and Locality](https://arxiv.org/abs/1911.08297).

### Adversarial check on Q1: one rule can affect many anchors

Let G_(i,b) be the high-promise tables whose i-th bit is b. For two coordinates i,j, use E=G_(i,0) union G_(j,0) and H=G_(i,1) union G_(j,1). If an anchor has different bits at i,j, its upward-closed filter generated by all matching literals contains E and H. Their intersection is the off-diagonal pair of slices. When the high promise realizes all patterns on triples of coordinates, no matching literal generator is contained in that intersection, so this particular filter rejects the pair.

For coordinates corresponding to inputs 0^n and e_1, exactly N affine truth tables disagree there, and all are low-circuit tables for large n. Thus one pair can hit at least N explicit anchored filters. The filters for distinct anchors are distinct by two-coordinate fullness. This does not cover all filters for those anchors and is not a small cover. It falsifies a naive per-rule bounded-anchor argument. A useful global charge must measure whether a rule helps complete an entire closure derivation, not merely how many anchors it touches.

## Q9   Quantitative synthesis of a minimax anti-checker

**Idea.** Treat anti-checking as a zero-sum game. For each hard truth table, minimax already yields a short sample; the open question is whether a small circuit can synthesize such a sample from the explicit table.

**Why it may constrain arbitrary algorithms.** The output must refute every size-$s_1$ circuit, without assuming how a SAT solver is implemented. OPS show that under $NP\subseteq P/poly$ the selector can be built at size $N^{1+O(\beta)}$.

**Known result.** C-21 closes the existence lemma via minimax, and C-22 puts the prefix-extension search in $\Sigma_2^P$. Under $P=NP$ this gives an unspecified polynomial-time selector; it does not give the near-linear exponent required to contradict O-1.

**Smallest validating theorem.** For some fixed $\delta>0$ and every sufficiently small fixed $\beta$, prove that no size-$N^{1+\delta}$ circuit maps every table with $CC(f)>s_2$ to a valid OPS anti-checker. By OPS this implies $NP\not\subseteq P/poly$.

**Immediate attack.** Do not reprove existence or use range size. Split circuits by their error-set geometry and target the near-circuit exceptions for which small error sets cluster in structured regions.

## Q10   Adversarial sparse supports inside sparse circuit regions

**Idea.** C-23 proves random sparse supports are easy for anti-checking: list all positives and append a fixed hitting set for dense low-circuit 1-sets. The exceptional case is a hard support $R$ contained in the 1-set of a low circuit with low density.

**Why it may help.** Such a circuit creates a structured region in which all difficult disagreement points may lie. If a selector must either identify that region or spend many queries, a representation-independent lower bound may be possible.

**Likely barrier.** The containing circuit is not given. There are exponentially many candidate circuits, and the residual error sets $D^{-1}(1)\setminus R$ can overlap irregularly. Counting all sparse supports or capturing all positive points does not identify the correct superset.

**Smallest validating theorem.** A lower bound on the circuit size of any map that, on every high-complexity support contained in a low-density size-$s_1$ circuit region, outputs a point in the residual 1-set of every such region.

**Immediate attack.** Try to falsify this proposed necessary behavior by constructing a selector that hits residual sets without recovering a containing circuit. Keep constants explicit and compare the query length $s_2^{10}$ to the family size and region density.

**Counterexamples / updated filter.** C-24 and C-26 show axis-aligned and affine regions are recovered by coordinate/linear hulls. C-30 extends recovery to bounded-degree polynomial graphs by feature-span closure. C-31 shows Hamming balls defeat fixed-degree closure but are recovered by maximum weight. C-32 shows secret linear images of product regions are recovered from Fourier peaks and minimal dependencies. Q10 must now target low-circuit regions that evade several such observables; none of these failures proves arbitrary selectors must recover a region.

## Q11   Uniform distinguishers and sparse magnification

Atserias and MÃƒÂ¼ller (2025) use sparse distinguishers to obtain a uniform magnification theorem for approximation-MCSP. Their stated consequence is $P\ne NP^{\oplus P}$ under a near-linear P-uniform circuit lower bound. This bypasses the OPS nonuniform selector but does not by itself imply $P\ne NP$.

**Decision.** Keep it as a lower-priority route. First seek a proved class implication to $P\ne NP$ or a target lower bound that yields the desired conclusion directly. Do not silently identify $NP^{\oplus P}$ with $NP$.

## Q12   Observable-closure stress tests for hidden low-circuit regions

**Idea.** Build sparse high-complexity supports inside low-circuit sets whose descriptions are initially hidden. Stress-test recovery in a fixed order: coordinate hull, affine span, bounded-degree polynomial closure, simple statistics such as extremal weight, then Fourier/matroid structure. C-24 through C-33 show that each tested structured family is easy by some selector, and C-33 gives a criterion covering connected spanning Fourier-peak matroids.

**Why it may help.** It prevents us from mistaking an opaque description for a hard selector input. Positive samples can expose structure through a representation different from the circuit that defines the region.

**Likely barrier.** The test only falsifies candidate distributions and specific recovery mechanisms. Even a region hard for all current methods gives no lower bound on selectors that use a different transversal construction. This route must not become a substitute for O-1.

**Smallest validating theorem.** Either construct a low-circuit region of support-budget size whose high-complexity sparse supports have no near-linear anti-checker selector, or prove a universal reduction from valid anti-checkers to a representation-independent description/recovery task. Neither theorem is known here.

**Immediate attack.** Test random low-circuit constraint sets for large feature closure and weak Fourier fingerprints, while retaining enough support entropy for $CC(1_R)>s_2$. Then attempt to convert that property into a lower bound on all transversals, rather than only on region-recovery algorithms.


## Q13   Prove a superlinear routing lower bound for anti-checkers (current primary attack)

**Object.** A total multi-output circuit $A$ maps an $N$-bit truth table $f$ to a short address list $Q_f$ such that, whenever $CC(f)>s_2$, every circuit of size $s_1$ disagrees with $f$ somewhere on $Q_f$.

**Established baseline.** C-34 proves every valid selector depends on $N-o(N)$ input bits. C-38 uses multi-output circuit-graph connectivity to sharpen this to $N-o(N)$ fan-in-two gates. This is universal but only linear. Output-range and support-count bounds are weaker for gate size.

**Smallest useful theorem.** For some fixed $\delta>0$ and all sufficiently small fixed $\beta$, every such selector has size $N^{1+\delta}$ on infinitely many lengths, with constants aligned to the OPS implication. This alone is sufficient to force $NP\not\subseteq P/poly$ through Theorem 1.4.

**Adversarial attack.** C-36 rules out robust affine sketches, while C-39 shows that priority encoders can use label feedback to defeat both constant hypotheses in $O(N)$ gates. A lower bound must handle arbitrary nonlinear feedback and the full low-circuit class; it cannot charge each input independently or assume a containing low-circuit region is identified.

**Status.** Primary target O-1. No superlinear invariant is known here. Q16 is the current concrete subproblem: quantify the extra routing needed to hit all $M_1$ circuit traces at once. C-34/C-38 give only a near-$N$ baseline; do not claim a breakthrough from it.

## Q14   Nonlinear fiber shrinkage and query-label feedback

**Input.** C-35 shows a fixed sample succeeds on almost all random tables. C-36 rules out robust linear sketches, even with an unlimited decoder, by fixing a sketch value and completing a high table with zero labels on the resulting query list.

**Exact necessary condition.** For every query list $q$ and every size-$s_1$ circuit trace $y$ on $q$, a valid selector's address fiber $\{f:Q_f=q, f|_q=y\}$ contains at most $M_2$ tables.

**Question.** Can a bounded-fan-in circuit make those conditional fibers this small by using the selected labels themselves to determine the addresses? A theorem ruling this out at size $N^{1+\epsilon}$ would reach O-1. A counterexample selector would identify the nonlinear mechanism any lower bound must address.

**Adversarial checks.** The affine-sketch theorem does not cover nonlinear summaries. A fixed-menu range argument only works while the union of candidate coordinates leaves more than $\log M_2$ bits free. A single-circuit fixed-point argument is false: Ã¢â‚¬Å“query the first 1-bitÃ¢â‚¬Â avoids zero labels on every nonzero table. The full family of low-circuit traces must be handled simultaneously.

**Status.** Active subproblem, not a solution. Prove a fiber-shrinkage lower bound or construct a small feedback selector; audit the result against arbitrary sharing and negation.

## Q16   Simultaneous witness routing for all small circuits

**Stress test.** C-39's priority encoders find a 1- and a 0-witness in $O(N)$ gates, defeating the constant-zero and constant-one hypotheses for every nonconstant table. The selector must route against all $M_1=2^{O(s_1\log(s_1+n))}$ small-circuit traces simultaneously.

**Target.** Identify a property of the full family of residual disagreement sets that forces superlinear address-circuit size, even when query labels feed back into the addresses. A candidate must survive the priority-encoder construction and the C-36 affine-sketch obstruction.

**Status.** New primary formulation; no lower bound yet. Avoid arguments based on a single circuit, a fixed finite hypothesis family, or fixed query samples.

## Q17   Dual anti-approximation margin and witness extraction

**Object.** $\Delta_s(f)=\max_\mu\min_{D\in\mathcal C_s}\Pr_{x\sim\mu}[D(x)\ne f(x)]$.

**Established fact (C-40).** If $CC(f)>Cns$, then $\Delta_s(f)\ge1/3$; random sampling from a maximizing distribution gives a transversal of size $O(s\log(s+n))$. For a rational candidate distribution, finding a violated constraint is weighted circuit fitting and belongs to NP. An NP-oracle ellipsoid plus random rounding gives a high-probability $\mathrm{FBPP}^{\mathrm{NP}}$ selector on promised high inputs; exact list validity is coNP, and generic existential list search has a $\Sigma_2^P$ form.

**What this changes.** It removes anti-checker existence and output budget as candidate bottlenecks. It isolates witness selection on the full truth-table input. The value gap $\Delta=0$ versus $\Delta\ge1/3$ is itself a Gap-MCSP promise, so the margin is not an independent lower-bound invariant.

**Highest-value attack.** Seek a construction of the dual distribution/list that does not call the weighted fitting oracle and works for every hard table. Adversarial test: on exceptional tables, a fixed sample has a trace realized by a small circuit; an argument must force adaptive change in the sample. Reject claims that merely restate the margin gap or invoke minimax existence as an algorithm.

**Status.** Conceptual refinement of C-21; no separation progress. Keep secondary to direct O-1 unless a concrete extraction theorem appears.

## Q18   Adversarially defeat data-independent witness menus

**Theorem (C-41).** For supports of weight $w=Kns=\Theta(N^\beta)$, circuit counting makes almost every support high complexity above $Cns$. For any fixed menu of $m$ distributions with $mw/N=o(1)$, averaging and Markov give one such support whose mass under every menu distribution is $o(1)$. The constant-zero circuit then has tiny error for every menu member.

**Learning.** C-15's fixed-list obstruction extends to every small data-independent distribution menu. A valid construction must select its witness using the table itself.

**Limit and next attack.** This does not touch a selector with up to $2^{tn}$ possible outputs and nonlinear dependence on $f$. Try to prove a capacity theorem for *input-dependent* menu selection; first account for C-34/C-38's $N-o(N)$ essential-input result and C-39's linear priority feedback. Do not claim a lower bound from C-41 alone.

## Q15   Audit proof-assistant claims at their axiom interfaces

**Trigger.** Arthanari's June 2026 pedigree-polytope preprint claims $P=NP$ with Lean verification.

**Finding (C-37).** In the linked repository, `QuickProtocol (LayeredPoint n)` is assumed as an axiom, the MCF necessity direction is an axiom (the backup proof has 16 sorries), the alternative polytope is a `Unit` placeholder, and membership-to-optimization/STSP transfers include axioms. Therefore the theorem is machine-checked only conditional on assumptions that include the missing algorithmic step; it is not an axiom-free resolution.

**Reusable method.** For any claimed formal proof, inspect (1) every axiom's exact type, (2) whether an implication assumes the target conclusion under a new name, (3) whether oracle protocols and resource bounds are represented concretely, and (4) both soundness and completeness of decision procedures. A checked theorem with unchecked axioms is not a proof of the target.

**Priority.** Audit genuine new claims when encountered, but do not let unaccepted claims displace O-1 unless an assumption-free argument survives a full proof review.

## Q19   Search-to-decision collapse does not control the magnification exponent

**Lemma (C-44).** For fixed $f$, a length-$O(s\log(s+n))$ anti-checker list is described by a $\Sigma_2^P$ search relation: existentially choose the list, then universally quantify over all size-$s$ circuits and check that one listed point disagrees. C-40 guarantees existence on the high-complexity promise. Under P=NP, PH=P, and bit-by-bit self-reduction finds a list in polynomial time in the full truth-table length $N$ whenever one exists.

**What it teaches.** Decidability of the selector relation is not the hard resource. The generic algorithm yields only $N^{O(1)}$ circuits with no controlled exponent. The OPS theorem already gives $N^{1+\epsilon}$ circuits under $NP\subseteq P/poly$, so this conditional search construction is a route diagnostic rather than a new theorem toward separation.

**Next attack.** Find a quantitative, near-linear implementation of the selector search that avoids generic PH decision, or return to O-1 and lower-bound the nonlinear routing directly. Do not infer the required exponent from P=NP.

## Q20   Flatten KPT witnesses without enumerating satisfying assignments

**Trigger.** C-43 records that existential anti-checker data yields finite adaptive KPT functions whose later outputs depend on earlier challenge witnesses.

**Target.** Prove a polynomial-overhead transcript-composition lemma that extracts one stable SAT solver/anti-checker selector from those adaptive functions without choosing satisfying assignments in advance. A generic branch over $n$-bit assignments is exponential, and substituting a hypothesized SAT circuit does not provide the $S^1_2$ proof required by Theorem 7.

**Status.** Speculative proof-complexity direction. The paper identifies the dependency, but this project has no flattening theorem or EF lower bound. Keep O-1 primary.

## Q21   Deterministically route through the residual circuit version space

**Object (C-45).** For each small circuit $D$, let $E_D(f)=\{x:D(x)\ne f(x)\}$. A query list $Q$ is valid exactly when it hits every $E_D$, or equivalently when no circuit survives with $D|_Q=f|_Q$.

**Baseline.** The survivor/counterexample loop is sound and terminates after at most $|\mathcal C_s|$ rounds, but that is exponential in $s\log s$. C-40's dual margin ensures a random sample of $O(\log|\mathcal C_s|)$ points from $\mu_f$ hits every error set.

**Attack.** Search for a circuit-specific potential that constructs a short transversal. A point that eliminates a constant fraction of survivors would give logarithmically many rounds, but the obvious potential needs the weighted number of surviving circuits that err at that point. Weighted counting is a candidate bottleneck, not a proven requirement; avoid claiming #P-hardness without an encoding reduction.

**Adversarial limit.** Arbitrary set systems show an oracle returning one unhit set and any one point in it can make the loop take exponentially many steps even when a tiny transversal exists. This only invalidates black-box greedy progress. The real circuit class may have exploitable structure, which is the next question.

**Related literature (C-46).** Compton, Pabbaraju, and Zhivotovskiy show the one-point greedy teaching procedure can require $\Omega(\log|\mathcal C|)$ examples ([arXiv:2505.03223](https://arxiv.org/html/2505.03223)). That matches, rather than exceeds, C-45's $O(\log|\mathcal C_s|)$ query bound under constant margin. It therefore does not obstruct the combinatorial construction. Their work also does not analyze the cost of computing the best point for a circuit version space.

## Q22   Version-space score is a conditional construction, not a universal barrier

**Oracle baseline (C-47).** Given $Q$, count $Z_Q$, the number of small-circuit descriptions matching $f$ on $Q$, and for each $x$ count $G_{Q,x}$, those survivors that disagree at $x$. The C-40 margin guarantees $\max_xG_{Q,x}\ge\gamma Z_Q$, so repeatedly choosing a maximizer empties the version space in $O(\gamma^{-1}s\log(s+n))$ steps. These are #P counts; the construction is an explicit $\mathrm{FP}^{\#P}$ selector.

**C-48 update.** Exact #P counts are not essential under $NP\subseteq P/poly$: relative approximate counts on the short transcript suffice, and Stockmeyer plus nonuniform derandomization yields the known $N^{1+O(\beta)}$ selector. This closes the conditional score-construction question. It does not imply that every selector computes the score.

**Next target.** Stop treating score approximation as the main open problem. A lower bound on that chosen greedy implementation would not constrain selectors that use another method. Work on the universal puncturing-certificate function directly: map each high-complexity table $f$ to a set $Q$ such that $f|_Q$ is absent from the projection of all size-$s$ circuits, and prove the required size lower bound for every such circuit map.

**Status.** C-47/C-48 are oracle and conditional construction baselines. The universal selector lower bound remains O-1.

## Q23   Robust puncturing certificates via local correction

**Lemma (C-49).** Pointwise correction of a Boolean circuit costs $O(n)$ gates per changed truth-table location. Therefore, if a query set anti-checks all circuits of size $s_1$, then the restricted labels must be at Hamming distance $\Omega(s_1/n)$ from the trace of every circuit of size $s_1/2$. A minimax-length list has relative distance $\Omega(1/n^2)$; a selector output of $q$ queries only gets the general relative bound $\Omega(s_1/(nq))$, since the OPS interface allows a longer list. The full OPS high promise is likewise globally $\Omega(s_2/n)$-far from circuits of size $s_1$.

**Novel use to test.** Treat the output as a robust puncturing rather than only a set outside the projected code. Sparse distinguishers can amplify the trace distance after the selector has chosen its query set; polylogarithmic parity weight follows only for minimax-length lists, not the full selector allowance.

**Adversarial result.** The distinguisher has no effect on the unresolved routing step: the query set itself depends on all of $f$, and the project has no theorem that charges an arbitrary circuit for finding it. At fixed $\beta$, the available circuit-count estimate gives $2^{O(N^\beta)}$ possible YES tables, not the $2^{N^{o(1)}}$ sparsity premise in general formula magnification. Neither its formula conclusion nor the conditional uniform implication to $P != NP^{oplus P}$ establishes $P != NP$. Full parameter audit: research/ROUTE_AUDIT_2026-09-25.md.

**Status.** A proved refinement of the certificate, not progress on the O-1 exponent. Continue only if robust trace separation yields an independently justified lower bound on arbitrary input-dependent routing.

## Q24   Locate heavy-overlap error regions for the full circuit family

**Lemma (C-50).** For any odd tuple of size-$s_0$ circuits, the set where a majority of them err on a table with $CC(f)>s_2$ has size $\Omega((s_2-k s_0)/n)$ whenever the majority size is below $s_2$. Otherwise the majority circuit can be patched on that region to compute $f$. At OPS parameters this is $\Omega(s_2/n)$ uniformly for odd k up to $\kappa n$. For odd k >= 3, some pair in every such tuple has $\Omega(s_2/n)$ common disagreement points.

**Potential route.** A selector needs a small transversal of all disagreement sets. C-50 says the circuit-derived range space has heavy-overlap regions across every small subfamily. If the intersections can be organized into a succinct cover, the query list might be found without approximating residual-circuit counts.

**Adversarial check.** C-28's arbitrary-hypergraph counterexample shows majority overlap alone does not imply a small transversal. A single-circuit or fixed-tuple witness can be found by evaluating its majority against the truth table, but that does not select a point that removes a large fraction of the full version space. The needed theorem is a circuit-specific global organization of these regions, with a circuit-cost bound.

**Quantitative generic counterexample.** On a universe of size m, take all subsets E with |E|>m/2. For any odd k-set subfamily, its majority-error region H has |H|>m/(k+1): total incidence exceeds km/2, while points outside H occur in at most (k-1)/2 sets. For k<=kappa*n this is Omega(m/n), which is stronger than the circuit-derived Omega(N^beta/n) when m=N. Yet the whole family needs a transversal of size ceil(m/2). Thus even the quantitative C-50 property does not by itself yield the desired small global transversal.

**Immediate test.** Try to construct such an organization from bounded-width families of circuit differences; first rule out simple unique-marker constructions, which C-50 already excludes when their errors are almost disjoint.

**Status.** Open, distinct from score counting only if it gives a point-selection method that avoids residual-version-space weights.

## Q25   Turn dense low-circuit error overlap into a findable transversal

**Input.** C-51 proves that the graph on low-circuit functions, joining pairs wrong together on $\Omega(N^\beta/n)$ coordinates, has constant density. The same holds inside every residual subfamily.

**Potential use.** For a residual family of size $m$, pair-coordinate incidence gives a point wrong for $\Omega(m\sqrt{N^\beta/(Nn)})$ members. An ideal max-score process over distinct functions gives a combinatorial query bound $O(N^{(1+\beta)/2}\sqrt n)$, worse than C-40's $O(N^\beta\operatorname{poly}(n))$ minimax list bound for fixed $\beta<1$. This is only existential; counting distinct functions may be harder than counting syntactic descriptions, and score extraction is not implemented.

**Adversarial check.** An abstract common-core family can have many distinct hypotheses, maximal overlap, and a constant-size fixed-query selector. Heavy-overlap density therefore does not force superlinear circuit size. The all-subsets hypergraph counterexample also blocks generic transversal conclusions.

**Exact next theorem.** Find a circuit-specific property of the full disagreement family that turns heavy pair overlap into an efficiently discoverable constant-fraction error point for every residual version space, or prove that any such discovery circuit has superlinear size. C-40 already gives existence of such a point under a dual margin; the unresolved issue is synthesis and universal selector necessity.

**Status.** Structural direction proved, but dominated as a list-existence bound and not a lower-bound route. Keep only as a diagnostic; do not extend by incidence counting alone.

## Q26   Convert implicit hard functions into explicit Gap-MCSP tables

**Motivation.** Recent work gives conditional NP-hardness for sampler-described Gap-ImpMCSP, while OPS magnification uses explicit truth-table inputs. The potential bridge is to recover the unique label function from the sampler and materialize its table.

**First theorem needed.** Given a polynomial-size sampler $E(r)=(x,b)$ with full support over $x$ and consistent labels, compute $f(x)=b$ for every $x$ in time polynomial in the sampler description and $2^n$, while preserving the reduction's gap and source-input polynomial bound.

**Adversarial check.** Full support guarantees that a preimage exists, not that one can efficiently find it. Invertible-label search may be hidden in the sampler; enumerating its random tapes can cost $2^{poly(n)}$. Also, if the function arity is polynomial in the SAT input length, writing its $2^n$-bit table is already exponential. Reducing arity to $O(\log m)$ while retaining the hardness gap has not been established.

**Status.** Adjacent speculative route only. The 2025 and 2026 learning/implicit-MCSP results do not currently supply this explicitness theorem or an unconditional lower bound.


## Q27 - From a universal first query to conditional tail elimination

C-52 proves the root of the greedy version-space tree is near-linear: O(n) sampled descriptions give N hardwired marginals, and a selector chooses a coordinate wrong on at least 3/20 of all low-circuit descriptions for every high table. The conditional dual margin is 3/10.

For any transcript tau with nonempty survivor set, the same dual margin supplies a coordinate wrong on at least 3/10 of the survivors under any distribution supported on them. A uniform sample tracks all transcripts of length at most k while their mass is at least rho using O((kn+log(1/eta))/(gamma*rho)) samples after the C-53 relative-Chernoff refinement. Below rho, empirical emptiness is not a certificate that the true version space is empty.

**Next target.** Find a near-linear conditional profile/update, a circuit-specific rare-tail elimination theorem, or a different universal construction. Do not infer impossibility for arbitrary selectors from this sample-based limitation.


**C-53 refinement to Q27.** Use relative Chernoff bounds rather than additive Hoeffding when estimating conditional scores. One sample of size $O((kn+\log(1/\eta))/(\gamma\rho))$ tracks all residual and next-query ranges while residual mass is at least $\rho$ and preserves constant contraction. It reaches inverse-polynomial residual mass with polynomial sample size, but the residual falls below that threshold after $O(n)$ contractions unless it is empty. This is the strongest global-sampling version checked so far; the next target remains exact tail elimination.


## Q28 - Continue after the forced nonempty rare-tail handoff

C-54 combines relative sampling with DNF interpolation. Any transcript of $O(n)$ queried labels still has a size-$s_1$ circuit consistent with it, but constant-fraction contraction drives the uniform residual mass below $N^{-a}$ after $O(n)$ rounds. Thus the global-sample guarantee expires at a nonempty cell before the minimum $\Omega(s_1/n)$ anti-checker length.

**Next target.** Find a conditional sampler or score mechanism that keeps working below inverse-polynomial mass, or replace description-mass contraction with a potential that certifies the whole residual class. A valid anti-checker needs at least $\Omega(s_1/n)$ distinct queries by interpolation, but this does not lower-bound its circuit size. The OPS query budget is much larger, so closing that gap is the live issue.


## Q29 - Treat anti-checker synthesis as a circuit Skolemization problem

For each high table $f$, minimax and sampling prove that there exists a list $Q$ of $O(\log |\mathcal C_{s_1}|)\le t_n$ inputs such that every size-$s_1$ circuit disagrees with $f$ somewhere on $Q$, where $t_n=2^{10\beta n}$. Formally this is $\forall f\in F_n\;\exists Q\in X_n^{\le t_n}\;R_n(f,Q)$. A near-linear selector instead requires a circuit family $S_n$ of size $N^{1+\epsilon}$ with $\forall f\in F_n\;[|S_n(f)|\le t_n\land R_n(f,S_n(f))]$. The relation $R_n(f,Q)$ is coNP-checkable: its negation has a circuit description agreeing with all queried labels. Thus the existence proof does not provide a generic small Skolem circuit.

**Highest-leverage target.** Prove an efficient nonuniform uniformization theorem for this specific relation, or a lower bound against every such uniformizer. Attack whether the universal circuit counterexample can be avoided using a succinct semantic certificate; do not assume a lower bound for the global-sampling greedy architecture transfers to arbitrary selectors. This sharpens the logical location of O-1 but does not resolve it.

## Q30 - Search reductions that survive all valid anti-checkers

**Idea.** Map each source input $x$ to a high table $f_x$ and use a polynomial-size decoder $B(x,Q,f_x|_Q)$ that recovers the source answer for every valid selector output $Q$.

**Current barriers.** C-58: a common base anti-checker survives any local payload that misses it. C-59: two low approximants localized to disjoint, easy-decoding regions combine by a mux, so the table cannot be above the OPS high threshold. A short-transversal hypergraph counterexample prevents inferring a localized approximant merely from every short list hitting the region. C-60: Kannan's source language depends on fixed exponent k; after table generation and decoding, the total exponent e_k must still be below k.

**Smallest theorem.** A high-promise, all-valid-output reduction with controlled exponent blowup, or a semantic selector lower bound that bypasses reductions.

**Status.** No such reduction yet. Keep this queued below direct O-1 and universal-selector lower bounds; do not develop another local patch gadget without a new mechanism.

**C-61 update.** If the reduction's decoder relies on every valid query list touching each of many pairwise-disjoint regions, this cannot work: the common dual-margin distribution forces each mandatory region to have mass $3/10-o(1)$, allowing at most three. A surviving design must encode through overlapping or nonlocal correlations, or avoid reductions and attack S-1 directly.

**Fractional form.** Any fractional packing of mandatory regions has total weight at most 10/3+o(1), so bounded-overlap families are also limited to constant packing density.

**C-62 update.** For output-only decoding, opposite-answer tables must differ on at least p*=0.3-o(1) mass under each endpoint's dual witness; otherwise one valid labeled list serves both. This condition does not apply when the decoder also uses the original source input.
## Q31 - Agreement fibers expose the selector's exact failure witness

Given a candidate selector S and low circuit D, define \(A_D^S=\{f:f|_{S(f)}=D|_{S(f)}\}\). S succeeds on all high tables exactly when every such fiber is contained in \(SIZE(s_2)\). The selector lower bound asks whether some fiber must contain a high table. Fiber membership has a circuit of size \(O(|S|+t(N+s_1+n))\), including the address-dependent table muxes.

**What this adds.** It turns the self-consistent completion problem into a family of explicit circuit-supported sets and makes the quantifiers auditable. It does not lower-bound S: for the class of two constant functions, a linear-size priority selector has singleton agreement fibers.

**Next attack.** Find a property of the full size-s1 circuit classÃ¢â‚¬â€likely closure under patching or a richness/extension propertyÃ¢â‚¬â€that forces one self-indexed agreement fiber to escape SIZE(s2). Try to prove or falsify that property for arbitrary address feedback before deriving any exponent claim.

**Status.** Exact reformulation proved; target lemma open. See C-63 and [the reset audit](RESEARCH_RESET_2026-09-25.md).
## Idea 229 - Lower-bound only minimax-length selector outputs

Under NP subset P/poly, C-48 constructs a valid selector of length O(s1 log(s1+n)) and circuit size N^(1+O(beta)). Therefore a lower bound for every selector restricted to K_n=C0 s1 log2(s1+n+2) outputs, for all sufficiently small fixed beta in an interval, still gives NP not-subset P/poly. This is a sharper target than lower-bounding selectors with the full OPS budget 2^(10 beta n).

C-49 adds a robust trace property: these short lists differ from every size-s1/2 circuit trace on Omega(s1/n) coordinates, a relative distance Omega(1/n^2). The challenge is to turn that margin into a bound on the shared circuit that routes f to the list. The output length remains far below N, but output sparsity alone gives only the existing linear input-support lower bound.

**Status.** Conditional implication proved as C-66; short-selector circuit lower bound open. Prefer this over broad S-1 for the next attack because it is sufficient and more constrained.

**Concrete failed catalogue gadget.** The proposed A=G_(1,0), B=G_(2,0), C=A intersect B, E_j=A union D_j, H_j=B union D_j construction encoded incidence only on listed pairs. The unlisted pair (A,B) has consequence C and violates every encoded filter at once. Including C in each filter forces all C union D_j by upward closure, erasing the incidence choices. Thus no artificial gap has been embedded in the actual semantic model.

## Q34 - Activation-set circuit lower bound (new formal interface)

C-74 rewrites a q-pair list as q positive recursive states over anchor space. State i activates on the intersection of two unions: a union of literal half-cubes and previous states admitted by endpoint containment on each side. The least fixed point yields a set K_Q that avoids every high table. A successful cover of Y must therefore implement a promise separator Y subseteq K_Q subseteq {0,1}^N minus U.

The semantic endpoint sets disappear into a fixed directed incidence relation T_j subset E_i,H_i; no entropy is assigned to that relation. The count q measures the number of recursive intersection states. Unrolling gives at most q^2 AND gates, so ordinary circuit lower bounds lose too much; the target is a lower bound directly on this recursive program or a semantic structural restriction that improves the unrolling.

**Adversarial tests.** Any invariant must allow C-73's shared two-literal state, catch the unlisted (A,B) shortcut, and respect C-72's logarithmic proof-depth floor. The depth bound alone only implies the existing local linear scale.

**Literature hook.** Monotone-circuit conjunctive complexity studies AND-gate count, but existing results do not directly cover dual-rail inputs, recursive least fixed points, and a low/high promise separator. Use it to look for methods, not as a ready theorem.

**Status.** Formal model proved; separator lower bound and realizability converse open. No P-versus-NP progress yet.

## Q35 - Karchmer-Wigderson communication game (closed for the present target)

For low w and high z, the pair-list proof gives an interactive mismatch-finding protocol. Bob picks an endpoint side unsupported at z; Alice supplies a support for that side at w. A literal support outputs a coordinate where w and z differ; a prior-state support descends to a state active at w and inactive at z, with strictly lower activation rank. The protocol uses at most q states and O(q log(N+q)) bits (C-75).

**Why this does not advance O-2.** The deterministic communication complexity of this low/high mismatch relation is at most O(s1 log s1 + log N): Alice can send a size-s1 circuit for w, then Bob finds a coordinate where z disagrees. This is N^(beta+o(1)), below the already known local q >= N-o(N) lower bound. Communication bits lose the shared-DAG/state-count information that matters.

**Learning.** Any KW-style continuation must lower-bound protocol DAG size or state complexity directly, not depth/communication cost. The generic separator simulation from C-74 already points to this; do not present this protocol as new asymptotic progress.

**Status.** Exact simulation proved; this direct communication-complexity route is dominated and inactive.

**Precision note (C-74).** The activation recurrence retains exactly the seed clauses, containment incidence sets P_i,R_i, and empty-consequence flags. These data are induced by actual semantic endpoints and satisfy set-inclusion constraints; an arbitrary recursive intersection program need not be realizable by a pair list.

## Q36 - Lower-bound shared seed clauses plus their monotone decoder

C-76 factors any successful list through its 2q seed bits sigma(w)=(a_1,b_1,...,a_q,b_q). The least-fixed-point output h_Q(s) is monotone in s. Hence no low seed vector can lie below a high seed vector. For each low w, the conjunction of every nonconstant seed clause true at w is a CNF certificate whose satisfying tables all have circuit complexity at most s2. A satisfiable m-clause CNF has at least 2^(N-m) models, so every low w satisfies at least N-log_2(M2)=N-o(N) seed clauses. Its family of matched-literal supports also has transversal number at least N-o(N).

**What this sharpens.** The pair system cannot use its recursive wiring to recover information absent from the seed vector. This exposes the division of labor: clauses supply a one-sided code; the monotone fixed-point decoder selects the low patterns.

**Why this alone stalls.** The clause-count conclusion is only q>=N/2, weaker than the local N-o(N) pair lower bound. An abstract dictionary of the 2N signed unit clauses gives every table an isolating minterm, so feature counting alone does not force superlinear size. The lower bound must charge how q recursive states decode those features while sharing across all low anchors.

**Next theorem.** Lower-bound the number of semantic states needed by a monotone decoder h on any clause dictionary whose low fibers are CNF traps for all high tables; or prove a structural property of actual endpoint-incidence networks that prevents the 2N-unit dictionary from being decoded cheaply.

**Status.** C-76 proved; no superlinear consequence yet.


### Q37 Ã¢â‚¬â€ Ranked cyclic rectangle non-shareability

**Prompt.** The C-77 activation recurrence is a cyclic monotone conjunctive program with q AND states and an input-specific rank decreasing along every valid low/high mismatch path. Find an invariant that lower-bounds q directly, without unfolding to an acyclic rect-DAG.

**Known limits.** Ordinary communication bits are too weak (C-75). The generic binary-fanin DAG expansion costs \(O(q^3)\); the acyclic AND-only expansion costs qÃ‚Â². A restricted low/high DAG need only separate the promise and may accept medium tables. A valid lower bound should either apply to the exact \(D^\circ_\cap\) model or prove a separator lower bound strong enough to survive these losses.

**First proof subgoal.** For each state rectangle \(R_i=A_i\times B_i\), quantify how many low anchors / high tables can share each decreasing transition \(i\to j\), and prove that a cyclic dependency SCC cannot compress too many independent literal mismatches. Any proposed charging scheme must survive the 2-state cycle example and the previous per-anchor, fractional, and fixed-family ceilings.

**Status.** Open. No lower bound or counterexample construction yet.


**Quantitative bridge (C-77).** Let SepAnd(Y,Z) be the minimum number of acyclic monotone AND gates separating low tables from high tables on signed-literal inputs; medium tables are unconstrained. Every q-pair cover gives SepAnd(Y,Z) <= q^2. Proving SepAnd(Y,Z) > N^(2+2 epsilon) would imply the target rho > N^(1+epsilon).

## Q38 Ã¢â‚¬â€ Lower-bound residual rectangles, not transcript depth

Keep separate the total mismatch relation \(Y\times Z\), the Q-dependent ranked closure-witness relation, ordinary communication bits, protocol-tree nodes, and acyclic rect-DAG nodes. A circuit description gives \(O(s_1\log(n+s_1)+\log N)\) communication but only an exponential generic DAG upper bound. A successful Q gives a direct rank-layered rect-DAG of size \(O(q^2(q+N))=O(q^3)\); the q-state dependency graph itself can cycle.

The interval-pattern construction gives a universal DAG of size \(O(|Y|+\sum_{I\ dyadic}\pi_I(Y))\). Candidate non-shareability statistic: the number of distinct residual restriction patterns. Current evidence is upper-bound-only; no theorem forces an arbitrary DAG to expose these states.

**Next attempt:** find a fooling family or rectangle bottleneck lower bound for MCSP mismatch whose quantitative scale exceeds \(N^{3+3\epsilon}\), or work directly in the cyclic intersection model to avoid the cubic loss.

**Status:** formal bridge proved, lower-bound handle open. See C-78 / O-79.

## Q39 Ã¢â‚¬â€ Promise-to-exact transfer must pay for the medium band

For low \(Y=\mathrm{SIZE}(s_1)\), medium \(M=\mathrm{SIZE}(s_2)\setminus Y\), and high \(Z=\mathrm{SIZE}(s_2)^c\), every signed truth-table cylinder contains a medium table for sufficiently small fixed OPS \(\beta\). The upward closure generated by \(M\) and the matching literal slices of any low anchor is a semi-filter above that anchor. Every pair with endpoints in \(Z\) misses it.

This proves that a cover/endpoint list for the larger positive class \(\mathrm{SIZE}(s_2)\) cannot simply be reused for \(Y\). It does not rule out new pairs involving M.

**Next attempt:** quantify the minimum extra pair cost required to hit the medium-band escape filters, or show that a promise rect-DAG cannot be converted to an exact low-set cover from size alone.

**Status:** obstruction proved; conversion question open. See C-79 / O-80.

## Q40 Ã¢â‚¬â€ Lower-bound incompatible partitions, not the number of anchors

For a fixed block partition of truth-table coordinates, the whole family of \(2^{\Theta(s_1)}\) low tables constant on those blocks has an \(O(N)\)-vertex DAG against all high tables. Every high table is mixed on a block; Bob finds one, Alice gives the low bit there, and Bob chooses an opposite coordinate.

For each individual low table \(w\), every high \(z\) varies on at least one of \(w^{-1}(0)\), \(w^{-1}(1)\), since otherwise \(z\in\{0,1,w,\neg w\}\) and is low. Candidate non-shareability target: quantify the number of incompatible low-induced two-block partitions a single DAG state can serve.

**Status:** fixed-partition route decisively too easy; full varying-partition lower bound open. See C-80 / O-82.


## Q41 - Row-signature diameter and its ceiling

Equal full row signatures in a rect-DAG force low-table distance at most log|SIZE(s2)|. A C-80 code gives S_rect=Omega(s1), after taking the logarithm of the number of signatures. This is a real non-shareability lemma but cannot reach the target: row-signature counting is capped by log|Y|=N^(beta+o(1))=o(N).

## Q42 - Column signatures are low-excluding certificates

Equal high-column signatures force their common agreement restriction to have no low completion. Minterm interpolation supplies a low completion for every pattern on O(s1/n) coordinates, but large irregular restrictions need not be low-completable. No column packing bound follows yet.

## Q43 - q states are cyclic loop states

A successful fusion list is an input-ranked cyclic witness game with q states and O(q^2+qN) support arcs. This is exactly D^circ_cap=rho, not a standard acyclic DAG. Binary acyclic rank unrolling remains O(q^3) vertices. Seek a compression theorem respecting endpoint containment, or work directly in the cyclic model.


## Q44 - A whole row class has a high-free common core

Fix a row-signature class R. For every high z, all pairs (w,z), w in R, have the same reachable output leaves. A common leaf must be valid for all rows, so its coordinate is fixed across R. Therefore the coordinates fixed by all rows in R, with their common pattern, form a cylinder containing no high tables. Counting forces at least N-log|SIZE(s2)| fixed coordinates.

**Learning:** this upgrades pairwise diameter to a common certificate for each state class. It still gives only a cylinder-cover bound S >= log C_cyl; singleton cylinders and the medium band block a superlinear transfer. Need charge transitions among such cylinders.


## Q45 - Cross-signature classes need a common separating coordinate

Partition Y and Z by their full row and column signatures. Every class product R x C has identical feasible leaves for all pairs, so one common leaf must be valid throughout the product. Hence the common-coordinate cores of R and C intersect at a coordinate with opposite fixed bits.

**Open step:** turn this class-pair condition into a lower bound on the number of classes or on the DAG routing structure. A cover by 2N signed-coordinate rectangles exists, so leaf-cover counting alone is too weak.

Counting signatures cannot reach the transfer scale: row classes give at most log|Y|=o(N), columns at most N, and class pairs at most N+o(N). A useful argument must lower-bound routing cost rather than class count.


## Q46 - History merging fails at the node-validity condition

A scan-and-merge state labelled by the full product Y x Z remains valid for all pairs, including pairs that already differ on the scanned prefix. It cannot switch to a suffix-only search. Restricting to prefix-equal pairs is not one rectangle unless the exact common pattern is retained.

**Learning:** this kills the simple O(N) universal scan, not arbitrary sharing. Any small DAG must preserve residual validity in its rectangle labels.


## Q47 - Fixed linear fingerprints cannot beat N-o(N)

A rank-r linear map on the N truth-table bits has fibers of size 2^(N-r). If r<N-log|SIZE(s2)|, every fiber contains a high table. Therefore each low input shares its sketch with some high input.

**Scope:** exact for linear sketches and fixed coordinate samples; no conclusion for nonlinear summaries or adaptive DAGs.

## Q48 - Circuit descriptions do not make interval mismatch rectangular

Let G(d) be the table of a short circuit description. For each interval I, restriction-pattern rectangles {d:G(d)|I=u} x {z:z|I!=u} give a valid shared DAG. The predicate that there is a mismatch somewhere in I mixes d and z, so this construction must preserve u. The profile bound is still far from near-linear.

**Open:** exploit syntax to route more efficiently, or prove that every shared protocol pays for a comparable residual-pattern family.


## Q49 - Replace generic DAG lower bounds with SepCirc

The signed-mismatch rect-DAG for Y x Z is equivalent up to constants to the minimum Boolean circuit separating low tables from high tables. A fusion q-cover maps to this circuit with O(q^3) size. Thus a separator lower bound with exponent margin above N^3 implies the desired superlinear rho bound.

**Limit:** the DAG/circuit pair is a promise separator. By C-90 it yields the active promise cover with O(L) pairs; medium tables matter only for upgrading to the different full-domain exact cover. The equivalence still gives no lower bound.

## Q50 - Separate promise and full-domain covers

The active \(\rho_{\rm prom}\) uses \(\Gamma=Y\sqcup Z\), while \(\rho_{\rm full}\) includes the medium band in its universe. A rect-DAG for \(Y\times Z\) gives a separator circuit, hence a promise cover with O(L) pairs. A full cover restricts to a promise cover. C-79 only blocks the reverse upgrade by reusing endpoints inside Z.

**Learning:** the medium-band escape is not an obstruction to the requested reverse transformation for the projectÃ¢â‚¬â„¢s actual promise. It only separates promise and exact full-domain formulations. Continue with direct cyclic q lower bounds or faster acyclicization.
## Q51 - Localize the cyclic cost to strongly connected components

After deleting the redundant self-support arcs, use a directed support edge j -> i when T_j is contained in an endpoint of pair i, and let e_C count the two-sided incidences internal to SCC C. C-91 proves a fan-in-two separator bound O(qN+q^2+sum_C(r_C e_C+r_C^2)), improving O(q^3) when support incidence or SCC width is low. Next inspect endpoint-induced structure inside a largest dense SCC: can alternatives be quotiented by equal supports or dominated states without increasing the charged intersections? Any quotient must preserve both side-support predicates and the least fixed point on every truth-table input.

**Limit:** no bound on the weighted internal support incidences follows from current arguments. One large dense nontrivial SCC leaves the cubic worst case intact; sparse or acyclic loop-free support graphs compile in quadratic total size.

## Q52 - Remove transitive two-sided carrier supports

After self-loop deletion, quotient the distinct carriers T_i by inclusion. Remove a lower-carrier rule state from both supports of i whenever its carrier is a strict non-cover subset of T_i. Retained cover incidences exist on both sides, so in every fixed point activation propagates upward along every carrier inclusion. Any deleted term into i is therefore redundant: it can be true only when i itself is already true. C-92 proves that this pruning preserves the least fixed point.

**Learning:** nesting creates many support incidences but not necessarily genuine recursive complexity. The remaining incidence question must account for one-sided supports and equal-carrier alternatives; no lower bound follows from the pruning.

## Q53 - Quotient duplicate carrier states but keep rule alternatives

Group states by distinct carrier t=T_i. If the group has at least two states, all have the same final activation bit because every peer carrier supports both endpoints. The group's activation condition is the OR over its candidate conjunctions c_i=(seed-left OR other carriers) AND (seed-right OR other carriers). C-93 proves that the resulting p-state least fixed point lifts exactly to the q-state recurrence and gives the carrier-SCC compiler O(qN+e_out+sum_C p_C(e_C+q_C)).

**Learning:** quotienting reduces the recursion depth and SCC width to p distinct carriers, but does not merge candidate conjunctions. OR_i(A_i AND B_i) cannot generally be replaced by (OR_i A_i) AND (OR_i B_i), because that creates cross-pair activations. The next possible compression has to preserve this alternative-specific compatibility.

## Q54 - Factor shared cover propagation; charge escape feedback

After C-92/C-93, every strict-subcarrier support still present is a carrier-poset cover and appears on both sides. Factor the common signal K_t=OR_{u covered by t} x_u from every candidate conjunction. The residual candidate supports are one-sided and come from carriers u not contained in the target carrier t. Thus every dependency cycle uses an escape edge. C-94 replaces each Hasse round by upward closure of the escape-triggered candidate set; if s distinct carrier values occur as escape sources, at most s+1 macro rounds are needed.

**Compiler:** O(qN+(s+1)(xi+kappa+q)), where xi is candidate-side escape incidence and kappa is the number of carrier covers. If there are no escape supports, this is O(qN+q+kappa).

**Learning:** the true feedback resource is not total containment incidence; it is the one-sided escape system. The next task is to lower-bound its non-shareability or find a compact router. C-94 proves no lower bound on s, xi, or q.

## Q55 - Every low contradiction passes through an empty-rule escape

The two literal seed clauses of any empty-carrier candidate cannot be jointly satisfiable: fixing one true literal from each fixes at most two table bits, leaving at least 2^(N-2) satisfying tables, one of which is high because M2<2^(N-2). Direct activation at that high table would contradict the principal filter. Therefore every low anchor that activates an empty carrier uses an escape source in S_0, the carriers appearing on one-sided supports of empty rules.

**Learning:** the proof endpoint is localized: \(Y\subseteq\bigcup_{u\in S_0}X_u\). This does not lower-bound |S_0| because a source activation set can cover many low anchors. The next step must couple these activation sets to the opposite-side blocking condition on high tables.

When both seed clauses are nonempty, their necessary unsatisfiability forces them to be opposite unit literals on one truth-table coordinate. Thus the missing escape side is determined by that coordinate's value; if one clause is empty, its side always needs an escape. Try to exploit these coordinate-indexed terminal routes without assuming different rules have disjoint anchor sets.

## Q56 - Cross-anchor shareability of terminal support cones

C-96: every low anchor w has a terminal causal cone C(w) containing at least (N-log2 M2)/2 true seed clauses. The proof is a high-free CNF model-count argument. This does not beat q>=N-o(N), and the cones may overlap almost entirely.

**Next:** seek a structural constraint on how one shared state/cone can serve different low anchors while preserving the high-side block. Do not count incidences as if cones were disjoint.

## Q57 - Quotient description rows; attack range separation

C-97 proves that a standard mismatch rect-DAG on circuit descriptions D1 x Z has exactly the same minimum size as on truth tables Y x Z. Lifting predicates through G:D1->Y gives one direction; restricting along a section gives the other. Short descriptions lower communication bits but do not lower protocol-tree or shared-DAG node count.

The rect-DAG is equivalent to a Boolean separator circuit for Y versus Z. Universal evaluation of G(d)(k) does not decide the range-separation promise or make the interval mismatch predicate a rectangle. The pattern-indexed scan costs O(|Y|+sum_I pi_I(Y)); its failure is architectural, not a lower bound.

**Next:** either construct a standard N^(1+o(1)) separator DAG (which would kill the desired superlinear rho route), or prove a non-shareability lower bound for arbitrary rect-DAGs / directly for cyclic rho. Preserve the cubic conversion loss: a separator lower bound must exceed N^(3+3epsilon) to force q>N^(1+epsilon) through the generic q^3 compiler.

## Q58 - Use PRFs as a conditional benchmark, then isolate the unconditional gap

C-98: if one-bit PRFs remain secure against nonuniform polynomial-size distinguishers with polynomially many queries, every standard rect-DAG separating Y from Z must be superpolynomial in N. A separator would query all N padded inputs, recognize every PRF table as low, and reject almost every uniform table as high. The threshold works because N^beta/(cn) can dominate any fixed polynomial evaluation size after choosing N=Theta(lambda^a), while N^beta log N=o(N).

**Learning:** short descriptions do not make the range easy to separate; cryptographic pseudorandomness formalizes that barrier conditionally. The literature already uses this MCSP/PRF principle, so the project-specific value is the exact promise-parameter and rho-transfer calculation, not a novel cryptographic idea. The proof still needs an unconditional non-shareability invariant; the assumption itself is not an unconditional P-vs-NP result.

## Q59 - Do not mistake the PRF benchmark for an independent proof route

C-99: if NP were contained in P/poly, the NP language MCSP would have polynomial circuits. Fix the threshold at s2; the resulting separator accepts all Y and rejects all Z. C-98 then turns it into a nonuniform PRF distinguisher using N polynomially many queries. Therefore the nonuniform PRF assumption itself implies NP not subset P/poly.

**Learning:** C-98 gives a useful conditional scale check for the cyclic/rect-DAG bridge, but the cryptographic premise is already at least strong enough to prove the target separation. Uniform PRFs do not repair this because the separator circuit family may be nonuniform. Return to an unconditional DAG or cyclic-state invariant for actual progress.

## Q60 - Batch shared OR frontiers before acyclicization

C-100: instead of separately building \(r\) ORs over the same \(m\)-bit input vector, partition the vector into blocks of about \(\log r\), compute every subset OR per block once, and assemble the requested ORs. The circuit size is \(O(r(1+m/\min\{m,\log r\}))\). Applied to C-94, this batches literal seeds, escape supports, and carrier down-sets; the worst-case q-to-DAG compiler improves from \(O(q^3)\) to \(O(q^3/\log q)\).

**Learning:** sharing has a real but limited arithmetic payoff: it removes a logarithmic factor from repeated OR routing. It does not remove the \(s+1\) fixed-point rounds or the need to distinguish a promise range. The strongest remaining route is still a lower bound on cyclic \(q\) itself, or an unconditional separator lower bound above \(N^{3+3\epsilon}/\log N\). Do not mistake this compiler optimization for non-shareability.

## Q61 - Recast terminal proof cones as contained truth-table cubes

C-101 defines Delta_box(s2), the largest coordinate subcube of truth tables wholly contained in SIZE(s2). Selecting one true literal from each clause of a C-96 terminal-cone CNF yields m >= N-Delta_box(s2). Circuit counting gives Delta_box <= O(s2 log(n+s2)), reproducing only N-o(N). A localized input subcube gives Delta_box >= Omega(s2); do not confuse this with C-80's block-constant family, whose coordinates are correlated.

**Learning:** VC dimension is not the right strengthening by itself. The cone needs a cube with one common outside pattern, and the generic count gives exactly the old ceiling. The remaining issue is overlap between cones, not the local number of seed clauses.

## Q62 - Use fiber disagreement as an alternate total relation, not as a DAG lower bound

C-102: if z were constant on both fibers of a low w, then z would be a unary postprocessing of w and therefore low. Thus every high z cuts an edge inside one of the two cliques induced by w's fibers. A witness pair (a,b) has a rectangle-local certificate: Alice checks w(a)=w(b), Bob checks z(a)!=z(b).

**Learning:** the O(N^2) rectangle cover gives a short nondeterministic witness, but deterministic DAG routing must handle candidate pairs where only one party's predicate succeeds. This exposes exactly why certificate existence is not state sharing. No fusion-path transfer or lower bound follows yet; the C-75 mismatch relation remains the target.

## Q63 - Use the fiber relation as an upper-bound falsification target

C-103 proves S_mis <= O(S_fib), but C-105 now gives S_fib >= Omega(N^(2-beta)/log N), closing the near-linear fiber-DAG falsification branch. This does not transfer to rho because C-104 loses N^2. C-106 gives the only direct candidate: extract an O(q log^d N) universal fiber-edge set from Q; no such map is proved.

## Q64 - Close the fiber relation's reverse conversion and reject it as the main lower-bound route

C-104 constructs a fiber-search DAG from a signed-mismatch DAG by running mismatch games on constants 0 and 1, storing their outputs (p,q), then using w or not-w to produce a third point. The copy index retains (p,q), so the size is O(N^2 S_mis); use Y^-=SIZE(s1-1) so not-w remains in Y. Along with C-103 this settles the comparison only with an N^2 loss. A fiber lower bound would need to exceed O(N^(5+3epsilon)/log N) to force the fusion target through C-100.

**Learning:** the fiber reformulation is useful as a falsification test but quantitatively inferior as a proof route. Return priority to direct cyclic non-shareability or promise-separator lower bounds.


## Q65 - Lower-bound the fiber DAG's output labels using affine subcubes

C-105: any leaf-output set E for fiber disagreement must induce Omega(a) edges inside every affine subspace A of size a=Theta(s2 n). Otherwise many isolated vertices in E[A] support 2^(Omega(a)) sparse modifications z=1_(A\S); since this exceeds the size-s2 circuit count, at least one is high, yet none of E is a valid output against w=1_A. Averaging over random affine A gives |E|=Omega(N^2/(s2 n))=Omega(N^(2-beta)/n).

**Learning:** a fixed universal answer list is substantially more expensive than an ordinary mismatch-coordinate list. This is a real superlinear lower bound for the auxiliary fiber search, but C-104's N^2 reverse loss erases it when transferred to rho. Seek a direct fusion-to-fiber map with smaller output-index memory, or return to the cyclic q-state invariant.

## Q66 - Use C-105 only through a direct edge-set extraction from Q

C-105 proves that every fiber-disagreement DAG needs Omega(N^(2-beta)/log N) distinct output edges. This rules out the near-linear DAG falsifier for that auxiliary relation, but C-104's N^2 reverse loss makes it useless as a mismatch/rho lower bound.

C-106 isolates the only promising transfer: a q-state fusion cover would have to yield a fixed universal fiber-edge list E_Q of O(q log^d N) edges. Then the label lower bound would force q=Omega(N^(2-beta)/(log N)^(d+1)). The closure path currently outputs only one signed mismatch; another arbitrary point may lie in the opposite low-table fiber. Derive E_Q from rule supports or abandon this transfer explicitly. Keep direct cyclic non-shareability as the main target.


## C-107 - Why the pairwise-parity lift fails

The obvious lift compares parity(w(a),w(b)) with parity(z(a),z(b)); it reports a mismatch both when w is equal and z differs (valid) and when w differs and z is equal (invalid). This is not an accident of parity. At one candidate pair, valid outputs occupy A x B, with A={00,11}, B={01,10}. Because both complements are nonempty, any independent local code F(u),G(v) whose entire mismatch set is contained in A x B must be constant and equal, so it has no output. Thus a raw one-shot lift cannot make every mismatch valid; a stateful protocol might still route to a valid one.

This leaves a precise kind of novelty worth pursuing: a stateful shared DAG must use its history to avoid false cross-pattern mismatches while preserving at least one valid pair for every low/high input. That is global routing/non-shareability, not an ordinary parity or universal-circuit trick.


## Q67 - Pin the auxiliary fiber certificate list within polylog factors

C-108 uses the patching lemma: if z differs from a unary postprocessing of low w on t coordinates, CC(z)<=CC(w)+O(nt), so a high z is at distance Theta(s2/n) from each unary map. A random graph with p=Theta(n^2/s2) edges per pair hits every cut of that size on every low-w fiber, by a union bound over the 2^(O(s2)) low rows and all cuts. It yields a universal fiber output list E of O(N^(2-beta)n^2) edges. C-105 gives Omega(N^(2-beta)/n), so the list optimum is tight up to O(log^3 N).

**Learning:** certificate existence is much cheaper than a routed shared DAG. The residual after a failed candidate is a union of rectangles, so a pointer-only scan cannot be merged into one suffix state. A correct DAG by enumerating low rows costs 2^(O(s2))|E|; the deterministic routing gap remains. This is auxiliary and does not transfer to rho.

## Q68 - Separate certificate-list optimality from deterministic routing

C-108 establishes a universal fiber-edge list of O(N^(2-beta)n^2), and C-105 gives Omega(N^(2-beta)/n) for every such list. Thus the nondeterministic answer-list size is determined up to log^3. This does not upper-bound the deterministic rect-DAG: checking candidate i leaves a residual that is a union of Alice-failure and Bob-failure rectangles, not one rectangle. The shared node would need enough history to rule out skipped earlier intersections.

**Next test:** exploit the special form P_w={edges whose endpoints agree under w} and Q_z={edges crossing z}, rather than arbitrary set intersection. Seek a compact deterministic router or a fooling family proving that the histories cannot be shared. Any such result still needs a transfer to the q-state fusion target.

## Q69 - A logarithmic set of low rows cannot form a fiber-output fooling family

C-109: combine r<=eta n low tables into W(x)=(w_1(x),...,w_r(x)). If high z were constant on all W-fibers, it would be h(W) and have circuit size at most r s1+O(r2^r)<s2. So every high z has an edge whose endpoints agree on all r rows and differ on z.

**Learning:** this is a common output *per column*, not one fixed edge over a column rectangle. It does not make a small DAG, but it shows that counting a small tuple of row anchors as mutually incompatible cannot prove non-shareability. The real quantity must charge the varying edge choice / column routing, not just how many rows a state serves.


## Q70 - Charge the cross-pairs created by state merging

C-110: a standard rect-DAG node is a rectangle, so merging contexts \(A_i\times B_i\) also admits \(A_i\times B_j\). Descendant outputs must solve every cross-pair. A suffix scan cannot merge distinct equal-prefix histories when a cross-pair agrees on the suffix. The same invariant gives each fusion state a coordinate set separating its active-low rows and inactive-high columns.

**Next:** compute cross-pair obligations for circuit-description prefixes or universal-circuit states on the actual Gap-MCSP promise. The full-cube prefix counterexample is not a lower bound for the promise. A useful result must force either many retained contexts or many additional descendant outputs, then connect that charge to q or \(\rho\).


## Q71 - High-mask splices force prefix state, but common partitions bypass it

C-111 uses circuit counting to choose a within-block mask p with both p and its complement above \(s_2+O(k)\). Any two distinct block-constant low tables spliced across P={p=1} and J={p=0} produce a high table: on a block where the rows differ, the splice restricts to p or its complement. The splice equals the first row on J and the second on P. Hence all off-diagonal prefix contexts have cross-pairs with no J-mismatch, and a prefix-first/suffix-only rect-DAG needs \(2^{\Theta(s_1)}\) states.

**Learning:** this is real-promise non-shareability for one architecture, not a global lower bound. The same low family has the O(N) mixed-block DAG from C-80. A general lower bound must rule out adaptive structural witnesses and incompatible circuit partitions, not just cross-pair splices.


## Q72 - Random coordinate splices amplify a separated low code

C-112: for a code C of K truth tables and minimum distance d, a random subset P gives each ordered pair's hybrid uniformly over 2^d completions. If d>2log K+log|SIZE(s2)|, a union bound yields one split where all off-diagonal hybrids are high. A constant-distance subcode of the C-80 family has K=2^{Omega(s1)}, d=Omega(N), so the condition holds for every fixed beta<1.

This forces a prefix-first/suffix-only rect-DAG to keep every codeword's P-pattern context separate: the splice is high, has the second row's P-pattern, and matches the first row on J. The O(N) mixed-block DAG still evades the lower bound. Use the lemma to test other router architectures, but do not infer general DAG hardness.


## Q73 - Move from static split incompatibility to adaptive partition diversity

C-112 makes every cross-splice high across a separated low code, but C-80's common block partition lets Bob find a mixed block without learning the P-pattern. Thus static product-hull incompatibility can force exponential state in one scan order while an adaptive DAG stays linear.

**Next:** build a low family whose circuit-induced partitions have no small common coarsening, then quantify how any rect-DAG must either identify the active partition or carry enough state to test several. A useful argument must survive adaptive search and give a size lower bound, not just a bad fixed coordinate split.


## Q74 - Count-state search routes all low k-juntas

C-113: for a low function with at most k essential variables, Alice can choose a k-set S containing its support. Any high z has >k essential variables. Thus \([n]\setminus S\) and \(\operatorname{Ess}(z)\) intersect. A balanced interval PLS with states recording exact counts \((a,b)\) and invariant \(a+b>|I|\) finds a common direction in n^{O(1)} rect-DAG states after the PLS conversion. Bob then selects a boundary edge of z in that direction; w is constant on it, yielding a mismatch. Size O(N log N+polylog N).

**Learning:** the \(\binom nk\) possible variable supports are not enough to force a large DAG. A harder family must hide high complexity within the same support set, so support cardinality cannot witness the needed fiber split.

## Q75 - Reusable count-intersection PLS template

C-114 abstracts C-113. If each input pair gives local sets \(A_x,B_y\subseteq[n]\) with \(|A_x|+|B_y|>n\), balanced interval states store their exact counts and descend to a common element. This yields an acyclic PLS of O(n^2) states and O(log n) communication per step, hence an n^{O(1)} rect-DAG. A valid suffix can be shared once per output index if its full product rectangle solves the relation.

**Use and boundary:** search for alternative low-circuit/high-table witness sets satisfying the cardinality condition or another similarly compact PLS invariant. The irrelevant-variable instantiation fails for parity, already a low all-essential function. This closes only that simple generalization; it does not close O-99/O-93.

## Q76 - Gate-signature fiber witness; route is unresolved

C-115: select \(k=\Theta(\log s_2)\) wire values of a low circuit C, including the output (input wires may pad the selection), with lookup cost \(O(k2^k)\) below the circuit-size gap. Every high z varies inside some common-signature cell; otherwise z factors through the k wires and is low. By patching, the total number of minority assignments over cells is \(\Omega(s_2/n)\).

**Next:** find a shared rect-DAG that routes to a varying cell without storing the full circuit partition, or prove that product-hull cross-pairs force many states. The variation may concentrate in one cell, so count-intersection does not automatically apply. C-80 still defeats arguments based on a single fixed partition. This is a witness lemma, not a DAG lower bound.

## Q77 - Cofactor hardness is easy to locate, hard to transfer

C-116: with \(m=\Theta(n)\) fixed prefix cofactors, a high table must have a cofactor of circuit size \(>4s_1\), while every low table cofactor has size \(\le s_1\). Bob can choose the hard cofactor, giving an \(O(m)\)-branch DAG reduction to a smaller constant-factor-gap mismatch problem.

**Learning:** this spends the original \(\Theta(n)\) gap. The reduction is only \(S_{\rm large}\le O(nS_{\rm constant-gap})\). A hard marker cannot reverse it because the marker itself creates an easy mismatch. Find a gap amplifier that preserves the output location, or return to a direct lower bound for \(\rho\)/the cyclic closure game.

## Q78 - Exploit exact padding only where parameter margins survive

C-117 gives no-size-loss monotonicity for the mismatch rect-DAG under ignored-input padding. With a fixed shift \(\beta'>\beta\), a lower bound exponent \(\gamma\) transfers to \((\beta/\beta')\gamma\) at the original dimension. This is useful only if \(\gamma\) clears the target after that loss and the theorem is uniform at \((\beta',c\beta'/\beta)\). It does not transfer lower bounds from C-116's \(4s_1\) high-cofactor promise.

## Q79 - Pull back semi-filters to transfer \(\rho\) without a DAG

C-118 proves \(\rho_{\rm prom}(n-k;s_1,s_2)\le\rho_{\rm prom}(n;s_1,s_2)\). Restrict big pair endpoints to the lifted smaller high domain. A failed small cover would give a semi-filter \(\mathcal F'\); its inverse image under \(A\mapsto A\cap Z^\iota\) is a proper upward-closed big filter above the lifted low row and preserved by every original pair. Contradiction.

This avoids the q-to-rect-DAG cubic loss. It still needs a direct lower bound at a shifted parameter. For fixed \(\beta'>\beta\), the exponent scales by \(\beta/\beta'\); choose the shift and needed exponent margin before using it.

## Q80 - C-119: padding is exact transport, not a quantifier collapse

Ignored-input padding directly transfers the cyclic cover at fixed absolute thresholds. For rational lambda=p/q>1, compare n=pt with n'=qt and shift (beta,c) to (lambda beta,lambda c). This costs a factor 1/lambda in the exponent and requires a lower-bound theorem uniform over all small fixed shifted betas. A single hard beta remains a single target beta. If the source result is uniform at the shifted c, smaller-low-set monotonicity transfers it to the OPS c0 without padding, so no magnification advantage is gained. Exact subsequences avoid rounding; infinitely-often lower bounds must align with the subsequence. The source cover model allows empty endpoints, and restricted empty-side pairs are vacuous if a variant excludes them.

**Next:** retain C-118 as a direct comparison lemma, but return to O-1/O-99/O-101 for an actual lower-bound mechanism. Do not spend further effort on parameter algebra unless a concrete shifted-parameter theorem becomes available.

## Q81 - C-120: adversarially hide all variation in one signature cell

Fix a low circuit C and any k-wire signature partition with kâ‰ˆ(1/2)log s2, including the output wire. A largest fiber F has at least N/sqrt(s2) points. There are 2^|F| ways to alter w only on F, but only 2^{O(s2 n)} size-s2 truth tables. For beta<2/3, some such alteration is high. The two constant-on-F alterations are computable from C plus a signature equality test, so the high alteration must vary inside F. It agrees with w everywhere else; the C-49 patching margin puts Omega(s2/n) mismatches inside this single cell.

**Learning:** the C-115 witness has no multi-cell dispersal guarantee. Any count-based search for several varying signature cells is falsified. To proceed, the router must either identify one pair-dependent cell across circuit descriptions or use a different invariant that does not require dispersion. This is not a general DAG lower bound; adaptive routing remains open.

## Q82 - C-121: separate common-partition sharing from adaptive sharing

A fixed partition Pi into m cells yields an O(N)-vertex mismatch DAG if every low table is constant on each cell and any cell-constant table can be computed below s2. Bob chooses a cell where z is mixed, Alice supplies w's cell value, then Bob scans that cell for the opposite value. The sum of scan lengths is N. C-80 is one instance.

This architecture cannot cover all SIZE(s1): each point indicator is a low circuit, and it separates its coordinate from every other coordinate, forcing any partition respected by all low rows to be the discrete N-cell partition. Thus C-120's one-cell concentration and C-121's linear router leave one sharp frontier: quantify how much shared state is needed when the partition itself depends on the low row. No DAG lower bound follows yet.

## Q83 - C-122: every small anchor tuple has an O(N) suffix

For any fixed r<=eta n low rows w_1,...,w_r, partition truth-table coordinates by their joint output vector W(x). If a high z were constant on these cells, z=h(W), computable using r s1 gates for the row circuits plus O(r2^r) lookup gates. Choosing eta<min(beta,c/3) keeps this below s2. So z is mixed on a cell common to all rows. Bob selects the mixed cell, Alice gives her row value, and Bob scans for an opposite bit, yielding an O(N)-vertex DAG for the entire tuple.

**Learning:** arbitrary O(n)-sized anchor sets cannot be made pairwise incompatible using only common-fiber witnesses. The group suffix depends on the chosen tuple; naive covering of the full low class by such groups costs O(N|Y|/n). The hard question is how a small DAG might reuse suffixes among groups, or why it cannot.
## Q84 â€” Descriptor invariance leaves a promise-separator problem

C-123 proves exact equality of minimum rect-DAG size before and after replacing each low table by a syntactic circuit description; a section gives the reverse restriction. The DAG is therefore governed by semantic separation, not the description length. Direct enumeration of all descriptions gives size O(NÂ·2^ell), ell=O(s1 log(s1+n)). Universal-circuit evaluation only checks a supplied witness d; it does not compress the existential projection. Next work must attack C_sep(Y,Z) itself or the ranked cyclic cover directly. Keep the quantitative chain rho_promâ‰¤O(S_rect)â‰¤O(rho_prom^3/log rho_prom); do not claim a lower bound from the enumeration or the nonrectangle interval test.
## Q85 â€” Check whether succinct MCSP or SoS can transfer to explicit separator size

C-124 audits two nearby results. Gap-ImpMCSP hardness assumes cryptographic/proof-complexity hypotheses and uses a sampler circuit as the instance; explicit table-separator composition can cost exponential expansion. SoS degree lower bounds certify individual hard truth tables, not one shared separator across Y and Z. Only pursue these as a DAG route if a polynomial-size representation-preserving reduction to C_sep(Y,Z) is found.

## Q86 - Seek a low-cost partial-table encoding of a cyclically hard function

Use C-125: compose the q-state cyclic separator with a monotone map phi. Each YES image must contain a low table code; each NO image must be consistent and extend to a high table. Count the map's a AND gates and seek CycAnd(f)-a > N^(1+epsilon). OR-only maps fail for triangle: low-weight NO inputs force one fixed sign per coordinate, collapsing f to an N-AND conjunction. The direct per-triangle map costs O(r^3) against only Omega(r^3/log^4(r)) known. The remaining target is a factored, variable-witness encoding; none is known. Keep this separate from C-75 shared-DAG non-shareability.


## Q87 - Treat LowExt_Y as the exact target of the partial-code map

Define LowExt_Y(u) by existence of a full low-table one-hot code below u. C-126 proves f=LowExt_Y composed with phi under the transfer hypotheses. Separately require each NO image to have a high completion; otherwise it may be medium and the cyclic separator has no fixed value there. On NO, phi is consistent; on YES it may be conflict-rail rich outside one selected low code. The next lead is a low-AND monotone reduction to LowExt_Y with a high completion on NO, or a theorem that such reductions cost at least the cyclic complexity of f. The free-rail asymmetry is why the C-125 OR-only argument does not generalize immediately.

## Q88 - Use the conflict-support tradeoff for variable low witnesses

C-127: for any two YES inputs x,y, their selected low codes can differ only at coordinates where phi(x OR y) has both rails. If the union S of all YES conflicts has delta coordinates, all low witnesses agree outside S; enumerate at most 2^delta completions to compute f from phi with at most a+N+delta*2^delta AND gates. Thus a transfer proving q>N^(1+epsilon) needs delta >= (1+epsilon)log2(N)-O(log log N). This is only a necessary spread condition, not a q bound. Next try either a conflict-incidence lower bound on a or a construction with logarithmically spread code variation and high NO completions.

## Q89 - Local PRGs handle the promise tree, not the shared DAG

C-128 uses the existing local PRGs to prove formula/tree lower bounds for the low/high promise itself, despite free medium values: random tables are high with overwhelming probability, while every locally generated low table must be accepted. The bounds scale as N^(3 beta-o(1)) for de Morgan formulas above beta=1/3 and N^(2 beta-o(1)) for arbitrary-basis formulas/BPs above beta=1/2. The OPS target needs every sufficiently small beta, and the C-75 object is a shared DAG. Do not transfer this to q without a sharing-preserving theorem. Look for a PRG/fooling argument against the exact rectangle-DAG model or a near-lossless closure-to-BP simulation.

## Q90 - Signature-volume accounting for shared states

C-129: At a rect-DAG state v, every distinct low projection onto its descendant output coordinates forces an entire high-table fiber out of the state rectangle. Quantitatively, if K_v has k coordinates and there are r row signatures, then |Z minus B_v| >= r(2^(N-k)-M2) whenever 2^(N-k)>M2. This sharpens the product-hull rule into an exclusion-volume constraint. The open step is a global charge that avoids paying for the same excluded high table at many states. Stress-test any proposed sum against adaptive rectangle routing and state reuse; a local per-node inequality does not yet imply a DAG or q lower bound.

## Q91 - Adapt bottleneck counting without charging the root

C-131's natural width h_v(w) counts the minimum number of descendant mismatch coordinates needed to hit every high column in B_v. It is already N-log|SIZE(s2)| at the root for every low row, so a direct endpoint-to-bottleneck assignment loads the root with all rows. Every fixed low row also needs N-log|SIZE(s2)| distinct reachable output coordinates, but this invariant only counts distinct coordinates (at most N for fixed w); context-specific internal leaves may still be needed. Beame--Whitmeyer's 2025 method succeeds for Search-BPHP by exploiting collision/equality structure and per-node capacity; no such capacity lemma is available here. Look for a pair-distribution or multiscale width that avoids the root collapse and charges only first routed divergence. Reject any unweighted excluded-volume sum by C-130.

## Q92 - Width alone cannot bound bottleneck capacity

C-132 gives a promise-specific counterexample. Let I have 3N/4 coordinates, P=pi_I(Y), and retain high columns whose I-prefix is outside P. This child rectangle has all low rows, can output only within I, and has natural row width in (N/2,3N/4] for every low row by completion counting. The full root has width N-o(N); splitting off this dense child gives a legal half-width-preserving edge through which every row can be routed into the band [0.4N,0.8N). Hence an assignment based on width crossing can overload one node with all |Y| rows. Track the excluded-prefix family or another path-context statistic; C-130 still forbids raw unweighted exclusion charges. This defeats width-only capacity, not all bottleneck proofs. See C-132/O-112.

## Q93 - Restriction richness kills the current universal-DAG architecture

C-133: the dyadic restriction-sharing DAG stores one state for each interval and low-row restriction. For any k=Theta(s1/n), all 2^k patterns occur on every k-coordinate block via an OR of point minterms, forcing at least (N/k)2^k = 2^(Omega(N^beta/n^2)) states. This is a rigorous falsification of C-78 as a near-linear universal DAG, not an arbitrary-DAG lower bound. Next, look for a routing theorem forcing this kind of profile in general DAGs, or exploit semantic column filtering to build a different small DAG. Any proposed invariant must survive the C-132 all-row width-band rectangle and C-130 repeated exclusions.

## Q94 - Couple row variation to column residuals

C-134 is a counterexample to using low-row projection richness alone: all 2^k tables supported on a k-coordinate block are low, yet their mismatch relation against the high class has a linear DAG because every high table has a 1 outside the block. A useful state potential must record both row variation on descendant outputs and the common witness regions still available on the column side. Test it against C-132's filtered all-row child and C-130's repeated off-path exclusions. No general lower bound is known.

## Q95 - Normalize small-variation row states

C-135: if a state row set A varies on at most d=Theta((s2-s1)/n)=Theta(s1) table coordinates, any table matching one row outside V(A) is still size <=s2. So every high column has a mismatch on a coordinate constant across A, and the entire rectangle can be routed by Bob in O(N) states. The full root has variation support N; the hard step is global. Try to prove either reuse among all small-variation scans gives a near-linear universal DAG, or many pairs are forced through distinct large-variation residual states. Track column filtering; do not infer hardness just from |V(A)|. See O-115.

## Q96 - Attack routing, not witness scarcity

C-136: every low/high pair has at least d+1=Theta(s1) mismatch coordinates. The 2N labelled mismatch rectangles therefore have fractional-cover cost 2N/(d+1)=O(N/s1), and a label-conflict fooling family has at most O(N/s1) pairs; public-coin coordinate sampling finds a witness in expected O(N/d) bits. Yet any fixed universal coordinate sample needs N-o(N) positions. This isolates the open resource as deterministic adaptive state reuse. Seek a lower bound on rectangle-preserving history compression, or a small deterministic DAG that exploits the dense witness sets. Avoid repeating output-count, ordinary fooling-set, or fixed-sample arguments. See C-136/O-116.

## Q97 - Reject joint-input cyclic scans unless rectangles are preserved

C-137: the O(N)-state cyclic procedure that compares w_i,z_i and merges both equal outcomes is a joint-input transducer, not a rect-DAG, because (A0 x B0) union (A1 x B1) is generally nonrectangular. If the fixed-order scan preserves its prefix history, every k-bit prefix occurs on low rows and has high completions, forcing 2^k distinct continuation rectangles for k=Theta(s1/n). Try a genuinely adaptive rectangle-preserving compression, or prove the contexts cannot merge. Do not transfer generic pair-machine cycles to rho without a closure-game simulation. See O-117.

## Q98 - Use the high-table count to sharpen, then retire, output-label fooling

C-138: for r=A s2, binom(N,r)>N|SIZE(s2)| when A is large enough. A random partition into r-blocks therefore has a choice where every block indicator is high. Against the zero low row this yields N/r=Omega(N/s2) pairs with disjoint valid output labels, improving C-129's direct floor by Theta(n). But C-136 caps label-conflict families at O(N/s1), and both bounds are sublinear in N. Treat this as a sharper baseline, then move to rectangle routing rather than spending effort on another output-disjoint-label variant. See O-118.


## Q99 - Share activation-rank routers without losing rectangle structure

C-139 proves the exact Q-to-search interface: q activation rectangles form a ranked cyclic rectangle game, and every fixed-pair path terminates because first-activation rank strictly decreases. A direct acyclic simulation layers states as (i,r) and then routes among q+2N supports, costing O(q^2(q+N)) vertices; the better known compiler is O(q^3/log q). Try to share the support-selection trees across r or bypass explicit rank layering. Every proposed merge must preserve a product rectangle and pass C-132's all-row filtered child, C-135's easy low-variation states, and C-137's equal-prefix cross-pairs. A lower bound on a generic cyclic game transfers to rho only if the C-74 containment/seed syntax is retained.

**Model hygiene.** S_DAG<=S_tree for vertex-count measures, so the intended possible gap is low communication bits/depth versus large graph size, or a tree larger than a shared DAG. Do not formulate the impossible claim small tree size but larger DAG size. Unique-output toy relations show that O(log M) bits can require M leaves, but C-136's dense mismatch outputs rule out that direct leaf mechanism for Gap-MCSP.


## Q100 - Separate witness-path duplication from separator hardness

C-140: the two-state cycle x1=(s1 OR x2) AND c, x2=(s2 OR x1) AND c reverses activation order across inputs, but its least-fixed-point output is simply c AND (s1 OR s2). The rank-layered witness path needs context that the minimum acyclic output circuit discards. First test whether such a recurrence is realizable by legal fusion endpoints; regardless, any proposed lower bound must target all separators rather than the specific Q path. Then seek an actual-promise cross-pair obstruction that survives alternative outputs. No Gap-MCSP bound follows from the toy.


## Q101 - Embed rank-reversing SCCs into a successful promise separator

C-141 realizes the C-140 cycle with legal endpoints on a Boolean cube, but both carriers are nonempty and the output has a tiny acyclic formula. Determine whether a similar SCC can sit upstream of an empty-carrier rule in a successful promise cover while keeping the terminal separator hard. The endpoint constraints matter: empty-rule sides are disjoint, so overlapping carrier states cannot both feed them directly. Any construction must give a rigorous cover and a lower bound against all alternative separator computations, not just rank unrolling.


## Q102 - Find a hard promise where the successful closure cycle cannot simplify away

C-142 closes the toy embedding question: a successful three-pair cover can contain a rank-reversing 1<->2 SCC and still have a two-gate separator. The remaining challenge is to realize many incompatible activation orders on the OPS low/high promise and prove every separator must preserve enough contexts. Any lower bound restricted to the selected Q-witness path is insufficient; the toy shows an alternate circuit can ignore that path. Test candidate gadgets against C-132/C-135 and preserve the full quantitative route to rho_prom.

**Q101 status:** resolved at the finite toy level by C-142; no Gap-MCSP consequence.


## Q103 - Find the actual-promise obstruction beyond rank-layer profiles

C-143 scales the legal successful toy to a q-state SCC with all q activation rotations: the explicit rank-layer architecture has Theta(q^2) rectangles, while a different O(q)-gate separator is immediate. Therefore neither cycle size, rank-profile diversity, nor the size of one Q-witness DAG is enough. For Gap-MCSP, seek a property of Y=SIZE(s1), Z=SIZE(s2)^c that forces every separator (including one unrelated to Q's supports) to preserve many residual contexts. Stress-test against C-132/C-135 and preserve the q-to-rho transfer scale. No such property is known yet.

## Q104 - Normalize the cyclic-rank target against alternative covers

C-144 proves the C-143 q-cycle list is deletion-minimal but the promise admits a one-pair cover, E*={z_i}, H*={r}; hence rho_prom=1. The q^2 rank-layer count is only a cost of the selected witness proof, not of an optimal cover. Next test whether one can construct a finite promise where (i) every successful pair list needs q states, (ii) an optimal list has a large SCC with many activation orders, and (iii) every alternative endpoint system still has a separator/cover lower bound matching q. Do not use rank-layer diversity as a lower bound before this optimality issue is addressed. A toy only diagnoses the proof route; the actual objective remains OPS-specific shared-state non-shareability.

## Q105 - Find a global potential for broad bootstrap states

C-145 proves that every low anchor's first active rule has a carrier containing at least 2^(N-2)-M2 high tables, and all those high tables activate the same rule. The finite C-143 cycle fails precisely because its seed cylinder is empty on U. The missing work is downstream: quantify how a Q routes a low w from its broad seed state to an empty-carrier rule while all coactive high tables avoid the empty output. Seek a potential on high-side activation sets/carrier intersections that can be charged across shared states without summing overlapping exclusions (C-130) or assuming every path preserves width (C-132). No superlinear lower bound follows yet.

## Q106 - Turn seed-cylinder cofactor drops into non-shareability

C-146: a first-round seed state becomes constant on its matching one/two-bit cylinder, so the restricted recurrence loses one state. The obvious sum-over-cylinders argument is killed by the exact-one promise: binom(r,2) cofactors each have Omega(r) cover complexity, but a single O(r) global circuit serves all of them. Now isolate what SIZE(s1) contributes that exact-one lacks. A candidate direct-sum theorem must charge reused gates across different fixed-bit cofactors, with the actual high completion counts and promise separator semantics preserved. Do not claim rho(C) <= q-1 without a containment-preserving realization proof.

## Q107 - Shared-DAG continuation at C-147

The current user steering makes the C-75 shared-DAG branch primary again. C-78--C-123 already formalize the search relations, literature models, transfer inequalities, and description-invariance; C-137 kills only the fixed-order equality scanner. Fresh primary-source audit confirms that standard Boolean games have an acyclic out-degree-two graph with free local predicates, while the native fusion measure is cyclic intersection complexity.

Do not spend another round on the syntax-only descriptor shortcut or rank-layer counting. The concrete next options are: (a) find an N^(1+o(1)) universal mismatch rect-DAG for the full circuit class, which would give rho_prom near-linear; or (b) prove a residual-rectangle non-shareability theorem at a scale that beats the cubic/log q-to-DAG loss, while controlling column filtering and cross-pairs. Direct lower bounds on cyclic q avoid the loss. O-120 is dormant during this phase. See C-147/O-121.

## Q108 - Local PRGs test the tree side, not shared-DAG reuse

The promise adaptation of the CLKM local-PRG method is valid for fixed beta>1/3, where it yields a De Morgan formula lower bound N^(3 beta-o(1)) even with arbitrary medium-band labels. The source lemma assumes formula size t>=N; for beta<=1/3 its locality at that floor is not at most s1, so this argument gives no bound in the small-beta magnification range. In all parameter ranges formula size does not lower-bound rect-DAG size because sharing changes the measure. Retire this as a direct shared-DAG route; continue only with a share-sensitive PRG theorem or a proved q-to-formula transfer. See C-148/C-149/O-121.

## Q109 - Canonical first-missing carrier scan and its residual state

C-150 selects, for each low/high pair, the earliest activated rule whose carrier omits the high table; its missed endpoint must be literal-seeded, so it directly yields a mismatch coordinate. Try to compile this scan with shared states. At round t the continuation depends on P_t(w)=intersection of the first t active carriers, which varies by row. C-142 is a legal toy where merging first-round continuation rectangles adds cross-pairs that skip the direct witness, but an alternate one-pair cover bypasses the obstruction. Either prove an OPS-specific factorization for residuals, obtain a state lower bound that covers every separator, or find a different separator that bypasses the residual signature. Do not count states of this canonical scan as a lower bound on arbitrary S_rect; preserve C-143/144's alternate-separator warning. See O-122/O-121.

## Q110 - Selector hardness must survive witness projection

C-151: the relation A_S=[k]\\S, B_T=T union {k} has unique answer min(A_S intersect B_T) with at least 2^(k-1) k-labelled rect-DAG leaves, hence deterministic communication Theta(k) and rect-DAG/protocol-tree size 2^(Theta(k)). Projecting outputs to â€œany common elementâ€ makes the same input relation one-leaf easy because k is always common. This is a calibration for C-150: a difficult first-missing carrier selector does not lower-bound signed mismatch, which accepts any differing coordinate. A transfer needs every valid-output leaf to be selector-homogeneous, or an explicit decoder/reduction. No OPS consequence.

## Q111 - Test C-150 leaf homogeneity against every separator

C-152 gives an exact sufficient criterion: if the canonical selector h is constant on each leaf rectangle of a mismatch DAG, relabeling leaves yields an h-DAG with no size increase. An output-label decoder is a stronger, DAG-independent sufficient condition. Gap-MCSP mismatch outputs omit the first-excluded carrier, so the criterion is unpaid. Try to prove that all valid mismatch leaves refine selector fibers on a carefully chosen OPS restriction, or retire this transfer route. A failure of the criterion alone does not show a small DAG or a lower bound.

## Q112 - C-153 kills generic leaf-homogeneity transfer

On the C-142 finite promise, both lows have c=1 and p1,p2 both have c=0, so their 2x2 product is a valid c-mismatch rectangle. The C-150 selector matrix there is [[2,1],[2,1]]: p1 selects state 2 and p2 state 1. A full valid rect-DAG can use that mixed leaf and enumerate the remaining columns. Therefore canonical-state charging does not follow from successful fusion or from rectangle semantics alone. Continue only if the OPS promise has a concrete selector-preserving restriction; otherwise prioritize a different O-121 invariant that addresses all mismatch leaves.

## Q113 - Try colourful-sunflower lifting through an output-preserving restriction

The CCC 2025 theorem gives a large rect-DAG lower bound for Index-lifted CSP search. Try partywise maps from its lifted inputs into actual low/high truth tables. The decisive requirement is that each mismatch output leaf decode to a constraint falsified on every source pair in its pulled-back rectangle; arbitrary table disagreement does not certify this. Record any output-decoder/refinement overhead and enforce the OPS table-size/circuit-complexity bounds. Need L/r>N^(3+3epsilon)/log N through the current compiler, or a direct cyclic-cover transfer. C-154 records exact theorem and current gap.

## Q114 - Retract the partial-Index mismatch no-go

C-155 was wrong: it imposed agreement on pairs y_x=0 that are outside SearchORâˆ˜Index's legal domain. The legal-domain code a(x)=0^m, b(y)=y works and decodes every mismatch to the sole valid output. This is a useful domain-discipline correction. For the total unsat-CSP relations in C-154, continue only with statements that hold on every source pair.

## Q115 - Analyze paired cut covers for total CSP search

C-156: a fixed-label bitwise mismatch code is exactly a family of cuts on Alice's and Bob's inputs whose two cross-rectangles are both monochromatic-valid and whose union covers all pairs. A standard rectangle cover does not suffice because each code coordinate creates two opposite orientations. Prove a lower bound on this paired cut-cover number for a wide Index-lifted unsat CSP, or construct one with quantitative size; then compare it to the lifting theorem and the OPS compiler threshold. This narrows the direct embedding search without claiming a general reduction barrier.

## Q116 - Require progress in every cyclic communication model

C-157's O(N)-state root-loop has a finite valid route for every mismatch pair but also an infinite route for every pair. Any existential-path definition for cyclic search collapses to listing all output labels. The useful analogue of C-74 must enforce a well-founded progress measure on actual transitions and preserve product rectangles. Try to characterize the weakest such condition that still admits q activation states and can be compared with standard DAG size; do not count a cyclic graph's vertices without accounting for termination semantics.

## Q117 - Globalize the full-side-child lemma

C-158: a binary cover of one rectangle by two rectangles always has a child retaining the complete row side or the complete column side. This produces a one-party local routing strategy at each Boolean-game node, but it does not prevent histories from merging at later vertices. Combine the forced full-side step with C-129's row-signature/high-column exclusion inequality to derive a global state charge. Stress-test against C-130 overlap and C-132's all-row filtered child; keep the OPS-specific and every-separator requirements explicit. No lower bound follows yet.

## Q118 - Look for a global reuse charge beyond Sokolov's local gate trichotomy

C-159: C-158 is already part of Sokolov's Boolean-game/circuit correspondence. A binary node is AND, OR, or copy, but this local classification has no size lower-bound force. Investigate whether the C-129 row-signature/high-column inequality can be amortized across AND/OR/copy nodes while handling DAG merging, overlapping exclusions (C-130), and the all-row filtered child (C-132). Retire any argument that counts gate types or local projections without a global potential. The target remains an OPS-specific lower bound for every separator or a near-linear universal DAG.

## Q119 - Find the feature that separates MCSP from easy threshold promises

A symmetric two-tail Hamming promise matches the low/non-high counts, large-cylinder high completions, local low-row restriction richness, Hamming separation, coarse patch stability, complement symmetry, and closure under arbitrary coordinatewise Boolean recombinations of O(n) low rows into the non-high band, yet has an (O(N\log N)) separator. Use C-160 as a mandatory stress test for any C-129/trichotomy charge. A viable invariant must detect finer structure of the actual SIZE(s1)/SIZE(s2) classes and apply to every separator, not just Q's chosen states. C-123 already rules out syntax-only description-space compression. No such distinguishing invariant is currently known.

## Q120 - Test basis-composition closure as a state-reuse obstruction

C-161 adds the full affine family and its Hamming patch neighborhoods to an easy calibration; Walsh-Hadamard decoding keeps the separator at N^(1+o(1)). Thus balance, affine symmetry, and one large orbit do not suffice. The actual low class contains n input-literal truth tables forming a separating basis. There are |GL(n,2)|=2^(n^2+O(1)) ordered linear bases, each implemented with O(n^2) gates; composing any such basis with a Boolean circuit g computes g(Ax) with O(n^2) overhead. High tables exclude all these compositions when g fits within the s2 budget. Investigate whether these overlapping basis-induced partitions force distinct residual rectangles in every mismatch DAG. First test the claim against C-122's O(N) router for any family of at most eta*n low rows (for sufficiently small eta), and against descriptor invariance C-123. A proof must exploit interactions beyond these small anchor sets and beyond short descriptions. No lower bound currently follows.
## Q121 - Charge nonlinear composition interactions, not basis descriptions

C-162 rules out treating the 2^(nÂ²+O(1)) ordered linear bases or their affine component rows as distinct hard anchors: the actual affine row family has a Walsh near-linear separator against Z, and descriptions lift/restrict without changing standard rect-DAG size. Each basis composition g(Ax) is just a low circuit when its O(nÂ²) overhead fits. Investigate only whether residual rectangles for many nonlinear g-composition families force incompatibility under product-hull merging. Any claim must apply to arbitrary separators, survive C-122/C-130/C-132 and C-160/C-161, and clear the explicit DAG-to-rho transfer threshold. No lower bound currently follows.

Promise guardrail: size-\(s_2\) compositions outside \(Y\) are medium rows, absent from \(Y\times Z\); their labels are unconstrained. Prioritize low-budget compositions unless a rigorous medium-extension lemma is found.

## Q122 - Apply the mismatch decoder-capacity test before CSP embeddings

C-163: let chi_out*(R) be the fractional cover number of a total source search relation by its valid-output sets. The OPS Hamming gap forces every encoded source pair to mismatch in Delta=Theta(N^beta/n) positions. If each of the 2N signed mismatch types has at most r output-labelled decoder terminals, then chi_out*(R) <= 2Nr/Delta=O(r n N^(1-beta)). Compute or lower-bound this parameter for the C-154 lifted CSP source. If it exceeds this threshold, the proposed decoder overhead is impossible; if not, C-156's paired-cut validity must still be proved. This is a reduction filter, not a target lower bound. Check whether the actual source's many-answer relation has low enough fractional output cover to survive.

**Source check.** The CCC cPHP lifting relation has pigeon-pair outputs, so its fractional output-cover number is at most binom(k,2). Under polynomial k versus truth-table arity n, this is much smaller than the OPS capacity O(nN^(1-beta)); C-163 does not eliminate this candidate. Continue by analyzing the actual paired-cut sets for Ind_m^k and by constructing the table maps. Keep the CCC theorem as a lead, not as an OPS lower bound.

## Q123 - Compare cPHP/Index hardness with the necessary decoder cost

C-164 derives r>=Delta m^2 d/(2N) for any OPS table-mismatch encoding of the Index-lifted cPHP source, because each fixed-answer rectangle has uniform mass at most 1/(m^2 d). Compare
(m/(A d w log(mk)))^w / r
against N^(3+3epsilon)/log N, using an explicit table-length N and decoder construction. The output-cover filter C-163 is too coarse here: cPHP's outputs are only pigeon pairs, so chi_out*<=binom(k,2). This route remains viable if the lifted lower bound dominates the decoder cost, but the partywise SIZE(s1)/SIZE(s2)^c table maps and every mismatch-leaf decoder still need to be constructed. Do not infer an OPS lower bound before those maps exist.

**Parameter-direction warning.** C-164 proves a minimum decoder size r_min, not a usable upper bound. For the existing lifted lower bound L0, the OPS threshold T is reachable by this transfer only if L0>T r_min; even then, construct the map and prove r<=L0/T. If the inequality fails, the currently cited lifting guarantee is insufficient at that schedule.

## Q124 - Build or rule out a bounded signed decoder for lifted cPHP

C-165 proves that the CCC paper's one-sided cPHP/Index-to-mKW output map does not handle both signs of C-75 mismatch: any decoder for the full signed relation needs at least d/2 output-labelled leaves per mismatch type. C-164 adds r>=Delta*m^2*d/(2N). Try to construct a refinement meeting both costs and then compare it with the lifted DAG lower bound and OPS threshold; alternatively, prove a stronger lower bound on a selected mismatch rectangle that makes the refinement consume the lifting gain. The fixed-decoder route is closed for d>=3. Do not state that all cPHP transfers are impossible.

## Q125 - Interval restriction contexts versus arbitrary state sharing

C-166 rechecks C-78/C-133 and specializes C-110 to the universal interval scanner. C-167 then uses C-160 to refute a generic polynomial-loss normalization: a two-tail threshold promise has an O(N log N) arbitrary rect-DAG but 2^(Theta(N^beta/n)) pairwise nonmergeable contexts in an interval-local scanner. Do not pursue promise-independent interval normalization. The remaining version must identify a property specific to SIZE(s1) versus SIZE(s2)^c and prove a controlled conversion; otherwise shift to arbitrary rectangle-state merging without interval labels. Circuit descriptions alone do not specify a joint rectangle. Keep O(q^3/log q) cover-to-DAG loss explicit. C-167 is a route-pruning calibration, not an OPS bound. See bridge Â§Â§92-93/O-127.
## Q126 - Force genuine two-party adaptivity in any compact mismatch DAG

C-168 closes the row-only nonadaptive sample route: for each w in Y, any coordinate set S(w) guaranteed to contain a mismatch with every z in Z must have size at least N-log2|SIZE(s2)|=N-o(N), even if S is chosen from a circuit description. Try to construct a compact DAG whose Bob-dependent rectangle transitions exploit the high table to select a smaller relevant region, or prove that state sharing cannot implement that adaptation with o(N^(3+3epsilon)/log N) nodes. Keep this separate from interval-local routers, whose generic normalization is refuted by C-167, and from the ranked cyclic q-state model. No DAG or rho_prom lower bound follows from C-168.

## Q127 - Charge repeated alternation after eliminating one-switch DAGs

C-170 shows that an Alice-first one-switch DAG needs 2^Theta(s1) frontier states, using the C-80 block code and the C-81 diameter bound; a Bob-first one-switch DAG needs 2^Omega(s1/n) states, using low-table pattern realization and cylinder counting. The description-first universal circuit is therefore not a compact rect-DAG, and neither party can send a single synopsis after which the other finishes. Attack the genuinely alternating case: define a rectangle-state potential that combines row packing, low-pattern realization, and high-column exclusion, then charge each switch despite state merging. A prescribed scan architecture does not count. Alternatively try to build a small multi-round DAG as a falsification. The quantitative O-128 target and the q-to-DAG loss stay unchanged.

**Mandatory countercheck for Q127.** The C-80 block-constant subpromise defeats any attempt to add the two one-switch state lower bounds: its B-to-A-to-B router is O(N). Therefore the needed potential must charge *row-dependent* fiber changes, not merely force two or more owner switches. C-121 rules out a single common partition for all Y, but gives no lower bound for a DAG that selects partitions adaptively.

## Q128 - Salvage or retire the fiber-witness lower bound

C-171 proves S_rect(Fib)>=Omega(N^(2-beta)/n) by affine-flat component counting, but Fib is a stronger output relation than C-75 mismatch. Fib-to-Mis is O(1); Mis-to-Fib needs O(N^2) state copies to retain prior output coordinates, so the lower bound gives no useful Mis bound. Attempt a direct simulation that avoids storing the pair, or recast the affine-flat component obstruction on ordinary mismatch rectangles. If neither works, keep C-171 only as a fixed-pair-menu no-go and return to O-129's alternating-state charge. Exact scope and proof are in bridge Â§97.

## Q129 - Global cylinder budget and the missing alternation charge
C-172 replaces C-129's r separate M2 allowances by one global allowance: for a state with r realized row signatures on K, at least r*2^(N-|K|)-M2 high columns are excluded. At the root this gives |pi_K(Y)|2^(N-|K|)<=M2, and point-indicator realizability adds Theta(s1/n) coordinates to the N-log M2 floor. This is a sharper state constraint, but its excluded-column sets may overlap heavily across nodes. Do not sum them without a disjointness/charging proof. Also, C-135 patching means a fixed N-Theta(s1) candidate set already hits every pair; the difficulty is rectangle-valid routing, not output support. Try an overlap-aware potential against C-80's adaptive router and C-160's threshold separator, or retire the profile as a local bound and return to O-129.

## Q130 - Retired direct Rect-DL lower-bound transfer
C-173 tests the 2025 rectangle-decision-list connection. A rect-DAG leaf cover gives a multi-output rectangle list with <=S terms, but the trivial 2N signed mismatch rectangles already solve Mis as such a list. Thus list length is too weak for a superlinear lower bound. Compiling ordered rectangle queries back to a distributed protocol requires retaining Alice/Bob failure context because (A^c x Y) union (A x B^c) is nonrectangular. Rect-DL output alternation is not player alternation. Reopen only if a hard Boolean output projection is forced across every valid mismatch choice or a new context-sensitive list measure is shown to transfer.

## Q131 - Replace raw cylinder exclusions by path-conditioned charge
C-175 gives exact owner-sensitive conflict-set inclusions, but C-80 supplies an O(N)-state counterexample to summing |Z\\B_v|: with m=Theta(s1/n) block states, each excludes almost all high columns, and the overlap is Omega(m). Seek a potential conditioned on the actual parent rectangle or on path reach probability, so an off-path block does not charge the same z repeatedly. It must still rule out a near-linear router for the full SIZE(s1) promise and survive C-160's threshold separator. If no controlled charging law exists, retain C-175 as a route-pruning theorem and attack a different state invariant.

### Q132 - Residual-context distinguishability under DAG merges
Replace absolute conflict volume with the residual contract at a state: its feasible product rectangle A_v x B_v, descendant routing suffix, output support K_v, and the incoming history rectangles that merge there. A necessary support condition is that K_v hit every coordinate-difference set in the merged product hull, equivalently pi_K(A_v) and pi_K(B_v) are disjoint. This is not sufficient for a legal shared suffix: the DAG must actually route each pair to one of its valid labels. Seek a large family of histories for the actual low/high promise such that no small acyclic graph can merge them with one correct suffix, even when K_v may include previously queried coordinates. Stress tests: C-80's O(N) block router, C-110's product-hull condition, and C-160's O(N log N) threshold separator. This is only a target formulation; no lower bound is currently proved.

### Q133 - Local PRG for separator circuits at magnification locality
For any total Gap-MCSP separator H, uniform acceptance is at most M2/2^N and every generator output in SIZE(s1) is accepted, so a PRG with such low-locality outputs that fools H would refute H. Find a generator that fools all size-S unrestricted separator circuits with output locality <=s1 for S>N^(1+epsilon), or prove why the construction is equivalent to the desired circuit lower bound. The known CLKM PRG for standard branching programs has lambda=S^(1/2)2^(O(sqrt(log S))); it yields only N^(2beta-o(1)) for small beta and does not transfer to rect-DAGs. This is a narrowly stated target, not progress toward the required bound yet.


### Q134 - Lower-bound sparse-envelope complexity under residual merges
By C-178, every C-75 separator is a circuit H with SIZE(s1) subseteq H^{-1}(1) subseteq SIZE(s2); this is the exact circuit form of the rect-DAG target. A universal circuit evaluates a proposed description, but short descriptions do not eliminate the existential quantifier over descriptions. The direct OR costs N*2^(O(N^beta)); the one-switch protocol has an exponential frontier. For Q132, define a candidate merge's full product hull A_* x B_* and seek an explicit lower bound on the smallest separator circuit for it. A positive lower bound must hold for many hulls with a shared suffix budget t, survive C-80 and C-160, and quantify how the lower bounds force >N^(3+3epsilon)/log N rect-DAG nodes (or improve the q compiler). At the root this becomes the original sparse-envelope problem, so prioritize proper sub-hulls with a new tractable invariant. This is an exact target, not a proved lower bound.



### Q135 - Go beyond one-shot affine fingerprints
C-179 proves that for each fixed low row w, any affine map L_w(x)=A_w x+b_w that must differ from L_w(w) on every high table has rank at least N-log2(M2)=N-o(N). Thus coordinate samples and parity sketches cannot give a short one-shot detector. Test whether an adaptive sequence of linear tests can reuse states after equal answers, or whether a nonlinear synopsis can exploit the actual SIZE(s1) versus SIZE(s2)^c structure. Any construction must still output a mismatch coordinate; any lower bound must apply to arbitrary alternating rect-DAGs and survive C-80/C-160. The result is currently only a route filter.



### Q136 - Can adaptive parity tests share states?
C-180 forces depth N-log2(M2) for any one-input parity decision tree separator, even when each parity query depends on earlier answers. A DAG can still have this depth with only O(N) vertices, so the tree theorem does not approach the shared-DAG target. Analyze whether merges of distinct affine path-cosets in a parity branching program require many states, then test whether any resulting invariant transfers to arbitrary rect-DAGs. Do not confuse parity decision trees with the two-party mismatch protocol; a useful transfer must preserve the output-coordinate relation and the N^(3+3epsilon)/log N threshold.



**Q135 disposition.** C-180 resolves the adaptive parity decision-tree subcase with a near-N depth lower bound. Keep Q136 for the genuinely open question: whether sharing affine path contexts in a branching DAG costs more than O(N) states. This restricted result does not affect the arbitrary rect-DAG target.



**C-181 disposition for Q133.** Existing local PRGs against branching programs have better nondeterministic variants, but their promise-gap consequence is S>=N^(3beta/2-o(1)), still sublinear for every sufficiently small beta; their model also excludes arbitrary separator circuits. Q133 should remain focused on a locality curve for unrestricted separator circuits, not on further BP-only exponents unless a reduction to C-75 is proved.

### Q137 - Route the mixed output fiber

The output wire alone partitions coordinates into F_0 and F_1 according to w(x). If z were constant on both fibers, a one-bit lookup composed with the low circuit would compute z below s2. Taking majority z on each fiber gives a low h; point-minterm patching forces dist(z,h)=Omega(s2/n). Thus one of just two fibers is mixed and contains Omega(s2/n) mismatches. This improves the local witness from C-115's larger gate signature, but it remains pair-dependent through z.

The mixed fiber now has a fixed label b, but its membership still depends on the low row through w_i=b. In a fully merged, unfiltered one-state-per-stage scan, the two continuations (not in this fiber; in this fiber and matching z) have product hull Y x Z. At stage i with 2^(i-1)>M2, a high extension can be set opposite at i and equal to w at every later scan position, so a suffix that only checks later positions fails. This proves a no-go for that scanner architecture. A router that keeps filtered contexts or revisits coordinates is not covered. Prove a merge lower bound that survives those options, or construct a routing DAG that avoids context growth. Stress-test against C-80's O(N) block router and C-160's threshold separator. The arbitrary alternating-DAG target and O(q^3/log q) compiler are unchanged.

## Idea 320 - A dense witness fiber is not a locally selectable state

C-183 gives a promise-valid 2x2 XOR submatrix for the predicate that the high table is mixed on the low row's zero-output fiber. Choose low rows whose zero sets are {p1,p2} and {p1,p3}; high completions with restrictions 001 and 010 exist because 2^(N-3)>|SIZE(s2)|. The mixed-fiber predicate is [[0,1],[1,0]], so its two valid pairs cannot merge into one product rectangle.

Learning: C-182's dense-fiber lemma is only a pairwise existence statement. The identity of the useful fiber depends jointly on both inputs, so â€œBob picks the fiber, then scanâ€ has a genuine rectangle-state gap. This only kills a single-rectangle selector. It does not bound the number of rectangles needed or arbitrary DAG size. Next seek a bounded-state alternating selector or a quantitative residual-rectangle lower bound, with C-80 and C-160 as counterchecks.

## Idea 321 - Track residual circuit complexity, not only mismatch mass

C-184 defines e_b(w,z) as the minimum circuit size of any total extension agreeing with z on the low circuit's output fiber F_b. A one-bit mux gives CC(z)<=CC(w)+e_0+e_1+O(1), so one fiber retains nearly half the high table's circuit complexity. Patching a constant on that cell also shows it contains Omega(s2/n) mismatches. For a k-bit signature partition, the sum of all cell extension complexities is at least CC(z)-cost(signature)-O(k2^k).

Learning: C-182's dense mismatch fiber can be strengthened to a hard residual trace. This still does not solve the shared-DAG problem: the identity of the hard cell is joint, and the simple mixed-cell selector already has the XOR obstruction C-183. Next test whether extension complexity is subadditive or monotone under product-hull merges in a way that yields a DAG potential; if not, retire it as another existence-only invariant.

## Idea 322 - Residual hardness needs cross-pair variation

C-185 tests C-184 against the known common-partition router C-121. Every pair still has an output fiber whose z-trace has extension complexity Omega(s2), yet a fixed partition respected by the whole structured low family gives an O(N)-node mismatch DAG. So per-pair residual hardness is not a state lower bound.

Learning: the scarce resource is not merely a hard restriction of z; it is the inability to name a useful residual cell uniformly across many rows and columns while keeping every merged product hull valid. The next invariant must measure diversity/addressability across a DAG state and must fail to charge the C-80/C-121 router.
## Idea 323 - Sparse rows quantify the cost of unfiltered partition menus

C-186 counts how many r-point-indicator low tables can be constant on one m-cell partition: at most sum_{i<=r} binom(m,i). Covering all such low rows by partitions of m=O(s2)=o(N) cells takes at least (N/(e m))^r contexts when m>=r, with a similar bound for m<r. Thus the full-column C-121 router cannot be generalized by a small static menu of common partitions.

Learning: this strengthens the fact that one common partition cannot respect all low circuits, but it still does not charge a general rect-DAG. A DAG may shrink Bob's column set before row contexts merge, or share suffixes across partitions. The next proof target is the cost of that filtering under product-hull safety; compare C-133 and C-160 before treating the context count as a state lower bound.

## Idea 324 - Hamming-ball filters expose the center-sharing bottleneck

C-187: for a fixed center u, every safe-radius Hamming ball around u has an O(N)-size threshold separator against all high tables. In particular, the sparse point-indicator rows of C-186 lie in one safe ball around zero, so a linear DAG handles them even though a small menu of their common-partition routers is impossible.

Learning: the cost is not filtering one local cluster; it is representing which center or other local geometry applies across far-apart low rows. A static menu of safe balls is exponentially large on C-80's separated code family for beta<1/2, but this does not rule out an alternating DAG that constructs row-dependent structure. Any new invariant must charge that global sharing and still give only O(N) on C-80/C-121 and C-160.

## Idea 325 - Treat global center selection as approximate learning, but respect direction

C-188 expresses the union of safe Hamming balls around SIZE(s1) as an existential projection over a low circuit description and an error set. A learner that lists t-size hypotheses for every size-s1 function within error epsilon/2 yields, by Oliveira et al.'s ITCS 2020 Lemma 34, an approximate-MCSP separator of size O(N poly(t/epsilon)). With t=s1 and epsilon=Theta(N^(beta-1)/n), every project-high table is a NO instance by point-patching, and t/epsilon=Theta(N).

The critical warning is implication direction: the published lemma gives learner -> separator and separator hardness -> learning hardness. It does not give learner lower bound -> separator lower bound. Its converse-style results use additional NP-completeness/reduction assumptions. Thus a query-count lower bound is not yet a C-75 DAG lower bound. The remaining possible use is an explicit learner construction that yields a compact separator, or a new reverse transfer valid for the actual Gap-MCSP promise.

## Idea 326 - Separate column certification from shared mismatch routing

For a fixed high table z, define h_Y(z) as the least number of coordinates Q such that every low row differs from z somewhere on Q. Low point-minterm circuits shatter every fixed set of k=Theta(s1/n) coordinates, so h_Y(z)>k for every z. This differs sharply from C-168: a low-row-selected set that must catch every high table needs N-o(N) coordinates.

Learning: Bob may have a much shorter local certificate than Alice's row-only candidate set. But a certificate is not a router. Scanning Q while continuing on agreement merges diagonal prefix rectangles, and the lower bound k=Theta(N^beta/n^2) is far below the required state bound. If max_z h_Y(z)<=k, Bob can send the sorted Q(z), Alice returns w restricted to Q(z), and Bob outputs a mismatch, for O(k log N) communication bits and at most 2^{O(k log N)} protocol-tree nodes. This is not a better DAG bound. Next investigate the cost of addressing and searching Q(z) under product-hull-safe sharing; do not count certificate coordinates as DAG states.



## Idea 327 - Peel off high columns with a common short certificate

For k=ceil(log2|Y|)+1 and any fixed Q of k coordinates, the low class realizes at most |Y| patterns on Q. Every other pattern certifies that all low rows differ from any table carrying it. Since k=O(N^beta) and each cylinder has 2^(N-k) completions, almost all completions are high; the certified high set has size at least (1/2-o(1))*2^N.

Learning: there is a single sublinear support set that handles a constant fraction of high columns, even though the full relation still has the hard trace-matched branch. This does not imply a near-linear DAG: finding a mismatch inside Q remains a search problem, and naming the up to |Y| matched patterns costs 2^{O(N^beta)} contexts. Next test whether the trace-matched residual can be recursively compressed under product-hull safety; keep C-80 and C-160 as counterchecks.

### Q138 - Compress the trace-matched residual after C-190

Fix Q with k=ceil(log2|Y|)+1 coordinates. C-190 partitions high columns into a large branch whose Q-pattern is not realized by any low row (every pair there has a mismatch in Q) and a trace-matched residual with at most |Y| possible Q-patterns. The first branch still needs a rectangle-valid mismatch search on Q; the residual may require exponentially many pattern contexts if handled by explicit enumeration.

Try to construct a recursive shared suffix for the matched branch or prove that distinct trace patterns cannot merge under the output support available to a common suffix. Keep all outputs valid for every cross-pair in the product hull. Any standard rect-DAG lower bound must exceed N^(3+3epsilon)/log N under the current q-to-DAG compiler; the construction must beat the M1=2^{O(N^beta)} explicit menu. Stress-test against C-80/C-121 and C-160.

## Idea 328 - Trace equality is highly non-shareable only if Q is discarded

For C-190's fixed Q, the exact matched-pair set E_Q has r_Q=|Y|Q| signature blocks. Each block has a high completion, while a product rectangle contained in E_Q can cover only one block. Point-indicator traces imply r_Q>=binom(k,t); because k/t=Omega(n), this is N^{omega(1)}.

Learning: the clean recursion “compare Q, then forget it and solve the remaining coordinates” cannot merge all matched signatures into a tail-only rectangle state. But this is not an arbitrary Mis lower bound: a general suffix can use Q-output leaves for cross-signature pairs, and a promise rectangle may intersect E_Q in a diagonal union. Next charge the tradeoff between those exits and signature-specific residuals; do not transfer the E_Q rectangle-cover number directly.
## Idea 329 - Recast mismatch as monotone KW; separate rectangle and equality states

C-192 gives an exact dual-rail encoding rho(u)_(i,b)=1[u_i=b]. With the high table as the monotone-KW 0-input and the low table as the 1-input, every KW output is exactly a valid signed mismatch. Thus C-75 is a partial monotone KW relation, with no protocol-size loss under the encoding. The Q-matched relation E_Q is one equality-feasible state q(w)=r(z)=code(w|Q), while C-191 says any rectangle cover constrained to lie inside E_Q needs r_Q=N^(omega(1)) rectangles.

Learning: the state geometry explains the C-191 boundary. Equality-feasible states can carry many diagonal trace blocks in one node; standard rect-DAG states must be products. Every rectangle is a special case of both degree-two equality and inequality feasibility, so lower bounds in those stronger models transfer to the target DAG. Known monotone-real/inequality lower bounds are function-specific and do not automatically transfer to Gap-MCSP. The route is now to test an OPS-specific lower bound or compact protocol in the stronger model, while keeping O-141's cross-signature exits unresolved.
## Idea 330 - Equality-feasible states trivialize mismatch search in linear size

C-193 gives a degree-two equality protocol with states E_i for equality on the first i coordinates, states D_i for equal prefixes plus a mismatch at i, and two signed-output leaves per i. Every disjoint low/high pair reaches its first differing coordinate. The graph uses at most 4N+1 vertices.

Learning: equality states are too expressive for the desired lower bound. E_i is a diagonal union, not a rectangle; the C-190 matched state E_Q has r_Q=N^(omega(1)) signature blocks and cannot be represented by fewer than r_Q rectangles if those rectangles remain inside it. This does not lower-bound arbitrary rect-DAGs. Retire equality-protocol lower bounds; investigate inequality protocols separately and return to O-141 for the standard model.


## Idea 331 - A universal triangle protocol does not share as rectangles

C-194 constructs an O(N)-vertex degree-two inequality protocol for signed mismatch on every disjoint pair of N-bit table families. Its comparison states encode lexicographic greater-than on an interval; the split is correct because a larger binary word is larger either on the high half or, after a tie, on the low half. This works for C-75 without exploiting short circuit descriptions.

Learning: the shared-state barrier is specifically product structure. A comparison triangle can represent large ordered unions in one state, while a rect-DAG cannot assume such a state is a rectangle. The direct rectangle cover of greater-than may require 2^(k-1) rectangles on k-bit inputs, and generic promises exhibit an exponential rect-DAG versus linear inequality-protocol gap. This retires stronger inequality/equality lower bounds as a route but proves nothing about actual C-75 rect-DAG size or rho_prom. Continue O-141: charge cross-signature mismatch exits against tail-context reuse under product-hull safety, with C-80/C-160 as required counterchecks.

## Idea 332 - Use ordered low prefixes to falsify comparator-state compilation

C-195 uses the actual circuit-size gap. Point-indicator DNFs realize every prefix of length t=Theta(s1/n)=Theta(N^beta/n^2). The corresponding low truth tables occur at regularly spaced integers; each intervening interval is larger than the whole size-s2 class, so each gap contains a high table. The consecutive-gap pairs form a fooling family of size 2^t-1 for C-194's top comparison triangle.

Learning: this is stronger than the generic greater-than cover example because it survives restriction to SIZE(s1) x (complement SIZE(s2)). It rules out direct expansion of the universal inequality protocol into a rect-DAG, but the selected subpromise has an O(N)-vertex alternative: scan for a 1 in the suffix, where every low row is zero and every chosen high column has a nonzero suffix. Do not turn a hard state cover into a relation lower bound. Continue the O-141 task of pricing cross-signature outputs against tail-state reuse, using this ordered-prefix construction as a stress test for any statewise simulation.

## Idea 333 - Separate Q exits from tail conflicts at each shared state

For a rect-DAG state A_v x B_v, split descendant output support into P_v inside Q and T_v outside Q. If low/high signature fibers sigma,tau overlap on T_v, product-hull safety forces sigma and tau to differ on P_v. Each diagonal signature represented on both sides must be separated entirely by T_v. Quantitatively, r diagonal signatures and t=|T_v| force the state to exclude at least max(0,r*2^(N-|Q|-t)-M2) high columns. This proves a local exit-versus-tail tradeoff.

The aggregation attempt stops: C-130 shows excluded high columns can recur across many reachable states, and C-80/C-160 show coarse local constraints can coexist with small DAGs. A state may also expose all Q outputs and leave diagonal pairs to a shared tail subgraph, so signature count is not a state lower bound. Next, seek a path-sensitive charge for these cylinders together with the routing complexity of shared Q exits; retire the attempt if that charge fails either calibration. No global lower bound yet. See C-196/O-141.
**Idea 334 - Communication bits can hide a large shared-DAG requirement.** For any m-bit Boolean function f, Alice can send her KW input x using m bits and Bob finds a differing coordinate, so deterministic communication is O(m). Yet the DAG-like KW theorem identifies rect-DAG size with Boolean circuit size up to constants, and counting gives f with size 2^(Omega(m)). Conversely parity has an O(m)-node KW DAG but an Omega(m^2)-node tree/formula. Keep the measures straight: tree node count is never smaller than DAG size; it is communication bits that can be small while the DAG is huge. These are calibrations, not Gap-MCSP lower bounds. See bridge C-196, tree/DAG paragraph.

### Idea 335 - Lifted-CSP reduction into the actual high-complexity promise (C-198)
Represent C-75 as partial-monotone KW on one-hot dual rails. This matches the rectangle-DAG model in CCC 2025 colourful-sunflower lifting, so an answer-preserving reduction from an Index-lifted CSP search relation would transfer its DAG lower bound with no size loss. The hard part is constructing Bob outputs that are all outside SIZE(s2), while ensuring every truth-table mismatch decodes to a valid CSP witness. Succinct Bob output circuits of size <=s2 are ruled out immediately. Affine-coset embeddings fail because one parity check separates the cosets in O(N) gates. Next step: only pursue a non-affine hard-image encoding with explicit parameters beating N^(3+3epsilon)/log N; otherwise retire this transfer route. No theorem yet.



### Idea 336 - Use dense-domain robustness to filter low Bob columns (C-199)
The 2024 triangle-DAG lifting proof tolerates a dense-column promise: initialize its error-column set with the omitted Bob columns, then use the same Triangle Lemma and error removal. With a constant loss, any omitted density below 1/4 is harmless. The project removes only 2^(-N+o(N)) of all N-bit columns, so a lifted relation can map Bob inputs to raw strings and restrict to high tables. This removes the individual high-image construction requirement. It does not supply an answer-preserving reduction: every table mismatch orientation must be a valid CSP witness, and simple low-image families have O(N)-size range tests. Continue only with a cut-cover-compatible source relation and a low image whose separator is not easy. Quantitative lower bound remains unproved.



### Idea 337 - Do not transfer clique-colouring hardness through its easy image range (C-200)
The CCC 2025 cPHP reduction maps Alice to an isolated k-clique on a selected transversal. Its range is recognized by an O(N logN) degree-check circuit and is disjoint from every c-colourable Bob graph. So the resulting C-75 mismatch promise has a small separator even if Bob inputs are filtered to high tables. Also, reverse edge differences are extra C-75 outputs that the mKW reduction cannot decode. This route is closed. Any replacement needs a low image with no small general Boolean envelope and a decoder valid for both signed orientations.

### Idea 338 - Use the corrected full-exponent lifting bound, but isolate the map bottleneck (C-201)
The ECCC 2024 triangle-DAG theorem has threshold (1/2)m^((1-delta)w). The dense-column restriction still gives Omega(m^((1-delta)w)) with a quarter-size constant and omitted-column density <1/4. Setting mr=N and r=polylog(N), this crosses N^(3+3epsilon)/logN whenever (1-delta)w>3+3epsilon. Thus parameter strength is no longer the limiting issue for this lifting interface. The missing step is an answer-preserving reduction into low/high truth tables: every low image needs size-s1 generation but no easy envelope, and both mismatch orientations must decode to valid source witnesses. The CCC clique-colouring map fails both tests. Continue only with a concrete map or a proved no-go; no target lower bound has been obtained.

### Idea 339 - Screen lifted sources by answer-fiber rectangle mass (C-202)
For an output-refined reduction into C-75, each mismatch type must be partitioned into source-valid product rectangles. The full-clause unique-output Search(F) relation has answer-fiber rectangle mass at most (1/(2m))^v, so its decoder requires Omega(m^(v-1)) leaves per type. This dominates the C-201 lifting lower bound at the tested width. Retire unique-output sources for this transfer. Search for answer-rich sources with both (i) lifting lower bound above the decoder/refinement cost and (ii) an encoding with low individual circuits, hard low-image envelope, and both signs valid. Apply C-164's cPHP bound before building a map.

### Idea 340 - Keep cPHP, but separate decoder feasibility from embedding (C-203)

For constant-degree cPHP on an expander with k left vertices and c=alpha k, the CCC lifting width is W=Omega(k). Setting N=Theta(mk), the source lower bound is about N^W/polylog(N)^W, while C-164's necessary decoder refinement is only Omega(N^(1+beta)/(k^2 logN)) per mismatch type. Thus fixed W>4+3epsilon+beta passes the compiler-times-minimum-decoder exponent screen. This means C-202's unique-output failure should not be generalized to answer-rich CSP search.

The pass gives no decoder upper bound or encoding. C-204 closes the dense-column robustness issue for CCC by using its arbitrary-column Full Range Lemma and charging the omitted high-table columns within the triangle-error budget. Next seek a hard low-image map and a decoder below L/T. The standard clique-colouring image still fails C-200.

### Idea 341 - Use the CCC Full Range Lemma on high-table Bob columns (C-204)

For a lifted relation with base width W, the CCC 2025 Full Range Lemma already allows Bob's current column set to be an arbitrary subset of the full product, provided its density clears epsilon. In its theorem proof epsilon is about 2^(-4W log(mn)); the triangle-error union bound is about 2^(-W log(mn)). Removing the OPS non-high tables costs eta=2^(-N+o(N)), negligible when N=Theta(mn) and W log(mn)=o(N), even after charging all protocol states. Thus the cPHP lift may take Bob's raw flattened table and restrict to high tables. This is a proof adaptation, not a verbatim theorem statement; details are C-204. The source route still lacks a hard low-image map and an all-sign decoder.

### Idea 342 - Rank-layer the fusion router, then price its fan-out (C-210)

Let `tau_i(w)` be the first activation round of rule i. States `(i,r)` with Alice condition `tau_i(w)<=r` and Bob condition `tau_i(z)=infinity` yield an acyclic rank-lift: every rule-support transition decreases r, and literal supports terminate at a mismatch. This is a valid q^2-state *multiway* protocol for a successful cover. It does not produce a q^2 standard DAG because each state has up to q rule supports and N literal supports; the edges/routers are cubic at OPS q>=N/2. The attempt narrows the hope of avoiding unrolling: the original q-state graph is small only with pair-dependent ranking and cyclic semantics. Next use C-209 to identify when support routers for different ranks can safely share; any claim must retain product-hull correctness and C-80/C-160 counterchecks. No lower bound or better compiler resulted.

### Idea 343 - Use a sparse family of mismatch samples (C-211)

Point-minterm patching makes every low/high pair differ on `d=Omega(s2/n)` coordinates. A probabilistic construction yields `R=O(d log(eN/d))` subsets of size `k=ceil(N/d)` whose total incidence count is `O(N logN)` and which hit every d-set. This looks like a compact universal output support. It fails to give a DAG because “this sample contains a mismatch” is a union of rectangles, not a product rectangle; the sample index is a joint property. A prefix scan confined to one sample that discards its tested coordinates fails the product-hull test on exponentially many matched-prefix patterns. A composite protocol that uses other samples or revisits old coordinates may evade this test. Continue only by constructing a product-rectangle selector or proving a cross-sample non-shareability charge. No C-75 or fusion bound follows. See bridge C-211/O-141.


### C-212 next-step queue

1. Reuse the exact sparse indicator `O(n+r*n/log(r+1))` and propagate it before developing any new point-patching or shattering argument.
2. Try to turn the improved C-191 scale `log r_Q=Omega(s1 log n)` into a quantitative Q-exit versus tail-router tradeoff under C-209's full product hull. Do not charge only equality-contained rectangles.
3. Test the tradeoff against C-80's O(N) block router and C-160's O(N log N) threshold separator.
4. Revisit O-141's state potential using `Omega(s2)` mismatch density and the `Theta(s2)` low-variation easy-router threshold. A valid potential must account for overlapping excluded high columns and repeated output support.
5. Keep C-210's rank-layer routing cost and all transfer thresholds unchanged unless a genuinely shared support-router construction is proved.

The shattering/context improvements are route-specific and are not an arbitrary-DAG lower bound. No breakthrough has been obtained.


### C-213 route filter

The cyclic product-rectangle model is too strong for lower bounds: a `5N`-state coordinate cycle solves all disjoint mismatch promises and safely revisits cross-history coordinates. Do not spend effort proving superlinear complexity in that model. Test only a representation theorem that preserves the fusion restrictions: can a legal pair-list closure encode independent row/column state predicates with controlled q? The universal root state needs the cut `X=Y`, so a generic answer is the sparse-envelope problem itself. If no structure beyond that is found, return to O-141 for acyclic DAGs and the native `x_i(v)` activation equations. Preserve C-80/C-160 counterchecks. No q bound follows.

### C-214 route filter — count the native closure syntax

The q-state least-fixed-point system has only 4Nq+2q^2+q bits of effective recurrence description, even though endpoints are arbitrary semantic subsets: two signed seed clauses per state, predecessor incidence, and empty outputs. Counting yields an artificial full partition with q=Omega(2^(N/2)), while the universal cyclic rectangle scan uses 5N states. This rules out generic polynomial compilation from cyclic rectangles to fusion. The promising next question is whether a concrete actual-promise restriction can force a closure-hard truth table on every separator; the medium band and the fixed explicit SIZE promise block direct counting. Do not treat C-214 as a Gap-MCSP lower bound. Preserve O-141 and all magnification losses. Full proof: research/C75_SHARED_DAG_CONTINUATION_2026-09-27.md.

### C-215 Q-exit graph update

For each state v, join low/high Q-signatures when their tail projections overlap. Every such edge must be separated on the descendant Q-output coordinates. A fixed pair witness persists to its routed child, but the graph can gain edges when the tail support shrinks and lose edges under filtering; neither edge count nor static excluded-column volume is a conserved potential. Continue O-141 only with a parent-conditioned pair/history flow that prices Q exits against tail suffix reuse and survives C-80/C-160. The 2026 monotone-learning lifting paper is conditional and sample-based; no C-75 image map is available. Details: research/C215_Q_EXIT_GRAPH_AUDIT_2026-09-27.md.

### C-216/C-217 next move — leave fixed scans behind; attack general merge reuse

C-216 sharpens the local state profile to `r_v*2^(N-k-t_v)<=M2+Delta_v`, but transition accounting fails because Alice children duplicate the deficit and Bob children pay `|Z|`. Do not sum this potential.

C-217 closes the fixed-order scan candidate: for any coordinate permutation, every prefix of length `Theta(s1)` has `2^j` low patterns and high completions, and product-hull safety forces distinct continuation states. The direct scan is therefore superpolynomial, but this says nothing about general rect-DAGs. Short-description transmission remains only a small communication-bit protocol; enumeration costs `N*2^(O(s1 log(n+s1)))`. Next seek either (a) an adaptive/revisiting DAG with near-linear size that evades the ordered-prefix obstruction, or (b) a theorem reducing arbitrary DAGs to ordered profiles with quantified overhead. Any proposed reduction must survive C-80/C-160 and beat the existing cubic cover-to-DAG loss. Neither direction is established. See C216/C217 reports.

**C-217 scope correction.** Only first-mismatch fixed-order scans are ruled out. If a protocol defers output, cross-pairs with different prefixes may still have a later mismatch and may be routed through a common suffix. Test this deferred-output construction directly before attempting to reduce arbitrary DAGs to ordered scans.

**Deferred-output follow-up.** The C-212 Hamming gap allows dropping any fixed `Theta(s2)` coordinates while retaining at least one mismatch per pair. This defeats any attempt to extend C-217's first-mismatch argument using only the fact that a cross-pair differs in the scanned prefix: a deferred protocol can rely on a later mismatch. But the remaining support still has `N-o(N)` coordinates, and support does not route pairs. Seek a product-rectangle-safe selector for a differing coordinate or a lower bound on the number of states needed to realize this selector.


### Idea 345 ? Use a stricter low threshold to create distance?dimension slack (C-218)

For any fixed `gamma<beta`, `SIZE(N^gamma)` is a subset of the magnification low set, so a separator lower bound for this smaller class transfers to the original. Its description entropy/VC dimension is `O(N^gamma n)`, while its distance from `CC>N^beta` remains `Omega(N^beta)`. This yields a sublinear per-column mismatch certificate `O(N^(1-beta+gamma)n)` and, via Sauer?Shelah, a fixed `O(N^gamma n)`-coordinate block whose missing patterns certify a constant fraction of high columns while all pairs retain a robust tail. The idea has not solved routing: selecting `Q_z`, finding the differing coordinate inside Q, and merging histories remain product-hull problems. Test the projected class `pi_Q(SIZE(N^gamma))` for a small search DAG; preserve C-80/C-160 and the existing `N^(3+3epsilon)/logN` transfer threshold.


### C-218-A ? Sauer completions rule out a fixed-order block router

For the C-218 block `Q` of size `2 VCdim(Y')`, take a prefix J of size `Theta(N^gamma)` that Y' shatters. Every prefix pattern p has a high completion in Q: the p-slice of `pi_Q(Y')` has VC dimension at most v on `2v-|J|>v` remaining coordinates, so Sauer-Shelah leaves an absent suffix pattern; its full-table cylinder has a high extension. The C-217 cross-prefix argument then forces `2^(Theta(N^gamma))` states for every first-mismatch fixed-order scan on Q. This kills only the obvious local scanner; deferred/adaptive routing and state sharing across Q branches remain open.


### Idea 346 - Count residual separators, not descriptions or scan prefixes (C-220)

A shared rect-DAG vertex represents one separator for the full Cartesian product of all row and column histories that reach it. The invariant is `pi_Kv(A_v) intersect pi_Kv(B_v)=empty` for the descendant output support `K_v`. This is the exact currency of safe state reuse. Circuit descriptions are only a change of row parameterization and preserve graph size exactly. The open idea is to find an overlap-safe potential that charges distinct residual separators across the DAG while surviving C-80/C-160 and C-209; otherwise construct a near-linear separator. Current loss: a separator lower bound must exceed `N^(3+3epsilon)/log N` to imply the target fusion lower bound through the known compiler.

**Route correction:** tree vertex complexity cannot be below DAG vertex complexity for the same relation. Use communication bits/depth versus graph vertices for that comparison. Also, since every rectangle is a triangle, `S_triangle<=S_rect`; a triangle-DAG lower bound would transfer, but C-194's universal `4N-1`-state triangle protocol makes a superlinear lower bound in that stronger model impossible. Binary search for a mismatch is not a one-state rect-DAG branch because interval-existence is joint in the two inputs; a multi-rectangle refinement is unbounded and remains open.


### Idea 347 - Feature order versus closure readout

A successful Q has a monotone least-fixed-point readout on its 2q seed-clause bits. Therefore every low/high pair must be incomparable in the order direction `sigma_Q(w) not<= sigma_Q(z)`: one clause is true on the low table and false on the high table. The clause's false set is a subcube, yielding an oriented subcube-cut cover. But all 2N signed literals give such a cover for any disjoint promise, while fixing one low table forces at least `N-log|SIZE(s2)|` clauses true there. This proves only a linear feature floor and places a hard ceiling on pairwise-feature arguments. The live target is the structured positive closure readout that pairs supports and shares predecessor carriers. Full proof: `research/C221_SEED_FEATURE_VS_CLOSURE_READOUT_2026-09-27.md`.



### Idea 348 - Adaptive wire signatures are necessary; fixed menus are exponential (C-222)

A C-115 signature is a partition of truth-table addresses into `K=2^k` fibers. The low class contains all support indicators on t=`Theta(N^beta/n)` points. Such an indicator factors through a signature exactly when its support is a union of whole fibers, and one K-cell partition represents at most `sum_{j<=t} binom(K,j)` supports. For K<=N^beta this is only a `2^(-Omega(N^beta))` fraction of all low t-sparse indicators. Any fixed menu that works for every low table therefore has `2^(Omega(N^beta))` items, even if its maps are arbitrary.

This rules out replacing the C-dependent C-115 wire choice by a public polynomial menu. It does not rule out an adaptive selector or a general DAG that shares without factoring each low table through a menu item. Next seek an implicit/adaptive selector with product-hull-safe state sharing, or abandon the signature route for a different C-75 invariant. C-80/C-160 remain controls. Full proof: `research/C222_FIXED_SIGNATURE_MENU_LOWER_BOUND_2026-09-27.md`.



### Idea 348-A - Separate menu entropy from selector circuit size (C-222-A)

The C-222 fixed-menu theorem is not an adaptive-selector lower bound. On its t-sparse witness family, sort `(w_i,i)` records with a bitonic network, output the t support addresses, and use them as the parameters of a shared point-indicator circuit. The selector costs `O(N log^3N)` gates and outputs `O(N^beta)` bits. This shows that exponentially many possible fixed maps can still have an efficiently computed choice on a structured family. The unresolved target is synthesis/selection for all low circuits and sharing the selected signatures without breaking product-hull safety. Full caveat: section C-222-A of the C-222 report.


### Idea 349 - An explicit adaptive signature selector is a search object (C-223)

If a circuit S outputs a size-`s1` circuit computing each low truth table w, then comparing that selected circuit against all N input bits gives a separator of size `O(|S|+N s1 log(s1+n))`. At OPS parameters the verification term is `O(N^(1+beta))`, so even a small selector does not give a near-linear DAG automatically. Conversely, a separator need not synthesize a circuit; passing from decision information into a circuit witness is a search-to-decision step, and classical exact MCSP search-to-decision is a known open question. This is not an equivalence for our gap promise. Do not infer general DAG hardness from selector hardness unless all small DAGs are shown to yield selectors. Continue O-141 on arbitrary product-hull-safe state reuse, and test direct near-linear DAG constructions separately. Full note: `research/C223_ADAPTIVE_SIGNATURE_SEARCH_MCSP_BOUND_2026-09-27.md`.


### Idea 350 - Robust signatures separate approximation error from fiber variation (C-224)

For an approximate low-table circuit C, include its output among k selected wires. Given a high table z, look up the majority z-bit in each signature cell, then point-patch all bad approximation addresses and all minority good addresses. This yields `CC(z)<=|C|+O(k*2^k+(e+m)n)`. Thus a high z forces either large approximation error or substantial within-fiber variation, which gives a valid equal-w/different-z witness. This extends the C-115 local lemma but supplies no DAG state charge: obtaining/signaling the adaptive signature and handling cross-history product hulls remain exactly the O-147/O-141 obstacle. Natural-property learning is only an approximate learner under stronger uniformity; it does not compile into the required DAG. Full derivation: `research/C224_APPROXIMATE_FIBERS_NATURAL_PROPERTY_BOUNDARY_2026-09-27.md`.

### Idea 351 - One-cell adversaries survive approximate signatures (C-225)

For any approximate C for low w with at least half its addresses good, take a largest signature cell among good addresses. If k is below both beta*n and (1-beta)*n, that cell has `N^(beta+delta)` addresses for some delta>0, enough to exceed the number of size-s2 circuits. Flip w on an arbitrary subset of this cell; counting supplies a high completion. The empty and full flips are low because the cell predicate is computed from C, the signature, and the known low circuit w. Patching against both endpoints forces `Omega(s2/n)` minority points in this one cell. Thus local variation cannot be converted into a count of many cells. Focus on selector-free identification and global product-hull charges; O-141 remains open. Proof: C-225.

### Idea 352 - Use alternating reachability as the native shared-state model (C-226)

A q-pair closure is exactly a cyclic alternating reachability game: each state requires both side obligations (universal fork), while each side chooses one seed/predecessor (existential support); least-fixed-point semantics means infinite plays lose. It has O(q) states, O(q^2) transitions on OPS covers, and input-dependent ranks. This captures sharing without miscalling it a rect-DAG. Standard MCSP NBP lower bounds extend to promise separators at threshold scale s1^{3/2-o(1)}, but do not transfer to the alternating model and only exceed N for beta>2/3. Pursue a direct alternating closure lower bound or a rigorously small compiler; the generic subset simulation is exponential. Full audit: C-226.


## Current phase priority - O-151 / C-227

Work on native closure certificate sharing and proof-context splicing. Track the signed seed support outside a shared state occurrence together with the support of a replacement subproof. The exact splice always exists syntactically; it contradicts soundness only if the union is consistent and leaves more than `kappa_square(s2)` coordinates free. C-230 pins this threshold to Theta(s2 log s2) at fixed-beta OPS scales. In parallel, seek a direct N polylog N or N^(1+o(1)) native cover for actual Gap-MCSP. Do not return to local signature refinements or generic BP flattening unless they prove one of these global claims. See O-151 and C-227/C-230.

## C-227 - Shared-state splicing has an exact consistency test

Represent an activation by a finite proof tree with signed truth-table literals at its leaves. At a rule state, every E-side support pairs with every H-side support; at a repeated state occurrence, any second proof rooted there can replace the first subtree. This formalizes what reuse actually forces. The mixed proof is syntactically valid, but opposite signs on one coordinate make the support unrealizable. If it is consistent, soundness implies it fixes at least N-log2(M2) coordinates. The new challenge is to force a shared occurrence whose context and replacement supports are consistent and leave more than log2(M2) coordinates free. Counting shared state names or wide certificates is not enough. Exact proof: `research/C227_NATIVE_CERTIFICATE_SPLICE_LAW_2026-09-27.md`.

## C-228 counter-calibration for O-151

A random subfamily of a structured family of individually easy tables can have enormous total-promise fusion readout complexity by counting alone. If the selected positives form a hypercube-independent set, every accepting certificate fixes all N bits and every consistent safe splice identifies an existing positive; no forbidden hybrid is forced. This does not model Gap-MCSP because the rejecting side contains easy tables. It does show that width, many easy anchors, and linear feature separation do not imply dangerous splicing. Any O-151 proof must use the specific geometry of SIZE(s1) against CC>s2. Full details: C-228.

## C-229 - Near-linear universal-circuit grammar attempt

Write low membership as `exists one small-circuit description d, then verify all N table bits against that same d`. Per-description coordinate chains give a huge cover. Sharing states across descriptions removes the witness identity and the positive grammar cross-combines unrelated side supports; keeping the identity restores one copy per description. This pinpoints the construction's first failed implication, but it is not a general lower bound because closure carriers could encode semantic consistency. Next seek a semantic quotient of partial descriptions, and charge its cross-compatible contexts. Full note: C-229.

## C-230 - Certificate width is tight at the subcube scale

Define kappa_square(s2) as the largest dimension of a truth-table-coordinate subcube entirely inside SIZE(s2). Soundness forces every consistent proof certificate to leave at most kappa_square free bits. Counting gives O(s2 log s2); Lupanov's circuit synthesis lets every labeling of an input-prefix block of Theta(s2 log s2) addresses be computed within size s2, giving the matching lower bound. Therefore the splice must leave more than Theta(s2 log s2) coordinates free; a better width theorem cannot come from counting alone. See C-230 and the original Lupanov citation there.


## Current route superseding O-151 priority: C-75 shared DAG (C-232)

The user's latest steering prioritizes standard acyclic product-rectangle DAG complexity. The generic short-description shortcut is falsified: some N-output Karchmer-Wigderson mismatch relations have O(N) communication bits but Omega(2^N/N) DAG states. For actual Gap-MCSP, descriptions and truth tables induce exactly the same minimum DAG; universal evaluation leaves an expensive `exists d forall k` check, and 2N mismatch rectangles do not automatically binary-expand while keeping intermediate nodes rectangular. O-152 is the active obligation: lower-bound the OPS separator above `N^(3+3epsilon)/log N` or build a near-linear DAG. Keep `rho<=O(S_rect)<=O(rho^3/log rho)` and the product-hull merge law explicit. C-232 is not an actual-promise lower bound. Native proof splicing O-151 is subordinate unless it improves this target.

## C-233 — Worklist activation ranks do not yet compile to a DAG

Native q-rule activation ranks solve the min–max recurrence `tau_i=1+max(min E-support rank,min H-support rank)`. A Dijkstra-style heap finalizes each active rule once and processes each support incidence once, giving `O(q^2 polylog q)` RAM evaluation. The input-dependent heap and memory access pattern is not a Boolean circuit. TSCs give a sharper model distinction: the direct cyclic positive-signal network is an `O(q^2)` partial recognizer (YES→1, NO→Z), while RAM simulation gives a total `O(q^2 polylog q)` separator. A partial-TSC lower bound above `N^(2+2epsilon+delta)` would force q superlinear, but no such bound is known and TSC is more expressive than an acyclic DAG. Standard `O(q^3/log q)` rect-DAG transfer remains unchanged. Next test: an oblivious fan-in-two simulation with `O(q^2 polylog q)` area despite rank-reversing SCCs, or keep TSC as a separate model. Full proof: `research/C233_MINMAX_ACTIVATION_RANK_AND_TRISTATE_RAM_BRIDGE_2026-09-27.md`.
## Idea 353 - Blockwise description replication and the mixing dichotomy (C-234)

Encode every k-bit Boolean function g, with 2^k=Theta(s2), as a low n-bit table by repeating g across r=N/2^k=Theta(N/s2) prefix blocks. Independent choices in all blocks range over the full table cube, so almost every hybrid is high by circuit counting. If proof trees exposed a disjoint state occurrence per block whose subtree and outside context were block-pure, state-label reuse would force exponentially many accepted hybrids and q>=2^(Omega(s2)).

The localization condition is false as a generic inference: the diagonal-only subpromise is decided by an O(N)-size block-equality circuit and has an O(N)-pair fusion cover. The live new invariant is therefore block-mixing entropy: quantify how much a state subproof and its context jointly touch across blocks, then prove either many independent substitutions survive or the mixing requires superlinear q. Do not assume address blocks align with proof-tree branches. Full conditional proof and hostile test: C-234.
## Idea 354 - Overlap fingerprints versus prefix-varying ownership (C-234)

On the repeated-circuit family w_g(p,u)=g(u), a context from g and replacement subproof from h are compatible exactly when g=h on every suffix input u represented in both supports (in any prefix block). This overlap is a partial description fingerprint. Full overlap blocks cross-description splicing. Outside the overlap, if each suffix input's repeated copies are all assigned to one side, the splice completes to another low diagonal table. A dangerous hybrid needs ownership to vary across prefix blocks on many suffix inputs. The next measure should jointly track fingerprint coverage and the circuit complexity/entropy of the ownership mask, not merely shared state labels or certificate widths. Details and conditional theorem: C-234.

### C-235 — Attack canonical endpoints, not only free-cube dimension

Represent every proof support by its Boolean interval `[ell,u]`. A compatible splice intersects intervals; its lower endpoint is the OR of positive supports and its upper endpoint is the AND of the complements of negative supports. Both endpoints must be size-s2 for a sound output proof. This suggests searching for a high-complexity ownership join directly, which could evade the already-tight safe-cube dimension barrier. The law is exact but does not force such a join: the unproved work is to show that covering all low circuits with few states forces a high join/meet. The singleton-safe artificial promise and diagonal equality cover are counterexamples to any generic forced-splice claim. See C-235.

C-235 literature motif: Austrin–Risse's SoS MCSP lower-bound framework uses CSP incidence expansion and local Boolean substitutions; their paper also treats monotone circuit size on monotone Boolean slice functions. Try replacing C-234's repeated blocks with expander-overlapping local views so nonlocal sharing can be tracked through an incidence graph. The exact transfer is absent: SoS refutations and native fusion readout are different measures, and encoding a hard slice promise as actual low/high-complexity truth tables is unresolved. Source: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2023.31.

### C-236 — Bound the compatible ownership-mask image

For typical repeated low anchors g,h, their disagreement set has Theta(N) coordinates. A compatible context/subproof splice induces a selector choosing g or h on each disagreement coordinate; its endpoint is low, so at most `|SIZE(s2)|=2^(o(N))` distinct masks can occur among `2^(Theta(N))` possibilities. The exact missing step is a grammar-wide theorem connecting q states to the number/structure of these masks. The diagonal equality cover shows q=O(N) can safely restrict them to prefix-constant profiles; do not count proof trees without a bound on cyclic unfoldings or seed incidence. See C-236.

C-236-A: Each compatible mask has an explicit completion `H_mu=w_h XOR mu` accepted by the splice. Thus the safe profile set is precisely bounded by the number of low tables; most masks on D have a canonical high completion. This makes profile avoidance a necessary behavior of any sound closure, but it does not yet say how many q-states profile avoidance costs. The diagonal equality cover realizes only prefix-constant masks and remains the main counterexample to generic claims.

### C-237 — Do not pursue random-pair free-width improvements

The selector-safe set for a typical repeated-anchor pair still contains a cube of dimension `Theta(s2 n)`, matching the universal C-230 limit. Explicit constructions use a prefix subcube in one differing suffix column for beta<1/2, and multiple differing suffix columns with arbitrary prefix functions for beta>=1/2. Thus a local dimension-only argument is exhausted. Next measure the grammar's ability to select/describe these structured free sets and ownership masks, or pursue the full-promise upper cover. See C-237.

### C-238 — Common ranked witness skeletons mix globally

If x,y share the same active-state/predecessor topology in their ranked proof DAGs, combine all E-side seed witnesses from x with all H-side witnesses from y. Consistency suffices for a valid finite accepting proof, so the whole mixed cylinder is low. This exposes a global strategy-level product beyond one occurrence. Pigeonholing fails because a q-rule list admits up to `2^(O(q log q))` skeletons; the repeated low anchor family is much smaller. Seek restrictions on realizable skeletons from the fixed recurrence, not a raw count. See C-238.
### C-239 — Canonical rank fibers and cross-family conflict-or-cover

The state activation-rank vector alone does not determine the witness skeleton: a nonmaximal side can use either a seed or a predecessor while preserving the state rank. The two side-support minima per state do determine one canonical skeleton, so equal-side-rank anchors satisfy C-238's full E/H mixing law. For fixed Q, the canonical profile is a function of the 2q-bit seed signature, giving at most 2^(2q) canonical fibers. This sharpens the count for the canonical choice, not the set of all possible witness topologies, and is still too large for pigeonholing. Every shared state has a precise semantic duty: all context/replacement pairs either contain opposite rails or jointly cover all but kappa_square(s2) coordinates. The next target is an extremal bound for such cross-families under the legal endpoint-containment recurrence. A blockwise circuit-description cover still needs to keep one description alive across every block. See C-239.
**Artificial-model check for C-239.** Monotone clique-versus-coloring is not the needed toy: each YES clique certificate leaves N-binom(k,2) bits free and all completions remain YES, unlike the `kappa_square(s2)=o(N)` safe-cylinder regime. Exact-clique recognition requires negative information and loses the standard monotone lower bound. Seek a width-preserving lift before importing monotone global-witness arguments. Razborov's primary paper: https://www.mathnet.ru/php/archive.phtml?jrnid=dan&option_lang=eng&paperid=9192&wshow=paper.
C-239 collision check: one literal seed test per suffix input u separates all repeated anchors w_g(p,u)=g(u) with Theta(s2) features. The q>=N-o(N) regime has enough raw seed capacity, so don't use a seed-profile pigeonhole. Seek a restriction coming from endpoint-containment geometry plus soundness.

## Idea 355 — Representation-invariant shared routing (C-241)

The short-description route is exactly audited: any shared rect-DAG over circuit descriptions pulls back/restricts with no vertex change, so syntax cannot itself compress the graph. A universal evaluator only evaluates G(d)[k]; it does not remove the shared exists-d forall-k consistency problem. The direct minterm and dyadic-profile DAGs remain exponential. The live idea is to turn the product-hull condition into a global potential on residual row/column projections, allowing adaptive DAG merges but charging each genuinely new residual separator. C-215/C-216 show that naive statewise deficit sums fail; next candidates must account for overlap when paths enter from Alice and Bob splits. No lower bound is yet obtained.
The C-240 empty-root normal form reduces seed-clause preprocessing to O((q-m)N+m) when m output roots have complementary singleton seeds. It leaves the predecessor OR routers untouched, so the dense-SCC cost remains. Do not pursue this as an asymptotic compiler unless endpoint-containment yields a bound on support incidences or SCC feedback.


## Idea 356 — Couple native splice intervals to high-side blocker maps (C-242)

The exact cyclic recurrence has a finite antichain-semiring grammar: alternatives are minimized unions of support families, and each rule takes the union-product of its E/H supports. Cycles are resolved by least finite-proof semantics; every minimal support has a witness of height at most q. For any high table z, choose one false side at each inactive state. Following those blocker choices through a ranked proof of any low w yields a path entirely through states active on w and inactive on z, ending at a seed literal where w and z differ.

At a shared state i, every context/replacement pair gives an output proof. If compatible, its whole Boolean interval is contained in SIZE(s2): both the positive-rail OR endpoint and negative-rail AND endpoint are low, and at most kappa_square(s2)=Theta(s2 log s2) coordinates remain free. This is stronger than free-width alone, but still no q-charge. The candidate invariant is the joint incidence of (i) high blocker choices and (ii) compatible context/replacement interval endpoints. A useful theorem must show that covering all low circuits forces a forbidden high join or superlinear q; a construction must exploit only joins whose entire intervals stay low.

The dual blocker path itself is only a short pairwise mismatch witness and does not give a superlinear bound. C-228 remains counting hardness without dangerous splices; C-234's block-isolation condition is false as a universal inference because the diagonal subpromise has an O(N) equality cover. Continue with the full-promise near-linear cover in parallel. Full exact derivation and limitations: research/C242_NATIVE_CERTIFICATE_ANTICHAIN_AND_BLOCKER_PATH_2026-09-27.md.


## Idea 357 — Prefix-intersection cover as the native upper-bound baseline (C-242)

For any fixed ordering of truth-table coordinates, build one carrier for each realized low-table prefix p: T_p is the intersection of its matching high-side coordinate slices. Each prefix extension uses one legal fusion pair (parent carrier, next literal slice). Stop at length N-1. Every low w and its one-output-bit neighbor have circuit size at most s1+O(n)<s2, so the high-side intersection T_p for w's N-1 prefix is empty. This gives a valid native cover of size at most sum_{t=2}^{N-1}|pi_t(SIZE(s1))| <= N|SIZE(s1)|.

The construction is exponentially large: C-212's uniform Theta(s1)-coordinate shattering gives 2^t distinct nonempty prefix cylinders for every t<=c s1 (the high side intersects each because each such cylinder has size much larger than |SIZE(s2)|). Thus the fixed-order prefix trie cannot give N polylog N. This only retires this fixed-order construction; adaptive coordinate choice, semantic circuit quotients, and non-prefix closure joins remain open.


### Idea 359 — Factor the output into safe state zones (C-244)

For each state i, let P_i be the family of finite proof supports rooted there and K_i the family of accepting-context supports with a marked hole at i. Then the legal accepted language is exactly the union over i of the intersections [P_i] AND [K_i]. Every low anchor lies in at least one such state zone, and soundness makes every whole zone a subset of SIZE(s2). At a high table, every state has either no matching context or no matching replacement proof. This packages all cross-splices at a state into one global factor rather than tracking a selected collision.

The new lower-bound target is to bound the low-circuit mass or description entropy of a zone from the shared grammar that generates both context and proof supports. Zone count alone fails because each zone is a union of potentially exponentially many cylinders; C-228 and C-234 remain hostile checks. In parallel, synthesize the full-promise zones in N polylog N or N^(1+o(1)) states. Exact theorem and proof: research/C244_STATE_ZONE_FACTORISATION_AND_GLOBAL_READOUT_2026-09-27.md.


### Idea 360 — Differentiate the certificate grammar at a marked state (C-245)

Use an antichain semiring whose addition is alternative derivation and whose multiplication unions compatible supports. Add a one-hole context component: in each two-sided rule, the marked hole propagates through one side while the other side carries an ordinary proof. This is the proof-support analogue of automatic differentiation. It generates all context/replacement joins from the same cyclic grammar.

For any input where a context and proof at i both match, their substitution yields an accepting proof containing i. Loop deletion along the root-to-hole path and rank-minimal sibling derivations give a matching context of height at most 2q. So the full-context state zone is captured by this bounded marked grammar. The construction has q^2 family labels across target states but may have exponentially large antichains; label counting gives no lower bound. Next seek an invariant on the joint support-incidence tensor that uses actual low/high circuit geometry. See research/C245_MARKED_ANTICHAIN_GRAMMAR_FOR_CONTEXTS_2026-09-27.md.


### Idea 361 — Repeated-block certificate capacity versus grammar count (C-246)

For C-234's repeated table family, a support cylinder can contain an anchor with freely varying g(u) only if all r repeated copies of that suffix coordinate are unfixed. With at most kappa_square(s2)=o(N) free coordinates, one safe output certificate covers at most 2^(kappa/r)=2^(o(s2)) of the 2^(Theta(s2)) diagonal anchors. This forces exponentially many proof certificates.

The q-state grammar can still have q*2^q*(2N+q)^(2q) ranked witness DAGs. At q around N this capacity dwarfs the low-anchor family; the count gives only a bound below the established linear floor. Thus raw antichain cardinality and proof-tree counts are closed as routes to superlinear q. The next invariant must use cross-join compatibility/endpoint geometry, not merely how many certificates exist. Full derivation: research/C246_REPEATED_BLOCK_CERTIFICATE_CAP_AND_COUNTING_FAILURE_2026-09-27.md.


### Idea 362 — Multi-hole splice entropy and private regions (C-247)

Mark pairwise disjoint occurrences in one accepting proof. Replacing all of them at once with arbitrary rooted proofs is valid whenever the total support remains consistent. If each replacement choice has an associated anchor code on a private coordinate region untouched by the context and other replacements; distinct anchors have distinct projections there, every tuple gives a distinct accepted table. Soundness caps the product of replacement-family sizes by |SIZE(s2)|.

This recovers C-234's exponential hybrid contradiction under block isolation, but does not force private slots. Nested occurrences, cross-rail conflicts, and diagonal fingerprints reduce the compatible product. The next target is a q-sensitive dichotomy between large splice partition function and expensive organization of overlaps. Total entropy is only O(N), so it cannot alone yield a superlinear q bound. Full theorem and limits: research/C247_MULTIHole_SPLICE_ENTROPY_BUDGET_2026-09-27.md.


### Idea 363 — Blocker rectangles as the native product-hull object (C-248)

For each state i, define A_i as low tables activating i and B_i as high tables on which i is inactive. The product R_i=A_i×B_i is forced by unary state semantics. Every pair in R_i has a high-blocked side; the low table supplies a seed or predecessor on that same side, giving an exact recursive decomposition into mismatch rectangles or R_j. Activation rank terminates every pair's route. This makes global cross-state reuse explicit, but rectangle area/count fails: the artificial promise Y=all nonconstant tables, Z={0^N,1^N} has a one-rule cover with R_1=Y×Z. Different pairs route to different mismatches, so a shared pair rectangle does not itself produce a mixed truth table. Seek a lower bound on the shared two-sided routing grammar, not on rectangles alone.

An independent compiler unrolls q rounds to at most 3q²+1 unbounded-fan-in monotone gates, gate-count model only. Its O(q²(N+q)) incidences remain cubic near q=N, so it does not repair the standard compiler. The relevant lower-bound target would be monotone extension complexity of the actual dual-rail Gap-MCSP promise; no such bound is known here. Full proof and literature boundary: research/C248_BLOCKER_RECTANGLES_AND_MONOTONE_EXTENSION_COMPILER_2026-09-27.md.


### Idea 364 — Bi-blocked output roots and fixed escape witnesses (C-249)

Because the actual high set intersects every signed literal half-cube, a minimum-rank active empty-carrier root on any accepted low input cannot have an empty endpoint. Such a side would need either an impossible empty seed slice or an earlier empty-carrier predecessor. Each useful root therefore has two nonempty disjoint endpoints and contains high witnesses z_E,z_H that block the opposite sides. C-240 further limits direct seed vocabularies to one complementary literal pair or a seedless side; every proof must escape the root through a predecessor. H-side escapes pair with the fixed z_E, and E-side escapes with z_H.

This provides a normalized root-to-escape layer but no charge for how many anchors each predecessor rectangle serves. Root count, fixed witnesses, and the one-bit selector are only O(q). The next theorem must aggregate the escape relation with safe context/proof joins, or show how to build a near-linear full-promise cover. The C-248 q=1 toy fails the high-side shattering condition, so it only blocks generic rectangle-area arguments. See research/C249_BIBLOCKED_OUTPUT_ROOT_NORMAL_FORM_2026-09-27.md.


### Idea 365 — Half-safe escape supports at seedful roots (C-250)

At a minimum-rank output root with a direct seed literal (k,b), a low anchor matching that literal cannot exit through an opposite-side seed. It must use a predecessor. The high half-cube inside the seed side is excluded from the opposite endpoint and hence from the predecessor carrier. C-243 then says every high completion of an escape support avoids bit b, so that half of the support cylinder is all low. This forces at most ceil(log2|SIZE(s2)|)+1 free coordinates.

On repeated-block anchors this gives a per-support capacity of 2^((kappa+1)/r), recovering the certificate-capacity phenomenon for seedful branches. Taking the result to its limit still fails at certificate-to-state counting: q states permit exp(O(q log(N+q))) ranked witness-DAG descriptions, which is too many at the linear scale. Seedless roots still need the two-sided C-242/C-247 join analysis. Next seek a grammar-wide reuse charge, not a stronger local width bound. Full derivation: research/C250_ONE_SIDED_SAFE_ESCAPE_CYLINDERS_2026-09-27.md.


### Idea 366 — Root escape dichotomy closes the local seedless gap (C-251)

At a normalized empty output root, inspect a low anchor's selected root proof. If a direct seed matches, the other side must use a predecessor, whose support is half-safe by C-250. If no direct seed matches, both sides use predecessors; their support union is consistent, and every completion preserves the empty-root proof, so the whole union cylinder is low. Thus every low anchor has either a one-sided half-safe escape support or a two-sided wholly-low paired support. On repeated-block anchors either signature type has capacity at most 2^((kappa+1)/r).

This takes the local argument through seedless and missed-seed roots, but still stops at signature counting. Paired proof-DAG counts square the previous upper bound only up to constants, leaving exp(O(q log(N+q))) descriptions. The next step must charge incidence/overlap among signatures that reuse states, or construct a near-linear full-promise cover. No state lower bound follows from per-signature capacity. Full proof and exact failure: research/C251_ROOT_ESCAPE_SUPPORT_DICHOTOMY_2026-09-27.md.


### Idea 367 — Quotient root escapes to a state-conflict graph (C-252)

For each empty output root i, every pair of active predecessor states (j\in P_i,k\in R_i) is forbidden on high tables: C-243 would put a high table in both disjoint endpoints. A matching direct seed on one side plus an active opposite predecessor is likewise forbidden. Conversely every accepted low triggers one of these patterns. Collapsing over roots yields a bipartite conflict relation on at most q state pairs and at most 2qN state/literal incidences; the resulting depth-two readout has at most q^2+2qN terms.

This quotients exponentially many certificate supports into state fibres and gives a concise representation of the O-153 cross-root obstruction. In the OPS regime q=Omega(N), its transfer to ordinary unbounded-fan-in gates is still O(q^2), matching C-248, and graph independence alone cannot bound how many high tables share a profile. Next search for a fibre-geometry/VC or closure invariant that links the q-state activation map to the actual SIZE(s1)/outside-SIZE(s2) promise. Do not use graph size or edge count as a lower bound. Full proof and failed count route: research/C252_STATE_CONFLICT_GRAPH_READOUT_2026-09-27.md.

### Idea 368 ? Conflict-profile fibres are marker subcubes (C-253)

For each exact active-state profile sigma, a conflict edge makes its whole fibre low. If sigma is independent, active states carry a marker vocabulary B_sigma: every low table in that fibre matches some marker, while every high table avoids all markers. Thus the high part lies in a subcube fixing r_sigma coordinates, with size at most 2^(N-r_sigma). Summing fibres gives a high-realized profile with r_sigma<=log2(I)+o(1), where I is the number of independent profiles represented on U.

This fails as a q-charge because the weakly marked profile may be unused by low inputs, while low profiles can be edgeful. Two-wise shattering does not by itself couple those fibres; one profile with no markers can support all high coordinate patterns. Next test the closure equations under coordinate flips/partial assignments, or retire graph-only entropy counting. Full proof and exact limitation: research/C253_CONFLICT_PROFILE_FIBRE_SUBCUBES_2026-09-27.md.

### Idea 369 ? Hazard boundaries on the partial-support lattice (C-254)

Extend each state to partial assignments by asking whether it has a proof support contained in C. This is monotone. If a partial support already activates a conflict pair or a state plus an incident seed literal, every completion activates an empty root and is low. Hence any first hazardous prefix for a low anchor fixes at least N-log2|SIZE(s2)| coordinates, under every coordinate order.

Selected-witness correction: a readout term has a finite ranked proof DAG on at most q state labels, with at most two seed literals per state plus one marker. This gives q >= (N-log2|SIZE(s2)|-1)/2, a valid but weaker-than-known linear floor. To improve it, aggregate overlapping witness DAGs across anchors; state-on event counts alone remain insufficient. See corrected C-254.

### Idea 370 ? Approximate-MCSP magnification parameter bridge, endpoint mismatch

If a truth table z is h entries from a size-s1 table, point-patching yields a circuit for z of size s1+O(h n). Therefore outside SIZE(s2) implies distance greater than (s2-s1)/O(n) from SIZE(s1). For s2=N^alpha, the fractional gap is about N^{-(1-alpha)}/polylog N; an approximation radius N^{-eta} with eta>1-alpha makes the exact gap promise a restriction of approximate MCSP.

Atserias?Muller (2025) magnify suitable sparse approximate-problem lower bounds to NP not subset NC1 or P different from NP^oplusP. Those statements do not by themselves imply P different from NP, and the required formula/uniform-circuit lower bound remains unproved. Keep this as a checked parameter connection, not a replacement for the native fusion lower bound. Source: https://arxiv.org/html/2503.24061.


### Idea 371 — Residual-hull state charge for the C-75 mismatch DAG (C-255)

For a shared DAG node v with rectangle A_v x B_v, let K_v be all output labels below it. Correctness is exactly `pi_Kv(A_v) intersect pi_Kv(B_v)=empty`. When histories merge, the suffix must solve the full cross-product hull of their unions. Try to attach to each state a residual signature whose potential decreases under every child transition and whose total cannot be charged twice when high projections overlap. C-80/C-160 are hostile checks. A local projection deficit or description count is not enough. The useful quantitative target through the current compiler is `S_rect>N^(3+3epsilon)/log N`; alternatively, an `N^(1+o(1))` adaptive DAG would kill the superlinear-cover route. No potential is proved yet. See C-255.

### Idea 372 — Transfer DAG bottleneck counting through a hard-image search embedding (C-255)

Beame–Whitmeyer (ICALP 2025, Theorem 1.7) prove a `2^(Omega(m^(1/4)))` lower bound for triangle-DAGs solving bit-pigeonhole search. Taking `m=K(log N)^4` clears the current compiler threshold for large K. The hard-image condition has a new solution: since `|SIZE(s1)||SIZE(s2)|=2^o(N)`, choose a common mask `r` outside `SIZE(s1) xor SIZE(s2)`; then every low codeword `u` maps to the high table `u xor r`. The unresolved condition is answer soundness: for each coordinate, one of the two signed mismatch rectangles is diagonal (if r_k=1) or off-diagonal (if r_k=0), and every such rectangle must be contained in a valid source-answer set under a fixed decoder. No BPHP encoding with this cut-soundness property is known. A separate bottleneck-width adaptation still lacks a per-node capacity lemma. Full proof: C-255.
### Idea 373 — Common-translate answer-code reconstruction obstruction (C-256)

Static output-label decoding can leak enough structure to reconstruct the supposedly hard mask. For a two-wise-rich hard KW partition with 0,e_i on one side and 1^M on the other, every active C-75 coordinate must encode one source bit with the same phase on both parties. The active-coordinate indicator is OR_i(u_0 xor u_ei), and r=v_1 xor u_0 xor active; this costs O(Ms1). The full-domain BPHP source is also blocked: both signed labels at an active target coordinate would make the Alice domain the union of two fixed collision-equality sets, which cannot cover it. These are reduction-interface no-go results, not target lower bounds. Next test whether terminal-specific decoding has a small enough binary-DAG refinement cost; otherwise focus on direct bottleneck capacity or an actual C-75 DAG construction. See C-256.

### Idea 374 — Parity-code splicing lock (C-257)

The even/odd parity promise has a native fusion cover of size `4N-4` although every proper partial assignment has an odd high completion and every consistent accepting support fixes all N bits. Any consistent splice is again even. This is a hostile calibration: width, high-side richness, and anchor count do not force dangerous splicing. The missing target-specific resource is common short-description consistency for `SIZE(s1)` under mixed support joins. Do not use this toy as an OPS lower bound. See `research/C257_PARITY_CODE_SPLICE_LOCKING_CALIBRATION_2026-09-27.md`.

### Idea 375 - Native equality-fingerprint subcover (C-258)

An explicit `2N+2d-1`-pair native list covers all tables constant on each of d blocks of size r, provided this repeated family is disjoint from the actual high set. It builds the two fixed-value carriers for each block, merges them, then intersects across blocks. In particular it covers a `2^d`-member subfamily of `SIZE(s1)` when `d log d=O(s1)`. This is the direct-native form of C-234's diagonal equality escape, not a cover of all low circuits. Next test whether a near-linear family of semantic fingerprints can cover the full low class, or prove that arbitrary circuit descriptions resist all such compression. See C-258.

### Idea 376 - Product-code closure bound (C-258)

For a product of local codebooks `A_j` on coordinate blocks `B_j`, C-258 gives a direct rule count `q<=sum_j |A_j||B_j|+2d-1`. The repeated-block family is the constant-size-library case. This makes explicit how a compact global fingerprint can support extensive reuse; the upper-bound question is whether all low circuits admit a near-linear collection of such regions, and the lower-bound question is whether circuit-description compatibility prevents that. No answer is known. See C-258.

### Idea 377 - The cofactor/splice threshold is Theta(n) (C-259)

The exact circuit patching budget is `CC(hybrid)<=t s1+O(t)`, so up to `Theta(n)` prefix-selected low cofactors remain below s2. The C-247 product entropy budget gives the reverse scale: more than `C n` private slots with `2^(Theta(s2))` alternatives contradict soundness. Next prove the missing q-to-slot/selector theorem; do not count a constant number of compatible holes as progress. See C-259 and C-116.

### Idea 378 - Pair proof joins with their dual blockers (C-260)

The native least-fixed-point grammar generates minimal proof certificates `C_i` and their exact minimal transversal blockers `B_i`. For an accepting context K with a hole at i, every consistent join `K union P` with a proof P rooted at i is an accepting output certificate, and every output blocker hits it. Pigeonholing forces an internal state to serve `2^d/q` repeated-block anchors when `d log d=O(s1)`, but C-258's O(N) equality fingerprint shows this reuse can remain safe. This creates a two-sided incidence object `(K,P,B)` tied to one q-rule grammar. The missing bound is incidence multiplicity: one blocker can hit many joins. No q lower bound follows. Full derivation: C-260.
