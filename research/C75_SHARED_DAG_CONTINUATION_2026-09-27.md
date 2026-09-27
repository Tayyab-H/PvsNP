# C-214 - Native fusion-state counting and the shared-DAG boundary

Date: 27 September 2026

## Scope

Continue the C-74/C-75 line only. This note gives an exact relation-level audit, checks the best cover-to-DAG and DAG-to-cover transfers, and adds a direct counting theorem for the native fusion closure on arbitrary promise partitions. The counting theorem is a model-separation calibration, not a lower bound for the actual Gap-MCSP promise.

Write \(N=2^n\), \(Y=\mathrm{SIZE}(s_1)\), and \(Z=\{0,1\}^N\setminus\mathrm{SIZE}(s_2)\), so \(Y\cap Z=\varnothing\). The actual target remains
\[
\rho_{\mathrm{GapMCSP}}=\rho_{\mathrm{prom}}(Y,Z)>N^{1+\epsilon}.
\]

## The two C-75 relations

### Plain signed mismatch

The input is \((w,z)\in Y\times Z\). Alice knows the low truth table \(w\); Bob knows the high truth table \(z\). A valid output is \((k,b)\) satisfying
\[
w_k=b,\qquad z_k=1-b.
\]
It is total because \(Y\cap Z=\varnothing\). This is the ordinary promise-restricted Bit/Karchmer-Wigderson relation.

### Q-dependent closure path

Fix a proposed pair list \(Q=((E_i,H_i))_{i=1}^q\), with \(T_i=E_i\cap H_i\). For each \(w\), let \(\tau_i(w)\) be the first round at which \(T_i\) enters the least closure generated from the matching slices
\[
L_{w,k}=Z\cap\{z:z_k=w_k\}.
\]
A valid Q-path output is a finite sequence of rule states and side choices, ending in a signed mismatch, with the following conditions:

1. It starts at a rule \(i_0\) with \(T_{i_0}=\varnothing\) and \(\tau_{i_0}(w)<\infty\).
2. At a visited state \(i\), Bob chooses a side \(S\in\{E_i,H_i\}\) absent from \(z\). Such a side exists because \(z\notin T_i\).
3. Alice either supplies a seed \(L_{w,k}\subseteq S\), in which case \(z_k\ne w_k\) and the path outputs \((k,w_k)\); or supplies a predecessor \(j\) with \(T_j\subseteq S\) and \(\tau_j(w)<\tau_i(w)\), and the path continues at \(j\).

The path relation depends on all endpoints, carrier inclusions, and empty-carrier labels in Q. It is total on \(Y\times Z\) exactly when Q is a successful cover. The rank decreases on Alice's input, so every valid path terminates in at most q rule moves. A Q-specific path therefore preserves more structure than the plain mismatch output, but its state graph is cyclic in general.

## Resource audit

These are different resources; none should be called simply “communication size.”

| Model | Current bound or identity for the actual promise |
|---|---|
| Deterministic communication bits, plain mismatch | \(O(s_1\log(n+s_1)+\log N)\) by sending a circuit description and scanning locally; the recorded lower bound is \(\Omega(\log N)\). |
| Protocol tree vertices | At least \(N-\log_2 M_2\) output leaves in the recorded disjoint-output family; description transmission gives at most \(N\,2^{O(s_1\log(n+s_1))}\) vertices. |
| Acyclic binary product-rectangle DAG | \(S_{\rm rect}=\Theta(C_{\rm sep})\), where \(C_{\rm sep}\) is the minimum Boolean circuit size of any \(h\) with \(h=1\) on Y and \(h=0\) on Z. Medium truth tables are unconstrained. |
| Q-dependent path communication | At most \(O(q\log(N+q))\) bits by naming the side/support at each of at most q rule states; total exactly when Q succeeds. |
| Q-specific ranked cyclic witness | q rule states, plus at most \(2N\) signed-output leaves; up to \(O(q(q+N))\) support choices. Termination is by the pair-dependent rank \(\tau_i(w)\). |
| Unrestricted cyclic rectangle protocol | At most \(5N\) states for every disjoint promise, by the C-213 coordinate scan. This is not a fusion cover. |

The tree/DAG comparison needs one correction in its wording: a tree with few vertices cannot be harder than a DAG with many vertices, since every tree is already a DAG. The useful separation is between communication depth/bits and graph vertices: an \(m\)-bit deterministic protocol may have \(2^{\Theta(m)}\) tree vertices, while a shared DAG is governed by residual-relation reuse. Formula/tree versus circuit/DAG comparisons run in the other direction.

## Nearby models and exact transfers

| Model | Semantics | Relation to Q |
|---|---|---|
| Sokolov Boolean DAG-like games; GGKS rect-DAGs | Acyclic, outdegree at most two; each node is a product rectangle and its children cover that rectangle. | Plain C-75 mismatch is exactly the promise-restricted search relation. Its minimum DAG size is \(\Theta(C_{\rm sep})\). |
| GGKS triangle/F-DAGs | A triangle state has form `a(x)<b(y)`; every product rectangle is a triangle, so this is a stronger protocol model. | `S_triangle <= S_rect`: a lower bound for triangle-DAG size transfers directly to rect-DAGs, while a triangle-DAG upper bound does not. C-194's particular interval-comparison protocol and C-195's lower bound on its top state's rectangle expansion do not lower-bound every rect-DAG. |
| Cavalar-Oliveira cyclic intersection complexity | Cyclic set equations with their least-fixed-point semantics. | The promise fusion measure is exactly \(q=\rho_{\rm prom}=D^\circ_{\cap}\) for the chosen promise ground set and semi-filter model. |
| Nakayama-Mar(u)oka loop circuits | Cyclic specifications with loop semantics, in a related but not identical functional framework. | Historical/theorem-level antecedent; the Cavalar-Oliveira adaptation is needed for this exact semi-filter cover identity. |
| Amano-Mar(u)oka conjunctive complexity | AND-gate count for a specialized monotone circuit problem. | No C-75 transfer without an AND-preserving reduction. |

For a successful Q, the q activation states themselves form a valid *cyclic* closure computation. They do not automatically form a standard DAG: a state may use a predecessor whose activation rank is lower for the current w, while the fixed rule-dependency graph has cycles. C-141 supplies a legal rank-reversing SCC, so there need not be a global topological order on the q labels. This alone does not prove that every acyclic representation needs q squared states; the C-141 separator simplifies, so it is only a counterexample to the naive global-order argument.

The best proved standard-DAG compiler remains
\[
S_{\rm rect}=O(q^3/\log q)
\]
(and \(D_{\cap}\le q^2\) in the separate AND-only measure). Rank layering gives \(q^2\) rule/rank rectangles, but each has up to \(O(q+N)\) supports; counting only the vertices and ignoring the fanout is invalid. No lower bound rules out a better compiler such as \(O(q\,\mathrm{polylog}\,N)\); it is simply not established.

**Attempt to share the rank-layer support routers.** For a fixed rule i and endpoint side S, the legal predecessor labels \(j\) with \(T_j\subseteq S\) are fixed; what changes with the layer r is which of those j are active by round r-1 on a given row. Reusing one router across several r-values is valid only if its suffix solves the full product hull of the incoming rank rectangles and routes every cross-pair to a support that remains valid there. A fixed target layer \((j,r-1)\) is not automatically valid for rows arriving from another r. Splitting by (r,j) recovers the known fanout cost. C-141 rules out replacing the input-dependent ranks by a global topological order, but does not prove all alternative router sharing impossible. The exact missing proof would be a quantitative lower bound on how many product-hull-safe support-router contexts are needed, or a construction that shares them.

In the reverse direction, an L-vertex rect-DAG yields an \(O(L)\)-size Boolean separator, which Cavalar-Oliveira converts to a promise cover:
\[
\rho_{\rm prom}\le O(S_{\rm rect}).
\]
Together, the usable chain is
\[
q=\rho_{\rm prom}\le O(S_{\rm rect})\le O(q^3/\log q).
\]
Consequently, the current generic route needs
\[
S_{\rm rect}>N^{3+3\epsilon}/\log N
\]
to force \(q>N^{1+\epsilon}\). A direct q lower bound avoids this loss. Alternatively, the AND-only route needs \(D_{\cap}>N^{2+2\epsilon}\). The ceilings \(\rho_w\le N-1\), \(\rho^*=O(N)\), and \(\rho(\mathcal H)=O(N\log|\mathcal H|)\) concern distinct restricted regimes; they are not a universal cap on \(\rho_{\rm prom}\).

Primary model sources: [Sokolov, Dag-like Communication and Its Applications](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download); [Garg, Göös, Kamath, and Sokolov, Monotone Circuit Lower Bounds from Resolution](https://theoryofcomputing.org/articles/v016a013/v016a013.pdf); [Cavalar and Oliveira, Boolean Circuit Complexity and Two-Dimensional Cover Problems](https://www.dcs.warwick.ac.uk/~igorcarb/documents/papers/CO25.pdf); [Nakayama and Maruoka, Loop Circuits and Their Relation to Razborov's Approximation Model](https://doi.org/10.1006/inco.1995.1083); [Amano and Maruoka, The Monotone Circuit Complexity of Quadratic Boolean Functions](https://doi.org/10.1007/s00453-006-0073-0).

## Short circuit descriptions and the universal-DAG test

Let \(D_{s_1}\) be descriptions of circuits of size at most \(s_1\), and \(G(d)=\mathrm{TT}(C_d)\). Lifting every Alice rectangle side through \(G\) turns a table-DAG into a description-DAG without changing vertices. Conversely, choose one description \(\sigma(w)\) for each \(w\in Y\) and restrict any description-DAG to \(\sigma(Y)\); this gives a table-DAG with the same graph. Thus the minimum rect-DAG sizes on descriptions and tables are equal.

Sending d is still a useful bit protocol: Bob locally evaluates its circuit and scans for a mismatch. But a binary decision tree that first distinguishes d has exponentially many possible description transcripts. To merge them into a DAG, every merged state must handle the full product hull of all incoming row and column histories. If \(K_v\) is the set of mismatch coordinates below a state with rectangle \(A_v\times B_v\), its necessary safety condition is
\[
\pi_{K_v}(A_v)\cap \pi_{K_v}(B_v)=\varnothing.
\]
This condition is exact for output support, but it gives no aggregate vertex lower bound: internal exclusions can overlap, and C-80/C-160 are near-linear counterexamples to coarse local-capacity arguments. A direct minterm separator costs \(N\,2^{O(s_1\log(n+s_1))}\); no near-linear universal DAG is known.

**Falsification result:** any proposed \(N^{1+o(1)}\) description-aware DAG would, by the section argument, already be an \(N^{1+o(1)}\)-size separator for the actual low/high promise. That would refute the desired superlinear \(\rho_{\rm prom}\) route using the reverse transfer. The existence of short individual descriptions alone neither constructs that DAG nor rules it out.

## C-214 theorem: direct counting separates generic fusion closure from cyclic rectangle search

This is a direct count in the native closure syntax; it improves on merely passing through a generic circuit-unrolling bound.

For an arbitrary Boolean function \(f:\{0,1\}^N\to\{0,1\}\), set
\[
Y_f=f^{-1}(1),\qquad Z_f=f^{-1}(0),
\]
and let \(q_f\) be the minimum number of fusion pairs covering this partition promise.

For one q-rule closure, its entire dependence on an anchor \(w\) is captured by:

* two seed clauses \(A_i(w),B_i(w)\), each an OR of a subset of the \(2N\) signed literals \([w_k=b]\);
* two predecessor subsets \(P_i,R_i\subseteq[q]\), specifying the AND/OR recurrence
  \[
  x_i^{(t+1)}=
  \left(A_i\vee\bigvee_{j\in P_i}x_j^{(t)}\right)
  \land
  \left(B_i\vee\bigvee_{j\in R_i}x_j^{(t)}\right);
  \]
* a subset \(O\subseteq[q]\) of empty-carrier rules, with output \(h_Q(w)=\bigvee_{i\in O}x_i^*(w)\).

The clauses arise from the endpoint slice sets \(S(E_i),S(H_i)\), the predecessor subsets from carrier containment, and \(O\) from which intersections are empty. Arbitrary semantic endpoints do not add other anchor-dependent data to this recurrence.

There are at most
\[
2^{4Nq}\cdot 2^{2q^2}\cdot 2^q
=2^{4Nq+2q^2+q}
\]
such abstract systems with q rules. This upper count may include unrealizable data, which only makes the bound safer. A successful cover of the partition \((Y_f,Z_f)\) outputs \(h_Q=1\) on \(Y_f\) and \(0\) on \(Z_f\); since these sets partition the whole cube, \(h_Q=f\) exactly.

Let \(Q_0=\lfloor 2^{N/2-1}\rfloor\). The number of functions representable by any system with at most \(Q_0\) rules is bounded by
\[
(Q_0+1)2^{4NQ_0+2Q_0^2+Q_0}
=2^{\,2^{N-1}+o(2^N)}
<2^{2^N}
\]
for all sufficiently large N. Since there are \(2^{2^N}\) Boolean functions on N-bit inputs, some f has
\[
q_f>Q_0=\Omega(2^{N/2}).
\]
This is a rigorous exponential native-fusion lower bound for some artificial partition promise. By C-213, the very same promise has an unrestricted cyclic product-rectangle mismatch protocol with at most \(5N\) states. Hence there is no general polynomial-overhead transformation from that broad cyclic rectangle model to the fusion closure model.

### What the count teaches, and why it does not transfer to Gap-MCSP

The structural reason for the generic separation is now explicit: a q-rule closure has only \(O(qN+q^2)\) bits of *effective state-description information*—seed-literal incidence and predecessor/empty-state incidence—even though each endpoint is an arbitrary semantic subset of \(Z_f\). A cyclic rectangle protocol has free independent predicates on its two parties and does not pay to describe these unary closure-state signatures.

This does not lower-bound the actual \(\rho_{\rm GapMCSP}\). Counting over all Boolean f proves that some partition is hard, not that the one structured sparse-envelope promise \(Y=\mathrm{SIZE}(s_1), Z=\mathrm{SIZE}(s_2)^c\) is hard. The medium band also means a C-75 separator is an arbitrary extension of the prescribed labels, not a fixed total function. Transferring the theorem would require a promise-preserving encoding that makes every separator expose a hard family of closure outputs. No such encoding is known; this is the same hard-image/envelope bottleneck seen in the failed lifting attempts.

## Disposition and next proof target

C-214 is a Tier-4 model-separation theorem and a useful falsification result for generic cyclic-to-fusion compiler claims. It is not a Tier-1/2/3 result for the actual promise. Keep the active target at O-141: prove a quantitative, product-hull-safe Q-exit/tail tradeoff for arbitrary acyclic rect-DAGs on \(Y\times Z\), or construct a near-linear separator and close that route. A new route must beat the exact transfer losses above and retain C-80/C-160 as counterchecks. No superlinear actual-promise DAG/cover bound or P-versus-NP proof has been obtained.

## C-215 continuation pointer

A state-local Q-exit overlap graph yields a proved label-separation condition and the root tail-support bound, but its edge count does not aggregate through arbitrary alternating states. See `research/C215_Q_EXIT_GRAPH_AUDIT_2026-09-27.md` for the proof, attempted flow invariant, and literature boundary.

## C-216/C-217 continuation — profile inequality and universal-scan falsification

C-216 sharpens the state-local projection count to `r_v*2^(N-|Q|-t_v)<=M2+Delta_v`, with `r_v` common Q-signatures and `Delta_v` omitted high columns. The root support bound gains `log r_Q`. At Alice splits the deficit is available independently to each child; at Bob splits the summed bound pays `|Z|`. Neither transition yields a useful global charge.

C-217 tests the direct universal circuit-evaluation scan. It proves that any fixed-order mismatch scanner has at least `2^(Theta(s1))` states: C-212 uniform shattering realizes all short prefixes, high completions exist for each, and product-rectangle safety prevents merging distinct matched prefixes when passed coordinates cannot be revisited. The theorem is a subclass lower bound only. It does not constrain arbitrary adaptive/revisiting rect-DAGs or change `rho_prom<=O(S_rect)<=O(q^3/log q)` and the required target `S_rect>N^(3+3epsilon)/logN`.

The exact model comparison, relation formalization, and both transformation directions remain as audited in C-214. Short description transmission gives small communication bits but not a shared DAG; direct enumeration still costs `N*2^(O(s1 log(n+s1)))`. O-141 remains active at the general product-hull/Q-exit charge or a near-linear separator. No actual-promise superlinear DAG/cover lower bound or P-vs-NP proof has been obtained. Full new proof: `research/C217_ORDERED_SCAN_WIDTH_2026-09-27.md`; C-216 details: `research/C216_COLUMN_DEFICIT_PROFILE_2026-09-27.md`.


## C-223 adaptive selector pointer

An adaptive procedure that outputs a size-`s1` circuit for each low table gives a separator after all N addresses are verified, at cost `O(R+N s1 log(s1+n))` for selector size R. The reverse direction is not automatic: a separator need not synthesize a circuit, and a general rect-DAG need not expose one. Treat explicit signature selection as a search-MCSP-style sufficient condition only; do not replace O-141 with a selector-hardness claim. Exact statement and caveats: `research/C223_ADAPTIVE_SIGNATURE_SEARCH_MCSP_BOUND_2026-09-27.md`.

**C-217 scope correction.** The exponential state theorem only applies to fixed-order scans that halt at the first mismatch. It does not rule out deferred-output scans or general rect-DAGs. Any next step must test whether such protocols can safely merge histories using later mismatches; no unrestricted lower bound is claimed.


## C-218 continuation ? parameterized certificate geometry

C-218 tests the deferred-output state after a monotone restriction to `Y'=SIZE(N^gamma)`, `gamma<beta`. This restriction is legitimate for separator lower bounds because `SepCirc(Y,Z)>=SepCirc(Y',Z)`. The resulting original-promise separator bound can then be combined with the existing cover-to-DAG compiler; no monotonicity claim across different closure ground sets is needed. The stronger gap gives `d(Y',Z)=Omega(N^beta)` against only `log|Y'|=O(N^gamma n)` description bits. Thus every high z has an `o(N)`-coordinate set hitting all low disagreements. A separate Sauer?Shelah argument gives a fixed block of `O(N^gamma n)` coordinates with at least a quarter of patterns absent from the low projection; those patterns have high completions and every pair retains a large off-block mismatch set.

This separates three resources: a per-column certificate, a common-block certificate for a constant fraction of high columns, and the cost of routing to a signed mismatch. Only the first two are proved. `Q_z` is not a shared state label, and local projection disjointness does not construct a product-rectangle selector. The projected block problem is the next test; O-141 and the standard-DAG transfer threshold remain open.

## C-220 shared-DAG audit pointer

C-220 gives the explicit plain-mismatch and Q-path relations, the promise separator/rect-DAG proof in both directions, the description-space section argument, and the current q-to-DAG loss. It also corrects the triangle-DAG order and records why the universal description scan and interval binary search do not automatically share states. The exact current obligation remains a global product-hull charge or a near-linear separator; no new actual-promise bound follows. See `research/C220_SHARED_DAG_FRONTIER_2026-09-27.md`.


## C-221 seed-feature/readout pointer

C-221 proves that a successful Q's seed clauses already separate every low/high pair in product order, but the minimum subcube-cut feature family is at most 2N. Thus feature-only counting cannot give superlinear q; the remaining native-closure target is readout interaction/paired-support reuse. Full proof and O-141 sharpening: `research/C221_SEED_FEATURE_VS_CLOSURE_READOUT_2026-09-27.md`.



## C-222 gate-signature route pointer

C-222 proves that a fixed menu of signatures with at most `N^beta` cells needs `2^(Omega(N^beta))` items to factor every low t-sparse point indicator. Thus the C-115 fiber-variation witness cannot be universalized by a polynomial menu. It remains open whether circuit-dependent signatures can be exposed and shared adaptively in a product-hull-safe DAG. See `research/C222_FIXED_SIGNATURE_MENU_LOWER_BOUND_2026-09-27.md`.


## C-241 shared-DAG priority pointer

The latest user instruction returns the primary focus to standard acyclic rect-DAG sharing. C-241 re-audits the exact relation and models, proves description-space size invariance, records the direct and restriction-profile universal constructions and their limits, adds the Sokolov PLS comparison, and checks C-240's empty-root seed normal form against the rank-layer compiler. No arbitrary-DAG lower bound or near-linear separator was obtained. See `research/C241_SHARED_DAG_DESCRIPTION_INVARIANCE_2026-09-27.md`.



## Latest priority pointer after C-242

The newest user attachment (27 September 2026, after C-241) restores native cyclic fusion closure as the primary route. Continue O-153 certificate sharing/splicing and the full-promise near-linear cover search; O-152 standard rect-DAG work is secondary unless it improves the compiler or yields a direct q-invariant. C-242 records the exact finite antichain grammar, high-side blocker path, compatible-interval soundness law, and a fixed-order prefix-cover upper construction that is exponential by shattering. No q-charge or near-linear cover follows. See research/C242_NATIVE_CERTIFICATE_ANTICHAIN_AND_BLOCKER_PATH_2026-09-27.md.


## C-243/C-244 native-closure continuation

The active priority is O-153 native certificate sharing, not standard DAG refinement. C-243 proves proof-cylinder containment in the state carrier and a local packing inequality; correlated carriers stop the obvious additive potential. C-244 gives the exact global factorisation Acc_Q=union_i([P_i] intersect [K_i]), with q safe state zones covering all low tables and excluding all high tables. This is the cleanest current expression of global readout sharing, but no bound on a zone's low-circuit mass in terms of q is known. Continue with joint context/proof grammar complexity or a full-promise near-linear cover; keep C-228/C-234 hostile checks. No superlinear native lower bound or P-vs-NP proof has been obtained.


## C-245 marked context grammar

The C-244 state zones can be generated by an antichain one-hole grammar. A context hole propagates through one E/H predecessor branch, with an ordinary proof on the other. If a context and proof both match an input, cycle deletion on the hole path and rank-minimal sibling proofs preserve zone membership with context height at most 2q. This gives a joint q-rule representation with q^2 context-family labels; the antichain contents may be exponential, so it is not a lower bound. Next seek a q-bounded invariant of the context/proof join tensor or a full-promise near-linear native cover. See C-245; no superlinear fusion result or P-vs-NP proof has been obtained.


## C-246 certificate-count calibration

In the C-234 repeated-block family, any safe support cylinder covers at most 2^(kappa_square(s2)/r)=2^(o(s2)) diagonal anchors, so an exponential number of proof supports is necessary. A q-state grammar nevertheless has at most q*2^q*(2N+q)^(2q) ranked witness DAG certificates. This yields only q log(N+q)=Omega(s2), below the known linear floor. Raw certificate counting is therefore retired as a route to superlinear q; continue with semantic context/proof cross-join geometry. See C-246.


## C-247 multi-hole splice budget

Simultaneous substitution at disjoint occurrences is accepted whenever the full support union is consistent. Private coordinate regions where associated anchor completions have injective projections turn a product of choices into distinct accepted tables, bounding total replacement entropy by log|SIZE(s2)|. C-234's block-isolation premise yields 2^N hybrids and violates this budget; diagonal equality survives by context fingerprints. The new lower-bound target is a q-sensitive dichotomy between large compatible splice products and expensive overlap organization. No q-charge follows from entropy alone. See C-247.


## C-248 blocker-rectangle continuation

For each native state i, the low inputs activating it and high inputs on which it is inactive define a product rectangle R_i in Y×Z. Output rectangles cover the full promise relation. If a high input blocks one side of i, every low input in that rectangle has a witness on the same side; a seed witness gives a signed mismatch rectangle and a predecessor witness gives R_j. Pair-specific routes terminate by the low input's activation rank. This is the exact global cross-pair consequence of reusing a native state.

The raw rectangle measure does not help: all disjoint promises have a 2N signed-mismatch cover. An independent unrolling gives an O(q²)-gate monotone separator extension only in the unbounded-fan-in gate-count model; its wire count remains O(q²(N+q)). There is no actual-promise lower bound in either model. Continue the native recursive routing charge and the independent near-linear full-promise cover search. Full definitions and caveats: research/C248_BLOCKER_RECTANGLES_AND_MONOTONE_EXTENSION_COMPILER_2026-09-27.md.


## C-249 output-root normalization

In the actual OPS regime, the high side intersects every signed half-cube. For each accepted low table, a minimum-rank active empty-carrier root therefore has both endpoints nonempty: an empty endpoint cannot contain a seed slice, and a predecessor carrier contained in it would be an earlier empty root. Each such root contains fixed high witnesses on both disjoint endpoints, which block opposite sides. Combining C-240's two-coordinate seed-vocabulary lemma, the root's direct seed branch is at most a one-bit complementary selector, and every proof must continue into a predecessor. This gives a fixed-witness root-to-escape incidence relation, but no charge on how many low tables each predecessor serves. Full proof and exact limitations: research/C249_BIBLOCKED_OUTPUT_ROOT_NORMAL_FORM_2026-09-27.md.


## C-250: one-sided safe escape cylinders

For a seedful minimum-rank root and a low anchor matching direct literal (k,b), the opposite-side proof must use a predecessor. By C-243, each high completion of a predecessor support lies in its carrier; the root's matching high half-cube is excluded from that carrier. Thus the bit-b half of the support cylinder is wholly in SIZE(s2), and its free width is at most ceil(log2|SIZE(s2)|)+1. This is a conditional local cap, not a state lower bound: repeated-block cylinder capacity does not overcome exp(O(q log(N+q))) witness-DAG count. Seedless roots remain open. Resume with a global cross-root context/proof reuse charge or a near-linear full-promise cover. See research/C250_ONE_SIDED_SAFE_ESCAPE_CYLINDERS_2026-09-27.md.


## C-251: seed-or-pair root escape normal form

Every accepted low at a normalized empty root has one of two proof forms. If a direct root seed matches, the opposite predecessor support is half-safe as in C-250. If no direct seed matches, both sides use predecessor supports; their consistent union cylinder preserves the accepting root derivation, so it lies wholly in SIZE(s2) and has at most floor(log2|SIZE(s2)|) free coordinates. This covers seedless roots and missed-seed branches locally. Repeated-block projection gives at most 2^((kappa+1)/r) anchors per selected one-support or paired-support signature.

This closes the local support-capacity gap, not the state-count gap. Counting paired proof DAGs changes the existing exp(O(q log(N+q))) bound only by constants in its exponent. Continue with the cross-root incidence/compatibility charge or the N polylog N cover counter-program. Full note: research/C251_ROOT_ESCAPE_SUPPORT_DICHOTOMY_2026-09-27.md.


## C-252: state-conflict readout

Collapse all paired predecessor signatures by state identity. For each empty output root, the cross-product of its E/H predecessor sets gives directed conflict pairs (j,k). A high table cannot activate both: by C-243 it would belong to both disjoint endpoints. A root seed on one side and an active opposite predecessor similarly give a high-forbidden state/literal incidence. Conversely each accepted low activates one of these patterns. The conflict relation has at most q^2 edges and there are at most 2qN seed/state incidences, giving a depth-two readout of at most q^2+2qN terms over the q least-fixed-point predicates and raw table bits.

This is an exact cross-root quotient. The readout has q^2+2qN terms, which is O(q^2) under the existing OPS floor q=Omega(N); compiling the predicates by unrolling remains at the C-248 scale. Independent-set/profile counting and readout size alone do not lower-bound q. The unresolved target is activation-fibre geometry for the actual promise or an N polylog N full-promise cover. Full statement and limitation: research/C252_STATE_CONFLICT_GRAPH_READOUT_2026-09-27.md.

## C-253: marker-subcube localization of activation fibres

An exact state profile containing a conflict edge is wholly low. For an independent profile sigma, let B_sigma be the direct-seed literals incident to its active states. Low tables in the fibre must match at least one such literal; high tables must avoid all of them. Hence the high fibre lies in a subcube fixing r_sigma coordinates and has size at most 2^(N-r_sigma), unless both polarities of a coordinate are marked, which makes it empty.

Summing high fibres gives one realized profile with r_sigma<=log2(I)+o(1)<=q+o(1), where I is the number of independent profiles represented on U. This does not force any low anchor to use that profile. Continue by seeking a closure-specific coupling between low-output profiles and high fibres under coordinate flips/partial supports. No q-bound follows from the entropy estimate. Full proof: research/C253_CONFLICT_PROFILE_FIBRE_SUBCUBES_2026-09-27.md.

## C-254: partial-support hazard boundary

On partial supports, state activation is monotone. If a partial support already activates a C-252 conflict pair or a state together with an incident seed literal, the corresponding empty output root activates on every completion, so the whole cylinder is low. Thus every low table's first hazardous prefix along any coordinate order has width at least N-log2|SIZE(s2)|.

C-254's chain-event argument alone does not locate the first hazard. Correction: a selected C-252 readout witness has a finite ranked proof DAG with at most q state labels, at most two seed leaves per state, and at most one extra marker literal. Its hazardous support has width at most 2q+1, yielding q >= (N-log2|SIZE(s2)|-1)/2. This is only a linear floor and is weaker than the existing N-o(N) floor. Do not claim that C-254 yields no q-bound, or that an individual state has an unbounded support independent of q. Full correction: research/C254_PARTIAL_SUPPORT_HAZARD_BOUNDARY_2026-09-27.md.


## C-255 — Shared-DAG priority resumed

The user's latest attached instruction makes standard acyclic product-rectangle DAGs primary again. C-255 re-audits the exact plain-mismatch and Q-path relations, the nearest DAG/loop/fusion models, the q-to-DAG loss, reverse separator-to-cover transfer, description-space invariance, and the strongest direct description-enumeration separator. It identifies the precise product-hull non-shareability condition but obtains no global aggregation. A common-translate lemma now maps every low base table to a high table, resolving the hard-image existence condition for source reductions; the unresolved condition is that every signed mismatch rectangle decode to a valid source answer. Direct universal evaluation remains exponential; C-217 only rules out fixed-order first-mismatch scans. Continue with an adaptive/revisiting universal-DAG attempt or an OPS-specific residual-state lower bound, while preserving the threshold `S_rect>N^(3+3epsilon)/log N` needed through the known compiler. Full report: `research/C255_SHARED_DAG_ROUTE_RESTART_2026-09-27.md`. No actual-promise superlinear bound or P-vs-NP proof.
