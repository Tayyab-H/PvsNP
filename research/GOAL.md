# Goal and standards

Establish a rigorous proof of P = NP or P != NP. If a full resolution is not obtained, aim for a genuinely new theorem that materially reduces the unrestricted gap, with the exact remaining obstacle stated.

A result must specify its objects, quantifiers, computation model, resource bounds, uniformity, and assumptions. Every implication must be proved or cited precisely. Restricted-model results need an explicit transfer theorem before they can constrain arbitrary polynomial-time algorithms. Finite experiments may falsify claims or check implementations; they do not establish asymptotic statements. Do not call a result a breakthrough until it survives an adversarial proof audit.

## Active route

**Latest priority reset (user's attached instruction, 27 September 2026, after C-254):** focus on the standard acyclic shared product-rectangle DAG for the exact C-75 mismatch relation. Do not restart broad P-vs-NP brainstorming. Current audit: [C-255](C255_SHARED_DAG_ROUTE_RESTART_2026-09-27.md); latest route test: [C-256](C256_HARD_TRANSLATE_KW_DECODER_OBSTRUCTION_2026-09-27.md). Either prove an OPS-specific shared-state lower bound or construct an adaptive/revisiting near-linear DAG. Keep the exact q-to-DAG loss `S_rect=O(q^3/log q)` visible, so the transfer target for `q>N^(1+epsilon)` is `S_rect>N^(3+3epsilon)/log N`. C-256 rules out common-hard-translate reductions with static output-label decoding from two-wise-rich KW sources (by reconstructing the mask in `O(M s1)` size) and from full-domain BPHP collision search (by a two-answer cover obstruction). These are transfer no-go results, not DAG lower bounds. The live alternatives are terminal-specific decoding with an explicit size-preserving simulation, a different source answer geometry, the direct per-node bottleneck-capacity lemma, or an actual C-75 DAG construction. Re-audit every candidate against product-hull safety and C-80/C-160/C-213/C-217/C-232. Short circuit descriptions do not change rect-DAG size, and the direct universal separator remains exponential. The earlier O-153 native certificate-sharing programme is superseded as the active priority; use its proofs only where they improve the DAG compiler or yield a direct invariant. No P-vs-NP breakthrough has been obtained.

The overall proof target remains a Gap-MCSP lower bound with an explicit magnification transfer. Prioritize the weakest open theorem on the active shared-DAG route. Search for counterexamples before extending a construction, state every quantitative loss, and record each failure's first broken implication.

C-222/C-223 close the fixed-menu repair and delimit explicit adaptive circuit selection. Do not resume that branch unless it yields a global product-hull charge or a near-linear separator.

**Current work order:** first test direct bottleneck-capacity proofs on the actual C-75 relation; next search for terminal-specific/source reductions whose decoder overhead can be bounded; in parallel try to construct a near-linear adaptive full-promise DAG. Do not spend effort on another static common-translate/KW or static common-translate/BPHP map: C-256 rules out those interfaces. Literature review supports proof work but is not a substitute for it.


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


## C-236 continuation — canonical low hybrids and the missing q-charge

The selector cap has an exact witness table: for any compatible context/replacement pair from repeated anchors g,h, the selector mu extracted from either endpoint gives the table `H_mu=w_h XOR mu`. This is a completion of the mixed support, hence itself lies in SIZE(s2). The map mu -> H_mu is injective. Thus the compatible selector image is contained in `L_{g,h}={mu: H_mu in SIZE(s2)}`, whose size is at most `|SIZE(s2)|=2^(O(s2 n))`; for typical g,h, the full mask space on D has size at least `2^(N/3)`. Masks outside L have a canonical high hybrid and cannot be realized by a compatible splice.

This still gives no q lower bound. The diagonal equality cover restricts profiles to prefix-constant masks, whose hybrids remain low. The exact next theorem must use the q-state grammar across all low-anchor pairs to charge how it restricts compatible profile images; raw proof-tree counts are uncontrolled. Target `q>=N^(1+epsilon)` for a fixed epsilon, or first an unbounded factor over N, while the near-linear full-promise cover search remains active. Full proof: `research/C236_DISAGREEMENT_SELECTOR_CAP_FOR_COMPATIBLE_SPLICES_2026-09-27.md`.

## C-237 continuation — width-only route is closed for typical disagreement profiles

The safe selector set for a typical repeated-anchor pair contains structured subcubes of dimension Theta(s2 n), matching the global C-230 ceiling. The Lupanov constructions are in `research/C237_SAFE_SELECTOR_CUBE_DIMENSION_2026-09-27.md`. Do not pursue a stronger local free-dimension bound from random anchor disagreement; any next lower-bound step must charge the grammar's profile geometry/description or its global cross-products. The full-promise near-linear cover search remains active. No q lower bound or P-vs-NP proof follows from C-237.
## C-239 continuation — canonical rank fibers and cross-family charge

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
