# C-488 - Project-wide first-principles reassessment and endpoint-pair certificates

**Date:** 2 October 2026  
**Scope:** synthesis of the repository through C-487; one exact refinement of the hard-distribution route; no frontier change.

## 1. The problem after removing every algorithmic assumption

Let (N=2^n), (s_1=\lfloor N^\beta/(10n)\rfloor), and (s_2=N^\beta), for fixed (0<\beta<1). Write

\[
Y=\{T:\mathrm{CC}_n(T)\le s_1\},\qquad Z=\{T:\mathrm{CC}_n(T)>s_2\}.
\]

A total circuit (F:\{0,1\}^N\to\{0,1\}) is a valid separator exactly when

\[
Y\subseteq F^{-1}(1)\subseteq \{0,1\}^N\setminus Z = L_{s_2}.
\]

The middle band is unconstrained. The target is to prove that every such fan-in-two total-gate circuit has more than (N^{1+\epsilon}) gates for one fixed \(\epsilon>0\), for every sufficiently small fixed \(\beta>0\). The published Oliveira-Pich-Santhanam theorem has a universal constant in its statement; its proof instantiates the low threshold (2^{\beta n}/(10n)) and high threshold (2^{\beta n}), and the fixed-\(\epsilon\) quantifier implies (\mathrm{NP}\not\subseteq\mathrm{P/poly}\). The gates may share arbitrarily; wires, gate descriptions, and synthesis time are different costs. [OPS, Theorem 1.4 and proof](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)

This exact formulation removes several tempting but invalid shortcuts. A lower bound for one extension is not a lower bound for the minimum over all extensions. A recognizer for a chosen Low subfamily need not accept all of (Y). A circuit need not reconstruct a short description or output a witness. A result for formulas, comparator circuits, paid-AND states, or native fusion does not transfer to ordinary total gates without a cost-preserving theorem.

## 2. What the accumulated work establishes, grouped by the resource it measures

The C-1 through C-487 artifacts are best understood as tests of a few proof interfaces, not as hundreds of independent candidate proofs.

1. **Input dependence and information.** Essential-input, support, query, certificate, sketch, and cofactor arguments establish that a separator can depend on nearly all (N) table bits. This reaches the linear information scale. It does not force superlinear gates: parity depends on all (N) bits and has (O(N)) gates. One-cut cofactor diversity also stops at a linear cap, and selectors realize exponentially many cofactors with only linearly many shared gates.
2. **Properties of selected Low families.** Affine checks, ANF degree, weight spectra, repeated blocks, sparse parity checks, and global relations have cheap shared tests. C-487's (k)-junta family is a sharp entropy calibration: it has (2^{\Theta(N^\beta)}) Low tables but an (O(N))-gate repeated-block test. These are counterexamples to ensemble heuristics, not to the full lower-bound target.
3. **Witness and source-map routes.** A costed reduction must map every source YES to (Y), every source NO to (Z), and count all table generation and postprocessing gates. Paying (q^2) AND states does not pay (q^2) total gates. No reviewed source map leaves the required superlinear residual margin.
4. **Alternate models.** Formula, fixed-depth, comparator, branching-program, oracle, paid-state, fusion, and cyclic-closure results are model-specific. Existing MCSP formula and comparator lower bounds are valuable controls, but do not lower-bound arbitrary shared circuits. For example, the comparator result has an exponent increment proportional to the low-size exponent \(\alpha\), (1+\alpha/2-\delta), and is in a restricted model; as \(\alpha\) tends to zero it supplies no uniform positive increment for the OPS quantifier. [Comparator-circuit theorem](https://link.springer.com/article/10.1007/s00453-022-01091-y), [MCSP restricted-model bounds](https://www.cs.sfu.ca/~kabanets/papers/MCSP_lower_bounds.pdf)

The failures do **not** prove that a merge-stable potential is impossible, that a hard pair of distributions cannot exist, or that P=NP. They show that the specific proxies tried so far do not charge distinct shared gates above (N). The locality barrier and natural-proofs barrier constrain specified proof methods under their assumptions; neither is a universal impossibility theorem. [Chen et al., locality barrier](https://eccc.weizmann.ac.il/report/2019/168/), [Razborov-Rudich, Natural Proofs](https://doi.org/10.1006/jcss.1997.1494)

## 3. Exact mechanism refinement: a labeled endpoint-pair distribution

Let (\mathcal C_S) be all total fan-in-two circuits of at most (S) gates. Let (Q) be any distribution on labeled examples ((T,b)) with (T\in Y,b=1) or (T\in Z,b=0). Define

\[
\mathrm{Err}_Q(A)=\Pr_{(T,b)\sim Q}[A(T)\ne b].
\]

**Endpoint-pair lemma.** If there is a (\delta>0) such that every (A\in\mathcal C_S) has (\mathrm{Err}_Q(A)\ge\delta), then no valid size-(S) separator exists.

**Proof.** A valid separator labels every point in the support of (Q) correctly, so its error is zero, contradicting the assumed lower bound. This uses the forced endpoints only and allows arbitrary sharing and arbitrary middle labels. \(\square\)

Equivalently, write (Q) as a weighted pair (D_+,D_-), supported on (Y,Z), with

\[
\mathrm{Err}(A)=\lambda\Pr_{D_+}[A=0]+(1-\lambda)\Pr_{D_-}[A=1].
\]

This changes the premise from C-487's low-versus-uniform comparison to endpoint prediction error on selected supports; neither condition is known here to imply the other in general. The endpoint version does not require PRG-like indistinguishability from uniform, but it requires a high-supported negative distribution and a lower bound against every size-S circuit. It also does not require an efficient sampler or a uniform-table density calculation. It can match selected global statistics on the two sides.

### Exact finite duality, and why it is not yet progress

For fixed (N,S), the circuit class and endpoint universe are finite. If no size-(S) separator exists, then every (A\in\mathcal C_S) mislabels at least one forced endpoint. Select one such labeled counterexample for each circuit description and let (Q) be uniform over this multiset. Constants ensure there is at least one positive and one negative witness type. Every circuit then has error at least (1/M_S), where

\[
M_S=|\mathcal C_S|\le 2^{O(S\log(N+S))}.
\]

Conversely, any endpoint-supported (Q) with positive minimum error rules out a separator. Thus the unrestricted existence of such a (Q) is equivalent to the desired finite circuit lower bound; the witness construction is nonconstructive and assumes the very nonseparability we need to prove. At (S=N^{1+\epsilon}), its generic error can be only (2^{-O(N^{1+\epsilon}\log N)}). The useful research problem is therefore to find a *structured, independently analyzable* pair (D_+,D_-), not to advertise the finite duality as a breakthrough.

This also corrects the strength of the earlier C-487 route: a fixed constant gap against uniform is sufficient, but it is not necessary. The endpoint pair is a distinct search target, not an established shortcut.

## 4. Strong counterconstruction: matching a global statistic still leaves a cheap separator

The endpoint-pair idea must survive the required hostile families.

Take (k<n) maximal with (2^k/k\le s_1/4), put (m=2^k=\Theta(s_1\log s_1)=\Theta_\beta(N^\beta)), and let (D_+) be uniform over balanced Boolean functions (g:\{0,1\}^k\to\{0,1\}), lifted to (n)-bit tables

\[
T_g(a_1,\ldots,a_n)=g(a_1,\ldots,a_k).
\]

By Shannon-Lupanov, every output is Low; every output also has exactly (N/2) ones. Let (D_-) be uniform over balanced (N)-bit tables conditioned on 
\(\mathrm{CC}_n(T)>s_2\). This support is nonempty and conditioning removes only a (2^{-N+o(N)}) fraction: circuit counting gives 
\(|L_{s_2}|\le2^{O(s_2\log(n+s_2))}=2^{o(N)}\), whereas 
\(\binom{N}{N/2}=2^{N-o(N)}\).

Both distributions have the same exact Hamming weight, so a population-count test cannot distinguish them. Nevertheless, the (O(N))-gate test that checks equality of all table entries with the same (k)-bit prefix accepts every (D_+) sample. Every table passing that test is a (k)-junta and hence has circuit complexity at most (s_1); therefore it rejects every (D_-) sample. This is a total ordinary circuit separator for this *pair of supports*. It proves that matching a simple statistic is not enough and that pair distributions must resist all shared structural tests, not just tests against uniform. It does not refute the endpoint-pair lemma or the full OPS target.

The same warning is visible for affine tables (face parity), sparse parity-check ensembles, global block relations, and the toy random-DAG sampler. Such tests screen a proposed pair; passing them does not establish the required error bound against all (S)-gate circuits.

## 5. Quantitative frontiers and resource ledger

* **Ordinary lower:** unchanged at the essential-input floor (N-O(N^\beta\log N)), including the C-406 refinement. This is not a gate lower bound.
* **Ordinary complete upper:** enumerating all at-most-(s_1) circuit descriptions and comparing the table against each gives (O(N2^{O(N^\beta)})) total AND/OR/NOT gates. This accepts exactly (Y), so it is full-promise correct. No near-linear separator was found.
* **OPS target:** no (N^{1+\epsilon}) lower bound for all total extensions for one fixed (\epsilon) and all sufficiently small fixed (\beta); no NP-not-P/poly proof.
* **Native target:** no new (\rho\), fusion, or cyclic-closure result. These remain separate absent a compiler with complete gate/state accounting.
* **Resource separation:** gate count is the target in this report. Fan-out wires, circuit-description bits, paid AND states, OR transitions, and offline synthesis/runtime must be separately accounted for; none can silently substitute for total-gate cost.

## 6. Route decision from first principles

The immediate target should be the **endpoint-pair error game** at the exact OPS thresholds:

1. Seek (D_+\) supported on (Y) and (D_-\) supported on (Z), with a proof that every (N^{1+\epsilon})-gate total circuit incurs positive error under their mixture, for one fixed \(\epsilon\) and every sufficiently small fixed \(\beta\).
2. Prefer pairs whose distributions share low-cost global statistics; use repeated-block, parity, ANF, weight, and block-generation tests as rejection filters. Do not rely on a selected Low property that itself certifies low circuit complexity, since no High distribution can match it.
3. Keep the mechanism honest: if the proof of small error is just the finite witness construction, a PRG assumption, an unproved anti-sharing axiom, or a bound in another model, record no progress toward the unconditional ordinary frontier.
4. Continue a direct potential only if every AND/OR/NOT gate's contribution is bounded under arbitrary fan-out and merges and the endpoint constraints force a superlinear final value.
5. Pair every lower-bound cycle with the exact enumeration upper and account for gates, wires, descriptions, and synthesis time separately.

This priority is a new *search formulation*, not a claim that the pair-distribution route is easier. The finite duality shows that without additional structure it is exactly the original lower bound. The genuine missing mathematical object remains a theorem about unrestricted shared computation separating the two endpoint sets.

## 7. Final first-principles assessment

Across the project, there is no evidence that one elementary definition or an overlooked counting identity will settle P vs NP. The repeated failure point is precise: semantic constraints force many relevant bits, many witnesses, or many distinct residual behaviors, but shared gates can compute and reuse information without paying once per witness or residual state. Input information alone naturally yields a linear scale. To move past it, a proof must measure a computational interaction that survives reuse, or import an endpoint-hardness theorem whose assumptions are explicit.

The user intuition that a new idea may exist is mathematically reasonable. The evidence does not support saying that a breakthrough is close or that it must lie in a particular niche. The productive adjustment is to stop treating each failed proxy as a near-miss and make every new proposal answer one exact question: why must every circuit consistent with *all* forced endpoints spend more than (N^{1+\epsilon}) distinct total gates?

**Strongest new proved statement:** the endpoint-pair error lemma and its finite dual characterization.  
**Counterexample:** a balanced Low (k)-junta distribution and a balanced High distribution are separated by an (O(N))-gate repeated-block test.  
**Quantitative frontier effect:** none.

## Primary references checked

* Oliveira, Pich, Santhanam, [Hardness Magnification Near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and proof.
* Lupanov, [On the Possibilities of Synthesis of Circuits out of Various Elements](https://www.mathnet.ru/php/archive.phtml?jrnid=tm&option_lang=rus&paperid=1277&wshow=paper), 1958.
* Chen et al., [Beyond Natural Proofs: Hardness Magnification and Locality](https://eccc.weizmann.ac.il/report/2019/168/).
* Razborov and Rudich, [Natural Proofs](https://doi.org/10.1006/jcss.1997.1494).
* Cheraghchi et al., [Circuit Lower Bounds for MCSP from Local Pseudorandom Generators](https://www.cs.sfu.ca/~kabanets/papers/MCSP_lower_bounds.pdf).
* [Algorithms and Lower Bounds for Comparator Circuits from Shrinkage](https://link.springer.com/article/10.1007/s00453-022-01091-y).
