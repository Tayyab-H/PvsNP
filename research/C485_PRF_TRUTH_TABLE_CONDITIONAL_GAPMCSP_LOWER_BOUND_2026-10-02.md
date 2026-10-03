# C-485 — PRF truth tables instantiate the hard-YES route conditionally

**Date:** 2 October 2026  
**Status:** parameter-checked conditional lower bound for ordinary Gap-MCSP separators. It is not unconditional and is not claimed as a new PRF technique.

## 1. Exact statement

Let $N=2^n$, $s_1=\lfloor N^\beta/(10n)\rfloor$, and $s_2=N^\beta$, for a fixed $0<\beta<1$. Assume a keyed family
$$
P_\lambda:\{0,1\}^{\lambda}\times\{0,1\}^{\lambda}\to\{0,1\}
$$
with:

1. an AND/OR/NOT evaluation circuit of size at most $A\lambda^d$ for every key and input, for constants $A$ and $d\ge1$ (increase $d$ if needed); and
2. pseudorandom-function security against **nonuniform** Boolean oracle circuits of every fixed polynomial size and query bound in $\lambda$.

Then, for every fixed $\epsilon>0$, no family of total AND/OR/NOT circuits of size at most $N^{1+\epsilon}$ can separate all tables of complexity at most $s_1$ from all tables of complexity greater than $s_2$, for all sufficiently large $n$.

The nonuniform security clause is essential: a Gap-MCSP separator is itself a nonuniform circuit family. Uniform-only PRF security does not rule it out.

## 2. Proof with the parameters charged

Choose a constant $\delta>0$ with $\delta d<\beta$, and for each $N=2^n$ let $\lambda=\lceil N^\delta\rceil$. For all sufficiently large $n$, $\lambda>n$. Map an address $x\in\{0,1\}^n$ injectively to the $\lambda$-bit string $0^{\lambda-n}x$. For a key $K$, define the $N$-bit table
$$
T_K[x]=P_\lambda(K,0^{\lambda-n}x).
$$

**Every generated table is Low.** Hardwire $K$ into the evaluation circuit and pad its address input. Thus
$$
CC_n(T_K)\le A\lambda^d+O(\lambda)
           =O(N^{\delta d})\le \lfloor N^\beta/(10n)\rfloor=s_1
$$
for sufficiently large $n$, since $\beta-\delta d>0$.

Suppose $F_N$ were a valid separator of size $N^{1+\epsilon}$. A nonuniform oracle distinguisher queries the PRF on the $N$ padded addresses, forms the truth table, and runs $F_N$. Its query count, query wiring ($O(N\lambda)$ bits), and total circuit size are polynomial in $\lambda$: $N=\lambda^{1/\delta+o(1)}$ and $N^{1+\epsilon}=\lambda^{(1+\epsilon)/\delta+o(1)}$. The geometrically growing sequence of $\lambda$ values has an infinite strictly increasing subsequence, on which the advice can contain the corresponding $F_N$. On every PRF key it accepts, because $T_K\in L_{s_1}$.

For a uniformly random truth table $R$, validity forces $F_N(R)=0$ whenever $CC_n(R)>s_2$. Hence its acceptance probability is at most
$$
\Pr[F_N(R)=1]\le \frac{|L_{s_2}|}{2^N}
\le 2^{-N+O(s_2\log(N+s_2))}
=2^{-N+o(N)}.
$$
The circuit-counting bound includes every size-$s_2$ table, and $s_2\log(N+s_2)=O(N^\beta\log N)=o(N)$. The distinguisher therefore has advantage $1-2^{-N+o(N)}$, contradicting the assumed PRF security. This proves the conditional statement.

The same argument rules out any fixed polynomial size $N^c$ separator family, by replacing $1+\epsilon$ with $c$; the resulting oracle circuit is still polynomial in $\lambda$. The exponent $\delta$ can be chosen once for each fixed $\beta$ from the evaluation exponent $d$.

## 3. Hostile tests and scope

Parity checks, Hamming-weight tests, repeated-block equality, sparse parity checks, and simple global-relation tests all have polynomial-in-$N$ circuit size. If any such test separated the PRF-table distribution from uniform with non-negligible advantage, it would already violate the assumed PRF security. So this construction passes those ensemble screens *conditionally*. This says nothing about a concrete PRF absent the security assumption, and it does not give a full-promise separator.

The exact full-promise upper attempt remains the Low-description enumerator: enumerate $K_0=2^{O(N^\beta)}$ Low circuit descriptions, compare each with all $N$ table bits, and OR the matches, costing $O(N2^{O(N^\beta)})$ total gates. The PRF argument does not compress this circuit; it only shows that any much smaller separator would break the assumed PRF.

## 4. Literature and model audit

The basic implication “an efficient MCSP test distinguishes pseudorandom-function tables from random tables” is established literature, not a novelty claim. The primary MCSP lower-bound paper explicitly describes this route and notes that prior restricted-model lower bounds exploit PRGs secure against AC$^0$ or formula tests; it also develops a different coin-problem route for AC$^0[p]$. [Golovnev et al., ECCC TR19-018](https://eccc.weizmann.ac.il/report/2019/018/). C-485's project-specific contribution is to charge the key/address/evaluation parameters against this project's exact $s_1,s_2$ and nonuniform total-gate separator.

Recent conditional hardness for Gap-Implicit-MCSP uses a different input representation (a sampler of labeled examples) and assumptions involving indistinguishability obfuscation and proof systems; it does not transfer to this explicit truth-table, ordinary-circuit target. [ECCC TR26-091](https://eccc.weizmann.ac.il/report/2026/091/).

| Resource | Accounting |
|---|---|
| Table generator | Per-key address circuit costs $A\lambda^d+O(\lambda)\le s_1$. |
| Separator | Counts all AND/OR/NOT gates; the hypothesized $N^{1+\epsilon}$ family becomes polynomial in $\lambda$. |
| PRF tester | Makes $N$ oracle queries and applies the separator; total size/query count are polynomial in $\lambda$. |
| Descriptions and wires | Nonuniform advice includes the separator description. No wires or runtime are used as free gates in its size. |
| Native fusion | Not used; no $\rho$ consequence follows. |

## 5. Exact effect and first-principles lesson

**Strongest proved statement:** under the stated nonuniform PRF assumption, the exact OPS separator family does not have $N^{1+\epsilon}$ total gates; in fact it has no fixed-polynomial-size family. The parameter proof respects the complete promise and uses only Low YES outputs plus the counting bound on the separator's accepting set under uniform input.

**Unconditional frontier: unchanged.** No PRF security against these nonuniform tests has been proved unconditionally. Assuming it is cryptographic input and cannot be presented as a proof of $P\ne NP$. The known natural-proofs and black-box barriers explain why broad constructive tests can conflict with PRFs; they are warnings about proof methods, not universal impossibility theorems. [Razborov–Rudich](https://eccc.weizmann.ac.il/report/1994/010/), [Fan–Li–Yang](https://eccc.weizmann.ac.il/report/2021/125/).

**Research update:** the earlier distributional sufficient condition is now met under an explicit cryptographic hypothesis and exact OPS parameters. This closes only the conditional version of that route. An unconditional proof must build comparable pseudorandomness from a theorem, not assume it; alternatively return to an all-extension gate inequality or a promise-saturated reduction. The ordinary lower and exact enumerative upper remain unchanged.

