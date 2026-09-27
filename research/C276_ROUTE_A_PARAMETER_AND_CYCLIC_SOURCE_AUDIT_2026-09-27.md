
## C-275 — Sparse-support interpolation strengthens the C-125 map obstruction

**Classification: GLOBAL-STRUCTURAL (necessary condition on transfer maps).**

For every subset `A` of the `N=2^n` truth-table addresses with `k>=2` members, the indicator `1_A` has a fan-in-two Boolean circuit of size `O(k n/log k)`. Partition address bits into blocks of width `floor(log2 k)`, generate all block patterns once per block, AND the block indicators for each address in `A`, and OR the resulting address minterms. Thus if low tables `w,z` differ on at most `k` addresses, `CC(z)<=CC(w)+O(k n/log k+n)`.

In a C-125 map, let `S` be the union of coordinates at which some YES image contains both rails, and let `delta=|S|`. Joining any two YES source inputs shows that every selected low witness has the same bits outside `S`. Fix one such witness `w0`. The predicate

```text
AND_{i notin S} phi_{i,w0[i]}(x)
```

accepts every YES input. If it accepted a NO input, its high completion would agree with `w0` outside `S` and differ only on `S`. When `s1+O(delta n/log delta+n)<=s2`, the interpolation circuit would make that high completion low, impossible. Therefore `CycAnd(f)<=a+N-delta-1` in this range.

For `s1=N^beta/(c0 log N)`, `s2=N^beta`, and fixed `0<beta<1`, choose a sufficiently small `c_beta>0`; every `delta<=c_beta s2` is patchable. Hence any map intended to transfer a source lower bound `L` with `a<L-N^(1+epsilon)` must have `delta>c_beta s2=Omega_beta(N^beta)`. This is a required design feature, not a q bound: it counts the union of conflict coordinates across all YES inputs and permits the conflicts to be distributed sparsely.

Full proof and boundary cases: `research/C275_SPARSE_SUPPORT_INTERPOLATION_STRENGTHENS_MAP_OBSTRUCTION_2026-09-27.md`.

## C-276 — Route A parameter audit and primary-source cycle check

**Classification: CONDITIONAL-TRANSFER.**

For the total monotone source used with C-274/C-275, take `f_v(G)=1` iff the maximum matching size `nu(G)>=v/4` (take v divisible by four). Rao's gap theorem still gives `L(v)>=exp(c sqrt(v))` for every monotone circuit computing this extension: it accepts every perfect matching and rejects every graph with no `v/4`-matching. C-266 transfers this bound to the cyclic AND measure. Under the exact C-125 map conditions, the composition gives

```text
q >= L(v)-a(N).
```

Thus the exact target inequality is `L(v)>N^(1+epsilon)+a(N)`. If `v=ceil(A (ln N)^2)` and `a(N)<=N^eta`, it suffices to choose a fixed margin with `c sqrt(A)>max(1+epsilon,eta)`. If `a=polylog(N)`, only `c sqrt(A)>1+epsilon` is needed. A YES completion circuit of size `poly(v)=polylog(N)` fits `s1=N^beta/(c0 log N)` for every fixed `beta>0` once N is large. The still-missing part is exactly a monotone signed-rail map of AND-cost `a` for which every YES image contains a low one-hot code and every NO image lies below a high one-hot completion. The high-completion inequality is an independent requirement; merely ruling out low witnesses is not a substitute.

Combining the target inequality with C-275 gives a sharper necessary map specification: every successful transfer to `q>N^(1+epsilon)` must have global YES conflict support `delta>c_beta s2`. Below that threshold the common low restriction produces a separator with at most `a+N-delta-1` AND gates, inconsistent with the required saving over `L(v)`. No construction meeting this broad-conflict condition is known.

The cycle comparison was rechecked against the primary papers. Rao's revision-5 proof defines a sparse matching approximant for each gate in a topological induction; at an AND gate it combines the already constructed approximants of the two children and prunes oversized matching terms. This inductive step is not directly defined on feedback. Cavalar–Oliveira's cyclic discrete model instead evaluates an inflationary update from empty sets and proves convergence in at most the number of states; flattening uncharged union paths leaves `q` AND equations over at most `M+q` sources per side. Unrolling `q` rounds costs `O(q^2(M+q))` ordinary fan-in-two monotone gates. Since `M=Theta(v^2)`, an `exp(c sqrt(v))` acyclic lower bound implies `q>=exp(c' sqrt(v))` for some `c'>0`; the polynomial compiler loss does not erase the exponential source bound.

This matches the logic of Nakayama–Maruoka's loop-circuit result: approximation lower bounds need a model explicitly compatible with feedback. Their theorem identifies their generalized approximation distance with loop-circuit size; it does not, by itself, transfer Rao's newer spread-matching approximants to the present cyclic model. The independent clique precedent is different: Cavalar–Oliveira's exact cover/cyclic-intersection characterization imports Karchmer's clique cover lower bound directly. For matching, the current proof-theoretic route is the explicit unrolling above, not an assumed analogy with clique.

**Primary sources:** Rao, [*Monotone Circuit Lower Bounds from Spread Matchings*, ECCC TR26-129 rev. 5](https://eccc.weizmann.ac.il/report/2026/129/revision/5/download), especially Theorem 1 and Section 3.1; Cavalar and Oliveira, [*Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://arxiv.org/abs/2503.14117), Section 2.5 and Theorems 30/35; Nakayama and Maruoka, [*Loop Circuits and Their Relation to Razborov's Approximation Model*](https://doi.org/10.1006/inco.1995.1083).

## Route checkpoint after C-274–C-276

The actual Gap-MCSP fusion bound is unchanged at `q=N-o(N)`. Task 1 is settled at source level by C-266/C-276. Task 2's parameter arithmetic is settled conditionally, but the map construction in A4 remains open; C-275 makes its required global-conflict support explicit. The best Route B object is still the context/proof/blocker compatibility tensor (C-270), which has no charge after the C-258 equality calibration. The expander-overlap family C-272 creates high independent hybrids but no grammar-forced replacement slots. The next useful step is a concrete construction with `delta>c_beta s2` and low AND-cost, or a proof that the full low-circuit witness family forces that cost to be near `L(v)`; if that stalls, continue Route B only by proving an incompatible-wiring synchronization theorem beyond C-258.
