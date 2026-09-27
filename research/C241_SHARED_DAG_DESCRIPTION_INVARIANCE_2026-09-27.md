# C-241 — Shared-DAG audit and description-space invariance

Date: 27 September 2026  
Priority: standard acyclic product-rectangle DAG for the C-75 Gap-MCSP mismatch relation.  
Status: exact model reductions and a universal-construction audit; no new lower bound for the actual promise.

## 1. Exact search relation

Let `N=2^n`, `Y=SIZE(s1)`, `Z={0,1}^N \ SIZE(s2)`, and assume `s1<s2`. Alice receives `w in Y`; Bob receives `z in Z`. The plain signed mismatch relation is

```text
Mis(w,z) = {(k,b) : w[k]=b and z[k]=1-b}.
```

It is total on `Y x Z` because `Y` and `Z` are disjoint. Omitting `b` changes the output alphabet by at most a factor of two.

For a proposed fusion list `Q=((E_i,H_i))_(i=1)^q`, put `T_i=E_i intersect H_i`. Its stronger, Q-specific path relation has outputs consisting of a start empty-carrier rule, a sequence of rule/side/support choices, and a final signed mismatch. At rule `i`, Bob chooses a side `S in {E_i,H_i}` not containing `z`. Alice supplies either (a) a seed `L_(w,k) subseteq S`, where `L_(w,k)=Z intersect {z':z'[k]=w[k]}`, or (b) a predecessor `j` with `T_j subseteq S` and activation rank `tau_j(w)<tau_i(w)`. A seed gives `z[k]!=w[k]`; a predecessor continues the path. The rank strictly decreases, so a valid path has at most `q` rule moves. This path relation is total on `Y x Z` exactly when `Q` is a successful cover. A plain mismatch output need not certify a Q-path.

## 2. Keep the resources separate

Write `M2=|SIZE(s2)|` and let `C_sep(Y,Z)` be the minimum fan-in-two Boolean circuit size of any `h` with `h=1` on `Y` and `h=0` on `Z`; its values on the medium band are unrestricted.

| Resource | Bound or exact interpretation |
|---|---|
| Deterministic communication bits for plain mismatch | `O(s1 log(n+s1)+log N)`: Alice sends a circuit description; Bob evaluates it along the truth-table addresses and returns a mismatch. Any protocol needs at least `log2(N-log2 M2)-O(1)` bits by the output-support argument. |
| Protocol-tree vertices | At least `N-log2 M2` output leaves, since all output coordinates together must hit every low/high difference set. Description transmission gives at most `O(N 2^(O(s1 log(n+s1))))` vertices. |
| Acyclic binary rect-DAG vertices | `S_rect(Y,Z)=Theta(C_sep(Y,Z))`, up to fixed basis/input-source conventions. |
| Q-path communication bits / tree vertices | `O(q log(q+N))` bits; direct unrolling has at most `2^(O(q log(q+N)))` vertices. |
| Q-specific cyclic closure | `q` intersection/rule states with least-fixed-point semantics; explicit support incidence is at most `O(q^2+qN)`. This is a loop/closure object, not an acyclic rect-DAG. |

For the first two lower bounds, if a protocol's output coordinates lie in `K`, then for any fixed `w`, all `2^(N-|K|)` tables agreeing with `w` on `K` must be low. Thus `2^(N-|K|)<=M2` and `|K|>=N-log2 M2`. At OPS scales `log M2=o(N)`, giving only a linear-in-`N` output-support bound and an `Omega(log N)` bit bound. It does not give a superlinear state lower bound.

## 3. Exact acyclic-DAG/separator correspondence

The C-75 mismatch relation is the promise restriction of the Karchmer-Wigderson `Bit` relation. The promise version still has the circuit correspondence because a separator may be any extension off `Y union Z`.

* **Separator circuit to rect-DAG:** associate a rectangle to each gate `g` by `A_g x B_g`, where `A_g={w in Y:g(w)=1}` and `B_g={z in Z:g(z)=0}`. AND/OR gates split this product into child rectangles; shared gates remain shared DAG vertices. Signed input literals give valid mismatch leaves. This costs `O(C_sep+N)` under standard input-source conventions.
* **Rect-DAG to separator circuit:** a leaf `(k,b)` is the literal `[x_k=b]`. If a product rectangle is covered by two child rectangles, either one child contains the parent, or the parent row side is contained in both child row sides, or its column side is contained in both child column sides. Copy the containing child's separator, OR the child separators in the row-union/column-intersection case, and AND them in the dual case. Reverse topological induction gives `C_sep=O(S_rect)`.

This is the Boolean DAG/KW correspondence, not a computation of arbitrary state predicates. GGKS's rect-DAG model is the same acyclic product-rectangle resource for search relations. Their lifting theorems apply to specified gadget-composed sources; no answer-preserving reduction from those sources to this MCSP promise is currently established.

Other nearby models have different semantics:

| Model | Exact relationship and quantitative boundary |
|---|---|
| Sokolov Boolean DAG-like KW games | The ordinary mismatch game; its acyclic graph size corresponds to Boolean circuit size. The promise version measures separator size `C_sep`. |
| Sokolov communication PLS games | The standard state graph is acyclic and has a separate communication cost `t` for state membership/successor choice. An `L`-vertex Boolean game gives an `L`-vertex PLS graph with `t<=2` (weighted PLS size `O(L)`); an `L`-vertex, cost-`t` PLS graph converts to a Boolean game of size `O(L 2^(3t))`. |
| GGKS rectangle-DAGs | Same product-rectangle DAG resource. Their theorem gives `rect-DAG(S composed with IND_m^n)=n^(Theta(w(S)))` for the specified large index gadget. To transfer it here requires a size-controlled, answer-preserving map from such a composed search relation into `Mis_(Y,Z)`; no such map is recorded. |
| GGKS triangle/F-DAGs | Richer state family, hence `S_triangle<=S_rect`; a triangle-DAG lower bound would transfer to rect-DAG. C-194 gives a `4N-1`-state triangle protocol for any disjoint mismatch promise, so this richer model cannot yield a superlinear C-75 lower bound. |
| Cavalar–Oliveira cyclic intersection complexity | On the C-75 promise ground set and its semi-filter generators, `rho_prom=D_cap^circ` exactly. This is the native least-fixed-point fusion measure, not ordinary acyclic DAG size. |
| Nakayama–Maruoka loop circuits | Their theorem identifies the approximation distance `rho(f,M(F_max))=Theta(size_loop(f))`. Cavalar–Oliveira adapt the method to the exact set identity `rho_prom=D_cap^circ`. No direct numerical inequality between the original `size_loop` and this promise measure follows without matching their semantics and generators. |
| Amano–Maruoka conjunctive complexity | `C_and(f)` counts AND gates in monotone circuits, with results for quadratic Boolean functions. No C-75 inequality follows: the promise separator is a general Boolean circuit and needs an AND-preserving reduction to the specific monotone function. |

The Q-specific support walk is not a standard Sokolov PLS game: its fixed rule graph may cycle, and termination comes from the Alice-input-dependent rank `tau_i(w)`. Layering by that rank gives `O(q^2)` acyclic state copies, while choosing among up to `q+N` supports takes `t=O(log(q+N))` bits. The generic PLS-to-Boolean conversion then costs at most `O((q^2+N)(q+N)^3)`, worse than the direct rank-layer/support-router compiler `O(q^3/log q)` in the active range. Thus the `q` named closure states form a cyclic ranked system exactly in the native fusion/least-fixed-point model; they are not a `q`-vertex standard rect-DAG or standard PLS.

## 4. Circuit descriptions cannot shrink this DAG measure

Let `D` be any set of circuit descriptions and `G:D -> Y` the truth-table map, assumed onto. Define the description-space relation by

```text
Mis_G(d,z) = Mis(G(d),z).
```

Then

```text
S_rect(Mis_G)=S_rect(Mis_(Y,Z)).
```

**Proof.** Lift every Alice-side set `A subseteq Y` at every table-DAG node to `G^(-1)(A) subseteq D`. All rectangles, transitions, and valid outputs are preserved, so `S_rect(Mis_G)<=S_rect(Mis_(Y,Z))`. Conversely choose one section `sigma:Y->D` with `G(sigma(w))=w`. Restrict each Alice-side node set of a description-DAG to `sigma(Y)`, then identify `sigma(w)` with `w`. The graph, rectangle property, and output validity are preserved, giving the reverse inequality. Collisions among descriptions do not matter.

Thus a DAG that reads a low circuit description directly can be useful only if it already yields a small separator for the truth-table promise. This proves representation invariance; it does **not** prove that the separator is large. Counting descriptions or changing to description-space cannot supply the missing lower bound.

## 5. Strongest direct universal construction tested

The direct separator is

```text
h(w) = OR_(d in D) AND_(k in [N]) [w[k]=G(d)[k]].
```

It accepts exactly the low tables and rejects every high table. With `|D|<=2^(O(s1 log(n+s1)))`, its fan-in-two size is `O(N |D|)`. A universal circuit can evaluate `G(d)[k]`, but it does not remove the outer existential over `d` or the requirement to check all `N` coordinates against the same description.

A more shared, still explicit router stores the restriction profile `w|I` for each dyadic coordinate interval `I`. If `pi_I(Y)=|{w|I:w in Y}|`, its size is `O(sum_I pi_I(Y))`. Since `pi_I(Y)<=min(|Y|,2^|I|)`, this is at most `O(N |Y|/log |Y|+N log N)` for large `|Y|`. C-133 also gives a matching architecture-specific obstruction at a chosen level: for `k=Theta(s1/n)`, every k-bit pattern occurs on each k-coordinate block, forcing at least `(N/k)2^k=2^(Omega(N^beta/n^2))` distinct profile states. Thus the profile router is decisively not near-linear. Neither its upper bound nor this fixed-profile lower bound controls arbitrary adaptive/revisiting DAGs.

The `2N` rectangles

```text
{d:G(d)[k]=b} x {z:z[k]=1-b}
```

cover every promised pair. This proves a small nondeterministic rectangle cover, not a deterministic DAG. A binary rect-DAG must split each intermediate product rectangle into two child rectangles; an arbitrary union of these mismatch rectangles need not remain a rectangle. Likewise, “there is a mismatch in interval I” is a joint predicate, not generally a rectangle. On rows `00,11` and columns `00,11`, the diagonal pairs agree on both positions and the off-diagonal pairs mismatch; merging two histories at the second position introduces a cross-pair with no suffix mismatch. C-217 rules out fixed-order first-mismatch scans with exponentially many states on the OPS promise, but does not rule out general adaptive/revisiting DAGs.

**Answer to the critical description question:** short individual descriptions give a short communication message and a huge direct enumeration tree. In the standard DAG model, the exact section theorem says they provide no representation-based size discount. Whether the actual promise nevertheless has a small separator remains open.

## 6. Tree versus DAG and artificial calibration

With the same vertex-count convention, every protocol tree is a DAG, so `DAGsize<=Treesize`. The proposed separation “small tree by vertices but large shared DAG” is impossible. The meaningful gaps are communication bits versus graph vertices, and formula/tree size versus circuit/DAG size.

For any Boolean `f` on `N` bits, its KW mismatch relation uses only `N` output coordinates and has an `O(N+log N)`-bit protocol (Alice sends her input). Circuit counting gives some `f` with circuit size `Omega(2^N/N)`; Sokolov's DAG/KW theorem transfers this to rect-DAG size. This is a sharp artificial example showing that low communication and a small output alphabet do not imply a small shared DAG. It does not transfer to the structured `SIZE(s1)` versus `SIZE(s2)^c` promise. Parity gives the opposite vertex-count gap: a formula/protocol tree of `Theta(N^2)` can be represented by a shared `O(N)` circuit/DAG.

The C-75-specific candidate invariant remains the product-hull condition: if a state has rectangle `A_v x B_v` and descendant output-coordinate set `K_v`, correctness requires `pi_(K_v)(A_v) intersect pi_(K_v)(B_v)=empty`. This is necessary and exact for that state's output support. C-215/C-216 show why the local exclusions do not add to a global state charge; C-217 covers only fixed-order scanners. No global non-shareability theorem for arbitrary C-75 DAGs follows.

## 7. Transfer chain and active target

The current proved quantitative chain is

```text
rho_prom <= O(S_rect),
S_rect <= O(rho_prom^3/log rho_prom),
D_cap <= rho_prom^2,
rho_prom = D_cap^circ.
```

The reverse map from a rect-DAG to a promise cover is near-lossless. The current general cover-to-standard-DAG compiler pays for rank layering and support routing; its cubic/log loss cannot be suppressed by counting the `q` cyclic activation names as acyclic states. More detailed proved bounds are:

```text
S_rect = O(qN + q^2 + sum_C (r_C e_C + r_C^2))
       = O(qN + q^2 + q d^2),
```

where `r_C` is a rule-SCC size, `e_C` its internal side-support incidence count, and `d=max_C r_C`. This follows after deleting automatic self-supports and evaluating each SCC in at most `r_C` rounds. A carrier-quotient compiler gives `O(qN+e_out+sum_C p_C(e_C+q_C))`, while the escape-normal-form compiler gives `O(qN+(s+1)(xi+kappa+q))`; these can improve special covers but do not bound the worst case. For `d<=sqrt(q)`, the first bound is `O(q^2)` when `q>=N-o(N)`. Thus a separator lower bound above `N^(2+2epsilon)` would force `q>N^(1+epsilon)` **within that sparse-SCC subclass**. No theorem shows every minimum cover lies in that subclass. The best unconditional standard rect-DAG bound remains `O(q^3/log q)`, and a worst-case `O(q polylog N)` compiler is unproved. Consequently, to infer `rho_prom>N^(1+epsilon)` for all covers through the general compiler requires

```text
S_rect > c N^(3+3epsilon)/log N.
```

A direct lower bound on `rho_prom` avoids this loss. An `N^(1+o(1))` separator/DAG would instead imply `rho_prom<=N^(1+o(1))` and defeat this fixed-superlinear fusion target; it would not resolve P versus NP.

Keep the previously proved ceilings as route filters: `rho_w<=N-1`, `rho*=O(N)`, and `rho(H)=O(N log|H|)` for a fixed semi-filter family `H`. They concern one-anchor, universal, or fixed-family settings; none is a universal `O(N)` cap on the adaptive promise measure `rho_prom`.

## 8. Cross-check C-240's empty-root normal form against the compiler

C-240 gives a small but exact refinement for empty-carrier output rules. Let `O` be the output-rule set and let `m` count rules in `O` whose two direct seed vocabularies are both nonempty. For each such rule, C-240 forces complementary literals `a_i=ell_i` and `b_i=not ell_i` on one coordinate. At rank layer `r`, its recurrence simplifies to the selector

```text
x_i[r] = (ell_i AND R_i[r-1]) OR ((NOT ell_i) AND P_i[r-1]),
```

where `P_i` and `R_i` are still the ORs of the legal predecessor states on the two sides. If one seed vocabulary is empty, one predecessor OR remains mandatory. Thus the direct seed-clause construction cost improves from `O(qN)` to `O((q-m)N+m)` for this class of lists. With `E_ext` denoting cross-SCC side-support incidences, the SCC circuit can be bounded by

```text
O((q-m)N + m + E_ext + sum_C (r_C e_C + r_C^2) + q).
```

This is a valid parameter-sensitive improvement when many output rules have complementary singleton seeds and the support graph is sparse. It does not improve the worst-case rank-router loss: C-240 places no bound on `E_ext` or on the dense internal SCC term `sum_C r_C e_C`; the compiler bound still permits cubic cost for a dense q-state SCC, though no such SCC is shown necessary or impossible. So C-240 does not establish an `O(q polylog N)` compiler or a stronger general transfer; it only narrows where seed-vocabulary cost can remain.

**Disposition and tier.** The exact model comparison and representation-invariance result are Tier 4/route-audit progress; they do not provide the requested Tier 1–3 lower bound or a breakthrough. They close the claim that short descriptions alone buy a small shared DAG, but not the C-75 route. The next proof target is an OPS-specific global charge on product-hull-safe residual states strong enough to exceed `N^(3+3epsilon)/log N`, or an explicit near-linear separator for the complete promise. C-240 does give the parameter-sensitive seed-cost refinement above, but no support-incidence bound or worst-case near-lossless compiler. No actual-promise superlinear DAG/cover bound or P-vs-NP proof has been obtained.

## Primary literature checked

- [Sokolov, *Dag-like Communication and Its Applications* (ECCC TR16-202)](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download): Boolean DAG/KW correspondence and related DAG-like games.
- [Garg, Göös, Kamath, and Sokolov, *Monotone Circuit Lower Bounds from Resolution*](https://theoryofcomputing.org/articles/v016a013/v016a013.pdf), Sections 2–3: rect-DAG and triangle-DAG definitions and lifting scope.
- [Cavalar and Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://eccc.weizmann.ac.il/report/2025/033/download), Theorem 30: exact cover/cyclic-intersection characterization and acyclic-unfolding limits.
- [Nakayama and Maruoka, *Loop Circuits and Their Relation to Razborov's Approximation Model*](https://doi.org/10.1006/inco.1995.1083): loop circuits and approximation-model relation.
- [Amano and Maruoka, *The Monotone Circuit Complexity of Quadratic Boolean Functions*](https://doi.org/10.1007/s00453-006-0073-0): conjunctive complexity in a specialized monotone setting.
- [Karchmer and Wigderson, *Monotone Circuits for Connectivity Require Super-Logarithmic Depth*](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/KW88/KW88.pdf): communication-game/circuit framework and formula calibration.

Detailed earlier proofs and route audits: [C-75 continuation](C75_SHARED_DAG_CONTINUATION_2026-09-27.md), [C-220 frontier](C220_SHARED_DAG_FRONTIER_2026-09-27.md), [C-232 same-alphabet calibration](C232_SAME_ALPHABET_DAG_NONSHAREABILITY_CALIBRATION_2026-09-27.md), and [DAG/Fusion bridge](DAG_FUSION_BRIDGE_2026-09-26.md).
