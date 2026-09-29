# C-305 - Circuit verification as an alternating game exposes the address-memory cost

Date: 28 September 2026  
Classification: **GLOBAL-CONSTRUCTION AUDIT / SCOPED ROUTE FILTER.** The native recurrence has exact reachability-game semantics. A straightforward game for checking a low circuit against every table coordinate needs the gate-address product and already exceeds the near-linear target. This is not a lower bound for arbitrary native covers; it isolates the only compression point, namely address information carried through proof/context supports.

## 1. Native recurrence is a reachability game

For fixed pair list Q and anchor w, write the seed clauses and predecessor sets as

```text
x_i^(t+1) = (A_i(w) OR OR_{j in P_i} x_j^t)
            AND
            (B_i(w) OR OR_{j in R_i} x_j^t).
```

Here each `A_i,B_i` is a disjunction of matching signed truth-table literals. At active state i, the universal player chooses left or right. The existential player then either selects a matching seed literal on that side and wins, or selects one active predecessor and moves there. A predecessor has strictly smaller activation rank. Therefore state i is active by round t exactly when the existential player can force a seed within t moves, for every universal side choice. Conversely, any winning strategy in this finite reachability game can be made positional and terminates within q rank layers. This recovers the least fixed point exactly.

Thus one active state can be viewed as an AND-OR game position, and a successful low-table derivation can be represented by a positional witness choosing one response per state and side. The game graph is fixed by Q; only the seed truth values depend on w.

## 2. Candidate: use a strategy to encode one circuit description

Low-table membership has the shape

```text
exists circuit description d of size <= s1
such that for every address x in {0,1}^n, C_d(x)=w_x.
```

A natural alternating verifier guesses/reuses gate wiring and lets the universal player challenge an address. The same gate choice must be used regardless of which address is challenged; this is the attractive feature of a positional strategy.

For a fixed circuit with s gates, the direct game that evaluates it on all N=2^n addresses uses positions `(gate,address)`. Every transition must preserve the address until a primary-input or output-table check, and the terminal seed must query the particular signed table literal at that address. This construction has `Theta(Ns)` gate-address positions, up to constant factors for polarity and output checks. At the OPS scale `s=s1=N^beta/(c log N)`,

```text
Ns1 = N^(1+beta-o(1)),
```

which is larger than `N^(1+o(1))` for every fixed beta>0. This is an architecture cost for a supplied circuit description, not a full-promise cover upper bound. One fixed Q must accept every low table and reject every high table while selecting one globally consistent circuit description; this construction does not implement that selector. See C-340.

There is a second consistency issue for an *existentially chosen* description. If gate choices are attached to each `(gate,address)` position, they can vary with the challenged address and describe a piecewise circuit rather than one circuit. If all addresses share one gate position, the state no longer records which `w_x` the branch must inspect. The seed clause at one native state is a fixed disjunction of literals; it cannot condition a literal query on an address chosen earlier in a game history.

## 3. Where compacting the product would have to happen

The direct game has two registers: gate identity and table address. A near-linear cover must avoid their Cartesian product. C-281 supplies the one native place where information can survive without a separate state label: an address-dependent partial assignment in a proof or context support. But any context K and replacement proof P at a shared state can be spliced whenever `K union P` is consistent, and the whole resulting cylinder must lie in `SIZE(s2)`.

This gives the concrete global condition for a compressed evaluator:

1. carry the challenged address in proof/context supports while reusing gate states across addresses;
2. keep the chosen circuit wiring coherent across all address branches;
3. prove that every compatible cross-join of address contexts and gate proofs has only `SIZE(s2)` completions.

The last condition is exactly where a locally compact evaluator can fail: independent address branches may select different gate witnesses, and a compatible splice can combine them into a table outside the high-threshold-safe family. C-281's owner mask records which coordinates such a splice assigns to the replacement proof.

## 4. Calibration and disposition

This is a route audit, not an impossibility theorem. The `Ns1` count only applies to the explicit gate-address product evaluator. C-258 proves that equality fingerprints can compress a large repeated-block family to `O(N)` native pairs, so address count or circuit-description entropy alone cannot force the product. C-257 also shows that many safe cross-splices can be protected by a compact global invariant.

The new construction question is narrower and more concrete: can support contexts act as a compact address register while a shared native state fixes the same gate-choice policy for every address, with all cross-context/proof splices remaining in `SIZE(s2)`? A positive construction would be an O-168 candidate; a negative theorem would need a q-sensitive bound on these address-indexed compatibility products, not a lower bound for the explicit product construction. No q improvement, near-linear full-promise cover, or P-vs-NP proof follows here.

### C-306 correction

C-306 rules out the support-only address-register mechanism proposed above. For one fixed table, every matching context and replacement support is a subset of its full literal set, so every such cross-pair is compatible. The recurrence also forgets support contents when it activates a state. Thus supports cannot make a shared state route conditionally on the challenged address. The product-cost audit remains valid, but any surviving compressed evaluator must encode global circuit choice in the fixed state-level activation pattern or use a different semantic mechanism. See `research/C306_SUPPORTS_CANNOT_STORE_CONTROL_STATE_2026-09-28.md`.
