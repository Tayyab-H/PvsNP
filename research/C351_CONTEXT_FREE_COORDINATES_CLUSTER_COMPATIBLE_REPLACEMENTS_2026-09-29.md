# C-351 - Compatible replacements cluster on a context's free coordinates

Date: 29 September 2026  
Route: Q208 / sharpen multi-hole substitution using the support width forced by soundness.  
Classification: **EXACT CONDITIONAL PROJECTION CONSTRAINT; NO q LOWER BOUND.**

## 1. Setup

Let `K` be an output context with one hole labeled by state `i`. Let `w_0` be a low anchor matched by `K`. For each anchor `w_a`, let `P_a` be a finite proof support rooted at `i`, matched by `w_a`, and suppose `K union P_a` is consistent. By substitution it is an accepting output support. Put

```text
R = [N] minus Var(K),
O_a = R minus Var(P_a),
kappa = kappa_square(s2).
```

The set `R` consists of coordinates not already fixed by the context.

## 2. Projection-clustering lemma

For every such replacement,

```text
|O_a| <= kappa.
```

Indeed, the compatible output support `K union P_a` has a completion cylinder contained in `SIZE(s2)`. It can leave at most `kappa` coordinates free. The coordinates left free are exactly `R minus Var(P_a)`.

Now suppose two replacement supports `P_a` and `P_b` are mutually consistent. Whenever `w_a` and `w_b` differ at a coordinate of `R`, the two supports cannot both mention that coordinate: they would contain opposite literals. Therefore

```text
dist(w_a restricted to R, w_b restricted to R)
    <= |O_a union O_b|
    <= 2*kappa.
```

For any family of replacement proofs that are pairwise mutually consistent and individually compatible with the same context `K`, their anchors have projected diameter at most `2*kappa` on `R`.

This gives a necessary condition for a **pairwise-compatible** replacement menu at one hole: its anchor restrictions have pairwise distance at most `2*kappa` on `R`. This condition must not be read as a bound on every menu in a multi-hole product. A full product of choices across holes requires compatibility between choices at different holes; it does not require two alternatives at the same hole to be mutually consistent. The distinction is audited in C-352.

## 3. Exact limitation

The condition can be vacuous. If `K` fixes every coordinate, then `R=empty`, and it can protect an arbitrary number of mutually incompatible anchor-specific replacement proofs without enabling a cross-splice. More generally, the argument gives no useful restriction when `|R|<=2*kappa`. At OPS scale `kappa=Theta(s2 log s2)`, while the C-336 local menu varies on `Theta(s2)` coordinates, so this bound alone does not rule out that menu. Nor does it bound how many different contexts one state can generate.

C-257 parity and C-258 repeated equality remain consistent: both can restrict compatible products or use context coordinates to protect them. No lower bound on the number of contexts or on the q-rule grammar follows from the projection diameter alone.

## 4. The next q-sensitive dichotomy

For each balanced state cut from C-350, split on its context free set `R`:

1. If `|R|` is small, the context fixes almost the whole anchor. A lower bound would need to charge how many such near-complete contexts the q-state grammar can generate while covering all low tables.
2. If `|R|` is large, any jointly compatible replacement menu is confined to projected diameter `2*kappa` on `R`. A lower bound would need a low family whose restrictions disperse across every such large R, and a proof that enough alternatives must share one context/hole product.

This is a conditional projection constraint on compatible replacements, not a strengthening of C-336's general product-or-selector gap. It supplies no count of contexts and no q-charge. The actual native lower bound remains `q >= N-o(N)`; no superlinear bound, full-promise near-linear cover, or P-vs-NP proof follows.
