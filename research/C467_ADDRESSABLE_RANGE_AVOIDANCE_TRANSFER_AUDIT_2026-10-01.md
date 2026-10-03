# C-467 - dense natural properties solve only addressable range avoidance

**Status:** a precise project-proved implication and a costed failure of the general source transfer; no Gap-MCSP or P-vs-NP frontier change.

## Addressable-range lemma

Let N=2^n, and let R be a set of N-bit truth tables with density at least 1-delta, disjoint from every function of n input bits having ordinary circuit size at most t. Let E(x,z) be a single-output fan-in-two circuit of size r<=t, where z ranges over {0,1}^n and x is a seed. Define the N-bit output table T_x by T_x[z]=E(x,z).

For each fixed seed x, hardwiring x in E gives an n-input circuit of size at most r for T_x. Therefore T_x is not in R. If membership in R is computed by a circuit Q, sample a uniform y in {0,1}^N and output it when Q(y)=1. Every output is outside the range of x -> T_x, and one trial succeeds with probability at least 1-delta. This is an unconditional consequence of the useful-property guarantee, not a lower bound.

For C-465's separator-induced property, delta <= 2^(-N+O(N^beta*n)) and t=floor(N^beta/(10n)). Thus the property would give an almost-sure randomized solver for this restricted Avoid problem whenever the entire range has a single-output addressable evaluator of at most t gates.

## Why the transfer stops for arbitrary multi-output circuits

Given an arbitrary circuit C with N output wires, a generic evaluator E_C(x,z)=C(x)_z must select one of N output wires using the n-bit address z. A binary mux network costs O(N) gates, in addition to the gates of C. Since t=N^beta/(10n)=o(N), the addressability cost exceeds the useful property's Low threshold. This is an upper-bound accounting fact, not a lower bound: structured multi-output circuits may have cheaper addressable evaluators.

A sharp model check is a constant multi-output map whose N output labels encode an arbitrary truth table. Its gate count can be zero if output labels are free, while an evaluator selecting the zth label needs a mux of size O(N). If description bits or output wires are charged, they must be reported separately; neither model gives a free O(t)-gate addressable evaluator from gate count alone.

## Literature comparison and route verdict

Hirsch and Volkovich prove that randomized Turing reductions to MCSP can solve Range Avoidance with high probability using an MCSP oracle, for arbitrary range circuits. Their result concerns oracle algorithms, not a circuit lower bound for MCSP or the OPS promise. The addressable-range lemma above is a restricted consequence of a dense useful property, and does not strengthen their general oracle result or produce an NP-hard source. [Hirsch-Volkovich, ECCC TR25-220](https://eccc.weizmann.ac.il/report/2025/220/download)

To turn this into a source route would require a source problem whose hard instances are encoded by compact addressable range families, together with exact Low/High endpoints and a generator-plus-separator budget below source hardness. No such source or budget is established here. Do not treat the existence of an almost-everywhere non-range table as evidence that arbitrary Avoid is easy: verification by R works only because every range table is guaranteed Low.

**Frontier effect:** none. The ordinary circuit lower bound remains N-O(N^beta log N), with the existing additive logarithmic reconvergence refinement. The exact full-promise upper remains O(N*2^(O(N^beta))). No near-linear full-promise separator, fixed-epsilon OPS lower bound, native rho advance, or P-vs-NP proof was obtained.