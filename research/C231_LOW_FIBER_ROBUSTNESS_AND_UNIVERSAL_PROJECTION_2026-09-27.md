# C-231 — Robust low fibers and the universal-quantifier barrier

Date: 27 September 2026  
Scope: use the C-230 Lupanov cube quantitatively on the actual OPS thresholds. This proves common flexible address blocks around every low table, strengthens residual mismatch support, and identifies an exact quantifier obstruction to projecting a fusion cover. It does not yield a q lower bound.

## 1. One fixed address block is harmless for every low table

Let (N=2^n), (s_1=N^\beta/(c n)), (s_2=N^\beta), and fix (0<\beta<1). Choose a prefix cylinder of input addresses

\[
F=\{x\in\{0,1\}^n:x_{1..n-k}=p\},\qquad m=|F|=2^k,
\]

with (2^k/k\le \eta s_2), where eta is a sufficiently small constant. Then (k<n) and (m=\Theta(s_2\log s_2)=\Theta(N^\beta n)).

For any (w\in\mathrm{SIZE}(s_1)), take a circuit C for w. For any labeling g of F, Lupanov synthesis gives a k-input circuit for g of size (O(2^k/k)\le O(\eta s_2)). Let (P_F) test the fixed prefix. The table that equals g on F and w outside F is computed by

\[
(\neg P_F\wedge C)\vee(P_F\wedge g).
\]

Its size is at most (s_1+O(n+\eta s_2)\le s_2) after fixing eta small and taking n large. Thus, for **every** low table w, the entire coordinate cube that fixes w outside this one common F and frees all m coordinates of F lies in SIZE(s2).

Consequences:

1. No high table has the same restriction as a low table outside F. Hence the projected low and high sets on ([N]\setminus F) are disjoint.
2. A separator for the actual promise must find a mismatch outside F for every low/high pair.

This is a fixed support statement, not a fusion-cover construction: an existing closure may use F literals to distinguish low tables from medium tables.

## 2. The remaining support still has a linear-in-s2 mismatch margin

The sparse-indicator patching lemma from C-212 computes the indicator of any r-address set with (O(n+r n/\log(r+1))) gates. Suppose low w and high z differ on only r coordinates outside F. Patch C for w by (i) replacing its values on F with z's arbitrary F-pattern, using the k-input Lupanov circuit, and (ii) flipping the r outside-F disagreements with the sparse indicator. This gives

\[
\mathrm{CC}(z)\le s_1+O(\eta s_2+n+r n/\log(r+1)).
\]

Choose eta and then a constant (\gamma_\beta>0) small enough. If (r\le\gamma_\beta s_2), the right side is below s2 for all sufficiently large n, a contradiction. Therefore

\[
\boxed{\forall w\in\mathrm{SIZE}(s_1),\ z\notin\mathrm{SIZE}(s_2):\quad
|\{j\notin F:w_j\ne z_j\}|\ge\gamma_\beta s_2.}
\]

So there is a common omitted block of Θ(s2 log s2) coordinates, yet every promised pair still has Ω(s2) mismatches in the remaining coordinates. The previous global Hamming-distance theorem gives Ω(s2) mismatches somewhere; this strengthens it by locating the whole residual support outside one fixed address block.

## 3. A smaller common block is entirely low for deep-low anchors

Choose (F_0) of prefix-block form with (|F_0|=\Theta(s_1\log s_1)=\Theta(s_2)), taking the Lupanov circuit for arbitrary values on F0 to cost at most (s_1/4). For every (w\in\mathrm{SIZE}(s_1/4)), every table obtained by changing w arbitrarily on F0 has circuit size at most

\[
s_1/4+s_1/4+O(n)<s_1.
\]

Thus each outside restriction in π(Y0), where (Y_0=\mathrm{SIZE}(s_1/4)) and π deletes F0, has **all** its completions in the low set. If h_Q is any successful fusion readout, then

\[
\forall p\in\pi(Y_0)\ \forall u\in\{0,1\}^{F_0}:\quad h_Q(p,u)=1.
\]

For any p in the projection of the high set Z, at least one completion u is a high table, hence

\[
\forall p\in\pi(Z)\ \exists u\in\{0,1\}^{F_0}:\quad h_Q(p,u)=0.
\]

Consequently the robust projection

\[
g_Q(p)=\bigwedge_{u\in\{0,1\}^{F_0}}h_Q(p,u)
\]

is a valid separator between π(Y0) and π(Z). This is an exact consequence of the promise and the low cube; no assumption on medium-band behavior is needed.

## 4. Why this does not yet compile to a smaller closure

The original q-rule recurrence has the form

\[
x_i=(A_i\vee\bigvee_{j\in P_i}x_j)\wedge(B_i\vee\bigvee_{j\in R_i}x_j).
\]

Universal quantification over u commutes with the top conjunction, but not with the side ORs:

\[
\forall u\,(x_1(u)\vee x_2(u))
\ne
(\forall u\,x_1(u))\vee(\forall u\,x_2(u)).
\]

The one-bit counterexample (x_1(u)=u, x_2(u)=1-u) has the left side true and the right side false. Different predecessor derivations can cover different block completions. To form g_Q exactly, one must preserve the coverage of all (2^{|F_0|}) completions, not merely keep predecessors that are universally active. A direct cofactor construction uses (2^{|F_0|}) copies of h_Q, which is useless. The native q-state grammar may have a more compact coverage representation, but none is established.

This identifies a sharper research question than “delete a large coordinate block”:

> Can a q-state positive cyclic closure certify, with controlled q, that its accepting proof family covers every completion of a block for low projections while leaving at least one high completion uncovered for high projections?

The obstruction is a ∀-completion/∃-proof exchange. At a fixed state, accepted completions may be covered by different predecessor supports; a shared-state count does not preserve the coverage relation.

**Status:** uniform safe block and residual mismatch lemma proved from Lupanov synthesis plus C-212 patching; robust low projection separator derived exactly; the universal-fiber compilation is open. No superlinear q bound, near-linear cover, or P-vs-NP proof follows.
