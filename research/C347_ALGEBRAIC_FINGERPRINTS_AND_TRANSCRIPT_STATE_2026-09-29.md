# C-347 - Algebraic fingerprints compress checks but not native transcript state

Date: 29 September 2026  
Route: test whether arithmetization or sum-check can replace the gate-by-address verifier by a near-linear exact C-319 cover.  
Classification: **CONSTRUCTION AUDIT; THE STANDARD FINGERPRINT ROUTE DOES NOT FIT THE EXACT GAME; NO q IMPROVEMENT.**

## 1. The proposed compression

For a table `f:{0,1}^n -> {0,1}`, a candidate low circuit `C` is a correct witness exactly when

```text
for every address a in {0,1}^n, C(a)=f(a).
```

The dual rejection condition is equally exact: if `CC(f)>s2`, every circuit `C` of size at most `s1` disagrees with `f` at some address. This suggests replacing the `N` address checks by one algebraic fingerprint, or by a sum-check protocol that has only `poly(n)` communication.

## 2. Why the direct polynomial fingerprint is not a near-linear exact verifier

The table has a multilinear extension

```text
f_hat(X) = sum_{a in {0,1}^n} f(a) * product_i (a_i*X_i + (1-a_i)*(1-X_i)).
```

An arithmetic translation `C_arith` of a Boolean circuit agrees with `C` on Boolean inputs, using `NOT(z)=1-z`, `AND(z,u)=zu`, and `OR(z,u)=z+u-zu`. However, `C_arith` need not equal the multilinear extension of C away from the Boolean cube. Its individual degree can grow exponentially with the circuit size. A Schwartz-Zippel test against `f_hat` therefore needs a field whose size exceeds that degree to obtain a constant error bound; the challenge then contains `Theta(s1)` bits per coordinate in the worst case, and the circuit no longer has a small challenge space.

Replacing `C_arith` by the multilinear extension `C_hat` fixes the degree, but it removes the cheap evaluation step: constructing or evaluating `C_hat` from the succinct circuit C is itself a truth-table extension problem. The direct construction can require evaluating C on all N Boolean addresses, restoring an `N*s1`-scale gate/address computation (or a comparably costly transform). Equality on the Boolean cube remains the clean exact test; the algebraic rewrite alone has not compressed it.

This is not a claim that every possible arithmetization has large cost. It identifies the missing ingredient precisely: a low-degree extension of a size-s circuit's truth table that is both cheaply evaluable and compatible with the native game.

## 3. Sum-check moves the same memory obligation to the final query

Sum-check reduces verifier communication by sending an adaptive transcript of field elements. Its final check still evaluates the relevant low-degree extensions at the accumulated challenge vector. A conventional verifier stores that vector (or has oracle access that evaluates the extensions there). In C-319, seed predicates read only fixed disjunctions of input-table literals; a state reached after histories merge has no access to the caller's challenge transcript. Its least-fixed-point value depends only on the current state and the fixed seed signature.

There are two direct encodings, neither giving the requested cover:

1. Keep the address/challenge and the circuit gate in the state. This restores the gate-by-address product, with `N*s1` states for Boolean-address evaluation, before charging transcript-field overhead.
2. Share a gate/configuration state across challenges. Then the continuation loses the challenged address or challenge prefix. The state cannot ensure that repeated uses of an input variable refer to the same chosen challenge value. This is the C-341 state-merging obstruction in algebraic-verifier form.

The same-anchor support-product result from C-281/C-342 blocks treating a proof support as a private transcript register: two supports matching one anchor are compatible, so their cross-substitutions must remain sound.

## 4. Exact scope of the obstruction

The argument rejects the standard arithmetize-then-fingerprint proposal and direct sum-check compilation into the current positional C-319 game. It does **not** prove that every native cover needs `N*s1` states, and it gives no lower bound for arbitrary endpoint-induced games. A different construction could still provide a cheap low-degree truth-table extension, an input-derived activation code that coherently carries the challenge, or a semantic cover that does not verify a selected circuit gate by gate. Each would need a complete all-input C-281 soundness proof.

## 5. Checkpoint

- Actual native lower bound: `rho_GapMCSP >= N-o(N)`.
- Superlinear native bound: not obtained.
- Near-linear full-promise cover: not obtained.
- Positive `CohEnc` transfer or general reconstruction-to-decision compiler: not obtained.
- P-vs-NP proof: not obtained.

The algebraic route is parked unless someone supplies the missing succinct extension/readout primitive. Do not count the small communication of sum-check as a small native state count.
