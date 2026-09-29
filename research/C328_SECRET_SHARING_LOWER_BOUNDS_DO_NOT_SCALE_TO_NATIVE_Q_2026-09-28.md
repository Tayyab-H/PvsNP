# C-328 - Secret-sharing circuit lower bounds are below the native q scale without an address lift

Date: 28 September 2026  
Route: test a recent secret-sharing/monotone-circuit connection against Q186.  
Classification: **PARAMETER FILTER; NO LOWER-BOUND-PRESERVING MAP TO q.**

## Literature result and scale translation

Applebaum and Nir construct a uniform family `E_t` of monotone circuits of size `Theta(t)` over `Theta(t)` inputs whose average secret-share size is `Omega(t/log t)`, hence total share size `Omega(t^2/log t)`. Their meta-complexity theorem also makes it coNP-hard to distinguish cheap from expensive secret-sharing instances given a monotone circuit. These are strong results about secret-sharing complexity and its recognition problem.

For a direct truth-table embedding into the project parameter, `Theta(t)` Boolean inputs require a table length

```text
N = 2^(Theta(t)),   so t=Theta(log N).
```

The explicit share-size lower bound is then only `Omega(log^2 N/loglog N)`, which is far below the native floor `q=N-o(N)`. A product over address positions might change the scale, but no such product has been shown to preserve the secret-sharing lower bound inside C-281's compatible-support grammar.

## Why the apparent algebraic bridge is not yet a transfer

C-281's state supports form an idempotent compatible-union grammar. C-304 embeds it faithfully into monomial ideals in a `3^N`-dimensional algebra, but table acceptance is membership of the input-dependent full monomial. A secret-sharing access structure is a monotone predicate on participant subsets, and its known circuit compilers/lower bounds do not supply a q-state representation of these ideal-valued equations. There is no map here taking a q-pair Gap-MCSP cover to a secret-sharing scheme of total size `O(q polylog N)` or conversely.

Therefore the new secret-sharing theorem cannot by itself prove `q>N g(N)`, and the coNP-hardness of GapSS is a hardness-of-recognition statement, not an unconditional lower bound for this fixed MCSP promise. To reopen this route, first prove a semantics-preserving translation with explicit parameters and verify it on C-257 parity and C-258 equality. Until then, keep Q186 on direct native synchronization or the full-promise cover.

Sources: Applebaum and Nir, [*The Meta-Complexity of Secret Sharing*](https://eccc.weizmann.ac.il/report/2025/001/download), Theorem 4.1 and Theorem 2.3; native ideal boundary: `research/C304_IDEMPOTENT_SUPPORT_ALGEBRA_AND_SPAN_PROGRAM_BRIDGE_2026-09-28.md`.

**Disposition:** no new native q bound, full-promise cover, CohEnc transfer, or P-vs-NP proof. This closes the direct parameter substitution only, not every possible secret-sharing connection.
