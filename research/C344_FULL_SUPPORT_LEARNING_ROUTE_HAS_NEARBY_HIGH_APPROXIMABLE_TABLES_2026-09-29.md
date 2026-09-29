# C-344 — Uniform full-support learning does not capture the explicit Gap-MCSP NO side

Date: 29 September 2026  
Route: literature-transfer audit of the 2026 full-support PAC-learning / implicit-MCSP result.  
Classification: **EXACT COUNTING OBSTRUCTION TO THE UNIFORM-SAMPLER LIFT; NO GAP-MCSP BOUND.**

## 1. Candidate connection

Goldberg, Juvekar, and Kabanets give conditional randomized half-Levin NP-hardness results for full-support learning and a gap version of **Implicit** MCSP, under cryptographic and proof-complexity assumptions. Their NO condition says that no circuit of size `subexp(s)` predicts the labels with accuracy noticeably above `1/2` on the supplied distribution. The project asks about explicit full truth tables with `s1=N^beta/(c log N)` and `s2=N^beta`, where `N=2^n`.

The most direct map sends an explicit truth table f to the uniform full-support example distribution `(x,f(x))`. It has the right YES case: if `CC(f)<=s1`, a size-s1 circuit predicts every label. The NO case fails for some promised high tables, as the following counting argument proves. This tests that direct lift; it does not rule out a more carefully constructed, f-dependent sampler.

## 2. High tables can be almost perfectly approximable

Fix any low table g, for example the constant-zero function. Circuit counting gives

```text
|SIZE(s2)| <= 2^(C s2 log(s2+n))
```

for an absolute model-dependent constant C. Let `r=K s2` for a sufficiently large fixed K (depending on beta and C). Since beta is fixed below 1, eventually `r<N/2`, and

```text
log2 binom(N,r)
  >= r log2(N/r)
  = K s2 ((1-beta) log2 N - log2 K)
  > C s2 log2(s2+n).
```

Choose K so the last inequality holds for all sufficiently large N. The Hamming sphere of radius r around g is then larger than `SIZE(s2)`. Hence it contains a table f with `CC(f)>s2`.

That f differs from g on exactly r addresses. A circuit can compute f by testing whether the n-bit input is one of those r addresses and toggling g there. Equality tests and their OR use `O(r n)` gates, so

```text
CC_approx(f) <= CC(g)+O(r n)=O(N^beta log N)=O(s1 (log N)^2).
```

Under the uniform-address distribution, this circuit predicts f with accuracy

```text
1-r/N = 1-K N^(beta-1) = 1-o(1).
```

Because `O(s1 (log N)^2)` is polynomial in s1 for every fixed beta>0, it is far below `subexp(s1)` (under the standard meaning `2^{s1^{Omega(1)}}`, and also under the weaker `2^{o(s1)}` convention). Thus this promised high table is a YES-like instance for the learning approximation criterion, not a NO instance. The direct uniform full-support sampler does not reduce the project’s Gap-MCSP promise to that learning problem.

## 3. What a repair would need

To obtain the learning NO condition, a sampler for a high truth table would need to place enough weight on points that defeat **every** circuit of size `subexp(s1)`. The counting proof does not show that no such f-dependent sampler exists. But constructing it is an anti-checker synthesis problem: one must find, from the whole truth table, a succinct distribution whose support hits the disagreement set of every small circuit. This is precisely the constructive selection bottleneck that appears in OPS, not an automatic consequence of high worst-case circuit complexity.

The cited 2026 result is itself conditional and concerns a sampler-described distribution / implicit source function; it is not an unconditional lower bound for the explicit all-address Gap-MCSP promise. No reduction with the required all-input, size-preserving sampler construction is established here. Primary source: [ECCC TR26-091](https://eccc.weizmann.ac.il/report/2026/091/).

## 4. Status and frontier update

This is a route-specific transfer obstruction, not a new lower bound. It does explain why the full-support-learning connection cannot be imported by simply making the truth-table rows uniform. The main native/circuit target is unchanged: `rho_GapMCSP>=N-o(N)`, with no superlinear bound, unconditional near-linear cover, positive CohEnc margin, or P-vs-NP proof.

The next step for this cross-field route, if reopened, is to construct an explicit succinct anti-checker sampler for every high truth table and prove its subexp(s1)-predictor soundness. Without that construction, further work on the learning theorem itself does not transfer to the present promise. The primary research target remains a general circuit lower bound for Gap-MCSP, as recorded in C-343.
## Correction added by C-345

The uniform-address obstruction above remains valid. Refine the last paragraph: the phrase “subexp(s1)-size predictor” must be read with a specified Total-Learn gap function g. TR26-091's formal theorem permits g(s)=2s, so the C-344 patch circuit does not rule out every f-dependent sampler in the learning family. For large g(s1), the same nearby high table is an exact-predictor obstruction. For a constant-factor g, C-345 proves pointwise hard-core-list existence under the OPS gap constants, while leaving the selector unconstructed. See research/C345_TOTAL_LEARN_GAP_PARAMETER_AND_POINTWISE_HARDCORE_MAP_2026-09-29.md.
