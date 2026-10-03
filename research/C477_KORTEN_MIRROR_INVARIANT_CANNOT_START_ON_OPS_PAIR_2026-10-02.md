# C-477 — Korten's mirror-set invariant cannot initialize on the raw OPS endpoints

**Date:** 2 October 2026  
**Status:** a quantitative, route-specific obstruction to applying the new fixed-depth parity adversary directly to the OPS Karchmer–Wigderson pair. No OPS lower-bound improvement or full-promise upper improvement.

## 1. The proposed transfer

For $N=2^n$, fix $0<\beta<1$ and the OPS thresholds

$$s_1=\left\lfloor\frac{N^\beta}{10n}\right\rfloor,\qquad s_2=N^\beta,$$

with forced endpoint sets $U=L_{s_1}$ and $V=\{T:CC_n(T)>s_2\}$. A valid separator yields a Karchmer–Wigderson rectangle DAG for $U\times V$ (C-476). The new candidate was to apply Oliver Korten's top-down parity adversary to this pair and turn its rectangle invariant into a lower bound on the shared-state DAG.

Korten's preprint gives two relevant mirror-set lemmas. The first uses the $p$-limit condition: for Bernoulli-$p$ free coordinates $P$, require $Y\cap[x]_P\ne\varnothing$ with probability at least $3/4$; it assumes $D_\infty(X)\le k$ and $q=64kp\le1$. The stronger version defines an $(p,k)$-limit by requiring $|Y\cap[x]_P|\ge2^{|P|-k}$ with probability at least $3/4$, and assumes $q=Ck^2p\le1/2$ for a universal constant $C$. The latter is used for the improved fixed-depth parity theorem. We test both versions below. [Korten, Sections 2--4](https://arxiv.org/abs/2609.38677)

## 2. OPS endpoint facts

### 2.1 Count and entropy deficit of the Low side

For a fixed fan-in-two basis, a circuit with at most $s_1$ gates has a topological description using at most

$$s_1\bigl(2\log_2(n+s_1)+O(1)\bigr)+O(\log(n+s_1))$$

bits: each gate chooses a type and two predecessors, and the circuit chooses an output. Since $\log_2(n+s_1)=\beta n-o(n)$, for each fixed $\beta$,

$$\log_2|U|\le(\beta/5+o(1))N^\beta=o(N).$$

Thus the min-entropy deficit of uniform $X\in U$ is

$$D_\infty(U)=N-\log_2|U|=N-o(N).$$

By contrast, $|V|=2^N-|L_{s_2}|=2^N-2^{o(N)}$, so $V$ has min-entropy deficit less than $1$ for sufficiently large $N$.

### 2.2 Every Low–High pair has a growing Hamming gap

Patching $d$ truth-table locations of a circuit for $u\in U$ costs at most $dn+n+3$ gates. Therefore every $u\in U$, $v\in V$ satisfies

$$d_H(u,v)\ge\Delta:=\max\!\left(0,\left\lceil\frac{s_2-s_1-n-3}{n}\right\rceil\right)=\Theta(N^\beta/n).$$

This is the exact C-414 distance bound. In particular, the gap $\Delta$ tends to infinity for every fixed $\beta>0$.

## 3. Proof that the mirror-set lemma has no valid starting orientation

For the lemma's left $p$-limit condition, the event $Y\cap[x]_P\ne\varnothing$ requires $P$ to contain the entire disagreement set of some opposite-endpoint pair.

### Orientation A: $X=U$, $Y=V$

If $x\in U$ and $V\cap[x]_P\ne\varnothing$, then $|P|\ge\Delta$. To satisfy a $3/4$ limit probability, Markov's inequality forces

$$pN=\mathbb E|P|\ge\tfrac34\Delta,
\qquad\text{so}\qquad p\ge\frac{3\Delta}{4N}=\Theta(N^{\beta-1}/n).$$

But the mirror-set lemma must use $k\ge D_\infty(U)=N-o(N)$ and $64kp\le1$, which forces $p\le(1+o(1))/(64N)$. These bounds conflict by a factor $\Theta(\Delta)\to\infty$. The sparse Low side cannot be the lemma's $X$.

### Orientation B: $X=V$, $Y=U$

The entropy condition permits $k=1$, so the mirror-set hypothesis requires $p\le1/64$. There exists a promised High table $v\in V$ at distance greater than $N/4$ from every Low table: the union of radius-$N/4$ Hamming balls around $U$ has size at most

$$|U|\,2^{H_2(1/4)N+o(N)}=2^{H_2(1/4)N+o(N)}=o(2^N),$$

while the unpromised middle set $L_{s_2}$ has size $2^{o(N)}$. For this $v$, the event $U\cap[v]_P\ne\varnothing$ requires $|P|>N/4$. Hence for every $p\le1/64$,

$$\Pr[U\cap[v]_P\ne\varnothing]\le\Pr[|P|>N/4]\le4p\le1/16,$$

again far below $3/4$. The dense High side cannot be the lemma's $X$ either.

### The strengthened $(p,k)$-mirror lemma

The same endpoint facts also rule out initializing Korten's stronger lemma on this pair. Its limit condition asks, with probability at least $3/4$, for at least $2^{|P|-k}$ opposite-side tables agreeing outside $P$; its parameter condition is $Ck^2p\le1/2$.

If $X=U$, then $k\ge D_\infty(U)=N-o(N)$. On every successful $P$, at least one Low--High pair agrees outside $P$, so $|P|\ge\Delta$. Thus $pN\ge3\Delta/4$, and
$$Ck^2p=\Omega(N^2\Delta/N)=\Omega(N\Delta)>1/2$$
for all sufficiently large $N$.

If $X=V$, use the High table $v$ above with $d_H(v,U)>N/4$. Any successful $P$ must have $|P|>N/4$. Moreover, because the intersection contains at least $2^{|P|-k}$ members of $U$ and $|U|=2^{o(N)}$, success forces
$$k\ge |P|-\log_2|U|>N/4-o(N).$$
The $3/4$ success probability and Markov's inequality give $pN\ge3N/16$, hence $p\ge3/16$. Consequently $Ck^2p=\Omega(N^2)>1/2$, again contradicting the lemma's parameter condition.

### The obstruction survives every nonempty subrectangle

A top-down adversary may first pass to a subrectangle, so it is useful to state the stronger form. Let $X\subseteq U$ and $Y\subseteq V$ be any nonempty sets. Write $k$ for the parameter used in either lemma; it must satisfy $k\ge D_\infty(X)$ and $k\ge1$. Since $X,Y$ are disjoint, any successful limit event requires $P\ne\emptyset$.

If the lemma takes $X\subseteq U$ as its entropy-controlled side, then $k\ge N-\log_2|U|=N-o(N)$. For the original lemma, $64kp\le1$ implies $pN\le N/(64k)=O(1)$ with limiting bound $1/64$, so $\Pr[P\ne\emptyset]\le pN<3/4$. For the strengthened lemma, $Ck^2p\le1/2$ implies $pN\le N/(2Ck^2)=O(1/N)$, also impossible.

Now take $X\subseteq V$, $Y\subseteq U$. Let $Z$ be the set of High tables at distance greater than $N/4$ from every member of $U$. The counting argument above gives $|V\setminus Z|=2^{0.811N+o(N)}$, so $|Z|=2^N-o(2^N)$. Split according to the lemma's chosen $k$. If $k\ge N/10$, the original condition gives $pN\le N/(64k)\le10/64<3/4$, contradicting the necessary event $P\ne\emptyset$. The strengthened condition gives $pN\le N/(2Ck^2)=O(1/N)$, with the same contradiction. If $k<N/10$, then $D_\infty(X)\le k$ implies $|X|>2^{0.9N}$, hence $X\cap Z\ne\emptyset$. Fix $v\in X\cap Z$. In the original lemma, success requires $|P|>N/4$, so $p\ge3/16$, while $64kp\le1$ gives $p\le1/64$. In the strengthened lemma, success requires both $|P|>N/4$ and $2^{|P|-k}\le|U|$, forcing $k>N/4-o(N)$, contrary to $k<N/10$. Thus neither version can be initialized on any nonempty subrectangle of $U\times V$, in either orientation.

Together these calculations rule out initializing either published mirror-set invariant on the OPS pair, even after restricting to any nonempty subrectangle, in either orientation. The obstruction combines the exact Low–High distance margin with the extreme entropy imbalance; it is not merely that Korten's theorem happens to mention parity.

## 4. What the obstruction does and does not establish

**Proved:** neither the original $p$-limit mirror-set lemma nor the strengthened $(p,k)$-limit mirror-set lemma can be initialized on any nonempty subrectangle $X\times Y$ with $X\subseteq U$ and $Y\subseteq V$. For the original lemma, the Low orientation makes $kp\gg1$ and a far High point defeats every $p$ allowed in the High orientation. For the stronger lemma, the required $Ck^2p$ exceeds its allowed constant in both orientations. Thus Korten's fixed-depth parity results do not transfer directly through either published mirror-set invariant.

**Not proved:** no impossibility theorem for all top-down arguments, all asymmetric rectangle potentials, or all DAG-state lower bounds. A new invariant could use the small description entropy of $U$ and the growing margin $\Delta$ without importing the mirror-set lemma. It would still need to charge distinct shared states rather than path unfoldings.

## 5. Counterchecks and paired construction

The usual sharing canaries remain unchanged: parity, repeated-block equality, linear-incidence sparse parity checks, and simple global block relations all have $O(N)$-gate readouts on their induced families. They do not satisfy the full Low-completeness/High-soundness requirement and do not refute the OPS target.

The complete separator control is still the exact enumeration $F(T)=\bigvee_{C:|C|\le s_1}[T=C]$, with $O(N\,2^{O(N^\beta)})$ total gates. C-474 rules out substantial compression through a balanced sketch with fewer than $N-O(N^\beta\log N)$ bits. No near-linear full-promise separator was constructed here.

## 6. Exact frontier and route change

**Quantitative effect: none.** Ordinary separator lower bound remains $N-O(N^\beta\log N)$ essential inputs plus C-406's additive logarithmic reconvergence refinement. The fixed-$\epsilon$ OPS target remains open. Exact full-promise upper remains $O(N\,2^{O(N^\beta)})$. Native $\rho_{GapMCSP}\ge N-o(N)$ is separate. No P-vs-NP conclusion follows.

Retire the direct Korten mirror-set transfer and do not keep tuning its $p$-parameters. The next lower-bound mechanism must handle the OPS pair's sparse/dense endpoint asymmetry and its $\Delta=\Theta(N^\beta/n)$ local gap from the start, or move to a different source map or gate-semantic invariant. The immediate construction test remains a full-promise near-linear separator, with gates, wires, description, and runtime kept separate.

### Primary sources

- Oliveira, Pich, and Santhanam, [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4.
- Korten, [*Top-Down Lower Bounds for All Depths*](https://arxiv.org/abs/2609.38677), Lemma 2, Lemma 5, and Theorem 3.
- Project patching proof and exact distance parameter: [C-414](C414_PROMISE_EMBEDDING_SUPPORT_CAPACITY_NO_GO_2026-09-30.md).
