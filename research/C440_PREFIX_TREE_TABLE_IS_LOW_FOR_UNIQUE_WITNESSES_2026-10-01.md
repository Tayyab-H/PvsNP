# C-440 - Prefix-tree tables stay Low even when the canonical witness is hard

## Question

Can the Ren-Williams prefix-existence queries be batched by making one truth table whose input is a candidate prefix and whose output says whether that prefix extends to a satisfying assignment? Such a table appears to expose all adaptive prefix answers at once. This cycle gives the candidate its strongest direct test and separates the table's circuit complexity from the cost of generating it from the source input.

The source paper reconstructs a lexicographically first (formally, largest in its proof) satisfying assignment by asking whether a prefix can be extended to a satisfying assignment, then PCP-checks a short circuit encoding such a witness. Each query is promise-smart ([Ren--Williams, ECCC TR26-118, pp. 4--5 and 14--15](https://eccc.weizmann.ac.il/report/2026/118/download)).

## Candidate construction

Let `phi_x` be a satisfiable formula with a canonical witness `w_x in {0,1}^r`. Define a table `T_x` whose coordinates encode all strings `p` of length at most `r`, padded to `N=2^(r+1)` coordinates, by

```text
T_x(p) = 1  iff  some satisfying assignment of phi_x has prefix p.
```

The intended use was to let one OPS separator classify this table, thereby replacing the adaptive sequence of prefix queries with a single instance.

## Proof attempt and decisive counterconstruction

Suppose `phi_x` has exactly one satisfying assignment, namely `w_x`. Then `T_x(p)=1` exactly for the `r+1` prefixes of `w_x` (including the empty prefix). A circuit for the fixed table can hardwire those prefixes:

```text
T_x(z) = OR_{j=0}^r [ z = code(w_x[1..j]) ].
```

With `d=r+1` address bits, each equality test costs `O(d)` fan-in-two AND/OR/NOT gates, and the OR costs `O(r)` more. Hence

```text
CC(T_x) <= O(r^2).
```

For every fixed `beta>0` and every fixed OPS constant `c_0`,

```text
O(r^2) < 2^(beta(r+1))/(c_0(r+1)) = N^beta/(c_0 log_2 N)
```

for all sufficiently large `r`. Thus the prefix-tree table is OPS-YES for **every** unique-witness formula, regardless of the witness bits or the circuit complexity of the function `x -> w_x`. In particular, putting a source output bit in `w_x` does not make this table High when that bit is zero. Hardwiring the fixed witness is legal in the nonuniform circuit-size measure for `T_x`; the cost of finding or emitting that witness belongs to the separate map-generator budget.

This refutes the proposed inference “a difficult canonical witness makes its prefix-extension truth table High.” It is a counterexample to this table encoding, not to all source maps and not to OPS GapMCSP. A source-specific family with many witnesses might have a more complex prefix-extension table, but a lower bound on that table's total circuit size would be a new theorem and does not follow from the near-maximum lower bound for `x -> w_x` alone.

### Stronger control: the encoded-history gadget can be easy on both labels

The unique-witness test might be dismissed because the Ren--Williams history circuit can have many satisfying assignments. The one-query special case of their construction gives a stronger control. Let the machine ask one NP query `phi(z)` and output its answer, with witness `z in {0,1}^s`. Its history is `h=(y,out,z)`, and the history circuit accepts exactly when `y` is the number of queries whose supplied witness satisfies `phi` and `out` is the simulated output.

For the satisfiable query `phi(z)=z_1`, accepted histories are exactly those with `y=out=z_1`; the remaining `s-1` witness bits are free. For an unsatisfiable query, accepted histories are exactly those with `y=out=0`; all witness bits are free. Thus both cases have many satisfying assignments, but the prefix-extension predicate is simple in each case. Encode a prefix by its length and its padded contents using `2L` address bits, where `L=s+2` is the history length. A prefix extends to an accepted history iff its already-specified bits do not conflict with the relevant equality constraints (`y=out=z_1` in the satisfiable example, or `y=out=0` in the unsatisfiable example). Address validity, length decoding, and these constant-many bit comparisons have `O(L^2)` gates. With `N=2^(2L)`, this is below `N^beta/(c_0 log_2 N)` for every fixed beta and sufficiently large L.

So even a multi-witness version of the history prefix table can be Low on both a YES and a NO query. This is an exact counterexample to a generic inference from “many witness prefixes” or witness entropy to High circuit complexity. It is still only a toy one-query source, not the full Ren--Williams hard source; the actual source-specific prefix table remains open.

## Generator accounting and local-verifier alternative

The proof above concerns the output table's ordinary circuit complexity; it does not assert a cheap circuit mapping `x` to all of `T_x`. Computing each coordinate of `T_x` decides a prefix-existence question and may itself require costly existential work. If the proposed multi-output generator uses the source oracle or already knows the source output, its cost cannot be hidden in the reduction.

The direct PCP alternative avoids existentially filling the table: make coordinates represent a proposed witness/circuit and a random verifier string, then put the verifier's local accept/reject bit at each coordinate. This has a small circuit as a function of its address and fixed query parameters on both source outcomes. Whenever its size is below the OPS low cutoff, both outcomes map Low. Listing or generating all entries has its own multi-output gate, output-routing, and construction-time costs, but even a cheap generator would not create the missing High side.

## Hostile controls and paired upper bound

The usual shared-computation controls remain decisive for generic charges: parity is computed with `O(N)` XORs; repeated-block equality compares representatives in `O(N)` gates; a sparse parity-check family with total incidence `L` costs `O(L)` and is `O(N)` when `L=O(N)`; simple copied/complemented or sparse linear block relations are evaluated from shared seeds and relations. These falsify generic incidence and per-block gate charges, but they are not counterexamples to a promise-preserving map.

For comparison, the exact full-promise separator remains Low-description enumeration. For `K=2^(O(N^beta))` descriptions `d` of circuits of size at most `s1`, use `E_d(x)=AND_{i<N}[x_i=C_d(i)]` and `Sep(x)=OR_d E_d(x)`. It handles every Low and High table at `O(NK)=O(N*2^(O(N^beta)))` total gates and wires. The prefix-tree candidate offers no compression of this complete separator; the unique-witness family alone has a constant Low-side label and is only a restricted promise.

## Status and quantitative effect

**Project-proved:** for every fixed unique witness `w` of length `r`, the all-prefixes-of-`w` indicator table has an `O(r^2)` fan-in-two circuit and is OPS-YES at length `N=2^(r+1)` for every fixed `beta>0`, once `r` is sufficiently large.

**Failed mechanism:** canonical-witness hardness does not transfer to circuit hardness of the witness's prefix-tree table. The direct local verifier also fails to supply an outcome-dependent high table. This closes the two obvious “batch the prefix answers” encodings, not a source-specific map with a different hard-table construction.

**Frontier unchanged:** ordinary `N-O(N^beta log N)-1` plus C-406 refinement; OPS `N^(1+epsilon)` remains open with one common epsilon for every sufficiently small fixed beta; exact full-promise upper `O(N*2^(O(N^beta)))`; native `rho>=N-o(N)` separate. No ordinary lower-bound improvement, near-linear separator, or P-vs-NP proof was obtained.
