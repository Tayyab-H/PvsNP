# C-353 - Overlap fingerprints reduce the live question to ownership complexity

Date: 29 September 2026  
Route: combine C-234's repeated-block splice calculation with C-245's marked antichains and C-260's blocker dual.  
Classification: **EXACT DIAGONAL SUBPROMISE LEMMA + FRONTIER CORRECTION; NO q IMPROVEMENT.**

## 1. Do not rederive the support grammar

The support-generation recurrences already exist. C-245 computes proof antichains `P_i` and one-hole context antichains `K_i` from the same q-rule grammar; its bounded context recurrence is exact for the state zone. C-260 adds the absent-feature blocker antichains and the compatible context/proof convolution. C-251 shows why counting ranked proof-DAG descriptions does not charge q: at `q=Theta(N)` the signature count is `exp(O(N log N))`, larger than every candidate low-anchor family recorded here.

Therefore the unresolved step is not to define another support family. It is to assign a quantity to their **jointly generated overlap, ownership, and blocker incidence** that has a q-sensitive composition law.

## 2. Exact overlap test on repeated-block anchors

Use C-234's diagonal family. Let addresses be `(p,u)`, where p ranges over r prefix blocks and u ranges over the `2^k` suffixes. For each Boolean function g on k bits, define

```text
w_g(p,u) = g(u).
```

Take a context support K matched by `w_g` and a replacement proof support C matched by `w_h`. Write `dom(S)` for the coordinates mentioned by support S, and define

```text
Omega(K,C) = {u : for some p, (p,u) is in dom(K) intersect dom(C)}.
```

Then the following equivalence is exact:

```text
K union C is consistent
    iff
g(u) = h(u) for every u in Omega(K,C).
```

If g and h differ at a suffix u represented in both domains, some repeated coordinate `(p,u)` carries opposite literals. Conversely, if they agree on every such suffix, all overlaps have the same sign, and nonoverlapping coordinates cannot conflict. This recovers C-234's equation (36) directly in the C-245 support-language notation.

Thus the overlap set is a description fingerprint: `Omega={0,1}^k` permits only `g=h`, whereas a smaller Omega permits cross-description compatibility exactly when the descriptions agree on Omega.

## 3. Exact safe-ownership calibration

For a compatible pair `(K,C)`, form its canonical completion by taking the C sign on coordinates mentioned only by C, and the K sign elsewhere (including free coordinates). On suffixes in Omega, g=h, so the completion is independent of this tie convention.

Suppose, for each suffix u, the resulting bit is constant across all prefix blocks p. Then the whole hybrid has the form

```text
z(p,u) = f(u)
```

for some k-bit Boolean function f. Under C-234's choice of k, Lupanov synthesis gives `CC(z) <= B*2^k/k <= s1/4`; the splice is low. Thus ownership constant across prefix blocks on every suffix is a sufficient condition for a low splice. A non-diagonal splice can vary only on suffixes where `g(u) != h(u)` and `u` lies outside Omega. Prefix-dependent ownership there is necessary for a non-diagonal splice, but not sufficient for a high splice: a few varying coordinates may still be computable within s2.

This separates the mechanisms cleanly:

1. **Fingerprint:** overlap forbids cross-splicing descriptions that disagree on Omega.
2. **Ownership:** outside Omega, the owner pattern decides whether the hybrid stays diagonal.
3. **High-side condition:** prefix variation must occur on a suffix where g and h differ outside Omega, and the resulting hybrid must be complex enough to exceed s2 before it contradicts soundness.

No one of these three quantities alone charges the state grammar.

## 4. Why the conditional product proof does not give a lower bound

C-234 shows that block-isolated replacement contexts would expose independent choices across the r prefix blocks and force `q >= 2^(Omega(s2))`. The hypothesis is not automatic. The restricted diagonal family itself has an O(N)-pair native equality cover (C-258); C-326 computes its exact separator as

```text
AND_(j=1,...,d) ( OR_(a in {0,1}) AND_(t=1,...,r) [w_(j,t)=a] ).
```

For a diagonal anchor `w_g(j,t)=g(j)`, the accepting proof chooses `a=g(j)` in each block, and the inner conjunction contributes every literal `(j,t,g(j))`. Their union is exactly `ell(w_g)`. If `g!=h`, these full supports conflict at every repeated coordinate where the functions differ. Thus the C-258 native list of `2N+2d-1` rules realizes the complete, pairwise-incompatible menu from C-352 on this subpromise. A correct general argument must account for the nonlocal overlap/ownership patterns used by this grammar; it cannot assume that a chosen proof assigns each prefix block to a separate state occurrence.

The full low class creates the additional difficulty: its tables need not share one repeated-block description. Any useful q-charge must prove that extending the equality fingerprint from this diagonal family to all size-s1 circuits requires superlinear rule cost, or must construct a full-promise near-linear grammar.

## 5. Corrected continuation target

The project already has:

- exact proof/context antichains and context substitution (C-245, C-281);
- exact certificate/blocker duality (C-260);
- a conditional block-product lower bound plus a counterexample to automatic isolation (C-234);
- a root-signature count showing why raw description counts stop short (C-251);
- the C-351 compatible-replacement projection bound and C-352's same-hole quantifier correction.

The next mathematical target is a **composition potential** for the q-rule-generated relation of `(state, context, proof, overlap fingerprint, ownership profile, high blocker)`. It must distinguish the all-low-circuits promise from the diagonal equality subpromise, charge nonlocal mixing rather than proof occurrences, and remain O(N) on parity, repeated equality, and local-constraint calibrations. A raw count or a restatement of the antichain grammar does not meet this target.

Checkpoint: actual Gap-MCSP lower bound remains `N-o(N)`; no near-linear full-promise cover, superlinear synchronization theorem, positive CohEnc transfer, reconstruction compiler, or P-vs-NP proof has been obtained.
