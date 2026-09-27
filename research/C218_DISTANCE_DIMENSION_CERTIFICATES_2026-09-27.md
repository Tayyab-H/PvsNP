# C-218 ? Distance?dimension slack and per-column mismatch certificates

Date: 27 September 2026

## Question

Can the improved C-212 Hamming gap be combined with the fact that the low set is much smaller after a monotone restriction, to get a useful selector for deferred-output rect-DAGs?

Write `N=2^n`, `Z={0,1}^N \ SIZE(s2)`, with `s2=N^beta`, and the original low set `Y=SIZE(N^beta/(c n))`. Fix any constant `gamma` with `0<gamma<beta`, and put `Y'=SIZE(N^gamma)`.

## 1. Monotone restriction preserves the lower-bound target

For all sufficiently large n, `Y' subset Y`. Every separator that is 1 on Y and 0 on Z is also a separator that is 1 on Y' and 0 on Z. Therefore

`SepCirc(Y,Z) >= SepCirc(Y',Z)`.

Thus a separator lower bound for the smaller low class transfers to the original promise. Once proved, it can feed the already-audited cover-to-DAG compiler on the original promise. This permits choosing a stricter low threshold as an analytic tool; it does not assert that the stricter promise itself is easier to prove hard.

## 2. A sublinear certificate for each high column

By C-212 sparse patching, there is a constant `a>0` such that every `w in Y'` and `z in Z` differ on at least

`d = a N^beta`

coordinates, for all sufficiently large n. Circuit counting gives

`log2 |Y'| = O(N^gamma n) = o(d)`.

For each fixed high table z, define a coordinate certificate to be a set `Q_z subseteq [N]` such that every low table disagrees with z somewhere on Q_z:

`for every w in Y',  Q_z intersects {i : w_i != z_i}`.

Choose m coordinates uniformly without replacement. For a fixed w, the probability that all m miss its disagreement set is at most

`(1-d/N)^m <= exp(-dm/N)`.

A union bound over Y' shows that if

`m = ceil((N/d)(ln |Y'| + 1))`,

then the probability that some low table is missed is less than one. Hence such a Q_z exists. Since `d=Omega(N^beta)` and `log |Y'|=O(N^gamma n)`,

`|Q_z| = O(N^(1-beta+gamma) n) = o(N)`.

This is a worst-case, per-high-column certificate bound. It sharpens the balanced-threshold O(N) certificate estimate in C-217 by shrinking the low side while preserving the implication to the original lower-bound target.

The certificate number also has a floor: C-212 shattering implies that for every high z, no coordinate set of size at most `Theta(N^gamma)` can be a certificate, because Y' realizes every pattern on each such set. Thus the bound currently lies between `Omega(N^gamma)` and `O(N^(1-beta+gamma)n)`.

## 3. A fixed projection block with many certified columns

Let `v=VCdim(Y')`. Since a shattered v-set requires `2^v` distinct tables,

`v <= log2 |Y'| = O(N^gamma n) = o(d)`.

For any fixed coordinate set Q of size `k=2v`, the Sauer?Shelah bound gives

`|pi_Q(Y')| <= sum_{i=0}^v binom(2v,i) <= (3/4) 2^(2v)`.

So at least one quarter of the Q-patterns are absent from the low projection. Each absent pattern has `2^(N-k)` extensions, more than `|SIZE(s2)|` for large n because `k=o(N)` and `log |SIZE(s2)|=o(N)`. Therefore each absent pattern has high completions. At least a `1/4-o(1)` fraction of high columns have a Q-pattern absent from `pi_Q(Y')`; for those columns, Q certifies a mismatch against every low row.

At the same time, `k<d` for large n, so every low/high pair still has at least `d-k=Omega(d)` mismatches outside Q. This gives a block with both a constant-density certificate branch and a robust residual tail.

## 4. Why this still does not give a DAG

The per-column sets Q_z depend on z. A shared product-rectangle state needs one Bob-side class on which its chosen support works for every column in that class; a separate certificate for each z does not supply such a state. Sending Q_z costs `O(|Q_z| log N)` communication bits, but the transcript tree can still have exponentially many vertices in that message length.

Even on the fixed Q certificate branch, the protocol must route a particular pair `(w,z)` to an actual differing coordinate in Q. The union of the coordinate-output rectangles is not one product rectangle. A fixed-order scanner on Q can have exponential width from low-class shattering. The Sauer bound shows many columns are certifiable; it gives no compact mismatch selector, and the remaining columns can be filtered into many product-hull contexts.

The root support fact also remains distinct from routing: because `|Q|<d`, every pair retains a mismatch outside Q, but no binary rect-DAG suffix for that residual relation has been constructed. C-80/C-160 remain required counterchecks for any proposed state charge.

## 5. Literature boundary and next test

Classical teaching dimension asks for labeled examples that identify one target concept among the concepts in a class. The needed object here is an outside-table coordinate certificate plus a shared two-party selector. The standard teaching-dimension definition does not supply that selector or a transfer to rect-DAG size; see [Notions of teaching and complexity in computational learning theory](https://www.cs.columbia.edu/~rocco/Public/ntd.pdf).

The next concrete test is to analyze the projected class `P_Q=pi_Q(Y')`: can its circuit-description structure yield a polynomial-size rect-DAG for finding a mismatch between `p in P_Q` and `q outside P_Q`, while an equal-pattern branch safely continues into the tail? Any proposed construction must bound the product hull after merges and charge the residual columns. A lower bound on this restricted block relation could also be useful, but by itself it must be combined with the fraction and number of block branches to exceed the O-141 transfer threshold.

## Disposition

C-218 proves a parameterized certificate improvement and a Sauer-based density lemma. These are a new structural lead, not a C-75 DAG bound: no shared certificate selector, projected-block router, superlinear `rho_prom` bound, or P-vs-NP proof has been obtained. The compiler and target remain unchanged: `rho_prom <= O(S_rect)`, `S_rect=O(q^3/log q)`, and the standard-DAG target is `S_rect>N^(3+3epsilon)/log N` to force `q>N^(1+epsilon)` through the current compiler. O-141 stays open.



## C-218-A ? A fixed-order router on the projected block is still exponentially wide

The fixed-block certificate branch does not admit the obvious first-mismatch scan. This can be proved even though the projected Bob set is only the complement of `pi_Q(Y')` and the original C-217 high-completion count no longer applies directly.

Let `v=VCdim(Y')`, choose any `Q` of size `k=2v`, and let `P=pi_Q(Y')`. Sparse interpolation gives a constant `alpha>0` such that Y' shatters every set of `t'=floor(alpha*N^gamma)` coordinates; hence `v>=t'`. Fix any first-mismatch scan order on Q and let J be its first `j=floor(t'/2)` coordinates. For each pattern `p` on J, low shattering supplies a row `w_p in Y'` extending p. Consider the suffix patterns on `Q\J` that occur among members of P with J-pattern p. This suffix family has VC dimension at most v, and its domain has size `k-j=2v-j>v`. Sauer-Shelah therefore bounds its size by `sum_{i=0}^v binom(k-j,i)<2^(k-j)`. Choose an omitted suffix pattern r_p. Then `q_p=(p,r_p)` is outside P. Its full truth-table cylinder has `2^(N-k)>|SIZE(s2)|` extensions, so at least one extension `z_p` is high. Thus `(w_p,z_p)` agrees on J and reaches the scan frontier after that prefix.

For distinct p,p', the product rectangle at a merged frontier state would contain `(w_p,z_p')`, a valid low/high pair whose mismatch occurs inside the already-scanned J. An immediate first-mismatch scanner cannot route that cross-pair to the shared frontier. Hence all `2^j=2^(Theta(N^gamma))` prefix patterns require distinct states.

This closes the fixed-order scan as a polynomial-size router for the C-218 common-block certificate branch. It does not lower-bound adaptive/revisiting rect-DAGs or rule out a block router that defers output and safely uses later coordinates.
