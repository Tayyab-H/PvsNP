# C-293 - Certificate width forces a linear-in-v CohEnc floor

Date: 28 September 2026  
Classification: **PROVED COHENC LOWER BOUND / QUANTITATIVE ROUTE FILTER.** The bound is far below the source decision lower bound and does not yield a superlinear OPS transfer.

## 1. Circuit certificate-width lemma

Use the project's fan-in-two paid-AND convention: the map is an acyclic monotone circuit with `a` binary AND gates; OR gates may have arbitrary fan-in and are not charged in `a`.

**Lemma.** If an output rail is nonzero, it has a positive input certificate of width at most `a+1`.

**Proof.** Choose an input on which the rail is 1 and trace a proof of this value backward through the circuit. At each OR gate, keep one predecessor that is 1; at each AND gate, keep both predecessors. Keep shared gates only once. Contract the selected OR paths. The resulting connected proof DAG has at most `a` AND vertices, each with at most two outgoing edges, and has `L` leaves, each a source variable or constant 1. It has at most `2a` edges. A connected graph on at most `a+L` vertices has at least `a+L-1` edges, so `a+L-1<=2a`, hence `L<=a+1`. Removing constant leaves gives a source-variable certificate of width at most `a+1`. The certificate is the set of source variables at its leaves; setting those variables to 1 forces the output rail to 1. QED.

The proof allows arbitrary fan-out and sharing. Fan-in two is essential: for an unbounded-fan-in AND charged as one gate, one gate can have a certificate of arbitrarily large width.

## 2. Every dual-rail coordinate has a certificate-width tradeoff

Fix one truth-table coordinate `j` of a C-125 ODDFACTOR map. If both rails are nonzero, apply the lemma to obtain certificates `A` for `phi_{j,0}` and `B` for `phi_{j,1}`, each of width at most `a+1`. C-292 says the input graph `A union B` must be ODDFACTOR-YES. It therefore contains an odd-factor subgraph, which has at least `v` edges: every one of the `2v` vertices has positive odd degree in that subgraph, so the degree sum is at least `2v`. Consequently `|A union B|>=v`.

\[
v\le |A\cup B|\le |A|+|B|\le 2(a+1),
\qquad
a\ge \left\lceil\frac v2\right\rceil-1.
\]

More generally, if one selected opposite-rail certificate `A` touches only `r` vertices, every certificate `B` on the other rail must touch all `2v-r` remaining vertices, and therefore

\[
|B|\ge \left\lceil\frac{2v-r}{2}\right\rceil,
\qquad
a\ge \left\lceil\frac{2v-r}{2}\right\rceil-1.
\]

This is a direct cost for a sparse NO decoy certificate: the opposite polarity must supply enough positive evidence to complete a spanning even-component graph.

## 3. General certificate-width form

Let `f` be any monotone source and let `W(f)` be the minimum number of input variables in a positive certificate: setting those variables to 1 forces `f=1` for every setting of the other inputs. Let `L=CycAnd(f)`. For a C-125 map with `N` table coordinates and `a` paid AND gates:

* If some coordinate has both rails nonzero, choose one certificate of width at most `a+1` for each rail. Their union makes both rails true, and monotonicity preserves this on every superset. NO consistency then forces every such superset to be YES. Therefore `W(f)<=2(a+1)`.
* If no coordinate has both rails nonzero, YES coverage fixes one low code `w*`. Conjoining the map's `N` rails for `w*` computes `f` using at most `a+N-1` AND gates, so `L<=a+N-1`.

Combining the cases gives the general bound

\[
a\ge \min\!\left\{\left\lceil\frac{W(f)}2\right\rceil-1,\ L-N+1\right\}.
\]

This separates two possibilities: either a varying polarity requires cross-rail certificates whose union is a positive source certificate, or fixed polarities expose a common low code and yield a direct source separator.

## 4. ODDFACTOR instantiation

For ODDFACTOR on `K_{v,v}`, `W(f)=v`: a perfect matching is a positive certificate with `v` edges, and every positive certificate must contain an odd-factor subgraph, requiring at least `v` edges. C-291 gives `L=CycAnd(ODDFACTOR_v)>N+v` when `v=(log N)^K` for sufficiently large fixed `K`. Thus `L-N+1>v`, and the general bound specializes to

\[
\boxed{\mathrm{CohEnc}_{s_1,s_2}(\mathrm{ODDFACTOR}_v)\ge \left\lceil\frac v2\right\rceil-1}.
\]

## 5. What the bound does and does not close

This proves a positive-AND lower bound on the reconstruction measure, rather than only excluding OR-only maps. It also gives a certificate-level design rule: any encoder below the threshold would need all coordinates to have a fixed polarity, making the source decision cheap; to vary a coordinate, opposite-rail certificates must together contain at least `v` graph edges.

At `v=polylog(N)`, the lower bound is only `polylog(N)`, whereas the source decision lower bound is superpolynomial in `N`. It leaves the decisive interval `v/2 <= CohEnc << CycAnd` open and does not change the actual fusion bound `q=N-o(N)`. The proof charges neither the number of distinct certificate pairs nor their reuse across the `N` output coordinates. That shared-DAG accounting remains the central O-171 task.

The odd-cut characterization and source lower bound used here are in Cavalar et al., [*Monotone Circuit Complexity of Matching*, ECCC TR25-102](https://eccc.weizmann.ac.il/report/2025/102/download); see Theorem 2 and Definition 1.
