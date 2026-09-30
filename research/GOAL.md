## Current priority - 30 September 2026 (C-424 continuation)

Keep the unconditional ordinary OPS total-gate target primary: `N=2^n`, YES `CC<=N^beta/(c n)`, NO `CC>=N^beta`, with one fixed epsilon>0 for every sufficiently small fixed beta>0. C-424 retires the local first-pivot selector: even an actual High table and an O(N)-gate filter sound on every High input admit an exponentially weighted low endpoint family whose pivot misses a special Low table with probability o(1). The filter fails full Low completeness. A certificate-cover proof gives accepting cubes with at most O(N^beta n) free coordinates, but raw cube counting yields only a sublinear gate bound. The new target is a shared-DAG charge for covering every Low table by sound certificates, paired with an attempt to construct such a complete cover near-linearly. Do not assume certificate cubes are disjoint or charge their occurrences separately. Test parity, repeated-block equality, sparse parity checks, and global relations. Exact full-promise enumeration remains O(N*2^(O(N^beta))); ordinary lower frontier remains N-O(N^beta log N)-1 plus C-406's additive refinement; OPS N^(1+epsilon) remains open; native rho>=N-o(N) remains separate. Use fusion only if a proved advantage transfers. Full C-424 proof: research/C424_HIGH_TABLE_PIVOT_FAILURE_AND_COMPLETENESS_BARRIER_2026-09-30.md.
## Previous priority - 30 September 2026 (C-419 continuation)

Keep the unconditional ordinary OPS total-gate target primary: for `M=2^d`, YES `CC<=M^beta/(10d)`, NO `CC>=M^beta`, with one fixed `epsilon>0` for every sufficiently small fixed `beta>0`. C-419 combines C-408 and C-418 to close every fixed balanced-block dimension exponent: for each `0<beta<1/2` and `0<gamma<1`, some partition into `q=Theta(M^gamma)` equal blocks has an exact induced-promise separator of `O(q log^2 q)=M^(gamma+o(1))` gates. If `gamma<=beta`, C-418 makes every nonconstant block pattern High, so testing equality costs `O(q)`; if `gamma>beta`, C-408 gives a Hamming-threshold separator. This retires equal-block restrictions across the full dimension range as a hard-trace route; parity remains outside the slice. It is not a full-promise separator or lower bound. Continue paired maps only for non-block-constant images whose source label is hard after all shared signals are exposed. Keep gates, wires, description bits, uniform output time, and native fusion resources distinct. The full-promise exact separator remains `O(M*2^(O(M^beta)))`; the ordinary lower frontier remains `M-O(M^beta log M)-1` plus C-406's additive logarithmic refinement; OPS `M^(1+epsilon)` remains open; native `rho>=M-o(M)` is separate. Full report: `research/C419_ALL_BLOCK_DIMENSIONS_HAVE_EASY_TRACES_2026-09-30.md`.

## Previous priority - 30 September 2026 (C-415 continuation)

Keep the unconditional ordinary OPS total-gate target primary: for a d-variable truth table of length `M=2^d`, YES `CC<=2^(beta*d)/(10d)`, NO `CC>=2^(beta*d)`, and one fixed `epsilon>0` must rule out `M^(1+epsilon)` gates for every sufficiently small fixed `beta>0`. C-415 uses the 2026 f-Simple-Extension literature as a new reduction route, then closes the naive exact-label transfer: `f(x)=OR_r(x)`, `g(x,y)=OR_r(x) OR PARITY_m(y)` for `m>=r+2` is nondegenerate, has key `0^m`, and has `CC(g)>=3(m-1)>r-1+m=CC(f)+m` but `CC(g)=O(r+m)`. Thus it is a negative simple-extension instance yet still below OPS's exponential-in-d low threshold. More generally, any nondegenerate explicit base `f` with circuit upper bound U has a negative extension `f OR PARITY_(U+6)` of O(d) total circuit size. OR-products of k copies remain O(km) gates on km variables and do not amplify to OPS NO. Do not equate structural nonmembership or a one-gate excess with the OPS high threshold; the next useful route needs a promise-preserving construction whose every NO output has `2^(beta*d)` circuit complexity. Full report: `research/C415_SIMPLE_EXTENSION_GAP_AMPLIFICATION_FAILS_2026-09-30.md`.

## Previous priority - 30 September 2026 (C-414 continuation)

Keep the unconditional ordinary OPS total-gate target primary: `N=2^n`, YES `CC<=N^beta/(c n)`, NO `CC>=N^beta`, with one fixed `epsilon>0` ruling out `N^(1+epsilon)` gates for every sufficiently small fixed `beta>0`; the proof uses denominator `10n`, so the gap ratio is `10n`. C-414 proves support-capacity bounds for single- and multiple-instance indexed-lookup reductions. For `t` promised `N`-bit tables generated with `R` gates and read by `t` separator calls plus a `B`-gate postprocessor that may inspect generated tables and separator outputs, but receives no raw source bits outside the encoder, computing an arbitrary `K`-bit indexed source readout forces `K<=tN+2R` and `R+tS+B>=K-1`. Thus this route cannot force superlinear per-call `S` from source MUX complexity when the source width fits the aggregate table width; when it exceeds that width, the encoder bears `Omega(K)` gates. Opposite-promise tables differ in `Theta(N^beta/n)` coordinates, but parity replication shows this distance does not charge independent gates. Seek a distinct index-free encoding or a direct invariant of an arbitrary one-bit separator; do not repeat per-incidence, neighborhood, static-menu, or arbitrary-lookup counting. The ordinary frontier remains `N-O(N^beta log N)-1` plus C-406's additive logarithmic refinement; OPS `N^(1+epsilon)` remains open; native `rho>=N-o(N)`; full-promise enumeration remains `O(N 2^(O(N^beta)))`. Full cycle: `research/C414_PROMISE_EMBEDDING_SUPPORT_CAPACITY_NO_GO_2026-09-30.md`.

## Previous priority - 30 September 2026 (C-413 continuation)

Keep the unconditional ordinary OPS total-gate target primary: `N=2^n`, YES `CC<=N^beta/(c n)`, NO `CC>=N^beta`, with one fixed `epsilon>0` ruling out `N^(1+epsilon)` gates for every sufficiently small fixed `beta>0`; the proof uses denominator `10n`, so the gap ratio is `10n`. C-413 proves the exact batch-lookup compiler and random-lookup lower bound, but fails to force an arbitrary separator to compute such a lookup on a promise-preserving embedding. The random-oracle MCSP reduction also has oracle-relative witness circuits and only a constant-factor gap around `M/log M`. Do not repeat local-volume, query-incidence, or static-menu charges; seek an index-free promise embedding or a direct invariant of the separator's one-bit function. Keep the ordinary frontier `N-O(N^beta log N)-1` plus C-406's additive logarithmic refinement, OPS `N^(1+epsilon)` open, and native `rho>=N-o(N)`. The full-promise upper is still `O(N 2^(O(N^beta)))`. Full cycle: `research/C413_BATCHED_LOOKUP_CHARGE_FAILS_TO_TRANSFER_TO_OPS_2026-09-30.md`.

## Previous priority - 30 September 2026 (C-412 continuation)

Keep the unconditional ordinary OPS total-gate target primary: at N=2^n, YES CC<=N^beta/(c n), NO CC>=N^beta, and seek one fixed epsilon>0 that rules out N^(1+epsilon)-gate separators for every sufficiently small fixed beta>0 (Theorem 1.4; the proof uses denominator 10n). C-412 proves that each sufficiently small low table has a Hamming ball of radius Theta(N^beta/n^2) that every separator must accept. The local-flatness mechanism gives no gate charge: one gate can have a huge input fiber, and an O(N)-gate threshold recognizes a large sparse YES subfamily and its forced neighborhoods while rejecting every NO table. Retire neighborhood/derivative counts as a standalone route; exploit the full circuit-generated anchor family only if a new ordinary-gate theorem can be proved. C-411 rules out a fixed anti-checker menu only in its stated locality parameter range, not adaptive selectors or arbitrary separators. Do not assume a separator outputs a witness. C-410 rules out per-address mux charging. The ordinary frontier remains N-O(N^beta log N)-1 plus C-406's additive logarithmic refinement; OPS N^(1+epsilon) remains open; native rho>=N-o(N). Full C-412 proof: research/C412_LOW_CIRCUIT_PATCH_BALLS_NO_GATE_CHARGE_2026-09-30.md.

## Previous priority - 30 September 2026 (C-411 continuation)

Keep the unconditional ordinary OPS total-gate target primary: at `N=2^n`, YES `CC<=N^beta/(c n)`, NO `CC>=N^beta`, prove one fixed `epsilon>0` rules out size `N^(1+epsilon)` separators for every sufficiently small fixed `beta>0` (Theorem 1.4; concrete proof denominator `10n`). C-410 removes a false per-address charge: `q` arbitrary truth-table queries can be read in `O((N+q)log^3(N+q))` gates. C-411 uses the published locality theorem to rule out static target-scale anti-checker menus whenever the menu saving `delta>(3*kappa+2)*beta` for sets of size `N^(kappa beta)`; for the OPS `kappa=10`, a constant menu saving is impossible for sufficiently small beta. This does not rule out adaptive selectors or arbitrary separators. Continue with a direct total-gate invariant or a proved bridge from decision to adaptive selector; do not revive static menus or assume a separator outputs a witness. C-409 remains conditional only.

Continue seeking an unconditional shared-work invariant or a full-promise separator. The random support and balanced-block restrictions are closed; C-406 cycle rank yields only logarithmic extra gates. Keep exact costs distinct: total Boolean gates, wires, circuit description, runtime, and native `rho`/paid-AND/OR/endpoint/cycle measures. Full-promise enumeration remains `O(N*2^(O(N^beta)))`. **No numeric frontier change:** ordinary `N-O(N^beta log N)-1` plus C-406's additive refinement; OPS `N^(1+epsilon)` open; native `rho>=N-o(N)`. Full conditional proof, attacks, and literature comparison: `research/C409_FULL_TABLE_PSEUDORANDOMNESS_CONDITIONAL_GAPMCSP_2026-09-30.md`.

## Prior priority - 30 September 2026 (C-408 continuation)

The primary mathematical target is the ordinary total-gate premise in OPS Theorem 1.4: for the universal constant `c` and thresholds `s1=N^beta/(c n)`, `s2=N^beta`, prove there is one fixed `epsilon>0` such that every sufficiently small fixed `beta>0` requires more than `N^(1+epsilon)` fan-in-two gates. OPS's proof gives the concrete denominator `10n`; its promise convention is YES at complexity `<=s1` and NO at complexity `>=s2` (strict `>s2` is equivalent when `s2` is nonintegral; our C-408 proof in fact rejects every table of complexity `>=s2`). See Theorem 1.4 in the primary source.

C-408 closes random balanced block-constant restrictions as a way to produce hard traces: an `m=N^(gamma+o(1))` dimensional block slice has a complete induced-promise threshold separator of `O(m log^2m)` gates. Its counting mechanism controls which low truth tables can lie on that slice, but it gives no charge to a full-promise circuit; the restricted label itself is cheap. C-406 gate-graph cycle rank remains the only currently proved explicit sharing-control mechanism, and its exact output is an additive `Omega(log N)` reconvergence/gate refinement, not a superlinear gate bound. Do not sharpen either route without a new theorem connecting it to full-promise total work.

Pair each direct full-promise lower-bound attempt with a separator construction handling every promised YES and NO table. Keep gates, wires, circuit-description bits, runtime, native paid AND states, OR operations, semantic endpoints, and cyclic closure separate. Treat parity, repeated-block equality, sparse parity-check systems, and simple global block relations as active cheap-sharing countertests. A lower-bound construction must identify which of them it includes or excludes and prove why its computation charge survives unrestricted reuse. **Current numeric frontier unchanged:** ordinary `S>=N-O(N^beta log N)-1`, with C-406's additive `E(C)+gamma log_2N-O(1)` refinement; OPS exponent target open; native `rho_GapMCSP>=N-o(N)`; exact low-circuit enumeration costs `O(N*2^(O(N^beta)))`. C-408 report: `research/C408_RANDOM_BLOCK_SUBSPACE_TRACE_2026-09-30.md`.

## Prior priority - 30 September 2026 (C-407 continuation)

Keep the exact OPS ordinary total-gate target primary. C-407 closes random coordinate-support restrictions as a route to a hard promised trace: for every fixed `beta<1/2`, a subspace of dimension `N^gamma` for `beta<gamma<1-2beta/5` has an `O(N^gamma log^2 N)` threshold separator for its entire induced low/high promise. The proof counts small circuits whose support lies in a random coordinate set and uses minterm cost to separate low from high; this is project-specific and nonuniform in the chosen support. It does not touch the full promise because dense low tables such as parity lie outside the slice. Do not repeat sparse-support restrictions. Next pursue either a genuinely nonlinear promise-preserving trace with a proved hard label, or a direct all-low/full-high separator argument; pair the attempt with an upper-bound construction that handles every promised table. The full-promise enumeration upper remains `O(N*2^(O(N^beta)))`, leading ordinary lower bound `N-O(N^beta log N)` with C-406's additive `E(C)+gamma log_2 N-O(1)` refinement, OPS exponent target open, and native `rho>=N-o(N)` unchanged. Report: `research/C407_RANDOM_SUPPORT_RESTRICTION_COUNTERCONSTRUCTION_2026-09-30.md`.

## Previous priority - 30 September 2026 (C-406 continuation)

Keep the ordinary OPS total-gate target primary with exact thresholds `s1=N^beta/(c log_2 N)`, `s2=N^beta`, one fixed epsilon, and every sufficiently small fixed beta. C-406 tests whether formula lower bounds can control unrestricted sharing. The cycle-rank unfolding theorem is valid: `S` gates and gate-to-gate cycle rank `mu` (primary-input occurrences split as leaves) give a formula with at most `2S2^mu` leaves; OPS Theorem 5 therefore forces `mu=Omega(log N)` for any near-linear separator in the contained parameter range. This is a genuine structural constraint and strengthens the gate count to `S>=E(C)+gamma log_2 N-O(1)` for every fixed `beta<1/2` and `gamma<1-2 beta`. It leaves the main `N-O(N^beta log N)` asymptotic floor and OPS exponent target unchanged. Retire cycle rank as a standalone route to the OPS exponent. The next attempt must charge computation on all low anchors in a way that exceeds this entropy slack, or produce a full-promise near-linear separator; do not return to survivor counting or single-anchor Hamming balls without a new transfer. Full cycle: `research/C406_CYCLE_RANK_FORMULA_TRANSFER_2026-09-30.md`.
# Goal and standards

## Prior record - 30 September 2026 (C-405 continuation)

Keep the unconditional ordinary OPS total-gate target primary: for `M=2^d`, the proof's concrete gap is YES `CC<=M^beta/(10d)` versus NO `CC>=M^beta`, and requires one fixed `epsilon>0` for every sufficiently small fixed `beta>0`. C-416 proves a min-entropy ceiling for filling a partial table at random: the low-table count is `2^(O(M^beta))`, so a completion sampler with min-entropy `h` reaches Low with probability at most `2^(O(M^beta)-h)`. This rules out high-entropy random totalization when there are many stars, not correlated or source-aware samplers. Parity, repeated blocks, sparse parity checks and simple global block relations give explicit low-complexity counterconstructions. The entropy bound does not charge shared separator gates and does not directly apply to f-SEP*, whose existential extension predicate differs from low circuit complexity. The full-promise exact separator remains `O(M*2^(O(M^beta)))`; the ordinary lower frontier remains `M-O(M^beta log M)-1` plus C-406's additive logarithmic refinement; OPS `M^(1+epsilon)` remains open; native `rho>=M-o(M)` is separate. Next, attempt a deterministic paired-family embedding that maps a source hard bit to low versus provably OPS-high tables and prove the composition cost in ordinary fan-in-two gates. Reject quickly if the high-table lower bound cannot be established. Full cycle: `research/C416_PARTIAL_TABLE_COMPLETION_ENTROPY_LIMIT_2026-09-30.md`.

## Previous priority - 30 September 2026 (C-415 continuation)

Keep the ordinary OPS total-gate target primary with exact thresholds s1=N^beta/(c log_2 N), s2=N^beta, one fixed epsilon, and every sufficiently small fixed beta. C-405 tested hard-core preimage opacity as a share-aware mechanism: it proves a conditional lower bound for one sampler-defined function, but no all-promised map to explicit Gap-MCSP. For its 2m+1-bit domain, quantitative security must be 2^(delta m) to match table threshold 2^(beta(2m+1)), requiring beta<delta/2; subexponential 2^(m^alpha) hardness with alpha<1 is insufficient. The implicit-MCSP reductions have exponential-size truth-table outputs relative to their SAT source and therefore do not yield an OPS/P-poly contradiction. Change the next mechanism: investigate either (i) a polynomial-source-length explicit promise-preserving reduction with a hard label trace, or (ii) an ordinary full-promise separator exploiting shared circuit-description structure with a proved total-gate bound. Do not continue counting seed entropy, assume a non-shareability principle, or charge per-address inversion without proof. The direct full-promise separator remains O(N*2^(O(N^beta))); ordinary lower bound remains N-O(N^beta log N)-1; native rho remains N-o(N). Full cycle: research/C405_HARDCORE_PREIMAGE_READOUT_AND_IMPLICIT_TRANSFER_AUDIT_2026-09-30.md.

## Prior priority - 30 September 2026 (C-404 continuation)

Keep the ordinary OPS total-gate target primary. C-404 closes cut-transcript capacity at the linear scale and rules out short linear-fingerprint compression. Restriction composition is exact, but a random-subspace construction shows that even a near-full-dimensional all-promised slice with many low tables can induce only easy subspace membership; the encoder costs `O(N^(1+beta)log N)`, yet gives no separator lower bound. The next mechanism must force a hard non-subspace low trace while every other image point is high, or abandon restriction composition. Do not assume the induced label is hard or that the map is cheap. Keep testing actual near-linear full-promise separators. The C-403 `N-O(N^beta log N)` ordinary lower bound and native `rho>=N-o(N)` bound remain unchanged. Full cycle: [C-404](C404_CUT_TRANSCRIPT_CAPACITY_AND_PROMISE_RESTRICTIONS_2026-09-30.md).

## Prior priority - 30 September 2026 (C-403 continuation)

Primary target: ordinary total-gate lower bounds for Gap-MCSP via the exact Oliveiraâ€“Pichâ€“Santhanam magnification theorem. For `N=2^n`, low threshold `s1=N^beta/(c log N)`, and high threshold `s2=N^beta`, seek one fixed `epsilon>0` such that every sufficiently small fixed `beta>0` requires circuits larger than `N^(1+epsilon)`. C-403 proves every separator has `S>=N-O(N^beta log N)`, by bounding the accepted subcube dimension using the count of non-High tables and then charging all essential inputs through the connected fan-in-two ancestor DAG. This is a rigorous linear baseline, but the input-support mechanism is capped at N and cannot reach the target. C-402 separately closes additive block-subfunction charging. Continue with a distinct global feature that forces computation beyond merely using all input coordinates, preserving the all-separators and middle-band requirements; do not assume description reconstruction, witness enumeration, separate address checks, or retained caller history.

Keep fusion and cyclic closure as secondary tools only when they yield a specified advantage. Native q, paid AND count, OR operations, wires, semantic endpoint descriptions, total Boolean gates, and runtime remain separate. Native full-promise q is still `N-o(N)`; no near-linear full-promise cover or P-vs-NP proof is known. Preserve C-257/C-258/C-307/C-317 and later verified counterexamples.

Establish a rigorous proof of P = NP or P != NP. If a full resolution is not obtained, aim for a genuinely new theorem that materially reduces the unrestricted gap, with the exact remaining obstacle stated.

A result must specify its objects, quantifiers, computation model, resource bounds, uniformity, and assumptions. Every implication must be proved or cited precisely. Restricted-model results need an explicit transfer theorem before they can constrain arbitrary polynomial-time algorithms. Finite experiments may falsify claims or check implementations; they do not establish asymptotic statements. Do not call a result a breakthrough until it survives an adversarial proof audit.

## Prior route record (native fusion; secondary after C-401)

The O-153 and C-256 work orders below are historical. The current work order is the 29 September priority above, continued at C-384/Q230.

**Latest priority reset (user's attached instruction, 27 September 2026, after C-256):** return to the native cyclic fusion closure and make global sharing/readout complexity the primary route. The central hypothesis is that too much reuse among accepting derivations permits a cross-context splice that leaves `SIZE(s2)`, because the splice loses the requirement that the whole truth table come from one common small-circuit description. Work from the exact `C_i` certificate grammar and joint context/proof families, but attack their overlap and geometry rather than certificate width or raw counts. C-257 rules out a generic width/shattering/anchor-count splice argument. C-258 gives an explicit `O(N)` native cover for a repeated-block subfamily of `SIZE(s1)` against the actual high set; C-259 calibrates the multi-hole threshold at `Theta(n)`: `O(n)` prefix-selected size-`s1` cofactors are still patchable inside `SIZE(s2)`, while more than `C n` independent high-entropy slots would violate the `SIZE(s2)` count. The missing theorem is to force such slots or a hard ownership selector from the q-state grammar, or charge suppressing them to q. Continue O-153 as primary and the full-promise `N polylog N` / `N^(1+o(1))` native-cover construction as a counter-program. O-152's standard DAG route is secondary unless it yields a direct q-invariant or a near-lossless bridge. No P-vs-NP breakthrough has been obtained.

The overall proof target remains a Gap-MCSP lower bound with an explicit magnification transfer. Prioritize the weakest open theorem on native closure sharing, test near-linear constructions adversarially, state every quantitative loss, and record each failure's first broken implication.

C-222/C-223 close the fixed-menu repair and delimit explicit adaptive circuit selection. Do not resume that branch unless it yields a global product-hull charge or a near-linear separator.

**Current work order:** continue O-153 from C-260's paired proof/blocker antichains. The exact law is that the consistent output-certificate family is the context/proof join, and every such join is hit by every output blocker. A forced internal-state collision across exponentially many repeated-block low anchors follows from C-249 plus pigeonholing, but C-258 shows that this reuse can be protected by an equality fingerprint. The live missing step is a q-sensitive bound on the joint incidence geometry; the transversal identity alone gives no charge. Derive either `Theta(n)` independent high-entropy splice slots / a hard ownership selector or a superlinear suppression cost from q, never assume block isolation. In parallel, seriously try a near-linear native full-promise cover while preserving one circuit description across all address checks. Use C-257/C-258/C-259 as mandatory counterchecks. Keep the artificial multi-check code family as a diagnostic only until a superlinear native lower bound is proved. Literature review is secondary and only useful when it directly advances these proof obligations.

**Priority allocation:** about 50% native sharing/splicing proofs, 20% near-linear upper-bound construction, 15% artificial models, 10% amplification only after an `N g(N)` lower bound exists, and 5% directly relevant literature. Do not promote local width, certificate counts, or isolated state collisions as progress toward a superlinear bound.


C-191 is a historical checkpoint, not the current frontier. It proves a superpolynomial context requirement for the tail-only Q-forgetting recursion, but cross-signature Q-output exits block transfer to unrestricted Mis. C-194 later closes the inequality/equality-protocol lower-bound arm with a universal 4N-1-state inequality protocol; this is not a rect-DAG. The live task is still to charge cross-signature exits in the standard product-rectangle model or construct a compact rect-DAG for the full low/high promise. Continue O-141/Q134/Q138 with C-80/C-121 and C-160 as counterchecks. No arbitrary-DAG lower bound, near-linear construction for the full low class, or P-vs-NP breakthrough is known.


C-179 also closes one-shot affine fingerprints: any per-row parity sketch that separates w from all high tables needs rank N-log2|SIZE(s2)|=N-o(N). Continue with Q134's residual separator complexity and Q135's adaptive/nonlinear extensions; no arbitrary-DAG bound follows from C-179.


C-180 rules out shallow adaptive parity decision trees but not shared DAGs: its depth lower bound is only N-o(N), compatible with O(N) vertices. Continue to target residual separator complexity and the effect of merging affine or nonlinear contexts; restricted parity results have no transfer to arbitrary rect-DAGs.










Latest frontier C-195: C-194 gives a universal degree-two inequality protocol with 4N-1 triangle states, but C-195 proves that its top greater-than state needs at least 2^(Theta(N^beta/n^2)) product rectangles even on the actual OPS promise. This blocks direct statewise compilation, not every rect-DAG construction; the selected prefix/gap subpromise still has an O(N)-vertex scan DAG because all low suffixes are zero. The active target remains an OPS-specific lower bound on the standard acyclic rect-DAG above N^(3+3epsilon)/log N, or an explicit near-linear rect-DAG for the full low/high promise. O-142 is closed. O-141 remains open at the Q-output cross-signature exits. No new bound on S_rect or rho_prom, and no P-vs-NP proof, has been obtained.

## Current continuation: C-196

The latest proved addition is a local product-hull invariant: at each standard rect-DAG state, tail-projection overlap between two Q-signature fibers forces their signatures to differ on a Q-output coordinate available below that state. If r_v diagonal signatures occur on both sides, their disjoint cylinders jointly force exclusion of at least max(0,r_v*2^(N-|Q|-|T_v|)-M2) high columns. This does not aggregate across states; C-130 overlap and C-80/C-160 counterchecks remain active. Description-space DAG size is exactly invariant under replacing low tables by circuit descriptions. The live goal remains to charge cross-signature exits against reusable tail states, exceed N^(3+3epsilon)/log N in standard DAG size, or find a near-linear DAG for the full promise. No new rect-DAG/rho lower bound or P-vs-NP proof has been established.

## C-198 continuation note
The newest route probe identifies a no-loss lifting interface through partial monotone KW and the CCC 2025 colourful-sunflower theorem. The unproved step is an answer-preserving reduction whose Bob images are all high-circuit-complexity and whose every mismatch is a lifted-search witness. Affine-coset embeddings are ruled out by an O(N) parity separator. O-141 remains the active proof obligation; this is not a breakthrough and the overall goal stays active.



## C-199 continuation note
The latest proved route refinement is a dense-column robustness adaptation of the 2024 triangle-DAG lifting proof: omitting the non-high tables, a 2^(-N+o(N)) fraction, preserves its lower bound up to constants. Therefore individual high-table generation is unnecessary. The unresolved transfer is answer-preserving mismatch encoding with a hard low-image envelope; the easy pointer-code construction has an O(N)-size separator. The active goal remains open.



## C-200 continuation note
The standard colourful-sunflower clique-colouring reduction is now falsified as a C-75 lower-bound route: its Alice-image range has an O(N logN) Boolean recognizer, and signed mismatch adds reverse edges that the mKW decoder cannot handle. Dense-column lifting robustness remains useful but does not fix this. O-141 / shared-DAG lower bounds remain open; no breakthrough or P-vs-NP proof has been achieved.

## C-201 continuation note
A source audit corrected C-199's lifting exponent: Theorem 2.11 gives (1/2)m^((1-delta)w), confirmed by the paper's m^(.99w) near-tightness statement. The dense-column restriction preserves Omega(m^((1-delta)w)) up to constants. This can clear the cubic/log transfer threshold at fixed width if (1-delta)w>3+3epsilon and the source variable count is polylogarithmic in N, but the answer-preserving low/high embedding remains absent. O-141 stays open; this is only a stronger conditional interface.

## C-202 continuation note
A rectangle-mass argument kills the natural unique-output Search(F) source for the lifting transfer. In the Index-lifted full-clause formula, every fixed-answer product rectangle has measure at most (1/(2m))^v, forcing Omega(m^(v-1)) decoder leaves per mismatch type; this exceeds the available lifted lower-bound exponent for the chosen parameters. The live transfer needs answer-rich sources with cheaper decoding, plus a hard low-image envelope. This is route-specific, not a general impossibility or breakthrough; O-141 remains open.

## C-203 continuation note

The constant-degree cPHP source is not eliminated by the decoder-mass test: its CCC 2025 lifting exponent can exceed the fusion compiler threshold multiplied by C-164's minimum decoder cost for fixed width W>4+3epsilon+beta. C-204 now adapts the CCC proof to the exponentially sparse OPS non-high-column deletion, so Bob can be the flattened raw string restricted to high tables. The remaining blockers are an actual per-type decoder upper bound, an all-promised partywise table encoding, and a hard low-image envelope. Keep the focus on the shared-DAG transfer; no new S_rect, rho, or P-vs-NP lower bound has been obtained.

## C-204 continuation note

The CCC 2025 Full Range Lemma and triangle-error union bound support a dense-column restriction; the proof adaptation absorbs the OPS non-high tables, whose density is 2^(-N+o(N)), when W log(mk)=o(N). This closes the high-image/column-deletion issue for fixed-width cPHP. It does not create the low-table map or output decoder. O-143 is closed; O-124/O-141 remain open.

## C-210 current frontier

The latest proof-level addition makes the acyclicization cost explicit. A successful q-pair cover yields a q-state ranked cyclic router; rank layering yields q^2 acyclic multiway states but O(q^2(q+N)) support arcs, so this is not a q^2 binary-DAG compiler. The prior O(q^3/log q) standard compiler and reverse `rho_prom=O(S_rect)` remain the quantitative chain. Short descriptions still do not compress graph states: description-space and truth-table-space DAG sizes coincide. O-141 remains open at amortized product-hull-safe support-router reuse; no superlinear rect-DAG/cover bound or P-vs-NP proof has been obtained.

## C-211 current frontier

A fresh universal-support probe proves that any low/high pair has `Omega(s2/n)` differing coordinates, and probabilistic set cover gives `O(N logN)` total coordinate incidences in a family hitting every such mismatch set. This is not a protocol: selecting a sample with a mismatch is nonrectangular, and a scan that forgets its matched prefix conflicts with the product-hull law unless the suffix can reuse old outputs. The sample-family result identifies output support as too coarse; the unresolved resource is binary product-rectangle routing and cross-history reuse. O-141 remains open. No small universal DAG, superlinear `S_rect` or q bound, or P-vs-NP proof has been obtained.


## C-212 continuation

The latest proof-level progress is a sparse interpolation lemma: any r-point truth-table patch has circuit cost `O(n+r*n/log(r+1))` via shared block decoders. It upgrades the low shattering scale to `Theta(s1)` and the OPS pairwise low/high Hamming gap to `Omega(s2)`, strengthening several restricted-router/context bounds. It does not yield a global rect-DAG lower bound: C-209's product-hull condition still lacks an amortized charge for Q-output exits across cross-signature histories. Continue from bridge C-212 and O-141, using C-80/C-160 as required counterchecks; preserve the current q-to-DAG losses. No P-vs-NP resolution has been obtained.


## C-213 model filter

A `5N`-state cyclic rectangle protocol solves mismatch on every disjoint promise by revisiting previously scanned coordinates, but its independent party-local predicates do not compile automatically into legal fusion closure activations. Broad cyclic-protocol lower bounds are therefore not a route to the target. Continue with acyclic rect-DAG state sharing or the native fusion equations; preserve the current transfer losses. No `rho_prom` upper bound or P-vs-NP proof follows. See bridge C-213.

## C-214 continuation

A direct count in the native closure recurrence shows some arbitrary N-bit partition needs Omega(2^(N/2)) fusion pairs although every disjoint mismatch promise has a 5N-state cyclic rectangle protocol. This proves a strong generic model separation; it does not transfer to the actual low/high circuit promise. Continue O-141 only on the actual acyclic rect-DAG/native closure target, preserving the cubic/log transfer threshold and the free medium band. Full proof and exact C-75 relation audit: `research/C75_SHARED_DAG_CONTINUATION_2026-09-27.md`. No P-vs-NP proof has been obtained.


## C-220 continuation

Continue only the C-75 shared-DAG route. The current proof target is a global charge for distinct residual separators across product-hull-safe merged histories, above `N^(3+3epsilon)/log N`, or a near-linear separator construction. The exact relation, description-space invariance, and transfer losses are audited in `research/C220_SHARED_DAG_FRONTIER_2026-09-27.md`. Triangle-DAG lower bounds transfer in the useful direction (`S_triangle<=S_rect`); no such lower bound has been obtained for this promise. Overall P-vs-NP goal remains active; no proof-level breakthrough is claimed.


## C-221 continuation

Every successful fusion list gives an oriented subcube-cut cover through its seed clauses, but the optimal feature-only cover is at most 2N, so this captures only the known linear scale. Continue at the closure readout: prove that pairing and reusing supports in the positive least-fixed-point program costs superlinear size for this actual promise, or find a near-linear cover. Do not count clause features alone as progress toward the superlinear target. See `research/C221_SEED_FEATURE_VS_CLOSURE_READOUT_2026-09-27.md`. Goal remains active; no P-vs-NP proof has been obtained.



## C-222 continuation

The direct fixed-menu repair to C-115 is closed: any menu of signatures with at most `N^beta` cells needs `2^(Omega(N^beta))` members just to factor all low t-sparse point indicators. Continue at adaptive or implicitly shared circuit-dependent signatures, with product-hull-safe routing; do not infer a general DAG lower bound from this route filter. C-80/C-160 remain mandatory calibrations. See `research/C222_FIXED_SIGNATURE_MENU_LOWER_BOUND_2026-09-27.md`. Goal remains active.



**C-222-A refinement.** The exponential menu lower bound is only a count of fixed maps: a sorting network gives a near-linear adaptive selector for sparse point indicators by outputting their support and a small circuit description. Do not infer an adaptive-selection lower bound from menu cardinality. Continue with the full class of low circuits and the product-hull-safe sharing problem. See C-222-A in `research/C222_FIXED_SIGNATURE_MENU_LOWER_BOUND_2026-09-27.md`.


## C-224 continuation

C-224 proves a robust local signature lemma: an approximate low-table circuit plus k selected wires can represent a high table if approximation-error points and within-fiber minority points are patched, at cost `O(r+k*2^k+(e+m)n)`. Thus high complexity forces error mass or fiber variation; it does not provide the selector or global product-hull charge. A separator complement resembles a large natural property, but CIKK learning requires a uniform P-natural family and yields approximate learning, not a rect-DAG/compiler. Keep focus on C-75/O-141: charge arbitrary shared suffixes or construct a near-linear separator, with the existing `q -> S_rect=O(q^3/log q)` loss explicit. Full note: `research/C224_APPROXIMATE_FIBERS_NATURAL_PROPERTY_BOUNDARY_2026-09-27.md`. No superlinear bound or P-vs-NP proof follows.

## C-225 continuation

C-225 proves one-cell concentration for approximate signatures: for low w and any approximate C correct on at least N/2 positions, a sufficiently large good wire-signature cell admits a high completion obtained by flipping w only there. Both endpoint tables stay below s2, so point-patching forces `Omega(s2/n)` minority points within that single cell. Choosing k=`kappa*n` with `kappa<min(beta,1-beta)` makes the argument work for all fixed beta in (0,1). This closes the mixed-cell-count approach, not the shared-DAG route. Continue O-141/O-149 on selector-free identification of the varying cell and product-hull-safe suffix reuse; no `S_rect`/rho lower bound or P-vs-NP proof follows. Full proof: `research/C225_APPROXIMATE_SIGNATURE_ONE_CELL_CONCENTRATION_2026-09-27.md`.

## C-226 continuation frontier

C-226 gives the exact alternating-reachability normal form for fusion: q states, universal two-side obligations, existential support choices, least/reachability semantics. It also derives a standard co-NBP lower bound for the gap promise from the local-PRG proof, of scale s1^{3/2-o(1)}; at OPS parameters this only exceeds N for beta>2/3. There is no polynomial compiler from the cyclic alternating closure to ordinary NBP, so this result does not imply a fusion lower bound. Continue from O-150: either attack alternating closure directly at small beta, prove a special low-overhead BP compilation, or build a near-linear rect-DAG. Keep C-75 product-hull constraints and the best recorded `q -> O(q^3/log q)` rect-DAG loss explicit. No P-vs-NP proof has been found.


## C-236 continuation â€” canonical low hybrids and the missing q-charge

The selector cap has an exact witness table: for any compatible context/replacement pair from repeated anchors g,h, the selector mu extracted from either endpoint gives the table `H_mu=w_h XOR mu`. This is a completion of the mixed support, hence itself lies in SIZE(s2). The map mu -> H_mu is injective. Thus the compatible selector image is contained in `L_{g,h}={mu: H_mu in SIZE(s2)}`, whose size is at most `|SIZE(s2)|=2^(O(s2 n))`; for typical g,h, the full mask space on D has size at least `2^(N/3)`. Masks outside L have a canonical high hybrid and cannot be realized by a compatible splice.

This still gives no q lower bound. The diagonal equality cover restricts profiles to prefix-constant masks, whose hybrids remain low. The exact next theorem must use the q-state grammar across all low-anchor pairs to charge how it restricts compatible profile images; raw proof-tree counts are uncontrolled. Target `q>=N^(1+epsilon)` for a fixed epsilon, or first an unbounded factor over N, while the near-linear full-promise cover search remains active. Full proof: `research/C236_DISAGREEMENT_SELECTOR_CAP_FOR_COMPATIBLE_SPLICES_2026-09-27.md`.

## C-237 continuation â€” width-only route is closed for typical disagreement profiles

The safe selector set for a typical repeated-anchor pair contains structured subcubes of dimension Theta(s2 n), matching the global C-230 ceiling. The Lupanov constructions are in `research/C237_SAFE_SELECTOR_CUBE_DIMENSION_2026-09-27.md`. Do not pursue a stronger local free-dimension bound from random anchor disagreement; any next lower-bound step must charge the grammar's profile geometry/description or its global cross-products. The full-promise near-linear cover search remains active. No q lower bound or P-vs-NP proof follows from C-237.
## C-239 continuation â€” canonical rank fibers and cross-family charge

C-239 audits the canonical skeleton idea. The activation-rank vector alone is insufficient; a two-rule legal endpoint example has equal state ranks but different seed/predecessor choices. The augmented profile of both side-support minima per state determines one canonical skeleton. For fixed Q it is determined by the 2q-bit seed signature, giving at most 2^(2q) canonical fibers: a better count for this choice, not for every possible witness topology, and still too many to force sharing. The conflict-or-cover law at each reusable state and the one-description synchronization obstacle remain active. Continue seeking a q-sensitive extremal theorem while pursuing the full-promise near-linear cover. See C-239. Goal remains active; no superlinear rho bound, full-promise cover, or P-vs-NP proof has been obtained.
**Priority allocation from the latest steering note.** Put about 50% into native certificate-sharing/splicing proofs, 20% into a full-promise near-linear cover, and 15% into artificial models that satisfy the safe-cylinder calibration. Reserve 10% for amplification only after an `N g(N)` lower bound exists, and 5% for literature directly bearing on these routes. The C-239 clique toy failed the width test; do not reuse it as evidence for the target.


## C-251 continuation

C-251 closes the local seedless-root gap in the escape-support analysis. For each accepted low at a normalized empty root, either a matching direct seed leaves one opposite-side predecessor with a C-250 half-safe support, or no seed matches and two predecessor supports have a union cylinder contained in SIZE(s2). On repeated-block anchors each selected one-support or paired-support signature has subfamily capacity at most 2^((kappa+1)/r). The unresolved step is still global: signature/DAG counts are exp(O(q log(N+q))) and do not charge q. Continue O-153 with a cross-root reuse/compatibility theorem, and keep the N polylog N full-promise cover as a counter-program. Full local proof and failure analysis: research/C251_ROOT_ESCAPE_SUPPORT_DICHOTOMY_2026-09-27.md. Goal remains active; no P-vs-NP proof has been obtained.


## C-252 continuation

C-252 aggregates the escape signatures by state pairs. Empty-root predecessor pairs form a bipartite conflict graph: no high table activates both endpoints, while each accepted low activates some conflict edge or an active-state/direct-literal incidence. This yields a depth-two readout of at most q^2+2qN terms over the q least-fixed-point state predicates and input literals. In the relevant OPS regime q=Omega(N), it matches rather than improves the existing O(q^2) unbounded-fan-in scale. The next target is a structural bound on the high-side activation fibres compatible with this conflict graph, or a near-linear cover. Do not infer a q-bound from graph size, independence number, or readout term count alone. Full proof and limitation: research/C252_STATE_CONFLICT_GRAPH_READOUT_2026-09-27.md. Goal remains active; no P-vs-NP proof has been obtained.

## C-253 continuation

C-253 localizes every activation-profile fibre. A profile containing a conflict edge is wholly low. For an independent profile sigma, low tables in its fibre must match a seed marker attached to an active state, while high tables must avoid every such marker and therefore lie in a subcube fixing r_sigma coordinates. The high-side entropy sum implies some realized independent profile has r_sigma<=q+1, but this may be an unused-by-lows profile with no markers. The graph/fibre count still gives no q improvement. Next test whether the cyclic activation equations constrain how fibres change under coordinate flips or partial assignments. Full proof and exact failure: research/C253_CONFLICT_PROFILE_FIBRE_SUBCUBES_2026-09-27.md.

## Literature calibration

Cavalar?Oliveira (2025) already establish the exact general correspondence between fusion cover complexity and cyclic intersection complexity. The current native closure is therefore an exact target model, not a route around the cover lower-bound problem. Treat C-252's state-conflict graph as a specialized internal normal form, distinct from their graph-complexity objects. The outstanding target is a quantitative lower bound for the actual Gap-MCSP promise. Primary source: https://arxiv.org/abs/2503.14117.

## C-254 continuation

C-254 lifts the C-252 forbidden-pattern readout to partial assignments: any hazardous support has a low-only completion cylinder of dimension at most log2|SIZE(s2)|. A selected readout witness has at most q distinct state labels and at most two seed leaves per state, plus one marker, yielding q >= (N-log2|SIZE(s2)|-1)/2. This is valid but weaker than the existing N-o(N) floor; arbitrary coordinate-order chain event counting still supplies no stronger aggregation. The current primary route is the C-255 shared-DAG programme above. Full correction: research/C254_PARTIAL_SUPPORT_HAZARD_BOUNDARY_2026-09-27.md.

## C-261â€“C-265 priority reset and success criterion

The latest steering raises the progress threshold. Do not report another local lemma as major progress. The next phase is: (A) import a genuinely strong cyclic monotone lower bound through the exact LowExt map; (B) prove independent splicing versus expensive global synchronization in the native grammar; then (C) keep attacking a full-promise N^(1+o(1)) cover as a falsification route. Bounded route filters: C-263 kills the direct sparse matching code, C-264 shows equality fingerprints defeat raw incidence counts, and C-265 kills naive independent cofactor recursion.

C-261 is genuine source-model progress: the spread-matching lower bound survives q-state least-fixed-point semantics after explicit unrolling. C-262 shows the source size v=Theta(log^2 N) gives enough exponent for arbitrarily small fixed beta if the map and YES completions are polylogarithmic. The map is absent, so the actual Gap-MCSP fusion lower bound remains N-o(N). Keep the goal active.

## Latest priority reset - 27 September 2026 (after C-256)

This instruction supersedes the prior route allocation above. Prioritize only two main attacks: (A) import a genuinely exponential cyclic monotone lower bound into exact `LowExt_{s1}` with a monotone map of AND-cost smaller than the source lower bound and a high completion on every NO input; (B) prove global context/subproof synchronization versus independent splicing for the full `SIZE(s1)` class, calibrated against C-258 equality fingerprints. Secondary bounded attempts: (C) terminal-specific BPHP sink refiners, and (D) an ordinary circuit compiler for fixed-support closure worklists. Do not continue local refinements unless they cross one of these barriers. After 3-5 claims, state whether q changed. The actual q bound remains `N-o(N)`. Latest detailed audit is `research/C266_CYCLIC_MATCHING_LOWEXT_AND_SYNCHRONIZATION_AUDIT_2026-09-27.md`; next task is a concrete global-validity encoding for Route A, or an explicit proof that its cost cannot clear the parameter inequality.

The C-271 universal-circuit quotient audit closes explicit description enumeration, blockwise witness forgetting, independent cofactor recursion, and one-state-per-subfunction tables. It leaves the all-class near-linear cover problem open and does not change q.

## C-273 continuation

The July 2026 monotone-learning result was tested as a Route A bridge. Its natural partial-example vector P lies below a fitting low code, while C-125 needs the low code below the YES image; the standard order reversal creates two rails on unspecified coordinates and cannot support a NO high code. Sparse consistent examples have many high completions by counting, which is compatible with C-125 because NO images may also have low completions. C-273 retires only the direct sample-list encoding and leaves a source-monotone asymmetric rail map with low AND cost as the open task. C-272's edge-hybrid entropy also supplies no q charge. Three-claim checkpoint: q unchanged at N-o(N). Continue O-157/O-163 and O-158/O-162.

## C-274 continuation

C-274 strengthens the transfer-map constraint: if the union S of all YES-side conflict coordinates has size at most about (s2-s1)/logN, the shared low-code restriction outside S lets the monotone map plus an N-way AND compute the source. Thus any map that saves more than N ANDs against CycAnd(f) must have a global conflict support of Omega((s2-s1)/logN), or Omega(N^beta/logN) in the project range. This is stronger than C-127's logarithmic support bound, but still allows broad support spread across different YES inputs. The actual q bound remains N-o(N); next test such broad-conflict architectures or derive a per-input conflict aggregation theorem. See O-164.

## Updated route state after C-275/C-276

The conflict-support patch bound is now `O(delta logN/log delta)`, not the earlier `O(delta logN)` minterm estimate. Hence a transfer strong enough for `q>N^(1+epsilon)` requires a global YES conflict union `delta>c_beta s2`, while the exact matching parameter remains `v=A(log N)^2` with `exp(c sqrt(v))>N^(1+epsilon)+a(N)`. The source theorem survives the cyclic least-fixed-point semantics by explicit unrolling; its direct approximation induction is not itself cyclic.

The actual `q` lower bound remains `N-o(N)`. Task 1 and the arithmetic in Task 2 are settled; Task 2's construction is open. Route B's best object is the context/proof/blocker tensor, but C-258 equality fingerprints and C-272's single-expander calibration show no global state charge. Continue with a broad-conflict LowExt map, or prove the map's AND-cost must consume the source lower bound. The goal remains active.

## C-277: Hall-cut obstruction to an OR-only LowExt map

OR-only rail outputs have one fixed polarity per truth-table coordinate because any two opposing edge supports would conflict on a one/two-edge NO graph. All YES codes are then equal, and their containment test is an N-clause monotone CNF. The vertex-cover graphs `G_W` for `|W|=v/4-1` provide `2^(H_2(1/4)v-o(v))` NO inputs. Any clause that accepts every perfect matching can reject at most `2^(v/2-1)` of them by Hall's condition. Thus the CNF needs `2^(0.311...v-o(v))` clauses; at `v=A(logN)^2`, this is larger than N. Zero-AND maps are ruled out, but positive-AND maps are not. No change to q: it remains `N-o(N)`.


## Continuation after C-278

C-278 rules out fixed-NO-scaffold witness-union reductions: if the YES-only excess rails vanish on NO, their OR already computes the source within the map's AND cost. Continue Route A only with a construction whose NO partial image varies with the input and remains high-completable and low-code-free, while YES images contain a full low code and have broad conflict support. Keep the exact `q>=L-a` arithmetic visible. In parallel, revisit Route B only at the global incompatible-synchronization level, testing every proposed object against the C-258 equality fingerprint. Actual q remains `N-o(N)`; no proof of P versus NP has been obtained.

## Continuation after C-279

C-279 verifies that the C-125 asymmetric order conditions can be met with variable high NO codes, but its scalar-rank palette is useless quantitatively: output coordinates reveal each rank predicate, and adjacent-pair decoding gives `CycAnd(F)<=a+O(log^2N)`. Continue by replacing scalar ranks with witness-indexed NO profiles, while proving the output cannot decode the source with `o(L)` extra AND gates. Simultaneously formulate the native context/subproof synchronization object in terms of global profile decodability and retest it against C-258. Preserve the actual checkpoint `q=N-o(N)`; the goal remains active until a verified proof-level breakthrough.
## Priority reset after C-280/C-281

The active research priority is the global sharing/readout problem in the native cyclic fusion closure. The antichain grammar and exact context/proof splice law are already established (C-260); C-281 expresses their table-space consequence through owner masks. Work on a q-sensitive owner-mask product rank and, in parallel, a full-promise N^(1+o(1)) cover. Route A matching maps, ordinary DAGs, and local-width refinements are secondary unless they produce a global theorem or near-lossless transfer. The actual q bound is still N-o(N); no proof of P versus NP has been found.

## C-282 correction (C-283)

C-282's proposed N-gate rail-collision source separator is invalid when the bottom NO image is partial: its differing coordinate can be unset. With d bottom holes and K compatible low codes, the corrected separator costs `a+(N-d)+K max(d-1,0)`, with `K<=2^d`. If `K>0`, sparse-support interpolation against the high bottom completion further forces `d=Omega_beta(s2)` in the OPS gap. C-279 has empty baseline and still fails through a short decoder, so this condition is not sufficient. Route A and native routes O-167/O-168 remain active. Actual `q=N-o(N)`; no P-vs-NP proof has been obtained.

## C-284 parameter update

The matching source dimension can be raised to `v=N^delta` for any fixed `0<delta<min(beta,1-beta)`: sparse matching-incidence witnesses still fit `SIZE(s1)`, while counting still supplies `N^delta` high balanced-class tables. The cyclic source lower bound then beats every polynomial map cost. This removes the polylog source-size restriction but not the map problem; the scaled rank palette still has a short decoder. The active research objective is unchanged and the goal remains unresolved.

## C-285 route update

A direct expander-overlap of raw table projections does not force multiple synchronization costs. Compatibility is coordinatewise equality and factors through one partial assignment; edge expansion adds redundant equalities. Retire overlap-edge count as an invariant. A live Route B construction must use nonprojection coherence and provide a native rule charge for enforcing it. This is not a breakthrough; q remains `N-o(N)` and the full-promise cover search remains open.

## Priority reset after C-286-C-288

C-286 establishes the correct shared-DAG theorem in directional form; Rao's literal two-sided approximation claim is unsupported, but the one-sided errors suffice to prove the entire canonical-table contradiction. The matching source threshold misses the patchable radius at small beta under direct witness coding, so retire that main route. C-287 gives a canonical-table cost floor for Rao clique, but C-290 corrects its route-kill inference: unrolling gives a lower, not upper, bound on `CycAnd`, and a useful map interval remains unresolved. C-288 defines `CohEnc` and proves `rho_GapMCSP>=CycAnd(f)-CohEnc(f)`, but the ODDFACTOR span program has not been converted to LowExt; direct solution-share rails reveal the source decision at equal AND cost. The actual q bound remains `N-o(N)`.

Next work changes mechanism: investigate whether a monotone two-sided primal/dual code can realize a genuine `CohEnc << CycAnd` separation; otherwise prove comparable-decision cost for this reconstruction model. In parallel, resume the near-linear full-promise cover as the falsification branch. C-257 parity and C-258 equality remain mandatory native counterchecks. The goal remains active and unresolved.

## C-289 priority update - 28 September 2026

This pass's C-289 note is a crosswalk, not a new theorem: its proof-term cylinders are already covered by C-244's state zones, and the `Theta_beta(N^beta logN)` maximum dimension is C-230. The low-set versus cylinder-volume comparison is a corollary and gives no q bound. Continue the existing O-153/O-244 low-mass/readout attack and O-168 near-linear cover search; do not track O-169 separately. Preserve C-257/C-258. No q change; actual `q=N-o(N)`. The goal remains active.

## C-290 proof-audit checkpoint

The Rao-clique canonical-table obstruction is retained after choosing `k=2ell` so the promise is disjoint. The claim that it rules out every transfer was unsupported: `CycAnd>=sqrt(L0/C)` cannot show `CycAnd<=L0/4`. A color-coding upper bound `exp(O(k))*poly(m)` remains above the current map-cost floor. Continue the exact transfer-window audit only if it can yield a valid map or close the comparison; otherwise maintain primary focus on O-153/O-168. Actual `q=N-o(N)`; no P-vs-NP proof.
**C-359 continuation:** the attached fixed-circuit lane-selector matrix cannot yield a superlinear q lower bound through ordinary rectangles/fooling sets/communication: with N address rows and constant-size action alphabet its partition number is at most O(N), even if circuit descriptions are added as columns. Escaping that ceiling requires anchor/context rows and a coherent single-description quantifier; independent per-address circuits make the condition trivial. Any extraction from arbitrary C-319 acceptance must be proved, since a cover is only a decision object. Otherwise return directly to the full-promise support-grammar/near-linear-cover branches. Current proved q remains N-o(N); no breakthrough is established.

**C-360 continuation:** tested formula leaf weighting as a possible way to force description/address synchronization. It counts repeated leaves in trees, but one shared OR/state activation serves arbitrarily many callers in a circuit or C-319 graph. The next candidate must be a semantic, splice-sensitive state-incidence weight, not occurrence count. Any extraction of a circuit witness from arbitrary native acceptance must overcome the known MCSP decision/search barrier; actual q remains N-o(N).


## C-361 continuation

Directly serializing the published Multi-MCSP reduction preserves explicit table length but not its complexity gap: output indexing permits an O(b)-size mux in one direction and incurs a factor b in the generic reverse direction, while the source hardness is only for CC(T â€¢ g)-k. The fixed construction's random T slice also excludes the scalar YES case for sufficiently small beta. Park this transfer unless a specific baseline-canceling scalar encoding is found. Return effort to the exact C-319 game and the full-promise cover target; no result beyond rho_GapMCSP>=N-o(N) is recorded.
## C-362 continuation

The exact C-319 recurrence is an explicit reachability game, but native cost q counts paired states while a standard graph-game form also pays for up to q^2 predecessor arcs and qN literal exits. The literature's open circuit-size boundary and mismatch between graph size and q rule out a generic graph-game shortcut. Continue only with a lower bound that uses the constrained signed-literal seed map to charge q, or a valid full-promise near-linear cover. No checkpoint changed: q remains N-o(N); no state synchronization theorem, full-promise cover, positive CohEnc transfer, or P-vs-NP proof has been obtained. The goal remains active.
**C-362 refinement:** the exact native system is the least fixed point of a monotone one-step circuit F_Q over q state bits and 2N dual-rail input bits, with K=O(q(N+q)+N). Therefore a direct breakthrough would be a lower bound for this LFP representation on the actual Gap-MCSP separator, or a q=O(N^(1+o(1))) full-promise cover. Generic graph-game edge size and the MCSP lower bounds for formulas/ordinary branching programs do not transfer; C-339 already audited those models. Keep the goal active.

**C-363 exact route cap:** q=O(N) singleton seed predicates can make the conceptual seed signature injective, so signature capacity and signature-fiber separation alone cannot force a superlinear q bound. Those signature bits are coupled inside their paired equations rather than exposed as free wires. Any next lower-bound argument must charge that cyclic readout, or a construction must implement it in N^(1+o(1)) states with full-promise soundness. This does not change the recorded `q=N-o(N)` bound. Full derivation: `research/C363_SEED_SIGNATURE_HAS_A_LINEAR_INFORMATION_CEILING_2026-09-29.md`.

**C-364 correction:** patching a low table shows `NO_Gap subseteq NO_Approx`; this containment is insufficient to transfer a lower bound from approximate MCSP to Gap-MCSP, since the approximate promise may additionally reject medium tables. Fixed-beta OPS also lies outside the cited subexponential-threshold theorem, and the latter is a formula result rather than a C-319 readout bound. Do not reuse this as a q argument; require reverse containment/equality or a reduction preserving the high threshold and native cost. The lower bound remains `N-o(N)`.

C-365 continuation: the universal-circuit lift G_f(d,x)=U_s1(d,x) XOR f(x) makes the description explicit and evaluates it at every address, but its O(s1 log s1)=O_beta(s2) cost consumes the logarithmic OPS gap. Its huge ambient table has an N-bit image, so full-promise target q lower bounds do not restrict to source q without an endpoint-valid theorem. The only witness-based repair left is an activation code that the LFP itself computes; raw storage capacity is enough, but search-level readout is unresolved. Continue with a direct C-319 readout theorem or a full-promise N^(1+o(1)) cover; do not assume arbitrary decision acceptance yields a circuit witness. Actual q remains N-o(N).

C-365 direction correction: its universal-circuit lift is source-to-target; ambient target hardness does not lower-bound source q. A valid continuation needs a reverse reduction from the full target promise or a lower bound proved directly for the image-restricted promise in a native model that contains every source cover at no greater q.

C-366 retires the entropy-to-search inference: incompressible outputs can be generated from equally informative inputs, and the Omega example is uncomputable. C-367 isolates the explicit search-then-verify construction: selection of a small circuit from w is separate from checking its value at every address; the direct checker costs O(N s1 log s1), while no matching lower bound is proved. Continue on the requested shared-description/address frontier, but do not assume arbitrary cover acceptance yields a circuit description or infer an Ns lower bound from the explicit trace. Current native q remains N-o(N); goal status stays active.

C-367's linear-sketch refinement gives a rigorous exclusion of another tempting compression: any deterministic adaptive linear measurements used to verify a fixed candidate against all high tables need rank N-o(N), by counting the affine transcript fiber. This includes short multilinear-extension fingerprints. It is only a linear information bound; nonlinear readout and native endpoint OR-seeds remain open. No tests were run; only mathematical derivation and document consistency checks were performed.

C-367 now includes a low-degree generalization of the linear-sketch result: the matching-transcript indicator is a nonzero Boolean polynomial, so Reed-Muller minimum distance forces total answer degree at least N-o(N) for deterministic exact verification. This closes low-total-degree fingerprinting as a near-linear-compression route, while leaving nonlinear readout and the native support grammar open.

C-368 derives an exact native-game certificate lemma from C-319 monotonicity: each accepted low table has a minimal seed-test set whose CNF cone is sound and therefore uses at least N-log2|SIZE(s2)|=N-o(N) clauses. This does not improve q because there are two seed features per pair; the live target is a state-sharing/cross-splice charge for these per-anchor certificates.

C-369 calibration: an exponential-in-s1 repeated-fiber subfamily is captured by one O(N)-clause safe CNF and an actual O(N)-state C-258 subcover. This closes anchor-count/certificate-width-only variants of O-216; continue toward a full-promise topology-diversity charge or an N^(1+o(1)) full-promise cover. The active target and lower bound are unchanged.

C-370 advances O-218 with a certificate-internal invariant: every low anchor's true-literal supports have near-full transversal number and contain Omega(N/log q) disjoint logarithmic supports. Continue by comparing these supports across anchors and proving a positional state reuse charge or a C-281/C-320 forbidden splice. The result itself is not a superlinear q bound; preserve the full-promise objective and C-257/C-258 calibrations.

C-370 clarification: the singleton f-true supports are those of the common equality CNF in C-369. They are not asserted to be seed clauses extracted from the separate C-258 native subcover; C-258 is used only as the matching easy-family state-count calibration.

C-370 refinement: if t_k is the number of certificate clauses with at most k f-true literals, the sampling proof gives the full tradeoff t_k >= N(2m)^(-1/(k+1)) - h - 1. In particular, for m=O(N), at least N/2-h-O(1) clauses have O(log N) true literals; and when beta<1/2, at least Omega(sqrt(N)) clauses have exactly one true literal. This strengthens the matching corollary but still supplies no state charge.

C-371 sharpens O-219: any single safe certificate cone containing two low anchors farther apart than h+2 has a selected clause with disjoint true supports of combined size at most log2(2m), and the certificate clauses' splice-falsification subcubes cover almost all owner masks. C-369 shows pairwise witnesses can be shared at linear cost on repeated-fiber tables. Continue with a multi-anchor topology-diversity charge or a full-promise near-linear cover; no q improvement follows.

C-371 literature note: Cheraghchi-Kabanets-Lu-Myrisiotis prove exp(N/O~(log^2 N)) lower bounds for a single CNF or DNF computing exact MCSP, but one C-319 safe certificate cone is not the full acceptance predicate. The least-fixed-point readout may union many certificate cones, and no size-preserving flattening to one CNF/DNF is known. This result therefore does not transfer to q; see C-339 and C-371.

C-372 adds a proved common-policy obstruction using Reed-Muller dual distance: one sound seed-CNF cone containing a large low-circuit code family needs superpolynomially many clauses. It does not yet charge arbitrary q-state covers because policies can vary by input; the crude number of seed-subset regions is sufficient to separate this subfamily at q around N. Preserve the active target and continue toward a transition-graph-sensitive cross-cone theorem. Current proved lower bound: q>=N-o(N); no P-vs-NP proof.

C-373 strengthens the Reed-Muller cone obstruction to arbitrary policy switching: every polynomial-q sound policy region captures at most 2^(-Omega(sqrt(D))) of the low code, so a complete cover must use 2^(Omega(sqrt(D))) distinct policy regions. The generic 2^(2q) count gives only q=Omega(sqrt(D)), weaker than the established linear bound. The next open step is a transition-graph-sensitive capacity or cross-region splice theorem; generic CNF fooling/counting is exhausted at this scale. Goal remains active; q remains N-o(N).

C-374 closes the pure policy-region count avenue: any cover can choose one region per low table, and log|SIZE(s1)|=o(N), so cardinality alone cannot even reach the current linear lower bound. Continue on the transition-sensitive cross-policy context/proof product obligation O-222; charge actual graph sharing through C-281 compatibility and account for C-130/C-132/C-145. Goal remains active; q remains N-o(N).

C-375 retires ordinary deterministic communication-bit lower bounds as a superlinear route when transferred linearly to q: the explicit N-bit table has communication complexity at most N/2+O(1) under any coordinate split. It sharpens the active target to the computational capacity of the recurrent C-319 decoder, since O(N) seed features can already expose the full table and q rounds yield at most q^2 paid AND occurrences. No q improvement or proof is established; keep the goal active and pursue a direct state/work lower bound or full-promise N^(1+o(1)) construction.

C-376 derives an exact paired low/high mismatch game from any C-319 cover, with at most q native states and termination by decreasing activation rank. The induced mismatch relation has a trivial N-state coordinate scan, so it does not improve the lower bound. This isolates what a usable selector/game reduction must preserve: circuit-description coherence or an equivalent promise-specific computation constraint. Hazard-free formula results do not transfer through the current one-sided support semantics. Keep the goal active; q remains N-o(N), with no full-promise near-linear cover or P-vs-NP proof.
C-377 uses positional determinacy to fix one global winning action table for each accepted input. The resulting policy cube is sound and fixes N-o(N) coordinates, but this yields only q>=N/2-o(N), below the established floor. The policy is not compelled to encode a circuit, and counting policies cannot pay for q. Keep the goal active and pursue a transition-graph-sensitive cross-anchor policy theorem or a full-promise N^(1+o(1)) cover; no breakthrough has been established.
C-378 isolates the exact splice condition for per-input policies: an acyclic hybrid of their actions yields a sound cube, but cyclic hybrids can have true selected seeds and still lose under least-fixed-point semantics. Thus C-281-compatible support unions are not enough; any cross-anchor charge must also control well-foundedness despite C-141/C-142 rank reversals. The live target is an acyclic-hybrid closure theorem for one fixed transition graph or a full-promise N^(1+o(1)) cover. No q improvement; keep the goal active.
C-379 proves that each positional root-policy cube can contain at most one codeword from the C-372 far-apart low Reed-Muller family, forcing |F| distinct root-policy pairs. The action-table count still yields only q>=|F|/O(q log N), which is sublinear for this family. This closes another policy-count variant; no q improvement. Continue with O-226's graph-sensitive valid acyclic-hybrid analysis or the full-promise near-linear cover.

## C-380/C-381 - Acyclic policy paths and why one representative per anchor is not enough

C-380 proves same-root winning positional policies are connected by a rank-ordered path of structurally acyclic hybrids. The remaining issue is literal consistency. C-381 combines those paths with C-320: selecting one root/policy per low anchor yields only |F|^2(2q+1)=2^(o(N)) path masks, while almost every robust split avoids this set and its C-320 balls. Thus one representative per anchor cannot force the forbidden splice. This is a quantifier-order/entropy obstruction, not a failure of C-320 or the exact C-380 lemma.

Checkpoint after C-383: all A-E outcomes remain NO; q is still N-o(N), with no near-linear full-promise cover or P-vs-NP proof. C-382 closes split-independent mask forcing. C-383 rules out residual/profile/policy/communication counts and naive gate-address storage as the superlinear charge. Continue on actual least-fixed-point readout work or construct the full-promise near-linear cover. The overall goal remains active.

## C-384 continuation

A fixed description C can be verified by N signed table literals, so its selector matrix cannot itself force q>N; moreover circuit padding can change the matrix without changing the represented table. Do not continue fixed-description rectangle, fooling-set, or witness-count variants. Continue only with a representation-independent joint-description/address theorem induced from every valid C-319 cover, or an explicit endpoint-valid near-linear graph. Preserve `exists one C forall x`; per-address descriptions are vacuous. C-320 applies only after a high owner pattern is forced; compatible products are safe. Checkpoint: q remains N-o(N), and neither a full-promise near-linear cover nor a P-vs-NP proof is established.

## C-384 novelty correction and next subproblem

C-349/C-342/C-367 already cover representation instability, observable selector channels, and search-versus-all-address verification. C-384 synthesizes those results and adds the fixed-table native bracket `N-o(N) <= rho <= N+O(1)`; it is not a new route. Continue with the activation-code branch: prove an arbitrary C-319 cover yields a coherent low-circuit decoder from its input-derived signature/activation profile, or show why no such decoder/readout can be obtained at near-linear q. Do not count raw profile bits, since q=Theta(N) can expose all table bits. Keep the goal active; q remains N-o(N).

## C-385 continuation note - exact seed-order characterization

A fixed seed signature map admits some monotone promise decoder iff no low signature is coordinatewise below any high signature; equivalently, the seed-feature rectangles cover every low/high pair. The full 2N signed singleton features satisfy this condition for every disjoint promise, and their paired signature can be injective at linear scale, but the paired recurrence may still fail to decode anything. Therefore all seed-order, fiber, and pairwise-feature arguments have a universal linear ceiling. The active cost is the constrained least-fixed-point readout (O(q^2) monotone-gate unrolling); no superlinear native bound or near-linear full-promise cover follows. See research/C385_MONOTONE_SEED_ORDER_ISOLATES_READOUT_COST_2026-09-29.md.


## C-386 through C-388 continuation

C-386 rechecked the strategy-as-description idea: positional actions may store bits, but a merged state-side has no caller-address register; this closes only that architecture, not the input-derived activation-profile channel or arbitrary C-319 covers.

C-387 rigorously proves the Reed-Muller narrow-seed localization candidate. For each fixed epsilon>0 and any fixed polynomial state exponent a, every valid q<=N^a cover has at least (1-epsilon)N-o(N) global seed slots of width C(a,epsilon,delta) log N. The proof combines C-370's sparse certificate count with a 2r-th moment tail for the (D-1)-wise independent RM probe. This is a structural linear-scale theorem only: q remains N-o(N). Wide seed tests may still be essential to the readout, so the localization does not yet imply a local-only LFP.

C-388 formalizes the C-346 hard-core sample relation R(f,Q). A proposed sample is coNP-verifiable, and existence of one is a Sigma_2^P promise separator. The minimax/LP construction uses an NP best-response task, and no efficient selector, all-selector lower bound, or q-preserving bridge to arbitrary native covers is known.

Active work items are O-229 (prove or refute wide-feature dispensability in the localized certificate core while preserving all-high rejection) and O-230 (construct or lower-bound selector synthesis with the NP optimization cost charged and prove an explicit bridge before transferring conclusions). The project goal remains active. No superlinear Gap-MCSP bound, full-promise near-linear cover, or P-vs-NP proof has been obtained.


## C-389 continuation

C-389 tests O-229 with an explicit monotone feature-map countermodel: near-full narrow sparse certificate support can coexist with an essential wide readout coordinate. Thus the deletion inference is false from monotonicity and incidence data alone. The countermodel is not endpoint-realizable as far as established, so the native question remains open. Keep the goal active; q remains N-o(N), with no full-promise cover or P-vs-NP proof.

## C-390 continuation and mandatory checkpoint

C-390 closes the remaining endpoint-realization gap for the *subpromise* form of O-229. A masked Reed-Muller membership circuit and one wide root give a valid q=O(N log N) C-319 cover of the RM probe against the actual high set; deleting every globally wide seed makes it reject every RM anchor. This is a route-kill for the universal wide-feature deletion inference, not a full-promise result. The low probe remains easy to recognize in O(N log N), and the cover does not accept all SIZE(s1).

Checkpoint: the native quantitative bound did not move beyond N-o(N); selector synthesis has neither a near-linear construction nor an all-selector N^(1+epsilon) lower bound; there is no q-preserving bridge; no collectively hard low subclass was found; and no lower bound for the general C-319 local-seed LFP readout was proved. C-390 is the one concrete outcome: endpoint-realizable wide features can be indispensable at near-linear subpromise cost. Continue with the two computational frontsâ€”full LFP readout work and hard-core selector synthesisâ€”and charge every optimization/separation oracle. The project goal remains active; no P-vs-NP proof or breakthrough claim is made.

## C-391 continuation

C-391 makes the selector search-to-decision gap precise. The canonical fixed-length sample encoding can be found by O(L log N) prefix-extension queries, each in Sigma2^P because candidate validity is coNP. Thus the canonical selector is in FP^Sigma2, but this does not give Boolean circuits of near-linear size. The unconditioned existence predicate answers only the empty-prefix query; it does not automatically answer the conditioned queries needed to extract the witness. Continue both fronts in parallel: attack the complexity of these prefix queries/selector relation, and independently seek a state-sensitive bound or near-linear construction for the full C-319 LFP. No quantitative Gap-MCSP bound changed; goal remains active.

## C-392 continuation

C-392 constructs an O(N log^3 N) sorting selector that is valid for 1-o(1) of uniformly random weight-N^beta high tables, with empirical error at least 0.45 against every C-388 size-T circuit. This sharpens C-23 but only on the typical sparse distribution. It route-kills average-case sparse-support lower bounds; the exceptions and arbitrary high inputs are still the actual all-selector challenge. Keep the full-promise C-319 LFP front active independently. Native q remains N-o(N); there is no all-high selector, selector/native bridge, or P-vs-NP proof. The goal remains active.

## C-393 continuation and checkpoint

C-393 gives an exact paid-AND upper bound `A_cap<=m+(s+1)(q-m)`, where s counts distinct one-sided escape-source carriers after C-92/C-93/C-94 normalization. It isolates the readout's work parameter but no theorem makes s=o(q), so this remains an upper compiler, not a lower bound. The mandatory five-part checkpoint is in `research/FRONTIER_CHECKPOINT_AFTER_C393_2026-09-29.md`. All five success questions are still negative; change mechanism now. Stop refining sample concentration or narrow-seed certificates as standalone routes. Next attack the actual anchor-versus-seed-clause incidence structure or a collectively hard low family, with C-258 equality as the hostile calibration. The overall goal remains active.

## C-394 correction - signature cones are C-385 in certificate form

C-394 identifies the full set of seed clauses true on an accepted low f as a canonical safe certificate: its model set is the preimage of the signature upper cone, which monotonicity maps into Q's sound acceptance set. This is exactly C-385's order characterization, not a new result; C-368 yields at most q >= (N-o(N))/2, weaker than the current q >= N-o(N). The proof-DAG selector can shorten the certificate but adds no q bound. The active target remains a representation-independent cost for the constrained LFP readout, or a valid near-linear full-promise cover. Keep the goal active.

This completes the canonical-incidence question from the C-393 checkpoint and closes it as a standalone lower-bound route. Continue only if incidence is tied to endpoint-constrained readout work, escape-source cost, or a forced cross-anchor splice; do not return to raw rows, widths, or certificate counts.

## C-395/C-396 side result - polynomial covers need growing escape-source diversity

C-395 adapts CKLM local restrictions to the actual low/high promise, explicitly handling its unrestricted middle interval. C-396 applies the source lemma in its all-depth form: polynomial-size AC0 separators cannot have depth `O(log N/log log N)`. Since C-393 compiles a C-319 cover with k escape sources to depth `O(k+1)`, every polynomial-size full-promise cover must have `k=Omega(log N/log log N)`. This narrows the possible architecture of a near-linear cover, but it does not improve the state bound `q>=N-o(N)` or lower-bound the paid-AND measure. Keep this as a proved side constraint; the active proof target remains a q-sensitive charge for the exact readout or a near-linear construction, with C-258 as the equality calibration. The overall goal remains active.

## C-397 continuation - exact bridge and literature boundary

C-397 audits the new continuation request against the current repository. The Reed-Muller narrow-seed lemma is not pending; C-387 already proves it, and C-390 kills universal wide-seed deletion at subpromise scale. A hard-core selector for C-388's exact relation composes with its coNP verifier to produce a promise-coNP/poly separator. Under `NP subseteq P/poly` this yields a polynomial-size ordinary separator, but with no controlled exponent. A decision bit still does not self-reduce to the conditioned Sigma_2 prefix queries needed for Q (C-391). No size-controlled selector/native-cover bridge is known.

Fixed-point logic and Datalog remain analogies rather than transferred lower bounds. The checked FPC characterization applies to uniform symmetric circuit families on relational structures. C-319's endpoint-derived clauses are nonuniform and may single out any truth-table coordinate; no symmetry-preserving interpretation with controlled q overhead is known. Orbit symmetrization across input-variable permutations has `n!` copies and is superpolynomial in `N=2^n`. Keep the exact C-319 recurrence as target; do not claim an LFP theorem yields superlinear q. The active task is to find a small verifier for the specific selector relation under a precise hypothesis, avoid its universal search layer, or charge the complete endpoint-derived LFP directly. See `research/C397_FIXED_POINT_AND_SELECTOR_TRANSFER_AUDIT_2026-09-29.md`.
## C-398 continuation - conditional selector transfer and unconditional limits

C-398 refines C-397: the coNP validity test for a hard-core list depends only on its addresses and labels, an input of `M=O(N^beta log N)` bits. Define one fixed NP language `BAD` with unary circuit-size parameter T, so under `NP subseteq P/poly` its circuit exponent d is uniform as beta varies. Computing labels from the full table costs `O(N^(1+beta) log N)` by direct lookup; the BAD verifier costs `O(N^(beta*d) log^d N)`. Hence an all-high selector of size `N^(1+delta)` yields a Gap-MCSP separator of size `N^(1+epsilon)` for any fixed epsilon>delta, by choosing beta sufficiently small and `beta*d<1`. This is conditional on small circuits for BAD; it neither constructs the selector nor proves P-vs-NP.

Unconditionally, enumerating predictor circuits gives only `2^(O(N^beta))` verifier size. The minimax proof and its best-response oracle do not improve this. The parallel C-319 check also closes the tempting C-393/C-396 inference: the available `A_cap` lower and upper bounds yield only `q>=(N-o(N))/(s+1)`, while C-396 lower-bounds s rather than upper-bounding it. Keep searching for an efficient sample relation/verifier and, separately, a direct q-sensitive LFP charge or full-promise construction. Native q remains `N-o(N)`; no P-vs-NP proof. See `research/C398_SELECTOR_TO_DECISION_NEAR_LINEAR_UNDER_NP_POLY_2026-09-29.md`.
**Proof-carrying sample audit.** Turning `BAD` into a SAT formula and attaching a sound refutation removes the universal search from verification, but only if the proof is supplied. Completeness gives a refutation for high-side samples, while C-346 gives no useful bound on its length. Treat this as a proof-complexity research target, not a current selector result.

## C-399 continuation - finite-list learning reduction fails after padding

C-399 checks the proposed CircCons route against its actual promise. A C-388 finite empirical list on K<=L points is fit exactly by a lookup circuit of size O(Lm). The direct table-driven sampler's O(Ln) size bound does not certify the required `m>sqrt(s)` condition at the original dimension; C-346 supplies no shorter sampler for the selected list. Padding enough to meet that condition using this encoding makes the theorem's `SIZE(m^(log log m))` NO-side class large enough to memorize the list. This closes the direct padded-list transfer only; a different succinct large-support sampler remains unruled out, and SZK^A is not a deterministic P verifier.

## C-400 continuation - mux toy resolves at linear subpromise cost

C-400 constructs `f_y(a,z)=y_a` with `M=N^(beta/2+o(1))` freely chosen data bits. Its natural DNF has a different unique true OR witness at each one-valued address a, but the family is recognized by fiber equalities `w_(a,z)=w_(a,0)`. This gives an `A_cap<2N` signed-literal separator and, by C-307, a valid endpoint-derived native cover for that subpromise; the one-anchor lower bound makes its scale `Theta(N)`. The mux route therefore cannot prove superlinear q from local witness diversity. It does not yield a full-promise cover. For the actual objective, continue seeking either (i) a low family with no O(N) signed local-constraint recognizer plus a proof that C-319 sharing forces a compatible C-320 high splice, or (ii) an endpoint-valid near-linear cover of all `SIZE(s1)`. The full-promise bound remains `N-o(N)` and the Goal stays active.

### C-420 research cycle

Tested a new promised codeword embedding with an explicit ordinary-gate cost interface. A random code image can indeed have one Low word and every nonzero word OPS-High, and counting supplies hard kernel predicates. The full proof attempt shows why this still cannot charge the separator: the image trace is zero testing, so `O(N)` gates decide it and the table map must already compute the hard predicate. A separate kernel argument rules out linear sketches of rank below `N-O(N^beta log N)` as full-promise preprocessors. The exact enumerator remains exponential in `N^beta`; neither ordinary nor native frontiers move. Retired this zero-anchor embedding and low-rank sketch route; proceed to direct shared-readout mechanisms.

### C-421 research cycle

Derived a separator-specific certificate extractor: from the actual evaluation DAG on a High input, one reverse pass marks local gate certificates and yields a coordinate set forcing rejection. The set anti-checks every Low circuit, and shared gates are visited once, so the construction costs O(S) total gates. The proved list length is only `min(N,2S)` and can be N; parity is the width-N calibration. Compressing it to the OPS `N^(10 beta)` scale requires a separate Sigma2 search because fixed-certificate validity is coNP and middle inputs may be accepted. No ordinary/native frontier change.
