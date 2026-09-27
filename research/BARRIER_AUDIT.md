# Barrier audit

## Representation independence and nonuniformity

The active theorem targets arbitrary Boolean circuit separators, not one solver architecture. A polynomial-time SAT decider induces polynomial-size circuits, and the fusion theorem connects those circuits to the project cover measure. Nonuniform advice is included.

For the exact family conversion, restrict the separator to Gamma=Y union Z, express input bits and negations as the 2N generators, and translate AND gates to intersections. Constants can be formed from complementary literals with O(1) overhead. The argument does not assume a witness, search tree, or preferred encoding.

## Natural proofs

The magnification implication is published, but this does not show that a proposed proof of its premise avoids every natural-proofs obstacle. Test largeness, constructivity, and PRG usefulness against the actual property on N-bit truth tables. Do not dismiss or endorse a proof solely by labeling it natural.

## Relativization and algebrization

The near-linear leaf bound is combinatorial and relativizing in spirit; it does not establish the superlinear theorem. Any candidate that treats an oracle as a literal generator or changes only the input encoding should be tested against oracle worlds. No oracle-resistant ingredient for O-1 is currently identified.

## Proof complexity

The semi-filter closure is an explicit refutation process, but the target is a circuit lower bound, not a lower bound in a fixed proof system. A proof-search or proof-length argument needs a size-preserving bridge to arbitrary circuits; none is currently available.

## Advice, preprocessing, sharing, and recomputation

The measure includes nonuniform circuits and arbitrary DAG sharing through the intersection-complexity theorem. Recomputing rather than storing does not evade a circuit-size lower bound. A proof that counts only proof-DAG leaves, one decomposition, or a selected filter family does not account for alternative circuit computations.

## Uniformity and promise parameters

Gap-MCSP is a promise problem. Use Gamma=Y union Z or prove the chosen totalization is legitimate. Track n=log N, fixed beta, s1=2^(beta n)/(c n), and s2=2^(beta n) separately. Magnification quantifies over every sufficiently small fixed beta; one parameter sequence is insufficient.

## Current outcome

No known barrier refutes the route, and no new ingredient crosses the central lower-bound barrier. The exact missing statement is a slightly superlinear lower bound against arbitrary circuit separators; the cover route's superlinear \(\rho\) target is a stronger sufficient condition, not a necessary one.

The OPS paper explains that its magnification theorem is based on efficiently constructing anti-checkers from the assumption \(\mathrm{NP}\subseteq\mathrm{P/poly}\). Chen et al.'s locality barrier shows why direct lifts of some existing weak lower-bound techniques can fail: the magnified problem may have small circuits with local oracle gates, while those lower-bound techniques also handle such gates. A candidate route therefore needs a genuinely nonlocal invariant or a lower-bound model that escapes the local-oracle simulation. This does not prove that all methods are blocked.

The low-anchor coordinate trace gives \(D(Y\mid\mathcal B)\ge N-o(N)\). A proposed complementary \(2N-o(N)\) bound was withdrawn because its high-anchor subcube could contain gap and high tables. The corrected interpolation argument gives only \(\rho(Z)=\Omega(N^\beta/n^2)\), which does not improve the leading bound. This diagnoses the current coordinate charge; it does not show that every acyclic invariant stops at \(N\).

## Anti-checker existence versus synthesis

Finite minimax and sampling already give short anti-checkers for each hard truth table. This is compatible with the fixed-sample counterexample because the equilibrium distribution depends on the table. A proof that merely improves the existential support size does not address the OPS barrier. The unresolved object is the map from the full truth table to a valid support, with a quantitative circuit-size lower bound.

For a proposed support, anti-checking is coNP-verifiable; extending a partial list is in $\Sigma_2^P$. Under $P=NP$ this becomes polynomial-time searchable, but the polynomial degree has no reason to be near one in the truth-table length. OPS's conditional near-linear selector uses stronger nonuniform approximate counting. This is a parameter barrier, not a quantifier contradiction.

## Sparse hard-support caveat

C-23 gives a near-linear selector on almost every uniformly random weight-$s_2$ table. Thus the sparse-support counting argument C-18 cannot by itself imply a lower bound on selector circuits. The remaining sparse worst cases are supports inside sparse low-circuit regions; outputting all positives and a fixed hitting set does not handle their low-density supersets. Any claimed lower bound must address those cases rather than a typical random support.

## Separate 2025 uniform magnification result

Atserias and Müller prove a uniform MCSP approximation magnification theorem whose lower-bound premise implies $P\ne NP^{\oplus P}$. This is a real alternative target and avoids the specific nonuniform selector, but that class separation is not currently a proof of $P\ne NP$. Keep the route separate unless a valid implication between the classes is established.


## Near-total input dependence does not charge routing

C-34/C-38 are representation independent: any valid selector depends on $N-o(N)$ inputs and, by the circuit-graph connectivity count, needs at least $N-o(N)$ fan-in-two gates. This is still only linear because a bounded-fan-in circuit can aggregate information from all inputs in linear size. A candidate invariant must measure how addresses and labels are routed so every small circuit is hit. Do not present sensitivity or dependency count as a superlinear obstruction.

C-35/C-36 sharpen the distributional and representation audit. A fixed sample is valid on almost every uniformly random table, so average-case success does not control worst-case exceptions. Every robust affine sketch of dimension $k=o(N)$ also fails as an address mechanism, even with an unrestricted decoder. This is not a lower bound against arbitrary circuits: nonlinear address feedback can correlate selected coordinates with sketch fibers. Any claimed extension must bound this feedback without assuming a selector architecture.

C-38 raises the universal fan-in-two selector lower bound to $N-o(N)$ gates, but C-39's priority encoder meets the linear scale for the two constant hypotheses. Thus the connectivity bound is essentially sharp for simple classes. A superlinear proof must exploit simultaneous avoidance of the full exponentially large low-circuit class, not merely input dependence or positive/negative witness selection.

C-51 converts the majority-error lemma into a dense graph of pairs of low-circuit functions that err together on many inputs. This is representation independent, but the induced max-score contraction is weaker than the dual-margin result, and an abstract common-core class has the same overlap property with a constant-size selector. Counting distinct functions may be harder than #P counting circuit descriptions. Therefore the statistic does not constrain arbitrary routing without an additional property using the full circuit class on actual hard tables.

The June 2026 Goldberg–Juvekar–Kabanets result proves conditional NP-hardness for gap ImpMCSP and full-support learning under subexponential iO and proof-system assumptions. It works with sampler-described instances and does not yield the explicit OPS Gap-MCSP lower bound unconditionally. It is a conditional hard-instance-generation precedent, not a way around the current model or assumption gap; details are in [the continued reassessment](REASSESSMENT_2026-09-25_CONTINUED.md).

## Dual-witness route audit (C-40)

The minimax margin and random-support argument apply to the full circuit class and do not assume a solver representation. They are, however, existence statements. The direct fractional LP has an NP separation oracle (weighted circuit fitting), and exact integral-list validity is coNP; generic list search is a $\Sigma_2^P$ relation. This does not cross a barrier or imply a lower bound. It shows where an algorithmic construction would use computational power and why replacing the selector by an existential theorem is insufficient. The margin threshold is itself a reformulation of the Gap-MCSP promise, so using it as a new invariant would be circular.

C-41 adds an adversarial sparse support against any sufficiently small menu of fixed distributions. This is still a distribution-menu restriction, not a circuit lower bound: an arbitrary selector can choose its distribution as a nonlinear function of the whole truth table. The claim is only that a data-independent prior strategy cannot be universal.

## New formal-language claims

C-42's Loop-theoretic P-vs-NP manuscript is conditional in its own abstract on an internal capacity principle and explicit bridges back to classical complexity. Until those bridges are proved from the standard machine model with polynomial resource preservation, an internal theorem does not constrain arbitrary P algorithms. The full PDF was inaccessible in this audit, so exact axiom types remain open.

## Quantifier collapse is not quantitative circuit collapse (C-44)

Under P=NP, the polynomial hierarchy collapses to P, so the $\Sigma_2^P$ relation for finding an anti-checker list becomes polynomial-time searchable on promised high tables. This yields some polynomial circuit family, but its degree is unrestricted. The OPS magnification theorem requires a specific near-linear $N^{1+\epsilon}$ bound; class collapse by itself gives no exponent control. This separates a decision-class implication from the resource-preserving bridge actually needed.

## Approximate counting reconstructs the conditional selector, not a lower bound (C-48)

The version-space potential can be optimized by relative approximate counts, not exact #P values. Stockmeyer places the approximation in BPP$^{NP}$; under $NP\subseteq P/poly$, the short-transcript approximation has deterministic polynomial-size circuits after amplification and nonuniform fixing of random bits. Parallel evaluation over all $N$ candidate points and $O(s\log(s+n))$ rounds gives the familiar $N^{1+O(\beta)}$ selector. This is consistent with the OPS magnification argument and confirms that the score is an implementation choice. No lower bound for that chosen implementation constrains selectors using a different computation. Any proof must lower-bound the universal puncturing-certificate map directly or prove a representation-independent reduction to score computation.


## C-52 - Global marginals solve only the first query

A constant-error coordinate exists against the entire low-circuit description set and can be found for every high table by hardwiring an O(n)-sample marginal profile; the selector uses O(Nn) gates. Thus the first greedy point does not inherently require #P counting.

The profile is not a conditional sample. For a residual cell of mass r, conditional frequencies divide joint frequencies by r; a global additive approximation only gives constant relative accuracy while r is above its error scale. An empty empirical version space does not certify that the true one is empty. This is a limitation of this sampling architecture only; arbitrary selectors may avoid these scores.


## C-53 - Relative sampling sharpens but does not close the tail

A multiplicative Chernoff argument over all transcript ranges needs only $O((kn+\log(1/\eta))/(\gamma\rho))$ samples to preserve constant-fraction elimination while residual mass is at least $\rho$. This is better than the inverse-square bound from additive approximation and lets a polynomial-size sample track inverse-polynomial cells.

A surviving description may have mass $1/|\mathcal H|$. At that scale the sample requirement depends on the full description space, which is superpolynomial in $N$ here. The result rules out only the obvious global-sample completion. It neither proves any particular rare cell is reached nor constrains selectors that do not follow this construction.


## C-54 - The sampled prefix stops before interpolation runs out

For any $q=O(n)$ transcript, a DNF on the queried positive points matches all labels using $O(qn)=O(n^2)$ gates, which is below $s_1$ eventually. Therefore no such transcript is an anti-checker. Relative sampling with inverse-polynomial threshold certifies only $O(n)$ constant-contraction rounds, so its guarantee ends while a small consistent circuit is still known to exist. The remaining gap to $\Omega(s_1/n)$ queries is specific to this greedy sample method; it does not imply a circuit lower bound for arbitrary selectors.


## C-55 through C-57 - Witness totality, routing, and output length

Minimax proves a short external teaching set pointwise, but its coNP validity relation does not have a generic small circuit Skolemization. The existential greedy strategy uses exact residual counts; this is an implementation barrier, not evidence that every selector must count. The trace-cylinder lemma shows why output counting is weak: a valid trace is shared by $2^{N-q}$ completions, almost all high at OPS parameters. The external teaching-set length is only pinned between $\Omega(s_1/n)$ and $O(s_1\log(s_1+n))$; shrinking this interval does not by itself bound the circuit that routes $f$ to a valid trace. No standard learning-theory hardness transfers without a reduction for this outside-class, nonminimal, succinct-circuit setting.

## Search-reduction and decoder audit (C-58--C-60)

A reduction to anti-checker selection must handle every valid output, not only the output of a chosen selector. Local changes outside one valid base list leave that list valid (C-58). A proposed repair using one easy-recognizable block per source bit also fails if each omitted-bit approximation is low-circuit and correct off its own disjoint block: two approximants plus a mux compute the high table in $2s_1+\mathrm{poly}(n)$ size (C-59).

This does not establish that every short list forced through a region yields a low-circuit disagreement set contained in that region. The bounded-length hypergraph counterexample in C-59 blocks that inference. Any successful transfer must give a different all-output mechanism and separately prove the high-table promise and resource preservation.

Kannan's theorem leaves both a quantifier gap (the hard language can depend on fixed exponent $k$) and a resource gap. If table generation and output decoding have circuit exponents $b_k,d_k$, table blowup $N=m^{a_k}$ gives composed exponent $e_k=\max\{a_k(1+\epsilon),b_k,d_k\}$. A contradiction requires $k>e_k$, while also ensuring high tables and all-output decoding (C-60). No such reduction is established.

C-61 supplies an additional semantic limit on region-based reductions: with the same dual witness for one high table, each region mandatory for all lists up to $t$ must absorb nearly $3/10$ of its mass. Thus there can be at most three disjoint mandatory regions. This does not limit arbitrary all-output decoders; a region may be nonmandatory while output correlations still encode information.
