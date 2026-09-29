# C-382 - Projection-aware entropy cap for all safe splice products

Date: 29 September 2026  
Route: Strengthen C-381 from selected positional policies to every C-281-compatible context/proof product.  
Classification: **EXACT SAFE-PATTERN CAP + SPLIT-INDEPENDENCE NO-GO.**

## 1. Owner patterns live only on the disagreement set

Fix two distinct low anchors f,g from a code family F, and let

    D(f,g) = {a in [N] : f[a] != g[a]},
    d_fg = |D(f,g)|.

An owner pattern u in {0,1}^{D(f,g)} determines one splice h_(f,g,u): on D it chooses f or g according to u, and outside D the anchors agree. The map

    u -> h_(f,g,u)

is injective: a change to u at any address in D changes the resulting table at that address.

Now take *any* C-281-compatible context K and replacement proof P at a shared state, where K matches f and P matches g. Their support union is an accepting support, so every completion is in SIZE(s2). Its canonical owner splice is therefore in SIZE(s2). Consequently, for this fixed pair, the set of owner patterns arising from all compatible context/proof products, across all states and all proof trees, has size at most

    |SIZE(s2)| <= 2^{O(s2 log(s2+n))}.

This bound does not count or enumerate policies. It follows from soundness plus injectivity of the owner map. The same cap applies to the consistent acyclic hybrids in C-380.

## 2. A random split avoids every safe product pattern

Let P be uniform in {0,1}^N. For a fixed owner pattern u on D, consider all full masks mu extending u. Every such mask induces the same splice, because f=g outside D. There exists an extension within radius r of P exactly when dist(P|D,u)<=r: choose mu=P outside D. The analogous statement holds for the complement of P. This is an event about an arbitrary owner-mask extension, not a claim that an endpoint product realizes that extension. It is the right event because C-320's robustness excludes every full mask near P or its complement.

    Pr[dist(P|D,u) <= r or dist(P|D,1-u) <= r]
       <= 2 * 2^(-d_fg) * sum_(j=0)^r binom(d_fg,j)
       <= 2^(-d_fg + 1 + d_fg H_2(r/d_fg)).

Consequently the probability that some full owner-mask extension of u is in either forbidden ball is exactly controlled by this projection count.

There are at most |F|^2 |SIZE(s2)| pair-patterns across all ordered anchor pairs. If d_fg >= d = Omega(N), log|F|=O(N^beta), and r=Theta(N^gamma/n) for fixed beta<gamma<1, then

    log(|F|^2 |SIZE(s2)|) = O(N^beta*n) = o(N),
    d_fg H_2(r/d_fg) = O(N^gamma) = o(N).

A union bound gives

    Pr[P is near any safe pair-pattern or its complement]
       <= 2^(-d + O(N^beta*n + N^gamma))
       = 2^(-Omega(N)).

Thus almost every split avoids the radius-r projection-neighborhood of *every* owner pattern that any compatible product can produce on F. This is stronger than C-381's bound for one representative path per anchor: it covers the entire endpoint-realizable compatible-product family without counting policies.

C-320 independently says that almost every split is robust: all off-diagonal splices within radius r of P or its complement have circuit complexity above s2. A robust split must avoid every safe product pattern, since a nearby extension would be both a C-281-accepted low table and C-320-high. The two high-probability properties are consistent; no contradiction is forced.

## 3. What the cap closes

This closes the split-independent forcing version of O-227. A random/global split cannot be used to prove that some compatible product enters the forbidden balls: the set of all such products already maps into the low-table class, and that class has only 2^{o(N)} members per anchor pair. The obstruction is not merely too few selected policies.

The logic boundary is exact:

- A compatible context/proof product is sound by C-281, so its splice is low.
- C-320's robust split makes nearby splices high.
- Therefore every compatible product must avoid the robust balls.
- To get a contradiction, one must first prove that a *specific endpoint-generated product* has a high splice and then prove that the same context and proof are compatible. The high-complexity claim cannot be obtained by hoping a split-independent random mask intersects the already-safe product family.

A surviving theorem must correlate the owner mask with the actual endpoint-generated supports, rather than choose a mask independently and try to find it in a small family of safe products. It may instead exploit an input-dependent split, a direct algebraic invariant of the support grammar, or a full-promise near-linear construction.

## 4. Checkpoint

- C-381 representative-policy avoidance: strengthened to all C-281-compatible products on F.
- Owner-pattern count per anchor pair: at most |SIZE(s2)|, proved.
- P-dependent full-mask extensions on common coordinates: these do not change the splice, and C-320 robustifies against every such mask. The projection-neighborhood count is therefore the exact probability for existence of a forbidden-ball extension.
- Native lower bound: unchanged at q >= N-o(N).
- No superlinear q bound, full-promise near-linear cover, or P-vs-NP proof.

Full context: C-281's cylinder substitution law, C-320's robust split, and C-381's policy-path analysis.
