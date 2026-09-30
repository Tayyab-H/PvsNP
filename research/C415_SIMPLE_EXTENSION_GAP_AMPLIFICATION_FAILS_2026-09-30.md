# C-415 - Simple-extension hardness does not yet meet the OPS gap

Date: 30 September 2026

**Status:** a general low-complexity negative-extension construction and reduction audit. For any nondegenerate base with a zero input and a known `U`-gate circuit, adjoining `U+6` parity variables gives an f-Simple-Extension NO of `O(d)` circuit size. Thus exact nonmembership does not give the exponentially larger NO complexity required by OPS Gap-MCSP, including when the base is MUX. The attempted product amplification also remains low circuit complexity. This closes a naive transfer route, not all reductions. The ordinary and native frontiers do not change.

## 1. Quantitative target

Write `d` for the number of input variables of a truth table and `M=2^d` for its input length. The concrete OPS thresholds are

```text
s1 = M^beta/(10 d) = 2^(beta*d)/(10 d),
s2 = M^beta         = 2^(beta*d),
```

for a fixed sufficiently small `beta>0`; the magnification quantifier is one fixed `epsilon>0` and every sufficiently small fixed `beta>0`. The gap ratio is `10d`. The universal-constant formulation and the concrete denominator `10d` are Theorem 1.4 and its proof in Oliveira-Pich-Santhanam.

The scale mismatch is immediate but decisive: for every fixed `a` and fixed `beta>0`,

```text
d^a = o(2^(beta*d)/d).
```

So a reduction whose NO outputs are only known to have polynomial-in-arity circuit size has not produced OPS NO instances at all: those outputs are still YES for large `d`.

## 2. What simple-extension reductions establish

For a base function `f` on `r` variables and `m` added variables, the STACS 2026 simple-extension predicate asks whether a total function `g` on `d=r+m` variables is nondegenerate, has a key `k` with `g(x,k)=f(x)` for every `x`, and has exact circuit size

```text
CC(g) = CC(f) + m.
```

This is an exact-structure decision problem, not a promise that nonmembers have circuit complexity `2^(beta*d)`. Even in the strongest natural restriction where all candidate `g` already has the key and is nondegenerate, failure of the exact-size condition only says `CC(g) != CC(f)+m`. If a reduction proves a one-gate excess, the resulting lower bound is `CC(g)>=CC(f)+m+1`, still polynomial in `d` for linear-size `f`.

### A low-complexity nonmember for every explicit base function

Let `f` be a nondegenerate function on `r` variables with a zero input `x0`. Let `U` be the size of any known circuit for `f`, and let `C=CC(f)<=U`. Set `m=U+6` and define

```text
g(x,y_1,...,y_m) = f(x) OR PARITY(y_1,...,y_m).
```

Then:

1. `g` depends on every input. For an original variable, restrict `y=0^m` and inherit its dependence from `f`; for each new `y_j`, fix `x=x0` and all other `y` bits to zero.
2. `k=0^m` is a key, since `g(x,0^m)=f(x)` for every `x`.
3. `CC(g)>=3(m-1)-3=3(U+5)-3=3U+12>C+m`: restricting `x=x0` yields parity. If constants are not free, at most three extra gates generate shared 0 and 1 signals from `y_1`; the DeMorgan-basis parity lower bound is `3(m-1)` binary gates ([Carmosino et al., Main Lemma/Table 1](https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.23/LIPIcs.STACS.2026.23.html)), and charging NOT gates cannot weaken it.
4. `CC(g)<=U+4(m-1)+1=5U+21=O(d)`, where `d=r+m` is the total arity; compute `f`, a linear parity chain using at most four AND/OR/NOT gates per XOR, then one final OR.

Thus `g` is **not** a simple extension: it has the key and is nondegenerate, but its size exceeds `CC(f)+m`. Its circuit size is nevertheless `O(d)`. The truth table has length `M=2^d`, so for every fixed `beta>0`, eventually

```text
CC(g) <= O(d) < 2^(beta*d)/(10d) = s1.
```

The negative f-Simple Extension label therefore maps to a Gap-MCSP YES table. This construction applies in particular to `f=OR_r` and to MUX: any explicit upper bound `U=O(r)` for a nondegenerate base gives an extension-negative output of arity `d=O(r)` and circuit size `O(d)`, without knowing or characterizing the base's optimal circuits. This directly falsifies the transfer “not a simple extension implies high circuit complexity.” It does not falsify the OPS target.
## 3. Attempted amplification by independent copies

For `k` disjoint copies of a `d0`-variable table function `g`, their OR is computable with at most `k*CC(g)+(k-1)` gates on `d'=k*d0` variables. Starting from the explicit `O(d0)` circuit above gives an `O(d')` circuit for the product. The truth-table length becomes `M'=2^d'`, whose OPS YES threshold is `2^(beta*d')/(10d')`; the product remains deep inside YES for every fixed `beta>0` and sufficiently large `d'`.

This is an explicit shared-computation counterconstruction to the proposed amplifier: repeating a circuit-size-`O(d0)` extension-negative example across independent blocks only creates a linear-size function of the enlarged arity. A direct-sum lower bound would not repair this particular construction; the explicit upper circuit already puts the constructed negative instances below `s1`. To reach an OPS NO label, a different construction must make its no-case output have at least `2^(beta*d')` gates.

The same check applies to a MUX of `k` candidate functions: a selector tree plus the `k` component circuits costs `O(k*CC(g)+k)`, which is polynomial in the total number of input variables for these candidates. MUX's reuse structure may make its exact simple-extension predicate a more interesting source problem, but it does not itself amplify a polynomial circuit-size gap to the OPS threshold.

## 4. What the 2026 literature does and does not give

Carmosino, Dang, and Jackman prove that `f`-Simple Extension is in P when optimal circuits for `f` have linear size, bounded fanout, and are polynomially enumerable up to isomorphism and input permutation. Their 2026 result characterizes optimal XOR circuits and puts XOR-Simple Extension in P; OR-Simple Extension is also easy. They identify MUX as a promising candidate because its known constructions reuse subcircuits, but the known bounds are only linear and not tight, and a full optimal-circuit characterization or MUX-Simple-Extension hardness is not proved. These results concern an exact extension predicate; they do not establish a full-promise separator or the OPS-sized high-complexity outputs.

The general `f OR PARITY` construction is a project-level counterexample to the exact-label transfer. The scale comparison is elementary and unconditional. Neither is a new circuit lower bound. Chen et al.'s locality barrier remains technique-specific; this arithmetic gap audit neither invokes nor strengthens that barrier. This route would become relevant to OPS only after proving a promise-preserving reduction with YES size at most `2^(beta*d)/(10d)` and NO size at least `2^(beta*d)` for all sufficiently large `d`, including every output the reduction can produce.

## 5. Paired full-promise separator attempt

The exact classifier remains: enumerate every circuit description of size at most `s1`, compare the input table against each generated truth table, and OR the equality results. It accepts every YES table and rejects every NO table. With `K_low=2^(O(s1*log(s1+d)))=2^(O(M^beta))` descriptions, a direct fan-in-two implementation costs `O(M*K_low)=M*2^(O(M^beta))` total gates. This is a valid full-promise separator but not near-linear; simple-extension structure does not compress this enumeration in the attempted construction.

## 6. Exact conclusion and next obligation

The new obstruction is **gap amplification**, not indexed-readout capacity: structural nonmembership and even a proved one-gate excess are far too weak compared with the OPS threshold `2^(beta*d)`. The next useful step on this route would be a concrete total-function encoding in which satisfiable/source-YES instances yield low circuits while every source-NO output provably has circuit complexity at least `2^(beta*d)`. A claim about optimal circuit shape, a count of candidate extensions, or an exact `+1` size gap is insufficient.

**Exact quantitative effect:** none. Ordinary `S>=N-O(N^beta log N)-1` with C-406's additive logarithmic refinement remains the frontier; OPS `N^(1+epsilon)` is open. Native `rho_GapMCSP>=N-o(N)` remains separate. The explicit full-promise upper is still `O(N*2^(O(N^beta)))`. This audit establishes no paid-AND, OR-only, wire, description-bit, runtime, or native cyclic-closure lower bound.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and proof.
- Carmosino, Dang, and Jackman, [*Simple Circuit Extensions for XOR in PTIME*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.23/LIPIcs.STACS.2026.23.html), STACS 2026.
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://doi.org/10.1145/3538391), JACM 2022.
- Mazor and Pass, [*Gap MCSP is not (Levin) NP-complete in Obfustopia*](https://eccc.weizmann.ac.il/report/2024/053/), Revision 2 (2026); conditional result about witness-preserving reductions, not a circuit lower bound.
- Hirahara and Ilango, [*NP-Hardness of Approximating Meta-Complexity: A Cryptographic Approach*](https://www.rahulilango.com/papers/MCSP-Proceedings-2025.pdf), conditional/quasipolynomial nonadaptive hardness; this does not supply the unconditional ordinary separator lower bound sought here.
