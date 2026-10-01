# C-449 — Conditional implicit MCSP hardness does not transfer through table expansion

**Date:** 1 October 2026  
**Status:** primary-literature transfer audit with a proved generic materialization bound. The candidate does not improve the ordinary Gap-MCSP frontier.

## 1. Candidate and source theorem

Goldberg, Juvekar, and Kabanets, *Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions* (ECCC TR26-091, June 2026), prove conditional NP-hardness for an implicit version of Gap-MCSP. The instance is a circuit `E` sampling labeled examples `(x,f_E(x))`, with full support over `x`; the object being classified is the sampler description, not the explicit truth table. Their Theorem 40 assumes subexponentially secure iO, subexponentially secure NIWI, and no infinitely-often subexponentially optimal proof system. Under related assumptions, the paper also proves `NP ⊄ io-SIZE[2^{n^{o(1)}}]`; its displayed hard-function construction gives a lower bound `2^{n^ν}` for some `ν>0` when the function's address width is at most polynomial in `n`. This is a subexponential-in-address guarantee, not a fixed-exponential one.

Primary source: [ECCC TR26-091](https://eccc.weizmann.ac.il/report/2026/091/download/), especially Definitions 24–26, Theorem 40, and Lemma 29.

## 2. Exact attempted map to explicit tables

Let the source input be `φ` of length `m`. Suppose its reduction produces a sampler `E_φ` with `k(m)`-bit first coordinate, `q(m)` random seed bits, and a circuit of size `a(m)`. On promised instances, `E_φ` defines a total function `f_φ` and has full support in the first coordinate. Define the explicit table

```text
T_φ[x] = OR_{r∈{0,1}^{q(m)}} [ E_φ(r) = (x,1) ],   x∈{0,1}^{k(m)}.
```

Consistency and full support make this exactly `f_φ(x)`. For a deterministic uniform reduction, compile the circuit generating `E_φ`, then unroll the sampler and equality tests independently for every `x`. This gives a valid shared multi-output table generator with

```text
N = 2^k,
g_table(m) = O(2^{k+q} · poly(a,m,k,q))
```

gates. This is a constructive upper bound, not a lower bound on all possible table generators. If `f_φ` is easy, its table is Low once `CC(f_φ)≤N^β/(c k)`. To land in the required High set, however, the no-case must prove `CC(f_φ)>2^{βk}` for a fixed `β>0`.

## 3. Why the transfer currently fails

The implicit theorem's no-case rules out circuits of size `g(s(k))` for source-paper subexponential `g` (that is, `g(t)≤2^{t^{1/c}}` for every constant `c`). Because `s` is polynomial in `k`, the guaranteed size scale remains `2^{k^{o(1)}}`. Since `E_φ` has full support and defines a total function, a circuit computing `f_φ` exactly would achieve accuracy `1`; the no-case therefore implies `CC(f_φ)>g(s(k))`, but only at that scale. It does not certify the fixed-exponential bound `2^{βk}` required to prove `T_φ∈H`. For Lemma 29, if its hard function has address width `k(n)≤n^d` and circuit lower bound `2^{n^ν}` with `ν<1`, then `n≥k^{1/d}` translates the stated lower bound into `CC(f)≥2^{k^{ν/d}}`. This is a stretched-exponential lower-bound guarantee with exponent below `1`; in truth-table length `N=2^k`, that bound is `N^{k^{ν/d-1}}=N^{o(1)}`, below `N^β` for every fixed `β>0`. The paper does not establish a fixed-exponential-in-`k` bound. Neither result supplies the actual explicit-table High endpoint.

Even if a stronger endpoint were obtained, composition with a Gap-MCSP separator of size `S` only gives a source circuit of size `S+g_table`. A source lower bound must exceed `g_table+N^{1+ε}`. The published implicit-instance hardness theorem does not supply this source circuit lower bound, and the direct truth-table materializer costs exponential in the sampler seed/address lengths. Thus its NP-hardness implication cannot be substituted for the missing source-map margin.

The reduction also relies on existence assumptions about cryptographic primitives and optimal proof systems; the paper explicitly describes aspects of the half-Levin reduction as nonconstructive. This is a separate obstacle to treating it as an unconditional explicit reduction, but the endpoint and cost mismatches already suffice to block the transfer.

## 4. Strongest proved statement and scope

**Proved here.** If a total full-support sampler has seed length `q` and address width `k`, exhaustive seed aggregation computes its explicit truth table with at most `O(2^{k+q} poly(size(E),k,q))` gates. On YES instances this table inherits the sampler-defined function's circuit upper bound. The stated implicit hardness results do not prove that this table's circuit complexity exceeds `2^{βk}`; nor do they give a source lower bound exceeding the cost of this materializer plus `N^{1+ε}`.

**Disposition.** Retire the direct implicit-to-explicit expansion route at its present theorem and cost. Reopen it only with both (i) a proof that every no-instance materializes to a table of complexity `>2^{βk}` and (ii) an all-input source hardness margin larger than the complete shared generator plus `N^{1+ε}`. This is a failed transfer, not a counterexample to Gap-MCSP or a universal impossibility theorem.

## 5. Paired upper-bound check and frontier

No near-linear full-promise separator was constructed. The exact full-promise enumeration remains `O(N·2^{O(N^β)})`; this implicit source map does not improve it. The ordinary circuit lower bound remains `N-O(N^β log N)-1` with the C-406 logarithmic refinement. The comparator lower bound and native `ρ` frontier remain separate measures. OPS's common-fixed-`ε` target and P-vs-NP remain open.
