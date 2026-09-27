# C-243 — Carrier volume and proof-cylinder packing

Date: 27 September 2026  
Route: native cyclic fusion closure, continuing O-153/C-242.  
Status: exact state-local capacity theorem; no global q-charge or P-vs-NP result.

## 1. Why add carrier volume to the splice profile

C-242 tracks the seed support of a proof and the Boolean interval of an output splice. That omits an exact intermediate constraint: every proof rooted at a rule state forces its high-side cylinder into that state's fixed carrier. This gives a geometric capacity limit on how many disjoint proof cylinders one state can host. The question is whether these state capacities can be aggregated through predecessor intersections.

Let

```text
U = {0,1}^N minus SIZE(s2),       M2 = |SIZE(s2)|,
T_i = E_i intersect H_i,
Cyl(C) = {x in {0,1}^N : C subset ell(x)}.
```

Here C is a consistent signed-literal support and `dom(C)` is its set of fixed coordinates.

## 2. Certificate-carrier containment

**Lemma.** For every state i and every finite proof support C rooted at i,

```text
U intersect Cyl(C) subseteq T_i.
```

**Proof.** Let z be a high table extending C. At every seed leaf of the proof tree, the selected matching slice contains z and is contained in the relevant endpoint. Induct up the finite proof: if the selected predecessor subproof derives carrier T_j, its endpoint-containment edge puts T_j inside the parent endpoint; if the selected option is a seed, that slice is inside the endpoint. The two side supports therefore place both E_i and H_i in the upward closure generated from z's matching literal slices. The rule derives T_i. Every set in this closure contains z, beginning with the literal slices, so z is in T_i. This proves the inclusion.

The same argument in Boolean language says: if C is a proof support for i and a high input z matches every literal in C, then i is active on z and therefore its carrier contains z.

## 3. Quantitative capacity bound

Write t=|dom(C)|. Its full table cylinder has size `2^(N-t)`, and deleting the M2 non-high tables removes at most M2 points. Therefore

```text
|T_i| >= |U intersect Cyl(C)| >= 2^(N-t) - M2.
```

Equivalently, for every finite proof support C rooted at i,

```text
|dom(C)| >= r_i := N - log2(|T_i| + M2).
```

Since T_i is a subset of U, `r_i >= 0`. For an empty-carrier output state this recovers

```text
|dom(C)| >= N - log2(M2),
```

the known linear certificate floor. For a carrier close to a half-cube, it only forces one or a few fixed coordinates, as expected.

There is also a packing form. Let F be a family of proof supports rooted at i, each fixing at most t coordinates, such that the high-side cylinders `U intersect Cyl(C)` are pairwise disjoint. Then

```text
|F| * (2^(N-t) - M2) <= |T_i|,             when 2^(N-t)>M2.
```

For integer t at or below r_i, whenever the denominator is positive, `2^(N-t)-M2 >= |T_i|`, so at most one such disjoint high cylinder can fit. This caveat matters: once t is above r_i, a cylinder may contain only non-high tables, the high-side lower bound can vanish, and this lemma gives no capacity bound. The exact transition from a high-intersecting proof cylinder to a safe low-only cylinder is therefore part of the remaining problem.

## 4. Contexts make the missing tradeoff explicit

For a reusable state i, every accepting context support K and every proof support C rooted at i produce an output support K union C. Thus

```text
U intersect Cyl(K) intersect Cyl(C) = empty.
```

The positive proof cylinders `U intersect Cyl(C)` lie inside T_i by the lemma. A context is therefore a negative cylinder that avoids the entire state-activation family on U. Yet for the original low anchor w, its selected context and subproof cylinders intersect at w. Each state is serving low tables through a context/subproof intersection while avoiding every high table in that cross-product.

This gives a concrete state profile with three parts:

1. carrier volume `|T_i|`;
2. the overlap/packing geometry of `U intersect Cyl(C)` over all finite proof supports C rooted at i;
3. the context cylinders K that hit the required low anchors but avoid all those high-side proof cylinders.

It refines C-242's interval join relation by adding the intermediate carrier. It does not yet bound q.

## 5. Where a global charge presently breaks

For predecessor states j and k with `T_j subseteq E_i` and `T_k subseteq H_i`,

```text
T_j intersect T_k subseteq T_i.
```

Consequently a parent's carrier can be small only if the relevant predecessor-carrier intersection is small. But the measure of `T_j intersect T_k` is not determined by the individual volumes: the carriers can be strongly correlated, nearly identical, or disjoint. Endpoint sets are arbitrary semantic subsets, so no product-measure or rank-additivity inequality follows from the recurrence alone. Treating `-log |T_i|` as an additive potential would assume the missing independence.

Moreover, C-80/C-160's small covers can have highly correlated intermediate carriers, and C-234's diagonal equality cover safely shares low intervals. Any proposed packing charge must allow these cases at O(N) or O(N log N) size. C-228 also shows that carrier/certificate capacity can coexist with readout hardness caused by an arbitrary chosen positive subset, which is not the actual low-circuit promise.

## 6. Narrow literature check and transfer boundary

Alon and Boppana prove strong monotone circuit lower bounds for clique and, for fixed clique size, give an AND-gate lower bound of order `m^s/(log m)^s`. This is a lower bound for a different explicit monotone function; without a reduction to the actual dual-rail Gap-MCSP separator it does not bound fusion q. Their paper also has a balancing lemma controlling OR gates from AND-gate count, but it does not address cyclic least-fixed-point readout. [Alon–Boppana, *The Monotone Circuit Complexity of Boolean Functions*](https://web.math.princeton.edu/~nalon/PDFS/Publications/The%20monotone%20circuit%20complexity%20of%20Boolean%20functions.pdf).

Austrin–Risse prove SoS degree lower bounds for MCSP and analogous results for minimum monotone circuit size on monotone slice functions. Their theorem concerns a proof system and local substitutions, not the native C-75 closure or an ordinary monotone AND-count lower bound for its promise separator. No transfer is established here. [Austrin–Risse, CCC 2023](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2023.31).

The potential route is now more specific: prove a joint carrier-volume / certificate-overlap / context-blocking inequality that survives arbitrary correlations. A successful inequality must aggregate over the actual low-circuit anchors and beat the known `N-o(N)` fusion floor. No such inequality is proved.

## 7. Status

**Proved:** every proof cylinder at state i is contained in T_i; this gives the carrier-rank lower bound and a packing inequality for disjoint proof cylinders. **Unresolved:** how a q-state grammar distributes low anchors among overlapping proof cylinders and blocking contexts, how these local capacities aggregate across cycles, and whether this yields superlinear q. No near-linear full-promise cover or P-vs-NP proof is obtained.
