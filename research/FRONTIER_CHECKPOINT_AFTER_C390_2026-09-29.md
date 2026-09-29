# Frontier checkpoint after C-390

Date: 29 September 2026  
Purpose: honor the C-384 continuation brief's required A-E checkpoints after four substantive claims (C-387 through C-390), and reset the active mechanism.

## Audit conclusions

**C-387 localization lemma: proved.** For any fixed polynomial state bound $q\le N^a$, C-370 gives each Reed-Muller anchor at least $(1-\varepsilon)N-h-O(1)$ selected certificate clauses with at most $k=O(\log N)$ true literals. The RM dual distance gives $(D-1)$-wise independence. Taking $r=\lceil(a+3)\log_2N\rceil$, with $2r<D$, the $2r$-moment/Markov bound gives for each global clause of width $w\ge\max(4k,16r)$

\[
\Pr[|E_C(f)|\le k]\le(8r/w)^r\le N^{-(a+3)}.
\]

Even when $w\ge D$, the estimate is valid because only moments involving at most $2r<D$ distinct coordinates are used. Averaging over at most $2q\le2N^a$ slots leaves at most $2N^{-3}$ wide sparse incidences in expectation. Hence at least $(1-\varepsilon)N-h-O(1)$ distinct global seed slots have width $C(a,\varepsilon,\delta)\log N$. The attachment's weaker $N/2-o(N)$ conclusion follows. This changes no q lower bound.

**C-390 endpoint audit: passed with scoped conclusion.** The masked RM membership circuit has q=O(N log N), every circuit-state carrier contains (S_H), the output carrier equals (S_H), and the root's H seed is the wide mismatch clause. The root activates on every RM anchor, while the high-carrier invariant plus its seedless self-loop blocks every high table. Zeroing wide seeds prevents all RM anchors from entering. This refutes universal wide-seed deletion in the endpoint model for a subpromise. It is not complete for SIZE(s1), and the RM family has easy O(N log N) membership.

## Required five-part checkpoint

| Front | Result at C-390 |
|---|---|
| Native quantitative bound | Unchanged: $\rho_{\mathrm{GapMCSP}}\ge N-o(N)$; no full-promise $N^{1+\epsilon}$ bound or $N^{1+o(1)}$ cover. |
| Hard-core selector | C-388 gives a coNP verification relation and a $\Sigma_2^P$ existential search formulation. No near-linear selector and no $N^{1+\epsilon}$ lower bound for every selector. |
| Selector/native bridge | None. A selector output does not decide its own coNP validity; a one-bit cover need not output a witness. No q-preserving reduction in either direction. |
| Collectively hard low subclass | None. RM is individually easy and has an O(N log N) membership circuit; no suitable low subclass has been found. |
| Local-seed LFP readout | C-390 proves wide seeds can be indispensable in one endpoint-realizable subpromise system. It gives no lower bound for the general/full-promise readout. |

The route-kill is specific and useful: C-387's localization cannot be promoted to a local-only decoder using certificate sparsity, monotonicity, and endpoint validity alone. Do not spend another cycle refining the same RM certificates or seeking another subpromise counterexample solely to establish this point.

## Next mechanism

1. **Selector synthesis, Front A.** Keep $R(f,Q)$ exact. Any multiplicative-weights, ellipsoid, boosting, or conditional-expectation proposal must implement and charge its NP best-response / coNP validity work as a Boolean circuit in $N$. Seek either an actual $N^{1+o(1)}$ selector or a lower bound for every valid selector, not only a canonical one.
2. **Native computational readout, Front B.** Attack the endpoint-derived least fixed point itself on the full promise. A theorem must apply to arbitrary valid C-319 lists and charge computation, not raw seed information, policy count, or generic graph-game size. The standard q-round compiler costs q-squared paid ANDs; ordinary lower bounds transfer only when their measure and promise match.
3. **Bridge test.** Only connect A and B after writing a concrete reduction and its size loss. C-388's coNP check prevents treating a sample Q as a self-certifying decision witness.

The goal stays active. This checkpoint records one proof-level route-kill, not a P-vs-NP breakthrough.
