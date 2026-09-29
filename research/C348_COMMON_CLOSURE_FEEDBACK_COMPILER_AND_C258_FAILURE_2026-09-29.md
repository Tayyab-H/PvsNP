# C-348 - Common-closure feedback gives a refined compiler, but C-258 defeats it as a separator invariant

Date: 29 September 2026  
Route: refine the root-free AND-count compiler by factoring common predecessors before measuring feedback.  
Classification: **EXACT PARAMETERIZED COMPILER + HOSTILE CALIBRATION; LOCAL ONLY, NO q IMPROVEMENT.**

## 1. Factor common-predecessor closure

Delete empty-consequence roots as in C-322 and intrinsic self-loops as in C-324. For each remaining state i, write

```text
C_i = P_i^E intersect P_i^H
E_i' = P_i^E minus C_i
H_i' = P_i^H minus C_i
G_i(x) = (A_i OR OR_(j in E_i') x_j)
         AND (B_i OR OR_(j in H_i') x_j).
```

The recurrence is `F_i(x)=OR_(j in C_i)x_j OR G_i(x)`. Let `cl_C(S)` be the least superset of S closed under the fixed common-predecessor edges `j -> i` for `j in C_i`. Then the exact least fixed point is

```text
mu F = mu (x -> cl_C({i : G_i(x)=1})).
```

This is the common-closure identity from C-325. Common-edge propagation costs only OR wiring; each `G_i` contributes one paid AND gate.

## 2. Closure-expanded dependency graph and compiler bound

Let `Anc_C(i)` contain i and every state whose common-edge path reaches i. Define a directed graph D on root-free states by putting `j -> i` whenever there is a state k such that

```text
k is in Anc_C(i), and j is in E_k' union H_k'.
```

Thus D records every variable that can influence the closed update of an output state. Let F be any feedback vertex set of D, of size k, and let q0 be the number of root-free states. Assume for simplicity that we use the bound globally after root deletion, rather than summing over D components.

**Compiler claim.** The exact separator induced by the native list has a monotone circuit with at most

```text
m + (k+1)*q0
```

AND gates, where m is the number of deleted output roots. Arbitrary-fan-in OR gates and signed table literals are free, as in `A_cap`.

**Proof.** Fix the k feedback-state values y. On the other q0-k states, D is acyclic. Every dependency of a `G_k` term used by an outside-state equation precedes each outside output that receives that term; otherwise D would contain a backward edge and a cycle. Schedule each `G_k` after its outside predecessors are evaluated and before its outside recipients. This evaluates the outside equations uniquely in one topological pass, using at most one AND per `G_k` (at most q0 gates). The resulting outside values define a monotone map `g:{0,1}^k -> {0,1}^k` on the feedback states. One evaluation of g also costs at most q0 AND gates. Iterating g from zero reaches its least fixed point in at most k strict rounds, since each strict round activates a new feedback bit. One final topological pass recovers all outside states at the fixed point. The total is at most `(k+1)q0` AND gates, plus one terminal AND per output root. Fixed points of the full system correspond to fixed points of g together with the uniquely determined outside solution, so this computes the least fixed point, not merely an arbitrary fixed point. □

In particular, an acyclic D gives a linear `m+q0` compiler. This refines C-324's feedback-set parameter because common propagation is first treated as free closure.

## 3. Mandatory C-258 calibration: the graph parameter remains too crude

The repeated-block equality cover C-258 has a linear-size native subcover, and C-326 computes its exact output with `2N-d-1` AND gates by reducing each prefix branch to a prefix product. Yet its closure-expanded graph D still has bidirected adjacent-state pairs on each prefix branch. In the notation of C-326, `G_t` depends on `x_(t-1)` and is propagated by common closure to every shallower prefix. For each adjacent pair `x_j,x_(j+1)` away from the terminal boundary:

- `x_j -> x_(j+1)` is the one-sided dependency used by `G_(j+1)`;
- `x_(j+1) -> x_j` is induced because `G_(j+2)` propagates through common closure to `x_j`.

Each branch therefore contains a path of 2-cycles and needs `Omega(r)` feedback vertices. There are `2d` disjoint value branches with `N=dr`, so `k=Omega(N)` for this cover, while q is `O(N)`. The compiler bound falls back to `O(N^2)` and misses C-326's exact linear simplification.

This is a useful negative calibration: merely factoring common predecessors and counting feedback vertices still fails on a required easy family. C-326 succeeds through a stronger *absorption law*: a predecessor that already forces a shallower prefix makes the longer common-closure route redundant, leaving the prefix-product recurrence. The closure-expanded graph does not see that algebraic dominance.

## 4. Scope and decision

The compiler theorem is exact and can be useful for an instance whose closure-expanded feedback core is small. It does not bound that core for minimum covers of the full OPS promise, and its raw feedback count is large on C-258. It is therefore **LOCAL/STRUCTURAL** and is not the next primary target. Any successor must encode absorption/nested-product structure, not just graph feedback, and must also survive C-257 parity, C-307 local-code covers, C-317 safe cylinders, and C-281 compatible splices.

No breakthrough checkpoint changes: the actual lower bound remains `rho_GapMCSP >= N-o(N)`; no superlinear native bound, full-promise near-linear cover, positive CohEnc transfer, general reconstruction compiler, or P-vs-NP proof was obtained.
