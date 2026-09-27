# C-258 — Explicit native cover for a repeated-block low subfamily

Date: 27 September 2026  
Scope: test whether the actual high set `U={z:CC(z)>s2}` admits a linear native closure on a structured subfamily of `SIZE(s1)`. It does. This recovers the diagonal-equality hostile check from C-234 in the native rule syntax; it is not a cover of all `SIZE(s1)`.

## 1. Repeated-block anchors

Let `N=dr` and partition the coordinates into `d` blocks of length `r>=2`. Define

\[
\mathsf{Rep}_{d,r}=\{w_g:g\in\{0,1\}^d,\ w_g(j,t)=g_j\text{ for all }j,t\}.
\]

Assume `Rep_{d,r} subseteq SIZE(s1)`, hence `Rep_{d,r} intersect U=empty`, and that every one-coordinate slice of `U` is nonempty. The latter holds for the OPS high side by its two-coordinate shattering property. This family has `2^d` anchors. When the blocks are truth-table suffix repetitions, each member ignores the suffix inputs and can be implemented by a lookup circuit on the `log d` prefix bits; for example `O(d log d)` gates suffice, so one may take `d log d=O(s1)`.

For each block `j`, value `a`, and prefix length `t`, define

\[
P_{j,a,t}=U\cap\{z:z_{j,1}=\cdots=z_{j,t}=a\},\quad P_{j,a,0}=U,
\]

and let

\[
C_j=P_{j,0,r}\cup P_{j,1,r}=U\cap\{z:\text{block }j\text{ is constant}\},\qquad
A_k=\bigcap_{j\le k}C_j.
\]

Then `A_d=U intersect Rep_{d,r}=empty`.

The same construction gives a general product-code statement. Partition the coordinates into blocks `B_1,...,B_d`; choose a nonempty local codebook `A_j subseteq {0,1}^{|B_j|}` per block; and let the target family be the product `Y=A_1 x ... x A_d`. If `Y intersect U=empty` and every literal slice of U is nonempty, then a native list covers all of Y with

\[
q\leq \sum_{j=1}^d |A_j|\,|B_j|+2d-1.
\]

For each local word `a in A_j`, define `P_{j,a,0}=U` and

\[
P_{j,a,t}=U\cap\{z:z|_{B_j[1..t]}=a|_{[1..t]}\}.
\]

List `(P_{j,a,t-1}, U intersect {z:z_{B_j[t]}=a_t})` for each t. Its carrier is `P_{j,a,t}`. Merge the local words using `C_j=union_{a in A_j}P_{j,a,|B_j|}=U intersect {z:z|_{B_j} in A_j}` and the pair `(C_j,U)`. Finally intersect `C_1,...,C_d` in a chain. If a selected local-word carrier is empty, the low anchor already derives empty; otherwise it is a generated subset of `C_j` and activates the merge. The final carrier is `U intersect Y=empty`. The rule count is `sum_j |A_j||B_j|+d+(d-1)`. Repeated blocks are the special case `A_j={0^r,1^r}` for every j.

## 2. Listed fusion pairs

For the repeated-block case, use these endpoint pairs, all subsets of `U`:

1. For every block `j`, bit `a`, and `t=1,...,r`, list
   \[
   (P_{j,a,t-1},\ U\cap\{z:z_{j,t}=a\}).
   \]
   The rule carrier is exactly `P_{j,a,t}`.
2. For every block `j`, list `(C_j,U)`, whose carrier is `C_j`.
3. For `k=2,...,d`, list `(A_{k-1},C_k)`, whose carrier is `A_k`.

There are `2dr+d+(d-1)=2N+2d-1` pairs.

## 3. Completeness and soundness

Fix a repeated anchor `w_g`. In block `j`, choose `a=g_j`. The first rule in that block has `P_{j,a,0}=U` and its second endpoint is the initial matching slice at coordinate `(j,1)`, so it adds `P_{j,a,1}`. Inductively, if `P_{j,a,t-1}` is in the closure, the matching literal slice at `(j,t)` is the second endpoint of the next rule, so that rule adds `P_{j,a,t}`. In particular the terminal carrier `P_{j,a,r}` is generated and is contained in `C_j`; the merge rule `(C_j,U)` therefore adds `C_j` (the endpoint `U` is in the upward closure of any nonempty initial slice).

Once every `C_j` has been added, the rules `(A_{k-1},C_k)` add `A_2,...,A_d`. The final carrier is `A_d=empty`, since no high table lies in the repeated-block family. Thus every `w_g` is covered.

For soundness, fix any high anchor `z in U`. Every initial matching slice contains `z`. Upward closure preserves `z`, and intersections of sets containing `z` still contain `z`. So no empty set is ever generated from a high anchor. This establishes a native cover of the promise `Rep_{d,r}` versus the actual OPS high side, with `q=O(N)`.

## 4. Splice interpretation and what it does not prove

Any consistent finite output proof support has a cylinder disjoint from `U`: otherwise a high extension would activate the same proof tree, contradicting soundness. Hence every consistent context/subproof splice remains inside `SIZE(s2)`. The rule list uses an equality fingerprint across each repetition block, so it has a compact global invariant that protects cross-context reuse.

This gives a concrete reason local richness and low-anchor entropy are insufficient. The family can be exponentially large in `d=o(N)`, each anchor can have a short circuit, the high side is the actual high-complexity set, and the native cover still costs only `O(N)` for this subpromise. The construction does **not** cover all of `SIZE(s1)`: general small circuits need not be constant on any shared block partition. The missing global theorem must force incompatibility across enough distinct circuit descriptions, beyond any such equality fingerprint, or the upper-bound programme must find a small collection of fingerprints covering the full class.

This is closely related to C-234's diagonal equality separator, but here the endpoint pairs are written directly in the native C-74 recurrence. It is not a superlinear upper or lower bound for the full Gap-MCSP promise and does not resolve P vs NP.
