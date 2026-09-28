# C-292 - ODDFACTOR certificate complementarity and the OR-only boundary

Date: 28 September 2026  
Classification: **SCOPED STRUCTURAL LEMMA / ROUTE FILTER.** This does not construct a LowExt encoder or improve the fusion bound.

## 1. Source and C-125 interface

Take ODDFACTOR on the bipartite graph with sides of size `v`, with one monotone output rail pair `(phi_{j,0},phi_{j,1})` per truth-table coordinate. A C-125 map has these two properties:

* for every YES graph `G`, there is a low table `w` such that `e(w)<=phi(G)`;
* for every NO graph `G`, there is a high table `z` such that `phi(G)<=e(z)`.

The second condition implies that both rails at the same coordinate cannot be 1 on a NO graph.

ODDFACTOR is 1 exactly when every connected component, including isolated vertices, has even order. Equivalently, the all-ones vector lies in the GF(2) span of the edge columns `u_i+u_j`; a solution is an edge set with odd degree at every vertex. This is the source's linear-span representation, but the C-125 map must expose a *complete* one-hot table, including the rail for every zero bit.

## 2. Exact odd-cut characterization of positive certificates

For an edge set `H`, regard it as a graph on all `2v` vertices, so isolated vertices count as components. A positive certificate for a monotone rail is an edge set whose presence forces that rail to 1.

Let `D0` be the odd-cut NO family: choose a vertex set `S` of odd size, and include precisely the bipartite edges internal to `S` or internal to its complement. There are no edges crossing the cut. Every graph in this family is ODDFACTOR-NO: if an odd factor existed, the sum of its degrees over `S` would be odd, but every selected edge has either zero or two endpoints in `S`.

The following equivalence is exact:

> `H` is contained in some odd-cut graph if and only if `H` has a connected component of odd order.

If all components of `H` have even order, every union of components has even size, so no odd set `S` can be a union of components; some edge of `H` must cross every proposed odd cut. Conversely, if `C` is an odd-order component, take `S=V(C)`. No edge of `H` crosses from `C` to its complement, so `H` is contained in that odd-cut graph. Thus a certificate edge set is not contained in any odd-cut NO graph precisely when the input graph `H` is ODDFACTOR-YES: all its components have even order, equivalently it contains an odd-factor subgraph.

Now fix coordinate `j`. Let `A` be any positive certificate for rail `phi_{j,0}` and `B` any positive certificate for rail `phi_{j,1}`. The graph with edge set `A union B` activates both rails by monotonicity. C-125 NO consistency therefore forces:

\[
\boxed{A\cup B\text{ is ODDFACTOR-YES, for every opposite-rail certificate pair }(A,B).}
\]

Equivalently, every such union has all components even and contains an odd-factor subgraph. This condition is also sufficient for *NO consistency on all ODDFACTOR-NO inputs*: a NO graph cannot contain an ODDFACTOR-YES subgraph, since ODDFACTOR is upward closed. The condition handles constants by treating a constant-1 rail as having the empty certificate.

This is more informative than checking only one- or two-edge inputs. It says exactly what paired positive evidence must accomplish: their union must be an ODDFACTOR-YES graph, so every source vertex belongs to an even connected component.

## 3. Zero-AND corollary

Suppose the map uses no AND gates, so each rail is a constant or an OR of source-edge variables. Every nonempty positive certificate then has at most one edge. If both rails at coordinate `j` are nonzero, select one certificate from each; their union has at most two edges. For `v>=3`, this edge set has an odd component (in particular, at least one isolated vertex remains), so it is an ODDFACTOR-NO input. This contradicts the certificate-pair condition.

Consequently, at each coordinate exactly one rail is nonzero: at least one must be nonzero because every YES image contains a complete one-hot low code, and both cannot be nonzero by the preceding argument. Let `w*` be the fixed table whose bit is the unique active polarity at each coordinate. Every YES image contains `e(w*)`.

The monotone circuit

\[
h(G)=\bigwedge_{j=1}^{N}\phi_{j,w^*_j}(G)
\]

accepts every YES input. If it accepted a NO input, C-125 would give `e(w*)<=phi(G)<=e(z)` for a high table `z`. Coordinatewise order between complete one-hot codes implies `w*=z`, contradicting that `w*` is low and `z` is high. Thus `h` computes ODDFACTOR with at most `N-1` AND gates.

At `v=(log N)^K` for sufficiently large fixed `K`, C-291 gives `CycAnd(ODDFACTOR_v)>N`; hence no zero-AND OR-rail C-125 map exists at that parameter. The generic OR-only principle was already present in C-125; this corollary checks it against the stronger ODDFACTOR source rather than claiming a new asymptotic lower bound.

## 4. What this says about the span-program proposal

The GF(2) span program gives a sparse odd-factor witness on each YES input, but its coefficient vector is only a support. An availability rail `phi_{e,1}=x_e` with `phi_{e,0}=0` exposes which edges are present; it does not give a complete code. At a coordinate where an available witness omits edge `e`, the required zero rail is blank. A span-program reconstruction that merely chooses coefficients after seeing the graph therefore does not satisfy the YES inequality `e(w)<=phi(G)`.

To expose both values monotonically, positive certificates for the two rails must be paired so their union is an ODDFACTOR-YES graph containing an odd-factor subgraph. A compact construction would need to share the AND work that assembles these spanning even-component certificates across all table coordinates, while also ensuring each NO image has a high completion. The linear algebra alone does not supply this monotone, total-code completion.

This isolates the next proof target: bound or construct the *cross-polarity certificate-pair system* generated by a small shared AND DAG. Counting rail outputs or citing the linear span program is insufficient; the missing object is a compact monotone way to generate complementary certificates whose union closes every vertex into even components.

## 5. Scope and status

This is an exact structural constraint on C-125 rails over ODDFACTOR and a zero-AND route filter. It neither lower-bounds positive-AND CohEnc by a useful amount nor rules out a shared positive-AND construction. The actual fusion lower bound remains `q=N-o(N)`; no superlinear OPS transfer or P-vs-NP proof follows.

Primary source for the odd-cut distribution, the component characterization, and the exponential monotone lower bound: Cavalar et al., [*Monotone Circuit Complexity of Matching*, ECCC TR25-102](https://eccc.weizmann.ac.il/report/2025/102/download), especially Theorem 2 and Definition 1.
