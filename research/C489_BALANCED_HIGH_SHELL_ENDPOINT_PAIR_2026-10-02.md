# C-489 - Balanced high shells around every balanced Low table

**Date:** 2 October 2026  
**Status:** proved a weight-preserving endpoint-pair construction by counting; no circuit lower-bound improvement.

## 1. Target and relation to prior work

For (N=2^n), fixed (0<\beta\le1/4), let (s_1=\lfloor N^\beta/(10n)\rfloor) and (s_2=N^\beta). Low tables have circuit size at most (s_1); High tables have size greater than (s_2).

C-458 already proved a two-sided patching bound: changing one truth-table entry costs (O(n)) gates, so every Low/High pair differs in at least \(\Omega(s_2/n)\) entries. C-344 already used circuit counting to show that a sphere of radius (K s_2) around a fixed Low table contains at least one High table. C-489 strengthens the latter fact in a form useful for the endpoint-pair route: around **every balanced Low table**, almost every neighbor in a suitable radius-(\Theta(s_2)) shell is High, while preserving exact Hamming weight.

The perturbation estimate is also stated explicitly in a 2026 note, although its one-point (O(n)) bound was implicit in earlier MCSP arguments. [Krinkin, 2026 preprint](https://arxiv.org/abs/2603.09379). C-489 does not claim novelty for the patching bound or the unrestricted-radius existence argument.

## 2. Theorem: almost all balanced shell neighbors are High

Call an (N)-bit table balanced if it has Hamming weight (N/2). Let

\[
t=2\lceil 2s_2\rceil,
\]

so (t) is even and (t=(4+o(1))s_2). For any balanced table (T), define its weight-preserving shell

\[
\mathcal S_t(T)=\{T':\mathrm{wt}(T')=N/2,\ d_H(T,T')=t\}.
\]

It is obtained by choosing (t/2) one-positions of (T) to flip to zero and (t/2) zero-positions to flip to one, hence

\[
|\mathcal S_t(T)|=\binom{N/2}{t/2}^{2}.
\]

**Theorem.** For every fixed (0<\beta\le1/4), all sufficiently large (n), and every balanced (T\in\{0,1\}^N),

\[
\Pr_{T'\sim\mathrm{Unif}(\mathcal S_t(T))}[\mathrm{CC}_n(T')\le s_2]
\le 2^{-\Omega(s_2 n)}.
\]

In particular, at least a \(1-2^{-\Omega(s_2n)}\) fraction of the shell is promised High.

**Proof.** A fan-in-two circuit on (n) inputs with at most (s_2) gates has a description consisting of its gate types and predecessor indices. A direct description count gives

\[
|L_{\lfloor s_2\rfloor}|
\le (s_2+1)(n+s_2+1)[5(n+s_2)^2]^{s_2}.
\]

Since \(\log_2(n+s_2)=\beta n+o(n)\), this implies
\(\log_2|L_{\lfloor s_2\rfloor}|\le(2\beta+o(1))s_2n\).
For any fixed center (T), at most this many points in \(\mathcal S_t(T)\) can be Low-at-the-high-threshold. On the other hand, using \(\binom{M}{k}\ge(M/k)^k\),

\[
|\mathcal S_t(T)|=\binom{N/2}{t/2}^2
\ge (N/t)^t
=2^{(4(1-\beta)+o(1))s_2n}.
\]

For \(\beta\le1/4\), the shell exponent is at least \((3-o(1))s_2n\), while the circuit-count exponent is at most \((1/2+o(1))s_2n\). Thus the fraction of tables in the shell with circuit complexity at most \(s_2\) is at most their global count divided by the shell size, which is \(2^{-\Omega(s_2n)}\), uniformly in (T). \(\square\)

The elementary argument controls the exact integer boundary by counting circuits of at most \(\lfloor s_2\rfloor\); all remaining shell points satisfy \(\mathrm{CC}_n(T')>N^\beta\).

## 3. A promise-supported pair with matched weight

Let (D_+) be **any** distribution supported on balanced tables in (L_{s_1}). Such tables exist for every fixed \(\beta>0\) and large (n), for example nonconstant affine functions. Define (D_-) as follows:

1. draw (T\sim D_+);
2. draw (T'\) uniformly from \(\mathcal S_t(T)\), conditioned on \(\mathrm{CC}_n(T')>s_2\);
3. output (T'\).

The theorem makes the conditioning event nonempty for every center and shows that it rejects only a \(2^{-\Omega(s_2n)}\) fraction of the unconditioned shell. Therefore (D_+) is supported on promised YES tables and (D_-) is supported on promised NO tables. The two sides have exactly the same Hamming weight (N/2), the same parity of the table bits, and are coupled at exact Hamming distance (t=\Theta(N^\beta)).

This gives a concrete hard-pair **candidate format** without claiming that it is hard. It removes a weight or global-parity distinguisher between the two distributions. It does not give an efficient sampler for (D_-): conditioning on circuit complexity is not known to be efficiently testable. It also does not bound the error of any ordinary circuit under the pair.

## 4. Strong counterconstruction against simple Low families

The pair format remains easy when (D_+) is supported on a recognizable subfamily.

**Balanced (k)-juntas.** Choose (k) as in C-487 so Shannon-Lupanov synthesis puts every (k)-variable function below (s_1), and let (D_+) be uniform over balanced functions (g\) lifted as (T_g(a)=g(a_1,\ldots,a_k)). The paired (D_-) above is balanced and High. Yet the circuit checking that all entries with the same first-(k)-bit prefix agree has (O(N)) total gates. It accepts every (D_+) sample. Any table passing the test is a (k)-junta with circuit size at most (s_1), so it rejects every (D_-) sample. Exact weight matching does not hide repeated-block structure.

**Affine/parity family.** If (D_+) is supported on affine tables, every two-dimensional face has XOR zero. Checking all face parities costs (O(Nn^2)=O(N\log^2N)) gates. A High table cannot be affine, since affine functions have (O(n))-gate circuits. This test separates all affine (D_+) samples from every High-supported (D_-), including the balanced shell pair.

**Sparse checks and global block relations.** Restricting (D_+) to block functions satisfying fixed sparse parity checks or a simple global relation does not help: block equality plus those checks is still (O(N\operatorname{polylog}N)) and rejects every High table satisfying the same relation, since the relation-specific block family itself has small circuits. These are failures of the chosen (D_+), not of the general shell construction.

Thus the shell construction neutralizes coarse weight and parity statistics, but does not conceal any address structure that certifies membership in a simple Low family. A viable choice of (D_+) must have broad Low support without a cheap complete family-membership test, or the argument must directly bound circuit error for the pair.

## 5. Serious lower-bound attempt and where it stops

For a fixed pair (D_+,D_-), define

\[
\mathrm{Err}(A)=\tfrac12\Pr_{T\sim D_+}[A(T)=0]
+\tfrac12\Pr_{T\sim D_-}[A(T)=1].
\]

If every (N^{1+\epsilon})-gate total circuit has positive error, a valid full-promise separator is impossible. The shell theorem supplies the exact promise support and gives the pair a controlled Hamming coupling. The missing theorem is that **every** circuit of the target size has positive error for some suitably chosen (D_+); no such bound is proved here. For the (k)-junta and affine choices, the tests above have zero error, so those candidates are conclusively retired.

The radius cannot be shrunk to the known patching scale by this counting argument. At (t=\Theta(s_2/n)),

\[
\log_2|\mathcal S_t(T)|=O(s_2),
\]

while the standard upper bound on the number of tables of circuit size at most s_2 is 2^{O(s_2 log(s_2+n))}=2^{O(s_2 n)}. That bound is too large to force a High neighbor in this sphere. Hence a factor-Theta(n) annulus remains between the patching lower radius Omega(s_2/n) and the radius Theta(s_2) where counting gives a typical High shell. This is a limitation of the counting method, not a theorem that smaller-radius High neighbors never exist.

## 6. Literature, barriers, and resource audit

- C-344 already proved that every Low center has at least one High table at Hamming distance (K s_2); this cycle strengthens that to an almost-all, exact-weight-preserving shell for balanced centers. [C-344](C344_FULL_SUPPORT_LEARNING_ROUTE_HAS_NEARBY_HIGH_APPROXIMABLE_TABLES_2026-09-29.md)
- C-458's two-sided perturbation lemma gives the opposite, lower-distance constraint (d_H(Y,Z)=\Omega(s_2/n)). The 2026 perturbation note makes explicit that changing one truth-table bit costs (O(n)), with an (O(nd_H)) bound for general perturbations. [C-458](C458_FIRST_PRINCIPLES_AUDIT_AND_ROBUST_CODEBOOK_MODEL_2026-10-01.md), [Krinkin preprint](https://arxiv.org/abs/2603.09379)
- The average-case MCSP/one-way-function equivalence of Ilango, Ren, and Santhanam applies to specified locally samplable distributions and stronger multiplicative gap parameters in one theorem; it does not automatically apply to this non-efficiently-conditioned OPS-scale pair. [STOC 2022 paper](https://hanlin-ren.github.io/files/pdf/stoc22_robustness.pdf)
- The locality and natural-proofs barriers remain method-specific; no barrier escape is claimed. This construction does not yield a bound on paid AND states, OR operations, wires, descriptions, runtime, fusion, or cyclic closure.

## 7. Exact frontier effect and next test

**Strongest proved statement:** for every balanced Low table, a radius-(\Theta(N^\beta)) shell preserving exact weight is (1-2^{-\Omega(N^\beta n)}) High, for every fixed (0<\beta\le1/4) and sufficiently large (n).

**Counterexample:** for the balanced (k)-junta or affine pair, an (O(N\operatorname{polylog}N)) total-gate circuit separates (D_+) from (D_-) perfectly.

**Quantitative effect:** none. The ordinary essential-input lower bound remains (N-O(N^\beta\log N)); the full-promise upper remains (O(N2^{O(N^\beta)})); no fixed-\(\epsilon\) OPS lower bound, near-linear full-promise separator, native \(\rho\) theorem, or P-vs-NP proof follows.

**Next mathematical question:** can (D_+) be chosen over a broad, balanced Low family for which every circuit that sharply separates it from this conditioned noise shell would itself imply a superlinear separator lower bound? First test uniform random size-(s_1) circuit descriptions at the true fixed-beta scale against exact weight, essential variables, ANF/Fourier statistics, equality patterns, and low-cost block relations. Any test that separates the pair retires that sampler only; passing tests is not a proof.
