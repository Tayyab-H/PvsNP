# C-313 - An arbitrary monotone guard does not inherit the literal-cofactor decoder

Date: 28 September 2026  
Classification: **MECHANISM BOUNDARY / ROUTE FILTER.**  
Scope: continuation of the C-311/C-312 ODDFACTOR primal-dual LowExt construction.

## 1. What C-312 actually uses

C-312 is an exact decoder only because the guard is a source literal `x_r`. On `x_r=0`, the NO image is bottom, so the free OR of all rails computes the zero cofactor. On `x_r=1`, universal dual consensus saturates a fixed opposite-rail pair on every YES input, and NO consistency makes that pair false on NO. Those are exact monotone decoders for the two literal cofactors; the identity

```text
f(x) = f_0(x_without_r) OR (x_r AND f_1(x_without_r))
```

then gives `CycAnd(f)<=2a+2`.

Replacing `x_r` with an arbitrary monotone guard `g(x)` does not give this decomposition. The zero-guard region is defined using `not g`, which is not an allowed monotone selector. A circuit that correctly decodes `f` on `g=0` may continue to accept NO inputs with `g=1`; a pair decoder can handle YES inputs with `g=1`, but it cannot remove the false positives from the first decoder using a negative test for `g`.

## 2. Exact limitation of the aggregate decoder

Write `D=OR_{j,b} Phi_(j,b)` and fix `R=Phi_(j,0) AND Phi_(j,1)`. For a universal-dual guarded map, `D=1` on every YES input because a complete low code is present; `R=1` on YES inputs where `g=1`; and `R=0` on every NO input by one-hot high-code consistency. If some NO input with `g=1` also has `D=1`, then the aggregate observation `(D,R,g)=(1,0,1)` occurs on a NO input. Any YES input with `g=0` and no primal rail collision gives `(1,0,0)`. Since `(1,0,0) <= (1,0,1)`, no monotone Boolean function of just these three aggregates can separate those two cases.

This is a deliberately limited statement: it does not rule out using the full `2N`-rail vector or a richer cofactor family. It identifies why the one-literal Shannon proof cannot be promoted by replacing its literal with a single semantic guard bit.

## 3. Consequence for the live route

A surviving guarded span-program map must do at least one of the following:

1. make the guarded decoy contribution vanish on every NO input and account for the cost of whatever condition enforces that vanishing (if the condition is exactly `g=1` on YES and `g=0` on NO, it already decides the source);
2. provide a controlled family of literal cofactors whose exact decoders can be recombined with quantified state/gate cost; or
3. use information in the full output profile that cannot be compressed to the monotone aggregates above, while preserving NO one-hot consistency and avoiding every cheap output-only decoder.

The third option is the genuine global-selector/reconstruction problem. It reconnects to O-168 and O-179; it is not solved by a small monotone guard circuit alone. No CohEnc upper bound, q improvement, or P-vs-NP result follows.

## 4. Frontier checkpoint against the continuation agenda

The new attachment's requested C-282 work is already superseded in the repository by C-286: shared-DAG accounting has no output-rail factor, but the valid theorem is directional rather than two-sided. The exact matching amplification threshold and its failed OPS patch-radius condition are recorded there. The clique canonical-table test is C-287/C-290; the reconstruction measure and ODDFACTOR direct-span obstruction are C-288/C-291/C-310/C-311; literal guarding and the hard zero cofactor are C-312. Thus repeating those items would add no result.

The exact live frontier remains: construct a non-vacuous varying YES-code C-125 map with an explicit cheap cost, or prove a general decision compiler for that richer map; independently, find a q-sensitive global coherence theorem or a near-linear full-promise cover. Actual `rho_GapMCSP=N-o(N)`.
