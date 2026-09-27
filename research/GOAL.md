# Goal and standards

Establish a rigorous proof of P = NP or P != NP. If a full resolution is not obtained, aim for a genuinely new theorem that materially reduces the unrestricted gap, with the exact remaining obstacle stated.

A result must specify its objects, quantifiers, computation model, resource bounds, uniformity, and assumptions. Every implication must be proved or cited precisely. Restricted-model results need an explicit transfer theorem before they can constrain arbitrary polynomial-time algorithms. Finite experiments may falsify claims or check implementations; they do not establish asymptotic statements. Do not call a result a breakthrough until it survives an adversarial proof audit.

## Active route

Current phase: continue from C-74/C-75 on standard acyclic product-rectangle DAG complexity for the Gap-MCSP low/high mismatch relation. The exact relation, nearby DAG/loop models, description-space invariance, and cover-to-DAG transfer chain have already been audited; do not restart those tasks. C-194 closes O-142: signed mismatch has a universal 4N-1-state degree-two inequality protocol, but this model has triangle states and can be exponentially stronger than rect-DAGs. The live target is an OPS-specific lower bound against arbitrary alternating rect-DAGs, or an explicit near-linear rect-DAG for the full low/high promise. A standard rect-DAG lower bound must exceed N^(3+3epsilon)/log N under the current compiler to force rho_prom>N^(1+epsilon); a direct cyclic-cover lower bound avoids that loss. C-175/C-176 retire raw and simple path-weighted conflict-volume charges. C-187 shows that local Hamming-ball filters, including the sparse point-indicator subfamily, have O(N)-size separators; C-189 gives only an Omega(s1/n) worst-case lower bound on Bob-selected certificates, while C-190 shows a fixed O(N^beta)-coordinate set certifies a mismatch for at least half of high columns; C-168 forces N-o(N) for low-row-selected universal witnesses. Shared search remains unresolved. Continue O-141/Q134/Q138 and suffix-valid residual-context analysis from the C-190 trace split, with C-80/C-121 and C-160 as counterchecks. See [CURRENT_STATE.md](CURRENT_STATE.md), [DAG_FUSION_BRIDGE_2026-09-26.md](DAG_FUSION_BRIDGE_2026-09-26.md), and [OPEN_OBLIGATIONS.md](OPEN_OBLIGATIONS.md).

The overall proof target remains a Gap-MCSP lower bound with an explicit magnification transfer. Prioritize the weakest open theorem on this active shared-DAG path. Search for counterexamples before extending a construction, state every quantitative loss, and record each failure's first broken implication.

C-222/C-223 close the fixed-menu repair and delimit explicit adaptive circuit selection: a circuit selector yields a separator only after an `N s1`-scale universal evaluation, while a general rect-DAG need not synthesize a circuit. Do not treat selector hardness as an unrestricted DAG lower bound. Continue O-141 on global product-hull-safe state reuse, or falsify the route with a direct near-linear DAG. Full latest route note: `research/C223_ADAPTIVE_SIGNATURE_SEARCH_MCSP_BOUND_2026-09-27.md`.


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
