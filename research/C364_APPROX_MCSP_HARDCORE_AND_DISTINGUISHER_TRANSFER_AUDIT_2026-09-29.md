# C-364 - Approximate-MCSP hardness is nearby, but does not transfer to q

Date: 29 September 2026  
Route: test whether recent sparse-distinguisher magnification for approximate MCSP yields a direct lower bound for the full OPS Gap-MCSP native readout.  
Classification: **EXACT PROMISE EMBEDDING + LITERATURE/PARAMETER AUDIT; NO q IMPROVEMENT.**

## 1. A precise distance implication, with the quantifiers exposed

Write the table length as `N=2^n`, and let

```text
s1 = N^beta/(c n),   s2 = N^beta
```

for fixed `0<beta<1` and fixed `c>0`. If a table `z` differs from a table `w` computed by a size-`s1` circuit in `t` positions, then `z` can be computed by first computing `w` and patching those `t` addresses. A fan-in-two De Morgan circuit for the patch is an OR of `t` address minterms, costing `O(t n+n)` gates; XORing the patch into `w` changes only the constant factor. Thus

```text
CC(z) <= s1 + O(t n+n).
```

Consequently, if `CC(z)>s2`, then for every `w in SIZE(s1)`

```text
d_H(z,w) = Omega((s2-s1)/n) = Omega(N^beta/n).
```

Choose a fixed `eta` with `0<eta<beta`, and set `theta=1-beta+eta`. For large N,

```text
N^(1-theta) = N^(beta-eta) <= Omega(N^beta/n).
```

So every NO table of the OPS promise is also a NO table of the approximate promise that rejects tables at distance at least `N^(1-theta)` from `SIZE(s1)`. In set notation,

```text
NO_Gap subseteq NO_Approx.
```

This is the **wrong direction** for automatically transferring a lower bound on approximate MCSP to Gap-MCSP. The approximate promise may require rejection of additional tables, potentially of medium circuit complexity; a Gap-MCSP separator may accept them. Thus the approximate problem is at least as restrictive, and a lower bound for it does not automatically lower-bound the Gap-MCSP separator. A useful transfer would need the reverse containment (or equality), or a complexity-preserving reduction from approximate MCSP into the OPS promise; none is supplied by the patch-distance calculation.

## 2. Test against Atserias-Muller distinguishers

Atserias and Muller prove a strong probabilistic-formula lower bound for approximate MCSP when the circuit threshold `sigma(n)` is at least polynomial in the address length and at most `2^{o(n)}`; their Theorem 32 gives a lower bound of the form `N^(2 theta-delta)` for fixed approximation exponent `theta` and slack `delta`. Their uniform magnification theorem instead assumes a P-uniform circuit lower bound and yields `P != NP^{oplus P}`. [Atserias and Muller, *Simple general magnification of circuit lower bounds*](https://arxiv.org/html/2503.24061), Theorems 27 and 32.

Even if the promise direction were repaired, there are two further mismatches with this project:

1. At fixed OPS `beta>0`, `sigma(n)=N^beta/(c n)=2^(beta n)/(c n)` is **not** `2^{o(n)}`: `log_2 sigma(n)/n -> beta`. Thus Theorem 32 does not apply to the fixed-beta promise, even though the distance implication in Section 1 gives a fixed `theta<1`.
2. Letting `beta` tend to zero with `n` would repair the sparsity condition, but it leaves the theorem's fixed-parameter regime and does not provide a native-state bound. The cited lower bound is for probabilistic formulas; C-319 is a cyclic shared-state least-fixed-point system. Formula expansion can duplicate a shared state many times, and no size-preserving conversion is known. The uniform theorem has a separate uniformity premise and conclusion; the project q-cover is nonuniform, and its generic circuit unrolling also loses polynomial factors.

Therefore this is not yet a lower-bound bridge to Gap-MCSP. The patch argument proves only that Gap-NO instances lie inside the approximate-NO set. The substantive missing item would be a reduction in the other direction that turns every approximate-NO instance into a table of complexity above `s2`, while preserving low YES instances and controlling native readout cost. Without it, the cited formula lower bound gives no `q=omega(N)` result, no `q>N^(1+epsilon)` result, and no P-vs-NP proof. The core alternatives remain a direct lower bound for the coupled C-319 readout or a full-promise near-linear cover.

## 3. Learning and next test

The distance calculation is worth retaining as a relation between NO sets, but not as a lower-bound transfer: `NO_Gap subseteq NO_Approx` makes Approx the stronger promise. The current Atserias-Muller theorem also has a threshold mismatch: its strongest formula result assumes a subexponential-in-`n` circuit threshold, while fixed-beta OPS has threshold `2^{Theta(n)}`. Even closing that parameter gap would leave both the promise-direction problem and the transfer from formulas to cyclic LFP readouts.

I also tested the simplest proposed reverse reduction, repetition encoding. Let `g(x,i)=f(x)` for a copy index `i`. It multiplies Hamming distances by the number of copies, but a circuit for `g` restricts at any fixed `i` to a circuit for `f` with only O(log k) index-hardwiring overhead; conversely, `f` computes `g` with O(log k) extra gates. Thus repetition amplifies distance while preserving circuit size up to small overhead, and cannot turn a table of medium circuit complexity into a table above `s2`. A usable reverse reduction would need a genuine circuit-hardness amplifier: low `f` must still yield low `g`, but every sufficiently small circuit for `g` must decode to a circuit approximating `f` with a quantitatively smaller size than the encoding cost. No such asymmetric compiler is known here.

**Checkpoint:** the actual native bound remains `rho_GapMCSP >= N-o(N)`. No new native lower bound, full-promise cover, positive CohEnc transfer, or P-vs-NP proof was obtained. Keep the goal active; do not report this promise embedding as a breakthrough.
