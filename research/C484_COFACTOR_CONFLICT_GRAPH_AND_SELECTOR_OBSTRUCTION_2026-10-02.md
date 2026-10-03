# C-484 — Cofactor conflicts give a real gate bound, but only a linear ceiling

**Date:** 2 October 2026  
**Status:** Exact lower-bound lemma for every total separator; route fails to reach superlinear size, with a shared-selector counterconstruction. No full-promise near-linear separator found.

## 1. Target and model

Let $N=2^n$, $s_1=\lfloor N^\beta/(10n)\rfloor$, and $s_2=N^\beta$, for sufficiently small fixed $\beta>0$. Define

$$
U=\{T\in\{0,1\}^N:CC_n(T)\le s_1\},\qquad
V=\{T\in\{0,1\}^N:CC_n(T)>s_2\}.
$$

An admissible $F$ is any total fan-in-two AND/OR/NOT circuit with $F(U)=1$ and $F(V)=0$; middle labels are free. Its size $S$ counts every gate, permits unrestricted fan-out, and does not count wires as gates. The OPS magnification target is one fixed $\epsilon>0$ for every sufficiently small fixed $\beta$, with $S>N^{1+\epsilon}$. The exact gap parameters and consequence were checked in C-476 against [Oliveira–Pich–Santhanam, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf).

## 2. Mechanism: forced cofactor conflicts

Choose any coordinate set $A\subseteq[N]$ and let $B=[N]\setminus A$. For $a\in\{0,1\}^A$, write

$$
F_a(b)=F(a,b),\qquad b\in\{0,1\}^B.
$$

Define the **forced cofactor-conflict graph** $G_A(U,V)$. Its vertices are assignments $a\in\{0,1\}^A$. Join $a,a'$ when some common completion $b$ gives a forced opposite pair:
$$
((a,b)\in U\ \wedge\ (a',b)\in V)
\quad\text{or}\quad
((a,b)\in V\ \wedge\ (a',b)\in U).
$$

Every admissible $F$ maps adjacent vertices to different residual functions: at that $b$, one cofactor is 1 and the other is 0. Thus $a\mapsto F_a$ is a proper coloring, so
$$
\chi(G_A(U,V))\le |\{F_a:a\in\{0,1\}^A\}|.
$$

**Support lemma.** A fan-in-two circuit of $S$ gates depends on at most $2S+1$ primary inputs. Every supported input except for the direct-output case must enter a reachable gate through one of its at most $2S$ input pins. If two assignments to $A$ agree on the supported coordinates in $A$, their cofactors are identical. Consequently,
$$
|\{F_a\}|\le 2^{|A\cap\operatorname{supp}(F)|}
\le 2^{\min(|A|,\,2S+1)},
$$
and every valid separator obeys
$$
\boxed{S\ge \frac{\log_2\chi(G_A(U,V))-1}{2}.}
$$

This is an all-extension statement: it uses only the forced endpoints and allows any middle-band behavior. It counts ordinary total gates, not paid AND states or runtime.

## 3. Why this cannot magnify by itself

There are only $2^{|A|}\le 2^N$ graph vertices. Hence $\log_2\chi(G_A)\le N$, and this one-cut mechanism can force at most $S\ge (N-1)/2$. It cannot yield $N^{1+\epsilon}$ for any $\epsilon>0$, even if $G_A$ is complete. Combining several cuts would require an additive gate charge; a gate can participate in many restrictions, and no such charge is proved here.

The stronger invalid proposal—charge one new gate for each distinct cofactor—is false. Let
$$
f_k(a,b)=\bigvee_{i=1}^k(a_i\wedge b_i).
$$
This circuit has $k$ AND gates and $k-1$ OR gates, hence $2k-1$ total gates. Fixing $a$ to the indicator of $Q\subseteq[k]$ yields the cofactor $\bigvee_{i\in Q}b_i$. All $2^k$ such functions are distinct, including the empty OR. One shared selector circuit therefore represents exponentially many residual states with only $O(k)$ gates. State multiplicity is not gate count.

## 4. Hostile tests

| Pattern | Cheapest shared computation / cofactor behavior | What it rules out |
|---|---|---|
| Parity | An $m$-bit parity has $O(m)$ gates. After fixing any $k$ variables, there are only two residual functions: parity on the remaining bits or its complement. | Counting restriction assignments as distinct residual information. |
| Repeated-block equality | For $r$ blocks of $b$ bits, compare each block with the first and AND the equalities, using $O(rb)=O(N)$ gates. Fixing the first block gives $2^b$ distinct residual predicates on the remaining blocks. | Charging each residual predicate or repeated comparison as an independent gate. |
| Sparse parity checks | For an $r\times N$ binary matrix with $I$ nonzero entries, compute all row parities and combine them in $O(I+r)$ Boolean gates. Fixing $A$ changes the syndrome by $H_Aa$, so the residual family has at most $2^{\operatorname{rank}(H_A)}$ syndrome shifts, yet it is represented by this shared circuit. | Treating check count or the number of cofactor states as computation cost. |
| Simple globally related blocks | Given generator bits $z$, generate or check blocks $x^{(j)}=z\oplus c_j$ with $O(N)$ XOR-simulation gates and fan-out. Fixing generator bits can produce exponentially many different residual checks. | Charging output positions, repeated relations, or residual diversity without paying for shared generator logic. |

These are counterexamples to generic state-multiplicity charging. They are not counterexamples to an OPS separator lower bound: none of these functions is proved to accept every table in $U$ and reject every table in $V$.

## 5. Paired construction attempt and model ledger

I tried to use the cofactor view to share work in a complete separator by grouping size-$s_1$ circuit candidates according to their restrictions on $A$. The exact safe implementation still enumerates all $K=2^{O(N^\beta)}$ candidate descriptions, compares each candidate with the $N$ input bits, and ORs the equality flags. It has $O(NK)=O(N2^{O(N^\beta)})$ total gates. A prefix trie or cofactor cache has at most $NK$ candidate-position pairs in the direct construction; no $O(N\operatorname{polylog}N)$ or other near-linear cost was proved. This remains a valid full-promise upper, not a compression.

| Resource | Accounting in this cycle |
|---|---|
| Total gates | Every AND/OR/NOT counted; all bounds above use this measure. |
| Fan-out and wires | Fan-out can reuse gate outputs; the selector counterexample uses that reuse. Wires are not gates. |
| Cofactor labels | Counting residual functions is not equivalent to counting circuit gates. |
| Paid AND states / native fusion | Not used; no native $\rho$ consequence is claimed. |
| Runtime / description bits | Neither substitutes for total-gate size. Candidate descriptions are counted in $K$, and comparisons in $NK$. |

## 6. Literature, originality, and exact frontier effect

The cofactor-conflict graph and support bound are elementary restriction arguments; this report claims no literature novelty. Chen et al.'s locality barrier concerns lower-bound techniques that remain effective with small-fan-in oracle gates; it neither proves this cofactor argument impossible nor makes it an escape route. No oracle-resilience theorem was established here. [Chen et al., *Beyond Natural Proofs: Hardness Magnification and Locality*](https://arxiv.org/abs/1911.08297).

**Strongest proved statement:** for every $A\subseteq[N]$, every valid separator of $S$ total gates satisfies
$$
S\ge\frac{\log_2\chi(G_A(U,V))-1}{2}.
$$
The proof is exact and applies to arbitrary shared circuits.

**Quantitative effect: none.** The bound is capped by $(N-1)/2$, below the fixed-$\epsilon$ OPS target. The ordinary essential-input lower bound remains $N-O(N^\beta\log N)$, with C-406's recorded refinement; the exact full-promise upper remains $O(N2^{O(N^\beta)})$. No near-linear full-promise separator, superlinear ordinary-gate lower bound, native-fusion bound, or P-vs-NP proof was obtained.

**Route change:** retire one-cut cofactor diversity and raw residual-state counting as superlinear mechanisms. Reopen only if a new argument prices the jointly selected cofactor family by total gates across many cuts with a proved no-double-counting rule. The next route must measure joint selector complexity, not residual-label count.

