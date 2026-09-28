# C-314 - Prefix-block safe envelope isolates the selector bottleneck

Date: 28 September 2026  
Classification: **STRUCTURAL LEMMA / COVER CANDIDATE, NOT A COVER CONSTRUCTION.**  
Route: native full-promise cover / O-168.

## 1. A safe superset of the low class

Write `N=2^n`, `s1=N^beta/(c0 log2 N)`, and `s2=N^beta`. Choose `k=Theta(log N)` prefix blocks, with the constant small enough that `k*s1<=s2/2`. Partition truth-table inputs by their first `r=ceil(log2 k)` bits into `k'=2^r` equal blocks, adjusting k by a factor at most two.

Define

```text
A_k(s1) = { w : every prefix restriction w_a on the remaining n-r bits
                has Boolean circuit size at most s1 }.
```

Every `w in SIZE(s1)` belongs to `A_k(s1)`: fix the prefix inputs in a circuit for w, which cannot increase its gate count. Conversely, for any `w in A_k(s1)`, synthesize each block restriction separately and select it with its prefix equality indicator. This costs

```text
CC(w) <= k' * s1 + O(k' * r) <= s2
```

for all sufficiently large N, since `k'=O(log N)` and `k'r=O(log N loglog N)=o(N^beta)` for every fixed beta>0. Thus

```text
SIZE(s1) subseteq A_k(s1) subseteq SIZE(s2).
```

This replaces the exact low class by a larger, explicitly compositional **safe envelope**. For every high table `z` with `CC(z)>s2`, at least one prefix restriction `z_a` must have `CC(z_a)>s1`; otherwise the block synthesis above would put z in `SIZE(s2)`.

## 2. Why this is not yet a q-cover

The statement "some block is hard" is not itself a legal closure witness. The native recurrence branches through signed truth-table literals and previously generated compatible supports; it does not receive the predicate `CC(z_a)>s1` as a free oracle. To use this envelope, one must either:

1. build a native rule system that routes to a locally hard block without storing `(gate,address)` and without accepting medium/low hybrids; or
2. prove that any such routing needs superlinear q because the state must synchronize block identity with circuit-gate evaluation.

The direct evaluator that stores both a block/gate identity and a within-block address still pays `Theta(N*s1)` (C-305). The envelope therefore identifies the semantic selector needed by O-168, but supplies neither an `N^(1+o(1))` cover nor a lower bound. It must pass the C-257 parity, C-258 equality, and C-281 owner-mask splice checks.

## 3. Checkpoint

This is a sound structural enlargement of the promise's low side, not a q improvement. The actual bound remains `rho_GapMCSP=N-o(N)`. The unresolved question is whether prefix-block identity can live in native proof supports without becoming an address register or allowing incompatible block hybrids.
