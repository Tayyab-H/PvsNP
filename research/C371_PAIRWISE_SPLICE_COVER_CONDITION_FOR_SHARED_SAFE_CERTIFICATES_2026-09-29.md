# C-371 - A shared safe certificate must block almost every splice mask

Date: 29 September 2026  
Route: combine the C-320 splice cube with the exact seed-CNF certificate from C-368/C-370.  
Classification: **EXACT CROSS-ANCHOR NECESSITY; NO STATE-COUNT IMPROVEMENT.**

## 1. Setup

Let `f,g` be two tables in the same sound certificate cone

\[
\Phi(w)=\bigwedge_{j=1}^m C_j(w)\subseteq\mathrm{SIZE}(s_2).
\]

Write `D={a:f_a!=g_a}`, `d=|D|`, and for each clause define its f- and g-true literal supports

\[
E_j(f)=\{a:C_j\text{ has a literal on }a\text{ true at }f\},\qquad
E_j(g)=\{a:C_j\text{ has a literal on }a\text{ true at }g\}.
\]

For each owner mask `mu` on D, let `h_mu` take g's bit on mu and f's bit elsewhere. These are `2^d` distinct tables.

## 2. Pairwise splice-cover inequality

At most `M=|SIZE(s2)|` owner masks yield low splices. Every other splice is high and therefore lies outside the sound cone `Phi`; it must falsify at least one clause.

If `E_j(f)` and `E_j(g)` intersect, the common true literal stays true under every splice, so clause j falsifies no owner mask. If the supports are disjoint, they lie in D. The clause is false exactly when every coordinate in `E_j(f)` is assigned to g and every coordinate in `E_j(g)` is assigned to f. This is a subcube of fraction

\[
2^{-|E_j(f)|-|E_j(g)|}.
\]

The falsification subcubes of the clauses cover at least `1-M/2^d` of the owner cube. The union bound therefore gives the necessary inequality

\[
\boxed{\displaystyle
\sum_{j:E_j(f)\cap E_j(g)=\varnothing}
2^{-|E_j(f)|-|E_j(g)|}\;\ge\;1-2^h/2^d,
\qquad h=\log_2 M.}
\tag{1}
\]

This holds for every pair of low tables in one certificate cone, not merely for a specially chosen code family.

## 3. A small-witness consequence

Assume `d>=h+2`, so the right side of (1) is at least `3/4`. Let `K=ceil(log2(2m))`. The total contribution from clauses with `|E_j(f)|>K` is at most

\[
m2^{-(K+1)}\le 1/4.
\]

Hence clauses with `|E_j(f)|<=K` contribute at least `1/2`. There are at most m clauses, so at least one clause satisfies

\[
E_j(f)\cap E_j(g)=\varnothing,
\qquad
|E_j(f)|+|E_j(g)|\le\log_2(2m).
\tag{2}
\]

Thus every far pair sharing a safe cone has a clause that certifies the two anchors using only logarithmically many true literals in total, with the two witness supports disjoint. The condition is necessary, not sufficient: it does not ensure that one clause family blocks every high splice, and it says nothing about the transition graph needed to select a safe cone.

## 4. Equality calibration and the remaining barrier

For two distinct members of the repeated-fiber family in C-369, choose a fiber on which their constant bits differ. Either binary equality clause for a representative/nonrepresentative coordinate pair is true at the two tables through opposite singleton supports. Its total witness size is two, consistent with (2); the common equality CNF blocks all mixed-fiber splices with only O(N) clauses. Therefore the pairwise inequality is tight on the C-258 equality calibration and cannot alone force superlinear q.

The remaining target is a **multi-anchor** theorem: show that one q-state readout cannot choose compatible small-witness clauses for all the diverse low-circuit anchors while keeping each resulting CNF cone inside `SIZE(s2)`, or explicitly construct such a full-promise readout. Pairwise splice coverage, distance, and C-370's per-anchor support counts do not yet bound how many different cones a shared state graph can generate.

## 5. Literature transfer boundary

Cheraghchi, Kabanets, Lu, and Myrisiotis prove that a single CNF or DNF computing exact MCSP on N-bit truth tables requires size `2^(N/O~(log^2 N))` (Theorem 4). This is a strong lower bound for one depth-two representation, but `Phi` here is only one sound certificate cone. The full C-319 acceptance predicate is a least-fixed-point readout that can be a union of many such cones; no size-preserving flattening to one CNF or DNF is established. Therefore that theorem does not imply a q bound for this lemma. The model-transfer audit is recorded separately in C-339. Primary paper: [Cheraghchi, Kabanets, Lu, and Myrisiotis, *Circuit Lower Bounds for MCSP from Local Pseudorandom Generators*](https://doi.org/10.4230/LIPIcs.ICALP.2019.39).

## 6. Checkpoint

- Inequality (1) for any two anchors in the same sound certificate cone: **proved**.
- Small disjoint witness clause (2) for distance at least `h+2`: **proved**.
- Cross-anchor/state charge, superlinear q lower bound, or full-promise near-linear cover: **not obtained**.
- Actual native lower bound remains `rho_GapMCSP>=N-o(N)`.
