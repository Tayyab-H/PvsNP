# C-455 — the cryptographic route has a uniformity fork

**Date:** 1 October 2026  
**Question:** Can the full-table PRG/PRF mechanism from C-409 be weakened to a standard cryptographic assumption without merely assuming the desired nonuniform separation?  
**Result:** The quantifiers split cleanly. Security against the nonuniform circuit family that would be the OPS separator rules out that separator, but sufficiently strong nonuniform OWF/PRF security already implies `NP not subseteq P/poly`. Uniform security does not see an arbitrary nonuniform separator. This closes the “weaker crypto assumption” obligation as a route to an independent proof; it does not change any unconditional bound.

## 1. Exact model and a search-to-inversion lemma

Let `f_n:{0,1}^n -> {0,1}^n` be polynomial-time computable. Define the NP language

```text
PREFIX_f = {(y,p) : some x in {0,1}^n extends p and f_n(x)=y}.
```

The pair `(y,p)` is padded and length-delimited, so each relevant input has length `O(n)`. If `NP subseteq P/poly`, `PREFIX_f` has a polynomial-size circuit family. On input `y=f_n(x)`, query that circuit successively on prefixes: choose bit 0 when the current prefix followed by 0 is extendable, and choose bit 1 otherwise. At each step some extension exists. After `n` steps the resulting string `x'` satisfies `f_n(x')=y`.

Unrolling the `n` circuit calls gives a polynomial-size **nonuniform inverter**, successful on every image point. Therefore:

> **Proposition (project-derived).** A polynomial-time computable function family that is one-way against nonuniform polynomial-size adversaries implies `NP not subseteq P/poly`.

The proof is exact for length-preserving functions; polynomially related input/output lengths only change padding. A deterministic inverter is a special case of a randomized adversary. This proposition is not a proof that any candidate function is one-way.

If OWF security is only against **uniform** polynomial-time algorithms, the circuit family for `PREFIX_f` cannot be inserted into that security game: it is advice depending on `n`. The same search argument under the stronger assumption `P=NP` uses a uniform decider and does show that a uniform OWF implies `P != NP`. It does not upgrade a uniform OWF premise to `NP not subseteq P/poly`.

## 2. Apply the fork to C-409

For a PRF table on `N=2^n` addresses, any valid Gap-MCSP separator `A_N` is a distinguisher: query all `N` addresses, form the truth table, and run `A_N`. Every generated table in the stated support is Low and is accepted. A uniform random table is High with probability `1-2^{-N+o(N)}` by circuit counting and is rejected. The complete truth-table query interface costs `N` queries; evaluation then costs `CC(A_N)` gates. No circuit-description reconstruction is involved.

The security quantifier decides whether this is a valid contradiction:

| Security premise | Does it cover `A_N`? | What follows |
|---|---|---|
| Nonuniform security against `N^(1+epsilon)`-gate table distinguishers | Yes, by definition | Excludes the OPS separator at those parameters; with OPS quantifiers, implies `NP not subseteq P/poly`. |
| Nonuniform security against polynomial-size adversaries in key length `lambda`, with `N=poly(lambda)` | Yes; `N` queries and `A_N` are polynomial in `lambda` | Already implies `NP not subseteq P/poly`: under that class collapse, MCSP is in NP and has polynomial-size circuits, which supply the distinguisher. This is C-99. |
| Uniform security against uniform polynomial-time distinguishers | Only if `A_N` is uniformly constructible | Does not refute an arbitrary nonuniform OPS separator. |

For C-409's calibration `lambda=n^2`, `N=2^n=2^{sqrt(lambda)}`. Security against nonuniform distinguishers of size `2^(lambda^alpha)` for any fixed `alpha>1/2` also covers, under `NP subseteq P/poly`, the MCSP separator of size `N^d=2^{d sqrt(lambda)}` for every fixed circuit exponent `d`, as well as the `N` queries. Thus this stronger PRF premise independently yields the target class separation even without invoking the particular OPS exponent.

This identifies the precise mistake in trying to “weaken only the cryptography”: weakening to uniform adversaries loses the nonuniform circuit under study; keeping nonuniform adversaries strong enough to cover all polynomial-in-`N` separators already excludes `NP subseteq P/poly`. The C-409 assumption remains a correct conditional implication and useful calibration, but is not an independent route from a weaker, uniform cryptographic premise to the OPS nonuniform lower bound.

## 3. Adversarial checks and paired construction

- The proposed implication never charges support size, witness count, or local constraints. It runs an arbitrary shared separator itself as a distinguisher.
- Parity/affine tables, repeated blocks, sparse parity-check outputs, and simple global block relations fail as candidate PRG distributions: their full-table relations have `O(N polylog N)` shared checkers, as recorded in C-409.
- This is not a counterexample to the conditional PRG theorem. It shows only that these explicit low-table distributions do not meet the required security.
- The paired unconditional full-promise upper remains exact enumeration: enumerate all size-`s1` circuit descriptions and compare each output against all `N` coordinates, for `O(N 2^(O(N^beta)))` gates. No near-linear full-promise separator was constructed. No ordinary-to-native fusion compiler follows from this audit.

## 4. First-principles project synthesis

Across the audited routes, the proof obligations separate into three noninterchangeable quantities:

1. **Semantic endpoints:** every candidate must accept all tables of circuit size at most `s1`, reject every table of size at least `s2`, and may choose freely in between.
2. **Computation:** OPS counts total ordinary AND/OR/NOT gates with unrestricted fan-out. Input support, certificate width, number of low descriptions, communication, and source-map gate count do not by themselves lower-bound reusable gate work. A vector-output map additionally has wires, description, and construction cost.
3. **Strength of the premise:** a uniform algorithmic hardness premise cannot rule out an arbitrary circuit family. A nonuniform premise that can do so may already entail the desired class separation.

This makes the missing result more precise, not smaller: either prove a superlinear total-gate lower bound for **every** codebook-sandwich extension, or give a source reduction with exact Low/High endpoints and a full costed nonuniform interface whose source hardness exceeds generator plus separator plus postprocessor. No new potential with an operation-wise sharing bound and superlinear promise-forced terminal value has been proved. The native `rho` problem remains a separate model; its `N-o(N)` bound does not transfer here.

## 5. Retrospective audit through C-455

The research record now has many concrete route tests. Their common lesson is that they constrain descriptions of a separator or a restricted architecture; OPS instead measures the total gates of its arbitrary shared Boolean DAG.

| Research family | What is actually established | Why it has not crossed the OPS target |
|---|---|---|
| Essential inputs, interpolation, reconvergence | Every extension depends on `N-O(N^beta log N)` table bits; C-406 gives a small additive reconvergence refinement. | Dependence is information/support, not superlinear gate work. |
| Communication, rank, entropy, policy counts | Sharing-safe encodings and exact information ceilings are available. | The relevant ranks/capacities saturate at linear scale, or count low descriptions rather than computation. |
| Certificates, anti-checkers, selectors, witnesses | Semantic anti-checkers can be short; acceptance certificates can be extracted from an evaluated DAG. | A short semantic object need not be output or computed by the decision circuit; middle-band freedom and coNP/`Sigma_2` validation block the transfer. |
| Local reductions and restricted models | The OPS thresholds inherit the published AC0 locality obstruction; formulas, CNFs, and branching programs have separate known lower bounds. | Locality is not arbitrary fan-in-two depth/fan-out, and none of the restricted-model bounds has a proved low-loss compiler for the shared DAG. |
| Native fusion/cyclic closure | The exact native model has `rho>=N-o(N)` and endpoint-realizable counterexamples invalidate blanket wide-seed deletion. | `rho`, paid AND states, OR rules, wires, and total ordinary gates are distinct; a quadratic unrolling is an upper compiler, not a lower-bound transfer. |
| Codes, restrictions, repeated blocks, products, simple extensions | Many candidate subpromises have explicit linear or near-linear recognizers; direct repetition can leave both sides OPS-Low. | A hard trace is not a full-promise separator, and source-map/generator costs can consume the hardness margin. |
| PRF/local-PRG | A small separator is a distinguisher for low tables versus uniform. | Uniformity misses arbitrary advice; nonuniform security strong enough to refute it already implies the target separation. |
| Full-promise algorithms | Exact enumeration is a valid `O(N 2^(O(N^beta)))` separator. | No construction close to `N^(1+o(1))` has been found. |

The strongest correction to the project's earlier instinct is therefore: **we have not found a missing statistic of witnesses, addresses, or constraints that prices the decision circuit.** Repeatedly increasing sample sizes, block counts, or native-state parameters cannot fix that mismatch. What is missing is a theorem about the actual Boolean function on the entire `N`-bit domain, or an endpoint-preserving reduction whose complete circuit cost is lower than a proven hard-source bound. A proof that a circuit “must reconstruct the witness” is not available and is not a valid substitute.

## 6. Research direction that survives the audit

Use two gates-on-the-page checkpoints before investing in a new mechanism:

1. **Direct route:** define an invariant on an arbitrary total fan-in-two AND/OR/NOT DAG. Prove its change under each gate with unrestricted fan-out, then prove the invariant is superlinear for every `L_s1 subseteq F^{-1}(1) subseteq L_{<s2}` extension. If it only counts support, entropy, rectangles, or certificate width, the existing linear ceilings already kill that version.
2. **Reduction route:** give one explicit source family and a multi-output map. Prove every YES image has circuit size at most `s1`, every NO image exceeds `s2`, and `CC(source) > g_map + CC(F) + g_post`. Count map gates separately from output wires, advice/description bits, and runtime. The local AC0 obstruction rules out only the shallow parity architecture; an arbitrary-depth map still needs its own complete proof.

These are proof obligations, not assumed “non-shareability” principles. The current evidence does **not** identify a smaller theorem that would imply the OPS target while avoiding its central difficulty. The most productive next cycle should choose a concrete candidate invariant or map and either prove every obligation or retire it after its strongest sharing attack.

## 7. Frontier and status

- **Proved here:** nonuniform OWF security implies `NP not subseteq P/poly`, by a prefix-search inverter; the uniform/nonuniform distinguisher boundary for C-409 is explicit.
- **Established background:** the OPS magnification parameters and theorem; the full-table local-PRG template used in C-409; C-99's direct PRF-to-class-separation implication.
- **Not established:** any candidate OWF/PRF with the required security; an unconditional OPS separator lower bound; a near-linear full-promise separator; or a transfer to native fusion.
- **Quantitative effect:** none. Ordinary lower bound remains `N-O(N^beta log N)-1` plus C-406's additive refinement; the common-fixed-`epsilon` OPS target remains open; exact full-promise upper remains `O(N 2^(O(N^beta)))`; native `rho>=N-o(N)` remains separate. No P-vs-NP proof.

Primary reference for the magnification quantifiers: Oliveira–Pich–Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf). The local-PRG application and parameter choices are fully stated in [C-409](C409_FULL_TABLE_PSEUDORANDOMNESS_CONDITIONAL_GAPMCSP_2026-09-30.md); the nonuniform-PRF consequence is recorded in C-99.
