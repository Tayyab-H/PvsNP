# C-431 — The OPS low-threshold scale dominates address encoding

**Result.** A stronger obstruction to the direct Hirahara–Ilango transfer follows from the YES circuit size alone. Even if the target truth-table input encoding could shrink, fitting its selected YES cutoff under OPS forces `D = Omega(tau log n / beta)`. The displayed soundness bound gives a `tau`-scale gap guarantee (with a growing polylogarithmic variant in Remark V.8), and does not establish the `g>cD` ratio required at this dimension. An edge-address codec alone therefore cannot fix the current parameter match. This is a transfer audit, not a universal reduction barrier or a new OPS lower bound.

## 1. Exact OPS requirement

Let the target function have `D` input variables and truth-table length `N=2^D`. OPS Theorem 1.4 states a universal constant `c>=1` and thresholds

```text
YES: CC(f) <= 2^(beta D)/(cD)
NO:  CC(f) > 2^(beta D).
```

Its proof explicitly uses `c=10`. The magnification quantifier is one fixed `epsilon>0` such that for every sufficiently small fixed `beta>0`, this promise is outside `Circuit[N^(1+epsilon)]`.

For a source promise with YES `CC<=s` and certified NO `CC>g*s`, ignored-variable padding to `D` variables preserves the complexity. Nesting the thresholds requires

```text
c D s <= 2^(beta D) < g s,
```

which implies `g>cD` and

```text
D >= log2(c D s)/beta >= log2(s)/beta.
```

This lower bound on `D` comes from the OPS YES threshold; it is independent of how compactly the original source truth table is encoded.

## 2. Apply the scale bound to the HI reduction

In the HI parameterization, the YES circuit bound is set to

```text
s_HI := Theta(n lambda / (tau log lambda)),     lambda = n^(a tau)
```

for a sufficiently large constant `a`. Hence, for growing `n` and admissible `tau>=constant`,

```text
log2(s_HI) = a tau log2(n) - O(log(tau log lambda)) + O(log n)
        = Theta(tau log n).
```

The padding-fit condition therefore forces

```text
D >= Omega(tau log n / beta).
```

The soundness analysis certifies a circuit-size ratio `g=Omega(tau)` (Remark V.8 obtains a growing polylogarithmic factor by taking `tau` to grow polylogarithmically). It does not establish the `g>cD` needed here: using this YES cutoff requires a certified ratio on the `tau log n / beta` scale. The old edge-coordinate argument independently gave `D >= Omega(tau log(n/tau))`; this new calculation shows that compressing that coordinate alone leaves a threshold-fit obstruction through `s_HI`.

Careful scope: this does not upper-bound the true NO circuit complexity or show no stronger soundness proof is possible. It proves that the displayed YES upper bound and displayed `tau`-scale gap do not certify an OPS-compatible threshold nesting, even after arbitrary lossless address re-encoding.

## 3. Attack the re-encoding idea

**Edge index.** If the function is redefined only on listed edges, an input could name an edge by an index in `E`, using `ceil(log2 |E|)` bits, and the edge tuple could be hardwired and decoded. This can reduce the explicit edge field when `|E| << n^tau`. If the HI YES circuit threshold remains `s_HI`, it does not change the lower bound `D>=log2(s_HI)/beta`. It also changes the function and its soundness proof: the existing reduction defines the input edge over `[n]^tau` and relies on its stated all-edge behavior. A list-index version needs a fresh proof that every NO edge is still represented and that the decoding/verification circuit stays within the YES bound.

**Seed-compress ciphertext randomness.** Each edge input also includes `tau` independent-looking indices `r_v in [lambda']`, with `lambda' <= lambda^(O(tau^2))`, plus ciphertext bits and an NIWI proof string. Replacing all indices by a short seed would restrict the inputs to a pseudorandom subset. The existing soundness proof evaluates an arbitrary circuit on uniformly sampled encryption randomness; it does not establish security against the correlated seed distribution. A seed generator secure against the relevant nonuniform circuits and compatible with every per-edge hybrid is a new cryptographic lemma, not a free codec. Even if obtained, it must also preserve the NIWI proof coordinate and the OPS fit inequality in Section 1.

These are counterattacks to the address-width explanation, not counterexamples to the HI theorem. The decisive transfer deficit currently survives either attack through the required low threshold.

**C-432 follow-up.** For an explicitly listed hypergraph, the edge-index proposal can in fact be made soundness-preserving: hardcode a list index and apply the original pointwise-in-each-edge hybrid argument. The resulting decoder cost is charged in the YES circuit. This repairs the codec concern but leaves `s_HI` at the same scale, so it does not change the threshold obstruction proved here; see C-432 for the full construction and proof.

## 4. Shared computation and named construction countertests

The safe composition accounting remains: if a source predicate is computed from `t` promised tables generated with `R` total gates, an arbitrary `S`-gate separator, and a `b`-gate postprocessor, then a source circuit of size at most `R+tS+b` exists. If a proved source lower bound is `H`, then `S >= (H-R-b)/t`. This does not assume a circuit topology or forbid reuse. To contradict separators of size `N^(1+epsilon)`, one needs `H>R+b+tN^(1+epsilon)`; neither source route audited in C-430 supplies that inequality in the ordinary model.

The cheapest shared computations remain counterexamples to local incidence charges: parity uses `O(N)` AND/OR/NOT gates; repeated-block equality uses `O(N)`; sparse parity-check systems with `O(N)` total incidences use `O(N)`; copy/complement and fixed simple block relations cost `O(N+R)`. None decides full Gap-MCSP or refutes either published reduction.

## 5. Paired full-promise separator attempt

Enumerate the `K=2^(O(s1 log(s1+D)))=2^(O(N^beta))` descriptions of size-`s1` circuits, compare each candidate against all `N` input bits, and OR the equality flags. This is a correct separator on every promised YES and NO input and costs `O(NK)=O(N*2^(O(N^beta)))` ordinary total gates. A prefix trie shares matching prefixes, but has at most `sum_{j=0}^N min(2^j,K)=O(NK)` nodes in the general bound; no structural compression for the entire Low-circuit family was proved. Repeated-block and other globally simple low families can have `O(N)` specialized recognizers, so description count alone is not a lower bound on separator cost.

## 6. Resource accounting, barriers, and frontier

The attempted lower bound counts ordinary fan-in-two total gates. The shared-gate composition lemma concerns the complete composed DAG. It proves no paid-AND-state, OR-operation, wire, circuit-description, construction-runtime, or native cyclic-fusion lower bound. The HIR oracle route from C-430 remains a separate failure of generic de-oracling: an `r=1+10k^2 n`-bit oracle admits a generic mux-tree compilation of `O(2^r)` gates, but this is not a lower bound for that structured oracle. The Chen et al. locality barrier remains method-specific; this cycle neither bypasses nor strengthens it.

**Strongest proved statement:** OPS threshold fitting requires `g>cD` and `D>=log2(cDs)/beta`. For the HI displayed YES cutoff `s_HI`, this demands `D=Omega(tau log n/beta)`, while the cited proof displays a `tau`-scale gap guarantee; no direct/padded OPS transfer follows from these bounds.

**Quantitative frontier: unchanged.** The ordinary lower bound remains `S_sep >= N-O(N^beta log N)-1` plus C-406's additive logarithmic refinement. The OPS `N^(1+epsilon)` target remains open. The exact unconditional full-promise separator remains `O(N*2^(O(N^beta)))`. Native `rho_GapMCSP>=N-o(N)` remains separate.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and Section 4.1.
- Hirahara and Ilango, [*NP-hardness of the Minimum Circuit Size Problem from Well-Studied Assumptions* (FOCS 2025)](https://www.rahulilango.com/papers/MCSP-Proceedings-2025.pdf), Lemmas V.2–V.3, Theorem V.7, Remark V.8.
- Huang, Ilango, and Ren, [*NP-Hardness of Approximating Meta-Complexity: A Cryptographic Approach* (ECCC TR23-046)](https://eccc.weizmann.ac.il/report/2023/046/download), Theorems 4.1 and 4.5; transfer audit in C-430.
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://eccc.weizmann.ac.il/report/2019/168/download/).
