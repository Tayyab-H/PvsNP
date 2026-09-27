# C-251 — Root escape support dichotomy

Date: 27 September 2026  
Route: O-153, combine C-249 root normalization with C-250's half-safe escape lemma and close the seedless/missed-seed branch at the level of proof supports.  
Status: local support theorem proved; no aggregation into a state lower bound.

## 1. Setting

Let (Y=mathrm{SIZE}(s_1)), (L=mathrm{SIZE}(s_2)), and (U={0,1}^N\setminus L), with the OPS parameter regime and the C-74/C-75 least-fixed-point closure. Fix an empty-carrier output root (i) normalized as in C-249, and a low table (w\in Y) accepted through (i). A proof support is a consistent set of signed table literals at the leaves of a selected finite proof tree. If (C\subseteq\ell(w)), every table extending (C) preserves the selected seed and predecessor witnesses above those leaves.

Write (C_E,C_H) for the supports selected on the two root sides when both are predecessor proofs. A direct seed on one side contributes its one signed literal instead. Supports chosen from one proof of (i) are consistent because they are all matched by (w).

## 2. Theorem: seed-or-pair escape dichotomy

For every normalized empty-carrier root (i) and every accepted low (w) routed through it, choose a root proof according to the following cases.

1. **A direct root seed matches (w).** Use that seed on its side. The opposite side must be witnessed by a predecessor support (C\subseteq\ell(w)). By C-250, at most

   \[
   \left\lceil\log_2|L|\right\rceil+1
   \]

   coordinates are free in (C). In particular, for the matching root literal ((k,b)), the half of (mathrm{Cyl}(C)) with bit (b) is contained in (Y\subseteq L).

2. **No direct root seed matches (w).** Both root sides require predecessor proofs, with supports (C_E,C_H\subseteq\ell(w)). Their union (C_*=C_E\cup C_H) is consistent. Every Boolean table extending (C_*) preserves both predecessor derivations, activates the empty-carrier output root, and is therefore in (Y\subseteq L). Consequently

   \[
   |\mathrm{free}(C_*)|\le\lfloor\log_2|L|\rfloor.
   \]

The second case includes roots with no direct seeds (the seedless branch) and anchors that miss all available direct seed literals. It is a paired-cylinder statement: it does not imply the same width bound for (C_E) or (C_H) separately.

### Proof

At an empty-carrier root, activation is acceptance. A selected finite derivation remains valid under any table that agrees with all its leaf literals: seed leaves remain present, and predecessor leaves remain active by induction up the proof tree. In case 1, C-249's seed normal form and C-240 ensure the opposite side has no matching direct seed on (w), so it uses a predecessor. The one-sided width conclusion is precisely C-250, using the matching high half-cube inside the seed side's endpoint and the C-243 carrier lemma.

In case 2, each side's chosen witness must be a predecessor. Any Boolean completion of (C_*) preserves both branches, hence activates (i). The output carrier is empty, so soundness puts every such completion in (Y\subseteq L). If (f=|\mathrm{free}(C_*)|), this cylinder has (2^f) tables, giving (2^f\le |L|) and the stated bound. \(\square\)

## 3. Repeated-block consequence

On C-234's family with (r) repeated copies of each suffix coordinate, a consistent support cylinder with (f) free table coordinates can match at most (2^{f/r}) diagonal anchors: a suffix bit can vary only when all its (r) copies are free. Thus each selected escape signature covers at most

\[
2^{(\lceil\log_2|L|\rceil+1)/r}
\]

anchors in case 1 and at most (2^{\lfloor\log_2|L|\rfloor/r}) in case 2. This closes the *local capacity gap* for seedless and missed-seed routes: every anchor has a safe one-support or paired-support signature.

## 4. Exact failure of the state-count route

The conclusion counts required signatures, not states. A paired signature consists of two rooted predecessor proof-DAG descriptions plus a root; counting pairs squares the existing bound (q\,2^q(2N+q)^{2q}), changing only constants in its logarithm. At (q=\Theta(N)), the available description count remains (exp(O(N\log N))), which is larger than any anchor family of size at most (2^N). The one-support branch has the same obstruction. No incompatibility, overlap, or cross-root reuse charge is obtained.

Therefore C-251 does not strengthen the existing (q\ge N-o(N)) floor, prove a near-linear full-promise cover, or resolve P versus NP.

## 5. Next proof obligation

For each output root, the accepting anchors now split into one-sided seed escapes and two-sided predecessor joins. The next theorem must use the *incidence geometry* of these signatures across the same q-state grammar: either prove that many signatures sharing states force a high cross-join / forbidden low cylinder, or construct a compact full-promise cover from the dichotomy. Merely counting safe signature pairs, or bounding each union cylinder separately, repeats the C-246 failure.
