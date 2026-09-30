# C-414 - Source-support capacity blocks cheap indexed-lookup reductions

Date: 30 September 2026

**Status:** proved a necessary table-generation cost for single- and multiple-instance reductions that make a Gap-MCSP separator compute an indexed source bit through promised tables. The promise also forces a large Hamming change at every source-bit flip, but this alone does not charge gates. Sharing counterexamples remain. This closes one lookup-transfer architecture; no Gap-MCSP frontier changes.

## 1. Exact target and model

Let `N=2^n`, with OPS thresholds `s1=N^beta/(10n)` and `s2=N^beta`, for fixed sufficiently small `beta>0`. A separator `h:{0,1}^N->{0,1}` accepts every table of ordinary fan-in-two AND/OR/NOT circuit size at most `s1` and rejects every table of size at least `s2`; the middle band is free. The magnification target is one fixed `epsilon>0` such that every sufficiently small fixed `beta` requires more than `N^(1+epsilon)` total gates. The required threshold ratio is `s2/s1=10n`.

## 2. Promise-forced edge distance

If tables `u,v` differ in `d` truth-table coordinates, then

```text
CC(v) <= CC(u) + d*n + n + 3.
```

For each changed address, append its `n`-literal minterm, OR the `d` minterms, share the `n` negated input variables, and XOR the correction with a circuit for `u`; these use at most `dn+n+3` additional total gates. Consequently, any promised YES table `u` and promised NO table `v` satisfy

```text
d >= Delta := max(0, ceil((s2-s1-n-3)/n)) = Theta(N^beta/n).
```

This is a full-promise statement: it uses no label from the free middle band. It says that a promise-preserving encoding cannot change the YES/NO answer after flipping a source bit while changing only a few table entries.

## 3. A necessary-cost theorem for a single-instance lookup embedding

Suppose `A=(A_1,...,A_K)` is an arbitrary `K`-bit data string, `i in [K]` is an index, `E(A,i)` is an `N`-bit truth table produced by a fan-in-two circuit with `R` total gates, and `h` is a valid Gap-MCSP separator with `S` total gates. Assume the reduction is promise-preserving and

```text
h(E(A,i)) = A_i        for every A in {0,1}^K and every i in [K].
```

Then

```text
K <= N + 2R,       so R >= (K-N)/2,
S + R >= K-1.
```

**Proof of the support bound.** Fix `j` and set `i=j`. The composite output changes when only `A_j` flips, so at least one coordinate of the vector `E(A,j)` changes. Therefore `A_j` must influence some output coordinate of `E`. Among all `K` data variables, at most `N` can occur as direct input wires among the `N` output wires. Every other essential data variable must enter at least one gate, and the `R` fan-in-two gates have at most `2R` input pins. Hence `K<=N+2R`.

**Proof of the composition bound.** Wire the `N` outputs of `E` directly to the `N` inputs of `h`; their composition computes the `K`-to-1 multiplexer `MUX_K(A,i)=A_i` with exactly `R+S` gates. Every data input `A_j` is essential. In the connected output-ancestor DAG of a fan-in-two circuit, if `I` distinct input vertices are essential and there are `G` gates, connectivity requires at least `I+G-1` edges while fan-in gives at most `2G`; thus `G>=I-1`. So `MUX_K` needs at least `K-1` gates and `R+S>=K-1`.

If `K=N^(1+delta)` for fixed `delta>0`, then the *reduction circuit itself* needs `R >= (1/2-o(1))K` gates. It is already superlinear in `N`; composition cannot attribute this cost to `h`. If `K<=N`, the multiplexer lower bound is at most linear in the table length and cannot force the OPS target. Thus an arbitrary-index lookup lower bound cannot be transferred by a cheap single-table map through the separator. This is a no-go for that specific architecture, not for all promise embeddings or direct lower-bound arguments.

The same support argument covers a multiple-instance variant. Let an encoder produce `t` promised `N`-bit tables from `(A,i)` using `R` gates, and let a postprocessor return `A_i` using `B` further gates. It may inspect `i`, all `t` separator outputs, and the generated tables themselves; it receives no raw data bit of `A` except through the encoder. Then

```text
K <= t*N + 2R,       R + t*S + B >= K-1.
```

For the first inequality, each of the `K` data bits must influence some generated table coordinate; at most `tN` distinct data bits can be passed directly to output wires and at most `2R` can enter encoder gates. The second inequality follows because the entire composition computes `MUX_K`; inspecting encoder outputs in the postprocessor adds no gates beyond those already counted in `R`. In particular, if `R+B=o(K)`, then `K<=tN+o(K)`, so `K/t<=N(1+o(1))`: this lookup argument cannot force a superlinear per-call cost `S`. If instead `K/t>N^(1+epsilon)`, then `R=Omega(K)` and the encoder itself bears the superlinear work. This closes the simple multi-instance indexed-readout transfer when all source information must pass through the generated promise tables and the reduction/postprocessor are required to be cheaper than the source lookup.

## 4. The edge-distance charge fails under sharing

The promise-forced `Delta` changes per source-bit flip do not imply `K*Delta` gates. For `K=N`, define an `N`-bit output vector by

```text
E_j(A) = parity(A_1,...,A_N)       for every j in [N].
```

Flipping any one source bit changes all `N` output coordinates, yet one shared XOR chain computes the parity in `N-1` XOR gates and fans it out to every output. In AND/OR/NOT basis this is `O(N)` gates. This is a counterexample to charging output differences or bit-to-coordinate incidences separately. It is not a promise-preserving MCSP encoding and does not refute the target lower bound.

The other required cheap-sharing attacks remain decisive against generic additive charges:

- **Parity:** all `N` prefix parities have `Theta(N^2)` expanded incidences but use one `O(N)` shared XOR chain.
- **Repeated-block equality:** comparing `b` copies of an `m`-bit block to the first, for `N=bm`, costs `O(N)` gates; repeated constraints are not fresh scans.
- **Sparse parity checks:** `O(N)` nonzero entries yield an `O(N)`-gate XOR readout; nested prefix checks can have `Theta(N^2)` expanded incidence but share one prefix chain.
- **Simple global block relations:** compute a shared copy/prefix-XOR relation once, then perform the `N` comparisons in `O(N)` gates.

Every example bounds ordinary total gates with unrestricted fanout. None is a full-promise Gap-MCSP separator.

## 5. Paired full-promise separator attempt

For every circuit description `D` of size at most `s1`, hardwire its `N`-bit truth table, compare the input table to it, and OR all equality results. This accepts every YES table and rejects every NO table, with middle-band behavior unrestricted. If there are `K_low=2^(O(s1 log(s1+n)))=2^(O(N^beta))` descriptions, the explicit total-gate cost is `O(N K_low)`. A trie of the candidate truth tables also has worst-case `O(N K_low)` nodes, and the direct unrolled equality circuit has the same order; neither route gives a near-linear bound. No compact DAG representation of this particular candidate family, or circuit that decides its membership in near-linear size, is established here. This is a valid exact full-promise construction, but the near-linear construction attempt fails at that representation step.

## 6. Literature, novelty, and frontier

Oliveira-Pich-Santhanam Theorem 1.4 uses a universal constant denominator and its proof instantiates `10n`; it requires the same fixed-`epsilon`, all-sufficiently-small-`beta` quantifiers above. Ilango's random-oracle MCSP result is relative to oracle-circuit complexity and has a constant-factor gap around `M/log M`, so it does not furnish the OPS ratio `10 log M`. Chen et al.'s locality theorem is technique-specific and does not preclude this or another unrestricted approach.

The edge-distance lemma is the C-412 sparse-address patch bound applied to opposite promise labels. The source-support and multiplexer factorization bounds are project-level deductions from essential-input connectivity. They are not a new circuit lower bound. The parity replication example proves why the Hamming-distance statement alone does not charge total gates.

**Exact quantitative effect:** none. Ordinary `S>=N-O(N^beta log N)-1` and C-406's additive logarithmic refinement remain the frontier; the OPS `N^(1+epsilon)` target remains open. Native `rho_GapMCSP>=N-o(N)` remains separate. The full-promise upper remains `O(N 2^(O(N^beta)))`. No paid-AND, OR-only, wire, description-bit, runtime, or cyclic-closure lower bound follows.

The lookup-transfer route is closed for a cheap single- or multiple-instance encoding whose only hardness source is an arbitrary `K`-bit indexed readout and whose generated promised tables are the only channel carrying the source data: when `K` exceeds the aggregate table width, the encoder already needs `Omega(K)` gates. A remaining route would need a different hard source or an invariant of the separator itself, and a full-promise/total-gate proof; merely batching more indexed reads cannot overcome the support-capacity inequality.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4.
- Ilango, [*SAT Reduces to the Minimum Circuit Size Problem with a Random Oracle*](https://eccc.weizmann.ac.il/report/2023/165/download).
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://doi.org/10.1145/3538391).
