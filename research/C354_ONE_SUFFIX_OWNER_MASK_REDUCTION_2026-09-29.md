# C-354 - A one-suffix splice turns ownership into a smaller circuit

Date: 29 September 2026  
Route: sharpen C-353's overlap/ownership analysis by isolating one suffix column.  
Classification: **EXACT LOCAL SPLICE REDUCTION + HIGH-MASK COUNTING; NO q IMPROVEMENT.**

## 1. The one-column family

Keep C-234's split of an address into `(p,u)`, where `u` has k bits and `p` has m=n-k bits. Choose one suffix `u0` and define

```text
w0(p,u) = 0
w1(p,u) = 1 iff u=u0
z_mu(p,u) = 1 iff (u=u0 and mu(p)=1).
```

The first two anchors have O(n)-size circuits, hence are in SIZE(s1) at the fixed OPS parameters for sufficiently large n. For every Boolean function `mu` on m bits,

```text
CC(mu) - O(1) <= CC(z_mu) <= CC(mu) + O(n).
```

The lower inequality follows by restricting z to `u=u0` (and hardwiring those k input bits). For the upper inequality, compute `mu(p)` and gate it with the equality test `u=u0`. Thus the hybrid's complexity is, up to the displayed additive overhead, exactly the complexity of its owner mask.

## 2. Almost every mask makes a high splice

For C-234's maximal k, `2^k=Theta(s2)` and

```text
r = 2^m = 2^(n-k) = Theta(N/s2).
```

Assume a fixed `0<beta<1/2`. A standard circuit-description count gives

```text
|SIZE_m(s2+O(n))| <= 2^(O(s2 log(s2+m))) = 2^(O(s2*n)).
```

Meanwhile the owner-mask space has `2^r` functions, and

```text
r/(s2*n) = Theta(N^(1-2*beta)/n) -> infinity.
```

It follows that all but a `2^{-Omega(r)}` fraction of masks satisfy `CC(mu)>s2+O(n)`. By the restriction inequality, the corresponding `z_mu` have circuit complexity greater than s2. So a random owner pattern on this one repeated suffix already gives a high table; independent variation across many suffixes is unnecessary for this local high-side fact.

## 3. Exact C-281 splice interpretation

Take any state i, a context support K at i matched by w0, and a replacement proof support C at i matched by w1. If `K union C` is consistent, every coordinate outside the suffix column `(p,u0)` carries only 0-signs, since both anchors are zero there. At a coordinate `(p,u0)`, K can carry only 0 and C only 1; consistency forbids both signs from occurring together.

Define the canonical owner mask

```text
mu_(K,C)(p) = 1 iff C mentions the 1-literal at (p,u0),
```

and fill all unmentioned coordinates by 0. The union support is contained in the truth table `z_mu`. C-281 substitution therefore gives an accepting proof for `z_mu`. Soundness forces

```text
CC(mu_(K,C)) <= s2+O(1).
```

Thus, for this anchor pair, every compatible same-state context/proof join must land in the low-circuit owner-mask class. In particular, its set of distinct masks has cardinality at most `2^(O(s2*n))` and VC dimension at most `O(s2*n)`: shattering T prefix positions would generate `2^T` distinct masks, all of which must be in that circuit class.

This is a state-local forbidden-cube condition. It is more concrete than saying that complicated ownership is dangerous: a full Boolean cube of owner choices on more than `O(s2*n)` prefix positions would directly contain a high splice.

## 4. Restricting the game gives a smaller abstract separator

There is a second exact consequence of the one-column embedding. Start with any valid q-state C-319 list for the full N-coordinate promise and restrict its input tables to `z_mu`. Each seed clause is a disjunction of signed table literals. On this slice, every coordinate outside `(p,u0)` is fixed to zero: a fixed-true literal makes the restricted clause the constant true predicate, fixed-false literals disappear, and literals in the column become the corresponding signed literals of mu. The predecessor graph and empty-root set do not change. Induction on the least-fixed-point rounds shows that the restricted acceptance function is computed by the same q-state recurrence with these simplified clauses.

If `CC(mu)<=s1/2`, then `CC(z_mu)<=s1` for sufficiently large n, so the restricted recurrence accepts. If `CC(mu)>s2+O(1)`, then `CC(z_mu)>s2`, so it rejects. Hence every full cover induces, at no increase in q, a separator in the **more permissive abstract least-fixed-point model with signed input clauses** on m input variables. This is a lower-bound transfer only; the simplified recurrence is not claimed to come from endpoint pairs over the reduced high-table universe.

The reduced table length is `r=2^m=Theta(N^(1-beta))`. Put `beta'=beta/(1-beta)`. For `beta<1/2`, `beta'<1`, `s2+O(1)=Theta(r^beta')`, and `s1/2=Theta(r^beta'/log r)` up to changed fixed constants. Thus this is an OPS-shaped self-restriction to a smaller truth-table length and a larger exponent. If one proved `rho_abs(r,beta')>=r^(1+delta)` for this abstract model, then the original cover would obey

```text
q >= N^((1-beta)(1+delta)+o(1)),
```

which is superlinear exactly when `delta>beta/(1-beta)`. No such superlinear bound for the abstract recurrence is currently known, so this parameter transform is not itself a q improvement.

## 5. Why this still does not charge q

The theorem constrains only compatible cross-pairs for the fixed anchors w0,w1. It does not show that a reused state must generate a large cube of masks. A grammar may make the two anchors' supports incompatible, as complete supports do; C-258/C-326 realize this safe behavior for the repeated-block subpromise with O(N) rules. Nor does completeness for the low masks imply that one state sees the corresponding cross-anchor context/proof pairs: the accepting proofs for different `z_mu` may use different states and supports.

There is also a quantitative limit to a per-state mask-count argument. The number of size-s1 masks has logarithm at most `O(s1 log s1)=O(s2)`, whereas the soundness-only bound on possible size-s2 masks has logarithm `O(s2 log s2)=O(s2*n)`. So the local safe mask universe is exponentially larger (in the exponent by a factor of order n) than the low family can be. Counting distinct masks at one state cannot by itself force many states; the needed charge must use how the grammar organizes and reuses the masks.

The missing implication is now sharply localized:

```text
all-low coverage of the one-column family
    -> many cross-compatible owner masks at shared states,
       or a rule cost for keeping the masks pairwise separated.
```

Neither side of this implication is proved. The result does not exceed `q >= N-o(N)`, construct a full-promise near-linear cover, or prove P != NP. It supplies a concrete test for any proposed state-capacity or forced-splice theorem: for each reused state on this pair, its compatible owner-mask relation must avoid every mask outside `SIZE_m(s2+O(1))`.

## 6. Learning and next step

The C-353 phrase “prefix-varying ownership” was too coarse. Variation on a few coordinates can be low; variation drawn from a large enough owner cube can encode an arbitrary prefix function and is high with overwhelming counting probability. The useful object is therefore not owner-mask weight or entropy alone, but the **dimension of a cube contained in the compatible context/proof join relation**, together with the cost of preventing such cubes while covering all low masks.

Next, test whether the C-245/C-260 grammar forces a large owner cube for a rich family of low one-column masks, or whether an O(N)-rule construction can keep all cross-anchor pairs incompatible while covering that family. Preserve parity and repeated-equality calibrations. This is a new support-grammar composition question, not a return to circuit-local selector matrices.
