# C-437 — A near-maximum source gives a transfer window, but no table map

## 1. Literature lead

Ren and Williams prove that there is a language/function in `E^{prMA}/1` requiring Boolean circuits of size `Ω(2^m/m)` on infinitely many (in the theorem, near-maximum-hard) input lengths `m`. Their construction uses an iterative win-win argument, Range Avoidance, PCPs, bounded-round NP queries, and a smart promise-MA oracle; all oracle queries in the construction satisfy the oracle promise. See the primary [ECCC TR26-118](https://eccc.weizmann.ac.il/report/2026/118/) and [arXiv version](https://arxiv.org/abs/2607.09963).

Unlike Rao's matching theorem, this lower bound is against unrestricted Boolean circuits. It therefore avoids the monotonicity mismatch from C-436. It still needs a promise-preserving map to the explicit OPS truth-table input, and the source's `prMA` computation does not itself disappear under composition.

## 2. Explicit transfer mechanism and theorem

Fix a source function `L_m:{0,1}^m->{0,1}` with `CC(L_m) >= h(m)` on an infinite set `I`, where `h(m)=a*2^m/m` for a fixed `a>0`. For a fixed OPS parameter `beta`, suppose there is a map

```text
Gamma_m : {0,1}^m -> {0,1}^{N_m},     N_m = 2^{n_m},
```

computed by a fan-in-two multi-output circuit of `R_m` gates, and a postprocessor of `B_m` gates, such that for every `x`:

```text
L_m(x)=1  =>  CC(Gamma_m(x)) <= N_m^beta/(c n_m),
L_m(x)=0  =>  CC(Gamma_m(x)) > N_m^beta.
```

Assume `N_m -> infinity` along the source-hard lengths. There are no middle-band outputs. If a total OPS separator `C_{N_m}` of size `S_m` exists, the circuit `B_m ∘ C_{N_m} ∘ Gamma_m` computes `L_m` and has at most `R_m+S_m+B_m+O(1)` gates. Hence

```text
CC(L_m) <= R_m + S_m + B_m + O(1).
```

This follows by literal circuit composition and allows arbitrary sharing inside `Gamma_m`, `C_{N_m}`, and the postprocessor. It does not charge wires or description bits as gates.

**Transfer criterion.** If, for infinitely many `m in I`,

```text
R_m + B_m + N_m^(1+epsilon) < a*2^m/m,
```

then no OPS separator family of size `N^(1+epsilon)` can exist at that `beta`. To meet the OPS magnification quantifier, the same fixed `epsilon` must work for every sufficiently small fixed `beta`, with an appropriate reduction for each such `beta`.

This gives two scale windows:

* If `N_m <= m^d` and `R_m+B_m <= m^k` for fixed `d,k`, the composition cost is polynomial in `m`, far below `2^m/m`. Thus a deterministic polynomial-time promise-preserving reduction from this source to the exact explicit GapMCSP promise would rule out `N^(1+epsilon)` separators for its target beta with ample room. To establish the full OPS premise, such a reduction must be available for every sufficiently small fixed beta with one common epsilon.
* If `N_m=2^{alpha m}` and the map circuit cost is `2^{gamma m+o(m)}`, the sufficient exponent condition is `max(gamma, alpha(1+epsilon))<1`. This permits an exponential truth table only when it is subexponential relative to the source's near-maximum lower bound.

## 3. Construction attempt: encode the source computation/history

The first candidate is to turn a source computation or its accepting-history predicate into a truth table `Gamma_m(x)`, hoping that accepting source inputs give succinct tables and rejecting inputs give high-circuit-complexity tables.

This attempt currently fails at both ends:

1. A direct local-history predicate whose table bits are computable by a polynomial-size circuit in `(x,address)` gives `CC(Gamma_m(x))<=poly(m,n)` for every source input. When `N=2^{alpha m}`, this is eventually below `N^beta/(c n)` for every fixed `beta>0`, so all outputs are Low. It cannot encode a NO side.
2. For polynomial `N_m=m^d`, the generic `poly(m)` pointwise generator upper bound need not fit the Low cutoff `m^(d beta)/(c d log m)` when `beta` is sufficiently small, and it gives no lower bound above `m^(d beta)` on the NO side. A near-maximum source lower bound does not imply that an individual generated truth table is hard; that conclusion would require a new reduction theorem.
3. The source algorithm uses a smart `prMA` oracle. If the map uses that oracle, the composed object is an oracle circuit, whereas the source lower bound is for ordinary circuits. The oracle cannot be silently compiled away. A proposed map must either be deterministic at the stated gate cost or give a proved simulation of every oracle answer.
4. A conventional computation tableau large enough to encode the exponential-time source computation is not polynomial length. Simply materializing it does not fit the polynomial-output route, and making it succinct brings back the pointwise-easiness problem above.

These are obstructions to the direct history/table construction, not impossibility theorems for all reductions. The key missing object is now specific: a deterministic (or fully costed, ordinary-circuit-generable) map that makes source YES outputs `N^beta/(c n)`-simple and source NO outputs `>N^beta`-hard, while its *entire* multi-output generator cost remains below `2^m/m`.

**Paired full-promise upper attempt.** The exact Low-description separator remains the only proved unconditional construction in the project record: enumerate `K=2^(O(N^beta))` Low descriptions and compare each candidate table against all N coordinates, for `O(NK)` total gates. It accepts every Low table and rejects every High table. C-437 finds no shared near-linear implementation and does not change this upper bound. The C-435 parity, repeated-block, sparse-check, and global-relation examples remain mandatory counterattacks for any proposed direct gate potential; they do not themselves instantiate the source map above.

## 4. Relation to existing branches and barriers

The composition inequality is the same general resource-accounting principle as C-430, now applied to a source with a much stronger unrestricted-circuit lower bound. It is not a new theorem about separators. The new value is a sharp source/target budget: polynomial-output reductions would be more than strong enough, and subexponential-output reductions have the explicit exponent window above.

The primary ECCC TR26-091 result on implicit MCSP is conditional and takes a sampler circuit as input; it does not supply the explicit table map required here. Hirahara–Ilango's conditional source route (C-430–C-433) likewise remains distinct and misses OPS threshold nesting with its displayed bounds. The locality barrier remains relevant: any construction that secretly gives the separator small fan-in oracle power cannot be treated as an ordinary-circuit transfer.

## 5. Strongest statement and exact effect

**Project-proved statement:** the transfer inequality `CC(L_m)<=R_m+S_m+B_m+O(1)` and the resulting near-maximum source budget criterion.

**Failed construction:** local computation-history truth tables are easy on both source sides at the subexponential table scale; no promise-preserving table map was constructed.

**Frontier unchanged:** ordinary `N-O(N^beta log N)-1` plus C-406's additive refinement; OPS `N^(1+epsilon)` open; exact full-promise separator `O(N*2^(O(N^beta)))`; native `rho>=N-o(N)` separate. C-437 does not prove `P != NP`.

### Primary sources

- Ren and Williams, [Near-Maximum Circuit Lower Bounds for Exponential Time with Merlin-Arthur Queries](https://eccc.weizmann.ac.il/report/2026/118/), ECCC TR26-118, July 2026.
- Oliveira, Pich, Santhanam, [Hardness Magnification near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4.
- Goldberg, Juvekar, Kabanets, [Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions](https://eccc.weizmann.ac.il/report/2026/091/).
- Chen et al., [Beyond Natural Proofs: Hardness Magnification and Locality](https://doi.org/10.1145/3538391).
