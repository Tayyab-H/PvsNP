# C-343 — Universal-selector quantifiers and the magnification bridge

Date: 29 September 2026  
Route: Q201 / check whether selector failure is logical (quantifier order) and identify the exact conditional bridge from OPS to the native game.  
Classification: **EXACT QUANTIFIER FILTER + CIRCUIT/RELAY MODEL RECONCILIATION; NO IMPROVED BOUND.**

## 1. Frozen target

The primary object remains the exact C-319 recurrence

```text
x_i^(t+1)(w) =
  (A_i(w) OR OR_{j in P_i^E} x_j^t(w))
  AND
  (B_i(w) OR OR_{j in P_i^H} x_j^t(w)),
```

with q globally shared states and least-fixed-point semantics. The target remains a first superlinear lower bound on the actual Gap-MCSP fusion cover, or a valid near-linear full-promise cover. The verified bound is still `rho_GapMCSP >= N-o(N)`.

## 2. Exact quantifier-collapse lemma

Let `w in {0,1}^N` be any table, `a in [N]` an address, and `C` a circuit. Consider a proposed verifier that makes a fresh circuit choice after the address is challenged:

```text
for every address a, there exists a circuit C_a of size <= s
such that C_a(a) = w_a.
```

For every table w this statement is true as soon as the circuit class contains the two constant circuits: choose `C_a` to be the constant `w_a`. Therefore

```text
forall a exists C_a: C_a(a)=w_a
```

has no distinguishing power at all. The necessary coherent condition is instead

```text
exists one C of size <= s, forall a: C(a)=w_a.
```

The quantifiers cannot be swapped. This proves that duplicating a circuit witness independently at each universal address challenge cannot yield a sound Gap-MCSP cover. It is not merely a circuit-size loss: the resulting predicate accepts every table.

## 3. What sharing must transmit

The obvious repair chooses one circuit globally. A shared positional state can keep the same successor choice whenever it is revisited, but the continuation at that state has no caller/address parameter. If address-specific gate checks merge there, it cannot later select different local witnesses as the address varies. If gate-address copies are used instead, their independent choices restore the invalid `forall a exists C_a` quantifier order unless a separate global consistency mechanism couples them.

C-281/C-306 give a second restriction on one proposed coupling: supports matching the same accepted table cannot carry an exclusive caller/description association through a reused state, because every context support is compatible with every matching replacement support and the full cross-product must be sound. This does not rule out every semantic use of supports or every native cover.

The remaining readable-state route is still real. C-342 proves that the input reaches the fixed graph through the `2q` seed-clause signature, and the activation vector is deterministic from that signature. At q near N these channels have enough raw capacity to encode the input or a short description; no information-capacity argument rules them out. A positive construction must select a globally valid description from w, make the description and current address jointly readable during verification, and prove soundness for every compatible splice.

## 4. Check against the OPS bridge

OPS Theorem 1.4 states that if, for every sufficiently small fixed `beta>0`, the corresponding Gap-MCSP promise has no Boolean circuit of size `N^(1+epsilon)` for some fixed `epsilon>0`, then `NP` is not contained in `Circuit[poly]`. With `N=2^n`, its thresholds have the form `s1=2^(beta*n)/(c*n)=N^beta/(c log N)` and `s2=2^(beta*n)=N^beta`, matching the project’s magnification scale. This is a conditional magnification theorem, not an unconditional circuit lower bound. [OPS, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf)

The known native-to-circuit compiler goes in the other direction: unrolling q rounds yields an ordinary monotone circuit with at most `q^2` paid AND gates. Consequently, using only that compiler, an ordinary lower bound `L(N)` yields `q >= sqrt(L(N))`; proving `q>N^(1+epsilon)` this way needs `L(N)>N^(2+2epsilon)`. OPS’s `N^(1+epsilon)` threshold alone does not cross the native linear barrier through this square-loss bridge.

The reverse compiler is **already established** in the repository as C-109 / Idea 109; an earlier draft of this report incorrectly called it open. For any disjoint promise `Y,Z` and any De Morgan circuit C of size S that is 1 on Y and 0 on Z, dual-rail the N input bits. For each monotone wire g, take the semantic carrier `E_g={z in Z: g(z)=1}`. An AND gate is a pair `(E_a,E_b)`, whose consequence is `E_a intersect E_b=E_g`; an OR gate uses the carrier `E_g=E_a union E_b` and a pair `(E_g,Z)`, whose predecessor inclusions make either child sufficient. Literal carriers are initially active exactly on matching low inputs. Induction through the circuit proves completeness, while every active carrier on a fixed high table z contains z; since the output carrier is empty, soundness follows. With dual-rail overhead and one rule per AND/two per OR, `rho(Y,Z)<=3S+1` (up to the gate convention already stated in C-109).

The transfers are asymmetric. If `C(N)` is the minimum fan-in-two De Morgan circuit size for this promise and `rho(N)` is the minimum fusion-list size, C-109 gives

```text
rho(N) <= 3 C(N) + 1,
so C(N) >= (rho(N)-1)/3.
```

Thus proving `rho>N^(1+epsilon)` itself proves a general circuit lower bound `C=Omega(N^(1+epsilon))`; the fusion endpoints do not make the desired lower-bound task easier than the central circuit lower-bound problem. In the other direction, the C-319 q-round compiler gives `A_cap<=q^2` when unbounded OR fan-in and semantic seed clauses are free in the paid-AND measure. Do not silently identify `A_cap` with standard fan-in-two circuit size: charging all OR/seed fan-in gives the larger explicit compiler recorded in Idea 107. The q-squared bound alone therefore transfers only lower bounds stated in the matching paid-AND model.

By the contrapositive of OPS, under `NP subseteq Circuit[poly]` there are circuit upper bounds at arbitrarily small beta choices (for each fixed target exponent); C-109 turns each such circuit into a fusion cover of size at most `3S+1`. This is enough for the magnification implication: a lower bound `rho>N^(1+epsilon)` uniformly for every sufficiently small beta would contradict those arbitrarily small-beta upper-bound instances after choosing a fixed exponent margin. It is not an unconditional near-linear cover. See the existing proof in `ideas.md` (Idea 109) and the model audit in `research/BARRIER_AUDIT.md`.

## 5. Construction-side check

The local selector architecture has now been tested from both quantifier directions:

- independently selecting `C_a` after each challenge accepts every w (Section 2);
- choosing one circuit in path history loses the challenged address after a shared state (C-341);
- storing a selected circuit only in the current path state requires `2^(Omega(s1))` residual states for the sparse-indicator family (C-342);
- matching support payloads at one anchor cannot retain a private caller tag (C-281/C-306).

These facts eliminate several concrete verifier layouts, but they do not exhaust the q-state recurrence. In particular, an input-derived activation code or a non-circuit proof grammar remains outside these architecture-specific arguments. I did not derive a near-linear full-promise cover.

## 6. Five-question checkpoint

1. **Did `rho_GapMCSP` improve beyond `N-o(N)`?** No.
2. **Was a valid near-linear full-promise cover constructed?** No.
3. **Was a state-sensitive synchronization theorem proved for arbitrary C-319 covers?** No; only scoped selector obstructions are proved.
4. **Was a positive CohEnc transfer constructed?** No.
5. **Was a general reconstruction-to-decision compiler proved?** No.

Because all five answers are no, the next phase must change mechanism rather than add another nearby selector obstruction. The OPS-to-native bridge is closed by C-109: under `NP subseteq Circuit[poly]`, the conditional OPS circuit upper bound already gives a same-exponent native cover. Therefore the live mathematical task is a general circuit lower bound for the actual Gap-MCSP promise, or a direct q lower bound strong enough to imply one. Any proposed native invariant must be recognized as a candidate technique for this major lower bound and must survive C-257/C-258/C-307/C-317; raw information, profile count, or proof-path count is not enough. The exact quantifier-collapse lemma remains a useful filter for verifier architectures, not a route around the circuit barrier.

## Status

No P-vs-NP proof, superlinear native bound, unconditional near-linear native cover, or positive transfer was obtained. The quantifier-collapse lemma is exact but architecture-specific. The C-109 circuit-to-relay compiler is prior repository work, not a new result of C-343; C-343's contribution is to connect that compiler to the current C-319/OPS frontier, identify the required exponent margin, and correct the earlier mistaken open-bridge claim. The actual bound remains `rho_GapMCSP >= N-o(N)`. No tests were run; this was a proof and literature audit.
