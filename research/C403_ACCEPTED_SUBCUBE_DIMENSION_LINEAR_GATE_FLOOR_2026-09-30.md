# C-403 — Sparse non-High region forces almost every input to matter

Date: 30 September 2026  
Status: proved ordinary-circuit lower bound `N-o(N)`; **no superlinear OPS bound**

## 1. Target

Keep the exact OPS Gap-MCSP parameters: `N=2^n`, low threshold `s1=N^beta/(c n)`, high threshold `s2=N^beta`, with one fixed `epsilon>0` sought for every sufficiently small fixed `beta>0`. A separator is any total fan-in-two AND/OR/NOT circuit that accepts every table of circuit size at most `s1` and rejects every table of circuit size at least `s2`; its output on the middle band is free. OPS counts total gates, while input fanout is unrestricted. See [OPS, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).

## 2. Mechanism: a low-accepting subcube cannot have many free coordinates

Let `C` be any valid separator and let `E(C)` be the number of essential truth-table input bits of its Boolean output function. Use the all-zero table `0^N` as a fixed low input, so `C(0^N)=1`. Let `U` be the set of inessential input bits. If the essential bits are fixed to zero and the bits in `U` vary arbitrarily, `C` remains 1 on the whole resulting subcube of size `2^|U|`.

Every point in this accepted subcube must have circuit complexity strictly below `s2`; otherwise it is a promised NO input. The number of `n`-input Boolean functions of circuit size less than `s2` is at most the number of their fan-in-two circuit descriptions:

```text
K2 <= 2^(O(s2 log(N+s2))) = 2^(O(N^beta log N)).
```

Therefore `2^|U|<=K2`, so

```text
|U| <= O(N^beta log N),
E(C) >= N - O(N^beta log N).
```

This argument uses only the forced output on low and high inputs; it makes no choice for the middle band. For fixed `beta<1`, `N^beta log N=o(N)`, so every valid separator depends essentially on `(1-o(1))N` of the table coordinates.

### Convert essential inputs to ordinary total gates

Trim `C` to the ancestor DAG of its output. If its output is a gate, let `S'` be the number of gates in this cone, `I` the number of primary-input vertices with a path to the output, and `c<=2` the number of distinct constant sources. The underlying graph is connected, has `S'+I+c` vertices, and has at most `2S'` wires because each gate has fan-in at most two. Hence

```text
S'+I+c-1 <= 2S',    so    S' >= I+c-1 >= E(C)-1.
```

If the output is directly an input or a constant, it has at most one essential input, which is impossible once `N-O(N^beta log N)>1`. Thus every separator obeys

```text
S(C) >= N - O(N^beta log N) - 1 = (1-o(1))N.
```

The constants in `O(.)` are independent of `N` for each fixed beta and the fixed circuit-description convention. This is a proved lower bound in the requested ordinary total-gate model.

## 3. Adversarial checks and the ceiling of this mechanism

The support argument is sharp in scale. A circuit recognizing one fixed table by conjunction of its `N` signed input literals has `N-O(1)` gates, depends on all `N` bits, and has an accepting set with one point. Thus almost-full essential support alone cannot force more than linear size.

There is also a promise-specific near-linear subpromise separator. If `r=floor(s1/(C n))` for a sufficiently large constant `C`, every table of Hamming weight at most `r` has a minterm DNF of size `O(rn+n)<s1`, hence is a genuine YES table. The circuit that tests whether the input table has weight at most `r` accepts this entire sparse YES subfamily and rejects every actual high table, since no table below weight `r` can have circuit complexity at least `s2`. A binary adder tree computes the weight threshold using `O(N)` ordinary gates. This shows that broad acceptance of a structured low subfamily plus rejection of all high tables can coexist with linear cost; it is not a full-promise separator because it rejects low tables such as parity.

An equivalent decision-tree corollary holds: on the path for any low input, a deterministic decision tree separator must query at least `N-O(N^beta log N)` bits, since its accepting leaf is a subcube containing no high table. The corollary is about adaptive queries, not a superlinear Boolean-circuit lower bound.

The decisive obstruction is now explicit. Counting the non-High set forces nearly every input coordinate into the separator's support and yields `N-o(N)` gates. But there are only `N` input coordinates, so this mechanism is exhausted at the linear scale. It says nothing about repeated use, gate-to-gate interactions, or how a circuit computes the joint low-table membership predicate after reading its inputs. C-402's ISA example remains the hostile countercheck against converting independent block information to additive DAG work.

## 4. Paired full-promise upper attempt

The exact full-promise upper construction still enumerates every size-`s1` circuit description `D` and tests equality of the input table to `TT(D)`:

```text
OR_D AND_{a in {0,1}^n} [ T[a] = D(a) ].
```

It accepts every low table, rejects every high table, and may label the middle either way. With `K1<=2^(O(s1 log(s1+n)))=2^(O(N^beta))` descriptions, its ordinary gate cost is `O(N K1)=O(N 2^(O(N^beta)))`. Its candidate truth tables are hardwired; its gate count, wire list/description bits, and exponential construction time are separate quantities. This is not a near-linear separator. The sparse-weight threshold above only separates a restricted YES subfamily, so it cannot replace enumeration for the full promise.

## 5. Exact effect on the frontier

**Strongest proved statement:** every OPS separator has at least `N-O(N^beta log N)-1` ordinary fan-in-two gates, for every fixed `0<beta<1`. Equivalently, it has `(1-o(1))N` gates. The key invariant is the dimension of an accepting subcube, bounded by the logarithm of the number of non-High tables.

**Not proved:** any `N^(1+epsilon)` bound, a near-linear full-promise separator, a native fusion improvement, or `P != NP`. C-319's paid AND states, OR operations, wires, semantic endpoints, wide seeds, unrestricted reuse, cycles, and all required semi-filter extensions are not analyzed by this ordinary-circuit argument. The native full-promise `q>=N-o(N)` frontier remains separate and unchanged.

The new mechanism is useful as an ordinary-gate baseline and a falsification test, not as a candidate proof of the OPS magnification hypothesis. To reach the required exponent, a future argument must charge computation beyond the mere presence of the `N` input coordinates.
