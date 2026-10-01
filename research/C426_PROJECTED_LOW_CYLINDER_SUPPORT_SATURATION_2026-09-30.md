# C-426 - Projected Low cylinders saturate the support obstruction

Date: 30 September 2026  
Status: proved support-scale refinement; **no superlinear gate bound and no OPS-frontier change**

## Exact target convention

Set `N=2^n`, `s1=N^beta/(10n)`, and `s2=N^beta`, with fixed `0<beta<1`. YES means `CC(f)<=s1`; NO means `CC(f)>s2`, so the first integer NO size is `floor(s2)+1`. OPS Theorem 1.4 uses this strict-`>` convention. Its quantifiers require one fixed `epsilon>0` such that, for every sufficiently small fixed `beta>0`, the ordinary fan-in-two total-gate complexity of Gap-MCSP exceeds `N^(1+epsilon)`; this implies `NP not subseteq P/poly` ([OPS, Theorem 1.4 and Definition 2.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)).

The `10n` denominator is the concrete instantiation used in OPS's proof. The theorem is about ordinary total gates. Nothing below transfers to native fusion states, OR operations, wires, or cycle closure.

## Mechanism tested: essential-input support as a computation potential

For a separator `C`, let `E(C)` be the number of essential truth-table inputs. The C-403 argument gives, for every valid separator,

```text
E(C) >= N - O(s2*n),       S(C) >= E(C)-1,
```

where `S(C)` is the number of ordinary fan-in-two gates. Indeed, `0^N` is Low, so changing any subset of the inessential coordinates leaves `C` accepting. Every table in that accepted subcube must have complexity at most `s2`, because a table of complexity greater than `s2` is a promised NO. Circuit counting bounds the number of such tables by `2^(O(s2*n))`; hence there are at most `O(s2*n)` inessential coordinates. The connected output-cone DAG then gives `S(C)>=E(C)-1`.

This is a legitimate shared-circuit invariant: it counts distinct essential inputs, not occurrences, and the graph argument permits arbitrary fanout. Its decisive limitation is equally exact: `E(C)<=N`, so this potential cannot yield more than a linear gate lower bound. The construction below shows the `O(s2*n)` support deficit is attainable in order even by a complete separator.

## Full-promise separator that ignores a block

Choose a fixed prefix `p` of the `n`-bit address and let

```text
B = { x in {0,1}^n : x has prefix p },   |B|=2^d.
```

Choose `d<n` so that `2^d=Theta(s2*log s2)` and every `d`-input Boolean function has a fan-in-two circuit of at most `Delta=s2/8` gates. This is possible by Lupanov synthesis: an arbitrary `d`-bit function has size `O(2^d/d)`; the fixed prefix mask costs `O(n)` more gates. Since `beta<1` is fixed, `d=beta*n+O(log n)<n` for sufficiently large `n`, and `n=o(s2)`. The classical source is Lupanov's 1958 synthesis result ([MathNet record and scan](https://www.mathnet.ru/php/archive.phtml?jrnid=tm&option_lang=rus&paperid=1277&wshow=paper)). This is the same safe-subcube scale already calibrated in C-230/C-231; I use it here rather than claim a new Lupanov bound.

For a table `w`, write `pi_B(w)` for its restriction to addresses outside `B`, and define

```text
L_B = { pi_B(g) : CC(g)<=s1 }.
C_B(w) = 1 iff pi_B(w) is in L_B.
```

**Claim.** `C_B` is a valid separator for the complete OPS promise and is independent of every input bit indexed by `B`.

**Proof.** Every Low table `w` has `pi_B(w) in L_B`, so it is accepted. If `C_B(w)=1`, choose a Low table `g` with `pi_B(g)=pi_B(w)`. On `B`, let `h` be the suffix function giving the values of `w`. A circuit for `w` is

```text
(not P_B AND g) OR (P_B AND h),
```

where `P_B` tests the fixed address prefix. Its size is at most `s1+Delta+O(n) < s2` for all sufficiently large `n`. Thus every accepted table has complexity strictly below `s2`, and in particular no promised NO table is accepted. Middle-band tables may receive either answer, as permitted. Since `C_B` reads only coordinates outside `B`, all `|B|=Theta(s2 log s2)=Theta(N^beta*n)` bits in `B` are inessential. QED.

Combining this with C-403 pins down the *order* of the smallest possible essential support (equivalently, the largest possible inessential support):

```text
min over valid C of E(C) = N - Theta(N^beta*n)
```

for each fixed `0<beta<1`. So some complete separator has `Theta(N^beta*n)` inessential coordinates, and no separator can have more than `O(N^beta*n)` of them. An argument that tries to force a separator to use more than `N-O(N^beta log N)` distinct table coordinates is exhausted. This is a support result only; it is not a statement about total gates beyond the already-known linear floor.

## Strongest counterconstruction and full-promise cost

The projected separator can be implemented by enumerating all descriptions of size at most `s1`. For each candidate circuit `D`, compare the input's `N-|B|` retained bits with the hardwired trace `pi_B(TT(D))`, then OR the equality tests.

Let `M<=2^(O(s1*log(s1+n)))=2^(O(N^beta))` be the number of candidate descriptions. Then the explicit implementation has:

| Resource | Bound |
|---|---:|
| Ordinary total fan-in-two gates | `O(NM)=O(N*2^(O(N^beta)))` |
| Wires | `O(NM)` |
| Gate-list description bits | `O(NM*log(NM))` |
| Direct construction time | `O(NM*(s1+log(NM)))` |
| Inputs used | At most `N-|B|` |

This is a valid complete separator but not a near-linear one. Its direct implementation matches the existing Low-description enumeration scale; projecting away `B` does not make this construction cheaper. This is not a lower bound on the optimum circuit size of projected membership: another circuit for that predicate, or a different full-promise separator, could be smaller. It is the strongest counterconstruction to the support-potential mechanism found in this cycle, not a counterexample to the OPS lower-bound program.

## Shared-computation adversarial checks

No incidence-count charge survived the standard reuse canaries:

* XOR/parity of `N` table bits uses `N-1` XOR gates and reuses each partial parity; an address-parity truth table is also Low at the OPS scale.
* Equality of repeated blocks can be checked against representatives with `O(N)` gates, regardless of how many repeated positions an expanded constraint list names.
* A family of sparse parity checks with total incidence `L` has an `O(L+r)` shared XOR/readout circuit for `r` checks; when `L+r=O(N)`, the full check is linear.
* Copy, complement, and bounded-incidence XOR relations among blocks can be verified with `O(N+T)` gates, where `T` is the seed-relation computation cost. Repeated coordinates do not create a separate gate charge.

These are gate-level counterexamples to counting equations or local inconsistencies independently. The examples are not complete Gap-MCSP separators; `C_B` above is the complete construction and pays exponentially in `N^beta`.

## Why the next proof step is not automatic

For a *particular* separator `C`, C-231's deep-Low block gives a valid robust projection `R_C(p)=AND_u C(p,u)`: every completion of a sufficiently deep Low anchor is Low and accepted, while a projected High fiber has at least one rejected High completion. But the direct implementation uses `2^|F|` cofactors of `C`; unrestricted reuse does not itself give a smaller circuit for this universal quantifier. Conversely, the existence of the canonical projected-membership separator `C_B` does not imply every separator computes `L_B`, because a general separator may use the middle band and the deleted coordinates differently. No gate inequality from arbitrary `C` to `R_C` is proved here. Do not assume such a compiler or call it a non-shareability principle.

The locality barrier is technique-specific: Chen et al. explain why certain lower-bound methods that extend to small-fan-in oracle gates cannot prove the relevant magnification frontiers; it is not a theorem ruling out all global total-gate arguments ([Chen et al., primary paper](https://eccc.weizmann.ac.il/report/2019/168/download/)). C-426 neither bypasses nor strengthens that barrier. Originality classification: the safe block follows from the established Lupanov construction and prior C-230/C-231 project lemmas; the new cycle-level statement is the explicit full-promise projection separator and the resulting tight order of the essential-support deficit. It is a direct synthesis/corollary, not a new circuit lower-bound technique.

## Exact effect and next obligation

**Strongest proved statement:** a full-promise separator can ignore `Theta(N^beta log N)` truth-table inputs, and every separator has at most `O(N^beta log N)` inessential inputs. Thus the minimum essential-support size is `N-Theta(N^beta log N)`. The construction has `O(N*2^(O(N^beta)))` total gates.

**No frontier change:** ordinary lower bound remains `S>=N-O(N^beta log N)-1` plus C-406's additive logarithmic refinement; the OPS `N^(1+epsilon)` target remains open; the exact full-promise upper remains `O(N*2^(O(N^beta)))`; native `rho>=N-o(N)` remains separate. No result about paid AND states, OR operations, wires, arbitrary semantic endpoints, unrestricted cyclic reuse, or semi-filter extensions follows.

Retire essential-input support, cylinder width, and safe-block size as candidates for the superlinear gate charge. The next ordinary-gate cycle must use a genuinely gate-semantic feature beyond support and certificate count, or exhibit a full-promise separator below the current enumeration scale. Any proposed robust-fiber reduction must prove its gate inequality for arbitrary separators and preserve all middle inputs; do not posit it as an assumption.
