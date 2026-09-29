# C-324 - Feedback-core compiler for the root-free closure game

Date: 28 September 2026  
Route: refine C-323 by separating each root-free SCC into a feedback vertex core and an acyclic remainder.  
Classification: **EXACT PARAMETERIZED COMPILER; NO UNCONDITIONAL q IMPROVEMENT.**

## 1. Setup and theorem

Start with a valid q-pair promise cover and delete its m empty-consequence roots using C-322. Let V be the remaining v=q-m states. Their exact least-fixed-point equations are

```text
x_i = (A_i OR OR_(j in P_i^E) x_j)
      AND (B_i OR OR_(j in P_i^H) x_j).
```

Here A_i and B_i are the signed-literal seed clauses, and the predecessor relations are fixed by endpoint containment. Since T_i=E_i intersect H_i is contained in both endpoints, every state is its own predecessor on both sides. Those self-dependencies can be deleted without changing the least fixed point: with the self terms removed, write the right side as G_i(x); the original right side is exactly x_i OR G_i(x). A vector is a fixed point of the original map iff it is a pre-fixed point of G, and the least fixed points coincide.

Build the loopless root-free dependency graph with edge j->i for distinct states whenever T_j is contained in E_i or H_i. Decompose it into SCCs C. For each C let r_C=|C|, and choose a feedback vertex set F_C of its internal loopless graph, of size k_C. The induced graph on D_C=C\\F_C is acyclic. Let A_cap(Q) be the least number of AND gates in a monotone separator circuit for the active promise, with arbitrary-fan-in OR and signed table literals free, as in C-307.

**Theorem.** The exact separator induced by Q has a monotone circuit satisfying

```text
A_cap(Q) <= m + sum_C [ r_C + k_C (r_C - 1) ].
```

More precisely, for a chosen feedback set F_C, let lambda_C(F_C) be the maximum number of strict iterations of its reduced feedback-core map, starting from zero, over all Boolean assignments to its seed clauses and incoming external-state signals. Then

```text
A_cap(Q) <= m + sum_C [ (r_C-k_C) + lambda_C(F_C) r_C ],
lambda_C(F_C) <= k_C.
```

Thus the second bound implies the first. Minimizing the displayed cost over feedback sets can improve the compiler further.

## 2. Proof, component by component

Process the root-free SCC condensation in topological order. Fix one component C and regard all earlier-component states, together with the seed clauses, as inputs. Write F=F_C, D=D_C, r=|C| and k=|F|.

For any fixed assignment a to the k feedback states, the equations for D have a unique solution h(a): evaluate them in a topological order of the acyclic graph induced by D. Each D state costs one AND gate, so h costs r-k AND gates. Substituting h(a) into the k equations on F gives a monotone map g:{0,1}^k->{0,1}^k; evaluating g together with h costs r AND gates total, one per state in C. All ORs and the external signals are free in this measure.

The least fixed point of the component equations is (a*,h(a*)), where a* is the least fixed point of g. To see this, every fixed point of the full component system must have D-part h(a), by acyclicity, and its F-part must satisfy a=g(a). Conversely, each fixed point a of g extends to the full fixed point (a,h(a)). Monotonicity of h then shows that the least fixed point of g gives the least full fixed point.

Iterate g from a_0=0. Each strict round changes at least one of the k zero bits to one, so after at most k strict rounds a_k is fixed. If lambda is the maximum number of strict rounds for the allowed input signals, lambda iterations compute a_lambda=a*. Each iteration computes h(a_t) and g(a_t), costing r AND gates. Compute h(a*) once more in the acyclic D part, costing r-k gates, so the full component costs at most

```text
lambda*r + (r-k).
```

This proves the refined bound. Since lambda<=k, it is at most `k*r+r-k = r+k(r-1)`. Once every root-free component has been evaluated, each deleted root tests its two terminal factors with one AND gate. The final OR over roots is free, giving the stated total.

The use of a least fixed point is essential in the self-loop deletion step: the algebraic identity `F_i(x)=x_i OR G_i(x)` removes self-support without treating an unsupported cycle as a proof.

## 3. Calibration and exact scope

- A root-free acyclic graph has k_C=0 in every component, hence `A_cap(Q)<=q`. This recovers C-307's direct compiler for an acyclic AND/OR separator.
- A directed-cycle SCC of r states has a one-vertex feedback set, giving at most `2r-1` AND gates, rather than the C-323 `r^2` estimate.
- A large SCC whose cycles all pass through one hub also has k_C=1 and the same linear bound. SCC cardinality alone therefore overstates the cyclic cost.
- In the worst case k_C=r_C-1, the bound is `r_C+(r_C-1)^2`; the quadratic loss remains for dense feedback cores.

The C-257 prefix-parity construction has a root-free dependency graph ordered by its prefix stages, so its explicit SCCs are acyclic. C-258 is a sharper hostile check: within a block/value branch, the nested carriers P_t give dependencies in both directions between adjacent prefix states. Each adjacent pair is a directed 2-cycle, so a feedback vertex set has size at least floor((r-1)/2) on an r-state branch, even though C-258 gives an O(N)-pair cover of its repeated-block subpromise. Thus the new bound can be far from tight on an easy promise; feedback vertex number by itself is not a q-sensitive invariant and cannot be assumed small for useful covers. The C-307 acyclic separator compiler remains an alternative construction, but does not show that the particular native list has a small feedback core. These are route filters, not evidence for an OPS feedback-core bound.

C-281's compatible-context/proof products remain untouched: an acyclic or low-feedback compiler says how cheaply a particular state graph expands into an ordinary separator, but supplies no owner-mask or description-coherence theorem. C-317's entropy ceiling is unchanged. No bound on k_C or lambda_C is known for a minimum cover of the actual Gap-MCSP promise.

## 4. Literature boundary and next obligation

Pauly's *Parameterized Games and Parameterized Automata* proves that reachability graph-game forms define monotone functions and notes that these forms can be more concise than monotone circuits. It explicitly asks what monotone-circuit size is required to extract from a reachability graph-game form (Open Question 11.2). This is the same general conversion gap that prevents treating the native cyclic state count as an acyclic gate count; it cautions against assuming a general near-linear compiler. The present theorem gives a concrete structural parameter, feedback-core size/iteration depth, on which an extraction bound does hold. Primary source: https://arxiv.org/abs/1809.03093 (see also the published EPTCS version, https://doi.org/10.4204/EPTCS.277.3).

The live fork is sharper: for full OPS covers, either find a near-linear construction whose induced separator has a better compiler than this generic feedback-set bound, or prove that any low-state cover exposes feedback dynamics that cannot be compressed. The relevant target is not merely large SCCs; directed cycles/hub SCCs are cheap, while C-258 shows high feedback-set size can coexist with a linear native subcover. Any proposed invariant must explain both cases and preserve C-317 safe cylinders and C-281 compatible joins.

**Status:** exact compiler refinement only. The actual native lower bound remains `q=N-o(N)`. No superlinear full-promise cover bound, near-linear full-promise cover, or P-vs-NP proof follows.
