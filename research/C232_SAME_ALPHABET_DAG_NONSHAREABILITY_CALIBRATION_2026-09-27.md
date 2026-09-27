# C-232 — Same-alphabet DAG nonshareability calibration

Date: 27 September 2026  
Scope: continue the C-74/C-75 shared-DAG route. Audit the strongest generic short-description/universal-evaluator attack, and test whether low communication can coexist with large DAG size even for the ordinary mismatch output alphabet. This is a rigorous model calibration, not a lower bound for the actual Gap-MCSP promise.

## 1. Exact C-75 relation and resource separation

Put `N=2^n`, `Y=SIZE(s1)`, and `Z={0,1}^N minus SIZE(s2)`, with `s1<s2`. The plain relation is

\[
\mathsf{Mis}_{Y,Z}(w,z)=\{k\in[N]:w_k\ne z_k\}.
\]

For a signed output, return `(k,w_k)`; this changes the number of output labels by at most a factor of two. The relation is total since `Y` and `Z` are disjoint.

Alice can send a circuit description `d` for `w`, requiring `O(s1 log(n+s1))` bits, after which Bob scans the table addresses and finds a mismatch with `z`. Thus deterministic communication is

\[
C_{\rm det}(\mathsf{Mis}_{Y,Z})=O(s_1\log(n+s_1)+\log N).
\]

The output-support argument gives the lower bound `C_det >= log2(N-log2|SIZE(s2)|)` up to additive constants: if every leaf outputs one of fewer than `N-log2|SIZE(s2)|` coordinates, then more than `|SIZE(s2)|` completions of any fixed low table agree on all output coordinates, so at least one completion is high and the protocol has no valid output for that pair. The protocol-tree vertex count is a different resource: the generic bit bound gives at most `2^(O(s1 log(n+s1)))` vertices, while the same argument gives at least `N-log2|SIZE(s2)|` output leaves.

For a fixed proposed `q`-pair cover `Q`, the stronger `Q`-path relation records a start rule, each absent side selected by Bob, and each seed or lower-activation-rank predecessor selected by Alice. It is total on `Y x Z` exactly when `Q` succeeds. The path has at most `q` rule moves, so its deterministic communication is `O(q log(q+N))` bits and its unrolled protocol tree has at most `2^(O(q log(q+N)))` vertices. These are not `q` standard DAG states: the static support graph can cycle, while termination uses the input-local rank `tau_i(w)`.

## 2. A same-output-alphabet counterexample to generic compression

Let `f:{0,1}^N -> {0,1}` be any Boolean function and define its Karchmer–Wigderson mismatch relation on
`Y_f=f^{-1}(1)` and `Z_f=f^{-1}(0)`. Alice sends `x` in `N` bits; Bob then returns any coordinate `k` with `x_k != y_k`. This uses at most `N+ceil(log N)` bits, and its output alphabet has only `N` coordinates (or `2N` signed labels).

There are functions `f` whose fan-in-two circuit size is `Omega(2^N/N)`. Indeed, the number of size-`S` circuits on `N` inputs is at most `2^{O(S log(N+S))}`; for `S=c 2^N/N` and a sufficiently small constant `c`, this is less than the `2^(2^N)` Boolean functions. The Sokolov DAG form of the Karchmer–Wigderson theorem says that the minimum acyclic Boolean communication-game size for `Bit_f` is within constant factors of circuit size. Therefore some ordinary mismatch relations with only `N` output labels have

\[
\mathsf{DAGsize}(\mathsf{Mis}_{Y_f,Z_f})=\Omega(2^N/N)
\]

despite `O(N)` deterministic communication bits. The large DAG requirement is not an output-alphabet artifact; it is the circuit complexity of the separator encoded by the two sides.

For this example the same protocol tree has at most `O(N 2^N)` vertices (Alice's `2^N` possible inputs, followed by Bob's `N` possible output labels), and at least `Omega(2^N/N)` vertices because every tree is a DAG. This makes the distinction precise: the communication **bit** cost is linear while both graph-vertex measures can be exponential. Parity supplies the separate example where DAG sharing reduces vertex count from `Theta(N^2)` to `O(N)`.

There is a distinct tree-versus-DAG phenomenon in the other direction: every tree is already a DAG, so `DAGsize <= Treesize` under the same vertex measure. Parity gives a standard calibration where its Karchmer–Wigderson protocol tree/formula has size `Theta(N^2)` while a shared circuit/DAG has `O(N)` gates. Thus the meaningful comparisons are communication bits versus graph vertices, and DAG reuse versus tree expansion; “small tree by vertex count but large DAG” is impossible.

**Transfer limit.** This counterexample is an arbitrary Boolean partition. It does not imply that the fixed `SIZE(s1)` versus `SIZE(s2)^c` separator has large circuit complexity. It only proves that short communication, a small mismatch output alphabet, and cheap descriptions do not generically upper-bound shared-DAG size by a polynomial in the message length.

## 3. Strongest direct universal-description construction and its failure

Let `D` contain one canonical description for each table in `Y`, and let `G(d)=TT(C_d)`. The direct separator is

\[
h(w)=\bigvee_{d\in D}\ \bigwedge_{k\in[N]}[w_k=G(d)_k].
\]

It accepts every low table and rejects every high table, leaving the medium band unrestricted. Circuit counting gives `|D| <= 2^(O(s1 log(n+s1)))`, so the direct construction costs at most
`O(N 2^(O(s1 log(n+s1))))` fan-in-two gates. A universal circuit computes `G(d)_k` from `(d,k)`, but still leaves the existential disjunction over descriptions. Evaluating one candidate description is cheap; eliminating the global `exists d` condition is the expensive operation.

The same issue appears in the protocol. For each signed coordinate there is a valid mismatch rectangle

\[
R_{k,b}=\{d:G(d)_k=b\}\times\{z:z_k=1-b\}.
\]

The `2N` rectangles cover all promised pairs. This is an `O(N)` rectangle cover, but it is not automatically a binary rect-DAG: a standard internal node must itself be a rectangle covered by its two child rectangles. If a product `A x B` is covered by `A_0 x B_0` and `A_1 x B_1`, then either one child contains the parent, or (after swapping the parties if needed) `A` is contained in `A_0 union A_1` while `B` is contained in `B_0 intersect B_1`. An arbitrary union of mismatch rectangles need not have this form, so replacing one high-fan-out cover node by a binary tree is invalid unless every intermediate union remains rectangular.

The direct universal-evaluator scan has a two-address obstruction. Take low rows `w0=00,w1=11` and high columns `z0=01,z1=10`. After scanning coordinate 1, the matched histories are `(00,01)` and `(11,10)`; each still has a mismatch at coordinate 2. If the universal scan merges them into one “continue at coordinate 2” state, its product hull is `{00,11} x {01,10}`. The cross-pairs `(00,10)` and `(11,01)` agree at coordinate 2, so that state cannot route every pair to a suffix output. The scan must retain the matched prefix (two states here) or revisit coordinate 1. This is the local product-hull failure behind C-217's exponential lower bound for fixed-order first-mismatch scanners on the actual OPS promise; it does not rule out a different adaptive DAG.

Description-space gives no state reduction by itself. If `G:D -> Y` is onto, precompose each Alice state predicate on `Y` with `G` to lift a truth-table rect-DAG to descriptions. Conversely choose one description `sigma(w)` for each `w in Y` and restrict every description-side predicate to `sigma(Y)`. Both maps preserve all graph nodes, rectangle conditions, and valid mismatch outputs. Hence

\[
S_{\rm rect}(D\times Z\text{ under }G)=S_{\rm rect}(Y\times Z).
\]

This is the exact failure point of the syntax-only universal-DAG attack: `G` helps Alice communicate a witness, but it does not shrink the circuit/separator computed by a shared graph.

## 4. Closest literature models and explicit comparison

| Model | State/semantics | C-75 relation and transfer |
|---|---|---|
| Sokolov Boolean DAG-like communication game | Acyclic outdegree-two graph; each node is a product rectangle from separate Alice/Bob predicates; child rectangles cover the parent; leaves carry valid answers. | Plain C-75 signed mismatch is exactly the promise restriction of `Bit`. For any promise `(Y,Z)`, its minimum rect-DAG size is `Theta(C_sep(Y,Z))`, where `C_sep` is minimum Boolean circuit size of any `h` with `h=1` on `Y`, `h=0` on `Z`. Medium inputs are free. |
| Garg–Göös–Kamath–Sokolov rect-DAG | The same product-rectangle DAG resource, used for composed search relations and proof/circuit lower bounds. | The model matches C-75 directly. Their lifting theorem supplies lower bounds for specified gadget-composed sources; it does not create a reduction from the actual Gap-MCSP mismatch promise. |
| GGKS triangle-/F-DAG | Acyclic states may be triangles or other structured non-product relations; every rectangle is a triangle. | `S_triangle <= S_rect`, so a triangle-DAG lower bound transfers to rect-DAG. But C-194 gives a universal `4N-1`-state triangle protocol for every disjoint mismatch promise; this kills a superlinear target in that stronger geometry. |
| Cavalar–Oliveira cyclic intersection / fusion cover | Cyclic set equations evaluated by least fixed point; the exact theorem identifies semi-filter cover complexity with cyclic intersection complexity. | On the C-75 promise ground set `Gamma=Y union Z` and its coordinate-slice generator family, the project’s `q`-pair measure is the corresponding cyclic/cover complexity. It is not standard acyclic rect-DAG size. |
| Nakayama–Maruoka loop circuits | Cyclic specifications studied through a generalized approximation model. | This is the historical loop-circuit connection. Cavalar–Oliveira explicitly adapt the argument: their exact theorem uses semi-filters and intersection complexity, unlike the earlier general functional/Boolean-circuit formulation. Use the adapted theorem for the C-75 identity. |
| Amano–Maruoka conjunctive complexity | Counts AND gates in monotone circuits; their cited results concern quadratic Boolean functions. | It can measure an acyclic monotone resource only after an AND-preserving reduction. C-75 separator circuits are general Boolean circuits and the promise-dependent endpoints do not provide that reduction. |

The `S_rect=Theta(C_sep)` claim has a direct two-way proof on this promise. Given a separator circuit, make one state per gate and let its row side be the low inputs where the gate is 1 and its column side the high inputs where it is 0. At an AND or OR gate, the parent rectangle is covered by the two child rectangles; circuit sharing is retained as DAG sharing. Literal leaves give signed mismatch outputs. In the reverse direction, assign each rect-DAG node a separator circuit for its rectangle: at a leaf use its mismatch literal; at an internal node, if the parent is covered by row-union/column-intersection children, OR their separators, and in the dual column-union/row-intersection case AND them; if one child already contains the parent, copy that child's separator. The two-rectangle product-cover trichotomy guarantees one of these cases. This uses `O(S_rect)` gates. Since only Y and Z are constrained, the circuit need not decide exact membership in `SIZE(s1)` on the medium band.

## 5. Quantitative transformation chain

For the actual promise, the circuit/rect-DAG induction and the recorded fusion transformations give

\[
q=\rho_{\rm prom}\le O(S_{\rm rect}),\qquad
S_{\rm rect}\le O(q^3/\log q),\qquad
D^\circ_{\cap}=q,\qquad D_{\cap}\le q^2.
\]

The first inequality is the no-loss direction up to basis constants: a rect-DAG yields a separator circuit, then the promise-relativized fusion construction gives a cover. The forward compiler is the expensive direction. Its rank-lift uses `(rule, rank)` contexts, up to `q^2`, and each context has up to `O(q+N)` support choices; support routing cannot be omitted. Batching yields the recorded `O(q^3/log q)` standard rect-DAG bound when `q` is at least on the order of `N`.

Therefore the generic forward transfer proves `q>N^(1+epsilon)` only from

\[
S_{\rm rect}>c\,N^{3+3\epsilon}/\log N
\]

for an appropriate constant. A Tier-2 DAG lower bound `N g(N)` with `g(N)->infinity` is mathematically meaningful but does **not** imply superlinear `q` through the cubic compiler. Conversely, a construction `S_rect=N^(1+o(1))` would imply `q=N^(1+o(1))` by the reverse transfer and would rule out every fixed-exponent superlinear target `N^(1+epsilon)`.

Keep the earlier ceilings as route filters: `rho_w<=N-1`, `rho*=O(N)`, and `rho(H)=O(N log|H|)` for a fixed semi-filter family `H`. A proposal that reduces the full promise to a one-anchor, universal, or fixed-family case cannot prove the desired superlinear promise-cover lower bound. O-152 needs genuinely adaptive/global reuse beyond those restricted regimes.

The q-state fusion path itself is a ranked cyclic protocol, not an acyclic DAG. Its `tau_i(w)` rank is Alice-local and can reverse around a static dependency cycle; C-141 records a rank-reversing SCC. Replacing each rule by rank layers gives an acyclic graph, but the product with support routing costs more than `q^2` vertices. Allowing cycles and merely requiring per-pair termination is a different model: C-213 has a `5N`-state cyclic rectangle solver for every disjoint mismatch promise, while C-214 shows cyclic-rectangle size does not generically control fusion cover size.

## 6. Exact nonshareability invariant and remaining task

At any rect-DAG node `v`, let `A_v x B_v` be its full rectangle and let `K_v` be the set of coordinates labelling descendant mismatch leaves. Correctness implies

\[
\pi_{K_v}(A_v)\cap\pi_{K_v}(B_v)=\varnothing.
\]

If histories `A_h x B_h` merge at `v`, the suffix must solve the full cross-history hull `(union_h A_h) x (union_h B_h)`, not only each incoming history. This is the precise product-hull nonshareability condition. It is local and exact; C-80/C-160 show that summing statewise deficits naively is invalid. The missing theorem is a global overlap-safe charge on distinct residual separator functions or a concrete `N^(1+o(1))` separator for the full promise.

**Disposition:** the short-description shortcut is killed as a generic argument; a same-alphabet artificial relation demonstrates the communication/DAG gap. No near-linear DAG was constructed and no OPS-specific superlinear DAG bound was proved. Continue O-141 on the full product-rectangle model; keep the native closure compiler as a separate transfer route and preserve the cubic/log loss explicitly. No P-vs-NP proof follows.

### Primary sources

- Dmitry Sokolov, [*Dag-like Communication and Its Applications* (ECCC TR16-202)](https://eccc.weizmann.ac.il/report/2016/202/download), especially Definitions 2.1–2.3 and Theorem 3.2.
- Mauricio Karchmer and Avi Wigderson, [*Monotone Circuits for Connectivity Require Super-Logarithmic Depth*](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/KW90/KW90.pdf), for the Karchmer–Wigderson formula/protocol framework and the Khrapchenko parity calibration.
- Ankit Garg, Mika Göös, Pritish Kamath, and Dmitry Sokolov, [*Monotone Circuit Lower Bounds from Resolution*](https://theoryofcomputing.org/articles/v016a013/), for rect-DAG, triangle-DAG, and F-DAG models and gadget-composed lifting.
- Bruno P. Cavalar and Igor C. Oliveira, [*Boolean Circuit Complexity and Two-Dimensional Cover Problems* (ECCC TR25-033)](https://eccc.weizmann.ac.il/report/2025/033/download), Theorem 30 and Corollary 17 for the exact cyclic-cover identity and quadratic acyclic unfolding at the AND-count level.
- Katsutoshi Nakayama and Akira Maruoka, [*Loop Circuits and Their Relation to Razborov's Approximation Model*](https://doi.org/10.1006/inco.1995.1083); compare the precise model adaptation in Cavalar–Oliveira.
- Kazuyuki Amano and Akira Maruoka, [*The Monotone Circuit Complexity of Quadratic Boolean Functions*](https://doi.org/10.1007/s00453-006-0073-0), for conjunctive complexity and its function-specific monotone setting.
