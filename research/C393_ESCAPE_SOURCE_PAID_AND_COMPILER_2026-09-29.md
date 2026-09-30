# C-393 - Escape-source rounds bound paid AND work in the native readout

Date: 29 September 2026  
Route: extract the C-94 event-bounded normal form in the specialized `A_cap` measure.  
Classification: **PROVED PARAMETERIZED UPPER COMPILER FOR EVERY VALID COVER; NO ESCAPE-COUNT BOUND OR READOUT LOWER BOUND.**

## 1. Statement

Let a valid C-319 cover have q rules, m empty-carrier output roots, and v=q-m nonroot candidate rules. Delete roots from the pre-acceptance recurrence as in C-322. Apply C-92's two-sided transitive-support pruning, C-93's equal-carrier quotient (retaining each candidate rule as a separate alternative), and C-94's escape normalization.

Let s be the number of distinct nonroot carrier values that occur as one-sided escape sources after these reductions. In the paid-AND measure `A_cap` of C-307—binary AND gates are charged, while arbitrary-fan-in ORs, signed literals, and seed clauses are free—the active promise separator has a circuit with at most

```text
m + (s+1)*v
```

binary AND gates. The terminal contribution is m because the root-free terminal tests need not agree even though full-system root bits eventually agree. This bound should be combined by taking the minimum with the C-323 SCC and C-324 feedback-core compilers.

## 2. Proof

In C-94 normal form, the carrier recurrence is

```text
H_t(x) = K_t(x) OR D_t(x),
D_t(x)   = OR_{i in I_t} d_i(x),
d_i(x)   = (a_i OR OR_{u in L_i} x_u)
           AND (b_i OR OR_{u in R_i} x_u).
```

`K_t` is propagation from lower Hasse-cover carriers; `L_i,R_i` contain only one-sided escape sources. Let `Up(D(x))` be the upward closure of the carrier values where D is true. By induction through the finite carrier poset, the fixed-point equations `x=H(x)` are equivalent to `x=Up(D(x))`: the Hasse terms propagate every D-trigger upward, while no other terms remain after C-92/C-93/C-94. The two monotone maps therefore have the same least fixed point.

Iterate `G(x)=Up(D(x))` from zero. One macro-round computes at most v candidate conjunctions d_i, then combines them and propagates upward using only free OR gates. Thus each round costs at most v paid AND gates.

The first round is counted separately. For every later strict round, D must change on the preceding carrier vector; otherwise its upward closure would also be unchanged. Since seed values are fixed during the iteration, a candidate conjunction can newly turn on only if one of its escape-source carrier variables has changed from 0 to 1. The iteration is monotone, so each of the s distinct source variables can make this transition at most once. There are therefore at most s later strict rounds, for at most s+1 rounds total. Once the carrier fixed point is reached, each of the m root terminal tests is a conjunction of its two root-free side predicates, costing one paid AND; their final OR is free. This gives `m+(s+1)v`.

## 3. Scope and hostile checks

- This is an `A_cap` upper bound, not a Boolean gate-count bound: the seed clauses and all OR computations are free in this measure. C-94's ordinary-circuit compiler still charges the seed/support OR networks.
- C-322 does not permit replacing the m root terminal tests by one test after root deletion. Only the *full-system final root bits* agree; the root-free terminal predicates `E_r(y) AND H_r(y)` can differ. The safe cost remains m.
- Since `s<=v`, the worst case is still quadratic. When `s=o(v)`, this compiler can beat the generic quadratic bound; taking the minimum with C-323/C-324 can improve it further for favorable SCC or feedback profiles.
- The project has no bound forcing s to be small, no lower bound on `A_cap` above the scale needed for a superlinear q conclusion, and no full-promise near-linear cover. Local seed width does not by itself bound the escape-source count.
- C-387/C-390 remain route filters for wide-feature deletion; C-393 does not revive that inference.

**Status:** a proved state-sensitive parameterization of the exact readout's paid AND work. The native lower bound remains `q>=N-o(N)`; no all-selector bound, q-preserving selector bridge, or P-vs-NP proof follows.
