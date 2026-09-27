# C-233 — Min–max activation ranks, event-driven closure, and the TSC boundary

Date: 27 September 2026  
Scope: continue the C-75 shared-state route. Test whether the cyclic fusion closure's input-dependent activation order can be evaluated by a worklist, and whether that gives a better *standard acyclic* DAG compiler. The proved result is a project-specific operational characterization and a transfer to tri-state circuits (TSCs); I make no claim that the underlying Dijkstra-style algorithm is new in the literature. It does not improve the standard rect-DAG bound or separate P from NP.

## 1. The exact rule system

Fix a proposed q-pair list Q and an anchor table u∈{0,1}^N. Write its least-fixed-point equations as

\[
x_i^{t+1}(u)=\left(a_i(u)\vee\bigvee_{j\in P_i}x_j^t(u)\right)
\wedge
\left(b_i(u)\vee\bigvee_{j\in R_i}x_j^t(u)\right),\qquad x^0=0,
\]

where P_i and R_i are the two support sets induced by carrier containment and a_i,b_i are the two literal-seed clauses. The sequence is increasing, and every coordinate can change from 0 to 1 only once. Let τ_i(u) be its first activation round, or ∞ if i never activates.

## 2. Min–max rank equation

For any rank vector τ, define

\[
L_i=\min\bigl((\{0\}\text{ if }a_i(u)=1)\cup\{\tau_j:j\in P_i\}\bigr),\qquad
R_i'=\min\bigl((\{0\}\text{ if }b_i(u)=1)\cup\{\tau_j:j\in R_i\}\bigr),
\]

with the minimum of an empty set equal to ∞. Then the least activation ranks satisfy

\[
\tau_i=1+\max(L_i,R_i')
\]

when both sides are finite, and τ_i=∞ otherwise. This is a least-solution equation: self-support cannot create a finite rank, since every finite derivation must use supports already active at a strictly earlier round.

**Proof.** If i first activates at round t, each side of its conjunction has a seed or a predecessor active by round t−1, so L_i,R_i'≤t−1 and the candidate rank is at most t. Conversely, if both side minima are finite and at most r, their witnessing seeds/predecessors are active by round r; therefore i is active by round r+1. Taking the least finite derivation rank gives equality. This is the standard AND/OR proof-height recurrence, written as a min–max relaxation equation.

## 3. A settled-state worklist algorithm

The ranks can be computed with a Dijkstra-style priority queue.

1. Initialize L_i to 0 when a_i(u)=1 and to ∞ otherwise; initialize R_i' analogously.
2. Whenever both minima for i become finite, set its tentative key to 1+max(L_i,R_i') and insert/decrease that key in a min-heap.
3. Pop the least tentative key τ_i. Finalize i at that rank. For each outgoing support arc from i, lower the corresponding L or R' minimum of its target to τ_i and update that target's key if both sides are now finite.
4. Stop when the heap is empty. The empty-carrier rules that were finalized are exactly those activated by the least closure.

The invariant is that each tentative key is the height of an actual finite proof tree, hence is not below the true activation rank. When the least key t is popped, any not-yet-finalized predecessor has rank at least t; because a target's activation rank is one plus the maximum of its two side minima, such a predecessor cannot later lower the popped key. Induction on popped keys proves that every finite τ_i is finalized at its exact rank. Each rule is finalized once and each support incidence is processed once.

Let E=Σ_i(|P_i|+|R_i|)≤2q². Computing all seed clauses by scanning their at most 2N literals costs O(qN). The worklist then takes O((q+E)log(q+1)) word-RAM operations with a binary heap. Successful OPS covers already satisfy q≥N−o(N), so the full evaluation takes O(q² polylog q) RAM time. The proof is uniform in the seed bits and works for cyclic support graphs; it does not assume a global topological order.

## 4. What this says about DAG size—and what it does not

The worklist is a per-input algorithm, not a standard Boolean circuit. Its queue, heap, and memory addresses depend on u. Replacing those accesses by ordinary fan-in-two circuitry is precisely where the RAM time bound can expand. In particular, the worklist does **not** establish an O(q² polylog q) rect-DAG or Boolean-separator circuit. The already proved standard compiler remains

\[
S_{\rm rect}=O(q^3/\log q),
\]

and the q² acyclic-intersection statement still counts AND gates while leaving OR/support routing uncharged. Thus the desired O-152 inequality and its N^(3+3ε)/log N threshold are unchanged.

The boundary is real in the literature: Heath–Kolesnikov–Ostrovsky's TSC model allows cycles and input-dependent gate firing and simulates a T-step RAM with O(T log^3T loglogT) gates; they explicitly contrast this with ordinary Boolean-circuit RAM simulation, which scans memory on accesses. Applying that theorem to the worklist gives a **tri-state**, not standard Boolean, total separator of size q² polylog q. If S_TSC(Y,Z) denotes minimum total tri-state-circuit size of a Boolean separator, then

\[
S_{\rm TSC}(Y,Z)\le O(q^2\operatorname{polylog}q).
\]

Consequently, a lower bound S_TSC>N^(2+2ε+δ) for any fixed δ>0 would imply q>N^(1+ε) for all sufficiently large N (the polylog is absorbed by N^δ). A bound with no exponent slack must explicitly dominate the simulator's polylogarithmic loss. No such total-separator TSC lower bound is known here.

This does not provide a reverse reduction from arbitrary TSCs to fusion covers. TSCs can emulate RAM programs, while fusion rules have the much narrower carrier-containment incidence syntax. Nor does TSC size lower-bound rect-DAG size by itself: TSCs are more expressive than acyclic Boolean circuits. This is a candidate lower-bound model with a better q-side upper transfer, not an OPS-specific lower bound.

## 5. Explicit positive-signal network and its limitation

There is also a direct cyclic signal-flow representation of the positive least closure. Encode “active” by signal 1 and “not yet active” by Z. Convert each true input literal to a 1-signal with a controlled buffer; false literals produce no signal. Join gates implement each side OR. A buffer controlled by the first side and carrying the second side implements the conjunction: it emits 1 exactly when both sides have received a signal. Wire each rule output back to its support joins. Starting with internal wires Z, this asynchronous network activates exactly the least fixed point, independent of notification order.

Define S_TSC^+(Y,Z) as the minimum number of TSC gates in a recognizer whose output is 1 on every w∈Y and remains Z on every z∈Z; behavior on the medium band is unrestricted. The network is an O(qN+E)=O(q²)-gate S_TSC^+ recognizer, counting every seed/support incidence. On nonaccepting inputs its output remains Z, so it is not a total Boolean separator. The terminating worklist/TSC simulation above supplies the separate total 0/1 separator.

This partial-recognizer variant gives the sharper conditional transfer: if S_TSC^+(Y,Z)>N^(2+2ε+δ) for fixed δ>0, then q>N^(1+ε) for all sufficiently large N. Indeed, q≤N^(1+ε) would give S_TSC^+≤Cq²≤CN^(2+2ε), contradicting that lower bound. No such lower bound is known. The measure allows undefined output on NO instances, which makes it more expressive than ordinary Boolean separators and makes the lower-bound problem at least as demanding; it is a target definition, not a result.

## 6. Comparison with the active C-75 models

| Model | What it counts | C-75 relation | Quantitative result |
|---|---|---|---|
| Standard Sokolov/GGKS rect-DAG | Acyclic product-rectangle states | Exactly the promise mismatch relation; size Θ(separator-circuit size) | q-cover → O(q³/log q) states; lower bound threshold remains N^(3+3ε)/log N |
| Cavalar–Oliveira cyclic intersection / fusion | Least-fixed-point intersections; unions are free | Exact identity q=ρ_prom=D°_∩ for the promise model | q states but support expansion prevents counting them as an acyclic DAG |
| TSC | Fan-in-two XOR/buffer/join gates, cyclic graph, tri-state signals and input-dependent firing | Activation is a one-sided partial recognizer; a terminating worklist gives a total separator | q-cover → O(q²) partial recognizer or O(q² polylog q) total separator; no reverse or TSC lower bound |

The useful new distinction is between (i) the number of rule activations, which is at most q, (ii) the support-incidence work E, which is at most 2q², and (iii) the circuit area needed to compile input-dependent queue accesses. The min–max rank system exposes the first two exactly; standard DAG lower bounds must still confront the third.

## 7. Disposition and next test

**Positive result:** the native closure has a precise min–max activation-rank characterization, a Dijkstra-style O(q² polylog q) RAM evaluator, and a direct O(q²)-gate TSC partial recognizer. The latter yields a lower-bound target with only quadratic q-loss if one can prove a sufficiently strong TSC partial-recognizer bound.

**Failed implication:** RAM work is not Boolean-circuit size. No O(q² polylog q) acyclic product-rectangle DAG follows, so the principal O-152 target is not improved.

**Next test:** seek an explicit *oblivious* implementation of the closure worklist whose ordinary circuit area is O(q² polylog q), or prove that the carrier-support graph admits a special static routing network with that area. Any such compiler must handle dynamic priority/order without assuming the input-dependent ranks are a global topological order; C-141's rank-reversing SCC remains the counterexample. If no such compiler emerges, treat TSC lower bounds as a separate model rather than importing them into O-152.

### Primary source

- David Heath, Vladimir Kolesnikov, and Rafail Ostrovsky, [*Tri-State Circuits: A Circuit Model that Captures RAM* (ECCC TR23-095)](https://eccc.weizmann.ac.il/report/2023/095/). The report defines 0/1/Z wires, XOR/buffer/join gates, eager input-dependent firing, and an O(T log^3T loglogT)-gate simulation of T RAM steps.
