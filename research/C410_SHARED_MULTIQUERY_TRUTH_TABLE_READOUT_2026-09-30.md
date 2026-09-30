# C-410 — Shared multi-query truth-table readout

**Status:** proved fan-in-two circuit compiler and corrected OPS resource accounting. This removes a per-address gate charge; it does not prove a separator lower bound or change the P-vs-NP frontier.

## Exact compiler statement

Let `x in {0,1}^N` be a truth table, with `N=2^n`, and let `a_1,...,a_q in {0,1}^n` be outputs of any fan-in-two circuit `A(x)` (the addresses may be arbitrary functions of the entire table, may repeat, and need not retain caller history). There is a fan-in-two DAG which, given `x` and those address wires, outputs all pairs

```text
(a_j, x[a_j]),  j=1,...,q
```

using `O((N+q) log^3(N+q))` additional Boolean gates. In particular, for `q<=N` this is `O(N log^3 N)`, not `O(qN)`. The total is `|A|+O((N+q)log^3(N+q))` if the addresses must first be computed.

This statement charges total gates in an ordinary fan-in-two DAG. It makes no claim about native paid-AND states, OR-rule counts, description bits, or an implementation whose output wires are charged separately as gates.

## Proof

Create `N` table records `(address=i, kind=table, id=0, value=x_i)` and `q` query records `(address=a_j, kind=query, id=j, value=0)`. Sort the `N+q` records by `(address, kind, id)`, with the table kind ordered before the query kind. A bitonic sorting network on the next power of two records uses `O((N+q)log^2(N+q))` compare-exchange operations. A comparator on `O(log(N+q))` key/payload bits has an `O(log(N+q))` fan-in-two implementation, so the first sort costs `O((N+q)log^3(N+q))` gates.

Scan the sorted records from left to right while maintaining one bit `v`: a table record sets `v` to its payload; a query record copies `v`. Each update uses a constant number of gates, so this costs `O(N+q)` gates. Because every table address occurs exactly once and sorts before all queries with that address, each query record now carries the correct `x[a_j]`, including when query addresses repeat.

Sort the records a second time with query records first and ordered by `id`, followed by table records. This costs another `O((N+q)log^3(N+q))` gates. The first `q` output records are now the requested pairs in their original order. Padding records in the sorting networks use a sentinel key and do not affect the scan or outputs. This proves the bound.

For parallel depth, replace the sequential scan by a prefix network on the constant-size state maps `v -> payload` (table record) and `v -> v` (query record); this uses `O((N+q)log(N+q))` additional gates and `O(log(N+q))` depth. With standard comparator circuits the overall depth is `O(log^3(N+q))`. A sequential scan has the same gate count and linear scan depth. These are separate measures.

## OPS application and precise effect

OPS Theorem 1.4 uses `N=2^n`, YES threshold `s1=2^(beta n)/(10n)` in its proof, and NO threshold `s2=2^(beta n)`. Its quantifiers are one fixed `epsilon>0` and every sufficiently small fixed `beta>0`; the theorem states a universal denominator constant `c`, while the proof uses `10`. Under `NP subseteq Circuit[poly]`, OPS Lemma 4.1 constructs an input-dependent anti-checker list of length `t=2^(10 beta n)=N^(10 beta)`, then calls a size-`m^ell` circuit for Succinct-MCSP on the `t` address/label pairs. The paper separately charges `O(tN)` gates to form those pairs by evaluating each variable-address lookup.

For fixed `beta<1/10`, `t<=N`; the compiler above forms all labels and pairs in `O(N log^3 N)` gates, regardless of address dependence or reuse. The formatter term in that conditional proof therefore drops from `O(N^(1+10 beta))` to `O(N polylog N)`. The selector still costs at most `N^(1+k beta)` under the same assumption, and the verifier still costs `(poly(n)N^(10 beta))^ell`. Choosing `beta` sufficiently small relative to the fixed verifier exponent and `k` still gives the published `N^(1+epsilon)` conditional separator. Thus this tightens one resource account but does not strengthen the magnification implication, establish its lower-bound premise, or change any unconditional bound.

The C-410 compiler also covers the final readout even if the anti-checker addresses are generated adaptively and only their final outputs are exposed. It does not compute the addresses or certify that they anti-check every small circuit. In the OPS construction, the address-selection circuit itself and Succinct-MCSP verification remain the costly parts; this compiler only prevents charging each final table lookup as a separate `N`-gate mux.

## Counterconstruction and mechanism audit

The strongest counterconstruction to a per-query charge is the compiler just proved: all `q` reads, including unrelated data-dependent addresses, can be answered together in near-linear total gates by a sort-and-merge circuit. Repeated-block equality, parity, sparse parity-check systems, and simple global block relations are even cheaper examples of shared readout; C-401 and C-408 already give their `O(N)`-gate counterchecks. These refute a generic argument that `q` address/label pairs force `qN` gates. They do not refute the OPS lower-bound program.

The full-address list `a_1,...,a_N=(0,...,N-1)` is an additional calibration: it requires no address-generation gates and the labels are just the input wires, yet its succinct-consistency instance has length `Theta(N log N)`. Under `NP subseteq Circuit[poly]`, the available verifier bound is `(N log N)^ell`, not necessarily near-linear. Thus list generation/readout and checking whether any size-`s` circuit matches are different costs. No lower bound on the second follows from the first.

The other anti-checker branch has a separate established obstruction: the static Anti-Checker Hypothesis from OPS is false by Chen et al., Corollary 61, using their locality theorem for oracle formulas. The existing `New Model.MD` already records that result and the mismatch between its short-set parameters and fixed-`beta` OPS thresholds. C-410 does not re-open that route. The refutation concerns that static family/formula argument; it is not a lower bound against arbitrary ordinary circuits or against the input-dependent OPS anti-checker selector.

## Full-promise upper attempt

Sorting the complete table or batching queries does not decide whether an arbitrary promised YES table has a small circuit. Exact enumeration of all size-`s2` circuits still gives the recorded `O(N*2^(O(N^beta)))` total-gate separator. Distance-to-constant threshold circuits still miss dense low tables such as parity. No near-linear separator for the full promise was constructed in this cycle.

## Strongest proved statement and frontier effect

The new proved statement is the `O((N+q)log^3(N+q))` total-gate compiler for arbitrary multi-query truth-table readout. It is a generic shared-computation upper bound, not a lower-bound mechanism. It tells us that any successful OPS total-gate lower bound cannot charge the list's final label extraction query by query; it must charge the selector computation, Succinct-MCSP consistency test, or a directly proved property of every separator.

**Exact quantitative frontier:** unchanged. Ordinary separators still have `S >= N-O(N^beta log N)-1`, with C-406's additive `E(C)+gamma log_2 N-O(1)` refinement; the OPS `N^(1+epsilon)` premise remains open. Native `rho_GapMCSP >= N-o(N)` is unchanged. No paid-AND, OR, endpoint, wire, description, runtime, or cyclic-closure lower bound follows.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4, Lemma 4.1, and the proof's separate `O(tN)` formatter charge.
- Chen, Hirahara, Oliveira, Pich, Rajgopal, and Santhanam, [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol151-itcs2020/LIPIcs.ITCS.2020.70/LIPIcs.ITCS.2020.70.pdf), Theorem 59 and Corollary 61 refuting the static Anti-Checker Hypothesis.
