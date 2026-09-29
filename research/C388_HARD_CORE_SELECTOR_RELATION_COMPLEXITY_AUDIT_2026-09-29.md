# C-388 - The hard-core selector is a coNP-verified, second-level search problem

Date: 29 September 2026  
Route: formalize the C-345/C-346 sample selector as an exact relation and audit its construction, verification, and reduction boundaries.  
Classification: **EXACT RELATION AND POLYNOMIAL-HIERARCHY UPPER BOUNDS; NO EFFICIENT SELECTOR OR LOWER BOUND.**

## 1. Parameter and relation audit

Use the OPS parameters recorded in C-346:

\[
N=2^n,\qquad s_1=\frac{N^\beta}{10n},\qquad s_2=N^\beta,
\]

where $n=\log_2N$ and fixed $0<\beta<1$. Thus the attachment's $10\log N$ denominator is the same up to the chosen logarithm base. Let $T=\lceil1.515s_1\rceil$, the predictor threshold used in C-346, and let $L=\lceil cN^\beta\rceil$ for the fixed sample-size constant supplied by its Hoeffding/union-bound argument.

For an explicit truth table $f\in\{0,1\}^N$ and a list $Q=(x_1,\ldots,x_\ell)$ of addresses in $\{0,1\}^n$, $1\le\ell\le L$, repetitions allowed, define labels implicitly by $f(x_i)$ and

\[
\operatorname{err}_{f,Q}(C)=\frac1\ell\sum_{i=1}^{\ell}[C(x_i)\ne f(x_i)].
\]

The hard-core relation is

\[
R(f,Q)\iff \forall C\in\mathrm{CIRCUIT}_{n,T},\quad
\operatorname{err}_{f,Q}(C)\ge0.259.
\tag{3}
\]

C-346 proves that every $f$ with $CC(f)>s_2$ has some such $Q$. Adding the fixed uniform-mass branch of weight $1/1024$ gives full support and keeps every size-$T$ predictor's accuracy below $0.742<0.75$. If $CC(f)\le s_1$, $f$ itself is a size-$T$ circuit with zero error on every $Q$, so no $Q$ satisfies (3). Thus

\[
\exists Q\ R(f,Q)
\]

separates the stated low and high promise, with medium tables unconstrained. The full-support mixture is deterministic postprocessing of $Q$; it need not be encoded by the list itself.

## 2. Verification and search complexity

Assume the standard finite gate-description encoding. Since $T\log(T+n)=N^{\beta+o(1)}$, a circuit of size at most $T$ has a polynomial-length encoding in the explicit input length $N$. Given one proposed circuit $C$, its error on $Q$ is computed in polynomial time by evaluating it on the listed addresses and reading $f$'s labels. Therefore

\[
R(f,Q)\in\mathrm{coNP}.
\]

The complement witness is a size-$T$ circuit with error below $0.259$. This proves membership only; it does not establish coNP-completeness.

The existential witness $Q$ has polynomial length in $N$, and the verifier for $R$ is coNP. Hence the decision language

\[
H(f):=[\exists Q,\ |Q|\le L,\ R(f,Q)]
\]

lies in $\Sigma_2^P$. It has the required low/high promise behavior by the preceding paragraph. The direct deterministic exhaustive algorithm enumerates lists and circuit descriptions in time

\[
2^{O(L\log N+T\log(T+n))}
=2^{O(N^\beta\log N)}
=2^{N^{\beta+o(1)}}.
\]

This is a finite upper bound, not a polynomial-time or near-linear circuit construction.

One exact counting view is

\[
B_T(f,Q)=\#\{\text{valid circuit descriptions }C:|C|\le T,
\operatorname{err}_{f,Q}(C)<0.259\}.
\]

With a canonical polynomial-length encoding, $B_T$ is a #P function and (3) is exactly $B_T(f,Q)=0$. Counting descriptions rather than distinct Boolean functions avoids a duplicate-function counting issue; zero detection is unchanged. Counting how many lists $Q$ satisfy (3) is a higher-level problem: guessing $Q$ and asking an NP oracle whether a bad circuit exists places that count in #P^NP. Neither counting formulation supplies an efficient selector. Approximate counting is useful only if one proves an algorithm and an error guarantee for this particular implicit circuit class; C-346 provides neither.

## 3. Exact minimax formulation and the cost of optimization methods

For fixed $f$, put $\ell_f(x,C)=[C(x)\ne f(x)]$. The hard-core value is the finite zero-sum game

\[
v(f)=\max_{\mu\in\Delta([N])}\ \min_{C\in\mathrm{CIRCUIT}_{n,T}}
\sum_x\mu_x\ell_f(x,C).
\]

Its dual is

\[
v(f)=\min_{\pi\in\Delta(\mathrm{CIRCUIT}_{n,T})}\ \max_{x\in[N]}
\sum_C\pi_C\ell_f(x,C).
\]

C-346 shows $v(f)\ge0.26$ for every high table. Sampling $O(\log|\mathrm{CIRCUIT}_{n,T}|/\eta^2)=O(N^\beta)$ addresses from an optimal distribution and applying a union bound gives the finite empirical list with margin $0.259$.

This does not make multiplicative weights, boosting, or an LP solver an efficient construction. A separation/best-response step asks whether there is a size-$T$ circuit whose error under a supplied rational address distribution is below a threshold. A proposed circuit is a polynomially checkable witness, so the decision oracle is in NP; actually supplying a best response is an NP search task. An ellipsoid or online-learning analysis with this oracle is an oracle algorithm, not an unconditional small Boolean circuit. Circuit-description length, oracle implementation, rational precision, and the final output circuit's size must all be charged.

## 4. Why this is not yet a reduction to or from native C-319 covers

- A selector $S(f)=Q$ that is correct on high tables does not decide the promise. Testing whether its output satisfies (3) still has a universal quantifier over all size-$T$ circuits, i.e. the coNP verification above. No near-linear circuit for that test is known here.
- A one-bit Gap-MCSP decision circuit need not output any witness $Q$. Thus decision does not automatically synthesize a hard-core sample.
- C-319 seed clauses and C-370 certificates are not already anti-checker samples. A hard-core list must hit the disagreement set of every small predictor on the address domain. A safe seed certificate instead has the property that its satisfying truth tables are all in $\mathrm{SIZE}(s_2)$. The quantifiers and objects differ; no q-preserving conversion has been proved.
- Canonicalizing $Q$, for example by choosing the lexicographically first valid list, defines one selector but cannot prove that *every* valid selector is hard. Conversely, the existence of many witnesses gives no small selector without an explicit search procedure.

Therefore the two required lower/upper directions remain open: no $N^{1+\epsilon'}$ lower bound for every valid selector is proved, and no $N^{1+o(1)}$ selector circuit is constructed. Nor is there a near-linear reduction in either direction between selector synthesis and arbitrary C-319 covers.

## 5. Checkpoint

- Exact relation and thresholds: **formalized**.
- Candidate verification: **coNP upper bound**, with NP counterexample witness.
- Existence of a witness for high tables / no witness for low tables: **proved in C-346 plus the size-$T$ inclusion**.
- Efficient selector, lower bound for all selectors, and a q-preserving bridge: **not proved**.
- Native $q\ge N-o(N)$, no full-promise near-linear cover, no P-vs-NP proof.

The productive next step is an actual construction or lower bound for this set-valued selector, with the NP best-response cost accounted for, alongside the separate C-319 local-certificate/readout question. The selector route is not interchangeable with the native route until an explicit transfer is proved.

## 6. Literature audit: boosting does not remove the weak-learner cost

Feldman's distribution-specific agnostic-boosting work connects optimal hard-core-set constructions to boosting and constructs hard-core sets through a boosting framework ([Feldman 2009](https://arxiv.org/abs/0909.2927)). This is a useful algorithmic template, but it is oracle-relative: the framework invokes a weak agnostic learner on changing distributions. In the present relation, the corresponding best response is to find a size-T circuit with sufficiently low weighted error against f. A proposed circuit is a polynomially checkable witness, so this is an NP search task. Replacing it with a free oracle would not yield a Boolean selector circuit; a valid construction must implement or avoid this optimization step and charge its circuit size. The literature therefore supports the C-388 bottleneck diagnosis, not a selector construction or lower bound.
