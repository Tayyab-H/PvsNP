# C-385 - Monotone seed order isolates the readout cost

Date: 29 September 2026  
Route: sharpen C-342/C-363 by characterizing exactly what seed signatures alone can separate.  
Classification: **EXACT ORDER-SEPARATION THEOREM / LINEAR SEED-CHANNEL CEILING; NO q IMPROVEMENT.**

## 1. Setup

For a fixed C-319 list Q with q pairs, write

```text
sigma_Q(w) = (A_1(w), B_1(w), ..., A_q(w), B_q(w)) in {0,1}^{2q}.
```

The two features at state i are the seed predicates in its paired recurrence. Each is an OR of a fixed consistent collection of signed table literals, or a constant. Once sigma is fixed, iterate the fixed transition map from zero. Since every operation in the recurrence is monotone in the seed bits, there is a monotone Boolean function G_Q such that

```text
Accept_Q(w) = G_Q(sigma_Q(w)).
```

Let L=SIZE(s1) be the required accepting set and H={w: CC(w)>s2} the required rejecting set. Medium tables are unconstrained.

## 2. Exact monotone-order criterion

**Theorem.** For a fixed feature map sigma, some monotone Boolean decoder G separates L from H if and only if

```text
for every l in L and h in H, sigma(l) is not coordinatewise <= sigma(h).
```

Equivalently, every low/high pair must have a seed coordinate j with

```text
sigma_j(l)=1 and sigma_j(h)=0.
```

**Proof.** Necessity follows from monotonicity: if sigma(l)<=sigma(h), then G(sigma(h))>=G(sigma(l))=1, contradicting rejection of h. Conversely, if there is no such ordered pair, define

```text
G*(u)=1 iff there exists l in L with sigma(l)<=u.
```

This is monotone, accepts every sigma(l), and rejects every sigma(h) by the assumed condition. This converse is only about an unrestricted monotone decoder; it does not assert that G* is realizable by the q-state C-319 recurrence.

The pairwise form says that the rectangles

```text
{l in L: sigma_j(l)=1} x {h in H: sigma_j(h)=0}
```

for j=1,...,2q must cover L x H. It is a useful exact reduction of all seed-only arguments to a structured rectangle cover.

## 3. Why the seed-order condition stops at the linear scale

For each coordinate a and bit b, let lambda_(a,b)(w)=1 exactly when w_a=b. If l and h are distinct tables, choose a coordinate a where they differ and set b=l_a. Then

```text
lambda_(a,b)(l)=1,   lambda_(a,b)(h)=0.
```

Thus the 2N signed singleton features satisfy the order criterion for **every** disjoint low/high promise, independent of circuit complexity. They can be grouped as N pairs of opposite singleton endpoints; on input w, the corresponding seed pair is (NOT w_a, w_a). This is an input-distinguishing feature bank, not an accepting cover. In the actual endpoint realization every T_i is empty, so all q states are roots and each is a predecessor of every state. Since each seed conjunction is (NOT w_a) AND w_a=0, the all-zero activation vector remains the least fixed point. C-363 separately establishes that an O(N)-slot C-319 seed signature can be injective on all tables.

Consequently, none of the following alone can prove q=omega(N): counting signature fibers, proving seed-signature injectivity is necessary, forbidding low-signature <= high-signature pairs, or counting rectangles contributed by individual seed predicates. The full signed-literal bank satisfies all those tests with 2N features. A successful lower bound must use the transition graph's inability (or cost) to decode and combine the features, not merely their information or order-separation power.

## 4. Remaining computational resource

The recurrence readout is more restricted than an arbitrary monotone decoder. It has q state variables, fixed predecessor sets, and q least-fixed-point rounds. Unrolling those rounds creates O(q^2) unbounded-fan-in monotone gates, in addition to the 2q seed ORs over signed table literals. This gives the familiar q-to-circuit upper compilation but no lower bound. Any use of circuit lower bounds must account for the fact that Q chooses an extension on medium tables; a lower bound for exact MCSP membership alone need not apply to every extension of the Gap-MCSP promise.

The literature check found unconditional MCSP lower bounds in restricted classes such as AC0[p], not a lower bound for this arbitrary paired least-fixed-point readout. For example, Golovnev, Ilango, Impagliazzo, Kabanets, Kolokolova, and Tal prove an AC0[p] lower bound for MCSP; it supplies no transfer to unrestricted C-319 graphs or arbitrary promise extensions ([ECCC TR19-018](https://eccc.weizmann.ac.il/report/2019/018/)).

## 5. Checkpoint and next obligation

- The seed signature has an exact cross-order characterization: **proved**.
- Seed information/order separation alone can force a superlinear q bound: **no; universal 2N-feature bank rules this out**.
- A superlinear lower bound for the coupled C-319 readout, or a full-promise q=N^(1+o(1)) cover: **not obtained**.
- Current native lower bound: `rho_GapMCSP >= N-o(N)`.
- P vs NP: **unresolved**.

Continue O-228 at the recurrence/readout level. A useful next result must either give a graph-sensitive lower bound on monotone fixed-point readout for the actual OPS promise, handling arbitrary seed clauses and unconstrained medium values, or explicitly construct the promised near-linear full cover. Do not reopen raw signature, fiber, policy-count, or fixed-circuit selector arguments.

## 6. Exact reachability-game form correspondence

The recurrence also has a direct game realization. For each rule i make a universal node u_i with two moves, to existential side nodes e_i and h_i. From e_i, the existential player may move to any predecessor j in P_i^E, or to an input terminal labelled A_i. From h_i, the choices are predecessors in P_i^H or the terminal labelled B_i. A true seed terminal goes to a winning sink; a false seed terminal goes to a losing sink. Infinite play is losing for the existential player. Add an existential start node whose choices are exactly the empty-consequence roots.

The attractor (least reachability winning region) obeys

```text
win(i) = (A_i OR OR_{j in P_i^E} win(j))
         AND
         (B_i OR OR_{j in P_i^H} win(j)),
```

so it is exactly the C-319 least fixed point, including the rule that cycles without a true seed do not win. This graph has O(q) vertices and O(q^2) possible predecessor edges. The input enters only through the 2q terminal outcomes, each of which in C-319 is itself an OR of signed truth-table literals.

This identifies C-319 as a particularly structured reachability graph-game form followed by a seed substitution. Pauly proves that graph-game forms define monotone Boolean functions and are closed under least fixed points, and explicitly asks how large monotone circuits for these fixed-point functions must be. The correspondence locates our generic readout question in that framework, but does not import a lower bound: the relevant instance additionally has paired universal obligations, arbitrary endpoint-induced predecessor incidence, and seed terminals constrained to be signed-literal ORs. Our direct q-round unrolling gives the project-standard O(q^2) monotone-gate upper bound; the missing result remains an OPS-specific lower bound or a full-promise small game form ([Pauly, *Parameterized Games and Parameterized Automata*, Theorem 8, Proposition 10, Open Question 11](https://arxiv.org/abs/1809.03093)).

**Scope check.** The game correspondence is exact for a fixed Q; it is not a reduction from arbitrary monotone games to Gap-MCSP. The 2N signed-literal bank from Section 3 satisfies only the seed-order condition. It does not provide the fixed game form that reads the bank correctly.

### Endpoint-realizability caveat

The translation is one-way for research purposes: every endpoint list Q yields the game form above, but it has not been shown that every abstract choice of the predecessor sets and seed clauses can be realized by endpoints. In the native model, the edge `j -> i` means `T_j subseteq E_i` or `T_j subseteq H_i`, while the seed bits are determined by which complete literal slices lie in those same endpoints; these incidences are coupled. Also `T_i subseteq E_i,H_i` forces a self-loop on both sides at every state. Such self-loops do not change the least fixed point from zero: before x_i first activates, its self-loop contributes zero, and after activation monotonicity keeps it active. A lower bound for the relaxed game-form class would transfer to C-319; an upper construction in that relaxed class would not transfer without an endpoint-realization proof.

