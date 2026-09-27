# O-1 selector Skolemization audit — 25 September 2026

## Question

The OPS anti-checker lemma says that for each high-complexity truth table there is a short list of input points that every low circuit gets wrong somewhere. Does this existence proof give an efficiently computable list as a function of the truth table?

The thresholds and list budget below use Oliveira–Pich–Santhanam's published Anti-Checker Lemma 4.1: [Hardness Magnification Near State-of-the-Art Lower Bounds](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf).

## Exact quantifiers

Let $X_n=\{0,1\}^n$, $N=2^n$, let $\mathcal C_n$ be the finite set of Boolean functions computed by circuits of size at most $s_1$, and let $F_n$ be the promise set of truth tables with circuit complexity greater than $s_2$. Define

$$
R_n(f,Q) \iff \forall D\in\mathcal C_n\;\exists x\in Q:\;D(x)\ne f(x).
$$

The existence theorem has the form

$$
\forall f\in F_n\;\exists Q\in X_n^{\le L_n}:\;R_n(f,Q),
\qquad L_n=O(\log|\mathcal C_n|).
$$

For the OPS parameters, $\log|\mathcal C_n|=O(s_1\log(s_1+n))=O(N^\beta)$, below the allowed $2^{10\beta n}=N^{10\beta}$ list budget for fixed $\beta>0$ and sufficiently large $n$.

The circuit-construction target is stronger and has a different quantifier shape:

$$
\exists S_n\quad
\bigl(|S_n|\le N^{1+\epsilon}\bigr)
\quad\text{and}\quad
\forall f\in F_n:\;
\bigl(|S_n(f)|\le t_n\ \land\ R_n(f,S_n(f))\bigr),
\qquad t_n=2^{10\beta n}.
$$

Here $S_n$ is one nonuniform circuit per input length. It cannot contain a separate hardwired list for each of the $2^N$ possible tables.

## Proof of list existence from the margin

At the exact OPS ratio $s_2=10ns_1$, C-52 proves

$$
\Delta(f):=
\min_{\mu\in\Delta(\mathcal C_n)}
\max_{x\in X_n}\Pr_{D\sim\mu}[D(x)\ne f(x)]
\ge 3/10
$$

for every $f\in F_n$. The contradiction if $\Delta(f)<3/10$ is an odd majority of $k\ge9n$ independently drawn low circuits: Hoeffding and a union bound over $N=2^n$ points make the majority equal $f$ everywhere, while its size is at most $(0.9+o(1))s_2<s_2$.

The margin is stable under conditioning in the following precise sense. For every nonempty subset $A\subseteq\mathcal C_n$ and every probability distribution $\mu$ supported on $A$, the definition of $\Delta(f)$ gives some $x$ for which at least $3/10$ of $\mu$'s mass disagrees with $f(x)$. In particular, using the uniform distribution on the current residual set, there is a query that removes at least a $3/10$ fraction of its circuits. Repeating this *existential* choice empties the residual in at most

$$
\left\lceil\frac{\ln|\mathcal C_n|}{-\ln(7/10)}\right\rceil+1
=O(\log|\mathcal C_n|)
$$

queries. This supplies the short-list existence statement directly.

## Where the constructive proof stops

The greedy proof asks for a point maximizing the number of currently surviving circuits that disagree with $f$. For a transcript $\tau$, these counts are

$$
\#\{D\in\mathcal C_n:D\text{ agrees with }\tau,\;D(x)\ne f(x)\}.
$$

The transcript has at most $O(s_1\log s_1)$ queried labels, and testing a proposed circuit against it is polynomial in the truth-table input length $N$. But computing the counts exactly is a counting problem over exponentially many circuit descriptions. Approximate global sampling computes the first score cheaply (C-52); relative sampling handles residual mass at least $\rho$ (C-53); C-54 proves that this particular method loses its guarantee at a still-nonempty residual after $O(n)$ rounds when $\rho$ is inverse-polynomial.

There is a complexity-theoretic way to state the obstruction. For explicit $f$ and $Q$, failure of $R_n(f,Q)$ has an NP witness: a size-$s_1$ circuit agreeing on every point in $Q$. Thus $R_n$ is coNP-checkable, and the search statement $\exists Q\,R_n(f,Q)$ is a second-level search relation. Totality on the promise does not by itself give a small circuit Skolem function.

## Adversarial generality audit

1. A hypothetical selector may avoid greedy scoring, uniform residual mass, and circuit-description sampling entirely. Therefore the C-53/C-54 cutoff is not a lower bound on arbitrary selectors.
2. A fixed or globally sampled menu can miss an exact survivor. This falsifies that sampling architecture, not every way of choosing $Q$ from $f$.
3. The short list itself is not a readily checkable certificate: verifying that no size-$s_1$ circuit agrees on all of it is the coNP predicate $R_n$.
4. The universal lower-bound target remains the size of every circuit family that uniformizes $R_n$ on $F_n$, or directly the OPS Gap-MCSP circuit lower bound O-1. Either target is already a major lower-bound problem; the quantifier rewrite alone is no progress on O-1.

## Alternative attacks tested against the same bottleneck

### LP / separating-measure computation

The finite minimax theorem gives a distribution $\nu_f$ on coordinates such that every low circuit disagrees with $f$ on at least a constant $\nu_f$-mass. This is an appealing semantic witness. But standard ellipsoid-style construction needs a separation oracle: for a candidate weighting $w$ on coordinates, find a size-$s_1$ circuit minimizing weighted disagreement with $f$. That is a weighted circuit-fitting optimization problem, not a known polynomial-time or near-linear-size oracle. The minimax proof therefore relocates the problem to finding the adversarial low circuit; it does not furnish $\nu_f$ efficiently.

### Bounded-arithmetic / KPT extraction

Formalizing the totality proof may permit a witnessing theorem to extract functions, but the output predicate contains a universal quantifier over low circuits. Existing KPT analysis (C-43) warns that extraction can be adaptive to counterexample witnesses. Flattening those dependencies by enumerating all challenges can be exponential. A useful result here would need a resource bound for one nonadaptive selector, not merely a finite adaptive witness tree.

### Direct diagonalization

Trying to make a selector's output agree with a fixed low circuit requires setting $f(x)$ after seeing each selected address $x$. For a general selector, those addresses can depend on every truth-table bit, so the recursive assignment does not determine the next address. The fixed-point constraint $f|_{Q(f)}=D|_{Q(f)}$ has not been shown to have a high-complexity solution. Simple versions are defeated by a selector that first searches the truth table for a disagreement with the chosen constant circuit. This route presently hides a selector lower bound inside the fixed-point existence claim.

### Output counting / information

For a fixed query set $Q$ with $q$ distinct points, validity depends only on the trace $f|_Q$: write $T_Q=\{D|_Q:D\in\mathcal C_n\}$. If a trace $y\notin T_Q$, then every one of its $2^{N-q}$ extensions satisfies $R_n(f,Q)$. At most $M_2\le2^{O(s_2\log(n+s_2))}$ of these extensions have circuit complexity at most $s_2$. Hence, when $q+\log_2 M_2<N$, the list is valid for many high tables sharing that trace. At OPS length $q\le2^{10\beta n}$ with fixed $\beta<1/10$, both $q$ and $\log M_2$ are $o(N)$, so almost all extensions are high. Thus a small output range or short output string does not by itself force a large circuit: a valid list can serve a huge cylinder of tables. This is C-56 below.

There is also an exact average/worst-case split. For uniformly random $f$, its trace on $Q$ is uniform in $\{0,1\}^q$, so

$$
\Pr_f[R_n(f,Q)]=1-\frac{|T_Q|}{2^q}\ge1-\frac{|\mathcal C_n|}{2^q}.
$$

Thus a fixed list with $q\ge\log_2|\mathcal C_n|+\omega(1)$ is valid for almost every truth table. Yet the all-zero trace lies in $T_Q$ (the constant-zero circuit realizes it), and its $2^{N-q}$ extensions include high tables whenever $q+\log_2M_2<N$. A fixed list can therefore succeed on almost all tables and still fail on a high table. This is the precise exceptional-cylinder obstruction behind C-15.

These four attempts all fail at the same point: none bounds the complexity of routing an arbitrary high table to one of its valid trace cylinders.

### Local patch encoding plus a hard base table

Point-patching suggests encoding a source instance in a small set $P$ of truth-table locations while keeping the table high. This can preserve hardness: if $CC(g)>2s_2$ and $h$ differs from $g$ on $r<s_2/(A n)$ points, where $A$ is the point-patching constant, then $CC(h)>s_2$; otherwise patching a size-$s_2$ circuit for $h$ would compute $g$ with size below $2s_2$.

But this does not force a selector output to reveal the patch. Choose any valid anti-checker $Q_0$ for $g$ disjoint from $P$. Every modified table $h$ agreeing with $g$ on $Q_0$ still has the same valid anti-checker $Q_0$, because validity depends only on that trace. Therefore a reduction that must decode the source from *every* valid selector output fails on this family: the relation permits one common output independent of the encoded data. To make local patching useful, one would need $P$ to hit every valid anti-checker for the base table, or a stronger construction that makes every valid output encode the source. No manageable hitting-set theorem of this kind is known here.

## Kannan-hierarchy reduction audit

Kannan's theorem gives, for each fixed exponent $k$, a language $L_k\in\Sigma_2^P\cap\Pi_2^P$ outside $\mathrm{SIZE}(n^k)$; the language can depend on $k$ ([Kannan 1982](https://doi.org/10.1016/S0019-9958(82)90382-5)). It does not establish one fixed $\Sigma_2^P$ language outside all polynomial circuit sizes. A search reduction must map each source input $x$ of length $m$ to a high table $f_x$ of length $N=m^{a_k}$ and give a polynomial-size decoder $B$ such that $B(x,Q,f_x|_Q)=L_k(x)$ for **every** valid selector output $Q$ for $f_x$. If the table generator, selector composition, and decoder have circuit exponents $b_k$, $a_k(1+\epsilon)$, and $d_k$, the total exponent is at most $e_k=\max\{a_k(1+\epsilon),b_k,d_k\}$, up to lower-order factors. A contradiction needs $k>e_k$, and no reduction with these exponents controlled against $k$ has been constructed. The high-table promise and validity for every output are extra obligations absent from ordinary completeness reductions. A common $Q$ and common trace defeat output-only decoding; with a decoder that also sees $x$, they only help if the resulting fixed-trace decoder has exponent below $k$.

This closes the tempting inference “the selector relation is at the second level, so Kannan gives its lower bound.” Kannan's theorem is not a fixed-language superpolynomial lower bound, and a many-one reduction to the decision relation would not automatically reduce the search selector with exponent preservation.

## Output-decoding reductions: a patch-switch obstruction

Write $E_D(g)=\{x:D(x)\ne g(x)\}$. Suppose two size-$s_1$ circuits $D_i,D_j$ satisfy $E_{D_i}(g)\subseteq P_i$ and $E_{D_j}(g)\subseteq P_j$ for disjoint regions $P_i,P_j$. Then

$$
g(x)=\begin{cases}D_j(x)&x\in P_i,\\D_i(x)&x\notin P_i.\end{cases}
$$

The first branch is correct on $P_i$ because $P_i\cap P_j=\varnothing$; the second is correct outside $P_i$. A fan-in-two circuit for the region indicator and one mux therefore gives

$$
CC(g)\le 2s_1+CC(\mathbf 1_{P_i})+O(1).
$$

Consequently, if $CC(g)>s_2$, every such decoder-recognizable patch region must have indicator complexity $>s_2-2s_1-O(1)$. At the OPS ratio $s_2=cn s_1$, this rules out the natural gadget in which deleting any one source bit leaves a size-$s_1$ approximation that is wrong only on that bit's easy-to-recognize, disjoint address block. Two of those approximants would already compute the allegedly hard table by switching.

**Scope warning.** One cannot infer the premise $E_D(g)\subseteq P$ from the weaker condition that every valid list of length at most $t$ intersects $P$. For the abstract hypergraph with edges $\{p,x_i\}$ for $i=1,\ldots,t+1$, the singleton $\{p\}$ is a transversal, every transversal of size at most $t$ intersects $P=\{p\}$, yet no edge is contained in $P$. Thus the patch-switch lemma blocks a useful class of bit-decoding reductions; it does not rule out every way short selector outputs could be forced to reveal information. The remaining reduction target needs either actual low-circuit approximants localized to each decoded region or a different all-valid-output mechanism, plus a proof that the mechanism survives this short-transversal counterexample.

## Mandatory-region mass bound (C-61)

Fix a high table $f$ and its dual-margin distribution $\nu$ with $\nu(E_D)\ge\gamma=3/10$ for every low circuit. A set $P$ that every valid list of at most $t$ queries must intersect cannot have small $\nu$-mass. If $p=\nu(P)<\gamma$, conditioning $\nu$ outside $P$ leaves every error set mass at least $(\gamma-p)/(1-p)$. A sample of $t$ points outside $P$ hits all $M_1$ error sets whenever
$$
t\frac{\gamma-p}{1-p}>\ln M_1,
$$
by a union bound. Therefore mandatory status forces
$$
\nu(P)\ge\frac{\gamma-\alpha}{1-\alpha},\qquad \alpha=\frac{\ln M_1}{t}.
$$

For pairwise-disjoint mandatory regions, their masses sum to at most one, so
$$
m\le\left\lfloor\frac{1-\alpha}{\gamma-\alpha}\right\rfloor.
$$
At OPS parameters, $\ln M_1=O(N^\beta)$ and $t=N^{10\beta}$, hence $\alpha=O(N^{-9\beta})$. With $\gamma=3/10$, for all sufficiently large $n$ this bound is at most three. Thus a fixed hard table cannot have four pairwise-disjoint regions that every allowed anti-checker must query.

This blocks “one mandatory disjoint query block per source bit” reductions, even without assuming a localized low-circuit approximant for each block. It does not constrain overlapping regions, information encoded across many query points inside one region, or a decoder that does not rely on mandatory regions. Full proof and finite threshold are in C-61 of [the claim ledger](CLAIM_LEDGER.md).

## Learning-theory formulation: external teaching sets

For a finite concept class $\mathcal C$, define the external teaching number of a target $f\notin\mathcal C$ by

$$
\operatorname{ETD}_{\mathcal C}(f)
=\min\{|Q|:f|_Q\notin\{D|_Q:D\in\mathcal C\}\}.
$$

This is the anti-checker list length viewed as a teaching/certificate quantity for a target outside the hypothesis class. For $\mathcal C=\mathcal C_{s_1}$ and $CC(f)>s_2$, C-55 gives

$$
\operatorname{ETD}_{\mathcal C_{s_1}}(f)
=O(\log|\mathcal C_{s_1}|)=O(s_1\log(s_1+n)).
$$

C-49's local-patching argument gives the lower bound

$$
\operatorname{ETD}_{\mathcal C_{s_1}}(f)=\Omega(s_1/n).
$$

At fixed OPS $\beta$, this pins the information/query size to the interval $\Omega(N^\beta/n^2)$ through $O(N^\beta)$ up to constants and representation details. The OPS output allowance is larger. Therefore the unresolved resource is not how many labeled examples a teacher needs, but the circuit size of one map $f\mapsto Q_f$ that always supplies them.

This terminology is a useful lens, not a claim of a new learning-theory invariant. Known hardness results for finding *minimum* teaching sets do not apply automatically: our target is outside the class, the list may be nonminimal, the hypothesis class is succinctly represented by circuits, and the required lower bound concerns one nonuniform selector circuit on all high tables. A reduction matching all these features would be needed.

A generic VC-dimension shortcut also fails. On a domain $X$ of size $m\ge3$, take the class $\mathcal C=\{X\setminus\{i\}:i\in X\}$. It has VC dimension 1: any singleton is shattered, but on any two points the all-zero pattern is missing. For the outside target $f\equiv1$, every proper subset $Q\subsetneq X$ is matched by the concept $X\setminus\{i\}$ for some $i\notin Q$, so $\operatorname{ETD}_{\mathcal C}(f)=m$. Thus low VC dimension alone does not produce a short external teaching set. In the circuit problem the useful short-list theorem instead comes from the special minimax margin proved using majority closure.

## Next attack

Look for a representation-independent way to compute an external teaching set from $f$ without counting the exact residual circuit family. Alternatively, reduce a known hard search problem to finding any sufficiently short external teaching set for this succinct circuit class, not merely to minimizing its length. Any proposed shortcut must be attacked with an arbitrary selector that ignores its favored representation. In particular, do not promote a failure of global sampling to a universal selector lower bound.

## Status

**Proved reframing and existence derivation; no separation and no new unrestricted lower bound.** The productive fact is that the mathematical obstruction is not lack of a short anti-checker: it is the input-dependent circuit uniformization of those witnesses. O-1 remains open.

**Fractional form.** More generally, mandatory regions with fractional packing weights whose pointwise overlap is at most one have total weight at most (1-alpha)/(gamma-alpha)=10/3+o(1). This follows by integrating their overlap against the same dual distribution. It also limits bounded-overlap region gadgets, while leaving highly overlapping encodings open.

## Dual-mass separation for output-only decoding (C-62)

For high tables $f,g$, write $P(f,g)=\{x:f(x)\ne g(x)\}$. If either $\nu_f(P(f,g))<p_*$ or $\nu_g(P(f,g))<p_*$, where $p_*=(\gamma-\alpha)/(1-\alpha)$, C-61 gives a valid list of at most $t$ addresses outside the difference set. Its labels are identical for both tables, so their valid labeled-list sets intersect.

Consequently, an output-only decoder that must return different answers for source instances mapped to $f$ and $g$ requires both directed dual distances to be at least $p_*$. This is a necessary encoding condition, not a lower bound. If the decoder also receives the source input, the common-list observation alone does not determine its answer; charge the decoder's circuit size in the Kannan exponent audit.
The bound also has a robust patch form: if $\nu(P)<(\gamma-\alpha)/(1-\alpha)$, there is one valid list entirely outside $P$. Every table agreeing with $f$ off $P$ has the same trace on that list, so local payloads confined to such a dual-light region cannot support all-valid-output decoding from the list and its labels.

## C-63 — Agreement-fiber form of adversarial completion

For a fixed candidate selector S and low circuit D, set \(A_D^S=\{f:f|_{S(f)}=D|_{S(f)}\}\). The selector succeeds on every high table iff every one of these fibers is contained in SIZE(s2). Thus the exact S-1 counterexample target is \(\exists D\in SIZE(s1)\,\exists f\,[CC(f)>s2\land f\in A_D^S]\). Membership in a fixed fiber has a circuit of size O(|S|+t(N+s1+n)) after address muxing.

This is a precise reformulation, not an advance in the asymptotic lower bound. The two-constant concept class has a linear priority selector whose agreement fibers contain no hard target, so any proof must use circuit-class-specific richness or closure. See C-63 in the claim ledger and the reset audit.
**C-64 adversarial quantifier check.** Fixing a single low D is too weak: the first truth-table coordinate where f differs from the hardwired D is found by an O(N)-gate priority encoder. A fixed menu of m low tables is handled in O(mN) gates. Therefore the hard circuit D in the C-63 counterexample must be selected jointly with f against the full low-circuit class; no one-baseline patch argument can reach the superlinear target.