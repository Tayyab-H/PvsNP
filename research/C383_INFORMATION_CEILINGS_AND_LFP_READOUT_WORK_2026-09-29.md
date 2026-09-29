# C-383 - Information ceilings sharpen the caller-context target

Date: 29 September 2026  
Route: O-228 audit against the exact C-319 game and the current Gap-MCSP parameters.  
Classification: **EXACT ROUTE FILTER + READOUT-WORK TARGET; NO q IMPROVEMENT.**

## 1. Low-table entropy cannot force a superlinear state count

At the OPS scale, `s1=N^beta/(c*n)` and `N=2^n`. Circuit counting gives

```text
log2 |SIZE(s1)| = O(s1 log(s1+n)) = O(N^beta) = o(N).
```

Suppose a proposed state invariant only assigns a distinct finite profile to each low table. If the profile has `t` bits, injectivity yields

```text
t >= log2 |SIZE(s1)|,
where log2 |SIZE(s1)| = O(N^beta) = o(N).
```

Since `log2 |SIZE(s1)|=o(N)`, this counting method cannot force `t>N` or `q>N`, and the cover need not assign distinct profiles to distinct low tables in the first place. Without a separate lower bound on the required profile length, the count alone may yield less. A residual-count argument must therefore prove more than that different circuit descriptions exist: it must charge the computation needed to produce or use the residuals.

## 2. Policy counts and ordinary communication hit separate ceilings

For a fixed q-state graph, a positional policy chooses at most one action at each of 2q state-side positions. There are at most `2N+q` literal/predecessor actions, plus an unused-position option, so the crude count including a root choice is

```text
q*(2N+q+1)^(2q) = 2^(O(q log N))
```

for polynomial q. This has ample capacity to assign different policies to every low table once q is near N; it gives no superlinear charge.

Likewise, a deterministic communication protocol for an arbitrary relation on two N-bit tables can transmit one table, using N+O(1) bits. For a relation on a single N-bit table split between two parties, the party holding the smaller half can send it using at most N/2+O(1) bits. Thus a proof that lower-bounds q only by ordinary communication bits cannot force q>N. C-375 contains the exact one-table bound and its source/high mismatch application.

## 3. C-319 exposes enough raw bits at linear q; computation is the bottleneck

For fixed Q, collect its 2q seed predicates into

```text
sigma_Q(w) = (A_1(w), B_1(w), ..., A_q(w), B_q(w)) in {0,1}^{2q}.
```

The predecessor graph is fixed, so the least-fixed-point output is a deterministic monotone readout `G_Q(sigma_Q(w))`. This is an exact factorization by induction on the fixed-point rounds. At q=Theta(N), the signature has enough bit capacity to encode an N-bit table, and C-363 exhibits O(N) endpoint-selected features that reveal the full table. Raw seed information therefore does not force q superlinear.

The generic compiler evaluates q rounds and uses q conjunctions per round, hence at most q^2 paid AND gates when unbounded OR fan-in is free. To infer `q>N^(1+epsilon)` through this compiler requires an OPS-specific lower bound above `N^(2+2epsilon)` for the induced readout measure. Ordinary circuit separators give a related hardness-magnification target, but no known result in the reviewed sources supplies this bound for C-319's least-fixed-point graph.

## 4. A raw gate-by-address product count also fails

A q-state recurrence has two predecessor subsets per state, so its fixed adjacency data use at most `2q^2` bits. Each of its 2q seed clauses selects, for every coordinate, absent / positive / negative, giving at most `3^N+1` clauses and `O(N)` description bits per side. Including the at most `2^q` root sets, the number of syntactic systems is bounded by

```text
(3^N+1)^(2q) * 2^(2q^2+q) = 2^(O(qN+q^2)).
```

This is an upper bound on possible recurrences; endpoint containment may restrict which encodings are realizable.

A size-s circuit's full gate-by-address value matrix has `sN` bits. At q=Theta(N), the recurrence's `O(N^2)` static description capacity is already large enough to encode this matrix for every s=o(N), including the OPS low-circuit scale `s1=N^beta/(c*n)`. Therefore the count of `(gate,address)` pairs alone cannot imply q=Omega(sN). The issue is operational: can one fixed transition system use the stored incidence data to verify one selected circuit consistently across all universal address challenges, despite context-free state activation and the endpoint-containment constraints? Any successful address-multiplexing lower bound must prove a semantic access/consistency bottleneck, not merely count the product coordinates.

## 5. What O-228 must prove

“Different caller histories want different residuals” is not yet a lower bound. A C-319 state has one activation predicate of the whole table; history is not an extra input. But one state can be reused by many callers when its computed predicate serves their shared subtask, and a winning policy may vary with the input. Counting callers, policies, profiles, or transcript bits is already below or at the linear information ceiling.

A viable state-sensitive theorem must instead show that the *fixed recurrence* cannot compute the promise separator with q states: either lower-bound the least-fixed-point readout's actual AND/state work above the q^2 transfer threshold, improve the compiler to a loss compatible with existing lower bounds, or prove a direct q-sensitive theorem on the exact OPS promise. The alternative remains a concrete `N^(1+o(1))` full-promise cover. Such a theorem must be induced by arbitrary valid covers; it may not assume extraction of a circuit witness, a gate/address register, or caller history.

## 6. Checkpoint

- Superlinear native q bound: **NO**; remains `q >= N-o(N)`.
- Full-promise near-linear cover: **NO**.
- State-sensitive synchronization theorem for exact C-319: **NO**.
- Positive CohEnc transfer or general reconstruction-to-decision compiler: **NO**.
- P-vs-NP proof: **NO**.

The search target has been refined from residual *count* to residual *computation*. Do not reopen raw entropy, policy counts, or ordinary communication. Keep the overall goal active.

## 7. Literature context

Pauly explicitly posed the monotone-circuit-size cost of least fixed points of reachability graph-game forms as an open question in 2018; this is a model-level warning, not evidence of a C-319 lower bound ([*Parameterized Games and Parameterized Automata*](https://cronfa.swan.ac.uk/Record/cronfa46098/Download/0046098-26112018112133.pdf)). The OPS magnification theorem identifies a superlinear circuit lower bound for Gap-MCSP as a route to `NP` not in `P/poly` ([Oliveira, Pich, and Santhanam](https://www.theoryofcomputing.org/articles/v017a011/)).
