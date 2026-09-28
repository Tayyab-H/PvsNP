# C-291 - Updated ODDFACTOR source window and auxiliary-witness sidecar no-go

Date: 28 September 2026  
Classification: **SOURCE UPDATE / ROUTE FILTER.**  
Status: strengthens the candidate hard source and isolates a bad augmentation; no C-125 map or Gap-MCSP lower-bound improvement.

## 1. Literature update: ODDFACTOR is exponentially hard for monotone circuits

C-288 records the older Babai-Gal-Wigderson bound `m^(Omega(log m))`. Cavalar, Göös, Riazanov, Sofronova, and Sokolov later proved that bipartite perfect matching on side size `v` needs monotone circuits of size at least

```text
2^(v^(1/3-o(1))).
```

Their Theorem 2 transfers this lower bound to ODDFACTOR: on the support of their odd-cut distribution, perfect matching and ODDFACTOR agree pointwise, so the same approximation argument applies. The paper states the ODDFACTOR consequence as `2^(v^Omega(1))`. ODDFACTOR remains in deterministic logspace and has a linear-size monotone `GF(2)` span program. Thus its known span-program/monotone-decision gap is exponential, stronger than the earlier quasipolynomial statement in C-288.

## 2. The stronger source also survives cyclic closure

For `q` paid states in the native cyclic intersection model on `M=Theta(v^2)` graph inputs, the established unrolling gives an ordinary monotone circuit of size

```text
S <= C q^2 (M+q).
```

If `q<v^2`, this is polynomial in `v`, contradicting the exponential ODDFACTOR lower bound. Hence `q>=v^2` for large `v`; then `S<=C' q^3`, and the same lower bound implies

```text
CycAnd(ODDFACTOR_v) >= 2^(v^Omega(1)).
```

The polynomial unrolling loss changes the constant in the exponent, not the superpolynomial scale.

Choose `v=(log N)^K` for a fixed `K` large enough that `Kc>1`, where `c>0` is any fixed exponent furnished by the source lower bound. A low witness odd-factor edge set has a solution supported on at most `2v` edges: take a linearly independent subfamily spanning the target. Its truth-table indicator has circuit size

```text
O(v log N / log v)=polylog(N),
```

so it lies in `SIZE(s1)` for every fixed `beta>0` and all sufficiently large `N`. Meanwhile the cyclic source lower bound is

```text
2^((log N)^(Kc-o(1))),
```

which dominates every fixed polynomial in `N`. Therefore a C-125 encoder of polynomial AND-cost would give a very strong transfer. This is a source-parameter opportunity only; the encoder remains the missing object.

## 3. Exact failure of the obvious dual-witness sidecar

One tempting repair is to append an explicit dual certificate to each source input and let it select a high table. If YES inputs set every auxiliary dual-rail variable to `1`, while NO inputs use a consistent one-hot encoding, this augmentation destroys the source lower bound before the C-125 transfer is used.

For auxiliary bits `(y_i^0,y_i^1)_{i=1}^r`, the monotone circuit

```text
H(y) = AND_{i=1}^r (y_i^0 AND y_i^1)
```

uses `2r-1` AND gates, accepts the YES top vector, and rejects every consistent one-hot NO encoding. It ignores the graph and the advertised dual certificate. If the auxiliary block is the full `N`-coordinate table rail vector, the same shortcut costs at most `2N-1` AND gates. In the proposed `v=polylog(N)` source window, either cost is far below `CycAnd(ODDFACTOR_v)`.

This remains true even if an affine hash maps each supplied dual witness to a high-complexity table and the rail encoder computes that hash cheaply: the source separator can still inspect only the auxiliary top-versus-one-hot pattern. High completion complexity does not preserve source hardness when the decoy selector is explicitly visible as a monotone side channel.

## 4. Consequence for the next construction

The useful part of the ODDFACTOR lead is now quantitative: a polynomial-cost C-125 map would be far below the source's cyclic decision complexity, with low YES witness tables fitting the OPS parameters. The failed part is adding a freely visible dual certificate. A surviving map must derive its NO-side partial rails monotonically from the original hard input (or use an auxiliary encoding for which no comparably cheap monotone separator exists), while keeping every NO image below a high completion and every YES image above a low code.

No such map, `CohEnc` separation, native owner-mask rank bound, near-linear full-promise cover, superlinear `q` bound, or P-versus-NP proof follows here. The actual fusion bound remains `q=N-o(N)`.

Primary source: Cavalar, Göös, Riazanov, Sofronova, and Sokolov, [*Monotone Circuit Complexity of Matching*, ECCC TR25-102](https://eccc.weizmann.ac.il/report/2025/102/download), Theorems 1-2 and Section 3.3. ODDFACTOR's linear `GF(2)` span program is from Babai-Gal-Wigderson, [*Superpolynomial Lower Bounds for Monotone Span Programs*](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/GAL/SPAN/COMBINATORICA/final.pdf).
