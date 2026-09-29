# C-322 - Empty roots broadcast activation; isolate the pre-root game

Date: 28 September 2026  
Route: Q181 / exact C-319 recurrence, re-audited against C-240/C-252.  
Classification: **EXACT NORMAL FORM; RAW ACCEPTED ACTIVATION PROFILES COLLAPSE; NO q IMPROVEMENT.**

## 1. Empty-root broadcast lemma

For each state i, write `T_i=E_i intersect H_i`. Let `R={r:T_r=empty}` be the output roots. For any root r and any state i,

```text
T_r=empty subseteq E_i and T_r=empty subseteq H_i,
```

so `r in P_i^E intersect P_i^H`. The exact recurrence therefore gives

```text
x_r^t=1  =>  x_i^(t+1)=1 for every i.
```

If R is nonempty, all root activation predicates are identical at the least fixed point: activation of any root forces every other root one round later. The list's output OR can be replaced, as a Boolean predicate, by any fixed root bit. Moreover,

```text
output(w)=1  iff  x_i^*(w)=1 for every state i.
```

Thus every accepted low table has the same final activation profile, the all-ones vector. For activation ranks `tau_i(w)=min{t:x_i^t(w)=1}`, any accepted w satisfies `tau_i(w)<=tau_r(w)+1` for every state i and every first-activating root r. Different roots' finite activation ranks differ by at most one.

This collapses the final-state activation-profile VC/shattering proposal on the YES side: it cannot encode which low circuit description was accepted. Any useful activation-profile statistic must look before the first root, at rank/proof/context data, or at a separate seed-support object.

## 2. Exact root-free pre-acceptance system

The post-root broadcast creates a circular-looking readout if one reasons only with final state bits. Remove it explicitly. Let `V` be the nonempty-consequence states `[q]` with the roots `R` removed. Define `y_i(w)` for i in V as the least fixed point of

```text
y_i^(t+1)(w) =
  (A_i(w) OR OR_(j in P_i^E intersect V) y_j^t(w))
  AND
  (B_i(w) OR OR_(j in P_i^H intersect V) y_j^t(w)),
```

starting from zero. For each root r, set

```text
E_r(w)=A_r(w) OR OR_(j in P_r^E intersect V) y_j(w),
H_r(w)=B_r(w) OR OR_(j in P_r^H intersect V) y_j(w).
```

Then the original list accepts w exactly when

```text
OR_(r in R) (E_r(w) AND H_r(w)) = 1.
```

**Proof.** Before the first root activates, every root bit is zero. Consequently the nonroot coordinates of the full iteration agree, round by round, with the root-deleted iteration y. If a root activates in the full system, take the first one; its two true factors are witnessed only by its seeds or by nonroot predecessors, so the displayed root test holds. Conversely, if the displayed test holds for a root, the full-system nonroot closure contains y by monotonicity, so both root factors eventually become true and the root activates. Once it activates, the broadcast lemma applies. QED.

This is a temporal normalization of the C-319 object. It keeps the exact semantic seed clauses and predecessor sets and exposes the part of the state graph that must do useful work before acceptance. It is compatible with C-240's complementary-singleton/seedless root restriction and C-252's conflict readout, but removes post-acceptance state activations from the readout.

## 3. What this changes and what it does not

The raw final activation profile on every low table is now known exactly, so profile entropy on accepted tables is not a candidate synchronization measure. The live object is the root-free least-fixed-point vector y together with the terminal root tests. Its profiles can vary across low tables, and C-143 already warns that rank/profile diversity alone need not force many rules. A useful invariant must charge the reusable pre-root state graph and its compatible proof/context products, not the broadcast that happens after an empty consequence is derived.

This result gives no q lower bound: the root-free system may still have q states, its clauses may span every cofactor lane, and arbitrary endpoints remain legal. C-257 parity, C-258 repeated equality, C-307 LDPC/local constraints, C-317 safe cylinders, and C-320 owner-mask balls remain mandatory checks. Actual `rho_GapMCSP=N-o(N)`; no full-promise near-linear cover or P-vs-NP proof follows.
