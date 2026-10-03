# C-462 â€” A random coordinate slice around a Low table has a simple separator

**Date:** 1 October 2026  
**Question:** Can a coordinate-subcube restriction through a Low table expose a hard source trace for the OPS promise?  
**Result:** There exists a common random free-coordinate set for which every Low completion is sparse relative to every Low anchor, while every promised High completion is farther away. A weight threshold separates the induced promise with a sublinear-size circuit. This generalizes C-407 from the zero anchor; it is a project-proved restriction lemma, not a bound on full Gap-MCSP.

## 1. Exact model

Let `N=2^n`, with OPS thresholds

```text
s1 = N^beta/(c*n),       s2 = N^beta,
```

where `c` is the fixed OPS constant and `beta>0` is fixed. The full separator must accept every table of circuit size at most `s1` and reject every table of circuit size greater than `s2`; the middle band is free. Fix an arbitrary anchor table `T0` with `CC(T0)<=s1`.

For a coordinate set `B subseteq [N]`, consider the subcube

```text
Q(B,T0) = { T : T[i]=T0[i] for every i outside B }.
```

Its `|B|` free bits encode the error vector `E=T XOR T0`, whose support is contained in `B`.

## 2. Counting makes Low completions sparse on a random slice

Fix a constant `delta` with `beta<delta<1`, and set `m=floor(N^delta)`. Choose `B` uniformly among the `m`-subsets of `[N]`. Let `K` be the number of functions on `n` variables with circuit size at most `2s1+O(1)`. Standard gate-description counting gives

```text
log_2 K = O(s1*log_2(n+s1)) = O(beta*n*s1)
```

for each fixed `beta` and all sufficiently large `n`.

For any fixed function `E` with support size `w`,

```text
Pr[supp(E) subseteq B] = (m)_w/(N)_w <= (m/N)^w.
```

Define

```text
rL = ceil((log_2 K + 2)/log_2(N/m)).
```

Since `rL+1 >= (log_2 K+2)/log_2(N/m)`, the union bound is at most `K(m/N)^(rL+1) <= 1/4`. Hence there exists a set `B` such that every such circuit function supported inside `B` has weight at most `rL`. This property depends only on the size-`2s1+O(1)` circuit class, not on the anchor, so the same `B` works for every `T0` of size at most `s1`.

If `T` is a Low completion in `Q(B,T0)`, then `E=T XOR T0` is computed by a circuit of size at most `CC(T)+CC(T0)+O(1)<=2s1+O(1)`. It is supported in `B`, so the selected slice guarantees

```text
CC(T)<=s1 and T in Q(B,T0)  =>  dist(T,T0)<=rL.
```

Since `log_2(N/m)=(1-delta)n+o(n)`,

```text
rL = O(beta*s1/(1-delta)).
```

## 3. High completions must be farther from the anchor

The C-458 patching lemma says changing `r` table entries costs at most `K0*r*(n+1)` gates for a universal constant `K0`. Therefore

```text
CC(T) <= CC(T0)+K0*dist(T,T0)*(n+1).
```

Choose

```text
rH = floor((s2-s1)/(2*K0*(n+1))).
```

For sufficiently large `n`, every completion at distance at most `rH` has circuit size strictly below `s2`. The formal OPS NO side is `CC(T)>s2`; this argument also rejects the boundary case `CC(T)=s2`. Thus

```text
CC(T)>=s2 and T in Q(B,T0)  =>  dist(T,T0)>rH.
```

As `s2/s1=c*n`, `rH=Theta(c*s1/K0)`. Since `rL/s1=O(beta/(1-delta))`, for every fixed `delta<1` there is a sufficiently small fixed `beta>0` such that `rL<rH`. The requirement `delta>beta` ensures `rH<m` eventually.

## 4. Complete separator for the restricted promise

On the free coordinates of `Q(B,T0)`, define

```text
Q(y)=1 iff wt(y)<=rH,
```

where `y` records which bits differ from `T0` on `B`. Every Low completion has weight at most `rL<rH`, and every promised High completion has weight greater than `rH`. Thus `Q` is a valid total separator for the promise *restricted to this subcube*. A fan-in-two population counter and comparison implement it in `O(m log m)=O(N^delta log N)` gates and wires. Naming its selected table inputs costs `O(m log N)` bits, and naming the anchor values on those inputs costs `O(m)` bits; a Low-circuit description of `T0` takes `O(s1 log(n+s1))` bits. These are description costs, not additional circuit gates. The random-set existence proof is nonuniform and does not claim efficient construction time.

This is stronger than the generic two-ball calibration in C-459: it uses circuit-description counting to control the Low completions and patching to control the High completions, for the actual OPS table promise. It still does not construct a separator on the full `N`-bit domain.

## 5. What this closes and what it does not

The result refutes the generic assumption that a coordinate subcube through a Low anchor is automatically a hard trace: it constructs one common free-coordinate set `B` for which all anchored slices have an explicit `O(N^delta log N)`-gate separator. It does not show every coordinate set gives easy slices; a specially selected structured slice could still induce a hard partial function. A proof that lower-bounds the minimum separator size on the constructed slices cannot yield the OPS superlinear bound.

It does **not** imply that an arbitrary full separator `F` has a small restriction: `F|Q` can be any valid extension and may be more complicated than the constructed weight threshold. It does not rule out non-coordinate restrictions, a family of restrictions with a proved joint gate charge, or a source map with its own exact endpoint proof. **Adversarial constructions.** `PARITY` and repeated-block equality both have `O(n)`-gate implementations and can serve as Low anchors `T0`; the theorem applies to the difference `E=T XOR T0`, not to the density or pattern of `T0`. For an attempted completion, take `E(x)` to be the indicator that `r` independent parity checks on the address bits all vanish. It has weight `N/2^r` and an `O(nr)`-gate circuit. With `r` near `(1-delta)n`, this weight is about `N^delta`, well above `rL`; the selected random `B` therefore cannot contain its entire support. The same test works for a block relation such as `E(x)=1` iff a fixed prefix of the address is zero, which has an `O(n)` circuit and support about `N^delta`. These structured examples would refute the sparsity property on a `B` chosen to contain their support, but they do not refute the existential random-`B` theorem. The exact-cardinality counterexample is `B={0,1,...,m-1}` in binary address order: its indicator compares `x` with the constant `m`, so has an `O(n)`-gate circuit and weight exactly `m >> rL`. Thus the property cannot hold for every coordinate set.

No assumption is made that `F` reconstructs a circuit or enumerates witnesses. The only charge in the proof is the ordinary gate count of the *constructed restricted separator*. Its gates, fixed-mask description, and offline choice of `B` are distinguished.

**Paired complete-separator construction attempt.** The exact full-promise baseline enumerates the `M=2^(O(s1 log(n+s1)))=2^(O(N^beta))` Low circuit descriptions, compares each candidate against all `N` table bits, and ORs the equality tests. This is complete, but costs `O(NM)` ordinary gates and wires. C-461 sorted-codebook binary-search attempt does not improve that circuit bound: sequential RAM comparisons hide pivot access, while an ordinary circuit must pay for pivot selection/muxing; rank-to-description unranking is also unproved. Thus this construction branch produces no near-linear full-promise separator.

## 6. Quantitative frontier

**New proved statement:** for each fixed `delta in (0,1)` and sufficiently small fixed `beta<delta`, there is one coordinate set `B` of size `N^delta` such that, around every Low anchor `T0`, the OPS promise restricted to `Q(B,T0)` admits an `O(N^delta log N)`-gate separator.

**Full problem:** unchanged. The ordinary lower bound remains `N-O(N^beta log N)` with C-406's additive logarithmic reconvergence refinement. Exact full-promise enumeration remains `O(N*2^(O(N^beta)))`. The OPS common-fixed-`epsilon` target, native `rho>=N-o(N)`, and P-vs-NP remain open.

### Primary source for the promise parameters

- Oliveira, Pich, Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).
