# C-453 - direct-product repetition does not amplify the simple-extension gap

**Date:** 1 October 2026  
**Question:** Can independent block repetition turn exact `f`-Simple-Extension NO instances into OPS-High truth tables?  
**Result:** No for the natural AND-product of the C-452 OR examples. For every repetition count, the product has a valid key, is a genuine NO, and has only linear-in-arity circuit size. Since OPS-High is exponential in the truth-table arity, both YES and NO products remain Low. This retires this direct-product amplifier, not arbitrary encodings.

## 1. The attempted amplifier

For `n>=3`, take `f_0(x)=OR_n(x)`. From C-452 define the simple extension

```text
u(x,y) = OR_n(x) OR y
```

with `CC(u)=n`, and the non-simple, nondegenerate extension

```text
v(x,y) = OR_n(x) XOR (x_1 AND y)
```

with `n+1 <= CC(v) <= n+5` and valid key `y=0`.

Repeat `r>=1` independent blocks and AND their outputs. The proposed base and two product tables are

```text
f_r(x^1,...,x^r) = AND_{j=1}^r OR_n(x^j),
U_r(x^1,y_1,...,x^r,y_r) = AND_{j=1}^r u(x^j,y_j),
V_r(x^1,y_1,...,x^r,y_r) = AND_{j=1}^r v(x^j,y_j).
```

The base has `rn` essential inputs and a read-once AND/OR formula with `rn-1` gates, so `CC(f_r)=rn-1`. `U_r` has `q=r(n+1)=rn+r` essential inputs, a key `y=0^r`, and an AND/OR formula with `rn+r-1=q-1` gates. Hence `U_r` is a YES simple extension of `f_r` by `r` variables.

## 2. The repeated NO remains near-minimal and OPS-Low

`V_r` has the same key: setting all `y_j=0` gives `f_r`. It depends on every input: for each block, set all other block outputs to 1 and use the corresponding essential input of `v`. It is nonmonotone in every `y_j`: set all other block outputs to 1 and set `x^j_1=1`; changing `y_j` from 0 to 1 changes that block's output from 1 to 0.

Because `V_r` is nonmonotone and depends on all `q` inputs, it cannot have the minimum `q-1` gates. As in C-452, a circuit on `q` essential inputs requires at least `q-1` binary gates; equality forces a read-once monotone AND/OR formula. Thus

```text
CC(V_r) >= q.
```

For an upper bound, use one `n+5`-gate circuit for each copy of `v` and combine the `r` outputs with `r-1` AND gates:

```text
CC(V_r) <= r(n+5)+(r-1) = rn+6r-1 = q+5r-1 <= 3q.
```

The OPS truth-table length is `N=2^q`. For each fixed `beta>0` and constant `c`,

```text
s1 = 2^(beta q)/(c q),       s2 = 2^(beta q).
```

For all sufficiently large `q`, both `CC(U_r)=q-1` and `CC(V_r)<=3q` are below `s1`. Therefore this direct-product transform sends a valid simple-extension YES and a valid simple-extension NO to OPS-Low. No lower bound on `CC(V_r)` beyond `q` is needed to establish failure.

## 3. What the test does and does not show

It shows that ANDing independent copies, adding independent extension variables, and relying on a putative additive cost do not bridge the scale mismatch: the product circuit grows only linearly in its new input count, while `s2` grows exponentially in that count. The construction uses ordinary shared circuits throughout and does not assume a direct-sum lower bound; its explicit upper bound is enough to defeat the proposed amplifier.

It does not refute tensoring for a base family whose NO products are already exponentially hard, nor a nonlinear encoding whose generator cost is fully charged. Such a construction must prove that every NO input is sent above `s2`, including near-optimal perturbations, and that every YES is below `s1`.

## 4. Paired full-promise construction and current literature

The unconditional full-promise separator remains `F_enum(T)=1` iff some circuit of size at most `s1` computes `T`. It accepts every YES and rejects every NO, at cost `O(N 2^(O(N^beta)))` gates. No near-linear full-promise separator was found by the product attempt.

The C-452 literature lead on total `f`-Simple Extension remains useful for candidate selection: characterized OR and XOR bases have polynomial-time extension decision, while the cited work suggests multiplexer/high-fan-out functions as open structural cases. The product audit shows that exact-extension complexity—even when the base is amplified by independent blocks—does not supply an OPS High endpoint unless an additional theorem proves exponential circuit complexity of the NO image. [Carmosino, Dang, and Jackman](https://arxiv.org/abs/2511.16903). The OPS theorem still requires one common fixed `epsilon>0` for all sufficiently small fixed `beta`; no part of this test meets that quantifier. [OPS, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf).

## 5. Strongest statement and next research action

**Project-proved:** for every `r>=1` and `n>=3`, `U_r` is a YES simple extension of `f_r`, while `V_r` is a nondegenerate valid-key NO with `q <= CC(V_r) <= 3q`, where `q=r(n+1)`. Thus direct AND-product repetition fails the OPS High endpoint for every fixed beta eventually.

**Frontier:** unchanged. Ordinary `N-O(N^beta log N)-1` plus C-406's logarithmic reconvergence refinement; common-fixed-epsilon OPS target open; exact full-promise upper `O(N 2^(O(N^beta)))`; native `rho>=N-o(N)` separate. No P-vs-NP result.

Retire independent AND-repetition as a gap amplifier. The next source route must hide the source label rather than merely combine near-optimal extensions, and its image hardness must be proved against unrestricted circuits. If no image map survives endpoint and cost audits, return to a direct ordinary-DAG lower-bound mechanism rather than increasing the repetition parameter.
