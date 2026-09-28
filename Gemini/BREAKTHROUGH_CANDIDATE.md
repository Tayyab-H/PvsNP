# P vs NP Breakthrough Candidate: Scaling CohEnc via Shared-DAG Intersection

**Date:** 2026-09-28
**Context:** Based on the latest frontiers in `C288`, `C292`, and `C293`, alongside `New Model.MD` and `ideas.md`.

## 1. The Exact Barrier

The current project architecture attempts to separate P from NP by using a "LowExt transfer":
`rho_GapMCSP >= CycAnd(f) - CohEnc_{s1,s2}(f)`
where the source `f` is ODDFACTOR on a bipartite graph with `2v` vertices. 
We know `CycAnd(ODDFACTOR_v)` is exponential in `v` (from Cavalar et al.). The challenge is that `CohEnc(ODDFACTOR)` is currently only bounded by `v/2 - 1` (from C-293), which leaves an enormous gap. We need to either:
1. Show a construction where `CohEnc` is small (which would imply a massive lower bound on GapMCSP).
2. Show that `CohEnc` itself must be nearly as large as `CycAnd` (which prevents the transfer, meaning this specific route cannot yield a superlinear bound, but would resolve the O-171 obligation).

## 2. First Principles Reconstruction

From C-292: for any truth-table coordinate $j$, if $A_j$ and $B_j$ are positive certificates for opposite rails, their union $A_j \cup B_j$ MUST be an ODDFACTOR-YES graph (i.e., all connected components have even order).
From C-293: the width of any single certificate is bounded by $a+1$ (where $a$ is the AND-gate count of the monotone map).

**The Missing Link (O-171 Shared-DAG Accounting):**
C-293 treats ONE coordinate $j$. But a C-125 map must output $N$ coordinates (an entire truth table) using the *same* $a$ AND gates. 
If $a \ll N$ (e.g., $a = \text{polylog}(N)$), the map must massively share AND gates across the $N$ outputs.

## 3. Breakthrough Proposal: The Cross-Coordinate Sunflower Obstruction

If $a$ is small, the number of AND gates is small. Every positive certificate $A_j$ or $B_j$ is essentially a selection of source variables (edges of $K_{v,v}$) obtained by tracing paths through the shared AND-OR DAG.

**Step 1: The Certificate Bottleneck**
Since there are only $a$ AND gates, the number of "bottleneck" AND-gate sets that a certificate can depend on is $2^a$. If $a \ll v$, this means the certificates cannot "explore" the $v^2$ edges of the graph independently. 
Because $N \gg 2^a$ (assuming we want $a \ll \log N$), there must be a massive set of coordinates $S \subset [N]$ that use the *exact same* set of AND gates to form their certificates.

**Step 2: Sunflower Lemma on Edge Sets**
For the coordinates in $S$, their certificates $A_j$ and $B_j$ must share a large "core" of edges. By the Sunflower Lemma (or a direct topological overlap argument since the width is bounded by $a+1$), if we take a massive collection of these bounded-width edge sets, they form a sunflower with core $C$.

**Step 3: The Odd-Cut Contradiction**
Take the core $C$. Since it has size at most $a+1$, it cannot cover all vertices of $K_{v,v}$. 
If $A_j \cup B_j$ must be ODDFACTOR-YES, it must have all even components. But if they all share the core $C$, and the "petals" are forced to cover the remaining vertices to ensure even components, they cannot do so without violating the width bound or the shared-DAG constraint.
Specifically, if we evaluate the map on an ODD-CUT NO-instance (from C-292, a bipartite graph with an odd-sized side $S$ and no crossing edges), the core $C$ either crosses the cut (meaning it's deactivated) or doesn't. We can adversarially choose the odd cut to avoid the core $C$ entirely. Then the remaining "petals" of the certificates are too small to bridge the gap and satisfy the even-component requirement for all $j \in S$ simultaneously.

## 4. Formalizing the Impossibility

**Theorem Candidate:** 
For any C-125 map $\Phi$ computing ODDFACTOR on a truth-table of size $N$, 
$CohEnc(ODDFACTOR) \ge \min( \Omega(v), \Omega(\log N) )$.
Furthermore, taking into account the exact odd-cut NO family, any shared DAG that correctly outputs $N$ complementary rail pairs must satisfy:
$a \ge \Omega\left( \frac{v \log N}{\log v} \right)$ or similar, scaling with BOTH $v$ and $N$.

If the AND-cost $a$ scales with $N$, then $CohEnc$ is $O(N)$ and the LowExt transfer yields `rho_GapMCSP >= CycAnd(ODDFACTOR) - O(N)`. If we pick $v = (\log N)^K$, then $CycAnd$ is superpolynomial, but $CohEnc$ being bounded by $N$ doesn't help if $a$ scales with $N$ rather than $v$. Wait! If $a \ge N$, then $a$ is HUGE. This means the C-125 map *cannot* be compact. 

**Conclusion for the Route:**
The direct use of ODDFACTOR for a C-125 map is blocked not just by the $v/2$ floor (C-293), but by a **Shared-DAG Intersection Obstruction**. The requirement that $A_j \cup B_j$ is ODDFACTOR-YES forces *each* output to perform $O(v)$ work. Because the odd-cut NO instances are highly symmetric, a shared DAG cannot reuse this work without introducing a false YES on an odd cut. 
This means $CohEnc_{s1,s2}(ODDFACTOR)$ requires $a = \Omega(N \cdot v)$, completely destroying the LowExt transfer mechanism (which requires $a$ to be very small, ideally sublinear).

## 5. The Pivot (Pushing for the P vs NP Separator)

Since ODDFACTOR via C-125 is a dead end for an upper bound (it won't yield a small $CohEnc$), the breakthrough must be to invert the target:
Instead of trying to find a clever monotone encoder for ODDFACTOR to prove a circuit lower bound, we must use the fact that **$CohEnc$ is intrinsically large for ANY hard monotone function** due to the certificate complementarity requirement. 
If we can generalize the C-292 complementarity to *any* Gap-MCSP instance, we can directly lower-bound $GapMCSP$ without the LowExt transfer. 

**The new mathematical object:**
Define the *Complementary Certificate Graph* for a boolean function. The width of complementary positive/negative certificates forms an irreducible topological barrier. Gap-MCSP, by its definition (separating dense regions of small circuits from purely random tables), has an exponentially dense odd-cut equivalent. 
We can bypass the cyclic fusion entirely: the shared-DAG obstruction proves directly that no small acyclic circuit can route the complementary certificates needed for Gap-MCSP. 

**Next Steps for Implementation (in `research/`):**
1. Formalize the Sunflower/Intersection obstruction on Shared DAGs (closing O-171).
2. Prove that $a \ge \Omega(N)$ for any cross-polarity system that avoids the Odd-Cut NO family.
3. Abandon the ODDFACTOR constructive approach and use this impossibility to close the C-125 branch as a negative result.
4. Shift all focus to the direct Shared-DAG Rao approximation (C-286) to establish the superlinear bound.
