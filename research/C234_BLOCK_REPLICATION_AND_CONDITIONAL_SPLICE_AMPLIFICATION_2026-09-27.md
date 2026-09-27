# C-234 — Block replication, residual obligations, and a conditional splice amplifier

Date: 27 September 2026  
Scope: implement the user's priority change toward native cyclic fusion readout. This develops an OPS-specific family of low anchors with a huge high-complexity hybrid space, proves a conditional q lower bound under an explicit proof-localization hypothesis, and then falsifies that hypothesis as an automatic consequence using a linear-size separator for the restricted family. It does **not** prove a lower bound for the full Gap-MCSP promise.

## 1. Native state obligations as a cross-product

Fix a successful q-rule closure and use the finite-proof grammar from C-227. For a state i, let \(\mathcal K_i\) be the supports of accepting-proof contexts obtained by removing one occurrence of i, and let \(\mathcal S_i\) be the supports of finite proofs rooted at i. Substitution gives

\[
K\in\mathcal K_i,\ C\in\mathcal S_i\quad\Longrightarrow\quad K\cup C\in\mathcal S_{\rm out}.
\]

Write \(\operatorname{dom}(A)=\{k:(k,b)\in A\text{ for some }b\}\), and call A consistent if it contains no opposite rails. Let \(\kappa=\kappa_\square(s_2)\), the largest number of free coordinates in a subcube contained in \(\mathrm{SIZE}(s_2)\). Soundness gives the exact state obligation

\[
\boxed{K\cup C\text{ consistent}\quad\Longrightarrow\quad
|[N]\setminus(\operatorname{dom}K\cup\operatorname{dom}C)|\le\kappa
\quad\text{for every }K\in\mathcal K_i,C\in\mathcal S_i.}
\tag{34}
\]

Equivalently, for a fixed replacement support C with free set \(F_C=[N]\setminus\operatorname{dom}C\), every context compatible with C must pin all but at most \(\kappa\) coordinates of \(F_C\). The symmetric statement holds for a fixed context and every compatible replacement. This is stronger than pairwise agreement among the derivations originally selected for low anchors: a shared state creates the *entire* context-by-subproof product.

Equation (34) gives a semantic obligation for a state, but not a state-count bound. A context can carry many literal choices, and the proof grammar can have exponentially many finite unfoldings. Any global potential must charge how this residual obligation is represented across the grammar, rather than count contexts or use one local projection.

## 2. Low diagonal tables and high block hybrids

Set \(N=2^n\), fix \(0<\beta<1\), and use OPS scales \(s_2=N^\beta\), \(s_1=s_2/(c n)\). Standard circuit counting gives

\[
|\mathrm{SIZE}(s_2)|\le 2^{A s_2\log_2(s_2+n)}
\]

for a basis-dependent constant A. By Lupanov synthesis, every Boolean function on k variables has a fan-in-two circuit of size at most \(B2^k/k\), for an absolute basis-dependent B.

Choose k so that \(B2^k/k\le s_1/4\) and k is maximal, using the standard Lupanov synthesis bound ([1958 MathNet record and scan](https://www.mathnet.ru/php/archive.phtml?jrnid=tm&option_lang=rus&paperid=1277&wshow=paper)). Then

\[
2^k=\Theta(s_1\log s_1)=\Theta(s_2),\qquad k=\beta n+O(1).
\]

Split an n-bit address as \((p,u)\), where \(u\in\{0,1\}^k\) and \(p\in\{0,1\}^{n-k}\). There are

\[
r=2^{n-k}=N/2^k=\Theta(N/s_2)
\]

prefix blocks, each with \(2^k\) truth-table coordinates. For every k-bit Boolean function g, define the diagonal table

\[
w_g(p,u)=g(u).
\]

It ignores p, so \(CC(w_g)\le s_1/4<s_1\). Now independently choose a function \(g_p\) for each prefix and form

\[
z_{\vec g}(p,u)=g_p(u).
\]

There are exactly \((2^{2^k})^r=2^N\) such block hybrids: together they are the whole truth-table cube. Since the non-high tables number at most \(2^{O(s_2 n)}=2^{o(N)}\), all but a vanishing fraction of these hybrids have circuit complexity greater than \(s_2\). Thus the actual low class contains a large, explicit diagonal subfamily whose independent block hybrids are overwhelmingly high.

This construction is a concrete source of incompatible global circuit descriptions. Its entropy per block is \(2^k=\Theta(s_2)\); the \(r=\Theta(N/s_2)\) independent blocks carry \(\Theta(N)\) bits of choice, far more than the \(O(s_2 n)\) bits needed to describe all size-s2 circuits.

## 3. Conditional blockwise-splice theorem

For each diagonal anchor \(w_g\), choose one finite accepting proof tree \(\Pi_g\). Let \(\Lambda_p=\{( (p,u),b):u\in\{0,1\}^k,b\in\{0,1\}\}\) be the two-rail labels belonging to block p.

Assume the following **block-isolation property** for this chosen proof family:

1. For every g and block p, \(\Pi_g\) has a marked occurrence \(v_{g,p}\) of a rule state.
2. The marked occurrences for distinct blocks are pairwise disjoint in the proof tree.
3. The subtree rooted at \(v_{g,p}\) has support contained in \(\Lambda_p\), and the rest of \(\Pi_g\) has support contained in \(\bigcup_{p'\ne p}\Lambda_{p'}\).

Let \(i_{g,p}\in[q]\) be the state label at this occurrence. For a fixed p, these labels partition the \(D=2^{2^k}\) choices of g into at most q classes. Put \(L=D/(2rq)\). The total number of g lying in a class of size less than L for at least one p is at most

\[
r q L=D/2.
\]

Therefore some base g_0 lies in a class of size at least L for every block p. Independently choose \(g_p\) from the class of g_0 at block p. The subtree of \(\Pi_{g_p}\) at \(v_{g_p,p}\) has the same root state as the marked occurrence in \(\Pi_{g_0}\), so it can replace that subtree. Because the marked subtrees are disjoint and block-isolated, doing all r substitutions gives a valid accepting proof whose support is contained in \(z_{\vec g}\). The hybrids are distinct as the g_p vary. Hence the closure accepts at least

\[
L^r=\left(\frac{D}{2rq}\right)^r
\]

distinct block hybrids whenever L is at least 1. If \(q\ge D/(2r)\), the desired exponential lower bound on q already holds. Otherwise L>1, and soundness forces these hybrids all to be in \(\mathrm{SIZE}(s_2)\), so

\[
\log_2 q\ \ge\ \log_2 D-\log_2(2r)-\frac{\log_2|\mathrm{SIZE}(s_2)|}{r}.
\tag{35}
\]

Here \(\log_2D=2^k=\Theta(s_2)\), while

\[
\frac{\log_2|\mathrm{SIZE}(s_2)|}{r}
=O\!\left(\frac{s_2 n\,s_2}{N}\right)
=o(s_2)
\]

for every fixed \(\beta<1\), and \(\log r=O(n)=o(s_2)\). Thus block-isolation would imply

\[
\boxed{q\ge 2^{\Omega(s_2)}.}
\]

This is a real quantitative consequence of repeated context/subproof substitution and low-description repetition. It is much stronger than a single dangerous splice, because it counts the Cartesian product of the choices across all blocks.

### Exact overlap fingerprint on the diagonal family

The localization hypothesis can be weakened for a *single* splice by recording which suffix values the two supports overlap on. Let K be a context from a diagonal proof for g and C a replacement subproof from a diagonal proof for h. For prefix p and suffix u, K can only contain the rail g(u) at coordinate (p,u), and C can only contain h(u). Define

\[
\Omega(K,C)=\{u:\exists p,\ (p,u)\in\operatorname{dom}K\cap\operatorname{dom}C\}.
\]

Then the exact consistency test is

\[
\boxed{K\cup C\text{ is consistent}\iff g(u)=h(u)\text{ for every }u\in\Omega(K,C).}
\tag{36}
\]

Thus the overlap is a semantic fingerprint of the circuit description: if it covers all k-bit suffixes, no different h can be spliced into this context. If its size is t, exactly \(2^{2^k-t}\) k-bit functions h agree with g on it. For a suffix u where g(u) and h(u) differ, a compatible pair cannot overlap at any of the r copies of u. Each copy is then owned by K, by C, or left free. Soundness bounds the total number of free copies by \(\kappa_\square(s_2)\).

This exposes a concrete safe-sharing mechanism. If, for every u, all nonfree copies are owned by the same side across the prefix blocks, the partial splice has a diagonal completion: choose g(u) when K owns the copies and h(u) when C owns them, and fill free copies with that common value. Every such completion is still a k-variable function and hence has size at most s1/4. Dangerous high hybrids therefore require a sufficiently complex *prefix-varying ownership mask* across many suffix values. A lower bound must charge that mask or show that the overlap fingerprint cannot be made complete cheaply. The promise alone does not force the block-local cuts used in the conditional theorem.

## 4. Hostile test: block isolation is not forced by the promise

The diagonal subpromise itself has a linear-size separator: accept exactly when all prefix blocks of the input truth table are identical. This checks \(N-2^k\) equalities between input bits and has Boolean circuit size O(N). It accepts every \(w_g\), and every high-complexity table is rejected because any table constant across the prefix blocks is a function of only k address bits and has circuit size at most \(s_1/4\).

By the standard separator-to-fusion transfer, this restricted promise has a successful O(N)-pair fusion cover. Comparing this fact with (35) proves that block isolation cannot be guaranteed for every anchor in every chosen proof family: in any selection of one accepting proof per diagonal anchor, at least one selected proof must fail the isolation property. Nonlocal interleaving and context/subproof overlap are the mechanisms the next argument must confront. The localization hypothesis is therefore a sufficient condition, not the desired theorem.

This hostile test is useful. It pinpoints what the next theorem must measure: **cross-block mixing inside a proof DAG**. Counting block-local state labels is inadequate because a small closure can enforce the repeated-description condition through nonlocal context structure. The proof-localization route survives only if it is replaced by a dichotomy that charges either (a) many independently replaceable block contexts, or (b) enough cross-block mixing/overlap to force superlinear q.

## 5. Parallel near-linear-cover attack and its first obstruction

For a high table z, every low circuit differs from z on at least d=Omega(s2/n) coordinates by the point-patching argument already recorded in the project. A uniformly random set of t coordinates misses one fixed low table's disagreement set with probability at most exp(-td/N). Circuit counting gives log |SIZE(s1)|=O(s1 log(s1+n))=O(s2) at OPS scales. A union bound therefore needs

\[
t=O\!\left(\frac{N}{d}\log |\mathrm{SIZE}(s_1)|\right)=O(Nn)
\]

samples to certify that z differs from every low circuit. Truncating at N simply returns the full truth table. Even if a z-dependent hitting set were found cheaply, deciding whether an input table's projection lies outside the low projection still has an exponential direct lookup cost. This sampling/anti-checker construction therefore does not produce an `N polylog N` cover. The failure is the same global witness-coherence issue in C-229, not a new local-distance gap. No claim is made that an adaptive non-sampling selector cannot do better.

The other current upper-bound calibration is the diagonal block subpromise: block equality costs O(N), but this test does not recognize arbitrary low circuits. Extending it would require a compact semantic test that all address cofactors share one small gate graph; that is the full-class consistency problem and no such cover was constructed.

## 6. Current assessment and next exact question

The block-replicated construction is actual-promise compatible at the anchor/high end: its diagonal tables lie in \(\mathrm{SIZE}(s_1)\), and almost every independent hybrid lies outside \(\mathrm{SIZE}(s_2)\). But the simple diagonal subfamily has an O(N) separator, so this alone cannot lower-bound the full low/high promise. The missing implication is exactly

\[
q\text{ small}\ \Longrightarrow\ \text{many compatible, independently replaceable block contexts}
\quad\text{or a costly cross-block mixing pattern}.
\]

The next proof attempt should define, for each proof-DAG state and each prefix block, a residual block profile recording (i) which suffix inputs have literals in the state subproof, (ii) which occur in its outside context, and (iii) where the two supports overlap on the same rail. Then seek an entropy inequality for the full q-state grammar, robust to arbitrary endpoint seed sets and alternative proof trees. The conditional estimate (35) supplies the target scale and C-80/C-121/C-134/C-160/C-161/C-213 remain hostile counterchecks.

**Status:** proved exact residual obligation, proved a block-hybrid counting construction, and proved a conditional exponential lower bound under block-isolation. The isolation premise is not automatic and is falsified as a universal claim by an O(N) cover for the diagonal subpromise. No superlinear lower bound for the full Gap-MCSP fusion measure, no near-linear cover for the full promise, and no P-vs-NP proof follow.
