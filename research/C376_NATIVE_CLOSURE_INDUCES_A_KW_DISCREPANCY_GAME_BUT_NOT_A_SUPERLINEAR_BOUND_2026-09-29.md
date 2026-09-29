# C-376 - Native closure induces a paired discrepancy game, but mismatch alone is too weak

Date: 29 September 2026  
Route: convert the C-319 least-fixed-point proof into a low/high Karchmer-Wigderson style search game and test whether its state count can charge q.  
Classification: **EXACT q-STATE GAME LEMMA + REPRESENTATION AUDIT; NO q IMPROVEMENT.**

## 1. The paired discrepancy game

Fix a valid q-pair C-319 cover. Write (x_i^{(t)}(u)) for its activation of state i on table u after t closure rounds, and (x_i(u)) for the least-fixed-point value. Let

\[
L=\mathrm{SIZE}(s_1),\qquad H=\{z:\mathrm{CC}(z)>s_2\}.
\]

For each state define its two obligation disjunctions at the fixed point:

\[
D_i^E(u)=A_i(u)\vee\bigvee_{j\in P_i^E}x_j(u),\qquad
D_i^H(u)=B_i(u)\vee\bigvee_{j\in P_i^H}x_j(u).
\]

Then \(x_i(u)=D_i^E(u)\wedge D_i^H(u)\). A live pair is a state i with \(x_i(w)=1\) and \(x_i(z)=0\), for \(w\in L,z\in H\).

At a live pair, Bob chooses a side S in {E,H} with D_i^S(z)=0; one exists because x_i(z)=0. Alice then chooses a disjunct on that side that witnesses activation of i on w at its first round t_i(w). If it is a seed literal (a,b), the side being false on z means z_a != b = w_a, so the game outputs coordinate a. If it is a predecessor j, then x_j(z)=0, while the round-t witness gives x_j^(t_i(w)-1)(w)=1; hence j is live and has strictly smaller first-activation round.

Start from any empty-consequence root active on w. Soundness makes that root inactive on z. First-activation round strictly decreases at every predecessor step, so the game terminates after at most q transitions with a coordinate a satisfying w_a != z_a.

This proves that every valid cover induces a stateful alternating search procedure with q native state labels. Its local actions retain the C-319 structure: Bob chooses a failed side, and Alice chooses a true seed literal or an allowed predecessor. The game is a direct pairwise view of the endpoint/transition semantics; it does not assume that the cover extracts a circuit description.

## 2. Why this does not cross the linear barrier

The induced relation is simply

\[
R(w,z)=\{a\in[N]:w_a\ne z_a\},\qquad w\in L,\ z\in H.
\]

Every low/high pair differs, but the same search relation, considered without the C-319 transition restrictions, is solvable for all distinct table pairs by scanning coordinates in order and using one control state per coordinate. Thus a lower bound that uses only this relation and ignores the native transition algebra is capped by the trivial N+1-state scan. This does not upper-bound native q: the scan need not satisfy C-319 endpoint-containment constraints. It does show what any useful game lower bound must use - the native transition algebra or a selector-coherence condition - not merely correctness on the mismatch relation. A cover must decide the low/high promise without receiving a high table as a second input, and if a witness-based route is used it must coordinate one low-circuit description across all addresses.

The paired game remains useful only if strengthened with a resource that cannot be simulated by the universal coordinate scan, for example, a proved selector-coherence condition induced by every valid cover. No such condition follows from this game lemma. C-340/C-349 remain controlling cautions: arbitrary acceptance does not supply a circuit witness, and a gate internal witness pattern is representation-dependent.

## 3. Why standard hazard-free KW theorems do not transfer

A partial support C activates the native output only when a finite proof support lies inside C. By C-281/C-254, activation is sound in the one direction that every completion of C lies in \(\mathrm{SIZE}(s_2)\). The converse is not established: a cube can be covered by different accepting supports on different completions even when no one support is contained in C. Therefore this is a one-sided safe-certificate extension, not the exact three-valued hazard-free extension of a total Boolean function.

The standard hazard-free Karchmer-Wigderson theorem characterizes hazard-free **formula** size/depth; the dag-like Karchmer-Wigderson theorem characterizes ordinary circuit size for its acyclic protocol model. C-319 has shared recursive states whose terminating rank depends on the low table, and no q-preserving compilation from that cyclic game to either standard protocol model is proved. Formula or ordinary communication lower bounds therefore do not yield a new q bound here. Primary references: [Ikenmeyer, Komarath, and Saurabh, ECCC TR21-100](https://eccc.weizmann.ac.il/report/2021/100/download) and [Sokolov, ECCC TR16-202](https://eccc.weizmann.ac.il/report/2016/202/).

## 4. Checkpoint and next obligation

- Native lower bound: still (q\ge N-o(N)).
- Exact result: every cover induces the terminating q-state paired discrepancy game above.
- Exact failure: the unaugmented mismatch relation has an N-state scan, so it cannot certify q>N.
- Hazard-free formula transfer: unavailable without full ternary semantics and a sharing-preserving compiler.
- Next target: prove a selector/coherence invariant from the C-319 equations themselves, or attack the recurrent decoder directly; do not lower-bound the bare low/high mismatch relation.
- No full-promise near-linear cover or P-vs-NP proof has been obtained.
