# C-325 - Common-predecessor closure and the C-258 feedback audit

Date: 28 September 2026  
Route: hostile-check C-324 against C-258; isolate two-sided state propagation in the native equations.  
Classification: **EXACT NORMAL FORM + COMPILER ROUTE FILTER; NO q IMPROVEMENT.**

## 1. C-258 has large feedback vertex number despite a linear native subcover

In C-258, fix one block j and one local value a. Write

```text
P_t = U intersect {z_(j,1)=...=z_(j,t)=a},  t=1,...,r.
```

The rule for t uses endpoints `E_t=P_(t-1)` and `H_t=U intersect {z_(j,t)=a}`, with `P_0=U`, and has consequence `T_t=P_t`. In the repeated-block OPS calibration, choose `d log d=O(s1)` blocks, `r=N/d=o(N)`. Every such prefix cylinder has `2^(N-t)>|SIZE(s2)|` completions for large N, so each P_t is nonempty.

For every t<r:

- `T_t=P_t` is contained in `E_(t+1)=P_t`, so the predecessor graph has edge `t -> t+1`.
- `T_(t+1)=P_(t+1)` is contained in both `E_t=P_(t-1)` and `H_t`, so it has edge `t+1 -> t` (indeed this is a common predecessor on both obligations).

Thus each branch contains a bidirected path on r state vertices. Any feedback vertex set must hit every adjacent 2-cycle, requiring at least `floor(r/2)` vertices for that branch. The two value branches across d blocks are disjoint, so the total feedback vertex number is `Omega(dr)=Omega(N)`, while C-258 is an `O(N)`-pair native cover of its repeated-block subpromise.

This does not disprove C-324's circuit upper bound: the bound is valid but loose on this cover. It does disprove the hoped-for shortcut that a useful linear native cover must have small raw feedback vertex number. A q-sensitive compiler must use more than unlabelled cycle deletion.

## 2. Exact factoring of common predecessors

For a root-free state i, let

```text
C_i = P_i^E intersect P_i^H
E'_i = P_i^E minus C_i
H'_i = P_i^H minus C_i
c_i(x) = OR_(j in C_i) x_j
G_i(x) = (A_i OR OR_(j in E'_i) x_j)
         AND (B_i OR OR_(j in H'_i) x_j).
```

After deleting intrinsic self-loops as in C-324, the recurrence factors exactly:

```text
F_i(x) = (c_i(x) OR left_i(x)) AND (c_i(x) OR right_i(x))
       = c_i(x) OR G_i(x).
```

Let `cl_C(y)` be the least superset of y closed under every common-predecessor implication `j -> i` for j in C_i; this is a fixed OR/reachability closure determined entirely by the endpoint-containment graph. Then

```text
mu F = mu (x -> cl_C(G(x))).
```

**Proof.** If x is fixed by F, it is closed under the common-predecessor edges and contains G(x), so `cl_C(G(x)) subseteq x`; hence x is a pre-fixed point of the map `H(x)=cl_C(G(x))`. Conversely, if x is fixed by H, then x is the C-closure of G(x): every 1-coordinate either has G_i(x)=1 or has an active immediate common predecessor. Therefore `F(x)=x`. Thus every F-fixed point is H-pre-fixed, and every H-fixed point is F-fixed. Their least fixed points coincide.

The closure `cl_C` costs only free OR wiring once the static graph is known. Each evaluation of G uses at most one paid AND per state. This form separates free two-sided propagation from the genuinely conjunctive residual transitions. It does **not** bound the number of iterations of H, and can still have a large feedback graph after common-edge closure; it is an exact interface for a sharper compiler, not yet one.

## 3. What this changes in the research model

C-324 remains a correct parameterized compiler, but Q184 cannot use feedback vertex number alone. C-258's backward edges are common predecessors, while forward progress is supplied by one-sided, seed-gated transitions. The promising next question is whether these seed-gated cycles can be eliminated or compiled by a measure on the residual map G after common-predecessor closure, with C-258 taking linear cost. Any proposed measure must still charge the full OPS class's compatible context/proof products and preserve arbitrary semantic endpoints.

This is a precise gap: static common-edge reachability is free; the challenge lies in how the seed-labelled AND map changes the C-closed set. No OPS-specific bound on that interaction is known. C-257 parity remains a separate calibration, while C-281 owner-mask compatibility and C-317's safe-cylinder entropy are unchanged.

**Status:** the low-feedback-number shortcut is rejected by C-258. The common-predecessor factorization is exact, but it yields no superlinear lower bound, near-linear full-promise cover, or P-vs-NP proof. The actual native lower bound remains `q=N-o(N)`.
