# Claim ledger

Status labels: PUBLISHED, PROJECT-PROVED, CONDITIONAL, TESTED, OPEN. Project proofs still require an independent hostile reconstruction.

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

## C-13 Ã¢â‚¬â€ High-anchor interpolation gives only a sublinear complement-side bound

**Statement.** Let \(N=2^n\), \(Y\) be the truth tables of circuit size at most \(s_1\), \(Z\) those of size at least \(s_2\), and \(\mathcal B\) the \(2N\) literal slices on \(\Gamma=Y\sqcup Z\). The project leaf-trace argument, applied with target \(Z\) and opposite side \(Y\), gives only
\[
\rho(Z,\mathcal B)=\Omega(s_1/n)=\Omega(N^\beta/n^2)
\]
at \(s_1=N^\beta/(cn)\). It does not give \(N-\log M_1\).

**Status.** PROJECT-DERIVED ELEMENTARY LEMMA, independently reconstructed this turn. It is sublinear and does not improve the leading \(N-o(N)\) bound from C-03.

**Proof.** Fix a high anchor \(a\in Z\). The first empty intersection in a trace over \(Y\) uses at most \(m+1\) matching literal leaves if the pair list has \(m\) rules. If these leaves fix \(q\) distinct truth-table coordinates, their subcube consists of all tables matching \(a\) on those positions and is disjoint from \(Y\). But any prescribed 0/1 pattern on \(q\) distinct positions can be interpolated by a Boolean DNF: use one minterm for each position prescribed 1 and disjoin them. With fan-in-two gates this costs at most \(O(qn)\) gates. Thus if \(q\le s_1/(C n)\) for a suitable fixed constant \(C\), this subcube contains a table in \(Y\), a contradiction. Therefore \(q>\Omega(s_1/n)\), and \(m+1\ge q\) proves the claim. Both constant truth tables in \(Y\) ensure the matching literal generators required by the high-anchor semi-filters are nonempty.

**Correction of failed argument.** The statement Ã¢â‚¬Å“the cube contains no low table, therefore its size is at most \(M_1\)Ã¢â‚¬Â is false. The cube may contain gap and high tables. The attempted estimate \(\rho(Z)\ge N-\log M_1-1\) and the derived \(2N-o(N)\) gate bound are withdrawn.

**Scope.** By complement duality this contributes to \(D_\cup(Y\mid\mathcal B)\), but only a lower-order term. The one-sided \(N-o(N)\) result C-03 remains the strongest asymptotic lower bound recorded here.

## C-14 Ã¢â‚¬â€ Acyclic circuit complexity is the minimum sufficient magnification target

**Statement.** For the promise classifier on \(\Gamma=Y\sqcup Z\), the OPS theorem only requires a slightly superlinear lower bound on ordinary (acyclic) circuit size. In the literal-slice model it suffices to prove \(D(Y\mid\mathcal B)>N^{1+\epsilon}\) in the exact theorem quantifiers. A lower bound \(\rho(Y,\mathcal B)>N^{1+\epsilon}\) is sufficient but stronger, since \(\rho\) is cyclic intersection complexity and \(\rho\le D_\cap\le D\).

**Status.** PROVED implication / route refinement; not a new lower bound.

**Proof.** Each generator in \(\mathcal B\) is the truth set, restricted to \(\Gamma\), of a positive or negative input literal. Translating each AND gate to intersection and each OR gate to union shows that every De Morgan circuit separator of size \(S\) has \(D(Y\mid\mathcal B)\le S\) on the promise domain. Conversely, every set-construction sequence gives a De Morgan circuit on the full truth-table input whose behavior on \(\Gamma\) is the required separator. A circuit over any fixed fan-in-two complete basis has a constant-factor De Morgan simulation. Thus if \(D>N^{1+\epsilon'}\) for infinitely many lengths, with \(\epsilon'>\epsilon\), no arbitrary-basis circuit of size \(N^{1+\epsilon}\) can solve the promise at those lengths once \(N\) is large enough; exponent slack absorbs the conversion constant. Apply OPS with the smaller exponent.

**Proof location / dependencies.** C-01, C-02, and C-04; CavalarÃ¢â‚¬â€œOliveira definitions of discrete and intersection complexity, and OPS Theorem 1.4.

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

## C-15 Ã¢â‚¬â€ No fixed query set is an anti-checker for all high-complexity truth tables

**Statement.** Let $N=2^n$. Fix any set $Q\subseteq\{0,1\}^n$ of at most $t=2^{10\beta n}$ query points, and let the high threshold be $s_2=2^{\beta n}$, for fixed $0<\beta<1/10$. For all sufficiently large $n$, there is a truth table $f$ of circuit complexity greater than $s_2$ that is zero on every point of $Q$. Therefore $Q$ is not an anti-checker for all functions above the high threshold, even against the constant-zero circuit.

**Status.** PROVED BY COUNTING; an elementary obstruction to nonadaptive samples, not a new circuit lower bound.

**Proof.** There are exactly $2^{N-|Q|}\ge 2^{N-t}$ truth tables that are zero on $Q$. The number of truth tables computable by circuits of size at most $s_2$ is at most $2^{O(s_2\log(n+s_2))}=2^{O(n2^{\beta n})}$, by encoding a circuit gate by gate. Because fixed $\beta<1/10$, both $t=2^{10\beta n}$ and $n2^{\beta n}$ are $o(2^n)=o(N)$. Hence $N-t>O(n2^{\beta n})$ for sufficiently large $n$, so more zero-on-$Q$ functions exist than there are low-circuit functions. At least one such $f$ has complexity greater than $s_2$, and the constant-zero circuit agrees with it on all of $Q$.

**Consequence for the active route.** OPS's anti-checker list cannot be a fixed set of sample points: the list must depend on the entire input truth table. The relevant unresolved object is therefore an adaptive selector circuit $A_{n,\beta}:\{0,1\}^N\to(\{0,1\}^n)^t$ such that every $f$ of complexity $>s_2$ is anti-checked by its output against every size-$s_1=s_2/(10n)$ circuit. OPS prove that $\mathrm{NP}\subseteq\mathrm{Circuit[poly]}$ yields such selectors of size $N^{1+O(\beta)}$. A lower bound excluding these selectors in the corresponding quantifier regime would be sufficient for separation; this lemma itself only rules out nonadaptive samples.

**Proof location / dependencies.** Elementary circuit counting. Compare OPS, [Hardness Magnification Near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Lemma 4.1 and Theorem 1.4.

**Generality audit.** This argument fixes $Q$ before $f$ is chosen. It says nothing about an adaptive circuit whose queried coordinates depend on all $N$ bits of $f$; that adaptive lower bound is the open step.
## C-16 Ã¢â‚¬â€ A valid anti-checker selector induces a descent to the high-threshold boundary

**Statement.** Fix a total map $A$ that, on every table $f$ with $CC(f)>s_2$, outputs a sample anti-checking every circuit of size at most $s_1$. Fix any circuit $D$ of size at most $s_1$. Starting from any $f_0$, repeatedly replace the bits at all queried locations $A(f_i)$ by the corresponding values of $D$. The process terminates after at most $N$ strict rounds at a table $f_*$ satisfying $CC(f_*)\le s_2$. Its Hamming distance from $f_0$ is exactly the number of distinct bits changed.

**Status.** PROVED ELEMENTARY DESCENT; no lower bound or separation follows.

**Proof.** Use $d_H(f_i,D)$ as a nonnegative integer potential. If $CC(f_i)>s_2$, the anti-checker property supplies a queried point at which $f_i$ disagrees with $D$, so replacing every queried bit by its $D$-value strictly decreases the potential. At most $N$ bits can be changed. The process therefore reaches $f_*$ where all queried labels agree with $D$. If $CC(f_*)>s_2$, the selector property would give a disagreement, contradiction. Since every updated coordinate is set to the fixed value $D(y)$ and is never changed away from it, the number of coordinates changed equals $d_H(f_0,f_*)$.

**Stronger-start estimate.** If $CC(f_0)>2s_2$, then $d_H(f_0,f_*)=\Omega(s_2/n)$: otherwise, starting from a circuit of size at most $s_2$ for $f_*$, patch each differing truth-table point with one $n$-bit minterm, obtaining a circuit for $f_0$ of size $s_2+O(d_H(f_0,f_*)n)<2s_2$.

**Failure point.** The endpoint may have any complexity up to $s_2$, including the entire promise gap; it need not be a low instance of size at most $s_1$. Moreover, one batch can change $t\gg s_2/n$ bits, so the stronger-start estimate gives no contradiction. Updating one mismatch per round forces many rounds but does not force the selector circuit itself to be large.

**Proof location / dependencies.** Direct descent using the selector guarantee and pointwise DNF patching. It is an adversarial audit of the self-reference idea in Idea 182.
## C-17 Ã¢â‚¬â€ Any valid adaptive selector needs a large range of query sets

**Statement.** In the OPS parameters, let $s_2=2^{\beta n}$, $t=2^{10\beta n}$, and $0<\beta<1/10$ be fixed. If a selector $A$ is valid for every $f$ with $CC(f)>s_2$, then the number $q$ of distinct query sets in its range must satisfy
$$
q\,t\ge N-\log_2 M_2,
$$
where $M_2=|\{f:CC(f)\le s_2\}|$. In particular, circuit counting gives $q\ge(1-o(1))N/t=(1-o(1))N^{1-10\beta}$.

**Status.** PROVED BY COUNTING; quantitative adaptation requirement, not a circuit-size lower bound.

**Proof.** Let $\mathcal R$ be the selector's range after removing repeated query locations from each output, and set $U=\bigcup_{S\in\mathcal R}S$. Then $|U|\le qt$. If $qt<N-\log_2M_2$, more than $M_2$ truth tables are zero on $U$, so at least one has circuit complexity greater than $s_2$. For this $f$, the output $A(f)$ is a subset of $U$ and every label there is zero. The constant-zero circuit agrees on the whole sample, contradicting validity. Thus $qt\ge N-\log_2M_2$. Since $\log_2M_2=O(s_2\log(n+s_2))=o(N)$ and $t=N^{10\beta}$, the asymptotic bound follows.

**Limitation.** Range size alone does not yield a circuit lower bound. A simple non-selector circuit can attain this range by making one query address a projection of $\lceil\log q\rceil$ truth-table input bits (choosing $q$ addresses) and making the other query points fixed outside that address set. This takes at most $O(tn)$ output wiring, far below $N^{1+\epsilon}$ here. It does not satisfy the anti-checker property; it shows that output diversity itself is cheap. The hard task is routing each high-complexity input to a sample that is actually valid for its labels.
**Proof location / dependencies.** C-15 and the standard circuit-counting bound. The explicit failure mode for turning range size into circuit size is included above.
## C-18 Ã¢â‚¬â€ Sparse hard tables force exponentially many anti-checker samples

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

**Limit.** The resulting polynomial-time exponent can be arbitrarily large and depends on the fixed decision procedure. It yields only polynomial-size selectors, not the near-linear $N^{1+O(\beta)}$ selectors that OPS obtain under $NP\subseteq P/poly$. This explains why Ã¢â‚¬Å“P=NP makes the witness findableÃ¢â‚¬Â does not itself contradict the magnification threshold.

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
A set $Q$ is an anti-checker for $f$ against $\mathcal C_s$ if and only if $Q\cup R$ is a transversal of the family $\{E_D:R\subseteq D^{-1}(1),\ D\in\mathcal C_s\}$, where Ã¢â‚¬Å“transversalÃ¢â‚¬Â means intersecting every member. More precisely, a list $Q$ anti-checks iff $Q\setminus R$ intersects each such $E_D$; circuits rejecting some point of $R$ are already caught by $R$.

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

**Statement.** With probability $1-o(1)$, $1_R$ has circuit complexity above $s_2$, no size-$s_1$ circuit agrees with it throughout $A$, and the maximum Hamming weight among points of $R$ is exactly $k$. Thus the selector Ã¢â‚¬Å“compute $k_R=\max_{x\in R}|x|$ and output $B_{k_R}$Ã¢â‚¬Â is valid on this distributional family, has output length at most $t$, and has circuit size $O(N\operatorname{poly}(n))$.

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

**Claim audited.** Otto Beseka Isong, Ã¢â‚¬Å“P vs. NP: A Loop-Theoretic Approach,Ã¢â‚¬Â written August 13 and posted to SSRN August 18, 2026 ([SSRN record](https://ssrn.com/abstract=7280038)).

**Evidence available.** The abstract describes internal Loop-theoretic complexity classes and says the separation follows under an Ã¢â‚¬Å“internal Loop-theoretic finite-transition capacity principleÃ¢â‚¬Â and Ã¢â‚¬Å“explicit Loop-to-complexity bridge axioms.Ã¢â‚¬Â Thus the abstract itself presents the classical implication as conditional on these principles/bridges; it does not state an assumption-free derivation from the standard Turing-machine definitions.

**Status.** NOT VERIFIED AS A CLASSICAL P-vs-NP PROOF; ABSTRACT-LEVEL AUDIT ONLY. The PDF endpoint returned a Cloudflare 403 in this environment, so the exact axiom types, proofs, and possible circularity of the bridge could not be checked. No theorem from the manuscript is used in the active route.

**Required next check if the paper becomes relevant.** Obtain the full text and expand every bridge axiom into ordinary definitions of polynomial-time verification, search, and simulation. In particular, prove that the internal archive-size/transition lower bound transfers with polynomial resource preservation to standard SAT instances and arbitrary deterministic algorithms. Until then, the argument is a conditional framework claim, not a classical separation.

## C-43 - Exact feasible-antichecker condition in the Extended Frege route

**Published statement audited.** Pich and Santhanam, Theorem 7 / informal Theorem 3, Ã¢â‚¬Å“Towards $P\ne NP$ from Extended Frege lower boundsÃ¢â‚¬Â ([arXiv HTML](https://arxiv.org/html/2312.08163v1), Section 3). For fixed $k\ge3$, suppose a polynomial-time function $F(1^n)$ outputs one of:

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

**Status.** PROVED REFORMULATION plus a standard potential calculation; no selector lower bound. It sharpens the active bottleneck from Ã¢â‚¬Å“find an anti-checkerÃ¢â‚¬Â to Ã¢â‚¬Å“construct a short transversal for the circuit disagreement hypergraph without enumerating or exactly counting its exponentially large version space.Ã¢â‚¬Â Any claim that this requires #P/counting remains a conjectural route diagnosis unless supported by a reduction.

## C-46 - Teaching-set literature matches the logarithmic query count but gives no circuit-selector bound

**Source.** Compton, Pabbaraju, and Zhivotovskiy, Ã¢â‚¬Å“Lower Bounds for Greedy Teaching Set ConstructionsÃ¢â‚¬Â (arXiv:2505.03223, submitted 2025-05-06), [arXiv HTML](https://arxiv.org/html/2505.03223).

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

**Audit / limit.** This shows the C-47 #P oracle is not essential to the *conditional construction*: approximate local scores suffice when NP has polynomial-size circuits. It does not give an unconditional selector, because the small circuits for the BPP\(^NP\) approximator are obtained from the assumption (NP\subseteq P/poly). It also does not show that every selector computes or approximates these scores. Thus it reconstructs a known direction of the OPS magnification argument and leaves O-1 untouched. Treat Ã¢â‚¬Å“score computation is necessaryÃ¢â‚¬Â as false unless a separate reduction proves it.

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

## C-58 Ã¢â‚¬â€ Local changes preserve a disjoint valid anti-checker

**Statement.** If $Q_0$ is valid for a table $g$ against every circuit in $\mathcal C_{s_1}$, then it remains valid for every $h$ satisfying $h|_{Q_0}=g|_{Q_0}$. In particular, arbitrary changes on a patch $P$ disjoint from $Q_0$ preserve $Q_0$ as a valid output.

**Proof.** For each low circuit $D$, validity gives a point $x\in Q_0$ with $D(x)\ne g(x)$. Since $h(x)=g(x)$, the same point witnesses $D(x)\ne h(x)$. This holds for every $D$.

**Use and scope.** It defeats local patch encodings whenever a common valid list for the unpatched base misses the payload region. It says nothing about modifications that invalidate every base list, nor does it lower-bound arbitrary selectors. PROVED; semantic statement over the full circuit class.

## C-59 Ã¢â‚¬â€ Patch-switch lemma for easy-decoding regions

**Statement.** Let $g$ be a Boolean function and let $D_i,D_j$ have circuit size at most $s_1$. If $E_{D_i}(g)\subseteq P_i$, $E_{D_j}(g)\subseteq P_j$, and $P_i\cap P_j=\varnothing$, then
$$CC(g)\le 2s_1+CC(\mathbf 1_{P_i})+O(1).$$

**Proof.** Output $D_j(x)$ on $P_i$ and $D_i(x)$ outside $P_i$. The first circuit is correct on $P_i$ because $D_j$ can err only on disjoint $P_j$; the second is correct off $P_i$. A mux costs constant additional gates once $\mathbf 1_{P_i}$ is computed.

**Consequence.** At the OPS ratio $s_2=cn s_1$, a table with $CC(g)>s_2$ cannot have this pair of low approximants when $P_i$ has polynomial-in-$n$ indicator complexity. Thus the natural reduction gadget in which each omitted source bit leaves a low-circuit approximation wrong only on that bit's easy-decoding block cannot encode a high table.

**Scope warning.** The condition that every *short* transversal meets a region $P$ does not imply that some disagreement set lies inside $P$. The hypergraph with edges $\{p,x_i\}$ for $t+1$ distinct $x_i$ has the short transversal $\{p\}$, every transversal of size at most $t$ meets $P=\{p\}$, and no edge is contained in $P$. Therefore C-59 rules out a specific localized-approximation gadget, not every all-valid-output reduction. PROVED; not an O-1 lower bound.

## C-60 Ã¢â‚¬â€ Kannan's theorem does not directly lower-bound the selector

**Statement.** For each fixed $k$, Kannan gives a (potentially $k$-dependent) language $L_k\in\Sigma_2^P\cap\Pi_2^P$ outside $\mathrm{SIZE}(n^k)$. A search reduction must map source input $x$ to a high table $f_x$ and have a decoder $B(x,Q,f_x|_Q)$ recover $L_k(x)$ for every valid selector output $Q$. With table blowup $N=m^{a_k}$, selector exponent $a_k(1+\epsilon)$, and generation/decoding circuit exponents $b_k,d_k$, the composed circuit exponent is at most $e_k=\max\{a_k(1+\epsilon),b_k,d_k\}$ up to lower-order factors. Contradiction requires $k>e_k$, as well as the high-table promise and all-output correctness.

**Status.** The theorem is established literature; no reduction meeting these conditions is known in this project. This is a failed direct transfer, not evidence against the selector lower bound itself. Reference: [Kannan 1982](https://doi.org/10.1016/S0019-9958(82)90382-5).

## C-61 Ã¢â‚¬â€ Mandatory regions must carry dual-margin mass

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

## C-62 Ã¢â‚¬â€ Opposite labels need dual-mass separation for output-only decoding

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

## C-63 Ã¢â‚¬â€ Exact agreement-fiber form of selector failure

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
## C-64 Ã¢â‚¬â€ A fixed adversarial circuit cannot force selector cost

Let D be one fixed table. The map S_D(f) that outputs the first address x with f(x)\ne D(x), whenever one exists, is computable by an O(N)-gate circuit: hardwire D's N truth-table bits, compare them with f, and use a priority tree to return the first differing address. For any f\ne D, this one query certifies disagreement with D.

More generally, for a fixed menu \(D_1,\ldots,D_m\), output one first-difference address for each D_j. This is an O(mN)-gate circuit and a list of m queries. Every table that differs from all menu members is anti-checked against the entire menu.

**Consequence.** An adversarial-completion proof cannot fix one low circuit, or a sufficiently small preselected menu, and infer an \(N^{1+\delta}\) lower bound from that alone. It must handle the full table-dependent family \(SIZE(s_1)\) simultaneously. This is a quantifier/architecture obstruction, not a selector upper bound for the circuit class.

**Status.** PROVED by direct priority encoding. It explains why the adversary D in C-63 must be chosen jointly with f after seeing the candidate S; no fixed-D argument is enough.
## C-65 Ã¢â‚¬â€ Exact beta quantifier for the selector route

For each arity n, let \(N=2^n\), \(s_1=2^{\beta n}/(cn)\), \(s_2=2^{\beta n}\), and \(t_n=2^{10\beta n}\), where c is the fixed OPS constant. Suppose there are constants \(\delta,\beta_0>0\) such that for every fixed \(0<\beta<\beta_0\) with \(\beta<1/10\), every selector family valid at all sufficiently large arities and with output budget \(t_n\) has size greater than \(N^{1+\delta}\) infinitely often. Then \(NP\not\subseteq P/poly\).

Here validity means: for all sufficiently large n, all f with \(CC(f)>s_2\), and all circuits D with \(CC(D)\le s_1\), there exists x in S_n(f) such that D(x) differs from f(x); also \(|S_n(f)|\le t_n\). This is exactly \(\forall f\,\forall D\,\exists x\).

**Proof.** Assume \(NP\subseteq P/poly\). By OPS Lemma 4.1, there is a constant \(k\) such that for every sufficiently small fixed \(\beta>0\) the anti-checker selector has size at most \(2^{n+k\beta n}=N^{1+k\beta}\) for every sufficiently large arity n. Choose a fixed \(\beta<\min(\beta_0,1/10,\delta/(2(k+1)))\), also below the OPS smallness threshold. Then the selector size is at most \(N^{1+\delta/2}\) for all large n, contradicting the assumed infinitely-often lower bound \(>N^{1+\delta}\). Since \(P\subseteq P/poly\), this also implies \(P\ne NP\).

**Quantifier warning.** A lower bound for only one fixed beta chosen before the unknown constant k is not sufficient by this argument. The robust interval of beta values lets the proof choose beta after k. No arithmetic-progression robustness is needed for this direct OPS contradiction: the conditional selector exists at every sufficiently large arity, so a lower bound on any infinite subsequence suffices.

**Status.** PROVED implication from the stated selector theorem and the published OPS anti-checker lemma. The selector lower-bound premise remains OPEN and is itself a major circuit lower bound.
## C-66 Ã¢â‚¬â€ Short-list selector lower bounds also suffice

Let \(C_0\) be a fixed constant large enough for C-48, and set \(K_n=\lceil C_0s_1\log_2(s_1+n+2)\rceil\), with the OPS parameters \(s_1=2^{\beta n}/(cn)\), \(s_2=2^{\beta n}\), and \(N=2^n\). Suppose there are \(\delta,\beta_0>0\) such that for every sufficiently small fixed \(\beta\in(0,\beta_0)\), every selector family valid for all sufficiently large arities and outputting at most \(K_n\) addresses has circuit size greater than \(N^{1+\delta}\) infinitely often. Then \(NP\not\subseteq P/poly\).

**Proof.** Assume \(NP\subseteq P/poly\). C-48 gives, for every sufficiently small fixed beta, a valid selector with list length at most \(K_n\) and circuit size \(N^{1+\kappa\beta}\) for some constant \(\kappa\) fixed by the assumed polynomial-circuit exponent. Choose beta in the lower-bound interval with \(\beta<\delta/(2(\kappa+1))\). The conditional selector then has size at most \(N^{1+\delta/2}\) for all large n, contradicting the assumed infinitely-often lower bound. Hence \(NP\not\subseteq P/poly\), and therefore \(P\ne NP\).

**Why this is a narrower target.** The published OPS budget is \(2^{10\beta n}\), while C-48's conditional construction needs only \(O(s_1\log(s_1+n))=N^{\beta+o(1)}\) queries. A lower bound for this shorter-output subclass is sufficient for separation and may be easier to attack. C-49 also gives every such trace relative distance \(\Omega(1/n^2)\) from size-\(s_1/2\) circuit traces. Neither advantage is yet a circuit-size lower bound. Also choose C0 large enough that alpha=ln(M1)/K_n<1/15; C-61 then still forces each region mandatory for every K_n-list to have dual mass greater than 1/4, so at most three pairwise-disjoint mandatory regions remain possible.

**Status.** PROVED conditional implication from C-48; OPEN short-list selector lower-bound premise. This is a distinct sufficient route from O-1 and is strictly more targeted than S-1's full OPS output budget.

## C-67 Ã¢â‚¬â€ Exact cyclic closure recurrence for a pair list

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

## C-68 Ã¢â‚¬â€ Clause form of the initial anchor predicates

For an endpoint \(E\subseteq U\), put \(S(E)=\{(k,b):U\cap\{z:z_k=b\}\subseteq E\}\). The endpoint's initial activation predicate is exactly
\[
a_E(w)=\bigvee_{(k,b)\in S(E)}[w_k=b].
\]
If \(E\ne U\), \(S(E)\) contains at most one polarity of each coordinate, since the two literal slices at a coordinate partition \(U\). Thus a q-pair closure system has 2q clause-valued anchor inputs and a fixed semantic containment network. This structural reduction does not bound the network or separate the promise.

**Status.** PROJECT-PROVED by direct set inclusion; see C-67 and the closure-game report.

## C-69 Ã¢â‚¬â€ State-aware remaining distance is one-pair-Lipschitz

For partial list \(Q\), define \(\delta_Q(w)=\min\{|R|:\mathcal C_{Q\cup R}(w)\ni\varnothing\}\). For a surviving anchor, \(0\le\delta_Q(w)\le N-1\), using the chain intersection of its N matching slices. If p is one additional pair, then
\[
0\le \delta_Q(w)-\delta_{Q\cup\{p\}}(w)\le1.
\]
Monotonicity proves the left inequality. For the right inequality, any extension R that kills after \(Q\cup\{p\}\) can be replayed after Q by adding p first, so \(\delta_Q(w)\le1+\delta_{Q\cup\{p\}}(w)\).

**Status.** PROJECT-PROVED. The missing step is a useful bound on the marginal decrease aggregated over anchors; C-09 rules out a naive per-rule anchor-incidence bound.

At \(Q=\varnothing\), C-03 gives \(\delta_{\varnothing}(w)\ge N-\log_2M_2-1=N-o(N)\) for every low anchor. A fixed distribution \(\mu\) with uniformly tiny one-pair expected decrease would have yielded a superlinear lower bound by telescoping, but C-73 refutes that condition already at \(Q=\varnothing\). The distance remains valid; the additive static-potential strategy is closed.

## C-70 Ã¢â‚¬â€ Fixed-family fractional rounding is conditional, not global

Suppose a specified family \(\mathcal H\) of R semi-filters has fractional pair-cover weights of total W, with violation weight at least 1 for every \(F\in\mathcal H\). Sampling \(k=\lceil W(\ln R+1)\rceil\) independent pairs from the normalized weights covers every member of \(\mathcal H\) with positive probability by a union bound; hence an integral cover of size \(O(W\log(R+1))\) exists. If the project ceiling \(W\le8N+1\) applies to that fractional cover, this gives \(O(N\log(R+1))\).

**Status.** PROJECT-PROVED conditional rounding. The \(8N+1\) fractional ceiling is supplied by the prior project record, but its original proof location is not yet pinned in this ledger.

**Scope warning.** This only covers the specified \(\mathcal H\). The global cover problem quantifies over every semi-filter extension of every anchor. A pair that changes a current least closure may merely add a nonempty consequence; it need not derive empty. Therefore a fixed family or one selected filter per anchor does not establish a global \(\rho\) upper bound.

## C-71 Ã¢â‚¬â€ Finite-state recurrence cross-check

**Test.** On \(U=\{1,\ldots,6\}\subset\{0,1\}^3\), with anchors \(000\) and \(111\), the script experiment_fusion_closure_recurrence.py compares the explicit family-of-subsets closure to recurrence C-67 for all 2,080 one-rule pairs and 100,000 seeded two-rule lists at both anchors. It checks no empty-consequence rule activates from literal seeds alone and that the known two-pair list derives empty for both anchors.

**Result.** All 204,160 explicit-closure/fixed-point comparisons passed; every run stabilized within q strict rounds. In addition, for both anchors a selected two-literal intersection saves one rule in the local certificate, matching C-73's sharing mechanism.

**Status and scope.** TESTED finite model only. This is an implementation cross-check of C-67, not evidence for an asymptotic lower or upper bound.

## C-72 Ã¢â‚¬â€ Empty consequences need a nonempty bootstrap

Assume \(U\) contains a high-complexity table in every two-coordinate cylinder. For any empty-consequence rule \(T_i=E_i\cap H_i=\varnothing\) and low anchor w, its two initial seed predicates cannot both hold. If \(L_{w,k}\subseteq E_i\) and \(L_{w,\ell}\subseteq H_i\) with \(k\ne\ell\), two-wise shattering gives a table in their intersection, contradicting \(E_i\cap H_i=\varnothing\). If \(k=\ell\), the matching slice itself would be a nonempty subset of both endpoints. Therefore no empty rule activates in the first round from literal slices alone.

At OPS parameters the shattering hypothesis follows from \(M_2<2^{N-2}\): each two-coordinate cylinder has \(2^{N-2}\) truth tables, while only \(M_2=2^{o(N)}\) tables have circuit complexity at most \(s_2=N^\beta\), for fixed \(\beta<1\) and large n.

**Depth consequence.** A round-t contradiction proof unfolds to a binary AND/OR tree with at most \(2^t\) matching-literal leaves. Their intersection must be empty in U, so at least \(N-\log_2M_2\) distinct coordinates are fixed. Hence \(t\ge\log_2(N-\log_2M_2)=\log_2N-o(\log N)\).

**Status and scope.** PROJECT-PROVED under the stated two-wise-shattering/counting condition. This is a proof-depth lower bound, not a superlinear pair-count bound; a proof may have logarithmic depth and \(N-o(N)\) total rules.

## C-73 Ã¢â‚¬â€ No static anchor weighting makes the first shared pair negligible

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


### C-77 Ã¢â‚¬â€ Exact cyclic-complexity identity and DAG conversion audit

For the distinct full-domain exact low-set cover, a successful q-pair list induces a monotone least-fixed-point network on signed truth-table literals with q AND/intersection states and output exactly 1_Y; every non-low table has a principal semi-filter preserving every pair. CavalarÃ¢â‚¬â€œOliveira give \(\rho_{\rm full}=D^\circ_\cap(Y\mid\mathcal B_{\rm full})\) and \(D_\cap\le(D^\circ_\cap)^2\). The active project target is instead the promise-domain \(\rho_{\rm prom}\) on \(Y\sqcup Z\), whose output is 1 on Y and 0 on Z with medium values unconstrained; C-90 gives the exact ambient distinction and \(\rho_{\rm prom}\le\rho_{\rm full}\). For either chosen domain, q pairs imply at most qÃ‚Â² acyclic AND gates, and the generic binary rect-DAG conversion costs O(qÃ‚Â³). Sourced model comparison and proofs: [DAG/Fusion bridge audit](DAG_FUSION_BRIDGE_2026-09-26.md), [CavalarÃ¢â‚¬â€œOliveira](https://arxiv.org/abs/2503.14117), [Sokolov](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download), [GargÃ¢â‚¬â€œGÃƒÂ¶ÃƒÂ¶sÃ¢â‚¬â€œKamathÃ¢â‚¬â€œSokolov](https://jakobnordstrom.se/docs/publications/GGKS18_MonotoneCircuitLBsResolution.pdf). Status: proved reformulation and conversion bounds; target lower bound open.

## C-78 Ã¢â‚¬â€ Formal C-75 relation and shared-DAG conversions

The ordinary mismatch relation has inputs (w\in Y,z\in Z), Alice knows (w) (or a circuit description (d) with (G(d)=w)), Bob knows (z), and the output is ((k,b)) with (w_k=b\ne z_k). It is total. Sending a size-(s_1) circuit description gives deterministic communication (O(s_1\log(n+s_1)+\log N)) bits, but only the generic (2^{O(c)}) protocol-tree/rect-DAG size from a (c)-bit protocol.

For a successful pair list (Q), the stronger witness relation outputs a ranked sequence of rule-side supports ending at a signed mismatch. It is total exactly when (Q) activates an empty consequence on every low anchor; direct routing uses (O(q\log(q+N))) bits. Standard Sokolov Boolean games and GGKS rectangle-DAGs are acyclic, binary-cover models. The fusion state graph can contain cycles; activation rank is input-dependent. Explicit rank unrolling yields a standard rect-DAG of size (O(q^2(q+N))=O(q^3)), while the acyclic AND-only conversion is at most (q^2). A Tier-1 target (q>N^{1+\epsilon}) would therefore require rect-DAG size (>N^{3+3\epsilon}), or an AND-only separator bound (>N^{2+2\epsilon}).

A pattern-sharing universal mismatch DAG was constructed with size (O(m+\sum_{I\ dyadic}\pi_I(Y))), where (m=|Y|) and (pi_I(Y)) counts distinct low-table restrictions to interval (I). This is an upper bound for one protocol, not a lower bound or near-linear construction at the OPS parameters. Parity and counting-selected hard Boolean functions separately show that communication bits can be small relative to DAG size, while a node-count tree can never be smaller than its DAG.

**Status.** Model comparison and the stated conversions are proved; no non-shareability lower bound is established. Detailed construction and literature scope: [DAG/Fusion bridge audit](DAG_FUSION_BRIDGE_2026-09-26.md), section 9.

## C-79 Ã¢â‚¬â€ Medium-band filter defeats direct promised-cover reuse

For sufficiently small fixed OPS ÃŽÂ², every signed truth-table coordinate cylinder contains a function of circuit complexity in ((s_1,s_2]). Proof: choose (k) with (2^k\in[s_2/32,s_2/16]); a shared prefix decoder plus an OR of selected minterms computes all (2^{2^k}) functions of (k) variables in at most (s_2) gates. For either prescribed output bit at any input, half of these functions lie in that cylinder. Their count exceeds the standard upper bound (2^{C_0s_1\log(n+s_1+2)}=2^{(C_0\beta/c+o(1))s_2}) on low tables when ÃŽÂ² is sufficiently small.

Let (M=\mathrm{SIZE}(s_2)\setminus\mathrm{SIZE}(s_1)), (Z=\mathrm{SIZE}(s_2)^c), and (U_Y=M\cup Z). For any (w\in Y), the upward closure over (U_Y) generated by (M) and all matching literal slices (L_{k,w_k}\cap U_Y) is a semi-filter above (w). Each such slice intersects (M). Therefore no endpoint (E\subseteq Z) contains a generator, so (E\notin\mathcal F_w); every pair with both endpoints in (Z) is preserved vacuously. Thus no pair list whose endpoints all live in (Z), including a cover designed for the larger positive class \(\mathrm{SIZE}(s_2)\), can be reused directly as a cover for (Y).

**Scope.** This blocks direct endpoint reuse and a naive monotonicity argument for the promise-to-exact reverse transformation. It does not exclude a transformation that adds medium-band pairs, and it gives no new asymptotic lower bound for ÃÂ. Full proof: [DAG/Fusion bridge audit](DAG_FUSION_BRIDGE_2026-09-26.md), section 10.

## C-80 Ã¢â‚¬â€ A large structured low subfamily has a linear-size mismatch DAG

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

## C-90 Ã¢â‚¬â€ Promise-domain reverse conversion and ambient-universe monotonicity

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

Fix \(\beta<1/2\), and take the C-80 block-constant low family with \(m=\Theta(s_1)\) blocks of size \(B=N/m=\Theta(nN^{1-\beta})\). Circuit counting gives a mask p on the within-block inputs for which both p and its complement have circuit complexity \(>s_2+O(k)\), since \(2^B\) exceeds the \(2^{O(s_2 n)}\) small-circuit count. Let P be the coordinates where p=1 and J its complement. For block codewords a,b, splice \(z_{a,b}=w_b\) on P and \(w_a\) on J. If aâ‰ b, restriction to a differing block is p or its complement, so \(z_{a,b}\in Z\); while \(w_a\in Y\), \(w_a|_J=z_{a,b}|_J\), and \(z_{a,b}|_P=w_b|_P\).

Thus every pair of distinct P-pattern contexts has a low/high cross-pair that agrees throughout J. A rect-DAG suffix-only continuation cannot merge any two such contexts, because its product rectangle would contain that invalid cross-pair. A prefix-first router that records the exact P-pattern and then outputs only in J needs \(2^m=2^{\Theta(s_1)}\) continuation states.

**Status and limit.** PROVED for the specified prefix-first/suffix-only submodel, on actual Gap-MCSP low/high inputs. C-80's O(N) adaptive mixed-block DAG handles the same structured low family, so this is not a general rect-DAG lower bound. It does not improve \(\rho\), q, or the q-to-DAG conversion. It strengthens O-98 by replacing the arbitrary-string example with promise-realized cross-pairs.


## C-112 - A separated low code has a split with all cross-splices high

For \(\mathcal C\subseteq\{0,1\}^N\) of size K and minimum distance d, if \(d>2\log K+\log |\mathrm{SIZE}(s_2)|\), a uniform random coordinate subset P gives, for each ordered aâ‰ b, a uniformly random splice among \(2^{d(a,b)}\) completions of their common restriction. At most \(|\mathrm{SIZE}(s_2)|\) are low/medium. Union-bounding over fewer than K^2 pairs proves there is one split P for which every off-diagonal splice is high.

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
**C-123 â€” Descriptor invariance and the universal-DAG barrier.** For any surjection from circuit descriptions D onto the low truth-table set Y, the minimum rect-DAG size for mismatch on DÃ—Z equals that on YÃ—Z: lift Alice-side state predicates by preimage, and reverse by restricting to a section. The same size is Î˜(C_sep), where C_sep is the Boolean circuit size of any separator h with h(Y)=1 and h(Z)=0. Directly OR-ing one exact-table test per description gives an explicit O(NÂ·2^ell) separator/DAG for ell=O(s1 log(s1+n)); this is exponential in description length. A universal evaluator for one supplied description does not implement the existential projection defining Y. This kills the syntax-only shortcut and binary-search construction, not all small DAGs; no lower bound on C_sep or rho follows.
**C-124 â€” Adjacent MCSP literature does not transfer automatically.** The 2026 conditional NP-hardness result for Gap-ImpMCSP takes succinct sampler circuits as inputs; the project separator takes explicit N-bit tables, and no polynomial-size composition from the former to the latter is known. Austrin-Risse's SoS degree lower bound is per fixed hard table, whereas the needed object is one separator for all low/high tables. Neither result implies a bound on S_rect or rho_prom. See C-124.

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

Let Y={(0,1,1,0),(1,0,1,0)} and Z={zA=(0,1,0,0), zB=(1,0,0,0), zC=(1,1,1,1), p1=(1,1,0,1), p2=(1,1,0,0)} over coordinates (a,b,c,f). Use pair endpoints E1={zA,p1,p2}, H1={zC,p1}; E2={zB,p1,p2}, H2={zC,p2}; E0={p1}, H0={p2}. Then T1={p1}, T2={p2}, T0=empty. On U=Z, the literal slices are a0={zA}, b0={zB}, c1={zC}, f1={zC,p1}, with complements as listed in bridge Â§69. The seed sets are E1:a0, E2:b0, H1:c1/f1, H2:c1, and no seed is contained in E0 or H0. The non-self support graph contains 1<->2 on E sides and the two root edges 1->0, 2->0.

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

The CCC 2025 colourful-sunflower lifting theorem gives a rect-DAG lower bound of (m/(A|Sigma|w(S)log(mn)))^w(S) for Index-lifted search Sâˆ˜Ind_m^n, where w(S) is subcube-DAG width. To use it here requires partywise maps from lifted inputs to low/high truth tables and an output-preserving decoder taking every mismatch leaf to a constraint falsified throughout its source rectangle; table length and circuit-class cardinalities must also fit. No such map is known. The result is a concrete lead and a template, not a Gap-MCSP or P-vs-NP lower bound. Any transfer must clear the current cubic/log compiler threshold L/r>N^(3+3epsilon)/log N or reach rho_prom directly.

## C-155 RETRACTED - The partial-Index no-go imposed constraints off-domain

The proof wrongly required a(x)=b(y) whenever y_x=0. In SearchORâˆ˜Index, those pairs have no valid output and lie outside the partial relation's domain, so a reduction need not satisfy anything there. On the legal domain y_x=1, the code a(x)=0^m, b(y)=y works: coordinate x mismatches, and every mismatch coordinate can decode to the sole output 1. Thus the claimed direct-encoding impossibility is false. The error is a quantifier/domain mistake, not a subtle gap. In the CCC CSP application the base unsatisfiable-CSP search is total; a corrected argument must use valid outputs on every lifted input pair.

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

For a surjection G:D→Y from low-circuit descriptions to distinct low truth tables, the minimum standard mismatch rect-DAG size on D×Z equals that on Y×Z: lift row rectangles by G^{-1}, and restrict a description-DAG along any section Y→D. Thus short syntactic descriptions alone provide no shared-state compression. The best generic description protocol still has exponential-in-communication tree size; the universal joint mismatch predicate is nonrectangular.

The ordered bases in GL(n,2) number 2^{n²+O(1)}, but their component rows range over only the N linear functions. For each basis A and combiner g, g(Ax) costs size(g)+O(n²), so the compositions that fit the s1 budget are already rows of Y. Exact affine membership is testable by Walsh–Hadamard transform in O(N log²N), giving a near-linear mismatch DAG for Aff_n×Z. No obstruction across nonlinear g-composition families follows.

Model/conversion result reaffirmed: q=ρ_prom=D°_cap; q yields a ranked cyclic router and S_rect≤O(q³/log q), while an L-node standard mismatch DAG gives ρ_prom≤O(L). Thresholds remain q direct >N^(1+ε), AND-only >N^(2+2ε), or standard rect-DAG >N^(3+3ε)/log N. This is a precise reformulation/falsification checkpoint only; no new lower bound or P-vs-NP result.

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
If every low restriction s on I has a high extension z_s in Z, then distinct restriction states cannot merge while their descendants are required to output a mismatch inside I: z_s lies in B_r for r!=s, so the product hull contains (w_s,z_s) for w_s|I=s, a pair agreeing throughout I. Counting gives the extension premise whenever 2^(N-|I|)>|SIZE(s2)|. Also, O(Ln) point-indicator circuits realize all 2^L patterns on any L selected positions when L n<=s1/O(1). Hence interval-local scanners need 2^L contexts per such interval. This is a rigorous scanner-specific non-shareability theorem. It does not lower-bound arbitrary rect-DAGs because a DAG may change coordinates or solve cross-pairs outside I; the needed normalization is open. See bridge §92.
## C-167 - C-160 refutes generic interval normalization

For the C-160 promise Y_a={x:|x|<=a or |x|>=N-a}, Z_b={z:b<|z|<N-b}, with a=floor(N^beta/n), b=floor(N^beta), every pattern on an interval I of length L<=a extends both to a low row (fill the complement with zeros) and to a high column (fill to weight floor(N/2)). The interval-local router therefore has 2^L pairwise nonmergeable restriction contexts: merging r and s puts a cross-pair (w_s,z_s) in the product hull that agrees on I. At L=a its size is at least 2^a. Yet the promise has an O(N log N) threshold separator and therefore an O(N log N) arbitrary rect-DAG. Thus no promise-independent normalization to interval-local routers can have polynomial size loss. This only refutes the generic O-127 route; an OPS-specific normalization and every actual Gap-MCSP lower bound remain open. See bridge C-167.
## C-168 - Alice-only coordinate selection requires N-o(N) positions

For any fixed low table w and any candidate mismatch set S(w) chosen from w (or from a circuit description of w) alone, if every z in Z={0,1}^N minus SIZE(s2) must disagree with w somewhere in S(w), then all 2^(N-|S(w)|) completions matching w on S(w) lie in SIZE(s2). Hence |S(w)|>=N-log2|SIZE(s2)|=N-o(N) in the OPS range. This extends fixed-coordinate cylinder counting to row-dependent but nonadaptive samples. It does not constrain Bob-dependent adaptive rectangle-DAG routing or imply a graph-size lower bound. See bridge C-168.

## C-170 - One-switch protocols need exponentially many frontier states

For a fixed-order one-switch mismatch DAG, if Alice sends first, a message class A must have a common bit pattern on every coordinate that Bob's suffix can output. Correctness for all high z forces these coordinates to number at least N-log2|SIZE(s2)|, so A has Hamming diameter at most log2|SIZE(s2)|. The C-80 block-constant low code has 2^Theta(s1) rows at distance Theta(N/s1), exceeding this diameter for fixed beta<1/2. Hence there are at least 2^Theta(s1) Alice frontier states.

If Bob sends first, each message class B subset Z must be constant on an output-coordinate set S whose pattern is avoided by every low row. Point-indicator circuits realize every pattern on at most t=floor(s1/(C n)) coordinates, so |S|>t. Each B is therefore contained in a cylinder of size at most 2^(N-t-1), forcing at least (1-o(1))2^(t+1)=2^Omega(s1/n) Bob frontier states to cover Z. These bounds allow arbitrary shared suffix DAGs but assume no return to the sender after the switch. Repeatedly alternating rect-DAGs are not bounded; no rho_prom or P-vs-NP consequence follows. See bridge §96.

## C-171 - A fixed menu of low-fiber crossing pairs is nearly quadratic

Define Fib(w,z) to output {i,j} with w_i=w_j and z_i!=z_j. It is total on Y x Z because otherwise z is a unary function of w and has circuit size at most s1+O(1). For a fixed candidate-label graph G on table coordinates, retain edges whose endpoints have equal w-bit. If z is constant on the components of this retained graph, no menu edge is valid. Since the menu must work for every high z, the 2^c component-constant tables must all lie in SIZE(s2), so c<=ell=log|SIZE(s2)|.

For every affine flat H of size m with 2ell<=m<4ell, the table 1_H is in SIZE(s1) for large n. The retained graph contains G[H], whose component count is at least m-e_G(H); hence every such flat must span at least m-ell edges of G. A random affine flat contains any fixed edge with probability m(m-1)/(N(N-1)), giving
|E(G)| >= (m-ell)N(N-1)/(m(m-1)) = Omega(N^2/ell) = Omega(N^(2-beta)/n).
Any rect-DAG for Fib has at least this many distinct output labels.

This is not a C-75 lower bound. Fib leaves refine to a signed mismatch with O(1) extra states, but the reverse construction from mismatch needs up to O(N^2) state copies to remember three output labels; the resulting inequality is too lossy. C-171 closes only the nonadaptive fixed-pair-menu shortcut and records a precise transfer failure. See bridge §97.

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

One-hot dual-rail encodings put every N-bit table at Hamming weight N, so distinct low/high encodings are incomparable. Assigning 1 to encoded low tables and 0 to encoded high tables gives a monotone-consistent partial Boolean function. Its monotone KW outputs are exactly signed mismatches. Thus a C-75 rect-DAG is the restricted partial monotone KW DAG. If a lifted CSP search relation reduces answer-preservingly to C-75, inverse images of rectangles give a same-size DAG and the CCC 2025 colourful-sunflower lower bound transfers without size loss. No such reduction is known; the high-table requirement on every Bob image and validity of every mismatch output are the unresolved conditions. Any affine-coset low/high subpromise is easy: a separating parity check gives an O(N)-gate separator. Status: precise route interface and route filter only; no new S_rect, rho, or P-vs-NP lower bound. Details and source: bridge §123.



## C-199 - Dense Bob-column deletion preserves triangle-DAG lifting up to constants

For Search(F) composed with IND_m^r, take any Bob subset B with omitted density eta<1/4. The proof of the 2024 triangle-DAG lifting theorem adapts by initializing the accumulated error-column set with B^c. After deleting whole columns and earlier error rows/columns, states remain triangles; on retained columns the restricted protocol still covers each parent and its leaves are correct. The Triangle Lemma's per-state bounds are unchanged. With protocol-size constant 1/4 in place of 1/2, accumulated protocol error is <1/4, so together with eta<1/4 at least half the root columns remain and the source Full Image Lemma applies. Thus the same width-w resolution consequence holds with only a constant-factor lower-bound loss.

For the OPS promise, |SIZE(s2)|/2^N=2^(-N+o(N)); hence the high-table column set is dense enough. This removes the requirement that a reduction explicitly generate only high tables. It does not solve the answer-preserving map: every oriented mismatch must be a valid lifted-search output, and the low-table family must not have a simple linear-size membership test. A blockwise pointer encoding fails because its range is recognized in O(N) gates. Status: proved proof adaptation / route filter only; no C-75 lower bound. Details: bridge §124; primary source ECCC 2024 Report 185, Theorem 2.11.



## C-200 - The standard colourful-sunflower image family has a near-linear separator
In the CCC 2025 cPHP-to-clique-colouring reduction, Alice's graph is exactly one k-clique on one selected vertex in each of k parts, with every other edge absent. For an adjacency table on V=mk vertices (N=binom(V,2) input bits), a Boolean circuit computes all degrees and accepts iff exactly one vertex per part has degree k-1 and every other vertex has degree 0. The active vertices then form a k-clique. This costs O(V^2 log V)=O(N log N) gates. It accepts every Alice image and rejects every c-colourable Bob graph; restricting Bob graphs further to high-circuit-complexity tables does not change that. Hence the signed-mismatch subrelation on these images has an O(N logN) rect-DAG, below the project threshold. In addition, the mKW reduction decodes only Alice-present/Bob-absent edges, whereas signed mismatch also permits the reverse orientation. The unmodified reduction cannot transfer a C-75 lower bound. Status: this concrete lifting image route is closed; no target lower bound follows. Details: bridge §125.

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

This is not a rect-DAG or fusion cover. “Q contains a mismatch” is generally not a rectangle (two-bit off-diagonal witness), and the sample index cannot be selected by a single product state. A scan confined to one sample that discards its tested prefix is blocked by product-hull cross-pairs; a composite protocol using other samples or revisiting old coordinates is not ruled out. Thus this kills no general DAG and gives no lower bound; it identifies routing/selection, not output-support, as the remaining issue. See bridge C-211/O-141.


## C-212 - Sparse interpolation and upgraded local bounds

**Status:** proved. For every r-point subset of the n-bit address cube, shared block decoders give an exact indicator circuit of size `O(n+r*n/log(r+1))`. Therefore the low class shatters every fixed set of `Theta(s1)` table coordinates, and sparse patching raises the OPS low/high Hamming gap to `Omega(s2)`. This supersedes the weaker point-minterm quantitative bounds in C-133, C-135 through C-137, C-170, C-172, C-189, C-191, C-195, and C-211 where applicable. The proof assumes the project's standard fan-in-two Boolean basis with free fan-out and fixed `0<beta<1`.

**Limit:** the stronger numbers still concern fixed-order/one-switch architectures, local certificates/routers, or rectangle covers constrained to an equality/triangle state. Product-hull-safe global aggregation is open. No arbitrary rect-DAG, fusion-cover, or P-vs-NP bound follows. See bridge C-212.


## C-213 - Universal cyclic rectangle scan; fusion transfer fails

**Status:** proved model counterexample. For every disjoint `A,B subseteq {0,1}^N`, a cyclic product-rectangle protocol with N scan states, 2N one-bit selector states, and 2N output leaves solves mismatch in at most N scan steps from any scan state, under the specified strategy. The cycle revisits old coordinates and makes the full product hull of merged equal-prefix histories safe.

**Boundary:** the protocol is not acyclic and its party-local rectangle predicates are independent/free. A fusion rule instead generates a one-input activation set via the endpoint/support least-fixed-point equations; no small conversion from the cyclic scan to legal fusion pairs is known. Thus C-213 kills the broad cyclic-rectangle lower-bound target only. It does not give a small standard rect-DAG, a bound on `rho_prom`, or a P-vs-NP result. See bridge C-213; retain C-80/C-160 and O-141.

## C-214 — Exponential generic separation by counting native closure descriptions

For each q-rule fusion closure on an N-bit full-partition promise, the anchor recurrence is specified by two seed-literal subsets from a 2N-literal vocabulary per rule, two predecessor subsets of [q] per rule, and the empty-output subset. Thus at most 2^(4Nq+2q^2+q) Boolean functions are computed by q-rule systems. Counting over q<=2^(N/2-1) yields fewer than 2^(2^N) functions for large N. Therefore some Boolean partition has fusion-pair complexity Omega(2^(N/2)); its signed-mismatch relation nevertheless has the universal 5N-state cyclic rectangle protocol of C-213. This proves that arbitrary cyclic rectangle protocols do not admit a generic polynomial-overhead conversion to fusion closure.

**Limit:** the counted partition is existential and need not equal the actual SIZE(s1)/SIZE(s2)^c promise. The middle band of the actual promise leaves separator values unconstrained. No C-75, OPS, or P-vs-NP lower bound follows. Full proof: research/C75_SHARED_DAG_CONTINUATION_2026-09-27.md.

## C-215 - Q-exit overlap graph: proved local condition, unproved aggregation

**Status:** local lemma proved; global use not proved. At a rect-DAG state v, join low Q-signature sigma to high signature tau when their projections on the descendant tail-output set T_v overlap. Let P_v be the descendant Q-output set. Every such edge satisfies sigma|P_v != tau|P_v; otherwise a row and column witness agree on all descendant outputs. In particular, no diagonal edge is possible, and a complete bipartite overlap subgraph has disjoint P_v-projections on its two sides.

At the root, if fewer than N-|Q|-log2(M2) tail coordinates occur below the root, then fixing a low row's Q-signature and its values on those tail coordinates leaves more than M2 completions; one is high, creating a forbidden diagonal edge. Hence the root must expose at least N-|Q|-log2(M2) tail coordinates. A fixed overlap witness pair persists to the child it enters while it remains in the child's rectangle, but edge count is not monotone because tail support shrinks and row/column sides are filtered. No parent-conditioned flow or state lower bound follows. See research/C215_Q_EXIT_GRAPH_AUDIT_2026-09-27.md; O-141 stays open.

### C-216 — Statewise signature/column-deficit profile

**Status:** proved local inequality; aggregation fails. For each rect-DAG state `v`, let `r_v` count Q-signatures present on both sides, `t_v` be descendant tail-output support, and `Delta_v` be omitted high columns. Disjoint cylinders give `r_v*2^(N-|Q|-t_v)<=M2+Delta_v`. At the root this strengthens support by `log r_Q`; Alice transitions duplicate the deficit allowance and Bob transitions add `|Z|`, preventing a useful scalar global charge. This is not a superlinear DAG bound. See `research/C216_COLUMN_DEFICIT_PROFILE_2026-09-27.md`.

### C-217 — Fixed-order mismatch scans require exponential width

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

Let C have size r and approximate a low table w on all but e addresses. Select k internal wire values from C, including its output, as a signature. For a high table z, let m count good addresses that disagree with the per-cell majority of z. A lookup on the signature followed by point-minterm corrections computes z with size `r+O(k*2^k+(e+m)n)`. Hence if `CC(z)>=s2`, then `r+O(k*2^k+(e+m)n)>=s2`; the precise forced mass is on the residual scale `(s2-r-c1*k*2^k)/(c2*n)`, and is `Omega(s2/n)` when `r+c1*k*2^k<=s2/2`. A mixed good cell contains x,y with same signature, w(x)=w(y), and z(x)≠z(y). This is a robust local extension of C-115, not a global DAG charge. Natural-property learning does not currently improve the C-75 route: the separator family is nonuniform absent a uniform constructor, and the cited theorem returns approximate learners rather than shared DAGs. O-141 and all transfer losses remain unchanged. Proof and scope: `research/C224_APPROXIMATE_FIBERS_NATURAL_PROPERTY_BOUNDARY_2026-09-27.md`.

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

## C-232 — Same-alphabet communication/DAG separation; OPS transfer remains open

For an arbitrary Boolean function `f` on N-bit inputs, its KW mismatch relation has N output labels and an `O(N)`-bit protocol (Alice sends her input). Circuit counting gives a function with circuit size `Omega(2^N/N)`, and Sokolov's DAG/KW theorem transfers this to rect-DAG size. This is a generic counterexample to “short communication or small output alphabet implies a small shared DAG.” It does not transfer to the fixed Gap-MCSP promise. For that promise, `S_rect=Theta(C_sep)` and truth-table versus circuit-description input representations have equal minimum DAG size. The direct separator `OR_d AND_k[w_k=G(d)_k]` costs `N*2^(O(s1 log(n+s1)))`; universal evaluation alone does not remove the existential over d. The `2N` mismatch rectangles form a small cover, but arbitrary unions in that cover cannot be binary-expanded unless every intermediate set is a rectangle. Quantitative chain remains `rho_prom<=O(S_rect)` and `S_rect<=O(rho_prom^3/log rho_prom)`; forcing `rho_prom>N^(1+epsilon)` through the latter requires `S_rect>cN^(3+3epsilon)/logN`. Status: model-level calibration proved; no actual-promise superlinear bound or P-vs-NP proof. Full note: C-232.

**C-233 (proved operational lemma; no P-vs-NP consequence).** For the q-rule least closure `x_i=(a_i OR OR_{j∈P_i}x_j) AND (b_i OR OR_{j∈R_i}x_j)`, first-activation ranks are the least solution of `tau_i=1+max(min({0 if a_i}∪{tau_j:j∈P_i}), min({0 if b_i}∪{tau_j:j∈R_i}))`, with infinity when either side has no finite support. A min-priority worklist finalizes exact ranks in nondecreasing order because every candidate is one plus both supporting ranks; each rule is finalized once and each support incidence processed once. With `E<=2q^2`, seed evaluation costs `O(qN)`, yielding `O(qN+(q+E)log q)` word-RAM operations. The closure has a direct `O(qN+E)=O(q^2)`-gate TSC partial recognizer, outputting 1 on Y and Z on high tables, and a total TSC separator of size `q^2 polylog q` via RAM simulation. Neither bound implies a standard Boolean circuit/rect-DAG of that size; RAM/TSC-to-acyclic conversion is unresolved. A partial-TSC lower bound `>N^(2+2epsilon+delta)` would imply `q>N^(1+epsilon)`, but none is established. See `research/C233_MINMAX_ACTIVATION_RANK_AND_TRISTATE_RAM_BRIDGE_2026-09-27.md`.
## C-234 - Conditional blockwise substitution theorem

**Proved conditionally.** Let D be the family of all k-bit Boolean functions, repeat each g in D across r=N/2^k address-prefix blocks, and choose k so every g has circuit size at most s1/4 and 2^k=Theta(s2). All diagonal tables lie in SIZE(s1); independent block hybrids range over all 2^N tables. If a selected accepting proof for each diagonal table has pairwise-disjoint state occurrences isolating each block from its outside context, then state-label pigeonholing plus repeated valid substitution yields at least (|D|/(2rq))^r accepted hybrids. Circuit counting forces q>=2^(Omega(s2)) at OPS scales.

**Not proved for arbitrary covers.** Block isolation is not automatic. The diagonal-only subpromise has an O(N) Boolean separator and therefore an O(N)-pair fusion cover, proving that no choice of one accepting proof per anchor can satisfy the isolation hypothesis for every anchor simultaneously. The missing theorem is a quantitative charge for the resulting nonlocal/interleaved proof structure or an alternative compatibility theorem. No full-promise superlinear fusion lower bound follows. Full proof: research/C234_BLOCK_REPLICATION_AND_CONDITIONAL_SPLICE_AMPLIFICATION_2026-09-27.md.
**C-234 exact fingerprint refinement.** For diagonal anchors w_g(p,u)=g(u), context K from w_g and replacement support C from w_h are compatible iff g and h agree on every suffix u represented by at least one coordinate in dom(K) intersect dom(C). The overlap is a partial truth-table fingerprint; a full fingerprint prevents cross-description splicing. For differing u outside the fingerprint, the copies across prefix blocks are assigned to K, C, or left free; constant-side ownership has a low diagonal completion. Dangerous hybrids require prefix-varying ownership. This is an exact mechanism description, not a q lower bound.

## C-235 — Native splice intervals and endpoint joins/meets

For a consistent dual-rail support S, define the Boolean interval `Q(S)=[ell(S),u(S)]`, where ell is the indicator of positive literals and u is the complement of the negative-literal set. Then `Q(S union T)=Q(S) intersect Q(T)`, `ell(S union T)=ell(S) OR ell(T)`, and `u(S union T)=u(S) AND u(T)`. Every output-proof interval of a sound Gap-MCSP closure is wholly inside SIZE(s2); in particular both endpoints are size-s2. This yields exact endpoint constraints for arbitrary context/subproof splices, simultaneous disjoint-occurrence substitutions, and every E/H side cross-product at an output rule.

The endpoint law suggests a possible route around the tight `Theta(s2 log s2)` safe-cube dimension: force a high canonical ownership endpoint directly. No mechanism forcing one is known. The C-228 singleton-safe promise and C-234 diagonal equality cover pass the hostile check. This is a verified structural reformulation, not a lower bound. Full proof: `research/C235_CUBE_INTERVAL_CALCULUS_FOR_NATIVE_SPLICES_2026-09-27.md`.

## C-236 — Disagreement-restricted ownership selector cap

For two repeated low anchors `w_g(p,u)=g(u)` and `w_h(p,u)=h(u)`, any compatible context/subproof splice has endpoint z in SIZE(s2). On the disagreement set D, z equals one of the two anchor values coordinatewise. The selector `mu=(w_g XOR w_h) AND (z XOR w_h)` records which anchor was chosen and is computable with size at most `s2+2s1+O(1)`. More directly, distinct masks require distinct restrictions of z, so across all compatible splices at most `|SIZE(s2)|=2^(o(N))` masks occur. For typical g,h, D has size at least N/3, leaving `2^(Omega(N))` possible masks, almost all forbidden. This isolates the exact consistency constraint, but does not lower-bound q: no bound connects q to the image size of context/subproof products. The O(N) diagonal equality cover passes by keeping masks prefix-constant. Full proof: `research/C236_DISAGREEMENT_SELECTOR_CAP_FOR_COMPATIBLE_SPLICES_2026-09-27.md`.

**C-236-A completion refinement.** For each compatible selector mu, the canonical source hybrid `H_mu=w_h XOR mu` is a completion of the mixed support and hence is itself low. Thus masks outside `L_{g,h}={mu:H_mu in SIZE(s2)}` cannot be induced; the mask-to-hybrid map is injective, giving the `|SIZE(s2)|` cap. This strengthens endpoint-only bookkeeping but still does not connect profile-image size to q. See C-236.

## C-237 — The disagreement-selector safe width is tight

For typical repeated low anchors `w_g,w_h`, their safe selector set contains an axis-aligned cube of dimension `Theta_beta(s2 n)`. If beta<1/2, put a Lupanov-sized free subcube in one disagreement column. If beta>=1/2, choose q differing suffix columns and vary arbitrary prefix functions; Lupanov synthesis costs `O(qr/(n-k)+qk+s1)<=s2`. C-230 gives the matching O(s2 n) upper bound. Thus random anchor disagreement does not shrink the safe-cube threshold; charge free-set geometry/grammar generation instead. No q bound follows. Full proof: `research/C237_SAFE_SELECTOR_CUBE_DIMENSION_2026-09-27.md`.

## C-238 — Whole-skeleton E/H cross-product

A ranked witness skeleton records the active states and the selected predecessor edges while abstracting away seed-literal identities. If two accepted tables realize the same skeleton, mixing all E-side seed labels from x with all H-side labels from y preserves a finite proof DAG whenever the mixed support is consistent. Its full cylinder lies in SIZE(s2). This is a global version of state reuse. The immediate counting route fails: there are at most `2^(O(q log q))` skeletons in a q-rule system, too many for the `2^(Theta(s2))` repeated low anchors when q>=N. No q lower bound follows. Full proof: `research/C238_GLOBAL_WITNESS_SKELETON_MIXING_2026-09-27.md`.
## C-239 — Canonical rank fibers and conflict-or-cover

The activation-rank vector from C-233 alone does not determine the side witnesses: a nonmaximal side can have minimum rank 0 on one anchor and a positive predecessor rank on another while the state activation rank stays fixed. C-239 gives an endpoint-realizable two-rule counterexample. The augmented profile of both side minima per state does determine a canonical skeleton; selected predecessor edges decrease rank, and equal-side-rank accepted anchors obey C-238's whole-skeleton E/H cross-product. For fixed Q, this canonical profile is a function of the 2q-bit seed signature, so it gives at most 2^(2q) canonical fibers. This is not a count of all C-238 witness topologies, and it remains too large for anchor pigeonholing at q>=N.

For a reusable state i, let K range over outside-context supports in accepting proofs with a marked i occurrence and C over finite proof supports rooted at i. Substitution gives an accepting output support K union C. If consistent, soundness and C-230 imply |free(K) intersect free(C)|<=kappa_square(s2); otherwise the support contains opposing rails. This is the exact conflict-or-cover obligation on state reuse. No extremal theorem charging it to q is known. A blockwise residual-description attempt also fails to produce a near-linear cover because it must preserve nonempty intersection with one common circuit description across all address blocks. Full proof and limits: research/C239_CANONICAL_RANK_FIBERS_AND_NATIVE_SPLICE_OBLIGATION_2026-09-27.md.

## C-241 — Description-space invariance for shared mismatch DAGs

Status: proved exact model fact; no actual-promise lower bound. For any onto map G:D->Y, the rect-DAG complexity of (d,z)->Mis(G(d),z) on D x Z equals that of (w,z)->Mis(w,z) on Y x Z. Lift Alice-side sets through G for one inequality; restrict a description-DAG to a section sigma:Y->D for the reverse. This handles noncanonical/multiple descriptions exactly. Therefore short circuit descriptions help the bit protocol but cannot reduce standard DAG size unless they yield a small separator circuit for the truth-table promise.

The direct universal separator has size O(N|Y|), and the dyadic restriction-profile router has size O(sum_I pi_I(Y)) <= O(N|Y|/log|Y|+N log N), still exponential for OPS low families. The 2N signed mismatch rectangles are a small nondeterministic cover; they do not furnish a binary product-rectangle DAG. The actual shared-state obligation is global aggregation of the local product-hull condition. Quantitative chain and limits: C-241; no superlinear S_rect, rho_prom, or P-vs-NP result.

Sokolov PLS remains distinct: its state graph is acyclic and a state/successor choice with t communication bits incurs an O(2^(3t)) conversion factor per state. Rank-layering Q gives O(q^2) states and t=O(log(q+N)); the resulting O((q^2+N)(q+N)^3) Boolean game is worse than the direct rank/support compiler. The cyclic q-state closure therefore has no hidden standard-PLS identification.

**C-241 compiler cross-check with C-240.** If m empty-carrier output rules have both seed vocabularies nonempty, C-240 forces each pair to be complementary literals on one coordinate. The seed-construction term in the SCC compiler can therefore be refined from O(qN) to O((q-m)N+m). More precisely the bound is O((q-m)N+m+E_ext+sum_C(r_C e_C+r_C^2)+q). This is parameter-sensitive but does not constrain external support incidence or dense SCC feedback; it leaves the worst-case compiler loss unchanged. No near-lossless q-to-DAG map follows.


## C-242 — Finite antichain grammar and blocker-path dual

**Established.** For a q-state positive least-fixed-point fusion closure, each state has an exact antichain grammar of inclusion-minimal seed supports, obtained as the least finite-proof solution; every minimal support has a witness of height at most q. Every state context/replacement-support pair produces an output proof by subtree substitution. In a successful Gap-MCSP closure, every consistent such support has its full Boolean interval inside SIZE(s2), so both canonical endpoints are in SIZE(s2) and its free dimension is at most kappa_square(s2).

**Established.** For every high table z, each inactive state has a false side whose seeds and active predecessors are absent. Following these sides through a ranked accepting proof for any low table w reaches a mismatching seed literal after at most q state visits.

**Not established.** No q-sensitive bound on the number/geometry of compatible interval joins; no forced high splice; no near-linear full-promise cover; no superlinear native fusion lower bound; no P-vs-NP resolution. Proof and scope: research/C242_NATIVE_CERTIFICATE_ANTICHAIN_AND_BLOCKER_PATH_2026-09-27.md.


**C-242 upper-cover calibration.** For a fixed coordinate order, the native prefix-intersection construction has size at most sum_{t=2}^{N-1}|pi_t(SIZE(s1))|. It is correct because every length-(N-1) low prefix has exactly two table completions, both in SIZE(s2) by one-point patching, so its high-side carrier is empty. C-212 shattering makes the first Theta(s1) levels exponential, so this construction is not near-linear. This is a valid construction and a route-specific failure, not a lower bound on adaptive/native covers. Full argument: research/C242_NATIVE_CERTIFICATE_ANTICHAIN_AND_BLOCKER_PATH_2026-09-27.md.


## C-243/C-244 — carrier containment and state-zone factorisation

**Proved.** If C is any finite proof support rooted at state i, then U intersect Cyl(C) is a subset of T_i. Therefore |T_i| >= 2^(N-|dom(C)|)-M2; pairwise-disjoint high portions of t-fixed-coordinate proof cylinders obey the C-243 packing inequality.

**Proved.** Let P_i be all finite proof supports rooted at i and K_i all finite accepting contexts with a hole at i. On legal inputs, Acc_Q(x)=OR_i([P_i](x) AND [K_i](x)). For a sound promise separator, the q zones Z_i=[P_i] intersect [K_i] cover SIZE(s1) and are each subsets of SIZE(s2). Every compatible K,C cylinder is low.

**Open.** No bound relates q to the number or geometry of low circuits in a grammar-generated zone; carrier intersections may be correlated. No superlinear native lower bound, near-linear full-promise cover, or P-vs-NP proof follows. See research/C243_CARRIER_VOLUME_AND_CERTIFICATE_PACKING_2026-09-27.md and research/C244_STATE_ZONE_FACTORISATION_AND_GLOBAL_READOUT_2026-09-27.md.


## C-245 — Marked proof/context antichain grammar

**Proved.** Over the antichain semiring of consistent signed-literal supports, a one-hole context recurrence propagates the hole through one rule side and an ordinary proof through the other. For every input and state i, the full-context zone is unchanged if contexts are restricted to height at most 2q: shorten the root-to-hole path by deleting repeated states and replace sibling proofs by rank-minimal proofs.

**Consequence.** The C-244 state-zone decomposition has a direct representation from the same q-rule grammar, with q^2 context-family indices over all hole targets and at most 2q iterations. This counts family labels only; antichains may be exponentially large. It gives no superlinear q lower bound. Full derivation: research/C245_MARKED_ANTICHAIN_GRAMMAR_FOR_CONTEXTS_2026-09-27.md.


## C-246 — Repeated-block proof-cylinder capacity; count route fails

**Proved.** In the C-234 diagonal family, if N=rm and each suffix value is repeated r times, a sound support cylinder fixing all but at most kappa coordinates can match at most 2^(kappa/r) diagonal anchors. Since kappa=o(N) and m=Theta(s2), this is 2^(o(m)); an exponential number of proof supports is needed to cover the family.

**Count audit.** A q-state closure has at most q*2^q*(2N+q)^(2q) ranked witness-DAG encodings. Hence certificate count yields only Theta(m)-kappa/r <= O(q log(N+q)), weaker than q>=N-o(N) when m=N^beta, beta<1. The first failed implication is exponential support count => superlinear state count. Full proof and learning: research/C246_REPEATED_BLOCK_CERTIFICATE_CAP_AND_COUNTING_FAILURE_2026-09-27.md.


## C-247 — Multi-hole splice entropy budget

**Proved.** Pairwise disjoint marked occurrences in a finite accepting proof can be replaced simultaneously. If their associated anchor completions have distinct restrictions to disjoint private coordinate sets left free by the context and other slots, and all unions are consistent, then the product of family sizes is at most |SIZE(s2)| by soundness.

**Calibration.** C-234 block isolation gives 2^N distinct accepted hybrids and contradicts log|SIZE(s2)|=o(N), recovering its conditional exponential bound. The diagonal equality cover defeats the private-slot premise through context fingerprints. No small-q theorem forces a large compatible product or charges fingerprints superlinearly. See research/C247_MULTIHole_SPLICE_ENTROPY_BUDGET_2026-09-27.md.


## C-248 — Blocker rectangles and monotone extension

**Proved.** Every state i induces the product rectangle R_i=A_i×B_i of low tables activating i and high tables blocking i. Output rectangles cover Y×Z. Each R_i is covered by signed seed-mismatch rectangles on whichever side the high input blocks, together with predecessor rectangles; low activation ranks force routes to terminate within q steps. Thus state reuse automatically includes every cross-pair in the rectangle.

**Transfer.** Unrolling q least-fixed-point rounds produces a monotone separator extension over the signed-seed encoding with at most 3q²+1 unbounded-fan-in gates, counting gates but not wires. A lower bound M on this extension measure implies q≥sqrt((M−1)/3). The compiler has O(q²(N+q)) gate-input incidences, hence O(q³) at q≈N; it is not an improved bounded-fan-in compiler.

**Limit.** Every disjoint promise already has a 2N mismatch-rectangle cover. More sharply, the artificial promise Y={0,1}^N \setminus {0^N,1^N}, Z={0^N,1^N} has a one-rule native cover and a full rectangle R_1=Y×Z; different pairs route to different mismatching coordinates. Rectangle area and raw cover count do not charge q, and pair-space cross-swaps do not splice truth tables. No lower bound on the actual promise's monotone extension measure, no superlinear fusion bound, no near-linear cover, and no P-vs-NP proof has been obtained. See research/C248_BLOCKER_RECTANGLES_AND_MONOTONE_EXTENSION_COMPILER_2026-09-27.md.


## C-249 — Bi-blocked output-root normal form

**Proved.** At OPS parameters, every signed coordinate half-cube intersects the high side U because |SIZE(s2)|=2^{o(N)}. For each accepted low table, an active empty-carrier state of minimum activation rank has two nonempty, disjoint endpoints: an empty endpoint cannot contain a nonempty seed slice, and any predecessor carrier contained in it would itself be empty and activate earlier. Thus only roots with both endpoints nonempty are needed for completeness.

**Consequence.** Each normalized root i contains high witnesses z_E∈E_i and z_H∈H_i that block its opposite sides. By C-240, direct root seed vocabularies are at most a complementary singleton literal pair or are seedless on one side; an accepting proof must pass to a predecessor. The one-bit root choice or forced escape maps low anchors into predecessor rectangles paired with fixed high witnesses.

**Limit.** This is only a root normal form. It gives no bound on the number or geometry of predecessor families, no q-sensitive cross-join charge, no near-linear cover, and no P-vs-NP proof. The C-248 one-state generic counterexample lacks the actual high-side shattering premise. See research/C249_BIBLOCKED_OUTPUT_ROOT_NORMAL_FORM_2026-09-27.md.


## C-250 — Half-safe predecessor supports

**Proved, conditional on C-243.** At a seedful minimum-rank output root, a low anchor matching a direct literal (k,b) must escape through an opposite-side predecessor. Every high table extending any support cylinder C for that predecessor lies in its carrier, which is disjoint from the root's matching high half-cube. Thus the half of Cyl(C) with bit k=b contains no high tables and is wholly in SIZE(s2). Therefore |free(C)| <= ceil(log2|SIZE(s2)|)+1.

**Limit.** On repeated-block anchors this limits each seedful escape cylinder to 2^((kappa+1)/r) anchors, but witness-DAG counting still gives only a scale below the existing linear q floor. Seedless roots are outside the lemma. The needed next result remains a q-sensitive aggregation of context/proof joins across roots; no superlinear q bound or P-vs-NP proof follows. See research/C250_ONE_SIDED_SAFE_ESCAPE_CYLINDERS_2026-09-27.md.


## C-251 — Root escape support dichotomy

**Proved.** Every accepted low at a C-249 normalized empty root has one of two selected proof forms. If a direct seed matches, the opposite predecessor support is half-safe by C-250. If no direct seed matches, both sides use predecessor supports; their union is consistent, and every completion preserves the empty-root proof, so the union cylinder lies wholly in SIZE(s2) and has at most floor(log2|SIZE(s2)|) free coordinates. This covers seedless roots and missed-seed branches at the paired-support level.

**Consequence and limit.** In the C-234 repeated-block family each selected single or paired support signature covers at most 2^((kappa+1)/r) anchors. Counting signatures still gives only exp(O(q log(N+q))) capacity, since paired proof-DAG descriptions square the old count up to constants. No cross-root reuse charge, superlinear state bound, near-linear full-promise cover, or P-vs-NP proof follows. See research/C251_ROOT_ESCAPE_SUPPORT_DICHOTOMY_2026-09-27.md.


## C-252 — State-conflict graph readout

**Proved.** Aggregate predecessor pairs over all empty output roots into relation G subset [q] x [q]. No high table activates both endpoints of a pair, since C-243 puts it in both disjoint root endpoints. Direct seed/opposite-predecessor branches similarly give at most 2qN forbidden state/literal incidences. Every accepted low activates a pair in G or a state/literal incidence. Thus a depth-two separator readout has at most q^2+2qN terms over the q cyclic activation predicates and input literals.

**Limit.** The readout has q^2+2qN terms; with the existing OPS floor q=Omega(N), composing it with q-round unrolling remains O(q^2) unbounded-fan-in gates, matching C-248. The conflict graph does not bound activation-fibre sizes or give a superlinear q lower bound. The new target is a fibre-geometry theorem for the actual low/high circuit promise, or a near-linear cover. No P-vs-NP proof follows. See research/C252_STATE_CONFLICT_GRAPH_READOUT_2026-09-27.md.

## C-253 ? Conflict-profile fibre subcubes

**Proved.** A profile containing a C-252 conflict edge has no high inputs. For an independent profile sigma, let B_sigma be the seed literals incident to its active states. The low fibre is contained in the union of B_sigma's literal slices; the high fibre avoids all those literals and lies in a subcube fixing every marked coordinate. Thus |U intersect F_sigma| <= 2^(N-r_sigma), or the fibre is high-empty if both polarities are marked at one coordinate.

**Entropy audit.** If I independent profiles occur on high inputs and r_min is their minimum marker-coordinate count, then |U|/2^N <= I*2^(-r_min), so r_min<=log2(I)+o(1)<=q+o(1). This only guarantees one weakly marked high profile; it need not be used by low inputs. Two-wise shattering alone does not force low/high profiles to be coupled. No state lower bound, near-linear cover, or P-vs-NP proof follows. See research/C253_CONFLICT_PROFILE_FIBRE_SUBCUBES_2026-09-27.md.

## C-254 ? Partial-support hazard boundary

**Proved.** Define state activation on a partial support C by existence of a finite proof with all leaf literals contained in C. If C already activates an edge of the C-252 conflict relation, or an active state plus an incident direct-seed literal, every completion activates an empty output root. Hence Cyl(C) is contained in SIZE(s2), and |dom(C)|>=N-log2|SIZE(s2)|. Hazard is monotone under extending C; every low table has a first hazardous prefix at depth at least this large in every coordinate order.

**Corrected support bound.** A selected readout term has a ranked witness DAG with at most q distinct states, at most two seed literals per state, and at most one additional marker. Thus its hazardous support has width <=2q+1, giving q >= (N-log2|SIZE(s2)|-1)/2. This is only linear and weaker than the existing N-o(N) floor; no superlinear aggregate follows. See research/C254_PARTIAL_SUPPORT_HAZARD_BOUNDARY_2026-09-27.md.

## C-257 — Parity-code native closure calibration

**Proved.** For odd-parity high set `U` and even-parity anchors, a native list of `4N-4` pairs derives the empty set for every low anchor. Prefix-parity carriers propagate by intersecting with each next matching literal slice; the final even-parity intersection is empty. Every proper partial assignment has a high odd completion, so every consistent output-proof support fixes all N coordinates.

**Splice consequence.** A consistent context/subproof splice is again an output proof and therefore fixes all N bits. Its unique completion cannot be high by soundness, so it is another even anchor. Thus density/shattering, full certificate width, and anchor abundance alone cannot force a bad splice or superlinear q.

**Scope.** This artificial promise does not match `SIZE(s1)` and yields no OPS bound. O-153 needs an actual low-circuit-description consistency theorem. See `research/C257_PARITY_CODE_SPLICE_LOCKING_CALIBRATION_2026-09-27.md`.


## C-255 — Shared-DAG route audit

For plain C-75 signed mismatch, the minimum binary rect-DAG size is `Theta(C_sep)`, the minimum Boolean separator extension size. Pullback through `G(d)=TT(C_d)` and restriction to one description per low table show exact size invariance in description space. A q-pair fusion cover currently yields only `S_rect=O(q^3/log q)`; conversely `q<=O(S_rect)`. The q activation graph is cyclic with input-dependent ranks, so q named rules do not themselves form an acyclic q-node DAG. Product-hull safety at each merged state is exact, but no overlap-safe global charge or near-linear adaptive DAG was obtained. C-255 also proves the common-translate lemma: if `|SIZE(s1)||SIZE(s2)|<2^N`, some `r` has `u xor r` outside `SIZE(s2)` for every `u in SIZE(s1)`. It does not solve source-reduction cut soundness. See `research/C255_SHARED_DAG_ROUTE_RESTART_2026-09-27.md`.
**C-256 static-decoder obstruction (proved).** Let f:{0,1}^M->{0,1} have two-wise-rich one/zero sides, with 0,e_i on the one-side and 1^M on the zero-side. For any common translate r, low base-table encodings u_x,v_y, and a fixed decoder from each outer mismatch label (k,b) to a KW answer, if every induced mismatch rectangle is source-valid then r=v_{1^M} xor u_{0^M} xor OR_i(u_{0^M} xor u_{e_i}). Hence C(r)=O(Ms1); if this fits s2, it contradicts r notin SIZE(s1) xor SIZE(s2). Separately, for full-domain BPHP search, a static decoder from each (k,b) to a collision answer is impossible: at an active coordinate both signed rectangles are nonempty, and their two fixed Alice collision-equality sets would have to cover the full assignment domain, which two equality predicates cannot do. Scope: static output-label reductions only; no target DAG lower bound, because repeated labels at distinct sinks could be decoded differently. Full proof and BPHP source details: research/C256_HARD_TRANSLATE_KW_DECODER_OBSTRUCTION_2026-09-27.md.

## C-258 - Repeated-block native subcover

For coordinates partitioned into d blocks of length r, let `Rep_{d,r}` be all blockwise constant tables and let U be the actual complement of `SIZE(s2)`. If `Rep_{d,r} subseteq SIZE(s1)` and every literal slice of U is nonempty, the explicit block-prefix/merge/intersection construction in C-258 gives a successful native list with `q=2N+2d-1`. It is an upper bound for this subfamily only. This realizes the diagonal equality fingerprint directly in the cyclic closure model. It does not aggregate over all low circuits and therefore gives no full-promise upper bound or lower bound.

## C-259 - Cofactor patching/splice threshold

**Proved.** If t prefix cofactors are each computed by a size-s1 circuit, muxing them gives `CC<=t s1+O(t)`. Under `s2/s1=cn`, all t up to a sufficiently small constant multiple of n are safely in `SIZE(s2)`. Circuit counting gives `log |SIZE(s2)|=O(s2 n)`; therefore, under C-247's private-coordinate and injective-completion hypotheses, t independent replacement families of size `2^(Theta(s2))` can be sound only for `t=O(n)`.

**Calibration.** Both the constructive patch and the private-slot entropy contradiction turn at `Theta(n)`, matching C-116. This means a constant number of holes cannot suffice; it does not imply that a q-state grammar exposes n holes, nor that q must be superlinear to suppress them. See `research/C259_COFACTOR_PATCHING_SPLICE_THRESHOLD_2026-09-27.md`.

## C-260 - Native proof–blocker duality

**Proved.** On arbitrary seed-feature inputs, each native state has a minimal certificate antichain `C_i` and a minimal absent-feature blocker antichain `B_i`; the least-fixed-point recurrences are De Morgan duals and `B_i=Tr(C_i)`. Output blockers are the transversal family of output certificates. For the consistent table-realizable certificates, cutting an accepting proof at state i gives `C_out^cons=min_i(K_i join P_i)`. Every compatible join is hit by every output blocker. On actual table inputs, this yields sound accepting cubes, low-free rejecting cubes, and a mismatch literal for each low/high pair.

**Limit.** The transversal law only forces a nonempty intersection; it does not limit how many compatible joins one blocker literal can hit, or charge q for the family of joins. It does not improve the `N-o(N)` native lower bound or construct a full-promise near-linear cover. The candidate next invariant is q-sensitive incidence geometry of context/proof joins against the shared blocker grammar. Full proof: `research/C260_NATIVE_PROOF_BLOCKER_DUALITY_2026-09-27.md`.

**Forced-reuse calibration.** For a repeated-block subfamily of size `2^d` with `d log d=O(s1)`, every anchor's minimum-rank active empty root has a predecessor by C-249. Assigning its first predecessor state to that anchor forces some internal state to serve at least `2^d/q` anchors. This is genuine state reuse, but C-258's O(N) equality-fingerprint cover of the same family shows the collision can be safe; no compatible cross-product follows.
