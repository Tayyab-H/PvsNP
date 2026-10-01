# C-434 — the Gap promise inherits a comparator bound, but sharing blocks the lift

**Result.** The local-PRG proof of Cavalar–Lu's comparator-circuit lower bound uses only two kinds of inputs: PRG-generated Low tables and uniformly random restricted tables that are High with probability at least one half. It therefore tolerates an arbitrary free middle band. For the project's OPS thresholds, it yields `Omega(N^(1+0.455 beta))` comparator gates and, separately, `Omega(N^(1+0.455 beta))` active wires for every fixed `0<beta<1/2`, for sufficiently large table length `N`. The proof below derives the gate bound directly, accounting for at most two active wires per gate.

This is a real promise-specific theorem for comparator circuits. It does **not** lower-bound ordinary fan-in-two DAG circuits: comparator circuits restrict reuse of intermediate values, and no size-preserving compiler from arbitrary shared circuits was proved. The ordinary OPS frontier is unchanged.

## 1. Exact promise and inherited lower bound

Let `N=2^d` be the truth-table length and use the OPS promise

```text
YES: Size(f) <= s1 = N^beta/(c*d)
NO:  Size(f) >  s2 = N^beta,
```

where `c>=1` is OPS's universal constant (its proof instantiates `c=10`) and `beta` is any fixed sufficiently small positive constant. A comparator circuit has gates `(u,v) -> (u AND v, u OR v)`, initial wires may be labelled by input literals, and an intermediate wire cannot be freely copied to arbitrarily many successor computations. Cavalar–Lu prove that MCSP at threshold `N^alpha` needs `N^(1+alpha/2-eta)` comparator wires for `0<alpha<=1-eta`; their proof uses a local PRG of seed length `ell^(2/3+o(1))` for `ell`-wire comparator circuits. [Cavalar–Lu, Theorems 16–17](https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.34/LIPIcs.ITCS.2022.34.pdf)

OPS's magnification implication asks for one fixed `epsilon>0` that works for every sufficiently small fixed `beta`. Here the exponent gain is only `0.455 beta`, which tends to zero with `beta`; so even a valid transfer to ordinary circuits would not meet that uniform-`epsilon` quantifier. The result is also in the comparator model rather than the ordinary `Circuit` model required by the implication. [OPS, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)

This is not fixed by tuning the parameters within the same local-PRG proof. For threshold parameter `alpha` and shrinkage parameter `eta`, local PRG outputs have complexity `N^(alpha-eta/3+o(1))`; fitting them below the OPS YES cutoff requires `alpha-eta/3 < beta`. The lower-bound exponent gain is `alpha/2-eta`, so

```text
alpha/2-eta < beta/2 - 5*eta/6 < beta/2.
```

Thus this particular restriction/PRG mechanism has a beta-dependent ceiling and cannot deliver one fixed positive exponent gain as `beta` tends to zero. This is a proof-specific limitation, not a lower bound on every possible comparator technique.

The following parameter choice transfers that proof to the exact promise above. Set

```text
delta = beta/100,
alpha = beta-delta = 0.99 beta,
eta = 4 delta = 0.04 beta,
chi = 1+alpha/2-eta = 1+0.455 beta.
```

For all sufficiently large `N`, every comparator separator correct on all promised inputs has more than `N^chi` gates. The analogous wire lower bound follows by starting with at most `N^chi` active wires.

**Proof.** Suppose a comparator separator `C` has at most `N^chi` gates. It has at most `2N^chi` active wires, since each gate touches two wires. Choose `k` to be a power of two within a constant factor of `N^(alpha+eta/2)`, and partition the `N` input bits into `N/k` consecutive, aligned blocks of length

```text
k = Theta(N^(alpha+eta/2)) = Theta(N^(beta+delta)).
```

Fix all but one block to zero. Averaging the number of active wires over the blocks gives a restriction `C_rho` with at most

```text
ell = 2*N^chi/(N/k) = O(N^(3 alpha/2-eta/2))
```

wires. Cavalar–Lu's local PRG for this restricted circuit has seed length

```text
r = ell^(2/3+o(1)) = N^(alpha-eta/3+o(1))
  = N^(beta-7 delta/3+o(1)).
```

Every seed output, placed in the free block with the other table bits fixed, is a Low truth table: its circuit size is `polylog(N)+r`, which is below `N^beta/(c*d)` for large `N`. Thus the separator accepts every PRG output.

For a uniformly random assignment to the free block, the standard counting bound used in the Cavalar–Lu proof gives circuit complexity at least

```text
k/(10 log k) = N^(beta+delta)/O(log N) > N^beta
```

with probability at least one half. Those tables are promised NO inputs and must be rejected. The uniform acceptance probability is therefore at most one half, even if the separator accepts every other input in the free middle band. The PRG acceptance probability is one. This gap of at least one half contradicts its `1/3`-fooling guarantee for `C_rho`.

The parameter conditions hold: `alpha>0`, `alpha<=1-eta`, the PRG outputs fit below `s1` by a fixed polynomial margin, and the random restricted tables exceed `s2` by a fixed polynomial margin. Since `k` is a power of two and the blocks are aligned, embedding a local truth table in one block and setting the rest to zero costs its local circuit plus `O(log N)` gates. In particular, this proof never assigns a required answer to a middle-band table. The transfer uses the local output guarantee of the PRG, not reconstruction of a circuit description or enumeration of witnesses.

The cited paper states the exact-MCSP version. This project-level refinement is the observation that its proof only needs the Low-generator and High-random portions, so the same exponent works for the wider OPS gap. It is not a new comparator-circuit lower-bound technique.

## 2. What this mechanism charges, and what it does not

The charge is to comparator **gates** in the displayed proof and to active **wires** in its wire-count variant. These are separate measures, related here only by the elementary `active wires <= 2 * gates` bound. Intermediate values have bounded fanout: each comparator overwrites its two wires with AND/OR results, and the model has no general primitive that branches an arbitrary intermediate value to many consumers. Neither result gives an ordinary-circuit gate bound, paid-AND-state bound, OR-operation bound, description-length bound, runtime bound, or native cyclic-closure bound.

The strongest direct attempt to lift it to the project target is formula unfolding. If an ordinary `S`-gate DAG has gate-to-gate cycle rank `mu`, the project's C-406 unfolding lemma gives a formula with at most `2*S*2^mu` leaves. A De Morgan formula is simulable by a comparator circuit with linear overhead, so C-434 implies the necessary tradeoff

```text
S * 2^mu >= N^(1+0.455 beta)/O(1),
log_2 S + mu >= (1+0.455 beta)*log_2 N - O(1).
```

This rules out a low-sharing separator in the corresponding size range and forces `mu >= (0.455 beta-epsilon)log_2 N-O(1)` if `S<=N^(1+epsilon)`. It does not rule out an ordinary separator with arbitrary reuse: `mu` may be large, and the exponential unfolding erases the very sharing the target allows. C-406 already gives a stronger logarithmic cycle-rank constraint in its parameter range, so this is a consistency check, not a frontier improvement.

## 3. Construction attacks and paired upper bound

Parity has an `O(N)` ordinary circuit and also an `O(N)` comparator circuit: maintain both parity polarities. Given wires `P, not P` and input literals `x, not x`, two comparator gates produce `A=P AND not x`, `B=P OR not x`, `C=not P AND x`, `D=not P OR x`; a third gate's OR output is `A OR C = P XOR x`, and a fourth gate's AND output is `B AND D = not(P XOR x)`. Repeated-block equality uses `O(N)` gates by comparing corresponding bits and ANDing the equality flags. Sparse parity checks with `O(N)` total incidences use this parity update a constant number of times per incidence with dual-rail inputs, followed by a linear aggregation. Copy, complement, permutation, and fixed sparse block recurrences can likewise be checked in linear size. These constructions defeat generic incidence, anchor, and independent-witness charges; they do not separate GapMCSP, whose promise quantifies over every Low and every sufficiently High table.

For the complete promise, I also tried to turn the exact Low-circuit enumerator into a near-linear separator by sharing the address decoder and organizing circuit descriptions as a prefix trie. Let `K=2^(O(s1 log(s1+N)))=2^(O(N^beta))` be the number of candidate circuits. The predicate is

```text
OR over descriptions d of size <=s1: AND over table addresses i in [N], [x_i = Eval(d,i)].
```

Sharing address decoding costs only `O(N polylog N)` once, but the generic trie still has up to `K` leaves and each leaf needs the `N`-bit table agreement test. This gives `O(NK)=O(N*2^(O(N^beta)))` total gates; no proved factoring compresses the candidate-dependent equalities to near-linear size. The exact construction handles every promised YES and NO input. A comparator implementation by an OR of literal minterms has the same exponential scale. Thus the paired upper attempt does not construct a near-linear full-promise separator or native cover.

## 4. Originality, barriers, and frontier

The comparator lower bound is published; the gap-promise transfer above is a direct project derivation from its proof. The attempt to convert it to arbitrary DAGs stops exactly at the cost of sharing. No cost-preserving comparator compiler, or proof that every OPS separator has small cycle rank, is known here. This does not bypass Chen et al.'s locality barrier: it proves a bound only in the bounded-fanout comparator model and contributes no new lower-bound invariant against unrestricted separators. [Chen et al., *Beyond Natural Proofs: Hardness Magnification and Locality*](https://doi.org/10.1145/3538391)

**Strongest proved statement:** for each fixed `0<beta<1/2`, the OPS GapMCSP promise requires more than `N^(1+0.455 beta)` comparator gates and, separately, more than that many active wires for sufficiently large `N`, under the cited comparator model. This sharpens the exact promise result for a restricted circuit class only; its beta-dependent exponent does not meet OPS's fixed-`epsilon` quantifier.

**Quantitative frontier: unchanged.** Ordinary total-gate lower bound remains `N-O(N^beta log N)-1` plus C-406's refinement; ordinary OPS `N^(1+epsilon)` remains open; exact full-promise separator remains `O(N*2^(O(N^beta)))`; native `rho_GapMCSP>=N-o(N)` is separate. The next mechanism must charge arbitrary intermediate reuse directly, or prove a valid restriction that reduces it without assuming a circuit architecture.

### Primary sources

- Cavalar and Lu, [*Algorithms and Lower Bounds for Comparator Circuits from Shrinkage* (ITCS 2022)](https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.34/LIPIcs.ITCS.2022.34.pdf), Theorems 16–17 and Section 2.1.
- Oliveira, Pich, and Santhanam, [*Hardness Magnification near State-Of-The-Art Lower Bounds* (CCC 2019)](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 for the OPS thresholds.
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://doi.org/10.1145/3538391), for the technique-specific locality barrier.
