# A Working Model for P vs NP

**Last updated:** 28 September 2026
**Status:** research framework; no proof of $P\ne NP$ or $P=NP$ has been found.  
**Purpose:** make the project's accumulated results usable as a theory-building tool, so new ideas start from precise proof obligations and known failure modes.

This is the project's synthesis file. [ideas.md](ideas.md) remains the broad idea log; [P_VS_NP_PROJECT_AUDIT_2026-08-24.md](P_VS_NP_PROJECT_AUDIT_2026-08-24.md) remains the detailed evidence and literature audit. This file extracts a working model from them and records what that model predicts next.

## Current research priority: global sharing in native fusion closure

The active route is the exact positive cyclic closure, not a generic DAG lower bound. Each rule has two endpoint obligations; finite proof trees witness least-fixed-point activation. Reuse at a state gives the exact product law: any accepting context with a hole at state `i` combines with any finite proof rooted at `i`, provided the resulting seed support is table-consistent. The central unresolved issue is global: can one short circuit description remain consistent across all those context/proof joins?

C-257 gives a necessary hostile calibration. On the odd-parity high set, every proper partial assignment extends to a high object, and every sound output support fixes all `N` coordinates. Yet a `4N-4`-rule fusion list accepts all even anchors, and each consistent splice is again even. So high-side density, certificate width, anchor abundance, and reuse do not force a high hybrid. The missing ingredient must distinguish the actual low-circuit family from an algebraically closed code: low tables each have a short description, but spliced pieces may fail to come from one common description once their combined description cost crosses `s2`.

C-258 shows the equality-fingerprint escape inside the actual high universe. More generally, if a target family is a product of local codebooks `A_j` across coordinate blocks and is disjoint from `U=complement SIZE(s2)`, a direct native list has `q<=sum_j |A_j||B_j|+2d-1` pairs. For repeated-block subfamilies `Rep_{d,r} subseteq SIZE(s1)`, this is `2N+2d-1=O(N)`: build carriers for each constant block value, merge the two values per block, then intersect the block predicates. This is an `O(N)` cover of that subfamily, not the full low class. It sharpens the next question: can low circuits be partitioned or covered by only near-linearly many similarly compressible semantic regions, or does the full class force a superlinear number/cost of distinct fingerprints?

C-259 fixes the scale for multi-hole attacks. The OPS ratio is `s2/s1=cn=Theta(log N)`. Up to `Theta(n)` size-`s1` cofactors can be selected by a prefix mux and still produce a size-`s2` table; more than `C n` mutually independent slots, each with `2^{Theta(s2)}` choices and private coordinates, would exceed the total number of size-`s2` tables by C-247's product bound. This matches C-116's cofactor fragmentation threshold. It does not say that q forces such slots. The live theorem is to derive `Omega(n)` compatible independent choices or selector complexity from the joint context/proof grammar, and then charge suppressing them to q.

This is a hypothesis, not a theorem. The proof target is a q-sensitive statement about the full joint context/proof grammar: either many compatible joins create a table outside `SIZE(s2)`, or suppressing those joins costs superlinear `q`. A matching counter-program is to build a near-linear native cover for the full Gap-MCSP promise. The standard DAG branch stays secondary unless it gives a direct invariant or a near-lossless compiler.

## 1. The current model in one sentence

**A P-vs-NP proof must turn a compact local description of an NP computation into a global, uniform, and verifiable obstruction to every polynomial-time solver.** The project has repeatedly found local witnesses, large counts, or elegant representations; the unpaid step is usually proving that one small uniform object cannot integrate all of the relevant information.

I call this the **global integration model**. It is a project-level research framework, not a theorem or a claim that the problem has a single hidden obstruction. Its value is operational: it tells us what a proposed proof must construct, what it must rule out, and where a failed route spent its resources.

A new local refinement is now proved for a test family: a **polarity budget** forces both signs of each variable in formulas, while a packing of disjoint disagreement supports forces an exact selector size. This explains how a critical trace boundary can arise. The finite circuit checks suggest some resistance to sharing, but the all-size circuit claim remains open. The refinement improves our account of one mechanism; it does not pay the global uniformity, superlinearity, or transfer debts in the P-vs-NP proof ledger.

## 2. Start with the quantifiers

For SAT, membership has the form

$$
x\in\mathrm{SAT}\iff \exists w\;V(x,w)=1,
$$

where $V$ runs in polynomial time and $|w|$ is polynomial in $|x|$. The witness can be checked locally once supplied. A polynomial SAT decider would also yield a polynomial witness finder by fixing witness bits one at a time and asking whether a satisfying completion remains possible.

The open gap is the existence of one uniform polynomial-time decision procedure for all inputs. It is not enough to show that some instances have many assignments, that some witnesses are hard to find by a chosen search method, or that a particular proof system needs long proofs. A separation must exclude every polynomial-time SAT decider, or establish a lower-bound route with a proved transfer to that statement.

The project's meta-complexity route makes the quantifiers visible on a truth table $f$ with $N=2^n$ entries. For a low-circuit class $\mathcal C_{<s}$,

$$
f\text{ is low}\iff \exists C\in\mathcal C_{<s}\;\forall x\; C(x)=f(x),
$$

while

$$
f\text{ is high}\iff \forall C\in\mathcal C_{<s}\;\exists x\; C(x)\ne f(x).
$$

Finding one disagreement for each candidate circuit is easy if the full table is already available: scan the table and take the first mismatch. The hard step is compressing this potentially huge selector and certifying its universal coverage without simply restating the original circuit-minimization question.

This is the model's first rule:

> **Keep existence, search, counting, avoidance, and proof separate.** A compact description of a relation does not automatically give an algorithm to decide it, find a witness, avoid its image, or certify that avoidance.

The pinned-fiber audit in Section 2 of the project audit makes this distinction explicit for SAT, MCSP, and range-avoidance problems.

### 2.1 Work backward from each answer

The decision problem is already equivalent to one focal statement: $P=NP$ iff $SAT\in P$, by Cook--Levin. The two possible answers have sharply different logical shapes.

| Starting assumption | What follows | What does **not** follow from it alone |
|---|---|---|
| $P=NP$ | SAT has one uniform polynomial-time decider and, by self-reduction, one uniform polynomial-time witness finder. More generally, polynomially balanced NP witness relations can be searched in polynomial time. Also $NP=coNP$. | It does not say that a particular proof system has short proofs for every theorem, nor that every proof-finding task is easy when the shortest proof itself is enormous. |
| $P=NP$ | No standard length-indexed one-way function can exist: inversion is an NP witness search problem, and the input length/index can be supplied to the search relation. | This is only a consequence. Assuming one-way functions proves $P\ne NP$ conditionally; it does not prove the premise unconditionally. |
| $P\ne NP$ | $SAT\notin P$, and no single polynomial-time algorithm decides SAT or always finds a satisfying assignment on satisfiable inputs while rejecting unsatisfiable ones. | It is not known to force $NP\ne coNP$, one-way functions, or the nonexistence of polynomially bounded Cook--Reckhow proof systems. Those are stronger or separate questions. |
| $NP=coNP$ | There exists a polynomially bounded Cook--Reckhow proof system for TAUT. Conversely, such a proof system implies $NP=coNP$. | This condition is not known to decide $P$ versus $NP$; in particular, $P\ne NP$ would not by itself rule it out. |

The first row follows directly: decide whether each prefix of a proposed witness can be extended to a satisfying assignment, fix a successful next bit, and repeat for the polynomially many witness bits. Under $P=NP$, each extension question is in P. The one-way-function row uses the same search-to-decision construction on the relation $f(x)=y$, with the input length supplied so the preimage is polynomially bounded. Under $P=NP$, any fixed Cook--Reckhow proof system can also be automatized in time polynomial in the formula length plus the shortest proof length: existence of a proof below a proposed length supplied in unary is an NP question, and under $P=NP$ it can be decided and searched. This does not imply polynomial-size proofs in a preselected system. These are implications, not evidence favoring either answer.

The crucial quantifier distinction appears when trying to use a time hierarchy. For each integer $k\ge1$, a nondeterministic time hierarchy theorem supplies some language $L_k\in NTIME(n^{k+1})\subseteq NP$ outside $NTIME(n^k)$, hence outside $DTIME(n^k)$. The desired separation is instead

$$
\exists L\in NP\;\forall k\; L\notin DTIME(n^k),
$$

because $P=\bigcup_k DTIME(n^k)$. The hierarchy statement has the order $\forall k\,\exists L_k$; exchanging those quantifiers is invalid. Each diagonal language may depend on $k$, and the hierarchy theorem supplies no one language outside every polynomial clock. This is a concrete reason the ordinary time-hierarchy diagonal does not settle $P\ne NP$.

The same resource multiplication appears if hierarchy languages are routed through SAT completeness. A language decided nondeterministically in $n^r$ time has a Cook--Levin formula whose size is polynomial in its computation tableau. A hypothetical SAT decider with clock $m^k$ would then give a deterministic algorithm whose exponent is multiplied by $k$ and by the tableau encoding exponent. A hierarchy language chosen outside one clock need not lie outside this larger clock. Raising the hierarchy exponent also raises the formula size and therefore the composed clock. This is a precise accounting failure for that direct route, not a barrier to every possible reduction or diagonal argument.

For SAT, the same target can be written in witness-search form using Section 7's fixed universal machine:

$$
P\ne NP\iff\forall c,d\;\exists\varphi\in SAT\;\forall p\ (|p|\le c\Rightarrow p\text{ fails to output a verified witness for }\varphi\text{ within }|\varphi|^d\text{ steps}).
$$

This makes the proof obligation exact: for each fixed description budget and polynomial clock, produce a satisfiable formula defeating every short program. A naive self-referential tableau does not close the loop. If simulating a candidate for $n^d$ steps makes the encoded formula length $M\approx n^d$, that same candidate receives roughly $M^d\approx n^{d^2}$ steps on the final formula. This calculation blocks that direct construction; it is not a theorem against all diagonal methods. Succinct encodings or a different fixed-point argument would need a proved uniform decoding and size bound.

**Current logical diagnosis:** starting from $P=NP$ yields strong and useful consequences, but none is presently contradictory. Starting from $P\ne NP$ reduces to the explicit all-clocks SAT witness lower bound above. A proof must supply a new lemma that creates this uniform object, or a different theorem-level route to the same separation. This is the point to test creative logic constructions against, rather than treating self-reference, incompleteness, or a hierarchy theorem as a proof by themselves.

### 2.2 What ZFC can and cannot add

Using $P=NP\iff SAT\in P$, the equality can be written as

$$
\exists e,k\;\forall\varphi\;[M_e\text{ halts within }(|\varphi|+2)^k\text{ steps and outputs 1 iff the formula $\varphi$ is satisfiable].
$$

Here $e$ is a deterministic machine code and the predicate in brackets is computable: the clocked run is finite, and SAT itself is decidable by exhaustive search. With a standard arithmetization, this is a $\Sigma^0_2$ sentence; its negation $P\ne NP$ is $\Pi^0_2$. This classification is about logical form, not difficulty. The two quantifier blocks still range over all machine codes, exponents, and formulas.

A proof search can enumerate ZFC derivations and eventually find a proof of either sentence if ZFC proves one. If the question is independent of ZFC, that search never halts; no finite timeout distinguishes independence from a very long proof. We have no known ZFC proof of either answer and no known independence result for this specific sentence. GÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶del's incompleteness theorem does not imply that P vs NP is independent merely because it is important or difficult. Establishing independence would require separate relative-consistency results for ZFC plus each answer (and assumptions about ZFC's consistency); establishing a proof requires the actual derivation. Truth in the standard natural numbers and provability from ZFC must remain separate ledger entries.

**Proof attempt:** seek either (i) a structural theorem yielding the all-clocks SAT witness obstruction in Section 2.1, or (ii) a formal reduction from a known theorem to one side. The ZFC classification itself supplies neither. It does rule out a misleading strategy: waiting longer or invoking incompleteness cannot replace the missing lower-bound lemma.

### 2.3 A stronger proof-complexity route

For Cook--Reckhow proof systems, $NP=coNP$ is equivalent to the existence of one system $\Pi$ and one polynomial bound $q$ such that every tautology $\tau$ has a $\Pi$-proof of length at most $q(|\tau|)$. To see the equivalence, a polynomially bounded system puts TAUT in NP; since TAUT is coNP-complete, this gives $coNP\subseteq NP$, and complementing gives $NP\subseteq coNP$. Conversely, if NP=coNP then TAUT is in NP. Its polynomial certificate verifier yields a proof system by outputting the certified tautology on valid inputs and a fixed tautology otherwise; every tautology then has a polynomial-size proof. Negating this gives the exact alternative

$$
\forall\Pi\;\forall k\;\exists\tau\in TAUT\;\forall\pi\ (|\pi|\le(|\tau|+2)^k\Rightarrow \Pi(\pi)\ne\tau).
$$

Thus an all-systems, all-polynomial-bounds proof lower bound would establish $NP\ne coNP$, and therefore $P\ne NP$. It is a valid theorem-level route, but stronger than needed. A self-referential sentence saying ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œI have no short $\Pi$-proofÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â is not enough: the construction must prove the sentence is a tautology, account for its own length, and rule out every proof of the permitted length. This is the same encoding obligation in a sharper proof-theoretic setting.

**Synthesis with prior proof-complexity work.** This route is already explored in Ideas 27ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“45, so the current task is to strengthen those attempts rather than repeat them. The implication chain is $P=NP\Rightarrow NP=coNP\Rightarrow$ a polynomially bounded proof system $\Rightarrow$ an optimal proof system $\Leftrightarrow$ an ordinary fast consistency prover (FCP). It is open whether existence of an ordinary FCP implies $NP=coNP$. Joosten's stronger ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œunlikely FCP,ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â with a uniform bound tied to axiom-recognition time, is equivalent to $NP=coNP$. The existing per-$k$ reflection construction (Idea 28) loses against the $k$-dependent axiom-checking exponent, while the tower packaging (Idea 42) reaches the PudlÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡k finite-consistency conjecture already at its first stage. A recursive jump operator for TAUT would rule out optimal systems and hence imply $P\ne NP$, but Egidy's 2026 oracle result shows that a general jump proof cannot relativize. These are theorem-level targets with known gaps, not established routes to a proof.

The strongest fixed-point attempt in the log is Idea 45. Assuming an efficient syntactic fixed point, it makes a formula whose falsifying assignment would encode a short proof of that same formula; soundness then forces the formula to be a tautology. Its explicit candidate-proof interface has size at least linear in the proof cutoff, so the resulting lower bound remains polynomially compatible with proof simulation. Idea 119 isolates this coverage cost precisely. If $m$ assignment bits encode all candidate proof strings of length at most $L$, then $2^m\ge2^{L+1}-1$, so $m\ge L+1$. In the direct explicit formula interface, this gives $|\tau|=\Omega(L)$. A lower bound of $L$ on the old system's proof is then polynomially compatible with any other system whose decoder must print $\tau$; it does not establish a jump. The only direct-encoding escape is to prove a sound normal form covering every relevant short proof with fewer bits.
**Naive size audit.** A separate tableau diagonal starts with a seed parameter $n$ and tries to exclude all proofs up to $L=n^k$. An explicit formula that describes or checks those candidate proofs can have final length $N=\mathrm{poly}(L)$. A polynomially bounded proof system would then only promise a proof up to $q(N)$, which can be much larger than $L$. The diagonal has not contradicted the assumed proof bound unless it excludes proofs at the bound determined by its own final formula length. The required truth proof is not the absence statement: it must come from the fixed point and soundness, as in Idea 45. A bare assertion of nonproof would not suffice.

**Active proof attempt:** with Idea 119 formalized, seek either (i) a proven normal form that compresses all relevant proofs into fewer candidate bits or (ii) a non-relativizing uniform jump/FCP lower bound. Any normal form must be sound, polynomially checkable, and strong enough to cover every short proof; generic enumeration has the linear coverage cost above. Do not repeat the already-audited per-$k$ reflection or fixed-system diagonal without a new contraction.

### 2.4 ZFC status as a separate branch

Write $A$ for the arithmetic sentence $P=NP$. Relative to a consistent ZFC, three proof statuses are possible for this particular sentence: ZFC proves $A$, ZFC proves $\neg A$, or ZFC proves neither (independence). GÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶del's incompleteness theorem says that sufficiently strong consistent effective theories leave some sentences undecided; it does not identify $A$ as one of them. The standard-model truth value of $A$ is a separate question. Consistency alone is not a soundness assumption, so the project must not infer standard truth merely from the existence of a ZFC derivation without stating the soundness assumption being used.

This distinction is strategically useful because it exposes a narrow route from independence theory, while also showing its ceiling. Let $C$ be a candidate combinatorial sentence. If one proves in ZFC that $A\to C$, and separately proves $C$ independent of ZFC, then ZFC cannot prove $A$: a proof of $A$ would yield a proof of $C$. This does **not** prove $\neg A$, nor does it resolve the standard-model truth of $A$. To prove $C$ independent, an implication from a known independent theorem $J\to C$ is insufficient: unprovability does not transfer in that direction. One needs, for example, a reverse reduction $C\to J$, a genuine equivalence, or a model construction that settles both sides.

**Case study: subset sum and the Jump Free Theorem.** Williamson's [2024 arXiv preprint](https://arxiv.org/abs/2404.00468) translates Friedman's Jump Free Theorem into a subset-sum corollary $C$. Its abstract explicitly says that independence of the translated theorem and corollary is *conjectured*, not established. A direct ZFC argument below proves the computational corollary for a natural encoding, so the conjecture cannot be used without fixing the exact bijections and computational statement. The Jump Free Theorem implying $C$ does not establish $C$ independent. Even if an appropriately fixed version of $C$ were proved independent, this route would at most rule out a ZFC proof of $P=NP$; it would not prove $P\ne NP$. The lead is therefore a useful proof-status test case, not a separation result.

**Direct bounded-weight proof for the canonical encoding.** Fix $k\ge2$ and let $\gamma_0=\gamma_1=\gamma_2=\gamma$, where $\gamma(2j)=j$ and $\gamma(2j+1)=-(j+1)$. For each $p$, set $E_p=\{0,\ldots,p-1\}$ and $D_p=E_p^k$. Fullness supplies $f_p\in S$ with domain $D_p$; reflexivity gives $\operatorname{range}(f_p)\subseteq\operatorname{field}(D_p)=E_p$. Thus every integer appearing in either list $F(\hat f_p)$ or $H(\hat f_p)$ has absolute value at most $p$, and each list has at most $p^k$ entries (counting multiplicity).

For any such list $a_1,\ldots,a_n$, let $B=\sum_i|a_i|\le p^{k+1}$. Initialize $R_0=\{0\}$ and update $R_i=R_{i-1}\cup\{s+a_i:s\in R_{i-1}\}$; then $0\in R_n$ exactly when a subset sums to zero. The sets stay inside $[-B,B]$, so the table has $O(B)$ states and can be updated in $O(B\,\mathrm{polylog}(p))$ bit operations per item. For a nonempty-subset convention, attach a Boolean flag recording whether any item was selected and accept only state $(0,1)$. The total time is $O(nB\,\mathrm{polylog}(p))=O(p^{2k+1}\,\mathrm{polylog}(p))$. For fixed $k\ge2$, this is at most $O(p^{3k})$ on a multitape machine. A single-tape simulation is bounded by $O(p^{6k})$, so one fixed choice such as $t=6$ suffices under either standard model. The same uniform algorithm handles both sequences. Hence the corollary's existential sequence statement is provable in ZFC for this canonical encoding, without assuming $P=NP$ and without invoking the Jump Free Theorem.

This does not settle a version with three arbitrary fixed bijections $\gamma_i:\mathbb N\to\mathbb Z$: their output bit lengths may grow faster than any polynomial in the input index, and the paper does not state an effective or polynomial-growth condition. In that version, $P=NP$ supplies a bound polynomial in the full binary input length, not automatically $O(p^{kt})$. A sufficient bridge is an explicit uniform bound $N_p\le p^c$ on the total binary length of each instance: then an $N_p^d$ subset-sum algorithm runs in $O(p^{cd})$, hence in $O(p^{kt})$ for a fixed $t$. The exact quantifiers over $\gamma_i$, the meaning of the sequence-time bound, and uniform generation of the instance family must be fixed before the independence conjecture has a precise formal and computational meaning. The canonical case is already settled; do not spend more work trying to prove its independence.

**Proof task for this branch:** only continue with a fully specified noncanonical version of $C$. First state the three bijections, their computability and bit-growth bounds, whether the $f_p$ sequence must be uniformly generated, and the exact input model. Then either prove a real reduction $C\to J$ / relative-consistency result or close the branch. The canonical version is ZFC-provable by the dynamic program above. Keep the direct separation target in Sections 2.1 and 2.3: an independence result about a different sentence cannot replace an SAT lower bound.

### 2.5 Semantic promises survive only certified transformations

A new hierarchy-theorem audit adds a distinct proof obligation: **promise preservation**. For a semantic class such as $UP$ or $BPP$, a machine description alone does not guarantee class membership. The machine must satisfy its promise on every input in the scope of its class definition. In the standard advice convention for a semantic class, $M(x,s_n)$ must be valid for the selected advice sequence $s_n$; the other advice choices may be invalid.

In quantifier form, semantic advice gives $\exists M,\alpha\;\forall n\;\forall x\in\{0,1\}^n:\mathrm{Promise}(M,x,\alpha(n))$ together with correctness on those same pairs. Hardwiring a fixed $s$ requires $\forall n\;\forall x\in\{0,1\}^n:\mathrm{Promise}(M,x,s)$, a strictly stronger statement. When $\alpha$ is eventually constant, finitely many exceptional input lengths can be hard-coded; an advice sequence that changes infinitely often has no such general repair.

More precisely, if any valid advice realization for $L$ is eventually constant, then $L$ already belongs to the corresponding no-advice class: patch its finite exceptional input lengths into the machine and run the stabilized variant on the tail. Thus a genuine semantic-advice separation must use an advice sequence with infinitely many changes. In Pervyshev's hierarchy construction, the advice supplies facts such as whether a candidate machine satisfies the semantic promise and what advice is correct for its padded simulation; its one-bit hierarchy is not a single global advice bit.

This distinction breaks a tempting advice-removal argument. Hao Wu's [2017 note](https://arxiv.org/abs/1711.11158) claims that if $CTIME(t)\subseteq CTIME(T)/A$, then a constant-advice computation can be split into $2^a$ fixed-advice machines, each of which is in $CTIME(t)$, and then recombined. Under standard semantic advice, the middle claim is not justified: a fixed advice string may be wrong at infinitely many lengths and the resulting machine may violate unambiguity or an error promise there. The formal semantic advice definition in Fortnow, Santhanam, and Trevisan's [hierarchy paper](https://theory.stanford.edu/~trevisan/pubs/promise.pdf) explicitly requires validity only for the correct advice, distinguishing this from the robust Karp--Lipton convention. Their paper notes that a hierarchy under the stronger Karp--Lipton convention would imply one without advice; that does not transfer automatically to the standard semantic hierarchy.

For $UP$, let $M(x,b)$ reject deterministically when $b=|x|\bmod2$, and otherwise branch into $\max(2,|x|)$ accepting paths. The advice sequence $s_n=n\bmod2$ makes this a valid $UP/1$ computation of the empty language. Neither fixed variant is unambiguous on infinitely many lengths. Therefore the advice hierarchy for $UTime[n^a]/1$ from [ECCC TR05-054](https://eccc.weizmann.ac.il/report/2005/054/) cannot be turned into an unadvised hierarchy by the displayed hardwiring argument without a new promise-preservation lemma. A 2021 ECCC account still describes the unadvised $BPP$ hierarchy as wide open, which reinforces that this claimed generic shortcut is not part of the accepted resolution of that problem.

As further context, [ECCC TR24-049](https://eccc.weizmann.ac.il/report/2024/049/) calls its hierarchy for the specialized oblivious class $O_2TIME$ the first uniform hierarchy theorem for a semantic class. This is not a direct theorem about $UP$ or $BPP$, but it is another reason to check the exact model hypotheses before treating Wu's generic claim as established.

The combination step itself is sound if promise validity is robust: after fixing each of the $2^a$ advice strings, obtain a lower-time advised decider for each resulting language, store all their advice blocks, and use the original $a$-bit selector to run only the matching decider. The missing step is the claim that each fixed variant is a valid semantic-class machine. This cleanly separates a potentially repairable wrapper from its unproved premise.

This lead has two independent ceilings. First, the displayed advice-elimination proof has a semantic-validity gap under the standard advice definition. Second, even if one repairs it and proves strict containments among fixed polynomial clocks for $UP$, the output has the form $\forall k\,\exists L_k$; it does not give one language outside $P=\bigcup_k DTIME(n^k)$. The latter requires $\exists L\in NP\,\forall k$, so ordinary per-clock hierarchy cannot be promoted to $P\ne NP$ by exchanging quantifiers.

**Operational rule:** whenever a proof fixes advice, guesses a witness encoding, changes a promise input, or enumerates semantic machines, write the promise predicate next to the transformation and prove it is preserved on all required inputs. If the proof assumes correctness only for a special advice sequence, do not treat off-sequence machine variants as class members.

### 2.6 Global unambiguity validity is undecidable

Let $U_{\mathrm{valid}}$ be the set of explicitly polynomial-clocked nondeterministic machine descriptions that have at most one accepting path on every input. Its complement is recursively enumerable: enumerate all input strings and the finite clock-bounded path pairs, and halt if two accepting paths are found. Thus $U_{\mathrm{valid}}\in\Pi^0_1$.

For hardness, from a deterministic machine $T$ build a nondeterministic machine $N_T$ that, on input $1^n$, simulates $T$ on blank input for $n$ steps, then rejects if $T$ has not halted and otherwise branches into exactly two accepting paths. It rejects non-unary inputs. A standard bounded universal simulation gives a polynomial clock $p_T(n)=C_T(n+1)^c$, with $C_T$ and fixed exponent $c$ effectively obtainable from the machine model and the description of $T$; include this clock in the output pair. If $T$ never halts, $N_T$ has no accepting paths and is unambiguous on every input. If $T$ halts at step $r$, every unary input of length at least $r$ gives two accepting paths. Therefore $T\in\overline{HALT}$ exactly when the clocked $N_T$ is in $U_{\mathrm{valid}}$. This proves $\Pi^0_1$-completeness.

**Finite-audit corollary.** For any tested input-length cutoff $B$, choose a deterministic $T_B$ that halts only after more than $B$ steps. Its reduction machine has no accepting paths on inputs of length at most $B$, yet is ambiguous on all sufficiently long unary inputs. Thus finite testing of inputs cannot certify global unambiguity; a proof needs an invariant covering every input length. This does not say finite tests are useless for finding counterexamples: one ambiguous input refutes validity immediately.

The proof-system lesson is precise: there is no general computable filter that enumerates all and only valid $UP$ machines from clocked nondeterministic descriptions. A diagonal construction must handle invalid candidates through an explicit promise-preserving guard, or prove its particular candidate machines unambiguous by construction. The undecidability result does not prevent the latter and does not itself separate $P$ from $NP$; it rules out only a generic effective validity check.

### 2.7 Proof-certified validity can miss valid descriptions

Fix a consistent, recursively axiomatized theory $T$ extending enough arithmetic for Godel's second incompleteness theorem. Let $H_T$ search for a $T$-proof of a contradiction and halt if it finds one. Apply the construction in Section 2.6 to obtain the explicit clocked machine $(N_{H_T},p)$. The theory $T$ can formalize the equivalence

$$
N_{H_T}\text{ is globally unambiguous}\quad\Longleftrightarrow\quad \mathrm{Con}(T).
$$

More explicitly, the middle statement is $\forall n\,\neg\mathrm{Halt}_T(n)$, where $\mathrm{Halt}_T(n)$ says that the proof search finds a contradiction within $n$ simulation steps. If such a halt occurs, input $1^n$ (or a longer unary input) has two accepting paths; if none occurs, every input is rejected.

If $T$ is consistent, $H_T$ never halts, so $N_{H_T}$ has no accepting paths and is genuinely unambiguous. But if $T$ proved this machine's global unambiguity, the formalized equivalence would let $T$ prove its own consistency, contradicting the second incompleteness theorem. Thus, assuming $T$ is consistent, there is a particular valid clocked machine description whose validity $T$ cannot certify. For $T=ZFC$, this is conditional on ZFC's consistency.

**Scope warning:** this does not show that a UP *language* lacks a provably unambiguous machine description: this constructed machine recognizes the empty language, which has an obvious deterministic representation. It only shows that proof enumeration is incomplete at the level of machine descriptions. A sound theory's proof-certified list can be a useful sound subclass, but it cannot be assumed to include every valid description. This is not a P-vs-NP separation.

### 2.8 The language-level enumeration dichotomy

Hartmanis and Hemachandra (1988, Lemma 2.7) prove the exact bridge the preceding code-level result lacks:

$$
UP\text{ has a polynomial-time many-one complete language}
\quad\Longleftrightarrow\quad
\text{some r.e. list of clocked categorical machines covers every language in }UP.
$$

Here *categorical* means globally unambiguous on every input, and *covers* means that each UP language is accepted by at least one listed machine. This is an enumeration of representatives, not necessarily of all valid machine codes.

**Complete language implies a covering list.** Fix a categorical machine $C$ for a UP-complete language. Enumerate all polynomial-time many-one reduction machines $g_i$ with clocks and output the compositions $C\circ g_i$. Each composition is categorical: $g_i$ is deterministic and $C$ has at most one accepting path on every output. Completeness ensures that every UP language occurs in this list up to its language.

**Covering list implies a complete language.** Let an effective enumerator output only clocked categorical machines $N_i$, and suppose their languages cover UP. Build one universal nondeterministic machine $U$ that receives an encoding of a candidate $N_i$, input $x$, a unary simulation budget $1^t$, and a finite computation transcript certifying that the enumerator actually output $N_i$. It checks the transcript deterministically; malformed or uncertified descriptions reject. It then simulates $N_i(x)$ for at most $t$ steps, preserving its accepting paths. This is polynomial in the total input length because $t$ is unary and the candidate description and transcript are part of the input. Every accepting simulation is for a member of the categorical list, so $U$ is categorical on *all* inputs, including malformed encodings (which reject). For any fixed listed $N_i$ with clock $p_i$, hardwire one valid output transcript and map $x$ to its encoding with budget $t=p_i(|x|)$. This map is polynomial-time for fixed $i$, and $x\in L(N_i)$ iff the encoded input is in $L(U)$. Thus $U\in UP$ and every UP language many-one reduces to $L(U)$.

This theorem reconciles the two enumeration facts: the set of all valid machine descriptions is not computable and is not r.e., but an r.e. *sublist* can still cover all UP languages if and only if UP has a complete language. The 1988 paper states that unrelativized existence of UP-complete languages was unknown; a 2024 paper still lists ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œUP has no many-one complete setsÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â as a conjecture, while constructing an oracle where UP lacks complete sets even though NP = PSPACE. Oracle results do not settle the unrelativized question. [HartmanisÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Hemachandra (1988)](https://doi.org/10.1016/0304-3975(88)90022-9), [DingelÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“EgidyÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“GlaÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸er (2024)](https://doi.org/10.4230/LIPIcs.MFCS.2024.50).

**Proof-theoretic corollary.** Let $F$ be a sound, effectively axiomatized theory. Enumerate machine descriptions together with $F$-proofs that they are categorical. Soundness makes this an r.e. list of valid machines. If every UP language had some $F$-provably categorical representation, this list would cover UP, so Lemma 2.7 would give a UP-complete language. Therefore, if UP has no complete language, then for every such $F$ some UP language has no representation whose categoricality $F$ can prove. This is a language-level result, but it is conditional on the unresolved no-UP-complete conjecture.

The no-complete conjecture would itself imply the desired separation. Let $B_P=\{(M,x,1^t):M\text{ accepts }x\text{ within }t\text{ steps}\}$ for deterministic machines $M$. Universal bounded simulation puts $B_P$ in P, and every $L\in P$ reduces to it by hardwiring a decider and its polynomial clock. Thus $B_P$ is P-complete under polynomial-time many-one reductions. If $P=UP$, it is UP-complete; contrapositively, if UP has no many-one complete language, then $P\ne UP$ and hence $P\ne NP$. This is stronger than the target and still unproved. The converse is false relative to oracles: HartmanisÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Hemachandra also construct an oracle with $P^A\ne UP^A$ while $UP^A$ does have complete sets, so UP-completeness by itself does not collapse the classes.

**Proof-complexity bridge.** KÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶bler, Messner, and TorÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡n (2003, Theorems 10ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“11) prove that a p-optimal CookÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Reckhow proof system for $TAUT$ implies a UP-complete language, even under logspace many-one reductions. Their construction gives a more local promise guard than the enumeration transcript above: encode the assertion that a clocked machine has at most one accepting path on all inputs of length at most $n$ as a coNP statement, reduce it to a tautology, and include a proof of that tautology in the universal machine's input. A sound proof certifies unambiguity on the particular simulated input length; p-optimality supplies short, efficiently constructible proofs for the canonical formulas arising from each fixed categorical machine. In the source's strict $|z|<n$ convention, use cutoff $n=|x|+1$ for an input $x$ to cover the endpoint. The resulting proof-carrying universal simulator is globally UP.

There is a one-way route from this proof-system problem to the target: if $P=NP$, then $TAUT\in P$ and the map that outputs its input when it is a tautology (and a fixed tautology otherwise) is a p-optimal proof system. Therefore, proving that no p-optimal proof system for $TAUT$ exists would imply $P\ne NP$. The converse is not established here; neither $P\ne NP$ nor $P\ne UP$ is known to rule out p-optimal systems. See [KÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶blerÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“MessnerÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“TorÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡n (2003)](https://doi.org/10.1016/S0890-5401(03)00058-0).

### 2.9 A precise unique-SAT target for separating $P$ from $UP$

Theorem 2.1 of Hartmanis and Hemachandra gives a useful exact reformulation. Let $\mathcal{S}$ range over polynomial-time decidable sets of Boolean formulas such that every formula in $\mathcal{S}$ has at most one satisfying assignment. Then

$$
P\ne UP
\quad\Longleftrightarrow\quad
\exists\mathcal{S}\in P:\;\mathcal{S}\subseteq\mathrm{UniqueSAT}_{\le1}\ \text{and}\ \mathcal{S}\cap SAT\notin P.
$$

For the forward direction, choose a clocked categorical machine $N$ for some $L\in UP\setminus P$. Use a parsimonious CookÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Levin encoding $\varphi_{N,x}$ in which accepting paths correspond one-to-one with satisfying assignments. The range $\mathcal{S}_N=\{\varphi_{N,x}:x\in\{0,1\}^*\}$ is polynomial-time recognizable because the encoding records $N,x$ and has checkable canonical syntax. Since $N$ is categorical, every formula in this range has at most one satisfying assignment. If $\mathcal{S}_N\cap SAT$ were in P, then $L(N)$ would be in P, contradiction.

For the reverse direction, decide whether $\varphi\in\mathcal{S}$ deterministically, then guess and verify a satisfying assignment. Inputs outside $\mathcal{S}$ have no accepting paths; inputs inside have at most one. This is a categorical polynomial-time machine for $\mathcal{S}\cap SAT$. If that language is not in P, then $P\ne UP$.

Because $P\subseteq UP\subseteq NP$, a proof of this target would imply $P\ne NP$. It is a reformulation, not a lower bound: the unpaid obligation is to produce one such explicit $\mathcal{S}$ and prove $\mathcal{S}\cap SAT\notin P$. Finite SAT experiments can test individual instances but cannot establish that lower bound. The characterization appears in [HartmanisÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Hemachandra (1988)](https://doi.org/10.1016/0304-3975(88)90022-9).

### 2.10 Worst-case one-way functions are exactly the $P$ versus $UP$ gap

Grollmann and Selman (1988), building on Ko, characterize a particular *complexity-theoretic* notion of one-way function. Here $f:\{0,1\}^*\to\{0,1\}^*$ is total, polynomial-time computable, injective, and honest (input and output lengths are polynomially related); it is one-way if no polynomial-time total inverter $g$ satisfies $f(g(y))=y$ for every $y$ in the range of $f$. This is a worst-case notion. It is weaker than cryptographic average-case one-wayness.

$$
P\ne UP\quad\Longleftrightarrow\quad\text{a function of this kind exists}.
$$

**One-way function implies $P\ne UP$.** Given such an $f$, define

$$
L_f=\{(u,y):\exists z\le_{ll}u\;[f(z)=y]\},
$$

where $\le_{ll}$ is length-lexicographic order. To recognize $L_f$ unambiguously, on input $(u,y)$ set $m=|u|$ and guess exactly $m+1$ bits as the rank of $z$ among all strings of length at most $m$. There are $2^{m+1}-1$ such strings, so each has one rank and one guess path; reject the one unused rank, then check $z\le_{ll}u$ and $f(z)=y$. Injectivity gives at most one accepting rank. Honesty gives a polynomial bound $N(|y|)$ on the length of any preimage of $y$. If $L_f$ had a P decider, query it at length-lex thresholds to binary-search the unique preimage among strings of length at most $N(|y|)$ using polynomially many queries of polynomial size. This would invert $f$ in polynomial time on its range, a contradiction. Hence $L_f\in UP\setminus P$.

Conversely, a polynomial-time inverter immediately decides $L_f$: compute its candidate preimage for $y$, verify $f(z)=y$, then check $z\le_{ll}u$. Thus $L_f\in P$ iff $f$ is polynomial-time invertible.

**$P\ne UP$ implies a one-way function.** Choose $L\in UP\setminus P$ and a clocked categorical machine $M$ for it. Encode complete computation transcripts canonically, including their input. Define

$$
f_M(z)=\begin{cases}
1y,&z\text{ is a valid accepting transcript of }M(y),\\
0z,&\text{otherwise.}
\end{cases}
$$

Transcript checking is polynomial time. The tags separate the two cases; in the first case, unambiguity gives at most one accepting transcript for each $y$, so $f_M$ is injective. The clock on $M$ makes input and output lengths polynomially related, so $f_M$ is honest. If a polynomial-time inverter existed, run it on $1y$ and verify whether its output maps to $1y$. That test decides whether $M$ accepts $y$, putting $L$ in P. Thus $f_M$ is one-way.

Since $UP\subseteq NP$, $P\ne UP$ implies $P\ne NP$. The theorem therefore makes a proved worst-case one-way function a valid route to the separation. It also exposes the exact debt in the project's finite-substrate proposal: checking modular exponentiation and defining a discrete logarithm prove efficient evaluation and describe an inverse, but they do not prove that no polynomial-time inverter exists. A fixed modulus is finite and cannot witness asymptotic one-wayness. An unbounded algebraic proposal must additionally define one uniform total function on bit strings, prove injectivity and honesty under its encoding, and establish worst-case non-invertibility. For $j\mapsto g^j\bmod p$, exponents must be restricted or encoded so collisions modulo the group order do not destroy injectivity. Meeting these bookkeeping conditions would make the target well-formed; the non-invertibility lower bound remains the separation-level obstacle.

**A precise totalization of the discrete-log candidate.** This repairs the function-definition obligations without claiming hardness. A valid input is a canonical tuple $1\langle p,g,C,x\rangle$, where $p\ge3$ is prime, $C$ is the sorted complete prime factorization $p-1=\prod_i q_i^{e_i}$, $1\le g<p$ passes $g^{(p-1)/q_i}\not\equiv1\pmod p$ for each distinct $q_i$, and $0\le x\le p-2$. Primality, the factorization product, and the primitive-root tests are polynomial-time checkable. Define

$$
F(1\langle p,g,C,x\rangle)=1\langle p,g,C,g^x\bmod p\rangle
$$

on valid tuples, and $F(s)=0s$ on every malformed or invalid string. The leading tags separate the two branches. In the valid branch, $g$ has order $p-1$, so distinct canonical exponents give distinct outputs; in the invalid branch, $s\mapsto0s$ is injective. The output retains $p,g,C$, and both $x$ and $g^x\bmod p$ use at most $O(\log p)$ bits, so input and output lengths are polynomially related. Repeated squaring and validation compute $F$ in polynomial time. Its range points beginning with $0$ invert by dropping the tag; its valid range points beginning with $1$ invert exactly by computing the certified discrete logarithm. Thus $F$ is one-way iff no uniform polynomial-time algorithm computes discrete logs for all supplied certified prime-order cyclic-group instances. This is a clean conditional candidate specification, not a proof that it is one-way. The certificate avoids needing to find the factorization or a generator during evaluation, and the totalization handles all noninstances without introducing collisions.

**Exact conversion to unique-SAT for this candidate.** For any injective polynomial-time $F$, the threshold language $L_F=\{(u,y):\exists z\le_{ll}u,\ F(z)=y\}$ is in UP. On input $(u,y)$, a machine with $m=|u|$ guesses exactly $m+1$ bits, decodes that rank among the $2^{m+1}-1$ strings of length at most $m$, rejects the unused rank, and accepts exactly when the decoded $z\le_{ll}u$ and $F(z)=y$. Each $z$ has one guess path, and injectivity gives at most one accepting $z$. A parsimonious CookÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Levin encoding of this machine gives a canonical formula $\varphi_{u,y}$ with one satisfying assignment iff $(u,y)\in L_F$, and at most one satisfying assignment always. Choose a canonical encoding that records the source pair in reserved, forced input-tag variables; their unit clauses make the pair recoverable and add no multiplicity. Then the family $S_F=\{\varphi_{u,y}:(u,y)\in\{0,1\}^*\times\{0,1\}^*\}$ is P-recognizable by decoding the tag and checking the canonical syntax. Moreover, $S_F\cap SAT$ is in P iff $L_F$ is in P: each reduces to the other by the canonical encoding. The threshold-search proof above gives $L_F\in P$ iff $F$ has a polynomial-time inverter. So for the certified discrete-log candidate, the unique-SAT lower bound and the worst-case inversion lower bound are exactly the same unpaid theorem, with only a parsimonious representation change between them.

This theorem is a bridge, not an independent proof strategy: the abstract construction from $L\in UP\setminus P$ is conditional on the very separation sought, while an explicit arithmetic candidate pays the full inverse lower bound. Source: [GrollmannÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Selman (1988), *Complexity Measures for Public-Key Cryptosystems*](https://epubs.siam.org/doi/10.1137/0217018).

### 2.11 Three equivalent faces of unambiguous hardness

The categorical-language, unique-SAT, and inverse-function leads are three encodings of the same intermediate separation, not three independent pieces of evidence:

| Form | Exact target | Conversion already available |
|---|---|---|
| Language | Some $L\in UP\setminus P$ | Direct definition of $P\ne UP$ |
| Formula slice | Some $S\in P$, every $F\in S$ has at most one satisfying assignment, and $S\cap SAT\notin P$ | HartmanisÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Hemachandra Theorem 2.1 (Section 2.9) |
| Inverse map | A total honest injective polynomial-time $f$ with no polynomial-time inverter | GrollmannÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Selman characterization (Section 2.10) |

All three targets imply $P\ne NP$ because $UP\subseteq NP$. They require the stronger intermediate fact $P\ne UP$; a proof of $P\ne NP$ alone is not known to imply $P\ne UP$. Beigel, Buhrman, and Fortnow construct an oracle $A$ with $P^A=UP^A\ne NP^A$, and describe it as making satisfiability tractable on formulas with at most one satisfying assignment while $P^A\ne NP^A$. This does not decide the unrelativized question, but it shows that a proof of P versus NP cannot follow from a relativizing argument that only separates $P$ from $UP$. The shared invariant is unique-witness structure plus an unconditional proof that deciding or extracting that unique object is not in P. A failed discrete-log candidate would not refute the unique-SAT route, and a finite unique-SAT search would not support one-wayness; credit progress only when a proof crosses the common $P$ versus $UP$ boundary. See [BeigelÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“BuhrmanÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Fortnow, STOC 1998](https://doi.org/10.1145/276698.276737) and their [author-hosted paper](https://lance.fortnow.com/papers/files/newiso.pdf).

The June 2026 paper by Carleton et al. offers a useful technique and a sharp scope test. Its Theorem 7 proves $P=UP_{\le f(n)}$ iff $P=UP_{\le f(n)+O(1)}$ for nondecreasing $f$: the proof removes the lexicographically least accepting path on inputs with multiple accepting paths (ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œpath poisoningÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â), then uses the assumed lower-ambiguity collapse to decide the resulting auxiliary languages. Theorem 4 constructs an oracle separating $P=UP_{\le O(1)}$ from every unbounded ambiguity bound up to $2^{n^{O(1)}}$; Theorem 12 gives a broader limit on robust links. So path poisoning is a real bounded-ambiguity collapse method, but its proof relies on the collapse assumption and does not lift $P=UP$ to $P=NP$. A nonrelativizing bridge would still be needed. See [Carleton et al., *Linked Fates* (2026)](https://arxiv.org/abs/2606.20399).

### 2.12 Witness polarity and positive self-reference

The diagonalization obstacle can be described as a polarity gap. A verified accepting path is positive evidence: one short transcript proves that a machine accepts. Rejection means that no accepting path exists, which is negative information. If an effective list outputs only categorical clocked machines, an enumerator-certified universal simulator with an explicit unary time budget is in UP; its complement is in coUP. The direct diagonal language ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œaccept exactly when the listed machine does not acceptÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â therefore lands in coUP. Without the explicit unary budget, machine-dependent polynomial exponents also defeat a single fixed simulation clock. Global unambiguity controls the number of positive accepting paths, but does not make nonacceptance easy to certify.

There is a finite fixed-point obstruction for one tempting family of self-reference constructions. Suppose a construction defines its outputs on $m$ selected inputs using only positive acceptance witnesses from a candidate machine. The induced map $F:\{0,1\}^m\to\{0,1\}^m$ is monotone in the coordinatewise order: adding positive accepting evidence cannot remove an existentially supported output. Every such map has a fixed point. Starting with $v_0=0^m$ and iterating $v_{t+1}=F(v_t)$ gives an ascending chain because $0^m$ is the bottom element and $F$ is monotone; finiteness makes the chain stabilize at $v=F(v)$. Therefore this restricted finite positive-evidence scheme cannot force disagreement for every possible acceptance vector. This does not rule out arbitrary diagonalization: a successful strategy could use nonmonotone information, exploit a complexity-theoretic structure theorem, or avoid bit-flipping a candidate's language altogether.

The same lens extends to all languages. The powerset lattice $2^{\{0,1\}^*}$ is complete, so Tarski's fixed-point theorem gives a fixed point for every monotone language transformer $\Phi$. An oracle machine that uses only positive membership queries to a candidate language induces a monotone transformer: every accepting computation relative to $A$ remains accepting relative to any superset $B\supseteq A$. Thus a positive-only oracle self-reference cannot force $\Phi(A)\ne A$ for every possible language. This is not a UP diagonalization barrier by itself, since Tarski's fixed point need not be decidable or lie in UP. The route would need either a proof that all such fixed points escape the admissible machine list, or a genuinely nonmonotone/structural ingredient.

The ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œpath poisoningÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â result of Carleton et al. is a useful comparison, not an escape from this barrier. Their proof can remove a least accepting path once the assumption $P=UP_{\le f(n)}$ lets it decide auxiliary languages, but the operation is conditional on that lower-ambiguity collapse. The project needs a nonrelativizing way to get the required negative information or a different invariant. [Idea 129](ideas.md) records the exact restricted lemma and next checks.

### 2.13 Total permutations supply witnesses on both sides

There is a sharper function branch than the injective one-way-function route. A total, honest, polynomial-time bijection $f:\{0,1\}^*\to\{0,1\}^*$ is a *one-way permutation* when no polynomial-time algorithm computes its inverse. Homan and Thakur prove that such a permutation exists exactly when $P\ne UP\cap coUP$. This implies $P\ne NP$: if $P=NP$, then $UP=P$ and, since $P$ is closed under complement, $coUP=P$ as well. The result concerns worst-case inversion, not cryptographic average-case hardness. The BeigelÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“BuhrmanÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Fortnow oracle with $P^A=UP^A\ne NP^A$ also has $coUP^A=P^A$, so this stronger sufficient target does not evade the relativization barrier. [HomanÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Thakur (2003), Theorem 3.1](https://doi.org/10.1016/S0022-0000(03)00068-0).

The key proof mechanism exposes a useful witness-polarity principle. Let $B(n)$ be a polynomial honesty bound for $f$, and define

$$
T_f=\{(u,y): \text{the unique }z\text{ with }f(z)=y\text{ satisfies }z\le_{ll}u\}.
$$

For membership, guess the unique preimage $z$ of length at most $B(|y|)$, verify $f(z)=y$ and $z\le_{ll}u$. This puts $T_f$ in UP. For nonmembership, onto-ness guarantees that $y$ has a preimage, and uniqueness guarantees that it is the same single $z$; guess and verify $f(z)=y$ and $z>_{ll}u$. This puts the complement in UP. Fixed-width rank guesses can encode the bounded candidate strings one-to-one, so both verifiers remain unambiguous. Thus $T_f\in UP\cap coUP$.

Moreover, $T_f\in P$ exactly when $f$ has a polynomial-time inverse. An inverse decides $T_f$ by comparing the recovered preimage with $u$. In the other direction, a $T_f$ decider locates the unique preimage by binary search in length-lex order over the $2^{B(|y|)+1}-1$ strings of length at most $B(|y|)$, using $O(B(|y|))$ threshold queries of polynomial size. Therefore a one-way permutation gives an explicit language in $UP\cap coUP\setminus P$.

This identifies what totality adds to the earlier injective map. For an injection that is not onto, a threshold query's negative answer may mean either ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œthe preimage lies laterÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â or ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œthere is no preimageÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â; the latter has no preimage witness. For a permutation, every output has exactly one preimage, so the two sides of the threshold have positive, unique certificates. The new model phrase is **two-sided unique witness**: onto-ness converts a search boundary into a language in $UP\cap coUP$. It resolves the syntactic polarity problem for this specific encoding, but it does not prove that the language is hard.

**Finite-model-logic form of the same target.** GrÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤del's 1994 characterization connects $P=UP\cap coUP$ to the weak definability principle: for every first-order logic on finite structures that captures $P$, every total query defined *implicitly* with a unique relation on each input structure is also *explicitly* definable by a formula of that logic. For a fixed total implicit definition, a verifier guesses a candidate relation and checks the defining formula plus whether the queried tuple belongs to it (or does not). The global uniqueness guarantee of that fixed definition ensures at most one successful relation witness; the verifier does not test uniqueness afresh. With fixed relation arity, a canonical fixed-length table encoding of the relation has polynomial size and gives one guess path per relation. Thus the implicit query naturally has both positive and negative unambiguous certificates; the weak definability principle says those queries can be computed in P and then named explicitly in a P-capturing logic. A failure of this principle for a suitable logic is another exact expression of the same $P$ versus $UP\cap coUP$ debt, not an independent proof or a ZFC independence result. See [GrÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¤del (1994), *Definability on Finite Structures and the Existence of One-Way Functions*](http://www.logic.rwth-aachen.de/pub/graedel/Gr-mlcs94.ps).

For the permutation candidate, this can be made concrete in ordered structures. Encode an output $y$ and polynomially many witness cells, with the cell bound supplied by the honesty polynomial. Let a relation variable $W$ encode a canonical padded preimage string; require it to decode to $z$ with $G(z)=y$, and require the unique empty relation on malformed structure encodings. The forward test is polynomial-time, so the [ImmermanÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Vardi characterization](https://doi.org/10.1016/S0019-9958(86)80029-8) gives a fixed $\mathrm{FO(LFP)}$ formula to verify it on ordered structures. Because $G$ is a permutation, each valid input structure has exactly one such $W$, making this a total implicit definition. If an explicit $\mathrm{FO(LFP)}$ formula defined $W$, evaluating it at each cell would recover $G^{-1}(y)$ in polynomial time. Thus one-wayness of this specific candidate would manifest as a concrete failure of weak definability. This does not remove the lower-bound debt; it gives a precise finite-model-theory encoding of it.

**Permutation repair of the certified discrete-log map.** Retain the canonical valid encodings $1\langle p,g,C,x\rangle$ from Section 2.10, where $p$ is an odd prime, $C$ is its complete canonical prime factorization certificate for $p-1$, $g$ is certified as a primitive root, and $0\le x<p-1$. Let $V$ be the P-decidable set of these encodings and define

$$
G(s)=\begin{cases}
1\langle p,g,C,(g^x\bmod p)-1\rangle,&s=1\langle p,g,C,x\rangle\in V,\\
s,&s\notin V.
\end{cases}
$$

For fixed $(p,g,C)$, exponent indices $x\in\{0,\ldots,p-2\}$ and output indices $(g^x\bmod p)-1\in\{0,\ldots,p-2\}$ are both the same finite set; primitiveness makes this block map a bijection. The parameters are retained, so blocks do not mix. The complement of $V$ is fixed pointwise. Hence $G$ is a permutation of *all* bit strings. Canonical factorization encoding keeps the tuple length polynomially bounded by $\log p$, while the retained $p$ field lower-bounds output length; malformed strings are fixed, so $G$ is honest. AKS primality tests, multiplication checks, and modular exponentiation make validation and evaluation polynomial-time. An inverse for $G$ is equivalent to a uniform polynomial-time algorithm for the certified discrete-log instances: on valid outputs recover the unique $x$ from $g^x\equiv a+1\pmod p$, and on invalid strings return the string itself.

Thus the exact unpaid debt for this *particular* permutation remains a worst-case discrete-log inverse lower bound. If established, it would prove the stronger separation $P\ne UP\cap coUP$, and therefore $P\ne NP$. The literature equivalence does not say this particular arithmetic candidate is hard whenever the class separation holds; it only guarantees that some one-way permutation exists under that separation. The converse direction of HomanÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Thakur uses a nontrivial totalization of partial onto one-way functions, so it is not a shortcut to proving the discrete-log lower bound.

**Hard witness choice for an easy language.** HomanÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Thakur's Theorem 3.4 gives two further equivalent forms: $ÃƒÆ’Ã†â€™Ãƒâ€¦Ã‚Â½ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£^*\in HiPermUP$, and the existence of some $L\in P\cap HiPermUP$. Here $HiPermUP$ means that a UPTM accepts $L$, its unique-witness function permutes $L$, and that witness function is not polynomial-time computable. This isolates the difficulty in selecting the unique proof object, even when membership in the language itself is easy. For $ÃƒÆ’Ã†â€™Ãƒâ€¦Ã‚Â½ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£^*$, compare a proposed string $y$ with the unique witness of $x$: both sides have the same accepting-path certificate, so the comparison lies in $UP\cap coUP$; if it were in P, binary search would compute the witness function. This is a repackaging of the same separation, not new hardness. It suggests that any logic-based construction should focus on definability of a canonical witness choice rather than only on the truth value of membership. [HomanÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Thakur (2003), Theorem 3.4](https://doi.org/10.1016/S0022-0000(03)00068-0).

### 2.14 The uniform-clock obstruction to diagonalizing inverse algorithms

A tempting construction is to enumerate candidate polynomial-time inverters $I_i$, simulate each on a chosen output, and locally alter a permutation so that $I_i$ fails. Let $n$ be the inverter's output-string input length and $m$ the permutation's preimage-input length. Honesty gives $m\le n^a$ for one fixed $a$, while the forward computation has one fixed clock $m^C\le n^{aC}$. Simulating $I_i$ through its own clock $n^{k_i}$ cannot fit this bound for unbounded $k_i$. Padding the output to length $N$ changes the forward allowance to at most $N^{aC}$ but the inverter budget to $N^{k_i}$, so the mismatch remains. Keeping the inverter input short while making the preimage much longer would evade that cost only by violating the permutation's fixed honesty bound.

The quantifiers matter. Diagonalizing against every polynomial inverter requires defeating every clock exponent with one fixed polynomial-time forward map. A separate map $F_c$ that handles inverters of exponent at most $c$ does not give one one-way permutation. This rejects the naive clocked-simulation-plus-padding template, not all diagonalization: a successful construction would need a way to expose an inverter's error with a polynomially bounded local check independent of its exponent, or use a nonrelativizing structure theorem. [Idea 131](ideas.md) records this failed route and the exact cost mismatch.

### 2.15 Public-input neutrality cannot coexist with a unique message

A newly audited arXiv preprint claims $P\ne NP$ by assigning a linear-length message $M(Y)$ to a public SAT instance $Y$, proving that every satisfying witness yields the same message, and then lower-bounding the time-bounded description length of $M(Y)$ given $Y$. The proposed upper bound under $P=NP$ is the familiar bit-by-bit SAT self-reduction. The questionable step is the lower-bound interface: it classifies public template/surface reads as neutral (zero pairwise distinction cost), then claims every ordinary observer of $Y$ has a trace made only of neutral, safe-buffer, and hidden-gauge evidence.

Here is the exact consistency test. Fix a message coordinate $j$ and let $\Gamma_j$ couple worlds with $B_j=0$ and $B_j=1$. If all satisfying witnesses over a given $Y$ have the same message, then $B_j=b_j(Y)$ on the sampler's support. Consequently every pair $(\omega^0,\omega^1)$ in the support of $\Gamma_j$ must have

$$Y(\omega^0)\ne Y(\omega^1).$$

Otherwise the same public instance would have two satisfying witnesses with opposite $j$th message bits. Therefore the full public input is never pair-neutral. If each accessible input-symbol read is normalized as a neutral atom and neutral coherence says those atoms agree at both endpoints of every coupled pair, then reading the whole encoded input forces $Y(\omega^0)=Y(\omega^1)$, a contradiction. More generally, every public feature that differs across these pairs must be charged by the evidence ledger; it cannot be declared free merely because it is not literally a message-bit tag.

This catches the gap in the paper's observer bridge: the evidence normal form is stipulated to admit only neutral/safe/gauge leaves, while the write-up does not establish that arbitrary computations of the complete public CNF can be represented using that restricted interface with the claimed cost bounds. Under $P=NP$, SAT self-reduction is an ordinary polynomial-time function of the public formula. It must be among the observers covered by the lower bound. If its input reads are all neutral, the trace theorem would say its exact prediction has zero advantage; if some public formula reads are not neutral, the claimed atom-completeness and neutral-coherence budget has not yet accounted for them. The paper's own remark that public CNF syntax may globally determine a unique message makes this an essential issue, not a cosmetic encoding detail.

The interface issue is explicit in the current text's definitions. Appendix D.5 says $Y$ is fully visible and the syntax discipline is not an access restriction. Yet Definition 5.23 specifies only a finite set of primitive reads; Theorem 5.25 and Lemma 6.6 cover observers using that interface, while D.29-D.31 map chosen template/surface symbols to neutral atoms and D.33 assumes completeness for primitives it generates. The missing bridge is a compiler from an arbitrary ordinary machine's reads of the full encoding to these primitives, with a proved cost bound. Include a complete-input read and it is phase-distinguishing, so cannot satisfy neutral coherence; omit parts of the input and ordinary observer coverage is unproved. This is the exact interface obligation, not merely a question of whether the message appears as a literal tag. [Current paper text](https://arxiv.org/html/2510.08814).

**Neutral-sufficient-statistic lemma.** Fix an opposite-message coupling $\Gamma_j$ of total mass one. If a finite vector of public observations $A(Y)=(A_1(Y),\ldots,A_q(Y))$ losslessly determines the encoded public instance on the support, then every coupled pair has $A(Y^0)\ne A(Y^1)$ because its message bits differ and each bit is fixed by $Y$. Consequently

$$
\sum_{i=1}^{q}\Gamma_j[A_i(Y^0)\ne A_i(Y^1)]\geq1.
$$

This says any complete finite public read transcript must contain a phase-separating observation; it cannot be composed solely of zero-derivative neutral atoms. A valid budget may charge that observation, but must then prove a useful bound for its charge. The current interface defines neutralization syntactically and does not establish such a cost bound for a lossless representation of all of $Y$. See [Idea 132](ideas.md) and [audit Section 94](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

The scale is decisive for the paper's desired aggregate estimate. If $|S|=\Theta(t)$ message coordinates are each fixed by $Y$, then for every $j\in S$ the full-input bit vector changes somewhere on every $\Gamma_j$-coupled pair. Summing the per-bit disagreement charges over $j$ gives at least $|S|=\Theta(t)$, so a complete-input charge cannot feed the claimed $o(t)$ budget. Declaring those reads neutral gives zero charge but contradicts pair-neutrality. A repaired proof would need a new resource-sensitive argument about computations over the full input, strong enough to beat this linear information flow and to cover the hypothetical SAT search.

**Reusable principle ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â visible-target incompatibility.** If a target is a well-defined function of the full public instance, any coupling of opposite target values must change the public instance. Exact pairwise invariance of all input symbols cannot be a free-information premise in a lower bound for computing that target. To recover a valid proof route, replace pair-neutrality of raw syntax with a proved resource-sensitive bound for every ordinary input-reading algorithm, including global computations over the formula. That replacement is itself the hard computational statement; statistical mixing of hidden witness variables does not supply it.

This sharpens the earlier full-input observer warning in Idea 122 / audit Section 84. The conclusion is limited: it identifies a missing/contradictory interface requirement in the preprint's stated proof architecture, not a theorem that all coupling arguments fail, and not a P-vs-NP proof. See [Idea 132](ideas.md) and audit Section 94. Source under audit: [Goertzel, arXiv:2510.08814, v2 submitted 22 April 2026](https://arxiv.org/abs/2510.08814).

### 2.16 Gauge entropy is not quotient hardness

The same preprint introduces a hidden representative $g$ and a quotient $z=x\oplus g$. Its gauge action sends $(x,g,z,\xi,M)$ to $(x\oplus s,g\oplus s,z,\xi,M)$, preserving both satisfiability and message. This creates a useful exact check on any argument that charges message prediction to hidden-gauge entropy.

For every satisfying witness, choose $s=g$. The transformed witness is

$$x'=x\oplus g=z,\qquad g'=0,\qquad z'=z,$$

and remains satisfying with the same $M$. Thus every support formula has a satisfying assignment with the entire gauge vector fixed to zero. Under $P=NP$, a polynomial SAT search can find such a witness: add the unit constraints $g_v=0$ for all gauge coordinates and run the usual bit-fixing self-reduction on the resulting still-satisfiable CNF. The added clauses are polynomial in the instance size.

In the stated verifier, lock, buffer, and readout constraints depend on $z$ and auxiliary variables, while $x,g$ occur to realize $z=x\oplus g$. Substitute $g=0,x=z$; the gauge equation becomes tautological, and its Tseitin auxiliaries can be recomputed or dropped. This yields the quotient witness relation on $(z,\xi,M)$. Any quotient witness extends to a full canonical-gauge witness in polynomial time, and any full witness can first be gauge-transformed and then projected. Thus the message-search problems are polynomial-time interreducible. Any actual hardness has to reside in finding a quotient completion, not in reproducing the sampler's arbitrary gauge representative.

The sampler may nevertheless have $g\sim\mathrm{Unif}(\{0,1\}^{V})$ conditional on $Y,z$. That entropy describes which representative the sampler happened to choose. It does not force an algorithm that seeks an invariant message to recover that sampled representative. There is a semantic fork in the evidence argument: if a gauge atom refers to the sampler's $g$, the SAT search's canonical witness need not make that atom true; if it refers to the algorithm's chosen witness, that witness's gauge is fixed by the algorithm and the sampler's product-uniform entropy lemma does not apply to it. In either interpretation, a separate theorem must connect successful computation of the gauge-invariant $M(Y)$ to correctly predicting the sampler's random $g$.

Under the same $P=NP$ assumption used for the claimed contradiction, the distinction is sharp: the restricted SAT self-reduction computes $M(Y)$ perfectly with a satisfying witness whose gauge is $0$, while the sampler's uniform gauge equals $0$ with probability $2^{-|V|}$ conditional on $Y$ (by the stated hidden-gauge product law). Thus message success does not entail predicting the sampled representative.

This is **representative entropy versus quotient hardness**. Randomizing a redundant witness representation is not itself a lower bound for computing an invariant of its orbit. The actual hard object would have to be the quotient/message information encoded by the public constraint system, with all public reads charged and the observer allowed to choose any satisfying representative. This supplements, rather than replaces, the public-input incompatibility in Section 2.15. See [Idea 133](ideas.md) and audit Section 95. The source explicitly states the gauge symmetry and message invariance in Lemma 4.15 and the product-uniform representative law in Lemma D.18; it also bars a gauge-fixing rewrite in Corollary 5.21, but that syntactic normalizer rule does not by itself restrict a P-time SAT search from adding the valid $g=0$ unit constraints. [Current paper text](https://arxiv.org/html/2510.08814).

This gives a general design rule for witness symmetries: if a group action preserves $Y$ and the verifier relation, the single-message promise forces the message to be invariant on its orbits. Randomizing only the orbit representative cannot hide a target that is a function of the orbit. Search for an efficient canonical section first; if one exists, prove hardness on the quotient rather than charging the representative entropy.

### 2.17 Clock-specific hardness and the padding rate test

Clock dependence has two different roles. The contradiction's quantifiers can be read as follows: $P=NP$ supplies one exponent $D_*$ and one SAT-search program; the proposed lower bound supplies, for each fixed $D$, an ensemble and positive constants tailored to that $D$. Instantiate the latter at $D_*$ and take the message length large enough to beat the one program's constant description. No construction uniform over all $D$ is needed for this step. A single sampler hard against every polynomial-time decoder is a stronger goal, because it must have one fixed polynomial sampling exponent while its hardness clock grows.

For a padding-only assembly, suppose the construction at hardness clock $d$ has a base public input of length $m$, sampling cost $m^{a_d}$, and a proved lower bound against decoders running in time $m^d$. Pad the instance to length $N=m^{r_d}$ while preserving its message and allowing decoders on the padded instance to simulate on the base input. A single polynomial-time sampler requires $a_d/r_d$ to remain bounded (and also requires uniform cost to choose the index and write padding). If every sufficiently large selected block must exclude every fixed decoder clock $N^k$, the translated base clock $m^{r_d k+O(r_d)}$ requires $d/r_d\to\infty$, hence $d/a_d\to\infty$. If only arbitrarily large hard blocks are required, an effectively selectable subsequence with unbounded $d/r_d$ may suffice, so the corresponding necessary rate is unbounded $d/a_d$. If $a_d=\Omega(d)$, neither version can make the translated hardness clock unbounded by padding alone. Even when the rate test passes, uniform schedule, construction, parameter thresholds, and hardness transfer remain to prove.

Applied to the audited preprint, its Section 11 fixes $D_*$ before choosing the ensemble, which is the right order for its proposed contradiction. Section 12 allows constants to depend on each fixed $D$, and Hypothesis 12.3 requests polynomial-time instantiations for each fixed pair $(D,B)$; the text gives no single construction-time exponent or rate relating it to $D$. This blocks an inference to one fixed hard sampler or one-way function, but it is not by itself a flaw in the fixed-$D_*$ contradiction. The independent public-input and gauge-quotient gaps remain. See [Idea 134](ideas.md#idea-134---a-rate-condition-for-padding-clock-specific-hard-ensembles) and [audit Section 96](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

### 2.18 A class-relative decompressor must be uniform

A June 2026 preprint defines a class-relative witness complexity by minimizing over both a near-shortest description $d$ and an arbitrary machine $M\in\mathbf P$, but constrains only $|d|$ and the runtime on that one input. Since $M$ may change with the object and its description length is uncharged, this quantity is degenerate for polynomially long outputs.

**Constant-printer lemma.** For every string $x$ of length $N$, let $M_x$ ignore its input and print $x$. This is a polynomial-time machine: for the fixed machine $M_x$, its constant output time $O(N)$ is bounded by a polynomial in every input length. Choose any $d$ with $U(d)=x$ and $|d|\leq K(x)+c_0$. The definition then gives

$$
\gamma_{\mathbf P}(x)\leq T_{M_x}(d)=O(N).
$$

The machine's code can contain all of $x$, but the definition does not charge that code or require the same $M_x$ for different strings. Thus a claim that $\gamma_{\mathbf P}(x)$ is superpolynomial in an instance length cannot follow for strings whose output length is polynomial in that instance length. In the preprint's SAT family, $x_\varphi=(1,y_\varphi)$ has length at most $|\varphi|+1$, so a machine that simply prints $x_\varphi$ gives a linear-time decompressor under the stated definition, regardless of SAT hardness.

More generally, $K(x)\leq |x|+O(1)$, so the near-shortest input has length $O(|x|)$, and the printer can also read it if required. Conversely, in the paper's standard output-tape Turing model, writing an output of length $N$ takes at least $N$ steps. Therefore, for one model-dependent constant $C$,

$$
|x|\leq\gamma_{\mathbf P}(x)\leq C(|x|+1)
$$

for every string $x$. The class-relative measure is thus $\Theta(|x|)$: it records output length alone, up to constants. This directly contradicts Theorem 4.4's claimed superpolynomial lower bound on $\gamma_{\mathbf P}(x_\varphi)$ under the paper's ordinary explicit formula encoding, where $|x_\varphi|=O(|\varphi|)$. The proof's inference is independently invalid: ruling out one fixed $M$ that works on the whole hard subfamily does not rule out the pointwise minimum choosing a different $M_\varphi$ for each output.

The same quantifier error breaks the reverse direction of its proposed $P=NP$ characterization. The hypothesis gives, separately for each $w$, some $x_w$, some near-shortest $d_w$, and some $M_w\in\mathbf P$ with $M_w(d_w)=x_w$. It does not give one fixed $M^*$ for all instances, nor does it provide a way to find $d_w$ from $w$. The proof nevertheless asserts that the pointwise bound supplies one fixed decompressor and searches only descriptions of the special form $\langle\varphi,\pi_{M^*}\rangle$. Neither restriction follows from the premise. The forward direction itself explicitly uses machines $M_{c'_w}$ whose descriptions grow with $|w|$, confirming that the definition permits instance-dependent decompressor code.

For SAT under a verifier that accepts ignored certificate padding, the right-hand condition of the proposed characterization can in fact be met unconditionally: for each satisfiable formula, pad a valid assignment to polynomial length and choose a suffix making the certificate Kolmogorov-rich by counting; the two-sided bound gives $\gamma_{\mathbf P}=\Theta(|x_w|)=\mathrm{poly}(|w|)$. For unsatisfiable formulas, a polynomial-length fixed-form certificate can also be printed by its own machine. Thus the advertised biconditional, if correct, would itself imply $P=NP$. This is not a proof of $P=NP$: the reverse proof does not yield a uniform SAT algorithm, because it has not paid for or fixed the decompressor or made its description recoverable. The preprint's forward proof allows padding and decompressors whose descriptions grow with $|w|$, confirming that its quantifiers are instancewise.

The padding claim has a direct counting proof. If a valid witness has length at most $q(n)$, let the verifier ignore a suffix and pad the total witness to $3q(n)$ bits. For the fixed witness prefix, there are at least $2^{2q(n)}$ suffix choices, while fewer than $2^{q(n)}$ strings in total have Kolmogorov complexity below $q(n)$. Thus one padded witness has $K\geq q(n)=\Omega(n)$, and its total length remains polynomial. The choice is existential and need not be computable; that is precisely why it does not provide a search algorithm.

**Uniformity ladder.** Keep three logically different claims separate: (1) *objectwise expansion*, $\forall x\,\exists(M_x,d_x)$ with low cost, which the free-index minimum makes trivial; (2) *one decoder*, $\exists M\,\forall x\,\exists d_x$, which still leaves the descriptions existential and may require exponential search; and (3) *uniform representation*, where a fixed polynomial-time selector computes the relevant $d_x$ (or a fixed canonical encoding supplies it). Only the third level can directly turn short-description expansion into an ordinary algorithm. Fixing $M$ alone is insufficient.

**Reusable rule.** A measure intended to distinguish uniform search must either fix one decompressor across the family or penalize its description strongly enough to rule out per-instance hardcoding; merely bounding its code by a polynomial is insufficient. It must also state whether near-shortest descriptions are uniformly obtainable from instances. An existential per-object minimum over a class of algorithms is nonuniform advice in disguise. Detailed audit: [Idea 135](ideas.md#idea-135---uncharged-per-instance-decompressors-erase-the-search-cost) and [audit Section 97](P_VS_NP_PROJECT_AUDIT_2026-08-24.md). Source: [Buono, *Witness Complexity of Short Descriptions*, arXiv:2606.31370v1](https://arxiv.org/abs/2606.31370).

### 2.19 A computable map cannot manufacture Kolmogorov-rich outputs from every input

The same preprint's Conjecture 4.18 asks for a polynomial-time map $f_L$ such that $K(f_L(w))=\Omega(|w|)$ uniformly for every $w\in L$. This is incompatible with Kolmogorov complexity monotonicity on any language with a simple infinite sequence of yes-instances.

For every fixed computable $f$, a fixed wrapper runs a shortest program for $w$ and then computes $f(w)$, so

$$
K(f(w))\leq K(w)+O_f(1).
$$

Take the simple satisfiable SAT family $\varphi_m=\bigwedge_{i=1}^{m}(x_i\lor\neg x_i)$. Its explicit encoding length $n_m$ grows at least linearly and at most polynomially with $m$, while a fixed program given $m$ prints it, giving $K(\varphi_m)=O(\log m)=O(\log n_m)$. Any fixed polynomial-time $f_{SAT}$ therefore has $K(f_{SAT}(\varphi_m))=O(\log n_m)$, contradicting the conjectured $\Omega(n_m)$ lower bound. So Conjecture 4.18 is false as stated for SAT, independently of $P$ versus $NP$.

This does not contradict the earlier pointwise counting argument: for each input there may exist a high-complexity padded witness, but selecting one such pad uniformly would make it a computable image of the input and hence keep its Kolmogorov complexity at most $K(w)+O(1)$. The forward implication under $P=NP$ can choose pads noncomputably because it asserts only pointwise existence. The proposed uniform strengthening cannot hold over low-complexity inputs.

**Proof-design lesson.** An absolute $K$-richness condition on an output of a fixed computable map is incompatible with simple inputs. To retain a meaningful uniform target, restrict to an explicitly defined high-$K$ instance family and prove that a hard NP search problem remains on that family, or remove the absolute incompressibility requirement and formulate the needed uniform witness property directly. Conditional Kolmogorov complexity does not repair this particular issue: for fixed computable $f$, $K(f(w)\mid w)=O(1)$. Detailed proof: [Idea 136](ideas.md#idea-136---kolmogorov-complexity-cannot-rise-under-a-uniform-map) and [audit Section 98](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

### 2.20 Random padding turns a high-$K$ promise solver into a BPP solver

There is still a precise randomized/nonuniform consequence of high-$K$ padding. Define $SAT_{pad}=\{\langle\varphi,r\rangle:\varphi\in SAT\}$ with a standard efficiently parsed pair encoding of length $|\varphi|+|r|+O(\log(|\varphi|+|r|))$. Let $0<\delta<1$ be fixed. Suppose a deterministic polynomial-time machine $A$ correctly decides $SAT_{pad}$ on every well-formed $z$ satisfying $K(z)\geq\delta|z|$; its answers outside that promise may be arbitrary.

Fix any $\beta$ with $\delta<\beta<1$. Among uniform $N$-bit strings, counting shows

$$
\Pr_{r\leftarrow\{0,1\}^{N}}[K(r)<\beta N]\leq 2^{-(1-\beta)N+O(1)}.
$$

The pair encoding has a fixed computable projection to $r$, so $K(\langle\varphi,r\rangle)\geq K(r)-O(1)$. Pad to $N=C|\varphi|$ bits for a sufficiently large constant $C$. Since $\beta>\delta$, choose $C$ so that $\beta N-O(1)\geq\delta(|\varphi|+N+O(\log N))$ for all sufficiently large inputs. A randomized SAT algorithm can now sample $r$, run $A(\langle\varphi,r\rangle)$, and be wrong only when $r$ is atypically compressible. Its error is exponentially small, so $SAT\in BPP$.

The same proof works after a polynomial-time many-one reduction from any $L\in NP$, padding in proportion to the reduction output length; therefore such an $A$ implies $NP\subseteq BPP$. Alternatively, fix for each input length one incompressible pad $r_n$ guaranteed by counting and give it as advice. The resulting deterministic family has polynomial advice and yields $NP\subseteq P/poly$.

This does not imply $P=NP$: the consequences are randomized or nonuniform. It does give a sharper barrier for any proposed high-$K$-slice route. Deterministic uniform generation of rich outputs is impossible on simple inputs (Section 2.19), while random or advice padding can reach the high-$K$ promise only by moving the implication to BPP or P/poly. See [Idea 137](ideas.md#idea-137---random-padding-links-high-k-slices-to-bpp-and-p-poly) and [audit Section 99](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

### 2.21 The access channel is part of the randomness claim

The phrase ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œuse a high-K stringÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â hides three different computational interfaces. Keep them separate:

1. **Promise input:** a deterministic machine must decide a target language correctly when its input is high-K, but receives no oracle telling it whether an input is high-K. For padded SAT, random padding turns such a solver into a BPP SAT algorithm, while fixing one high-K pad per length gives a P/poly algorithm (Section 2.20).
2. **Advice:** a string selected separately for each input length is supplied to a uniform machine. High-K advice can encode a useful length-indexed choice, but does not answer arbitrary questions about whether other strings are high-K.
3. **Membership oracle:** the machine may query whether an arbitrary string belongs to a specified high-complexity set. This oracle exposes a semantic test that the other two interfaces do not provide.

This distinction is consequential in the literature. Allender et al. show that resource-bounded random-string sets have substantial oracle power: for example, $EXP=NP^{R_{Kt}}$ and $PSPACE=ZPP^{R_{Ks}}\subseteq P^{R_K}$ for their stated measures and reductions ([TR02-028](https://eccc.weizmann.ac.il/eccc-reports/2002/TR02-028/index.html)). Those theorems do not give a solver for a high-K promise slice. In 2026, Milovanov constructed a universal plain decompressor $U$ for which the halting problem is not in $P^{R_{C_U}}$, where $R_{C_U}=\{x:C_U(x)\geq |x|\}$; the paper notes earlier work giving a different universal $U$ for which the halting problem is in that oracle class ([arXiv:2605.16261](https://arxiv.org/abs/2605.16261)). Thus exact-threshold plain-K oracle power can depend sharply on the decompressor, even though universal plain complexities differ by only an additive constant. A threshold with no slack is sensitive to that constant.

There is a useful derived chain for the promise-input interface. If $A\in P$ solves padded SAT on every $K(z)\geq\delta|z|$ instance, Section 2.20 gives $NP\subseteq BPP$. Hu, Lu, and Oliveira prove for their nondeterministic time-bounded Kolmogorov estimation problem that $MINnKT\in BPP$ iff $NP\subseteq BPP$ ([TR25-203](https://eccc.weizmann.ac.il/report/2025/203/)). Hence such an $A$ would also imply $MINnKT\in BPP$. This is only a composition of two implications; the meta-complexity theorem is not a Karp reduction from the promise slice. Likewise, $NP\subseteq BPP$ lets one invert any polynomial-time candidate one-way function by applying SAT decision to the prefix-extension formulas for a preimage and self-reducing bit by bit. So existence of one-way functions would conditionally rule out this high-K promise solver. Neither conditional consequence is an unconditional lower bound.

**Access-triple rule.** Every proposal based on ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œrandom,ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œincompressible,ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â or ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œhigh complexityÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â objects must specify $(\mathcal K,\mathsf{access},\mu)$: the complexity measure $\mathcal K$, the access mode (promise input, advice, or membership oracle), and the threshold margin $\mu$. Prove robustness to the additive invariance constants of the chosen universal machine whenever the argument claims machine-independent meaning. Counting establishes abundance; it supplies neither an oracle nor a uniform selector.

There is also a direct obstruction to derandomizing the padding by a polynomial-size list that stays inside the promise. Let $\varphi_n$ be a simple satisfiable formula of length $\Theta(n)$ printed by a fixed program given $n$ in binary, so $K(\varphi_n)=O(\log n)$. If a fixed computable procedure maps $(n,i)$ to any candidate padded instance $z_{n,i}=\langle\varphi_n,r_{n,i}\rangle$, and the list has polynomial size, then $i$ has $O(\log n)$ bits and $K(z_{n,i})\leq K(n,i)+O(1)=O(\log n)$. Since $|z_{n,i}|\geq\Theta(n)$, every listed candidate eventually fails any promise $K(z)\geq\delta|z|$ for fixed $\delta>0$. Thus no polynomial-size list generated uniformly from these simple SAT inputs can furnish a valid promised call to $A$ at every index. This rules out the direct ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œenumerate a small sample set of valid padsÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â upgrade from BPP to P; it does not rule out other derandomization methods that establish correctness outside the promise or add a new structural hypothesis.

Machine invariance needs the same margin discipline. An additive $c$-bit change between universal machines can move objects within $c$ bits of a threshold $K(z)=\delta|z|$ across the boundary. A reduction whose outputs satisfy the stronger bound $K(z)\geq(\delta+\epsilon)|z|$ remains inside the $\delta$ promise under such a change once $|z|\geq c/\epsilon$. The bare language defined by $K(z)\geq\delta|z|$ is not thereby machine-independent.

### 2.22 Fixed-clock incompressibility is a direct coNP target

Use $K^t(x)$ for the length of the shortest program printing $x$ within a fixed time bound $t(|x|)$; keep this distinct from Levin's $Kt$, which charges description length plus logarithm of runtime. For an integer $q\ge2$, fix the polynomial $t(n)=n^q$ and define

$$
R_t=\{x:K^t(x)\geq |x|-1\}.
$$

The complement is in NP: a certificate is a program of length at most $|x|-2$, and the verifier simulates the fixed $t(|x|)$-step clock. Counting guarantees that $R_t$ has at least one member at every length. Thus $R_t\notin P$ would imply $P\ne NP$. This is an exact, natural separation target, rather than a route that first pads arbitrary SAT instances.

Hirahara proves that $R_t$ is P-immune whenever $t(n)=n^{\omega(1)}$ ([ECCC TR20-050](https://eccc.weizmann.ac.il/report/2020/050/download/)). The proof explains why this does not yet settle the polynomial-clock case. If an infinite P subset $S\subseteq R_t$ had decider $M$ running in $n^a$, choose at infinitely many lengths a member $r=a_0a_1$ with prefix $|a_0|=n-m$ and suffix length $m=C\log n$. Exhaustively search suffixes $u$ until $M(a_0u)=1$. The output lies in $S$, but it has a description of length $n-m+O(\log n)<n-1$ and is printed in time $2^m n^{a+O(1)}=n^{a+C+O(1)}$. A super-polynomial clock eventually contains this runtime, contradiction. For a fixed clock $t(n)=n^q$, the argument only contradicts a decider whose exponent satisfies $a+C+O(1)<q$. An arbitrary P decider may have exponent larger than the fixed $q$.

This yields a quantitative partial result: for a constant $C_0$ depending on the fixed encoding and universal machine, any polynomial-time decider for $R_{n^q}$ must have exponent at least $q-C_0$. It does not show that $R_{n^q}\notin P$; an exponent proportional to $q$ is consistent with this lower bound. Under $P=NP$, the ordinary Cook-Levin reduction for the bounded simulation can also produce a P decider with exponent proportional to $q$ (the tableau length grows as $n^q$ and the SAT algorithm contributes its own fixed exponent), so the current bounds fit together without contradiction.

The $q-C_0$ estimate is deliberately coarse; coding details sharpen it (Idea 141). For plain K, a fixed-size suffix can be searched because the program can infer $n$ from its own input length, giving time $O(n^a\log n)$ and ruling out decider degree $a<q$ under an efficient universal simulator. For an arbitrary infinite P subset and prefix-free K, a self-delimiting code for $n$ costs $\log n+O(\log\log n)$ bits; the suffix search then costs $n^{a+1}\operatorname{polylog}n$, ruling out $a\leq q-2$ and giving the generic immunity-proof floor $a\geq q-1$. Kraft's inequality explains why that all-length code cannot have constant overhead.

For the **full target** $R_{n^q}$, the prefix-free bound improves. Counting gives at least one accepted string at every length, so take only lengths $n=2^k$. A prefix-free program can encode $k$ in $h(k)=\log k+O(\log\log k)=O(\log\log n)$ bits, hard-code the prefix of a member of $R_{n^q}$, and search a suffix of length $h(k)+C$. There are only $2^{h(k)+C}=O(\log n\operatorname{polyloglog}n)$ suffixes. A decider of degree $a<q$ would therefore produce, within $O(n+n^a\operatorname{polylog}n)=o(n^q)$ time for $q\ge2$, an accepted output described in at most $n-2$ bits, contradiction. So any P decider for the full $R_{n^q}$ must have degree at least $q$ under plain or prefix-free K. This sparse-length refinement does not establish P-immunity: an arbitrary infinite P subset need not occupy the computable lengths $2^k$ (Idea 144). It also leaves deciders of degree $q$ or higher untouched.

The same paper connects non-trivial SAT algorithms with immunity for Levin-$Kt$ random strings: a Williams-style satisfiability speedup yields immunity against a uniform circuit class. This is a real bridge between SAT algorithms and algorithmic randomness, but the Levin-$Kt$ random set is not known to lie in coNP; its immunity alone does not separate P from NP. The central target remains to obtain a P-immunity or any non-P lower bound for a fixed polynomial-clock $R_t$, where NP verification still applies.

**Proof debt.** Either prove $R_{n^q}\notin P$ for one fixed $q$, or give a different coNP language whose lower bound survives arbitrary P exponents. The super-polynomial-clock theorem cannot be transferred by choosing $q$ after seeing the decider: the language changes with $q$, and no uniform bound on the decider exponent as a function of $q$ is known. This is the clock/uniformity debt in a concrete algorithmic-information setting.

### 2.23 Random-string lists have a construction clock and a selection clock

Korten and Santhanam construct short-seed pseudorandom generators under explicit hardness assumptions and use their output lists to obtain strings with high time-bounded Kolmogorov complexity ([CCC 2025](https://doi.org/10.4230/LIPIcs.CCC.2025.35), especially Theorems 16 and 23). The list has a member that is hard to compress because incompressibility is a dense coNP property; concatenating all candidates avoids having to identify the good member. Their construction is conditional, and its polynomial running time is not shown to be below the Kolmogorov clock being tested.

Separate three costs: time to generate the list, number of candidates, and time to recognize a hard member. This yields a precise conditional test. Fix $R_q=\{x:K^{|x|^q}(x)\geq |x|-1\}$. Suppose a uniform polynomial-time algorithm enumerates a list $L_n$ of at most $n^b$ strings of length $n$, and $L_n$ intersects $R_q$ for infinitely many $n$. If a P decider for $R_q$ ran in time $n^a$, scanning the list would find an accepted member in time $n^{\max(g,a+b)+O(1)}$, where $n^g$ bounds list generation. If no member is accepted, output $0^n$ so the selector is total. On every length where the list hits, its output is a member of $R_q$ and has a description of length $O(\log n)$ within that time. Therefore, if $q>\max(g,a+b)+O(1)$, this contradicts membership in $R_q$. This is a valid degree lower bound from a hitting list, but it proves $R_q\notin P$ only if the clock exponent dominates the list and selector exponents for every possible P decider. For one fixed $q$, the decider's exponent is not known in advance.

There is a matching construction floor. If a list of polynomial size is enumerated in time $T'(n)$, each candidate can be described by the fixed enumerator, $n$, and its $O(\log n)$-bit index. If $T'(n)\log T'(n)=o(T(n))$, every candidate has $K^{T(n)}=O(\log n)$, so the list cannot hit $\{x:K^{T(n)}(x)\geq n-1\}$. Thus a generated hitting list must take essentially $T/\log T$ time just to produce its promised hard member. Under $P=NP$, coNP membership would let us select the good candidate, but the recognition procedure also has polynomial overhead in the clock. The construction and recognition costs together do not give a sub-$T$ description.

The same paper identifies a method barrier: with an NP oracle, constructing near-maximally incompressible strings is equivalent to constructing exponentially hard truth tables (Theorem 46); its Theorem 48 rules out a specified relativizing black-box reduction between range-avoidance exponents separated by more than one. This is not an impossibility theorem for all constructions. It does say that a direct relativizing hardness-to-random-string conversion cannot be assumed to remove the missing clock advantage; a successful route needs a non-black-box or otherwise nonrelativizing step.

**Learning / next move.** Close the generic short-list route as a way to select a $K^T$-random string in less than its own clock. Keep the decider-dependent suffix search from Section 2.22 only as a degree lower bound. A new proof must either control the exponent of a single uniform family of $R_q$ deciders, exploit structure of the particular decider to find an accepted extension faster than exhaustive suffix search, or replace explicit high-$K$ construction with a direct lower-bound invariant. Track $(T_{\rm list},|L|,T_{\rm test},T_{\rm select},T_K)$ separately. This also connects to the time-bounded chain-rule analysis already recorded below: information-additivity claims can encode a gap-MCSP-in-P premise together with a circuit lower bound, rather than supplying either one for free.

### 2.24 The suffix search is optimal when the decider is a black box

Fix a prefix $u$ and suffix length $m$, and expose the P decider only through the Boolean oracle $f(v)=M(uv)$, promised to accept at least one suffix. In this query model, finding an accepted suffix needs $\Omega(2^m)$ queries: take the family of oracles with exactly one accepting suffix at an unknown location. After fewer than $2^m-1$ all-negative queries, at least two locations remain possible, so no deterministic output is guaranteed correct. By Yao's argument, bounded-error randomized search also needs $\Omega(2^m)$ queries against a uniformly located singleton.

For the prefix-free compression proof, $m=\log n+O(\log\log n)$, so this black-box barrier costs $n\operatorname{polylog}(n)$ calls and accounts for the extra polynomial factor in the clock. For plain K the generic proof can take fixed $m$, so it pays only a constant number of calls. The lower bound is deliberately limited to query access: an algorithm that inspects the code of $M$ may exploit special structure of this exact coNP decider. Therefore the remaining proof opportunity is non-black-boxÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Âprove that the semantic form of a correct decider for $R_q$ forces a faster accepted-suffix search, or derive a different lower-bound invariant. The query theorem alone does not establish that such a speedup exists.

### 2.25 Self-reference has a formula-size budget

Test the liar-style proposal to build a SAT formula $x$ with $SAT(x)=1-A(x)$ for a proposed SAT algorithm $A$. Given an ordinary input $z$ of length $n$, Cook-Levin can encode the computation ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ$A(z)$ rejectsÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â as a formula $F_A(z)$. If $A$ runs for $T(n)=n^d$ steps, the direct rectangular space-time tableau has on the order of $T(n)^2$ local records, and writing the indexed CNF explicitly takes $O(T(n)^2\log T(n))=n^{2d}\operatorname{polylog}(n)$ bits.

The intended self-reference would require the input to $A$ to be the final formula whose tableau is being encoded. The direct size recurrence therefore grows from $n$ to about $n^{2d}\operatorname{polylog}(n)$, then from that length to about $n^{4d^2}\operatorname{polylog}(n)$. For every fixed $d\ge1$, this route does not close at a finite large length. Padding cannot fix the recurrence: padding raises the length at which $A$ runs and makes its next tableau larger still. Kleene's recursion theorem gives self-reference for program behavior, but does not promise a same-size fixed point in a representation whose explicit computation tableau is superlinear.

Running $A$ inside the constructor avoids the tableau-size expansion but creates a separate fixed-point failure. Define $F_A(z)=\bot$ if $A(z)$ accepts and $F_A(z)=\top$ if $A(z)$ rejects, for fixed contradiction and tautology formulas. This is polynomial-time computable and satisfies $SAT(F_A(z))=1-A(z)$. If $A$ is correct, $F_A$ swaps $\top$ and $\bot$, so it has a 2-cycle and no fixed point. A SAT contradiction from self-reference would require an admissible $z=F_A(z)$; the recursion theorem does not guarantee a raw formula fixed point for this anti-answer map.

These are two distinct failures, not a theorem against all self-reference. A succinct circuit for the tableau changes the language to succinct SAT, which an ordinary SAT algorithm need not decide; the constant-size map lacks a fixed point. A successful route needs both a size-controlled ordinary-SAT representation and a reason a relevant self-consistent instance exists. Ko's 1991 work already shows oracle dependence for variations of time-bounded program-size problems, which is a useful warning that nearby classification questions can require nonrelativizing methods; it does not establish the same oracle theorem for our exact $R_{n^q}$ language ([Ko, SIAM J. Comput. 20(5)](https://doi.org/10.1137/0220059)).

**Learning / next move.** For every self-reference proposal, prove that the desired fixed point exists and write the object-size map $n\mapsto m(n)$ before invoking a fixed-point theorem. Require an explicit inequality showing the final object can contain the computation or witness interface used to define it. Search for a smaller semantic interface than the full tableau; state its ordinary SAT encoding length and verifier time, and do not switch to succinct SAT without a reduction back to ordinary SAT. This extends the exponent audit in Section 2.1 with the two failures isolated in [Idea 143](ideas.md#idea-143---a-liar-formula-needs-a-size-controlled-fixed-point).

## 3. The proof-debt ledger

Every proposed approach should be scored against these obligations. The entries are a checklist, not a numerical complexity measure.

| Obligation | Question a proof must answer | Common unpaid bill in this project |
|---|---|---|
| **Target** | What exact language, promise, or lower bound would imply $P\ne NP$? | A construction proves a nearby geometric fact without reaching SAT, Gap-MCSP, or a known transfer theorem. |
| **Representation** | How many bits describe the object, and what is the cost of evaluating it? | A succinct code hides an exponentially long truth table, algebra element, or computation. |
| **Uniformity** | Who constructs the object, and in what time and advice model? | Counting proves that a hard object exists, but does not find it or give a uniform family. |
| **Semantic coverage** | Which candidates, inputs, or witnesses does the invariant cover? | A bound works for selected anchors, one selector, or a sampled set, while the theorem quantifies over all of them. |
| **Witness representation** | Is the algorithm required to recover the sampled witness, or may it choose any satisfying witness? | Entropy in a random certificate representative is charged as though it were necessary to recover the invariant message; gauge fixing can remove the representative without changing the quotient. |
| **Promise preservation** | Does every transformed, fixed-advice, or simulated machine still satisfy the semantic promise on every required input? | A correct advice sequence makes a machine unambiguous or bounded-error, but the proof applies a class theorem to variants using incorrect advice. |
| **Global integration** | How does one small procedure combine information from the whole instance? | Local mismatch tests or per-anchor certificates do not explain the cost of combining them. |
| **Sharing** | Can one circuit or proof reuse work across many obligations? | A count charges separately for many witnesses although a shared circuit, relay, or endpoint pair covers them together. |
| **Certification** | What efficiently checkable object proves the universal negative claim? | A valid exclusion set exists, but checking that no low circuit fits it is itself hard. |
| **Transfer** | Which theorem converts the lower bound into a standard complexity separation? | The estimate is only linear, concerns formulas instead of circuits, or falls below the magnification threshold. |
| **Barrier test** | Which relativizing, natural, or algebraizing version of the argument is ruled out? | The proof manipulates black-box local behavior and still works with arbitrary oracle gates. |

The dominant present diagnosis is **global integration debt**: most candidate methods reach a useful object, but do not show that a small uniform computation cannot combine the object's local pieces. A closely related debt is **universal certification**: a short candidate certificate is not useful if verifying its claimed coverage expresses a hard synthesis problem.

## 4. Two proof engines in this project

### 4.1 Gap-MCSP magnification through fusion covers

One established conditional route is:

1. Encode a promise version of Gap-MCSP as a family of semi-filters.
2. Prove a slightly superlinear lower bound on the required fusion-cover number at the theorem's parameters.
3. Apply the hardness-magnification theorem to obtain $\mathrm{NP}\not\subseteq\mathrm{P/poly}$, hence $P\ne NP$.

The transfer is real and useful. The missing premise is the superlinear lower bound. The project's exact analyses show why many natural constructions fail: local witness families can be covered by shared pairs, cyclic relays, prefix-count recurrences, affine interpolation sets, or other compact closure systems. The current general proof-DAG argument gives a near-linear lower bound for the broad semi-filter formulation, below the required superlinear threshold. The target must exploit a promise-specific invariant that survives arbitrary sharing and does not relativize away.

Relevant evidence is collected in audit Sections 18 and 21-25 and in [ideas.md](ideas.md), including the exact cyclic relay constructions and the Reed-Muller/affine-span counterexamples. These are route-specific obstructions, not evidence that the transfer theorem is unusable.

### 4.2 High truth tables, exclusion sets, and partial synthesis

For a high table $f$, define

$$
\tau_s(f)=\min\{|Q|:\forall C\in\mathcal C_{<s}\;\exists x\in Q\;C(x)\ne f(x)\}.
$$

This is the smallest image of any counterexample selector. Partial-function realization gives the theorem-level floor $\tau_s(f)=\Omega(s\log s)$ when $s\gg n$, and counting shows this order is achieved for some high tables. The bound is about certificate existence and size; it gives no efficient construction or verifier.

For arbitrary partial tables, validating that $Q$ excludes every low circuit is coNP-hard under randomized reductions, by the partial-MCSP result. The reduction is important as a diagnostic: a generic certificate checker for arbitrary $(f|_Q,Q)$ cannot be assumed to be easy. A successful construction must add structure that supports a different proof of non-realizability.

The two engines share one bottleneck: **a global condition over all candidate computations has to be represented and verified without paying for the full truth table or re-solving the original problem.** The common diagnosis is a synthesis from project evidence, not a formal equivalence between these two routes.

## 5. The trace-boundary model: a new experimental lens

For a low class $\mathcal C_{<s}$ and rows $Q$, define

$$
T_s(Q)=\{C|_Q:C\in\mathcal C_{<s}\},\qquad
H_s(Q)=\{0,1\}^{Q}\setminus T_s(Q).
$$

$T_s(Q)$ is the set of restrictions low circuits can realize; $H_s(Q)$ is the set of missing labelings, or **trace holes**. A partial labeling $p$ is critical on $Q$ exactly when

$$
p\in H_s(Q)\quad\text{and}\quad p\oplus e_x\in T_s(Q)\quad\text{for every }x\in Q.
$$

This translates a minimum selector into a local boundary statement. But it does not prove that $Q$ is a globally minimum selector for a total extension: another set of rows may exclude every low function with fewer points. Always check both the punctured boundary and all alternative selectors.

### Exact four-input finding

In the bounded-fan-in De Morgan formula model with at most four AND/OR gates, all 3,302 low functions were enumerated. Across all 12,870 eight-row sets, the smallest hole-set size is eight and occurs on 74 sets. Ten of those hole sets are affine cosets of a binary $[8,3,4]$ linear code with weight enumerator $1+6z^4+z^8$. The code has not been assigned a standard family name.

For the even-parity input set $Q=\{0,3,5,6,9,10,12,15\}$, one missing restriction is $p=0x81$, and

$$
H_5(Q)=\{0x18,0x24,0x42,0x7e,0x81,0xbd,0xdb,0xe7\}.
$$

After translating by $p$, this hole set is the span of $0x99,0xa5,0xc3$. All its nonzero differences have weight four or eight, so none of $p$'s immediate neighbors is another hole. Every one-row deletion has a low formula witness. The total table $f=0x8181$ extends $p$; it is the five-gate function

$$
f(x)=(\neg x_0\land\neg x_1\land\neg x_2)\lor(x_0\land x_1\land x_2),
$$

independent of $x_3$. Exhaustive enumeration gives formula complexity five and $\tau_5(f)=8$. The separate shared-circuit enumerator finds the same $n=4$ function classes as the formula enumerator through four gates, so the low-side exclusion survives arbitrary fanout and sharing in this finite model.

Each of the eight missing partial labelings has 16 exact five-gate total completions in this row set. For $p=0x81$, those 16 completions give 16 different labelings on the eight unselected inputs; that extension set is not an affine subspace under the direct XOR check. This is another finite structural fact, not evidence of an asymptotic code construction.

### Failed five-input lift

The exact five-input class of formulas with at most five gates has 147,136 functions. On the 16 even-parity rows, it realizes 28,584 patterns and leaves 36,952 holes, but no hole has all one-bit neighbors in the trace. Four one-odd-row variants also have zero critical holes. Ten seeded row sets at each size 12 through 17, an additional 24 seeded 17-row sets, and a greedy row choice maximizing distinct traces all found zero critical holes. The greedy sample reached 22,848 trace patterns on 17 rows.

This rejects the naive parity-row scaling conjecture on the tested sets. It does not prove that no five-input sample works: neither the random sample nor the greedy objective exhausts the row-set space. The experiment and full reproducible parameters are in [experiment_five_input_trace_criticality.py](experiment_five_input_trace_criticality.py).

### What this lens contributes to proof search

The trace language separates four quantities that had been blurred in earlier attempts:

1. the number of low functions;
2. the number of distinct low traces on $Q$;
3. whether a target labeling is a hole and whether its one-bit neighbors are present;
4. whether any smaller row set works for the completed total function.

Code distance helps with item 3 after the holes have been established. It does not prove that a target is a hole, establish items 1-2 at scale, or settle item 4. A serious extension needs an invariant of low-circuit traces that proves all of these claims uniformly.

### A scale-matched polarity-and-pair theorem for formulas

The five-input experiment above held the competitor cutoff fixed at five gates. That is useful for testing the naive lift of the four-input example, but it is not matched to the target's growing formula size. There is a separate family with an exact all-$m$ proof.

Use the bounded-fan-in De Morgan **formula** model: leaves are signed input literals, internal gates are binary AND/OR, and subcomputations cannot be shared. On inputs $(a,y_1,\ldots,y_m)$, let

$$
F_m(a,y)=1\quad\Longleftrightarrow\quad y=0^m\text{ or }y=1^m,\qquad m\ge3.
$$

Its formula size is exactly $2m-1$. An upper bound is the disjunction of the two endpoint minterms. For the lower bound, changing any $y_i$ from 0 to 1 at the zero endpoint makes the output fall, so a formula must contain a negative occurrence of $y_i$; changing that coordinate from 0 to 1 at the opposite endpoint makes the output rise, so it must also contain a positive occurrence. Thus there are at least $2m$ literal leaves, and a binary formula with $L$ leaves has $L-1$ gates. On the sample, the falling edge is $(1,0^m)\to(1,e_i)$ and the rising edge is $(0,1^m-e_i)\to(0,1^m)$, so the same occurrence argument excludes every low formula.

Now take the sample

$$
Q_m=\{(1,y):|y|\le1\}\;\cup\;\{(0,y):|y|\ge m-1\}.
$$

It has $2m+2$ rows. For a vector in the two endpoint neighborhoods, low witnesses are: $\bigwedge_i y_i$ at $y=0^m$; $\bigwedge_i\neg y_i$ at $y=1^m$; $(\bigwedge_{j\ne i}\neg y_j)\lor(\bigwedge_j y_j)$ at $y=e_i$; and $(\bigwedge_j\neg y_j)\lor(\bigwedge_{j\ne i}y_j)$ at $y=1^m-e_i$. Each differs from $F_m$ on exactly the two-row fiber $(0,y),(1,y)$ and has at most $2m-2$ gates. These $2m+2$ disagreement pairs are disjoint. Any selector image against all formulas below size $2m-1$ must hit every pair, hence needs at least $2m+2$ rows; $Q_m$ hits one row in each pair and excludes the entire low formula class. Therefore, with this precise threshold convention,

$$
\tau^{\rm formula}_{2m-1}(F_m)=2m+2.
$$

**Transfer-scale audit:** this family has $n=m+1$ input bits, truth-table length $N=2^{m+1}$, target gate count $s=2m-1=\Theta(n)=\Theta(\log N)$, and selector size $q=2m+2=\Theta(\log N)$. Hardness-magnification routes need lower bounds at a much larger circuit scale such as $s=N^\beta$ for fixed $\beta>0$. So even an all-$m$ circuit theorem for this family would be a local mechanism result; it could not itself meet those transfer parameters or separate P from NP.

The proof and a finite exact-class verifier are in [experiment_antipodal_formula_selector.py](experiment_antipodal_formula_selector.py). The script checks $m=3,4$; the symbolic argument covers all $m\ge3$. For $m=4$, it confirms a five-input, six-gate competitor cutoff, target table `0xC0000003`, and a ten-row selector. This complements the preceding five-input, five-gate failure: criticality returns at the scale-matched cutoff, so the fixed-cutoff failure was not evidence against every larger-input analogue.

**Updated interpretation:** the critical sample here is generated by a *polarity budget* (both signs of every relevant variable are forced) plus a *disagreement packing* (disjoint two-row errors force the selector size). This is a clean mechanism behind a punctured trace boundary; it does not need the earlier code-coset observation. It is a formula result with linear size and a hand-built function. Sharing is the missing step: a circuit can reuse intermediate computations, so the leaf count no longer gives a gate lower bound. Even a circuit analogue with a linear bound would remain far below what is needed for P versus NP. The next question is whether any invariant charges shared gates for satisfying many opposite-polarity obligations at once, and whether that invariant can be made superlinear and transferred to general circuits.

### Shared-circuit stress test: exact at three finite sizes

I encoded topologically ordered circuits with arbitrary fanout, AND/OR gates of fan-in two, NOT gates of fan-in one, and free constants and signed input literals. The solver chooses every gate and the output wire; unused slots allow all smaller circuits. [experiment_circuit_selector_antipodal.py](experiment_circuit_selector_antipodal.py) searches for a circuit matching $F_m|_{Q_m}$ with at most $2m-2$ gates, then checks a $2m-1$-gate upper bound.

For $m=3$ and $m=4$, Z3 returns UNSAT at 4 and 6 gates, respectively, and SAT at 5 and 7 gates; the SAT circuits are independently evaluated on every sample row. The $m=5$ eight-gate case timed out in Z3, but an independent CNF encoding returns UNSAT with both CaDiCaL and Glucose. That CNF encoding reproduces the $m=3,4$ bounds and verifies their SAT witnesses. Since the disjoint formula witnesses are circuits and the endpoint-minterm formulas give upper bounds, the solver results establish exact circuit selector sizes 8, 10, and 12 at $m=3,4,5$, conditional on trusting the UNSAT runs. No proof traces have been independently checked. This suggests, but does not prove, the all-$m$ conjecture $\mathrm{CC}_{\rm circ}(F_m)=2m-1$.

This is a real model extension beyond formulas, but it remains a linear lower bound for a tiny explicit family. It has no P-vs-NP consequence. A proof must explain why a circuit cannot reuse intermediate signals across the two antipodal acceptance regions. The $m=5$ Z3 attempts returned `unknown`, but the CNF encoding resolved the partial-sample question independently. The $m=6$ ten-gate query was interrupted without a result after the scale audit showed that further dimension increases would not address the proof goal. Even an all-$m$ theorem here would be a mechanism lemma, not a separation.

## 6. Why the previous routes repeatedly stalled

| Route | What the work established | Why it did not yield a separation | Reusable lesson |
|---|---|---|---|
| Self-reference, diagonalization, and ZFC | Several precise fixed-point and proof-size formulations; code-length and verifier costs were audited. | The diagonal statement moves the description or time bound; independence claims did not supply a theorem separating standard classes. | Write the input length, proof length, and quantifiers into the same equation before using self-reference. |
| Geometry, topology, and filters | Many exact finite closure, cover, and counterexample computations; a conditional magnification route is formalized. | Open/closed structure and many witnesses often collapse under unrestricted endpoints, relays, or shared pairs; available cover lower bounds stay too small. | Charge shared computation, not raw witness or anchor counts. |
| Heavy atoms, discrepancy, and measure arguments | Exact support-overlap bounds and tests of several distributions; some explicit constructions can be made algorithmic. | Sparse majority witnesses can be selected disjointly and covered cheaply; an $O(\log M)$ or linear cover does not meet the needed magnification scale. | Optimize against every endpoint and overlap pattern before proving an aggregate-load bound. |
| Algebra, Fourier, and feature maps | Exact linear-algebra formulations and finite checks; affine and Reed-Muller constructions expose failure cases. | Basis change does not remove Boolean-support hardness; coefficient extraction can be exponential; affine images often create small covers. | State the representation and extraction cost, and identify the step that survives algebrization. |
| Proof complexity, compression, and cryptography | Useful conditional connections and several certificate formulations. | Some assumptions already imply a complexity separation; a succinct verifier may restate SAT/partial-MCSP; current proof-size lower bounds do not transfer to general circuit size. | Prove the premise is weaker than the desired conclusion and the verifier is sound in the actual encoding. |
| Selector images and trace holes | An $\Omega(s\log s)$ selector-image floor, partial-MCSP hardness, a code-shaped four-input trace, and an exact all-$m$ formula selector family. | Generic verification is hard; fixed-cutoff parity samples fail; the all-$m$ formula mechanism is linear and sharing-sensitive. | Use the antipodal family to study sharing, but require a superlinear, uniformly certifiable invariant and an explicit transfer. |

These outcomes diagnose methods, not the mathematical possibility of a proof. Relativization, natural-proofs, and algebrization results restrict proof techniques; they do not imply independence from ZFC, impossibility, or $P=NP$.

### Public-input evidence must cover ordinary computation

A recent preprint claims $P\ne NP$ through a lower bound on polynomial-time prediction of a unique message encoded by satisfying witnesses. Its SAT-search upper bound under $P=NP$ is standard. The key unresolved bridge is on the lower-bound side: the paper gives an evidence calculus for a restricted primitive-read interface and assumes atom completeness, but it does not prove that every polynomial-time machine reading the full public SAT string has an evidence trace in that interface. See [ideas.md, Idea 11](ideas.md#idea-11--semantic-evidence-syntax-leakage-and-the-neutral-atom-trap), [Idea 122](ideas.md#idea-122--coupling-derivatives-are-not-computational-distinguishability), and audit Sections 28 and 84.

The exact coupling fact is: for phase laws $\mu_0,\mu_1$ and an observation $T$, the minimum over couplings of $\Pr[T(X_0)\ne T(X_1)]$ equals $\operatorname{TV}(T_*\mu_0,T_*\mu_1)$. A fixed coupling can have much larger disagreement than total variation, so a pairwise derivative under that coupling is not automatically predictive advantage. Moreover, if a rigid target bit is a function of the full public input $Y$, the two conditional input laws have disjoint supports and full-input total variation is $1$. Any meaningful lower bound must therefore be computational: bound the distinguishing advantage of every size-bounded circuit on the actual encoded $Y$, while proving that the evidence accounting faithfully represents all its input reads.

An exact parity example guards against local-to-global errors. For even $n$, $A=I+J$ over $\mathbb F_2$ is its own inverse, so $Y=AM$ efficiently reveals $M$ from all coordinates, while any set of at most $n-2$ coordinates leaves every individual $M_i$ uniform. Bounded-arity neutrality alone cannot establish hardness of global computation. The proof debt is to get a uniform computational-discrepancy theorem for a fixed SAT-witness sampler; proving that for a message recoverable from a satisfying witness would be a major average-case hardness result, not a consequence of relabeling public syntax as neutral.

The example has a polynomial-size SAT realization: Tseitin encode the $O(n^2)$ bounded-fan-in XOR gates for $AZ=Y$ into 3CNF. The encoded instance is satisfiable for every sampled $Y$, and every satisfying witness has the same message $Z=A^{-1}Y$. A standard parser and parity circuit recover this message from the public formula in polynomial time. A gauge lift $Z=X\oplus G$ can add many witness representatives without changing the easy public decoding. Thus local clause syntax, witness-message rigidity, and hidden gauge symmetry do not by themselves establish prediction hardness; that hardness must be proved for the full input representation.

The current time-bounded Kolmogorov literature reinforces this limit. Kabanets and Kolokolova characterize a sublinear-error chain rule for conditional $K^t$ by both an exponential-time circuit lower bound and a promise-gap $K^t$ problem in P; under cryptographic NP-hardness of that promise problem, the chain-rule question is equivalent to $P=NP$ ([ECCC TR25-089, Revision 1](https://eccc.weizmann.ac.il/report/2025/089/)). Thus an algorithmic-information reformulation can expose the missing hardness premise precisely, but it does not supply it.

## 7. Rules for generating and testing new ideas

Before building an experiment or proof sketch, write:

1. **Target theorem.** State the exact lower bound and the cited transfer to $P\ne NP$.
2. **Quantifiers.** Identify every universal circuit, input, anchor, selector, proof system, and randomized reduction.
3. **Model.** Specify formulas versus circuits, gate basis, fanout, uniformity, advice, time, and encoding length.
4. **Certificate.** State what a verifier receives and why soundness holds without evaluating the original hard predicate.
5. **Sharing adversary.** Attempt to combine all local witnesses in one small circuit, relay, proof DAG, or endpoint cover.
6. **Barrier check.** Ask whether the proof relativizes, is natural in the relevant sense, or algebrizes. Identify the nonrelativizing step if needed.
7. **Falsification.** Find the smallest counterexample or exact toy where the claimed invariant must hold. Distinguish failure of the mechanism from a theorem-level no-go.
8. **Status label.** Mark each result as theorem, conditional theorem, exact computation, heuristic, or open obligation.

Numerics are for selecting conjectures and finding counterexamples. The proof target is a symbolic invariant, a uniform construction, a verifier/refutation, and a parameter-matched transfer.

### Proof-first criterion: resource-bounded descriptions of SAT witnesses

Fix a universal machine $U$. Define

$$K_{\mathrm{SAT}}^t(\varphi)=\min\{|p|: U(p,\varphi)\text{ halts within }t(|\varphi|)\text{ steps and outputs a satisfying assignment of }\varphi\},$$

with value $\infty$ if no such program exists. Then

$$P=NP\quad\Longleftrightarrow\quad \exists c,d\ \forall\text{ satisfiable }\varphi,\ K_{\mathrm{SAT}}^{|\varphi|^d}(\varphi)\le c.$$

For the forward direction, a polynomial SAT decider plus the standard bit-by-bit self-reduction gives one polynomial-time witness-finding machine; its fixed code is a program of constant length for $U$. Conversely, if constants $c,d$ work, enumerate the finitely many programs of length at most $c$, simulate each for $|\varphi|^d$ steps, and check any output assignment directly. This decides SAT in polynomial time: every satisfiable input has a successful program, while an unsatisfiable input has none. Consequently, $P\ne NP$ is equivalent to saying that for every fixed $c,d$, some satisfiable formula has no satisfying assignment produced by any $c$-bit program within $|\varphi|^d$ steps.

This is an exact reformulation, not a lower bound. It sharpens the project's separation between witness existence and witness search: the required obstruction is resource-bounded and uniform over all short program descriptions. Plain conditional Kolmogorov complexity cannot supply it. The lexicographically first satisfying assignment is computable by exhaustive search, so it has a constant-length conditional description from $\varphi$, regardless of the search time. A valid incompressibility route must retain the time bound and prove a lower bound against every fixed polynomial exponent; entropy or counting over witness strings alone does not do that.

The logical next step is to seek a structural proof of this time-bounded obstruction for SAT, while writing out the cost of any self-reference that tries to build a formula defeating all short programs. If encoding their $n^d$-step computations makes the new formula longer, then their clock becomes the larger new input raised to $d$; the diagonal must close this size/exponent loop instead of assuming it away. Full statement, proof, caveats, and the related current-literature screen are in [ideas.md](ideas.md#idea-115--resource-bounded-witness-descriptions-characterize-the-search-gap).

## 8. Current research program

**Priority update (25 September 2026):** Track C is now the active track: work backward from both truth values, formalize the quantifiers, and try explicit proof constructions. The long-running finite SAT/CEGIS jobs on toy relay families were stopped without conclusions; no partial solver state is being counted as evidence. Do not restart dimension sweeps. Tracks A and B are dormant unless a proof-level invariant gives a concrete reason to return to them. Use computation only to falsify a precisely stated lemma or check a small witness.

### Track A (dormant): turn the polarity-and-pair formula theorem into a sharing-resistant statement

- Treat the fixed-cutoff five-input parity search as closed unless a new invariant suggests a different row family.
- The antipodal sample has solver-derived exact circuit selector sizes at $m=3,4,5$. The $m=6$ ten-gate query was interrupted and is inconclusive. Do not resume a dimension sweep unless a specific predicted invariant or proof-producing objective makes the result useful. Prioritize a symbolic account of sharing, or close this toy route with a precise obstruction.
- Identify a gate-charging invariant for the two antipodal 1-certificates that survives fanout. Compare any proposed bound with a circuit using shared subcomputations and with the dual-rail monotone simulation.
- For every partial target, prove it is absent, produce every deletion witness, then rule out all smaller row sets for a total extension.
- Treat partial-MCSP hardness as a warning against generic certificates; any short refutation must exploit extra structure explicitly.

### Track B (dormant): find the missing superlinear global invariant

- Continue the Gap-MCSP fusion-cover route only with a promise-specific measure that survives arbitrary sharing and improves beyond the known near-linear cover bounds.
- Use the endpoint, relay, and proof-DAG constructions already in the audit as adversarial tests for every proposed lower bound.
- Require the final estimate to cross the hardness-magnification threshold with the correct uniformity and size parameters.

### Track C (active): foundations, quantifiers, and proof systems

- Use the exact bounded-description criterion above as a proof target, not as an answer: establish the required lower bound by structural reasoning, or identify the diagonal size/exponent point where a proposed construction fails.
- Work with the explicit $\Sigma^0_2$/$\Pi^0_2$ form in Section 2.2 without inferring ZFC independence. As a stronger route, test the all-systems/all-polynomial-bounds TAUT proof-length target in Section 2.3; keep formula truth, proof-system soundness, and encoding costs separate.
- Treat the subset-sum/Jump-Free independence proposal as closed for the canonical integer encoding: Idea 121 gives a ZFC dynamic-program proof of its corollary. Reopen only for a precisely stated noncanonical map/bit-encoding version, and do not infer a separation from auxiliary-sentence independence.
- Start from a precise statement of the form "a polynomial-time checker accepts a dense set of strings whose truth entails a known hardness property."
- Charge the proof size and succinct statement verification independently; do not let an exponential universal claim enter under a short code without a sound polynomial-time checker.
- Keep conditional crypto or proof-system assumptions labeled conditional, and test whether each premise already implies $\mathrm{NP}\ne\mathrm{coNP}$ or $P\ne NP$.
- For bounded-consistency arguments, state whether the required conclusion is an external proof-length lower bound, a uniform proof-finding algorithm, or a sentence provable in a fixed weak theory. Monroe-style non-certification and GÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶del incompleteness do not by themselves give the first of these.
- For coupling/evidence arguments, distinguish fixed-pair disagreement from total variation and from size-bounded circuit discrepancy. Prove that the observer interface covers every read of the full encoded input before applying an atomic budget.
- When lower bounds are parameterized by an algorithm clock, distinguish a contradiction that specializes to one fixed $D_*$ from a claim that one sampler defeats every clock. For the latter, obtain the sampler exponent and test the padding rate condition in Section 2.17; per-clock polynomial constructions do not automatically combine into one uniform hard generator.
- Before using entropy of a sampler's satisfying witness to lower-bound search, distinguish that sampled witness from the witness a solver may choose. Test whether a verifier symmetry admits an efficiently specified canonical satisfying slice; in the current gauge lift, $g=0$ preserves satisfiability and the message (Idea 133 / audit Section 95).
- For a class-relative decompression measure, require one fixed decompressor across the family or penalize machine descriptions enough to exclude per-instance hardcoding; a polynomial code-size bound alone still permits printers for polynomial-size outputs. Even a fixed decompressor does not make existential near-shortest descriptions uniformly findable (Idea 135 / audit Section 97).
- Reject any proposed polynomial-time map that is required to turn every input $w$ into an output of absolute Kolmogorov complexity $\Omega(|w|)$: $K(f(w))\leq K(w)+O(1)$, and simple yes-instances violate the target. If incompressibility is essential, restrict and analyze the input family instead of asking a uniform map to create it (Idea 136 / audit Section 98).
- Treat this particular witness-complexity route as closed unless its definition changes: the stated $\gamma_{\mathbf P}$ is $\Theta(|x|)$, Theorem 4.4 contradicts that identity, Theorem 4.7's reverse proof assumes unprovided uniformity, and Conjecture 4.18 is impossible on simple SAT instances. A repair with an effective description selector but no absolute-$K$ richness is simply a uniform NP witness search formulation, equivalent to the original target (Ideas 135-136 / audits 97-98).
- If considering a high-K promise slice, test random padding and advice padding first. For padded SAT, a P algorithm correct on all $K(z)\geq\delta|z|$ inputs would imply $NP\subseteq BPP$ (and $P/poly$); this is a substantial consequence but not $P\ne NP$ (Idea 137 / audit Section 99).
- State the access triple $(\mathcal K,\mathsf{access},\mu)$ for every algorithmic-randomness argument. Do not transfer power from a membership oracle to a promise-input solver; check dependence on the universal machine when the threshold has no growing margin (Idea 138 / audit Section 100).
- Treat fixed-polynomial-clock incompressibility $R_{n^q}$ as a direct coNP target. The known P-immunity theorem requires super-polynomial clocks; quantify the candidate decider exponent and do not promote that theorem to a P-vs-NP proof (Idea 139 / audit Section 101).
- For algebraic ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œone-wayÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â constructions, demand a proof of the inverse lower bound in the standard bit model; finite-field identities and measured runtimes establish only the forward map and tested instances (see Idea 116 and audit Section 78).

These tracks are not assumed to converge. Evidence may close one of them and redirect effort.

## 9. Working conclusions and update discipline

1. The problem is open; there is no known proof in this work.
2. The strongest shared diagnosis is global integration plus universal certification, with construction, sharing, and transfer costs tracked separately.
3. The selector floor is a genuine theorem about certificate existence, not a solution to its construction or verification problem.
4. The four-input code-shaped trace is exact and reproducible. A separate polarity-and-disagreement construction gives an all-$m$ formula theorem; the earlier five-input, five-gate test only falsifies that fixed-cutoff lift, not the scale-matched family.
5. Shared-circuit synthesis agrees with the formula threshold in three finite cases, $m=3,4,5$, using two SAT backends for the newest lower bound. The $m=6$ query was interrupted without a conclusion. These are not an asymptotic circuit lower bound, and increasing $m$ alone is not a research objective.
6. The subset-sum consequence of the Jump Free Theorem is not a viable independence route in its canonical encoding: a bounded-weight DP proves it directly in ZFC (Idea 121 / audit Section 83). The all-arbitrary-bijection version still needs a precise computational formalization.
6. Nothing in finite tests establishes an asymptotic separation. A proof would have to replace the finite pattern with a theorem covering arbitrarily large instances.
7. Update this file after each material theorem, counterexample, failed conjecture, or change in the proof-debt ledger. Keep complete logs and citations in the audit and exact experiments in their scripts.
8. The backward-implication map in Section 2.1 records the current formal target: the ordinary hierarchy gives $\forall k\,\exists L_k$, while SAT separation needs one language/formula obstruction uniform across all polynomial clocks. Do not call this quantifier audit a proof; use it to reject constructions that silently exchange quantifiers or hide their encoding cost.
9. The proof-system branch in Section 2.3 synthesizes Ideas 27ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“45. The fixed-point tautology is sound but has only a proof-cutoff-sized interface; ordinary FCP, recursive jumps, and finite-consistency lower bounds each have separate known gaps. Any future proof attempt must improve one of those exact bounds or use a genuinely non-relativizing ingredient.
10. A lower bound for SAT search must model every read of the full encoded input. Coupling disagreement, coordinate-wise neutrality, and bounded-arity leakage do not imply computational indistinguishability; use size-bounded circuit discrepancy and prove the evidence interface is complete for ordinary input-reading machines (Idea 122 / audit Section 84). If a target is unique as a function of the public instance, opposite-target coupling endpoints necessarily have different encodings, so those bytes cannot all be free neutral evidence (Idea 132 / audit Section 94).
11. Treat semantic validity as part of a machine's type. Advice-based hierarchy results do not yield uniform semantic hierarchies by hardwiring advice unless every fixed variant preserves the promise. Even a valid hierarchy among fixed polynomial clocks has the wrong quantifier order for $P\ne NP$ (Idea 123 / audit Section 85).
12. For explicitly polynomial-clocked nondeterministic machine descriptions, the index set of globally unambiguous machines is $\Pi^0_1$-complete (Idea 124 / audit Section 86). Therefore no total computable procedure can decide global UP validity for arbitrary descriptions; delayed counterexamples also show why finite input testing alone cannot prove the promise. This blocks a generic validity-filter repair, while leaving proofs about particular machines fully possible.
13. Proof enumeration does not automatically solve this validity barrier. Assuming a consistent effective arithmetic theory $T$, there are valid clocked machine descriptions whose unambiguity $T$ cannot prove, by encoding $\mathrm{Con}(T)$ (Idea 125 / audit Section 87). The witness machine recognizes the empty language, so the result concerns descriptions, not a missing UP language or a class separation.
14. The language-level gap is controlled by UP-completeness: an r.e. list of categorical clocked machines covers all UP languages iff UP has a many-one complete language (Idea 126 / audit Section 88). The no-complete-set direction would give a language with no proof-certified categorical implementation in any sound effective theory, but that conjecture remains open.
15. A concrete sufficient target for $P\ne NP$ is an explicit $\mathcal{S}\in P$ consisting only of formulas with at most one satisfying assignment such that $\mathcal{S}\cap SAT\notin P$ (Idea 126 / audit Section 88). Proving the last clause is the full lower-bound debt; unique-solution checks on samples do not pay it.
16. Proof complexity offers a second sufficient target: prove that $TAUT$ has no p-optimal CookÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Reckhow proof system. Since $P=NP$ would give a p-optimal system, this would separate $P$ and $NP$; p-optimality also implies UP-completeness by the proof-carrying machine construction of KÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶blerÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“MessnerÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“TorÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡n (Idea 126 / audit Section 88). No nonexistence proof is known in this work.
17. GrollmannÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Selman characterize worst-case honest injective polynomial-time one-way functions exactly by $P\ne UP$ (Idea 127 / audit Section 89). Such a function would imply $P\ne NP$, but the equivalence does not make an unproved inverse lower bound easier. Any arithmetic candidate must first be one uniform total, honest, injective function under a precise bit encoding; then worst-case non-invertibility remains the full theorem-level debt.
18. Categorical languages outside P, P-recognizable unique-SAT slices with hard SAT intersection, and worst-case honest one-way functions are three equivalent ways in this project to target $P\ne UP$ (Idea 128 / audit Section 90). They share one proof debt and do not amount to independent evidence; the target is stronger than bare $P\ne NP$, whose truth need not force $P\ne UP$ by any known implication.
19. A naive diagonalization against a categorical list needs to distinguish ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œno accepting pathÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â; its universal simulator has a UP language but the direct complement lies in coUP. Finite self-reference rules using only positive witness information induce monotone Boolean maps and hence admit fixed points (Idea 129 / audit Section 91). This filters one restricted template, not all diagonal arguments; a successful proof needs a nonmonotone source or a different invariant.
20. HomanÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“Thakur characterize worst-case one-way permutations by $P\ne UP\cap coUP$ (Idea 130 / audit Section 92). For any honest P-computable permutation $f$, its unique-preimage threshold language lies in $UP\cap coUP$, because onto-ness supplies a unique certificate on both sides; it is in P iff $f$ is invertible. A certified discrete-log map can be made a permutation by mapping each valid exponent block bijectively and fixing every malformed string. This is a stronger sufficient branch than the $P\ne UP$ route, but its particular inverse lower bound is wholly unpaid.
21. A direct diagonalization against polynomial-time inverters has a fixed-exponent debt: simulating an inverter with clock $n^{k_i}$ cannot fit a single forward P clock $n^C$ for unbounded $k_i$. Padding the output scales the inverter's input too; padding only the preimage breaks honesty. This rejects a specific universal-simulation template, not diagonalization in general (Idea 131 / audit Section 93).
22. A unique message $M(Y)$ determined by a public instance means opposite-message worlds necessarily have different full inputs. Therefore raw input syntax cannot be both pair-neutral and the complete input interface for ordinary observers. Any evidence lower bound must charge all target-bearing public syntax or prove a resource-sensitive restriction covering the hypothetical SAT self-reduction (Idea 132 / audit Section 94).
23. Uniform randomness in a gauge representative does not imply hardness of a gauge-invariant message: the symmetry itself lets every satisfying assignment be transformed to $g=0$. A SAT-search algorithm under $P=NP$ can enforce that representative, so any entropy argument must connect target success to the sampler's random representative rather than to an algorithm-chosen witness (Idea 133 / audit Section 95).
24. A class-relative decompressor minimum that leaves machine code uncharged collapses on each object: a machine hardcoding $x$ prints it in $O(|x|)$ time. Therefore no polynomial-output family can have superpolynomial $\gamma_{\mathbf P}$, and pointwise existence of a fast decompressor does not yield a uniform solver (Idea 135 / audit Section 97).
25. For every fixed computable $f$, $K(f(w))\leq K(w)+O(1)$. Therefore a uniform P-time map cannot output an absolutely Kolmogorov-rich witness on every SAT input: regular satisfiable formulas have logarithmic $K$ in their length. Restricting to high-$K$ instances requires a separate hardness-preserving reduction (Idea 136 / audit Section 98).
26. Close the audited class-relative witness-complexity route in its current form: $\gamma_{\mathbf P}(x)=\Theta(|x|)$ for all $x$ under the stated output model, and its attempted uniform strengthening fails by Kolmogorov monotonicity. Reopen only for a materially different definition that proves a uniform search consequence without hiding a selector or assuming impossible absolute incompressibility (Ideas 135-136 / audits 97-98).
27. Random incompressible padding maps ordinary SAT instances into a high-K promise set with overwhelming probability; hence a P solver on that set would yield SAT in BPP. Fixing one high-K pad per length gives a P/poly solver (Idea 137 / audit Section 99). Neither consequence is itself a P-vs-NP separation.
28. A high-K promise solver, high-K advice string, and oracle for high-K membership are distinct interfaces. Resource-bounded random-string oracles can encode major class power, but that power does not transfer to promise solving; plain-K oracle power at the exact threshold $C_U(x)\geq|x|$ can even vary with the universal decompressor. On simple SAT inputs, every entry in a uniformly generated polynomial-size pad list has only $O(\log n)$ complexity, so list enumeration cannot keep calls inside a linear high-K promise. Track the complexity measure, access mode, and threshold margin separately (Idea 138 / audit Section 100).
29. For fixed polynomial $t(n)=n^q$, the language $R_t=\{x:K^t(x)\geq|x|-1\}$ lies in coNP and would separate P from NP if outside P. Known P-immunity for time-bounded random strings needs super-polynomial $t$; the enumeration proof only yields a polynomial-degree lower bound for fixed $q$. Keep the clock and verifier-class requirements coupled (Idea 139 / audit Section 101).
30. A polynomial-size list that hits $R_{K^T}$ separates P from NP only if its generation and P-decider-based selection costs fit below the same $T$ clock. In fact, generating a list that contains a $K^T$-random item already takes at least about $T/\log T$ by the description argument. Korten-Santhanam's conditional short-seed construction avoids identification by concatenation and has no subclock guarantee; their oracle barrier also warns against a direct relativizing black-box upgrade (Idea 140 / audit Section 102).
31. For an arbitrary infinite P subset, the generic prefix-free suffix proof pays a logarithmic code for the occupied output length, while plain K can infer it from program length. This gives a one-degree difference in the generic immunity argument; it is not the strongest bound for the full language, which has members at every length (Idea 141 / audit Section 103).
32. With only oracle access to a decider on suffixes, searching for an accepted suffix among 2^m possibilities has worst-case query complexity Theta(2^m), even under the promise that a hit exists. Any improvement to the fixed-clock compression proof must inspect the structure of the R_q decider or change the invariant; a generic black-box search trick cannot remove the suffix cost (Idea 142 / audit Section 104).
33. A recursion theorem does not pay for the encoding of a candidate's computation. The direct SAT liar formula based on a full tableau grows the input length to roughly the square of the candidate's runtime, so reapplying an n^d decider expands the tableau again. A valid fixed point needs a proved size bound in ordinary SAT; a succinct tableau would be a different problem (Idea 143 / audit Section 105).
34. For the full $R_{n^q}$ target with integer $q\ge2$, count guarantees a member at every length. Restricting to $n=2^k$ lets a prefix-free compressor encode $k$ in $O(\log\log n)$ bits, search only $O(\log n\operatorname{polyloglog}n)$ suffixes, and rule out every decider degree $a<q$; the runtime includes the $O(n)$ cost to print the output. This does not give P-immunity for arbitrary infinite subsets and leaves $a\ge q$ open (Idea 144 / audit Sections 101 and 103).
35. Kraft's inequality forces every prefix-free code for infinitely many selected lengths to have unbounded index-code lengths. In a one-prefix exhaustive-suffix compression, the suffix count is therefore unbounded too; a black-box decider that can spend its full $n^q$ time on each query defeats the exact-clock case. Sparser lengths slow this overhead but cannot make it constant. A proof at degree $q$ must exploit structure of the actual decider or change the invariant (Idea 145 / audit Section 107).
36. Under $P=NP$, if the full fixed-clock language $R_q$ were in P, then the relation ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œthere is an accepted length-$n$ extension of this prefixÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â lies in NP and becomes decidable in P. Greedy prefix self-reduction yields a P-time generator for members of $R_q$ at every length. Compression forces its running time to exceed $n^q$ eventually, so the generator's degree is at least $q$; FNP=FP supplies no smaller exponent and hence no contradiction (Idea 146 / audit Section 108).

37. A dense-property pseudodeterministic constructor may output its canonical member with high probability only on infinitely many lengths. Decoding its bits by a probability threshold gives a PP predicate, not automatically a BPP predicate, because the theorem has no gap on the other lengths. Therefore $P=NP\Rightarrow BPP=P$ does not directly derandomize it. This is a majority-projection gap distinct from the existential extension step; even $PP=P$ would only give an unconstrained-degree selector (Idea 147 / audit Section 109).
38. The oracle in Aaronson-Ingram-Kretschmer, Theorem 10, has $P^A=NP^A=BPP^A$ but $PP^A\ne P^A$: it gives $P^{\#P^A}>P^A$, and $P^{\#P^A}=P^{PP^A}$. Thus relativizing consequences of the P=NP collapse cannot by themselves turn the majority-output predicate from Idea 147 into P; a successful argument needs a nonrelativizing property of the concrete constructor or target (Idea 148 / audit Section 110).
39. To produce any accepted member rather than the canonical pseudodeterministic output, search existentially over the constructor's random tapes and verify candidates with the $R_q$ decider. Under $P=NP$, this is an FNP-to-FP search and succeeds on every good length, avoiding the PP majority projection. Its polynomial degree remains uncontrolled, so the $n^q$ clock contradiction is not obtained (Idea 149 / audit Section 111).
40. If a random-tape verifier accepts at least a $1-2^{-n}$ fraction of $r(n)$-bit tapes, deterministic black-box search needs exactly $\lfloor2^{r(n)-n}\rfloor$ membership queries in the worst case, while one random query succeeds with probability at least $1-2^{-n}$. Thus density alone gives polynomial deterministic query complexity only when $\max\{0,r(n)-n\}=O(\log n)$; if $r(n)-n=\omega(\log n)$ the query bound is super-polynomial. This is an oracle-query barrier only; the P=NP existential-prefix search is code-aware and remains possible, with its clock exponent unpaid (Idea 150 / audit Section 112).
41. Chen et al.'s one-bit-advice corollary adds no selector advantage: under \(P=NP\), existentially quantify the advice bit and a random tape, then verify any \(R_q\) output. This removes the advice sequence on infinitely many successful lengths but keeps the uncontrolled polynomial-degree gap. Canonical bit extraction remains a promise-majority question because only the selected advice values have a guaranteed gap (Idea 151 / audit Section 113).
42. Time hierarchy gives, for every fixed \(c\), a language in \(\mathrm{DTIME}(n^{c+1})\setminus\mathrm{DTIME}(n^c)\), so P has no common degree and, under P=NP, neither does NP. The all-machine normal form \(\forall i\exists j\forall x\,E(i,j,x)\) is equivalent to the SAT-based \(\exists j\forall\varphi\,[D_j(\varphi)=SAT(\varphi)]\) form by NP-completeness; neither form supplies a uniform exponent (Idea 152 / audit Section 114).
43. An odd-negation cycle of actual ordinary CNFs would contradict a correct SAT decider, but direct full-tableau encodings expand at every edge and do not close. The parity contradiction is established; size-controlled instance construction remains unpaid (Idea 153 / audit Section 115).
44. The direct rectangular tableau's quadratic blowup is not a general Cook-Levin lower bound: classical reductions encode nondeterministic time $T$ in $T\operatorname{polylog}T$ formula size. This improves the two-stage fixed-clock selector bound from $n^{4qd^2+1+o(1)}$ to $n^{qd^2+1+o(1)}$. The exact greedy selector uses n-1 extension queries because the high-K set has members in both first-bit halves; this remains a linear query cost. Generic SAT search needs Theta(n) NP queries under ETH, but that does not lower-bound this structured selector and ETH cannot be invoked under P=NP (Idea 154 / audit Section 116).

45. If a randomized constructor outputs any member of $R_q$ with probability at least $1-2^{-h(n)}$ and its run fits below the $n^q$ K-clock, then its random tape length must be at least $n+h(n)-O(\log n)$. For the dense-property theorem's good lengths, h(n)=n, so at least $2n-O(\log n)$ random bits are necessary. This blocks the short-seed compression shortcut but gives no contradiction because polynomial randomness and an uncontrolled constructor degree remain possible (Idea 155 / audit Section 117).
46. The dense-property pseudodeterministic theorem applies to R_q under P=NP, but its published proof chooses recursion and reconstruction parameters from the decider exponent; it proves polynomial time without a fixed-clock bound below n^q. A resource-preserving version is still needed (Idea 157 / audit Section 119).
47. Given a supplied list of m candidates containing an R_q member, conjunctions of their low-K SAT formulas find a hit in O(log m) SAT calls and total time O((m n^(q+o(1)))^d). For m=n this improves the generic selector exponent when d>1, but a polynomial list generated in sub-n^q time consists only of low-K strings; finding a guaranteed short-description list is the new barrier (Idea 158 / audit Section 120).
48. The high-K outputs of the fixed-clock universal evaluator are exactly missing outputs of a one-bit-stretch circuit of size O(n^q log n) (Idea 161). Under P=NP, a generic Avoid solver polynomial in that size gives no proved sub-n^q runtime; the upper-bound accounting is not a lower bound on this special family. The APEPP and proof-system connections identify the universal-verification barrier, but do not transfer lower bounds to it (Idea 159 / audit Section 121).
49. dWPHP is the logical form of Range Avoidance. Under JLS-secure iO and coNP not in i.o.AM, a KPT extraction argument shows PV1 cannot prove the relevant dWPHP principles, because such a proof would yield a constant-round Avoid strategy with O(1) inversion queries. This concerns feasible proof extraction, not ZFC independence, and does not give an unconditional lower bound for the special R_q family (Idea 160 / audit Section 122).
50. For q>=2, encode each program p of length j<n-1 by z=1^(n-2-j)0p, with 1^(n-1) as the dummy. Pippenger-Fischer/Koucky gives an evaluator circuit with O(n^q log n) gates. Its standard gate-list encoding has length S=O(n^q(log n)^2). Under P=NP a general Avoid solver with time S^d yields O(n^(qd)(log n)^(2d)), not a subclock guarantee even at d=1. This is an upper-bound limitation, not a lower bound on the special family. The remaining opening is a code-aware solver for the implicit evaluator, not generic search-to-decision (Idea 161 / audit Section 123).
51. Keep clock-bounded plain K and Levin Kt separate. The fixed-clock language R_q excludes only descriptions with |p|<n-1 that finish by n^q, which makes its complement NP. Kt charges |p|+log(time) and permits subexponential or exponential runtimes; Hu, Lu, and Oliveira's 2026 coding equivalence for Kt and EXP versus BPP therefore does not transfer to R_q or P versus NP. The required target is R_q not in P for one fixed q; P-immunity would be stronger than necessary. A degree floor a>=q does not suffice because P has no common polynomial degree (Idea 162 / audit Section 124).
### 2.26 The exact-clock compression boundary is a black-box bottleneck

For integer $q\ge2$, Idea 144 rules out a P decider of degree $a<q$ for the full $R_{n^q}$ target. To test whether a sparser sequence of lengths could also handle $a=q$, let $n_j$ be any computable unbounded sequence and encode its index by a prefix-free word $e(j)$ of length $h_j$. A compressor of the form $e(j)u$, with $|u|=n_j-m_j$, needs $m_j\ge h_j+C$ to save enough bits after universal-machine overhead. It must then allow at least $2^{h_j+C}$ suffix candidates.

Kraft's inequality, $\sum_j2^{-h_j}\le1$, implies $h_j\to\infty$ along the sequence. Consequently no choice of computable sparse lengths makes the number of suffixes uniformly bounded. The singleton-oracle adversary from Section 2.24 shows why a black-box search may have to test them all. If each call costs as much as the $n_j^q$ clock, the search need not fit in that same clock, however slowly the query factor grows.

This is a limitation of the *proof template*, not a lower bound on a correct $R_{n^q}$ decider. Its code might reveal common work across related suffixes, and a different compressor could avoid this interface. The exact next target is to prove such a sharing property for any correct decider, or replace accepted-suffix selection with an invariant whose production cost does not multiply the decider's full runtime by an unbounded factor. Literature check: Hirahara's result establishes P-immunity for super-polynomial clocks, while the fixed-polynomial clock remains the relevant gap in this branch ([ECCC TR20-050](https://eccc.weizmann.ac.il/report/2020/050/download/)); that theorem does not remove the equality-case bottleneck here.

### 2.27 Search-to-decision does not control the selector degree

Fix $q\ge2$. Since the full $R_q=\{x:K^{|x|^q}(x)\ge |x|-1\}$ is in coNP, under $P=NP$ it has a P decider $D_q$. Counting gives an accepted string at every length. The extension language

$$
E_q=\{(1^n,u): |u|\le n,\;\exists z\in\{0,1\}^{n-|u|}\text{ with }D_q(uz)=1\}
$$

is in NP, since $z$ is a polynomial-size witness and $D_q$ is polynomial-time. Under $P=NP$, $E_q$ is in P. Greedily query whether the current prefix still has an accepted completion after appending $0$, and append $1$ only if the answer is no. This yields a deterministic polynomial-time function $G_q$ that outputs a member of $R_q$ at every length. This is a concrete FNP-to-FP search consequence, not just the statement that membership is easy.

The selector's degree is the unpaid resource. Measure the program consisting of $G_q$ and a self-delimiting encoding of $n$ on the same fixed reference universal machine used to define $K^t$, including simulation and output costs. Its description is $O(\log n)$ bits. If this program ran in at most $n^q$ steps for infinitely many large $n$, its output would violate membership in $R_q$. Therefore its reference-machine runtime eventually exceeds the fixed clock; a polynomial implementation with exponent below $q$ is impossible, while degree $q$ with a sufficiently large leading constant is not excluded. The collapse $P=NP$ provides no degree bound below $q$ for the extension language, so this route restates the clock barrier rather than resolving it.

The direct rectangular-tableau accounting gives a selector in $n^{4qd^2+1+o(1)}$ time, but that is not the standard quasilinear formula-size reduction. Classical reductions from nondeterministic time $T$ to 3SAT have size $T\operatorname{polylog}T$. With a SAT algorithm running in $N^d$, this improves the two-stage selector bound to $n^{qd^2+1+o(1)}$: the first decision costs $n^{qd+o(1)}$, the extension verifier has that same time, its SAT reduction and decision cost $n^{qd^2+o(1)}$, and the greedy search makes $n$ sequential prefix queries. Since $d\ge1$ for explicit SAT input, this remains strictly above the $n^q$ clock. The quadratic tableau blowup was a template cost; the remaining adaptive-search factor is an accounting gap, not a lower bound on every code-aware selector. The needed advance is a batch/shared search lemma for these related extension instances, or a different compression invariant. See Section 2.35 and [Jahanjou, Miles, and Viola, Section 1.2](https://eccc.weizmann.ac.il/report/2013/099/revision/3/download/).

Recent nearby results concern different measures. Hu, Lu, and Oliveira's 2026 ICALP paper equates nontrivial coding for Levin $Kt$ with $EXP\ne BPP$ ([ECCC TR25-211](https://eccc.weizmann.ac.il/report/2025/211/)); Kabanets and Kolokolova's sublinear-error chain-rule characterization for fixed-clock $K^t$ additionally requires a strong exponential-time circuit lower bound and a promise-gap meta-complexity condition ([ECCC TR25-089, Revision 1](https://eccc.weizmann.ac.il/report/2025/089/)). Neither result supplies the missing degree-preserving selector here. Do not transfer conclusions between $K^t$, $Kt$, and randomized variants.

### 2.28 Infinitely-often pseudodeterminism leaves a majority-projection gap

Assume $P=NP$ and fix $q\ge2$. The dense language $R_q=\{x:K^{|x|^q}(x)\ge |x|-1\}$ is in P and has density at least $1/2$ at every length. Chen, Lu, Oliveira, Ren, and Santhanam's dense-property theorem then gives a randomized polynomial-time constructor $B$ and canonical members $x_n\in R_q$: on every length it outputs only $x_n$ or $\bot$ except with probability at most $2^{-n}$, and on infinitely many lengths it outputs $x_n$ with probability at least $1-2^{-n}$ ([Theorem 1.1](https://arxiv.org/abs/2305.15140)).

The output-bit threshold is a majority question. Let $p_{n,i}$ be the probability that $B(1^n)$ emits an $n$-bit output with bit $i$ equal to 1. The language $M_B=\{(1^n,i):p_{n,i}\ge1/2\}$ is in PP. On every successful length, its answers recover all bits of $x_n$, because the probability is at least $1-2^{-n}$ for a 1-bit and at most $2^{-n}$ for a 0-bit. The theorem supplies no gap on unsuccessful lengths, however, so it does not put $M_B$ in BPP. Consequently, $P=NP\Rightarrow BPP=P$ cannot be applied to this threshold predicate as stated. This differs from the prefix-extension selector in Section 2.27: that route asks an existential NP question, while output extraction asks for a majority over random tapes.

If one additionally assumes $PP=P$, bitwise evaluation of $M_B$ gives a deterministic polynomial-time generator agreeing with $x_n$ on infinitely many lengths. Its polynomial degree remains unconstrained, and the exact-clock compression argument only excludes degree below $q$. Thus even this stronger class collapse does not yield a separation by itself. The dense-property theorem instead conditionally exhibits a separation between randomized and deterministic time-bounded description measures: infinitely often, $rK^{n^c}(x_n)=O(\log n)$ for some constant $c$, yet $K^{n^q}(x_n)\ge n-1$. The random seed may have polynomial length, so fixing it does not provide a short deterministic description.

**Model update:** selector proofs have two distinct projection costs: existential projection (NP, used by greedy extension) and majority projection (PP, used to decode a randomized canonical output). A claimed transfer from randomized construction to deterministic compression must identify the all-input promise gap that makes majority evaluation a BPP predicate, or prove a special NP certificate for the majority structure. Both would still need a running-time exponent below $q$ to close the fixed-clock argument. See [Idea 147](ideas.md#idea-147---infinitely-often-pseudodeterminism-hides-a-majority-projection-step) and audit Section 109.

### 2.29 Oracle evidence that majority projection survives P=NP

Aaronson, Ingram, and Kretschmer prove there is an oracle $A$ for which

$$
P^A=NP^A\ne BQP^A=P^{\#P^A}.
$$

This entails $PP^A\ne P^A$. Relative to any oracle, $P^{\#P^A}=P^{PP^A}$: PP threshold queries allow binary search for a polynomial-bit #P count, and #P threshold counts express PP queries. If $PP^A=P^A$, this equality would force $P^{\#P^A}=P^A$, contradicting Theorem 10. Also $BPP^A=P^A$ in this oracle world, since relativized BPP lies in the polynomial hierarchy and $P^A=NP^A$ collapses that hierarchy.

This sharpens Section 2.28. A world can make SAT decision, NP search, and bounded-error randomness polynomial-time while leaving majority/counting strictly stronger. Therefore the majority projection used to recover bits of the dense pseudodeterministic constructor is a real relativizing boundary. This does not prove that its concrete $M_B$ is hard without an oracle and does not block a nonrelativizing argument tied to the actual $R_q$ decider. It locates the needed novelty: a structure-specific argument that collapses this PP threshold or avoids it. See [Idea 148](ideas.md#idea-148---the-majority-gap-survives-a-relativized-pnp-collapse), [The Acrobatics of BQP, Theorem 10](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2022.20), and audit Section 110.

### 2.30 Existential search for a valid random tape avoids canonical decoding

Fix $q\ge2$ and assume $P=NP$. Then $R_q=\{x:K^{|x|^q}(x)\ge |x|-1\}$ has a P decider $D_q$. The dense-property theorem gives a randomized polynomial-time constructor $B$ and canonical members $x_n\in R_q$ that $B$ outputs with probability at least $1-2^{-n}$ on infinitely many lengths. Let $r(n)$ bound the random tape length. Define $W_q(1^n,s)$ to mean that the deterministic simulation of $B(1^n)$ with tape $s$ emits an $n$-bit $y$ accepted by $D_q$. This relation is in P under the assumption. Its prefix-extension language $F_q(1^n,p)=1$ iff some length-$r(n)$ extension $s\supseteq p$ satisfies $W_q$ is in NP, hence P under $P=NP$. Greedy self-reduction finds a successful tape whenever one exists. Every good length has at least one such tape, so this produces some member of $R_q$ on infinitely many lengths without decoding the canonical output bits.

This avoids the PP threshold from Section 2.28, but not the fixed-clock debt. The search is polynomial with a degree determined by the P decision for $F_q$ and may be at least $q$. The compression contradiction requires a reference-machine runtime below $n^q$. This is no stronger yet than the all-length existential selector of Section 2.27, whose degree is likewise unknown. The seed construction becomes useful only if its special verifier yields a selector with a proved exponent below $q$; any such accounting must include the random-tape length, simulation and membership costs, Cook-Levin tableau size, SAT algorithm exponent, and number of seed-prefix queries. See [Idea 149](ideas.md#idea-149---search-for-a-successful-random-tape-instead-of-decoding-a-majority) and audit Section 111.

### 2.31 Density alone does not deterministically identify a successful seed

Fix length $n$, seed length $r$, and an oracle $f:\{0,1\}^r\to\{0,1\}$ with acceptance density at least $1-2^{-n}$. At most $b=\lfloor2^{r-n}\rfloor$ seeds are rejected. The exact deterministic worst-case query complexity of finding an accepted seed is $b$: query $b$ distinct seeds; if all reject, the density promise forces every unqueried seed to accept. Conversely, a strategy making fewer than $b$ queries can be answered negatively, after which an adversary marks all queried seeds and the strategy's output as rejected. At most $b$ rejections are used, so the promise remains true and the strategy fails. A single uniform random query succeeds with probability at least $1-2^{-n}$.

For the constructor in Section 2.30, take $f(s)=1$ when $B(1^n;s)$ outputs a string accepted by $D_q$. On a good length its acceptance density is at least $1-2^{-n}$. Therefore a membership-oracle-only deterministic selector needs $\lfloor2^{r(n)-n}\rfloor$ queries when $r(n)\ge n$ (and zero when $r(n)<n$); this is polynomial exactly when $\max\{0,r(n)-n\}=O(\log n)$. The Chen et al. theorem guarantees polynomial running time but does not state a randomness bound this tight ([Theorem 1.1](https://arxiv.org/abs/2305.15140)).

This query lower bound does not apply to code-aware computation of the existential prefix predicate $F_q$: under $P=NP$, that is a stronger interface that can reason about many seeds together. Nor does it show the concrete $W_q$ is hard. It proves only that near-certain success, viewed as an arbitrary dense membership oracle, gives no generic deterministic shortcut. Thus the proof target is either a random-bit-efficient constructor, a non-black-box structural shortcut for $F_q/W_q$, or another route with the total selector time below $n^q$. See [Idea 150](ideas.md#idea-150---near-certain-success-still-needs-many-black-box-seed-queries) and audit Section 112.

This should not be conflated with pseudo-deterministic query complexity. Chattopadhyay, Dahiya, and Mahajan show a cubic upper bound from pseudo-deterministic to deterministic query complexity for total search problems and study PromiseFIND1, where canonical-output requirements cause a large gap from ordinary randomized search ([MFCS 2023, Theorem 3.2](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.34)). Here the oracle lower bound concerns deterministic search for any accepted point in a near-full set; the one-query randomized algorithm is not canonical. The dense-property constructor itself is only guaranteed to succeed on infinitely many lengths. These model distinctions matter when importing query results into the time-bounded $K^t$ argument.


### 2.32 One-bit advice is cheap for existential search, not for canonical decoding

Chen et al.'s Corollary 3.2 gives a randomized polynomial-time constructor with a one-bit advice sequence \(\alpha_n\). On each advised input it outputs a canonical string with probability at least \(1-2^{-n}\), and the canonical string belongs to the dense easy target on infinitely many lengths. The advice selects the successful branch; the corollary gives no uniform polynomial-time procedure for computing this sequence and no all-length guarantee that the selected string is in the target.

For \(R_q\), assume \(P=NP\). The advice bit can be eliminated for the weaker task of finding any target member: put \(\alpha\) and a random tape \(s\) into one existential witness, simulate the randomized machine on that fixed tape, and verify the emitted \(y\) with the P decider for \(R_q\). Prefix extension is in NP and hence in P under the assumption. First query the empty-prefix extension predicate; if no witness exists, return a fixed default string. This makes the transducer total under P=NP, and it finds a valid output on every length where a valid tape exists, including infinitely many lengths supplied by the corollary. The direct selector in Section 2.27 is stronger on coverage because it finds an \(R_q\) member at every length under the same assumption. This is therefore an alternate infinitely-often existential-search interface, with one extra witness bit, not a better selector.

Canonical decoding remains different. Its bitwise predicate asks whether an output bit has probability at least \(1/2\). The gap is guaranteed only for the selected advice values, not for all inputs \((1^n,\alpha)\). Therefore this is a promise-majority predicate, not automatically a total BPP language. The implication \(P=NP\Rightarrow BPP=P\) does not apply without a total bounded-error formulation or another way to identify valid advice values.

The lesson is that advice length and advice computability are separate resources. A constant-size advice string can be eliminated by finite existential branching for an any-witness output, but that does not supply canonical-output decoding. The resulting selector also has an uncontrolled polynomial degree; to contradict \(R_q\), its reference-machine runtime must be below \(n^q\) on infinitely many target-producing lengths. This is not a new separation route until that exponent debt is paid.


### 2.33 P=NP is not a uniform-degree collapse

Fix an effective enumeration \(N_i\) of nondeterministic machines with explicit polynomial clocks and \(D_j\) of deterministic machines with explicit polynomial clocks. For each \(i,j,x\), let \(E(i,j,x)\) assert that \(N_i\) and \(D_j\) agree on \(x\). Because the clocks make both computations finite, \(E\) is decidable. The class statement has the arithmetic form

$$
P=NP \quad\Longleftrightarrow\quad \forall i\ \exists j\ \forall x\ E(i,j,x),
$$

with paired machine-and-clock indices understood. Its negation is \(\exists i\ \forall j\ \exists x\ \neg E(i,j,x)\). A proof of separation must produce one clocked NP language defeating every polynomially clocked deterministic candidate. Defeating all machines at one fixed degree only proves a language lies outside that one \(\mathrm{DTIME}(n^c)\) class.

The deterministic time hierarchy supplies, for every fixed \(c\), a language in \(\mathrm{DTIME}(n^{c+1})\setminus\mathrm{DTIME}(n^c)\), because \(n^c\log n=o(n^{c+1})\). Hence P has no common fixed exponent. If \(P=NP\), those same hierarchy languages are in NP, so NP also cannot be contained in \(\mathrm{DTIME}(n^c)\) for any fixed \(c\). This does not conflict with \(P=NP\): the class equality allows the deciding degree to depend on the language.

This blocks a tempting generic repair to the selector argument. A search-to-decision theorem giving every polynomial-time verifier a deterministic search algorithm with one fixed exponent independent of that verifier would collapse P to a fixed-degree class, contradicting the deterministic hierarchy. Likewise, diagonalizing against the first \(k\) machines incurs a degree depending on their maximum clock exponent; increasing \(k\) to cover all candidates loses every fixed polynomial bound, while fixing \(k\) leaves infinitely many candidates.

The project-specific lower bound synchronizes with this obstacle: the full fixed-clock set \(R_q\) itself requires decision degree at least \(q\) if it is in P (Section 2.22 / Idea 144). Raising \(q\) raises the known lower bound on the target's degree at the same time. Thus the generic \(P=NP\) selector, whose degree may depend on \(q\), cannot be forced below \(n^q\) by merely choosing a larger \(q\). The remaining proof target is one explicit NP language whose construction defeats every deterministic polynomial clock, or a genuinely target-specific implication that yields such a witness.

The all-machine presentation above is syntactically \(\Pi^0_3\). By NP-completeness of SAT, there is also an equivalent \(\Sigma^0_2\) presentation: some clocked deterministic machine decides SAT on all inputs. Negating that compact presentation gives a \(\Pi^0_2\) form for \(P\ne NP\). Neither quantifier form implies ZFC independence; arithmetical-hierarchy level alone does not determine provability. Source for the deterministic hierarchy: Hartmanis and Stearns, [On the Computational Complexity of Algorithms (1965)](https://doi.org/10.1090/S0002-9947-1965-0170805-7).



### 2.34 Odd-negation cycles isolate the self-reference debt

For a correct SAT decider \(A\), an odd cycle of ordinary CNFs with \(\operatorname{SAT}(\phi_i)=1-A(\phi_{i+1})\) would force \(b_0=1-b_0\). The constant anti-answer construction in Section 2.25 gives a two-cycle, which is consistent. Adding a k-state cyclic tag evolves (tag,b) to (tag+1 mod k,1-b); for odd k, the full state period is 2k, still even. More generally, every actual cycle of a map that flips SAT has even length, so finite closure alone cannot force an odd orbit. Program-index recursion does not automatically give a raw-formula fixed point. Direct rectangular tableaux for \(A(\phi_{i+1})\) expand quadratically and do not close a finite cycle. That blowup is template-specific: generic nondeterministic time T has 3SAT encodings of size T polylog(T). Even with these, a decider running in m^d time produces a next formula of size m^{d+o(1)}; this still grows for d>1, but is not a barrier to code-aware fixed-point constructions. Succinct tableaux change the target to succinct SAT. A future construction must prove the odd semantic cycle, ordinary-formula closure, and fixed-clock construction cost separately. This is a diagnostic for the tested liar family, not a barrier to every self-reference method. See [Idea 153](ideas.md) and [Idea 143](ideas.md#idea-143---a-liar-formula-needs-a-size-controlled-fixed-point).

### 2.35 Quasilinear encodings expose the remaining search cost

The rectangular tableau is only one verifier-to-SAT encoding. Classical reductions convert nondeterministic time T to 3SAT size T polylog(T), using efficient machine simulations; Jahanjou, Miles, and Viola summarize this history in Section 1.2. Therefore the earlier quadratic formula-size estimate is not a general lower bound and should not be used to diagnose the selector barrier.

For fixed q >= 2, suppose SAT is decided in N^d time. The complement verifier for R_q runs in n^q polylog(n), so the first reduction and SAT call decide R_q in n^{qd+o(1)}. The extension predicate E_q has a verifier of that time; a second quasilinear reduction and SAT call decide one extension query in n^{qd^2+o(1)}. Greedy self-reduction needs only n-1 adaptive extension queries: counting gives |R_q at length n| >= 2^{n-1}+1, so both first-bit halves contain a member and the first bit can be fixed without a query. The total remains n^{qd^2+1+o(1)}. Since d >= 1 for an explicit formula input, this is still above n^q.

This accounting identifies two different interfaces: reduction size and witness extraction. Quasilinear simulation sharply improves the first. The density promise saves one query but does not change the linear number of sequential answers in this selector; this accounting is not a lower bound against sharing across these related queries. The next mathematical target is a structured batch-search theorem for E_q, or a compression argument that uses less than a full selector. Any claimed improvement must specify whether it changes the SAT exponent d, the cost per query, the number of adaptive queries, or the compression threshold. Generic SAT witness extraction uses Theta(n) NP queries under ETH, but that theorem concerns arbitrary formulas and cannot be imported into the P=NP branch (Idea 154).

This is a refinement of the generic pipeline, not a proof of P != NP. Source: Jahanjou, Miles, and Viola, [Local Reductions, Section 1.2](https://eccc.weizmann.ac.il/report/2013/099/revision/3/download/); see also Pippenger and Fischer, [Relations Among Complexity Measures](https://doi.org/10.1145/322123.322138).


### 2.36 Randomness required by a fast high-K constructor

Fix q and suppose B(1^n) uses r(n) random bits and outputs some member of R_q with probability at least 1-2^{-h(n)} on a sequence of lengths. If the deterministic computation B(1^n;s) fits within n^q on every tape, then r(n) >= n+h(n)-O(log n) on those lengths.

Choose k=n-C log n for a sufficiently large fixed C. Every k-bit seed s has a description of length k+O(log n)<n-1 that pads s with zeros and runs B. If any such padded tape outputs x in R_q, the description violates K^{n^q}(x)>=n-1. Therefore all 2^k such tapes are failures. Since the failure fraction is at most 2^{-h(n)}, the total number of failing tapes is at most 2^{r(n)-h(n)}, forcing r(n)>=h(n)+k. If r(n)<k, all tapes are already short descriptions, contradicting the positive success probability.

For the dense-property theorem's infinitely-often success guarantee, h(n)=n, so a constructor running inside the fixed K-clock would need at least 2n-O(log n) random bits. This is a genuine constraint on the pseudo-construction route, but it is not a contradiction: the theorem permits polynomially many random bits, and under P=NP the constructor's time exponent is not bounded below q. A proof target would be to obtain, from P=NP, a constructor with error 2^{-n}, 2n-\omega(\log n) random bits, and fixed-tape runtime below n^q; the density theorem gives none of these tight resource bounds. Randomness density alone therefore cannot fix a successful seed with a short description.

This applies to any-member search and does not rely on canonical-output decoding. It complements the seed-query barrier in Section 2.31 and the conditional constructions in Section 2.30. Source: Chen et al., [Polynomial-Time Pseudodeterministic Construction of Primes, Theorem 1.1](https://arxiv.org/abs/2305.15140); project derivation: [Idea 155](ideas.md).

### Established references used by this model

- Andreev's partial Boolean function realization theorem, [MathNet record](https://www.mathnet.ru/eng/dm939).
- Hirahara, partial-MCSP NP-hardness, [ECCC TR22-119](https://eccc.weizmann.ac.il/report/2022/119/).
- Oliveira, Pich, and Santhanam, Gap-MCSP hardness magnification, [Theory of Computing article](https://www.theoryofcomputing.org/articles/v017a011/).
- Jech, *On GÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶del's second incompleteness theorem*, [arXiv:math/9204207](https://arxiv.org/abs/math/9204207).
- Hartmanis and Hemachandra, *Complexity Classes without Machines: On Complete Languages for UP*, [Theoretical Computer Science 58 (1988)](https://doi.org/10.1016/0304-3975(88)90022-9).
- Dingel, Egidy, and GlaÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸er, *An Oracle with no UP-Complete Sets, but NP = PSPACE*, [MFCS 2024](https://doi.org/10.4230/LIPIcs.MFCS.2024.50).
- KÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶bler, Messner, and TorÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡n, *Optimal proof systems imply complete sets for promise classes*, [Information and Computation 184 (2003)](https://doi.org/10.1016/S0890-5401(03)00058-0).
- KÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¶hler-Schindler and Steif use the ALL-EQUAL Boolean function in distributional complexity analysis, [paper](https://research.chalmers.se/publication/551459/file/551459_Fulltext.pdf); this is context for the test family, not a citation for the selector theorem.
- Joosten, [Propositional Proof Systems and Fast Consistency Provers](https://arxiv.org/abs/2004.05431); Egidy, [Recursive Jump Operators and Optimal Proof Systems](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.88/LIPIcs.ICALP.2026.88.html); see also [ideas.md, Ideas 27ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“45](ideas.md).
- Pervyshev, [Time Hierarchies for Computations with a Bit of Advice, ECCC TR05-054](https://eccc.weizmann.ac.il/report/2005/054/); Fortnow, Santhanam, and Trevisan, [Hierarchies for Semantic Classes](https://theory.stanford.edu/~trevisan/pubs/promise.pdf); Wu, [A Note on Time Hierarchies for Reasonable Semantic Classes without Advice](https://arxiv.org/abs/1711.11158); Oliveira et al., [ECCC TR21-039](https://eccc.weizmann.ac.il/report/2021/039/); Gajulapalli, Li, and Volkovich, [ECCC TR24-049](https://eccc.weizmann.ac.il/report/2024/049/). See Idea 123 / audit Section 85 for the promise-preservation audit.
- Goertzel, [A Quantale-Weakness Route to $P\ne NP$, arXiv:2510.08814](https://arxiv.org/abs/2510.08814), current v2; audited as a claimed proof in [audit Section 94](P_VS_NP_PROJECT_AUDIT_2026-08-24.md). The public-input neutrality and ordinary-observer coverage are not established by the stated interface.
- Project-specific derivations and caveats: [audit Section 70](P_VS_NP_PROJECT_AUDIT_2026-08-24.md), [audit Section 71](P_VS_NP_PROJECT_AUDIT_2026-08-24.md), and [audit Sections 72-76](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).


### 2.37 Randomized descriptions spend an uncharged coin budget

Let R_q be the length-n strings with K_U^{n^q}(x) >= n-1. If a randomized program of code length L, given 1^n, uses r(n) fair bits and outputs an R_q member with probability at least 1-2^{-h(n)}, for h(n) >= 1, and every fixed-tape run fits the n^q universal-machine clock, then

$$
L + r(n) >= n + min(h(n), r(n)) - O(log n).
$$

Indeed, put k = max(0,n-L-C log n) for a sufficiently large constant C. Each k-bit prefix s, followed by zeros, would otherwise give a deterministic description shorter than n-1 for an R_q output. If k>0, all 2^k padded tapes must fail. If r<k, even a full tape is a short description, contradicting positive success. When h<=r, the failure bound gives 2^k<=2^{r-h}, hence L+r>=n+h-O(log n). When h>r, the allowed number of failures is below one, so all tapes succeed; this contradicts k>0. Therefore k=0 and L>=n-O(log n), which gives the claimed bound with min(h,r). Variable random-bit use can be padded to a fixed upper bound.

For fixed L=O(log n), error 2^{-n} forces at least 2n-O(log n) random bits, and success probability at least 1/2 forces at least n-O(log n). Thus short randomized program descriptions of high deterministic-K strings are compatible with their high K: the random tape carries the missing information. Chen et al.'s randomized-K corollary measures program length but does not charge these coins ([Theorem 1.1, Corollary 1.3](https://arxiv.org/abs/2305.15140)).

Clock alignment is a separate condition. Under P=NP, R_q is dense and polynomial-time decidable, so the dense-property theorem applies. But its constructor's polynomial exponent depends on the property algorithm, whose own degree may already be at least q. The theorem does not guarantee fixed-tape runtime below n^q, and we cannot choose q after seeing the constructor without changing the property. A viable route must prove a self-aligned clock bound or a randomness-removal theorem that preserves it.

**Model update:** track three coordinates for randomized construction arguments: program bits L, coin bits r, and fixed-tape time exponent c. High deterministic K forces L+r >= n+min(h,r)-O(log n) only when every fixed-tape run, including universal-machine overhead, fits the same n^q clock; a strict runtime exponent c<q suffices. A small L alone is not compression, and a polynomial-time constructor alone does not establish c <= q. See [Idea 156](ideas.md).

### 2.38 The dense-property constructor has no proved self-clock

Under P=NP, fix q and let D_q decide R_q in n^a_q time. The fixed-clock counting argument gives a_q >= q. Chen et al.'s Theorem 1.1 applies because R_q is dense and easy, but its proof chooses tau with A_Q running in n^(tau/3), then lambda=c(tau+1)kappa and beta>=100lambda, and recursively sets n_(i+1)=n_i^beta. The reconstruction bound is (d+n)M^(c rho), with M=n_(i+1), while d'_i<=2n_i^c+n_i^tau. Thus this branch is certified in roughly n_i^(tau+beta*c*rho) time. Since tau depends on the decider exponent and beta depends on tau, the proof establishes polynomial time but no bound below n^q for Q=R_q.

This is not a lower bound on the constructor's true runtime; a faster implementation may exist. It is a limit of the theorem as a proof ingredient: the published analysis does not establish the clock fit required by the randomized-description lemma. Picking q after this constructor is analyzed changes the property and its decider. The next target is a resource-preserving construction or a selector that avoids full verification by D_q.

The general randomness inequality in Section 2.37 is L+r >= n+min(h,r)-O(log n); when h<=r it reduces to L+r >= n+h-O(log n). For the dense theorem's short fixed code and error 2^(-n), the counting argument itself forces r>=n on successful lengths, then at least 2n-O(log n) coins, if and only if the fixed-tape runtime fits the same R_q clock. See [Idea 157](ideas.md) and Chen et al., [Theorem 1.1, Section 3](https://arxiv.org/html/2305.15140v2).


### 2.39 Batch selection sharpens the exponent but exposes an input-list obstruction

For each supplied n-bit x_i, reduce the NP predicate K_U^{n^q}(x_i)<n-1 to a 3CNF F_i of size n^(q+o(1)). For a block S of candidates, F_S=AND_{i in S} F_i is satisfiable iff all candidates in S are outside R_q. If the supplied list has a member of R_q, binary splitting finds one using O(log m) SAT calls. The formula sizes shrink geometrically, so with SAT time N^d the total cost is O((m n^(q+o(1)))^d). For m=n this is n^((q+1)d+o(1)), improving the generic prefix selector n^(qd^2+1+o(1)) when d>1, but still exceeding n^q.

This does not construct the candidate list. Density greater than one half guarantees a hit only for lists containing more than half of all n-bit strings. More sharply, any polynomial-size list enumerated by one fixed program in time n^c for c<q consists entirely of strings outside R_q: an item is described by the enumerator, n, and its O(log n)-bit index, and the resulting program runs within the K-clock. Therefore no uniformly generated sub-clock list can solve the problem. A useful construction would need a nontrivial implicit family with a provable hit and a short way to expose a member, without listing a family large enough to exceed the clock.

The actual improvement is limited but rigorous: combine many independent short-description tests into one SAT conjunction, reducing oracle rounds and avoiding the second generic reduction for each extension query. It does not remove the need for an input family that already contains a high-K string. See [Idea 158](ideas.md) and [Idea 154](ideas.md).

### 2.40 Fixed-clock incompressibility is one-bit range avoidance

Fix q. For each n, enumerate all programs of length below n-1 as the inputs of a circuit C_{n,q}:{0,1}^{n-1}->{0,1}^n; use one dummy input, simulate each program for n^q steps, and map invalid or wrong-length outputs to a fixed default. Every n-bit output not in Range(C_{n,q}) has K_U^{n^q} at least n-1. The pigeonhole count guarantees a missing output. This puts the high-K construction in the exact one-bit-stretch Range Avoidance form already identified by the fiber model in Sections 2.2-2.3.

A source-checked simulation sharpens the explicit circuit size to O(n^q log n): Pippenger-Fischer/Koucky give log-space-uniform circuits of size O(T log T) for T-time computations, and the construction simulates the full final configuration. The short-program index decoder costs O(n^2), within this bound for q>=2. Under P=NP, general Avoid search takes polynomial time in the encoded circuit length. With O(n^q log n) gates, a standard gate-list encoding has length S=O(n^q(log n)^2); a solver with time S^d composes to O(n^(qd)(log n)^(2d)). Even d=1 yields only an O(n^q(log n)^2) upper bound, which does not certify the required o(n^q) runtime; for d>1, the generic upper bound is weaker still. These are not runtime lower bounds on the structured family. Thus the sharper universal simulation narrows the accounting gap without closing it. See [Idea 161](ideas.md) and [Audit Section 123](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

Ren, Santhanam, and Wang's Theorem 6.6 connects FNP algorithms for general constant-stretch Avoid with propositional proof systems that break every nonuniform proof-complexity generator. Their high-K reduction uses a closely related short-program range circuit, but with a conditioned time-bounded K convention; keep this as a structural bridge, not an unqualified identity with R_q. Under P=NP, Avoid is in FP and the theorem's proof-system consequence is consistent with NP=coNP and a polynomially bounded proof system.

**New proof target.** For the explicit unary family L_q={(1^n,y): y is outside Range(C_{n,q})}, L_q is in coNP: its complement guesses an (n-1)-bit input z and evaluates the uniformly generated C_{n,q}(z) in polynomial time. Showing L_q is not in P already implies P!=NP. The stronger target L_q not in NP would imply NP!=coNP as well, but is not necessary for the separation. The generic APEPP-completeness theorem does not establish this for the special family. Conversely, assuming P=NP gives an FP selector, but the generic accounting is polynomial in an encoded circuit length O(n^q(log n)^2), with no proved bound below the n^q clock. Any successful route must improve this clock accounting or prove an NP-certificate lower bound for this family. See [Idea 159](ideas.md) and [Audit Section 121](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

### 2.41 Dual weak pigeonhole is a proof-extraction problem

For a polynomial-time map f:{0,1}^n->{0,1}^ell with ell>n, dWPHP says that some output y is absent from the range. Counting proves existence. A deterministic selector must find y; a proof in a weak arithmetic theory must justify the universal claim that every input misses y.

Ilango, Li, and Williams use KPT witnessing to connect these tasks. A proof of dWPHP for circuit evaluation in a theory extending PV yields a constant-round Student-Teacher strategy: the student proposes y and the teacher answers with a preimage whenever y is not missing. Thus the proof would give an AVOID algorithm with O(1) circuit-inversion queries. Assuming JLS-secure iO and coNP is not infinitely often in AM, they rule out that algorithm and conclude that the corresponding dWPHP statements are not provable in TPV; APC1 therefore strictly extends PV1 under these assumptions.

This is a conditional statement about feasible proof extraction. ZFC can prove the finite pigeonhole assertion, and the PV1 result does not establish independence from ZFC. Nor does it settle P versus NP: its cryptographic and AM assumptions are unproved, and the general AVOID lower bound does not automatically transfer to the particular universal-program circuit C_{n,q}. The useful model upgrade is to distinguish mathematical existence, proof in a weak computational theory, and an efficient uniform witness algorithm. See [Idea 160](ideas.md), [Audit Section 122](P_VS_NP_PROJECT_AUDIT_2026-08-24.md), and the earlier [dual-pigeonhole audit](P_VS_NP_PROJECT_AUDIT_2026-08-24.md#58-pigeonhole-proofs-and-dual-weak-pigeonhole).

### 2.42 The range circuit is near-linear in its simulation clock

Let T=n^q, q>=2. Encode a program p of length j<n-1 by z=1^(n-2-j)0p; the all-ones string is the single dummy input. This maps the 2^{n-1}-1 short programs bijectively onto all other inputs and costs O(n^2) gates to decode. The universal machine's T-step simulation has log-space-uniform circuits with O(T log T) gates by the Pippenger-Fischer/Koucky theorem. The construction in Shalunov's exposition maps an initial configuration to the full final configuration, so it computes the output string as a multi-output function without a factor n per output bit. Thus the gate count is O(n^q log n), and a standard gate-list encoding has length S=O(n^q(log n)^2).

If P=NP, a general AVOID solver obtained from decision has time polynomial in the encoded circuit length. With S=O(n^q(log n)^2), a time-S^d solver gives O(n^(qd)(log n)^(2d)). For d=1 the bound is O(n^q(log n)^2), which fails to certify subclock time; higher d gives weaker generic bounds. This is a more exact diagnosis than the former n^{O(q)} estimate, but not a lower bound on special-case runtime. A possible new route must operate on the uniform description of C_{n,q} and avoid materializing it, without making the universal missing-output predicate too expensive. There is no such algorithm or lower bound yet.

Source: Shalunov, [ECCC TR25-078, Theorem 2.2 and Appendix B](https://eccc.weizmann.ac.il/report/2025/078/download/); Pippenger-Fischer, [*Relations Among Complexity Measures*](https://doi.org/10.1145/322123.322138). See [Idea 161](ideas.md) and [Audit Section 123](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

### 2.43 The clock-complexity plane and the coding-theorem transfer gap

For a description p of an n-bit string x, record two separate costs: program length ell=|p| and runtime tau. The fixed-clock measure K_U^{n^q}(x) asks whether any point with ell<n-1 lies below the horizontal deadline tau<=n^q. Its hard set R_q is in coNP because a counterexample is a short p together with a polynomially bounded simulation. Counting gives |R_q intersect {0,1}^n| >= 2^(n-1)+1, so it is dense at every length.

Levin's Kt(x)=min_{p,t:U^t(p)=x}(|p|+ceil(log t)) uses a different geometry: it excludes a diagonal region in the (ell, log tau) plane and allows runtimes up to nearly 2^n when the total score is below n. A Kt code need not run in n^q steps. For example, a code with length n-2sqrt(n) and runtime 2^sqrt(n) has Kt below n by sqrt(n), while its runtime lies outside every fixed n^q clock for sufficiently large n. Thus a coding theorem that yields Kt(x)<=n-omega(log n) does not automatically yield a short description counted by the NP verifier for R_q.

Hu, Lu, and Oliveira prove that weak or non-trivial coding for deterministic Kt is equivalent to EXP != BPP; their nondeterministic Kt analogue characterizes NEXP != BPP. This is a substantial coding/lower-bound bridge, but the resource measure is not the fixed polynomial clock needed here. Their theorem supplies no R_q decider lower bound and no P-versus-NP separation. Transferring it would require an additional theorem that converts the produced Kt code into one whose runtime is at most n^q while retaining enough program-length savings; the paper's statement does not provide that.

This makes the current exponent trap explicit. For each fixed q, R_q is coNP and hence lies in P under P=NP. The compression argument rules out a decider of degree a<q, but leaves a>=q. A Cook-Levin reduction followed by a SAT algorithm of degree c gives a generic upper bound around n^(qc+o(1)) under P=NP. These bounds are compatible: P contains languages requiring arbitrarily large fixed polynomial degrees, so an increasing degree floor as q grows is not itself a contradiction. Choosing q after seeing the decider changes the language and cannot close the quantifier gap.

The next proof obligation is now precise: prove R_q not in P for one fixed q, or derive from P=NP a selector/resource bound contradicting the already proved degree floor. P-immunity would suffice but is stronger than required. A generic polynomial-time search-to-decision theorem is insufficient because its exponent is uncontrolled. See [Idea 162](ideas.md) and [Audit Section 124](P_VS_NP_PROJECT_AUDIT_2026-08-24.md).

Source: Hu, Lu, and Oliveira, [*Equivalence Between Coding and Complexity Lower Bounds*, ICALP 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.110/LIPIcs.ICALP.2026.110.html), Theorems 1 and 3; full version [ECCC TR25-211](https://eccc.weizmann.ac.il/report/2025/211/).

### 2.44 Exponent floors, parameter uniformity, and conditional range avoidance

Let alpha_q be the infimum exponent a for which a P decider for R_q runs in O(n^a), if one exists. The fixed-clock compression proof gives alpha_q>=q. If P=NP and SAT has a degree-d algorithm, a quasilinear Cook-Levin encoding of the bounded simulation gives a generic decider in n^(qd) polylog(n) time, so alpha_q<=qd. These bounds scale together. Since P contains languages of arbitrarily high fixed polynomial degree, the family of inequalities alpha_q>=q is consistent with P=NP; increasing q never supplies the missing contradiction.

The quantifiers explain why a variable-clock diagonal is not an immediate repair. For each fixed q, R_q is in coNP and P=NP supplies a decider, but the exponent may depend on q. If q is instead part of the input, verifying a short program for n^q steps is not polynomial in the combined input length when q is unbounded. That uniformized language is no longer covered by P=NP. The valid target remains one fixed q with R_q not in P; proving P-immunity is sufficient but stronger.

Korten and Santhanam's 2025 paper gives conditional polynomial-time constructions of strings with K^(n^k)(x)>=n-poly(log^[d](n)) for infinitely many n, under strong time-versus-NP-oracle-with-advice assumptions; it also proves tractability of uniform Range Avoidance in specified circuit-size and stretch regimes. This is useful evidence that hardness assumptions can yield explicit high-complexity objects. It does not give the exact n-1 threshold for our R_q family, and the theorem does not bound its constructor's polynomial degree below k. Indeed, the paper notes that a K^T-hard string cannot be generated in o(T/log T); with T=n^k, this forces near-n^k construction time on successful lengths. Any attempt to use it here must check the precise uniformity, stretch, clock, and deficit parameters; ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“polynomial timeÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â alone does not beat n^q.

**Formal-logic limit.** P versus NP can be encoded as an arithmetic sentence and therefore has a definite formal statement in ZFC. It is not known whether ZFC proves that sentence or its negation. Enumerating ZFC proofs of both sides finds a proof if either exists, but no finite-time argument guarantees termination if the sentence is independent of ZFC. Thus longer proof search is not itself a completeness theorem; each attempted argument still needs a valid derivation.

**Sources:** Korten and Santhanam, [*How to Construct Random Strings*, ECCC TR25-104](https://eccc.weizmann.ac.il/report/2025/104/), especially Theorem 12 and Section 4.4; the SAT encoding and exponent accounting above are the project's deductions from the fixed-clock verifier and the stated SAT running time.


### 2.45 Multi-string time-bounded chain rule: separation target and cryptographic obstruction

Let CR denote the conditional multi-string chain rule for time-bounded Kolmogorov complexity with an error e(N)=o(N). For each fixed D>1 it asserts a fixed polynomial clock p_D and constants such that, for every sufficiently large admissible tuple,

\[
K^t(x_1,\ldots,x_\ell\mid y) \geq \sum_{i=1}^{\ell}K^{p_D(t)}(x_i\mid y,x_1,\ldots,x_{i-1}) - O(\ell\log t)-N/D.
\]

This branch has two checked directions.

**P=NP implies CR.** For fixed C>1, let A_C(x,y,1^t) accept exactly when some program p of length at most |x|-|x|/C prints x from y within t steps. This is an NP predicate: p is a polynomial-size witness and its t-step computation is polynomially verifiable because t is unary. Under P=NP, A_C is polynomial-time. Conditional plain-K counting shows that for every y, at least half of n-bit x have K(x|y)>n-O(1); these also exceed the time-bounded threshold for large n. Thus A_C rejects at least half of uniform x while accepting every x with K^t(x|y)ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€šÃ‚Â¤n-n/C. It is the natural property required by the Kabanets-Kolokolova characterization. Their Theorem 7.6 also uses Kannan's consequence that P=NP gives E not-in io-SIZE[2^{o(n)}]. Their Theorems 7.1 and 7.6 therefore establish P=NP => CR. A proven failure of CR with a linear deficit on arbitrarily large instances would imply P!=NP.

**CR rules out standard cryptographic one-way functions.** Kabanets-Kolokolova's Theorem 5.2 turns CR with e=o(N) into a P-computable natural property for K^t of usefulness n-n/D for each constant D>1. Take D=10. If a standard cryptographic one-way function existed, the standard construction from OWFs would give a secure polynomial-time generator G with n-bit output and n^epsilon-bit seed for some epsilon<1. Choose unary t polynomially large enough to cover G. Every output G(z) has K^t at most n^epsilon+O(1), below 0.9n, so the natural property accepts every generator output. It rejects at least half of uniform n-bit strings, making it a polynomial-time distinguisher and contradicting security. Hence CR implies that standard cryptographic OWFs do not exist. The paper's Appendix B gives a separate stronger-error result: its two-string chain rule with delta=o(n^{1/3}) yields deterministic polynomial-time inversion on almost all inputs for every polynomial-time length-preserving function.

Thus P=NP => CR => no standard cryptographic OWFs, while standard cryptographic OWF existence => P!=NP and CR failure. The OWF premise is unproved, so this is a conditional implication map, not a P-vs-NP proof. Nor does CR imply P=NP unconditionally: the reverse direction in the paper needs NP-hardness of the gap problem, currently conditional on cryptographic assumptions.

**Conditional witness extraction from a PRG.** A seed and its stretched output do not by themselves prove that their conditional complexities are high. The repair is to test blocks of logarithmic size. Fix a proposed chain rule with clock p(t), hidden coefficient a for O(ell log t), and error e(N,t)=o(N). Choose D so the PRG seed length N^alpha is at most (1-1/D-eta)N for some eta>0. Choose C>2D so e(N,t)ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€šÃ‚Â¤N/C eventually. For t=N^k above the required clocks, partition an N-bit PRG output into ellÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€¹Ã¢â‚¬Â N/(c log t) blocks of bÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€¹Ã¢â‚¬Â c log t bits and set

\[
S=\left\lfloor\frac{N-N/D+a\ell\log t+N/C}{\ell}\right\rfloor.
\]

With c sufficiently large, SÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€šÃ‚Â¤b-2log ell-O(1). The test A(x) accepts iff some block has K^{p(t)}(x_i|x_{<i})ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€šÃ‚Â¤S. It is deterministic polynomial time in t because it enumerates at most 2^{S+1}=t^{O(c)} candidate programs and simulates each for p(t). Counting shows A accepts only O(1/ell) of uniform strings. PRG security then implies A rejects almost all generator outputs. For any rejected output, each block has K^{p(t)}>S, so the conditional-complexity sum exceeds N-N/D+a ell log t+N/C. The entire output still has K^tÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€šÃ‚Â¤N^alpha+O(log N), which is below N-N/D by eta N. Once eÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€šÃ‚Â¤N/C, the proposed chain inequality is violated by ÃƒÆ’Ã…Â½Ãƒâ€šÃ‚Â©(N).

Thus OWF existence gives a conditional, efficient witness-generation procedure against every proposed sublinear-error chain rule: sample seeds and retain an output rejected by A. This is a useful strengthening of the implication-only audit. The coNP-looking lower bound is not tested directly; logarithmic block size lets us decide its bounded-program complement by exhaustive search in polynomial time, then PRG security forces the desired hard blocks. The construction remains conditional on OWFs and does not settle P vs NP unconditionally.

The unconditional target remains adversarially quantified: for some fixed D, every proposed polynomial clock and cutoff must have arbitrarily large tuples where the conditional-complexity sum exceeds the joint complexity by at least N/D plus O(ell log t). The PRG method supplies such tuples only under OWF existence. A proof without crypto assumptions must produce the same low-joint/high-conditional structure directly or derive it from a premise weaker than OWFs and sufficient for P!=NP.

**Source:** Kabanets and Kolokolova, [ECCC TR25-089, revision 1, Theorems 5.2, 7.1, 7.6 and B.1](https://eccc.weizmann.ac.il/report/2025/089/revision/1/download/); Huang, Ilango, and Ren, [ECCC TR23-046](https://eccc.weizmann.ac.il/report/2023/046/).


**Direction check.** In fact, P=NP implies PH=P, hence BPP=P because BPP is in PH. The deterministic time hierarchy gives EXP != P, so P=NP entails EXP != BPP. By the Hu-Lu-Oliveira equivalence, their Kt coding property therefore holds in a P=NP world. This makes the logical direction decisive: that coding theorem cannot refute P=NP; it is compatible with, and follows from, the collapse assumption.

There is also an exact way to push this bridge to its limit. Use the same universal machine for K_U^{n^q} and Kt_U. If x is in R_q, every program producing it either has length at least n-1, or runs longer than n^q. Hence Kt_U(x) >= min(n-1, q log n) = q log n for all sufficiently large n. Under P=NP, R_q is nonempty and in P, so FNP=FP gives a polynomial-time selector; if its degree is b, encoding the selector and n gives Kt_U(x_n)=O((b+1)log n) on a time-efficient fixed machine. Comparing these bounds says that b must grow at least linearly with q up to fixed machine-model constants. It does not bound b from the degree of a membership decider: generic search-to-decision leaves that exponent uncontrolled. Hu-Lu-Oliveira's n^epsilon coding guarantee is weaker than the selector's O(log n) code and cannot improve the clock coefficient. This closes the direct Kt transfer attempt: the useful missing result is still a fixed-q P-immunity theorem or a stronger resource-preserving selector implication.




### 2.46 Chain-rule consequences and the average/worst-case boundary

Let CR denote the conditional multi-string chain rule for time-bounded Kolmogorov complexity with sublinear error, in the parameter regime of Kabanets-Kolokolova, ECCC TR25-089 revision 1.

The current implication ledger is:

| Premise | Forced consequence | Status |
|---|---|---|
| \(P=NP\) | CR | Proved in Kabanets-Kolokolova using Kannan's exponential circuit lower bound and their characterization. |
| CR | \(E\not\subset io\text{-}SIZE[2^{o(n)}]\), hence \(BPP=P\) | Proved by their characterization and hardness-vs-randomness theorem. |
| CR | No standard cryptographic OWFs / secure polynomial-stretch PRGs | Proved from the efficiently computable natural property and the PRG distinguisher argument. |
| CR | The specified conditional \(GapMcK^tP\) promise problem is in P | Proved by their exact characterization. |
| CR + NP-hardness of that gap problem | \(NP=P\) | Conditional theorem: randomized NP-hardness gives \(NP\subseteq BPP\), and CR gives \(BPP=P\). The reverse implication \(P=NP\Rightarrow CR\) is already known. |

The apparent shortcut CR \(\Rightarrow\) no one-way functions \(\Rightarrow P=UP\) is invalid. The two uses of ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“one-way functionÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â do not have the same quantifiers. Grollmann-Selman characterize \(P\ne UP\) by a worst-case function that has no deterministic polynomial-time inverter succeeding on every range input. The chain-rule natural-property argument excludes cryptographic families that resist randomized polynomial-time inversion on a non-negligible fraction of uniformly sampled inputs. An inverter can succeed on almost all random inputs and still fail on exceptional inputs, so this does not rule out the worst-case function in the Grollmann-Selman theorem.

Valiant-Vazirani says \(P=UP\) implies \(NP\subseteq RP\), not by itself a known \(P=NP\) theorem. But in the CR setting, \(BPP=P\) is already available and \(RP\subseteq BPP\). Thus a valid derivation of \(P=UP\) from CR would finish the separation proof; the audited argument does not provide that derivation.

The exact implication map is therefore: \(P=NP\Rightarrow CR\); \(CR\Rightarrow BPP=P\), \(CR\Rightarrow\) no cryptographic OWFs, and \(CR\Rightarrow GapMcK^tP\in P\); and \(CR+\) NP-hardness of that precise gap promise problem \(\Rightarrow P=NP\). The last hardness assumption is the missing bridge in the cited equivalence. HIR obtain relevant meta-complexity hardness only under cryptographic assumptions and within stated parameter regimes.

The next proof target is to establish unconditional NP-hardness of the exact promise-gap problem that CR places in P, or construct a direct parameter-preserving SAT reduction. Such a reduction must produce its instance in polynomial time without first finding an unknown satisfying witness, and must meet the theorem's clock and additive-gap requirements.

**Proof discipline update.** For each implication, record (i) worst-case or average-case hardness, (ii) deterministic or randomized algorithms, (iii) single function or uniform family, (iv) all inputs or a distribution of inputs, and (v) unconditional or assumed premise. A type mismatch is a broken proof arrow even when both claims use the label ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“one-way.ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â

Sources: [Kabanets-Kolokolova, ECCC TR25-089 revision 1](https://eccc.weizmann.ac.il/report/2025/089/revision/1/download/); [Grollmann-Selman (1988)](https://epubs.siam.org/doi/10.1137/0217018); [Huang-Ilango-Ren, ECCC TR23-046](https://eccc.weizmann.ac.il/report/2023/046/download/).



### 2.47 The witness-encryption route to a conditional CR iff P = NP theorem

Kabanets-Kolokolova Theorem 6.4, using Huang-Ilango-Ren, states that if subexponentially secure witness encryption for NP exists, then it is NP-hard under randomized polynomial-time reductions to distinguish the promise cases
\[
K^{t_H(n)}(x\mid y)\le\sqrt n
\qquad\text{and}\qquad
K^{2^{n^2}}(x\mid y)\ge n-O(1),
\]
where \(|x|=n\), \(|y|=\mathrm{poly}(n)\), and \(t_H\) is a polynomial.

Under CR, the conditional-gap characterization provides a P algorithm for a promise gap with yes condition \(K^t(x\mid y)\le s\) and no condition \(K^{\tau(t)}(x\mid y)>s+n/C\), for a fixed polynomial \(\tau\) and constant \(C>1\). Given a HIR instance, set \(s=\lceil\sqrt n\rceil\) and \(t=t_H(n)\). HIR yes instances satisfy the yes condition. On HIR no instances, the time bound \(\tau(t_H(n))\) is polynomial in \(n\) and therefore less than \(2^{n^2}\) for large \(n\). Monotonicity in the time bound gives
\[
K^{\tau(t_H(n))}(x\mid y)\ge K^{2^{n^2}}(x\mid y)\ge n-O(1)>\lceil\sqrt n\rceil+n/C.
\]
Thus the CR-derived algorithm solves the NP-hard HIR promise problem. Because the hardness reduction is randomized, this implies \(NP\subseteq BPP\). CR also supplies the exponential circuit lower bound \(E\not\subset io\text{-}SIZE[2^{o(n)}]\), and hardness-versus-randomness gives \(BPP=P\). Therefore witness encryption plus CR implies \(P=NP\). Since \(P=NP\Rightarrow CR\) is unconditional, under the stated assumption \(CR\iff P=NP\).

This is an implication audit, not a proof of either premise. It exposes precisely what a fully unconditional route would need to replace: the witness-encryption hardness bridge, or a direct unconditional construction violating CR from \(P\ne NP\). The parameter match relies on the polynomial-clock promise being unary encoded; the randomized reduction yields BPP, and the E circuit lower bound is essential for the final collapse.

Sources: [Kabanets-Kolokolova, ECCC TR25-089 revision 1](https://eccc.weizmann.ac.il/report/2025/089/revision/1/download/); [Huang-Ilango-Ren, ECCC TR23-046](https://eccc.weizmann.ac.il/report/2023/046/download/).



### 2.48 The witness-locking obligation in an unconditional gap reduction

Suppose a randomized polynomial-time reduction maps a SAT formula \(\varphi\) to a promised conditional-\(K^t\) instance \((x,y,1^s,1^t)\). If a fixed program \(q\) of length at most \(s\) maps \(y\) to \(x\) within \(t\) on every reduction output, then every output satisfies \(K^t(x\mid y)\le s\); the reduction cannot map an unsatisfiable input to the high-complexity side. Thus simply including \(\varphi\) and the reduction's coins in \(y\) while generating \(x\) efficiently from them makes the reduction fail.

An unconditional reduction must generate \((x,y)\) without knowing a satisfying assignment, yet arrange that a satisfying witness enables a short \(t\)-time conditional description of \(x\), while unsatisfiable instances keep \(K^{\tau(t)}(x\mid y)>s+\delta\). HIR's witness-encryption reduction implements this witness-locking mechanism under a cryptographic assumption. No general impossibility theorem is known for non-cryptographic constructions; this observation rules out only reductions where \(y\) already provides the same efficient reconstruction in both cases.

For every candidate reduction, make the promised distinction explicit:
1. Write the actual conditional program for a YES instance and count its bits, including the encoding of any witness, random seed, and decoder.
2. Check whether the same decoder works on NO instances.
3. Prove the NO lower bound at the specified enlarged clock \(\tau(t)\), rather than arguing only that no short witness is visible.
4. Verify that the reduction samples the instance without computing an unknown satisfying witness.

This turns ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“encode SAT into Kolmogorov complexityÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â into a concrete construction obligation: witness-dependent compression must be available on YES instances but withheld on NO instances, while the reduction itself remains efficient.

Sources: [Kabanets-Kolokolova, ECCC TR25-089 revision 1, Theorem 6.4](https://eccc.weizmann.ac.il/report/2025/089/revision/1/download/); [Huang-Ilango-Ren, ECCC TR23-046](https://eccc.weizmann.ac.il/report/2023/046/download/).



### 2.49 Parameter test for direct diagonalization

For a source formula of length \(m\), direct enumeration of all programs of length at most \(s\) costs \(2^{s+1}\mathrm{poly}(m,n,t)\). With \(n\) and the unary clock \(t\) polynomial in \(m\), this is polynomial-time only for \(s=O(\log m)\). A conventional short description for a YES instance that includes a general satisfying assignment has length \(\Omega(m)\). Thus the exhaustive diagonalization template cannot both enumerate its whole cutoff and encode a general witness within that cutoff. Padding \(x\) to any polynomial length \(n\) does not alter this conflict if the desired cutoff grows as a positive fraction of n.

This is not a lower bound against all reductions: a special source could have shorter witnesses, or a different construction could avoid enumerating programs. Randomly sampling x also supplies high conditional K on NO instances with high probability by counting, but leaves open how a satisfying witness enables short recovery of x when the reduction generated x without knowing that witness. If the conditional y exposes the seed used to generate x, the same short description works in both promise cases; hiding the seed returns to the witness-locking problem.

**Candidate audit:** Given source size m, require an explicit accounting for target size n, yes-description size s, reduction time, unary clock t, and no-case complexity at \(\tau(t)\). This rules out the direct exhaustive-diagonalization template on its own parameters; it is not a general impossibility theorem.

Related: [Idea 167](ideas.md), Section 2.48.



### 2.50 Rank compression for a unique witness spends exponential time

After Valiant-Vazirani isolation, a formula may have exactly one satisfying assignment. A program can name that assignment by ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“the first satisfying assignment,ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â but evaluating this description by exhaustive lexicographic search takes \(2^{\Theta(m)}\mathrm{poly}(m)\) time for an \(m\)-bit formula in the direct construction. Since the conditional-K gap input supplies its clock \(t\) in unary, an exponential \(t\) makes the reduction's output exponential in m. A polynomial clock keeps the reduction short but does not let this rank program find the witness.

Thus uniqueness saves no description bits for a rank among all assignments: that rank may need m bits. A constant rank among satisfying assignments saves bits but leaves the search problem in the decoder. This rules out the direct Valiant-Vazirani-plus-enumeration repair of the witness-length conflict, not all methods of exploiting uniqueness.

**Audit rule:** report rank size and rank-decoding time separately. Isolation proves there is one witness with some probability; it does not compute it.



### 2.51 What the witness-encryption assumption supplies

Huang-Ilango-Ren's reduction samples a uniform message \(m\in\{0,1\}^n\) and encryption randomness r, then outputs \(x=m\) and \(y=\operatorname{WE}(1^\lambda,\varphi,m;r)\). This is efficient without a witness.

If \(\varphi\) is satisfiable, a witness w decrypts y to m. The conditional Kolmogorov program stores the formula and the fixed decryption procedure plus w; their parameters ensure its length is below the yes cutoff \(n^{1/c}\) and its runtime is polynomial \(t_1(n)\).

If \(\varphi\) is unsatisfiable, enumerate all programs of length at most \(n-105\) for clock \(t_2(n)=2^{n^c}\) on condition y. This gives a list containing every output with conditional complexity at most \(n-105\). Witness-encryption list-security says the sampled uniform m is in the list with probability at most \(1/3\), so it has conditional complexity above \(n-105\) with probability at least \(2/3\). The parameters keep the enumeration within the security budget.

Thus the primitive supplies both halves of the reduction: witness-gated compression on satisfiable inputs and list-hiding on unsatisfiable inputs. An unconditional replacement must prove these two properties for a polynomial-time generated pair (m,y) without already solving SAT. Merely making m random yields the high-K half but not the low-K half; making m efficiently reconstructible from public y yields the low-K half in both cases.

Source: [Huang-Ilango-Ren, ECCC TR23-046, Theorem 3.1 and its proof](https://eccc.weizmann.ac.il/report/2023/046/download/).



### 2.52 Witness encryption does not itself rule out P = NP

Under the standard definition, witness-encryption security is required for NO instances, while decryption correctness is required when a valid witness exists. If \(P=NP\), an encryption algorithm can decide whether \(\varphi\) is satisfiable: output the tagged plaintext \((1,m)\) when it is, and output \((0,r)\) with fresh random r independent of m otherwise. A valid witness enables decryption in the satisfiable branch. In the unsatisfiable branch, ciphertext distributions are identical for all messages, so security is perfect.

Thus witness encryption can coexist with \(P=NP\); it does not secretly supply the separation. The conditional result from Section 2.47 is consistent: under WE, CR implies the collapse \(P=NP\), and in that collapse world WE can be trivialized using the SAT decider.

Source for the security condition: [Huang-Ilango-Ren, ECCC TR23-046, Definition 2.1](https://eccc.weizmann.ac.il/report/2023/046/download/).



### 2.53 Algorithmic chain rule: constructive budget allocation, with a strict notion mismatch

Hirahara and Nanashima's revised 2026 report assumes \(GapK^t\text{-vs-}K\in pr\text{-}BPP\) and gives an algorithmic chain rule. On a sequence \(x=(x_1,\ldots,x_m)\), an efficient randomized procedure produces per-coordinate integers \(k_i\) such that, with high probability, each \(k_i\) lower-bounds the appropriate conditional time-bounded universal information \(q^{\tau(t)}(x_i\mid x_{<i})\), while their sum is at most \(q^t(x)+mO(\log t)\). The algorithmic output matters: it makes the budget allocation usable inside later adaptive procedures. The paper uses it to derive efficient universal inductive inference under the meta-complexity assumption.

This result does not currently give a SAT reduction. Its assumption is an *unconditional* gap with YES \(K^t(x)\le s\) and NO *plain, unbounded* \(K(x)>s+c\log(t|x|)\). The KK/HIR construction concerns conditional \(K^t(x\mid y)\), and HIR's NO promise lower-bounds \(K^{2^{n^2}}(x\mid y)\) at a finite clock. These differ in both conditioning and clock strength.

Formally, \(K(x)=\inf_T K^T(x)\le K^T(x)\). A high lower bound at a particular finite T does not lower-bound the infimum: a shorter program may halt after T. Conversely, a lower bound on plain K implies the same lower bound at every finite clock. So HIR's finite-clock list-security guarantee cannot directly satisfy the newer plain-K NO promise. Removing the condition y also has a cost: a conditional YES program uses y for free, while an unconditional program must describe or efficiently regenerate it, which can exceed the cutoff.

| Route/condition | What is controlled | What the 2026 chain rule adds | Missing bridge to P vs NP |
|---|---|---|---|
| Hirahara--Nanashima \(GapK^t\text{-vs-}K\in pr\text{-}BPP\) | Unconditional, fast YES descriptions versus high *plain* K on NO | Produces usable per-prefix complexity budgets and yields universal inductive inference | No matching NP-hard reduction established; no \(P=NP\) or \(P\ne NP\) consequence stated |
| KK/HIR conditional \(GapMcK^tP\) | YES fast \(K^t(x\mid y)\), NO high \(K^T(x\mid y)\) for explicit large T | No automatic transfer: condition and plain-K lower bound differ | Under subexponentially secure WE, the exact KK chain rule gives the conditional collapse theorem already recorded in ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§2.47 |

**Research decision.** A reduction audit must preserve four labels at every arrow: plain versus time-bounded K, conditional versus unconditional, deterministic K versus randomized-universal (q^t), and finite-clock versus all-clock lower bounds. A promising next lemma would bridge one of these gaps with explicit code-length and clock accounting; absent that lemma, the 2026 result is a stronger tool for inductive inference, not progress to an unconditional separation.

There is a further implication check: \(P=NP\Rightarrow DistNP\subseteq AvgP\subseteq AvgBPP\Rightarrow GapK^t\text{-vs-}K\in pr\text{-}BPP\Rightarrow\) the stated inductive-inference algorithm. The first arrow is immediate because a polynomial-time SAT/NP decider solves every distributional instance. Thus this route's premise and conclusion are compatible with \(P=NP\). The cited work gives this forward implication, not a reverse implication to \(P=NP\).

**Sources:** Hirahara--Nanashima, [ECCC TR25-092 revision 1](https://eccc.weizmann.ac.il/report/2025/092/revision/1/download/), Definitions 2.1/4.3 and Lemma 5.1; Kabanets--Kolokolova, [ECCC TR25-089 revision 1](https://eccc.weizmann.ac.il/report/2025/089/revision/1/download/); Huang--Ilango--Ren, [ECCC TR23-046](https://eccc.weizmann.ac.il/report/2023/046/download/).



### 2.54 A fixed-clock avoidance family yields an E hard function if P = NP

This is a conditional derivation from the project's range-avoidance construction. Let \(N=2^m\), fix a sufficiently large constant q, and let \(C_{N,q}:\{0,1\}^{N-1}\to\{0,1\}^{N}\) simulate every program of length below \(N-1\) for \(N^q\) steps, outputting its N-bit result or a default. The circuit has \(G=O(N^q\log N)\) gates and a standard gate-list input has length \(S=O(N^q(\log N)^2)\). Any missing output \(y_N\) has \(K_U^{N^q}(y_N)\ge N-1\) (Ideas 159 and 161).

Assume \(P=NP\). The predicate that a prefix u extends to a missing output of a given circuit is in \(\Sigma_2^P\); since \(\mathrm{PH}=\mathrm{P}\), output a missing y one bit at a time in polynomial time in the explicit circuit size. Thus \(y_N\) can be found in \(\mathrm{poly}(S)=N^{O(q)}\) time. Let \(f_m\) have truth table \(y_{2^m}\). Computing \(f_m(z)\) by generating the whole truth table takes \(2^{O(m)}\) time, hence \(f\in E\). This remains true even if the construction is slower than \(N^q\): N is \(2^m\), and every fixed polynomial in N is single-exponential in m.

If an m-input circuit D of size s computes \(f_m\), a fixed program can encode D and print its entire truth table. Its description length is \(O(s\log s+\log N)\); its simulation time is at most \(N^b\) for a fixed b when \(s\le N\). Choose q>b and a sufficiently small constant c. For \(s\le cN/m\), the description is below \(N-1\) and the runtime is at most \(N^q\) for large m. That contradicts \(K_U^{N^q}(y_N)\ge N-1\). Therefore
\[
C(f_m)=\Omega(2^m/m).
\]
So \(P=NP\) implies that E contains a near-maximum circuit-hard function, and in particular \(E\not\subset io\text{-}SIZE[2^{o(m)}]\). This supplies a concrete witness for the circuit-lower-bound conjunct in the KK characterization. It does not contradict \(P=NP\): the witness lies in E rather than NP, and the deterministic time hierarchy gives \(P\subsetneq E\).

**Resource accounting:** the range-avoidance computation uses \(\mathrm{poly}(S)\) time to put the hard truth table in E; the separate \(N^q\) clock is used to refute a hypothetical small circuit. The output length N and the lower-bound language input length m=\(\log N\) must not be confused.

**Novelty calibration:** the general Range-Avoidance-to-E-circuit-hardness implication is established in the literature; this is a conditional instantiation for the project's fixed-clock family. See [ECCC TR24-076](https://eccc.weizmann.ac.il/report/2024/076/) and [Ideas 159/161/173](ideas.md).

**Sources:** the project's [Ideas 159/161](ideas.md); Chen, Hirahara, and Ren, [*Symmetric Exponential Time Requires Near-Maximum Circuit Size*](https://arxiv.org/abs/2309.12912); Kabanets--Kolokolova, [ECCC TR25-089 revision 1](https://eccc.weizmann.ac.il/report/2025/089/revision/1/download/), Theorems 7.1 and 7.6.


### 2.55 The fixed-clock route has a degree barrier

Fix q and use the range circuit \(C_{n,q}\) from Idea 159. It has \(G=O(n^q\log n)\) gates and a standard gate-list input of length \(M(n,q)=O(n^q(\log n)^2)\); a missing output \(y_n\) satisfies \(K_U^{n^q}(y_n)\ge n-1\). If \(P=NP\), the prefix-extension predicate for AVOID is in P because it is in \(\Sigma_2^P\). Let d be the fixed polynomial degree of this decider in the explicit circuit input size. The generic bitwise search takes at most
\[
O(nM(n,q)^d)=n^{qd+1}(\log n)^{2d}
\]
time. To turn its output into a contradiction, this would have to be below \(n^q\); the required inequality \(qd+1<q\) is impossible for \(d\ge1\). Even granting a direct functional selector of degree \(d'\ge1\), its generic bound \(M^{d'}\) still requires \(qd'<q\), also impossible.

This proves a limitation of the generic proof route, not an unconditional lower bound against every specialized selector. The Kolmogorov argument says that no fixed program taking n and fixed q can generate these missing outputs in \(o(n^q)\) time. A general AVOID selector instead receives the explicit gate list, whose standard uniform construction takes \(O(n^q(\log n)^2)\) time; the K argument does not directly lower-bound that selector's runtime measured from receipt of this longer input. Thus a P algorithm under \(P=NP\) may be polynomial in circuit size and remain consistent with the K clock. It can yield the E near-maximum circuit lower bound in ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§2.54 without contradicting \(P=NP\).

**Prior-work integration:** the degree-floor conclusion is already captured in Ideas 139, 161, and 163. This section is a cross-check and records the input-model distinction; it does not advance the fixed-q P-immunity result.

**Succinct-input check:** replacing the explicit gate list by a short uniform circuit generator does not preserve the \(\Sigma_2^P\) search predicate. At the empty-prefix query, for \(n=2^m\), the quantified output y and preimage x have length exponential in m, and circuit evaluation is exponential in m. The succinct prefix-extension problem is in \(\Sigma_2^{EXP}\) under the usual encoding; \(P=NP\) collapses only PH. Unary padding of length n can restore the polynomial-hierarchy scale, but each fixed-q padded language has its own P-decider degree and the collapse gives no bound tying that degree to q. Padding to \(n^q\) makes input length match the K clock. Neither representation closes the exponent gap.

**New proof target:** stop trying to make this selector outrun its own clock. A successful separation must instead connect a logical or proof-theoretic feature of SAT to a property incompatible with \(P=NP\), or construct one NP verifier that diagonally handles every polynomial exponent. The latter must solve the uniform-exponent problem: a fixed NP verifier has one fixed polynomial bound, whereas the putative P decider may have any fixed degree.

**Learning:** the failure is structural and input-model-sensitive. \(P=NP\) collapses the decision level for this total search relation; the output carries n bits of clock-bounded incompressibility relative to a short uniform generator, while the search algorithm is given an explicit circuit of size \(M(n,q)\). Membership in FP does not compare these two input models. Polynomial degrees are multiplicative in q, so ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“choose q largerÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â is not a valid repair.


### 2.56 Source hiding is necessary for a SAT-to-K-gap reduction

Let a randomized reduction on formula \(\varphi\) and tape r output \((x,y,1^s,1^t)\), where \(|\varphi|=m\), \(|r|=\rho(m)\), and \(|x|=n\). Suppose the NO promise is \(K_U^{\tau(t)}(x\mid y)>s+\Delta(n)\), and the reduction runs in time \(T_R(m)\).

If a program q, given y, reconstructs \(\langle\varphi,r\rangle\) in \(T_0\) steps, a fixed wrapper runs the reduction on that recovered pair and prints x. Whenever this composition fits within \(\tau(t)\), it gives \(K_U^{\tau(t)}(x\mid y)\le |q|+O(1)\). Therefore every promised NO output requires \(K_U^{T_0}(\langle\varphi,r\rangle\mid y)>s+\Delta(n)-O(1)\) for every such fitting decoder. A description that simply stores \(\varphi,r\) also gives \(K_U^{\tau(t)}(x\mid y)\le m+\rho(m)+O(\log(m+\rho(m)))\) whenever the reduction itself fits the NO clock.

This turns Idea 167's reconstruction warning into a quantitative source-hiding condition. For unsatisfiable inputs, y must conceal enough of both the formula and the reduction tape that their recovery plus R cannot compress x below the NO threshold. HIR's witness-encryption reduction instead gives a conditional mechanism for making its random message incompressible given y; that does not establish a separate source-and-tape hiding theorem. The condition does not imply a one-way function and is not an impossibility theorem for unconditional reductions.

**Use as a proof filter:** before accepting any proposed reduction, compare its source length, random-tape length, reduction clock, YES threshold, and NO gap. Then check whether y efficiently reconstructs the source and tape within \(\tau(t)\). This is a concrete necessary-condition test, not a hardness proof.


### 2.57 NO-side K gaps impose a randomness budget

For a randomized reduction from an \(m\)-bit formula with a fixed \(\rho(m)\)-bit tape, the program that stores the formula and tape, ignores \(y\), and runs the reduction gives
\[
K_U^{\tau(t)}(x\mid y)\le m+\rho(m)+O(\log(m+\rho(m)))
\]
whenever the reduction and universal simulation fit the NO clock. Hence a promised NO cutoff \(k=s+\Delta(|x|)\) requires source-plus-tape description length above \(k\). If \(k\gg m\), this forces \(\rho(m)\ge k-m-O(\log k)\); in particular, target strings with a near-\(n\) NO complexity threshold and source length \(o(n)\) require nearly \(n\) random bits, assuming the clock covers the reduction.

This is a necessary randomness budget, not a separation. The deterministic special case is immediate: if the NO cutoff exceeds source length by more than the \(O(\log m)\) encoding overhead, a deterministic reduction is itself a short conditional program for x and cannot output a promised NO instance. In HIR, the target \(x=M\) is itself sampled uniformly from \(n\) bits, so the reduction already uses at least \(n\) random bits. The generic source-code floor is therefore compatible with its \(K^{2^{n^2}}(M\mid y)\ge n-O(1)\) NO guarantee. List-security is the substantive ingredient that prevents \(y\) from yielding a short description of \(M\); the source-and-tape calculation adds no contradiction to that construction. See [Idea 176](ideas.md).


## 2.58 The cover route has no remaining representation bridge

For the Gap-MCSP promise, take the finite universe Gamma=Y union Z, target A=Y, complement U=Z, and generator sets equal to each input-literal slice restricted to Gamma. This matches Cavalar and Oliveira's semi-filter cover definition. Their fusion lower bound rho(A,B) <= D_cap(A|B) says any fan-in-two De Morgan separator has at least rho AND gates. A superlinear rho bound would therefore rule out arbitrary small circuit separators in the magnification range; no assumption about a solver following the project closure trace is needed.

The project firing-rule circuit construction runs from a cover to a circuit and does not by itself establish this direction. The published rho <= D_cap theorem does. I checked the set-system definitions and the circuit model; the transfer is closed subject to the exact parameter and basis conventions in the ledger.

The remaining mathematical obstruction is a superlinear bound on rho. The proof-DAG leaf argument gives N-o(N) and stops because its resource is the number of table coordinates. It cannot be amplified by repeating the same per-anchor trace. The next target is a global charge for how one fixed rule list is reused across many low-circuit anchors, or a different invariant that still applies to arbitrary endpoints.

The live dependency graph, claim statuses, and adversarial checklist are in research/. No candidate proof is recorded.
## 2.59 A pair can hit many anchored filters without covering those anchors

Assume the high-circuit set realizes every pattern on any three fixed truth-table coordinates, which follows at the magnification parameters from the circuit-counting bound for fixed beta<1 and large N. Let G_(i,b) be the high tables with bit b at coordinate i. For coordinates i,j, define E=G_(i,0) union G_(j,0) and H=G_(i,1) union G_(j,1).

For any low anchor a with a_i != a_j, its upward closure F_a of matching literal generators contains both E and H. The intersection E intersect H consists of the off-diagonal i,j patterns. Three-coordinate fullness shows no matching generator is a subset of this intersection, so E intersect H is not in F_a. Therefore the pair violates this particular anchored filter.

Choose i,j as the truth-table coordinates for inputs 0^n and e_1. Among the 2^(n+1)=2N affine Boolean functions, exactly N have different values there; each has circuit size O(n), below s1 for large n. One pair therefore hits at least N distinct explicit anchored filters; distinctness follows because a matching slice at a coordinate where two anchors differ belongs to only one of their upward closures. It does not cover all filters above any anchor, so it gives no bound on rho. It does refute a simple proof strategy that assigns only a constant number of anchor interactions to each pair.

This stress test sharpens the global-sharing obligation: count completed closure derivations or residual-set reduction, not the raw number of anchors touched by a rule. See C-09 and the Q1 adversarial check in the research ledger.


## 2.60 Local Hamming-ball thresholds collapse under a balanced pair

The project semi-filter definition is easy to misread: a semi-filter is a nonempty upward-closed family of subsets of U that excludes the empty set. It does not have to preserve every intersection. Preservation is tested only against the proposed pair list. Therefore F_a={S subseteq U : mu_a(S)>1/4} is a valid semi-filter whenever each anchor generator has mass above 1/4.

Take N=2^n, s2=N^beta, s1=s2/(c n), U={z:CC(z)>=s2}, and Y={a:CC(a)<=s1}. For each a in Y, let mu_a be uniform on the high tables within Hamming distance d=K s2 of a. Standard circuit counting gives M(t)<=2^(C0 t log(n+t)). For fixed beta<=1/2 and K>4C0, the ball has volume at least (N/d)^d, whose logarithm exceeds log M(s2) by Omega(s2 log N). Hence each high part H_a has size 2^(Omega(s2 log N)). A fixed coordinate disagrees with a on at most d/N of the full ball, and deleting the M(s2) low tables changes this by a negligible factor. Thus every matching literal slice has mu_a-mass 1-o(1), in particular above 3/4.

Now color each z in U independently red or blue. For a fixed anchor, Hoeffding bounds the chance either color receives at most 1/4 of H_a by 2 exp(-|H_a|/8). There are only 2^(O(s2)) low anchors, so a union bound succeeds because |H_a|>=2^(Omega(s2 log N)). Some partition U=E disjoint-union H therefore has mu_a(E),mu_a(H)>1/4 for every a. The pair belongs to every F_a in both coordinates, while E intersect H is empty and belongs to none. One arbitrary endpoint pair thus violates all the selected threshold semi-filters simultaneously.

This is a proved no-go for a natural Q2 distribution: any fractional dual supported on these one-per-anchor local-threshold filters has a pair covering its entire mass. It does not rule out other, nonlocal semi-filters. The lesson is to test pair-selected balanced partitions against the candidate dual before optimizing its measure. The full quantified proof and circuit-counting constants are in C-10.
## 2.61 A distinct conditional bridge through Extended Frege

Pich and Santhanam give a proof-theoretic route to P != NP: under their bounded-arithmetic formalization, non-polynomial-boundedness of Extended Frege together with a polynomial-time error-witness function for incorrect SAT circuits implies the separation. Their paper lists feasible anti-checkers as a separate sufficient condition. The error-witness condition quantifies over arbitrary polynomial-size SAT circuits, so it addresses the arbitrary-algorithm issue semantically. However, it moves the bottleneck to a major open proof-complexity statement, EF non-p-boundedness, and to a formalization condition that cannot be inferred merely from standard-model existence.

There is a useful direction check. Assuming a polynomial-time SAT decider, the relation "circuit C errs on formula x" is polynomial-time decidable. Existence of an error is therefore an NP search problem in the combined input (C,1^n); under P=NP, prefix self-reduction yields a polynomial-time error finder. This shows that the standard-model witness condition is compatible with P=NP. It does not establish the paper's S2^1-provability condition, and it does not supply an EF lower bound. The route is a valid conditional framework, not a current proof. See Pich and Santhanam, https://arxiv.org/abs/2312.08163, and Q7 in the research queue.

In detail, for a circuit C and prefix p define Q(C,1^n,p) to mean that some n-bit extension x of p satisfies C(x) != SAT_n(x). If SAT is in P, this is an NP predicate and hence a P predicate. Querying Q on successive prefixes constructs an error input in polynomially many queries. Thus the standard-model error-witness side of the conditional theorem is not itself a separation assumption. The extra issue is proof inside S2^1, not the search-to-decision reduction; see C-12.

## 2.62 [RETRACTED] Complement-side coordinate-counting claim

The attempted claim that the high side satisfies `rho(Z) >= N - log_2 |Y| - 1` is false: a high-anchor subcube avoiding `Y` may contain gap tables and other high tables, so its cardinality is not bounded by `|Y|`. Consequently, the derived `2N-o(N)` De Morgan lower bound is withdrawn.

The valid replacement is the interpolation bound recorded in ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§2.64: if a leaf trace fixes `q` distinct truth-table positions around a high anchor, every assignment on those positions can be extended by a DNF of size `O(qn)`. When `q` is small enough, this extension lies in `Y`, contradicting that the leaf subcube avoids `Y`; this yields only `rho(Z)=Omega(s_1/n)`, not `N-o(N)`.
## 2.63 The cyclic cover target is stronger than magnification requires

OPS magnification requires that Gap-MCSP have no circuit family of size $N^{1+\epsilon}$ in the stated quantifier regime. On the promise domain $\Gamma=Y\sqcup Z$, the restricted literal generators represent any De Morgan circuit, and any fixed complete basis has a constant-factor De Morgan simulation. Therefore a superlinear lower bound on ordinary acyclic set complexity $D(Y\mid\mathcal B)$ is the minimum direct target.

The project route historically sought $\rho(Y,\mathcal B)>N^{1+\epsilon}$. More generally, complement duality gives $D(Y\mid\mathcal B)\ge\rho(Y,\mathcal B)+\rho(Z,\mathcal B)$, so a superlinear bound on this sum would also suffice. Cavalar and Oliveira identify each $\rho$ exactly with cyclic intersection complexity and prove $\rho\le D_\cap\le\rho^2$. These cover conditions are stronger than OPS needs; the valid high-anchor estimate is only the interpolation bound in ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§2.64. The historical cross-anchor work remains useful only if it gives acyclic progress or a credible superlinear cyclic theorem. The published non-membership quantifier should not be inflated to a claim that every sufficiently large length is hard; retain exponent slack when changing circuit bases.

The resulting dependency chain is: O-1 (slightly superlinear circuit lower bound for Gap-MCSP) ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ OPS Theorem 1.4 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ $NP\not\subseteq P/poly$ ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ $P\ne NP$. The local cover compiler is not a missing bridge. The unproved object is the strong arbitrary-circuit lower bound itself. See [frontier reassessment](research/FRONTIER_REASSESSMENT_2026-09-25.md).

## 2.64 Corrected high-anchor interpolation bound

Let a high truth table $a\in Z$ be fixed. In the fusion trace over the low side $Y$, suppose the empty intersection fixes $q$ truth-table positions to match $a$. A subcube avoiding $Y$ cannot be bounded in size by $|Y|$: it may contain only gap or high tables. The valid observation is instead that any prescribed pattern on $q$ distinct positions can be extended by a DNF of size $O(qn)$: make one minterm for each position prescribed 1, then disjoin the minterms. If $q\le s_1/(C n)$ for a suitable constant $C$, this extension is a low-circuit table in the subcube, a contradiction. Since a trace with $m$ pair rules has at most $m+1$ leaves, $\rho(Z,\mathcal B)=\Omega(s_1/n)=\Omega(N^\beta/n^2)$.

This adds only a sublinear term to the OR-side complexity and does not improve the leading $N-o(N)$ lower bound from the low-anchor trace. The failed symmetric count is retained in ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§2.62 with an explicit retraction so the same inference is not reused.

## 2.65 Fixed samples fail; the anti-checker must adapt to the whole truth table

Let $N=2^n$, $s_2=2^{\beta n}$, and $t=2^{10\beta n}$, for any fixed $0<\beta<1/10$. Fix any sample $Q\subseteq\{0,1\}^n$ of size at most $t$. There are $2^{N-|Q|}\ge2^{N-t}$ truth tables that are zero on $Q$, whereas circuit counting gives at most $2^{O(s_2\log(n+s_2))}=2^{O(n2^{\beta n})}$ tables of circuit size at most $s_2$. Since $t+n2^{\beta n}=o(N)$, at least one table $f$ that is zero on all of $Q$ has complexity greater than $s_2$. The constant-zero circuit agrees with this high-complexity $f$ on every sampled point. So a fixed anti-checker sample cannot work uniformly over all high-complexity functions.

This pinpoints why the OPS anti-checker lemma computes its sample from the full truth table: adaptivity is necessary. The relevant lower-bound object is a multi-output circuit $A_{n,\beta}$ that reads all $N$ bits of $f$ and outputs $t$ query locations; on every $f$ with circuit complexity $>s_2$, those locations must collectively refute every circuit of size $s_1=s_2/(10n)$. OPS show that if $\mathrm{NP}\subseteq\mathrm{Circuit[poly]}$, such selectors exist with size $N^{1+O(\beta)}$, and combine them with a succinct-MCSP decider to solve Gap-MCSP. Thus a lower bound against these adaptive selectors is a real alternate target, but it still has to defeat arbitrary input-dependent computation; the fixed-sample counting lemma does not do that.

The named static Anti-Checker Hypothesis is a distinct parameter regime: it asks for a fixed family of $2^{(2-\epsilon)n}$ sets of size $2^{n^{1-\epsilon}}$ that covers functions above circuit size $2^{n^\lambda}$. Chen et al. refute that hypothesis using a formula lower bound, but those set sizes and hardness thresholds differ from OPS Lemma 4.1, where $s_2=2^{\beta n}$ and $t=2^{10\beta n}$. A selectorÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢s range is itself a fixed family of candidate samples, but it can have up to $2^{tn}$ members; the refutation of the much smaller, differently parameterized family does not rule it out. See [Chen et al.](https://arxiv.org/abs/1911.08297), C-15, C-17, and [the OPS anti-checker lemma](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).
## 2.66 Self-referential patching gives a descent, not a contradiction

Fix a valid adaptive selector $A$ and any circuit $D$ of size at most $s_1$. From a table $f_i$, replace the queried bits in $A(f_i)$ by $D$'s values. If $CC(f_i)>s_2$, at least one queried bit disagrees with $D$, so the Hamming distance to $D$ decreases. After at most $N$ strict updates, the process reaches $f_*$ whose selected labels all match $D$. Selector correctness forces only $CC(f_*)\le s_2$.

The endpoint may be in the gap $(s_1,s_2]$, so this does not construct a low MCSP table. If the initial table has complexity above $2s_2$, changing it to any table of complexity at most $s_2$ requires at least $\Omega(s_2/n)$ bit edits, since each corrected truth-table point can be patched with an $n$-literal minterm. But the anti-checker sample has $t=2^{10\beta n}\gg s_2/n$ coordinates, so one batch can make all required changes. Processing only one disagreement per round produces many rounds without implying that $A$ is large. This is a rigorous limit of this self-reference idea, recorded in C-16 and Idea 182.
## 2.67 The selector must range over many samples, but range is not complexity

Let $\mathcal R$ be the set of distinct query sets output by a valid OPS selector and $q=|\mathcal R|$. The union of all possible queried positions has size at most $qt$. If $qt<N-\log_2M_2$, where $M_2$ counts truth tables of circuit size at most $s_2$, then a counting argument produces an $f$ of complexity greater than $s_2$ that is zero on this entire union. The constant-zero circuit then passes every sample the selector could output, a contradiction. Therefore $q\ge(N-\log_2M_2)/t=(1-o(1))N^{1-10\beta}$ for fixed $\beta<1/10$.

This is a stronger adaptation statement than merely saying one fixed sample fails: the selector needs exponentially many distinct query sets as a function of $n$. C-18 strengthens the range estimate to $q\ge 2^{\eta s_2/n}$ by considering sparse hard truth tables. Neither bound is a circuit-size lower bound. A $t$-point output has $tn$ address bits; copying suitably grouped input bits to these addresses can produce $2^{\Theta(tn)}$ distinct samples with output wiring alone (and $tn\gg s_2/n$ here). Those outputs need not be valid anti-checkers. The unresolved computation is routing each high-complexity table to a sample whose labels refute every small circuit. See C-17 and C-18.

## 2.68 Sparse hard tables force a large anti-checker range

Take a uniformly random support $R\subseteq\{0,1\}^n$ of size $s_2=2^{\beta n}$ and let $f=1_R$. For sufficiently small fixed $\beta>0$, circuit counting shows that most such supports define functions of circuit complexity greater than $s_2$: there are about $2^{(1-\beta)ns_2}$ supports, compared with at most $2^{(C_0\beta+o(1))ns_2}$ circuits of size at most $s_2$.

For any fixed sample $S$ of at most $t=2^{10\beta n}$ points, its intersection with $R$ is hypergeometric. Set $r=\lfloor s_2/(4cC_dn^2)\rfloor$, where a DNF with $r$ exact minterms costs at most $C_d rn$ gates and the low threshold is $s_1=s_2/(cn)$. A tail bound gives $\Pr[|R\cap S|\ge r]\le 2^{-\Omega(s_2/n)}$. Consequently, any family of fewer than $2^{\eta s_2/n}$ candidate samples has a single sparse support meeting fewer than $r$ positive points in every sample. Counting ensures one such support is still hard; on each sample a small DNF listing its positive points agrees with the table. So no sample anti-checks it, and every valid selector must have at least $2^{\eta s_2/n}$ distinct outputs.

This is a quantitative range theorem, not a selector circuit lower bound. The output can encode $tn$ bits and the OPS sample length has $t=s_2^{10}$, much more than the theorem's necessary $\Omega(s_2/n^2)$ sample-point count. The computational challenge remains to choose a valid sample from the truth-table input. The related static Anti-Checker Hypothesis is already known to be false. This sparse argument independently recovers that refutation for every fixed $\lambda\in(0,1)$: with $s=2^{n^\lambda}$, the sparse-support count has logarithm $(1-o(1))ns$, while circuit descriptions contribute only $O(sn^\lambda)=o(ns)$. This matches the published parameter quantifier; it is distinct from OPS's $s=2^{\beta n}$ regime, which requires small fixed $\beta$. See C-18 and [Chen et al.](https://arxiv.org/abs/1911.08297).

## 2.69 Positive-point capture is necessary but computationally easy

The C-18 adversary gives a stronger local requirement. If $f=1_R$ is a high-complexity table with $|R|=s_2$, then any valid selector sample must contain at least $r=\Omega(s_2/n^2)$ points of $R$. Otherwise the DNF with an exact minterm for each sampled 1-point agrees with $f$ throughout that sample and remains within the low threshold $s_1$.

This requirement alone is easy to satisfy. Sort the $N$ records $(f(i),i)$ by their truth-table bit with a sorting network and output the first $t$ coordinate labels. The network uses $O(N\log^2N)$ compare-exchange operations, each implementable with $O(n)$ gates, so total size is $O(Nn^3)$. On every weight-$s_2$ table, since $t\ge s_2$, the output includes every positive coordinate. It need not anti-check the table: a small circuit may still match the selected zeros and ones. Therefore sparse-positive capture alone cannot give the selector circuit lower bound. The next argument must constrain the full label pattern, especially how selected zeros block every size-$s_1$ circuit. See C-19 and Idea 185.

## 2.70 Anti-checkers as instance-dependent transversals

For a fixed table $f$, each small circuit $D$ has an error set $E_D(f)=\{x:f(x)\ne D(x)\}$. A sample is an anti-checker exactly when it intersects every set in $\mathcal E_f=\{E_D(f):CC(D)\le s_1\}$. Patching $D$ at all error points shows $|E_D(f)|>(s_2-s_1)/(C_dn)$ whenever $CC(f)>s_2$.

The size of individual error sets does not explain the OPS short sample. There are $M_1=2^{O(s_1\log(n+s_1))}$ candidate circuits, and a union bound for a uniform random sample needs $m=O((N/\delta)\log M_1)$, where $\delta=\Omega(s_2/n)$ is the minimum error-set size. Since $\log M_1=O(\beta s_2)$, this generic argument gives $m=O(\beta nN)$, exceeding the universe size. It forgets the structure and dependence on $f$ that let the OPS construction choose only $t=s_2^{10}$ queries under its circuit assumption.

The resulting proof target is sharper in conceptual terms: show that computing a short transversal for the error sets of all small circuits, conditioned on the full high-complexity truth table, requires superlinear circuit size. C-18 forces the selector to have many possible transversals; C-19 shows positive-point capture alone is easy; C-20 explains why uniform sampling from minimum-distance information is too weak. The remaining obstacle is the structured placement of selected zeros and ones that defeats all low circuits simultaneously.

### 2.71 Anti-checkers are short equilibrium strategies; existence is not construction

For a fixed truth table $f$ and a class $\mathcal C_s$ of smaller circuits, form the zero-sum game with circuits as rows, domain points as columns, and payoff $1[D(x)\ne f(x)]$. The input player maximizes the least disagreement probability against a circuit. If every mixed circuit strategy had worst-case error below $1/2-\varepsilon$, sampling $O(n/\varepsilon^2)$ circuits and taking their majority would compute $f$ exactly: Hoeffding plus a union bound over all $2^n$ inputs makes the majority correct everywhere for some sample. Thus $CC(f)=\Omega(ns/\varepsilon^2)$ forces an input distribution under which every size-$s$ circuit errs with probability at least $1/2-\varepsilon$.

Now sample $O(\log|\mathcal C_s|/\varepsilon^2)=O(s\log(n+s)/\varepsilon^2)$ points from that distribution. Another Hoeffding bound, this time unioned over all circuits, gives a small multiset on which every such circuit errs on a constant fraction. This is the Lipton-Young anti-checker theorem. OPS's high threshold is a sufficiently large constant times $n$ times its low threshold, so the parameter shape agrees.

The important distinction is between a per-table equilibrium witness and a circuit that computes one from the truth table. The game proves that every hard table has a short anti-checker. It does not give a uniform way to find the equilibrium distribution, nor a small circuit for the map $f\mapsto Q_f$. OPS's constructive lemma addresses this second question conditionally using approximate counting under $NP\subseteq P/poly$. C-21 records the proof and the constant caveat.

### 2.72 Quantifier audit: anti-checker synthesis is a second-level search problem

For an explicit table $f$ and a proposed list $Q=(q_1,\ldots,q_r)$,
$$
\operatorname{AC}(f,Q)\equiv
\forall D\ (|D|\le s)\ \exists j\le r:\ D(q_j)\ne f(q_j).
$$
Its complement has a circuit $D$ as a polynomial-length witness, so verifying $\operatorname{AC}$ is coNP. Asking whether a prefix of $Q$ has any valid completion adds an outer existential quantifier and is in $\Sigma_2^P$. On the promise $CC(f)>S$ for which minimax guarantees some $Q$, $P=NP$ collapses PH to P and makes bit-by-bit search polynomial-time. This gives polynomial-size selectors, with no useful control on their degree.

OPS's conditional selector is quantitatively much sharper: under $NP\subseteq P/poly$, its size is $N^{1+O(\beta)}$. A lower bound excluding selectors of size $N^{1+\delta}$ for a fixed $\delta>0$ and all sufficiently small fixed $\beta$ would contradict that construction by choosing $\beta$ below $\delta$ divided by the unknown polynomial exponent constant. This is a sufficient route to $NP\not\subseteq P/poly$, not an independent proof of the needed lower bound. The first unresolved mathematics is quantitative synthesis against arbitrary circuits, not game-theoretic existence.

### 2.73 Sparse-support adversary: random supports admit a cheap anti-checker

The range lower bound C-18 suggested attacking the selector on weight-$s_2$ truth tables. A stronger adversarial check shows that uniformly random supports are actually easy for almost all instances. Choose a fixed set $Q_0$ of $O(\log M_1)$ points hitting the 1-set of every size-$s_1$ circuit whose 1-density exceeds $1/2$. Such a set exists by random sampling and a union bound.

For a uniformly random support $R$ of size $s_2$, the probability a size-$s_1$ circuit of density at most $1/2$ contains every point of $R$ is at most $2^{-s_2}$; unioning over $M_1=2^{O(\beta s_2/c)}$ circuits still gives $o(1)$ for small $\beta$. Also $R$ is disjoint from $Q_0$ with probability $1-o(1)$, and circuit counting shows $1_R$ has complexity greater than $s_2$ with probability $1-o(1)$. For any support with all three properties, $R\cup Q_0$ anti-checks every low circuit: one missing positive catches a circuit, while a circuit containing every positive must be dense and is caught by $Q_0$ at a zero.

The map that lists all positive coordinates and appends the fixed $Q_0$ is implementable by a sorting network of size $O(Nn^3)$ and fits within OPS's sample length. This is not a selector for all hard tables; it fails on exceptional supports contained in low-density circuit sets. It does show that a worst-case selector lower bound cannot rest on random sparse supports or on range size alone. The likely hard sparse instances are structured supports whose low-complexity supersets are sparse and must be located from the support.

### 2.74 Axis-aligned sparse regions are easy to recover too

Take a fixed axis-aligned subcube $A$ of size $a=2^{\lfloor10\beta n\rfloor}$, just within the OPS sample budget. Let $R$ be a random subset of $A$ of size $w=K s_2$, for a sufficiently large fixed $K$. The number of such supports has logarithm
$$
\log_2\binom{a}{w}\ge (9K\beta-o(1))ns_2.
$$
For $K$ larger than the circuit-counting constant divided by 9, almost every such $1_R$ has complexity above $s_2$. At the same time, the number of size-$s_1$ circuit restrictions to $A$ is only $2^{O(\beta s_2/c)}$, so almost no such low circuit agrees with $1_R$ on all of $A$.

With probability $1-o(1)$, every free coordinate of $A$ takes both values on $R$. Hence the smallest coordinate subcube containing the positive support is exactly $A$. A sorting circuit can find the positives, compute their coordinatewise AND/OR pattern, and output every point in the resulting hull in size $O(Nn^3)$. Since no low circuit agrees with $f$ throughout $A$, the hull is an anti-checker.

Thus even the natural hard sparse family inside a small low-circuit region is easy when the region has a simple hull recoverable from positives. The sparse-support route now needs a low-density circuit region that is not reconstructed by this kind of closure, together with a proof that every valid sample must encode its hidden structure. See C-24.

### 2.75 Frontier reset: isolate the exact work that remains

**Strongest local result.** The known minimax theorem gives a short constant-error anti-checker for each hard table; the new project lemma gives an explicit near-linear circuit for anti-checkers on almost every sparse support. Neither is a P-vs-NP lower bound.

**Primary dependency path.**
$$
P\ne NP
\ \Leftarrow\ NP\not\subseteq P/poly
\ \Leftarrow\ \text{OPS Gap-MCSP lower bound}
\ \Leftarrow\ \text{no near-linear anti-checker selector under OPS parameters}.
$$
The last implication is sufficient by OPS: if $NP\subseteq P/poly$, their approximate-counting construction gives selectors of size $N^{1+O(\beta)}$. The exact open target must quantify over every circuit with arbitrary sharing, negation, advice, and recomputation.

**Classification of the first unresolved statement.** It is not a missing technical lemma in the cover derivation. It is itself a major nonuniform circuit lower bound, and any selector lower bound strong enough for the magnification implication is known to force $NP\not\subseteq P/poly$. Thus the selector is a more semantic presentation of the target, not yet a reduction in difficulty.

**Alternative attacks that hit this node.**

1. **Hard-support synthesis.** Restrict to high-complexity sparse tables lying inside low-density small-circuit sets; prove that any anti-checker selector must locate their containing low circuits or pay superlinear size. The random-support candidate is falsified by C-23.
2. **Near-circuit geometry.** Uniform sampling can hit diffuse error sets; point-patching gives a lower distance floor, but leaves a wide band of small, highly structured error sets. Find a representation-independent theorem controlling this band.
3. **Feasible proof complexity.** Pich-Santhanam show feasible SAT anti-checkers plus a non-p-bounded Extended Frege system imply $P\ne NP$. This moves the burden to formalizable witness generation and EF lower bounds; it does not discharge either.
4. **Uniform distinguisher magnification.** Atserias-MÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ller (2025) derive $P\ne NP^{\oplus P}$ from a near-linear uniform-circuit lower bound for an approximation of MCSP. This avoids the nonuniform selector but does not currently imply $P\ne NP$.
5. **Self-reference/fixed points.** The existing patching descent only ends at complexity at most $s_2$, within the gap. A naive hope that every overwrite map has many fixed points is false: selecting the first 1 and overwriting it by 0 can leave the all-zero table as the unique fixed point.

**Choice.** Keep O-1 as the primary route because it is the weakest direct theorem with a proved path to the requested separation. Shift the selector subroute from generic random supports toward structured near-circuit exceptions. Do not spend more effort on existence, static sample families, or raw sample-range counts unless they give a circuit-size lower bound.

### 2.76 Relative density separates statistical hardness from region recovery

Let $A\subseteq X$ be a known region, $R$ a uniformly random $w$-subset of $A$, and $\mathcal C$ a family of $M$ candidate low circuits. Fix $0<\eta<1$. If
$$
M\eta^m=o(1),\qquad M(1-\eta)^w=o(1),\qquad wm/|A|=o(1),
$$
then a fixed $m$-point multiset $Q_A\subseteq A$ exists such that, with high probability over $R$, $R\cup Q_A$ anti-checks all of $\mathcal C$ against $1_R$. This is C-25. The proof is a two-density split: circuits with relative density at most $1-\eta$ are unlikely to contain all random positives; the fixed $Q_A$ hits every circuit with density above $1-\eta$; the overlap is negligible.

This generalizes C-23's whole-domain split. C-24 supplies one efficient way to recover a special $A$ (the coordinate hull of random positives in a subcube). The actual bottleneck is explicit: for a hidden region, statistical anti-checking is easy conditional on its identity, but we have no general theorem that a selector must recover that region, nor a circuit lower bound for doing so. The region may not be unique, and a selector could use a different sample altogether. Do not turn ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“the natural construction needs $A$ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â into ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“every construction needs $A$.ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â

**Research consequence.** Test regions with algebraic or combinatorial closures (affine subspaces, cosets, spans, matroid flats) where random positives may reveal a compact superset that is itself an anti-checker. A successful closure theorem would eliminate more structured sparse-support examples, but would still be only diagnostic unless it yields a worst-case selector lower bound or a reduction to one.

### 2.77 Affine regions are observable from random positives

C-26 makes one of the closure tests concrete. Let $A$ be any affine subspace of dimension $d=\lfloor10\beta n\rfloor$ in $\mathbb F_2^n$, and place $w=K2^{\beta n}$ random positives in it. For $K$ large enough, counting makes the resulting truth table harder than $s_2$, while the random points span $A$ with probability $1-o(1)$: failure puts them in one of at most $2^{d+1}$ affine hyperplanes, each hit with probability at most $2^{-w}$. Counting restrictions also shows that no size-$s_1$ circuit agrees with the sparse truth table throughout $A$. Therefore outputting all of $A$ anti-checks every low circuit. Gaussian elimination recovers the affine equations, and enumerating the points costs $O(Nn^3)$ circuit size; the list length is within $t$.

This subsumes coordinate subcubes as a support-region family and rules out affine subspaces/cosets as hard examples when the positives are random and numerous. It reinforces the ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“observable closureÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â diagnostic: random examples expose simple algebraic structure. It does **not** prove a general region-recovery theorem or a lower bound for arbitrary selectors. A hard instance could use a region with no efficiently computable closure, or a selector could avoid the region representation entirely.
### 2.78 The sparse-support problem is a version-space transversal

For $f=1_R$, every low circuit that rejects some positive is already refuted by querying $R$. The remaining circuits accept all of $R$; each has a residual extension set $E_D=D^{-1}(1)\setminus R$, consisting exactly of false positives. An additional query list anti-checks these circuits precisely when its zero-labeled queries hit every $E_D$. This exact equivalence is C-27.

This reframes C-25's known-region sample as a transversal construction: random positives rule out sparse residual extensions that contain all of $R$, and a region-relative sample hits the dense extensions. C-21's minimax argument gives a fractional transversal: a distribution on inputs places constant mass on every error set; sampling $O(\log|\mathcal C_s|)$ points yields an integral transversal. The theorem proves existence, not an efficient way to find the distribution or the sample from the truth table.

**Proof direction to investigate.** The primal problem is to find a small set of zero-labeled points hitting all circuit extensions of $R$. Its fractional relaxation asks for a distribution that gives every such extension constant mass. A dual distribution over circuits captures the failure of any proposed input distribution; the minimax contradiction says such a circuit mixture would compute $f$ too well. The unresolved step is a quantitative lower bound on synthesizing a transversal for all high-complexity tables, or a structural theorem that makes those transversals computable. Do not call the search NP-hard without a reduction, and do not infer that every selector must use the region-based construction.
### 2.79 Majority gives a local overlap constraint, not a selector

C-28 adds a direct consequence of circuit hardness. Take any odd $q$ low circuits that all accept the positive support $R$. If no outside point is accepted by a majority of them, their majority computes $1_R$ exactly. Thus, whenever $CC(1_R)$ exceeds $O(qs_1+q^2)$, every such $q$-tuple has a point lying in a strict majority of its residual extension sets. In the OPS scale, this applies to $q$ up to a constant fraction of $s_2/s_1=cn$.

This is a local packing condition on the version space. It does not directly produce a hitting set for the whole family: the majority point can depend on the chosen subfamily, and a bounded matching number does not generally bound a set system's transversal number. The computational question is how to identify useful subfamilies and their majority points without enumerating exponentially many candidate circuits. This gives a sharper search target, not a separation.
### 2.80 A majority-overlap property alone cannot shrink the transversal

A stress test prevents an overreach from C-28. Let the universe have size $m$ and take as hyperedges every set of size greater than $m/2$. In any $q$ selected edges the total incidence count is greater than $qm/2$, so some point belongs to a strict majority of them. This is exactly the strongest all-subfamilies majority-overlap conclusion, yet the minimum transversal has size $\lceil m/2\rceil$: every smaller set has a complement containing a strict-majority edge.

Therefore no abstract theorem from ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“every small subfamily has a majority pointÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â to ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“there is a tiny transversalÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â can work without extra assumptions. The residual error sets of circuits may have useful structure beyond this property, but that structure must be proved and exploited. This closes one tempting combinatorial shortcut.
### 2.81 Restriction recursion spends the same n-factor gap

Idea 197 tests a natural self-reduction. Split the $n$-bit domain into $B=2^k$ restrictions on $n-k$ variables. If each restriction has circuit size at most $u$, a multiplexer gives a circuit for $f$ of size $O(Bu+Bk)$. Hence $CC(f)>s_2$ forces only one restriction to have complexity about $s_2/B$.

A local anti-checker against size $s_1$ needs restriction complexity on the order of $(n-k)s_1$. Since $s_2=\Theta(ns_1)$, this permits only a constant number of blocks, depending on theorem constants. It cannot branch into a growing family of substantially smaller selector instances. A fixed-factor split may be possible if constants allow it, but it does not reduce the asymptotic problem. The naive restriction recursion is therefore not a route around the synthesis bottleneck.
### 2.82 Region size is not the obstacle when the region is known

C-29 combines the full-region and relative-density constructions into a size dichotomy. Fix a known region $A$ and put $w=K s_2$ random positives in it, with enough support entropy that $\binom{|A|}{w}\gg|\mathcal C_{s_2}|$.

- If $|A|\le t=s_2^{10}$, output all of $A$. Circuit counting says a random support is unlikely to match any size-$s_1$ circuit throughout the region, so this full-region sample is an anti-checker.
- If $|A|>t$, the region is much larger than $wm=O(s_2^2)$ for $m=O(\log|\mathcal C_{s_1}|)=O(s_2)$. C-25 supplies a fixed $Q_A$ hitting all circuits dense in $A$; random positives are unlikely to be contained in any sparse circuit. Output $R\cup Q_A$.

Both lists fit in the OPS length bound and are emitted with $O(Nn^3)$ circuit size for each fixed known $A$. The choice of circuit can hardwire information about $A$ and, in the large case, $Q_A$. This does not give a single selector for unknown regions. It does show that small-versus-large region size is not the obstacle: the remaining issue is finding a useful region from the truth table, or proving that such a region is irrelevant to every possible selector.
### 2.83 Learn a hidden region as a bounded-degree algebraic closure

C-30 extends the coordinate/affine hull idea using finite-field algebra. Map each point $x$ to its feature vector $\phi_d(x)$ of all squarefree monomials of degree at most a fixed $d$. The closure generated by positives $R$ is
$$
\operatorname{cl}_d(R)=\{x:\phi_d(x)\in\operatorname{span}_{\mathbb F_2}(\phi_d(R))\}.
$$
This identity follows by taking the orthogonal complement: the vectors orthogonal to the feature span are exactly the coefficients of degree-$d$ polynomials vanishing on every positive. If random positives span the feature space of a degree-$d$-closed region $A$, this closure recovers $A$ exactly.

A finite evaluation-code distance condition guarantees spanning. If every nonzero degree-$d$ polynomial restriction to $A$ is nonzero on at least a $\delta$ fraction, then the chance $w$ random positives fail to span is at most $2^L(1-\delta)^w$, where $L=\sum_{i\le d}\binom ni$. For fixed $d$ and constant $\delta$, $L$ is polynomial in $n$ while $w=2^{\beta n}$, so failure vanishes. Feature extraction, Gaussian elimination, and scanning the truth table to output the closure fit in $O(Nn^{O(d)})$ size.

This works, for example, for bounded-degree polynomial graph regions of sample-budget size: their defining equations make them degree-closed, and substitution bounds the restricted polynomial degree, giving constant relative distance. Counting makes sparse supports in such a region high-complexity and rules out low circuits agreeing throughout it; outputting the recovered region is then an anti-checker.

**Updated hard-instance filter.** A structured hidden region is not enough. It must evade cheap observable closures: coordinate hull, affine span, and now bounded-degree polynomial closure. This is a uniform selector for a promising structured family, not a worst-case result. The key unresolved question remains whether an arbitrary hard table admits a useful recoverable closure, or whether selectors can be lower-bounded without forcing them to use one.

### 2.84 A closure can fail while another statistic succeeds

C-31 is an adversarial check on C-30. Let $A$ be a Hamming ball of radius $k=\lfloor\rho n\rfloor$, choosing $\rho$ so $\beta<H_2(\rho)<10\beta$. It has enough support entropy for $w=K s_2$ random positives to produce a table harder than $s_2$, but $|A|<t$. The full ball anti-checks low circuits with high probability because almost no size-$s_1$ circuit agrees with the random sparse table throughout $A$.

For every fixed feature degree $d\le k$, the ball contains all weight-$\le d$ vectors, whose feature vectors form a triangular basis. Thus its degree-$d$ closure is the whole cube; random positives span this full feature space, so C-30's output is too large. Yet the same positives include a point on the boundary layer with probability $1-o(1)$. Their maximum Hamming weight recovers $k$, and the selector outputs the whole ball with $O(N\operatorname{poly}(n))$ size.

**Lesson.** No one closure should be mistaken for a universal explanation. Hamming balls defeat bounded-degree feature closure but are easy under the weight statistic. A credible hard-region candidate has to survive multiple independent observables, and that still would not prove every selector must reconstruct the region.
### 2.85 Fourier and matroid fingerprints expose secret product regions

C-32 tests a region with hidden linear coordinates. In transformed coordinates, take the product of blocks $B=\{0,e_1,\ldots,e_r\}$. Its membership circuit is tiny after the hidden linear map is hardwired, and its size can sit strictly between $s_2$ and the list budget. Fixed-degree polynomial closure fails on this family, but its Fourier spectrum reveals the hidden coordinates.

For uniform $z\in B$, the parity bias is $(r+1-2|u|)/(r+1)$. In a product of blocks, among nonzero frequencies the largest biases occur exactly at one-block frequencies of local weight one or $r$; every other coefficient is separated by a constant gap. The zero frequency is ignored. The truth-table Walsh transform estimates all coefficients at once. Thresholding finds the high-frequency vectors, and their minimal linear dependencies group them into the hidden blocks. Projecting the positive examples onto a basis of each group reveals the allowed local patterns. The selector reconstructs and outputs the whole region.

The calculation uses several ideas together: Fourier analysis for discovery, matroid circuits for grouping, and sample-based pattern recovery. It gives a near-linear selector for secret linear images of this product family. The research lesson is another adversarial filter: simple algebraic closure is not enough; spectral fingerprints and dependency structure may also reveal a region. This still does not imply that every arbitrary selector must recover a region.

### 2.86 Fourier-maximizer matroids give a general product-region test

C-33 abstracts the C-32 mechanism. For a fixed block alphabet $B\subseteq\mathbb F_2^r$, take the set S of nonzero parity frequencies attaining the largest absolute Fourier coefficient of the uniform distribution on B. In a product of many blocks, any multi-block frequency has coefficient at most the square of this maximum. If S spans each block and its binary matroid is connected, the global spectral peak set splits into connected components that are exactly the hidden blocks.

A selector can estimate the whole Walsh spectrum, recover those components, learn each block's allowed patterns from the positives, and output the region. C-32 is the explicit singleton-plus-zero block whose peak set is a single minimal-dependence circuit. The general criterion rules out many more fixed-alphabet product regions after an unknown linear change of basis.

**Next stress test.** Choose local alphabets whose Fourier-maximizer matroid is disconnected or fails to span, and inspect whether the next spectral levels recover the missing directions. Absence of this particular fingerprint is only a method-specific obstacle; it does not show the region or its anti-checker is hard to synthesize.

### 2.87 The universal bottleneck is now the routing complexity itself

The audit reset changes how this model allocates effort. The observable-region results C-24 through C-33 are useful adversarial filters, but accumulating more such families does not address the highest unresolved node. The direct target is the unrestricted promise classifier for Gap-MCSP: for one fixed $\epsilon>0$ and every sufficiently small fixed $\beta>0$, rule out size-$N^{1+\epsilon}$ circuit families at the OPS parameters. OPS show that this would imply $NP\not\subseteq P/poly$ and hence $P\ne NP$.

C-34 gives a universal selector fact. Any valid anti-checker selector must depend on $N-o(N)$ of the truth-table bits: otherwise fix all bits it reads to zero, let its output sample be $Q$, and complete a high-complexity table that is zero on both the read set and $Q$. The constant-zero circuit then passes the purported anti-checker. C-38 sharpens the gate conversion: in a fan-in-two circuit with $L$ output bits, connecting $E$ essential inputs to those outputs requires at least $E-L$ gates. With $E=N-o(N)$ and $L=tn=o(N)$, every selector needs $N-o(N)$ gates. This is a universal near-linear bound, still only linear; a shared circuit can aggregate all $N$ inputs in $O(N)$ gates.

This pinpoints a quantitative transition: **reading nearly all input bits is necessary but insufficient; the unresolved cost is choosing a short query list whose labels simultaneously defeat every small circuit.** Output-range size and positive capture do not charge that routing (C-17--C-20). Any next invariant must lower-bound the full map $f\mapsto Q_f$ without assuming region recovery, a preferred circuit architecture, or a representation of the selector.

Three independent alternatives remain, all with explicit unresolved cores: (i) prove the direct Gap-MCSP circuit lower bound; (ii) formalize a SAT-decider-to-proof-system transfer and prove the required Extended Frege lower bound; or (iii) build a polynomially verifiable diagonal SAT family whose self-reference has no tableau-size blowup. Current audits show no route has a smaller established open lemma than the first. Work is therefore focused on the direct quantitative selector/separator bottleneck; family-specific recovery work is secondary unless it produces a universal routing theorem.

Recent conditional literature on implicit MCSP and full-support learning combines subexponentially secure indistinguishability obfuscation with the nonexistence of optimal proof systems to obtain NP-hardness results. These assumptions can yield substantial meta-complexity consequences, but they do not provide an unconditional circuit lower bound for the OPS Gap-MCSP promise. This is a useful comparison point, not an active proof step.

### 2.88 A short linear sketch cannot route the anti-checker queries

C-35 quantifies the exceptional-input problem: any one fixed sample of $t=2^{10\beta n}$ positions is valid for all but a $2^{-t+O(2^{\beta n})}$ fraction of uniformly random tables. Random truth tables therefore give no worst-case selector lower bound; the unresolved inputs lie in cylinders where the sampled labels imitate a low circuit.

C-36 tests a natural compression escape: compute a short global linear sketch $Af$ and decode the query addresses from it. If the row space of $A$ has minimum distance greater than $t$, deleting the at most $t$ queried columns leaves rank $k$. For any fixed sketch value $h$, one can set every queried label to zero and still retain $2^{N-|Q_h|-k}$ completions. At OPS parameters this exceeds the number of tables of complexity at most $s_2$ whenever $k=o(N)$. One completion is high complexity, yet the selector returns $Q_h$ and the constant-zero circuit passes. This rules out robust affine-sketch architectures even when the decoder is computationally unrestricted.

The representation-independent form is a fiber-capacity condition: for every address value $q$ and every low-circuit trace $y$ on $q$, a valid selector's address fiber over $(q,y)$ must contain at most $M_2$ tables. A superlinear lower bound would need to show that small general circuits cannot arrange these fibers, despite nonlinear computation and feedback from the very bits they query. C-36 does not prove that statement. It sharpens the open question to **query-label feedback**: how must a selector couple its address choices to observed labels strongly enough to avoid a high-complexity completion?

**Adversarial checks.** (i) Robust linear global sketches fail by rank and completion. (ii) A fixed menu of samples fails when the union of its queried coordinates leaves more than $\log_2M_2$ free bits. (iii) A blanket fixed-point claim for one circuit is false: the toy address rule ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“query the first 1-bitÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â avoids an all-zero queried label on every nonzero table. Any fixed-point route must handle all low-circuit traces simultaneously, not just force agreement with the zero circuit.

**Next proof target.** Extend the fiber-capacity obstruction beyond affine sketches, or prove a circuit-size lower bound from it that survives arbitrary nonlinear selectors. A promising intermediate condition is a quantitative bound on how much fixing selected labels can shrink address-map fibers. The obstacle is that a selector can deliberately make its addresses depend on those labels; no general bound on this feedback is currently known.

### 2.90 The linear gate bound is tight for simple hypothesis classes

C-39 gives a concrete adversarial construction against an overextension of C-34/C-38. A fan-in-two priority encoder finds the first 1 in the truth table using $O(N)$ gates; a second encoder applied to the complement finds the first 0. The two queried labels disagree with both constant circuits for every nonconstant table, hence for every high-complexity table. This is not a selector against all size-$s_1$ circuits, but it proves that the constant-zero completion argument alone cannot force superlinear size.

The priority encoder uses a binary tree. Each node stores its nonempty flag and the first-one index in its block. Combining blocks costs $O(h)$ gates at height $h$, and summing $(N/2^h)O(h)$ over heights gives $O(N)$. Thus nonlinear query-label feedback is achievable at the near-$N$ scale. The remaining challenge is routing against all small circuits simultaneously, whose class size is $M_1=2^{O(s_1\log(s_1+n))}$.

**Refined target.** A lower-bound proof must exploit the joint constraints from many circuit traces at once. It cannot derive superlinear size from requiring one 1-witness, one 0-witness, or witnesses against a fixed finite set of constant-size circuits. It also cannot assume addresses are independent of the labels they sample, since the priority encoder couples them in linear size.

### 2.89 Audit formal claims by inspecting the axiom boundary

C-37 audits a June 2026 claim of Lean-verified $P=NP$ through membership in a pedigree polytope. The repository's final theorem is checked by Lean, but its central prerequisites are not derived there: `tardos_strongly_polynomial` is an axiom of type `QuickProtocol (LayeredPoint n)`; the MCF necessity direction is another axiom, with a backup development still containing 16 sorries; `An n` is declared to be `Unit`; and the transfer from membership to optimization and STSP is partly axiomatized. Thus ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“zero `sorry`sÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â does not mean the conclusion follows from the kernel alone: every axiom must be audited for whether it already contains the hard step.

There is also a general logical distinction: proving ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“if the proposed flow test accepts, then $X$ is in the polytopeÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â proves soundness of positive certificates, not a decision algorithm. A membership decider needs completeness too. The main Lean chain bypasses this by taking a quick membership protocol as an axiom. The claimed result therefore gives no accepted resolution and no P-vs-NP theorem for our project. Its useful lesson is procedural: follow the exact types and dependencies of formal assumptions, not their names or the build status.

### 2.91 The dual margin separates existence of anti-checkers from their synthesis

For a truth table $f$ and circuit class $\mathcal C_s$, define
\[
\Delta_s(f)=\max_{\mu\in\Delta(\{0,1\}^n)}\min_{D\in\mathcal C_s}\Pr_{x\sim\mu}[D(x)\ne f(x)].
\]
This is a representation-independent *anti-approximation margin*: it asks for the input distribution under which the best size-$s$ circuit still makes the largest unavoidable error. If $CC(f)>Cns$ for a suitable absolute $C$, finite minimax and majority amplification force $\Delta_s(f)\ge1/3$. Sampling $O(s\log(s+n))$ inputs from a maximizing distribution then gives a short list that disagrees with every size-$s$ circuit. This reconstructs the existence half of C-21, with constants to be matched separately to OPS.

The proof's quantifiers matter. Minimax gives $\exists\mu\;\forall D$ an error lower bound; it does not give a computable map $f\mapsto\mu_f$. For a rational candidate $\mu$, a violated constraint has a succinct witness: a size-$s$ circuit whose weighted disagreement is below $1/3$. Verifying that witness is in NP. Thus the direct ellipsoid route to the fractional certificate exposes a weighted circuit-fitting NP search. With an NP oracle, the ellipsoid method can find a feasible rational $\mu$, after which random sampling gives a promised-input $\mathrm{FBPP}^{\mathrm{NP}}$ selector with arbitrarily high success probability. It does not give an always-correct deterministic selector. For a fixed candidate list $Q$, validity is coNP; existentially finding a valid $Q$ is naturally a $\Sigma_2^P$ search relation. OPS's construction under $NP\subseteq P/poly$ uses a specialized iterative argument, so the quantifier count alone is not the construction.

The margin is not an independent hardness invariant: $\Delta_s(f)=0$ iff $CC(f)\le s$ (otherwise the uniform distribution gives every smaller circuit error at least $1/N$), while $CC(f)>Cns$ implies $\Delta_s(f)\ge1/3$. On the low-versus-high promise, distinguishing these two margin cases is Gap-MCSP at the same scale. This is useful as a *failure diagnosis*: the existence proof has already done all it can; the open work is constructive witness extraction without assuming a circuit/NP solver. Any proposed method to compute $\Delta_s$ or its witness must pass the circularity audit against O-1.

**Current model:** high circuit complexity implies a short dual certificate exists; the unresolved operator is $f\mapsto$ a valid certificate. The selector's output length is not the bottleneck. The bottleneck is finding a distribution whose support evades every low-circuit trace, especially on exceptional truth tables where a fixed sample trace is circuit-realizable.

### 2.92 Sparse supports defeat every small data-independent witness menu

C-41 sharpens the fixed-sample failure. Fix any menu of $m$ distributions $\mu_1,\ldots,\mu_m$ over the $N$ truth-table coordinates, where $m w/N=o(1)$ and $w=Kns=\Theta(N^\beta)$. A uniformly random $w$-point support has expected mass $w/N$ under each distribution. Markov plus a union bound shows at least half of supports have mass at most $2mw/N=o(1)$ under every menu member. Circuit counting says all but an $o(1)$ fraction of these supports have $CC(1_R)>Cns$ once $K$ is large. So there is a high-complexity sparse table on which every fixed-menu distribution has vanishing error against the zero circuit.

This proves that the witness distribution must depend on the full table, not just on a small menu chosen in advance. It does *not* rule out a circuit selecting among its possible outputs from the data: an OPS selector can have up to $2^{tn}$ address lists, vastly more than the menu sizes covered by C-41. The result therefore strengthens the adversarial test but leaves the nonlinear routing problem intact.

### 2.93 A new formal language needs a proved bridge back to standard resources

C-42 records an August 2026 Loop-theoretic manuscript. Its abstract describes internal complexity classes and explicitly makes the classical separation depend on a finite-transition capacity principle plus Loop-to-complexity bridge axioms. This raises the right audit questions for any ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“new languageÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â approach: what exactly is the internal time/space measure; how is a standard verifier represented; and which theorem translates an internal lower bound into a lower bound for every ordinary polynomial-time Turing machine?

The abstract-level conclusion is conditional, not an assumption-free classical proof. The SSRN PDF was unavailable to inspect in this session (403 response), so we do not infer that the bridge axioms are false or circular; their exact types remain unverified. The route becomes useful only if the axioms are proved from ordinary computation with polynomial resource preservation. A new vocabulary can expose an invariant, but the translation theorem carries the P-vs-NP force.

### 2.94 Quantifier collapse and circuit resources are different layers

C-44 formalizes a useful stress test. For an explicit truth table $f$, asking for a short list $Q$ that disagrees with every small circuit has the form $\exists Q\,\forall D\,R(f,Q,D)$, with a polynomial-time matrix. It is therefore a $\Sigma_2^P$ search relation. C-40 supplies existence on high-complexity tables. If $P=NP$, then $PH=P$, so prefix self-reduction finds a valid list in polynomial time in $N=2^n$ and hence yields polynomial-size circuits.

The exponent is the point: the generic collapse gives $N^{O(1)}$, not the $N^{1+\epsilon}$ bound at which OPS magnification yields $NP\not\subseteq P/poly$. By contraposition, OPS gives that near-linear nonuniform upper bound for an appropriate small-$\beta$ choice under $NP\subseteq P/poly$; the generic search argument is weaker and does not prove a contradiction. Thus decision-theoretic equivalence does not itself control the physical cost of routing through a length-$N$ truth table.

### 2.95 KPT witness dependence is a real interface, not notation

PichÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSanthanam Theorem 7 requires one $S^1_2$-provably correct generator. With only existential anti-checker data, KPT yields a fixed number of adaptive functions. A later function may depend on an earlier satisfying assignment. Replacing that assignment by the output of a conjectured SAT solver is semantically valid only if the solver is correct; formalizing the resulting selector still needs a proof of that correctness. Enumerating all $n$-bit assignments is an exponential generic flattening, not a polynomial solution.

This identifies the exact proof-theoretic target: a polynomial-overhead transcript composition or witness-independent invariant, plus EF non-p-boundedness. Neither follows from minimax existence, $P=NP$ as a standard-model claim, nor the KPT theorem alone. The direct O-1 Gap-MCSP lower bound remains the primary route because its first unresolved node is explicit and it avoids adding an independent EF hypothesis.

### 2.96 The anti-checker is a transversal of the residual circuit version space

For each size-$s$ circuit $D$, let $E_D(f)=\{x:D(x)\ne f(x)\}$. After querying $Q$, the surviving version space is $V_f(Q)=\{D:E_D(f)\cap Q=\emptyset\}$. The selector succeeds exactly when $V_f(Q)=\emptyset$. This is a precise shift from ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“produce a listÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â to ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“hit every disagreement set.ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â

On a high-complexity table, the elementary loop ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“find any surviving circuit, then add one mismatchÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â terminates, but only after at most $|\mathcal C_s|=2^{O(s\log s)}$ rounds. C-40's margin supplies $\mu$ with $\mu(E_D)\ge\gamma$ for every circuit. Let $\Psi(Q)=|V_f(Q)|$. Then
\[
\mathbb E_{x\sim\mu}\Psi(Q\cup\{x\})=\sum_{D\in V_f(Q)}(1-\mu(E_D))\le(1-\gamma)\Psi(Q).
\]
Some query therefore removes at least a $\gamma$ fraction of all surviving circuits. Choosing such points successively proves deterministically that a transversal of $O(\gamma^{-1}\log|\mathcal C_s|)$ points exists; random sampling gives the same order.

A natural deterministic selection rule maximizes the number of surviving circuit descriptions that disagree at a point. Computing that score is a #P-style counting task for this representation. This identifies a concrete route, not a barrier theorem: no reduction proves such counting is necessary, and no counting lower bound here follows from P vs NP alone. The active constructive question is whether circuit-specific structure can find a short transversal without enumerating or counting the exponentially large residual class. A successful lower-bound route must show why every small circuit fails at this routing task, rather than assume it.

**Learning-theory check (C-46).** Teaching-set research offers a close structural analogy, but the verified greedy lower bound is not an obstacle to C-45's query count: its $\Omega(\log|\mathcal C|)$ one-point example matches the $O(\log|\mathcal C_s|)$ bound obtained from constant dual margin. More importantly, C-45 proves a constant-fraction query exists for every residual version space. The bottleneck is computing such a query for circuit hypotheses, not the combinatorial number of rounds. The teaching-set paper has different target quantifiers and gives no circuit-specific computational lower bound. Use it as context, not as a barrier or proof bridge.

### 2.97 The dual-margin selector has a direct #P-oracle implementation

C-47 converts the potential into an explicit algorithm. Maintain $Q$ and count the circuit descriptions still agreeing with $f$ on $Q$. For every possible next input $x$, count how many survivors disagree at $x$. The C-40 distribution implies that the average of this count under $\mu_f$ is at least $\gamma$ times the number of survivors, so a maximizer removes at least a $\gamma$ fraction. After $O(\gamma^{-1}s\log(s+n))$ steps, no small circuit survives.

These counts are #P functions of the current query list and labels, so the method is a deterministic $\mathrm{FP}^{\#P}$ selector with polynomially many oracle calls (at the OPS scale, $O(Ns\log s)$). It exposes a concrete resource conversion: the existential short list becomes a constructive greedy list if exact residual counts are available. This is not an ordinary polynomial-time circuit construction; P vs NP does not collapse #P counting to P. C-48 below sharpens this baseline: relative approximate scores recover the conditional selector under $NP\subseteq P/poly$. Neither exact nor approximate score computation is known to be necessary for arbitrary selectors.

### 2.98 Approximate scores recover the conditional near-linear selector

The exact #P oracle in 2.97 is stronger than the contraction argument needs. For a transcript $\tau=((q_i,b_i))$, a candidate $x$, and the observed bit $b=f(x)$, count the size-$s$ circuit descriptions that match $\tau$ and disagree with $b$ at $x$. This is a #P quantity on the *transcript*, whose length after $K=O(s\log(s+n))$ rounds is only $O(Kn)=O(sn^2)$.

Stockmeyer's approximate-counting procedure gives relative approximations using BPP$^{NP}$. If $NP\subseteq P/poly$, then these local procedures have polynomial-size deterministic circuits on every fixed transcript length: replace NP queries by their advice circuits, amplify error below $2^{-m-2}$ for $m$-bit inputs, and fix random bits that work simultaneously on all inputs. Zero counts can be detected exactly by an NP query. This works because the conditional upper-bound assumption supplies the local circuits; it does not provide them unconditionally.

The dual margin gives $\max_x G_{\tau,x}\ge\gamma Z_\tau$. A constant-factor approximation to every score, followed by taking the largest estimate, still removes a constant fraction of the current version space. There are $N$ candidate addresses per round and $K=N^{\beta+o(1)}$ rounds. The local score circuits have size polynomial in $m=N^{\beta+o(1)}$, while selecting an address and reading its truth-table bit cost $O(N\operatorname{poly}(m))$ per round. For a fixed polynomial degree $a$ of the local circuits, the unrolled selector has size $N^{1+(a+1)\beta+o(1)}=N^{1+O(\beta)}$. Its list length $Kn=O(N^\beta n)$ fits the OPS budget for small fixed $\beta$.

This reconstructs the conditional OPS anti-checker mechanism from the version-space potential. It does not give a new lower bound, does not prove $NP\subseteq P/poly$, and does not show that an arbitrary small selector must compute these scores. The proof programme must target the universal puncturing-certificate function directly unless such a necessity reduction is actually established.

### 2.99 Reset: the actual unknown is the arbitrary-selector routing lower bound

The shortest dependency chain still begins with O-1, the slightly-superlinear circuit lower bound for the exact Gap-MCSP promise. The first unresolved statement is not the existence of short samples, a useful dual distribution, or a greedy contraction point; all three exist. The hard statement is that *every* ordinary circuit mapping each high-complexity truth table to a short separating coordinate set must have superlinear size.

Coding language helps state the problem cleanly. The set of small-circuit truth tables is a nonlinear code in $\{0,1\}^N$. For a high table $f$, the output $Q_f$ must puncture the code so that $f|_{Q_f}$ is outside the code's projection on those coordinates. Fiber capacity and essential-input dependence are necessary conditions, but current arguments give only $N-o(N)$ gates. An arbitrary selector may use a completely different computation from greedy version-space scoring, so lower-bounding that score alone would not suffice.

Alternative attacks remain separate: (i) direct circuit lower bounds for this puncturing-certificate map; (ii) diagonalization with a single NP verifier exponent, where prior constructions fail to keep the diagonal language in NP; and (iii) the Pich--Santhanam route, which still needs an $S^1_2$-provable generator and EF not p-bounded. None currently supplies the O-1 theorem. Do not call this a breakthrough: it is a sharper accounting of where the conditional construction lives and where the unconditional proof still stops.

### 2.100 Robust puncturing certificates and the correction-cost invariant

Let $Q_f$ be an anti-checker for a truth table $f$ against circuits of size $s_1$. A circuit can be patched at any one truth-table point with $O(n)$ gates by adding a minterm indicator; patching $r$ points costs $O(nr)$. Therefore $f|_{Q_f}$ cannot be within fewer than $\Omega(s_1/n)$ labels of the trace of any circuit of size $s_1/2$, or that circuit could be patched to agree on the whole query set and contradict anti-checking. For a minimax-length list of $O(s_1\log s_1)$ points, this gives relative trace distance $\Omega(1/n^2)$. The OPS selector interface allows up to $2^{10\beta n}$ points, however; with $q$ selected points the general relative bound is only $\Omega(s_1/(nq))$. The same correction argument says every OPS high table is globally $\Omega(s_2/n)$-far from every size-$s_1$ circuit.

This is a representation-independent necessary property of every valid selector, including nonlinear selectors with feedback; it is not sufficient, since a trace can be far from every size-$s_1/2$ circuit and still be realized by a size-$s_1$ circuit. It changes the certificate model from mere nonmembership in a punctured circuit code to robust separation from a smaller circuit class. A sparse distinguisher can amplify that separation once $Q_f$ is known, but does not compute $Q_f$ or lower-bound its routing circuit. The primary open node O-1 remains unchanged.

The 2025 general-magnification check does not close the gap: at fixed $\beta$, the generic count for MCSP YES tables is $2^{O(N^\beta)}$, not the $2^{N^{o(1)}}$ sparsity required by the general formula theorem. The paper's uniform MCSP theorem says that a specified lower bound for P-uniform approximate-MCSP circuits would imply $P != NP^{oplus P}$, not $P != NP$; a formula lower bound also does not exclude polynomial-size circuits for NP. Keep this as a certificate refinement and a closed bridge attempt, not a claimed separation.

### 2.101 Majority closure forces overlap among low-circuit disagreement sets

For high $f$ and any odd tuple $D_1,\ldots,D_k$ of circuits of size at most $s_1$, the pointwise majority $M$ has size $O(k s_1+k^2)$. Let $E_i=\{x:D_i(x)\ne f(x)\}$ and let $H$ be the set of points lying in at least $(k+1)/2$ of the $E_i$. The majority differs from $f$ exactly on $H$. If $H$ were too small, patching the majority on $H$ would give a circuit for $f$ of size at most $s_2$, contradicting hardness. For OPS parameters and odd $k\le\kappa n$ (small enough constant $\kappa$), this forces $|H|=\Omega(s_2/n)=\Omega(N^\beta/n)$. For $3\le k\le\kappa n$, counting pair incidences inside $H$ shows some pair among the tuple has an error-set intersection of this order.

This extends the support-specific majority-overlap fact in C-28. It defeats a tempting SAT encoding in which a constant number of low circuits have almost-disjoint error regions and a single hidden marker is the only way to hit all of them: the majority of those circuits would compute the high table except at the marker, and one minterm patch would contradict high complexity. The result does not imply a short transversal. Indeed, the arbitrary family of all subsets larger than half the universe has majority-error regions larger than $N/(k+1)$ for every odd k-tuple, stronger than the circuit-derived $N^\beta/n$ bound when $k=O(n)$, while its transversal number is about $N/2$. Thus incidence and majority-region bounds alone cannot do the job; the open mathematical task is to exploit circuit-specific overlap geometry to locate a transversal for exponentially many disagreement sets.

### 2.102 Global heavy-overlap graph and its limit

For a high table f, define one vertex for each distinct function computed by a circuit of size at most s1, and join two vertices when their error sets against f intersect in at least Omega(N^beta/n) points. C-50 applied to every triple says every triple contains such an edge. The non-edge graph is triangle-free, so Mantel's theorem forces a constant fraction of all pairs to be heavy-overlap pairs. The statement is semantic over circuit functions and remains valid under arbitrary circuit sharing and negation.

In any residual family of m candidate circuits, pair-coordinate incidence yields a point wrong for at least Omega(m*sqrt(N^beta/(N*n))) members. An ideal max-score process over distinct functions gives only a weak contraction and a query bound worse than C-40's minimax list. This is an existential count: counting distinct functions may be harder than counting syntactic descriptions, and no efficient point selector follows. The graph is global, but its edges do not reveal a common coordinate or an efficient way to find a transversal. A common-core toy model makes the limitation explicit: many distinct hypotheses can all err on a fixed set S, so every majority-error region contains S and every pair has maximal overlap, while querying one known point of S is a constant-size selector. The mathematical problem is to use the full circuit class on actual high-complexity tables, not overlap density alone.

**Moment caution.** If p_x is the fraction of low circuits wrong at x, the k-majority estimate gives sum_x p_x^r >= h/2^k. This is not a lower bound of order N on sum_x p_x: the power-mean inequality has the opposite direction, and a vector supported on h coordinates can satisfy the moment bound. The only immediate maximum-coordinate estimate is weaker than the constant-fraction point already implied by C-40's dual margin. Do not infer average circuit distance from this moment inequality.

### 2.103 Implicit hardness does not yet give explicit hard tables

Recent learning and implicit-MCSP work is useful for seeing how cryptography, proof complexity, and learning reductions can create hard sampler-described objects. The 2025 GoldbergÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œKabanets paper proves NP-hardness for a semi-proper circuit-learning problem and relates CGL hardness to witness encryption; the 2026 GoldbergÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œJuvekarÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œKabanets paper gives conditional hardness for gap ImpMCSP under iO and proof-system assumptions. These are not direct lower bounds for the explicit OPS promise.

The exact missing conversion is label extraction plus size preservation. Full support says each input has some sampler preimage; it does not supply an efficient method to find one and recover its unique label. Materializing a truth table on n-bit inputs also costs 2^n output bits. A proof that changes the representation must keep the source reduction polynomial, the truth-table size appropriate to OPS, and the circuit gap intact. Until such a theorem is supplied, implicit hardness remains an adjacent route, not an O-1 proof.

### 2.104 Root profile versus conditional tail

At the exact OPS ratio, minimax gives every high table a dual margin of at least 3/10: otherwise a majority of the smallest odd number k>=9n of low circuits would compute it with (0.9+o(1))s2<s2 gates. Averaging over the uniform fixed-length description prior implies a coordinate where at least 3/10 of descriptions are wrong.

An O(n)-sample approximates all N coordinate marginals to error 3/40. Hardwire the N frequencies and maximize empirical disagreement to get an O(Nn)-gate circuit that finds, for every high f, a point wrong on at least 3/20 of descriptions. The first contraction has a compact global profile; it is not the difficult step.

For each transcript, the same margin applies to its conditional survivor set. But a global sample may miss rare survivors, so empirical emptiness is not an anti-checker certificate. Separate (i) cheap root marginals, (ii) conditional profile reconstruction, and (iii) final exact elimination. Only (i) is resolved. The adaptive tail remains open, without implying every selector must use this architecture. See [C-52 report](research/C52_FIRST_QUERY_AND_ADAPTIVE_SAMPLING.md).


### 2.105 Relative sampling pushes the greedy process farther

For the finite family of transcript residuals and one-step disagreement events, multiplicative Chernoff bounds yield an all-ranges sample of size $O((kn+\log(1/\eta))/(\gamma\rho))$ that preserves constant-fraction contraction whenever the residual description mass is at least $\rho$. The proof thresholds disagreement-event masses at $\lambda=\gamma\rho/8$: events above the threshold receive relative error at most $1/4$, while smaller events have empirical mass below $2\lambda$. A true good coordinate has mass at least $\gamma r$ in a residual of mass $r$, so an empirical maximizer must remove at least $\gamma r/2$.

This improves the additive Hoeffding estimate by one factor of $1/\rho$. A polynomial-size sample can follow the process through inverse-polynomial survivor mass. But each contraction reduces mass geometrically; after $O(\log(1/\rho))$ steps it can enter the untracked tail. Reaching exact emptiness by this method requires tracking down to $1/|\mathcal H|$, so the generic sample scales with the full description count. This identifies the precise tradeoff for the sampled-greedy architecture, not a lower bound on other selectors.

**Update to the model.** The root profile is cheap; the adaptive profile remains sampleable at an improved inverse-mass rate; exact tail certification is still the bottleneck. Any new idea should beat that final description-count dependence or avoid maintaining a residual version space.


### 2.106 Interpolation pins down the sampled-greedy handoff

For any consistent transcript of $q$ queried points, OR the minterms corresponding to its positive labels. This DNF matches every label and uses $O(qn)$ gates. Hence all transcripts of $O(n)$ points still admit a size-$s_1$ completion for fixed OPS $\beta$ and large $n$.

C-53's relative sample with threshold $\rho=N^{-a}$ preserves constant-fraction contraction for $O(\log(1/\rho))=O(n)$ rounds, after which the residual mass is below $\rho$. By that time the DNF interpolant still exists, so the sample method's guarantee ends at a nonempty residual. With a sample of $O(n^2N^a)$ descriptions, direct unrolling costs $N^{1+a}\operatorname{poly}(n)$ gates. This is a real near-linear prefix construction and a real nonempty-tail stress test, but it leaves a gap to the necessary $\Omega(s_1/n)$ query length and proves nothing about other selector architectures.

The new obligation is to continue after this handoff: condition on rare residuals without a description-sized sample, or find a different potential whose progress does not collapse with uniform survivor mass.


### 2.107 Pointwise witnesses versus a circuit selector

The minimax margin is valid after every conditioning: for every nonempty residual set of low circuits and every distribution supported on it, some coordinate has disagreement probability at least $3/10$. Choosing the uniform distribution on the residual and repeating gives an existential anti-checker of $O(\log|\mathcal C_{s_1}|)$ queries. This proves $\forall f\in F_n\,\exists Q\,R_n(f,Q)$.

The required selector statement has different quantifiers: there must be one circuit family $S_n$ of size $N^{1+\epsilon}$, outputting at most the OPS budget $t_n=2^{10\beta n}$ points, such that every high table $f$ satisfies $R_n(f,S_n(f))$. The relation $R_n$ is coNP-checkable because a low circuit agreeing on the whole list witnesses failure. Pointwise existence does not construct a small circuit Skolem function. This is the central logic-level distinction: the list is short, but its dependence on the entire truth table is the unresolved computational content.

C-52's cheap root profile and C-53's relative sample do not close that gap. C-54 shows the latter loses its guarantee at a nonempty residual, while arbitrary selectors may bypass sampling and greedy scoring. Therefore do not turn a method-specific tail failure into an architecture-independent lower bound. The active target is now explicit: construct the near-linear uniformizer for $R_n$, or lower-bound every such uniformizer; otherwise attack O-1 directly. Full statement and proof: [O-1 selector Skolemization audit](research/O1_SELECTOR_SKOLEMIZATION_AUDIT.md).


### 2.108 A valid list serves a full trace cylinder

For a fixed list $Q$, let $T_Q$ be the restrictions to $Q$ of all size-$s_1$ circuits. Then $Q$ is a valid anti-checker for $f$ exactly when $f|_Q\notin T_Q$. This condition ignores every truth-table bit outside $Q$. Therefore, once a trace is anti-realizable by low circuits, all $2^{N-|Q|}$ extensions share the same valid list. Since there are only $2^{O(s_2\log(n+s_2))}$ size-$s_2$ functions, when $|Q|+\!O(s_2\log(s_2+n))=o(N)$ almost all those extensions are high-complexity tables.

This defeats a tempting information-counting argument: a short anti-checker output need not identify its input table and may be valid on an enormous cylinder. It does not give one fixed list for all high tables; the challenge is still routing each input to a trace outside $T_Q$. See C-56 and the selector audit. The output's short length cannot stand in for a circuit lower bound.

For a fixed $Q$, the exact fraction of all tables it anti-checks is $1-|T_Q|/2^{|Q|}$. A list longer than $\log_2|\mathcal C_{s_1}|$ by a growing additive term works for almost every random table. But its all-zero trace remains realizable by the constant-zero circuit, and when $|Q|+\log_2M_2=o(N)$ that failing trace has high-complexity extensions. This is why average-case success of a fixed list says nothing about the worst-case selector task.


### 2.109 External teaching-set lens

For a target $f$ outside a hypothesis class $\mathcal C$, call $Q$ an external teaching set if $f|_Q$ is not the restriction of any $D\in\mathcal C$. This is exactly an anti-checker against $\mathcal C$. For $\mathcal C_{s_1}$ and $CC(f)>s_2$, the established bounds are

$$
\Omega(s_1/n)\le \operatorname{ETD}_{\mathcal C_{s_1}}(f)
\le O(\log|\mathcal C_{s_1}|)=O(s_1\log(s_1+n)).
$$

The lower bound is local patching (C-49); the upper bound is conditional minimax contraction (C-55). These bounds concern sample length. They do not bound the circuit size of the map selecting a sample from $f$. Treat computational hardness of minimizing ordinary teaching sets only as a lead: our targets lie outside the class, lists need not be minimum, and the class is succinct. A reduction to this selector task must prove all of those details.

**VC-dimension stress test.** For $|X|=m$, the class $\{X\setminus\{i\}:i\in X\}$ has VC dimension 1, but the outside target $f\equiv1$ needs all $m$ points before no class member matches its trace. So VC dimension alone cannot supply a small external teaching set. The short OPS list uses the stronger circuit-majority minimax margin; the outstanding problem is computing a witness, not invoking a generic VC bound.

### 2.110 All-valid-output reductions have a patch-switch test

Two small-circuit approximants for a table, each correct outside its own disjoint, easy-recognizable region, can be switched to compute the table in 2s1+poly(n) gates. Since the high threshold is s2=Theta(ns1), this contradicts high complexity. This rules out a natural gadget in which omitting one source bit leaves only its own simple address block incorrect.

There is a separate common-witness trap: if a payload patch misses one valid anti-checker Q0, then Q0 remains valid on every patched table. The reverse implication is false under a length bound: a short transversal can be forced through a region without any disagreement set lying inside it; edges {p,x_i} give the counterexample. Future reductions must invalidate common lists and avoid both easy-region switching and this bounded-transversal quantifier error. These are method-specific barriers, not a lower bound for arbitrary selectors.

### 2.111 Kannan's exponent is not automatically preserved

Kannan supplies a different second-level language for each fixed circuit exponent k. A reduction maps x to a high table f_x and uses a decoder B(x,Q,f_x|_Q) that is correct for every valid selector output Q. If the table length is m^a_k, selector composition contributes exponent a_k(1+epsilon); table-generation and output-decoder circuits add exponents b_k and d_k. The composed exponent is at most e_k=max{a_k(1+epsilon),b_k,d_k}, up to lower-order factors. Contradiction requires k>e_k, plus the high-table promise and all-output correctness. The selector relation's second-level quantifier pattern does not provide these bridges.

### 2.112 The universal selector lower bound as adversarial completion

For a proposed list circuit S and table f, failure of validity is exactly:

$$
CC(f)>s_2\quad\land\quad
\exists D\in\mathcal C_{s_1}\;\forall x\in S(f),\ D(x)=f(x).
$$

So a direct lower bound can be pursued as a completion theorem: given any size-$N^{1+\delta}$ S, construct a high table f and a low circuit D whose truth table agrees with f on the selector's own output list. This is the precise self-consistency target; it must not be mistaken for a proof that such a completion exists.

C-34 establishes it when S leaves more than $t_n+\log_2 M_2+O(1)$ table coordinates unread: fix the read coordinates to zero, read the resulting list, then complete a high table that is also zero there while D is the zero circuit. C-38 converts the resulting essential-input bound to a linear gate bound. Once S can depend on every coordinate, that construction becomes circular. C-39 shows why merely choosing D to be a constant is insufficient: a priority encoder can query both labels. The unresolved step is to construct a nonconstant small D while respecting the address feedback of an arbitrary S.

### 2.113 Mandatory query regions consume dual mass

Fix a high table f and a dual distribution nu on input coordinates such that every low circuit D has error mass at least gamma=3/10. Call P mandatory if every valid anti-checker list of at most t points intersects P. Let M1 count the low-circuit functions and alpha=ln(M1)/t.

If p=nu(P)<gamma, conditioning nu on the complement leaves each low circuit's error probability at least (gamma-p)/(1-p). A random list of t points from that conditional distribution hits all M1 error sets whenever

$$
t(gamma-p)/(1-p)>ln(M1).
$$

Therefore mandatory status forces p >= (gamma-alpha)/(1-alpha). For OPS, alpha=O(N^(-9 beta))=o(1), so each mandatory region has mass 0.3-o(1). At most three pairwise-disjoint mandatory regions can exist for the same high table. This closes a reduction pattern that tries to encode many source bits by forcing every valid list through a separate disjoint address block.

This does not lower-bound an arbitrary selector: information may be encoded in a large list within one region, overlapping regions, or correlations among query addresses. Full proof: C-61 in the claim ledger.

**Fractional extension.** If the mandatory regions have fractional packing weights w_P with pointwise overlap at most one, then sum_P w_P <= 1/(0.3-o(1)) = 10/3+o(1). Thus the obstruction covers bounded-overlap families as well as disjoint blocks. It still does not constrain highly overlapping encodings or arbitrary correlations across the list.
**Common-witness form.** If a patch region P has nu-mass below (gamma-alpha)/(1-alpha), there exists one valid anti-checker list Q outside P. Every table that agrees with the base f outside P has the same labeled trace on Q, so this witness works across the entire patch family. A decoder that receives only Q and those labels cannot recover different source answers. Therefore a useful local encoding must alter at least about 3/10 of the base table's dual mass, not merely many raw truth-table bits.

### 2.114 Dual-mass separation for output-only decoding

For high tables f and g, let P be the set of addresses where they differ. If either dual witness assigns P mass below p*=(gamma-alpha)/(1-alpha), then one can sample a list outside P that anti-checks both tables with the same labels. Hence their valid labeled-list sets intersect.

An output-only decoder that must assign different source answers to f and g therefore requires both nu_f(P)>=p* and nu_g(P)>=p*. This is a directed dual-mass metric condition on reductions. A standard decoder may also receive the source input x; then this argument does not decide the answer, and the decoder's circuit exponent must be charged explicitly. C-62 proves the condition and its scope.

### 2.115 Agreement fibers: exact form of the selector bottleneck

For a candidate table-dependent anti-checker S and low circuit D, define the self-indexed agreement fiber \(A_D^S=\{f:f|_{S(f)}=D|_{S(f)}\}\). S succeeds on every high table precisely when all these fibers contain only tables of complexity at most s2. So the direct adversarial attack is to find one low D whose agreement fiber contains a high table.

This reformulation is exact but does not create a lower bound. A priority selector for the two-constant concept class has agreement fibers consisting only of the constants, demonstrating that list length, class size, and margin alone cannot force a hard member. The full circuit class must contribute a new extension or closure theorem that survives input-dependent address feedback. No such theorem is established. C-63 records the proof, circuit-cost audit, and toy counterexample.
### 2.116 The adversary must range over the whole low-circuit class

For one fixed low table D, a linear-size priority encoder finds the first truth-table coordinate where f differs from D. For a menu of m fixed low tables, the selector can output one mismatch coordinate per table at O(mN) gate cost. This does not defeat the OPS selector problem because the low-circuit class is exponentially larger and the selected query list must hit the error set of every member simultaneously.

The lesson for C-63 is a quantifier requirement: the hard D cannot be fixed before the candidate selector or reduced to a small fixed menu. The proof must use the full representation-rich class and the interaction among its many disagreement sets. C-64 proves the fixed-menu bound; it does not establish a lower bound for the full class.
### 2.117 Quantifier alignment for the selector separation route

OPS Lemma 4.1 supplies an anti-checker selector of size \(N^{1+k\beta}\) under \(NP\subseteq P/poly\), for every sufficiently small fixed beta, where k is fixed by the assumed polynomial circuit exponent. Therefore a selector lower bound at one beta chosen in advance may miss the beta needed to beat k. A sufficient theorem is: there exist delta,beta0>0 such that for every fixed beta in (0,beta0), every valid selector family with budget \(N^{10\beta}\) has size greater than \(N^{1+\delta}\) infinitely often. Choose beta after k, also below 1/10 so the query budget is sublinear, to get the contradiction. C-65 proves this implication and its beta quantifier is now the target standard.

An independent public Lean workbench also records the selector-fiber equivalence, the linear input-support ceiling, and the failure of additive per-anchor sensitivity because gates are shared. Treat these as audited obstructions, not novel lower bounds; the next candidate must measure promise-specific shared computation beyond coordinate support. See [the external audit](research/EXTERNAL_SELECTOR_AUDIT_2026-09-25.md).
### 2.118 Short-list selectors are a sufficient lower-bound target

C-48's conditional selector uses only \(K_n=O(s_1\log(s_1+n))=N^{\beta+o(1)}\) query addresses under \(NP\subseteq P/poly\), rather than the OPS allowance \(2^{10\beta n}\). Thus a circuit lower bound for every valid selector with this shorter output, for every sufficiently small beta in an interval, would still contradict the conditional construction and separate NP from P (C-66). The interval is needed to choose beta after the assumed P/poly exponent is known.

These shorter certificates also inherit C-49's relative trace distance \(\Omega(1/n^2)\) from circuits of size \(s_1/2\). That is a stronger local robustness guarantee, not yet a gate lower bound for the map selecting the list. Choosing C0 large also makes alpha=ln(M1)/K_n<1/15, so the C-61 argument still limits disjoint mandatory regions to three at this shorter budget. The active research question is whether this promise-specific trace geometry forces a non-coordinate shared-computation cost beyond the linear input-support bound.

### 2.119 Adaptive fusion closure as a least-fixed-point game

The active fusion route has an exact state representation. For a semantic rule list \(Q=((E_i,H_i))_{i=1}^q\), each consequence \(T_i=E_i\cap H_i\) is one state bit. From anchor \(w\), bit \(i\) activates when its E-side and H-side each contain either a matching literal slice or an already active consequence:
\[
x_i^{(t+1)}(w)=
\left(a_i(w)\vee\bigvee_{j:T_j\subseteq E_i}x_j^{(t)}(w)\right)
\wedge
\left(b_i(w)\vee\bigvee_{j:T_j\subseteq H_i}x_j^{(t)}(w)\right).
\]
This is the least solution from zero of a positive cyclic AND/OR system. It stabilizes after at most q strict rounds. An empty consequence activates exactly when the least preserving closure has reached the contradiction; if none activates, that closure is itself a valid semi-filter witness against Q.

Each initial endpoint test is a disjunction of signed truth-table coordinates. For \(E\subseteq U\), it is \(\bigvee_{(k,b):\,U\cap\{z:z_k=b\}\subseteq E}[w_k=b]\). A proper E can contain at most one polarity for each coordinate. The remaining containment network \(T_j\subseteq E_i,H_i\) is unrestricted semantic data, so counting endpoint descriptions is not a valid invariant.

For a partial list Q, define the remaining closure distance \(\delta_Q(w)\) as the minimum number of extra pairs needed to activate an empty consequence. It is at most \(N-1\) by the literal-slice chain and one-pair-Lipschitz. C-03 gives the initial value \(\delta_{\varnothing}(w)\ge N-\log_2M_2-1=N-o(N)\) for every low anchor. A natural sufficient lemma would bound \(\mathbb E_\mu[\delta_Q-\delta_{Q\cup\{p\}}]\le N^{-\epsilon}\) for every Q,p under one fixed distribution \(\mu\), but C-73 refutes it already at Q empty. Averaging over coordinate pairs in a minimum certificate finds one two-literal intersection that saves a rule for at least \(1/4-o(1)\) of any anchor distribution. The distance remains useful, but an additive static average cannot force a superlinear bound.

Fractional rounding for a fixed R-filter family gives \(O(N\log R)\) pairs under the project fractional ceiling, but a fixed list of witnesses does not represent all semi-filter extensions. A pair may enlarge a current proper closure without making it empty; the next adversarial witness then depends on Q. This adaptive quantifier is the precise reason the fixed-family estimate is not a universal \(O(N\operatorname{polylog}N)\) upper bound.

The recurrence was cross-checked against explicit upward closure in 204,160 one-rule and seeded two-rule cases on the sparse six-point toy. It recovers the toy's exact two-pair universal cover and verifies that a shared two-literal intersection saves one local rule for each anchor. This validates the encoding and illustrates C-73's sharing mechanism; a global state-complexity potential, a superlinear cover bound, and \(P\ne NP\) remain open. See [the full closure-game audit](research/FUSION_CLOSURE_GAME_2026-09-26.md), C-67ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œC-73, and [the reproducible check](experiment_fusion_closure_recurrence.py).

### 2.120 Empty-rule activation has a proof-depth floor

The high promise side is two-wise rich: for every assignment to two distinct truth-table coordinates, the corresponding cylinder has \(2^{N-2}\) tables, while the total number \(M_2\) of tables of complexity at most \(s_2=N^\beta\) is \(2^{o(N)}\) for fixed \(\beta<1\). Thus every such cylinder contains a high table.

For an empty rule \(E_i\cap H_i=\varnothing\), its two seed predicates cannot both be true at the same low anchor. If different coordinates supplied matching slices contained in E and H, two-wise richness gives a high table in their intersection; if the coordinate is the same, either the same nonempty slice lies in both endpoints or the anchor cannot match both polarities. Therefore no empty consequence activates in the first round.

More generally a first empty activation at round t has an unfolded binary AND/OR proof with at most \(2^t\) literal leaves. Their matching subcube must exclude the entire high side, which requires at least \(N-\log_2M_2\) distinct coordinates. Hence \(t\ge\log_2(N-\log_2M_2)=\log_2N-o(\log N)\). C-72 records the proof. This lower-bounds parallel proof depth only; it leaves open whether many anchors force a superlinear total rule list.

### 2.121 The first shared step defeats additive progress

For each low anchor choose a minimum literal-slice certificate \(S_w\) excluding all high tables. Its size is \(N-o(N)\). Under any probability measure \(\mu\) on low anchors, averaging over the \(\binom N2\) coordinate pairs shows that some pair \(\{k,\ell\}\) occurs in \(S_w\) for \(1-o(1)\) of the mass. One of the four signs \((b,c)\) then accounts for at least \(1/4-o(1)\) mass. Adding the pair of literal slices \((G_{k,b},G_{\ell,c})\) reduces the remaining rule count by exactly one on all those anchors: it replaces the first intersection of those two certificate leaves.

Therefore every static \(\mu\) has an initial one-pair marginal of at least \(1/4-o(1)\). This refutes the proposed small-marginal theorem as a route to \(N^{1+\epsilon}\), even though \(\delta_Q\) itself is well-defined and one-pair-Lipschitz. C-73 records the exact calculation.

**Implication for the next model.** The proof must track shared intermediate intersections as objects that can pay for many anchors at once. The difficulty is to show that sharing a few low-order intersections does not let a short pair system assemble the full high-excluding certificates for all low anchors. This suggests a global state-complexity potential on the intersection DAG, not an additive sum of per-anchor distances.

A block test exposes the next compression obstacle. A k-coordinate block can compute all \(2^k\) pattern states using \((k-1)2^k\) pairs; merging two blocks needs pattern-specific intersections, and a balanced hierarchy has an exponential top table. Taking a union over all patterns restores U and erases the anchor condition. Restricting to low-anchor patterns still gives up to \(M_1=2^{N^{\beta+o(1)}}\) states. This rejects the direct block-recursion route, not all semantic compression.

### 2.122 Pair lists as recursive dual-rail intersection programs

For each rule i, let X_i be the set of anchors at which its consequence T_i enters the least closure. The exact update is

    X_i^(t+1)=(A_i union union_{j:T_j subset E_i} X_j^(t))
              intersect (B_i union union_{j:T_j subset H_i} X_j^(t)),

where A_i and B_i are unions of matching literal half-cubes. A semantic pair list is therefore a positive recursive program with q intersection states. Its empty-rule activation set K_Q contains every low anchor it refutes and excludes every high table in U. This is the separator property C-74.

Unrolling q rounds gives at most q^2 AND gates, with unbounded ORs. This yields a necessary representation, but not a converse or a useful bounded-fan-in lower bound: the generic conversion costs an extra factor O(N+q). The direct proof target is a superlinear lower bound on the recursive program's number q of states. Monotone conjunctive complexity is a literature analogue, but dual rails, fixed-point recursion, semantic incidence relations, and the promise gap make this a different model.

The restricted-catalogue incidence gadget fails: its unlisted pair (A,B) produces a common violation for every filter; inserting that consequence into all filters forces every encoded T_j and destroys the incidence choices. This is a concrete warning that arbitrary semantic pairs must be handled from the start.

**Research status.** Exact reformulation only; no state lower bound, separator theorem, or P-versus-NP breakthrough. See C-74 and Q34.

### 2.123 Why the direct communication-game proof is too weak

Given low w and high z, follow a least-fixed-point proof of an empty rule at w. Since the same empty state is inactive at z, Bob selects a side unsupported at z; Alice gives a literal or prior-state support valid at w. A literal gives a differing coordinate. A prior state remains active on w but inactive on z and has a smaller activation rank. This yields a deterministic mismatch protocol in O(q log(N+q)) communication (C-75).

The relation itself has an easy protocol: Alice sends a size-s1 circuit for w, and Bob scans z for a disagreeing coordinate. Its cost is O(s1 log s1 + log N)=N^(beta+o(1)), below the local linear pair-count lower bound. Therefore communication depth is the wrong measure. A promising variant would need a direct lower bound on the protocol DAG/state system, retaining sharing information that ordinary communication cost discards.

**Status.** Fully checked auxiliary route; closed for the superlinear target.

### 2.124 Seed predicates form a one-sided code with a monotone decoder

Write sigma(w) for the vector of all 2q endpoint seed predicates. Fixing the seed values makes the closure recurrence depend on nothing else about w; its output h_Q(sigma(w)) is monotone in the seed vector. If Q kills every low anchor and no high anchor, then no low codeword sigma(w) can be coordinatewise below a high codeword sigma(z).

For each low w, conjoin all nonconstant seed clauses true at w. Any table satisfying this CNF has a seed vector above sigma(w), so monotonicity would make the closure refute it too. The CNF therefore contains no high tables. Since a satisfiable m-clause CNF on N bits has at least 2^(N-m) models, w must satisfy at least N-log2(M2)=N-o(N) seed clauses. Equivalently, the matched-literal support hypergraph at w has transversal number at least N-o(N).

This is a necessary condition, not the sought global bound. It gives only q>=N/2, weaker than the existing local q>=N-o(N). An abstract dictionary of both polarities of every bit already supplies full minterm certificates; the unresolved task is the state cost of the monotone decoder and its compatibility with actual semantic endpoints.

**Research target refined by C-76.** Prove a superlinear lower bound on the semantic state decoder for any dictionary whose accepting low patterns have high-excluding CNF certificates, or find an O(N)-state decoder to refute the route. The clause dictionary alone cannot carry the separation lower bound.


### 2.125 Shared DAGs versus cyclic fusion states (C-77)

The active pair list is a cyclic monotone conjunctive computation on \(\Gamma_{\rm prom}=Y\sqcup Z\), with filter universe \(Z\). Its q rules are q AND/intersection states; unrestricted OR support routing is free in the fusion measure. The activation fixed point is 1 on low-circuit truth tables and 0 on high-circuit tables; its medium-band values are unconstrained. The separate full-domain cover recognizes exact low membership. Cavalar-Oliveira exact theorem identifies each chosen ground-set parameter with cyclic intersection complexity:
\[
\rho_{\rm prom}(Y,\mathcal B_{\rm prom})=D^\circ_\cap(Y\mid\mathcal B_{\rm prom}).
\]
This is the precise model, rather than ordinary deterministic communication complexity.

A useful communication certificate exists for every low/high pair: start at a Q-state active on the low table and inactive on the high table; follow an active predecessor on the low side while the same predecessor is inactive on the high side; the least-fixed-point rank strictly decreases; eventually a literal gives a signed mismatch. The rule-dependency graph may be cyclic globally, even though each valid run terminates. This is a ranked cyclic rectangle game, not an ordinary rect-DAG.

Resource conversions:

- cyclic intersection count q to acyclic AND count: at most q^2;
- cyclic system to binary-fanin full circuit / rect-DAG size: O(q^2(q+N))=O(q^3) using q>=N-o(N); the SCC-sensitive C-91 bound improves this to O(qN+q^2+sum_C(r_C e_C+r_C^2));
- full exact-membership KW DAG back to a fusion cover: at most its AND count;
- promised low/high KW DAG back to the active promise-ground-set cover: O(L) pairs for an L-vertex DAG, by C-90; accepting the medium band blocks only an upgrade to the separate full-domain exact cover.

Hence a standard DAG-size lower bound must exceed roughly \(N^{3+3\epsilon}\) to imply the target \(q>N^{1+\epsilon}\) through the generic conversion. A lower bound on acyclic AND complexity for every low/high monotone separator above \(N^{2+2\epsilon}\) would suffice through the square bound. Both are open.

The primary working object is now **ranked cyclic non-shareability**: prove that shared support routing in a cyclic conjunctive program on \(Y\sqcup Z\) cannot accept every size-\(s_1\) truth table and reject every table above \(s_2\) with only \(N^{1+o(1)}\) intersections. Ordinary protocol bits, universal-circuit evaluation, hashing, and the parity tree/DAG example do not establish this. See [DAG/Fusion bridge audit](research/DAG_FUSION_BRIDGE_2026-09-26.md).

### 2.126 C-78: shared DAGs preserve state reuse but do not preserve cycles for free

The search relation has two versions. Plain mismatch on \(Y\times Z\) is total and has low communication cost \(O(s_1\log(n+s_1)+\log N)\), because Alice can send a circuit description. The Q-dependent witness relation additionally asks for the ranked sequence of closure supports; it is total only when Q covers every low table and uses \(O(q\log(q+N))\) communication by direct traversal.

Sokolov Boolean communication games and GGKS rect-DAGs are acyclic binary rectangle-cover graphs. Fusion is exactly cyclic intersection complexity \(D^\circ_\cap=\rho\), with q charged AND states and free OR support routing. Rank unrolling yields a standard rect-DAG of \(O(q^2(q+N))=O(q^3)\); acyclic AND-only complexity is at most \(q^2\). A lower bound transferred through the binary DAG therefore needs scale \(N^{3+3\epsilon}\), while a separator AND lower bound needs \(N^{2+2\epsilon}\).

A universal interval-pattern DAG has \(O(|Y|+\sum_{I\ dyadic}\pi_I(Y))\) nodes, where \(\pi_I(Y)\) counts low-table restrictions on interval I. It shares comparison states whenever restrictions agree, improving on one scan per low table. It is an upper bound for a particular construction, not a general lower-bound statistic, and it is far above near-linear under current class-size bounds.

**Learning:** bit cost, tree-node count, DAG-node count, AND count, and cyclic-state count are distinct resources. The graph on q rule states can cycle, even though every valid path decreases an input-specific activation rank. Any direct lower bound must retain cyclic least-fixed-point semantics or pay the unrolling loss.

### 2.127 C-79: a medium-band filter blocks direct promise-cover reuse

For sufficiently small fixed OPS \(\beta\), every signed input-coordinate cylinder contains a table in \(M=\mathrm{SIZE}(s_2)\setminus\mathrm{SIZE}(s_1)\). Choose \(k\) with \(2^k\asymp s_2\); a shared prefix decoder plus an OR of selected minterms computes all \(2^{2^k}\) functions of k variables in \(O(2^k)\) gates. Half have either prescribed value at any fixed coordinate. This outnumbers size-\(s_1\) circuits when \(\beta\) is small, by the standard circuit-counting upper bound.

For a low anchor w, take the upward closure over \(M\cup Z\) generated by M and all matching literal slices. It is a semi-filter above w. Every such slice intersects M, so an endpoint contained entirely in Z cannot contain any generator. Thus all pairs in a cover for the larger class \(\mathrm{SIZE}(s_2)\), whose endpoints lie in Z, preserve this filter and cannot be re-used as a cover for low Y.

**Scope:** this proves a concrete obstruction to direct endpoint reuse, not to a reverse transformation that adds medium-band pairs. It gives no superlinear lower bound.

**Frontier:** prove residual-rectangle non-shareability at the \(N^{3+3\epsilon}\) rect-DAG scale, prove the target directly in \(D^\circ_\cap\), or construct a genuinely \(N^{1+o(1)}\) universal DAG. No such lower bound or construction is known. Full proofs: [DAG/Fusion bridge audit](research/DAG_FUSION_BRIDGE_2026-09-26.md), ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§9ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ10.

### 2.128 C-80: fixed structural families can share very cheaply

The family of all functions on k input bits, lifted to \(N\)-entry truth tables, contains \(2^{\Theta(s_1)}\) low tables when \(2^k=\Theta(s_1)\). Yet the mismatch search against every high table has an \(O(N)\)-node rect-DAG: a high table must be mixed on some common fiber block, Bob locates that block, Alice provides its low value, and Bob outputs a coordinate with the opposite value.

The family size and even the per-anchor certificate length therefore say little about shared-DAG hardness. The unresolved cost is the routing among many incompatible partitions induced by all low circuits. For each fixed \(w\), every high \(z\) varies on a fiber of \(w^{-1}(0),w^{-1}(1)\), but the location and partition vary with \(w\).

**Next theorem:** lower-bound the number of incompatible partition-residual rectangles that an arbitrary DAG needs, or construct a compact router for all circuit descriptions. C-80 is a counterexample to code-family counting as a lower-bound tactic, not a refutation of the full Gap-MCSP DAG route.



### 2.129 C-81/C-82: signatures encode partial certificates

For a rect-DAG with S vertices, a low row's signature records membership in every row side A_v. If two low rows share it, their common reachable leaves are identical against each high table. A disagreement set D larger than log|SIZE(s2)| would have a high completion, but no output label could be valid for both rows. Therefore each signature class has diameter at most N^(beta+o(1)).

The condition is genuine, but row-signature counting has a hard ceiling: there are at most |Y| signatures, so it can prove at most S >= log|Y|=N^(beta+o(1))=o(N). The fixed-block low code yields only S=Omega(s1).

The dual column statement is a certificate condition. Two high tables sharing a signature must have a common agreement pattern with no low completion. Any pattern on O(s1/n) truth-table coordinates has a low completion by minterm interpolation, but large irregular partial assignments may not.

**Model update:** single-party signatures do not capture the routing cost. A useful lower bound must charge joint residual transitions or incompatible circuit-induced partitions.

### 2.130 C-83: fusion states are cyclic loop states

A successful q-pair list induces q rule states. On each low/high pair, Bob selects a side false at the high closure and Alice selects a matching literal or active predecessor. Every predecessor step decreases the low input's first-activation rank, so play terminates within q steps. The static graph may cycle and has O(q^2+qN) semantic support arcs.

This is exactly the cyclic-intersection model D^circ_cap=rho, not a standard acyclic rect-DAG. Binary acyclic rank layering still costs O(q^2(q+N))=O(q^3); no O(q polylog N) conversion is known. Counting q loop states alone does not remove cycles or pay for fan-out.

**Open theorem:** exploit endpoint-induced incidence to compress the acyclic simulation, or prove a direct superlinear lower bound in D^circ_cap. No P-vs-NP proof has been obtained.


### 2.131 C-84: a DAG state class has a common high-free core

A row-signature class R shares every feasible DAG vertex. For any fixed high table z, all pairs (w,z) with w in R therefore share the same reachable output leaves. A common reachable leaf has to be valid for every row in R, so its coordinate is fixed to one common bit throughout R and differs from z. The coordinates on which all rows of R agree form a partial assignment with no high completion.

Counting completions forces this core to fix at least N-log|SIZE(s2)| = N-N^(beta+o(1)) coordinates. Every rect-DAG therefore induces a cover of Y by at most 2^S high-free coordinate cylinders, giving S >= log C_cyl(Y,Z).

**Limit:** singleton cylinders give C_cyl <= |Y|, hence this still cannot force S>N. The cylinders may include medium tables, so the statement does not directly give a fusion cover. The new content is the common-core geometry; the lower-bound work shifts to the number and routing cost of these certificates.


### 2.132 C-85: quotient blocks must be separated by a common coordinate

Partition Y and Z by complete membership signatures across the DAG nodes. Every product block R x C has the same feasible vertices for all its input pairs, because both row-side and column-side rectangle memberships are fixed within the classes. The same reachable leaves serve the entire block. One common output leaf must therefore use a coordinate fixed on all rows in R and all columns in C, with opposite values.

In common-core notation, every pair of nonempty classes satisfies K_R intersect K_C nonempty with p_R(k) != q_C(k) for some k. This couples the row and column certificate geometry.

**Open direction:** bound the class arrangement or the routing cost needed to realize all cross-class separations. A count of output rectangles is insufficient: the relation already has a 2N-rectangle signed-mismatch cover.

Counts of row signatures, column signatures, or class pairs are capped respectively by log|Y|=o(N), N, and N+o(N), all below the N^(3+3epsilon) scale required by the current q-to-DAG bridge. The lower-bound target must charge how a DAG routes through these class pairs.


### 2.133 C-86: state reuse must preserve residual correctness

An O(N) scan-and-merge idea would use one state after coordinate i for every history with no mismatch so far. In the Boolean DAG game, however, the state is a rectangle-defined valid set, and every pair valid at that state must still have a correct continuation. A full-product state also includes pairs whose mismatch was in the discarded prefix, so searching only the suffix can fail.

The set of pairs that agree on a prefix is a union over all prefix patterns, not a rectangle. Retaining the pattern restores validity and reproduces the profile-state construction. This kills the scan-and-merge shortcut; other shared routers remain open.


### 2.134 C-87/C-88: fingerprints and circuit-description space

A rank-r linear sketch of an N-bit truth table has fibers of size 2^(N-r). If r<N-log|SIZE(s2)|, each fiber contains a high table. Thus every low w has a high z with the same sketch. This rules out sublinear fixed-coordinate and linear fingerprints, but says nothing about nonlinear separators or adaptive DAGs.

In description space Alice can send a size-s1 circuit description using O(s1 log s1) bits, after which Bob finds a mismatch locally. A shared interval DAG can index states by the restriction G(d)|I; the predicate that some mismatch occurs in I mixes both parties and is not a rectangle. The best construction therefore retains restriction profiles and is not near-linear.

**Open theorem:** exploit circuit syntax to reduce the profile cost, or prove a lower bound against every description-aware shared DAG. Neither has been established.


### 2.135 C-89: the shared-DAG target is a separator circuit

Define SepCirc(Y,Z) as minimum Boolean circuit size of a function equal to 1 on low tables Y and 0 on high tables Z, with medium inputs unconstrained. The standard rect-DAG for signed mismatch on Y x Z is equivalent up to constant basis factors to SepCirc. From a DAG, label leaves by signed literals and combine child separators by AND, OR, or child reuse according to the rectangle-cover case. In the other direction, restrict the Karchmer-Wigderson game of a separator circuit to Y x Z.

A q-pair cover gives SepCirc=O(q^2(q+N))=O(q^3). Therefore a separator lower bound N^(3+3epsilon+delta), with any fixed delta>0 to absorb constants, implies q>N^(1+epsilon) and then P!=NP by OPS.

**Limit:** SepCirc may accept medium tables, so it does not give the full-domain exact cover. C-90 shows the rect-DAG does reverse to the active promise cover with O(L) pairs. C-79 blocks only direct endpoint reuse when upgrading to the full-domain universe.

### 2.136 Promise and full-domain cover parameters

Keep two ambient universes distinct:

- \(\rho_{\rm prom}\): \(\Gamma_{\rm prom}=Y\sqcup Z\), with endpoint/filter universe Z. This is the current Gap-MCSP target.
- \(\rho_{\rm full}\): \(\Gamma_{\rm full}=\{0,1\}^N\), with universe \(M\sqcup Z\). This is the exact low-set cover.

A mismatch rect-DAG of L vertices is equivalent up to basis constants to a promise separator circuit, and that circuit's set construction gives \(\rho_{\rm prom}\le O(L)\). Conversely, a full-domain cover restricts to a promise cover: lift any hypothetical preserving filter on Z by inverse image under intersection with Z. Hence \(\rho_{\rm prom}\le\rho_{\rm full}\).

The medium-band escape filter blocks direct reuse of a promise cover as a full-domain cover, not the DAG-to-promise-cover map. Quantitatively, \(\rho_{\rm prom}\le\mathrm{SepCirc}\asymp\mathrm{rectdag}\le O(\rho_{\rm prom}^3)\). The left side makes a direct \(\rho_{\rm prom}>N^{1+\epsilon}\) target sufficient for OPS; the cubic right side means a generic DAG lower bound would need exponent above 3 to establish that q target.

**Research consequence:** keep attacking direct cyclic non-shareability at q states, or improve q-to-acyclic conversion. Do not treat the full-domain medium band as an obstacle to the active promise-domain reverse map.

### 2.137 C-91: component-local cyclic cost

The global q-round unfolding is wasteful when the fixed support graph has small strongly connected components. Since T_i=E_i intersect H_i lies in both endpoints, the raw support graph has a self-loop at every state. C-91 proves that deleting these self-support terms preserves the least fixed point; SCCs are taken in the resulting loop-free graph. If component C has r states, its incoming external signals are fixed, and its local least fixed point stabilizes after at most r rounds. Each local round costs O(r^2) bounded-fanin support OR and AND gates, giving O(r^3) per component.

A sharper gate count keeps the internal side-incidence e_C=sum_{i in C}(|P_i intersect C|+|R_i intersect C|), counting only loop-free incidences: the cost is O(qN+q^2+sum_C(|C|e_C+|C|^2)). Thus q^2 size follows if every SCC has e_C=O(|C|), or if the largest SCC is O(sqrt(q)). This is a proved compiler refinement, not a circuit lower bound. The true remaining bottleneck is a large, dense mutually recursive component; it may still admit a compact separator.

### 2.138 C-92: carrier inclusion removes transitive two-sided supports

After C-91 removes self-support loops, partially order the distinct carriers T_i by inclusion. If T_j is a strict non-cover subset of T_i, its support into rule i is present on both sides and can be deleted. Every cover relation remains a two-sided support, so in every fixed point an active state propagates along every upward carrier chain. Therefore any deleted support into i can only be active when i is already active; the pruning preserves the least fixed point.

**Learning:** a dense-looking dependency graph can be an artifact of transitive inclusion. Nesting alone does not force a cubic SCC compiler cost. One-sided supports and equal-carrier groups are not removed by this argument. See C-92 in the DAG/Fusion bridge audit.

### 2.139 C-93: equal carriers share a recursive bit, not their alternatives

Group rules by their distinct intersection T_i. If a group has at least two rules, every rule supports every peer on both sides; hence at the least fixed point all bits in that group agree. Replace them by one carrier bit whose activation condition is the OR of the original per-rule conjunctions. A singleton group retains its one conjunction. This quotient preserves the least fixed point for every seed assignment.

For carrier SCC C, let p_C count carrier bits, q_C count candidate rules, and e_C count internal candidate-side carrier incidences; let e_out count external incidences. Solving SCCs locally yields separator size O(qN+e_out+sum_C p_C(e_C+q_C)), coarsely O(qN+qp^2) for p distinct carriers. The seed clauses and q alternatives remain charged. Combining the quotient with C-92 reduces recursive width but does not give a lower bound on q or a P-vs-NP proof.

**Next obstruction:** the group update is OR_i(A_i AND B_i), not generally one pair (OR_i A_i) AND (OR_i B_i); that factoring creates cross-pair activations. Any further compression must preserve candidate-specific two-sided compatibility.

### 2.140 C-94: one-sided escape supports carry all feedback

After the C-91 self-loop deletion, C-92 inclusion pruning, and C-93 equal-carrier quotient, the only strict-subcarrier supports left are Hasse-cover edges, and they support both sides of every candidate at the upper carrier. Factor their common OR signal K_t. A remaining support from carrier u not contained in target carrier t can occur on only one side, because support on both endpoints would imply u subseteq E_i intersect H_i=t. Thus every directed cycle in the reduced carrier graph must include a one-sided escape edge.

Write the quotient recurrence as H_t(x)=K_t(x) OR D_t(x), where D_t is the OR of candidate-specific conjunctions built from literal seeds and escape supports. Let Up close a carrier set upward in the inclusion poset. The macro map G(x)=Up(D(x)) has exactly the same fixed points as H: the Hasse recurrence expands to x_t=OR_{s subseteq t}D_s(x). If s distinct carrier values occur as escape sources, iteration of G from zero stabilizes in at most s+1 rounds, because every later strict round requires a newly activated escape-source carrier.

With xi candidate-side escape incidences and kappa Hasse edges, this gives an ordinary separator circuit of size O(qN+(s+1)(xi+kappa+q)). Since xi<=2qs, kappa<=p(p-1)/2 and p<=q, this is at most O(qN+qp^2); if s=0 it is O(qN+q+p^2). Compare with C-91/C-93 by support structure; none dominates uniformly.

**Magnification audit:** in the worst case p,s<=q and q>=N-o(N), the compiler remains O(q^3), so a generic separator-DAG lower bound still needs scale above N^(3+3epsilon) to force q>N^(1+epsilon). If there are no escape supports and p<=N^gamma, then q<=N^(1+epsilon) would imply separator size O(N^max(2+epsilon,2gamma)). This conditional bound does not cover arbitrary pair lists because p and s are uncontrolled.

**Literature boundary:** using a feedback vertex set to analyze Boolean-network fixed points is established; for example, [Aracena, Goles, Moreira, and Salinas](https://arxiv.org/abs/2004.01259) enumerate fixed points with exponential dependence on a positive feedback vertex set. C-94's contribution is the project-specific reduction of fusion supports to a carrier-poset DAG plus one-sided escape dependencies, not the general feedback-set idea.

### 2.141 C-95: the final empty rule needs an escape input

For the OPS parameter regime, the number \(M_2\) of non-high truth tables is less than \(2^{N-2}\). The two direct seed predicates of an empty-carrier rule are clauses over signed table bits. If their conjunction had one satisfying assignment, fixing one true literal from each clause would leave a subcube of at least \(2^{N-2}\) satisfying assignments, including a high table. That would directly activate the empty carrier at a high input, contradicting the principal-filter witness. Thus every empty-rule seed conjunction is identically false.

At every low anchor, an activated empty rule must therefore use a one-sided escape support. Let S_0 be the carrier values appearing in escape lists of empty-carrier rules, and X_u the low-anchor set activating carrier u. Then \(Y\subseteq\bigcup_{u\in S_0}X_u\).

If both empty-rule seed clauses are nonempty, unsatisfiability forces them to be complementary unit literals on one coordinate. The bit value determines which endpoint requires an escape source; an empty seed clause always requires an escape on that side.

**Learning:** the final contradiction path cannot be purely seed-driven; every low table must reach the empty consequence through S_0. This identifies the exact interface for a lower bound. It does not lower-bound |S_0| because activation sets may overlap, so the proof must also charge how the other side stays blocked on high tables.

**New frontier:** prove the escape alternatives are non-shareable at the required scale, or build a compact escape router. C-94 localizes feedback but gives no lower bound on s, xi, q, or separator complexity.

### 2.142 C-96: terminal cones contain many seed features, but may overlap

For each low anchor w, choose an empty-carrier rule active at w and one true support on each side. Let C(w) contain the terminal rule and the full predecessor cones of selected predecessor supports. The conjunction of nonconstant seed clauses in C(w) true at w is high-free: any table satisfying it preserves the selected predecessor activations and direct seed supports, activating the empty carrier. If it has m clauses, it has at least 2^(N-m) models, so m>=N-log2(M2). At most two seed clauses come from one rule, giving |C(w)|>=(N-log2(M2))/2=(N-o(N))/2.

This localizes linear causal support for each contradiction, but is weaker than the global q>=N-o(N) floor and says nothing about overlap among different anchors. Only the selected predecessor cones are predecessor-closed; unused terminal-rule alternatives need not be included.

### 2.143 C-97: description length is not shared-DAG size

Let G:D1->Y map short circuit descriptions to their truth tables. For signed mismatch on Y x Z, standard rect-DAG size is exactly invariant under replacing Y by D1: lift each Alice predicate through G for one direction, and choose a section Y->D1 to restrict a description-space game for the other. Free local computation makes the same true for communication cost and protocol-tree size.

Rect-DAG size is Theta(SepCirc(Y,Z)), the circuit size of a promise separator (free behavior on medium tables). A q-pair cover gives the current O(q^3) standard DAG bound in general, with sharper C-91/C-93/C-94 parameterized bounds; conversely a DAG of size L gives rho_prom=O(L). Therefore a standard N^(1+o(1))-size DAG would kill the desired rho>N^(1+epsilon) route. A universal evaluator G(d)(k) alone does not provide rectangle-valid shared states; the prefix-pattern construction has size O(|Y|+sum_I pi_I(Y)) and is not near-linear. This is a precise failure of that construction, not a lower bound. The proof and model table are in the C-97 bridge section.

### 2.144 C-98: a conditional cryptographic test for shared-DAG non-shareability

Assume a one-bit PRF family with polynomial-size evaluation circuits and security against nonuniform polynomial-size distinguishers with polynomially many oracle queries. Embed its truth tables on N=Theta(lambda^a) padded inputs. Choose a so that a*beta > d. Then every PRF table belongs to the low class Y, since s1=N^beta/(cn) dominates the evaluation circuit. A uniform truth table belongs to the high class Z except with probability 2^(-N+o(N)), because only 2^(O(N^beta log N)) tables have circuit size at most s2=N^beta.

A promise separator circuit h of size N^C would query all N PRF values and evaluate h. It accepts every PRF table and almost never a uniform table, contradicting the PRF assumption. Thus, conditionally, SepCirc=S_rect=N^(omega(1)); the inequality S_rect<=O(rho_prom^3) yields rho_prom=N^(omega(1)).

**Learning:** the shared-DAG difficulty is exactly the type of range-separation task that cryptographic pseudorandomness can make hard, even though each row individually has a short circuit. This adapts the established MCSP/PRF paradigm to the project's promise and tracks the cubic cover-to-DAG loss. It is conditional, not an unconditional non-shareability theorem and not a P-vs-NP proof. Keep the unresolved target as an unconditional lower bound or an explicit small separator.

### 2.145 C-99: the PRF premise already implies the class separation

Under C-98's nonuniform-secure PRF assumption, suppose NP were contained in P/poly. MCSP is in NP: guessing a small circuit and checking it on all N truth-table entries is polynomial time after capping oversized thresholds at the Shannon bound. Therefore MCSP has polynomial-size nonuniform circuits. Fix the MCSP threshold to s2=N^beta. The resulting circuit accepts every table in Y, since s1<s2, and rejects every table in Z. It is a promise separator of size polynomial in N, hence polynomial in lambda under the C-98 embedding. Querying all N padded PRF points and applying this circuit distinguishes PRF outputs from uniform tables, contradicting security.

So the C-98 implication rho_prom=N^(omega(1)) is correct under its assumption, but the assumption already implies NP not subset P/poly and P not equal NP. This conditional theorem calibrates the DAG/fusion model; it does not provide an independent path to the separation. The nonuniform security is essential because an arbitrary separator circuit family need not be uniformly constructible.

### 2.146 C-100: batch the OR frontiers in the cyclic-to-DAG compiler

For r fixed subsets of a common m-bit vector, split the vector into blocks of about log r bits. Precompute every subset OR once within each block; then assemble each requested OR from its block outputs. The fan-in-two circuit size is \(O(r(1+m/\min\{m,\log(r+1)\}))\). This elementary shared-subset construction batches the seed clauses, escape support lists, and carrier down-sets in C-94.

The refined compiler is
\[
O\!\left(qN/\log N+(s+1)\left[q+\min\{\xi,q(1+s/\log(q+1))\}+\min\{p+\kappa,p+p^2/\log(p+1)\}\right]\right),
\]
where p is the number of carriers, s the distinct escape-source count, xi their candidate-side incidence count, and kappa the Hasse edge count. Its generic worst case is \(O(q^3/\log q)\), a logarithmic improvement over the previous \(O(q^3)\) simulation.

**Learning:** repeated routing ORs can be shared more aggressively than the direct edge-by-edge compiler charged. This does not alter the true bottleneck: the least-fixed-point system still needs escape rounds, and a standard DAG lower bound transfers only after the remaining polynomial loss. The target has only shifted by a logarithmic factor; no superlinear lower bound, universal near-linear DAG, or P-vs-NP proof has been obtained. Continue prioritizing direct non-shareability of the cyclic states.

### 2.147 C-101: terminal-cone cube dimension does not beat counting

For a C-96 terminal-cone CNF with m seed clauses, choosing one true literal from every clause fixes at most m truth-table coordinates. The remaining coordinate subcube lies wholly in SIZE(s2), so m >= N-Delta_box(s2), where Delta_box is the largest coordinate cube contained in the circuit class. Since there are at most 2^(O(s2 log(n+s2))) size-s2 circuits, Delta_box <= O(s2 log(n+s2)); this recovers only m >= N-o(N). A localized k-dimensional input subcube supports every Boolean labeling on its 2^k points with an O(n+2^k)-size circuit, showing Delta_box >= Omega(s2) for s2 >> n. This does not improve the upper bound needed for a cone lower bound.

A coordinate cube requires all outside truth-table bits to be fixed. Ordinary VC shattering does not impose that, and C-80's block-constant code is not a coordinate cube. Koiran's report with a similar title studies sigmoidal circuits and does not give the needed standard-circuit bound. Keep the cross-anchor cone overlap as the unresolved issue.

### 2.148 C-102: high tables split a low table's fiber

If a high table z were constant on each fiber of a low table w, then z=g composed with w for one of four unary Boolean maps, making z one of 0, 1, w, or not-w and therefore low. Consequently there are a,b with w(a)=w(b) and z(a) != z(b). Each fixed pair is a rectangle-local certificate (Alice checks equality under w; Bob checks inequality under z), giving an O(N^2)-rectangle nondeterministic cover.

This alternate total search relation has not been connected to the ranked C-75 fusion path. A certificate cover is not a deterministic binary routing DAG: when only one party accepts a candidate, the protocol still needs a valid continuation. Treat this as a candidate structural language for partition incompatibility, not as a non-shareability theorem.

### 2.149 C-103: fiber search supplies an upper-bound falsification test

A standard fiber-disagreement DAG converts leaf-by-leaf into a signed-mismatch DAG, so rho_prom <= O(S_fib). C-105 rules out the near-linear fiber-DAG falsifier: the output labels already require Omega(N^(2-beta)/log N) edges. The auxiliary lower bound still does not transfer to rho because C-104 loses N^2 on SIZE(s1-1). C-106 gives a conditional bridge: if a q-state closure induced O(q log^d N) universal valid fiber edges, then q=Omega(N^(2-beta)/(log N)^(d+1)); no extraction is known.

### 2.150 C-104: the reverse fiber simulation loses N squared

A mismatch DAG can solve fiber disagreement on Y^-=SIZE(s1-1) by using constant anchors to obtain p with z_p=1 and q with z_q=0, retaining (p,q) in the state-copy index, then using a mismatch run on w or not-w. If the first two points have different w-bits, the third point supplies either a diagonal or off-diagonal cell that completes a same-w/different-z pair. This requires O(N^2 S_mis) graph vertices; Y^- ensures not-w remains in the low class.

Together with C-103, the comparison loses N^2 and changes the low threshold by one gate in the reverse direction. Combining with the C-100 compiler means a fiber lower bound must exceed O(N^(5+3epsilon)/log N) to force q>N^(1+epsilon). This is worse than a direct mismatch or cyclic-cover proof, so use fiber search only to falsify the route with a small DAG.


### 2.151 C-105: affine-subcube output-label barrier for fiber search

A fiber-disagreement DAG's leaf labels form an edge set E on the N input points. For every affine subspace A of size a=Theta(s2 n), its low indicator w=1_A forces E[A] to have Omega(a) edges: if too many points of A were isolated, exponentially many size-a/4 subsets S of isolated points would define z=1_(A\S), and circuit counting guarantees a high z for which no E-edge is a valid output. Averaging over random affine subspaces gives |E|=Omega(N^2/a)=Omega(N^(2-beta)/n).

This proves a superlinear lower bound for the auxiliary fiber-DAG's output labels. The C-104 transfer loses N^2, so it does not yield a mismatch or fusion lower bound. The useful next question is whether the q-state closure itself forces a fiber witness without storing an arbitrary pair of output indices.


### 2.152 C-106: the fiber relation is hard, but its output does not yet come from Q

A fiber witness occupies two cells in the same row of the (w,z) truth table. The closure witness emits one signed mismatch point, and another arbitrary point can lie in the opposite row. C-105 proves the auxiliary fiber DAG needs Omega(N^(2-beta)/log N) distinct output edges, but C-104's N^2 conversion does not transfer this to the mismatch DAG.

The exact conditional bridge is: extract from each successful q-state fusion cover a universal set E_Q of O(q log^d N) coordinate edges, every low/high pair having a valid fiber edge in E_Q. Then C-105 yields q=Omega(N^(2-beta)/(log N)^(d+1)), which is superlinear for every fixed beta<1. This extraction is not proved. Continue on the cyclic states' transition/seed structure; do not mistake auxiliary fiber hardness for a rho lower bound.


### 2.153 C-107: local pair encodings cannot yield fiber witnesses as one mismatch

At a coordinate pair, valid fiber patterns form A x B: Alice's two w-bits agree (A={00,11}) and Bob's two z-bits differ (B={01,10}). Both complements are nonempty, and the promise realizes all local patterns. If independent local encodings F(u),G(v) disagree only on A x B, choose u0 outside A and v0 outside B; equality on invalid cross-pairs forces all F and G labels to one common value. No mismatch remains. This proves that pairwise parity, and any other pointwise encoding whose mismatches are all supposed to be valid, fails for a structural reason. It does not rule out a DAG that filters false mismatches through stateful routing.

The lemma does not forbid a stateful DAG that first narrows the candidate pairs and then routes around false mismatches. Any successful q-to-fiber bridge must use such global state information; keep this distinct from the one-coordinate C-75 witness path.



### 2.154 C-108: sparse universal answer lists nearly match the fiber label lower bound

Patching a low table w on t truth-table coordinates costs O(nt) gates. Hence a high table z must disagree with each unary postprocessing of w on Theta(s2/n) or more points. In one w-fiber, z has a cut with both sides at least r=Theta(s2/n). A random graph with edge probability p=Theta(n/r)=Theta(n^2/s2) hits every such cut of every low w; there are only 2^(O(s2)) low tables, and the cut-miss probability per fiber is exp(-Omega(n|A|))=exp(-Omega(s2)). Thus there exists a universal output-edge list of O(N^(2-beta)n^2) labels. C-105's Omega(N^(2-beta)/n) lower bound pins the minimum label list within O(log^3 N).

This list is only a nondeterministic certificate cover. Serial candidate checks leave a union of row-failure and column-failure rectangles, so a single suffix state is invalid. A correct deterministic DAG by exact low-row enumeration costs O(|Y^-||E|)=2^(O(s2))N^(2-beta)n^2. The remaining issue is the deterministic state-sharing cost; no improvement to rho follows.

### 2.155 C-108's open continuation: route the answer list deterministically

The random universal list and C-105 nearly determine how many possible fiber-edge outputs are needed, but not how to select one with a DAG. For candidate edge e_i, Alice knows P_i(w) (the endpoint w-bits agree) and Bob knows Q_i(z) (the z-bits differ). Totality says their 1-sets intersect. After previous candidates fail, the residual is a union of row-failure and column-failure rectangles, so a shared suffix node cannot forget the rejection history. The coarse exact-row protocol has 2^(O(s2))|E| states.

The structured intersection problem may be easier than arbitrary set intersection because P_w comes from a low-complexity cut and Q_z from an arbitrary high table. Find either a compact router or a lower bound on its state reuse. This remains auxiliary until connected to the cyclic q-state cover.

### 2.156 C-109: tuples of O(log N) low rows have a common fiber witness per high column

Combining r low functions into W=(w_1,...,w_r) costs r s1 gates. If z is constant on each W-fiber, z=h(W) and a DNF for h costs O(r2^r). For r<=eta n with eta<beta and small relative to c, r s1+O(r2^r)<s2, contradicting high complexity. Therefore every high z has a,b with z(a)!=z(b) and w_j(a)=w_j(b) for all r low rows.

This gives a shared valid output for a small row tuple, but the output pair depends on z. It prevents the simplest row-fooling construction and sharpens the target: lower-bound the routing needed to select a column-dependent edge inside a common joint fiber, rather than count rows alone.


### 2.157 C-110: A shared state must solve the rectangle hull of merged histories

A rect-DAG node represents a product set \(A\times B\). If several transcript contexts merge there, the rectangle also contains every cross-pair \(A_i\times B_j\). The descendants must solve those pairs. With \(\Lambda\) the output coordinates below a node, correctness requires disjoint projections \(A|_\Lambda\) and \(B|_\Lambda\). This is the formal cost of forgetting history.

For a prefix search, separate equal-prefix contexts cannot simply merge into a suffix-only state: cross-prefix pairs can agree on the suffix. For a fusion rule state i, the static support graph has descendant output coordinates \(\Lambda_i\); activation-rank descent proves that these coordinates separate the active-low rows from inactive-high columns. This is a necessary structural invariant, not a size lower bound. It is specific to rect-DAG/Boolean-game semantics; a weaker reached-pairs-only DAG model needs separate analysis.

The open task is to quantify the product-hull cross-pairs generated by merging low-circuit descriptions and prove that they force many states or outputs on the real Gap-MCSP promise. The generic q-to-rect-DAG loss is still cubic, and no new \(\rho\) bound follows from C-110.


### 2.158 C-111: Promise-realized cross-pairs defeat a prefix-first router

For \(\beta<1/2\), a block of the C-80 partition has \(B=\Theta(nN^{1-\beta})\) coordinates, more than the \(O(s_2 n)=O(N^\beta n)\) bits needed to count all size-\(s_2\) circuits. Choose a within-block mask p such that both p and \(\neg p\) have complexity above \(s_2+O(k)\). For low block-constant tables \(w_a,w_b\), splice \(w_b\) on P={p=1} and \(w_a\) on J={p=0}. When \(a\ne b\), the splice restricts on a differing block to p or \(\neg p\), so it is high. It agrees with \(w_a\) on J and has P-pattern \(w_b|_P\).

Thus merging two exact P-pattern contexts into a shared suffix-only rect-DAG state creates a low/high cross-pair with no suffix mismatch. The prefix-first/suffix-only router needs exponentially many states in \(s_1\). This does not lower-bound general DAGs: the common block structure supports the O(N) mixed-block DAG from C-80. The unresolved issue is sharing across incompatible circuit-induced partitions under adaptive routing.


### 2.159 C-112: Random splicing of a separated low code

Let C be K truth tables with minimum distance d. Under a uniformly random coordinate split P,J, the splice taking b on P and a on J is uniform over 2^d completions on the disagreement coordinates. If d>2log K+log|SIZE(s2)|, union-bounding over all ordered pairs gives a split for which every off-diagonal splice is high.

A constant-distance error-correcting subcode of the C-80 block-constant family has K=2^{Omega(s1)} and d=Omega(N). Since the size-s2 circuit class has logarithmic size O(N^beta n)=o(N), this applies for all fixed beta<1. It forces a prefix-first/suffix-only rect-DAG to maintain a separate continuation state for every codeword pattern. The general DAG can evade this by using the common block partition and the O(N) mixed-block search from C-80. This is a route-specific non-shareability theorem, not a fusion lower bound.


### 2.160 Frontier after C-112: an adaptive route escapes static incompatibility

A random split can make every splice between distinct rows of a separated low code high, forcing separate states if the protocol commits to that split and then searches only its complement. Yet the C-80 family is solved by an O(N) DAG that searches for a mixed block before committing to any codeword pattern. This is a concrete example where severe non-shareability for one fixed decomposition coexists with efficient adaptive sharing.

The next model must measure diversity of circuit-induced partitions under adaptive search, or charge the cyclic fusion states directly. The static rectangle-hull condition alone cannot yield a global lower bound.


### 2.161 C-113: Adaptive count search handles all low k-juntas

For a low k-junta, the complement of a k-variable support has size n-k. A high table must have at least k+1 essential variables, so its essential-variable set intersects that complement. A PLS game follows a balanced interval tree, with each state recording the exact counts of the two sets inside the current interval and maintaining \(a+b>|I|\). It has O(n^2) states and O(log n) communication per transition; Sokolov's conversion yields n^{O(1)} rect-DAG size.

Bob chooses a z-boundary edge in the shared direction. The low table is constant along that edge, while z changes, so one endpoint is a mismatch. Duplicating O(N)-size edge selectors for n directions gives an O(N log N+polylog N) mismatch rect-DAG for every k-junta low row versus every high table.

This falsifies support-set diversity as a standalone hardness source. The construction does not cover low circuits whose essential support is large; the next structural witness must detect complexity inside a fixed support, perhaps through cofactor boundaries or gate-induced partitions.

### 2.162 C-114: Count-intersection is a reusable adaptive search primitive

For party-local sets \(A_x,B_y\subseteq[n]\), the condition \(|A_x|+|B_y|>n\) guarantees an intersection. A balanced binary interval tree gives an acyclic PLS: states record exact local counts \((a,b)\) in interval I and maintain \(a+b>|I|\). The parties disclose child counts and descend into a child preserving the inequality. There are O(n^2) states and O(log n) communication per successor; Sokolov's PLS-to-Boolean-game conversion yields n^{O(1)} rect-DAG size.

For C-113, the sets are low-row irrelevant variables and high-column essential variables. For each direction i, all routed pairs lie in one valid rectangle: low rows invariant under i times high tables essential in i. The O(N)-vertex mismatch suffix can be shared once per direction, even when several direction-game leaves output i, because this larger rectangle is valid and contains each leaf rectangle. Total size is O(nN+n^{O(1)}).

This is a useful sufficient condition for adaptive sharing, not a full-class separator. Parity is a low O(n)-size circuit with all n variables essential, so the irrelevant-variable set can be empty. Any full Gap-MCSP extension needs a richer witness than support cardinality. This failure is specific to the current certificate; it does not establish DAG hardness.

### 2.163 C-115: Small circuit gate signatures force a high-table split

Choose \(k=\Theta(\log s_2)\) wire values of a low circuit, including its output (input wires may pad the selection), so the original circuit plus an arbitrary k-bit lookup has size below \(s_2\). Every high table must vary on at least one fiber of the joint wire signature; if not, the high table factors through those wires and the lookup circuit computes it. Patching the majority value in each fiber gives a total minority mass of \(\Omega(s_2/n)\).

This generalizes the existence of an adaptive witness beyond low-support functions: even a low circuit with all input variables essential induces a small internal-state partition that a high table must split. The unresolved step is global sharing. The partition is selected by and varies with the circuit description, and the guaranteed minority mass may be concentrated in one cell. The simple count-intersection PLS does not route this relation, and no DAG or fusion-cover lower bound follows. This is a candidate for a new state-merging invariant, not a proof.

### 2.164 C-116: A high circuit contains a hard cofactor, but the gap fragments

If \(s_2=cns_1\), split the input domain into \(m=\Theta(n)\) fixed prefix cells. If every cofactor of a high table had complexity at most \(4s_1\), a selector circuit could combine them below \(s_2\). So one cofactor is high above \(4s_1\); every cofactor of a low row remains at most \(s_1\). Bob can adaptively select the hard cell, yielding an upper reduction to a constant-factor-gap search DAG on a slightly smaller domain.

This identifies a robust local witness, but it spends the \(n\)-factor gap and does not transfer lower bounds upward. Adding a fixed hard marker to embed a smaller instance fails: the low row cannot match the marker, so the DAG may output a mismatch there. We need either an output-preserving gap amplifier or a direct state lower bound.

### 2.165 C-117: Same-threshold padding is exact for mismatch DAGs

A truth table lifted to ignore extra input variables has exactly the same circuit complexity. Restricting a larger rect-DAG to those lifted rows/columns and projecting each output coordinate back to its suffix gives a smaller rect-DAG with no extra vertices. Hence \(S_{n-k}(a,b)\le S_n(a,b)\).

The promise thresholds reparameterize: on \(n'=n-k\) variables, \(\beta'=\beta n/n'\) and \(c'=cn/n'\). For fixed \(\beta'>\beta\), \(N'=N^{\beta/\beta'}\), so a small-instance lower bound exponent \(\gamma\) becomes \((\beta/\beta')\gamma\). This offers a way to import stronger-parameter lower bounds only when they have enough exponent margin and are uniform across the shifted constants. It is distinct from the failed reverse embedding of the weaker \(4s_1\) cofactor problem.

### 2.166 C-118: Pullback transfers the fusion cover itself

Ignored-input lifting embeds the smaller low/high truth tables into the larger promise without changing circuit complexity. Restrict a big cover's endpoints to the smaller lifted high set. If this list failed, a small semi-filter \(\mathcal F'\) would be above a lifted low row and preserved by each restricted pair. Pull it back to \(\widehat{\mathcal F}=\{A:A\cap Z^\iota\in\mathcal F'\}\). Inclusion and intersection commute with this map, so \(\widehat{\mathcal F}\) is proper, upward closed, above the full matching slices, and preserved by every big pair. This contradicts big coverage. Therefore \(\rho_{\rm small}\le\rho_{\rm big}\) at identical absolute thresholds, with no acyclicization loss.

Reparameterizing a fixed shift \(\beta'>\beta\) scales the exponent by \(\beta/\beta'\). This can move a direct \(\rho\) lower bound across nearby parameters only if the lower bound has enough exponent margin and is uniform in c and \(\beta\). The transfer is exact; the needed lower bound remains open.

### 2.167 C-119: The padding ray preserves thresholds but not the proof quantifier

For a rational scale lambda=p/q>1, ignored-input padding from n'=qt to n=pt preserves the exact absolute MCSP thresholds under (beta,c) -> (lambda beta,lambda c). A cover lower bound with exponent 1+eta at the smaller dimension becomes exponent (1+eta)/lambda at the larger dimension. Therefore the OPS premise is preserved only if the source result is uniform for every sufficiently small fixed shifted beta and has the margin eta>lambda(1+epsilon)-1. One fixed beta still yields one fixed beta after padding.

This identifies the geometry of the transfer: the ratio c/beta is preserved when the domain dimension changes, but the lower-bound exponent is contracted. A fixed shifted constant lambda c0>c0 corresponds to a smaller low class; hardness for that whole beta interval already implies hardness at c0 by monotonicity in the anchor set. Thus padding does not simplify the magnification hypothesis. It remains useful as an exact direct-rho comparison, without the cubic DAG loss. Rounded dimensions introduce constant-factor threshold changes and require an explicit robustness lemma; do not discard them as asymptotically harmless. The cover definition allows empty endpoints, and any restricted empty-side pair is vacuous and may be removed if using a nonempty-endpoint variant.

### 2.168 C-120: A hard residual can be hidden in one signature fiber

The gate-signature model has a sharp concentration example. Select kÃƒÂ¢Ã¢â‚¬Â°Ã‹â€ (1/2)log s2 circuit wires, including the output. The largest signature cell has at least N/sqrt(s2) truth-table positions. Alter a low table only inside this cell. There are exponentially many such completions, far more than the number of size-s2 circuits for every fixed beta<2/3. Since the two constant-on-cell completions remain low by testing the signature and overriding the output, some high completion must be nonconstant inside the cell. Patching forces Omega(s2/n) mismatches, all inside that one cell.

This teaches a specific failure mechanism: circuit hardness can be localized in one large fiber, so the number of mixed fibers cannot serve as a global potential. The challenge is the pair-dependent identity of that fiber and the cost of finding it with shared states. The result is a witness-concentration lemma, not a lower bound.

### 2.169 C-121: Common partitions explain the linear escape

If all low rows are constant on a fixed partition with m cells, and computing the cell label plus an arbitrary m-bit lookup costs less than s2, every high row must be mixed on one cell. Bob can select such a cell, Alice supplies the low row's bit there, and Bob scans that cell for the opposite high bit. The total shared rect-DAG has O(N) vertices. This generalizes the C-80 mixed-block router.

The full low-circuit class has no nontrivial common partition: each point indicator has O(n) gates and is low, so any cell containing two positions is split by some low row. The only partition respected by all low rows is the N-singleton partition, whose lookup is too large and whose cells cannot be mixed. Together with C-120, this separates two mechanisms: hard variation can localize inside one row-specific cell, and shared partitions make that cell easy to route; the unresolved resource is adaptive state reuse across different partitions.

### 2.170 C-122: Small row families share a linear-size suffix

Take any fixed r<=eta n low truth tables and partition coordinates by their r-bit output vector. If a high table were constant on every joint-signature cell, a circuit could compute the r row functions and then an arbitrary r-bit lookup, using r s1+O(r2^r)<s2 gates for eta<min(beta,c/3). Therefore every high table is mixed in a cell where all r low rows are constant. The C-121 router gives a rect-DAG with O(N) vertices for the entire fixed row family.

This rules out direct incompatibility arguments based on only O(n) anchors and their common fibers. It says nothing about the full low class: a row outside the tuple need not respect that partition, and separate grouping has exponential cost. The missing resource remains suffix reuse across many different anchor groups.
## Descriptor projection and shared-state cost (C-123)

The description length of each low table is not a shared-DAG size bound. If G maps circuit descriptions onto Y, the descriptor-input and truth-table-input mismatch relations have exactly equal minimum rect-DAG size: every state predicate pulls back along G, and a section restricts it back. The DAG's graph therefore sees the semantic promise, regardless of whether Alice can name one short witness.

Equivalently, the shared mismatch DAG has the size of a Boolean circuit separating Y from Z, with arbitrary behavior on the medium band. A universal circuit evaluates G(d)(x) for a supplied d, but Y membership is the projection ÃƒÂ¢Ã‹â€ Ã†â€™d ÃƒÂ¢Ã‹â€ Ã¢â€šÂ¬x[t_x=G(d)(x)]. Direct enumeration gives an exponential-in-description-length upper bound; no small separator follows from evaluation alone. The open resource is compression of that existential projection into globally reusable states.

Quantitative bridge: rho_promÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¤O(S_rect) and S_rectÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¤O(rho_prom^3/log rho_prom). A near-linear S_rect would rule out superlinear rho_prom; a separator lower bound must exceed roughly N^(3+3epsilon)/log N to force rho_prom>N^(1+epsilon) through the current compiler. This is a route clarification, not a separation result.
## Adjacent literature: representation and proof resource must match (C-124)

Conditional NP-hardness results for implicit MCSP use sampler circuits as inputs; this project's rect-DAG separator takes explicit truth tables. A sampler may need exponential expansion to produce the N-bit table, so the implication is not automatic. SoS degree lower bounds for one fixed hard table likewise do not provide a single shared separator for the full low/high promise. Treat these as possible sources of techniques, not as lower bounds on q or rho until a size-controlled transfer is proved.

### 2.171 C-125: Compose a partial-table map before unfolding the closure

The pair list is a cyclic monotone separator H_Q on signed table rails, with one counted AND per pair. A monotone map phi from a hard f into these rails can bypass the q-to-DAG conversion loss: if every YES image contains a full code for a low table and every NO image lies below a high-table code, then CycAnd(f) <= q+a, where a is phi's AND count. A consistent NO partial table with 2^d > |SIZE(s2)| unset completions has a high completion.

The OR-only argument assumes at least one YES input, as triangle does. Every NO graph with at most two edges forbids opposite rails from appearing together, so each coordinate has one globally fixed sign. Any YES image must contain that fixed low table, and the N rail predicates conjoined compute f with at most N-1 ANDs. The direct triangle-witness expansion costs O(r^3), above the known Omega(r^3/log^4(r)) cyclic lower bound. The transfer is valid but uninstantiated; finding a cheap variable-witness map is O-106. This is not a shared-DAG lower bound or a P-vs-NP proof.




### 2.172 C-126: Factor the map through the low-code extension predicate

Define LowExt_Y(u)=1 exactly when a full signed encoding e(w) of some low table w in Y lies below rail vector u. The C-125 hypotheses imply f(x)=LowExt_Y(phi(x)): on YES this is the low-code witness; on NO a low code below phi and a high code above phi would force the same full table, impossible. The NO high-completion requirement remains separate because H_Q has unconstrained values on medium tables. So the construction target is a low-AND monotone reduction to LowExt_Y plus a high completion for every NO input. NO images are consistent partial assignments; YES images may have extra conflicts beyond the selected low code. This explains why the OR-only obstruction has not yet generalized to circuits with AND gates. No lower bound or P-vs-NP consequence follows yet.

### 2.173 C-127: Witness diversity requires conflict support

If YES inputs x,y select different low table codes, then both full codes lie below phi(x OR y), because f is monotone and phi is monotone. Every differing coordinate must have both rails active at that join. Let S be the union of conflict coordinates over YES inputs, |S|=delta. All selected low tables then agree outside S. Enumerating at most 2^delta possibilities on S and reusing phi computes f with at most a+N+delta*2^delta AND gates. Thus CycAnd(f)-a <= N+delta*2^delta; any transfer establishing q>N^(1+epsilon) needs delta >= (1+epsilon)log2(N)-O(log log N). This is a necessary conflict-spread condition on the map, not a q lower bound. Next frontier O-108 is to exploit conflict incidence or construct a map meeting this threshold with high completions on NO inputs.

### 2.174 C-128: Local PRG bounds respect the promise but not sharing

The local-PRG method of Cheraghchi et al. extends to a low/high promise separator: uniform truth tables are high with overwhelming probability, while each generated table has circuit size at most s1 and must be accepted. Thus medium-band behavior does not invalidate the method. It gives formula/tree lower bounds N^(3 beta-o(1)) for de Morgan formulas when beta>1/3 and N^(2 beta-o(1)) for arbitrary-basis formulas or branching programs when beta>1/2. This does not reach the OPS all-small-beta range. More importantly, these lower bounds concern trees or branching programs, whereas C-75's rect-DAG keeps shared states; no conversion preserves that distinction with useful loss. The next task O-109 is a sharing-preserving transfer or a PRG argument against the rect-DAG model itself. This is a model-boundary result, not a q lower bound.

### 2.175 C-129: State reuse has a projection-volume price

In a rect-DAG node v, let K_v be the coordinates available at descendant output leaves, A_v the low rows, and B_v the high columns. A valid state cannot contain row and column tables with the same projection onto K_v. If A_v has r distinct K_v signatures, each signature excludes its entire high-completion fiber from B_v. Since a fiber has 2^(N-|K_v|) completions and at most M2=|SIZE(s2)| are low,

    |Z minus B_v| >= r(2^(N-|K_v|)-M2)

whenever the right side is positive. This turns cross-pair hull validity into a quantitative state constraint. It suggests charging the loss of high columns when states merge many low contexts. The missing proof is global: the same high tables may be excluded at many nodes, and adaptive routing can shrink B before merging. Hence this is a structural non-shareability lemma, not yet a DAG or fusion lower bound. The plain relation also has an Omega((1-beta)n) communication-bit lower bound from disjoint high supports, but this does not challenge the existing linear-in-N fusion floor. See C-129/O-110.

### Update 2026-09-26 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Endpoint support versus shared routing

C-131 makes the current shared-DAG obstacle more precise. For each fixed low table w, every coordinate set S with 2^(N-|S|)>M2=|SIZE(s2)| has a high completion z agreeing with w on S. Therefore a correct mismatch protocol must make at least N-log2(M2)=N-N^(beta+o(1)) distinct output coordinates reachable for each individual w. This is an endpoint support condition; it does not count the internal states needed to route each z to a valid output. It only bounds distinct coordinates (at most N for a fixed w) and does not rule out a need for many context-specific leaf vertices.

The natural bottleneck width at a node is the minimum set of descendant output coordinates that hits every high column in that node. At the root this width is already N-o(N) for every low row. Consequently, the recent bottleneck-counting proof for Search-BPHP cannot be transplanted by simply mapping rows to the first node above a width threshold: that rule assigns all rows to the root. That proof's per-node bound uses pigeonhole collision structure and triangle slices. Our C-129 projection-volume constraint is a possible replacement ingredient, but C-130 proves that raw excluded-volume summation double-counts one high table at Omega(N) reachable states.

**Updated model principle:** endpoint output diversity is nearly maximal already; the missing complexity is the routing topology that preserves valid rectangles while letting one DAG serve all low rows. A useful new invariant must measure first divergence along chosen paths and bound how many low/high contexts a state can absorb. No such invariant, superlinear rect-DAG lower bound, or P-vs-NP proof has been obtained.

### Update 2026-09-26 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Width bands do not control state capacity

C-132 tests the edge-crossing repair to C-131. Rectangle coverage implies that for each fixed row, the parent width h is at most the sum of widths of its children containing that row, so one child retains at least half. This supplies a path across width scales. But width alone does not bound how many rows can cross at one node. Take I of size 3N/4, let P be the low-table restrictions to I, and let B consist of high tables with I-prefix outside P. The valid rectangle Y x B has outputs confined to I and has width between N/2 and 3N/4 for every low row, while the root width is N-o(N). A root split can make this rectangle a child; a width-preserving route can send every row through that same in-band state.

The new constraint is therefore sharper: a capacity argument must use the structure of the high columns excluded by a state (here, complete fibers over low prefixes), not merely the number of output coordinates needed to hit its remaining columns. The node's possible row set can be all of Y even at a middle width scale. C-130 also shows raw volume charges overlap across off-path states. No global charging invariant is currently established.

### 2.176 - Local surjectivity falsifies the interval-restriction universal DAG

The C-78 router shares a state by the pair (dyadic interval I, exact restriction u of a low table to I). That state key has a serious structural cost. On any k truth-table coordinates, every 0/1 pattern is realized by a low circuit for k up to a constant multiple of s1/n: use an OR of point minterms, with O(kn) gates. Thus the low language is locally surjective at this scale.

At a dyadic scale k=Theta(s1/n), C-78 must contain (N/k)2^k distinct states. Different patterns have disjoint nonempty row sides; different blocks have different row sides because any joint pattern on their union is also low-realizable. Hence this particular router has 2^(Omega(s1/n)) = 2^(Omega(N^beta/n^2)) states and cannot be a near-linear universal DAG.

The deduction is architectural. A general rect-DAG need not preserve exact interval prefixes; it can choose semantic row subsets, arbitrary descendant coordinate sets, and column filters before merging. So local richness only yields a universal-DAG lower bound after a routing theorem forces those contexts to appear. C-132 warns that width does not force them: a single all-row rectangle can sit at intermediate width after filtering columns by low prefixes. The open object remains the *residual rectangle relation* and how its compatible states can be reused, not the count of possible restrictions in isolation.

**Research consequence.** Retire C-78 as a candidate near-linear universal construction. Any replacement must avoid storing exact short-block patterns, perhaps by a different aggregate statistic; any lower-bound attempt must prove that a general protocol cannot make that aggregation without admitting cross-pairs whose required mismatch lies outside its descendants. No q lower bound or P-vs-NP result follows. See C-133/O-113.

### 2.177 - Restriction richness is not enough; the residual columns matter

C-134 isolates a trap in the C-133 direction. A low subfamily can realize every pattern on a block I and contain 2^k rows, while still admitting an O(N)-state mismatch DAG. If all those rows are zero outside I, every high table must have a 1 outside I, and a Bob-side scan finds a mismatch without identifying the row.

So the required non-shareability invariant cannot be a count of low projections alone. It must pair each state's row-side profile with the residual high-column set and account for shared witness regions that bypass the detailed row contexts. This is not a small router for the full low class; the full Y has no large fixed common zero region. The active target remains: force a superlinear state lower bound for the full Y x Z relation or attack rho_prom directly, while preserving the cubic-or-better transfer loss. See C-134/O-114.

### 2.178 - Small row-variation support is an easy state

For a row family A, V(A) is the set of truth-table coordinates on which its rows vary. The coordinates outside V(A) carry a common pattern c. Starting from any w0 in A, changing only r coordinates costs O(nr) additional circuit gates: mask w0 off those coordinates and OR in the requested point minterms. Hence if |V(A)| is below about (s2-s1)/n, every completion of c is still non-high.

It follows that every high table must disagree with c somewhere outside V(A). A protocol can scan those common coordinates on Bob's input alone and return a mismatch valid for every row in A. Such a rectangle has an O(N)-state router even when A contains many low tables. For OPS, the cutoff is Theta(s1). This subsumes the supported-block example.

The global obstacle is now explicit: the root has V(Y)=[N], while subprotocols may reach small-variation row sets that are easy locally. The count and sharing pattern of those states, and the residual columns on large-variation states, are what a lower bound must control. Small variation is an upper-bound criterion; large variation is not a hardness theorem. See C-135/O-115.

### 2.179 - The mismatch relation has abundant witnesses but costly deterministic history

Patching a low truth table w at r coordinates costs O(nr) extra gates. With the OPS gap this means every high table z differs from every low w on d+1=Theta(s1) or more positions. So each pair has many valid signed mismatch labels. The 2N label rectangles yield a fractional cover of cost 2N/(d+1), and a public-coin protocol can sample coordinates until it finds a mismatch in expected O(N/d) bits. A fixed coordinate set cannot do the same universally: any set T leaving more than log2|SIZE(s2)| positions free has a high completion agreeing with a chosen low table on all of T.

This contrast locates the current difficulty in deterministic routing. A randomized query can forget earlier equal answers because its next coordinate is fresh; a deterministic rect-DAG must maintain a rectangle after every history, and histories with different equal bit patterns generally cannot be merged without admitting invalid cross-pairs. The label-conflict fooling-set method is also capped at O(N/d), since each pair already has at least d+1 labels among 2N. These are precise method ceilings, not a lower bound for arbitrary DAGs: some incompatible rectangles may have pairs with common labels, and global state reuse may still be possible. New lower-bound work must charge the routing histories; new upper-bound work should try to compress them. See C-136/O-116/Q96.

### 2.180 - Cycles do not permit joint-bit rectangle merges

A one-state-per-coordinate cyclic scanner seems to solve any unequal pair of N-bit strings: output on a mismatch, and send both equal outcomes to the next coordinate. Its transition after equal bits is the union (A0 x B0) union (A1 x B1). This is usually not a rectangle, because the product hull also contains the cross pairs. So the O(N)-state object is a joint-input transducer, not a standard rect-DAG. A cycle changes termination, not the requirement that each shared state represent a rectangle.

For the fixed-order repair that preserves the equal-prefix pattern, every pattern on k=Theta(s1/n) coordinates has a low extension and a high completion. It therefore creates 2^k distinct nonempty continuation rectangles. This confirms C-133 for the scan architecture while leaving open whether an adaptive semantic DAG can merge contexts by another invariant. The q-state closure game has its own monotone activation semantics and cannot inherit a bound from a generic pair transducer without a proved reduction. See C-137/O-117/Q97.

### 2.181 - Counting gives high tables with sparse supports

There are M2<=2^(O(s2 log(s2+n))) tables of circuit size at most s2. A Hamming sphere around zero of weight r=A s2 has binom(N,r) members; choosing A large makes this exceed N M2. A random partition of the table coordinates into r-blocks therefore has a choice in which every block indicator is high. Against the low zero table, the block indicators give Omega(N/s2) disjoint output-label sets.

This improves the elementary deterministic communication lower bound to (1-beta)n-O(1), but its leaf bound N/s2 remains below the existing Omega(N) rect-DAG floor. A random weight-r perturbation of any low table is high with probability 1-o(1), but each output coordinate is selected with probability r/N, so direct leaf-mass arguments recover only N/r leaves. C-136's label-conflict ceiling is O(N/s1), only a factor Theta(n) above the construction. Output scarcity will not produce the required superlinear state bound; the unresolved variable remains global routing. See C-138/O-118/Q98.

### 2.182 - Fusion is a ranked cyclic rectangle search, not an ordinary DAG

For a successful q-rule fusion cover, associate to each rule i the activation rectangle R_i=(Y intersect X_i) x (Z minus X_i). Empty-carrier rules cover the root Y x Z. At a valid pair (w,z) in R_i, one endpoint side is absent from z's least closure. The same side is present for w, so choose a support that witnessed its presence at i's first activation. A literal support gives an actual mismatch; an earlier carrier support leads to R_j, with first-activation rank tau_j(w)<tau_i(w). Each branch is the product of a w-local support condition and a z-local absent-side condition. Thus the protocol preserves rectangles, can have cycles in its static support graph, and nevertheless terminates on each fixed pair.

This is the exact shared-state object C-75 was pointing toward: q rule states (plus at most 2N output terminals) and O(q^2+qN) possible support arcs. It is a ranked cyclic rectangle game induced by the special C-74 dual-rail/containment recurrence. It is not Sokolov's standard Boolean game, which is globally acyclic and binary-outdegree; nor is every cyclic rectangle game automatically a fusion cover. The primary literature confirms the boundary: Sokolov's Boolean game and PLS graphs are acyclic ([definitions and conversion](https://eccc.weizmann.ac.il/report/2016/202/revision/1/download)); the exact fusion characterization is cyclic intersection complexity ([Cavalar-Oliveira, Theorem 30](https://arxiv.org/abs/2503.14117)).

Layering by activation-rank threshold creates q^2 rule states; binary routing through up to q+2N supports costs O(q^2(q+N))=O(q^3) at q>=N-o(N). This explicit simulation exposes rank unrolling and support selection as the two costs, but does not improve the best O(q^3/log q) compiler. The live opportunity is a context-preserving shared router for different rank thresholds; no such construction or lower bound is known. C-132 and C-135 show why state width and row variation alone cannot force duplication, while C-137 shows a joint-bit merge is not a legal rectangle state.

**Logic correction for model comparisons:** by vertex count, every tree is already a DAG, so minimum DAG size is at most minimum tree size. Small communication depth can coexist with exponentially many tree vertices; a c-bit binary protocol has at most 2^(c+1)-1 vertices. Thus only the bits-versus-graph-size gap can point toward a large shared-DAG target; small tree node count but large DAG node count is impossible. The unique-output toy relation (Alice's a in [M], Bob fixed, sole valid output a) has log M communication bits and M required leaves, but Gap-MCSP's dense mismatch labels block this leaf-count trick. No superlinear bound or P-vs-NP proof follows.

### 2.183 - Input-dependent rank can be proof-path overhead

The abstract recurrence x1=(s1 OR x2) AND c, x2=(s2 OR x1) AND c has two mutually supporting states. If s1=1,s2=0,c=1 then x1 activates first; if s1=0,s2=1,c=1 then x2 activates first. Its least fixed point is nevertheless x1=x2=c AND (s1 OR s2), which has a constant-size acyclic circuit. Thus q^2 state duplication in a rank-layered C-75 witness simulation need not reflect separator circuit size; another circuit can forget the path and compute the same output directly.

This is only an abstract monotone recurrence. It has not been realized by legal fusion endpoints or reduced to Gap-MCSP. Its use is to kill an invalid inference: lower-bounding a chosen rank-unrolled proof path does not lower-bound every separator. A viable non-shareability theorem must survive output simplification and alternative search paths. See C-140/O-117/Q100.

### 2.184 - The rank-reversing cycle is realizable, but its output is easy

The two-state C-140 system has a legal literal-slice endpoint realization on Gamma={0,1}^5. Let A={a=0}, B={b=0}, C={c=1}, P=C intersect(A union B), with distinct p1,p2 outside C. Set E1=A union P union {p1,p2}, H1=C union {p1}; E2=B union P union {p1,p2}, H2=C union {p2}. Then T1=P union {p1}, T2=P union {p2}; each carrier supports the other on its E endpoint, while marker asymmetry blocks cross-support on H endpoints. The only seeds are A,B,C, so after omitting self-supports the recurrence is x1=(A OR x2) AND C and x2=(B OR x1) AND C. Its least solution is x1=x2=C AND (A OR B), and the activation order reverses between A-only and B-only rows.

This closes endpoint realizability for the local cycle fragment, but not for a successful cover: both T_i are nonempty and there is no low/high separator. The output is also an easy acyclic formula. Thus genuine cycles in legal endpoints do not imply a hard separator, and q^2 rank layers remain a path-simulation cost rather than a lower bound. The new target is to embed this behavior into a successful promise separator with a proven obstruction to every alternative small output circuit. See C-141/O-117/Q101.

### 2.185 - A successful cycle can be a witness artifact even in a cover

Use four-bit anchors (a,b,c,f), low set Y={(0,1,1,0),(1,0,1,0)} and high universe Z={zA=(0,1,0,0), zB=(1,0,0,0), zC=(1,1,1,1), p1=(1,1,0,1), p2=(1,1,0,0)}. Three legal endpoint pairs are E1={zA,p1,p2}, H1={zC,p1}; E2={zB,p1,p2}, H2={zC,p2}; E0={p1}, H0={p2}. Their carriers are {p1},{p2},empty. Literal slices give seeds a=0 on E1, b=0 on E2, c=1 and f=1 on H1, c=1 on H2, and no seeds on the root endpoints. The support graph has a genuine 1<->2 SCC and separate edges to the empty root.

The least closure equations reduce to x1=(a0 OR x2) AND (c1 OR f1), x2=(b0 OR x1) AND c1, and x0=x1 AND x2. On the two low anchors the order is 1 then 2, and 2 then 1; both activate x0. Each of the five high points leaves x0 inactive. So this is a successful finite-promise cover with input-dependent cyclic ranking. Nevertheless h=c AND (NOT a OR NOT b) is a constant-size separator.

This is stronger than an abstract cyclic equation or an unsuccessful fragment: the phenomenon exists inside a valid cover. It also settles why rank-layer lower bounds alone are inadequate. The static support SCC can force duplicated proof histories, while a different separator ignores those histories. To advance the OPS route, prove a non-shareability property for all output circuits/separators, not just for the Q chosen by the cover. See C-142/O-117/Q102.

### 2.186 - Quadratic rank-profile diversity can coexist with linear output

Scale C-142 to q states: each has carrier {p_i}, E_i contains p_i and p_(i-1) plus its seed singleton z_i, and H_i contains p_i plus a shared c-control point r. An empty root pair uses p1 and p2. Low anchors w_j activate only seed j with c=1; high z_i have c=0 despite matching seed i, marker points have c=0, and r has c=1 but no seed. Balanced tag bits ensure no accidental generator containment. Thus the q-rule SCC is a directed cycle; low anchor j activates it in cyclic order j,j+1,..., and every low reaches the empty root while all high points avoid it.

All activation ranks occur: tau_i(w_j)=1+((i-j) mod q). The direct layered states R_(i,s) have q(q-1)+1 distinct rectangles, since s<q gives q different cyclic windows of size s and s=q gives one common Y x Z state. Still h=c AND (OR_i t_i) separates the promise with O(q) gates. This is a successful cover family showing that rank-profile count is not a lower bound on the output DAG. Any useful non-shareability theorem must use the actual OPS promise to defeat alternative separator circuits; see C-143/O-117/Q103.

### 2.187 - The q-cycle witness list is deletion-minimal, but rho is one

For the C-143 high universe U={z_i,p_i:i in [q]} union {r}, take E*={z_i} and H*={r}. The low anchor w_i has its t_i=1 slice exactly {z_i} and its c=1 slice exactly {r}, so this one empty-carrier pair derives empty on every low anchor. For a high point other than r, any matching t_j=1 singleton is {z_j}, distinct from {r}; matching t_j=0 and c=0 slices have size 2q, and matching tag slices have size q or q+1. Its matching c=1 slice is absent. Thus it cannot generate H*. At r, every matching slice contains r and therefore cannot fit inside E*. The same promise has rho=1.

The q-cycle-plus-root list is deletion-minimal internally: removing a cycle rule strands its uniquely seeded low anchor, and removing the root leaves no empty carrier. But this is not global minimality; a different semantic pair bypasses every state. This corrects the interpretation of C-143: its Theta(q^2) rank-layer rectangles are a property of one chosen witness protocol, against an optimal one-pair cover. That is a strong counterexample to charging proof-path size to rho, but it supplies no lower-bound evidence about optimal cyclic covers or Gap-MCSP. Any rank-based lower bound must control alternative endpoint choices, not just make the selected list irredundant. See C-144/O-117/Q104.

### 2.188 - OPS seed states start broad on the high side

Let M2=|SIZE(s2)|=2^o(N). Every cylinder fixing two distinct truth-table bits contains at least 2^(N-2)-M2 high tables. For any low anchor w, a successful least-fixed-point closure must activate at least one rule in round one; otherwise zero remains a fixed point. Both sides of that rule must be seeded by literal slices matching w. The common high cylinder lies in its carrier T_i=E_i intersect H_i, so T_i contains at least 2^(N-2)-M2 high tables. Each such high table also activates state i at round one.

This is a structural difference from the finite q-cycle toy: its two seed slices have empty intersection on its sparse high universe and the resulting carrier is a singleton. In OPS, early states cannot isolate low anchors; they are shared with a constant fraction of high inputs. A future lower bound must charge what happens later, when support dependencies route low anchors to empty while avoiding those high columns. The immediate lemma is local and does not strengthen q>=N-o(N); high-side regions at different states can overlap heavily. See C-145/O-119/Q105.

### 2.189 - A seed cylinder drops one recurrence state; cofactor costs do not add

For a successful OPS closure, a low anchor has a round-one seed state from C-145. Fix the one or two literal coordinates that seed it. On this entire cylinder the state is active for every anchor, so replacing it by the constant 1 yields a separator recurrence with one fewer AND-state. This is an induced-recurrence cofactor fact, not automatically a cover of the restricted promise: restriction may create new endpoint-containment edges.

The tempting next stepÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âsum the restricted lower boundsÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Âfails on the exact-one promise. With r-bit tables, low inputs the weight-one vectors and high inputs all other vectors, the high side is two-coordinate dense. A prefix/suffix monotone circuit gives rho=O(r); a fixed one-hot low anchor needs all r literals, giving rho>=r-1. Yet each of the binom(r,2) cofactors fixing two bits to zero is another exact-one promise on r-2 bits and costs at least r-3. Thus a linear-size global construction can serve quadratically many hard cofactors. OPS progress needs a sharing obstruction tied to the full low-circuit language, not just dense high side or local cofactor hardness. See C-146/O-120/Q106.

### 2.190 - Shared-DAG complexity is a promise-separator problem, not a description-length problem

For Y=SIZE(s1) and Z=(SIZE(s2))^c, signed mismatch is total on Y x Z. A successful fusion list Q adds a stronger witness output (the rule/support path); that relation is total exactly when Q covers every low anchor. Do not conflate them.

A standard Sokolov Boolean game has an acyclic graph of out-degree at most two. Each vertex's arbitrary Alice predicate and Bob predicate define a rectangle; these local computations are free in the graph-size measure. Therefore replacing a low truth table by one of its short circuit descriptions does not reduce the minimum DAG size: lift predicates through the description map, or restrict along one representative description per low table. The hard resource is which product rectangles can be reused, not how short one row's code is.

The exact current bridge is rho_prom=D^circ_cap and rho_prom<=SepCirc(Y,Z)=Theta(S_rect)<=O(rho_prom^3/log rho_prom). A small O(N^(1+o(1))) mismatch DAG would imply a near-linear fusion-cover upper bound and kill this superlinear-cover route. A DAG lower bound transfers to rho only above the cubic/log scale N^(3+3epsilon)/log N unless the compiler improves; a direct cyclic q lower bound avoids that loss.

Current failed shortcuts: q activation states can form a genuine cyclic witness graph but not necessarily an acyclic DAG; rank layers can be bypassed by another separator (C-143/144). A state merge must preserve the whole product hull (C-110), and the equal-prefix coordinate scanner needs exponentially many contexts (C-137). These do not rule out every adaptive DAG. The open task is an actual-promise non-shareability lemma or a near-linear universal DAG; neither has been proved. The primary-source comparison is in bridge C-147. See O-121/Q107.

### 2.191 - Local pseudorandomness gives a tree bound but does not measure reuse

For OPS thresholds s1=N^beta/(c n), s2=N^beta, the CLKM local-PRG promise-separator argument is rigorous only for fixed beta>1/3. Their De Morgan formula lemma is stated for size t>=N and has locality lambda(t)=t^(1/3)2^(O((log t)^(2/3))). Above beta=1/3, padding to N first gives lambda(N)<=s1, and the usual contradiction yields formula size t>=N^(3 beta-o(1)) despite arbitrary medium-band labels. For beta<=1/3 the cited lemma cannot start: lambda(N)>s1, and it gives no lower bound in the active sufficiently-small-beta range.

This is a promise-separator application of the local-PRG method only when beta>1/3, outside the active magnification range. At beta<=1/3 the source lemma does not yield a formula bound. At every beta, formula size does not lower-bound S_rect or rho_prom without a separate sharing-sensitive transfer. C-148/C-149 is calibration only; O-121 remains open.

### 2.192 - The first excluded active carrier gives a mismatch, but not yet a reusable state

For a successful Q and a low/high pair (w,z), order the rules active on w by first activation round, breaking ties by index. At least one active empty-carrier rule is in this list, so some carrier omits z. Choose the first such carrier T_i. If z misses E_i and E_i were supported by an earlier active T_j subset E_i, then z would also miss T_j at an earlier rank, contradiction. Thus the missed endpoint is seeded by a matching literal slice; the symmetric case applies to H_i. That literal is true on w and false on z, so it gives a valid output coordinate. This canonicalizes the witness without following Q's cyclic support path.

The tempting scan is not automatically a rect-DAG. After t accepted carriers the residual set is P_t(w)=intersection of the first t active carriers, and the column residual can differ with w. Merging rows with different P_t values takes a product hull and may admit pairs that should have stopped at an earlier missing carrier. C-142 gives a concrete legal fusion toy where this happens; its alternative one-pair cover shows that this path-specific failure says nothing about the optimum. A rect-DAG proof needs multiple residual contexts or a proof that all cross-pairs remain solvable. No OPS lower bound on this residual relation is known, and another separator can bypass Q. Record it as a candidate non-shareability invariant, not as a lower bound on S_rect or rho. See C-150/O-122/O-121.

### 2.193 - Canonical witnesses can be much harder than finding any witness

Let A_S=[k]\\S and B_T=T union {k}, S,T subset [k-1]. Their intersection is {k} union (T\\S), so a witness always exists. Requiring the least common element makes every diagonal pair output k. A rectangle labelled k cannot contain two diagonal pairs: the rectangle also contains both cross-pairs, and one has a common element below k. Thus at least 2^(k-1) k-labelled leaves are needed. Yet if any common element is accepted, constant output k solves the relation. The two search problems have identical inputs and wildly different rectangle-DAG complexity. This demonstrates that a canonical selector lower bound is not a lower bound for a multivalued search task.

**Transfer rule.** For a given rect-DAG solving a multivalued relation, if its selector h is constant on every leaf rectangle, relabel leaves and obtain an h-DAG at unchanged size. A decoder from each valid output label to h is a sufficient global condition. C-150's closure selector returns a carrier/literal witness, while Gap-MCSP accepts any signed mismatch and omits the carrier index. No such decoder or all-separators leaf-homogeneity theorem is known. Therefore the selector is a candidate proof aid only; O-123 asks whether its complexity can survive output projection. The toy establishes no OPS lower bound.

For this toy, unique minimum has deterministic communication Theta(k), since there are 2^(k-1) k-labelled diagonal leaves and Alice can send S followed by Bob's O(log k)-bit answer. Its rect-DAG and protocol-tree sizes are 2^(Theta(k)); any-common has zero communication and one leaf. These bounds apply to acyclic rectangle semantics. They do not transfer to loop circuits unless their terminal reach sets have the same rectangle property.

### 2.194 - A successful closure can have selector-mixed mismatch leaves

C-142 supplies a concrete counterexample to generic selector transfer. Both low anchors have c=1, while p1 and p2 both have c=0, so the full rectangle Y x {p1,p2} is solved by the single output ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œmismatch on c.ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â But C-150's first-excluded carrier is state 2 on p1 and state 1 on p2, regardless of which low row is used. The selector matrix is [[2,1],[2,1]], so the valid output rectangle mixes selector fibers. A full finite rect-DAG can route that rectangle to a c-labelled leaf and handle the other high points separately. Thus successful fusion and rectangular correctness do not force leaves to preserve the selected support path. This closes the generic O-123 route; only an OPS-specific subpromise could revive it. No OPS bound follows.

### 2.195 - Colourful-sunflower lifting offers a DAG lower-bound template

The 2025 theorem ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œLifting with Colourful SunflowersÃƒÂ¢Ã¢â€šÂ¬Ã‚Â proves that if S is a search relation over Sigma^n with subcube-DAG width w(S), then any triangle-DAG (therefore any rect-DAG) for S composed with the m-bit Index gadget has size at least (m/(A|Sigma|w(S)log(mn)))^w(S). This is directly about shared DAG size and may yield a strong lower bound when paired with a wide unsatisfiable-CSP search problem.

The project could use it only after a concrete reduction: Alice's lifted input x must map to a table in SIZE(s1), Bob's y to a table outside SIZE(s2), and every mismatch leaf on the pulled-back rectangle must decode to a CSP constraint falsified throughout that rectangle. If decoding refines leaves, its vertex overhead must be charged. Also verify the truth-table length N and source-side cardinalities. The theorem alone is not an OPS or P-vs-NP lower bound. With current rho_prom-to-S_rect compiler loss, transferred S_rect must exceed N^(3+3epsilon)/log N to imply rho_prom>N^(1+epsilon); a direct cyclic-cover transfer would avoid that loss. See C-154/O-124.

### 2.196 - RETRACTED: the partial-Index code obstruction was false

The earlier argument incorrectly imposed codeword equality on inputs outside the partial relation's legal domain. For SearchOR composed with Index, the legal inputs satisfy y_x=1. On those inputs, Alice's code a(x)=0^m and Bob's code b(y)=y always mismatch at coordinate x. Since the one-block SearchOR relation has the sole output 1, every mismatch coordinate decodes to a valid output. The claimed direct-coding obstruction is withdrawn; it cannot be used against C-154/O-124.

### 2.197 - Total mismatch encodings are paired cut covers

For a total relation R on X x Y, partywise r-bit codes a(x), b(y) with a fixed decoder work exactly when, for every coordinate t, both cross rectangles X_t^0 x Y_t^1 and X_t^1 x Y_t^0 carry fixed valid output labels, and these rectangles cover X x Y in total. Here X_t^u={x:a_t(x)=u} and Y_t^u={y:b_t(y)=u}. This is an exact characterization of direct coordinatewise encodings. A plain monochromatic rectangle cover is weaker because each bit creates both opposite cross rectangles. It gives no lower bound for lifted CSP search or OPS by itself.

### 2.198 - Cyclic sharing needs a termination invariant

An O(N)-vertex cyclic mismatch router can be faked by making every internal state the full rectangle Y x Z, giving each state one edge to a signed mismatch leaf and one edge to the next state in a cycle. Every promised pair has a finite path to some valid leaf. But every pair also has an infinite continuation path, so existential finite-path semantics trivialize cyclic search. This is not a standard rectangle-DAG or the fusion closure game. Any cyclic shared-state model must impose a well-founded, input-sensitive progress measure; C-139 supplies one for a successful fusion cover via decreasing activation rank.

For a binary rectangle node, if its rectangle A x B is covered by two child rectangles, then at least one child preserves all of A or all of B. Otherwise choose a row outside the first child's row side; coverage forces the second child to contain all of B. This elementary product-cover fact lets a party choose a valid successor locally, but it does not bound how many residual rectangles a DAG needs. The open target remains a state-reuse bound on the actual low/high mismatch relation, with all quantitative losses in the bridge report kept active.

### 2.199 - The local rectangle trichotomy is known; the global charge is open

The stronger C-158 trichotomy was already explicit in Sokolov's Theorem 3.2 proof: for a parent rectangle covered by two child rectangles, either the parent row side lies in both child row sides (AND), its column side lies in both child column sides (OR), or one child contains the parent (copy). This is exactly how a Boolean communication game reconstructs a circuit. C-158 is therefore not a novel non-shareability lemma.

For the C-75 promise relation, the same induction turns an acyclic rect-DAG into a Boolean separator circuit: signed-mismatch leaves become literals; the three internal cases become AND, OR, or copying. This verifies the established reverse bound rho_prom<=O(S_rect). The live challenge is global: lower-bound how many distinct separator states survive arbitrary circuit sharing. C-129's local excluded-column bound cannot simply be summed, as C-130 and C-132 demonstrate. See C-159/O-126.

### 2.200 - C-160: local cylinder data do not force a superlinear DAG

Set a=floor(N^beta/log N), b=floor(N^beta), take low rows of weight at most a or at least N-a, and high columns from the middle band b<weight<N-b. The low class has 2^Theta(N^beta) members on a logarithmic scale; the non-high class has 2^Theta(N^beta*log N). Every pattern on at most a coordinates occurs among low rows, every low/high pair differs by Theta(N^beta), the radius-a neighborhood of the low class is non-high, and every subcube larger than the non-high class contains a high table. The low set is complement-closed; every coordinatewise Boolean recombination of up to floor(b/a)=Theta(log N) low rows remains in the non-high band. These reproduce the generic counting, local-surjectivity, patch-stability, cylinder, and compositional closure facts used in C-129/C-133/C-135/C-136.

Yet the separator accepting exactly weights at most a or at least N-a has a fan-in-two circuit of size O(N log N), by counting the input ones with a binary accumulator. Hence its mismatch relation has an N^(1+o(1)) rect-DAG and its analogous active fusion cover is O(N log N). This calibration proves that C-129's local state-volume inequality plus the known AND/OR/copy trichotomy cannot yield a superlinear lower bound using only those generic promise statistics. It does not give a small DAG for actual Gap-MCSP. O-126 must use finer structure of the SIZE(s1)/SIZE(s2) classes or directly exploit their ranked cyclic closure; what that feature is remains open.

### 2.201 - C-161: affine richness is still not enough

Augment the C-160 promise with every affine truth table on n input bits and include all tables within Hamming distance a=floor(N^beta/log N) of an affine table in the non-high set. This adds only 2N low tables and at most 2N times a radius-a Hamming ball of non-high tables, so the logarithmic class-count scales remain 2^Theta(N^beta) and 2^Theta(N^beta log N). The promise now includes balanced low rows, input-affine symmetry, and their patch neighborhoods.

The added non-high region remains easy to recognize. For a table u, the nearest affine function has distance \((N-\max_\ell|\widehat{(-1)^u}(\ell)|)/2\). A fast Walsh-Hadamard transform computes all coefficients with O(N log^2 N) Boolean gates, including the O(log N)-bit arithmetic. Together with the two Hamming-tail tests this gives an N^(1+o(1)) separator and active fusion cover. Thus a large balanced orbit or affine invariance still does not supply a superlinear DAG lower bound.

C-161 does not retain C-160's closure under arbitrary recombination of Theta(n) low rows: the n input literals form a separating basis, and composing them with an arbitrary size-s2 circuit ranges over the original size-s2 circuit class. There are 2^(n^2+O(1)) ordered bases from GL(n,2); each basis consists of n low linear forms and computes an invertible relabeling of the N input points. Any combiner g of size at most s2-O(n^2) composed with such a basis still has size at most s2. The candidate frontier is whether the residual rectangles induced by these many overlapping bases force state reuse costs in every separator. C-122 handles each family of at most eta*n low rows by an O(N) router for sufficiently small eta, so one small anchor family does not suffice. No such lemma is proved; see O-126/Q120.
### 2.202 - Short descriptions do not settle shared-DAG reuse

For the C-75 mismatch relation on low truth tables Y and high tables Z, a rect-DAG is exactly a circuit for some separator of Y from Z. If low tables are represented by descriptions d with G(d)=w, lifting row sets by G^{-1} and restricting along a section YÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢D preserve the number of DAG states exactly. A short description therefore makes ordinary communication cheap, but does not shrink shared-DAG complexity by itself. Universal evaluation of G(d)_k and z_k still asks a joint mismatch question; that predicate is not generally a rectangle.

The q-pair cover itself is q=ÃƒÂÃ‚Â_prom=DÃƒâ€šÃ‚Â°_cap. It gives a q-state cyclic witness router with input-dependent decreasing activation rank. Cycles can occur in its static graph, so standard acyclic simulation retains the known losses: AND-only separator size ÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¤qÃƒâ€šÃ‚Â² and standard rect-DAG size O(qÃƒâ€šÃ‚Â³/log q). In reverse, an L-node mismatch DAG gives ÃƒÂÃ‚Â_promÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¤O(L). Hence a direct q>N^(1+ÃƒÅ½Ã‚Âµ) bound is ideal; separator targets are >N^(2+2ÃƒÅ½Ã‚Âµ) in AND-only size or >N^(3+3ÃƒÅ½Ã‚Âµ)/logN in standard DAG size.

The many-bases idea must quotient truth tables from descriptions. There are 2^(nÃƒâ€šÃ‚Â²+O(1)) ordered linear bases but only N distinct linear functions among their component rows. A table g(Ax) costs size(g)+O(nÃƒâ€šÃ‚Â²), so bases whose compositions fit the budget merely produce members of Y. The affine subfamily versus actual Z is easy: Walsh-Hadamard testing detects affine truth tables in O(N logÃƒâ€šÃ‚Â²N) gates. Thus neither basis count nor affine symmetry is a state lower bound. A non-shareability theorem would need a new cross-state incompatibility across nonlinear compositions and arbitrary valid mismatch leaves. No such theorem or superlinear bound is known. See C-162 / bridge section 88.

Composition closure at the \(s_2\) threshold is not automatically usable: if the composed table is not in \(Y\), it may be in the medium band, which is absent from the promise relation and has unconstrained separator labels. Restrict the candidate to low-budget compositions unless a separate medium-extension theorem is proved.

### 2.203 - C-163: mismatch distance limits output-decoder capacity

The C-136 patching argument gives a minimum Hamming distance Delta=Theta(N^beta/n) between every low table and every high table. A reduction into the C-75 mismatch relation therefore cannot treat one coordinate disagreement as one arbitrary source answer: every encoded pair produces at least Delta distinct mismatch coordinates, and each must be decodable to an answer valid on that source pair.

For a total source relation R, write chi_out*(R) for the minimum fractional cover of all source pairs by valid-output sets. If each signed mismatch type can be refined into at most r output-labelled terminals, the 2N types provide at most 2Nr output incidences in total. Weighting each incidence by 1/Delta gives
chi_out*(R) <= 2Nr/Delta = O(r n N^(1-beta)).

Thus high fractional output-cover complexity forces large decoder refinement. For a unique-answer relation with M used labels, r >= M Delta/(2N). A relation whose answer is Alice's k-bit input, with k approximately (1-beta/2)n, already requires r=Omega(N^(beta/2)/n), even though Alice knows the answer and all her source inputs can be mapped to O(n^2)-size low truth tables. The output alphabet itself fits among 2N mismatch types; the obstruction is the multiplicity demanded by the Hamming gap.

This is a feasibility condition on coordinatewise mismatch reductions and bounded decoders, especially O-124/O-125. It does not lower-bound the target DAG or fusion cover, and it does not address reductions that bypass mismatch labels. Before investing in a source relation, compute its fractional output-cover number and compare it to the available 2Nr/Delta decoder budget. See bridge section 89.

### 2.204 - C-164: Index rectangles require decoder refinement

For the lifted graph-pigeonhole search relation, Alice holds pointers x in [m]^k and Bob holds y in [d]^(mk); output (p,q) is valid when the selected neighbors Gamma(p,y_(p,x_p)) and Gamma(q,y_(q,x_q)) coincide. Under uniform product inputs, any rectangle on which the distinct pair (p,q) is valid throughout has probability at most 1/(m^2 d), for a simple degree-d graph.

The bound comes from projecting Alice's rectangle to S, the set of pointer pairs (x_p,x_q), and making Bob satisfy the corresponding partial-matching constraints on every array-position pair in S. If the constraint graph has rank R=sum(vertices-components), the Bob-side measure is at most d^(-R). The number of edges in the graph is at most d^(R-1), so the rectangle measure is at most 1/(m^2 d).

An OPS low/high encoding creates at least Delta=Theta(N^beta/n) mismatches on every source pair. If each signed mismatch type is refined into at most r source-valid rectangles, averaging under the uniform source distribution forces
r >= Delta m^2 d/(2N).
This gives a necessary decoder cost for the C-154 lifting route. It does not by itself defeat the route: the source DAG lower bound (m/(A d w log(mk)))^w can outgrow this cost for sufficiently large width. The missing pieces remain the parameterized comparison and actual maps into low/high circuit-complexity tables. See bridge Ãƒâ€šÃ‚Â§90 and O-124/Q123.

### 2.205 - C-165: one-sided lifting outputs do not cover signed mismatch

For the Index-lifted cPHP source on a simple left-degree-d graph, each fixed output pair of distinct pigeons p!=q is valid on at most a 1/d fraction of uniform Bob inputs when Alice's pointer vector is fixed. A table coordinate splits Alice inputs into A_0,A_1 and Bob inputs into B_0,B_1; its two signed mismatch rectangles are A_0 x B_1 and A_1 x B_0. If both Alice sides are nonempty and each orientation has at most r output-labelled decoder leaves, fixing one Alice input on each side yields mu(B_0),mu(B_1)<=r/d, hence r>=d/2. If r<d/2, every Alice code bit must be constant. A Bob input balanced over each pigeon's d neighbors makes every fixed output valid on at most 1/d of Alice inputs, so no mismatch leaf family of fewer than d/2 outputs can cover all Alice rows. Thus the full signed C-75 relation has no fixed coordinate/sign decoder for d>=3.

The 2025 cPHP reduction to monotone Karchmer-Wigderson search only decodes the one-sided edge orientation where Alice has an edge that Bob lacks. This is why it is not already a reduction to C-75's signed mismatch relation. A decoder refinement with at least d/2 leaves per signed type remains possible; it must also pay C-164's Hamming-distance cost. This closes a shortcut, not the lifted-CSP program. See bridge Ãƒâ€šÃ‚Â§91 and Q124.


### 2.206 - C-166: recheck of the known interval-router obstruction

The C-78 universal interval scanner shares all descriptions that induce the same low-table restriction r on interval I. Its state rectangle is {w:w|I=r} x {z:z|I!=r}. If a high table extends a second low restriction s!=r, then it belongs to Bob's side at state r but agrees on I with the Alice rows at state s. Merging these states creates a cross-pair with no valid output in I. Thus short descriptions do not compress the restriction-state family inside this architecture.

For L selected coordinates, point-indicator circuits realize all 2^L low restrictions using O(Ln) gates. If 2^(N-L)>|SIZE(s2)|, each restriction also has a high extension. C-133 already proves that the C-78 profile router has (N/L)2^L distinct vertices at that dyadic level, including across different intervals. The cross-pair explanation here is a specialization of C-110, not a new lower bound. This is not a lower bound on arbitrary rect-DAGs: unrestricted DAGs may change intervals and output on another coordinate. The missing statement is a normalization theorem preserving product rectangles and the magnification budget. See C-166/O-127.
### 2.207 - C-167: generic interval normalization fails

C-160 supplies a counterexample to a promise-independent interval normalization. On its two-tail threshold promise, every pattern on an interval of length L<=a=floor(N^beta/n) extends both to the low side and to the high middle band. The C-110 product-hull argument forces 2^L separate contexts for any router whose descendants must output within that interval. At L=a this is 2^a states. The same promise has an O(N log N) separator circuit, so its unrestricted rect-DAG is near-linear. A generic conversion from arbitrary rect-DAGs to interval-local routers must therefore have superpolynomial loss in N.

This retires only the generic form of O-127. The actual SIZE(s1) versus SIZE(s2)^c promise might admit a special normalization if its circuit-complexity structure supplies a new invariant; no such invariant is known. Keep arbitrary state merging and the q-to-DAG cubic/log loss as the live baseline. C-167 is route pruning, not a Gap-MCSP lower bound.
### 2.208 - C-168: low-row-only samples cannot save coordinates

Fix low row w. If Alice chooses a candidate mismatch set S(w) before seeing Bob's high table, every high z must differ from w inside S(w). But if |S(w)|<N-log2|SIZE(s2)|, then the cylinder of tables matching w on S(w) contains more tables than the entire size-s2 class, so at least one completion is high and defeats the sample. Thus every row-only nonadaptive candidate set has size N-o(N) at OPS parameters. Choosing S from a circuit description does not help.

This is not a DAG lower bound: Bob-dependent rectangle states can route to outputs outside any Alice-preselected set. The surviving avenue is joint adaptive reuse; any proposed near-linear DAG must explain how its state graph exploits Bob's information without reverting to almost all coordinate labels.

### 2.209 - C-170: compact routing requires repeated alternation

The direct ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œAlice sends her circuit description, Bob evaluates it against z, and outputs a mismatchÃƒÂ¢Ã¢â€šÂ¬Ã‚Â architecture is one-switch. It cannot be compressed into a small shared DAG. In any Alice-first one-switch protocol, a message class of low rows must agree on at least N-log|SIZE(s2)| output coordinates: Bob's same response to a high table must work for every row in that class, and all completions matching the class's common pattern must be non-high. The C-80 block-constant family has 2^Theta(s1) codewords separated by more than log|SIZE(s2)| for fixed beta<1/2, so they require distinct frontier states.

The reverse one-switch direction is also expensive. In a Bob-first protocol, a message class must be constant on a coordinate set whose pattern is avoided by every low table. But point-indicator circuits realize arbitrary patterns on t=Theta(s1/n) coordinates. Each Bob message is therefore confined to a cylinder of codimension >t, and covering the nearly full high side needs 2^Omega(s1/n) messages.

This is the precise boundary of the short-description shortcut: one party cannot send a single synopsis and leave the other to complete the search with few shared states. A compact C-75 DAG, if one exists, must exploit repeated alternation so later state choices depend on both sides' accumulated rectangle restrictions. The one-switch theorem does not bound such DAGs; proving an alternation-sensitive charge is the next frontier. See C-170/O-129.

**Stress test.** The block-code family used in the Alice-first lower bound has an O(N)-state B-to-A-to-B DAG when treated as its own restricted low promise. Bob locates a block on which z varies; Alice's block-constant row has a fixed bit there; Bob locates an opposite coordinate. So repeated adaptivity can erase both one-switch barriers on a structured family. The full low class has no shared block partition (C-121); the target is a compact way to route through row-dependent circuit fibers.

### 2.210 - C-171: fiber-witness menus and the transfer barrier

For every low truth table w and high table z, some fiber of w contains two inputs with different z-bits: otherwise z is a unary Boolean function of w and therefore has size at most s1+O(1). This gives a stronger output relation Fib(w,z) asking for a same-w/different-z coordinate pair.

A fixed graph of possible pair outputs cannot be small. For a low row w=1_H where H is an affine subspace of size mÃƒÂ¢Ã¢â‚¬Â°Ã‹â€ 2 log|SIZE(s2)|, the graph induced inside H must have at least m-log|SIZE(s2)| edges; otherwise the monochromatic-edge graph has too many components, and a high z can be made constant on all of them. Averaging over affine H forces Omega(N^2/log|SIZE(s2)|)=Omega(N^(2-beta)/n) candidate edges. Thus C-115's fiber witness cannot be found from a near-linear, input-independent pair menu.

This is not a C-75 lower bound. A Fib solver yields a mismatch with constant leaf refinement, but converting a mismatch DAG back to Fib requires remembering several prior output labels and presently costs O(N^2) copies. A stronger relation's lower bound does not transfer in that direction. This route is useful only if a substantially cheaper reverse simulation or a direct mismatch-state version is found. See C-171/O-130.

### 2.211 - C-172: one global low-table budget across a state's cylinders
For a rect-DAG state v, let K be all output coordinates below it and let P be the distinct K-patterns of its low rows. Every high table agreeing on K with any p in P is excluded from v: it forms a pair with the low row realizing p, and no descendant output can witness a mismatch. The cylinders for distinct p are disjoint. Therefore the whole union can contain at most M2 non-high tables, giving

    |Z minus B_v| >= |P| 2^(N-|K|) - M2.

This corrects C-129's weaker per-cylinder subtraction. At the root it implies |pi_K(Y)|2^(N-|K|)<=M2; arbitrary patterns on t=Theta(s1/n) selected coordinates are realized by point-minterm circuits, so |K|>=N+t-log M2. It is a sharper local invariant, not a global DAG lower bound: C-135 patching gives a fixed N-Theta(s1) candidate-output set that hits every pair, while still leaving the routing problem untouched. The open step is charging overlap among excluded high-column sets across alternating states (O-131), with the C-80 adaptive router and C-160 threshold separator as counterchecks.

### 2.212 - C-173: rectangle decision lists expose a failed-query context gap
A rect-DAG's leaf feasible rectangles cover the promise and each carries a valid signed mismatch label. Listing them produces a multi-output rectangle decision list with at most S terms. This relaxation is already solved in 2N terms by listing all signed mismatch rectangles, so its length cannot prove a superlinear DAG lower bound.

The opposite direction fails for a precise reason. A rectangle-list query A x B requires Alice to test membership in A and Bob to test membership in B. The combined failure set (A^c x Y) union (A x B^c) is generally not a rectangle, so a protocol cannot merge both failure outcomes into one continuation state. The 2025 Rect-DL alternation hierarchy counts changes in Boolean list outputs, not owner switches in a rect-DAG. Reopen only with a forced hard output projection or a richer list measure that preserves failed-query context; see C-173/Q130/O-132.

### 2.213 - C-174: forced output bits cannot exploit Rect-DL size
A Boolean projection h of the mismatch label, if forced to one value on every valid output for each pair, is the OR of the at most 2N mismatch rectangles whose labels have h=1. So the induced function has a Rect-DL of length <=2N and a single output switch. This is far below the superlinear DAG transfer target. Sign projections reduce to comparing Hamming weights after fixed bit flips. If h colors only coordinate blocks, every cross pair differs in exactly one block; a complete bipartite distance-one family is either fixed in one block or a 2x2 square. O-132 is therefore retired as a decision-list-size route, while a direct DAG lower bound remains a distinct possibility.

### 2.214 - C-175: conflict-set gates and why exclusions overlap
For state v let C_v be the full-table set matching some feasible row on all descendant output coordinates. At Alice-owned nodes, C_v subseteq C_0 union C_1; at Bob-owned nodes, C_v subseteq C_0 intersect C_1. Although C-172 bounds the high part of each C_v, these volumes cannot be added. A block-constant low subpromise has an O(N)-state router with m=Theta(s1/n) candidate-block states, each excluding almost all high columns due to its prefix condition; the exclusions repeat by Omega(m). This falsifies raw global summation. O-131 must use path-conditioned mass or a different invariant, with the full circuit class and C-160 threshold countercheck still required.

### 2.215 C-176 - Path weighting removes overcount, not the hard part
The natural repair to C-175 is to charge only a conflict cylinder inside a reached parent context. At Bob nodes, a selected child may be cross-conflicting with the sibling's descendant outputs; summing this event over a path is at most the path length. But the C-80 block router admits valid pairs with zero such events, so no per-pair or distribution-free lower bound follows. The remaining issue is not how to count excluded columns. It is whether many distinct residual rectangles and incoming histories are required because their product hulls cannot share one acyclic suffix. A usable invariant must lower-bound that state topology and survive the C-80/C-160 calibrations. No superlinear result follows.

### 2.216 C-177 - Locality ceiling for a Gap-MCSP separator
If H accepts all SIZE(s1) tables and rejects every table outside SIZE(s2), then a uniform table is accepted with probability at most M2/2^N, while every output of a generator whose table-circuit locality is at most s1 is accepted. Thus any PRG that fools H must have locality above s1. Existing local PRGs for standard branching programs give only S>=s1^(2-o(1))=N^(2beta-o(1)), sublinear for the required sufficiently small beta. Their theorem does not transfer to the C-75 unrestricted circuit-equivalent rect-DAG. The live PRG target would need both general-circuit fooling at S>N^(1+epsilon) and outputs of circuit size <=s1; this is another exact formulation of the hard separator issue. No C-75 bound follows.


### 2.217 - C-178: shared gates compute a sparse envelope, not a description
A C-75 separator circuit H has accepting set A with SIZE(s1) subseteq A subseteq SIZE(s2). Thus the shared-DAG target is exactly the circuit complexity of a sparse envelope of the low-circuit class inside the size-s2 class. The low class itself is an existential projection: x is low iff some circuit description d computes exactly x. A universal circuit handles the verifier for a fixed d; it does not eliminate the existential quantifier. Enumerating all descriptions costs N*2^(O(N^beta)), while Alice sending d gives low communication and an exponential one-switch frontier. This explains exactly why short individual descriptions do not automatically become shared states, but it does not prove that compression is impossible. The next theorem must lower-bound residual separator complexity on product hulls created by DAG merges, or give a compact sparse envelope. No superlinear bound follows yet.



### 2.218 - C-179: parity sketches inherit the sparse-envelope size ceiling
For a fixed low table w, a per-row affine sketch x -> A_w x+b_w can separate w's sketch from every high table only if its collision coset w+ker(A_w) contains no high table. It must therefore fit entirely inside SIZE(s2), so its rank is at least N-log2|SIZE(s2)|=N-o(N). The usual coordinate sample is just a special case. This blocks nonadaptive parity fingerprints as a compression device. It leaves adaptive and nonlinear shared-state routing open and gives no rect-DAG lower bound.



### 2.219 - Nonlinear output length is not a sharing invariant
For a fixed low table w, the single bit h_w(x)=1[x=w] distinguishes w from every high table. Its circuit takes O(N) gates and changes with w. This shows that the affine rank obstruction cannot be generalized by counting output bits alone. A lower bound must measure the shared cost of the whole family of row-dependent predicates, or the adaptive state graph that computes a mismatch.



### 2.220 - C-180: adaptive parity trees retain near-N depth
If a one-input separator uses adaptive affine parity queries, then the path followed by any low table fixes at most t affine equations. Its entire affine leaf cell must lie within SIZE(s2), so it has at most M2 points and t>=N-log2(M2)=N-o(N). Adaptivity in the tree does not help. This does not constrain a shared DAG: it may merge many path cells and use only O(N) states at that depth. The remaining question is state sharing, not parity-query depth.



### 2.221 - C-181: BP local-PRG exponents scale with the low threshold
The local PRG against nondeterministic, co-nondeterministic, and parity branching programs has locality S^(2/3+o(1). The same gap argument as C-177 then forces a size-S BP separator to have S>=s1^(3/2-o(1))=N^(3beta/2-o(1)). This is below N throughout the small-beta magnification range. Stronger exact-MCSP lower bounds at near-maximal size thresholds do not automatically transfer to the much smaller s1 regime. The model is also still a branching program, not the general circuit-equivalent rect-DAG.

### 2.222 - Shared-DAG frontier: the cell is small, its identity is not

The C-74/C-75 relation is now written with totality and resources separated. Plain mismatch is total independently of a fusion list. A Q-specific witness path is total exactly when Q covers every low anchor; its per-pair termination uses a decreasing activation rank, not a global topological order. The fusion measure is cyclic intersection complexity q=rho_prom=DÃƒâ€šÃ‚Â°_cap. A standard rect-DAG is acyclic and has Theta the size of a Boolean promise-separator circuit; the known generic cover-to-DAG compiler costs O(q^3/log q), while the reverse cover transfer is linear.

The strongest local version uses only the output wire: the two fibers w^{-1}(0),w^{-1}(1) cannot both be constant for a high z, since a two-entry lookup composed with the low circuit would compute z. Majority values on the two fibers define a low h, and point-minterm patching forces dist(z,h)=Omega(s2/n). One mixed output fiber therefore contains Omega(s2/n) mismatches from w. Its identity still depends on the pair. This is a denser local witness than a single coordinate. It still depends on the low circuit. The fully merged, unfiltered one-state-per-stage scan cannot merge its two continuation cases. At any late stage i with 2^(i-1)>M2, the hull contains a high pair that mismatches at i but agrees on every later scan position, so that suffix fails. A general DAG may keep filtered contexts or revisit earlier coordinates; this is only a scanner-specific failure.

The language for the live obstruction remains: product-hull-safe state reuse. A shared suffix is valid only if it solves every cross-pair in the product of its merged row and column projections. The open theorem must charge many such incompatible residual contracts across arbitrary alternating states, or an explicit near-linear sparse-envelope circuit will close this route. No such lower bound/construction emerged here.

### 2.223 - Mixed-fiber identity is jointly determined

C-182 supplies a dense mismatch witness in one of two output fibers, but C-183 shows the identity of the mixed fiber is not a one-party or one-rectangle choice. On three addresses, take low rows whose zero sets are {p1,p2} and {p1,p3}; choose high completions with restrictions 001 and 010. The predicate "high table is mixed on the low row's zero fiber" is then the XOR matrix. Merging its two valid pairs restores invalid cross-pairs. The new model distinction is: witness density is a property of each pair, while witness addressability is a product-rectangle property of the routing states. A proof must bridge those two resources through a quantitative sharing theorem. The 2x2 obstruction proves no such bridge automatically; it is not a lower bound against alternating DAGs.

### 2.224 - Hardness mass survives cheap output partitions

C-184 adds a conservation law to the model. If a low circuit partitions addresses into fibers and e_b is the smallest circuit extension of the high table's trace on fiber b, then CC(z)<=CC(w)+sum_b e_b+O(1). Thus high circuit complexity cannot disappear on both fibers at once: at least one residual trace stays hard. That same fiber must contain Omega(s2/n) mismatches, since a constant trace patched at its minority points would be a small extension. For k low circuit predicates, the sum of cell extension complexities loses only the selector cost and O(k2^k).

This is a property of each fixed pair and its low-circuit partition. It does not make the hard cell addressable to Alice and Bob, and it does not imply a DAG lower bound. The next model upgrade would need a rectangle-stable potential that charges how much residual extension complexity is lost when contexts merge, while accounting for cross-pairs.

### 2.225 - Cross-pair variation, not pointwise hardness, is the scarce resource

C-185 is the mandatory countercheck for the C-184 conservation law. Even if every pair has an extension-hard, mismatch-dense output fiber, a structured family with a shared coarse partition can have an O(N)-node router. The router finds a mixed cell of the family-wide partition and never needs to identify the pairwise hard output fiber. Therefore the size of residual hardness is a pairwise fact; shared-DAG difficulty must come from variation in which residual cells are useful across the rectangle's row and column sets.

A candidate potential must be stable under product hulls, charge cross-pair incompatibility, and give only linear cost on C-80/C-121 and C-160. This is the current model refinement, not a lower bound.
### 2.226 - Unfiltered common partitions have a large context cost

C-186 turns the fixed-partition escape into a quantitative covering lemma. The family of r-point-indicator low rows can be covered by common-partition subfamilies with at most m cells only using at least binom(N,r)/sum_{i<=r}binom(m,i) contexts. For m=O(s2)=o(N), this is superpolynomial at the OPS parameters, even though each context has a linear-size C-121 router.

This closes the unfiltered static-menu variant of the common-partition strategy. It does not cover a DAG that filters the high-column side before merging row contexts or shares suffixes across distinct partitions. The unresolved quantity is the price of that filtering under product-hull safety.
### 2.227 - Local Hamming filters are cheap; global center identity is not

C-187 corrects the inference from C-186. If u is one low center and s1+O(Rn)<s2, then the Hamming ball d_H(v,u)<=R is separated from every high table by a threshold circuit with O(N) gates. Population count is linear-size, and hardwiring the center costs at most O(N). For u=0, this one circuit accepts all r-point indicators of C-186 whenever r<=R. Exponentially many unfiltered partition contexts can therefore coexist with one linear shared mismatch DAG.

The remaining distinction is local filtering cost versus global addressability. A C-80 code of exponentially many low rows has pairwise distance much larger than the safe radius for beta<1/2, so no polynomial static list of center balls covers it. That packing argument applies only to a static ball menu. An arbitrary alternating DAG need not name centers explicitly, and product-hull-valid sharing may exploit a different structure. The active theorem must charge that global state reuse, not the count of contexts in one selected router family. This is a countercheck/refinement, not a lower bound.

**Novelty audit:** the Hamming perturbation bound itself is established in C-49/C-136 and is explicitly stated in Krinkin's 2026 preprint. C-187 only applies it to local separator circuits. The 2002 paper *k-Approximating Circuits* uses neighborhoods in the Boolean function's input domain, not neighborhoods in truth-table space, so it supplies no transfer to this problem.

### 2.228 - Global center selection is approximate learning, but the known arrow points one way

The safe-radius union ÃƒÂ¢Ã¢â‚¬Å¾Ã¢â‚¬Â¢_R(SIZE(s1)) is a valid sparse envelope: it contains every low table and, by patching, contains no table above s2 when R=O((s2-s1)/n). Its membership asks whether the input truth table is within R errors of *some* small circuit. That is a two-part existential witness (circuit description plus error set), so the local O(N) ball test does not remove the global search.

Oliveira et al.'s ITCS 2020 Lemma 34 connects this search to non-adaptive learning. A learner for size-s1 circuits, with t-size hypotheses and error epsilon/2, yields an approximate-MCSP separator with size O(N poly(t/epsilon)). Set t=s1 and epsilon=Theta(N^(beta-1)/n) so that t+O(epsilon Nn)<s2; then all project-high tables are NO instances and t/epsilon=Theta(N). The circuit-size loss is N poly(N), and the lemma's direction is learner-to-separator. Its converse-style theorem needs extra NP-completeness/reduction assumptions. Therefore learning lower bounds cannot be used as separator lower bounds here. The model insight is a precise identification of the center-addressability task with approximate circuit learning, plus a hard limit on the current transfer.

### 2.229 - Column certificates expose an asymmetry but not a shared search

For a high table z, let h_Y(z) be the smallest coordinate set Q on which every low table differs from z somewhere. Point-minterm circuits realize every pattern on any fixed k=Theta(s1/n) addresses, so h_Y(z)>k=Omega(N^beta/n^2). In contrast, a coordinate set chosen from a low row and required to catch every high table has size N-o(N), by the high-completion cylinder count (C-168).

If every high column had a certificate of at most k coordinates, Bob could send its sorted indices in O(k log N) communication bits; Alice returns her bits there, and Bob outputs a mismatch. The resulting protocol tree has at most 2^{O(k log N)} nodes. This still says nothing about rect-DAG size. After a match, the feasible pairs fix equality on the tested coordinate, and merging the two possible equal-bit cases creates a diagonal union, not a rectangle.

The model distinction is now sharper: the proved lower bound on column certificates is only sublinear, whereas row-only universal candidates need N-o(N) positions. Actual maximum column-certificate size is unresolved. If those certificates were uniformly short, communication could be correspondingly short, yet state sharing would remain unpriced. The next proof target is a theorem about the cost of addressing and searching Bob-selected certificates under product-hull safety. Coordinate count alone is only Omega(N^beta/n^2), so it cannot support the required superlinear DAG bound. The obvious uniform upper-bound attempt also stalls: the point-patching distance Delta=Theta(s2/n) and |Y|=2^{O(N^beta)} give a random hitting-set size O((N/Delta) log |Y|)=O(Nn), worse than the trivial N coordinates. A nearby VC-dimension theorem for description-bounded circuits only guarantees one large shattered subcube, not that every small coordinate set is shattered; because h_Y minimizes over arbitrary Q(z), it does not improve the uniform bound (Pinon et al., Proposition 46, https://arxiv.org/abs/2103.12686).




### 2.230 - Short certificates cover half the high side, but routing is the bottleneck

Let M1=|SIZE(s1)| and choose k=ceil(log2 M1)+1 coordinates Q. The low class has at most M1 restrictions to Q, so at least 2^k-M1 patterns are absent. Every completion of an absent pattern differs from every low table on Q. At most M2=|SIZE(s2)| completions of each pattern can be non-high. Since k=O(N^beta) while log M2=O(N^beta n)=o(N), at least (1/2-o(1))*2^N high tables have a mismatch certificate on the same fixed Q.

This is stronger than saying some high columns have short certificates: one sublinear support works for a constant fraction of Z. On that restricted subrelation, Alice can send w|Q and Bob return a mismatch in O(k+log N) bits, but the resulting tree can have 2^{O(k)}=2^{O(N^beta)} nodes. It still gives no shared search. A protocol must find which coordinate differs on Q, and the remaining columns have a restriction realized by at least one low row. Enumerating those row-pattern contexts costs up to M1=2^{O(N^beta)}. The proof target is to compress that trace-matched residual while preserving product rectangles; C-80 and C-160 remain counterchecks.


### 2.231 - Tail-only trace recursion needs superpolynomial contexts

For the C-190 coordinate set Q, every low trace sigma has at least one high completion, so the Q-equality subrelation E_Q contains a pair for every signature. A product rectangle wholly contained in E_Q can carry only one signature. If t=Theta(s1/n), then point-indicators give r_Q>=binom(k,t), and M1>=binom(N,t) implies k/t=Omega(n); therefore r_Q=N^{omega(1)}.

This is a real non-shareability lemma for recursive routers that verify equality on Q, discard Q, then continue using only tail coordinates. It is not a general DAG lower bound: a suffix for the full Mis relation can output a mismatch from Q on cross-signature pairs. A promise rectangle can also intersect many diagonal E_Q blocks without being contained in E_Q. The unresolved theorem is an amortized tradeoff between cross-signature Q-outputs and the number of tail contexts.
### 2.232 - Signed mismatch is monotone KW after dual-rail encoding

For each truth-table coordinate i, replace the bit by two indicators rho(u)_(i,b)=1[u_i=b]. If Alice holds a high table z and Bob holds a low table w, a monotone KW output with Alice's rail 0 and Bob's rail 1 is exactly a signed mismatch coordinate: z_i=1-b and w_i=b. Every low/high pair has such an output, and no low dual-rail word is below a high one, so these labels define a partial monotone function. Its monotone upward closure is the canonical separator accepting every low rail and rejecting every high rail.

This makes the C-75 rect-DAG an exact standard monotone KW DAG after a promise-preserving encoding. It also clarifies the relationship to equality-feasible communication states. The C-190 condition w|Q=z|Q is a single state of the form q(w)=r(z), even though C-191 says it takes r_Q=N^(omega(1)) product rectangles if every rectangle must stay within that equality relation. The missing theorem remains global: a general mismatch DAG can let cross-signature pairs exit through Q-coordinate outputs, so it need not realize that matched-trace state as a rectangle cover.

The inequality/equality protocol models in monotone real circuit work are stronger state geometries than product rectangles. Any rect-DAG embeds into them at the same number of states, so a lower bound on those stronger models would suffice. Their known lower bounds are for particular functions and do not automatically apply to this partial MCSP separator. The circuit separator complexity and the cubic q-to-DAG loss are unchanged. This is a precise model bridge, not a new lower bound or P-vs-NP progress.
### 2.233 - Equality states make mismatch search linear, but do not preserve rectangles

The equality-feasible protocol model can solve any disjoint row/column mismatch relation in O(N) states. A state E_i stores the condition that the first i table bits match; a state D_i stores that the first i-1 match and bit i differs. The former branches to the next matching-prefix state or the mismatch state; the latter branches to the two signed mismatch outputs. The explicit graph has at most 4N+1 states and uses only equality predicates q(w)=r(z).

This closes equality-protocol lower bounds as a route to a superlinear C-75 rect-DAG lower bound. The E_i states are not rectangles: they contain diagonal unions of many row/column prefix classes. For the C-190 set Q, C-191 shows the matched state has r_Q=N^(omega(1)) signatures, and a rectangle constrained to remain inside it can cover only one. The linear equality protocol therefore explains what a stronger state can remember, while the standard rect-DAG still has the unresolved product-hull constraint.

Keep degree-two inequality protocols / monotone real circuits as a separate, still untested model. Do not use the equality-to-rectangle expansion of this particular protocol as a lower bound for every rect-DAG.


### 2.234 - Inequality protocols are too strong for signed mismatch

C-194 gives a universal degree-two inequality protocol of 4N-1 vertices for signed mismatch on any disjoint families of N-bit strings. At each interval state, one local map encodes the corresponding substring as a binary integer and compares it with the other party's substring. The protocol splits by which whole string is larger, then recursively finds a bit with the same mismatch orientation. Its singleton sinks are exactly dual-rail output coordinates.

This is a property of the model: each state may use arbitrary local real-valued maps, whose descriptions are free when only graph vertices are counted. The resulting comparison triangles can encode nonrectangular relations with exponentially many product rectangles. In fact, standard rect-DAGs for some arbitrary mismatch promises are exponentially large by the Karchmer-Wigderson circuit correspondence and circuit counting, while their inequality protocols are linear. Therefore the linear protocol neither compiles to a small rect-DAG nor bounds the actual Gap-MCSP fusion number.

Learning: do not seek a C-75 lower bound in the inequality/equality protocol model. It cannot exceed 4N for this output relation, and there is no generic polynomial conversion from that model back to rect-DAGs. Keep the proof target on product rectangles, where cross-signature Q-output exits and safe state merging remain uncharged. This closes O-142 only; O-141 remains live. See C-194 and the primary sources linked there.

### 2.235 - The inequality comparator cannot be expanded statewise on the OPS promise

C-195 sharpens the C-194 model boundary. With N=2^n, s1=N^beta/(c n), and s2=N^beta, every t-bit prefix p for t=floor(s1/(C n))=Theta(N^beta/n^2) has a low table w_p=p followed by N-t zeros. It is an OR of at most t point indicators, each of circuit size O(n). Consecutive w_p values are separated, as integers, by gaps of size 2^(N-t)-1. Since the entire non-high class has size M2=2^(O(N^beta n))=2^o(N), every gap contains a high table z_p.

The selected pairs (z_p,w_p) all lie in C-194's root L comparison state. For p<q, however, z_p<w_(p+1)<=w_q. Thus no product rectangle contained in that state can contain two selected pairs, and covering the state on the actual promise needs at least 2^t-1=2^(Theta(N^beta/n^2)) rectangles.

Learning: the comparison protocol's linear graph does not compile by replacing each triangle state with rectangles; that direct expansion is superpolynomial even for the actual low/high classes. Yet this state-cover bound does not lower-bound the relation: on the selected prefix-row/gap-column subpromise, all low suffix bits are zero and every high gap column has a suffix 1, so Bob scans the suffix in an O(N)-vertex rect-DAG. The triangle is hard to expand, while that restricted search problem has another cheap organization. The open target is still to charge Q-output exits and residual-context reuse across all product states. See bridge C-195/O-141.

### 2.236 - A state trades Q-output exits against tail separation

Fix C-190's coordinate set Q. At a standard rect-DAG state with rectangle A x B, let P be the descendant output coordinates inside Q and T the descendant coordinates outside Q. If low and high signature fibers overlap on T, their signatures must differ somewhere on P; otherwise a product-hull pair agrees on every output available below the state. A signature occurring on both sides is diagonal, so its tail projections must be disjoint. More quantitatively, if r diagonal signatures are present and |T|=t, then the state excludes at least max(0,r*2^(N-|Q|-t)-M2) high columns.

The proof stops at aggregation. C-130 shows these excluded columns can recur at many reachable states; C-80 and C-160 show coarse local constraints can coexist with linear or near-linear DAGs. A state can expose all Q outputs and let a shared tail subgraph handle the diagonal pairs, so a count of signatures is not a state lower bound. The next attempt must charge the routing graph for Q exits together with the tail contexts. Description strings still do not help automatically: description-space rect-DAG size equals truth-table-space size, and a universal circuit leaves the existential projection over descriptions. This is a local invariant only, with no new global lower bound or P-versus-NP consequence. See research bridge C-196/O-141.
### 2.237 - Communication bits, tree nodes, and shared states are distinct

For an m-bit Boolean function f, its KW Bit relation has deterministic communication O(m): Alice sends her m-bit input, and Bob returns a differing position. By the Sokolov DAG-like KW/circuit correspondence and circuit counting, there are f for which the standard rect-DAG needs 2^(Omega(m)) states. Parity gives the reverse sharing calibration: O(m) DAG nodes versus Omega(m^2) formula/tree nodes. A protocol tree can never have fewer nodes than the optimal DAG; the potentially small quantity is communicated bits, not tree-node count. These examples clarify C-75's resource separation without proving anything about the specific low/high promise.

### 2.238 - Partial monotone KW creates a precise lifting interface, not yet a reduction

Encode a table x by the one-hot rails e(x)_(i,b)=1 iff x_i=b. All encodings have equal weight, hence are pairwise incomparable. Set a partial monotone function to 0 on encoded high tables and 1 on encoded low tables. Its monotone KW output (i,b) is exactly a signed mismatch, so the project's rect-DAG is the corresponding restricted partial monotone KW DAG. The CCC 2025 colourful-sunflower lifting theorem is therefore compatible with the target model. An answer-preserving reduction from a lifted unsatisfiable-CSP search relation would transfer a DAG lower bound at no size loss by taking rectangle preimages.

The missing ingredient is a reduction into the actual promise: each Bob image must have circuit complexity greater than s2, and every mismatch coordinate must decode to a valid hard-search witness. Efficiently generated Bob tables cannot meet that high-complexity condition. Affine-coset code constructions also fail: a parity check separates the cosets with O(N) gates. Learning: model compatibility is not enough; the reduction must create hard truth tables without introducing easy mismatch witnesses. This is a candidate interface only, not progress on the required quantitative lower bound. See research bridge C-198.



### 2.239 - High-table filtering is cheap inside DAG lifting, but output compatibility remains
The ECCC 2024 triangle-DAG lifting proof removes error columns bottom-up. Its proof adapts when the initial error set contains the omitted Bob columns; because the target high-table set omits only 2^(-N+o(N)) of all truth tables, the lifting lower bound survives up to a constant factor. This means a reduction need not individually generate high tables.

The remaining condition is exact: each oriented mismatch set at a table coordinate is a rectangle cut by one row predicate and one column predicate. A source search reduction must make both oriented cuts valid outputs. At the same time, the low-image family must resist simple range recognition; the natural blockwise pointer code has an O(N)-gate range test. Thus dense high-side restriction resolves one technical obstacle, while output-preserving encoding and hard low-image recognition remain the main barriers. No lower bound or proof follows. See research bridge C-199.



### 2.240 - A hard source DAG can collapse after an easy image embedding
The CCC 2025 colourful-sunflower construction gives hard monotone KW relations through clique-colouring, but its particular Alice images are isolated k-cliques on a selected transversal. A degree-based O(N logN) circuit recognizes that entire range and rejects every c-colourable Bob graph. Thus the corresponding C-75 signed-mismatch promise is easy even if high tables are selected on Bob's side. Moreover, reverse adjacency differences are legal C-75 outputs but not valid monotone-KW outputs. Learning: source-problem DAG hardness does not transfer through a reduction unless both output decoding and low-image envelope hardness survive. The standard clique-colouring map fails both checks. See research bridge C-200.

### 2.241 - Corrected lifting exponent sharpens a conditional bridge

The 2024 triangle-DAG lifting theorem has size threshold (1/2)m^((1-delta)w); its own near-tightness comparison verifies that exponent. Seeding the proof's accumulated column errors with a deleted set of density below 1/4, and reducing the theorem's constant to 1/4, leaves enough row and column entropy for the same resolution extraction. Hence the high-table restriction retains Omega(m^((1-delta)w)), not a square-root exponent.

This improves the quantitative *source lower bound*. If mr=N, r=polylog(N), and (1-delta)w>3+3epsilon, the bound could cross the project's cubic/log rect-DAG compiler threshold. It does not provide a source-to-C-75 map: Alice's images still need low circuits and a hard-to-recognize envelope, and both signs of every C-75 mismatch must decode to valid source witnesses. Treat this as a corrected conditional interface, not a C-75 lower bound.

### 2.242 - Unique search answers make mismatch decoding expensive

For the Index-lifted search relation of the CNF containing one clause per falsifying assignment, the valid output is unique. A product rectangle on which one answer remains valid must restrict the address projection of Alice in every variable block, while Bob fixes every indexed bit reachable from that projection. Its uniform mass is at most (1/(2m))^v. Consequently, refining each of C-75's 2N mismatch types into valid answer rectangles requires Omega(m^(v-1)) leaves per type when the table length is N=mv.

At v=16 and w=15, the dense-column lifting lower bound is only Omega(m^13.5) for delta=0.1, so decoder overhead dominates. This kills the simple unique-answer source transfer, including any fixed answer decoder. It does not kill answer-rich sources or direct encodings. Future source selection should measure output-fiber rectangle mass before investing in a lifting reduction; cPHP's C-164 bound is the closest calibration. See research bridge C-202.

### 2.243 - An answer-rich lifted source can pass the decoder exponent filter

The constant-degree cPHP family in the CCC 2025 lifting paper has base width W=Omega(k) on suitable expanders. Its lifted triangle-DAG lower bound is (m/(A d W log(mk)))^W. If a prospective table encoding has N=Theta(mk) bits, C-164's minimum output-refinement cost is Omega(Delta m^2d/N)=Omega(dN^(1+beta)/(k^2 logN)) per signed mismatch type. The source exponent can exceed the current compiler threshold times this minimum decoder cost once fixed W>4+3epsilon+beta. Therefore the unique-output failure C-202 is source-specific; answer-rich cPHP remains quantitatively viable at this screen.

The distinction is between a lower bound on necessary decoder cost and the missing upper bound. No decoder with r<L/T leaves per mismatch type, no partywise low/high table map, and no proof of dense-column robustness for the CCC theorem have been obtained. C-201's robustness proof applies to a different binary lifting theorem. The clique-colouring map still has the easy O(N logN) low-image envelope from C-200. This is a parameter filter only, not a C-75 lower bound.

### 2.244 - The colourful-sunflower lift tolerates the high-table deletion

The CCC 2025 proof's Full Range Lemma is stated for an arbitrary Bob-column subset Y of density above epsilon, and its triangle lemma explicitly bounds the union of structured error-column sets. Rerunning the extraction with Bob's root domain B equal to the high truth tables works when the omitted fraction eta=2^(-N+o(N)) is below the local error scale 2^(-Theta(W log(mn))). For N=Theta(mn) and W log(mn)=o(N), even an S-fold error charge is negligible at the theorem's protocol-size threshold. This gives the same m^(Omega(W)) lifted triangle-DAG lower bound up to constants. See bridge C-204 and [the primary CCC 2025 source](https://drops.dagstuhl.de/storage/00lipics/lipics-vol339/ccc2025/html/LIPIcs.CCC.2025.36/LIPIcs.CCC.2025.36.html).

For power-of-two alphabet d and compatible N=log2(d)*mk, Bob's raw flattened string ranges uniformly over all tables, so the high-side map is the identity restricted to high outputs. C-200's standard Alice graph image remains easy; the low-image map, both-orientation decoder, and decoder upper bound are still absent. This closes a technical interface, not the Gap-MCSP lower bound.

### 2.245 - Raw Bob bits force a source-hard decoder unless sink context is charged

Take any proposed Alice code on the cPHP Index source and any table coordinate i. One value of that coordinate contains at least half of Alice's pointer inputs. If Bob's map is the raw bijection from the lifted alphabet array to all table strings, the opposite Bob-bit slab still has density 1/2-o(1) after removing low-circuit tables. The CCC lifting proof's row-error estimate shows that the source relation remains hard on this dense product slab: after deleting errors, Alice retains blockwise min-entropy log(m/8), and Bob retains constant density.

Thus a decoder that depends only on the mismatch label (coordinate and sign) must solve a source-hard cPHP restriction and costs as much as the original lifted lower bound. The advertised decoder-refinement gain disappears. The possible escape is precise: the decoder must use the **target DAG sink rectangle** as additional context, or the Bob map must cease to be raw and balanced. The former makes context accounting part of the shared-state problem; the latter must still guarantee all images are high and preserve both mismatch signs. This closes a parameter screen that ignored decoder size, not the cPHP route in every form and not C-75 itself. See bridge C-205/O-144.

### 2.246 - A sparse sink has a low-codimension entropy witness, but collision branches remain

Any row set A of density rho in `[m]^k` has a slice with blockwise min-entropy `delta log m` after fixing fewer than `log_m(1/rho)/(1-delta)` pointer addresses. The proof repeatedly conditions on a pattern that is too heavy; each such conditioning boosts density by `m^(1-delta)` per fixed address. Therefore polynomially many target-DAG contexts can only lose a constant number of address coordinates before a regular slice appears.

For complete cPHP, after this restriction, Bob's values at the fixed addresses create a finite pattern split. If the prefix values are distinct, the residual pigeonhole search keeps online-matching width Omega(c-t); if they collide, the prefix itself solves the search. This isolates the missing shared-DAG invariant: a global charge must count how the DAG reuses or fragments address-fiber collision branches. The entropy slice is not a cover of its parent row set, and the Bob side may concentrate on easy collisions, so no sum over slices is valid yet. See research bridge C-206/O-145. No C-75 lower bound follows.

### 2.247 - Shared-state descriptions are quotient-invariant

For C-75 on `Y x Z`, a standard rect-DAG is Theta-equivalent to a Boolean circuit separating the promise classes. If Alice is given a size-s1 circuit description `d` instead of its truth table `w=G(d)`, the minimum DAG size is unchanged: lift each Alice-local state predicate through `G`, then reverse by choosing one description for each `w`. This uses the model's free local predicates; the charged resource is graph states. A universal circuit evaluates one description, but the shared graph still must solve the existential projection defining the low set. Hence short descriptions alone are not a state-reuse lemma: a near-linear universal graph would already be the sought sparse-envelope circuit. The route remains open only as the actual circuit lower-bound problem. See research bridge C-207; no lower bound was proved.

### 2.248 - A state's output support is a hitting set, not a routing proof

For any valid rect-DAG state v, the projections of its row and column rectangles onto descendant output coordinates K_v must be disjoint. Equivalently, every pair in the state has some mismatch among K_v. The local density inequality for row traces is just this projection disjointness plus cylinder counting; it holds for arbitrary mismatch relations and supplies no low-circuit-specific internal hardness. It certifies that a mismatch exists, not that a binary shared DAG can select one. Root high-table counting still forces near-full output support, but internal column deficits overlap (C-80/C-175). The new-model target is therefore a parent-conditioned routing invariant for shared projection patterns, not an additive sum of state capacities. See C-208/O-141; no lower bound follows yet.

### 2.249 - Merging histories exposes their product hull

At any shared rect-DAG state v, every root-to-v history is a product rectangle contained in v's local rectangle. Consequently, if histories `A_h x B_h` merge, the suffix at v handles the entire hull `(union_h A_h) x (union_h B_h)`, including pairs never present in any one incoming history. On the outputs below v, the union of row projections must be disjoint from the union of column projections. This is the precise meaning of product-hull-safe reuse. It is a necessary contract, not a lower bound: C-80 has an O(N) DAG that satisfies it, and C-191's prefix outputs can route cross-signature pairs. The unresolved quantity is how the residual separator cost of many such hulls can be charged without double-counting shared suffixes. See C-209/O-141.

### 2.250 - Rank is the hidden resource behind cyclic fusion states

The fusion list's q rule states are not an ordinary q-node DAG. Each active rule has a least-fixed-point rank `tau_i(w)` depending on the row input, and a valid support move decreases that rank for the current pair. This gives a q-state **ranked cyclic** protocol. Making the ranking explicit yields product rectangles `(i,r)` and an acyclic multiway graph with q^2 rule/rank states; support routing can still have O(q+N) alternatives per state, so ordinary binary size remains cubic-order. A q^2 vertex count that ignores fan-out is not a standard binary-DAG upper bound.

This locates a possible non-shareability issue: merging routers from different ranks is safe only if their product hull still admits all cross-history support choices. C-209 states the necessary hull law, but there is no theorem charging these router contexts and no superlinear DAG or fusion lower bound. Preserve the distinction `q=rho_prom=D^circ_cap`, `rho_prom<=O(S_rect)`, `S_rect=O(q^3/log q)`. The exact cyclic model has q charged intersections; binary DAG simulation pays for routing and acyclicization. No breakthrough has been obtained.

### 2.251 - Static support can be near-linear while routing stays hard

Every low/high pair has at least `d=Omega(s2/n)` mismatch coordinates by circuit patching. A set-cover argument supplies `R=O(d log(eN/d))` subsets of `k=ceil(N/d)` coordinates, total `O(N log N)` incidences, such that every mismatch set hits some subset. This closes only the support-selection question in an existential sense. It does not specify which subset a shared protocol can route to: the joint predicate Ã¢â‚¬Å“this subset has a mismatchÃ¢â‚¬Â is not a product rectangle.

A scanner confined to one sample that forgets matched prefixes is unsafe under product-hull merging. At the point-minterm scale, all `2^t` patterns for `t=Theta(s1/n)` occur as low rows and have high completions; merging their histories into a suffix restricted to untested coordinates permits cross-pairs with no valid output. A composite suffix allowed to revisit old coordinates or other samples may still work, so this is not a general lower bound. The new lesson is that small mismatch support and large state complexity can coexist because the support set must be selected and routed with product rectangles. O-141 remains open; no DAG, q, or P-vs-NP bound follows.


## C-212 model update: sparse interpolation versus shared search

A fixed `t=Theta(s1)` set of truth-table coordinates is fully shattered by the low class. The mechanism is sharing: divide the n address bits into blocks of width about `log r`, build every local equality decoder once per block, then combine only the r selected addresses. An arbitrary r-point correction therefore costs `O(n+r*n/log(r+1))`, and the high side is `Omega(s2)` Hamming distance from every low table. This sharpens local geometry without changing the central model distinction.

The exact C-75 ordinary search object is still the promise-restricted signed-mismatch relation, with one output `(i,b)` per pair satisfying `w_i=b,z_i=1-b`. Its standard acyclic product-rectangle DAG size is `Theta` the sparse-envelope separator-circuit size. A fusion cover is instead the promise's cyclic intersection complexity: rule dependencies can cycle in the static graph while each input pair follows a decreasing activation rank. Rank-layering uses `q^2` rule/rank vertices before accounting for high fan-out; the best standard compiler remains `O(q^3/log q)`. Thus neither the improved local shattering nor a cyclic q-state count closes the gap.

The best current non-shareability law is still C-209: a shared suffix solves the full product hull of every row and column history entering the state. C-191 gives many diagonal signature contexts, now at scale `2^(Omega(s1 log n))`, but cross-signature pairs can use Q outputs and avoid those tail contexts. We have not proved that the exits cost enough DAG vertices. C-80 and C-160 remain decisive counterchecks against coarse profile, variation, and volume potentials. The needed theorem is a globally amortized, product-hull-safe Q-exit/tail tradeoff for actual low/high circuit classes, strong enough to beat `N^(3+3epsilon)/log N`, or an explicit near-linear separator for the whole promise.

The closest existing model comparisons and their exact limits are tabulated in bridge C-212 and sourced to the primary Sokolov, GGKS, Cavalar-Oliveira, Nakayama-Mar(u)oka, and Amano-Mar(u)oka works. No C-75 superlinear DAG bound or P-vs-NP proof has been established.


## C-213 model boundary: cycles can erase context, but fusion cannot be inferred

There is a `5N`-state cyclic rectangle protocol for signed mismatch on any disjoint pair of N-bit string families. It scans one coordinate per state and wraps around; a deterministic local strategy exits as soon as it sees a mismatch. The wraparound suffix revisits coordinates whose history was erased, so the node can solve the full product hull. This kills lower-bound attempts against the unrestricted cyclic rectangle model.

The fusion cover is a narrower cyclic computation. Each state is one unary closure activation set on a single truth-table input, generated from legal literal slices and contained predecessor carriers; a protocol rectangle instead has independently free row and column predicates. A semantic cut represents any rectangle, but constructing that cut as a legal closure state may cost as much as the sparse-envelope separator. The universal cyclic scan therefore does not give an O(N) fusion cover, and no standard acyclic DAG follows from it. The active targets remain an OPS-specific acyclic rect-DAG lower bound above the cubic transfer threshold or a direct native-closure argument. See bridge C-213.

## C-214 Ã¢â‚¬â€ Effective description length of a fusion closure state system

Although each fusion endpoint may be an arbitrary semantic subset, the closure recurrence sees it only through a seed clause over the 2N signed table-bit literals and the predecessor-containment incidence relation. A q-rule system therefore has at most 4Nq+2q^2+q bits of effective specification. For arbitrary full partitions this gives, by direct counting, a promise requiring Omega(2^(N/2)) fusion pairs. The mismatch search on that same partition still has a 5N-state cyclic rectangle protocol. This exposes the model boundary: free independent party predicates can encode far more than a unary least-fixed-point closure state.

This is a generic model-separation theorem only. It does not identify the actual SIZE(s1)/SIZE(s2)^c promise as a hard partition. The gap problem requires one explicit sparse envelope, and its middle band permits multiple separator extensions. Use C-214 to reject generic cyclic-to-fusion transfers, then return to O-141's actual product-hull sharing problem. Keep q<=O(S_rect)<=O(q^3/log q) and the required S_rect>N^(3+3epsilon)/log N threshold visible. No P-vs-NP proof follows.

### C-215 Ã¢â‚¬â€ Q-exit graphs and the missing global charge (27 September 2026)

At a rect-DAG state, make a bipartite graph between low and high Q-signatures, joining two signatures when their tail projections overlap. Every edge must differ on the descendant Q-output coordinates; otherwise its row and column witness agree at every output below the state. At the root, high-completion counting forces at least N-|Q|-log2(M2) tail output coordinates. A fixed witness pair persists to the child it enters, but the graph can gain edges as tail support shrinks and lose edges under input filtering, so edge count is not a potential. A useful next invariant must follow parent-conditioned pair histories and charge Q exits against reused tail suffixes. C-80 and C-160 remain counterchecks. See research/C215_Q_EXIT_GRAPH_AUDIT_2026-09-27.md.

The July 2026 lifting result for monotone learning is a possible source of proof techniques, but it is conditional on rETH and works from succinct labelled examples. It does not give a size-controlled map to the complete low/high truth-table promise: a succinct example generator is itself a small table circuit, so it cannot directly provide the high images needed here. No C-75 DAG or fusion bound follows.

### C-216/C-217 Ã¢â‚¬â€ Local deficits and the fixed-order boundary

C-216 adds a state-local profile: common Q-signature multiplicity times the number of free tail completions is bounded by the non-high mass plus the high columns filtered out at that state. Root specialization gives a `log r_Q` support gain, but it does not add across transitions: Alice branches duplicate the budget and Bob branches introduce an almost full-cube term. Local capacity is still not a global state potential.

C-217 gives a sharp obstruction to the most direct universal DAG. Any fixed coordinate order must retain `2^(Theta(s1))` matched-prefix states because the low circuit class shatters every short coordinate set and every such prefix has a high completion. Product-hull safety forbids merging different no-mismatch prefixes if the scanner cannot revisit coordinates. This excludes fixed-order scanners while leaving adaptive/revisiting rect-DAGs untouched. The central model remains: short individual descriptions simplify communication bits, but a shared DAG must implement the existential projection over all descriptions. No near-linear separator or unrestricted rect-DAG lower bound has been found.

The quantitative route is unchanged: `rho_prom=q`, `rho_prom<=O(S_rect)`, and the known compiler gives `S_rect=O(q^3/log q)`. Any rect-DAG lower bound intended to yield `q>N^(1+epsilon)` must exceed `N^(3+3epsilon)/logN`; the fixed-order theorem does not meet this transfer because it is restricted to one protocol architecture. Preserve C-80/C-160 and continue O-141.

**C-217 scope clarification.** The prefix-state lower bound only holds when a fixed-order scanner halts at its first mismatch. A deferred-output DAG may merge histories whose cross-pairs retain a later mismatch; adaptive and revisiting DAGs are also outside the theorem. The robust lesson is that the direct first-mismatch universal scan cannot be compressed by ordinary prefix sharing, not that all shared DAGs are large.

**Deferred-output implication.** With minimum low/high distance `d=Omega(s2)`, discarding fewer than d fixed coordinates preserves a mismatch for every pair. This gives a root output-support set of size `N-O(s2)=N-o(N)`, not a protocol. It explains why a deferred-output DAG can evade the first-mismatch prefix argument while leaving the true difficulty untouched: product-rectangle routing must select a mismatch coordinate. Do not turn support existence into a DAG upper bound.


### 2.252 ? Distance?dimension slack is a certificate resource, not a routing resource

Shrink the yes-side to `SIZE(N^gamma)` for any fixed `gamma<beta`. A separator lower bound for this subpromise transfers to the original because every separator for the larger yes-side also separates the smaller one. C-212 gives low/high distance `d=Omega(N^beta)`, while the number of low tables has logarithm and VC dimension `O(N^gamma n)=o(d)`. Therefore every high table has a sublinear coordinate set that hits its mismatch set against every low table. Sauer?Shelah also gives a common `O(N^gamma n)`-coordinate block with a constant fraction of projected patterns absent from the low class, while the rest of the coordinates retain large mismatch distance.

This adds a distinction to the model: **support certificates can become sublinear after a monotone parameter restriction, but product-rectangle routing can still be hard**. A certificate is either selected separately for each Bob table or exposes a local block; neither tells the shared DAG which coordinate differs for its particular row. The next proof target is a router for the projected class `pi_Q(SIZE(N^gamma))` whose states remain valid on the full product hull. No global DAG charge or P-vs-NP proof follows. See C-218/O-141.


### 2.253 ? Certificate blocks inherit the no-revisit width obstruction

The C-218 fixed block can make many high columns certificate-bearing, but searching inside the block is not automatically cheap. If Q has size twice the VC dimension v of the reduced low class, every low-shattered prefix p has an absent suffix completion: the p-slice has VC dimension at most v, and the remaining block has more than v coordinates, so Sauer-Shelah leaves a missing pattern. Each missing block pattern has a high full-table completion. Therefore a fixed-order first-mismatch router on Q still needs exponentially many prefix states. This rules out the direct local scanner and leaves deferred/adaptive product-hull routing as the next target. It is not an arbitrary-DAG lower bound. See C-218-A/O-141.


### 2.254 - C-75 shared states are residual separators

A rect-DAG vertex is not merely a remembered circuit description or a coordinate counter. Its row and column histories form a full product rectangle `A_v x B_v`; all pairs in that product must still reach a valid mismatch below the vertex. If `K_v` is the descendant output support, then `pi_Kv(A_v) intersect pi_Kv(B_v)=empty`. This is the exact local law for state reuse. The proof-level gap is global: local supports/exclusions overlap, so they do not sum to more than a linear state bound. The next invariant must price different residual separators across states while retaining C-80/C-160/C-209 counterexamples.

Circuit descriptions do not compress the minimum graph: truth-table pullback and a one-description-per-table section give equal rect-DAG sizes. They do compress communication bits, because Alice can send one description, but that is a depth/bit resource rather than shared-state count. A tree cannot be smaller than a DAG in vertex count; the valid contrast is low communication bits versus many graph nodes or formula/tree size versus circuit/DAG reuse.

Model direction to preserve: triangles include rectangles, hence `S_triangle<=S_rect`; a triangle-DAG lower bound would imply a rect-DAG lower bound. But C-194 gives a universal `4N-1`-state triangle-DAG for every disjoint mismatch promise, so this stronger model is too powerful for a superlinear lower bound on C-75. C-195's rectangle expansion of one chosen triangle state does not rule out alternative rectangle-DAGs. No OPS-specific superlinear state bound is known.

The obvious binary-search improvement to the universal description scan also fails as a one-state branch: Ã¢â‚¬Å“there is a mismatch in interval IÃ¢â‚¬Â is not generally a product rectangle. For `I={1,2}`, rows `00,01` and columns `10,00` contain two mismatch pairs but their cross-pair `00,00` has no mismatch. Covering that branch by multiple rectangles is possible in principle; counting that cost is still open.



### 2.255 - The fusion feature map is easy; the closure readout is the hard part

For a successful q-pair list, its 2q seed clauses form a feature map `sigma_Q(x)`. Since the least-fixed-point closure is monotone in these seed bits, every low/high pair must have a feature that is 1 on the low table and 0 on the high table. A seed clause is an OR of signed literals; its zero set is a subcube, so these features give an oriented subcube-cut cover of the promise. The minimum cut count is at least `N-log|SIZE(s2)|`, but at most `2N`, because the signed-literal features separate every distinct pair. This isolates why literal witnessing, mismatch supports, and clause counting stop at a linear scale.

The unresolved complexity is the **closure readout**: the positive least-fixed-point program must combine the features in paired AND rules, share predecessor carriers, activate an empty carrier on every low table, and keep every high table inactive. O-141 should target the cost of that interaction beyond the linear feature cover, not the feature dimension itself. Exact proof and limits: `research/C221_SEED_FEATURE_VS_CLOSURE_READOUT_2026-09-27.md`. No superlinear fusion/DAG lower bound or P-vs-NP proof follows.


### 2.256 - The closure readout is a cover by wide activation certificates

View the least-fixed-point output as a monotone function of the seed-clause bits. Each low table must contain a minimal set `U` of true seed features that already forces this output to 1. If the corresponding clause conjunction is satisfiable, all tables satisfying it activate an empty carrier, so none can be high. Since there are at most `|SIZE(s2)|` such tables, fixing one true literal per clause shows `|U|>=N-log|SIZE(s2)|`. Every low table contains at least one such wide certificate, and every high table avoids all of them.

This turns the native-closure question into a certificate-family problem: can the q paired rules generate a cover of all low-circuit feature vectors by wide consistent certificates while excluding every high-circuit vector, with q superlinear? Width alone yields only the linear floor because there are 2q features. The needed progress is an overlap/readout lower bound on this particular certificate hypergraph. Proof and caveats: `research/C221_SEED_FEATURE_VS_CLOSURE_READOUT_2026-09-27.md`, section C-221-A.




### 2.257 - Circuit-dependent signatures cannot be replaced by a short fixed menu

C-115 selects a small set of gate values from the particular low circuit. A fixed menu of address signatures is not an adequate substitute: every low t-sparse point indicator must have support that is a union of signature fibers, and one K-cell partition represents only `sum_{j<=t} binom(K,j)` of the `binom(N,t)` possible supports. At the OPS scale `t=Theta(N^beta/n)` and `K<=N^beta`, the ratio is `2^(-Omega(N^beta))`; a universal menu needs superpolynomially many signatures.

This formalizes why short descriptions do not automatically become shared states. The signature in the witness is input-dependent, and an adaptive DAG must expose it while preserving every merged product hull. This result rules out only fixed-menu universalization; it says nothing against adaptive selectors or general rect-DAGs. See `research/C222_FIXED_SIGNATURE_MENU_LOWER_BOUND_2026-09-27.md`.




### 2.258 - Fixed-menu entropy does not lower-bound adaptive selection

C-222 forces exponentially many fixed signatures to cover the point-indicator family, but this is not a lower bound on a circuit that selects a signature from the table. For a t-sparse indicator, a sorting network can recover its support addresses in `O(N log^3 N)` gates; those addresses specify a short point-indicator circuit. So a large set of possible signatures can still have an efficiently computed choice on a structured subfamily.

The unresolved issue is whether an adaptive selector can handle **all** low-circuit tables without essentially solving search-MCSP, and whether its choices can be shared in a DAG while preserving product hulls. The menu-count theorem alone does not settle either question. See C-222-A in the C-222 report.


### 2.259 - Explicit synthesis and implicit shared routing are different tasks

An exact selector for low tables that outputs a size-`s1` circuit gives a separator: evaluate its selected circuit on all N addresses and compare against the input truth table. With selector size R this costs `O(R+N s1 log(s1+n))`, which is `O(R+N^(1+beta))` at the OPS parameters. The verification factor means a small selector does not automatically yield a near-linear DAG.

A separator is only a yes/no promise function; it need not return a circuit for a low table. Converting decision information into an exact small-circuit witness is a search-to-decision step, which is known to be open for classical MCSP in the cited literature. Our C-75 object is a gap promise, so no equivalence is claimed. General rect-DAGs can route using product rectangles without exposing any circuit description. Therefore selector lower bounds are not substitutes for O-141's unrestricted state-reuse theorem. See `research/C223_ADAPTIVE_SIGNATURE_SEARCH_MCSP_BOUND_2026-09-27.md`.

Recent context: Hirahara and Ilango's FOCS 2025 result establishes conditional NP-hardness for constant-factor approximate MCSP under deterministic quasipolynomial nonadaptive reductions and three strong assumptions. It does not settle this unconditional Gap-MCSP selector/DAG question. The source and exact scope are recorded in C-223.


### 2.260 - Approximation errors are the escape hatch from signature fibers

Suppose a circuit C of size r approximates a low table w with e errors. Select k of C's wires, including its output, to define an address signature. For a high table z, let m be the number of good addresses whose z-bit is a minority value inside its signature cell. A cell lookup composed with C, followed by point corrections, computes z with size `r+O(k*2^k+(e+m)n)`. Therefore a high z forces either enough approximation errors or enough within-fiber variation to pay the remaining s2 circuit-size gap. When the variation is positive, two good addresses in one cell have the same w-bit and different z-bits, yielding the C-115 style local mismatch witness.

This isolates the limitation of approximate natural-property learning. To force fiber variation, the error count must satisfy roughly `e*n<s2-r-O(k*2^k)`, i.e. `epsilon<N^(beta-1)/n` if `e<=epsilon*N`. Carmosino et al.'s natural-property theorem gives randomized learning under a **uniform P-natural** property; a nonuniform C-75 separator circuit family does not meet that premise by itself. Even under the added uniformity, learning is not a shared-DAG compiler: it neither locates a signature without synthesis nor charges cross-history product hulls. O-141 remains the real global obstacle. Full statement and proof: `research/C224_APPROXIMATE_FIBERS_NATURAL_PROPERTY_BOUNDARY_2026-09-27.md`.

### 2.261 - A signature's entire hard variation can hide in one good cell

Let C be an approximate circuit for low table w, and let k selected wire values, including C's output, partition addresses. The largest cell among addresses where C=w has size at least `(N-e)/2^k`. If this cell F is larger than the circuit-description count at threshold s2, flipping w on subsets of F produces a high table. Yet both endpointsÃ¢â‚¬â€w and w with all of F flippedÃ¢â‚¬â€are low when `s1+|C|+O(k)<s2`, because F is testable using w, C, and the signature. Point-patching from both endpoints forces `Omega(s2/n)` minority addresses, all in F.

Choosing `kappa<min(beta,1-beta)` makes the cell large enough for counting while keeping k logarithmic in N, for every fixed beta. Thus fiber variation is real but may be concentrated in one cell. Do not count mixed cells or sum their number. The unresolved resource is locating a pair-dependent cell without explicit circuit synthesis and sharing its suffix under the full product-hull condition. This refines C-120/C-224 and leaves O-141 open. Full proof: `research/C225_APPROXIMATE_SIGNATURE_ONE_CELL_CONCENTRATION_2026-09-27.md`.

### 2.262 - Fusion states form a cyclic alternating reachability game

A fusion rule is an AND of two support obligations; a side obligation is an OR over literal seeds and predecessor rule states. The exact semantics is a least reachability fixed point, so infinite plays lose. This gives a compact O(q)-state alternating program with O(q(N+q)) transitions and input-dependent decreasing activation ranks. A standard rect-DAG has neither universal branching nor cycles, and a standard NBP path cannot verify both branches of a shared activation proof without unfolding or storing the active state set. The generic BP simulation is exponential in q. Existing MCSP BP lower bounds therefore do not yet charge fusion q. Their local-PRG method gives a promise co-NBP lower bound about s1^{3/2}; at OPS low threshold N^beta/(cn), this becomes superlinear only above beta=2/3. This is outside the small-beta magnification target. The native lower-bound problem is cyclic alternating reachability on the explicit low/high promise, with product-hull-safe sharing still required. See C-226.


### 2.263 - Native proof-context splice law

An activation state has a finite positive proof grammar: choose an E-side support and an H-side support, then union their seed labels. This gives a local cross-product law inside the fusion closure. If an accepting proof contains state i, any other finite proof rooted at i can replace that occurrence; the output proof remains valid. This is the exact native meaning of state reuse.

The splice does not automatically create a legal truth table. Seed labels are dual-rail: opposite signs on a coordinate make the mixed support inconsistent. If the support is consistent, every table in its cylinder is accepted, so soundness forces it to fix at least N-log2(M2) coordinates. The global lower-bound target is consequently precise: force a shared context/replacement pair whose union is consistent but fixes fewer coordinates. The needed invariant must remember the proof context outside the shared occurrence, not just the state certificate antichain. See `research/C227_NATIVE_CERTIFICATE_SPLICE_LAW_2026-09-27.md` and O-151. This conditional splice law is proved; forced sharing for SIZE(s1) and any superlinear cover bound remain open.

### 2.264 - Global readout hardness can avoid dangerous splicing

Choose a random sparse subfamily W of an explicit set E of individually small-circuit truth tables, and classify W versus the entire remaining cube. Counting q-rule closure descriptions gives some W with superpolynomial fusion readout complexity, while the feature floor is still only linear. By choosing W with no Hamming-neighbor pair, every accepting certificate must pin all N table bits; a consistent proof-context splice can only identify a member already in W. This is a real artificial global-readout lower bound, but its source is arbitrary labeling, not a forced high hybrid. The rejecting side contains easy tables, so it is not Gap-MCSP. It narrows O-151: certificate width and anchor count alone cannot force the needed splice; actual low/high circuit geometry must be used. Full proof: `research/C228_RANDOM_SUBFAMILY_READOUT_CALIBRATION_2026-09-27.md`.

### 2.265 - The near-linear witness grammar must synchronize one description

The exact low-table predicate is an existential circuit description followed by N coordinate checks. A direct proof grammar assigns a separate chain to each description. Reusing a state across descriptions creates cross-combinations of side proofs that may no longer verify one common circuit; attaching the description to the state prevents that mix but costs one state family per description. This identifies the concrete upper-bound problem: compress the semantic class of unfinished circuit-evaluation obligations without losing global witness identity. C-227's context/subproof cross-product is the audit condition. The direct attempt gives no lower bound because carrier semantics could synchronize descriptions more cheaply. See C-229.

### 2.266 - Safe certificate cylinders have the Lupanov scale

The exact obstruction to a proof splice is not just the count of non-high tables; it is the largest full coordinate subcube contained in SIZE(s2), denoted kappa_square(s2). Counting bounds it by O(s2 log s2). A block of 2^k addresses sharing a fixed input prefix supports every Boolean labeling using a k-input Lupanov circuit, so kappa_square(s2)=Omega(s2 log s2) at fixed-beta OPS scales. Hence the maximum safe free-coordinate footprint is Theta(s2 log s2). Certificate width is tight up to constants. The useful O-151 target is a consistent splice leaving more than kappa_square coordinates free, or a distinct global invariant. See C-230; source is linked there.

## C-232 Ã¢â‚¬â€ Shared-DAG principle: descriptions do not share by themselves

The live model is the standard acyclic product-rectangle DAG for the C-75 signed mismatch relation. This is exactly the circuit complexity of a promise separator `h`, up to constant basis changes. Replacing a low truth table by one of its short circuit descriptions preserves the minimum DAG size exactly: lift Alice's state predicates through the evaluation map to go from tables to descriptions, and restrict to one canonical description per table to go back.

A same-output-alphabet calibration shows why short communication is too weak: for some Boolean `f` on N-bit inputs, the ordinary KW mismatch game has only N output labels and an O(N)-bit protocol, yet circuit counting plus the DAG/KW theorem forces `Omega(2^N/N)` DAG states. Parity supplies the opposite tree/DAG direction: shared gates can make a DAG much smaller than every protocol tree. Since every tree is a DAG, a small tree by vertex count cannot be harder than a large DAG.

For actual Gap-MCSP, the low description enables a cheap bit protocol but the universal-DAG attempt still computes `exists d forall k: w_k=G(d)_k`. Its direct circuit uses `N*2^(O(s1 log(n+s1)))` gates. The `2N` coordinate-mismatch rectangles are a small cover, but binary DAG nodes must be rectangles at every intermediate merge; arbitrary groups of those rectangles do not satisfy that condition. Each merged state must solve its complete row/column product hull, with disjoint projections on all descendant output coordinates. A global charge for those residual separators is the missing theorem.

Keep the transfer losses visible: `rho_prom<=O(S_rect)`, while the best recorded forward compiler is `S_rect<=O(rho_prom^3/log rho_prom)`. So a DAG lower bound of `N g(N)` with merely unbounded g does not force superlinear fusion q; the current target is `S_rect>N^(3+3epsilon)/log N`, or a near-linear construction that kills this route. The arbitrary-function calibration is not a Gap-MCSP lower bound. See C-220/C-232 and O-152.

The O-152 search must preserve the established ceilings `rho_w<=N-1`, `rho*=O(N)`, and `rho(H)=O(N log|H|)` for fixed semi-filter families; the live issue is adaptive/global reuse on the full low/high promise.

### C-233 addition Ã¢â‚¬â€ event-driven rank vs acyclic sharing

The fusion closure's least fixed point has a useful operational form: rule i activates one round after the slower of its best E-side and H-side proofs. Assign seeds rank 0 and each predecessor its first activation rank; then `tau_i=1+max(min E-support rank,min H-support rank)`. A Dijkstra-style worklist computes all finite ranks by settling each rule once and processing each support arc once, in `O(q^2 polylog q)` RAM time for a successful q-rule OPS cover. This explains why the cyclic system can be evaluated efficiently without a global topological order; rank-reversing SCCs remain possible because the order is input-dependent.

HeathÃ¢â‚¬â€œKolesnikovÃ¢â‚¬â€œOstrovsky tri-state circuits supply a nearby hardware model: cycles plus 0/1/Z signals and input-dependent gate firing. The direct fusion network is an `O(q^2)` one-sided recognizer (YES outputs 1; NO remains Z); a terminating RAM evaluator gives a total `q^2 polylog q` TSC separator. A partial-TSC lower bound above `N^(2+2epsilon+delta)` would force q superlinear. This is not an acyclic Boolean DAG, and its stronger model makes that lower bound difficult; the standard rect-DAG threshold `N^(3+3epsilon)/log N` is unchanged. Keep TSC, cyclic fusion complexity, and standard rect-DAG complexity distinct. Full derivation: `research/C233_MINMAX_ACTIVATION_RANK_AND_TRISTATE_RAM_BRIDGE_2026-09-27.md`.


### 2.267 - A shared state carries a residual obligation across every context

For state i, let K_i be all outside-context seed supports from accepting proofs with an occurrence of i, and S_i all seed supports of finite proofs rooted at i. Reuse gives the full Cartesian product: every K in K_i combines with every C in S_i. In a sound Gap-MCSP cover, each compatible union K union C must fix all but at most kappa_square(s2)=Theta(s2 log s2) coordinates. Therefore a replacement support C that leaves a large coordinate set free forces every compatible context to supply almost all of those coordinates. This is the native semantic obligation of a shared state; the unresolved cost is how the grammar represents all such contexts and residual supports.

### 2.268 - Repeating one small circuit exposes a block-hybrid amplifier

Choose k so all k-bit functions have circuit size at most s1/4 and 2^k=Theta(s2). Repeat one function g across r=N/2^k=Theta(N/s2) address-prefix blocks. Every diagonal table is low, while independent block choices range over all truth tables and almost all are high. If each accepting proof had disjoint block-local state occurrences, heavy state-label fibers and repeated substitution would force q>=2^(Omega(s2)).

The exact localization premise fails as a generic principle: the diagonal subpromise has an O(N)-size equality-of-blocks separator and an O(N)-pair fusion cover. The remaining task is to measure the nonlocal mixing that keeps contexts and replacement proofs synchronized, or show that this mixing itself costs q>N. This is a conditional amplifier, not a Gap-MCSP lower bound. See C-234.


### 2.269 - State reuse creates a description fingerprint and an ownership mask

For repeated low tables w_g(p,u)=g(u), a context support from g and a replacement support from h conflict precisely when they both pin some coordinate copy (p,u) where g(u) differs from h(u). Therefore the set of suffix inputs appearing in any overlap is a partial fingerprint of the whole k-bit function: h remains splice-compatible exactly when it agrees with g on that set.

At a suffix input outside the fingerprint, the repeated prefix copies cannot be pinned by both sides if g and h differ. Each copy is assigned to the context, the replacement, or is free. If all copies for each u are assigned to a single side, the splice completes to another diagonal table, still low by the k-variable synthesis bound. To create a high hybrid, the ownership pattern must vary across prefix blocks and carry enough global complexity. This makes the next target precise: charge fingerprint coverage or prefix-varying ownership across the entire cyclic grammar. C-234 proves the local algebra and conditional blockwise amplifier, but not the required global charge.

## C-235: interval semantics of proof reuse

A consistent dual-rail proof support defines a Boolean interval `[ell(S),u(S)]`: its positive literals set the lower endpoint, while the complement of its negative literals sets the upper endpoint. Combining supports intersects their intervals. Therefore a context/replacement splice has lower endpoint `ell(K) OR ell(C)` and upper endpoint `u(K) AND u(C)`. Every table in a sound output-proof interval, including both canonical endpoints, must lie in `SIZE(s2)`. The same join/meet rule holds for simultaneous substitutions at disjoint proof occurrences and for the complete E-side by H-side product at an output root.

This gives a new object for the global-sharing programme: the ownership endpoints generated by compatible products. A lower-bound proof might force one such endpoint to have circuit complexity above s2, avoiding reliance on a free cube larger than `kappa_square(s2)`. The law itself forces no such endpoint: the C-228 isolated-anchor example and the C-234 diagonal equality cover have only safe singleton intervals. Thus the unresolved theorem is global and OPS-specific: prove that a small grammar covering all of `SIZE(s1)` cannot keep every compatible endpoint join/meet inside `SIZE(s2)`, or construct a compact grammar that does. No superlinear fusion lower bound or P-vs-NP proof follows yet.

A relevant literature motif is AustrinÃ¢â‚¬â€œRisse (CCC 2023): their SoS lower-bound framework combines expansion of CSP incidence graphs with substitutions of variables by local Boolean functions, and they also prove an analogous monotone-circuit statement for monotone Boolean slice functions. This suggests exploring overlapping expander-local views instead of simple repeated blocks. The transfer is currently blocked: their complexity measure is SoS proof size/degree, whereas our target is native cyclic fusion readout, and no reduction maps the hard slice instances to the actual `SIZE(s1)` versus `CC>s2` promise. Treat it as a construction prompt, not a lower bound. See C-235.

## C-236: disagreement selectors expose the missing global charge

For two repeated anchors `w_g(p,u)=g(u)` and `w_h(p,u)=h(u)`, let D be their disagreement coordinates. A compatible splice produces low endpoints z. On D, each endpoint chooses the g-bit or h-bit. The selector `mu=(w_g XOR w_h) AND (z XOR w_h)` records that choice and is computed by a circuit of size `s2+2s1+O(1)`. For typical g,h, D has at least N/3 positions, so there are `2^(Omega(N))` possible masks, but only `|SIZE(s2)|=2^(o(N))` can arise from low endpoints. This is the exact mask-image cap imposed by soundness.

The cap still does not imply q>N: the q-state grammar may generate huge families of finite proof trees, and no global accounting links the grammar size to the masks in its compatible context/subproof products. The diagonal equality cover keeps the profile prefix-constant and demonstrates a safe O(N) strategy on that restricted class. Next seek a grammar-sensitive bound on mask-image entropy across all low-anchor pairs, preserving C-228 and C-230 counterchecks. This is a proved interface restriction, not a P-vs-NP result.

C-236 exact completion correction: every compatible selector mask mu yields not only low endpoints but a low mixed hybrid `H_mu=w_h XOR mu` that extends the support. The selector family is therefore a subset of `L_{g,h}={mu:H_mu in SIZE(s2)}` and contains at most `|SIZE(s2)|` masks, despite `2^(Omega(N))` possible assignments on a typical disagreement set. This is the exact object whose generation must be charged against q. No q bound follows yet.

## C-237: the safe selector width does not shrink on typical anchor pairs

For typical repeated low anchors g,h, their disagreement set still contains structured free regions that support arbitrary patches of size `Theta(s2 n)` while every completion remains in SIZE(s2). Below beta=1/2 one such region is an input-prefix subcube inside a single differing suffix column. At or above beta=1/2, use a controlled number of differing suffix columns and synthesize arbitrary prefix functions on each. This matches C-230's universal safe-cube dimension. The failed improvement is informative: randomness of anchor disagreement alone does not help; the needed invariant must charge how a q-state grammar locates and reuses the structured free sets. See C-237.

## C-238: whole-strategy witness mixing

A ranked proof DAG has one selected E and H witness per active rule state. If two accepted tables use the same predecessor topology, their witnesses can be mixed globally: use E seed labels from one and H seed labels from the other. The common acyclic topology makes the mixed proof finite; consistency of its support implies every completion is accepted and hence low. Thus a state skeleton carries a full E/H product obligation, not only a local context/subproof pair.

The raw count is not enough: a fixed q-rule list can have `2^(O(q log q))` such skeletons, much more than the repeated-anchor family at q>=N. The target is a recurrence-specific restriction on which topologies can cover all low circuits, or a proof that a large topology fiber necessarily creates a high compatible selector. This is a proved structural law with no q bound yet. See C-238.
## C-239: canonical rank fibers and the splice duty of a shared state

The least-fixed-point activation-rank vector alone does not determine the witness skeleton: for a nonmaximal side, a seed and a predecessor can yield the same state rank. C-239 gives an endpoint-realizable two-rule counterexample. The augmented profile of both side-support minima at every state does determine one canonical proof skeleton: use a seed at side rank 0 and otherwise the least-index predecessor attaining the minimum; the root is the least active empty-carrier rule. Equal-side-rank accepted tables share a skeleton and obey C-238's global E/H cross-product. For fixed Q the profile is determined by its 2q-bit seed signature, giving at most 2^(2q) canonical fibers. This sharpens the count for the canonical choice, not the set of all possible witness topologies, and is still too large for pigeonholing at q>=N.

For each reusable state i, collect outside contexts K from accepting proofs with a marked i occurrence and finite replacement supports C rooted at i. Every pair K,C yields an output proof on their union. Soundness forces a precise condition: either K and C conflict on a dual rail, or their union fixes all but at most kappa_square(s2)=Theta(s2 log s2) coordinates. Equivalently, their free-coordinate sets intersect in at most kappa. This is the semantic obligation a global sharing theorem must charge to q; no such extremal charge is known.

The blockwise circuit-description upper-cover attempt still fails at residual synchronization: after checking address blocks, the program must preserve that one size-s1 circuit description agrees with every block. Resetting the description per block admits Frankenstein hybrids. There is no compact residual-family update in hand. C-234's linear equality cover warns that this difficulty must be tied to the full low-circuit class, not diagonal coherence alone. Detailed proof and limitations: C-239.
**Failed toy calibration.** The monotone clique promise offers a global-witness lower-bound model, but its accepting clique cylinders are too wide: fixing the edges of a clique leaves almost all graph bits free, and every completion remains YES. Exact adjacency would need negative rails and no longer inherits the monotone lower bound. The toy therefore fails C-230's narrow-safe-cylinder condition; a useful artificial model must preserve the dense high side and make every accepting cylinder narrow. See C-239.
The toy cannot be used to infer anything about the actual fusion model. Its lesson is only a filter for future artificial constructions: preserve dense high inputs and narrow safe cylinders while retaining a provable global-sharing lower bound.
A further failed counting route: for repeated anchors w_g(p,u)=g(u), one seed-literal test at a chosen prefix copy for each suffix u recovers the entire k-bit truth table g. Thus only Theta(s2) seed tests can distinguish all repeated anchors, while the active q floor already supplies at least N-o(N) states. Rank/seed-profile pigeonholing cannot force collisions on this family. The successful-cover constraintsÃ¢â‚¬â€not raw signature capacityÃ¢â‚¬â€must do the work. This is a capacity observation, not a fusion-cover construction; see C-239.

## Shared-DAG model for the C-75 promise (C-241)

For Y=SIZE(s1) and Z equal to all N-bit tables outside SIZE(s2), the signed mismatch relation is total on Y x Z. Its standard acyclic rect-DAG complexity is exactly the Boolean separator-circuit size up to constant/input-source conventions. One direction turns circuit gates into product rectangles; the reverse direction combines the two child separators using the two-rectangle product-cover trichotomy.

This gives the main model lesson: if G:D->Y maps descriptions onto low truth tables, then a DAG on (d,z) for Mis(G(d),z) has exactly the same minimum size as a DAG on (w,z). Pullback gives one inequality and a section gives the other. Circuit descriptions reduce communication bits to O(s1 log(n+s1)+logN), but do not give a graph-size discount. The direct construction asking whether there exists one d that matches all N coordinates, and the dyadic restriction-profile router, are exponential; the 2N mismatch rectangles are nondeterministic certificates, not a deterministic DAG.

Sokolov's communication PLS is also acyclic. Rank-layering a q-rule fusion path uses O(q^2) PLS states and O(log(q+N)) bits to choose a support; the generic PLS-to-Boolean simulation then costs O((q^2+N)(q+N)^3), worse than the direct O(q^3/logq) rank/support compiler. The q-state closure remains a distinct input-ranked cyclic model, not a standard PLS or rect-DAG. See C-241 and Sokolov's Theorem 3.1.

The proved transfer chain is rho_prom<=O(S_rect)<=O(rho_prom^3/log rho_prom), with D_cap<=rho_prom^2 and rho_prom=D_cap^circ. Therefore the generic DAG target is above N^(3+3epsilon)/logN to force rho_prom>N^(1+epsilon). SCC-sensitive compilers can reach O(q^2) only for covers with largest rule-SCC at most sqrt(q); arbitrary covers still have the cubic/log loss. The active new theorem target is a global product-hull charge for adaptive/revisiting DAGs or a near-linear separator. The local projection constraint is necessary but has no global charge yet. This phase has no actual-promise superlinear lower bound or P-vs-NP proof. Full audit: C-241.
The C-240 empty-root normal form does save part of the seed-evaluation term: if m empty output rules have complementary singleton seed vocabularies, C-91's seed cost becomes O((q-m)N+m), and the refined SCC compiler is O((q-m)N+m+E_ext+sum_C(r_C e_C+r_C^2)+q). It does not reduce the cost of predecessor OR routing or rule feedback; a dense SCC still leaves a cubic upper-bound term. So this is an instance-sensitive improvement only, not a near-lossless general compiler.


## C-242 update Ã¢â‚¬â€ Certificate grammar and blocker interaction (27 September 2026)

**Priority.** The latest attached instruction restores native cyclic closure as the main route. Work on O-153 first: derive a grammar-wide global-sharing/splicing theorem for the actual Gap-MCSP promise. Pursue an explicit N polylog N or N^(1+o(1)) full-promise cover independently. Standard acyclic rect-DAG analysis is secondary unless it improves the native compiler or supplies a direct q-invariant.

**Certificate algebra.** The q-state least fixed point is an antichain-valued AND/OR grammar over signed truth-table literals. At each state, alternatives on each side are unioned and minimized; the E and H obligations combine by pairwise union of their supports. The least solution is exactly the inclusion-minimal finite proof supports, and every minimal support is witnessed by a proof of height at most q. Reuse is exact: every outside context K for state i combines with every replacement support C rooted at i.

**Soundness obligation.** A consistent support defines an interval [ell,u] of all tables extending its signed literals. Every compatible context/replacement splice must have its whole interval inside SIZE(s2). In particular ell is the OR of its positive rails, u is the AND of its negative-rail complements, both endpoints must be low, and the free-coordinate intersection is at most kappa_square(s2)=Theta(s2 log s2). This interval law is stronger than a width-only condition, but does not yet charge sharing to q.

**Dual view.** On any high table z, each inactive state has at least one side with no matching seed and no active predecessor. Fixing such a side at every inactive state gives a blocker map. Following it through a ranked accepting proof for a low table w stays in states active on w and inactive on z, then terminates at a signed literal distinguishing w from z in at most q state visits. This is a useful exact pairwise normal form; path length alone does not exceed the known logarithmic-depth obstruction.

**Failure lessons.** C-230 makes the safe-cube width threshold tight. C-228 gets superlinear readout for individually easy anchors by counting, but compatible safe splices only identify existing positives; it is not an OPS splice mechanism. C-234's blockwise splice amplifier requires proof localization, while the diagonal-only promise has a linear equality cover. The missing theorem couples high blocker maps to the grammar's compatible low-interval join profiles and charges either avoided dangerous joins or compact semantic synchronization. No such theorem or full-promise cover is known. See C-242.


### C-242-A Ã¢â‚¬â€ Native prefix trie calibration

A fixed-order native cover can share prefix intersections: one state carrier for each realized low-table prefix, built by intersecting the parent carrier with the next matching literal slice. At prefix length N-1, the two completions are both in SIZE(s2) by one-point patching; hence the high-side carrier is empty. The construction has q<=sum_t |pi_t(SIZE(s1))|<=N|SIZE(s1)|. C-212's Theta(s1)-coordinate shattering makes its first Theta(s1) levels exponential, so this specific trie cannot reach N polylog N. The failure is limited to a fixed-order prefix architecture; it says nothing about adaptive or non-prefix joins.

**Context-dominant safe reuse.** A shared rule state can occur after an outside proof context has already fixed all N coordinates of its anchor. Every compatible replacement then leaves the output singleton unchanged, so the state collision creates no hybrid. A q lower bound must charge how anchor-specific context information is assembled and shared, not count state visits alone. This is the immediate obstruction to turning the blocker-path lemma into a splice theorem.


## C-243/C-244 Ã¢â‚¬â€ carrier geometry and state-zone readout

Use three semantic objects for each closure state i: its carrier T_i, its proof language P_i, and its accepting-context language K_i. A proof cylinder's high portion must lie inside T_i, yielding a local carrier-volume constraint. More globally, the whole accepted language factors exactly as the union of q zones Z_i=[P_i] AND [K_i]. Every low table lies in a zone; every zone is entirely inside SIZE(s2). This is the precise global footprint of state reuse.

The central quantity is not the number of proof trees or the size of T_i alone, but the joint generation complexity of P_i and K_i under one cyclic grammar. Their cross-product must cover every low circuit while every compatible support union remains a low-only cylinder. A high table blocks one side of every zone. The missing theorem is a q-sensitive bound on how much low-circuit description mass one such grammar-generated zone can safely cover; carrier-volume sums fail under correlated intersections, and zone counts hide exponentially many derivations.

Keep C-228's safe singleton splices and C-234's diagonal equality cover as hostile checks. The counter-program remains an explicit N polylog N / N^(1+o(1)) cover for the full promise. C-244 is an exact global decomposition, not a lower bound or P-vs-NP proof. Full derivations: research/C243_CARRIER_VOLUME_AND_CERTIFICATE_PACKING_2026-09-27.md and research/C244_STATE_ZONE_FACTORISATION_AND_GLOBAL_READOUT_2026-09-27.md.


### C-245 Ã¢â‚¬â€ Marked proof grammar as automatic differentiation

Represent a proof support by an antichain-semiring value. A context with one hole is its first-order marked component: across an AND of the two rule obligations, the hole goes through one branch and the other branch is an ordinary proof. Thus proof families and all state-context families are generated jointly from the same q-state grammar. For zone membership, arbitrary context unfoldings can be shortened to height 2q while retaining the marked state, so all zones have a bounded marked-grammar description.

This identifies the exact algebra of global reuse, but it does not charge the grammar: there are q^2 marked family labels and exponentially large support antichains may still occur. Continue by seeking a bounded-by-q invariant of their joint incidence and safe endpoint profiles. Keep C-228 singleton safety and C-234 diagonal equality as hostile checks. See research/C245_MARKED_ANTICHAIN_GRAMMAR_FOR_CONTEXTS_2026-09-27.md.


### C-246 Ã¢â‚¬â€ Certificate volume is not readout cost

On repeated-block anchors, a safe support cube covers at most 2^(kappa/r) diagonal functions: a suffix value can vary only when all r copies are free. This can force exponentially many distinct supports to cover the low family, yet q states have enough witness choices to generate up to exp(O(q log(N+q))) certificates. At the known linear q floor this count is already much larger than exp(Theta(s2)).

Therefore the size of an antichain certificate family is not a state lower bound. The cost lies in arranging its members so every context/replacement cross-join remains low. Keep the safe-cylinder calculation as a calibration, and seek a semantic invariant of the joint context/proof incidence tensor. C-246 gives the inequality and exact failure.


### C-247 Ã¢â‚¬â€ Multi-hole splice entropy

A proof may have several disjoint occurrences available for replacement. Their choices are not merely pairwise: every globally consistent tuple produces an accepted output proof. If the replacement slots expose disjoint private coordinate regions, the choice tuple injects into the resulting table, so the product of slot entropies is bounded by log|SIZE(s2)|.

This is the general product budget behind C-234's conditional block hybrid. It explains the failure precisely: low q does not yet imply private slots; the diagonal equality construction avoids them by copying a full description fingerprint into the context. Seek a structural dichotomy that charges either independent replacement entropy or the circuit-description synchronization required to suppress it. Information-only charges max out at the N-bit scale and cannot yield superlinear q. See C-247.


### C-248 Ã¢â‚¬â€ Blocker rectangles are the global sharing unit

For each fusion state i, the low tables where it activates and the high tables where it is inactive form a full product rectangle R_i=A_iÃƒâ€”B_i in the canonical low/high mismatch relation. If a high table blocks one rule side, every low table activating that state supplies a witness on that side. The witness is either a signed coordinate mismatch or a predecessor state, so R_i recursively routes through mismatch rectangles and other R_j rectangles. All pairs in the cross-product must be handled; sharing cannot be analyzed pair by pair. The path terminates because low-side activation rank decreases.

This is a precise global interpretation of native state reuse, but not yet a lower-bound measure. Any disjoint promise has a trivial cover by its 2N signed mismatch rectangles, so area or rectangle-cover counting cannot force superlinear q. A sharper hostile example has Y equal to all nonconstant tables and Z={0^N,1^N}; one fusion rule with endpoints {1^N} and {0^N} accepts exactly Y, yet its single state rectangle is all of YÃƒâ€”Z. Different pairs use different coordinate mismatches. This confirms that cross-swapping low/high pairs does not construct a mixed truth-table hybrid. The obstruction is the organization of one globally shared two-sided recursive routing grammar for the actual low/high circuit promise.

Unrolling the q-state least fixed point for q rounds also yields a monotone promise-separator extension with at most 3qÃ‚Â²+1 unbounded-fan-in gates (gate count only). The input-incidence cost is O(qÃ‚Â²(N+q)), cubic at qÃ¢â€°Ë†N, so this does not improve the bounded-fan-in transfer. AustrinÃ¢â‚¬â€œRisse's monotone-slice results concern SoS refutation size; no bridge turns them into a lower bound on this separator or on q. Continue O-153 and the independent near-linear full-promise cover search. Full details: research/C248_BLOCKER_RECTANGLES_AND_MONOTONE_EXTENSION_COMPILER_2026-09-27.md.


### C-249 Ã¢â‚¬â€ Output roots have a two-sided escape normal form

In the actual parameter regime, the high side U intersects every signed literal half-cube. For any low table, select an active empty-carrier root of minimum activation rank. Both its endpoints must be nonempty: an empty endpoint admits no nonempty seed slice, and any predecessor carrier inside it would itself be empty and therefore an earlier output root. We may ignore degenerate roots when covering low tables.

Each normalized root has disjoint nonempty endpoints E_i,H_i. A high table z_EÃ¢Ë†Ë†E_i blocks its H side, and z_HÃ¢Ë†Ë†H_i blocks its E side. C-240's two-coordinate shattering normal form says the root's direct seeds are either one complementary literal pair on one coordinate or are absent on one side; every accepting derivation must enter a predecessor. Hence the first escape is selected by at most one table bit or is forced through a predecessor side, and it can be paired with a fixed high blocker independent of the low anchor.

This is an exact root-to-escape description, not a lower bound: predecessor row sets may be reused by many roots and anchors. The next missing result is a global charge for those escapes after context/proof cross-joins, or a compact cover using them. See research/C249_BIBLOCKED_OUTPUT_ROOT_NORMAL_FORM_2026-09-27.md.


### C-250 update: a half-safe predecessor lemma, not yet an aggregation principle

At a seedful empty-carrier output root, a low anchor matching direct literal (k,b) must escape on the opposite side through a predecessor. The matching high half-cube is contained in the seed side's endpoint and disjoint from the opposite endpoint. C-243 transfers this exclusion to any predecessor proof support C: no high table extending C can have bit b at k. Hence at least half of Cyl(C) is contained in SIZE(s2), giving `free(C) <= ceil(log2 |SIZE(s2)|)+1`.

This sharpens the local semantics of escape proofs. With repeated coordinates it caps seedful support capacity at `2^((kappa+1)/r)` anchors. Yet the same first failure persists: many required certificates do not imply many states, because one q-state grammar can have `exp(O(q log(N+q)))` ranked witness-DAG descriptions. The lemma does not cover seedless roots, whose proofs require two-sided joins. The useful next question is whether the same state reuse that organizes many half-safe supports forces a large compatible context/proof splice family. No such aggregation theorem or P-vs-NP proof has been established. Full derivation: `research/C250_ONE_SIDED_SAFE_ESCAPE_CYLINDERS_2026-09-27.md`.


### C-251 update: every root escape has a safe support signature

The seedless branch can be expressed cleanly in the same support language. At a normalized empty output root, a low anchor either matches a direct root seed, leaving an opposite-side predecessor with the one-sided C-250 bound, or matches no direct seed. In the latter case both sides require predecessor proofs. The union of their supports is consistent, and every completion preserves both branches and activates the empty root; soundness therefore makes the entire union cylinder low. Its free-coordinate count is at most `floor(log2 |SIZE(s2)|)`.

Thus each accepted anchor has a safe one-support or paired-support escape signature, including seedless roots. Repeated-block projections bound each signature's anchor capacity by `2^((kappa+1)/r)`. This closes a local coverage gap, but signature pairs are still too numerous: their ranked proof-DAG count is `exp(O(q log(N+q)))`, so counting cannot yield a superlinear state bound. The actual frontier is cross-root incidence: show that extensive reuse of support states forces a high cross-join or costs extra states, or build a near-linear full-promise cover. No P-vs-NP proof follows. Full derivation: `research/C251_ROOT_ESCAPE_SUPPORT_DICHOTOMY_2026-09-27.md`.


### C-252 update: quotient escape support to a state-conflict graph

The one-sided and paired support signatures can be aggregated by the predecessor state IDs. For each empty output root i, connect every E-predecessor j to every H-predecessor k. A high table cannot activate both states, because C-243 would put it in the root's two disjoint endpoints. Direct seed/opposite-predecessor choices add forbidden incidences between a state and a signed input literal. Every low anchor accepted at an empty root activates either a conflict edge or a seed/state incidence. This yields a depth-two readout with at most `q^2+2qN` terms over the q state predicates and input bits.

This is a genuinely smaller *description of the splice interface*: it aggregates exponentially many proof supports into a finite graph and labelled incidences. It does not yet give a smaller circuit compiler, because the q activation predicates remain cyclic least-fixed-point functions; with the existing OPS floor q=Omega(N), unrolling plus readout costs O(q^2). High activation profiles are independent sets of the graph, but independent-set counting says nothing about fibre sizes; many truth tables may share a profile. The next proof target is a structural restriction on these fibres from the promise, or a near-linear cover. No q lower bound or P-vs-NP proof follows. Full theorem: `research/C252_STATE_CONFLICT_GRAPH_READOUT_2026-09-27.md`.

### C-253 update: profile fibres have marker subcube bounds

For each exact activation profile sigma, a conflict edge implies the whole profile fibre is low. For a conflict-free profile, the seed markers attached to its active states separate low and high members: every low table matches at least one marker and every high table avoids them all. Thus the high part of this fibre lies in a subcube fixing each marked coordinate, with at most 2^(N-r_sigma) tables. If both marker polarities occur at one coordinate, the high fibre is empty.

The entropy sum proves only that some profile actually used by high inputs has at most q+o(1) marked coordinates. It may have no low members, so it yields no state lower bound. The next missing principle must couple activation profiles used by low proofs to those covering U, using the positive cyclic equations under coordinate flips or partial assignments. No P-vs-NP proof follows. Full derivation: research/C253_CONFLICT_PROFILE_FIBRE_SUBCUBES_2026-09-27.md.

### Literature boundary from C-252

The 2025 Cavalar?Oliveira paper proves that, in its general finite discrete setting, fusion cover complexity equals cyclic intersection complexity exactly (Theorem 3, https://arxiv.org/abs/2503.14117). This validates the native cyclic closure as an exact target model, while also warning that a new encoding of its states is not itself a new lower-bound method. C-252's state-conflict graph is distinct from the paper's bipartite graph-complexity constructions. The project still needs a quantitative theorem for the specific low/high circuit promise, or a matching compact cover.

### C-254 update: hazardous supports form a high-rank boundary

For a partial table support C, activate a state when it has a finite proof whose leaves all match C. This activation is monotone under adding literals. If C activates a conflict edge, or an active state paired with a marker literal, the corresponding empty root activates for every completion. Soundness therefore makes the whole cube low, forcing |dom(C)|>=N-log2|SIZE(s2)|. Every coordinate ordering of a low input reaches its first hazard only near the top of the Boolean lattice.

Correction: choose the active C-252 readout term and compress its finite least-rank proof into a DAG with at most q distinct state labels and at most two seed leaves per state, plus one marker literal. Its hazardous support has width <=2q+1, so C-254 yields q >= (N-log2|SIZE(s2)|-1)/2. This is valid but weaker than the existing N-o(N) floor. Any further gain must aggregate selected witness DAGs across anchors with overlap control; raw chain activation counts still do not suffice. See corrected C-254.

### Literature check: approximate MCSP magnification is not yet a P-vs-NP bridge

Point-patching implies that a table outside SIZE(s2) is at Hamming distance at least (s2-s1)/O(n) from every table in SIZE(s1), where n is the truth-table input length. Thus an exact Gap-MCSP lower bound can transfer to a stronger approximate-MCSP promise when the approximation radius is smaller than this gap. Atserias?Muller (2025) give uniform magnification thresholds for approximate MCSP, but their stated endpoints are NP not subset NC1 or P different from NP^oplusP, not P different from NP. This route is worth retaining as a parameterized side implication, but it does not replace the O-153 fusion target. Primary source: https://arxiv.org/html/2503.24061.


### C-255 update: the shared object is a residual product hull

The active model is now the standard acyclic rect-DAG for the total signed-mismatch relation on the low/high promise. A state is not merely a coordinate subset or a circuit-description prefix: it owns a product rectangle, and its entire descendant suffix must solve every cross-pair in that rectangle. Description-space and truth-table-space DAG sizes coincide exactly. The known compiler from a q-pair cyclic fusion cover still loses a cubic/log factor because input-dependent ranks require q^2 contexts and those contexts need support routers. The missing invariant must charge residual product hulls globally without double-counting overlapping high projections. C-255 records exact model boundaries, the exponential universal construction, transfer threshold, and failures; no new lower bound follows.

### C-255 added lead: bottleneck counting on mismatch slices

The ICALP 2025 BeameÃ¢â‚¬â€œWhitmeyer triangle-DAG lower bound gives a concrete shared-state method to test: map many one-sided inputs to bottleneck states and prove that each state can absorb only a small fraction. For C-75 define `lambda_v(w)` as the minimum number of descendant signed-mismatch labels covering the slice `{w} x B_v`; it is at least `N-log2|SIZE(s2)|` at the root and one at an output leaf. The missing theorem is a node-capacity bound using circuit-class shattering and high-side density. A separate common-translate lemma solves the high-image part of a source reduction: choose `r` outside `SIZE(s1) xor SIZE(s2)`, then every low base table `u` maps to a high table `u xor r`. What remains is cut soundness: every diagonal/off-diagonal signed mismatch rectangle induced by the source code must be a valid answer under a fixed decoder. C-255 gives the exact conditions and parameter scale. This is a candidate route, not a C-75 lower bound.
### C-256 model update: answer soundness can reveal the hard translate

The common translate is not a free black-box wrapper. On a rich KW source, fixed-label cut soundness forces every active address bit to copy a source coordinate, with the same phase on Alice's low table and Bob's translated table. A finite test family (0^M, all e_i, and 1^M) then reconstructs the translate as r=v_{1^M} xor u_{0^M} xor OR_i(u_{0^M} xor u_{e_i}). The circuit cost O(Ms1) collides with the OPS gap when M=Theta(log N) and the constants satisfy the transfer threshold. For full-domain BPHP, the analogous obstruction is combinatorial: one target coordinate has only two signed labels, so static decoding would cover all Alice assignments by two fixed collision-equality predicates, impossible.

This teaches a source-transfer filter: for each source answer, take its Alice and Bob projections, and compute their cover numbers. If tau_X>2 and tau_Y>1, one target bit cannot statically decode both signed mismatch cells: any active bit must vary on both sides, after which its two labels cover X by only two answer projections. BPHP has this obstruction because each answer's projections lie inside one fixed collision-pair equality set, and two such equalities never cover a full assignment domain. Terminal-specific decoding can evade this filter only by using path-refined rectangles; if a target DAG has S sinks and each sink rectangle needs a source-search refiner of size at most T, substitution costs at most S(1+T). The quantitative target is to keep S(1+T) below the source lower bound while S itself exceeds N^(3+3epsilon)/log N. No target lower bound follows from C-256. The live proof target remains the actual C-75 shared product-hull bottleneck-capacity theorem or a near-linear DAG.

## C-260 - Two-sided proof/blocker model

Treat a native closure as one cyclic grammar generating two dual families over the signed-literal seed alphabet:

- `C_i`: minimal present-feature certificates that activate state i;
- `B_i`: minimal absent-feature blockers that keep state i inactive.

The least-fixed-point proof and blocker recurrences are De Morgan duals, so `B_i=Tr(C_i)` exactly. At the output, `C_out` covers accepting inputs and `B_out` covers rejecting inputs. On actual tables, any low certificate and high blocker intersect in a literal expressing a truth-table mismatch.

State reuse has its own exact convolution: a context support K with a hole at i joins every replacement proof P at i whenever `K union P` is consistent. Every such join is an accepting certificate and is hit by every output blocker. The useful global object is therefore the incidence geometry of `(K,P,B)` under one shared q-rule grammar. Merely knowing each join intersects each blocker is too weak: one literal can hit many joins, while C-257 parity and C-258 equality fingerprints show safe reuse can be organized linearly.

C-260 also isolates what is already forced by pigeonholing. On a repeated-block family with `2^d` low anchors and `d log d=O(s1)`, every minimum-rank empty-root proof continues to an internal predecessor by C-249. Hence one internal state is used by at least `2^d/q` anchors. This does not force dangerous reuse: C-258 builds an O(N) cover of exactly this family, where equality fingerprints keep the joins safe. The missing theorem is not Ã¢â‚¬Å“some state is shared,Ã¢â‚¬Â but Ã¢â‚¬Å“sharing creates a large compatible context/proof product unless q pays to encode its fingerprint.Ã¢â‚¬Â

Current next theorem target: bound this incidence geometry by q strongly enough to force more than `Theta(n)` independent high-entropy splice choices, a hard ownership selector, or a superlinear cost for suppressing both. In parallel, preserve the same small-circuit description across all address checks in any near-linear upper-cover attempt. C-260 is an exact structural model, not a q lower bound or a P-vs-NP breakthrough.

## C-261 to C-265 Ã¢â‚¬â€ Source hardness, bridge tax, and synchronization

The model now separates three quantities that used to get blended together:

1. **Source hardness.** A powerful monotone lower bound can survive the native cyclic least-fixed-point syntax. For v-vertex bipartite matching, q cyclic AND states unroll into a monotone separator of size O(q^2(v^2+q)); Rao's exp(Omega(sqrt(v))) lower bound therefore yields CycAnd(MATCH_v) >= exp(Omega(sqrt(v))). Cycles reduce the exponent only by a constant factor. This is a theorem about the matching promise, not about Gap-MCSP.
2. **Bridge tax.** The C-125/C-126 map is the decisive missing implication. With v=A(ln N)^2, the source has only Theta(log^4 N) edge inputs and can exceed N^(1+epsilon) by a constant choice of A. YES completion circuits of poly(v) fit every fixed s1=N^beta/(c log N). The unresolved resource is the AND cost of a monotone map that also guarantees a high completion on every NO input.
3. **Description validity.** LowExt ranges over every low truth table. A syntactically intended matching witness does not suffice: constant tables and one-bit perturbations are also low. The map must make global code validity follow from monotone partial rails. This is the exact failure in the direct sparse-edge encoding.
4. **Synchronization.** Shared-state reuse is safe when a compact fingerprint forces compatible descriptions to agree. C-258 does this with block equality at O(N) cost. The desired lower bound cannot charge state collisions, row counts, or blocker hits alone; it must show that all low circuit descriptions require many distinct synchronization relations in one q-rule grammar.
5. **Upper-bound budget.** Independent cofactor choices consume circuit description size multiplicatively. The size gap allows only O(log N) independent size-s1 pieces, while trivial unrestricted leaves require N^(1-beta+o(1)). Therefore a near-linear cover, if it exists, must preserve one shared description through a global evaluation or use a new semantic quotient.

### Current checkpoint

The full Gap-MCSP native fusion bound is still q=N-o(N). The new matching result is source-side only. Primary open edge: construct or rule out the C-125/C-126 LowExt map at the quantified cost. Parallel native edge: a synchronization-versus-splicing theorem that survives C-258 and C-257. The full-promise near-linear cover remains the required falsification test. See research/C261_MATCHING_CYCLIC_LOWEXT_AND_GLOBAL_ROUTE_AUDIT_2026-09-27.md.

## 27 September 2026: revised success criterion and two primary routes

The latest research instruction changes what counts as meaningful progress. Do not accumulate local lemmas unless one immediately crosses a route threshold. A major result must do at least one of the following:

1. prove `q >= N g(N)` for an unbounded `g`;
2. build a full-promise `N^(1+o(1))` native fusion cover;
3. give a near-lossless transfer from a genuinely hard source into native fusion;
4. prove a global native-sharing theorem that does not collapse to one-anchor, certificate-width, or local-profile arguments.

The actual promise fusion lower bound remains `q=N-o(N)`.

### Primary route A: cyclic monotone hardness into LowExt

The source side is now proof-checked. Rao's spread-matching theorem gives `exp(Omega(sqrt(v)))` monotone circuit hardness for perfect matching versus graphs with no `v/4`-matching. A q-state cyclic intersection program has an inflationary least-fixed-point evaluation that stabilizes in q rounds; flattening its free union states and unrolling gives an ordinary monotone separator with `O(q^2(v^2+q))` gates. Therefore the matching hardness does survive native cycles, with only a polynomial loss, and `CycAnd(MATCH_v)=exp(Omega(sqrt(v)))`.

Set `v=A(log N)^2`. If a monotone map `phi` into signed partial truth tables has AND-cost `a<=N^eta`, then the exact C-125/C-126 transfer forces `q>N^(1+epsilon)` whenever `c' sqrt(A)>max(1+epsilon,eta)` with fixed margin. `poly(v)` low witness circuits fit `s1=N^beta/(c log N)` for every fixed `beta>0`. This resolves the parameter issue; it does not construct `phi`.

`LowExt` quantifies over every low truth table. A source matching witness family alone is not enough: universal zero rails admit a constant-zero completion on NO inputs. A fully pinned hard baseline is also blocked if every YES witness changes it on an efficiently described mask of cost at most `s2-s1`, because that makes the baseline itself an `s2`-size table. Thus the map must encode global code validity while retaining hidden high-completion hardness in coordinates not already pinned on NO inputs. Ilango's ETH-hard partial-MCSP reduction offers an optimal-description synchronization motif, but it supplies neither the required monotone AND budget nor high NO completions.

**A's exact frontier:** a low-AND monotone signed-rail map with low YES completion, high NO completion, and cost below the cyclic source bound. Do not count source hardness as Gap-MCSP progress until this map exists.

### Primary route B: global synchronization versus independent splicing

The strongest available object is the q-grammar's context/proof compatibility relation paired with output blockers. A context with a hole at state i can join every replacement proof at i whose support union is consistent; every such join's whole completion cylinder lies in `SIZE(s2)`. This is the actual global synchronization law.

The equality-fingerprint test is mandatory. C-258 covers an exponential repeated-block subfamily of low tables with `2N+2d-1` native pairs, synchronizing reused descriptions at linear cost. So counts of compatible pairs, number of rows, blocker hits, or mere state collisions do not force superlinear q. A theorem must show the full `SIZE(s1)` language needs many mutually incompatible synchronization relations or else yields a splice family with more than `|SIZE(s2)|` members.

An expander-overlap family is a candidate construction: low tables would expose local views of one latent short circuit across many overlapping coordinate sets; independent splices should usually destroy global circuit simplicity. This has not been constructed or proved. It must be tested against the possibility that one shared O(N) fingerprint scheme synchronizes all views.

**B's exact frontier:** prove a dichotomy between a forbidden global splice product and superlinear cost to represent circuit-description compatibility. Any local width, certificate-count, or endpoint-description argument is insufficient by itself.

### Bounded secondary routes

- **Terminal-specific BPHP refinement:** static mismatch labels fail. A generic fixed-hole answer-rectangle cover has `Theta(m^2 2^{n0})` pieces per sink, which is `N^{Theta(K log^3 N)}` at `n0=K log^4 N`; this destroys the source exponent. Such a cover is not automatically a binary rect-DAG, since unions of rectangles need not remain rectangles. Progress requires an honest DAG refiner and a theorem that actual sink preimages localize the hole values.
- **Closure compiler:** the input-dependent worklist scans q activations and E<=2q^2 support incidences once, but a direct Boolean circuit replays E incidences for q rounds. An oblivious queue/routing circuit of near-E size is unproved; dynamic state selection and writes must be counted.

### Research discipline

After every 3-5 claims, explicitly compare the actual q lower bound with its previous value. The latest five-claim checkpoint found no change. Continue only at the four global frontiers above, retain exact cost models, and label claims using the project's fixed classification list. Current detailed report: [C-266 to C-270](research/C266_CYCLIC_MATCHING_LOWEXT_AND_SYNCHRONIZATION_AUDIT_2026-09-27.md).

### Route 4 check: universal-circuit quotient attempt (C-271)

Explicit circuit-description enumeration costs `N*2^{O(s1 log(s1+n))}`. Merging candidates only by block restriction loses the same-circuit-across-addresses condition, while a product of independent cofactors stays sound for O(log N) blocks and cannot reach a trivial synthesis base. A state per exact subfunction is already superpolynomial on sparse-indicator restrictions. These failures apply to those implementations only; they do not rule out an implicit global semantic quotient. Current q remains `N-o(N)`. See [C-271](research/C271_NEAR_LINEAR_UNIVERSAL_CIRCUIT_QUOTIENT_AUDIT_2026-09-27.md).

## C-272/C-273: overlap entropy and example-to-table scale

C-272 gives overlapping low tables from expander edge views and many high independent hybrids, but one fixed consistency system has a compact checker and no native q-charge is proved. The extension to many incompatible wirings remains an open synchronization theorem.

C-273 isolates an order mismatch in the direct example-list encoding. For specified rails P and a fitting low table w, P<=e(w), while C-125 needs e(w)<=phi(YES). The standard upper-completion encoding reverses this order but turns every unspecified coordinate into a two-rail conflict, so it cannot lie below a one-hot NO code. Sparse consistent examples nevertheless have abundant high completions by counting: with m=poly(logN), only m of N=2^d locations are fixed, while log|SIZE(s2)|=o(N). C-125 does not prohibit simultaneous low completions on NO inputs. Thus the NO side is cheap here; the open construction is a single source-monotone map with the asymmetric orders and affordable AND cost. The cited 2026 result supplies conditional sample-agreement hardness, not that map.

Checkpoint after C-271-C-273: q remains N-o(N). Current viable frontiers are O-157/O-163's source-monotone asymmetric rail map and O-158/O-162's global synchronization-versus-splicing charge; do not promote example hardness, hybrid entropy, or local counts to an actual q-bound improvement.

## C-274: Patchable conflict support must be broad

For a C-125 monotone map, let S be the coordinates where any YES image activates both rails. Joining two YES inputs shows that their selected low witnesses agree outside S. If the shared restriction outside S is all a NO image specifies, a high completion would be a patch of one low table on S. Point-minterm patching costs O(logN(|S|+1)); therefore if |S|<=Theta((s2-s1)/logN), conjoining the fixed outside-S rails computes the source with at most a+N-1 AND gates. Any map saving more than N gates against the source lower bound must instead use Omega((s2-s1)/logN)=Omega(N^beta/logN) globally conflicted coordinates. This strengthens C-127's logN support condition, but permits broad support and does not improve q. Exact proof: research/C274_CONFLICT_SUPPORT_PATCHING_OBSTRUCTION_2026-09-27.md. Next test whether broad conflict can be distributed sparsely over YES inputs without making NO rails conflict.

## 2.48 - Conflict support and transfer feasibility

A monotone map from a hard source to `LowExt` has a global obstruction: selected low witnesses on all YES inputs agree outside the coordinates where some YES image contains both rails. If that conflict union is small, the map plus an AND of the common rails already separates the source. Sparse block decoding sharpens the patch cost from `O(delta logN)` to `O(delta logN/log delta)`, so at the OPS parameters a useful transfer must have `Omega(N^beta)` globally conflicted positions.

This only constrains the union across YES inputs; it does not force many conflicts on any one input or charge AND gates. The matching source itself is now settled: cyclic least-fixed-point feedback can be unrolled in q rounds at polynomial overhead, preserving its `exp(Omega(sqrt(v)))` lower bound. With `v=A(logN)^2`, the arithmetic clears every fixed small beta if the map has sufficiently low AND-cost. The problem has concentrated into a specific interface: low one-hot code below every YES image; a high one-hot extension above every NO image; and broad global conflicts at cost below the source exponent. No such map is known. See C-275 and C-276.

## 2.49 - Hall cuts expose the cost of a shared witness

A rail map with no AND gates has only ORs of matching-edge inputs. Since any graph with one or two edges is a NO instance, each table coordinate can expose at most one polarity across all inputs. Every YES image must then contain the same low table, and the map collapses to an N-clause monotone CNF. Hall's theorem gives a concrete obstruction: each clause that accepts all perfect matchings can reject only at most `2^(v/2-1)` of the vertex-cover graphs with `v/4-1` cover vertices, but there are `2^(H_2(1/4)v-o(v))` such graphs. The required clause count is `2^(0.311...v-o(v))`, which exceeds N at the logarithmic-square matching scale.

This route-kill applies only to zero-AND maps. It says that any useful witness encoding must use positive AND-cost to make low completions depend on the source input, while keeping rail pairs consistent on every NO input. Combined with C-275, those witness-dependent conflicts must span more than `c_beta s2` coordinates globally. Exact cost and high NO completions remain the missing bridge; actual q is still `N-o(N)`. See C-277.


## 2.50 - The NO side must carry varying decoy information

C-278 formalizes a route filter for fixed-scaffold witness maps. If every NO input maps to one fixed partial vector P, and the map's input-dependent additions vanish on NO, then ORing all added rails detects the source exactly: NO inputs add nothing, while every YES low code must contribute a rail outside P because P has no low completion. This extraction costs no AND gates beyond the map's a. Consequently `a>=CycAnd(f)`, leaving no transfer margin. The fact that every YES has a succinct witness code is insufficient by itself.

The surviving map must make its NO partial table vary with the source input. That variation must be monotone, remain below some high completion, and avoid every low completion; on YES inputs the map must additionally contain one whole low code and create the broad conflict support required by C-275. These coupled conditions identify the real asymmetric encoding problem. They do not establish an impossibility theorem for variable NO images; actual q remains `N-o(N)`. See C-278.

## 2.51 - LowExt maps need a hard-to-decode NO profile, not merely variable codes

C-279 gives an explicit variable-NO map for a two-block matching threshold. A NO input below the boundary emits no rails; a boundary NO input emits one high code selected by the split rank. A YES input activates two neighboring rank predicates, and their disjoint address-class codes jointly contain the low all-zero table. Balanced random classes can all be chosen high by counting at `m=Theta(log^2 N)`.

The exact cost audit kills the hoped-for transfer: each rank predicate is visible on a designated output coordinate, and the source is the OR of adjacent rank-predicate intersections. Thus `CycAnd(F)<=a_map+O(m)`, so this map spends all but O(logÃ‚Â²N) of the source hardness. The structural upgrade is that the open problem is not simply to make NO images vary. Their compatibility/activation profile must avoid a cheap global decoder. This is the same object Route B must charge against the equality-fingerprint cover. No q improvement; `q=N-o(N)`. See C-279.
## 2.52 - Native closure as a cylinder grammar; ownership carries description identity

The primary phase is now native cyclic sharing/readout. C-260's minimal supports form a grammar over partial assignments: OR chooses proof alternatives, compatible join combines two sides, and a conflict is bottom. Cutting a proof at a reused state yields a context and replacement. Every compatible cross-combination is accepted, so its full completion cylinder must lie in SIZE(s2).

For context K matching low table w and replacement P matching low table w', the owner mask `Var(P)\\Var(K)` defines a canonical completion that takes P's table only on P-exclusive coordinates and w elsewhere. This mask is a concrete carrier of global circuit-description synchronization. The safe-mask image is capped by the number of size-s2 tables, but no theorem connects that cap to q. Counts, certificate width, and reused-anchor collisions fail against parity lock and the repeated-block equality cover. The next target is a q-sensitive product-rank theorem for compatible owner masks across the full low-circuit class; in parallel, seek an N^(1+o(1)) native cover that kills the route. Actual q lower bound remains q >= N-o(N). Full analysis: research/C281_NATIVE_CYLINDER_GRAMMAR_AND_OWNER_MASK_FRONTIER_2026-09-27.md.

### Algebraic reading of the native closure

For a certificate family, use antichain addition `A+B=Min(A union B)` and multiplication `A*B=Min({a union b: a in A,b in B, a union b consistent})`. The empty family is zero and the singleton empty support is one. Every fusion pair is one multiplication of two sums; a q-pair closure is therefore a q-multiplication cyclic circuit over this compatible-support semiring. This records the exact resource directly, with least-fixed-point semantics for cycles. It suggests algebraic support/factorization lower bounds, but ordinary monotone arithmetic or decomposable-circuit bounds transfer only after an overlap-preserving reduction. See C-281.

## 2.53 - Bottom-NO collision attempt and its hole correction

C-282 proposed a source separator from rail collisions by fixing a high completion above the bottom NO image. Its proof incorrectly treated that partial image as if it pinned the high table on every coordinate. If the bottom image leaves blank a coordinate where a YES low witness differs from the chosen high completion, no collision follows. The one-bit map `phi(0)=empty`, `phi(1)=e(w)` demonstrates the missing implication.

The exact repair exposes the bypass family. Let `P=phi(0)` have d holes and let `K(P)={w in SIZE(s1):P<=e(w)}`. Collisions on pinned coordinates plus code tests on only the d holes give `CycAnd(f)<=a+(N-d)+K max(d-1,0)`. More strongly, if K is nonempty, any low `w in K` and the high completion of P differ only on the holes; sparse-support interpolation forces `d=Omega_beta(s2)` in the OPS gap. This matches the scale of C-275's global conflict support. It is not sufficient: C-279 has P empty and K equal to the whole low class, yet its rank states expose a short source decoder. Route A remains open; actual q remains `N-o(N)`. The next useful question is whether a low-cost map can exploit the compatible low codes without making a short source decoder. Full correction: `research/C283_BOTTOM_BASELINE_HOLES_COUNTEREXAMPLE_AND_REPAIR_2026-09-27.md`.

## 2.54 - Matching source size can be polynomial in the table length

C-284 removes a false parameter restriction in the matching-to-LowExt route. With side size `v=N^delta` and `0<delta<min(beta,1-beta)`, a perfect-matching witness table represented as a sparse edge-indicator has size `O(v logN/logv)=O(v/delta)<=s1`. The cyclic source lower bound is `exp(Omega(N^(delta/2)))`, which beats every polynomial map AND-cost. At the same time, counting supplies `N^delta` balanced address classes whose indicator tables all lie outside `SIZE(s2)`, because their choice entropy is `Theta(N^(1-delta)logN)` while the high threshold class has description entropy `O(N^beta logN)`.

Thus the source need not be only polylogarithmic: a polynomial source dimension works for every fixed beta after choosing delta below both beta and 1-beta. The missing piece remains a monotone low-AND map satisfying the full YES/NO orders without a short source decoder. Scaling C-279's rank palette does not help; its adjacent-rank decoder still spends nearly all source hardness. This is parameter progress only; actual q remains `N-o(N)`. Full derivation: `research/C284_POLYNOMIAL_DIMENSION_MATCHING_TRANSFER_WINDOW_2026-09-28.md`.

## 2.55 Projection overlap and the missing nonlinear coherence charge

C-285 tests expander-overlapping local views. If each view is a restriction of the same N-bit table to S_v, compatible view assignments glue uniquely to a word on the coordinate union. For each table coordinate, all equalities between its occurrences are generated by a spanning tree; extra expander edges are redundant. Therefore edge expansion alone does not create more independent splice choices or synchronization relations. A safe compatible-support cylinder is still limited to `log2 |SIZE(s2)|` free coordinates.

This narrows the global-synchronization target. A winning family must link views through different Boolean transformations, not just repeated raw coordinates. Native support compatibility only checks signed-literal agreement; parity or gate-consistency conditions need explicit derivations. The key missing statement is a rule-cost lower bound for enforcing many independent nonlinear relations while reusing arbitrary endpoints. C-258's equality-fingerprint cover remains the required hostile countercheck. C-285 is a route-kill for projection-only expander constructions, not progress on actual q, which remains `N-o(N)`.

## 2.56 - Shared-DAG approximation is directional

Rao's spread construction does not give full equality approximation on both distributions. Its useful guarantees are one-sided: on YES, `Phi<=tilde(Phi)` except with probability `a*2^-t`; on NO, `tilde(Phi)<=Phi` except with probability `a*4^t*epsilon`. For a multi-output DAG, one approximant per shared node and propagation through free OR gates charges only distinct AND nodes, with no factor for the number of table rails. This is the correct approximation language for LowExt: it preserves witness rails on YES and prevents false rails on NO.

If a rail fires on a `p`-fraction of matching YES inputs, its selected term law is `pR`-spread. For perfect matching on `v` vertices and the `G(W)` no-large-matching distribution, `R=v/4`, so `theta_M=64 alpha_M(t+log2(1/xi))/v`. A low YES witness is within `N(theta_M+delta1)` of a canonical table. C-275 interpolation turns that into a full contradiction if `s1+A*r*n/log2(r+1)+B*n<=s2` and the NO error/union conditions hold. This completes the logic past polarity concentration.

## 2.57 - Source amplification filters matching, while clique transfer remains open

For matching, `theta_M=Theta(v^-1/2)+O(logN/v)`, so a polylog source forces `Ntheta_M=N/polylogN`, outside the `N^beta` patch radius. Direct matching-indicator witness codes also require `v<=N^beta` up to constants, while patchability requires `v>=Omega_beta(N^(2*(1-beta))`. Retire this matching route for small beta unless a different witness family changes the code-size relationship.

Rao's clique spread distributions give `theta_C=Theta(log^3N/N^2)` at `m=N^2`, `ell=Theta(log^2m)`, and valid disjoint-gap choice `k=2ell`. The canonical-table argument excludes C-125 maps up to `A_map=L0/4`. It does not close the transfer: cyclic unrolling gives `CycAnd>=sqrt(L0/C)`, a lower bound, not the upper bound needed to compare against `A_map`. Color coding gives an upper `exp(O(k))*poly(m)`, which is above the map floor at these parameters. A useful map might still occupy `A_map<a<CycAnd`; neither its existence nor impossibility is known. See C-290.
## 2.58 - CohEnc is the missing reconstruction measure

Define `CohEnc_{s1,s2}(f)` as the minimum AND cost of a monotone dual-rail map whose YES images contain a low one-hot table and whose NO images lie below a high one-hot table. Composition gives the exact inequality `rho_GapMCSP>=CycAnd(f)-CohEnc(f)`. This separates the needed quantity from ordinary decision cost.

ODDFACTOR demonstrates a known gap between a linear GF(2) span program and `m^(Omega(logm))` monotone circuit complexity. The span witness is a sparse odd-degree edge set, but direct solution-use rails vanish on NO; ORing them computes ODDFACTOR and consumes the decision lower bound. Direct availability also lets the zero table complete NO images. Thus `SpanRec<<decision` is not yet `CohEnc<<CycAnd`. The native grammar of C-281 is a compatible-support semiring, with no additive inverses; no translation to GF(2) has been found. A viable construction needs a monotone two-sided primal/dual table code or a theorem that any such code can be compiled back to source decision at comparable AND cost.

## 2.80 - C-230/C-244 crosswalk: safe-cylinder volume is not low-set mass

For the active promise `Y=SIZE(s1)`, `Z={CC>s2}`, a monotone dual-rail proof term is a consistent partial assignment P. If it fires on a low table, it fires on every completion of P; soundness therefore forces `[P]` to contain no high table, so `[P] subseteq SIZE(s2)`. Medium tables are allowed. Conversely these high-free cylinders, if they cover Y, define a valid promise separator. This is the correct promise analogue of exact low-set implicants and avoids the full-domain/promise confusion.

The term expansion of a monotone promise separator gives gap-safe cylinders, but C-244's proof/context zones already capture the stronger native structure. C-230 already proves that the largest safe cylinder has `Theta_beta(N^beta logN)` free coordinates by Lupanov synthesis and counting. The elementary comparison `log|SIZE(s1)|=O_beta(N^beta)` shows that such a cylinder can exceed the entire low class, with excess points in the medium band. This is a crosswalk, not a new theorem. The active unresolved object remains the q-sensitive low-mass/readout bound in O-153/O-244 or a near-linear cover in O-168. C-257 parity, C-258 equality, and C-281 owner-mask hybrids remain compulsory tests. Actual `q=N-o(N)`; no lower-bound change.

The raw cylinder-volume lower bound is dead for the active promise, as follows from C-230 plus circuit counting. The next invariant must track low-set mass, cylinder positions, and compatibility across a shared grammar. Do not treat C-289's repackaging as progress beyond C-230/C-244.

## 2.81 - C-290: transfer inequalities must be compared in the correct direction

The Rao-clique line supplies a sound map-cost obstruction: with disjoint parameters `k=2ell`, every C-125 map costs above `A_map=L0/4`. But cyclic unrolling says `CycAnd >= sqrt(L0/C)`. A lower bound below `A_map` does not upper-bound `CycAnd` and cannot close `rho >= CycAnd-a`. A monotone color-coding circuit gives `CycAnd <= exp(O(k))*poly(m)`, which is above the obstruction floor at the chosen constants. The exact possible window is `A_map<a<CycAnd`; both its existence and a map in it remain unproved. Learning: always align the direction of lower/upper inequalities before retiring a transfer route. Actual `q=N-o(N)`.

## 2.83 - ODDFACTOR source strength rises; explicit dual sidecars erase it (C-291)

Cavalar et al.'s matching-sunflower theorem improves the monotone decision lower bound for bipartite matching to `2^(v^(1/3-o(1)))` and transfers an exponential lower bound to ODDFACTOR, while ODDFACTOR has a linear GF(2) span program. Native cyclic unrolling preserves `CycAnd(ODDFACTOR_v)=2^(v^Omega(1))`. With `v=(log N)^K` for sufficiently large fixed K, this exceeds every polynomial in N; odd-factor witnesses supported on at most `2v` edges still have `polylog(N)` table circuits, fitting `s1` for every fixed beta. This is a strong source window, not a LowExt transfer.

The attempted shortcut of adding explicit dual-witness variables has a structural leak. If YES carries the all-ones auxiliary dual-rail vector and NO carries a consistent one-hot vector, a monotone AND of every auxiliary rail separates those promise sides in linear size, independent of the graph. Hashing a dual witness into a high table cannot restore the lost source hardness. The unresolved principle is: coherent reconstruction needs NO decoys that are hard to recognize as source-side information, while the map must still produce them monotonically from the hard input. Actual `q=N-o(N)`; no C-125 map or P-vs-NP proof.

### C-292 - Opposite-rail certificates must union to YES graphs

For ODDFACTOR, a graph edge set lies in some odd-cut NO input exactly when it has an odd-order component. So at any table coordinate, every positive certificate for rail 0 combined with every positive certificate for rail 1 must cover all vertices in even components: their union must be an ODDFACTOR-YES graph, hence contain an odd-factor subgraph. This is the precise monotone form of the missing span-program step. GF(2) linear reconstruction returns a sparse support, but a C-125 YES image is a total one-hot table. Edge-availability rails expose selected support positions and leave omitted positions blank; the existential span witness cannot fill those zero rails after the map is evaluated.

With no AND gates, certificates are empty or one edge, so opposite rails cannot both be available. Each coordinate then has fixed polarity; the common low code gives an `N-1` AND separator, contradicting ODDFACTOR's C-291 lower bound at `v=(log N)^K`. This is the familiar OR-only floor, not a useful positive-AND bound. The next target is a shared-DAG cost theorem for generating the paired odd-factor certificate families across all coordinates, together with a high completion on every NO. No `CohEnc` separation or q improvement follows. See C-292.

### C-293 - Certificate width gives a positive-AND reconstruction floor

A fan-in-two monotone circuit with `a` paid AND gates has a positive certificate of width at most `a+1` for every nonzero rail: trace a true proof, choose one predecessor at each OR, retain both at each AND, contract OR paths, and use connected-graph edge counting. C-292 says opposite-polarity certificates at one ODDFACTOR coordinate must union to an ODDFACTOR-YES graph, which contains an odd-factor subgraph of at least `v` edges. Thus any coordinate supporting both rail functions forces `a>=ceil(v/2)-1`. If every coordinate has a fixed polarity, the map contains one common low code on all YES inputs, and its `N`-rail conjunction separates the source with `a+N-1` AND gates. C-291 excludes that case below the same threshold for `v=(log N)^K`, K large. This proves `CohEnc>=ceil(v/2)-1`, but only a polylogarithmic floor at the useful source setting. To reach a transfer, we need the number/diversity of certificate pairs, not just their individual width. The actual q bound is unchanged.

The reusable statement is source-agnostic. If `W(f)` is the minimum width of a positive certificate and `L=CycAnd(f)`, then `CohEnc(f)>=min(ceil(W(f)/2)-1,L-N+1)`: varying one rail polarity requires two short certificates whose union is a positive certificate; keeping fixed polarities gives a direct separator with cost `a+N-1`. For ODDFACTOR, `W=v`; source hardness makes the certificate-width term the active floor.

## C-294: high-code consensus over odd-cut NO extensions

A possible way to obtain varying NO decoys is to label every odd-cut NO extension with a high table and pin, at a given input, only bits shared by all odd-cut NO extensions above it. This is automatically monotone: adding source edges shrinks the extension family, so consensus can only increase. For ODDFACTOR, odd-cut NO graphs correspond to odd cuts. An affine label on an odd cut is a linear form on the component-selection bits; it is unanimous exactly when its coefficient vector is 0 or the odd-component parity vector p. This turns monotonicity and high completion into a clean algebraic interface.

The first natural affine family fails quantitatively. For every balanced-subset coordinate, one consensus polarity restricts to ODDFACTOR on a large balanced block, so the cut-consensus map retains superpolynomial AND complexity. This does not rule out a cheaper submap: C-125 requires only one low-code rail per bit on YES, not every unanimous rail. It also does not rule out nonlinear cut labels. The live question is whether one can omit hard consensus pins while still covering all YES inputs and varying NO labels enough to avoid a fixed-scaffold decoder. See research/C294_ODD_CUT_CONSENSUS_AFFINE_RAIL_OBSTRUCTION_2026-09-28.md.

## C-295 - Coherent affine consensus and the two-conflict decoder

A useful refinement of C-294 is to reuse one balanced cut subset A at every truth-table coordinate. Then all odd-cut labels collapse to two complementary high tables R and complement(R), which can be made simultaneously high by counting. The consensus NO image is necessarily below one of those codes or zero.

This turns the submap question into a compact decoder theorem. On YES, any covered low code differs from each high code, so the image conflicts with both. On NO, a submap is compatible with at least one of the two. OR the conflicts against each code and AND them: one extra AND computes ODDFACTOR. Therefore no pointwise submap can be cheap in AND count at the chosen polylogarithmic source scale. The lesson is that code-family size alone is not the key parameter; it is the AND complexity of testing conflict with the whole NO envelope. Two complementary labels are maximally easy to decode and therefore force hardness back into the encoder.

Scope: this rules out only submaps of the coherent two-code affine consensus construction. It does not cover coordinate-dependent affine labels, arbitrary C-125 maps, or nonlinear label families. The active fusion lower bound remains q=N-o(N). See research/C295_TWO_CODE_AFFINE_CONSENSUS_SUBMAP_DECODER_2026-09-28.md.

Generalization: for a fixed high-code envelope H of size k, compute one conflict OR per code and AND the k outputs. This gives a source decoder using the encoder plus k-1 AND gates. The structural quantity to study is not just the number of decoys; it is the AND complexity of testing conflict with the whole envelope. If the source has monotone AND-count A(f), the map cost g satisfies g >= A(f)-k+1; only k <= A(f)/2 guarantees g >= A(f)/2. Larger families may still have a simpler structured conflict test.

## C-296 - High NO labels are not enough when the YES code is fixed

The odd-cut blocker construction gives a clean way to build a valid monotone map. Choose sets U_j of odd cuts; label a cut T by the incidence vector z_T(j)=1[T in U_j]. At coordinate j, turn on the zero rail exactly when every cut in U_j has a crossing edge. YES graphs cross every odd cut, so the fixed zero table is present. On NO, an odd component yields a compatible cut T; the output can only pin zeros where z_T also has zero, so z_T is a high completion. Random incidence matrices make all cut labels high by a direct union bound.

The construction fails for a fundamental reason: every YES input contains the same low code, while no NO image contains that code. Their N-rail conjunction is an ODDFACTOR circuit, independent of how complicated the NO-label family is. Thus decoy diversity must be paired with low-code diversity. Raw witness rails are also unsafe because ORing them may recover the source. The live interface is a shared monotone map whose low code varies across YES inputs and whose NO-side decoys mask every short witness decoder. See C-296 and O-173.

## C-297 - Two-sided code-envelope pressure

Every C-125 encoder carries two finite semantic families: low codes that witness YES coverage and high codes that bound NO images. Either family can be used to decode the source. For k high labels, test conflict with each and AND the tests, costing k-1 extra AND gates. For r low witnesses, test containment of each complete code and OR the tests, costing r(N-1) AND gates. A NO image cannot contain a low code because it is below a high complete code. Therefore g >= A(f)-min(k-1,r(N-1)). The implication is useful as a route screen: both families must be large enough to defeat their simple decoders, and then their shared structure must still be hard to read. It does not bound the full SIZE(s1) and high-table universes. See C-297 and O-173.

## C-298 - Subgraph-lifted consensus creates matching lower cones

A rail can be active when some subgraph H of the current graph has a nonempty compatible odd-cut family and all its cuts agree on the bit. This is monotone; on a NO input G, every compatible cut of G is also compatible with H, so the rail agrees with every high completion label for G. The exact form is OR over candidate cuts T of AND over opposite-label cuts T' of "G has an edge crossing T' but not T." This repairs the empty-family/vacuity problem of ordinary consensus, though its direct AND cost can be huge.

On a perfect matching M, the rail is active precisely when some candidate cut T has no opposite-labelled cut whose matching-boundary set is contained in B_M(T). Thus YES coverage requires a monochromatic lower cone in the odd-subset poset of matched edges at every coordinate. For affine labels c+|T intersect A| mod 2, toggling a matched pair across A preserves the boundary and flips the bit, eliminating both rails. Requiring coverage on every perfect matching forces A empty or all vertices, so every cut receives one fixed code R. The lift then outputs e(R) everywhere; if R is high it has no low YES completion, and adding witness-only rails makes their conflict OR compute ODDFACTOR. The affine version is retired, while nonlinear labels remain open under O-174. No CohEnc separation or q improvement follows. See C-298.

### O-175 - Global polarity conjecture for matching fibers

For a fixed coordinate label z on odd cuts, C-298 reduces lifted-rail availability on a perfect matching M to a monochromatic fiber of cuts crossing exactly one edge e in M. The fiber's color is fixed by the singleton cut at e's left endpoint. An exact toy enumeration over every Boolean labeling at v=2 and v=3 found: whenever every matching has at least one mono fiber, some one polarity has a mono fiber for every matching. This suggests that any complete lifted low code may be fixed across all perfect matchings, which would trigger the finite-low-envelope decoder. The check is only a conjecture source; prove or refute globally and then account for the actual rail circuit cost. See O-175.

## C-299 - Mono-fiber polarity propagates across all perfect matchings

The C-298 nonlinear lift has an exact matching test: a coordinate rail is active on M iff some edge e in M has a monochromatic fiber of odd cuts crossing exactly e. If M,M' form one alternating cycle, every fiber of M intersects every fiber of M'; choose the odd vertex interval between the two designated edges. A monochromatic polarity on M therefore fixes every monochromatic fiber on M'. For even v>=6, matchings are connected by relative v-cycles (these generate S_v), so each coordinate has exactly one available polarity across all perfect matchings.

A LowExt map must then output one fixed complete table b on every perfect matching, and its YES order condition makes b low. Its rail conjunction accepts all perfect matchings and rejects every odd-cut NO graph below a high code. This is enough to invoke Cavalar et al.'s matching lower bound: their proof requires correctness only on the perfect-matching/odd-cut distribution support, where Match and Odd agree. The resulting AND cost is superpolynomial for even v=(log N)^K, K>3. No claim is made that every odd-factor YES graph contains a perfect matching; the decoder is used only as a distributional separator. This closes the pure lifted-consensus map for arbitrary nonlinear labels, not a general C-125 map with separate witness rails. C-300's attempted sidecar extension is withdrawn for a distribution mismatch; C-301 later rules out every polynomial-cost C-125 map at the selected polylog scale. See C-299â€“C-301.

## C-300 - Rao/odd-cut distribution mismatch (withdrawn route-kill)

The attempted spread-to-expansion chain is not instantiated: C-286's Rao approximation error is for Rao's `G(W)` NO distribution, but a sidecar assumed to vanish on Cavalar odd-cut NO inputs need not vanish on `G(W)`. The expansion/deletion calculation remains a conditional combinatorial lemma. Learning: a source-side support condition cannot be moved across distributions without a coupling or explicit transfer. C-301 later handles all polynomial-cost C-125 maps by using Cavalar's approximation directly on its own matching/odd-cut pair.

## C-301 - Compatible odd-cut mass forces polarity for every C-125 ODDFACTOR map

Apply Cavalar et al.'s gatewise matching approximation to the shared monotone DAG; its local errors are charged once per node, so reuse across `2N` roots incurs no output multiplier. Fix `w=floor(v^(1/3)/log v)`. The matching-DNF smallness satisfies `r=O(w^3 log^2v)=O(v/logv)=o(v)`. If both rails at one coordinate contain terms A and B of width at most w, their union has at most `2w` edges, so its graph on `2v` vertices has an isolated vertex. At least a `2^(-2w)` fraction of odd-cut colorings are constant on the union's components, making both terms true. The shared-DAG odd-cut over-approximation error is `o(2^(-2w))`, so one-hot NO soundness excludes the pair.

Each coordinate consequently has one rail polarity. The YES directional guarantee (the approximant is above the exact map on D1 except with probability `o(1)`) forces every low witness on a good perfect matching to be the same table b. Conjoining the original b-rails yields a separator accepting `1-o(1)` of perfect matchings and zero odd-cut NO inputs. Applying the same approximation to this separator contradicts the DNF agreement cap unless its size exceeds `2^floor(v^(1/3)/logv)`. Thus `a+N+v^2+1 >= Omega(2^(v^(1/3)/(2logv)))`.

For `v=(logN)^K`, K>3, this rules out every polynomial-cost C-125 ODDFACTOR map, including NO-active maps. It does not yield a positive reconstruction/decision transfer or a P-vs-NP result. Learning: the paired-term obstruction works at a fixed quantitative width safely inside the approximation theorem's regime; do not extrapolate its asymptotic `2^-omega(w)` error to the boundary of the circuit lower bound. Full details are in `research/C301_SHORT_TERM_OVERLAP_FORCES_GLOBAL_POLARITY_2026-09-28.md`.

### Checkpoint after C-298â€“C-301

- **Actual `q=N-o(N)` bound changed?** No.
- **Cheap C-125 encoder for ODDFACTOR constructed?** No. Conversely, all polynomial-cost encoders at the polylog source scale are ruled out.
- **A global structural result obtained?** Yes: paired short opposite-polarity terms have a large compatible odd-cut NO family, forcing one global rail polarity under Cavalar's odd-cut approximation error budget.
- **Decision/reconstruction gap established?** No positive gap. The encoder lower bound is on the same stretched-exponential scale as the known cyclic-decision lower bound.
- **Near-linear full-promise cover or P-vs-NP proof?** No.

The ODDFACTOR-as-polynomial-encoder route is now closed. Further work should compare the exact `CohEnc` lower bound with the true cyclic upper/lower bounds or select a different monotone source whose witness reconstruction can plausibly be cheaper than decision.

## C-302 - Raw owner-mask rank does not charge native states

An owner mask is one of `N` Boolean address-vectors, so its `GF(2)` rank is at most N. Raw vector rank cannot by itself prove the target `q>N^(1+epsilon)`. The parity-lock calibration is stronger: its safe canonical hybrids include every even table, whose affine span has dimension `N-1`, while an explicit `4N-4`-pair native cover handles the promise. Thus even nearly full affine dimension of safe hybrids is compatible with linear q in an artificial promise.

This retires raw mask rank and hybrid affine dimension as standalone invariants, not an algebraic proof using actual `SIZE(s1)` structure. A useful replacement must charge how a small native grammar selects/synchronizes owner masks across low-circuit descriptions. The separate full-promise near-linear-cover attack remains the counter-program. The actual bound is still `q=N-o(N)`; no superlinear Gap-MCSP bound or P-vs-NP proof follows. Full audit: `research/C302_RAW_OWNER_MASK_RANK_CEILING_2026-09-28.md`.

## C-303 - Promise separation does not yield an SoS refutation

The native separator labels only the low and high sides of the MCSP gap. Medium tables are unconstrained, so evaluating it to zero on a high table does not certify that the table has no size-`s2` circuit. The separator trace has no automatic conversion to a Positivstellensatz identity. The cited Austrin--Risse degree bound is also below the current `q=N-o(N)` floor for fixed `beta<1`; their stronger size theorem needs an errorless heuristic-circuit assumption. A revival needs a sound completion of the medium band and a stronger degree window. This is an interface obstruction, not evidence that SoS cannot help. Actual q is unchanged; O-168 global description coherence and the full-promise cover remain active. See `research/C303_GAP_SEPARATOR_TO_SOS_BRIDGE_AUDIT_2026-09-28.md`.

## C-304 - Compatible-support grammar as an ideal-valued algebra

Write a support as a consistent partial truth-table assignment and identify each proof family with its upward closure under adding literals. Over a field K, the algebra with basis `m_S` for consistent supports and product `m_S m_T=m_(S union T)` when compatible (zero on conflict) has dimension `3^N`. The upward-closed family U maps faithfully to the monomial ideal `I(U)=span{m_S:S in U}`. Alternative proof becomes ideal sum; compatible proof composition becomes ideal product. Thus C-281 has an exact algebraic semantics, and a table w is accepted iff `m_ell(w)` belongs to the output ideal.

This is not a conventional span program: the tested monomial depends on every input coordinate, and the ambient algebra is exponential-dimensional. A scalar field valuation is impossible because idempotent alternative `x+x=x` forces every homomorphism into a cancellative additive group to vanish. The parity calibration also kills top-degree rank as a generic q measure. A useful algebraic advance now requires a compressed ideal or tensor representation tied to low-circuit description selection; it must pass C-257/C-258. See C-304 and `research/C304_IDEMPOTENT_SUPPORT_ALGEBRA_AND_SPAN_PROGRAM_BRIDGE_2026-09-28.md`. Actual q remains `N-o(N)`.

## C-305 - Interpret native closure as an AND-OR strategy game

In the exact recurrence, an active state is a position: the universal player selects left or right, then the existential player supplies a matching table literal or an active predecessor. Activation rank gives a bounded reachability objective and a positional witness strategy. This suggests encoding circuit-description choices as strategy choices, with universal branches challenging all N truth-table addresses.

The direct evaluator state is `(gate,address)`, so it costs `Theta(Ns1)=N^(1+beta-o(1))`, not `N^(1+o(1))`. If gate states are shared over addresses, the seed clause cannot remember which table bit is being checked; if gate states are copied per address, gate choices can vary across addresses. C-281 supports can carry address context, but their cross-splices must all remain low. The exact missing mechanism is a compact address-carrying context language whose shared gate choices stay globally coherent under every compatible splice. C-257/C-258 show that address/state products or high reuse do not alone imply large q. See C-305; actual q remains `N-o(N)`.

## C-306 - Support provenance is not control state

A support can record which matching literals a proof used, but activation passes only a Boolean state bit forward. At one fixed table w, all matching contexts and proofs lie inside `ell(w)`, so every cross-pair is compatible. Thus support annotations cannot enforce that a shared state uses one proof choice for one address context and another choice for a different context. The C-305 address-register proposal is retired in that form.

A compact evaluator must place its global circuit-description choice in the fixed state-level activation pattern, or use another semantic quotient. This is stronger than saying the explicit product is too large: supports cannot repair its lost address register. It remains a scoped no-go, not a general q lower bound. Preserve C-257/C-258; actual q remains `N-o(N)`. See C-306.
## C-307 - Native algebraic complexity must respect compatibility filtering

For a dense high set, an acyclic monotone separator with a binary AND gates and free OR structure compiles into a fusion cover with at most a pairs: each AND gate intersects the high-side carriers of its two inputs, and the low table's matching literal slices or earlier carriers put both endpoints in the closure. Combined with the known q-to-acyclic unrolling, this gives
\[
\sqrt{A_{\cap}(Y,Z)}\le \rho_{\mathrm{prom}}(Y,Z)\le A_{\cap}(Y,Z),
\]
where A_cap counts AND gates with ORs free. This sharpens one transfer direction, but it does not improve the target exponent: a separator lower bound above N^(2+2epsilon) would still be needed to force q>N^(1+epsilon).

Code distance and ordinary monotone arithmetic hardness do not automatically lower-bound the native grammar. Arithmetic multiplication preserves all positive cross-products; native multiplication deletes conflicting products and collapses duplicate supports. That conflict filter is a computational resource. Separately, bounded-width constraint families have signed monotone CNFs, so O(N) local forbidden patterns yield O(N) covers even when the YES family is large. New algebraic attacks must bound compatible-product complexity or global selector synchronization, not only code distance, rank, or arithmetic circuit size. They must still pass parity and repeated-equality calibrations. Actual q lower bound remains q >= N-o(N); no OPS transfer or P-vs-NP proof follows. See C-307.


**Expander-code calibration (C-307):** an asymptotically good binary LDPC code has positive rate, positive distance, and O(N) constant-weight parity checks. Its membership separator compiles to O(N) fusion rules. Because the promise NO set is the code complement, every sound output support must be a full codeword; thus one linear grammar can generate exponentially many isolated full certificates. Count and distance are therefore insufficient. This family is a promise calibration, not an embedding into SIZE(s1).


**OPS local-clause screen (C-307):** in a monotone CNF separator, each clause's falsifying pattern must fix more than about s1/n coordinates, because every smaller partial truth table has a SIZE(s1) completion. A uniform random table is high with probability 1-o(1), so covering the high side requires at least 2^(Omega(s1/n)) clauses. This kills direct forbidden-pattern enumeration as a near-linear OPS construction. It does not apply to circuits with shared AND gates or cyclic q-state closure, where one shared subcircuit can stand for many clauses.

## C-308 - Paid conjunctions are the right cost parameter for the matching approximation

Cavalar et al.'s matching-sunflower proof can be adapted to charge only binary AND nodes in a shared monotone DAG. Free OR structure forms unions of matching-DNF term families; each paid AND takes their compatible cross-product and one plucking/truncation step. The finite universe of matching terms of width at most `2w` bounds the pluck work by `v^(O(w))` even when an OR has enormous fan-in. Choosing the sunflower error small enough makes the D0 error per AND node at most `v^(-4w)`. OR roots use exact unions and AND roots reuse their counted approximation, so a union bound over paid nodes controls all output roots simultaneously.

For ODDFACTOR, opposite-polarity short rail terms force at least `2^(-2w)` mass on odd-cut NO inputs. Under the C-308 error budget this is impossible, so each truth-table coordinate has one polarity. YES witnesses fix a common low table on almost all perfect matchings; its conjunction gives a one-sided source separator. Applying the AND-count approximation a second time proves every C-125 map has `a+N-1>2^w`, where `w=v^(1/3)/(log v)^(2/3+gamma)` for any fixed `gamma>0`. This is stronger than C-301's bounded-fan-in conversion.

**Model implication:** C-308 closes a resource-accounting gap for the ODDFACTOR reconstruction lower bound, not the actual fusion exponent. It does not build an encoder or show its cost below exact cyclic decision. The next source-selection test is a strict separation between exact monotone decision and one-sided distributional decision that can be upgraded to an all-input C-125 map. OPS remains at `rho=N-o(N)`; no P-vs-NP proof has emerged. Full derivation: `research/C308_AND_COUNT_MATCHING_APPROXIMATION_AND_COHENC_2026-09-28.md`.

## C-310 - Short-term NO mass bypasses the o(v)-small DNF condition

Under the odd-cut coloring distribution, a fixed matching of `ell<v` edges is monochromatic edge-by-edge with probability exactly `2^(-ell)`. Hence any nonempty matching-DNF of width at most w accepts at least `2^(-w)` of D0. This gives a direct obstruction: a one-sided separator approximant whose D0 false-positive error is below that threshold must be the zero DNF.

Applying this fact to C-308's free-OR, paid-AND approximation removes the `r=o(v)` requirement. Take `w=c*v^(1/3)/(log v)^(2/3)` for small fixed c, so `q=e*r/v<=1/16` even though r is Î˜(v). The D1 truncation tail remains geometric. For a hypothetical ODDFACTOR C-125 map with `a+N-1<=16^w`, paired opposite rails force one polarity per coordinate and a common low table; its rail conjunction Q rejects every odd-cut NO and accepts almost all perfect matchings. Q's approximating DNF has D0 mass below `2^(-w)`, so it is empty, yet it must accept a positive fraction of D1. Thus `a+N-1>16^w`.

This is a sharper encoder lower bound, not a fusion lower bound. It does not construct the map needed for a transfer and leaves `rho_GapMCSP=N-o(N)`. The active question remains whether one can realize a genuine exact-decision versus witness-reconstruction gap on all source inputs. See `research/C310_ODD_CUT_TERM_MASS_TIGHTENS_COHENC_2026-09-28.md`.

## C-309 - Minimal-witness orbit coverage is the missing exactness condition

For a monotone source f invariant under a finite symmetry group G, suppose its inclusion-minimal YES inputs are one G-orbit of size L. A one-sided separator Q that accepts at least 1-eta of a uniform minimal witness can be made exact by ORing t relabeled copies, where `t=floor(log L/log(1/eta))+1`. Each minimal witness is missed with probability at most `eta^t`; the union bound gives one relabeling family covering every minimal YES input. Monotonicity extends acceptance to all YES inputs, while soundness and G-invariance preserve all NO rejections. The AND-count grows by a factor t.

This makes distributional reconstruction precise: a decoder on one transitive orbit can be exactified at cost O(log L), but an approximation distribution that sees only some minimal-witness orbits cannot certify the whole source. MATCH satisfies the one-orbit condition. ODDFACTOR does not: its minimal YES inputs include nonmatching odd forests, so C-308's matching support yields exact MATCH behavior only. The source criterion should require one-orbit coverage, a small set of all covered orbits, or upward generation of every YES input from the chosen orbit. This is a route filter, not a C-125 construction or q lower bound. See `research/C309_ORBIT_COVERAGE_AND_DISTRIBUTIONAL_DECODING_2026-09-28.md`.

## C-311 - Dual witness coding must avoid YES-side polarity saturation

A monotone span program provides a shrinking dual witness set `Y_X`: on YES it is empty, and on NO it contains a separator. Label each dual witness y by an arbitrary high-complexity truth table c(y), and put rail `(j,b)` on exactly when every y in `Y_X` has label bit b at j. This is monotone, every YES image dominates any low table by vacuity, and every NO image is dominated by the high code of any chosen dual witness. Thus a span-program representation can be translated into a formally valid C-125 map at the level of semantics.

But on every YES input both rails at every fixed coordinate are active. On NO no fixed coordinate can have both rails, because the dual family is nonempty. Hence one AND of a fixed opposite-polarity rail pair computes the source exactly. The map has `CohEnc(f)>=CycAnd(f)-1`, so this construction cannot give a useful reconstruction/decision gap even with a random codebook of high tables.

The broader saturation rule is now a mandatory audit: if any fixed coordinate has both rails active on all YES inputs, one AND gate on those rails is an exact source separator under C-125 NO soundness. A useful map must keep YES completions varying without giving away a fixed pair test. C-311 closes the universal-dual-consensus version of the ODDFACTOR/MSP route, not every primal/dual construction. The actual OPS lower bound remains `N-o(N)`.

## C-312 - Literal-guarded dual consensus has a factor-two cofactor compiler

A guarded construction can avoid C-311's global saturation: on `x_r=0`, use NO-vanishing primal rails; on `x_r=1`, add universal dual-consensus rails. It can satisfy C-125 because NO inputs in the first slice map to bottom and NO inputs in the second slice have high dual completions, while YES inputs retain low primal codes.

The source can still be decided from the two cofactors. On the zero slice, OR all output rails; on the one slice, AND a fixed opposite-polarity pair. Monotone Shannon decomposition gives `CycAnd(f)<=2a+2` for a map of AND cost a. Thus a one-input guard limits any decision/reconstruction separation to a constant factor, but does not rule out a constant-factor margin. For ODDFACTOR the primal rail family is still the cost bottleneck. Generalize only if the guard has a controlled cofactor cover; do not claim a full route-kill. Actual q remains `N-o(N)`.

**C-312 ODDFACTOR cofactor sharpening:** for any fixed graph edge e, the restriction `x_e=0` contains `ODDFACTOR_(v-4)` by padding it with a fixed disjoint pair of opposite odd stars on the four reserved vertices per side, with the endpoints of e chosen as leaves so e is unused. Thus a guarded map whose zero slice vanishes on NO must pay at least the ordinary monotone complexity of `ODDFACTOR_(v-4)` on that slice. This leaves the guarded branch hard at the source's superpolynomial scale, though it still does not prove an additive comparison to full `CycAnd(ODDFACTOR_v)`.

## C-313 - Arbitrary monotone guards are not literal cofactors

C-312's factor-two source compiler depends on a literal variable: the zero-slice decoder is recombined with the one-slice decoder using positive Shannon expansion. Replacing the literal by an arbitrary monotone guard does not preserve this step because the guard-zero region is selected by `not g`, which is unavailable to monotone composition. The aggregate signals `D=OR(all rails)`, a fixed pair `R`, and `g` can even order a yes case `(1,0,0)` below a no case `(1,0,1)` whenever the no-side decoys make D true; no monotone function of these three aggregates can distinguish them.

This is only a boundary for the aggregate decoder, not a no-go for the full rail vector. A viable guarded MSP route needs either a quantified literal-cofactor cover, a decision procedure for false-positive NO guard profiles, or genuinely global output-profile information. A cheap monotone guard alone is insufficient. Thus the live target is again O-168/O-179's global selector/reconstruction problem. The attachment's requested shared-DAG Rao and canonical-table analyses are already recorded in C-286/C-287, with later ODDFACTOR updates in C-288/C-310/C-311/C-312. Actual `q=N-o(N)`.

## C-314 - Prefix-block safe envelope (candidate only)

Every low table can be viewed as k=Theta(log N) prefix-block restrictions, each of circuit size at most s1. Conversely, any table whose k block restrictions each have size at most s1 can be synthesized using k separate circuits plus a prefix selector, costing `k*s1+O(k loglogN)<=s2` for a sufficiently small constant in k. Thus `SIZE(s1) subseteq A_k(s1) subseteq SIZE(s2)`. A high table must have at least one block restriction above s1.

This creates a compositional safe envelope that may help the native cover route. It does not identify the hard block inside the C-75 closure: testing its circuit complexity is exactly the selector/address problem, and the explicit gate-address evaluator still costs Theta(N*s1). See `research/C314_PREFIX_BLOCK_SAFE_ENVELOPE_AND_SELECTOR_BOTTLENECK_2026-09-28.md`.

## C-315 - Prefix decomposition is a local constant-gap problem plus a coherence problem

For k=Theta(log N) blocks, any local separator between block functions of size at most s1 and those above t0â‰ˆs2/k composes by AND into a valid global separator. The local ratio t0/s1 is only a constant; the construction uses k copies, and C-307 then compiles the acyclic monotone circuit to a native cover. This is a conditional upper reduction, not a cover because the local separator is itself unknown.

Counting sharpens the envelope calibration: for every fixed 0<beta<1 there are globally high tables whose every block has circuit complexity in `(B*s1,A*s1]` for fixed constants B>1 and A>B. Build many functions on a fixed subcube of each block, discard the size-`B*s1` functions, and compare the product-family count to the count of size-`s2` global circuits. Therefore no high table must contain a block with a superconstant-factor gap over s1. The model's live hinge is a native direct-sum/coherence theorem for these disjoint local gap instances, or a shared block selector cheaper than k independent copies. Block counting alone supplies no q charge; keep C-257 parity, C-258 equality, and C-281 compatible-splice checks. Actual `rho=N-o(N)`. Full proof and limits: `research/C315_PREFIX_BLOCK_CONSTANT_GAP_AND_DISTRIBUTED_HARDNESS_2026-09-28.md`.

## C-316 - Exact algebraic fingerprints retain essentially all addresses

For the pointwise algebra `F_2^N`, the N coordinate indicators are orthogonal idempotents. Any family of unital algebra homomorphisms that detects every table difference is injective and must have total target dimension at least N; scalar homomorphisms are exactly address evaluations. Separately, if a linear sketch is used only by equality against a low witness, its kernel must lie inside `SIZE(s2)` because the zero table is low, forcing sketch rank at least `N-O(s2 log(s2+n))=N-o(N)`. Explicitly evaluating a size-s1 circuit at those coordinates costs `O(N*s1)`.

This retires only exact-difference multiplicative fingerprints, linear equality sketches, and their explicit gate-by-address evaluator. The claims do not constrain nonlinear promise-specific selectors or arbitrary fusion covers. The current target remains C-315/Q177's blockwise coherence problem; actual `rho=N-o(N)`. Details: `research/C316_ALGEBRAIC_FINGERPRINT_ROUTE_FILTER_2026-09-28.md`.

## C-317 - Blockwise safe cylinders saturate the splice-entropy ceiling

For k=Theta(log N) prefix blocks, choose in every block a fixed u-dimensional suffix-address subcube with `2^u=Theta((s2/k) log(s2/k))` free truth-table entries. Each completion is computed by one local Lupanov circuit per block plus a prefix selector, with total size at most s2. Thus one sound cylinder can contain `Theta(s2 log s2)` independent switches spread across all k blocks, matching the global upper bound `log |SIZE(s2)|=O(s2 log s2)`. This retires block-count, free-coordinate count, and raw owner-mask entropy as ways to improve the splice contradiction.

C-315's local counting family has a sharper distributional corollary: with constants giving an exponent margin, a uniform independent tuple of moderately hard blocks is globally high except with probability `2^(-Omega(s2 log N))`. Yet the diagonal tuple family obtained by repeating one local function can be globally small because one circuit ignores the prefix. Local hardness and global independence must therefore be kept distinct. The live Q177 target is to measure **description incoherence** between independent block choices and correlated restrictions of one global circuit, inside the compatible-support grammar. No direct-sum law, q improvement, or P-vs-NP result is established. Full calibration: `research/C317_BLOCKWISE_SAFE_CYLINDER_TENSORIZATION_2026-09-28.md`.

Direct-sum theorems for tensor-product Boolean matrices are only a source of techniques: native endpoints can couple blocks globally, as C-257's parity carriers demonstrate. A tensor argument needs a valid factorization theorem or a q-sensitive cost for such global couplings; endpoint factorization cannot be assumed.

## C-318 - Prefix restrictions are a cofactor ensemble

Split address inputs into a prefix selecting one of `k` blocks and a suffix. The block restrictions `(f_a(y))_a` form a vector-valued cofactor ensemble. In the exact SIMD model where each gate acts coordinatewise on k-bit wires, suffix inputs are diagonal vectors and prefix inputs are fixed lane masks, the scalar circuit size of the global function is **exactly** the vector-circuit gate count: scalar gates lift lane-wise, and conversely each vector wire is scalarized by selecting the lane indexed by the prefix inputs. Repeated identical blocks share a single cofactor circuit, while C-315's independent moderate-hard blocks are globally high with overwhelming probability by counting.

The C-281 grammar is also SIMD over blocks: supports split into k partial-assignment lanes, and one paid state performs a compatibility-filtered union across the whole lane vector. This is not the same algebra as Boolean SIMD circuits. The sharpened target is a bridge or a direct q lower bound between these two ensemble models. Generic matrix tensor direct-sum theorems do not apply because native endpoints can couple lanes globally (C-257). This exact reformulation gives no q bound or P-vs-NP result. Details: `research/C318_COFACTOR_ENSEMBLE_AND_NATIVE_SIMD_MODEL_2026-09-28.md`.

Equivalently, let `E_s` be the k-lane ensembles of global circuit complexity at most s. Each proof support is a product box across blocks; soundness requires each box inside `E_s2`, and completeness requires the generated box family to cover `E_s1`. The q-state system is therefore a **cofactor-SIMD interpolation cover** over a compatibility-filtered box algebra. This is only a coordinate reindexing of the original problem, but it cleanly states what a q-sensitive bridge must analyze.

## C-319 â€” The native SIMD object is an alternating state game

For a q-pair fusion list, each state i has two seed clauses `A_i(w),B_i(w)`, each a consistent disjunction of signed truth-table bits (or the constant true), and two fixed predecessor sets. Its exact recurrence is

```text
x_i^(t+1) = ( A_i OR OR_(j in P_i^E) x_j^t )
            AND ( B_i OR OR_(j in P_i^H) x_j^t ).
```

The output is the OR of active empty-consequence states. This is an input-labelled alternating reachability game: the universal move chooses one of two endpoint obligations; the existential move supplies a matching literal or follows an active predecessor; cycles count only when the least fixed point reaches a true seed. A state clause can read literals from every cofactor lane, so lane count cannot be charged independently without a theorem controlling global coupling.

Unrolling q rounds gives at most q^2 paid AND gates. An ordinary monotone-interpolant lower bound therefore transfers only through a square-root loss; q>N^(1+epsilon) would require a lower bound above N^(2+2epsilon) by this route. The count-only variants do not bridge that loss: a singleton safe-box cover has at most `|SIZE(s1)|` boxes, whose logarithm is `N^(beta+o(1))=o(N)`, and any sound separator's accepted set lies inside `SIZE(s2)`, so the logarithm of its matrix rank is also sublinear. C-317 separately saturates the safe-box free-coordinate budget. None of these ceilings applies to a genuinely state-sensitive invariant.

The next model upgrade is a **state-graph synchronization measure**: it must quantify how a q-state alternating graph synchronizes independent block descriptions while preserving every compatible context/proof splice, and allow the linear-cost parity and repeated-equality constructions. Avoid endpoint-description arguments, box counts, log-rank, and free-coordinate entropy. Exact derivation and literature boundaries are in [C-319](research/C319_NATIVE_CLOSURE_AS_ALTERNATING_COFACTOR_GAME_2026-09-28.md). The actual lower bound remains `rho_GapMCSP=N-o(N)`.

## C-320/C-322 â€” From splice-mask restrictions to the pre-acceptance game

C-320 refines the code-splice argument: one split makes every off-diagonal code splice superlinear in a chosen exponent `gamma`, and all masks within `Theta(N^gamma/n)` of that split or its complement remain forbidden. This gives a robust compatibility constraint, but the forbidden balls are tiny and no proof shows that a q-state graph must generate a mask in them. The result is a calibration, not a state bound.

C-321 re-derives the seed-feature factorization and the 2N literal ceiling already recorded in C-76/C-221/C-260. It is an audit, not a new result; Q182 is closed as redundant.

**C-321 novelty correction.** This is an independent re-derivation of facts already recorded in C-76/C-221/C-260, not a new frontier result. Q182 is closed as redundant; the note remains as a consolidated audit.

## C-322 â€” Root broadcast and the pre-acceptance game

An empty-consequence root has its consequence contained in both endpoints of every state. Hence it is a predecessor on both obligations everywhere: activation of any root forces all states active one round later. Before the first root activates, the nonroot states evolve exactly according to a root-deleted least fixed point. The original output is equivalent to the OR, over empty roots, of their two terminal tests against that root-free closure. Accepted inputs therefore all have the same final activation profile, the all-ones vector. This retires final-profile VC/shattering as a synchronization statistic.

This is an exact structural reduction, not a state lower bound: the root-free graph may still use all nonroot states, and the terminal tests may combine arbitrary endpoint-derived clauses. Do not pursue further output-root normalizations. The active obligation is still a q-sensitive theorem for jointly realizable transitions and context/proof reuse. The actual bound remains `rho_GapMCSP=N-o(N)`; no near-linear full-promise cover or P-vs-NP proof has been found.

## C-323 â€” Root-free SCCs refine the circuit compiler

The root-free pre-acceptance graph has a useful exact parameter that the full graph hides. If there are m roots and root-free SCC sizes `r_C`, evaluate SCCs in condensation order. Each r-state component stabilizes in at most r rounds; each round uses one AND per state. The terminal root tests add at most m more ANDs. Thus the same separator has a monotone circuit with arbitrary-fan-in ORs and at most `m+sum_C r_C^2` AND gates. If every root-free SCC has size at most d, then `A_cap<=m+d(q-m)<=dq`.

In the full predecessor graph, an empty root points to every state. Every state used in a finite accepting proof has a path back to a root, so proof-relevant states coalesce with the root in one SCC. Those root edges represent only post-acceptance broadcast; deleting roots before SCC analysis can reveal the actual pre-acceptance component structure. This is a lower-loss transfer on covers with controlled root-free SCCs, not an unconditional lower bound. The large-SCC case still has the qÂ² loss, and no OPS SCC-profile theorem is known. Continue by proving such a profile bound or directly charging a large pre-root SCC through context/proof synchronization. Full derivation: [C-323](research/C323_PREROOT_SCC_COMPILER_2026-09-28.md).


## C-324 - Feedback-core depth is the relevant circuit-transfer parameter

The root-free SCC compiler can be sharpened: after deleting intrinsic self-dependencies, an SCC with r states and a feedback vertex set of k states has an acyclic remainder. Fixing the k core values lets the remainder be evaluated once in topological order; the k-bit least fixed point needs at most k strict rounds. This yields an AND-count compiler of at most `r+k(r-1)` per SCC, with a sharper parameter given by the maximum seed-labelled core iteration depth. Therefore an SCC can be large and still be cheap: a directed cycle or a hub-dominated SCC has k=1. The true graph-side obstacle is dense cyclic feedback or long core iteration, not SCC size alone.

This refines the decision tree for O-180: test whether feedback-core dynamics can be simplified using endpoint semantics, then search for an OPS-specific reason the remaining cycles force incompatible context/proof products. C-258 is a direct warning against feedback vertex number as a standalone measure: nested prefix carriers create many 2-cycles, yet the repeated-block subpromise has an O(N)-pair cover. C-281's owner-mask and description-coherence problem remains untouched. The actual bound stays `rho_GapMCSP=N-o(N)`; C-324 is a parameterized compiler, not a separation. Full derivation: `research/C324_FEEDBACK_CORE_COMPILER_2026-09-28.md`.


## C-325 - Separate free implication closure from paid conjunction

C-258's nested prefix carriers generate a bidirected path in each block/value branch, forcing `Omega(N)` feedback vertices across the construction even though the repeated-block subpromise has an `O(N)`-pair cover. Therefore raw feedback-set size cannot measure the cost of native synchronization. The exact recurrence can be factored: common predecessors appearing in both endpoint obligations become a free OR-propagation relation C, and the remaining work is a seed-labelled AND map G. The least fixed point is exactly `mu(cl_C o G)`. This identifies a sharper object for the model: how much new structure the guarded AND steps add after taking free implication closure. No bound for OPS follows yet. Continue from C-325/Q185, preserving C-257 parity, C-281 compatible splices, and C-317 safe cylinders. Full derivation: `research/C325_COMMON_PREDECESSOR_CLOSURE_AND_C258_FEEDBACK_AUDIT_2026-09-28.md`.

## C-326 - Equality cycles collapse to prefix products, but only on the equality subpromise

The C-258 repeated-block cover is now solved at its exact least fixed point. Its common-predecessor edges create many cycles, but the seed-labelled paid transitions are nested: branch state t is active precisely when the first t block bits equal a. The merge layer repeats the same prefix-product pattern over blocks. This explains mathematically why raw feedback size is irrelevant here: the cycles only propagate already-paid nested conjunctions backward. The exact separator uses `2N-d-1` AND gates under the high-cylinder richness condition.

Model consequence: a valid full-class synchronization measure cannot count cycles without reading the seed labels and their containment order. At the same time, the special total-prefix order supplies no theorem for arbitrary endpoint graphs. Close C-258 as a calibration; require any generalization to prove a full-promise transfer before treating it as progress. The true frontier remains the q-state game's ability to enforce one global small-circuit description across all N truth-table addresses. See `research/C326_NESTED_COMMON_CLOSURE_COMPILER_FOR_C258_2026-09-28.md`.

## C-327 - Pseudorandom source width must scale with the proof's actual term width

An almost-k-wise family of permutations is succinct, but succinctness alone does not preserve a sunflower lower bound. The relevant approximation has terms of width `w=Theta(v^(1/3)/(log v)^(2/3))`; to get a source lower bound exceeding `N^(1+epsilon)`, choose `v=(log N)^K` with K>3, making `w=omega(log N)`. Thus `k=O(log N)` cannot preserve the needed matching-term probabilities. Taking `k=Theta(w)` still has a polylogarithmic seed, but this does not control the full DNF union or create a CohEnc map. Learning: compare pseudorandomness order to every quantifier/term width in the proof before treating a succinct source as a hard transfer. Close this specified experiment; return primary effort to full-promise state synchronization. See `research/C327_SUCCINCT_MATCHING_AUDIT_AND_WIDTH_BARRIER_2026-09-28.md`.

## Current breakthrough checkpoint

No verified result in C-324 through C-327 improves the actual lower bound `q=N-o(N)`, constructs a full-promise `N^(1+o(1))` cover, proves a state-sensitive synchronization theorem, constructs a positive CohEnc transfer, or proves a general reconstruction-to-decision compiler. C-326 is the exact repeated-equality calibration; C-327 closes one secondary pseudorandom-source parameter choice. Keep the long-horizon objective unchanged. The next work must prove a theorem directly about the full promise or build a valid full-promise cover; another local invariant is not a success.

## C-328 - Secret-sharing hardness needs an address-scale transfer

Recent meta-complexity work gives explicit monotone circuits on `Theta(t)` input variables whose total secret-sharing complexity is `Omega(t^2/log t)`. At truth-table length `N=2^(Theta(t))`, this is only `polylog(N)` and cannot move the native lower bound above its `N-o(N)` floor. The secret-sharing recognition problem's coNP-hardness does not itself imply a Gap-MCSP q lower bound.

The native proof grammar has an exact compatible-support ideal model, but that algebra has `3^N` states/monomials in its faithful representation and tests an input-dependent full-table monomial. A useful cross-field bridge would need a lower-bound-preserving translation from the q-state grammar to a compact secret-sharing scheme or vice versa, with cost `O(q polylog N)` or better. No such translation is known here; a direct use of the share-size theorem is closed. Preserve the idea only as a conditional interface, not a new invariant. See `research/C328_SECRET_SHARING_LOWER_BOUNDS_DO_NOT_SCALE_TO_NATIVE_Q_2026-09-28.md` and C-304.

## C-329 - A shared state is not a lane-wise selector

The exact reachability game has positional winning policies. Fixing one policy gives a cube of input tables accepted by that policy; valid-cover soundness forces the entire cube into `SIZE(s2)`. This is an exact normal form, but counting policies is ineffective: there are at most `q(q+2N+1)^(2q)`, while low-table families have only `2^(o(N))` descriptions. This yields no bound above the existing `q=N-o(N)` floor.

The attempted near-linear universal-circuit verifier exposes a separate issue. In ordinary SIMD circuit evaluation, an OR gate may use child u on one address lane and child v on another. A positional policy at one shared native state selects one successor for all histories reaching it. The two-lane pattern `(u,v)=(1,0)` and `(0,1)` is already enough to break the shared-gate construction. Copying address contexts restores lane-specific choices but incurs the familiar gate/address product.

Model update: the native game is lane-wide in what it can constrain, but a reused state does not carry a lane-indexed control register. Compatible-support multiplication joins partial assignments and deletes conflicts; it is not pointwise Boolean-vector multiplication. The open question is whether an encoding can recover lane-specific selectors within `N^{1+o(1)}` states, or whether this mismatch forces superlinear q on the full low-circuit class. The toy obstruction rules out only the proposed shared positional gate-witness architecture; it is not a theorem about arbitrary endpoints. See C-329/Q189.


## C-330/C-331 â€” What the latest two audits add

The C-319 system is not a general alternating verifier with a writable proof tape. Its only input-dependent persistent object is the least-fixed-point activation vector. A positional action choice is not observable to a parent, and activation rank is not an output: every winning state eventually becomes true, while downstream equations use only true/false predecessor status. Therefore a strategy cannot silently carry a global circuit description or PCP proof through merged contexts.

The new TR26-220 sunflower theorem is a potential tool for vertex-color distributions, but not for the matching edge distributions in C-310. D0 has cycle constraints; D1 has incident-edge exclusion. A vertex-color lift doubles term width and does not improve the matching-specific sunflower parameters. C-327 stays closed unless a new source architecture also solves the missing C-125 map.

The live construction question is now sharper: find a globally shared witness whose value is *observable* from the state activation vector without copying every address context, or bypass witness verification entirely. The corresponding lower-bound question is to charge that readable commitment inside arbitrary compatible context/proof products. The actual q floor remains N-o(N); neither route has advanced it.


## C-332 â€” Alternation-sensitive pseudorandom shrinkage as a distinct route

The MCSP literature contains an almost-quadratic lower bound for ordinary branching programs, proved from local pseudorandom generators. The proof's low/random input contrast is promise-compatible, but the generator's output tables have circuit complexity about the square root of the BP size. At the project's small beta thresholds, this local complexity is too large. The known theorem also does not apply to C-319, whose state equations are cyclic and universally alternating.

This gives a precise new target rather than a transferred result: prove a local-PRG or shrinkage theorem directly for the q-state positive alternating reachability system, with output-table complexity below s1 at q around N. The theorem must distinguish the full Gap-MCSP promise and survive the parity-lock construction. A compiler to ordinary branching programs would also need a proven near-linear size bound; neither compiler nor shrinkage theorem is known here. The actual native lower bound remains N-o(N).


## C-333 â€” Low-degree polynomial outputs reveal a parity trap in generic PRG attempts

Choosing a random degree-<K polynomial over GF(2^n) and taking its trace gives a K-wise independent truth table computable by O(Kn^2) gates. At K=Theta(s1/n^2), this is a genuinely low-circuit source, but its N output bits lie in a linear code of dimension at most Kn<N. A nonzero dual codeword gives a parity test that accepts every source output and half of uniform tables. The abstract C-319 equation syntax computes this parity with O(N) states. C-257 gives a related O(N)-pair cover only for an artificial parity universe; endpoint realization over the actual high-table universe is not shown.

The key qualification is that the parity tester is not sound for Gap-MCSP; it rejects many low tables. Generic abstract-game PRG is too strong, while the necessary PRG for actual sound pair systems is essentially the unresolved lower-bound statement. C-257's endpoint realization uses an artificial parity universe, not the actual high-table universe. A second parameter obstruction is joint dependence: 2q seed clauses of width O(log q) can inspect min(N,O(q log q)) coordinates, so matching each clause marginal does not fool the readout. The model's new distinction is **generic indistinguishability versus sound-separator indistinguishability**. Only the latter could advance Q192, and it requires exploiting endpoint incidence and soundness. No q or P-vs-NP result follows.


## C-334 â€” Strategy regions are small CNFs, but too numerous for generic PRGs

A positional winning strategy need not name one true literal each time it uses a seed. It can keep the whole seed clause as the condition for that stop. Fixing predecessor choices and these seed stops gives a CNF region with at most 2q clauses; the same strategy wins everywhere in that region. There are at most q(q+2)^(2q) raw strategies, but at most 2^(2q) distinct policy-CNFs, since only the subset of fixed seed clauses used at stops determines the region. Every region of a sound cover lies in SIZE(s2); the standard satisfying-count argument forces at least N-o(N) clauses per nonempty region, but because a policy has at most 2q clauses this only recovers q>=N/2-o(N).

This normal form makes a nonlinear source avenue concrete. Naor-Naor epsilon-biased sample spaces have seed length O(logN+log(1/epsilon)); a fixed-seed output table has polylogN circuit size, and every parity test has small bias. They remove the specific linear parity defect of C-333. But Bazzi's limited-independence theorem, applied separately to at most 2^(2q) distinct regions, needs k=O(q^2), which is too high at qâ‰ˆN. The next step must exploit overlap among policies or endpoint soundness directly. This is a precise route, not a q improvement or P-vs-NP result.

## C-335 â€” GEN blocks a generic recurrence-to-span-program translation

With arbitrary predecessor sets and positive input seeds, a q-state least-fixed-point recurrence computes GEN_n using O(n^3) states. Yet GEN_n requires monotone span programs of size 2^{n^{Omega(1)}} over every field. Thus an abstract native-like recurrence can be much more succinct than any MSP; one cannot infer a small MSP from its state count alone. The generic formula-unrolling conversion is too large to improve the q floor. Endpoint incidence alone does not block GEN internal states: assign each gate its truth set over the high-table universe as consequence. All such consequences are nonempty, so the empty-root output remains false. The unresolved restrictions are empty-root semantics and full-promise soundness. C-335 does not establish such a bridge or any q bound.

**Priority boundary:** C-335 is a structural calibration, not the primary frontier. Under the C-319 continuation directive, the next work belongs on O-167/O-168: charge state reuse across compatible context/proof products, or give an explicit full-promise near-linear cover. Revisit the span-program route only if it supplies one of those outcomes.

## C-336 â€” Multi-hole reuse creates a product constraint

Cut several state occurrences from one accepting derivation and replace them independently. If the union of supports is consistent, the result is still an accepting proof; its entire cylinder must stay below the `s2` threshold. At the project parameters, `K log N` independent block choices can be made from families whose one-block embeddings are each `s1`-small, while their full product is larger than `SIZE(s2)`. Therefore a single context cannot expose all those choices independently. This gives a concrete form of the global synchronization problem: the game must either prevent the multi-hole product through support incompatibility or encode a common selector across blocks. What remains unknown is how many states that prevention costs. No superlinear bound follows yet; see C-336.


### C-337: independent products can be blocked by a cheap global selector

The C-336 multi-hole splice law rules out one accepting context exposing all independent block replacements, but it does not charge the number of states needed to avoid that product. For `k=K log N` subcubes, there is an explicit signed monotone circuit with `N+O(log N log^2 log N)` AND gates that accepts tables supported on at most `R log N` blocks and rejects the all-block independent product. All accepted tables have size at most `s2`; by C-307 the construction yields a restricted native cover. It accepts every one-block `s1` anchor, so the product obstruction alone cannot force additional states.

This selector does **not** cover all `SIZE(s1)`: it rejects many dense low tables, including parity and repeated-equality examples. Thus it is a calibration, not O-168. The next theorem must make essential use of the all-low coverage requirement, or exhibit a selector broad enough to cover every low circuit. C-336''s one-block circuit overhead is `O(n)` for a general fixed subcube, not always `O(log k)`; the correction does not affect its asymptotic claim because `s1 >> n`.



**Selector stress test â€” distinct rows still do not measure shared description.** A stronger block selector can allow up to d=R log N distinct row patterns: compare every pair of rows, enumerate d representatives, and require every row to match one. Its extra AND cost is O(k^2*M + k*binom(k,d)) = o(N) for k=K log N, M=Theta(s2), and R small. This includes repeated rows but still rejects a low table with row b equal to the minterm [the first log k suffix bits equal b]. All k rows are different, while one O(n)-size global circuit generates the entire table by testing block-prefix = suffix-prefix. Hence the right invariant must measure the complexity of the relation generating cofactor rows, not just activity or the number of distinct rows. See C-337.


### C-338: sample hardness still lacks asymmetric code rails

The July 2026 monotone-learning and partial-monotone-MCSP results produce hard labelled-example instances under rETH, not a monotone C-125 map to full truth tables. The natural example rails lie below any low code fitting the sample, but the transfer needs the low code below the YES image. Setting both rails on every unobserved coordinate fixes that order and destroys consistency, so no high one-hot completion can dominate the same image on NO. Reversing input bits to mark omitted examples makes fitting monotone but makes reconstruction of the retained sample set nonmonotone. The unresolved requirement is a witness-dependent rail construction that is monotone, conflict-rich on YES, consistent on NO, and cheaper than the source decision function by a positive margin. See C-338 and the primary paper at https://arxiv.org/abs/2607.12331.


**C-339 model boundary:** the q-state alternating recurrence has a known q^2 binary-AND unrolling into a signed monotone shared DAG. Hence a superlinear q bound needs a direct separator lower bound above N^2 (more precisely N^(2+2epsilon) for q>N^(1+epsilon)). Stronger MCSP formula bounds cannot be used without a sharing-preserving conversion; ordinary branching-program bounds omit universal alternation and cyclic least-fixed-point semantics; SoS lower bounds concern proofs; and the exponential CNF bound stops at CNF. The target is now sharply identified as the actual shared-DAG/alternating-game model. No current theorem crosses this boundary. See research/C339_MCSP_LOWER_BOUND_MODEL_TRANSFER_AUDIT_2026-09-29.md.

**C-340 quantifier correction:** the N*s1 gate-address product is the cost of checking one supplied circuit description. It is not a full-promise cover, because the cover must use one fixed state graph for all low tables and maintain one circuit choice across every universal address challenge. A genuine cover at q=O(N*s1) would sit below N^(1+epsilon) for beta<epsilon and refute the proposed rho route. The fixed-description evaluator does not implement this existential selector: per-address choices allow different circuits, while shared gate states lose the address. The OPS circuit lower-bound theorem itself is not contradicted because the known q-to-circuit conversion costs q^2. See research/C340_NS1_EVALUATOR_IS_NOT_FULL_COVER_2026-09-29.md.

**C-341 â€” Selector choices need a readable continuation.** A positional choice at a shared gate-configuration state is globally fixed for each state-side obligation, but the continuation after entering that state no longer knows which address called it. Gate-configuration consistency and address-dependent OR-witness choice are separate requirements: `x_1 OR not x_1` is true at both addresses, yet two lanes reaching the same state-side cannot use different child actions. A successful compression needs an explicit mechanism that jointly preserves the global description and address context through evaluation; strategy choices alone are not a readout, and support tags alone cannot act as control state (C-306/C-331). This retires one architecture only, not all native selectors. Current q remains `N-o(N)`; O-167/O-168 remain open.

## C-342 - A selector needs a readable channel

The exact C-319 equations factor all input dependence through `2q` seed-clause truth values. Once that signature is fixed, every activation bit, root result, and set of winning positional policies is fixed. An existential choice of successor is proof data: another state cannot read which successor was selected. Thus a circuit description cannot be transmitted by a shared positional choice.

The second candidate channel, proof-support provenance, also has a precise limit. For one accepted table `w`, every matching context support and every matching replacement support is contained in the same one-sided literal set `ell(w)`. Every pair is compatible, so C-281 substitution requires the complete context-by-proof product to remain sound. A support code therefore cannot keep a private caller/description correlation at a reused state; all cross-completions must be low.

This does not mean the game has no memory. The activation vector has q bits and the seed signature has 2q input-derived bits; at q near N these have enough raw capacity to encode substantial information. One-hot activation markers could read a description if it were already known. The hard step is selecting and activating one globally valid description from a general low table: activation is deterministic from the seed signature, so an existential strategy cannot write this code. Then every address-check state must read the code without a gate-by-address product. The other direction must turn the same-anchor safe-rectangle law into a state lower bound for arbitrary covers, without assuming they evaluate a particular circuit. C-342 gives the channel boundary and exact proofs, but no q improvement. See `research/C342_OBSERVABLE_SELECTOR_CHANNELS_AND_SAME_ANCHOR_RECTANGLES_2026-09-29.md`.

The multiplexer gives a bounded test of the residual-context idea. If an explicit verifier state is required to return `Mux(d,a)=d_a`, the residual functions for different a are pairwise distinct, so one shared address-free continuation cannot answer all addresses. This proves a state lower bound for that verifier interface only; arbitrary native covers need not expose mux queries.

**Novelty boundary:** the factorization restates C-319, and same-anchor rectangularity is C-281/C-306. The useful addition is a consolidated selector-channel model and the restricted mux residual test; no general q lower bound was found.

The path-only selector has an explicit superpolynomial state lower bound. For `r=floor(s1/(3n))`, indicators of r-element subsets of the N addresses have circuit size at most `s1` and yield `M=binomial(N,r)=2^(Omega(s1))` distinct functions. An exact selector that stores the chosen function only in its post-selection graph state must assign distinct residual states to all M functions, since two different indicators disagree at some address. This excludes a path/state register at polynomial q. It does not exclude input-derived seed/activation codes or non-evaluation proof grammars; the full arbitrary-cover target remains open. See C-342.

## C-343 - Preserve the witness quantifier; audit the magnification bridge

The per-address verifier formula `forall a exists C_a: C_a(a)=w_a` is true for every table: use the constant circuit equal to `w_a`. MCSP membership needs `exists one C forall a`. This is the exact logical reason that independent gate/address copies do not enforce one global description. Shared states can preserve a positional choice but lose the challenged address; path-only storage of a circuit has superpolynomial residual-state cost; same-anchor proof supports cannot be a private caller tag. These exclude specific encodings only.

The earlier C-109/Idea 109 theorem already compiles every standard De Morgan circuit separator of size S for disjoint promises Y,Z into a valid fusion cover with at most `3S+1` rules. Thus a `rho>N^(1+epsilon)` lower bound would itself prove a general circuit lower bound of the same exponent for Gap-MCSP, and by OPS would imply `NP` not in `P/poly` with a fixed exponent margin. Under `NP subseteq Circuit[poly]`, the OPS contrapositive supplies circuit upper-bound instances at arbitrarily small beta choices, which C-109 converts to same-exponent conditional fusion covers. This is conditional, not an unconditional construction. The other direction remains different: C-319 unrolling gives at most `q^2` paid AND gates when OR fan-in and semantic seed clauses are free; do not identify that measure with standard fan-in-two circuit size. The actual q bound remains `N-o(N)`. The next target is the general Gap-MCSP circuit lower bound or a direct q proof strong enough to imply it; selector-layout no-gos are no longer the main branch. See `research/C343_QUANTIFIER_COHERENCE_AND_MAGNIFICATION_BRIDGE_CHECKPOINT_2026-09-29.md`.

## C-344 - Worst-case high complexity is compatible with easy uniform approximation

The explicit Gap-MCSP NO promise is worst-case circuit complexity. The recent full-support learning problem requires that no subexponential-in-s predictor achieve noticeably better than 1/2 accuracy on a sampler-specified distribution. These conditions are not interchangeable. Fix a low table g. A Hamming sphere of radius `r=K s2` around g has more elements than `SIZE(s2)` for K sufficiently large, so it contains a promised high table f. Yet f differs from g at only r addresses; the exception set can be listed with an `O(r logN)` circuit, giving a predictor of size `poly(s1)` with accuracy `1-o(1)` under uniform addresses. Therefore the direct uniform-example encoding misses the learning NO promise on some high tables. Only a newly constructed f-dependent anti-checker sampler could repair this; its all-small-circuits hitting guarantee is the unresolved computational task. The actual fusion bound is unchanged. See `research/C344_FULL_SUPPORT_LEARNING_ROUTE_HAS_NEARBY_HIGH_APPROXIMABLE_TABLES_2026-09-29.md`.
## C-345 â€” Learning gaps versus hard-core-list synthesis

The Total-Learn target has an explicit predictor cutoff g(s); the 2026 theorem permits polynomial g, including g(s)=2s. So the uniform-sampler failure in C-344 does not eliminate every table-conditioned distribution. If f has CC(f)>T*(ln N+1)/(2 epsilon^2)+O(T), minimax gives an address distribution on which each size-T circuit has error at least 1/2-epsilon. A sample of O(T log(T+n)/epsilon^2) addresses preserves a constant error margin simultaneously for all size-T circuits. For T=lambda*s1 this sample has O(N^beta) entries under the OPS parameters, provided the gap constant c has enough slack. Adding a small uniform component yields full support. The sampler can encode an explicit truth table after padding the domain dimension; its representation size is polynomial in that padded dimension.

The failure point is computational: Q exists for each f, but the project has no efficient selector f -> Q. This is the same universal anti-checker synthesis problem in O-1/Q201. Conversely, the C-344 nearby-high table has an exact circuit of size O(s2*n), so no distribution can satisfy a target whose g(s1) exceeds that cost. Keep the two statements separate: large learning gaps are blocked by exact patch predictors; constant-factor gaps retain pointwise feasibility but not an effective reduction. Full parameter proof: research/C345_TOTAL_LEARN_GAP_PARAMETER_AND_POINTWISE_HARDCORE_MAP_2026-09-29.md.
## C-346 â€” The hard-core existence constants fit the OPS gap

The OPS proof explicitly uses c=10. Separate two losses in the minimax argument. With T=ceil(1.5*s1) and hard-core margin a=0.24, k=ceil((lnN+1)/(2a^2)) sampled circuits have a majority circuit of size kT+O(k^2), using a direct threshold-counting dynamic program; k=O(n), so this overhead is negligible relative to s2=N^beta. The leading ratio kT/s2 tends to 125 ln(2)/96<0.903. Hence CC(f)>s2 forces an address distribution where every size-T circuit errs at least 0.26. A separate empirical tolerance eta=0.001 yields a list Q of O(N^beta) points with error at least 0.259 for every size-T circuit. Mixing uniform addresses at weight 1/1024 gives full support and predictor accuracy below 0.742. This meets a Total-Learn NO cutoff of 3/4 with predictor gap 1.5, and domain padding makes the sampler description polynomial in its domain dimension.

The result is pointwise: every high f has such a Q. It does not compute Q from f. The next barrier is exactly this selector, with validity forall small circuits C, exists a listed disagreement. Full derivation and the conditional-theorem boundary are in C-346.

## C-347 - Algebraic fingerprints compress communication, not native state

The low-function witness condition is `exists C forall addresses a, C(a)=f(a)`. A direct arithmetic translation of C may have degree `2^s`; a low-degree multilinear extension of C's truth table is not known to be cheaply evaluable from C. Sum-check cuts communication but needs the accumulated challenges at its final query. C-319 states have no caller-history input, and same-anchor proof supports cannot serve as private transcript registers. Thus the standard algebraic verifier either loses the challenged address at a shared state or restores gate-by-address copies. This is a construction-specific no-go, not a general q lower bound. A new method must make the challenge readable from input-derived activations while preserving all compatible splices. Actual q remains `N-o(N)`.
## C-348 - Closure-expanded feedback is useful only with absorption

Common-predecessor edges can be factored as free static closure, leaving one residual AND term per state. A feedback vertex set of size k in the closure-expanded dependency graph yields an exact separator with at most m+(k+1)q0 AND gates. C-258 defeats the hope that k is small on cheap subcovers: its k is Omega(N), although its nested prefix products compile linearly. The needed refinement is an absorption-aware invariant that charges full-promise synchronization while assigning C-258 linear cost. No such invariant is known.

## C-349 - Selector matrices need representation invariance

A local OR-witness matrix attached to one chosen circuit is not a cover invariant. Output padding f OR 0 makes the output selector constant, disjoint-OR normalization changes witness patterns at constant size overhead, and De Morgan conversion can remove OR gates. The canonical object is the gate-value trace, but an address-by-gate trace still needs a readable global description and an address channel in C-319. Do not infer q>N from hardness of one selected M_C. The live target is a representation-invariant trace/readout lower bound that transfers from every valid cover, or an explicit full-promise near-linear readout construction; actual q remains N-o(N).
## C-349 - A representation-invariant selector matrix is not enough

The A-E checkpoint is all NO. Do not continue generating circuit-local selector normal forms. The next route works directly with C-281 support grammar: a reused state has context and replacement-proof support families, and every compatible cross-pair creates a sound owner-mask hybrid. The goal is to show that a low-state grammar must either generate a C-320-forbidden hybrid or spend many rules. The naive per-state capacity claim fails because full anchor supports K=P=ell(w) can make different anchors incompatible. The missing bound must charge the grammar's ability to generate these supports selectively against the complete high universe.
## C-350 - Wide certificates have balanced state cuts

A sound accepting proof fixes at least N-kappa_square(s2)=N-o(N) coordinates. Following the larger of the two proof branches down the tree until the remaining support first drops below half yields a marked state with Omega(N) support on each side: context width at least half and replacement width between one-quarter and one-half. Therefore some state has balanced-cut load at least |F|/q on any chosen low subfamily F. This is an exact extraction lemma but no lower bound: overlap can erase the owner mask, and code-family splices may remain low. The missing theorem is grammar-sensitive: force a compatible forbidden owner mask from high balanced load, surviving parity and repeated-equality covers.


## C-351/C-352 - Compatibility is the hinge, and it is local

At a fixed context K, mutually consistent replacement supports obey a sharp projected-diameter constraint: on coordinates not fixed by K, their anchor projections differ pairwise on at most 2*kappa_square(s2) positions. The mutual-consistency hypothesis is essential. A product across several holes only tests one choice per hole, so it says nothing about whether two alternatives at the same hole conflict. Complete supports ell(w) for distinct low anchors give individually sound singleton cylinders and avoid all pairwise joins. C-258/C-326 realize these supports on the repeated-block subpromise with a linear native list, but not for the full low-circuit class. Thus the missing object is the extra grammar cost of extending this fingerprint to all low circuits. The lower bound remains N-o(N).


The exact compatibility rule for a complete multi-hole product is coordinatewise: among distinct holes, every sign appearing in one replacement menu must agree with every sign in another. Opposite-sign variation can be hidden within one hole, since two alternatives there are never selected together. This explains why cross-hole products do not bound within-hole menu size.

## C-353 - The grammar is known; its joint composition cost is not

C-245 already specifies the marked proof and context antichain recurrences, and C-260 gives the certificate/blocker dual. The unresolved object is their joint use, not another encoding of the grammar. On repeated-block anchors w_g(p,u)=g(u), a context K from g and replacement C from h are compatible exactly when g and h agree on every suffix u represented in both supports. Outside that overlap fingerprint, the owner assignment across prefix blocks determines whether a splice remains a low diagonal table or becomes a non-diagonal hybrid. Block isolation would make the independent products force exponential q, but the diagonal family has an O(N) equality cover, so no isolation theorem can hold for arbitrary proof choices. The desired invariant must charge nonlocal ownership variation together with blocker maps, and stay linear on equality and parity. No such potential is proved; the actual bound is still N-o(N).

## C-354 - One-suffix owner masks give a smaller-instance splice test

Fix two repeated-block low anchors that differ at one suffix `u0`: `w0=0` and `w1(p,u)=1[u=u0]`. A splice is exactly `z_mu(p,u)=1[u=u0]mu(p)`, with `CC(mu)-O(1) <= CC(z_mu) <= CC(mu)+O(n)`. For fixed `beta<1/2`, the mask domain has `r=Theta(N/s2)` points, while the number of size-`s2+O(n)` prefix functions is only `2^(O(s2*n))`; hence almost every mask creates a high table. C-281 then says every compatible same-state context/proof pair across these two anchors must produce a low-complexity mask. This gives a concrete local invariant: the compatible owner-mask relation cannot contain a large Boolean cube (dimension above O(s2*n)).

What this teaches: â€œownership variesâ€ is too imprecise. A single changed suffix can carry a whole smaller truth table, and the relevant local obstruction is whether the support grammar exposes a high-complexity prefix function through compatible joins. Restricting any full game to this slice also preserves the abstract signed-clause recurrence at the same q, with the exponent changed from beta to `beta/(1-beta)`; this could transfer a future lower bound from the more permissive reduced model, but it is not an endpoint-list reduction. The missing global step remains forcing such a join, or charging the rule cost of preventing it. Complete supports can avoid every cross-anchor join at linear cost on the equality subpromise, so this is not yet a q lower bound. See `research/C354_ONE_SUFFIX_OWNER_MASK_REDUCTION_2026-09-29.md`.

### C-355/C-356 - Tree geometry is not synchronization cost

C-355's LCA split is valid for canonical proof trees: either a linear fraction of the varying-column coordinates is duplicated at one rule occurrence, or a state cut exposes a linear exclusive-owner set and a large context. This fixes a proof-tree geometry gap but does not prove a q bound.

C-356 is the hostile calibration that determines what this dichotomy can and cannot support. On the C-354 column, take d=Theta(s1) prefix blocks and let each block be a repeated bit. There are 2^d low tables, their pairwise Hamming distance is r/d=Theta(N^(1-2 beta)), and for beta<1/3 that exceeds the sound free-coordinate allowance. Yet the family is a product code; add fixed-zero singleton blocks outside the column and C-258 gives an O(N)-rule native cover against the actual high set. So low-family size, code distance, proof support width, and a pigeonholed state/triple cannot alone force a high splice. The missing object must charge how the exact transition graph realizes the shared equality fingerprint while covering all low circuits, or produce a full-promise near-linear cover. The measured bound remains rho_GapMCSP>=N-o(N); neither report advances P vs NP.

### C-357/C-358 - Generic compiler limits; RM code membership is cheap

C-357 counts a family of monotone CNFs represented by O(q)-state reachability readouts and proves that some require Omega(q^2/log q) bounded-fan-in ordinary gates. This blocks a generic subquadratic total-gate compiler. It does not settle the paid-AND measure used by the q^2 unrolling, and it does not imply a Gap-MCSP lower bound. Pauly's 2018 paper on parameterized games explicitly poses the circuit size of least-fixed-point graph-game forms as an open question.

C-358 tests the exact C-355 Reed-Muller family. The fast Boolean MÃ¶bius transform computes ANF coefficients in O(r log r) gates; high-degree coefficients all vanish exactly on RM(d,m). Testing the remaining N-r bits to zero gives an O(N)-size separator for this RM subfamily from the actual high set, hence C-109 gives an O(N)-rule native subpromise cover. The code family is therefore not a q-hard witness even though it has exponential size and large distance. The broad goal remains unchanged: find a state-sensitive theorem for all low circuits or a full-promise near-linear cover.

### C-359 - Fixed selector matrices have a linear partition ceiling

For a fixed circuit's address-by-gate selector matrix, the address side has only N rows and the local action alphabet is constant. Partition by (address, action): each cell family is a monochromatic rectangle, so there are at most kN rectangles (2N for forced binary OR witnesses). Standard deterministic communication complexity is at most log N+O(1), and standard fooling sets cannot exceed the row scale. This rules out the hope that making one fixed circuit's selector entries more complex will force a superlinear native state count. It does not constrain arbitrary C-319 covers. The needed object is a relation lifted across low anchors/descriptions together with a proved reduction from every valid cover, or a direct grammar-sensitive splice theorem. The native lower bound remains N-o(N).

### C-360 - Tree weighting is neutralized by native state reuse

Formula leaf-weighting turns each occurrence of a variable into an s-way OR, so its cost scales with the number of occurrences. A shared circuit computes the weighted OR once and fans it to every use; C-319 likewise has one state activation reused by all incoming derivations. Therefore the formula search-to-decision theorem does not transfer by counting paths or occurrences. The useful conceptual residue is to weight semantic state-context incidence: tags for distinct address/circuit contexts must either remain separate or, if merged, produce a forbidden C-281/C-320 splice. The forcing step is open. Ren-Santhanam's relativized separation of MCSP decision from search reinforces that arbitrary decision acceptance does not automatically expose a witness. Current native q remains N-o(N).


### C-361 - Output indexing preserves data volume, not description coherence

The right way to serialize a vector truth table is h(x,i)=F_i(x): adding log b index bits creates b slices and keeps the table length within a constant factor. This corrects the false "exponential table blow-up" objection. The real mismatch is computational. A circuit for the vector plus an O(b)-size mux computes h; conversely h's b cofactors give a generic vector circuit of size b times larger. Multi-MCSP can measure the cost of adding T to an already-shared family g, namely CC(T â€¢ g)-CC(g). A scalar MCSP threshold sees absolute cost and has no free access to g, so it cannot simply subtract that baseline. In the published construction, T is itself a random hard slice, and the output count makes its scalar restriction too large for the low promise at sufficiently small beta. The model lesson: preserve the distinction between table volume, indexed-evaluation cost, and incremental multi-output cost. Revisit only with a concrete encoding that resolves all three and meets the actual thresholds; otherwise the primary problem is still global description coherence in the C-319 state graph, not a wrapper reduction.
### C-362 - Native state count differs from graph-game description size

An exact q-pair recurrence becomes a reachability game with q universal state nodes, 2q existential obligation nodes, up to q predecessor exits and N signed-literal exits per obligation. Thus explicit graph size is O(q(N+q)+N), not O(q). The input enters only through 2q endpoint-selected ORs of consistent signed literals, and cycles without a true seed lose. Pauly's graph-game Proposition 9 gives a monotone-circuit depth bound but no size bound; Open Question 11 asks about circuit size for least-fixed-point graph-game forms. Therefore the literature does not give a generic q lower bound. The model upgrade needed is either a direct state-count theorem for this literal-exit interface or a q-sensitive charge for endpoint-selected seed incidence; counting graph edges, independent seed bits, support width, or raw signatures is insufficient. Current Gap-MCSP lower bound remains N-o(N).
### C-362 refinement - the native game is an LFP circuit instance

On independent dual-rail input u, let F_Q(x,u)=(T_Q(x,u),u), with T_Q given by the exact state recurrence. F_Q is a monotone circuit of size K=O(q(N+q)+N); the C-319 output is one bit of mu_x F_Q on consistent dual-rail inputs. Thus the fundamental model is not just a game graph: it is a succinct least-fixed-point operator with q recursive state bits and a structured literal input map. The generic iteration uses q copies of F_Q, but any substantially better circuit compiler is a separate open question. A useful lower bound must charge q in this specific LFP representation and must still separate all low tables from all high tables.

## C-363 - visibility is linear; readout is the unresolved cost

The C-319 input enters through `2q` signed-literal disjunctions. At q=O(N), singleton endpoint sides can make the conceptual seed signature injective. Those signature values are not free wires: they enter only through their paired state equations, so injectivity does not mean that the activation vector exposes each bit separately. Raw signature capacity, fiber counts, and pairwise signature distinguishability nevertheless cannot explain a superlinear q bound; the missing resource is the fixed least-fixed-point readout that must combine the coupled features into a sound low-circuit/high-circuit separator. The needed theorem is a readout lower bound or an explicit sub-N^(1+o(1)) construction, not a raw memory-capacity bound. Exact note: `research/C363_SEED_SIGNATURE_HAS_A_LINEAR_INFORMATION_CEILING_2026-09-29.md`.

## C-364 - Approximate-MCSP hardness has the wrong promise direction

A circuit patch argument shows every OPS Gap-MCSP NO table is Hamming-far from every `SIZE(s1)` table: distance is `Omega((s2-s1)/n)`. But this gives only `NO_Gap subseteq NO_Approx`; approximate MCSP is at least as restrictive and may have additional medium-complexity NO tables. Its formula lower bound does not automatically transfer to the Gap-MCSP separator, which may accept those tables. At fixed beta the low threshold `2^(beta n)/n` also fails the subexponential-in-n parameter of the new Atserias-Muller formula theorem, and formulas do not capture the cyclic shared-state C-319 readout. A useful bridge needs reverse containment/equality or a controlled reduction from the approximate promise. Full audit: `research/C364_APPROX_MCSP_HARDCORE_AND_DISTINGUISHER_TRANSFER_AUDIT_2026-09-29.md`.

Simple repetition does not supply that reverse reduction: it multiplies Hamming distance, but any fixed copy slice recovers the original function at O(log k) overhead, so circuit size is preserved up to small additive cost. A successful encoder must amplify circuit complexity while keeping low functions low and must have an efficient reverse decoder for every small output circuit.

### C-365 â€” Three channels for a shared circuit description

The universal-circuit audit separates the address-selector problem into three architectures. Supplying the description as an input lets one universal circuit evaluate it at every address, but a size-s1 circuit needs O(s1 log s1)=O_beta(s2) control/evaluation scale, consuming the OPS logarithmic gap; the lifted truth table also has 2^Theta_beta(s2) coordinates and only an N-bit image. Keeping the description only in a path/policy has the C-342 residual-function state explosion. Storing it in the activation vector fits by raw capacity because s2 is much smaller than N, but requires the least-fixed-point readout to find a valid circuit description on every low table. That is search-level witness extraction, not a consequence of decision acceptance. A valid direct separator may avoid circuit witnesses, so the activation channel is a construction target rather than a universal necessity. No q progress; see research/C365_UNIVERSAL_CIRCUIT_LIFT_SPENDS_THE_OPS_GAP_2026-09-29.md.

C-365 direction correction: the lift maps a source instance to a target instance. Restricting a target circuit or endpoint list to that image can transfer a target upper bound back to the source, but cannot transfer target hardness. An ambient target lower bound becomes relevant only through a reverse reduction or a direct lower bound for the image promise together with a q-preserving embedding of every source cover.

### C-366 - Output incompressibility is not search hardness

Kolmogorov incompressibility proves Shannon-scale circuit lower bounds for uncomputable truth tables such as prefixes of Chaitin's Omega. It does not show that a small search map cannot output a high-entropy description from an input that already contains the information: the identity map is the simplest counterexample. Applied to C-319, the activation vector depends on the table, so counting circuit-description bits against the fixed graph description does not rule out an activation decoder. Any self-reference route must force information absent from the input or prove a formal diagonalization. See research/C366_SELF_REFERENCE_ENTROPY_DOES_NOT_PROVE_MCSP_SEARCH_HARD_2026-09-29.md.

### C-367 - Separate description selection from all-address checking

A circuit-witness verifier has two costs: a search/readout map from the whole table to one small-circuit description, and an exact check that the description matches all N entries. The direct universal-circuit checker costs O(N s1 log s1)=O_beta(N^(1+beta)); that is an upper bound for this architecture, not a lower bound. The gate-by-address trace used by the straightforward evaluator does not prove every checker needs that many gates. A C-319 activation code would be a witness selector only if its description bits are coherently readable; a cover's decision acceptance alone does not imply this. The newly isolated circuit question is whether Eq(d,w)=[w=TT(C_d)] admits an exact N^(1+o(1)) circuit or a superlinear lower bound. Even either result transfers to arbitrary covers only with a separate witness-extraction theorem. See research/C367_DESCRIPTION_SELECTION_AND_ALL_ADDRESS_VERIFICATION_2026-09-29.md.

Fixed or deterministic adaptive coordinate queries have a separate counting lower bound: any verifier accepting a low table and rejecting every size-s2-high table needs N-O(s2 log s2)=N-o(N) queries along that low table's accepting path. Otherwise the unqueried subcube has more completions than SIZE(s2), so one high completion follows the same path. This is only a linear query bound and does not model the native gameâ€™s arbitrary ORs of signed literals.

### C-367 refinement - deterministic linear fingerprints also need nearly all bits

Along the accepting transcript for a low table f, adaptive GF(2)-linear measurements of rank r leave an affine fiber of size 2^(N-r). If r<N-log2|SIZE(s2)|, that fiber contains a high table with the same transcript. Thus deterministic exact fingerprints based on multilinear-extension evaluations or other linear sketches need N-o(N) independent answer bits. This remains a linear information bound and does not cover nonlinear circuits, randomized error, or C-319's arbitrary OR-of-literal seed map.

### C-367 refinement - Reed-Muller transcript bound

For a deterministic adaptive verifier whose answer bits are Boolean polynomials in the truth-table entries, let D be the sum of their degrees along an accepted low-table transcript. The transcript-fiber indicator is the product of the equations asserting that every answer matches. It is a nonzero Boolean polynomial of degree at most D. Reed-Muller minimum distance gives at least 2^(N-D) tables in that fiber; soundness therefore forces D>=N-log2|SIZE(s2)|=N-o(N). This rules out low-total-degree exact fingerprints, not arbitrary nonlinear circuits or the unrestricted native seed map. Full proof is in C367.

### C-368 - Every low acceptance needs a near-full monotone seed certificate

For the exact seed signature sigma_Q(w) and monotone readout G_Q, any accepted low table f has an inclusion-minimal true seed set S_f with G_Q(1_Sf)=1. Requiring all nonconstant seed clauses in S_f to remain true defines a sound CNF region: any table in it has signature above 1_Sf and is therefore accepted. A satisfiable m-clause CNF has at least 2^(N-m) models, while soundness permits only SIZE(s2) models. Hence every such certificate contains m>=N-log2|SIZE(s2)|=N-o(N) nonconstant clauses. Since a state pair supplies two seed features, this gives q>=N/2-o(N), weaker than the existing q>=N-o(N). The new use is structural: any superlinear proof must charge how large per-anchor certificates are shared across state sides or force a C-320 splice. Full proof: research/C368_EVERY_ACCEPTED_LOW_TABLE_HAS_A_NEAR_FULL_SAFE_SEED_CERTIFICATE_2026-09-29.md.

## C-369 - Large low families can share a linear certificate and native subcover

Partition addresses into d=2^k fibers of r=2^(n-k) points. The family of tables constant on each fiber has 2^d members; a decision tree on k input bits computes every member in O(d) gates. Choose d=Theta(s1) small enough that this is at most s1. The common CNF asserting equality of each fiber point with its representative uses 2d(r-1)=2(N-d) clauses and has exactly this family as its model set, so it is a safe certificate cone entirely inside SIZE(s1). C-258/C-326 also give this repeated-block family an actual O(N)-state native subcover when 2^(r-3)>|SIZE(s2)|, which holds for fixed beta<1/2 at these parameters. This does not cover every low circuit or say an arbitrary C-319 cover exposes this CNF. It does show that anchor count and the C-368 width floor alone cannot force distinct certificates or superlinear q. The live target is endpoint-incidence/least-fixed-point complexity for combining different circuit topologies, or a full-promise near-linear cover. Full derivation: research/C369_LINEAR_NATIVE_COVER_FOR_A_LARGE_REPEATED_FUNCTION_FAMILY_2026-09-29.md.

## C-370 - A near-disjoint witness skeleton inside every safe seed certificate

Fix an accepted low table f and its sound seed-CNF certificate. For each clause, take the set E_j(f) of table coordinates whose clause literal is true at f. Any coordinate set hitting all E_j pins one true literal per clause, leaving a subcube of satisfying tables. Since the whole cone lies in SIZE(s2), every hitting set has size at least N-log2|SIZE(s2)|=N-o(N). A random half-set hits every large edge except at most 1/2 in expectation; deleting edges larger than K=ceil(log2(2m)) therefore leaves a small-edge hypergraph with hitting number at least N/2-o(N). A maximal matching in it gives Omega(N/log m) pairwise-disjoint clause supports of size O(log m). For polynomial q this is Omega(N/log N) disjoint sparse witnesses per low anchor. C-258 equality realizes the calibration with singleton supports; this is structure, not a q lower bound. The missing step is charging these witness systems across anchors to positional state reuse or endpoint incidence. Full proof: research/C370_NEAR_PERFECT_HITTING_NUMBER_IN_EACH_SAFE_SEED_CERTIFICATE_2026-09-29.md.

C-370 clarification: the singleton f-true supports are those of the common equality CNF in C-369. They are not asserted to be seed clauses extracted from the separate C-258 native subcover; C-258 is used only as the matching easy-family state-count calibration.

C-370 refinement: if t_k is the number of certificate clauses with at most k f-true literals, the sampling proof gives the full tradeoff t_k >= N(2m)^(-1/(k+1)) - h - 1. In particular, for m=O(N), at least N/2-h-O(1) clauses have O(log N) true literals; and when beta<1/2, at least Omega(sqrt(N)) clauses have exactly one true literal. This strengthens the matching corollary but still supplies no state charge.

## C-371 - Pairwise splice coverage inside one safe certificate cone

If two low tables f,g lie in the same sound certificate CNF with m clauses and differ on d coordinates, their 2^d owner splices are distinct; at most |SIZE(s2)|=2^h can be low. Each high splice must falsify a certificate clause. A clause with a common f/g true literal never fails on a splice; otherwise its false-mask fraction is exactly 2^(-|E_f|-|E_g|), where E_f,E_g are its disjoint true-literal supports at the two anchors. Thus the sum of these fractions is at least 1-2^(h-d). If d>=h+2, some selected clause has disjoint supports with total size <=log2(2m). This is a necessary small-witness condition for every far pair sharing a cone. C-369 equality meets it with two singleton supports and O(N) clauses, so pairwise conditions alone do not charge superlinear q. The live target is a multi-anchor theorem tied to one positional state readout. Full proof: research/C371_PAIRWISE_SPLICE_COVER_CONDITION_FOR_SHARED_SAFE_CERTIFICATES_2026-09-29.md.

C-371 literature note: Cheraghchi-Kabanets-Lu-Myrisiotis prove exp(N/O~(log^2 N)) lower bounds for a single CNF or DNF computing exact MCSP, but one C-319 safe certificate cone is not the full acceptance predicate. The least-fixed-point readout may union many certificate cones, and no size-preserving flattening to one CNF/DNF is known. This result therefore does not transfer to q; see C-339 and C-371.

## C-372 - Dual-distance anchors and the common-policy barrier

The degree-t Reed-Muller evaluation code on N=2^n addresses gives a controlled low-circuit family with 2^r tables, r=N^(H_2(delta)+o(1)), each computable in o(s1) gates when H_2(delta)<beta. Its dual distance D=2^(t+1) means every projection onto fewer than D coordinates is the full cube. Therefore any seed clause true on every codeword has width at least D. A single sound CNF policy cone containing all codewords needs at least (1-o(1))*2^D clauses to reject the high-table universe, because each such clause falsifies at most 2^(N-D) tables. This gives an exponential common-policy obstruction for a low family whose pairwise distances also exceed h=log|SIZE(s2)|.

The boundary is precise: C-319 may use a different policy cone for each accepted table. Since r=o(N), the crude number of possible seed-clause subsets at q>=N-o(N) is already enough to separate the family member by member. Thus this theorem is not a q lower bound. The next proof obligation is to charge policy switching to the fixed transition graph or derive a high splice across cones. Parameter source: Reed-Muller duality and distance in the cited coding-theory notes; proof and scope in research/C372_REED_MULLER_SHARED_POLICY_CONE_OBSTRUCTION_2026-09-29.md.

## C-373 - Policy diversity from bounded independence

The C-372 Reed-Muller family gives an arbitrary-cover consequence. Uniform codewords are (D-1)-wise independent, so Bazzi's theorem implies that any sound policy CNF with m<=2q clauses captures at most O(m^2.2*2^(-sqrt(D-1)/10)) of the family, plus its negligible uniform-cube measure. At polynomial q this is 2^(-Omega(sqrt(D))). Therefore a complete C-319 cover must realize at least 2^(Omega(sqrt(D))) distinct positional-policy regions on this low-circuit family. C-334 bounds those regions by 2^(2q), giving q=Omega(sqrt(D)) only; the actual N-o(N) lower bound remains stronger. The important new layer is that the single-cone obstruction applies quantitatively even when policies vary. The open state-count question is whether one fixed transition graph can realize this many sound regions without paying more states or causing a high compatible splice. The general CNF-fooling theorem is complete here; only graph-sensitive structure could improve the charge. See research/C373_REED_MULLER_POLICY_DIVERSITY_BOUND_2026-09-29.md and Bazzi's paper, https://doi.org/10.1137/070691954.

## C-374 - Policy count cannot pay for state count

A valid cover can choose one safe policy region for each low table, so it never needs more than |SIZE(s1)| regions. At OPS scale log|SIZE(s1)|=o(N). A q-pair graph has at most 2^(2q) distinct seed-clause regions, so any argument based only on how many regions are required can extract at most q=o(N). This is weaker than the established q>=N-o(N) floor. C-373's Reed-Muller per-region bound remains correct, but its region-count corollary cannot reach the target. Stop region-count-only variants. A useful proof must charge how one fixed transition graph realizes cross-anchor contexts and continuation supports, using C-281 compatible-product soundness while handling C-130/C-132/C-145 counterexamples. Full route-cap proof: research/C374_POLICY_COUNT_ROUTE_CANNOT_CROSS_LINEAR_2026-09-29.md.

## C-375 - Separate information from recurrent computation

An explicit N-bit table has deterministic communication complexity at most N/2+O(1) across any fixed two-party coordinate split, since the smaller block can be sent in full. Thus ordinary communication bits, when transferred linearly to q, cannot establish a superlinear state lower bound. This does not rule out direct state-capacity or rectangle-partition arguments with a different q relationship.

The seed channel itself is not the bottleneck: O(N) endpoint-selected singleton features can distinguish all tables. The resource left to explain is the coupled recurrent readout: the q state equations must turn those observations into the low/high separator, and the q-round unrolling uses at most q^2 paid AND occurrences. A route through standard formula/BP lower bounds still needs a compiler preserving the relevant q or SCC parameter; none is currently available. The live alternatives are a direct lower bound for this registered monotone decoder or a full-promise N^(1+o(1)) implementation. Actual q remains N-o(N); no P-vs-NP proof. Full audit: research/C375_COMMUNICATION_INFORMATION_CEILING_AND_REGISTER_WORK_PIVOT_2026-09-29.md.

## C-376 - The native proof is a paired mismatch game, but mismatch forgets the promise

Given low w and high z, a valid C-319 cover supplies a live root. At each live state, z falsifies at least one side obligation; follow that side and choose a witness true on w. A literal witness immediately reveals a coordinate where w and z differ. A predecessor witness remains inactive on z and has smaller first-activation rank on w. This gives a terminating interaction on the cover's q state labels. It is a useful exact view of state reuse across two tables.

The interaction's terminal task is just finding any differing coordinate. A scan through the N coordinates uses N+1 states for all unequal pairs, whether or not either table has a small circuit. Thus a state-capacity argument must retain more than the low/high mismatch relation. It must encode a coherent low-circuit description or another decision-specific resource, and it must prove that every valid cover induces that resource. The standard hazard-free Karchmer-Wigderson theorem is formula-specific and requires exact three-valued behavior; native support activation gives only safe 1-certificates. No q improvement; actual bound remains N-o(N). Full proof: research/C376_NATIVE_CLOSURE_INDUCES_A_KW_DISCREPANCY_GAME_BUT_NOT_A_SUPERLINEAR_BOUND_2026-09-29.md.
## C-377 - Positional strategy is coherent within one input, but is not a circuit witness

Reachability-game positional determinacy gives one fixed existential action for each state-side pair on a low table. This is stronger than following a pairwise mismatch path: the same policy works against every universal play. The selected seed literals define a safe coordinate cube, so the policy fixes at least N-o(N) table bits. This only recovers q>=N/2-o(N), and the policy may vary with the input or simply record raw bits. The unresolved object is how one fixed transition graph organizes these per-input global policies across different low circuits; policy counting is too coarse. Seek a C-281 cross-anchor reuse theorem or a full-promise near-linear cover. No q improvement; actual bound remains N-o(N). Full proof: research/C377_POSITIONAL_POLICY_NORMAL_FORM_AND_DESCRIPTION_GAP_2026-09-29.md.
## C-378 - Policy splicing needs a well-founded hybrid

Per-input positional policies provide global action tables, but choosing actions from different tables is safe only when the resulting reachable state-side choices are legal and the predecessor graph is acyclic. In that case the seed literals prove a sound cube by backward induction. A hybrid can instead create a seedless cycle even when both source policies individually win; the least fixed point rejects it. This is why C-281-compatible support union alone is not enough. A state-sensitive synchronization theorem must count cross-anchor policy reuse and control hybrid well-foundedness together, with C-141/C-142 as rank-reversal calibrations. No q improvement; see research/C378_ACYCLIC_POLICY_HYBRIDS_AND_CYCLE_OBSTRUCTION_2026-09-29.md.
## C-379 - Code distance forces policy diversity, but not state growth

The far-apart Reed-Muller low family from C-372 has minimum distance larger than h=log|SIZE(s2)|. Each C-377 positional policy cube leaves at most h coordinates free, so a fixed root-policy pair can cover at most one codeword. A complete cover must realize |F| distinct root-policy pairs, with at least |F|/q in some root class. However one q-state graph has q(q+2N+1)^(2q) possible action tables, so the resulting q lower bound is still o(N). The conclusion is useful only as a calibration: policy diversity is real, but a count does not charge the graph's state reuse. Continue to O-226's valid acyclic-hybrid closure theorem. Full proof: research/C379_REED_MULLER_POLICY_CUBE_DIVERSITY_2026-09-29.md.

## Policy paths do not automatically hit robust splice regions (C-380/C-381)

For a fixed C-319 root, two positional winning policies can be extended and connected by a path of at most 2q one-action switches that remains acyclic. A consistent intermediate policy defines a safe cube, but some hybrids may select opposing literals.

Pair C-380 with C-320: after choosing one root/policy for each low table, there are at most |F|^2(2q+1) path masks. When log|F|=o(N), this is 2^(o(N)) for polynomial q. Yet the radius-r owner-mask ball has size 2^(o(N)) among 2^N splits, and almost every split is C-320-robust. A random robust split therefore avoids every selected path mask and its complement. This is a formal reason that representative policy paths cannot force the splice; it does not rule out the full endpoint-realizable policy/continuation family.

The next model object is the state-constrained image of *all* compatible same-root policies under the owner-mask map. Counting all action tables costs 2^(O(q log N)) and is already too coarse when q is linear. A useful theorem must exploit endpoint incidence, or the construction branch must supply an explicit global-description/address channel.

The quantitative target for a split-independent forcing argument is sharp at the entropy scale: radius-r balls occupy at most 2^(-N+N H_2(r/N)+O(1)) of the split space. Thus a mask family must have at least 2^(N-N H_2(r/N)-O(1)) members to hit every robust split. At r=Theta(N^gamma/n), this is 2^(N-O(N^gamma)); one policy per low anchor supplies only 2^(o(N)) masks.

There is a stronger semantic distinction. A consistent acyclic hybrid of complete positional policies is itself a winning policy, so its splice is safe by soundness. C-320's forbidden balls can only expose a product assembled from partial context/proof pieces that is accepted without forming a globally well-founded policy. If owners on coordinates where two anchors agree are allowed to depend on the split, work on the disagreement set D: each fixed owner pattern has split probability at most 2^(-|D|+O(N^gamma)) of landing in a robust forbidden ball. This remains exponentially small for the C-320 code distance |D|=Omega(N).

# C-382 update: safe-product entropy is not the live invariant

C-382 upgrades C-381's random-split avoidance from one chosen winning policy per anchor to every C-281-compatible context/proof product. For a fixed anchor pair, the owner map on the disagreement set is injective, and compatibility makes each resulting splice a member of SIZE(s2). Therefore there are at most |SIZE(s2)|=2^(o(N)) such patterns per pair. A random robust split avoids the union of all these patterns. This closes the split-independent forcing branch.

There is also a semantic correction: a completion of a genuinely compatible C-281 product is low by soundness, so it cannot itself be the high splice. The contradiction must come from a q-sensitive theorem showing that a proposed graph cannot keep all required products compatible/sound, or from a different direct state lower bound. A random mask chosen independently of the endpoint-generated product family cannot do that work.

The active model question now concerns caller-context loss in the exact C-319 recurrence. One shared state has one activation predicate of the entire table; proof history does not supply an address, gate index, or private circuit-description register. A promising lower-bound invariant would distinguish continuation predicates demanded by different gate/address contexts and show that merging them causes an unsound high completion. It must still allow the linear parity/equality and blockwise-cylinder calibrations. No such distinguishability theorem is proved. The counter-route remains an explicit near-linear full-promise cover with one coherent circuit description across all address checks.

# C-383 update: caller labels must become a work lower bound

C-383 audits the proposed caller-context direction. The low class has only 2^(O(N^beta)) members, so injecting low tables into residual labels cannot demand more than o(N) label bits. The q-state system can realize q(2N+q+1)^(2q) positional policies, and communication on N-bit inputs is at most linear. At q=Theta(N), the 2q seed predicates already have capacity for the full input table. These facts do not rule out a stronger structural theorem, but they rule out raw profile, policy, or communication counts as the missing charge.

The exact open object is now the computational cost of the C-319 least-fixed-point readout. Its standard compiler uses q^2 paid AND gates, so an OPS-specific lower bound above N^(2+2epsilon) in that measure would imply q>N^(1+epsilon); alternatively, prove q directly. The readout theorem must be induced by arbitrary valid covers and cannot assume an extracted circuit witness or caller/address register. The near-linear full-promise cover remains the opposite branch. No breakthrough is claimed.

C-383 also kills a tempting address-multiplexing count. The recurrence has 2q predecessor sets over q states (O(q^2) bits) and 2q seed clauses over N addresses (O(qN) bits). At q=Theta(N), its static description has O(N^2) bit capacity, sufficient to store all sN entries of a gate-by-address matrix for OPS s=o(N). Static storage does not imply an operational verifier: endpoints restrict the allowable transition incidences, and a state cannot receive its caller context as an extra input. The missing theorem must lower-bound semantic access and coherent use of the encoded data.

## C-384 model update: representation dependence versus joint continuation

A fixed description collapses the verification task to N table literals: `w=tt(C)` iff every coordinate equals the constant `C(x)`. Its native separator is O(N), matching the known N-o(N) floor. Thus the apparent `gate x address` workload is not a function invariant. The transformation `C_f -> C_f AND (H OR NOT H)` leaves the table unchanged while inserting a gate whose forced OR witness follows H(x). Any selector-hard family must therefore be robust across every small representation of each table, or be extracted from the native cover itself.

The real quantifier is `exists one C, for every x`. Per-address descriptions make the property vacuous. In the C-319 game a positional policy can commit one global action at a shared gate, but that action is not a readable register for a later state, and the shared state forgets its caller address. Supports record proof provenance but do not restore this control channel. The open object is a joint-description/address continuation theorem: either show every sound q-state graph needs a superlinear number of such continuations, or exhibit an endpoint-valid graph that maintains coherence with q=N^(1+o(1)).

C-281/C-320 must be used in the right order: a genuinely compatible support product is safe by soundness; a high owner pattern must be forced before the robust-splice lemma can contradict anything. Current q remains N-o(N). C-384 is a route correction, not a breakthrough.

**Novelty correction:** the selector-representation obstruction here was already proved in C-349, and the activation-code/search gap was already isolated in C-342/C-367. C-384 adds only the fixed-singleton linear bracket; it is a synthesis, not a breakthrough. The next phase should continue from the activation-code readout question and avoid re-running matrix-padding arguments.
