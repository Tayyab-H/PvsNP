# C-396 - Growing-depth local restrictions force many escape sources

Date: 29 September 2026  
Route: strengthen C-395 by applying the all-depth pseudorandom restriction lemma directly, with explicit parameters.  
Classification: **PROMISE-SPECIFIC GROWING-DEPTH AC0 LOWER BOUND AND QUANTITATIVE C-319 PARAMETER BOUND; NO q IMPROVEMENT.**

## 1. Promise and theorem

Let `N=2^n` be the truth-table length. Fix `0<beta<1` and a constant `c_gap>0`, with promise thresholds

```text
s1 = N^beta / (c_gap log N),
s2 = N^beta.
```

A separator must accept every table of circuit complexity at most `s1` and reject every table of complexity greater than `s2`; it may behave arbitrarily in the middle interval.

**Theorem 1 (growing-depth AC0 restriction bound).** Fix `beta` and a polynomial-size exponent `B>0`. There is a constant `delta>0` such that, for all sufficiently large `N`, no AC0 circuit of size at most `N^B` and depth at most

```text
delta * log N / log log N
```

separates this promise. One may take any fixed `delta < (1-beta)/2`; the proof below uses `delta=(1-beta)/4` with slack for floors and constants.

**Corollary (escape-source lower bound inside C-319).** Fix `A>0`. There is a constant `c_A>0` such that, for all sufficiently large `N`, every valid full-promise C-319 cover with `q<=N^A` rules has

```text
k >= c_A * log N / log log N,
```

where `k` is the number of distinct one-sided escape-source carriers in the C-393 normal form (C-393 denotes this parameter by `s`). This is a structural restriction on polynomial-size covers. It does not imply `q>N^(1+epsilon)`, nor a lower bound on C-393's paid-AND measure.

## 2. Proof of Theorem 1

We use CKLM's pseudorandom restriction lemma in its all-depth form (Lemma 31) and the local-computability argument in the proof of their Lemma 29. The source states the restriction guarantee for arbitrary integers `d,t`; we use that statement directly rather than extrapolating the fixed-depth asymptotic notation in Lemma 29. See [Cheraghchi, Kabanets, Lu, and Myrisiotis, *Circuit Lower Bounds for MCSP from Local Pseudorandom Generators*](https://www2.cs.sfu.ca/~kabanets/papers/MCSP_lower_bounds.pdf), Lemmas 29 and 31.

Let `C` have size `S<=N^B` and depth `d<=delta log N/log log N`. Pad by unused gates if necessary so `S>=N`; this preserves the function and depth. Put `L=ceil(log_2 S)`, choose `t=L`, `p=1/(C0 L)` for a sufficiently large absolute constant `C0` (for example, `C0=1024` after absorbing the paper's log-base convention), and set `epsilon0=2^(-10 L^2)`.

CKLM Lemma 31 gives a restriction `rho0` for which, with probability at least `2/3`, the number of stars is at least

```text
N * p^(d-2) / 80.
```

Its failure bound for not reducing to a width-`t` DNF or CNF is

```text
S * (2^(2t+1) * (10 p log S)^t
     + epsilon0 * 2^((t+1)(2t+log S))).
```

With the chosen parameters the first term is `2^(-Omega(L))` and the second is `2^(-Omega(L^2))`; for all sufficiently large `N` this failure probability is below `1/3`. Hence there exists a restriction meeting both properties. A width-`t` CNF or DNF can be made constant by fixing at most `t` of its remaining variables: falsify one clause for a CNF, or satisfy one term for a DNF. Compose these fixes with `rho0` to obtain `rho` such that `C_rho` is constant, leaving

```text
m >= N * p^(d-2) / 80 - t
```

stars.

The restriction is locally computable. Lemma 31 gives a circuit that, from a coordinate index and a fixed seed, outputs the corresponding coordinate of `rho0`; the seed can be hardwired. Its size is `d * r * O_tilde(log N)`, where

```text
r = O((log S + t log(1/p))^2
       + (log S + t log(1/p)) * log(1/epsilon0)).
```

For `S<=N^B`, we have `L=O(log N)`, `t=Theta(log N)`, `log(1/p)=O(log log N)`, and `log(1/epsilon0)=O((log N)^2)`. Thus `r=polylog(N)`. Since `d=O(log N/log log N)`, the local restriction circuit has polylogarithmic size. The at-most-`t` extra fixed coordinates are hardwired using another `O(t log N)` gates. Therefore the completion `f0` which agrees with all fixed coordinates of `rho` and sets every star to zero has circuit complexity `polylog(N)`, and in particular is below `s1` for large `N`.

Because `C_rho` is constant and `f0` is a YES table, this constant is 1. We now show that the same subcube contains a NO table. Since `S<=N^B`, there is a constant `B'>0` with `L<=B' log_2 N`. For `d<=delta log_2 N/log_2 log_2 N`,

```text
N * p^(d-2)
  = N / (C0 L)^(d-2)
  >= N^(1-2 delta)
```

for all sufficiently large `N`; this uses `log_2(C0 B' log_2 N)/log_2 log_2 N -> 1`. Taking `delta=(1-beta)/4` gives `1-2delta=(1+beta)/2>beta`. Hence

```text
m >= N^((1+beta)/2) / 80 - O(log N)
  >> N^beta log N.
```

There are `2^m` completions of the restriction. On the other hand, the number of Boolean functions on `n=log_2 N` inputs with circuit complexity at most `s2` is at most the number of bounded-fan-in circuit descriptions,

```text
|SIZE(s2)| <= 2^(O(s2 log(s2+n))) = 2^(N^(beta+o(1))).
```

Since `m` exceeds this exponent, one completion has circuit complexity greater than `s2`. It is a NO table, but `C` accepts every completion because `C_rho` is constantly 1. Contradiction. The argument explicitly handles the promise's unrestricted middle interval: the zero-star completion lies below `s1`, while counting guarantees a completion above `s2`.

## 3. C-319 consequence

In the C-393 normal form, each macro-round computes candidate seed/support ORs, one AND per candidate, and an upward-closure OR. The terminal root tests add constant depth. Thus a cover with `k` distinct escape sources has an AC0 implementation of depth at most `a0(k+1)` and size polynomial in `q,k,N`, for an absolute constant `a0`. More concretely, with unbounded-fan-in OR gates, the gate count is `O(q(k+1))`; the wire count is polynomial whenever `q,k` are polynomial.

Suppose, toward contradiction, that a valid cover has `q<=N^A` and `k<c_A log N/log log N`, where `c_A` is chosen small enough that `a0(k+1)<=delta log N/log log N` for the `delta` in Theorem 1. The compiler then gives a polynomial-size, depth-at-most-`delta log N/log log N` AC0 separator. Padding its gate count to at least `N` if needed, Theorem 1 rules it out. Therefore `k=Omega_A(log N/log log N)` for every polynomial-size full-promise cover family.

## 4. What this does and does not buy

- C-395's bounded-`k` contradiction is quantitatively strengthened to a growing-depth regime.
- A hypothetical near-linear native cover cannot route its full-promise computation through only a bounded or sub-`log N/log log N` set of escape-source carriers.
- The result does not increase the known native bound `q>=N-o(N)`. The lower bound on `k` is still much smaller than `q` and is compatible with `q=Theta(N)`.
- C-393 is an upper compiler: `A_cap<=m+(k+1)(q-m)`. A lower bound on `k` does not lower-bound `A_cap`, because the compiler inequality points in the opposite direction.
- No selector/native bridge or P-vs-NP proof follows. The live next question is whether the forced escape-source diversity can be charged to a representation-independent state/readout cost while preserving the C-258 equality calibration, or whether a near-linear full-promise cover can realize it cheaply.

**Literature scope.** The restriction mechanism is from CKLM; their paper proves lower bounds for exact MCSP in restricted models and mentions gap-MCSP as a hardness-magnification motivation. The thresholds here are the OPS gap regime. This note supplies an explicit restriction-and-counting derivation for this promise and its C-319 consequence; it makes no historical-priority claim. The OPS magnification theorem targets unrestricted polynomial-size circuits at a superlinear threshold, while the present result is only for AC0 and cannot be transferred to general circuits. See [CKLM](https://www2.cs.sfu.ca/~kabanets/papers/MCSP_lower_bounds.pdf) and [OPS, *Hardness Magnification Near State-of-the-Art Lower Bounds*](https://www.theoryofcomputing.org/articles/v017a011/).

**Status:** proof-level progress on the structure of polynomial-size C-319 covers and a promise-specific AC0 lower bound. The exact unrestricted Gap-MCSP state-count problem remains open.
