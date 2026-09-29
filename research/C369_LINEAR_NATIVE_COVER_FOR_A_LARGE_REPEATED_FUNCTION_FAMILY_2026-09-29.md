# C-369 - A linear native cover supports an exponential low-circuit subfamily

Date: 29 September 2026  
Route: calibrate C-368 certificate sharing against repeated truth-table fibers and the exact C-258 cover.  
Classification: **EXACT LARGE-SUBFAMILY CALIBRATION; O(N) STATES; NOT A FULL-PROMISE COVER.**

## 1. The family

Write an address as `(u,y)`, where `u` has `k` bits and `y` has `n-k` bits. Let `d=2^k`, `r=2^(n-k)`, and `N=dr`. Define

\[
\mathcal R_{d,r}=\{w: w_{(u,y)}=a_u\text{ for some }a\in\{0,1\}^d\}.
\]

Thus each of the `d` address fibers is constant, while its `d` constant values are arbitrary. The family has exactly `2^d` tables. A complete binary decision tree on the `k` address bits computes any choice of `a`, using at most `C d` gates for an absolute constant `C` (including shared input negations). Choosing a power of two `d=Theta(s1)` with `Cd<=s1` gives

\[
\mathcal R_{d,r}\subseteq\mathrm{SIZE}(s_1),\qquad
|\mathcal R_{d,r}|=2^d=2^{\Theta(s_1)}.
\]

## 2. One common safe clause certificate

For every fiber `u` and every nonrepresentative suffix `y!=0`, impose equality with the representative bit:

\[
(\neg w_{(u,0)}\lor w_{(u,y)})\;\land\;
(w_{(u,0)}\lor\neg w_{(u,y)}).
\]

The conjunction `Phi_{d,r}` of these clauses has exactly `2d(r-1)=2(N-d)` clauses and its satisfying tables are exactly `R_{d,r}`. Consequently its entire model set lies in `SIZE(s1)`, hence in `SIZE(s2)`, and every one of the `2^d` low tables satisfies this same safe CNF.

This is a certificate-level calibration, not a claim that an arbitrary C-319 cover contains these clauses among its endpoint seeds. It shows that the C-368 width bound alone cannot turn the number of low anchors into a comparable number of distinct safe certificates: one near-`2N`-clause cylinder can contain `2^{Theta(s1)}` low tables.

## 3. Native subpromise realization from C-258

The family is precisely the repeated-block family in C-258/C-326, with `d` blocks of length `r`. Under the C-326 richness condition `2^(r-3)>|SIZE(s2)|`, the recorded native construction accepts this family and rejects every high table using

\[
q=2N+2d-1=O(N)
\]

state pairs. In the OPS regime, `log2 |SIZE(s2)|=O(s2 log(s2+n))=N^(beta+o(1))`. With `d=Theta(s1)` and any fixed `beta<1/2`, `r=N/d=N^(1-beta+o(1))` eventually exceeds this logarithm, so the richness condition holds. This is an actual linear-state **subpromise** cover for an exponentially large low family; the full-promise separation and high-set rejection are those established in C-258/C-326.

## 4. Consequence for the active state-count question

The combined calibration rules out a certificate-count argument based only on (i) each low anchor needing `N-o(N)` clauses and (ii) the low family having `2^{Theta(s1)}` members. Large low families can share a near-linear clause description and can have an `O(N)` native subcover. A successful state lower bound must distinguish the whole `SIZE(s1)` promise from these repeated-fiber families and exploit endpoint incidence or least-fixed-point compatibility across genuinely different circuit descriptions.

Limits: this does not construct a full-promise `N^(1+o(1))` cover; it does not improve `q>=N-o(N)`; it does not show that all C-319 covers expose a common certificate; and it proves no P-vs-NP result. The next target remains a theorem charging the cost of combining different low-circuit topologies, or a full-promise near-linear construction.

## 5. Checkpoint

- `2^(Theta(s1))` low tables share one safe `2(N-d)`-clause CNF: **proved**.
- The same family has the recorded `O(N)`-state C-258 native subcover under the richness condition: **proved by C-326**.
- A full-promise cover or superlinear q lower bound: **not obtained**.
- Actual native lower bound: `rho_GapMCSP>=N-o(N)`.
