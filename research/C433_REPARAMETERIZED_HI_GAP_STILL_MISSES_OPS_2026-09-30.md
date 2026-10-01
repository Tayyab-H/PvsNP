# C-433 — Reindexing lets HI lower its scale, but the certified gap still misses OPS

**Result.** Combine C-432's edge-list index with a retuning of HI's amplification parameter. The original YES proof pays `poly(n^tau)` gates to test `e in E`; an index into the explicit edge list replaces that term by a shared decoder of `O(M log M+M tau log n)` gates, where `M=|E|<=n^(C log tau)` for the cited hypergraph reduction. The NO proof's additive loss is only `poly(n tau)` (ordinary polynomial, not `poly(n^tau)`). Therefore, for a sufficiently large fixed `A`, the published HI analysis supports `lambda=n^(A log tau)` rather than `n^(A tau)`, while retaining its certified factor `g=Omega(tau)`.

This improves the HI YES cutoff from `log s=Theta(tau log n)` to `log s=Theta(log tau log n)`. It is a real conditional parameter improvement. It still cannot meet OPS: Theorem III.6 allows `gamma<tau<=(log n)^(1/gamma)` for universal `gamma>=1`, so the best certified ratio satisfies

```text
g / (cD) <= O(beta * tau/(log tau * log n))
         <= O(beta / (log(n)^(1-1/gamma) * log log n)) = o(1).
```

The OPS fit therefore still fails for every fixed `beta>0` at large `n`. This is already an optimistic fit: the actual target dimension `D` must also be at least the number of input variables of the indexed HI function, including the NIWI proof field. That can only increase the required dimension and strengthen the mismatch. This is not an upper bound on the true NO circuit complexity.

## 1. Parameters and explicit edge decoder

The HI source reduction from SAT to Gap-`tau`-Uniform Vertex Cover runs in `n^(O(log tau))` time and writes an explicit edge list. Hence its output has `M<=n^(C log tau)` edges for a universal constant `C`. Use C-432's indexed function: input `j in [M]`, decode `e_j`, and default invalid indices to zero. Its ordinary fan-in-two decoder size is

```text
R_E = O(M log M + M*tau*log n) = n^(O(log tau))*polylog(n).
```

This cost includes shared index-equality tests. Its hardwired endpoint list occupies `O(M*tau*log n)` description bits; writing the source list and decoder is part of reduction time, not an uncharged gate operation. Per-edge soundness is preserved as proved in C-432.

## 2. Why the smaller lambda is allowed by the displayed proof

The source hardness theorem's exact range is `gamma_0 < tau <= (log n)^(1/gamma_0)` for its universal constant `gamma_0>=1`. Set the integer security parameter `lambda=ceil(n^(A log_2 tau))` for a sufficiently large fixed `A`. The exponent `A` is chosen once to dominate both the fixed degree of the residual `poly(n*tau)` terms and the edge-list exponent `C log_2 tau`. As in HI's footnote 8, select `n` along the source hard-function subsequence so `2^(m-1)<=n*lambda<=2^m`; integer rounding changes this scale only by a constant factor. Since `tau>gamma_0>=1`, integer `tau>=2`, and this choice also satisfies `n<=lambda<=2^n` for sufficiently large `n` in the allowed range.

**YES side.** In Lemma V.2, step 1 is the only term `poly(n^tau)`: it tests membership in `E` over the full tuple domain `[n]^tau`. The indexed function removes this test. The remaining displayed costs are `O(tau^3 Q)`, `poly(n)` / `poly(q,tau)` verifier and selection work, and

```text
O(OPT*lambda / log(OPT*lambda)),    OPT <= gamma*n/tau.
```

The decoder `R_E` is dominated by the cover term when `A>C` with slack. The ordinary-polynomial `poly(n*tau)` terms are also dominated after increasing `A`. Since `Q=2^m/m^5=Theta(n*lambda/m^5)`, the ratio of `tau^3 Q` to the cover term is `O(tau^4/m^4)=o(1)`, because `m=Theta((1+log tau)log n)` and `tau<=log n`. Thus the indexed YES circuit has cutoff

```text
s = O(n*lambda / (tau*log(n*lambda))).
```

In particular,

```text
log s = Theta((1 + A*log tau)*log n) = Theta(log tau*log n).
```

**NO side.** HI Lemma V.3 subtracts `4*sqrt(2 gamma/tau)*n*lambda + poly(n*tau)` from the source `Kt` lower bound `delta*n*lambda`. Choose `tau` above the same constant hardness threshold as HI and increase `A` so `n*lambda` dominates the fixed-degree `poly(n*tau)` loss. Then the bound remains `Kt(f_{psi,E})>=Omega(n*lambda)`, and the same conversion used in Theorem V.7 gives

```text
CC(f_{psi,E}) >= Omega(n*lambda / log(n*lambda)).
```

Compared with `s`, this certifies a multiplicative factor `g=Omega(tau)`; `log(lambda)/log(n*lambda)` is bounded below by a positive constant for `tau>=2` and fixed `A`. For each edge, the index `j` is included in the predictor's program description, costing `O(log M)` bits. All extraction programs still use the same indexed circuit as their oracle. This increment is absorbed in HI's existing `poly(n*tau)` correction; no edge-dependent oracle or free input decoder is assumed. The HI assumptions are unchanged.

These term-by-term changes are the reason this is stronger than merely shortening the address: the YES membership term is eliminated, while the separate NO-side remainder is still dominated by the new lambda choice. A generic edge codec without the explicit-list bound would not justify the retuning.

**Quantified conditional statement.** Assume HI's three hypotheses: subexponentially secure NIWIs for SAT; `coNP` not contained in `i.o.NSIZE(2^(n^epsilon))` for some fixed `epsilon>0`; and `P^NP/poly` not contained in `i.o.SIZE(delta*2^n/n)` for some fixed `delta>0`. Let `gamma_0` be the universal constant in Theorem III.6, and let `d` bound the fixed-degree `poly(n*tau)` correction. For each admissible `gamma_0<tau<=(log n)^(1/gamma_0)`, with `tau` also above the constant needed to make the square-root soundness loss smaller than `delta`, and for `n` selected along HI's hard-function subsequence, choose one fixed `A` larger than the edge-list exponent and `d`. Then the indexed HI output satisfies: every unsatisfiable `psi` on a YES hypergraph gives `CC(f_idx)<=O(n*lambda/(tau log(n*lambda)))`; on a NO hypergraph, HI's reduction supplies an unsatisfiable `psi` with `CC(f_idx)>=Omega(n*lambda/log(n*lambda))`. The reduction remains deterministic quasipolynomial time. The constants may depend on the fixed HI assumptions, but not on `n`; the statement is conditional and source-specific.

## 3. OPS fit after the reparameterization

OPS Theorem 1.4 requires

```text
YES: CC(f) <= 2^(beta D)/(cD)
NO:  CC(f) >  2^(beta D),
```

for universal `c>=1` (the proof uses `c=10`), and requires one fixed `epsilon>0` to work for every sufficiently small fixed `beta>0`. Nesting a source YES cutoff `s` and certified NO factor `g` by ignored-variable padding requires `g>cD` and `D>=log_2(s)/beta`.

Take `g_cert` to be the multiplicative factor of order `tau` actually supplied by the displayed HI lower-bound calculation; this is a certified guarantee, not an upper bound on the true NO complexity. For the improved parameters,

```text
g_cert/(cD) <= O(beta*tau/(log tau*log n)).
```

The hypergraph-hardness range has `gamma_0<tau<= (log n)^(1/gamma_0)` with `gamma_0>=1`. Uniformly over the admissible range, `tau/(log tau*log n)=o(1)`: at the largest allowed `tau`, it is at most `O(1/(log(n)^(1-1/gamma_0)*log log n))`, which is `O(1/log log n)` when `gamma_0=1`; smaller `tau` only decreases the ratio once `tau>=2`. Thus no fixed beta makes the displayed HI gap fit the OPS thresholds asymptotically. Larger true NO complexity is not ruled out; this is the limit of the certified lower bound.

The reduction still has quasipolynomial construction time. With `lambda=n^(A log tau)`, `log(n*lambda)=O(log n log tau)`; the amplified seed width obeys `log(lambda')=O(tau^2 log(lambda))=polylog(n)`, as do `q`, the selected formula size `|psi|`, and the proof field. HI Proposition V.1's time `(n*lambda)^(O(tau^2))*2^poly(|psi|*q*tau)` is therefore `2^polylog(n)` throughout the allowed `tau` range. The output truth-table input width is also `polylog(n)`, so the table generation remains within the same quasipolynomial regime.

## 4. The mechanism and its attack surface

The controlled resource is an ordinary fan-in-two circuit's **total gates**, including the edge decoder. Given one common circuit `C` for the indexed function, specialize it to each valid edge by putting that edge's index in the predictor description. HI's hybrid then says: if `C` predicts the promised output with high success, each edge has an endpoint whose amplified key is time-bounded-Kolmogorov-simple relative to the same oracle `C`. Those vertices form a cover of every edge. A NO hypergraph has no cover smaller than `n(1-gamma_0/tau)`, so almost all vertex keys would be simple relative to `C`; error correction and the HI hard-source assumption then force a short program using oracle `C` to encode `Omega(n*lambda)` bits of the source, contradicting its time-bounded Kolmogorov lower bound unless the circuit description is long. An `S`-gate fan-in-two circuit has a description of `O(S log(S+D))` bits and can be evaluated within HI's chosen time bound; hence `S=Omega(n*lambda/log(n*lambda))`. This separates description length from gate count. Arbitrary fanout and reuse are allowed throughout: this is the published HI information-extraction argument, with each per-edge index charged in its extractor description and the YES-side table lookup charged in gates.

The mechanism is specific to this cryptographic reduction. The requested shared-readout attacks all defeat generic incidence or anchor charges:

- `PARITY(x_1,...,x_N)` has a fan-in-two implementation with `O(N)` gates (each XOR uses constant many AND/OR/NOT gates).
- For `q` repeated blocks of `r` bits, testing whether all blocks equal the first uses `O(qr)=O(N)` gates, sharing the reference bits.
- A sparse parity-check system with `O(N)` total nonzero entries computes every syndrome bit and checks that all are zero in `O(N)` gates; row overlaps can be reused.
- Blocks obtained from one seed block by copy, complement, permutation, or a fixed sparse linear recurrence can be checked coordinatewise in `O(N)` gates while reusing intermediate bits.

These constructions refute incidence-count and independent-witness charges, but they do not refute HI's key-extraction mechanism: they lack its per-edge hard-source assumption and conditional key structure. Nor do they yield a full-promise GapMCSP separator. They are counterexamples to a broader mechanism, not to the HI reduction or the lower-bound program.

## 5. Paired separator attempt, model, and frontier

The full-promise separator enumerates all `K=2^(O(s1 log(s1+D)))=2^(O(N^beta))` circuits of size at most `s1`, compares each against all `N` truth-table bits, and ORs the equality flags. It handles every promised YES and NO input in `O(N*2^(O(N^beta)))` ordinary total gates: a promised YES matches one candidate; a promised NO matches none. Neither the indexed HI construction nor the parameter change yields a near-linear separator or a native cover.

The comparison counts ordinary fan-in-two **total gates**, including the edge decoder. It proves no paid-AND-state, OR-only, wire, description-length, uniform-runtime, or cyclic-fusion lower bound. Parity, repeated-block equality, sparse parity checks with linear incidence, and simple global block relations still have `O(N)` shared readouts; these defeat incidence charges, not the HI reduction or full GapMCSP.

**Assumptions and scope.** This is a conditional reparameterization of HI under its original NIWI, coNP nondeterministic-circuit, and `P^NP/poly` assumptions, plus the explicit edge-list bound from Theorem III.6. It does not bypass or strengthen the Chen et al. locality barrier: that barrier concerns specified local-oracle simulations of weak lower-bound techniques, whereas this cycle gives no lower bound against arbitrary separators and supplies no new nonlocal invariant. It is not an unconditional circuit lower bound or a claim of priority over the published HI construction.

**Strongest proved statement:** the explicit-list HI reduction can use `lambda=n^(A log tau)` and certify `YES CC<=O(n*lambda/(tau log(n*lambda)))` versus `NO CC>=Omega(n*lambda/log(n*lambda))`, giving a factor `Omega(tau)` while reducing `log s` to `Theta(log tau log n)`. The OPS fit remains impossible from these certified parameters because `tau/log s=o(1)` over the published hypergraph-hardness range.

**Quantitative frontier: unchanged.** Ordinary `S_sep>=N-O(N^beta log N)-1` plus C-406's additive refinement; OPS `N^(1+epsilon)` remains open; exact full-promise separator `O(N*2^(O(N^beta)))`; native `rho_GapMCSP>=N-o(N)` separate.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and Section 4.1.
- Hirahara and Ilango, [*NP-hardness of the Minimum Circuit Size Problem from Well-Studied Assumptions* (FOCS 2025)](https://www.rahulilango.com/papers/MCSP-Proceedings-2025.pdf), Theorem III.6, Section V-A, Lemmas V.2–V.5, and Theorem V.7. Page 10 displays the `poly(n^tau)` YES membership term; page 11 displays the `poly(n*tau)` additive NO loss.
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://eccc.weizmann.ac.il/report/2019/168/download/), for the technique-specific locality barrier.
