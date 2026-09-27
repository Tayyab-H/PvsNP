# Dead ends and reusable failure lessons

## Minimax existence does not construct the selector (C-40)

1. **Attempt.** Treat the minimax anti-approximation distribution as the missing selector and try to use its short random sample directly.
2. **Exact failure.** Minimax proves $\exists\mu\,\forall D$; it gives no small circuit computing $\mu$ from $f$. The natural LP separation problem is weighted circuit fitting. Random rounding gives a valid list with high probability, not an always-correct map for every hard table.
3. **Type.** The existence theorem is correct; the claimed algorithmic upgrade is a quantifier/error-correction gap. The margin value itself restates Gap-MCSP across the relevant thresholds.
4. **Next attempt.** Find a constructive dual-witness extraction method that bypasses the weighted fitting oracle, or prove such extraction requires the O-1 lower-bound complexity. Do not rename the LP value as an independent invariant.

## Per-anchor proof-DAG leaf counting

1. **Attempt.** Trace the first rule deriving the empty intersection for one low-circuit anchor; charge leaves to matching truth-table literals.
2. **Exact failure.** It proves at most m+1 leaves and hence m>=N-O(s2 log(n+s2)). There are only N distinct coordinates, so this charge cannot become superlinear.
3. **Type.** Fundamental limitation of this invariant.
4. **Next attempt.** Charge cross-anchor reuse or another global circuit resource. Repeating the same trace with more notation will not pass N.

## Unrestricted row/column graph proxy

1. **Attempt.** Identify a table with a pair of halves and lower-bound a two-dimensional graph cover.
2. **Exact failure.** On the restricted promise domain the target factors as a single rectangle, so the proxy has cover number at most one.
3. **Type.** The proxy forgets the relevant structure.
4. **Next attempt.** Keep original bit-literal generators, or prove a transfer that retains the lost information.

## Canonical and feature-span semi-filters

1. **Attempt.** Use canonical graph/literal filters, majority/support filters, Reed Muller spans, affine-orbit features, or q-ary feature spaces.
2. **Exact failure.** Explicit disjoint endpoint pairs cover these families, often in one pair.
3. **Type.** Construction-family failure, not evidence that all semi-filters are easy.
4. **Next attempt.** Construct noncanonical filters and test arbitrary endpoint pairs before claiming a lower bound.

## Separator-to-filter shortcut

1. **Attempt.** Assume a small circuit gives an efficiently recognizable hard-complexity filter, then invoke a filter theorem.
2. **Exact failure.** Proving the filter axioms and high-complexity condition already requires the lower-bound content; this is circular.
3. **Type.** Circularity.
4. **Next attempt.** Work directly with the promise-cover measure and its published circuit transfer.

## Confusing the local cover compiler with the lower-bound transfer

1. **Attempt.** Use the project firing-rule compiler from an m-pair cover to a separator of size O(Nm+m^3) as the bridge to arbitrary circuits.
2. **Exact failure.** This direction alone does not show arbitrary small separators yield small covers.
3. **Type.** Wrong implication direction if used alone.
4. **Next attempt.** Use Cavalar and Oliveira rho<=D_cap inequality: each separator gives an intersection construction with at most its number of AND gates. This closes the bridge for the matching measure.

## Fixed-clock K target and increasing q

1. **Attempt.** Set R_q={x:K^(n^q)(x)>=|x|-1} and increase q until compression contradicts a polynomial decider.
2. **Exact failure.** A polynomial decider may have any fixed degree; compression only forces degree at least q for that fixed language.
3. **Type.** Quantifier mismatch.
4. **Next attempt.** Produce one fixed language with an unbounded degree requirement or prove a fixed R_q is not in P.

## Expected-violation minimization

1. **Attempt.** Prove an expected-violation margin for UNSAT and round by conditional expectation.
2. **Exact failure.** The inequality and rounding are sound, but finding an assignment with expected violations below one requires the hard global minimization.
3. **Type.** Algorithmic gap, not a flaw in averaging.
4. **Next attempt.** Prove a structural optimizer theorem or a polynomially computable surrogate.

## Direct liar / proof-deadline diagonalization

1. **Attempt.** Self-reference against all polynomial SAT solvers or bounded proof search.
2. **Exact failure.** The explicit tableau is too large, or the diagonal sampler s runtime expands the clock so it no longer diagonalizes against the predictor at the invoked clock.
3. **Type.** Resource/self-reference mismatch.
4. **Next attempt.** Give a time-preserving fixed point while keeping the language NP-verifiable; recursion-theorem existence alone is insufficient.

## Source-hiding / randomness floor

1. **Attempt.** Obtain a large conditional Kolmogorov-complexity NO gap from a reduction using little randomness.
2. **Exact failure.** Source plus random tape is a short conditional description when the clock covers the reduction. HIR already samples an n-bit message, so the bound is compatible.
3. **Type.** Parameter floor, not a contradiction to HIR.
4. **Next attempt.** Establish a hiding or extraction theorem beyond source-and-tape counting. This does not currently touch arbitrary SAT solvers.

## Finite experiments

Finite exhaustive tests can reject a pair list or template. Passing small cases does not imply an asymptotic lower bound. Preserve experiments as counterexample search, never as proof.

## Naive per-rule anchor capacity

1. **Attempt.** Bound the cover size by arguing each pair can affect only a bounded number of low anchors.
2. **Exact failure.** A two-coordinate construction, recorded as C-09, makes one pair violate an explicit upward-closed anchored filter for N affine low-circuit tables. High-promise three-coordinate fullness verifies the claim.
3. **Type.** This is a counterexample to the naive capacity statement, not to the main route.
4. **Next attempt.** Charge completed derivations or shrinking of the residual high set, not raw rule activations or pair-filter incidences. Keep the distinction between hitting one filter and covering every filter above an anchor.

## Hamming-ball threshold filters have a one-pair cover

1. **Attempt.** For each low anchor, take the uniform distribution on high tables within Hamming radius d=K s2 and define F_a={S:mu_a(S)>1/4}.
2. **Result.** These are valid semi-filters: they are nonempty, upward closed, exclude the empty set, and contain every matching literal slice. Circuit counting makes each local support exponentially large and gives each matching slice mass 1-o(1). A random two-coloring of U balances every local measure simultaneously by Hoeffding plus a union bound over all low anchors. The resulting disjoint pair (E,H) has mu_a(E),mu_a(H)>1/4 for every a, while E intersect H is empty. It therefore violates every one of these selected filters. See C-10 for the full proof.
3. **Type.** This is a rigorous collapse of one proposed dual support, not a definitional failure and not a counterexample to the main lower-bound route. Any fractional dual supported on these filters has a pair covering its full mass.
4. **Next attempt.** Search for distributions over more varied, nonlocal semi-filters whose pair-violation mass remains small. A single scalar measure around each anchor is too easy to balance by an arbitrary disjoint partition.

## Symmetric high-anchor counting attempt is invalid

1. **Attempt.** Apply the low-anchor leaf-count proof with target $Z$ and assert that a matching subcube avoiding all low tables has at most $M_1$ points, yielding $\rho(Z)\ge N-\log M_1-1$ and a $2N-o(N)$ total gate bound.
2. **Exact failure.** The cube is disjoint from $Y$, but its other points may be gap tables or members of $Z$. Therefore its size is not bounded by the number $M_1$ of low tables. The claimed symmetric entropy estimate is false as an inference.
3. **Corrected result.** A q-point truth-table pattern can be interpolated by a DNF of size $O(qn)$. Thus an empty high-anchor cube must fix $q=\Omega(s_1/n)=\Omega(N^\beta/n^2)$ coordinates, giving only a sublinear complement-side bound; see C-13.
4. **Type.** Invalid counting argument, caught by checking what class contains the entire subcube.
5. **Next attempt.** Do not count a set's complement as sparse unless its complement is actually included in the counted class. Any stronger dual argument must use a property of the gap/high points inside the cube, not merely their absence from $Y$.

## Selector self-reference by iterative patching stops in the gap

1. **Attempt.** Given an adaptive anti-checker selector $A$ and a small circuit $D$, repeatedly overwrite the sample locations $A(f)$ with $D$'s labels. Hope for a high-complexity fixed point that contradicts selector correctness.
2. **Valid implication.** Hamming distance to $D$ strictly decreases at every stage where $CC(f)>s_2$. The process terminates at a table $f_*$ whose selected labels agree with $D$; hence $CC(f_*)\le s_2$.
3. **Exact failure.** The promise gap allows $s_1<CC(f_*)\le s_2$. Even from a start above $2s_2$, the required $\Omega(s_2/n)$ edits are fewer than the selector's batch length $t=2^{10\beta n}$, so a single round can cross the boundary. One-at-a-time updates yield a long trajectory but no circuit lower bound.
4. **Classification.** Fundamental gap in this construction, not a technical omission. Any repair must force the endpoint below $s_1$ or derive an independent contradiction from the trajectory. The selector guarantee only activates above $s_2$.
5. **Lesson.** Self-reference needs a fixed point inside the promised hard region; a monotone potential that terminates outside the guarantee is not diagonalization.

## Random sparse supports as a selector lower-bound family

1. **Attempt.** Use the exponentially large sample range forced by C-18, together with random weight-$s_2$ supports, to argue that anti-checker selection must be computationally difficult.
2. **Exact failure.** For almost every support $R$, there is a fixed $Q_0$ of $O(\log M_1)$ coordinates hitting the 1-set of every low circuit with density above $1/2$, while no low circuit of density at most $1/2$ contains all of $R$. Also $R\cap Q_0=\varnothing$ with high probability. Then $R\cup Q_0$ is a valid anti-checker, and a sorting circuit outputs it in $O(Nn^3)$ size.
3. **Type.** The random sparse family is an easy distributional subdomain. This does not refute a worst-case selector lower bound: exceptional high-complexity supports may lie inside sparse low-circuit sets.
4. **Next attempt.** Attack structured supports whose positives are contained in a sparse low-circuit 1-set. Prove that any successful selector must identify such a low-density superset or construct a short hitting set for its residual zeros. Do not infer circuit size from range size or positive-point capture.

## Axis-aligned subcubes as hard sparse regions

1. **Attempt.** Place random positive supports inside a low-density subcube, so the fixed set $Q_0$ from C-23 misses the containing circuit's sparse 1-set.
2. **Exact failure.** With $w=K s_2$ random positives inside a sample-sized subcube $A$, counting gives high global circuit complexity and rules out every size-$s_1$ circuit matching the full pattern on $A$. The positive support reveals $A$ as its coordinatewise hull with probability $1-o(1)$, so a sorting circuit outputs $A$ itself as an anti-checker in $O(Nn^3)$ size (C-24).
3. **Type.** This is another easy distributional subdomain, not a refutation of worst-case selector hardness.
4. **Next attempt.** The low-density region must resist recovery from simple statistics of its positive support, including coordinate hulls. A proposed hard region should be attacked with direct recovery strategies before lower-bound arguments are developed.

## Robust affine sketches and single-circuit fixed points

**Attempt.** Replace full truth-table processing by a short linear sketch, then decode the anti-checker addresses from the sketch. In parallel, seek a self-reference theorem forcing some high table to match the constant-zero circuit at its selected queries.

**Result.** C-36 refutes every robust affine-sketch selector under $N-t-k>\log M_2$: conditioning on a sketch value and setting the selected labels to zero leaves $2^{N-|Q|-k}>M_2$ completions, including a high table. The fixed-point shortcut is false for one circuit: the rule “query the first 1-bit” has no nonzero input whose queried label is zero.

**Failure type.** Architecture-specific obstruction and counterexample to an overbroad fixed-point premise; neither is a universal selector lower bound. The affine argument does not handle nonlinear feedback. A fixed-point argument must range over all low-circuit traces and preserve high complexity, not just force one label.

**Next change.** Study conditional fibers of the address map. A valid selector must make every fiber with a low-circuit query trace contain at most $M_2$ tables. Seek a quantitative circuit lower bound for this property, and adversarially test it against selectors whose addresses depend on the queried bits.

**Additional stress test (C-39).** A linear-size priority encoder outputs the first 1 and first 0 positions, anti-checking both constant circuits on every nonconstant table. Thus the constant-zero fixed-point obstruction is too narrow to force superlinear size; the lower bound must capture simultaneous avoidance of all small-circuit traces.

## One-counterexample-at-a-time anti-checker search (C-45)

1. **Attempt.** Repeatedly find a size-$s$ circuit agreeing with $f$ on the current list, scan the truth table for a disagreement, and add that coordinate.
2. **What is proved.** On the high-complexity promise, each round removes at least the selected circuit, so the procedure terminates after at most $|\mathcal C_s|=2^{O(s\log s)}$ rounds. C-40's dual margin proves a random sample of $O(\log|\mathcal C_s|)$ points exists.
3. **Exact failure.** The basic NP witness (a surviving circuit) gives no guarantee that the selected counterexample removes a useful fraction of the residual version space. In an abstract set system, error sets $E_i=H\cup\{p_i\}$ have a one-point transversal from the common set $H$, yet an adversarial black-box response can return a private point $p_i$ and take $m$ rounds. This is a failure of the black-box greedy route, not a lower bound for explicit circuit families or for all algorithms.
4. **Next change.** Seek a circuit-specific balancing potential or a direct deterministic transversal construction. The obvious potential counts weighted surviving circuits; no theorem proves approximate counting necessary, and no #P-hardness claim is made.

## Generic flattening of KPT's adaptive anti-checker witnesses

1. **Attempt.** Replace the existential anti-checker family in the Pich–Santhanam route by KPT's finite list of polynomial-time witness functions, then collapse the adaptive dependence to one selector.
2. **Exact failure.** The $i$-th function can depend on earlier challenge strings, including satisfying assignments. Feeding it the output of a hypothesized SAT circuit only gives a semantically useful challenge when that circuit is correct; it does not give an $S^1_2$ proof of correctness. Expanding over all possible $n$-bit witnesses costs $2^n$ branches in the generic construction, not polynomial overhead.
3. **Type.** This refutes the naive flattening, not every possible KPT-based construction. The Pich–Santhanam paper itself records the adaptive-witness obstruction; no impossibility theorem for all collapses is known here.
4. **Next attempt.** Find a witness-independent invariant of the KPT transcript, a polynomial-size strategy-composition theorem, or a direct $S^1_2$ selector. Any claimed route must still address EF non-p-boundedness and yield a statement not equivalent to the circuit lower bound being sought.


## Essential-input counting does not reach the magnification exponent (C-34)

**Attempt.** Use the anti-checker promise to force every valid selector to inspect many truth-table coordinates, then convert dependency count into gate count.

**Result.** Adversarial completion proves that the selector must depend on at least $N-t-\log_2M_2-O(1)=N-o(N)$ inputs. The original incidence count gave $(1/2-o(1))N$ gates, but C-38's graph-connectivity count sharpens the consequence to $N-o(N)$ gates.

**Exact failure.** An $O(N)$-gate circuit can depend on all N input bits and can share intermediate summaries among every output. The sharpened $N-o(N)$ bound remains linear and contains no superlinear information.

**What a successor must do differently.** Lower-bound the routing from $f$ to its query labels, including how summaries are selected and shared. Do not repeat dependency, sensitivity, or output-entropy counts unless paired with a theorem that charges the shared computation.

## Sparse-distinguisher amplification after selector routing (C-49)

**Attempt.** Strengthen the anti-checker from a one-error transversal to a robust code-distance certificate, then apply sparse distinguishers to amplify its trace gap.

**What is proved.** Local correction of r points costs O(nr) gates. Every valid query trace is therefore Omega(s1/n)-far from the traces of size-s1/2 circuits. A minimax-length list has relative distance Omega(1/n^2); for a selector output of q queries the general relative bound is only Omega(s1/(nq)). Sparse distinguishers can amplify either gap after the query set has been selected.

**Exact failure.** The distinguisher transforms labels on an already selected Q_f; it provides no lower bound for computing f -> Q_f. At fixed OPS beta, the generic count of low-circuit tables gives 2^(O(N^beta)), which does not establish the 2^(N^(o(1))) sparsity condition for general formula magnification. The uniform MCSP theorem's conditional conclusion is P != NP^{oplus P}; the formula lower-bound conclusion does not rule out polynomial circuits for NP. Thus this does not yield P != NP or move O-1.

**Classification and lesson.** The robust-certificate lemma is a proved universal invariant; the attempted transfer is closed at the current parameter/model mismatch. Future work must attack arbitrary routing itself or provide a new theorem linking robust puncturing complexity to unrestricted circuit size.

## Unique-marker reduction using a few almost-disjoint circuit errors (C-50)

**Attempt.** Encode a hard search problem in one coordinate that every valid anti-checker must query, using a fixed small family of low circuits whose disagreement sets share only that marker and otherwise have disjoint private regions.

**Exact failure.** For any fixed odd family of $k$ low circuits, their majority has size $O(k s_1+k^2)$. If the majority disagrees with high $f$ on only a constant-size marker (or fewer than $\Omega(s_2/n)$ points), patching those points computes $f$ with at most $s_2$ gates. More generally, C-50 forces a majority-error region of size $\Omega(s_2/n)$ and a large pairwise error-set overlap. The proposed unique marker cannot be the only majority-error location.

**What remains possible.** This rules out only the simple fixed-family construction. A reduction might use a growing family with complex overlap geometry, but it must maintain high circuit complexity and prevent a short alternative transversal. No such construction is currently known here.

## C-48 — Exact #P scores are not the selector bottleneck

**Attempt.** Treat exact counting of surviving circuits as the central obstruction to constructing the C-45 greedy anti-checker.

**What survived.** The greedy potential and C-47's FP$^{\#P}$ implementation are correct, but exact counts are unnecessary for constant-fraction contraction. Relative approximate counts suffice. Under $NP\subseteq P/poly$, Stockmeyer approximate counting on the short transcript yields the known $N^{1+O(\beta)}$ conditional selector.

**Why the proposed conclusion fails.** No proof shows an arbitrary valid selector must follow this greedy algorithm, approximate the score, or encode the same potential. Lower-bounding this implementation alone would not establish O-1. This is a scope failure, not evidence that the count itself is easy unconditionally.

**Future constraint.** Target the universal puncturing-certificate map directly, or first prove a size-preserving reduction from every selector to the score computation. Do not assert #P-hardness/necessity without such a reduction.

## Majority moments do not force large average circuit distance

**Attempt.** Use C-50 for tuples of $k=\Theta(n)$ low circuits to show that a uniformly random low-circuit function must disagree with a high table on a constant fraction of coordinates on average.

**Calculation.** If $p_x$ is the fraction of low circuits wrong at $x$ and $r=(k+1)/2$, then a random $k$-tuple majority is wrong at $x$ with probability at most $2^k p_x^r$. The C-50 region lower bound yields $\sum_x p_x^r\ge h/2^k$.

**Exact failure.** The power-mean inequality does not convert this lower bound on the r-th moment into a lower bound on $\sum_xp_x$; the inequality gives the opposite direction for the desired conclusion. A vector supported on $h$ coordinates satisfies the moment constraint with first moment only $h$. At most one obtains $\max_xp_x\ge(h/(N2^k))^{1/r}$, already weaker than the constant-fraction coordinate implied by C-40's dual margin.

**Type and lesson.** Invalid strengthening, caught before being entered as a theorem. Do not use majority moments to claim average distance or a stronger dual margin without an additional distributional premise.

## A global marginal sample does not finish adaptive selection (C-52 audit)

A sample of O(n) descriptions estimates every root marginal to constant accuracy, and an O(Nn)-gate circuit finds a first query eliminating a constant fraction. Reusing one global sample fails as a proof method once the survivor mass is below the additive error scale: the empirical version space can be empty while the exact one is nonempty.

Uniform convergence tracks residual and next-query events through depth k with O((kn+log(1/eta))/delta^2) samples at additive error delta. Conditional scoring at survivor mass rho needs delta=O(rho). This closes only the generic global-sample extension. No rare-cell reachability claim is established.


## C-53 correction - the adaptive sample bound is inverse-linear, not inverse-square

The first audit used additive Hoeffding for every numerator and denominator, giving a sufficient sample size proportional to $1/\rho^2$. That is not the strongest analysis. For the finite family of transcript ranges, multiplicative Chernoff plus a cutoff at $\lambda=\gamma\rho/8$ gives relative error on all masses at least $\lambda$ and suppresses the empirical frequency of smaller error events. The resulting sample size is $O((kn+\log(1/\eta))/(\gamma\rho))$ and still guarantees a constant-fraction query whenever the residual mass is at least $\rho$.

This corrects the quantitative bound but not the conclusion: the sample may miss nonempty residuals below $\rho$. To guarantee all nonempty residuals generically, the threshold must reach $1/|\mathcal H|$, which makes this sample-based implementation superpolynomial. No impossibility claim for arbitrary selector circuits follows.


## C-54 - Polynomial-threshold sampling has a nonempty handoff

The range-sampling argument can be implemented for $O(n)$ rounds with $N^{1+a}\operatorname{poly}(n)$ gates when tracking residual mass down to $N^{-a}$. But every $O(n)$-query transcript has a low-circuit DNF interpolant of size $O(n^2)$. Consequently the first residual below the sampling threshold is nonempty, and the output prefix is not a complete anti-checker.

This is a closed limitation of the inverse-polynomial-threshold sample guarantee. Do not claim the sample selector cannot continue by another mechanism: its query budget allows $\Omega(s_1/n)$ or more points, and this result gives no lower bound on routing cost.
# O-1 witness-selector attacks checked — 25 September 2026

## Global sampling past inverse-polynomial residual mass

Relative Chernoff sampling improves the global-sample cost to inverse-linear in residual mass, but exact termination requires a description-scale sample. DNF interpolation proves the C-54 cutoff is reached at a nonempty residual after only $O(n)$ rounds. This kills the global sampled-greedy continuation as a near-linear full selector; it does not lower-bound arbitrary selectors. See C-52–54.

## LP / ellipsoid construction of the separating distribution

The minimax dual gives a coordinate distribution separating every low circuit from a high table. The standard ellipsoid route needs a separation oracle that finds a low circuit minimizing weighted disagreement. This is weighted circuit fitting, so the proposed construction hides a major search problem in the oracle. It is not an independent constructive proof.

## Direct selector diagonalization

The attempt to answer every queried point according to one fixed low circuit is circular when future query addresses depend on unassigned truth-table bits. A self-consistent high completion of $f|_{Q(f)}=D|_{Q(f)}$ has not been proved. Priority selection defeats the simple constant-circuit version. The missing fixed-point theorem would itself need to handle arbitrary selectors.

## Output-counting / entropy shortcut

C-56 shows validity depends only on $f|_Q$. A valid trace has $2^{N-|Q|}$ extensions, almost all high at OPS parameters. Thus a short output list can be shared by huge numbers of high tables; counting outputs or output bits does not yield a selector circuit lower bound. The actual input-dependent routing remains open.

## Local patch encoding and direct Kannan transfer (C-58--C-60)

**Attempt.** Encode source bits by modifying a high base table on address regions, and argue that every valid anti-checker output must query those regions; then decode the source from the returned addresses or labels. A second version tries to transfer Kannan's fixed-exponent second-level lower bound to the selector relation.

**Exact failure.** If a valid base list $Q_0$ misses the patch, every modified table agreeing with the base on $Q_0$ retains $Q_0$ as a valid list (C-58). If instead the construction provides, for each decoded bit, a small circuit agreeing with the high table outside a simple, disjoint bit-region, two such circuits and a mux compute the whole table in $2s_1+\mathrm{poly}(n)$ size (C-59). Also, “every valid list of length at most $t$ hits $P$” does not imply there is a low-circuit disagreement set contained in $P$; the hypergraph with edges $\{p,x_i\}$ is a counterexample. Kannan's language can vary with exponent $k$, and a reduction blowup $m\mapsto m^{a_k}$ may erase the exponent gap (C-60).

**Classification.** This closes the common-list / easy-decodable localized-patch gadget and the naive Kannan inference. It is not a fundamental impossibility result for all search reductions and gives no selector or Gap-MCSP lower bound.

**What a successor must do.** Invalidate every common base witness, survive the patch-switch lemma, handle the bounded-length transversal caveat, preserve high circuit complexity for both source answers, and give all-valid-output decoding with controlled exponent blowup. Otherwise attack the selector or O-1 directly without a hardness-transfer gadget.

**C-61 refinement.** Even when localized low approximants are absent, a reduction cannot force every short valid list to touch many pairwise-disjoint source regions: each such mandatory region consumes at least $(3/10-o(1))$ of one dual-margin distribution, so there are at most three. This rules out another region-coded gadget class. It does not rule out overlapping regions or information carried by correlations among many queried addresses.

## Parity padding does not force independent dual-mass changes (C-62 stress test)

**Attempt.** Amplify C-62 by padding a hard source input x with r switch bits z and replacing its answer by L(x) XOR parity(z). Since every z-edge flips the answer, hope to force r independent dual-mass changes in the encoded truth table.

**Counterconstruction against that inference.** If A_x and B_x are two high-table encodings with output-distinguishable valid-list sets, define F(x,z)=A_x when parity(z)=0 and F(x,z)=B_x when parity(z)=1. Every z-edge has the same difference support P(A_x,B_x); C-62's edge condition can be met by this one shared change, with no r-way disjointness. Computing parity costs O(r) gates in the source-to-table circuit.

**Scope.** This is not a complete reduction: constructing A_x,B_x with the high promise, all-output decoding, and controlled exponent remains open. It shows that C-62's pairwise separation alone cannot be summed over source coordinates. An additive lower bound needs an extra independence or bounded-overlap theorem that defeats shared parity encoding.
## Generic agreement-fiber anti-concentration is false

**Attempt.** After rewriting selector failure as finding a high table in a low-circuit agreement fiber, consider proving a generic theorem that every short selector has some hard member in one of those fibers, using only the size of the concept class and the witness-length bound.

**Counterexample.** Let the domain have N points and the low class consist of the two constant functions. On every nonconstant target, select one address labeled 0 and one labeled 1. This is a valid anti-checker; a priority encoder computes it with O(N) gates. The agreement fiber for constant 0 is exactly the constant-zero table, and similarly for constant 1. Neither fiber contains a hard target relative to any threshold above constants.

**Exact lesson.** The agreement-fiber reformulation does not itself yield a lower bound. A proof must use closure and richness specific to the full size-s1 circuit class, not merely finite-class cardinality, minimax margin, or query budget. This is a counterexample to the class-generic route, not to S-1 for circuit-size classes.
## Fixing one low circuit does not challenge a selector

A proposed adversary that fixes a low table D and argues the selector must find where f differs from D cannot force a superlinear bound. Hardwire D and use a priority encoder to output the first differing truth-table coordinate; this takes O(N) gates. A fixed menu of m low tables is handled with O(mN) gates by outputting one mismatch for each. Thus lower bounds must address the full input-dependent family of low circuits, not one or a small fixed menu. See C-64.
### Direct Rect-DL transfer (C-173)
A rect-DAG leaf cover induces a multi-output rectangle list, but the list-size measure is at most 2N for mismatch by the trivial signed-coordinate cover. Rect-DL's 2025 alternation hierarchy counts output-value switches, not protocol owner switches. A list-to-protocol simulation also cannot merge the two parties' failed membership tests for A x B, since (A^c x Y) union (A x B^c) is nonrectangular. Retired as a direct superlinear route; retain only the possible forced-output-projection question O-132.

### Forced-output Rect-DL size route (C-174)
For any forced Boolean projection h of a mismatch output, the induced 1-set is the union of at most 2N signed mismatch rectangles. Hence Rect-DL length is at most 2N, which cannot reach the superlinear transfer target. Sign-only and coordinate-block-only projections have even simpler structure. Retired as a decision-list-size route; direct DAG lower bounds are not ruled out.

### Raw conflict-cylinder summation (C-175)
At a DAG state, the high tables in C_v are excluded from B_v, but the same high table may be excluded from many off-path states. The C-80 block router gives m=Theta(s1/n) such states in an O(N)-vertex DAG, each with nearly all high columns excluded. Therefore summing |Z\\B_v| cannot lower-bound graph size. Any salvage needs a path-conditioned or parent-conditional potential.

### C-176 - Standalone path-weighted cross-conflict charge
The candidate charge at a reached Bob split counts when the selected child’s high column lies in the sibling’s descendant conflict set. It is safely path-conditioned and at most the path length, but it is not forced: in the C-80 router choose a low block-constant row and a high table mixed on every block, with the first two bits of block 1 opposite that row. A high such table exists by counting more than M2 candidates. The router selects the mixed block and immediately finds the first mismatch; the table avoids both sibling conflict sets. Thus this charge can be zero on a valid pair. Retired as a standalone lower-bound potential; do not infer that all path-weighted potentials fail.

### C-177 - CLKM local-PRG transfer to C-75
The gap promise version of the local-PRG contradiction is valid: a generator with outputs in SIZE(s1) is accepted everywhere by H, while H accepts at most M2/2^N of uniform tables. But the known generator for size-S general branching programs has locality S^(1/2)2^(O(sqrt(log S))), implying only S>=N^(2beta-o(1)). This is below the N-o(N) rect-DAG bound for beta<1/2, and the standard branching-program model is not the C-75 unrestricted circuit-equivalent rect-DAG. Retire as a transfer route; retain the general-circuit local-PRG formulation as Q133.


### C-178 - Naive universal-circuit elimination of the description
A universal evaluator computes V(d,x), but the separator needs to classify x after existentially quantifying over d. The direct OR of equality tests for every size-s1 circuit description costs N*2^(O(N^beta)) at OPS parameters, far above polynomial size. Sending d gives short communication but an exponential one-switch frontier, already ruled out as a compact DAG architecture by C-170. This closes only direct enumeration and one-switch evaluation; it does not rule out a compressed existential projection or a genuinely alternating rect-DAG. Any stronger non-shareability claim is a lower bound on residual separator complexity and must be proved.



### C-179 - One-shot affine parity sketches cannot be short
Fix low row w. If a linear or affine sketch has the property that every high table gets a different sketch value from w, its entire collision coset around w must lie inside SIZE(s2). That coset has size 2^(N-rank), so rank is at least N-log2|SIZE(s2)|=N-o(N). This extends the coordinate-sampling obstruction to arbitrary per-row parity tests. It only kills one-shot affine fingerprints; it says nothing about adaptive nonlinear routing or about a DAG that uses collisions to continue.



### C-180 - Adaptive parity trees give only a depth bound
An adaptive affine-parity decision tree separator has depth at least N-log2(M2), because the leaf cell of a low table is an affine subspace that contains no high tables. This closes only shallow parity decision trees. A DAG can merge paths and still have depth N-o(N) in O(N) nodes, so the bound does not reach shared rect-DAG size.



### C-181 - Stronger BP local PRGs do not reach small beta
The STACS 2021 local PRG with locality S^(2/3+o(1)) extends C-177's acceptance-versus-uniform argument to a gap promise and yields only S>=N^(3beta/2-o(1)). For every beta<1/2 this is below N^(3/4), hence weaker than the existing N-o(N) DAG floor. The read-once co-nondeterministic HSG needs about sqrt(N) locality. Both models are restricted branching programs; no transfer to the arbitrary separator circuit/rect-DAG is known. Keep the result as a parameter audit, not a target lower bound.

