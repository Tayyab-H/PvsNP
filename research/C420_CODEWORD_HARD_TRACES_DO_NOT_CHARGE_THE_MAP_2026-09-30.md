# C-420 - Codeword-hard promise traces still put the hard work in the map

**Status:** the proposed reduction mechanism is fully specified and its key existence lemmas are proved, but its cost transfer fails. A random linear code can have every nonzero word OPS-High while zero is Low; the induced promise on the code is then just zero testing, with an `O(N)` separator. More generally, if a source predicate is embedded as membership in the kernel of a syndrome map and the table is the corresponding encoded syndrome, the table generator must already pay the source predicate's circuit complexity up to `O(N)`. This is a proved route-specific no-go, not a counterexample to the full lower-bound program. No quantitative frontier changes.

## 1. Exact OPS target used here

Let `N=2^n`, with fixed `0<beta<1`, `s1=floor(N^beta/(10n))`, and `s2=ceil(N^beta)`. A valid promise separator accepts every truth table of circuit size at most `s1` and rejects every table of size at least `s2`; behavior in the middle band is unrestricted. OPS Theorem 1.4 states the magnification implication with universal `c>=1`: if there is one fixed `epsilon>0` such that for every sufficiently small fixed `beta>0`, `Gap-MCSP[2^(beta n)/(c n),2^(beta n)]` has no fan-in-two circuit of `N^(1+epsilon)` gates, then `NP` is not contained in polynomial-size circuits. Their proof instantiates `c=10`. Circuit size counts total gates over any fixed fan-in-two Boolean basis; fanout is unrestricted. The theorem does not count wires, description bits, or the time to construct the circuit as gates.

## 2. Candidate mechanism: hard codeword syndrome lift

The intended charge was: encode a source `x` as an `N`-bit truth table `T(x)` so that `T(x)=0` exactly when `x` satisfies a hard global constraint, while every other `T(x)` is OPS-High. A full-promise separator `h` would then decide the source constraint after the table generator has supplied all reusable intermediate values. This avoids assuming that `h` reconstructs a circuit description, enumerates witnesses, or separately checks addresses.

The exact construction template is:

- Choose a codimension-`r` subspace `C=ker(H)` of `F_2^K`, where `H:F_2^K -> F_2^r` has rank `r`.
- Choose an injective linear map `E:F_2^r -> F_2^N` whose nonzero image words all have circuit complexity at least `s2`.
- Set `T(x)=E(Hx)`. Then `x in C` maps to `0^N` (Low), and `x notin C` maps to an OPS-High table. Every output of the map is promised.

This template has two proved ingredients:

**High-code existence.** There are at most `2^(O(s2 log(N+s2)))=2^(O(N^beta n))` tables of circuit complexity below `s2`. For a uniformly random `r`-dimensional subspace `W` of `F_2^N`, each fixed nonzero table lies in `W` with probability `(2^r-1)/(2^N-1) <= 2^(r-N+1)`. Therefore, if `N-r` exceeds the circuit-count exponent by a sufficiently large constant factor, a union bound gives a subspace `W` with `W\{0}` entirely OPS-High. Choose any basis map `E` onto `W`.

**Hard kernel existence.** For `1<=r<=K/2`, the number of codimension-`r` subspaces of `F_2^K` is `2^(r(K-r)+O(1))`. The number of fan-in-two Boolean circuits with `K` inputs and at most `L` gates is `2^(O(L log(K+L)))`. Counting therefore gives some such `C` whose membership function `g_C(x)=1 iff x in C` needs `Omega(r(K-r)/log K)` total gates (for polynomially related parameters).

These facts jointly give an exact all-promised embedding of a source predicate with a superlinear circuit lower bound. The remaining issue is which part of the composed computation pays for it.

## 3. Decisive proof obstruction: the induced selector is cheap

Let `R` be the total fan-in-two gate count of the multi-output map `T`, and let `S` be the gate count of any valid Gap-MCSP separator `h`. On the image of `T`, the separator's label is exactly `T=0` versus `T!=0`. The induced label has an `O(N)`-gate implementation `h_0(y)=NOR(y_1,...,y_N)`. Consequently,

```text
CC(g_C) <= R + O(N),
```

by composing the map with `h_0`. The arbitrary separator gives only

```text
CC(g_C) <= R + S.
```

The first inequality is the decisive one: whenever the hard-kernel counting argument gives `CC(g_C)=L`, the generator must already have `R>=L-O(N)`. The second inequality cannot isolate `S`. The source lower bound is absorbed before the purported Gap-MCSP computation begins. This holds with unrestricted reuse and ordinary total-gate accounting; no gate is hidden in a wire or paid-AND convention.

For example, taking `K=N` and `r=floor(N/2)` yields a nonconstructively hard kernel predicate of complexity `Omega(N^2/log N)`. The code image can simultaneously be chosen so every nonzero table is OPS-High. But the map `x -> E(Hx)` itself then needs `Omega(N^2/log N)` gates, since NOR of its output computes the hard kernel predicate. Thus the construction proves that the *map* is expensive; it proves no superlinear lower bound on a full-promise separator.

This is stronger than merely observing that a known implementation of `H` is dense: it rules out every encoding of this zero-versus-nonzero form whose total map cost is claimed to be `o(CC(g_C))`.

## 4. Adversarial tests of the charge

The same syndrome story gives cheap shared readouts whenever the relation is structured:

- **Parity:** one parity equation costs `K-1` XOR gates, and its zero-test adds `O(1)` gates. Replicating prefix parities has `Theta(K^2)` expanded incidences but only `O(K)` shared gates.
- **Repeated-block equality:** compare one representative per block or compute adjacent XOR differences once; fanout does not multiply the charge. For `q` free block values, equality to a common value costs `O(q)` gates.
- **Sparse parity checks:** a system `Hz=0` with `t` nonzeros costs `O(t+r)` gates by computing each listed parity and ANDing the check results. Bounded row weight and `r=O(K)` give `O(K)` total gates.
- **Simple global block relations:** copy/XOR generators are evaluated once, then reused across every dependent coordinate. Gate count follows the shared generator, not the number of table positions or constraints.

These refute a generic “number of codewords / constraints / incidences forces paid work” principle. They do not give a full-promise separator, and they do not refute the OPS target.

## 5. Paired full-promise construction attempt

A short *linear sketch* looked like a possible near-linear full-promise separator: compute `L(f)` for a rank-`k` linear map and classify the sketch. It cannot compress the table substantially while remaining exact. Every function in the kernel of `L` shares its sketch with `0^N`, which is Low. If `N-k > O(N^beta n)`, the kernel has more elements than the total number of functions of circuit size below `s2`; hence it contains a High table. That High table and `0^N` collide, so no downstream classifier can separate the promise. Thus every such exact linear sketch must have rank

```text
k >= N - O(N^beta log N).
```

This closes aggressive linear dimension reduction only. Rank near `N` does not imply superlinear gates: the identity sketch is just wires, and it leaves the original decision problem unsolved.

The exact all-input construction remains: enumerate every circuit description of size at most `s1`, compare its `N`-bit truth table with the input, and OR the equality tests. Circuit counting gives `2^(O(N^beta))` candidates, so this is a correct full-promise separator of `O(N 2^(O(N^beta)))` total gates. It handles every Low and every High input, but is not near-linear. A hashed candidate-list shortcut was not proved safe: a collision between any Low and any High invalidates exact promise separation, and random collision bounds over a fixed distribution do not rule out worst-case collisions.

## 6. Model and literature audit

- **Total gates:** all inequalities above count every fan-in-two Boolean gate, including XOR when used. No AND-only lower bound is inferred.
- **Paid AND / OR:** not used as a surrogate for total gates; OR/NOR comparisons are explicitly charged `O(N)`.
- **Wires and reuse:** fanout is unrestricted and free in the gate measure; `R` counts gates in the complete multi-output table map. The `N` output connections, the matrix/router description, and gate count are distinct.
- **Description bits:** the existential random subspace or dense matrix may take `Theta(Nr)` bits to specify. This is not included in circuit gates and supplies no uniform construction.
- **Runtime:** materializing the `N`-bit table takes `Theta(N)` output time; it is not the map's gate count.
- **OPS magnification:** the exact fixed-`epsilon`, all-sufficiently-small-fixed-`beta` quantifier is verified from Theorem 1.4 of Oliveira, Pich, and Santhanam. The required consequence is `NP not-subset P/poly`, hence `P != NP`, if that premise is proved.
- **Known barriers:** Chen et al.'s locality barrier rules out specified lifts of existing locality-based lower-bound methods in their oracle/locality setting. C-420 is an ordinary promise-embedding audit; it neither bypasses nor strengthens that barrier. Formula and restricted-circuit MCSP lower bounds do not transfer to unrestricted total-gate DAG circuits by this argument.
- **Originality:** circuit counting and random-subspace avoidance are standard ingredients. C-420 records their exact OPS-parameter application and proves the map-versus-selector cost obstruction; it does not claim a new general circuit lower-bound technique or literature priority.

## 7. Result and next mechanism

**Strongest proved statement:** an `r`-dimensional subspace of `N`-bit tables can be chosen so every nonzero member is OPS-High, but using its zero/nonzero label to encode a hard source forces the multi-output table generator itself to have at least the source predicate's circuit complexity minus `O(N)`. A rank-`k` linear sketch that separates the full OPS promise must retain `N-O(N^beta log N)` dimensions.

**Frontier effect: none.** Ordinary full-promise lower bound remains `S>=N-O(N^beta log N)-1` plus C-406's additive logarithmic refinement. The required OPS `N^(1+epsilon)` lower bound remains open. Native `rho_GapMCSP>=N-o(N)` is separate and unchanged. Exact full-promise enumeration remains `O(N 2^(O(N^beta)))`. No near-linear full-promise separator or native cover was constructed.

**Route decision:** close the kernel-membership/zero-anchor lift and low-rank linear sketch as standalone mechanisms. Do not sharpen them by counting more anchors. The next attempt must make the induced trace label itself computationally hard after all shared map signals are available, or prove a potential directly on arbitrary full-promise separators with a gate-by-gate growth bound.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/), Theorem 1.4 and circuit-size conventions.
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://arxiv.org/abs/1911.08297), for the technique-specific locality-barrier audit.
- Project calibrations: [C-401](C401_SHARED_READOUT_CHARGE_AND_ORDINARY_GATES_2026-09-29.md), [C-417](C417_PAIRED_FAMILY_OUTPUT_MODEL_TRADEOFF_2026-09-30.md), and [C-419](C419_ALL_BLOCK_DIMENSIONS_HAVE_EASY_TRACES_2026-09-30.md).
