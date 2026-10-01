# C-435 — communication rank survives sharing, but its output ceiling is linear

**Cycle question.** Can a semantic statistic force an ordinary fan-in-two DAG to spend gates after it has all `N` table bits, with unrestricted fanout? I tested a cut communication-rank charge and paired it with an exact full-promise separator construction.

## 1. OPS target and quantifiers

Write `N=2^n`. OPS Theorem 1.4 uses a universal constant `c>=1`: if there is one fixed `epsilon>0` such that for every sufficiently small fixed `beta>0`,

```text
Gap-MCSP[s1,s2] is not in Circuit[N^(1+epsilon)],
s1 = 2^(beta*n)/(c*n) = N^beta/(c log2 N),
s2 = 2^(beta*n) = N^beta,
```

then `NP` is not contained in `Circuit[poly]`. The quantifier is uniform in `epsilon` as `beta` tends to zero. A lower bound with exponent `1+theta*beta` for a fixed `theta` does not meet it. This is the ordinary total-gate target; wire, description, runtime, paid-AND, and native-state measures are separate.

## 2. A fully specified shared-computation charge

For a Boolean predicate `F:{0,1}^N -> {0,1}` and a partition of its input coordinates into `A` and `B`, form the `2^|A|` by `2^|B|` matrix `M_F^A,B` with entry `F(a,b)`. Define

```text
R_A,B(F) = log2 rank_GF(2)(M_F^A,B).
```

**Theorem.** If an AND/OR/NOT fan-in-two DAG with `S` gates computes `F`, then for every partition `A|B`,

```text
rank_GF(2)(M_F^A,B) <= 2^(2S+1),
R_A,B(F) <= 2S+1.
```

**Proof.** Alice receives the `A` coordinates and Bob the `B` coordinates. Bob sends Alice the values of the `B`-input variables that occur on circuit input edges. There are at most `2S` such occurrences, since there are at most two input slots per gate. Alice now knows every primary input value used by the DAG and evaluates all gates, including all reused intermediate values. If the circuit output is a raw Bob input, Bob sends that one additional bit. This is a deterministic one-way protocol using at most `2S+1` bits. Each transcript defines a rectangle of input pairs; the accepting matrix is a union of at most `2^(2S+1)` such rectangles. A rectangle indicator has GF(2) rank one, so subadditivity of rank gives the claim. No assumption is made about the circuit's architecture, fanout, or computation order beyond acyclicity.

This is a genuine total-gate inequality for arbitrary shared DAGs. But a matrix with `2^|A|` rows and `2^|B|` columns has rank at most `2^min(|A|,|B|)`. Therefore `R_A,B(F)<=min(|A|,|B|)<=N/2`, and this route can certify at most a linear gate lower bound. Averaging `R_A,B` over any family of cuts does not help: the average output value is still at most `N/2`, while the protocol bound is at most `2S+1` on every cut.

The improvement it would provide is explicit: a promise-forced value `R_A,B>=2N^(1+epsilon)+1` would imply `S>=N^(1+epsilon)`. Such a value cannot occur for any Boolean predicate on `N` bits, so this mechanism is structurally too weak for OPS even before proving a GapMCSP-specific rank lower bound.

This theorem counts total AND, OR, and NOT gates uniformly. It gives no separate paid-AND-state or OR-operation lower bound. The fan-in slots (and hence circuit wires, under this representation) are at most `2S`; it does not bound nonuniform description bits or the time needed to construct the circuit.

A complete lower-bound theorem from this mechanism would also need a promise-forced rank value for every valid separator extension; no such value is proved, and the free middle band lets each separator choose its extension there. More fundamentally, a superlinear `R_A,B` is impossible for any cut because of the dimension ceiling. Replacing rank by the sum over cuts only multiplies both the per-circuit upper bound and the output ceiling by the number of cuts.

## 3. Strong counterconstruction and calibration cases

The rank ceiling is not merely a weak estimate on easy examples. Let `N=2m` and set

```text
G_m(x,y) = AND_{i=1}^m (x_i OR y_i).
```

Its communication matrix is the Kronecker product of `m` copies of `[[0,1],[1,1]]`, whose determinant is nonzero over GF(2). Thus its rank is `2^m`, the maximum possible for this balanced cut. Yet `G_m` uses `m` OR gates and `m-1` AND gates, exactly `N-1` gates. This defeats any attempt to turn full cut rank, by itself, into a superlinear shared-gate charge. It is a counterexample to this mechanism, not to a GapMCSP lower bound.

The requested construction attacks also have cheap shared implementations:

- **Parity:** a chain of `N-1` XOR operations, each XOR realizable with a constant number of AND/OR/NOT gates, costs `O(N)`. Across a balanced input split its GF(2) communication matrix has rank at most two.
- **Repeated-block equality:** for two `m`-bit blocks, compute the `m` pairwise XNORs and AND them. This costs `O(N)` gates; the communication matrix is the identity and has full rank `2^m`.
- **Sparse parity checks:** for `r<=N` rows with total incidence `L=O(N)`, compute each row parity and AND the checks. This costs `O(L+r)=O(N)` gates, counting constant-size XOR implementations.
- **Simple global block relation:** split the input into `k` blocks and accept iff all block parities equal the first block's parity. Computing the parities, comparisons, and final AND takes `O(N)` gates.

These examples falsify generic charges based only on rank, parity-check incidence, repeated-block constraints, or the number of interacting blocks. They do not classify the GapMCSP promise.

## 4. Complete-promise separator attempt and resource accounting

Let `K` be the number of fan-in-two circuit descriptions of size at most `s1`. Standard description counting gives `K<=2^(O(s1 log(s1+n)))=2^(O(N^beta))` for each fixed `beta>0`. A valid exact separator is

```text
OR over descriptions d of size <= s1:
    AND over addresses i in {0,1}^n: [input_table[i] = output_d(i)].
```

Every promised YES table is accepted, and every promised NO table is rejected because its circuit complexity exceeds `s2>s1`; the middle band needs no prescribed answer. Its resources are:

- **Total gates:** `O(NK)=O(N*2^(O(N^beta)))`. Each description contributes an `N`-literal equality test; the final OR has `O(K)` gates.
- **AND gates / OR gates:** `O(NK)` ANDs for candidate equalities and `O(K)` ORs for their union; input complements can be shared in `O(N)` NOT gates.
- **Wires:** `O(NK)` fan-in-two wires. A truth-table coordinate may feed one test per description; that fanout is explicitly paid as wires and appears in the gate network.
- **Hardwired description:** the nonuniform circuit layout and candidate truth-table polarities take `O(NK log(NK))` bits under a standard gate-index encoding. These are advice/description bits, not gates.
- **Construction time:** direct enumeration and evaluation of every candidate circuit on all `N` addresses takes `O(K*N*poly(s1,n))` time. This is not the circuit-size measure.

I tried sharing by placing candidate truth tables in a prefix trie and reusing every common equality prefix. The trie has at most `1+NK` nodes. For a general list of `K` strings, it can branch into all `K` distinct prefixes after `ceil(log2 K)` positions and retain distinct suffix paths of length `N-ceil(log2 K)`, leaving `Theta(NK)` nodes. I have no proof that the special set of Low-circuit truth tables admits a much smaller representation, and this construction therefore does not improve the exact enumeration upper bound. It also supplies no lower bound against other separators.

## 5. Literature, barriers, and originality

The rank-to-communication argument is a standard deterministic communication technique; its application here is an audit of one concrete sharing charge, not a new general circuit lower-bound theorem. The published OPS magnification theorem remains the exact target above. Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam's locality barrier warns that many lower-bound methods persist when small-fan-in oracle gates are added; the rank argument neither bypasses nor resolves that barrier.

I checked two newer primary sources. Atserias–Müller's 2025 general magnification paper gives new distinguisher-based thresholds and a uniform MCSP implication for a different uniform class separation; it does not establish the required nonuniform ordinary-circuit bound for the OPS promise. Goldberg–Juvekar–Kabanets (ECCC TR26-091, June 2026) prove conditional hardness for *implicit* MCSP under subexponentially secure iO and a proof-system assumption; the input is a sampler circuit and the result is conditional, so it does not lower-bound ordinary circuits on an explicit truth-table input.

## 6. Result and next pivot

**Strongest proved statement this cycle:** any arbitrary shared `S`-gate separator has `rank_GF(2)(M)<=2^(2S+1)` on every input cut. The proof charges fan-in-two input slots, including arbitrary reuse. Its required potential is capped at `N/2`, and the full-rank `N-1`-gate construction shows that the cap is attained by a linear-size computation. Retire cut rank and uniform averages of cut rank as standalone superlinear mechanisms.

**Frontier: unchanged.** Ordinary total-gate lower bound remains `N-O(N^beta log N)-1` with C-406's additive refinement; the OPS `N^(1+epsilon)` target is open; exact full-promise enumeration is `O(N*2^(O(N^beta)))`; native `rho_GapMCSP>=N-o(N)` remains separate. The next ordinary-DAG attempt must use a promise-specific property beyond generic cut rank, without assuming a separator extracts descriptions or queries addresses individually.

### Primary sources checked

- Oliveira, Pich, Santhanam, [Hardness Magnification near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4.
- Chen et al., [Beyond Natural Proofs: Hardness Magnification and Locality](https://doi.org/10.1145/3538391).
- Atserias and Müller, [Simple General Magnification of Circuit Lower Bounds](https://www.cs.upc.edu/~atserias/papers/magnification/magnification.pdf), June 2025.
- Goldberg, Juvekar, Kabanets, [Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions](https://eccc.weizmann.ac.il/report/2026/091/download/), ECCC TR26-091.
