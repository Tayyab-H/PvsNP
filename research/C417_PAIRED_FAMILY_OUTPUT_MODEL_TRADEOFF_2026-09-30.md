# C-417 - Paired-family reductions trade address generation against output routing

**Status:** two exact composition lemmas proved; generic paired-family transfer not obtained.
**Date:** 30 September 2026.
**Ordinary OPS frontier:** unchanged.
**Native fusion frontier:** unchanged.

## 1. Target and exact promise

Let `d` be the number of variables in the table functions, `M=2^d`, and use the concrete OPS thresholds

```text
s1 = floor(M^beta/(10d)),    s2 = ceil(M^beta),
```

with fixed `0<beta<1`. The low side is `CC(T)<=s1`; the high side is `CC(T)>=s2`; the middle is undefined. OPS's magnification theorem has one universal low-threshold constant and requires one fixed `epsilon>0` for every sufficiently small fixed `beta>0`; its proof uses the denominator `10d`.

The attempted mechanism is a deterministic paired-family embedding. Given a source Boolean function `H(z)`, produce a table `T_z` with the OPS label equal to `H(z)` on every source input, so an arbitrary separator `F` of `S` gates would yield a small circuit for `H`. The map must not compute `H` itself, every table must land on the right side of the actual gap, and all sharing and output representation costs must be stated.

## 2. Address-uniform, single-output generator: exact theorem

Suppose `G(z,a)` is one ordinary fan-in-two AND/OR/NOT circuit of `R` gates, where `z` is the source input and `a` is a `d`-bit address. Define

```text
T_z[a] = G(z,a), for every a in {0,1}^d.
```

Let `F` be an `S`-gate total circuit separating the OPS promise, and suppose `T_z` is promised for each source input under consideration. Then:

1. For every fixed `z`, `CC(T_z)<=R+O(1)`: hardwire `z` into `G` and leave `a` as the table-function input. If constants are not free, two or three fixed gates generate them from an address input. In particular, if any source input must map to an OPS-NO table, then `R+O(1)>=s2`.
2. The composed source function `H(z)=F(T_z)` has a circuit of at most `S+MR+O(1)` gates: hardwire each of the `M` addresses into one copy of `G`, feed their outputs to the `M` input wires of `F`, and share any additional subcircuits only if their common structure is explicitly established. Hence a known lower bound `CC(H)>=L` implies only `S>=L-MR-O(1)` by this generic construction.

**Proof.** The fixed-`z` restriction of `G` is a `d`-input circuit for exactly the table function `T_z`, using no more than its `R` gates plus a constant number to simulate hardwired constants if required. For the composition, make `M` copies of `G`, one per address, and connect the resulting `M` bits to `F`. This is a valid fan-in-two circuit for `H`. It costs at most `MR+S+O(1)` gates; hardwired address constants can be generated once and shared. Any factor below `M` requires a separately proved batch-sharing construction; it cannot be assumed from the number of queries or from reuse inside one copy of `G`.

This format preserves an immediate ordinary-circuit upper bound on every fixed table, but that bound prevents a generator of `R<s2-O(1)` gates from producing any promised NO table. Even when `R+O(1)>=s2`, the generic composition charge is `MR`, which may swamp the desired `M^(1+epsilon)` separator scale. This is an exact limitation of this transfer accounting, not a lower bound on `F`.

## 3. Multi-output table map: sharing composes, gate count misses the router

Now let `E(z)` be a multi-output circuit with `M` designated output wires and `R` internal gates, and suppose the designated output vector is the complete table `T_z`. Substituting `E` into `F` gives

```text
CC(H) <= R + S + B,
```

if a `B`-gate postprocessor follows `F`. This composition shares every gate of `E` exactly once and makes no assumption that `F` reconstructs a witness. The inequality is a valid total-gate statement; wires and description bits remain distinct measures.

However, `R` alone does not upper-bound `CC(T_z)`. Under the standard gate-only multi-output convention, a circuit computes each output component when it is an input wire or a gate output; naming the designated output wires is part of the interface. Choose any table `h` with `CC(h)>=s2`. Such a table exists because at most `2^(O(s2 log(d+s2)))=2^(O(M^beta*d))=2^o(M)` tables have circuits below `s2`, while there are `2^M` tables. There is a two-gate, `M`-output map on one source bit `b` with

```text
E(0) = 0^M,
E(1) = h.
```

Generate `zero = b AND NOT b`; at output position `a`, wire `zero` when `h[a]=0` and wire `b` when `h[a]=1`. The map uses one NOT and one AND gate, while its `M` output-wire choices encode `h`. `E(0)` is OPS-YES and `E(1)` OPS-NO, yet the source function recovered through `F` is just `NOT b`, with one gate. This is **not** a useful hardness reduction: the output routing has `Theta(M)` bits (and need not be uniformly constructible in polynomial time from `b`). It is a counterexample to treating a multi-output map's gate count as its complete cost or as evidence that its outputs are low.

More generally, expose the router explicitly. Suppose `E` computes `r` source-dependent signals `v_1(z),...,v_r(z)`, and the table bit at address `a` is `T_z[a]=v_{lambda(a)}(z)`, where the index selector `lambda:{0,1}^d->[r]` has a `q`-gate circuit. Fixing `z` turns every `v_j(z)` into a constant. A mux over those `r` constants computes `T_z(a)` in `q+c_mux*r+O(1)` gates. Therefore an OPS-NO table in this representation forces

```text
q + c_mux*r + O(1) >= s2,
```

for a fixed constant `c_mux` determined by the AND/OR/NOT implementation of a binary mux tree.

If the selector is charged as part of a uniform bitwise generator, this recovers the preceding high-side obstruction. If it is carried by output-wire labels, its `q`-gate value and its description/wire length cannot silently be charged to `R` or to the separator's gate count. This separates total gates, output wires, circuit-description bits, and uniform construction time.

## 4. Counterconstruction attempts

| Construction | Cheapest relevant shared computation | Outcome |
|---|---|---|
| Parity / affine parity tables | The address-uniform generator evaluates parity with `O(d)` gates; every fixed table is Low for large `d`. A separator can check affine parity from the explicit table in `O(M log M)` gates. | Cannot supply the OPS-high side; the check handles only this subpromise. |
| Repeated-block equality | The table generator selects a hardwired `2^k`-bit seed by prefix and ignores the suffix, costing `O(2^k)`; checking all repeated-block equalities takes `O(M)` gates. | The generated family stays Low at `k=floor(beta*d/2)`; equality count does not force superlinear gates. |
| Sparse parity-check blocks | `T_z(x,y)=z_x XOR PARITY(y)` is generated with `O(2^k+d)` gates; its suffix-edge constraints are checked in `O(Md)=O(M log M)` gates. | Many local checks coexist with near-linear total-gate verification, but the check is not a full-promise separator. |
| Simple global relations | `T_z(x,y)=z_x XOR h(y)` costs `O(2^k+CC(h)+d)` for simple `h`. | Seed entropy and local constraints do not transfer to the full promise. |
| Two-gate routed map | The multi-output construction above maps a source bit to a fixed Low/High pair using two gates and `M` output-wire choices. | Refutes a gate-only high-side estimate for arbitrary vector-output maps; its source is trivial and its routing is long. |

For the low families, take `k=floor(beta*d/2)`. Then `2^k+d=o(M^beta/d)`, so their circuits lie below `s1` for each fixed `beta>0` once `d` is large enough. These constructions falsify proposed charges based on number of blocks, checks, or output incidences. They do not give a full-promise separator, since they reject valid Low tables outside the chosen families.

## 5. Serious transfer attempt and decisive missing construction

The exact gate inequality for a legitimate multi-output map is attractive: if `H(z)=F(E(z))` has a proved ordinary circuit lower bound `L`, then `S>=L-R-B`. It allows arbitrary fan-out/sharing and assumes only that `F` is a one-bit separator. The attempt fails at the promise embedding, not at the composition proof:

1. The address-uniform map makes every table's circuit size at most `R`, so it cannot generate the required high side cheaply, and its generic source-composition compiler costs `MR`.
2. The multi-output map allows full sharing in the composition, but its gate count does not limit the table's fixed truth-table complexity unless the output router is also controlled. The explicit two-gate example places that complexity in wires/description.
3. Charging the router as a `q`-gate function restores a valid high-side bound `q+c_mux*r+O(1)>=s2`; no construction found here makes that charge simultaneously small, yields a source function with a lower bound `L>S+R+B`, and maps every relevant source input into the correct OPS promise.

The missing result is not an assumed "non-shareability principle." It is a concrete, uniform or otherwise admissible family `E` for which (i) the low/high table labels are proved at thresholds `s1,s2`, (ii) the router/interface cost is explicit, and (iii) the source function has a lower bound exceeding the fully shared composition size. No such family is obtained in this cycle.

## 6. Paired full-promise separator attempt

The best explicit separator remains the exact circuit enumerator: test equality against every table in `Low_s1` and output 1 on a match. It handles every promised YES and every promised NO, with arbitrary middle-band behavior, using `O(M*2^(O(M^beta)))` fan-in-two gates. The affine, repeated-block, and sparse-check recognizers cost at most `O(M log M)` but omit valid Low tables, so none improves this upper bound. No near-linear full-promise cover was constructed.

## 7. Literature and originality check

- **OPS threshold and quantifiers:** Oliveira, Pich, and Santhanam's Theorem 1.4 uses a universal low-threshold constant and asks for one fixed `epsilon` for every sufficiently small fixed `beta`; their proof instantiates denominator `10d`.
- **Multi-output convention is established:** Ilango, Loff, and Oliveira define a multi-output circuit by requiring each component function to be a gate or input-wire output, and count AND/OR/NOT gates. Their paper proves NP-hardness of exact minimization for total multi-output functions under randomized reductions. C-417's output-routing example is elementary bookkeeping under this standard model, not a new result about Multi-MCSP and not an OPS reduction.
- **Known locality barrier:** C-417 neither uses localized oracle gates nor derives a new oracle lower bound. It does not bypass or strengthen Chen et al.'s technique-specific hardness-magnification locality barrier.
- **Originality classification:** the composition inequalities and routing counterexample are project-level model audits assembled for this paired-family attempt. They establish no new asymptotic lower bound and no P-vs-NP separation.

## 8. Exact quantitative effect

**No frontier change.** Ordinary separators still have the proved floor `S>=M-O(M^beta log M)-1`, with C-406's additive logarithmic refinement. The OPS target `S>M^(1+epsilon)` for one fixed `epsilon>0` and every sufficiently small fixed `beta>0` is open. The native `rho_GapMCSP>=M-o(M)` target is separate and unchanged. The exact full-promise upper is `O(M*2^(O(M^beta)))` total gates. C-417 proves no lower bound on wires, descriptions, runtime, paid AND states, OR operations, endpoint width, or cyclic fusion closure.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and proof.
- Ilango, Loff, and Oliveira, [*NP-Hardness of Circuit Minimization for Multi-Output Functions*](https://www.dcs.warwick.ac.uk/~igorcarb/documents/papers/ILO20.pdf), Sections 1.1 and 4.1 (gate-size and output-component conventions).
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://doi.org/10.1145/3538391), for the scope of the locality barrier.
