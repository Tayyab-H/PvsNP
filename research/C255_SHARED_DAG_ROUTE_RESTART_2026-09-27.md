# C-255 — Shared-DAG route audit and attack

Date: 27 September 2026  
Priority: standard acyclic product-rectangle DAGs for the exact C-75 Gap-MCSP mismatch relation.  
Status: exact relation/model comparisons re-audited; description-aware universal construction remains exponential; no OPS-specific superlinear DAG or fusion lower bound obtained.

## 1. Exact relation and information held by each party

Set `N=2^n`, `Y=SIZE(s1)`, `Z={0,1}^N with SIZE(s2) removed`, with `s1<s2`. Alice receives a full truth table `w in Y`; Bob receives a full table `z in Z`. For a proposed pair list `Q=((E_i,H_i))_(i=1)^q`, put `T_i=E_i intersect H_i` and `L_(w,k)=Z intersect {z':z'_k=w_k}`.

The **plain signed-mismatch relation** is

```text
Mis(w,z) = {(k,b): w[k]=b and z[k]=1-b}.
```

It is total on `Y x Z` exactly because the promise sides are disjoint. Alice can instead be given a circuit description `d` with `G(d)=TT(C_d)=w`; this is a representation of her table, not extra information available to Bob.

The **Q-path relation** has the same inputs, but its output must certify a path through this particular `Q`. Let `tau_i(w)` be the least closure round at which `T_i` is activated from the matching slices. A valid path starts at an empty-carrier root active on `w`. At a visited `i`, Bob chooses a side `S in {E_i,H_i}` not containing `z`; Alice then gives either a seed `(k,w_k)` with `L_(w,k) subset S`, or a predecessor `j` with `T_j subset S` and `tau_j(w)<tau_i(w)`. The seed ends at signed mismatch `(k,w_k)`; the predecessor continues at `j`. The rank decreases, so a valid path has at most `q` rule visits. This relation is total on `Y x Z` iff `Q` is a successful fusion cover. It is strictly more structured than plain mismatch: a valid mismatch need not certify the required Q-path.

## 2. Keep the resources distinct

Write `S_rect` for the minimum number of vertices in a binary acyclic product-rectangle DAG solving plain mismatch, and `C_sep` for the minimum fan-in-two Boolean circuit size of any extension `h` with `h=1` on `Y` and `h=0` on `Z`. Values on the medium band are free.

| Resource | Relation and bound |
|---|---|
| Deterministic communication bits, plain mismatch | `O(s1 log(n+s1)+log N)`: Alice sends a circuit description and Bob scans for a differing coordinate. The universal output-support argument gives only `Omega(log N)` bits at OPS scales. |
| Ordinary protocol-tree vertices | At least `N-log2|SIZE(s2)|` leaves by output-coordinate coverage; explicit description transmission uses `O(N |D_s1|)` vertices, where `|D_s1|=2^(O(s1 log(n+s1)))`. |
| Acyclic binary rect-DAG vertices | `S_rect=Theta(C_sep)` up to fixed basis/input-source constants. |
| Q-path communication | `O(q log(q+N))` bits, by naming at most q states/sides and a seed coordinate or predecessor at each step. A literal unrolling has at most `2^(O(q log(q+N)))` tree vertices. |
| Native Q closure | q cyclic least-fixed-point states and `O(q^2+qN)` support incidences. Each pair-specific path terminates by `tau_i(w)`; the static state graph need not be acyclic. |

The tree lower bound follows because if a protocol outputs only coordinates in `K`, then for each low `w` every table agreeing with `w` on `K` must be low; hence `2^(N-|K|)<=|SIZE(s2)|`. It is only a linear output-label/leaf floor and does not force a superlinear graph.

## 3. Closest models: what matches, and what does not

| Model | Exact relation to this target |
|---|---|
| Sokolov DAG-like Karchmer–Wigderson communication | For ordinary Bit/mismatch, acyclic shared protocol vertices characterize Boolean circuit size. On the promise, the circuit is an arbitrary separator extension, so the same equivalence gives `S_rect=Theta(C_sep)`. This is the exact standard-DAG model to attack. |
| Garg–Göös–Kamath–Sokolov rect-DAG | Same product-rectangle DAG resource for search relations. Their lifting theorems apply to specified gadget-composed sources; they do not apply to this MCSP promise without a size-controlled, answer-preserving reduction. |
| GGKS triangle/F-DAG | Stronger state geometry: every rectangle is representable as a triangle, so `S_triangle<=S_rect`. A lower bound in that richer model transfers upward to rect-DAGs. C-194's universal `4N-1` triangle protocol prevents a superlinear lower bound in the triangle model, so it gives no rect-DAG lower bound. |
| Sokolov communication PLS | A separate acyclic state model with a local communication cost for state membership/successor selection. Q's native rule graph may cycle and uses an Alice-input-dependent rank. Layering gives `O(q^2)` rank copies before support routing; a Q path is not a q-vertex standard PLS graph. |
| Nakayama–Maruoka loop circuits | Cyclic circuit specifications are the historical conceptual antecedent. Their function/approximation semantics do not, by themselves, identify the exact promise-relative Q-path or rect-DAG measure. |
| Cavalar–Oliveira cyclic intersection complexity | Exact identity for the fusion-cover measure in the project's finite semi-filter setting: `rho_prom = D_cap^circ = q`. This calibrates native Q closure, not ordinary acyclic rect-DAG size. |
| Amano–Maruoka conjunctive complexity | Counts AND gates in specialized monotone circuits for quadratic functions. There is no C-75 transfer without an AND-preserving reduction; the separator is a general Boolean circuit. |

The literature audit confirms three distinct semantics: (i) ordinary acyclic KW/rect-DAG sharing, (ii) Q's cyclic least-fixed-point closure with pair-dependent termination, and (iii) loop-circuit/intersection formalisms. C-75 is exactly the second for fusion covers, exactly a promise-restricted mismatch search for the first, and not automatically interchangeable with the third. The relevant source results and theorem identifiers are listed at the end.

## 4. Best proved cover-to-DAG and reverse transformations

The q activation labels do not themselves yield a q-node acyclic DAG. A predecessor edge can go from a statically later label to an earlier one for one low table and reverse under another table; C-141 supplies a rank-reversing SCC. The legal generic acyclicization attaches the low-input activation rank: nodes `(i,r)` with `i in [q]` and `r in [q]`, for at most `q^2` rule/rank contexts. Each context still has to route among up to `q+N` legal predecessor/seed supports. Omitting those support routers is invalid because each branch must solve the full product hull of all histories entering it.

The best recorded standard-DAG compiler remains

```text
Q cover of q pairs  ->  S_rect = O(q^3/log q)
```

in the active range. The unbatched accounting is `q^2` contexts and `O(q^2(q+N))` support incidences; batching gives the stated size bound. No `O(q polylog N)` or `O(q)` compiler is proved. Nor is there a theorem ruling one out.

The reverse direction is near-lossless:

```text
rect-DAG with S vertices -> separator circuit O(S) -> fusion cover rho_prom <= O(S).
```

Combining the best available implications gives `rho_prom <= O(S_rect) <= O(rho_prom^3/log rho_prom)`. Consequently a standard-DAG lower bound only implies the desired `rho_prom>N^(1+epsilon)` through the generic forward compiler if it exceeds `N^(3+3epsilon)/log N`. A near-linear `N^(1+o(1))` rect-DAG would conversely imply a near-linear fusion cover and kill the superlinear-cover target. Tier-1 transfer remains unavailable until the q-to-DAG loss is improved or a direct fusion lower bound is proved.

## 5. Description-space pullback and the strongest direct universal construction

Let `D_s1` be all legal size-`s1` circuit descriptions and `G:D_s1 -> Y` map a description to its truth table. For `Mis_G(d,z)=Mis(G(d),z)`, the minimum rect-DAG size is **exactly** invariant:

```text
S_rect(Mis_G) = S_rect(Mis_(Y,Z)).
```

Pulling every Alice rectangle side back through `G` proves `<=`; choosing one canonical section `sigma(w)` with `G(sigma(w))=w` and restricting a description-DAG to `sigma(Y)` proves `>=`. Description collisions do not matter. Thus exposing a short circuit description does not change the shared-DAG problem.

The direct universal separator is

```text
h(w) = OR_(d in D_s1) AND_(k in [N]) [w[k]=G(d)[k]].
```

It has size `O(N |D_s1|)` (up to description/evaluator encoding), exponential in `s1 log(n+s1)`. A deterministic protocol can instead send `d` and scan the N addresses, but a tree that distinguishes all descriptions has exponentially many leaves. Reusing a suffix after those descriptions merge is permitted only when the merged rectangle remains safe for every cross-pair in its product hull. No `N^(1+o(1))` description-aware DAG is constructed here.

The C-217 shattering theorem rules out a narrower tempting construction: every fixed-order scan that stops at its first mismatch has `2^(Theta(s1))` continuation states on the actual promise. It does **not** rule out adaptive/revisiting rect-DAGs or deferred-output protocols. This is a route filter, not the desired general lower bound.

## 6. Non-shareability condition: exact but not yet aggregatable

At a rect-DAG state `v`, let its full rectangle be `A_v x B_v`, and let `K_v` be all output coordinates below it. Correctness requires

```text
pi_Kv(A_v) intersect pi_Kv(B_v) = empty.
```

Equivalently, every pair in that state has a mismatch among its descendant output labels. If histories `(A_r x B_r)` merge at v, the suffix must solve `(union_r A_r) x (union_r B_r)`, including cross-history pairs. This is the precise non-shareability test: histories may merge only when the entire product hull stays mismatch-solvable below v.

Attempted amplification: charge each state for the row/column projection patterns it excludes. It fails because a high column or projection can be excluded at many states, and descendant output sets shrink along paths; local deficits overlap. C-80/C-160 and the C-208/O-141 audits are explicit hostile checks. The weaker proposed assertion “one state serves at most k low anchors” is false for general promises: large rectangles can contain many anchors, and C-213 gives a one-rule native cover for a large artificial promise. C-232 gives a sharper generic DAG calibration: an O(N)-output-alphabet mismatch relation can have `O(N)` deterministic communication bits but `Omega(2^N/N)` rect-DAG vertices by counting. Neither artificial result transfers to the specific low-circuit/high-circuit partition.

So far the exact structural law is local (product-hull safety), not a global state charge. The missing theorem must use the geometry of `SIZE(s1)` versus the dense complement of `SIZE(s2)` to aggregate residual relations without summing repeated exclusions. No Tier-1/2/3 non-shareability lemma is proved.

## 7. Priority and next falsification tests

This route is **not killed**: description invariance kills “short descriptions automatically mean a small DAG,” while the direct universal construction is exponential and the fixed-order scan is too restricted. The remaining question is precisely whether adaptive, revisiting product-rectangle routing has a compact construction for the actual promise or an OPS-specific shared-state lower bound.

Next work should focus on: (a) one stronger universal DAG using adaptive block tests or shared residual predicates, with its exact vertex count and product-hull proof; (b) a proposed state-merging lower-bound invariant tested against C-80/C-160/C-213/C-232; (c) any lower bound on `S_rect` checked against the `N^(3+3epsilon)/log N` compiler threshold; and (d) any q-to-DAG improvement proved from the actual rank/support recurrence, not by counting q labels while suppressing their routers. Retire a candidate immediately if it reduces to output support, a fixed semi-filter family, or a generic cyclic protocol.

**Conclusion:** this is a rigorous Tier-4 model correspondence plus a Tier-5 quantitative audit. It is not a P-vs-NP breakthrough and yields no new superlinear `rho_prom` or `S_rect` bound.

## 8. New bottleneck-counting transfer test (Beame–Whitmeyer, 2025)

Beame and Whitmeyer prove that every triangle-DAG for the natural two-party search relation of the bit pigeonhole principle has at least `2^(n0^(1/4)/sqrt(2)-2)` nodes. Their proof adapts Haken–Cook bottleneck counting: each sink must lie in one of the valid collision-pair rectangles `R_(i,j)`; they define, for each node and one-sided input, the minimum number of such output rectangles covering that slice; a partial map assigns many one-sided inputs to nodes, while a source-specific combinatorial lemma bounds how many can be assigned to one node. This is a real shared-DAG lower-bound technique, rather than a communication-depth argument.

### Exact reduction needed to transfer it

For a source total search relation `S subset X x Y -> O`, suppose there are maps `phi_A:X->SIZE(s1)` and `phi_B:Y->Z`, and a fixed output-label decoder `delta:(k,b)->O`. Require that for every source pair `(x,y)`, every signed mismatch `(k,b)` of `phi_A(x),phi_B(y)` satisfies `delta(k,b) in S(x,y)`. Then every rect-DAG for C-75 pulls back, vertex-for-vertex, to a rect-DAG for S. Therefore

```text
S_triangle(S) <= S_rect(S) <= S_rect(C-75),
```

since triangle-DAGs are at least as powerful as rect-DAGs. The BPHP lower bound would then transfer. Its source parameter can be chosen around `n0=K(log N)^4`: the known `2^(Omega(n0^(1/4)))` size scale can exceed `N^(3+3epsilon)/log N` for large enough K, while the source input length `O(n0 log n0)` is only polylogarithmic in N. Thus parameter size is not the main obstruction.

### Common hard-translate lemma

There is an exact counting construction for the high-image condition. Write `L=SIZE(s2)`. If

```text
|SIZE(s1)| * |L| < 2^N,
```

then there is a mask `r in {0,1}^N` outside the difference set `SIZE(s1) xor L`: at most `|SIZE(s1)||L|` masks have the form `w xor z` with `w in SIZE(s1)` and `z in L`. Consequently

```text
u in SIZE(s1)  =>  u xor r notin SIZE(s2).
```

At OPS parameters, `log |SIZE(s1)|+log |SIZE(s2)|=O(s2 log(n+s2))=o(N)`, so the inequality holds for all sufficiently large N. Since the bad-mask fraction is `2^{-N+o(N)}` and atypical Hamming weights have exponentially small fraction, r can also be chosen with weight in `[N/4,3N/4]`. Thus, given **any** low base encoding `u_y in SIZE(s1)` of each Bob source input, `phi_B(y)=u_y xor r` is high for every y. This resolves the bare hard-image existence issue without computing a hard table.

It does not solve answer soundness. For low base codewords `u_x,u_y`, an image mismatch occurs exactly when `u_x[k] xor u_y[k] != r[k]`. If `r[k]=0`, the two signed mismatch rectangles are the off-diagonal bit patterns `(u_x,u_y)=(0,1),(1,0)`; if `r[k]=1`, they are the diagonal patterns `(0,0),(1,1)`. A transfer needs a fixed decoder assigning each of these rectangles a source answer valid for every source pair in that rectangle, and these rectangles together must cover all source pairs. In BPHP, the natural valid-answer rectangles assert that two pigeons collide; no coordinate encoding satisfying this cut-soundness condition is known.

The direct coordinate encoding of a BPHP collision test fails immediately. If `u_x[k]=1` iff Alice's halves of pigeons i,j agree and `u_y[k]=1` iff Bob's halves agree, the desired collision is the `(1,1)` rectangle. With `r[k]=1`, the same coordinate also emits the false-positive `(0,0)` mismatch; with `r[k]=0`, it emits only the two off-diagonal patterns, neither of which certifies that pair collision. Reassigning a false-positive signed label to some other colliding pair would need a separate proof that this same output is valid throughout that entire rectangle; the pigeonhole principle alone supplies only a pair depending on the full input.

An ordinary polylogarithmic-size Bob encoding alone is low and fails. A common hard translate repairs that defect, while a naive hard padding block remains unsafe because every padding mismatch must decode to a valid answer; a universal output would collapse the source search. C-256 subsequently proves that the static-label version of this interface is impossible for two-wise-rich hard KW sources and for full-domain BPHP collision search. Terminal-specific decoding remains distinct and would require a size-controlled refinement of each pulled-back sink rectangle. See `research/C256_HARD_TRANSLATE_KW_DECODER_OBSTRUCTION_2026-09-27.md`.

### Bottleneck width for mismatch: definition and current boundary

For a rect-DAG state v, let `A_v x B_v` be its rectangle and `K_v` its descendant coordinate labels. For a fixed low row w in `A_v`, define

```text
lambda_v(w) = min{|I| : I subseteq K_v and every z in B_v differs from w
                     on some coordinate in I}.
```

Equivalently, `I` selects signed mismatch rectangles covering the one-row slice `{w} x B_v`. At the root, `lambda_root(w) >= N-log2|SIZE(s2)|` by the cylinder count; at a mismatch leaf, it is 1. The dual high-column width is the minimum coordinate set separating `A_v` from one z. By the `Omega(s2)` low/high distance and a random hitting-set argument, at the root it is at most `O((N/s2) log|Y|)`, which at the project's `s2=Theta(s1 log N)` scales is only a constant-factor-N bound, not `O(log|Y|)` or a sublinear-in-N guarantee. This corrects the tempting but false inference that a small row-description class gives logarithmic output width for every high column.

This is the right analogue of the paper's node/slice width, but it is not yet a bottleneck theorem. The missing step is a C-75-specific capacity bound: at an intermediate shared node, bound the low anchors that can be assigned when their residual mismatch width crosses a threshold, using low-circuit patch shattering and high-side cylinder density. Shattering alone does not bound arbitrary subsets `A_v` of the low class; local projection deficits can overlap across DAG nodes. Therefore the BPHP proof does not transfer by replacing collision rectangles with coordinate-mismatch rectangles. The precise candidate is to establish a partial bottleneck map plus a node-capacity lemma robust to arbitrary product-rectangle filtering, and falsify it against C-80/C-160.

**Disposition:** this is a new, technically close lower-bound template and a precise reduction interface (Tier 3 candidate), not a lower bound for the actual promise. The common-translate lemma handles the high-image requirement; the first unresolved implication is a cut-sound low encoding that makes every signed mismatch a valid source answer. No C-75 bound changes.

## Primary sources

- Dmitry Sokolov, [*Dag-like Communication and Its Applications*](https://eccc.weizmann.ac.il/report/2016/202/), ECCC TR16-202, Boolean DAG-like KW/circuit correspondence and communication PLS.
- Ankit Garg, Mika Göös, Pritish Kamath, and Dmitry Sokolov, [*Monotone Circuit Lower Bounds from Resolution*](https://theoryofcomputing.org/articles/v016a013/), rect-DAG, triangle-DAG, F-DAG, and gadget-lifting models.
- Bruno P. Cavalar and Igor C. Oliveira, [*Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://arxiv.org/abs/2503.14117), exact cyclic intersection/cover characterization (Theorem 3 in the arXiv version; Theorem 30 in the longer version cited in project notes).
- Katsutoshi Nakayama and Akira Maruoka, [*Loop Circuits and Their Relation to Razborov's Approximation Model*](https://doi.org/10.1006/inco.1995.1083), loop-circuit function/approximation identity.
- Kazuyuki Amano and Akira Maruoka, [*The Monotone Circuit Complexity of Quadratic Boolean Functions*](https://doi.org/10.1007/s00453-006-0073-0), conjunctive complexity and monotone quadratic functions.
- Paul Beame and Michael Whitmeyer, [*Multiparty Communication Complexity of Collision-Finding and Cutting Planes Proofs of Concise Pigeonhole Principles*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.21/LIPIcs.ICALP.2025.21.html), ICALP 2025, Theorem 1.7 and Section 5 bottleneck count for triangle-DAGs computing the bit-pigeonhole search relation.
