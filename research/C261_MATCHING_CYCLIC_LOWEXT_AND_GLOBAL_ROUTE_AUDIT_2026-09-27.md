# C-261 to C-265 — matching transfer, LowExt parameters, and route filters

Date: 27 September 2026  
Priority reset: use the supplied C-256 steering note; repository work through C-260 is preserved.  
Checkpoint rule: five claims, then pause and compare the actual Gap-MCSP q bound with its previous value.

## C-261 — Cyclic monotone matching lower bound

**Classification: GLOBAL-STRUCTURAL.**

Let \(v\) be even and let \(f_v\) be the promise separator that is 1 on bipartite graphs with a perfect matching and 0 on graphs with no matching of size \(v/4\). The values on the medium band are unrestricted. Rao's September 2026 revision proves that every monotone circuit separating these two graph classes has at least \(\exp(c\sqrt v)\) gates for a constant \(c>0\).

This lower bound survives the least-fixed-point cycles in the native model. Suppose a cyclic monotone grammar has q AND states. Contract each union-only strongly connected component: its least fixed point is just the union of its external inputs. Each AND state is then the intersection of two unions of original generators and the q AND states. On a fixed input, the q-bit state vector is iterated from zero; monotonicity means each bit changes from 0 to 1 at most once, so q rounds suffice. Unroll those rounds. Each state in each round is an AND of two ORs, and each OR has at most \(M+q\) terms, where \(M=\Theta(v^2)\) is the number of graph-edge inputs and the other terms are prior-round states. Replacing each OR by binary gates gives an ordinary monotone separator of size

\[
S \le C q^2(M+q)
\]

for a universal constant C. Rao's lower bound therefore implies

\[
\exp(c\sqrt v) \le Cq^2(\Theta(v^2)+q).
\]

If q were below \(\exp(c\sqrt v/4)\), the right-hand side would be at most \(\exp(3c\sqrt v/4+O(\log v))\), a contradiction for large v. Thus

\[
\boxed{\operatorname{CycAnd}(f_v)\ge \exp(\Omega(\sqrt v)).}
\]

The proof uses the *specific* resource conversion relevant here: q cyclic AND states, q least-fixed-point rounds, then an explicit fan-in-two unrolling. It does not infer cyclic hardness from a superficial resemblance to ordinary monotone circuits. This establishes the first requested matching-source threshold. It is a source theorem, not a Gap-MCSP bound.

Primary source: [Rao, *Monotone Circuit Lower Bounds from Spread Matchings*, ECCC TR26-129, revision 5](https://eccc.weizmann.ac.il/report/2026/129/revision/5/download). The cyclic set/intersection model and its exact relation to fusion are defined by [Cavalar and Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems*](https://arxiv.org/abs/2503.14117).

## C-262 — Exact parameter region for a LowExt transfer

**Classification: CONDITIONAL-TRANSFER.**

Retain the exact C-125/C-126 hypotheses. Let \(\phi_N\) be a monotone map into the signed partial-table feature space with AND cost \(a(N)\). On every YES graph, its image must contain the one-hot code of some \(w\in\mathrm{SIZE}(s_1)\). On every NO graph, its image must lie below the one-hot code of some \(z\notin\mathrm{SIZE}(s_2)\). Then

\[
q \ge \operatorname{CycAnd}(f_v)-a(N)
  \ge \exp(c_1\sqrt v)-a(N)
\]

for a constant \(c_1>0\).

Choose

\[
v(N)=\left\lceil A(\ln N)^2\right\rceil .
\]

Then the source term is \(N^{c_1\sqrt A-o(1)}\). If \(a(N)\le N^\eta\), a sufficient strict-margin condition for \(q>N^{1+\epsilon}\) is

\[
c_1\sqrt A>\max\{1+\epsilon,\eta\}.
\]

More explicitly, choose any \(\delta>0\) and require \(c_1\sqrt A\ge\max\{1+\epsilon,\eta\}+\delta\). If \(a(N)=\operatorname{polylog}N\), any \(\eta>0\) can be used, and the condition reduces to \(c_1\sqrt A>1+\epsilon\).

The matching instance has \(M=\Theta(v^2)=\Theta((\log N)^4)\) edge bits. A proposed YES completion computable by \(\operatorname{poly}(v)\) gates fits

\[
s_1=N^\beta/(c_0\log N)
\]

for every fixed \(\beta>0\), once N is sufficiently large. Thus the small-\(\beta\) issue is quantitatively solved *if* both the completion circuits and the map have polylogarithmic cost. The NO high-completion condition is exact: if \(\phi(x)\subseteq e(z)\) and \(e(w)\subseteq\phi(x)\), then \(e(w)\subseteq e(z)\); one-hot codes force \(w=z\), impossible for low w and high z.

**Still missing:** an explicit monotone \(\phi_N\) with these YES and NO properties and AND cost below the source exponent. The parameter calculation does not construct one.

## C-263 — Sparse edge-code attempt fails at the LowExt quantifier

**Classification: ROUTE-KILL.**

Tested the direct encoding of a matching witness as a sparse table over edge addresses.

* If \(w_M\) has 1s on matching edges and \(\phi(G)\) supplies 1-rails for present edges and 0-rails universally, then \(e(w_M)\subseteq\phi(G)\) for each matching \(M\subseteq G\). But the all-zero table code is also below every image, so LowExt is true on NO graphs.
* Complementing the encoding makes the all-one table code an unconditional false witness.
* Pinning a baseline bit does not repair this template: a one-bit perturbation of a simple baseline truth table is itself computable by a small circuit. The partial constraints must rule out every such unintended low completion, not only malformed matching witnesses.

This kills the plain edge-incidence/sparse-code construction, not all C-125 maps. It isolates the issue: LowExt quantifies over *all* low truth tables, so a witness-only encoding must enforce global code validity against the full low-circuit class. Requiring a valid matching witness in the intended syntactic family is insufficient.

## C-264 — Global compatibility matrix tested on equality fingerprints

**Classification: CALIBRATION.**

The strongest candidate object currently available is the state-indexed compatibility relation

\[
\mathsf{Comp}_i(w,w')=1
\]

when some accepting context with a hole at state i matches w and some proof rooted at i matches w', with a consistent union of their seed supports. Add the output blocker family to record which literal hits each compatible join. C-260 proves this three-way incidence exactly; every diagonal low pair is covered by some state, and every compatible join is hit by every output blocker.

The required hostile test is the repeated-block diagonal-equality cover. C-258 realizes that cover with q=2N+2d-1. Its equality fingerprints keep cross-description joins safe even though many descriptions reuse states. Thus pair counts, blocker-hit counts, distinct rows, or raw information in \(\mathsf{Comp}_i\) cannot alone force superlinear q. A valid synchronization-vs-splicing theorem must show that the *actual full class* \(\mathrm{SIZE}(s_1)\) demands many incompatible compatibility relations whose grammar representation costs more than O(N); the repeated-block family admits a compact equality scan.

This route remains open at the global step. No q-sensitive incidence multiplicity or relation-complexity measure that passes C-258 and yields a lower bound has been proved.

## C-265 — Independent cofactor recursion spends the soundness budget

**Classification: ROUTE-KILL.**

Tested a block-decomposition route to an \(N^{1+o(1)}\) full-promise cover. Split the n-bit truth-table address into \(\log r\) selector bits and \(r\) blocks. Every size-\(s_1\) circuit restricts to a size-\(s_1\) circuit on each block. Conversely, any independent tuple of r such block circuits has a mux circuit of size \(rs_1+O(r\log r)\), so taking \(r=\Theta(n)\) gives a safe enlarged low family inside \(\mathrm{SIZE}(s_2)\).

The hoped-for recursion is to cover that product by independently covering each block and then refine each block again. Its soundness cost multiplies: after L levels, a table assembled from independent leaf circuits can require roughly \(R s_1\) gates, where \(R\) is the product of the block branching factors. The OPS promise permits only \(R=O(n)\) such independent pieces. A trivial truth-table-synthesis base needs \(R\) at least \(N/s_1=N^{1-\beta}\operatorname{polylog}N\); even using Lupanov's \(O(2^{n'}/n')\) synthesis bound still requires \(R=N^{1-\beta+o(1)}\). Both are much larger than n for fixed \(\beta<1\). Hence the naive independent-cofactor recursion cannot reach a trivial base while staying inside \(\mathrm{SIZE}(s_2)\).

This retires only independent product recursion. A successful upper construction still needs a shared circuit description across blocks, precisely the coherence obstacle recorded in C-229/C-260.

## Literature side lead: block summaries

Cavalar, de Rezende, Gray, and Santhanam's 2026 result on monotone learning and partial monotone circuit size uses lifted proof-complexity instances, blockwise proof variables, and summary variables that encode absence patterns across a block. It is a conditional time-hardness result for succinct labelled samples, not an unconditional monotone circuit lower bound for LowExt and not a reduction from matching to our signed table encoding. The useful technique-level lead is to test whether block summaries of *absent rails* can compress many context/proof compatibility constraints while preserving the same latent low-circuit description. The missing quantitative bridge is still a monotone map with small AND cost.

Primary source: [Cavalar, de Rezende, Gray, and Santhanam, ECCC TR26-128](https://eccc.weizmann.ac.il/report/2026/128/download).

## Five-claim checkpoint

The actual Gap-MCSP fusion lower bound has **not changed**: it remains \(q=N-o(N)\). C-261 improves the source-side result to \(\operatorname{CycAnd}(\mathrm{MATCH}_v)\ge\exp(\Omega(\sqrt v))\), and C-262 shows that \(v=\Theta(\log^2N)\) would meet the target if the exact LowExt reduction had polylogarithmic AND cost. The outstanding qualitative implication is still the map construction. On the native route, C-260's context/proof/blocker incidence passes its required equality-fingerprint calibration but yields no q-charge. On the upper route, independent cofactor recursion cannot stay within the size-\(s_2\) soundness budget.
