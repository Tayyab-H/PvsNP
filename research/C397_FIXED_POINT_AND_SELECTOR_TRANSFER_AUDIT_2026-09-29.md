# C-397 — Fixed-point literature and hard-core-selector transfer audit

Date: 29 September 2026  
Route: continue the C-384 work order after C-396; audit the Reed–Muller localization candidate, then test fixed-point-logic and selector bridges.  
Classification: **PRIOR LEMMA CONFIRMED; NEW ONE-WAY SELECTOR-TO-coNP/poly IMPLICATION; FIXED-POINT LITERATURE ROUTE NOT TRANSFERABLE AS-IS; NO NATIVE q IMPROVEMENT.**

## 1. Status of the narrow-seed localization candidate

The candidate lemma in the continuation brief is already proved as C-387. For every fixed polynomial state exponent `a`, every fixed `epsilon>0`, and the Reed–Muller probe `F=RM(floor(delta n),n)` with `H_2(delta)<beta`, C-387 proves that a valid cover with `q<=N^a` has at least

```text
(1-epsilon)N - h - O(1)
```

distinct global seed slots of width at most `C(a,epsilon,delta) log N`. In particular, at least `N/2-o(N)` slots are logarithmic-width. The width constant depends on the fixed error tolerance; the theorem does not say that one fixed width constant gives `N-o(N)` slots simultaneously for every epsilon.

The proof is a valid double count, not a new claim here: C-370 supplies nearly N certificate clauses with at most `k=O(log N)` true literals at each anchor; the `(D-1)`-wise independent Reed–Muller distribution and a `2r`-moment bound make a globally wide clause sparse with probability at most `N^(-(a+3))`; averaging over anchors bounds the number of narrow global slots from below. See [C-387](</D:/projects/P vs NP/research/C387_RM_GLOBAL_NARROW_SEED_LOCALIZATION_2026-09-29.md>).

Its known limit is decisive for the proposed inference: C-390 constructs an endpoint-realizable `q=O(N log N)` *subpromise* cover where a wide root seed is necessary for low completeness, even though C-387's narrow certificate core exists. Thus localization does not by itself reduce the actual readout to local seeds. The full-promise computational-readout question remains open.

## 2. Exact one-way bridge from a selector to promise-coNP/poly

Use the exact C-388 relation. Let `T=ceil(1.515 s1)`, `L=ceil(c N^beta)`, and let `Q=(x_1,...,x_l)` be a list of `1<=l<=L` addresses. Define

```text
R(f,Q) iff for every Boolean circuit C of size at most T,
             (1/l) * sum_i [ C(x_i) != f(x_i) ] >= 0.259.
```

For malformed encodings of `Q`, define `R` to be false. A bad circuit is a polynomial-length witness to `not R`, and its error on the listed addresses is polynomial-time checkable, so `R` is coNP. C-346 proves that every `CC(f)>s2` table has a valid Q; if `CC(f)<=s1`, the circuit for f itself has zero empirical error, so no valid Q exists.

**Proposition.** Suppose a nonuniform circuit family `S_N` of size `R_N` outputs a list `Q=S_N(f)` on every N-bit table, and outputs an R-valid list on every high table. Then

```text
L_S = { f : R(f,S_N(f)) }
```

is a promise-coNP/poly separator for Gap-MCSP: it accepts all low tables and rejects all high tables. The complement has an NP witness consisting of a size-T circuit with empirical error below `0.259` (or a malformed output); the verifier evaluates `S_N`, checks the encoding and evaluates that circuit on the listed addresses. The selector circuit is the nonuniform advice. Medium tables remain unconstrained.

This is an exact reduction to a coNP verification layer, not by itself a Boolean separator of size `R_N+O(N)`. C-398 sharpens the conditional accounting: the validity predicate uses only `O(N^beta log N)` encoded sample bits, and its labels can be gathered from f in `O(N^(1+beta) log N)` gates. Under a size-`M^d` circuit bound for the one fixed NP language `BAD` (which follows from `NP subseteq P/poly`), sufficiently small beta yields a near-linear-exponent Gap-MCSP separator whenever the selector has a smaller fixed exponent. This remains conditional; no unconditional near-linear decision circuit follows from a selector alone. See [C-398](</D:/projects/P vs NP/research/C398_SELECTOR_TO_DECISION_NEAR_LINEAR_UNDER_NP_POLY_2026-09-29.md>).

The reverse reduction remains absent. A one-bit Gap-MCSP decision circuit does not answer the conditioned prefix-extension questions needed to construct Q; C-391 places those queries in `Sigma_2^P` and records the failure of the empty-prefix decision query to self-reduce. Neither a coNP verifier for a candidate list nor the proposition above yields a q-preserving conversion to arbitrary C-319 covers.

## 3. Why generic fixed-point and Datalog results do not charge q here

C-319 has a precise finite monotone recurrence. For `i in [q]`, with fixed predecessor sets `P_i^E,P_i^H` and input-dependent seed clauses `A_i(w),B_i(w)`,

```text
x_i^(t+1)(w) =
  ( A_i(w) OR OR_{j in P_i^E} x_j^t(w) )
  AND
  ( B_i(w) OR OR_{j in P_i^H} x_j^t(w) ).
```

Starting at zero, at most q strict rounds occur. Direct unrolling gives an ordinary monotone circuit with O(q^2) state-conjunction gates, besides seed evaluation and OR wiring; C-393 gives a sharper compiler only under its escape-source normal form. This is an upper translation. It is not a lower bound on the number of states.

Fixed-point logic and Datalog provide a useful vocabulary for the recurrence, but their known complexity theorems do not automatically lower-bound this parameter. In particular, the Anderson–Dawar characterization links fixed-point logic with counting to **uniform symmetric** circuit families on relational structures. Its symmetry hypothesis is explicit in the result ([Cambridge accepted-paper record](https://www.repository.cam.ac.uk/items/c7c99215-9069-4b5d-b37c-e0772e49024a)). A C-319 list is nonuniform in N, its endpoint-derived seed clauses may distinguish arbitrary truth-table coordinates, and it is not supplied with a symmetric structure interpretation. Semantic invariance of Gap-MCSP under input-variable renaming does not make an arbitrary cover's internal graph symmetric.

For context, the usual orbit symmetrization over the n! permutations of the n input variables makes n! transformed circuit copies. Since `N=2^n`, `n!=N^(Theta(log n))`; this standard construction is far above near-linear size. This only diagnoses the cost of that symmetrization method; it is not a lower bound against more efficient canonicalization. A fixed-vocabulary structure interpretation and a symmetry-preserving reduction with controlled q overhead would be needed before FPC inexpressibility could transfer.

More generally, an evaluation theorem or a lower bound parameterized by formula/program size must be translated to C-319's state-pair count. Here q states can carry `2qN` seed-incidence bits and `Theta(q^2)` predecessor-incidence bits. At q=Theta(N), that static description capacity is already Theta(N^2). A theorem charging total rule/wire count therefore need not give a superlinear q lower bound; a q-preserving lower bound for the exact endpoint-derived recurrence is still needed.

## 4. Checkpoint and next move

| Required front | Result after this audit |
|---|---|
| Native bound | Unchanged: `q>=N-o(N)`; no full-promise `N^(1+o(1))` cover. |
| Hard-core selector | No all-high near-linear selector and no `N^(1+epsilon)` lower bound for every selector. New exact consequence: selector plus coNP verification yields a promise-coNP/poly separator. |
| Native-selector bridge | Still none with near-linear overhead; the one-way coNP/poly implication is not a C-319 reduction. |
| Collectively hard low subclass | None established. |
| Local-seed LFP | Localization is proved, but wide-seed dispensability is false in the C-390 subpromise example; no full-promise readout lower bound. |

The localization claim has already been handled; do not renumber or repeat it. The finite-model-theory analogy is not currently a usable lower-bound route without a q-preserving, symmetry-compatible interpretation. The next useful bridge test is whether the *specific* coNP predicate `not R(f,Q)` has a circuit verifier small enough under a stated assumption to meet a near-linear magnification threshold, or whether a different sample-validity formulation avoids universal circuit search. In parallel, retain the full endpoint-derived LFP as the native target. No P-vs-NP breakthrough is claimed.
