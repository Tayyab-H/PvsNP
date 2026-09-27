# Fusion closure game: exact state and proof frontier — 26 September 2026

## Purpose and target

The active sufficient route is the Cavalar–Oliveira fusion/intersection route for the exact Gap-MCSP promise. A superlinear lower bound on the joint cyclic cover complexity would imply the corresponding arbitrary-circuit lower bound, then \(NP\not\subseteq P/poly\) by OPS magnification and \(P\ne NP\). The transfer is established; the superlinear bound is open. This note makes the per-anchor closure process explicit and records what the present evidence does and does not support.

## Exact closure recurrence

Let \(U\) be the high-complexity side, let \(w\notin U\) be a low anchor, and write its nonempty matching literal slices as \(L_{w,k}=\{z\in U:z_k=w_k\}\), \(1\le k\le N\). Let
\[
Q=((E_i,H_i))_{i=1}^q,\qquad T_i=E_i\cap H_i.
\]
The initial family is the upward closure of the \(L_{w,k}\). Close it under the listed rules: whenever \(E_i,H_i\) belong to the family, add \(T_i\), then take upward closure again. Denote the least resulting family by \(\mathcal C_Q(w)\).

For each rule define
\[
a_i(w)=1\iff (\exists k)\ L_{w,k}\subseteq E_i,\qquad
b_i(w)=1\iff (\exists k)\ L_{w,k}\subseteq H_i,
\]
and the fixed containment sets
\[
P_i=\{j:T_j\subseteq E_i\},\qquad R_i=\{j:T_j\subseteq H_i\}.
\]
Starting with \(x_i^{(0)}(w)=0\), iterate
\[
x_i^{(t+1)}(w)=
\left(a_i(w)\lor\bigvee_{j\in P_i}x_j^{(t)}(w)\right)
\land
\left(b_i(w)\lor\bigvee_{j\in R_i}x_j^{(t)}(w)\right).
\tag{1}
\]
Then \(x_i(w)=1\) at the least fixed point exactly when \(T_i\in\mathcal C_Q(w)\). The closure derives \(\varnothing\) exactly when some fixed-point-active rule has \(T_i=\varnothing\). If no empty set is derived, \(\mathcal C_Q(w)\) is itself a proper semi-filter above \(w\) preserved by every pair in \(Q\). Thus \(Q\) covers all semi-filters above every low anchor exactly when (1) derives an empty consequence for every low anchor.

**Proof.** At stage \(t\), the generated sets are the literal slices and the \(T_j\) with \(x_j^{(t)}=1\); membership in their upward closure means that at least one of these generators is a subset. Hence \(E_i\) belongs exactly when \(a_i\lor\bigvee_{j\in P_i}x_j^{(t)}\), and similarly for \(H_i\). Rule \(i\) adds \(T_i\) precisely when both tests hold, giving (1). The map is monotone on \(\{0,1\}^q\); iteration from zero yields its least fixed point. At most \(q\) state bits can change from zero to one, so the iteration stabilizes after at most \(q\) strict rounds. If the generated family excludes empty, upward closure makes it nonempty, excludes empty, contains all required slices, and is closed under each rule; this is the promised counterexample semi-filter. The converse follows because every semi-filter preserved by \(Q\) contains every stage of the least closure.

## What the anchor inputs look like

For any endpoint \(E\subseteq U\), let
\[
S(E)=\{(k,b):U\cap\{z:z_k=b\}\subseteq E\}.
\]
Then its initial input to (1) is the clause
\[
a_E(w)=\bigvee_{(k,b)\in S(E)}[w_k=b].
\tag{2}
\]
If \(E\ne U\), \(S(E)\) contains at most one polarity for each coordinate: containing both slices would imply \(E=U\). Thus every rule contributes two disjunctive anchor predicates, while all \(P_i,R_i\) are fixed endpoint-containment relations. Endpoints have no description-cost restriction, so these relations must be treated as semantic data, not as short encoded objects.

Equation (1) is therefore a positive cyclic AND/OR system with clause-valued inputs. Equivalently, it is a finite alternating proof game: a rule is proved active by producing a support for each of its two sides; on each side one may use a matching literal slice or an already proved rule. A finite proof tree exists exactly for least-fixed-point activation. This language gives a precise target for a cross-anchor invariant, but no such invariant has been proved.

## A contradiction cannot be seeded at round one

The actual high side \(U=Z\) two-wise shatters truth-table coordinates for the OPS parameters: every assignment to two distinct coordinates extends to \(2^{N-2}\) tables, while the total number \(M_2\) of tables of circuit complexity at most \(s_2=N^\beta\) is \(2^{o(N)}\). Hence every such two-coordinate cylinder contains a member of \(Z\), for fixed \(\beta<1\) and large n.

If \(T_i=\varnothing\), then \(a_i(w)\land b_i(w)=0\) for every low anchor w. Otherwise a matching slice \(L_{w,k}\subseteq E_i\) and another \(L_{w,\ell}\subseteq H_i\) would exist. If k and \(\ell\) differ, two-wise shattering supplies \(z\in U\) in both slices, contradicting \(E_i\cap H_i=\varnothing\). If k=\(\ell\), the same matched slice is nonempty and lies in both endpoints, again a contradiction. Thus an empty-consequence rule cannot activate directly from the initial literal slices.

More generally, if an empty consequence first activates at round t, unfold its least-fixed-point proof into a binary AND/OR tree and choose one matching literal at each seed leaf. The tree has at most \(2^t\) leaves. Their matching slices must have empty intersection in U, so by the same counting argument at least \(N-\log_2 M_2\) distinct coordinates are fixed. Therefore
\[
t\ge \log_2(N-\log_2 M_2)=\log_2N-o(\log N).
\]
This is a proof-depth lower bound, not a pair-count lower bound: a proof can have \(N-o(N)\) leaves but only logarithmic depth and \(N-o(N)\) total rules. It sharpens the lesson that any contradiction must grow from nonempty intermediate intersections before its final empty rule.

## Adaptive cross-anchor game and candidate potential

For a partial pair list \(Q_t\), define the survivor set
\[
Y_t=\{w\in Y:\mathcal C_{Q_t}(w)\text{ does not contain }\varnothing\}.
\]
The pair designer wins when \(Y_t=\varnothing\). The adversary's canonical witness at a surviving anchor is \(\mathcal C_{Q_t}(w)\) itself. This witness depends on the current pair list; that dependence is the central adaptive feature.

A useful state-aware distance is
\[
\delta_Q(w)=\min\{|R|:\mathcal C_{Q\cup R}(w)\ni\varnothing\}.
\]
The one-anchor chain gives \(0\le\delta_Q(w)\le N-1\) for a survivor. Adding one pair changes each \(\delta_Q(w)\) by at most one: monotonicity gives one direction, while any extension that kills after \(Q\cup\{p\}\) can be replayed after \(Q\) by first adding \(p\). This absorbs arbitrary within-anchor cascades into the distance definition.

At the empty list, the project leaf-count theorem C-03 gives the stronger pointwise start
\[
\delta_{\varnothing}(w)\ge N-\log_2 M_2-1=N-o(N)
\]
for each low anchor, where \(M_2\) counts tables of complexity at most \(s_2\). A tempting sufficient lemma would be to find a probability distribution \(\mu\) on low anchors and an \(\epsilon>0\) such that, for every partial list \(Q\) and every semantic pair \(p\),
\[
\mathbb E_{w\sim\mu}\!\left[\delta_Q(w)-\delta_{Q\cup\{p\}}(w)\right]\le N^{-\epsilon}.
\tag{3}
\]
If (3) held, telescoping along any list that kills all anchors would require at least \((N-\log_2M_2-1)N^\epsilon=N^{1+\epsilon-o(1)}\) pairs. However, C-73 refutes (3) already at \(Q=\varnothing\), for every choice of \(\mu\).

**Proof of the refutation.** Write \(G_{k,b}=U\cap\{z:z_k=b\}\), and let \(d_0=\lceil N-\log_2M_2\rceil\). For each w choose one minimum literal-slice certificate \(S_w\) whose intersection in U is empty. Its size \(d(w)\) satisfies \(d(w)\ge d_0\), while the exact one-anchor theorem gives \(\delta_{\varnothing}(w)=d(w)-1\). For a random coordinate pair \(\{k,\ell\}\), the \(\mu\)-mass of anchors with both coordinates in \(S_w\) averages at least \(\binom{d_0}{2}/\binom N2=1-o(1)\). Hence some \(\{k,\ell\}\) has mass at least this amount. Split those anchors into the four patterns \((w_k,w_\ell)\); one pattern \((b,c)\) has mass at least \(\theta/4\), where \(\theta=\binom{d_0}{2}/\binom N2\). Add the single pair \(p=(G_{k,b},G_{\ell,c})\). For every anchor in that pattern class whose chosen certificate contains k and \(\ell\), p precomputes the intersection of those two certificate slices; intersecting the remaining \(d(w)-2\) slices uses \(d(w)-2\) further pairs. Thus \(\delta_{\{p\}}(w)\le d(w)-2\), and C-69's one-pair bound makes the decrease exactly one. Consequently
\[
\sup_p\mathbb E_{w\sim\mu}[\delta_{\varnothing}(w)-\delta_{\{p\}}(w)]
\ge \theta/4=(1-o(1))/4.
\]
The \(\delta_Q\) distance remains valid, but a static weighted sum of it cannot yield a superlinear lower bound by a uniform one-pair marginal estimate. The first intersection is highly shareable. The raw survivor count also has no useful bound: C-09 shows a pair can hit at least N selected filters. Counting endpoint descriptions is invalid because endpoints are unrestricted.

### Attempt to amplify shared intersections by blocks

For a fixed block of k coordinates, one can precompute the intersection for every one of its \(2^k\) anchor patterns with \((k-1)2^k\) pair rules. This compresses a local certificate from k literal leaves to one block state, and the four-pattern k=2 case is exactly the constant-fraction saving in C-73. But combining two such blocks requires pattern-specific intersections: the direct construction uses \(2^{2k}\) rules for the four-coordinate state table. Repeating over a balanced hierarchy makes the top state table exponential in the block width. Replacing all pattern-indexed states by their unions loses anchor conditioning—the union over every pattern on a block is U. Restricting to patterns realized by low anchors cuts the top table to at most \(M_1\), still exponential in \(N^\beta\), and is only the brute finite-family route.

This is a failed amplification as a route to \(N^{1+\epsilon}\), not a lower bound against alternative sharing. It identifies the missing operation: combine block states without either enumerating anchor patterns or merging their semantic regions back into U.

## Failed shortcuts and the exact lesson

1. **Static family rounding is not a global cover theorem.** If a fractional pair cover of a fixed family of \(R\) semi-filters has total weight \(W\le 8N+1\), sampling \(k=\lceil W(\ln R+1)\rceil\) pairs covers that fixed family. This is a conditional rounding lemma; the project-supplied \(8N+1\) ceiling still needs its original proof attached to the claim ledger. The global \(\rho\) problem ranges over every semi-filter extension, not one chosen filter per anchor. For a currently surviving anchor, a sampled pair may merely add a new nonempty \(T_i\); it need not derive empty. The next adversarial semi-filter can then be the larger closure. So rounding the minimal literal-generated filter per anchor is not sufficient.
2. **Raw per-rule influence is false as a lower-bound potential.** A rule may alter many anchors at once (C-09). Any valid potential must measure adaptive closure progress after the pair's cascade, not count anchor-rule incidences.
3. **Per-anchor hardness saturates at \(N-1\).** Every anchor has a chain cover using at most \(N-1\) pair rules. Superlinear growth must arise from global non-shareability across anchors; strengthening the single-anchor leaf count cannot reach it.
4. **Threshold and balanced partitions collapse.** The checked four-point block family has a two-pair cover for every tested threshold and coordinatewise monotone aggregation. Hamming-ball majority filters admit one common pair. These are falsification tests for proposed block amplification, not evidence about all semi-filters.

## Artificial integrality-gap controls

- Shared-core graph-edge filters reduce to graph cuts. For \(K_m\), the integral cover is \(\lceil\log_2m\rceil\), while a random cut gives fractional cost about 2. This supplies a logarithmic gap but not the required \(N^{1+\epsilon}\) scale or the anchor-literal condition.
- Co-singleton filters have exact cover \(\binom N2\), but their fractional cover is equally large and the example lacks the anchor condition. Large integral complexity by itself is therefore insufficient.

No artificial construction currently satisfies all three ceilings—per-anchor at most \(N-1\), global fractional \(O(N)\), and global integral \(N^{1+\epsilon}\)—with arbitrary semantic endpoints and anchor literals. A useful construction must also survive adding any semantic pair and recomputing the entire least closure.

### Relaxed random set-cover gap and partial semantic encoding

The three numerical ceilings alone are compatible with a large gap. Let \(R=\exp(N^\epsilon)\) anchors each contribute one target filter, and take \(M=R^2\) abstract pair-actions, each covering each target independently with probability \(1/N\). With high probability every target lies in at least \(M/(2N)\) actions, so weight \(2N/M\) on every action gives a fractional cover of total \(2N\). For a fixed k-action list, each target is missed with probability \((1-1/N)^k\); when \(k=cN\ln R\) for any fixed \(c<1\), the expected number missed is \(R^{1-c-o(1)}\). A union bound over at most \(M^k=\exp(O(N(\ln R)^2))\) action lists shows that some target remains uncovered for every such list, since \(R^{1-c}\) dominates this logarithm. Thus the abstract integral cover is \(\Omega(N\ln R)=\Omega(N^{1+\epsilon})\), while the fractional cover is \(O(N)\); the local one-target cover is 1.

There is a partial encoding of an arbitrary incidence matrix on a *restricted catalogue*. Let \(A=G_{1,0}\), \(B=G_{2,0}\), and \(C=A\cap B\); select anchors with first two bits \(00\). For catalogue index j, choose a small same-size set \(D_j\) in the \(11\) quadrant, with the \(D_j\) forming an antichain, and set \(E_j=A\cup D_j\), \(H_j=B\cup D_j\). Then \(T_j=E_j\cap H_j=C\cup D_j\). Choose the \(D_j\) so each \(T_j\) is smaller than every matching literal slice. For anchor w, the upward closure of all matching slices plus any chosen subfamily of the \(T_j\) is a semi-filter; it contains every \(E_j,H_j\), and its membership choices on the antichain \(T_j\) encode arbitrary violations among the catalogue pairs.

The gadget fails as a lower-bound construction because the *unlisted* pair \((A,B)\) has intersection C. Every filter in the encoded family contains A and B but excludes C, so this single pair violates all of them. Adding C to every filter blocks the shortcut but, by upward closure, then forces every \(T_j\) into every filter and destroys the encoded incidence. Thus this is an explicit example of why controlling a chosen catalogue is not enough when endpoints are arbitrary semantic subsets. The random set-cover gap remains a relaxed calibration, not a true fusion realization.

## Universal upper-bound stress test

The candidate \(O(N\operatorname{polylog}N)\) upper bound is not established. Fractional rounding cannot prove it without a finite family of filters whose size has a manageable logarithm, and the set of all proper semi-filters above the anchors is far larger. Nor does a bound for a selected family imply a bound for \(\rho\). A valid upper bound must give one pair list that kills the adaptive closure for every low anchor, despite arbitrary semantic endpoints. Conversely, a lower-bound proof must exhibit a surviving low anchor for every short list; a fixed witness family is only one possible method.

## Ranked next proof work

1. **Potential beyond additive anchor distance (highest value).** The static-\(\mu\) marginal bound for \(\delta_Q\) is false by C-73. The next candidate must charge creation and reuse of intermediate intersection states, so that a pair saving one rule across a constant fraction of anchors is recorded as shared work rather than treated as anomalous progress. Stress-test against C-09, C-73, and the sparse-cube cascade.
2. **Universal \(O(N\operatorname{polylog}N)\) cover search.** Try to construct an explicit global pair list, or prove that all known compression attempts fail because the closure witnesses are \(Q\)-dependent.
3. **Artificial gap model.** Search for a realizable set-cover-like model with the three ceilings and genuine anchor literals; keep graph cuts and co-singletons as calibration controls.
4. **Static fractional/threshold route.** Closed for the tested threshold families and unsuitable as a complete proof without an exponentially large, carefully structured family and a separate argument that handles adaptive closure.

**Status:** the exact closure-game recurrence, a state-aware per-anchor distance, the refutation of its static additive marginal strategy, and the proof-depth floor are established. A potential charging shared intermediate intersections, the required integrality gap, the universal upper bound, the superlinear \(\rho\) lower bound, and \(P\ne NP\) remain open. The finite recurrence cross-check is at [experiment_fusion_closure_recurrence.py](../experiment_fusion_closure_recurrence.py); the sparse-cube exact search is at [experiment_universal_cover_q2_n3_sparse_anchors.py](../experiment_universal_cover_q2_n3_sparse_anchors.py). They verify toy behavior only.


## Continuation: the closure game as a dual-rail intersection circuit

For each rule i, let X_i^(t) be the set of anchors at which T_i enters the closure by round t, and let A_i and B_i be the anchor sets satisfying its two literal-seed predicates. The exact update is

    X_i^(t+1) = (A_i union union_{j:T_j subset E_i} X_j^(t))
                intersect (B_i union union_{j:T_j subset H_i} X_j^(t)).

Each A_i and B_i is a union of signed coordinate half-cubes. Thus a pair list is a positive recursive intersection-union program on anchor space, evaluated at its least fixed point. Let K_Q be the union of X_i^(q) for empty-consequence rules. For every high table z in U, each active T_i contains z by induction, so K_Q avoids U. A list refuting every low anchor therefore computes a promise separator Y subseteq K_Q subseteq {0,1}^N minus U.

This representation is necessary, not a converse. It is monotone in the 2N dual-rail indicators [w_k=0],[w_k=1], restricted to valid one-hot inputs. Unrolling q rounds gives at most q^2 AND gates and 2q^2+O(q) unbounded-fan-in OR gates. Converting every OR to bounded fan-in can cost O(q^2(N+q)); generic bounded-fan-in circuit lower bounds therefore do not transfer with the needed exponent. The useful target is a direct superlinear lower bound on q states in this recursive promise-separator model, or a sharper simulation.

The literature's monotone-circuit conjunctive complexity (minimizing AND gates) is a methodological analogue, not an imported theorem: standard results do not cover the complementary dual rails, recursive least-fixed-point semantics, arbitrary semantic containment network, and this promise separator. A starting reference is [Amano and Maruoka (2006)](https://doi.org/10.1007/s00453-006-0073-0).

The restricted-catalogue incidence gadget also fails concretely. With A=G_(1,0), B=G_(2,0), C=A intersect B, and E_j=A union D_j, H_j=B union D_j, the unlisted pair (A,B) yields C and violates every encoded filter. Putting C into every filter forces all C union D_j by upward closure and erases the incidence choices. The relaxed random set-cover gap remains only a calibration, not a realization in the semantic model.

**Status:** exact activation-set reformulation established (C-74); direct state lower bound, realizability converse, superlinear rho lower bound, and P != NP remain open. The new model is a proof target, not a breakthrough.

## Communication-game stress test (C-75)

The closure proof for a low w against a high z yields a deterministic protocol to find a differing truth-table coordinate. Bob chooses an unsupported endpoint side at z; Alice supplies a support valid at w. A prior-rule support descends to a lower activation rank, and a literal support terminates with a mismatch. The number of visited states is at most q, so communication is O(q log(N+q)).

This does not help the target: Alice can send a size-s1 circuit for w, letting Bob scan z for a mismatch, so the relation has communication cost only O(s1 log s1+log N)=N^(beta+o(1)). That is weaker than the existing local q>=N-o(N) bound. The Karchmer-Wigderson style proof loses the shared-state DAG information; only a direct state/DAG lower bound could be useful.

**Priority update after C-74/C-75:** first target a lower bound on the recursive separator program's state count q, with containment-incidence constraints explicit; second seek a sharper fixed-point-to-circuit simulation; retain global-cover and genuine artificial-gap searches as parallel diagnostics. Do not pursue ordinary communication bits as the main route.

## Seed-feature monotonicity and CNF traps (C-76)

The output depends on an anchor only through the 2q seed predicates. If their truth vector is s, the least fixed point gives a monotone output h_Q(s). Thus, for every low w and high z, some seed clause is true on w and false on z. For each low w, conjoin the nonconstant seed clauses true at w. Every satisfying table has a seed vector coordinatewise above sigma(w), so h_Q would refute it; hence the CNF contains no high table.

A satisfiable m-clause CNF on N truth-table bits has at least 2^(N-m) models: select one true literal per clause at w and fix those at most m coordinates. Since the CNF's models all have circuit complexity at most s2, m>=N-log2(M2)=N-o(N). Equivalently, the hypergraph of matching literal supports of the true seed clauses has transversal number at least N-o(N), since fixing a smaller hitting set would leave a high table while preserving all clauses.

This is a necessary-condition result but only yields q>=N/2, weaker than the known local q>=N-o(N) theorem. A dictionary of both signed unit clauses for every coordinate gives a minterm certificate for every table, so counting the seed features cannot supply the desired superlinear bound. The live target is the state cost of the monotone decoder and its compatibility with endpoint-induced containment relations.


## C-77: cyclic KW / PLS bridge and exact DAG losses (2026-09-26)

The detailed model comparison is in [DAG_FUSION_BRIDGE_2026-09-26.md](DAG_FUSION_BRIDGE_2026-09-26.md).

**Total relations.** For \(Y=\mathrm{SIZE}(s_1)\) and \(Z=\mathrm{SIZE}(s_2)^c\), the signed mismatch search relation on \(Y\times Z\) is total because \(Y\cap Z=\emptyset\). A stronger \(Q\)-dependent relation outputs a path from an empty-consequence rule active on \(w\) to a matching literal that differs on \(z\). It is total exactly when Q refutes every low anchor. The path exists because each rule transition strictly decreases the least-fixed-point activation rank on \(w\).

**New precise bridge.** The active project cover uses \(\Gamma_{\rm prom}=Y\sqcup Z\) and filter universe \(Z\). Its activation sets \(X_i\) form a cyclic monotone circuit with one AND/intersection per fusion pair; all support collection is by OR. The least fixed point is 1 on \(Y\) and 0 on \(Z\), while its medium-band values are unconstrained. Cavalar-Oliveira exact identity \(\rho=D^\circ_\cap\) applies on this promise ground set. A separate full-domain cover has exact low-class characteristic \(1_Y\), but is not the active Gap-MCSP parameter. Cyclic-to-acyclic unfolding gives at most \(q^2\) AND gates. Counting support-routing ORs in a binary-fanin simulation of the active recurrence gives \(O(q^2(q+N))=O(q^3)\), using \(q\ge N-o(N)\).

**Cyclic protocol insight.** The rule states \(R_i=\{w:x_i(w)=1\}\times\{z:x_i(z)=0\}\) are rectangles, and every valid pair at \(R_i\) either reaches a signed mismatch output or a lower-rank \(R_j\). The dependency graph can contain cycles even though every input-specific valid path terminates. A rank-aware loop game is a better exact communication language than an ordinary rect-DAG; a standard DAG still needs unrolling.

**Reverse conversion and its scope.** A DAG for low-versus-high mismatch gives a separator that may accept the medium-complexity band. That prevents an automatic conversion to the distinct full-domain exact cover. It does not block conversion to the active promise cover: on \(Y\sqcup Z\), the separator's 1-set is exactly \(Y\), and C-90 gives \(\rho_{\rm prom}\le O(L)\) for an \(L\)-vertex rect-DAG. The full-domain cover would follow from an exact separator against the entire non-low complement.

**Universal-DAG attempts.** Sending a circuit description proves only a low communication-bit protocol; its tree may have exponentially many nodes. Universal circuit evaluation is joint computation, not a rectangle split. An interval mismatch predicate is generally non-rectangular (the two-bit mismatch matrix on rows/columns 00,11 is anti-diagonal). A direct union bound for a fixed coordinate sample does not beat N at OPS parameters. These failures do not rule out structured shared DAGs.

**Target translation.** A rect-DAG lower bound via the generic binary-fanin conversion would need size above \(N^{3+3\epsilon}\) to force \(q>N^{1+\epsilon}\). In the aligned acyclic conjunctive measure, a lower bound above \(N^{2+2\epsilon}\) for every monotone separator of low from high would suffice through \(D_\cap\le q^2\). No such separator lower bound is known here. See the dedicated report for model definitions, source links, the parity tree/DAG calibration, and the exact next lemma.


## C-157/C-158 continuation - Progress and binary sharing

A tempting O(N)-vertex cyclic mismatch router gives every full-root state one edge to a signed mismatch leaf and one edge to the next state in a cycle. Every pair has a finite accepting route, but also an infinite continuation route. Existential finite-path semantics would trivialize every total search relation, so a cyclic model needs a well-founded input-sensitive progress rule. C-74 supplies one through decreasing activation rank; the root-loop is not a fusion construction.

For an acyclic binary Boolean communication game, if a rectangle A x B is covered by two child rectangles, then either the first child contains all of A or the second contains all of B (after intersecting with the parent). A party can therefore choose a locally valid successor at each node. This is only a local routing fact. It does not bound shared states globally; O-126 asks whether it can combine with C-129's excluded-column inequality without failing on C-130 overlap or C-132's all-row filtered child.

Current fixed-output bounds for plain mismatch remain n-o(1) to O(N^beta) communication bits and N-o(N) to min(2^(O(N^beta)), O(q^3/log q)) standard rect-DAG vertices. A successful q-cover gives a q-state ranked cyclic rectangle graph plus 2N output leaves and O(q^2+qN) possible arcs; converting it to an acyclic binary DAG still has the cubic/log loss. No near-linear universal DAG or superlinear DAG/cover lower bound has been established.

**C-159 source correction.** The local binary rectangle trichotomy is already in Sokolov's circuit-game proof: the parent row side lies in both children (AND), the parent column side lies in both (OR), or one child contains the parent (copy). Thus C-158 is a restatement/corollary, not a novel lower-bound lemma. The live task is still a global quantitative charge across shared states; C-130 and C-132 block direct summation of local constraints.

## C-160 - Threshold calibration narrows the global-charge target

Tested whether C-129's local excluded-column inequality plus the Sokolov AND/OR/copy rule could support a generic superlinear DAG lower bound. A stronger calibration is a symmetric two-tail Hamming promise. Set a=floor(N^beta/n), b=floor(N^beta), let Y_a contain strings of weight at most a or at least N-a, and let Z_b contain strings with b<weight<N-b. Then log2|Y_a|=Theta(N^beta), the non-high set has log2-size Theta(N^beta*n), every pattern on at most a coordinates extends to a low row, promised pairs are separated by Theta(N^beta), every cylinder larger than the non-high set contains a high column, and changing at most a bits of a low row stays non-high. Also Y_a is complement-closed and every coordinatewise Boolean recombination of up to floor(b/a)=Theta(n) low rows remains non-high.

Nevertheless, the separator accepting weight at most a or at least N-a has an O(N log N) fan-in-two circuit. The corresponding rect-DAG and active fusion cover are O(N log N)=N^(1+o(1)). Thus O-126 cannot be solved by generic cardinality/cylinder/projection arguments; it needs finer structure of the actual SIZE classes or a direct ranked-closure potential. This is not an OPS upper bound, a superlinear lower bound, or a P-vs-NP result. Full proof and definitions: bridge section 86.

## C-161 - Affine-balanced calibration and the composition frontier

Augmented C-160's low side with all 2N affine truth tables and its non-high side with their radius-a Hamming neighborhoods. The low/non-high log-count scales and the cylinder completion bound are unchanged, and the promise now includes balanced low rows, complement symmetry, and affine input-permutation symmetry. For an N-bit table u, the distance to the nearest affine truth table is \((N-\max_\ell|\widehat{(-1)^u}(\ell)|)/2\). A Walsh-Hadamard circuit computes this test in O(N log^2 N) gates, so the augmented mismatch DAG and active cover are still N^(1+o(1)).

This kills balance and one structured orbit as sufficient non-shareability features. It does not preserve C-160's arbitrary Theta(n)-row composition closure. The next candidate is that actual SIZE(s1) contains many overlapping bases, including the n input literals, and their size-s2 composition closure; a proof must show why the resulting residual relations cannot share states. C-122 gives an O(N) router for any sufficiently small linear-sized anchor family, while C-123 rules out description syntax alone. No OPS lower bound follows yet.
## C-162 - Shared DAG and basis-count checkpoint

The C-75 mismatch relation is total on Y×Z; the Q-path relation is total exactly for a successful cover. A short circuit description gives O(s1 log s1+log N) communication bits, but description-space and truth-table-space rect-DAG sizes are equal by lift/restrict. Sokolov/GGKS DAGs are acyclic rectangle systems; the fusion object is exactly cyclic intersection complexity and only becomes a standard DAG after the known conversion. Current bounds: q=ρ_prom=D°_cap, S_rect≤O(q³/log q), and ρ_prom≤O(S_rect); target transfer thresholds are unchanged.

The GL(n,2) basis count does not create that many anchors: only N distinct linear forms occur as component rows, and g(Ax) is an ordinary low circuit when its O(n²) basis overhead fits. The affine subfamily against actual Z has an O(N log²N) separator via exact Walsh affine testing. This kills basis-count/affine-orbit charges, not the full nonlinear-composition candidate. No non-shareability theorem, superlinear bound, or P-vs-NP proof was obtained. Details and primary links are in bridge section 88.

The active relation excludes the medium band: compositions known only to fit the \(s_2\) budget need not be Alice low rows and impose no separator constraint. Any continuation of the basis idea must keep its derived rows inside \(Y\) or prove a separate extension transfer.

**C-163 output-capacity refinement.** The C-136 distance gap says every promised pair has Delta=Theta(N^beta/n) valid signed mismatch coordinates. If a total source search problem is encoded partywise into Y x Z, and each mismatch type is refined by at most r output-labelled decoder leaves, then its fractional output-cover number is at most 2Nr/Delta=O(r n N^(1-beta)). This is a necessary test for the C-154 CSP-lifting transfer: large source output-cover complexity forces a large decoder/refinement overhead. It is not a lower bound on S_rect or rho_prom; see bridge section 89.

**C-164 Index geometry.** The C-154 cPHP/Index source has a stronger constraint than output-label count alone: under uniform inputs every monochromatic rectangle for a fixed pigeon-pair answer has measure at most 1/(m^2 d). Therefore any encoding into Delta-separated OPS low/high tables, with r valid decoder rectangles per signed mismatch type, requires r>=Delta m^2 d/(2N). The lifted DAG lower bound may still dominate this cost for large width, so the route remains open; low/high table maps and the full parameter comparison are missing.

**C-165 signed-orientation gap.** The cPHP/Index lifting source has per-row output density at most 1/d. Consequently any full signed-mismatch decoder with fewer than d/2 labelled leaves per mismatch type is impossible; in particular, the fixed one-sided decoder used by the CCC monotone-KW reduction cannot be transferred unchanged to C-75. A larger refinement is not excluded and must be charged together with C-164. This closes only the fixed-decoder shortcut, not O-124.

## C-166 - Recheck of the C-78/C-133 interval scanner

The short-circuit-description objection was rechecked against the existing C-78 universal interval rect-DAG; its size lower bound was already proved in C-133, and its product-hull obstruction is C-110 specialized. At state (I,r), Alice's side fixes w|I=r and Bob's side requires z|I!=r. If a distinct low restriction s has a high extension z_s|I=s, then the union-product hull of the r and s states contains a pair agreeing throughout I. So those states cannot merge if the common descendants may output only inside I. Since point-indicator circuits realize every L-bit pattern on L chosen coordinates for L=O(s1/n), and every such pattern has high extensions whenever 2^(N-L)>|SIZE(s2)|, each fixed-interval subroutine needs 2^L contexts. C-133 already proves that the explicit profile router has (N/L)2^L distinct vertices at that dyadic level.

This is an architecture-specific lower bound, not an OPS lower bound for arbitrary rect-DAGs. A general DAG could route to a mismatch outside I; no normalization is known. The exact q-state object remains the ranked cyclic Q-router, and the best acyclic conversion remains O(q^3/log q). See bridge §92 and O-127.
## C-167 - Interval-normalization calibration

C-160's threshold promise has a near-linear arbitrary separator DAG but forces 2^a restriction contexts in any interval-local scanner, where a=Theta(N^beta/n). This refutes a generic polynomial-loss normalization from arbitrary rect-DAGs to interval-local routers. It does not weaken the actual closure-cover target because the calibration is not the SIZE(s1)/SIZE(s2)^c promise. O-127 is now OPS-specific; otherwise use a state invariant that does not require descendants to output within a fixed interval. Full proof: bridge section 93.
## C-168 - Row-only sampling requires nearly all coordinates

If Alice's selected low table or circuit description determines a candidate set S(w) of mismatch positions before Bob's input is used, then any high z must differ from w on S(w). Otherwise the entire cylinder matching w on S(w) would be non-high. Since the non-high class has M2=|SIZE(s2)| tables, 2^(N-|S(w)|)<=M2 and |S(w)|>=N-log2 M2=N-o(N). This eliminates row-dependent nonadaptive sampling, but not Bob-dependent DAG routing. Full statement: bridge section 94.

## C-170 - One-switch synopsis protocols are ruled out

For Alice-first protocols, the C-80 block code and the high-table cylinder count force at least 2^Theta(s1) distinct recipient frontier states. For Bob-first protocols, low circuits realize every pattern on t=Theta(s1/n) coordinates, so each Bob message class lies in a codimension-t cylinder and at least 2^Omega(s1/n) frontier states are needed. These bounds allow arbitrary shared DAG suffixes but do not cover repeated alternation.

The critical countercheck is C-80 itself: on the block-constant low subpromise, a B-to-A-to-B router has O(N) vertices. Bob finds a block where z varies; Alice's row is constant on that block; Bob outputs a mismatch. Thus the one-switch barriers cannot be added across rounds. The unresolved state invariant must charge circuit-dependent fiber selection. Full proof and quantitative details: DAG_FUSION_BRIDGE_2026-09-26.md, §96; O-129.

**C-172 state constraint update.** At any rect-DAG node, r distinct low-row signatures on k descendant output coordinates generate r disjoint cylinders. Since every high table in these cylinders would agree with some feasible row on all descendant outputs, those high columns must be absent from the state. The *global* count of low tables gives |Z minus B_v|>=r*2^(N-k)-M2, sharpening C-129. At the root, point-minterm patterns imply k>=N+Theta(s1/n)-log M2. This is still N-o(N), and C-135 patching gives a fixed N-Theta(s1) candidate set that hits all mismatches; the unresolved issue is how to route, not support size. No overlap-aware charge across alternating states has been found. See bridge section 98 and O-131/Q129.

**C-174/O-132 resolution.** Any forced Boolean projection of the mismatch output is a union of at most 2N signed mismatch rectangles, hence has a Rect-DL of length at most 2N and one output switch. This cannot reach the superlinear C-75 transfer threshold. The sign-only and coordinate-block-only versions are also simple. A direct rect-DAG lower bound would be a distinct result; see bridge section 100.

**C-175/O-131 refinement.** State conflict sets obey owner-sensitive union/intersection containments, but raw excluded-column volumes are not additive. The C-80 B-to-A-to-B router has m=Theta(s1/n) states each excluding almost all high columns, with Omega(m) overlap, despite O(N) total vertices. A future potential must condition on reachable parent rectangles or actual paths; see bridge section 101/Q131.

**C-176 continuation - conditional mass stress test.** The direct parent-conditioned cross-conflict charge avoids C-175's off-path overlap but fails as a mandatory progress measure: the C-80 router has valid high tables mixed in every block, with a first-coordinate mismatch, whose selected branches avoid each sibling conflict set. The charge is at most path length and can be zero on such a pair. O-131 is narrowed to residual-context non-shareability under product-hull-safe DAG merges; no S_rect/rho/P-vs-NP bound changed. See bridge §102 and Q132.

**C-177 local-PRG check.** The CLKM method extends to a gap separator, but its general-branching-program locality yields only N^(2beta-o(1)) for OPS's small beta, below the existing N-o(N) DAG floor; no model transfer to C-75 rect-DAGs is known. The only direct version asks for an s1-local PRG fooling unrestricted separator circuits, which restates the core obstacle. See bridge §103/Q133; no rho or P-vs-NP bound changed.


## C-178 - Sparse-envelope normal form for shared DAGs
For the C-75 low/high relation, a separator's accepting set is exactly a sparse envelope A with SIZE(s1) subseteq A subseteq SIZE(s2). This makes the C-75 rect-DAG target the circuit complexity of an approximate existential projection over size-s1 descriptions. A universal circuit evaluates one proposed description, but converting that verifier into a one-input separator requires eliminating the description. Direct enumeration costs N*2^(O(N^beta)); the communication protocol that sends d is cheap in bits but retains an exponential one-switch frontier. A merge lower bound must quantify separator complexity for the complete product hull of incoming histories, not just show that coordinate projections are disjoint. Root residual complexity is the original target, so this reformulation provides no lower bound yet. See bridge section 104.



## C-179 - Affine fingerprints need almost full rank
The C-168 coordinate-cylinder bound extends to any per-row affine map L_w(x)=A_wx+b_w. If all high tables must map away from L_w(w), the collision coset w+ker(A_w) lies entirely in SIZE(s2). Hence rank(A_w)>=N-log2|SIZE(s2)|=N-o(N). This blocks one-shot parity sketches, not adaptive nonlinear DAG routing; it does not output a mismatch coordinate or lower-bound rho.



## C-180 - Adaptive parity decision trees cannot be shallow
A separator computed by adaptive affine-parity queries has depth at least N-log2|SIZE(s2)|: the path of any low input is an affine cell with at most |SIZE(s2)| members. This is a tree-depth theorem only. Sharing can reduce an N-deep tree to O(N) DAG nodes in principle, so no C-75 or fusion lower bound follows.



## C-181 - Promise-gap local PRG calculation for branching programs
The STACS 2021 local PRG against nondeterministic, co-nondeterministic, and parity BPs has locality S^(2/3+o(1)). Since a Gap-MCSP separator accepts all low-locality outputs but only a 2^(-N+o(N)) fraction of uniform tables, its size in those models must satisfy S>=s1^(3/2-o(1))=N^(3beta/2-o(1)). This misses the OPS small-beta range and does not apply to unrestricted rect-DAGs. See bridge section 107 and the primary STACS source linked there.


## Shared-DAG continuation C-210 - explicit rank-lift

For each closure rule i let `tau_i(v)` be the first activation round, or infinity. Define `R_(i,r)={w in Y:tau_i(w)<=r} x {z in Z:tau_i(z)=infinity}`. If Q succeeds, a root over the empty-intersection rules covers Y x Z. At a pair in `R_(i,r)`, one endpoint side is absent from z's closure; w's membership in that side has a literal seed (a valid mismatch) or a prior consequence `T_j` whose activation rank is strictly less than `tau_i(w)`. Since `T_j` is contained in the absent side, j is inactive on z. Thus transitions go to `R_(j,r-1)` and the layered protocol is acyclic.

There are q^2 rule/rank states plus O(N) answer leaves. This is a multiway state count only: each state can have O(q+N) support choices, giving O(q^2(q+N)) arcs and cubic-order binary routing when q>=N/2. The original q states work in a cyclic, input-ranked protocol; this is not the standard Sokolov/GGKS acyclic binary DAG. This proof makes the q-to-DAG loss explicit but does not improve the best recorded O(q^3/log q) compiler or yield a lower bound. See bridge C-210/O-141; the global product-hull charge remains open.


## C-212/C-213 closure-state update

C-212 sharpens the literal patching baseline without changing the closure equations: a set of r addresses in the n-bit truth-table domain has an exact indicator circuit of `O(n+r*n/log(r+1))` gates via shared block decoders. Thus the low class shatters fixed sets of `Theta(s1)` coordinates and each low/high pair differs on `Omega(s2)` coordinates. This only improves local geometry and architecture-specific context counts; the legal fusion activation constraints and the q-to-DAG transfer remain unchanged.

C-213 supplies a counterexample to lower bounds in the unrestricted cyclic rectangle-protocol model. A `5N`-state coordinate cycle solves mismatch for every disjoint promise when the deterministic strategy exits at the first mismatch and wraps around after equal bits. This does not instantiate the fusion closure: cyclic protocol states use independent free predicates on Alice's and Bob's inputs, while a fusion rule's state is a single unary least-fixed-point activation set generated from legal endpoints, literal slices, and predecessor carriers. The scan's root rectangle `Y x Z` corresponds to the cut `X=Y`, the separator whose closure cost is the unresolved object. Therefore no `rho_prom` upper bound follows. The live proof target remains an acyclic rect-DAG lower bound with the recorded `N^(3+3epsilon)/log N` transfer threshold, or a direct argument for the native closure system.

## C-214 — Native recurrence counting versus unrestricted cyclic rectangles

For an arbitrary Boolean partition f on N-bit strings, a q-rule closure separator is determined by at most two subsets of the 2N signed literals per rule, two subsets of q predecessor states per rule, and a subset of empty-output states. Hence at most 2^(4Nq+2q^2+q) functions arise from q rules. Summing over q<=2^(N/2-1) gives fewer than 2^(2^N) systems for large N, so some full-partition promise requires q=Omega(2^(N/2)). C-213's 5N cyclic rectangle scan still solves its mismatch relation. This is a direct generic separation between the unrestricted two-party cyclic rectangle model and unary least-fixed-point fusion closure.

The count only proves existence of a hard partition. It says nothing about the specific SIZE(s1)/SIZE(s2)^c promise, whose middle band leaves separator labels free. Do not use it as an OPS lower bound. It does rule out any generic polynomial-overhead conversion from arbitrary cyclic rectangle protocols to fusion pairs. Full derivation and the active transfer inequalities are in `research/C75_SHARED_DAG_CONTINUATION_2026-09-27.md`.
## C-239 — Canonical rank-fiber cross-product

Using C-233's exact min–max equation, choose seed witnesses at side-support rank 0 and otherwise the least-index predecessor attaining that side's minimum finite rank. The activation-rank vector alone does not determine these choices: a nonmaximal side may use a seed or a predecessor at the same state rank. C-239 gives an endpoint-realizable two-rule counterexample. The augmented profile of both side minima per state determines the acyclic proof skeleton; equal-profile accepted anchors obey C-238's global E/H seed-mixing law whenever the mixed support is consistent. For fixed Q, the side-rank profile is determined by the 2q-bit seed signature, so at most 2^(2q) canonical fibers are realized. This sharpens the count for this selected skeleton convention, not the count of every possible topology, and remains too large for anchor pigeonholing at q>=N.

The state-level splice obligation is now expressed as conflict-or-cover: for every outside context K and finite replacement support C at a reused state, either the supports conflict on opposite rails or their union leaves at most kappa_square(s2) coordinates free. This exact condition is not yet charged to q. The attempted blockwise circuit-description cover still needs to preserve one common description across all address blocks; no near-linear residual-family update was found. Full argument, including limits: research/C239_CANONICAL_RANK_FIBERS_AND_NATIVE_SPLICE_OBLIGATION_2026-09-27.md.

No change to the current linear-scale fusion lower bound and no proof of P != NP.

## C-241 — Shared-DAG transfer boundary

The latest steering makes the standard C-75 rect-DAG primary. Description-space and truth-table-space DAG sizes are exactly equal; the plain relation has S_rect=Theta(C_sep). A fusion list still yields a least-fixed-point cyclic closure with q states, not an acyclic q-node DAG. Current general compiler is S_rect=O(q^3/log q), reverse transfer rho_prom=O(S_rect), while SCC/carrier/escape refinements help only on structured instances. The target remains an OPS-specific product-hull charge above N^(3+3epsilon)/logN or a near-linear separator. C-240's empty-root seed lemma is a possible compiler refinement prompt, not a DAG lower bound. See research/C241_SHARED_DAG_DESCRIPTION_INVARIANCE_2026-09-27.md.


## C-242 continuation pointer

The newest priority reset returns to native cyclic closure. C-242 gives the finite antichain certificate grammar, context/replacement interval law, and high-side blocker path. It also records a fixed-order prefix-intersection native cover and shows why shattering makes that construction exponential. The global O-153 blocker/compatible-join charge and the full-promise near-linear cover remain open. See research/C242_NATIVE_CERTIFICATE_ANTICHAIN_AND_BLOCKER_PATH_2026-09-27.md.
