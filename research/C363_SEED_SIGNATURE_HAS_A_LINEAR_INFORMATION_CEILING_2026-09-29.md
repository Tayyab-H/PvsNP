# C-363 - Seed signatures have a linear information ceiling

Date: 29 September 2026  
Route: isolate how much of the C-319 input can be recovered from seed predicates before charging the least-fixed-point readout.  
Classification: **EXACT REPRESENTATION LEMMA / ROUTE CAP; NO q IMPROVEMENT.**

## 1. The literal feature bank

For each table coordinate `a in [N]` and bit `b in {0,1}`, define the signed-literal feature

```text
lambda_(a,b)(w) = 1 iff w_a=b.
```

Each C-319 seed predicate is an OR of a fixed set of these features. A singleton endpoint therefore exposes one feature exactly. Conversely, the N positive features `lambda_(a,1)` recover the entire input table:

```text
w = (lambda_(1,1)(w), ..., lambda_(N,1)(w)).
```

This can be realized at the seed-signature level by N states, one with endpoint `{(a,1)}` and its other endpoint the all-universe set for each coordinate `a`; the first seed slot is `w_a`, and the all-universe side contributes a constant-true seed. The transition graph may couple the resulting activation bits, so this is not a claim that the states independently output the table bits. It demonstrates only the point needed here: an O(N)-state signature can already be injective on all 2^N tables.

If one wants a feature that separates every **ordered** pair directly, rather than an injective signature, the full `2N` signed singleton features suffice: for `w != z`, choose a differing coordinate `a` and the sign `b=w_a`, giving `lambda_(a,b)(w)=1` and `lambda_(a,b)(z)=0`.

## 2. Consequence for signature-only lower bounds

Let

```text
sigma_Q(w) = (A_1(w), B_1(w), ..., A_q(w), B_q(w)).
```

The C-319 induction gives a fixed readout `G_Q` with `Accept_Q(w)=G_Q(sigma_Q(w))`. Once `q` is O(N), the available seed channel can distinguish every table; at `q=N`, a valid singleton/all-universe realization can make it injective. Therefore no argument that charges only the number of distinguishable tables, the number of signature fibers, or pairwise low/high signature collisions can force `q=omega(N)`. Such an argument saturates when the input itself is visible.

This does **not** say the readout is cheap or that the signature bits are free wires. `A_i` and `B_i` occur only in their own paired transition equation; an injective conceptual signature need not produce an injective activation vector or make its coordinates separately readable downstream. The fixed map `G_Q` is the least fixed point of that coupled C-319 system, and the same q states must expose and combine the features into the right low/high separator. In particular, injectivity of `sigma_Q` does not give a small separator readout, and the singleton-state example above does not accept exactly `SIZE(s1)` while rejecting tables above `s2`.

## 3. The sharpened mathematical target

Separate two resources that were previously conflated:

1. **Seed-slot information:** the vector `sigma_Q` can encode the full N-bit table with O(N) states.
2. **Coupled readout:** those seed values are wired into the same q paired recurrences; the least fixed point must still output 1 on every `SIZE(s1)` table and 0 outside `SIZE(s2)`.

The first resource has a linear construction at the signature level. Any superlinear theorem must charge the second resource: it must show that the paired fixed-point readout cannot compute the promise separator with q=O(N), despite having enough seed slots to encode the table. This agrees with the two compiler bounds already in the repository: C-319 unrolling gives at most q^2 paid AND gates, while C-109 compiles a fan-in-two De Morgan separator of size S to at most `3S+1` native pairs. Hence a superlinear native lower bound would also be a superlinear circuit lower bound for the same promise; input information by itself cannot be the source of that lower bound.

## 4. Checkpoint and next move

- The proved Gap-MCSP bound remains `rho_GapMCSP >= N-o(N)`.
- No superlinear q theorem, full-promise near-linear cover, positive CohEnc transfer, or P-vs-NP proof is obtained.
- Retire raw seed-signature capacity and fiber-count arguments as primary routes. A live continuation must analyze the cost of the cyclic readout on an injective or near-injective seed encoding, or construct that readout in `N^(1+o(1))` states for the full promise.

This is a model clarification and exact route cap, not a breakthrough.
