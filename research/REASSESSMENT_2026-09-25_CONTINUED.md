# Research reassessment — 25 September 2026 (continued)

## Reconstructed target and dependency path

The shortest established path remains

```text
OPEN O-1: Gap-MCSP[s1,s2] requires circuits larger than N^(1+epsilon)
    -- Oliveira–Pich–Santhanam magnification --> NP is not in P/poly
    --> P is not NP
```

Here `N=2^n`, `s1=N^beta/(c n)`, and `s2=N^beta`. The first open node is already a major unrestricted circuit lower bound. It quantifies over arbitrary nonuniform circuits, so the missing fact is not a bridge from a preferred solver architecture: it is the lower bound itself. The selector formulation is equivalent as a target-specific encoding of the same synthesis barrier: map each high table `f` to a short query list `Q_f` whose labels disagree with every size-`s1` circuit on at least one query.

The strongest established project bounds remain linear: the semi-filter/cover route gives `N-o(N)` gates, and every valid selector has `N-o(N)` essential inputs. The C-40 minimax argument gives short anti-checkers per table; C-47/C-48 clarify that exact counting is one construction method, not a universal property of selectors. C-49 gives robust trace distance, and C-50 gives large majority-error regions for every small odd subfamily. None gives a superlinear lower bound for arbitrary routing.

## C-51 — A dense graph of large pairwise error overlaps

Let `f` have `CC(f)>s2`, and let `C` be the set of distinct Boolean functions with circuit complexity at most `s0`. For each `D` in `C`, write `E_D={x:D(x) != f(x)}`. Suppose `s0=s1` at OPS parameters.

For any three distinct functions `D1,D2,D3`, their majority circuit has size at most `3s0+O(1)`. Its error set is the set of inputs belonging to at least two of `E_D1,E_D2,E_D3`. By the local-correction lemma C-49, this set has size at least

`h = (s2 - 3s0 - O(1))/(a n) = Omega(N^beta/n)`,

where `a` is the point-correction constant. Since each point in that majority-error set belongs to at least one of the three pairwise intersections, one pair has intersection size at least `h/3`.

Define a graph on `C` by joining `Di,Dj` when `|E_Di intersect E_Dj| >= h/3`. Every triple contains an edge. Therefore the graph of non-edges is triangle-free. Mantel's theorem implies that the heavy-overlap graph has at least `binom(|C|,2)-floor(|C|^2/4) = |C|^2/4-O(|C|)` edges.

This is a genuine global consequence of C-50: a constant fraction of all pairs of low-circuit functions are wrong together on `Omega(N^beta/n)` inputs. It is compatible with arbitrary sharing and negation because it is stated for circuit functions, not a chosen representation.

### Further consequence for residual sets

The same triple argument applies to any subset `A` of `m` low-circuit functions. Each heavy edge inside `A` has at least `h/3` common error points. If `d_x` is the number of functions in `A` wrong at `x`, then

`sum_x binom(d_x,2) >= (h/3) * (m^2/4-O(m))`.

As `binom(d_x,2) <= d_x^2/2`, some point is wrong for at least `Omega(m*sqrt(h/N))` functions in `A`. An ideal max-score process over residual distinct functions therefore contracts by only `Omega(sqrt(h/N)) = Omega(N^(-(1-beta)/2)/sqrt(n))` per round. Over `O(s1 log s1)=O(N^beta)` rounds this yields a combinatorial query bound `O(N^((1+beta)/2)*sqrt(n))`, worse than the C-40 minimax list bound `O(N^beta poly(n))` for fixed `beta<1`. This is only an existential process: counting distinct functions may be harder than #P counting syntactic descriptions, and it supplies no circuit for identifying a high-incidence point. It does not improve the selector construction or O-1.

### Adversarial test: overlap statistics do not force routing hardness

An abstract search problem shows the limitation without relying on repeated copies of one hypothesis. Fix a core set `S` of `h` coordinates. Let the hypothesis class contain many distinct functions, all zero on `S`, with arbitrary distinct behavior outside `S`; declare as hard targets tables that are one on every point of `S`. Every hypothesis error set contains `S`, so every odd-tuple majority-error region has size at least `h`, and every pair has maximal common overlap. Yet the selector that queries any fixed point of `S` is valid and has constant circuit size. This is not an MCSP counterexample: the declared hard predicate and the fixed common core are artificial. It proves that majority-region size and overlap alone cannot imply a superlinear selector lower bound. The missing theorem must use the richness and representation-specific geometry of *all* small circuits in relation to actual high-complexity tables.

## Failed strengthening caught before entry

I tested whether the `k=Theta(n)` majority statement forces the *average* low-circuit error size to be `Omega(N)`. Let `p_x` be the fraction of low circuits wrong at coordinate `x`, and let `r=(k+1)/2`. The probability that a random `k`-tuple majority is wrong at `x` is at most `2^k p_x^r`. C-50 then gives `sum_x p_x^r >= h/2^k`.

This does **not** imply a linear lower bound on `sum_x p_x`: the power-mean inequality goes in the opposite direction for the desired conclusion. For example, `p_x=1` on `h` coordinates and zero elsewhere is consistent with the displayed moment bound while `sum_x p_x=h`. At most the weak fact `max_x p_x >= (h/(N 2^k))^(1/r)` follows, and it is weaker than the constant-fraction point already implied by C-40's dual margin. No average-distance claim is made.

## Distinct attacks at the O-1 bottleneck

| Attack | Precise first theorem needed | Adversarial outcome | Decision |
|---|---|---|---|
| Globalize C-50 with extremal graph theory | Convert a dense heavy-overlap graph into a short, efficiently findable transversal | Density gives only pair coverage; an abstract common-core family has maximal overlap and a constant-size selector | Closed as a generic route; retain C-51 as a structural lemma |
| Use repeated selector updates against a fixed low circuit | Keep the update trajectory inside `CC(f)>s2` until a fixed point contradicts selector validity | Hamming distance to the fixed circuit decreases, but the trajectory can leave the high promise into the gap; no fixed point in the promise follows | Fails at promise preservation, not just implementation cost |
| Diagonalize over all polynomial-time SAT machines | A single NP verifier must encode a diagonal challenge against machines with unbounded polynomial exponents | The usual machine-indexed diagonal uses an exponent depending on the machine and loses NP membership; padding does not repair that | Remains open; no new construction found |
| Conditional hard-instance generation through implicit MCSP | Remove cryptographic and proof-system assumptions, or derive O-1 for explicit truth tables with the OPS parameters | The 2026 result is conditional and studies succinct/implicit instances and learning; it does not prove the explicit Gap-MCSP circuit lower bound | Useful adjacent program, not a route to an unconditional proof |

The best-supported route remains direct O-1, but the new fact identifies the exact circuit-specific extension to seek: turn dense pairwise agreement-on-error into an efficiently discoverable global organization of the full disagreement family. The theorem must beat the known dual-margin selector construction in the conditional `NP subseteq P/poly` world and apply to arbitrary selectors, rather than only to majority/greedy procedures.

## Literature update

Goldberg, Juvekar, and Kabanets (June 2026), [*Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions*](https://eccc.weizmann.ac.il/report/2026/091/download/), prove conditional NP-hardness for gap ImpMCSP and full-support PAC learning from subexponentially secure indistinguishability obfuscation plus nonexistence of an infinitely-often subexponentially optimal propositional proof system. The paper also derives conditional almost-everywhere circuit lower bounds for NP and cryptographic consequences. Its objects are sampler-described/implicit truth tables and its theorem is assumption-dependent; it neither gives an assumption-free result nor the explicit truth-table Gap-MCSP bound O-1. The paper is relevant to the hard-instance-generation and proof-complexity programs, but does not change the active dependency DAG.

Adjacent work by Goldberg and Kabanets (June 2025), [*Witness Encryption and NP-hardness of Learning*](https://eccc.weizmann.ac.il/report/2025/070/download), proves unconditional NP-hardness for a semi-proper PAC learning task for circuits (the learner may use a slightly larger circuit class) and characterizes certain CGL hardness reductions through witness encryption. This is an algorithmic hardness result for a sampler/distribution learning problem, not an unrestricted lower bound for explicit Gap-MCSP. **Transfer audit (inference):** a sampler gives an implicit description of labels and full support only guarantees that a preimage exists. Extracting each unique label may require solving a search problem over the sampler's random tapes; moreover, if the underlying arity is polynomial in the SAT input length, writing its full truth table costs exponential output. No reduction was found that compresses the arity to logarithmic size while preserving the gap and source-size bound. This is the concrete obstruction recorded as Q26.

The published OPS magnification theorem remains the shortest direct path; its exact stated implication is available in [Theory of Computing](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf).

## Current stopping point for this pass

No proof of P vs NP or new unrestricted lower bound has been found. C-51 is proved and useful as a map of the error-set geometry, but it does not materially lower the unrestricted complexity barrier. The next high-value step is to test whether a circuit-specific algebraic property of the heavy-overlap graph—one that survives arbitrary circuit sharing and negation—can be shown to yield a findable constant-fraction error coordinate. Without such a property, more incidence counting will only repackage O-1.

## C-52 - A universal first contraction is cheap; adaptation is the bottleneck

At exact OPS parameters, a sharpened minimax/majority argument gives Delta_s1(f)>=3/10 for each promised high table. Otherwise a distribution on size-s1 circuits has expected error below 3/10 at every input. A majority of the smallest odd k>=9n samples has pointwise error at most exp(-0.08k) by Hoeffding. Since 0.72>ln 2, union-bounding over 2^n inputs gives a sampled majority equal to f; its size (0.9+o(1))s2<s2, contradiction.

Sample m=O(n) fixed-length descriptions uniformly from the low-circuit class. Let q_x=Pr[D(x)=1]. Averaging the dual margin shows that every high f has some x with Pr[D(x) != f(x)]>=3/10. Hoeffding and a union bound give one sample whose frequencies approximate all N marginals within 3/40. Hardwire the N integer frequencies and maximize empirical disagreement. The resulting nonuniform circuit has O(Nn) gates and returns a point where at least 3/20 of descriptions disagree, for every promised high table. It is one contraction, not a full anti-checker.

For transcripts of length at most k, there are O((k+1)(2N)^(k+1)) residual and next-query events. A sample of O((kn+log(1/eta))/delta^2) approximates all event masses to additive delta. If each residual mass is at least rho, delta=O(gamma*rho) preserves constant-fraction conditional contraction. Below rho, the sample may have no surviving description while the exact version space remains nonempty. This calculation diagnoses the global-sample method; it does not show a rare cell is reachable by the OPS selector and does not constrain other selector architectures.

**Next proof target.** Separate root-profile compression from conditional-tail elimination. Seek a near-linear conditional profile, a circuit-specific tail theorem, or a different universal-selector construction. O-1 is unchanged. Full claim: [C-52 ledger entry](CLAIM_LEDGER.md#c-52---a-near-linear-first-query-selector-from-global-marginals).


## C-53 - Relative range sampling is sharper than additive approximation

The additive union-bound estimate in the first C-52 audit costs $O((kn+\log(1/\eta))/\delta^2)$ to reach additive precision $\delta$. For conditional contraction, use multiplicative Chernoff instead. Across all residual sets and one-more-query disagreement ranges through depth $k$, there are at most $O((k+1)(2N)^{k+1})$ events. Put $\lambda=\gamma\rho/8$. A sample of size
$$
O((kn+\log(1/\eta))/(\gamma\rho))
$$
simultaneously gives relative error at most $1/4$ on every event of mass at least $\lambda$ and empirical mass below $2\lambda$ on every smaller disagreement event. If a residual has mass $r\ge\rho$, a good coordinate has joint error mass at least $\gamma r$. Its empirical score is at least $3\gamma r/4$. Any coordinate with true error mass below $\gamma r/2$ has empirical score at most $5\gamma r/8$ above the cutoff or below $\gamma r/4$ under it. Therefore choosing the empirical maximum still removes at least a $\gamma/2$ fraction of the exact residual. Since all transcript ranges are covered at once, adaptivity is included.

This improves the global-sample construction from inverse-square to inverse-linear dependence on the smallest tracked mass. A polynomial-size sample can track down to inverse-polynomial mass, but constant contractions bring a nonempty residual below that scale after only $O(n)$ rounds. Exact completion by this method requires tracking mass down to $1/|\mathcal H|$, which makes the sample depend on the full, superpolynomial description space. This is method-specific: it is neither an arbitrary-selector lower bound nor a proof that a rare residual is reached on a high input.

**Learning.** Do not stop at the first additive uniform-convergence bound. Match the concentration inequality to the conditional objective: a relative count is enough because the denominator is common to all candidate coordinates, and the dual margin promises one joint score of order $\gamma r$. This saves a factor $1/\rho$ but leaves the final-tail obstruction intact.


## C-54 - The inverse-polynomial sample guarantee ends at a live version space

Every consistent list of $q$ queries can be interpolated by a DNF with one minterm per positive label, size $O(qn)$. Thus for $q=O(n)$, the residual size-$s_1$ version space is certainly nonempty. C-53's sample guarantee for residual mass at least $N^{-a}$ gives a constant-fraction contraction for $O(n)$ rounds; the first time its mass crosses the threshold, the transcript still has only $O(n)$ points and therefore still has a low-circuit interpolant.

For this prefix, the sample size is $O(n^2N^a)$ and direct score unrolling costs $O(N^{1+a}\operatorname{poly}(n))$, which lies below $N^{1+\epsilon}$ for any $\epsilon>a$. This makes a concrete near-linear prefix selector, but it stops before the known interpolation lower bound $\Omega(s_1/n)$ on anti-checker length. The result identifies the limitation of this sampled-greedy architecture, not an obstruction to arbitrary circuits.

**Next move.** Work on continuation past the live residual: sample from the conditional class without paying inverse residual mass, exploit a circuit-specific structure that gives a new progress measure, or lower-bound all such continuations directly. The last option is O-1 itself, not a shortcut.
