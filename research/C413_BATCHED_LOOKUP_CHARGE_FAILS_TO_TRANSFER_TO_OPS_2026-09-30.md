# C-413 - Batched lookup work is measurable, but no OPS separator exposes it

Date: 30 September 2026

**Status:** proved an ordinary total-gate compiler for batched access to a fixed lookup table, and the matching random-table lower bound for one unrestricted lookup. The attempt to force that lookup inside an arbitrary Gap-MCSP separator fails at the promise-preserving embedding step. A recent random-oracle hardness reduction also misses the OPS multiplicative gap and uses oracle-relative circuit complexity. No quantitative frontier changes.

## 1. Exact target

Let `N=2^n`, `s1=N^beta/(10n)`, and `s2=N^beta`. A valid separator accepts every table of ordinary fan-in-two AND/OR/NOT total-gate complexity at most `s1` and rejects every table of complexity at least `s2`; behavior in between is unrestricted. The OPS magnification theorem uses a universal denominator constant `c` and proves its reduction with `c=10`: if one fixed `epsilon>0` rules out `N^(1+epsilon)`-gate separators for every sufficiently small fixed `beta>0`, then `NP` is not in `P/poly`. Thus the required threshold ratio is `s2/s1=10n=10 log_2 N`.

## 2. Candidate mechanism: the cost of a shared finite lookup alphabet

Let `A:{0,1}^{<=L}->{0,1}` be any fixed lookup table, `K=2^{L+1}-1` its number of possible query strings, and let an ordinary circuit of `S` fan-in-two gates produce `Q` query strings `q_1(x),...,q_Q(x)` nonadaptively. There is a circuit with the same input `x` that outputs all `A(q_i(x))` using

```text
S + O((Q+K)(L+log(Q+K)) log^2(Q+K))
```

total AND/OR/NOT gates. The bound is for total gates; it is not a paid-AND, wire, or runtime measure.

**Proof.** Form `Q` query records `(key=q_i(x), type=query, tag=i)` and `K` fixed dictionary records `(key=u, type=dictionary, value=A(u))`, with dictionary records ordered before queries at equal keys. A sorting network orders all `Q+K` records by key. A record has width `O(L+log(Q+1))`. A compare-exchange on two such records costs `O(L+log(Q+1))` fan-in-two gates, including the key comparison and conditional swaps. Batcher sorting uses `O((Q+K)log^2(Q+K))` compare-exchanges. A scan in sorted order carries the last dictionary value forward; each query record then carries `A(key)`. A second sort on tags returns answers to their original output wires. This gives the stated gate bound. If constants are not primitive, all required constants cost an additional `O(K+Q)` gates. Description bits and construction time are separate from this gate count; both are polynomial in the displayed network size.

For a fixed query-dependency depth `d`, an oracle circuit with `q` oracle gates, query length at most `L`, and `S` ordinary gates can therefore be compiled to an ordinary circuit of size

```text
S + O(d(q+K)(L+log(q+K)) log^2(q+K)).
```

At each oracle layer, all currently available query words are batched together. The bound makes no per-query `K` charge and permits unrestricted reuse of every ordinary subcomputation. If layers are unbounded, the factor `d` must be retained.

There is a complementary lower bound for one lookup: by counting fan-in-two circuits, for a uniformly random `A:{0,1}^L->{0,1}`, with probability `1-2^{-Omega(2^L)}` every circuit computing `A` has at least `Omega(2^L/L)` gates. Circuits of size `t` number at most `2^{O(t log(t+L))}`; taking `t=c 2^L/L` for a sufficiently small constant `c` leaves an exponentially small fraction of the `2^{2^L}` tables computable. This is a real ordinary-gate charge for an explicit lookup task. It would be superlinear in `N` if a valid reduction forced a random lookup with `2^L=N^{1+delta}` while spending `o(N^{1+delta}/log N)` gates to construct the lookup inputs.

## 3. Counterconstructions to naive charges

The compiler is also a counterexample to charging `K` gates separately for each query: the same fixed dictionary serves all `Q` lookups, at total cost near-linear in `Q+K` up to logarithms. More generally, all of the requested sharing attacks survive:

- `N` prefix parities have `Theta(N^2)` expanded incidences but one shared XOR chain uses `N-1` XOR gates, or `O(N)` AND/OR/NOT gates.
- Equality of `b` repeated `m`-bit blocks to the first block uses `O(N)` gates for `N=bm` bits, rather than a separate full scan for every constraint.
- A sparse parity-check matrix with `O(N)` nonzero entries has an `O(N)` XOR readout. Its nested-prefix variant can have `Theta(N^2)` expanded incidence and still use one `O(N)` prefix chain.
- If each block is a copy or a shared prefix-parity transform of a base block, compute the base statistics once and compare the `N` positions in `O(N)` gates.

These disprove per-incidence and per-query computation charges. They do not refute a lower bound on a richer, promise-forced global lookup mechanism.

## 4. Transfer attempt and exact failure

The lookup lower bound concerns a circuit whose output is `A(i)` on a freely varying `L`-bit address. A Gap-MCSP separator has only one output bit on an `N`-bit table. To obtain the lookup lower bound from it, one would need an explicit map `Phi(A,i)` such that (i) every `Phi(A,i)` is promised, (ii) its low/high label equals `A(i)`, and (iii) the `N` bits of `Phi(A,i)` can be generated from `(A,i)` by a circuit whose cost is below the lookup lower bound. No such map is known. The naive map picks one fixed low table or one fixed high table according to `A(i)`, but generating that table from an arbitrary `A` already requires computing the same lookup. Supplying the selected bit separately leaves the missing consistency condition `b=A(i)` outside the MCSP instance. Composing a separator with a map that performs the lookup merely pays the target cost before the separator runs. This is the decisive failed implication; no witness, description, or address-reader output is inferred from a separator.

The direct upper attempt remains exact low-circuit enumeration. For `K_low=2^{O(s1 log(s1+n))}=2^{O(N^beta)}` descriptions, test equality with each hardwired `N`-bit truth table and OR the results. This is a valid full-promise separator with `O(N K_low)` total gates, including equality and outer OR gates; it can reject the middle band. Trie and batch-read sharing do not remove the need to distinguish all candidate tables, and no near-linear full-promise construction is obtained.

As a local promise calibration, C-412's `O(N)` Hamming-weight threshold accepts full radius-`Theta(N^beta/n^2)` balls around all tables of weight at most `floor(s1/(8n))`, and rejects every promised NO table. It omits dense low tables such as parity, so it is not a full separator. It remains a strong counterexample to generic neighborhood or incidence charging, not to the full program.

## 5. Literature and quantitative bridge audit

Oliveira-Pich-Santhanam Theorem 1.4 has the quantifiers and thresholds stated above. The locality theorem of Chen, Hirahara, Oliveira, Pich, Rajgopal, and Santhanam rules out certain weak-model locality techniques; C-411's fixed-menu corollary is parameter-specific. Neither constrains arbitrary ordinary total-gate separators.

Ilango's primary ECCC paper proves NP-hardness of an **oracle-circuit** MCSP promise relative to a random oracle. Its Theorem 6 YES circuits have size at most

```text
(1+o(1)) (2 lambda*n*tau + 2 lambda*n/tau)/log n
```

and its NO instances have oracle-circuit size at least

```text
(2 lambda*n*tau + n*lambda/8)/log(2 lambda*n*tau+n*lambda/8).
```

For fixed sufficiently large `tau`, both are `Theta(M/log M)` for output table length `M=4 tau n lambda`; their ratio is a fixed constant approaching `1+1/(16 tau)`, whereas OPS requires the ratio `10 log_2 M`. The theorem's YES witness circuits also use oracle gates, so even compiling them to ordinary gates must be separately charged. Padding by dummy inputs preserves the circuit-complexity values and cannot turn this constant ratio into a logarithmically growing ratio while retaining both thresholds. Thus this strong oracle reduction does not transfer to the requested OPS gap.

The 2026 gate-elimination papers of Carmosino-Dang-Jackman give constructive linear lower bounds for XOR, the multiplexer, and affine dispersers, plus a convergent DeMorgan circuit-rewriting formalization. These are explicit-function lower bounds, not a promise-preserving map from arbitrary Gap-MCSP separators to a hard lookup. The 2025 XOR-simple-extension result puts total XOR extension in P; it closes XOR as a candidate for that particular hardness transfer. MUX extension remains a candidate in that work, but C-400 already shows a linear-size separator for the MUX witness subpromise, so it alone cannot charge the full promise.

These are established results. The batched-lookup compiler and the OPS ratio comparison are project-level derivations, not new lower bounds. The lookup lower bound is standard circuit counting applied to this explicit object. No oracle result is treated as an ordinary-model theorem.

## 6. Exact frontier effect and next mechanism

**Strongest proved statement:** finite shared lookups of query alphabet size `K` and depth `d` can be compiled at the total-gate cost above; a random `L`-bit lookup needs `Omega(2^L/L)` total gates. The intended lower-bound route fails because no promise-preserving embedding makes an arbitrary separator compute that lookup below its cost.

**Quantitative effect:** none. The ordinary lower bound remains `S >= N-O(N^beta log N)-1` with C-406's additive logarithmic refinement. The OPS `N^(1+epsilon)` target remains open. The exact full-promise upper remains `O(N 2^{O(N^beta)})`. Native `rho_GapMCSP >= N-o(N)` remains separate and unchanged. This report gives no paid-AND, OR-only, wire, description-bit, runtime, or cyclic-closure lower bound.

The next attempt must begin from an index-free promise embedding or a direct invariant of the separator's one-bit function. Repeating lookup entropy, address-incidence, neighborhood-volume, or static-menu counting without such a new bridge is not productive.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and proof.
- Ilango, [*SAT Reduces to the Minimum Circuit Size Problem with a Random Oracle*](https://eccc.weizmann.ac.il/report/2023/165/download), Theorems 6 and 8 and Section 6.2.
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://doi.org/10.1145/3538391), Theorem 59 and Corollary 61.
- Carmosino, Dang, and Jackman, [*Convergent Gate Elimination and Constructive Circuit Lower Bounds*](https://arxiv.org/abs/2602.17942) and [*Constructive Separations from Gate Elimination*](https://arxiv.org/abs/2604.23958).
- Carmosino, Dang, and Jackman, [*Simple Circuit Extensions for XOR in PTIME*](https://arxiv.org/abs/2511.16903).
