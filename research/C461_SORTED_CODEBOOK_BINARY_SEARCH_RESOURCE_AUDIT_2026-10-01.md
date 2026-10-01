# C-461 — Sorted Low-codebook binary search does not give a small circuit

**Date:** 1 October 2026  
**Question:** Can the exact full-promise separator be improved by sorting all Low truth tables and using binary search?  
**Status:** construction audit; no new upper bound, lower bound, or frontier change.

## 1. The tempting argument

Let `K` be the number of distinct `n`-input truth tables with circuit size at most `s1`. Circuit counting gives

```text
K <= 2^(O(s1 log(n+s1))) = 2^(O(N^beta)).
```

After sorting these `K` strings lexicographically, a RAM algorithm can compare an input table `T` against `O(log K)` pivots. If each comparison scans `N` bits, its sequential running time is `O(N log K)`. Since `log K=O(N^beta)`, this looks like an `O(N^(1+beta))` separator, which would defeat any common fixed-exponent OPS lower bound for sufficiently small beta.

That argument silently gives the circuit a random-access read-only memory containing the sorted list and a sequential program counter. Neither resource is free in an ordinary fan-in-two Boolean circuit. Replacing the ROM by a circuit that generates the pivot from its rank has a further missing step: one needs an efficient unranking map from lexicographic rank to a circuit description for that truth table. Enumerating descriptions is easy; ranking their distinct truth tables is precisely not supplied by that enumeration.

## 2. Correct circuit accounting

There are two direct circuit implementations; neither has `O(N log K)` gates in general.

**Unroll the binary-search tree.** A binary search over `K` candidate keys has `O(K)` pivot nodes. A comparison of the `N` input bits against one hardwired pivot takes `O(N)` fan-in-two gates. Duplicating the comparison circuit for every node therefore costs `O(NK)` gates. The execution path visits only `O(log K)` pivots, but a Boolean circuit is an acyclic computation with no free conditional execution; all branch logic must be represented in its gate graph.

**Select pivots with multiplexers.** At a given search step, the current comparison history determines the next pivot index. Selecting one of `K` hardwired `N`-bit pivot words from that index requires an `N`-bit, `K`-way mux. A binary mux tree uses `Theta(K)` constant-size muxes per output bit, hence `Theta(NK)` gates for one such access in the generic construction. Repeating this over the search steps does not yield the proposed logarithmic gate count. Describing the sorted list as a ROM and charging only the comparisons changes the computational model.

The exact Low-description enumerator already gives a valid `O(NK_desc)`-gate full-promise separator: for each short circuit description, test agreement at all `N` addresses, then OR the equality results. Sorting its distinct outputs and unrolling search has the same `O(NK)` order. A Patricia trie can help when many table prefixes are shared, but its edge labels must still be checked; no compression bound for the actual Low codebook sufficient for a near-linear separator is proved here.

## 3. Description and wire resources

The raw sorted list contains `KN` table bits. Storing candidate circuit descriptions instead takes up to `K*O(s1 log(n+s1))` bits. A standard circuit of `G` gates has only `O(G)` gate input pins and a gate-list description of `O(G log(N+G))` bits. Thus the proposed RAM cannot be inserted into the model as an uncharged oracle: either its data and access structure are built into gates/wires, or the result is a RAM/ROM complexity bound, not an ordinary circuit-size bound. Gate count, wires, description length, and the time to sort/enumerate are distinct measures; a small count of comparisons alone proves no circuit upper bound.

This accounting does **not** prove that every circuit recognizing the Low codebook needs `Omega(NK)` gates. The Low codebook is highly structured, unlike a generic `K`-element subset of `{0,1}^N`; exploiting that structure remains an open route to a better upper bound. The result closes only the claim that sorting plus ordinary binary search already supplies one.

## 4. Promise and counterexample audit

The exact membership predicate for `L_s1` is a valid full-promise separator: it accepts every Low table and rejects every table with complexity greater than `s2`. This cycle is therefore a genuine paired full-promise construction attempt. Its sorted-list implementation has no proved gate advantage over the existing description enumerator.

Parity, repeated-block equality, sparse parity-check systems, and simple global block relations all have linear-size circuits when their relation descriptions are linear. They show that local structure can be shared, but do not make the entire Low-codebook dictionary available by a free lookup. Conversely, the weight-threshold separator for a Hamming-ball promise (C-459) shows that a dictionary's cardinality alone does not imply recognition hardness. Neither side establishes the complexity of the actual Low set.

## 5. Exact frontier

The strongest unconditional ordinary lower bound remains `N-O(N^beta log N)` with C-406's additive logarithmic reconvergence refinement. The exact full-promise upper remains `O(N*2^(O(N^beta)))`; no near-linear full-promise separator was obtained. The OPS common-fixed-`epsilon` lower bound, native `rho>=N-o(N)`, and P-vs-NP remain open. The C-460 first-principles diagnosis stands: progress needs either a proved total-gate charge for every extension or a genuinely compressed, fully charged Low-codebook recognizer.

### Primary source for the target quantifiers

- Oliveira, Pich, Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).
