# C-452 - simple-extension decision has easy no-instances inside OPS-Low

**Date:** 1 October 2026  
**Question:** Can the total `f`-Simple Extension problem provide an ordinary Gap-MCSP source map?  
**Result:** A full-input-dependent counterexample with a valid key shows that identity truth-table encoding does not preserve the OPS NO endpoint, even for `f=OR_n`. Both a YES simple extension and a NO non-simple extension have `O(n)` circuit size on `n+1` inputs, while the OPS Low threshold at their truth-table length is exponential in `n`. This retires the direct identity transfer, not every transformed reduction.

## 1. Source problem and required transfer

For a nondegenerate base function `f` on `n` inputs and `m` extension inputs, the total `f`-Simple Extension problem asks whether a truth table `g(x,y)` satisfies all three conditions:

1. `g` depends on every input;
2. `CC(g)=CC(f)+m`;
3. some key `k` satisfies `g(x,k)=f(x)` for every `x`.

This framework is relevant because a positive answer is specified by an exact circuit-size condition plus a key restriction. However, using `g` itself as the Gap-MCSP truth table would require every no-instance of `f`-SEP to have `CC(g)>N^beta`, where `N=2^(n+m)`, while every yes-instance is below `N^beta/(c(n+m))`. The definition of `f`-SEP does not provide that NO-side complexity promise.

## 2. Counterconstruction that survives the easy syntactic filters

Take `f(x)=OR_n(x)` with `n>=3` and one extension bit `y`. Its exact circuit complexity in the fan-in-two AND/OR/NOT total-gate model is `CC(f)=n-1`: an OR chain is an upper bound, and dependence on `n` inputs requires at least `n-1` binary gates. The function

```text
g_yes(x,y) = OR_n(x) OR y
```

is a YES instance: it depends on all `n+1` inputs, has size `n=CC(f)+1`, and restricts to `f` at key `y=0`.

Now define

```text
g_no(x,y) = OR_n(x) XOR (x_1 AND y).
```

This is a NO instance even though it passes both simple checks often used to preprocess `f`-SEP inputs:

* It depends on every input. For `y=0`, it is `OR_n`; hence every `x_i` is essential. For `x_1=1`, its value changes with `y`, so `y` is essential.
* It has a valid key: `g_no(x,0)=OR_n(x)` for all `x`.
* It is not simple because its circuit complexity is greater than `n=CC(f)+1`. It is nonmonotone in `y` (at `x_1=1`, changing `y` from 0 to 1 changes output 1 to 0). Any circuit on `n+1` essential inputs needs at least `n` binary gates to connect all those inputs to the output; NOT gates do not join two dependency components. A circuit with at most `n` total gates must therefore have exactly `n` binary gates and no NOT gates. After removing irrelevant gates, its undirected dependency graph has `2n+1` vertices (`n+1` inputs and `n` gates) and `2n` wires, so it is a tree. Rooting this tree at the output shows each input and intermediate signal is used once; the circuit is a read-once AND/OR formula and is monotone. Therefore `g_no` cannot have size `n` or less.
* It nevertheless has size at most `n+5`: compute `OR_n` in `n-1` OR gates, `x_1 AND y` in one AND gate, and XOR the two results using five AND/OR/NOT gates. Thus `n+1 <= CC(g_no) <= n+5`.

This proof distinguishes simple from non-simple without assuming a particular optimal implementation. The NO example is nondegenerate and has a key; its failure is solely that its size is a few gates above the exact target.

The obstruction survives padding to any number `r>=1` of extension inputs. Let

```text
g_r(x,y) = OR_n(x) XOR (x_1 AND OR_r(y)).
```

It is nondegenerate, has key `y=0^r`, and is nonmonotone in each `y_j`. The exact simple-extension size would be `CC(OR_n)+r=n+r-1`. Since `g_r` depends on all `n+r` inputs but is nonmonotone, it cannot be computed with the minimum `n+r-1` gates; a direct circuit gives `n+r <= CC(g_r) <= n+r+4`. Its truth-table length is `2^(n+r)`, so `g_r` remains OPS-Low for every fixed beta once `n+r` is large. Padding the exact-extension instance with many essential key bits therefore does not create a High endpoint.

## 3. OPS endpoint calculation

The truth-table input length for either function is `N=2^(n+1)`. For each fixed `beta>0` and constant `c`,

```text
s1 = N^beta/(c log_2 N) = 2^(beta(n+1))/(c(n+1)),
s2 = N^beta = 2^(beta(n+1)).
```

Both `CC(g_yes)=n` and `CC(g_no)<=n+5` are at most `s1` for all sufficiently large `n`. Hence the direct map `g -> its truth table` sends this explicit f-SEP NO instance into OPS-Low, not OPS-High. The separation between the two `f`-SEP answers is an exact `m`-gate equality, while the OPS gap separates a cutoff of exponential scale from a much larger exponential cutoff. A constant additive circuit-size discrepancy cannot fill it.

This refutes the direct identity transfer from total `f`-SEP to OPS Gap-MCSP, including a proposal that simply filters out degenerate tables or tables with no key. It does **not** rule out a different transformation that amplifies the non-simple side, nor does it prove that any such amplification is impossible.

## 4. Broader perturbation lemma and what it demands

The example is not tied to OR. Suppose `f` has distinct 1-inputs `a_0,a_1`, and every input variable has at least two distinct sensitive edges. For `m>=1`, let `p(y)` be parity and set

```text
g(x,y) = f(x) XOR [ x = a_{p(y)} ].
```

Every fixed `y` slice differs from `f` at exactly one 1-input, so there is no key. Parity makes each new `y_j` essential. A point modification removes at most one sensitive edge in each input direction, so the hypothesis preserves essentiality of every original input. A circuit for `g` uses a circuit for `f`, parity on `m` bits, two equality tests on `n` bits, and a constant-size selector/XOR, giving
`CC(g) <= CC(f)+O(n+m)`.

Therefore, whenever a proposed base size satisfies `CC(f)+O(n+m) <= s1`, its simple-extension NO set already contains OPS-Low truth tables. This is an endpoint obstruction to identity encoding even beyond the specific OR example. Any replacement map must amplify **every** such low-complexity NO case, not just establish hardness of deciding exact simple extensions.

## 5. Literature check and paired upper construction

Carmosino, Dang, and Jackman prove that total `f`-Simple Extension is in polynomial time when optimal circuits for `f` have linear size, bounded fan-out, and efficiently enumerable polynomially many forms; they apply this to `OR_n` and `XOR_n`. They identify multiplexers and superconstant fan-out as possible next candidates. Their result is an algorithmic classification of selected exact-extension problems, not an OPS lower bound. The counterexample above adds a gap-specific point: even an `f`-SEP base with an intricate exact-size condition supplies no OPS High endpoint merely from being non-simple. [Primary paper](https://arxiv.org/abs/2511.16903).

Paired full-promise construction: the exact separator that accepts precisely `L_s1` enumerates all Low circuit descriptions and checks all `N` table bits. Its fan-in-two size is `O(N 2^(O(N^beta)))`; it handles every promised YES and NO table, but is not near-linear. No shorter full-promise separator was constructed here. This is the same upper bound audited in C-451, not a new algorithm.

The OPS theorem still requires the same fixed `epsilon>0` for every sufficiently small fixed `beta`, at `s1=N^beta/(c log N)` and `s2=N^beta`; no result in this cycle changes that frontier. [OPS, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf). The locality barrier constrains specified local proof transfers, not every route; this exact-extension failure is a separate endpoint mismatch. [Chen et al.](https://eccc.weizmann.ac.il/report/2019/168/).

## 6. Strongest proved statement and next action

**Project-proved:** `f=OR_n` has a valid-key, nondegenerate `f`-SEP NO instance `g_no` with `n+1 <= CC(g_no) <= n+5`; at its truth-table length, that NO instance is OPS-Low for every fixed `beta>0` eventually. A broader point-perturbation lemma gives low-complexity non-simple extensions for robust base functions.

**Counterexample scope:** direct identity encoding and simple padding that preserves an `O(n+m)` description. This is not a counterexample to an arbitrary gap-amplifying reduction, to OPS, or to P vs NP separation.

**Frontier:** unchanged. Ordinary separator lower bound `N-O(N^beta log N)-1` plus C-406's logarithmic reconvergence refinement; common-fixed-epsilon OPS target open; full-promise upper `O(N 2^(O(N^beta)))`; native `rho>=N-o(N)` separate. No P-vs-NP result.

The `f`-SEP literature branch should not be pursued by choosing a more complicated base function alone. Before studying a multiplexer or another high-fan-out base, specify a transformation and prove a gap theorem that sends *all* non-simple inputs to High despite near-optimal perturbations such as `g_no`. The unresolved mechanism is gap amplification under unrestricted circuit sharing, not exact optimal-circuit enumeration by itself.
