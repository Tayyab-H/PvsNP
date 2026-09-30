# C-398 - A near-linear conditional selector-to-decision reduction

Date: 29 September 2026  
Route: sharpen C-397 by charging the hard-core verifier at its true, short input length.  
Classification: **PROVED CONDITIONAL SIZE TRANSFER UNDER SMALL CIRCUITS FOR ONE NP LANGUAGE; NO UNCONDITIONAL SELECTOR, q IMPROVEMENT, OR P-VS-NP SEPARATION.**

## 1. One fixed NP language for sample validation

Keep the C-388/C-346 relation and parameters

```text
N = 2^n,
s1 = N^beta/(10n),
s2 = N^beta,
T = ceil(1.515*s1),
L = ceil(c*N^beta).
```

For a padded list of `L` addresses, include its actual length `ell`, the address array `Q`, the label array `y`, `n`, and a unary encoding of `T`. Define one language `BAD` (independent of beta): a well-formed input is in `BAD` iff there is an n-input Boolean circuit of size at most the unary T whose empirical error on the first ell examples is less than `259/1000`. Malformed inputs are rejected.

If the full input length is `M`, a witness circuit has description length `O(T log(T+n))`, and its predictions on ell examples can be checked in time polynomial in M. Therefore `BAD` is one fixed language in NP. For the C-346 parameters,

```text
M = O(L*n + T + n) = O(N^beta log N).
```

Using one universal language matters: under `NP subseteq P/poly`, its circuit exponent is a single constant `d`, independent of the later choice of beta. More generally, the argument only assumes `BAD` has circuits of size `O(M^d)` for some fixed d.

The relation `R(f,Q)` is equivalent, on a valid encoding, to `not BAD(n,T,Q,f|_Q)`. C-346 supplies valid lists of the fixed padded length L for every high f; low f have no valid list because f itself has size at most T and error zero.

## 2. Cost of composing selector, table lookup, and verifier

Suppose `S_N` is a total circuit on the N table bits. On every high table it outputs a valid C-388 list Q of length at most L. The output has a fixed-width encoding with a length field and padding.

Given the address bits from `S_N(f)`, compute the labels `y_i=f(x_i)` by direct lookup. For each i, compare `x_i` to each of the N constant addresses and OR together the matching `f_a` bit. With bounded-fan-in gates this takes `O(N log N)` gates per query, hence

```text
O(L*N*log N) = O(N^(1+beta) log N)
```

gates for all labels. Syntax/length validation of the fixed-width output costs only polynomial in its output length. Then feed `(n,T,Q,y)` to a circuit for `BAD` and negate its answer, also requiring the format to be valid.

**Theorem.** Suppose `BAD` has circuits of size `O(M^d)` for one fixed d. Fix `delta>=0` and `epsilon>delta`. For any sufficiently small fixed beta satisfying

```text
beta < min{ epsilon-delta, 1/d, beta_OPS },
```

where `beta_OPS` is any upper limit required by the chosen OPS theorem, an all-high selector of size `R_N<=N^(1+delta)` yields a Gap-MCSP separator of size at most `N^(1+epsilon)` for all sufficiently large N.

Indeed, the composed size is

```text
R_N + O(N^(1+beta) log N) + O((N^beta log N)^d)
= N^(1+delta) + O(N^(1+beta) log N)
  + O(N^(beta*d) log^d N).
```

The first two exponents are strictly below `1+epsilon`; `beta*d<1` makes the verifier term sublinear in N up to its logarithmic factor. The selector accepts every high input after validation. It rejects every low input because the circuit for f itself witnesses `BAD` for any list. The middle interval is unrestricted. Under `NP subseteq P/poly`, the premise on `BAD` holds for some fixed d because `BAD` is a single NP language.

This sharpens C-397's coarse `R_N+N^c` accounting: the validation circuit acts on the compressed sample, not the full truth table. The composition is conditional on a small circuit for `BAD`; it neither constructs S nor proves such a verifier unconditionally. It also does not turn a decision bit into the conditioned Sigma_2 prefix queries needed to synthesize Q.

## 3. Unconditional verifier-size check

The direct unconditional verifier enumerates all size-T circuit descriptions. Their number is

```text
2^(O(T log(T+n))) = 2^(O(N^beta)).
```

For each candidate it evaluates the ell listed examples. This gives a deterministic circuit upper bound `2^(O(N^beta))*poly(M)` for `BAD`, which is superpolynomial in N for every fixed beta>0. It is not near-linear. The minimax and LP existence proof does not remove this enumeration: its best-response/separation question is precisely whether a circuit in `BAD` exists. No short, polynomial-time-checkable certificate of `R(f,Q)` for all valid hard-core lists has been derived.

Thus an unconditional improvement needs a new ingredient: a specific small-circuit algorithm for this one NP language, a different sample relation with an unconditional efficient verifier, or a structural/native certificate that proves the universal predictor condition without solving the same search problem. The present result isolates the exact conditional leverage and does not assume any such ingredient.

### Proof-carrying sample attempt

There is a precise way to move validation into NP, at the cost of a new proof-length obligation. From the NP verifier for `BAD`, uniformly construct a polynomial-size Boolean circuit whose witness inputs encode a size-T predictor and whose output says it is valid and achieves error below `0.259` on `(Q,y)`. A standard Tseitin encoding gives a CNF `Phi_(n,T,Q,y)` that is satisfiable exactly when `BAD` holds. Augment the sample by a refutation `pi` of this CNF in a sound proof system with polynomial-time proof checking. Then checking `(Q,pi)` is deterministic polynomial time in `M+|pi|`; a low table admits no sound refutation because its own circuit makes `Phi` satisfiable.

For high f, C-346 supplies a Q making `Phi` unsatisfiable, so a refutation exists in a complete system such as Frege. But C-346 gives no polynomial, near-linear, or otherwise useful bound on `|pi|`. Requiring `|pi|<=M^c` makes the augmented relation NP-verifiable, yet its witness-existence premise is a new proof-complexity theorem not implied by minimax. A generic exhaustive refutation can be exponential in the CNF variable count, which is polynomial in M. Thus this formulation removes universal search from *verification* only by moving the hard part to existence and output length; it is a candidate for future work, not an efficient selector.

## 4. Native C-319 front: exact failed charge

The parallel attempt was to combine C-396's `s=Omega(log N/log log N)` escape-source lower bound with C-393's paid-AND compiler and the known `A_cap>=N-o(N)` floor. Since

```text
A_cap <= m + (s+1)(q-m) <= (s+1)q,
```

these facts yield only `q >= (N-o(N))/(s+1)`. C-396 is a lower bound on s, not an upper bound, and s may be as large as q. Therefore this inequality does not improve the existing `q>=N-o(N)` result; reversing the compiler would be invalid. A new endpoint-specific inequality that charges distinct escape carriers to state count is still required. No q-sensitive lower bound or endpoint-valid full-promise construction was found in this step.

## 5. Checkpoint

| Front | Status after C-398 |
|---|---|
| Native C-319 state count | Unchanged: `q>=N-o(N)`; no `N^(1+o(1))` full-promise cover. The attempted C-393/C-396 charge gives no improvement. |
| Hard-core selector | Still no all-high construction or all-selector superlinear lower bound. Conditional theorem: a selector of exponent `1+delta` gives a separator of exponent `1+epsilon` under `BAD` circuits, and hence under `NP subseteq P/poly`, for sufficiently small beta. |
| Unconditional verifier | Enumeration costs `2^(O(N^beta))`. A proof-carrying relation is P-checkable if a refutation is supplied, but C-346 gives no short-refutation bound. |
| Selector/native bridge | Still none with q-preserving overhead. |
| P-vs-NP | No proof or breakthrough. |

The project Goal remains active. C-398 is a conditional size-transfer theorem and a quantified route audit, not a P-vs-NP result.
