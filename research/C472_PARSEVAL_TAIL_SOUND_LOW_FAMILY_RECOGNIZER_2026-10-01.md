# C-472 — Parseval tail yields a sound robust recognizer for linear-junta tables

**Status:** proved near-linear sound recognizer for a structured, exponentially large family of Low tables and its forced Hamming neighborhood. This repairs C-471's false positives from small Fourier coefficients, but the recognizer still omits small circuits with full-dimensional Fourier support. It is not an OPS separator and does not change the frontier.

## 1. Definition and parameters

Set `N=2^n`, fix `0<beta<1/2`, and use `s1=floor(N^beta/(10n))`, `s2=N^beta`. Choose even `m` so `2^m` is a sufficiently small constant fraction of `s1`. Let

```text
J_m = { f(x)=g(Ax) : A:F_2^n -> F_2^m linear, g:{0,1}^m -> {0,1} }.
```

Every `f in J_m` has circuit size at most `s1/4`: compute the m parity forms in `O(mn)` gates and use a mux tree of `O(2^m)` gates for g. Put `r=floor(a*s1/n)` for a sufficiently small constant a, so patching at most `4r` truth-table positions onto any member of `J_m` still costs less than `s1` gates. Thus the whole radius-r neighborhood of `J_m` is forced Low.

For a truth table T, compute its sign Walsh coefficients `W_T(u)` as in C-471. Set `tau=3r`, and define

```text
S_tau(T) = {u : |W_T(u)| > tau},
B_tau(T) = span(S_tau(T)),
Tail_tau(T) = sum_{u notin B_tau(T)} W_T(u)^2.
```

The recognizer Q(T) outputs 1 exactly when `dim(B_tau(T))<=m` and `Tail_tau(T)<=4*N*r`.

## 2. Robust completeness on J_m

Let `T0(x)=g(Ax)` have effective rank `d<=m` and Fourier-support span `W0`. Each nonzero unnormalized Walsh coefficient of T0 has magnitude at least `2^(n-d)>=2^(n-m)`: it is `2^(n-d)` times a nonzero integer Walsh coefficient of g.

For fixed beta `<1/2`,

```text
2^(n-m) = Theta(N/s1) = Theta(n*N^(1-beta)) >> r = Theta(N^beta/n^2).
```

If T differs from T0 in at most r table positions, each Walsh coefficient changes by at most `2r`. Hence, for sufficiently large N, the threshold `tau=3r` keeps every originally nonzero coefficient above threshold and every originally zero coefficient below it. Therefore `B_tau(T)=W0`. Parseval gives

```text
sum_u (W_T(u)-W_T0(u))^2 = 4*N*dist_H(T,T0) <= 4*N*r.
```

All coefficients outside W0 of T0 are zero, so `Tail_tau(T)<=4Nr`. Thus Q accepts every radius-r perturbation of every member of J_m. These are genuine OPS-YES tables by the choice of r.

## 3. Soundness against every High table

Suppose Q(T)=1 and write B=`B_tau(T)`. Project the sign function `chi_T` orthogonally onto the Walsh characters in B, obtaining a real-valued function p whose Fourier support lies in B. Choose the Boolean sign function `h=sign(p)` on each coset of `B^perp` (choose either sign on ties). Then h depends on at most m linear forms.

At every address where `chi_T` and h disagree, `|chi_T-p|>=1`. Orthogonality and the unnormalized transform convention give

```text
dist_H(T,h) <= sum_x (chi_T(x)-p(x))^2
             = Tail_tau(T)/N
             <= 4r.
```

The function h has circuit size at most `s1/4`; patching at most `4r` positions costs at most `s1/2` after choosing a small enough a. Hence `CC_n(T)<s1`. In particular, Q rejects every table with `CC_n(T)>s2`. This is a proof of soundness; Q does not output h or reconstruct a circuit description.

## 4. Ordinary gate count

The Walsh transform uses `O(Nn^2)` Boolean gates: n butterfly stages, `O(Nn)` signed additions/subtractions, and O(n)-bit arithmetic. Thresholding coefficients is `O(Nn)`. A fan-in-two Gaussian-elimination circuit forms a basis for `B_tau(T)` in `O(Nn^3)` gates. For each of N frequency indices, basis membership takes `O(n^2)` gates. Squaring the N `O(n)`-bit Walsh coefficients, summing those outside B, and comparing to `4Nr` costs `O(Nn^2)` gates. Therefore Q is an ordinary AND/OR/NOT circuit of total size `O(Nn^3)=O(N log^3 N)`, below `N^(1+epsilon)` for every fixed epsilon>0 and large enough N. The count includes all transform, rank, membership, multiplication, summation, and comparison gates; there is no free subspace search or ROM.

## 5. Completeness failure and exact limitation

Let `L_1,...,L_{m+1}` be independent linear forms and set

```text
f(x) = AND_{j=1}^{m+1} L_j(x).
```

This is a Low table: its circuit costs `O((m+1)n)=O(n^2)<<s1`. The sign Fourier support of AND on `m+1` bits contains every frequency of their `(m+1)`-dimensional span, with nonzero coefficients; after lifting to n variables these coefficients have magnitude at least `2^(n-m) >> tau`. Thus `dim(B_tau(f))=m+1` and Q rejects f. The predicate is not complete for the full Low set.

C-471's high perturbations with small maximum Fourier coefficient are rejected by Q because their total Fourier-tail energy is proportional to their Hamming error count, which is much larger than r. The key distinction is that Parseval controls the *sum of squared tails*, while a coefficientwise cutoff alone did not.

## 6. Barrier and originality audit

The transform, Parseval identity, and address-patching estimate are standard. C-472's project-level refinement is the combined two-sided statement: a data-dependent Fourier subspace is recovered at a threshold with a gap, and a Parseval tail certificate proves every accepted table is within `4r` edits of a Low junta. The method gives a real `N polylog N` sound recognizer, but no claim of a full MCSP lower bound or a new coding/Fourier theorem is made.

This is not the hardness-magnification locality barrier: it is an explicit one-sided recognizer and an exact Low-completeness counterexample. The established barrier concerns adapting known weak-model lower-bound techniques to magnification targets with small-fan-in oracle circuits; see [Oliveira et al., ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/).

**Next algebraic model to test.** For sign functions, Boolean gates have exact Fourier-coordinate identities:

```text
W_{f AND g}(u) = 1/2 * (N*[u=0] + W_f(u) + W_g(u)
                         - (1/N)*sum_v W_f(v)W_g(u+v)),
W_{f OR g}(u)  = 1/2 * (-N*[u=0] + W_f(u) + W_g(u)
                         + (1/N)*sum_v W_f(v)W_g(u+v)),
W_{NOT f}(u)   = -W_f(u).
```

This gives a Fourier-DAG language that preserves the source circuit's shared gate graph at the symbolic level. It is only a change of representation: it does not make the convolutions free, and no useful arbitrary-sharing potential or cost-preserving Boolean compiler has been proved. A viable successor must bound the actual total gates needed to recognize the closure of these operations, without assuming the separator reconstructs a source circuit.

## 7. Paired full-promise attempt and frontier

Adding the missing Low functions by enumerating all size-s1 circuit tables restores completeness at the existing `O(N*2^(O(N^beta)))` gate scale. No near-linear full-promise separator is known. The ordinary lower bound remains `N-O(N^beta log N)` plus C-406's additive logarithmic reconvergence refinement; the common-fixed-epsilon OPS target, native rho target, and P-vs-NP remain open.
