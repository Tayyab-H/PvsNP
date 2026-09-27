# Range audit for Krajíček's theory generator

**Status:** conditional proof for the theorem-consistent, one-bit-stretch interpretation of the construction. This does not prove $P\ne NP$. The published source has an off-by-one inconsistency that must be resolved before treating the result as a correction to the literature.

## Proposition

Fix a p-time first-order theory $T\supseteq S^1_2$. Interpret Krajíček's construction with its stated one-bit stretch and Theorem 2.2: if the parsed input prefix is a formula Φ of length $c$, the construction searches over prefixes $w\in\{0,1\}^{c+1}$. For every input length $n$, the resulting range on $n$-bit inputs is decidable in time polynomial in $n$.

Consequently, the complement of the full range is an infinite $P$ language disjoint from the range. Thus this specific theory-driven family cannot intersect every infinite $NP$ language, for any fixed $T$, under this interpretation.

## Proof

Fix an input length $n$, and let $L=\lfloor\log_2 n\rfloor$. Enumerate all binary strings of length at most $L$, retaining exactly those that are valid encodings of one-free-variable formulas. There are fewer than $2^{L+1}\le 2n$ candidates. The paper assumes formula codes are prefix-free.

For a candidate formula Φ of length $c\le L$, all decisions in Step 2 depend only on $n$ and Φ:

1. Enumerate the $2^{c+1}\le 2n$ strings $w\in\{0,1\}^{c+1}$.
2. For each $w$, enumerate all proof strings of size at most $L$, fewer than $2^{L+1}\le2n$ under the standard finite-alphabet encoding.
3. Check whether any candidate is a valid $T$-proof of Φ^w.

For fixed $T$, proof checking is polynomial time: the paper treats a p-time theory as a polynomial-time decidable set of sentences, so each axiom/line test uses that fixed membership predicate; standard derivation checking is polynomial in the proof and formula encoding lengths. Equivalently, one may use the fixed p-time axiomatization of $T$. The construction of Φ^w is polynomial in $n$. There are polynomially many formula, prefix, and proof candidates, so the branch and, when applicable, its first unproved prefix $w_\Phi$ are computable in polynomial time.

If the branch for Φ is normal, every seed in its entire cylinder

The input cylinder is $\Phi\{0,1\}^{n-c}$.

It maps to the output cylinder $w_\Phi\{0,1\}^{n-c}$,

because the algorithm emits $w_\Phi$ and copies the remaining suffix unchanged. The lengths agree: $(c+1)+(n-c)=n+1$. Since formula codes are prefix-free, each such input cylinder has exactly $2^{n-c}$ members and distinct formula cylinders are disjoint.

Now decide whether a given $y\in\{0,1\}^{n+1}$ belongs to the range:

1. Compute the branch for every eligible formula Φ. If a normal branch has $w_\Phi$ as a prefix of $y$, accept. A preimage is explicit: let $s$ be the suffix of $y$ after $w_\Phi$, and use seed $\Phi s$. It has length $n$, parses the same Φ by prefix-freeness, and outputs $y$.
2. Otherwise, $y$ can be in the range only through the default output $0^{n+1}$. Let

   $q_n=\sum_{\Phi\ \mathrm{eligible\ and\ normal}}2^{n-|\Phi|}$.

   The normal formula cylinders are disjoint, so $q_n$ is exactly the number of seeds taking normal branches. A default seed exists iff $q_n<2^n$. This count includes formula classes taking a default branch and inputs with no eligible formula prefix. Accept $0^{n+1}$ exactly when a default seed exists; reject all other strings.

The candidate loops are polynomial in $n$, and the count uses $O(n)$-bit integers over polynomially many terms. Thus the length-$(n+1)$ range-membership problem is in $P$. Hard-code the finitely many small lengths.

For each $n$, a function from $2^n$ seeds has at most $2^n$ outputs among $2^{n+1}$ strings. Hence at least $2^n$ strings of length $n+1$ are outside the range. The complement is infinite; by the range decider it is in $P\subseteq NP$, and it is disjoint from the range. This disproves universal $NP$-hitting for this construction. By Theorem 2.2, no definition of this complement can have all its true Φ^w tail sentences provable in $T$.

## Source discrepancy and scope

The published Step 2 sets $c:=|\Phi|+1$ and then takes $w\in\{0,1\}^{c+1}$, so its $w$ has length $|\Phi|+2$. Step 3 nevertheless claims output length $n+1$ after concatenating $w$ with the entire suffix $u_0$, which would have length $n+2$. Lemma 2.1 claims one-bit stretch, and Theorem 2.2 explicitly uses $w\in\{0,1\}^{c+1}$ with $c=|\Phi|$. The proposition above follows that theorem- and stretch-consistent convention, $|w|=|\Phi|+1$. The journal version still describes Problem 2.4 as open. The mismatch and the apparent consequence should receive an independent specialist audit before being presented as a literature correction.

This is a structural result about the published suffix-copy construction only. It neither proves nor refutes the existence of a different polynomial-time map whose range intersects every infinite $NP$ set, and it does not imply either $P=NP$ or $P\ne NP$.

## Primary sources

- [Krajíček, arXiv version, construction and Theorem 2.2](https://arxiv.org/html/2303.10637)
- [Krajíček, Journal of Symbolic Logic version, DOI 10.1017/jsl.2023.69](https://doi.org/10.1017/jsl.2023.69)
