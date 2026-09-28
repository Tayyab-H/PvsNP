# C-308 - Matching approximation charged to paid AND gates

Date: 28 September 2026  
Classification: **PROVED RESOURCE REFINEMENT / STRONGER ODDFACTOR ENCODER LOWER BOUND.** The matching-sunflower approximation can be run on an acyclic monotone DAG with binary AND gates and arbitrary-fan-in, uncharged OR gates. Its error is charged to shared AND nodes, not total gate count or output count. This strengthens the C-301 bound but does not produce a LowExt encoder, a positive decision/reconstruction gap, or a P-vs-NP proof.

## 1. AND-count matching approximation

Work on the bipartite graph with sides of size `v`, edge universe `E(K_(v,v))`, and Cavalar et al.'s distributions `D1` (uniform perfect matching) and `D0` (odd cut). Consider a monotone acyclic multi-output circuit with `A` binary AND gates. OR gates may have arbitrary fan-in and cost zero. Input edge variables are exact singleton matching terms.

Fix an integer `w<v/4` and put

```text
eps_sun = v^(-10w),
r = max_{1<=ell<=2w} O(ell log^2(ell/eps_sun))
  = O(w^3 log^2 v),
q = e*r/v.
```

Assume `r=o(v)`, so `q=o(1)`. Assign one approximating matching-DNF to each paid AND node in topological order. At a binary AND node, take the union of the two input term families after collapsing all OR-only paths, form all unions of one term from each side that are still matchings, and discard nonmatching unions. The resulting terms have width at most `2w`. Repeatedly apply the matching-sunflower plucking rule until there are at most `r^ell` terms of each width `ell`, then delete terms wider than `w`. Handle the empty term as the constant-one DNF and simplify it before each operation; its appearance from a pluck is already charged to that pluck's D0 error.

This operation has no hidden fan-in or output multiplicity. Before plucking, there are at most

```text
M(v,w) = sum_{ell<=2w} binom(v^2,ell) <= v^(6w)
```

distinct possible matching terms, regardless of how many OR inputs or output roots there are. Each pluck reduces the number of terms by at least one. With `eps_sun=v^(-10w)`, the total D0 false-positive probability introduced at one AND node is at most `M*eps_sun <= v^(-4w)` (weakening constants if needed). The sunflower lemma gives the displayed `r` because `log(1/eps_sun)=10w log v`.

On `D0`, dropping nonmatching unions and wide terms only under-approximates the gate; plucking is the only source of a false positive. On `D1`, a true AND has a pair of firing terms whose union must be a matching, so dropping nonmatching unions loses nothing. Plucking only enlarges the DNF. The only `D1` loss comes from deleting a wide term. Since a fixed `ell`-edge matching is contained in a uniform perfect matching with probability at most `(e/v)^ell`, the loss at one node is at most

```text
sum_{ell>w} r^ell (e/v)^ell <= q^(w+1)/(1-q).
```

Induction through the shared DAG and a union bound over its `A` paid nodes give directional errors

```text
Pr_D0[some approximated node is 1 while its exact node is 0]
    <= A*v^(-4w),
Pr_D1[some exact node is 1 while its approximation is 0]
    <= A*q^(w+1)/(1-q).
```

Every pure-OR signal and OR output root is the exact union of its incoming approximants. An AND output root reuses the single approximation already assigned to that shared paid node. Thus the same two error bounds hold simultaneously for any number of output rails; there is no factor for OR gates, OR fan-in, or output roots. The approximant at a paid AND root is itself plucked and `r`-small, which is the form used for the final separator `Q`. This is the directional version needed below. It uses the matching-sunflower lemma and DNF agreement argument of Cavalar et al., but the resource parameter here is the number of paid AND nodes rather than their total bounded-fan-in circuit size. [Primary source](https://eccc.weizmann.ac.il/report/2025/102/revision/1/download)

## 2. Apply it to every ODDFACTOR C-125 map

Let `Phi` be any C-125 map for bipartite `ODDFACTOR_v`, with `N` table coordinates and `a` binary AND gates. Assume for contradiction that

```text
a + N - 1 <= 2^w.
```

The simultaneous approximation above applies to all shared map nodes. Its odd-cut error obeys

```text
delta0 <= 2^w*v^(-4w) = (2/v^4)^w < 2^(-2w),
```

for large `v`, and its matching error is

```text
delta1 <= 2^w*q^(w+1)/(1-q) = o(1).
```

For a table coordinate `j`, suppose the two approximating rails contain terms `A` and `B`, one in each polarity. Their union has at most `2w` edges. On all `2v` vertices it has an isolated vertex when `v>4w`, hence an odd-sized connected component. An odd-cut coloring constant on every component makes both terms fire; exactly half of such component-constant colorings have odd parity. Since the union has at most `2w` edges, this event has `D0`-probability at least `2^(-2w)`. Outside the simultaneous D0 error event, both approximating rails lie below the exact rails, contradicting the one-hot high-completion condition. Since `delta0<2^(-2w)`, no coordinate has terms in both polarities.

At least one polarity occurs at every coordinate: any matching outside the `delta1` exceptional set is a YES input, its C-125 image contains a complete low table, and the `D1` directional guarantee preserves all rails of that table. The unique available polarity at each coordinate therefore forms a table `b`. A good matching's low witness must equal `b`, so `b` belongs to `SIZE(s1)`. The original circuit

```text
Q(G) = AND_{j=1}^N Phi_(j,b_j)(G)
```

rejects every odd-cut NO input: its high completion differs from the low table `b` at some coordinate. It accepts at least `1-delta1` of the perfect-matching distribution.

The circuit `Q` has at most `a+N-1<=2^w` paid AND gates and arbitrary free OR structure. Apply the same approximation theorem directly to `Q`; its matching-DNF is `r`-small and has width at most `w`. Here `r=O(w^3 log^2v)=o(v)`. The DNF agrees with ODDFACTOR on `D0` and on `1-o(1)` of `D1`, hence has total agreement `1-o(1)`. This contradicts Cavalar et al.'s theorem that every `o(v)`-small matching-DNF has agreement at most `1/2+o(1)`.

Consequently, for every width in the stated regime,

```text
a + N - 1 > 2^w.
```

This is a lower bound on the actual paid-AND cost of every valid C-125 encoder, including maps with rails active on NO inputs. It removes the `O((a+N)(v^2+a+N))` bounded-fan-in expansion used in C-301 and its square-root loss.

## 3. Explicit parameter choice

For any fixed `gamma>0`, set

```text
w = floor(v^(1/3) / (log v)^(2/3 + gamma)).
```

Then `r=O(v/(log v)^(3 gamma))=o(v)`, `q=o(1)`, and `w<v/4` for all sufficiently large `v`. Thus

```text
CohEnc_(s1,s2)(ODDFACTOR_v) > 2^w - N + 1.
```

At `v=(log N)^K` for any fixed `K>3`, `w/log N -> infinity`; the lower bound is superpolynomial in `N`. The matching indicator witnesses used in this source window have `O(v log N/log v)` circuit size, which is below `s1=N^beta/(c log N)` for every fixed `beta>0` and sufficiently large `N`.

The width can approach the matching-sunflower threshold from below by taking arbitrarily small fixed `gamma`. This still does not give a positive transfer margin: the argument lower-bounds every encoder on the same matching/odd-cut distribution that yields the source's monotone lower bound. No encoder upper bound below true `CycAnd(ODDFACTOR)` has been found.

## 4. What changed and what did not

**Changed:** the ODDFACTOR encoder lower bound is now charged directly in the number of paid AND gates. For widths `w=v^(1/3)/log^(2/3+gamma)v`, every C-125 map has `a+N-1>2^w`; this is stronger than C-301's `a+N+v^2+1 >= Omega(2^(v^(1/3)/(2 log v)))`.

**Unchanged:** the actual fusion lower bound remains `rho_GapMCSP=N-o(N)`. C-308 does not construct a C-125 map, show `CohEnc << CycAnd`, prove a near-linear full-promise cover, or separate P from NP. The live question becomes more precise: find a source where the *exact* monotone decision cost is much larger than the cost of a one-sided distributional separator plus the witness-reconstruction overhead, and build the corresponding all-input C-125 map.

## 5. Literature basis and scope

Cavalar et al.'s Lemma 2 supplies the matching-sunflower threshold; Lemmas 3 and 4 give gatewise plucking and the agreement cap. Their published theorem states a total circuit-size lower bound. C-308's extension to free unbounded OR fan-in is proved above by treating each paid AND node as one plucked cross-product and bounding the pluck iterations by the finite universe of width-`2w` matching terms. The claim is not that the paper states an AND-count theorem.

## 6. Later sharpening (C-310)

C-310 observes that any matching term of width `ell<v` has exact D0 mass `2^(-ell)`. This lets the final one-sided separator contradiction use term mass directly, rather than requiring the output DNF to be `o(v)`-small and invoking the DNF agreement cap. Consequently one may take `w=Theta(v^(1/3)/log^(2/3)v)` with `r` a sufficiently small constant fraction of `v`, obtaining `a+N-1>exp(Omega(v^(1/3)/log^(2/3)v))`. Use `research/C310_ODD_CUT_TERM_MASS_TIGHTENS_COHENC_2026-09-28.md` for the strongest current ODDFACTOR encoder bound.
