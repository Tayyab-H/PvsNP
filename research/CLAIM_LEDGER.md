# Claim ledger

Status labels: PUBLISHED, PROJECT-PROVED, CONDITIONAL, TESTED, OPEN. Project proofs still require an independent hostile reconstruction.

## C-405   Hard-core preimage readout and implicit-to-explicit transfer

**Statement.** Given a permutation family P_m of circuit size p(m), let H_m(x,z)=inner_product(x,z) mod 2 be hard-core for G_m(x,z)=(P_m(x),z) against nonuniform circuits up to t(m). The full-support sampler E_m((a,x,z)) outputs ((0,P_m(x),z),H_m(x,z)) for a=0 and ((1,x,z),0) for a=1. Its label is f_m(0,y,z)=H_m(P_m^{-1}(y),z), f_m(1,y,z)=0, on a domain of 2m+1 bits. Any arbitrary shared AND/OR/NOT circuit of S gates computing f_m yields a predictor of size S+p(m)+O(1) with success 1; hence S>t(m)-p(m)-O(1).

**Status.** CONDITIONAL: the gate inequality is project-proved under the nonuniform Goldreich-Levin hard-core assumption for the permutation family. The proof is direct composition and imposes no circuit-topology or reuse restriction. The sampler-to-function theorem is not claimed as a new crypto theorem.

**Assumptions and model.** Fan-in-two total AND/OR/NOT gates, free wires and unrestricted fanout; hard-core security must hold against nonuniform circuits at the stated t(m). The truth-table length is L=2^(2m+1). A subexponential t(m)=2^(m^alpha), alpha<1, does not meet high threshold L^beta=2^(beta(2m+1)) for any fixed beta>0; t(m)=2^(delta m) for fixed 0<delta<2 matches for beta<delta/2, up to lower-order terms.

**Scope and counterexamples.** Parity, repeated-block equality, O(N)-total-sparsity parity checks, and simple copy/XOR block relations have O(N)-gate shared readouts. Adding arbitrary unused random bits to a sampler changes neither its support nor its label function. Thus entropy and global dependence alone are not gate charges. The hard-core theorem yields one hard NO table, not a promise-preserving hard label map for the full Gap-MCSP separator. Its table can be materialized by enumerating seed/challenge pairs once and scattering labels in O(L poly(m)) time, so there is no per-address inversion cost to charge. A fixed random sample of table addresses also fails as a proved near-linear accelerator: the direct union bound over all high tables and low descriptions is vacuous at sublinear sample size, and candidate search remains M-way.

**Transfer and frontier.** TR26-091 proves conditional NP-hardness for implicit Gap-MCSP but does not supply an OPS-compatible explicit-table reduction. The explicitization by seed enumeration has runtime 2^r poly(|E|,r,m)+2^m; source reductions have output truth-table length 2^poly(q), so composing an N^(1+epsilon)-size separator does not yield poly(q)-size SAT circuits. The ordinary Gap-MCSP lower bound stays N-O(N^beta log N)-1; native rho stays N-o(N); the full-promise enumeration separator stays O(N 2^(O(N^beta))). See [C-405](C405_HARDCORE_PREIMAGE_READOUT_AND_IMPLICIT_TRANSFER_AUDIT_2026-09-30.md), [OPS](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), and [TR26-091](https://eccc.weizmann.ac.il/report/2026/091/download/), [Goldreich-Levin, STOC 1989](https://doi.org/10.1145/73007.73010).

## C-404   Cut-transcript capacity and promise-preserving restrictions

**Statement.** Any fan-in-two `S`-gate circuit for `f` induces, across every input partition, a deterministic communication protocol of cost at most `2S+1`. The single-cut bound caps at `N/2+1`, and summing partitions does not improve it because a wire can be charged on every partition. For a linear fingerprint separator that accepts the low table `0^N` and rejects every high table, the kernel fiber at `0^N` must have at most `K2=2^(O(N^beta log N))` elements; consequently the fingerprint width is at least `N-O(N^beta log N)`.

**Additional construction.** There exists a subspace `V<=F_2^N` of codimension `d=O(N^beta log N)` such that its intersection with all non-High tables is exactly a coordinate subspace `W` of dimension `k=Theta(N^beta/(log N)^2)` consisting of low tables. Its systematic encoder has `O(N^(1+beta)log N)` AND/OR/NOT gates. The induced promise label is membership in `W`, hence has an `O(N)`-gate circuit; this is a counterexample to count-only hard-restriction arguments.

**Status.** PROJECT-PROVED (the simulation, fiber-count, and subspace-existence constructions); cut route closed at the linear scale. Restriction-composition transfer is PROJECT-PROVED; no hard promised restriction found.

**Assumptions.** Ordinary fan-in-two total gates, unrestricted fanout, OPS thresholds `s1=N^beta/(c log2 N)` and `s2=N^beta`, and the promise labels only. Hash claim applies to linear maps and the candidate-union fingerprint construction specified in C-404.

**Proof location / dependencies.** [C-404](C404_CUT_TRANSCRIPT_CAPACITY_AND_PROMISE_RESTRICTIONS_2026-09-30.md), Sections 2–5; OPS Theorem 1.4.

**Counterexamples / scope.** Parity, repeated-block equality, sparse parity-check predicates, and simple global block relations are linear-size shared circuits. These refute local-incidence charges, not Gap-MCSP lower bounds. The fingerprint argument does not cover arbitrary nonlinear compression.

**Quantitative effect.** None beyond C-403's `N-O(N^beta log N)` gate lower bound. Native fusion q and runtime/description costs are not changed.

**Additional literature check.** The 2026 Carmosino–Dang–Jackman gate-elimination refuters concern fixed functions and give no promise-preserving reduction to Gap-MCSP; retain as a technique lead only.

## C-01   Fusion cover lower-bounds intersection complexity

**Statement.** For finite nontrivial A subset Gamma and nonempty generator family B, rho(A,B) <= D_cap(A|B) <= rho(A,B)^2, and rho(A,B) = D_cap^cyc(A|B).

**Status.** PUBLISHED, Cavalar and Oliveira Theorems 22, 24, 30.

**Assumptions.** Definitions of semi-filter, being above an anchor, pair preservation, and intersection complexity match the paper.

**Proof location / dependencies.** [Cavalar and Oliveira, Boolean Circuit Complexity and Two-Dimensional Cover Problems](https://arxiv.org/abs/2503.14117), sections 3.1-3.4.

**Counterexamples / scope.** This is a characterization, not a lower-bound technique by itself.

**Unrestricted relevance.** Yes: any fixed-basis circuit separator can be converted to a De Morgan circuit with constant-factor size overhead. The resulting set construction has total operation count at most that size, and its AND count is at least D_cap, hence at least rho.

## C-02   Promise-ground-set transfer for Gap-MCSP

**Statement.** Set Gamma=Y union Z, A=Y, U=Z, and B to the 2N literal sets restricted to Gamma. Then the project rho_GapMCSP is exactly rho(A,B), and D(A|B) is the De Morgan circuit complexity of the promise classifier. Any fixed-basis circuit separator of size S yields D(A|B)=O(S), so rho<=D_cap<=D=O(S).

**Status.** PROJECT-PROVED / SOURCE-VERIFIED THIS TURN.

**Assumptions.** Both promise sides are nonempty; correctness is required on Y and Z; the gap is excluded from Gamma; circuits use a fixed finite complete basis.

**Proof location / dependencies.** Project research synthesis section 7.1; project audit section 7; C-01. This uses rho<=D_cap, not the local compiler from a cover to a separator.

**Counterexamples / scope.** Another totalization or generator family would need a new identification.

**Unrestricted relevance.** Yes, all nonuniform circuit separators are covered; therefore any polynomial-time SAT decider would be covered.

## C-03   Near-linear promise-cover lower bound

**Statement.** If m pair rules derive empty for a fixed low-circuit anchor, the first empty-intersection rule has a proof DAG with at most m+1 matching-literal leaves. These consistent coordinate restrictions must exclude every high-circuit table. If M2 counts tables below s2, then rho_GapMCSP>=N-log2(M2)-1=N-O(s2 log(n+s2))-1. At s2=N^beta, fixed beta<1, this is (1-o(1))N.

**Status.** PROJECT-PROVED; finite trace checks are corroboration only.

**Assumptions.** Project closure semantics and matching-literal generators; standard circuit-counting bound M2=2^(O(s2 log(n+s2))).

**Proof location / dependencies.** [Research synthesis](../P_vs_NP_Research_Synthesis_2026-09-23.docx), Proposition 21.7; [project audit](../P_VS_NP_PROJECT_AUDIT_2026-08-24.md), sections 21 and 7.1.

**Counterexamples / scope.** This invariant cannot exceed N-O(log M2), since it charges distinct truth-table coordinates. Experiments check small cases only.

**Unrestricted relevance.** Via C-02 it lower-bounds arbitrary circuits, but only linearly.

## C-04   Gap-MCSP hardness magnification

**Statement.** For universal c, if for some epsilon>0 and every sufficiently small fixed beta>0, Gap-MCSP[2^(beta n)/(c n),2^(beta n)] is not in Circuit[N^(1+epsilon)], then NP is not contained in Circuit[poly]. The published notation is a circuit-family non-membership statement; do not strengthen it to hardness at every sufficiently large length unless separately proved.

**Status.** PUBLISHED, Oliveira, Pich, and Santhanam Theorem 1.4.

**Assumptions.** Exact parameter regime and asymptotic quantifiers; nonuniform circuits.

**Proof location / dependencies.** [Hardness Magnification Near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4.

**Counterexamples / scope.** It is an implication; the needed premise is open. Since P is contained in P/poly, its conclusion implies P != NP.

**Unrestricted relevance.** Yes.

## C-05   Conditional cover-to-separation route

**Statement.** A superlinear rho_GapMCSP lower bound in the exact C-04 regime implies the C-04 circuit lower bound by C-01/C-02, then P != NP.

**Status.** CONDITIONAL; implication chain established, premise OPEN.

**Assumptions.** Same epsilon/beta quantifiers; absorb basis constants with exponent slack.

**Proof location / dependencies.** C-01 to C-04; project audit section 7.

**Counterexamples / scope.** Existing lower bound is N-o(N).

**Unrestricted relevance.** Yes, if the premise is proved.

## C-13 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â High-anchor interpolation gives only a sublinear complement-side bound

**Statement.** Let \(N=2^n\), \(Y\) be the truth tables of circuit size at most \(s_1\), \(Z\) those of size at least \(s_2\), and \(\mathcal B\) the \(2N\) literal slices on \(\Gamma=Y\sqcup Z\). The project leaf-trace argument, applied with target \(Z\) and opposite side \(Y\), gives only
\[
\rho(Z,\mathcal B)=\Omega(s_1/n)=\Omega(N^\beta/n^2)
\]
at \(s_1=N^\beta/(cn)\). It does not give \(N-\log M_1\).

**Status.** PROJECT-DERIVED ELEMENTARY LEMMA, independently reconstructed this turn. It is sublinear and does not improve the leading \(N-o(N)\) bound from C-03.

**Proof.** Fix a high anchor \(a\in Z\). The first empty intersection in a trace over \(Y\) uses at most \(m+1\) matching literal leaves if the pair list has \(m\) rules. If these leaves fix \(q\) distinct truth-table coordinates, their subcube consists of all tables matching \(a\) on those positions and is disjoint from \(Y\). But any prescribed 0/1 pattern on \(q\) distinct positions can be interpolated by a Boolean DNF: use one minterm for each position prescribed 1 and disjoin them. With fan-in-two gates this costs at most \(O(qn)\) gates. Thus if \(q\le s_1/(C n)\) for a suitable fixed constant \(C\), this subcube contains a table in \(Y\), a contradiction. Therefore \(q>\Omega(s_1/n)\), and \(m+1\ge q\) proves the claim. Both constant truth tables in \(Y\) ensure the matching literal generators required by the high-anchor semi-filters are nonempty.

**Correction of failed argument.** The statement ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“the cube contains no low table, therefore its size is at most \(M_1\)ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â is false. The cube may contain gap and high tables. The attempted estimate \(\rho(Z)\ge N-\log M_1-1\) and the derived \(2N-o(N)\) gate bound are withdrawn.

**Scope.** By complement duality this contributes to \(D_\cup(Y\mid\mathcal B)\), but only a lower-order term. The one-sided \(N-o(N)\) result C-03 remains the strongest asymptotic lower bound recorded here.

## C-14 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Acyclic circuit complexity is the minimum sufficient magnification target

**Statement.** For the promise classifier on \(\Gamma=Y\sqcup Z\), the OPS theorem only requires a slightly superlinear lower bound on ordinary (acyclic) circuit size. In the literal-slice model it suffices to prove \(D(Y\mid\mathcal B)>N^{1+\epsilon}\) in the exact theorem quantifiers. A lower bound \(\rho(Y,\mathcal B)>N^{1+\epsilon}\) is sufficient but stronger, since \(\rho\) is cyclic intersection complexity and \(\rho\le D_\cap\le D\).

**Status.** PROVED implication / route refinement; not a new lower bound.

**Proof.** Each generator in \(\mathcal B\) is the truth set, restricted to \(\Gamma\), of a positive or negative input literal. Translating each AND gate to intersection and each OR gate to union shows that every De Morgan circuit separator of size \(S\) has \(D(Y\mid\mathcal B)\le S\) on the promise domain. Conversely, every set-construction sequence gives a De Morgan circuit on the full truth-table input whose behavior on \(\Gamma\) is the required separator. A circuit over any fixed fan-in-two complete basis has a constant-factor De Morgan simulation. Thus if \(D>N^{1+\epsilon'}\) for infinitely many lengths, with \(\epsilon'>\epsilon\), no arbitrary-basis circuit of size \(N^{1+\epsilon}\) can solve the promise at those lengths once \(N\) is large enough; exponent slack absorbs the conversion constant. Apply OPS with the smaller exponent.

**Proof location / dependencies.** C-01, C-02, and C-04; CavalarÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œOliveira definitions of discrete and intersection complexity, and OPS Theorem 1.4.

**Unrestricted relevance.** This exactly identifies the weakest missing separator theorem in the selected magnification route. It does not make that theorem easier or prove it.

## C-06   Source-plus-tape description floor

**Statement.** A randomized reduction with m-bit source and rho(m)-bit fixed tape satisfies K_U^{tau(t)}(x|y) <= m+rho(m)+O(log(m+rho(m))) if reduction and simulation fit the NO clock.

**Status.** PROJECT-PROVED elementary lemma; no separation consequence.

**Assumptions.** Tape is included in the description and the clock covers the reduction.

**Proof location / dependencies.** [ideas.md](../ideas.md), Idea 176; [New Model.MD](../New%20Model.MD), section 2.57.

**Counterexamples / scope.** HIR already samples an n-bit message, so this floor is compatible with its NO guarantee; list-security is the substantive hiding property.

**Unrestricted relevance.** Constrains reduction parameters, not arbitrary SAT algorithms.

## C-07   Fixed-clock Kolmogorov target

**Statement.** For R_q={x:K^(n^q)(x)>=|x|-1}, the project compression argument forces any polynomial-time decider to have degree at least q.

**Status.** PROJECT-PROVED route result; no separation.

**Assumptions.** Fixed-clock and coding conventions in New Model.

**Proof location / dependencies.** [New Model.MD](../New%20Model.MD), fixed-clock K sections.

**Counterexamples / scope.** Any fixed polynomial degree remains possible, so increasing q across different languages is not a contradiction.

**Unrestricted relevance.** Does not currently separate P from NP.

## C-08   Finite experiments

**Statement.** Workspace scripts report exhaustive small closure checks, candidate-template covers, affine-feature tests, and proof-DAG tracing.

**Status.** TESTED only.

**Assumptions.** Each script s finite parameter range and implementation.

**Proof location / dependencies.** [Research synthesis](../P_vs_NP_Research_Synthesis_2026-09-23.docx),  21 25.

**Counterexamples / scope.** No finite check proves the asymptotic all-filter lower bound.

**Unrestricted relevance.** None without a separate extrapolation theorem.

## C-09 - One pair can hit many affine-anchor filters

**Statement.** Suppose U contains at least one table realizing every pattern on any three fixed coordinates. For distinct coordinates i,j, set G_(k,b)=U intersect {z:z_k=b}, E=G_(i,0) union G_(j,0), and H=G_(i,1) union G_(j,1). For every anchor a with a_i != a_j, the upward closure F_a of its matching literal generators is a semi-filter above a that does not preserve (E,H).

**Status.** PROJECT-DERIVED ELEMENTARY LEMMA, proved in this audit; no novelty claim about the literature.

**Assumptions.** Every one-coordinate generator is nonempty and U realizes the specified three-coordinate patterns. At the Gap-MCSP parameters with s2=N^beta for fixed beta<1, the standard circuit-counting bound gives fewer than 2^(N-3) tables below s2 for large N, so every pattern on three coordinates has a high-circuit extension.

**Proof location / dependencies.** Proof: E and H each contain a matching generator when a_i != a_j. Their intersection is the union of the two off-diagonal i,j slices. Three-coordinate fullness ensures no matching generator G_(k,a_k) is contained in that intersection, so it is not in F_a. Thus F_a contains E,H but not E intersect H. Distinct anchors give distinct such filters: a matching slice at a coordinate where two anchors differ is in one upward closure, and two-coordinate fullness keeps it out of the other.

**Counterexamples / scope.** Choosing i,j as the truth-table rows 0^n and e_1, exactly N affine functions have unequal values there; all have circuit size O(n), hence are low anchors for large n. So this one pair violates at least N distinct explicit anchored filters. It does not cover every semi-filter above any anchor and gives no upper or lower bound on rho.

**Unrestricted relevance.** This falsifies simple arguments that charge each pair only O(1) anchor-filter interactions. It does not constrain arbitrary SAT algorithms or advance the magnification bound by itself.

## C-10 - One pair hits all Hamming-ball threshold semi-filters

**Statement.** Fix 0<beta<=1/2 and c>0. Put N=2^n, s2=N^beta, s1=s2/(c n), let U be truth tables of circuit complexity at least s2, and let Y be truth tables of complexity at most s1. Assume the standard circuit-counting bound M(t)<=2^(C0 t log2(n+t)). Choose a constant K>4C0 and d=ceil(K s2). For each a in Y, let H_a be the Hamming ball of radius d around a intersected with U, and let mu_a be uniform on H_a. For all sufficiently large n: (i) every matching literal slice G_(i,a_i) has mu_a-mass greater than 3/4; and (ii) there is a partition U=E disjoint-union H such that mu_a(E)>1/4 and mu_a(H)>1/4 for every a in Y. Consequently F_a={S subseteq U:mu_a(S)>1/4} is a semi-filter above a, and the same pair (E,H) violates every selected F_a.

**Status.** PROJECT-PROVED asymptotic lemma; proof below. This is a no-go for a proposed dual support, not a lower bound on rho.

**Assumptions.** The standard circuit-counting estimate; fixed beta in (0,1/2], fixed c>0; the Cavalar-Oliveira definition of semi-filter (nonempty upward-closed family excluding empty) and pair preservation only for the tested list.

**Definition source.** Cavalar and Oliveira, Definitions 18-20, [Boolean Circuit Complexity and Two-Dimensional Cover Problems](https://arxiv.org/abs/2503.14117).

**Proof.** Write V=|B(a,d)|, independent of a. Since d=o(N), V>=binom(N,d)>=(N/d)^d, so log2 V >= (K(1-beta)-o(1))s2 log2 N. The number M2 of tables below s2 is at most 2^(C0 s2 log2(n+s2))=2^(C0(beta+o(1))s2 log2 N). Since K>4C0 and beta<=1/2, M2/V<=2^(-Omega(s2 log N)). Thus |H_a|>=V-M2>=V/2, uniformly in a. Under the uniform measure on the full ball, a fixed coordinate differs from a with probability at most d/N, since the average Hamming distance is at most d and coordinates are symmetric. After deleting the M2 low tables, the mismatch probability is at most (d/N)/(1-M2/V)=o(1). Hence every matching literal slice has mu_a-mass >3/4 for large n.

The circuit count for Y gives log2 |Y|=O(s1 log(n+s1))=O(s2) for fixed beta,c. Independently color every z in U with one of two colors. For a fixed a, Hoeffding gives probability at most 2 exp(-|H_a|/8) that either color has mu_a-mass outside (1/4,3/4). Since min_a |H_a|>=2^(Omega(s2 log N)) while log |Y|=O(s2), a union bound shows that some coloring balances both colors for every a. Let E,H be the color classes. The family F_a is nonempty because U belongs to it, upward closed by monotonicity of mu_a, and excludes empty. It contains every matching generator by the >3/4 bound, so it is above a. But E,H are both in F_a and E intersect H=empty is not. Thus the same pair violates all F_a.

**Counterexamples / scope.** The theorem covers one threshold semi-filter per low anchor, constructed from local Hamming-ball measures. It does not cover all semi-filters above any anchor. In particular, it does not disprove a fractional dual supported on a more varied family.

**Unrestricted relevance.** It directly allows arbitrary endpoints and shows that this natural family cannot witness a lower bound: one pair covers its entire support.

## C-11 - A mass-one full filter cannot lie above a low anchor

**Statement.** Let U be the high-table set and let a be a low truth table outside U. No probability measure mu on U can assign measure one to every matching literal slice G_(i,a_i).

**Status.** ELEMENTARY.

**Assumptions.** Truth-table coordinates range over all N inputs; G_(i,a_i)={z in U:z_i=a_i}.

**Proof location / dependencies.** Their intersection over all coordinates is {a} intersect U=empty. If each slice had measure one, their finite intersection would have measure one, impossible for a probability measure on U.

**Counterexamples / scope.** The family {S:mu(S)=1} is globally intersection-closed, but the project semi-filters need not be. This fact only says a full mass-one filter cannot contain all anchor generators; it is not an obstruction to the semi-filter cover problem and must not be used to reject nontrivial threshold families.

**Unrestricted relevance.** None by itself; it narrows a candidate dual construction.

## C-12 - Under P=NP, a wrong SAT circuit has a polynomial-time counterexample finder

**Statement.** Assume SAT has a deterministic polynomial-time decider D. There is a deterministic polynomial-time search algorithm which, on input (C,1^n), outputs a string x in {0,1}^n with C(x) != SAT_n(x) if one exists, and otherwise reports that none exists.

**Status.** CONDITIONAL ELEMENTARY LEMMA; proved here by search-to-decision.

**Assumptions.** D decides the totalized SAT_n predicate correctly; n is given in unary.

**Proof location / dependencies.** The prefix predicate Q(C,1^n,p) says that some n-bit x extending p satisfies C(x) != SAT_n(x). Guessing x and evaluating C,D shows Q is in NP. Under P=NP, Q is in P. Query Q successively on the two possible next-bit prefixes; after at most n decisions this finds a counterexample whenever one exists. Each query has length polynomial in |C|+n, so total runtime is polynomial in the combined input length.

**Counterexamples / scope.** This proves standard-model polynomial-time witness finding assuming P=NP. It does not show that S^1_2 proves the procedure correct, which is the formalized hypothesis needed in the Pich-Santhanam route.

**Unrestricted relevance.** It quantifies over arbitrary circuit descriptions C; it is not tied to a solver architecture.

## C-15 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â No fixed query set is an anti-checker for all high-complexity truth tables

**Statement.** Let $N=2^n$. Fix any set $Q\subseteq\{0,1\}^n$ of at most $t=2^{10\beta n}$ query points, and let the high threshold be $s_2=2^{\beta n}$, for fixed $0<\beta<1/10$. For all sufficiently large $n$, there is a truth table $f$ of circuit complexity greater than $s_2$ that is zero on every point of $Q$. Therefore $Q$ is not an anti-checker for all functions above the high threshold, even against the constant-zero circuit.

**Status.** PROVED BY COUNTING; an elementary obstruction to nonadaptive samples, not a new circuit lower bound.

**Proof.** There are exactly $2^{N-|Q|}\ge 2^{N-t}$ truth tables that are zero on $Q$. The number of truth tables computable by circuits of size at most $s_2$ is at most $2^{O(s_2\log(n+s_2))}=2^{O(n2^{\beta n})}$, by encoding a circuit gate by gate. Because fixed $\beta<1/10$, both $t=2^{10\beta n}$ and $n2^{\beta n}$ are $o(2^n)=o(N)$. Hence $N-t>O(n2^{\beta n})$ for sufficiently large $n$, so more zero-on-$Q$ functions exist than there are low-circuit functions. At least one such $f$ has complexity greater than $s_2$, and the constant-zero circuit agrees with it on all of $Q$.

**Consequence for the active route.** OPS's anti-checker list cannot be a fixed set of sample points: the list must depend on the entire input truth table. The relevant unresolved object is therefore an adaptive selector circuit $A_{n,\beta}:\{0,1\}^N\to(\{0,1\}^n)^t$ such that every $f$ of complexity $>s_2$ is anti-checked by its output against every size-$s_1=s_2/(10n)$ circuit. OPS prove that $\mathrm{NP}\subseteq\mathrm{Circuit[poly]}$ yields such selectors of size $N^{1+O(\beta)}$. A lower bound excluding these selectors in the corresponding quantifier regime would be sufficient for separation; this lemma itself only rules out nonadaptive samples.

**Proof location / dependencies.** Elementary circuit counting. Compare OPS, [Hardness Magnification Near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Lemma 4.1 and Theorem 1.4.

**Generality audit.** This argument fixes $Q$ before $f$ is chosen. It says nothing about an adaptive circuit whose queried coordinates depend on all $N$ bits of $f$; that adaptive lower bound is the open step.
## C-16 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â A valid anti-checker selector induces a descent to the high-threshold boundary

**Statement.** Fix a total map $A$ that, on every table $f$ with $CC(f)>s_2$, outputs a sample anti-checking every circuit of size at most $s_1$. Fix any circuit $D$ of size at most $s_1$. Starting from any $f_0$, repeatedly replace the bits at all queried locations $A(f_i)$ by the corresponding values of $D$. The process terminates after at most $N$ strict rounds at a table $f_*$ satisfying $CC(f_*)\le s_2$. Its Hamming distance from $f_0$ is exactly the number of distinct bits changed.

**Status.** PROVED ELEMENTARY DESCENT; no lower bound or separation follows.

**Proof.** Use $d_H(f_i,D)$ as a nonnegative integer potential. If $CC(f_i)>s_2$, the anti-checker property supplies a queried point at which $f_i$ disagrees with $D$, so replacing every queried bit by its $D$-value strictly decreases the potential. At most $N$ bits can be changed. The process therefore reaches $f_*$ where all queried labels agree with $D$. If $CC(f_*)>s_2$, the selector property would give a disagreement, contradiction. Since every updated coordinate is set to the fixed value $D(y)$ and is never changed away from it, the number of coordinates changed equals $d_H(f_0,f_*)$.

**Stronger-start estimate.** If $CC(f_0)>2s_2$, then $d_H(f_0,f_*)=\Omega(s_2/n)$: otherwise, starting from a circuit of size at most $s_2$ for $f_*$, patch each differing truth-table point with one $n$-bit minterm, obtaining a circuit for $f_0$ of size $s_2+O(d_H(f_0,f_*)n)<2s_2$.

**Failure point.** The endpoint may have any complexity up to $s_2$, including the entire promise gap; it need not be a low instance of size at most $s_1$. Moreover, one batch can change $t\gg s_2/n$ bits, so the stronger-start estimate gives no contradiction. Updating one mismatch per round forces many rounds but does not force the selector circuit itself to be large.

**Proof location / dependencies.** Direct descent using the selector guarantee and pointwise DNF patching. It is an adversarial audit of the self-reference idea in Idea 182.
## C-17 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Any valid adaptive selector needs a large range of query sets

**Statement.** In the OPS parameters, let $s_2=2^{\beta n}$, $t=2^{10\beta n}$, and $0<\beta<1/10$ be fixed. If a selector $A$ is valid for every $f$ with $CC(f)>s_2$, then the number $q$ of distinct query sets in its range must satisfy
$$
q\,t\ge N-\log_2 M_2,
$$
where $M_2=|\{f:CC(f)\le s_2\}|$. In particular, circuit counting gives $q\ge(1-o(1))N/t=(1-o(1))N^{1-10\beta}$.

**Status.** PROVED BY COUNTING; quantitative adaptation requirement, not a circuit-size lower bound.

**Proof.** Let $\mathcal R$ be the selector's range after removing repeated query locations from each output, and set $U=\bigcup_{S\in\mathcal R}S$. Then $|U|\le qt$. If $qt<N-\log_2M_2$, more than $M_2$ truth tables are zero on $U$, so at least one has circuit complexity greater than $s_2$. For this $f$, the output $A(f)$ is a subset of $U$ and every label there is zero. The constant-zero circuit agrees on the whole sample, contradicting validity. Thus $qt\ge N-\log_2M_2$. Since $\log_2M_2=O(s_2\log(n+s_2))=o(N)$ and $t=N^{10\beta}$, the asymptotic bound follows.

**Limitation.** Range size alone does not yield a circuit lower bound. A simple non-selector circuit can attain this range by making one query address a projection of $\lceil\log q\rceil$ truth-table input bits (choosing $q$ addresses) and making the other query points fixed outside that address set. This takes at most $O(tn)$ output wiring, far below $N^{1+\epsilon}$ here. It does not satisfy the anti-checker property; it shows that output diversity itself is cheap. The hard task is routing each high-complexity input to a sample that is actually valid for its labels.
**Proof location / dependencies.** C-15 and the standard circuit-counting bound. The explicit failure mode for turning range size into circuit size is included above.
## C-18 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Sparse hard tables force exponentially many anti-checker samples

**Statement.** Fix the fan-in-two circuit basis and its circuit-count constant. There is $\beta_0>0$ such that, for every fixed $0<\beta<\min(\beta_0,1/10)$ and all sufficiently large $n$, any family $\mathcal S$ of subsets of $\{0,1\}^n$, each of size at most $t=2^{10\beta n}$, that has the following property

> for every truth table $f$ with $CC(f)>s_2=2^{\beta n}$, some $S\in\mathcal S$ is an anti-checker for $f$ against all circuits of size at most $s_1=s_2/(c n)$,

must satisfy $|\mathcal S|\ge 2^{\eta s_2/n}$ for a constant $\eta=\eta(\beta,c,\mathcal C)>0$, where $\mathcal C$ is the fixed circuit basis. The selector's range is such a family, so this also lower-bounds its number of distinct output samples.

**Status.** PROJECT-DERIVED COMBINATORIAL LEMMA; proof below. It strengthens C-17's coordinate-union bound on range size but still gives no circuit-size lower bound. Chen et al. already refute the related static Anti-Checker Hypothesis in a different parameter regime; the sparse-support proof below independently recovers that kind of obstruction and gives a quantitative form for OPS parameters.

**Proof.** Let $s=s_2$ and $N=2^n$. Circuit counting gives at most
$$
M_s\le 2^{C_0s\log_2(n+s)}
$$
truth tables of circuit size at most $s$, for a basis-dependent constant $C_0$. Since $\log_2(n+s)=\beta n+O(1)$, $\log_2 M_s\le (C_0\beta+o(1))ns$. In contrast,
$$
\log_2\binom Ns\ge s\log_2(N/s)=(1-\beta)ns.
$$
Choose $\beta_0$ small enough that $(1-\beta)>2C_0\beta$ for $\beta<\beta_0$. Then exponentially more weight-$s$ truth tables exist than tables of circuit size at most $s$.

Set $r=\lfloor s/(4cC_dn^2)\rfloor$, where $C_d$ is a constant such that a DNF with $r$ minterms on $n$ variables has circuit size at most $C_d rn$. Choose a support $R$ uniformly among all $s$-subsets of $\{0,1\}^n$. For any fixed candidate sample $S$ of size at most $t$, the random variable $X=|R\cap S|$ is hypergeometric, and
$$
\Pr[X\ge r]\le \binom{|S|}{r}(s/N)^r\le\left(\frac{e t s}{rN}\right)^r.
$$
Because $r=\Theta(s/n^2)$ and $t/N=2^{-(1-10\beta)n}$, the parenthesized ratio is at most $2^{-(1-10\beta)n/2}$ for sufficiently large $n$. Hence
$$
\Pr[X\ge r]\le 2^{-\Omega((1-10\beta)s/n)}.
$$
If $|\mathcal S|<2^{\eta s/n}$ for a sufficiently small $\eta>0$, a union bound shows that at least half of all supports $R$ satisfy $|R\cap S|<r$ for every $S\in\mathcal S$.

There are still more than $M_s$ such supports, by the circuit-counting comparison above. Choose one for which $f=1_R$ has $CC(f)>s$. On each $S\in\mathcal S$, the table $f$ has fewer than $r$ ones. A DNF containing one exact $n$-literal minterm for each such one agrees with $f$ on all of $S$ and has size at most $C_d rn\le s_1$. Thus no $S\in\mathcal S$ is an anti-checker for this $f$, contradicting the family property. Therefore $|\mathcal S|\ge2^{\eta s/n}$.

**Corollary for the named Anti-Checker Hypothesis.** For any fixed $0<\lambda<1$, put $s=2^{n^\lambda}$. Then $\log\binom{2^n}{s}=(1-o(1))ns$, while the circuit-description exponent is $O(s\log(n+s))=O(sn^\lambda)=o(ns)$. Thus many weight-$s$ supports define functions of circuit complexity greater than $s$. For any fixed $0<\epsilon<1$, put $t=2^{n^{1-\epsilon}}$. The same hypergeometric argument gives failure probability $2^{-\Omega(s/n)}$ per candidate set, while a proposed family has only $2^{O(n)}$ sets. Since $s/n\gg n$, one sparse hard truth table defeats the entire family. This independently recovers the published refutation by Chen et al. [Beyond Natural Proofs](https://arxiv.org/abs/1911.08297), whose proof proceeds through a locality/formula-lower-bound argument. The exponent comparison here applies for every fixed $\lambda\in(0,1)$ because $n^\lambda=o(n)$; it is separate from the OPS regime $s=2^{\beta n}$, where small $\beta$ is needed.

**Scope and bottleneck.** For OPS parameters the selector range can have as many as $2^{tn}$ samples, and $tn\gg s/n$. The range lower bound therefore fits comfortably inside the output space and does not imply a circuit lower bound. The unresolved task remains the computational routing from each hard input to a valid sample, not the existence or number of candidate samples alone.

Since $q\le N^t=2^{tn}$ for an ordered list of $t$ query points, the range theorem also forces $tn\ge\eta s/n$, or $t\ge\eta s/n^2$. This query-count corollary is weaker than the OPS choice $t=s^{10}$ and still gives no circuit-size lower bound.

## C-19 - Sparse-support anti-checking forces positive-point capture, which is cheap

**Statement.** In the OPS parameters, every valid selector on a high-complexity table $f=1_R$ with $|R|=s_2$ must output at least $r=\Omega(s_2/n^2)$ distinct points from $R$. This is necessary because otherwise a DNF with one exact minterm for each sampled 1-point has size at most $s_1$ and agrees with $f$ throughout the sample. However, the positive-point capture condition by itself has a circuit of size $O(Nn^3)$: a sorting network can sort all $N$ records $(f(i),i)$ by the first component and output the first $t$ indices. Since $t\ge s_2$, this includes every positive coordinate on weight-$s_2$ inputs.

**Status.** PROVED NECESSARY CONDITION AND EXPLICIT LIMIT; not a selector construction and not a circuit lower bound.

**Proof.** For a weight-$s_2$ support, C-18's interpolation argument says any sample with fewer than $r=\lfloor s_2/(4cC_dn^2)\rfloor$ positive coordinates is agreed with by a size-$s_1$ DNF. Thus every sample output by a valid selector must contain at least $r$ positives. For the limitation, sort the $N$ records carrying each truth-table bit and its $n$-bit coordinate label using a fan-in-two sorting network. A sorting network with $O(N\log^2N)$ compare-exchange gates, each implementable with $O(n)$ Boolean gates, has size $O(Nn^3)$. Its first $t$ labels contain all $s_2$ positive positions whenever $s_2\le t$. This satisfies the necessary positive-capture condition on every weight-$s_2$ support but may still output a sample on which some small circuit agrees; in particular, positive capture alone does not establish anti-checking.

**Learning.** The sparse hard-support adversary yields the range theorem because it bounds the number of candidates simultaneously defeated. It does not make the selector computation hard: a circuit can find all positives of a sparse truth table in near-linear size. A proof from this route must exploit how zeros and all competing small circuits constrain the chosen sample, beyond merely requiring many positive hits.

## C-20 - Anti-checking is an instance-dependent hitting-set problem

**Statement.** For a fixed high-complexity truth table $f$, define the error family
$$
\mathcal E_f=\bigl\{\{x:f(x)\ne D(x)\}: CC(D)\le s_1\bigr\}.
$$
A query set is an anti-checker exactly when it hits every member of $\mathcal E_f$. Moreover, each error set has size greater than $(s_2-s_1)/(C_dn)$, where $C_d$ is a fixed point-patching constant. In the OPS parameters, the generic random-sample union bound using only this minimum error-set size and circuit counting certifies a hitting set only at the vacuous scale $O(\beta nN)$, larger than the entire universe.

**Status.** PROVED REFORMULATION AND QUANTITATIVE LIMIT OF A GENERIC METHOD; no lower bound on instance-dependent hitting sets.

**Proof.** If a size-$s_1$ circuit $D$ disagreed with $f$ at $h$ points, patch $D$ at those exact truth-table points using $h$ minterms. This gives a circuit for $f$ of size at most $s_1+C_dhn$. Since $CC(f)>s_2$, necessarily $h>(s_2-s_1)/(C_dn)$. By definition, a set $Q$ is an anti-checker precisely if $Q\cap E\ne\varnothing$ for every $E\in\mathcal E_f$.

For a uniformly random $m$-point sample, a fixed error set of size $\delta$ is missed with probability at most $\exp(-m\delta/N)$. A union bound over at most $M_1=2^{O(s_1\log(n+s_1))}$ circuits gives the sufficient scale $m=O((N/\delta)\log M_1)$. Under OPS parameters, $\delta=\Omega(s_2/n)$ and $\log M_1=O(\beta s_2)$, so this generic estimate is $m=O(\beta nN)$, which exceeds $N$ for sufficiently large $n$. It therefore cannot certify the much shorter $t=s_2^{10}$ sample from only minimum distance and a count of circuits.

**Learning.** An anti-checker is an instance-dependent transversal of the error sets of all low circuits. The hard part is not that the errors are empty or too small individually; it is exploiting their structured overlap, conditional on the full table $f$, to find a short transversal. Generic VC/epsilon-net reasoning that forgets this dependence gives a sufficient bound of order $nN$, rather than the OPS target $t=s_2^{10}$; its ratio to that target is $nN/s_2^{10}$, so it supplies no useful sublinear sample bound in this regime.

## C-21 - Minimax gives a short, strong anti-checker for each hard table

**Statement.** Let $f:\{0,1\}^n\to\{0,1\}$ and let $\mathcal C_s$ be the set of circuits of size at most $s$ in a fixed fan-in-two basis. For every fixed $0<\varepsilon<1/4$, if
$$
CC(f)>C_\varepsilon n(s+1)
$$
for a sufficiently large constant $C_\varepsilon$, then there is a multiset $Q_f$ of
$$
O\!\left(\frac{\log |\mathcal C_s|}{\varepsilon^2}\right)
=O\!\left(\frac{s\log(n+s)}{\varepsilon^2}\right)
$$
inputs such that every $D\in\mathcal C_s$ disagrees with $f$ on at least a $1/2-2\varepsilon$ fraction of $Q_f$.

**Status.** PROVED HERE FROM FINITE MINIMAX AND Hoeffding; this is a known anti-checker theorem of Lipton and Young, not a new separation result.

**Proof.** Make a zero-sum game whose rows are circuits $D\in\mathcal C_s$, whose columns are inputs $x\in\{0,1\}^n$, and whose payoff is $1[D(x)\ne f(x)]$. Let
$$
v=\max_{\mu}\min_{D\in\mathcal C_s}\mathbb E_{x\sim\mu}[1[D(x)\ne f(x)]].
$$
By finite minimax, $v=\min_{\pi}\max_x\mathbb E_{D\sim\pi}[1[D(x)\ne f(x)]]$. If $v<1/2-\varepsilon$, draw $k=\lceil(n\ln 2+1)/(2\varepsilon^2)\rceil$ circuits independently from the minimizing distribution $\pi$. For each fixed $x$, Hoeffding's inequality bounds the probability that their majority is wrong by $e^{-2\varepsilon^2k}$. A union bound over all $2^n$ inputs is less than one, so some such majority circuit computes $f$ exactly. Its size is $O(k(s+1))=O(n(s+1)/\varepsilon^2)$, contradicting the assumed circuit lower bound when $C_\varepsilon$ is large enough. Hence $v\ge1/2-\varepsilon$.

Take a maximizing input distribution $\mu$. Draw
$$
r=\left\lceil\frac{\ln|\mathcal C_s|+1}{2\varepsilon^2}\right\rceil
$$
independent samples from $\mu$. For each fixed $D$, its sampled disagreement fraction is below its expectation by more than $\varepsilon$ with probability at most $e^{-2\varepsilon^2r}$. A union bound over $\mathcal C_s$ is less than one. Therefore some multiset $Q_f$ has disagreement fraction at least $v-\varepsilon\ge1/2-2\varepsilon$ for every $D$. Circuit counting gives $\log|\mathcal C_s|=O(s\log(n+s))$.

**OPS parameter check.** For $s=s_1=s_2/(cn)$ and fixed small $\beta$, $\log|\mathcal C_s|=O(\beta s_2/c)$, so the support bound is $O(s_2)$ up to constants. The majority argument needs the published constant in the high/low threshold ratio to dominate $C_\varepsilon$; this entry does not assert a sharper constant than the source theorem.

**Scope.** The distribution $\mu$ and its sampled support depend on the full truth table $f$. The proof establishes existence separately for each hard $f$; it gives no small circuit that maps every $f$ to a suitable support. A fixed input sample still fails by C-15. The unsettled theorem is constructive synthesis, not existence of short anti-checkers.

**Sources.** Lipton and Young, [Simple Strategies for Large Zero-Sum Games with Applications to Complexity Theory](https://www.cs.ucr.edu/~neal/Lipton94Simple.pdf), Theorem 6; OPS, [Hardness Magnification Near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and Lemma 4.1.

## C-22 - Anti-checker generation is a second-level search relation

**Statement.** Fix an explicit truth table $f$ of length $N=2^n$, a sample length $r$, and a circuit cutoff $s\le\mathrm{poly}(N)$. The relation
$$
\operatorname{AC}(f,Q)\iff
\forall D\in\mathcal C_s\ \exists j\le r:\ D(q_j)\ne f(q_j)
$$
is in coNP: a violating circuit $D$ is a polynomial-length witness for its complement. The problem of extending a prescribed prefix of $Q$ to a full anti-checker is in $\Sigma_2^P$. If every high-complexity $f$ under consideration has some length-$r$ anti-checker, then under $P=NP$ a valid $Q$ can be found by polynomial-time self-reduction, since $P=NP$ collapses the polynomial hierarchy to $P$.

**Status.** PROVED QUANTIFIER CLASSIFICATION AND CONDITIONAL SEARCH CONSEQUENCE.

**Proof.** The complement of $\operatorname{AC}$ guesses a description of $D$ and checks all $r$ locations by evaluating $D$ and looking up the corresponding bits of the explicit table. For a prefix $p$, extension asks whether there exists a completion $Q$ such that $\operatorname{AC}(f,Q)$; this is an existential quantifier followed by the universal circuit quantifier, with the finite disjunction over sample locations inside the polynomial-time predicate. Thus it is a $\Sigma_2^P$ language. Under $P=NP$, $\mathrm{PH}=P$, so decide prefix extension one output bit at a time, preserving a yes answer at each step.

**Limit.** The resulting polynomial-time exponent can be arbitrarily large and depends on the fixed decision procedure. It yields only polynomial-size selectors, not the near-linear $N^{1+O(\beta)}$ selectors that OPS obtain under $NP\subseteq P/poly$. This explains why ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“P=NP makes the witness findableÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â does not itself contradict the magnification threshold.

## C-23 - Almost every sparse hard support has a near-linear anti-checker circuit

**Statement.** Put $N=2^n$, $s_2=2^{\beta n}$, and $s_1=s_2/(cn)$ for a fixed circuit-count constant $c$ and sufficiently small fixed $\beta>0$. For a uniformly random support $R\subseteq\{0,1\}^n$ of size $s_2$, with probability $1-o(1)$:

1. $f=1_R$ has $CC(f)>s_2$;
2. a fixed set $Q_0$ of $O(s_1\log(n+s_1))=O(s_2)$ points, chosen independently of $R$, is disjoint from $R$; and
3. $Q=R\cup Q_0$ is an anti-checker for $f$ against every size-$s_1$ circuit.

Consequently, a circuit of size $O(Nn^3)$ can output a valid anti-checker for a $1-o(1)$ fraction of weight-$s_2$ supports: sort the truth-table positions by their labels, output all $s_2$ positive coordinates, then append the hardwired $Q_0$. This is only a distributional/partial-domain selector, not a valid OPS selector on every high-complexity table.

**Status.** PROJECT-DERIVED PROBABILISTIC LEMMA; proof below. It narrows the sparse-support attack and demonstrates that C-18's range lower bound is not a selector-size lower bound.

**Proof.** Let $M_1=|\mathcal C_{s_1}|\le2^{C_0s_1\log_2(n+s_1)}$. First choose $Q_0$ by sampling $m=\lceil\log_2 M_1\rceil+2$ points independently and uniformly from the domain. For any fixed circuit whose 1-set has density greater than $1/2$, the chance that $Q_0$ misses its 1-set is at most $2^{-m}$. A union bound over $\mathcal C_{s_1}$ is less than one, so there exists a fixed $Q_0$ hitting the 1-set of every such circuit.

Now choose $R$ uniformly among the $s_2$-subsets. For a fixed circuit $D$ with 1-density at most $1/2$, the probability $R\subseteq D^{-1}(1)$ is at most $2^{-s_2}$. Therefore the chance that any such $D$ contains all of $R$ is at most $M_1\,2^{-s_2}=o(1)$ when $\beta$ is sufficiently small, because $\log_2M_1=O(\beta s_2/c)$. Also
$$
\Pr[R\cap Q_0\ne\varnothing]\le \frac{s_2|Q_0|}{N}
=O(s_2^2/N)=o(1)
$$
for $\beta<1/2$. Finally, circuit counting gives
$$
\log_2\binom{N}{s_2}=(1-\beta-o(1))ns_2
$$
while $\log_2|\mathcal C_{s_2}|=O(\beta ns_2)$; for sufficiently small $\beta$, the fraction of supports with $CC(1_R)\le s_2$ is $o(1)$. Thus all three properties hold simultaneously with probability $1-o(1)$.

For any such $R$, take a circuit $D$ of size at most $s_1$. If $D$ rejects some $x\in R$, it disagrees with $f$ at that positive sample point. Otherwise $R\subseteq D^{-1}(1)$. The second property above rules out density at most $1/2$, so $D$ has density greater than $1/2$ and $Q_0$ contains a point $y$ with $D(y)=1$. Since $Q_0\cap R=\varnothing$, $f(y)=0$, so $D$ disagrees at $y$. Hence $R\cup Q_0$ anti-checks all size-$s_1$ circuits.

The output circuit finds the $s_2$ positive positions using a sorting network on the $N$ truth-table bits and their $n$-bit labels. A fan-in-two sorting network costs $O(Nn^3)$ gates; the fixed $Q_0$ labels are hardwired. For $\beta<1/10$, the output list fits within the OPS length $t=s_2^{10}$.

**Learning / failure mode.** This does not handle exceptional supports contained in the 1-set of a sparse low circuit. For those, $Q_0$ need not hit the relevant low-density circuit error set $D^{-1}(1)\setminus R$. Thus any sparse-support lower-bound attempt must target these structured supports and show that locating their low-density containing circuits cannot be done cheaply. A lower bound based only on uniform random sparse supports is falsified by this selector.

## C-24 - Sparse supports inside sample-sized subcubes are also easy

**Statement.** Fix sufficiently small $\beta>0$, put $s_2=2^{\beta n}$, $s_1=s_2/(cn)$, and let $a=2^{\lfloor10\beta n\rfloor}$ be within the OPS sample budget $t=2^{10\beta n}$. Fix any axis-aligned subcube $A\subseteq\{0,1\}^n$ of size $a$. Choose $R$ uniformly among the $w=K s_2$-subsets of $A$, where $K$ is a sufficiently large constant depending on the circuit-counting constant. With probability $1-o(1)$:

1. $f=1_R$ has circuit complexity greater than $s_2$;
2. no size-$s_1$ circuit agrees with $f$ on every point of $A$; and
3. the smallest axis-aligned subcube containing $R$ is exactly $A$.

Therefore the sample $A$ itself anti-checks every size-$s_1$ circuit. A circuit of size $O(Nn^3)$ can recover the hull of the positives and output it, so this entire random subcube-supported family is another easy distributional subdomain.

**Status.** PROJECT-DERIVED COUNTING AND HULL-RECOVERY LEMMA; it narrows the structured sparse-support target but does not give a worst-case selector.

**Proof.** The number of possible supports inside $A$ satisfies
$$
\log_2\binom{a}{w}\ge w\log_2(a/w)
=(9K\beta-o(1))ns_2.
$$
The number of truth tables computable by size-$s_2$ circuits is at most $2^{(C_0\beta+o(1))ns_2}$. Choose $K>C_0/9$; then a uniformly random support is represented by no size-$s_2$ circuit with probability $1-o(1)$. The number of restrictions to $A$ induced by size-$s_1$ circuits is at most $2^{O(s_1\log(n+s_1))}=2^{O(\beta s_2/c)}$, negligible compared with $\binom{a}{w}$. Hence with probability $1-o(1)$ no such circuit agrees with $f$ on all of $A$.

For each free coordinate of $A$, the probability that all $w$ random points have the same bit in that coordinate is at most $2^{1-w}$. A union bound over at most $n$ free coordinates shows that every free coordinate takes both values on $R$ with probability $1-o(1)$. Fixed coordinates of $A$ are constant on $R$, so the coordinatewise hull of $R$ is exactly $A$.

Given the truth table, sort the indices carrying label $1$, compute for each coordinate whether all positive indices agree, and then enumerate the points matching exactly those fixed coordinates. Sorting/filtering the $N$ labeled indices with fan-in-two networks costs $O(Nn^3)$ gates. On the event above this outputs all of $A$. Since no size-$s_1$ circuit agrees with $f$ throughout $A$, every such circuit errs somewhere in the output sample.

**Learning / failure mode.** A simple low-density region is not enough to make a hard selector instance. The region must also be hard to recover from the positive support; axis-aligned subcubes are recovered by the coordinate hull. Any next sparse-support candidate should use a low-circuit region with no comparably cheap hull or canonical closure.

## C-25 - A known region admits a relative-density anti-checker

**Statement.** Let $X$ be a finite domain of size $N$, let $A\subseteq X$ have size $a$, and let $\mathcal C$ be a finite family of $M$ Boolean functions on $X$. Fix $0<\eta<1$. Choose $R$ uniformly from the $w$-subsets of $A$. Suppose parameters satisfy
$$
M\eta^m=o(1),\qquad M(1-\eta)^w=o(1),\qquad \frac{wm}{a}=o(1).
$$
Then there is a fixed multiset $Q_A$ of $m$ points in $A$, independent of $R$, such that with probability $1-o(1)$ over $R$:

1. no $D\in\mathcal C$ whose relative 1-density on $A$ is at most $1-\eta$ contains all of $R$ in its 1-set;
2. $Q_A\cap R=\varnothing$; and
3. $R\cup Q_A$ anti-checks every member of $\mathcal C$ against $1_R$.

Density is measured relative to $A$. This is an existence result for a known region; it gives no procedure for recovering an unknown $A$ from $R$.

**Proof.** Sample an ordered list $Q$ of $m$ points independently and uniformly from $A$, independently of $R$. A fixed $D$ with relative 1-density greater than $1-\eta$ is missed by $Q$ with probability at most $\eta^m$. A union bound makes the probability that some such circuit is missed at most $M\eta^m=o(1)$. For a fixed $D$ with relative density at most $1-\eta$, sampling $R$ without replacement gives $\Pr[R\subseteq D^{-1}(1)]\le(1-\eta)^w$: each successive conditional fraction of available points in its 1-set is at most its original density. Unioning over $\mathcal C$ gives at most $M(1-\eta)^w=o(1)$. Also $\Pr[Q\cap R\ne\varnothing]\le wm/a=o(1)$ by a union bound over pairs of sampled points. Thus the joint failure probability over $(Q,R)$ is $o(1)$; averaging over $Q$ fixes one list $Q_A$ whose failure probability over $R$ is $o(1)$. For a remaining $R$, any $D$ either rejects some point of $R$, or contains all of $R$. In the latter case it has relative density greater than $1-\eta$, so $Q_A$ contains a point $y$ with $D(y)=1$. Since $Q_A\cap R=\varnothing$, $1_R(y)=0$. Therefore $R\cup Q_A$ anti-checks every $D$.

**High-complexity addendum.** If $R$ is viewed as the full truth table $1_R$ on $X$, and $\binom{a}{w}$ divided by the number of size-at-most-$S$ circuit-computable truth tables tends to infinity, then a uniformly random $R$ has $CC(1_R)>S$ with probability $1-o(1)$. This separate counting condition can be combined with the anti-checker conclusion by a union bound.

**Status.** PROVED ELEMENTARY PROBABILISTIC LEMMA. The region-relative split generalizes C-23: once $A$ is known, random positives make low-density containing circuits unlikely, and a small fixed sample hits all nearly-full circuits. It does not solve the input-dependent synthesis problem of finding or exploiting an unknown $A$.

## C-26 - Random supports in affine subspaces reveal their region

**Statement.** Fix a sufficiently small constant $0<\beta<1/10$, let $N=2^n$, $s_2=2^{\beta n}$, $s_1=s_2/(cn)$, and $t=2^{10\beta n}$. Let $d=\lfloor10\beta n\rfloor$, $a=2^d$, and fix any affine subspace $A\subseteq\mathbb F_2^n$ of dimension $d$. Choose $w=K s_2$ points uniformly without replacement from $A$, where $K$ is a sufficiently large constant. With probability $1-o(1)$, $f=1_R$ has $CC(f)>s_2$, the affine hull of $R$ is $A$, and no size-$s_1$ circuit agrees with $f$ on all of $A$. Consequently, outputting all of $A$ gives a valid anti-checker of length $a\le t$. On this promised support family, the map $f\mapsto A$ and its output are computable by circuits of size $O(Nn^3)$.

**Proof.** Standard circuit counting gives at most $2^{C s\log_2(n+s)}$ functions of circuit size at most $s$, for a basis-dependent constant $C$. Since
$$
\log_2\binom{a}{w}\ge w\log_2(a/w)=(9K\beta-o(1))ns_2,
$$
choosing $9K>C$ makes the number of supports dominate the number of size-$s_2$ circuits by an exponential factor. Thus $CC(1_R)>s_2$ with probability $1-o(1)$. Likewise, the number of size-$s_1$ circuit restrictions to $A$ is at most $2^{O(s_1\log(n+s_1))}=2^{O(s_2)}$, negligible compared with $\binom{a}{w}$; hence no such circuit has restriction exactly $1_R|_A$ with probability $1-o(1)$.

If the affine hull of $R$ is a proper subset of $A$, then $R$ is contained in some affine hyperplane of $A$. There are fewer than $2^{d+1}$ such hyperplanes, each containing half of $A$, and the probability all $w$ sampled points lie in any fixed one is at most $2^{-w}$. The union bound $2^{d+1-w}=o(1)$ proves $\operatorname{aff}(R)=A$. By the preceding restriction-counting event, every size-$s_1$ circuit disagrees with $f$ somewhere on $A$, so the full region is an anti-checker. A circuit can compact the positive indices, perform Gaussian elimination on their $n$-bit labels, and enumerate the $2^d$ affine combinations; these operations fit in $O(Nn^3+an^2)=O(Nn^3)$ gates. The output list has $a\le t$ entries.

**Learning / failure mode.** The affine equations may be hidden initially, but many random positives recover them by linear algebra. This expands C-24 beyond coordinate subcubes and rules out affine subspaces/cosets as hidden-region hard instances of this form. It is still only a distributional subcase: no theorem says every worst-case selector must identify a region, and this result gives no selector lower bound.

## C-27 - Sparse-support anti-checking is exactly a transversal problem

**Statement.** Let $f=1_R$ for $R\subseteq X$, and let $\mathcal C_s$ be a family of Boolean functions. For every $D\in\mathcal C_s$ that accepts all positives, define its residual error set
$$
E_D=D^{-1}(1)\setminus R.
$$
A set $Q$ is an anti-checker for $f$ against $\mathcal C_s$ if and only if $Q\cup R$ is a transversal of the family $\{E_D:R\subseteq D^{-1}(1),\ D\in\mathcal C_s\}$, where ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“transversalÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â means intersecting every member. More precisely, a list $Q$ anti-checks iff $Q\setminus R$ intersects each such $E_D$; circuits rejecting some point of $R$ are already caught by $R$.

**Proof.** If $D$ rejects some $r\in R$, then $D(r)=0\ne f(r)=1$. Otherwise $R\subseteq D^{-1}(1)$, so every point of $R$ is accepted by $D$ and cannot witness disagreement. A listed point $x\notin R$ witnesses disagreement exactly when $D(x)=1$, which is exactly $x\in E_D$. Thus every remaining circuit is caught precisely when the output's zero-labeled points hit every residual extension set. The two conditions are equivalent.

If $CC(f)>s$, none of the residual sets is empty, since $E_D=\varnothing$ would mean $D^{-1}(1)=R$ and hence $D=f$. The minimax proof of C-21 can be read as a fractional-transversal argument: there is a distribution on $X$ assigning constant mass to every residual error set; sampling $O(\log|\mathcal C_s|)$ points converts it into a small integral transversal.

**Status / limit.** PROVED EXACT REFORMULATION. This identifies the synthesis bottleneck as finding a small transversal in a version space of circuit extensions. It is not a lower bound: an arbitrary selector need not explicitly recover a region, and the equivalence alone does not show that transversal synthesis is hard. OPS's conditional construction remains the strongest relevant upper bound; no unconditional matching lower bound is known here.

## C-28 - Majority circuits impose a local overlap condition

**Statement.** Let $f=1_R$, and let $D_1,\ldots,D_q$ be size-at-most-$s$ circuits all accepting every point of $R$, where $q$ is odd. If every point $x\notin R$ is accepted by at most $(q-1)/2$ of these circuits, then their majority computes $f$. Therefore, whenever $CC(f)$ exceeds the size of a majority circuit on $q$ size-$s$ circuits, every such $q$-tuple has some $x\notin R$ accepted by at least $(q+1)/2$ members. Equivalently, every such subfamily of residual extension sets has a point of majority overlap.

**Proof.** On $R$, all $D_i$ output $1$, so their majority outputs $1=f$. Outside $R$, at most $(q-1)/2$ output $1$, so the majority outputs $0=f$. A fan-in-two circuit can compute the majority of $q$ bits with $O(q^2)$ additional gates, giving total size $O(qs+q^2)$. The contrapositive gives the overlap claim.

For $q=3$, high enough circuit complexity rules out three pairwise-disjoint residual extension sets. This is only a local packing constraint: bounded matching number alone does not give a small transversal for arbitrary set systems, and the stronger majority-overlap condition has not been converted into a selector lower bound or a near-linear synthesis algorithm.

**Stress test of the implication.** Even the majority-overlap property for every subfamily does not force a small transversal in general. On a universe of size $m$, take all subsets $E$ with $|E|>m/2$. Any $q$ selected sets have more than $qm/2$ incidences, so some point belongs to more than half of them. Yet a transversal must have at least $\lceil m/2\rceil$ points: any smaller set has a complement containing one of these strict-majority subsets. Thus the overlap lemma alone cannot be upgraded to a short selector by a generic hypergraph argument. The circuit-derived family may have additional structure, but that structure must be used explicitly.

## C-29 - Known-region sparse supports are easy across the sample-size split

**Statement.** Let $s_2=2^{\beta n}$, $s_1=s_2/(cn)$, and $t=s_2^{10}$ for a sufficiently small fixed $\beta<1/10$. Let $A\subseteq\{0,1\}^n$ be fixed and known to the selector circuit, and choose $R$ uniformly among the $w=K s_2$-subsets of $A$, with $K$ a sufficiently large constant. Consider supports with $\binom{|A|}{w}/|\mathcal C_{s_2}|\to\infty$.

If $|A|\le t$, output all of $A$. With probability $1-o(1)$ this anti-checks every size-$s_1$ circuit, since circuit counting makes it unlikely that any such circuit agrees with $1_R$ throughout $A$. If $|A|>t$, there is a fixed list $Q_A$ of $m=O(s_2)$ points, independent of $R$, such that with probability $1-o(1)$, $R\cup Q_A$ is an anti-checker. Here one may take $m=\log_2|\mathcal C_{s_1}|+\omega(1)$ and choose $K$ so $|\mathcal C_{s_1}|2^{-w}=o(1)$; then $wm/|A|=o(1)$ because $|A|>s_2^{10}$. Both outputs have length at most $t$ and are computed by a circuit of size $O(Nn^3)$ (the small-region output is hardwired; the large-region circuit sorts the positives and appends the hardwired $Q_A$).

**Proof.** For $|A|\le t$, every low circuit agreeing with $1_R$ on all of $A$ determines one of at most $|\mathcal C_{s_1}|$ restrictions. The probability a uniform support equals one of them is at most $|\mathcal C_{s_1}|/\binom{|A|}{w}=o(1)$, since $|\mathcal C_{s_1}|\le|\mathcal C_{s_2}|$. Thus querying all of $A$ catches every low circuit. For $|A|>t$, apply C-25 with $\eta=1/2$: a fixed $Q_A$ hits every circuit with relative 1-density above $1/2$, while a low-density circuit contains all of $R$ with probability at most $2^{-w}$. The union bound and negligible overlap give the anti-checker. Since $|A|>s_2^{10}$ and $m,w=O(s_2)$, the overlap probability is $O(s_2^2/s_2^{10})=o(1)$. Circuit counting on $|A|>s_2^{10}$ also gives $\binom{|A|}{w}\gg|\mathcal C_{s_2}|$ when $K$ is sufficiently large, consistent with the stated high-complexity support promise.

**Limit / lesson.** The circuit is allowed to depend on the fixed region $A$; this is not one selector uniform over unknown regions. The dichotomy shows that region size itself is not the obstacle: small regions can be output whole, while large regions leave room for a fixed relative-density hitting set. The unresolved issue is input-dependent recovery or replacement of an unknown useful region, and no argument shows every selector must do that.

## C-30 - Bounded-degree algebraic closure recovers hidden support regions

**Statement.** Fix a constant degree $d$, put $N=2^n$, $s_2=2^{\beta n}$, $s_1=s_2/(cn)$, $a=2^{\lfloor10\beta n\rfloor}$, and $w=K s_2\le a$, where $K$ is a sufficiently large constant. Let $\phi_d(x)\in\mathbb F_2^L$, $L=\sum_{i=0}^d\binom ni$, be the vector of all squarefree monomials of degree at most $d$. Suppose a fixed region $A\subseteq\mathbb F_2^n$ has size $a$ and:

1. **degree-$d$ closure:** $A=\{x:\phi_d(x)\in\operatorname{span}(\phi_d(A))\}$;
2. **evaluation distance:** every nonzero degree-at-most-$d$ polynomial restricted to $A$ is nonzero on at least a $\delta$ fraction of $A$; and
3. $2^L(1-\delta)^w=o(1)$.

If also $\binom{a}{w}/|\mathcal C_{s_2}|\to\infty$, then for uniformly random $R\in\binom Aw$, with probability $1-o(1)$:

* $CC(1_R)>s_2$;
* the degree-$d$ closure of $R$ equals $A$;
* no size-$s_1$ circuit agrees with $1_R$ throughout $A$.

Therefore one circuit, uniform over all such $A$, can recover the closure from the truth table and output all of $A$ as an anti-checker. It has size $O(Nn^{O(d)})$ and output length $a\le t=s_2^{10}$.

**Proof.** The number of supports is larger than the number of size-$s_2$ circuit tables by the stated ratio, so circuit counting gives $CC(1_R)>s_2$ with probability $1-o(1)$. Since $|\mathcal C_{s_1}|\le|\mathcal C_{s_2}|$, the probability any low circuit restriction to $A$ equals the random support indicator is at most $|\mathcal C_{s_1}|/\binom aw=o(1)$.

For closure recovery, write $W_A=\operatorname{span}\{\phi_d(x):x\in A\}$. If the sampled feature vectors fail to span $W_A$, some nonzero linear functional on $W_A$ vanishes on all of them. It corresponds to a degree-at-most-$d$ polynomial whose restriction to $A$ is nonzero. There are at most $2^L$ such functionals, and each vanishes on at most a $(1-\delta)$ fraction of $A$. Sampling without replacement, the failure probability is at most $2^L(1-\delta)^w=o(1)$. The common zero set of all degree-at-most-$d$ polynomials vanishing on $R$ is exactly $\{x:\phi_d(x)\in\operatorname{span}(\phi_d(R))\}$, by orthogonal-complement duality. Once the sample spans $W_A$, degree-$d$ closure recovers $A$. By the degree-$d$ closure assumption, querying every point of $A$ catches every low circuit because none agrees with $1_R$ on all of $A$.

The circuit forms the $N\times L$ matrix whose row for $x$ is $1_R(x)\phi_d(x)$, row-reduces it over $\mathbb F_2$, tests each of the $N$ domain points for feature-span membership, and compacts the resulting labels (truncating/padding outside the promise). For fixed $d$, Gaussian elimination and all membership tests cost $O(NL^2)$ gates, and label compaction costs $O(N\operatorname{poly}(n))$. Since $L=O(n^d)$, the total is $O(Nn^{O(d)})$. On the promised inputs the output is exactly $A$ and has length $a\le t$.

**Example class.** A graph $A=\{(u,g(u)):u\in\mathbb F_2^k\}$ of a fixed-degree-$r$ polynomial map is degree-$r$ closed, since its defining equations $y_j+g_j(u)=0$ have degree at most $r$. Substituting $g$ into any degree-$r$ polynomial gives degree at most $r^2$ in $u$. A nonzero Boolean polynomial of degree at most $D$ on $k$ bits has weight at least $2^{k-D}$: induct on $k$, splitting on the last variable; if it occurs, the difference of the two restrictions is a nonzero polynomial of degree at most $D-1$, and if it does not occur, the support doubles. Hence every nonzero restriction has relative weight at least $2^{-r^2}$, so $\delta\ge2^{-r^2}$. With $L=O(n^r)$ and $w=K2^{\beta n}$ the spanning failure probability vanishes. Taking $k=\lfloor10\beta n\rfloor$ and $K$ sufficiently large also gives the support-count condition.

**Limit / lesson.** This is a constructive, uniform selector for a broad but structured promise family, not a selector for all high-complexity tables and not a P-vs-NP proof. It identifies a useful new filter: candidate hidden regions must resist not only coordinate and affine hulls but also bounded-degree algebraic closure learned from the positive support.

## C-31 - Hamming balls defeat fixed-degree closure but remain easy to recover

**Setup.** Fix constants $0<\beta<1/10$ and $\gamma$ with $\beta<\gamma<10\beta$. Choose $0<\rho<1/2$ with binary entropy $H_2(\rho)=\gamma$, let $k=\lfloor\rho n\rfloor$, and set $A=B_k=\{x:|x|\le k\}$. Then $|A|=2^{\gamma n+o(n)}<t=s_2^{10}$, where $s_2=2^{\beta n}$. Let $w=K s_2$, with $K$ sufficiently large, and sample $R$ uniformly from $\binom Aw$.

**Statement.** With probability $1-o(1)$, $1_R$ has circuit complexity above $s_2$, no size-$s_1$ circuit agrees with it throughout $A$, and the maximum Hamming weight among points of $R$ is exactly $k$. Thus the selector ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“compute $k_R=\max_{x\in R}|x|$ and output $B_{k_R}$ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â is valid on this distributional family, has output length at most $t$, and has circuit size $O(N\operatorname{poly}(n))$.

At the same time, for every fixed degree $d$, the degree-$d$ feature vectors of points in $A$ span all of $\mathbb F_2^L$ once $k\ge d$, so $\operatorname{cl}_d(A)=\mathbb F_2^n$. Moreover, every nonzero degree-at-most-$d$ polynomial has constant relative weight on $A$ (depending on $\rho,d$), so $w\gg L$ random positives span the full feature space with probability $1-o(1)$. The bounded-degree closure selector therefore outputs the whole domain on these inputs and misses the list budget. This is a concrete failure of that closure method, not a hard selector instance.

**Proof.** Circuit counting gives $\log_2|\mathcal C_{s_2}|=O(\beta n s_2)$. Since
$$
\log_2\binom{|A|}{w}\ge w\log_2(|A|/w)=K(\gamma-\beta+o(1))n s_2,
$$
choosing $K$ large makes the support count dominate $|\mathcal C_{s_2}|$; it also dominates $|\mathcal C_{s_1}|$. This proves high complexity and the no-agreement property with probability $1-o(1)$. The boundary layer $|x|=k$ is a constant fraction $(1-2\rho)/(1-\rho)+o(1)$ of the Hamming ball, so a sample of $w\to\infty$ points contains a boundary point with probability $1-o(1)$.

For the feature-span claim, $A$ contains every indicator vector $1_S$ for $|S|\le d$. Their feature-vector matrix has entries $1[T\subseteq S]$ for $|T|,|S|\le d$; ordered by cardinality, it is triangular with diagonal one, hence has rank $L$. For the distance claim, take a nonzero polynomial of maximal degree $r\le d$ and a degree-$r$ monomial with nonzero coefficient. Summing its values over all assignments to those $r$ variables gives one for every assignment to the other variables. In particular, for each assignment of weight at most $k-r$ to the other variables, at least one completion lies in $A$ and has polynomial value one. Thus the support on $A$ has size at least $\binom{n-r}{k-r}$, whose ratio to $|A|$ is bounded below by a positive constant depending only on $\rho,d$. The C-30 union bound then shows random positives span the full feature space.

Finally, the fraction of $A$ on its boundary tends to a positive constant, so the maximum sampled weight equals $k$ with high probability. A circuit can compute the maximum by parallel comparisons over the table, then enumerate/filter all inputs of weight at most that maximum. This costs $O(N\operatorname{poly}(n))$ gates.

**Learning / failure mode.** A region can defeat every fixed-degree algebraic closure yet be recovered by a simple statistic such as maximum weight. A useful adversarial region must evade several independent closure mechanisms; even that would not prove that every anti-checker selector must recover it.

## C-32 - Fourier spectrum recovers a hidden linear product region

**Setup.** Fix a block size $r\ge3$, let $r\mid n$, and put $m=n/r$. Let $B=\{0,e_1,\ldots,e_r\}\subseteq\mathbb F_2^r$. Choose $\beta<\gamma<10\beta$, where $\gamma=\log_2(r+1)/r$, and let $s_2=2^{\beta n}$, $s_1=s_2/(cn)$, $t=s_2^{10}$. For every sufficiently small fixed $\beta$, a fixed $r$ with this entropy condition exists: $g(r)=\log_2(r+1)/r$ decreases to zero with adjacent ratios below $2$, so its values cross the interval $(\beta,10\beta)$. For an arbitrary invertible linear map $T:\mathbb F_2^n\to\mathbb F_2^n$, define $A=T^{-1}(B^m)$, of size $(r+1)^m=2^{\gamma n}<t$. The set $A$ has a membership circuit of size $O(n^2)$ and is therefore a low-circuit region. Choose $w=K s_2$ points uniformly without replacement from $A$, with $K$ sufficiently large.

**Statement.** With probability $1-o(1)$, $1_R$ has circuit complexity above $s_2$, no size-$s_1$ circuit agrees with it throughout $A$, and one selector circuit independent of $T$ recovers and outputs all of $A$. Its sample length is $|A|<t$ and its circuit size is $O(N\operatorname{poly}(n))$ (with the polynomial depending on fixed $r$).

**Fourier fingerprint.** For uniform $z$ on $B$, the parity bias at $u\in\mathbb F_2^r$ is
$$
\widehat\nu(u)=\frac{r+1-2|u|}{r+1}.
$$
Let $\alpha=(r-1)/(r+1)$ and $\lambda=\max((r-3)/(r+1),\alpha^2)<\alpha$. For the product distribution on $B^m$, among nonzero frequency vectors the coefficients of magnitude $\alpha$ are exactly the vectors having, in one block, either a weight-one vector or the all-ones vector, and zero in every other block. All other nonzero-frequency coefficients have magnitude at most $\lambda$. The zero frequency has coefficient $1$ and is discarded. Under $T$, this high-frequency set is mapped by $T^T$.

**Selector construction.** Apply a fast Walsh-Hadamard transform to the truth-table indicator of $R$ to compute all $N$ empirical Fourier coefficients. The sample without replacement is uniform on $A$; Hoeffding's inequality and a union bound over $N$ frequencies show that, with probability $1-o(1)$, all coefficients are within a fixed fraction of the spectral gap $\alpha-\lambda$. Thresholding therefore recovers the exact high-frequency set.

In standard block coordinates, each block contributes $r+1$ high-frequency vectors $e_1,\ldots,e_r,h=e_1+\cdots+e_r$. Every $r$ of them are independent and their full set is a minimal linear dependence. Since the block spaces form a direct sum, the minimal dependencies of size $r+1$ in the entire high-frequency set are exactly the blocks. Enumerating subsets of this size (polynomially many because $r$ is fixed) recovers the blocks after the unknown invertible transform.

Choose any $r$ vectors from each recovered block dependence as a basis of parity forms. Project the positive examples onto these $r$ forms. Each of the $r+1$ allowed local patterns occurs with probability $1/(r+1)$ under uniform $A$, so all patterns are observed with probability $1-o(1)$ after $w$ samples. The selector now knows the exact allowed pattern set in every transformed block and outputs all $x$ satisfying those block constraints, which is precisely $A$.

The Walsh transform costs $O(Nn^2)$ Boolean gates using $O(n)$-bit additions. Frequency extraction, fixed-size dependence enumeration, pattern recovery, point membership, and output compaction add $O(N\operatorname{poly}(n))$ gates.

**Counting and anti-checking.** Since $|A|=2^{\gamma n}$,
$$
\log_2\binom{|A|}{w}\ge K(\gamma-\beta+o(1))n s_2.
$$
For sufficiently large $K$, this dominates $\log_2|\mathcal C_{s_2}|=O(\beta n s_2)$ and also $\log_2|\mathcal C_{s_1}|$. Thus the random table is high-complexity and no low circuit agrees throughout $A$, both with probability $1-o(1)$. The recovered full region is therefore an anti-checker.

**Learning / failure mode.** Even a region that defeats fixed-degree algebraic closure (C-31) may expose a Fourier fingerprint and a matroid of minimal dependencies. Secret linear transformations and product constraints are still too structured. This rules out a larger explicit family of hidden-region examples; it does not lower-bound arbitrary selectors.

## C-33 - A Fourier-matroid criterion for learning hidden product regions

**Statement.** Fix a block dimension $r$ and a proper set $B\subsetneq\mathbb F_2^r$ with full affine span. Let $\nu$ be uniform on $B$, and define
$$
\alpha=\max_{u\ne0}|\widehat\nu(u)|,\qquad
S=\{u\ne0:|\widehat\nu(u)|=\alpha\}.
$$
Assume $S$ spans $\mathbb F_2^r$ and its binary linear matroid is connected. Since $B$ is proper, $\alpha>0$; since it has full affine span, $\alpha<1$. Let $\lambda$ be the maximum of $\alpha^2$ and the magnitudes of all nonzero local Fourier coefficients below $\alpha$, so $\lambda<\alpha$.

For $m=n/r$ and any unknown invertible linear map $T$, put $A=T^{-1}(B^m)$. If $\beta<\gamma=\log_2|B|/r<10\beta$, choose $w=K2^{\beta n}$ random distinct points in $A$, with K sufficiently large for the circuit-counting entropy. Then with probability $1-o(1)$, $1_R$ has complexity above $s_2$, no size-$s_1$ circuit agrees on all of A, and a single near-linear selector (depending on fixed B,r but not T) recovers and outputs A.

**Proof.** The Fourier coefficient of a product distribution factors across blocks. A nonzero global frequency supported in one block at a local frequency in S has magnitude $\alpha$. Any other nonzero global frequency either has a local factor below $\alpha$, or uses at least two nonzero blocks and has magnitude at most $\alpha^2$. Thus the set of largest nonzero Fourier coefficients is exactly the union of the transformed copies of S, with constant gap $\alpha-\lambda$. Hoeffding's inequality for sampling without replacement and a union bound over $N$ frequencies show that the empirical Walsh spectrum of $1_R/w$ identifies this set with probability $1-o(1)$.

In the original coordinates, that high-frequency set is a direct union of m copies of S in independent r-dimensional subspaces. Its binary matroid is the direct sum of m connected matroids, so its connected components are exactly the hidden blocks. Enumerating circuits of size at most $r+1$ recovers these components in polynomial time for fixed r. Choose a basis in each component. Projecting the positive samples onto each basis reveals the transformed image of B in that block: every one of its |B| patterns has probability $1/|B|$, and all are observed with probability $1-o(1)$ after w samples. Membership in the product of these learned pattern sets recovers A.

The Walsh transform, frequency compaction, fixed-r matroid-component computation, pattern recovery, and output compaction use $O(N\operatorname{poly}(n))$ gates. Since $|A|=2^{\gamma n}<t$, the full region fits in the output list. Finally,
$$
\log_2\binom{|A|}{w}\ge K(\gamma-\beta+o(1))n2^{\beta n}.
$$
For K large this dominates both circuit counts $|\mathcal C_{s_2}|$ and $|\mathcal C_{s_1}|$, proving high complexity and that no low circuit agrees throughout A.

**Limit / use.** C-32 is the explicit case $B=\{0,e_1,\ldots,e_r\}$, whose maximizer set is the circuit $\{e_1,\ldots,e_r,\sum_i e_i\}$. C-33 shows the mechanism applies to any fixed block alphabet with a connected, spanning Fourier-maximizer matroid. To resist this attack, a product-region candidate must break that condition or its spectral gap. This remains a distributional selector construction, not a lower bound for arbitrary selectors.

## C-34 - Every valid anti-checker selector depends on almost all truth-table bits

**Statement.** Let $N=2^n$, $s_2=2^{\beta n}$, and $t=2^{10\beta n}$ for fixed $0<\beta<1/10$. Suppose a deterministic multi-output circuit $A$ maps every $N$-bit truth table to a list of at most $t$ points in $\{0,1\}^n$, and for every $f$ with $CC(f)>s_2$ its output is an anti-checker against all circuits of size at most $s_1=s_2/(10n)$. Then the set $S$ of input coordinates on which any output bit of $A$ depends satisfies
\[
|S|\ge N-t-\log_2 M_2-O(1)=N-o(N),
\]
where $M_2$ is the number of $n$-input Boolean functions of circuit size at most $s_2$. If $A$ has fan-in-two gates and $L=tn$ output bits, its gate count is at least $(|S|-L)/2=\tfrac12N-o(N)$.

**Status.** PROJECT-PROVED elementary selector lower bound. It is universal over valid selectors, but only linear and does not improve the Gap-MCSP magnification threshold.

**Proof.** Assume $|S|<N-t-\log_2M_2-O(1)$. Consider the output list $Q$ of $A$ when every input coordinate in $S$ is zero. Construct an $N$-bit truth table $f$ that is zero on $S\cup Q$ and arbitrary elsewhere. There are at least $2^{N-|S|-t}>M_2$ such completions, so at least one has circuit complexity greater than $s_2$. Because $f$ is zero on $S$, $A(f)=Q$. The constant-zero circuit agrees with $f$ on every point of $Q$, contradicting the anti-checker property. Hence $|S|\ge N-t-\log_2M_2-O(1)$. Standard circuit counting gives $\log_2M_2=O(s_2\log(s_2+n))=o(N)$, and $t=o(N)$ for $\beta<1/10$. In a fan-in-two multi-output circuit, every essential input either connects directly to one of the $L$ output wires or enters a gate; the latter accounts for at most $2\,\operatorname{size}(A)$ distinct inputs. Thus $|S|\le 2\,\operatorname{size}(A)+L$ and the gate lower bound follows.

**Generality audit / limit.** This argument quantifies over the entire valid selector and uses no region or implementation assumption. It only counts essential input variables; an $O(N)$-gate circuit can depend on all $N$ inputs. Extracting a superlinear lower bound requires a property of the *routing function* $f\mapsto Q_f$, beyond near-total dependence. The result is consistent with OPS's conditional $N^{1+O(\beta)}$ selector and yields no separation by itself.

## C-35 - A fixed sample anti-checks almost every random truth table

**Statement.** Let $N=2^n$, fix a set $Q\subseteq\{0,1\}^n$ of $t$ distinct query points, and let $M_1$ be the number of $n$-input Boolean functions of circuit size at most $s_1$. For uniformly random $f:\{0,1\}^n\to\{0,1\}$,
\[
\Pr[\exists D\ (CC(D)\le s_1\ \wedge\ D|_Q=f|_Q)]\le M_1 2^{-t}.
\]
Consequently, for the OPS parameters $s_1=2^{\beta n}/(10n)$, $s_2=2^{\beta n}$, and $t=2^{10\beta n}$, a fixed $Q$ is an anti-checker against all size-$s_1$ circuits for a random high-complexity table with probability at least
\[
1-2^{-t+O(2^{\beta n})}-2^{-N+O(2^{\beta n}n)}=1-o(1).
\]

**Status.** PROJECT-PROVED by direct counting. Distributional fact only; it gives no selector for the exceptional tables and no lower bound on an adaptive selector.

**Proof.** For each fixed low circuit $D$, exactly $2^{N-t}$ truth tables agree with $D$ on $Q$. A union bound over the $M_1$ low-circuit functions gives at most $M_1 2^{N-t}$ bad tables, proving the first inequality. Circuit counting gives $\log_2 M_1=O(s_1\log(s_1+n))=O(2^{\beta n})$. Separately, at most $M_2=2^{O(s_2\log(s_2+n))}$ tables have circuit size at most $s_2$, so a uniformly random table is high with probability $1-M_2/2^N=1-2^{-N+O(2^{\beta n}n)}$. For fixed $0<\beta<1/10$, $t=2^{10\beta n}$ dominates $2^{\beta n}$, establishing the displayed bound.

**Learning.** Any universal lower bound must be driven by atypical tables for which a candidate fixed sample agrees with some low circuit. An average-case lower bound for the selector under the uniform truth-table distribution cannot by itself reach the OPS target: a set-theoretic valid selector can use one fixed sample on the $1-o(1)$ easy portion and reserve its adaptive behavior for the exceptional portion. Complexity of recognizing and routing those exceptions is the open issue.

## C-36 - Robust linear sketches cannot choose a valid anti-checker

**Statement.** Let $N=2^n$, let $A:\mathbb F_2^N\to\mathbb F_2^k$ be a full-rank linear map, and suppose its row space has minimum Hamming distance greater than $t$. Let $H$ be any decoder that maps each sketch value $h$ to an ordered list $Q_h$ of at most $t$ points of $\{0,1\}^n$. If
\[
N-t-k>\log_2 M_2,
\]
where $M_2$ is the number of truth tables of circuit complexity at most $s_2$, then the address selector $f\mapsto Q_{Af}$ is not a valid anti-checker for all $f$ with $CC(f)>s_2$, regardless of the computational complexity of $H$.

More generally, for any address sketch $g(f)=h$ and decoder $Q_h$, validity requires every fiber
\[
\{f:g(f)=h,\ f|_{Q_h}=y\}
\]
to contain at most $M_2$ tables whenever $y$ is the restriction of some circuit of size at most $s_1$. This is an exact necessary condition, independent of circuit architecture.

**Status.** PROJECT-PROVED. The first statement rules out a robust affine-sketch architecture, not arbitrary selectors.

**Proof.** Fix any sketch value $h$ and let $Q=Q_h$, with $r\le t$ distinct coordinates. The restriction of $A$ to columns outside $Q$ has rank $k$. Otherwise some nonzero row-space vector would be supported inside $Q$, contradicting minimum distance greater than $t$. Therefore the system $Af=h$ with $f|_Q=0$ has exactly $2^{N-r-k}$ solutions. Since $N-r-k\ge N-t-k>\log_2M_2$, there are more such solutions than low-complexity tables. Choose one with $CC(f)>s_2$. Its sketch is $h$, so the selector outputs $Q_h$, and the constant-zero circuit agrees with $f$ on every queried point. This contradicts validity. For the general condition, if a fiber slice for a low-circuit trace contained more than $M_2$ tables, at least one would have complexity greater than $s_2$ and would fail against the circuit realizing that trace.

For OPS parameters $s_2=2^{\beta n}$ and $t=2^{10\beta n}$ with fixed $\beta<1/10$, standard circuit counting gives $\log_2M_2=O(n2^{\beta n})=o(N)$ and $t=o(N)$. Thus the obstruction applies whenever the sketch dimension is $k=o(N)$, including $k\le tn$ address bits, provided the row-space distance exceeds $t$. Robust sketches of this kind exist: for a uniformly random full-rank $k\times N$ binary matrix with $k=o(N)$ and $t=o(N)$, a union bound gives probability at most $2^{k-N+H_2(t/N)N+o(N)}=o(1)$ of a nonzero row-space word of weight at most $t$.

**Generality audit / limit.** This attacks address maps that factor through a robust linear sketch, even with an unrestricted decoder. It does not cover nonlinear summaries or selectors whose addresses use feedback from the queried truth-table labels in a way that destroys the large completion fibers. The exact fiber-capacity condition identifies that feedback as a concrete target, but proving it forces superlinear size for arbitrary circuits would still imply the unresolved routing lower bound; no such bridge is proved here.

## C-37 - The 2026 pedigree-polytope Lean artifact does not verify its P-vs-NP claim

**Claim audited.** Arthanari's June 2026 preprint claims a strongly polynomial membership algorithm for the pedigree polytope and a Lean-verified consequence $P=NP$.

**Status.** PROOF-ARTIFACT AUDIT: the linked repository does not provide an axiom-free formal proof of this consequence. This is a statement about the current Lean artifact, not a proof that every mathematical argument in the preprint is false.

**Evidence and exact gap.** In the repository's `N_PEqualsNP.lean`, `tardos_strongly_polynomial` is declared as an axiom whose conclusion is `QuickProtocol (LayeredPoint n)`. The comments define `QuickProtocol` as a polynomial-time membership algorithm for the pedigree polytope. It is not a theorem deriving that protocol from the MCF optimization problem. The same file makes `An n` a placeholder `Unit`, and declares the transfer `membership_An_of_Pn` and the optimization-to-STSP implication `mi_objective_solves_stsp_ax` as axioms. Separately, `N_MembershipCharacterisation.lean` states the necessity direction of the membership/MCF equivalence as `axiom necessity_of_mcf`; its comments point to a backup proof containing 16 sorries. The repository README independently labels this direction an axiom. Thus the critical algorithmic bridge is assumed in the formal artifact rather than obtained from the verified sufficiency result plus Tardos's theorem.

**Proof-chain diagnosis.** A sufficient certificate test (MCF optimum at its maximum implies polytope membership) is not by itself a membership decider: a decider also needs the converse to know that no valid member is rejected when the test fails. The main Lean theorem consumes a pre-supplied `QuickProtocol` axiom, so it bypasses this missing direction. The machine checker verifies derivations from these axioms, not their mathematical validity.

**Sources.** Preprint: [arXiv:2606.03194](https://arxiv.org/abs/2606.03194). Primary code: [`N_PEqualsNP.lean`](https://github.com/TiruArt/Pedigree-Polytopes-Lean4/blob/main/MembershipProject/Core/N_PEqualsNP.lean), [`N_MembershipCharacterisation.lean`](https://github.com/TiruArt/Pedigree-Polytopes-Lean4/blob/main/MembershipProject/Core/N_MembershipCharacterisation.lean), and [repository README](https://github.com/TiruArt/Pedigree-Polytopes-Lean4). The Clay Mathematics Institute still lists P vs NP as unsolved: [official problem page](https://www.claymath.org/millennium/p-vs-np/).

**Use for this project.** The route is not a counterexample to the open status and supplies no breakthrough. It is a useful methodological example: inspect the types of formal axioms, not only `sorry` counts or successful builds; distinguish a one-sided certificate theorem from a decision procedure; and ensure representation-to-oracle reductions are actually implemented with polynomial bit complexity.

## C-38 - Essential-input connectivity gives a near-N gate lower bound

**Statement.** Any fan-in-at-most-two Boolean circuit with $L$ output wires and $E$ essential input variables has at least $E-L$ gates. Consequently, for an OPS anti-checker selector with $L=tn$ address-output bits, C-34 implies
\[
\operatorname{size}(A)\ge N-t-\log_2 M_2-tn-O(1)=N-o(N)
\]
for each fixed $0<\beta<1/10$.

**Status.** PROJECT-PROVED graph-counting lemma; it sharpens C-34's earlier, weaker $(1/2-o(1))N$ conversion. It remains a linear lower bound and does not establish O-1.

**Proof.** Delete gates that are not on any path from an essential input to an output depending on an essential input. Let $E'$ be the number of retained gates and $L'\le L$ the number of retained output ports. In the underlying undirected graph, all $E$ essential input vertices and the retained gates lie in components containing at least one retained output; hence the number $c$ of components is at most $L'$. The graph has $E+E'+L'$ vertices, so it has at least $E+E'+L'-c\ge E+E'$ edges. On the other hand, each retained gate contributes at most two incoming edges and each output port at most one, so the graph has at most $2E'+L'$ edges. Therefore $E+E'\le2E'+L'$, or $E'\ge E-L'\ge E-L$. Since the original circuit has at least $E'$ gates, its size is at least $E-L$.

For an anti-checker selector, C-34 gives $E\ge N-t-\log_2 M_2-O(1)$. Its address list uses at most $L=tn$ bits. For fixed $\beta<1/10$, both $t$ and $tn$ are $o(N)$, and circuit counting gives $\log_2M_2=O(n2^{\beta n})=o(N)$. Substitution yields $N-o(N)$ gates.

**Generality audit / limit.** The graph argument allows unrestricted fan-out, sharing, and negation; it only uses the fan-in bound. It shows a selector cannot compress its dependence on nearly all table bits to substantially fewer than $N$ gates when it has $o(N)$ outputs. It does not rule out a linear-size circuit with global sharing, so the unresolved step is still a superlinear routing lower bound.

## C-39 - A linear priority encoder anti-checks the two constant circuits

**Statement.** There is a fan-in-two circuit of size $O(N)$ that, on every nonconstant truth table $f\in\{0,1\}^{N}$, outputs two query positions $q_0,q_1$ with $f(q_0)=0$ and $f(q_1)=1$. Hence it is a valid anti-checker for the fixed hypothesis class consisting of the constant-zero and constant-one circuits, on every high-complexity table.

**Status.** PROJECT-PROVED elementary construction. It is not an anti-checker for all circuits of size $s_1$.

**Proof.** A binary-tree priority encoder finds the first 1 in an $N$-bit word. At each node for a block of length $2^h$, store whether that block contains a 1 and the binary index of its first 1. The flag is the OR of the child flags; the high bit of the index records whether the first 1 lies in the right child, and the remaining $h-1$ bits select between the child indices. The work at a node is $O(h)$ gates. Across the full tree the size is $O(\sum_{h=1}^{n}(N/2^h)h)=O(N)$. Apply a second such encoder to $\neg f$ to find a 0. For nonconstant $f$ both outputs exist and their labels are 1 and 0, respectively.

**Learning.** The constant-zero completion in C-34 is a strong witness against fixed samples but cannot by itself force a large selector: a linear-size selector can search for a 1, and together with the complementary search can defeat both constant hypotheses. A fixed finite family of constant-size hypotheses can likewise be handled by computing one disagreement witness per hypothesis at linear cost. A superlinear lower bound must exploit the simultaneous requirement for the exponentially large class of circuits of size $s_1$, rather than one or a few selected circuits.

## C-40 - Minimax gives a dual anti-approximation margin, not a selector

**Statement.** Let $X=\{0,1\}^n$, $N=2^n$, and let $\mathcal C_s$ be the fan-in-two circuits of size at most $s$. Define
\[
\Delta_s(f)=\max_{\mu\in\Delta(X)}\min_{D\in\mathcal C_s}\Pr_{x\sim\mu}[D(x)\ne f(x)].
\]
There is an absolute constant $C$ such that, for $s\ge n$, if $CC(f)>Cns$, then $\Delta_s(f)\ge 1/3$. Consequently some list $Q$ of $O(s\log(s+n))$ inputs satisfies $\forall D\in\mathcal C_s\;\exists x\in Q:D(x)\ne f(x)$.

**Status.** PROJECT-PROVED reconstruction of the finite minimax / majority argument already underlying C-21. This is a precise semantic formulation, not a new lower bound or an efficient selector.

**Proof.** Use the finite zero-sum game with row strategies $x\in X$, column strategies $D\in\mathcal C_s$, and payoff $1[D(x)\ne f(x)]$. If $\Delta_s(f)<1/3$, minimax gives a distribution $\lambda$ on $\mathcal C_s$ for which every $x$ has expected disagreement below $1/3$. Draw $k=O(n)$ circuits independently from $\lambda$. For each fixed $x$, Hoeffding's inequality bounds the probability that their majority is wrong by $e^{-k/18}$; taking $k\ge18(n\ln2+1)$ makes the union bound over $2^n$ inputs less than 1. Thus some sampled majority computes $f$ everywhere. A fan-in-two majority circuit has $O(k^2)$ gates, so the total is $O(ks+k^2)=O(ns)$ when $s\ge n$, contradicting $CC(f)>Cns$ for sufficiently large absolute $C$. Hence $\Delta_s(f)\ge1/3$.

Choose a witnessing $\mu$. There are $M_s=|\mathcal C_s|\le2^{O(s\log(s+n))}$ circuits. A sample of $q$ independent points from $\mu$ is entirely consistent with any fixed $D$ with probability at most $(2/3)^q$. For $q>\log M_s/\log(3/2)$, a union bound gives a sample inconsistent with every $D$, proving the list-size claim.

**Constructive audit.** The fractional feasibility LP has variables $\mu_x$ and constraints $\mu_x\ge0$, $\sum_x\mu_x=1$, and $\sum_x\mu_x1[D(x)\ne f(x)]\ge1/3$ for every $D\in\mathcal C_s$. For a rational candidate $\mu$, a violated constraint is witnessed by a size-$s$ circuit whose weighted disagreement with $f$ is below $1/3$. Guessing that circuit and evaluating the weighted sum over the explicit truth table is an NP verification. The rational ellipsoid/separation theorem therefore finds a feasible $\mu$ with an NP oracle (the LP has dimension $N$ and polynomial bit complexity in the explicit truth-table input). Random sampling then gives a promised-input $\mathrm{FBPP}^{\mathrm{NP}}$ procedure that outputs a short anti-checker with failure probability at most $\delta$ using $O(s\log(s+n)+\log(1/\delta))$ samples. This is not an always-correct deterministic selector. For a fixed candidate list $Q$, validity is coNP (failure is witnessed by a small circuit agreeing everywhere on $Q$); existentially finding such a $Q$ is naturally a $\Sigma_2^P$ search relation. OPS's selector construction under $NP\subseteq P/poly$ uses its specialized iterative argument, so this generic quantifier count is not a substitute for that proof.

**Circularity / scope.** $\Delta_s(f)=0$ iff $CC(f)\le s$: if $f$ is outside $\mathcal C_s$, the uniform distribution gives every circuit error at least $1/N$. Also, $CC(f)>Cns$ forces $\Delta_s(f)\ge1/3$. Thus on the promise $CC(f)\le s$ versus $CC(f)>Cns$, distinguishing $\Delta_s(f)=0$ from $\Delta_s(f)\ge1/3$ is a semantic reformulation of Gap-MCSP at the same $s$ versus $\Theta(ns)$ scale. The LP language identifies the dual witness and the exact optimization oracle; it does not make the unrestricted lower-bound premise easier by itself. OPS constants must be matched before using this statement in that theorem.

## C-41 - No small fixed menu of distributions witnesses every hard table

**Statement.** Fix $0<\beta<1$ and OPS-scale $s=N^\beta/(cn)$, with high threshold $S=Cns$ for a fixed constant $C$. For a sufficiently large constant $K=K(C,\beta)$, let $w=\lceil Kns\rceil=o(N)$. For every fixed menu $\mu_1,\ldots,\mu_m$ of distributions on $\{0,1\}^n$ with $m w/N=o(1)$, there exists a support $R\subseteq\{0,1\}^n$, $|R|=w$, such that $CC(1_R)>S$ and $\mu_j(R)=o(1)$ for every $j$. Thus no such table-independent menu supplies constant-error dual witnesses for all high-complexity tables. For any fixed $\beta<1$, the complexity condition holds once $K$ is chosen large enough; uniform constants can be chosen over a fixed bounded range of $\beta$ away from $1$.

**Status.** PROJECT-PROVED counting / averaging lemma. It strengthens the fixed-sample obstruction only for data-independent menus. It does not constrain menus whose choice depends on the full truth table.

**Proof.** Choose $R$ uniformly among the $w$-subsets. For each $j$, $\mathbb E[\mu_j(R)]=w/N$. Markov gives $\Pr[\mu_j(R)>2mw/N]\le1/(2m)$; by a union bound, with probability at least $1/2$ all $m$ masses are at most $2mw/N=o(1)$. Meanwhile, circuit counting gives at most $2^{O(S\log(S+n))}$ supports of complexity at most $S$, whereas
\[
\log_2\binom Nw=\Omega\bigl(w\log(N/w)\bigr).
\]
At $s=N^\beta/(cn)$ and $w=Kns$, the latter exponent is $\Omega(KN^\beta(1-\beta)n)$, while the former is $O(C\beta N^\beta n)$; choosing $K$ sufficiently large makes the fraction of low-complexity supports $o(1)$. Hence some $R$ satisfies both the mass bounds and $CC(1_R)>S$. Against the constant-zero circuit, its error under each $\mu_j$ is exactly $\mu_j(R)=o(1)$.

**Adversarial limit.** The selector may have $2^{tn}$ possible query lists, far beyond the sub-$N^{1-\beta}$ menu size ruled out here, and it chooses the list as a function of $f$. C-41 therefore proves the necessity of genuine table-dependent routing but supplies no lower bound for such routing.

## C-42 - Loop-theoretic P-vs-NP manuscript is conditional at the abstract level

**Claim audited.** Otto Beseka Isong, ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“P vs. NP: A Loop-Theoretic Approach,ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â written August 13 and posted to SSRN August 18, 2026 ([SSRN record](https://ssrn.com/abstract=7280038)).

**Evidence available.** The abstract describes internal Loop-theoretic complexity classes and says the separation follows under an ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“internal Loop-theoretic finite-transition capacity principleÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â and ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“explicit Loop-to-complexity bridge axioms.ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â Thus the abstract itself presents the classical implication as conditional on these principles/bridges; it does not state an assumption-free derivation from the standard Turing-machine definitions.

**Status.** NOT VERIFIED AS A CLASSICAL P-vs-NP PROOF; ABSTRACT-LEVEL AUDIT ONLY. The PDF endpoint returned a Cloudflare 403 in this environment, so the exact axiom types, proofs, and possible circularity of the bridge could not be checked. No theorem from the manuscript is used in the active route.

**Required next check if the paper becomes relevant.** Obtain the full text and expand every bridge axiom into ordinary definitions of polynomial-time verification, search, and simulation. In particular, prove that the internal archive-size/transition lower bound transfers with polynomial resource preservation to standard SAT instances and arbitrary deterministic algorithms. Until then, the argument is a conditional framework claim, not a classical separation.

## C-43 - Exact feasible-antichecker condition in the Extended Frege route

**Published statement audited.** Pich and Santhanam, Theorem 7 / informal Theorem 3, ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Towards $P\ne NP$ from Extended Frege lower boundsÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â ([arXiv HTML](https://arxiv.org/html/2312.08163v1), Section 3). For fixed $k\ge3$, suppose a polynomial-time function $F(1^n)$ outputs one of:

1. a polynomial-in-$n^k$ size search circuit $B$ such that every satisfying assignment for a size-$n$ formula $x$ implies that $B(x)$ is a satisfying assignment; or
2. finite sets $A,A'$ and a relation $D$ of total size polynomial in $n^k$, encoding a selected witness $y_x$ for each $x\in A$, with (i) every satisfiable $x\in A$ assigned a valid witness, and (ii) for every size-$n^k$ decision circuit $C$, some $x\in A$ has $\mathrm{SAT}_n(x,y_x)\ne C(x)$.

If $S^1_2$ proves that $F$ has this property, then EF not being polynomially bounded implies $\mathrm{SAT}_n\notin\mathrm{Circuit}[n^k]$ for infinitely many $n$. The theorem's proof translates the $S^1_2$ statement to polynomial-size EF proofs; assuming small SAT circuits then makes the generated search circuit correct and yields p-boundedness of EF.

**Status.** PUBLISHED CONDITIONAL IMPLICATION, SOURCE-VERIFIED. It does not establish either premise unconditionally. The auxiliary function is required to be a single polynomial-time generator whose correctness is provable in $S^1_2$.

**Quantifier audit.** If the generator is replaced by bare existential sets for each $n$, the formal statement gains an existential block before the universal circuit block (the paper identifies a $\forall\Sigma^b_2$ formulation). KPT witnessing then yields a finite adaptive sequence of polynomial-time functions depending on earlier challenge values, not one fixed output list. The authors explain that this does not directly give p-size EF proofs of all tautologies because later circuits/lists depend on earlier witnesses. This is a genuine choice/uniformity bottleneck, not a missing line in the minimax proof.

**Relation to C-40.** C-40 establishes standard-model per-table existence of a short anti-checker under a circuit-hardness gap and describes an NP-oracle fractional construction. It does not provide the uniform $F$, the exact Pich--Santhanam parameter regime, or an $S^1_2$ proof. Therefore it cannot discharge C-43's hypothesis. The route also still assumes EF is not p-bounded; it remains conditional and is not currently a shorter path than O-1.

## C-44 - Under P=NP, anti-checker search collapses to polynomial time, but not to the OPS exponent

**Statement.** Fix an OPS parameter pair with low-circuit class $\mathcal C_s$ and a list budget $t=O(s\log(s+n))$ large enough for the C-40 sampling theorem on high-complexity tables. For explicit truth-table input $f\in\{0,1\}^N$, define
\[
V(f,Q)\iff \forall D\in\mathcal C_s\;\exists j\le t:\ D(q_j)\ne f(q_j).
\]
The search relation $\exists Q\,V(f,Q)$ is in $\Sigma_2^P$ (the circuit description and list have polynomial length in $N$). C-40 guarantees a witness $Q$ whenever $CC(f)$ exceeds its high threshold. If $P=NP$, then $PH=P$, so the decision version and its prefix self-reductions are in $P$; a deterministic polynomial-time algorithm can find a valid $Q$ whenever one exists, and return a default output otherwise. Thus the promised selector has polynomial-size circuits under $P=NP$.

**Proof.** For fixed $(f,Q,D)$, checking whether some listed point disagrees is polynomial time. Hence $V$ is a coNP predicate and existential search over polynomial-length $Q$ is a $\Sigma_2^P$ search problem. Under $P=NP$, $\Sigma_2^P=P$. For each output-bit prefix $p$, the question whether $p$ extends to a valid $Q$ remains in $\Sigma_2^P=P$; querying this decision procedure bit by bit constructs $Q$ in polynomial time. The promise-side existence follows from C-40. Standard unrolling gives polynomial-size circuits, with an uncontrolled polynomial exponent.

**Exact limitation.** This is not a new route to the magnification premise: $P=NP$ already implies $NP\subseteq P/poly$, and the contrapositive of OPS supplies a near-linear nonuniform upper bound for an appropriate small-$\beta$ choice, with the theorem's exact quantifiers. The direct $PH$-collapse construction only yields $N^{O(1)}$ circuits; it does not give $N^{1+\epsilon}$ or a contradiction to O-1. The missing resource statement is a near-linear implementation of this particular $\Sigma_2$ search relation, not merely its placement in $P$.

**Status.** CONDITIONAL SEARCH-TO-DECISION LEMMA, PROVED; no P-vs-NP progress. It calibrates the quantitative gap between logical decidability and the circuit-size threshold required by OPS.

## C-45 - Anti-checker synthesis is a version-space transversal problem

**Statement.** Let $X=\{0,1\}^n$, $f:X\to\{0,1\}$, and $\mathcal C_s$ be the size-$s$ circuit class. Define disagreement sets $E_D=\{x:D(x)\ne f(x)\}$ and the residual version space after query list $Q$ by
\[
V_f(Q)=\{D\in\mathcal C_s:E_D\cap Q=\varnothing\}.
\]
Then $Q$ is an anti-checker exactly when $V_f(Q)=\varnothing$, equivalently when $Q$ hits every $E_D$. On the high-complexity promise $CC(f)>s$, every $E_D$ is nonempty. Given $Q$ and a surviving $D\in V_f(Q)$, one can find a counterexample $x\in E_D$ by evaluating $D$ against the explicit truth table $f$ in $O(N\,\mathrm{poly}(s,n))$ time (or by scanning the table and stopping at the first mismatch). Adding $x$ strictly removes at least $D$, so the loop terminates after at most $|\mathcal C_s|=2^{O(s\log(s+n))}$ rounds.

**What the margin adds.** If C-40 supplies a distribution $\mu$ with $\mu(E_D)\ge\gamma$ for every $D$, define the residual potential $\Psi(Q)=|V_f(Q)|$. For every current $Q$,
\[
\mathbb E_{x\sim\mu}\Psi(Q\cup\{x\})=\sum_{D\in V_f(Q)}(1-\mu(E_D))\le(1-\gamma)\Psi(Q).
\]
Thus some point contracts the number of survivors by a factor at most $1-\gamma$. Repeating this choice gives a deterministic *existence proof* of a hitting list of length at most $\lfloor\log|\mathcal C_s|/[-\log(1-\gamma)]\rfloor+1=O(\gamma^{-1}\log|\mathcal C_s|)$, matching the random-sampling scale. The key unresolved distinction is existence versus finding a contracting point: for fixed $Q,x$, the natural score counts circuit descriptions consistent with $Q$ and disagreeing at $x$. These are #P-style counting quantities, but no reduction shows they are necessary for every selector or that this specific counting problem is hard.

**Oracle stress test.** In arbitrary set systems, a black-box routine that returns any unhit set and one point in it can take $m$ rounds even if a one-point transversal exists: take $E_i=H\cup\{p_i\}$ for common nonempty $H$ and distinct private points $p_i$, and let the oracle always return $p_i$. This only rules out the naive counterexample loop in a black-box model. It does not prove that circuit-specific structure cannot yield a faster selector, nor that approximate counting is necessary for every algorithm.

**Status.** PROVED REFORMULATION plus a standard potential calculation; no selector lower bound. It sharpens the active bottleneck from ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“find an anti-checkerÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â to ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“construct a short transversal for the circuit disagreement hypergraph without enumerating or exactly counting its exponentially large version space.ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â Any claim that this requires #P/counting remains a conjectural route diagnosis unless supported by a reduction.

## C-46 - Teaching-set literature matches the logarithmic query count but gives no circuit-selector bound

**Source.** Compton, Pabbaraju, and Zhivotovskiy, ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Lower Bounds for Greedy Teaching Set ConstructionsÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â (arXiv:2505.03223, submitted 2025-05-06), [arXiv HTML](https://arxiv.org/html/2505.03223).

**Verified result.** The paper studies greedy teaching-set procedures for finite concept classes of VC dimension $d$. It shows the $k=1$ greedy procedure can require $\Omega(\log|\mathcal C|)$ examples, and for small constant $c>0$ extends a $\Omega(\log\log|\mathcal C|)$ lower bound to $k\le\lceil cd\rceil$; the authors stress that this concerns the analyzed procedure, not all teaching-set methods. Its target concept lies within the class (or is selected by the procedure), unlike our fixed high-complexity $f$ outside $\mathcal C_s$.

**Relevance and limit.** C-45's residual version space is a teaching-set/epsilon-net style object. The paper's $\Omega(\log|\mathcal C|)$ one-point greedy bound is the same order as C-45's $O(\log|\mathcal C_s|)$ query bound when $\gamma$ is constant, so it does not undermine the balanced-contraction argument. In C-45, the dual margin guarantees a point removing a $\gamma$ fraction of every current version space; the unresolved issue is computing such a point, not proving that one exists or bounding the number of ideal greedy rounds. The paper does not address that circuit-specific computation, and no reduction to Gap-MCSP or P vs NP is known here.

**Status.** VERIFIED RELATED LITERATURE; methodological input only, no theorem transferred to the project.

## C-47 - A greedy anti-checker can be extracted with an exact #P counting oracle

**Statement.** Under C-40's high-table margin premise, there is a deterministic $\mathrm{FP}^{\#P}$ procedure that outputs a valid anti-checker list of $O(\gamma^{-1}s\log(s+n))$ queries. For the OPS scale, its number of #P oracle calls is $O(Ns\log(s+n))=O(N^{1+\beta})$ for fixed $\beta>0$ and $s=2^{\beta n}/(cn)$.

**Construction.** Let $H$ be the finite set of valid descriptions of circuits of size at most $s$. Given the current list $Q$, use #P queries to compute
\[
Z_Q=|\{D\in H:D|_Q=f|_Q\}|,
\qquad
G_{Q,x}=|\{D\in H:D|_Q=f|_Q,\ D(x)\ne f(x)\}|
\]
for each $x\in\{0,1\}^n$. If $Z_Q=0$, return $Q$. Otherwise choose $x$ maximizing $G_{Q,x}$ and append it. Each count is #P because a circuit-description string is a polynomial-length witness and checking its size, validity, and values on $Q\cup\{x\}$ is polynomial time.

**Proof.** The dual-margin distribution $\mu$ from C-40 satisfies $\mu(E_D)\ge\gamma$ for every $D$. Therefore
\[
\sum_x\mu(x)G_{Q,x}=\sum_{D:D|_Q=f|_Q}\mu(E_D)\ge\gamma Z_Q.
\]
Some $x$ has $G_{Q,x}\ge\gamma Z_Q$, so the maximum-coverage choice leaves at most $(1-\gamma)Z_Q$ survivors. After $O(\gamma^{-1}\log|H|)=O(\gamma^{-1}s\log(s+n))$ rounds, no descriptions survive and $Q$ is valid. If the high-table promise fails, cap the loop and return a default output.

**Limit.** This is an explicit oracle algorithm, not a polynomial-size ordinary circuit or an unconditional selector. Exact #P answers are doing the balancing work; the number of calls is near-linear in $N$ only at small fixed $\beta$, while the oracle itself is unbounded relative to P. No lower bound shows that every selector needs this counting operation.

**Status.** CONDITIONAL-ORACLE CONSTRUCTION, PROVED from C-40. It makes the constructive barrier concrete but does not resolve O-1.

## C-48 - Approximate version-space scores reconstruct the conditional OPS selector

**Statement.** Fix the OPS parameters $N=2^n$, $s=2^{\beta n}/(c n)$, and high threshold $S=2^{\beta n}$, with constants chosen so $S>Cns$ for the absolute constant in C-40. If $NP\subseteq P/poly$, then there is a nonuniform anti-checker selector for every table of circuit complexity $>S$, with list length $O(s\log(s+n))$ and circuit size $N^{1+O(\beta)}$. This is a version-space derivation of the same conditional upper-bound phenomenon as the published OPS anti-checker lemma, not a new lower bound or a P-vs-NP result.

**Local score.** For a transcript \(\tau=((q_i,b_i))_{i\le k}\), candidate point \(x\), and bit \(b\), let
\[
G_{\tau,x,b}=\#\{D\in H_s: D(q_i)=b_i\ (i\le k),\ D(x)\ne b\},
\]
where \(H_s\) is a fixed set of valid syntactic descriptions of size-at-most-\(s\) circuits. This is a #P function: a description is the witness and the displayed tests are polynomial-time. Stockmeyer approximate counting gives a BPP\(^NP\) algorithm for a constant-relative approximation when the count is nonzero; an NP query detects zero exactly. Under \(NP\subseteq P/poly\), these local approximation functions have deterministic polynomial-size circuits in their own input length. For a fixed input length, amplify the randomized procedure to error below (2^{-m-2}) on each (m)-bit instance and use a union bound over all instances before fixing its random tape. The resulting circuit is correct on every transcript of that length.

**Greedy proof.** Suppose the current transcript is consistent with \(Z\) descriptions. C-40 gives a distribution \(\mu_f\) for which every described circuit errs with mass at least \(\gamma\). Therefore
\[
\sum_x\mu_f(x)G_{\tau,x,f(x)}\ge\gamma Z,
\]
so some point has score at least \(\gamma Z\). If all nonzero scores are approximated within a factor \(1\pm\delta\), choosing the largest estimate selects an actual score at least \((1-\delta)/(1+\delta)\) times the maximum. With fixed \(\delta<1/3\), each round contracts the survivor count by a constant factor. After \(K=O(\gamma^{-1}\log|H_s|)=O(s\log(s+n))\) rounds none survive. If the table is not on the high-complexity promise, the same fixed-length circuit may simply output its (K) addresses; correctness is required only on high tables.

**Circuit accounting.** The complete transcript has length \(m=O(Kn)=O(s n^2)=N^{\beta+o(1)}\). In each round, evaluate the local score circuit for all (N) candidate points in parallel and take a maximum; this costs (N\,m^{O(1)}+N\operatorname{poly}(s,n)) gates. Reading the truth-table bit at the selected address costs (O(N)) gates per round. Across (K=N^{\beta+o(1)}) rounds, the size is (N^{1+O(\beta)}). The output length (Kn=O(N^\beta n)) is below the OPS allowance (2^{10\beta n}) for each fixed sufficiently small \(\beta>0\).

**Audit / limit.** This shows the C-47 #P oracle is not essential to the *conditional construction*: approximate local scores suffice when NP has polynomial-size circuits. It does not give an unconditional selector, because the small circuits for the BPP\(^NP\) approximator are obtained from the assumption (NP\subseteq P/poly). It also does not show that every selector computes or approximates these scores. Thus it reconstructs a known direction of the OPS magnification argument and leaves O-1 untouched. Treat ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“score computation is necessaryÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â as false unless a separate reduction proves it.

**Relation to published work.** OPS prove the corresponding conditional anti-checker construction in Lemma 4.1 of [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf). C-48 is a reconstruction using the C-45 version-space potential, not a claim of novelty for the conditional selector theorem.

**Status.** CONDITIONAL RECONSTRUCTION, PROVED from C-40 and Stockmeyer approximate counting; no separation progress.

## C-49 - Local correction upgrades anti-checkers to robust puncturing certificates

**Statement.** For fan-in-two circuits over a fixed complete basis there is a constant $a$ such that changing a truth table on $r$ inputs increases circuit size by at most $a n r+a$, by patching the changed points with minterm indicators. Consequently, if $Q$ is an anti-checker for $f$ against all circuits of size at most $s_1$, then for every circuit $D$ of size at most $s_0<s_1$,

    d_H(f|_Q,D|_Q) > (s_1-s_0-a)/(a n)

up to integer rounding. Otherwise patch $D$ at its mismatching points on $Q$ to obtain a size-at-most-$s_1$ circuit agreeing with $f$ on every query, contradicting the anti-checker property.

**OPS-scale consequence.** Taking $s_0=\lfloor s_1/2\rfloor$, every valid selector's trace is at distance $\Omega(s_1/n)$ from every size-$s_1/2$ circuit trace. For a minimax-length list with $|Q|=O(s_1\log(s_1))$, this is relative distance $\Omega(1/n^2)$ for fixed $\beta>0$. The OPS selector interface allows up to $t=2^{10\beta n}$ queries, however, so for a selector output of $q$ distinct queries the general relative bound is only $\Omega(s_1/(nq))$; at the maximum budget this is $\Omega(N^{-9\beta}/n^2)$. Globally, $CC(f)>s_2$ implies Hamming distance $\Omega((s_2-s_1)/n)=\Omega(N^\beta/n)$ from every size-$s_1$ circuit.

**Proof.** For each point where the base circuit has the wrong label, construct its minterm on the $n$ input bits. An OR of correction minterms and a masking conjunction patches both 0-to-1 and 1-to-0 errors using $O(n)$ gates per point. If $D$ has $r$ mismatches on $Q$, the patched circuit agrees with $f$ on all of $Q$; the displayed radius ensures its size is at most $s_1$, which is forbidden by the selector guarantee.

**Attempted bridge.** Atserias-Muller distinguishers can amplify the relative trace distance after $Q$ has been selected, but this does not charge the arbitrary nonlinear circuit that chooses $Q_f$. At fixed OPS $\beta$, the generic count of low-circuit truth tables is at most $2^{O(N^\beta)}$, which does not establish the $2^{N^{o(1)}}$ sparsity premise of their general formula magnification theorem. Their uniform MCSP theorem says that a specified lower bound for P-uniform approximate-MCSP circuits would imply $P\ne NP^{\oplus P}$, not the target $P\ne NP$; the general formula lower-bound conclusion also does not imply a circuit lower bound for NP. See [*Simple general magnification of circuit lower bounds*](https://arxiv.org/html/2503.24061), Theorems 8-11.

**Limit/status.** PROVED UNIVERSAL NECESSARY CONDITION; no superlinear selector lower bound follows. The lemma sharpens the coding interpretation but leaves O-1 unchanged: computing the input-dependent robust puncturing is still the unresolved step.

## C-50 - High complexity forces a large majority-error region in every small circuit subfamily

**Statement.** Let $f:\{0,1\}^n\to\{0,1\}$ have $CC(f)>s_2$. Let $D_1,\ldots,D_k$ be distinct circuits of size at most $s_0$, where $k$ is odd. Write $E_i=\{x:D_i(x)\ne f(x)\}$, and let

    H = {x : x belongs to at least (k+1)/2 of E_1,...,E_k}.

The majority circuit $M=\mathrm{Maj}(D_1,\ldots,D_k)$ has size $O(k s_0+k^2)$ and differs from $f$ exactly on $H$. Local correction then gives

    |H| > (s_2-O(k*s_0+k^2))/(a*n)-O(1/n),

for the point-correction constant $a$ from C-49. In particular, for every fixed odd $k$ and OPS choice $s_0\le s_1$, this is $\Omega(N^\beta/n)$ for sufficiently large $n$.

For the OPS parameters, the same $\Omega(N^\beta/n)$ lower bound holds uniformly for all odd $k\le\kappa n$, for a sufficiently small constant $\kappa>0$: then the majority circuit has size at most $s_2/2$ for all sufficiently large $n$.

**Pair-overlap consequence (for odd $3\le k\le\kappa n).** Since every point of $H$ lies in at least $\binom{(k+1)/2}{2}$ pairwise intersections, averaging gives a pair $i\ne j$ with

    |E_i intersect E_j| >= ((k+1)/(4k))*|H| = Omega(N^beta/n)

for fixed $k$. Thus no fixed-size subfamily of small circuits can have error sets whose majority overlap is confined to a constant-size marker.

**Proof.** A fan-in-two circuit computes the majority of $k$ bits using $O(k^2)$ gates, in addition to the $k$ input circuits. At a point $x$, that majority is wrong exactly when at least $(k+1)/2$ of the $D_i$ are wrong. If $H$ were smaller than the displayed threshold, patching $M$ at all points in $H$ would compute $f$ with at most $s_2$ gates, contrary to the high-complexity premise. For the pair bound, sum $|E_i\cap E_j|$ over all pairs and count incidences pointwise on $H$; division by $\binom{k}{2}$ gives the stated factor.

**Relation and limit.** This extends C-28's majority-overlap observation from supports of the form $1_R$ to arbitrary high-complexity truth tables and includes a quantitative region-size bound. It rules out a naive reduction that tries to force one unique anti-checker query using a fixed number of almost-disjoint error sets; the OPS bound in fact rules out majority overlap confined to fewer than $\Omega(N^\beta/n)$ points for subfamilies as large as $\kappa n$. It does not provide a short transversal or a way to locate $H$; C-28's arbitrary-hypergraph counterexample still blocks a generic hitting-set conclusion.

**Status.** PROVED structural constraint, not a selector lower bound. The next step would need to exploit how the whole circuit disagreement family realizes these heavy-overlap regions.

## C-51 - The low-circuit error-overlap graph is dense

**Statement.** Fix a high table `f` with `CC(f)>s2`, and let `C` be the set of Boolean functions of circuit complexity at most `s0=s1`. For each `D in C`, set `E_D={x:D(x) != f(x)}`. Join distinct `D,D'` when `|E_D intersect E_D'| >= h/3`, where

    h = (s2 - 3*s1 - O(1))/(a*n) = Omega(N^beta/n)

and `a` is the local-correction constant from C-49. Then the graph contains at least `binom(|C|,2)-floor(|C|^2/4) = |C|^2/4-O(|C|)` edges.

**Proof.** For any triple of distinct low-circuit functions, their majority has circuit size at most `3*s1+O(1)`. It errs exactly on the inputs lying in at least two of the three error sets. Patching the majority at those points and applying C-49 shows that its error set has size at least `h`. Each point in this region contributes to at least one of the three pairwise intersections, so some pair has intersection at least `h/3`. Thus every vertex triple in the heavy-overlap graph contains an edge; its complement is triangle-free. Mantel's theorem bounds the complement by `floor(|C|^2/4)`, proving the edge count.

**Residual-family corollary.** For any subfamily of `m` low-circuit functions, the same graph has `Omega(m^2)` heavy edges. Each such edge has at least `h/3` common error points, so for `d_x=|{D in A:D(x) != f(x)}|`,

    sum_x binom(d_x,2) >= Omega(h*m^2).

Since `binom(d_x,2)<=d_x^2/2`, some coordinate is wrong for at least `Omega(m*sqrt(h/N))` members. An ideal max-score process over residual distinct functions therefore contracts by only `Omega(sqrt(h/N))=Omega(N^(-(1-beta)/2)/sqrt(n))` per round. Its combinatorial query bound `O(N^((1+beta)/2)*sqrt(n))` is weaker than the C-40 minimax bound `O(N^beta*poly(n))` at fixed `beta<1`. This is only an existential process: counting distinct functions may be harder than #P counting syntactic circuit descriptions, and no ordinary circuit cost for score extraction is established.

**Generality audit.** The graph theorem is about all low-circuit functions and is representation independent. It still does not imply a small or efficiently computable transversal. In an abstract common-core model, many distinct hypotheses all err on a fixed set `S` of size `h`; every majority-error region contains `S`, but querying one fixed point of `S` is a constant-size selector. Thus overlap statistics alone cannot prove a superlinear selector lower bound. The required additional fact must use the richness and specific geometry of the full circuit class on actual high-complexity tables.

**Status.** PROVED structural refinement of C-50; no movement on O-1. Full derivation and the adversarial toy model are in [`REASSESSMENT_2026-09-25_CONTINUED.md`](REASSESSMENT_2026-09-25_CONTINUED.md).

## C-52 - A near-linear first-query selector from global marginals

**Statement.** At exact OPS parameters s1=2^(beta*n)/(10n), s2=2^(beta*n), one nonuniform O(Nn)-gate circuit family finds, for every high table, a coordinate where at least 3/20 of all size-s1 syntactic circuit descriptions disagree.

**Proof.** If the minimax dual margin were below 3/10, finite minimax gives a distribution on size-s1 circuits with error below 3/10 at every fixed input. Take the smallest odd k at least 9n independent samples. Hoeffding bounds the majority error at a fixed input by exp(-0.08k), so a union bound over N=2^n inputs is less than one since 0.72>ln 2. Some sampled majority computes f exactly. Its size is ks1+O(k^2) <= (0.9+o(1))s2 < s2, contradiction. Thus the margin is at least 3/10.

Let H be the finite set of fixed-length descriptions of size-s1 circuits and choose D uniformly. Put q_x=Pr[D(x)=1]. Averaging the margin over descriptions gives sum_x mu_f(x) Pr[D(x) != f(x)] >= 3/10, so some coordinate has error mass >=3/10. A uniform sample of m=O(log N)=O(n) descriptions has empirical qhat_x within 3/40 of every q_x, by Hoeffding and a union bound. Hardwire the N integer frequencies. For any input f, the empirical disagreement score at x is qhat_x if f(x)=0 and 1-qhat_x if f(x)=1. A maximizing coordinate has true error mass at least 3/20. The score tournament costs O(Nn) gates and the profile takes O(N log n) bits. Duplicate descriptions are harmless.

**Limit.** This is one contraction, not a full anti-checker. Uniform additive approximation through transcripts of length k costs O((kn+log(1/eta))/delta^2) samples. Conditional scores at survivor mass rho need delta=O(rho); below that scale the sample may miss a surviving circuit. This is a limitation of this sampling method, not a lower bound for arbitrary selectors. Full proof: [C-52 report](C52_FIRST_QUERY_AND_ADAPTIVE_SAMPLING.md).


## C-53 - Relative sampling tracks adaptive contractions to a mass threshold

**Statement.** Let $\mathcal H$ be a finite distribution on low-circuit descriptions with dual margin $\gamma$ against a high table $f$. Let $\mathcal R_k$ consist of every residual event $A_\tau$ and every one-more-query disagreement event from transcripts of length at most $k$. For any $0<\rho\le1$, there is a uniform sample of
$$m=O(((k+1)n+\log(1/\eta))/(\gamma\rho))$$
descriptions that, with probability at least $1-\eta$, supports a greedy selector eliminating at least a $\gamma/2$ fraction of every residual version space of mass at least $\rho$, simultaneously over all such transcripts.

**Proof.** The range count is $|\mathcal R_k|\le O((k+1)(2N)^{k+1})$. Let $\lambda=\gamma\rho/8$. Chernoff plus a union bound gives relative error at most $1/4$ for every range of mass at least $\lambda$, at sample size $O((\log|\mathcal R_k|+\log(1/\eta))/\lambda)$. The same tail bound ensures every event of mass below $\lambda$ has empirical frequency below $2\lambda$. For a residual $A$ with mass $r\ge\rho$, the dual-margin average gives a coordinate whose disagreement event has mass at least $\gamma r$. Its empirical score is at least $3\gamma r/4$. Any event of true mass below $\gamma r/2$ has empirical score at most $5\gamma r/8$ if it is at least $\lambda$, and below $\gamma r/4$ otherwise. Thus an empirical maximizer has true conditional error at least $\gamma/2$. The sample works for every transcript range at once, so adaptivity causes no additional union-bound loss beyond $\log|\mathcal R_k|=O(kn)$.

**Limit.** This improves the additive Hoeffding sample bound from inverse-square to inverse-linear dependence on the smallest tracked residual mass. It permits polynomial-size samples to track inverse-polynomial residuals. Constant-factor contraction brings the residual below such a threshold after only $O(n)$ rounds unless it has already vanished. Guaranteeing exact termination by this generic method requires $\rho\le1/|\mathcal H|$ and a sample scaling with $|\mathcal H|$; this is superpolynomial in $N$ for the low-circuit description class. This is a limitation of global sampling, not a lower bound for arbitrary selectors and not a proof that a rare residual is reached.

**Status.** PROVED range-sampling lemma; no O-1 progress. Detailed derivation: [C-52/C-53 report](C52_FIRST_QUERY_AND_ADAPTIVE_SAMPLING.md).


## C-54 - Relative-sampling contraction reaches a nonempty tail before anti-checker length

**Statement.** For every transcript of $q=O(n)$ queries, there is a size-$s_1$ circuit agreeing with all labels, for sufficiently large $n$ at fixed $\beta>0$. Therefore a C-53 sample-based greedy process, even when implemented with an $N^{1+\epsilon}$-size circuit for any fixed $\epsilon>0$, cannot obtain a complete anti-checker during the $O(n)$ phase for which it tracks inverse-polynomial residual mass. If it makes constant-fraction contractions until the residual falls below $N^{-a}$, that first below-threshold residual is nonempty.

**Proof.** A DNF consisting of one minterm for each queried point labeled 1 outputs 1 on those points and 0 on all other queried points. Its size is $O(qn)$. For $q=O(n)$ this is $O(n^2)<s_1$ eventually. Meanwhile C-53 gives a contraction by at least $\gamma/2$ whenever the residual mass is at least $\rho=N^{-a}$. After $O(\log(1/\rho))=O(n)$ such rounds, the residual mass crosses below $\rho$. The transcript length is still $O(n)$ and hence below the DNF interpolation threshold $\Omega(s_1/n)$; the residual is nonempty. The C-53 sample size and direct score implementation at this depth are $m=O(n^2N^a)$ and $O(N^{1+a}\operatorname{poly}(n))$ gates.

**Scope.** This proves where the relative-sampling guarantee ends for this greedy construction, not that a selector cannot continue with a different computation or a richer conditional sampler. The known query-length lower bound $\Omega(s_1/n)$ is still far below the allowed OPS budget and gives no selector gate lower bound.

**Status.** PROVED method-specific stress test; O-1 unchanged. See [C-52/C-53 report](C52_FIRST_QUERY_AND_ADAPTIVE_SAMPLING.md).


## C-55 - Anti-checker existence is not an efficient circuit selector

**Statement.** For every high table $f$, there is an anti-checker $Q$ of size $O(\log|\mathcal C_{s_1}|)\le t_n$, but this yields only $\forall f\in F_n\,\exists Q\in X_n^{\le t_n}\,R_n(f,Q)$. A selector circuit requires one family $S_n$ of size $N^{1+\epsilon}$ satisfying $\forall f\in F_n\,[|S_n(f)|\le t_n\land R_n(f,S_n(f))]$, where $t_n=2^{10\beta n}$ is the OPS output budget.

**Proof.** C-52 gives $\Delta(f)\ge3/10$. For every nonempty residual subset of low-circuit descriptions, its uniform distribution is among the distributions covered by the minimax margin, so some coordinate disagrees with at least 3/10 of its mass. Greedily query such a coordinate; the number of remaining descriptions falls by a factor at most 7/10 per step, so $O(\log|\mathcal C_{s_1}|)$ queries empty the residual. This is an existence proof. The predicate $R_n(f,Q)$ that no low circuit matches the labels is coNP-checkable, since its negation is witnessed by a circuit description. Nothing in totality of this relation supplies a small circuit to select $Q$ from $f$.

**Generality / status.** This formalizes the unresolved witness-uniformization step; it does not strengthen O-1. A lower bound for one greedy implementation would not imply a lower bound for arbitrary selectors. Full quantifier and complexity audit: [O-1 selector Skolemization audit](O1_SELECTOR_SKOLEMIZATION_AUDIT.md). PROVED reformulation; O-1 remains OPEN.


## C-56 - A valid anti-checker is constant on a trace cylinder

**Statement.** Fix a query set $Q$ of $q$ distinct inputs and let $T_Q=\{D|_Q:CC(D)\le s_1\}$. If $y\notin T_Q$, then every truth table $f$ with $f|_Q=y$ has $R_n(f,Q)$. There are exactly $2^{N-q}$ such tables, of which at least $2^{N-q}-M_2$ have circuit complexity greater than $s_2$, where $M_2$ is the number of size-$s_2$ functions.

**Proof.** The anti-checker predicate for fixed $Q$ is exactly $f|_Q\notin T_Q$, so it is invariant under changing any bits outside $Q$. At most $M_2$ extensions have circuit complexity at most $s_2$; subtracting this count gives the bound.

For uniformly random $f$, the trace is uniform on $\{0,1\}^q$, hence $\Pr_f[R_n(f,Q)]=1-|T_Q|/2^q\ge1-|\mathcal C_{s_1}|/2^q$. So one fixed list may work for almost every table once $q\gg\log|\mathcal C_{s_1}|$, while its all-zero trace still fails and has many high-complexity extensions whenever $q+\log M_2<N$.

**OPS consequence.** If $q\le2^{10\beta n}$ and fixed $\beta<1/10$, then $q=o(N)$ and $\log_2 M_2=O(s_2\log(n+s_2))=o(N)$. For any anti-realizable trace $y$, almost all its extensions are high-complexity tables sharing the same valid list.

**Limit / learning.** This refutes output-counting arguments that assume one short list can serve only a few high tables. It does not construct a selector or show that a fixed list works for every high table: the trace must first lie outside $T_Q$. See the four-route audit in [O-1 selector Skolemization audit](O1_SELECTOR_SKOLEMIZATION_AUDIT.md). PROVED structural fact; no O-1 progress.


## C-57 - External teaching-set length is between patching and minimax bounds

**Definition.** For a target $f$ and hypothesis class $\mathcal C$, set $\operatorname{ETD}_{\mathcal C}(f)=\min\{|Q|:f|_Q\notin\{D|_Q:D\in\mathcal C\}\}$ when $f\notin\mathcal C$.

**Statement.** If $CC(f)>s_2$ and $\mathcal C=\mathcal C_{s_1}$ at OPS parameters, then

$$
\Omega(s_1/n)\le\operatorname{ETD}_{\mathcal C_{s_1}}(f)
\le O(\log|\mathcal C_{s_1}|)=O(s_1\log(s_1+n)).
$$

**Proof.** Any valid $Q$ must be at Hamming distance $\Omega(s_1/n)$ from the trace of every circuit of size at most $s_1/2$, by C-49's point-patching argument. This forces $|Q|=\Omega(s_1/n)$. For the upper bound, C-52's margin holds for every distribution supported on every nonempty residual family; choose the uniform distribution and repeatedly query a coordinate wrong on at least 3/10 of survivors. The survivor count contracts by at least a factor 7/10 each round, so $O(\log|\mathcal C_{s_1}|)$ queries suffice.

**Scope / status.** This narrows the combinatorial certificate-length range to within polynomial factors but leaves selector circuit complexity untouched. It is a project-defined lens, not a claim that ordinary teaching-dimension hardness transfers. PROVED from C-49/C-55; no new O-1 lower bound.

## C-58 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Local changes preserve a disjoint valid anti-checker

**Statement.** If $Q_0$ is valid for a table $g$ against every circuit in $\mathcal C_{s_1}$, then it remains valid for every $h$ satisfying $h|_{Q_0}=g|_{Q_0}$. In particular, arbitrary changes on a patch $P$ disjoint from $Q_0$ preserve $Q_0$ as a valid output.

**Proof.** For each low circuit $D$, validity gives a point $x\in Q_0$ with $D(x)\ne g(x)$. Since $h(x)=g(x)$, the same point witnesses $D(x)\ne h(x)$. This holds for every $D$.

**Use and scope.** It defeats local patch encodings whenever a common valid list for the unpatched base misses the payload region. It says nothing about modifications that invalidate every base list, nor does it lower-bound arbitrary selectors. PROVED; semantic statement over the full circuit class.

## C-59 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Patch-switch lemma for easy-decoding regions

**Statement.** Let $g$ be a Boolean function and let $D_i,D_j$ have circuit size at most $s_1$. If $E_{D_i}(g)\subseteq P_i$, $E_{D_j}(g)\subseteq P_j$, and $P_i\cap P_j=\varnothing$, then
$$CC(g)\le 2s_1+CC(\mathbf 1_{P_i})+O(1).$$

**Proof.** Output $D_j(x)$ on $P_i$ and $D_i(x)$ outside $P_i$. The first circuit is correct on $P_i$ because $D_j$ can err only on disjoint $P_j$; the second is correct off $P_i$. A mux costs constant additional gates once $\mathbf 1_{P_i}$ is computed.

**Consequence.** At the OPS ratio $s_2=cn s_1$, a table with $CC(g)>s_2$ cannot have this pair of low approximants when $P_i$ has polynomial-in-$n$ indicator complexity. Thus the natural reduction gadget in which each omitted source bit leaves a low-circuit approximation wrong only on that bit's easy-decoding block cannot encode a high table.

**Scope warning.** The condition that every *short* transversal meets a region $P$ does not imply that some disagreement set lies inside $P$. The hypergraph with edges $\{p,x_i\}$ for $t+1$ distinct $x_i$ has the short transversal $\{p\}$, every transversal of size at most $t$ meets $P=\{p\}$, and no edge is contained in $P$. Therefore C-59 rules out a specific localized-approximation gadget, not every all-valid-output reduction. PROVED; not an O-1 lower bound.

## C-60 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Kannan's theorem does not directly lower-bound the selector

**Statement.** For each fixed $k$, Kannan gives a (potentially $k$-dependent) language $L_k\in\Sigma_2^P\cap\Pi_2^P$ outside $\mathrm{SIZE}(n^k)$. A search reduction must map source input $x$ to a high table $f_x$ and have a decoder $B(x,Q,f_x|_Q)$ recover $L_k(x)$ for every valid selector output $Q$. With table blowup $N=m^{a_k}$, selector exponent $a_k(1+\epsilon)$, and generation/decoding circuit exponents $b_k,d_k$, the composed circuit exponent is at most $e_k=\max\{a_k(1+\epsilon),b_k,d_k\}$ up to lower-order factors. Contradiction requires $k>e_k$, as well as the high-table promise and all-output correctness.

**Status.** The theorem is established literature; no reduction meeting these conditions is known in this project. This is a failed direct transfer, not evidence against the selector lower bound itself. Reference: [Kannan 1982](https://doi.org/10.1016/S0019-9958(82)90382-5).

## C-61 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Mandatory regions must carry dual-margin mass

**Setup.** Fix a high table $f$ at the OPS ratio, and let $E_D=\{x:D(x)\ne f(x)\}$ for each distinct function $D$ of circuit size at most $s_1$. By C-52 there is a distribution $\nu$ on coordinates with $\nu(E_D)\ge\gamma=3/10$ for every such $D$. Let $M_1$ be the number of these low-circuit functions and let $t$ be the allowed list length.

Call a region $P\subseteq\{0,1\}^n$ **mandatory** if every anti-checker list of length at most $t$ for $f$ intersects $P$. Put $\alpha=(\ln M_1)/t$. If $\alpha<\gamma$, every mandatory region obeys
$$
\nu(P)\ge\frac{\gamma-\alpha}{1-\alpha}.
$$
Consequently, $m$ pairwise disjoint mandatory regions satisfy
$$
m\le\left\lfloor\frac{1-\alpha}{\gamma-\alpha}\right\rfloor.
$$

**Proof.** Write $p=\nu(P)$. If $p<\gamma$, condition $\nu$ on the complement of $P$. For every low circuit, its conditional error mass is at least $\delta=(\gamma-p)/(1-p)$. Draw $t$ independent coordinates from this conditional distribution. A fixed circuit is missed with probability at most $e^{-t\delta}$, so the union bound over $M_1$ low functions is less than one whenever $t\delta>\ln M_1$. There is then a valid anti-checker list of at most $t$ points wholly outside $P$, contradicting mandatory status. Hence $t\delta\le\ln M_1$, which rearranges to the stated lower bound on $p$. The case $p\ge\gamma$ also satisfies it. For disjoint regions, their $\nu$-masses sum to at most one, yielding the bound on $m$.

**OPS consequence.** Here $\ln M_1=O(s_1\log(s_1+n))=O(N^\beta)$ while $t=N^{10\beta}$, so $\alpha=O(N^{-9\beta})$. For all sufficiently large $n$, $\alpha<1/15$ and $(1-\alpha)/(3/10-\alpha)<4$. Thus at most three pairwise-disjoint regions can be mandatory for every list within the OPS budget.

**Scope / status.** This is a proved corollary of the dual margin plus random sampling; it is not claimed as a new result in the literature and gives no selector-circuit lower bound by itself. It blocks reductions that require every valid output on a fixed high table to hit four or more disjoint prescribed regions. It does not rule out overlapping regions, encoding across many addresses in a single region, or arbitrary all-valid-output decoding. PROVED from C-52 and finite-class counting.

**Fractional-packing form.** If mandatory regions P carry nonnegative weights w_P with sum_{P containing x} w_P at most one for every address x, then their total weight is at most (1-alpha)/(gamma-alpha). Indeed, integrate the pointwise overlap bound against nu to get sum_P w_P nu(P) <= 1, and use the mass lower bound already proved for each P. Thus the fractional packing number of mandatory regions is at most 10/3+o(1) at OPS parameters; bounded-overlap families inherit the corresponding linear bound.
**Common-witness corollary.** Let $p_*=(\gamma-\alpha)/(1-\alpha)$. If $\nu(P)<p_*$, the same sampling argument produces a valid list $Q\subseteq\{0,1\}^n\setminus P$ of at most $t$ points for the base table $f$. Every table $h$ agreeing with $f$ outside $P$ has the identical labeled trace on $Q$, so this one list is valid for all such $h$ as well. Thus a source family whose tables vary only inside a dual-light patch region has an output-independent common witness; any decoder that sees only the list and its queried labels cannot recover different source answers from it.

## C-62 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Opposite labels need dual-mass separation for output-only decoding

For high tables $f,g$, define the difference set $P(f,g)=\{x:f(x)\ne g(x)\}$ and let $p_*=(\gamma-\alpha)/(1-\alpha)$ from C-61. If
$$
\nu_f(P(f,g))<p_* ,
$$
then $f$ and $g$ have a common valid list of at most $t$ addresses with identical labels: apply C-61's conditioned sample to $f$ outside $P(f,g)$. By symmetry, if either $\nu_f(P(f,g))<p_*$ or $\nu_g(P(f,g))<p_*$, their valid labeled-list sets intersect.

Therefore, in a reduction whose decoder sees only the labeled anti-checker output and must return different source answers for tables $f_x,f_y$, both directed separations must hold:
$$
\nu_{f_x}(P(f_x,f_y))\ge p_*,\qquad
\nu_{f_y}(P(f_x,f_y))\ge p_*.
$$

**Proof.** Let $P=P(f,g)$. Under $\nu_f$, the error set of each size-$s_1$ circuit has mass at least $\gamma$. If $\nu_f(P)<p_*$, the C-61 sampling calculation gives a list $Q$ of at most $t$ points outside $P$ hitting every $E_D(f)$. It is valid for $f$; because $f=g$ on $Q$, it has the same trace and is valid for $g$. A decoder receiving only this shared labeled output cannot return two different answers. The symmetric argument gives the second necessary inequality.

**Scope / status.** This is a necessary condition only for output-only decoding from the selector's labeled list. Standard search reductions may let the decoder also use source input $x$; in that model the lemma alone does not force equal decoded answers, and the decoder's circuit exponent must be included in the reduction audit C-60. PROVED as a corollary of C-61; not a P-vs-NP lower bound.

## C-63 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Exact agreement-fiber form of selector failure

Fix a table length N, a low class \(\mathcal C_1=SIZE(s_1)\), a high threshold \(s_2\), a query budget t, and a selector circuit S whose output is a list of at most t addresses. For each \(D\in\mathcal C_1\), define
\[
A_D^S=\{f\in\{0,1\}^N: \forall a\in S(f),\ f(a)=D(a)\}.
\]
Then S is valid on every table with circuit complexity greater than \(s_2\) if and only if \(A_D^S\subseteq SIZE(s_2)\) for every \(D\in\mathcal C_1\).

**Proof.** If S is valid on every high f, no high f can agree with any low D on all addresses in S(f); hence every \(A_D^S\) contains only tables of complexity at most \(s_2\). Conversely, if every such fiber is contained in \(SIZE(s_2)\), then for any high f and any low D, f cannot agree with D on all of S(f). Thus S(f) is a valid anti-checker list.

For fixed D, membership in \(A_D^S\) is computable by a circuit of size \(O(|S|+t(N+s_1+n))\): compute the addresses, multiplex each selected input-table bit, evaluate D at each address, compare, and AND the comparisons. At OPS parameters the generic evaluation overhead is \(O(tN)=O(N^{1+10\beta})\).

**Quantifier target (S-1).** To refute every candidate selector S, it suffices and is necessary to find some low D and some \(f\in A_D^S\) with \(CC(f)>s_2\). Equivalently, every candidate S must have at least one agreement fiber not supported inside the high-threshold low class.

**Generality stress test.** This claim is an exact reformulation, not a lower bound. For the concept class \(\{0^N,1^N\}\), a priority selector querying a zero and a one on every nonconstant table is valid, and its two agreement fibers are the two constants. Thus no class-independent anti-concentration theorem for agreement fibers is true. The circuit-size class must supply the missing structure.

**Status.** PROVED equivalence and circuit-size upper bound for the fiber predicate; OPEN whether any such fiber must contain a high table for every near-linear S at OPS parameters. It is not claimed as a P-vs-NP result or a new lower bound.
## C-64 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â A fixed adversarial circuit cannot force selector cost

Let D be one fixed table. The map S_D(f) that outputs the first address x with f(x)\ne D(x), whenever one exists, is computable by an O(N)-gate circuit: hardwire D's N truth-table bits, compare them with f, and use a priority tree to return the first differing address. For any f\ne D, this one query certifies disagreement with D.

More generally, for a fixed menu \(D_1,\ldots,D_m\), output one first-difference address for each D_j. This is an O(mN)-gate circuit and a list of m queries. Every table that differs from all menu members is anti-checked against the entire menu.

**Consequence.** An adversarial-completion proof cannot fix one low circuit, or a sufficiently small preselected menu, and infer an \(N^{1+\delta}\) lower bound from that alone. It must handle the full table-dependent family \(SIZE(s_1)\) simultaneously. This is a quantifier/architecture obstruction, not a selector upper bound for the circuit class.

**Status.** PROVED by direct priority encoding. It explains why the adversary D in C-63 must be chosen jointly with f after seeing the candidate S; no fixed-D argument is enough.
## C-65 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Exact beta quantifier for the selector route

For each arity n, let \(N=2^n\), \(s_1=2^{\beta n}/(cn)\), \(s_2=2^{\beta n}\), and \(t_n=2^{10\beta n}\), where c is the fixed OPS constant. Suppose there are constants \(\delta,\beta_0>0\) such that for every fixed \(0<\beta<\beta_0\) with \(\beta<1/10\), every selector family valid at all sufficiently large arities and with output budget \(t_n\) has size greater than \(N^{1+\delta}\) infinitely often. Then \(NP\not\subseteq P/poly\).

Here validity means: for all sufficiently large n, all f with \(CC(f)>s_2\), and all circuits D with \(CC(D)\le s_1\), there exists x in S_n(f) such that D(x) differs from f(x); also \(|S_n(f)|\le t_n\). This is exactly \(\forall f\,\forall D\,\exists x\).

**Proof.** Assume \(NP\subseteq P/poly\). By OPS Lemma 4.1, there is a constant \(k\) such that for every sufficiently small fixed \(\beta>0\) the anti-checker selector has size at most \(2^{n+k\beta n}=N^{1+k\beta}\) for every sufficiently large arity n. Choose a fixed \(\beta<\min(\beta_0,1/10,\delta/(2(k+1)))\), also below the OPS smallness threshold. Then the selector size is at most \(N^{1+\delta/2}\) for all large n, contradicting the assumed infinitely-often lower bound \(>N^{1+\delta}\). Since \(P\subseteq P/poly\), this also implies \(P\ne NP\).

**Quantifier warning.** A lower bound for only one fixed beta chosen before the unknown constant k is not sufficient by this argument. The robust interval of beta values lets the proof choose beta after k. No arithmetic-progression robustness is needed for this direct OPS contradiction: the conditional selector exists at every sufficiently large arity, so a lower bound on any infinite subsequence suffices.

**Status.** PROVED implication from the stated selector theorem and the published OPS anti-checker lemma. The selector lower-bound premise remains OPEN and is itself a major circuit lower bound.
## C-66 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Short-list selector lower bounds also suffice

Let \(C_0\) be a fixed constant large enough for C-48, and set \(K_n=\lceil C_0s_1\log_2(s_1+n+2)\rceil\), with the OPS parameters \(s_1=2^{\beta n}/(cn)\), \(s_2=2^{\beta n}\), and \(N=2^n\). Suppose there are \(\delta,\beta_0>0\) such that for every sufficiently small fixed \(\beta\in(0,\beta_0)\), every selector family valid for all sufficiently large arities and outputting at most \(K_n\) addresses has circuit size greater than \(N^{1+\delta}\) infinitely often. Then \(NP\not\subseteq P/poly\).

**Proof.** Assume \(NP\subseteq P/poly\). C-48 gives, for every sufficiently small fixed beta, a valid selector with list length at most \(K_n\) and circuit size \(N^{1+\kappa\beta}\) for some constant \(\kappa\) fixed by the assumed polynomial-circuit exponent. Choose beta in the lower-bound interval with \(\beta<\delta/(2(\kappa+1))\). The conditional selector then has size at most \(N^{1+\delta/2}\) for all large n, contradicting the assumed infinitely-often lower bound. Hence \(NP\not\subseteq P/poly\), and therefore \(P\ne NP\).

**Why this is a narrower target.** The published OPS budget is \(2^{10\beta n}\), while C-48's conditional construction needs only \(O(s_1\log(s_1+n))=N^{\beta+o(1)}\) queries. A lower bound for this shorter-output subclass is sufficient for separation and may be easier to attack. C-49 also gives every such trace relative distance \(\Omega(1/n^2)\) from size-\(s_1/2\) circuit traces. Neither advantage is yet a circuit-size lower bound. Also choose C0 large enough that alpha=ln(M1)/K_n<1/15; C-61 then still forces each region mandatory for every K_n-list to have dual mass greater than 1/4, so at most three pairwise-disjoint mandatory regions remain possible.

**Status.** PROVED conditional implication from C-48; OPEN short-list selector lower-bound premise. This is a distinct sufficient route from O-1 and is strictly more targeted than S-1's full OPS output budget.

## C-67 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Exact cyclic closure recurrence for a pair list

**Statement.** Let \(Q=((E_i,H_i))_{i=1}^q\), \(T_i=E_i\cap H_i\), and let \(L_{w,k}\) be the nonempty matching literal slices for anchor \(w\). Define \(a_i(w)=1\) iff some \(L_{w,k}\subseteq E_i\), \(b_i(w)=1\) iff some \(L_{w,k}\subseteq H_i\), \(P_i=\{j:T_j\subseteq E_i\}\), and \(R_i=\{j:T_j\subseteq H_i\}\). The least closure under the pair rules is represented exactly by the least fixed point from zero of
\[
x_i^{(t+1)}=
\left(a_i(w)\lor\bigvee_{j\in P_i}x_j^{(t)}\right)
\land
\left(b_i(w)\lor\bigvee_{j\in R_i}x_j^{(t)}\right).
\]
The closure contains \(\varnothing\) iff some active rule has \(T_i=\varnothing\); otherwise that closure is a proper semi-filter above \(w\), preserved by every pair in \(Q\).

**Status.** PROJECT-PROVED; the proof is in [the fusion closure-game report](FUSION_CLOSURE_GAME_2026-09-26.md). This is an exact representation, not a superlinear lower bound.

**Convergence.** The update is monotone on \(q\) bits. Starting at zero, there are at most \(q\) strict rounds, since each strict round activates at least one previously inactive rule.

**Scope.** The result assumes every matching literal slice is nonempty, as holds for the dense Gap-MCSP high side at the stated parameter range. The pair endpoints remain arbitrary semantic subsets; no description cost is assumed.

## C-68 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Clause form of the initial anchor predicates

For an endpoint \(E\subseteq U\), put \(S(E)=\{(k,b):U\cap\{z:z_k=b\}\subseteq E\}\). The endpoint's initial activation predicate is exactly
\[
a_E(w)=\bigvee_{(k,b)\in S(E)}[w_k=b].
\]
If \(E\ne U\), \(S(E)\) contains at most one polarity of each coordinate, since the two literal slices at a coordinate partition \(U\). Thus a q-pair closure system has 2q clause-valued anchor inputs and a fixed semantic containment network. This structural reduction does not bound the network or separate the promise.

**Status.** PROJECT-PROVED by direct set inclusion; see C-67 and the closure-game report.

## C-69 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â State-aware remaining distance is one-pair-Lipschitz

For partial list \(Q\), define \(\delta_Q(w)=\min\{|R|:\mathcal C_{Q\cup R}(w)\ni\varnothing\}\). For a surviving anchor, \(0\le\delta_Q(w)\le N-1\), using the chain intersection of its N matching slices. If p is one additional pair, then
\[
0\le \delta_Q(w)-\delta_{Q\cup\{p\}}(w)\le1.
\]
Monotonicity proves the left inequality. For the right inequality, any extension R that kills after \(Q\cup\{p\}\) can be replayed after Q by adding p first, so \(\delta_Q(w)\le1+\delta_{Q\cup\{p\}}(w)\).

**Status.** PROJECT-PROVED. The missing step is a useful bound on the marginal decrease aggregated over anchors; C-09 rules out a naive per-rule anchor-incidence bound.

At \(Q=\varnothing\), C-03 gives \(\delta_{\varnothing}(w)\ge N-\log_2M_2-1=N-o(N)\) for every low anchor. A fixed distribution \(\mu\) with uniformly tiny one-pair expected decrease would have yielded a superlinear lower bound by telescoping, but C-73 refutes that condition already at \(Q=\varnothing\). The distance remains valid; the additive static-potential strategy is closed.

## C-70 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Fixed-family fractional rounding is conditional, not global

Suppose a specified family \(\mathcal H\) of R semi-filters has fractional pair-cover weights of total W, with violation weight at least 1 for every \(F\in\mathcal H\). Sampling \(k=\lceil W(\ln R+1)\rceil\) independent pairs from the normalized weights covers every member of \(\mathcal H\) with positive probability by a union bound; hence an integral cover of size \(O(W\log(R+1))\) exists. If the project ceiling \(W\le8N+1\) applies to that fractional cover, this gives \(O(N\log(R+1))\).

**Status.** PROJECT-PROVED conditional rounding. The \(8N+1\) fractional ceiling is supplied by the prior project record, but its original proof location is not yet pinned in this ledger.

**Scope warning.** This only covers the specified \(\mathcal H\). The global cover problem quantifies over every semi-filter extension of every anchor. A pair that changes a current least closure may merely add a nonempty consequence; it need not derive empty. Therefore a fixed family or one selected filter per anchor does not establish a global \(\rho\) upper bound.

## C-71 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Finite-state recurrence cross-check

**Test.** On \(U=\{1,\ldots,6\}\subset\{0,1\}^3\), with anchors \(000\) and \(111\), the script experiment_fusion_closure_recurrence.py compares the explicit family-of-subsets closure to recurrence C-67 for all 2,080 one-rule pairs and 100,000 seeded two-rule lists at both anchors. It checks no empty-consequence rule activates from literal seeds alone and that the known two-pair list derives empty for both anchors.

**Result.** All 204,160 explicit-closure/fixed-point comparisons passed; every run stabilized within q strict rounds. In addition, for both anchors a selected two-literal intersection saves one rule in the local certificate, matching C-73's sharing mechanism.

**Status and scope.** TESTED finite model only. This is an implementation cross-check of C-67, not evidence for an asymptotic lower or upper bound.

## C-72 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Empty consequences need a nonempty bootstrap

Assume \(U\) contains a high-complexity table in every two-coordinate cylinder. For any empty-consequence rule \(T_i=E_i\cap H_i=\varnothing\) and low anchor w, its two initial seed predicates cannot both hold. If \(L_{w,k}\subseteq E_i\) and \(L_{w,\ell}\subseteq H_i\) with \(k\ne\ell\), two-wise shattering gives a table in their intersection, contradicting \(E_i\cap H_i=\varnothing\). If \(k=\ell\), the matching slice itself would be a nonempty subset of both endpoints. Therefore no empty rule activates in the first round from literal slices alone.

At OPS parameters the shattering hypothesis follows from \(M_2<2^{N-2}\): each two-coordinate cylinder has \(2^{N-2}\) truth tables, while only \(M_2=2^{o(N)}\) tables have circuit complexity at most \(s_2=N^\beta\), for fixed \(\beta<1\) and large n.

**Depth consequence.** A round-t contradiction proof unfolds to a binary AND/OR tree with at most \(2^t\) matching-literal leaves. Their intersection must be empty in U, so at least \(N-\log_2M_2\) distinct coordinates are fixed. Hence \(t\ge\log_2(N-\log_2M_2)=\log_2N-o(\log N)\).

**Status and scope.** PROJECT-PROVED under the stated two-wise-shattering/counting condition. This is a proof-depth lower bound, not a superlinear pair-count bound; a proof may have logarithmic depth and \(N-o(N)\) total rules.

## C-73 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â No static anchor weighting makes the first shared pair negligible

Let \(\mu\) be any probability distribution on low anchors. For each w choose one minimum literal-slice certificate \(S_w\) whose intersection in U is empty, with \(d(w)=|S_w|\). By the high-side counting bound, \(d(w)\ge d_0:=\lceil N-\log_2M_2\rceil=N-o(N)\), and by the exact one-anchor theorem \(\delta_\varnothing(w)=d(w)-1\). Write \(G_{k,b}=U\cap\{z:z_k=b\}\).

Average over the \(\binom N2\) coordinate pairs. The mean \(\mu\)-mass of anchors with \(\{k,\ell\}\subseteq S_w\) is
\[
\theta:=\frac{\binom{d_0}{2}}{\binom N2}=1-o(1).
\]
So some pair \(\{k,\ell\}\) belongs to \(S_w\) on mass at least \(\theta\). Partition this mass into its four \((w_k,w_\ell)\) patterns; one pattern \((b,c)\) has mass at least \(\theta/4\). The semantic pair \(p=(G_{k,b},G_{\ell,c})\) precomputes the intersection of those two certificate slices. For every anchor in that class, the remaining \(d(w)-2\) slices can be intersected using \(d(w)-2\) further pairs, giving \(\delta_{\{p\}}(w)\le d(w)-2\). C-69's one-pair Lipschitz bound makes the decrease exactly one.

Therefore, for every \(\mu\),
\[
\sup_p\mathbb E_{w\sim\mu}\!\left[\delta_\varnothing(w)-\delta_{\{p\}}(w)\right]\ge\theta/4=1/4-o(1).
\]
No static distribution can satisfy the proposed \(N^{-\epsilon}\) marginal bound, even at the empty partial list.

**Status.** PROJECT-PROVED, conditional only on the recorded exact one-anchor certificate theorem and high-side counting bound. This refutes an additive weighted-distance proof strategy; it does not refute \(\delta_Q\), rule out adaptive potentials, or supply a global cover.

## C-74 - Pair lists induce dual-rail least-fixed-point separators

For each rule i define X_i^(t)={w:x_i^(t)(w)=1}, and let A_i,B_i be the anchor sets satisfying its two literal seed predicates. C-67 is exactly

    X_i^(t+1)=(A_i union union_{j:T_j subset E_i} X_j^(t))
              intersect (B_i union union_{j:T_j subset H_i} X_j^(t)).

The set K_Q of anchors on which Q derives an empty consequence is the union of X_i^(q) over empty-consequence rules. For every z in U, every active T_i contains z by induction, so K_Q is disjoint from U. Consequently, a pair list refuting all low anchors Y yields a separator Y subseteq K_Q subseteq {0,1}^N minus U. Each A_i and B_i is a union of signed coordinate half-cubes; the system is monotone in the 2N dual-rail indicators, evaluated only on valid one-hot rail assignments.

Unrolling the least fixed point for at most q rounds gives an ordinary unbounded-fan-in AND/OR circuit with at most q^2 AND gates and 2q^2+O(q) OR gates. This is a necessary representation and a potentially useful interface to conjunctive/monotone circuit complexity. It is not an equivalence: arbitrary such circuits need not be realizable by semantic endpoints, and converting to bounded fan-in incurs an additional factor up to O(N+q).

**Status.** Project-proved from C-67 and the invariant that every active consequence contains each high-side table z. It reframes O-2 as a lower bound for a promise separator in a recursive dual-rail intersection program; no lower bound for this program is known. Related monotone conjunctive-complexity literature is only an analogy because it lacks the dual rails, recursive least-fixed-point semantics, and this promise.

## C-75 - A direct Karchmer-Wigderson path collapses to communication complexity

Fix a pair list Q, a low anchor w on which Q activates an empty rule, and a high table z in U. Every empty-consequence state is inactive at z. Starting from an empty rule active at w and inactive at z, Bob can choose one of its two sides whose support disjunction is false at z. Alice chooses a literal or prior-state witness making that same side true at w. If the witness is a literal, it matches w and not z, giving a differing truth-table coordinate. If it is a prior state j, then j is active at w and inactive at z; its first activation round at w is strictly earlier, so the protocol descends and terminates after at most q rules. Each round communicates one side bit and a support label, for total communication O(q log(N+q)).

This is a valid deterministic protocol for the relation that, on (w,z) in Y x U, outputs a coordinate where w and z differ. It does not imply the target lower bound: Alice can send a size-s1 circuit description for w, after which Bob scans z for a mismatch, so this relation has communication cost O(s1 log s1 + log N)=N^(beta+o(1)). The resulting q lower bound is weaker than the already known one-anchor q >= N-o(N), let alone superlinear.

**Status.** PROJECT-PROVED protocol simulation; route closed as a source of the needed superlinear bound. A useful future variant would need a richer relation or a measure that charges the number of protocol states/DAG reuse rather than communication bits.

## C-76 - Seed monotonicity yields a CNF trap for every accepting anchor

Let C_1,...,C_(2q) be the literal-clause seed predicates a_i,b_i, and let sigma(w) be their truth vector. For a seed vector s, run C-67's recurrence with the seed values fixed; let h_Q(s)=1 iff an empty consequence activates. The update is monotone in every seed bit, so h_Q is monotone on {0,1}^(2q). If Q refutes every low anchor and preserves every high table z in U, then h_Q(sigma(w))=1 for w in Y and h_Q(sigma(z))=0 for z in U. Therefore sigma(w) is not coordinatewise below sigma(z): every low/high pair has some seed clause true on w and false on z.

For fixed low w, let J(w) be the nonconstant seed clauses true on w and form Phi_w = AND_(j in J(w)) C_j. Every satisfying table z of Phi_w has sigma(w) <= sigma(z), since constant-true seeds are true everywhere. Monotonicity would then give h_Q(sigma(z))=1, so z cannot be high. Thus Phi_w has at most M_2 satisfying truth tables.

A satisfiable CNF with m clauses on N variables has at least 2^(N-m) satisfying assignments: choose one literal made true by w in each clause, fix those at most m variables to w, and leave the rest free. Hence |J(w)| >= N-log_2 M_2=N-o(N). More sharply, the hypergraph whose edges are the coordinates of literals in each true clause that match w has transversal number at least N-log_2 M_2: any smaller hitting set would leave a high table in the cylinder fixing the hit coordinates, while preserving every true seed clause.

**Limit.** This only implies 2q>=N-o(N), weaker than the existing local pair-count bound q>=N-o(N). The clause dictionary alone cannot prove a superlinear bound: an abstract dictionary containing both one-literal polarities for every coordinate gives each table its full minterm. The unresolved part is the shared monotone decoder h_Q and its realizability by q semantic pair states.

**Status.** PROJECT-PROVED as a necessary condition for any successful list. It sharpens the target to a shared family of seed clauses plus a monotone state decoder, but does not improve the asymptotic pair-count lower bound.


### C-77 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Exact cyclic-complexity identity and DAG conversion audit

For the distinct full-domain exact low-set cover, a successful q-pair list induces a monotone least-fixed-point network on signed truth-table literals with q AND/intersection states and output exactly 1_Y; every non-low table has a principal semi-filter preserving every pair. CavalarÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œOliveira give \(\rho_{\rm full}=D^\circ_\cap(Y\mid\mathcal B_{\rm full})\) and \(D_\cap\le(D^\circ_\cap)^2\). The active project target is instead the promise-domain \(\rho_{\rm prom}\) on \(Y\sqcup Z\), whose output is 1 on Y and 0 on Z with medium values unconstrained; C-90 gives the exact ambient distinction and \(\rho_{\rm prom}\le\rho_{\rm full}\). For either chosen domain, q pairs imply at most qÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â² acyclic AND gates, and the generic binary rect-DAG conversion costs O(qÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³). Sourced model comparison and proofs: [DAG/Fusion bridge audit](DAG_FUSION_BRIDGE_2026-09-26.md), [CavalarÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œOliveira](https://arxiv.org/abs/2503.14117), [Sokolov](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download), [GargÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œGÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶sÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œKamathÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSokolov](https://jakobnordstrom.se/docs/publications/GGKS18_MonotoneCircuitLBsResolution.pdf). Status: proved reformulation and conversion bounds; target lower bound open.

## C-78 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Formal C-75 relation and shared-DAG conversions

The ordinary mismatch relation has inputs (w\in Y,z\in Z), Alice knows (w) (or a circuit description (d) with (G(d)=w)), Bob knows (z), and the output is ((k,b)) with (w_k=b\ne z_k). It is total. Sending a size-(s_1) circuit description gives deterministic communication (O(s_1\log(n+s_1)+\log N)) bits, but only the generic (2^{O(c)}) protocol-tree/rect-DAG size from a (c)-bit protocol.

For a successful pair list (Q), the stronger witness relation outputs a ranked sequence of rule-side supports ending at a signed mismatch. It is total exactly when (Q) activates an empty consequence on every low anchor; direct routing uses (O(q\log(q+N))) bits. Standard Sokolov Boolean games and GGKS rectangle-DAGs are acyclic, binary-cover models. The fusion state graph can contain cycles; activation rank is input-dependent. Explicit rank unrolling yields a standard rect-DAG of size (O(q^2(q+N))=O(q^3)), while the acyclic AND-only conversion is at most (q^2). A Tier-1 target (q>N^{1+\epsilon}) would therefore require rect-DAG size (>N^{3+3\epsilon}), or an AND-only separator bound (>N^{2+2\epsilon}).

A pattern-sharing universal mismatch DAG was constructed with size (O(m+\sum_{I\ dyadic}\pi_I(Y))), where (m=|Y|) and (pi_I(Y)) counts distinct low-table restrictions to interval (I). This is an upper bound for one protocol, not a lower bound or near-linear construction at the OPS parameters. Parity and counting-selected hard Boolean functions separately show that communication bits can be small relative to DAG size, while a node-count tree can never be smaller than its DAG.

**Status.** Model comparison and the stated conversions are proved; no non-shareability lower bound is established. Detailed construction and literature scope: [DAG/Fusion bridge audit](DAG_FUSION_BRIDGE_2026-09-26.md), section 9.

## C-79 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Medium-band filter defeats direct promised-cover reuse

For sufficiently small fixed OPS ÃƒÆ’Ã…Â½Ãƒâ€šÃ‚Â², every signed truth-table coordinate cylinder contains a function of circuit complexity in ((s_1,s_2]). Proof: choose (k) with (2^k\in[s_2/32,s_2/16]); a shared prefix decoder plus an OR of selected minterms computes all (2^{2^k}) functions of (k) variables in at most (s_2) gates. For either prescribed output bit at any input, half of these functions lie in that cylinder. Their count exceeds the standard upper bound (2^{C_0s_1\log(n+s_1+2)}=2^{(C_0\beta/c+o(1))s_2}) on low tables when ÃƒÆ’Ã…Â½Ãƒâ€šÃ‚Â² is sufficiently small.

Let (M=\mathrm{SIZE}(s_2)\setminus\mathrm{SIZE}(s_1)), (Z=\mathrm{SIZE}(s_2)^c), and (U_Y=M\cup Z). For any (w\in Y), the upward closure over (U_Y) generated by (M) and all matching literal slices (L_{k,w_k}\cap U_Y) is a semi-filter above (w). Each such slice intersects (M). Therefore no endpoint (E\subseteq Z) contains a generator, so (E\notin\mathcal F_w); every pair with both endpoints in (Z) is preserved vacuously. Thus no pair list whose endpoints all live in (Z), including a cover designed for the larger positive class \(\mathrm{SIZE}(s_2)\), can be reused directly as a cover for (Y).

**Scope.** This blocks direct endpoint reuse and a naive monotonicity argument for the promise-to-exact reverse transformation. It does not exclude a transformation that adds medium-band pairs, and it gives no new asymptotic lower bound for ÃƒÆ’Ã‚ÂÃƒâ€šÃ‚Â. Full proof: [DAG/Fusion bridge audit](DAG_FUSION_BRIDGE_2026-09-26.md), section 10.

## C-80 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â A large structured low subfamily has a linear-size mismatch DAG

Choose (k) with (m=2^kin[s_1/16,s_1/8]), and let (Y_ksubseteq Y) be the (2^m) truth tables constant on blocks indexed by the first (k) input bits. Shared decoding of all (k)-bit minterms gives each such table a circuit of size at most (3m+O(1)<s_1).

For any high table (zin Z), some block must contain both output values; otherwise (z) is itself a (k)-junta and has size at most (s_1<s_2). Bob can find a mixed block with (O(m)) interval states. After Alice's row is partitioned by its constant bit on that block, Bob finds a coordinate of the opposite bit with (O(N/m)) states for each block/sign. The resulting rect-DAG for (mathrm{Mis}_{Y_k,Z}) has (O(m+m(N/m))=O(N)) nodes.

**Status.** PROJECT-PROVED construction. It falsifies lower-bound arguments based only on the size of a low subfamily or per-anchor isolation. It is not a DAG for all (Y	imes Z); the unresolved issue is sharing across incompatible circuit-induced partitions. Full construction: [DAG/Fusion bridge audit](DAG_FUSION_BRIDGE_2026-09-26.md), section 11.



## C-81 - Row-signature diameter for rect-DAGs

For a rect-DAG with S vertices and rectangles A_v x B_v, let sigma(w) record membership in every A_v. If two low rows share a signature and differ on D, then 2^|D| <= M2=|SIZE(s2)|. Otherwise a completion of their common restriction is high; the two pairs have identical feasible vertices but no shared valid signed-mismatch output. Thus each signature class has diameter at most log2 M2 = N^(beta+o(1)).

The C-80 block code yields S >= log2|C| = Theta(s1), not S >= |C|. Any row-signature-only proof is capped by log2|Y|=N^(beta+o(1))=o(N).

**Status.** Proved structural condition; quantitative consequence insufficient. See DAG/Fusion bridge audit, sections 12-13.

## C-82 - Dual column-signature certificate

If high columns z,z' share a signature, their common restriction on A={k:z_k=z'_k} has no low completion. Otherwise a low row matching it would give identical feasible vertices and no output valid for both columns. Minterm interpolation gives a low completion for every pattern on at most s1/(C n) coordinates, for a suitable absolute circuit-basis constant C. Thus equal-signature columns must agree on more coordinates.

**Status.** Exact dual condition; no column packing bound or Tier-1/Tier-2 lower bound follows.

## C-83 - q fusion states form an input-ranked cyclic game

A successful q-pair list induces q rule states. Bob selects a side false at z; Alice chooses a matching literal support or an active predecessor at w. Each predecessor transition decreases the low input's first-activation rank, so every play terminates in at most q steps. The static graph may cycle and has at most 2q^2+2qN support arcs.

This is the exact cyclic-intersection model D^circ_cap=rho, not a standard acyclic rect-DAG. The known safe acyclic conversion remains O(q^3) vertices and q^2 AND gates.

**Status.** Exact semantics identified; no near-lossless acyclic conversion or new lower bound.


## C-84 - A row-signature class lies in a high-free cylinder

Let R be a row-signature class and K_R the coordinates on which every row in R agrees, with common pattern p_R. For each high z, all pairs (w,z), w in R, have identical feasible DAG vertices and identical feasible leaves. Any reachable leaf is therefore valid for every row in R, so its mismatch coordinate lies in K_R and disagrees with z. Hence the cylinder fixing p_R on K_R contains no high table. Counting completions gives |K_R| >= N-log|SIZE(s2)| = N-N^(beta+o(1)).

If C_cyl(Y,Z) is the minimum number of high-free coordinate cylinders covering Y, any S-vertex rect-DAG gives C_cyl(Y,Z) <= 2^S, hence S >= log C_cyl(Y,Z).

**Limit.** Singleton cylinders show log C_cyl <= log|Y|=o(N); cylinders can contain medium tables. This improves the structural description of a state class but not the quantitative lower bound or fusion transfer.


## C-85 - Cross-signature classes share one separating output coordinate

Partition Y by row signatures and Z by column signatures. For any nonempty class pair R,C, all pairs in R x C have identical feasible DAG vertices and leaves. A common reachable leaf is valid for every pair, so there is a coordinate k fixed on all rows of R and all columns of C, with opposite common values. Equivalently, the common-coordinate cores K_R and K_C intersect at a coordinate with opposite labels.

**Status.** Proved structural class-pair constraint. No lower bound on class count or routing cost has been obtained; counting only row classes is capped by log|Y|=o(N), and coordinate leaves give a 2N rectangle cover.

Counting column classes alone is capped by log|Z|<=N, and counting class pairs by log(|Y||Z|)<=N+o(N). All signature-counting routes remain below the N^(3+3epsilon) scale required after the current cubic q-to-DAG conversion; the open quantity is routing cost.


## C-86 - The universal coordinate scan cannot merge histories for free

A proposed scan DAG that uses a full Y x Z rectangle as the state after coordinate i is valid for pairs whose mismatch occurred earlier. Every valid vertex in the Sokolov Boolean game must itself have a valid path to a correct output leaf, so a suffix-only scan fails for those pairs. Restricting the state to pairs equal on the scanned prefix gives a union of prefix-pattern rectangles, not one rectangle; preserving correctness requires retaining the pattern state.

**Status.** Kills the specific O(N) scan-and-merge construction, not all possible small DAGs. Source: Sokolov, Definition 2.1 and Remark 2.1.


## C-87 - Linear sketches need N-o(N) rank

For a linear map on N truth-table coordinates with rank r, every fiber has size 2^(N-r). If r < N-log|SIZE(s2)|, every fiber contains a high table, so each low w has a high z with the same sketch. Thus fixed coordinate samples and linear fingerprints with fewer than N-N^(beta+o(1)) bits cannot separate all low/high pairs.

**Scope.** This is a counting obstruction for equal-size linear fibers. It does not rule out nonlinear separators; the low-set indicator is itself a hard nonlinear separator.

## C-88 - Description-space interval profiles

On circuit descriptions d, mismatch relation MisDesc(d,z) is total and Alice sending d yields O(ell+log N) communication for ell=O(s1 log(n+s1))=N^(beta+o(1)). The interval-profile construction has rectangles {d:G(d)|I=u} x {z:z|I!=u}, with pi_I(D)<=min(2^|I|,2^ell). The mixed predicate "a mismatch occurs in I" is not generally a rectangle, so this construction still retains restriction profiles.

**Status.** No near-linear universal DAG or lower bound for every description-space DAG has been established.


## C-89 - Promise rect-DAG complexity equals separator-circuit complexity

Let SepCirc(Y,Z) be the minimum Boolean circuit size of h with h=1 on Y and h=0 on Z. A rect-DAG of size L for signed mismatch yields an O(L)-size h: put the signed input literal at each output leaf; at an internal node combine child circuits with AND or OR according to which side of the parent rectangle is contained in both child sides, or reuse a child when the parent rectangle is contained in it. Conversely, a separator circuit gives a Karchmer-Wigderson DAG for its full 1/0 sets, which restricts to Y x Z. Hence rectdag(Mis_Y,Z)=Theta(SepCirc(Y,Z)) up to basis constants.

A q-pair fusion cover gives SepCirc(Y,Z)=O(q^3). With a fixed exponent margin, SepCirc>N^(3+3epsilon+delta) implies q>N^(1+epsilon), then P!=NP by OPS.

**Limit.** The separator may accept the medium band, so it does not directly yield the distinct full-domain exact cover. It does yield the active promise cover with O(L) pairs by C-90. C-79 blocks direct endpoint reuse for the promise-to-full upgrade, not the DAG/circuit equivalence.

## C-90 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Promise-domain reverse conversion and ambient-universe monotonicity

**Statement.** Distinguish \(\rho_{\rm prom}\), on \(\Gamma_{\rm prom}=Y\sqcup Z\) with filter universe Z, from \(\rho_{\rm full}\), on the entire truth-table cube with filter universe \(M\sqcup Z\). The active project target is \(\rho_{\rm prom}\). An L-vertex mismatch rect-DAG yields a promise separator circuit of size O(L), then a cover with \(\rho_{\rm prom}\le O(L)\). Also \(\rho_{\rm prom}\le\rho_{\rm full}\).

**Proof of restriction monotonicity.** Restrict each endpoint of a full cover Q to Z. If the restricted list failed, a proper semi-filter F over Z above a low anchor would preserve all restricted pairs. Lift it to \(\widetilde F=\{A\subseteq M\cup Z:A\cap Z\in F\}\). Upward closure and propriety are inherited. Every full matching literal slice lies in the lift because its Z-restriction lies in F. If E,H are in the lift, F contains \((E\cap Z)\cap(H\cap Z)=(E\cap H)\cap Z\), so the lift preserves the original pair. Contradiction. Thus a full cover restricts to a promise cover at no greater pair count.

**Quantitative relation.** With C-78/C-89, \(\rho_{\rm prom}\le\mathrm{SepCirc}(Y,Z)\asymp\mathrm{rectdag}(\mathrm{Mis}_{Y,Z})\le O(\rho_{\rm prom}^{3})\). A q lower bound directly gives the separator lower bound needed by OPS; obtaining q from a generic rect-DAG lower bound still pays the cubic loss. C-79 blocks only the direct upgrade from promise endpoints in Z to a full-domain cover; it does not obstruct DAG-to-\(\rho_{\rm prom}\).

**Status.** Project-proved elementary ambient restriction lemma and scope correction; no new asymptotic lower bound.

## C-91 - SCC-sensitive acyclicization of the fusion recurrence

**Statement.** Delete the automatic self-support incidences i in P_i^0,R_i^0, which preserve the least fixed point. In the resulting loop-free support graph, let r_C be SCC sizes and e_C=sum_{i in C}(|P_i intersect C|+|R_i intersect C|) the internal side-support incidences. The active promise separator has a fan-in-two Boolean circuit of size O(qN+q^2+sum_C(r_C e_C+r_C^2)); its internal support network uses AND/OR gates and is monotone in the signed seed-clause values. Since e_C<=2r_C^2, this implies O(q^2+q d^2) for maximum SCC size d and q>=N-o(N); sparse SCCs or d<=sqrt(q) give O(q^2).

**Proof.** For any fixed input, if state i is 0, its self-support terms contribute nothing; if it first activates, both non-self support sides are already true, so the loop-free iteration activates it in the same round and monotonicity keeps it active. Thus deleting self-support does not change the least fixed point. Topologically process the loop-free SCC condensation. Build all seed clauses and external-predecessor ORs in O(qN+q^2). Within an SCC C of size r_C, hold external predecessor signals fixed and iterate its internal activation bits from zero. The least fixed point stabilizes within r_C strict rounds. Each round uses O(e_C+r_C) fan-in-two OR gates for internal support selection and O(r_C) AND gates for state updates, giving O(r_C e_C+r_C^2) gates for C. Add the final OR over empty-consequence states and sum over components. The resulting circuit separates Y from Z on the active promise. QED.

**Status.** PROJECT-PROVED by direct recurrence analysis. It refines the generic cubic upper bound but gives no lower bound: one giant SCC remains possible, and the project has no theorem charging its size or internal sharing.

## C-92 - Transitive two-sided carrier-support pruning

**Statement.** After deleting self-supports, remove from both support sides of rule i every state j whose carrier T_j is a strict non-cover subset of T_i in the finite poset of distinct carriers. The least fixed point is unchanged for every seed assignment.

**Proof.** F'<=F. For each cover s<t, every state with carrier s remains a support on both sides of every rule with carrier t: T_j=s is contained in t=T_i and T_i is contained in both endpoints, while the cover relation is not pruned. Hence every fixed point y of F' satisfies y_j=1 implies y_i=1 along cover chains, for every strict carrier inclusion. Every deleted support term into i is therefore 0 whenever y_i=0; when y_i=1, F'_i(y)=1 implies F_i(y)=1. Thus every F'-fixed point is an F-fixed point. In particular lfp(F') is fixed by F; together with F'<=F, monotone leastness gives equality of least fixed points.

**Status.** PROJECT-PROVED recurrence reduction. It removes transitive two-sided incidences, not equal-carrier alternatives or one-sided support.

## C-93 - Equal-carrier quotient with candidate alternatives retained

**Statement.** Group rule states by their distinct carriers t=T_i. A group with one rule contributes its one seed/support conjunction; a group with at least two rules contributes one carrier bit whose update is the OR of all its candidate conjunctions, with same-carrier support removed. The least fixed point of this p-state map lifts exactly to the original q-state least fixed point.

**Proof.** At the rule-state least fixed point, a 1 in a multi-rule equal-carrier group forces every peer state to 1 because the carrier is contained in both endpoints. If the group's common value is 0, every candidate conjunction is 0. If it is 1, consider the first state in the group to activate: at that round no same-carrier support was yet active, so its own seed and other-carrier supports made its candidate conjunction true; monotonicity preserves it. Thus the carrier vector is a fixed point of the quotient. Conversely, lift the quotient least fixed point: a 0 group has all candidate conjunctions false, and a 1 multi-rule group has a peer state supporting both sides of every rule. This lift is a fixed point of the rule system. Leastness in both directions proves equality. The full proof and compiler count are in C-93 of the bridge report.

**Compiler consequence.** If C ranges over SCCs of the carrier graph, with p_C carriers, q_C candidate rules, e_C internal candidate-side carrier incidences and e_out external incidences, SCC iteration gives separator size O(qN+e_out+sum_C p_C(e_C+q_C)), hence the coarse bound O(qN+qp^2). The q alternative conjunctions remain charged; only recursive state width is quotiented.

**Status.** PROJECT-PROVED exact least-fixed-point quotient and compiler bound; no lower bound on q or P-vs-NP separation follows.

## C-94 - Feedback is carried only by one-sided escape supports

**Statement.** After C-91 self-loop removal, C-92 transitive pruning, and C-93 equal-carrier quotient, every remaining proper-inclusion support is a Hasse-cover support shared on both sides. Every other support carrier u into a rule at t is not a subset of t and can occur on at most one endpoint. Writing K_t for the OR of lower-cover carrier states and L_i,R_i for the candidate-specific one-sided escape supports, the exact quotient recurrence is H_t=K_t OR OR_{i in I_t}((a_i OR L_i) AND (b_i OR R_i)).

**Proof.** If u is a support on both endpoints, then u is contained in their intersection t. Equal carriers were quotiented; C-92 removes strict non-cover subcarriers; the remaining proper subcarriers are exactly the covers. The distributive identity (K OR A) AND (K OR B)=K OR (A AND B) factors this shared cover signal out of each candidate. Since Hasse edges strictly increase the carrier order, every directed cycle must use a one-sided escape edge u->t with u not subset t.

**Compiler.** Let Up(D) denote upward closure in the carrier poset and D_t the OR of the escape-only candidate conjunctions at t. H and G(x)=Up(D(x)) have the same fixed points: the equations x_t=D_t OR OR_{u cover t}x_u recursively characterize x=Up(D(x)). If S is the set of distinct escape-source carriers and s=|S|, iterate G from zero. After the initial round, each strict increase requires a previously inactive carrier in S to activate, since only those carrier bits are dynamic inputs to D. Thus at most s further strict rounds suffice. With xi candidate-side escape incidences, kappa Hasse edges, q rules, and p distinct carriers, this gives separator size O(qN+(s+1)(xi+kappa+q)) <= O(qN+(s+1)(q(s+1)+kappa)) <= O(qN+qp^2). When s=0 the sharper bound is O(qN+q+kappa)=O(qN+q+p^2). The full derivation is C-94 of the bridge report.

**Status.** PROJECT-PROVED normal form and event-bounded compiler. It isolates the cyclic source but proves no lower bound on escape count, q, or separator size.

## C-95 - Empty-carrier rules require an escape at activation

**Statement.** Under the active Gap-MCSP parameters \(M_2<2^{N-2}\), every empty-carrier rule has mutually unsatisfiable direct seed clauses. Consequently every low anchor that activates an empty rule must activate at least one carrier in the empty-rule escape-source set \(S_0\).

**Proof.** If both seed clauses were satisfied by any truth table, choose one true signed literal from each. Fixing at most two table bits leaves at least \(2^{N-2}\) assignments satisfying both. Since only \(M_2\) tables are non-high, one of them is high and would activate the empty-carrier rule directly, contradicting the principal-filter preservation property. Thus the seed conjunction is identically false. At a low input, an active empty rule must therefore obtain at least one missing side from a one-sided escape support. Hence \(Y\\subseteq\\bigcup_{u\\in S_0}X_u\), where \(X_u\) is the activation set of carrier u.

**Status.** PROJECT-PROVED necessary-path lemma. It gives no lower bound on \(|S_0|\); a single carrier activation set may serve many lows.

## C-96 - Terminal support cones carry linearly many true seed clauses

For each low anchor, choose an activated empty-carrier rule and one true support on each side. Let C(w) contain that rule and the full predecessor cones of each selected predecessor support. The conjunction of all nonconstant seed clauses true at w from rules in C(w) has at most M2 models: any satisfying table preserves the selected predecessor activations by monotonicity, preserves direct selected seed supports, and would therefore activate the empty carrier. A satisfiable m-clause CNF has at least 2^(N-m) models, so at least N-log2(M2) seed clauses are true in this cone. Since each rule contributes at most two clauses, |C(w)| >= (N-log2(M2))/2=(N-o(N))/2.

**Audit clarification:** only the selected predecessor cones are predecessor-closed; the unused incoming alternatives of the terminal rule need not be included. This is a local linear-cone bound, weaker than the C-03 global q>=N-o(N) floor and with no cross-anchor non-shareability consequence.

## C-97 - Circuit descriptions do not reduce standard shared-DAG size

For any surjection G:D1->Y from circuit descriptions to the low truth tables, the minimum standard Boolean communication-game / rect-DAG size for signed mismatch on D1 x Z equals that on Y x Z. Lift a game by composing Alice predicates with G; restrict a description-space game along any section Y->D1 for the reverse. This also preserves ordinary communication cost and protocol-tree size when local computation is free.

The standard rect-DAG size is Theta(SepCirc(Y,Z)), the minimum Boolean circuit size of a promise separator h=1 on Y, h=0 on Z; medium values are free. The reverse map gives rho_prom<=O(SepCirc)<=O(rho_prom^3). The strongest generic q-to-DAG bounds remain C-91/C-93/C-94 parameterized compilers and O(q^3) worst case; the cyclic q-state system is not a standard acyclic binary rect-DAG. A near-linear standard DAG would instead imply rho_prom<=N^(1+o(1)) and kill the desired superlinear cover route.

A universal circuit for G(d)(k) does not by itself construct a small DAG: interval-mismatch predicates are not rectangles, and pattern-indexed states still cost O(|Y|+sum_I pi_I(Y)). This kills the naive scan-and-merge architecture only. No superlinear DAG or cyclic-cover lower bound is proved. Full definitions, proofs, quantitative thresholds, model comparisons, and primary sources are in [the DAG/fusion bridge audit](DAG_FUSION_BRIDGE_2026-09-26.md), C-96/C-97.

## C-98 - PRFs conditionally rule out polynomial shared separators

Assume a one-bit PRF family with per-key evaluation circuit size lambda^d, secure against nonuniform polynomial-size distinguishers making polynomially many queries. Fix 0 < beta < 1, let N = 2^n, and use s1 = N^beta/(cn), s2 = N^beta. Choose a constant a with a*beta > d and lambda = Theta(N^(1/a)). Restrict the PRF domain to N padded inputs 0^(lambda-n)x. Each key table is in Y, while a uniform table is in Z with probability 1-2^(-N+o(N)), by circuit counting. Any separator h of size N^C can be evaluated after querying the full restricted domain, giving a nonuniform polynomial-size distinguisher with advantage 1-o(1). Thus SepCirc(Y,Z) > N^C for every fixed C, conditionally; so S_rect = N^(omega(1)), and S_rect <= O(rho_prom^3) implies rho_prom = N^(omega(1)).

This is a precise promise-separator application of the known MCSP/PRF paradigm, not an unconditional or claimed-novel circuit lower bound. The nonuniform-security requirement and the N=poly(lambda) query scaling are essential. Full quantifiers and proof are C-98 in the [DAG/fusion bridge report](DAG_FUSION_BRIDGE_2026-09-26.md).

## C-99 - Nonuniform PRFs already imply the target circuit separation

Assume C-98's nonuniform-secure PRF family. If NP were contained in P/poly, MCSP would have polynomial-size circuits because it is in NP: a circuit is a polynomial-size witness up to the Shannon cap, and its truth table can be checked in polynomial time in the N-bit input length. Fixing the MCSP threshold to s2=N^beta gives a polynomial-size separator: it accepts every low table of complexity at most s1<s2 and rejects every high table above s2. Since N=Theta(lambda^a), this separator is a polynomial-size, N-query nonuniform PRF distinguisher, contradicting security. Hence NP is not in P/poly.

**Learning.** The C-98 implication rho_prom=N^(omega(1)) is valid conditionally, but its PRF hypothesis already implies the desired class separation. It is a conditional model benchmark, not an independent P-vs-NP route. Uniform PRF security alone cannot address arbitrary nonuniform separator circuits without a uniformity condition on h_n.

## C-100 - Batched subset-OR compiler improves the q-to-rect-DAG bound

For \(r\) prescribed ORs of subsets of a common \(m\)-bit vector, partition inputs into blocks of \(k=\min(m,\lfloor\log_2r\rfloor)\); compute every subset OR within each block once, then assemble each requested OR from its block values. This gives a fan-in-two monotone circuit of size \(O(r(1+m/\min\{m,\log(r+1)\}))\), with the direct \(O(rm)\) bound covering small \(r\).

Applying this to the C-94 escape normal form batches the \(2q\) seed clauses over \(2N\) signed-literal indicators, the \(2q\) escape-support ORs over \(s\) source states, and the \(p\) up-closure downsets over \(p\) carrier bits. With the sparse incidence/Hasse implementations available as alternatives, the compiler becomes
\[
O\!\left(qN/\log N+(s+1)\left[q+\min\{\xi,q(1+s/\log(q+1))\}+\min\{p+\kappa,p+p^2/\log(p+1)\}\right]\right).
\]
Since \(q\ge N-o(N)\) and \(p,s\le q,\ \xi\le2qs,\ \kappa\le p^2\), its coarse worst-case bound is \(O(q^3/\log(q+1))\), versus C-94's \(O(q^3)\).

**Status and limit.** PROJECT-PROVED compiler upper bound; it does not lower-bound \(q\), construct a near-linear DAG, or establish \(P\ne NP\). It improves the generic separator-lower-bound scale only by a logarithmic factor: \(q\le N^{1+\epsilon}\) gives \(S_{\rm rect}=O(N^{3+3\epsilon}/\log N)\). Description-space invariance (C-97) means a description-aware DAG of this type is already a separator circuit on truth-table rows. Full proof and parameter cases are in C-100 of the [DAG/fusion bridge report](DAG_FUSION_BRIDGE_2026-09-26.md).

## C-101 - Terminal cones have high-free coordinate cubes, but counting stops at the old bound

A selected C-96 cone CNF with m clauses has no high-table satisfying assignments. Choosing one true literal per clause at its low anchor leaves a coordinate subcube of dimension at least N-m, all of whose tables have circuit size at most s2. Let Delta_box(s2) be the maximum dimension of a coordinate subcube contained in SIZE(s2). Then m >= N-Delta_box(s2). Counting circuits gives Delta_box(s2) <= O(s2 log(n+s2)), so the result remains m >= N-o(N), exactly the previous asymptotic scale. A localized input subcube gives Delta_box(s2) >= Omega(s2) when s2 >> n; the C-80 block-constant code is not itself a coordinate subcube because its fiber equalities correlate table coordinates.

**Status:** proved reformulation, no cross-anchor cone bound. Ordinary VC dimension is weaker than Delta_box because it does not fix the outside truth-table bits. Generic counting is the only upper bound used here; the superficially related Koiran report concerns sigmoidal circuits, not this parameter. Full derivation and boundary: C-101 in the [DAG/fusion bridge report](DAG_FUSION_BRIDGE_2026-09-26.md).

## C-102 - Fiber-disagreement is a total alternate search relation

For every low table w and high table z, there exist domain points a,b with w(a)=w(b) and z(a) != z(b). Otherwise z is constant on each of w's two fibers and hence equals one of 0, 1, w, or not-w, each of circuit size at most CC(w)+O(1), contradicting the project gap. Each fixed output pair defines a rectangle: Alice checks w(a)=w(b), Bob checks z(a)!=z(b). The O(N^2) output rectangles yield a short nondeterministic certificate, but not a deterministic routing DAG; verifying a rectangle cover does not organize failures on one side into valid binary transitions.

**Status:** exact structural lemma, Tier 5 only. No reduction from the C-75 ranked path or a shared-DAG lower bound is known. Keep it auxiliary until such a transfer is proved. See C-102 in the bridge report.

## C-103 - Small fiber-disagreement DAGs imply small mismatch DAGs

At a fiber-search leaf labeled (a,b), split its valid rectangle by Alice's shared value w(a)=w(b) and Bob's orientation (z(a),z(b)) in {(0,1),(1,0)}. Each of the at most four product rectangles has a fixed mismatch coordinate: for orientation (0,1), choose b if the shared w-bit is 0 and a if it is 1; reverse this for orientation (1,0). A constant-size binary rectangle gadget replaces each leaf. Hence S_mis <= O(S_fib), and the C-90 reverse transfer gives rho_prom <= O(S_fib).

An N^(1+o(1))-size fiber DAG would therefore kill the desired superlinear rho route. The reverse implication is not known, so a fiber-DAG lower bound alone does not prove the target. The relation remains a falsification target, not a lower-bound route.

## C-104 - Reverse mismatch-to-fiber simulation costs N squared

For the one-gate-smaller low class Y^-=SIZE(s1-1), complement stays in Y. Run mismatch games on constants 0 and 1 to get p,q with z_p=1,z_q=0. Store (p,q) in the graph copy index. If w_p=w_q, output the pair. If (w_p,w_q)=(0,1), run the mismatch game on not-w to obtain a coordinate where w=z; if (1,0), run it on w to obtain a coordinate where w!=z. In either case one of p,q pairs with the new coordinate inside the same w-fiber and across different z-bits. Indexing copies by (p,q) costs O(N^2 S_mis) vertices.

Together with C-103, this gives only an N^2-loss comparison with the fiber relation, and one direction uses Y^- instead of Y. Since a q-cover gives S_mis=O(q^3/log q), a fiber lower bound would need to exceed O(N^(5+3epsilon)/log N) to force q>N^(1+epsilon). This is worse than attacking the mismatch DAG or cyclic cover directly. No near-lossless reverse conversion is known.

## C-105 - Superlinear lower bound for universal fiber-edge labels

For a fiber-disagreement DAG on SIZE(s1-1) x Z, let E be its set of unordered pair outputs. For every affine subspace A of size a=Theta(s2 n), the indicator w=1_A is low. If E[A] has fewer than a/8 edges, then it has more than 3a/4 isolated points. There are 2^(Omega(a)) size-a/4 subsets S of those points, more than the number M2 of size-s2 circuits for a suitable constant in a. Hence one z=1_(A\S) is high. No E edge is a valid fiber witness for (w,z): across A's boundary w changes, outside A z is constant, and inside A no edge crosses S from its isolated vertices to A\S. Therefore every such A must span Omega(a) E-edges.

A uniform random affine subspace contains each fixed pair with probability a(a-1)/(N(N-1)); averaging yields |E|=Omega(N^2/a)=Omega(N^(2-beta)/n). Thus the auxiliary fiber rect-DAG has a superlinear number of vertices from its output labels alone. The same proof applies to any fixed universal output-edge list, since it uses only that every low/high pair must have at least one valid listed edge.

**Transfer audit:** C-104 loses N^2 going from mismatch to fiber, so this lower bound divided by N^2 is vacuous for mismatch/rho. This is a genuine lower bound for the auxiliary relation and a useful output-nonshareability lemma, but not P-vs-NP progress. See C-105.

## C-106 - Exact output gap between a fusion witness and a fiber witness

For each low/high pair, partition coordinates into C_ab={x:w(x)=a,z(x)=b}. A fiber witness exists iff one w-row contains both z-values. A C-75 closure path emits one signed mismatch coordinate, hence one point in C_01 or C_10; this does not identify a second point in the same row. Even one agreement output may be in the opposite row, e.g. C_01 and C_11. Therefore C-105's output-label lower bound does not transfer from the path output alone.

**Conditional implication.** If every successful q-pair cover induced a fixed universal coordinate-edge set E_Q of size O(q log^d N), with a valid fiber witness from E_Q for every low/high pair, then C-105 gives q=Omega(N^(2-beta)/(log N)^(d+1)), superlinear for each fixed beta<1. No such E_Q or implication from Q is proved. The C-75 rule states are semantic set pairs, not coordinate-edge labels, and the ranked path only returns one mismatch.

**Status.** C-105 rules out a near-linear DAG for the auxiliary fiber relation at fixed beta<1, closing its small-DAG falsification branch. This remains auxiliary because C-104 loses N^2 when reducing fiber search to mismatch. The direct q-to-universal-edge-set bridge is open; do not cite the conditional implication as a fusion lower bound.

## C-107 - Every-mismatch-valid local encodings cannot represent fiber witnesses

For a coordinate pair (a,b), Alice sees u=(w(a),w(b)) and Bob sees v=(z(a),z(b)). Valid fiber outputs are exactly A x B, where A={00,11} and B={01,10}. Both A and B have nonempty complements, and all four patterns on each side occur in the promise. If local encodings F(u),G(v) have any mismatch only on A x B, choose u0 outside A and v0 outside B. Equality on invalid pairs forces F(u0)=G(v0)=gamma, then F(u)=gamma for every u and G(v)=gamma for every v. Hence there can be no mismatch anywhere. This rules out every pointwise recoding that expects all signed mismatches of the encoded tables to be valid fiber outputs, including the naive pairwise-parity lift. A separate stateful routing protocol could still filter false candidates.

**Status.** PROVED for pointwise, independently computed local encodings. It does not rule out multi-state routing that suppresses invalid candidates before output.

It does not rule out a stateful shared DAG that routes among candidate pairs. C-106's missing q-to-fiber transfer must therefore use global state/transition information; a local lifted mismatch coordinate cannot provide it.




## C-108 - A sparse universal fiber-edge list is near label-optimal

For Y^-=SIZE(s1-1), Z={z:CC(z)>s2}, and fixed 0<beta<1, a high z differs from every unary postprocessing of any w in Y^- on more than 2r coordinates, where r=Theta(s2/n). Otherwise patching the exceptional points onto g(w) gives a circuit of size below s2. Thus in some fiber of w, z splits the points into two sets each of size at least r.

Choose a random graph on the N truth-table coordinates with edge probability p=Cn/r=Theta(n^2/s2). For each low w, each of its two fibers A, and every cut of A with both sides at least r, the number of potential crossing edges is at least r|A|/2. The probability of a missed cut, union-bounded over all cuts in A, is exp(-Omega(Cn|A|)); since |A|>=2r this is exp(-Omega(Cs2)). Circuit counting gives only exp(O(s2)) low w's, so large C ensures one graph hits every relevant cut. Its edge count is O(N^2n^2/s2)=O(N^(2-beta)n^2).

C-105 gives the lower bound Omega(N^2/(s2n)) on every universal output list. Hence the minimum fiber output-list size is pinned within O(n^3). This is a rigorous nondeterministic-cover/leaf-label result, not a deterministic-DAG upper bound. Serially testing the edge list fails because the failed-prefix residual is a union of rectangles, not one rectangle; routing histories cannot be merged into a suffix state without losing valid earlier candidates. Enumerating every low row gives only the coarse rect-DAG upper bound O(|Y^-||E|)=2^(O(s2))N^(2-beta)n^2.

**Status and limit.** Strong auxiliary output-label result; no transfer to mismatch or rho. It quantifies exactly how cheap the fiber certificates can be while leaving their deterministic sharing cost unresolved. Full proof: C-108 in the bridge report.



## C-109 - Joint fibers of logarithmically many low anchors still split every high table

For r low tables w_1,...,w_r, combine their circuits into W=(w_1,...,w_r). If z is constant on W-fibers, it factors as h(W), where h has at most 2^r input patterns. A DNF computes h with O(r2^r) gates, so CC(z)<=r s1+O(r2^r). Choose r<=eta n for a sufficiently small constant eta<beta and eta/c; then r s1+O(r2^r)<s2 for large n. Therefore each high z varies on a joint fiber: there are a,b with every w_j(a)=w_j(b) and z(a)!=z(b).

**Status and limit.** PROVED common-witness lemma. Every O(log N)-sized tuple of low rows has, for each high column, some output edge valid for all rows in the tuple. The edge may depend on z, so this is not a common fixed leaf label and gives no small DAG. It kills only the simple strategy of choosing a logarithmic-size row fooling family with no common valid output.


## C-110 - A shared rect-DAG state must solve the product hull of its histories

In a rect-DAG, every state \(v\) has a rectangle \(A_v\times B_v\), and its descendants must produce a valid output for every pair in that rectangle. If \(\Lambda(v)\) is the set of output coordinates on descendant leaves, then \(A_v|_{\Lambda(v)}\cap B_v|_{\Lambda(v)}=\varnothing\). If transcript contexts \(A_i\times B_i\) merge at v, its rectangle includes all cross-pairs \(A_i\times B_j\); the common suffix must solve those too.

Applied to equal-prefix search, merging distinct common-prefix contexts and checking only the suffix fails: the product hull contains cross-prefix pairs that can agree throughout the suffix and have no suffix mismatch. Applied to a fusion pair list, the static side-support digraph gives each active/inactive rule rectangle \(A_i\times B_i\) a descendant-output coordinate set \(\Lambda_i\) whose projections separate \(A_i\) and \(B_i\). The input-dependent first-activation rank proves every such pair reaches one of those outputs.

**Status and limit.** PROVED as a necessary state invariant and as a no-go for the prefix-forgetting universal scan. It does not establish that the requisite cross-pairs exist for arbitrary Gap-MCSP description contexts, nor does it lower-bound \(|\Lambda_i|\) or q. Existing quantitative conversions are unchanged: AND-only acyclic complexity at most q^2; safe standard rect-DAG size O(q^3); DAG-to-active-cover O(L). No superlinear \(\rho\) result follows.


## C-111 - Promise-realized cross-pairs block prefix-first suffix-only routing

Fix \(\beta<1/2\), and take the C-80 block-constant low family with \(m=\Theta(s_1)\) blocks of size \(B=N/m=\Theta(nN^{1-\beta})\). Circuit counting gives a mask p on the within-block inputs for which both p and its complement have circuit complexity \(>s_2+O(k)\), since \(2^B\) exceeds the \(2^{O(s_2 n)}\) small-circuit count. Let P be the coordinates where p=1 and J its complement. For block codewords a,b, splice \(z_{a,b}=w_b\) on P and \(w_a\) on J. If aÃƒÂ¢Ã¢â‚¬Â°Ã‚Â b, restriction to a differing block is p or its complement, so \(z_{a,b}\in Z\); while \(w_a\in Y\), \(w_a|_J=z_{a,b}|_J\), and \(z_{a,b}|_P=w_b|_P\).

Thus every pair of distinct P-pattern contexts has a low/high cross-pair that agrees throughout J. A rect-DAG suffix-only continuation cannot merge any two such contexts, because its product rectangle would contain that invalid cross-pair. A prefix-first router that records the exact P-pattern and then outputs only in J needs \(2^m=2^{\Theta(s_1)}\) continuation states.

**Status and limit.** PROVED for the specified prefix-first/suffix-only submodel, on actual Gap-MCSP low/high inputs. C-80's O(N) adaptive mixed-block DAG handles the same structured low family, so this is not a general rect-DAG lower bound. It does not improve \(\rho\), q, or the q-to-DAG conversion. It strengthens O-98 by replacing the arbitrary-string example with promise-realized cross-pairs.


## C-112 - A separated low code has a split with all cross-splices high

For \(\mathcal C\subseteq\{0,1\}^N\) of size K and minimum distance d, if \(d>2\log K+\log |\mathrm{SIZE}(s_2)|\), a uniform random coordinate subset P gives, for each ordered aÃƒÂ¢Ã¢â‚¬Â°Ã‚Â b, a uniformly random splice among \(2^{d(a,b)}\) completions of their common restriction. At most \(|\mathrm{SIZE}(s_2)|\) are low/medium. Union-bounding over fewer than K^2 pairs proves there is one split P for which every off-diagonal splice is high.

Apply this to a constant-relative-distance error-correcting subcode of the C-80 block-constant low family. It has K=2^{Omega(s1)} rows at distance d=Omega(N). Since log |SIZE(s2)|=O(N^beta n)=o(N) for every fixed beta<1, the condition holds throughout the OPS range beta<1. All distinct P-pattern contexts then have a high cross-splice matching the first row on J=[N]\\P. A prefix-first rect-DAG whose continuation outputs only in J must retain a separate state for each codeword, requiring 2^{Omega(s1)} states.

**Status and limit.** PROVED for that prefix-first/suffix-only router. C-80's adaptive mixed-block DAG still solves the structured low family in O(N) vertices, so the result is not a lower bound for arbitrary DAGs or for rho. It strengthens C-111's beta<1/2 mask construction to every beta<1 and makes the cross-splice mechanism independent of a specially hard mask.


## C-113 - The union of all k-juntas has an N polylog N mismatch rect-DAG

Let \(Y_k\) be functions on n variables with at most k essential variables, where \(C_{\rm DNF}k2^k\le s_1<s_2\). For low \(w\in Y_k\), choose a k-set \(S_w\) containing its essential variables. Every high z has more than k essential variables \(T_z\), since any function of at most k variables has size at most s1. Thus the sets \(A_w=[n]\setminus S_w\) and \(T_z\) have sizes summing to at least n+1 and intersect.

Find an intersection direction with a count-state PLS on a balanced interval tree. States \((I,a,b)\) record exact Alice/Bob set sizes inside I with a+b>|I|; these are rectangles, there are O(n^2) states, and the interval strictly shrinks. Computing child counts costs O(log n) communication per move. Sokolov's conversion gives a rect-DAG of size n^{O(1)} for outputting a common direction. For each direction i, Bob then selects one of the N/2 hypercube edges on which z changes (O(N) vertices per i). Since w ignores i, it is constant on this edge; Alice and Bob choose the endpoint where w and z differ. Total size is O(nN+n^{O(1)})=N polylog N.

**Status and limit.** PROVED upper bound for the restricted row domain Y_k times all Z; the variable support set may vary over all \(\binom nk\) possibilities. This falsifies the idea that support-partition diversity alone forces many states. It does not cover all SIZE(s1), since low circuits may depend on many variables; it yields no \(\rho\) upper bound for the full promise.

## C-114 - Generic count-intersection PLS and C-113 audit

If Alice's input specifies \(A_x\subseteq[n]\), Bob's specifies \(B_y\subseteq[n]\), and \(|A_x|+|B_y|>n\) for every pair, then the relation returning \(i\in A_x\cap B_y\) has an acyclic communication PLS with \(O(n^2)\) states and \(O(\log n)\) communication per membership/successor operation. Balanced interval states record exact local counts \((a,b)\) with \(a+b>|I|\); one child preserves the invariant, and singleton termination gives the intersection element. By Sokolov Theorem 3.1 this yields an \(n^{O(1)}\)-vertex rect-DAG.

Applied to k-juntas, take \(A_w=[n]\setminus S_w\) for a k-set containing \(\operatorname{Ess}(w)\), and \(B_z=\operatorname{Ess}(z)\). For each output direction i, all terminal rectangles sit inside the valid rectangle of low rows invariant under i times high columns essential in i. One \(O(N)\) boundary-edge selector can therefore be shared per i, yielding \(O(nN+n^{O(1)})=N\,\mathrm{polylog}(N)\) vertices. This verifies C-113's suffix-sharing step.

**Limit.** This witness cannot cover all low circuits: parity has size \(O(n)\) and all n variables essential, so its irrelevant-variable set is empty. This refutes only the support-cardinality template, not the general shared-DAG route or any lower bound on \(\rho_{\rm prom}\).

## C-115 - Gate-signature fiber variation for every low/high pair

Let \(C\) be any size-\(s_1\) circuit for w. Choose \(k=\Theta(\log s_2)=\Theta(n)\) wire values including the output (input wires may pad the selection), with \(s_1+O(k2^k)<s_2\), and partition assignments x by their k-bit signature. If z were constant on every cell, a lookup circuit composed with C would compute z in size below \(s_2\). Hence some cell contains x,y with w(x)=w(y) and z(x)\ne z(y). This gives a total, circuit-dependent fiber-disagreement witness for all low/high pairs.

More quantitatively, majority-labeling each signature cell is a circuit of size at most \(s_2/8\) for suitable k. A high z must differ from that function on \(\Omega(s_2/n)\) assignments, since each exceptional point can be patched with an n-literal minterm at O(n) gates. Thus the total minority mass, and hence the number of ordered within-cell z-disagreement pairs, is \(\Omega(s_2/n)\).

**Limit.** Let \(A_C\) be all same-signature ordered pairs and \(B_z\) all z-disagreement ordered pairs. Although \(|A_C|\ge N^2/2^k\) and \(|A_C\cap B_z|\ge\Omega(s_2/n)\), these bounds do not imply \(|A_C|+|B_z|>N^2\), so C-114's count-intersection route does not apply. This failure occurs for a constant low row with k-1 selected input wires and a high table of weight \(K s_2=o(N)\), which exists by circuit counting: both separate sets have size \(o(N^2)\). The cells depend on C. No shared-DAG lower bound or q-transfer follows. This is a structural witness theorem (Tier 5 pending a routing invariant), not a breakthrough.

## C-116 - Cofactor fragmentation gives only an upper reduction

For \(s_2=cns_1\), partition n-bit inputs into \(m=\Theta(n)\) fixed prefix cofactors, with \(m\) small enough that muxing \(m\) circuits of size \(4s_1\) costs below \(s_2\). Every z of circuit size \(>s_2\) has some cofactor \(z_u\) of size \(>4s_1\); otherwise all cofactors combine to a circuit below \(s_2\). Every low w restricts to a circuit of size at most \(s_1\). Bob can route to a heavy cofactor, so
\(S_n(s_1,s_2)\le O(m S_{n-\log m}(s_1,4s_1)+m)\).

This preserves a mismatch witness while reducing the gap to a constant factor. It is only an upper-bound reduction. A hard-marker reverse embedding creates an easy mismatch outside the encoded cofactor, so it does not transfer lower bounds. No consequence for \(\rho\) is established.

## C-117 - Exact ignored-input padding for mismatch rect-DAGs

Lifting tables on \(n-k\) input variables to ignore k additional variables preserves circuit complexity exactly. Restricting an n-variable rect-DAG to these lifted rows and columns preserves its graph and rectangle semantics; output coordinates can be projected to their suffix. Hence \(S_{n-k}(a,b)\le S_n(a,b)\) for the same absolute thresholds, with no size loss.

For OPS parameters, the same thresholds correspond to \(\beta'=\beta n/(n-k)\), \(c'=cn/(n-k)\) on \(n-k\) variables. More generally a fixed \(\beta'>\beta\) can be matched with \(n'=(\beta/\beta')n\) and \(c'=c\beta'/\beta\), giving exponent transfer \(N'^\gamma=N^{(\beta/\beta')\gamma}\). This is a DAG statement only; applying magnification or transferring to \(\rho\) requires the appropriate exponent margin and uniformity.

## C-118 - Direct \(\rho_{\rm prom}\) monotonicity under input padding

Lift \((n-k)\)-variable truth tables to n variables by ignoring k inputs. Circuit complexity is unchanged. If a big active-promise cover \(Q\) is restricted by intersecting each endpoint with the lifted smaller high class \(Z^\iota\), it still covers the smaller promise. Otherwise a smaller semi-filter \(\mathcal F'\) above a lifted low row and preserved by every restricted pair pulls back to \(\widehat{\mathcal F}=\{A\subseteq Z_n:A\cap Z^\iota\in\mathcal F'\}\). This is proper and upward closed, contains all full matching slices, and preserves every pair of Q, contradicting that Q covers the big promise. Therefore \(\rho_{\rm prom}(n-k;s_1,s_2)\le\rho_{\rm prom}(n;s_1,s_2)\), with no DAG conversion loss.

For fixed \(\beta'>\beta\), choose \(n'=(\beta/\beta')n\) and \(c'=c\beta'/\beta\) (rounding n' changes thresholds by bounded factors). A lower bound \(\rho(n')>N'^{1+\epsilon'}\) transfers as \(N^{(\beta/\beta')(1+\epsilon')}\). It reaches \(N^{1+\epsilon}\) only with sufficient exponent margin and uniformity in the shifted parameters.

## C-119 - Padding does not collapse the OPS quantifier

For a fixed rational lambda=p/q>1, compare arities n=pt, n'=qt, and set beta'=lambda beta, c'=lambda c. Then the two parameter pairs have exactly the same absolute (s1,s2), so C-118 gives rho_qt(beta',c') <= rho_pt(beta,c). A source lower bound rho_qt>(2^(qt))^(1+eta) transfers to exponent (1+eta)/lambda at the larger dimension; reaching 1+epsilon requires eta>lambda(1+epsilon)-1. For OPS constant c0, this compares source constant lambda c0 to target c0. It maps every small fixed beta' to every small target beta=beta'/lambda only if the source bound is uniform over that interval at the fixed shifted constant. One fixed beta' gives only one target beta. Since the larger source constant has a smaller low class, a lower bound there already implies the same-arity lower bound at c0 by monotonicity; padding adds no magnification leverage when the full parameter family is known. Rounded dimensions require an unproved constant-factor threshold robustness argument, so use exact rational subsequences or prove robustness separately. For infinitely-often hardness, the source hard arities must meet the chosen subsequence (automatic for an all-large-n bound).

The C-118 endpoint restriction is valid: the source definition allows every pair of subsets of the filter universe, including empty sets. If a variant disallows empty endpoints, delete any restricted pair with an empty side; every proper semi-filter excludes the empty set, so such a pair is vacuously preserved. **Status:** exact transfer and endpoint audit proved; no lower bound or P-vs-NP separation obtained. Full derivation: [C-119 in the DAG/fusion bridge report](DAG_FUSION_BRIDGE_2026-09-26.md#49-c-119---padding-quantifiers-endpoint-admissibility-and-the-ops-threshold).

## C-120 - One signature cell can carry all high-table disagreement

Let C compute low w and select k=floor((1/2)log2(s2)) wire values including its output. A largest common-signature cell F has size at least N/2^k=Omega(N/sqrt(s2)), and w is constant on F. There are 2^|F| tables agreeing with w outside F; the two constant-on-F completions have size s1+O(k). For every fixed beta<2/3, |F| exceeds log2|SIZE(s2)|=O(s2 log(n+s2)), so some completion is high and nonconstant on F. It differs from w only inside F. By C-49, the mismatch count there is still Omega(s2/n).

Thus the C-115 minority-mass witness can be concentrated in one selected signature cell. Any lower bound whose charge is the number of mixed cells gets only 1. This does not refute a count-intersection PLS by itself: that would require compact Alice- and Bob-local witness sets, and the mixed-cell set is indexed by Alice's circuit partition. The varying cell remains circuit- and pair-dependent; this gives no shared-DAG, cyclic-cover, or P-vs-NP lower bound. Full proof: [C-120 in the DAG/fusion bridge report](DAG_FUSION_BRIDGE_2026-09-26.md#50-c-120---high-table-mismatch-can-be-concentrated-in-one-gate-signature-cell).

## C-121 - Common-partition families have O(N) mismatch DAGs

Suppose every low row is constant on each cell of a fixed partition of the truth-table coordinates into m cells, whose label map costs t gates, with t+O(m)<s2. Every cell-constant table then has a circuit of size below s2, so each high table is mixed on some cell. A rect-DAG lets Bob select a mixed cell, Alice reveal that row's bit on it, and Bob scan the cell for an opposite high bit. The selector costs O(m) vertices and the cell scans total O(N), giving O(N) size. This generalizes C-80.

For Y=SIZE(s1), every point indicator has O(n) gates and lies in Y for large n. Any partition on whose cells every low row is constant must therefore be discrete; with m=N, the cell-constant lookup is not below s2 when beta<1. So a common useful partition cannot solve the full promise. Combined with C-120, this isolates the remaining issue as adaptive sharing across circuit-dependent partitions. No arbitrary-DAG or rho lower bound follows. Full proof: [C-121 in the DAG/fusion bridge report](DAG_FUSION_BRIDGE_2026-09-26.md#51-c-121---a-common-cheap-partition-gives-a-linear-dag-and-full-sizes1-has-no-such-partition).

## C-122 - Small anchor families admit O(N)-vertex shared DAGs

For any fixed family A={w_1,...,w_r} of r<=eta n low tables, use their joint output signature W(x)=(w_1(x),...,w_r(x)). If high z were constant on every joint fiber, then z=h(W) and has a circuit of size at most r s1+O(r2^r)<s2 for eta<min(beta,c/3). Hence every high z is mixed on a common cell for all rows in A. The C-121 router gives a rect-DAG of O(N+2^r)=O(N) vertices for A x Z.

This strengthens C-109 from witness existence to a shared router and rules out incompatibility arguments based only on O(n) selected anchors. It does not scale to all Y: a row outside A need not be constant on W-fibers, and the naive partition into groups costs O(N|Y|/n). No suffix reuse across groups or global q lower bound follows. Full proof: [C-122 in the DAG/fusion bridge report](DAG_FUSION_BRIDGE_2026-09-26.md#52-c-122---any-on-sized-low-anchor-family-has-a-linear-shared-router).
**C-123 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Descriptor invariance and the universal-DAG barrier.** For any surjection from circuit descriptions D onto the low truth-table set Y, the minimum rect-DAG size for mismatch on DÃƒÆ’Ã¢â‚¬â€Z equals that on YÃƒÆ’Ã¢â‚¬â€Z: lift Alice-side state predicates by preimage, and reverse by restricting to a section. The same size is ÃƒÅ½Ã‹Å“(C_sep), where C_sep is the Boolean circuit size of any separator h with h(Y)=1 and h(Z)=0. Directly OR-ing one exact-table test per description gives an explicit O(NÃƒâ€šÃ‚Â·2^ell) separator/DAG for ell=O(s1 log(s1+n)); this is exponential in description length. A universal evaluator for one supplied description does not implement the existential projection defining Y. This kills the syntax-only shortcut and binary-search construction, not all small DAGs; no lower bound on C_sep or rho follows.
**C-124 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Adjacent MCSP literature does not transfer automatically.** The 2026 conditional NP-hardness result for Gap-ImpMCSP takes succinct sampler circuits as inputs; the project separator takes explicit N-bit tables, and no polynomial-size composition from the former to the latter is known. Austrin-Risse's SoS degree lower bound is per fixed hard table, whereas the needed object is one separator for all low/high tables. Neither result implies a bound on S_rect or rho_prom. See C-124.

## C-125 - Monotone partial-table transfer and OR-only no-go

A q-pair fusion cover gives a cyclic monotone separator H_Q on signed table rails, with q AND gates under least-fixed-point semantics. If an acyclic monotone map phi uses a AND gates, every YES input of f has a low one-hot table code below phi(x), and every NO input has phi(x) below a high code, then H_Q composed with phi computes f. Consequently CycAnd(f) <= q+a, hence q >= CycAnd(f)-a. A consistent NO partial table with d unset coordinates has a high completion whenever 2^d > |SIZE(s2)|.

If every rail of phi is constant or an OR of variables, f(0)=0, f has at least one YES input, and every input of weight at most two is NO, the NO condition prevents both signs of any coordinate from appearing. Any YES input must contain the same fixed low code. Conjoining its N rail predicates computes f with at most N-1 AND gates. So OR-only maps cannot transfer a cyclic lower bound above N. For triangle, Cavalar-Oliveira give Omega(r^3/log^4(r)); the direct map assigns one fixed low table to each candidate and computes candidate-triangle indicators, costing O(r^3) AND gates, so this lower bound gives no positive q bound. No Gap-MCSP instantiation or separation follows; see C-125 in the DAG/fusion bridge report.




## C-126 - Exact factorization through low-code extension

Let LowExt_Y(u)=1 iff some low table code e(w), w in Y, is coordinatewise below u. Any C-125 map phi satisfies f(x)=LowExt_Y(phi(x)): YES follows from its low-code witness; for NO, a low code below phi and a high code above phi would imply e(w)<=e(z), forcing w=z, impossible because Y and Z are disjoint and codes are one-hot. The high-completion condition still matters: it places NO images below a point where the fusion separator is known to be zero; medium inputs have unconstrained separator values. Therefore transfer-map design has two obligations: reduce f to LowExt_Y with few AND gates, and ensure every NO image has at least one high completion. A count of unset bits is sufficient but not necessary. On NO inputs phi is consistent; on YES inputs it may have extra rail conflicts beyond the selected low code. No bound on the required AND count is known.

## C-127 - Witness variation requires many conflict coordinates

For a C-125 map phi for a monotone f with a YES input, define S(phi) as the coordinates where some YES image has both signed rails active, and let delta=|S(phi)|. Choose one low-table witness w_x for each YES input x. For any x,y with f(x)=f(y)=1, monotonicity puts both codes below phi(x OR y); hence every coordinate on which w_x and w_y differ lies in S(phi). All selected witnesses agree with a fixed w0 outside S. There are at most 2^delta low tables matching w0 there.

Enumerate these tables: conjoin the fixed outside-S rails, OR the inside-S code tests for all such tables, and reuse phi's outputs. This computes f, since a NO input accepted by the circuit would have a low code below phi and a high code above it, forcing the same table. The acyclic circuit uses at most a+N+delta*2^delta AND gates, so CycAnd(f)-a <= N+delta*2^delta. Therefore a C-125 transfer proving q>N^(1+epsilon) requires delta >= (1+epsilon)log2(N)-O(log log N). This is a structural constraint on the transfer map, not a q upper bound or a fusion-cover lower bound.


## C-128 - Promise MCSP lower bounds for formulas do not reach shared DAGs

The local-PRG argument of Cheraghchi-Kabanets-Lu-Myrisiotis extends to a gap promise separator: uniform tables are high with probability 1-2^{-N+o(N)} when s2=N^beta, beta<1, while every local-PRG output of circuit size <=s1=N^beta/(cn) must be accepted. Thus a size-S de Morgan formula separator needs S>=N^(3beta-o(1)) for beta>1/3, using locality S^(1/3)2^{O((log S)^(2/3))}; arbitrary-basis formula or general branching-program separators need S>=N^(2beta-o(1)) for beta>1/2, using locality S^(1/2)2^{O(sqrt(log S))}. For smaller beta these are not superlinear bounds. These are tree/formula or branching-program lower bounds; they do not lower-bound the shared rect-DAG or q. Medium-band behavior is genuinely free in the transferred argument. Source: Cheraghchi et al. (2020), full citation in C-128 of the bridge report.

## C-129 - C-75 resource bounds and state-volume exclusion

For the total signed-mismatch relation on Y=SIZE(s1), Z={0,1}^N minus SIZE(s2), let M2=|SIZE(s2)| and choose d>log2(M2). Partition coordinates into m=floor(N/d) disjoint d-blocks. Each block supports 2^d>M2 tables, so it supports a high table z_i. Against the common low row 0^N, the valid signed mismatch labels are nonempty and pairwise disjoint across i. Hence any standard protocol tree or rect-DAG has at least m leaves, and deterministic communication is at least log2(m)-O(1). Taking d=Theta(s2 log(s2+n)) gives D_cc >= (1-beta)n-O(log n) and a direct DAG/tree floor N^(1-beta-o(1)).

For a rect-DAG node v with feasible rectangle A_v x B_v and descendant-coordinate set K_v, validity implies disjoint K_v-projections of A_v and B_v. If k=|K_v| and r=|pi_Kv(A_v)|, then each distinct row signature excludes at least 2^(N-k)-M2 high columns from B_v whenever positive. Thus |Z minus B_v| >= r(2^(N-k)-M2). This is a proved local product-hull/volume constraint: merging more low-row signatures forces the state either to retain a large descendant output set or to exclude more high columns. No global charging is known. This does not improve q: the existing rho_prom>=N-o(N) floor and rho_prom<=O(S_rect) already imply S_rect=Omega(N), while q-to-rect-DAG remains only the upper simulation S_rect<=O(q^3/log q). Full proof and model bounds are in C-129 of research/DAG_FUSION_BRIDGE_2026-09-26.md.

## C-130 - Raw exclusion volumes overlap across reachable states

In the C-78 restriction-sharing DAG, choose w=0 and a high z supported on d coordinates, with d>log2(M2) and d=O(s2 log(s2+n))=o(N/log N). For every dyadic interval I disjoint from supp(z), the reachable state R_(I,0) excludes z from its high-column side. Since at most d(log N+1) dyadic intervals meet supp(z), z is excluded at Omega(N) distinct reachable states. Thus summing C-129's local excluded-volume count with constant multiplicity is invalid. This kills raw per-state volume charging, not weighted/path-context potentials. Full calculation: C-130 in the DAG/fusion bridge report.

## C-131 - Every low row needs almost all output coordinates in its reachable subgraph

Let M2=|SIZE(s2)|. For any low row w and coordinate set S with 2^(N-|S|)>M2, the fiber {z:z|S=w|S} contains a high table. Therefore no set of fewer than N-log2(M2) mismatch coordinates can hit all high columns against w. In any correct rect-DAG, the set of coordinate labels on leaves reachable while Alice holds w must have size at least N-log2(M2)=N-N^(beta+o(1)). This is a per-row support requirement, not a superlinear vertex bound: it only counts distinct coordinates (at most N for fixed w), not how many context-specific leaves are needed. The natural bottleneck width h_v(w), defined as the minimum number of descendant coordinates hitting all B_v columns, is already N-o(N) at the root, so the published triangle-DAG bottleneck assignment does not transfer directly. Beame--Whitmeyer's 2025 Search-BPHP bottleneck method depends on collision/equality structure and has no known reduction to this promise relation. See C-131/O-111.

## C-132 - A width-band node may contain all low rows

Let I have 3N/4 coordinates, P=pi_I(Y), and B={z in Z:z|I not in P}. Since |Y| and M2=|SIZE(s2)| are 2^o(N), for any w in Y and S subset of I with |S|<=N/2, the fiber matching w on S has at least 2^(N/2) tables. Fewer than M2 are non-high and at most |P|2^(N/4)=2^(N/4+o(N)) have prefix in P, so some high z in B matches w on S. Therefore for the valid rect-DAG subproblem Y x B, h_v(w)>N/2. A protocol whose outputs lie in I gives h_v(w)<=3N/4. Thus one node with row side all of Y can lie in a common width band for every low row.

Attach this node to a full protocol by splitting Y x Z into Y x B and Y x (Z minus B); both children are rectangles and each subproblem has a valid protocol. The root width is at least N-log2(M2)=N-o(N). With band [0.4N,0.8N), the child node lies in-band and has width greater than half the root for every row, so a legal width-preserving path choice can route every row through it. This disproves any generic per-node capacity estimate based only on the natural width h_v(w). It does not rule out a globally chosen assignment or a refined statistic tracking the excluded-column family. No DAG or fusion lower bound follows. See O-112.

## C-133 - Local surjectivity makes the C-78 universal DAG huge

For any coordinate set I of k points, every restriction u in {0,1}^I is realized by a truth table that is 1 on the selected points of I and 0 elsewhere. An OR of at most k point minterms computes that table in at most kn+n+O(1) fan-in-two gates. Hence pi_I(Y)=2^k for k<=s1/(8(n+1)).

The C-78 dyadic restriction-sharing construction creates a distinct state for each interval I and each realized restriction u. Choose a dyadic k between s1/(32(n+1)) and s1/(16(n+1)). Its N/k intervals contribute (N/k)2^k states. Distinct patterns give different nonempty row sides; distinct intervals at this level also give different row sides because arbitrary patterns on their 2k-coordinate union are low-realizable. Thus the construction has 2^(Omega(s1/n)) = 2^(Omega(N^beta/n^2)) states, far above N^(1+o(1)).

This kills only that interval-and-exact-restriction construction. It is not a lower bound for arbitrary rect-DAGs or rho_prom; general states may use semantic row subsets, arbitrary coordinate sets, and high-column filtering. O-113 records the missing routing theorem. No P-vs-NP result follows.

## C-134 - Maximal local row richness is compatible with a linear DAG

For I of size k<=s1/(8(n+1)), let Y_I be all truth tables supported inside I. The point-minterm construction realizes every pattern on I, so |Y_I|=2^k. Yet every high z in Z has a 1 outside I, while every row in Y_I is 0 outside I. A rect-DAG scans the N-k outside coordinates; at the first 1 it outputs the valid signed mismatch (j,0). The continuation rectangles fix earlier outside bits to 0, so this is a standard O(N)-vertex rect-DAG.

Therefore local projection richness, even on an exponentially large subfamily, is not by itself a general non-shareability invariant. The argument does not extend to all Y because the full low class has no such common zero region. C-133 still rules out only the C-78 exact-restriction construction, and no arbitrary-DAG or rho_prom bound follows. O-114 records the sharpened obligation.

## C-135 - Small variation support gives a common-mismatch router

Let A be a nonempty subset of Y, and define V(A) as the truth-table coordinates on which A is nonconstant. Choose w0 in A. Any table z agreeing with w0 outside a coordinate set S can be computed from a size-s1 circuit for w0 by patching S: z=(w0 AND NOT chi_S) OR p, where chi_S marks S and p marks the positions in S where z is 1. Point-minterm circuits give CC(z) at most s1+K n(|S|+1) for an absolute K.

If the size of V(A) is at most d=floor((s2-s1)/(4K n)) and the gap dominates the additive O(n), every completion matching w0 on the common coordinates [N] minus V(A) has complexity at most s2. Therefore each z in Z differs from that common pattern somewhere outside V(A), a coordinate where every row in A has the same bit. Scanning these coordinates gives an O(N)-vertex rect-DAG for A x B for every B subset of Z. For OPS, d=Theta(s1).

This generalizes C-134's common-zero support block. It classifies low-variation rectangles as locally easy but does not bound how many such states a full protocol needs; large variation support is not itself hard. O-115 is the remaining global task. No superlinear DAG or fusion-cover bound follows.

## C-136 - Hamming gap makes witness scarcity and ordinary fooling sets too weak

Let Y=SIZE(s1), Z={0,1}^N minus SIZE(s2), and take d=floor((s2-s1)/(4Kn)) as in C-135. If w is low and z is high, changing w only on the r coordinates where w and z differ gives a circuit for z of size at most s1+Kn(r+1). Therefore r>d, or z would have size below s2. Every low/high pair has at least d+1 valid signed mismatch outputs.

For each coordinate i and sign b, the labelled rectangle R_(i,b)={w:w_i=b} x {z:z_i=1-b} is valid. Giving each of the 2N labelled rectangles weight 1/(d+1) covers every pair fractionally, with total weight 2N/(d+1)=O(N/s1)=O(n N^(1-beta)) in the OPS parameters. This is a statement about the ordinary labelled-rectangle cover of the search relation, not the fusion parameter rho and not a deterministic rect-DAG upper bound.

It also caps the usual label-conflict fooling-set method. If a family of pairs is pairwise unable to share any output-labelled leaf, their sets of valid labels are pairwise disjoint. Each such set has at least d+1 labels, among only 2N total, so the family has size at most 2N/(d+1)=O(N/s1). This does not cap arbitrary rectangle-partition or DAG lower bounds. C-138 improves C-129's explicit output-family construction from N/(s2 log s2) to N/s2; the remaining gap to this method ceiling is a factor Theta(n), and both quantities are sublinear for fixed beta>0.

Public randomness makes pairwise search cheap: sample a uniform coordinate, reveal its two bits, and stop on a mismatch. Each trial succeeds with probability at least (d+1)/N, giving a zero-error protocol with expected O(N/d) communicated bits when the sampled coordinate is public. Yet a fixed coordinate set T cannot certify all pairs if 2^(N-|T|)>M2=|SIZE(s2)|: for any fixed low w, the fiber agreeing with w on T then contains a high completion. Thus every universal fixed sample needs at least N-log2(M2)=N-o(N) coordinates.

**Structural lesson.** The relation has abundant witnesses, a small fractional labelled cover, and a short randomized search. The unresolved cost is deterministic routing: an adaptive protocol must remember enough of the equal-answer history to keep each continuation a rectangle, while globally sharing those continuation states across different low circuits. This reinforces the C-130/C-132/C-135 frontier; it proves no superlinear deterministic DAG or rho lower bound and no P-vs-NP result.

## C-138 - Counting gives disjoint high supports of size O(s2)

Let M2=|SIZE(s2)| <= 2^(C s2 log(s2+n)) for a circuit-model constant C. Fix beta<1 and choose r=ceil(A s2), where A is a sufficiently large constant depending on beta and C. Since

    log2 binom(N,r) >= r log2(N/r)
                         = A(1-beta-o(1)) s2 n,

we can ensure binom(N,r)>N M2 for all sufficiently large n. In a uniformly random permutation of [N], form m=floor(N/r) disjoint r-blocks. Each block is marginally a uniform r-subset; at most M2 subsets have indicator tables of circuit size <=s2. The expected number of non-high blocks is at most m M2/binom(N,r)<1. Therefore some partition has every block S_i high as a support table 1_{S_i}.

Against the low zero table, the valid output labels for (0^N,1_{S_i}) are exactly {(j,0):j in S_i}. These sets are disjoint across blocks, so every deterministic protocol tree or rect-DAG needs at least m=Omega(N/s2)=Omega(N^(1-beta)) leaves. This sharpens C-129's generic block-size choice d>log2(M2)=Theta(s2 log s2), improving its direct leaf and deterministic-communication floors by a factor Theta(log s2)=Theta(n): D_cc >= (1-beta)n-O(1).

The sphere count also gives a near-neighbor distribution: for any fixed low w, at most M2 of the binom(N,r) masks e of weight r make w XOR e non-high. With the chosen A this bad fraction is below 1/N. Sampling w from any distribution on Y and then a uniform weight-r mask therefore lands in Y x Z with probability 1-o(1). But each fixed output coordinate appears in the mask with probability r/N, so a direct leaf-mass argument under this distribution gives only Omega(N/r) leaves, the same scale as the block packing.

**Limit.** The direct leaf bound is still sublinear in N and is weaker than the existing Omega(N) rect-DAG floor implied by rho_prom>=N-o(N). It does not approach the superlinear target. Together with C-136, it narrows the elementary label-conflict fooling-set scale to between Omega(N/s2) and O(N/s1), a factor Theta(n), but does not change the active q-to-DAG transfer or prove a superlinear DAG bound.

## C-137 - A cyclic coordinate scanner is not a rectangle DAG

A tempting O(N)-state machine scans coordinates cyclically, outputs at the first mismatch, and sends both equal outcomes (0,0) and (1,1) to the same next state. On a promised unequal pair this terminates within one sweep. But a standard rect-DAG node must represent a rectangle. If the current rectangle is A x B and both row bit classes A0,A1 and column classes B0,B1 are nonempty, the equal-outcome union (A0 x B0) union (A1 x B1) is not a rectangle: any product containing both diagonal blocks also contains cross pairs A0 x B1 and A1 x B0. Thus the scanner's merge is a joint-input finite-state transition, not a legal rectangle-preserving protocol transition. Cyclicity does not remove this constraint.

For a fixed coordinate-order scanner, the necessary history cost is explicit. On any k coordinates with k<=s1/(8(n+1)), every prefix pattern u occurs on a low row by point-minterm realization (C-133). Every such pattern also has a high completion because 2^(N-k)>M2 for large n. Hence after k equal comparisons the continuation contexts A_u x B_u are all nonempty and have distinct row sides. A rectangle-preserving fixed-order scan must retain at least 2^k distinct contexts at that layer. Taking k=Theta(s1/n) makes this exponential in N^beta/n^2. This only rules out the fixed-order merge/scan architecture; it is not a lower bound on arbitrary rect-DAGs or on cyclic fusion complexity.

## C-139 - Exact ranked-cyclic protocol induced by a successful cover

For each rule i, the valid search state is the rectangle R_i=(Y intersect X_i) x (Z minus X_i). A successful Q makes the root Y x Z covered by the R_i for empty-carrier rules. At R_i, choose a side whose endpoint is absent from z's least closure; the side is present for w, so w supplies a literal seed or an earlier-active predecessor rule. A literal seed is a valid mismatch because the same matching slice is absent at z. A predecessor j is inactive at z by upward closure, and its first activation round on w is strictly below i's. Each branch condition factors into a row predicate and a column predicate, so all transitions preserve rectangles. The static graph can cycle, but each fixed-pair path terminates by strict decrease of the activation rank.

Thus q rules induce a ranked cyclic rectangle-search graph with O(q+N) vertices and O(q^2+qN) possible support arcs. This is not an ordinary rect-DAG: the literature's Sokolov Boolean games are globally acyclic and binary-outdegree, whereas the exact fusion characterization is cyclic intersection complexity. Rank-layering gives a direct standard rect-DAG of O(q^2(q+N))=O(q^3) size, which does not improve the best saved O(q^3/log q) compiler; it isolates rank unrolling and support routing as the costs. No reverse transformation from an arbitrary ranked cyclic rectangle protocol to a fusion cover is proved.

Also correct the tree comparison: for vertex-count measures S_DAG<=S_tree, so a small protocol tree cannot coexist with a larger minimum DAG. Low communication bits can coexist with exponentially many tree/DAG vertices; c bits imply at most 2^(c+1)-1 tree nodes. In Gap-MCSP, short circuit-description communication therefore says nothing near-linear about S_rect. C-139 is a model clarification and ranked-search construction, not a superlinear lower bound or P-vs-NP proof. See O-117/Q99 and the bridge report section 66.

## C-140 - Rank-layer overhead need not be separator overhead

For the abstract cyclic monotone system x1=(s1 OR x2) AND c and x2=(s2 OR x1) AND c, evaluated from zero, the least fixed point is x1=x2=c AND (s1 OR s2). On inputs (s1,s2,c)=(1,0,1) and (0,1,1), the two possible first-activation orders are opposite, so the support graph is cyclic and no fixed topological order preserves both witness paths. Nevertheless the output has a constant-size acyclic circuit. This shows that the q^2 rank-layer expansion can be an artifact of preserving the C-75 path, not a lower bound on the minimum separator.

Scope is deliberately limited: endpoint-realizability inside the C-74 fusion model is not proved, and the toy is not a Gap-MCSP reduction. It kills only arguments that charge the rank-layered witness construction itself. A useful non-shareability theorem must rule out output simplification or alternative paths. No rho, DAG lower bound, or P-vs-NP result follows.

## C-141 - Legal endpoint realization of the rank-reversing SCC

On Gamma={0,1}^5, let A={a=0}, B={b=0}, C={c=1}, P=C intersect (A union B), p1=(1,1,0,0,0), p2=(1,1,0,1,0), and set E1=A union P union {p1,p2}, H1=C union {p1}, E2=B union P union {p1,p2}, H2=C union {p2}. Then T1=P union {p1}, T2=P union {p2}; T2 subset E1, T1 subset E2, while the opposite H-side containments fail. Checking all signed coordinate half-cubes shows E1's only literal seed is A, E2's is B, and each H_i's only literal seed is C. After deleting self-supports, the legal fusion recurrence is x1=(1_A OR x2) AND 1_C and x2=(1_B OR x1) AND 1_C. The least fixed point is x1=x2=1_C AND (1_A OR 1_B), with opposite first-activation orders on the A-only and B-only inputs.

This proves that an input-ranked static cycle occurs in an actual semantic endpoint instance, not just in abstract equations. It is not a successful cover: T1,T2 are nonempty, and the example has no target/high promise. Its output is also a constant-size acyclic predicate, so it only validates the rank-overhead caution from C-140. No Gap-MCSP or rho lower bound follows.

## C-142 - Successful toy cover with input-reversing activation ranks

Let Y={(0,1,1,0),(1,0,1,0)} and Z={zA=(0,1,0,0), zB=(1,0,0,0), zC=(1,1,1,1), p1=(1,1,0,1), p2=(1,1,0,0)} over coordinates (a,b,c,f). Use pair endpoints E1={zA,p1,p2}, H1={zC,p1}; E2={zB,p1,p2}, H2={zC,p2}; E0={p1}, H0={p2}. Then T1={p1}, T2={p2}, T0=empty. On U=Z, the literal slices are a0={zA}, b0={zB}, c1={zC}, f1={zC,p1}, with complements as listed in bridge Ãƒâ€šÃ‚Â§69. The seed sets are E1:a0, E2:b0, H1:c1/f1, H2:c1, and no seed is contained in E0 or H0. The non-self support graph contains 1<->2 on E sides and the two root edges 1->0, 2->0.

The least-fixed-point equations are x1=(a0 OR x2) AND (c1 OR f1), x2=(b0 OR x1) AND c1, x0=x1 AND x2. On the two low anchors, the first activation orders are 1,2 and 2,1 respectively, and x0=1. On every z in Z, x0=0: zA/zB fail c1, zC has no a0/b0 seed so the cycle's least fixed point is 00, p1 has no E seed, and p2 has no rule seed. Hence this is a successful three-pair cover for the finite promise. Yet h=c AND (NOT a OR NOT b) separates Y from Z with constant size.

This demonstrates that rank-reversing cycles can occur inside a successful cover, while rank-layer duplication remains only a witness-path cost. It is not a Gap-MCSP embedding or a lower bound. Q101 is closed at the toy level; Q102 retains the actual-promise task.

## C-143 - Scaled rank-cycle calibration

For q>=4, take low anchors w_i with c=1 and one-hot seed bits t_i=1. Let Z contain z_i with c=0 and t_i=1, marker points p_i with c=0 and all t=0, and r with c=1 and all t=0. Add tag coordinates that uniquely identify these 2q+1 high points while each tag slice has size q or q+1; the probabilistic method gives L=O(log q) such coordinates. Pair i has E_i={z_i,p_i,p_(i-1)}, H_i={r,p_i}, so T_i={p_i}; the root pair E0={p1},H0={p2} has empty carrier. Size counting of restricted literal slices shows the only seeds are t_i=1 on E_i and c=1 on H_i; the root has none. The lfp is x_i=(t_i OR x_(i-1)) AND c and x0=x1 AND x2. Every low anchor activates the q-cycle in a different rotation and activates the root; every high point leaves the root inactive.

The separator h=c AND OR_i t_i has O(q) gates. The explicit rank-layer architecture nevertheless has q(q-1)+1 distinct rectangles R_(i,s), since for s<q the row side is a distinct cyclic window of s low anchors and all high columns remain. This proves a quadratic blowup for the rank-layer construction relative to a linear separator on a successful finite promise. It is not a lower bound on arbitrary rect-DAGs or rho and has no Gap-MCSP transfer. The lesson is to stop treating rank-layer states as necessary output states.

## C-144 - A deletion-minimal cyclic cover can have optimum rho=1

In the C-143 finite promise, let U=Z={z_i,p_i:i in [q]} union {r}. The single pair E*={z_i:i in [q]}, H*={r} has empty carrier. Every low w_i contains the generator {z_i} via t_i=1 in E* and {r} via c=1 in H*, so it derives empty. For a high point other than r, any matching t_j=1 singleton is {z_j}, not {r}; all matching t_j=0 and c=0 slices have size 2q, and matching tag slices have size at least q>=4. The c=1 singleton {r} is not matched. Hence H* is not generated. At r, every matching slice contains r and so cannot lie in E*. Thus this one-pair list covers the promise, and rho_prom=1.

The original q-cycle plus root list is deletion-minimal: removing the root leaves no empty carrier; removing cycle rule i leaves w_i without any E-side seed, and no state activates. This is not global minimum-cardinality. Hence deletion-minimality and a large cyclic SCC do not justify a lower bound on rho; an alternative semantic pair can bypass the entire list. C-143's rank-layer count remains true for its chosen witness protocol but its comparison to optimum is now Theta(q^2) versus 1. No OPS or P-vs-NP consequence follows.

## C-145 - Seed-first activation forces a large high carrier

For fixed OPS beta<1, circuit counting gives M2=|SIZE(s2)|=2^o(N). Every two-coordinate literal cylinder therefore contains at least 2^(N-2)-M2 high tables. In a successful q-rule cover, every low anchor must have some round-one active rule, since if the recurrence maps zero to zero its least fixed point is zero forever. That rule's two endpoints are both seeded by literals matching the anchor. Their common high cylinder is contained in T_i=E_i intersect H_i, so |T_i intersect Z|>=2^(N-2)-M2; all those high tables also activate rule i at round one. (If the two literals use the same coordinate, the stronger one-coordinate count applies.) Thus every low anchor bootstraps through a state that is simultaneously active on a constant fraction of high inputs. This quantifies the failure of the C-143 sparse toy, whose seed cylinder is empty and whose carrier is a singleton.

The result is only local: those high inputs may activate nonempty states and still avoid every empty carrier. It does not improve the q>=N-o(N) floor. The next target is a global charging argument for how later supports shrink these large coactivation regions while keeping each low anchor on a route to empty. See C-145/O-119/Q105.

## C-146 - A seed cylinder removes one state, but hard cofactors need not add

For a low w, C-145 supplies a round-one state i and matching seed literals on at most two coordinates. On their common subcube C, state i is identically active; it has nonempty carrier, so it is not an output state. Substituting it by 1 yields a q-1-state recurrence for the separator restricted to C. This is a cofactor statement about the induced recurrence, not automatically a legal q-1-pair cover, since restriction can introduce new endpoint containments.

A direct-sum amplification is false in general. For the finite promise Y={e_j:j in [r]}, Z={0,1}^r\Y, Z is two-coordinate shattered. A dual-rail prefix/suffix circuit gives rho=O(r), while any single low anchor needs all r literals in a closure certificate, so rho>=r-1. Each of the binom(r,2) cofactors fixing two bits to 00 is another exact-one promise on r-2 bits and has rho>=r-3. Therefore summing cofactor lower bounds would overcount by Theta(r^2), despite the global rho=Theta(r). The OPS target needs a direct-sum statement tailored to its low-circuit language; density plus cofactor hardness is insufficient.

## C-147 - Shared-DAG re-entry audit (checkpoint; no new lower bound)

The current shared-DAG agenda is already substantially developed in C-78--C-123 and C-139--C-146. Primary-source reinspection confirms the model boundary: Sokolov/GGKS rect-DAGs are acyclic with out-degree at most two and free local predicates; the project cover is exactly cyclic intersection complexity. A descriptor-space mismatch DAG has the same size as the truth-table-row DAG by lift/restrict, so short circuit syntax alone cannot compress its topology. The quantitative chain remains rho_prom=D^circ_cap and rho_prom<=SepCirc=Theta(S_rect)<=O(rho_prom^3/log rho_prom). No near-linear universal DAG, arbitrary-DAG non-shareability bound, superlinear rho bound, or P-vs-NP proof was obtained. Continue under O-121; do not repeat C-123/C-137 as open tests.

## C-148 - Promise-specific local-PRG lower bound for formulas

For OPS thresholds s1=N^beta/(c n), s2=N^beta with fixed 1/3<beta<1, every De Morgan formula h satisfying h=1 on SIZE(s1) and h=0 outside SIZE(s2) has size at least N^(3beta-o(1)). The CLKM local-PRG lemma is stated only for formula size t>=N, with output-local circuit complexity lambda(t)=t^(1/3)2^(O((log t)^(2/3))). Since lambda(N)<=s1 for beta>1/3, padding rules out formula size below N; applying the lemma for N<=t<=N^3 gives t>=s1^(3-o(1)); t>N^3 is already larger. The medium band causes no issue because its uniform measure is at most |SIZE(s2)|/2^N. For beta<=1/3 this cited lemma yields no such lower bound: its t>=N parameter floor has locality too large for s1. This is a promise-specific formula result only in the beta>1/3 range, not a rect-DAG or rho lower bound. See bridge section 75 and the primary CLKM paper.

## C-149 - Correct the CLKM parameter range

The C-148 claim for all beta<1 was overbroad. Lemma 17 of the cited CLKM paper assumes formula size t>=N. Padding a smaller separator to N only works when beta>1/3, since lambda(N)=N^(1/3+o(1)) must be at most s1=N^beta/(c n). Thus the stated N^(3 beta-o(1)) promise-formula lower bound is valid for beta>1/3 only; the cited argument gives no such bound for beta<=1/3. This removes C-148 from the active small-beta magnification range. It never implied a rect-DAG or fusion lower bound.

## C-150 - First-excluded activation state gives a literal mismatch witness

For a successful Q, fix low w and high z. Among states i active on w with z notin T_i, choose one of minimum first-activation round tau_i(w), breaking ties by index. This set is nonempty because an active empty-carrier rule exists. Since z misses T_i=E_i intersect H_i, it misses an endpoint, say E_i. At i's first activation, E_i was seeded by a matching literal or by an earlier active carrier T_j subset E_i. The latter would have tau_j<tau_i and z notin T_j, contradicting minimality. Hence E_i contains a matching literal slice L_(k,w_k), while z notin E_i, so w_k differs from z_k. The H_i case is symmetric. Therefore Q induces a canonical mismatch selector by scanning active states in (tau_i,i) order and stopping at the first carrier that omits z.

This simplifies the witness path but does not yet improve the DAG compiler. After t scans the continuation relation has row residuals P_t(w)=intersection of the first t active carriers. These residuals vary with w in general, so merging scan histories can create a nonrectangular product hull and lose the fact that earlier carriers contained z. Keeping rank and current-state context gives up to q^2 states, and routing their supports/output literals can recover the known cubic-scale bound. No OPS residual-rectangle lower bound or arbitrary-separator consequence follows; see bridge section 76 and O-122.

## C-151 - Canonical selector hardness can vanish under output projection

For k>=2, let A_S=[k]\\S and B_T=T union {k}, with S,T subset [k-1]. Their intersection is {k} union (T\\S), always nonempty. In the unique-minimum relation, each diagonal (S,S) outputs k. Distinct S,T force one cross-pair to have minimum below k, so a k-labelled rectangle contains at most one diagonal. Hence at least 2^(k-1) such leaves. If any common element is accepted, k solves every pair in one leaf. This is a finite rect-DAG example where canonical-selector hardness disappears under projection to any witness; it gives no OPS bound.

## C-152 - Selector transfer requires leaf homogeneity

If a rect-DAG for a multivalued relation has a canonical selector h constant on each accepting leaf rectangle, relabeling its leaves gives an h-DAG at unchanged size. An input-independent decoder from every valid output label to h is a sufficient way to guarantee this. C-151 shows the condition cannot be presumed: the one-leaf any-intersection solver outputs k on all inputs, while the unique minimum varies. C-150's carrier index is not part of the signed-mismatch output, so no selector-to-mismatch transfer is established. Any transfer must prove leaf homogeneity for all valid separators or give another reduction. Cyclic/loop models are outside this lemma unless their terminal reach sets obey the same rectangle semantics.

## C-153 - A valid mismatch rectangle mixes first-excluded states

In the successful C-142 toy, both low anchors have c=1 and high columns p1,p2 have c=0, so Y x {p1,p2} is one valid c-mismatch rectangle. The C-150 first-excluded carrier index on this rectangle is 2 for column p1 and 1 for p2, for both rows. A rect-DAG may route the whole rectangle to a c-labelled leaf and complete the finite promise on other columns by enumeration. Hence the generic all-separators leaf-homogeneity/label-decoder route fails even on a successful fusion toy. This is not an OPS embedding or lower bound; only a promise-specific restriction could restore the transfer.

## C-154 - A powerful CSP lifting theorem has no current Gap-MCSP transfer

The CCC 2025 colourful-sunflower lifting theorem gives a rect-DAG lower bound of (m/(A|Sigma|w(S)log(mn)))^w(S) for Index-lifted search SÃƒÂ¢Ã‹â€ Ã‹Å“Ind_m^n, where w(S) is subcube-DAG width. To use it here requires partywise maps from lifted inputs to low/high truth tables and an output-preserving decoder taking every mismatch leaf to a constraint falsified throughout its source rectangle; table length and circuit-class cardinalities must also fit. No such map is known. The result is a concrete lead and a template, not a Gap-MCSP or P-vs-NP lower bound. Any transfer must clear the current cubic/log compiler threshold L/r>N^(3+3epsilon)/log N or reach rho_prom directly.

## C-155 RETRACTED - The partial-Index no-go imposed constraints off-domain

The proof wrongly required a(x)=b(y) whenever y_x=0. In SearchORÃƒÂ¢Ã‹â€ Ã‹Å“Index, those pairs have no valid output and lie outside the partial relation's domain, so a reduction need not satisfy anything there. On the legal domain y_x=1, the code a(x)=0^m, b(y)=y works: coordinate x mismatches, and every mismatch coordinate can decode to the sole output 1. Thus the claimed direct-encoding impossibility is false. The error is a quantifier/domain mistake, not a subtle gap. In the CCC CSP application the base unsatisfiable-CSP search is total; a corrected argument must use valid outputs on every lifted input pair.

## C-156 - Direct mismatch encodings are paired monochromatic cut covers

For a total relation R on X x Y, separate r-bit codewords a(x),b(y) with a fixed decoder delta(t,u,v) work exactly when the following oriented rectangles cover X x Y and each rectangle's label is valid throughout it: X_t^0 x Y_t^1 labelled delta(t,0,1), and X_t^1 x Y_t^0 labelled delta(t,1,0), where X_t^u={x:a_t(x)=u} and Y_t^u={y:b_t(y)=u}. This follows because bitwise mismatch at t is exactly the union of those two cross-products; conversely, any family of paired row/column cuts satisfying coverage and validity defines such codewords. A plain monochromatic rectangle cover is insufficient because every coordinate creates both complementary cross-rectangles. This characterizes fixed-label coordinatewise reductions only; an input-aware decoder must be refined and charged separately. No Gap-MCSP transfer follows yet.

## C-157 - A cyclic mismatch router is vacuous without progress

One can put the full promise rectangle at each of 2N cyclic states, give each state an edge to one signed mismatch leaf and an edge to the next state, and obtain a finite valid path for every pair in O(N) vertices. But there are also infinite continuation paths. If cyclic protocols require only existence of a finite accepting path, every total relation with a valid output per pair has this trivial construction. The model must require termination under its transition strategy or a well-founded rank. C-74's one-sided activation semantics and C-139's decreasing first-activation rank are additional structure; the root-loop does not give a fusion cover or a standard DAG.

## C-158 - Two-child rectangle coverage preserves a full side

If A x B is covered by A_0 x B_0 and A_1 x B_1, then either A is contained in A_0 or B is contained in B_1 (after intersecting with the parent). A standard binary Boolean-game node therefore permits a locally deterministic choice by one party. This is local and gives no state-count lower bound. For C-75 the fixed-output relation bounds remain n-o(1) to O(N^beta) communication bits and N-o(N) to 2^(O(N^beta)) tree/DAG vertices, plus the q-cover compiler S_rect=O(q^3/log q). No superlinear q or S_rect lower bound follows. See bridge sections 83-84 and O-126.


## C-159 - C-158 is a known rectangle-to-circuit trichotomy

Sokolov's Theorem 3.2 proof already establishes the stronger three-case property for a rectangle covered by two child rectangles: either the parent row side lies in both child row sides, the parent column side lies in both child column sides, or one child contains the parent rectangle. These cases reconstruct the separator circuit by AND, OR, or copying. C-158 is a weaker corollary, not a novel DAG lower-bound lemma. Its only remaining research value is as a possible local ingredient in a global state-reuse charge. This does not improve the current lower bounds. Primary source: https://eccc.weizmann.ac.il/report/2016/202/download

## C-160 - Generic cylinder and trichotomy data permit near-linear DAGs

Take a=floor(N^beta/log N), low rows of weight at most a or at least N-a, and high columns from the middle band b<weight<N-b for b=floor(N^beta). Then the low class has size 2^Theta(N^beta), the non-high class has size 2^Theta(N^beta*log N), every pattern on at most a coordinates occurs among low rows, every low/high pair has distance Theta(N^beta), every cylinder larger than the non-high class contains a high column, and the radius-a neighborhood of the low class is non-high. The low class is complement-closed, and every coordinatewise Boolean combination of up to floor(b/a)=Theta(log N) low rows stays non-high. Nevertheless, testing whether the weight is at most a or at least N-a is a separator of fan-in-two circuit size O(N log N), hence the rect-DAG and active fusion cover are O(N log N)=N^(1+o(1)). Therefore no superlinear lower bound follows in general from these statistics plus the C-129 local inequality and Sokolov's AND/OR/copy trichotomy. This is only a calibration: it does not construct a small DAG or cover for actual Gap-MCSP. O-126 must use finer OPS-specific structure or directly exploit cyclic closure.

## C-161 - Balanced affine low rows still admit a near-linear promise separator

Augment the C-160 synthetic low side with all affine truth tables on n input bits, and augment its non-high set with the radius-a neighborhoods of those affine tables. The affine family has 2N members, all of circuit size O(n). The added neighborhoods have size at most 2N times the Hamming-ball volume of radius a, whose logarithm is Theta(N^beta), so the non-high count remains 2^Theta(N^beta log N). The low/high Hamming gap is at least a+1, and the large-cylinder and local-pattern facts remain valid.

For an N-bit table u, compute its Walsh transform. The nearest affine truth-table distance is \((N-\max_\ell|\widehat{(-1)^u}(\ell)|)/2\). A fast Walsh-Hadamard circuit uses O(N log^2 N) Boolean gates, including integer additions on O(log N)-bit values. Thus the augmented promise has a separator, rect-DAG, and active fusion cover of size N^(1+o(1)). Balanced low rows, an affine orbit, and its patch neighborhoods do not suffice for a superlinear DAG bound. This calibration does not preserve the full C-160 closure under arbitrary recombination of Theta(n) low rows; exploiting that closure across a rich family of bases remains open. No actual Gap-MCSP upper bound or lower bound follows.

## C-162 - Description-space equality; basis labels do not imply non-shareability

For a surjection G:DÃ¢â€ â€™Y from low-circuit descriptions to distinct low truth tables, the minimum standard mismatch rect-DAG size on DÃƒâ€”Z equals that on YÃƒâ€”Z: lift row rectangles by G^{-1}, and restrict a description-DAG along any section YÃ¢â€ â€™D. Thus short syntactic descriptions alone provide no shared-state compression. The best generic description protocol still has exponential-in-communication tree size; the universal joint mismatch predicate is nonrectangular.

The ordered bases in GL(n,2) number 2^{nÃ‚Â²+O(1)}, but their component rows range over only the N linear functions. For each basis A and combiner g, g(Ax) costs size(g)+O(nÃ‚Â²), so the compositions that fit the s1 budget are already rows of Y. Exact affine membership is testable by WalshÃ¢â‚¬â€œHadamard transform in O(N logÃ‚Â²N), giving a near-linear mismatch DAG for Aff_nÃƒâ€”Z. No obstruction across nonlinear g-composition families follows.

Model/conversion result reaffirmed: q=ÃÂ_prom=DÃ‚Â°_cap; q yields a ranked cyclic router and S_rectÃ¢â€°Â¤O(qÃ‚Â³/log q), while an L-node standard mismatch DAG gives ÃÂ_promÃ¢â€°Â¤O(L). Thresholds remain q direct >N^(1+ÃŽÂµ), AND-only >N^(2+2ÃŽÂµ), or standard rect-DAG >N^(3+3ÃŽÂµ)/log N. This is a precise reformulation/falsification checkpoint only; no new lower bound or P-vs-NP result.

The composition budget must be handled on the promise domain: a table generated within the \(s_2\) size budget is either already in \(Y\), or may lie in the omitted medium band. Medium rows are not C-75 inputs, so their exclusion from \(Z\) does not by itself constrain a mismatch DAG.

## C-163 - Decoder capacity from the promise Hamming gap

Let Delta=Theta(N^beta/n) be the C-136 minimum distance between Y and Z. For a total source relation R, let chi_out*(R) be the minimum total weight on outputs such that every source pair has valid-output weight at least one. Suppose partywise maps send every source pair to Y x Z, and a decoder started from any signed mismatch type has at most r output-labelled terminal incidences, counting separately for each type. There are 2N types. For each output o, let c_o count its incidences. Every source pair has at least Delta mismatch coordinates, each of which must decode to a valid source output, so sum_{o in R(x,y)} c_o >= Delta. Thus c_o/Delta is a fractional output cover and
chi_out*(R) <= (sum_o c_o)/Delta <= 2Nr/Delta = O(r n N^(1-beta)).

For r=1, this is necessary for C-156's fixed-decoder paired-cut embeddings. If the source relation has a unique answer on each pair and uses M labels, then chi_out*=M, requiring r >= M Delta/(2N). The relation whose answer is Alice's k=floor((1-beta/2)n)-bit input has M=Theta(N^(1-beta/2))<2N; its inputs encode as low truth tables with O(n^2)-size circuits, yet any mismatch-based decoder needs Omega(N^(beta/2)/n) terminal incidences per signed mismatch type. This calibrates an output-interface barrier, not the Gap-MCSP DAG itself. It applies only when every mismatch is decoded through the charged interface; it gives no separator or fusion-cover lower bound.

## C-164 - Rectangle mass bound for Index-lifted cPHP

Let G be a simple bipartite graph of left degree d>=2, with k left vertices, and consider Search(cPHP(G)) composed with Index_m^k. Alice inputs x in [m]^k, Bob inputs y in [d]^(mk), and a distinct output pair p!=q is valid when Gamma(p,y_(p,x_p))=Gamma(q,y_(q,x_q)). Under uniform product inputs, any rectangle A x B all of whose pairs admit the fixed distinct output pair (p,q) has measure at most 1/(m^2 d).

For proof, let S be the projection of A to pointer pairs (x_p,x_q). Its row density is at most |S|/m^2. Bob's rectangle side must satisfy a partial-matching constraint between variables y_(p,i) and y_(q,j) for every (i,j) in S. If the resulting bipartite graph has rank R=sum_components(vertices-1), then the Bob density is at most d^(-R). Each component with v vertices has at most floor(v^2/4)<=d^(v-2) edges; summing over nontrivial components gives |S|<=d^(R-1). Thus the product density is at most 1/(m^2 d).

Consequently, any partywise encoding of this relation into OPS low/high tables with minimum distance Delta=Theta(N^beta/n), followed by at most r valid rectangle leaves per signed mismatch type, must satisfy Delta<=2Nr/(m^2d), so r>=Delta m^2d/(2N). The cPHP outputs are pigeon pairs, giving the coarser chi_out*<=binom(k,2); C-164 adds the Index-rectangle density cost. This constrains a proposed decoder refinement only. It does not rule out the lifted-CSP route or prove a target DAG/fusion lower bound. The exact transfer must still compare the lifting lower bound divided by r with N^(3+3epsilon)/log N, and produce the low/high maps.

## C-165 - Fixed-decoder obstruction for the signed C-75 relation

For Search(cPHP(G)) composed with Index_m^k, with G simple of left degree d>=3 and m divisible by d, under uniform Bob inputs each fixed Alice input x and each output pair of distinct pigeons p!=q has validity probability at most 1/d. For any partywise embedding into disjoint table families and a mismatch decoder with at most r output-labelled rectangle leaves per signed mismatch type, consider one table coordinate and the partitions A_0,A_1 of Alice and B_0,B_1 of Bob. If both Alice sides are nonempty, fixing one x on each side shows mu(B_0),mu(B_1)<=r/d; hence r>=d/2. If r<d/2, every Alice code bit is constant. Choose y* so each pigeon's selected-neighbor sequence is balanced across its d neighbors. Every output pair is then valid on at most a 1/d fraction of Alice inputs. Since each mismatch type at y* is either active for all x or none, r<d/2 output leaves cannot decode any active type over all x; if none is active the encoded low and high tables are equal. Both alternatives contradict totality and disjointness. Therefore r>=d/2, and a fixed decoder r=1 is impossible.

This does not contradict the CCC cPHP-to-clique-colouring reduction: that reduction decodes the one-sided mKW output (edge in Alice's graph and absent in Bob's), not both orientations of a general signed mismatch. A bounded input-dependent refinement remains possible; combine this with C-164's r>=Delta*m^2*d/(2N) distance requirement. This is a scoped transfer no-go, not a lower bound on S_rect or rho_prom.

## C-166 - Re-audit of the known interval-router obstruction

For each coordinate interval I and low restriction r, the universal interval router uses the rectangle
A_r x B_r = {w in Y:w|I=r} x {z in Z:z|I!=r}.
If every low restriction s on I has a high extension z_s in Z, then distinct restriction states cannot merge while their descendants are required to output a mismatch inside I: z_s lies in B_r for r!=s, so the product hull contains (w_s,z_s) for w_s|I=s, a pair agreeing throughout I. Counting gives the extension premise whenever 2^(N-|I|)>|SIZE(s2)|. Also, O(Ln) point-indicator circuits realize all 2^L patterns on any L selected positions when L n<=s1/O(1). Hence interval-local scanners need 2^L contexts per such interval. This is a rigorous scanner-specific non-shareability theorem. It does not lower-bound arbitrary rect-DAGs because a DAG may change coordinates or solve cross-pairs outside I; the needed normalization is open. See bridge Ã‚Â§92.
## C-167 - C-160 refutes generic interval normalization

For the C-160 promise Y_a={x:|x|<=a or |x|>=N-a}, Z_b={z:b<|z|<N-b}, with a=floor(N^beta/n), b=floor(N^beta), every pattern on an interval I of length L<=a extends both to a low row (fill the complement with zeros) and to a high column (fill to weight floor(N/2)). The interval-local router therefore has 2^L pairwise nonmergeable restriction contexts: merging r and s puts a cross-pair (w_s,z_s) in the product hull that agrees on I. At L=a its size is at least 2^a. Yet the promise has an O(N log N) threshold separator and therefore an O(N log N) arbitrary rect-DAG. Thus no promise-independent normalization to interval-local routers can have polynomial size loss. This only refutes the generic O-127 route; an OPS-specific normalization and every actual Gap-MCSP lower bound remain open. See bridge C-167.
## C-168 - Alice-only coordinate selection requires N-o(N) positions

For any fixed low table w and any candidate mismatch set S(w) chosen from w (or from a circuit description of w) alone, if every z in Z={0,1}^N minus SIZE(s2) must disagree with w somewhere in S(w), then all 2^(N-|S(w)|) completions matching w on S(w) lie in SIZE(s2). Hence |S(w)|>=N-log2|SIZE(s2)|=N-o(N) in the OPS range. This extends fixed-coordinate cylinder counting to row-dependent but nonadaptive samples. It does not constrain Bob-dependent adaptive rectangle-DAG routing or imply a graph-size lower bound. See bridge C-168.

## C-170 - One-switch protocols need exponentially many frontier states

For a fixed-order one-switch mismatch DAG, if Alice sends first, a message class A must have a common bit pattern on every coordinate that Bob's suffix can output. Correctness for all high z forces these coordinates to number at least N-log2|SIZE(s2)|, so A has Hamming diameter at most log2|SIZE(s2)|. The C-80 block-constant low code has 2^Theta(s1) rows at distance Theta(N/s1), exceeding this diameter for fixed beta<1/2. Hence there are at least 2^Theta(s1) Alice frontier states.

If Bob sends first, each message class B subset Z must be constant on an output-coordinate set S whose pattern is avoided by every low row. Point-indicator circuits realize every pattern on at most t=floor(s1/(C n)) coordinates, so |S|>t. Each B is therefore contained in a cylinder of size at most 2^(N-t-1), forcing at least (1-o(1))2^(t+1)=2^Omega(s1/n) Bob frontier states to cover Z. These bounds allow arbitrary shared suffix DAGs but assume no return to the sender after the switch. Repeatedly alternating rect-DAGs are not bounded; no rho_prom or P-vs-NP consequence follows. See bridge Ã‚Â§96.

## C-171 - A fixed menu of low-fiber crossing pairs is nearly quadratic

Define Fib(w,z) to output {i,j} with w_i=w_j and z_i!=z_j. It is total on Y x Z because otherwise z is a unary function of w and has circuit size at most s1+O(1). For a fixed candidate-label graph G on table coordinates, retain edges whose endpoints have equal w-bit. If z is constant on the components of this retained graph, no menu edge is valid. Since the menu must work for every high z, the 2^c component-constant tables must all lie in SIZE(s2), so c<=ell=log|SIZE(s2)|.

For every affine flat H of size m with 2ell<=m<4ell, the table 1_H is in SIZE(s1) for large n. The retained graph contains G[H], whose component count is at least m-e_G(H); hence every such flat must span at least m-ell edges of G. A random affine flat contains any fixed edge with probability m(m-1)/(N(N-1)), giving
|E(G)| >= (m-ell)N(N-1)/(m(m-1)) = Omega(N^2/ell) = Omega(N^(2-beta)/n).
Any rect-DAG for Fib has at least this many distinct output labels.

This is not a C-75 lower bound. Fib leaves refine to a signed mismatch with O(1) extra states, but the reverse construction from mismatch needs up to O(N^2) state copies to remember three output labels; the resulting inequality is too lossy. C-171 closes only the nonadaptive fixed-pair-menu shortcut and records a precise transfer failure. See bridge Ã‚Â§97.

### C-172 - Global-cylinder state constraint
For every valid rect-DAG state v with output-coordinate set K_v, row projection P_v=pi_{K_v}(A_v), and high-column set B_v,

    |Z minus B_v| >= max(0, |P_v|*2^(N-|K_v|)-|SIZE(s2)|).

Proof: the |P_v| full truth-table cylinders are disjoint; a high table in one cannot be in B_v, since a row realizing that pattern agrees with it on every descendant output coordinate. At most |SIZE(s2)| tables across their union are non-high. At the root this yields |pi_K(Y)|2^(N-|K|)<=|SIZE(s2)|. Low point-minterm patterns imply |K|>=N+Theta(s1/n)-log|SIZE(s2)|. This sharpens C-129 but remains a local bound and does not imply superlinear DAG size.

### C-173 - Rect-DL model boundary
A rect-DAG with S nodes induces a multi-output list of at most S valid leaf rectangles. Since the signed mismatch rectangles themselves give a 2N-term list, this relaxation cannot prove S_rect>2N. The reverse simulation from a rectangle list is not free: testing A x B uses separate Alice/Bob checks, and the combined failure set (A^c x Y) union (A x B^c) is generally nonrectangular. The 2025 Rect-DL hierarchy concerns Boolean output alternation, not protocol owner switches. Direct transfer retired; no C-75 lower bound.

### C-174 - Forced output projections are too small for the Rect-DL route
If h(i,b) is constant across all valid outputs for every pair in a subpromise, then the induced bit is 1 exactly on the union of the mismatch rectangles whose labels have h=1. There are at most 2N such rectangles. Thus its Rect-DL length is <=2N and cannot prove the superlinear rect-DAG target. Sign-only projections reduce to Hamming-weight comparison after fixed bit flips. Coordinate-block projections induce a complete bipartite distance-one relation in block Hamming space; if both sides have at least two patterns, the differing block is fixed or the only variable case is a 2x2 square. O-132 is closed as a decision-list-size transfer, not as a claim that all output-bit DAGs are easy.

### C-175 - Owner-sensitive conflict cylinders and explicit overlap
For C_v={z: exists w in A_v with z|K_v=w|K_v}, correctness gives B_v intersect C_v=empty. Alice-owned splits have C_v subseteq C_0 union C_1; Bob-owned splits have C_v subseteq C_0 intersect C_1. These set laws are exact but not additive. In the C-80 block-constant subpromise, choose m=Theta(s1/n) prefix blocks of size L=N/m. The block-constant family is low, and for beta<1/2 there are more than M2 tables with exactly one mixed block, so a high such table exists. The O(N)-state scan router uses one state per candidate block. For every j>=2 its column side has size at most 2^(N-L+1), so that state excludes (1-o(1))|Z| high columns. Summing C-172 exclusions therefore overcounts by Omega(m) in an O(N) DAG. A successful global potential must be path-weighted or conditional on the parent column set.

### C-176 - Parent-conditioned cross-conflict does not force DAG size
For a Bob split u -> v0,v1 with column partition B0,B1 and descendant conflict sets C0,C1, count a path charge when it takes vi but z lies in C_(1-i). The expected total charge is at most expected path length and hence at most S_rect. It can nevertheless be zero on a valid C-80 block-router pair: choose a high z mixed on every block, with its first two bits opposite the low row's first-block constant bit, and choose z high by the M2 counting bound. The path takes the mixed-block branch and then immediately outputs the first-coordinate mismatch, avoiding both sibling conflicts. Thus a parent-conditioned conflict mass has no pointwise lower bound and does not establish S_rect > N. The remaining problem is state-merge non-shareability for full residual rectangles, not conflict volume. No rho or P-vs-NP bound follows.

### C-177 - Gap local-PRG calculation in a restricted model
For a total separator H accepting SIZE(s1) and rejecting the high side Z=SIZE(s2)^c, uniform acceptance is at most M2/2^N, while any generator whose outputs all have circuit size <=s1 is accepted with probability 1. Hence a PRG that fools H with error <1-M2/2^N must have output locality >s1. The CLKM local PRG for general branching programs has locality S^(1/2)2^(O(sqrt(log S))); substituting gives S>=s1^(2-o(1))=N^(2beta-o(1)). For every sufficiently small beta<1/2 this is o(N), weaker than the existing N-o(N) standard-DAG floor. The theorem is for standard branching programs; no polynomial simulation from C-75 rect-DAG/unrestricted separator circuits is established. This closes the CLKM transfer as a C-75 lower-bound route. No rho or P-vs-NP consequence follows.


### C-178 - Sparse-envelope normal form for the shared-DAG target
Let Y=SIZE(s1), Z={0,1}^N minus SIZE(s2), and M2=|SIZE(s2)|. A Boolean separator H for (Y,Z) is exactly a circuit whose accepting set A satisfies Y subseteq A subseteq SIZE(s2): the first inclusion is completeness, and the second follows because every table outside SIZE(s2) is in Z and must be rejected. Conversely every such sparse envelope gives a valid separator. Therefore its minimum circuit size SepCirc(Y,Z) obeys SepCirc(Y,Z)=Theta(S_rect(Mis_Y,Z)) by the established Sokolov circuit/rect-DAG correspondence.

With D the descriptions of circuits of size at most s1 and V(d,x) the predicate TT(C_d)=x, the exact low-class predicate is the existential projection chi_1(x)=exists d in D: V(d,x). A universal circuit computes V(d,x) while d is an input, but it does not compute this projection. Directly OR-ing one N-literal equality test per description costs O(N|D|) gates. Since |D|<=2^(O(s1 log(s1+n))) and s1=N^beta/(c n), this is N*2^(O(N^beta)), superpolynomial for fixed beta>0. It is an explicit enumeration upper bound, not a lower bound against alternating DAGs.

Alice can send d using O(s1 log(s1+n)) bits; Bob locally computes TT(C_d), scans against z, and returns a mismatch coordinate using O(log N) more bits. This proves only low communication. The one-switch DAG has an exponential description frontier (C-170); description-space relabeling preserves rect-DAG size (C-162). The exact missing theorem is a small or large circuit for the existential projection's sparse envelope. A common suffix of t nodes for merged history rectangles must solve their reachable product hull, so a non-shareability proof must lower-bound the residual separator complexity of many hulls and charge these costs across states. At the root this is precisely SepCirc(Y,Z). C-178 clarifies Q132 but gives no lower bound on S_rect, rho_prom, or P versus NP.



### C-179 - Per-row affine-linear fingerprints have rank N-o(N)
Fix w in Y and an affine map L_w(x)=A_w x+b_w from F_2^N to F_2^r. If L_w(z) differs from L_w(w) for every z in Z={0,1}^N minus SIZE(s2), then the collision set w+ker(A_w) contains no high table and is therefore a subset of SIZE(s2). Since this coset has 2^(N-rank(A_w)) elements, 2^(N-rank(A_w))<=M2, giving rank(A_w)>=N-log2(M2) and r>=N-log2(M2). At OPS parameters log2(M2)=O(N^beta n)=o(N), so even a row-dependent one-shot parity fingerprint requires N-o(N) independent bits. This strictly generalizes the coordinate-only sample bound C-168. It applies only when sketch equality itself is forbidden on every low/high pair; it does not cover adaptive or nonlinear rect-DAGs, and it does not produce a mismatch output. No S_rect, rho_prom, or P-vs-NP lower bound follows.



### C-180 - Adaptive parity decision-tree depth lower bound
Let T be a deterministic decision tree for a separator H of Y=SIZE(s1) from Z={0,1}^N minus SIZE(s2), where every query is an affine linear form over F_2 and query choice may depend on earlier answers. Fix w in Y and let t be its path length. The queried answers define a nonempty affine subspace C_w of dimension at least N-t; every table in C_w follows the same path and receives H=1. Correctness forces C_w subseteq SIZE(s2), so 2^(N-t)<=M2 and t>=N-log2(M2)=N-o(N). This rules out shallow adaptive parity decision trees. It does not lower-bound a DAG with merged contexts, and depth N-o(N) is consistent with O(N) vertices. No S_rect or rho_prom consequence follows.



### C-181 - Gap transfer of the STACS 2021 branching-program local PRG
For a size-S separator H of SIZE(s1) versus the complement of SIZE(s2), uniform acceptance is at most M2/2^N=2^(-N+o(N)), while any local generator output of table circuit complexity at most s1 is accepted with probability 1. Cheraghchi-Hirahara-Myrisiotis-Yoshida's local generator against nondeterministic, co-nondeterministic, and parity branching programs has locality lambda(S)=S^(2/3+o(1). Consequently any separator in a fooled BP model has S>=s1^(3/2-o(1))=N^(3beta/2-o(1)). This is sublinear throughout OPS's required beta<1/2 range. Their read-once co-nondeterministic HSG has locality about sqrt(N) up to polylog factors and likewise does not apply at small beta. This is a promise-gap extension in restricted BP models, not a C-75 rect-DAG/circuit lower bound. Source: https://drops.dagstuhl.de/storage/00lipics/lipics-vol187-stacs2021/LIPIcs.STACS.2021.23/LIPIcs.STACS.2021.23.pdf. No rho or P-vs-NP consequence follows.


## C-182 - One output fiber contains a dense mismatch set

**Statement.** In the OPS regime s1=o(s2), the output wire partitions the coordinates into at most two fibers F_b={x:w(x)=b}. Let h be the majority z-value on each fiber. The low circuit for w plus a two-entry lookup computes h with size s1+O(1)=o(s2). If h differs from z at r positions, point-minterm patching computes z with size s1+O(1)+O(rn), so z high forces r=Omega(s2/n). One fiber has minority count Omega(s2/n); it is mixed and, since w is constant there, contains at least that many w/z mismatches. Thus every low/high pair has a circuit-dependent mixed output fiber with Omega(s2/n) mismatches.

**Status.** PROJECT-PROVED as a parameterized corollary of the circuit lookup and point-minterm patching arguments. It is a local witness lemma only.

**Proof location / dependencies.** Research bridge C-182; gate-signature factorization C-115 and low/high patching-distance lemma C-49.

**Counterexamples / scope.** This does not identify the cell jointly or uniformly across low circuits. In a fully merged, unfiltered one-state-per-stage scanner, a late continuation hull contains a high pair mismatching at the skipped coordinate and matching all later coordinates; filtered-context or coordinate-revisiting routers are not ruled out. No arbitrary rect-DAG, fusion-cover, or P-vs-NP lower bound follows.


## C-183 - The mixed output-fiber label is not a rectangle predicate

Choose three addresses p1,p2,p3. Let wA be 0 exactly on {p1,p2} and 1 elsewhere; let wB be 0 exactly on {p1,p3} and 1 elsewhere. These rows have O(n)-size circuits. Since 2^(N-3)>|SIZE(s2)|, choose high completions z0,z1 with restrictions (0,0,1) and (0,1,0), respectively. Define M0(w,z)=1 iff z is nonconstant on the entire zero-output fiber of w. Its promise-domain matrix is [[0,1],[1,0]]. Therefore the two valid pairs cannot form one product rectangle: their product hull contains the invalid diagonal pairs.

This proves that the C-182 witness fiber cannot be selected by one rectangle-local branch in the direct scanner architecture. It does not rule out multiple rectangles, bounded alternation, or an arbitrary rect-DAG, and gives no superlinear lower bound on S_rect or rho_prom. Full proof: bridge section 109.

## C-184 - Extension complexity is conserved across low-defined fibers

For w in SIZE(s1), let F_b={x:w(x)=b}, and let e_b be the minimum circuit size of any total circuit agreeing with z on F_b. A one-bit multiplexer combines the two extensions with a circuit for w, so CC(z)<=CC(w)+e_0+e_1+O(1). Therefore every z outside SIZE(s2) forces e_0+e_1>s2-s1-O(1), and one fiber has extension complexity at least (1/2-o(1))s2 in the OPS regime. If r_b is the minority count of z on that fiber, patching a constant at those points gives e_b=O(1+r_b n), so r_b=Omega(s2/n). The same fiber is both extension-hard and mismatch-dense.

For any k circuit-computable predicates of total size a, the 2^k cell extensions satisfy CC(z)<=a+sum_u e_u+O(k 2^k). This is a circuit-composition chain rule. It proves a hard residual trace exists but does not select it from either party's input or lower-bound a rect-DAG. See bridge section 110.

## C-185 - C-121 defeats a pointwise extension-hardness potential

C-184 forces a hard output-fiber extension for every low/high pair. On the C-121 structured subpromise, however, a fixed common partition has all low rows cell-constant, every high table is mixed on some cell, and the resulting mismatch rect-DAG has O(N) vertices. Thus large pairwise extension complexity coexists with a linear shared DAG. A lower-bound potential must capture cross-pair variation and state addressability, not only residual hardness magnitude. This is a route filter; the full low-circuit class has no such common coarse partition. See bridge section 111.
## C-186 - Common-partition covers need many contexts for sparse low rows

Let Y_r contain all r-point-indicator truth tables, with rn=O(s1). A family of rows constant on a fixed partition with m cells can contain at most sum_{i=0}^r binom(m,i) members of Y_r, since each support must be a union of at most r cells. Thus a cover of Y_r by T such partition families needs T>=binom(N,r)/sum_{i=0}^r binom(m,i), which is at least (N/(e m))^r for m>=r and at least (N/(2r))^r for m<r. If m=O(s2)=o(N), this is superpolynomial at the OPS parameters. Therefore a small menu of unfiltered C-121 common-partition routers cannot cover even the sparse low subfamily. This is architecture-specific; arbitrary DAGs can filter columns or share suffixes. Full proof: bridge section 112.

## C-187 - Fixed-center Hamming balls have linear-size mismatch DAGs

Fix u with CC(u)<=s1 and integer R such that s1+O(Rn)<s2. Patching u at at most R addresses shows every z outside SIZE(s2) has d_H(z,u)>R. The N-bit threshold function H(v)=1[d_H(v,u)<=R] has an O(N)-gate Boolean circuit: hardwire u by choosing each input or its negation, compute population count with O(N) full-adder compressors, and compare with R. Therefore H separates A(u,R)={w in SIZE(s1):d_H(w,u)<=R} from all high tables, and the Boolean-circuit/rect-DAG correspondence gives S_rect(A(u,R),Z)=O(N).

Taking u=0 and R>=r with Rn=O(s2) handles the whole sparse point-indicator family Y_r from C-186 in one linear-size DAG whenever rn=O(s1)=o(s2). Thus C-186's superpolynomial context count is specific to unfiltered common-partition routers. A C-80 code with 2^{Theta(s1)} words and minimum distance Theta(N/s1) requires exponentially many fixed-center balls in the beta<1/2 OPS regime because the safe radius is O(s2/n); this is only a static-menu lower bound. The perturbation inequality is already present in C-49/C-136 and is stated explicitly by Krinkin (arXiv:2603.09379); C-187's value is the subpromise separator application, not a new circuit-sensitivity theorem. It gives no lower bound on arbitrary alternating rect-DAGs or rho_prom and no P-vs-NP consequence. Full proof and prior-art boundary: bridge section 113.

## C-188 - Approximate learning reframes center selection but gives no reverse lower bound

Let \(\mathcal N_R(Y)=\{v:\exists w\in Y,\ d_H(v,w)\le R\}\). Patching gives \(Y\subseteq\mathcal N_R(Y)\subseteq\mathrm{SIZE}(s_2)\) for \(R=O((s_2-s_1)/n)\), so membership is a canonical sparse-envelope separator if its existential circuit-description projection can be computed. More generally, choose a hypothesis budget t and error epsilon with t+O(epsilon N n)<s2. Every project-high table is then a NO instance of approximate MCSP[(s1,0),(t,epsilon)], because an epsilon-close t-circuit could be patched to compute it below s2.

Oliveira et al., ITCS 2020, Lemma 34, show that a non-adaptive membership-query learner for SIZE(s1), outputting t-size hypotheses to error epsilon/2, yields an approximate-MCSP circuit of size O(N*poly(t/epsilon)); hence such a learner gives an upper bound for the project promise. For t=s1 and OPS parameters, epsilon=Theta(N^(beta-1)/n) and t/epsilon=Theta(N), so the stated circuit loss is N*poly(N), not a near-linear bound. The direction cannot be reversed: a learner lower bound does not imply an approximate-MCSP or project-separator lower bound under Lemma 34. The paper's converse-style result assumes additional reductions/NP-completeness not established here. This is a model connection and route filter, not a DAG or rho lower bound. Full audit: bridge section 114.

## C-196 - Q-output exits and tail support obey a local product-hull tradeoff

Fix C-190's coordinate set Q. At a rect-DAG state v with rectangle A_v x B_v, let K_v be descendant output coordinates, P_v=K_v intersect Q, and T_v=K_v setminus Q. For signatures sigma,tau with nonempty row and column fibers, if their projections on T_v overlap, then sigma and tau must differ on at least one coordinate of P_v. Otherwise a pair from the overlapping fibers agrees on every descendant output coordinate, violating correctness. Thus P_v must hit each signature-difference set whose tail projections overlap; diagonal signature fibers must be separated entirely by the tail.

If r_v signatures meet both A_v and B_v, and t_v=|T_v|, then

    |Z minus B_v| >= max(0, r_v*2^(N-|Q|-t_v)-M2),  M2=|SIZE(s2)|.

For each diagonal signature choose w_sigma in A_v. All high tables agreeing with w_sigma on Q union T_v are excluded from B_v, and the cylinders are disjoint across signatures.

Status and limit: proved local state invariant. It couples off-diagonal Q exits to tail-overlap and residual contexts, but it does not charge excluded columns across states; C-130 gives overlap, and C-80/C-160 remain easy-DAG counterchecks. No new bound on rect-DAG size, rho, or P versus NP follows. See bridge section 122 and O-141.

## C-198 - Partial-monotone KW lifting is compatible but lacks a high-image reduction

One-hot dual-rail encodings put every N-bit table at Hamming weight N, so distinct low/high encodings are incomparable. Assigning 1 to encoded low tables and 0 to encoded high tables gives a monotone-consistent partial Boolean function. Its monotone KW outputs are exactly signed mismatches. Thus a C-75 rect-DAG is the restricted partial monotone KW DAG. If a lifted CSP search relation reduces answer-preservingly to C-75, inverse images of rectangles give a same-size DAG and the CCC 2025 colourful-sunflower lower bound transfers without size loss. No such reduction is known; the high-table requirement on every Bob image and validity of every mismatch output are the unresolved conditions. Any affine-coset low/high subpromise is easy: a separating parity check gives an O(N)-gate separator. Status: precise route interface and route filter only; no new S_rect, rho, or P-vs-NP lower bound. Details and source: bridge Ã‚Â§123.



## C-199 - Dense Bob-column deletion preserves triangle-DAG lifting up to constants

For Search(F) composed with IND_m^r, take any Bob subset B with omitted density eta<1/4. The proof of the 2024 triangle-DAG lifting theorem adapts by initializing the accumulated error-column set with B^c. After deleting whole columns and earlier error rows/columns, states remain triangles; on retained columns the restricted protocol still covers each parent and its leaves are correct. The Triangle Lemma's per-state bounds are unchanged. With protocol-size constant 1/4 in place of 1/2, accumulated protocol error is <1/4, so together with eta<1/4 at least half the root columns remain and the source Full Image Lemma applies. Thus the same width-w resolution consequence holds with only a constant-factor lower-bound loss.

For the OPS promise, |SIZE(s2)|/2^N=2^(-N+o(N)); hence the high-table column set is dense enough. This removes the requirement that a reduction explicitly generate only high tables. It does not solve the answer-preserving map: every oriented mismatch must be a valid lifted-search output, and the low-table family must not have a simple linear-size membership test. A blockwise pointer encoding fails because its range is recognized in O(N) gates. Status: proved proof adaptation / route filter only; no C-75 lower bound. Details: bridge Ã‚Â§124; primary source ECCC 2024 Report 185, Theorem 2.11.



## C-200 - The standard colourful-sunflower image family has a near-linear separator
In the CCC 2025 cPHP-to-clique-colouring reduction, Alice's graph is exactly one k-clique on one selected vertex in each of k parts, with every other edge absent. For an adjacency table on V=mk vertices (N=binom(V,2) input bits), a Boolean circuit computes all degrees and accepts iff exactly one vertex per part has degree k-1 and every other vertex has degree 0. The active vertices then form a k-clique. This costs O(V^2 log V)=O(N log N) gates. It accepts every Alice image and rejects every c-colourable Bob graph; restricting Bob graphs further to high-circuit-complexity tables does not change that. Hence the signed-mismatch subrelation on these images has an O(N logN) rect-DAG, below the project threshold. In addition, the mKW reduction decodes only Alice-present/Bob-absent edges, whereas signed mismatch also permits the reverse orientation. The unmodified reduction cannot transfer a C-75 lower bound. Status: this concrete lifting image route is closed; no target lower bound follows. Details: bridge Ã‚Â§125.

## C-201 - Corrected exponent in the dense-column lifting corollary
Theorem 2.11 of ECCC Report 185 states the size threshold as (1/2)m^((1-delta)w), not (1/2)m^((1-delta)w/2). Its near-tightness discussion explicitly obtains m^(.99w) at delta=1/120. Starting the published bottom-up error removal with omitted Bob columns and using size cap (1/4)m^((1-delta)w) leaves at least half the root columns when the omitted density is below 1/4; the source row and column error bounds then give the same width-w resolution extraction. Thus the restricted-domain triangle-DAG lower bound remains Omega(m^((1-delta)w)). This corrects C-199's exponent and improves its quantitative interface. It still supplies no C-75 reduction or target lower bound. Source and proof audit: bridge C-201.

## C-202 - Unique-output Index search has prohibitive mismatch-decoder cost
Let F_v contain one width-v clause C_a falsified exactly by each assignment a in {0,1}^v. For Search(F_v) composed with IND_m^v, each input pair has unique answer C_z where z_i=y_(i,x_i). Under uniform inputs, every product rectangle contained in a fixed-answer fiber has measure at most (1/(2m))^v: if S_i is the set of addresses used by the row side in coordinate i, the row density is at most product_i |S_i|/m and the column side fixes all corresponding y_(i,j), giving factor 2^(-sum_i |S_i|). Therefore a relation-preserving decoder for each full C-75 mismatch-type pullback, using at most K output-labelled rectangles per type, requires K>= (1-eta)(2m)^v/(2N)=Omega(m^(v-1)) when N=mv and Bob omits only eta<1/4. For v=16,w=15,delta=0.1, C-201 gives source lifting lower bound Omega(m^13.5), below the decoder cost Omega(m^15), so this source cannot transfer the bound after refinement. A fixed-label decoder is impossible. This does not rule out answer-rich search relations or direct encodings. No target lower bound follows. Details: bridge C-202.

## C-203 - Constant-degree cPHP passes the decoder-cost exponent screen

For the CCC 2025 cPHP source on a constant-degree expander with k left vertices and c=alpha k right vertices, Theorem 28 gives width W=Omega(k), and Theorem 11 gives lifted triangle-DAG size L=(m/(A d W log(mk)))^W. With target table length N=Theta(mk), C-164 forces any per-signed-mismatch decoder with r output-labelled rectangle leaves to use r=Omega(Delta m^2d/N)=Omega(d N^(1+beta)/(k^2 logN)) when Delta=Theta(N^beta/logN) and the omitted Bob density is bounded away from one. The compiler threshold is T=N^(3+3epsilon)/logN, so T r_min=Theta(d N^(4+3epsilon+beta)/(k^2(logN)^2)). For fixed k,d,W and W>4+3epsilon+beta, L/(T r_min) grows; hence the known minimum decoder cost does not rule out this source.

This is only a parameter feasibility calculation. It does not supply a decoder upper bound r<L/T or partywise maps into SIZE(s1) x SIZE(s2)^c. C-204 now proves the needed dense-column robustness for the CCC colourful-sunflower lifting proof at the OPS deletion density. The standard cPHP-to-clique-colouring image is closed by C-200. No C-75, rho, or P-vs-NP lower bound follows. Primary source and derivation: bridge C-203/C-204; [CCC 2025 paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol339/ccc2025/html/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.html).

## C-204 - Colourful-sunflower lifting survives the OPS high-table restriction

Let S:Sigma^n -> O have subcube-DAG width W. The CCC 2025 proof extends to a Bob column set B of density 1-eta, when W log(mn)=o(mn) and eta=2^(-Theta(mn)+o(mn)): a triangle-DAG solving the lifted relation on [m]^n x B still has size Omega((m/(A'|Sigma|W log(mn)))^W), for an adjusted absolute constant A'. The proof adaptation uses the paper's Full Range Lemma, which is already stated for arbitrary column subsets Y above a density threshold, plus its triangle-error union bound. The OPS complement of SIZE(s2) has density 2^(-N+o(N)); with N=Theta(mn) and fixed-width cPHP parameters, its deletion is below the local 2^(-Theta(W log(mn))) error scale, and the accumulated extra error remains negligible. Details and hypotheses: bridge C-204; primary [CCC 2025 paper, Lemma 16 and Claim 17](https://drops.dagstuhl.de/storage/00lipics/lipics-vol339/ccc2025/html/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.html).

This closes the dense-column robustness obligation for that parameter regime. It permits flattening a power-of-two-alphabet Bob array directly to all N-bit strings and restricting to high tables. It does not provide an Alice map into SIZE(s1), a decoder for both mismatch signs, or a decoder upper bound. No C-75/rho/P-vs-NP lower bound follows.

## C-205 - Raw cPHP flattening forces a source-hard per-type decoder

Let beta flatten `[d]^(mk)` bijectively to N=mk log2(d) bits and restrict Bob to high tables. For any Alice map alpha, any bit coordinate i has a value b assumed by at least half of `[m]^k`; the opposite beta-bit slab, after high-table deletion, still has density `1/2-o(1)`. The corresponding signed mismatch type therefore contains a product subdomain `A x B` with Alice density at least 1/2 and Bob density at least 1/3.

The CCC 2025 lifting proof adapts to any such dense root rectangle: using its per-state row-error bound with a 1/8 protocol-size constant leaves at least 3/8 of the full Alice cube, which has blockwise min-entropy at least `log(m/8)`; accumulated Bob errors are `o(1)`, leaving constant column density. Thus a type-only rect-DAG decoder that is correct on every pair of that mismatch type must itself have size Omega(L), where L is the lifted cPHP lower-bound scale in C-203. Copying a type-only decoder at each target sink yields only `L <= O(SD)` with `D=Omega(L)`, hence no superlinear target-DAG lower bound.

This is a proof adaptation of the CCC 2025 full-version lifting argument, not a printed theorem. It closes only raw bijective Bob flattening with a decoder depending solely on mismatch type. A decoder conditioned on the target sink rectangle or a non-raw Bob encoding remains open; neither is handled by the per-type calculation. No C-75, rho, or P-vs-NP lower bound follows. Full proof and source audit: bridge C-205.

## C-206 - Sparse row sides contain low-codimension high-entropy slices

For every nonempty `A subseteq [m]^k` of density `rho` and every `delta in (0,1)`, repeatedly condition on a coordinate pattern whose probability under the current uniform slice exceeds `m^(-delta |I|)`. Each conditioning step fixes `|I|` more coordinates and increases the slice density by a factor greater than `m^((1-delta)|I|)`. The process terminates at a slice with blockwise min-entropy `delta log m` after fixing

    t < log(1/rho)/((1-delta)log m)

coordinates. Thus a row side of density at least `1/S` has a structured witness after `O(log_m S)` address fixes. For polynomial-size target DAGs with fixed source parameters, this is a constant number of addresses.

For complete cPHP with `2c` pigeons and `c` holes, a fixed injective prefix of `t<c` selected values leaves an online-matching hard residual problem of width `Omega(c-t)`; a colliding prefix is an immediate witness. Partitioning Bob's columns by the `c^t` prefix-value patterns gives a local hard/easy dichotomy. The gap is global: sink row slices are not a cover, and Bob sink sets may concentrate on collision patterns. No way to sum these contexts without overlap has been proved. This is a rigorous regularization lemma and route diagnostic, not a C-75 or P-vs-NP lower bound. Details: bridge C-206/O-145.

### C-207 - Primary-source audit of the shared-DAG normal form

Sokolov's Boolean communication game has an acyclic graph of outdegree at most two; every valid node is a product rectangle, its children cover the parent, and its valid leaves output a mismatch. On the partial promise `Y x Z`, the minimum size is Theta the minimum circuit size of any separator `h(Y)=1, h(Z)=0`, by the rectangle-to-circuit induction and restriction of the KW game for `h`. If Alice instead receives a circuit description `d` with `G(d)=w`, a surjection/section argument preserves minimum graph size exactly. Short descriptions can reduce communication bits but do not independently compress shared states.

Quantitative chain: `rho_prom=q=D_circ_cap`; `D_cap<=q^2`; `S_rect=O(q^3/log q)` by the best recorded compiler; and `rho_prom=O(S_rect)` in reverse. The requested `rho_prom>N^(1+epsilon)` therefore needs `S_rect>N^(3+3epsilon)/log N` through this route. Parity proves an artificial tree-vs-DAG gap but supplies no C-75 transfer. Tier 4 model reconciliation is confirmed; O-141/O-133 remain open. No new lower bound follows. Primary sources and details: research bridge C-207.

### C-208 - Local capacity is equivalent to disjoint output projections

In a valid acyclic rect-DAG state `v`, let `K_v` be the descendant mismatch-coordinate set. Since every valid pair at v has a valid path to a leaf, correctness forces `pi_Kv(A_v) intersect pi_Kv(B_v)=empty`. Conversely, disjoint projections ensure every pair has some mismatch in K_v, though they do not furnish a binary rectangle routing. Hence `|B_v|/2^N <= 1-|pi_Kv(A_v)|/2^|K_v|`. The local density bound is universal to mismatch search and contains no internal use of the SIZE promise. At the root, excluding high completions recovers C-172's near-full label-support bound. Internal excluded-column sets overlap; C-80/C-175 refute raw summation. The remaining O-141 target is parent-conditioned state-merging/routing, not another per-state density deficit. No C-75 lower bound.

### C-209 - Product-hull law for a shared state

For each root-to-v path h, its feasible history inputs form a rectangle `H_h=A_h x B_h` contained in the local state rectangle `A_v x B_v`. If several histories share v, their full product hull `(union_h A_h) x (union_h B_h)` is still inside v and must be solved by its suffix. Hence the descendant output-coordinate projections of the union of all history row sides and union of all history column sides are disjoint. Equivalently, every row-history projection must be disjoint from every column-history projection, including cross-histories. This is exact and follows from product-rectangle semantics; it does not itself lower-bound graph size. C-80 remains a required O(N) countercheck, and C-191's Q-output exits can still permit merging. The missing theorem is an amortized lower bound on residual separator costs for these hulls. See bridge C-209/O-141.

### C-210 - Rank-lifting gives an explicit acyclicization

For rule i, define `tau_i(v)` as its first least-fixed-point activation round, or infinity. For `r=1,...,q`, the rectangle `R_(i,r)={w in Y:tau_i(w)<=r} x {z in Z:tau_i(z)=infinity}` is a valid rank-bounded state. A successful Q's root is covered by `R_(i,q)` for its empty-intersection rules. At `R_(i,r)`, choose a side of i absent from z's closure; w's membership in that side has a literal seed, giving a signed-mismatch leaf, or a prior rule j with `tau_j(w)<tau_i(w)<=r`; since `T_j` is contained in the absent side, j is inactive on z and the transition reaches `R_(j,r-1)`. This proves a rank-layered acyclic multiway protocol with q^2 rule/rank states plus O(N) output leaves.

The state count hides fan-out: each layered state has up to O(q+N) support choices, for O(q^2(q+N)) arcs. At OPS parameters q>=N/2, the edge count is O(q^3); binary-outdegree conversion cannot be claimed to cost only q^2. The q states themselves give a ranked cyclic protocol only if pair-dependent strict rank decrease is part of the model. The existing O(q^3/log q) ordinary rect-DAG compiler remains best recorded. This is a transformation/model clarification, not a size lower bound; O-141 remains open. Details: bridge C-210.

### C-211 - Pairwise mismatch supports admit a near-linear static hitting family

Assuming `s2/s1` grows and the OPS patching parameters apply, any `w in SIZE(s1)` and `z outside SIZE(s2)` differ on at least `d=Omega(s2/n)` positions: patching the r differences with point minterms costs `s1+O(rn)`. For `k=ceil(N/d)`, a random k-subset misses a fixed d-set with probability at most e^-1. Taking `R=ceil(2d ln(eN/d))` independent samples and union-bounding over at most `(eN/d)^d` d-sets yields a family hitting every pairwise mismatch set, with total incidences `Rk=O(N log N)`.

This is not a rect-DAG or fusion cover. Ã¢â‚¬Å“Q contains a mismatchÃ¢â‚¬Â is generally not a rectangle (two-bit off-diagonal witness), and the sample index cannot be selected by a single product state. A scan confined to one sample that discards its tested prefix is blocked by product-hull cross-pairs; a composite protocol using other samples or revisiting old coordinates is not ruled out. Thus this kills no general DAG and gives no lower bound; it identifies routing/selection, not output-support, as the remaining issue. See bridge C-211/O-141.


## C-212 - Sparse interpolation and upgraded local bounds

**Status:** proved. For every r-point subset of the n-bit address cube, shared block decoders give an exact indicator circuit of size `O(n+r*n/log(r+1))`. Therefore the low class shatters every fixed set of `Theta(s1)` table coordinates, and sparse patching raises the OPS low/high Hamming gap to `Omega(s2)`. This supersedes the weaker point-minterm quantitative bounds in C-133, C-135 through C-137, C-170, C-172, C-189, C-191, C-195, and C-211 where applicable. The proof assumes the project's standard fan-in-two Boolean basis with free fan-out and fixed `0<beta<1`.

**Limit:** the stronger numbers still concern fixed-order/one-switch architectures, local certificates/routers, or rectangle covers constrained to an equality/triangle state. Product-hull-safe global aggregation is open. No arbitrary rect-DAG, fusion-cover, or P-vs-NP bound follows. See bridge C-212.


## C-213 - Universal cyclic rectangle scan; fusion transfer fails

**Status:** proved model counterexample. For every disjoint `A,B subseteq {0,1}^N`, a cyclic product-rectangle protocol with N scan states, 2N one-bit selector states, and 2N output leaves solves mismatch in at most N scan steps from any scan state, under the specified strategy. The cycle revisits old coordinates and makes the full product hull of merged equal-prefix histories safe.

**Boundary:** the protocol is not acyclic and its party-local rectangle predicates are independent/free. A fusion rule instead generates a one-input activation set via the endpoint/support least-fixed-point equations; no small conversion from the cyclic scan to legal fusion pairs is known. Thus C-213 kills the broad cyclic-rectangle lower-bound target only. It does not give a small standard rect-DAG, a bound on `rho_prom`, or a P-vs-NP result. See bridge C-213; retain C-80/C-160 and O-141.

## C-214 Ã¢â‚¬â€ Exponential generic separation by counting native closure descriptions

For each q-rule fusion closure on an N-bit full-partition promise, the anchor recurrence is specified by two seed-literal subsets from a 2N-literal vocabulary per rule, two predecessor subsets of [q] per rule, and the empty-output subset. Thus at most 2^(4Nq+2q^2+q) Boolean functions are computed by q-rule systems. Counting over q<=2^(N/2-1) yields fewer than 2^(2^N) functions for large N. Therefore some Boolean partition has fusion-pair complexity Omega(2^(N/2)); its signed-mismatch relation nevertheless has the universal 5N-state cyclic rectangle protocol of C-213. This proves that arbitrary cyclic rectangle protocols do not admit a generic polynomial-overhead conversion to fusion closure.

**Limit:** the counted partition is existential and need not equal the actual SIZE(s1)/SIZE(s2)^c promise. The middle band of the actual promise leaves separator values unconstrained. No C-75, OPS, or P-vs-NP lower bound follows. Full proof: research/C75_SHARED_DAG_CONTINUATION_2026-09-27.md.

## C-215 - Q-exit overlap graph: proved local condition, unproved aggregation

**Status:** local lemma proved; global use not proved. At a rect-DAG state v, join low Q-signature sigma to high signature tau when their projections on the descendant tail-output set T_v overlap. Let P_v be the descendant Q-output set. Every such edge satisfies sigma|P_v != tau|P_v; otherwise a row and column witness agree on all descendant outputs. In particular, no diagonal edge is possible, and a complete bipartite overlap subgraph has disjoint P_v-projections on its two sides.

At the root, if fewer than N-|Q|-log2(M2) tail coordinates occur below the root, then fixing a low row's Q-signature and its values on those tail coordinates leaves more than M2 completions; one is high, creating a forbidden diagonal edge. Hence the root must expose at least N-|Q|-log2(M2) tail coordinates. A fixed overlap witness pair persists to the child it enters while it remains in the child's rectangle, but edge count is not monotone because tail support shrinks and row/column sides are filtered. No parent-conditioned flow or state lower bound follows. See research/C215_Q_EXIT_GRAPH_AUDIT_2026-09-27.md; O-141 stays open.

### C-216 Ã¢â‚¬â€ Statewise signature/column-deficit profile

**Status:** proved local inequality; aggregation fails. For each rect-DAG state `v`, let `r_v` count Q-signatures present on both sides, `t_v` be descendant tail-output support, and `Delta_v` be omitted high columns. Disjoint cylinders give `r_v*2^(N-|Q|-t_v)<=M2+Delta_v`. At the root this strengthens support by `log r_Q`; Alice transitions duplicate the deficit allowance and Bob transitions add `|Z|`, preventing a useful scalar global charge. This is not a superlinear DAG bound. See `research/C216_COLUMN_DEFICIT_PROFILE_2026-09-27.md`.

### C-217 Ã¢â‚¬â€ Fixed-order mismatch scans require exponential width

**Status:** proved for a restricted architecture only. Uniform shattering of `t=Theta(s1)` coordinates implies that, for every fixed coordinate order, every `j<=t` prefix has all `2^j` low patterns. Since `2^(N-j)>M2`, each pattern also has a high completion. In a scanner that cannot revisit passed coordinates, two distinct matched-prefix histories cannot merge: their product rectangle would contain a promised cross-pair whose mismatch is already behind the scan. Thus fixed-order scans need `2^(Theta(s1))` states. This rules out the direct universal coordinate-scan candidate, not arbitrary rect-DAGs. No `S_rect`, `rho_prom`, or P-vs-NP consequence. See `research/C217_ORDERED_SCAN_WIDTH_2026-09-27.md`.

**C-217 scope clarification:** the exponential-width theorem applies to fixed-order scans that halt immediately on the first mismatch. Deferred-output scans and general rect-DAGs are not covered. Do not cite it as an unrestricted C-75 lower bound.


## C-218 ? Distance?dimension slack and certificate bounds

**Status:** proved parameterized certificate and projection lemmas; no DAG transfer. For `0<gamma<beta`, put `Y'=SIZE(N^gamma) subset Y=SIZE(N^beta/(c n))` and keep `Z={CC>N^beta}`. Any separator for `(Y,Z)` also works for `(Y',Z)`, hence separator lower bounds for the smaller low side transfer upward. The resulting original-promise separator bound can be combined with the established cover-to-DAG compiler; no monotonicity claim for closure measures on different ground sets is needed. C-212 patching gives `d(Y',Z)=Omega(N^beta)`; circuit counting gives `log|Y'|=O(N^gamma n)`. Uniformly for every z in Z, sampling `m=ceil((N/d)(ln|Y'|+1))` coordinates and union-bounding over Y' proves a hitting certificate of size `O(N^(1-beta+gamma)n)=o(N)`. Also `VCdim(Y')<=log2|Y'|=o(d)`. For any fixed Q of size `2v`, `v=VCdim(Y')`, Sauer?Shelah leaves at least one quarter of patterns outside `pi_Q(Y')`; each missing-pattern cylinder has a high completion, and all pairs retain `Omega(d)` mismatches off Q.

**Limit:** certificates depend on z or certify only a fraction of columns; neither selects a mismatch coordinate in a product-rectangle DAG. No `S_rect`, `rho_prom`, or P-vs-NP lower bound follows. See `research/C218_DISTANCE_DIMENSION_CERTIFICATES_2026-09-27.md`; O-141 remains active.


**C-218-A restricted routing lemma:** proved. On any `Q` with `|Q|=2v`, `v=VCdim(Y')`, a fixed-order first-mismatch scan for `pi_Q(Y')` against its complement requires `2^(Theta(N^gamma))` states. The proof uses uniform shattering for low prefixes, Sauer-Shelah on each prefix slice to find a missing Q-completion, and `2^(N-|Q|)>|SIZE(s2)|` to lift it to a high table. Scope is only this scanner architecture; it does not apply to deferred-output/adaptive rect-DAGs. See C-218 report, section C-218-A.


## C-219 - Universal mismatch-certificate menu

**Status: proved certificate theorem; no separator-size consequence.** A probabilistic construction gives `L=O(N/H)` coordinate sets of size `m=O(NH/d)` such that every high table has at least `L/2` menu items separating it from every low table by margin `16H`, for `H=ln|SIZE(N^gamma)|` and low/high distance `d=Omega(N^beta)`. Conjoining projected robust-consistency predicates yields a separator, but no small circuit for those predicates is known. See `research/C219_UNIVERSAL_CERTIFICATE_MENU_2026-09-27.md`.

## C-220 - Shared-DAG exact boundary and model correction

**Status: proved transfer/model facts; no new actual-promise lower bound.** The C-75 signed-mismatch relation is exactly the promise-restricted Bit/KW relation. A rect-DAG and a Boolean separator are equivalent up to linear size (and an additive input-source term in the general size convention); in this OPS promise the separator depends on `N-o(N)` coordinates, so that term is absorbed. Description-space and table-space rect-DAG sizes are equal under truth-table pullback and a section. The best fusion transfers remain `rho_prom<=O(S_rect)` and `S_rect=O(q^3/log q)`. The local product-hull projection condition is proved, but no global state charge is known.

**Correction:** GGKS triangle states include all rectangles. Therefore `S_triangle<=S_rect`; a triangle-DAG lower bound would transfer to rect-DAGs. C-194 gives a universal `4N-1`-state triangle-DAG for signed mismatch on every disjoint promise, so the stronger model cannot supply a superlinear lower bound here. C-195's state expansion concerns only one protocol and is not a lower bound on alternative rect-DAGs. Full audit: `research/C220_SHARED_DAG_FRONTIER_2026-09-27.md`.


## C-221 - Seed-cut cover is only a linear feature bound

**Status: proved structural lemma; no superlinear consequence.** For a successful q-pair closure, its 2q seed clauses define a feature map `sigma_Q`. The least-fixed-point output is monotone in these features. Thus every low/high pair has a seed coordinate true on the low table and false on the high table; each clause's zero set is a subcube, giving an oriented subcube-cut cover. The minimum such cover lies in `[N-log2(M2),2N]`, the upper bound following from all signed literals. Therefore seed-feature separation alone cannot prove a superlinear q lower bound. The missing resource is the constrained positive closure readout. Full proof and O-141 update: `research/C221_SEED_FEATURE_VS_CLOSURE_READOUT_2026-09-27.md`.



## C-222 - Fixed universal signature menus are superpolynomial

**Status: proved architecture-specific obstruction; no general lower bound.** Every t-sparse point indicator for `t=Theta(N^beta/n)` is in `SIZE(s1)`. A K-cell signature factors such an indicator exactly when its support is a union of fibers; one partition represents at most `sum_{j<=t} binom(K,j)` supports. For `K<=N^beta`, the fraction is `2^(-Omega(N^beta))`, so any fixed menu covering all these low tables has `2^(Omega(N^beta))` members. This rules out universalizing C-115 by a polynomial menu, not adaptive selectors or arbitrary rect-DAGs. Full proof: `research/C222_FIXED_SIGNATURE_MENU_LOWER_BOUND_2026-09-27.md`.



**C-222-A scope correction.** The menu lower bound does not lower-bound adaptive selector circuit size. A bitonic sorting network extracts the support of a t-sparse indicator in `O(N log^3 N)` gates and outputs a short point-indicator circuit description. The sparse witness family therefore has an efficient adaptive selector even though every fixed menu needs `2^(Omega(N^beta))` items. Any selector hardness claim must address the full `SIZE(s1)` family. See section C-222-A of the C-222 report.


## C-223 - An explicit low-table selector yields a separator, with evaluation loss

**Status: proved one-way implication; no selector or DAG lower bound.** Suppose a Boolean circuit S on the N-bit truth table outputs a description of a circuit of size at most `s1`, and its output computes w exactly for every `w in SIZE(s1)`. Then evaluate the selected circuit at every one of the N addresses and compare with the corresponding input bit. This gives a separator for `SIZE(s1)` versus the complement of `SIZE(s2)` of size `O(size(S)+N s1 log(s1+n))`. At `s1=N^beta/(c n)`, the verification term is `O(N^(1+beta))` up to constants. Thus explicit circuit synthesis is sufficient for a separator but can be much more expensive than a near-linear DAG.

No converse is established: a separator only decides the promise and need not output a circuit for a low table. This is not an exact reduction to the classical MCSP search-to-decision question because the project uses a gap promise and leaves the medium band unconstrained. A general rect-DAG may route tables without synthesizing any circuit. Selector lower bounds therefore do not imply unrestricted DAG lower bounds without an additional reduction. Full proof and literature boundary: `research/C223_ADAPTIVE_SIGNATURE_SEARCH_MCSP_BOUND_2026-09-27.md`.


## C-224 - Approximate signature fibers trade error mass for within-fiber variation

Let C have size r and approximate a low table w on all but e addresses. Select k internal wire values from C, including its output, as a signature. For a high table z, let m count good addresses that disagree with the per-cell majority of z. A lookup on the signature followed by point-minterm corrections computes z with size `r+O(k*2^k+(e+m)n)`. Hence if `CC(z)>=s2`, then `r+O(k*2^k+(e+m)n)>=s2`; the precise forced mass is on the residual scale `(s2-r-c1*k*2^k)/(c2*n)`, and is `Omega(s2/n)` when `r+c1*k*2^k<=s2/2`. A mixed good cell contains x,y with same signature, w(x)=w(y), and z(x)Ã¢â€°Â z(y). This is a robust local extension of C-115, not a global DAG charge. Natural-property learning does not currently improve the C-75 route: the separator family is nonuniform absent a uniform constructor, and the cited theorem returns approximate learners rather than shared DAGs. O-141 and all transfer losses remain unchanged. Proof and scope: `research/C224_APPROXIMATE_FIBERS_NATURAL_PROPERTY_BOUNDARY_2026-09-27.md`.

## C-225 - One-cell concentration survives approximate signatures

Fix low w with `CC(w)<=s1` and an approximate circuit C of size r that agrees with w on at least N/2 positions. For any k-wire signature containing C's output, some good cell F has `|F|>=N/2^(k+1)`. If `|F|>A*s2*log(s2+n)` and `s1+r+O(k)<=s2/2`, count the completions `z_A=w xor 1_A` for A subseteq F. There are more than the number of tables of circuit size <s2, so one completion is high. Both endpoints w and `w xor 1_F` are low: the latter's circuit computes F using the exact test `C(x)=w(x)` and the signature pattern. The high completion is therefore nonconstant on F and, by point-minterm patching against both low endpoints, has `Omega(s2/n)` minority points in this one good cell. For any fixed beta in (0,1), choose `kappa<min(beta,1-beta)` and k=`floor(kappa*n)`; then the cell size exceeds the circuit-count threshold. This extends C-120 to approximate circuits and the full fixed-beta range. It falsifies mixed-cell-count charges, not arbitrary DAG lower bounds: the location F depends on w,C and the chosen high table. Full proof: `research/C225_APPROXIMATE_SIGNATURE_ONE_CELL_CONCENTRATION_2026-09-27.md`.

## C-226 - Fusion closure is alternating reachability, not an ordinary BP

For each rule i, the least activation equation is an AND of two sides, each an OR over seed literals and predecessor rules. This is exactly the least reachability winning set of a cyclic alternating program: universal choice of side, existential choice of support, infinite plays losing. The program uses O(q) states and O(q(N+q)) transitions. The q rule states therefore cannot be identified with q vertices of a standard acyclic rect-DAG or a one-path NBP. Activation witnesses are shared proof DAGs with two support obligations per node; unrolling may duplicate subproofs, while tracking the active/rank assignment generically takes 2^{O(q)} BP states.

From the local PRG/HSG for standard NBP/co-NBP models, a promise co-NBP separator between CC<=s1 and CC>s2 (both thresholds o(N/n)) must have size at least s1^{3/2-o(1)}: complement it, then it rejects all local low-circuit generator outputs and accepts almost all uniformly random high tables. At OPS parameters this is N^{3 beta/2-o(1)}, useful as a superlinear floor only for beta>2/3. This is an inference from the cited local-generator proof, not the paper's verbatim theorem. Since fusion closure is mapped only to alternating reachability, this BP lower bound gives no q bound. Full proof/scope: `research/C226_FUSION_CLOSURE_ALTERNATING_BP_BOUNDARY_2026-09-27.md`.


## C-227 - Native certificate grammar and splice-soundness condition

Each least-fixed-point activation has a finite AND/OR proof tree. At state i, every E-side proof support combines with every H-side proof support by union; alternatives form the minimal-support antichain. Replacing a state occurrence in an accepting proof by any other finite proof rooted at that state is syntactically valid. Its support is the outside-context support K union the replacement support C'. For any consistent such union, the entire truth-table cylinder is accepted. A successful Gap-MCSP cover rejects all tables of complexity greater than s2, so that cylinder has at most M2=|SIZE(s2)| tables and fixes at least N-log2(M2) distinct coordinates.

A forced-splice contradiction must therefore produce a consistent cross-context support fixing fewer than N-log2(M2) coordinates. State reuse alone does not suffice: opposite signs can make the support unrealizable, while a consistent union can fix almost every coordinate and leave only low/medium tables. Full grammar, proof, and finite toy-model calibration: `research/C227_NATIVE_CERTIFICATE_SPLICE_LAW_2026-09-27.md`.

Status: grammar and conditional splice law proved. No forced low-footprint splice for actual low-circuit tables; no superlinear fusion lower bound or P-vs-NP proof follows.

## C-228 - Easy anchors can have hard global readout without splice hardness

Fix a subexponential but superpolynomial family E of truth tables, each of circuit size at most s0=N^alpha, and choose a random R-element subfamily W with R=2^(N^delta), 0<delta<alpha<1. An explicit sparse-indicator family supplies |E|=2^Theta(N^alpha/n). Since the hypercube graph has degree N, one can choose W with no adjacent pair. The total promise Y=W, Z=all other tables has a q-rule readout lower bound by counting: there are binom(|E|,R) possible W, but at most 2^(4Nq+2q^2+q) q-rule outputs. This gives q >= 2^(N^delta/2+O(log N)) for some W, despite every YES table being individually easy and the seed-feature floor being only linear.

Every consistent accepting certificate must fix all N coordinates, since its cylinder lies in the independent set W. Any consistent context/subproof splice in a sound closure also fixes all N coordinates and lands back on W; this model does not force a forbidden hybrid. The readout lower bound comes from arbitrary global labeling, not dangerous splicing. The high side contains many easy tables, so this is an artificial promise and not Gap-MCSP. Learning: certificate width, anchor abundance, and individual easiness alone do not establish the O-151 mechanism; an actual-promise splice proof must exploit additional geometry of SIZE(s1) versus CC>s2. Full proof: `research/C228_RANDOM_SUBFAMILY_READOUT_CALIBRATION_2026-09-27.md`.

## C-229 - Direct universal-circuit witness grammar exposes a synchronization cost

Low-table membership is `exists description d, for all N coordinates k: w_k=C_d(x_k)`. Building one coordinate-check chain per low circuit description gives the simple O(N times number-of-low-tables) native cover. Sharing check states across descriptions removes the description tag that keeps all N checks tied to one witness d. The exact certificate grammar then cross-combines E/H supports from different descriptions; soundness needs every such hybrid to be inconsistent or high-free. Keeping d in the state prevents this cross-mix but restores description-indexed copies. This is a failure of the proposed construction at its sharing step, not a lower bound: carriers may encode semantic consistency more compactly. Next seek a semantic quotient of partial circuit descriptions and count its cross-compatible obligations. Full audit: `research/C229_UNIVERSAL_CIRCUIT_CERTIFICATE_GRAMMAR_AUDIT_2026-09-27.md`.

## C-230 - The exact splice threshold is the maximum safe subcube dimension

Let kappa_square(s2) be the maximum number of free truth-table coordinates in a full subcube all of whose tables have circuit size at most s2. Any consistent accepting proof support C has free-coordinate set of size N-r(C), so soundness requires N-r(C)<=kappa_square(s2). Circuit counting gives kappa_square=O(s2 log(s2+n)). Conversely, fix an input-prefix subcube F of size 2^k and allow an arbitrary Boolean function on its k free address bits, zero outside F. Lupanov synthesis computes every such extension in O(n+2^k/k) gates. Choosing 2^k=Theta(s2 log s2) gives kappa_square=Omega(s2 log s2). Thus kappa_square=Theta(s2 log s2)=Theta(log|SIZE(s2)|) for fixed-beta OPS scales. Certificate-width sharpening alone is therefore exhausted up to constants. Source: Lupanov 1958, bibliographic record/scan at MathNet; full derivation and splice consequence: `research/C230_HIGH_FREE_SUBCUBE_DIMENSION_CALIBRATION_2026-09-27.md`.

## C-232 Ã¢â‚¬â€ Same-alphabet communication/DAG separation; OPS transfer remains open

For an arbitrary Boolean function `f` on N-bit inputs, its KW mismatch relation has N output labels and an `O(N)`-bit protocol (Alice sends her input). Circuit counting gives a function with circuit size `Omega(2^N/N)`, and Sokolov's DAG/KW theorem transfers this to rect-DAG size. This is a generic counterexample to Ã¢â‚¬Å“short communication or small output alphabet implies a small shared DAG.Ã¢â‚¬Â It does not transfer to the fixed Gap-MCSP promise. For that promise, `S_rect=Theta(C_sep)` and truth-table versus circuit-description input representations have equal minimum DAG size. The direct separator `OR_d AND_k[w_k=G(d)_k]` costs `N*2^(O(s1 log(n+s1)))`; universal evaluation alone does not remove the existential over d. The `2N` mismatch rectangles form a small cover, but arbitrary unions in that cover cannot be binary-expanded unless every intermediate set is a rectangle. Quantitative chain remains `rho_prom<=O(S_rect)` and `S_rect<=O(rho_prom^3/log rho_prom)`; forcing `rho_prom>N^(1+epsilon)` through the latter requires `S_rect>cN^(3+3epsilon)/logN`. Status: model-level calibration proved; no actual-promise superlinear bound or P-vs-NP proof. Full note: C-232.

**C-233 (proved operational lemma; no P-vs-NP consequence).** For the q-rule least closure `x_i=(a_i OR OR_{jÃ¢Ë†Ë†P_i}x_j) AND (b_i OR OR_{jÃ¢Ë†Ë†R_i}x_j)`, first-activation ranks are the least solution of `tau_i=1+max(min({0 if a_i}Ã¢Ë†Âª{tau_j:jÃ¢Ë†Ë†P_i}), min({0 if b_i}Ã¢Ë†Âª{tau_j:jÃ¢Ë†Ë†R_i}))`, with infinity when either side has no finite support. A min-priority worklist finalizes exact ranks in nondecreasing order because every candidate is one plus both supporting ranks; each rule is finalized once and each support incidence processed once. With `E<=2q^2`, seed evaluation costs `O(qN)`, yielding `O(qN+(q+E)log q)` word-RAM operations. The closure has a direct `O(qN+E)=O(q^2)`-gate TSC partial recognizer, outputting 1 on Y and Z on high tables, and a total TSC separator of size `q^2 polylog q` via RAM simulation. Neither bound implies a standard Boolean circuit/rect-DAG of that size; RAM/TSC-to-acyclic conversion is unresolved. A partial-TSC lower bound `>N^(2+2epsilon+delta)` would imply `q>N^(1+epsilon)`, but none is established. See `research/C233_MINMAX_ACTIVATION_RANK_AND_TRISTATE_RAM_BRIDGE_2026-09-27.md`.
## C-234 - Conditional blockwise substitution theorem

**Proved conditionally.** Let D be the family of all k-bit Boolean functions, repeat each g in D across r=N/2^k address-prefix blocks, and choose k so every g has circuit size at most s1/4 and 2^k=Theta(s2). All diagonal tables lie in SIZE(s1); independent block hybrids range over all 2^N tables. If a selected accepting proof for each diagonal table has pairwise-disjoint state occurrences isolating each block from its outside context, then state-label pigeonholing plus repeated valid substitution yields at least (|D|/(2rq))^r accepted hybrids. Circuit counting forces q>=2^(Omega(s2)) at OPS scales.

**Not proved for arbitrary covers.** Block isolation is not automatic. The diagonal-only subpromise has an O(N) Boolean separator and therefore an O(N)-pair fusion cover, proving that no choice of one accepting proof per anchor can satisfy the isolation hypothesis for every anchor simultaneously. The missing theorem is a quantitative charge for the resulting nonlocal/interleaved proof structure or an alternative compatibility theorem. No full-promise superlinear fusion lower bound follows. Full proof: research/C234_BLOCK_REPLICATION_AND_CONDITIONAL_SPLICE_AMPLIFICATION_2026-09-27.md.
**C-234 exact fingerprint refinement.** For diagonal anchors w_g(p,u)=g(u), context K from w_g and replacement support C from w_h are compatible iff g and h agree on every suffix u represented by at least one coordinate in dom(K) intersect dom(C). The overlap is a partial truth-table fingerprint; a full fingerprint prevents cross-description splicing. For differing u outside the fingerprint, the copies across prefix blocks are assigned to K, C, or left free; constant-side ownership has a low diagonal completion. Dangerous hybrids require prefix-varying ownership. This is an exact mechanism description, not a q lower bound.

## C-235 Ã¢â‚¬â€ Native splice intervals and endpoint joins/meets

For a consistent dual-rail support S, define the Boolean interval `Q(S)=[ell(S),u(S)]`, where ell is the indicator of positive literals and u is the complement of the negative-literal set. Then `Q(S union T)=Q(S) intersect Q(T)`, `ell(S union T)=ell(S) OR ell(T)`, and `u(S union T)=u(S) AND u(T)`. Every output-proof interval of a sound Gap-MCSP closure is wholly inside SIZE(s2); in particular both endpoints are size-s2. This yields exact endpoint constraints for arbitrary context/subproof splices, simultaneous disjoint-occurrence substitutions, and every E/H side cross-product at an output rule.

The endpoint law suggests a possible route around the tight `Theta(s2 log s2)` safe-cube dimension: force a high canonical ownership endpoint directly. No mechanism forcing one is known. The C-228 singleton-safe promise and C-234 diagonal equality cover pass the hostile check. This is a verified structural reformulation, not a lower bound. Full proof: `research/C235_CUBE_INTERVAL_CALCULUS_FOR_NATIVE_SPLICES_2026-09-27.md`.

## C-236 Ã¢â‚¬â€ Disagreement-restricted ownership selector cap

For two repeated low anchors `w_g(p,u)=g(u)` and `w_h(p,u)=h(u)`, any compatible context/subproof splice has endpoint z in SIZE(s2). On the disagreement set D, z equals one of the two anchor values coordinatewise. The selector `mu=(w_g XOR w_h) AND (z XOR w_h)` records which anchor was chosen and is computable with size at most `s2+2s1+O(1)`. More directly, distinct masks require distinct restrictions of z, so across all compatible splices at most `|SIZE(s2)|=2^(o(N))` masks occur. For typical g,h, D has size at least N/3, leaving `2^(Omega(N))` possible masks, almost all forbidden. This isolates the exact consistency constraint, but does not lower-bound q: no bound connects q to the image size of context/subproof products. The O(N) diagonal equality cover passes by keeping masks prefix-constant. Full proof: `research/C236_DISAGREEMENT_SELECTOR_CAP_FOR_COMPATIBLE_SPLICES_2026-09-27.md`.

**C-236-A completion refinement.** For each compatible selector mu, the canonical source hybrid `H_mu=w_h XOR mu` is a completion of the mixed support and hence is itself low. Thus masks outside `L_{g,h}={mu:H_mu in SIZE(s2)}` cannot be induced; the mask-to-hybrid map is injective, giving the `|SIZE(s2)|` cap. This strengthens endpoint-only bookkeeping but still does not connect profile-image size to q. See C-236.

## C-237 Ã¢â‚¬â€ The disagreement-selector safe width is tight

For typical repeated low anchors `w_g,w_h`, their safe selector set contains an axis-aligned cube of dimension `Theta_beta(s2 n)`. If beta<1/2, put a Lupanov-sized free subcube in one disagreement column. If beta>=1/2, choose q differing suffix columns and vary arbitrary prefix functions; Lupanov synthesis costs `O(qr/(n-k)+qk+s1)<=s2`. C-230 gives the matching O(s2 n) upper bound. Thus random anchor disagreement does not shrink the safe-cube threshold; charge free-set geometry/grammar generation instead. No q bound follows. Full proof: `research/C237_SAFE_SELECTOR_CUBE_DIMENSION_2026-09-27.md`.

## C-238 Ã¢â‚¬â€ Whole-skeleton E/H cross-product

A ranked witness skeleton records the active states and the selected predecessor edges while abstracting away seed-literal identities. If two accepted tables realize the same skeleton, mixing all E-side seed labels from x with all H-side labels from y preserves a finite proof DAG whenever the mixed support is consistent. Its full cylinder lies in SIZE(s2). This is a global version of state reuse. The immediate counting route fails: there are at most `2^(O(q log q))` skeletons in a q-rule system, too many for the `2^(Theta(s2))` repeated low anchors when q>=N. No q lower bound follows. Full proof: `research/C238_GLOBAL_WITNESS_SKELETON_MIXING_2026-09-27.md`.
## C-239 Ã¢â‚¬â€ Canonical rank fibers and conflict-or-cover

The activation-rank vector from C-233 alone does not determine the side witnesses: a nonmaximal side can have minimum rank 0 on one anchor and a positive predecessor rank on another while the state activation rank stays fixed. C-239 gives an endpoint-realizable two-rule counterexample. The augmented profile of both side minima per state does determine a canonical skeleton; selected predecessor edges decrease rank, and equal-side-rank accepted anchors obey C-238's whole-skeleton E/H cross-product. For fixed Q, this canonical profile is a function of the 2q-bit seed signature, so it gives at most 2^(2q) canonical fibers. This is not a count of all C-238 witness topologies, and it remains too large for anchor pigeonholing at q>=N.

For a reusable state i, let K range over outside-context supports in accepting proofs with a marked i occurrence and C over finite proof supports rooted at i. Substitution gives an accepting output support K union C. If consistent, soundness and C-230 imply |free(K) intersect free(C)|<=kappa_square(s2); otherwise the support contains opposing rails. This is the exact conflict-or-cover obligation on state reuse. No extremal theorem charging it to q is known. A blockwise residual-description attempt also fails to produce a near-linear cover because it must preserve nonempty intersection with one common circuit description across all address blocks. Full proof and limits: research/C239_CANONICAL_RANK_FIBERS_AND_NATIVE_SPLICE_OBLIGATION_2026-09-27.md.

## C-241 Ã¢â‚¬â€ Description-space invariance for shared mismatch DAGs

Status: proved exact model fact; no actual-promise lower bound. For any onto map G:D->Y, the rect-DAG complexity of (d,z)->Mis(G(d),z) on D x Z equals that of (w,z)->Mis(w,z) on Y x Z. Lift Alice-side sets through G for one inequality; restrict a description-DAG to a section sigma:Y->D for the reverse. This handles noncanonical/multiple descriptions exactly. Therefore short circuit descriptions help the bit protocol but cannot reduce standard DAG size unless they yield a small separator circuit for the truth-table promise.

The direct universal separator has size O(N|Y|), and the dyadic restriction-profile router has size O(sum_I pi_I(Y)) <= O(N|Y|/log|Y|+N log N), still exponential for OPS low families. The 2N signed mismatch rectangles are a small nondeterministic cover; they do not furnish a binary product-rectangle DAG. The actual shared-state obligation is global aggregation of the local product-hull condition. Quantitative chain and limits: C-241; no superlinear S_rect, rho_prom, or P-vs-NP result.

Sokolov PLS remains distinct: its state graph is acyclic and a state/successor choice with t communication bits incurs an O(2^(3t)) conversion factor per state. Rank-layering Q gives O(q^2) states and t=O(log(q+N)); the resulting O((q^2+N)(q+N)^3) Boolean game is worse than the direct rank/support compiler. The cyclic q-state closure therefore has no hidden standard-PLS identification.

**C-241 compiler cross-check with C-240.** If m empty-carrier output rules have both seed vocabularies nonempty, C-240 forces each pair to be complementary literals on one coordinate. The seed-construction term in the SCC compiler can therefore be refined from O(qN) to O((q-m)N+m). More precisely the bound is O((q-m)N+m+E_ext+sum_C(r_C e_C+r_C^2)+q). This is parameter-sensitive but does not constrain external support incidence or dense SCC feedback; it leaves the worst-case compiler loss unchanged. No near-lossless q-to-DAG map follows.


## C-242 Ã¢â‚¬â€ Finite antichain grammar and blocker-path dual

**Established.** For a q-state positive least-fixed-point fusion closure, each state has an exact antichain grammar of inclusion-minimal seed supports, obtained as the least finite-proof solution; every minimal support has a witness of height at most q. Every state context/replacement-support pair produces an output proof by subtree substitution. In a successful Gap-MCSP closure, every consistent such support has its full Boolean interval inside SIZE(s2), so both canonical endpoints are in SIZE(s2) and its free dimension is at most kappa_square(s2).

**Established.** For every high table z, each inactive state has a false side whose seeds and active predecessors are absent. Following these sides through a ranked accepting proof for any low table w reaches a mismatching seed literal after at most q state visits.

**Not established.** No q-sensitive bound on the number/geometry of compatible interval joins; no forced high splice; no near-linear full-promise cover; no superlinear native fusion lower bound; no P-vs-NP resolution. Proof and scope: research/C242_NATIVE_CERTIFICATE_ANTICHAIN_AND_BLOCKER_PATH_2026-09-27.md.


**C-242 upper-cover calibration.** For a fixed coordinate order, the native prefix-intersection construction has size at most sum_{t=2}^{N-1}|pi_t(SIZE(s1))|. It is correct because every length-(N-1) low prefix has exactly two table completions, both in SIZE(s2) by one-point patching, so its high-side carrier is empty. C-212 shattering makes the first Theta(s1) levels exponential, so this construction is not near-linear. This is a valid construction and a route-specific failure, not a lower bound on adaptive/native covers. Full argument: research/C242_NATIVE_CERTIFICATE_ANTICHAIN_AND_BLOCKER_PATH_2026-09-27.md.


## C-243/C-244 Ã¢â‚¬â€ carrier containment and state-zone factorisation

**Proved.** If C is any finite proof support rooted at state i, then U intersect Cyl(C) is a subset of T_i. Therefore |T_i| >= 2^(N-|dom(C)|)-M2; pairwise-disjoint high portions of t-fixed-coordinate proof cylinders obey the C-243 packing inequality.

**Proved.** Let P_i be all finite proof supports rooted at i and K_i all finite accepting contexts with a hole at i. On legal inputs, Acc_Q(x)=OR_i([P_i](x) AND [K_i](x)). For a sound promise separator, the q zones Z_i=[P_i] intersect [K_i] cover SIZE(s1) and are each subsets of SIZE(s2). Every compatible K,C cylinder is low.

**Open.** No bound relates q to the number or geometry of low circuits in a grammar-generated zone; carrier intersections may be correlated. No superlinear native lower bound, near-linear full-promise cover, or P-vs-NP proof follows. See research/C243_CARRIER_VOLUME_AND_CERTIFICATE_PACKING_2026-09-27.md and research/C244_STATE_ZONE_FACTORISATION_AND_GLOBAL_READOUT_2026-09-27.md.


## C-245 Ã¢â‚¬â€ Marked proof/context antichain grammar

**Proved.** Over the antichain semiring of consistent signed-literal supports, a one-hole context recurrence propagates the hole through one rule side and an ordinary proof through the other. For every input and state i, the full-context zone is unchanged if contexts are restricted to height at most 2q: shorten the root-to-hole path by deleting repeated states and replace sibling proofs by rank-minimal proofs.

**Consequence.** The C-244 state-zone decomposition has a direct representation from the same q-rule grammar, with q^2 context-family indices over all hole targets and at most 2q iterations. This counts family labels only; antichains may be exponentially large. It gives no superlinear q lower bound. Full derivation: research/C245_MARKED_ANTICHAIN_GRAMMAR_FOR_CONTEXTS_2026-09-27.md.


## C-246 Ã¢â‚¬â€ Repeated-block proof-cylinder capacity; count route fails

**Proved.** In the C-234 diagonal family, if N=rm and each suffix value is repeated r times, a sound support cylinder fixing all but at most kappa coordinates can match at most 2^(kappa/r) diagonal anchors. Since kappa=o(N) and m=Theta(s2), this is 2^(o(m)); an exponential number of proof supports is needed to cover the family.

**Count audit.** A q-state closure has at most q*2^q*(2N+q)^(2q) ranked witness-DAG encodings. Hence certificate count yields only Theta(m)-kappa/r <= O(q log(N+q)), weaker than q>=N-o(N) when m=N^beta, beta<1. The first failed implication is exponential support count => superlinear state count. Full proof and learning: research/C246_REPEATED_BLOCK_CERTIFICATE_CAP_AND_COUNTING_FAILURE_2026-09-27.md.


## C-247 Ã¢â‚¬â€ Multi-hole splice entropy budget

**Proved.** Pairwise disjoint marked occurrences in a finite accepting proof can be replaced simultaneously. If their associated anchor completions have distinct restrictions to disjoint private coordinate sets left free by the context and other slots, and all unions are consistent, then the product of family sizes is at most |SIZE(s2)| by soundness.

**Calibration.** C-234 block isolation gives 2^N distinct accepted hybrids and contradicts log|SIZE(s2)|=o(N), recovering its conditional exponential bound. The diagonal equality cover defeats the private-slot premise through context fingerprints. No small-q theorem forces a large compatible product or charges fingerprints superlinearly. See research/C247_MULTIHole_SPLICE_ENTROPY_BUDGET_2026-09-27.md.


## C-248 Ã¢â‚¬â€ Blocker rectangles and monotone extension

**Proved.** Every state i induces the product rectangle R_i=A_iÃƒâ€”B_i of low tables activating i and high tables blocking i. Output rectangles cover YÃƒâ€”Z. Each R_i is covered by signed seed-mismatch rectangles on whichever side the high input blocks, together with predecessor rectangles; low activation ranks force routes to terminate within q steps. Thus state reuse automatically includes every cross-pair in the rectangle.

**Transfer.** Unrolling q least-fixed-point rounds produces a monotone separator extension over the signed-seed encoding with at most 3qÃ‚Â²+1 unbounded-fan-in gates, counting gates but not wires. A lower bound M on this extension measure implies qÃ¢â€°Â¥sqrt((MÃ¢Ë†â€™1)/3). The compiler has O(qÃ‚Â²(N+q)) gate-input incidences, hence O(qÃ‚Â³) at qÃ¢â€°Ë†N; it is not an improved bounded-fan-in compiler.

**Limit.** Every disjoint promise already has a 2N mismatch-rectangle cover. More sharply, the artificial promise Y={0,1}^N \setminus {0^N,1^N}, Z={0^N,1^N} has a one-rule native cover and a full rectangle R_1=YÃƒâ€”Z; different pairs route to different mismatching coordinates. Rectangle area and raw cover count do not charge q, and pair-space cross-swaps do not splice truth tables. No lower bound on the actual promise's monotone extension measure, no superlinear fusion bound, no near-linear cover, and no P-vs-NP proof has been obtained. See research/C248_BLOCKER_RECTANGLES_AND_MONOTONE_EXTENSION_COMPILER_2026-09-27.md.


## C-249 Ã¢â‚¬â€ Bi-blocked output-root normal form

**Proved.** At OPS parameters, every signed coordinate half-cube intersects the high side U because |SIZE(s2)|=2^{o(N)}. For each accepted low table, an active empty-carrier state of minimum activation rank has two nonempty, disjoint endpoints: an empty endpoint cannot contain a nonempty seed slice, and any predecessor carrier contained in it would itself be empty and activate earlier. Thus only roots with both endpoints nonempty are needed for completeness.

**Consequence.** Each normalized root i contains high witnesses z_EÃ¢Ë†Ë†E_i and z_HÃ¢Ë†Ë†H_i that block its opposite sides. By C-240, direct root seed vocabularies are at most a complementary singleton literal pair or are seedless on one side; an accepting proof must pass to a predecessor. The one-bit root choice or forced escape maps low anchors into predecessor rectangles paired with fixed high witnesses.

**Limit.** This is only a root normal form. It gives no bound on the number or geometry of predecessor families, no q-sensitive cross-join charge, no near-linear cover, and no P-vs-NP proof. The C-248 one-state generic counterexample lacks the actual high-side shattering premise. See research/C249_BIBLOCKED_OUTPUT_ROOT_NORMAL_FORM_2026-09-27.md.


## C-250 Ã¢â‚¬â€ Half-safe predecessor supports

**Proved, conditional on C-243.** At a seedful minimum-rank output root, a low anchor matching a direct literal (k,b) must escape through an opposite-side predecessor. Every high table extending any support cylinder C for that predecessor lies in its carrier, which is disjoint from the root's matching high half-cube. Thus the half of Cyl(C) with bit k=b contains no high tables and is wholly in SIZE(s2). Therefore |free(C)| <= ceil(log2|SIZE(s2)|)+1.

**Limit.** On repeated-block anchors this limits each seedful escape cylinder to 2^((kappa+1)/r) anchors, but witness-DAG counting still gives only a scale below the existing linear q floor. Seedless roots are outside the lemma. The needed next result remains a q-sensitive aggregation of context/proof joins across roots; no superlinear q bound or P-vs-NP proof follows. See research/C250_ONE_SIDED_SAFE_ESCAPE_CYLINDERS_2026-09-27.md.


## C-251 Ã¢â‚¬â€ Root escape support dichotomy

**Proved.** Every accepted low at a C-249 normalized empty root has one of two selected proof forms. If a direct seed matches, the opposite predecessor support is half-safe by C-250. If no direct seed matches, both sides use predecessor supports; their union is consistent, and every completion preserves the empty-root proof, so the union cylinder lies wholly in SIZE(s2) and has at most floor(log2|SIZE(s2)|) free coordinates. This covers seedless roots and missed-seed branches at the paired-support level.

**Consequence and limit.** In the C-234 repeated-block family each selected single or paired support signature covers at most 2^((kappa+1)/r) anchors. Counting signatures still gives only exp(O(q log(N+q))) capacity, since paired proof-DAG descriptions square the old count up to constants. No cross-root reuse charge, superlinear state bound, near-linear full-promise cover, or P-vs-NP proof follows. See research/C251_ROOT_ESCAPE_SUPPORT_DICHOTOMY_2026-09-27.md.


## C-252 Ã¢â‚¬â€ State-conflict graph readout

**Proved.** Aggregate predecessor pairs over all empty output roots into relation G subset [q] x [q]. No high table activates both endpoints of a pair, since C-243 puts it in both disjoint root endpoints. Direct seed/opposite-predecessor branches similarly give at most 2qN forbidden state/literal incidences. Every accepted low activates a pair in G or a state/literal incidence. Thus a depth-two separator readout has at most q^2+2qN terms over the q cyclic activation predicates and input literals.

**Limit.** The readout has q^2+2qN terms; with the existing OPS floor q=Omega(N), composing it with q-round unrolling remains O(q^2) unbounded-fan-in gates, matching C-248. The conflict graph does not bound activation-fibre sizes or give a superlinear q lower bound. The new target is a fibre-geometry theorem for the actual low/high circuit promise, or a near-linear cover. No P-vs-NP proof follows. See research/C252_STATE_CONFLICT_GRAPH_READOUT_2026-09-27.md.

## C-253 ? Conflict-profile fibre subcubes

**Proved.** A profile containing a C-252 conflict edge has no high inputs. For an independent profile sigma, let B_sigma be the seed literals incident to its active states. The low fibre is contained in the union of B_sigma's literal slices; the high fibre avoids all those literals and lies in a subcube fixing every marked coordinate. Thus |U intersect F_sigma| <= 2^(N-r_sigma), or the fibre is high-empty if both polarities are marked at one coordinate.

**Entropy audit.** If I independent profiles occur on high inputs and r_min is their minimum marker-coordinate count, then |U|/2^N <= I*2^(-r_min), so r_min<=log2(I)+o(1)<=q+o(1). This only guarantees one weakly marked high profile; it need not be used by low inputs. Two-wise shattering alone does not force low/high profiles to be coupled. No state lower bound, near-linear cover, or P-vs-NP proof follows. See research/C253_CONFLICT_PROFILE_FIBRE_SUBCUBES_2026-09-27.md.

## C-254 ? Partial-support hazard boundary

**Proved.** Define state activation on a partial support C by existence of a finite proof with all leaf literals contained in C. If C already activates an edge of the C-252 conflict relation, or an active state plus an incident direct-seed literal, every completion activates an empty output root. Hence Cyl(C) is contained in SIZE(s2), and |dom(C)|>=N-log2|SIZE(s2)|. Hazard is monotone under extending C; every low table has a first hazardous prefix at depth at least this large in every coordinate order.

**Corrected support bound.** A selected readout term has a ranked witness DAG with at most q distinct states, at most two seed literals per state, and at most one additional marker. Thus its hazardous support has width <=2q+1, giving q >= (N-log2|SIZE(s2)|-1)/2. This is only linear and weaker than the existing N-o(N) floor; no superlinear aggregate follows. See research/C254_PARTIAL_SUPPORT_HAZARD_BOUNDARY_2026-09-27.md.

## C-257 Ã¢â‚¬â€ Parity-code native closure calibration

**Proved.** For odd-parity high set `U` and even-parity anchors, a native list of `4N-4` pairs derives the empty set for every low anchor. Prefix-parity carriers propagate by intersecting with each next matching literal slice; the final even-parity intersection is empty. Every proper partial assignment has a high odd completion, so every consistent output-proof support fixes all N coordinates.

**Splice consequence.** A consistent context/subproof splice is again an output proof and therefore fixes all N bits. Its unique completion cannot be high by soundness, so it is another even anchor. Thus density/shattering, full certificate width, and anchor abundance alone cannot force a bad splice or superlinear q.

**Scope.** This artificial promise does not match `SIZE(s1)` and yields no OPS bound. O-153 needs an actual low-circuit-description consistency theorem. See `research/C257_PARITY_CODE_SPLICE_LOCKING_CALIBRATION_2026-09-27.md`.


## C-255 Ã¢â‚¬â€ Shared-DAG route audit

For plain C-75 signed mismatch, the minimum binary rect-DAG size is `Theta(C_sep)`, the minimum Boolean separator extension size. Pullback through `G(d)=TT(C_d)` and restriction to one description per low table show exact size invariance in description space. A q-pair fusion cover currently yields only `S_rect=O(q^3/log q)`; conversely `q<=O(S_rect)`. The q activation graph is cyclic with input-dependent ranks, so q named rules do not themselves form an acyclic q-node DAG. Product-hull safety at each merged state is exact, but no overlap-safe global charge or near-linear adaptive DAG was obtained. C-255 also proves the common-translate lemma: if `|SIZE(s1)||SIZE(s2)|<2^N`, some `r` has `u xor r` outside `SIZE(s2)` for every `u in SIZE(s1)`. It does not solve source-reduction cut soundness. See `research/C255_SHARED_DAG_ROUTE_RESTART_2026-09-27.md`.
**C-256 static-decoder obstruction (proved).** Let f:{0,1}^M->{0,1} have two-wise-rich one/zero sides, with 0,e_i on the one-side and 1^M on the zero-side. For any common translate r, low base-table encodings u_x,v_y, and a fixed decoder from each outer mismatch label (k,b) to a KW answer, if every induced mismatch rectangle is source-valid then r=v_{1^M} xor u_{0^M} xor OR_i(u_{0^M} xor u_{e_i}). Hence C(r)=O(Ms1); if this fits s2, it contradicts r notin SIZE(s1) xor SIZE(s2). Separately, for full-domain BPHP search, a static decoder from each (k,b) to a collision answer is impossible: at an active coordinate both signed rectangles are nonempty, and their two fixed Alice collision-equality sets would have to cover the full assignment domain, which two equality predicates cannot do. Scope: static output-label reductions only; no target DAG lower bound, because repeated labels at distinct sinks could be decoded differently. Full proof and BPHP source details: research/C256_HARD_TRANSLATE_KW_DECODER_OBSTRUCTION_2026-09-27.md.

## C-258 - Repeated-block native subcover

For coordinates partitioned into d blocks of length r, let `Rep_{d,r}` be all blockwise constant tables and let U be the actual complement of `SIZE(s2)`. If `Rep_{d,r} subseteq SIZE(s1)` and every literal slice of U is nonempty, the explicit block-prefix/merge/intersection construction in C-258 gives a successful native list with `q=2N+2d-1`. It is an upper bound for this subfamily only. This realizes the diagonal equality fingerprint directly in the cyclic closure model. It does not aggregate over all low circuits and therefore gives no full-promise upper bound or lower bound.

## C-259 - Cofactor patching/splice threshold

**Proved.** If t prefix cofactors are each computed by a size-s1 circuit, muxing them gives `CC<=t s1+O(t)`. Under `s2/s1=cn`, all t up to a sufficiently small constant multiple of n are safely in `SIZE(s2)`. Circuit counting gives `log |SIZE(s2)|=O(s2 n)`; therefore, under C-247's private-coordinate and injective-completion hypotheses, t independent replacement families of size `2^(Theta(s2))` can be sound only for `t=O(n)`.

**Calibration.** Both the constructive patch and the private-slot entropy contradiction turn at `Theta(n)`, matching C-116. This means a constant number of holes cannot suffice; it does not imply that a q-state grammar exposes n holes, nor that q must be superlinear to suppress them. See `research/C259_COFACTOR_PATCHING_SPLICE_THRESHOLD_2026-09-27.md`.

## C-260 - Native proofÃ¢â‚¬â€œblocker duality

**Proved.** On arbitrary seed-feature inputs, each native state has a minimal certificate antichain `C_i` and a minimal absent-feature blocker antichain `B_i`; the least-fixed-point recurrences are De Morgan duals and `B_i=Tr(C_i)`. Output blockers are the transversal family of output certificates. For the consistent table-realizable certificates, cutting an accepting proof at state i gives `C_out^cons=min_i(K_i join P_i)`. Every compatible join is hit by every output blocker. On actual table inputs, this yields sound accepting cubes, low-free rejecting cubes, and a mismatch literal for each low/high pair.

**Limit.** The transversal law only forces a nonempty intersection; it does not limit how many compatible joins one blocker literal can hit, or charge q for the family of joins. It does not improve the `N-o(N)` native lower bound or construct a full-promise near-linear cover. The candidate next invariant is q-sensitive incidence geometry of context/proof joins against the shared blocker grammar. Full proof: `research/C260_NATIVE_PROOF_BLOCKER_DUALITY_2026-09-27.md`.

**Forced-reuse calibration.** For a repeated-block subfamily of size `2^d` with `d log d=O(s1)`, every anchor's minimum-rank active empty root has a predecessor by C-249. Assigning its first predecessor state to that anchor forces some internal state to serve at least `2^d/q` anchors. This is genuine state reuse, but C-258's O(N) equality-fingerprint cover of the same family shows the collision can be safe; no compatible cross-product follows.

## C-261 Ã¢â‚¬â€ Cyclic matching hardness survives the fusion fixed point

**Classification: GLOBAL-STRUCTURAL.** Rao's revision-5 spread-matching theorem gives exp(Omega(sqrt(v))) ordinary monotone circuit size for separating v-vertex bipartite graphs with a perfect matching from graphs with no matching of size v/4. A q-state positive cyclic AND grammar stabilizes in q rounds; explicit binary unrolling costs O(q^2(v^2+q)). Therefore its native cyclic AND count is also exp(Omega(sqrt(v))). This is a source lower bound only; no Gap-MCSP transfer follows. Full proof: research/C261_MATCHING_CYCLIC_LOWEXT_AND_GLOBAL_ROUTE_AUDIT_2026-09-27.md.

## C-262 Ã¢â‚¬â€ LowExt parameter geometry

**Classification: CONDITIONAL-TRANSFER.** Under the exact C-125/C-126 map conditions, q >= exp(c sqrt(v))-a. Setting v=A(ln N)^2 gives q>N^(1+epsilon) whenever exp exponent c sqrt(A) exceeds both 1+epsilon and the exponent eta of a(N), with a fixed margin. Poly(v) YES completion size is polylogarithmic and fits s1=N^beta/(c0 log N) for every fixed beta>0. The missing object is the map itself: few-AND monotone phi, a low-code witness for every perfect-matching graph, and a high completion above every NO image.

## C-263 Ã¢â‚¬â€ Sparse matching-code map fails

**Classification: ROUTE-KILL.** The direct edge-incidence map with universal zero rails admits the all-zero low code on NO graphs; its complemented version admits the all-one code. Pinning a fixed baseline coordinate does not repair the construction because one-bit perturbations of a simple baseline remain small circuits. This kills the direct template, not all LowExt reductions.

## C-264 Ã¢â‚¬â€ Compatibility incidence calibration

**Classification: CALIBRATION.** State-indexed compatible context/proof pairs joined against output blockers are the strongest current synchronization object. C-258's O(N) repeated-block cover implements equality fingerprints and keeps such reuse safe, so raw pair, row, or blocker-hit counts cannot imply superlinear q. A new theorem must charge description-dependent synchronization for the full circuit class.

## C-265 Ã¢â‚¬â€ Independent cofactor recursion route filter

**Classification: ROUTE-KILL.** Independent block cofactors preserve soundness only while the total number R of freely chosen size-s1 pieces is O(n), since their mux costs R s1. Reaching a trivial all-functions leaf requires R=N^(1-beta+o(1)), beyond that budget. This rules out the naive product recursion, not a globally synchronized near-linear cover.

## C-266 Ã¢â‚¬â€ Proof-theoretic cyclic matching lower bound audit

**Classification: GLOBAL-STRUCTURAL.** Rao's 2026 spread-matching theorem gives `exp(Omega(sqrt(v)))` fan-in-two monotone circuit lower bounds for perfect matching versus no `v/4`-matching. Any native cyclic intersection grammar with q paid AND states has an inflationary q-bit update and stabilizes in q rounds. Flattening its free union equations and unrolling gives an ordinary monotone separator of size `O(q^2(v^2+q))`; therefore `CycAnd(MATCH_v)>=exp(Omega(sqrt(v)))`. Direct Rao gate induction fails on cycles because its gate approximant needs an already-defined pair of child approximants; unrolling resolves the dependency at polynomial loss. This is a source theorem only. Full audit: `research/C266_CYCLIC_MATCHING_LOWEXT_AND_SYNCHRONIZATION_AUDIT_2026-09-27.md`.

## C-267 Ã¢â‚¬â€ Exact matching-to-LowExt parameter window

**Classification: CONDITIONAL-TRANSFER.** Under C-125/C-126, with map AND-cost `a(N)`, the matching lower bound yields `q>=exp(c' sqrt(v))-a(N)`. For `v=ceil(A(ln N)^2)` and `a<=N^eta`, any fixed-margin condition `c' sqrt(A)>max(1+epsilon,eta)` gives `q>N^(1+epsilon)`. A `poly(v)` YES completion fits `s1=N^beta/(c0 log N)` for every fixed `beta>0`. The map and the high completion on each NO image remain unconstructed, so the actual Gap-MCSP q-bound is unchanged.

## C-268 Ã¢â‚¬â€ Partial-MCSP ETH hardness does not instantiate C-125

**Classification: ROUTE-KILL (direct transplant only).** Ilango's ETH-hardness reduction encodes Bipartite Permutation Independent Set into existence of a small monotone read-once formula for a full truth-table partial function. This is an algorithmic hardness theorem; it supplies neither a source-monotone rail map with measured AND-cost nor a high unrestricted-circuit completion on NO instances. The direct transplant is invalid without those additional properties. It remains a technique-level lead for synchronizing many optimal circuit descriptions. Primary source and exact scope are recorded in C-266.

## C-269 Ã¢â‚¬â€ Structured full-baseline witness masks are too easy

**Classification: ROUTE-KILL (structured template only).** If a NO image pins a common high table z on all coordinates and each YES matching witness w_M differs from z on a succinctly computable mask D_M of circuit cost at most `s2-s1-O(1)`, then `z=w_M XOR 1_{D_M}` has size at most s2, contradiction. This kills the natural matching-edge block-mask repair of C-263. It does not apply to partial NO images whose unpinned high-completion bits are hidden.

## C-270 Ã¢â‚¬â€ Compatibility tensor fails the equality-fingerprint test as a q-charge

**Classification: CALIBRATION.** The joint context/proof relation plus output blockers is an exact global synchronization object: every accepting low anchor contributes a diagonal context/proof join, and every consistent join is sound. Counting compatible pairs or excluded pairs does not charge q, because endpoints are arbitrary semantic sets. C-258's repeated-block family has exponentially many descriptions yet synchronizes them through `2N+2d-1` equality-fingerprint pairs. A surviving theorem must use a full-`SIZE(s1)` property absent from that calibration and lower-bound its native grammar cost; none is proved here.

## C-271 - Universal-circuit semantic quotient fails to preserve one witness cheaply

**Classification: ROUTE-KILL (explicit-description and independent-block implementations only).** Enumerating size-s1 descriptions and checking all N outputs costs `N|D_s1|`, with `|D_s1|=2^{O(s1 log(s1+n))}`. Merging by local block restrictions loses the requirement that one description work on every block; independent cofactors stay sound only for `O(n)` pieces, while a trivial base needs `N^(1-beta+o(1))`. A one-state-per-exact-subfunction quotient is already superpolynomial on the shattered sparse-indicator family. This kills those three implementations, not all global semantic quotients. No near-linear full-promise cover is found; q remains `N-o(N)`. Full route audit: `research/C271_NEAR_LINEAR_UNIVERSAL_CIRCUIT_QUOTIENT_AUDIT_2026-09-27.md`.

## C-272 - Expander-overlap low-code family has high hybrids but no q charge

**Classification: CALIBRATION.** Let V=Theta(s2), b=log V, and choose the constant in V so Lupanov gives every b-bit Boolean labeling C circuit size at most s1/8. On a strongly explicit constant-degree expander H over [V], define table coordinates as r=K log N copies of each directed incidence (u,i), and set `w_C(u,i,j)=C(u) XOR C(Gamma(u,i))`. Address decoding and the neighbor map cost polylog N, so every w_C lies in SIZE(s1). With K large, the number E=V d0 r of incidence-copy coordinates exceeds `log2|SIZE(s2)|=O(s2 log N)`. Independent edge-copy recombinations therefore yield 2^E distinct tables, almost all outside SIZE(s2). Expansion makes the local views overlap: changing a nontrivial set of vertex labels changes many edge views.

This is a concrete CSP-style splice family, but it does not force the native grammar to expose independent replacement slots. A fixed expander's consistency relation has a compact O(E) check, and E can be o(N) at the entropy threshold. To force superlinear q, one needs many incompatibly wired expander/projection systems and a proof that q=O(N) cannot synchronize them all. No such grammar theorem is proved. Full construction and missing implication: `research/C272_EXPANDER_OVERLAP_LOW_CODE_SPLICE_CALIBRATION_2026-09-27.md`.

## C-273 - Recent monotone example hardness does not transfer to full-table LowExt

**Classification: ROUTE-KILL (direct example-list encoding only); POSITIVE CALIBRATION for the NO side.** A consistent list of examples gives a partial rail vector `P` with `P<=e(w)` whenever a circuit `w` fits it, the reverse of C-125's YES requirement `e(w)<=phi(YES)`. Reversing the order by allowing both rails at unspecified positions makes the vector incompatible with every one-hot NO high completion. On the other hand, if `m=poly(log N)` positions are specified in an `N`-entry table, then there are `2^(N-m)` completions and `log |SIZE(s2)|=O(N^beta log N)=o(N)`, so high completions are abundant; low completions on a NO sample list are permitted by C-125 and are not an obstruction. The 2026 result does not supply one source-monotone, AND-costed rail map with the required asymmetric orders; it is conditional rETH hardness for monotone agreement on samples. Retire only the direct example-list encoding. The surviving hint is that the NO high-completion condition is cheap for sparse samples, so focus on constructing the YES upper-code rails monotonically while keeping NO rails below a high code. Details and primary source: `research/C273_MONOTONE_EXAMPLE_HARDNESS_TO_LOWEXT_AUDIT_2026-09-27.md`.

**Checkpoint after C-271 through C-273:** three new route audits/calibrations did not change the actual lower bound, which remains `q=N-o(N)`. C-271 closes three explicit near-linear cover implementations; C-272 gives high expander hybrids without a q-charge; C-273 closes direct polynomial-example-list transfer into full-table LowExt. The frontier is still O-157's unrestricted high-completion map or O-158's global synchronization theorem, with O-162 as a candidate-family obligation.

## C-274 - Patchable global conflict support makes the LowExt map pay

**Classification: GLOBAL-STRUCTURAL.** For a C-125 map `phi` from a monotone source, let `S` be the table coordinates conflicted on at least one YES image, and `delta=|S|`. Low witnesses for any two YES inputs must agree outside S: join the two source inputs, use monotonicity of `phi`, and differing witness bits would activate both rails at that joined YES image. Fix their common restriction `w0` outside S. The monotone predicate `AND_{i notin S} phi_{i,w0[i]}` accepts every YES. If a NO were accepted, its required high completion would agree with low `w0` outside S and could be patched on S using at most `K log(N)(delta+1)` gates. Therefore, when `s1+K log(N)(delta+1)<=s2`, the predicate separates the source, giving `CycAnd(f)<=a+N-delta-1`. Thus a useful transfer with source lower bound L and map cost a<L-N forces `delta>floor((s2-s1)/(K log N))-1`. For OPS parameters this is Omega(N^beta/logN), strengthening C-127's logarithmic conflict-support condition. Large union support remains possible and is not a q lower bound. Full proof and scope: `research/C274_CONFLICT_SUPPORT_PATCHING_OBSTRUCTION_2026-09-27.md`.

## C-275 - Sparse-support interpolation strengthens the transfer obstruction

**Classification: GLOBAL-STRUCTURAL.** Every k-element subset of the n-bit truth-table address cube has a fan-in-two Boolean indicator circuit of size `O(k n/log k)`, by shared block-pattern decoding. Replacing the crude `O(kn)` point-minterm patch in C-274, any C-125 map whose union of YES conflict coordinates has `delta<=c_beta s2` (for fixed `0<beta<1`) yields a source separator with at most `a+N-delta-1` AND gates, because a NO high completion agreeing with the common low restriction outside the conflict set can be patched on those delta positions within the `s2-s1` gap. Consequently a map intended to save more than N AND gates must conflict on `Omega_beta(s2)=Omega_beta(N^beta)` coordinates in the union across YES inputs. This is a design constraint, not a q bound; conflicts may be distributed sparsely. Full proof: `research/C275_SPARSE_SUPPORT_INTERPOLATION_STRENGTHENS_MAP_OBSTRUCTION_2026-09-27.md`.

## C-276 - Route A parameter audit and primary-source cycle check

**Classification: CONDITIONAL-TRANSFER.** Use the total monotone extension `f_v(G)=1 iff nu(G)>=v/4` (v divisible by four); Rao's gap theorem lower-bounds every circuit for it because it accepts all perfect matchings and rejects all graphs with no `v/4`-matching. C-266 transfers `L(v)>=exp(c sqrt(v))` to cyclic AND complexity. A C-125 map of AND-cost `a(N)` then gives `q>=L(v)-a(N)`. To force `q>N^(1+epsilon)`, require `L(v)>N^(1+epsilon)+a(N)`. At `v=A(ln N)^2`, a fixed margin `c sqrt(A)>max(1+epsilon,eta)` suffices when `a<=N^eta`; poly(v) YES completions fit `s1` for every fixed beta. Combining with C-275, any such map must have global YES conflict support `delta>c_beta s2`; below this threshold its cost cannot leave the required transfer margin. The primary-source audit confirms Rao's gatewise approximation induction is acyclic, while explicit unrolling of the native inflationary q-state equations costs `O(q^2(v^2+q))` and preserves exponential matching hardness. This is source/parameter progress only: the map remains absent and actual q remains `N-o(N)`. Full audit and loop/clique comparison: `research/C276_ROUTE_A_PARAMETER_AND_CYCLIC_SOURCE_AUDIT_2026-09-27.md`.

**Checkpoint after C-274Ã¢â‚¬â€œC-276:** the actual Gap-MCSP bound has not changed from `q=N-o(N)`. Task 1 (cyclic matching source) and Task 2's parameter arithmetic are settled conditionally. The qualitative missing step remains a low-AND monotone rail map with high NO completions and broad YES conflict support; Route B still lacks a global synchronization charge beyond the C-258 equality fingerprint.

## C-277 - Hall cuts rule out OR-only matching-to-LowExt maps

**Classification: ROUTE-KILL (zero-AND maps).** If every rail of a C-125 map is an OR of matching-source edge variables/constants, NO consistency on graphs with at most two edges forces a fixed available polarity at every table coordinate. Every YES image must then contain the same full low code, giving an N-clause monotone CNF separator. For `f_v(G)=1` iff `nu(G)>=v/4`, Hall's theorem shows each clause that accepts all perfect matchings can reject at most `2^(v/2-1)` of the vertex-cover graphs `G_W` with `|W|=v/4-1`; there are `2^(H_2(1/4)v-o(v)}` such W. Thus a CNF needs `2^(0.311...v-o(v)}` clauses, more than `N` when `v=A(log N)^2`. This closes all zero-AND maps for the matching source at the transfer scale. It does not constrain positive AND-cost maps and does not change q. Full proof: `research/C277_HALL_CUT_OBSTRUCTION_TO_OR_ONLY_LOWEXT_MAP_2026-09-27.md`.

**Checkpoint after C-275Ã¢â‚¬â€œC-277:** the actual Gap-MCSP fusion lower bound remains `q=N-o(N)`. The cyclic source bound and transfer parameters are usable, but zero-AND maps and patchable-conflict maps are ruled out. The next Route A target must use positive AND-cost to produce witness-dependent rails with global conflict support above `c_beta s2`, while keeping `a<L(v)-N^(1+epsilon)` and the NO high-completion condition. Route B still has no global synchronization theorem beyond its equality calibration.

## C-278 - Fixed-scaffold witness-union maps spend the source AND complexity

**Classification: ROUTE-KILL.** Scope: fixed-scaffold witness-union maps. Suppose every NO input maps to the same fixed partial rail vector `P`, and all input-dependent rails vanish on NO inputs. On YES inputs, `phi=P OR psi` contains some low code `e(w)`. Since `P` itself lies below a high completion, it contains no low code. Therefore at least one excess rail of `psi` is active on every YES input, while all excess rails vanish on NO. OR all excess outputs: this computes the source `f` using the same `a` AND gates as the map, so `CycAnd(f)<=a`. Thus the canonical union of matching-witness codes, either from the zero baseline or over any fixed high/partial scaffold, cannot yield a useful `q>=CycAnd(f)-a` transfer. A viable map needs genuinely input-dependent NO-side rails as well as the YES witness additions. This does not rule out such maps and does not change q. Full proof: `research/C278_FIXED_NO_BASELINE_WITNESS_MAP_AND_EXTRACTION_2026-09-27.md`.

**Checkpoint after C-275Ã¢â‚¬â€œC-278:** the actual Gap-MCSP fusion lower bound remains `q=N-o(N)`. Route A now has explicit filters for zero-AND maps, patchable conflict support, and every fixed-NO-scaffold witness-union construction. The remaining A4 object must use varying NO partial images while preserving high completion and preventing low completion, and still cost less than `L(v)-N^(1+epsilon)`. Route B's global synchronization dichotomy remains open; its reuse tensor still passes the C-258 equality counterexample without charging states.

## C-279 - Rank-coded variable-NO map is valid but nearly exhausts source hardness

**Classification: CALIBRATION.** For two disjoint bipartite matching instances of side size `m`, set the source to `nu(G1)+nu(G2)>=m+2`. Its cyclic AND complexity is at least `exp(Omega(sqrt(m)))` by diagonal restriction to the hard `nu(G)>=m/2+1` matching threshold and cyclic unrolling. Partition the `N` truth-table addresses into `m=Theta(log^2 N)` balanced classes `S_t` whose indicator tables `z_t` all lie outside `SIZE(s2)`; counting gives `log binom(N,N/m)=Theta((N/m)log m) >> log|SIZE(s2)|` for every fixed `beta<1`. Let `R_t=[nu(G1)>=t] AND [nu(G2)>=m+1-t]`. Output the OR of `R_t`-selected signed codes `e(z_t)`. On NO inputs, either no `R_t` fires and the image is empty, or exactly one fires and the image is a high code. On YES inputs at least two consecutive `R_t` fire; adjacent `S_t` are disjoint, so the image contains the low code `e(0^N)`. This is a valid C-125 map with varying NO images. But each `R_t` is directly readable as a positive rail at any address in `S_t`, and the source equals `OR_t(R_t AND R_(t+1))`. Therefore `CycAnd(F)<=a_map+m-1` and `L-a_map<=m-1=O(log^2 N)`. The map does not transfer a superlinear q-bound; its exact lesson is that rank-only NO profiles have a cheap state-pair decoder. Full construction and proof: `research/C279_RANK_CODE_LOWEXT_MAP_AND_DECODER_COST_2026-09-27.md`.

**Checkpoint after C-278Ã¢â‚¬â€œC-279:** actual `q=N-o(N)`. C-279 meets the asymmetric LowExt order conditions but misses the cost threshold by a proved `O(log^2 N)` decoder; it is a calibration, not a breakthrough. Route A's unresolved target is now sharply narrowed to witness-indexed variable NO states whose YES activation has no sublinear state-pair decoder and whose map still costs less than `L-N^(1+epsilon)`. Route B should analyze the same compatibility object as global decodability, tested against equality fingerprints.

## C-280 Ã¢â‚¬â€ Fixed-left two-half matching palettes collapse even with pairing-sensitive terms

**Classification: ROUTE-KILL (fixed-left two-half exact-matching palettes).** Rao's approximation proof uses only its perfect-matching YES distribution and its vertex-cover-graph NO distribution, so the same monotone lower bound holds on that restricted hard support; the cyclic transfer follows the q-round unrolling from C-266. For the transfer construction, split the left vertices into fixed blocks `A,B`. At coordinate i let `F0_i(C)` and `F1_i(C)` be arbitrary subsets of bijections from A or B onto right set C. NO consistency on `G(C)` forbids both families being nonempty. YES coverage on every perfect matching with right split `C,C^c` says `F0_i(C)=all` or `F1_i(C^c)=all`; otherwise a missing bijection from each family gives an uncovered perfect matching. Applying this to both splits and using the NO constraints forces one polarity to be full on both C and Cc and the other empty. Hence every YES full code equals the NO code on `G(C)`, contradicting low/high separation. This strengthens the earlier endpoint-only diagnosis to arbitrary selected bijections. It does not cover more blocks, different support terms, or partial NO codes. Actual `q` unchanged. Full proof: `research/C280_RAO_PROMISE_RESTRICTION_AND_ENDPOINT_PALETTE_NO_GO_2026-09-27.md`.

## C-281 Ã¢â‚¬â€ Compatible native splices have a canonical owner-mask table

**Classification: CALIBRATION / GLOBAL-STRUCTURAL.** C-260's antichain grammar and context/proof substitution law can be expressed as a grammar over partial assignments in `{*,0,1}^N` with inconsistent joins sent to bottom. If context support K matches low table w and replacement support P matches low table w', then every compatible `K union P` accepts its whole completion cylinder. The mask `mu=Var(P)\\Var(K)` gives a canonical completion `h_mu=(mu?w':w)`, so `h_mu` must lie in `SIZE(s2)` and `CC(h_mu)<=CC(w)+CC(w')+CC(mu)+O(1)`. For fixed `(w,w')`, distinct masks restricted to their disagreement coordinates yield distinct low hybrids, hence at most `|SIZE(s2)|` compatible mask restrictions occur. This turns synchronization into a state-indexed owner-mask product problem, but gives no q-sensitive bound: parity lock and repeated-block equality remain safe. Actual `q=N-o(N)`. Full derivation: `research/C281_NATIVE_CYLINDER_GRAMMAR_AND_OWNER_MASK_FRONTIER_2026-09-27.md`.

**Priority checkpoint after C-280Ã¢â‚¬â€œC-281:** the latest steering supersedes the C-279 Route-A emphasis. The main route is global sharing/readout in the native cyclic closure, with owner-mask product rank as the live candidate invariant; the near-linear full-promise cover is the counter-program. Matching-to-LowExt, ordinary DAGs, and local widths are secondary. The actual bound remains `q=N-o(N)`; neither a q-charge nor a near-linear cover was found in these two claims.

## C-282 - Bottom-NO rail collision attempt (withdrawn by C-283)

**Original classification: ROUTE-KILL, now withdrawn.** The proof assumes that the bottom partial image pins the high completion's rail at a coordinate where a YES low code differs. A partial image may leave that coordinate blank, so the collision is not forced. See C-283 for an explicit one-bit counterexample to the claimed detector and a corrected decomposition.

## C-283 - Bottom-baseline holes and compatible low-code bypass

**Classification: COUNTEREXAMPLE.** The C-282 collision-detector implication fails for `phi(0)=empty`, `phi(1)=e(w)`: this obeys the abstract C-125 one-hot order for low `w` and disjoint high `z`, yet no collision occurs on YES. For `P=phi(0)` with `d` holes and `K={w in SIZE(s1):P<=e(w)}`, use pinned-coordinate collisions and test only the d hole rails for each compatible code. This separates the source with at most `a+(N-d)+K max(d-1,0)` AND gates. Since `K<=2^d`, a C-125 transfer proving `q>N^(1+epsilon)` must satisfy `N-d+K max(d-1,0)>N^(1+epsilon)`. Also, if `K>0`, a low code in K and the high bottom completion differ only on d coordinates; sparse-support interpolation therefore forces `d=Omega_beta(s2)` in the OPS gap. C-279 has `P=empty`, `K=SIZE(s1)`, and still fails through a short decoder, so this condition does not construct a useful map. C-282's route closure is invalid; actual `q=N-o(N)`.

## C-284 - Polynomial-dimension matching source window

**Classification: CONDITIONAL-TRANSFER.** Let the matching source side size be `v=N^delta`, with fixed `0<delta<min(beta,1-beta)`. Rao's cyclic lower bound is `L(v)>=exp(c N^(delta/2))`, dominating every polynomial map cost. A perfect-matching witness table encoded as a sparse indicator on edge-address coordinates has circuit size `O(v logN/logv)=O(v/delta)`, which fits `s1=N^beta/(c0 logN)` because `delta<beta`. Also, `r=N^delta` balanced address classes can all be chosen to have high indicator tables: `log binom(N,N/r)=Theta(N^(1-delta)logN)` exceeds `log|SIZE(s2)|=O(N^beta logN)` because `delta<1-beta`. Thus source dimension and high-code palette can both be polynomial in N, removing the polylog parameter bottleneck. A polynomial-AND C-125 map would yield `q>N^(1+epsilon)` for every fixed epsilon, but the map is still missing. The C-279 rank palette scales only by exposing a short source decoder, so it does not realize this transfer. Full parameter proof: `research/C284_POLYNOMIAL_DIMENSION_MATCHING_TRANSFER_WINDOW_2026-09-28.md`.

## C-285 - Projection-only expander overlap does not create synchronization rank

**Classification: ROUTE-KILL.** In a construction where each local view is a restriction of the same table to a coordinate set, pairwise compatibility means agreement on shared raw coordinates. Compatible tuples inject into one word on the union of those coordinates, so the overlap graph's edge count or expansion does not create extra degrees of freedom; per-coordinate spanning trees generate all equality checks. A safe splice cylinder still has at most `log2 |SIZE(s2)|` free coordinates. This kills expansion-only charges for projection views, but gives neither an O(N) full-promise cover nor a superlinear q bound. A surviving construction must enforce nonprojection coherence through explicit native derivations and charge those rules. Full argument: `research/C285_PROJECTION_OVERLAP_SYNCHRONIZATION_NO_GO_2026-09-28.md`.

## C-286 - Shared-DAG Rao approximation and complete polarity contradiction

**Classification: GLOBAL-STRUCTURAL / ROUTE-TEST.** Rao's matching construction does not give two-sided `Pr[tilde(Phi)!=Phi]` bounds. It gives directional YES under-approximation error at most `a*2^-t` and NO over-approximation error at most `a*4^t*epsilon`. Assigning one approximant to each distinct shared DAG node and propagating directional errors through OR and AND shows the union is charged only to the `a` paid AND nodes, with no `2N` factor. These directional bounds suffice: a YES density `p` rail DNF certificate is `pR`-spread, so `p>=theta_M=64 alpha_M(t+log2(1/xi))/v` forces NO firing with probability `1-xi`. Opposite-polarity exclusion, YES witness coverage, C-275 patching, and a union bound over dominant NO rails then give an exact canonical-table contradiction whenever `s1+A*r*n/log2(r+1)+B*n<=s2`, `r=ceil(N*(theta_M+delta1))`, `delta0<1-2xi`, and `Nxi+delta0<1`. For `v=Theta(log^2 N)`, `Ntheta_M=Theta(N/logN)`, outside the `Theta_beta(N^beta)` patch radius. Retire the polylog matching source with direct matching-indicator witnesses as the main route; alternative witness families are not ruled out. Full proof: `research/C286_DIRECTIONAL_SIMULTANEOUS_RAO_AND_POLARITY_THEOREM_2026-09-28.md`.

## C-287 - Rao clique spread amplification gives a canonical-table map-cost obstruction

**Classification: CONDITIONAL ROUTE TEST; transfer window unresolved (C-290).** Use the disjoint promise with `m=N^2`, `ell=ceil(D(log m)^2)`, and `k=2ell`; this satisfies `k>ell` and Rao's parameter conditions for large N. The shared directional approximation and spread amplification give `theta_C=Theta(log^3N/N^2)`, so `N theta_C=o(1)`. For `L0=(m/(k ell))^(t/3)` and `a<=L0/4`, the canonical table is within one bit of a low witness and sparse-support patching contradicts the high NO completion. Thus every valid C-125 map has `a>L0/4`. Unrolling only proves `CycAnd>=sqrt(L0/C)`, a lower bound below the map-cost floor; it does not upper-bound CycAnd and cannot retire the route. A color-coding monotone upper bound is `exp(O(k))*poly(m)`, above this floor at the displayed parameters. The interval and map construction remain open; actual `q=N-o(N)`. See C-287 and correction C-290.
## C-288 - ODDFACTOR span reconstruction is not yet LowExt reconstruction

**Classification: FRAMEWORK / ROUTE-BOUNDARY.** Define `CohEnc_{s1,s2}(f)` as the minimum AND cost of a monotone dual-rail map whose YES images contain a `SIZE(s1)` code and whose NO images sit below a code outside `SIZE(s2)`. Composition proves `rho_GapMCSP>=CycAnd(f)-CohEnc(f)`. ODDFACTOR has a `GF(2)` monotone span program of size `m=v^2`, each edge supplying `u_i+u_j` and target the all-ones vector; a solution can be chosen with at most `2v` edges. Babai-Gal-Wigderson prove monotone circuit complexity `m^(Omega(log m))`, a real span-program/decision separation. The direct rail map exposing whether a solution uses each edge has all NO rails zero, and ORing positive rails recovers ODDFACTOR at the map's same AND cost; this is exactly C-278's no-transfer obstruction. The availability map also admits the zero table on NO. No monotone two-sided primal/dual LowExt map or C-281-native-to-span-program valuation is known. Full analysis: `research/C288_ODDFACTOR_COHENC_AND_NATIVE_RECONSTRUCTION_BOUNDARY_2026-09-28.md`.

**Checkpoint after C-286-C-288:** actual `q=N-o(N)`. The required full two-sided Rao error statement was corrected to one-sided promise-direction guarantees; this correction still completes the polarity proof. Matching fails the small-beta source criterion for direct witness coding, and the clique source is closed for the C-125 transfer. A known `SpanRec << monotone decision` gap does not imply `CohEnc << CycAnd`. No superlinear `q`, useful LowExt map, native algebraic lower bound, near-linear full-promise cover, or P-vs-NP proof has been obtained. Next change mechanism: pursue a two-sided monotone primal/dual code or a comparable-decision lower bound for `CohEnc`; in parallel resume the full-promise cover search.

## C-289 crosswalk - Promise terms restate the existing safe-zone picture

**Classification: SYNTHESIS / ELEMENTARY COROLLARY; NOT A NEW CORE THEOREM.** The positive-term cylinder wording is a direct expansion of monotone separator semantics and is encompassed by C-244's proof/context state-zone factorization. The exact maximum safe-cylinder dimension `Theta_beta(N^beta logN)` is C-230's Lupanov/counting theorem. The additional observation that such a cylinder has more points than `SIZE(s1)` follows by comparing `log|SIZE(s1)|=O_beta(N^beta)` to the C-230 dimension; its excess points are medium. This makes raw volume counting useless but adds no q-sensitive cost. The genuine open obligation remains O-153/O-168/O-244. Actual `q=N-o(N)`; no near-linear cover or P-vs-NP proof. Crosswalk: `research/C289_SAFE_CYLINDERS_AND_PROMISE_COVER_FACTORING_2026-09-28.md`.

**Corollary to C-230 (not a new claim):** since `log|SIZE(s1)|=O_beta(N^beta)` but the largest safe-cylinder dimension is `Theta_beta(N^beta logN)`, such a cylinder can contain more tables than the entire low class; the extra completions lie in the medium band. This explains why total cylinder volume does not measure low-class coverage. It adds no q bound and the active missing cost is already O-153/O-244.

## C-290 - Clique transfer inequality and parameter audit

**Classification: PROOF AUDIT / ROUTE REOPENED.** The original C-287 positive-clique choice `k=ceil(2 eta_0 ell)` did not explicitly ensure disjointness `k>ell`; repair it to `k=2ell`. The canonical-table map-cost obstruction then holds on a valid promise. Separately, `CycAnd>=sqrt(L0/C)` is not `CycAnd<=L0/4`; the inference retiring clique was reversed. A color-coding detector gives `CycAnd<=exp(O(k))*poly(m)`, which does not resolve whether the actual cyclic complexity is above the encoder floor. No map, positive transfer, q improvement, or P-vs-NP proof follows. Full audit: `research/C290_CLIQUE_TRANSFER_AUDIT_AND_REOPENING_2026-09-28.md`.

## C-291 - ODDFACTOR's exponential monotone gap strengthens the source, not the map

**Classification: SOURCE UPDATE / ROUTE FILTER.** Cavalar-GÃƒÂ¶ÃƒÂ¶s-Riazanov-Sofronova-Sokolov prove `Match_v>=2^(v^(1/3-o(1)))` and transfer the argument to ODDFACTOR, with the published statement `2^(v^Omega(1))`; ODDFACTOR retains its linear GF(2) span program. Since q cyclic states unroll to `O(q^2(v^2+q))` monotone gates, `CycAnd(ODDFACTOR_v)>=2^(v^Omega(1))`. Setting `v=(log N)^K` for sufficiently large fixed K makes this dominate every fixed polynomial in N, while a solution supported on at most `2v` edges has a `polylog(N)` truth-table circuit and fits `SIZE(s1)` for each fixed beta. This is a much stronger conditional source window, but no C-125 map or `CohEnc` separation is constructed.

An explicit dual-certificate sidecar with YES auxiliary vector all-ones and NO auxiliary vectors consistent one-hot is a route-kill: `AND` of all auxiliary rails separates the promise in `2r-1` gates (or `2N-1` for N table coordinates), ignoring the hard graph. Thus a visible NO witness can erase the source lower bound even when it hashes to a high table. The live task is to derive variable NO rails monotonically from the original hard input, or prove an augmented source remains hard against this side-channel. Full derivation: `research/C291_ODDFACTOR_EXPONENTIAL_SOURCE_AND_WITNESS_SIDECAR_NO_GO_2026-09-28.md`.

## C-292 - ODDFACTOR opposite-rail certificates must union to a YES graph

**Classification: SCOPED STRUCTURAL LEMMA / ZERO-AND ROUTE FILTER.** For any positive certificates `A,B` of opposite rails at one truth-table coordinate, C-125 NO consistency forces the graph on `A union B` to be ODDFACTOR-YES, so it contains an odd-factor subgraph. Indeed, an edge set is contained in an odd-cut NO graph iff it has an odd-order connected component; equivalently, it avoids all odd cuts iff every component (including isolates) has even size. Thus opposite-rail evidence must jointly cover every source vertex in even components. With zero AND gates every rail certificate is empty or a single edge, so for `v>=3` no coordinate can have both rails nonzero; YES coverage then fixes one common low table, and its `N`-rail conjunction computes ODDFACTOR in `N-1` AND gates. C-291 contradicts this when `v=(log N)^K` for large fixed K. The OR-only corollary repeats the known C-125 principle; the exact certificate-union characterization is the useful constraint on positive-AND CohEnc. The GF(2) span witness does not fill zero rails: availability exposes support but leaves a blank at every omitted edge coordinate. No positive-AND lower bound, encoder, q improvement, or P-vs-NP proof. Full proof: `research/C292_ODDFACTOR_CERTIFICATE_COMPLEMENTARITY_AND_OR_ONLY_FILTER_2026-09-28.md`.

## C-293 - Certificate width gives a positive-AND CohEnc floor for ODDFACTOR

**Classification: PROVED COHENC LOWER BOUND / QUANTITATIVE ROUTE FILTER.** In a monotone acyclic circuit with `a` binary AND gates and free arbitrary-fanin OR, every nonzero output has a positive input certificate of width at most `a+1`: choose one true predecessor at each OR and both at each AND; after contracting OR paths, the connected proof DAG has at most `a` two-outdegree AND nodes, hence at most `a+1` leaves. If both rails at one C-125 ODDFACTOR coordinate are nonzero, C-292 forces each certificate union to be ODDFACTOR-YES, so it contains an odd-factor subgraph with at least `v` edges. Hence `2(a+1)>=v`, or `a>=ceil(v/2)-1`. If no coordinate has both rails active, every YES image contains one fixed low code and composing its `N` rails with the map separates ODDFACTOR using `a+N-1` AND gates. C-291's `2^(v^Omega(1))` cyclic lower bound exceeds `N+v` for `v=(log N)^K` and sufficiently large fixed K, so this fixed-polarity case is impossible below the threshold. Therefore `CohEnc_{s1,s2}(ODDFACTOR_v)>=ceil(v/2)-1` at that source scale. This is only a polylogarithmic lower bound at the chosen parameters; shared pair counting and the superpolynomial gap remain open. Full proof: `research/C293_ODDFACTOR_CERTIFICATE_WIDTH_COHENC_FLOOR_2026-09-28.md`.

**General form (proved in C-293):** For any monotone source `f`, let `W(f)` be its minimum positive-certificate width and `L=CycAnd(f)`. A C-125 map with `N` table bits and cost `a` satisfies `a>=min(ceil(W(f)/2)-1, L-N+1)`: a doubly-supported coordinate gives two width-`a+1` certificates whose union forces `f=1`; otherwise fixed rail polarities yield the `a+N-1` source separator. For ODDFACTOR, `W=v` and C-291 makes the second term larger, giving the stated floor.

## C-294 - Odd-cut NO-extension consensus gives a valid template but hard affine rails

**Classification: NEW TEMPLATE / SCOPED OBSTRUCTION.** Assign a high table to every odd-cut NO extension. For any input G, activate a signed rail exactly when all compatible odd-cut NO extensions above G have the same bit there. Removing compatible extensions under edge addition makes this a monotone map; YES graphs have no compatible odd cut and therefore full conflict, while every NO image lies below each compatible high label. For affine labels z_[S](j)=R_j xor |S intersect A_j| mod 2 with balanced A_j, consensus is controlled by q=0 or q=p on the component-parity affine hyperplane. On a restriction that leaves the larger of A_j and its complement as an arbitrary ODDFACTOR instance and fixes a perfect matching on the other side, one of these rails equals ODDFACTOR_h for h>=v/2. Converting the cited ordinary monotone size bound to the project AND-only cost by flattening OR regions still forces superpolynomial AND cost at v=(log N)^K. This retires only the affine cut-consensus map; cheaper submaps may omit consensus pins and nonlinear labels remain open. Full derivation: research/C294_ODD_CUT_CONSENSUS_AFFINE_RAIL_OBSTRUCTION_2026-09-28.md. Actual q=N-o(N); no P-vs-NP proof.

## C-295 - Coherent two-code affine consensus forces hard submaps

**Classification: SCOPED ENCODER NO-GO.** Fix one balanced set A across all truth-table coordinates and label an odd cut by R or complement(R) according to the parity of its intersection with A. A random R can be chosen so both tables are outside SIZE(s2); there are only two labels to union-bound. The consensus map has YES output all rails and NO output e(R), e(complement(R)), or zero. For every pointwise submap F that covers each YES input with some SIZE(s1) code, define U as the OR of F's rails opposite R and V as the OR of rails opposite complement(R). Both U,V are 1 on YES because the low table differs from both high tables. On NO, F is below one of the two one-hot labels or zero, so U AND V is 0. Thus U AND V computes ODDFACTOR with one additional AND gate. The matching-sunflower theorem gives ordinary monotone size 2^(v^c) for some c>0; flattening OR-only regions converts an a-AND decoder to size O((a+1)(v^2+a)), forcing a=2^(Omega(v^c)). For v=(log N)^K and sufficiently large fixed K this is superpolynomial in N. This closes the pointwise-submap escape only for the coherent two-code affine consensus family. Coordinate-dependent labels, non-submap C-125 maps, and nonlinear labels remain open. Actual q=N-o(N); no transfer or P-vs-NP proof. Full derivation: research/C295_TWO_CODE_AFFINE_CONSENSUS_SUBMAP_DECODER_2026-09-28.md.

**Finite-envelope corollary (C-295):** For any C-125 monotone map whose NO images are each below one of k fixed high tables, the source equals the AND over those k labels of the OR of rails conflicting with each label. This costs at most k-1 additional binary AND gates. If A(f) is the source AND-count lower bound and the envelope size is k, the map cost g obeys g >= A(f)-k+1; in particular, k <= A(f)/2 forces g >= A(f)/2. For odd-cut labels, the possible envelope size can exceed the current ODDFACTOR lower bound, so this corollary does not settle coordinate-dependent or nonlinear families.

## C-296 - Odd-cut blocker map is valid; fixed low code forces source cost

**Classification: VERIFIED C-125 CONSTRUCTION / ROUTE NO-GO.** Let C be the odd-cut classes and choose U_j subset C. Label T by z_T(j)=1 iff T is in U_j, and set F_(j,0)=AND over T in U_j of the cut-crossing predicate X_T, with F_(j,1)=0. YES graphs cross every odd cut, so e(0)<=F. On a NO graph, any odd component T is compatible; every active zero rail has T not in U_j, hence agrees with z_T and F<=e(z_T). Random U_j give uniformly random labels, and a union bound makes all labels high when v+s2 logN=o(N). But e(0) is the same low code on every YES input, while each NO output has a blank at a coordinate where its compatible high code has bit 1. Therefore ODDFACTOR=AND_j F_(j,0), so a map with g AND gates gives a source circuit with g+N-1 gates. The known source lower bound forces g=2^(v^Omega(1)) for v=(logN)^K with K large. Random direct formulas use about N*2^(2v-3) AND gates; no shared-circuit lower bound is claimed. The result rules out fixed-zero cut blockers, not variable-low-code maps. Full derivation: research/C296_ODD_CUT_FAMILY_BLOCKER_MAP_AND_FIXED_CODE_NO_GO_2026-09-28.md.

## C-297 - Dual code-envelope decoders give a necessary map tradeoff

**Classification: PROVED SOURCE-DECODER TRADEOFF.** Let W be r low codes covering all YES images of a C-125 map, and H be k high codes covering every NO image. For each z in H, OR the rails conflicting with z; AND over H. This computes the source with k-1 extra AND gates, so g>=A(f)-k+1. For each w in W, AND the N rails matching w; OR over W. A NO image cannot contain a low code because e(w)<=F<=e(z_high) would force w=z_high. This second decoder costs r(N-1) additional AND gates, giving g>=A(f)-r(N-1). Together g>=A(f)-min(k-1,r(N-1)). It is necessary but does not rule out the full SIZE(s1) and high-table envelopes. Full proof: research/C297_DUAL_CODE_ENVELOPE_DECODER_TRADEOFF_2026-09-28.md.

## C-298 - Subgraph-lifted odd-cut consensus has an exact matching-fiber criterion

**Classification: NEW MONOTONE TEMPLATE / AFFINE ROUTE NO-GO.** Assign each odd cut a high code z_T. At input G, a rail (j,b) is active when some subgraph H subseteq G has a nonempty compatible-cut family on which bit j is unanimously b. Monotonicity follows by retaining H; on NO, C(G) is contained in C(H), so all active rails agree with every compatible high code z_T. Equivalently, the rail is OR_T of AND_T' X_(delta(T') minus delta(T)), over labels b and 1-b. On a perfect matching M, it is active iff some label-b cut T has no opposite-labelled T' with B_M(T') subseteq B_M(T).

For affine cut labels c+|T intersect A| mod 2, any matching edge crossing A can be toggled at both endpoints to obtain an oppositely labelled cut with the same matching boundary; this kills both rails. Since every nontrivial A has a crossing edge contained in some perfect matching, full low-code coverage on all matching inputs forces each A to be empty or all vertices. Then every high label is the same table R and the lift outputs e(R) everywhere; adding witness rails that vanish on NO makes their opposite-R OR a source decoder. Thus this affine lift has no transfer margin. Nonlinear labels and arbitrary maps remain open. Full proof: research/C298_SUBGRAPH_LIFTED_ODD_CUT_CONSENSUS_MATCHING_FIBER_NO_GO_2026-09-28.md.

## C-299 - Global polarity on matching fibers kills nonlinear lifted consensus

**Classification: PROVED STRUCTURAL THEOREM / SCOPED ROUTE-KILL.** On a perfect matching M, C-298's lifted rail is active iff some singleton-boundary fiber F(M,e) is monochromatic. For matchings M,M' whose union is one alternating 2v-cycle, every F(M,e) intersects every F(M',f), via the odd cut consisting of the vertex interval between e and f. Thus a mono fiber of color b in M forces every mono fiber in M' to have color b; if M has both colors, M' has none. For even v>=6 the graph generated by relative v-cycles is connected: v-cycles normally generate S_v, because they generate a normal subgroup containing a nonidentity even element and an odd element, and A_v is simple. Therefore every coordinate has a unique polarity b_j available on every perfect matching.

A C-125 map D must then output exactly e(b) on every perfect matching; the low YES condition forces b in SIZE(s1). The monotone circuit AND_j D_(j,b_j) accepts every perfect matching and rejects every odd-cut NO graph, using a+N-1 AND gates. This is enough: Cavalar et al. explicitly state the matching lower-bound proof only needs correctness on the support of the perfect-matching/odd-cut distributions, where Match and Odd agree. Flattening free OR regions transfers their 2^(v^(1/3-o(1))) lower bound to a superpolynomial AND-cost for even v=(log N)^K, K>3. This does not assert every Odd YES graph has a perfect matching. It closes C-298's pure lift for arbitrary nonlinear labels, not arbitrary C-125 maps or a D OR W witness sidecar. Full proof: research/C299_MONO_FIBER_POLARITY_GLOBAL_PROPAGATION_2026-09-28.md.

## C-300 - Rao/odd-cut distribution mismatch (route-kill withdrawn)

**Classification: WITHDRAWN ROUTE-KILL / CONDITIONAL EXPANSION LEMMA.** The attempted proof applied C-286's Rao approximation error on Rao's `G(W)` NO distribution to sidecars known to vanish on Cavalar's odd-cut NO distribution. These are different distributions, so the claimed sparse exceptional matching set was not established. The matching-graph expansion/deletion calculation remains conditional on an independently proved sparsity premise; it does not close O-176. Do not cite C-300 as an encoder lower bound. C-301 later treats arbitrary C-125 maps using Cavalar's approximation directly on the matching/odd-cut pair. Full audit: `research/C300_RAO_EXPANSION_KILLS_NO_VANISHING_SIDECARS_2026-09-28.md`.

## C-301 - Short-term overlap forces global polarity in every ODDFACTOR C-125 map

**Classification: PROVED QUANTITATIVE MAP LOWER BOUND / ROUTE FILTER.** Use Cavalar et al.'s gatewise matching-sunflower approximation on the shared DAG, with its errors charged per node rather than per output rail. For width `w`, a circuit of size at most `2^w` has matching-DNF rails that are `r`-small, meaning at most `r^ell` terms of each width `ell`, with `r=O(w^3 log^2 v)`. Each paired opposite-polarity terms of width at most `w` fires together on at least `2^(-2w)` of odd-cut NO inputs. At the explicit choice `w=floor(v^(1/3)/log v)`, `r=O(v/log v)=o(v)` and the total NO over-approximation error is `o(2^(-2w))`. Hence no coordinate has terms in both polarities.

YES directional correctness then forces one complete low table b across all but `o(1)` of perfect matchings. The conjunction of its original rails rejects every odd-cut NO input and accepts `1-o(1)` of perfect matchings. Applying the same approximation theorem to this decoder contradicts Cavalar et al.'s `1/2+o(1)` DNF agreement cap. Thus its circuit size exceeds `2^floor(v^(1/3)/log v)`, giving `a+N+v^2+1 >= Omega(2^(v^(1/3)/(2 log v)))`. For `v=(log N)^K`, fixed `K>3`, this rules out every polynomial-cost C-125 ODDFACTOR map, including arbitrary NO-active rails.

This is a strong `CohEnc` lower bound, not a successful transfer: no positive `CohEnc` versus true `CycAnd` margin follows. The actual `q=N-o(N)` bound is unchanged; no P-vs-NP proof follows. Full quantitative proof: `research/C301_SHORT_TERM_OVERLAP_FORCES_GLOBAL_POLARITY_2026-09-28.md`.

## C-302 - Raw owner-mask rank cannot yield a superlinear state bound

**Classification: INVARIANT FILTER / NEGATIVE CALIBRATION.** Each owner mask is an N-bit vector, so the `GF(2)` rank of any set of individual masks is at most N; that statistic alone cannot imply `q>N^(1+epsilon)`. More strongly, C-257's parity-lock promise has `2^(N-1)` safe canonical hybrids spanning the entire even-parity subspace of dimension `N-1`, while its explicit native cover uses `4N-4` pairs. The proof cuts a successful derivation for each even anchor into a context and replacement proof; their compatible join fixes that anchor, so each even table occurs as a safe diagonal hybrid. Thus large affine dimension is compatible with linear q in the calibration.

This does not rule out an actual-promise theorem that charges owner-mask *selection complexity* to shared states. It retires raw mask rank and hybrid affine dimension as standalone routes. The next native algebraic attempt must exploit global circuit-description coherence and survive C-257/C-258. No actual q bound changes. Full audit: `research/C302_RAW_OWNER_MASK_RANK_CEILING_2026-09-28.md`.

## C-303 - Promise-separator evaluation does not supply an SoS refutation

**Classification: PROOF-COMPLEXITY BRIDGE FAILURE / PARAMETER FILTER.** A native cover separator is constrained only on `CC(u)<=s1` and `CC(u)>s2`; its behavior on medium tables is arbitrary. So `h_Q(e(z))=0` for a high z does not refute `Circuit_s2(z)`: a medium table u can satisfy `CC(u)<=s2` and still be rejected by h_Q. A q-state evaluation trace is not an algebraic unsatisfiability certificate. Austrinâ€“Risse's SoS degree lower bound applies to refuting the circuit-existence formula for an individual hard function, while their size lower bound also needs a small errorless heuristic circuit and a specified error count. At `s2=N^beta`, the degree threshold `N^(beta(1-epsilon))` is below the existing linear q floor for fixed beta<1. Reviving the route requires a sound medium-band totalization and a stronger parameter window. No q change. Full audit: `research/C303_GAP_SEPARATOR_TO_SOS_BRIDGE_AUDIT_2026-09-28.md`.

## C-304 - Compatible-support proofs embed as monomial ideals, but not scalar span valuations

**Classification: EXACT ALGEBRAIC REPRESENTATION / ROUTE FILTER.** The C-281 antichain semiring of consistent partial assignments has a faithful realization by monomial ideals in the algebra with basis `m_S` for the `3^N` consistent supports and multiplication `m_S m_T=m_(S union T)` when compatible, zero otherwise. Alternative proof is ideal sum; compatible proof composition is ideal product. A complete anchor w is accepted exactly when its input-dependent full-table monomial `m_ell(w)` belongs to the output ideal. The algebra is exact but exponential-dimensional and is not a classical span program with a fixed target and input-selected rows. Moreover, any unital semiring homomorphism from the idempotent support semiring to a field is trivial: `x+x=x` forces `phi(x)=0` by additive cancellation. Thus scalar GF(2) valuation cannot preserve OR-alternative and proof composition. The C-257 parity calibration also shows top-degree rank is useless by itself: `2^(N-1)` accepted full-table monomials coexist with `4N-4` native pairs. No q improvement; a revival needs a compressed ideal/tensor invariant that tracks actual low-circuit description selection and passes C-257/C-258. Full proof: `research/C304_IDEMPOTENT_SUPPORT_ALGEBRA_AND_SPAN_PROGRAM_BRIDGE_2026-09-28.md`.

## C-305 - Native closure is an AND-OR reachability game; explicit circuit evaluation has a gate-address product

**Classification: EXACT SEMANTIC REFORMULATION / SCOPED CONSTRUCTION FILTER.** The q-state recurrence is a reachability game: at each active rule, the universal player chooses a side and the existential player supplies a matching seed or active predecessor; decreasing activation rank guarantees termination. A direct verifier for a fixed size-s circuit against all N table coordinates uses gate-address positions, `Theta(Ns)` states. At `s=s1=N^beta/(c logN)`, this is `N^(1+beta-o(1))`, too large for O-168. If gate positions are shared across addresses, the seed query loses the challenged address; if they are duplicated, a strategy can choose different gate wiring per address. C-281 proof/context supports are the only identified compression site, but all compatible splices must remain SIZE(s2). This does not lower-bound arbitrary covers: C-257/C-258 show compact global fingerprints can protect extensive reuse. No q change or P-vs-NP result. Full audit: `research/C305_ALTERNATING_EVALUATION_AND_ADDRESS_MEMORY_AUDIT_2026-09-28.md`.

## C-306 - Proof supports cannot act as a conditional address register

**Classification: SCOPED NO-GO / CORRECTION TO C-305 CANDIDATE.** For a fixed table w, every context support K and replacement proof P at a reused state that matches w is a subset of `ell(w)`. Thus K union P is always consistent; the same-anchor context/proof compatibility relation is the complete product. C-281 substitution makes every such splice a safe accepted proof. Moreover, the recurrence activates states using only seed-existence bits and predecessor-state bits; it does not inspect the support content. Hence support tags cannot make a shared state route conditionally on the address branch. A per-address witness can degenerate from `exists one d for all x` to the vacuous `for all x exists d_x`; supports do not enforce their equality. This kills only support tags as control memory, not arbitrary O-168 covers. C-257/C-258 remain valid calibrations. No q improvement. Full proof: `research/C306_SUPPORTS_CANNOT_STORE_CONTROL_STATE_2026-09-28.md`.
## C-307 - AND-count separator compiler and compatible-code route boundary

**Classification: EXACT MODEL BRIDGE / ALGEBRAIC ROUTE FILTER.** For a promise whose high side meets every signed literal half-cube, an acyclic monotone separator with a binary AND gates and arbitrary-fan-in free OR gates compiles into a native cover with at most a pairs: assign each AND gate the two high-side carrier sets of its inputs, then induct over the low-table derivation. The known unrolling gives A_cap<=rho_prom^2, so sqrt(A_cap)<=rho_prom<=A_cap. This sharpens the separator-to-cover compiler but leaves the exponent target unchanged; a lower bound above N^(2+2epsilon) is needed to force rho_prom>N^(1+epsilon).

The code-polynomial arithmetic lower bound does not transfer directly to C-281: arithmetic multiplication retains every positive cross-term, whereas incompatible partial-support products vanish. Bounded-width local-constraint promises also have signed monotone CNFs and O(N)-pair covers when there are O(N) forbidden local patterns. Hence distance, rate, and arithmetic hardness alone are not source lower bounds for the native grammar. The actual OPS result remains N-o(N); no near-linear OPS cover or P-vs-NP proof follows. Full derivation and scope: research/C307_COMPATIBLE_CODE_POLYNOMIAL_TRANSFER_AUDIT_2026-09-28.md.


**C-307 expander-code calibration.** A binary expander-code family of positive rate and positive relative distance has O(N) constant-weight parity checks. Its code-membership separator is a conjunction of O(N) signed local clauses, so C-307's compiler gives q=O(N). For the promise C versus its complement, soundness forces every accepting support to be a full codeword: any partial cube contains two points at distance one, while distinct codewords are farther apart. Thus the grammar yields exponentially many distinct full supports with linear q. This is a calibration against certificate-count and distance-based lower bounds, not an OPS reduction. Primary source: https://www.cs.yale.edu/homes/spielman/PAPERS/expandersIT.pdf.


**C-307 restricted separator lower bound.** A monotone CNF on signed truth-table literals separating SIZE(s1) from the complement of SIZE(s2) must have every non-tautological clause width greater than K=floor(s1/(4n)), n=log2N: any falsifying pattern on at most K coordinates extends to a low table by hardcoding its at most K one-addresses, at cost at most 3Kn<=s1. Each clause then rejects at most 2^(-(K+1)) of uniform tables, while Z has density 1-o(1); hence at least (1-o(1))2^(K+1)=2^(Omega(N^beta/log^2N)) clauses are needed. This is superpolynomial for fixed beta>0, but it applies only to CNFs, not general acyclic circuits with shared AND nodes or native q-state closure. It blocks direct local-clause enumeration and leaves the global-sharing question open.

## C-308 - Matching-sunflower approximation in paid-AND measure

**Classification: PROVED RESOURCE REFINEMENT / STRONGER ODDFACTOR C-125 LOWER BOUND.** Cavalar et al.'s matching approximation extends to a shared monotone DAG with binary AND gates and arbitrary-fan-in, free OR gates. At each paid AND node, the family of width-at-most-2w matching terms has at most v^(6w) distinct members. Plucking with sunflower error v^(-10w) makes its D0 overapproximation error at most v^(-4w); truncating to width w loses at most q^(w+1)/(1-q) on D1, where q=e*O(w^3 log^2v)/v. The union over failures is over paid AND nodes only. OR-only paths and OR roots are exact unions; AND roots reuse their already-counted node approximation, so there is no OR-fanin or 2N-output multiplier.

For any valid ODDFACTOR C-125 map of AND-cost a with N coordinates, if a+N-1<=2^w then paired opposite-polarity terms force at least 2^(-2w) odd-cut NO mass, exceeding the shared-node error. Thus every coordinate has one polarity; YES coverage fixes one low table b on almost all perfect matchings. The conjunction of its original rails rejects all odd-cut NO inputs and accepts 1-o(1) of D1. Applying the same approximation theorem to that separator contradicts the o(v)-small-DNF agreement cap. Therefore a+N-1>2^w.

For `w=floor(v^(1/3)/(log v)^(2/3+gamma))`, any fixed `gamma>0`, the smallness is `r=O(v/(log v)^(3gamma))=o(v)`. With `v=(log N)^K`, `K>3`, the encoder lower bound is superpolynomial in N. This improves C-301 by removing its fan-in-two square-root loss. It does not give a C-125 encoder upper bound or `CohEnc<CycAnd` margin; actual `rho_GapMCSP=N-o(N)`, and no P-vs-NP proof follows. Full proof: `research/C308_AND_COUNT_MATCHING_APPROXIMATION_AND_COHENC_2026-09-28.md`.

## C-309 - A one-orbit distributional separator exactifies at logarithmic orbit cost

**Classification: EXACT SYMMETRIZATION THEOREM / SOURCE-SELECTION CRITERION.** Let a finite group G preserve a monotone source f and act transitively on its L inclusion-minimal YES inputs. If a monotone circuit Q with a paid AND-count a rejects every NO input and accepts at least 1-eta of a uniform minimal YES input, then ORing t=floor(log L/log(1/eta))+1 random G-relabeled copies yields an exact separator for some choice of relabelings. For each minimal YES input the miss probability is at most eta^t; L*eta^t<1. Monotonicity extends acceptance to all YES inputs, while G-invariance preserves rejection of all NO inputs. Thus `CycAnd(f)<=t*a`.

For MATCH_v, perfect matchings form one orbit, so the C-308 extracted one-sided separator from any C-125 map exactifies at `O(v log v)(a+N-1)` AND gates. ODDFACTOR has other minimal-witness orbits: for v>=4, a spanning forest made from K_(1,3), K_(3,1), and v-4 disjoint matching edges is minimal and not isomorphic to a perfect matching. The matching distribution therefore yields only a hard MATCH subfunction, not an exact Odd separator. Candidate sources should have one manageable minimal-witness orbit, few well-covered orbits, or a selected orbit whose upward closure contains every YES input. This is a source filter only: no C-125 map, positive CohEnc/CycAnd margin, q improvement, or P-vs-NP proof. Full proof: `research/C309_ORBIT_COVERAGE_AND_DISTRIBUTIONAL_DECODING_2026-09-28.md`.

## C-310 - Odd-cut term mass tightens the ODDFACTOR encoder bound

**Classification: PROVED PARAMETER SHARPENING / TERM-MASS ROUTE.** Every partial matching M of `ell<v` edges fires on exactly `2^(-ell)` of the odd-cut distribution D0. Thus a matching-DNF of width `w<v` with D0 mass below `2^(-w)` has no terms. Use the C-308 paid-AND approximation with `eps_sun=v^(-10w)`, giving per-node D0 error `v^(-4w)`, and choose `w=floor(c v^(1/3)/(log v)^(2/3))` for small fixed c so `q=e*O(w^3 log^2v)/v<=1/16`. No `r=o(v)` condition is needed; the D1 deletion tail is geometric for q<1.

If a C-125 ODDFACTOR map had `a+N-1<=16^w`, opposite-polarity short terms force at least `2^(-2w)` NO mass and hence global polarity. YES coverage fixes a common low code b; its rail conjunction Q rejects every odd-cut NO input and accepts at least 14/15 of perfect matchings. A second approximation to Q has D0 false-positive mass below `2^(-w)`, so its width-w matching-DNF has no terms, while the D1 underapproximation guarantee forces it to accept at least 13/15 of matchings. Contradiction. Therefore `a+N-1>16^w=exp(Omega(v^(1/3)/(log v)^(2/3)))`. This sharpens C-308 by removing the `gamma>0` slack and agreement-cap step. It still does not produce an encoder upper bound, a CohEnc/CycAnd margin, any q improvement, or a P-vs-NP proof. Full proof: `research/C310_ODD_CUT_TERM_MASS_TIGHTENS_COHENC_2026-09-28.md`.

## C-311 - Universal dual-consensus reconstruction has a one-gate exact decoder

For a monotone span program, let `Y_X` be the dual separator set. It is empty iff the source accepts and decreases under input inclusion. Given any table label c(y) for each dual witness, define monotone output rails by `Phi_(j,b)(X)=1` iff every `y in Y_X` has `c(y)[j]=b`. On YES, both polarities fire at every coordinate, so any low table is dominated. On NO, any selected y gives `Phi(X)<=e(c(y))`; if all c(y) are outside `SIZE(s2)`, this is a valid high completion.

However, for any fixed coordinate j, `f=Phi_(j,0) AND Phi_(j,1)`: both rails are true when `Y_X` is empty, and cannot both be true on a nonempty dual set. Therefore any such map of AND count a yields an exact monotone source separator with at most a+1 gates, so `CohEnc(f)>=CycAnd(f)-1`. This is a proof-level no-go for universal dual consensus as a reconstruction-gap construction, independent of the complexity of the codebook. See `research/C311_UNIVERSAL_DUAL_CONSENSUS_MAP_AND_DECODER_NO_GO_2026-09-28.md`.

## C-312 - Single-literal guard implies a factor-two decision upper bound

Suppose a C-125 map of AND cost a maps all NO inputs to zero on slice `x_r=0`, and has both fixed-coordinate rails active on every YES input in slice `x_r=1`. On the first slice, the free OR of the rails computes `f_0`; on the second, the pair AND computes `f_1` with one extra gate. Monotonicity gives `f=f_0 OR (x_r AND f_1)`, so `CycAnd(f)<=2a+2`.

The guarded dual-consensus pattern `P_(j,b) OR (x_r AND U_(j,b))`, with NO-vanishing primal rails P and universal dual rails U, satisfies these hypotheses. It is a valid construction pattern but only yields a constant-factor decision/reconstruction comparison; it does not exclude a factor-two transfer and no ODDFACTOR cost improvement is known. See `research/C312_SINGLE_GUARD_COFACTOR_TRANSFER_2026-09-28.md`.

**C-312 ODDFACTOR fixed-edge cofactor:** Let e=(l*,r*) be fixed. In the `x_e=0` restriction, reserve four vertices on each bipartition side including l*,r*, make those two vertices leaves in disjoint opposite `K_(1,3)` and `K_(3,1)` stars, set every cross-block edge to zero, and leave the residual `(v-4) x (v-4)` block as an arbitrary graph. The fixed component is an odd factor and avoids e; the whole graph has an odd factor iff the residual graph does. Hence `ODDFACTOR_(v-4)` is a monotone projection of the cofactor. Any map whose NO outputs vanish on that slice has AND count at least `A_ac(ODDFACTOR_(v-4))`. This is a route-specific hard-slice bound, not an additive `CohEnc/CycAnd` comparison. See C-312.

## C-313 - Arbitrary monotone guard is not a literal cofactor

The C-312 decoder `CycAnd(f)<=2a+2` uses the positive Shannon identity for a source literal. For a general monotone guard g, separating the g=0 cofactor from g=1 NO decoy inputs needs a negative selector, so the same proof does not follow. Specifically, let D be the OR of all output rails and R a fixed opposite-rail AND. If a YES g=0 input and a NO g=1 input both have D=1,R=0, their `(D,R,g)` vectors are ordered `(1,0,0)<=(1,0,1)`, which no monotone function of these aggregate signals separates. This does not rule out a decoder using the full rail vector or a controlled literal-cofactor family. It filters only the proposed arbitrary-guard shortcut; actual q remains `N-o(N)`. Full boundary: `research/C313_ARBITRARY_GUARD_IS_NOT_A_LITERAL_COFACTOR_2026-09-28.md`.

## C-314 - Prefix-block safe envelope for O-168

For `k=Theta(log N)` prefix blocks with k chosen so `k*s1<s2`, define A_k by requiring every restricted block truth table to have circuit size at most s1. Constant restriction gives `SIZE(s1) subseteq A_k`; separate block circuits plus a prefix selector give `A_k subseteq SIZE(s2)`. Therefore every high z has a prefix block with restricted complexity >s1. This is a proved safe-envelope lemma. It does not produce a native closure rule for selecting the hard block: a free test for block complexity is not among the literal seeds, and explicit gate-address evaluation costs `Theta(N*s1)`. No q change. See `research/C314_PREFIX_BLOCK_SAFE_ENVELOPE_AND_SELECTOR_BOTTLENECK_2026-09-28.md`.

## C-315 - Prefix blocks expose a local constant-gap bottleneck (28 September 2026)

**Proved reduction.** For `k=Theta(log N)` blocks and `t0=floor((s2-O(k log k))/k)`, every global low table restricts to a block function in `SIZE(s1)`, while every global high table has at least one block of complexity above `t0`; otherwise separate synthesis puts the whole table in `SIZE(s2)`. A local monotone separator over signed block literals for `SIZE(s1)` versus `CC>t0` can therefore be copied k times and ANDed, using at most `k*a+(k-1)` AND gates when its cost is a. By C-307 this gives a native cover of at most that many pairs. The ratio `t0/s1=c0 log N/k+o(1)` is constant at k=Theta(log N). This is a conditional upper reduction, not a construction or lower bound.

**Counting calibration.** For every fixed `0<beta<1`, constants `B>1` and `A>B` can be chosen so that some `z` is globally above `s2` but every one of its k block restrictions has complexity in `(B*s1,A*s1]`. Inside each block, use arbitrary functions on a fixed u-dimensional address subcube: Lupanov gives size `O(n_b+2^u/u)` for a family of cardinality `2^(2^u)`. Set `2^u=Theta(A*s1 log s1)`, discard the at most `2^(O(B*s1 log s1))` locally small functions, take independent block choices, and compare the product count `2^(Omega(k*A*s1 log s1))` against `|SIZE(s2)|<=2^(O(s2 log s2))`. Large enough fixed A makes the product contain a high table; `A*s1=o(s2)`. Thus high tables need not have a block with superconstant-factor complexity over s1. The exact `>s1` selector question remains.

**Limit.** The construction creates no native q charge. It refines C-314 to a blockwise constant-gap problem and makes the missing step explicit: prove a q-sensitive direct-sum/coherence theorem for the local separators or construct a shared selector beating k copies. Actual `rho_GapMCSP=N-o(N)`. Full proof: `research/C315_PREFIX_BLOCK_CONSTANT_GAP_AND_DISTRIBUTED_HARDNESS_2026-09-28.md`.

## C-316 - Exact algebraic fingerprints preserve address dimension (28 September 2026)

**Algebra lemma.** For `B=F_2^N` with pointwise operations, its N coordinate indicators are pairwise orthogonal idempotents. Any finite family of unital algebra homomorphisms into finite-dimensional commutative `F_2`-algebras that detects every table difference has an injective product map; the images of the N indicators are nonzero orthogonal idempotents and hence linearly independent. The total target dimension is at least N. If each target is a field, every homomorphism is evaluation at one address.

**Promise-specific sketch lemma.** If a linear map `L:F_2^N -> F_2^d` is used by the separator `accept z iff L(z)=L(w)` for some `w in SIZE(s1)`, then soundness and `0 in SIZE(s1)` imply `ker L subseteq SIZE(s2)`. Thus `N-rank(L)<=log2|SIZE(s2)|=O(s2 log(s2+n))`, so `rank(L)>=N-o(N)`. Explicit gate-by-coordinate evaluation costs `O(N*s1)`.

**Scope.** These facts filter exact-difference algebra-homomorphic fingerprints, linear equality sketches, and the explicit evaluator. They do not lower-bound arbitrary nonlinear separators or native fusion q. Full proof and limits: `research/C316_ALGEBRAIC_FINGERPRINT_ROUTE_FILTER_2026-09-28.md`.
## C-317 - Product safe cylinders saturate the blockwise splice-entropy budget (28 September 2026)

Let k=Theta(log N) prefix blocks and choose a u-dimensional suffix subcube in each, with `2^u=Theta((s2/k) log(s2/k))`. Every arbitrary labeling of the k free subcubes is computed by k local Lupanov circuits and a prefix mux in total `O(k n + k 2^u/u)<=s2`, for a sufficiently small constant in the subcube size. Thus a sound cylinder with `Theta(s2 log s2)` independently variable table coordinates exists across all blocks; this matches the global counting ceiling. Separately, the C-315 moderate-hard product family is globally high with probability `1-2^(-Omega(s2 log N))` after its constants have an exponent margin, while repeated identical blocks can share one small global circuit. These facts retire block count/free-coordinate entropy as standalone direct-sum charges. The remaining Q177 target is description-coherence of block restrictions under the C-281 compatible-product grammar. No q improvement or P-vs-NP result follows. Full proof: `research/C317_BLOCKWISE_SAFE_CYLINDER_TENSORIZATION_2026-09-28.md`.
## C-318 - Cofactor ensembles exactly repackage global circuit size (28 September 2026)

For `f:{0,1}^{r+m}->{0,1}`, define its k=2^r prefix restrictions `F(y)=(f(a,y))_a`. In a k-lane circuit with coordinatewise AND/OR/NOT, diagonal suffix inputs, and fixed prefix-bit lane masks, the minimum vector-gate count equals `CC(f)`: scalar circuits lift gatewise; conversely scalarizing each vector wire by the input prefix selects the corresponding lane and uses the same gates. This turns the C-315 block product into a shared cofactor-ensemble problem. The C-281 closure has a different SIMD algebra on partial-assignment support vectors: alternative is family union, and a paid state performs compatibility-filtered coordinatewise support union. No transfer or q bound is established; arbitrary endpoint sets may couple lanes globally, as in C-257. Full formulation: `research/C318_COFACTOR_ENSEMBLE_AND_NATIVE_SIMD_MODEL_2026-09-28.md`.

Reindexed promise: with `E_s={F:V_k(F)<=s}`, a support is a product box across the block lanes. Completeness covers `E_s1`; soundness puts every generated box inside `E_s2`. The q-state problem is an interpolation-cover problem over the compatible-box algebra; it is exact reformulation only.

## C-319 - Native closure is an alternating cofactor game (28 September 2026)

For each pair `(E_i,H_i)`, set `T_i=E_i intersect H_i`; let `A_i(w)` and `B_i(w)` be the disjunctions of matching literal slices contained in the respective endpoints; and let `P_i^E={j:T_j subset E_i}`, `P_i^H={j:T_j subset H_i}`. The exact closure iteration is

```text
x_i^(t+1)=(A_i OR OR_(j in P_i^E)x_j^t) AND
           (B_i OR OR_(j in P_i^H)x_j^t),   x^0=0.
```

The output ORs the active empty-consequence states. This is a least-fixed-point, input-labelled alternating reachability game with q states; each universal move chooses an endpoint obligation and each existential response supplies a true literal seed or a predecessor state. An endpoint's seed is a consistent disjunction of signed table bits unless the endpoint is all of U, in which case it is true. Clauses can mix every prefix lane. Unrolling q rounds gives at most q^2 AND gates, so ordinary monotone-circuit lower bounds transfer with a square-root loss only.

**Invariant ceilings.** A sound-box cover of `SIZE(s1)` has a singleton-box cover with at most `|SIZE(s1)|` boxes, so its log is `O(s1 log(s1+n))=N^(beta+o(1))=o(N)`. Any sound separator accepts only tables in `SIZE(s2)`, so its indicator rank under any flattening is at most `|SIZE(s2)|`, again with sublinear logarithm. Together with C-317's `Theta(s2 log s2)` safe-box dimension construction, these retire box-count/log-rank/free-coordinate entropy as standalone routes beyond q=N. They do not constrain state-sensitive invariants. C-257 and C-258 remain the parity/equality counterchecks. No q improvement follows. Full proof: `research/C319_NATIVE_CLOSURE_AS_ALTERNATING_COFACTOR_GAME_2026-09-28.md`.

## C-320 - Robust code-splice balls constrain compatible owner masks (28 September 2026)

For a low constant-distance code `C` of size K and distance d, a uniformly random coordinate split P makes every off-diagonal splice high with positive probability whenever `d>2 log K+log |SIZE(T)|`; union-bound failure is at most `K^2 |SIZE(T)|/2^d`. If patching r coordinates costs at most `c0*n*r`, the same conclusion holds for every owner mask within radius r of P or its complement whenever `T>s2+c0*n*r`. On the C-80 code at OPS parameters, for any fixed `beta<gamma<1` there is a common split and radius `r=Theta(N^gamma/n)` that forbid all off-diagonal low-code owner masks in those two balls. The radius exceeds `s1`, but the two balls occupy an exponentially tiny fraction of masks and the state graph is not forced to generate one. This strengthens C-112 without improving q. Full proof: `research/C320_ROBUST_CODE_SPLICE_BALLS_AND_STATE_LIMIT_2026-09-28.md`.

## C-321 - Seed-feature separation re-audit; feature-only ceiling is linear (28 September 2026)

For a fixed C-319 game Q, its acceptance function factors as `G_Q(phi_Q(w))`, where `phi_Q` is the vector of 2q seed-clause truth values and `G_Q` is the monotone least-fixed-point readout of the transition graph. Every low/high pair must have `phi_Q(low) not<=phi_Q(high)`, so some seed clause separates that pair. But the 2N unit signed-literal tests already separate every pair of distinct tables. Therefore any lower bound using only first-layer pair distinguishability, seed-profile count, or profile injectivity cannot force `q>N`; the missing charge must use the restricted transition readout and the endpoint-incidence constraints. The readout has positive seed-certificate width at most 2q and negative width at most q, which is structural description, not a q improvement. Full proof and scope: `research/C321_ACTIVATION_PROFILE_CEILING_AND_TRANSITION_READOUT_2026-09-28.md`.

**Novelty audit:** C-76 already has the seed-vector factorization and low-side CNF traps; C-221 proves the pair-separation condition and the `2N` signed-literal ceiling; C-260 gives the certificate/blocker duality. C-321 is an independent re-derivation, not a new claim. Q182 is closed as redundant.

## C-322 - Empty roots broadcast; exact pre-root closure (28 September 2026)

Let `T_i=E_i intersect H_i` and `R={r:T_r=empty}`. For every state i and every root r, `T_r` is contained in both `E_i` and `H_i`, so r belongs to both predecessor sets of i. Thus `x_r^t=1` forces `x_i^(t+1)=1` for every i. If any root activates, all states activate in one further round; all roots have the same final Boolean activation predicate, and every accepted table has the all-ones final activation profile. This rules out final accepted activation-profile VC/shattering as a synchronization measure.

There is also an exact temporal reduction. On the nonroot state set `V=[q]` with `R` removed, run the least-fixed-point recurrence after deleting all root predecessors. Before the first root activates, the full nonroot iteration agrees with this root-free system. For each root r, test its two seed-or-root-free-predecessor factors against the root-free closure. The original list accepts exactly when at least one such terminal test succeeds: a first activated root has no active root predecessor, and conversely any successful root-free terminal test is preserved by monotonicity in the full system. This is an exact output-root normalization only. It gives no q bound, does not shrink the nonroot graph, and does not control endpoint incidence or compatible context/proof reuse. Do not pursue further root-normalization variants; keep O-180 on a genuine state-sensitive synchronization theorem. Full proof: `research/C322_ROOT_BROADCAST_AND_PREROOT_NORMAL_FORM_2026-09-28.md`.

**Checkpoint after C-320â€“C-322:** actual Gap-MCSP lower bound beyond `N-o(N)`â€”**no**; valid near-linear full-promise coverâ€”**no**; new state-sensitive synchronization theoremâ€”**no**; positive CohEnc transferâ€”**no**; general reconstruction-to-decision compilerâ€”**no**. C-321 is a duplicate audit; C-322 is structural only. Continue O-180 on compatible context/proof products, not feature counts or final activation profiles. No P-vs-NP conclusion follows.

## C-323 - Root-free SCC profile refines the AND-count compiler (28 September 2026)

For a valid q-pair list with m empty-consequence roots, delete the roots using C-322 and let `r_1,...,r_c` be the SCC sizes of the remaining predecessor graph. The exact separator has a monotone circuit with arbitrary-fan-in OR gates and at most

```text
m + sum_a r_a^2
```

AND gates. Process root-free SCCs in condensation order; with external predecessors fixed, an SCC of r states stabilizes from zero after at most r strict rounds, using at most r AND gates per round. Each root's final two-factor test costs one additional AND. Thus if the maximum root-free SCC size is d, `A_cap(Q)<=m+d(q-m)<=d q` (and if there are no nonroots, `A_cap(Q)<=q`).

This improves the qÂ² compiler on covers with small root-free SCCs. It also explains why applying the older full-graph SCC compiler directly can miss this structure: each empty root is a predecessor of every state, so the post-acceptance broadcast merges every proof-relevant state into a root SCC. The C-322 deletion removes those irrelevant edges before SCC analysis. No bound on d is known for minimum OPS covers, and one large root-free SCC restores the quadratic loss. This is a parameterized compiler, not a q lower bound or a near-linear cover. Full proof and limitations: `research/C323_PREROOT_SCC_COMPILER_2026-09-28.md`.


## C-324 - Feedback-core compiler sharpens root-free SCC accounting (28 September 2026)

Delete root-free self-dependencies, which do not change the least fixed point. In each root-free SCC C of size r_C, choose a feedback vertex set F_C of size k_C. For fixed core values, the remaining r_C-k_C states are uniquely evaluated in topological order. The reduced k_C-dimensional core map is monotone and stabilizes from zero in at most k_C strict rounds. Evaluating one round costs r_C AND gates; one final acyclic pass costs r_C-k_C. Including m terminal roots gives

```text
A_cap(Q) <= m + sum_C [ r_C + k_C (r_C-1) ].
```

More sharply, for a chosen F_C let lambda_C be the maximum number of strict core iterations over seed-clause and incoming-boundary assignments. Then `A_cap(Q)<=m+sum_C[(r_C-k_C)+lambda_C*r_C]`, with lambda_C<=k_C. A directed-cycle SCC or a hub-dominated SCC has k_C=1 and compiles to at most `2r_C-1` AND gates; an acyclic root-free graph compiles with at most q gates. Dense feedback cores still incur quadratic cost. C-258 is a hostile countercheck: its nested prefix carriers create directed 2-cycles between adjacent states in each block/value branch, hence feedback vertex number at least `floor((r-1)/2)` for an r-state branch, while the repeated-block subpromise still has an O(N)-pair cover. Thus the feedback-set compiler is loose on this known easy subpromise and k_C alone is not a q-sensitive synchronization invariant. The C-257 prefix construction is acyclic; neither it nor C-307's acyclic separator compiler implies small feedback cores for arbitrary covers. This does not constrain C-281 compatible context/proof products or prove an OPS feedback-core bound. Pauly 2018 explicitly leaves general circuit-size extraction from reachability graph-game forms open (Open Question 11.2); the present theorem supplies a structural parameter, not a general resolution. Full proof and boundaries: `research/C324_FEEDBACK_CORE_COMPILER_2026-09-28.md`. The actual OPS native lower bound remains `N-o(N)`.


## C-325 - C-258 defeats raw feedback size; factor common predecessors (28 September 2026)

In C-258, for each block/value branch with nonempty nested carriers `P_t`, adjacent states have both directed edges: `P_t subseteq E_(t+1)=P_t`, and `P_(t+1) subseteq E_t=P_(t-1)` and `H_t`. In the repeated-block OPS regime `r=o(N)`, every such cylinder has more completions than `|SIZE(s2)|`, so all P_t are nonempty. Each branch therefore contains a bidirected path and requires at least `floor(r/2)` feedback vertices; across the disjoint value/block branches this is `Omega(N)`, even though the C-258 subpromise has an O(N)-pair cover. C-324 remains a correct compiler but is loose on this hostile example; low feedback vertex number is not a necessary property of a linear cover.

For any root-free recurrence, let `C_i=P_i^E intersect P_i^H` be common predecessors and remove them from both sides to define residual `G_i`. The Boolean identity `(c_i OR u_i) AND (c_i OR v_i)=c_i OR (u_i AND v_i)` gives `F_i(x)=c_i(x) OR G_i(x)`. Let `cl_C` be closure under common-predecessor implications. Then `mu F=mu(x -> cl_C(G(x)))`: every F-fixed point is a pre-fixed point of this map, and every fixed point of the map is F-fixed. This isolates free two-sided OR propagation from residual seed-labelled AND transitions, but does not bound the iteration depth after closure. Full proof and limits: `research/C325_COMMON_PREDECESSOR_CLOSURE_AND_C258_FEEDBACK_AUDIT_2026-09-28.md`. No q improvement or P-vs-NP result follows; the actual lower bound remains `N-o(N)`.

## C-326 - Exact nested-closure compiler for C-258 (28 September 2026)

Assume `N=dr`, `d>=2`, `r>=4`, `U` is the high set, `U intersect Rep_(d,r)=empty`, and `2^(r-3)>2^N-|U|`. The last condition implies every cylinder with at least `r-3` free coordinates meets U, supplying the witnesses for the endpoint-containment audit. For each fixed block/value prefix branch, common-predecessor closure yields

```text
G_1=b_1
G_2=(b_1 OR x_1) AND b_2
G_t=x_(t-1) AND b_t                       (t>=3)
x_t=OR_(s>=t) G_s.
```

Its least fixed point is `x_t=AND_(u<=t)b_u`: the candidate is fixed because these prefix products decrease with t, and every fixed point is forced to contain each prefix product by induction. Hence a terminal branch is active exactly when its block is constant in that value. The C-j/A-k merge equations have the same nested absorption and yield `c_j=B_j`, `a_k=AND_(j<=k)B_j`; the final root test is exactly the repeated-block predicate. Two prefix chains per block plus the final block conjunction use `2N-d-1` AND gates, despite `Omega(N)` raw feedback vertices in the pair list.

The derivation is exact for this subpromise under the richness condition, and a prior ephemeral exhaustive evaluator found no mismatch for six parameter pairs through N=9. It gives no general common-closure compiler, full-promise cover, or q improvement. This resolves C-258 as a required hostile calibration only. Full endpoint audit and proof: `research/C326_NESTED_COMMON_CLOSURE_COMPILER_FOR_C258_2026-09-28.md`.

## C-327 - Logarithmic-wise matching pseudorandomness misses the useful width (28 September 2026)

Kaplan-Naor-Reingold give `k`-wise almost independent permutations with description length `O(k log v + log(1/delta))`, so for `v=polylog(N)`, `k=O(log N)` is succinct. However C-310's matching-sunflower width is `w=Theta(v^(1/3)/(log v)^(2/3))`. The source lower bound can exceed `N^(1+epsilon)` only for `v=(log N)^K` with K>3; then `w=omega(log N)`. At K=3, `w=o(log N)` and `exp(Omega(w))=N^(o(1))`. Thus the prescribed O(log N)-wise experiment does not preserve the individual term-containment probabilities needed at a transfer-capable scale. Raising k to Theta(w) still gives a polylogarithmic seed, but controlling each term probability alone does not control a large DNF union, and there is still no C-125 encoder with positive margin. The requested secondary route is closed without affecting the primary target. Sources and parameter audit: `research/C327_SUCCINCT_MATCHING_AUDIT_AND_WIDTH_BARRIER_2026-09-28.md`.

**Checkpoint after C-324-C-327:** actual Gap-MCSP lower bound beyond `N-o(N)`â€”**no**; full-promise `N^(1+o(1))` coverâ€”**no**; q-sensitive synchronization theoremâ€”**no**; positive CohEnc transferâ€”**no**; general reconstruction-to-decision compilerâ€”**no**. Do not relabel either calibration as a breakthrough.

## C-328 - Secret-sharing lower bounds do not reach the native q scale directly (28 September 2026)

Applebaum-Nir give a uniform family of monotone circuits of size `Theta(t)` over `Theta(t)` variables with total secret-share size `Omega(t^2/log t)`. In a direct truth-table embedding, `N=2^(Theta(t))`, so this becomes only `Omega(log^2 N/loglog N)`, below `q>=N-o(N)`. Their coNP-hardness of recognizing cheap versus expensive sharing is a meta-complexity theorem and does not lower-bound the fixed Gap-MCSP fusion parameter. C-304's exact native algebra is ideal-valued in dimension `3^N`, and no q-to-share translation is established. Close only the direct parameter substitution; leave the broader access-structure bridge open pending a semantics-preserving, parameter-explicit conversion. Full note: `research/C328_SECRET_SHARING_LOWER_BOUNDS_DO_NOT_SCALE_TO_NATIVE_Q_2026-09-28.md`.

## C-329 - Positional policies and lane-selector obstruction (28 September 2026)

The exact C-319 game is a finite reachability game. For every accepted table, a rank-decreasing positional strategy from an empty root selects one predecessor or one true seed literal for each state-side obligation. Fixing the strategy yields a coordinate subcube contained in `SIZE(s2)`, and acceptance is the union of these policy cubes. The crude policy count is at most `q(q+2N+1)^(2q)` and gives only `q=Omega(s1/log N)` on a distance-`Omega(N)` low code, weaker than `N-o(N)`. A direct near-linear universal-circuit construction with one shared state per gate also fails: at a two-lane OR gate with child values (1,0) and (0,1), one positional choice cannot witness both lanes. This closes that specific construction and count method, not arbitrary q-state covers. Full derivation: `research/C329_POSITIONAL_POLICIES_AND_LANE_SELECTOR_OBSTRUCTION_2026-09-28.md`.


## C-330/C-331 â€” Local research results only

C-330: TR26-220 does not directly apply to D0/D1 over edges; the vertex-color lift is parameter-weaker than the matching-specific C-310 sunflower argument and leaves the encoder gap untouched.

C-331: adversarial universalization of PCP randomness yields an exact exists-proof/for-all-challenge relation, but no transfer into C-319's activation equations because proof commitments are not observable after state merging. This closes only the direct PCP compilation attempt.

Neither claim changes rho_GapMCSP=N-o(N), yields a near-linear cover, proves a state-sensitive theorem, constructs a positive CohEnc margin, or proves P != NP.


## C-332 â€” Ordinary BP lower bounds do not yet transfer to q

Known local-PRG lower bounds for exact MCSP give an almost-quadratic branching-program lower bound. Their proof's yes/no distribution argument is compatible with low/high promises, but the known generator's local output complexity is S^(1/2+o(1)); at small beta this is above s1 for all S in the theorem's range S>=N. Separately, C-319 is an alternating least-fixed-point system, not a standard BP, and q^2 unrolling is not a near-linear BP simulation. No native lower bound follows.


## C-333 â€” Polynomial-source PRG parity obstruction

Let K<N and choose a random degree-<K polynomial over GF(2^n), outputting its trace at all N=2^n addresses. The table distribution is K-wise independent, is supported on a binary linear code of dimension at most Kn, and every output has circuit size O(Kn^2). Since Kn<N in the small-beta parameter choice, a nonzero dual codeword defines a parity test with source acceptance 1 and uniform acceptance 1/2. The abstract C-319 equation syntax computes this parity with O(N) states. C-257 separately realizes parity on r>=2 selected coordinates with 4r-4 actual pairs for an artificial parity promise; it does not establish those endpoints over the actual high-table universe. Hence this source fails as a PRG for generic abstract readouts, but no no-go for actual sound Gap-MCSP pair systems follows.

For a generic abstract C-319 readout, after discarding clauses wider than R=Theta(log(q/epsilon)), the 2q remaining clauses can jointly inspect at most min(N,2qR) coordinates. Exact independence sufficient for their joint vector by the generic k-wise argument therefore has order min(N,O(q log(q/epsilon))); the polynomial construction then costs O(min(N,q log(q/epsilon))n^2)=O(Nn^2) at qâ‰ˆN, too large for s1. An acyclic abstract chain can read the conjunction of q seed features, confirming that marginal clause statistics alone do not fool arbitrary readouts. C-257's pair realization is for an artificial parity universe, so this is not a restriction on legal endpoints over the actual high-table universe. Full scope: `research/C333_LOW_DEGREE_POLYNOMIAL_PRG_PARITY_OBSTRUCTION_2026-09-29.md`.


## C-334 â€” Positional policies form a union of sound CNF regions

For every accepted table of a C-319 game, choose a rank-decreasing positional strategy. At each state-side where it stops, retain the full seed clause rather than a particular true literal. The resulting region R_sigma is the conjunction of at most 2q seed clauses. Fixed predecessor edges are unchanged and well-founded, so the same strategy wins on every table in R_sigma. There are at most q(q+2)^(2q) raw strategies, but at most 2^(2q) distinct regions because the CNF depends only on the subset of the fixed 2q seed clauses used at stops. Conversely every accepted input has a policy; therefore Accept_Q is a union of at most 2^(2q) distinct CNF regions. For a sound cover each nonempty region is contained in SIZE(s2). A satisfying anchor for an m-clause CNF yields at least 2^(N-m) satisfying assignments, so m>=N-log2|SIZE(s2)|=N-o(N), giving only q>=(N-o(N))/2. This exact normal form does not beat the existing q>=N-o(N) bound.

Naor-Naor small-bias spaces provide low-circuit truth tables with inverse-polynomial bias, removing C-333's source-specific parity distinguisher. Bazzi's k-wise-independence bound applied separately to each distinct policy CNF and union-bounded over M<=2^(2q) regions requires k=O(q^2), useless at qâ‰ˆN. This closes only the generic small-bias-plus-policy-union estimate. Sources and derivation: C-334.

## C-335 â€” GEN refutes a generic abstract recurrence-to-MSP compiler

The abstract q-state least-fixed-point equations can compute GEN_n with O(n^3) states: each potential triple gets two states computing its input bit AND the two antecedent point states; each point state ORs the incoming triple witnesses, and point 1 is seeded true. The designated output is the state for point n. Robereâ€“Pitassiâ€“Rossmanâ€“Cook's GEN lower bound, restated in ECCC TR26-070 Theorem 12, requires monotone span-program size 2^{n^{Omega(1)}} over every field. Hence no polynomial-size MSP compiler applies to arbitrary abstract recurrences with a designated output, even nonuniformly. The generic q-round formula expansion gives only 2^{O(q log q)} MSP size and at best q=Omega(N/log N) from maximal N-variable MSP lower bounds. This is not a result for the actual C-319 separator output: although endpoint-incidence pairs can realize GEN internally, every constructed consequence is nonempty, so the output is false. No native q change follows. See C-335.

## C-336 â€” Multiple-hole substitution forbids independent block menus in one context

The C-281 substitution law extends to a context with labeled holes at any states: plugging a finite proof into each hole preserves acceptance whenever the union of all signed supports is consistent. Thus the whole completion cylinder of the union lies in `SIZE(s2)` for a sound separator. At OPS scale, let `k=K log N` address blocks and choose in each block a truth table supported on a fixed subcube of size `2^u=Theta(s1 log s1)` with local circuit size at most `alpha s1`. A table supported on just one block has global size `<=s1`, but the independent product across k blocks has `2^(Theta(K*s2 log N))` members. For K large, this exceeds `|SIZE(s2)|`, so at least one tuple is high. Therefore no one accepting context can have k mutually compatible, block-local replacement menus whose independent products realize all these tuples. This is an exact primary-route product constraint, but no q-dependent argument forces such a context or charges its avoidance. C-257 parity and C-258 equality evade the independent-menu hypothesis. No q improvement follows. Full derivation: C-336.


## C-337 â€” A near-linear activity selector avoids the C-336 product (29 September 2026)

Let `k=K log N` disjoint address subcubes each have `M=lambda*s1*log(s1)` coordinates. Although the independent product over all k blocks contains high tables by counting, a signed-literal monotone circuit can recognize the restricted family that is zero outside these coordinates and nonzero on at most `r=R log N` blocks. Every such table is in `SIZE(s2)`: each active block has arbitrary local pattern circuit cost `O(lambda*s1)`, with an `O(n)` fixed-subcube equality cost, so at most r active blocks cost `O((R*lambda/c0)*s2)+O(n^2)<=s2` for suitable constants. Use one AND per coordinate to check zeros, then a sorting network on the k block-zero flags to test the activity threshold using `O(k*log^2 k)` additional AND gates. C-307 converts this separator into a native cover with `q<=N+O(log N*log^2 log N)` for this restricted anchor family versus the actual high set.

This does not accept all of `SIZE(s1)` and rejects parity/repeated-block low tables, so it is not an O-168 construction and does not pass the full hostile calibrations. It does show that C-336''s forbidden product alone cannot force superlinear q: a global activity selector rejects the independent high product while accepting all individual block menus at linear cost. The full-promise q-charge must use the obligation to cover every low circuit, beyond product entropy or menu availability. See `research/C337_NEAR_LINEAR_BLOCK_SELECTOR_ESCAPE_2026-09-29.md`.



**C-337 extension audit:** Allowing at most d=R log N distinct block rows remains near-linear: shared pairwise equality tests cost O(k^2*M), and enumerating representative sets costs O(k*binom(k,d))=o(N) when K*H_2(R/K)<1. Every accepted table is in SIZE(s2), so C-307 again gives a restricted cover. This includes repeated rows, but rejects the low O(n)-size relation table whose row b is the minterm [suffix-prefix=b]. Thus even a distinct-cofactor count does not measure coherence; a small circuit can generate many different rows by a shared relation. It still does not cover all SIZE(s1) or change q. Details in C-337.


## C-338 - 2026 monotone example hardness does not give an asymmetric full-table map (29 September 2026)

Cavalar, de Rezende, Gray, and Santhanam prove under randomized ETH that partial monotone circuit size from labelled examples is strongly hard to approximate; Theorem 1.2 contrasts sample sets consistent with a small monotone formula against sets with no nontrivial correlation with larger monotone circuits. This is a sample-agreement theorem, not a C-125 map into full truth-table rails. The natural example rails P satisfy P<=e(w) for every fitting low table, whereas C-125 requires e(w)<=Phi(YES). Filling every unobserved coordinate with both rails reverses the order but makes the YES vector inconsistent, so no one-hot high code can dominate it on NO. Marking omitted examples instead can make consistency monotone, but reconstructing the retained sample list then uses negation. The result gives no monotone rail map, no map AND-cost upper bound, and no positive CycAnd-CohEnc margin. It does not change the unconditional native lower bound N-o(N). This closes only the direct example-list adaptation; a witness-dependent C-125 map remains open. Primary source: https://arxiv.org/abs/2607.12331. Full order audit: research/C338_2026_MONOTONE_LEARNING_COHENC_ORDER_AUDIT_2026-09-29.md.


## C-339 - Known MCSP lower bounds do not reach the C-307 separator measure

The q-state cover unrolls to a signed monotone acyclic separator with at most q^2 binary AND gates. Therefore an A_cap lower bound L yields only q >= sqrt(L); the requested q >= N^(1+epsilon) needs A_cap >= N^(2+2epsilon). CKLM's N^(3-o(1)) De Morgan formula lower bound would clear this threshold only if the separator had a comparable formula-size simulation. Sharing can make formula expansion exponential, and no near-linear compiler for the exact separator is known. Their N^(2-o(1)) arbitrary-basis formula and general branching-program bounds are model-mismatched: C-319 is a cyclic universally alternating least-fixed-point system, with no q-preserving BP compilation.

The Austrin-Risse SoS bounds concern proof degree for MCSP and minimum monotone-circuit size of slice functions, not circuit size of the full-promise separator. C-307's exponential CNF lower bound applies only when the separator is a CNF; it does not lower-bound shared AND-DAGs. No located theorem proves A_cap > N^2 on the OPS promise, and no cited result yields a superlinear q bound or a near-linear full-promise cover. Continue O-167/O-168 directly; do not spend further effort transferring formula/BP/SoS bounds without a lower-bound-preserving compiler. Full model audit: research/C339_MCSP_LOWER_BOUND_MODEL_TRANSFER_AUDIT_2026-09-29.md.

## C-340 - The gate-address evaluator is not a full-promise cover

The OPS theorem requires one fixed epsilon>0 and every sufficiently small fixed beta>0. The C-305 cost N*s1=N^(1+beta-o(1)) would sit below N^(1+epsilon) when beta<epsilon if it were a full-promise cover. It is not: C-305 evaluates a supplied circuit description, while a valid cover needs one fixed state graph whose winning strategies may encode different low circuits and whose losing behavior excludes every high table. Duplicating (gate,address) states permits address-dependent wiring; sharing gate states loses the challenged address. C-306 rules out recovering that address from support annotations. Thus no parameter contradiction and no q upper bound follows. A valid O(N*s1) cover would refute the desired rho-route, though its q^2 circuit simulation would not itself contradict OPS Theorem 1.4. Source: [OPS Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf). Full audit: research/C340_NS1_EVALUATOR_IS_NOT_FULL_COVER_2026-09-29.md.

## C-341 - A shared positional selector loses its address context

In the C-319 game, histories that reach the same state on the same table have identical continuation games; the least-fixed-point value has no caller/address argument. Therefore address-specific verifier states that merge into one shared configuration selector cannot recover their address after the selector acts. Even if a successor retains the selected gate configuration, two lanes reaching the same OR-state side-obligation still cannot choose different true children (for example `x_1 OR not x_1`). This refutes the proposed shared-selector sketch and its unsupported `O(N+s^3)` count, not arbitrary endpoint-induced encodings or any general q bound. A valid repair needs an explicit address-and-description readout and a complete C-281 soundness proof. The actual bound remains `rho_GapMCSP >= N-o(N)`; see `research/C341_SHARED_CONFIGURATION_SELECTOR_LOSES_ADDRESS_CONTEXT_2026-09-29.md`.

## C-342 - Observable selector channels and same-anchor rectangles

For any fixed q-pair list Q, all input dependence factors through its 2q seed-clause truth values `sigma_Q(w)`: the fixed least-fixed-point recurrence is a deterministic map of that signature. Thus any circuit-description selector that the graph can actually read must be encoded in the seed signature/activation profile; a positional policy choice is proof data, not a message. Each accepted signature fiber is contained in `SIZE(s2)`, but this partition alone gives no useful q bound because rejected fibers may contain high tables and `|SIZE(s1)|/|SIZE(s2)|<1`. Separately, at a fixed accepted table w, every matching context support and replacement support at one reused state is a subset of `ell(w)`, so every pair is compatible; C-281 substitution forces their full Cartesian product of completion cylinders to lie in `SIZE(s2)`. Residual-function counting proves an architecture-specific lower bound: an exact path-only circuit selector needs at least `2^(Omega(s1))` post-selection states, using `2^(Omega(s1))` distinct low indicator functions; the multiplexer is the one-bit version. This does not cover activation-profile selectors or arbitrary covers. The remaining full-promise object is a readable activation-code construction or a reduction from arbitrary covers to safe rectangles/residuals. Actual `q>=N-o(N)` is unchanged. Full derivation: `research/C342_OBSERVABLE_SELECTOR_CHANNELS_AND_SAME_ANCHOR_RECTANGLES_2026-09-29.md`.

## C-343 - Universal-selector quantifiers and the OPS-to-native checkpoint

For every table `w`, the condition `forall address a exists size-s circuit C_a: C_a(a)=w_a` is vacuous: choose the constant circuit with value `w_a`. A valid witness verifier needs `exists one C forall a: C(a)=w_a`. This formally rejects per-address independent circuit guesses; C-341/C-342 separately reject address-erasing shared selectors and path-only description registers, without covering arbitrary native grammars. The C-319 unrolling maps q states to a monotone circuit with at most `q^2` paid AND gates when unbounded OR fan-in/semantic seed clauses are free; do not equate this with standard fan-in-two circuit size without charging those operations. Separately, the repository already proves the circuit-to-fusion direction in C-109 / Idea 109: any size-S De Morgan circuit separating disjoint Y,Z compiles into a valid fusion list with at most `3S+1` rules. Hence a lower bound `rho>N^(1+epsilon)` itself gives a general circuit lower bound `C=Omega(N^(1+epsilon))` for this promise. OPS Theorem 1.4 then supplies the magnification implication; its contrapositive guarantees circuit upper bounds at arbitrarily small beta choices under `NP subseteq Circuit[poly]`, which C-109 converts to same-exponent native covers. This is conditional, not an unconditional near-linear cover. All five attached breakthrough outcomes remain unachieved and the actual bound stays `N-o(N)`. C-343 corrects its initial mistaken claim that the reverse compiler was unknown; its quantifier-collapse lemma is an architecture filter, while the compiler is prior C-109 work. Full audit: `research/C343_QUANTIFIER_COHERENCE_AND_MAGNIFICATION_BRIDGE_CHECKPOINT_2026-09-29.md`.

## C-344 - Uniform full-support learning does not capture all high Gap-MCSP tables

Fix a low table g and let `r=K s2` for a sufficiently large constant K. Circuit counting gives `|SIZE(s2)|<=2^(C s2 log(s2+n))`, while the radius-r Hamming sphere around g has `binom(N,r)>2^(C s2 log(s2+n))` for fixed `0<beta<1`, since `log binom(N,r)>=K s2((1-beta)logN-logK)`. Therefore that sphere contains a table f with `CC(f)>s2`. But f differs from g in only r addresses, so a circuit obtained by patching those addresses has size `O(r n)=O(N^beta logN)=poly(s1)` and agrees with f on `1-r/N=1-o(1)` of uniform addresses. Hence the direct map from explicit Gap-MCSP to the 2026 full-support learning problem using uniform addresses fails: some promised high tables have subexponential-size predictors with near-perfect accuracy, violating that problem's NO condition. This does not rule out f-dependent anti-checker samplers; constructing one is the outstanding transfer, and no Gap-MCSP or rho lower bound follows. Primary source and derivation: `research/C344_FULL_SUPPORT_LEARNING_ROUTE_HAS_NEARBY_HIGH_APPROXIMABLE_TABLES_2026-09-29.md`.
## C-345 â€” Total-Learn parameter correction and pointwise hard-core lists (29 September 2026)

The formal Total-Learn promise has NO threshold g(s), and ECCC TR26-091 Theorem 33 allows all subexponential g, including polynomial choices such as g(s)=2s. C-344's uniform-address counterexample remains correct, but its â€œsubexp(s1)â€ wording was too broad: the nearby high table with CC(f)=O(s2*n) defeats any distribution only when the chosen g(s1) exceeds that patch-circuit size. For a small constant-factor predictor enlargement T=lambda*s1, minimax and majority sampling show that CC(f)>T*(ln N+1)/(2 epsilon^2)+O(T) implies a distribution on addresses with error at least 1/2-epsilon against every size-T circuit. An empirical sample of O(T log(T+n)/epsilon^2) points preserves a 2epsilon margin simultaneously for all such circuits. At OPS parameters this is O(N^beta) points, subject to the fixed constant c leaving the displayed slack. Mixing with a small uniform component gives full support, and domain padding makes the sampler circuit polynomial in its domain dimension. The construction is table-dependent and no efficient selector is known; it yields no Gap-MCSP or P-vs-NP lower bound. See research/C345_TOTAL_LEARN_GAP_PARAMETER_AND_POINTWISE_HARDCORE_MAP_2026-09-29.md.
## C-346 â€” Exact small-gap hard-core encoding at OPS c=10 (29 September 2026)

At the concrete OPS thresholds s1=N^beta/(10n), s2=N^beta, let T=ceil(3s1/2), a=6/25, k=ceil((lnN+1)/(2a^2)). If no input distribution forces size-T circuits to err at least 1/2-a, minimax gives a distribution over such circuits with pointwise expected error below 1/2-a. A majority of k draws computes any fixed high f exactly with positive probability; a direct threshold-counting circuit costs O(k^2), while kT/s2=125 ln(2)/96+o(1)<0.903. Since k=O(n), the overhead is o(s2). This contradicts CC(f)>s2, so a hard-core distribution exists. Sampling q=O(T log(T+n)/eta^2) points with eta=0.001 gives a list with empirical error at least 0.259 against every size-T circuit. Mix this with uniform addresses at weight 1/1024: the resulting full-support accuracy is below 0.742, hence below the Total-Learn cutoff 3/4, with predictor gap g(S)=ceil(3S/2). Domain padding makes the sampler size polynomial in its domain dimension while preserving the low predictor. The pointwise list Q is not efficiently selectable from f. This is not a reduction or an unconditional complexity result. See research/C346_EXPLICIT_SMALL_GAP_FULL_SUPPORT_ENCODING_AT_OPS_CONSTANTS_2026-09-29.md.

## C-347 - Algebraic fingerprints do not remove challenge state from C-319

The direct arithmetic extension of a size-s circuit may have individual degree `2^s`, making a Schwartz-Zippel fingerprint require a huge field. Evaluating the multilinear extension of the circuit's truth table avoids that degree but is not known to be cheaply evaluable from the succinct circuit. Sum-check compresses communication but still needs the accumulated challenge at its final oracle query. The exact native game has no caller-history register: merging gate states drops the challenge/address, while duplicating gate-by-address states returns the product construction. This closes the standard fingerprint/sum-check compilation only; no all-Q lower bound follows. The missing construction primitive is a cheaply evaluable extension with coherent activation-code readout and C-281 soundness. The actual native lower bound remains `N-o(N)`. See `research/C347_ALGEBRAIC_FINGERPRINTS_AND_TRANSCRIPT_STATE_2026-09-29.md`.
## C-348 - Common-closure feedback is an exact compiler, not a q invariant

For q0 root-free states and m empty roots, factor common-predecessor propagation into a static closure and residual maps G_i. If the closure-expanded residual dependency graph has feedback vertex number k, evaluate the noncore acyclic portion once per core iteration; the exact separator uses at most m+(k+1)q0 paid AND gates. The scheduling is valid because every input to a residual term precedes all noncore outputs reached from that term in the acyclic graph. C-258 still has k=Omega(N) despite its O(N)-pair subcover, while C-326 exploits a special prefix-absorption law to obtain an O(N) ordinary circuit. This compiler does not give a full-promise q bound.

## C-349 - Circuit-local selector hardness does not transfer to arbitrary covers

The OR-witness matrix M_C(x,g) depends on the chosen description C. For any f, padding its output as f OR 0 makes the output witness constant; the same function 1 also has the representation x_1 OR not x_1 with address-varying witness. A size-s circuit can make each OR disjoint as u OR (v AND not u) with at most 2s extra gates, and De Morgan conversion removes positive OR gates at constant-factor size. Thus one chosen circuit's local selector pattern is not a property of the low table. The unique gate-value matrix survives as an evaluation object, but no reduction from arbitrary sound C-319 covers to its address/gate readout is known. A viable selector lower bound must be representation-invariant and prove that transfer, or work directly with the native state/support algebra. Actual q remains N-o(N); no superlinear cover result follows.
## C-349 checkpoint - change mechanism

The required A-E audit is all negative: no improvement beyond N-o(N), no general state-capacity theorem, no C-320-forcing selector-hard family, no full-promise near-linear cover, and no lower-bound-preserving communication/rectangle/residual-state formulation. The next mechanism is direct support-grammar capacity. C-281 assigns each reused state a context family and replacement-proof family; every compatible pair yields a sound owner-mask splice. A support-only argument cannot bound one state's anchor capacity, since full supports K=P=ell(w) make every distinct-anchor cross-pair incompatible. The missing ingredient is a lower bound on the native rule grammar needed to generate those supports selectively. No q improvement follows yet.
## C-350 - Balanced cuts extract loaded states, but not dangerous products

Let an accepting proof support S have m variables. Soundness gives m>=N-kappa_square(s2). In the proof tree, repeatedly follow the larger of the two side subproofs until its variable count first falls to at most m/2. The selected state occurrence then has replacement support width in (m/4,m/2] and context width at least m/2, with their union equal to S. Thus one state is a balanced-cut occurrence for at least |F|/q anchors in any finite low family F after choosing one proof per anchor. This is a proof-tree extraction theorem, not a state-capacity result: the context/proof supports may overlap heavily, their owner mask may be empty, and distinct-anchor crosses may be incompatible. C-257 parity and C-258 equality remain safe linear calibrations. The next missing theorem must turn balanced-cut load into a compatible forbidden-mask splice by using how the rule grammar generates supports.


## C-351/C-352 - Conditional support projection; no menu capacity

For a fixed output context K, write R=[N] minus Var(K). Every replacement support P matched by a low anchor and compatible with K leaves at most kappa_square(s2) coordinates of R unmentioned. If two such replacement supports P_a,P_b are also mutually consistent, their anchors differ on at most 2*kappa_square(s2) coordinates of R. C-352 audits the quantifiers: a multi-hole Cartesian product supplies cross-hole consistency, not same-hole pairwise consistency. Complete supports ell(w) for distinct low anchors yield individually sound singleton cylinders and are mutually inconsistent, so support geometry alone allows arbitrarily large replacement menus. The arbitrary-family argument is not itself a full-promise grammar, but C-258/C-326 realize complete supports for the repeated-block subpromise with q=O(N). No bound on q for the full promise follows; the remaining target is a rule-sensitive extension to all of SIZE(s1). See C-351 and C-352 reports.


## C-353 - Exact overlap fingerprint, but no grammar charge

For repeated-block anchors w_g(p,u)=g(u), let Omega(K,C) contain suffixes u for which context K and replacement C both mention at least one repeated coordinate (p,u). If K is matched by w_g and C by w_h, then K union C is consistent exactly when g and h agree on Omega. For suffixes outside Omega, a canonical splice that chooses ownership independently of p at each u remains a k-variable table, hence has size at most s1/4 under C-234's parameter choice. Thus a high canonical splice requires sufficiently complex prefix-varying ownership; variation alone does not suffice. This is a precise integration of C-234/C-245, not a new q lower bound. C-245/C-260 already formalize the support and blocker grammars, while C-251 rules out raw signature counting. The missing theorem is a q-sensitive composition potential including overlap, ownership, and high blockers. Actual bound remains N-o(N).

## C-354 - One-suffix owner-mask reduction

Fix the C-234 address split `(p,u)` and one suffix `u0`. The anchors `w0=0` and `w1(p,u)=1[u=u0]` are low. Their splice `z_mu(p,u)=1[u=u0]mu(p)` obeys `CC(mu)-O(1)<=CC(z_mu)<=CC(mu)+O(n)`. For fixed `beta<1/2`, the mask domain size is `r=Theta(N/s2)` and `r/(s2*n)->infinity`; circuit counting shows all but a `2^{-Omega(r)}` fraction of masks yield high hybrids. If K is a context for w0 and C a replacement proof for w1 at the same state, consistency gives a splice z_mu, so every such compatible owner mask must have `CC(mu)<=s2+O(1)`. Therefore that compatible join relation has at most `2^(O(s2*n))` distinct masks and VC dimension O(s2*n); a full owner cube on more prefix positions contradicts soundness. Restricting any full q-state game to the slice also gives the same-q abstract signed-clause least-fixed-point separator at truth-table length `r=Theta(N^(1-beta))`, exponent `beta'=beta/(1-beta)`, and adjusted OPS constants. The seed clauses simplify under fixed outside coordinates; endpoint realizability over the reduced universe is not claimed. This is a lower-bound transfer only, not a q bound: the grammar need not generate a large compatible cube, and complete supports may keep the cross-anchor pair incompatible. Actual q remains N-o(N). Proof and parameter transform: `research/C354_ONE_SUFFIX_OWNER_MASK_REDUCTION_2026-09-29.md`.

## C-355 - Column-duplication or exclusive-owner proof-tree dichotomy

For a canonical finite accepting proof tree with one selected signed literal per seed leaf, let M be the number of supported coordinates in the varying column and assign each coordinate to the LCA of its leaf occurrences. Either some internal rule occurrence has at least M/4 coordinates whose LCA is there (so each is repeated across its two child proofs), or a heavy-child descent gives a state occurrence with exclusive owner size in `(M/8,M/2]` and outside-context column width at least M/2. This repairs the empty-owner issue for a single proof-tree cut. It does not control compatibility across different anchors or charge the graph that selects their supports. C-356 gives a linear equality-code calibration at matching family-size and distance scales, so the dichotomy is classified LOCAL/STRUCTURAL and is not the next q-bound route. Full statement: `research/C355_COLUMN_DUPLICATION_OR_EXCLUSIVE_OWNERSHIP_2026-09-29.md`.

## C-356 - Equality-code family matches the C-355 coarse parameters

On the C-354 one-suffix column, choose d=Theta(s1) prefix blocks and let each arbitrary bit determine one constant block. This gives `2^d=2^(Theta(s1))` low anchors with distance `r/d=Theta(N^(1-2 beta))`, larger than `kappa_square(s2)` for beta<1/3. Add singleton zero blocks outside the column. By C-258's product-code construction this subfamily has a sound native cover against the actual high set with q=O(N). Hence family size, code distance, large proof supports, and repeated state-label buckets do not alone force incompatible supports to mix into a high table. The cover is only for this subfamily, not all of `SIZE(s1)`; no full-promise q bound changes. See `research/C356_EQUALITY_CODE_MATCHES_C355_BUCKET_2026-09-29.md`.

## C-357 - Generic reachability readouts can need near-quadratic fan-in-two size

For h inputs, the family of monotone CNFs with exactly h distinct clauses of width floor(h/2) has `binomial(binomial(h,floor(h/2)),h)=2^(Omega(h^2))` distinct functions; the zero-set assignment indexed by a width-h/2 set recovers whether that exact clause is present. Each function is the readout of a recurrence with h input states, h clause-OR states, and h-1 AND-tree states, hence q=3h-1. Since size-S fan-in-two Boolean circuits number at most `2^(O(S log(S+h)))`, some readout requires `Omega(q^2/log q)` ordinary gates. Thus no generic `O(q^(2-epsilon))` bounded-fan-in total-size compiler works for all abstract readouts. Scope is limited: this does not lower-bound the project `A_cap` paid-AND count (wide OR is free there), nor does it use actual endpoint-realizable seed clauses or Gap-MCSP. Pauly 2018 already asks the generic least-fixed-point graph-game/circuit size question. Full proof and scope: `research/C357_GENERIC_GAME_TO_BOUNDED_FANIN_CIRCUIT_BARRIER_2026-09-29.md`.

## C-358 - Fast ANF transform gives a linear native cover of the C-355 RM subfamily

For an `r=2^m`-bit truth table, the Boolean ANF transform computes all algebraic-normal-form coefficients in O(rm) XOR gates. A table is in `RM(d,m)` iff every coefficient of degree greater than d vanishes. On the C-354 one-suffix embedding, add O(N) gates to require all bits outside the column to be zero. The resulting O(N+rm)=O(N) De Morgan circuit accepts exactly the C-355 RM anchors, all of which are in SIZE(s1) after choosing d with an s1/2 circuit budget. It rejects every table in the actual high set; C-109 compiles it to an O(N)-rule native cover of this subpromise. This explicitly retires RM codeword count/distance as a q-charge mechanism. It is not a full-SIZE(s1) cover and gives no full-promise q improvement. Proof: `research/C358_REED_MULLER_BUCKET_HAS_LINEAR_NATIVE_SUBPROMISE_COVER_2026-09-29.md`.

## C-359 - Fixed-circuit selector rectangles cannot exceed linear

For any matrix `M:X x G -> Sigma` with `|X|=N` and `|Sigma|=k`, the row slices `{x} x {g:M(x,g)=a}` give a monochromatic rectangle partition with at most kN parts. Hence the forced binary OR-witness matrix of any fixed circuit has rectangle-partition number at most 2N, standard single-color fooling sets at most N, and deterministic communication complexity at most `log N+1`. These measures cannot prove a superlinear q bound from that matrix, even if its entries are a hard selector function. This does not cover anchor-lifted relations or arbitrary C-319 covers. The next valid route needs a proved all-anchor embedding or a direct full-promise support-grammar charge. Full note: `research/C359_FIXED_CIRCUIT_SELECTOR_RECTANGLES_HAVE_A_LINEAR_CEILING_2026-09-29.md`.

## C-360 - Leaf weighting counts formula occurrences, not shared states

The formula search-to-decision technique that replaces a variable by a weighted OR charges each occurrence because a formula is a tree. In a circuit, compute the weighted OR once and fan its output to r consumers; cost stays O(s), independent of r. C-319 likewise has one state activation shared across all incoming derivations, so ordinary leaf weighting cannot charge address-context reuse. Any transfer needs state-incidence tags plus a proof that incompatible reuse forces a forbidden C-281/C-320 splice. Ren-Santhanam's relativized decision/search separation further warns that extracting a circuit witness from a decision procedure is not automatic. No q change; full report: `research/C360_LEAF_WEIGHTING_BREAKS_UNDER_STATE_REUSE_2026-09-29.md`.


## C-361 - Output-index serialization does not transfer the Multi-MCSP gap

For a b-output truth table F, the scalar function h(x,i)=F_i(x) has table length within factor two of the concatenated vector table, but circuit sizes satisfy only CC(h)<=CC(F)+O(b) and CC(F)<=b*CC(h)+O(b log b). Thus the index encoding alone does not preserve a multiplicative complexity gap. Ilango-Loff-Oliveira control Delta=CC(T â€¢ g)-k, not total circuit size: k is a shared large baseline and Delta is at most the set-cover number. For their fixed m0=Theta(nu^3) construction, the random table T appears as one scalar slice, forcing CC(h)=Omega(m0/log m0) whp; the target table length is at most nu^(r+6)polylog(nu) for fixed set-size r. Hence for beta below 3/(r+6), even YES source instances serialize above the target high threshold. This refutes the direct wrapper at the small-beta scale for the published parameterization only. No arbitrary multi-output-to-single-output impossibility, native q bound, or P-vs-NP result is claimed. Proof and cited primary source: research/C361_OUTPUT_INDEX_SERIALIZATION_DOES_NOT_TRANSFER_MULTIMCSP_GAP_2026-09-29.md.
## C-362 - Graph-game size does not charge native q

An exact q-pair C-319 list embeds into an explicit reachability game with q universal states and 2q existential side nodes. Every side node has at most q predecessor exits and at most N signed-literal exits (or a constant winning exit), so the explicit graph size obeys L=O(q(N+q)+N). This is exact for the native interface, where the seed clauses are ORs of endpoint-selected signed literals and cycles lose. Pauly's graph-game Proposition 9 bounds extracted monotone-circuit depth by graph-game size but not total circuit size; Open Question 11 asks the corresponding circuit-size question for least fixed points. Consequently, generic graph-game compactness or ordinary circuit lower bounds do not presently yield q>N: the explicit graph parameter can already be quadratic at q=Theta(N), and independent seed-leaf lower bounds do not transfer through the endpoint-selected OR map. No q improvement, full-promise cover, or P-vs-NP proof follows. Full proof and source: research/C362_GRAPH_GAME_SIZE_DOES_NOT_CHARGE_NATIVE_STATE_COUNT_2026-09-29.md and https://arxiv.org/abs/1809.03093.

## C-363 - Seed-signature information saturates at linear size

The N positive singleton seed predicates `w -> w_a` form an injective conceptual signature on all N-bit tables; the full 2N signed singleton family also separates every ordered pair. Thus an O(N)-state signature can encode the complete table, and signature entropy/fiber separation alone cannot yield q=omega(N). These seed values are not free wires: each pair enters one coupled recurrence. Singleton exposure is not a separator. The q-sensitive target is readout cost under the fixed C-319 recurrence, or a valid N^(1+o(1)) full-promise readout construction. No change to q. Full proof: `research/C363_SEED_SIGNATURE_HAS_A_LINEAR_INFORMATION_CEILING_2026-09-29.md`.

## C-364 - Distance-to-low does not transfer approximate-MCSP hardness

A patch of t truth-table entries costs O(t n), so `CC(z)>s2` implies distance `Omega((s2-s1)/n)` from every size-s1 table. Hence the Gap-MCSP NO set is contained in the approximate-MCSP NO set. The approximate promise is at least as restrictive and may additionally reject medium tables; a lower bound for its separator does not automatically lower-bound the Gap-MCSP separator, which may accept those tables. At fixed beta, `s1=2^(beta n)/(c n)` also falls outside the `2^{o(n)}` threshold in the cited Atserias-Muller formula result, and formula size does not transfer to cyclic C-319 readout. The route needs reverse containment/equality or a model-preserving reduction. No q improvement. Full audit: `research/C364_APPROX_MCSP_HARDCORE_AND_DISTINGUISHER_TRANSFER_AUDIT_2026-09-29.md`.

## C-365 - Universal-circuit lifts do not transfer ambient q hardness

For a universal circuit U_s(d,x), the lifted table G_f(d,x)=U_s(d,x) XOR f(x) maps SIZE(s1) into SIZE(O(s1 log s1)), while restriction to the zero-circuit description recovers f. At OPS parameters, the lift's control/evaluation cost is O_beta(s2), so it consumes the logarithmic low/high gap; its ambient truth table has 2^(n+O(s1 log s1)) entries but the image has N independent coordinates. A target separator circuit composes to a source separator at no more than an additive O(N) gate cost, but this reduction direction does not let target hardness imply source hardness. An ambient native q lower bound likewise cannot be pulled back without an endpoint-valid restriction theorem for the image promise. An activation-register repair has enough raw bits at q=Theta(N), but computing a valid description is search/readout, which cannot be inferred from decision acceptance. No q change. Full audit: research/C365_UNIVERSAL_CIRCUIT_LIFT_SPENDS_THE_OPS_GAP_2026-09-29.md.

## C-366 - Incompressibility does not by itself make MCSP search hard

Kolmogorov complexity gives a valid Shannon-scale circuit lower bound for an Omega-prefix truth-table family, but that family is uncomputable. The proposed MCSP-search entropy inference fails because the input truth table already contains the information in the output circuit description; the identity map outputs arbitrary incompressible strings from its input using only wires. A fixed graph description need not unconditionally encode every output of an input-dependent decoder. Thus entropy counting does not rule out a C-319 activation code, and no search lower bound or q improvement follows. Full proof audit: research/C366_SELF_REFERENCE_ENTROPY_DOES_NOT_PROVE_MCSP_SEARCH_HARD_2026-09-29.md.

## C-367 - Separate description selection from all-address verification

Given a supplied circuit description d, exact equality with an explicit N-bit table has the direct upper bound O(N s1 log s1)=O_beta(N^(1+beta)) via N universal-circuit evaluations. The straightforward gate/address trace does not give a lower bound because the predicate has one output and might admit a compressed computation; fixing d proves only Omega(N) by essential input dependence. A selector plus this checker gives a sound separator, but a decision cover need not expose a selector. The native bound remains N-o(N), and neither a full-promise near-linear cover nor a P-vs-NP result was obtained. Full derivation: research/C367_DESCRIPTION_SELECTION_AND_ALL_ADDRESS_VERIFICATION_2026-09-29.md.

**C-367 fixed-query corollary:** if a verifier reads fewer than N-log2|SIZE(s2)| coordinates on a low table's accepting path, an unqueried completion is high and indistinguishable. Thus deterministic coordinate-query verification needs N-o(N) queries. The result is only a linear query bound and does not imply a lower bound for C-319's OR-of-literal features.

**C-367 linear-sketch corollary:** adaptive GF(2)-linear measurements of transcript rank r leave an affine fiber of size 2^(N-r). If r<N-log2|SIZE(s2)|, that fiber contains a high table indistinguishable from the low table. Thus deterministic exact linear fingerprints require N-o(N) independent bits; this does not imply a circuit lower bound or cover nonlinear/native readout.

**C-367 Reed-Muller extension:** for deterministic adaptive answer bits of total Boolean-polynomial degree D, the matching-transcript indicator is nonzero at the accepted low table and has degree at most D. Its support is at least 2^(N-D). Since all transcript matches must be in SIZE(s2), D>=N-log2|SIZE(s2)|=N-o(N). This is a low-degree fingerprint barrier, not a circuit or native q lower bound.

## C-368 - Every accepted low table has a near-full safe seed certificate

For monotone G_Q over the 2q seed tests, choose a minimal set S_f of true coordinates with G_Q(1_Sf)=1. The conjunction of the selected nonconstant seed clauses implies acceptance by monotonicity and is sound, hence has at most |SIZE(s2)| models. A satisfiable m-clause CNF has at least 2^(N-m) models, so m>=N-log2|SIZE(s2)|=N-o(N). This yields only q>=N/2-o(N), below the existing N-o(N), but supplies a per-anchor certificate object for state-sharing analysis. Full proof: research/C368_EVERY_ACCEPTED_LOW_TABLE_HAS_A_NEAR_FULL_SAFE_SEED_CERTIFICATE_2026-09-29.md.

**C-369 (proved subfamily calibration):** for d=2^k=Theta(s1) dividing N and r=N/d, the repeated-fiber family has 2^d tables, each of circuit size O(d); one equality CNF with 2(N-d) binary clauses defines exactly the family. Under 2^(r-3)>|SIZE(s2)|, C-326 supplies its native C-258 subcover with q=2N+2d-1. For fixed beta<1/2 the richness inequality holds eventually by circuit counting. This is not a full-promise cover or a q lower-bound change. It proves that anchor count and per-anchor certificate width alone cannot yield a superlinear state charge.

**C-370 (proved certificate-support theorem):** for any accepted low table and sufficient sound seed-CNF certificate with m clauses, the hypergraph of variables carrying f-true clause literals has hitting number at least N-log2|SIZE(s2)|. Edges of size greater than K=ceil(log2(2m)) have a hitting set of size at most N/2+1 by random half-sampling. The remaining edges retain hitting number at least N/2-log2|SIZE(s2)|-O(1); a maximal matching gives at least (N/2-h-O(1))/K pairwise-disjoint supports. For polynomial q this is Omega(N/logN). This is not a q improvement; C-258's equality certificate is consistent and supplies singleton supports.

C-370 clarification: the singleton f-true supports are those of the common equality CNF in C-369. They are not asserted to be seed clauses extracted from the separate C-258 native subcover; C-258 is used only as the matching easy-family state-count calibration.

C-370 refinement: if t_k is the number of certificate clauses with at most k f-true literals, the sampling proof gives the full tradeoff t_k >= N(2m)^(-1/(k+1)) - h - 1. In particular, for m=O(N), at least N/2-h-O(1) clauses have O(log N) true literals; and when beta<1/2, at least Omega(sqrt(N)) clauses have exactly one true literal. This strengthens the matching corollary but still supplies no state charge.

**C-371 (proved shared-cone splice lemma):** if a sound seed-CNF cone with m clauses contains low tables f,g at distance d, then the clause falsification subcubes over the 2^d owner masks cover at least 1-|SIZE(s2)|/2^d. Their measures sum to at least that quantity; each clause contributes zero if it has a common f/g true literal, and otherwise contributes exactly 2^(-|E_f|-|E_g|) for disjoint true supports. For d>=log2|SIZE(s2)|+2, one selected clause has disjoint supports with |E_f|+|E_g|<=log2(2m). This is a necessary pairwise condition, not a q lower bound; C-369 equality is the linear-cost calibration.

C-371 literature note: Cheraghchi-Kabanets-Lu-Myrisiotis prove exp(N/O~(log^2 N)) lower bounds for a single CNF or DNF computing exact MCSP, but one C-319 safe certificate cone is not the full acceptance predicate. The least-fixed-point readout may union many certificate cones, and no size-preserving flattening to one CNF/DNF is known. This result therefore does not transfer to q; see C-339 and C-371.

## C-372 - Reed-Muller dual distance forces large common policy certificates

For t=floor(delta n), choose H_2(delta)<beta and delta<1-beta, and let F=RM(t,n). Its codeword count is 2^r with r=N^(H_2(delta)+o(1)); each codeword has circuit size O(rn)=o(s1). The code has primal distance 2^(n-t)>h+2 and dual distance D=2^(t+1)=N^(delta+o(1)). If a consistent clause is true on every member of F, its support width is at least D: otherwise full projection onto that support supplies a codeword falsifying it. In a sound CNF cone containing F, every high table must falsify some clause; each clause excludes at most 2^(N-D) tables. Therefore m>=(1-|SIZE(s2)|/2^N)2^D. A single C-319 policy cone has at most 2q clauses, so it cannot contain all of F at polynomial q. This does not bound arbitrary covers: the policy can vary with the anchor, and 2^(2q) crude clause-subset regions exceed 2^r at q>=N-o(N). No state-count change. Reed-Muller parameters are supported by Elkies's coding-theory notes and the cited minimum-weight-parity-check paper; full derivation and limitation: research/C372_REED_MULLER_SHARED_POLICY_CONE_OBSTRUCTION_2026-09-29.md.

## C-373 - Reed-Muller policy diversity for arbitrary C-319 covers

Uniform F=RM(t,n) is (D-1)-wise independent by dual distance D. Every positional-policy region of a C-319 cover is a sound CNF with at most 2q seed clauses (C-334). If q is polynomial in N, Bazzi's theorem bounds the difference between the region's probability under uniform F and uniform N-bit tables by O((2q)^2.2*2^(-sqrt(D-1)/10))=2^(-Omega(sqrt(D))). Soundness makes its uniform-table probability at most 2^(h-N), so each region contains at most a 2^(-Omega(sqrt(D))) fraction of F. Completeness then requires at least 2^(Omega(sqrt(D))) distinct policy regions. The C-334 cap 2^(2q) gives q=Omega(sqrt(D)), which is weaker than the established N-o(N) floor for our delta<1/2. This adds a cross-cone policy-diversity lemma but no state-count improvement. Primary source: Bazzi, https://doi.org/10.1137/070691954. Full proof and limitations: research/C373_REED_MULLER_POLICY_DIVERSITY_BOUND_2026-09-29.md.

## C-374 - Exact ceiling for policy-region counting

For any valid cover, choosing one positional-policy region for every f in SIZE(s1) gives a sound region cover with at most M1=|SIZE(s1)| distinct regions. Since log2 M1=O(s1 log(s1+n))=o(N) and at most 2^(2q) regions are determined by the 2q seed clauses, a proof using only region count can yield at most q=O(log M1)=o(N). Thus C-372/C-373 region-count bounds cannot reach the known linear q floor. This does not make the per-cone estimates false; it retires cardinality as the charging invariant. Any continuation must exploit the shared transition graph and cross-policy support geometry. Full proof: research/C374_POLICY_COUNT_ROUTE_CANNOT_CROSS_LINEAR_2026-09-29.md.

## C-375 - Ordinary communication bits do not measure superlinear state work

For any fixed two-party coordinate split of the N-bit input table, deterministic communication is at most the smaller block size plus O(1), hence at most N/2+O(1): one party sends its entire block and the other evaluates the fixed promise separator. A proof transferring ordinary communication-bit complexity to q with only a linear loss therefore cannot establish q>N^(1+epsilon). This is only a ceiling on that transfer, not on rectangle partition or direct state-capacity measures. C-363 shows O(N) seed features can already expose the whole table; C-319 unrolling yields at most q^2 paid AND occurrences. The unresolved resource is recurrent readout work/state reuse, or an explicit full-promise near-linear cover. No q improvement. Full audit: research/C375_COMMUNICATION_INFORMATION_CEILING_AND_REGISTER_WORK_PIVOT_2026-09-29.md.

## C-376 - A native cover induces a low/high mismatch search game

For every low w and high z, an active/inactive root gives a live state. At a live state i, z falsifies at least one of its two obligation disjunctions. Bob chooses such a side; Alice chooses a disjunct witnessing i's first activation on w. A seed literal outputs a coordinate where w and z differ. A predecessor remains inactive on z and has lower first-activation round on w, so the interaction terminates within q steps. This is an exact q-state paired search protocol induced by C-319. Its output relation is only "find a differing coordinate," which has an N+1-state scan for every distinct pair, independent of circuit complexity; hence this relation alone cannot prove superlinear q. A useful strengthening must retain description coherence or another promise-specific computational constraint. The standard hazard-free KW theorem is formula-specific and requires full ternary semantics, which native supports do not provide. Full derivation: research/C376_NATIVE_CLOSURE_INDUCES_A_KW_DISCREPANCY_GAME_BUT_NOT_A_SUPERLINEAR_BOUND_2026-09-29.md.
## C-377 - Positional-policy normal form for native acceptance

For a fixed accepted low table, finite reachability-game positional determinacy supplies one global existential action per reachable state-side pair. The reachable predecessor graph is acyclic, and the policy's selected seed literals define a coordinate cube on which the same root strategy wins. Cover soundness forces that cube inside SIZE(s2), so at least N-log2|SIZE(s2)|=N-o(N) coordinates are fixed. At most 2q seed exits give q >= (N-o(N))/2, weaker than C-03's q>=N-o(N). The policy is coherent across plays for one input but may vary across inputs and need not encode a small circuit. This is an exact policy normal form and route filter, not a q improvement. Full derivation: research/C377_POSITIONAL_POLICY_NORMAL_FORM_AND_DESCRIPTION_GAP_2026-09-29.md.
## C-378 - Acyclic policy hybrids are sound; cyclic hybrids can fail

For a fixed C-319 graph, any root policy that is valid on its reachable state-side pairs, has an acyclic reachable predecessor graph, and selects only true seeds activates that root by backward induction. Hence a state-by-state hybrid of winning policies that remains valid and acyclic defines a sound cube contained in SIZE(s2). A two-state recurrence has separate winning policies on f=(0,1,1,1) and g=(1,1,1,0) whose hybrid creates a reachable 1<->2 cycle; at u=(0,1,1,0), the selected b,c seeds are true but the least fixed point is zero. Thus support/literal compatibility alone does not justify policy splicing; well-foundedness must also be proved. The explicit recurrence example is not claimed endpoint-realizable, though C-141/C-142 establish legal input-dependent rank reversals. No q improvement. Full proof: research/C378_ACYCLIC_POLICY_HYBRIDS_AND_CYCLE_OBSTRUCTION_2026-09-29.md.
## C-379 - Far-apart low codewords require distinct root-policy pairs

For F=RM(floor(delta n),n), choose H_2(delta)<beta and delta<1-beta. Then F is contained in SIZE(s1), has size 2^r for r=N^(H_2(delta)+o(1)), and minimum distance d_min=N^(1-delta+o(1))>h=log2|SIZE(s2)|. C-377 assigns each winning positional policy a sound coordinate cube with at most h free bits, so one root-policy pair can cover at most one codeword. Thus at least |F| root-policy pairs are needed and one of q root classes has at least |F|/q policies. But there are at most q(q+2N+1)^(2q) action tables, yielding only q=Omega(r/log N)=o(N) at this parameter choice. This strengthens policy diversity but does not improve q>=N-o(N); raw action-table counting remains insufficient. Full proof: research/C379_REED_MULLER_POLICY_CUBE_DIVERSITY_2026-09-29.md.

## C-380 - Acyclic switching within a root class

For any two same-root winning policies, extend them to a common closed state set, topologically rank one policy, and switch actions in increasing rank. Acyclicity is maintained at every single-slot switch. This removes cycles as an obstruction to connecting same-root policies, but inconsistent seed literals can still make hybrid cubes empty. See research/C380_SAME_ROOT_POLICIES_HAVE_ACYCLIC_SWITCHING_PATHS_2026-09-29.md.

## C-381 - Robust splice splits avoid selected policy paths

With one selected policy per low anchor, all C-380 paths contain at most |F|^2(2q+1) consistent-hybrid masks. For log|F|=o(N), polynomial q, and C-320 radius r=Theta(N^gamma/n), a random P is within radius r of any such mask or complement with probability 2^(-N+o(N)) after a union bound. C-320's robust-split failure probability is also 2^(-Omega(N)), so some robust split avoids the entire representative path set. This proves that C-320 plus selected C-380 paths cannot force a high splice. The full endpoint-realizable policy family remains unconstrained; generic counting is too large at q>=N.

The 2024 Glinskih-Riazanov read-once NBP lower bound for total BP minimization is a related model result, but there is no transfer to alternating cyclic C-319 gap covers. No q improvement; the current proved bound remains N-o(N). Full notes: research/C381_ROBUST_SPLITS_AVOID_REPRESENTATIVE_POLICY_PATHS_2026-09-29.md.

## C-382 - Projection-safe splice entropy cap

For each fixed low-anchor pair, the owner-pattern map on disagreement coordinates is injective, and every C-281-compatible context/proof product has all completions in SIZE(s2). Thus at most |SIZE(s2)| distinct compatible owner patterns occur per pair. For any such pattern, all full owner-mask extensions induce the same splice; C-320 robustness applies to every extension, and an extension within radius r exists exactly when the split projection to D is within r. A random robust split avoids the projection-neighborhoods of all patterns with probability 1-2^(-Omega(N)). This closes split-independent robust-mask forcing. It does not improve q>=N-o(N). Ref: research/C382_PROJECTION_SAFE_SPLICE_ENTROPY_CAP_2026-09-29.md.

## C-383 - Information ceilings sharpen the C-319 target

The low class has log-size O(N^beta)=o(N), positional policies of a q-state graph number at most q(2N+q+1)^(2q), and ordinary communication is capped at O(N) for these table relations. The exact 2q seed-signature factorization can carry N raw bits at q=Theta(N), so neither profile entropy nor caller labels alone explain a superlinear lower bound. The remaining target is computational work in the fixed-point readout: a promise-specific paid-AND lower bound above N^(2+2epsilon) would beat the q^2 compiler, or a direct state theorem is needed. No q improvement. Full audit: research/C383_INFORMATION_CEILINGS_AND_LFP_READOUT_WORK_2026-09-29.md.

**C-383 address-multiplexing refinement.** Counting `sN` gate/address pairs cannot yield `q=Omega(sN)`: the fixed q-state recurrence has O(q^2+qN) syntactic description bits from predecessor incidence and seed clauses. At q=Theta(N), this static capacity is O(N^2), more than sN for every OPS s=o(N). This does not construct a valid cover; the unresolved issue is whether the fixed graph can *use* the encoding coherently, subject to endpoint-containment constraints and context-free state semantics.

## C-384 - A fixed circuit's lane-selector matrix does not charge native states

For fixed `C`, equality with its truth table is the conjunction of the N signed coordinate literals `w_x` or `not w_x`. Hence its De Morgan separator, and therefore its native cyclic-intersection complexity by C-01, is O(N), matching C-03's N-o(N) lower bound. Internal gate/address contexts introduce no additional necessary truth-table tests. The matrix is also representation-dependent: replacing `C_f` by `C_f AND (H OR NOT H)` preserves f while making the tautological OR's forced witness follow H(x). Thus the matrix of one chosen circuit cannot imply a lower bound on the separator or on arbitrary C-319 covers. The standard supplied-description checker costs O(N s1 log s1) ordinary circuit gates; no endpoint-valid native graph with a coherent description channel has been constructed. The actual target is joint-description/address coherence under `exists C forall x`; changing this to `forall x exists C_x` accepts every table via coordinatewise constants. No representation-independent state-capacity theorem, C-320 forcing lemma, q improvement, or near-linear full-promise cover follows. Full derivation: `research/C384_FIXED_CIRCUITS_HAVE_ONLY_LINEAR_SELECTOR_RESIDUALS_2026-09-29.md`.

**C-384 novelty correction.** C-349 already establishes representation instability of selected-circuit witness matrices, while C-342/C-367 already isolate activation readout and supplied-description verification. C-384 is retained only as a synthesis plus the fixed-singleton bracket `N-o(N) <= rho <= N+O(1)`; it must not be counted as a new selector lower-bound route.

## C-385 - Monotone seed-order characterization

**Claim.** For fixed Q, `Accept_Q(w)=G_Q(sigma_Q(w))` with monotone G_Q. A monotone decoder of a fixed signature map separates the low/high promise iff no low signature is coordinatewise below a high signature. Equivalently, seed-coordinate rectangles cover every low/high pair.

**Proof.** Monotonicity proves necessity. For sufficiency use `G*(u)=1` iff some low signature is below u; the no-comparability hypothesis makes this accept all low and reject all high. This decoder need not be realizable by the C-319 graph.

**Consequence.** The full 2N signed singleton predicates separate every distinct ordered pair of tables, so information/order/fiber arguments alone have a universal linear ceiling. Their paired C-319 seed slots need not yield an accepting recurrence. The unresolved resource is the coupled fixed-point decoder; its standard unrolling is O(q^2). See `research/C385_MONOTONE_SEED_ORDER_ISOLATES_READOUT_COST_2026-09-29.md`.

**C-385 proof audit correction.** The dual-rail feature example uses opposing literal endpoints, so every consequence is empty and the actual recurrence has all roots as predecessors of every state. It still rejects every input because each paired seed conjunction is contradictory and zero remains the least fixed point. The report has been corrected to use this exact recurrence rather than an endpoint-inconsistent no-predecessor equation.


## C-387 - Reed-Muller probes force globally narrow seed clauses

For F=RM(floor(delta n),n) from C-372, uniform anchors are (D-1)-wise independent with D=N^(delta+o(1)), and every anchor is in SIZE(s1). For each low anchor C-368/C-370 give at least (1-epsilon)N-h-O(1) selected certificate clauses with at most k=O(log N) f-true literals, for any fixed epsilon>0. A fixed globally wide clause of width w>=C log N has probability at most N^(-(a+3)) of having at most k true literals, by a 2r-moment bound with r=Theta(log N) and 2r<D. Averaging incidences over F shows at least (1-epsilon)N-h-o(N) global seed slots have width O(log N); in particular, at least N/2-o(N). The width constant depends on the polynomial q exponent and epsilon. This is a structural localization theorem for every polynomial-state valid cover, but it does not improve q>=N-o(N). It also does not show wide features are dispensable: a minimal monotone certificate can require additional wide seed slots. Full proof and exact constants: research/C387_RM_GLOBAL_NARROW_SEED_LOCALIZATION_2026-09-29.md.

## C-388 - Hard-core selector relation complexity

At the C-346 OPS parameters, define R(f,Q) to mean every size-T circuit errs on at least 0.259 of the labelled sample Q, with |Q|=O(N^beta). C-346 proves a witness exists for every high table; no witness exists on low tables because f itself is a size-T predictor. For an explicit candidate Q, R is in coNP (a bad circuit is a polynomial-size counterexample); the existence predicate exists Q R(f,Q) lies in Sigma_2^P and separates the promise. The empirical minimax LP has an NP best-response/separation task; oracle-based multiplicative weights or ellipsoid calls are not a near-linear Boolean selector. The exact verification and counting formulations are recorded, but no efficient selector, lower bound for all selectors, or q-preserving bridge to arbitrary C-319 covers is proved. Full audit: research/C388_HARD_CORE_SELECTOR_RELATION_COMPLEXITY_AUDIT_2026-09-29.md.


## C-389 - Sparse certificates do not imply local-only readout

In the abstract seed-signature factorization, take narrow features A_i(w)=w_i for i in [N], one wide feature B(w)=OR_i w_i, and monotone readout G(a,b)=b AND (AND_i a_i). This separates the singleton low input 1^N from every other table. Its minimal true seed certificate contains all N+1 features, while the safe certificate CNF has N width-one clauses plus one width-N clause; each narrow clause has one true literal at the anchor. Forcing the wide seed coordinate to zero preserves high rejection but loses the low anchor, despite the wide CNF clause being redundant in table space. Thus C-368/C-370/C-387 and monotonicity alone do not imply a local-only decoder. This is an abstract feature-map countermodel, not an endpoint-realizable C-319 cover or an MCSP lower bound. Full audit: research/C389_NARROW_CERTIFICATE_DOES_NOT_IMPLY_LOCAL_READOUT_2026-09-29.md.

## C-390 - An endpoint-realizable subpromise cover can require a wide seed

Let F=RM(floor(delta n),n) with H_2(delta)<beta, and let U be the actual OPS high set. Its dimension r=N^(H_2(delta)+o(1)) is o(N), all codewords lie in SIZE(s1), and its exact membership circuit has size O(N log N) by the fast Boolean Mobius transform. On any r+1 table coordinates choose a pattern p omitted by F; the corresponding subcube S is disjoint from F, has codimension o(N), and contains high tables. Mask every membership-circuit wire g to g OR I_S. In the C-109 endpoint compilation, use each input-literal carrier L_(a,b) union (S intersect U). All circuit-state consequences then contain S intersect U; the output carrier is exactly S intersect U. Add an empty-consequence root with endpoints S intersect U and U minus S. Its E seed is false, while its H seed is exactly the width-(r+1) mismatch clause OR_(a in A)[w_a != p_a]. The circuit output activates the root on every f in F; the root's H self-loop and the high-carrier invariant reject every z in U. If all globally wide seeds are zeroed, this root's H side is only its self-loop and no F anchor is accepted. This is an endpoint-realizable q=O(N log N) subpromise counterexample to a universal narrow-seed deletion theorem. It is not a full Gap-MCSP cover, and it gives no superlinear lower bound or P-vs-NP result. Full proof and endpoint audit: research/C390_ENDPOINT_REALIZABLE_WIDE_SEED_REQUIRED_SUBPROMISE_2026-09-29.md.

## C-391 - Prefix self-reduction puts canonical hard-core search in FP^Sigma2

Encode a variable-length hard-core sample canonically with a length field and a fixed padded array of at most L addresses. For a bit prefix p of this encoding, let EXT(f,p) assert that some valid completion Q extending p satisfies C-388's relation R(f,Q). Since R is coNP, EXT has the form exists Q for all size-T circuits C of a polynomial-time predicate, so EXT is in Sigma2^P. Starting from EXT(f,empty), query whether each next encoding bit can be zero while preserving an extension; otherwise choose one. After O(L log N) queries this outputs the lexicographically first valid Q. With a default output when EXT(f,empty) is false, this is a total selector in FP^Sigma2^P, valid on every high table. The decision predicate EXT(f,empty) alone does not provide the conditioned prefix answers, and no encoding of those constraints into the original f-only predicate is known. An exact circuit verifier for R composed with any high-valid selector would decide the promise, but the selector alone does not. This is an oracle upper bound and exact bridge diagnosis, not a Boolean circuit bound, an all-selector lower bound, or a q improvement. Full details: research/C391_SELECTOR_PREFIX_EXTENSION_SELF_REDUCTION_2026-09-29.md.

## C-392 - A near-linear selector works on almost every sparse support

For sufficiently small fixed beta, let S=ceil(N^beta), choose W uniformly among the S-subsets of the address domain, and set f=1_W. Choose a random permutation pi and take Q to be W followed by the first S zero addresses in pi-order. Both blocks are marginally uniform S-subsets of the full domain. Hoeffding sampling-without-replacement concentration plus a union bound over all size-T circuits shows that, with probability 1-o(1), each block's circuit density is within 0.05 of its full-domain density, provided (ln 2)*0.1515*A*beta<0.005. Thus every size-T circuit errs on at least 0.45 of Q. Separately, circuit counting gives CC(f)>S with probability 1-o(1) when A*beta<1-beta. Averaging fixes a permutation pi for which both hold on 1-o(1) of W.

A fixed-pi sorting network outputs these 2S addresses in O(N log^3 N) fan-in-two gates, so it is a near-linear partial selector for the exact C-388 relation on typical weight-S high tables. This strengthens C-23 from one disagreement against the size-s1 class to constant empirical error against size T=ceil(1.515s1). It rules out lower-bound arguments whose only hard instances are a 1-o(1) fraction of uniformly random weight-S supports. It does not handle exceptional supports, give a uniform way to find pi, decide its own coNP validity, imply an all-high selector, bridge to C-319, or change q>=N-o(N). Full proof: research/C392_NEAR_LINEAR_SELECTOR_ON_TYPICAL_SPARSE_TABLES_2026-09-29.md.

## C-393 - Escape-source rounds bound paid AND work in the native readout

For any valid q-rule C-319 cover with m empty-carrier roots and v=q-m nonroot candidate rules, apply C-322 root deletion and C-92/C-93/C-94 carrier normalization. Let s be the number of distinct nonroot carrier values used as one-sided escape sources. In C-94 form, `H_t=K_t OR D_t`, where K is Hasse propagation and D is the OR of candidate conjunctions `(a_i OR L_i(x)) AND (b_i OR R_i(x))`. The same fixed points are given by the macro map `G(x)=Up(D(x))`. Each round uses at most v binary AND gates; OR, seed-clause, and support computations are free in `A_cap`. After the first round, each strict macro-round requires a previously inactive escape-source carrier to turn on. Each of the s source bits changes at most once, so at most s+1 rounds are needed. The m root-free terminal tests add at most m AND gates, giving `A_cap(Q)<=m+(s+1)v`. C-322 only equates full-system final root bits; root-free terminal tests can differ, so do not reduce the m term without another lemma.

This can improve the generic quadratic readout compiler when s is small and is combined with C-323/C-324 by taking the minimum. It does not bound s, which may be v, and proves no readout lower bound or q improvement. Local seed width does not imply a bound on escape sources. Full proof and scope: research/C393_ESCAPE_SOURCE_PAID_AND_COMPILER_2026-09-29.md.

## C-394 - Monotone signature cones give canonical safe certificates

For a valid q-rule cover Q, write `sigma_Q(w)` for its 2q seed-clause truth vector and `Accept_Q(w)=G_Q(sigma_Q(w))` for the monotone LFP readout. If Q accepts a low f, the conjunction of every seed clause true on f defines the cone `{g:sigma_Q(f)<=sigma_Q(g)}`. Every such g is accepted by monotonicity and hence lies in `SIZE(s2)`. The full anchor-by-seed-clause incidence row is therefore a canonical safe certificate, computable in O(qN) gates. This is precisely C-385's order characterization expressed as a safe cone, not a new theorem; C-368's clause-count lemma yields only `q >= (N-o(N))/2`, weaker than the existing `q >= N-o(N)`.

There is also a deterministic, possibly smaller certificate: first-activation ranks choose a root and supporting seed/lower-rank predecessor on each side of every activated rule. The resulting proof DAG uses at most 2q seed clauses, and every satisfying table replays that proof, so soundness makes its model set a subset of `SIZE(s2)`. Tie-breaking gives a total multi-output circuit of size O(qN+q^2), defaulting when Q rejects. This adds a witness extraction, not a lower bound.

For a fixed Gamma, certificate safety is `forall g [g satisfies Gamma implies exists D of size <=s2 with TT(D)=g]`, a Pi_2^P predicate under explicit truth-table encoding. The incidence row certifies safety for accepted low inputs because the LFP readout proves its upward closure lies inside Q's sound acceptance set; incidence alone does not give the required acceptance/rejection decoder. In the abstract 2N signed-singleton bank, the N clauses matching f isolate it, so certificate length/incidence remains linear and does not capture the MCSP recognition cost. This is an exact C-385 corollary plus a proof-DAG extraction, not a q lower bound, selector/native size bridge, or P-vs-NP result. Full proof: research/C394_NATIVE_COVER_EXTRACTS_SAFE_CERTIFICATES_2026-09-29.md.

## C-395/C-396 - Local restrictions force growing escape-source diversity

Fix `0<beta<1` and the promise `s1=N^beta/(c_gap log N)`, `s2=N^beta`. C-395 adapts CKLM's locally computable restriction lemma to the promise: a fixed-depth `d>2` AC0 separator has size at least `exp(N^a)` for every fixed `a<min{beta/4,(1-beta)/(2(d-2)),1/(2(d-1))}`. The proof puts a locally computable completion below `s1`, then counts completions to find one above `s2`; the middle interval is unrestricted.

C-396 uses CKLM Lemma 31 directly at growing depth. For every fixed polynomial exponent `B`, no size-`N^B` AC0 separator has depth at most `delta log N/log log N`, for any fixed `delta<(1-beta)/2` (with `delta=(1-beta)/4` a safe choice). In the C-393 macro-round compiler, depth is `O(k+1)` and size is polynomial in `q,k,N`; consequently, for every fixed `A`, all sufficiently large `N` and every valid full-promise C-319 cover with `q<=N^A` satisfy `k=Omega_A(log N/log log N)` for the distinct one-sided escape-source carrier count `k`.

This is a proof-level structural restriction on polynomial-size covers, but it does not improve `q>=N-o(N)`, lower-bound the paid-AND readout measure, or prove P != NP. C-393's compiler is an upper bound, so a lower bound on its round parameter cannot be read in reverse. Full proofs: `research/C395_GAP_AC0_RESTRICTION_ESCAPE_SOURCE_LOWER_BOUND_2026-09-29.md` and `research/C396_GROWING_DEPTH_RESTRICTION_ESCAPE_SOURCE_BOUND_2026-09-29.md`.

## C-397 - Fixed-point and selector transfer audit

The narrow-seed localization candidate was already proved in C-387, with the precise quantifier that the `O(log N)` width constant depends on fixed epsilon; C-390 refutes the inference that wide seeds can therefore be deleted from the LFP. For the C-388 relation `R(f,Q)`, any all-input selector circuit that outputs an R-valid list on every high table composes with the coNP verifier to give a promise-coNP/poly separator. Under `NP subseteq P/poly` this gives a polynomial-size Boolean separator with an uncontrolled exponent, not a near-linear OPS consequence. No reverse decision-to-selector reduction or selector-to-C-319 reduction follows. The surveyed FPC/symmetric-circuit characterization assumes uniform symmetry on relational structures, while C-319 allows nonuniform asymmetric endpoint clauses; the standard variable-permutation orbit construction costs `n!` copies. Thus this literature route supplies no q-sensitive lower bound without a symmetry-preserving, q-controlled interpretation. Native q remains `N-o(N)`. Full audit: `research/C397_FIXED_POINT_AND_SELECTOR_TRANSFER_AUDIT_2026-09-29.md`.
## C-398 - Near-linear selector-to-decision transfer under small NP-verifier circuits

Encode the sample input to one fixed NP language `BAD(n,T,Q,y)`: it asks whether some n-input circuit of size at most unary T errs on the listed labeled examples by less than 0.259. Its witness and verification are polynomial in its input length M, and at C-346's thresholds `M=O(N^beta log N)`. If this one language has circuit size `O(M^d)` for a fixed d (in particular, if `NP subseteq P/poly`), composing its negation with an all-high selector requires also computing labels `f(x_i)` at the output addresses. Direct mux/lookup costs `O(N^(1+beta) log N)`. A selector of size `N^(1+delta)` therefore gives a promise separator of size

```text
N^(1+delta) + O(N^(1+beta) log N) + O(N^(beta*d) log^d N).
```

For any fixed `epsilon>delta`, choose fixed beta below `epsilon-delta`, `1/d`, and the OPS beta limit. Then the separator has size at most `N^(1+epsilon)` for large N. This sharpens C-397's coarse polynomial-overhead implication by charging validation at the compressed sample length. Unconditionally, enumerating all predictors costs `2^(O(N^beta))`; no near-linear verifier or selector follows. The concurrent C-393/C-396 charge test gives only `q>=(N-o(N))/(s+1)` from `A_cap>=N-o(N)` and `A_cap<=(s+1)q`, with s not upper-bounded. Native q remains `N-o(N)`; no all-high selector, full-promise near-linear cover, or P-vs-NP proof is established. Full derivation: `research/C398_SELECTOR_TO_DECISION_NEAR_LINEAR_UNDER_NP_POLY_2026-09-29.md`.
**C-398 proof-carrying variant audit.** Encode existence of a size-T predictor with error below 0.259 as a SAT instance `Phi_(n,T,Q,y)`. A sound refutation makes R polynomial-time checkable when the refutation is supplied, and low tables cannot admit one. C-346 only proves that Phi is unsatisfiable for some Q on high tables; it gives no short Frege/resolution refutation bound. Thus an NP-verifiable augmented relation is possible only with a new proof-length theorem. This is a precise candidate, not an efficient selector.
## C-399 - Direct finite hard-core lists do not meet CircCons's NO promise

Let a labeled distribution over `{0,1}^m` be supported on `K` distinct points with consistent labels. The circuit `h(x)=OR_{j:y_j=1}[x=x_j]` has zero empirical error and size `O(Km+K)`. The direct C-388 sample encoding has `K<=L=O(N^beta)` and a standard table-driven sampler of size `O(Ln)`, which is too large to certify `m=n=log N > sqrt(s)`; C-346 gives no more succinct sampler for its chosen list. After padding enough to meet the side condition using this encoding, `O(Lm)<=m^(log log m)` eventually, so the distribution fails CircCons's NO condition against `SIZE(m^(log log m))`. Thus Xia's CircCons-in-SZK^A theorem does not validate the direct padded C-388 list as a hard NO sample. A different succinct large-support sampler is not ruled out, and SZK^A is not itself a deterministic verifier. No selector, state lower bound, near-linear cover, or P-vs-NP proof follows. See `research/C399_FINITE_SAMPLE_CIRCCONS_MEMORIZATION_BARRIER_2026-09-29.md`.
## C-400 - A rich mux-witness family still has linear native subpromise complexity

For fixed `0<beta<1`, write `N=2^n`, choose `r=floor(beta*n/2)`, `M=2^r`, `K=2^(n-r)`, and index coordinates by `(a,z) in {0,1}^r x {0,1}^{n-r}`. The family `F={f_y:f_y(a,z)=y_a}` has `2^M` tables, each computed by a DNF of size `O(Mr)=O(N^(beta/2)log N)<=s1` eventually. In the natural minterm DNF, each address a with `y_a=1` forces its unique true OR term. Nevertheless F is exactly the set of tables constant on every z-fiber: `w_(a,z)=w_(a,0)` for all `z!=0`. Conjoining these `N-M` equalities uses `2(N-M)-1<2N` binary ANDs over signed-literal inputs. It accepts all F and rejects every high table; the high set meets every literal half-cube. By C-307 this gives a valid native subpromise cover with `q<2N`. A member of F and the one-anchor bound give `q>=N-o(N)`, so this toy subpromise has linear native complexity. This shows address-varying witness locations in one chosen circuit representation do not force superlinear states; a global extensional invariant can bypass them. It is not a full-promise cover or state-capacity theorem. Full derivation: `research/C400_MULTIPLEXER_WITNESSES_HAVE_LINEAR_NATIVE_SUBPROMISE_2026-09-29.md`.

## C-401 - Expanded incidence is not gate work for ordinary circuits

Use the OPS ordinary-circuit target as primary. Its exact promise is N=2^n, s1=N^beta/(c log_2 N), s2=N^beta, with one fixed epsilon applying for every sufficiently small fixed beta. The theorem's proof instantiates c=10. Raw support-incidence charging is false under arbitrary sharing: all prefix parities have Theta(N^2) expanded incidence but an N-1-XOR shared DAG. Parity, repeated-block equality, bounded-degree sparse parity checks, and simple global block relations likewise have O(N)-gate readouts. The share-aware total-gate measure B(H), which computes the entire syndrome vector Hx with unrestricted fanout, avoids this accounting mistake, but no reduction forces an arbitrary one-bit promise separator to compute Hx; linear-map lower bounds do not supply this transfer. The scalar zero-test route also has an entropy ceiling: any linear space contained in the low set has dimension O(N^beta), and the ambient candidates number only 2^(O(N^(1+beta))), insufficient by counting for N^(1+epsilon) when beta<epsilon. An explicit full-promise separator by enumerating all low circuits costs O(N*2^(O(N^beta))) gates. The ordinary OPS lower-bound target and native q frontier are unchanged. Full report: research/C401_SHARED_READOUT_CHARGE_AND_ORDINARY_GATES_2026-09-29.md.

The Atserias–Müller 2025 uniform magnification theorem for approximate MCSP is an additional literature lead. Direct transfer fails because its threshold requires sigma=2^(o(n)), whereas fixed-beta OPS s1 is 2^(Theta(n)); it treats P-uniform circuits and an approximation NO set that covers the unconstrained middle band. The proven patching estimate only places OPS high tables inside that stronger approximate NO set. This is not an ordinary Gap-MCSP lower bound; details and primary citations are in C-401.

## C-402 - Promise subfunctions do not charge shared DAG gates

For each input block of a partial promise, form the graph of outside contexts, connecting two contexts when some common block assignment has opposite promised labels. Every total separator restricts to a proper coloring, so the graph's chromatic number is bounded by the number of its block restrictions; this part preserves the undefined middle. At OPS parameters, there are at most `2^(O(N^beta))` YES tables. At most that many contexts per block have any YES completion, and every other context has only 0/undefined labels, so `log chi_i=O(N^beta)` and the total over at most N blocks is `O(N^(1+beta))`. It cannot reach the fixed `N^(1+epsilon)` target when beta<epsilon. Independently, indirect storage access has `Theta(m^2/log m)` total block-subfunction profile and an `O(m)` fan-in-two DAG, so additive profile-to-gate charging fails under reuse. Retire this route for OPS-scale total gates; retain the per-block coloring lemma as a diagnostic. Full-promise enumeration remains `O(N*2^(O(N^beta)))`; ordinary and native frontiers are unchanged. See `research/C402_PROMISE_SUBFUNCTION_CHARGE_AND_DAG_SHARING_2026-09-30.md`.

## C-403 - Sparse non-High region forces near-full essential support

For OPS Gap-MCSP with `s2=N^beta`, the number of non-High tables is at most the number of size-`s2` circuit descriptions, `2^(O(N^beta log N))`. The all-zero table is YES. If a valid separator has u inessential truth-table inputs, fixing all essential inputs to zero and varying those u coordinates gives an accepted subcube of size `2^u`; every point must be non-High. Hence `u=O(N^beta log N)` and at least `N-O(N^beta log N)` inputs are essential. The output ancestor DAG is connected; with S' fan-in-at-most-two gates, I input vertices and at most two constant sources, its at most 2S' wires imply `S'+I+c-1<=2S'`, so total gates are at least the essential-input count minus one. Therefore every separator has `S>=N-O(N^beta log N)-1=(1-o(1))N` for fixed beta<1. This is a true ordinary total-gate lower bound, independent of middle-band labels and arbitrary sharing, but the support mechanism is capped at N. A weight-threshold separator of O(N) gates handles the sparse low subpromise only and misses low tables such as parity. Full-promise enumeration remains `O(N*2^(O(N^beta)))`. No N^(1+epsilon), native q, or P-vs-NP improvement. Proof: `research/C403_ACCEPTED_SUBCUBE_DIMENSION_LINEAR_GATE_FLOOR_2026-09-30.md`.

## C-407 - Random coordinate supports yield an easy restricted promise

Fix `0<beta<1/2`, `N=2^n`, `s1=N^beta/(10n)`, `s2=N^beta`, and `beta<gamma<1-2beta/5`. A uniformly random coordinate set `P` of size `m=N^gamma` avoids containing the support of any size-`s1` circuit table of weight at least `5s1`: the count of such circuits is `2^((2beta+o(1))s1n)`, while containment probability for each support is at most `(m/N)^(5s1)=2^(-(5(1-gamma)+o(1))s1n)`. The union bound tends to zero. Hence every low table supported in P has weight below `5s1`. Conversely any weight-`w` table has a minterm circuit of at most `wn+n-1` gates, so `w<=8s1` implies complexity `<s2` for large N. Therefore weight threshold `6s1` separates the entire induced promise on `V_P={f:supp(f) subseteq P}` in `O(m log^2 m)` gates. This is a rigorous counterconstruction to random coordinate restrictions as a source of hard traces, not a separator of the full promise: parity and other dense low tables are outside `V_P`. The support P is obtained nonuniformly; no efficient construction is established. No ordinary or native frontier improves. Full proof: `research/C407_RANDOM_SUPPORT_RESTRICTION_COUNTERCONSTRUCTION_2026-09-30.md`.

## C-406 - Formula hardness forces logarithmic circuit reconvergence

Let C be an OPS Gap-MCSP separator at `N=2^n`, thresholds `s1=N^beta/(c n)`, `s2=N^beta`. For the output ancestor DAG, form the gate-to-gate graph and count each primary-input pin as a separate formula leaf; define `mu=E_g-G+1`. Unfolding gives a De Morgan formula with at most `2S2^mu` leaves. The input-pin count gives `mu<=G-E(C)+1`, hence `S>=E(C)+mu-1`. OPS Theorem 5 supplies, for each `0<alpha<2`, a formula-hard promise with low `n^d` and high `N^(alpha/2-o(1))`. If fixed `beta<alpha/2`, these YES/NO sets lie inside the OPS YES/NO sets, so C also separates that formula-hard promise. Hence `2S2^mu>N^(2-alpha)`. For `S<=N^(1+delta)`, `delta<1-alpha`, this gives `mu>(1-alpha-delta)log_2 N-O(1)`. Optimizing fixed `alpha>2 beta` and `delta>0` shows that for every `beta<1/2` and `gamma<1-2 beta`, all separators satisfy `S>=E(C)+gamma log_2 N-O(1)`. This is an additive gate improvement over the essential-input count, though the main `N-O(N^beta log N)` order and OPS exponent frontier remain unchanged. Exact proof and transfer: `research/C406_CYCLE_RANK_FORMULA_TRANSFER_2026-09-30.md`.

## C-408 - Random balanced block restrictions have a cheap complete trace

For fixed `0<beta<1/2`, `s1=N^beta/(10n)`, `s2=N^beta`, and `beta<gamma<1`, take `m=2^floor(gamma n)` equal blocks of `r=N/m` coordinates. For a fixed set `S` of weight `w=kr`, a uniform labeled balanced partition makes it a union of blocks with probability `binom(m,k)/binom(N,w) <= (N+1)2^(-(N-m)H_2(w/N))`. The number of size-`s1` AND/OR/NOT circuits is `2^((2beta+o(1))s1n)`, while for `5s1<=w<=N-5s1` the entropy exponent is `(5(1-beta)+o(1))s1n`; the union-bound gap is `(7beta-5+o(1))s1n<0`. Hence some partition has no low block-constant table in that weight band. Minterm DNF/CNF gives `CC<s2` within distance `6s1` of either constant, so the entire induced promise is separated by the Hamming-ball threshold `r*min(wt(x),m-wt(x))<=6s1`, using `O(m log^2m)` gates. This is a proved easy-trace counterconstruction for random repeated-block restrictions, not an ordinary full-promise lower bound or a new general theorem. Parity is outside this random slice; the trace computation is cheap. No numeric frontier changes: `S>=N-O(N^beta log N)-1` with C-406's additive logarithmic refinement; OPS `N^(1+epsilon)` open; native `rho>=N-o(N)` unchanged. Full proof and resource accounting: `research/C408_RANDOM_BLOCK_SUBSPACE_TRACE_2026-09-30.md`.

## C-409 - Full-table pseudorandomness conditionally excludes OPS separators

Fix epsilon>0 and beta in (0,1). If a distribution D_n over N=2^n-bit tables is supported on functions of circuit size at most `s1=N^beta/(c n)` and is indistinguishable from uniform by all nonuniform circuits of `N^(1+epsilon)` gates, then no such circuit separates the OPS promise with NO threshold `s2=N^beta`. A uniform table is High with probability `1-2^(-N+o(N))`, since size-`s2` circuit descriptions number `2^(O(N^beta n))`; a separator would accept D_n with probability one and uniform with probability `o(1)`. A PRF on n-bit addresses with n^2-bit keys has poly(n)-size output functions and matches the Low threshold for each fixed beta>0; security `2^(k^alpha)` with alpha>1/2 exceeds the target distinguisher scale `2^((1+epsilon)sqrt(k))`. The general local-PRG framework is established prior art; this is a parameter-matched conditional specialization, not an unconditional theorem about arbitrary circuits. Affine, sparse-linear, and repeated-block distributions have O(N polylog N) distinguishers. Ordinary and native frontiers do not change. Full proof and comparison: `research/C409_FULL_TABLE_PSEUDORANDOMNESS_CONDITIONAL_GAPMCSP_2026-09-30.md`.
## C-410 - Shared batch readout eliminates per-address table-mux charging

For an `N=2^n`-bit table and any `q` possibly table-dependent `n`-bit addresses, there is a fan-in-two DAG that outputs all `(a_j,f(a_j))` pairs using `O((N+q)log^3(N+q))` additional gates. Sort `N` tagged table records and `q` tagged query records by `(address,type,id)` with the table record first on ties; a linear prefix scan propagates the table bit to every following query record at the same address; sort again by query ID to return outputs in order. Bitonic sorting uses `O(M log^2M)` comparators for `M=N+q`, each comparator costs `O(log M)` gates. The construction handles arbitrary dependencies, repeated addresses, and unrestricted fanout.

At OPS parameters `t=2^(10 beta n)=N^(10 beta)`, this replaces the proof's separate `O(tN)` table-address formatter by `O(N log^3 N)` when fixed `beta<1/10`. The existing conditional selector size `N^(1+k beta)` and Succinct-MCSP verifier size `(poly(n)t)^ell` remain; hence the theorem's conditional `N^(1+epsilon)` upper consequence and magnification quantifiers do not change. The result disproves only a per-query gate charge, not the lower-bound program. Full-promise enumeration remains `O(N*2^(O(N^beta)))`; ordinary and native frontiers are unchanged. Proof and accounting: `research/C410_SHARED_MULTIQUERY_TRUTH_TABLE_READOUT_2026-09-30.md`.
## C-411 - Target-scale fixed anti-checker menus violate locality

Fix `s1=N^beta/(10n)`, `s2=N^beta`, and `kappa>=1` with `kappa*beta<1`. If a fixed menu of `L<=N^(2-delta)` sets, each of size at most `N^(kappa beta)`, anti-checks every `f` with `CC(f)>s2` against all circuits of size `s1`, then an AND of `L` NP Succinct-MCSP oracle calls computes `MCSP[n^c,N^beta]`. Each oracle fan-in is `m=N^(kappa beta+o(1))`; the oracle-formula measure is `SIZE3<=L*m^3=N^(2-delta+3*kappa beta+o(1))`, and adaptivity is one. Chen et al.'s Theorem 59 forbids this whenever `delta>(3*kappa+2)*beta`: choose `2*beta<epsilon_loc<delta-3*kappa*beta` and `alpha=epsilon_loc/beta>2`. Hence at `kappa=10`, no such static menu with fixed saving `delta` exists for `beta<delta/32`. This is a route-specific static-menu impossibility, not a general Gap-MCSP circuit lower bound, not an adaptive-selector lower bound, and not a P-vs-NP result. Full proof: `research/C411_TARGET_SCALE_STATIC_ANTICHECKER_MENU_LOCALITY_OBSTRUCTION_2026-09-30.md`.
## C-412 - Patch balls around low circuits are forced YES, but do not charge gates

For OPS s1=N^beta/(10n), let r=floor((floor(s1/2)-n-3)/n). If CC(f)<=floor(s1/2) and |R|<=r, the table f XOR 1_R has a circuit of size at most CC(f)+|R|n+n+3<=s1. Hence every separator accepts B_r(C_{floor(s1/2)}) and rejects C_{>=s2}. This is a precise full-promise local-flatness constraint with r=Theta(N^beta/n^2). The attempted potential, accepted neighborhood volume, has no proved per-gate growth bound. An O(N)-gate population-count threshold wt<=k+r, for k=floor(s1/(8n)), accepts the full radius-r neighborhood of every sparse table of weight <=k; all accepted tables are YES, but dense low tables such as parity are omitted. Repeated-block equality, O(N)-incidence parity checks, prefix parity chains, and simple copy/XOR block relations all have O(N)-gate shared readouts. These refute generic local-incidence charges, not the full-promise target. The exact full-promise enumerator remains O(N 2^(O(N^beta))). No quantitative frontier changes. Full proof and resource accounting: research/C412_LOW_CIRCUIT_PATCH_BALLS_NO_GATE_CHARGE_2026-09-30.md.

## C-413 - Batched lookup compilation and failed OPS transfer

For a fixed lookup table on K=2^(L+1)-1 possible query strings and Q nonadaptive queries generated by an S-gate ordinary circuit, a sorting-network dictionary compiler computes all answers with S+O((Q+K)(L+log(Q+K))log^2(Q+K)) total AND/OR/NOT gates. Applying it at d oracle-query dependency layers yields S+O(d(Q+K)polylog(Q+K)). A random L-bit lookup itself needs Omega(K/L) total gates by circuit counting. This is a proved shared-computation control mechanism for explicit lookup tasks, but no promise-preserving map forces an arbitrary one-bit Gap-MCSP separator to compute that lookup below its cost; the obvious map already performs the lookup or omits the consistency condition. Ilango's random-oracle MCSP reduction has oracle-relative witness circuits and a constant-factor gap around M/log M, while OPS needs s2/s1=10 log M. The full-promise enumerator remains O(N 2^(O(N^beta))); the ordinary and native quantitative frontiers are unchanged. Full proof and source audit: research/C413_BATCHED_LOOKUP_CHARGE_FAILS_TO_TRANSFER_TO_OPS_2026-09-30.md.

## C-414 - Promise support capacity closes a cheap indexed-lookup reduction

For any YES table `u` and NO table `v`, minterm patching gives `dist(u,v)>=Delta=max(0,ceil((s2-s1-n-3)/n))=Theta(N^beta/n)`. For a single-instance encoder `E(A,i)` of R fan-in-two gates outputting N bits, if a valid separator h satisfies `h(E(A,i))=A_i` for every arbitrary K-bit A and every i, then all K data bits must influence E; at most N can pass directly to outputs and at most 2R through gate pins, so `K<=N+2R`. Also `E` followed by h computes `MUX_K`, whose K essential data inputs force at least K-1 gates, so `R+S>=K-1`. For t tables and a B-gate postprocessor that may inspect i, the generated tables, and their h outputs but receives no raw source-bit bypass, the exact bounds generalize to `K<=tN+2R` and `R+tS+B>=K-1`. If `R+B=o(K)`, then `K/t<=N(1+o(1))`, so this MUX transfer cannot force a superlinear per-call S; if `K/t>N^(1+epsilon)`, the encoder itself must already use Omega(K) gates. This closes only cheap indexed-readout reductions, not direct OPS lower bounds. A parity-replication map has edge distance N for every source-bit flip but uses O(N) gates, so edge expansion is not additive gate work. The exact enumeration upper and all quantitative frontiers are unchanged. Full proof: research/C414_PROMISE_EMBEDDING_SUPPORT_CAPACITY_NO_GO_2026-09-30.md.

## C-415 - Exact simple-extension labels do not transfer to the OPS promise

For a table on `d` variables the OPS thresholds are `s1=2^(beta*d)/(10d)` and `s2=2^(beta*d)`. An f-Simple-Extension NO label only negates the exact condition `CC(g)=CC(f)+m`; it does not force the exponential-in-d high threshold. Explicitly, for `f(x)=OR_r(x)`, `m>=r+2`, and `g(x,y)=OR_r(x) OR PARITY_m(y)`, `0^m` is a key, every input is essential, and `CC(g)>=CC(PARITY_m)>=3(m-1)>r-1+m=CC(f)+m`, while a linear parity circuit gives `CC(g)=O(r+m)`. Thus this simple-extension NO is a Gap-MCSP YES for every fixed beta and sufficiently large m. More generally, for any nondegenerate base with a zero input and an explicit U-gate circuit, adjoining U+6 parity variables yields an f-Simple-Extension NO of O(d) circuit size. OR-products of k copies have O(km) gates on km variables and remain below s1. The 2026 STACS result establishes XOR-Simple-Extension in P and identifies MUX as a candidate exact-structure problem, but no OPS gap reduction follows. This is a reduction-scale obstruction, not a lower bound. Exact full-promise enumeration stays `O(N 2^(O(N^beta)))`; ordinary and native frontiers are unchanged. Full proof and sources: `research/C415_SIMPLE_EXTENSION_GAP_AMPLIFICATION_FAILS_2026-09-30.md`.
## C-416 - Completion entropy limits random totalization, not shared gate work

Let M=2^d and let Low_s1 contain d-variable truth tables of ordinary fan-in-two AND/OR/NOT circuit size at most s1=M^beta/(10d). Circuit descriptions give log2|Low_s1|=O(s1 log(s1+d))=O(M^beta). A partial table with u stars has 2^u completions, so uniform filling hits Low_s1 with probability at most |Low_s1|/2^u. More generally, a completion sampler of min-entropy h hits Low_s1 with probability at most |Low_s1|2^-h. Hence high-entropy randomized totalization cannot preserve an existential-low-completion YES instance when h exceeds O(M^beta). This is a sampler statement only: correlated parity, repeated-block, sparse-check, and simple global-block generators sample Low tables with low seed entropy even from the all-star table. No circuit gate inequality follows; f-SEP* is not automatically the low-completion predicate. Exact enumeration remains O(M*2^(O(M^beta))) gates; ordinary and native frontiers are unchanged. Full proof and scope: research/C416_PARTIAL_TABLE_COMPLETION_ENTROPY_LIMIT_2026-09-30.md.

The strongest gate-level countertest checks the sample structure directly. Affine-parity membership is certified by constant first derivatives and costs O(M log M) gates; repeated-block equality costs O(M); the sparse suffix parity-check family has O(M log M) direct checking cost. These are incomplete subpromise classifiers, not full-promise separators, but they rule out charging the number of local equations or incidences as independent gates. The full-promise classifier remains O(M*2^(O(M^beta))).

## C-417 - Paired-family maps expose an output-model tradeoff

Let M=2^d, and let a bitwise generator G(z,a) have R fan-in-two gates. For each fixed z, T_z(a)=G(z,a) has CC(T_z)<=R+O(1), so a promised High output forces R+O(1)>=s2. A generic composition with an S-gate separator evaluates G once at each of the M addresses and costs at most S+MR+O(1); any improvement requires a proved batch-sharing compiler. By contrast, a multi-output map E(z) with R gates and M designated output wires composes with the separator at S+R, but R does not bound CC(T_z): two gates plus M output-wire choices can map one source bit to the zero table or to any fixed High table. If outputs select among r computed signals using a q-gate address router, then fixing z yields CC(T_z)<=q+c_mux*r+O(1), and High forces q+c_mux*r+O(1)>=s2 up to a basis-dependent constant. This is an exact accounting result and an elementary output-routing counterexample, not a new lower bound. It identifies wires/descriptions/uniformity as separate charges. Parity, repeated blocks, sparse checks, and global relations remain cheap failures of local-incidence charges. The exact full-promise separator is still O(M*2^(O(M^beta))); ordinary and native frontiers are unchanged. Full proof: research/C417_PAIRED_FAMILY_OUTPUT_MODEL_TRADEOFF_2026-09-30.md.

## C-418 - High-threshold random block traces still have a cheap shared selector

For every fixed `0<beta<1` and `0<gamma<1-beta`, take `M=2^d` and `q=2^floor(gamma*d)=Theta(M^gamma)` equal blocks. A fixed nonconstant table of weight `w=kr` is block-constant with probability `binom(q,k)/binom(M,w) <= (M+1)2^{-(M-q)H_2(w/M)}`. The minimum entropy exponent is `Theta(M^(1-gamma) log M)`, which beats the `2^{O(M^beta d)}` circuits below the actual OPS high threshold `s2=M^beta`. Thus some partition makes every nonconstant block-constant table OPS-NO, while `0^M` and `1^M` are YES. The induced promise is still decided by comparing one representative per block, with `O(q)=O(M^gamma)` gates; `gamma=1/2` gives the square-root special case for `beta<1/2`. Fixing one block to zero gives a fully promised multi-output embedding of `q-1` source bits whose label is `NOR`; more generally `R` shared block signals induce a source label computable in `R+O(q)` gates. This strengthens C-408's restriction geometry but closes balanced-block routed traces as hard-source reductions. It does not handle tables outside the slice, including address parity, and is not a full-promise separator. Gates, output wires (`M`), partition description (up to `O(M log q)` bits), and `Theta(M)` output-writing time remain distinct; the partition existence proof is nonuniform. Native fusion resources are not analyzed. **No frontier change:** ordinary `S>=M-O(M^beta log M)-1` plus C-406's additive logarithmic refinement; OPS `M^(1+epsilon)` open; native `rho_GapMCSP>=M-o(M)` unchanged; exact full-promise upper `O(M*2^(O(M^beta)))`. Full proof: research/C418_HIGH_TRACE_RANDOM_BLOCKS_STILL_EASY_2026-09-30.md.


## C-419 - Every balanced-block dimension has an easy induced promise

For fixed `beta<1/2` and any fixed `gamma in (0,1)`, set `M=2^d, q=2^floor(gamma*d)=Theta(M^gamma)` and partition the table coordinates into q equal blocks. If `gamma<=beta`, then `gamma<1-beta` and C-418 gives a partition where every nonconstant block-constant table has `CC>=s2=M^beta`; equality of one representative per block decides the complete induced promise in `O(q)` gates. If `gamma>beta`, C-408 gives a partition where every Low trace lies within `5s1` of a constant and every trace within `6s1` of a constant is below `s2`; its Hamming-ball threshold decides the complete induced promise in `O(q log^2q)` gates. The two cases cover all fixed `gamma in (0,1)`, so every balanced equal-block dimension has an exact induced separator of `M^(gamma+o(1))` size. This retires the full balanced-block restriction family as a hard-trace route, but it is not a full-promise separator; parity remains outside the slices. Gates, `M` output wires, partition description, and output materialization time remain separate. Native fusion is untouched. **No frontier change:** ordinary `S>=M-O(M^beta log M)-1` plus C-406's additive logarithmic refinement; OPS `M^(1+epsilon)` open; native `rho_GapMCSP>=M-o(M)` unchanged; exact full-promise upper `O(M*2^(O(M^beta)))`. Full proof: `research/C419_ALL_BLOCK_DIMENSIONS_HAVE_EASY_TRACES_2026-09-30.md`.

## C-420 - Codeword-hard traces do not charge the separator

For fixed `0<beta<1`, circuit counting and a random-subspace union bound give an `r`-dimensional `W<=F_2^N` with `W\{0}` entirely OPS-High whenever `N-r>O(N^beta log N)`, while `0^N` is Low. Counting codimension-r subspaces of `F_2^K` shows some kernel-membership predicate needs `Omega(r(K-r)/log K)` ordinary fan-in-two gates. Yet for `T(x)=E(Hx)` with `im(E)=W` and `ker(H)=C`, the induced promise is zero versus nonzero, decided by `NOR_N` in `O(N)` gates. Thus `CC(1_C)<=R+O(N)` for every table-map circuit of R gates, and any claimed hardness is paid by the map; no lower bound on the Gap-MCSP separator follows. Also, any rank-k linear sketch separating the full OPS promise requires `k>=N-O(N^beta log N)`: otherwise its kernel has more elements than the number of tables of circuit size `<s2` and contains a High collision with `0^N`. The full-promise enumerator remains `O(N 2^(O(N^beta)))`. No ordinary, native, or P-vs-NP frontier change. Full proof: `research/C420_CODEWORD_HARD_TRACES_DO_NOT_CHARGE_THE_MAP_2026-09-30.md`.

## C-421 - Gate-proof certificates yield anti-checkers of length at most N

For every fan-in-two separator C of S total gates and every High truth table f, mark a local forcing certificate at the output and propagate marks backward through C's evaluated DAG. Each marked gate contributes at most two selected pins; shared gates are processed once. The resulting coordinate mask Q_f has `|Q_f|<=min(N,2S)` and every table agreeing with f on Q_f also makes C output 0. Since every Low table makes C output 1, Q_f is an anti-checker for all size-s1 circuits. The mask is computable from f by an `O(S)`-gate forward-evaluation/reverse-marking circuit; explicitly serializing up to N addresses is a separate `O(N polylog N)` formatting term. This uses total fan-in-two gates and unrestricted fanout. The bound can be N, and parity has exact zero-certificate complexity N, so it does not yield the OPS `N^(10 beta)` sample size. Short-certificate existence is Sigma2^P (fixed-Q validity is coNP), with the middle-band extension of C as the obstacle to importing an arbitrary anti-checker. Exact full-promise upper remains `O(N 2^(O(N^beta)))`; ordinary and native frontiers unchanged. Full proof: `research/C421_SEPARATOR_CERTIFICATES_ARE_ANTICHECKERS_BUT_NOT_SHORT_2026-09-30.md`.

## C-422 - Fractional anti-checkers are short, but do not charge separator gates

For s1=N^beta/(10n), s2=N^beta, and every High table f, define lambda(f)=max_mu min_{CC(g)<=s1} Pr_{a~mu}[f(a)!=g(a)]. Finite minimax plus majority composition proves lambda(f)>=1/4: if a distribution over Low circuits made every address wrong with probability below 1/4, the majority of k=8 ln(2N)+O(1)=O(n) samples would compute f everywhere, at total cost k*s1+O(k log^2 k)<s2. Circuit counting and sampling then give, for each such f, an anti-checker multiset of O(log |Low|)=O(N^beta) addresses on which every Low circuit errs on a constant fraction. The core anti-checker theorem is established prior work (Lipton-Young 1994; OPS uses it); this cycle provides explicit OPS gate accounting and audits the transfer.

This does not improve the separator lower bound. The anti-checker only excludes Low completions; an arbitrary separator may accept middle-band completions, so the list need not be a zero-certificate of its evaluation. No O(S+N^(1+O(beta))) circuit computing the sample from a separator was derived; minimax best response is an NP search over Low descriptions. The full-promise sample-plus-verifier idea is therefore not implemented. The explicit exact separator is still Low-table enumeration with O(N 2^(O(N^beta))) total gates. Ordinary frontier remains S>=N-O(N^beta log N)-1 plus C-406's additive logarithmic refinement; OPS N^(1+epsilon) open; native rho_GapMCSP>=N-o(N) unchanged. Full proof and countertests: research/C422_FRACTIONAL_ANTICHECKERS_DO_NOT_CHARGE_SEPARATOR_GATES_2026-09-30.md.

## C-423 - Boundary-pivot selectors can miss a Low table

The candidate selector samples the first accepting coordinate on a random-order path from a rejected input to a uniformly random distinct Low endpoint. It does not generically anti-check every Low endpoint. In a fully specified O(N)-gate toy, `L_A` has `2^t` sparse Low tables activating an A-literal branch and one special sparse Low table h activating a disjoint B-branch; for `f=0`, the pivot hits `D_h` with probability exactly `1/(2^t+1)`. Here `t=Theta(N^beta/n^2)`, each endpoint has a minterm DNF below `s1`, and `log|L|=O(N^beta)`. A parity variant with uniform weight-r endpoints has hit probability `r/N`. Since f=0 is Low in MCSP, these examples refute only an attempted generic inference from boundary behavior, endpoint entropy, and Hamming distance; they do not refute an actual-High-specific theorem or build a valid Gap-MCSP separator. The mechanism is retired pending such a theorem.

The paired linear-sketch attempt `w -> H(w) -> membership in H(Low)` cannot reduce the sketch to substantially fewer than N bits: if `dim ker H > log |SIZE(<s2)|=O(N^beta n)`, the kernel contains a High table, which collides with Low `0^N`. Nonlinear full-promise construction remains open; exact enumeration stays O(N*2^(O(N^beta))) gates. Four shared-computation checks remain O(N) for parity/equality/global blocks and O(L+m) for m sparse parity checks with L incidences, so incidence is not total-gate work. No quantitative frontier changes. Full proof and limitations: `research/C423_BOUNDARY_PIVOTS_MISS_LOW_TABLES_2026-09-30.md`.
## C-424 - Actual High table defeats the local pivot law; completeness is the missing global constraint

A counting-hard function `q` on `k=floor(alpha n)` bits, `beta<alpha<1`, can be placed on a simple address subcube B of size `m=Theta(N^alpha)` and zeroed elsewhere. Restriction proves `CC(f)>=CC(q)=Omega(N^alpha/n)>s2`. There is an `O(N)` circuit C accepting exactly `2^t` low sparse modifications of a fixed large table region plus one special low singleton h, with `t=Theta(N^beta/n^2)`. Every accepted table has circuit size below s1, so C rejects every High table, but it rejects other Low tables and is not a separator. Uniform random-order boundary pivots hit h's mismatch set with probability `O(N^(alpha-1))+2^-t=o(1)`. Thus local correctness at an actual High input and global soundness do not suffice; full completeness over all Low tables is the unexploited constraint. This is a counterexample to the pivot bridge, not to Gap-MCSP.

The accepting-certificate cylinders of any full separator lie within `SIZE(<s2)`, hence have at most `O(N^beta n)` free bits. A separated Low code forces `2^(Theta(N^beta/n^2))` distinct certificates, but partial-assignment counting gives only `S=Omega(N^beta/n^2)`. The certificate-count attempt is below the established linear floor and does not charge shared reuse. Exact complete separator construction remains `O(N*2^(O(N^beta)))` by Low-description enumeration.

**Frontier unchanged:** ordinary `S>=N-O(N^beta log N)-1` with C-406's additive logarithmic refinement; OPS `N^(1+epsilon)` open; native `rho_GapMCSP>=N-o(N)`; no P-vs-NP result. Full proof: `research/C424_HIGH_TABLE_PIVOT_FAILURE_AND_COMPLETENESS_BARRIER_2026-09-30.md`.