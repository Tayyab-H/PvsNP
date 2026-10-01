# C-432 — Edge indexing repairs the HI address encoding, but not the OPS fit

**Result.** The HI reduction can be reparameterized so the input names an edge of the explicit hypergraph by its list index. Its completeness and per-edge soundness proof survive: the NO proof only needs the predictor's guarantee separately for every listed edge. This reduces the edge-address field from `tau log n` bits to `log |E|` bits, with an explicit decoder-gate charge. It does **not** yield the ordinary OPS magnification transfer. The HI YES circuit cutoff remains `s=Theta(n*lambda/(tau log lambda))`; the OPS YES-threshold alone then forces `D >= log2(s)/beta = Omega(tau log n/beta)`, while the certified HI gap factor is only `g=Omega(tau)` (or `g=Omega(log^eta n)` when `tau=log^eta n`). Thus `g>cD` fails for sufficiently small fixed `beta` and large `n`, even if the edge address were free.

This refines C-431: the edge-list codec is not inherently blocked by soundness, but the remaining threshold-scale obstruction is independent of that codec. It is an audited conditional reduction, not a new unconditional lower bound.

**C-433 parameter follow-up.** Once the `poly(n^tau)` edge-membership term is removed, HI's ordinary-polynomial NO residual `poly(n*tau)` and the explicit-list decoder can both be dominated with `lambda=n^(A log tau)`. This improves the cutoff to `log s=Theta(log tau*log n)` while preserving a certified `Omega(tau)` gap. Even this stronger refactor fails the OPS ratio over the published `tau` range; see [C-433](C433_REPARAMETERIZED_HI_GAP_STILL_MISSES_OPS_2026-09-30.md).

## 1. Exact OPS condition

For a truth table on `D` variables, let `N=2^D`. OPS Theorem 1.4 uses

```text
YES: CC(f) <= 2^(beta D)/(cD)
NO:  CC(f) >  2^(beta D),
```

for a universal constant `c>=1` (the proof instantiates `c=10`). Its magnification premise asks for one fixed `epsilon>0` such that every sufficiently small fixed `beta>0` rules out size `N^(1+epsilon)` separators. A source promise with YES cutoff `s` and certified NO cutoff `g*s`, padded to `D` variables, fits only if

```text
c D s <= 2^(beta D) < g s.
```

In particular, `g>cD` and `D >= log2(cDs)/beta >= log2(s)/beta`, so a necessary condition is `g/log2(s)>c/beta`. A single source family intended to work for every sufficiently small fixed `beta` therefore needs its certified `g/log s` ratio to become arbitrarily large (or a beta-dependent family with the corresponding unbounded ratios). This dimension requirement is unaffected by re-encoding coordinates of the source.

## 2. Edge-indexed HI function

Take the explicit `tau`-uniform hypergraph `([n],E)` produced by the HI reduction, and write its edges in a fixed order as `e_0,...,e_(M-1)`, where `M=|E|`. Replace the `tau` vertex names in the function input by one index `j in [M]`. Keep the `tau` randomness coordinates, ciphertext bits, and NIWI proof field. Decode `e_j=(v_1,...,v_tau)` in the fixed order, form the same formula `phi_x`, and define

```text
f_idx(j, r_1,...,r_tau, c_1,...,c_tau, pi)
    = c_1 XOR H(v_1,r_1), if NIWI.Verify(psi OR phi_x,pi)=1;
      0,                 otherwise.
```

Every valid address names a listed edge, so the explicit `e in E` membership test disappears; invalid bit strings `j>=M` are defined to output zero. Randomness and ciphertext coordinates are indexed by the edge's sorted position, which is a bijection from the original vertex-indexed coordinates and preserves their product-uniform distribution. The decoder is a hardwired lookup table. With fan-in-two gates it costs

```text
R_E = O(M log M + M*tau*log n)
```

gates by sharing the equality tests for `j` across the `tau log n` decoded endpoint bits. Circuit constants and description bits are accounted for in the lookup implementation; this is not a zero-cost addressing assumption.

Concretely, compute `delta_j=[input=j]` for each listed index using `O(M log M)` gates, share those flags across all endpoint bits, and OR the flags whose hardwired endpoint bit is 1. One validity OR handles invalid indices. The table of endpoint constants has `O(M*tau*log n)` bits (in addition to the gate topology); these description bits and the time to generate the lookup are separate resources from the ordinary gate count. The composed HI reduction already explicitly outputs E, so writing this decoder and enumerating its shorter indexed truth table stays within its deterministic quasipolynomial-time budget.

## 3. Completeness and soundness proof

**Completeness.** If `E` has a vertex cover `V`, decode `e_j`, select its first vertex in `V`, and use exactly the HI YES circuit: compute the per-vertex generators, form `phi_x`, verify `pi`, and output the corresponding `c_i XOR H(v_i,r_i)`. The only change is the lookup decoder and removal of the membership test. Thus

```text
CC(f_idx) <= O(n*lambda/(tau*log lambda) + tau^3*Q
              + poly(q,tau,|psi|) + R_E).
```

The HI choice `lambda=n^(A*tau)` with sufficiently large constant `A` dominates `R_E` and the lower-order terms, giving the same cutoff scale `s=Theta(n*lambda/(tau log lambda))`. Here `M<=n^(O(log tau))`: the cited hypergraph reduction runs in `n^(O(log tau))` time and explicitly writes its edge list. The lookup gates are therefore within the displayed YES budget after increasing `A` by a fixed amount if needed.

**Soundness.** Fix any edge `e_j`. If a machine/circuit `A` computes `f_idx`, hardcode `j` and run `A`; this gives the original per-edge predictor on inputs for that particular edge with identical randomness, ciphertexts, and proof distribution. Hardcoding costs at most `O(log M)` description bits (and no input-dependent lookup). The HI hybrid argument is pointwise in `e`: for each listed edge, successful prediction implies that some endpoint has the required easy approximation; applying this to every `j` yields a vertex cover, contradicting the NO promise. The added `O(log M)` term is absorbed by the existing polynomial/additive terms in the time-bounded Kolmogorov bound. The proof does not use inputs for tuples outside `E` in its NO direction. Hence the edge-index change preserves the stated conditional soundness, with the same HI gap factor.

This conclusion is specific to a fixed, explicitly enumerated `E`. If the source representation gives only an implicit edge predicate, the index decoder need not be small; that setting is not claimed here.

## 4. Why the improved address does not meet OPS

With `lambda=n^(A*tau)`,

```text
log2(s) = log2(n*lambda/(tau*log lambda)) + O(1)
        = (A*tau+1)*log2(n) - O(log(tau^2*log n))
        = Theta(tau*log n).
```

So even an ideal codec making the edge-address field zero bits must use

```text
D >= log2(s)/beta = Omega(tau*log n/beta).
```

HI's displayed circuit gap guarantee is proportional to `tau`; with `tau=log^eta n`, the growing-factor remark gives a certified factor at least a constant multiple of `log^eta n`, while `log s=Theta(log^(1+eta)n)`. Choose `g_cert` at that displayed order, no larger than the theorem's coefficient. Then `g_cert/(cD)=O(beta/log n)`, which tends to zero for every fixed `beta`. The necessary condition `g>cD` therefore is not met by the cited guarantee. This does not prove that the true NO complexity has no stronger lower bound; it proves the cited bound and YES cutoff do not establish one.

The failed transfer mechanism has now changed twice for distinct reasons: C-430 identified the tuple-address width; C-432 removes that width and shows the remaining obstacle is the logarithm of the YES circuit cutoff itself. Further changes to edge coding alone are not a productive next step. A viable HI-based route would have to lower `log s` to `o(g)` with enough margin to handle every small fixed `beta`, or prove a substantially larger ordinary-circuit gap.

## 5. Paired full-promise separator attempt

For the full OPS promise, enumerate all `K=2^(O(s1 log(s1+D)))=2^(O(N^beta))` descriptions of circuits of size at most `s1`; compare each candidate truth table with all `N` input bits; OR the equality flags. This is a valid separator for every promised YES and NO instance, of ordinary total size `O(N*2^(O(N^beta)))`. The compressed HI reduction gives no shortcut for this universal table-family test. No near-linear full-promise separator or native cover is constructed here.

## 6. Model, originality, and frontier

- The proved comparison is for ordinary fan-in-two **total gates**, including the edge decoder and all composition work. No paid-AND-state, OR-only, wire, description-length, runtime, or native cyclic-fusion lower bound follows.
- The edge-index construction is a project-level reparameterization of HI's published function. It adds no new assumption: Theorem V.7 still uses subexponentially secure NIWIs for SAT, `coNP` not contained in `i.o.NSIZE(2^{n^epsilon})` for some constant `epsilon>0`, and `P^NP/poly` not contained in `i.o.SIZE(delta*2^n/n)` for some constant `delta>0` (with HI's stated corollary/case analysis available separately).
- This does not bypass or strengthen the Chen et al. locality barrier. It is a global, source-specific encoding audit.
- Parity, repeated-block equality, sparse parity checks with linear total incidence, and simple global block relations still admit `O(N)` shared readouts; they refute incidence charging only, not the promise problem.

**Strongest proved statement:** the explicit-edge HI reduction admits a soundness-preserving index encoding with `log |E|` address bits and an explicit `O(|E| log |E|+|E| tau log n)` decoder, but this does not lower the HI YES cutoff's logarithmic scale or satisfy the OPS gap-to-dimension condition.

**Quantitative frontier: unchanged.** Ordinary `S_sep >= N-O(N^beta log N)-1` plus C-406's additive refinement; OPS `N^(1+epsilon)` remains open; exact full-promise separator `O(N*2^(O(N^beta)))`; native `rho_GapMCSP>=N-o(N)` separate.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and Section 4.1.
- Hirahara and Ilango, [*NP-hardness of the Minimum Circuit Size Problem from Well-Studied Assumptions* (FOCS 2025)](https://www.rahulilango.com/papers/MCSP-Proceedings-2025.pdf), Theorem III.6, Section V-A, Lemmas V.2–V.5, Theorem V.7, and Remark V.8.
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://eccc.weizmann.ac.il/report/2019/168/download/), for the method-specific locality barrier.
