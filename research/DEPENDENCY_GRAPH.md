# Dependency graph

## Minimum Gap-MCSP route

OPEN O-1: Gap-MCSP has no size-\(N^{1+\epsilon}\) circuit family
  |
  | OPS Theorem 1.4, with its fixed-\(\beta\) family of premises
  v
PROVED conditional: \(\mathrm{NP}\not\subseteq\mathrm{P/poly}\)
  |
  | \(\mathrm P\subseteq\mathrm{P/poly}\)
  v
CONDITIONAL conclusion: \(\mathrm P\ne\mathrm{NP}\)

Equivalent set representation on \(\Gamma=Y\sqcup Z\): \(D(Y\mid\mathcal B)\) is the De Morgan circuit complexity of the promise classifier, with \(\mathcal B\) the positive and negative truth-table literal slices. Any fixed complete circuit basis has a constant-factor De Morgan simulation. Therefore a slightly superlinear lower bound on \(D\) is the weakest direct target in this route.

## Stronger fusion-cover subroute

OPEN O-2: \(\rho(Y,\mathcal B)+\rho(Z,\mathcal B)>N^{1+\epsilon}\)
  |
  | \(D\ge D_\cap(Y)+D_\cap(Z)\ge\rho(Y)+\rho(Z)\)
  v
OPEN O-1 circuit lower bound

Here each \(\rho\) is exactly cyclic intersection complexity. The joint cover route is a sufficient condition but still stronger than O-1; it is weaker than requiring one side alone to exceed the threshold. The project has \(\rho(Y,\mathcal B)\ge N-\log M_2-1\). The attempted symmetric estimate \(\rho(Z)\ge N-\log M_1-1\) was invalid because a high-anchor subcube avoiding low tables can contain gap and high tables. Interpolation of the prescribed coordinates gives only \(\rho(Z,\mathcal B)=\Omega(s_1/n)\), leaving the total acyclic lower bound at \(N-o(N)\).

## Current quantitative proof

PROJECT-PROVED: low-anchor empty-closure trace forces at least \(N-\log M_2-1\) intersections
  |
  +-- complement-side interpolation gives only \(\Omega(s_1/n)\) more union gates
  v
PROJECT-PROVED: \(D(Y\mid\mathcal B)\ge N-o(N)\)
  |
  +-- still linear; O-1 remains OPEN

The proof counts how many coordinates must be fixed before a subcube avoids the opposite promise side. It does not charge global gate reuse strongly enough to yield a superlinear exponent.

## Alternative proof routes (inactive)

- OPEN: violate the exact time-bounded Kolmogorov chain rule in the needed uniform parameter regime \(\to\) conditional \(\mathrm P\ne\mathrm{NP}\); existing audits find a degree/clock gap.
- OPEN: a fixed \(R_q\in\mathrm{coNP}\) outside P \(\to\) \(\mathrm P\ne\mathrm{NP}\); existing diagonalization does not beat its own verification clock.
- OPEN/FORMALIZATION: PichÃ¢â‚¬â€œSanthanam feasible error-witness condition plus the relevant Extended Frege lower-bound premise \(\to\) \(\mathrm P\ne\mathrm{NP}\).
- SELF-REFERENCE: SAT liar reductions fail the ordinary-instance size recurrence or have a two-cycle without a fixed point.

No alternative currently has a proved first open statement easier than O-1.

## Adaptive anti-checker alternative

OPEN: there is a fixed $\delta>0$ such that for every sufficiently small fixed $\beta>0$, infinitely many $n$ have no valid OPS selector of size $N^{1+\delta}$ for $s_1=2^{\beta n}/(10n)$, $s_2=2^{\beta n}$, and $t=2^{10\beta n}$.
  |
  | OPS Lemma 4.1: if $NP\subseteq Circuit[poly]$, then for its fixed (unknown) polynomial exponent there is a constant $k$ and selectors of size $N^{1+k\beta}$ for every sufficiently small $\beta$.
  | Choose $\beta<\delta/k$; the lower bound contradicts this selector family.
  v
PROVED implication: $NP\not\subseteq P/poly$ and hence $P\ne NP$.

The fixed-sample counting lemma C-15 only establishes that the selector must adapt to all truth-table bits. C-16's patching iteration terminates at complexity at most $s_2$ but may stop in the promise gap, so it does not establish the open selector lower bound. C-17 and C-18 give increasingly strong lower bounds on the number of distinct samples in the selector's range, but the $tn$ output bits can encode the C-18 range size without a circuit-size lower bound. C-19 shows that sparse-table positive capture is easy. C-20 reframes the sample as a table-conditioned transversal of all low-circuit error sets; generic size and minimum-distance bounds yield only a vacuous sample. A proof must exploit their structured overlap to lower-bound the computation of that transversal. The stated selector theorem is sufficient: under $NP\subseteq Circuit[poly]$, OPS fixes a constant $k$ and gives selectors of size $N^{1+k\beta}$ for every small $\beta$; choose $\beta<\delta/k$. This is a separate sufficient formulation of the O-1 difficulty, not a current proof.

## Dual anti-approximation formulation (C-40)

PROVED: $CC(f)>Cns$  
  -> finite minimax gives a distribution $\mu$ with $\Pr_{x\sim\mu}[D(x)\ne f(x)]\ge1/3$ for every $D\in\mathcal C_s$  
  -> sampling $O(s\log(s+n))$ points yields an anti-checker  
  -> OPEN: construct a valid witness list for every high-complexity $f$ by a small circuit, without assuming a solver for weighted circuit fitting.

The semantic margin $\Delta_s(f)$ is zero for $CC(f)\le s$ and bounded below for $CC(f)>Cns$. Computing that promise is Gap-MCSP itself. The LP exposes an NP separation problem but does not weaken O-1. It is a diagnostic of the witness-synthesis bottleneck, not a new implication toward separation.

## Minimax, search, and constructive selector

PROVED / KNOWN (C-21): if $CC(f)>\Theta(ns)$, finite minimax gives a distribution on inputs under which every size-$s$ circuit has constant error; Hoeffding sampling reduces its support to $O(s\log(n+s))$.
  |
  | does not compute the distribution or its support from $f$
  v
OPEN: lower-bound or construct the map $f\mapsto Q_f$ on all tables with $CC(f)>s_2$.
  |
  | OPS Lemma 4.1: under $NP\subseteq Circuit[poly]$, this map has size $N^{1+O(\beta)}$
  v
PROVED conditional implication: a matching lower bound for every sufficiently small fixed $\beta$ forces $NP\not\subseteq P/poly$, hence $P\ne NP$.

The selector relation is coNP for a proposed list, and its prefix-extension problem lies in $\Sigma_2^P$ (C-22). Under $P=NP$, self-reduction gives a polynomial-time selector, but with no near-linear exponent. This confirms that the magnification target is quantitative; the easy existence and generic search facts do not close it.

## Sparse-support audit

PROVED PROJECT LEMMA (C-23): for $1-o(1)$ of weight-$s_2$ supports, the list consisting of all positive positions plus a fixed hitting set for dense low-circuit 1-sets is a valid anti-checker. A sorting circuit of size $O(Nn^3)$ produces it on that fraction of inputs.
  |
  | does not cover every high-complexity table or the exceptional sparse supports
  v
OPEN: any sparse-support lower bound must target supports contained in sparse low-circuit 1-sets and prove that identifying/refuting those supersets is computationally expensive.

Thus C-18's sample-range theorem is compatible with an easy selector on almost all sparse inputs. Range size is not circuit complexity.

C-24 extends the distributional audit to supports inside sample-sized axis-aligned subcubes: the positive support reveals the entire region as its coordinate hull, and that region itself anti-checks all low circuits with high probability. The remaining candidate family must hide its low-density region from simple hull recovery; merely placing random positives inside a small circuit set does not suffice.

## Independent uniform route from 2025

PROVED CONDITIONAL THEOREM (Atserias-MÃƒÂ¼ller): a near-linear P-uniform circuit lower bound for an approximation of subexponential-threshold MCSP implies $P\ne NP^{\oplus P}$.
  |
  | no known implication from this separation alone to $P\ne NP$
  v
NOT A CURRENT P-vs-NP PATH; retain as a side route unless the class implication is strengthened.

## Region-relative sparse-support branch (C-25/C-26)

Known region $A$ + random support $R$ + two relative-density bounds => short anti-checker (C-25).

Affine subspace $A$ + random support $R$ => affine hull recovery by Gaussian elimination + output all of $A$ => near-linear selector on that promised distributional family (C-26).

Neither branch yields a worst-case selector lower bound. The missing implication is universal: failure of these natural region-based constructions does not show that every selector has to recover a containing region. The active proof obligation remains O-1 / the OPS selector lower bound.
## Version-space transversal (C-27)

For sparse $f=1_R$, querying $R$ catches every low circuit that rejects a positive. Remaining circuits accept $R$; each contributes the residual false-positive set $E_D=D^{-1}(1)\setminus R$. Additional zero queries anti-check exactly when they form a transversal of these $E_D$ sets.
  |
  +-- C-21 minimax: constant-mass fractional transversal exists
  |       +-- sampling: short integral transversal exists
  |
  +-- C-25 known-region density split: explicit probabilistic transversal
          +-- C-24/C-26 recover some simple regions cheaply

OPEN: compute such transversals for every high-complexity table at near-linear circuit size, or prove that no such selector exists. The equivalence and existence bounds do not establish hardness.

Residual version-space view (C-45):
  Q -> V_f(Q)={D in C_s: D agrees with f on Q}
  -> arbitrary counterexample removes at least one surviving circuit (at most |C_s| rounds)
  -> dual margin gives ÃŽÂ¼(E_D)Ã¢â€°Â¥ÃŽÂ³ for every D
  -> some point removes a ÃŽÂ³-fraction of every current V_f(Q)
  -> ideal greedy sequence has O(ÃŽÂ³^{-1} log |C_s|) points; random sampling gives the same order
  -> OPEN: find a ÃŽÂ³-fraction contraction point efficiently for the explicit circuit class.

Potential route: compute the number of surviving circuit descriptions that disagree at each point and choose a maximizer. This is #P-style counting, but no necessity or hardness reduction is established. A successful alternative may bypass this potential entirely.

C-47 makes that branch explicit:
  exact #P counts of survivors and pointwise errors
  -> choose a maximum-coverage point
  -> deterministic selector using O(N s log s) #P queries
  -> OPEN unconditionally: implement contraction in ordinary near-linear circuits or lower-bound the universal selector; no evidence shows every selector must use this greedy score.

This is an oracle upper bound only. It is not a P/poly selector and does not contradict O-1.

C-48 refines the conditional branch:
  relative approximate score (BPP^NP / Stockmeyer) on transcript length m=O(s n^2)
  -> under NP subset P/poly, deterministic polynomial-size local score circuits
  -> parallel scores for N candidate addresses over O(s log(s+n)) rounds
  -> selector size N^{1+O(beta)}
  -> reproduces the known OPS conditional upper bound; no lower bound follows.

Crucial reset: neither exact nor approximate score computation is known to be necessary for an arbitrary selector. A hardness result for this greedy branch alone cannot discharge O-1 without a reduction from every valid selector to that branch. The active node remains the direct slightly-superlinear circuit lower bound / universal puncturing-certificate lower bound.

## Proof-complexity and quantifier-collapse side route (C-43/C-44)

OPEN: a single $S^1_2$-provable feasible anti-checker generator
  -> PichÃ¢â‚¬â€œSanthanam Theorem 7 + EF not p-bounded
  -> SAT circuit lower bound

Replacing the generator by bare existential data gives a $\forall\Sigma^b_2$ claim
  -> KPT finite adaptive witnesses
  -> later outputs depend on earlier challenge witnesses
  -> OPEN: polynomial-overhead flattening that avoids unknown satisfying assignments.

P=NP
  -> PH=P
  -> the $\Sigma_2^P$ anti-checker-list search is in P
  -> a polynomial-time promised selector / polynomial circuits of unspecified degree.

This last branch does not reach the OPS $N^{1+\epsilon}$ threshold; by contraposition, OPS gives a near-linear upper bound for an appropriate small-$\beta$ choice from $NP\subseteq P/poly$. Neither side route replaces O-1.
## Bounded-degree algebraic closure (C-30)

Sparse positives in degree-$d$-closed $A$ with restricted evaluation distance $\delta$
  -> random sample spans degree-$d$ feature space ($2^L(1-\delta)^w=o(1)$)
  -> compute algebraic closure by Gaussian elimination
  -> recover A
  -> output A as anti-checker if $|A|\le t$ and no low circuit matches on A.

For bounded-degree graph regions, $L=poly(n)$ and $\delta$ is constant. This is a uniform near-linear selector on that promised family. It excludes another structured adversary but does not imply all hard tables have such closures.
## Fourier recovery of secret product regions (C-32)

Hidden invertible linear map + product block support
  -> product Fourier spectrum has a constant gap
  -> Walsh transform identifies high frequencies
  -> minimal dependencies group hidden blocks
  -> sample projections recover local pattern sets
  -> output the entire low-circuit region as an anti-checker.

This is uniform over the hidden linear transformation and near-linear in the truth-table length for fixed block size. C-31 is the adversarial check on C-30: Hamming balls have full fixed-degree closure but yield to maximum-weight recovery. Both branches eliminate structured distributions only. The universal selector lower bound remains open.
## General Fourier-matroid criterion (C-33)

Fixed local alphabet $B$ + full affine span + connected spanning set of maximal nonzero Fourier frequencies
  -> product spectrum has isolated single-block peaks
  -> Walsh transform recovers peak vectors
  -> matroid components recover hidden block spaces
  -> sample projections recover local pattern sets
  -> output full region as anti-checker.

C-32 instantiates the criterion with $B=\{0,e_i\}$. Residual test: disconnected/nonspanning peak sets and whether secondary levels expose the blocks.

## Universal selector dependence bound (C-34)

PROVED for every valid OPS selector:
  -> at least $N-t-\log M_2-O(1)=N-o(N)$ essential truth-table inputs
  -> C-38 connectivity count: at least $N-o(N)$ fan-in-two gates after accounting for $tn=o(N)$ output wires
  -> still only a linear circuit lower bound.

This is an adversarial-completion argument, not a promise about the selector architecture. C-38 gives the stronger near-$N$ gate conversion using circuit-graph connectivity, but a linear-size circuit can still depend on every input. The next open edge is a superlinear lower bound on the routing map from a hard truth table to a valid transversal.

## Conditional fibers and linear-sketch obstruction (C-35/C-36)

Uniform random table + fixed query list
  -> C-35: anti-checks with probability $1-2^{-t+O(2^{\beta n})}$
  -> leaves exceptional low-circuit trace cylinders
  -> C-36: robust rank-$k$ linear sketch cannot select a valid query list if $N-t-k>\log M_2$
  -> exact general necessary condition: every address/low-trace fiber has size at most $M_2$
  -> OPEN: prove nonlinear fiber shrinkage costs $N^{1+\epsilon}$ gates, or construct a small selector using label feedback.

The first three edges are proved, with C-36 restricted to affine sketches. The last edge is the unresolved routing lower bound; no implication from the fiber condition to superlinear size is established.

## Near-$N$ circuit-size consequence (C-38)

C-34: every valid selector has $E=N-o(N)$ essential inputs
  -> fan-in-two multi-output circuit with $L=tn=o(N)$ output bits
  -> graph connectivity forces $S\ge E-L=N-o(N)$ gates
  -> OPEN: strengthen linear gate connectivity to $N^{1+\epsilon}$ by charging query-label routing, not just input-to-output connectivity.

The graph count is proved and permits arbitrary fan-out/sharing. It is tight up to the output count for generic circuits and supplies no superlinear separation by itself.

## Linear feedback against constant hypotheses (C-39)

Truth table $f$ nonconstant
  -> priority encoder finds first 1 in $O(N)$ gates
  -> second encoder on $\neg f$ finds first 0 in $O(N)$ gates
  -> the two labels defeat both constant circuits
  -> OPEN: route a short query list that defeats every one of the $M_1$ size-$s_1$ circuits at once.

C-39 shows why the near-$N$ connectivity bound is plausible as a sharp baseline for a tiny hypothesis class. It is not a valid selector against the full circuit class.

## Robust puncturing route (C-49)

PROVED: pointwise circuit correction costs O(n) gates per changed truth-table coordinate
  |
  v
PROVED: every valid anti-checker trace is Omega(s1/n)-far from size-s1/2 circuit traces
  |
  +-- Atserias-Muller sparse distinguisher amplifies the already selected trace
  |      |
  |      +-- does not compute the input-dependent query set
  |      +-- fixed-beta sparsity and formula/uniform conclusion do not imply P != NP
  v
OPEN O-1 unchanged: superlinear lower bound for arbitrary routing to robust puncturings

This route strengthens the certificate's semantic property, not the selector circuit lower bound. Any continuation must charge arbitrary nonlinear query selection and feedback; fingerprint amplification after selection is insufficient.

C-49 + majority closure:
  PROVED: every odd subfamily of up to kappa*n low circuits has a large majority-error region (C-50)
  -> PROVED: some pair in each such subfamily of size at least 3 has a large error-set intersection
  -> C-51 PROVED: heavy-overlap graph on all low-circuit functions has constant density
  -> PROVED but weaker than C-40: every residual family has a point hitting an Omega(sqrt(N^beta/(N*n))) fraction
  -> OPEN: organize these local overlaps into an efficiently findable short transversal for the full circuit family
  -> OPEN O-1: lower-bound or construct the arbitrary selector that finds that transversal.

## Adjacent implicit-MCSP route (parked)

2025/2026 sampler-based CGL / ImpMCSP hardness results
  -> require a way to expose the implicit function's labels and preserve the gap
  -> OPEN Q26: size-preserving conversion to an explicit truth-table Gap-MCSP instance
  -> OPEN O-1 only if that conversion retains the OPS parameters

No such conversion is established. The 2025 learning hardness is unconditional for its specific learning task; the 2026 ImpMCSP result uses cryptographic and proof-system assumptions. Neither presently moves the explicit O-1 node.


## Global marginal selector (C-52)

Exact OPS ratio s2=10ns1
  -> minimax margin Delta_s1(f) >= 3/10
  -> O(n)-description sample approximates all N global marginals
  -> O(Nn)-gate circuit chooses a point rejecting at least 3/20 of descriptions
  -> OPEN: condition/reconstruct marginals for each residual version space
  -> OPEN: eliminate rare survivors and finish an anti-checker
  -> O-1 unchanged.

The first-query theorem is an upper-bound baseline, not progress on the superlinear lower-bound exponent.


## Relative adaptive sampling (C-53)

All transcripts of length at most k give only exp(O(kn)) residual/error ranges
  -> relative Chernoff sample of O((kn+log(1/eta))/(gamma*rho)) descriptions
  -> constant-fraction contraction while each residual has mass at least rho
  -> polynomial sample reaches inverse-polynomial rho
  -> after O(log(1/rho)) rounds, residual may be nonempty below rho
  -> exact emptiness requires a full-description-scale sample in this method
  -> OPEN: bypass global sampling or eliminate the rare tail structurally
  -> O-1 unchanged.

C-53 improves C-52's crude additive bound, not the general selector lower bound.


## Forced nonempty handoff (C-54)

Any q=O(n) labeled query transcript
  -> DNF interpolation circuit of size O(qn)=O(n^2)<s1
  -> residual low-circuit version space is nonempty
  -> C-53 relative greedy contraction crosses inverse-polynomial mass in O(n) rounds
  -> its certified prefix ends at a nonempty residual
  -> OPEN: continue through at least Omega(s1/n) queries and then certify exact emptiness
  -> O-1 remains the unrestricted selector lower bound.

This locates a genuine architecture-specific handoff point; it does not prohibit a different selector from continuing.


## Witness uniformization audit (C-55)

High table $f$
  -> minimax margin $\Delta(f)\ge3/10$
  -> existential greedy process deletes at least 3/10 of every nonempty residual
  -> $\forall f\,\exists Q$ of length $O(\log|\mathcal C_{s_1}|)$ with $R_n(f,Q)$
  -> OPEN: construct one $N^{1+\epsilon}$-size circuit family $S_n$ outputting at most $t_n=2^{10\beta n}$ points and satisfying $R_n(f,S_n(f))$ for every high $f$
  -> anti-checker selector lower bound / direct O-1 Gap-MCSP lower bound
  -> OPS magnification
  -> $P\ne NP$.

The relation $R_n(f,Q)$ is coNP-checkable because a matching low circuit witnesses failure. The pointwise existence arrow is proved; it is not an efficient Skolemization theorem. Global-sampling failure at C-54 gives no lower bound on the open selector node.

Output-counting / entropy
  -> C-56: each anti-realizable trace gives a cylinder of $2^{N-|Q|}$ tables sharing one valid list
  -> almost all extensions are still high at OPS parameters
  -> OPEN: identify the input-dependent routing difficulty; no circuit-size bound follows from the number or length of outputs.

## External teaching-set length (C-57)

High table $f$
  -> local patching: every valid list has length $\Omega(s_1/n)$
  -> minimax contraction: some valid list has length $O(s_1\log(s_1+n))$
  -> OPEN: size of the circuit mapping $f$ to any such list.

The length interval is only a polynomial factor at OPS parameters. Improving it alone does not address O-1 unless it also yields an efficient selector or an architecture-independent circuit lower bound.


## Separate selector-lower-bound route

Assumption $NP\subseteq P/poly$
  -> OPS Lemma 4.1 (C-48): there is a constant k such that for every sufficiently small fixed $\beta>0$, a valid selector of size $N^{1+k\beta}$ exists at all sufficiently large arities
  -> **OPEN S-1 / C-65:** there are $\delta,\beta_0>0$ such that for every fixed $0<\beta<\beta_0$ with $\beta<1/10$, every selector family valid on all hard tables against every circuit of size $s_1$ and with budget $t_n=N^{10\beta}$ has size $>N^{1+\delta}$ infinitely often
  -> choose $\beta<\min(\beta_0,1/10,\delta/(2(k+1)))$ after k is fixed
  -> contradiction to the conditional construction
  -> $NP\not\subseteq P/poly$
  -> $P\ne NP$.

S-1 is a distinct sufficient route, not shown equivalent to O-1. The beta interval is necessary to choose beta after the unknown exponent k is fixed. A lower bound on any infinite subsequence of arities suffices here; no progression-robust version is needed for the direct OPS contradiction. The lower bound is over every nonuniform selector on the high-table promise, not only greedy, sampling, or score-based implementations.

## Direct reduction to selector search: current transfer obstruction

Kannan fixed-exponent language $L_k$
  -> OPEN: polynomial-time map to high tables, with table length $N=m^{a_k}$
  -> OPEN: decoder $B(x,Q,f_x|_Q)$ returns $L_k(x)$ for every valid short anti-checker output
  -> selector composition exponent is $a_k(1+\epsilon)$; include reduction/decoder exponents $b_k,d_k$ in $e_k=max\{a_k(1+\epsilon),b_k,d_k\}$
  -> contradiction only if $k>e_k$.

C-58 blocks local payloads that leave a common valid base list unchanged. C-59 blocks the simple gadget with disjoint, easy-decoded regions and one low approximant per omitted source bit. Its short-transversal counterexample shows these are not a universal impossibility theorem. C-60 records the exponent/quantifier gap. No arrow from Kannan to S-1 or O-1 is established.

## Mandatory-region branch (C-61)

High table $f$
  -> C-52: one dual distribution $\nu$ has $\nu(E_D)\ge3/10$ for every low circuit $D$
  -> condition $\nu$ outside a proposed mandatory region $P$
  -> if $\nu(P)$ is too small, random sampling outside $P$ gives a valid list of at most $t$ points
  -> C-61: each mandatory $P$ has mass $\ge(3/10-\alpha)/(1-\alpha)$, $\alpha=\ln M_1/t$
  -> at most three pairwise-disjoint mandatory regions at OPS parameters
  -> OPEN: encode source information through overlapping/nonlocal output structure, or prove a selector lower bound without a region gadget.

C-61 is a genuine narrowing of the reduction design space, not a lower bound for the selector itself.

## Output-only reduction separation (C-62)

Oppositely labeled source instances $x,y$ mapped to high tables $f_x,f_y$
  -> if $\nu_{f_x}(\{f_x\ne f_y\})<p_*$, C-61 gives a common valid labeled list
  -> likewise for $\nu_{f_y}$
  -> an output-only decoder cannot return two answers on that shared output
  -> OPEN: prove reduction tables are dual-mass separated, or show that this separation itself costs too much to generate.

This condition does not apply when the decoder also sees $x$; then circuit complexity of that decoder is charged in C-60.

## Agreement-fiber attack (C-63)

Candidate selector S
  -> for each low D define \(A_D^S=\{f:f|_{S(f)}=D|_{S(f)}\}\)
  -> S is valid on all high tables iff every \(A_D^S\subseteq SIZE(s_2)\)
  -> OPEN S-1 adversarial completion: find D and high f in \(A_D^S\)

Each fixed fiber has a circuit of size O(|S|+t(N+s1+n)). This exposes the exact object to attack, but a two-constant concept class has a linear selector with singleton fibers. The next theorem must exploit a property of the full small-circuit class; no class-independent fiber bound is valid.
## Active research state Ã¢â‚¬â€ adaptive fusion closure (26 September 2026)

O-2 is the active sufficient attack. For each partial semantic pair list \(Q\) and low anchor \(w\), the least preserving closure is represented by the q-bit monotone recurrence in C-67. The anchor-dependent inputs are 2q disjunctive clauses of signed truth-table bits (C-68); pair endpoints have no description-cost restriction.

The canonical surviving witness \(\mathcal C_Q(w)\) changes with \(Q\). The per-anchor distance \(\delta_Q(w)\) to empty closure is at most \(N-1\) and changes by at most one when a pair is added (C-69). C-73 refutes the simplest cross-anchor theorem: for every static distribution on low anchors, some pair at the empty list saves one rule for at least \(1/4-o(1)\) mass. The active target is now a potential that charges shared intermediate intersections once, or a universal list construction. C-09 rules out raw anchor-incidence counting.

Fixed-family fractional rounding gives \(O(N\log R)\) for a specified R-filter family, conditional on the project fractional ceiling, but it does not cover all adaptive closures (C-70). A pair can add a nonempty intersection without deriving empty, so one selected filter per anchor is insufficient. The artificial graph-cut model gives only logarithmic integral complexity; co-singletons miss the fractional ceiling. Neither currently supplies the required gap.

**Status:** exact closure representation and the refutation of a static additive-distance potential are proved, then cross-checked on a finite toy. A shared-state potential, artificial superlinear gap, \(O(N\operatorname{polylog}N)\) global upper bound, and superlinear lower bound remain open. See [the closure-game report](FUSION_CLOSURE_GAME_2026-09-26.md).

## Secondary selector route (S-2 / C-66; inactive while fusion is primary)

Assumption $NP\subseteq P/poly$
  -> C-48 conditional version-space selector: list length $K_n=C_0s_1\log(s_1+n+2)$ and circuit size $N^{1+\kappa\beta}$ for every sufficiently small fixed beta
  -> OPEN S-2: every valid selector family restricted to this short list budget needs size $>N^{1+\delta}$ infinitely often, uniformly for beta in a small interval
  -> choose beta after kappa is fixed
  -> contradiction
  -> $NP\not\subseteq P/poly$
  -> $P\ne NP$.

S-2 is narrower than S-1's full OPS output budget and is sufficient because C-48 already outputs such short lists. C-49 gives these traces relative Hamming distance $\Omega(1/n^2)$ from size-$s_1/2$ circuit traces. Neither the shorter list nor trace robustness proves the required circuit lower bound.

**C-74 interface:** a q-rule list computes a recursive dual-rail separator using q activation states; the accepted set contains Y and avoids U. Acyclic unrolling costs q^2 AND gates, so generic circuit lower bounds lose too much. A direct state-count lower bound is open. The restricted-catalogue incidence gadget is killed by its unlisted (A,B) pair.

**C-75 stress test:** the pair-list proof gives a low/high mismatch protocol, but Alice can transmit a size-s1 circuit and Bob can find a differing coordinate in O(s1 log s1) communication. This is below the local N-o(N) rule bound; the ordinary communication-bit route is closed. Preserve state/DAG complexity if using KW-style methods.

**Precision note for C-74:** the recurrence uses seed clauses, the fixed containments P_i,R_i, and flags for empty consequences. These are induced by actual semantic endpoints and are constrained; the recurrence does not assert that an arbitrary incidence network is realizable.

**C-76 seed-feature factorization:** the least-fixed-point output is a monotone function h_Q of the 2q seed clauses. Every low anchor's true-seed conjunction excludes U and has at least N-log2(M2) clauses by the CNF model-count lemma. This does not improve the one-anchor bound; 2N unit clauses suffice for full minterms. The unresolved complexity is the shared semantic state decoder, not the clause dictionary by itself.


## C-77 cyclic-DAG branch

\(Q\) with q fusion pairs
\(\to\) q-state cyclic monotone conjunctive network
\(\to\) exact full characteristic function of \(Y\)
\(\to\) \(q=D^\circ_\cap(Y\mid\mathcal B)=\rho(Y,\mathcal B)\) [CavalarÃ¢â‚¬â€œOliveira exact theorem]
\(\to\) acyclic AND count at most qÃ‚Â² / full binary rect-DAG size \(O(q^3)\)
\(\to\) hypothetical separator lower bound \(>N^{2+2\epsilon}\) AND gates / rect-DAG lower bound \(>N^{3+3\epsilon}\)
\(\to\) \(q>N^{1+\epsilon}\)
\(\to\) existing OPS magnification bridge
\(\to\) \(P\ne NP\).

Open links: prove cyclic state non-shareability directly; strengthen the low/high promise DAG to cover the entire non-low complement; or prove the stated quantitative separator lower bound. Short-description communication protocols do not fill these links.

## C-78/C-79 shared-DAG update

\(Y\times Z\) signed mismatch
\(\to\) deterministic communication \(O(s_1\log(n+s_1)+\log N)\)
\(\to\) protocol tree may have \(2^{O(s_1\log(n+s_1))}\) nodes
\(\to\) successful q-pair cover yields a ranked witness path
\(\to\) rank-layered binary rect-DAG size \(O(q^2(q+N))=O(q^3)\)
\(\to\) desired q superlinear lower bound requires rect-DAG \(>N^{3+3\epsilon}\)

Alternative target: exact cyclic intersection \(D^\circ_\cap=\rho\), with no DAG loss. The pattern-profile universal DAG has size \(O(|Y|+\sum_{I\ dyadic}\pi_I(Y))\), an upper bound for one architecture only.

Promise-to-exact reversal: a full exact KW DAG can yield a circuit and hence a fusion cover. A promised \(Y\times Z\) DAG may ignore \(M=\mathrm{SIZE}(s_2)\setminus\mathrm{SIZE}(s_1)\). C-79 proves every signed coordinate cylinder has a medium table for sufficiently small OPS \(\beta\); the filter generated by \(M\) and the low anchor's literal slices is preserved by every pair whose endpoints lie in \(Z\). This blocks direct pair-list reuse but not a transformation adding medium-band pairs.



## C-81/C-82 signature constraints

Equal row signatures
-> a common high completion exists unless 2^d_H(w,w') <= |SIZE(s2)|
-> each row-signature class has diameter at most N^(beta+o(1))
-> C-80's block code yields S_rect >= log|C| = Theta(s1), while row-signature counting is capped by log|Y|=o(N).

Dually, equal high-column signatures
-> their common restriction has no low completion
-> minterm interpolation excludes only small restrictions
-> no column lower bound yet.

## C-83 cyclic-to-acyclic edge

q endpoint-induced rule states
-> input-specific activation rank makes every witness path terminate
-> static graph may cycle; support arcs O(q^2+qN)
-> exact cyclic intersection D^circ_cap=rho
-> safe standard acyclic simulation O(q^3).

Open links: a joint residual lower bound beyond row signatures, or a better endpoint-aware acyclic simulation. No improved rho bound follows yet.


## C-84 common-core certificate

A fixed row signature class R
-> identical feasible output leaves for every w in R against fixed z
-> a common leaf coordinate lies among the coordinates fixed across R
-> the resulting cylinder contains no high z
-> at least N-log|SIZE(s2)| coordinates are fixed
-> any S-vertex rect-DAG induces a cover by at most 2^S high-free cylinders.

This yields S >= log C_cyl(Y,Z), but C_cyl <= |Y| and these cylinders may contain medium tables. The quantitative and fusion-transfer gaps remain open.


## C-85 cross-class separation

Row-signature class R x column-signature class C
-> identical feasible vertices and leaves across the whole product
-> one common output leaf is valid for every pair
-> common-coordinate cores K_R and K_C intersect at opposite bits.

Open link: lower-bound the class arrangement or transition/routing cost. The 2N output rectangles give an immediate small cover but not a shared acyclic DAG.


## C-86 failed universal scan

Coordinate scan plus merging equal-prefix histories into one full-product state
-> that node is valid for pairs with earlier mismatches too
-> suffix-only continuation fails the all-valid-vertices condition
-> exact prefix-equality region is a union of pattern rectangles
-> retaining patterns recovers the profile-state blowup.

This kills one construction; it does not prove a lower bound against all DAGs.


## C-87 linear-sketch barrier

Rank-r linear summary of N table bits
-> every fiber has size 2^(N-r)
-> if r<N-log|SIZE(s2)|, every fiber contains a high table
-> fixed linear fingerprints need N-o(N) rank.

## C-88 description-space bridge

Alice sends circuit description d
-> communication O(ell+log N), ell=O(s1 log s1)
-> shared interval comparison still needs restriction patterns u
-> profile rectangles are valid, mismatch-in-I itself is non-rectangular
-> no near-linear construction or universal lower bound yet.


## C-89 promise separator circuit chain

Rect-DAG for Mis(Y,Z)
<-> Boolean circuit h with h=1 on Y and h=0 on Z, up to constants
-> q-pair cover gives SepCirc=O(q^3)
-> SepCirc>N^(3+3epsilon+delta) forces q>N^(1+epsilon)
-> OPS magnification gives P!=NP.

Reverse stops at the promise separator because h may accept M. C-79 blocks direct conversion to a low-set fusion cover.

## C-90 ambient-universe correction

Full-domain cover \(\rho_{\rm full}\)
-> restrict endpoints to Z
-> promise-domain cover \(\rho_{\rm prom}\) with no larger q.

Mismatch rect-DAG of size L
-> promise separator circuit O(L) [C-89]
-> \(\rho_{\rm prom}\le O(L)\) [C-02].

A promise cover/DAG does not directly yield \(\rho_{\rm full}\): C-79's medium-generated semi-filter avoids every pair with endpoints restricted to Z. This gap is only for promise-to-full upgrade, not DAG-to-active-promise-cover.
## C-91 Ã¢â‚¬â€ SCC refinement of the q-to-DAG edge

A successful q-pair promise cover has q recursive states. Delete the automatic self-support incidences first; this preserves the least fixed point because any state that first activates must already have both non-self support predicates true. In the resulting loop-free containment-dependency graph, if SCC sizes are r_C and internal side-support incidences are e_C, SCC-wise evaluation yields an ordinary binary-fanin separator of size O(qN+q^2+sum_C(r_C e_C+r_C^2)). Thus the q-to-DAG edge is O(q^2+q d^2) for maximum SCC size d; it is O(q^2) for acyclic dependency, sparse SCCs, and d<=sqrt(q). The lower-bound branch now splits: exploit large dense SCC geometry directly, or use a strong separator lower bound against the improved compiler for small/sparse-SCC covers. Neither branch currently proves q>N^(1+epsilon).

## C-92/C-93 - Carrier-poset pruning and quotient

C-91 loop deletion -> C-92 delete strict non-cover supports on both sides -> retained two-sided cover edges force monotone activation along carrier inclusion -> same least fixed point.

C-92 loop-free recurrence -> C-93 group rules by equal carrier -> one recursive carrier bit per distinct T_i, while retaining each rule's own candidate conjunction -> exact least-fixed-point quotient.

For carrier SCCs C, with p_C carrier states, q_C candidate rules, e_C internal candidate-side carrier incidences, and e_out external incidences:

q-state recurrence -> quotient H on p distinct carriers -> SCC iteration -> separator size O(qN+e_out+sum_C p_C(e_C+q_C)).

This can improve the q-to-separator compiler when p is small relative to q. It does not remove q alternative conjunctions and does not imply a lower bound on q. O-92 remains: prove non-shareability for the dense carrier/candidate core or find a further correct compression.

## C-94 - Factor inclusion propagation and isolate feedback

C-92 pruned recurrence + C-93 carrier quotient
-> all proper-subcarrier supports are retained Hasse covers, shared on both sides
-> factor common \(K_t=\bigvee_{u\lessdot t}x_u\) from each candidate conjunction
-> remaining candidate inputs are one-sided escape supports \(u\not\subseteq t\)
-> any directed cycle must contain an escape edge.

Replace one Hasse-propagation round \(H_t=K_t\vee D_t\) by \(G(x)=\mathrm{Up}(D(x))\); H and G have the same fixed points. If s distinct carrier values are escape sources, the macro iteration has at most s+1 rounds. The separator compiler is O(qN+(s+1)(xi+kappa+q)), with xi escape side incidences and kappa Hasse edges. This is a proof-level localization, not a lower bound; next prove escape-alternative non-shareability or construct a compact escape router.

## C-95 - Final contradiction must use an escape source

Two direct seed clauses at an empty-carrier rule, if jointly satisfiable, remain true on a subcube of size at least 2^(N-2). Since the non-high class has M2<2^(N-2) members, that subcube contains a high table and would directly derive the empty carrier there. Therefore each empty-rule seed conjunction is unsatisfiable. Every low anchor must activate at least one carrier from S_0, the set of escape sources feeding empty rules:

\(Y\subseteq\bigcup_{u\in S_0}X_u\).

This pins the last step of every contradiction proof to a one-sided escape, but the activation sets may overlap heavily; no |S_0| lower bound follows yet.

## C-96 - Terminal-cone seed lower bound

C-95 successful empty-rule activation -> choose one support per side -> selected-predecessor ancestor cones -> high-free CNF -> at least N-log2(M2) true clauses -> |C(w)|>=(N-log2(M2))/2. Depends on C-03/C-91 activation semantics. Does not strengthen q>=N-o(N), and leaves overlap unconstrained.

## C-97 - Description-space invariance and exact DAG bridge

C-75 plain mismatch relation + surjection G:D1->Y -> lift/restrict along a section -> equal standard rect-DAG size on descriptions and truth tables.

C-78/C-89 rect-DAG <-> promise separator circuit -> rho_prom<=O(SepCirc)<=O(rho_prom^3). The q activation graph is cyclic and input-ranked, not standard acyclic rect-DAG; current acyclicization losses are C-91/C-93/C-94. C-97 universal-evaluator audit identifies range separation and rectangle validity as the unresolved sharing cost.

## C-98 - Conditional PRF benchmark for the shared-DAG branch

Assume nonuniform-secure PRFs with polynomial-size per-key evaluation circuits
  |
  | restrict the oracle to N=Theta(lambda^a) padded points; choose a so that a*beta > d
  v
PRF truth tables lie in Y; uniform truth tables lie in Z with probability 1-2^(-N+o(N))
  |
  | any SepCirc of size N^C becomes a poly(lambda)-size N-query distinguisher
  v
CONDITIONAL: SepCirc(Y,Z)=S_rect=N^(omega(1))
  |
  | S_rect <= O(rho_prom^3)
  v
CONDITIONAL: rho_prom=N^(omega(1)); the OPS fusion target follows

This is a conditional calibration only. The MCSP/PRF paradigm is established; no unconditional separator or fusion lower bound is added.

## C-99 - Audit the strength of the C-98 assumption

Nonuniform-secure PRF assumption
  |
  | C-98: rules out polynomial separators and forces rho_prom=N^(omega(1))
  | C-99: if NP subset P/poly, MCSP in NP gets polynomial circuits
  |        fixing threshold s2 gives a separator; N=poly(lambda) queries break PRF
  v
CONDITIONAL: NP not subset P/poly, hence P != NP

Thus C-98 is a conditional calibration, not an independent route to P != NP. Uniform PRF security does not apply to arbitrary nonuniform separator circuits.

## C-100 - Batched-frontier compiler refinement

q-pair cyclic cover
  |
  | C-94 quotient, escape-source iteration (s+1 rounds)
  | C-100 batches seed/support/up-closure ORs over shared blocks
  v
S_rect = O(qN/log N + (s+1)[q + min{xi,q(1+s/log q)} + min{p+kappa,p+p^2/log p}])
  |
  | coarse p,s<=q, xi<=2qs, kappa<=p^2
  v
S_rect = O(q^3/log q) for q>=N-o(N)

Reverse DAG-to-cover transfer: rho_prom<=O(S_rect). Therefore a separator lower bound asymptotically above N^(3+3epsilon)/log N would force q>N^(1+epsilon). This is only a compiler improvement; no lower bound is supplied.

## C-101/C-102 - Local structure tested; cross-instance reuse remains uncharged

C-96 terminal cones can be viewed as high-free coordinate cubes, but circuit counting bounds their dimension by O(s2 log(n+s2)) and recovers only the existing N-o(N) clause count. A localized input subcube witnesses contained-cube dimension Omega(s2), while C-80's block-constant family is not a coordinate subcube. C-102 gives a total fiber-disagreement relation: every high table cuts an edge inside a low table's two fibers. Its O(N^2) rectangle certificate cover is nondeterministic and provides no deterministic binary routing.

Thus neither candidate improves the quantitative chain. The shared-DAG frontier remains O-89/O-91: a direct cyclic non-shareability bound or an unconditional separator lower bound surviving the q-to-DAG loss.

C-103: S_fib -> O(S_fib) signed-mismatch DAG -> rho_prom <= O(S_fib). C-105 rules out small fiber DAGs using Omega(N^(2-beta)/log N) output labels, but this auxiliary lower bound does not transfer back because C-104 loses N^2. C-106: an O(q log^d N)-size universal fiber-edge set extracted from Q would force q=Omega(N^(2-beta)/(log N)^(d+1)); the extraction is open.

C-104 closes the reverse relation simulation at a loss: S_fib(Y^-,Z) <= O(N^2 S_mis(Y,Z)). Combining this with the C-100 q-to-mismatch compiler gives only S_fib <= O(N^2 q^3/log q), so proving q>N^(1+epsilon) through fiber hardness would require S_fib > N^(5+3epsilon)/log N. Use the fiber route only as an upper-bound falsification test.


C-105: every affine A of size a=Theta(s2 n) must induce Omega(a) edges of a fiber-DAG's output set, else a high z=1_(A\S) supported on isolated vertices has no valid leaf. Averaging gives at least Omega(N^(2-beta)/n) distinct labels/vertices. This is a genuine auxiliary relation lower bound, but the C-104 N^2 transfer makes it vacuous for rho. The unresolved dependency is a direct q-state-to-fiber-output map or an improved reverse simulation.

## C-106 - The fiber relation's small-DAG branch is closed, and the transfer gap is exact

C-105 rules out an N^(1+o(1))-size fiber-disagreement DAG by its required Omega(N^(2-beta)/log N) distinct edge labels. This closes the auxiliary relation's small-DAG falsification branch, but does not lower-bound mismatch because C-104 loses N^2.

A fiber witness needs two coordinates in a common w-fiber with opposite z-bits. C-75's cyclic witness path supplies a single signed mismatch coordinate; one agreement point can still lie in the opposite w-fiber. The exact open bridge is an extraction of a universal edge set E_Q from a successful q-state closure, with |E_Q|=O(q log^d N). If proved, C-105 would force q=Omega(N^(2-beta)/(log N)^(d+1)); no such extraction is established. Therefore keep the active proof target on direct cyclic-state non-shareability.


## C-107 - Pointwise pair lifts fail by a rectangle-complement argument

For a candidate fiber edge (a,b), the valid local pattern set is A x B, with A={00,11} for equal low bits and B={01,10} for unequal high bits. The promise realizes the full four-pattern sets on both sides. If separately computed local labels F(u),G(v) differ only on A x B, choose u0 outside A and v0 outside B. Equality on (u0,v0), (u,v0), and (u0,v) forces every F and G label equal, so no mismatch exists. Thus no pointwise encoded-table mismatch has only valid fiber outputs. This rules out the raw lift, but a DAG could still route around false candidates; any successful transfer must make that selection explicit.


## C-108 - The output list is nearly optimal; routing remains the barrier

Patching shows any high z differs from every unary postprocessing of low w on Theta(s2/n) or more points. A random graph with edge probability p=Theta(n^2/s2) hits every cut of size at least r on each low-w fiber, simultaneously for all low w by a union bound over 2^(O(s2)) rows and all fiber cuts. This gives a universal fiber-edge list of O(N^(2-beta)n^2) labels. Together with C-105, the minimum universal answer list is between Omega(N^(2-beta)/n) and O(N^(2-beta)n^2), within O(n^3).

The edge list is not a rect-DAG: after candidate i fails, the surviving input pairs satisfy a union of Alice-failure and Bob-failure rectangles, generally not one rectangle. A suffix state forgets which party rejected each prior edge and can skip the only valid answer. Direct row enumeration gives a correct but exponential O(2^(O(s2))N^(2-beta)n^2)-vertex DAG. The next issue is exactly deterministic sharing/routing, not existence or size of a nondeterministic certificate list.


## C-110 - Product-hull non-shareability condition

Rect-DAG state semantics require every pair in each node rectangle to have a descendant valid output. When several histories merge, the node rectangle contains their product hull and all cross-pairs. Thus the descendant output coordinates separate the row and column projections. This rules out forgetting distinct equal prefixes before a suffix-only scan. For fusion rule rectangles, first-activation rank gives the corresponding reachable-output separation. No q lower bound follows until the size or incompatibility of these output sets is quantified on actual low/high instances.


## C-111 - Promise-level cross-context incompatibility, with adaptive escape

A counting argument for \(\beta<1/2\) supplies a mask p on each block's suffix domain such that p and its complement exceed \(s_2+O(k)\). Off-diagonal splices of C-80 block-constant low tables along the p-mask are high, and each splice matches the first row on the complementary coordinates. Therefore exact p-pattern contexts cannot merge into a suffix-only rect-DAG state. The result is specific to prefix-first routing: the shared block partition gives an O(N) adaptive mixed-block DAG, so the construction also demonstrates why local incompatibility is not yet a global DAG lower bound.


## C-112 - General distance-code splicing lemma

A uniformly random coordinate split turns any pair of codewords at distance d into a uniform one of 2^d splices. If d>2log K+log|SIZE(s2)|, a union bound ensures one split makes every off-diagonal splice high. A constant-distance subcode of block-constant low tables has exponential-in-s1 size and distance Omega(N), meeting this condition for every beta<1. This forces exponentially many states only for a prefix-first router with suffix-only outputs; adaptive block search remains O(N).


## O-99 - Adaptive partition diversity is the remaining gap

C-112: random coordinate splicing makes every off-diagonal hybrid of a separated low code high and proves a large state requirement for prefix-first/suffix-only routing. C-80: the same low family has a linear-size adaptive mixed-block DAG. Therefore the next lower-bound target is a family of low circuit partitions with no shared adaptive witness, or a direct cyclic-state invariant. No conclusion about rho follows from static splice incompatibility.


## C-113 - Essential-variable support is an adaptive common witness

For low k-juntas, Alice's irrelevant-variable set has size n-k. A high z has more than k essential variables, so Bob's essential-variable set intersects it. A count-state PLS on balanced intervals finds a shared direction; per-direction edge trees then locate a z-boundary edge on which w is constant. This yields an O(N polylog N) rect-DAG for all k-juntas versus high z. Thus varying supports alone are not a non-shareability source; hardness must remain inside essential-variable sets.

## Q75 - Reusable count-intersection PLS template

C-114 abstracts C-113. If each input pair gives local sets \(A_x,B_y\subseteq[n]\) with \(|A_x|+|B_y|>n\), balanced interval states store their exact counts and descend to a common element. This yields an acyclic PLS of O(n^2) states and O(log n) communication per step, hence an n^{O(1)} rect-DAG. A valid suffix can be shared once per output index if its full product rectangle solves the relation.

**Use and boundary:** search for alternative low-circuit/high-table witness sets satisfying the cardinality condition or another similarly compact PLS invariant. The irrelevant-variable instantiation fails for parity, already a low all-essential function. This closes only that simple generalization; it does not close O-99/O-93.

## C-115 dependency: gate-signature fibers

C-115 uses circuit evaluation plus a small truth-table lookup: if z is constant on the joint values of k selected low-circuit wires, z has a circuit of size \(s_1+O(k2^k)<s_2\). Therefore a high z varies inside one low-circuit signature cell, and patching gives \(\Omega(s_2/n)\) total minority mass. This supplies a candidate structural witness for O-101 but not a routing bound. The cells depend on the circuit; C-114's cardinality PLS does not apply, C-97 blocks syntax-only savings, and C-80 is the adaptive counterexample that any lower bound must survive.

## C-116 dependency: hard cofactor, lost gap

A table of size \(>s_2=cns_1\) must have one of \(m=\Theta(n)\) fixed-prefix cofactors of size \(>4s_1\), since otherwise muxing the cofactors gives a size-\(<s_2\) circuit. Every low row restricts to size \(\le s_1\), so Bob can choose a hard cofactor and solve a smaller constant-gap mismatch instance. This proves only \(S_{\rm large}\le O(n S_{\rm constant-gap})\), not the reverse. A hard marker in the unused cofactors creates a mismatch that can bypass the embedded instance. O-102 asks for a gap-amplifying reverse bridge.

## C-117 dependency: parameter padding

For unchanged absolute thresholds, ignored-input lifting gives \(S_{n-k}\le S_n\) exactly. Reparameterization changes \((\beta,c)\); fixed \(\beta'>\beta\) gives \(N'=N^{\beta/\beta'}\) and exponent loss \(\beta/\beta'\). This is only useful if a lower bound at the shifted parameters has enough margin and uniformity. Keep separate from C-116's upper reduction to the weaker \(4s_1\) cofactor promise.

## C-118 dependency: filter pullback transfers the cyclic cover directly

Restrict a big pair list to the lifted smaller high domain. Any small semi-filter counterexample pulls back under \(A\mapsto A\cap Z^\iota\) to a proper big semi-filter containing the lifted anchor slices and preserving the big pairs. Hence \(\rho_{\rm small}\le\rho_{\rm big}\) with no acyclicization loss. This differs from C-117's rect-DAG padding and gives a direct route across nearby \((\beta,c)\) values if a uniform lower bound is available.

## C-119 dependency: exact parameter ray, with no quantifier shortcut

For lambda=p/q>1, dimensions n=pt,n'=qt, and (beta',c')=(lambda beta,lambda c), the OPS thresholds match exactly under C-118. A source exponent 1+eta becomes (1+eta)/lambda; target exponent 1+epsilon needs eta>lambda(1+epsilon)-1. The OPS universal-small-beta condition survives only from a uniform source interval at fixed shifted c, not from one point. At c'>c0, the smaller low class is already monotonic-hardness stronger than the c0 class at the same beta, so padding does not create extra leverage. For infinitely-often statements use an aligned source subsequence; rounded thresholds need separate robustness. Source cover pairs allow empty endpoints; restricted vacuous pairs may be deleted in variants that forbid them.

## C-120 dependency: gate-signature mass has a one-cell extremizer

For kâ‰ˆ(1/2)log s2 selected wires, a largest signature cell has |F|â‰¥N/sqrt(s2). If beta<2/3, this exceeds log|SIZE(s2)|=O(s2 n). Among the 2^|F| completions agreeing with w off F, at least one is high and nonconstant on F because the two constant completions have size s1+O(k). Patching forces Omega(s2/n) disagreements, all inside F. This disproves any strengthening of C-115 to many mixed cells, so multiplicity alone cannot be a lower-bound charge. It does not rule out a count-state router with a new Alice/Bob-local encoding. The adaptive cost of identifying F across circuit-dependent partitions remains open.

## C-121 dependency: common partition is an O(N) escape only for structured rows

If all low tables are constant on a fixed partition with m cells and its label map plus m-bit lookup costs below s2, every high table is mixed on one cell. Bob finds that cell, Alice gives her common cell bit, and Bob finds the opposite high bit; the total rect-DAG has O(N) vertices. This generalizes C-80. The full SIZE(s1) class contains every point indicator, forcing any common partition to be discrete; hence it has no such useful common partition. C-120/C-121 together isolate the live difficulty as adapting across low-row-specific partitions.

## C-122 dependency: small row sets are jointly easy

For r<=eta n fixed low rows, their r-bit output signature has at most 2^r fibers. A high table constant on all fibers would have size r s1+O(r2^r)<s2. Thus every high column is mixed on a fiber common to all r rows. Applying C-121 yields an O(N)-vertex rect-DAG on that row family. This rules out O(n)-row incompatibility as a direct lower-bound source. Extending the suffix to rows outside the fixed family is the unproved global-sharing step; separate grouping costs O(N|Y|/n).
## C-123 â€” Description syntax does not lower DAG size

Circuit-description inputs and truth-table inputs have exactly the same minimum mismatch rect-DAG size by pullback and section. S_rect is Î˜ of the minimum Boolean promise-separator circuit size C_sep. Direct enumeration yields O(NÂ·2^ell), ell=O(s1 log(s1+n)); a universal evaluator does not remove the existential description quantifier. This closes the syntax-only universal-DAG idea but gives no lower bound. A rect-DAG lower bound transfers to rho with constant loss in the reverse direction; a q-pair list only yields the known O(q^3/log q) DAG upper bound.
## C-124 â€” No current transfer from adjacent MCSP results

The 2026 conditional Gap-ImpMCSP result changes the input representation to a succinct sampler; the project's S_rect is on explicit truth tables. Austrin-Risse SoS bounds concern per-table refutation degree. Neither maps to a lower bound on C_sep, S_rect, or rho_prom without a new quantitative reduction.

## C-125 dependency: compose the closure separator before acyclicizing

A q-pair list induces a cyclic monotone separator H_Q with q AND gates. If a monotone map phi has a AND gates, places a low table code below every YES image, and keeps every NO image below a high completion, then H_Q composed with phi computes f and CycAnd(f) <= q+a. This bypasses the q-to-rect-DAG loss, but requires a cheap partial-table encoding. Triangle OR-only maps are impossible once the cyclic lower bound exceeds N; the naive triangle witness map costs O(r^3) ANDs versus Omega(r^3/log^4(r)). No Gap-MCSP instantiation is known. Keep separate from C-75 DAG non-shareability.


## C-126 dependency: separate low-code recognition from high completion

Define LowExt_Y(u) iff some e(w), w in Y, is <=u. Under C-125, f=LowExt_Y composed with phi: on NO, any low code below phi and high code above phi would force equal full tables. Still require a high completion on each NO image because medium values of H_Q are unconstrained. Thus O-107 is a reduction-cost problem plus a separate completion problem. NO images are consistent; YES images may carry conflicts beyond a selected low code. This does not yet produce a cheap map or a q bound.

## C-127 dependency: low-code diversity is carried by conflict rails

For yes inputs x,y, selected low table codes e(w_x),e(w_y) both lie below phi(x OR y). Any coordinate where the codes differ is therefore a conflict at that join. If all YES conflicts lie in a delta-coordinate set S, all witnesses agree outside S; enumerating at most 2^delta candidate tables gives an acyclic circuit for f of AND count <=a+N+delta*2^delta. Hence a direct transfer beyond N^(1+epsilon) needs delta at least (1+epsilon)log N-O(log log N). The consequence constrains phi, not q. O-108 asks how to exploit conflict incidence or construct a map at the threshold.

## C-128 dependency: promise tree lower bounds have no automatic q transfer

Local-PRG MCSP lower bounds extend to Gap-MCSP promise separators because the proof uses rejection on uniform high tables and acceptance of locally generated low tables; medium behavior is irrelevant. For fixed beta, the direct bounds are N^(3beta-o(1)) for de Morgan formulas above 1/3 and N^(2beta-o(1)) for arbitrary-basis formulas/BPs above 1/2. They are not superlinear throughout OPS's sufficiently-small-beta interval and formula/tree size is not rect-DAG size. O-109 needs either a sharing-preserving simulation or a PRG lower bound for the DAG model itself.

## C-129 dependency: shared-state signature-volume constraint

For any rect-DAG state v, let K_v be its descendant output coordinates. Validity requires disjoint K_v-projections of its row and column sets. If there are r distinct row signatures and |K_v|=k, every signature excludes at least 2^(N-k)-M2 high tables from B_v when positive. This gives a local quantitative non-shareability condition. It does not sum globally because excluded high tables can overlap across states and the protocol may adaptively shrink B_v. The plain mismatch relation also has an Omega(log N) deterministic communication lower bound and an N^(1-beta-o(1)) leaf fooling family from disjoint high supports, both below the existing Omega(N) rect-DAG floor implied by rho_prom. Current q compiler loss and target remain unchanged.

## C-130 through C-136 dependency update: overlap, routing, and witness density

C-130 falsifies unweighted summation of excluded-column volumes because one high column is excluded at Omega(N) reachable restriction states. C-132 falsifies width-only per-node capacity: filtering columns can leave all low rows in one intermediate-width rectangle. C-133 kills the specific interval-plus-exact-restriction universal DAG by local surjectivity, while C-134 shows that local richness alone is not hard when a common mismatch region remains. C-135 identifies the complementary easy-state condition: row variation on at most Theta(s1) coordinates guarantees a Bob-side common-mismatch scan. These claims leave a global routing problem; neither side of the variation dichotomy gives a state count.

C-136 follows by applying C-135's point-patching estimate to each low/high pair: their Hamming distance is at least d+1=Theta(s1). Consequently the standard labelled mismatch rectangles have fractional-cover cost 2N/(d+1), label-conflict fooling sets have size at most 2N/(d+1), and public-coin coordinate sampling has expected cost O(N/d). C-131's completion count gives the opposing fixed-sample fact: every universal nonadaptive coordinate set needs N-o(N) positions. Together these establish that witness scarcity and fixed samples are the wrong resources; the remaining unknown is deterministic rectangle-preserving adaptive-state reuse. O-116 records the proof obligation. No bound in this chain improves rho_prom>=N-o(N), the S_rect<=O(rho_prom^3/log rho_prom) compiler, or the P-vs-NP status.

C-137 tests the apparent cyclic O(N)-state pair scanner against the model boundary. Its equal-bit merge combines two diagonal rectangles, so it is not a legal rect-DAG transition. Preserving fixed-order equal-prefix contexts yields 2^k nonempty states for k=Theta(s1/n), because every such prefix is both low-realizable and high-completable. This kills that scanner architecture but not adaptive semantic DAGs. O-117 keeps the model-transfer requirement explicit: generic joint-input transducers, standard rect-DAGs, and cyclic fusion closure have distinct semantics until a quantitative simulation is proved.

C-138 improves C-129's disjoint-output family: sphere counting and a random partition give Omega(N/s2) high support tables on disjoint coordinate blocks, hence D_cc >=(1-beta)n-O(1). This still gives only a sublinear number of leaves and is weaker than the existing Omega(N) rect-DAG floor. C-136 caps label-conflict families at O(N/s1), so the gap between the best explicit packing and that ceiling is Theta(n); O-118 retires this route as a superlinear DAG strategy.


## C-139 dependency: successful closure gives a ranked cyclic rectangle search

C-74's least-fixed-point activation sets define one valid rectangle per rule. A successful cover makes empty-carrier rule rectangles cover Y x Z; each pair then follows a literal mismatch or a strictly earlier-activated predecessor. This produces a rectangle-preserving cyclic search graph with q rule states, O(q^2+qN) support arcs, and per-pair termination. Rank threshold layering plus binary support routing costs O(q^2(q+N))=O(q^3), which does not improve the current O(q^3/log q) standard-DAG compiler. The unresolved dependency is a rank-sharing theorem or an actual-promise no-merge lemma. The tree/DAG order is S_DAG<=S_tree; communication bits alone only give an exponential tree-size bound. This adds no q lower bound.


## C-140 dependency: rank-preserving simulation is not a separator lower bound

The two-state monotone recurrence x1=(s1 OR x2) AND c, x2=(s2 OR x1) AND c has input-dependent activation order but simplifies to the acyclic output c AND (s1 OR s2). This blocks the inference from q^2 rank-layer states to a lower bound on S_rect. To use the ranked cyclic protocol, prove that every separator (not only the selected C-75 witness-path simulation) must retain the relevant contexts. The example is abstract; legal endpoint realization and promise transfer remain open.


## C-141 dependency: legal cyclic support does not force hard output routing

The C-140 rank-reversing recurrence is realized by actual endpoint intersections on a five-bit Boolean cube: carriers P union {p1} and P union {p2} support one another on the E sides while distinct markers prevent cross-support on the H sides. The resulting closure is input-ranked and cyclic, but its output simplifies to c AND (s1 OR s2). This confirms the model phenomenon and simultaneously blocks using rank-layer count as a DAG lower bound. The missing dependency is a successful cover/promise construction whose separator cannot simplify away the cycle.


## C-142 dependency: a successful cyclic witness can have a tiny separator

C-141's two-state cycle extends to a successful three-pair cover of a finite promise: the nonempty states feed a disjoint-endpoint empty rule, and activation rank reverses across the two low anchors. The output set is still recognized by h=c AND (NOT a OR NOT b), a constant-size separator. Hence successful cyclic support is possible, but path-preserving rank layers do not lower-bound the minimum separator. Any transfer to Gap-MCSP needs an output-level obstruction, not merely a cyclic support SCC. Q101 closes for toy existence; Q102 remains.


## C-143 dependency: large input-ranked SCCs still admit small output

For every q, a finite promise pair list can realize one q-state support cycle with q low anchors inducing all cyclic rotations as first-activation orders. The rank-layer protocol has Theta(q^2) distinct state/rank rectangles, yet the promise separator is h=c AND OR_i t_i with O(q) gates. This blocks a lower-bound transfer from C-75 path layers to S_rect. The next requirement is an OPS-specific hardness argument against every separator, not a generic cyclic-rank count.

## C-144 dependency: deletion-minimal witness lists need not approximate rho

The q-state C-143 cyclic list is deletion-minimal, yet a separate pair E*={z_i}, H*={r} covers the same finite promise, so rho_prom=1. The rank-layer protocol has Theta(q^2) rectangles while the optimal cover has one pair. Therefore state-count arguments must target minimum cover size directly and quantify over alternative semantic endpoints. No superlinear rho or OPS result follows.

## C-145 dependency: bootstrap states are broad on the high side

Every successful closure has a round-one seed state on each low anchor. Since any two literal constraints consistent with a low anchor have a high completion in the OPS promise, the state carrier contains a full high cylinder of size at least 2^(N-2)-M2; each such high anchor activates that state too. Thus any eventual separation is a later-support routing/shrinking phenomenon. This is an exact local constraint, not globally chargeable yet; O-119 asks for a potential robust to overlapping high regions and adaptive filtering.

## C-146 dependency: cofactor drops are not additive

A seed pair fixes a cylinder on which its state is constant 1, allowing that state to be removed from the restricted recurrence. But many hard cofactors can share the same O(r)-size exact-one circuit: each 00 two-bit cofactor has rho at least r-3, while the global exact-one promise has rho=Theta(r). Therefore no direct-sum lower bound follows from local cofactor complexity alone. O-120 asks for an OPS-specific obstruction to this kind of reuse.

## C-147 continuation dependency: preserve the shared-DAG frontier

The primary-source re-audit confirms that Sokolov/GGKS rect-DAGs are acyclic rectangle games with free local input predicates, while Cavalar--Oliveira's exact fusion identity is cyclic intersection complexity. The descriptor map D->Y preserves minimum standard DAG size by lift/restrict; universal evaluation of G(d)_k therefore supplies no topology compression. Current chain: rho_prom=D^circ_cap, rho_prom<=SepCirc=Theta(S_rect)<=O(rho_prom^3/log rho_prom). No near-linear full-promise DAG or arbitrary-DAG lower bound is known. Fixed scan and syntax-only shortcuts are closed; continue at O-121, requiring any route to survive C-110/C-130/C-132/C-135/C-143/C-146.

## C-148 dependency: local-PRG formula bound is not a DAG bound

The promise-specific CLKM argument applies only for beta>1/3: its formula PRG is stated for t>=N, and lambda(N)=N^(1/3+o(1))<=s1 only above that threshold. It yields t>=N^(3 beta-o(1)) there, with arbitrary medium-band labels handled by circuit counting. For beta<=1/3 the cited lemma gives no such bound. At every beta the result is only a formula bound and does not constrain S_rect without a separate DAG transfer; C-148/C-149 leaves O-121 intact.

## C-150 dependency: first-missing carrier scan

In a successful Q, for each (w,z) in Y x Z choose the active state of minimum first-activation rank whose carrier omits z. A support on the endpoint omitted by z would be an earlier-ranked active carrier also omitting z, contradiction; hence that endpoint is seeded by a matching literal and yields a coordinate mismatch. A scan in activation order is therefore correct as a path algorithm. Its round-t continuation relation is row-dependent through the residual intersection P_t(w) of prior carriers. Merging these histories may create cross-pairs outside the actual continuation relation, so this does not yet give a standard rect-DAG. q^2 rank/state contexts and output routers can recover the known cubic-scale compiler. No arbitrary-separator lower bound follows; see O-122/O-121.

## C-151/C-152 dependency: canonical selector versus multivalued output

For A_S=[k]\\S and B_T=T union {k}, the least common element requires 2^(k-1) k-labelled rectangle leaves: distinct diagonal pairs cannot share a k-rectangle because a cross-pair then has a smaller answer. Accepting any common element collapses the same problem to constant output k. More generally, a rect-DAG for a multivalued relation transfers to canonical selector h at equal size if h is constant on each output leaf rectangle; an output-label decoder is sufficient. The signed-mismatch output does not include C-150's carrier index, so this transfer is unproved. This is a route-calibration result only; it does not lower-bound OPS rect-DAGs or cyclic fusion covers.

## C-153 dependency: successful fusion still permits selector-mixed mismatch leaves

In C-142, the rectangle {wA,wB} x {p1,p2} has c=1 on every low and c=0 on every high, so c is a valid common mismatch output. Yet the first-excluded carrier is state 2 on p1 and state 1 on p2. This is an actual successful fusion toy with a valid selector-mixed rectangle, defeating any generic implication from the cover to leaf homogeneity. An OPS-specific restriction might still recover a selector, but absent one this branch does not support O-121. No full-promise lower bound follows.

## C-154 dependency: lifted CSP DAG lower bounds need an output-preserving embedding

The CCC 2025 colourful-sunflower lifting theorem gives rect-DAG size at least (m/(A|Sigma|w(S)log(mn)))^w(S) for Sâˆ˜Ind_m^n. Pulling back rectangles under separate Alice/Bob maps preserves rectangle geometry, so the missing bridge is semantic: every mismatch leaf must decode to a constraint violated throughout its pulled-back rectangle, with quantified refinement overhead. The low table must lie in SIZE(s1), the high table outside SIZE(s2), and source cardinalities must fit length N. No maps are known. To imply q>N^(1+epsilon), the transferred S_rect lower bound must exceed N^(3+3epsilon)/log N under the present compiler. This literature result is a promising template, not an OPS bound.

## C-155 RETRACTED: partial Index inputs void the claimed no-go

**Retraction.** SearchORâˆ˜Index is partial: pairs with y_x=0 are outside its legal domain, so the reduction imposes no constraint on their codewords. On legal pairs, a(x)=0^m and b(y)=y works, since y_x=1 guarantees a mismatch and the sole source output is 1. The false no-go has been withdrawn; the replacement criterion is C-156.

**C-156 criterion.** For a total source relation, fixed-decoder partywise codes are exactly paired cuts: each coordinate's mismatches are X_t^0 x Y_t^1 and X_t^1 x Y_t^0, each with a fixed valid output label, and all pairs must be covered. This is an exact characterization of coordinatewise embeddings, not a lower bound on their number or a transfer to OPS.

**C-157 cyclic-loop check.** A cycle of full-root rectangles, each with one signed-output leaf and one continuation edge, has a finite accepting route for every pair but also infinite routes. Existential finite-path semantics trivializes total search, so cyclic protocols need well-founded progress. Fusion provides pair-dependent activation-rank descent; arbitrary joint mismatch loops do not.

**C-158 binary cover structure.** If two child rectangles cover A x B, then A subset A_0 or B subset B_1 (after intersecting with the parent). A standard binary Boolean-game node therefore permits a locally deterministic choice by one party. This is local and gives no state-count lower bound. O-126 is the open dependency: combine the full-side property with C-129's high-column exclusion without double-counting, and survive C-132's filtered child.


**C-159 model audit.** Sokolov's Theorem 3.2 proof already contains the stronger rectangle trichotomy behind C-158, with AND/OR/copy circuit semantics. C-158 is therefore not a new non-shareability tool. O-126 is now specifically a search for a global charging theorem over these gate/state classes, with C-130/C-132 as counterexamples to raw local counting.

## C-160 dependency: generic local statistics are not enough

A symmetric two-tail Hamming-threshold promise can match the low/non-high cardinality exponents, local pattern richness, high-cylinder completion, Hamming separation, coarse patch stability, complement symmetry, and closure under arbitrary coordinatewise Boolean recombination of O(n) low rows used by C-129/C-133/C-135/C-136, while having an (O(N\log N)) separator. Thus the C-129 state inequality plus Sokolov's local gate trichotomy cannot yield a superlinear DAG theorem from those generic inputs alone. Any successful O-126 argument must identify a finer property specific to the circuit-complexity promise or work directly with its ranked cyclic closure.

## C-161 dependency: balanced low functions still admit a simple range test

Adding every affine truth table to the low side and its radius-a neighborhood to the non-high side preserves the subexponential count and cylinder scales. Nearest-affine distance is computed by a Walsh-Hadamard transform of size O(N log^2 N), so balanced outputs and affine symmetry alone do not force a large separator DAG. C-161 does not preserve closure under arbitrary size-s2 compositions of the input-literal basis; the unresolved structural candidate is interaction among many such bases, beyond the O(N) router for any one O(n)-row family (C-122).
## C-162 - Description and basis audit

C-162 uses the C-78 exact mismatch relation and C-97 description-space lift/restrict identity; it reaffirms the C-100 q-to-rect-DAG compiler and C-90 reverse map. The affine-subfamily upper bound uses Walsh-Hadamard affine membership. It narrows Q120/O-126 by ruling out raw GL(n,2) basis counts and affine-orbit multiplicity as non-shareability charges. Remaining dependency: prove an OPS-specific incompatibility across nonlinear composition residuals, or lower-bound the cyclic cover directly. No bound is added.

Composition constraints must respect \(\Gamma_{\rm prom}=Y\sqcup Z\): outputs only known to be in \(\mathrm{SIZE}(s_2)\) can be medium, where the mismatch DAG is unconstrained. A useful basis route must either generate low rows or prove a new medium-band transfer.

## C-163 - Output-cover capacity for mismatch reductions

Every (w,z) in Y x Z has at least Delta=Theta(N^beta/n) differing truth-table coordinates. In a partywise reduction from a total source search relation, if every signed mismatch type has at most r output-labelled decoder terminals, then each source pair's valid-output set must contain decoder capacity at least Delta. Counting the 2N types yields chi_out*(R) <= 2Nr/Delta=O(r n N^(1-beta)). This strengthens the O-124/O-125 feasibility audit for fixed-decoder or bounded-refinement transfers. It does not constrain non-mismatch reductions and gives no lower bound on the target DAG or fusion cover.

## C-164 - Index geometry constrains mismatch-decoder leaves

For Search(cPHP(G)) composed with Index_m^k, a fixed-output pigeon-pair rectangle has uniform product measure at most 1/(m^2 d) when G is simple of degree d: Alice's pointer-pair support is S subseteq [m]^2; every edge in S imposes a partial-matching constraint on the corresponding Bob array cells, and the constraint graph yields measure at most d^(-rank). The component edge count implies |S|<=d^(rank-1). Since every OPS low/high image pair has Delta=Theta(N^beta/n) mismatches, a decoder with r source-valid rectangle leaves per signed mismatch type must pay r>=Delta m^2 d/(2N). This is an explicit reduction-cost constraint; it is not a target lower bound and may be smaller than the lifted DAG bound by a large factor.

## C-165 - cPHP output density rejects fixed signed decoders

For fixed x in Search(cPHP(G)) composed with Index_m^k, each output pair (p,q) is valid on at most a 1/d fraction of uniform Bob inputs. A table coordinate with both Alice bit classes nonempty has two Bob-side mismatch classes; if each signed type has r valid decoder leaves, each class has measure at most r/d, forcing r>=d/2. If r<d/2, all Alice code bits are constant; a balanced Bob input y* then makes each output valid on at most 1/d of Alice inputs, so no active mismatch type can be decoded across all x. Thus no fixed decoder can map the full signed mismatch relation for d>=3. The CCC one-sided mKW decoder does not meet this interface. Input-aware refinement remains open, with the additional C-164 distance cost.

### C-166 dependency update

short descriptions d --surjection lift/section restriction--> same rect-DAG size as Y x Z (C-97/C-123)
high-extension count + point-indicator expressiveness --C-110 product-hull / C-133 profile count--> interval-router nonmerging (C-166 re-audit)
interval-state nonmerging --X--> arbitrary rect-DAG lower bound (missing O-127 normalization; alternate coordinate outputs remain possible)
successful fusion cover q --ranked cyclic rectangle game--> O(q^3/log q) acyclic rect-DAG (current compiler)
rect-DAG lower bound > N^(3+3epsilon)/log N --current compiler--> rho_prom > N^(1+epsilon)

### C-167 dependency update

C-160 threshold calibration --all patterns on |I|<=a have both low and high extensions--> 2^a nonmergeable interval contexts
threshold separator circuit O(N log N) --Sokolov circuit/game correspondence--> arbitrary rect-DAG O(N log N)
therefore generic arbitrary-DAG -> interval-router normalization --X polynomial size overhead
actual OPS-specific normalization --? requires a property beyond C-160/C-161 statistics

C-167 prunes the generic O-127 branch only. It does not change the OPS transfer chain or establish a Gap-MCSP lower bound.
C-168: row-only candidate sample S(w) --cylinder count--> |S(w)| >= N-log|SIZE(s2)| = N-o(N)
Bob-dependent rectangle routing --?--> only untested compact mismatch-DAG path

C-168 is a strategy-class no-go, not a bound on shared-DAG vertex count.

## C-227/C-228 dependency update: context splicing is exact but not universal

least-fixed-point fusion recurrence --finite proof trees and minimal-support grammar (C-227)
shared state occurrence --context support K x replacement support C -- valid accepting support K union C
consistent K union C -- full cylinder accepted -- must be contained in the non-high set

For actual Gap-MCSP, force a consistent splice fixing fewer than N-log|SIZE(s2)| coordinates -- high extension -- contradiction (open O-151)

Artificial total promise W versus complement -- q-description counting -- superpolynomial native readout for some random W subset of easy tables (C-228)
independent W -- every consistent certificate fixes all N bits -- safe splices only land back in W

C-228 blocks generic inference from certificate width/anchor count to dangerous splicing; the remaining dependency must use actual SIZE(s1) versus CC>s2 geometry. No actual-promise lower bound follows.

## C-229 dependency: the direct selector grammar's first broken implication

small-circuit low-table membership -- existential description d + N universal bit checks --> certificate grammar with one branch per d

share coordinate-check states across descriptions --X--> checks still refer to one common d (native grammar cross-products side supports)

retain description identity in state --safe--> description-indexed copy cost

semantic quotient of partial descriptions with sound cross-products --?--> N polylog N native cover OR superlinear class count

No quotient theorem is known; C-229 is a construction failure, not a lower bound.

## C-230 dependency: exact safe-cylinder geometry

consistent accepting support C --cylinder lies in SIZE(s2)--> N-r(C)<=kappa_square(s2)

circuit counting --> kappa_square(s2)<=O(s2 log s2)
Lupanov synthesis on a fixed input-prefix block --> kappa_square(s2)>=Omega(s2 log s2)

therefore kappa_square(s2)=Theta(s2 log s2) at fixed-beta OPS scales

O-151 splice target --consistent union with >kappa_square free coordinates--> high extension and contradiction

Certificate width is tight up to constants; global sharing, not a sharper generic width floor, must carry any new bound. See C-230.

C-232 arbitrary KW function -- `O(N)`-bit mismatch protocol and `Omega(2^N/N)` rect-DAG by circuit counting -- proves short communication/output alphabet do not generically compress shared DAGs

C-75 low-circuit descriptions `d` -- universal evaluator computes `G(d)_k` -- `exists d forall k` separator / `2N` mismatch-rectangle cover --X--> binary rect-DAG unless intermediate unions stay rectangles

description-space rect-DAG -- pullback by `G` (lift) / restriction to a section (retract) -- exact same minimum as truth-table-space

actual OPS product-hull residual separator charge O-152 --?--> `S_rect>N^(3+3epsilon)/log N` -- via `rho_prom<=O(S_rect)` and `S_rect=O(rho_prom^3/log rho_prom)` -- `rho_prom>N^(1+epsilon)`

## C-235 dependency: splice cubes and endpoint joins/meets

finite proof support S --signed-rail constraints--> Boolean interval Q(S)=[ell(S),u(S)]

support union S union T --interval intersection--> Q(S) intersect Q(T)
positive rails --OR--> lower endpoint ell; negative rails --AND of complements--> upper endpoint u

output proof interval --soundness--> every member, including both endpoints, lies in SIZE(s2)
context K + replacement C --compatible splice--> low endpoint join ell(K) OR ell(C) and low endpoint meet u(K) AND u(C)
multiple disjoint substitutions --compatible product--> low multiway join/meet (C-235)

small q closure covering SIZE(s1) --?--> either a compatible high ownership endpoint (contradiction) or a superlinear charge for safe endpoint/fingerprint structure

The arrows through endpoint safety are proved; the final global implication is open. C-228 singleton certificates and C-234's diagonal equality separator show that endpoint safety need not create a forbidden hybrid for arbitrary promises or restricted subpromises. C-230's `Theta(s2 log s2)` safe-cube dimension remains sharp, so this route's value is a new algebraic target, not a stronger width bound. See `research/C235_CUBE_INTERVAL_CALCULUS_FOR_NATIVE_SPLICES_2026-09-27.md`.

## Literature motif screened after C-235

CSP incidence expansion + local Boolean substitutions --proved by Austrin-Risse for their SoS MCSP framework / monotone-slice variants--> proof-system lower bounds

possible expander-overlap block construction --?--> global fusion endpoint-mixing charge

missing edges: hard monotone slice instance --?--> actual `SIZE(s1)`/`CC>s2` truth-table restriction; q-state fusion closure --?--> their monotone circuit or SoS measure with controlled loss. Do not infer the target lower bound from the paper. Source: [Austrin–Risse, CCC 2023](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2023.31).

## C-236 dependency: disagreement-selector profile cap

repeated low anchors `w_g,w_h` --disagreement set D of size Theta(N) for typical pair--> `2^|D|` possible owner masks

compatible context/subproof splice --endpoint z in SIZE(s2)--> `mu=(w_g XOR w_h) AND (z XOR w_h)` is a low-complexity selector; at most `|SIZE(s2)|=2^(o(N))` masks occur

q-state cyclic grammar --?--> bound on the number/structure of compatible masks across all low pairs --?--> either superlinear q or a near-linear full-promise construction

diagonal equality subpromise --O(N) separator--> only prefix-constant masks; this explains a safe restricted family and blocks a generic lower-bound inference. Proof of selector extraction/profile cap: `research/C236_DISAGREEMENT_SELECTOR_CAP_FOR_COMPATIBLE_SPLICES_2026-09-27.md`.

## C-237 dependency: local width audit closes

C-230 universal safe-cube upper bound `kappa_square(s2)=Theta(s2 n)` --typical repeated-anchor selector set contains matching-size structured cubes (C-237)--> no stronger local dimension threshold

free selector set geometry/description in q-state proof grammar --?--> global state charge or a compact realization preserving all low circuits

The C-237 constructions use Lupanov synthesis; they rule out strengthening O-153 by random-anchor free width alone. See `research/C237_SAFE_SELECTOR_CUBE_DIMENSION_2026-09-27.md`.

## C-238 dependency: whole-strategy cross-mixing

accepted x,y with common ranked witness topology tau --mix E seeds from x + H seeds from y--> acyclic mixed proof DAG

consistent mixed support --finite-proof semantics--> entire cube accepted --soundness--> low interval / safe disagreement selector (C-235/C-236)

q-rule recurrence --?--> structural limit on skeleton fibers --?--> a high compatible hybrid or superlinear q

raw count fails: at most `2^(O(q log q))` topologies, too many relative to the `2^(Theta(s2))` diagonal anchors when q>=N. See `research/C238_GLOBAL_WITNESS_SKELETON_MIXING_2026-09-27.md`.
## C-239 dependency: canonical ranks and exact state obligation

C-233 min–max activation ranks --activation rank alone loses the nonmaximal-side witness choice--> endpoint-realizable counterexample in C-239

both side-support minima at each state --deterministic seed/predecessor selection--> one canonical skeleton per side-rank profile --equal profile fiber--> global E/H cross-product (C-238)

fixed Q maps its 2q-bit seed signature to the canonical side-rank profile --at most 2^(2q) canonical fibers, not a count of every witness topology--> still too many for q>=N versus 2^(Theta(s2)) anchors--> no pigeonhole lower bound

shared state i --context K x replacement proof C--> output support K union C; if compatible, soundness --> free(K) intersect free(C) has size at most kappa_square(s2), else opposite rails conflict

legal endpoint-containment grammar --?--> q-sensitive extremal bound on these cross-families --?--> superlinear fusion lower bound or compact cover

Blockwise circuit-description residuals must preserve one common description across all blocks; no near-linear update representation found. Full derivation: research/C239_CANONICAL_RANK_FIBERS_AND_NATIVE_SPLICE_OBLIGATION_2026-09-27.md.

## C-241 shared-DAG priority and exact bounds

Mis_(Y,Z) total signed mismatch -> standard rect-DAG size Theta(C_sep(Y,Z)) by the promise KW/separator construction in both directions.

For every onto truth-table map G:D->Y: S_rect(Mis_G)=S_rect(Mis_(Y,Z)) (pullback through G; reverse by a section). Thus description length affects communication bits but gives no representation discount in DAG vertices.

rho_prom <= O(S_rect) <= O(rho_prom^3/log rho_prom); D_cap<=rho_prom^2; rho_prom=D_cap^circ. Therefore the generic rect-DAG lower bound needed to infer rho_prom>N^(1+epsilon) is S_rect>cN^(3+3epsilon)/logN. The rule-SCC compiler gives O(qN+q^2+q d^2) and improves to O(q^2) only under d<=sqrt(q); carrier/escape compilers are also instance-sensitive. No worst-case near-lossless q-to-DAG compiler is proved. O-152 is active at global product-hull-safe sharing or a near-linear separator. See research/C241_SHARED_DAG_DESCRIPTION_INVARIANCE_2026-09-27.md.


## C-242 — Native certificate/blocker interaction

q-state positive recurrence --least finite proof semantics--> antichain certificate grammar C_i (height <=q)

shared state i --outside context K + arbitrary replacement support C--> accepted support K union C

consistent support --interval law--> [ell_K OR ell_C, u_K AND u_C] subset SIZE(s2), free dimension <= kappa_square(s2)

high table z --choose false side at each inactive state--> blocker map --follow ranked low proof--> path in A_w\\A_z ending in a mismatching seed literal

blocker maps + context/replacement interval join profiles --?--> q-sensitive global charge or compact full-promise cover

No q-charge is proved: pairwise paths can be short; compatible joins can remain low; C-228/C-234 remain hostile checks. Active priority is O-153 native closure; O-152 standard DAG is secondary. See research/C242_NATIVE_CERTIFICATE_ANTICHAIN_AND_BLOCKER_PATH_2026-09-27.md.


C-242 fixed-order upper cover:
low class Y --realized prefixes pi_t(Y)--> native intersection carriers T_p
T_parent + next signed literal --one legal pair rule--> T_p
length-(N-1) prefix of low w --both completions have complexity <=s1+O(n)<s2--> T_p=empty
therefore q<=sum_{t=2}^{N-1}|pi_t(Y)|<=N|Y|

uniform Theta(s1) shattering + dense high complement --every pattern cylinder has high completion--> fixed-order trie size >=2^(Theta(s1))

This rejects the fixed-order prefix trie as the near-linear cover, not adaptive or non-prefix closure programs. See C-242.


C-243/C-244 native global profile:
finite proof C at state i --> U intersect Cyl(C) subset T_i --> carrier-volume and disjoint-cylinder packing bounds (C-243)
context family K_i + replacement family P_i --> exact state zone Z_i=[K_i] intersect [P_i]
output acceptance --> union_i Z_i; soundness --> every Z_i subset SIZE(s2) (C-244)
joint generation complexity of (K_i,P_i) --?--> q >= N g(N), g(N)->infinity
or a compact native construction of all zones --> q=N polylog N / N^(1+o(1)

The unresolved edge is the quantitative one: no per-zone low-circuit capacity bound is known, and predecessor carrier volumes need not multiply because they can be correlated. C-228 and C-234 rule out generic zone-count or splice-only charges. Continue O-153; O-152 remains secondary. Full proofs: C-243 and C-244 reports.


C-244 state-zone cover --mark one proof occurrence as a hole--> C-245 paired antichain grammar (ordinary proof P plus one-hole context K)
context path cycle deletion + rank-minimal side proofs --height <=2q--> same zone languages
joint q-rule grammar --?--> bound on low-description mass/profile tensor of each safe zone --?--> q superlinear
or explicit compact zone synthesis --> full-promise q=N polylog N / N^(1+o(1))

C-245 gives q^2 context-family labels but does not bound the antichain contents. It is a representation theorem only. The quantitative edge to q remains open; C-228/C-234 are mandatory hostile checks. Continue O-153.


C-234 repeated anchors (2^(Theta(m)) low tables) + safe cube limit kappa=o(N)
--all r=N/m copies of u must be free for g(u) to vary-->
one proof cylinder covers at most 2^(kappa/r)=2^(o(m))
--cover every anchor-->
at least 2^(Theta(m)) certificates
--q-state witness encoding count q*2^q*(2N+q)^(2q)-->
only q log(N+q)>=Theta(m), below the known linear floor for m=N^beta, beta<1

Therefore retire raw proof-certificate cardinality as a superlinear charge. The remaining O-153 edge must use the semantic pattern of compatible context/proof joins or construct a near-linear full-promise cover. See C-246.


C-245 marked proof grammar --choose t disjoint proof occurrences--> C-247 simultaneous substitution law
private coordinate sets + injective replacement codes + full consistency
  --> product of replacement choices is a set of distinct accepted tables
  --> product_j |A_j| <= |SIZE(s2)|
C-234 block isolation --private sets are blocks--> 2^N hybrids > |SIZE(s2)|

Missing edge: small q --> many private high-entropy slots OR superlinear cost to organize overlaps/fingerprints.
Nesting/rail conflicts shrink the compatible product; diagonal equality supplies a linear-size fingerprinting escape. Total information alone cannot exceed N. Continue O-153; full-promise near-linear cover remains the counter-program. See C-247.


C-242 blocker map + state-local activation/inactivation
  --factor pair semantics into A_i × B_i-->
C-248 native state rectangles R_i
  --high-blocked side + low witness-->
signed mismatch seed rectangle M_lambda OR predecessor rectangle R_j
  --low activation rank decreases-->
terminating recursive rectangle route for every (w,z) in Y × Z

Consequence: sharing a state forces its full cross-product of low/high pairs to share the same recursive exits. Missing edge: quantitative lower bound on two-sided route sharing for actual Gap-MCSP; ordinary mismatch cover has only 2N seed rectangles and defeats area/counting alone.

Hostile example: Y={0,1}^N minus {0^N,1^N}, Z={0^N,1^N}
  --one rule E={1^N}, H={0^N}-->
q=1 and R_1=Y×Z, with different coordinate exits for different pairs

Therefore pair-space product-hull mixing does not imply a truth-table splice; the actual O-153 charge must connect recursive routing to a common table-space ownership profile.

C-75 q-state least fixed point --unroll q rounds, unbounded fan-in, gate count only-->
C-248 monotone promise-separator extension of size <= 3q^2+1

Wire-sensitive cost is O(q^2(N+q)), cubic at q≈N; no improved standard compiler. Any useful lower bound must target the exact monotone extension promise or the native recursive rectangle system. See C-248.


C-242 dense high side: every signed literal slice is nonempty
  --minimum activation-rank choice among active empty states-->
C-249 normalized output root has E_i,H_i both nonempty and disjoint
  --choose z_E in E_i and z_H in H_i-->
fixed high blockers for H-side and E-side respectively

C-240 two-coordinate shattering --root seed vocabulary normal form-->
one complementary literal selector OR a seedless side
  --every accepting root derivation must escape to predecessor-->
root-to-escape rectangle (w,z_E) or (w,z_H)

Missing aggregation: charge predecessor/context joins across all roots, or construct a near-linear full-promise cover. Root nondegeneracy and one-bit selectors alone do not charge q. See C-249.


C-240 seed-vocabulary normal form + C-243 proof-cylinder containment
  --choose a matching direct seed at a minimum-rank output root with both endpoints nonempty (C-249)-->
mandatory opposite-side predecessor
  --matching high half-cube is excluded from its carrier-->
one-sided safe support cylinder; free(C) <= ceil(log2|SIZE(s2)|)+1 (C-250)
  --repeated-block projection-->
at most 2^((kappa+1)/r) seedful anchors per support

Failed arrow: certificate count -> superlinear q; ranked witness-DAG descriptions remain exp(O(q log(N+q))). Seedless-root proofs are not covered. Missing edge: a joint context/proof aggregation theorem that charges reuse and handles two-sided seedless escapes. See C-250.


C-249 normalized empty output root + accepted low anchor w
  --if a direct root literal matches w-->
one opposite-side predecessor support C, half-safe by C-250
  --if no direct root literal matches w-->
two predecessor supports C_E,C_H; their consistent union C_E union C_H has a wholly-low cylinder (C-251)

Repeated-block projection bounds each selected one-support or paired-support signature by 2^((kappa+1)/r) anchors.
Failed aggregation: the number of support/DAG signatures is still exp(O(q log(N+q))); no q-sensitive overlap or compatibility charge follows. Seedless support width is controlled only after taking the pair union, not on either side separately. See C-251.


C-251 root escape signatures --aggregate by predecessor state IDs across roots-->
conflict relation G subset [q] x [q] (at most q^2 edges)
  --high activation of both endpoints would place z in E_i intersect H_i-->
every high activation profile is G-independent

direct seed literal + opposite predecessor state --same carrier contradiction-->
at most 2qN forbidden state/literal incidences

Every accepted low triggers a G-edge or a forbidden incidence; the resulting readout has <=q^2+2qN terms over state predicates and input bits (C-252).
Failed edge: readout size -> state lower bound. Activation predicates are themselves q-state least-fixed-point functions; high fibre sizes are uncontrolled. Target activation-fibre geometry for the actual promise or a near-linear cover. See C-252.

activation profile sigma --if it contains a conflict edge (C-252)--> whole fibre is low
activation profile sigma independent --collect markers on active states--> B_sigma
  --low readout / high avoidance-->
low fibre subset union of marked literal slices; high fibre subset marker-avoiding subcube of size <=2^(N-r_sigma) (C-253)

High entropy gives some realized independent profile with r_sigma<=log2(I)+o(1)<=q+o(1), where I counts high-realized profiles.
Failed edge: this profile may have no low anchors and no markers. Need an activation-equation theorem coupling low-output fibres to high-covered fibres, not just entropy/profile count. See C-253.

partial support C --state proof activations monotone in C-->
C activates conflict pair OR active state + incident seed literal
  --corresponding empty root activates on every completion-->
Cyl(C) subset SIZE(s2); |dom(C)| >= N-log2|SIZE(s2)| (C-254)

Every low full assignment is hazardous; every coordinate-order chain reaches its first hazard only near the top.
Selected readout proof DAG: at most q state labels times two side witnesses, plus one marker, hence support width <=2q+1. Combined with the hazard-cylinder width gives q >= (N-log2|SIZE(s2)|-1)/2, only a linear bound below the existing N-o(N) floor. Failed edge: no superlinear aggregation across anchors. See corrected C-254.


C-75 plain mismatch on Y x Z
  --binary acyclic product-rectangle DAG, S vertices <==> separator circuit C_sep=Theta(S) (Sokolov KW/circuit correspondence)
  --separator to promise-relative fusion cover--> rho_prom<=O(S)

q-pair fusion cover
  --rank-layer q^2 contexts + support routing--> S_rect=O(q^3/log q) [best recorded compiler]
  --short circuit-description map G--> description-DAG of exactly same minimum size (pullback + section)

Needed edge: exact relation, product-hull-safe residual state invariant -> OPS-specific S_rect>N^(3+3epsilon)/log N, OR an adaptive/revisiting near-linear shared DAG. Current local projection disjointness has no overlap-safe global sum; C-255.

SIZE(s1) x SIZE(s2) difference set has size <= |SIZE(s1)||SIZE(s2)|=2^o(N)
  --choose r outside it--> every u in SIZE(s1) maps to high table u xor r (C-255)
  --source reduction still requires every induced diagonal/off-diagonal signed mismatch rectangle to decode soundly--> open cut-sound low code / bottleneck capacity.
C-255 common-translate source reduction + static label decoder
  --rich KW source cut soundness--> each active address copies one source bit with a common phase
  --test tables u_0,u_e1,...,u_eM,v_1--> recover r with O(M s1) gates (C-256)
  --if s2>=C M s1--> r is low, contradicting r outside SIZE(s1) xor SIZE(s2).

C-255 common-translate source reduction + full-domain BPHP Search
  --a mismatch label's preimage is a product rectangle and its fixed answer names one collision pair--> each side lies in that pair's row-equality set
  --both signs at one active coordinate partition the Alice domain into two such equality sets--> impossible, since no two fixed pair-equalities cover all full Alice assignments (C-256).

Therefore the static-label route is closed for these rich KW and full-domain BPHP sources. It does not imply a target-DAG lower bound: terminal-specific sink labels may refine source rectangles. If each pulled-back sink rectangle admits a source-search DAG of at most T vertices, sink substitution gives a source triangle-DAG of size at most S_rect(1+T), so the Beame–Whitmeyer source lower bound forces S_rect>=L_source/(1+T). Missing edge: bound T for the actual sink preimages strongly enough to retain S_rect>N^(3+3epsilon)/log N, or pursue the direct C-75 bottleneck-capacity theorem / near-linear construction. See C-256.
