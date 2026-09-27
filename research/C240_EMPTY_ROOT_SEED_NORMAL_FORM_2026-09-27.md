# C-240 — Seed normal form for empty-carrier output rules

Date: 27 September 2026  
Route: native cyclic fusion closure, continuing C-239/O-153.  
Status: exact structural lemma; it refines C-95 but gives no new lower bound.

## 1. Setup

Let (Usubseteq{0,1}^N) be the high side. Assume (U) two-wise shatters coordinates: every assignment to one or two distinct coordinates has an extension in (U). This holds for the active OPS parameters once (|mathrm{SIZE}(s_2)|<2^{N-2}).

For an endpoint (Esubseteq U), write

\[
S(E)=\{(k,b):L_{k,b}:=U\cap\{z:z_k=b\}\subseteq E\}.
\]

The direct seed predicate on anchor (w) is (a_E(w)=\bigvee_{(k,b)\in S(E)}[w_k=b]). Consider an empty-carrier output rule (i), with (E_i\cap H_i=\varnothing).

## 2. Seed-vocabulary theorem

If both (S(E_i)) and (S(H_i)) are nonempty, then there is a unique coordinate k and bit b such that

\[
S(E_i)=\{(k,b)\},\qquad S(H_i)=\{(k,1-b)\}.
\]

If either vocabulary is empty, the corresponding side's direct seed predicate is identically zero; the other side may have a larger vocabulary.

**Proof.** Choose (e=(k,b)\in S(E_i)) and (h=(\ell,c)\in S(H_i)). If (k\ne\ell), two-wise shattering gives (z\in U) with (z_k=b,z_\ell=c). Then (z\in L_{k,b}\cap L_{\ell,c}\subseteq E_i\cap H_i), contradiction. If (k=\ell) and (b=c), the nonempty slice (L_{k,b}) is contained in both endpoints, again a contradiction. Therefore (ell=k,c=1-b). Fixing h forces every member of (S(E_i)) to equal e; fixing e forces every member of (S(H_i)) to equal h. This proves the singleton conclusion.

Thus the two direct seed predicates of any empty root are either complementary single literals on one coordinate or one side has no direct seed at all. This strengthens C-95's anchor-wise statement (a_i(w)\land b_i(w)=0).

## 3. Exact output-root recurrence normal form

Let (P_i(w)=\bigvee_{j\in D_i^E}x_j(w)) and (R_i(w)=\bigvee_{j\in D_i^H}x_j(w)), after deleting self-supports as in C-91. The recurrence is

\[
x_i(w)=(a_i(w)\vee P_i(w))\land(b_i(w)\vee R_i(w)).
\]

There are two cases.

**Complementary-literal case.** If both seed vocabularies are nonempty, for one k,b we have (a_i(w)=[w_k=b]) and (b_i(w)=[w_k=1-b]). Hence

\[
x_i(w)=
\begin{cases}
R_i(w),&w_k=b,\\
P_i(w),&w_k=1-b.
\end{cases}
\]

The output root acts as a one-bit selector between two OR-families of predecessor carriers; it never activates directly from two seed sides.

**Seedless-side case.** If (b_i\equiv0), then (x_i=R_i\land(a_i\vee P_i)); the H-side predecessor family is mandatory. Symmetrically, if (a_i\equiv0), then (x_i=P_i\land(b_i\vee R_i)). If both direct predicates vanish, both predecessor families are mandatory.

Therefore every finite accepting proof of an empty root enters through at least one predecessor carrier. In the complementary-literal case, the coordinate selects which side's predecessor family supplies that entry. This is the structural source captured more coarsely by C-95's escape-source set (S_0).

## 4. What this does and does not buy

The result prevents an empty output endpoint pair from carrying two independent direct seed clauses over many coordinates. Its output-level direct seed information has at most one coordinate when both sides have seed vocabularies; otherwise one side is entirely predecessor-driven.

It does **not** bound the number of escape-source carriers, because one carrier may support many roots and many low anchors. It also does not bound the complexity of the nonempty predecessor states: their seed vocabularies and containment graph still carry the global circuit-consistency problem. C-80/C-121/C-134/C-160/C-161/C-213 and the C-234 equality-cover calibration remain unchanged. No superlinear (q) bound, near-linear full-promise cover, or P-vs-NP proof follows.

## 5. Next implication to test

Use this normal form to isolate the root-to-escape incidence relation: each accepted low anchor chooses a root and then activates at least one state in that root's zero-seed-side source family. The useful next theorem would charge either (a) the number of distinct escape carriers, or (b) the circuit-description inconsistency tolerated by a shared escape carrier, to q. C-95 already shows why merely proving that every low anchor reaches some escape source is insufficient; a single source may serve many anchors. Preserve the full-promise near-linear-cover search in parallel.
