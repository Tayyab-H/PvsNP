# C-242 — Native certificate antichains and the high-side blocker path

Date: 27 September 2026  
Route: native positive least-fixed-point closure (priority reset from the user's latest continuation note).  
Status: exact grammar and dual-path lemmas; no global q lower bound, near-linear cover, or P-vs-NP proof.

## 1. Priority and exact object

This note supersedes the C-241 DAG-first priority. The primary target is again the native cyclic fusion closure for the actual Gap-MCSP promise. O-153 (global sharing/splicing) is primary; the `N polylog N` / `N^(1+o(1))` full-promise cover search is an independent counter-program. O-152 is secondary unless it gives a near-lossless transfer or a direct native-state invariant.

Fix a rule list with states `[q]`, sides `S in {E,H}`, literal alphabet

```text
Lambda = [N] x {0,1},      ell(x) = {(k,x_k): k in [N]}.
```

For state i and side S, let `I_i^S` be the seed literals whose matching high-side slices lie in that endpoint, and `D_i^S` the predecessor states whose carriers lie in it. On a seed vector X subset Lambda, the least fixed point is

```text
x_i^(0) = 0
x_i^(t+1) = ( OR_{lambda in I_i^E} [lambda in X] OR OR_{j in D_i^E} x_j^(t) )
            AND
            ( OR_{lambda in I_i^H} [lambda in X] OR OR_{j in D_i^H} x_j^(t) ).
```

An output state has empty carrier. On a legal table input x, it is active exactly when the native closure derives the empty set from the matching literal slices of x.

## 2. Minimal-certificate grammar, with cycles handled explicitly

Let `S_i^(t)` be the supports of finite proof trees rooted at i whose height is at most t. A side support at depth t is either a singleton seed `{lambda}` with `lambda in I_i^S`, or a support in `S_j^(t)` for some `j in D_i^S`. Define

```text
A_i^(S,t) = {{lambda}: lambda in I_i^S} union union_{j in D_i^S} S_j^(t)
S_i^(0)   = empty
S_i^(t+1) = {a union b: a in A_i^(E,t), b in A_i^(H,t)}.
```

For a family F of supports, `Min(F)` denotes its inclusion-minimal antichain. Put `C_i^(t)=Min(S_i^(t))`. Then the exact antichain recurrence is

```text
C_i^(t+1) = Min {a union b : a in A_i^(E,t), b in A_i^(H,t)}.
```

This is the antichain semiring form: alternatives combine by `Min(union)`; the two rule obligations combine by `Min({a union b})`. It is a **least** fixed point, not an arbitrary solution of cyclic equations. Every activation has a rank at most q, since the monotone q-bit iteration from zero can add at most q state bits. Hence every minimal sufficient seed set has a proof of height at most q, and `C_i^(q)` is the complete inclusion-minimal certificate family. For output states O,

```text
C_out = Min( union_{i in O} C_i^(q) ).
```

For every seed vector X, the output activates iff some `C in C_out` satisfies `C subset X`. On legal table inputs, `x` is accepted iff some certificate `C` is contained in `ell(x)`. The families can be exponentially large; this is an exact semantic grammar, not an efficient enumeration procedure.

**Proof of completeness at depth q.** For an arbitrary seed vector X, least-fixed-point activation stabilizes after at most q strict additions. Every active state therefore has a finite derivation of height at most q. If X is inclusion-minimal among seed vectors activating a given state, the proof support C is a subset of X and also activates the state, so minimality forces C=X. Conversely, every proof support activates its root. Thus the height-q antichain is exactly the full minimal-support family.

## 3. Exact reuse law and its semantic obligation

At one state i, every E-side support pairs with every H-side support. If `A_i^E` and `A_i^H` are the full finite side-support families, every union `a union b` is a proof support for i; the two supports need not have appeared together in a previously selected proof.

There is also unrestricted context substitution. Let K be the leaf support outside a marked occurrence of i in any accepting proof, and let C be the support of any finite proof rooted at i. Replacing the marked subtree gives an accepting proof with support `K union C`. Thus

```text
K in K_i, C in S_i  =>  K union C in S_out.
```

This is exactly what reuse forces syntactically. It does not guarantee that a table satisfies the mixed support.

For a support A, let `P(A)={k:(k,1) in A}` and `Z(A)={k:(k,0) in A}`. It is consistent iff `P(A) intersect Z(A)=empty`. Its table interval is

```text
Q(A) = [ell_A,u_A],   ell_A = 1_{P(A)},   u_A = 1_{[N] minus Z(A)}.
```

For consistent supports,

```text
Q(K union C) = Q(K) intersect Q(C),
ell_(K union C) = ell_K OR ell_C,
u_(K union C) = u_K AND u_C.
```

In a sound closure for the Gap-MCSP promise, every consistent output-proof support has its **whole** interval inside `SIZE(s2)`. Consequently both canonical endpoints are in `SIZE(s2)`, and

```text
|free(K) intersect free(C)| <= kappa_square(s2) = Theta(s2 log s2)
```

for every compatible context/replacement pair. The endpoint condition is stronger than the free-coordinate bound: it also forbids a high OR-join of the positive rails or a high AND-meet of the upper endpoints.

This is the strongest exact universal closure law currently recorded for state reuse. It strengthens the intended *object* of study, but it does not charge its avoidance to q: opposite rails can make joins inconsistent, and legal joins can have low endpoints.

One concrete safe-reuse mode explains why state collisions alone are weak. If an outside context K already fixes all N coordinates of its anchor x, then every replacement support compatible with K still yields the singleton interval {x}. The shared state may be a common suffix after anchor-specific information was carried by the contexts. Thus a useful lower bound has to charge the construction and cross-compatibility of contexts, not simply the number of anchors visiting a state.

## 4. A dual obstruction for every high table

For a high table z, let `A_z` be the set of rule states active when the seed vector is `ell(z)`. No empty-carrier output state belongs to `A_z`: every active carrier contains z, by induction from the initial high-side literal slices, while an empty carrier does not.

For each inactive state i, its recurrence is false on at least one side. Choose one such side `theta_z(i)`. It satisfies both:

1. no seed in `I_i^(theta_z(i))` matches z;
2. no predecessor in `D_i^(theta_z(i))` is active on z.

Call `theta_z` the high-side blocker map. It is defined on every inactive state, in particular every output root.

**Blocker-path lemma.** For every accepted low table w and rejected high table z, there is a path of at most q state transitions from an output root to a seed literal lambda such that `lambda in ell(w)` and `lambda notin ell(z)`. Every visited state is active on w and inactive on z.

**Proof.** Choose a ranked proof for w from an active output root. At current state i, use the proof's witness on the side `theta_z(i)`. If it is a predecessor j, then j is active on w by the proof and inactive on z by the blocker property; continue. Its w-activation rank is strictly smaller, so this cannot continue for more than q states. It must terminate at a seed lambda selected by the proof. That lambda matches w, while the blocker property says it does not match z. Hence it is a differing truth-table coordinate.

The lemma gives a clean dual picture: a low proof descends through the states active on w and inactive on z against the blocker map of z, then terminates at a mismatch. It is a pairwise witness only. The proof may have depth O(log N) while its full certificate has N-o(N) leaves, so path length alone does not produce a superlinear state lower bound.

## 5. What this teaches about splicing

The same rule has two complementary descriptions:

- its minimal-certificate grammar is a shared AND/OR proof program;
- for each high z, its inactive states carry blockers that hit every accepting proof path.

A genuinely new lower-bound invariant should couple these objects. For state i, the relevant family is not just `C_i`, a rank, or an activation bit. It is the **context/replacement join relation**

```text
J_i = {(Q(K union C), ell_(K union C), u_(K union C)):
       K in K_i, C in S_i, K union C consistent}.
```

All elements of `J_i` are sound low intervals. A candidate theorem must show that covering every low-circuit table forces the closure either to produce a high endpoint in some `J_i`, or to spend superlinear q encoding the blockers that prevent that join. This sharpens the target from “find a shared state” to “bound the compatible low-interval join relation jointly with high blocker maps.” No such entropy/charging theorem is established here.

For the repeated-block anchors `w_g(p,u)=g(u)` from C-234, consistency of a context from g and a replacement from h still requires agreement on every suffix u represented in both supports. Outside that fingerprint, the lower/upper endpoint ownership profile must remain inside `SIZE(s2)`. C-236 caps safe selector masks by `|SIZE(s2)|`, but C-234's O(N) equality cover realizes only prefix-constant masks. The missing quantity is grammar-wide cost of the *set and geometry of safe ownership profiles*, including alternative proof trees—not mask count for one pair.

## 6. Hostile checks and failed lines

- **Certificate width only:** C-230 is sharp at `Theta(s2 log s2)`; another improvement of that threshold is not a route.
- **State collision or rank pigeonhole:** C-238/C-239 show the number of witness skeletons/profiles is already too large; activation rank alone does not determine a skeleton.
- **Blockwise independent hybrids:** C-234 gives an exponential conditional splice bound, but block isolation is not forced; the diagonal-only promise has an O(N) equality cover.
- **Many individually easy anchors:** C-228 has a superpolynomial native readout lower bound by counting while every consistent safe splice identifies an already accepted anchor. It fails the actual high-side promise and does not validate a splice mechanism.
- **Generic pairwise routing:** C-80 and C-160 remain small-cover calibrations; any proposed state charge must recover only O(N) or O(N log N) on them. C-121/C-134/C-161/C-213 and the one-anchor/fractional-cover ceilings also remain mandatory checks.
- **Universal-circuit upper cover:** the direct grammar for `exists d forall k` keeps d globally but is description-sized. Sharing coordinate checks across d loses same-description coherence. No `N polylog N` full-promise cover was found in this phase.

**Concrete native upper-cover attempt.** Fix an ordering of the N truth-table coordinates. For each realized prefix p of length t, let `T_p` be the intersection of its t matching high-side literal slices. A single pair rule intersects the parent carrier with the next matching slice, so all such prefix carriers can be built using

```text
q_prefix <= sum_{t=2}^{N-1} |pi_t(Y)|,
```

where `pi_t(Y)` is the set of length-t prefixes of low tables (duplicate carriers can be merged). Stop at length N-1: for each low w, both completions of its prefix are low, because flipping one truth-table output costs O(n) gates and `s1+O(n)<s2`; hence this carrier contains no high table and is empty. Thus every low anchor is accepted by its prefix chain. This is a valid native cover, but only the bound `q_prefix<=N|Y|` follows in general. Moreover, C-212's `Theta(s1)`-coordinate shattering forces `|pi_t(Y)|=2^t` for the first `t<=c s1` coordinates in any fixed order; each corresponding high-side cylinder is nonempty because `2^(N-t)>|SIZE(s2)|`. Therefore this fixed-order construction is already exponential. It does not rule out adaptive coordinate selection or non-prefix joins; it only closes the fixed-order upper-cover attempt.

The artificial-model request is not yet met: C-228 supplies easy anchors and superlinear readout, but not a forced dangerous splice; C-234 supplies high block hybrids and a conditional theorem, but its localization premise fails. This is a concrete gap in the proposed mechanism, not evidence against the actual target.

## 7. Next proof obligation

Keep O-153 as primary. For the diagonal repeated-block family, define a state-wise object that records jointly (i) the suffix fingerprint in the context/replacement overlap, (ii) coordinate ownership by each side in each prefix block, (iii) the lower and upper endpoint tables, and (iv) the blocker-side choice on states inactive at a high hybrid. Prove one of:

1. a q-sensitive charging theorem: if all these joins stay low for all low anchors, their profile families cannot cover `SIZE(s1)` with q=O(N); or
2. a compact construction exploiting precisely these safe joins, yielding a full-promise `N polylog N` or `N^(1+o(1))` cover.

The first direction must use more than `|SIZE(s2)|`, the maximum safe subcube dimension, or raw profile counts. The second must preserve one circuit description across all N address checks. Until one direction clears these requirements, there is no tangible breakthrough and no change to the overall P-vs-NP status.
