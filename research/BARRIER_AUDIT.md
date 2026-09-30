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

The circuit-to-communication simulation for C-404 charges at most one bit per crossing wire, which is valid under arbitrary fanout but yields only `O(N)` from any cut. Its random-quotient construction also gives a near-full-dimensional all-promised restriction whose many YES points form a simple subspace; the induced label is easy. Thus neither high communication on one cut nor restriction dimension/anchor count resolves the locality issue. Chen et al. exhibit small oracle-augmented circuits for specified magnification frontiers and show that certain weak-model lower-bound methods extend to those oracle gates. Their paper also records an OPS Gap-MCSP local-oracle implementation. This is a technique-specific locality barrier, not a universal impossibility theorem. C-404 neither analyzes the oracle model nor establishes a nonlocal invariant; its cut argument is closed at linear scale. A 2026 gate-elimination preprint gives constructive refuters for selected fixed functions (XOR, MUX, affine dispersers), but no construction that preserves the Gap-MCSP promise on every restriction. Treat that as a technique lead only. Full audit: [C-404](C404_CUT_TRANSCRIPT_CAPACITY_AND_PROMISE_RESTRICTIONS_2026-09-30.md); [Chen et al.](https://doi.org/10.1145/3538391); [Carmosino, Dang, Jackman](https://arxiv.org/abs/2604.23958).

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

## C-401 ordinary-circuit shared-readout audit

The priority reset is to the exact OPS total-gate target: N=2^n, s1=N^beta/(c log_2 N), s2=N^beta; a fixed epsilon must work for all sufficiently small fixed beta. The theorem states universal c and its proof instantiates 10. Local inconsistency/incidence cannot charge gates because unrestricted fanout compresses all prefix parities from Theta(N^2) expanded incidence to O(N) gates. Parity, repeated equality, sparse parity checks, and simple global block relations are also O(N). The full syndrome circuit size B(H) accounts for sharing, but the missing theorem is a representation-independent reduction from every one-bit promise separator to that entire readout. The alternative scalar zero-test of a low-contained subspace has only 2^(O(N^(1+beta))) ambient candidates, so counting cannot give a fixed exponent when beta is smaller than epsilon. No such reduction or ordinary superlinear bound is established. Exact low-circuit enumeration is a valid full-promise separator of O(N*2^(O(N^beta))) gates, not near-linear. The OPS and locality-barrier sources are linked in C-401; the latter blocks certain direct technique lifts and is not a universal impossibility theorem. Native q remains N-o(N). See research/C401_SHARED_READOUT_CHARGE_AND_ORDINARY_GATES_2026-09-29.md.

## C-402 promise-aware subfunction obstruction

Partial restriction incompatibility can be stated exactly: the conflict graph on outside-block contexts has chromatic number no larger than the number of restrictions induced by any total separator. But this statistic cannot reach the OPS exponent: there are only `2^(O(N^beta))` low tables, so every block has log chromatic number `O(N^beta)` and every partition's sum is `O(N^(1+beta))`. Further, unrestricted DAG sharing breaks additive charging even on total functions. Indirect storage access has `Theta(m^2/log m)` summed subfunction counts and an `O(m)` ordinary circuit, implemented by cascaded multiplexers. The classic Nechiporuk method is supported by disjoint block-labeled leaves/nodes in formulas and branching programs; Gal-Robere describe the overlap obstruction in general circuits and use model-specific wire/gate structure for comparator circuits. Their comparator-wire result does not transfer to ordinary total gates. The partial-promise coloring lemma is retained; additive profile charging is closed. No OPS, near-linear full-promise, or native-q improvement. See `research/C402_PROMISE_SUBFUNCTION_CHARGE_AND_DAG_SHARING_2026-09-30.md`, [Gal-Robere](https://eccc.weizmann.ac.il/report/2019/128/download/), and [Uhlig](https://doi.org/10.1007/3-540-54458-5_84).

## C-403 - accepted-subcube counting gives only a linear gate floor

The set of tables with complexity below `s2=N^beta` has size at most `2^(O(N^beta log N))`. Every separator accepts the all-zero table; if it ignored more than `O(N^beta log N)` coordinates, varying them would give an accepted subcube containing a high table. Thus at least `N-O(N^beta log N)` input coordinates are essential. The connected fan-in-two ancestor DAG then has at least one fewer gate than essential input sources. This proves `S>=N-O(N^beta log N)-1`, or `(1-o(1))N` for fixed beta<1. It is stronger than a support count alone because it charges each essential source through the circuit graph, but its ceiling is still linear. A binary-addition threshold for support weight is an O(N)-gate separator for the sparse low subpromise only; parity shows the YES family is not covered. No ordinary OPS exponent, full-promise near-linear construction, or native-q improvement. See `research/C403_ACCEPTED_SUBCUBE_DIMENSION_LINEAR_GATE_FLOOR_2026-09-30.md`.



## C-405 - cryptographic preimage charge versus locality barrier

The hard-core preimage construction gives a conditional lower bound on the ordinary circuit for one sampler-defined total function, with explicit composition cost `S+|P|+O(1)`. It is not a local-oracle lower-bound technique. The Chen et al. locality barrier concerns particular magnification frontiers where Q has efficient circuits augmented with small-fanin oracles and shows why several existing weak-model techniques extend to those oracles. It is not a universal impossibility theorem for ordinary total-gate lower bounds. The implicit-MCSP NP-hardness in TR26-091 is conditional and representation-level-specific; its polynomial sampler description does not provide an OPS-compatible explicit table reduction. C-405's mechanism has no current OPS transfer and does not alter the barrier audit. Sources: [Chen et al.](https://doi.org/10.1145/3538391), [Goldberg-Juvekar-Kabanets TR26-091](https://eccc.weizmann.ac.il/report/2026/091/download/).

## C-406 - formula-to-DAG unfolding audit

OPS Theorem 5 formula hardness transfers to the exact OPS promise for every fixed `beta<alpha/2`, because the theorem's YES threshold `n^d` is below `N^beta/(cn)` and its NO threshold `N^(alpha/2-o(1))` is above `N^beta`. A circuit with cycle rank `mu` unfolds to at most `2S2^mu` formula leaves, forcing `mu=Omega(logN)` for a near-linear separator. This is a project-level structural consequence and yields `S>=E(C)+gamma log_2 N-O(1)` for fixed `beta<1/2`, `gamma<1-2 beta`; it adds a logarithmic gate surplus but is not a superlinear lower bound, and the main `N-O(N^beta logN)` order remains. Cavalar�Oliveira (ECCC TR25-033) note that best known lower bounds for explicit unrestricted single-output Boolean functions remain linear with basis-dependent constant at most five; that is context, not a formal barrier for promise separators. Chen et al.'s locality barrier remains technique-specific. Sources and full parameter proof: `research/C406_CYCLE_RANK_FORMULA_TRANSFER_2026-09-30.md`, OPS Theorems 4�5, and [Cavalar�Oliveira](https://eccc.weizmann.ac.il/report/2025/033/download).


## C-407 - Random coordinate restriction is an easy induced promise

C-407 proves that a random coordinate support P of size N^gamma, beta<gamma<1-2beta/5, has an induced Gap-MCSP promise separable by an O(N^gamma log^2N)-gate Hamming-weight threshold. Circuit counting bounds the weight of all low tables supported on P; minterm circuits force high tables to have larger weight. This retires this coordinate-restriction route to hard traces, but says nothing about dense low tables or nonlinear promise-preserving maps. Murray-Williams' local-reduction results and gate-elimination refuters for explicit total functions are adjacent literature, not barriers to the general project. Sources: OPS https://theoryofcomputing.org/articles/v017a011/v017a011.pdf ; Murray-Williams https://theoryofcomputing.org/articles/v013a004/ ; Carmosino-Dang-Jackman https://arxiv.org/abs/2604.23958 . Full argument: research/C407_RANDOM_SUPPORT_RESTRICTION_COUNTERCONSTRUCTION_2026-09-30.md.

## C-408 - Restriction entropy is not a full-promise work charge

The random balanced-block calculation proves an easy induced trace, not hardness: every low table on the selected block-constant slice is near a constant, and the complete slice promise has an `O(m log^2m)` separator. It therefore supplies no challenge to unrestricted sharing in a full MCSP separator. This is distinct from the hardness-magnification locality barrier. Chen et al. (arXiv:1911.08297) show that several known lower-bound methods localize to circuits with small-fan-in, arbitrarily powerful oracle gates, while magnification reductions can expose such local oracles; Pich (arXiv:2212.09285) further proves localizability for broad uses of the approximation method. These are technique barriers, not a theorem that all MCSP lower-bound approaches fail. C-408 neither applies nor bypasses them. C-406 uses a cited formula lower bound and a structural DAG-unfolding transfer but only yields `Omega(log N)` cycle rank and an additive `O(log N)` gate surplus, consistent with the barrier. OPS's exact Theorem 1.4 threshold remains `N^beta/(c n)` versus `N^beta`, with one fixed epsilon and every sufficiently small fixed beta; the proof uses denominator `10n`. No ordinary, native, or P-vs-NP frontier changes. Detailed audit: `research/C408_RANDOM_BLOCK_SUBSPACE_TRACE_2026-09-30.md`.

## C-409 - Full-table PRF security is a conditional natural-property obstruction

The C-409 proof is a direct distributional argument: if a separator accepts all truth tables generated by a low-complexity PRF but rejects almost every uniform table, it distinguishes the PRF from random. Cheraghchi et al.'s local-PRG framework already uses exactly this low-output/pseudorandomness template to obtain MCSP lower bounds in restricted circuit models; C-409 specializes it to the general-circuit OPS gap under an assumed security level. Natural-proofs reasoning explains why such an efficient property conflicts with sufficiently secure PRFs; it does not construct that security. A key of `k=n^2` only aligns the size scales (`N^(1+epsilon)=2^((1+epsilon)sqrt{k})`), and an alpha>1/2 subexponential security hypothesis is stronger than standard polynomial security. No new unconditional method or lower bound results. Sources: Cheraghchi et al., ICALP 2019 local PRG paper; OPS Theorem 1.4; Chen et al. on locality. Full audit: `research/C409_FULL_TABLE_PSEUDORANDOMNESS_CONDITIONAL_GAPMCSP_2026-09-30.md`.

## C-410 - Locality and query-readout boundary

C-410 is a general shared-circuit compiler, not a lower bound: sorting N table records together with q adaptive-query outputs and propagating values through the sorted stream costs O((N+q)log^3(N+q)) gates. It removes the proof's separate O(qN) formatter charge at OPS parameters. This is consistent with the locality barrier: work charged to separate local query projections may be shared globally. Separately, the exact static Anti-Checker Hypothesis from OPS is refuted by Chen et al., Theorem 59/Corollary 61, through an oracle-formula locality lower bound. That refutation is route-specific and does not establish an unrestricted ordinary-circuit lower bound or refute the adaptive OPS anti-checker construction. No natural-proofs or locality barrier is bypassed by C-410; no P-vs-NP frontier changes.

## C-411 - Parameterized locality limit for static anti-checker menus

If a fixed anti-checker menu uses L=N^(2-delta) sets of size q=N^(kappa beta) at OPS high threshold N^beta, the induced AND of Succinct-MCSP oracles has SIZE3 at most N^(2-delta+3*kappa beta+o(1)). Chen et al.'s Theorem 59 forbids it when delta>(3*kappa+2)*beta, by choosing epsilon_loc between 2 beta and delta-3 kappa beta and alpha=epsilon_loc/beta. At kappa=10, constant-saving menus are excluded for sufficiently small beta. This is a parameter extension of the published static-AH refutation, not a general circuit lower bound. It leaves the adaptive OPS selector and ordinary total-gate target open. Proof: research/C411_TARGET_SCALE_STATIC_ANTICHECKER_MENU_LOCALITY_OBSTRUCTION_2026-09-30.md.

## C-412 - Local-flatness is not a locality-barrier result or a gate charge

The patch-ball inclusion B_r(C_{s1/2}) subset h^{-1}(1) subset C_{<s2} is an exact ordinary-promise constraint, but it does not show that a separator is a local computation or belongs to a small-fan-in-oracle model. The O(N)-gate sparse threshold is a restricted-subpromise counterexample to charging local neighborhoods, not a full separator. Chen et al. locality is technique-specific and does not decide this direct total-gate route. C-411's static-menu theorem remains separate. No new locality theorem or lower bound is claimed; see C412_LOW_CIRCUIT_PATCH_BALLS_NO_GATE_CHARGE_2026-09-30.md and the primary sources cited there.

## C-413 - Oracle lookup sharing and exact magnification mismatch

A sort/scan/restore compiler serves Q nonadaptive queries to a fixed K-entry Boolean table in O((Q+K)polylog(Q+K)) ordinary total gates, and d oracle layers add a factor d. This explicitly captures sharing; it is an upper compiler, not a universal lower bound. Random lookup tables require Omega(K/log K) gates by ordinary circuit counting, but C-413 does not show a Gap-MCSP separator computes such a lookup. Ilango's random-oracle reduction is relativized at the target circuit measure and has a constant-factor gap near M/log M. OPS needs the ratio s2/s1=10 log M. Therefore this transfer misses both standard-model and quantitative requirements. Neither OPS's ordinary total-gate lower bound nor the locality barrier is resolved; Chen et al.'s theorem still applies only to its specified oracle/locality methods. Details: research/C413_BATCHED_LOOKUP_CHARGE_FAILS_TO_TRANSFER_TO_OPS_2026-09-30.md.

## C-414 - Output support limits lookup reductions before the separator

If one or t promised N-bit tables are generated from a K-bit indexed source and a postprocessor that may inspect the generated tables and separator outputs, but no raw source bits, returns A_i, then K<=tN+2R where R counts all fan-in-two encoder gates. The composite MUX requires R+tS+B>=K-1. With sublinear-in-K encoder and postprocessor costs, source width per separator call is at most N(1+o(1)); if source width per call is superlinear, the encoder is already Omega(K). Thus the straightforward query-entropy reduction cannot charge a superlinear cost to the separator alone. This is a source-input support theorem, not a barrier against other encodings. OPS's theorem and Chen et al.'s locality theorem are unchanged; the latter still does not constrain arbitrary separators. Full proof: research/C414_PROMISE_EMBEDDING_SUPPORT_CAPACITY_NO_GO_2026-09-30.md.

## C-415 - Exact-extension reductions need exponential no-case hardness

For `M=2^d` table inputs, OPS needs no-case output complexity at least `2^(beta*d)`. The 2026 f-Simple-Extension framework tests exact size `CC(f)+m` and a restriction key; its negative label alone yields no exponential circuit lower bound. The explicit `OR_r(x) OR PARITY_m(y)` construction for `m>=r+2` is a nonmember with a key and all inputs essential, but its circuit size is `O(d)`, so it is a promise-YES table. More generally, adjoining U+6 parity variables to any explicit U-gate nondegenerate base gives a negative extension of O(d) size. Naive OR-products/MUX composition preserve polynomial-in-arity circuit upper bounds. This blocks only the exact-label transfer and naive product amplification; MUX's simple-extension complexity and other total reductions remain open. No OPS lower-bound or locality-barrier consequence follows. Full proof: `research/C415_SIMPLE_EXTENSION_GAP_AMPLIFICATION_FAILS_2026-09-30.md`.
## C-416 - Completion entropy is not a locality or gate lower bound

Circuit counting gives |Low_s1|<=2^(O(M^beta)) at OPS parameters. A partial table with u stars, completed uniformly, hits Low with probability at most 2^(O(M^beta)-u); a general sampler with min-entropy h has bound |Low|2^-h. This is an elementary sampler limitation. It fails to control source-aware correlations: parity, repeated-block tables, sparse parity-check families, and tables assembled from a small seed and a simple suffix relation can all be generated as Low outputs from low-entropy samplers. The argument does not derive a lower bound on any separator gate, does not construct a localized oracle computation, and neither bypasses nor strengthens Chen et al.'s technique-specific locality barrier. The partial f-SEP* predicate asks for some exact simple extension and is not itself an OPS low-completion promise. No ordinary, native, or quantitative P-vs-NP frontier changes. Full analysis: research/C416_PARTIAL_TABLE_COMPLETION_ENTROPY_LIMIT_2026-09-30.md.

## C-417 - Output routing is a model interface, not a locality-barrier bypass

The bitwise/multi-output tradeoff is ordinary circuit accounting. A single-output table generator of R gates gives each fixed table circuit size at most R, but the direct separator composition costs S+MR. A multi-output generator composes at S+R, but the standard gate-only multi-output definition allows designated outputs to be input wires or gate outputs; its M output choices may carry a long router description. Ilango, Loff, and Oliveira explicitly study gate-size circuit minimization for multi-output total functions, including the output-component convention. C-417's two-gate low/high routed example is not an OPS reduction and not a new theorem about that problem. It neither uses localized oracle gates nor bypasses/strengthens Chen et al.'s technique-specific locality barrier. The ordinary OPS exponent and native rho frontiers are unchanged. Sources and exact costs: research/C417_PAIRED_FAMILY_OUTPUT_MODEL_TRADEOFF_2026-09-30.md.

## C-418 - Stronger block-trace avoidance does not imply a hardness transfer

C-418 union-bounds against circuits below OPS `s2`, not only below `s1`. For every fixed `beta<1` and `gamma<1-beta`, it obtains `q=Theta(M^gamma)` blocks such that every nonconstant repeated-block table is High. The induced promise remains easy: equality of the `q` representative bits is decided in `O(q)` gates, and a source map through `R` shared block values has label complexity at most `R+O(q)`. This is a stronger restriction lemma and an explicit counterexample to treating repetition or high output complexity as work forced on a full separator. It is not a general lower-bound method, does not challenge the known locality barrier for specified approximation/local-oracle methods, and makes no native-fusion claim. The full-promise target and all quantitative frontiers remain unchanged. Report: research/C418_HIGH_TRACE_RANDOM_BLOCKS_STILL_EASY_2026-09-30.md.


## C-419 - Balanced-block traces are easy at every fixed dimension

Combining C-418 for `gamma<=beta` with C-408 for `gamma>beta` proves that, for every fixed OPS-small `beta<1/2` and every fixed block exponent `gamma in (0,1)`, some balanced partition has an exact induced-promise selector of `O(M^gamma log^2 M)` gates. The proof handles the actual `s1=M^beta/(10d), s2=M^beta` thresholds and arbitrary sharing; the resulting selector is small because the block pattern promise is simple. This closes the balanced-block restriction family as a hard-trace route, not as a full-promise lower bound. Parity is outside the slice. The locality barrier remains technique-specific and is neither bypassed nor contradicted; native fusion is not analyzed. No numeric frontier changes. Report: `research/C419_ALL_BLOCK_DIMENSIONS_HAVE_EASY_TRACES_2026-09-30.md`.

## C-420 - Codeword embedding failure and the exact OPS target

C-420's random codeword-hard subspace is compatible with the OPS thresholds but its induced promise is trivial zero testing: `W\{0}` is all High and `0^N` is Low, so `NOR_N` separates it. For a hard kernel-membership source, this forces the shared table generator—not the separator—to pay the source lower bound up to `O(N)`. This is a reduction accounting no-go, not an implication of the locality barrier. The linear-sketch obstruction is exact but limited: rank below `N-O(N^beta log N)` produces a kernel collision between zero and a High table. Neither result constrains arbitrary nonlinear full-promise separators. OPS Theorem 1.4 has one fixed epsilon for every sufficiently small fixed beta, low threshold `2^(beta n)/(c n)` with universal c (proof uses 10), and high threshold `2^(beta n)`; its general-circuit size is total fan-in-two gates. Chen et al.'s locality barrier remains technique-specific. No frontier changes. Report: `research/C420_CODEWORD_HARD_TRACES_DO_NOT_CHARGE_THE_MAP_2026-09-30.md`.

## C-421 - A real separator supplies a certificate, not a compact selector

The reverse proof-DAG extraction is an unconditional ordinary-circuit statement: every High input has a mask of at most `min(N,2S)` coordinates that fixes the separator's output to 0; therefore no Low circuit agrees on that set. Its gate cost is O(S) with shared gates marked once. This avoids assuming a description output or address-wise algorithm, but the mask may have N positions and does not meet OPS's `N^(10 beta)` list length for small beta. Shrinking it while preserving C=0 on every completion is Sigma2^P search because fixed-mask validity is coNP. The OPS anti-checker list only excludes Low circuits; C's arbitrary acceptance on middle tables can force a larger zero-certificate. Parity shows generic certificate width N is possible with O(N) gates. The result neither bypasses nor strengthens the locality barrier and changes no quantitative frontier. See C-421.

## C-422 - Anti-checker existence versus computation

The OPS parameterized game has a constant fractional disagreement value for every High table: if a distribution over Low circuits predicted all N addresses with error below 1/4, a majority of O(n) sampled circuits would compute the High table using fewer than s2 fan-in-two gates. Minimax and an O(log |Low|)=O(N^beta) sample yield a short anti-checker. This is the established Lipton-Young theorem in OPS gate parameters; it is per-input existence, not an efficiently computed selector and not a lower bound on a Gap-MCSP separator.

C-421's separator certificate is stronger semantically (it forces C=0 on every completion) but may have N coordinates. C-422's short anti-checker only excludes Low completions; middle-band completions may still be accepted by C. No bridge from an arbitrary separator's shared evaluation DAG to the fractional strategy was proved. OPS Lemma 4.1 constructs a larger N^(10 beta) list conditionally under NP subseteq P/poly; the locality barrier in Chen et al. remains technique-specific and is not contradicted or bypassed. Ordinary total-gate and native fusion frontiers are unchanged. See research/C422_FRACTIONAL_ANTICHECKERS_DO_NOT_CHARGE_SEPARATOR_GATES_2026-09-30.md, Lipton-Young (https://www.cs.ucr.edu/~neal/Lipton94Simple.pdf), OPS (https://theoryofcomputing.org/articles/v017a011/), and Chen et al. (https://eccc.weizmann.ac.il/report/2019/168/).
## C-423 - Boundary-pivot idea is not a locality-barrier result

The first-acceptance pivot test tries to extract a selector from the separator's global path behavior and makes no short-oracle-query assumption. Its failure is an explicit sparse two-branch counterexample to a generic entropy/distance lemma, not a Gap-MCSP counterexample; the rejected reference is Low. Thus it neither bypasses nor strengthens the published locality barrier. The paired linear-sketch attempt is blocked by a kernel-counting argument at rank `N-O(N^beta log N)` (more precisely `N-O(N^beta n)`), while nonlinear full-promise separation remains open. OPS Theorem 1.4 retains one fixed epsilon for all sufficiently small fixed beta. Full proof and exact caveats: `research/C423_BOUNDARY_PIVOTS_MISS_LOW_TABLES_2026-09-30.md`.
## C-424 - Local pivot counterexample now has an actual High table

C-424 embeds a counting-hard function on a simple truth-table address subcube, making f OPS-High by restriction. A linear-size filter accepts an exponential selected family of Low tables plus a marker singleton and rejects all High tables globally. Uniform first-acceptance pivots still miss the exceptional Low table with probability o(1). The filter's sole failure is completeness over the full Low class. This rules out using local endpoints, f's actual high complexity, and high-side soundness alone to prove a pivot theorem; it does not rule out a theorem exploiting full promise completeness. The locality barrier is neither bypassed nor contradicted. C-424 also converts soundness into accepting-cube width `N-O(N^beta log N)`, but a separated Low code and raw certificate counting yield only a sublinear gate bound. Full source and proof: `research/C424_HIGH_TABLE_PIVOT_FAILURE_AND_COMPLETENESS_BARRIER_2026-09-30.md`.