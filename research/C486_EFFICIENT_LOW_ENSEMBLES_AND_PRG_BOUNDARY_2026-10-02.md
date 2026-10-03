# C-486 — efficiently samplable Low ensembles hit a cryptographic boundary

**Date:** 2 October 2026  
**Status:** exact parameter implication for the strong distributional route; does not replace the weaker separator-specific condition and does not change the unconditional frontier.

## 1. Statement

Fix $0<\beta<1$, $N=2^n$, and $s_1=\lfloor N^\beta/(10n)\rfloor$. Let $m=\Theta(s_1\log(n+s_1))=\Theta(N^\beta)$ be enough bits to encode every fan-in-two circuit of at most $s_1$ gates on $n$ address bits.

Suppose a **uniform polynomial-time** generator
$$
G_n:\{0,1\}^{m}\to\{0,1\}^{N}
$$
has the following properties:

1. for every seed $z$, the output is the truth table of a function of circuit complexity at most $s_1$; and
2. the output distribution is computationally indistinguishable from uniform with negligible advantage against every nonuniform polynomial-size circuit in $m$.

After filling the geometrically spaced seed lengths by ignoring a constant-factor suffix of seed bits, this is a conventional pseudorandom generator with polynomial stretch $N=m^{1/\beta+o(1)}$. Consequently, the standard PRG-to-one-way-function implication applies.

This is a classification of a **strong sampler route**, not an equivalence with the OPS lower bound.

## 2. Proof and resource accounting

A description of an at-most-$s_1$ gate circuit on $n$ inputs uses
$$
O(s_1\log(n+s_1))=O(N^\beta)
$$
bits: each gate records its type and at most two predecessors among the $n$ inputs and previous gates. A fixed-length encoding can map every seed to a valid description, for example by reducing predecessor fields modulo the available earlier wires. Thus the uniform distribution on descriptions is an efficiently samplable distribution supported on $L_{s_1}$.

Given a description, evaluate its circuit on all $N=2^n$ addresses to produce the truth table. The direct sampler costs $O(Ns_1\operatorname{poly}(n))$ time or gates, which is polynomial in $m$ for each fixed $\beta$, since $N=m^{1/\beta+o(1)}$. The seed-to-output stretch is polynomial, and the assumed negligible indistinguishability against every polynomial-size test in $m$ is exactly the pseudorandom-generator requirement.

A size-$N^{1+\epsilon}$ separator is one polynomial-size test in $m$, because
$$
N^{1+\epsilon}=m^{(1+\epsilon)/\beta+o(1)}.
$$
As C-485 showed, its advantage on a Low-supported distribution versus uniform would be $1-2^{-N+o(N)}$. So the strong PRG condition rules out such separators, but it imports cryptographic hardness through the generator.

## 3. Why this does not close the distributional route

The C-481 sufficient condition only needs a distribution that prevents the target separators from having near-unit advantage; it does not require a uniform sampler or negligible advantage against **every** polynomial-size circuit. Therefore C-486 does not show that every possible hard-YES distribution implies one-way functions.

The natural uniform sampler over short circuit descriptions is only a candidate distribution. Sampling Low circuits is easy; proving that their truth tables fool large circuits is the hard part. C-481's affine-function ensemble is a concrete warning: every sampled table has an $O(n)$-gate address circuit, yet an $O(n)$-gate parity check on table coordinates accepts the ensemble and half of uniform tables. Low support and efficient sampling alone give no pseudorandomness.

## 4. Paired full-promise construction and exact frontier

The complete separator remains the explicit codebook test: enumerate $K=2^{O(N^\beta)}$ descriptions of circuits of size at most $s_1$, compare the input table against every candidate at all $N$ coordinates, and OR the equality flags. This is a valid separator of size $O(N2^{O(N^\beta)})$. C-486 gives no compression and no lower bound on this upper construction.

**Strongest proved statement:** an efficiently samplable Low-table ensemble with negligible indistinguishability against every polynomial-size circuit in its $m=\Theta(N^\beta)$ seed length is a polynomial-stretch PRG, hence yields one-way functions. This conclusion requires the stronger negligible-security condition stated above.

**Unconditional quantitative effect: none.** The ordinary lower bound remains $N-O(N^\beta\log N)$ essential inputs with the C-406 refinement; the exact full-promise upper is still $O(N2^{O(N^\beta)})$. The OPS fixed-$\epsilon$ target, native $\rho$ target, and P-vs-NP remain open.

## 5. Literature and next-route decision

The PRG/one-way-function equivalence is standard; see [Håstad, Impagliazzo, Levin, and Luby, *A Pseudorandom Generator from Any One-Way Function*](https://www.cs.bu.edu/fac/lnd/pdf/hill.pdf). C-485 and C-486 do not claim novelty for that equivalence or for MCSP's ability to distinguish pseudorandom truth tables from uniform tables.

**Route decision:** do not spend the next cycle merely inventing another efficient sampler over small circuits and hoping it is pseudorandom. A successful strong sampler would already be cryptographic. The constructive distribution path remains open only at the weaker separator-specific security level or through a genuinely new nonconstructive argument. In parallel, continue seeking the direct all-extension total-gate inequality or a promise-saturated source reduction; no assumed non-shareability principle is acceptable.

