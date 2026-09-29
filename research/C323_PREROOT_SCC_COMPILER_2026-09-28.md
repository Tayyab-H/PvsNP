# C-323 - Root-free SCCs give a parameterized AND-count compiler

Date: 28 September 2026  
Route: C-319 native game; use C-322's exact pre-root reduction to refine the ordinary-circuit compiler.  
Classification: **EXACT PARAMETERIZED COMPILER; NO UNCONDITIONAL q IMPROVEMENT.**

## 1. Setup

Take a valid q-pair separator Q and let `R={r:T_r=empty}` be its m output roots; V is the set of states `[q]` after removing R, with `v=q-m`. On V, use the exact root-deleted recurrence from C-322. Define its directed dependency graph by an edge `j -> i` when `j,i in V` and `T_j` is contained in at least one of `E_i,H_i`. Let its SCCs be `C_1,...,C_c`, with sizes `r_1,...,r_c`; thus `sum_a r_a=v`. Let `A_cap(Q)` denote the least number of AND gates in a monotone separator circuit when arbitrary-fan-in OR gates and signed table literals are free, as in C-307.

## 2. Theorem

The exact Gap-MCSP separator induced by Q has a monotone circuit satisfying

```text
A_cap(Q) <= m + sum_(a=1)^c r_a^2.
```

In particular, if `d=max_a r_a` (and V is nonempty),

```text
A_cap(Q) <= m + d(q-m) <= d q.
```

If V is empty, `A_cap(Q)<=m=q`.

### Proof

By C-322, acceptance is the OR over roots r of the two terminal factors

```text
(A_r OR OR_(j in P_r^E intersect V) y_j*)
AND
(B_r OR OR_(j in P_r^H intersect V) y_j*),
```

where `y*` is the root-free least fixed point. Order the SCCs of the root-free dependency graph topologically so every external predecessor of a component has already been evaluated. For one component C, freeze those external predecessor values and the seed clauses as inputs. The remaining local recurrence has r_C state bits and is monotone. Starting at zero, each strict round activates at least one new state; hence it stabilizes after at most r_C rounds. Each round computes one conjunction per state, so it uses at most r_C paid AND gates; its ORs have arbitrary fan-in and are free in `A_cap`. The component therefore costs at most r_C^2 AND gates. Summing over components computes every y_i*. Each root terminal test contributes at most one additional AND, and the final OR over roots is free. This proves the bound.

## 3. Why deleting roots matters for the SCC compiler

In the full dependency graph, every empty root r is a predecessor of every state, since `T_r=empty` is contained in both endpoints. Thus it has an edge `r -> i` to every state i. If a state i occurs in a finite accepting proof rooted at r, its proof dependencies give a path `i -> ... -> r`; combined with `r -> i`, it lies in r's SCC. All roots mutually reach one another, so the roots and every proof-relevant state are in one SCC of the full graph. A full-graph SCC decomposition therefore cannot expose a small-component structure in a minimal cover: the root's post-acceptance broadcast merges the useful graph.

C-322 removes exactly these post-acceptance dependencies while preserving the separator predicate. The root-free condensation can have several SCCs, and the compiler above charges their squared sizes instead of the square of their total size. This is the new leverage from the root-free form; the graph is not being decomposed before the output semantics are made exact.

## 4. Transfer consequence and boundary

If a family of valid covers has root-free SCC maximum `d=O(polylog N)`, then an ordinary monotone AND-count lower bound `L(N)` on the Gap-MCSP separator gives

```text
q >= L(N)/d.
```

That would be near-lossless up to a polylogarithmic factor and could cross the linear barrier with a sufficiently strong separator lower bound. More generally the exact inequality is `L(N)<=m+sum r_a^2`.

This does **not** prove that minimum covers have small root-free SCCs. In the worst case there is one nonroot SCC of size q-m, giving the previous quadratic scale. No current result controls `d` on the actual promise or gives an AND-count lower bound that depends on the SCC profile. The actual native lower bound remains `N-o(N)`; there is still no near-linear full-promise cover or P-vs-NP proof.

## 5. Hostile calibrations and next obligation

The parity-lock and C-307 LDPC/code-membership calibrations have O(N)-scale monotone separators and O(N)-pair covers; the repeated-equality family has an O(N)-pair cover. These do not test whether OPS root-free SCCs are small; they only rule out interpreting the new compiler as a generic direct-sum theorem.

The live fork is now precise: either prove an OPS-specific upper bound on the root-free SCC profile of some minimum cover (which, together with a strong enough AND-count lower bound, would yield superlinear q), or show that a large root-free SCC itself forces a direct q charge. Do not assume component sparsity, and do not transfer standard branching-program or acyclic-DAG lower bounds without a compiler preserving this SCC parameter.
