# Frontier checkpoint after C-393

Date: 29 September 2026  
Purpose: checkpoint after three proof-level claims since the C-390 frontier: C-391, C-392, and C-393.

## Required five-part checkpoint

| Front | Status after C-393 |
|---|---|
| Native quantitative bound | **No change.** The proved bound remains `rho_GapMCSP >= N-o(N)`. There is no full-promise `N^(1+epsilon)` lower bound or `N^(1+o(1))` cover. |
| Hard-core selector | **Partial-domain result only.** C-391 places canonical witness search in `FP^Sigma_2`; C-392 gives an `O(N log^3 N)` selector valid on `1-o(1)` of uniformly random sparse supports. There is still no all-high selector or all-selector lower bound. |
| Selector/native bridge | **None.** Candidate sample verification remains coNP; no size-controlled conversion to or from arbitrary C-319 covers is known. |
| Collectively hard low subclass | **None.** C-390's RM family is easy to recognize; no individually easy but collectively hard family with an OPS-preserving transfer has been proved. |
| Local-seed LFP readout | **Upper bound, no lower bound.** C-393 proves `A_cap<=m+(s+1)(q-m)` for every valid cover, where s counts distinct escape-source carriers. No full-promise bound on s or paid-AND lower bound is known. |

## What survived

- C-391 makes the search-to-decision quantifiers exact; it does not make selector search cheap.
- C-392 strengthens C-23 at C-388's exact error threshold, but only for the typical sparse-support distribution. Random sparse supports cannot be the sole hard distribution.
- C-393 pinpoints the escape-source carriers as the only source of feedback in the normalized readout and gives a paid-AND round bound. It is useful when s is small; no theorem currently forces that regime.

## Mechanism change

All five requested success questions remain unanswered. Stop refining narrow-seed localization, fixed-sample concentration, generic SCC counts, and raw escape counts as standalone routes. The next main attack is the **actual anchor-by-seed-clause incidence structure** from the continuation brief, tied to a collectively hard low family. It must be invariant under nonunique certificate choices, derived from arbitrary endpoint-valid covers, and pass C-258 repeated equality at linear cost. A promising theorem must bound a computational/readout measure or force superlinear q; raw table bits, row counts, or certificate width are insufficient. The selector and full-LFP fronts may continue only when they feed this new incidence/collective-recognition mechanism.

The overall goal remains active. None of these claims is a P-vs-NP proof or breakthrough.

## Incidence update after C-394

Correction after C-394 audit: the full seed-incidence row itself is a canonical safe clause set on every accepted low input. If `sigma(f)` is the 2q-bit seed vector, every table g above it (`sigma(f)<=sigma(g)`) is accepted by monotonicity and hence low by soundness. This is exactly C-385's order condition, not a new result; the proof-DAG subset is optional. C-368's clause count then yields only q >= (N-o(N))/2, below the already-known N-o(N) bound. The incidence matrix does encode safe cones, but the linear signed-singleton calibration shows those cones alone do not force superlinear q. Continue on constrained LFP readout/accept-reject computation or construct a full-promise near-linear cover.
