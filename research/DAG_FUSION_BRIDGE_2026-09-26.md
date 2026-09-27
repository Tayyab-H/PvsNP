# Shared DAG, cyclic closure, and fusion: exact bridge audit (2026-09-26)

## Scope and result

This note continues C-74ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“C-76. It studies only the shared-DAG / cyclic-closure route for the Gap-MCSP fusion cover. The main result of this audit is a clean separation of three resources that had been conflated:

1. the number \(q\) of fusion pairs / cyclic AND states;
2. acyclic **conjunctive complexity**, which counts AND gates and leaves OR gates free;
3. ordinary binary-fanin circuit or rectangle-DAG size, which counts the OR machinery and must also eliminate cycles.

CavalarÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Oliveira prove the exact identity
\[
 \rho(A,\mathcal B)=D^\circ_\cap(A\mid\mathcal B),
\]
where the right side is the least number of intersections in a cyclic set construction. Thus the target cover lower bound is already exactly a cyclic conjunctive-complexity lower bound. An ordinary DAG lower bound is useful only after its conversion loss is written down.

## 1. The two search relations and their totality

Let \(N=2^n\), \(Y=\{w:\mathrm{CC}(w)\le s_1\}\), and \(Z=\{z:\mathrm{CC}(z)>s_2\}\). The active project cover is the **promise-domain** quantity: \(\Gamma_{\rm prom}=Y\sqcup Z\), with generator slices restricted to \(\Gamma_{\rm prom}\), and filter universe \(U_{\rm prom}=Z\). The promised mismatch relation is
\[
 \mathrm{Mis}_{Y,Z}(w,z)=\{(k,b):w_k=b,\ z_k=1-b\},
 \qquad (w,z)\in Y\times Z.
\]
It is total: \(w\ne z\), since \(s_1<s_2\), so some coordinate differs and exactly one of the two signed outputs \((k,b)\) is valid.

There is a stronger \(Q\)-dependent **closure-witness relation**. For a proposed pair list \(Q=((E_i,H_i))_{i=1}^q\), put \(T_i=E_i\cap H_i\) and compute the least closure activation bits \(x_i(v)\) from the literal seeds of any truth table \(v\). A witness consists of a path
\[
 i_0,i_1,\ldots,i_t;\quad (k,b)
\]
such that:

- \(T_{i_0}=\varnothing\), \(x_{i_0}(w)=1\), and \(x_{i_0}(z)=0\);
- each transition \(i_r\to i_{r+1}\) uses one side \(S_r\in\{E_{i_r},H_{i_r}\}\), with \(T_{i_{r+1}}\subseteq S_r\), \(x_{i_{r+1}}(w)=1\), and \(x_{i_{r+1}}(z)=0\);
- at the final state \(i_t\), one side \(S_t\) is false at \(z\) and has a true seed at \(w\), giving \(w_k=b\), \(z_k=1-b\), and the seed slice \(\{u\in U:u_k=b\}\subseteq S_t\).

The ordinary mismatch relation is total whether or not \(Q\) works. The closure-witness relation is total exactly when \(Q\) refutes every low anchor. This distinction matters: one cannot use totality of plain mismatch to assume a successful closure certificate.

**Why a witness path exists when \(Q\) succeeds.** Start at any empty-consequence rule activated on \(w\). No empty-consequence rule is activated on \(z\in U=\Gamma\setminus Y\): the principal semi-filter \(\{S\subseteq U:z\in S\}\) is above \(z\) and preserves every pair. At a state active on \(w\) and inactive on \(z\), at least one of its two sides is false in the closure of \(z\). That same side is true at \(w\), so its proof is either a matching literal seed (which differs at \(z\)) or a consequence \(T_j\) contained in the side. In the latter case \(j\) is active on \(w\), inactive on \(z\), and has strictly smaller least-fixed-point activation rank on \(w\). The rank decreases, so the path ends at a literal mismatch in at most \(q\) transitions.

This is a useful *ranked cyclic search certificate*, not yet a standard acyclic communication DAG.

## 2. Exact models and transformations

| Model | Object and size measure | Cycles? | Relation to the fusion state system |
|---|---|---:|---|
| Deterministic tree protocol | Transcript tree; cost is worst-case communicated bits/depth, size is tree nodes/leaves | No | C-75 gives \(O(q\log(N+q))\) bits for the rule-following witness path. This is not a useful size lower bound: a size-\(c\) protocol may have \(2^{\Theta(c)}\) tree nodes. |
| Sokolov Boolean communication game / rectangle-DAG | Rooted DAG; each node has local predicates \(A_v(w)\), \(B_v(z)\). Its valid inputs form the rectangle \(\{w:A_v(w)=1\}\times\{z:B_v(z)=0\}\). A valid node's rectangle is covered by its at most two children; leaves carry valid outputs. Size is the number of graph nodes. | No | This is the state-sharing model relevant to KarchmerÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Wigderson. Sokolov proves the DAG analogue of the formula/circuit correspondence. GargÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“GÃƒÆ’Ã‚Â¶ÃƒÆ’Ã‚Â¶sÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“KamathÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Sokolov use rectangle-DAGs; for the full monotone KW relation of a monotone function, their size measure equals monotone circuit size. |
| Communication PLS game | Fixed state graph plus an input-dependent local successor strategy; size is states, with a separate worst-case communication cost \(t\) for checking a state and choosing a successor | The standard definition uses an acyclic graph | A Boolean communication game of size \(L\) gives a PLS game of size \(L\) and communication cost at most 2. Conversely Sokolov's simulation turns a PLS game of size \(L\), cost \(t\), into a Boolean game of size at most \(L2^{3t}\). This conversion can be expensive when \(t=\Theta(\log N)\). |
| CavalarÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Oliveira cyclic discrete complexity | Synchronous least-fixed-point evaluation of \(t\) set equations; \(D^\circ_\cap\) counts only intersection operations, with unions uncharged | Yes | Their exact theorem is \(\rho(A,\mathcal B)=D^\circ_\cap(A\mid\mathcal B)\). This is the native measure of the fusion closure. |
| Acyclic intersection / conjunctive complexity | Acyclic monotone set circuit; \(D_\cap\) counts intersections/AND gates, unions/OR gates are free | No | \(D^\circ_\cap\le D_\cap\le (D^\circ_\cap)^2\). Thus a cyclic fusion cover of \(q\) pairs has an acyclic realization with at most \(q^2\) AND gates, with no dependence on \(|\mathcal B|\). |
| NakayamaÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka loop circuits | Cyclic circuits in the generalized approximation framework; size is loop-circuit size | Yes | Related in spirit, but not an automatic model identity: CavalarÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Oliveira explicitly note that the NM95 formulation does not directly imply their result because its functionals differ from the monotone semi-filters used in \(\rho\). |
| AmanoÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka conjunctive complexity | Minimum number of AND gates in an ordinary monotone circuit; their paper studies quadratic Boolean functions, including a gap between single-level and general circuits | No | Closest acyclic resource analogue to \(D_\cap\), but their theorems are for quadratic functions, not the Gap-MCSP characteristic function or its promise separators. |

Primary definitions/results: [Sokolov, *Dag-like Communication and Its Applications* (ECCC revision)](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download); [GargÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“GÃƒÆ’Ã‚Â¶ÃƒÆ’Ã‚Â¶sÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“KamathÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Sokolov, *Monotone Circuit Lower Bounds from Resolution*](https://jakobnordstrom.se/docs/publications/GGKS18_MonotoneCircuitLBsResolution.pdf); [CavalarÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://arxiv.org/abs/2503.14117); [NakayamaÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka, *Loop Circuits and Their Relation to Razborov's Approximation Model*](https://doi.org/10.1006/inco.1995.1083); [AmanoÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka, *The Monotone Circuit Complexity of Quadratic Boolean Functions*](https://doi.org/10.1007/s00453-006-0073-0).

## 3. Exact cover-to-state conversion, then the acyclic losses

For \(Q\), define \(X_i=\{v\in\Gamma:x_i(v)=1\}\), and let \(A_i,B_i\) be the two literal-seed sets. The equations are
\[
 X_i^{t+1}=
 \left(A_i\cup\bigcup_{j:T_j\subseteq E_i}X_j^t\right)
 \cap
 \left(B_i\cup\bigcup_{j:T_j\subseteq H_i}X_j^t\right).
\]
The iteration starts at \(\varnothing\); the least fixed point is reached after at most \(q\) strict rounds. Because the iteration is increasing, it is equivalently written with a persistence union:
\[
 X_i^{t+1}=X_i^t\cup
 \left[
 \left(A_i\cup\bigcup_{j:T_j\subseteq E_i}X_j^t\right)
 \cap
 \left(B_i\cup\bigcup_{j:T_j\subseteq H_i}X_j^t\right)
 \right].
\]
Each rule contributes exactly one cyclic AND/intersection. The ORs collect the admissible literal seeds and earlier consequences. The output is the OR of the states with \(T_i=\varnothing\). For the active promise-domain list, it is 1 on \(Y\) and 0 on \(Z\); its value on the medium band \(M=\Gamma_{\rm full}\setminus(Y\cup Z)\) is unconstrained. This is a separator extension, not necessarily the exact characteristic function of \(Y\). A different full-domain cover takes \(\Gamma_{\rm full}=\{0,1\}^{N}\) and \(U_{\rm full}=\Gamma_{\rm full}\setminus Y=M\cup Z\). The principal-filter argument applies to that distinct cover, but a promise-domain pair list cannot simply be treated as a full-domain one (C-79/C-90).

Consequently, for the active promise-domain measure:
\[
q=\rho_{\rm prom}(Y,Z,\mathcal B)=D^\circ_\cap(Y\mid\mathcal B_{\rm prom})
\]
for a minimum pair list, by the CavalarÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Oliveira exact characterization. This is an exact cyclic-complexity identity on \(\Gamma_{\rm prom}\), not on the full truth-table cube.

For the acyclic conversion:

- **AND count only:** the cyclic-to-acyclic unfolding theorem gives at most \(q^2\) AND gates. This is the strongest quantitative conversion found for the target resource, because \(\rho\) counts intersections and charges no unions.
- **Ordinary binary-fanin gate count:** explicitly unrolling \(q\) rounds creates \(O(q^2)\) AND/OR *macro-gates* with unbounded fan-in. Expanding each state-support OR over up to \(q\) previous states, and computing the \(2q\) seed clauses over up to \(N\) literals, gives a safe binary-fanin size bound \(O(q^2(q+N))\). The seed clauses can be computed once, yielding \(O(q^3+qN)\). Since any successful \(Q\) already has \(q\ge N-o(N)\), this is \(O(q^3)\). The exact constant/fanin convention is not important here; the cubic loss is.
- **Rect-DAG view:** translating the binary monotone circuit to its KW rectangle-DAG gives the same \(O(q^3)\) vertex bound. A direct rule-state graph has only \(q\) rule vertices and \(O(q^2+qN)\) possible transition/support edges, but it may contain cycles. A standard rect-DAG must be acyclic, so the \(q\)-state graph cannot be counted as a \(q\)-vertex DAG without a proof that those cycles are removable.

Thus, to obtain \(q>N^{1+\epsilon}\) from ordinary binary rect-DAG size alone using this generic conversion, one would need a lower bound exceeding \(N^{3+3\epsilon}\) (up to constants). If the lower bound is specifically on acyclic AND-gate count for separators, the \(q^2\) conversion means a bound above \(N^{2+2\epsilon}\) would suffice. Neither lower bound has been obtained here. This identifies the exact exponent losses that a new argument must avoid.

## 4. Why the rank does not make this an ordinary DAG

For every rule \(i\), let
\[
R_i=\{w:x_i(w)=1\}\times\{z:x_i(z)=0\}.
\]
This is a rectangle. On each input pair in \(R_i\), a false side at \(z\) and a true support at \(w\) lead either to a signed mismatch leaf or to some \(R_j\). Along every actual transition, the activation rank on \(w\) decreases. Hence the \(q\) state rectangles with their support transitions form a terminating *cyclic* search system.

The static dependency graph need not be acyclic. A two-state example already has both edges \(1\to2\) and \(2\to1\):
\[
x_1=(a_1\vee x_2)\wedge b_1,\qquad
x_2=(a_2\vee x_1)\wedge b_2.
\]
With seed pattern \((a_1,b_1,a_2,b_2)=(1,1,0,1)\), state 1 activates at rank 1 and state 2 at rank 2. With \((0,1,1,1)\), state 2 activates at rank 1 and state 1 at rank 2. The graph has a cycle, but no valid support path cycles on either input. This proves that input-dependent rank termination does not give a global topological ordering of the rule states.

An ordinary acyclic expansion can tag a rule by a remaining round/rank budget, producing up to \(q^2\) rule-layer states before support-selection circuitry. The activation-rank proof is therefore a candidate language for a new *ranked cyclic rectangle game*, not a shortcut that already yields a standard rect-DAG lower bound.

## 5. Reverse direction: what a DAG lower bound would and would not imply

For the **active promise-domain measure**, the reverse direction succeeds with constant-factor loss. An \(L\)-vertex rect-DAG for \(\mathrm{Mis}_{Y,Z}\) yields an \(O(L)\)-size separator circuit by C-89. Restrict that circuit's AND/OR set construction to \(\Gamma_{\rm prom}=Y\sqcup Z\). Then
\[
\rho_{\rm prom}(Y,Z,\mathcal B_{\rm prom})\le D_\cap(Y\mid\mathcal B_{\rm prom})\le D(Y\mid\mathcal B_{\rm prom})=O(L).
\]
Thus a small shared DAG for the actual promise gives a small fusion cover for that same promise; no medium-band condition is needed for this direction.

There is a separate **full-domain** cover \(\rho_{\rm full}\), whose universe includes \(M\). A promise separator circuit may accept medium tables, so it does not compute exact membership in \(Y\), and the previous implication does not produce a full-domain cover. C-79 proves that simply embedding endpoints from \(Z\) fails: a semi-filter generated by the medium band and matching slices can escape every such pair. This blocks direct endpoint reuse, not the promise-domain reverse conversion, and does not rule out a conversion that adds medium-band pairs.

## 6. Universal DAG attempts from short circuit descriptions

Let \(d\) be a syntactic size-\(s_1\) circuit description and \(G(d)\in\{0,1\}^N\) its truth table. The relation \(\mathrm{Mis}_{Y,Z}\) remains total when Alice is given \(d\) instead of \(w\), by mapping \(d\mapsto G(d)\). Multiple descriptions may collide. The right semantic domain is the set of distinct low truth tables; local computation may choose a canonical description at no communication cost, but a DAG-size proof cannot count or identify all canonical descriptions for free in its *graph topology*.

Attempts audited:

- **Send \(d\), then compare:** valid as an ordinary protocol with \(O(s_1\log s_1+\log N)\) bits (C-75). Its binary tree may have exponentially many nodes. The communication-cost upper bound says nothing about shared-DAG size.
- **Universal-circuit evaluation:** a universal circuit can jointly evaluate \(G(d)_k\) and compare it with \(z_k\), but those are mixed Alice/Bob operations. A communication-DAG node must describe a rectangle, and the predicate ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œthere exists a mismatch in interval \(I\)ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â is generally not a rectangle. For a two-coordinate illustration, take Alice rows \(00,11\) and Bob columns \(00,11\); the mismatch predicate is 0 on the diagonal and 1 off-diagonal, so it is not a rectangle.
- **Binary search over mismatch locations:** each interval query is exactly the non-rectangular joint predicate above. The parties need a protocol to resolve it; binary search does not come for free from having a universal evaluator.
- **Hashing/sampling:** a high table must differ from a low table in at least \(\Omega(s_2/\mathrm{poly}(n))\) positions by the elementary ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œpatch the differing positionsÃƒÂ¢Ã¢â€šÂ¬Ã‚Â circuit bound. At OPS parameters this is only \(N^\beta/\mathrm{polylog}(N)\). Since the high side contains almost all truth tables, \(\log(|Y||Z|)=N+o(N)\); a direct union bound over every low/high pair therefore asks for more than N coordinate samples, so it gives no sublinear universal set. Independently, cylinder counting shows a fixed coordinate set must have size at least \(N-\log_2 M_2=N-o(N)\) to distinguish all low/high pairs. This kills the naive fixed-sample argument, not every possible structured hash.
- **Nonuniform preprocessing:** endpoints and rectangle predicates are semantic sets, so their description lengths are not charged. The hard quantity is the number and dependency of shared states. Listing one state per low table is an upper bound of roughly \(|Y|N\), not a lower bound; states might share. Proving or refuting that sharing is the open target.

No universal DAG of size \(N^{1+o(1)}\) was constructed, and no lower bound against it was proved. Short individual descriptions do not by themselves imply cheap state sharing.

## 7. Tree versus DAG calibration and the target's actual gap

A clean artificial calibration comes from parity. For \(f(x)=\mathrm{PARITY}_N(x)\), the Bit relation between \(f^{-1}(1)\) and \(f^{-1}(0)\) has a DAG-like protocol of size \(O(N)\), because parity has a linear-size Boolean circuit. Its tree-like protocol size equals Boolean formula size and is \(\Omega(N^2)\) by the Khrapchenko formula lower bound (the edge count between parity classes is \(N2^{N-1}\), while both classes have size \(2^{N-1}\)). Thus sharing can give a genuine polynomial saving.

This only calibrates the distinction. It does not model the target's cyclic AND measure: parity is non-monotone, and its DAG's gates include both conjunctions and disjunctions. The fusion target allows arbitrary unions free and counts cyclic intersections. The corresponding target-specific challenge is stronger: show that shared OR/support routing cannot compress the cyclic AND states for the full low-circuit language.

## 8. Next proof target

The sharp formulation suggested by this audit is:

> **Promise-domain cyclic conjunctive non-shareability.** On \(\Gamma_{\rm prom}=Y\sqcup Z\), with the \(2N\) literal generators restricted to that domain, every cyclic monotone conjunctive construction that is 1 on Y and 0 on Z needs more than \(N^{1+\epsilon}\) intersections: \(D^\circ_\cap(Y\mid\mathcal B_{\rm prom})=\rho_{\rm prom}>N^{1+\epsilon}\). Its Boolean extension on medium tables is irrelevant to this parameter.

Equivalent fusion statement for the active promise ground set: \(\rho_{\rm prom}(Y,Z,\mathcal B_{\rm prom})>N^{1+\epsilon}\). This is distinct from the full-domain exact low-set cover \(\rho_{\rm full}\).

Define \(\operatorname{SepAnd}(Y,Z)\) as the least number of AND gates in any acyclic monotone circuit on the \(2N\) signed-literal inputs that is 1 on every one-hot encoding of \(Y\) and 0 on every one-hot encoding of \(Z\); OR gates are free, and values on the medium band and invalid encodings are unrestricted. Every successful q-pair cover supplies one feasible circuit, and the cyclic-to-acyclic inequality gives \(\operatorname{SepAnd}(Y,Z)\le D_\cap(Y\mid\mathcal B)\le q^2\). Therefore the concrete sufficient lemma is
\[
\operatorname{SepAnd}(Y,Z)>N^{2+2\epsilon}\quad\Longrightarrow\quad
\rho(Y,\mathcal B)>N^{1+\epsilon}.
\]
The binary rect-DAG version has the weaker cubic conversion target \(>N^{3+3\epsilon}\), because it charges the OR routing as well. No such separator lower bound has been proved here.

The new object to study is a **ranked cyclic rectangle certificate**: \(q\) shared rectangles \(R_i\), a cyclic dependency relation induced by the two fusion sides, and a per-Alice-input rank that decreases on every valid transition. The research question is whether bottleneck counting or a direct non-shareability invariant can lower-bound the number of these cyclic states without first unfolding them.

## Source notes

- CavalarÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Oliveira define cyclic discrete complexity by synchronous least-fixed-point iteration from empty, prove convergence in at most \(t\) rounds for \(t\) states, show \(D^\circ_\cap\le D_\cap\le(D^\circ_\cap)^2\), and prove the exact cover identity \(\rho=D^\circ_\cap\). They also explicitly distinguish their semi-filter/intersection formulation from NakayamaÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka's approximation-model formulation.
- Sokolov defines Boolean communication games by local Alice/Bob Boolean predicates and valid rectangles, relates them to DAG-like protocols and circuits, and separately defines PLS games with an acyclic state graph plus communication cost.
- GargÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“GÃƒÆ’Ã‚Â¶ÃƒÆ’Ã‚Â¶sÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“KamathÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Sokolov define rectangle-DAGs and connect their size to monotone KW / monotone circuit size. Their paper notes unresolved lifting questions for some richer feasible-set families; those results do not directly cover this cyclic fusion state model.
- Khrapchenko's formula bound gives the parity tree-size calibration; see the original [1971 paper record and full text](https://www.mathnet.ru/php/archive.phtml?jrnid=mzm&option_lang=eng&paperid=7071&wshow=paper).
- AmanoÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka's conjunctive complexity is the minimum AND-gate count in acyclic monotone circuits. Their explicit exponential single-level/general gap for a quadratic function motivates respecting sharing depth, but it is not a theorem about Gap-MCSP.

## 9. C-78 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Exact shared-DAG audit and quantitative conversions

This section addresses the continuation request's immediate questions. It refines, rather than replaces, C-77.

### 9.1 Search relations, who knows what, and totality

Set (N=2^n), (Y={win{0,1}^N:mathrm{CC}(w)le s_1}), and (Z={z:mathrm{CC}(z)>s_2}). Alice receives the full (N)-bit table (win Y); Bob receives (zin Z). Their ordinary output relation is

\[
\mathrm{Mis}_{Y,Z}(w,z)=\{(k,b):w_k=b,\ z_k=1-b\}.
\]

It is total because (Y\cap Z=\varnothing). Alice may instead receive a description (d) with (G(d)=w); descriptions can collide, but this does not change the relation.

For a fixed pair list (Q=((E_i,H_i))_{i=1}^q), put (T_i=E_i\cap H_i), and let (x_i(v)) be the least-fixed-point activation bit for table (v). Define the stricter witness relation (\mathrm{Path}_Q(w,z)) to output a finite sequence of rule indices and sides, ending with a signed literal ((k,b)), such that:

1. the first state has (T_{i_0}=\varnothing), (x_{i_0}(w)=1), and (x_{i_0}(z)=0);
2. at each visited state (i), the selected side (S\in\{E_i,H_i\}) is unsupported in the closure for (z), but is supported for (w) either by a matching literal or by a state (j) with (T_j\subseteq S);
3. a state-support transition goes to (j) with strictly smaller first-activation rank on (w), and the terminal literal satisfies (w_k=b\ne z_k).

For every successful cover, this relation is total on (Y\times Z). If (Q) misses even one low anchor, it is not total. The plain mismatch relation is total independently of (Q); these must not be conflated.

### 9.2 Complexity measures kept separate

| Measure | Object counted | Bound for these relations |
|---|---|---|
| Deterministic communication cost | Worst-case exchanged bits | For plain mismatch, Alice sends a circuit description and Bob returns a differing index: (O(s_1\log(n+s_1)+\log N)). For the annotated path output, following the (Q)-witness uses (O(q\log(q+N))) bits. |
| Ordinary protocol-tree size | Tree nodes, not bits | A protocol of cost (c) has at most (2^{c+1}-1) nodes. Thus the description protocol gives at most (2^{O(s_1\log(n+s_1))}\,\mathrm{poly}(N)) nodes; this is not a near-linear shared DAG. |
| Sokolov Boolean communication game / rectangle-DAG | Number of vertices in an acyclic graph of fan-out at most two; every node is a rectangle and each parent rectangle lies in the union of its children | Any protocol tree yields a tree-shaped game. The bounds above yield only the corresponding exponential-in-communication upper bounds in general. |
| Communication PLS game | Vertices in an acyclic state graph, plus a separate communication cost for state membership and successor selection | A size-(L), cost-(t) PLS game converts to a Boolean game of size at most (L2^{3t}); conversely a Boolean game of size (L) gives a PLS game of the same size and cost at most two. The standard model is acyclic. |
| Fusion / cyclic intersection | Number of intersection states; unions/support collection are uncharged | Exactly (q=D^\circ_\cap(Y\mid\mathcal B)=\rho(Y,\mathcal B)). This is the projectÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s native shared-state measure, but it is not a standard acyclic rectangle-DAG. |

Sokolov's Boolean game assigns each node separate local predicates on Alice's and Bob's input; its feasible pairs form a rectangle. GGKS's rectangle-DAG has the same binary-cover condition and gives the monotone circuit characterization for the *full* monotone KarchmerÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Wigderson relation. Neither theorem says that every partial low/high mismatch DAG yields a circuit for exact low-set membership.

### 9.3 Explicit (Q\to\) acyclic rect-DAG construction

The (q) rule states alone need not form an acyclic graph. The static containment relation can cycle: for example, on a four-element ambient set, take

\[
T_1=\{a,b\},\quad E_1=\{a,b,c\},\quad H_1=\{a,b,d\},
\qquad
T_2=\{a,c\},\quad E_2=\{a,b,c\},\quad H_2=\{a,c,d\}.
\]

Then (T_2\subseteq E_1) and (T_1\subseteq E_2), so the rule-dependency graph has a 2-cycle. The witness path is nevertheless well-founded on each low input because first-activation rank decreases. A standard DAG must encode that rank somehow.

Here is an explicit binary rect-DAG simulation. Let \(\tau_i(w)\) be the first round in which state (i) activates at (w), and define

\[
R_{i,r}=\{w\in Y:\tau_i(w)\le r\}\times\{z\in Z:x_i(z)=0\},\qquad 1\le r\le q.
\]

The root (Y\times Z) first branches, using row-only rectangles, to an empty-consequence rule active on (w); this costs (O(q)) vertices. At (R_{i,r}), Bob chooses a side false at (z). Alice then chooses one true support of that side at (w). A literal support ends at its signed mismatch leaf. A rule support (j) satisfies (T_j\subseteq S), (	au_j(w)\le r-1), and (x_j(z)=0), so the next state is (R_{j,r-1}). Each side has at most (q+N) possible supports; binary trees that partition Alice's anchor set by a first valid support and Bob's high-table set by the false side cost (O(q+N)) vertices per ((i,r)). Thus

\[
\operatorname{rectdag}(\mathrm{Mis}_{Y,Z})\le O\bigl(q+q^2(q+N)\bigr)=O(q^3),
\]

using the already-proved (q\ge N-o(N)). This is a valid DAG protocol for the plain mismatch relation. It improves on no asymptotic barrier: to force (q>N^{1+\varepsilon}) through this generic conversion would require a rect-DAG lower bound (>N^{3+3\varepsilon}).

There is a compact *custom* loop-game view with (q) rule states and input-dependent rank, but this is not Sokolov's PLS or a rect-DAG: the underlying state graph may cycle, and the side/support transition is selected from semantic input predicates. Counting only (q) rule states while silently treating the graph as acyclic is invalid. In the usual acyclic PLS model one may layer by rank, using (O(q^2+N)) vertices and (O(\log(q+N))) communication to select a successor; the generic PLS-to-Boolean-game conversion is then (O((q^2+N)(q+N)^3)), worse than the direct (O(q^3)) rect-DAG construction.

The (q^2) conversion remains strongest when counting only AND gates: (D_\cap\le q^2). Its OR/support network is free in (D_\cap), whereas a binary rect-DAG must pay to route over those supports.

### 9.4 Reverse direction and the exact role of the promise

There is an exact reverse equivalence for the *promise separator circuit*, even when medium tables are ignored. Define \(\mathrm{SepCirc}(Y,Z)\) as the minimum size of a Boolean circuit h on N truth-table bits with h(w)=1 for every w in Y and h(z)=0 for every z in Z.

An L-vertex rect-DAG for \(\mathrm{Mis}_{Y,Z}\) yields an \(O(L)\)-size separator circuit. At a leaf labelled by the mismatch \(w_k=b\ne z_k\), use the literal \(x_k\) if b=1 and \(\neg x_k\) if b=0; the leaf rectangle fixes those opposite bits. For an internal node v with child rectangles \(R_0,R_1\) covering \(R_v\), the rectangle lemma says either the row side of \(R_v\) lies in both child row sides, the column side lies in both child column sides, or \(R_v\) is contained in one child. In the three cases combine the child circuits by AND, OR, or reuse one child. The root circuit is 1 on Y and 0 on Z.

Conversely, a size-C circuit h separating Y from Z has a Boolean KarchmerÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Wigderson game for the full sets \(h^{-1}(1),h^{-1}(0)\) of size \(O(C)\) by Sokolov's Theorem 3.2; restricting its input sets to Y and Z gives a rect-DAG for \(\mathrm{Mis}_{Y,Z}\). Hence

\[
\mathrm{rectdag}(\mathrm{Mis}_{Y,Z})=\Theta(\mathrm{SepCirc}(Y,Z))
\]

up to the fixed basis constants. This is a precise identification of the shared-DAG target with ordinary Boolean circuit complexity of a *promise separator*.

Combined with C-78, a q-pair fusion cover gives

\[
\mathrm{SepCirc}(Y,Z)=O(q^2(q+N))=O(q^3).
\]

Therefore a separator lower bound \(\mathrm{SepCirc}(Y,Z)>N^{3+3\varepsilon+\delta}\) for any fixed \(\delta>0\) implies \(q=\Omega(N^{1+\varepsilon+\delta/3})>N^{1+\varepsilon}\) for large N, then \(P\ne NP\) by the existing OPS magnification bridge. Equivalently, one may state the threshold with an explicit constant margin. This is the cleanest inequality chain for this phase.

For the active promise-domain cover, a separator circuit or rect-DAG does yield a cover with \(O(S)\) pairs by C-02; hence \(\rho_{\rm prom}\le \mathrm{SepCirc}\asymp\mathrm{rectdag}\). The medium band matters only when upgrading to the distinct full-domain cover \(\rho_{\rm full}\). C-79 shows that keeping endpoints inside Z cannot perform that upgrade. Therefore the exact relations are asymmetric:
\[
\rho_{\rm prom}\le \mathrm{SepCirc}(Y,Z)\asymp\mathrm{rectdag}(\mathrm{Mis}_{Y,Z})\le O(\rho_{\rm prom}^{3}),
\]
with the final cubic bound from C-78. This still leaves a cubic loss when using a generic acyclic-DAG lower bound to prove a direct \(\rho_{\rm prom}\) lower bound.

### 9.5 A stronger universal mismatch DAG from restriction sharing

Let (m=|Y|), and for a coordinate interval (I\subseteq[N]) let \(\pi_I(Y)=|\{w|_I:w\in Y\}|\). A valid shared DAG can first branch on Alice's row to one of the (m) singleton rows; this takes (O(m)) vertices. For each dyadic interval (I) and pattern (u\in\{0,1\}^{I}) appearing as a restriction of a low table, create the rectangle

\[
R_{I,u}=\{w\in Y:w|_I=u\}\times\{z\in Z:z|_I\ne u\}.
\]

For a non-singleton interval, connect it to the two child-interval rectangles with the corresponding restrictions of (u). A pair in (R_{I,u}) differs somewhere in (I), so it lies in at least one child; a leaf interval outputs its signed mismatch. The child row class may be larger than the parent row class, which is permitted by the rect-DAG cover condition. This gives

\[
S_{\rm universal}\le O\left(m+\sum_{I\text{ dyadic}}\pi_I(Y)\right)
\le O\left(m+\sum_{\ell=0}^{\log N}2^\ell\min\{m,2^{N/2^\ell}\}\right).
\]

The second expression is (O(mN/\log m+N\log N)) up to absolute constants when (m\) is large. This improves on independently attaching an (O(N)) scan to each low table, but with the current (m\le2^{O(s_1\log(n+s_1))}) it is nowhere near (N^{1+o(1)}). No lower bound follows from this construction; it is an upper bound for one protocol architecture.

The attempted universal-circuit shortcut still fails at the rectangle condition. Computing (C_d(k)\oplus z_k) or ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œthere is a mismatch in interval (I)ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â centrally mixes Alice's and Bob's inputs. Even the 2-by-2 restriction with rows/columns (\{00,11\}) has the mismatch set off-diagonal, which is not a rectangle. A sequential scan's state ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œall earlier bits agreeÃƒÂ¢Ã¢â€šÂ¬Ã‚Â is a union of prefix-pattern rectangles; merging those histories into one state can add cross-pairs whose earlier coordinates already disagree. The restriction-sharing construction above repairs this only by retaining pattern-indexed rectangles. This is a precise failure of naive universal evaluation, not a proof that every possible shared DAG is large.

### 9.6 Tree/DAG calibration: depth, node count, and sharing

Two different separations need to be kept distinct.

- **Tree size versus DAG size:** parity on (n) bits has a DAG/circuit of (O(n)) gates but requires \(\Omega(n^2)\) formula size by Khrapchenko; the corresponding KW protocol tree is therefore quadratic while its shared DAG is linear. Here ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œtree complexityÃƒÂ¢Ã¢â€šÂ¬Ã‚Â means number of nodes, not communication bits.
- **Communication bits versus DAG size:** by counting, some (n)-bit Boolean function requires (\Omega(2^n/n)) circuit gates. Its full KW DAG has that size by the circuit/game characterization, although Alice can send her (n)-bit input and Bob can return a disagreeing coordinate using only (O(n+\log n)) communicated bits. The protocol tree may have exponentially many nodes. Thus low communication cost does not imply a small shared DAG.

There cannot be a small-node protocol tree and a larger minimum DAG for the same relation, since every tree is already a DAG and a DAG can share nodes. The relevant gap is low *depth/bits* with many tree nodes, or a large tree whose repeated subcomputations collapse in a DAG.

### 9.7 Quantitative status and next target

| Candidate lower bound | Transfer to (q=\rho) | Required scale for target (q>N^{1+\varepsilon}) |
|---|---:|---:|
| Promise-domain cyclic (D^circ_cap on Y sqcup Z) | equality | (>N^{1+epsilon}) (the target itself) |
| Acyclic AND-only exact/valid separator bound | (D_\cap\le q^2) | (>N^{2+2\varepsilon}) |
| Standard binary rect-DAG obtained by the explicit unrolling | (S\le O(q^3)) | (>N^{3+3\varepsilon}) |
| Ordinary communication cost | tree has (2^{O(c)}) nodes | no useful near-lossless transfer |

The highest-value immediate lemma remains a lower bound on the number of distinct compatible *residual rectangles* a successful Q must expose. The projection-profile construction shows how states can be shared whenever interval restrictions agree; it does not prove that a general DAG must expose all those states. C-79 below blocks upgrading to the full-domain exact cover; C-90 proves the reverse map to the active promise cover.

## 10. C-79 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Medium-band escape filter (proved)

This is a rigorous reason that a low/high promise separator's cover cannot simply be re-used for the low set.

### Lemma (every signed coordinate cylinder contains a medium table)

Assume (s_2=2^{\beta n}), (s_1=s_2/(c n)), and the standard circuit-counting bound

\[
|\mathrm{SIZE}(t)|\le 2^{C_0 t\log_2(n+t+2)}.
\]

For every sufficiently small fixed \(\beta>0\), every truth-table coordinate (a\in\{0,1\}^n), and each sign (b\in\{0,1\}), there is a table (v\) with

\[
s_1<\mathrm{CC}(v)\le s_2,\qquad v_a=b.
\]

**Proof.** Take (k\le n) with (m=2^k\in[s_2/32,s_2/16]), possible for large (n) because \(\beta<1\). Every Boolean function on the first (k) input bits is the OR of a chosen subset of the (m) minterms. A shared prefix-decoder computes all (m) minterms using (O(m)) fan-in-two gates, and the final OR costs (O(m)); with the constants in the interval chosen smaller if needed, every such lifted function has circuit size at most (s_2). At the fixed input (a), exactly half of the (2^m) functions have value (b). Thus at least (2^{m-1}) distinct tables in the cylinder (v_a=b) have size at most (s_2). The number with size at most (s_1) is at most

\[
2^{C_0s_1\log_2(n+s_1+2)}=2^{(C_0\beta/c+o(1))s_2}.
\]

Choose the fixed \(\beta\) small enough that (C_0\beta/c<1/64); since (m\ge s_2/32), the low-table count is strictly smaller than (2^{m-1}) for large (n). At least one table in the cylinder is therefore medium. \(\square\)

### Corollary (high-only endpoints miss a low-anchor filter)

Let (U_Y=\Gamma\setminus Y=M\cup Z), fix any (w\in Y), and let (L_{k,w_k}\) be the matching literal slice at coordinate (k). Define

\[
\mathcal G_w=\{M\}\cup\{L_{k,w_k}\cap U_Y:k\in[N]\},\qquad
\mathcal F_w=\{S\subseteq U_Y:\exists G\in\mathcal G_w,\ G\subseteq S\}.
\]

Each generator is nonempty; hence \(\mathcal F_w\) is an upward-closed nonempty family excluding \(\emptyset\), and it is above (w). By the lemma, every matching slice contains a point of (M). If (E\subseteq Z), then (E\) contains neither (M) nor any matching slice, so (E\notin\mathcal F_w). Therefore every pair ((E,H)) with both endpoints in (Z) is preserved by \(\mathcal F_w\) vacuously. In particular, **no list of pairs whose endpoints all lie in (Z)**ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âincluding any cover designed for the larger positive class \(\mathrm{SIZE}(s_2)\)ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âcovers the low-anchor filter \(\mathcal F_w\) over (U_Y).

This proves failure of the direct endpoint-reuse/monotonicity transformation. It does not preclude a reverse reduction that constructs additional pairs involving the medium band, and it does not itself improve the lower bound on \(\rho(Y,\mathcal B)\).

### Consequence for the route

The shared-DAG line is not killed: it has yielded (i) an exact cyclic state interpretation, (ii) a valid (O(q^3)) standard rect-DAG simulation, (iii) a pattern-sharing universal-DAG upper bound, and (iv) a proved promise-to-exact reverse-transfer obstruction. But the requested Tier 1ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“3 result is still missing. The immediate proof target is now a genuine residual-rectangle non-shareability theorem for the MCSP low/high relation or a direct superlinear lower bound on (D^\circ_\cap); the pattern projection counts are candidate statistics, not yet lower bounds.

### Primary literature checked for this phase

- Sokolov, [*Dag-like Communication and Its Applications*](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download): Boolean communication games and rectangles (Definitions 2.1ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“2.3), PLS games and the (L2^{3t}) conversion (Theorem 3.1), and the circuit/game correspondence (Theorem 3.2).
- GargÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“GÃƒÆ’Ã‚Â¶ÃƒÆ’Ã‚Â¶sÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“KamathÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Sokolov, [*Monotone Circuit Lower Bounds from Resolution*](https://jakobnordstrom.se/docs/publications/GGKS18_MonotoneCircuitLBsResolution.pdf): rectangle-DAG definition and full monotone KW characterization; their lower bounds use gadget lifting and do not directly apply to this promise/cyclic model.
- CavalarÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Oliveira, [*Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://arxiv.org/html/2503.14117): Theorem 30 gives \(\rho=D^\circ_\cap\); the authors explicitly say their theorem adapts NakayamaÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka and differs in using monotone semi-filters/intersection complexity rather than general functionals/generalized approximation.
- NakayamaÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka, [*Loop Circuits and Their Relation to Razborov's Approximation Model*](https://doi.org/10.1006/inco.1995.1083): the source of the loop-circuit connection, but not an identity for the present semi-filter cover without the CavalarÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Oliveira adaptation.
- AmanoÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka, [*The Monotone Circuit Complexity of Quadratic Boolean Functions*](https://doi.org/10.1007/s00453-006-0073-0): conjunctive complexity counts AND gates in acyclic monotone circuits; their results concern quadratic functions, including a single-level/general gap, and do not establish a Gap-MCSP separator lower bound.
- AustrinÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Risse, [*Sum-of-Squares Lower Bounds for the Minimum Circuit Size Problem*](https://eccc.weizmann.ac.il/report/2023/010/download): they prove degree lower bounds for SoS proofs that a fixed truth table has no circuit of size \(s\), and analogous results for minimum monotone circuit size of monotone slice functions. These are proof-system lower bounds for certifying circuit lower bounds; they are not lower bounds on the AND-gate/rect-DAG complexity of the MCSP characteristic separator \(Y\) versus \(Z\). No implication between these measures is used here.

## 11. C-80 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â A huge low code family can have an \(O(N)\) shared mismatch DAG

This kills the idea that a large low-code subfamily by itself forces a large shared DAG.

Choose \(k\) so \(m=2^k\in[s_1/16,s_1/8]\), and let \(B=N/m\). Partition the \(N\) truth-table coordinates into the \(m\) equal blocks indexed by the first \(k\) bits of the input. Let \(Y_k\) consist of all truth tables that are constant on every block. Every Boolean function on \(k\) variables has a shared prefix decoder that constructs all \(m\) minterms using \(2m+O(1)\) gates; ORing a selected subset costs at most \(m-1\) more. With these constants, all \(2^m\) block-constant tables have circuit size below \(s_1\), so \(Y_k\subseteq Y\), and \(|Y_k|=2^m=2^{\Theta(s_1)}\).

Every \(z\in Z\) must be mixed on some block: if it were constant on each block, it would itself be block-constant and hence have size at most \(s_1<s_2\). This gives a small DAG for \(\mathrm{Mis}_{Y_k,Z}\): Bob searches for a mixed block \(j\) using a binary interval tree over the \(m\) blocks (\(O(m)\) vertices); Alice's row is then split by its common value \(b\) on that block; Bob searches within the block for a coordinate with value \(1-b\). The latter takes \(O(B)\) rectangle states per pair \((j,b)\), hence \(O(mB)=O(N)\) in total. Each leaf outputs a valid signed mismatch.

Thus an exponential number of low rows can be served by a linear-size shared DAG whenever they share a common block partition. This does not construct a DAG for all of \(Y\times Z\): different low circuits need not share a partition, and Alice would have to communicate or otherwise expose which partition applies. It does falsify any lower-bound plan based only on the cardinality of a code family or on per-anchor isolation.

**Candidate structural target.** Study the family of circuit-induced partitions \(w^{-1}(0),w^{-1}(1)\) and ask how many incompatible partitions must be represented by shared rectangles. For each fixed low \(w\) and high \(z\), \(z\) must vary on at least one fiber of \(w\); otherwise \(z\in\{0,1,w,\neg w\}\) and is low. The hard, unproved step is to convert this pairwise fact into a lower bound on the shared state count when the partition itself varies with \(w\). It is not yet a transfer from fusion closure to a stronger search relation.

## 12. C-81 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Row-signature diameter lemma for every rect-DAG

There is a general, rigorous non-shareability condition for a rect-DAG solving \(\mathrm{Mis}_{Y,Z}\). For each vertex \(v\), write its rectangle as \(A_v\\times B_v\). Associate to each low row \(w\) its row signature

\\[
\\sigma_\\Pi(w)=(\\mathbf 1[w\\in A_v])_{v\\in V(\\Pi)}.
\\]

If two low tables \(w,w'\) have the same signature and \(D=\\{k:w_k\\ne w'_k\\}\), then

\\[
2^{|D|}\\le M_2:=|\\mathrm{SIZE}(s_2)|.
\\]

**Proof.** If \(2^{|D|}>M_2\), there is a high table \(z\) agreeing with \(w=w'\) outside D: among the \(2^{|D|}\) completions of their common restriction, at most \(M_2\) are low. For this fixed z, the two pairs \((w,z)\) and \((w',z)\) have the same membership at every rect-DAG vertex, since their row signatures agree. Hence they have the same reachable output leaves. But their valid signed-mismatch output sets are disjoint: outside D, z agrees with both; inside D, w and w' have opposite bits, so no single signed output can be valid for both. This contradicts correctness. Therefore every row-signature class has Hamming diameter at most \(\log_2M_2\). \\(\\square\\)

Equivalently, the signatures properly color the graph on Y joining pairs at Hamming distance \(>\log_2M_2\). This is a genuine structural condition on state reuse. A code C in Y whose pairwise distances exceed \(\log_2M_2\) has |C| distinct signatures, so \(2^{S_{rect}}\ge |C|\) and \(S_{rect}\ge\log_2|C|\). The fixed-block low code from C-80 has size \(2^{\\Theta(s_1)}\), with block distance \(N/\\Theta(s_1)\\gg\\log M_2\) for sufficiently small \u03b2<1/2, hence it yields only \(S_{rect}\\ge\\Theta(s_1)\). That is below the existing \(N-o(N)\) fusion floor and far below the \(N^{3+3\\epsilon}\) rect-DAG target.

**Learning.** We now have a precise necessary condition for sharing: one DAG state-signature class cannot contain two low rows farther apart than the logarithm of the number of size-\(s_2\) tables. The bottleneck is not proving pairwise distinguishability; it is proving that the number of required signatures or transitions grows superlinearly. The Hamming packing bound alone cannot do that at these OPS parameters.

## 13. C-82 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Signature certificates, dual obstruction, and quantitative ceiling

The C-81 row-signature lemma is valid because the completion count is compared with all tables of complexity at most \(s_2\), not merely with the low class. If two low rows \(w,w'\) share a signature and differ on \(D\), their common restriction has \(2^{|D|}\) completions. When this exceeds \(M_2=|\mathrm{SIZE}(s_2)|\), at least one completion is in \(Z=\mathrm{SIZE}(s_2)^c\), contradicting the shared reachable output leaf. Hence

\[
|D|\le \log_2 M_2\le C_0s_2\log_2(n+s_2+2)
=N^{\beta+o(1)}.
\]

For \(\beta<1/2\), the C-80 block code has minimum distance \(N/\Theta(s_1)\), which is larger than this radius. Its \(2^{\Theta(s_1)}\) codewords therefore have distinct row signatures, giving \(S_{\rm rect}\ge\log_2|C|=\Theta(s_1)\). The logarithm is essential: \(S\) vertices provide at most \(2^S\) row signatures.

There is a precise dual statement for columns. Give a high column \(z\) the signature \(\tau(z)=(\mathbf1[z\in B_v])_{v\in V}\). If \(z,z'\in Z\) have equal signatures, put \(A=\{k:z_k=z'_k\}\). Their common reachable leaves are identical for every fixed low row \(w\). If any \(w\in Y\) agrees with \(z\) on all of \(A\), then no signed mismatch output is valid for both \((w,z)\) and \((w,z')\): on \(A\) there is no mismatch, and on the complement \(z,z'\) have opposite bits. Therefore the partial assignment \(z|_A\) must have **no low completion**.

An elementary interpolation bound makes this dual condition concrete but weak. Any prescribed pattern on \(r\) distinct truth-table coordinates has a completion computed by a minterm DNF with \(O(rn)\) gates. Consequently every pattern on at most \(s_1/(C n)\) coordinates, for a suitable absolute circuit-basis constant \(C\), has a low completion. Equal-signature high columns must thus agree on more than \(s_1/(C n)\) coordinates. This is only a lower bound on their agreement set; it does not force many signatures.

**Method ceiling.** A proof that counts only distinct row signatures can never yield the required superlinear rect-DAG lower bound. There are at most \(|Y|\) such signatures, so it can give at most \(S_{\rm rect}\ge\log_2|Y|\). Circuit counting gives \(\log_2|Y|=O(s_1\log(n+s_1))=N^{\beta+o(1)}=o(N)\) for fixed \(\beta<1\). The dual column condition avoids this immediate ceiling, but the no-low-completion condition is easy to satisfy on large, irregular agreement sets and has not produced a packing bound.

**Status.** C-81 is a proved Tier-3 structural non-shareability condition. C-82 gives its exact dual and identifies why the row-signature route cannot reach Tier 1 or even the linear barrier. No stronger DAG lower bound follows.

## 14. C-83 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â The q rule states form a terminating cyclic game, not an acyclic DAG

The fusion list itself gives a compact cyclic witness machine. It has one state for each pair \(i\). At state \(i\), Bob selects a side \(S\in\{E_i,H_i\}\) false in the closure of \(z\); Alice selects either a matching literal contained in \(S\), which outputs its signed mismatch, or an active predecessor \(j\) with \(T_j\subseteq S\), which transitions to state \(j\). Since \(S\) is false for \(z\), such a predecessor is inactive for \(z\). Since it supports activation at \(w\), its first-activation round is strictly earlier than that of \(i\). The input-specific rank therefore decreases on every rule transition, and every valid play terminates in at most \(q\) transitions.

The static state graph can nevertheless contain cycles. Its semantic transition list has at most \(2q^2+2qN\) support arcs (rule supports and signed-literal supports), while the vertex count is \(q\) if output labels live on arcs. This is a compact **cyclic, input-ranked loop game**. It is not Sokolov's or GGKS's standard rect-DAG, whose graph is globally acyclic and whose branching is binary.

This compact model is already the project's exact \(D^\circ_\cap\) formulation: the q states are the q cyclic intersection gates, with the same seed clauses and endpoint-containment incidence. Calling the q states DAG nodes does not remove the cycles or make the local support routing free in a binary rect-DAG. The safe acyclic conversion remains \(O(q^2)\) AND gates and \(O(q^2(q+N))=O(q^3)\) binary rect-DAG vertices. An arbitrary cyclic rectangle game need not reverse to a fusion cover unless its transition predicates are induced by actual endpoints \(E_i,H_i\) and their intersections \(T_i\).

**Quantitative consequence.** No \(O(q\operatorname{polylog}N)\) conversion to a standard acyclic rect-DAG has been proved. The q-state loop formulation is exact but is a relabeling of cyclic intersection complexity, not a near-lossless reduction to an established acyclic DAG measure. A standard-DAG lower bound would still need to exceed \(N^{3+3\varepsilon}\) to force \(q>N^{1+\varepsilon}\) through the current generic conversion; the direct cyclic target remains \(D^\circ_\cap=\rho>N^{1+\varepsilon}\).

## 15. C-84 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â A row-signature class has one common high-free cylinder

C-81 can be strengthened from a pairwise diameter statement to a certificate for an entire signature class. Let R be all low rows with one fixed row signature, and let

\[
K_R=\{k:\text{ every }w\in R\text{ has the same bit }p_R(k)\}.
\]

Fix any z in Z. For every w in R, the feasible vertices of the rect-DAG on (w,z) are identical: membership in each row side A_v is fixed by the signature, and the column z is fixed. Therefore the set of feasible output leaves is identical for all w in R. Since the relation is total, it contains a leaf; that leaf must be valid for every w in R. Its output coordinate k consequently belongs to K_R, and z_k differs from p_R(k). This holds for every z in Z, so the cylinder

\[
C_R=\{u\in\{0,1\}^N:u|_{K_R}=p_R|_{K_R}\}
\]

contains no high table. Counting its \(2^{N-|K_R|}\) completions gives

\[
|K_R|\ge N-\log_2 M_2=N-N^{\beta+o(1)}.
\]

Thus every row-signature class lies in a single high-free coordinate cylinder fixing all but \(N^{\beta+o(1)}\) bits. If \(C_{\rm cyl}(Y,Z)\) is the minimum number of high-free coordinate cylinders covering Y, then every S-vertex rect-DAG satisfies \(C_{\rm cyl}(Y,Z)\le2^S\), hence \(S\ge\log_2 C_{\rm cyl}(Y,Z)\).

**Limit.** This strengthens the geometry of a reusable state class but does not beat the earlier code bound: singleton cylinders give \(C_{\rm cyl}\le|Y|\), and \(\log|Y|=N^{\beta+o(1)}=o(N)\). The cylinder may also contain medium tables, so it is not by itself an exact fusion-cover term over the full complement of Y. A stronger lower bound on the number of such certificates, or an argument involving transitions between classes, is still required.

## 16. C-85 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Every pair of row/column signature classes has a common output coordinate

For a rect-DAG \(\Pi\), partition Y into row-signature classes \(R\), and Z into column-signature classes C. Let \(K_R\) be the coordinates on which all rows of R are constant, with common pattern \(p_R\); define \(K_C,q_C\) symmetrically.

For every nonempty pair \(R,C\), there is a coordinate

\[
k\in K_R\cap K_C\quad\text{such that}\quad p_R(k)\ne q_C(k).
\]

Indeed, for every pair \((w,z)\in R\times C\), membership in every node rectangle is identical: the row signature fixes membership in \(A_v\), and the column signature fixes membership in \(B_v\). Thus all these pairs have the same feasible vertices and the same reachable output leaves. Choose one reachable leaf. Its signed mismatch label must be valid for every pair in \(R\times C\), forcing its coordinate to be constant with opposite values on the two entire classes.

This is stronger than the separate row- and column-certificate statements: every quotient block \(R\times C\) is contained in one common output rectangle, and the two classes' fixed-coordinate cores must intersect in an oppositely labeled coordinate. A quantitative lower bound now asks how many such class pairs can be arranged with at most \(2^S\) classes per side and at most S vertices, given the circuit-induced structure of Y and Z.

**Status and limit.** The class-pair lemma is proved, but no lower bound on the number of classes or routing vertices has been derived. Counting just row classes is capped by \(\log|Y|=o(N)\); counting column classes is capped by \(\log|Z|\le N\); and counting class pairs is capped by \(\log(|Y||Z|)\le N+o(N)\). Counting leaves is capped by the \(2N\) obvious signed-coordinate rectangles. All these counts fall below the \(N^{3+3\varepsilon}\) scale needed for the current fusion transfer. The promising missing term is the cost of organizing the cross-class separations into a shared acyclic DAG.

## 17. C-86 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Why the linear scan cannot merge equal-prefix histories

The tempting universal protocol scans coordinates and, after finding equality at coordinate i, merges all histories into one state for coordinate i+1. In Sokolov's Boolean communication game, a vertex is valid according to a product predicate \(A(v,w)=1\) and \(B(v,z)=0\); the root is valid on all \(Y\times Z\), and every valid non-leaf must have a valid child. This is stronger than saying that a path reached from the root happens to have a good continuation.

If the proposed state for coordinate i+1 is labelled by the full rectangle \(Y\times Z\), it is valid also for pairs whose only mismatch lies among the already scanned coordinates. Those pairs must still have a valid continuation from this vertex. A suffix-only scan fails on them. If instead the state is restricted to pairs equal on the scanned prefix, that set is a union of prefix-pattern rectangles, not one rectangle; taking its rectangular hull adds cross-pairs. Keeping the prefix pattern as part of the state restores correctness and returns to the pattern-profile construction.

Thus the path-history intuition does not yield an \(O(N)\) Sokolov rect-DAG for the mismatch relation. This kills that specific universal scan-and-merge construction, not every possible small DAG. The exact validity conditions are in Sokolov's Definition 2.1 and Remark 2.1.

## 18. C-87 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Linear fingerprints need almost N bits

Let \(L:\{0,1\}^N\to\{0,1\}^r\) be a linear sketch of rank r on the truth-table bits. Every fiber has size \(2^{N-r}\). If \(r<N-\log_2 M_2\), each fiber contains more than \(M_2=|\mathrm{SIZE}(s_2)|\) tables and therefore contains a high table. In particular, for every low w there is a high z with \(L(w)=L(z)\).

Thus no fixed-coordinate sample, parity sketch, or other linear fingerprint of fewer than

\[
N-\log_2 M_2=N-N^{\beta+o(1)}
\]

bits can separate every low table from every high table. This is an exact counting obstruction to sublinear nonadaptive linear sketches. It does not rule out nonlinear summaries: the one-bit separator \(1_{\mathrm{SIZE}(s_1)}\) is itself the hard function of interest.

## 19. C-88 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Description-space routing retains the interval pattern

Let D be the set of descriptions of circuits of size at most \(s_1\), with length \(\ell=O(s_1\log(n+s_1))=N^{\beta+o(1)}\), and let \(G(d)\) be the truth table computed by d. The promise relation \(\mathrm{MisDesc}(d,z)\) is total on \(D\times Z\); sending d and then scanning z gives communication \(O(\ell+\log N)\), but its protocol tree can have \(2^{O(\ell)}\) histories.

For a dyadic interval I and restriction u, the rectangle

\[
\{d:G(d)|_I=u\}\times\{z:z|_I\ne u\}
\]

is valid. Recursing on interval halves gives the same restriction-profile DAG, with profile count

\[
\pi_I(D)=|\{G(d)|_I:d\in D\}|\le\min(2^{|I|},2^\ell).
\]

The phrase ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œthere is a mismatch in IÃƒÂ¢Ã¢â€šÂ¬Ã‚Â still mixes d and z and is not generally a rectangle. Circuit syntax lets Alice evaluate \(G(d)|_I\), but a rectangle state that compares it with z must retain enough information about that restriction. The current construction therefore has the same profile-sum upper bound as the truth-table version; it is not near-linear, and this does not prove that every DAG must retain these exact profiles. Description collisions and canonicalization do not remove the mixed-predicate obstacle.

**Status.** The direct description protocol is cheap in communication, while the best shared construction still pays for restriction profiles. No small universal DAG or general lower bound against one has been proved.


## 20. C-90 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Promise-domain reverse conversion and ambient-universe audit

There are two different cover parameters in play, and they must not be identified:

- \(\rho_{\rm prom}\): \(\Gamma_{\rm prom}=Y\sqcup Z\), filter universe \(U_{\rm prom}=Z\), and literal generators restricted to \(\Gamma_{\rm prom}\). This is the active Gap-MCSP promise cover.
- \(\rho_{\rm full}\): \(\Gamma_{\rm full}=\{0,1\}^N\), filter universe \(U_{\rm full}=M\sqcup Z=\Gamma_{\rm full}\setminus Y\). This is an exact low-set cover.

**Reverse map for the active target.** If an \(L\)-vertex rect-DAG solves \(Y\times Z\), C-89 gives a Boolean separator circuit of size \(O(L)\). Its De Morgan set construction, restricted to \(\Gamma_{\rm prom}\), gives
\[
\rho_{\rm prom}\le D_\cap\le D=O(L).
\]
So the requested DAG-to-fusion-cover transformation succeeds for the actual project promise, with constant-factor loss. In particular, a universal DAG of size \(N^{1+o(1)}\) would imply \(\rho_{\rm prom}\le N^{1+o(1)}\), falsifying the fixed-superlinear \(\rho_{\rm prom}\) target.

**Restriction monotonicity (new project lemma).** One also has \(\rho_{\rm prom}\le\rho_{\rm full}\). Given a full-domain cover \(Q=((E_i,H_i))\) with endpoints in \(U_{\rm full}\), restrict endpoints to Z. If the restricted list failed to cover a low anchor, let \(\mathcal F\) be a proper semi-filter over Z above that anchor and preserving every restricted pair. Lift it by
\[
\widetilde{\mathcal F}=\{A\subseteq U_{\rm full}:A\cap Z\in\mathcal F\}.
\]
This is a proper upward-closed family, contains every full-domain matching literal slice because its Z-restriction belongs to \(\mathcal F\), and preserves every original pair since \((E_i\cap Z)\cap(H_i\cap Z)=(E_i\cap H_i)\cap Z\). That contradicts that Q is a full-domain cover. Hence every full cover restricts to a promise cover without increasing its pair count.

**What medium-band escape does and does not say.** C-79 rules out the converse *by direct endpoint reuse*: endpoints contained in Z can all be avoided by a medium-generated filter over \(M\sqcup Z\). It does not rule out adding medium-band pairs in a more elaborate conversion, and it does not obstruct the rect-DAG-to-\(\rho_{\rm prom}\) map above.

**Corrected reading of C-77/C-78.** A promise-domain closure list computes a separator extension that is 1 on Y and 0 on Z; its values on M are unconstrained. The principal-filter argument giving exact \(1_Y\) on all truth tables applies only to \(\rho_{\rm full}\). The cyclic characterization \(\rho=D^\circ_\cap\) holds for each chosen ground set, but the two ground sets yield different parameters.

**Quantitative map for the active promise target.** Combining C-78/C-89 with the reverse map gives
\[
\rho_{\rm prom}\le\mathrm{SepCirc}(Y,Z)\asymp\mathrm{rectdag}(\mathrm{Mis}_{Y,Z})\le O(\rho_{\rm prom}^{3}).
\]
Therefore a lower bound \(\rho_{\rm prom}>N^{1+\epsilon}\) itself gives the near-linear separator lower bound needed by OPS. To obtain the \(\rho\) lower bound from a generic rect-DAG lower bound, the cubic side still requires \(\mathrm{rectdag}>N^{3+3\epsilon+\delta}\). No superlinear \(\rho_{\rm prom}\) or rect-DAG lower bound has been proved.
## 21. C-91 - SCC-sensitive acyclicization

The generic O(q^3) expansion treats every rule state as one strongly connected component. Before measuring genuine recursion, remove each rule self-support: because T_i=E_i intersect H_i, the original sets P_i^0={j:T_j subset E_i} and R_i^0={j:T_j subset H_i} always contain i. The original activation update is

x_i(t+1) = (a_i OR OR_{j in P_i^0} x_j(t)) AND (b_i OR OR_{j in R_i^0} x_j(t)).

**Self-loop deletion lemma.** Replace P_i^0,R_i^0 by P_i=P_i^0 minus {i}, R_i=R_i^0 minus {i}. This preserves the least fixed point. For a fixed truth-table input, when x_i(t)=0 the original and reduced updates agree. If the original bit first becomes 1 at round t+1, both non-self side-support predicates were already true at t, so the reduced update also sets it to 1. The reduced iteration is monotone, hence that bit stays 1. Induction over rounds proves the two state vectors coincide at every round.

Use these loop-deleted P_i,R_i below. Form the loop-free directed graph with edge j -> i whenever j is in P_i or R_i, and let its strongly connected components have sizes r_1,...,r_m, with sum r_k=q. An acyclic graph now means there are no genuine dependencies between states that return to their starting state.
**Proposition.** If each seed clause is an OR of at most 2N signed input literals, the least-fixed-point output (OR of the empty-consequence states) has a fan-in-two Boolean circuit of size O(qN+q^2+sum_C(r_C e_C+r_C^2)), where r_C is the size of component C and e_C=sum_{i in C}(|P_i intersect C|+|R_i intersect C|) counts internal side-support incidences. The recursive support computation uses AND/OR gates and is monotone in the seed-clause values; as a function of raw truth-table bits, the seed clauses may use either polarity. Since e_C<=2r_C^2, this implies O(qN+q^2+sum_C r_C^3). For d=max_C r_C, it is O(qN+q^2+q d^2), and using q>=N-o(N), O(q^2+q d^2). It is O(q^2) for an acyclic graph, for sparse SCCs with e_C=O(r_C), or whenever d=O(sqrt(q)).

**Proof.** Topologically order the SCC condensation graph. For each state-side, build its signed-literal seed clause and OR the already-computed outputs of all external predecessor states into a fixed external-support signal. Across all sides, seed clauses cost O(qN) gates and external incidences cost O(q^2). Any NOT gates for raw input polarities cost at most O(N), absorbed in the bound since q>=N-o(N). Now consider one component C of size r with e internal side-support incidences. Its external signals are fixed functions of the original input, so compute the component least fixed point by iterating only its r internal state bits. Monotonicity from zero guarantees stabilization within r strict rounds. In each round, the internal support ORs use O(e+r) fan-in-two gates total, and the state updates use O(r) AND gates. Across r rounds this costs O(r e+r^2). Summing over components and adding the final output OR proves the bound. The circuit computes the same least fixed point, so on the active promise it accepts Y and rejects Z. QED.


**Research consequence.** The cubic loss is confined to large mutually recursive components with dense support incidence. The exact next bottleneck is the weighted internal incidence sum above, not SCC size alone. A successful list may still have one giant dense SCC, and no project argument currently limits this quantity or proves that its internal supports are hard to share. The refined question is whether endpoint-containment geometry forces many non-shareable residual supports, or whether it admits a compact separator.

**Status.** SCC-sensitive compiler theorem proved; no direct superlinear q lower bound or P-versus-NP proof follows yet.

## 22. C-92 - Remove transitive two-sided carrier supports

Apply C-91 self-loop deletion first. Let T be the set of distinct carrier sets T_i, ordered by inclusion. A strict relation s<t is a cover if there is no u in T with s<u<t. For each rule i and each state j with T_j a strict non-cover subset of T_i, delete j from both support sets P_i and R_i. Do not delete equal-carrier supports, cover supports, or one-sided supports.

**Proposition.** This pruning preserves the least fixed point of the activation recurrence, for every assignment to its seed clauses.

**Proof.** Let F be the loop-deleted original recurrence and F' the pruned recurrence. Coordinatewise F'<=F, so the least fixed point of F' is at most the least fixed point of F. Take any fixed point y of F'. For every cover s<t and every rule states j,k with T_j=s and T_k=t, the two-sided support j is retained in both support sets of k. Therefore y_j=1 implies y_k=1. Chaining cover relations shows that y_j=1 implies y_i=1 whenever T_j is a strict subset of T_i. Every deleted support term in rule i has this form. If y_i=0, all deleted terms into i are therefore 0, so F_i(y)=F'_i(y)=0. If y_i=1, then F'_i(y)=1 and hence F_i(y)=1. Thus every fixed point of F' is also a fixed point of F. In particular, the least fixed point of F' is a fixed point of F, so the least fixed point of F is at most it. The two least fixed points are equal. QED.

**Compiler consequence.** Recompute the loop-free support graph after pruning and apply C-91 using its reduced side-incidence counts. For a chain of q distinct carriers with one rule per carrier, the transitive two-sided support arcs shrink from quadratic many to the 2(q-1) incidences of adjacent carrier covers. Thus mere nesting of carrier sets does not force a dense SCC or a cubic unrolling cost.

**Limit.** Equal-carrier groups, cover edges between large duplicate groups, and dense one-sided endpoint supports remain. This is an equivalent recurrence simplification, not a lower bound or a proof that every successful cover has a sparse reduced graph.

**Audit.** The pruning proof survives the fixed-point check: for every cover pair of distinct carrier values (s<t), every state with carrier (s) is a support on both sides of every rule with carrier (t), because (t=T_i\subseteq E_i\cap H_i). Such incidences are retained. A cover chain therefore forces (y_j=1\Rightarrow y_i=1) in every fixed point of the pruned map, which is exactly what is needed to show every pruned fixed point is also a fixed point of the original map. The least fixed points coincide by monotonicity and pointwise (F'\le F). This is an equivalence of recurrences, not an assertion that the intermediate iteration sequences are identical.

## 23. C-93 - Quotient equal carriers while retaining their alternatives

Apply C-91 self-support deletion and, optionally, C-92 transitive pruning. Let \(\mathcal T=\{T_i\}\) be the distinct carrier values, \(I_t=\{i:T_i=t\}\), and \(p=|\mathcal T|\). The support test for a fixed recipient rule \(i\) depends on a source rule \(j\) only through \(T_j\). Thus an entire equal-carrier group either supports a given side of \(i\) or does not. For \(i\in I_t\), let \(P_i^*,R_i^*\subseteq\mathcal T\setminus\{t\}\) be the remaining source-carrier values on its two sides, and define

\[
c_i(x)=\left(a_i\vee\bigvee_{u\in P_i^*}x_u\right)\wedge
       \left(b_i\vee\bigvee_{u\in R_i^*}x_u\right),\qquad
H_t(x)=\begin{cases}
c_i(x),&I_t=\{i\},\\
\displaystyle\bigvee_{i\in I_t}c_i(x),&|I_t|\ge2.
\end{cases}
\]

Here \(a_i,b_i\) are the original literal-seed clauses. Equal-carrier support terms are omitted from \(c_i\); in the unquotiented recurrence they are present on both sides whenever \(|I_t|\ge2\), and the self term has already been deleted when \(|I_t|=1\).

**Proposition.** The least fixed point of the rule-state recurrence is exactly the lift of the least fixed point of \(H\): every rule state \(i\in I_t\) has final value \(x_i=x_t\), where \(x=\operatorname{lfp}(H)\).

**Proof.** Let \(F\) be the loop-free rule-state map and \(x^*=\operatorname{lfp}(F)\). Its iteration from zero is increasing. In any equal-carrier group of size at least two, if one state is 1 at a fixed point, then every other state has that state as support on both sides and is also 1. So the final bits in each such group agree; call their common value \(h_t\). For a singleton group, set \(h_t=x_i^*\).

If \(h_t=0\), all same-group supports vanish and the fixed-point equations give \(c_i(h)=0\) for every \(i\in I_t\), hence \(H_t(h)=0\). If \(h_t=1\) for a multi-rule group, consider the first iteration at which any state in that group becomes 1. Before that round every state in the group was 0, so the triggering rule's two sides were satisfied by its seeds and other-carrier supports. Let \(h^s_u\) be the OR of the rule-state bits in carrier group \(u\) at that earlier round. Since support membership depends only on the source carrier, \(c_i(h^s)=1\). The rule-state iteration is increasing, so \(h^s\le h\) and monotonicity gives \(c_i(h)=1\), hence \(H_t(h)=1\). For a singleton, its fixed-point equation is directly \(h_t=c_i(h)\). Thus \(h\) is a fixed point of \(H\).

Conversely, let \(y=\operatorname{lfp}(H)\) and lift it by setting every rule in \(I_t\) to \(y_t\). For a singleton, its rule equation is \(c_i(y)=H_t(y)=y_t\). For a group of size at least two, if \(y_t=0\), then \(H_t(y)=0\) forces every \(c_i(y)=0\), so every original rule output is 0. If \(y_t=1\), each rule has another active state of the same carrier on both support sides, so every rule output is 1. The lift is therefore a fixed point of \(F\). Leastness gives \(x^*\le y\) after lifting, while leastness of \(y\) and the fixed-point property of \(h\) give \(y\le h\). Hence \(h=y\) and the fixed points agree as claimed. QED.

**Carrier-SCC compiler bound.** Form the directed graph on the \(p\) carrier values, with an arc \(u\to t\) if some candidate \(i\in I_t\) uses \(x_u\) on either side of \(c_i\). Let its SCCs be \(C\), with \(p_C=|C|\), \(q_C=\sum_{t\in C}|I_t|\), and
\[
e_C=\sum_{t\in C}\sum_{i\in I_t}\bigl(|P_i^*\cap C|+|R_i^*\cap C|\bigr).
\]
Let \(e_{\rm out}\) count the analogous candidate-side incidences whose source carrier lies outside the destination SCC. Topologically solve the SCCs. For each candidate side, build its seed and external-support OR once; these cost \(O(qN+e_{\rm out})\). In SCC \(C\), iterate its \(p_C\) carrier bits from zero for at most \(p_C\) strict rounds. One round evaluates at most \(q_C\) candidate conjunctions, their internal support ORs, and their group ORs, for \(O(e_C+q_C)\) gates. The separator therefore has size
\[
O\!\left(qN+e_{\rm out}+\sum_C p_C(e_C+q_C)\right).
\]
Since the total number of candidate-side carrier incidences is at most \(2q(p-1)\), a coarse consequence is \(O(qN+qp^2)\). Use this together with, rather than in place of, C-91's rule-SCC bound; either can be better. When \(p\ll q\), the recursive-round factor depends on the number of distinct carriers, while the \(q\) distinct rule alternatives and their seed clauses are still charged.

**Why this does not merge rules into one pair.** The quotient output is an OR of candidate conjunctions, \(\bigvee_i(A_i\wedge B_i)\), not generally one conjunction \((\bigvee_iA_i)\wedge(\bigvee_iB_i)\). The latter introduces cross-pair activations; for example \((A_1,B_1)=(1,0)\), \((A_2,B_2)=(0,1)\) gives 0 versus 1. Equal carriers remove redundant recursive state bits, but not the alternative-specific side tests.

**Status and next bottleneck.** The quotient and its compiler bound are proved for every seed assignment. They improve the forward q-to-separator conversion on duplicate-heavy carrier lists, but give no lower bound on \(q\). The unresolved structure is now explicit: many candidate conjunctions may feed a small carrier SCC graph, or a large SCC may have many distinct carriers and dense one-sided supports. No theorem yet forces either pattern to have large separator complexity.

## 24. C-94 - Feedback factors through one-sided escape supports

Work after C-91 self-loop deletion, C-92 pruning, and C-93 equal-carrier quotient. Order the distinct carriers by inclusion, write \(u\lessdot t\) for a cover, and let \(I_t\) be the rule alternatives at carrier \(t\). For each \(i\in I_t\), every source carrier \(u\subsetneq t\) is supported on both sides. C-92 leaves exactly the lower covers \(u\lessdot t\); C-93 removes equal-carrier support. Conversely, if \(u\) supports both sides of rule \(i\), then \(u\subseteq E_i\cap H_i=t\). Therefore every remaining support whose carrier is not below \(t\) is one-sided.

Define the shared cover signal and the candidate-specific escape lists by
\[
K_t(x)=\bigvee_{u\lessdot t}x_u,\qquad
L_i=\{u\not\subseteq t:u\subseteq E_i\},\qquad
R_i=\{u\not\subseteq t:u\subseteq H_i\}.
\]
The two escape lists are disjoint. With
\[
d_i(x)=\left(a_i\vee\bigvee_{u\in L_i}x_u\right)
       \wedge\left(b_i\vee\bigvee_{u\in R_i}x_u\right),
\qquad D_t(x)=\bigvee_{i\in I_t}d_i(x),
\]
the quotient recurrence has the exact normal form
\[
H_t(x)=K_t(x)\vee D_t(x).
\]
Indeed, each candidate conjunction before factoring is \((a_i\vee K_t\vee L_i(x))\wedge(b_i\vee K_t\vee R_i(x))\), and \((K\vee A)\wedge(K\vee B)=K\vee(A\wedge B)\).

**Cycle localization.** The cover edges \(u\to t\) form the Hasse DAG of the carrier poset. Every directed cycle in the full carrier-support graph therefore contains at least one escape edge \(u\to t\) with \(u\not\subseteq t\). Thus recursive feedback is entirely due to one-sided endpoint supports; two-sided carrier inclusion only propagates activation upward.

**Escape-event compiler.** Let \(\mathsf{Up}(D)\) be the upward closure of the carrier set selected by D in the Hasse poset, and define \(G(x)=\mathsf{Up}(D(x))\). The fixed points of G are exactly those of H. For any H-fixed point, recursively expanding \(x_t=D_t(x)\vee\bigvee_{u\lessdot t}x_u\) along the finite poset gives \(x_t=\bigvee_{s\subseteq t}D_s(x)\), which is \(x=\mathsf{Up}(D(x))\). Conversely, if \(x=\mathsf{Up}(D(x))\), then an active t either has \(D_t(x)=1\) or has an active lower cover; an inactive t has neither. Hence H(x)=x, so the least fixed points agree.

Now iterate \(x^{(0)}=0\), \(x^{(r+1)}=G(x^{(r)})\). Let S be the set of distinct carrier values appearing in any \(L_i\) or \(R_i\), and \(s=|S|\). The sequence is increasing. If \(x^{(r+1)}>x^{(r)}\) for \(r\ge1\), then \(D(x^{(r)})\ne D(x^{(r-1)})\); some candidate conjunction has newly turned on, which requires at least one escape-source carrier in S to have changed from 0 to 1 between those rounds. Each such carrier changes only once. There are at most s such later strict steps, plus the initial step, so G stabilizes by round s+1.

Let \(\xi=\sum_i(|L_i|+|R_i|)\) count candidate-side escape incidences and \(\kappa=|\{(u,t):u\lessdot t\}|\) count Hasse edges. One macro-round evaluates all candidate escape ORs, q conjunction alternatives and group ORs, then computes \(\mathsf{Up}\) once by a topological pass over the Hasse DAG. Precompute seed clauses once. The resulting separator circuit has size
\[
O\bigl(qN+(s+1)(\xi+\kappa+q)\bigr)
\;\le\;
O\bigl(qN+(s+1)(q(s+1)+\kappa)\bigr),
\]
since \(\xi\le2qs\). In the escape-free case \(s=0\), this is \(O(qN+q+\kappa)=O(qN+q+p^2)\). In general it is at most \(O(qN+qp^2)\) because \(s\le p\), \(\kappa\le p(p-1)/2\), and \(p\le q\). Compare this event bound with C-91 and C-93's SCC bounds; none dominates in every support pattern.

**Limit.** This localizes all cyclicity but does not bound s, \(\xi\), or separator complexity from below. A small number of escape-source carriers gives a substantially shorter compilation, while many candidate-specific escape supports can still produce the cubic worst case. The next lower-bound target is the non-shareability of the escape alternatives after their common upward-closure signal has been factored.

**OPS loss audit.** In the unrestricted worst case \(p,s\le q\) and \(q\ge N-o(N)\), this remains \(O(q^3)\); a generic rect-DAG lower bound still needs to exceed \(N^{3+3\epsilon+\delta}\) to force \(q>N^{1+\epsilon}\). In the escape-free regime the bound is \(O(qN+p^2+q)\). If also \(p\le N^\gamma\), then any such cover with \(q\le N^{1+\epsilon}\) yields separator size \(O(N^{\max(2+\epsilon,2\gamma)})\). This is a conditional improvement only; the project has no theorem bounding p or s for all successful covers.

**Literature boundary.** The cut-set viewpoint is related to standard feedback-vertex-set methods for Boolean networks. For example, Aracena, Goles, Moreira, and Salinas give an algorithm for fixed-point enumeration based on a positive feedback vertex set, with exponential dependence on the cut-set size; their model and objective are not the Gap-MCSP separator compiler here ([paper](https://arxiv.org/abs/2004.01259)). C-94 should not be presented as inventing feedback-set unrolling. Its project-specific content is that endpoint intersection geometry yields an inclusion-poset Hasse DAG, all remaining cyclic dependencies are one-sided, and the least fixed point can be compiled through the resulting escape-source projection.

## 25. C-95 - A contradiction rule cannot fire from its two seed clauses alone

Assume the project parameter regime where the number \(M_2\) of truth tables of circuit complexity at most \(s_2\) satisfies \(M_2<2^{N-2}\). For an empty-carrier rule \(i\), its two direct seed predicates \(a_i(v)\) and \(b_i(v)\) are each disjunctions of signed truth-table literals.

**Proposition.** In any successful cover, \(a_i(v)\wedge b_i(v)\) is identically false for every rule with \(T_i=\varnothing\).

**Proof.** If some table v satisfied both seed clauses, choose one true literal from each. Fixing the at most two table bits appearing in those literals leaves a subcube of at least \(2^{N-2}\) tables on which both clauses remain true. Since only \(M_2<2^{N-2}\) tables are non-high, this subcube contains a high table z. At z, rule i activates directly from both seed sides, deriving its empty carrier. But the principal semi-filter of z preserves every pair, so a successful cover cannot derive the empty carrier at z. Contradiction. QED.

**Normal form of the seed conflict.** After duplicate literals are removed, an identically false seed clause is the empty clause. If both clauses are nonempty and their conjunction is unsatisfiable, they must be opposite unit literals on one coordinate. Otherwise choose a literal from the first clause; unless every literal of the second is its complement, the two chosen literals can be made true simultaneously. If the second is that opposite unit, any additional non-complement literal in the first also makes both clauses satisfiable. Hence only the complementary-unit case remains.

**Escape consequence.** In C-94 normal form, \(K_{\varnothing}=0\). Since every empty-rule seed conjunction is false, each low anchor w that activates an empty rule must use at least one of that rule's one-sided escape supports. Let \(S_0\) be the set of source carriers appearing in escape lists of empty-carrier rules, and \(X_u=\{w:x_u(w)=1\}\). Then
\[
Y\subseteq\bigcup_{u\in S_0}X_u.
\]
So every low anchor reaches the contradiction layer through the same explicit escape interface.

In the complementary-unit case, if \(a_i=\ell\) and \(b_i=\neg\ell\), every low activation with \(\ell(w)=1\) must use an R_i escape, while every one with \(\ell(w)=0\) must use an L_i escape (and conversely if the unit signs are reversed). If one seed clause is empty, that side always requires escape support. This gives a coordinate-indexed routing constraint at the final rule.

**Limit.** This proves a non-seed path is necessary at the final empty rule, but it gives no lower bound on \(|S_0|\): a single activation set \(X_u\) may contain many low anchors, and endpoint sets are semantic. The next counting argument must constrain how these source activations can simultaneously serve low anchors while remaining blocked on every high table.

## 26. C-96 - Every terminal support cone contains linearly many seed features

For a rule state j in the loop-free recurrence, let \(\operatorname{Anc}(j)\) be the state j together with every rule state that can reach j along a support-dependency path. This set is predecessor-closed, so \(x_j\) depends only on the seed clauses belonging to \(\operatorname{Anc}(j)\).

**Proposition.** Fix any low anchor w and choose an empty-carrier rule i activated at w. For each of its two true support sides, choose either its true seed clause or one active predecessor state. Let C(w) be the union of i and the ancestor cones of the at most two chosen predecessor states. Then at least \(N-\log_2 M_2\) nonconstant seed clauses from rules in C(w) are true at w. Consequently,
\[
|C(w)|\ge\frac{N-\log_2 M_2}{2}=\frac{N-o(N)}2.
\]

**Proof.** Let \(\Phi_w\) be the conjunction of all nonconstant seed clauses true at w whose rules lie in C(w). Every table v satisfying \(\Phi_w\) has seed vector coordinatewise at least that of w on every selected predecessor cone; each such cone is predecessor-closed. Monotonicity therefore preserves each chosen predecessor activation. The chosen direct seed supports at i also remain true, since i itself is included in C(w). Both sides of the same empty-carrier rule i consequently activate at v. A successful cover cannot do this on a high table, so \(\Phi_w\) has at most \(M_2\) satisfying tables. A satisfiable CNF with m clauses on N bits has at least \(2^{N-m}\) satisfying assignments, hence \(m\ge N-\log_2M_2\). At most two seed clauses belong to each rule state in C(w), giving the state-count bound. QED.

**Learning and limit.** This localizes a linear amount of seed/state complexity inside the causal cone of the final contradiction, instead of counting all 2q features as in C-76. It does not improve the global linear pair-count floor: the factor 1/2 is weaker than C-03, and the large cones for different low anchors may overlap almost completely. The next step is to prove that these terminal cones cannot all share the same states while routing the different low/high pairs.

## 27. C-97 - Description-space invariance and the exact DAG bottleneck

This continuation records the strongest conclusion from the requested shared-DAG audit. It sharpens C-75/C-78 without changing the unresolved lower-bound target.

### Exact search relations

Let $D_1$ be the set of valid descriptions of circuits of size at most $s_1$, and let $G:D_1\to\{0,1\}^N$ map a description to its truth table. Then $Y=G(D_1)$, $Z=\{z:\mathrm{CC}(z)>s_2\}$, and $Y\cap Z=\varnothing$.

The **plain mismatch relation** has Alice input $w\in Y$ (or a description $d\in D_1$, with semantic row $G(d)$); Bob has $z\in Z$. A valid output is $(k,b)$ with $w_k=b\ne z_k$. It is total because $w\ne z$. A proposed pair list $Q=((E_i,H_i))_{i=1}^q$ is irrelevant to this relation.

The **Q-witness relation** additionally outputs a path of rule indices, the side selected at each rule, each selected support (a predecessor rule or a signed literal), and the terminal $(k,b)$. Starting at an empty-carrier rule active on $w$ and inactive on $z$, each step chooses a side false at $z$ and a true support at $w$; a rule-support step goes to an active-on-$w$, inactive-on-$z$ predecessor of strictly smaller first-activation rank. The path ends at a literal mismatch after at most $q$ transitions. This relation is total on $Y\times Z$ iff $Q$ covers every low anchor. Plain mismatch remains total even when $Q$ fails. The local checks are separated: Alice checks activations and true supports from $w$; Bob checks inactive states and false sides from $z$; $Q$ is public.

### Proven invariance under circuit descriptions

**Proposition (surjective row relabelling).** For every finite surjection $G:D_1\twoheadrightarrow Y$, the minimum size of a Sokolov Boolean communication game / rect-DAG for mismatch on $D_1\times Z$ equals the minimum size for mismatch on $Y\times Z$. The same equality holds for deterministic communication cost and protocol-tree size in models with unrestricted local computation.

**Proof.** A game on $Y\times Z$ lifts to $D_1\times Z$ by replacing each Alice predicate $A_v(w)$ by $A_v(G(d))$; the graph is unchanged. Conversely, choose any section $\sigma:Y\to D_1$ with $G(\sigma(w))=w$. Given a game on $D_1\times Z$, replace $A_v(d)$ by $A_v(\sigma(w))$. Every pair $(w,z)$ now follows the valid game path for $(\sigma(w),z)$, and every output is valid for $w,z$. The graph is unchanged. The same lift/restriction argument applies to protocol trees and communication protocols because all local computation is free. Colliding descriptions therefore do not change any of these measures.

The same lift/restriction proof applies to the Q-witness relation for a fixed public Q, since every activation, support check, and valid output depends on d only through G(d). This gives a precise answer to the description-space test: syntax can shorten the *message* Alice sends, but it cannot by itself shrink the shared graph. The DAG topology has to solve the same row-separation problem after descriptions are quotiented by their truth tables.

### Model comparison and quantitative chain

| Model | Relation / resource | Proven bound for the Gap-MCSP promise |
|---|---|---|
| Deterministic communication | Bits exchanged on plain mismatch | $O(r+\log N)$, where $r=O(s_1\log(n+s_1))$: Alice sends a circuit description and Bob returns a differing coordinate. The Q-witness protocol costs $O(q\log(q+N))$ bits. |
| Protocol tree | Number of nodes, not bits | The description protocol has at most $2^{O(r)}N$ nodes (or $O(|Y|N)$ using a canonical row index). A tree protocol for the full Q-witness output has at most $2^{O(q\log(q+N))}=(q+N)^{O(q)}$ nodes. In general $c$ communicated bits only gives the upper bound $2^{c+1}-1$ on tree nodes. Tree complexity is the formula/separator analogue, not DAG complexity. |
| Sokolov Boolean game / rect-DAG | Acyclic graph, fan-out at most two; each state is a rectangle and its valid pairs are covered by its children | Exactly the ordinary shared-DAG model for plain mismatch. Its minimum size $S_{\rm rect}$ is within constant factors of $\mathrm{SepCirc}(Y,Z)$, the minimum Boolean circuit size of any $h$ with $h|_Y=1,h|_Z=0$. |
| Communication PLS | Acyclic state graph of size (L), with (t) bits to test membership/select a successor | Boolean game size (L\Rightarrow\) PLS size (L), cost at most 2; PLS size (L), cost (t\Rightarrow\) Boolean-game size at most (L2^{3t}). Fusion's static support graph can cycle, so it is not a standard PLS game. Rank-layering and then applying this theorem is worse than the direct rect-DAG compiler here. |
| Fusion / Cavalar-Oliveira cyclic intersection complexity | Least-fixed-point set equations; count only cyclic intersections; unions are free | Exact identity (q=\rho_{\rm prom}=D^\circ_\cap(Y\mid\mathcal B_{\rm prom})). This is the native cover measure, not an acyclic rectangle-DAG. |
| Acyclic conjunctive complexity | Count AND/intersection gates; ORs free | (\mathrm{SepAnd}(Y,Z)\le D_\cap\le q^2). This is a stronger transfer than charging all ordinary gates, but it does not count OR routing. |
| Ordinary fan-in-two separator circuit / rect-DAG | Count both AND and OR routing, eliminate cycles | General compiler: (S_{\rm rect}=\mathrm{SepCirc}\le O(q^3)), using (q\ge N-o(N)). C-91/C-93/C-94 give the sharper parameterized upper bounds below. |

The reverse map is near-lossless: an (L)-vertex rect-DAG gives a separator circuit of size (O(L)), and its dual-rail set construction gives a promise fusion cover with (q\le O(L)). Therefore
\[
  \rho_{\rm prom}\;\le\;\mathrm{SepCirc}(Y,Z)\;\asymp\;S_{\rm rect}\;\le\;O(\rho_{\rm prom}^{3}).
\]
For the AND-only separator measure, (\rho_{\rm prom}\le\mathrm{SepAnd}\le\rho_{\rm prom}^{2}). Thus a standard rect-DAG lower bound above (N^{3+3\epsilon+\delta}) (for fixed (\delta>0)) would imply (\rho_{\rm prom}>N^{1+\epsilon}); an AND-only lower bound above (N^{2+2\epsilon+\delta}) would also suffice. Neither lower bound is known here. A direct cyclic lower bound (q>N^{1+\epsilon}) avoids both losses.

### Why the q states do not yet give a standard q-node DAG

The q activation predicates (x_i(v)) do give q natural rectangles
\[
R_i=\{w\in Y:x_i(w)=1\}\times\{z\in Z:x_i(z)=0\}.
\]
Along each actual support path the first-activation rank on Alice's input decreases. But the static support graph can cycle, so these q rectangles are a **ranked cyclic search system**, not an acyclic Boolean communication game. A standard game also has binary branching. One fusion side can be supported by any of up to (q+N) earlier states or literal generators, so routing the chosen support cannot be silently treated as a free one-edge transition.

The current proven acyclicization bounds are:
\[
S_{\rm rect}=O(qN+q^2+\sum_C(r_Ce_C+r_C^2))
\]
after deleting self-supports and processing support SCCs, where (r_C,e_C) are the SCC size and internal side-incidences (C-91); and
\[
S_{\rm rect}=O(qN+e_{\rm out}+\sum_C p_C(e_C+q_C))
\]
after quotienting equal carriers (C-93). In the escape normal form, the event compiler is
\[
S_{\rm rect}=O(qN+(s+1)(\xi+\kappa+q)),
\]
where $s$ is the number of distinct escape-source carriers, $\xi$ counts candidate-side escape incidences, and $\kappa$ counts carrier covers (C-94). These bounds can beat $q^3$ for sparse SCCs, few carriers, or a small escape system; none proves a worst-case $O(q\operatorname{polylog}N)$ conversion. The missing cost is the routing/acyclicization of recursive alternatives, not the existence of q named activation predicates.

### Stress test of universal evaluation

A universal circuit can evaluate (G(d)_k) from a description (d) and a coordinate (k). That is Alice-local work. It does not decide, with a small shared state graph, which coordinate differs from Bob's arbitrary (z). The predicate ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œsome mismatch lies in interval (I)ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â is generally not a rectangle: on Alice rows \(\{00,11\}\) and Bob columns \(\{00,11\}\), the mismatch pairs are off-diagonal. A state that remembers only the scan position and merges prefix histories consequently admits pairs whose first mismatch was already discarded.

The valid pattern-sharing construction stores each occurring restriction (u=w|_I) as a state (R_{I,u}); its size is
\[
O\!\left(|Y|+\sum_{I\text{ dyadic}}\pi_I(Y)\right),\qquad
\pi_I(Y)=|\{w|_I:w\in Y\}|.
\]
Since \(\pi_I(Y)\le\min\{|Y|,2^{|I|}\}\), this is at most $O(|Y|N/\log|Y|+N\log N)$ for large $|Y|$. The circuit-counting upper bound gives $\log|Y|=O(s_1\log(n+s_1))=O(N^\beta)$, while the block-constant subfamily from C-80 gives $\log|Y|=\Omega(s_1)=N^{\beta-o(1)}$. Thus this particular profile bound remains exponential in $N^{\beta+o(1)}$, not near-linear. It is an upper bound for this construction only.

**Candidate non-shareability principle (not proved).** A standard rect-DAG can exploit short descriptions only if it compresses the *range-separation* problem: it must distinguish the image (G(D_1)) from all high tables while preserving rectangle validity at every state. In formula form the low side is
\[
w\in Y\iff \exists d\in D_1\;\forall k<N,\;w_k=G(d)_k,
\]
while a promise separator need only be 1 on this image and 0 on (Z), with the medium band unconstrained. A universal evaluator supplies the relation inside this quantifier; it does not eliminate the description quantifier or provide rectangle-valid shared states. A lower bound on that range-separation cost would be a genuine non-shareability theorem. No lower bound of this form has been proved, and no (N^{1+o(1)})-size universal DAG has been constructed.

### Literature boundary and status

The model comparison is now explicit. Sokolov's Boolean games are acyclic, binary-outdegree rectangle DAGs and have the circuit correspondence; GGKS use this DAG setting for the full monotone KW relation, so their theorem is not directly a lower bound for this partial, non-monotone signed-mismatch promise. Cavalar-Oliveira's Theorem 30 is the exact identity for this fusion/semi-filter cover and its cyclic intersection measure. They describe it as an adaptation of NakayamaÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka's loop-circuit connection; the generalized approximation functionals in NM95 are not themselves identical to the semi-filter cover. AmanoÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka conjunctive complexity is the acyclic AND-count analogue, with results for quadratic Boolean functions, not a theorem about the Gap-MCSP separator. Primary sources: [Sokolov, *Dag-like Communication and Its Applications*](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download), [GargÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“GÃƒÆ’Ã‚Â¶ÃƒÆ’Ã‚Â¶sÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“KamathÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Sokolov, *Monotone Circuit Lower Bounds from Resolution*](https://theoryofcomputing.org/articles/v016a013/), [CavalarÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://arxiv.org/abs/2503.14117), [NakayamaÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka, *Loop Circuits and Their Relation to Razborov's Approximation Model*](https://doi.org/10.1006/inco.1995.1083), and [AmanoÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Maruoka, *The Monotone Circuit Complexity of Quadratic Boolean Functions*](https://doi.org/10.1007/s00453-006-0073-0).

**Adjacent MCSP literature checked.** The OPS magnification paper states the relevant target: for small enough $\beta$, a general-circuit lower bound $\mathrm{Gap\text{-}MCSP}[2^{\beta n}/(cn),2^{\beta n}]\notin\mathrm{Circuit}[N^{1+\epsilon}]$ implies $\mathrm{NP}\not\subseteq\mathrm{Circuit}[\mathrm{poly}]$; this is the theorem the project is trying to reach, not a DAG lower bound already supplied by that paper ([OliveiraÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Pich, *Hardness Magnification Near State-of-the-Art Lower Bounds*](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf)). Existing near-quadratic formula results and AC$^0[p]$ lower bounds are restricted models; they do not imply a lower bound for unrestricted Boolean separator circuits. A new 2026 ECCC report proves conditional NP-hardness for *implicit* Gap-ImpMCSP given by a sampling circuit under cryptographic and proof-complexity assumptions, but that has a different input representation and approximation promise, and gives no unconditional lower bound on this project's $\mathrm{SepCirc}(Y,Z)$ ([GoldbergÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“JuvekarÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Kabanets, ECCC TR26-091](https://eccc.weizmann.ac.il/report/2026/091/download/)). The SoS MCSP results lower-bound proof degree/size for certifying circuit lower bounds, not the Boolean circuit size of a promise separator ([AustrinÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Risse](https://arxiv.org/abs/2311.12994)).

**Tier and next work.** The description relabelling proposition is a proved model-invariance result (Tier 4 in the requested hierarchy), and the interval-scan failure is precise but architectural (Tier 5). A standard rect-DAG of size $N^{1+o(1)}$ would give $\rho_{\rm prom}\le N^{1+o(1)}$ by the reverse map, decisively killing the desired $\rho>N^{1+\epsilon}$ route for every fixed $\epsilon>0$. No such DAG has been found. The actual Tier 1ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“3 goal remains untouched: prove $\mathrm{SepCirc}>N^{1+\epsilon}$ with near-lossless transfer, prove the stronger threshold needed to survive a cubic loss, or prove direct cyclic non-shareability $q>N^{1+\epsilon}$. Do not present the failure of universal evaluation as a lower bound.
## 28. C-98 - A PRF gives a conditional shared-DAG non-shareability theorem

This is a conditional stress test of the exact promise separator from C-97. It does not assume that a separator is an MCSP decider, so its values on the medium band remain free.

**Assumption.** There is a one-bit PRF family F_(lambda,k):{0,1}^lambda -> {0,1}, with lambda-bit keys, evaluation circuits of size at most lambda^d for a fixed d, and security against nonuniform polynomial-size distinguishers making polynomially many oracle queries. The nonuniform clause matters because a candidate separator circuit can be advice to the distinguisher.

**Claim.** Fix any project constant 0 < beta < 1 and c > 0, with
s1 = N^beta/(c n), s2 = N^beta, N = 2^n.
Under the assumption, for every constant C > 0, all sufficiently large n have
SepCirc(Y,Z) > N^C and hence S_rect(Mis_Y,Z) > N^C.
Consequently rho_prom = N^(omega(1)) under this cryptographic assumption.

**Proof.** Choose a constant a with a*beta > d, and for each n choose an integer security parameter lambda = Theta(N^(1/a)), so N = Theta(lambda^a) and N is polynomial in lambda. Restrict the PRF domain to the N points 0^(lambda-n)x, x in {0,1}^n, and view the resulting N-bit output as a truth table T_k. Padding preserves pseudorandomness for this restricted domain: an oracle distinguisher can make all N queries, and N = poly(lambda). Each T_k has circuit size at most lambda^d, which is at most s1 for all large n, since s1 = Theta(lambda^(a beta)/log lambda). Thus every PRF table lies in Y.

Circuit counting gives
|SIZE(s2)|/2^N <= 2^(-N+O(s2 log(s2+n))) = 2^(-N+o(N)),
because s2 = N^beta and beta < 1. Therefore a uniformly random N-bit table lies in Z with probability 1 - 2^(-N+o(N)).

If h were a separator of size at most N^C, an oracle distinguisher could query all N padded points, assemble their truth table, and output h(T). It accepts every PRF oracle, while it accepts a random function with probability at most 2^(-N+o(N)), since h=0 throughout Z. Its size and query count are polynomial in lambda, as N = Theta(lambda^a) and C is fixed. Its distinguishing advantage tends to 1, contradicting the assumed PRF security. If separators of size N^C existed for infinitely many n, the corresponding h_n can be supplied as nonuniform advice on the associated infinitely many security parameters; define the distinguisher to output 0 at other parameters. The resulting advantage is non-negligible infinitely often, also forbidden by security. Hence all sufficiently large n have no such separator. C-89/C-97 give S_rect asymp SepCirc, rho_prom <= O(S_rect) <= O(rho_prom^3); the cubic inequality then forces rho_prom to exceed every fixed polynomial in N. QED.

**What this tests.** The C-75 shared-DAG target is genuinely a range-separation problem: under a nonuniform-secure PRF assumption, no polynomial-size DAG can share enough work, even though each low row has a polynomial-size individual description. The argument uses the same core phenomenon already known for MCSP: pseudorandom-function tables have small circuits while random tables almost surely have high circuit complexity. See [Golovnev et al., ECCC TR19-018](https://eccc.weizmann.ac.il/report/2019/018/download/) for this established MCSP/PRF paradigm.

**Boundary.** This is not an unconditional lower bound and does not identify a new unconditional non-shareability invariant. It requires nonuniform PRF security, and its conclusion is conditional. It supplies a precise conditional benchmark for any proposed universal DAG: a polynomial-size construction would contradict PRFs. It does not show that a universal DAG exists or that PRFs exist. The usual tree-versus-DAG calibration remains parity: its search relation has an O(N)-node DAG but formula/tree size Omega(N^2); that example explains why the communication-bit upper bound is not the resource at issue, but it is not a lower bound for Gap-MCSP.
## 29. C-99 - The PRF benchmark already assumes the circuit separation

C-98 is a valid conditional non-shareability theorem, but its cryptographic hypothesis is not an independent route to P versus NP.

**Proposition.** Under the nonuniform-secure PRF assumption in C-98, \(\mathrm{NP}\not\subseteq\mathrm{P/poly}\), and therefore \(P\ne NP\).

**Proof.** Assume instead \(\mathrm{NP}\subseteq\mathrm{P/poly}\). MCSP is in NP: a circuit of size at most the threshold is a polynomial-size witness (after capping thresholds above the Shannon bound), and it can be checked against all N truth-table entries in polynomial time in the input length. Hence MCSP has polynomial-size nonuniform circuits.

For each n, apply the MCSP circuit to the truth table T with threshold \(s_2=N^\beta\). It outputs 1 on every \(w\in Y\), because \(\mathrm{CC}(w)\le s_1<s_2\), and 0 on every \(z\in Z\), because \(\mathrm{CC}(z)>s_2\). Fixing the threshold yields a polynomial-size promise separator \(h_n\). Under C-98's embedding \(N=\Theta(\lambda^a)\), this circuit has size polynomial in \(\lambda\). A nonuniform oracle distinguisher queries the N padded points, evaluates \(h_n\), and accepts PRF truth tables while rejecting a uniformly random truth table except with probability \(2^{-N+o(N)}\). This contradicts the assumed PRF security. Thus \(\mathrm{NP}\not\subseteq\mathrm{P/poly}\), which implies \(P\ne NP\). QED.

This also matches the established MCSP/PRF mechanism: MCSP distinguishes small-circuit PRF outputs from random high-complexity truth tables ([Golovnev et al., ECCC TR19-018](https://eccc.weizmann.ac.il/report/2019/018/download/)). The C-98 quantitative consequence \(\rho_{\rm prom}=N^{\omega(1)}\) remains a correct conditional theorem, but the assumption already entails the desired class separation. The C-98 line is therefore a calibration of the DAG measure under cryptographic hardness, not an independent proof strategy toward P versus NP.

**Model boundary.** The argument needs nonuniform PRF security because the separator family \(h_n\) may be nonuniform. Uniform PRF security alone does not rule out such an arbitrary circuit family unless one also gives effective uniform descriptions of the separators.

## 30. C-100 - Batched subset-ORs sharpen the cyclic-to-DAG compiler

This is a compiler improvement, not a lower bound. It attacks one avoidable cost in C-94: separately building many ORs over the same changing input vector.

**Subset-OR lemma.** Given \(r\) specified subsets \(S_1,\ldots,S_r\subseteq[m]\), all outputs
\[
y_i=\bigvee_{j\in S_i}x_j
\]
can be computed by a fan-in-two monotone circuit of size
\[
O\!\left(r\left(1+\frac{m}{\min\{m,\log_2(r+1)\}}\right)\right).
\tag{C100.1}
\]
For \(r=1\), the direct \(O(m)\) construction suffices. For \(r\ge2\), partition the \(m\) input bits into blocks of \(k=\min\{m,\lfloor\log_2r\rfloor\}\) bits. In each block, compute the OR for every subset, using at most \(2^k\le r\) gates. Each prescribed \(S_i\) is the OR of at most \(\lceil m/k\rceil\) such block values, costing at most that many additional gates. The total is \(O(r\lceil m/k\rceil)\), which gives (C100.1). Empty subsets output 0. This is a standard block-subset/Four-Russians-style batching argument; no lower bound on this construction is claimed.

**Apply it to C-94.** Keep the C-94 quotient and notation: \(q\) rules, \(p\) distinct carriers, \(s\) distinct escape-source carriers, \(\xi\) candidate-side escape incidences, and \(\kappa\) Hasse-cover edges. A successful list has \(q\ge N-\log_2M_2-1=N-o(N)\), so \(q\ge N/2\) for large \(N\).

* The \(2q\) literal-seed clauses are ORs of subsets of the \(2N\) signed-literal indicators. Apply (C100.1) once to compute them all. Their cost is \(O(qN/\log N)\) when \(q\ge N/2\).
* In each escape macro-round, the \(2q\) escape-support ORs can either be built from their incidences for \(O(\xi+q)\) gates or batched over the \(s\) source-state bits for \(O(q(1+s/\log(q+1)))\) gates. Take the smaller bound.
* The upward-closure map on the \(p\) carriers is \(x_t=\bigvee_{u\subseteq t}D_u\). It can be computed by propagating over the Hasse DAG in \(O(p+\kappa)\) gates, or by batching the \(p\) fixed down-set ORs in \(O(p+p^2/\log(p+1))\) gates. Take the smaller bound.
* Candidate conjunctions and the OR over alternatives cost \(O(q)\) per macro-round. C-94's least-fixed-point argument still gives at most \(s+1\) macro-rounds.

Therefore the promise separator, and hence a standard rect-DAG up to the usual constant-factor circuit/game translation, has size
\[
S_{\rm rect}=O\!\left(
\frac{qN}{\log N}
+(s+1)\left[
q+\min\!\left\{\xi,\ q\left(1+\frac{s}{\log(q+1)}\right)\right\}
+\min\!\left\{p+\kappa,\ p+\frac{p^2}{\log(p+1)}\right\}
\right]\right).
\tag{C100.2}
\]
The expression is interpreted with constant-sized terms when \(p\) or \(s\) is bounded. The circuit computes the same least fixed point; batching changes only how each fixed family of ORs is implemented.

Using \(p,s\le q\), \(\xi\le2qs\), and \(\kappa\le p^2\), (C100.2) gives the worst-case bound
\[
S_{\rm rect}=O(q^3/\log(q+1))
\]
for large \(q\ge N/2\), improving C-94's \(O(q^3)\) by a logarithmic factor. The reverse transfer remains \(\rho_{\rm prom}\le O(S_{\rm rect})\). Thus if \(q\le N^{1+\epsilon}\), this compiler yields \(S_{\rm rect}=O(N^{3+3\epsilon}/\log N)\); a separator lower bound asymptotically larger than this scale (with constants handled) would force \(q>N^{1+\epsilon}\). The improvement does not approach the desired \(O(q\,\mathrm{polylog}\,N)\) simulation and does not provide a separator lower bound.

**What the attempted universal DAG still says.** The description-space section argument in C-97 is decisive for this branch: any DAG whose local predicates use a circuit description \(d\) can be restricted along a section \(w\mapsto d_w\), with no change to the graph. A description-aware small DAG would therefore already be a small promise separator circuit on the truth-table input. Universal evaluation \(G(d)_k\), fingerprints, or a short protocol transcript do not bypass this range-separation problem. The block-constant subfamily from C-80 still warns that a large low-row count alone cannot prove non-shareability: a highly structured exponential subfamily has an \(O(N)\) DAG.

**Tier and next target.** C-100 is Tier 5 (a sharper reformulation/compiler bound), not Tier 1ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“3. Continue with either a direct lower bound on the least-fixed-point state count \(q\), or an unconditional separator lower bound strong enough to survive (C100.2). Any proposed state-merging lemma must be tested against the block-constant family and against the unrestricted local predicates allowed by the rect-DAG model.

## 31. C-101 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Terminal cones as high-free coordinate subcubes

This tests whether VC-dimension or subcube structure strengthens the C-96 terminal-cone count.

For the truth-table class \(\mathcal C_{s_2}=\mathrm{SIZE}(s_2)\subseteq\{0,1\}^N\), define its **contained coordinate-cube dimension**
\[
\Delta_\Box(s_2)=\max\{ |J|: \exists a\in\{0,1\}^{[N]\setminus J},\ \{a\cup u:u\in\{0,1\}^J\}\subseteq\mathcal C_{s_2}\}.
\]
This is at most the ordinary VC dimension of the circuit class on the \(N\) truth-table positions, because every pattern on \(J\) occurs. It is stronger than ordinary shattering: all completions must share one fixed pattern outside \(J\).

**Terminal-cone implication.** In C-96, let \(\Phi_w\) be the \(m\)-clause seed CNF for a selected terminal support cone. It has no high-table satisfying assignments, so every satisfying table lies in \(\mathcal C_{s_2}\). Select one literal made true by \(w\) from each clause. Fixing those literals fixes at most \(m\) truth-table coordinates and leaves a coordinate subcube of dimension at least \(N-m\), wholly inside \(\mathcal C_{s_2}\). Therefore
\[
m\ge N-\Delta_\Box(s_2).
\]

**Counting ceiling.** A bounded-fanin circuit of size at most \(s_2\) has at most \(2^{O(s_2\log(n+s_2))}\) descriptions, by specifying each gate type and its incoming wires. Any contained \(d\)-cube consists of \(2^d\) distinct such truth tables. Hence
\[
\Delta_\Box(s_2)\le O(s_2\log(n+s_2)),\qquad
m\ge N-O(s_2\log(n+s_2))=N-o(N)
\]
at the OPS parameters. This recovers the C-96 scale, not a stronger cross-anchor bound.

The parameter is not vacuous: choose a \(k\)-dimensional subcube \(A\subseteq\{0,1\}^n\) of input points, and let \(J=A\) as truth-table coordinates. For every labeling of \(A\), extend it by zero outside \(A\). A circuit computes the indicator of \(A\) and an arbitrary \(k\)-input truth table on \(A\); Shannon expansion computes the latter in \(O(2^k)\) gates. Thus, when \(s_2\gg n\), choosing \(2^k=\Theta(s_2)\) gives
\[
\Delta_\Box(s_2)\ge\Omega(s_2).
\]
This lower witness is a *localized input subcube*. The C-80 block-constant family is a large structured family, but its equalities across fibers do not make it a coordinate subcube; do not substitute it for this construction. The remaining gap between \(\Omega(s_2)\) and \(O(s_2\log(n+s_2))\) does not help C-96 because only the upper bound on \(\Delta_\Box\) enters the cone lower bound.

**Literature boundary.** Ordinary VC dimension is not the exact parameter needed here because it allows the outside truth-table bits to vary. Koiran's report titled *VC Dimension in Circuit Complexity* concerns a lower bound for sigmoidal circuits and does not supply a sharper contained-cube theorem for standard Boolean circuits ([ECCC TR95-051](https://eccc.weizmann.ac.il/report/1995/051/download/)). Generic circuit counting already gives the applicable upper bound. No published result located in this audit improves the cone estimate in the required setting.

**Status.** The terminal-cone subcube reformulation is proved, but it is Tier 5: it repackages the existing \(N-o(N)\) local clause bound. It does not constrain overlap of cones across low anchors. The live question is still whether different anchors can reuse the same cone states while keeping every high table outside the least closure.

## 32. C-102 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â High tables split a fiber of every low-table partition

For \(w\in Y\), partition the input domain \(X=\{0,1\}^n\) into fibers \(F_b(w)=\{x:w(x)=b\}\), \(b\in\{0,1\}\). For every \(z\in Z\), there are \(a,b\in X\) such that
\[
w(a)=w(b)\quad\text{and}\quad z(a)\ne z(b).
\]
**Proof.** If \(z\) were constant on each nonempty fiber of \(w\), then \(z=g\circ w\) for a unary Boolean map \(g\). There are only four such maps, so \(z\in\{0,1,w,\neg w\}\). Constants and \(w,\neg w\) have circuit size at most \(\mathrm{CC}(w)+O(1)\le s_1+O(1)<s_2\) for the project parameters, contradicting \(z\in Z\). Therefore one fiber contains both a \(z=0\) and a \(z=1\) point.

This defines a total **fiber-disagreement search relation** with output \((a,b)\). For each fixed pair \((a,b)\), its valid inputs form the rectangle
\[
\{w:w(a)=w(b)\}\times\{z:z(a)\ne z(b)\}.
\]
The \(O(N^2)\) such rectangles give a nondeterministic certificate cover: a prover can name \(a,b\) using \(2\log N\) bits, and Alice/Bob verify their respective conditions locally. That cover does **not** give a deterministic protocol DAG: the parties must route around a candidate when only one side's test succeeds, and a cover by output rectangles does not provide a valid binary routing of the whole \(Y\times Z\) rectangle. A deterministic protocol can still send Alice's circuit description and let Bob search, at \(O(s_1\log(n+s_1)+\log N)\) bits; its graph size is not thereby bounded.

The relation recasts the promise as follows: every high table cuts at least one edge inside the two-clique graph induced by each low table's fibers. This is a precise structural fact, but the obvious edge certificate has \(N^2\) candidates, and no lower bound on the shared DAG or reduction to the fusion activation graph follows. To connect it to C-75, one would need a theorem that maps a ranked fusion path to a fiber edge with controlled state cost, or proves that one DAG must route incompatible fiber partitions through many residual rectangles. Neither implication is established.

**Status and next falsification.** This is a candidate reformulation (Tier 5), not a non-shareability lemma. Try either a deterministic \(o(N^2)\) universal DAG for this fiber search on all low/high pairs, or a reduction showing that a small such DAG would yield a small separator for \(Y\) versus \(Z\). Until one is proved, the fiber relation is auxiliary and cannot replace the C-75 mismatch target.

## 33. C-103 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â A small fiber-disagreement DAG would kill the mismatch lower-bound route

Let \(S_{\mathrm{fib}}\) be the size of a standard binary-outdegree Boolean communication game for the total fiber-disagreement relation on \(Y\times Z\), and let \(S_{\mathrm{mis}}\) be the size for signed mismatch.

**Proposition.**
\[
S_{\mathrm{mis}}\le O(S_{\mathrm{fib}}),\qquad \rho_{\mathrm{prom}}\le O(S_{\mathrm{fib}}).
\]

**Proof.** At a fiber-game leaf labeled by \((a,b)\), every pair \((w,z)\) in its valid rectangle satisfies \(w(a)=w(b)\) and \(z(a)\ne z(b)\). Split that rectangle first according to Alice's common bit \(c=w(a)\), then according to Bob's orientation \((z(a),z(b))\in\{(0,1),(1,0)\). This takes a constant-size binary rectangle tree. Each resulting leaf has a fixed valid mismatch output: if the orientation is \((0,1)\), output \(b\) when \(c=0\) and \(a\) when \(c=1\); for orientation \((1,0)\), reverse those choices. Replacing each original leaf by this constant-size gadget yields a mismatch game with \(O(S_{\mathrm{fib}})\) vertices. The C-90 reverse map from a mismatch rect-DAG to the active promise fusion cover costs another constant factor. QED.

Hypothetically, an N^(1+o(1))-size fiber DAG would give rho_prom <= N^(1+o(1)); C-105 now proves that antecedent impossible for fixed beta<1 by an output-label lower bound. The actual C-105 lower bound remains auxiliary: C-104 loses O(N^2) in the reverse conversion and yields no mismatch-DAG lower bound.


## 34. C-104 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â The reverse fiber reduction exists, but loses N-squared

C-103 gave \(S_{\mathrm{mis}}(Y,Z)\le O(S_{\mathrm{fib}}(Y,Z))\). There is also a polynomial reverse simulation if the fiber relation is taken on the one-gate-smaller row set \(Y^- = \mathrm{SIZE}(s_1-1)\), so that complements remain in \(Y\).

**Proposition.**
\[
S_{\mathrm{fib}}(Y^-,Z)\le O\!\left(N^2 S_{\mathrm{mis}}(Y,Z)\right).
\]

**Construction.** Run a mismatch game on the constant-zero anchor to obtain \(p\) with \(z_p=1\). For each possible \(p\), attach a copy of the game on the constant-one anchor; its output \(q\) has \(z_q=0\). The graph now remembers \((p,q)\) in its copy index, using \(O(N^2 S_{\mathrm{mis}})\) vertices overall. For \(w\in Y^-\), let \(a=w_p\), \(b=w_q\). A constant-size rectangle gadget splits on Alice's two bits:

- if \(a=b\), output \((p,q)\);
- if \((a,b)=(0,1)\), run a mismatch game on \((\neg w,z)\). Its output \(r\) satisfies \(w_r=z_r\); pair \(r\) with \(p\) if \(w_r=0\), and with \(q\) if \(w_r=1\);
- if \((a,b)=(1,0)\), run a mismatch game on \((w,z)\). Its output \(r\) satisfies \(w_r\ne z_r\); pair \(r\) with \(q\) if \(w_r=0\), and with \(p\) if \(w_r=1\).

In every case the two selected positions have equal \(w\)-bits and different \(z\)-bits. The copy index retains \((p,q)\), and the signed mismatch leaf supplies enough orientation information to label the final output. Since \(\neg w\in Y\) for \(w\in Y^-\), each possible mismatch call is inside the game domain. There are \(O(N^2)\) indexed copies, each of size \(O(S_{\mathrm{mis}})\), plus constant selector/leaf overhead per pair.

Combining C-103/C-104 gives a one-sided-in-threshold equivalence with an \(N^2\) factor, not a near-lossless reduction. By C-100, a q-pair cover with \(q\le N^{1+\epsilon}\) gives
\[
S_{\mathrm{fib}}(Y^-,Z)\le O\!\left(\frac{N^{5+3\epsilon}}{\log N}\right).
\]
Therefore a fiber-DAG lower bound above this scale would imply the target, but it is quantitatively worse than attacking mismatch/cyclic fusion directly. The new relation does not improve the current route; it closes the reverse-conversion question only at a lossy polynomial scale.



## 35. C-105 Ã¢â‚¬â€ Leaf-label graph lower bound for fiber disagreement

This is a lower bound for the **auxiliary fiber-disagreement relation**, not for the C-75 mismatch relation. It extracts a necessary global condition on the output labels of any shared DAG.

Let \(\mathcal E\subseteq\binom{X}{2}\), \(|X|=N\), be the set of unordered pairs that occur as leaf outputs of a purported fiber-disagreement game on \(Y^-\times Z\), where \(Y^- = \mathrm{SIZE}(s_1-1)\). For every low anchor \(w\), each output edge must have equal \(w\)-bits at its endpoints; for every high table \(z\), a valid leaf also needs different \(z\)-bits.

**Theorem.** For fixed \(0<\beta<1\) at the OPS thresholds,
\[
|\mathcal E|=\Omega\!\left(\frac{N^2}{s_2 n}\right)=\Omega\!\left(\frac{N^{2-\beta}}{n}\right).
\]
Consequently every standard rect-DAG for fiber disagreement has at least this many vertices, since each distinct leaf label requires a leaf.

**Proof.** Let \(M_2=|\mathrm{SIZE}(s_2)|\le 2^{K s_2 n}\) for a constant \(K\), by circuit-description counting. Choose a power of two \(a=2^k\) with \(C s_2 n\le a<2C s_2 n\), where \(C\) is a sufficiently large constant. Every affine subspace \(A\subseteq\mathbb F_2^n\) of dimension \(k\) has indicator \(w_A=1_A\) computable by \(O(n^2)\) gates, hence \(w_A\in Y^-\) for large \(n\).

Suppose some such \(A\) spans fewer than \(a/8\) edges of \(\mathcal E\). Then more than \(3a/4\) vertices of \(A\) are isolated in the induced graph \(\mathcal E[A]\). Put \(t=\lfloor a/4\rfloor\). There are at least \(\binom{3a/4}{t}\ge2^{c a}\) choices of a size-\(t\) set \(S\) of isolated vertices, for an absolute \(c>0\). Choose \(C>K/c\), so this number exceeds \(M_2\). At least one truth table \(z_S=1_{A\setminus S}\) therefore has circuit complexity greater than \(s_2\), i.e. lies in \(Z\).

For this pair (w_A,z_S), an output edge cannot be valid. An edge crossing A and its complement has unequal w_A values; an edge outside A has equal zero z_S values; and an edge inside A cannot cross from S to A minus S, because every point of S is isolated in E[A]. Thus no leaf label in E is a valid output, contradicting totality. So every affine k-subspace spans at least a/8 output edges.

A uniformly random affine \(k\)-subspace contains any fixed pair of distinct points with probability \(a(a-1)/(N(N-1))\). Averaging the induced edge count gives
\[
|\mathcal E|\frac{a(a-1)}{N(N-1)}\ge\frac a8,
\]
which implies \(|\mathcal E|\ge N(N-1)/(8(a-1))=\Omega(N^2/a)\), as claimed. QED.
The proof uses only that every low/high pair has some valid edge in the fixed set E. It therefore lower-bounds any universal output list, equivalently any nondeterministic cover by edge-output rectangles, not just the leaf labels of a deterministic DAG.

**What this does and does not buy.** This proves an auxiliary relation-level shared-DAG lower bound \(N^{2-\beta-o(1)}\) from output-label non-shareability alone. It does not lower-bound the C-75 mismatch DAG. C-104 only gives \(S_{\mathrm{fib}}(Y^-,Z)\le O(N^2 S_{\mathrm{mis}}(Y,Z))\); dividing the new bound by \(N^2\) gives no nontrivial mismatch lower bound. Combined with the q-to-DAG compiler, the bound is far below the required \(N^{5+3\epsilon}/\log N\) fiber scale. The important remaining possibility is a direct map from the q-state fusion trace to fiber outputs with substantially less than \(N^2\) index memory; none is known.

## 36. C-106 - The fiber lower bound has a conditional bridge to q, but the bridge is missing

For a fixed low/high pair (w,z), let C_ab be the set of input points x with w(x)=a and z(x)=b. A fiber-disagreement output exists exactly when either C_00 and C_01 are both nonempty, or C_10 and C_11 are both nonempty. The C-75 closure path emits only one signed mismatch coordinate, hence one point in C_01 or C_10. Even one additional agreement point can be in the opposite w-row: C_01 together with C_11, for example, gives no fiber witness. The totality proof for fiber disagreement guarantees a same-row opposite-z pair exists, but the closure path does not identify its second point.

This is an output-type and state-memory gap, not a proof that no reduction exists. C-104 resolves it for a generic mismatch DAG by making several mismatch calls and retaining coordinate outputs in the graph state; the current construction pays O(N^2) copies. A q-fusion list consists of semantic set pairs, and its ranked path emits one signed coordinate rather than a preassigned list of coordinate-pair outputs.

**Conditional transfer target.** Suppose a successful q-pair fusion cover Q induced a fixed set E_Q of coordinate pairs such that every (w,z) in Y x Z has a fiber witness in E_Q, and suppose |E_Q|=O(q log^d N) for some fixed d. C-105 would imply q=Omega(N^(2-beta)/(log N)^(d+1)), which is superlinear for every fixed beta<1, and exceeds N^(1+epsilon) for every fixed epsilon<1-beta. This would be a strong non-shareability theorem. No construction of E_Q, or proof that Q implies such a universal output list, is known. In particular, the ranked path's single mismatch coordinate is insufficient by itself.

**Status.** C-105 rules out an N^(1+o(1))-size standard DAG for the auxiliary fiber relation at every fixed beta<1, by output labels alone. That closes the fiber-DAG small-upper-bound falsification branch. Its hardness does not lower-bound mismatch or rho because C-104 loses N^2. Keep the project target on the cyclic q-state system; use the conditional E_Q statement as the exact bridge obligation, not as a claimed consequence of Q.


## 37. C-107 - A raw local mismatch lift cannot avoid false fiber outputs

A tempting shared-DAG shortcut is to lift each coordinate pair (a,b) to one coordinate of two encoded tables, computed separately from Alice's pair pattern u=(w(a),w(b)) and Bob's pair pattern v=(z(a),z(b)). The fiber-valid pattern region is

- Alice patterns A={00,11}, meaning w(a)=w(b);
- Bob patterns B={01,10}, meaning z(a) differs from z(b).

Both A and B are nonempty proper subsets of the four pair patterns. The OPS promise realizes every Alice pattern by some low table, and every Bob pattern extends to a high table by two-coordinate shattering of Z.

**No-go lemma.** Let F and G be any local encodings of these patterns into a common alphabet, including vector-valued encodings. If F(u) != G(v) is allowed only for fiber-valid patterns u in A and v in B, then F and G must be constant and equal, so there are no mismatch outputs at all.

**Proof.** Choose u0 outside A and v0 outside B. Since their pair is invalid, F(u0)=G(v0)=gamma. For every u in A, (u,v0) is invalid, so F(u)=gamma. For every v in B, (u0,v) is invalid, so G(v)=gamma. The same invalid-pair constraints with v0 or u0 force F(u)=gamma for u outside A and G(v)=gamma for v outside B. Thus both encodings are identically gamma and never mismatch. QED.

In particular, the pairwise-parity lift produces a bad mismatch when w(a) differs from w(b) while z(a) equals z(b); no pointwise independent recoding of the two pair patterns can remove every false output while retaining a valid one. This rules out the input-only shortcut that treats every mismatch of the lifted tables as a valid fiber witness. It does not rule out a DAG that routes around bad candidate pairs and selects only valid mismatches using further stateful computation; that global routing problem remains open.




## 38. C-108 - A near-optimal universal edge list exists, but it is not yet a DAG

This sharpens the auxiliary fiber relation's output-label analysis. Let n=log2 N, s1=N^beta/(c n), s2=N^beta, with fixed 0<beta<1, and use the one-gate-smaller low class Y^-=SIZE(s1-1) from C-105.

**Patching-distance lemma.** There is an absolute basis constant C0 such that if z differs from any unary postprocessing g composed with w on t input points, then CC(z) <= CC(w)+C0 n(t+1). Start with g(w) and hardwire the exceptional points using their n-bit minterms. Therefore, for w in Y^- and z in Z, the distance from z to each of 0, 1, w, and not-w exceeds 2r, where

r=floor((s2-s1)/(8 C0 n))=Theta(s2/n).

Write A_b={x:w(x)=b}, and r_b=min(|A_b intersect z^-1(0)|, |A_b intersect z^-1(1)|). The closest unary postprocessing of w disagrees with z on r_0+r_1 points, so r_0+r_1>2r. At least one fiber A_b is therefore cut by z into two parts each of size at least r.

**Random universal edge list.** Choose each unordered pair of the N domain points independently with probability p=C n/r, for a sufficiently large constant C. We show that, simultaneously for every low w, each fiber A_b has an edge across every cut S, A_b minus S with both sides at least r. For a fixed fiber of size m>=2r and a fixed such cut, there are at least r(m-r)>=rm/2 possible crossing edges, so the probability of missing all of them is at most exp(-p r m/2). Union-bounding over at most 2^m cuts gives failure probability at most

exp(m ln 2 - C n m/2) <= exp(-C n m/4) <= exp(-C n r/2) = exp(-Omega(C s2)).

There are at most 2|Y^-| fibers to check, and circuit-description counting gives log |Y^-|=O(s2). Taking C large makes the union-bound failure probability less than 1/4. Also p=o(1), and a standard concentration bound gives a graph with O(p N^2)=O(N^2 n^2/s2) edges while retaining the cut property. Fix such an edge set E.

For any w in Y^- and z in Z, the distance argument gives a fiber cut with both sides at least r; the graph has an E-edge crossing it. Hence E is a universal output-label set for fiber disagreement. C-105 lower-bounds every such set by Omega(N^2/(s2 n)). Consequently the minimum universal fiber-edge list has size between

Omega(N^2/(s2 n)) and O(N^2 n^2/s2),

within a factor O(n^3). This is a near-tight characterization of the nondeterministic output-list size, not of deterministic rect-DAG size.

**Why the list does not immediately give a small DAG.** For a fixed list e_1,...,e_m, define Alice's bit P_i(w)=1 when e_i lies inside a w-fiber and Bob's bit Q_i(z)=1 when z changes across e_i. Totality says the two sets intersect. A serial search that tests i and advances after a failure has residual condition

intersection over j<=i of ((not P_j x Z) union (Y^- x not Q_j)),

which is generally a union of rectangles, not one rectangle. Merging all histories into a suffix state loses which party failed on earlier candidates; the enlarged rectangle can contain pairs whose only valid edge was skipped. This is the same cover-versus-routing obstruction from C-102.

A valid but coarse deterministic rect-DAG follows Alice's branch to the exact low row w, then lets Bob choose the first valid edge from E. It has O(|Y^-| m)=2^(O(s2)) N^(2-beta) n^2 vertices. This uses the short row description only by enumerating the low class and is far from near-linear. The random edge list therefore nearly matches C-105's label bound but does not yield a shared-state lower bound for the C-75 relation or an efficient deterministic router.


## 39. C-109 - Small tuples of low anchors share a fiber witness against every high table

Let w_1,...,w_r be low tables and define their joint label W(x)=(w_1(x),...,w_r(x)). If z is constant on every fiber of W, then z=h(W) for a Boolean h on at most 2^r patterns. Computing all w_j and then a DNF for h costs at most

r s1 + O(r 2^r)

gates. Choose a fixed eta>0 with eta<beta and eta/c sufficiently small, and take r<=eta n. Since s1=N^beta/(c n), the first term is at most (eta/c)N^beta, while r2^r=O(nN^eta)=o(N^beta). For sufficiently small eta and large n, this total is below s2=N^beta. Thus a high z cannot be constant on every joint fiber.

**Joint-fiber lemma.** For every tuple of r<=eta n low tables and every z in Z, there are input points a,b such that

w_j(a)=w_j(b) for every j in [r], while z(a) != z(b).

So a single fiber edge is a valid output simultaneously for all rows in any such tuple, although the edge may depend on z. This blocks a simple fooling-family strategy based on finding O(log N) low rows with pairwise incompatible valid outputs. It does not supply a fixed edge label for the whole high column set and does not bound DAG state count; the unresolved sharing resource remains how the DAG routes to a z-dependent common edge.

## 40. C-110 - Rectangle-hull constraint on state merging

This is a precise form of the history-loss obstruction for standard rect-DAGs. It applies to the total signed-mismatch relation on \(Y\times Z\), and to any other search relation with rectangular node semantics.

Let \(\Pi\) be a rect-DAG. Each vertex \(v\) has a rectangle \(R_v=A_v\times B_v\); its children cover \(R_v\), and every leaf is labelled by an output valid throughout its leaf rectangle. Let \(\Lambda(v)\subseteq[N]\) be the coordinates appearing on leaves reachable from \(v\). Since the graph below \(v\) is finite and acyclic, every pair in \(R_v\) reaches a valid descendant leaf. Therefore
\[
\forall w\in A_v,\ z\in B_v,\quad
\exists k\in\Lambda(v): w_k\ne z_k.
\]
Equivalently, the projection sets \(A_v|_{\Lambda(v)}\) and \(B_v|_{\Lambda(v)}\) are disjoint. This is a necessary condition on every shared state, not merely on its currently reached input pairs. Scope: Sokolov Boolean games and rect-DAGs, where a node is valid on a full product rectangle and its children cover that rectangle. A more permissive model that requires correctness only on pairs actually reaching a state needs a separate analysis; the product-hull conclusion does not automatically apply there.

**Merge rule.** Suppose several transcript contexts \(C_i=A_i\times B_i\) are merged into \(v\), so each \(C_i\subseteq R_v\). Then the rectangle \(R_v\) contains the product hull
\[
\left(\bigcup_i A_i\right)\times\left(\bigcup_i B_i\right),
\]
including every cross-pair \(A_i\times B_j\), not just the original contexts \(A_i\times B_i\). The descendant outputs must solve all those cross-pairs as well. Thus histories can be merged only when their product hull remains solvable by the shared suffix.

**Universal prefix scan falsification.** After a sequential scan has found equality on a prefix \(P\), each exact common prefix \(p\) gives context
\[
C_p=\{w:w|_P=p\}\times\{z:z|_P=p\}.
\]
Merging distinct \(p,p'\) into a single suffix-only state adds cross-pairs with \(w|_P=p\), \(z|_P=p'\). Such pairs can agree on every suffix coordinate. A continuation whose only outputs are suffix coordinates then has no valid answer on the enlarged rectangle. So the familiar Ã¢â‚¬Å“forget the equal prefix and scan the suffixÃ¢â‚¬Â optimization is not a rect-DAG unless the state retains enough prefix information or its descendants can also resolve these cross-pairs. This proves failure of that proposed universal router. It does not prove all descriptions or all histories require separate states: on the Gap-MCSP promise, existence of a high/low cross-pair with the required common suffix must be established for each proposed merge, and a router may revisit prefix coordinates.

**Application to the fusion machine.** Build the proof-support digraph with a transition arc \(i\to j\) whenever \(T_j\subseteq E_i\) or \(T_j\subseteq H_i\), and place a signed output \((k,b)\) at state \(i\) whenever the corresponding literal slice \(L_{k,b}\) is contained in one of its sides. Let \(\Lambda_i\) be the coordinates on outputs reachable from i in this finite digraph. If \(x_i(w)=1\) and \(x_i(z)=0\), choose a side of \(i\) unsupported at \(z\). A support for that side at \(w\) is either a literal mismatch or a predecessor state \(j\) active at \(w\), inactive at \(z\), with strictly smaller first-activation rank on \(w\). Following these supports terminates at a mismatch output. Hence
\[
A_i|_{\Lambda_i}\cap B_i|_{\Lambda_i}=\varnothing,\quad
A_i=\{w:x_i(w)=1\},\quad B_i=\{z:x_i(z)=0\}.
\]
This is a per-state projection-separation certificate for the cyclic machine. It records exactly what its static support graph guarantees. It does not bound \(|\Lambda_i|\), the number of states, or the number of output choices, so it is not yet a non-shareability lower bound.

**Quantitative placement.** The exact q-state object remains cyclic and rank-terminating. With explicit binary support selectors, the direct acyclic unfolding may charge support routing at every rank layer; the established safe bounds remain \(D_\cap\le q^2\) when only AND gates are counted and rect-DAG/circuit size \(O(q^3)\) under the present binary simulation and \(q\ge N-o(N)\). A rect-DAG lower bound \(L\) therefore yields only \(q=\Omega(L^{1/3})\) through that simulation; an AND-only separator lower bound \(A\) yields \(q=\Omega(\sqrt A)\). The reverse active-promise transformation is still \(\rho_{\rm prom}\le O(L)\), which means a small rect-DAG would imply a small cover, but a lower bound on L alone does not reverse into a lower bound on \(\rho\).

**Literature-definition check.** Sokolov's Boolean communication game assigns each vertex a product rectangle of valid pairs; the root rectangle is \(Y\times Z\), and child rectangles cover every pair valid at the parent. This is why merging transcript histories incurs the product-hull obligation. GGKS rectangle-DAGs are the acyclic shared-state model tied to monotone circuit size for the full monotone KW relation. CavalarÃ¢â‚¬â€œOliveira's exact fusion identity is instead cyclic discrete/conjunctive complexity; NakayamaÃ¢â‚¬â€œMaruoka is its methodological ancestor, not an identity for this semi-filter promise. The checked primary definitions support, rather than remove, the cyclic-versus-acyclic distinction.

**Status.** C-110 is a proved structural condition and kills the specific prefix-forgetting scan. No new lower bound on q, \(\rho_{\rm prom}\), or the C-75 rect-DAG follows. The next useful step is to quantify how many cross-pair obligations a candidate family of circuit-description contexts creates, while using actual Gap-MCSP high/low tables rather than the full-cube counterexample alone.

## 41. C-111 - Actual Gap-MCSP cross-pairs defeat a prefix-first suffix router

C-110's product-hull condition can be instantiated inside the actual low/high promise, not just on arbitrary unequal strings. This yields a strong obstruction for one natural description-space router, while C-80 shows why it is not a lower bound against all DAGs.

Assume a fixed \(0<\beta<1/2\), \(s_1=N^\beta/(cn)\), \(s_2=N^\beta\). Use the C-80 partition of the \(N\) truth-table coordinates into \(m=2^k\in[s_1/16,s_1/8]\) blocks, indexed by \(u\in\{0,1\}^k\), each of size \(B=N/m\). Every block-constant table
\[
w_a(u,v)=a_u,\qquad a\in\{0,1\}^m,\ v\in\{0,1\}^{n-k},
\]
has circuit size at most \(s_1\), by the shared prefix decoder from C-80.

There is a Boolean mask \(p:\{0,1\}^{n-k}\to\{0,1\}\) such that both \(p\) and \(\neg p\) have circuit complexity greater than \(s_2+Ck\), for any fixed basis constant C needed below. Indeed, the number of functions on \(n-k\) inputs with circuits of size at most \(s_2+Ck\) is at most
\[
2^{O((s_2+k)\log(n+s_2))}=2^{O(N^\beta n)},
\]
whereas all such functions number \(2^B\), and
\[
B=\Theta(nN^{1-\beta})\gg N^\beta n
\]
for \(\beta<1/2\). Excluding both the low-complexity masks and their complements still leaves a mask. This counting uses the same circuit-size convention as the project.

Let \(P=\{(u,v):p(v)=1\}\) be a set of truth-table coordinates and \(J=[N]\setminus P\). For any two codewords \(a,b\in\{0,1\}^m\), define the splice
\[
z_{a,b}(u,v)=
\begin{cases}
b_u,&p(v)=1,\\
a_u,&p(v)=0.
\end{cases}
\]
If \(a\ne b\), choose a block u on which they differ. Restricting \(z_{a,b}\) to that block gives either p or \(\neg p\). A circuit for \(z_{a,b}\) of size at most \(s_2\), with the first k input bits fixed to u, would give a circuit for p or its complement of size at most \(s_2+O(k)\), a contradiction. Hence every off-diagonal splice \(z_{a,b}\) is in \(Z\). Meanwhile \(w_a|_J=z_{a,b}|_J\), and \(z_{a,b}|_P=w_b|_P\). Since p is nonempty, the restrictions \(w_a|_P\) distinguish all \(2^m\) codewords.

Define nonempty prefix contexts
\[
A_a=Y\cap\{w:w|_P=w_a|_P\},\qquad
B_a=Z\cap\{z:z|_P=w_a|_P\},\qquad C_a=A_a\times B_a.
\]
Here \(w_a\in A_a\), and \(B_a\ne\varnothing\) because for any cÃ¢â€°Â a, \(z_{c,a}\in B_a\). For every distinct a,b, the cross-pair
\[
(w_a,z_{a,b})\in A_a\times B_b
\]
is low/high but agrees on every coordinate in J. Therefore no rect-DAG node whose entire descendant output set is confined to J can contain both contexts \(C_a\) and \(C_b\): its product rectangle would include this cross-pair, which has no valid J-coordinate mismatch. In the submodel that first identifies the exact P-pattern and then uses a suffix-only continuation, all \(2^m=2^{\Theta(s_1)}\) contexts require distinct continuation states.

**Why this does not lower-bound the general DAG.** C-80 gives an O(N)-vertex DAG for this same block-constant low family against all high z: Bob finds a mixed block, then Alice gives its constant bit and Bob finds an opposite coordinate. The router avoids recording the full P-pattern and uses the common block partition instead. Thus C-111 kills the prefix-first/suffix-only architecture on genuine Gap-MCSP inputs, but it also exhibits the kind of adaptive structural shortcut a global lower bound must rule out. It says nothing about a DAG for all low circuits, and it transfers no lower bound to q or \(\rho\).

**Status.** This is a proved Tier-3 non-shareability theorem for a specified router family. The general task is now sharper: either find an adaptive common-partition analogue for arbitrary small circuit descriptions, or prove that descriptions with incompatible cofactor partitions force many states even when the DAG can search adaptively.

## 42. C-112 - Distance-code splice lemma sharpens the promise-level obstruction

C-111's special within-block high mask can be replaced by a general counting lemma.

**Splice lemma.** Let \(\mathcal C\subseteq\{0,1\}^N\) have size K and minimum Hamming distance d, and let \(M_2=|\mathrm{SIZE}(s_2)|\). If
\[
d>2\log_2 K+\log_2 M_2,
\]
then there is one coordinate split \([N]=P\sqcup J\) such that every ordered off-diagonal splice
\[
z^P_{a,b}(i)=
\begin{cases}
b_i,&i\in P,\\
a_i,&i\in J
\end{cases}
\qquad(a,b\in\mathcal C,\ a\ne b)
\]
lies outside \(\mathrm{SIZE}(s_2)\).

**Proof.** Choose P uniformly among all subsets of [N]. For fixed ordered aÃ¢â€°Â b, let D={i:a_iÃ¢â€°Â b_i}; |D|Ã¢â€°Â¥d. The restriction \(P\cap D\) is uniform among the \(2^{|D|}\) subsets of D, and each such choice gives a distinct splice, while all coordinates outside D stay fixed. At most \(M_2\) of those splices have circuit size at most \(s_2\), so
\[
\Pr[z^P_{a,b}\in\mathrm{SIZE}(s_2)]\le M_2 2^{-d}.
\]
A union bound over fewer than \(K^2\) ordered pairs gives failure probability at most \(K^2M_2 2^{-d}<1\). Hence a split P exists for which every off-diagonal splice is high. \(\square\)

**Application to low circuits.** Take the C-80 block-constant family with m=Theta(s1) blocks and choose an error-correcting subcode \(\mathcal C\subseteq\{0,1\}^m\) of size \(K=2^{\Omega(m)}\) and relative distance at least a fixed \(\delta>0\). Such a code follows by greedy Hamming packing. Its block-constant truth tables all lie in Y and have minimum distance \(d\ge\delta N\). For every fixed \(\beta<1\),
\[
\log M_2=O(s_2\log(n+s_2))=O(N^\beta n)=o(N),\qquad
\log K\le m=O(s_1)=o(N).
\]
Thus \(d>2\log K+\log M_2\) for sufficiently large N, and C-112 supplies a split P for which all distinct-codeword splices are high. This strengthens C-111 from beta<1/2 to every fixed beta<1 without requiring a hard cofactor mask.

For each aÃ¢â€°Â b, highness of the splice implies that P intersects the disagreement set of a,b and J also intersects it; otherwise the splice would equal one of the low endpoints. Therefore the P-patterns \(w_a|_P\) distinguish the K low codewords. Define prefix rectangles \(C_a=A_a\times B_a\) as in C-111. The splice \(z^P_{a,b}\) lies in the high-column context B_b and agrees with w_a throughout J. Consequently a rect-DAG node with descendant outputs restricted to J cannot serve both C_a and C_b. Any router that first identifies the exact P-pattern and then uses a J-only continuation needs at least \(K=2^{\Omega(s_1)}\) continuation states.

**Limit and interpretation.** This is still a submodel theorem, not a lower bound for all rect-DAGs. The C-80 mixed-block search gives an O(N) DAG for the entire block-constant family and bypasses exact P-pattern storage. The result proves that every sufficiently separated low code has a split making all its cross-splices high, so a prefix-first suffix-only router is intrinsically incompatible with those rows; an adaptive router can evade that architecture. No q or \(\rho\) lower bound follows.

## 43. C-113 - Varying support sets still admit a near-linear adaptive DAG

C-80 handles block-constant rows sharing one partition. A wider subfamily allows the low row's relevant-variable set to vary over \(\binom nk\) choices and still has a small shared rect-DAG.

Let \(Y_k\) be the class of Boolean functions on n input variables whose essential-variable set has size at most k. Choose k so every k-variable Boolean function has a DNF circuit of size at most \(s_1\), for example \(C_{\rm DNF}k2^k\le s_1<s_2\). Thus \(Y_k\subseteq Y\). For \(w\in Y_k\), Alice selects any k-element set \(S_w\) containing \(\operatorname{Ess}(w)\). For \(z\in Z\), let \(T_z=\operatorname{Ess}(z)\). Every function depending on at most k variables has circuit size at most \(s_1\), so \(|T_z|\ge k+1\). Therefore
\[
A_w=[n]\setminus S_w,\quad B_z=T_z,\qquad
|A_w|+|B_z|\ge(n-k)+(k+1)=n+1.
\]
Hence \(A_w\cap B_z\ne\varnothing\). A direction \(i\) in the intersection is irrelevant to w and essential to z.

**Small rect-DAG for finding i.** Use a balanced binary decomposition tree of the direction set [n]. At each interval I, make a state \(q(I,a,b)\) for count pairs \(a=|A_w\cap I|\), \(b=|B_z\cap I|\) satisfying \(a+b>|I|\). Each state is a rectangle: Alice's side fixes her count to a, and Bob's side fixes his count to b. There are at most
\[
\sum_{I}(|I|+1)^2=O(n^2)
\]
such states over the balanced interval tree. Add a universal root. At the root, Bob communicates \(|B_z|\) and the path enters \(q([n],n-k,|B_z|)\). At \(q(I,a,b)\), the parties communicate the two counts in one child interval \(I_L\). If their sum exceeds \(|I_L|\), move to \(q(I_L,a_L,b_L)\); otherwise the other child must have count sum greater than its size and the protocol moves there. Interval size strictly decreases, so this is an acyclic PLS game with \(L=O(n^2)\) states and \(t=O(\log n)\) communication per transition. Sokolov's PLS-to-Boolean-game conversion gives a rect-DAG of size at most \(L2^{3t}=n^{O(1)}\) for the relation outputting an i in \(A_w\cap T_z\).

**Turn the direction into a mismatch.** For each output direction i, append a Bob-controlled binary tree with one leaf for each hypercube edge \((x,x\oplus e_i)\). Since \(i\in\operatorname{Ess}(z)\), Bob can choose an edge on which z changes. These trees use \(O(N)\) vertices per direction, or \(O(nN)\) total. For every input pair routed to direction i, Alice's low table is invariant under flipping i, while Bob's high table changes. At the chosen edge, Alice sends the common bit \(w(x)=w(x\oplus e_i)\); Bob then selects the endpoint whose z-bit is opposite and the terminal label is that truth-table coordinate. This final selector needs constant size per edge. The result is a rect-DAG for signed mismatch on \(Y_k\times Z\) of size
\[
O(nN+n^{O(1)})=N\,\operatorname{polylog}N.
\]

**What this falsifies and what it leaves.** Many different relevant-variable sets do not by themselves cause DAG hardness: the entire k-junta family, with up to \(\binom nk\) support choices, has a near-linear shared router. The construction exploits the fact that every high table has more than k essential variables and that a direction outside the low support yields a connected one-dimensional fiber edge. It does not cover low circuits with more than k essential variables, and its restricted-domain DAG gives no upper bound on the fusion cover for all Y. It directs O-99 toward low circuits whose hardness is not captured by essential-variable count.
## 44. C-114 - Count-intersection PLS template and audit of C-113

The C-113 count search extends to any pair of input-indexed set systems. Let Alice's input \(x\) specify \(A_x\subseteq[n]\), Bob's input \(y\) specify \(B_y\subseteq[n]\), and assume
\[
|A_x|+|B_y|>n\qquad\text{for every }(x,y).
\]
Then \(A_x\cap B_y\ne\varnothing\). The search relation returning any \(i\in A_x\cap B_y\) has an acyclic communication PLS with \(O(n^2)\) states and \(O(\log n)\) communication for membership/successor computation.

**Construction.** Take a balanced binary interval tree over \([n]\). Include a universal root and, for each interval \(I\), a state \(q(I,a,b)\) for counts \(a=|A_x\cap I|\), \(b=|B_y\cap I|\) satisfying \(a+b>|I|\). The root's successor records the two total counts. At \(q(I,a,b)\), the parties exchange the two counts in one child. If their sum exceeds that child's length, descend there; otherwise the other child satisfies the strict inequality because the parent does. At a singleton, both counts equal one and its index is a valid output. Every transition strictly decreases interval size. The state count is at most \(1+\sum_I(|I|+1)^2=O(n^2)\), since intervals at depth d have size about \(n/2^d\). Each membership/successor computation uses a constant number of counts of \(O(\log n)\) bits.

Sokolov's PLS-to-Boolean-game theorem converts a PLS with \(L\) states and communication \(t\) into a Boolean communication game with at most \(L2^{3t}\) vertices. Thus the intersection relation has a rect-DAG of \(n^{O(1)}\) vertices. For C-113, \(A_w=[n]\setminus S_w\), where \(S_w\) is a k-set containing the essential variables of w, and \(B_z=\operatorname{Ess}(z)\). The size condition is \((n-k)+(k+1)>n\).

**Suffix composition detail.** For each direction i, let \(A_i\) be all low rows invariant under flipping input variable i, and \(B_i\) all high columns that depend on i. On the entire rectangle \(A_i\times B_i\), Bob can choose a hypercube edge on which z changes; Alice supplies the common w-bit, and Bob outputs the endpoint with the opposite z-bit. This selector uses \(O(N)\) vertices. The direction game may have multiple output leaves for i, but they can all point to this one selector: its rectangle \(A_i\times B_i\) is a valid superset of each leaf rectangle. Boolean-game children need only cover the parent rectangle; they need not be subsets. Hence the total is \(O(nN+n^{O(1)})=N\,\mathrm{polylog}(N)\), with no unproved merging of incompatible rectangles.

**Limit for full Gap-MCSP.** The cardinality-intersection certificate does not extend to all low circuits by taking irrelevant variables as \(A_w\). Parity on n inputs has a size-\(O(n)\) circuit (hence is low in the project regime) and makes every input variable essential, so \(A_w=\varnothing\); even a high table has at most n essential variables, and the strict sum condition fails. This kills only this support-cardinality witness, not other adaptive or cyclic-state approaches. C-113 remains a restricted-domain upper bound and yields no bound on \(\rho_{\rm prom}\).

## 45. C-115 - Low-circuit gate signatures force high-table variation

This gives a circuit-internal analogue of the k-junta irrelevant-direction witness, while exposing a quantitative routing obstacle.

Let \(C\) be a circuit of size at most \(s_1\) computing a low row \(w\). Choose \(k\) wire values, including the output wire (input wires may pad the selection if needed), where
\[
k=\left\lfloor\log_2\!\left(\frac{s_2}{16C_0\log_2 s_2}\right)\right\rfloor
\]
and \(C_0\) is a basis-dependent constant large enough for a k-input lookup circuit. In the project regime \(s_1=o(s_2)\), \(k=\Theta(\log s_2)=\Theta(n)\), with \(k<n\) for each fixed \(\beta<1\). The selection can include input wires if the circuit has too few internal wires. Let \(\sigma(x)\in\{0,1\}^k\) be their joint values on assignment \(x\in\{0,1\}^n\); these values partition the N assignments into at most \(2^k\) signature cells.

If \(z\) were constant on every signature cell, then \(z=\phi\circ\sigma\) for some Boolean \(\phi\). The original circuit C computes the selected wires, and a DNF lookup for \(\phi\) costs \(O(k2^k)\). By the choice of k, \(s_1+O(k2^k)<s_2\) for sufficiently large n, contradicting \(z\in Z\). Therefore some signature cell contains \(x,y\) with \(\sigma(x)=\sigma(y)\) and \(z(x)\ne z(y)\). Since the output wire is among the selected wires, \(w(x)=w(y)\): this is a total gate-signature fiber-disagreement relation on \(Y\times Z\).

There is also a quantitative version. The majority value of z on each signature cell defines a function \(h=\psi\circ\sigma\) of circuit size at most \(s_1+O(k2^k)\le s_2/8\). If z differed from h on fewer than \(c s_2/n\) input points, one could correct those points by OR-ing that many n-literal minterms onto h, obtaining a circuit for z of size below \(s_2\). Thus the sum, over signature cells, of the minority counts \(\min(|F_{a,0}|,|F_{a,1}|)\) is \(\Omega(s_2/n)\). In particular there are at least \(\Omega(s_2/n)\) ordered within-cell pairs on which z differs.

**Why this is not yet a shared-DAG result.** Let \(A_C=\{(x,y):\sigma(x)=\sigma(y)\}\), Alice's candidate set, and \(B_z=\{(x,y):z(x)\ne z(y)\}\), Bob's local disagreement set. Their intersection consists of the valid signature-fiber outputs and has size at least \(\Omega(s_2/n)\); also \(|A_C|\ge N^2/2^k\). These bounds do not imply \(|A_C|+|B_z|>N^2\) on the fixed universe \([N]^2\), so the C-114 cardinality PLS does not apply. This failure can occur: for the constant low row, select k-1 input wires plus its output, so \(|A_C|=N^2/2^{k-1}=o(N^2)\). Circuit counting gives a high z of weight \(r=K s_2=o(N)\) for a sufficiently large fixed K (the number of weight-r tables exceeds \(|\mathrm{SIZE}(s_2)|\)); then \(|B_z|=2r(N-r)=o(N^2)\). The cells also vary with C. A protocol that sends C lets Bob search them, but C-97 shows that this short description does not reduce the minimum shared rect-DAG size. The lemma identifies a guaranteed witness and a mass floor, not a lower bound on routing or on q. C-80 remains the falsification check: a fixed block partition can still admit an O(N) adaptive mismatch DAG.

## 46. C-116 - Fixed-cofactor fragmentation preserves a hard subproblem but spends the gap

Write \(S_d(a,b)\) for the rect-DAG size of signed mismatch on \(d\)-variable truth tables with Alice in \(\mathrm{SIZE}_d(a)\) and Bob of circuit complexity \(>b\). Put \(s_2=cns_1\), as in the project parameterization. Choose \(m=2^k=\Theta(n)\), with the constant small enough that \(C_{\rm mux}\,4m s_1<s_2/2\); then \(k=\Theta(\log n)\).

For \(z:\{0,1\}^n\to\{0,1\}\), let \(z_u\) be its restriction to the prefix subcube \(x_{[k]}=u\). If every cofactor had circuit size at most \(4s_1\), a circuit could compute all \(z_u\)'s and mux them using the k-bit prefix, at total size at most
\[
C_{\rm mux}\,4m s_1+O(mk)<s_2
\]
for sufficiently large n. The selector overhead is \(o(s_2)\). This contradicts \(z\in Z\). Thus every high z has a prefix u with \(\mathrm{CC}_{n-k}(z_u)>4s_1\), while every low w has \(\mathrm{CC}_{n-k}(w_u)\le s_1\).

Bob can choose the first such u by unrestricted local computation and route into the corresponding cofactor search. Lifting a rect-DAG for the smaller promise through the restriction maps gives the upper-bound reduction
\[
S_n(s_1,s_2)\ \le\ O\!\left(m\,S_{n-k}(s_1,4s_1)+m\right).
\]
The branch rectangles are \(Y\times Z_u\), where Bob's canonical choice is u; each subgame tests only the corresponding restrictions. This is a valid adaptive shared-DAG construction conditional on the smaller constant-factor-gap DAG.

**Why it does not prove a lower bound.** The implication is in the upper-bound direction: a small constant-gap subproblem yields a small large-gap DAG. It does not turn a lower bound on \(S_{n-k}(s_1,4s_1)\) into one on \(S_n(s_1,s_2)\). The obvious reverse embedding adds a hard marker cofactor to force the full table above \(s_2\), but then every low row disagrees on that marker region, so a mismatch DAG may answer there and ignore the encoded cofactor instance. Matching the marker would make the low row itself high. A reverse reduction needs a different way to amplify cofactor complexity without adding an easy mismatch region. This is a concrete failure mode for cofactor-based transfer, not a no-go theorem.

## 47. C-117 - Same-threshold padding transfers DAG lower bounds exactly

For \(k\le n\), lift a Boolean function \(f\) on \(n-k\) variables to \(\widehat f(x_1,\ldots,x_n)=f(x_{k+1},\ldots,x_n)\). Circuit complexity is unchanged: an \((n-k)\)-input circuit can ignore the first k inputs, and any n-input circuit for \(\widehat f\) restricts to an \((n-k)\)-input circuit by fixing them.

Restrict an n-variable mismatch rect-DAG to lifted low and high tables. Every node rectangle remains a rectangle after intersecting both sides with the lift image. A terminal label \((u,v)\) is relabelled by suffix \(v\), since both lifted tables repeat that truth-table bit for all prefixes u. Therefore, with the same absolute thresholds \(a,b\),
\[
S_{n-k}(a,b)\le S_n(a,b)
\]
with no graph-size loss.

For the OPS parameterization \(s_2=2^{\beta n}\), \(s_1=s_2/(cn)\), the smaller \(n'=n-k\) instance has exactly the same thresholds when re-expressed using
\[
\beta'=\frac{\beta n}{n'},\qquad c'=\frac{cn}{n'}.
\]
If \(k=O(\log n)\), then \(\beta'=\beta+O(\log n/n)\) and \(c'=c+O(\log n/n)\). Alternatively, for a fixed \(\beta'>\beta\), take \(n'=(\beta/\beta')n\) (rounded); then \(N'=N^{\beta/\beta'}\) and \(c'=c\beta'/\beta\). A lower bound \(S_{n'}>N'^\gamma\) transfers to \(S_n>N^{(\beta/\beta')\gamma}\). This can transfer a result with exponent margin, but only if the lower-bound theorem is available at the transformed parameters. It says nothing about the weaker \(4s_1\) cofactors from C-116.

## 48. C-118 - Fusion-cover monotonicity under ignored-input padding

Let \(n'=n-k\) and lift an \(n'\)-variable truth table to an n-variable table by ignoring the first k input bits. Circuit complexity is unchanged, so the lifted low and high classes are subfamilies \(Y^\iota\subseteq Y_n\), \(Z^\iota\subseteq Z_n\).

A big-promise pair list \(Q=((E_i,H_i))\), with endpoints in \(\mathcal P(Z_n)\), restricts to \(Q'=((E_i\cap Z^\iota,H_i\cap Z^\iota))\). We claim that if Q covers the big promise, Q' covers the smaller one. Suppose not: some low \(w'\) and proper semi-filter \(\mathcal F'\subseteq\mathcal P(Z^\iota)\), containing every matching literal slice for \(\iota(w')\), are preserved by all pairs in Q'. Pull it back by the meet map
\[
\widehat{\mathcal F}=\{A\subseteq Z_n:A\cap Z^\iota\in\mathcal F'\}.
\]
This is a nonempty proper upward-closed family: intersection with \(Z^\iota\) preserves inclusion and pairwise intersection, \(Z_n\cap Z^\iota=Z^\iota\in\mathcal F'\), and \(\varnothing\notin\mathcal F'\). Every full matching literal slice for \(\iota(w')\) restricts to the corresponding smaller slice, so \(\widehat{\mathcal F}\) is above the lifted low anchor. Preservation of each restricted pair implies preservation of the original pair, because
\[
(E_i\cap H_i)\cap Z^\iota=(E_i\cap Z^\iota)\cap(H_i\cap Z^\iota).
\]
This contradicts that Q covers the big promise. Thus
\[
\rho_{\rm prom}(n-k;s_1,s_2)\le \rho_{\rm prom}(n;s_1,s_2)
\]
with no size loss. This is a direct filter pullback and does not pass through a rect-DAG.

For the OPS thresholds, reparameterize the smaller instance by \(\beta'=\beta n/(n-k)\), \(c'=cn/(n-k)\); it has exactly the same absolute \(s_1,s_2\). A lower bound \(\rho_{\rm prom}(n-k)> (2^{n-k})^{1+\epsilon'}\) therefore implies the big-instance bound \(>N^{(1-k/n)(1+\epsilon')}\). To reach \(N^{1+\epsilon}\), require \((1-k/n)(1+\epsilon')>1+\epsilon\), and verify the theorem uniformly at the shifted \(\beta',c'\). This preserves the direct cyclic-cover scale; the cubic q-to-rect-DAG loss is not incurred.

## 49. C-119 - Padding quantifiers, endpoint admissibility, and the OPS threshold

Write R_n(beta,c) for the active promise cover number on n-input truth tables with s2=2^(beta n), s1=2^(beta n)/(c n), and high universe Z_n={z: CC(z)>s2}. The exact C-118 statement is at identical absolute thresholds: R_{n'}(s1,s2) <= R_n(s1,s2), for n'<n.

**Exact rational parameter transport.** Let lambda=p/q>1 be fixed in lowest terms and compare dimensions n=pt and n'=qt. Put beta'=lambda beta, c'=lambda c. Then 2^(beta' n')=2^(beta n), and 2^(beta' n')/(c'n')=2^(beta n)/(cn), so C-118 gives the exact relation R_qt(beta',c') <= R_pt(beta,c). If R_qt(beta',c')>(2^(qt))^(1+eta) on the compared dimensions, then R_pt(beta,c)>(2^(pt))^((1+eta)/lambda). A target exponent 1+epsilon requires eta>lambda(1+epsilon)-1. For the OPS constant c0, this uses source constant c'=lambda c0. If the source lower bound holds for every sufficiently small fixed beta' at that one fixed c', the map beta=beta'/lambda covers every sufficiently small fixed target beta. When only infinitely-often source hardness is known, the exact rational map requires it on the subsequence n'=qt; an all-large-n source bound suffices automatically.

**Quantifier audit.** This is a correct conditional transport, not a way to infer the required bound from one fixed beta': one source value maps to only one target value for fixed lambda. To satisfy Theorem 1.4's universal small-beta premise, one still needs a lower-bound theorem uniform over an interval of fixed beta' with one common exponent eta, plus the exponent margin above. Moreover, because c'>c0 makes the low class smaller, a lower bound at (beta',c') already implies the corresponding separator/cover lower bound at (beta',c0) by monotonicity in the low anchor set. Therefore padding does not improve the magnification quantifier or exponent when this whole parameter family is available; its value is the exact no-DAG-loss comparison at fixed absolute thresholds. A single parameter point cannot be promoted to the OPS premise by padding.

**Rounding caveat.** For a general real lambda, choosing n'=floor(n/lambda) gives only bounded-factor changes in the thresholds when parameters are re-expressed using fixed beta',c'. Such changes are not automatically harmless for Gap-MCSP; no constant-factor robustness theorem is used here. The exact statement above avoids this by using dimensions pt,qt. The standard non-membership premise is only an infinitely-often lower bound, so rational-subsequence transport must track where those hard arities occur.

**Endpoint audit.** In the source cover definition, the pair universe is all (E,H) with E,H subseteq U; empty endpoints are permitted. Restricting a big pair to Z^iota can therefore be used directly. If one adopts a variant forbidding empty endpoints, any restricted pair with E intersect Z^iota empty or H intersect Z^iota empty is preserved vacuously by every proper semi-filter (which excludes empty); delete it. Duplicate restricted pairs can also be deleted. These operations only decrease list size, so the C-118 inequality remains valid under that variant.

**Status.** C-118 is sound for the project model, including the endpoint edge case. O-104's parameter audit is resolved: padding is a valid transfer lemma with exact arithmetic and explicit exponent/quantifier conditions, but it yields no lower bound and cannot replace the OPS all-small-fixed-beta hypothesis. The open task remains the direct superlinear lower bound, not parameter bookkeeping.

## 50. C-120 - High-table mismatch can be concentrated in one gate-signature cell

This makes the limitation in C-115 quantitative. Let a low table w be computed by a circuit C of size at most s1. Select k= floor((1/2)log2(s2)) wire values, including C's output, and let sigma_C map each truth-table input x to the k-bit signature of those wires. There are at most 2^k cells. Let F be a largest cell, so |F|>=N/2^k=Omega(N/sqrt(s2)). The output wire is in the signature, hence w is constant on F.

Consider every completion z that agrees with w outside F and is arbitrary on F; there are 2^|F| such tables. Only two completions are constant on F. Each has circuit size at most s1+O(k): evaluate C, test whether its k selected wires equal the fixed signature of F, and override the output by a constant on that cell. Circuit counting gives |SIZE(s2)| <= 2^{O(s2 log(n+s2))}. For every fixed beta<2/3, and in particular throughout the sufficiently-small-beta OPS regime,
\[
|F|=Omega(N^{1-beta/2}) >> s2 log(n+s2)=O(N^beta n).
\]
Thus 2^|F|-2>|SIZE(s2)| for large n. At least one completion z is outside SIZE(s2), and because the two constant completions are low, this high z is nonconstant on F. It agrees with w everywhere outside F. Therefore every mismatch between this low/high pair lies in the single signature cell F.

The C-49 patching bound further implies that z differs from w on Omega(s2/n) points: otherwise those exceptional values could be hardwired into C with fewer than s2 gates. So the concentration is compatible with the full robust disagreement mass from C-115; the mass need not spread over many cells.

**Consequence.** Any argument that strengthens C-115 by claiming many signature cells are mixed, or whose lower-bound charge is the number of mixed cells, is false in this parameter range. This does not refute every count-state router: a valid count-intersection PLS would still need Alice- and Bob-local witness sets, while the mixed-cell set is indexed by a partition chosen from Alice's circuit. No compact shared encoding of that cell is known. The live issue is to lower-bound the cost of finding the one varying cell across circuit-dependent partitions, or to construct a compact adaptive router. C-120 supplies no q, rect-DAG, or P-vs-NP lower bound.

**Source/definition check for C-119.** OPS Theorem 1.4 states its circuit lower-bound premise for every sufficiently small fixed beta at a universal constant c ([primary paper](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf)). Cavalar-Oliveira's Definition 21 and cover graph take the pair universe to be all (E,H) with E,H subsets of U, including empty endpoints ([primary report](https://eccc.weizmann.ac.il/report/2025/033/download)).

## 51. C-121 - A common cheap partition gives a linear DAG, and full SIZE(s1) has no such partition

Let Pi={C_1,...,C_m} be a fixed partition of the N truth-table coordinates. Assume every low row w in Y is constant on each cell. Also assume the partition label pi(x) is computable by a t-gate circuit and t+O(m)<s2. Any table constant on every cell equals h(pi(x)) for some Boolean lookup h on at most m labels; h has a fan-in-two implementation of O(m) gates. Hence every such table has circuit size below s2, so every z in Z is mixed on at least one cell.

This gives a standard rect-DAG of O(N+m)=O(N) vertices for Mis_{Y,Z}. Bob first selects a mixed cell j using a binary tree whose local tests are whether z is mixed in a subset of cells; the high-side sets of the two children cover the parent. Alice then reveals the common row bit b on C_j. Bob scans the coordinates of C_j for one with z(x)=1-b. Since the cell is mixed, the scan terminates, and the leaf outputs the signed mismatch (x,b). The per-cell scans have total size O(sum_j |C_j|)=O(N); the mixed-cell selector has O(m) states. This generalizes C-80 and is a valid universal router whenever the low family shares a partition whose cell-constant tables all remain below s2.

For the full class Y=SIZE(s1), every point indicator delta_a(x)=[x=a] lies in Y for sufficiently large n, since it has O(n) gates and s1>>n. If two distinct coordinates a,b belonged to one cell of a partition respected by every low row, delta_a would not be constant on that cell. Therefore every common partition for all of Y must be the discrete N-cell partition. On singleton cells every truth table is cell-constant, so the cheap-partition hypothesis t+O(m)<s2 fails for beta<1. Thus the C-80 escape cannot extend to the full low class through one fixed useful partition.

**Learning.** C-120 shows a hard pair can hide all mismatch inside one cell of a row's selected partition. C-121 shows that if the partition is shared across the row family, Bob can search for a mixed cell in O(N) states; but the full low class has no common coarse partition. The remaining target is to quantify the cost of adaptive reuse across row-dependent partitions. This is not a lower bound against arbitrary DAGs and does not imply a lower bound on rho.

## 52. C-122 - Any O(n)-sized low-anchor family has a linear shared router

Fix beta>0 and let s1=2^(beta n)/(cn), s2=2^(beta n). Choose a constant eta>0 with eta<beta and eta/c<1/3, and let A={w_1,...,w_r} be any fixed family of r<=eta n low tables. Define the joint output signature W(x)=(w_1(x),...,w_r(x)); its fibers form a partition with at most 2^r cells, and every row in A is constant on each cell.

If a high table z were constant on every W-fiber, then z=h(W) for a Boolean lookup h on r bits. Evaluating all r low circuits and then h costs at most
\[
r s_1+O(r2^r)\le (\eta/c+o(1))s_2<s_2,
\]
where eta<beta makes r2^r=o(s2). This contradicts CC(z)>s2. Hence every z in Z is mixed on some common W-fiber. The C-121 mixed-cell router applies: Bob selects a mixed fiber, Alice reveals w's bit there, and Bob finds a point with the opposite z-bit. Its size is O(N+2^r)=O(N), since eta<beta<1.

Therefore for every fixed A of at most eta n low anchors,
\[
S_{\rm rect}(A,Z)=O(N).
\]
This upgrades C-109's common-fiber existence lemma to an explicit shared-DAG upper bound for the entire small row family. It also rules out fooling-family arguments that rely only on making O(n) selected low anchors demand incompatible common-fiber outputs.

**Limit.** The tuple A must be fixed for the suffix: rows outside A need not be constant on its joint-signature cells. Partitioning all of Y into groups of at most eta n rows and attaching one such router per group costs O(N ceil(|Y|/(eta n))), which is exponential at OPS parameters. Suffix reuse between different groups is unproved. Thus C-122 supplies a strong local upper bound and a precise small-family ceiling, not a global DAG or fusion-cover upper bound.
## 53. C-123 - Description inputs do not shrink the shared-DAG problem

This closes the strongest direct universal-DAG attempt based on Alice's short circuit description and states exactly what remains open.

Let D be the syntactic descriptions of circuits on n inputs of size at most s1, and let G(d) be the truth table computed by d. The descriptor search relation is
\[
\mathrm{Mis}_{D,Z}(d,z)=\{(k,b):G(d)_k=b,\ z_k=1-b\}.
\]
For any surjection G:D\to Y, its minimum Boolean rect-DAG size is exactly the table-domain size S_rect(Y,Z). One direction lifts each Alice predicate A_v\subseteq Y to G^{-1}(A_v) and leaves every Bob predicate and graph node unchanged. For the other, choose a section s:Y\to D and restrict each descriptor-side predicate to s(Y). Rectangle validity, child coverage, and output validity are preserved in both directions. Thus descriptions can reduce ordinary communication cost, but they cannot reduce the minimum graph size in this model.

The same rect-DAG size is, up to basis constants, the minimum Boolean circuit size C_sep(Y,Z) of a promise separator h:{0,1}^N\to{0,1} with h(y)=1 for every y\in Y and h(z)=0 for every z\in Z. A separator gives the Karchmer-Wigderson game for h, restricted to Y\times Z. Conversely, label a DAG leaf (k,b) by the literal t_k if b=1 and by its negation if b=0; recursively combine child separators by AND or OR according to which side of the parent rectangle is contained in both child sides. This is the standard rectangle-DAG-to-circuit construction. Consequently,
\[
S_{\rm rect}(Y,Z)=\Theta(C_{\rm sep}(Y,Z)).
\]
The circuit's values on the medium band are unrestricted. In particular, the target is a promise separator, not necessarily exact MCSP membership.

**Explicit universal baseline.** Encode each bounded-fanin circuit description using
\[
\ell=O(s_1\log(s_1+n))
\]
bits, so |D|\le 2^\ell. For each description d, the exact-table test E_d(t) is the conjunction of the N signed input literals specifying G(d). The OR H(t)=\bigvee_{d\in D}E_d(t) accepts exactly Y and has Boolean circuit size O(N2^\ell). Its Karchmer-Wigderson game is therefore a valid universal rect-DAG of size O(N2^\ell). Equivalently, Alice can send d and then the parties find a differing coordinate with O(\ell+\log N) communication, but the induced protocol tree can have 2^{O(\ell)}N nodes. Neither bound is near-linear in N at the project parameters.

**Why universal evaluation does not improve this.** A universal circuit U(d,x) computes G(d)_x efficiently for a supplied d. Membership of a table t in Y, however, is the projected condition
\[
t\in Y\quad\Longleftrightarrow\quad \exists d\in D\ \forall x\in\{0,1\}^n,\ t_x=U(d,x).
\]
The evaluator handles the inner test for one d; it does not implement the existential projection as a small circuit. Also, the joint predicate Ã¢â‚¬Å“there is a mismatch in coordinate interval IÃ¢â‚¬Â is not a rectangle in general (on rows 00,11 and columns 00,11 its matrix is 0 on the diagonal and 1 off-diagonal). So binary search with a universal evaluator does not define a shared rect-DAG. This is an obstruction to that construction, not a lower bound against all DAGs: a small separator could still compress the projection by an as-yet-unknown method.

**Exact quantitative bridge.** The saved compiler and reverse conversion give
\[
S_{\rm rect}=\Theta(C_{\rm sep}),\qquad
\rho_{\rm prom}\le O(S_{\rm rect}),\qquad
S_{\rm rect}\le O\!\left(\frac{\rho_{\rm prom}^3}{\log\rho_{\rm prom}}\right).
\]
Thus an N^{1+o(1)} universal DAG would force \rho_{\rm prom}=N^{1+o(1)} and kill every fixed positive-exponent lower-bound target. In the other direction, to infer \rho_{\rm prom}>N^{1+\epsilon} from an ordinary DAG lower bound using the current compiler requires S_rect=\omega(N^{3+3\epsilon}/\log N). The only lossless object found so far is the ranked cyclic closure itself: its q states can cycle, and its per-input activation rank decreases, whereas standard Sokolov PLS/Boolean games require an acyclic state graph.

**Literature cross-check.** Sokolov's Boolean communication game has a DAG of rectangles with root Y\times Z, child rectangles covering each parent, and valid output labels; its PLS model is acyclic and the PLS-to-game simulation costs L2^{3t} for L states and t communication bits. Garg-Goos-Kamath-Sokolov use rectangle-DAGs for search and recover monotone circuit size for the full monotone KW relation. Cavalar-Oliveira's Theorem 30 gives the exact identity \rho=D^\circ_\cap for least-fixed-point cyclic intersection complexity, while their generic acyclic AND-count unfolding costs up to q^2. These are complementary models, not a hidden identification of the ranked closure with an ordinary acyclic DAG. Primary texts: [Sokolov](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download), [Garg et al.](https://www.theoryofcomputing.org/articles/v016a013/v016a013.pdf), and [Cavalar-Oliveira](https://arxiv.org/abs/2503.14117).

**Status.** The short-description route is closed as a shortcut: descriptors preserve the exact minimum DAG size, and the best direct enumeration baseline is exponential in description length. The universal-DAG question itself remains open because C_sep(Y,Z) has neither a near-linear construction nor a superlinear lower bound here. This is Tier 5 clarification, not a P-vs-NP breakthrough.
## 54. C-124 - Recent implicit-MCSP and SoS results do not yet lower-bound the explicit DAG

Two nearby results were checked because they touch the description/proof-complexity bottleneck.

Goldberg, Juvekar, and Kabanets' June 2026 ECCC report proves conditional NP-hardness for a gap version of ImpMCSP under randomized polynomial-time half-Levin reductions, assuming subexponentially secure indistinguishability obfuscation and no infinitely-often subexponentially optimal propositional proof systems. An ImpMCSP input is a succinct sampler that enumerates labeled examples in a scrambled order with full support; it is not the explicit N-bit truth-table input to S_rect. A separator on explicit tables cannot be composed with that sampler at polynomial cost in general, because producing all N table bits from the sampler may itself require exponential work in the sampler's input length. The conditional hardness result therefore supplies no unconditional lower bound on S_rect or rho_prom.

Austrin-Risse prove strong SoS degree lower bounds for certifying that a fixed hard truth table has circuit complexity above s. That is a per-instance proof-degree statement. A rect-DAG lower bound requires a single circuit separator that works simultaneously on every table in Y and every table in Z. No reduction from the SoS degree lower bound to C_sep(Y,Z), S_rect, or the cyclic cover has been established here.

**Learning.** These results confirm that succinct representations and proof systems can expose genuine MCSP hardness, but they inhabit different input and resource models. A useful transfer must explicitly map sampler inputs or SoS refutations to the explicit promise separator while controlling the output size; no such map is known. Sources: [Goldberg-Juvekar-Kabanets, ECCC TR26-091](https://eccc.weizmann.ac.il/report/2026/091/download/), [Austrin-Risse, SoS Lower Bounds for MCSP](https://arxiv.org/abs/2311.12994).

## 55. C-125 - Direct cyclic lower-bound transfer and OR-only obstruction

This is an alternate way around the cyclic-to-acyclic loss in C-78/C-100. It does not construct a shared rect-DAG and has no Gap-MCSP instantiation yet; it gives a direct transfer criterion to the original pair count.

Let Y = SIZE(s1), Z = {0,1}^N minus SIZE(s2), and let e(t) in {0,1}^{2N} be the signed one-hot encoding, with e(t)_(k,b)=1 exactly when t_k=b. A successful q-pair cover yields a monotone cyclic separator H_Q with q AND gates under least-fixed-point semantics: H_Q(e(w))=1 for w in Y and H_Q(e(z))=0 for z in Z.

**Transfer lemma.** Let f:{0,1}^m -> {0,1} be monotone. Suppose an acyclic monotone map phi:{0,1}^m -> {0,1}^{2N} uses a AND gates and satisfies:

- If f(x)=1, there is w in Y with e(w) <= phi(x).
- If f(x)=0, there is z in Z with phi(x) <= e(z).

Then H_Q composed with phi computes f. Monotonicity gives the correct output in each case. Since phi is acyclic and independent of H_Q's state variables, composition preserves least-fixed-point semantics and adds only a AND gates. Hence CycAnd(f) <= q+a, or q >= CycAnd(f)-a. This bypasses the generic q-to-rect-DAG loss if a suitably cheap phi exists.

A sufficient NO condition is explicit: if phi(x) encodes a consistent partial table on each NO input and leaves d coordinates unset, then 2^d > |SIZE(s2)| guarantees a high completion z, so phi(x) <= e(z).

**OR-only stress test.** Suppose each output rail of phi is a constant or an OR of input variables, f(0)=0, f has a YES input, and every input of Hamming weight at most two is NO. The NO condition forbids both rails of a coordinate from being 1 together on a NO input. If both rails were nonzero ORs, turning on one variable from each support would activate both on a NO input of weight at most two; constants are ruled out by the zero- or one-variable NO inputs. Thus each coordinate has at most one globally active sign. Any YES input must contain a full low one-hot code, forcing the same sign at every coordinate; call the resulting low table w*. The conjunction of these N rail predicates accepts every YES input. It rejects every NO input, since e(w*) <= phi(x) <= e(z) would force w*=z, impossible for w* in Y and z in Z. Therefore f has an acyclic monotone circuit with at most N-1 AND gates. OR-only maps cannot transfer a cyclic AND lower bound greater than N.

For triangle on r-vertex graphs, every graph with at most two edges is NO. Cavalar-Oliveira state the known bound CycAnd(CLIQUE_3) = Omega(r^3/(log r)^4). Thus, whenever this exceeds N, the OR-only map is impossible. For the direct witness expansion, assign one fixed low table w0 to every candidate triangle. Compute each candidate triangle indicator with two AND gates, then OR these indicators into the rails of e(w0). This valid map costs O(r^3) AND gates. The available Omega(r^3/(log r)^4) lower bound is smaller than that cost by a log^4(r) factor, so it gives no positive q bound. A useful transfer needs a cheaper map with variable low-table witnesses. Source: [Cavalar-Oliveira](https://arxiv.org/abs/2503.14117).

**Status.** The transfer lemma and OR-only no-go are proved. There is no superlinear fusion-cover bound, no lower bound on the exact C-75 rect-DAG, and no P-vs-NP result from this route. The next task is to find a hard monotone f and a valid map phi with a < CycAnd(f)-N^(1+epsilon), or prove a general lower bound on a that closes the route.




## 56. C-126 - The transfer map is a reduction to low-code extension

This sharpens C-125 by separating the yes-side coding condition from the no-side high-completion condition. Let e(t) be the signed one-hot encoding of an N-bit table and define the monotone predicate

    LowExt_Y(u) = 1 iff there exists w in Y with e(w) <= u.

Suppose phi satisfies the C-125 transfer conditions: every YES input x has a low w with e(w) <= phi(x), and every NO input x has a high z with phi(x) <= e(z). Then

    f(x) = LowExt_Y(phi(x))

for every x. On YES inputs this follows from the first condition. On a NO input, if a low w also satisfied e(w) <= phi(x), then e(w) <= phi(x) <= e(z). Since e(w) and e(z) each have exactly one set rail at every coordinate, e(w) <= e(z) forces w=z, contradicting Y disjoint from Z. This proves the NO direction.

The two requirements have distinct roles. Low-code extension alone distinguishes YES from NO on the image of phi. The additional high-table completion condition places each NO image below a point where the fusion separator is known to be 0; without it, phi may land on an unconstrained medium input. Every NO image is therefore a consistent partial assignment whose completion cube intersects Z. The unset-coordinate count from C-125 is sufficient, not necessary, for this intersection.

Conversely, if a monotone phi computes f through LowExt_Y and every NO image has a high completion, it satisfies C-125 exactly and gives CycAnd(f) <= q+a. Thus the search for a useful transfer is precisely for a low-AND monotone reduction to the upward closure of the signed low-table codes, with a separate high-completion guarantee on NO inputs.

**What this changes.** The witness table on a YES input may vary with x; the map need not output one fixed low truth table. On NO inputs the vector must be consistent, but YES images may contain extra conflicting rails outside the selected low code. This asymmetry is why the OR-only fixed-code proof does not immediately extend to maps with AND gates. No nontrivial lower bound on the AND cost of such a map is established. The next task is to exploit or lower-bound this exact extension predicate, not merely count low-table descriptions.

## 57. C-127 - Witness variation forces global conflict support

Let phi be a C-125 transfer map for a monotone function f with at least one YES input, and define its global conflict support

    S(phi) = { k in [N] : for some YES input x, both phi_(k,0)(x)=1 and phi_(k,1)(x)=1 }.

Write delta=|S(phi)|. For each YES input x choose a low witness w_x in Y with e(w_x)<=phi(x), and fix one YES input x0 with witness w0. If x is any other YES input, then x OR x0 is also YES. Monotonicity gives e(w_x)<=phi(x OR x0) and e(w0)<=phi(x OR x0). Therefore, whenever w_x and w0 differ at coordinate k, both signs are active at phi(x OR x0), so k lies in S(phi). Every selected low witness consequently agrees with w0 outside S(phi).

Let W be the low tables agreeing with w0 outside S(phi). Then |W|<=2^delta. The function f has the following acyclic monotone circuit, reusing phi's outputs:

    [AND over k outside S(phi) of phi_(k,w0[k])]
      AND
    [OR over w in W of (AND over k in S(phi) of phi_(k,w[k]))].

Every YES input satisfies the term for its selected witness w_x. If this circuit accepted a NO input, some w in W would have e(w)<=phi(x); the high completion z from C-125 also has phi(x)<=e(z), forcing w=z, impossible. The construction therefore computes f and uses at most a + N + delta*2^delta AND gates. Since an acyclic circuit is a special case of a cyclic one,

    CycAnd(f) - a <= N + delta*2^delta.

This is a support-versus-cost constraint on every C-125 map. If its transfer inequality is to prove q>N^(1+epsilon), then necessarily N+delta*2^delta>N^(1+epsilon), which entails

    delta >= (1+epsilon)*log2(N) - O(log log N).

The lemma does not upper-bound q and is not a lower bound on the full fusion cover. It says a successful cheap map cannot keep all YES-side conflicts concentrated on a very small fixed set of table coordinates. The next target is to exploit this forced conflict spread or strengthen the circuit reconstruction to account for a itself.


## 58. C-128 - Local-PRG MCSP bounds survive the promise, but only for trees

This is a representation-matched use of Cheraghchi, Kabanets, Lu, and Myrisiotis, *Circuit Lower Bounds for MCSP from Local Pseudorandom Generators* (2020). Their proof against exact MCSP uses only two facts about the tested function h: h rejects almost every uniform truth table, and h accepts every output of a local PRG whose output tables have circuit complexity below the threshold. The same argument works for the active Gap-MCSP separator despite arbitrary medium-band behavior.

Fix 0<beta<1, set s1=N^beta/(c n), s2=N^beta, and let h:{0,1}^N->{0,1} satisfy h=1 on SIZE(s1) and h=0 on tables of circuit complexity greater than s2. There are at most 2^{O(s2 log(s2+n))}=2^{o(N)} tables of size at most s2. Hence under a uniform table h accepts with probability at most 2^{-N+o(N)}. A local PRG against the model of h whose every seed output has table circuit size at most s1 is accepted with probability 1. Such a PRG cannot fool h within 1/3.

The paper gives, for size-S de Morgan formulas, a local PRG with output-bit circuit complexity S^{1/3} 2^{O((log S)^{2/3})}; for arbitrary-basis formulas or general branching programs it gives S^{1/2} 2^{O(sqrt(log S))}. These constructions are stated for S>=N. Therefore, when beta>1/3, a de Morgan formula separator must have size N^{3 beta-o(1)}: if its size were below N, use the PRG for size N (whose locality is below s1); otherwise apply the size-S PRG and invert its locality bound. Likewise, for beta>1/2, arbitrary-basis formula and branching-program separators require N^{2 beta-o(1)} size. This is a lower bound for the promise problem, not just exact MCSP; medium tables are counted with SIZE(s2) on the uniform side and are otherwise unrestricted.

**Why it does not advance the OPS target.** The magnification premise requires every sufficiently small fixed beta. For beta<=1/3 (de Morgan formula) or beta<=1/2 (arbitrary-basis formulas/branching programs), these bounds do not become superlinear. More fundamentally, these are formula/tree or branching-program bounds, not bounds on a shared rect-DAG. The C-75 DAG permits shared states, and the known map from it to a separator circuit preserves sharing rather than turning it into a formula. A formula lower bound therefore cannot be inserted into the q-to-DAG inequality chain. In the protocol-tree direction it yields only a tree-size bound; the q-state protocol has an O(q log N)-bit path bound, whose tree may be exponentially larger.

**Classification.** This closes a literature-transfer gap for the tree model and gives an explicit exponent range. It does not improve the arbitrary shared-DAG lower bound, the active q lower bound, or P-vs-NP. The needed new theorem is either a local-PRG-style lower bound for a model that still permits the rect-DAG's sharing, or a near-lossless conversion from fusion closure to a model covered by these bounds. Neither is known here. Source: [Cheraghchi, Kabanets, Lu, and Myrisiotis](https://www2.cs.sfu.ca/~kabanets/papers/MCSP_lower_bounds.pdf).


## 59. C-129 - Quantitative C-75 baseline and a state-volume constraint

This section completes the resource-by-resource accounting for the exact mismatch relation and adds a quantitative condition on any shared rectangle state.

### The relation and its two variants

Let Y = SIZE(s1) and Z = {0,1}^N minus SIZE(s2), with s1 < s2. Alice receives w in Y, Bob receives z in Z, and a valid output is a signed coordinate (k,b) with w_k=b and z_k=1-b. This relation is total because Y and Z are disjoint. Alice may instead receive a circuit description d with G(d)=w. The description map is onto Y after restricting to descriptions that compute low tables; collisions do not alter the relation's minimum rect-DAG size (C-123).

For a fixed proposed pair list Q, both parties know Q and may compute the semantic containment/support graph locally; Alice knows w and its activation vector, while Bob knows z and its activation vector. The stronger output is a path i0,...,it plus a signed coordinate (k,b) satisfying: T_i0 is empty and i0 is active on w but inactive on z; each transition ir to i(r+1) uses a side S_r in {E_ir,H_ir} that is false on z, with T_i(r+1) subset S_r and i(r+1) active on w but inactive on z; the terminal side S_t is false on z and contains a matching literal slice for w_k=b, with z_k=1-b. The activation rank on w strictly decreases at each rule transition. This path relation is total exactly when Q refutes every low anchor. It is not interchangeable with the always-total plain mismatch relation. The fully expanded witness definition and proof of existence are in Section 1 above.

### Quantitative bounds by model

Write ell = O(s1 log(s1+n)) = N^(beta+o(1)) for a fixed-length circuit description, where s2=N^beta, 0<beta<1, and s1=N^beta/(c n).

- **Deterministic communication:** the description protocol gives D_cc(Mis_Y,Z) <= ell + ceil(log N) + O(1). A direct lower bound is given below: D_cc >= (1-beta)n - O(log n) = Omega(n). Thus the known interval is Omega(n) <= D_cc <= N^(beta+o(1)).
- **Ordinary protocol tree:** the same protocol has at most O(N 2^ell) nodes. Every tree solving the relation needs at least floor(N/d) leaves, where d = Theta(s2 log(s2+n)), by the disjoint-output family below.
- **Rect-DAG:** its size is exactly the shared-state resource, and is Theta(C_sep(Y,Z)), the minimum Boolean promise-separator circuit size (C-89/C-123). The enumeration tree gives O(N 2^ell) vertices. The disjoint-output family gives a direct lower bound Omega(N/d); independently, the existing cover floor rho_prom >= N-o(N) and reverse conversion rho_prom <= O(S_rect) imply S_rect = Omega(N).
- **Q-dependent ranked path:** if Q succeeds, its q rule states plus at most 2N signed-output terminals give a cyclic search graph with q+2N vertices. Listing all possible support transitions costs at most O(q^2+qN) arcs: there are at most q possible rule supports on each of two sides and at most 2N literal seeds per side. Every fixed input-pair path terminates because the activation rank on w decreases. Communicating each chosen side/support gives O(q log(N+q)) bits overall. Counting only cyclic AND/intersection operations gives exactly q, the native cover measure. This is a cyclic state protocol, not a Sokolov/GGKS acyclic rect-DAG.
- **Cyclic closure and standard-DAG transfer:** the exact native identity remains q = rho_prom = D^circ_cap. The best general compiler recorded here gives S_rect = O(q^3/log q); conversely rho_prom <= O(S_rect). Therefore a rect-DAG lower bound above N^(3+3 epsilon)/log N is needed to force q > N^(1+epsilon) through this route. The elementary bounds in this section are far below that scale.

### Disjoint-output fooling family

Let M2 = |SIZE(s2)| be the number of distinct truth tables of circuit size at most s2. Choose an integer d > log2(M2), and partition md <= N truth-table coordinates into disjoint blocks A1,...,Am, where m=floor(N/d). For each block Ai, the 2^d tables supported inside Ai outnumber M2, so at least one such table zi is high. It is nonzero because the zero table is low. Fix the low row w=0^N.

The set of valid outputs for (w,zi) is precisely {(k,0): k is in supp(zi)}. These sets are nonempty and pairwise disjoint because the blocks are disjoint. Hence no protocol leaf, or rect-DAG output leaf, can solve two of these pairs: its single output label would have to lie in two disjoint valid-output sets. Consequently every protocol tree and every rect-DAG has at least m leaves/nodes, and deterministic communication is at least log2(m)-O(1).

Circuit counting gives log2(M2)=O(s2 log(s2+n)), so take d = Theta(s2 log(s2+n)) = N^(beta+o(1)). Then m = Omega(N/(s2 log(s2+n))) = N^(1-beta-o(1)) and D_cc >= (1-beta)n-O(log n). This is an elementary lower bound for the plain relation's tree and DAG sizes, not a lower bound on q: one closure state can support many different mismatch labels, and the current q-to-DAG direction is only an upper simulation.

### Shared-state non-shareability lemma

For a rect-DAG node v, write its feasible rectangle as A_v x B_v, with A_v subset of Y and B_v subset of Z, and let K_v subset of [N] be all coordinate labels appearing at descendant leaves. Validity forces the projections of A_v and B_v onto K_v to be disjoint, since a pair agreeing on all of K_v has no valid output anywhere below v. Put k=|K_v| and r=|pi_Kv(A_v)|. Each of the r distinct row signatures determines a disjoint K-fiber of size 2^(N-k). At most M2 tables in any fiber can be non-high. Since B_v must avoid every high table in each such fiber,

    |Z minus B_v| >= r(2^(N-k)-M2), whenever 2^(N-k)>M2.       (C-129)

In particular, a node that still admits every high column (B_v=Z) and has a nonempty row set must have k >= N-log2(M2). More generally, merging more row-projection signatures forces the shared state to discard proportionally many high columns unless its descendant output set is large.

This is a concrete product-hull constraint, stronger quantitatively than merely saying that merged histories create cross-pairs. It does not yet sum over nodes: a protocol can first shrink B_v, and the current proof has no charging rule that prevents the same excluded high tables from paying for many states. Thus it is a Tier-3 candidate non-shareability invariant, not a DAG lower bound beyond the elementary floor.

### Universal-DAG verdict and model comparison

The strongest explicit universal construction already found is the restriction-sharing DAG from C-78. For each dyadic coordinate interval I and low-table restriction u that occurs on I, use the rectangle

    R_(I,u) = {w in Y: w|I=u} x {z in Z: z|I differs from u}.

Recursing to the two subintervals is valid because every pair in the parent differs somewhere in I. After an O(|Y|)-vertex row-routing prefix, this gives

    S_universal <= O(|Y| + sum over dyadic I of pi_I(Y)),

where pi_I(Y) is the number of distinct restrictions of low tables to I. A coarse bound is O(|Y| N/log |Y| + N log N) when |Y| is large. This improves independent O(N)-scans per low row by sharing equal restrictions. It remains far above N^(1+o(1)) at the available |Y| upper bounds, and it does not lower-bound the optimal DAG.

Sending a description plus a mismatch index gives the simpler explicit tree of O(N 2^ell) states. Any further compression must merge different description histories into shared rectangles. Such a merge must satisfy the product-hull constraint above for every low/high cross-pair; universal-circuit evaluation alone does not certify it. C-123 already proves descriptor-domain and truth-table-domain rect-DAG sizes are equal, so replacing w by d is not itself a compression theorem. No N^(1+o(1)) universal DAG has been constructed, and the state-volume lemma does not rule one out.

The literature comparison remains model-specific: Sokolov's Boolean communication game and the Garg--Goos--Kamath--Sokolov rect-DAG are acyclic shared rectangles; Cavalar--Oliveira identify fusion exactly with cyclic intersection complexity; Nakayama--Maruoka loop circuits are related but use a different approximation-model setup; Amano--Maruoka study acyclic monotone AND-count complexity for quadratic functions. None identifies the ranked input-dependent closure with an ordinary acyclic rect-DAG. Primary sources: [Sokolov](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download), [Garg et al.](https://www.theoryofcomputing.org/articles/v016a013/v016a013.pdf), [Cavalar--Oliveira](https://arxiv.org/abs/2503.14117), [Nakayama--Maruoka](https://doi.org/10.1006/inco.1995.1083), and [Amano--Maruoka](https://doi.org/10.1007/s00453-006-0073-0).

**Classification.** C-129 gives the exact C-75 relation, direct communication/tree/DAG baselines, and a proved state-volume exclusion law. It identifies a sharper quantity to charge when histories merge, but the global charging step and any superlinear q lower bound remain open. No P-vs-NP breakthrough follows.


## 60. C-130 - The raw exclusion-volume sum double-counts by a factor N

I tested the direct global-charge idea against the strongest explicit universal construction, the restriction-sharing DAG in C-78. The test gives an exact obstruction to summing the C-129 excluded-column counts as though different states paid for disjoint tables.

Choose w=0^N and a coordinate block A of size d > log2(M2), where M2=|SIZE(s2)|. Among the 2^d tables supported inside A there is a high table z. Its mismatch support D=supp(z) is nonempty and has size at most d=O(s2 log(s2+n))=N^(beta+o(1))=o(N/log N) for each fixed beta<1.

For every dyadic coordinate interval I disjoint from D, the restriction-sharing DAG has the state

    R_(I,0) = {w' in Y: w'|I=0} x {z' in Z: z'|I is not 0}.

The high table z agrees with 0 on I, so z is in the stateÃ¢â‚¬â„¢s excluded high-column set Z minus B_(I,0). A coordinate belongs to only log2(N)+1 dyadic intervals, so at most d(log2(N)+1) intervals meet D. Out of the 2N-1 dyadic intervals, at least 2N-1-d(log2(N)+1)=2N-o(N) are disjoint from D. Thus the same high table is charged by the local exclusion measure at Omega(N) distinct states.

The intervals here are genuinely present/reachable in the restriction-sharing DAG: 0 is a low restriction on each I, and high tables differing from 0 on I exist, so each rectangle has a nonempty feasible set. This is not merely padding with duplicate or unreachable nodes.

**Consequence.** The state-volume inequality is valid, but summing |Z minus B_v|, or assigning each counted high table to only O(1) states, fails even on the known restriction-sharing construction. Any useful global potential must charge *newly exposed* information or account for the routing context, rather than count excluded tables state by state. The example does not rule out a weighted potential; it kills only the raw-volume sum and constant-multiplicity charging.

This also pinpoints why the interval construction can reuse states: a high table that agrees with a low row on many off-path intervals is excluded from many corresponding rectangles, while the pair itself follows only the interval branch containing a mismatch. C-86's scan observation and C-78's restriction sharing are therefore the right stress tests for every proposed global charge.

**Status.** O-110 is narrowed: the next candidate must charge the first divergence on the actual routed path, or prove that many incompatible restrictions force distinct states despite this Omega(N) overlap. The overlap loss is already linear in N, so it cannot by itself produce the required superlinear DAG bound, much less overcome the cubic q-to-DAG transfer. This is a proved failure of one summation strategy, not evidence against all shared-DAG lower bounds.


## 61. C-131 - Endpoint bottleneck width is large at the root

I tested whether the recent bottleneck-counting method for DAG-like communication could turn the C-129 state inequality into a path-sensitive charge. Beame and Whitmeyer assign individual inputs to bottleneck nodes using a width defined by the minimum number of output rectangles needed to cover a node's one-sided slice. Their proof is for Search-BPHP triangle-DAGs: the bound on inputs assigned to one node uses the equality-graph structure of pigeonhole violations and ordered slices of triangles. It is a useful template, but those hypotheses do not hold automatically for the present mismatch relation. [Primary paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/LIPIcs.ICALP.2025.21/LIPIcs.ICALP.2025.21.pdf).

Here is the exact natural width and the obstruction. For a rect-DAG node (v) with rectangle (A_v\times B_v), and a row (w\in A_v), define

    h_v(w) = min |S| over S subset of K_v such that
             every z in B_v differs from w on at least one coordinate in S,

where (K_v) is the set of coordinate labels at descendant leaves. This is precisely the minimum number of mismatch-output rectangles whose (w)-slice covers (B_v). Any correct protocol's leaves reachable with Alice input (w) provide such a cover.

Let (M_2=|\mathrm{SIZE}(s_2)|). For every (w\in Y) and every coordinate set (S\subseteq[N]) with (2^{N-|S|}>M_2), the fiber

    F(w,S) = {z : z|S = w|S}

contains a high table: it has (2^{N-|S|}) members and at most (M_2) non-high tables. Therefore no set of fewer than (N-\log_2 M_2) coordinates can hit every mismatch between (w) and (Z). At the root, for every low row,

    h_root(w) >= N - log2(M2) = N - N^(beta+o(1)).

Equivalently, the subgraph reachable with a fixed Alice input (w) must expose at least (N-\log_2 M_2) distinct output coordinates across its leaves. This is an inputwise strengthening of the root descendant-coordinate bound: every low row individually needs almost all coordinate labels available somewhere in its reachable subgraph.

This does not yield a superlinear vertex bound. The invariant counts only distinct coordinates (at most N for a fixed w), not how many context-specific leaf vertices are required, and the missing cost is how the graph routes different (z)'s to a valid leaf while preserving rectangular states. The bottleneck assignment template also fails in its direct form: when processing states from sinks toward the root, the root already has width (N-o(N)) for every remaining low row, so it would assign all such rows to one node. The BPHP proof avoids that collapse by a problem-specific per-node capacity estimate; C-129 supplies no corresponding capacity bound here. C-130's restriction-sharing DAG also shows why replacing nodewise capacity by an unweighted sum of off-path exclusions double-counts a fixed high table at ÃŽÂ©(N) states.

**Next obligation.** A successful adaptation needs a bottleneck statistic with (i) a root-to-sink crossing for many endpoint inputs, (ii) a nontrivial per-node capacity bound for the MCSP promise, and (iii) a charging rule tied to actual routing rather than all rectangles that exclude a table. The natural mismatch-cover width satisfies (i) but currently has no (ii); the raw signature-volume count has (ii) only locally and fails (iii). This narrows O-110/O-111 but proves no superlinear rect-DAG or fusion-cover lower bound.

**Classification.** The per-row output-support lemma is proved. The transfer of bottleneck counting is a failed attempt with a precise failure point. No P-vs-NP breakthrough follows.


## 62. C-132 - Width-band nodes can contain every low row

The edge version of the bottleneck idea avoids one defect of C-131. For a fixed row w, if a rectangle node is covered by two child rectangles, the child column sets for those children containing w cover the parent column set. Hence

    h_parent(w) <= h_child0(w) + h_child1(w),

where h is the minimum number of descendant output coordinates hitting all columns. At least one child has width at least half the parent's width. Following such a child gives a path on which width cannot drop by more than a factor two per step; since leaves have width one, this path crosses any intermediate width band. But the missing per-node capacity estimate is false for width alone, even on the active low/high promise.

Let (I\subseteq[N]) have size (3N/4), let (P=\{w|_I:w\in Y\}), and define

    B = {z in Z : z|I is not in P}.

Circuit counting gives (|Y|=2^{o(N)}) and (M_2=|\mathrm{SIZE}(s_2)|=2^{o(N)}) for every fixed promise exponent below one. Both B and (Z\setminus B) are nonempty for large N: tables with prefix in P number at most (|Y|2^{N/4}=2^{N/4+o(N)}), while any fixed prefix in P has (2^{N/4}>M_2) high completions. Every pair in (Y\times B) differs within I, so there is a valid rect-DAG for this rectangle whose descendant outputs lie entirely in I (for example, the restriction-sharing interval protocol).

Fix any (w\in Y) and (S\subseteq I) with (|S|\le N/2). The fiber of tables agreeing with w on S has size at least (2^{N/2}). At most (M_2=2^{o(N)}) of them are non-high, and at most (|P|2^{N/4}=2^{N/4+o(N)}) have I-restriction in P. Their sum is less than (2^{N/2}) for large N, so the fiber contains a z in B. Thus no such S hits all columns of B against w, and

    h_v(w) > N/2.

On the other hand, the sub-DAG outputs only in I, so its descendant label set (K_v\subseteq I) hits every pair and (h_v(w)\le |K_v|\le 3N/4). This holds for every low row w. We have therefore constructed a valid rectangle node with full row side (A_v=Y) and

    N/2 < h_v(w) <= 3N/4   for every w in Y.

To place it inside a full protocol, split the root (Y\times Z) into (Y\times B) and (Y\times(Z\setminus B)); these are rectangles covering the root. Use the interval protocol on the first child and any finite mismatch protocol on the second. The root width is at least (N-\log_2 M_2=N-o(N)). For the band ([0.4N,0.8N)), the child v lies in the band for every w and has width greater than half the root width. Since B is nonempty, for every w there is a pair (w,z) routed through v. Hence a path rule that follows any child retaining at least half-width can send every low row through this same bottleneck node. The node can absorb (|Y|) rows.

**What is falsified.** There is no per-node capacity bound based only on the value of (h_v(w)), even after restricting to nodes on a legitimate width-preserving path. A global proof could still choose paths by an additional rule or use a statistic that tracks which high columns were removed, the projection family P, or other context. C-132 does not disprove all bottleneck methods; it proves the direct width-only assignment has no generic capacity lemma. The edge inequality is valid but is not itself a DAG lower bound.

**Next obligation.** O-111 must account for the *shape* and prevalence of the excluded column set, not merely its width or cardinality. Test any refined assignment against this dense child rectangle and against C-130's repeated off-path exclusions. No superlinear rect-DAG bound or P-vs-NP result follows.

## 60. C-133 Ã¢â‚¬â€ The restriction-sharing universal DAG is exponentially large

This is a lower bound on the specific C-78 universal construction, not on arbitrary rect-DAGs.

Let Y be the low truth-table set SIZE(s1), with fan-in-two circuits and OPS parameters s1 = N^beta/(c n), for fixed 0 < beta < 1. Fix any set I of k truth-table coordinates. Every bit pattern u on I is the restriction of a row in Y whenever k <= s1/(8(n+1)): define the table to be 1 exactly on the selected inputs in I, and compute it as an OR of at most k full input minterms. The shared variable negations, minterms, and final OR use at most k n + n + O(1) gates, which is below s1 for these parameters and all large n. Thus every such I has all 2^k possible low-row restrictions.

The C-78 restriction-sharing construction has a state R_(I,u) for every dyadic interval I and every low-row restriction u on I. Choose a dyadic length k <= s1/(16(n+1)) and k >= s1/(32(n+1)). There are N/k intervals of this length, and each has all 2^k patterns. Therefore this construction has at least

    (N/k) 2^k = 2^(Omega(s1/n)) = 2^(Omega(N^beta/n^2))

states. The states counted at this one level are distinct: different patterns on one interval give disjoint nonempty row sides; for two distinct intervals, arbitrary patterns on their union (size 2k <= s1/(8(n+1))) are realizable, so their row sides differ. Thus deduplicating identical rectangles cannot reduce this architecture to N^(1+o(1)) states.

**What this kills.** C-78 cannot be the desired near-linear universal DAG. Its sharing key is an interval plus the exact low-table restriction there; the low class is locally surjective on every block of O(s1/n) coordinates, so those keys have exponentially many values.

**What this does not kill.** This is not a lower bound on arbitrary rect-DAGs, the C-75 relation, or q = rho_prom. General states can use arbitrary semantic row and column subsets, non-interval descendant outputs, and column filtering before rows merge. C-132 already shows why width alone cannot force interval-like contexts. C-123's descriptor-invariance result remains relevant: replacing tables by short circuit codes does not change minimum rect-DAG size, but it does not prove that this size is large.

**Updated target.** To go beyond C-133, prove a routing theorem forcing a general DAG to expose many restriction contexts, or find a different representation that compresses residual search relations without admitting invalid cross-pairs. Local surjectivity alone is insufficient because a protocol can shrink its high-column side before merging row contexts. No global non-shareability invariant, superlinear DAG lower bound, superlinear fusion-cover bound, or P-vs-NP result follows.
## 61. C-134 - Local restriction richness does not force a large general DAG

Let I be any set of k truth-table coordinates with k <= s1/(8(n+1)), and let Y_I consist of all tables supported inside I. Each of the 2^k patterns on I is in Y_I by the point-minterm construction from C-133, so this subfamily is maximally rich on I and has 2^k distinct rows.

Nevertheless, the mismatch relation on Y_I x Z has an O(N)-vertex rect-DAG. Every high table z in Z has a 1 at some coordinate j outside I: otherwise z is supported in I and the same O(kn) construction puts it below s1. Every row w in Y_I has w_j=0. Order the N-k coordinates outside I. At stage t, the rectangle contains all rows Y_I and those high columns that have been 0 on the earlier outside coordinates. Its two children are the columns with z_j=1, which form a leaf labelled (j,0), and the columns with z_j=0, which continue to stage t+1. At the final coordinate the continuation side is empty, since no high table is supported inside I. The rectangles cover at every stage, and every leaf label is a valid mismatch. This uses at most 2(N-k)+1 vertices.

**Lesson.** Exponentially many low rows and all possible restrictions on a small coordinate block do not by themselves imply a large shared-DAG complexity. Here all rows share the same zero pattern outside I, and every high column must expose a common-type witness there. Any general lower bound must capture how row variation interacts with the *available high-column residuals*; projection cardinality alone is insufficient. This example does not give a small DAG for the full Y x Z relation, since Y has no common zero region of this size.

**Updated O-113 test.** A proof that general DAGs must expose many restriction contexts cannot rely only on the fact that all patterns occur in a block. It must also rule out a common mismatch region or another column-side certificate that bypasses those contexts. C-132 supplies the complementary warning: filtering columns can keep all rows in a medium-width state. No arbitrary-DAG lower bound, fusion-cover lower bound, or P-vs-NP result follows.

### C-133/C-134 placement in the fusion inequality chain

The q-pair cover is exactly the active promise cyclic conjunctive complexity, q = rho_prom = D^circ_cap. The strongest general binary-fanin compilation currently recorded is S_rect = O(q^3/log q), and an L-vertex mismatch rect-DAG gives rho_prom <= O(L). Thus, if q <= N^(1+epsilon), the compiled separator has size O(N^(3+3epsilon)/log N); a rect-DAG lower bound asymptotically above that scale would force q > N^(1+epsilon). In the AND-only acyclic measure, D_cap <= q^2, so a separator lower bound above N^(2+2epsilon) would suffice. A direct cyclic lower bound on q avoids these losses. C-133 only lower-bounds one explicit DAG construction, and C-134 only refutes projection richness as a general statistic; neither enters this inequality chain as a lower bound for S_rect or q.

## 62. C-135 - Low-variation row rectangles admit a common mismatch router

Let A be a nonempty subset of Y, choose w0 in A, and define its variation support

    V(A) = {j in [N] : there are w,w' in A with w_j != w'_j}.

All rows in A agree with w0 on the complement C=[N]\\V(A). There is an absolute constant K such that, for every S subset of [N] with |S|=r, any table z agreeing with w0 outside S has

    CC(z) <= s1 + K n(r+1).

Indeed, let chi_S be the indicator of the selected truth-table coordinates in S, and let p be the indicator of those coordinates in S where z is 1. Both are ORs of at most r input minterms and have size O(n(r+1)). Then z=(w0 AND NOT chi_S) OR p. This preserves w0 outside S and sets z arbitrarily inside S.

For the OPS gap s2=c n s1, choose d=floor((s2-s1)/(4K n)). For sufficiently large n, K n(d+1)<s2-s1. If |V(A)|<=d, no high table z in Z can agree with w0 on all of C, since the displayed patch circuit would put z below s2. Thus every z in Z differs from the common row pattern at some coordinate j in C, and every w in A has that same bit w0_j there.

Consequently the whole rectangle A x B, for any B subseteq Z, has an O(N)-vertex rect-DAG: Bob scans the coordinates of C in a fixed order, continuing while z_j=w0_j and outputting (j,w0_j) at the first disagreement. No high column can reach the empty continuation after the last coordinate. Every leaf is a valid signed mismatch. In particular, any existing DAG state with row side A and |V(A)|<=d can have its descendants replaced by this common-mismatch router.

Here d=Theta((s2-s1)/n)=Theta(s1) for the OPS parameters. C-134 is the special case where A consists of all tables supported in I; C-135 shows that small coordinate-variation support, rather than a shared zero block, is the operative condition.

**Limit.** This is a local upper bound on easy rectangles, not a lower bound on the number of states in a DAG for the full Y x Z relation. The root has V(Y)=[N] because both constant tables are low. A protocol might have many distinct low-variation states whose scan subgraphs do not share, and large variation support alone does not guarantee a large projection profile or a costly state. The next step is to exploit the dichotomy between small-variation easy rectangles and large-variation residual rectangles without assuming that either family must have many vertices. No superlinear rect-DAG, fusion-cover, or P-vs-NP result follows.

## 63. C-136 - Hamming gap, fractional witnesses, and the deterministic-routing bottleneck

Set d=floor((s2-s1)/(4Kn)), with K as in C-135. For low w and high z, let r=dist_H(w,z). Patching a size-s1 circuit for w at the r disagreement points computes z using at most s1+Kn(r+1) gates. The choice of d leaves this below s2 whenever r<=d. Hence every promised pair has r>=d+1, and d=Theta(s1)=Theta(N^beta/n) in the OPS regime.

For each output label (i,b), define the legal mismatch rectangle

    R_(i,b)={w in Y:w_i=b} x {z in Z:z_i=1-b}.

Every promised pair belongs to exactly dist_H(w,z) of these 2N rectangles. Giving each label rectangle weight 1/(d+1) is therefore a fractional cover of the ordinary labelled search relation with total weight 2N/(d+1)=O(N/s1)=O(n N^(1-beta)). This is not a bound on rho_prom: the fractional object here is the standard rectangle cover of the C-75 relation, and overlapping rectangles do not supply a deterministic protocol partition.

The same count puts a hard ceiling on one common lower-bound method. In a label-conflict fooling family, no two selected pairs can share an output-labelled leaf. Their valid-label sets are then pairwise disjoint subsets of a universe of 2N labels, each of size at least d+1. Consequently the family has size at most 2N/(d+1)=O(N/s1). C-138 improves C-129's explicit construction from N/(s2 log s2) to N/s2, leaving a factor Theta(n) to this method ceiling; both are sublinear in N. This does not upper-bound the minimum rect-DAG: rectangles can be incompatible for global cross-product reasons even when their selected pairs share some valid labels.

There is also a public-coin protocol: repeatedly sample a uniform coordinate, publicly, and have the parties reveal their two input bits. A trial returns a valid signed mismatch with probability at least (d+1)/N. The protocol is zero-error and has expected O(N/d) communicated bits. In contrast, no fixed coordinate sample of size below N-log2(M2) works for every pair: for any fixed low w and coordinate set T with 2^(N-|T|)>M2, there is a high table agreeing with w on T. Since log2(M2)=N^(beta+o(1))=o(N), universal nonadaptive sampling requires N-o(N) coordinates.

**Frontier refinement.** Witness scarcity is not the obstruction: each pair has many outputs, the labelled fractional cover is small, and randomized search is short. Deterministic routing must adapt to equal answers, and each history constrains a rectangle; the unproved issue is whether those history-dependent residual rectangles can be shared globally with near-linear size. Standard label-conflict fooling sets and fixed-sample arguments cannot prove the needed superlinear lower bound. This is a proof-level negative result about those methods, not a DAG or fusion lower bound. See C-136/O-116/Q96.

## 65. C-138 - Sparse high tables sharpen the elementary leaf lower bound

The standard circuit count gives M2=|SIZE(s2)|<=2^(C s2 log(s2+n)). Choose r=ceil(A s2) with A large enough that binom(N,r)>N M2; for fixed beta<1, log binom(N,r)>=r log(N/r)=A(1-beta-o(1))s2 n. In a random partition of [N] into floor(N/r) blocks of size r, each block's indicator table is low with probability at most M2/binom(N,r). A union bound in expectation shows some partition has no low block, so every indicator 1_(S_i) is high.

The pairs (0^N,1_(S_i)) have pairwise-disjoint valid output-label sets, each supported on S_i. Thus a deterministic protocol tree or rect-DAG needs Omega(N/s2)=Omega(N^(1-beta)) leaves and D_cc >=(1-beta)n-O(1). This improves the earlier C-129 choice d>log M2 by a factor Theta(n) in the direct leaf and communication bounds.

For any fixed low w, at most M2 of the binom(N,r) weight-r masks e make w XOR e non-high, so a uniform perturbation is high with probability 1-o(1). This gives a natural noisy-pair distribution for future rectangle-corruption attempts. The direct leaf-mass calculation is capped at N/r: any labelled output leaf requires its coordinate to lie in the random mask, an event of probability r/N. Thus the noise distribution does not itself improve the leaf bound.

The result remains below the existing Omega(N) rect-DAG floor and far below a superlinear lower bound. C-136's label-conflict ceiling is O(N/s1)=O(nN^(1-beta)), so elementary output-disjoint families still leave a factor Theta(n) gap. Neither the rect-DAG inequality chain nor rho_prom changes. See C-138.

## 64. C-137 - Why a cyclic equality scanner cannot be shared as a rect-DAG

One apparent universal protocol uses one state per coordinate i: compare w_i,z_i, output (i,w_i) on a mismatch, and advance to i+1 on either equal pair 00 or 11; wrap after N. For every promised unequal pair it would find a mismatch in one pass. But this is not a standard rect-DAG. From a rectangle A x B, the two equality outcomes lead to (A_0 x B_0) union (A_1 x B_1), which is not a rectangle whenever both bit classes on each side are nonempty. A shared DAG node cannot be the union of those two diagonal blocks because its product rectangle would also contain the cross blocks. The proposed scanner silently gives the transition rule joint access to both bits and discards the transcript value; rect-DAG transitions must preserve rectangular state semantics. Allowing cycles does not license this merge.

For the fixed coordinate-order scan, every prefix assignment actually occurs on both sides. If k<=s1/(8(n+1)), C-133's point-minterm construction realizes every k-bit pattern u as a low-row restriction. For each u, the fiber fixing those k bits has 2^(N-k)>M2 completions, so it contains a high column. Thus all 2^k equal-prefix rectangles are nonempty and have distinct row sides; a valid fixed-order scan must retain at least 2^k distinct continuation states. With k=Theta(s1/n), this is 2^(Omega(N^beta/n^2)). This recovers the local-context obstruction in a precise falsification of the cyclic-scan shortcut, not a general rect-DAG lower bound.

**Model distinction.** A finite-state transducer allowed to test a pair of input bits jointly can solve mismatch in O(N) states by this scan. A deterministic communication/rect-DAG model cannot simply treat the joint equality result as one bit while forgetting which equal pair occurred. C-74's cyclic closure game is also not an arbitrary joint-input transducer: its transitions are constrained by separate anchor activation and endpoint support semantics. Therefore neither the O(N) transducer nor its invalid rectangular merge implies a small rho cover. See C-137/O-117/Q97.

## 66. C-139 - A successful fusion cover induces a ranked cyclic rectangle game

This makes the C-75 state-preservation claim explicit and separates it from an ordinary rect-DAG.

Let Q have q pair rules and activation predicates x_i on the promise anchor domain. Write

    F_{i,E}(u)=a_i(u) OR OR_{j:T_j subset E_i} x_j(u),
    F_{i,H}(u)=b_i(u) OR OR_{j:T_j subset H_i} x_j(u),
    x_i(u)=F_{i,E}(u) AND F_{i,H}(u),

with the least-fixed-point interpretation. Let tau_i(w) be the first round in which x_i(w) becomes 1. If Q covers every low anchor, then for every w in Y there is an empty-carrier rule i with x_i(w)=1, while every z in Z has x_i(z)=0 for every such rule. Thus the root rectangle Y x Z is covered by the rule rectangles

    R_i = (Y intersect X_i) x (Z minus X_i),   X_i={u:x_i(u)=1}.

For any pair (w,z) in R_i, x_i(z)=0 makes at least one side, say E_i, false at z: F_{i,E}(z)=0. Since x_i(w)=1, the same side has a support at w. At the first activation round tau_i(w), choose a support that was already present at round tau_i(w)-1. If it is a literal slice L_(k,b), then L_(k,b) being false at z forces z_k=1-b while w_k=b, so (k,b) is a valid mismatch output. If it is a predecessor carrier T_j subset E_i, then x_j(w)=1 and tau_j(w)<tau_i(w). Also x_j(z)=0: otherwise upward closure would put E_i in the z-closure, contradicting F_{i,E}(z)=0. Therefore the pair moves to R_j.

Every transition is rectangle-preserving. The false-side condition depends only on z; the selected true support depends only on w. Splitting by side and then by a fixed priority among the row-side supports gives product rectangles whose union covers R_i. A literal-support branch ends at a valid mismatch label; a rule-support branch lies inside R_j. The activation rank tau_i(w) strictly decreases at every rule transition, so every fixed pair terminates after at most q rule states even though the static support graph may have cycles.

Consequently Q yields a ranked cyclic rectangle protocol with q rule states, at most 2N shared output terminals (or output labels on arcs), one root, and O(q^2+qN) possible support arcs. It solves plain mismatch only on Y x Z when Q is successful; the Q-witness relation that includes the path/support transcript is total exactly under that success condition. Plain mismatch is total for every disjoint Y,Z independently of Q. This is a precise Q-to-cyclic-search transformation, not a converse for arbitrary cyclic games.

To obtain a standard Sokolov rect-DAG, layer rule state i by an upper bound r on tau_i(w). A rule transition from layer r goes to a predecessor in layer r-1; literal supports go to mismatch leaves. The resulting state layer has q^2 copies (i,r). Binary routing among up to q+2N supports costs O(q+N) selector nodes per layered state and side, giving the direct bound O(q^2(q+N))=O(q^3) under the project floor q>=N-o(N). This explicit construction does not improve the saved O(q^3/log q) compiler; it exposes the two costs separately: input-dependent rank unrolling and support selection. Sharing selector trees across r would have to retain the threshold context without admitting cross-pairs, which is exactly the unproved step. Existing SCC/escape compilers may be smaller for structured Q.

**Model boundary.** Sokolov's Boolean communication games are globally acyclic with outdegree at most two, and each node's valid inputs are a product rectangle; the PLS conversion also assumes an acyclic state graph. Cavalar-Oliveira's exact theorem instead identifies the fusion cover with cyclic intersection complexity. The ranked cyclic rectangle protocol above is the explicit search object induced by Q, but its arbitrary semantic activation predicates and support graph do not make it an ordinary rect-DAG or an arbitrary loop circuit. See [Sokolov's definitions and PLS conversion](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download) and [Cavalar-Oliveira, Theorem 30](https://arxiv.org/abs/2503.14117).

**Tree/DAG correction.** If tree and DAG complexity both count vertices, then S_DAG<=S_tree because every tree is already a DAG. The possible gap relevant here is between communication depth/bits and graph size: c communicated bits imply only a tree upper bound 2^(c+1)-1, not O(c). For this promise, sending a low circuit description gives O(s1 log(s1+n)+log N) bits but up to O(N 2^ell) tree vertices, ell=O(s1 log(s1+n)); a Q-path transcript gives O(q log(q+N)) bits and at most (q+N)^(O(q)) tree vertices. A lower bound on protocol-tree node count does not lower-bound minimum DAG size, because S_DAG<=S_tree.

As a calibration, the artificial total relation with Alice input a in [M], Bob input a fixed symbol, and unique valid answer a has communication cost ceil(log2 M) but requires M differently labelled leaves in every protocol graph. This demonstrates why bit cost does not bound graph size; it does not model Gap-MCSP, where every low/high pair has Theta(s1) or more valid mismatch labels (C-136). The unique-output pathology is therefore unavailable as the needed non-shareability lemma.

**Status and next step.** C-139 settles the exact q-cover-to-ranked-cyclic-rectangle transformation and its termination proof. It does not produce a standard DAG of O(q polylog N), a reverse map from general cyclic rectangle games to fusion covers, a superlinear q/S_rect lower bound, or P != NP. O-117 remains open: seek either a rectangle-preserving way to share the (i,r) support routers across activation thresholds, or an actual-promise obstruction to every such adaptive sharing. Stress-test against C-132's all-row filtered child, C-135's small-variation routers, and C-137's equal-prefix cross-pairs. The best quantitative chain remains rho_prom<=O(S_rect)<=O(rho_prom^3/log rho_prom), with C-91--C-100's structured improvements.

## 67. C-140 - Input-dependent rank can be an artifact of the witness path

Test the claim that the q^2 rank-layer expansion reflects necessary output-DAG complexity. Consider the two-state monotone least-fixed-point system

    x1^(t+1) = (s1 OR x2^t) AND c,
    x2^(t+1) = (s2 OR x1^t) AND c,
    (x1^0,x2^0)=(0,0),

for input bits s1,s2,c. Its least fixed point is x1=x2=c AND (s1 OR s2). If c=1 and (s1,s2)=(1,0), state 1 activates at round 1 and state 2 at round 2; for (0,1), the order reverses. The static support graph has both edges 1->2 and 2->1, so no single topological ordering preserves the selected activation path on both inputs. Yet the output x1 has a two-gate acyclic implementation.

This is an abstract activation recurrence of the C-74 AND/OR shape, not a demonstrated realization by legal semantic endpoints and not a Gap-MCSP construction. It falsifies only the inference that the q^2 rank-layer cost is inherently needed to compute the separator: an acyclic circuit can simplify the output and abandon the particular closure witness path. Therefore a lower bound on the layered Q-witness DAG would not by itself lower-bound S_rect or rho. Any useful no-sharing lemma must constrain the minimum separator computation, not merely the rank-preserving simulation of Q. The exact endpoint-realization question is left open; no project lower bound changes.

## 68. C-141 - The rank-reversing two-state cycle has legal semantic endpoints

C-140's algebraic example can be realized by actual endpoint intersections in the Boolean-cube generator system (though not as a successful cover). Let Gamma={0,1}^5 with coordinates a,b,c,d,e and generators all ten signed coordinate half-cubes. Put A={a=0}, B={b=0}, C={c=1}, and P=C intersect (A union B). Choose p1=(1,1,0,0,0), p2=(1,1,0,1,0), and define

    E1=A union P union {p1,p2},     H1=C union {p1},
    E2=B union P union {p1,p2},     H2=C union {p2}.

Then T1=E1 intersect H1=P union {p1}, and T2=E2 intersect H2=P union {p2}. Thus T2 is contained in E1 and T1 is contained in E2, but T2 is not contained in H1 and T1 is not contained in H2. Each carrier also supports its own rule, which is only a self-support and can be deleted from the least-fixed-point recurrence.

The only literal generator contained in E1 is A; the only one contained in E2 is B; the only literal generator contained in either H_i is C. For example, E1 misses a point of each other coordinate half-cube: it misses (1,0,0,0,1) for B and c=0, and misses every point with a=b=c=1 for C and the other positive-coordinate slices; the d/e slices also contain such omitted points. The symmetric checks apply to E2, and H_i=C plus one marker cannot contain any other full half-cube. The effective activation equations are therefore exactly

    x1=(1_A OR x2) AND 1_C,
    x2=(1_B OR x1) AND 1_C.

Their least fixed point is x1=x2=1_C AND (1_A OR 1_B). On an anchor with (a,b,c)=(0,1,1), x1 activates one round before x2; on one with (1,0,1), the order reverses. The static semantic support graph genuinely has both rule directions, despite each input's selected support path being acyclic.

**Scope.** This is a legal two-rule fragment of the fusion activation recurrence, not a successful cover: neither carrier is empty, so it does not separate any target from a high set. It confirms that input-dependent ranks and static cycles are not artifacts of an abstract equation system. At the same time, the activated predicate simplifies to a constant-size acyclic formula, so the C-140 warning survives: the rank layers describe a witness path, not necessary separator size. A successful-cover/Gap-MCSP embedding that preserves this dynamic cycle while preventing output simplification remains open.

## 69. C-142 - A successful toy cover contains a rank-reversing SCC but has a tiny separator

C-141's local cycle can be placed upstream of an empty rule in a valid finite promise cover. Use four-bit anchors (a,b,c,f), low set

    Y={wA=(0,1,1,0), wB=(1,0,1,0)},

and high/filter universe

    Z={zA=(0,1,0,0), zB=(1,0,0,0), zC=(1,1,1,1),
       p1=(1,1,0,1), p2=(1,1,0,0)}.

For coordinates a,b,c,f, the restricted literal slices on Z are respectively

    a=0:{zA}             a=1:{zB,zC,p1,p2}
    b=0:{zB}             b=1:{zA,zC,p1,p2}
    c=0:{zA,zB,p1,p2}    c=1:{zC}
    f=0:{zA,zB,p2}       f=1:{zC,p1}.

Define three pair rules by their endpoints, all subsets of Z:

    (E1,H1)=({zA,p1,p2},{zC,p1}),
    (E2,H2)=({zB,p1,p2},{zC,p2}),
    (E0,H0)=({p1},{p2}).

Their carriers are T1={p1}, T2={p2}, T0=empty. The only seed slices contained in E1,E2,H1,H2 are, respectively, a=0; b=0; c=1 and f=1; c=1. Neither singleton endpoint E0 or H0 contains any literal slice. The support edges are 2->1 and 1->2 on the E sides, self-supports, plus 1->0 through E0 and 2->0 through H0. No cross-support enters the H side of rule 1 or the H side of rule 2.

After omitting self-supports in the least fixed point, the activation equations are

    x1=(1_{a=0} OR x2) AND (1_{c=1} OR 1_{f=1}),
    x2=(1_{b=0} OR x1) AND 1_{c=1},
    x0=x1 AND x2.

On wA, x1 activates first and x2 second; on wB, x2 activates first and x1 second. Both activate x0. Directly on the five high points, x0 remains 0: zA and zB fail their c-side; zC has no initial a=0/b=0 seed so the x1/x2 cycle stays at its least solution 00; p1 has only the f=1 H1 seed and no E seed; p2 has neither root seed. Thus Q covers the two low anchors and avoids all of Z. The separator is nevertheless the constant-size function h(a,b,c,f)=c AND (NOT a OR NOT b).

**What this establishes.** A successful pair list can have a genuine cyclic support SCC whose selected activation order reverses across low anchors. Therefore the phenomenon is not restricted to unsuccessful fragments or abstract equations. But the example's separator has a two-gate implementation, so any lower bound on its rank-layered C-75 witness graph would be irrelevant to minimum separator complexity. This is a concrete warning against path-only non-shareability arguments.

**Limit.** This is a finite toy promise; it does not embed Gap-MCSP, give a lower bound on its cover, or challenge its magnification theorem. Its value is calibration: the direct cyclic game is real, while its static rank layers can still be bypassed by output simplification. Q101 is resolved at the toy level; Q102 asks for the actual-promised hard version.

## 70. C-143 - A q-cycle has quadratic rank layers but a linear separator

The C-142 gadget scales to a single large SCC. Fix q>=4. Let the coordinate set contain a control bit c, seed bits t_1,...,t_q, and L tag bits. Let the high universe Z contain 2q+1 distinct points z_i,p_i (i in [q]) and r. Set c=0 on every z_i,p_i and c=1 on r. Set t_j(z_i)=1 iff j=i, and set every t_j to 0 on every p_i and on r. Choose the tag strings of the 2q+1 high points to be distinct, with each tag-coordinate slice on Z of size q or q+1. Such tags exist: independently choose each tag column uniformly among balanced q-versus-(q+1) splits. A fixed pair collides on one column with probability q/(2q+1)<1/2; L=2 ceil(log2(2q+1))+2 columns separate all pairs by a union bound. Low anchors w_i have c=1, t_i=1, t_j=0 for j!=i; their tag bits can be arbitrary. Thus Y={w_i:i in [q]} is disjoint from Z.

Use one pair for each cycle state i, with p_0=p_q,

    E_i={z_i,p_i,p_(i-1)},       H_i={r,p_i},

and one empty-carrier root pair

    E_0={p_1},                   H_0={p_2}.

All endpoints are subsets of U=Z. The carriers are T_i={p_i} and T_0=empty. E_i contains exactly the state carriers T_i and T_(i-1); H_i contains T_i only. On Z, the only literal slice of size one for t_j is {z_j}, and the only size-one c-slice is {r}; these are distinct from the marker points. The t_j=0 and c=0 slices have size 2q, and every tag slice has size q or q+1. Since |E_i|=3, |H_i|=2, and the root endpoints have size one, no such larger slice is contained in an endpoint. It follows that the only seed in E_i is t_i=1, the only seed in H_i is c=1, and the root pair has no literal seeds.

After dropping self-supports, the least-fixed-point equations are

    x_i=(1_(t_i=1) OR x_(i-1)) AND 1_(c=1),   indices modulo q,
    x_0=x_1 AND x_2.

For low anchor w_j, state j activates first, then j+1, j+2, ..., cyclically; all q cycle states eventually activate and the root activates. The first-activation rank is

    tau_i(w_j)=1+((i-j) mod q),

so every state i attains every rank 1,...,q across the low anchors. For high z_i, the seed t_i is true but c=0, so no state activates. At p_i, c=0 and all seed bits vanish. At r, c=1 but every seed bit vanishes, so the least fixed point of x_i=x_(i-1) is all zero. Hence Q covers Y and avoids all of Z.

The ordinary promise separator is simply

    h=c AND (t_1 OR ... OR t_q),

of fan-in-two size O(q). Yet the direct rank-layer architecture has state rectangles

    R_(i,s)={w in Y:tau_i(w)<=s} x Z.

For each 1<=s<q, the q row sets are distinct cyclic windows of length s; different s have different cardinality. At s=q all q states collapse to the single rectangle Y x Z. Thus this architecture has q(q-1)+1=Theta(q^2) distinct rule/rank rectangles, while an unrelated standard rect-DAG from h has O(q) size. This is an explicit family where rank-layer duplication is not necessary for the separator.

**Scope.** The construction is a successful finite-promise cover, not a Gap-MCSP embedding. It does not prove a lower bound on the minimum rect-DAG or rho; instead it falsifies the use of rank-layer state count as a proxy for either. A real non-shareability theorem must exclude all alternative separators, not only the C-75 witness-path simulation. Q102 remains the actual-promise task.

## 71. C-144 - The q-cycle cover is deletion-minimal but the promise has a one-pair cover

The C-143 construction has an unrecorded stronger shortcut. Write its high universe as

    U = {z_i,p_i : i in [q]} union {r},
    E* = {z_i : i in [q]},    H* = {r}.

Then E* intersect H* is empty. For each low anchor w_i, its t_i=1 slice is exactly {z_i}, contained in E*, and its c=1 slice is exactly {r}, contained in H*. Thus the single pair (E*,H*) derives the empty set on every low anchor.

It does not derive the empty set on any high anchor. For a high point other than r, H* is not in its initial upward family. A matching t_j=1 slice, when present, is the singleton {z_j}, which is distinct from {r}; every matching t_j=0 slice and the matching c=0 slice have size 2q, and every matching tag slice has size q or q+1. The singleton c=1 slice {r} is not matched by these high points. Thus no matching literal slice is contained in H*. At r, H* is present, but E* is not in its initial upward family because every literal slice matching r contains r, while r is excluded from E*. With only one empty-carrier pair there are no intermediate states, so this proves a successful one-pair cover. The empty list fails, hence rho_prom=1 on this toy promise.

The q+1-pair C-143 list is nevertheless deletion-minimal as a list: deleting the root removes every empty-carrier rule; deleting cycle rule i leaves low anchor w_i with no seed at any remaining E-side, so the least fixed point stays zero. Therefore deletion-minimality of a presented Q does not imply minimum cover cardinality, and even a deletion-minimal q-state cyclic SCC can be bypassed by a different endpoint pair.

**Correction and lesson.** C-143 remains a valid counterexample to charging its chosen rank-layer rectangles to the separator computed by that Q. Its stronger comparison is now q^2 path-layer rectangles versus a one-pair optimum, not merely an O(q)-gate separator. This makes the example more decisive as a warning about proof-path lower bounds, but less informative about the structure of a minimum-size cover. Before using cyclic rank diversity as evidence about rho, require either global optimality of Q or a theorem that every successful cover inherits the obstruction. Neither is established. This finite toy gives no Gap-MCSP bound.

## 72. C-145 - Every first-round low activation has a large high-table carrier

This quantifies the two-coordinate shattering obstruction recorded in the closure-game note. Let (M_2=|\mathrm{SIZE}(s_2)|\le 2^{O(s_2\log(s_2+n))}=2^{o(N)}), and (Z=\{0,1\}^N\setminus\mathrm{SIZE}(s_2)). For fixed (\beta<1), every cylinder fixing two distinct truth-table coordinates contains at least (2^{N-2}-M_2) members of Z; a one-coordinate cylinder contains at least (2^{N-1}-M_2).

Take any successful q-pair cover Q and any low anchor w. Since the least-fixed-point iteration starts at zero and eventually activates an empty rule, at least one state i is active at round one: if F_w(0)=0, every later iterate is zero. Thus both endpoint tests at i are seeded by matching literal slices, say (L_{w,k}\subseteq E_i) and (L_{w,\ell}\subseteq H_i). The two literals agree with w, so their cylinder is nonempty and consistent. If kÃ¢â€°Â ell, the intersection (L_{w,k}\cap L_{w,\ell}\) contains at least (2^{N-2}-M_2) high tables; if k=ell, the matching slice contains at least (2^{N-1}-M_2). In either case

    |T_i intersect Z| >= 2^(N-2)-M2,       T_i=E_i intersect H_i.

Moreover, every high table z in that common cylinder matches both literal seeds, so x_i^(1)(z)=1 as well. Therefore every low anchor has a round-one seed state whose carrier contains a constant fraction (at least 1/4-o(1)) of the entire high side, and the same state activates on that high fraction.

**Why this distinguishes OPS from C-143/C-144.** In the finite toy, the two low seeds t_i=1 and c=1 have empty common high cylinder; the seed carrier is the singleton marker p_i. OPS's counting shattering forbids that geometry. In particular no empty-carrier rule can be a round-one seed state, and a toy transfer cannot preserve singleton seed carriers.

**Limit and next invariant.** The lemma is a local coactivation statement, not a q lower bound: high tables may activate nonempty carriers without reaching an empty root. A useful progress measure must track how the high activation region of these large seed states is filtered by later supports, while the low anchor still reaches an empty carrier. The exact task is to charge this high-side shrinkage globally across shared states, accounting for overlaps and multiple seed literal pairs. This adds no improvement to q>=N-o(N) by itself and yields no P-vs-NP result.

## 73. C-146 - Bootstrap cofactors lose a state, but cofactor lower bounds do not sum

**Seed-cylinder restriction lemma.** Fix a successful q-state Q and a low anchor w. By C-145, some state i activates in round one from matching literal slices on its two sides, at coordinates k and ell. Let C be the subcube of anchor tables matching those one or two literals. On every anchor v in C, those same restricted literal slices are contained in E_i and H_i, so x_i(v)=1 at round one. C-145 also shows T_i is nonempty, hence i is not an empty-output state. Restrict the activation recurrence of Q to C and substitute x_i=1 wherever state i supports another rule. The restricted separator now has only q-1 AND/intersection states. This is a statement about the induced recurrence; it does not automatically give a q-1 fusion cover on the restricted high universe, because restricting the universe can create new endpoint-containment relations.

**Why summing this over cylinders fails.** Let the finite promise have r-bit tables, low side Y={e_j: j in [r]} (the weight-one vectors), and high side Z={0,1}^r minus Y. For r>=4, Z contains a point in every two-coordinate cylinder. The exact-one predicate has a monotone dual-rail separator with O(r) ANDs: compute prefix and suffix conjunctions of zero rails, then OR the r terms that select one positive rail and zeros everywhere else. The standard cyclic-intersection conversion gives rho=O(r). Conversely, for a fixed low e_j, any proper coordinate cylinder matching e_j has a high completion, so its one-anchor literal certificate needs all r coordinates; the local closure bound gives rho>=r-1. Hence rho=Theta(r).

For every pair of coordinates fixed to 00, the restricted low side is again the weight-one promise on the other r-2 bits, so that cofactor still has cover complexity at least r-3. There are binom(r,2) such cofactors, while the global cover has only O(r) pairs. Thus even many dense, individually hard cofactors cannot be summed without a direct-sum theorem; one shared construction can serve them all. This finite example also shows that C-145's high-side density and cofactor drop alone cannot imply a superlinear bound. The missing ingredient must use structure specific to Y=SIZE(s1), Z=SIZE(s2)^c, or a proven constraint on how one state can serve different cofactors.

## 74. C-147 - Re-entry audit for the shared-DAG phase

This checkpoint follows the current user direction and preserves the existing frontier; it is not a new lower bound. The requested relation/model comparison, cover-to-DAG and reverse maps, description-space test, universal pattern-DAG attempt, and tree-versus-DAG calibration were already developed in C-78--C-123 and C-139--C-146. The fresh audit below checks the model boundaries against primary definitions and marks what is still open.

### Exact search objects

For plain signed mismatch, Alice has w in Y=SIZE(s1), Bob has z in Z={0,1}^N minus SIZE(s2), and an output (k,b) is valid exactly when w_k=b and z_k=1-b. This relation is total because Y and Z are disjoint; Q is irrelevant to its totality. The Q-witness relation additionally returns the empty-carrier starting rule, each selected side and support, and the terminal literal mismatch. The activation-rank argument makes that relation total exactly when Q covers every low anchor. These are different search relations and have different protocol costs.

### Literature/model boundary confirmed

Sokolov's Boolean communication game is an acyclic graph of out-degree at most two. Each vertex uses separate local predicates on Alice's and Bob's inputs, so its valid set is a rectangle and each valid parent pair continues to a child. Those local predicates are not charged as graph vertices. This free-local-computation convention is why replacing a truth table by a circuit description cannot itself shrink standard game size.

Garg--Goos--Kamath--Sokolov's rectangle-DAGs are likewise acyclic rectangle games; their lifting theorems concern specified composed search relations and do not automatically yield a lower bound for this Gap-MCSP promise. Cavalar--Oliveira identify the fusion cover exactly with their cyclic intersection complexity, not with an acyclic rect-DAG. Nakayama--Maruoka's loop-circuit identity is for their generalized approximation model and its functionals; Cavalar--Oliveira explain why that result does not directly establish the semi-filter cover identity. Amano--Maruoka count AND gates in acyclic monotone circuits and study quadratic functions. These are relevant analogies or neighboring models, not interchangeable definitions.

### Quantitative transfer, with losses visible

The native identity is q=rho_prom=D^circ_cap. A successful Q yields q activation rectangles and a cyclic, pairwise terminating witness graph with O(q^2+qN) possible support arcs. Pairwise termination follows from decreasing first-activation rank, but the static graph can cycle; therefore q vertices do not yet form a standard rect-DAG. The best general acyclic binary-DAG compilation currently recorded is S_rect=O(q^3/log q), with sharper bounds only for structured support systems. Conversely an L-vertex mismatch rect-DAG gives a promise separator circuit and a cover of size O(L). Thus

    rho_prom <= SepCirc(Y,Z) = Theta(S_rect) <= O(rho_prom^3/log rho_prom).

A direct cyclic lower bound rho_prom>N^(1+epsilon) meets the target. A standard rect-DAG lower bound must be asymptotically above N^(3+3epsilon)/log N to imply it through the present compiler. Merely proving S_rect>N^(1+epsilon) is insufficient for this transfer, though a rect-DAG of N^(1+o(1)) size would give a near-linear upper bound on rho_prom and kill the superlinear-cover route.

### Description-space and universal-DAG audit

For any surjection G:D->Y, a standard rect-DAG for the relation on descriptions D x Z has exactly the same minimum size as one on Y x Z: lift each row predicate by composition with G, and in the reverse direction restrict along a section sigma:Y->D. This is an equality because the model leaves local predicates uncharged. A universal circuit evaluating G(d)_k only computes an Alice-local bit; it does not make the joint mismatch predicate a rectangle. If local-predicate computation were charged, that would be a different DAG model, and no q-to-that-model transfer is established.

The best explicit generic pattern-sharing construction remains O(|Y|+sum_I pi_I(Y)) over dyadic intervals and row restrictions; the description-enumeration tree is O(N 2^ell), ell=O(s1 log(n+s1)). Neither gives N^(1+o(1)) for the full low-circuit class. C-137 proves the fixed-order scan repair needs exponentially many prefix contexts for k=Theta(s1/n), while C-110 explains the product-hull condition any legal state merge must preserve. These results kill syntax-only and prefix-forgetting shortcuts, not every possible adaptive shared DAG.

### Active frontier

No small universal DAG or OPS-specific arbitrary-DAG non-shareability theorem is known in this project. Do not infer a lower bound from rank layers, one-state-per-anchor counts, raw excluded-column volume, or cofactor sums: C-130, C-132, C-143/144, and C-146 already falsify those shortcuts. Continue on (i) a direct lower bound for the cyclic closure states, (ii) a separator/rect-DAG lower bound at the quantitative scale above, or (iii) an explicit N^(1+o(1)) universal DAG, which would refute the hoped-for superlinear rho route. No P-vs-NP proof or new superlinear bound was obtained in this checkpoint.

Primary sources checked: [Sokolov, Dag-like Communication and Its Applications](https://eccc.weizmann.ac.il/report/2016/202/download); [Garg et al., Monotone Circuit Lower Bounds from Resolution](https://theoryofcomputing.org/articles/v016a013/v016a013.pdf); [Cavalar--Oliveira, Boolean Circuit Complexity and Two-Dimensional Cover Problems](https://arxiv.org/abs/2503.14117); [Nakayama--Maruoka, Loop Circuits and Their Relation to Razborov's Approximation Model](https://doi.org/10.1006/inco.1995.1083); [Amano--Maruoka, The Monotone Circuit Complexity of Quadratic Boolean Functions](https://doi.org/10.1007/s00453-006-0073-0).

## 75. C-148/C-149 - Local-PRG formula bound adapts only above the parameter floor

This is a proved restricted-model consequence, not a new general circuit or fusion lower bound.

### Promise-separator lemma

Fix 1/3<beta<1 and the OPS thresholds s1=N^beta/(c n), s2=N^beta, with N=2^n and c>0 fixed. Let h be any Boolean function on N truth-table bits satisfying h(w)=1 for every w in Y=SIZE(s1) and h(z)=0 for every z in Z={0,1}^N minus SIZE(s2); h is unrestricted on the medium band. If h has a De Morgan formula of size t, then

    t >= s1^(3-o(1)) = N^(3 beta-o(1)).

**Proof.** The source's local-PRG lemma is stated for formula size t>=N and gives locality lambda(t)=t^(1/3)2^(O((log t)^(2/3))). If t<N, pad h to size N. Since beta>1/3, lambda(N)=N^(1/3+o(1))<s1, so this padded formula would accept every generator output and reject a uniform table with probability 1-2^(-N+o(N)), contradicting fooling. Thus t>=N. For N<=t<=N^3, apply the lemma at size t: if lambda(t)<=s1, the same promise-separation contradiction follows. Rearranging lambda(t)>s1 gives t>=s1^(3-o(1))=N^(3 beta-o(1)). If t>N^3, this lower bound already holds because beta<1. A uniform table lies in SIZE(s2) with probability at most |SIZE(s2)|/2^N=2^(-N+o(N)); arbitrary medium-band labels therefore do not affect the argument.

**C-149 parameter-floor correction.** The earlier C-148 draft stated this for every 0<beta<1; that was too broad. The cited source only supplies the formula PRG for t>=N. At beta<=1/3 its locality at t=N is N^(1/3+o(1)), which is not at most s1=N^beta/(c n), so the proof cannot be initiated by padding a smaller separator. No lower bound N^(3 beta-o(1)) for beta<=1/3 follows from this cited lemma. This is the small-beta regime relevant to OPS magnification, so C-148/C-149 is outside the active parameter range and gives no project-target progress.

The argument explicitly handles the promise: the medium band has uniform probability at most |SIZE(s2)|/2^N and may be labeled arbitrarily. It does not assume h computes exact SIZE membership.

### Why this does not improve the target

For beta>1/3 this gives a promise-specific formula bound, but it lies outside the sufficiently small-beta magnification range. For beta<=1/3 this argument gives no bound. At every beta, formula/tree size does not lower-bound rect-DAG/circuit size: DAG sharing can reduce size, and no near-lossless formula-to-DAG lower-bound transfer is available. The q-cover compiler gives a separator DAG/circuit of O(q^3/log q), not a formula of comparable size. Thus C-148/C-149 gives no lower bound on S_rect or rho_prom. It confirms that ordinary KW bit complexity and tree/formula size are separate from the shared-state resource.

### Recent-literature scope check

The 2026 ECCC work on ImpMCSP studies an implicit sample-distribution input and conditional half-Levin hardness under cryptographic/proof-complexity assumptions; the 2026 Pessiland paper studies average-case approximation of description length; and the 2025 learning/witness-encryption work concerns learning reductions and related promise variants. These results do not prove a lower bound for the explicit truth-table promise separator S_rect or for D^circ_cap. They remain useful conditional/meta-complexity context, not transfers to this shared-DAG target.

Primary source for the formula/PRG method and its t>=N hypothesis (Lemma 17): [Cheraghchi, Kabanets, Lu, and Myrisiotis, Circuit Lower Bounds for MCSP from Local Pseudorandom Generators](https://eccc.weizmann.ac.il/report/2019/022/revision/1/download/). Adjacent recent sources: [Goldberg, Juvekar, and Kabanets (2026), Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions](https://eccc.weizmann.ac.il/report/2026/091/download/); [Hirahara and Nanashima (2026), A Sharp Characterization of Pessiland](https://eccc.weizmann.ac.il/report/2026/052/download/); [Goldberg and Kabanets (2025), Witness Encryption and NP-hardness of Learning](https://eccc.weizmann.ac.il/report/2025/070/download/).

## 76. C-150 - First-excluded activation state is already a literal witness, but its scan is not a shared rect-DAG

Let a successful q-pair cover have the least-round activation recurrence

    x_i^(t+1)(w) = (a_i(w) OR OR_{j in A_i} x_j^t(w))
                     AND (b_i(w) OR OR_{j in B_i} x_j^t(w)),

where A_i indexes carriers T_j contained in E_i and B_i those contained in H_i; T_i=E_i intersect H_i. Let tau_i(w) be the first round when x_i becomes 1, or infinity if it never activates. For each low w, success means some empty-carrier state activates. For each high z, define

    i*(w,z) = argmin { (tau_i(w), i) : tau_i(w)<infinity and z notin T_i },

with lexicographic tie-breaking. The set is nonempty because an active empty carrier omits every z.

**Lemma (first-excluded state).** The endpoint E_i or H_i missed by z at i=i*(w,z) is seeded by a matching literal of w, not by an earlier carrier. For example, if z notin E_i and E_i were supported by T_j subset E_i at its first activation, then tau_j(w)<tau_i(w) and z notin T_j, contradicting minimality. Therefore the E_i side is seeded by a literal slice L_(k,w_k) subset E_i. Since z notin E_i, z_k differs from w_k. The H_i case is symmetric. Thus every successful Q defines a canonical mismatch selector: sort active rules by (tau_i(w),i), and the first carrier not containing z directly certifies a differing coordinate. This removes the need to follow the support path for this selector.

**Attempted compression.** A natural protocol scans the row-dependent activation order and continues past i only when z is in T_i. After t checks, its exact continuation relation is

    R_t = { (w,z) : w in W_t and z in P_t(w) },
    W_t={w: sigma_w has at least t active rules},
    P_t(w)=intersection_{r<=t} T_(sigma_w(r)),

where sigma_w is the sorted list of active rules. In general P_t(w) varies with w, so R_t is a union of row-specific rectangles, not necessarily one rectangle. Already at the first check, let A_i be the rows whose first active state is i. The continuation pieces A_i x (Z intersect T_i) need not have a rectangular union. Merging them at a common next state requires a rectangle containing their product hull; the hull can add cross-pairs whose current candidate already omits z. A continuation that tests only the next candidate is not shown to handle those pairs: they may need the earlier literal witness recomputed. Thus the one-node-per-round shortcut has no rectangular-correctness proof as stated. Keeping candidate identity and round gives up to q^2 contexts; adding all candidate/seed-output routers can restore the known cubic-scale construction. A more structured factorization may still exist, but this scan alone does not improve the q-to-DAG bound.

**Finite stress test using C-142.** On that legal three-rule toy, the first-active continuation rectangles include {wA} x {p1} and {wB} x {p2}; their hull adds (wA,p2) and (wB,p1). For (wA,p2), the first state T1={p1} is already missed, but a scan that skips it reaches T2={p2} and then the empty root. The root's missed endpoint E0={p1} is supported by T1, not by a literal, so the skipped candidate's seed witness has been lost. The symmetric cross-pair behaves analogously. This concretely falsifies the one-node-per-round scan on a successful fusion instance. However, the same toy has a one-pair alternative cover E*={zA,zB}, H*={zC}; it covers both lows by their a=0/b=0 and c=1 slices and avoids every high point. Thus the stress test exposes a real merge failure but gives no lower bound on the optimum cover or minimum DAG.

**Research value and limit.** The rank scan isolates a candidate non-shareability statistic: the rectangle-cover complexity of the incidence relation (w,z) with z in P_t(w), jointly over t. Large complexity would obstruct this particular canonical router. It would not lower-bound the minimum S_rect unless every valid separator were forced to preserve these residual intersections; C-143/144 already warn that another separator can bypass a chosen Q. No OPS lower bound on these residual relations, improved compiler, or rho bound follows. Continue O-121 with this as a candidate path-specific obstruction, and keep the existing quantitative transfer rho_prom<=S_rect<=O(rho_prom^3/log rho_prom) explicit.

## 77. C-151 - Canonical-witness hardness can vanish under output projection

This finite communication example isolates why C-150's canonical first-missing state is not automatically a lower bound on the ordinary mismatch search.

Fix k>=2. Alice's input is A_S=[k] minus S and Bob's input is B_T=T union {k}, where S,T range over all subsets of [k-1]. Every cross-pair has a nonempty intersection,

    A_S intersect B_T = {k} union (T minus S).

Consider the unique-output relation whose answer is the least element of A_S intersect B_T. On each diagonal pair (A_S,B_S), the unique answer is k. For distinct S,T, at least one of T minus S and S minus T is nonempty, so at least one cross-pair (A_S,B_T) or (A_T,B_S) has answer below k. A rectangle leaf labelled k cannot contain two diagonal pairs: containing both forces it to contain both cross-pairs, one of which has a different unique answer. Hence any rectangle-DAG with rectangular correctness has at least 2^(k-1) distinct k-labelled leaves.

Now project away the canonical requirement and ask for any common element of A_S and B_T. The answer k is valid on every input pair, so one rectangle leaf solves the entire search problem. Thus an exponential lower bound for a canonical selector can coexist with a trivial solution to the underlying multivalued search problem. A weak stage-by-stage scan also uses O(k) control states if it is allowed to merge nonrectangular reachability histories; the rect-DAG lower bound is precisely about the rectangle-hull requirement.

**Implication for C-75/C-150.** Encoding the first carrier missed by z, or its activation rank, as an output may create hard selector relations, but signed mismatch accepts any differing coordinate. C-142/143 are project-specific instances of the same danger: a complicated selected Q path can be bypassed by another separator or cover. To transfer a selector lower bound, one must either make the selector recoverable from every valid mismatch output or prove that every separator preserves the hard contexts.

There is also a direct encoding obstruction. No pair of binary codewords r(0),r(1) for Alice and c(0),c(1) for Bob can make coordinate mismatches occur only on input pattern (1,1): requiring equality on (0,0), (1,0), and (0,1) forces r(0)=c(0)=r(1)=c(1), so (1,1) also has no mismatch. Thus a coordinate-by-coordinate encoding of an AND/set-intersection witness into mismatch labels cannot solve the projection problem; a successful transfer needs a nontrivial gadget or global promise structure. This is a model calibration, not an OPS lower bound.

## 78. C-152 - Exact calibration of selector transfer across output fibers

C-151 gives a quantitative model test. For its unique-minimum relation, every rect-DAG needs at least 2^(k-1) leaves labelled k, one per diagonal pair. A deterministic protocol has at least that many leaves and hence at least k-1 bits; Alice can send S in k-1 bits and Bob can return the minimum index in ceil(log k) more bits. Thus deterministic communication is Theta(k), and the minimum rect-DAG and protocol-tree sizes are 2^(Theta(k)) (the protocol tree gives an O(k 2^k) upper bound). For the projected relation accepting any common element, the constant answer k is valid everywhere: communication is zero and the DAG has one leaf. The difference is caused by the output relation, not by a change in inputs.

Here is a precise transfer test. Let R(x,y) be a multivalued search relation and h(x,y) a canonical selector. If a rect-DAG solving R has the property that h is constant on every reachable leaf rectangle, relabel each leaf by that constant; this gives an h-DAG of exactly the same size. A sufficient condition independent of the particular DAG is a decoder g on output labels with g(a)=h(x,y) for every valid output a in R(x,y). C-151 violates this condition: the valid label k occurs on every pair, while the minimum common element varies. Therefore a lower bound for h transfers only after proving that every valid-output solver can be made h-homogeneous at its leaves, or establishing another explicit reduction; canonicality by itself is insufficient.

Applied to C-150, the closure scan outputs a state/literal witness, whereas the Gap-MCSP relation accepts a signed differing coordinate. The current relation does not require the carrier index, so the selector lower bound has no established decoder into mismatch labels. This is a concrete proof obligation for O-123, not evidence that such a decoder or a hard subrelation exists. C-151 is a calibration example, not an OPS lower bound.

**Loop-model boundary.** The above counts concern standard acyclic rectangle-DAGs and protocol trees. A cyclic/loop model can inherit the leaf argument only if its terminal reach sets are rectangles and its output semantics preserve those sets. No such equivalence with the C-74 least-fixed-point closure has been proved here; do not transfer the 2^(Theta(k)) DAG count to loop circuits by name alone.

## 79. C-153 - C-142 contains a valid mismatch leaf that mixes selector fibers

Use C-142's successful toy, with lows wA=(0,1,1,0), wB=(1,0,1,0), carriers T1={p1}, T2={p2}, and first-activation orders 1,2 on wA and 2,1 on wB. For either low, coordinate c is 1; on both high columns p1=(1,1,0,1) and p2=(1,1,0,0), c is 0. Hence the whole rectangle {wA,wB} x {p1,p2} has the same valid signed mismatch output c.

The C-150 first-excluded-state selector on this rectangle is

    selector       p1   p2
    wA              2    1
    wB              2    1

For wA, T1 contains p1 but omits p2; for wB, T2 contains p2 but omits p1. A rect-DAG can route this entire product rectangle to a c-labelled leaf, since all four pairs disagree on c. Thus that leaf is selector-mixed. Extend it to a solver for the full finite toy by first branching on Bob's predicate z in {p1,p2}, outputting c on this rectangle, and solving the remaining finite pairs by an identity-enumeration tree. The full finite mismatch relation therefore has a valid solver with a leaf that is not C-150-selector-homogeneous.

This falsifies the generic Ã¢â‚¬Å“all valid leaves reveal the canonical stateÃ¢â‚¬Â transfer, even for a successful fusion cover; no global decoder from the signed mismatch label c to the selected carrier can work on this toy. It does not show that every solver has mixed leaves, does not embed OPS/GAP-MCSP, and gives no S_rect or rho lower bound. Retire O-123's generic form. Any surviving transfer must exploit a property specific to the OPS promise or a chosen restricted subrelation; otherwise keep research effort on O-121's full separator question rather than charging this selector.

## 80. C-154 - Colourful-sunflower lifting is a strong adjacent DAG theorem, but lacks an OPS reduction

A fresh primary-source audit found [Lifting with Colourful Sunflowers (CCC 2025)](https://drops.dagstuhl.de/storage/00lipics/lipics-vol339-ccc2025/html/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.html). Its Theorem 11 states that for a search relation S:Sigma^n->O of subcube-DAG width w(S), every triangle-DAG (hence every rectangle-DAG) solving S composed with the m-bit Index gadget has size at least

    ( m / (A |Sigma| w(S) log(mn)) ) ^ w(S)

for an absolute constant A. The paper defines rectangle-DAG nodes as combinatorial rectangles, fan-out two, with child coverage and valid-output leaves. This is the right general kind of shared-state lower bound: it escalates a hard CSP search relation to a very large acyclic DAG lower bound. Its applications use reductions from lifted CSP search to monotone Karchmer-Wigderson/clique-colouring relations.

**Attempted transfer to the project.** A candidate reduction would map Alice's lifted input x to a low table alpha(x) in Y=SIZE(s1), Bob's input y to a high table beta(y) in Z=SIZE(s2)^c, and convert a mismatch output coordinate into a constraint falsified by the composed assignment Ind_m^n(x,y). The pullback of each rectangle under alpha x beta remains a rectangle, so a valid output-preserving reduction could transfer DAG size with little graph overhead. The missing condition is the output map: every leaf rectangle of the pulled-back mismatch DAG must have one CSP constraint falsified on all its source pairs, or a bounded-size rectangle-preserving decoder must refine it. Merely knowing that alpha(x) and beta(y) differ somewhere is not enough.

A stringent sufficient condition for a coordinate-only decoder is that, for every source pair, the entire mismatch support of alpha(x) and beta(y) be nonempty and consist only of coordinates encoding constraints violated by that pair. No such maps are known. C-151's local recoding obstruction and C-153's selector-mixed mismatch rectangle warn that pointwise embeddings can fail, but they do not prove a general impossibility; a global gadget or a different promise restriction remains possible. One must also verify table-length and circuit-class cardinalities for alpha and beta.

**Quantitative gate.** If an explicit reduction gave a lifted lower bound L and a DAG-size overhead r, it would imply S_rect>=L/r. Through the current q compiler, a lower bound intended to prove rho_prom>N^(1+epsilon) must satisfy L/r asymptotically above N^(3+3epsilon)/log N, unless the reduction reaches the cyclic cover directly. C-154 supplies no such reduction or OPS bound yet. The next bounded task is to construct the maps and output decoder or prove a specific obstruction; do not cite the lifting theorem alone as P-vs-NP progress.

## 81. C-155 RETRACTED - Partial Index search does not impose equality off its domain

The previous C-155 argument incorrectly required Alice and Bob codewords to agree whenever y_x=0. For SearchOR composed with Index, those pairs have no valid output; they are outside the partial relation's domain. A reduction on the legal promise is unconstrained there, so the all-zero-string argument does not apply.

There is a direct counterexample. On the legal domain D={(x,y): y_x=1}, whose only valid output for the one-block SearchOR relation is index 1, take a(x)=0^m and b(y)=y. Every legal pair has a mismatch at coordinate x; every mismatching coordinate may be decoded to the sole valid output 1. Thus a coordinatewise mismatch encoding exists on this partial promise. C-155's claimed impossibility is false and is withdrawn.

This correction matters for C-154: its CSP application uses an unsatisfiable CSP, whose falsified-constraint search relation is total, so the composed source relation has every lifted pair in its domain. Any no-go must use valid outputs on all pairs, rather than impose equality on invalid pairs of a partial toy. The next useful step is to characterize exactly which total search relations admit direct party-separable mismatch encodings.

## 82. C-156 - Exact cut-cover criterion for direct coordinatewise mismatch encodings

Let R(x,y) be a total two-party search relation. A length-r direct mismatch encoding consists of partywise bit maps a:X->{0,1}^r and b:Y->{0,1}^r and a fixed decoder delta(t,u,v) for u!=v. For each coordinate t and bit u, write X_t^u={x:a_t(x)=u} and Y_t^u={y:b_t(y)=u}. The mismatch labels at coordinate t occur on exactly two product rectangles:

    X_t^0 x Y_t^1    labelled delta(t,0,1),
    X_t^1 x Y_t^0    labelled delta(t,1,0).

Therefore such an encoding is valid if and only if (i) these oriented rectangles cover X x Y, and (ii) each rectangle is monochromatic-valid: its decoder label belongs to R(x,y) for every pair in that rectangle. The forward direction follows by expanding bitwise inequality; the reverse direction builds a_t,b_t from the specified row/column cuts. Empty rectangles can be ignored.

This reframes O-124's simplest possible transfer as a paired cut-cover problem: every source pair must lie on a mismatch side, and both sides of each cut must carry outputs valid throughout. A plain rectangle cover of the CSP search relation is not enough, because one mismatch coordinate creates both complementary cross-rectangles. This criterion concerns only fixed-label coordinatewise encodings; input-dependent decoders require a separate rectangle refinement and an explicit size charge. It supplies a concrete next target but no lifted-CSP or OPS bound by itself.

## 83. C-157 - A cyclic mismatch router collapses without a progress rule

I tried to build the strongest possible universal shared router from the fact that every promised pair has at least one differing coordinate. Let the output labels be t=(i,b) in [N] x {0,1}; let M_t be the rectangle of pairs with w_i=b and z_i=1-b. Form 2N internal vertices v_t, each carrying the full rectangle Y x Z, with two outgoing edges: one to a leaf labelled t and one to the next internal vertex in cyclic order. For every (w,z), some M_t contains it, so the graph has a finite path to a valid output. It uses O(N) vertices and O(N) edges.

This is not an acyclic rect-DAG. More seriously, every pair also has an infinite path that always takes the continuation edge. If a cyclic search object is accepted merely when some finite valid path exists, then the construction trivializes every total relation with a nonempty output set at every input: cycle through all labels and allow a valid leaf whenever its label works. That semantics has no meaningful termination guarantee. Requiring all paths to terminate, or requiring an input-dependent strategy with a decreasing well-founded potential, rejects this construction. C-139's fusion graph has the needed pair-specific rank decrease; the root-loop does not.

There is a second semantic failure if the loop is presented as an activation circuit on input pairs: its least-fixed-point equations accumulate mismatch rectangles using both parties' bits. That is a pairwise reachability computation. C-74 instead requires each state to be one set of single-table anchors, generated by legal literal seeds and endpoint-containment supports; its cross-party rectangle is then derived from that one-sided set. Replacing those states by pairwise mismatch predicates assumes the joint search computation that the reduction is supposed to obtain, and gives no legal fusion pair list. This pinpoints why cycles alone do not establish reusable closure states.

## 84. C-158 - Binary rectangle coverage forces a full-side child

Let a node rectangle A x B be covered by two child rectangles (A_0 x B_0) and (A_1 x B_1); children need not be subsets of the parent. Intersect each child with the parent, which preserves rectangularity and coverage. If A is not contained in A_0, choose a in A minus A_0. For every b in B, (a,b) must then lie in the second child, so B is contained in B_1. Therefore either A is contained in A_0 or B is contained in B_1. In particular, some child preserves a full parent projection.

The stronger exact trichotomy is: at least one of (i) A is contained in A_0 intersect A_1; (ii) B is contained in B_0 intersect B_1; or (iii) A x B is contained in one child rectangle. For proof, assume (i) fails and choose a outside A_0 (renaming children if needed). Coverage forces B to be contained in B_1. If (ii) also fails, choose b outside B_0. Coverage of every (a',b) then forces A to be contained in A_1, so the whole parent lies in child 1, giving (iii). This is the AND/OR/copy case analysis used to reconstruct a circuit from a Boolean communication game.

This also gives a local deterministic routing rule. In the first case, Bob chooses child 0 when b is in B_0 and child 1 otherwise; coverage guarantees child 1 contains every relevant row for the latter columns. In the second case, Alice uses the symmetric rule. Thus a standard binary Boolean communication game has a one-party local selector at every state. This does not remove state-reuse difficulty: the next residual rectangle can still depend on the selected party and prior path, and the same graph vertex can be reached from different histories.

**Literature check.** This trichotomy is not a new lemma: it appears explicitly in Sokolov's proof that Boolean communication games and circuits have equivalent size, where the three cases yield AND, OR, or copying a child function ([Theorem 3.2](https://eccc.weizmann.ac.il/report/2016/202/download)). The project-specific conclusion is only that the full-side observation cannot by itself supply a new non-shareability bound; its remaining use is as a local invariant to combine with C-129.

### Exact C-75 relation and current complexity bounds

The total relation is Mis(w,z)={(i,b): w_i=b and z_i=1-b}, for w in Y=SIZE(s1) and z in Z={0,1}^N minus SIZE(s2). Alice knows only w (or a circuit description of w); Bob knows only z; an output is valid exactly when it is a signed mismatch. Totality follows from s1<s2. The stricter Q-witness relation additionally reports the active empty-carrier start, side/support choices, and terminal mismatch; it is total only when Q is a successful cover.

| Object | Bound established in the project | What the bound says |
|---|---:|---|
| Fixed-output deterministic communication bits for Mis | n-o(1) <= D_cc^leaf <= O(s1 log(s1+n)+n)=O(N^beta) | Upper: Alice sends a circuit description and Bob returns a mismatch index. Lower: fixing w=0, any high z needs a 1 among the output coordinates reachable from that row; fewer than N-log2|SIZE(s2)| coordinates have a high completion with zeros on all of them. |
| Ordinary protocol-tree vertices | N-o(N) <= S_tree <= 2^(O(N^beta)) | The lower bound is the same fixed-row output-label argument. The upper bound is the circuit-description protocol tree. These are size bounds, not interchangeable with bit complexity. |
| Standard acyclic rect-DAG vertices | N-o(N) <= S_rect <= min(2^(O(N^beta)), O(q^3/log q)) | The lower bound counts distinct output labels reachable from w=0. The first upper bound is the protocol tree; the second is the current q-cover compiler. No N^(1+o(1)) construction or superlinear lower bound is known. |
| Q-dependent ranked cyclic rectangle graph | q rule states plus 2N output leaves; O(q^2+qN) possible arcs; each pair's selected path terminates | Exact cover-to-loop transformation: first-activation rank strictly decreases on each support transition. The static graph may cycle, so this is not an acyclic rect-DAG. |

The reverse acyclic map remains rho_prom<=O(S_rect), while the general forward map is S_rect=O(q^3/log q). Hence an S_rect lower bound must exceed N^(3+3epsilon)/log N to force q>N^(1+epsilon) by this compiler; a direct cyclic q lower bound avoids the loss. C-158 is only a local structure lemma. C-130/C-132 show why excluded-column charges can still overlap or pass through a filtered child, so O-126 remains open.

The communication row uses the fixed-output leaf convention of Boolean communication games. If a variant lets one party compute the final label from its private input, sending that label to both parties costs at most an additional log(2N) bits; the fixed-row leaf-count lower bound is not automatically a lower bound for the one-sided-output variant after paying that conversion cost.



## 85. C-159 - The rectangle trichotomy is already Sokolov's circuit reconstruction

I checked the primary definition and proof rather than treating C-158 as novel. In Sokolov's Boolean communication game, every node is a rectangle, a valid node's rectangle is covered by at most two child rectangles, and the graph is acyclic. His proof of Theorem 3.2 establishes the exact trichotomy: for parent A x B and children A_0 x B_0, A_1 x B_1, at least one holds: A is contained in both A_0,A_1; B is contained in both B_0,B_1; or the parent rectangle is contained in one child. The proof maps these cases to an AND gate, an OR gate, or copying the child function. C-158's full-side lemma is a weaker corollary.

For the promise mismatch relation, the same induction gives a separator circuit: a signed-mismatch leaf yields a literal that is 1 on its row side and 0 on its column side; the three internal cases combine the child separators by AND, OR, or copying. This recovers the existing O(S_rect)-size separator conversion and explains why uncharged local predicates do not trivialize the graph: the number and reuse pattern of rectangle states still determine circuit size.

**Research consequence.** C-158 is a known structural decomposition, not a new non-shareability lemma. Its possible value is only through a quantitative argument that sums or otherwise charges gate/state reuse across the C-75 DAG. C-130's overlapping excluded columns and C-132's all-row filtered child still defeat the direct local-charge attempts. No new bound on S_rect, rho_prom, or P versus NP follows. Primary source: [Sokolov, Theorem 3.2 proof](https://eccc.weizmann.ac.il/report/2016/202/download).

## 86. C-160 - Cylinder statistics and local richness do not force a superlinear DAG

This is a calibration against a *generic* globalization of C-129, not a model of the actual circuit-complexity promise.

Fix N=2^n, a constant beta in (0,1), and set a=floor(N^beta/n), b=floor(N^beta). Let

\[
Y_a=\{x\in\{0,1\}^N:|x|\le a\text{ or }|x|\ge N-a\}.
\]

Define the high side by the middle Hamming band.

\[
Z_b=\{x:b<|x|<N-b\},
\qquad W_b=\{0,1\}^N\setminus Z_b.
\]

The Hamming-ball estimate gives \(\log_2|Y_a|=\Theta(a\log(N/a))=\Theta(N^\beta)\), and \(\log_2|W_b|=\Theta(b\log(N/b))=\Theta(N^\beta n)\). These match the low and non-high counting scales used in the OPS setting.

The standard local facts all hold:

1. Every bit pattern on any coordinate set of size at most \(a\) extends to a row of \(Y_a\), by setting all unspecified bits to zero. In particular, this includes the smaller restriction scale \(\Theta(s_1/n)=\Theta(N^\beta/n^2)\) from C-133.
2. Every \(w\in Y_a,z\in Z_b\) has Hamming distance at least \(b+1-a=\Theta(N^\beta)\), which is at least the OPS patching-gap scale.
3. For any fixed coordinate set \(S\), if \(2^{N-|S|}>|W_b|\), every cylinder fixing \(w|_S\) contains a member of \(Z_b\). This is the completion premise behind C-129.
4. The radius-\(a\) Hamming neighborhood of \(Y_a\) lies inside \(W_b\): changing at most \(a\) bits moves a sparse row to weight at most \(2a\le b\), or a dense row to weight at least \(N-2a\ge N-b\). This matches the coarse patch-stability fact used for the OPS promise.
5. The complement of every row in \(Y_a\) is in \(Y_a\), and \(W_b\) contains every coordinatewise Boolean recombination of \(r\le\lfloor b/a\rfloor=\Theta(n)\) rows from \(Y_a\). To see this, write each row \(w_i\) as within Hamming distance \(a\) of a default constant \(d_i\in\{0,1\}\); the union \(D\) of their minority-coordinate sets has size at most \(ra\le b\). Outside \(D\), the vector \((w_1(j),\ldots,w_r(j))\) is the same default vector \(d\). For any Boolean map \(g:\{0,1\}^r\to\{0,1\}\), the recombination \(u_j=g(w_1(j),\ldots,w_r(j))\) is therefore equal to the constant \(g(d)\) outside \(D\), so \(u\) is within distance \(b\) of all-zero or all-one and belongs to \(W_b\). This is stronger than the circuit-class fact that composing \(r=\Theta(n)\) size-\(s_1\) circuits with a Boolean circuit \(g\) of size fitting the remaining \(s_2-rs_1\) budget produces a non-high table.
6. Every valid binary rectangle DAG obeys Sokolov's AND/OR/copy trichotomy, and every node obeys the corresponding C-129 excluded-column inequality with \(|W_b|\) in place of \(|\mathrm{SIZE}(s_2)|\).

Despite these properties, the separator \(h(x)=1[|x|\le a\text{ or }|x|\ge N-a]\) is computable by a fan-in-two circuit of size \(O(N\log N)\): count the input ones and compare with the two thresholds. It is 1 on \(Y_a\), 0 on \(Z_b\), and its medium-band values are allowed. The circuit-to-rect-DAG correspondence therefore gives \(S_{\rm rect}(Y_a,Z_b)=O(N\log N)=N^{1+o(1)}\); the established reverse conversion gives the analogous active fusion number \(\rho_{\rm prom}(Y_a,Z_b)=O(N\log N)\).

**Consequence for O-126.** No argument using only class cardinalities, large-cylinder completion, low-row projection richness, Hamming separation and patch stability, complement symmetry, closure under arbitrary coordinatewise Boolean recombination of \(\Theta(n)\) low rows into the non-high band, C-129's local volume inequality, and Sokolov's local gate trichotomy can prove a superlinear DAG lower bound in general: these data coexist with this near-linear separator. A successful OPS-specific state-reuse theorem must use finer structure of the actual low/high *circuit-complexity* classes, or work directly with cyclic closure semantics. This calibration neither constructs a small DAG for actual Gap-MCSP nor weakens a possible OPS-specific lower bound. It rules out several statistics-only versions of O-126 and records no superlinear bound or P-vs-NP result.

## 87. C-161 - Even a balanced affine low family has a near-linear separator

C-160's low rows mostly lie near the two constant tables. To test whether balanced low functions alone change the state-reuse picture, enlarge that calibration by all affine truth tables and include their patch neighborhoods among the non-high tables.

Let \(\mathrm{Aff}_n=\{x\mapsto c+\ell\cdot x:c\in\mathbb F_2,\ell\in\mathbb F_2^n\}\), viewed as length-\(N\) strings, and retain \(a=\lfloor N^\beta/n\rfloor\), \(b=\lfloor N^\beta\rfloor\), the two-tail family \(Y_a\), and \(W_b\) from C-160. Define

\[
Y^\star=Y_a\cup\mathrm{Aff}_n,\qquad
W^\star=W_b\cup\{u:\min_{f\in\mathrm{Aff}_n}d_H(u,f)\le a\},\qquad
Z^\star=\{0,1\}^N\setminus W^\star.
\]

Every affine truth table has circuit size \(O(n)\), hence belongs to the low class at the OPS thresholds for large \(n\). The affine family has \(2^{n+1}=2N\) elements. Its radius-\(a\) neighborhood has size at most \(2N\sum_{j\le a}\binom Nj=2^{O(N^\beta)}\), below the \(2^{\Theta(N^\beta n)}\) size of \(W_b\). Thus the low and non-high cardinality exponents remain those of C-160. Every pair in \(Y^\star\times Z^\star\) is at Hamming distance at least \(a+1\): this follows by the affine-neighborhood exclusion for affine rows and by the middle-band weight gap for the two tails. Local pattern richness and large-cylinder completion also persist. The construction is complement-symmetric and invariant under affine permutations of the input domain.

The promise still has a near-linear separator. From an input table \(u\), compute its Hamming weight and test the two tails as in C-160. To test whether \(u\) is within distance \(a\) of an affine function, set \(s_x=(-1)^{u(x)}\) and compute all Walsh coefficients

\[
\widehat{s}(\ell)=\sum_{x\in\mathbb F_2^n}s_x(-1)^{\ell\cdot x}.
\]

For the affine function \(\ell\cdot x+c\), the Hamming distance from \(u\) is \((N-(-1)^c\widehat{s}(\ell))/2\); hence the nearest-affine distance is at most \(a\) exactly when \(\max_\ell|\widehat{s}(\ell)|\ge N-2a\). The fast Walsh-Hadamard transform uses \(O(Nn)\) additions/subtractions on \(O(n)\)-bit integers, implementable by a Boolean circuit of size \(O(Nn^2)\); taking the maximum and testing the threshold costs at most the same order. Therefore \(1_{W^\star}\) is a separator of size \(O(Nn^2)=N^{1+o(1)}\), and the corresponding rect-DAG and active fusion cover have the same upper bound.

There is also a direct consequence for the actual OPS high side. The restricted row family \(\mathrm{Aff}_n\) is entirely in \(\mathrm{SIZE}(s_1)\), while every \(z\in Z=\{u:\mathrm{CC}(u)>s_2\}\) is non-affine. Thus the Boolean function that accepts exactly affine truth tables separates \(\mathrm{Aff}_n\) from the actual \(Z\). The same Walsh-Hadamard test detects exact affine membership by checking whether \(\max_\ell|\widehat{s}(\ell)|=N\), using \(O(Nn^2)\) gates. Hence the mismatch rect-DAG for the whole \(2N\)-row affine subfamily against the actual high class has size \(N^{1+o(1)}\). This rules out the affine subfamily alone as the source of a superlinear OPS DAG lower bound.

**What this falsifies and what it leaves.** Having many balanced low rows, an affine orbit of size \(2N\), complement/input-affine symmetry, radius-\(a\) patch neighborhoods, and the C-129 cylinder statistics still does not force a superlinear DAG. This enlarged calibration does not preserve C-160's closure under arbitrary recombination of \(\Theta(n)\) low rows: composing all \(n\) input literals with an arbitrary size-\(s_2\) circuit can produce any size-\(s_2\) truth table, and recognizing that whole composition range is the original separator problem. This isolates a more demanding candidate than row counts or symmetry: analyze the state-reuse effect of *many overlapping functional bases together with their full circuit-composition closure*. No lower bound or OPS transfer has been proved from this observation.
## 88. C-162 - Description-space invariance and the basis-count stress test

This checkpoint resumes the C-74/C-75 shared-state frontier. It rechecks the exact search relation and transfer chain, then tests whether the count of overlapping linear bases can itself force non-shareability. It does not prove a superlinear lower bound.

### Exact relations and what each party knows

Set \(N=2^n\), \(Y=\mathrm{SIZE}(s_1)\), and \(Z=\{0,1\}^N\setminus\mathrm{SIZE}(s_2)\). Alice receives \(w\in Y\), Bob receives \(z\in Z\), and

\[
\mathrm{Mis}_{Y,Z}(w,z)=\{(k,b):w_k=b,\ z_k=1-b\}.
\]

This is total because \(s_1<s_2\), hence \(w\ne z\). A valid output is a coordinate and the Alice bit at which the two tables differ. If Alice is given a circuit description \(d\) with \(G(d)=w\), the same relation outputs \((k,b)\) with \(G(d)_k=b\ne z_k\).

For a proposed fusion list \(Q=((E_i,H_i))_{i=1}^q\), put \(T_i=E_i\cap H_i\). For each anchor \(v\), let \(x_i^{(t)}(v)\) mean that the closure has derived the set \(T_i\) by round \(t\); it does not mean that the truth table \(v\) is an element of the set \(T_i\). Let \(a_i(v)\) and \(b_i(v)\) say that a matching literal slice for \(v\) is contained in \(E_i\) and \(H_i\), respectively. Then

\[
x_i^{(t+1)}(v)=x_i^{(t)}(v)\ \vee\
\left(a_i(v)\vee\bigvee_{j:T_j\subseteq E_i}x_j^{(t)}(v)\right)
\wedge
\left(b_i(v)\vee\bigvee_{j:T_j\subseteq H_i}x_j^{(t)}(v)\right),
\qquad x_i^{(0)}(v)=0.
\]

The Q-path search relation outputs an empty-carrier start \(i_0\), a sequence of side/support choices, and a terminal signed mismatch. Each support step must use a matching literal seed or a predecessor \(j\) with \(T_j\) contained in the selected side; predecessor steps strictly decrease the first activation round on \(w\). This relation is total on \(Y\times Z\) exactly when \(Q\) is a successful cover. Plain mismatch remains total whether or not \(Q\) succeeds.

### Complexity measures kept separate

| Object | Established bound | Scope |
|---|---:|---|
| Deterministic communication for plain mismatch | \(O(s_1\log(n+s_1)+\log N)\) bits; at least \(\Omega(\log N)\) for fixed-output protocols | Alice sends a circuit description; Bob compares it with \(z\). For each coordinate there is a high table with the required bit, giving \(N\) possible labels from a fixed zero row. |
| Deterministic communication for Path_Q | \(O(q\log(q+N))\) bits | A successful Q supplies a rank-decreasing witness path. This is a Q-dependent bound, not a lower bound for plain mismatch. |
| Ordinary protocol tree | At most \(2^{O(c)}\) vertices for a c-bit protocol | Description length controls depth, not shared graph size. |
| Standard acyclic rectangle-DAG | \(S_{\rm rect}=\Theta(\mathrm{SepCirc}(Y,Z))\), up to basis constants | Exactly the Boolean circuit size of a promise separator, through the rectangle/circuit correspondence. |
| Ranked cyclic Q-router | q rule states, at most 2N signed-output terminals, and \(O(q^2+qN)\) possible support arcs | Every actual path terminates by rank descent; its static graph can contain cycles. |
| Fusion cover | \(q=\rho_{\rm prom}=D^\circ_\cap(Y\mid\mathcal B_{\rm prom})\) for a minimum list | Exact active-promise identity from Cavalarâ€“Oliveira. |

The \(N-o(N)\) rect-DAG floor counts distinct signed output labels reachable from the fixed row \(w=0\): for each coordinate, the high side contains a table with bit 1 there. The upper bounds from a successful cover are \(O(q^3/\log q)\) for the best compiler currently recorded, and \(2^{O(s_1\log(n+s_1))}\) through the description protocol tree. The restriction-sharing construction \(O(|Y|+\sum_I\pi_I(Y))\) is another valid upper bound, not a lower bound.

### Model comparison: exact identities and non-identities

| Model | Exact object counted | Relation to C-75 |
|---|---|---|
| Sokolov Boolean communication game | Acyclic, out-degree-at-most-two graph; each node has separate Alice/Bob predicates, so its valid inputs form a rectangle; child rectangles cover the parent | This is the standard shared-DAG model. Sokolov proves Boolean-game size is equivalent up to constants to Boolean circuit size for the full Bit relation of a function. Restricting a separator game to \(Y\times Z\) gives the mismatch DAG. |
| GGKS rectangle-DAG | Acyclic DAG of combinatorial rectangles with valid-output leaves | This is the same shared-state geometry used in DAG-like KW lifting. Their monotone circuit equality concerns the full monotone KW relation; it does not identify the promise mismatch DAG with the cyclic fusion machine. |
| Communication PLS game | A fixed acyclic state graph plus an input-dependent strategy; state-membership/successor choice has a separate communication cost | Boolean games of size L yield PLS size L and cost at most 2; PLS size L and cost t yields a Boolean game of size at most \(L2^{3t}\). Cycles with input-sensitive ranks are not included. |
| Cavalarâ€“Oliveira cyclic discrete complexity | Least-fixed-point evaluation of t set equations; \(D^\circ_\cap\) counts only cyclic intersection operations | Exactly the fusion measure: \(\rho=D^\circ_\cap\). Their theorem also gives \(D^\circ_\cap\le D_\cap\le(D^\circ_\cap)^2\). This is the closest exact model, not a standard communication DAG. |
| Nakayamaâ€“Maruoka loop circuits | Cyclic circuits in a generalized approximation model | Related ancestry, not a literal identification: Cavalarâ€“Oliveira state that NM95 uses more general functionals and Boolean circuit complexity, whereas their exact theorem uses monotone semi-filters and intersection complexity. |
| Amanoâ€“Maruoka conjunctive complexity | AND gates in an acyclic monotone circuit | A useful resource analogue for the \(D_\cap\) transfer, but their quadratic-function results do not apply to this promise separator. |

Primary-source recheck: [Sokolov, definitions and Theorem 3.2](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download); [GGKS, rectangle-DAG definition and monotone KW connection](https://theoryofcomputing.org/articles/v016a013/v016a013.pdf); [Cavalarâ€“Oliveira, Theorem 30 and Corollary 17](https://eccc.weizmann.ac.il/report/2025/033/download).

### Cover-to-DAG and reverse transformations

A successful q-pair list gives the Q-specific cyclic router with q rule states. At state \(i\), Alice's side is \(A_i=\{w:x_i(w)=1\}\), Bob's side is \(B_i=\{z:x_i(z)=0\}\), so the state rectangle is \(A_i\times B_i\). Bob chooses an endpoint side absent from \(z\); Alice supplies a literal seed or a predecessor whose carrier lies in that side. Literal supports output a mismatch. A predecessor transition is rectangle-preserving and lowers \(\tau_i(w)\). This proves termination on each pair, even though the static support graph can cycle. It is a ranked cyclic search protocol, not a standard DAG.

For acyclic measures, the current best general bounds are

\[
\mathrm{SepAnd}(Y,Z)\le q^2,
\qquad
S_{\rm rect}=\mathrm{SepCirc}(Y,Z)\le O(q^3/\log q).
\]

The first is the acyclic intersection/AND-only conversion; it leaves OR routing uncharged. The second pays for ordinary binary-fanin routing and eliminates cycles; the batching improvement is C-100. The explicit rank-layer simulation is \(O(q^3)\), so it does not improve the best \(O(q^3/\log q)\) compiler. Counting only the q original rule nodes as an acyclic DAG is invalid whenever their dependency graph has cycles.

In reverse, an L-node mismatch rect-DAG yields an \(O(L)\)-size Boolean separator: mismatch leaves become literals, and Sokolov's AND/OR/copy rectangle trichotomy combines child separators. A Boolean separator has an \(O(L)\)-size positive dual-rail circuit on the \(2N\) signed truth-table literals. Restricting to the active promise ground set and applying the fusion theorem gives \(\rho_{\rm prom}\le O(L)\). This reverse map does not upgrade automatically to the distinct full-domain cover, because the separator may accept medium-complexity tables. An arbitrary cyclic search graph also does not reverse to a fusion list unless its transitions arise from actual endpoint pairs and their carrier-containment supports.

The full inequality chain and magnification thresholds are therefore

\[
q=\rho_{\rm prom}=D^\circ_\cap,\qquad
\rho_{\rm prom}\le O(S_{\rm rect}),\qquad
S_{\rm rect}=\Theta(\mathrm{SepCirc}),\qquad
S_{\rm rect}\le O(\rho_{\rm prom}^3/\log\rho_{\rm prom}).
\]

A direct \(q>N^{1+\varepsilon}\) lower bound meets the goal. An AND-only separator lower bound above \(N^{2+2\varepsilon}\) suffices through \(D_\cap\le q^2\). A standard rect-DAG lower bound must exceed \(N^{3+3\varepsilon}/\log N\) under the current compiler. Conversely, an \(N^{1+o(1)}\) mismatch DAG would imply \(\rho_{\rm prom}=N^{1+o(1)}\) and kill this superlinear-cover route.

### Short descriptions: exact limitation of the proposed shortcut

Let \(G:D\to Y\) map circuit descriptions onto low truth tables. The minimum standard rect-DAG size for \((d,z)\mapsto\mathrm{Mis}(G(d),z)\) equals that for \((w,z)\mapsto\mathrm{Mis}(w,z)\). A DAG on truth tables lifts by replacing each row set \(A_v\) with \(G^{-1}(A_v)\). A DAG on descriptions restricts along any section \(\sigma:Y\to D\), replacing \(A_v\) by \(\{w:\sigma(w)\in A_v\}\). Both operations preserve rectangles, edges, and valid leaves without changing the number of graph nodes. This equality relies on the standard model leaving local predicates uncharged. If evaluating predicates were charged, that would be a different model and needs a new transfer theorem.

Thus Alice's short circuit description gives a short communication protocol but no automatic state compression. A universal circuit can compute \(G(d)_k\) locally for Alice, and Bob can read \(z_k\), but the joint predicate â€œthere is a mismatch in interval Iâ€ need not be a rectangle. On rows and columns \(\{00,11\}\), the mismatch pairs are the off-diagonal two points; a rectangle containing both also contains the two equal pairs. Binary search on mismatch locations therefore needs genuine communication states. The existing strongest generic scan shares by low-row restrictions, \(O(|Y|+\sum_{I\ {\rm dyadic}}\pi_I(Y))\); it is not \(N^{1+o(1)}\) at OPS parameters. This proves the failure of the universal-evaluation shortcut, not the nonexistence of every small universal DAG.

There is a conditional obstruction already on record in C-98/C-99. Under nonuniform-secure PRFs, with the table length chosen polynomial in the PRF security parameter, a polynomial-size Gap-MCSP separator would distinguish PRF truth tables from uniform random tables by querying all N bits. Thus the premise rules out every polynomial-size shared DAG in that parameterization, despite the PRF rows having short individual circuit descriptions. The assumption also implies \(NP\not\subseteq P/poly\) through MCSP, so this is a conditional benchmark rather than an independent route to P versus NP. Unconditionally, the existence of an \(N^{1+o(1)}\) universal DAG remains open.

### Tree/DAG calibrations

Parity on m bits has a shared circuit/rect-DAG of \(O(m)\) nodes and formula/protocol-tree size \(\Omega(m^2)\) by Khrapchenko. Conversely, counting gives functions on m bits whose circuit and rect-DAG size is \(\Omega(2^m/m)\), while Alice can send her m-bit input and Bob can return a differing coordinate in \(O(m+\log m)\) communication. These examples isolate the resource: communication depth can be small while a shared graph is large, and sharing can also shrink a tree quadratically. Neither calibration supplies an OPS-specific lower bound.

### C-162 basis-count stress test

An ordered basis \(A\in GL(n,2)\) consists of n linear forms. The \(2^{n^2+O(1)}\) bases do not give that many distinct basis rows: across all bases, every component row is one of only \(2^n=N\) linear functions. Counting basis descriptions as distinct anchors therefore overcounts the actual truth-table domain. More generally, composing any such basis with a size-t circuit g gives \(g(Ax)\) using \(t+O(n^2)\) Boolean gates. When \(t\le s_1-O(n^2)\), the output is simply an element of the existing low class \(Y\); changing the basis does not create an independent promise instance. Description-space lift/restrict invariance prevents the number of syntactic basis descriptions alone from reducing DAG size.

There is a second budget boundary. A composition with total circuit size at most \(s_2\) is excluded from \(Z\), but if its truth table is not in \(Y\), it is in the medium band \(M=\mathrm{SIZE}(s_2)\setminus Y\). The C-75 relation has Alice domain \(Y\), and the active fusion ground set is \(Y\sqcup Z\); it imposes no condition on separator values or DAG rectangles involving medium tables. Thus closure under all size-\(s_2\) combiners is not, by itself, a closure property of the active mismatch relation. A useful composition argument must either stay within the \(s_1\) row budget or prove a separate extension/restriction theorem forcing a separator to respect selected medium tables. C-79 rules out the naive endpoint reuse that simply treats the promise separator as an exact low-set separator.

The affine subproblem is decisively easy even against the actual high class. All \(2N\) affine truth tables lie in \(Y\), and no \(z\in Z\) is affine. For \(s_x=(-1)^{z(x)}\), Walsh coefficients satisfy \(\max_\ell|\widehat{s}(\ell)|=N\) exactly for affine z. The fast Walshâ€“Hadamard transform and \(O(n)\)-bit arithmetic test affine membership with \(O(Nn^2)=N^{1+o(1)}\) Boolean gates. Hence the mismatch DAG for \(\mathrm{Aff}_n\times Z\) is near-linear. The large number of ordered bases of affine forms, by itself, cannot force a superlinear full-promise DAG.

This does not settle the narrower candidate in which many distinct nonlinear compositions remain inside the \(s_1\) row class and their residual relations interact. No state-incompatibility lemma across those low-budget composition families has been proved. Compositions known only to fit the \(s_2\) budget may be medium rows, so they cannot be charged in the active relation without an additional theorem. The basis count, the affine orbit, C-122's small-family router, and C-123's description invariance supply no such lemma.

**Checkpoint status.** Model correspondence is Tier 4, already known. The description-space equality and basis-count collapse reject two proposed generic shortcuts. No Tier 1â€“3 result, no \(N^{1+o(1)}\) DAG for all \(Y\times Z\), no superlinear \(S_{\rm rect}\) or \(\rho_{\rm prom}\) lower bound, and no P-vs-NP proof was obtained. Continue O-126 only with an OPS-specific state-reuse property of the full low/high promise or a direct cyclic-closure lower bound.

## 89. C-163 - Hamming distance imposes a decoder-capacity bound

This is a necessary-condition test for the C-154/O-124 source-to-mismatch route, not a lower bound on the actual mismatch DAG.

Let Delta=d+1=Theta(N^beta/n) be the established minimum Hamming distance between every w in Y=SIZE(s1) and z in Z=SIZE(s2)^c (C-136). Let R be a total source search relation on X x Y0 with output set O. Define its fractional output-cover number as the minimum sum of nonnegative weights lambda_o such that every source pair has valid-output weight at least one:
chi_out*(R)=min sum_o lambda_o, subject to sum_{o in R(x,y)} lambda_o >= 1 for every pair.

Suppose partywise maps send each source pair to a promised table pair (alpha(x),beta(y)) in Y x Z. After each signed mismatch type tau=(k,b), where Alice's bit is b and Bob's is 1-b, allow a decoder with at most r output-labelled terminal incidences. Count an incidence separately for every starting type, even if decoder states are shared. Every terminal label must be valid for every source pair reaching it.

For each output o, let c_o be the number of type/terminal incidences labelled o. There are 2N directed mismatch types, so sum_o c_o <= 2Nr. For any source pair, at least Delta table coordinates mismatch. Each such coordinate's decoder path ends at a source-valid output, hence
Delta <= sum_{o in R(x,y)} c_o.
Therefore lambda_o=c_o/Delta is a fractional output cover and
chi_out*(R) <= 2Nr/Delta = O(r n N^(1-beta)).

For a fixed coordinate/sign decoder, r=1; this strengthens C-156's paired-cut characterization with a quantitative capacity bound. If every source pair has a unique valid output and M distinct outputs occur, then chi_out*(R)=M, so any such reduction requires r >= M Delta/(2N).

**Calibration.** Take k=floor((1-beta/2)n) and the total relation on X={0,1}^k and a singleton Bob domain whose unique answer is o=x. It has M=2^k=Theta(N^(1-beta/2))<2N distinct answers. Alice's inputs can all be encoded as low tables: put the k input bits in k fixed truth-table positions and put zero elsewhere; a fan-in-two circuit of size O(kn)=O(n^2) computes each table, below s1 for fixed beta>0 and large n. But the capacity inequality requires
r = Omega(M Delta/N) = Omega(N^(beta/2)/n).
Thus even though the output alphabet fits among the 2N signed mismatch types and Alice knows the answer without communication, no fixed decoder, nor any decoder with only poly(n) output incidences per mismatch type, can realize this relation through promised low/high table mismatches. The obstruction is the number of repeated witnesses forced by the code-distance gap, not just output-alphabet size.

**Use and limits.** Before attempting an O-124 reduction, compute or lower-bound chi_out*(R). If it exceeds 2Nr/Delta, a decoder of the proposed size r is impossible. This does not rule out a source relation with small fractional output cover, a reduction not factoring through coordinatewise table mismatch, or a decoder whose refinement cost is large enough. It does not imply S_rect or rho_prom is large. It sharpens the C-154 transfer test by making the required decoder overhead explicit; see O-124/O-125.

**Check against the actual C-154 source family.** In the colourful-sunflower lifting theorem, Search(cPHP(G)) outputs a colliding pigeon pair (p,p'); its Index composition keeps those outputs. Therefore its fractional output-cover number is at most the number of possible pigeon pairs, chi_out* <= binom(k,2), simply by assigning weight one to every pair. For k polynomial in the truth-table input length n, this upper bound is far below n N^(1-beta), so C-163 does not rule out the standard cPHP lifting candidate at those parameter scales. This is only a pass of the capacity filter: it proves neither a partywise encoding into SIZE(s1) x SIZE(s2)^c nor C-156's paired-cut validity. The source relation and its output labels are stated in the primary CCC 2025 paper, Theorem 11 and the cPHP definition: https://drops.dagstuhl.de/storage/00lipics/lipics-vol339/ccc2025/html/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.html.

## 90. C-164 - Index cPHP rectangles force a decoder-refinement cost

C-163's output-label cover can be small for the C-154 source, so inspect individual valid rectangles. Use the lifted graph-pigeonhole search relation from the CCC 2025 construction. Let G be a simple bipartite graph with k left vertices (pigeons), left degree d>=2, and right side smaller than k. Alice has pointers x in [m]^k; Bob has arrays y in [d]^(mk); the induced choice for pigeon p is y_(p,x_p). A valid output is a pair of distinct pigeons p!=q with Gamma(p,y_(p,x_p))=Gamma(q,y_(q,x_q)); p=q is not a collision witness. The primary paper defines exactly this source relation and its Index composition (Theorem 11 and the cPHP definition; link in Â§89).

Under the uniform product distribution mu on Alice's pointers and Bob's arrays, every rectangle A x B monochromatic with output (p,q) has
mu(A x B) <= 1/(m^2 d).

**Proof.** Project A to S={(i,j): some x in A has x_p=i and x_q=j}. Since (x_p,x_q) is uniform on [m]^2, mu_X(A)<=|S|/m^2. For every (i,j) in S, all y in B must satisfy Gamma(p,y_(p,i))=Gamma(q,y_(q,j)). The equality relation between the two d-valued choices is a partial matching, since the graph has no repeated neighbors at either left vertex. Form the bipartite constraint graph with position-variables (p,i),(q,j) and edge set S. In each nontrivial connected component, fixing one root value determines at most one value at every other vertex along a spanning tree; inconsistent cycles only remove assignments. If R is the sum over components of (vertices-1), then mu_Y(B)<=d^(-R). For a component with v vertices and e edges, e<=floor(v^2/4)<=2^(v-2)<=d^(v-2). If there are t nontrivial components, this gives |S|<=d^(R-1): sum the component edge bounds and use t<=d^(t-1). Hence |S|d^(-R)<=1/d, proving the rectangle-mass bound.

Now suppose partywise maps encode every source pair as a promised low/high table pair, and every signed table mismatch is decoded by at most r output-labelled rectangle leaves. Each such leaf pulls back to a valid rectangle for some output (p,q), so has mu-mass at most 1/(m^2 d). For each source pair, the encoded tables differ in at least Delta=Theta(N^beta/n) positions. Averaging this Hamming distance under mu gives
Delta <= 2 N r/(m^2 d),
and therefore
r >= Delta m^2 d/(2N) = Omega(m^2 d N^(beta-1)/n).
For a fixed decoder, r=1, so no such encoding exists if m^2 d>2N/Delta.

**What this says about the lead.** The cPHP output-label cover itself obeys chi_out*<=binom(k,2), so C-163 alone usually passes when k is polynomial in the table input arity n. C-164 is sharper because it uses the Index pointers: even one fixed collision-pair rectangle has an extra m^(-2) density penalty. A direct reduction must pay the displayed decoder-refinement cost. This does not rule out the C-154 route: the lifted DAG lower bound is roughly (m/(A d w log(mk)))^w, and after dividing by the required decoder cost the result can still be large for growing width w. The actual parameter comparison and, more fundamentally, explicit low/high table maps remain open. Any transfer must preserve the OPS compiler target S_rect > N^(3+3epsilon)/log N (or bypass it with a direct rho_prom bound). This is a reduction obstruction/necessary cost, not a lower bound on S_rect or rho_prom.

**Parameter-direction caveat.** The bound r>=r_min is a lower bound on decoder cost, not an upper bound on it. If L0=(m/(A d w log(mk)))^w is the lifting theorem's guaranteed source-DAG lower bound and T=N^(3+3epsilon)/log N is the OPS rect-DAG transfer threshold, then this theorem can clear T through such a reduction only if its available decoder upper bound satisfies r<L0/T. The C-164 obstruction requires r>=r_min=Delta m^2 d/(2N), so a necessary feasibility check for this proof route is L0>T r_min, equivalently
(m/(A d w log(mk)))^w > Delta m^2 d N^(2+3epsilon)/(2 log N).
Indeed, T r_min = (N^(3+3epsilon)/log N)(Delta m^2 d/(2N)) = Delta m^2 d N^(2+3epsilon)/(2 log N).
Using Delta=Theta(N^beta/n), this is Theta(m^2 d N^(2+3epsilon+beta)/(n log N)).
Passing this inequality is not enough: an actual reduction and a matching decoder-size upper bound still have to be built. If it fails for a chosen parameter schedule, the current quantified lifting bound cannot overcome even the minimum decoder cost.

## 91. C-165 - A fixed signed-mismatch decoder cannot represent lifted cPHP

This sharpens C-156 for the specific C-154 source. It proves a no-go for fixed output decoding, independently of the table-circuit lower-bound work.

Use Search(cPHP(G)) composed with Index_m^k, where G is a simple bipartite graph of left degree d>=3 and each left vertex has d distinct neighbors. Alice has x in [m]^k; Bob has y in [d]^(mk); the induced assignment is z_p=y_(p,x_p); the output alphabet contains only distinct pairs p!=q, and (p,q) is valid iff Gamma(p,z_p)=Gamma(q,z_q). Assume m is divisible by d.

Under uniform Bob input y, for every fixed Alice input x and output pair (p,q),
Pr_y[(p,q) is valid] <= 1/d,
because z_p,z_q are independent uniform choices from the two d-element neighbor lists, which share at most d neighbors.

Suppose partywise maps encode all source inputs as two disjoint table families, and every signed mismatch type (table coordinate plus orientation) is decoded by a rectangle protocol with at most r output-labelled leaves, all valid on their leaf rectangles. At a fixed coordinate t, let A_0,A_1 partition Alice inputs and B_0,B_1 partition Bob inputs according to the encoded bits. If both A_0 and A_1 are nonempty, then the decoder leaves for A_0 x B_1, after fixing any x in A_0, cover B_1 by at most r output-valid Bob sets, each of measure at most 1/d. Hence mu(B_1)<=r/d. The opposite orientation similarly gives mu(B_0)<=r/d. Since B_0 and B_1 partition Bob's domain,
1=mu(B_0)+mu(B_1)<=2r/d.
Thus if r<d/2, every table-coordinate bit on Alice's side must be constant over all x.

Now choose a Bob input y* whose selected-neighbor sequence for each pigeon is balanced over its d neighbors; this is possible because d divides m. For uniform x, every fixed output pair (p,q) of distinct pigeons is valid on at most a 1/d fraction of Alice inputs. If all Alice table bits are constant, each mismatch type at y* is present for either every x or no x. Any present type would need at most r output-labelled leaves to cover all x, but their valid row sets have total measure at most r/d<1. So no mismatch type can be present. That would make the low and high encoded tables equal, contradicting disjointness. Therefore every such encoding/decoder requires r>=d/2. In particular, a fixed coordinate/sign decoder (r=1) is impossible for d>=3.

The CCC 2025 cPHP-to-clique-colouring reduction does provide a fixed decoder for the *one-sided monotone Karchmer-Wigderson output* (an Alice-present/Bob-absent edge); it does not decode both signs of arbitrary table mismatch. The C-165 obstruction explains exactly why that lemma cannot be imported unchanged into C-75. A refinement with r>=d/2 is not ruled out, and C-164 adds the separate distance-based requirement r>=Delta m^2 d/(2N). No table map, separator lower bound, or fusion-cover bound follows yet. Primary source for the one-sided reduction: the CCC 2025 paper, Lemma 19 and the cPHP definition, https://drops.dagstuhl.de/storage/00lipics/lipics-vol339/ccc2025/html/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.html.

## 92. C-166 - DAG-model audit and reconciliation with C-78/C-133

This continues the C-74/C-75 shared-DAG frontier. This is an audit and consolidation, not a new asymptotic lower bound: C-78 already constructed the restriction-profile interval router, C-110 gave the product-hull rule for state merging, and C-133 already proved that this router is exponentially large. This pass rechecks the exact models against primary sources and records the interval cross-pair proof in the present notation. None of these scanner-specific facts lower-bounds arbitrary rect-DAGs.

### Exact C-75 relation and model identifications

Let N=2^n, Y=SIZE(s1), and Z be the complement of SIZE(s2), with s1<s2. Alice holds w in Y; Bob holds z in Z. The total search relation is
Mis_Y,Z(w,z) = {(i,b): w_i=b and z_i=1-b}.
It is total because Y and Z are disjoint. If Alice instead holds a description d with G(d)=w, the output condition is G(d)_i=b != z_i. The finite surjection G:D->Y preserves standard rect-DAG size exactly: lift row predicates through G in one direction, and restrict along any section Y->D in the other. Short descriptions therefore do not reduce the shared-state measure.

For a proposed pair list Q=((E_i,H_i)) for i=1,...,q, the C-74 least-fixed-point state bits are
x_i^(t+1)(v) = x_i^t(v) OR
  (a_i(v) OR OR_{j:T_j subset E_i} x_j^t(v))
  AND
  (b_i(v) OR OR_{j:T_j subset H_i} x_j^t(v)),
where T_j=E_j intersect H_j and x_i^(0)(v)=0.
Here a_i,b_i are literal-slice seed predicates. Plain mismatch is total independently of Q; the stricter path relation that also outputs an empty-carrier start and support history is total exactly when Q is a successful cover.

### Comparison with the closest known models

| Model | What its states mean | Exact relation to this project |
|---|---|---|
| Sokolov Boolean communication game | Acyclic graph, out-degree at most two, root valid on the whole product, and each node has private Alice/Bob predicates; each node-valid input set is a rectangle. | This is the standard shared-DAG model for Mis_Y,Z. The rectangle/circuit induction gives rectDAG(Mis_Y,Z)=Theta(SepCirc(Y,Z)). Sokolov's circuit theorem is for the full Bit relation; restrict a separator game to Y x Z, and extend any promise separator arbitrarily off the promise, to obtain the promise version. |
| GGKS rect-DAG | Acyclic graph of product rectangles; children cover each parent; leaves carry outputs valid throughout their rectangle. | Same sharing geometry. Their exact monotone-circuit equality concerns the full monotone KW relation, not the cyclic fusion recurrence. Triangle-DAG and other non-product models need a separate simulation and loss accounting. |
| Communication PLS | A fixed state graph plus an input-dependent local strategy; acyclic Boolean games correspond to bounded-cost PLS with an exponential-in-cost conversion. | Can encode the ranked support walk, but does not remove its support-selection cost. Cycles with input-sensitive rank are not standard acyclic Boolean games. |
| Cavalar-Oliveira cyclic discrete complexity | Least-fixed-point set computations; D-circ-cap counts cyclic intersection operations over the semi-filter semantics. | Exact identity: rho_prom = D-circ-cap. Their acyclic intersection measure obeys D-circ-cap <= D_cap <= (D-circ-cap)^2. This is the closest exact model. |
| Nakayama-Maruoka loop circuits | Cyclic circuit specifications used in an approximation-model characterization. | Related ancestry, not identity: their loop-circuit theorem concerns distance to a generalized M(F_max) model. Cavalar-Oliveira adapt the idea to semi-filters and obtain the exact intersection-only cover characterization. |
| Amano-Maruoka conjunctive complexity | Number of AND gates in an acyclic monotone circuit. | A resource analogy for acyclic intersection cost, not the C-75 game. Their quadratic-function results do not establish a lower bound for this promise separator. |

Primary definitions and statements were rechecked in Sokolov, GGKS, Cavalar-Oliveira, Nakayama-Maruoka, and Amano-Maruoka; direct links are listed at the end of this section.

### Quantitative baseline for the separate measures

Let ell=O(s1 log(s1+n)) be a low-circuit description length. Current bounds:

| Measure | Bound for plain C-75 mismatch | Reason / caveat |
|---|---:|---|
| Deterministic communication bits | Omega(log N) <= D_cc <= O(ell+log N) | Alice sends a description; Bob finds and returns a differing coordinate. The lower bound comes from the output labels needed from a fixed low row. |
| Ordinary protocol-tree vertices | N-o(N) <= S_tree <= 2^O(ell+log N) | Every tree is a DAG, so a small tree cannot be larger than the minimum DAG. The upper bound expands the description protocol. |
| Standard acyclic rect-DAG vertices | N-o(N) <= S_rect=Theta(SepCirc(Y,Z)) <= O(q^3/log q) | The lower bound is the fixed-row output-label argument; the upper bound requires a successful q-cover. The profile router gives a separate O(|Y|+sum_I pi_I(Y)) construction. |
| Ranked cyclic Q-game states | q rule states plus at most 2N signed-output terminals | Every pair's selected route terminates by strict decrease of its activation rank; the static graph may cycle. It is not a standard acyclic DAG. |
| Ordinary communication depth for the Q path | O(q log(q+N)) bits | This does not imply a small shared graph; its direct protocol tree may have 2^O(q log(q+N)) vertices. |

Here N-o(N) uses log2|SIZE(s2)|=o(N), as in the OPS parameter range. The Q-path relation is total only for a successful cover; plain mismatch is always total on Y x Z.

### Best q-cover to shared-DAG transformation currently available

A successful Q gives an exact ranked cyclic rectangle game: q rule states, up to 2N signed-mismatch terminals, and O(q^2+qN) possible support arcs. Every fixed low/high pair has a route whose first-activation rank strictly decreases at each predecessor step, so every selected route terminates. The static dependency graph may contain cycles. This is input-sensitive well-foundedness that an ordinary acyclic DAG does not express.

Counting the q cyclic states alone as a standard DAG is invalid when the static graph has a cycle. Layering by activation rank and routing support choices explicitly gives O(q^2(q+N)) vertices; the best compiler currently recorded improves this to
S_rect=O(q^3/log q).
For successful OPS covers C-94 gives q>=N/2 for large N, so the compiler bound applies in its stated range. No O(q polylog N) conversion is established. Conversely, an L-node acyclic rect-DAG gives a Boolean promise separator of size O(L), hence rho_prom=O(L). The transfer chain remains
q=rho_prom=D-circ-cap,
rho_prom=O(S_rect),
S_rect=O(q^3/log q).
Thus a rect-DAG lower bound must exceed N^(3+3epsilon)/log N to force q>N^(1+epsilon) by this route. A direct q-lower bound avoids the loss. The q states are sufficient only in the ranked cyclic model, not in Sokolov/GGKS's acyclic model.

### Recheck of the C-78 universal rect-DAG

For an interval I of table coordinates, define pi_I(Y) as the number of distinct restrictions w|I for w in Y. For every distinct restriction r in Y|I, make a state
R(I,r) = {w in Y: w|I=r} x {z in Z: z|I != r}.
This is a rectangle and every pair in it has a mismatch in I. At a singleton interval it is a valid signed-mismatch leaf. At a larger dyadic interval I=I0 disjoint-union I1, connect R(I,r) to R(I0,r|I0) and R(I1,r|I1). Bob chooses the left child if z|I0 != r|I0, and otherwise the right child; the parent condition guarantees a right mismatch in the latter case. This is a local Bob rule and the children cover the parent rectangle. A binary Alice-only tree first routes the root product to the state indexed by Alice's full table w. The resulting acyclic rect-DAG has size
O(|Y| + sum over dyadic I of pi_I(Y)).
This is the C-78 universal DAG; its private predicates can use a circuit description, and duplicate descriptions of one truth table share states. C-133 already proves it is exponentially large at an OPS dyadic level, so this architecture is decisively not an N^(1+o(1)) construction. The general profile upper bound remains O(|Y|+sum_I pi_I(Y)).

### Proven non-shareability inside this router architecture

Fix an interval I, and write A_r={w: w|I=r}, B_r={z: z|I != r}. This is the C-110 product-hull condition specialized to interval states. Suppose states for two distinct restrictions r and s are merged while descendants are required to output a mismatch inside I. A single state must contain the product hull (A_r union A_s) x (B_r union B_s). If there is a high table z_s in Z with z_s|I=s, then z_s is in B_r for r!=s. For any w_s in A_s, the cross-pair (w_s,z_s) lies in that hull but agrees on every coordinate of I, so no I-local mismatch leaf can solve it. The merge is invalid. Consequently, if every low restriction on I has a high extension, all pi_I(Y) restriction states are pairwise nonmergeable for an interval-local scanner.

The extension premise has a simple counting certificate:
2^(N-|I|) > |SIZE(s2)| implies every pattern on I has a high extension.
There are 2^(N-|I|) extensions of each pattern and fewer than that many tables in SIZE(s2).

There is also an OPS-specific abundance calculation. Any assignment of bits to L selected table entries is computed by a DNF of at most L point indicators, with O(Ln) gates in a standard basis. Thus L*n <= s1/O(1) implies pi_I(Y)=2^L. When also N-L > log2|SIZE(s2)|, every such pattern has a high extension. For each fixed I, the cross-pair lemma requires 2^L separate contexts in an I-local subroutine. The explicit C-78 profile router has (N/L)*2^L tagged vertices at that level; C-133 proves these row sides are distinct even after deduplicating identical rectangles, using low realizability on the union of two intervals. This confirms the known failure of the interval-router construction. It does not rule out a different DAG that merges histories across coordinate regions.

**Scope limit.** This is not a lower bound for arbitrary rect-DAGs. A general DAG may change coordinate order, route to a mismatch outside I, or use separator states unrelated to this scanner's (I,r) invariant. C-137's prefix-state obstruction and C-110's product-hull condition remain architecture-specific unless a normalization theorem is proved. The universal circuit computes each party's local bits, but "there is a mismatch in I" is a joint predicate, not a rectangle: on row/column strings {00,11}, the mismatch set is the off-diagonal pair of points, whose rectangular hull also contains equal pairs. This disproves the direct universal-evaluation/binary-search shortcut, not every possible compact DAG.

### Tree, DAG, and communication calibration

A tree is itself a DAG, so a small protocol tree by vertex count can never coexist with a larger minimum DAG. The meaningful gap is between communication bits (depth) and shared graph size, and separately between formula/tree size and circuit/DAG size. By counting, some Boolean functions f on m bits have circuit complexity Omega(2^m/m); their Bit search relation has an O(m+log m)-bit protocol (Alice sends x; Bob returns a differing coordinate), while Sokolov's characterization forces a rect-DAG of Omega(2^m/m) nodes. Conversely, parity has an O(m)-node circuit/DAG but formula/protocol-tree size Omega(m^2). These calibrate the resource gap, not the Gap-MCSP promise.

**Fusion ceilings audit.** C-166 concerns a shared promise separator architecture. It does not evade or contradict rho_w<=N-1, rho*=O(N), or rho(H)=O(N log|H|) for fixed semi-filter families; those bounds concern other restricted/fractional cover regimes. No implication from the interval-scanner lower bound to rho_prom is established.

**Frontier and tier.** C-166 consolidates the C-110 product-hull rule and the C-133 interval-router lower bound; this is not new Tier 1-3 progress. There is still no arbitrary-DAG lower bound and no near-linear universal DAG. The exact model identification is Tier 4 and was already known. The conditional PRF benchmark in C-98/C-99 rules out polynomial separators under an assumption that already implies P != NP. Unconditionally, there is still no arbitrary-DAG lower bound above the required N^(3+3epsilon)/log N transfer threshold and no N^(1+o(1)) universal DAG. The actual N^(1+epsilon) fusion target remains open.

Primary sources:
- Sokolov, *Dag-like Communication and Its Applications*, definitions and Theorem 3.2: https://eccc.weizmann.ac.il/report/2016/202/revision/1/download
- Garg-Goos-Kamath-Sokolov, *Monotone Circuit Lower Bounds from Resolution*, rect-DAG models: https://theoryofcomputing.org/articles/v016a013/v016a013.pdf
- Cavalar-Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, Theorem 30: https://eccc.weizmann.ac.il/report/2025/033/download
- Nakayama-Maruoka, *Loop Circuits and Their Relation to Razborov's Approximation Model*: https://doi.org/10.1006/inco.1995.1083
- Amano-Maruoka, *The Monotone Circuit Complexity of Quadratic Boolean Functions*: https://doi.org/10.1007/s00453-006-0073-0

## 93. C-167 - C-160 refutes generic interval normalization

This is a new consequence of the existing C-160 calibration, aimed directly at O-127. It kills a promise-independent normalization of arbitrary rect-DAGs into interval-local scanners with polynomial size loss. It does not settle whether an OPS-specific normalization exists.

Use C-160's parameters

    a = floor(N^beta/n), b = floor(N^beta), 0 < beta < 1,

and its promise

    Y_a = {x : |x| <= a or |x| >= N-a},
    Z_b = {z : b < |z| < N-b}.

Let I be any coordinate interval of length L <= a. Every pattern r in {0,1}^I has both:

1. a low extension w_r in Y_a, obtained by setting every coordinate outside I to zero; then |w_r|=|r|<=L<=a;
2. a high extension z_r in Z_b with |z_r|=floor(N/2), obtained by filling floor(N/2)-|r| outside coordinates with ones. For sufficiently large N, b<floor(N/2)<N-b, and the required number of outside ones is feasible because L<=N/2.

Thus all 2^L low restrictions occur and each has a high extension. In the interval-local router, restriction r gives the rectangle

    A_r x B_r,
    A_r={w in Y_a : w|I=r},
    B_r={z in Z_b : z|I != r}.

If the states for distinct r and s were merged, the product hull would contain (w_s,z_s): both tables restrict to s on I, so this cross-pair has no valid mismatch output inside I. Therefore the 2^L restriction contexts are pairwise nonmergeable for any router that keeps descendants confined to I.

At L=a this forces at least 2^a states in that interval layer. Yet C-160's separator h(x)=1[|x|<=a or |x|>=N-a] has fan-in-two circuit size O(N log N), hence an O(N log N)-vertex rect-DAG by the Sokolov circuit/game correspondence. Since 2^a/(N log N) is superpolynomial in N for every fixed beta>0, no generic polynomial-loss normalization from arbitrary rect-DAGs to interval-local routers can hold.

**Frontier change.** Retire the generic form of O-127. The remaining question is narrower: can a normalization exploit a property specific to Y=SIZE(s1), Z=SIZE(s2)^c that fails for C-160? Any such proof must state that OPS-specific hypothesis and quantify its graph-size loss. C-160 is only a calibration, so this result gives no lower bound for the actual Gap-MCSP DAG, rho_prom, or P versus NP. It is Tier 5 route-pruning progress.
## 94. C-168 - Alice-only coordinate sampling still needs almost all positions

This tests a stronger universal-DAG shortcut than a fixed sample: let the allowed output-coordinate set depend arbitrarily on Alice's low table or on her circuit description.

Let M2=|SIZE(s2)|. Fix any low table w and any set S(w) subseteq [N] chosen using only w. Suppose a proposed router promises to output a mismatch at a coordinate in S(w) for every z in Z={0,1}^N minus SIZE(s2). Every table z agreeing with w on S(w) would then have to lie outside Z, so all its 2^(N-|S(w)|) completions must belong to SIZE(s2). Therefore

    2^(N-|S(w)|) <= M2,
    |S(w)| >= N-log2(M2).

In the OPS parameter range log2(M2)=o(N), so each low row needs an Alice-selected candidate set of N-o(N) coordinates. The proof is just cylinder counting and remains valid if S is chosen from any syntactic description d with G(d)=w; description collisions do not help.

**Limit.** This is a no-go for row-only, nonadaptive coordinate restriction. It is not a lower bound on rect-DAG size: a standard DAG may use Bob-dependent rectangle routing and output a coordinate that was not selected by Alice in advance. Thus a sublinear-output-support universal construction, if it exists, must exploit joint adaptive state sharing. C-168 is Tier 5 route pruning and adds no Gap-MCSP or fusion lower bound.

## 95. C-169 - The one-hot dual-rail image blocks direct monotone substitutions

This tests whether recent monotone gap-clique lower bounds can be imported by a direct monotone map into the C-75 relation.

For a truth table w in {0,1}^N, encode it by the 2N-bit vector e(w) with e(w)_(i,b)=1 exactly when b=w_i. Every valid encoding has Hamming weight N. Define the monotone-extension complexity

    MExt(Y,Z) = min{ size(F) : F is monotone on 2N variables,
                       F(e(w))=1 for all w in Y,
                       F(e(z))=0 for all z in Z }.

Then

    S_rect(Mis_Y,Z) <= MExt(Y,Z) <= O(S_rect(Mis_Y,Z)).

For the first direction, the monotone Karchmer-Wigderson game of F, restricted to e(Y) x e(Z), outputs a literal marker present in e(w) and absent in e(z), exactly a signed mismatch. For the reverse direction, an L-node rect-DAG gives an O(L)-size Boolean separator by Sokolov's rectangle trichotomy; the standard positive/negative rail simulation converts that separator to a monotone circuit on 2N variables with O(L) gates. The standard monotone circuit/game correspondence is proved in Sokolov's Theorem 3.2 and used in the GGKS rect-DAG framework.

**Constant-weight obstruction.** Suppose phi:{0,1}^m -> {0,1}^{2N} is coordinatewise monotone and phi(x) is a valid dual-rail table encoding for every x. For x<=y we have phi(x)<=phi(y), while both vectors have weight N, so phi(x)=phi(y). Since 0^m<=x for every x, phi is constant. Thus no nontrivial full-domain, coordinatewise-monotone substitution can map a monotone graph promise into valid table encodings while preserving the monotone-circuit structure.

This blocks only the direct monotone variable-substitution route. A gadget that uses non-code inputs, a nonmonotone partywise map, or an explicit extension constraint could evade it, but then the monotone lower bound does not transfer automatically. The CCC 2025 monotone Gap-Clique lower bound is therefore an adjacent technique, not an OPS DAG lower bound; no embedding into Y x Z has been constructed. See [the CCC 2025 paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol339-ccc2025/html/LIPIcs.CCC.2025.4/LIPIcs.CCC.2025.4.html). C-169 is Tier 5 route pruning.

## 96. C-170 - Both one-switch synopsis architectures are too large

This tests the direct use of Alice's short circuit description and its Bob-first analogue. A **one-switch** protocol has one party send a message represented by a frontier state; after that, only the recipient moves and chooses the output. The recipient may use an arbitrary shared DAG suffix. The bounds count distinct frontier states, so sharing inside that suffix does not evade them.

Write M2=|SIZE(s2)|. In the OPS range, log M2=O(s2 log(n+s2))=o(N) and |Z|=2^N-M2=(1-o(1))2^N.

### Alice sends first

For a message state m, let A_m be its low-row class, and let S_m be the set of coordinates that can label outputs in Bob's suffix. Since Bob's behavior depends only on (m,z), each output coordinate he chooses for a fixed z must have the same bit on every w in A_m. Let p_m be this common pattern on S_m. Correctness says every z in Z differs from p_m somewhere on S_m. Therefore every completion of p_m|S_m lies in SIZE(s2), and

    |S_m| >= N-log2(M2).

In particular, all rows in A_m have pairwise Hamming distance at most log2(M2). The C-80 block-constant code is a subset C of Y with |C|=2^Theta(s1) and minimum distance Theta(N/s1)=Theta(n N^(1-beta)). For fixed beta<1/2 this distance exceeds log2(M2)=O(N^beta n). Hence each Alice message class contains at most one member of C, and the one-switch protocol needs at least 2^Theta(s1) distinct frontier states.

### Bob sends first

For a Bob message class B_m subset Z, let S_m be the coordinates constant over B_m and p_m their common pattern. Once Alice receives m, any coordinate she outputs must be in S_m; validity for every z in B_m requires that for each w in Y some i in S_m has w_i != p_m(i).

Point-indicator circuits realize every prescribed pattern on any t coordinates with O(t n) gates. Thus if |S_m|<=t=floor(s1/(C n)) for a suitable basis constant C, a low table would match p_m on all of S_m, contradicting correctness. So |S_m|>t. The whole message class B_m is contained in the cylinder fixing p_m on S_m, hence |B_m|<=2^(N-t-1). Covering Z then requires at least

    |Z| / 2^(N-t-1) >= (1-o(1)) 2^(t+1)

distinct Bob frontier states, or 2^Omega(s1/n).

**Conclusion.** Neither sending a circuit description and letting Bob finish, nor sending a Bob-selected synopsis and letting Alice finish, yields a near-linear shared DAG. Both one-switch models have exponentially many states in a sublinear power of N. A compact C-75 DAG, if one exists, must use genuine alternation so later choices depend on rectangles selected using the other party's input.

**Limit.** These are lower bounds for fixed-order, one-switch DAGs only. An arbitrary rect-DAG may alternate owners repeatedly, and its state rectangle can shrink on both sides over time. No bound on those alternating states follows from C-170. It is Tier 5 route pruning for the unrestricted problem, not an OPS rect-DAG or rho_prom lower bound. O-129 asks for an alternation-sensitive potential or an explicit small multi-round DAG; O-128 remains open.

**C-80 countercheck against overgeneralization.** The same block-constant code has an O(N)-vertex adaptive DAG on its restricted low family: Bob finds a block where z is mixed (if z were constant on every block, z itself would be a low block-constant table); Alice's row has one constant bit on that block; Bob then finds a coordinate with the opposite bit. This uses a Bob-to-Alice-to-Bob switch pattern and collapses the exponential one-switch barrier to O(N) states. Thus one-way lower bounds cannot simply be multiplied or summed to lower-bound alternating DAGs. C-121 explains why this exact common-block router does not extend to all SIZE(s1): every truth-table coordinate can vary in a low point-indicator circuit. The unresolved problem is to route through circuit-dependent constant fibers without storing exponentially many fiber contexts.

## 97. C-171 - Fixed fiber-witness menus need nearly quadratic size

C-115 already implies a useful one-wire witness relation. Define
\[
\operatorname{Fib}(w,z)=\{\{i,j\}: w_i=w_j,\ z_i\ne z_j\}.
\]
It is total on Y x Z: if it were empty, z would be constant on each nonempty fiber of w, hence z=hâˆ˜w for a unary Boolean function h. There are only four such h, each adding O(1) gates to a circuit for w. For sufficiently large n this would put z below s2, contradicting zâˆˆZ.

Now restrict the possible output labels in advance to a fixed edge set E on the N truth-table coordinates. Let G=(V,E), V={0,1}^n. For low w, let G_w keep exactly the edges whose endpoints have the same w-bit. If z is constant on every connected component of G_w, then no edge in E witnesses Fib(w,z). Since E is assumed to cover every wâˆˆY,zâˆˆZ, all 2^{c(G_w)} component-constant tables must lie in SIZE(s2), so
\[
c(G_w)\le \ell:=\log_2 M_2,\qquad M_2=|\mathrm{SIZE}(s_2)|.
\]

Use low rows w=1_H for affine subspaces HâŠ‚F_2^n. Their circuit size is O(n^2), hence at most s1 for large n. Choose m=2^d with 2ellâ‰¤m<4ell; this is below N since ell=O(s2 log(n+s2))=O(N^beta n)=o(N). For every such H of size m,
\[
c(G_{1_H})\ge c(G[H])\ge m-e_G(H).
\]
The component bound therefore forces e_G(H)â‰¥m-ellâ‰¥m/2 for every affine H of that size.

A uniformly random affine d-flat contains any fixed pair of distinct vertices with probability m(m-1)/(N(N-1)). If L=|E|, averaging gives
\[
L\,\frac{m(m-1)}{N(N-1)}\ge m-\ell,
\]
and hence
\[
L=\Omega(N^2/m)=\Omega(N^2/\ell)
 =\Omega(N^{2-\beta}/n).
\]
Every rect-DAG for Fib must contain at least this many distinct output labels, so this is a genuine shared-DAG lower bound for Fib. It rules out a near-linear **fixed pair menu** for the fiber-witness route.

### Exact transfer audit

A Fib-DAG of size L gives a mismatch DAG of size O(L): at a leaf labelled {i,j}, split Alice's rows by their common bit w_i=w_j and Bob's columns by the orientation of z_i,z_j; one of i,j is then a signed mismatch.

The reverse simulation is much costlier. For w of size at most s1-1, run a C-75 mismatch DAG successively on (w,z), (NOT w,z), and (the constant 1-b,z), where the first output is (i,b). The second run yields j with w_j=z_j; the third yields k with z_k=b. If w_k=b, (i,k) witnesses Fib; otherwise, if w_j=b use (i,j), and if w_j=1-b use (j,k). Remembering the first two output labels requires up to O(N^2) copies of the DAG, so
\[
S_{\rm rect}(\mathrm{Fib}_{Y_0,Z})
 \le O(N^2 S_{\rm rect}(\mathrm{Mis}_{Y,Z})),
 \quad Y_0=\mathrm{SIZE}(s_1-1).
\]
Consequently the label bound only yields the vacuous
\(S_{\rm rect}(\mathrm{Mis})\ge\Omega(N^{-\beta}/n)\).
The stronger output relation is therefore not a lower-bound transfer to C-75. This is a quantified route failure, not a Gap-MCSP bound. It says that any useful use of C-115's fiber witness needs a substantially cheaper reverse map or a direct state invariant for mismatch itself.

## 98. C-172 - The global cylinder budget sharpens the state constraint

This strengthens C-129 by counting the non-high tables across all row-signature cylinders at once, rather than allowing up to M2 non-high tables separately in each cylinder.

Let a valid rect-DAG state v have rectangle A_v x B_v, where A_v subseteq Y and B_v subseteq Z. Let K_v subseteq [N] be the coordinates appearing at descendant output leaves, k_v=|K_v|, and P_v=pi_{K_v}(A_v), r_v=|P_v|. For each p in P_v, define the full truth-table cylinder C_p={u in {0,1}^N : u|K_v=p}. These r_v cylinders are disjoint and each has size 2^(N-k_v).

For every p in P_v choose w_p in A_v with w_p|K_v=p. If a high table z in C_p also belonged to B_v, the pair (w_p,z) would reach v and agree on every coordinate that any descendant leaf can output. The suffix below v could not return a valid mismatch, contradicting correctness. Thus B_v is disjoint from Z intersect the union of these cylinders. Since at most M2=|SIZE(s2)| tables in the entire truth-table cube are non-high,

    |Z minus B_v| >= |Z intersect union_{p in P_v} C_p|
                       >= r_v*2^(N-k_v) - M2.                 (C-172)

This holds even when the right side is negative; equivalently take its maximum with zero. C-129's r_v*(2^(N-k_v)-M2) bound remains valid but is weaker. The set form is also useful: every high table whose K_v-restriction is a pattern realized by A_v is excluded from B_v.

### Root consequence and calibration

At the root B=Z, so the union of all cylinders indexed by pi_K(Y) must lie entirely in SIZE(s2):

    |pi_K(Y)| * 2^(N-|K|) <= M2.

Let t=floor(s1/(C n)) for a basis constant C large enough that any pattern on t chosen truth-table coordinates is realized by a size-s1 circuit (OR the corresponding point-minterm indicators). If k=|K|<=t, all 2^k patterns occur, making the left side 2^N>M2, impossible. Hence k>t, |pi_K(Y)|>=2^t, and

    |K| >= N + t - log2(M2).

So the root output support has a slightly stronger explicit lower bound than N-log2(M2). In the OPS range t=Theta(N^beta/n^2) while log2(M2)=O(N^beta*n), so this remains N-o(N), not a superlinear DAG bound.

For an Alice-first one-switch state, all rows in a message class have the same pattern on its descendant output coordinates: for each used coordinate, some Bob input selects that output, and correctness for every row in the class fixes the row bit there. Thus r_v=1 and C-172 recovers the existing N-log2(M2) support bound; C-170's stronger code-packing state count is unchanged.

### Why this still does not charge alternating states

C-135's patching argument gives a fixed set K=[N]\\U with |U|=d=Theta(s1) such that every high z differs from every low w somewhere on K: if they agreed outside U, changing at most d truth-table entries of w would compute z with at most s1+O(nd)<=s2 gates. Therefore a near-full fixed candidate-label set already hits every low/high pair. It is not a routing DAG; choosing a valid coordinate while preserving rectangle states is the unresolved work. This falsifies any attempt to get a superlinear bound from root output-support size alone.

At an internal state, C-172 says that the high columns excluded by its row-signature cylinders are a *global* budget, but different states can exclude overlapping high tables. The C-80 B-to-A-to-B router and C-160's O(N log N) threshold separator remain mandatory counterchecks. No amortized charge over arbitrary alternating states, superlinear rect-DAG bound, rho_prom lower bound, or P-versus-NP result follows. O-131 is the next test: turn the cylinder profile into a path/state potential with controlled overlap, or retire it as a local constraint and return to O-129's general alternating-state problem.

## 99. C-173 - Rectangle decision lists do not directly lower-bound C-75

I checked a recent nearby model rather than treating its alternation results as automatically transferable. Podolskii and Prior's 2025 report studies Boolean rectangle decision lists (Rect-DL): an ordered list of arbitrary combinatorial-rectangle membership queries, with the first satisfied query determining a Boolean output. It proves alternation-depth hierarchies for that model. Its query is a *joint* rectangle-membership test; a standard C-75 rect-DAG node instead branches using one party's local input and must keep every state rectangle-valid.

There is an exact one-way relation. In the top-down rect-DAG definition, every node's feasible rectangle is covered by its children, and every leaf rectangle consists only of inputs for which its output label is valid. By induction, the leaf rectangles cover Y x Z. Listing the leaves in any order and assigning each its mismatch label gives a multi-output rectangle list of length at most the number of leaves, hence at most S_rect. The list need not be disjoint; the first rectangle hit still gives a valid output. But this measure is at most 2N for Mis: simply list the 2N signed mismatch rectangles R_(i,b)={w:w_i=b} x {z:z_i=1-b}. Thus a lower bound on this raw list length cannot yield a superlinear C-75 DAG bound.

The reverse compilation explains the gap. To test a rectangle A x B in a distributed protocol, Alice can first test x in A and Bob can then test y in B. The joint failure set is (A^c x Y) union (A x B^c), which is generally not a rectangle: it contains the two cross corners but omits the success corner A x B. Merging both failure cases into one next-list state is therefore illegal in a rect-DAG; keeping the failed-query context can grow with the list. No small-loss list-to-DAG conversion follows.

The 2025 paper's alternation counts changes in the Boolean outputs along the ordered list, not changes of speaking party in a deterministic protocol DAG. Its techniques could matter only after a new reduction, for example a Boolean output projection forced by every valid mismatch choice, or a lower bound on a richer context-sensitive multi-output list. Neither is available. This closes the direct Rect-DL transfer as a superlinear lower-bound route, while identifying the exact missing resource: remembering which local half of a joint rectangle test failed. It is related to C-137's nonrectangular equal-outcome merge, not a new C-75 bound.

Sources: Podolskii-Prior, *Alternation Depth of Threshold Decision Lists*, ECCC TR25-143, definitions of Rect-DL and its output alternation: https://eccc.weizmann.ac.il/report/2025/143/download; Garg-Goos-Kamath-Sokolov, *Monotone Circuit Lower Bounds from Resolution*, rect-DAG semantics: https://theoryofcomputing.org/articles/v016a013/v016a013.pdf.

## 100. C-174 - A forced output bit has only a linear Rect-DL certificate

Let h:[N] x {0,1}->{0,1} be any Boolean projection of the signed mismatch label. Suppose h is forced on a subpromise Y' x Z': for each pair (w,z), all valid mismatch labels (i,w_i) have the same h-value. Then that forced bit is exactly

    F_h(w,z)=1 iff there exists (i,b) with h(i,b)=1, w_i=b, z_i=1-b.

This is a disjunction of at most 2N rectangles. Listing the h=1 mismatch rectangles first and using default output 0 is a Rect-DL of length at most 2N and at most one output-value switch. Therefore no lower bound on Rect-DL *length* for a forced output projection can exceed 2N. The active transfer target for rho through the current compiler is larger than N^(3+3epsilon)/log N, so O-132's proposed Rect-DL-size route is quantitatively incapable of reaching it, regardless of how clever h is. This does not rule out a direct rect-DAG lower bound on F_h; it closes only the proposed decision-list transfer.

Two natural forced projections are even simpler:

1. If h(i,b)=b (or h(i,b)=b xor p_i for fixed coordinate flips p_i), forcedness says every pair is coordinatewise comparable after those flips. The bit is determined by which table has larger Hamming weight. Alice can send her weight in O(N) states and Bob compares his, so the induced Boolean function has an O(N)-state protocol DAG.
2. If h depends only on a block label phi(i), forcedness means every cross pair differs in exactly one block. Treat each block restriction as one symbol. The low and high row-pattern sets form a complete bipartite subgraph of the corresponding Hamming graph. If both sides have at least two distinct patterns, either every cross difference is in one fixed block, or the only nonconstant case is a 2-by-2 square on two blocks. Thus the block output is constant or the nonconstant part has only four input pairs.

The first statement closes O-132's generic Rect-DL-size hope; the examples also kill its simplest sign and coordinate-block encodings. Any remaining output-projection route must use a different hard measure and prove a direct transfer to rect-DAG size. No S_rect, rho_prom, or P-versus-NP lower bound follows.

## 101. C-175 - Conflict cylinders have owner-sensitive laws, but raw exclusions overcount

For a rect-DAG state v with feasible rectangle A_v x B_v, let K_v be its descendant output coordinates and define

    C_v = {z in {0,1}^N : exists w in A_v with z|K_v = w|K_v}.

Correctness gives B_v intersect C_v = empty. C-172 counts the size of C_v intersect Z. The state recursion also gives owner-sensitive inclusions. If Alice locally chooses between children 0 and 1, their row sets partition A_v, their column sides both contain B_v, and K_v=K_0 union K_1; hence C_v is a subset of C_0 union C_1 and B_v avoids both child conflict sets. If Bob locally chooses, both children retain A_v and their column sides partition B_v; then C_v is a subset of C_0 intersect C_1 and B_v avoids that intersection. These laws identify a potential interaction term, but alone they do not charge states globally.

### Explicit overlap stress test from C-80

Take m=2^r prefix blocks of equal size L=N/m, with m=Theta(s1/n) and a sufficiently small constant. Every table constant on each block is a function of the first r input bits and has circuit size O(mr)<=s1. Since beta<1/2, L=Theta(N^(1-beta)n^2) dominates log M2=O(N^beta n). The family of tables that are constant on all but exactly one block has size

    m * 2^(m-1) * (2^L-2) > M2.

So some high table z* is mixed on exactly one block. In fact every high table is mixed on at least one block, because a table constant on all blocks is low.

There is an O(N)-vertex B-to-A-to-B rect-DAG for this restricted low family: Bob scans blocks until finding a mixed block j; Alice gives the low row's constant bit on j; Bob scans that block for the opposite z-bit. At the block-j state v_j, A_vj is the full block-constant low family, B_vj consists of high columns whose earlier blocks are constant and block j is mixed, and K_vj is block j. Its row signatures are the two constant patterns, so C_vj is the set of all tables constant on block j.

For every j>=2, |B_vj|<=2^(N-L+1), because even ignoring the current mixed condition the first block must be constant. Since L grows and |Z|=(1-o(1))2^N, each such state excludes (1-o(1))|Z| high columns. Thus

    sum_j |Z minus B_vj| = Omega(m |Z|)

for a graph with only O(N) vertices. The same high table z* is counted in C_vj intersect Z for every j other than its unique mixed block, so the overlap is literal, not just a volume artifact. C-172's per-state cylinder volumes cannot be summed over states, even after using the one-global-M2 correction.

**Next invariant.** Any useful O-131 potential must weight exclusions by reachable path context or by conditional column mass inside the parent rectangle. Absolute complements Z\\B_v repeat the same high columns across many unused branches. The block router is the stress test; a generic exclusion-volume sum is retired. This is still only a subpromise calibration, not an upper bound for the full SIZE(s1) x Z relation.
## 102. C-176 - Parent-conditioned cross-conflict is path-safe but has no forced mass

C-175 suggests weighting a child conflict by the parent context. Test the most direct version. At a Bob-owned node u with children v0,v1, let the child rectangles be A x B0 and A x B1, with B0,B1 partitioning the parent column set. Let C_i be the descendant-output conflict set of child vi. Correctness gives Bi intersect Ci = empty. For a path that takes child i, call z a cross-conflict at u when z belongs to C_(1-i). Under any distribution mu on Y x Z, define Phi_mu as the expected number of Bob nodes on the actual path where this happens.

This quantity avoids C-175's raw off-path overcount: each charge is attached to a reached parent and its selected child. It also satisfies only the easy direction
    Phi_mu <= expected path length <= maximum path length <= S_rect.
That is an upper bound by DAG size, not a lower bound.

There is no positive per-pair lower bound. Use the C-80 block-constant low family with m blocks of size L, m=Theta(s1/n), beta<1/2, and L >> log M2. Fix a low row w and let b be its bit on block 1. Consider tables z that are mixed on every block, have z_1=z_2=1-b, and have at least one b later in block 1. There are
    (2^(L-2)-1) (2^L-2)^(m-1) > M2
such tables for the project parameters, so at least one is high.

In the C-80 router, Bob selects the mixed branch at block 1. The selected child is outside the sibling continuation conflict set because z is mixed on every later block, while every low row is constant on each block. Alice reports b. Bob then scans block 1 and outputs the mismatch at its first coordinate. At this scan node z is outside the sibling continuation conflict set because z_2=1-b; it is also outside the mismatch-leaf conflict set because z_1=1-b. There are no further Bob decisions on this path. Thus this valid low/high pair has Phi_mu=0 under its point-mass distribution, even though the router is correct.

Conclusion: parent-conditioned cross-conflict fixes literal overlap accounting but is not a mandatory witness of successful routing. Close it as a standalone state-charge potential. O-131 remains only as the broader search for a residual-state/non-shareability invariant that can force many distinct DAG vertices; path mass and conflict volume alone do not provide it. This is no S_rect, rho_prom, or P-vs-NP lower bound.

The next useful state object is the full residual contract (A_v, B_v, suffix routing behavior, K_v) together with the incoming history contexts. Projection disjointness on K_v is necessary for a shared suffix, but only says that every pair has some available mismatch label; it does not construct a suffix that routes to one. A lower bound would have to show that many histories cannot merge into one correct acyclic suffix for the whole product hull, despite the easy pairs and O(N)-state C-80 router.

## 103. C-177 - Local-PRG transfer to the gap promise, with the model and parameter losses

A useful nearby theorem is the local-PRG method for MCSP. Let H be any total Boolean separator that accepts every table in SIZE(s1) and rejects every table outside SIZE(s2). Its behavior on the medium band is unrestricted. Since
    M2 = |SIZE(s2)| <= 2^(O(s2 log(s2+n))) = 2^o(N)
for fixed OPS beta<1, a uniform N-bit table is accepted with probability at most M2/2^N = 2^(-N+o(N)). If G is a generator whose every output table has circuit size at most s1, then H(G(seed))=1 on every seed. Therefore G cannot fool H with error below 1-o(1).

This gives an exact gap version of the local-PRG obstruction: any size-S device H in a model fooled by G must have generator locality lambda(N,S)>s1. It does not require exact MCSP behavior on the medium band.

For general branching programs, Cheraghchi-Kabanets-Lu-Myrisiotis give a local PRG with
    lambda(N,S) = S^(1/2) * 2^(O(sqrt(log S)))
(Lemma 24); their Theorem 2 for exact MCSP follows by setting the locality threshold near N/log N. Applying the same generator to the gap argument yields only
    S >= s1^(2-o(1)) = N^(2 beta-o(1))
in the OPS parameterization s1=N^beta/(c n). Magnification requires every sufficiently small fixed beta, so choose beta<1/2; this lower bound is o(N) and is weaker than the project's existing N-o(N) rect-DAG floor.

There is also a model mismatch: the cited theorem lower-bounds standard branching programs and formulas, whereas the C-75 rect-DAG is equivalent, up to constant factors, to an unrestricted Boolean separator circuit. No polynomial simulation from that circuit/rect-DAG model to the cited branching-program model is established here. Thus C-177 is a rigorously quantified restricted-model route failure, not a C-75 or rho lower bound.

The only version that reaches the live target directly would be a generator that (i) fools every size-S Boolean separator circuit for the actual low/high promise and (ii) has every output table in SIZE(s1), with S>N^(1+epsilon). This is a concrete PRG formulation of the same hard separator problem; no such generator is known from the cited construction. Sources: [Cheraghchi et al., ICALP 2019](https://drops.dagstuhl.de/storage/00lipics/lipics-vol132-icalp2019/LIPIcs.ICALP.2019.39/LIPIcs.ICALP.2019.39.pdf), [OPS, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).


## 104. C-178 - Short descriptions, existential projection, and shared residual cuts

Let Y=SIZE(s1), Z={0,1}^N minus SIZE(s2), and M2=|SIZE(s2)|. A Boolean separator H for (Y,Z) is exactly a circuit whose accepting set A satisfies Y subseteq A subseteq SIZE(s2): completeness gives the first inclusion, and rejecting every table outside SIZE(s2) gives the second. Conversely every such sparse envelope is a valid separator. Thus the minimum sparse-envelope circuit size SepCirc(Y,Z) equals Theta(S_rect(Mis_Y,Z)) by the established Sokolov circuit/rect-DAG correspondence.

Now let D be descriptions of circuits of size at most s1, and let V(d,x) mean that x is exactly the truth table of the circuit encoded by d. The low-class predicate is the existential projection chi_1(x)=exists d in D: V(d,x). A gap separator computes some H with chi_1(x) <= H(x) <= chi_2(x), where chi_2 is the corresponding projection for size s2; medium tables may receive either value. A universal circuit computes V(d,x) with d supplied. It does not remove the existential quantifier over d. The direct construction ORs one N-bit equality test x=TT(C_d) per description, costing O(N|D|) gates. With |D|<=2^(O(s1 log(s1+n))) and s1=N^beta/(c n), this is N*2^(O(N^beta)), superpolynomial for every fixed beta>0. This is an explicit bound for description enumeration, not a lower bound against compressed projections or alternating DAGs.

The low communication strategy remains cheap: Alice sends d in O(s1 log(s1+n)) bits; Bob computes TT(C_d), scans it against z, and returns a differing coordinate using O(log N) additional bits. The corresponding one-switch tree has an exponential description frontier (C-170). Relabeling rows by descriptions preserves rect-DAG size exactly (C-162). Therefore per-row short descriptions do not by themselves provide shared-gate compression.

Here is the precise merge requirement. If incoming history rectangles are R_j=A_j x B_j and the common standard rect-DAG state has reachable rectangle A_* x B_* containing their product hull, its suffix is itself a solver for Mis restricted to A_* x B_*. If that suffix has t nodes, the minimum separator size SepCirc(A_*,B_*) is O(t). A proof of non-shareability must therefore lower-bound residual separator complexity for many such hulls and charge those suffix costs across the DAG. Projection-support disjointness only says some mismatch exists; it gives no circuit-size bound. At the root SepCirc(Y,Z) is the original target. This sharpens Q132 into an explicit residual-complexity obligation but yields no superlinear bound.

The transfer target remains: a standard rect-DAG lower bound must exceed N^(3+3epsilon)/log N to force rho_prom>N^(1+epsilon) through the current compiler; a direct cyclic-cover lower bound avoids that loss. No P-vs-NP consequence follows from C-178.



## 105. C-179 - One-shot affine fingerprints need almost full rank

C-168 rules out an Alice-chosen set of candidate coordinates of size below N-log2(M2). The same cylinder count applies to arbitrary parity sketches, including a sketch selected separately for each low row.

Fix w in Y and an affine map L_w(x)=A_w x+b_w over F_2, where A_w has r output coordinates. Suppose equality of sketches is never possible for a high table: L_w(z) != L_w(w) for every z outside SIZE(s2). The collision set is the affine coset

    {z : L_w(z)=L_w(w)} = w + ker(A_w).

It has exactly 2^(N-rank(A_w)) elements. By the assumed separation it contains no high table, so it is a subset of SIZE(s2), whose cardinality is M2. Therefore

    rank(A_w) >= N-log2(M2), and r >= N-log2(M2).

In the OPS range log2(M2)=O(s2 log(s2+n))=O(N^beta n)=o(N) for fixed beta<1. Thus every such one-shot affine fingerprint needs N-o(N) independent parity bits. Coordinate sampling is the special case where A_w selects coordinate rows. The proof permits the affine map to depend on w; its collision coset still has the same size.

This is only a no-go for a nonadaptive affine synopsis whose equality is meant to certify that the pair is not low/high. It neither lower-bounds arbitrary nonlinear fingerprints nor applies to adaptive rect-DAGs that use sketch collisions to continue routing. It also does not by itself output a mismatch coordinate. A near-linear universal DAG, if one exists, must use some other form of adaptivity or nonlinear structure. Record C-179 as a stronger route filter for Q135, not as a bound on S_rect or rho_prom.



**Nonlinear-synopsis stress test.** Message length alone does not give a lower bound: for a fixed low table w, the one-bit predicate h_w(x)=1[x=w] separates w from every high table because w is non-high. Its equality circuit costs O(N) gates and changes with w. The unresolved cost is making these row-specific tests work together on all low/high pairs in one shared DAG.



## 106. C-180 - Adaptive parity decision trees have near-N depth

Extend the affine-fingerprint test from C-179 to a deterministic adaptive parity decision tree T computing any Boolean separator H for (Y,Z). At each node T queries an affine linear form of the N input bits; later queries may depend on earlier answers. Fix w in Y and let t(w) be the number of queries on its path. The path fixes t(w) affine equations. Their common solution set C_w is a nonempty affine subspace of dimension at least N-t(w), and every x in C_w follows the same path as w. Since H(w)=1, no high table can belong to C_w; hence C_w subseteq SIZE(s2). Counting gives

    2^(N-t(w)) <= M2,
    t(w) >= N-log2(M2) = N-o(N).

The argument permits arbitrary adaptivity in choosing parity checks, but the computation is a decision tree whose output is a one-input separator. It does not bound a shared parity branching program: merged paths can have a union of different affine contexts, and a depth lower bound of N-o(N) still permits an O(N)-node chain. It also does not model the two-party mismatch search, where the output is a coordinate rather than the separator bit. C-180 is a proved restricted-model depth bound and a failed route to the superlinear shared-DAG target.



## 107. C-181 - Stronger local PRGs still miss the small-beta DAG target

I checked the STACS 2021 branching-program local-PRG result of Cheraghchi, Hirahara, Myrisiotis, and Yoshida. Their construction gives local pseudorandomness against nondeterministic, co-nondeterministic, and parity branching programs with output locality parameter lambda(S)=S^(2/3+o(1)) for size S; they derive an N^(3/2-o(1)) exact-MCSP lower bound near the largest circuit-size threshold.

The gap transfer itself is direct. Let H be a size-S separator for Y=SIZE(s1) and Z={0,1}^N minus SIZE(s2). Under uniform input, Pr[H=1]<=M2/2^N=2^(-N+o(N)). Every output of a local generator with locality at most s1 lies in Y, so H accepts every generator output. If H belonged to a branching-program class fooled by that generator, this acceptance gap would contradict fooling. Hence lambda(S)>s1, which gives

    S >= s1^(3/2-o(1)) = N^(3 beta/2-o(1)).

This is a valid promise-gap adaptation for those branching-program models, including unrestricted deterministic branching programs when the cited PRG applies. It remains below N for beta<2/3, and below N^(3/4) throughout the required OPS range beta<1/2. The read-once co-nondeterministic HSG has locality around sqrt(N) up to polylogarithmic factors, so it also does not reach s1 for small beta. Neither result transfers to the C-75 rect-DAG, which is equivalent to an unrestricted separator circuit rather than a branching program. This is a stronger restricted-model calibration than C-177, but it changes no S_rect, rho_prom, or P-vs-NP bound. Source: [Cheraghchi et al., STACS 2021, Theorem 5 and local-HSG discussion](https://drops.dagstuhl.de/storage/00lipics/lipics-vol187-stacs2021/LIPIcs.STACS.2021.23/LIPIcs.STACS.2021.23.pdf).

## 108. C-182 - One output fiber holds a dense mismatch witness

This continuation follows C-74/C-75 and does not reopen other P-vs-NP routes. Let N=2^n, Y=SIZE(s1), Z={0,1}^N minus SIZE(s2), and M2=|SIZE(s2)|.

### Exact search relations and cost accounting

The ordinary C-75 relation is
\[
\mathrm{Mis}_{Y,Z}(w,z)=\{(k,b):w\in Y,\ z\in Z,\ w_k=b,\ z_k=1-b\}.
\]
Alice knows w (or a circuit description d with TT(C_d)=w); Bob knows z. Its domain is the full product Y x Z, and it is total because Y and Z are disjoint.

For a proposed fusion list Q=((E_i,H_i))_{i=1}^q, set T_i=E_i intersect H_i and let x_i(v) be its least-fixed-point activation bit. The Q-path relation outputs a finite sequence of rule indices and selected sides, ending at (k,b). It starts at an empty-carrier i with x_i(w)=1,x_i(z)=0. At each state, Bob selects a side S absent from z's closure; Alice supplies either a matching literal G_{k,b} subset S with w_k=b, or a rule j with T_j subset S and x_j(w)=1. In either case x_j(z)=0; a rule transition strictly decreases the first activation round tau_j(w). A literal terminal has z_k=1-b. This path relation is total on Y x Z exactly when Q refutes every low anchor. Plain Mis is total regardless of Q.

Communication and tree size are different resources. Alice can send a size-s1 circuit description using O(s1 log(n+s1)) bits; Bob compares its truth table with z and returns a mismatch index, giving
\[
\log_2(N-\log_2 M2)\ \le\ CC(\mathrm{Mis}_{Y,Z})\ \le\
O(s1\log(n+s1)+\log N).
\]
For the lower bound, let K be the set of coordinate labels appearing at protocol leaves. If |K|<N-log2(M2), the cylinder of tables agreeing with any fixed low w on K has more than M2 elements, so it contains a high z and the pair has no output among the leaves. Thus there must be at least N-log2(M2)=N-o(N) distinct output coordinates and at least that many leaves; communication is at least log2(N-log2(M2))=n-o(1). The Q-path protocol uses O(q log(q+N)) bits by sending a side and support index at each of at most q steps. A binary protocol of cost c has at most 2^(c+1)-1 tree nodes, so these bit bounds give only exponential tree-size bounds. A rect-DAG is a distinct graph-size measure; no tree/DAG equality is asserted.

### Exact model boundary and transformations

The audited primary definitions give the following inequalities, with no hidden identification:
\[
q_{\min}=\rho_{\rm prom}=D^\circ_\cap(Y\mid\mathcal B_{\rm prom}),
\qquad
D^\circ_\cap\le D_\cap\le(D^\circ_\cap)^2,
\qquad
\rho_{\rm prom}\le O(S_{\rm rect})\le O(\rho_{\rm prom}^3/\log\rho_{\rm prom}).
\]
Here the cover universe is exactly Gamma_prom=Y disjoint-union Z, U=Z, and generators are the 2N literal slices restricted to Gamma_prom. The D-circ identity is cyclic set construction with least-fixed-point iteration; its resource counts intersections, with unions free. The middle inequality is only an acyclic AND-count bound. The last upper compiler pays for binary support routing and acyclicization; C-100 improves its generic total-size form to O(q^3/log q), not O(q^2).

A successful Q induces q rule rectangles
\[
R_i=(\{w:x_i(w)=1\})\times(\{z:x_i(z)=0\})
\]
and a ranked cyclic support graph with up to 2N output labels and O(q^2+qN) possible support arcs. For each fixed pair, the selected path terminates because tau strictly falls. The static graph can cycle. This exact q-state object is not an acyclic Sokolov/GGKS rect-DAG. Conversely, an L-vertex rect-DAG for Mis gives an O(L)-size Boolean separator: at a signed-mismatch leaf use its literal; at a two-child rectangle split combine child separators by AND, OR, or copy according to the rectangle-cover trichotomy. The ordinary fusion construction then gives rho_prom<=O(L). Thus standard rect-DAG and promise-separator circuit sizes are Theta-equivalent, while the cover-to-DAG direction currently has a cubic/log loss. The full-domain cover is a different parameter because medium-complexity tables are excluded from Gamma_prom.

The primary-literature comparison is therefore: Sokolov's Boolean games and GGKS rect-DAGs are acyclic, binary-outdegree rectangle systems; GGKS's exact monotone-circuit identity is for the full monotone KW relation, not this signed promise relation. Nakayama-Mar(u)oka loop circuits are a methodological ancestor, not identical to the semi-filter/intersection measure: Cavalar-Oliveira explicitly adapt the result to their set-theoretic cover. Amano-Mar(u)oka conjunctive complexity is the acyclic AND-count analogue, but their results are for quadratic functions and need an AND-preserving transfer before they apply here. Primary references: [Sokolov](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download), [GGKS](https://theoryofcomputing.org/articles/v016a013/), [Cavalar-Oliveira](https://doi.org/10.1145/3718746), [Nakayama-Mar(u)oka](https://doi.org/10.1006/inco.1995.1083), [Amano-Mar(u)oka](https://doi.org/10.1007/s00453-006-0073-0).

### One mixed output fiber, and the precise failure to share it

Use only the output wire of C, so k=1 and the partition has at most two cells F_b={x:w(x)=b}. On each nonempty cell let h take the majority z-value; on an empty cell assign either value. Then h=psi(w) for a one-bit lookup psi, so C plus a constant-size lookup computes h with size s1+O(1)=o(s2). If h differs from z at r points, patching those points with minterms of O(n) gates each computes z with size s1+O(1)+O(rn); since z is high, r=Omega(s2/n). The minority counts across the nonempty cells sum to r, so one cell has minority count Omega(s2/n). It is mixed. Since w is constant on that cell, its number of w/z mismatches is at least the minority count. Thus one of the two output fibers contains Omega(s2/n) mismatches. This argument also covers a constant w, when one cell is empty. The partition is simple, but which fiber is mixed still depends on z.

The direct scanner test fails at the product-hull step. Consider the proposed fully merged scan with one full-domain state Y x Z per stage and a suffix that outputs only at later scan positions. At a candidate output fiber b and coordinate i, let A1 be rows with w_i=b, A0=Y minus A1, B0={z:z_i=b}, and B1=Z minus B0. A mismatch is certified on A1 x B1. The two natural continuation pieces A0 x Z and A1 x B0 cannot be merged into one rectangle without taking the product hull Y x Z, which restores A1 x B1 pairs that already mismatched at i. This merge is actually invalid at late stages: number the positions in scan order, choose i with 2^(i-1)>M2, and take any w in A1, so b=w_i. Set z_i=1-b and set z equal to w at every later-scanned position, leaving the i-1 earlier positions free. There are more than M2 such completions, so at least one is high. The pair (w,z) lies in the merged hull, mismatches at i, and agrees on every coordinate the suffix scans, so the suffix cannot solve its full rectangle. Such late stages exist because log2(M2)=o(N). This kills the fully merged, unfiltered scanner. A scanner that keeps filtered contexts, or a general DAG that revisits coordinates/routes differently, is not covered; this is not a lower bound for arbitrary alternating rect-DAGs.

This candidate is subordinate to C-115/C-120/C-121 and C-133/C-170: it reduces the number of row-dependent cells but does not solve their shared selection problem. The strongest current falsification statement remains C-178: short descriptions give a verifier V(d,x), while the one-table separator requires eliminating the existential description d. The direct OR over descriptions is N*2^(O(s1 log(n+s1))); no N^(1+o(1)) universal DAG or arbitrary-DAG obstruction was obtained in this round.

**Status.** This is Tier 5 calibration only. There is no new superlinear rect-DAG or rho bound, no near-linear universal DAG, and no P != NP consequence. Keep the live target at O-133/Q134: either construct a compact circuit for a sparse envelope SIZE(s1) subseteq A subseteq SIZE(s2), or prove residual-context non-shareability for product hulls with a quantitative charge exceeding N^(3+3epsilon)/log N (or improve the q compiler).

## 109. C-183 - Selecting the mixed output fiber is itself nonrectangular

C-182 proves that for every low/high pair at least one output fiber of the low row is mixed by the high table. It does not show that one party can identify that fiber locally. The following 2-by-2 submatrix makes the obstruction exact.

Choose three distinct input addresses p1,p2,p3. Let wA be 0 exactly on {p1,p2} and 1 elsewhere; let wB be 0 exactly on {p1,p3} and 1 elsewhere. These truth tables have O(n)-size circuits (two point indicators and a negation), hence belong to Y for the project parameters. For each restriction below, N-3 > log2(M2) for sufficiently large n, so its completion cube contains more than M2 tables and therefore contains a high table. Choose z0 in Z with z0(p1,p2,p3)=(0,0,1), and z1 in Z with z1(p1,p2,p3)=(0,1,0).

Let M0(w,z)=1 exactly when z is nonconstant on the entire zero-output fiber F0(w)={x:w(x)=0}. Here F0(wA)={p1,p2} and F0(wB)={p1,p3}, so

                 z0       z1
    wA            0        1
    wB            1        0

This XOR matrix is not a rectangle. In particular, the two valid M0=1 pairs cannot be merged into one product rectangle: its product hull contains the two invalid diagonal pairs. Thus the mixed-fiber label is genuinely joint in (w,z); the existence of a dense mixed fiber does not supply a Bob-local choice or a single rectangle transition.

**Scope.** This rules out only the direct step that Bob selects the mixed output fiber and then the parties search inside it, when that selection is one product-rectangle branch. It does not rule out a bounded multi-rectangle selector, an alternating rect-DAG, or another router, and it gives no superlinear DAG or fusion-cover lower bound. The next target is to quantify the residual rectangles needed to select and reuse a fiber, or construct a bounded-switch router that passes C-80 and C-160. The failed implication was: pairwise witness density does not imply constant-cost shared-state addressability.

## 110. C-184 - Circuit complexity is conserved across a low-defined partition

Fix a low truth table w computed by a circuit C of size at most s1. Let F_b={x:w(x)=b}. Define e_b(w,z) to be the minimum size of a Boolean circuit D_b that agrees with z on F_b; D_b is unconstrained outside F_b. This is an extension complexity, not the circuit complexity of the restricted function in a separate address encoding.

A one-bit multiplexer gives the exact inequality
\[
CC(z) \le CC(w)+e_0(w,z)+e_1(w,z)+O(1).
\]
Indeed, choose minimum extensions D_0,D_1 and output (not C AND D_0) OR (C AND D_1). On each input address, C selects the extension for the fiber containing that address, so the result equals z everywhere. Therefore, if CC(z)>s2 and CC(w)<=s1,
\[
e_0(w,z)+e_1(w,z)>s2-s1-O(1).
\]
In the OPS regime s1=o(s2), at least one output fiber has extension complexity at least (1/2-o(1))s2. Empty fibers have constant-size extensions, so the hard fiber is nonempty. It cannot have a constant trace either. More quantitatively, let r_b be the minority count of z on F_b. A constant circuit patched at the r_b minority points gives an extension of size O(1+r_b n), so the hard fiber satisfies r_b=Omega(s2/n). Its mismatch count is at least r_b, whether the majority value agrees with w on that fiber or not. Thus the same fiber is both extension-hard and mismatch-dense.

More generally, let g_1,...,g_k be k address predicates computed by circuits of total size a, and let F_u={x:(g_1(x),...,g_k(x))=u} for u in {0,1}^k. Let e_u be the minimum circuit size of an extension agreeing with z on F_u. A k-bit decoder and multiplexer combine all these extensions:
\[
CC(z)\le a+\sum_u e_u+O(k2^k).
\]
Thus a high z forces
\[
\sum_u e_u> s2-a-O(k2^k),
\]
and some cell has extension complexity greater than (s2-a-O(k2^k))/2^k. This is a circuit-complexity chain rule for a partition computed by low circuits.

**Proof status and limit.** The inequalities are proved by explicit circuit composition. They strengthen C-182's local picture: the same output fiber carries Omega(s2/n) mismatches and has extension complexity at least (1/2-o(1))s2. They do not identify that fiber from either party's input, and C-183 shows even the simpler mixed-fiber predicate is not a rectangle. The rule is not a lower bound on rect-DAG size or rho_prom. The live question is whether extension complexity can be made into a residual-state potential that survives arbitrary product-hull merges.

## 111. C-185 - Pointwise residual hardness does not price shared-DAG size

C-184 is a pairwise statement: for each fixed (w,z), some output fiber F_b(w) has large extension complexity. C-121 gives a direct countercheck to using that number as a DAG potential. Suppose the low rows in a subpromise are constant on one fixed partition Pi={C_1,...,C_m}, and the partition label plus a lookup on its cells has circuit size below s2. Then every high z is mixed on at least one common cell C_j. Bob selects such a cell, Alice supplies the common bit w|C_j, and Bob scans C_j for a mismatch. The resulting rect-DAG has O(N+m)=O(N) vertices.

Nevertheless, for every low/high pair in this same subpromise, C-184 still forces an output fiber of w with extension complexity at least (1/2-o(1))s2 and Omega(s2/n) mismatches. The router is cheap because it uses the fixed shared partition Pi, not because the pairwise hard output fiber is easy.

**Disposition.** Any potential depending only on max_b e_b(w,z), or on the pairwise sum of extension complexities, cannot by itself imply a superlinear rect-DAG lower bound. This is a proved route filter, not a counterexample to the unrestricted target: the full SIZE(s1) family has no common coarse partition respected by every row (C-121). The surviving target is variation/addressability of residual hard cells across pairs inside each state, with product-hull safety. Stress-test any proposed invariant against C-80/C-121 before using it.
## 112. C-186 - Sparse point indicators force many unfiltered partition contexts

Let r be an integer with r n=O(s1), and consider the low family
\[
Y_r=\{\delta_S: S\subseteq[N],\ |S|=r\},
\]
where delta_S is 1 exactly on the r selected truth-table addresses. Each member has an O(rn)-size circuit, so Y_r is contained in SIZE(s1).

Suppose a subfamily A_j of Y_r consists entirely of tables constant on a fixed partition Pi_j of [N] into at most m cells. A member delta_S in A_j must have S equal to a union of whole cells. Since cells are nonempty and |S|=r, at most r cells can be selected. Therefore
\[
|A_j|\le \sum_{i=0}^{r}\binom{m}{i}.
\]
Consequently any cover of Y_r by such subfamilies needs
\[
T\ge \frac{\binom Nr}{\sum_{i=0}^{r}\binom mi}.
\]
When m>=r, standard binomial estimates give \(T\ge(N/(e m))^r\). When m<r, the denominator is at most 2^r, so \(T\ge(N/(2r))^r\). In particular, if m=O(s2), r=Theta(s1/n), and s2=o(N), then this full-column common-partition cover number is at least
\[
\exp\!\left(\Omega\!\left(r\log\frac{N}{\max\{s2,r\}}\right)\right),
\]
which is superpolynomial for the usual fixed-exponent OPS parameters.

**Router interpretation.** For a fixed partition Pi with label cost t and t+O(m)<s2, every high table is mixed on some cell, so C-121 supplies an O(N+m) mismatch router for any low subfamily constant on Pi against the full high side Z. C-186 shows that covering even the sparse low family by many such *unfiltered, full-column* partition contexts requires an enormous number of contexts. This rules out the naive strategy of covering all low anchors by a small menu of C-121 routers.

**Scope.** This is not a lower bound on arbitrary rect-DAG size. A general DAG may first filter Bob's columns, may share suffix states across different partitions, and need not route by a common partition at all. C-133/C-160 remain the relevant counterchecks. The next question is whether such column filtering can reduce the partition-context count without creating invalid product hulls.

## 113. C-187 - Hamming-ball subpromises have linear-size separators

Fix a center `u in {0,1}^N` with circuit complexity at most `s1`, and an integer `R >= 0` such that
\[
s_1+C Rn+C < s_2,
\]
for a sufficiently large absolute constant `C`. Define
\[
A(u,R)=\{w\in\mathrm{SIZE}(s_1):d_H(w,u)\le R\}.
\]
If a high table `z notin SIZE(s2)` had `d_H(z,u) <= R`, a circuit for `u`, patched at those at most `R` truth-table addresses by `O(n)`-gate minterms, would compute `z` using at most `s1+O(Rn)+O(1)<s2` gates. Hence every high table lies outside this ball.

The `N`-bit Boolean function
\[
H_{u,R}(v)=\mathbf 1[d_H(v,u)\le R]
\]
has an `O(N)`-gate circuit. Each mismatch bit `v_i xor u_i` is either `v_i` or its negation. Compute their population count with 3:2 full-adder compressors: each compressor reduces the total number of bit tokens by one, so at most `N` compressors leave at most two bits in each of `O(log N)` columns; one final addition and comparison to `R` use `O(log N)` more gates. Thus `H_{u,R}=1` on `A(u,R)` and `H_{u,R}=0` on all high tables. By the Boolean-circuit/rect-DAG correspondence (C-89),
\[
S_{\rm rect}(A(u,R),Z)=O(N).
\]

**C-186 application.** Take `u=0^N`. If `rn=O(s1)` and `s1=o(s2)`, choose `R>=r` with `O(Rn)<s2`. Then every `r`-point indicator lies in this ball, while every high table lies outside it. The sparse family `Y_r` from C-186 therefore has an `O(N)`-vertex mismatch rect-DAG against the full high side. This does not contradict C-186, which counts only unfiltered full-column common-partition routers.

**Static-menu calibration.** The center can be hardwired at linear cost for one ball, but the low class is not one ball. In the C-80 block-code family, distinct codewords have distance at least \(\Theta(N/s_1)\), whereas a safe radius is \(O(s_2/n)\). For fixed OPS exponent \(\beta<1/2\), \(N/s_1\gg s_2/n\), so each fixed-center ball contains at most one codeword and a static menu needs \(2^{\Omega(s_1)}\) centers. This is only a lower bound for that static architecture: an alternating DAG may synthesize or select row-dependent structure without explicitly listing centers. C-160 remains a required calibration for any global charge.

**Disposition.** C-187 is a proved local upper bound and shows that C-186's context count is not a general filtering cost. For this subpromise, the reverse rect-DAG-to-fusion transfer also gives an O(N) promise-domain cover. It gives no lower bound on \(S_{\rm rect}(Y,Z)\), no upper or lower bound on the full-promise \(\rho_{\rm prom}\), and no P-vs-NP consequence. The unresolved issue is global sharing of center-dependent tests (or another separator) across far-apart low rows while preserving product-hull correctness.

**Prior-art and novelty check.** The perturbation inequality used above is not new: the project already has the point-patching bound in C-49/C-136, and Krinkin explicitly states \(|CC(f)-CC(g)|\le c_B n\,d_H(TT(f),TT(g))\) for fixed finite complete gate bases ([2026 preprint](https://arxiv.org/abs/2603.09379)). The C-187 contribution is only the separator application to fixed-center subpromises and the C-186 countercheck. Cadoli, Donini, Liberatore, and Schaerf's *k-Approximating Circuits* studies adding input points near a Boolean function's support; its Hamming space is the function's input domain, so it is related terminology but not the truth-table perturbation statement used here ([ECCC TR02-067](https://eccc.weizmann.ac.il/report/2002/067/)). No lower-bound technique is obtained from either source.

## 114. C-188 - Center selection is approximate learning, with a one-way transfer

The fixed-center construction generalizes to the union of balls around all low tables. Let Y=SIZE(s1), choose an integer R satisfying
\[
s_1+\kappa Rn+\kappa<s_2,
\]
and define
\[
\mathcal N_R(Y)=\{v\in\{0,1\}^N:\exists w\in Y,\ d_H(v,w)\le R\}.
\]
Point-patching gives \(Y\subseteq\mathcal N_R(Y)\subseteq\mathrm{SIZE}(s_2)\). Thus, if its indicator has a small circuit, it is a valid sparse envelope for the full promise. Membership asks for the existential projection
\[
\exists\text{ a size-}s_1\text{ circuit }C\text{ and an error set }E,\quad |E|\le R,\quad v=TT(C)\oplus 1_E.
\]
Each fixed-center threshold \(d_H(v,TT(C))\le R\) costs O(N); selecting the low circuit C is the global problem.

There is a published bridge to learning theory. Oliveira et al., *Beyond Natural Proofs: Hardness Magnification and Locality*, Lemma 34, converts a non-adaptive membership-query learner for size-s circuits, with hypotheses of size t and error at most epsilon/2, into an approximate-MCSP separator of size \(O(N\,\mathrm{poly}(t/\epsilon))\). Choose t=s1 and epsilon>0 so
\[
s_1+\kappa\epsilon Nn+\kappa<s_2.
\]
If a high table were epsilon-approximated by a size-s1 hypothesis, patching its at most epsilon*N errors would compute it below s2. Every z in Z is therefore a NO instance of the approximate promise, so a separator for that approximate promise also separates the project promise. At \(s_1=\Theta(N^\beta/n)\), \(s_2=\Theta(N^\beta)\), one may take \(\epsilon=\Theta(N^{\beta-1}/n)\), giving \(t/\epsilon=\Theta(N)\). The stated size loss is \(N\,\mathrm{poly}(N)\), with no fixed polynomial degree in the lemma; this does not meet the project transfer target. Source: [Oliveira et al., ITCS 2020, Lemma 34](https://drops.dagstuhl.de/storage/00lipics/lipics-vol151-itcs2020/LIPIcs.ITCS.2020.70/LIPIcs.ITCS.2020.70.pdf).

**Failed implication.** Lemma 34 gives learner-to-separator, not learner-lower-bound-to-separator-lower-bound. The paper's converse-style implication uses additional assumptions, including NP-completeness and a reduction to approximate MCSP; they are not established for this project. Nor does a static menu of O(N) ball tests model an adaptive learner. Thus learning supplies a precise language for center selection but no present lower-bound transfer to arbitrary rect-DAGs or the cyclic cover.

C-184 supplies a separate residual-hardness fact: for k low-circuit predicates of total size a, the sum of minimum extension sizes over their cells is at least CC(z)-a-O(k*2^k). The hard cell still depends jointly on (w,z), and C-183 already shows the mixed-fiber selector can be nonrectangular. Any extension-complexity charge must survive cross-pairs and pass the C-80/C-160 calibrations before it can lower-bound S_rect or rho_prom.
## 115. C-189 - Column-certificate shattering leaves the shared-search question open

For a high table z in Z, define its coordinate certificate against the low class by
\[
h_Y(z)=\min\{|Q|:Q\subseteq[N],\ \forall w\in Y\ \exists i\in Q\text{ with }w_i\ne z_i\}.
\]
This is a set of coordinates, chosen with knowledge of z, on which no low row agrees with z throughout. It is a necessary local object for a Bob-side filter followed by a mismatch search, but not a protocol by itself.

There is an elementary uniform lower bound. Fix any set A subset [N] of size k. Every bit pattern on A is realized by a circuit of size O(kn): use one n-literal minterm for each address assigned 1 and OR those minterms. Hence, for k <= c*s1/n with a sufficiently small basis-dependent constant c > 0, Y shatters A. If Q has at most k coordinates, extend it to such an A and choose the low circuit whose pattern on A equals z|A. It agrees with z on all of Q, so Q is not a certificate. Therefore
\[
h_Y(z)\ge \lfloor c s_1/n\rfloor+1=\Omega(s_1/n)=\Omega(N^\beta/n^2)
\]
for every z in Z. The trivial upper bound is h_Y(z) <= N, since z is not in Y.

The simple counting upper-bound attempt is inconclusive. Point-patching gives a mismatch set of size at least Delta=Theta(s2/n) for every pair (w,z). For a fixed z, a uniformly random m-coordinate set misses one fixed w with probability at most exp(-m*Delta/N). Union-bounding over M1=|Y|<=2^{O(s1 log(n+s1))}=2^{O(N^beta)} rows requires m=O((N/Delta) log M1)=O(Nn) at OPS parameters. Capping at N recovers only the trivial certificate Q=[N]. Thus the circuit-count and distance bounds alone do not show that max_z h_Y(z)=o(N).

A nearby VC-dimension result initially suggests a stronger bound but has the wrong quantifier for h_Y. Pinon, Jungers, and Delvenne, Proposition 46, prove a large VC dimension for a description-bounded circuit class by shattering a particular embedded subcube of addresses (https://arxiv.org/abs/2103.12686). VC dimension gives existence of one large shattered set. A certificate Q(z), however, may use any coordinates; to rule out every certificate of size k requires shattering every k-set, or a different argument. The uniform point-minterm construction supplies only k=Theta(s1/n). So this apparent Omega(N^beta) strengthening is rejected.

This is the opposite quantifier order from C-168. A fixed set selected from the low row must hit every high column and needs N-log2|SIZE(s2)|=N-o(N) positions; a set selected from the high column must hit every low row and the shattering argument only forces Omega(s1/n) positions. The asymmetry leaves room for column filtering to be much cheaper locally.

**Attempt to turn it into a shared-DAG construction or lower bound.** If Bob could select a short certificate Q(z), every promised pair would have a mismatch in Q(z). But the set depends on Bob's input, and the protocol must still expose a mismatch while preserving rectangle-valid states. Scanning coordinates in Q(z) while continuing only when the two parties' bits agree creates a union of diagonal rectangles, not one rectangle; retaining the earlier coordinates in the output support avoids that immediate defect but gives no bounded-size routing argument. The lower bound h_Y(z)=Omega(s1/n) is sublinear and counts coordinates, not shared states. No lower bound on S_rect or rho_prom, no compact router, and no P-vs-NP consequence follows. If h* = max_{z in Z} h_Y(z) were at most k, there would be a deterministic protocol-tree upper bound O(k log N) bits: Bob sends the sorted list Q(z), Alice sends w restricted to Q(z), and Bob outputs any disagreement. This gives at most 2^{O(k log N)} tree nodes. It is not a rect-DAG bound: merging the continuation states after equal answers unions diagonal rectangles. This narrows O-140 to the cost of addressing and searching a Bob-selected certificate under cross-history product hulls.






## 116. C-190 - A common short certificate covers almost half of all high columns

Let M1=|Y| and M2=|SIZE(s2)|. Set k=ceil(log2 M1)+1 and fix any coordinate set Q subset [N] of size k. The trace set T_Q={w|Q:w in Y} has at most M1 patterns. Therefore at least 2^k-M1 >= 2^{k-1} patterns sigma on Q lie outside T_Q. Every table z with z|Q=sigma differs from every low row on at least one coordinate of Q, so h_Y(z)<=k.

Each such pattern has 2^{N-k} completions. At most M2 of those completions can have circuit size at most s2, so
\[
|\{z\in Z:h_Y(z)\le k\}|
\ \ge\ (2^k-M_1)(2^{N-k}-M_2).
\]
At OPS parameters, log M1=O(s1 log(n+s1))=O(N^beta), k=O(N^beta)=o(N), and log M2=O(s2 log(n+s2))=O(N^beta n)=o(N). Hence M2/2^{N-k}=o(1), and the right side is at least (1/2-o(1))*2^N. Thus one fixed Q of O(N^beta) coordinates certifies a mismatch for every low/high pair in a subset containing at least half of the high columns.

This is a genuine column-side structural decomposition, but not a small DAG. On the covered branch, a solver must still find an actual differing coordinate in Q for each pair. On that restricted subrelation, Alice can send w|Q and Bob can return a mismatch index, using k+O(log N) communication bits; the induced protocol tree has at most 2^{O(k)}=2^{O(N^beta)} nodes, already superpolynomial in N. The other branch consists of columns whose Q-pattern lies in T_Q; it can contain up to M1 distinct row-pattern contexts. Explicitly naming those patterns costs up to M1=2^{O(N^beta)} contexts, while merging them requires product-hull-safe suffixes. No lower bound or near-linear router follows. The next test is whether the trace-matched residual can be recursively compressed without enumerating its row patterns, with the C-80/C-160 calibrations retained.


## 117. C-191 - The trace-matched residual has many signature contexts, but this does not lower-bound Mis

Use C-190's fixed set Q and put T_Q={w|Q:w in Y}, r_Q=|T_Q|. Define the exact Q-equality pair set
\[
E_Q=\{(w,z)\in Y\times Z:w|Q=z|Q\}.
\]
Every signature sigma in T_Q has a high completion: its Q-cylinder has 2^{N-k}>M2 tables for sufficiently large OPS n, and at most M2 tables are non-high. Thus E_Q contains at least one diagonal signature pair for every sigma.

A product rectangle A x B contained entirely in E_Q can use only one Q-signature. Indeed, if A contained rows w,w' with distinct Q-traces, no z could agree on Q with both; and the same argument applies to B. Conversely, for each sigma, Y_sigma x Z_sigma is a rectangle contained in E_Q, where Y_sigma={w in Y:w|Q=sigma} and Z_sigma={z in Z:z|Q=sigma}. Hence the minimum number of product rectangles wholly contained in E_Q that cover E_Q is exactly r_Q.

This number is superpolynomial in N. Let t=floor(c*s1/n), with c small enough that every t-point indicator is in Y. For every S subset Q with |S|<=t, the point-indicator delta_S has Q-trace 1_S. Therefore
\[
r_Q\ge\sum_{j=0}^{t}\binom{k}{j}\ge\binom{k}{t}.
\]
Also M1=|Y|>=binom(N,t), so k=ceil(log2 M1)+1>=t log2(N/t)=Omega(tn). Thus k/t=Omega(n), and
\[
\log_2 r_Q\ge t\log_2(k/t)=\Omega(t\log n)
=\Omega(N^\beta\log n/n^2).
\]
Since n=log2 N and beta>0 is fixed, this implies r_Q=N^{omega(1)}.

**Scope and failed transfer.** This proves a non-shareability lemma only for rectangles required to lie inside the Q-equality relation. It rules out a recursive architecture that first certifies equality on Q, discards those coordinates, and sends every matched pair into a tail-only suffix whose product rectangles must remain Q-equal: such a system needs at least r_Q residual contexts. It does not lower-bound an arbitrary C-75 mismatch DAG. A general suffix may also output a mismatch in Q on cross-signature pairs, so its rectangles need not lie in E_Q; moreover, on the restricted promise E_Q, a single ambient rectangle can intersect many diagonal signature blocks. The first broken implication is therefore “many Q-equality contexts imply many states in the unrestricted multi-output mismatch DAG.” Output multiplicity and cross-signature routing remain uncharged. Continue O-141 on whether a standard rect-DAG can exploit those Q-output exits without reintroducing the lost signature contexts; retain the C-80/C-160 counterchecks and the N^(3+3epsilon)/log N transfer threshold.

## 118. C-192 - Dual-rail KW identifies the exact mismatch model; equality states explain C-191

This is a model identification and a sharper description of the open transfer, not a new lower bound.

For a table u in {0,1}^N, define its dual-rail encoding rho(u) in {0,1}^{2N} by
\[
\rho(u)_{i,b}=1 \quad\Longleftrightarrow\quad u_i=b,
\qquad i\in[N],\ b\in\{0,1\}.
\]
Reverse the parties in C-75: Alice receives z in Z and Bob receives w in Y. The monotone Karchmer-Wigderson output condition is a coordinate (i,b) with rho(z)_{i,b}=0 and rho(w)_{i,b}=1. This is equivalent, bit for bit, to z_i=1-b and w_i=b, exactly the signed mismatch output of C-75. Since w and z are distinct, such an output always exists.

The encoded promise is a valid partial monotone function. No low encoding is coordinatewise below a high encoding: if w_i differs from z_i, then at rail (i,w_i) we have rho(w)=1 and rho(z)=0. Hence the labels
\[
f(\rho(w))=1\quad(w\in Y),\qquad f(\rho(z))=0\quad(z\in Z)
\]
are monotonicity-consistent. For example, they extend to the monotone function
\[
f_\uparrow(x)=1\quad\Longleftrightarrow\quad
\exists w\in Y:\rho(w)\le x.
\]
Thus C-75 is exactly the monotone KW search relation of this partial function, after swapping the parties and naming each rail as an output coordinate. This is an isomorphism of promise inputs and outputs, so it preserves protocol-tree and rect-DAG sizes exactly.

The usual circuit correspondences do not improve the quantitative transfer. A Boolean separator h on tables yields a monotone dual-rail separator with constant-factor overhead by the standard two-rail simulation of NOT gates; restricting a monotone separator to valid rails yields an ordinary separator with constant-factor overhead. The rect-DAG/circuit characterization therefore remains the same C-89 separator measure. A q-pair fusion cover still gives the recorded O(q^3/log q) standard rect-DAG compiler, and an L-vertex rect-DAG still gives rho_prom=O(L). To infer rho_prom>N^(1+epsilon) through this compiler still requires a rect-DAG lower bound above N^(3+3epsilon)/log N.

There is a useful connection to equality-feasible protocols. C-190's matching set
\[
E_Q=\{(w,z):w|_Q=z|_Q\}
\]
is represented by one equality-feasible state: set q(w) to the binary code of w|_Q and r(z) to the same code of z|_Q, and declare the state feasible iff q(w)=r(z). By C-191, any product rectangle wholly inside E_Q fixes one signature, and exactly r_Q rectangles are needed to cover E_Q. Since r_Q=N^(omega(1)), representing this particular equality state using only rectangles contained in E_Q has superpolynomial cost.

This pins down what C-191 does and does not show. Equality-feasible states can store a matching trace as one semantic state, while the standard rect-DAG stores only products. But no arbitrary C-75 rect-DAG is forced to create a state contained in E_Q: it can route cross-signature pairs to Q-output leaves, and those leaves may share safely whenever their row and column projections have the same output bit orientation. The proposed charge from trace contexts to states therefore still breaks at O-141.

The adjacent protocol literature uses a separate hierarchy. In Folwarczny's definition, an inequality-feasible state is q(x)<r(y), a triangle-shaped set, and an equality-feasible state is q(x)=r(y), which can be a union of many diagonal rectangles. Every rectangle A x B is a special case of either model: for inequality, take q=1 on A and 2 off A, and r=2 on B and 1 off B; for equality, take q=0 on A and 1 off A, and r=0 on B and 2 off B. Thus any degree-two rect-DAG is also a degree-two protocol in each stronger feasibility model, with the same state count. If a rect-DAG leaf is only a subrectangle of its output cylinder, broaden it to the full output cylinder; every newly feasible terminal pair still has the same valid output. A lower bound for either stronger protocol complexity on this partial function would imply the corresponding rect-DAG lower bound.

Inequality protocols are characterized by monotone real circuits, and published exponential lower bounds apply to particular functions. They do not transfer to this Gap-MCSP partial function without a reduction or a new lower-bound argument. The 2022 comparison paper also emphasizes that strong lower bounds for equality protocols are open in its proof-complexity applications. This literature therefore supplies a candidate stronger target, not a result for the project.

**Short-description stress test.** The canonical upward-closed separator has the monotone DNF
\[
f_\uparrow(x)=\bigvee_{w\in Y}\ \bigwedge_{i=1}^{N}x_{i,w_i}.
\]
It has O(N|Y|) gates before any factoring. Circuit descriptions reduce the number of listed rows only to |Y|=2^(O(N^beta)); the universal circuit computes a term for a supplied description, but the outer existential OR over all descriptions remains. Factoring this projection to near-linear size is exactly the unresolved universal sparse-envelope problem. A short description for each w alone does not factor the existential OR.

**Historical next target, superseded by C-194.** At C-192 the proposed next experiment was to study degree-two inequality/equality protocols. C-194 constructs the universal 4N-1-state inequality protocol and closes that branch. The surviving target is product-rectangle state reuse in O-141; do not count C-191's r_Q as a global DAG lower bound without charging off-diagonal Q-output exits. No superlinear rect-DAG bound or P-vs-NP result follows from C-192 through C-194.

Primary references: [Sokolov, Dag-like Communication and Its Applications](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download); [Garg, Goos, Kamath, and Sokolov, Monotone Circuit Lower Bounds from Resolution](https://toc.ilab.sztaki.hu/articles/v016a013/v016a013.pdf); [Folwarczny, On Protocols for Monotone Feasible Interpolation](https://arxiv.org/abs/2201.05662); [Cavalar and Oliveira, Boolean Circuit Complexity and Two-Dimensional Cover Problems](https://arxiv.org/abs/2503.14117).
## 119. C-193 - Equality-feasible mismatch search has a linear protocol, so that lower-bound route is closed

C-192 suggested testing lower bounds in stronger equality-feasible protocols. That model is too strong for this purpose: the entire signed-mismatch relation on any two disjoint table classes has an explicit degree-two equality protocol with at most 4N+1 states.

Use the exact dual-rail mKW orientation from C-192. The first party holds x=rho(z) for z in Z (a 0-input); the second holds y=rho(w) for w in Y (a 1-input). Read a_i(x)=x_(i,1) and b_i(y)=y_(i,1); on valid rails these are z_i and w_i. For i=0,...,N define an equality-feasible state E_i by
\[
E_i(x,y) \quad\Longleftrightarrow\quad a_{[i]}(x)=b_{[i]}(y).
\]
It is one equality state: q_i(x)=code(a_[i](x)) and r_i(y)=code(b_[i](y)). For i=1,...,N define D_i by
\[
D_i(x,y) \quad\Longleftrightarrow\quad
 a_{[i-1]}(x)=b_{[i-1]}(y)\ \text{and}\ a_i(x)\ne b_i(y).
\]
It too is one equality state: q'_i(x)=2 code(a_[i-1](x))+a_i(x) and r'_i(y)=2 code(b_[i-1](y))+(1-b_i(y)). Equality forces equal prefixes and opposite current bits.

The graph has root E_0. For each i, add edges E_(i-1)->E_i and E_(i-1)->D_i. From D_i add edges to the two output leaves for the monotone mismatch coordinates (i,0) and (i,1). The sink for (i,b) has feasible set exactly x_(i,b)=0 and y_(i,b)=1; it is itself equality-feasible, using a row map equal to 0 when x_(i,b)=0 and 1 otherwise, and a column map equal to 0 when y_(i,b)=1 and 2 otherwise. For a valid dual-rail pair at D_i, either z_i=0,w_i=1, making leaf (i,1) feasible, or z_i=1,w_i=0, making leaf (i,0) feasible. A valid pair follows the E-chain through its common prefix, then enters D_i at its first differing coordinate. Since Y and Z are disjoint, no valid pair reaches E_N; attach E_N to any output leaf so every graph sink has an output label. The graph is acyclic, has out-degree at most two, and has (N+1)+N+2N=4N+1 vertices.

This is a linear-size universal protocol in the equality-feasible model; it works for every disjoint pair of table classes and ignores circuit descriptions. It decisively rules out an equality-protocol lower bound as a route to the project target, which needs more than N^(3+3epsilon)/log N rect-DAG states after the current compiler. It does not yield a standard rect-DAG: E_i is a union of prefix-diagonal product blocks, and E_k for C-190's Q contains r_Q=N^(omega(1)) signature blocks. C-191's rectangle-cover count explains the state expansion for this particular protocol, but an arbitrary rect-DAG may use different states and Q-output exits.

**O-142 update.** Retire the equality-protocol lower-bound arm. Keep only degree-two inequality protocols / monotone real circuits as a possible stronger-model target, and try to kill that too by a compact construction or an explicit reduction test. Existing results do not make inequality and equality models interchangeable at small size: the 2022 paper proves inequality-to-equality simulation with polynomial overhead, not the reverse needed here. No lower bound or construction for standard C-75 rect-DAGs changes.

## 120. C-194 - A universal linear inequality protocol also kills O-142

This is an explicit protocol in the degree-two inequality model, not a standard rect-DAG. It works for every pair of disjoint families of N-bit strings, so it applies to the C-75 promise without using circuit descriptions.

Use the exact dual-rail orientation from C-192: the first input is x=rho(z) for z in Z, the second is y=rho(w) for w in Y. A valid sink labeled (i,b) must be feasible only when x_(i,b)=0 and y_(i,b)=1. The promise Y intersect Z is empty.

For an interval I of table coordinates, let val_I(u) be the binary integer represented by u restricted to I, with the left half as the more significant bits. Build a balanced interval tree. It has 2N-1 intervals. For every interval I create comparison states L_I and G_I. At a nonsingleton interval split I into its higher-order half J and lower-order half K, and give each state two children of the same sign, one for J and one for K. Add a root state with constant local values 0<1 and children L_[N], G_[N].

For nonsingleton I, define the two local functions at L_I by

    q_LI(x)=2^|I| - val_I((x_(j,1))_(j in I)),
    r_LI(y)=2^|I| - val_I((y_(j,1))_(j in I)).

Since x_(j,1)=z_j and y_(j,1)=w_j on valid dual-rail inputs, L_I is feasible exactly when val_I(z)>val_I(w). At G_I use q_GI(x)=val_I((x_(j,1))_(j in I)) and r_GI(y)=val_I((y_(j,1))_(j in I)); it is feasible exactly when val_I(z)<val_I(w).

At singleton L_i use q=x_(i,0), r=y_(i,0); at singleton G_i use q=x_(i,1), r=y_(i,1). These are valid inequality-protocol sinks because each side's function is the same named input coordinate, and their feasible conditions are respectively z_i=1,w_i=0 and z_i=0,w_i=1. These agree with the internal comparison predicates on the promised dual-rail inputs.

Correctness is by ordinary binary comparison. If z_I>w_I, then either z_J>w_J or z_J=w_J and z_K>w_K, so at least one L-child is feasible. Every feasible L-child contains a signed mismatch of orientation z_i=1,w_i=0. The symmetric statement holds for G and orientation z_i=0,w_i=1. Since z and w are distinct, exactly one of the root's two orientation states is feasible. Following feasible children reaches a correctly labeled singleton.

The graph has 2(2N-1)+1=4N-1 vertices and outdegree at most two. Thus the minimum degree-two inequality-protocol size for C-75 is at most 4N-1, for every choice of disjoint Y,Z. Under the Hrubes-Pudlak definition, the local maps are unrestricted real-valued functions and protocol size counts vertices; the comparison maps above are legal. Their Theorem 5 identifies this model with monotone real circuits, not ordinary Boolean separators. Folwarczny's later comparison of inequality and equality protocols likewise treats these larger feasible-set geometries.

**Why this does not give a small C-75 rect-DAG.** An L_I state is a greater-than triangle, not a product rectangle. Its direct expansion into product rectangles can be exponential. For k-bit values, restrict the greater-than relation z>w to the promise Z={2j+1}, W={2j:0<=j<2^(k-1)}. The 2^(k-1) pairs (z,w)=(2j+1,2j) form a fooling family: one rectangle contained in z>w cannot contain pairs for two indices j<l, since its cross-pair (2j+1,2l) violates z>w. Therefore covering this single triangle state by rectangles can require 2^(k-1) rectangles. This is a state-expansion lower bound for the generic comparison predicate, not a lower bound on an alternative rect-DAG for C-75.

There is also a large generic model separation. For a Boolean function f on N bits, let Y=f^-1(1), Z=f^-1(0). Its signed-mismatch relation always has the 4N-1 inequality protocol above. By Sokolov's DAG-like KW/circuit correspondence, some such relations require standard rect-DAG size at least 2^N/poly(N), by counting Boolean circuits. Hence no generic polynomial-overhead conversion from inequality protocols to standard rect-DAGs is possible. This example is a model-separation witness only; it is not the actual SIZE(s1)/high promise.

**Disposition.** Close O-142 completely. Any lower bound in the inequality/monotone-real model is capped by 4N on this signed-mismatch relation, below the N^(3+3epsilon)/log N rect-DAG threshold needed by the current q-to-DAG compiler. The reverse conversion is not available: the model admits triangles that need exponentially many rectangles, and generic polynomial simulation is ruled out by the circuit-counting separation above. This changes neither S_rect nor rho_prom for actual Gap-MCSP. Keep O-141 active: the live object is still an acyclic product-rectangle DAG, and the unresolved issue remains whether cross-signature outputs can compress the matched-trace residual.

**Primary sources.** Hrubeš and Pudlák, [A note on monotone real circuits](https://users.math.cas.cz/~hrubes/PDFs/MReal.pdf), Definition and Theorem 5; Folwarczny, [On Protocols for Monotone Feasible Interpolation](https://arxiv.org/abs/2201.05662), protocol-model comparisons; Sokolov, [Dag-like Communication and Its Applications](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download), Boolean games and circuits.

## 121. C-195 - The universal comparison state has superpolynomial rectangle-cover cost on the actual OPS promise

C-194's O(N)-state inequality protocol cannot be expanded state-by-state into a small rect-DAG, even after restricting its first comparison state to the actual SIZE(s1)/high promise. This strengthens the generic triangle-versus-rectangle caveat, but it still does not lower-bound an alternative rect-DAG for the full relation.

Use the project parameters `N=2^n`, `s1=N^beta/(c n)`, and `s2=N^beta`, with fixed `0<beta<1` and constant `c>0`. Order the N table coordinates once and read every table as an integer in `[0,2^N-1]`, with the first table bit most significant. Choose

    t = floor(s1/(C n)) = Theta(N^beta/n^2)

for a sufficiently large basis constant C. For every t-bit prefix p, let

    w_p = p || 0^(N-t).

The table `w_p` is low: it is the OR of at most t point indicators, each of size O(n), so its circuit size is at most `O(tn) <= s1`. Its integer value is `p*2^(N-t)`. For each consecutive prefix p,p+1, the open integer interval between `w_p` and `w_(p+1)` contains `2^(N-t)-1` tables.

The number `M2=|SIZE(s2)|` of non-high tables satisfies `log2(M2)=O(s2 log(s2+n))=O(N^beta n)=o(N)`. Also `t=o(N)`. Therefore, for all sufficiently large n, every one of these gaps has more than M2 tables and contains at least one high table `z_p in Z`. Choose one such `z_p` in each gap. Then

    w_p < z_p < w_(p+1).

Now consider the feasible set of C-194's top L-state, on the promise, namely

    T_L = {(z,w) in Z x Y : val(z)>val(w)}.

Each pair `(z_p,w_p)` belongs to `T_L`. If a product rectangle `A x B` contained two selected pairs with p<q, its cross-pair `(z_p,w_q)` would also belong to `A x B`. But `z_p<w_(p+1)<=w_q`, so `(z_p,w_q)` is not in `T_L`, a contradiction. Thus the `2^t-1` selected pairs form a rectangle fooling family, and every rectangle cover of `T_L` has size at least

    2^t-1 = 2^(Theta(N^beta/n^2)).

This is superpolynomial in N for every fixed beta>0. It shows that a direct rectangle expansion of the comparison state in C-194 is prohibitively large on the actual promise, not just on an artificial promise. The first comparison state is semantically compact only because an inequality protocol is allowed arbitrary local maps and does not charge their description length.

**Scope and direct countercheck.** The lower bound applies to rectangles required to cover the feasible set of that specific L-state. An arbitrary rect-DAG for Mis need not contain or simulate that comparison state; it can use a different organization of output rectangles. In fact, the selected prefix-row/gap-column subpromise itself has an O(N)-vertex rect-DAG: every low row `w_p` is zero on the N-t suffix, while every chosen high gap table `z_p` has a nonzero suffix. Bob scans the suffix and outputs the first coordinate with `z_i=1`; the states `Y' x {z in Z': z_(t+1)=...=z_j=0}` are rectangles, each branching to the valid output at the next suffix coordinate or to the next scan state. Thus C-195 is a real-promise state-expansion obstruction and a concrete warning that one triangle's rectangle-cover number does not lower-bound the search relation. It gives no lower bound on `S_rect`, rho, or P versus NP. It strengthens the reason O-142 cannot be converted back generically and leaves O-141 unchanged.

**Proof check.** The only promise-specific inputs are the point-indicator construction for all `2^t` low prefixes and the global bound `M2<2^(N-t)-1`. The cross-pair contradiction uses product structure alone. C-78/C-133 previously established a related exponential cost for a fixed-order equality scanner; C-195 concerns the different ordered-comparison triangle used by C-194.

Reference for the model distinction and definitions: [Folwarczny, On Protocols for Monotone Feasible Interpolation](https://arxiv.org/abs/2201.05662). Its degree-two protocol states may have equality or strict-inequality feasibility; the equality prefix states above are not product rectangles.

## 122. C-196 - A local exit-versus-tail constraint for shared rectangles

This refines the product-hull condition for O-141. It quantifies which cross-signature pairs a state can safely pass to Q-coordinate outputs, and what its tail outputs must separate. It is a local theorem only; it does not yet charge states globally.

Fix the C-190 coordinate set (Q\subseteq[N]), with (k=|Q|), and write
\[
Y_\sigma=\{w\in Y:w|_Q=\sigma\},\qquad Z_\tau=\{z\in Z:z|_Q=\tau\}.
\]
Let (v) be any node of a standard rect-DAG for \(\mathrm{Mis}_{Y,Z}\), with feasible rectangle (A_v\times B_v). Let (K_v\subseteq[N]) be the coordinates appearing at descendant output leaves, (P_v=K_v\cap Q), and (T_v=K_v\setminus Q). For signatures \(\sigma,\tau\), put (A_{v,\sigma}=A_v\cap Y_\sigma) and (B_{v,\tau}=B_v\cap Z_\tau). Call \((\sigma,\tau)\) a tail-overlap edge at (v) if both sets are nonempty and
\[
\pi_{T_v}(A_{v,\sigma})\cap\pi_{T_v}(B_{v,\tau})\ne\varnothing.
\]

**Lemma.** For every tail-overlap edge, \(\sigma|_{P_v}\ne\tau|_{P_v}\). Equivalently, the Q-output support (P_v) must hit the coordinate-difference set \(\{i\in Q:\sigma_i\ne\tau_i\}\) for every signature pair whose tail projections overlap. In particular, there can be no tail-overlap edge on the diagonal \(\sigma=\tau\).

**Proof.** If the signatures agree on (P_v), tail overlap supplies (w\in A_{v,\sigma}) and (z\in B_{v,\tau}) that agree on every coordinate in (T_v). They also agree on every coordinate in (P_v), so they agree on all of (K_v=P_v\cup T_v). No descendant leaf can then output a valid mismatch for ((w,z)), contradicting correctness of state (v).

There is a quantitative consequence for diagonal contexts. Let
\[
r_v=|\{\sigma:A_{v,\sigma}\ne\varnothing\text{ and }B_{v,\sigma}\ne\varnothing\}|,
\qquad t_v=|T_v|,
\qquad M_2=|\mathrm{SIZE}(s_2)|.
\]
For each of these (r_v) signatures choose one (w_\sigma\in A_{v,\sigma}). Every high table (z) satisfying (z|_Q=\sigma) and (z|_{T_v}=w_\sigma|_{T_v}) agrees with (w_\sigma) on all descendant output coordinates, so it cannot lie in (B_v). The corresponding cylinders are disjoint across \(\sigma\), and their union has (r_v2^{N-k-t_v}) tables. At most (M_2) tables in the entire universe are non-high. Hence
\[
|Z\setminus B_v|\ \ge\ \max\!\left\{0,\,r_v2^{N-k-t_v}-M_2\right\}.
\]

This makes the local tradeoff explicit: a state that carries many Q-matched residual signatures either gives its tail support enough coordinates to distinguish those fibers, or excludes a large set of high columns; tail overlap between different signatures can be merged only when the Q-output support separates those signatures. The statement is necessary, not sufficient: it does not describe how the DAG routes the pairs to the claimed leaves.

**Why this does not close O-141.** The excluded high-column sets can overlap across states; C-130 gives a reachable-state counterexample to summing such volumes. A state may also take (P_v=Q), allowing all cross-signature pairs to use Q outputs while leaving the diagonal fibers to a shared tail subgraph. C-80 and C-160 show why generic local richness/cylinder conditions do not imply a large DAG: both have small rect-DAGs on their structured promises. A global charge must bound the reuse of those Q-output exits and tail subgraphs together, and must exceed (N^{3+3\epsilon}/\log N) standard states under the current cover compiler (or improve that compiler). No new lower bound on (S_{\rm rect}), \(\rho_{\rm prom}\), or P versus NP follows.

**Description-space falsification check.** Let (D_{s_1}) be all circuit descriptions of size at most (s_1), and let (G(d)=\mathrm{TT}(C_d)\). Since (G:D_{s_1}\twoheadrightarrow Y), lifting every row predicate through (G) gives
\[
\mathrm{rectdag}(D_{s_1}\times Z)=\mathrm{rectdag}(Y\times Z):
\]
the reverse inequality follows by restricting a description-space DAG to one chosen description of each (w\in Y\). Thus giving Alice (d) does not reduce shared-DAG size. A universal circuit verifies a fixed description, but the separator still has to compute the existential projection \(\exists d\in D_{s_1}:G(d)=w\); direct enumeration costs (O(N|D_{s_1}|)=N\,2^{O(s_1\log(n+s_1))}\), not (N^{1+o(1)}\). No small universal DAG is constructed, and no lower bound against one is proved. This is the exact unresolved sparse-envelope circuit problem, rather than an extra benefit furnished by short descriptions.

**Tree/communication versus shared-DAG calibration.** For any Boolean function (f:\{0,1\}^m\to\{0,1\}), its KW Bit relation has deterministic communication at most (m+O(\log m)): Alice sends (x\in f^{-1}(1)), then Bob finds a differing coordinate with (y\in f^{-1}(0)). Sokolov's DAG-like KW theorem identifies its rect-DAG size, up to basis constants, with Boolean circuit size (C(f)); counting gives functions with (C(f)=2^{\Omega(m)}). So low communication-bit cost can coexist with exponentially many shared-DAG states. This is not a counterexample with a small protocol-tree *node count*: any tree is itself a DAG, and the send-(x) tree may have (2^{\Theta(m)}) leaves. In the other direction, parity has an (O(m))-node KW DAG but an \(\Omega(m^2)\)-node tree by the formula lower bound. These artificial examples calibrate the measures but do not transfer to the SIZE(s1)/high promise.

The primary-model audit was checked against [Sokolov's ECCC paper](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download), [Garg–Göös–Kamath–Sokolov](https://theoryofcomputing.org/articles/v016a013/), and [Cavalar–Oliveira](https://arxiv.org/abs/2503.14117). The existing comparison in §2 is unchanged: Sokolov/GGKS require acyclic product-rectangle states; Sokolov's communication PLS graph is also acyclic and pays a (2^{3t}) state-simulation loss; the fusion closure is exactly the cyclic least-fixed-point intersection measure on the chosen promise ground set; Nakayama–Maruoka's generalized approximation functionals do not give the same cover identity; and Amano–Maruoka's AND-count results concern acyclic monotone circuits for quadratic functions. None supplies a lower-bound transfer for this partial Gap-MCSP relation.


## 123. C-198 - Partial-monotone KW exposes a lifting interface, but the high-side reduction is missing

Let e(x) in {0,1}^{2N} be the one-hot dual-rail encoding e(x)_(i,b)=1 iff x_i=b. Every encoded table has weight N; distinct encodings are incomparable. Define the partial monotone function f on domain e(Z) union e(Y) by f(e(z))=0 for z in Z, and f(e(w))=1 for w in Y. This is monotone-consistent. Its monotone Karchmer-Wigderson relation, with Alice holding e(z) and Bob holding e(w), outputs a coordinate (i,b) with e(z)_(i,b)=0<e(w)_(i,b)=1. Such an output is exactly a signed mismatch w_i=b != z_i, and every valid signed mismatch gives such a coordinate. Thus C-75 is exactly the restriction of this partial monotone KW relation to the encoded promise inputs (up to swapping party names).

The 2025 paper *Lifting with Colourful Sunflowers* states that monotone circuit size for a partial monotone function is equivalent to rectangle-DAG size of its monotone KW relation; its Theorem 11 lower-bounds triangle-DAG protocols for an Index-composed search relation by
\[
\left(\frac{m}{A|\Sigma|\,w(S)\log(mn)}\right)^{w(S)}.
\]
This is a model-compatible candidate technique, not yet a C-75 lower bound. A precise transfer condition is available: if maps from Alice/Bob inputs of such a lifted relation into Y,Z, plus an output decoder, preserve valid answers as signed mismatches, then pulling back every row/column side of a C-75 rectangle gives a same-size rect-DAG for the lifted relation. The theorem would then transfer with no DAG-size loss.

The missing construction is substantial. Every Bob image must lie outside SIZE(s2), and every mismatch coordinate of the two image tables must decode to a valid lifted-search witness. A Bob map computed by a circuit of size at most s2 (including its hardwired input description) cannot have high-table images. The standard explicit CSP/graph reductions in the colourful-sunflower paper do not provide such high-complexity truth tables. No reduction, parameter setting reaching N^(3+3epsilon)/log N, or contradiction with C-80/C-160 has been obtained.

**Affine-coset falsification.** A natural attempt to make high tables by translating a structured low code does not yield a hard subpromise. If C is a linear subspace of F_2^N, a is not in C, Y' is a subset of C, and Z' is a subset of a+C, choose a linear functional ell with ell(C)=0 and ell(a)=1. Then h(x)=1-ell(x) separates Y' from Z', with an O(N)-gate parity circuit, so S_rect(Y',Z')=O(N). Thus affine-coset embeddings cannot reach the current superlinear DAG target even when the coset contains only high tables.

**Disposition.** The lifting literature offers an exact interface for shared-DAG lower bounds, while short-description invariance and the affine-coset test identify two shortcuts that do not help. The live missing lemma is a reduction whose low images have size-s1 circuits, whose high images are provably outside size s2, and whose all mismatch outputs preserve a hard search relation. This is a candidate direction, not a proved non-shareability theorem; O-141 remains open and no new S_rect, rho_prom, or P-vs-NP lower bound follows.

Primary source: de Rezende and Vinyals, [*Lifting with Colourful Sunflowers* (CCC 2025), especially Theorem 11 and the partial monotone KW definition](https://drops.dagstuhl.de/storage/00lipics/lipics-vol339/ccc2025/html/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.html).



## 124. C-199 - Dense-column restriction preserves the triangle-DAG lifting lower bound

A useful high-side refinement follows from the error-removal proof of the triangle-DAG lifting theorem in the 2024 ECCC report. It removes the need for a reduction to map *every* lifted Bob input to a high-complexity table.

Let F be an unsatisfiable CNF on r variables, and consider Search(F) composed with IND_m^r, whose Bob universe is U={0,1}^{mr}. Let B be any Bob-column subset with omitted density eta=|U\B|/2^(mr). Use the same parameters as Theorem 2.11 of the source: width parameter w<=r, 0<delta<1-1/log m, and m >= (50r/delta)^(2/delta). If a triangle-DAG of size at most (1/4)m^((1-delta)w) solves the relation on [m]^r x B, the published proof adapts to produce a width-w resolution refutation of F, provided eta<1/4. Consequently, if F has no width-w resolution refutation, the restricted-domain triangle-DAG size is Omega(m^((1-delta)w)).

**Proof adaptation.** In the source proof's bottom-up error-removal process, initialize the accumulated bad-column set as Y_err^0=U\B instead of empty. At each state, remove these whole columns, plus the error rows/columns produced by earlier states, before applying the Triangle Lemma. Restricting a triangle to a set of columns, or deleting whole rows/columns, leaves a triangle. Every remaining pair lies in B, so the protocol's child-cover and leaf-correctness conditions hold on the retained state. The Triangle Lemma's per-state error bounds are unchanged. Taking the DAG-size constant 1/4 instead of 1/2 halves the source proof's accumulated protocol-error density below 1/4; together with eta<1/4, at least half the root columns remain. Their min-entropy is at least mr-1, which satisfies the same Full Image Lemma requirement for the stated large-m parameters. The rest of the resolution extraction is unchanged. This is a proof-level corollary of the published argument, not a theorem stated verbatim in that paper.

For the project promise, |SIZE(s2)|=2^(O(s2 log(n+s2)))=2^o(N) when s2=N^beta and beta<1. Thus if mr=N, the high-table columns B={0,1}^N\\SIZE(s2) have omitted density eta=2^(-N+o(N)), far below 1/4. A lifting reduction may therefore send its Bob input to the truth-table string itself and then restrict to this dense high-column domain; it need not prove each table high individually.

**What this does not solve.** We still need an answer-preserving map from lifted search inputs into C-75: every low image must have a size-s1 circuit, and each signed mismatch output must decode to a valid source witness. For a table coordinate i, the two oriented mismatch sets have the form
\[
\{x:f_i(x)=0\}\times\{y:g_i(y)=1\},\qquad
\{x:f_i(x)=1\}\times\{y:g_i(y)=0\},
\]
so each output orientation is a rectangle cut by two local predicates. General lifted clause-falsification predicates need not have this form. A test encoding that makes Alice's table a blockwise one-hot pointer code has a simple O(N)-gate range-membership separator; it therefore cannot deliver the required superlinear DAG lower bound even if Bob's retained tables are all high. The first broken implication is output-preserving reduction / hard low-image recognition, not high-column density.

**Quantitative target.** If a lifted relation with mr=N and no width-w resolution refutation is embedded as above, the robust lower bound is Omega(m^((1-delta)w)). It must exceed N^(3+3epsilon)/log N to force rho_prom>N^(1+epsilon) through the current compiler. No such embedding is known, and no C-75, rho, or P-vs-NP lower bound follows yet.

Primary source: [Cavalar, Glinskih, de Rezende, Robere, and Vinyals, *Truly Supercritical Trade-offs for Resolution, Cutting Planes, Monotone Circuits, and Weisfeiler-Leman*, ECCC Report 185 (2024), Theorem 2.11 and proof's error-removal step](https://eccc.weizmann.ac.il/report/2024/185/download).



## 125. C-200 - The standard colourful-sunflower reduction has an easy low-image envelope

The concrete reduction in Lemma 19 of *Lifting with Colourful Sunflowers* maps Alice's input x to the adjacency table of exactly one k-clique on the selected vertices \((x_p,p)\), with every other edge absent. Let V=mk be the graph's vertex count and N=binom(V,2) its adjacency-table length.

There is an O(N log V)-gate Boolean circuit h that accepts exactly these Alice-image graphs and rejects every c-colourable graph when c<k. For each vertex, compute its degree. Accept iff (i) every degree is either 0 or k-1, (ii) exactly one vertex in each of the k parts is active (degree k-1), and (iii) all other vertices have degree 0. With exactly k active vertices and each active degree k-1, the induced graph on them is a k-clique; the part condition gives one selected vertex per part. The Alice images satisfy the test. A c-colourable Bob graph cannot satisfy it because it would contain a k-clique. Degree counters use O(V^2 log V)=O(N log V) gates, and the remaining checks fit within that bound.

Therefore the C-75 mismatch relation restricted to these low/high image families has an O(N log N)-size separator and rect-DAG, even after restricting the Bob images to those truth tables outside SIZE(s2). It cannot furnish the required \(N^{3+3\epsilon}/\log N\) lower bound. There is a second issue: raw adjacency-table mismatches also include Bob-present/Alice-absent edges, whereas Lemma 19 decodes only Alice-present/Bob-absent edges. Thus the standard lifting-to-clique-colouring reduction is not itself an answer-preserving reduction to signed mismatch.

**Learning.** A source relation can have a large triangle-DAG lower bound while the particular low/high image families used by its reduction have a small ordinary separator. For transfer to C-75, the low image must resist a general Boolean range test, not merely support a hard monotone KW relation. Dense-column robustness removes the high-image obstacle but not this low-envelope collapse or the output-orientation mismatch. No C-75 or P-vs-NP lower bound follows.

Primary source for the map \(\mu_A\): de Rezende and Vinyals, [*Lifting with Colourful Sunflowers* (CCC 2025), Lemma 19](https://drops.dagstuhl.de/storage/00lipics/lipics-vol339/ccc2025/html/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.html).

## 126. C-201 - Correct the lifting exponent and sharpen the dense-column corollary

**Correction.** C-199's first draft misread the typeset factor 1/2 as a division of the exponent. Theorem 2.11 in the primary source assumes triangle-DAG size at most (1/2)m^((1-delta)w), not (1/2)m^((1-delta)w/2). The paper confirms this reading immediately afterward: with delta=1/120, the theorem rules out size m^(0.99w), matching its stated nearly tight upper bound m^(1.01w). Its local row-error estimate is m^(-(1-delta)w).

**Restricted Bob-domain corollary.** Let eta=1-|B|/2^(mr)<1/4. Run the source error-removal proof with initial accumulated column-error set U\B and the stricter size cap (1/4)m^((1-delta)w). The accumulated row-error density is at most 1/4; the newly generated column-error density is below 1/4 by scaling the source's linear-in-size bound. Therefore the root retains at least half of the Bob universe and at least 3/4 of the row universe. Both sides satisfy the Full Image Lemma/predensity hypotheses used in the published proof, so the same extraction yields a width-w resolution refutation. Thus, absent such a refutation, the restricted-domain triangle-DAG lower bound is Omega(m^((1-delta)w)), rather than Omega(m^((1-delta)w/2)).

**What improves and what does not.** With mr=N, the lifted lower bound is Omega((N/r)^((1-delta)w)). If r is polylogarithmic in N, fixed-width parameters with (1-delta)w>3+3epsilon would clear the project's current rect-DAG-to-cover threshold. The low-image and answer-preservation problems remain untouched: the CCC clique-colouring image still has the O(N log N) range separator from C-200, and an arbitrary C-75 signed mismatch still need not be a valid lifted-search witness. This is a corrected and stronger conditional interface, not a C-75 lower bound or a P-vs-NP breakthrough.

Primary source: [de Rezende et al., *Truly Supercritical Trade-offs for Resolution, Cutting Planes, Monotone Circuits, and Weisfeiler-Leman*, Theorem 2.11, its proof, and the near-tightness discussion](https://eccc.weizmann.ac.il/report/2024/185/download).

## 127. C-202 - Unique-output Index search cannot be decoded cheaply from mismatch types

This tests whether the corrected C-201 lifting exponent can be paired with a simple total source search problem and a small output decoder. The answer is negative for a natural unique-output source, even before imposing any low-circuit restriction on Alice's image.

Fix v>=2 and let F_v contain, for each a in {0,1}^v, the width-v clause C_a falsified exactly by assignment a. Then F_v is unsatisfiable and Search(F_v) has exactly one valid output on every assignment. In Search(F_v) composed with IND_m^v, the inputs are x in [m]^v and y in {0,1}^{mv}; the induced assignment is z_i=y_(i,x_i), and its unique answer is C_z. Let mu be uniform on this source input product.

**Rectangle-mass lemma.** If a product rectangle A x B is contained in the answer fiber for a fixed a, then
\[
\mu(A\times B)\le (1/(2m))^v.
\]
For each variable i, let S_i={j: x_i=j for some x in A}. Then A is contained in the product of the S_i, so mu_X(A)<=product_i |S_i|/m. Since every pair in A x B must induce assignment a, B must fix y_(i,j)=a_i for every j in S_i; hence mu_Y(B)<=2^(-sum_i |S_i|). Multiplying gives product_i |S_i|/(m 2^|S_i|), at most (1/(2m))^v because s/2^s<=1/2 for every positive integer s.

Now suppose partywise maps encode source pairs as promised low/high N-bit tables, N=mv, and each C-75 signed mismatch type has an output-decoder DAG with at most K output-labelled leaves that solves the entire pullback of that type. This is the relation-preserving, per-type decoder model; a decoder conditioned on a particular C-75 protocol history is outside this lemma, and its extra contexts must be charged separately. Pulling leaves back through the partywise maps preserves product rectangles. Every leaf must lie inside one unique-answer fiber, and the leaves over all 2N mismatch types cover the source domain (or a retained domain of measure 1-eta if Bob strings are restricted to a set omitting eta<1/4). Thus
\[
2N K (1/(2m))^v \ge 1-\eta,
\quad\text{so}\quad
K\ge (1-\eta)(2m)^v/(2N).
\]
For N=mv this is Omega(m^(v-1)). In particular, a fixed output label per mismatch type (K=1) is impossible for large m.

**Comparison with the lifting lower bound.** Take v=16 and w=15. Since every axiom of F_16 has width 16, F_16 has no width-15 resolution refutation. For fixed delta=1/10 and m=N/16 sufficiently large, C-201's robust triangle-DAG lifting theorem gives a source lower bound Omega(m^13.5) on the dense high-column restriction. But any per-type decoder refinement requires K=Omega(m^15) leaves. Therefore this unique-output source cannot yield a useful C-75 lower bound by dividing its lifted DAG lower bound by the decoder-refinement size: the required decoder is already larger than the source lower bound. This is independent of how the low tables are chosen.

**Scope and next filter.** This does not rule out a direct zero-refinement encoding of a source relation with many valid answers per pair, nor a different theorem whose lower bound survives the decoder cost. It closes the full-clause unique-output Search(F) candidate for the current lifting transfer. The next source must combine a large lifted-DAG lower bound with broad answer fibers / a small fractional output cover, while still admitting a low-image map into SIZE(s1) with no easy envelope. C-164's cPHP rectangle-capacity test remains the countercheck. No S_rect, rho_prom, or P-vs-NP lower bound follows.

Primary source for the lifting and relation models: [de Rezende et al., *Truly Supercritical Trade-offs for Resolution, Cutting Planes, Monotone Circuits, and Weisfeiler-Leman*, Theorem 2.11 and definitions of Search(F) composed with IND](https://eccc.weizmann.ac.il/report/2024/185/download).

## 128. C-203 - The constant-degree cPHP source passes the decoder-cost exponent screen

C-202 rules out the full-clause unique-output source, but it should not be generalized to all lifted search relations. The CCC 2025 source has many valid answers per pair, and its lifting width can grow while its fixed-answer rectangle mass is controlled by only two Index pointers.

Take the paper's second cPHP regime: a constant-degree bipartite expander with k left vertices and c=alpha k right vertices, where 0<alpha<1 is fixed. The paper's expansion and online-matching argument gives subcube-DAG width W=Omega(k) (Theorem 28); Theorem 11 gives a triangle-DAG lower bound

    L = (m/(A d W log(mk)))^W,

for fixed alphabet size d and an absolute A. Encode each d-ary Bob symbol by a constant number of bits, and let N=Theta(mk) be the candidate truth-table length. This is parameter bookkeeping only; it does not define the needed partywise maps.

For a decoder with at most r output-labelled rectangle leaves per signed mismatch type, C-164's rectangle-mass argument gives, on a Bob restriction omitting density eta,

    r >= (1-eta) Delta m^2 d/(2N),

where Delta=Theta(N^beta/log N) is the OPS low/high Hamming gap. With k,d,W fixed while m (and hence N) grows, this is

    r = Omega(d N^(1+beta)/(k^2 log N)).

The current fusion compiler needs a source-DAG lower bound above T=N^(3+3epsilon)/log N after decoder refinement. Even granting the *smallest* decoder compatible with C-164, the necessary parameter comparison is

    L > T r_min,
    T r_min = Theta(d N^(4+3epsilon+beta)/(k^2 (log N)^2)).

Since W can be made a sufficiently large fixed constant by choosing the cPHP base graph large, the theorem's guaranteed lower-bound expression is Omega(N^W/(C log N)^W) for fixed constants C,k,d,W. Thus L/(T r_min) tends to infinity whenever W>4+3epsilon+beta. The decoder-mass obstruction therefore does **not** kill this cPHP source. This only says the lower bound is large enough to survive the *minimum* forced refinement; C-164 is a lower bound on r, not the required upper bound, and no decoder of size below L/T has been constructed.

To make the refinement accounting explicit, let D be the maximum number of rect-DAG states in a decoder for any one signed mismatch type. A target DAG with S sinks can be pulled back and each sink replaced by a copy of its type decoder, giving a source rect-DAG with O(SD) states; intersecting decoder rectangles with the sink's pullback rectangle preserves product structure. Therefore the lifted lower bound gives S=Omega(L/D), and clearing the compiler threshold T requires D=O(L/T). C-164 lower-bounds only decoder leaves, hence also D, by r_min. The inequality L>T r_min is necessary for this route's decoder budget to remain possible, not sufficient to construct D.

The first transfer condition is now resolved at the high-table restriction: C-204 adapts the CCC theorem's own arbitrary-column Full Range Lemma and triangle-error accounting, so a Bob subset omitting 2^(-N+o(N)) of the columns retains the lifting lower bound. Choosing a power-of-two alphabet and compatible m,k makes flattening Bob's full d-ary array a bijection to N-bit strings. This removes individual high-table generation. The standard CCC map from cPHP to clique-colouring is still unusable here: its Alice-image range has the O(N log N) recognizer in C-200 and its monotone decoder accepts only one mismatch orientation.

**Disposition.** Keep cPHP as a parameter-feasible source with its high-side restriction now available. A transfer still needs (i) partywise table maps with every image promised, (ii) both mismatch orientations to decode, (iii) a per-type decoder upper bound r<L/T, and (iv) a hard low-image envelope. The hard low-image envelope remains central. No C-75, rho, or P-vs-NP lower bound follows.

Primary source: de Rezende and Vinyals, [*Lifting with Colourful Sunflowers* (CCC 2025), Theorem 11, Theorem 28, and the constant-degree cPHP regime](https://drops.dagstuhl.de/storage/00lipics/lipics-vol339/ccc2025/html/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.html).

## 129. C-204 - The colourful-sunflower lifting proof tolerates exponentially sparse omitted Bob columns

This closes O-143 for the deletion scale needed by the cPHP transfer. It is a proof adaptation of the CCC 2025 Theorem 11, not a new statement printed verbatim in that theorem.

Let S:Sigma^n -> O have subcube-DAG width W, and let B be a subset of Bob's lifted universe (Sigma^m)^n. Suppose a triangle-DAG solves S composed with Ind_m^n on [m]^n x B, and the omitted-column density is eta=1-|B|/|Sigma|^(mn). If W log(mn)=o(mn) and eta=2^(-Theta(mn)+o(mn)), rerunning the published extraction gives the same lifting lower-bound order

    size = Omega((m/(A' |Sigma| W log(mn)))^W)

for a possibly adjusted absolute constant A'.

**Proof audit.** The published Full Range Lemma is already formulated for an arbitrary column subset Y, requiring only |Y|>epsilon |Sigma|^(mn), and it uses Alice's blockwise min-entropy separately. Its parameter setting takes epsilon at most 2^(-4W log(mn)). The root column set B has density 1-eta, so it satisfies this hypothesis. At later simulation states the column side is a subset of B; the same lemma applies whenever that side clears the proof's density threshold. Tighten the threshold by a factor of two to absorb any loss eta. The published Triangle Lemma likewise treats the column side as an arbitrary subset and bounds the union of its structured error-column sets by 2^(-W log(mn)). Add B^c to the error bookkeeping: its density eta is smaller than the per-state threshold 2^(-4W log(mn)); even charging it once per protocol state costs at most S eta. For protocols below the theorem's lifting threshold, log S=O(W log(mn)), hence S eta=o(1) under W log(mn)=o(mn). The extracted subcube-DAG and its width contradiction therefore survive, with only constant changes. The only source-theorem inputs used here are the arbitrary-Y Full Range Lemma, the stated error-column union bound, and the same extraction; no assumption that Bob's domain is the entire product is needed.

**cPHP application.** Use the same constant-degree random-expander construction with a sufficiently large fixed power-of-two left degree d=2^a, and choose k,m so N=a m k is a power of two. Flattening y in [d]^(mk) then bijects Bob's full source universe with all N-bit truth tables. Restrict to columns whose tables lie outside SIZE(s2); the omitted fraction is 2^(-N+o(N)), and for fixed k,W the robustness condition holds. Thus the high-side image condition in C-198 is no longer an obstacle for this source: Bob may be the raw flattened string. This does not supply Alice's low-table map, an output decoder, or a hard low-image envelope.

**Disposition.** Mark the dense-column robustness subtask closed for CCC lifting at the OPS deletion density. C-203's parameter-feasible cPHP source can use the high-table restriction. O-124 remains open at the low-image map, both-orientation witness decoding, and decoder upper bound r<L/T. No S_rect, rho, or P-vs-NP lower bound follows.

Primary source: de Rezende and Vinyals, [*Lifting with Colourful Sunflowers* (CCC 2025), Lemma 16, Claim 17, and the proof sketch of Theorem 11](https://drops.dagstuhl.de/storage/00lipics/lipics-vol339/ccc2025/html/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.html).

## 130. C-205 - Dense mismatch slabs make raw cPHP decoding as hard as the source

C-203's exponent screen compared the lifted cPHP lower bound only with the *minimum leaf count* forced by C-164. A stronger obstruction applies to the raw-flattening map in C-204 if the output decoder is fixed by signed mismatch type (rather than tailored to each target-DAG sink).

### Dense-slab lifting lemma

Let `S:Sigma^k -> O` have subcube-DAG width at least `W`, with fixed `Sigma,W`. Let `A` be any subset of `[m]^k` of density at least `1/2`, and let `B` be any subset of `(Sigma^m)^k` of density at least `1/3`. For all sufficiently large `m`, a rect-DAG solving `S composed with IND_m^k` on `A x B` still has size

    Omega((m/(C |Sigma| W log(mk)))^W),

for an absolute constant `C` (with the same fixed-parameter regime as the CCC lifting theorem). This is a proof adaptation of the full CCC theorem, not a separately stated theorem.

**Proof audit.** In Appendix A.2 of the CCC 2025 full version, the Triangle Lemma gives at most `m^(k-(1-delta)W)` error rows per state and a Bob error-column fraction at most `(mk)^(-W)` per state. Suppose the restricted-domain protocol has at most `(1/8)m^((1-delta)W)` states. The union of row errors has size at most `m^k/8`, so at least `3m^k/8` rows of the initial `A` survive. For any nonempty `I subseteq[k]` and fixed address pattern `a in [m]^I`, at most `m^(k-|I|)` rows of the full cube realize `a`; therefore its probability under the surviving row set is at most `(8/3)m^(-|I|) <= (m/8)^(-|I|)`. The surviving rows have blockwise min-entropy at least `log(m/8)`, which exceeds the theorem's required `delta log m` for large `m` because `m^delta=Theta(|Sigma| W log(mk))`.

The accumulated Bob error fraction is at most

    (1/8)m^((1-delta)W)(mk)^(-W) = (1/8)m^(-delta W)k^(-W) = o(1).

Since `B` initially has density at least `1/3`, a constant-density Bob set remains. The root rectangle is therefore still pre-structured: its row side has the required blockwise entropy and its column side exceeds the Full Range Lemma's exponentially small threshold. The CCC simulation then extracts a width-`W` subcube-DAG for `S`, a contradiction. Reducing the size constant changes only the constant in the lower bound. This argument uses the full-version appendix's root/error-removal steps and its Full Range Lemma; see [the primary CCC paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol339/ccc2025/html/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.html) and [the authors' full version, Appendix A](https://derezende.github.io/index_files/colourful-sunflowers.pdf).

### Application to raw flattened cPHP

Use `N=a m k`, `d=2^a`, and the C-204 bijection `beta:[d]^(mk) -> {0,1}^N` obtained by flattening the symbol array. Let `alpha:[m]^k -> {0,1}^N` be any proposed Alice map; no circuit or injectivity assumption is needed for this obstruction. Fix any table coordinate `i`. One bit value `b` has an Alice preimage

    A = {x : alpha(x)_i=b}

of density at least `1/2`. Since `beta` is a bijection and its `i`th bit is balanced, the Bob slab

    B = {y : beta(y)_i=1-b and beta(y) is outside SIZE(s2)}

has density at least `1/2 - |SIZE(s2)|/2^N = 1/2-o(1)`, hence at least `1/3` for large `N`. Every pair in `A x B` has the same signed mismatch type `(i,b)`.

Consequently, a decoder that is specified only by `(i,b)` and must turn every occurrence of that signed mismatch into a valid cPHP witness is itself a rect-DAG solver for the lifted cPHP relation on `A x B`. By the dense-slab lifting lemma, that decoder has size `D=Omega(L)`, where `L=(m/(A_0 d W log(mk)))^W` is the source lower-bound scale from C-203. A target DAG with `S` sinks and a type-only decoder family of maximum size `D` gives a source DAG of size `O(SD)` by copying the relevant decoder at each sink and intersecting rectangles. The source lower bound then yields only `S=Omega(1)`, so this refinement route cannot reach the required `N^(3+3epsilon)/log N` threshold.

**Scope.** This closes the raw-bijection plus type-only-decoder version of the cPHP transfer, regardless of how the low tables are chosen. It does not rule out a non-raw Bob map, or decoders tailored to the target sink rectangle: a sink restriction may destroy the dense row/column hypotheses, and its context cost must be charged globally. It also does not lower-bound the actual C-75 DAG. C-203 remains a correct *necessary leaf-count* feasibility screen, but it is not evidence that the full per-type decoder can be cheaper than the source lower bound. Continue O-124 only through a materially different map or a proved sink-context accounting theorem; keep O-141 active. No rho or P-vs-NP lower bound follows.

## 131. C-206 - Address-entropy regularization bounds the codimension of a sink context

This advances O-144 by isolating what a sparse row side of a sink can look like before applying the lifting argument.

### Entropy-boosting lemma

Let `A` be a nonempty subset of `[m]^k` of density `rho`, and fix `0<delta<1`. There is a partial assignment `alpha` fixing `t` coordinates and a nonempty slice `A' = A intersect C(alpha)` such that `A'`, on the remaining coordinates, has blockwise min-entropy at least `delta log m`, with

    t < log(1/rho) / ((1-delta) log m).

**Proof.** Start with `A`. If the current slice is not blockwise `delta log m`-dense on its unfixed coordinates, there is a nonempty coordinate set `I` and pattern `a` with conditional probability greater than `m^(-delta |I|)`. Restrict to that pattern. If the current slice has density `rho_j` in its current subcube, the new density is

    rho_(j+1) = rho_j Pr[x_I=a | x in A_j] m^|I| > rho_j m^((1-delta)|I|).

Each step fixes at least one new coordinate, so the process terminates. If it fixes `t` coordinates in total, the final density is greater than `rho m^((1-delta)t)` and at most one, giving the stated bound. This is a direct min-entropy regularization argument; it does not use a lifting theorem.

### What it buys for sink rectangles

For a pulled-back sink rectangle `A_v x B_v` of normalized area at least `1/S`, its row density is at least `1/S`. If `S <= N^q`, `m=Theta(N)`, and `k,q` are fixed, C-206 yields a blockwise-dense row slice after fixing only `O(q)` pointer addresses. Thus a sink with polynomially small area need not be treated as an arbitrary low-entropy row set; it has a low-codimension structured witness.

For a complete cPHP source with `k=2c` pigeons and `c` holes, fixing `t<c` pointer addresses lets us partition Bob columns by the `c^t` selected-hole patterns at those addresses. On a pattern with distinct holes, the online-matching adversary can start with that size-`t` matching and continue on the remaining complete bipartite graph; the residual base width remains `Omega(c-t)`. The lifted theorem can then be applied if that pattern retains enough Bob columns. A pattern with a repeated hole instead has an immediate valid collision answer. For uniform Bob arrays, the union of these collision patterns has probability at most `binom(t,2)/c`; after restricting to high tables, the deleted density is still negligible for fixed `t`.

**Exact failure point.** A sink's Bob rectangle may concentrate on the collision patterns, making its decoder cheap on the selected row slice. If it retains a dense injective pattern, the residual lifted search is hard. The entropy lemma gives one structured address slice per sink, but those slices need not cover the sink row side, and their masses can overlap across sinks. No global charge has been proved that sums the hard injective slices or forces enough distinct collision-context states. This is a local regularization and a sharper O-144 map, not a rect-DAG lower bound. O-141 remains active; no C-75, rho, or P-vs-NP lower bound follows.

## 132. C-207 - Primary-source reconciliation: short descriptions do not reduce shared-DAG size

This checkpoint answers the requested model comparison and universal-DAG falsification test in one normal form. It is a verified model theorem and route filter, not a new lower bound.

Let `Y=SIZE(s1)`, `Z={0,1}^N\SIZE(s2)`, and `Mis(w,z)` output a signed coordinate `(i,b)` with `w_i=b` and `z_i=1-b`. Since `s1<s2`, `Y` and `Z` are disjoint, so `Mis` is total on `Y x Z`. For a proposed fusion list `Q`, the stricter witness relation outputs a decreasing activation/support path ending at such a signed coordinate; it is total on `Y x Z` exactly when `Q` succeeds on every low anchor. These are different relations and their totality must not be conflated.

### The standard shared graph is exactly separator-circuit size

Write `S_rect(Y,Z)` for the minimum size of Sokolov's Boolean communication game / binary rect-DAG for `Mis`, and `C_sep(Y,Z)` for the minimum Boolean circuit size of an `h` satisfying `h(w)=1` on `Y` and `h(z)=0` on `Z` (values on the medium band are free). Then

    C_sep(Y,Z) = Theta(S_rect(Y,Z)).

For the DAG-to-circuit direction, every state is a product rectangle, every leaf's rectangle has one fixed signed-mismatch label, and the two child rectangles cover the parent. The rectangle-cover trichotomy lets the parent separator be built from the child separators by AND, OR, or copying one child; leaves are literals (possibly negated). This is Sokolov's Boolean-game construction, restricted from full preimages to the promise. Conversely, a separator circuit gives its Karchmer-Wigderson game on the full 1/0 preimages, and restricting the two input sets to `Y` and `Z` preserves the graph and all valid outputs. The standard size loss is constant-factor, subject to the chosen Boolean basis.

The description-space version has exactly the same minimum. For any surjection `G:D -> Y` from syntactic circuit descriptions to their distinct truth tables, lift each Alice predicate by precomposition with `G`; in the reverse direction choose a section `sigma:Y -> D` and restrict each predicate to `sigma(Y)`. Both operations preserve every graph node, rectangle-cover condition, and output. Therefore

    S_rect(D x Z under G) = S_rect(Y x Z) = Theta(C_sep(Y,Z)).

This proves the precise obstruction to the syntax-only construction: a description-aware small shared graph would already be a small sparse-envelope separator. Universal evaluation computes `G(d)_i` locally, but does not implement the existential projection that separates all low tables from all high tables.

### Complexity notions and quantitative losses

- Deterministic communication for plain mismatch is at most `O(s1 log(n+s1)+log N)` bits: Alice sends a circuit description and Bob returns a differing coordinate. It is at least `log2(N-log2 M2)` bits, where `M2=|SIZE(s2)|`, because fewer than `N-log2 M2` distinct output coordinates leave a high completion agreeing with any fixed low row.
- Protocol-tree size is a separate quantity. The distinct-output argument gives at least `N-log2 M2` leaves; the description protocol gives at most `N*2^(O(s1 log(n+s1)))` nodes. A short bit protocol is not a small tree, and neither bound supplies graph sharing.
- Standard rect-DAG size is `Theta(C_sep)`. The parity KW relation is the clean artificial calibration: its formula/tree size is `Omega(N^2)` by Khrapchenko, while its circuit/rect-DAG size is `O(N)`. This demonstrates that sharing can matter, but gives no transfer to `Y x Z`.
- For the promise fusion measure, `q_min=rho_prom=D_circ_cap(Y|B_prom)` exactly. The current acyclic AND-only conversion is `D_cap <= q^2`; the best recorded ordinary rect-DAG compiler is `S_rect=O(q^3/log q)`, while a rect-DAG gives `rho_prom=O(S_rect)`. Thus a standard-DAG lower bound must exceed `N^(3+3 epsilon)/log N` to force `rho_prom>N^(1+epsilon)` with this compiler. A linear DAG lower bound, even with an unbounded factor, does not by itself meet that target.
- The q activation states are a ranked **cyclic** support system. A support path terminates because the first-activation rank decreases on each input pair, but the static dependency graph can contain cycles. It is not a Sokolov/GGKS acyclic rect-DAG; counting q rule states alone omits support routing and cycle removal. Nakayama-Mar(u)oka loop circuits are a conceptual ancestor, not an identity for this semi-filter/intersection measure; Cavalar-Oliveira's exact adaptation is the identity above. Amano-Mar(u)oka conjunctive complexity counts acyclic AND gates and concerns quadratic functions, so it applies here only through a proved AND-preserving reduction.

### Local state non-shareability and the unresolved aggregation

For a state rectangle `A_v x B_v`, let `K_v` be the table coordinates appearing at descendant output leaves, `k_v=|K_v|`, and `r_v=|pi_{K_v}(A_v)|`. For every low trace `p` on `K_v`, the full cylinder extending `p` is disjoint from `B_v` on high tables: otherwise its row witness and that high column agree at every descendant output. Since the `r_v` cylinders are disjoint and all non-high strings together number `M2`, this gives the local capacity inequality

    |B_v| + r_v * 2^(N-k_v) <= 2^N,
    density(B_v) + r_v/2^k_v <= 1.

Thus a state with a Bob side of density at least `1-eta` can retain at most `eta*2^k_v` low-row traces on its descendant output support. This is a clean local non-shareability constraint. At the root it recovers the near-full output-support requirement. It still does not aggregate: different state rectangles can exclude the same high columns, and the C-80 O(N)-state router shows that summing excluded-column mass over states is invalid. A valid Tier 1-3 argument must charge *which product-hull context* reaches each shared suffix, not just its rectangle's total excluded mass.

### Disposition

The primary definitions confirm that no known DAG model makes the universal-description route automatically small. The direct OR over descriptions costs `N*2^(O(s1 log(n+s1)))`; no `N^(1+o(1))` universal graph has been constructed. The route is not killed as a way to prove the target: proving or refuting such a graph is exactly the sparse-envelope circuit problem. The live Tier 1-3 target remains O-141/O-133: a product-hull-safe, globally charged state-merging lemma for the actual promise, strong enough to yield `S_rect>N^(3+3 epsilon)/log N`, or a near-linear separator construction that closes the route.

Primary sources: [Sokolov, *Dag-like Communication and Its Applications*, Definitions 2.1/2.3 and Theorem 3.2](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download); [Garg, Göös, Kamath, and Sokolov, *Monotone Circuit Lower Bounds from Resolution*, rectangle/triangle-DAG models](https://theoryofcomputing.org/articles/v016a013/); [Cavalar and Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*, Theorem 30 and its discussion of Nakayama-Mar(u)oka](https://doi.org/10.1145/3718746); [Nakayama and Maruoka, *Loop Circuits and Their Relation to Razborov's Approximation Model*](https://doi.org/10.1006/inco.1995.1083); [Amano and Maruoka, *The Monotone Circuit Complexity of Quadratic Boolean Functions*](https://doi.org/10.1007/s00453-006-0073-0).

## 133. C-208 - The local capacity bound is exactly projection disjointness

This audits C-207's local inequality before trying to aggregate it.

Let a valid rect-DAG state v have rectangle `A_v x B_v`, and let `K_v` be the set of table coordinates appearing on output leaves below v. Because the graph is acyclic and every valid nonleaf pair has a valid child, every pair in this rectangle reaches some valid output leaf below v. Therefore

    pi_Kv(A_v) intersect pi_Kv(B_v) = empty.

This condition is equivalent to saying that every pair in `A_v x B_v` has *some* mismatch coordinate in `K_v`: if the two projections shared a pattern, choosing rows and columns realizing it would give a pair with no available output below v; if they are disjoint, every pair differs somewhere in K_v. It follows immediately that, writing `k_v=|K_v|` and `r_v=|pi_Kv(A_v)|`,

    |B_v|/2^N <= |pi_Kv(B_v)|/2^k_v <= 1-r_v/2^k_v.

So C-207's capacity inequality is exact, but it is a projection-disjointness fact for *any* search relation whose answers are coordinate mismatches. It does not by itself use the circuit-complexity promise and is not yet a new Gap-MCSP lower-bound handle.

At the root, `B_root=Z`. For each low-row trace on K, its entire truth-table cylinder contains no high table; the disjoint cylinders therefore satisfy `|pi_K(Y)|*2^(N-|K|)<=M2`. This recovers the near-full root output-support lower bound. At internal states the low-trace exclusion sets can overlap across vertices. C-80/C-175 give the concrete countercheck: the same high columns are excluded at many scan states in an O(N)-state DAG. Raw summation of the local capacities cannot prove a superlinear bound.

**What remains genuinely uncharged.** Projection disjointness guarantees that a mismatch exists among the descendant labels; it does not provide a binary rectangle routing that selects one. The missing quantity must account for the *parent-conditioned routing of the common projection patterns* when states merge. This narrows O-141: stop trying to sum `|Z\\B_v|` or the equivalent local density deficit. Seek a transition/merge invariant that charges repeated pattern contexts only when the product hull forces them to be distinguished. The C-80 router and C-160 threshold separator remain mandatory calibrations. No new bound on `S_rect`, `rho_prom`, or P versus NP follows.

## 134. C-209 - Shared states must solve the full product hull of merged histories

This states the exact merge condition behind O-141 without assuming a state can handle only a bounded number of anchors.

Let `v` be a state of a rect-DAG, with local rectangle `R_v=A_v x B_v`. For each feasible root-to-v path h, let `H_h=A_h x B_h` be its history rectangle: the intersection of the row sides and column sides tested along that path. Since the path reaches v, `H_h subseteq R_v`. For any collection of nonempty histories entering v, put

    A_* = union_h A_h,     B_* = union_h B_h,     Hull = A_* x B_*.

Each `A_h subseteq A_v` and each `B_h subseteq B_v`, hence `Hull subseteq R_v`. Every pair in this full product hull is therefore solved by the suffix rooted at v, including cross-pairs whose row and column came from different histories. If `K_v` is the set of descendant output coordinates, the C-208 condition gives

    pi_Kv(A_*) intersect pi_Kv(B_*) = empty,

or equivalently `pi_Kv(A_h) intersect pi_Kv(B_g)=empty` for every ordered pair of histories h,g. This is a necessary state-merging law. It is stronger than checking only the original history rectangles separately.

### Stress tests and the remaining gap

- **C-80 block router:** it passes the law because it is an actual rect-DAG; its shared suffixes solve the cross-products admitted by their local rectangles. Thus the law cannot be used to claim that exponentially many low rows force many contexts. Any quantitative potential derived from it must still allow the O(N)-state router on this structured subpromise.
- **C-191 trace-equality contexts:** for histories `H_sigma=Y_sigma x Z_sigma`, different signatures sigma and tau can be merged only if the common suffix has outputs covering their cross-signature differences. The cross-hull condition alone does not forbid this: when Q outputs remain available, off-diagonal pairs can exit on Q, while diagonal pairs may be handled by tail outputs. C-191 only lower-bounds covers whose rectangles are required to stay inside the equality relation; an unrestricted suffix need not obey that restriction. Thus C-209 formalizes the Q-output-exit tradeoff but does not solve it.

The condition is a useful Tier 3 structural target, not a size lower bound: every valid DAG satisfies it by definition, and it gives no lower bound until we prove that many history collections have product hulls with large residual separator complexity and that these costs cannot reuse the same suffix gates. The next test is to quantify the number of distinct cross-history projection patterns a single suffix can safely support, while retaining C-80/C-160 counterexamples. No `S_rect` or `rho_prom` lower bound follows from C-209 alone.

## 135. C-210 - Rank-lifting makes the acyclicization cost explicit

This continues the C-74/C-75 shared-DAG audit by testing whether the q activation states can simply be counted as an ordinary DAG. They cannot, but the exact obstruction and the state expansion can be stated directly.

For a truth table `v`, let `tau_i(v)` be the first closure round at which rule `i` activates, and set `tau_i(v)=infinity` if it never activates. For `1<=r<=q`, define the product rectangle

    R_(i,r) = {w in Y : tau_i(w)<=r} x {z in Z : tau_i(z)=infinity}.

For every empty-intersection rule i, `R_(i,q)` is a root option. If Q succeeds, these rectangles cover `Y x Z`: every low row activates some empty rule, and no high column activates an empty rule, by the principal-filter witness.

At a pair in `R_(i,r)`, at least one of `E_i,H_i` is absent from z's closure. Choose that side S. Since i activates on w by round at most r, membership of S in w's closure has either (a) a literal-slice seed, yielding a valid signed mismatch leaf, or (b) a prior rule j with `T_j subseteq S` and `tau_j(w)<tau_i(w)<=r`. In case (b), S absent from z's closure implies `T_j` is absent there too, so the pair lies in `R_(j,r-1)`. Thus the rank-layered graph is acyclic and solves the Q-path relation.

This gives an explicit acyclic **multiway** graph with at most `q^2+2N+1` vertices. Each `(i,r)` state can have up to `2q` rule successors and up to `2N` signed-literal successors, so the construction can have `O(q^2(q+N))` arcs. At the OPS parameters, successful covers have `q>=N/2`, making this `O(q^3)` arcs. Under Sokolov's binary-outdegree convention, replacing the multiway routing by binary routers costs proportional to these choices; the existing `O(q^3/log q)` compiler remains the best recorded standard rect-DAG conversion. Therefore the `q^2` vertex count is not an `O(q^2)` binary-DAG bound: it hides the support-routing edges.

If cycles are allowed with the explicit requirement that every play follows a strictly decreasing pair-dependent rank, the original q rule states plus output labels already suffice; there are up to `O(q(q+N))` possible support arcs. This is the natural ranked cyclic protocol corresponding to the closure proof, and its termination is certified per input pair rather than by a global topological order. The cover parameter charges the q intersection rules; it does not charge an ordinary binary routing graph. This distinction is consistent with the exact identity `q=rho_prom=D^circ_cap` and prevents treating the closure network as an ordinary q-node rect-DAG.

### Reverse direction, description space, and lower-bound target

The reverse standard transformation remains linear up to basis constants: an S-node rect-DAG gives an O(S)-size promise separator by the rectangle-to-circuit induction, and the fusion construction gives `rho_prom<=O(S)`. Hence a rect-DAG lower bound transfers to q, but the forward compiler `S=O(q^3/log q)` is the costly direction. To force `q>N^(1+epsilon)` by that forward compiler still requires `S>N^(3+3epsilon)/log N`; the acyclic AND-count bound `D_cap<=q^2` offers a separate target above `N^(2+2epsilon)`.

No description-space shortcut changes these inequalities. For `G(d)=TT(C_d)`, precomposing Alice predicates with G lifts a truth-table DAG to descriptions, and restricting to one chosen description per low table maps any valid description DAG back with exactly the same graph. A universal circuit evaluates a candidate d, but a shared separator still solves the existential projection `exists d: G(d)=w`. The known restriction-profile router has size `O(|Y|+sum_I pi_I(Y))`; point-minterm circuits make `pi_I(Y)=2^|I|` on blocks of size `Theta(s1/n)`, so this specific router is exponentially large at an OPS level. This kills that router, not arbitrary DAGs.

### Disposition

C-210 proves an explicit rank-layered acyclicization and exposes its fan-out cost; it does not improve the best compiler or lower-bound the actual relation. The exact model comparison is: Sokolov/GGKS use acyclic binary product-rectangle DAGs; C-75 is their promise-restricted signed-mismatch relation (also partial monotone KW under dual rails); the fusion list is exactly Cavalar-Oliveira cyclic intersection complexity on the promise ground set; Nakayama-Mar(u)oka loop circuits are related but not an identity for this semi-filter model; Amano-Mar(u)oka AND-count results need a separate reduction. No small universal DAG, superlinear `S_rect`, superlinear q, or P-vs-NP proof has been obtained. Keep O-141 active and charge merged histories through C-209's product hulls.

Primary sources: [Sokolov, *Dag-like Communication and Its Applications*](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download); [Garg, Göös, Kamath, and Sokolov, *Monotone Circuit Lower Bounds from Resolution*](https://theoryofcomputing.org/articles/v016a013/); [Cavalar and Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://doi.org/10.1145/3718746).

## 136. C-211 - Near-linear mismatch hitting sets do not provide a shared-DAG router

This tests a concrete universal construction using the fact that low/high tables are Hamming-separated. It produces a small *static coordinate family* but does not yet produce a protocol.

### A near-linear family of coordinate sets hits every pair

If `w` has circuit size at most s1 and `z` differs from w in r truth-table positions, one can patch the circuit for w at those r inputs using r point minterms, at cost `O(rn)` gates. Hence, when `s2/s1` grows, every `w in Y, z in Z` has

    |{i : w_i != z_i}| >= d = Omega((s2-s1)/n) = Omega(s2/n).

Assume the OPS regime `d=o(N)` and `d->infinity`. Choose `k=ceil(N/d)` independent uniformly random k-subsets of `[N]`. A fixed d-set D is missed by one set with probability at most `(1-d/N)^k<=e^-1`. With `R=ceil(2d ln(eN/d))` independent sets, the failure probability for a fixed D is at most `e^-R`; there are at most `(eN/d)^d` such D. A union bound shows some family `Q_1,...,Q_R`, each of size k, hits every d-set and therefore every low/high mismatch set. Its total number of coordinate incidences is

    Rk = O(N log(eN/d)) = O(N log N).

Thus simple output-support coverage is near-linear even though any one row-selected support set must have `N-o(N)` coordinates (C-168). The family chooses a set *depending on the pair's mismatch set* only existentially; it is not yet an algorithm or a DAG.

### Why the hitting family does not yet give a protocol

For a set Q, the predicate `there is a mismatch in Q` is generally a union of mismatch rectangles, not a rectangle. On two coordinates, rows and columns with patterns `{00,11}` yield the off-diagonal relation; one product rectangle containing both off-diagonal pairs also contains the equal diagonal pairs. Therefore a binary rect-DAG cannot simply route the root into a state “sample Q_j is hit” and then search Q_j. Converting that existential sample choice to product-rectangle routing is the missing step.

A fixed-order scanner that forgets tested coordinates also fails its direct merge test: for `t<=Theta(s1/n)`, point-minterm circuits realize every pattern on t tested addresses, and since `N-t>log2|SIZE(s2)|`, each pattern has a high completion. If two distinct matched-prefix histories are merged into a suffix allowed to output only on the untested coordinates of that same sample, their cross-history pair can agree on every such suffix coordinate. C-209 then forbids the merge. This rules out the *discard-the-prefix, scan-only-the-current-sample* architecture at `2^t` contexts; it does not rule out a protocol whose suffix revisits earlier coordinates or uses other samples, since those exits may solve the cross-pairs.

### Disposition

The hitting-set lemma is a useful negative calibration: mismatch-support coverage can be `O(N log N)` while standard rect-DAG routing remains hard. It gives no upper or lower bound on `S_rect` or q, and does not close O-141. The next test is whether an adaptive sample selector can be represented by product rectangles while charging its cross-history exits, or whether a global near-linear router exists. Keep C-80/C-160 and C-209 active; no breakthrough follows.


## 137. C-212 - Shared block decoders sharpen sparse interpolation; the global DAG gap remains

This is a proof-level improvement to the local interpolation and patching bounds used throughout C-75. It strengthens several architecture-specific obstructions, but does not yet lower-bound an unrestricted rect-DAG or improve the fusion-cover transfer.

### Sparse-set indicator lemma

For any set `S` of `r` addresses in `{0,1}^n`, its indicator `1_S` has a fan-in-two Boolean circuit of size

    O(n + r*n/log(r+1)).

For `r=0` use a constant; for `r=1` use one equality test of size `O(n)`. For `r>=2`, put `L=floor(log2 r)` and partition the `n` input bits into `m=ceil(n/L)` blocks of width at most `L`. In each block, build all block-pattern equality signals using a shared binary prefix-conjunction trie. The trie uses `O(2^L)` gates per block, not `O(L*2^L)`: each node adds one input literal to its already-computed prefix. For every `a in S`, AND the `m` block signals matching `a`; then OR these `r` point indicators. The total is

    O(n + m*2^L + r*m + r)
      = O(n + r*n/log(r+1)).

The construction has no false positives and uses the standard project basis (fan-in-two AND/OR/NOT, constant-factor changes for any fixed complete basis). It exploits unbounded fan-out, as does the project circuit-size convention.

For a fixed coordinate set `Q` of size `t` and any prescribed bit pattern on `Q`, take `S` to be its 1-set. Restricting `1_S` to `Q` realizes exactly that pattern, with cost `O(n+t*n/log(t+1))`. In the OPS regime `s1=N^beta/(c*n)` for fixed `0<beta<1`, `log s1=beta*n-O(log n)`. Hence, for a sufficiently small constant `alpha=alpha(beta,basis)>0`, every labeling on every fixed set of `t=floor(alpha*s1)` table addresses is realized by a size-`s1` circuit. The gate count is `K*n + K*t*n/log(t+1) <= s1` after choosing alpha small and n large.

This is an improved project lemma, not a claim that shared-decoder/Lupanov synthesis is globally new. The novelty claim is limited to tightening and propagating the prior project bounds.

### Patching consequence: high tables are linearly far

If `w` and `z` differ on a set `D` of size `r`, then `z = w XOR 1_D`; one XOR-composition costs only a constant number of gates beyond the sparse indicator. Thus

    CC(z) <= CC(w) + O(n + r*n/log(r+1)).

Writing `Delta=s2-s1`, this forces

    dist_H(w,z) = Omega(Delta*log(Delta+1)/n)

whenever `log Delta=Theta(n)`. For the OPS parameters, `Delta=(1-o(1))s2` and `log Delta=beta*n+O(1)`, so every low/high pair has Hamming distance `Omega(s2)`, improving the earlier `Omega(s2/n)` bound by a factor of order n. The constants may depend on beta and the fixed gate basis.

The same patching bound upgrades C-135: if all rows in a state-side family agree with a low row `w0` outside a varying-coordinate set `V`, and `|V|<=a*Delta*log(Delta+1)/n` for a sufficiently small constant a, then every high table differs from `w0` outside V. Bob can scan the common coordinates and obtain an `O(N)`-state mismatch router for that rectangle. In the OPS regime this local easy-rectangle threshold is `Theta(s2)`, not merely `Theta(s1)`. It remains a local router, not a decomposition theorem for arbitrary DAGs.

### Quantitative corrections to earlier checkpoints

The following are stronger readings of old claims; the old weaker inequalities remain true. For each entry, the restriction to its stated architecture or relation remains essential.

| Checkpoint | Earlier scale | Updated scale | What it still does not prove |
|---|---:|---:|---|
| Uniform low-table shattering (C-133, C-137, C-170) | `Theta(s1/n)` coordinates | `Theta(s1)` coordinates | No unrestricted rect-DAG lower bound; fixed-order and one-switch only |
| C-133 restriction-profile router | `2^(Omega(s1/n))` states at a level | `2^(Omega(s1))` states at a level | Kills that router only |
| C-137 fixed-order equal-prefix scanner | `2^(Omega(s1/n))` contexts | `2^(Omega(s1))` contexts | Does not cover adaptive product-rectangle routing |
| C-170 Bob-first one-switch frontier | `2^(Omega(s1/n))` states | `2^(Omega(s1))` states | Multi-switch DAGs remain open |
| C-172 root output support | `N-log M2 + Omega(s1/n)` | `N-log M2 + Omega(s1)` | Still only `N-o(N)`; no internal-state summation |
| C-135 low-variation rectangle router | `|V|=Theta(s1)` | `|V|=Theta(s2)` | Local easy-rectangle classification only |
| C-136/C-211 low/high Hamming distance | `Omega(s2/n)` | `Omega(s2)` | Output support still does not route through rectangles |
| C-189 Bob-selected certificate `h_Y(z)` | `Omega(s1/n)` | `Omega(s1)` for every high z | A coordinate certificate is not a shared DAG |
| C-191 trace signatures on C-190's Q | `log r_Q=Omega(s1*log n/n)` | `log r_Q=Omega(s1*log n)` | Rectangles confined to Q-equality only; Q-output exits remain uncharged |
| C-195 top comparison-state cover | `2^(Theta(s1/n))` | `2^(Theta(s1))` rectangles | That triangle state is not forced in an arbitrary rect-DAG |
| C-211 universal hitting family | `O(N log N)` incidences | unchanged asymptotically | “Sample contains a mismatch” remains nonrectangular |

For C-191, take `t=Theta(s1)` and `k=ceil(log2 |Y|)+1`. The sparse indicators give `r_Q>=binom(k,t)`. Counting the t-point low indicators gives `k>=t*log2(N/t)=Omega(s1*n)`; the standard circuit-count upper bound gives `k=O(s1*n)`, so `k/t=Theta(n)`. Hence `log2 r_Q>=t*log2(k/t)=Omega(s1*log n)`. This is still only the cover number of rectangles constrained to the equality relation. For C-195, the low prefix family now has `2^t` members for `t=Theta(s1)`; since `t=o(N)` and `log M2=o(N)`, each consecutive-prefix gap still contains a high table. Its O(N)-state suffix scanner for that selected subpromise remains intact.

C-136's fractional labelled-rectangle cover improves to total weight `O(N/s2)` because every pair has `Omega(s2)` mismatches. The simple output-disjoint family from C-138 has `Omega(N/s2)` pairs, matching this method ceiling in order. The public-coin mismatch search improves to expected `O(N/s2)` bit reveals. The static random coordinate-family construction still has `O(N log(N/s2))=O(N log N)` total incidences, and still does not choose a sample by a product-rectangle transition.

### C-75 model comparison and exact inherited transfers

The closest-model audit at C-207 remains the correct framework. The primary definitions support these distinctions:

| Model | Feasible states / size | Exact relation to this project |
|---|---|---|
| Sokolov Boolean DAG-like communication; GGKS rect-DAG | Acyclic, out-degree at most two; every state is a product rectangle cut out by separate Alice/Bob predicates; size counts graph vertices | Plain C-75 signed mismatch on `Y x Z` is exactly this promise-restricted relation. Its minimum size is `Theta(C_sep)`, the minimum Boolean separator-circuit size. |
| GGKS triangle-DAG / broader `F`-DAG | Acyclic bounded-outdegree graph, but a state may be a triangle or an intersection of allowed predicates rather than a product rectangle | A stronger geometry. C-194's `4N-1` interval-comparison protocol uses triangle states; C-195 shows its top state needs `2^(Theta(s1))` rectangles even on this promise. That state expansion is not a lower bound on alternative rect-DAGs. |
| Cavalar-Oliveira cyclic intersection complexity | Cyclic state dependencies are interpreted through their specified closure/least-fixed-point semantics | The promise fusion measure is exactly `q=rho_prom=D^circ_cap`. It is not standard acyclic DAG size. |
| Nakayama-Mar(u)oka loop circuits | Cyclic circuit specifications with their loop semantics, related by the fusion characterization | A conceptual and theorem-level ancestor, but not an identity with every semi-filter or promise variant absent the Cavalar-Oliveira adaptation. |
| Amano-Mar(u)oka conjunctive complexity | Number of AND gates in monotone circuits for quadratic Boolean functions | No direct C-75 transfer; it needs an AND-preserving reduction. |

For plain mismatch, Alice has `w`, Bob has `z`, and a valid answer is `(i,b)` with `w_i=b` and `z_i=1-b`; it is total because `Y` and `Z` are disjoint. For a fixed proposed fusion list Q, the stricter closure-path relation outputs either such a literal witness or a supported predecessor rule of strictly smaller first-activation rank. It is total on `Y x Z` exactly when Q covers every low anchor while no high table reaches an empty carrier. Deterministic communication bits, protocol-tree nodes, rect-DAG vertices, and cyclic rule count q are different resources.

The existing bounds make the separation explicit. For plain mismatch, deterministic communication is `O(s1*log(n+s1)+log N)` bits by sending a low-circuit description, and is at least `log2(N-log2 M2)` bits by the distinct-output lower bound. A protocol tree has at least `N-log2 M2` leaves and the description protocol gives at most `N*2^(O(s1*log(n+s1)))` nodes. In contrast, `S_rect=Theta(C_sep)`. Parity gives a familiar sharing calibration (formula/tree size `Omega(N^2)` versus `O(N)` circuit/DAG size), while circuit counting gives bit-KW relations with `O(N)` communication but exponential DAG size. Neither artificial calibration transfers a lower bound to the actual promise.

The existing quantitative chain remains: `S_rect=Theta(C_sep)`; a standard rect-DAG of size S gives `rho_prom=O(S)`; the best recorded successful-cover compiler is `S_rect=O(q^3/log q)` (rank lifting gives q^2 vertices only before high-fan-out support routing); and the acyclic AND-only conversion gives `D_cap<=q^2`. Thus the current standard-DAG target is `S_rect>N^(3+3epsilon)/log N` to force `q>N^(1+epsilon)` through the cubic compiler, or above `N^(2+2epsilon)` through the separate AND-only bound. The reverse transfer and these losses are unchanged by C-212.

Short descriptions still do not make a shared DAG small. Pulling Alice predicates through `G(d)=TT(C_d)` and restricting along one chosen description per low table preserve every graph node, so description-space and truth-table-space rect-DAG sizes are equal. A universal circuit evaluates one description; it does not remove the existential projection over all descriptions. The direct OR construction costs `N*2^(O(s1 log(n+s1)))`; no `N^(1+o(1))` DAG or separator has been constructed. Conversely, no lower bound against all such DAGs has been proved.

### Disposition

C-212 strengthens shattering, patching, local router, and restricted-context bounds, and it closes the previous factor-n weakness in the uniform Hamming separation. It does not charge cross-history product hulls globally. The first missing implication remains: many locally necessary signature/context distinctions do not yet force many vertices in an unrestricted multi-output rect-DAG, because off-diagonal pairs may exit on Q and share a tail. O-141 stays active; C-80/C-160 and the product-hull law C-209 remain required counterchecks. No superlinear `S_rect` or `rho_prom` lower bound, and no P-vs-NP proof, follows.

The earlier ceilings `rho_w<=N-1`, `rho*=O(N)`, and `rho(H)=O(N*log|H|)` remain unchanged. C-212 does not collapse the live route to a fixed semi-filter family: its new facts concern low/high promise geometry, but the missing issue is still adaptive product-rectangle routing and global sharing.

Primary sources for the model distinctions: [Sokolov, *Dag-like Communication and Its Applications* (ECCC TR16-202)](https://eccc.weizmann.ac.il/report/2016/202/download); [Garg, Göös, Kamath, and Sokolov, *Monotone Circuit Lower Bounds from Resolution*](https://theoryofcomputing.org/articles/v016a013/v016a013.pdf); [Cavalar and Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://www.dcs.warwick.ac.uk/~igorcarb/documents/papers/CO25.pdf); [Nakayama and Maruoka, *Loop Circuits and Their Relation to Razborov's Approximation Model*](https://doi.org/10.1006/inco.1995.1083); [Amano and Maruoka, *The Monotone Circuit Complexity of Quadratic Boolean Functions*](https://doi.org/10.1007/s00453-006-0073-0).


## 138. C-213 - A universal linear cyclic rectangle protocol is too strong a model for fusion

This is a deliberate attempt to kill lower bounds in the broader cyclic communication model. It succeeds there, and sharpens the exact missing transformation to the fusion closure.

Let `A,B` be any disjoint subsets of `{0,1}^N`. For each coordinate `i` modulo N, create a state `S_i` whose feasible rectangle is all `A x B`. Create selector states `P_(i,b)` with rectangle `{x in A:x_i=b} x B`, and one output leaf `L_(i,b)` with rectangle `{x in A:x_i=b} x {y in B:y_i=1-b}`. At `S_i`, Alice selects `P_(i,b)` using her bit `x_i`. At `P_(i,b)`, Bob outputs `L_(i,b)` if `y_i=1-b`; if the bits agree, he goes to `S_(i+1)`, with `S_(N+1)=S_1`.

Every feasible set is a product rectangle. The graph has N scan states, 2N selector states, and 2N output leaves: `5N` vertices and out-degree at most two. The deterministic transition strategy terminates from any `S_i`: it checks coordinates cyclically, and because `A` and `B` are disjoint every input pair has a mismatch within one pass. It also terminates from each selector state. The cycle lets the common suffix revisit coordinates that were tested in other histories, so a state merged after equal outcomes still handles the entire cross-history product hull. This is a legitimate cyclic rectangle protocol with an explicit strategy and termination bound; it is not an acyclic rect-DAG. If a stricter cyclic model requires every arbitrary feasible-edge walk to terminate, this construction is not a witness for that stronger semantics; termination here is by the specified deterministic local strategy, which immediately outputs whenever the current bits mismatch.

The acyclic boundary matters. Simply cutting the edge `S_N -> S_1` leaves a suffix that can receive a product-hull pair whose only mismatch was at an earlier coordinate; restoring correctness then requires revisiting that coordinate or retaining additional history. This identifies why the cyclic protocol is linear, but does not claim a lower bound on every acyclic unrolling.

### Why this does not produce a small fusion cover

The C-75 q-rule system is not an arbitrary cyclic rectangle protocol. A fusion rule has one unary activation set `X_i` on the truth-table universe, generated by its two endpoint-support unions and predecessor carriers; its promise rectangle is `(Y intersect X_i) x (Z minus X_i)`. A communication rectangle `R=A_i x B_i` can be represented *semantically* by a cut `X=A_i union (Z minus B_i)` on `Y union Z`, but the cyclic protocol charges no cost for this cut or for its local predicates. There is no established construction that realizes all these cuts as legal fusion activation sets using O(N) pair rules. For the universal scan, even the full scan state `Y x Z` corresponds to the cut `X=Y` on the promise, which is exactly the sparse-envelope separator whose circuit/closure cost is unresolved.

Conversely, a successful q-pair fusion cover yields the more constrained ranked cyclic rectangle search graph from C-139/C-210: the rule state is a shared unary closure state, supports come from literal slices or contained predecessor carriers, and every chosen rule transition decreases the low input's activation rank. It has q rule states but up to `O(q^2+qN)` support choices. Those constraints prevent the 5N cyclic scan from being counted as a fusion cover. The q-to-standard-DAG and reverse bounds remain `S_rect=O(q^3/log q)` and `rho_prom=O(S_rect)`; no numeric transfer changes.

**Route disposition.** Any Tier 1-3 lower bound for arbitrary cyclic product-rectangle protocols is impossible: this model has a `5N`-state solver for every disjoint promise. Keep the lower-bound target in standard *acyclic* rect-DAGs or in the native restricted fusion closure. The first missing map is precise: convert free, independent party-local rectangle predicates in a cyclic search graph into one-input least-fixed-point activation sets generated by legal fusion supports, with quantitative control. No such conversion or its impossibility has been proved. This route-kill does not upper-bound `rho_prom`, does not give a near-linear acyclic DAG, and does not resolve P versus NP. It explains why the cyclic rectangle model is a useful countercheck but not the sought non-shareability invariant.

## 139. C-214 - Count the native closure syntax: exponential generic separation

This continues C-213 by asking whether the universal cyclic rectangle scan might imply a small fusion cover. A direct count in the actual least-fixed-point recurrence gives a strong negative answer for arbitrary partitions.

Let \(f:\{0,1\}^N\to\{0,1\}\), \(Y_f=f^{-1}(1)\), and \(Z_f=f^{-1}(0)\). For a q-rule list, each rule's anchor dependence is determined by two seed clauses, each an OR of a subset of the \(2N\) signed literals \([w_k=b]\); two predecessor subsets of \([q]\); and the subset of rules with empty carrier. Thus at most
\[
2^{4Nq+2q^2+q}
\]
Boolean output functions can arise from q-rule closures. This count remains valid with arbitrary semantic endpoints: the recurrence only sees their endpoint-slice signatures and carrier-containment incidence.

On a successful cover of the full partition, the output is 1 on \(Y_f\) and 0 on \(Z_f\), hence is exactly f. Summing the count through \(Q=\lfloor 2^{N/2-1}\rfloor\) gives at most
\[
(Q+1)2^{4NQ+2Q^2+Q}=2^{2^{N-1}+o(2^N)}<2^{2^N}.
\]
Therefore some f has \(q_f>Q=\Omega(2^{N/2})\). Its plain mismatch relation still has C-213's at-most-\(5N\)-state cyclic rectangle protocol. This proves that there is no generic polynomial-overhead conversion from unrestricted cyclic rectangle search to the unary fusion closure.

**Why this does not solve the project.** The count is existential over all Boolean partitions. It does not show that the fixed explicit sparse-envelope promise \(Y=\mathrm{SIZE}(s_1)\), \(Z=\mathrm{SIZE}(s_2)^c\) is one of the hard partitions. Its medium band also lets a separator extend the labels in many ways. An actual-promise transfer needs an encoding forcing every legal separator to expose a closure-hard function, with controlled q loss. No such encoding is known. Keep O-141 active and do not treat this as an OPS or P-vs-NP lower bound. The full relation definitions, model table, quantitative transfers, and proof audit are in [the C-75 shared-DAG continuation](C75_SHARED_DAG_CONTINUATION_2026-09-27.md).
