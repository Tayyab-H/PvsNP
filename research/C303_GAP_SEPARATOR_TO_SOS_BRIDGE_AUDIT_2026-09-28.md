# C-303 - A gap separator is not an SoS refutation

Date: 28 September 2026  
Classification: **PROOF-COMPLEXITY ROUTE AUDIT / BRIDGE FAILURE.** The connection to Austrin–Risse SoS lower bounds is real, but the direct conversion from a native Gap-MCSP cover to a refutation of circuit existence is invalid. No fusion lower bound follows.

## Candidate bridge

A q-pair native cover for the OPS promise induces a monotone separator `h_Q` on signed truth-table literals. On complete table encodings it satisfies only

```text
CC(u) <= s1  => h_Q(e(u))=1,
CC(u) >  s2  => h_Q(e(u))=0.
```

Its value on the medium band `s1 < CC(u) <= s2` is unconstrained. A tempting route is to hardwire a high table z, use `h_Q(e(z))=0`, and interpret the closure computation as a short SoS refutation of `Circuit_s2(z)`.

## Exact failure

An SoS refutation of `Circuit_s2(z)` certifies that **no** circuit of size at most `s2` computes z. A valid promise separator need not accept every table with circuit size at most `s2`: it may reject a medium table `u` with `s1<CC(u)<=s2`. Thus the semantic fact `h_Q(e(u))=0` is compatible with `Circuit_s2(u)` being satisfiable. Evaluating the separator to zero supplies no algebraic identity refuting that satisfiable constraint system.

To repair this, one would need a totalization theorem that turns promise behavior on the low/high gap into a sound refutation of every size-`s2` circuit, or a threshold-chain construction controlling the entire medium band. Neither is part of the native cover definition or C-281 grammar. A q-state evaluation trace alone is not an SoS certificate.

## Quantitative check against the primary result

Austrin and Risse prove that for any Boolean function f requiring circuits larger than s, SoS degree `Omega_epsilon(s^(1-epsilon))` is needed to refute `Circuits(f)`; for monotone slice functions they prove an analogous degree bound for small monotone circuits. Their size lower bound requires an additional errorless-heuristic-circuit hypothesis and a specified error count. See [Austrin–Risse, Sum-of-Squares Lower Bounds for the Minimum Circuit Size Problem](https://drops.dagstuhl.de/storage/00lipics/lipics-vol264-ccc2023/LIPIcs.CCC.2023.31/LIPIcs.CCC.2023.31.pdf), Theorems 1, 3–5.

At the OPS source threshold `s=s2=N^beta`, the degree lower bound scales as `N^(beta(1-epsilon))` up to the source's parameter conventions, below the existing native floor `q=N-o(N)` for every fixed `beta<1`. Even a hypothetical direct bound of degree `O(q)` would not force q above N. The stronger SoS size theorem cannot be invoked for arbitrary high truth tables: the promise says they lack small exact circuits, but does not give them a small errorless heuristic circuit with the theorem's required error parameter.

## Disposition and salvage condition

Retire the direct implication “small native cover / separator evaluation -> SoS refutation of `Circuit_s2(z)`.” A viable revival needs both:

1. a proof-producing conversion that soundly covers the unconstrained medium band; and
2. parameters whose SoS lower bound exceeds the current linear q floor after accounting for the conversion loss.

No such conversion or parameter window is known. The full-promise near-linear-cover and native global-description-coherence branches remain the active mechanisms. Actual `q=N-o(N)` is unchanged; no superlinear Gap-MCSP bound or P-vs-NP proof follows.
