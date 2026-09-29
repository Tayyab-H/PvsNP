# C-378 - Policy splicing is sound exactly when the hybrid remains well-founded

Date: 29 September 2026  
Route: turn C-377's per-input positional strategies into a state-sharing invariant by hybridizing their actions across anchors.  
Classification: **EXACT ACYCLIC-HYBRID LEMMA + TWO-STATE OBSTRUCTION; NO q IMPROVEMENT.**

## 1. Exact hybrid-policy lemma

Fix the C-319 transition graph and an empty-consequence root. A policy pi is an action assignment on the state-side pairs reached from that root. It is valid on its reachable part when every action selects either one true signed-literal seed, a constant-true seed, or an allowed predecessor. Let G_pi be the directed graph of selected predecessor actions reachable from the root.

If G_pi is acyclic and every selected nonconstant seed literal is true on a table u, then the root is active on u. Proof is backward induction in a topological order of G_pi: each state-side obligation is discharged by its selected predecessor, selected literal, or constant seed. Therefore the cube C_pi defined by its selected literals is wholly accepted. For a valid cover, soundness implies C_pi subset SIZE(s2).

Consequently, if pi_f and pi_g are winning policies on two low tables, a state-by-state hybrid tau of their actions is also a sound policy cube provided it remains valid on every root-reachable state-side pair and its root-reachable predecessor graph is acyclic. This is the exact point at which policy reuse could turn into a C-281-style cross-anchor splice.

## 2. Why acyclicity cannot be dropped

Consider the two-state recurrence

    x1 = (a OR x2) AND b
    x2 = c AND (d OR x1).

On f=(a,b,c,d)=(0,1,1,1), a winning policy from state 1 uses 1-E -> 2, the b seed at 1-H, and seeds c,d at state 2. Its reachable policy graph is acyclic.

On g=(1,1,1,0), a winning policy uses seeds a,b at state 1, seed c at state 2-E, and 2-H -> 1. This policy is also acyclic.

Hybrid the first policy's 1-E action with the second policy's 2-H action, retaining the b and c seed exits. The hybrid has the reachable cycle 1 -> 2 -> 1. The table u=(0,1,1,0) satisfies both selected seed literals b=c=1, but the least fixed point on u is x1=x2=0: the cycle has no seed base. Thus compatible selected literals alone do not imply acceptance. The hybrid's cyclic dependency is the obstruction.

This is an example at the recurrence-game level; this report does not claim that this exact four-seed recurrence has already been realized by legal fusion endpoints. Legal endpoint systems do exhibit input-dependent rank reversals and successful cyclic covers (C-141/C-142), so the well-foundedness issue is native to the project, not an artifact of the example.

## 3. A more precise state-sensitive target

Choose a winning positional policy and an empty root for each low anchor, then partition the anchors by their selected root. For a fixed root r and its policy family Pi_r, define the valid acyclic hybrid closure to consist of policies formed by choosing, independently at each state-side slot, an action appearing in a policy from Pi_r, and retaining only hybrids that are valid on every reachable slot and whose root-reachable predecessor graph is acyclic. Every such hybrid must define a cube contained in SIZE(s2).

The desired lower-bound theorem would show that a q-state transition graph cannot cover all low anchors across its at most q root classes while keeping every valid acyclic hybrid cube sound unless q is superlinear. Equivalently, prove that small q forces, within one root class, an acyclic cross-anchor hybrid whose cube has a high completion. This is more precise than counting policies or splicing supports alone: cyclic hybrids are not witnesses.

No quantitative bound on this acyclic hybrid closure is proved here. The project remains at q >= N-o(N). In particular, this does not construct a full-promise near-linear cover or prove a P-vs-NP separation.

## 4. Mandatory calibration

- C-258 equality: hybrid policies that mix repeated local patterns can remain low, so not every acyclic hybrid can be forced high.
- C-257 parity: the invariant must permit linear-size affine synchronization.
- C-281: support-level context/proof unions are useful only when they correspond to an acyclic policy hybrid.
- C-141/C-142: activation order can reverse across anchors, so no input-independent rank may be assumed without proof.

The next step is to characterize which cross-anchor action hybrids are acyclic in an arbitrary fixed C-319 graph, then test whether the low-circuit promise forces a high cube among them. This remains an open obligation, not a positive q result.
