# C-326 - Exact nested-closure compiler for the C-258 equality cover

Date: 28 September 2026  
Route: test Q185 on C-258 and eliminate its seed-labelled feedback cycles exactly.  
Classification: **EXACT SUBPROMISE COMPILER + FINITE EXHAUSTIVE CALIBRATION; NO FULL-OPS q IMPROVEMENT.**

## 1. Richness regime

Let N=dr with d>=2, r>=4, and let U be the high set. Write M=2^N-|U| for the number of non-high tables. Assume U is disjoint from the repeated-block family `Rep_{d,r}` and

```text
2^(r-3) > M.
```

Then every coordinate cylinder with at least r-3 free coordinates meets U. This supplies high witnesses for all non-containment checks below. In the OPS setting, `M=|SIZE(s2)|=2^(o(N))`; choose the repeated-block parameters with `r=o(N)` and `r>log2 M+3` (available for sufficiently small fixed beta in the project regime). Every nonroot carrier in C-258 is then nonempty, and the sole empty carrier is the final product root `A_d`.

## 2. Solve one nested prefix branch

Fix block j and bit a. Let `p_t` denote the state whose carrier is

```text
P_t = U intersect {z_(j,1)=...=z_(j,t)=a},  t=1,...,r,
```

and let `b_t(w)=[w_(j,t)=a]`. After deleting self-loops, the common-predecessor relation within this branch points from every deeper prefix to every shallower prefix: for s>t, `P_s` is contained in both endpoints of rule t. The only residual forward transition is from p_(t-1) through rule t. The first rule has its U endpoint as a true seed; for t=2 the first-prefix literal is also a seed on the left. For t>=3 a single literal slice cannot imply the first t-1 fixed coordinates. No carrier from another branch/block or from a merge state satisfies both endpoint containments; the richness assumption provides a high counterexample to each proposed containment.

Thus, with `G_t` the residual AND part after factoring common predecessors, the exact equations are

```text
G_1 = b_1
G_2 = (b_1 OR x_1) AND b_2
G_t = x_(t-1) AND b_t                         (3 <= t <= r)
x_t = OR_(s=t,...,r) G_s                      (1 <= t <= r).
```

The last line is the static common-edge closure from C-325. Its least fixed point is

```text
x_t* = AND_(u=1,...,t) b_u.
```

Indeed, these prefix products satisfy the equations: their values are nonincreasing in t, so the suffix OR `OR_(s>=t) G_s` equals the t-th product. For leastness, in any fixed point b_1=1 forces x_1=1 through G_1; inductively, if the first t-1 bits match and b_t=1, then G_t=1 (including t=2, where `b_1 OR x_1=1`). Hence every fixed point contains every 1 of the prefix-product vector. The terminal state p_r is active exactly when the whole block is constant a.

Define

```text
B_j = x_(j,0,r)* OR x_(j,1,r)*,
```

so `B_j=1` exactly when block j is constant.

## 3. Solve the nested block-merge system

Let c_j be the C_j state and let a_k be the A_k state for 2<=k<=d-1; use `a_1=c_1`. The containment audit gives, in the root-deleted system,

```text
c_1 = B_1 OR OR_(l=2,...,d-1) a_l
c_j = B_j OR OR_(l=j,...,d-1) a_l       (2 <= j < d)
c_d = B_d

a_k = OR_(l=k+1,...,d-1) a_l
      OR (a_(k-1) AND c_k)                (2 <= k <= d-1).
```

The `A_{d-1}` endpoint in the final empty-root test is represented by a_(d-1), and the `C_d` endpoint by c_d. Thus the original cover accepts exactly when `a_(d-1) AND c_d` is true. The root itself is removed before solving these equations, as required by C-322.

The least solution is

```text
a_k* = AND_(j=1,...,k) B_j       (1 <= k < d)
c_j* = B_j                       (1 <= j <= d).
```

For fixed-point verification, the prefix products are nonincreasing, so every future-`a` OR is either zero or its first term; substitution gives the displayed values. For leastness, c_1>=B_1 gives a_1>=B_1. If a_(k-1) contains the first k-1 block tests and B_k=1, then c_k>=B_k and the paid transition forces a_k=1. Also every c_j is at least B_j. This proves the candidate is below every fixed point, hence is the least one.

Consequently the exact separator computed by the C-258 list on the rich OPS promise is

```text
AND_(j=1,...,d) [ OR_(a in {0,1}) AND_(t=1,...,r) [w_(j,t)=a] ],
```

which accepts precisely `Rep_{d,r}` and rejects U.

## 4. Circuit cost and why this beats raw feedback number

Use two conjunction chains per block, one for each constant value; OR their outputs for B_j; then AND the d block tests. With free arbitrary-fan-in OR, the AND count is

```text
2d(r-1) + (d-1) = 2N-d-1.
```

This is a linear compiler for the **exact** output predicate of the C-258 native list, even though C-325 proved that its raw root-free feedback vertex number is Omega(N). The shortcut succeeds because every common-predecessor 2-cycle in a prefix branch is resolved by a nested seed product; the merge layer has the same absorption pattern. It is stronger than merely exhibiting some unrelated separator for the subpromise.

## 5. Finite hostile checks

An ephemeral exhaustive evaluator constructed the exact C-258 endpoint sets and iterated the native least-fixed-point recurrence for every table in `U union Rep`. It found zero mismatches for `(d,r)=(2,2),(2,3),(3,2),(2,4),(4,2),(3,3)`, covering N up to 9 and q=`2N+2d-1`. This checks the small finite semantics only; the proof above uses the explicit cylinder-richness condition for the asymptotic OPS case. No test file was added.

## 6. Scope and next obligation

C-326 resolves the C-258 calibration required by Q185 and shows that common-edge closure can support a linear compiler despite large graph feedback. Its proof uses a very special nested prefix/product hierarchy. It gives no elimination rule for arbitrary endpoint-containment graphs, no compiler for every q-state system, and no extra lower bound or upper bound for the full `SIZE(s1)` class. The new task is to characterize seed-labelled nested-closure systems in a form stable under compatible C-281 context/proof products, then determine whether any such structure is forced or forbidden for full OPS covers.

**Status:** exact subpromise result only. The actual Gap-MCSP lower bound remains `q=N-o(N)`; no full-promise near-linear cover or P-vs-NP proof follows.
