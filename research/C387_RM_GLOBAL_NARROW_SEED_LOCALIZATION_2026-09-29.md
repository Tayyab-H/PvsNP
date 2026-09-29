# C-387 - Reed-Muller probes force globally narrow seed clauses

Date: 29 September 2026  
Route: audit the proposed C-370/C-372 localization lemma using a limited-independence moment bound.  
Classification: **PROVED STRUCTURAL LOCALIZATION FOR EVERY POLYNOMIAL-STATE COVER; NO q IMPROVEMENT.**

## 1. Statement and parameters

Let $N=2^n$, $s_1=N^\beta/(10n)$, and $s_2=N^\beta$, for a fixed $0<\beta<1$. Choose a fixed $0<\delta<1/2$ with $H_2(\delta)<\beta$, and let

\[
F=RM(\lfloor\delta n\rfloor,n),\qquad D=2^{\lfloor\delta n\rfloor+1}=N^{\delta+o(1)}.
\]

As in C-372, every $f\in F$ lies in $\mathrm{SIZE}(s_1)$, and the uniform distribution on $F$ is $(D-1)$-wise independent. Put $h=\log_2|\mathrm{SIZE}(s_2)|=o(N)$.

Fix any valid C-319 cover with $q\le N^a$ state pairs, where $a>0$ is any fixed constant. Its $2q$ seed slots are consistent clauses, after duplicate literals are removed. For every fixed $\varepsilon\in(0,1)$, there is a constant $C=C(a,\varepsilon,\delta)$ such that at least

\[
(1-\varepsilon)N-h-O(1)
\]

of the cover's seed slots have global clause width at most $C\log N$. In particular, at least $N/2-o(N)$ slots have width $O(\log N)$, as proposed in the continuation brief.

The constants in the width bound may grow as $\varepsilon$ decreases. The theorem does not assert $N-o(N)$ narrow slots for one fixed width constant.

## 2. Sparse certificate clauses at each anchor

For each $f\in F$, C-368 supplies a sufficient sound seed-CNF certificate $S_f$ with $m_f\le2q$ nonconstant clauses. C-370 gives, for every integer $k\ge1$,

\[
t_k(f)\ge N(2m_f)^{-1/(k+1)}-h-1,
\]

where $t_k(f)$ counts selected certificate clauses having at most $k$ literals true at $f$.

Choose

\[
k=\left\lceil\frac{a\log_2N+2}{-\log_2(1-\varepsilon)}\right\rceil.
\]

Since $m_f\le2q\le2N^a$, we have $2m_f\le4N^a$, and therefore

\[
(2m_f)^{-1/(k+1)}\ge1-\varepsilon.
\]

Thus every anchor has at least

\[
t_k(f)\ge(1-\varepsilon)N-h-1
\tag{1}
\]

certificate clauses with at most $k=O(\log N)$ true literals.

## 3. A wide clause is very unlikely to be sparse on the probe code

Fix one global seed clause $C$ of width $w$, and let $X_i(f)$ indicate that its $i$-th distinct signed literal is true at $f$. Dual distance makes every set of fewer than $D$ table coordinates uniform on the Boolean cube. Sign changes preserve this property, so the $X_i$ are $(D-1)$-wise independent fair bits.

Set $r=\lceil(a+3)\log_2N\rceil$. For all sufficiently large $N$, $2r<D$. If $w\ge R:=\max(4k,16r)$, then $R=C\log N$ for a constant $C=C(a,\varepsilon,\delta)$, and $k\le w/4$. Write $Z_i=2X_i-1\in\{-1,1\}$. The event that at most $k$ literals of $C$ are true implies

\[
\left|\sum_{i=1}^w Z_i\right|\ge w/2.
\]

Because $2r<D$, the $2r$-th moment equals the fully independent moment. Expanding and pairing indices gives

\[
\mathbb E\left(\sum_i Z_i\right)^{2r}
\le(2r-1)!!\,w^r
\le(2r)^r w^r.
\]

Markov's inequality now yields

\[
\Pr_{f\sim F}[|E_C(f)|\le k]
\le\left(\frac{8r}{w}\right)^r
\le2^{-r}
\le N^{-(a+3)}.
\tag{2}
\]

This argument still applies when $w\ge D$: it uses only $2r=O(\log N)<D$ independence, not full independence on the whole clause support.

## 4. Incidence count and conclusion

Call a pair $(f,C)$ sparse if $C\in S_f$ and at most $k$ of its literals are true at $f$. By (1), there are at least $(1-\varepsilon)N-h-1$ sparse incidences for every $f\in F$.

Let $W$ be the set of global seed slots of width at least $R$. From (2), the expected number of wide slots with at most $k$ true literals at a uniform $f\in F$ is at most

\[
|W|N^{-(a+3)}\le2qN^{-(a+3)}\le2N^{-3}.
\]

The number of wide sparse certificate incidences is no larger. Hence the average over $F$ of the number of *narrow* sparse certificate clauses is at least

\[
(1-\varepsilon)N-h-1-2N^{-3}.
\]

Each global narrow seed slot contributes at most one incidence for each anchor, so the number of distinct slot positions of width below $R$ is at least this average. This proves the claim. The same bound also shows that all but at most a $2N^{-3}$ fraction of Reed-Muller anchors have no wide seed clause with at most $k$ true literals.

## 5. What this proves, and what it does not

- Every polynomial-state valid cover has at least $N/2-o(N)$ globally $O(\log N)$-width seed slots; in fact, for each fixed $\varepsilon>0$, the count is at least $(1-\varepsilon)N-o(N)$ with a width constant depending on $\varepsilon$: **proved**.
- The argument is for the actual C-319 cover: the certificates come from its seed coordinates, and the code is the low-circuit Reed-Muller family of C-372.
- This does **not** improve $q\ge N-o(N)$. It merely shows that a polynomial-state system cannot put all certificate structure into globally wide seed clauses.
- It does **not** allow the wide seed slots to be deleted from the LFP readout. C-370 counts sparse-support clauses within $S_f$; the same minimal certificate may also need wide clauses that are true on $f$ through many literals. Monotonicity alone does not show $G_Q(\mathbf1_{S_f\cap J_{\rm narrow}})=1$. A local-only decoder therefore needs a separate dispensability or simulation theorem.
- The Reed-Muller family is only a probe. C-358 gives an $O(N)$ membership separator for that family, so it cannot itself force a superlinear full-promise bound.

The next exact question is whether the narrow certificate core can be made into a useful *local-seed LFP* while retaining all-high rejection, or whether wide features can remain essential at linear state cost. Any deletion argument must be proved for the C-319 recurrence and the endpoint-realizable seed map; the abstract fact that many narrow certificate clauses exist is insufficient.

Checkpoint: native $q\ge N-o(N)$ is unchanged. No near-linear full-promise cover, superlinear lower bound, or P-vs-NP proof is obtained.
