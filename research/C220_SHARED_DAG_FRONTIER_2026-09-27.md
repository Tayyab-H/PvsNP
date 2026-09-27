# C-220 — The C-75 shared-DAG frontier, audited

Date: 27 September 2026  
Scope: C-74/C-75 only. This records the exact search relations, the current cover/DAG transfers, a direct description-space attack, and a correction to one model-comparison statement. It proves no new Gap-MCSP lower bound.

## 1. Exact search relations

Let `N=2^n`, `Y=SIZE(s1)`, and `Z={0,1}^N minus SIZE(s2)`, with `s1<s2`.

### Plain signed mismatch

The promised input is a pair `(w,z) in Y x Z`. Alice knows `w`, Bob knows `z`. The output relation is

\[
\mathsf{Mis}_{Y,Z}(w,z)=\{(k,b): k\in[N],\ b=w_k,\ z_k=1-b\}.
\]

It is total because `Y` and `Z` are disjoint. The usual Bit/KW output can omit `b`; adding the orientation bit changes output labels by at most a factor of two.

### Q-specific closure-path witness

Fix a public pair list `Q=((E_i,H_i))_{i=1}^q`, with `T_i=E_i intersect H_i`, and the closure generated from the matching slices `L_{w,k}={z in Z:z_k=w_k}`. Let `tau_i(w)` be the first closure round in which `T_i` is activated. A valid path certificate consists of:

1. A start rule `i0` with `T_i0=empty` and `tau_i0(w)<infinity`.
2. At each active rule `i`, Bob chooses a side `S in {E_i,H_i}` with `z notin S`. This is possible because a successful list keeps `z notin T_i`.
3. Alice either gives a seed index `k` with `L_{w,k} subseteq S`, ending with the signed mismatch `(k,w_k)`, or a predecessor `j` with `T_j subseteq S` and `tau_j(w)<tau_i(w)`.

The path relation depends on the proposed list, endpoint containments, seed incidences, and the input-dependent activation ranks. It is total on `Y x Z` exactly when `Q` is a successful cover. Forgetting the path maps a valid path output to a valid plain mismatch output; the converse need not hold.

With `Q` public as nonuniform advice, at most `q` rules are visited. Bob sends one side bit per rule; Alice names a predecessor or seed using `O(log(q+N))` bits. Thus deterministic communication is `O(q log(q+N))` bits and the direct protocol tree has at most `2^(O(q log(q+N)))` vertices. The `q`-state support graph can be cyclic, but every fixed input pair follows strictly decreasing `tau_i(w)` and terminates. This is not a standard acyclic rect-DAG.

## 2. Exact relation to acyclic rectangle-DAGs and separators

Write `C_sep(Y,Z)` for minimum fan-in-two Boolean-circuit gate size of any `h:{0,1}^N -> {0,1}` with `h=1` on `Y` and `h=0` on `Z`, leaving the medium band unrestricted. Let `S_rect(Y,Z)` be the fewest vertices in an acyclic, outdegree-two product-rectangle search DAG whose root is `Y x Z`, each node rectangle is covered by its children, and each leaf is labelled by a signed mismatch valid throughout that leaf rectangle.

For this actual promise,

\[
S_{\rm rect}(Y,Z)=\Theta(C_{\rm sep}(Y,Z)).
\]

Here is the two-way proof, with the input-source convention made explicit.

* **Circuit to DAG.** Put one state at each gate of a separator circuit, after converting to an AND/OR circuit over input literals with only linear size overhead. At gate `g`, its rectangle is `{w in Y:g(w)=1} x {z in Z:g(z)=0}`. If an AND gate differs as `1` on Alice input and `0` on Bob input, some child differs the same way; the OR case is dual. A literal leaf yields the corresponding signed mismatch. Shared circuit gates remain shared DAG states. Thus `S_rect=O(C_sep+N)`.
* **DAG to circuit.** At a leaf labelled `(k,b)`, use the literal `[x_k=b]`. At an internal node, its parent rectangle is covered by two child rectangles. A two-rectangle cover of a product rectangle has one of three forms: the parent is contained in one child; the row side is contained in both child row sides; or the column side is contained in both child column sides. In the latter two cases combine the child separators by OR or AND, respectively. Recursing in reverse topological order gives a separator circuit with `O(S_rect)` gates. This is the Boolean-game/KW DAG-to-circuit argument; it does not compute the semantic rectangle predicates themselves.

The `+N` source term is immaterial here. Any separator depending on coordinate set `K` must have `2^(N-|K|) <= |SIZE(s2)|`; otherwise some high table agrees with a low table on all of `K`. Hence every separator depends on at least `N-log2|SIZE(s2)|=N-o(N)` coordinates in the OPS regime. A fan-in-two circuit with `S` gates has at most `2S` input wires, so `C_sep=Omega(N-o(N))`. This also recovers the root-support linear lower bound, not a superlinear one.

The medium truth tables are important: a promise separator is an arbitrary extension off `Y union Z`, not a circuit deciding exact membership in `Y` on the full cube.

## 3. Literature-model audit and a correction

| Model | Exact relationship to this project |
|---|---|
| Sokolov Boolean DAG-like games; GGKS rectangle-DAGs | Acyclic, outdegree at most two, rectangle-valued states. Plain signed mismatch is the promise restriction of Bit/KW. For a total separator function the DAG/circuit correspondence is exact up to input-source conventions; the same induction works on the promise `Y x Z`. |
| GGKS `F`-DAGs and triangle-DAGs | A triangle state has form `{(x,y):a(x)<b(y)}`; every rectangle is a triangle (choose two-level labels). Thus `S_triangle<=S_rect`. A lower bound for triangle-DAGs would transfer to rect-DAGs; an upper bound for triangle-DAGs does not. C-194 and C-195 are route filters described below. |
| Cavalar-Oliveira cyclic intersection complexity | On the promise ground set `Gamma=Y union Z`, with the corresponding semi-filter family, the fusion-pair number is exactly `q=rho_prom=Dcirc_cap`. The theorem is about the relativized promise universe, not exact low-set membership on the full truth-table cube. |
| Nakayama–Maruoka loop circuits | A foundational cyclic-circuit/approximation connection. It motivates the loop viewpoint but is not, without the Cavalar–Oliveira translation, the exact semi-filter promise identity above. |
| Amano–Maruoka conjunctive complexity | Counts AND gates in monotone circuits, with results for quadratic Boolean functions. It is a useful acyclic AND-resource analogue; a C-75 consequence needs an AND-preserving reduction. |

**Triangle-model route filter.** The inclusion direction is useful in principle: a triangle-DAG lower bound would imply the same lower bound for rect-DAGs. But C-194 constructs a `4N-1`-state triangle-DAG for signed mismatch on every disjoint promise, so this stronger model has a universal linear upper bound and cannot yield the desired superlinear lower bound for C-75. C-195 only proves that one state in that particular protocol expands into many rectangles; it does not rule out a different rect-DAG.

The closure rule labels cannot simply be declared the vertices of a standard DAG. The fixed dependency graph may have cycles; `tau_i(w)` is an input-dependent ranking. C-141 supplies an actual rank-reversing SCC, so there is no globally valid topological order on the `q` rule names. This defeats the proposed `q`-node acyclicization, not all `O(q polylog N)` compilers.

The useful distinction is whether a termination rank is **separable** across the two inputs. For fusion, the activation rank `tau_i(w)` is Alice-local; its threshold sets are row predicates, so rank layering produces product-rectangle contexts `(i,r)` (at the cost of q^2 contexts and support routers). In C-213's universal cyclic mismatch scan, the progress rank is the position of the next mismatch and depends jointly on `(w,z)`. A time-copy `(state,r)` carrying the full rectangle `Y x Z` therefore does not encode who has already matched which prefix; cutting it into progress layers requires product-rectangle refinements of the joint mismatch predicate. The interval example below shows why one such layer is not a single rectangle. Per-pair termination within one cycle is not itself an acyclicization theorem.

## 4. Best proved transfers and their losses

The current exact/quantitative chain is

\[
q=\rho_{\rm prom}\le O(S_{\rm rect}),\qquad
S_{\rm rect}\le O(q^3/\log q),\qquad
D^\circ_{\cap}=q,\qquad D_{\cap}=O(q^2).
\]

The first inequality is the DAG/separator-to-promise-cover transfer. The second is the best recorded acyclicization/compiler: rank layering creates `q^2` rule/rank contexts, and support routing can have `O(q+N)` choices per context; batching improves the binary circuit/DAG count to `O(q^3/log q)` in the relevant range. Counting only `q^2` layer vertices while ignoring support routing is invalid. No proof presently gives an `O(q polylog N)` standard-DAG compiler or proves such a compiler impossible.

Consequently, the generic route from a standard-DAG lower bound to `q>N^(1+epsilon)` needs `S_rect > c N^(3+3epsilon)/log N` for a sufficiently large constant c.

\[
S_{\rm rect} \ge c N^{3+3\epsilon}/\log N.
\]

A direct `q`-lower bound avoids this cubic loss. Conversely, a near-linear `S_rect=N^(1+o(1))` would imply `q<=N^(1+o(1))` and kill the desired superlinear fusion route. The ceilings `rho_w<=N-1`, `rho*=O(N)`, and `rho(H)=O(N log|H|)` apply to distinct restricted regimes; none is a universal bound on `rho_prom`.

## 5. Does Alice's short description create a small shared DAG?

Let `N=2^n`, `Y=SIZE(s1)`, and `Z={0,1}^N minus SIZE(s2)`, with `s1<s2`.

* Pull a table-DAG state row set `A subseteq Y` back to `G^{-1}(A) subseteq D_s1`. This preserves every rectangle and every edge.
* Conversely choose one description `sigma(w)` for each `w in Y`; restrict every description-side state to `sigma(Y)`. This again preserves rectangles, paths, and outputs.

Therefore

\[
S_{\rm rect}(D_{s_1},Z)=S_{\rm rect}(Y,Z).
\]

The description gives a cheap **bit protocol**: Alice sends `d`, using `O(s1 log(n+s1))` bits; Bob computes `C_d(a_k)` while scanning coordinates until it differs from `z_k`, then outputs `(k,C_d(a_k))`. Total communication is `O(s1 log(n+s1)+log N)` bits. Its direct protocol tree has at most `O(N 2^(O(s1 log(n+s1))))` vertices. This is no shared-DAG construction: replacing `w` by `d` cannot decrease the minimum DAG size.

The obstruction is not that a graph vertex literally stores the description. A vertex may use arbitrary party-local predicates. The obstruction is that a shared vertex must be correct on the **entire product hull** of all row and column histories routed there. If `A_v x B_v` is a state rectangle and `K_v subseteq [N]` is the set of output coordinates below it, then necessarily

\[
\pi_{K_v}(A_v)\cap\pi_{K_v}(B_v)=\varnothing.
\]

Otherwise some pair entering the state agrees on every possible descendant output and no leaf can be valid. This is a proved local non-shareability condition, but its statewise exclusions overlap and have no known global sum; C-80/C-160 prohibit crude capacity summations.

### Universal-evaluator attack and failure point

The strongest direct candidate tried so far has Alice send `d`, then uses a universal circuit to evaluate `C_d` at successive addresses and compares each answer with Bob's `z_k`. As a protocol tree this is valid and has the bound above. Sharing the post-description scan solely by the next coordinate or the universal-circuit gate index is not valid: the merged rectangle contains cross-pairs from different descriptions and columns, including pairs whose only known mismatch lies at a coordinate already passed by the scan. C-217 proves exponential width for the fixed-order first-mismatch version. A separate mixed-cell/wire-signature construction (partitioning by `k=Theta(log log N)` circuit wires) has the same gap: the mixed cell depends on Alice's circuit, while Bob must choose/routably certify it; merging the “not this cell” and matched-bit branches again creates cross-pairs whose missed mismatch is behind the scan. These failures kill those scan architectures only. No `N^(1+o(1))` DAG construction and no lower bound against arbitrary adaptive/revisiting DAGs is known.

Binary search for a disagreement does not repair the sharing step. The proposed node test “there is a mismatch in interval I” is jointly a predicate of the two inputs, and is not generally a rectangle. For `I={1,2}`, rows `00,01` and columns `10,00` give mismatch pairs `(00,10)` and `(01,00)`, but their cross-pair `(00,00)` has no mismatch in I. Therefore a single rectangle state cannot represent that branch while covering both histories. If Alice's row is fixed to one table, Bob can test the interval locally; sharing that test across rows recreates the forbidden product hull. A more elaborate DAG may cover the branch by multiple rectangles, but that cost is exactly what remains to bound.

## 6. Tree/DAG calibration and the correct comparison

For the same vertex-count measure, a tree is a DAG, so `DAGsize(R)<=Treesize(R)`. Thus “small protocol tree but large shared DAG” is impossible under matching definitions. The meaningful separation is communication bits/depth versus graph vertices, or the opposite vertex-count gap where DAG reuse makes a DAG smaller than every tree.

\[
\mathrm{DAGsize}(R)\le\mathrm{Treesize}(R).
\]

Thus “small protocol tree but large shared DAG” is impossible under matching definitions. The meaningful separation is **communication bits/depth versus graph vertices**, or the opposite vertex-count gap where DAG reuse makes a DAG smaller than every tree.

Two calibrations make this concrete:

* For the Karchmer-Wigderson relation of parity on `m` bits, protocol-tree size is formula size `Theta(m^2)`, while a shared circuit/DAG has `O(m)` gates. The gap comes from reuse of residual parity computations.
* For the artificial relation whose unique output on `(x,y) in {0,1}^m x {0,1}^m` is `x`, Alice sends `m` bits, but every correct DAG needs `2^m` distinct answer leaves. This is a bit-versus-vertex gap caused by a huge output alphabet. C-75 has only `2N` signed mismatch labels, so distinct-output counting can force at most `2N` leaves and cannot reach the required superlinear target.

For C-75 specifically, short description transmission proves low deterministic communication bits, while Sokolov/GGKS says shared-DAG size is the separator-circuit size. The open theorem must show that the actual Gap-MCSP promise forces many globally distinct residual separators—or exhibit a near-linear separator. Ordinary communication cost alone cannot decide which.

## 7. Next proof obligation and disposition

The exact local state condition is known; the missing part is a global, overlap-safe charge. A candidate theorem should attach to every state `v` a residual separator for the full union of histories that merge there, and prove that the residual separator families across states require more than `N^(1+epsilon)` nodes, or enough nodes to cross the `N^(3+3epsilon)/log N` compiler threshold. Any proposed charge must allow the structured `O(N)` routers of C-80/C-160 and the suffix reuse of C-209. The alternative decisive result is an explicit `N^(1+o(1))`-size separator/DAG for the complete promise.

No such charge or construction has been found. C-220 is a model audit and route-narrowing correction, not a Tier-1/2/3 breakthrough. The overall P-vs-NP goal remains open and active.

### Primary sources

- [Sokolov, *Dag-like Communication and Its Applications*](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download), especially Definitions 2.1–2.3 and Theorem 3.2.
- [Garg, Göös, Kamath, and Sokolov, *Monotone Circuit Lower Bounds from Resolution*](https://theoryofcomputing.org/articles/v016a013/v016a013.pdf), §2 for rectangle-, triangle-, and F-DAGs.
- [Cavalar and Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://doi.org/10.1145/3718746), especially the cyclic discrete complexity characterization.
- [Nakayama and Maruoka, *Loop Circuits and Their Relation to Razborov's Approximation Model*](https://doi.org/10.1006/inco.1995.1083).
- [Amano and Maruoka, *The Monotone Circuit Complexity of Quadratic Boolean Functions*](https://doi.org/10.1007/s00453-006-0073-0).
