# C-390 - An endpoint-realizable subpromise cover can require a wide seed

Date: 29 September 2026  
Route: test O-229 by combining C-372's dual-distance low family with a masked circuit carrier and one native root rule.  
Classification: **PROVED q=O(N log N) ENDPOINT-REALIZABLE SUBPROMISE CALIBRATION; NOT A FULL-PROMISE COVER.**

## 1. Construction target

Fix beta and delta as in C-372: H_2(delta)<beta, delta<1/2, and delta<1-beta. Let

\[
F=RM(\lfloor\delta n\rfloor,n)\subseteq \mathrm{SIZE}(s_1),\qquad
U=\{z:\mathrm{CC}(z)>s_2\}.
\]

Write r=dim(F)=N^(H_2(delta)+o(1)) and h=log_2|SIZE(s_2)|=o(N). We construct a valid C-319 list that accepts every f in F and rejects every z in U, with q=O(N log N), such that setting every globally wide seed coordinate to zero makes it reject all of F.

The family is a subpromise of Gap-MCSP: the construction does not accept every table in SIZE(s_1).

## 2. A large subcube disjoint from the code

Choose any set A of m=r+1 table coordinates. The projection of F onto A has at most |F|=2^r patterns, fewer than the 2^m possible patterns. Choose p in {0,1}^A outside that projection and define

\[
S=\{w\in\{0,1\}^N:w|_A=p\},\qquad S_H=S\cap U.
\]

Then S∩F is empty. Since m=o(N), the subcube S has 2^(N-m) points, while |SIZE(s_2)|=2^h with h=o(N). Thus S_H is nonempty for all sufficiently large N. Also m>>log N.

Let I_S(w) be the conjunction of the m signed literals specifying S. There is a De Morgan circuit C_0 of size O(N log N) that accepts exactly F: compute all algebraic-normal-form coefficients of w using the fast Boolean Möbius transform, then test that coefficients above degree floor(delta n) vanish. It rejects every table in U.

## 3. Lift the circuit so every internal high carrier contains S_H

Convert C_0 to a monotone dual-rail circuit. For every wire g replace its value by

\[
\widehat g=g\lor I_S.
\]

The identities

\[
(g_1\land g_2)\lor I_S
=(g_1\lor I_S)\land(g_2\lor I_S),
\qquad
(g_1\lor g_2)\lor I_S
=(g_1\lor I_S)\lor(g_2\lor I_S)
\]

let us build the lifted circuit with O(N log N+m) gates. Each lifted gate is true on every point of S. The output computes C_0(w) OR I_S(w), so its high-table carrier is exactly S_H.

Realize each lifted input rail y_(a,b) OR I_S by the endpoint carrier

\[
E_{a,b}=L_{a,b}\cup S_H
\]

with opposite endpoint U. Its seed clause contains the literal [w_a=b], so every correct literal input on f in F activates the corresponding leaf state. The seed clause may also be true on extra low or medium tables; this only helps completeness. For high inputs, every seed that activates a state is contained in that state's endpoint, preserving the carrier soundness invariant.

Apply the C-109 gate-to-relay construction to the lifted circuit, using each gate's high carrier as its endpoint. For AND gates use the intersection rule; for OR gates use the two child rules with the other endpoint U. Every resulting state consequence contains S_H, because every lifted gate is true throughout S_H. The top carrier is exactly S_H, and it activates on every f in F.

This subgraph has O(N log N) rule pairs and has no empty-consequence state.

## 4. Add one root with a wide endpoint seed

Add a rule R with endpoints

\[
E_R=S_H,\qquad H_R=U\setminus S_H.
\]

Its consequence is empty, so R is the only root. Its E-side seed is false: no complete high-table literal slice is contained in S_H. Indeed, any single-literal slice has high tables outside the codimension-m subcube S, since fixing at most two table bits leaves 2^(N-2)>|SIZE(s_2)| tables for large N.

Its H-side seed is exactly the clause

\[
B_R(w)=\bigvee_{a\in A}[w_a\ne p_a],
\]

of width m. Each mismatch literal's entire high slice lies outside S; every other literal slice intersects S_H and is not contained in H_R. Thus B_R(w)=1 precisely when w is outside S.

The predecessor structure is also exact:

- The C-109 circuit states all have consequences containing S_H. Some include the top carrier S_H, so R's E-side can use an active output state on f in F.
- No circuit state consequence is contained in H_R, since S_H is nonempty and lies in every such consequence.
- R itself is a predecessor of R by empty-set containment, giving the forced self-loop.

For f in F, f is outside S, so B_R(f)=1; the lifted circuit output is active; hence R accepts f.

For a high table z in S_H, B_R(z)=0 and R's H-side has only its own self-loop. Starting from the zero vector, R never activates. For a high z outside S_H, the C-319 invariant says every active state consequence contains z. Therefore no active circuit state can have consequence contained in E_R=S_H. The E-side has no seed either, and R's self-loop cannot start the least fixed point. So R rejects every high table.

This proves the list is a valid endpoint-realizable C-319 cover for the subpromise F versus the actual OPS high set.

## 5. Truncation failure and combination with C-387

The only empty-consequence state is R. Its H-side predecessor set is {R}; its H-side seed is the width-m clause B_R. If every seed clause of width greater than C log N is fixed to zero, then B_R is zero for sufficiently large N because m=r+1=N^(H_2(delta)+o(1))>>log N. R's H-side becomes only its self-loop, so the least fixed point accepts no input, including every f in F.

The proof of C-387 uses completeness only on the Reed-Muller anchors and soundness on all high tables. It therefore applies unchanged to this subpromise list: for each fixed epsilon>0 this same q=O(N log N) graph has at least (1-epsilon)N-o(N) globally O(log N)-width seed slots in the selected safe certificates. Thus near-full narrow certificate support and an indispensable globally wide readout seed coexist in an actual endpoint-realizable system.

## 6. Scope and research consequence

- The local-only truncation inference is false even for the C-372 probe family and a near-linear-size native subpromise cover.
- The example is not a full Gap-MCSP cover because it accepts F, not all of SIZE(s_1).
- It does not improve q>=N-o(N), construct a full-promise near-linear cover, or prove a P-vs-NP separation.
- Do not simplify the full-promise task to a local-seed LFP merely from C-387. A surviving local route must account for how the globally wide gate coordinates enter the root/readout, or prove a stronger theorem specific to completeness on all low circuits.

This closes the proposed universal wide-feature deletion step on the Reed-Muller probe. The remaining target is computational work in the full readout or an actual full-promise construction/lower bound.
