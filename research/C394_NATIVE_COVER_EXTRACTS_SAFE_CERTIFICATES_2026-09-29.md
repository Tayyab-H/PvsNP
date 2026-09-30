# C-394 - Monotone signature cones give canonical safe certificates

Date: 29 September 2026  
Route: identify the certificate-independent safe completion set supplied by the C-319 seed signature, and audit what proof-DAG extraction adds.  
Classification: **EXACT SAFE-CONE COROLLARY OF C-385 PLUS PROOF-DAG EXTRACTION; NO NEW q LOWER BOUND OR SELECTOR/NATIVE SIZE BRIDGE.**

## 1. Canonical certificate from the full seed signature

Fix a valid q-rule C-319 cover Q with its 2q seed clauses C_1,...,C_(2q). Write

```text
sigma_Q(w) = (C_1(w), ..., C_(2q)(w)) in {0,1}^(2q).
Accept_Q(w) = G_Q(sigma_Q(w)),
```

where G_Q is the monotone least-fixed-point readout. For an accepted low table f, let

```text
Gamma_sig(Q,f) = { C_j : C_j(f)=1 }.
```

If g satisfies every clause in Gamma_sig(Q,f), then sigma_Q(f) <= sigma_Q(g) coordinatewise: every 1-coordinate of sigma_Q(f) remains 1, while coordinates that were 0 may change either way. Monotonicity gives

```text
Accept_Q(f)=1 and sigma_Q(f)<=sigma_Q(g)  =>  Accept_Q(g)=1.
```

Soundness therefore implies

```text
Models(Gamma_sig(Q,f)) subseteq SIZE(s2).
```

Thus the row of the anchor-by-seed-clause truth-incidence matrix is itself a canonical safe certificate. It has at most 2q clauses and is computed simply by evaluating the bank of seed clauses, in O(qN) gates for clauses of at most N literals. This is the concrete completion cone

```text
U_Q(f) = {g : sigma_Q(f) <= sigma_Q(g)} subseteq SIZE(s2).
```

This is exactly C-385's monotone-order condition in certificate form, not a new theorem. In particular, it corrects the initial C-394 framing: raw incidence is not missing the safety property; monotone readout already makes the full-signature row safe. C-368's safe-CNF model-count lemma gives at least `N-log2|SIZE(s2)|=N-o(N)` distinct true clauses in this row. Since there are 2q seed clauses, this implies only `q >= (N-o(N))/2`, weaker than the project's existing `q >= N-o(N)` bound.

For any high table h, no accepted low signature can lie coordinatewise below sigma_Q(h), since monotonicity would force Q to accept h. This is again the C-385 order obstruction. The abstract signed-singleton bank uses 2N features to make every table signature incomparable in the required direction; its cones can be singletons. Hence signature cones, row counts, and certificate incidence alone still have a linear ceiling.

## 2. Optional smaller certificate from an accepting proof

Fix a valid q-rule C-319 cover Q and a low table f that it accepts. Each state i has two seed tests, denoted `a_i(f), b_i(f)`, and two predecessor sets. Let `tau_i` be the first least-fixed-point round at which state i activates; inactive states have rank infinity. Choose the least-index output root r with finite rank.

For each active state i and each side, choose a deterministic witness to that side's first activation:

- if its seed test is true on f, choose that seed clause;
- otherwise choose the least predecessor j on that side with `tau_j < tau_i`.

Such a predecessor exists: at the first activation round of i, both factors of the recurrence were true using either a true seed or a predecessor active at an earlier round. The selected predecessor edges strictly decrease tau, so the chosen support is an acyclic finite proof DAG rooted at r. Let `Gamma_Q(f)` be the set of distinct seed clauses selected at its leaves. Then `|Gamma_Q(f)|<=2q`, every clause in Gamma is true on f, and every table g satisfying all clauses in Gamma reproduces the same proof DAG. Thus Q accepts g. By soundness, every such g lies in `SIZE(s2)`:

```text
Models(Gamma_Q(f)) subseteq SIZE(s2).
```

The tie-breaking makes `Gamma_Q(f)` a total deterministic multi-output function: return a default code if Q rejects f. A direct circuit evaluates 2q seed clauses in O(qN) gates, unrolls q least-fixed-point rounds in O(q^2) gates, records first-activation ranks, and follows the selected witnesses in O(q^2) further gates. Therefore the certificate selector has size O(qN+q^2). For q>=N-o(N), this is O(q^2); it is not a near-linear certificate selector.

This is a stronger incidence object than an arbitrarily chosen certificate per anchor: the certificate is selected canonically by the actual cover's transition graph. It still does not lower-bound Q, because no complexity lower bound for this multi-output function is known.

## 3. Exact safety quantifiers

For a fixed clause set Gamma true on f, define

```text
Safe(Gamma) iff for every N-bit table g,
                 (g satisfies every clause in Gamma)
                 implies (there exists a circuit D of size at most s2
                          whose truth table is g).
```

For an explicit circuit description D, the condition `TT(D)=g` is polynomial-time checkable in N: evaluate D on all N addresses. Consequently `Safe(Gamma)` has the form `forall g exists D: P(Gamma,g,D)`, hence belongs to `Pi_2^P` under the usual circuit encoding. The certificate extracted above is *known to be safe* because Q is globally valid; this argument does not give a cheap verifier for safety on an arbitrary proposed Gamma.

Let `B_Q` be Q's bank of 2q seed clauses. The relation

```text
exists Gamma subseteq B_Q:
    f satisfies Gamma and Safe(Gamma)
```

is true on every low table for a valid cover: `Gamma_Q(f)` witnesses it. It is false on every high table for any clause bank, since if all clauses in Gamma are true on high f, then f itself is a model of Gamma and violates safety. Thus safe-certificate existence is a promise separator, but the direct relation has a `Sigma_3^P` quantifier description. Q's LFP supplies a structured witness selector on low inputs without separately evaluating the universal-completion predicate.

## 4. What certificate incidence can and cannot establish

In the abstract universal signed-singleton bank, for every table f choose the N clauses fixing each coordinate to its value in f. Their conjunction has the unique model f. It is safe exactly when `CC(f)<=s2`. Hence every low input has an N-clause certificate with one true literal per clause; every high input has no safe certificate containing it. This shows that large certificate size, full transversal number, and row/column counts alone do not force superlinear q. A 2N feature bank can write the certificates; the unresolved work is realizing an efficient, sound monotone least-fixed-point readout for the actual promise.

There is an additional lower-bound warning: if a proposed selector is required to output a safe certificate only on low inputs and may do anything on high inputs, the universal singleton bank gives the map `f -> Gamma_f` by copying the N input bits, with O(N) circuit size. Thus lower-bounding the *partial certificate output map* cannot by itself prove q is large. A useful target must include the decision behavior that withholds acceptance on high inputs, or otherwise charge the cost of certifying that the chosen cylinder is safe.

This singleton construction is a calibration in the abstract clause bank, not a claim that an arbitrary valid C-319 cover contains those clauses or realizes the selector. C-258 equality remains the required native linear-cost hostile example.

## 5. What the incidence pivot now requires

The full truth-incidence matrix `M[f,j]=1 iff C_j(f)=1` already gives a canonical safe cone on every accepted low row. Its output map is just seed-clause evaluation, with O(qN) gates; therefore lower-bounding this partial certificate-output map alone cannot prove q is large. The graph-specific proof-DAG map may output a smaller support, but any useful complexity claim must include the readout's accept/reject behavior rather than only its output on lows.

The surviving target is a q-sensitive lower bound for the endpoint-constrained LFP decoder on the complete low/high promise, or a valid near-linear full-promise construction. Any lower-bound argument must handle multiple proof choices and preserve the C-258 equality calibration. The certificate view identifies the exact safe cones but is not an independent source of hardness.

**Status:** the full-signature safe-cone fact is a direct C-385 corollary; the proof-DAG extraction supplies an optional smaller certificate and the quantifier audit explains why detached safety verification is hard. Neither gives a new q bound, all-selector lower bound, near-linear full-promise cover, or P-vs-NP proof.
