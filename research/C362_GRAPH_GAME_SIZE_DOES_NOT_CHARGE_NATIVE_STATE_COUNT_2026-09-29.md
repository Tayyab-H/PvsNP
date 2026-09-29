# C-362 - Graph-game size does not charge the native state count

Date: 29 September 2026  
Route: test whether known reachability graph-game form results give a lower-bound-preserving shortcut for the exact C-319 recurrence.  
Classification: **PARAMETER-MATCHING AUDIT; NO q IMPROVEMENT.**

## 1. Exact graph-game encoding

For a native list with q pairs, the C-319 recurrence has two obligations per state. Build a reachability game with one universal state node i and two existential side nodes iE and iH. At i, the universal player chooses a side. From side iE, the existential player may move to any predecessor j in P_i^E or discharge the obligation by selecting a seed literal in A_i(w); similarly for side iH. A selected literal reaches a winning terminal iff it is true on w. Empty-consequence states are the existential roots. A play that cycles without reaching a true seed loses, exactly matching least-fixed-point semantics.

Each proper endpoint contains at most one polarity of each table coordinate as a full literal slice: if both polarities were contained, their union would be the whole universe. Thus each side node has at most N literal exits and at most q predecessor exits. An all-universe endpoint is represented by a direct winning exit. Counting vertices and explicit arcs, this gives a reachability graph-game form of size

```text
L_Q = O(q(N+q)+N).
```

The O(N) term accounts for shared signed-literal terminals. In the project regime q>=N-o(N), this is O(q^2). This is a faithful graph-game encoding, but its size is not q: each state can have a dense predecessor list and can inspect up to N signed literals on either side.

## 2. Why the literature parameter does not transfer automatically

Pauly defines Boolean functions by reachability graph-game forms and proves monotonicity. Proposition 9 extracts a monotone circuit whose depth is bounded by the graph-game form size, but explicitly notes that the resulting circuit may be much larger and gives no total-size bound. There is also a direct match to Open Question 11.1: replace each table bit by two independent dual-rail inputs u=(w_a, not-w_a), let F_Q(x,u) output the C-319 one-step state update together with u unchanged, and iterate F_Q from x=0. F_Q is monotone and has a fan-in-two circuit of size K=O(q(q+N)+N); the C-319 acceptance predicate is one output of mu_x F_Q, restricted to consistent dual-rail inputs. Iterating the operator for at most q strict state increases gives the generic O(qK) total-gate upper bound, while charging only AND gates and treating wide ORs as free gives the project's q^2 bound. Pauly asks what circuit size is needed for such least-fixed-point functions of a monotone circuit. This is a close model match, not a result specialized to Gap-MCSP or to its endpoint-selected seed map. Open Question 11.2 asks a related nested graph-game version. [Pauly, *Parameterized Games and Parameterized Automata*](https://arxiv.org/abs/1809.03093), Section 3, Proposition 9, and Open Question 11.

Two parameter mismatches block a direct use here:

1. A lower bound in explicit graph-game size L would imply only the corresponding implicit inequality `L <= O(q(N+q))`; with q already at least N-o(N), the linear-state regime permits L=Theta(N^2). It would take an edge-count lower bound above the quadratic scale to force q=omega(N) by this route.
2. A monotone-circuit lower bound for the induced function does not itself lower-bound L unless one has a size-efficient circuit-to-game conversion in the required direction. The cited paper does not provide that conversion for cyclic reachability forms; its depth bound is not a size bound.

There is an additional input-interface issue. The graph-game form sees 2q seed predicates, but in C-319 these are not independent input bits: each is an OR of a fixed set of signed truth-table literals, selected by endpoint containment. A lower bound for arbitrary independent leaf assignments therefore needs a separate transfer to this restricted composed input map.

## 3. Exact lower-bound arithmetic

If a future theorem proves that every explicit reachability graph-game form for the induced table separator needs L(N) vertices-plus-arcs, then the native list obeys

```text
L(N) <= C q(N+q)+C N.
```

Solving this inequality gives a q lower bound, but a merely superlinear graph-game lower bound can be absorbed by the qN term while q is near N. To certify q>=N*g(N) from this parameter alone, one needs a graph-game lower bound that grows past the corresponding `Theta(N^2*g(N)^2)` scale when q dominates N, plus an embedding theorem showing that the hard graph-game function is the actual Gap-MCSP separator induced by signed-literal seeds. No such theorem or embedding is available in the repository or in the targeted literature search.

This does not prove that graph-game methods cannot work. It pinpoints the missing object: a state-count lower bound for reachability forms with large, structured literal exits, or a promise-specific argument that charges endpoint incidence without charging every literal edge separately.

## 4. Decision and status

Do not pursue a generic “graph game is more succinct than a circuit” argument: the known model counts the transition graph, while native q ignores the endpoint-induced arc count, and the circuit extraction has no size guarantee. Pauly's explicit open question confirms this is a real model boundary rather than a missing routine compiler.

This audit supplies no first-superlinear native bound, no full-promise near-linear cover, no positive CohEnc transfer, and no P-vs-NP proof. The actual bound remains `rho_GapMCSP >= N-o(N)`. The main route remains a direct synchronization theorem for the exact q-state recurrence or a full-promise near-linear cover.
