# C-217 — Uniform shattering rules out a small fixed-order mismatch scanner

Date: 27 September 2026

## Question and scope

Test the most direct description-aware shared-DAG construction: inspect the truth-table coordinates in one fixed order, halt with the current mismatch as soon as one is found, and reuse the continuation state after equal prefixes. The result below rules out every such first-mismatch fixed-order scan for the actual low/high promise at superpolynomial size. It does not rule out arbitrary acyclic rect-DAGs, which may defer output after a mismatch, revisit coordinates through different suffixes, or use non-scan state predicates.

Write `N=2^n`, `Y=SIZE(s1)`, `Z={0,1}^N\SIZE(s2)`, and `M2=|SIZE(s2)|`. From C-212, there is a constant `alpha>0` such that `Y` shatters every fixed set of `t0=floor(alpha*s1)` table coordinates. Also `log2(M2)=O(s2*log(n+s2))=o(N)` in the OPS regime, so `2^(N-j)>M2` whenever `j<=t0` for sufficiently large N.

## First-mismatch ordered-scan theorem

Fix any permutation `pi` of the N table coordinates. Consider a deterministic acyclic product-rectangle protocol with these restrictions:

1. on every nonterminal path it compares coordinates in the order `pi(1),...,pi(N)`;
2. unequal bits immediately terminate with the current signed mismatch output;
3. equal bits proceed to the next coordinate, and later states may not output a passed coordinate.

Then every such protocol for signed mismatch on `Y x Z` has at least

\[
2^{t0}=2^{\Omega(s1)}
\]

reachable continuation states. In particular, since `s1=N^beta/(c n)` for fixed `0<beta<1`, this lower bound exceeds every fixed polynomial in N.

### Proof

For each `j<=t0`, the first j coordinates `P_j={pi(1),...,pi(j)}` are shattered. Thus every pattern `p in {0,1}^j` is the restriction of some low table `w_p in Y`.

The same pattern has a high completion: the cylinder of all N-bit strings extending p has `2^(N-j)>M2` members, while only M2 strings are outside Z. Choose `z_p in Z` extending p. The pair `(w_p,z_p)` agrees on the first j scanned coordinates, so it reaches a continuation state `v_p` after that matched prefix.

These states are pairwise distinct. If `p!=p'` reached the same product-rectangle state, that state's row projection would contain `w_p` and its column projection would contain `z_p'`. Product-rectangle feasibility would therefore put `(w_p,z_p')` in the state. This is a promised low/high pair that disagrees on one of the first j coordinates. Under the stipulated first-mismatch rule, that pair must terminate at its first such disagreement and cannot reach the shared continuation state, contradicting the state rectangle. Hence there are at least `2^j` different states at the j-prefix frontier; taking `j=t0` proves the bound.

The proof uses the full product-rectangle condition at a merge. It does not assume that the two chosen witness pairs themselves share a common path before the merge.

## Matching universal construction and why it is not small

There is a simple first-mismatch fixed-order protocol for any disjoint `Y,Z`. At stage j create one continuation state for every prefix `p` present in both projections `pi_{P_j}(Y)` and `pi_{P_j}(Z)`. Compare the next coordinate; a mismatch goes to one of the shared signed-output leaves, and equality goes to the state for the extended prefix. Binary branching needs only a constant number of vertices per continuation state. Its size is

\[
O\!\left(N+\sum_{j=0}^{N-1}
|\pi_{P_j}(Y)\cap\pi_{P_j}(Z)|\right).
\]

For every coordinate order, C-212 shattering and the high-completion count make the j-prefix intersection contain all `2^j` patterns for `j<=t0`. Thus this profile construction, and indeed every protocol in the fixed-order scan model above, has exponential width at that frontier. This decisively kills the ordinary “evaluate the short circuit while scanning its table” DAG as a near-linear universal construction.

## Description, fingerprint, and certificate checks

### Deferred-output escape: support is easy, routing is not

Let `d_min=min_{w in Y,z in Z} dist_H(w,z)`, which C-212 bounds below by `c*s2` for a constant `c>0`. If `R` is any fixed set of fewer than `d_min` coordinates, every low/high pair still differs on `K=[N]\R`. Thus a deferred-output protocol may safely forget those R coordinates at the root and restrict all eventual output labels to K. In the OPS range choose, for example, `|R|=floor(c*s2/2)=Theta(s2)=o(N)`. This only removes a sublinear number of coordinates and leaves `N-o(N)` possible output labels; it does not give a small routing DAG.

More importantly, the set K is only a list of labels. A protocol still has to route every pair to a coordinate where it differs. The rectangles `{w:w_i=b} x {z:z_i=1-b}` cover the relation, but the union over i is not a product rectangle, and no small product-rectangle selector for the differing coordinate follows from the Hamming gap. This is the concrete escape from C-217's first-mismatch lower bound and the same support-versus-routing gap identified in C-211. No deferred-output DAG construction or lower bound has been obtained.

- **Send the short description.** Alice can send a circuit description using `O(s1 log(n+s1))` bits; Bob can then evaluate it and find a mismatch. This is a short communication protocol, not a small shared DAG. C-207/C-214 already show description-space and truth-table-space rect-DAG size are exactly invariant under `G(d)=TT(C_d)`. A near-linear description-aware DAG would itself be a near-linear sparse-envelope separator.
- **Enumerate descriptions.** Testing equality against all low truth tables and OR-ing the tests gives the explicit separator/DAG upper bound `O(N*|Y|) <= N*2^(O(s1 log(n+s1)))`. Prefix sharing improves this only to a restriction-profile DAG, which the theorem lower-bounds exponentially for every fixed scan order. It does not lower-bound other Boolean circuits or rect-DAGs.
- **Bob-selected certificates.** C-212 gives pairwise disagreement `d=Omega(s2)`. For each fixed high table z, a uniformly random t-coordinate set misses a fixed low table's disagreement set with probability at most `exp(-dt/N)`. A union bound over `|Y|` shows that z has a coordinate certificate of size `O((N/s2)*log|Y|) = O((N/s2)*s1*log(n+s1))`; at the current OPS parameters this is only `O(N)`, not a sublinear improvement. Even a smaller `Q(z)` would still need a product-rectangle-safe selector/router, so the certificate alone is not a shared DAG.
- **Binary search, hashing, recursive decomposition.** Binary search needs a state to decide whether a block contains a mismatch, a joint predicate on `(w,z)` that is generally a union of rectangles. A short fingerprint of `w` is easy to transmit after its description but has not been shown to be computable by a small shared rect-DAG against arbitrary z. Decomposing the circuit still leaves the same task of selecting a differing address. No new construction results from these variants.

## Model audit and quantitative consequence

The exact relation and adjacent models were already compared in C-214: ordinary signed mismatch is the promise-restricted Sokolov/GGKS rect-DAG relation; the native fusion cover is Cavalar–Oliveira cyclic intersection complexity; loop-circuit and AND-only models require their own transfers. The exact compiler/reverse chain remains `q=rho_prom <= O(S_rect)`, `S_rect=O(q^3/log q)`. A standard-DAG lower bound must still exceed `N^(3+3epsilon)/log N` to force `q>N^(1+epsilon)` through the known compiler.

C-217 only proves an exponential bound for the fixed-order scan subclass. General rect-DAGs are not fixed-order scanners. The `O(N)` C-80 router and `O(N log N)` C-160 separator remain mandatory counterchecks for any proposed state potential; this theorem does not conflict with either. No lower bound on unrestricted `S_rect` or `rho_prom`, no improved fusion compiler, and no P-vs-NP proof follows. O-141 remains open at global product-hull-safe state reuse and Q-output exits.

## Scope clarification

The exponential state theorem is specifically for protocols that halt immediately at the first unequal coordinate in a fixed order. The proof does not apply to a fixed-order DAG that defers output after detecting a mismatch and deliberately merges those histories; a cross-pair with a past mismatch may still have a later mismatch that such a protocol could use. It also does not apply to general adaptive or revisiting rect-DAGs. No unrestricted DAG lower bound is claimed.
