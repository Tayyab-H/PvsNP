# C-319 — Native closure as an alternating cofactor game

Date: 28 September 2026  
Route: Q180 / compatible-box interpolation.  
Classification: **EXACT GAME NORMAL FORM + INVARIANT CEILINGS; NO q IMPROVEMENT.**

## 1. Exact input-labelled state system

Let the high-table universe be `U`, and let a proposed native list be
`(E_i,H_i)`, `i in [q]`, with consequence `T_i=E_i intersect H_i`.
For a table `w`, write

```text
L_(a,b) = U intersect {z : z_a=b}
```

for its signed literal slice. Define the seed clauses

```text
A_i(w) = OR { [w_a=b] : L_(a,b) subseteq E_i },
B_i(w) = OR { [w_a=b] : L_(a,b) subseteq H_i },
```

and the fixed predecessor sets

```text
P_i^E = {j : T_j subseteq E_i},
P_i^H = {j : T_j subseteq H_i}.
```

Starting from `x_i^0(w)=0`, the exact closure recurrence is

```text
x_i^(t+1)(w) =
   ( A_i(w) OR OR_(j in P_i^E) x_j^t(w) )
   AND
   ( B_i(w) OR OR_(j in P_i^H) x_j^t(w) ).
```

The output is `OR_{i:T_i=empty} x_i^q(w)`. The system is monotone, and every strict iteration activates at least one new state, so it reaches its least fixed point in at most q strict rounds. It accepts every low table and rejects every high table exactly when the list is a valid fusion cover.

Each endpoint seed is a consistent disjunction of signed table bits unless the endpoint is all of `U`, in which case its seed is the constant true predicate. Indeed, if both literal slices for one coordinate were contained in a proper endpoint, their union would be all of `U`.

## 2. Alternating reachability interpretation

Regard state `i` as a position at which the universal player selects one of two obligations, `E_i` or `H_i`. After that choice, the existential player either:

1. discharges the obligation using a true seed literal in `A_i(w)` or `B_i(w)`; or
2. moves to a predecessor `j` whose consequence is contained in the selected endpoint.

The least-fixed-point rule means that only strategies whose every branch terminates at a true seed are winning; a cycle by itself does not count as success. The root is chosen existentially among empty-consequence states. Thus q is the number of states in an input-labelled, two-obligation alternating reachability game. The literal clauses may mix addresses from every prefix block.

This is the exact native object behind C-318's cofactor-SIMD picture. The ordinary cofactor circuit computes all prefix restrictions with coordinatewise Boolean gates. The native game instead shares q global states whose clauses may couple all lanes, and whose support interpretation multiplies via compatibility-filtered joins. The fact that both are lane-wide does not make them the same algebra.

## 3. What the ordinary-circuit bridge costs

Unrolling q fixed-point rounds gives an acyclic monotone circuit with at most q AND gates per round, hence at most `q^2` AND gates in total (unbounded OR fan-in is free in this count). This recovers the known safe conversion but loses a square. Therefore an ordinary monotone interpolation lower bound `M` transfers only as `q >= sqrt(M)` through this route. A target `q>N^(1+epsilon)` would require an ordinary lower bound above `N^(2+2epsilon)` for the relevant interpolant.

No direct-sum theorem for independent lanes applies to the q-state game as stated: one state can have seed clauses touching every lane, and one compatible product acts on the whole support vector. C-257's prefix-parity carriers and C-258's repeated-block equality cover are explicit reminders that globally coupled states can protect many splices at linear cost.

## 4. Exact ceiling for box-count and rank potentials

Every output support is a product box over the cofactor lanes. Soundness requires the whole box to lie in `E_s2`; completeness requires these boxes to cover `E_s1`.

Let `B_min` be the minimum number of sound boxes needed to cover `E_s1`. Singleton boxes give the unconditional upper bound

```text
B_min <= |E_s1| = |SIZE(s1)|,
log2(B_min) <= O(s1 log(s1+n)) = N^(beta+o(1)) = o(N).
```

Likewise, the acceptance set of any sound separator is a subset of `SIZE(s2)`, so every ordinary matrix flattening of its 0/1 indicator has rank at most `|SIZE(s2)|`; the logarithm of this rank is also `N^(beta+o(1))=o(N)`. Consequently, a proof that charges q only through the logarithm of a minimum rectangle/box cover, or through the logarithm of acceptance-set rank, cannot even exceed the existing linear q floor. This is a mathematical ceiling on those statistics, not a ceiling on all possible uses of rank or communication complexity.

The product-dimension statistic has a separate ceiling: C-317 constructs a sound box with `Theta(s2 log s2)` free coordinates spread across all `Theta(log N)` lanes, matching the circuit-counting upper bound. Thus box count, log-rank, and free-coordinate entropy are all insufficient on their own.

## 5. Literature boundary

The ensemble-circuit terminology in C-318 is supported by Järvisalo et al.'s work on circuit synthesis for multiple outputs, but that work supplies no asymptotic lower bound for this MCSP promise or for the native game: [Järvisalo et al., *Finding Efficient Circuits for Ensemble Computation*](https://www.cs.helsinki.fi/u/mjarvisa/papers/jarvisalo-kaski-koivisto-korhonen.sat12.pdf).

Proof-complexity interpolation has a nearby language of monotone separators and DAG-like communication protocols. Those theorems require a specified proof system and an interpolation transformation; they do not automatically yield a lower bound on this arbitrary-endpoint closure game. See [Folwarczný, *On Protocols for Monotone Feasible Interpolation*](https://arxiv.org/abs/2201.05662). Austrin–Risse prove SoS refutation-degree bounds for MCSP and monotone-MCSP slice instances, which is a different measure from the game-state count q: [Austrin–Risse, CCC 2023](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2023.31).

## 6. Next attack and limits

The next proof target is a **state-graph invariant**, not an ordinary box statistic: quantify how many different cofactor-description relations one alternating state can safely synchronize across compatible context/proof splices. A candidate must distinguish independent moderate-hard block tuples from repeated/shared-description tuples, while allowing parity and equality synchronization at linear cost. Any proposed statistic must be computable from the q-state transition graph and its signed seed clauses, rather than from endpoint description length (endpoints are arbitrary semantic sets).

The actual bound remains `rho_GapMCSP=N-o(N)`. C-319 proves an exact game normal form and rules out several natural count-only transfers; it proves no q lower bound, near-linear full-promise cover, or P-vs-NP separation.
