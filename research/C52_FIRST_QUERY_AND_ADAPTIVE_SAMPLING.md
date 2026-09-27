# C-52 — First-query contraction and the adaptive-sampling limit

Date: 2026-09-25

## Claim

At the OPS promise parameters, every high table admits a coordinate on which a constant fraction of all small-circuit descriptions disagree. More strongly, a single nonuniform circuit family of size $O(Nn)$ finds such a coordinate for every high table. This resolves the root step of the version-space greedy process. It does not construct a full anti-checker and does not improve the O-1 lower bound.

Write $N=2^n$, $s_1=2^{\beta n}/(10n)$, and $s_2=2^{\beta n}$. Let

$$
\Delta_s(f)=\max_{\mu\in\Delta(\{0,1\}^n)}\min_{D:\,CC(D)\le s}
\Pr_{x\sim\mu}[D(x)\ne f(x)].
$$

## Exact margin at the OPS gap ratio

For $CC(f)>s_2=10ns_1$, we have $\Delta_{s_1}(f)\ge 3/10$. Suppose instead that $\Delta_{s_1}(f)<3/10$. By finite minimax, there is a distribution on size-$s_1$ circuits for which every fixed input has expected error below $3/10$. Draw $k$ to be the smallest odd integer at least $9n$ circuits independently and take their pointwise majority. For any fixed input, Hoeffding's inequality bounds the probability that the majority errs by

$$
\exp\left(-2k(1/2-3/10)^2\right)=\exp(-0.08k).
$$

Multiplying by $N=2^n$, the union bound is at most $\exp(n\ln2-0.72n)<1$. Thus some sampled majority equals $f$ on all inputs. Its fan-in-two circuit size is $ks_1+O(k^2)\le(0.9+o(1))s_2<s_2$, contradiction. Therefore the margin is at least $3/10$. The majority overhead is $O(n^2)=o(s_2)$ for each fixed $\beta>0$.

## One global sample finds the first point

Let $\mathcal H$ be a finite set of valid, fixed-length syntactic descriptions of circuits of size at most $s_1$, and choose $D$ uniformly from $\mathcal H$. Duplicates are allowed: all guarantees below are over descriptions, and each description computes a circuit to which the margin applies. Define

$$
q_x=\Pr_{D\sim U(\mathcal H)}[D(x)=1],\qquad
p_x(f)=\Pr_{D\sim U(\mathcal H)}[D(x)\ne f(x)].
$$

For every high $f$, averaging its dual-margin inequality over descriptions gives

$$
\sum_x\mu_f(x)p_x(f)
=\mathbb E_{D\sim U(\mathcal H)}\Pr_{x\sim\mu_f}[D(x)\ne f(x)]
\ge 3/10.
$$

Hence $\max_x p_x(f)\ge3/10$.

Take $m=O(\log N)=O(n)$ independent uniform descriptions and let $\widehat q_x$ be their output-one frequency. For $\epsilon=3/40$, Hoeffding and a union bound over all $N$ coordinates show there exists a sample satisfying $|\widehat q_x-q_x|\le\epsilon$ for every $x$. Fix one such sample nonuniformly. For any input table $f$, its empirical disagreement frequency is

$$
\widehat p_x(f)=
\begin{cases}
\widehat q_x,&f(x)=0,\\
1-\widehat q_x,&f(x)=1.
\end{cases}
$$

Then $|\widehat p_x(f)-p_x(f)|\le\epsilon$ simultaneously for all $x$ and all truth tables $f$. If $\widehat x$ maximizes the empirical score, then

$$
p_{\widehat x}(f)\ge \max_x p_x(f)-2\epsilon\ge3/20.
$$

Only the $N$ integer frequencies $m\widehat q_x\in\{0,\ldots,m\}$ need to be hardwired. The score at each coordinate is one of two constants, chosen by the input bit $f(x)$. A tournament with fixed tie-breaking compares $N$ scores and returns a maximizing $n$-bit address using $O(N(n+\log m))=O(Nn)$ gates. The profile costs $O(N\log n)$ hardwired bits. The sampled circuit descriptions are used only to prove that a good profile exists; the selector does not evaluate them. This is an unconditional nonuniform upper bound for the first query.

## Conditional sample extension

For a transcript $\tau=((x_1,b_1),\ldots,(x_j,b_j))$, let

$$
A_\tau=\{D\in\mathcal H:D(x_i)=b_i\text{ for every }i\}.
$$

The same dual distribution works after conditioning: if $A_\tau\ne\varnothing$, averaging over $D$ uniform in $A_\tau$ shows that some coordinate is wrong on at least a $3/10$ fraction of the residual descriptions. Thus an ideal greedy process continues to contract the residual set.

There are at most $O((k+1)(2N)^{k+1})$ events of the forms $A_\tau$ and $A_\tau\cap\{D:D(x)\ne b\}$ for transcripts of length at most $k$. A uniform sample of size

$$
m=O\left(\frac{kn+\log(1/\eta)}{\delta^2}\right)
$$

approximates all these event probabilities to additive error $\delta$ with probability at least $1-\eta$. If $P(A_\tau)\ge\rho$, then taking $\delta\le\gamma\rho/16$, where $\gamma=3/10$, estimates each conditional error probability to within $\gamma/4$. An empirical maximizer then still eliminates a constant fraction of that residual.

This does not close the process. The required additive accuracy scales with the residual mass: the displayed sample size is $O((kn+\log(1/\eta))/(\gamma^2\rho^2))$. Once a residual cell has mass below $\rho$, the sample can contain no surviving description even while the exact version space remains nonempty. A generic sample meant to represent every nonempty cell of a finite description space can require dependence on the entire space; this is not evidence that all such rare cells are reachable within the OPS query budget. Nor does it constrain selectors that use a different architecture.

## Adversarial review and next theorem

- **Duplicates:** syntactic duplicates only set the prior weights; the margin applies to every description, so the first-step proof is unchanged.
- **All-zero or all-one marginals:** these cause no issue. A high $f$ must still have some coordinate where the corresponding empirical error frequency is large.
- **Advice and gates:** the fixed marginal profile uses $O(N\log n)$ bits and $O(Nn)$ gates. It is nonuniform and does not claim an efficient uniform procedure for constructing the profile.
- **Scope:** a query eliminating $3/20$ of descriptions is not an anti-checker; many descriptions can remain. The project's superlinear target concerns the full map from a high truth table to a short list.
- **Next target:** either construct conditional profiles down to exact emptiness below $N^{1+\epsilon}$ gate cost, prove a circuit-specific tail-elimination principle, or bypass version-space scoring with a direct universal-selector argument. Do not infer a lower bound for arbitrary selectors from the sample's rare-cell failure.

**Classification:** C-52 is proved first-query progress and a sharpened diagnosis of the adaptive rare-survivor bottleneck. It is not a P-vs-NP proof or a movement on O-1.


## C-53 — Relative sampling improves adaptive tracking

The additive Hoeffding estimate above is not optimal for the adaptive step. Let $\mathcal R_k$ contain all residual events $A_\tau$ and all one-query elimination events $A_\tau\cap\{D:D(x)\ne b\}$ for transcripts of length at most $k$. Its size is at most $O((k+1)(2N)^{k+1})$, so $\log|\mathcal R_k|=O((k+1)n)$.

Fix $0<\rho\le1$ and the margin $\gamma=3/10$. Set $\lambda=\gamma\rho/8$. Multiplicative Chernoff bounds and a union bound give a uniform sample of size

$$
m=O\left(\frac{(k+1)n+\log(1/\eta)}{\gamma\rho}\right)
$$

such that, simultaneously for every event in $\mathcal R_k:$
1. every residual event of probability at least $\rho$ is estimated within relative error $1/4$;
2. every elimination event of probability at least $\lambda$ is estimated within relative error $1/4$; and
3. every elimination event of probability below $\lambda$ has empirical frequency below $2\lambda=\gamma\rho/4$.

For a residual $A_\tau$ of true mass $r\ge\rho$, the dual margin averaged over its descriptions supplies a coordinate whose disagreement event has mass $a\ge\gamma r$. Its estimate is at least $3a/4\ge3\gamma r/4$. If a coordinate with true mass below $\gamma r/2$ had score at least this value, then either its relative estimate would be at most $5\gamma r/8$, or (below $\lambda$) its empirical frequency would be below $\gamma r/4$. Both are contradictions. Thus the empirically best coordinate eliminates at least a $\gamma/2$ fraction of the exact residual. Because the sample guarantee holds for all transcript ranges at once, this remains valid along an adaptive path while the residual mass stays at least $\rho$.

This improves the additive-sampling requirement from $O(1/\rho^2)$ to $O(1/\rho)$ for constant $\gamma$. With a sample of polynomial size one can track residuals down to inverse-polynomial mass. But constant-factor contraction takes only $O(\log(1/\rho))=O(n)$ rounds before the residual mass drops below that threshold, unless it has already become empty. To guarantee continuation whenever any description survives, set $\rho=1/|\mathcal H|$; the sample bound then scales as $|\mathcal H|\,\mathrm{poly}(n,\log|\mathcal H|)$. The circuit class contains at least $\binom{N}{r}$ distinct low functions for $r=\Theta(s_1/n)$ via sparse point-set DNFs, so $\log|\mathcal H|=\Omega(N^\beta/n)$ and this generic full-tail sample is superpolynomial in $N$.

**Scope.** This is a sharper analysis of one global-sample/greedy architecture, not a lower bound for every selector. It does not prove that rare residual cells are reached on high inputs, and a different circuit could avoid tracking their masses. It does show that the obvious relative-sampling upgrade still leaves the same exact-emptiness bottleneck.


## C-54 — The polynomial-threshold prefix ends at a forced nonempty residual

The C-53 guarantee cannot finish the list after only a polynomial-threshold sample. First, a direct interpolation fact applies to every consistent transcript: if it contains $q$ distinct points, the DNF formed by OR-ing minterms for the points labeled 1 matches all transcript labels and has size $O(qn)$. Consequently every transcript of length $q\le q_0=\Omega(s_1/n)=\Omega(N^\beta/n^2)$ has a size-$s_1$ circuit consistent with it. In particular, for fixed $\beta>0$, no transcript of $O(n)$ queries can be an anti-checker for sufficiently large $n$.

Now fix any constant $a>0$ and let the C-53 relative sample track residual masses down to $\rho=N^{-a}$. While the exact residual mass $r$ is at least $\rho$, each selected point reduces it by a factor at most $1-\gamma/2$. Thus the first crossing below $\rho$ occurs within
$$
K=\left\lceil\frac{\ln(1/\rho)}{-\ln(1-\gamma/2)}\right\rceil+1=O(n)
$$
queries, unless the version space has already become empty. But $K<q_0$ for all sufficiently large $n$, so interpolation rules out emptiness. Therefore the guaranteed phase of this sample-based greedy method reaches a nonempty residual below the inverse-polynomial mass threshold.

For a fixed $a$, C-53 uses $m=O(n^2N^a)$ descriptions through this $K=O(n)$ depth. Directly evaluating all sample scores at every round has a nonuniform circuit implementation of size $O(KNm\log m+Kms_1+KNn)=N^{1+a}\operatorname{poly}(n)$; it fits $N^{1+\epsilon}$ for any $\epsilon>a$. This gives a rigorously near-linear prefix selector, but the prefix is much shorter than the $\Omega(s_1/n)$ queries required before any transcript can be an anti-checker. It does not show that the selector cannot continue by another mechanism. The precise conclusion is that relative global sampling loses its proof guarantee at a residual known to be nonempty.


**Published parameters.** The gap thresholds used here are those of the OPS Anti-Checker Lemma: low size $2^{\beta n}/(10n)$, high threshold $2^{\beta n}$, and list budget $2^{10\beta n}$; see [Oliveira, Pich, and Santhanam, Lemma 4.1](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf).
