# C-215 — Q-exit overlap graphs: a local lemma, no global charge yet

Date: 27 September 2026

## Scope

Continue O-141 only. The question is whether a shared product-rectangle suffix can reuse many trace contexts by sending cross-signature pairs to Q-coordinate outputs while sending same-signature pairs to the tail. This note makes that local geometry explicit and tests whether its edge count supplies a global potential.

Let (Q\subseteq[N]), let (Y=\mathrm{SIZE}(s_1)), (Z=\{0,1\}^N\setminus\mathrm{SIZE}(s_2)), and let a rect-DAG state (v) have feasible rectangle (A_v\times B_v\). Write (P_v=K_v\cap Q) and (T_v=K_v\setminus Q), where (K_v) is the set of coordinates at descendant output leaves. For a Q-signature \(\sigma\), set (A_{v,\sigma}=A_v\cap Y_\sigma\) and (B_{v,\sigma}=B_v\cap Z_\sigma\).

## Tail-overlap graph

Make a bipartite graph (G_v) whose left vertices are signatures with nonempty (A_{v,\sigma}), whose right vertices are signatures with nonempty (B_{v,\tau}), and whose edge \((\sigma,\tau)\) is present when

\[
\pi_{T_v}(A_{v,\sigma})\cap\pi_{T_v}(B_{v,\tau})\ne\varnothing.
\]

**Lemma.** Every edge \((\sigma,\tau)\) of \(G_v\) has \(\sigma|_{P_v}\ne\tau|_{P_v}\). Consequently, (G_v) has no diagonal edge, and if (U,V) induce a complete bipartite subgraph, then \(\pi_{P_v}(U)\cap\pi_{P_v}(V)=\varnothing\).

**Proof.** Choose (w\in A_{v,\sigma}) and (z\in B_{v,\tau}) agreeing on (T_v). If they also agreed on (P_v), they would agree on every descendant output coordinate in (K_v=P_v\cup T_v), so no descendant leaf could output a valid mismatch. This contradicts correctness of the suffix at (v). The complete-bipartite consequence follows by applying the first claim to any pair with a common (P_v)-projection.

This is a useful picture of the exit/tail tradeoff: Q outputs must separate every pair of signatures whose tail projections overlap. It is a local form of C-196, not an independent DAG lower bound.

## Root calibration

At the root (B=Z). Put (k=|Q|), (t=|T_{root}|), and (M_2=|\mathrm{SIZE}(s_2)|). If (N-k-t>\log_2 M_2), then for any low row (w\in Y_\sigma), fixing (z|_Q=\sigma) and (z|_{T_{root}}=w|_{T_{root}}) leaves more than (M_2) completions. At least one completion is high, producing a diagonal edge in (G_{root}), which the lemma forbids. Hence

\[
|T_{root}|\ge N-|Q|-\log_2 M_2.
\]

This recovers the known near-full tail-support requirement. It does not count states: the same descendant outputs may be reused, and internal (B_v) can filter away the particular high completions used at the root.

## Why edge counting did not globalize

For a *fixed input pair* \((w,z)\) witnessing an edge at (v), if it follows an internal edge to child (u), it remains a tail-overlap witness there whenever it remains in the child rectangle: (T_u\subseteq T_v). This gives a pathwise persistence fact. But the graph (G_u) can also gain edges because its tail support is smaller, while Alice or Bob filtering can remove other edges. Thus \(|E(G_v)|\) is neither a conserved flow nor a monotone potential.

More fundamentally, a diagonal Q-pair is not an edge of (G_v): correctness requires its row and column tail projections to be disjoint on the suffix support. Its path cannot exit on a Q label and must eventually reach a tail mismatch. Off-diagonal pairs can share that suffix only if the suffix also routes their Q mismatch. Counting static signature edges does not price this routing. C-80's (O(N)) block router and C-160's (O(N\log N)) threshold separator remain counterchecks against summing repeated contexts or excluded-column volume.

The next useful object would have to be a **parent-conditioned flow of individual cross-history witnesses**, recording which Q-overlap edges are created or removed at each split and how their actual pairs reach Q leaves or tail suffixes. A state count would then require a bound on how much such flow one product-safe suffix can carry. No such bound is proved here; this is an organization of the missing theorem, not progress to Tier 1–3.

## Literature check: 2026 monotone-learning lifting does not yet transfer

Cavalar, de Rezende, Gray, and Santhanam's July 2026 preprint uses lifting to prove rETH-hardness of learning monotone circuits and approximating monotone circuit size from succinct examples. Its representation is a sampled labelled-example distribution. The present C-75 target is a Boolean separator circuit on a complete (N)-bit truth table with arbitrary medium-band behavior. A direct reduction would need to map consistent examples to low truth tables and the hard case to high truth tables while preserving every signed mismatch output. A succinct sample generator itself gives a small circuit for its output table, so it cannot serve as a high image in the OPS parameter range without an additional, size-controlled encoding. The paper supplies a possible block-summary/lifting technique source, but no C-75 DAG or fusion lower bound follows from its conditional algorithmic hardness.

Primary source: [Cavalar, de Rezende, Gray, and Santhanam, *ETH-Hardness of Learning Monotone Circuits and Approximating Their Size* (arXiv:2607.12331)](https://arxiv.org/abs/2607.12331).

## Disposition

The graph lemma restates and packages C-196's local constraint; it does not close O-141. Static edge counts, local support, and raw exclusion volumes still do not aggregate through arbitrary alternating DAG states. The project target and transfer loss are unchanged: a standard rect-DAG lower bound must exceed \(N^{3+3\epsilon}/\log N\) under the current \(q\to S_{rect}=O(q^3/\log q)\) compiler to imply \(\rho_{prom}>N^{1+\epsilon}\). No superlinear actual-promise DAG/cover bound or P-vs-NP proof is established.
