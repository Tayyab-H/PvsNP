# C-380 - Same-root winning policies have an acyclic switching path

Date: 29 September 2026  
Route: sharpen C-378 by asking whether cycles can disconnect the positional policies needed by a valid cover.  
Classification: **EXACT ACYCLIC RECONFIGURATION LEMMA + LINEAR PAIRWISE CEILING.**

## 1. Extend two policies to a common state set

Fix a C-319 graph and one empty-consequence root r. Let pi and sigma be winning positional policies for two low tables f and g, both rooted at r. Let R_pi and R_sigma be the states reachable from r when the universal player ranges over both sides and the existential policy is fixed. Each reachable predecessor graph is acyclic, since a reachable cycle would let the universal player avoid every seed forever.

Put U=R_pi union R_sigma. Extend pi on R_sigma minus R_pi using sigma's actions, and extend sigma on R_pi minus R_sigma using pi's actions. Keep each policy's original actions on its own reachable set. These extensions do not change their root behavior. Their full predecessor graphs on U are acyclic: edges from R_pi stay in R_pi, edges from R_sigma minus R_pi follow sigma within R_sigma, and any cross edges point into R_pi intersection R_sigma, with no return edge from that intersection to the sigma-only region. The symmetric argument applies to the extended sigma policy. All chosen actions are legal native actions, and U is closed under either policy's transitions.

## 2. Acyclic policies are connected by single-slot switches

Let pi-hat and sigma-hat be the two extended policies, viewed as action tables on the 2|U| state-side slots. Choose a topological rank r(i) for the sigma-hat predecessor graph such that every predecessor edge i -> j has r(j)<r(i).

Starting from pi-hat, process states in increasing r(i). At each state, switch its two side actions, one at a time, to the corresponding sigma-hat actions. A switch to a seed adds no graph edge. A switch to a predecessor j cannot create a cycle: if it did, there would be a path j -> i in the current graph. Since r(j)<r(i), that path must contain a first edge u -> v with r(v)>=r(u). All earlier edges strictly decrease rank, so r(u)<r(i); state u has already been switched to sigma-hat, whose edges all decrease rank. Contradiction.

Thus the policies are connected by a path of at most 2|U|<=2q **structurally legal hybrids whose full predecessor graphs remain acyclic**. This does not contradict C-378: arbitrary hybrids can cycle, but there is always a carefully ordered acyclic route between two policies with the same root.

## 3. The remaining obstruction is literal consistency

For an intermediate hybrid tau, collect its selected nonconstant seed literals into L_tau. If these literals are consistent, their satisfying cube makes the same root policy win; cover soundness therefore forces that cube to lie inside SIZE(s2) and fix at least N-h coordinates, where h=log2|SIZE(s2)|. If L_tau contains opposite literals on a coordinate, its cube is empty and the policy yields no accepted table. The acyclic switching theorem alone does not prevent such inconsistent intervals.

This narrows the cross-anchor splice problem: cycles need not block every path, but the path may pass through empty literal cubes. The next target is to understand whether a switch path can be chosen so that some middle hybrid is consistent and has a high completion, or to bound the number and structure of the inconsistency barriers using the fixed seed clauses.

## 4. Pairwise action distance cannot exceed a linear charge

Suppose dist(f,g)=d. Each policy cube fixes at least N-h coordinates, so among the d coordinates where f and g differ, at least d-2h are fixed by both policies. On each such coordinate the policies select opposite seed literals, and therefore their action tables differ in at least one slot. One changed slot can account for at most two coordinates (its old and new literal labels), so the two action tables differ in at least (d-2h)/2 slots.

Since d<=N, this yields at most a linear-scale pairwise charge, and for the Reed-Muller family in C-379 the distance is sublinear. It cannot prove q=omega(N). Any superlinear result must use multi-anchor path compatibility or a full-promise construction, not pairwise policy distance.

## 5. Checkpoint

- Any two same-root winning policies admit a structurally legal acyclic switching path: proved.
- Every consistent intermediate policy cube is sound and fixes N-h coordinates: proved.
- The path can pass through inconsistent literal sets; no high completion is forced: unresolved.
- Pairwise action distance yields no superlinear q bound.

The native lower bound remains q>=N-o(N). No full-promise near-linear cover or P-vs-NP proof follows.
