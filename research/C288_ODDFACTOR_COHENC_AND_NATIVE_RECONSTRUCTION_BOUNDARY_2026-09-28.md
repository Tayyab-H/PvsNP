# C-288 - ODDFACTOR exposes the span/reconstruction gap, but not a C-125 encoder

Date: 28 September 2026  
Classification: **FRAMEWORK / ROUTE-BOUNDARY.**  
Status: precise complexity interface and exact failure of direct availability rails; no LowExt transfer or native span-program bridge.

## 1. ODDFACTOR from the span program

Let the bipartite graph have sides `L,R`, each of size `v`, and `m=v^2` edge variables. Work in `GF(2)^(2v)` with basis vectors `u_x` indexed by vertices. An edge `e=(i,j)` contributes `a_e=u_i+u_j`; the target is `t0=sum_x u_x`. The graph accepts iff `t0` lies in the span of the present-edge vectors. Equivalently, some edge indicator `lambda` supported on present edges satisfies

```text
A_G*lambda = 1 over GF(2),
```

which says every vertex has odd degree in the selected subgraph. This is Babai-Gal-Wigderson's linear-size monotone span program. A solution can be chosen with at most `rank(A_G)<=2v` selected edges by taking a basis subfamily whose span contains the target. On the `m` edge-address positions, its indicator table has circuit size `O(v*log m/log v)=O(v)` by C-275 for growing `v`.

The same paper gives a genuine representation separation: ODDFACTOR on `m` variables has monotone span program size `m` over `GF(2)`, but monotone Boolean circuit size `m^(Omega(log m))`. This separates linear witness-space representation from monotone decision. It is not yet a separation for the C-125 reconstruction measure.

## 2. Define LowExt reconstruction complexity

For a monotone source function `f` and OPS parameters `s1,s2`, define

```text
CohEnc_{s1,s2}(f) = minimum number of AND gates in a monotone acyclic,
                     2N-output map Phi satisfying:
  f(x)=1 => some w in SIZE(s1) has e(w) <= Phi(x),
  f(x)=0 => some z outside SIZE(s2) has Phi(x) <= e(z).
```

Set `CohEnc=+infinity` if no such map exists. The map exposes local information; the existential choice of one globally coherent low table performs reconstruction.

**Transfer theorem.** A `q`-AND cyclic fusion separator composed with a minimizing `Phi` gives a cyclic monotone circuit for `f` with at most `q+a` AND gates. The YES implication follows from `e(w)<=Phi(x)`; the NO implication follows from `Phi(x)<=e(z)` and one-hot incomparability of low and high codes. Therefore

```text
rho_GapMCSP >= CycAnd(f) - CohEnc_{s1,s2}(f).
```

This is a framework theorem. It is useful only after an explicit `CohEnc` upper bound below `CycAnd` is proved.

For comparison, define `SpanRec_K(f)` as the minimum size of a monotone span program over field `K` whose available input-labeled vectors span a target exactly on `f=1` inputs. ODDFACTOR gives `SpanRec_GF(2)=m` and monotone circuit complexity `m^(Omega(log m))`. No implication `CohEnc<=O(SpanRec)` is known.

## 3. Direct share-availability rails fail exactly

For each edge `e`, set

```text
Phi_{e,1}(G)=1 iff some solution has lambda_e=1,
Phi_{e,0}(G)=1 iff some solution has lambda_e=0.
```

On a YES graph, any one solution `lambda` gives `e(lambda)<=Phi(G)`. On a NO graph there is no solution, so all rails vanish. Since `t0!=0`,

```text
ODDFACTOR(G) = OR_e Phi_{e,1}(G).
```

If the rail predicates have AND-cost `a`, their OR decides ODDFACTOR with the same AND-cost, so `a>=CycAnd(ODDFACTOR)`. This is C-278's fixed-NO-scaffold extraction and leaves no transfer margin. Existential reconstruction by itself is not enough: if all NO rails vanish, exposing primal solution bits directly reveals the hard decision.

The simpler availability map `Phi_{e,1}=x_e`, `Phi_{e,0}=1` lets every supported subset be completed, including the all-zero table, on every input. It fails the NO side. Putting both polarities on each present edge instead creates conflicts on NO inputs.

## 4. Primal/dual idea and barrier

A NO graph has a dual separator `y` with `A_G^T y=0` and `y dot t0=1`; graphically this is an odd-cardinality union of components with no crossing edge. A potential two-sided encoding would expose a low primal `lambda` code on YES and a high dual `y` code on NO. But the dual condition asks that every present edge have equal endpoint labels, and the primal condition asks for `A_G*lambda=1`.

C-125 rails are monotone functions of edge availability and expose only signed individual table bits. They cannot directly test `lambda_e=0` on absent edges, enforce the global parity equation, or select one odd component. Even if one chosen dual code is compatible with a NO input, every low truth-table circuit consistent with the partial rails must be excluded; the existential domain is all of `SIZE(s1)`, not the intended span-program witness family. A fixed baseline or NO-vanishing dual rails are blocked by C-278. No construction with varying monotone NO decoys, high completions, and useful AND cost is known. This is a route boundary, not an impossibility theorem for ODDFACTOR encoders.

## 5. Native C-281 bridge and reversed span-program attack

C-281's native grammar uses compatible partial assignments: addition is idempotent union/minimization; multiplication is compatible union, with conflicts sent to bottom. It is not a `GF(2)` algebra: there are no additive inverses, and a signed-literal conflict is not linear dependence. A conversion

```text
q-state compatible-support grammar -> small span program
```

would need a semantics-preserving valuation mapping proof choice and compatible join to field operations, retaining shared states and the soundness condition that every completion cylinder lies in `SIZE(s2)`. No such valuation is defined. The parity-lock and C-258 equality-fingerprint covers remain required counterchecks.

There is a reverse candidate: Babai-Gal-Wigderson prove superpolynomial monotone span-program lower bounds for CLIQUE and explicit hard access structures. If a `q`-state owner-mask grammar implied an `O(q polylog N)` span program for its full low/high coherence predicate, these bounds might help. The required reduction from the partial Gap-MCSP owner-mask relation to such a hard access structure, preserving OPS quantifiers and near-lossless parameters, is missing.

## 6. Checkpoint and next mechanism

After C-286 through C-288, the actual bound remains `q=N-o(N)`. No useful C-125 encoder, native q-sensitive algebraic theorem, or `N^(1+o(1))` full-promise cover has been obtained. The clique source is closed for C-125 by C-287; matching fails the canonical-table criterion at small `beta` for direct witness coding. ODDFACTOR supplies a known span-program/monotone-circuit separation, but no `CohEnc` separation.

Do not sharpen spread thresholds or count more witness coordinates. The next Route A question is whether a **two-sided monotone code for primal/dual witness pairs** can let every YES have a low completion while every NO image excludes all of `SIZE(s1)` and still has a high completion. If not, seek a theorem that any such `CohEnc` map for a linear span program yields a monotone decision circuit with comparable AND-cost. In parallel, resume the full-promise cover as the explicit falsification branch.

Primary source: Babai, Gal, Wigderson, [*Superpolynomial Lower Bounds for Monotone Span Programs*](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/GAL/SPAN/COMBINATORICA/final.pdf), Theorem 1.1 and Section 2.1 (ODDFACTOR span program and monotone-circuit lower bound); Corollary 1.4 gives hard monotone span programs for CLIQUE.

## 7. Later source-strength correction (C-291)

The monotone-decision bound above is superseded quantitatively. Cavalar, Göös, Riazanov, Sofronova, and Sokolov prove `Match_v >= 2^(v^(1/3-o(1)))` and transfer the same approximation argument to ODDFACTOR on the odd-cut distribution, stating the latter as `2^(v^Omega(1))`. ODDFACTOR also lies in deterministic logspace and retains the linear GF(2) span program. The cyclic unrolling in C-266 transfers this to `CycAnd(ODDFACTOR_v)>=2^(v^Omega(1))`.

This makes the conditional source window substantially stronger: with `v=(log N)^K` and K sufficiently large, the cyclic lower bound dominates every fixed polynomial in N, while an odd-factor witness table supported on at most `2v` graph edges has `polylog(N)` circuit size. The unresolved C-125 map is still the bottleneck.

The direct proposal to append explicit dual-witness bits has an additional failure: if YES inputs use the all-ones auxiliary dual-rail vector and NO inputs use consistent one-hot vectors, `AND` of all auxiliary rails separates the promise in `2r-1` gates (or `2N-1` for an N-coordinate rail block), independently of ODDFACTOR. A high-table hash of the supplied witness does not repair this source-side shortcut. Any auxiliary witness system must itself retain hard monotone separation.

Full update and parameter calculation: `research/C291_ODDFACTOR_EXPONENTIAL_SOURCE_AND_WITNESS_SIDECAR_NO_GO_2026-09-28.md`.
