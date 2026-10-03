# C-487 — A separator-specific distribution criterion and an entropy-maximal counterexample

**Date:** 2 October 2026  
**Status:** exact sufficient criterion proved; a high-entropy Low ensemble is explicitly defeated; no asymptotic lower-bound improvement.

## 1. Exact target

Let \(N=2^n\), fix \(0<\beta<1\), and set

\[
s_1=\left\lfloor\frac{N^\beta}{10n}\right\rfloor,\qquad s_2=N^\beta.
\]

Write \(L_t=\{T\in\{0,1\}^N:\mathrm{CC}_n(T)\le t\}\). A valid total separator \(F\) must satisfy \(F(T)=1\) on \(L_{s_1}\), \(F(T)=0\) whenever \(\mathrm{CC}_n(T)>s_2\), and may choose either value in the middle band. Its size here is total fan-in-two AND/OR/NOT gates; wires, circuit descriptions, and the time used to synthesize a nonuniform circuit are separate measures.

The target is one fixed \(\epsilon>0\) such that for every sufficiently small fixed \(\beta>0\), every such separator has more than \(N^{1+\epsilon}\) total gates. OPS Theorem 1.4 gives the corresponding magnification implication to \(\mathrm{NP}\not\subseteq\mathrm{P/poly}\); its proof uses the \(2^{\beta n}/(10n)\) low threshold. The integer YES threshold is its floor. See the published theorem and proof in [Oliveira–Pich–Santhanam, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).

## 2. Fully specified mechanism: a hard-YES distribution

For a distribution \(D_{n,\beta}\) supported entirely on \(L_{s_1}\), define its distinguishing advantage against a circuit \(A:\{0,1\}^N\to\{0,1\}\) by

\[
\mathrm{Adv}_{D}(A)=\left|\Pr_{T\sim D}[A(T)=1]-\Pr_{U\sim\{0,1\}^N}[A(U)=1]\right|.
\]

**Theorem.** If there is a constant \(\eta>0\) such that every size-\(S\) total-gate circuit has \(\mathrm{Adv}_{D}(A)\le 1-\eta\), then, for all sufficiently large \(N\), no valid GapMCSP separator has at most \(S\) gates.

**Proof.** A valid separator \(F\) accepts every sample from \(D\), so \(\Pr_D[F=1]=1\). It rejects every table outside \(L_{s_2}\), including every promised NO instance. Hence

\[
\Pr_U[F(U)=1]\le \frac{|L_{s_2}|}{2^N}
\le 2^{-N+O(s_2\log(n+s_2))}
=2^{-N+o(N)}.
\]

The count uses the number of fan-in-two circuit descriptions; \(\beta<1\) makes \(s_2\log(n+s_2)=o(N)\). Thus \(F\) has advantage \(1-2^{-N+o(N)}>1-\eta\), a contradiction. This argument allows arbitrary DAG sharing and arbitrary middle-band labels: it uses only the two forced endpoint conditions. The simpler requirement \(\mathrm{Adv}_{D}(A)<1/2\) is a sufficient special case. \(\square\)

Consequently, a family \(D_{n,\beta}\) that keeps the advantage of every \(N^{1+\epsilon}\)-gate circuit bounded away from one, for the same fixed \(\epsilon\) and every sufficiently small fixed \(\beta\), would prove the requested ordinary lower bound and activate the OPS implication. The constant gap may depend on fixed \(\beta\). No circuit-description reconstruction or witness output is assumed.

This is a concrete *sufficient mechanism*, not a proof that such a distribution exists. Its exact unresolved step is the distributional lower bound itself.

## 3. Strong counterconstruction: maximal-scale entropy does not make a hard ensemble

The common shortcut “choose a high-entropy random family of Low tables” fails even when the seed entropy matches the full circuit-description exponent.

Use the Shannon–Lupanov upper bound: every \(k\)-variable Boolean function has a fan-in-two AND/OR/NOT circuit of size at most \((1+o(1))2^k/k\). Choose the largest \(k\) such that \(2^k/k\le s_1/4\). For large \(n\), \(k<n\), \(k=\log_2 s_1+\log_2\log_2 s_1-O(1)\), and

\[
m=2^k=\Theta(s_1\log s_1)=\Theta_\beta(N^\beta).
\]

Sample a uniformly random \(g:\{0,1\}^k\to\{0,1\}\), and output the \(n\)-input truth table

\[
T_g(a_1,\ldots,a_n)=g(a_1,\ldots,a_k).
\]

Every output is in \(L_{s_1}\) by Shannon–Lupanov. The map \(g\mapsto T_g\) is injective, so \(D_k\) has exactly \(2^m\) outputs and entropy \(m=\Theta_\beta(N^\beta)\), the same order as the description entropy of all size-\(s_1\) circuits.

Nevertheless, a linear-size test distinguishes it. For every prefix \(u\in\{0,1\}^k\), compare all truth-table bits \(T_{u v}\) with the representative bit \(T_{u0^{n-k}}\). The AND of these \(N-m\) equality checks uses \(O(N)\) total gates, accepts every \(T_g\), and accepts a uniform table with probability exactly

\[
2^{-(N-m)}.
\]

This is a proof-level counterexample to entropy, support size, and random choice within a large Low family as stand-alone hardness mechanisms. It is not a counterexample to the existence of a different hard-YES distribution or to the full GapMCSP lower-bound program. The underlying fact is old—Shannon–Lupanov synthesis is not claimed as new; this is its parameter-matched use as an adversarial ensemble.

### Canary audit

* **Affine/parity tables.** If \(f\) is affine on \(n\ge4\) address bits, the XOR of its four values on any two-dimensional address face is zero. Choose two disjoint faces: the two checks are independent, use \(O(1)\) gates, accept every affine table, and accept a uniform table with probability \(1/4\).
* **Repeated blocks / \(k\)-juntas.** The \(k\)-junta ensemble above is accepted by \(N-m\) shared equality checks and has uniform acceptance exactly \(2^{-(N-m)}\).
* **Sparse parity checks.** Restrict the \(m\) block labels \(g(u)\) by two independent checks, for example \(g(u_1)\oplus g(u_2)\oplus g(u_3)=0\) and \(g(u_4)\oplus g(u_5)\oplus g(u_6)=0\), using six distinct labels. Every output remains a \(k\)-variable function and hence Low. Check block equality plus these two sparse checks with \(O(N)\) gates; uniform acceptance is \(2^{-(N-m+2)}\).
* **Simple global block relation.** Instead require \(\bigoplus_{u\in\{0,1\}^k}g(u)=0\). Every output remains Low; block equality plus one parity of the \(m\) representatives uses \(O(N)\) gates, and uniform acceptance is \(2^{-(N-m+1)}\).

These are ensemble-specific distinguishers, not full-promise separators: they may reject other required Low tables and may accept High tables.

### Exploratory random-DAG sampler canary (finite only)

To make “random circuit description” precise for one experiment, start with the \(n\) address variables and constants 0 and 1. Append \(s\) gates; independently choose AND, OR, or NOT uniformly, and choose each predecessor uniformly with replacement from earlier wires. Finally choose an output wire uniformly. This samples valid Low tables but is not uniform over all syntactic descriptions.

For a truth table \(T\), define \(\mathrm{ess}(T)\) as the number of address variables \(x_j\) for which some adjacent pair of table entries differs. The test \(\mathrm{ess}(T)<n\) is computable in \(O(Nn)\) gates: for each \(j\), OR the \(N/2\) pairwise XORs, then test whether all \(n\) essentiality bits are 1. A uniform table fails this test with probability at most \(n2^{-N/2}\), because a fixed variable is inessential on exactly a \(2^{-N/2}\) fraction of tables.

An exploratory simulation found the following acceptance rates for this test:

| \(n\) | \(s\) | samples | sampler acceptance |
|---:|---:|---:|---:|
| 6 | \(150n=900\) | 2,000 | 0.9825 |
| 8 | \(150n=1,200\) | 2,000 | 0.9930 |
| 10 | \(150n=1,500\) | 2,000 | 0.9975 |
| 6 | \(1,000n=6,000\) | 300 | 0.9633 |
| 8 | \(1,000n=8,000\) | 300 | 0.9900 |
| 10 | \(1,000n=10,000\) | 300 | 0.9900 |

This is evidence that this particular random-DAG sampler is structurally exposed at toy sizes. These \(s=\Theta(n)\) samples are not the fixed-\(\beta\) OPS regime \(s_1=2^{\beta n}/(10n)\); the data prove no asymptotic claim and do not rule out every random-circuit encoding. The exact finite experiment is reproducible with [experiment_random_dag_essential_support.py](../experiment_random_dag_essential_support.py). Savicky's work on distributions induced by random Boolean formulas concerns tree syntax and a different limit regime, so it supplies no theorem for this DAG sampler.

## 4. Security quantifiers: correction and exact boundary for C-486

For fixed \(\beta\), a seed length \(m=\Theta_\beta(N^\beta)\) gives \(N=m^{1/\beta+o(1)}\). A target separator of size \(N^{1+\epsilon}\) is one circuit-size regime

\[
m^{q_\beta+o(1)},\qquad q_\beta=\frac{1+\epsilon}{\beta}.
\]

The exact separator criterion above asks for a distribution that fools this one fixed exponent \(q_\beta\) by a constant gap. It does **not** require negligible advantage against all polynomial-size tests. Since \(D_{n,\beta}\) may vary with \(\beta\), the fact that \(q_\beta\) grows as \(\beta\) shrinks does not by itself produce one generator secure against every polynomial exponent.

There is a useful stronger implication. If a *single uniform polynomial-time* generator \(G_m:\{0,1\}^m\to\{0,1\}^{m^{d+o(1)}}\) is indistinguishable from uniform by **every nonuniform polynomial-size circuit** with advantage at most \(1/3\), then it yields a weak one-way function against uniform polynomial-time inverters. Given an inverter \(I\), test \(y\) by checking whether \(G(I(y))=y\). On \(G(U_m)\) the test accepts with the inverter's success probability; on uniform \(y\) it accepts with probability at most \(2^m/2^{m^{d+o(1)}}\). The test is polynomial size because \(G\) is polynomial time. Thus every polynomial-time inverter succeeds with probability at most \(1/3+2^{m-m^{d+o(1)}}\). Standard weak-to-strong one-way-function amplification then gives a standard OWF. Goldreich's treatment states the weak-to-strong theorem in [Foundations of Cryptography, Sec. 2.3](https://www.wisdom.weizmann.ac.il/~/oded/foc-vol1.html).

This refines C-486: **negligible** PRG security is sufficient but not necessary for a cryptographic consequence; constant indistinguishability against *all polynomial degrees* already gives weak one-wayness. The fixed-\(\beta\), fixed-\(q_\beta\) condition remains weaker, so we do not infer ordinary OWFs from it. No known amplification converts only that one bounded circuit-size exponent into security against all polynomial-size inverters while preserving one fixed sampler.

## 5. Paired full-promise construction and resource ledger

Let \(K\le 2^{O(s_1\log(n+s_1))}=2^{O(N^\beta)}\) be the number of syntactic descriptions of circuits of at most \(s_1\) gates. A complete separator enumerates their truth tables as nonuniform constants, compares the input against each \(N\)-bit table, and ORs the equality flags. It accepts exactly \(L_{s_1}\), so it accepts every promised YES and rejects every promised NO.

| Resource | Cost |
|---|---:|
| Total AND/OR/NOT gates | \(O(NK)=O(N2^{O(N^\beta)})\) |
| Wires | \(O(NK)\) for the direct equality bank, with input fan-out represented explicitly |
| Nonuniform description bits | At most \(O(NK\log(NK))\) under a straightforward gate-list encoding |
| Offline synthesis time | A direct enumeration and evaluation implementation can take \(O(KNs_1\operatorname{poly}(n))\); this is not the gate count |
| Runtime on a table | Not asserted to be near-linear by this nonuniform circuit construction |

The paired construction is still far above \(N^{1+\epsilon}\) for fixed \(\beta>0\). No near-linear full-promise separator was found. No paid-AND-state, fusion, cyclic-closure, or \(\rho\) bound follows: this cycle concerns ordinary total-gate circuits only.

## 6. First-principles assessment, barriers, and next move

The failed routes separate into three questions. (i) Input support, information, and certificates can force roughly \(N\) relevant coordinates, but they do not charge post-read computation. (ii) Global statistics and code-like relations can often be evaluated with \(O(N)\) shared gates; the \(k\)-junta construction makes even a near-maximal-entropy ensemble easy. (iii) The remaining viable directions are a gate-by-gate lower bound for every extension, or an ensemble-specific computational indistinguishability theorem at the exact exponent \(q_\beta\). Neither has been proved here.

The classical natural-proofs barrier of Razborov–Rudich is conditional evidence against broad constructive properties useful against strong circuit classes; it is not an unconditional no-go for every separator lower-bound proof. See [Razborov–Rudich](https://doi.org/10.1006/jcss.1997.1494). The hardness-magnification locality barrier of Chen et al. identifies why specified existing weak lower-bound techniques, when they extend to the small-fan-in oracle circuits supplied by magnification, cannot reach the threshold. It is a method-specific barrier, not an impossibility theorem for all proofs; see [Chen et al.](https://eccc.weizmann.ac.il/report/2019/168/). OPS's theorem and the failed techniques audited here do not give a gate-charge theorem for arbitrary shared DAGs.

**Next concrete test:** analyze the uniform small-circuit-description ensemble against exact weight, affine checks, ANF, block-equality, sparse checks, and low-cost global relations. The present \(k\)-junta ensemble is an adversarial calibration, not that uniform-description ensemble. Only continue the sampler route if it survives these tests; surviving them is still not a pseudorandomness proof. In parallel, retain the direct all-extension target, and require any proposed potential to have a recurrence for AND, OR, and NOT under arbitrary fan-out and merges.

## 7. Frontier effect

**Strongest proved statement:** the distributional criterion in Section 2 rules out every valid size-\(S\) separator if a Low-supported ensemble fools all such circuits by a constant distinguishing gap. The parameter-matched \(k\)-junta family proves that maximal-scale seed entropy does not establish this premise.

**Quantitative effect: none.** The ordinary essential-input lower bound remains \(N-O(N^\beta\log N)\), with the C-406 refinement. The exact complete separator upper remains \(O(N2^{O(N^\beta)})\). No fixed-\(\epsilon\) OPS lower bound, near-linear full-promise separator, native \(\rho\) result, or P-vs-NP proof was obtained.

## References checked

* O. B. Lupanov, “On the possibilities of synthesis of circuits out of various elements,” [MathNet archive](https://www.mathnet.ru/php/archive.phtml?jrnid=tm&option_lang=rus&paperid=1277&wshow=paper), 1958.
* I. C. Oliveira, J. Pich, and R. Santhanam, [Hardness Magnification Near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and its proof.
* P. Savicky, [Random Boolean Formulas Representing Any Boolean Function with Asymptotically Equal Probability](https://doi.org/10.1016/0012-365X(90)90223-5), 1990; formula sampling is a different model from the DAG experiment above.
* L. Chen et al., [Beyond Natural Proofs: Hardness Magnification and Locality](https://eccc.weizmann.ac.il/report/2019/168/).
