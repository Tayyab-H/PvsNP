# C-256 — Common hard translates obstruct static source-answer decoders

**Date:** 27 September 2026  
**Route:** standard acyclic shared product-rectangle DAG for C-75  
**Status:** proved route-specific no-go theorem; not a C-75 lower bound

## 1. Question

C-255 fixed the high-image problem for a source reduction. If

`Y = SIZE(s1)`, `L = SIZE(s2)`,

then `|Y xor L| <= |Y||L| = 2^{o(N)}` in the OPS regime. Choose

`r notin Y xor L`.

For every low base table `u in Y`, `u xor r notin L`. Thus translating every Bob base table by the same `r` makes every image high. The remaining obligation is cut soundness: every signed mismatch output of the image pair must decode to one fixed valid source answer throughout the whole source rectangle inducing that output.

This note tests that obligation against hard Karchmer–Wigderson (KW) relations and the bit-pigeonhole search relation used by Beame–Whitmeyer. It proves two route-specific obstructions. For rich KW sources, cut soundness reconstructs `r` from only `O(M)` low tables. For full-domain BPHP collision search, static label soundness is impossible already from the two collision answers assigned to one target coordinate. These results rule out the common-translate/static-label reduction interface for these sources; they do not bound the target DAG itself.

## 2. Source and reduction model

Let `f:{0,1}^M -> {0,1}` and put

`X=f^{-1}(1)`, `Y_f=f^{-1}(0)`.

The signed KW relation on `X x Y_f` outputs `(i,a)` exactly when `x_i=a` and `y_i=1-a`.

Assume the following proposed encoding:

1. For each `x in X`, a base table `u_x in SIZE(s1)`.
2. For each `y in Y_f`, a base table `v_y in SIZE(s1)`.
3. A single fixed mask `r in {0,1}^N`, with every translated Bob table `v_y xor r` outside `SIZE(s2)`.
4. A **static output decoder** `delta(k,b)=(i,a)`, depending only on the C-75 output label `(k,b)`, such that every mismatch
   `u_x[k]=b != (v_y[k] xor r[k])`
   decodes to a valid KW answer `(i,a)` for that pair `(x,y)`.

The decoder is static in the standard sense of a relation reduction: it cannot inspect the source inputs or the path/terminal node of a particular protocol. The theorem below concerns this reduction interface, not arbitrary simulations with extra communication or terminal-specific decoding.

## 3. Rich hard KW functions exist

Call `f` **two-wise rich** if both `X` and `Y_f` project onto all four bit patterns on every pair of distinct source coordinates. In particular, each source coordinate takes both values on each side.

For every sufficiently large `M`, there are two-wise-rich functions satisfying

`f(0^M)=1`, `f(e_i)=1` for every `i in [M]`, and `f(1^M)=0`,

whose Boolean circuit complexity is `Omega(2^M/M)`.

Reason: choose a Boolean function uniformly subject to those `M+2` prescribed values. Failure of two-wise richness has probability at most `O(M^2) 2^{-Omega(2^M)}`. The number of size-`S` Boolean circuits is at most `2^{O(S log(M+S))}`; with `S=c 2^M/M` and a sufficiently small constant `c`, this is exponentially smaller than the `2^{2^M-(M+2)}` prescribed-value completions. Hence a function meeting richness and the circuit lower bound exists.

The KW communication DAG complexity of this source is the Boolean circuit complexity of `f`, up to the usual constant/input-source conventions.

## 4. Theorem: static cut-sound decoding forces a small translate

**Theorem.** Let `f` be two-wise rich and satisfy the prescribed values above. If a common-translate encoding as in Section 2 has a static cut-sound decoder, then there is a Boolean circuit for `r` of size

`O(M s1)`.

Consequently, if `s2 >= C M s1` for the absolute circuit-composition constant `C`, then `r in SIZE(s2)`. Since the all-zero table belongs to `SIZE(s1)`, this implies `r in SIZE(s1) xor SIZE(s2)`, contradicting the hard-translate condition.

### Proof

For each address `k`, write

`A_k(x)=u_x[k]` for `x in X`, and `B_k(y)=v_y[k] xor r[k]` for `y in Y_f`.

Call `k` active if some source pair has a mismatch at coordinate `k`.

**Step 1: At every active coordinate, both sides vary.** If `A_k` is constant and a mismatch occurs, one fixed signed label `(k,b)` is produced for every `x in X` against some fixed `y` (or all `y` in a nonempty subset). Static cut soundness would require all `x in X` to have the same value at one fixed source coordinate. Two-wise richness forbids this. The symmetric argument applies if `B_k` is constant. If both are constant and opposite, the mismatch rectangle is all of `X x Y_f`, which also cannot be a valid fixed signed KW cut because neither side is constant on any source coordinate. Therefore an active `k` has both `A_k` and `B_k` nonconstant. Conversely, if both vary, their independent product domains realize both mismatch signs. An inactive coordinate has `A_k` and `B_k` equal to the same constant on their respective domains.

**Step 2: A cut-sound active coordinate copies one source bit, up to a common flip.** For an active `k`, let

`delta(k,0)=(i_0,a_0)` and `delta(k,1)=(i_1,a_1)`.

Both mismatch rectangles are nonempty. Soundness gives

`{x in X:A_k(x)=0} subseteq {x:x[i_0]=a_0}`,

`{x in X:A_k(x)=1} subseteq {x:x[i_1]=a_1}`.

If `i_0 != i_1`, these two containments exclude the pattern
`(x[i_0],x[i_1])=(1-a_0,1-a_1)` from `X`, contrary to two-wise richness. Thus `i_0=i_1=i`. Since `A_k` takes both values and `X` has both values at coordinate `i`, we must have `a_1=1-a_0`; hence

`A_k(x)=x[i] xor a_0` for every `x in X`.

Applying the same argument to the two column sides of the mismatch rectangles gives

`B_k(y)=y[i] xor a_0` for every `y in Y_f`.

So the same source coordinate and same flip govern the low Alice bit and translated Bob bit.

**Step 3: Recover the active-coordinate mask from `M+1` low tables.** Let `u_0` and `u_{e_i}` be the low tables assigned to `0^M` and `e_i`. Define the Boolean table

`A(k) = OR_{i=1}^M (u_0[k] xor u_{e_i}[k])`.

At an active coordinate, Step 2 shows that exactly the term for its copied source coordinate is 1. At an inactive coordinate, `u_x[k]` is constant throughout `X`, so every term is 0. Thus `A(k)=1` exactly on the active coordinates.

**Step 4: Recover the mask itself.** Let `v_1` be the low base table assigned to `1^M in Y_f`. At an active coordinate with copied index `i` and flip `a_0`,

`u_0[k]=a_0`, while `v_1[k] xor r[k]=1 xor a_0`.

At an inactive coordinate, no source pair mismatches, so the common constant on `X` and the common constant on `Y_f` agree; therefore
`v_1[k] xor r[k]=u_0[k]`.

Both cases combine to

`v_1 xor r = u_0 xor A`,

and hence

`r = v_1 xor u_0 xor A`.

Each table `u_0`, `u_{e_i}`, and `v_1` has circuit size at most `s1`. XOR and OR composition therefore computes `r` with `O(M s1)` gates. This proves the theorem. `0^N in SIZE(s1)`, so if `r in SIZE(s2)` then `r=0^N xor r` belongs to `SIZE(s1) xor SIZE(s2)`, contradicting its choice. QED.

## 5. OPS parameter check

Suppose `s2/s1 = c n`, where `n=log_2 N` and `c` is the fixed OPS gap constant. Set `M=ceil(kappa log_2 N)`. Then the reconstruction has size `O(kappa s1 log N)`. It contradicts the translate choice whenever `c` exceeds the absolute composition constant times `kappa`.

Meanwhile the source KW DAG lower bound is `Omega(2^M/M)=N^{kappa-o(1)}`. Thus, for any fixed target exponent `3+3 epsilon`, this source can be made quantitatively large enough by choosing `kappa>3+3 epsilon`, provided the OPS gap constant is large enough that the reconstruction circuit still fits below `s2`. This parameter condition is explicit; C-256 does not silently assume arbitrary constants.

## 6. Full-domain bit-pigeonhole search has a two-answer cover obstruction

The obstruction has a general answer-projection form. For a source relation `R subseteq X x Y x O`, let `P_o^X={x: there exists y with (x,y,o) in R}` and `P_o^Y={y: there exists x with (x,y,o) in R}`. Let `tau_X` and `tau_Y` be the minimum number of these projections needed to cover their respective domains.

**Two-label lemma.** If `tau_X>2` and `tau_Y>1`, no static cut-sound decoder can map every target mismatch label `(k,b)` to a fixed answer for an image of the full product `X x Y` in which every pair maps to distinct C-75 tables. At an active target coordinate, a constant Alice bit would make a nonempty mismatch rectangle project onto all of `X`, contradicting `tau_X>2`; a constant Bob bit would similarly project onto all of `Y`, contradicting `tau_Y>1`. Hence both bits vary, and the two nonempty signed mismatch rectangles force `X` to be covered by two answer projections, again contradicting `tau_X>2`.

This criterion is useful before designing an encoding: a single target coordinate has only two signed labels, so static decoding can cover the source's Alice domain by at most two answer projections. A terminal-specific decoder escapes only by using path-refined source rectangles; its refinement cost must then be bounded in the binary DAG model.

Beame–Whitmeyer's BPHP search lower bound uses the natural split of a full assignment into Alice's and Bob's halves. For each pigeon `i`, write its two half-rows as `x_i` and `y_i`. A valid violated-clause answer necessarily names a pair `i != j` whose half-rows agree:

`x_i=x_j` and `y_i=y_j`.

This necessary condition is enough for the following no-go.

**Claim.** There is no static cut-sound decoder from all C-75 signed mismatch labels `(k,b)` to BPHP collision-pair answers for any maps from the full Alice and Bob assignment domains, provided every mapped pair is promised low-versus-high (for example by the C-255 common hard translate).

**Proof.** Fix a coordinate `k` and write `A(x)=u_x[k]`, `B(y)=v_y[k] xor r[k]`. A mismatch label `b` induces the nonempty product rectangle

`X_b x Y_{1-b}`, where `X_b={x:A(x)=b}` and `Y_{1-b}={y:B(y)=1-b}`.

If this rectangle is nonempty and its static decoder names pair `(i,j)`, cut soundness requires `X_b` to lie entirely in the Alice equality set `E^X_{ij}={x:x_i=x_j}` and `Y_{1-b}` entirely in `E^Y_{ij}={y:y_i=y_j}`. No equality set is the full assignment domain.

If `A` is constant, any nonempty mismatch has `X_b` equal to the whole Alice domain, impossible; similarly `B` cannot be constant. Thus any active coordinate has both bit functions nonconstant, so both signed mismatch rectangles `X_0 x Y_1` and `X_1 x Y_0` are nonempty. Their decoders give two fixed pairs `(i,j)` and `(p,q)`, and soundness forces

`X subseteq E^X_{ij} union E^X_{pq}`.

But two fixed equality constraints cannot cover the full Alice domain. The graph consisting of the two named pair-edges is a forest, so 2-color its vertices and give each pigeon one of two distinct half-row strings according to that coloring. Both listed pair-equalities then fail simultaneously. Hence no coordinate can be active. That contradicts promise totality: each mapped Alice table is in `SIZE(s1) subseteq SIZE(s2)`, each mapped Bob table is outside `SIZE(s2)`, so they differ somewhere.

The same proof applies if the decoder outputs an exact falsified BPHP clause rather than a pair, because each valid clause output still entails the named pair's half-row equality. The 2025 paper explicitly uses these collision-pair rectangles as a necessary condition for each sink: `R_ij={(x,y):x_i=x_j, y_i=y_j}`. See Beame–Whitmeyer, ICALP 2025, Section 5 and Theorem 1.7: [official paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.21/LIPIcs.ICALP.2025.21.html).

This is a second no-go, distinct from the KW reconstruction: it does not use the circuit-size budget for `r`, only full source domains, a static label decoder, and the fact that no two collision-pair row predicates cover all Alice assignments.

## 7. What these results prove—and do not prove

These are proof-level negative results about one transfer strategy:

- The common hard translate solves image hardness.
- For two-wise-rich KW sources, static cut soundness forces that same translate to have a circuit of size `O(M s1)`.
- For full-domain BPHP search, static cut soundness is impossible even before considering the translate's size.
- Therefore the common-translate/static-label method cannot transfer either of these source relations as stated.

This is **not** a lower bound on `S_rect`, a lower bound on fusion closure, or a P-vs-NP result. It does not rule out another source answer geometry, input-dependent or terminal-specific decoding, a different hard-image construction, or a direct bottleneck-capacity proof. Such a decoding scheme would need an explicit size-preserving simulation: the decoder cannot use source information for free, and terminal-specific relabeling must be valid on the entire pulled-back sink rectangle. Those alternatives need their own exact cost and cut-soundness checks.

### Exact cost condition for terminal-specific decoding

Suppose a target rect-DAG `D` has `S` vertices and the proposed source maps send every source pair into the C-75 promise. Pulling each node rectangle back through the partywise maps preserves product rectangles and the child-cover condition. For each sink `t`, let `Q_t` be its pulled-back source rectangle. If `Q_t` has a source-search rect-DAG of size at most `T_t`, replacing that sink by this refiner yields a source rect-DAG of size at most

`S + sum_t T_t`.

Thus, if all sink refiners have size at most `T`, a source lower bound `L_src` gives only

`S >= L_src/(1+T)`.

For BPHP with hole parameter `n_0=K(log N)^4`, Beame–Whitmeyer's lower bound is `L_src=2^{n_0^{1/4}/sqrt(2)-2}=N^{Theta(K^{1/4})}`. A polynomial refinement cost `T=N^d` could still be absorbed by choosing fixed `K` large enough, provided the exponent left after subtracting `d` exceeds `3+3 epsilon`. The missing theorem is a bound on the source-search complexity of the **actual sink preimages** `Q_t` created by an arbitrary small C-75 DAG. The trivial refiner for the whole source domain is already as hard as the source problem and gives no transfer. This is the precise terminal-specific avenue left open by the static-label no-go.

## 8. Research update and next test

The failure is structural, not a missing mask-count estimate: a rich KW source exposes enough one-bit test inputs (`0^M`, `e_i`, `1^M`) that every active target coordinate must copy one source bit with a common phase, and those tests reconstruct the supposedly hard translate. This rules out repeating the same translate-plus-rich-KW idea with a different random hard function.

Next, do not repeat a static-label common-translate construction for KW or BPHP. Test whether terminal-specific decoding can be compiled with a sufficiently small overhead, or whether an answer relation with a different rectangle geometry evades both obstructions. In parallel, prioritize the direct per-node bottleneck-capacity lemma on the actual C-75 promise. Preserve C-255's product-hull and q-to-DAG thresholds.

## References and project links

- C-255 exact DAG/source-reduction audit: `research/C255_SHARED_DAG_ROUTE_RESTART_2026-09-27.md`.
- KW circuit/DAG correspondence: see the primary references collated in C-255.
- OPS target and compiler losses: `research/GOAL.md`, `research/OPEN_OBLIGATIONS.md`.
