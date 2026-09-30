# C-402 — Promise subfunctions do not charge shared DAG gates

Date: 30 September 2026  
Status: proved promise lemma and two route-specific obstructions; **no OPS frontier improvement**

## 1. Target and scope

The active target remains the ordinary fan-in-two Boolean circuit version of Oliveira–Pich–Santhanam (OPS): with `N=2^n`, `s1=N^beta/(c n)` and `s2=N^beta`, prove one fixed `epsilon>0` such that for every sufficiently small fixed `beta>0`, no circuit of at most `N^(1+epsilon)` total gates separates the YES and NO sets. The theorem has a universal constant `c`; its proof instantiates `c=10`. OPS allows arbitrary circuit depth and free fanout; the middle band is unconstrained. See [OPS, Theorem 1.4 and the proof of Lemma 4.1](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf). This cycle does not use fusion or infer a native-state bound.

## 2. Mechanism: promise incompatibility across input blocks

Let `Pi=(Y_1,Y_0)` be any promise problem on `M` Boolean input bits, with undefined output outside `Y_1 union Y_0`. Fix a partition of the coordinates into nonempty disjoint blocks `B_1,...,B_k`. For block `B_i`, a context is an assignment `z` to all coordinates outside `B_i`. Its partial restriction `p_(i,z)` is defined on `u in {0,1}^{B_i}` precisely when `(u,z)` is promised, and then has value 1 on YES and 0 on NO.

Define the **incompatibility graph** `G_i`: its vertices are contexts with at least one promised completion, and two contexts `z,z'` are adjacent if some common block assignment `u` is promised in both contexts with opposite labels. Let `chi_i=chi(G_i)` and

```text
Lambda(Pi; B_1,...,B_k) = sum_i log_2(chi_i).
```

This is promise-aware: an edge only uses two points where the promise fixes opposite answers. No completion of the middle band is chosen in the definition.

### The valid separator lemma

If a total circuit `C` separates `Pi`, its restrictions `C_(i,z)(u)=C(u,z)` give a proper coloring of `G_i`: adjacent contexts cannot induce the same restricted Boolean function, because they disagree at a common promised assignment. Hence

```text
chi_i <= |{ C_(i,z) : z a context }|.
```

If `C` has `S` fan-in-two AND/OR/NOT gates, every restriction still has at most `S` gates; hardwiring context inputs costs no gates (or `O(1)` if the convention requires explicit constants). There are at most `2^(O(S log(S+M)))` functions on a block computable by such circuits, by counting gate types and predecessor indices. Therefore the proved share-robust consequence is only

```text
log chi_i <= O(S log(S+M))   for each i,
S >= Omega(max_i log chi_i / log(S+M)).
```

This controls each block separately and does not assume a separator outputs witnesses, descriptions, or a vector of answers.

### A promise-specific ceiling before any gate charging

Now let `Pi` be a restricted OPS promise on at most `N` free table bits. Let `K` be the number of YES tables. Each YES table is described by a size-`s1` circuit, so

```text
K <= 2^(O(s1 log(s1+n))) = 2^(O(N^beta)).
```

For a fixed block, at most `K` contexts have any YES completion: project every YES table onto its outside-block coordinates. Color each such context separately, and give all remaining contexts one extra color. The latter contexts have only defined 0 labels (or no defined labels), so no two of them conflict. Thus `chi_i <= K+1` and `log chi_i=O(N^beta)` for every block, regardless of its width. Since a partition of at most `N` coordinates has at most `N` blocks,

```text
Lambda <= O(N^(1+beta)).
```

For every proposed fixed `epsilon>0`, OPS requires the claim for fixed `beta` smaller than `epsilon`; at those parameters `Lambda=o(N^(1+epsilon))`. Consequently even an impossible ideal theorem charging one gate per unit of `Lambda` could not reach the requested uniform-in-small-beta exponent. Promise incompatibility is too low-information on the required parameter range before DAG sharing is considered.

This conclusion is not a lower bound for separators. It only rules out this statistic, with this charging target, as a route to the OPS exponent.

## 3. Strongest counterconstruction to additive charging: indirect storage access

The second obstruction is unrestricted sharing, even when the promise is total. Let `t` be a power-of-two parameter with `p=2^t`, and let `b` be a power of two with `b=Theta(p/t)`. Inputs consist of an address `a in {0,1}^{log b}`, `b` data blocks `x_0,...,x_(b-1)` each of `t` bits, and a `p`-bit lookup table `y`. Define

```text
ISA(a,x_0,...,x_(b-1),y) = y_[x_a],
```

where `x_a` is the block selected by `a` and is interpreted as an integer in `[p]`.

The number of input bits is `m=bt+p+log b=Theta(p)`. Partition the data bits into the `b` blocks `X_i`. After setting `a=i`, the restriction to `X_i` is `x -> y_[x]`. Varying `y` over all `p=2^t`-bit strings realizes every Boolean function on `t` bits, so each block has at least `2^p` distinct subfunctions and

```text
sum_i log_2 r_(X_i)(ISA) >= b*p = Theta(p^2/t) = Theta(m^2/log m).
```

Nevertheless `ISA` has an `O(m)` ordinary fan-in-two circuit: use `t` balanced `b`-to-1 multiplexers to select the `t` bits of `x_a`, followed by one `p`-to-1 multiplexer selecting `y_[x_a]`. A binary mux costs a constant number of AND/OR/NOT gates, and `bt=Theta(p)`, so the total is `O(p)=O(m)`. This is a direct counterexample to any universal constant-factor claim `S >= c Lambda`, including the total partial-function version above (a total function is a special promise problem). It exposes the exact missing resource: subfunction computations for different blocks reuse the same selector and lookup DAG.

The construction is the standard indirect-storage-access phenomenon. Savage's circuit-complexity chapter gives the linear-size mux construction and the matching `Theta(m^2/log m)` Nechiporuk formula count. Gal and Robere explicitly explain that the method works for formulas/branching programs because their block-labeled leaves/nodes are disjoint, and that it does not directly apply to general circuits because subcomputations overlap; they cite Uhlig's small-circuit/high-subfunction construction. See [Savage, Chapter 9](https://cs.brown.edu/people/jsavage/book/pdfs/ModelsOfComputation_Chapter9.pdf), [Gal–Robere, ECCC TR19-128](https://eccc.weizmann.ac.il/report/2019/128/download/), and [Uhlig, FCT 1991](https://doi.org/10.1007/3-540-54458-5_84). The promise conflict graph is a useful formalization of partial restrictions, not a claimed new circuit lower-bound method.

## 4. Required construction attacks

The requested families do not rescue an additive charge:

* **Parity:** every block restriction is parity or its complement, so each `chi_i<=2`; a running XOR computes the whole predicate in `N-1` XOR gates, and each XOR has a constant-size AND/OR/NOT implementation, giving `O(N)` ordinary gates.
* **Repeated-block equality:** a block restriction is equality to a fixed reference block or the constant-zero function; summing the logarithms is `O(N)`, and coordinate comparisons plus one conjunction use `O(N)` gates.
* **Sparse parity checks:** for a bounded-degree system with `O(N)` incidences, each block restriction is an affine system. Its distinct right-hand sides contribute at most `2^(rank(H|B_i))`, so `sum_i log chi_i<=sum_i |B_i|=N`; compute the sparse syndrome with `O(N)` XOR gates, translate each XOR to a constant-size AND/OR/NOT circuit, then combine the checks in `O(N)` more gates.
* **Simple global block relations:** if every block is a known copy/complement of a reference block, each block has at most `2^{|B_i|}+1` relevant restrictions; the profile is `O(N)` and direct comparisons give an `O(N)` test.

These examples are calibrations, not counterexamples to the Gap-MCSP objective. ISA is the decisive counterexample to charging block restriction information to total DAG gates.

## 5. Paired full-promise upper-bound attempt

Try to exploit common work across all size-`s1` candidate descriptions. Let `K` be their syntactic count. An exact separator is

```text
OR over candidates D of [ AND over all N addresses a of (input[a] = D(a)) ].
```

Each candidate equality costs `O(N)` ordinary gates, so this gives `O(NK)=O(N 2^(O(N^beta)))` gates. Input bits can be wired to all candidate tests without a fanout charge, and the candidate tables can be hardwired. This shares the *input* values but leaves K candidate-specific equality outcomes and conjunctions. The alternate direct implementation—instantiate a universal circuit to evaluate each candidate at each address—costs `O(K N s1)` gates with the straightforward evaluator and is worse. These two explicit architectures give no factorization to `N polylog N`; they do not prove that every full-promise separator needs exponential size.

Gate count, description length, and runtime remain distinct. A gate-list representation can use `O(KN log(KN))` bits; those bits are not OPS gate cost. Enumerating descriptions to construct the separator takes exponential time. This attempt is a valid full-promise upper bound (it may reject middle inputs), not a near-linear separator. No native cover is claimed or inferred.

## 6. Computation model, barriers, and exact result

`S` above is total ordinary Boolean gates with fan-in two and unbounded depth/fanout. The proof does not convert XOR-only or formula complexity to this measure. It says nothing new about wires, circuit descriptions, runtime, fusion count `q`, paid AND states, free OR operations, endpoints, or cyclic LFP semantics. Thus the native full-promise frontier remains `q>=N-o(N)`; C-319's arbitrary endpoints, wide seeds, reuse, cycles, and every required semi-filter extension remain necessary for any separate native claim.

The locality barrier is not a theorem against all lower-bound techniques; C-401 records its exact scope. Here the route-specific literature obstruction is more direct: classical subfunction counting is additive when the model has a disjoint per-block cost, while unrestricted DAG sharing invalidates that accounting. The comparator-circuit result of Gal–Robere succeeds only after using a special model-specific relationship between wires and gates; its wire lower bound is not an ordinary Boolean-gate lower bound and gives no direct OPS transfer.

**Strongest proved statement in this cycle:** for any partial promise and any block, the incompatibility chromatic number is bounded by the number of distinct restrictions of every total separator; on a restricted OPS promise, the sum of its logarithms is at most `O(N^(1+beta))`. Independently, the total-function ISA construction has a `Theta(m^2/log m)` subfunction profile and only `O(m)` ordinary gates, falsifying additive profile-to-DAG charging.

**Exact frontier effect:** none. No fixed `epsilon>0` ordinary `N^(1+epsilon)` lower bound, no near-linear full-promise separator/native cover, and no P-vs-NP result. The C-401 ordinary OPS threshold remains the frontier; native `q>=N-o(N)` remains secondary and unchanged.

**Mechanism decision:** retire promise subfunction/incompatibility sums as a source of the required OPS lower bound. Keep only the per-block restriction-coloring lemma as a reusable diagnostic. The next ordinary-circuit attempt must account for a whole shared DAG globally, not add independently counted block descriptions; it must also obtain information exceeding the `O(N^(1+beta))` low-set ceiling when beta is arbitrarily small. No additive “non-shareability” assumption is introduced.

No finite experiment was used: every claim above is an asymptotic proof or an explicit circuit construction.
