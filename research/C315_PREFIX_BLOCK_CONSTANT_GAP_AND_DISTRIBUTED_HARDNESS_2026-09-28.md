# C-315 - Prefix blocks expose a local constant-gap bottleneck

Date: 28 September 2026  
Route: C-314 safe envelope / O-168 full-promise cover.  
Classification: **PARAMETER REDUCTION + COUNTING CALIBRATION; NO q BOUND.**

## 1. Claim

Fix any constant `0 < beta < 1`, write `n=log2 N`, `s2=N^beta`, and `s1=N^beta/(c0*n)`. Partition the truth-table addresses into `k=Theta(n)` equal prefix blocks, with the constant chosen so that

```text
k*s1 + O(k log k) <= s2/2.
```

There are constants `B>1` and `A>B`, such that, for all sufficiently large N, some table `z` satisfies

```text
CC(z) > s2,
B*s1 < CC(z restricted to block a) <= A*s1   for every block a,
```

Thus globally high tables exist for which every block is moderately hard, but no block is known to be harder than a fixed constant multiple of `s1`. This tests the block scale quantitatively; it does not make a high table's support an accepting proof.

## 2. Counting construction of a globally high table with only moderately hard blocks

Let each block have `m=N/k` addresses and `n_b=log2(m)=n-log2(k)` input bits. For an integer `u<n_b`, consider the family `F_u` of block functions that are zero outside one fixed `u`-dimensional address subcube and are arbitrary on that subcube. It has exactly `2^(2^u)` members. Lupanov synthesis gives circuits of size

```text
O(n_b + 2^u/u).
```

Choose `t=A*s1` and choose `u` so `2^u=Theta(t log t)` with a sufficiently small constant. Since `t=N^beta/polylog(N)`, we have `u=(beta+o(1))n<n_b`, and every member of `F_u` has circuit size at most `t` for large N. Also,

```text
log2 |F_u| = 2^u >= c1*t*log2(t)
```

for a constant `c1>0`.

There are at most `2^(C*B*s1*log(B*s1+n_b))` block functions of complexity at most `B*s1`. Choose `A/B` large enough that this is less than half of `|F_u|`; after discarding those functions, a family `F'_u` remains with

```text
B*s1 < CC(f) <= A*s1   for every f in F'_u,
log2|F'_u| >= c2*A*s1*log2(s1)
```

for a constant `c2>0` (with constants chosen in order). Choose an independent member of `F'_u` on each of the `k` address blocks. Distinct tuples give distinct N-bit tables, so the product family has size at least

```text
2^(c2*k*A*s1*log2(s1))
  = 2^(c2*A*(k/(c0*n))*s2*log2(s1)).
```

The number of N-bit tables with Boolean circuit size at most `s2` is at most `2^(C*s2*log2(s2+n))` for a basis-dependent constant `C`. Since `log s1/log(s2+n) -> 1`, choose the fixed constant `A` large enough that the product family is larger than `SIZE(s2)`. Some assembled table `z` is therefore outside `SIZE(s2)`, while every block restriction has complexity in `(B*s1,A*s1]`.

Here `A*s1/s2=A/(c0*n)=o(1)`. The constants can be selected so `B` exceeds the C-314 local threshold ratio `s2/(k*s1)=c0*n/k`, while `A` is larger still. This gives a high table with every block beyond that local threshold and with all block complexities bounded by a constant multiple of `s1`.

## 3. Exact reduction to a family of local constant-gap separators

Let `t0=floor((s2-O(k log k))/k)`. If every block restriction has circuit size at most `t0`, separate block circuits plus the prefix selector synthesize the whole table in size at most `s2`. Every global low table restricts to `SIZE(s1)`. Therefore a local **monotone separator over signed block literals** `g` satisfying

```text
g=1 on SIZE(s1) over m=N/k table inputs,
g=0 on every block function of circuit size >t0
```

can be copied to each block and combined by AND. This gives a separator for the global low/high promise: low tables make every copy accept, and a high table has at least one block on which its copy rejects. If `g` has `a` AND gates, the combined acyclic monotone circuit has at most `k*a+(k-1)` AND gates; C-307's compiler converts it to a native cover with at most that many pairs.

For `k=Theta(n)`, the local threshold ratio is only

```text
t0/s1 = (s2/(k*s1)) + o(1) = c0*n/k + o(1) = Theta(1).
```

Thus the prefix envelope trades the original logarithmic global gap for a constant-factor local gap, replicated across `Theta(log N)` blocks. Choosing `k=o(n)` increases the local gap but shrinks the number of blocks and changes their input length; it does not itself give a cheaper native selector. No direct-sum lower bound for this composition follows from the construction.

## 4. What this rules out and what it leaves open

The counting construction falsifies any use of C-314 that assumes globally high tables must contain a block whose circuit complexity is superconstant-factor larger than `s1`: every block can lie in `(B*s1,A*s1]` for fixed constants. The safe-envelope implication itself remains correct. A local separator at the exact threshold `s1` is still a possible mechanism, but the global selector must combine local decisions without losing consistency or paying for a full address/gate product.

This moves O-168's target to one of two concrete outcomes: prove a q-sensitive direct-sum/coherence theorem for the blockwise local gap, or construct a shared native selector that beats the `k`-copy implementation. Any lower bound must pass C-257 parity, C-258 equality, and C-281 compatible-splice checks. The construction does not turn block count or anchor count into a q charge.

**Literature boundary.** Wolfgang J. Paul's disjoint-variable circuit results show that additivity under disjoint composition cannot be assumed for general circuit tasks: some arbitrarily complex multi-output functions have `C(f x f) <= (1+epsilon)C(f)`. This is not a theorem for our monotone `AND` composition or the fusion grammar, but it reinforces why Q177 needs a model-specific proof. [Paul, *Realizing Boolean Functions on Disjoint Sets of Variables* (1976)](https://doi.org/10.1016/0304-3975(76)90089-X).

No near-linear full-promise cover, superlinear `q`, CohEnc/decision gap, or P-vs-NP proof follows. The actual result remains `rho_GapMCSP=N-o(N)`.
