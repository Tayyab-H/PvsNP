# Frontier reassessment — 25 September 2026

## Reconstructed state

The project has accumulated three different kinds of work; they should not be conflated.

1. **Main unrestricted route:** Gap-MCSP hardness magnification. The promise is on \(N=2^n\)-bit truth tables, with YES circuit size at most \(2^{\beta n}/(cn)\) and NO circuit size greater than \(2^{\beta n}\). OPS show that a slightly superlinear circuit lower bound in the specified range implies \(\mathrm{NP}\not\subseteq\mathrm{P/poly}\), hence \(\mathrm P\ne\mathrm{NP}\).
2. **Project fusion route:** represent the promise classifier on \(\Gamma=Y\sqcup Z\) using the \(2N\) literal slices. Cavalar–Oliveira's fusion theorem gives \(\rho\le D_\cap\le\rho^2\), with \(\rho\) exactly the cyclic intersection complexity. The project has a per-side coordinate/leaf proof and a cross-anchor sharing counterexample; all previously tested measure families or canonical filters have short covers.
3. **Alternative explorations:** fixed-clock Kolmogorov targets, source-hiding reductions, one-way-function ideas, proof complexity, and liar-style diagonalization. The latest durable notes identify their blockers: selector degree versus its own clock, source plus random-tape descriptions, proof formalization, or formula-size fixed points. None currently has an end-to-end theorem closer than the direct circuit target.

The Hamming-ball threshold result is a valid no-go for that chosen dual support, not a general semi-filter theorem. Its argument is already subsumed by earlier measure-family cover results in the project record; it is not new P-vs-NP progress.

## Minimum dependency path

```text
OPEN: Gap-MCSP has no circuit family of size N^(1+epsilon)
  -- OPS Theorem 1.4, for every sufficiently small fixed beta -->
NP is not in P/poly
  -- P is contained in P/poly -->
P is not NP
```

Use the published non-membership quantifier exactly. For each fixed \(\beta\), \(\notin\mathrm{Circuit}[N^{1+\epsilon}]\) means there is no circuit family meeting the bound; under the ordinary asymptotic convention the obstruction occurs infinitely often. Do not silently strengthen it to “all sufficiently large lengths.” Constants from a fixed-basis to De Morgan simulation are absorbed by taking exponent slack.

The literal-slice discrete complexity \(D(Y\mid\mathcal B)\) captures this acyclic promise-circuit question. The ρ route is a stronger sufficient subroute: proving \(\rho>N^{1+\epsilon}\) would suffice, but magnification does not demand cyclic lower bounds.

## Complement-side attack: failed symmetric count, corrected interpolation bound

The known low-anchor trace gives \(\rho(Y,\mathcal B)\ge N-\log_2 M_2-1=N-o(N)\). I tried to repeat the count with target \(Z\), claiming that an empty-intersection subcube contains no low table and therefore has size at most \(M_1\). This is false: the subcube may contain gap and high tables. The resulting \(\rho(Z)\ge N-\log M_1-1\) and \(D\ge2N-o(N)\) claims are withdrawn.

A valid but weaker bound comes from interpolation. If the high-anchor trace fixes \(q\) coordinates, any pattern on those positions can be extended to a Boolean function using a DNF of size \(O(qn)\). For \(q\le s_1/(C n)\), this is a low-circuit table in the same subcube, contradicting that the subcube avoids \(Y\). Thus \(q=\Omega(s_1/n)\), giving \(\rho(Z,\mathcal B)=\Omega(N^\beta/n^2)\). Literal-complement duality adds this to the OR-side complexity, but the term is sublinear and does not improve the leading \(N-o(N)\) lower bound. See corrected ledger item C-13.

**Reusable lesson.** “No point from the sparse set lies in a subcube” does not upper-bound the subcube's cardinality. Counting can bound the size of a cube only when every point in it belongs to the counted class; for the low-side proof the counted class is all tables below \(s_2\), but for the attempted high-side proof the cube can be populated by gap/high tables.

## Adversarial audit of the bottleneck

- **Quantified class:** all fixed-basis nonuniform Boolean circuits, not a solver architecture.
- **Representation:** every such circuit has a constant-factor De Morgan simulation. On \(\Gamma\), its input literals are exactly the project generators. Thus a circuit that ignores a favored filter family is still represented by \(D\); no hidden solver-behavior premise is needed for the direct target.
- **Current cover limitation:** \(\rho\) ranges over arbitrary endpoint subsets and so already handles nonlocal choices, sharing, and advice in its exact cyclic model. The failed step is mathematical size, not a missing representation bridge.
- **Circularity:** O-1 itself is the needed strong Gap-MCSP circuit lower bound. It implies a major separation but is not known to follow from \(\mathrm P\ne\mathrm{NP}\); do not dress it up as an independent lemma.
- **Locality:** OPS's theorem constructs anti-checkers from the assumption \(\mathrm{NP}\subseteq\mathrm{P/poly}\). Chen et al. identify a locality barrier: magnified problems may admit small circuits augmented with local oracle gates, and several weak lower-bound methods extend to those gates. This blocks direct adaptations of those methods, not every conceivable proof.

## Fundamentally different attacks on O-1

| Attack | New object | Why it could apply to arbitrary algorithms | First theorem to prove | Main adversarial failure mode | Status |
|---|---|---|---|---|---|
| Acyclic AND/OR potential | A semantic potential on the complete circuit DAG, including both union and intersection structure | It lower-bounds the represented function itself, so sharing and negation are included by the De Morgan conversion | A superlinear lower bound on \(D(Y\mid\mathcal B)\), with exponent slack | The low-side coordinate trace tops out at N; the corrected opposite-side interpolation is only sublinear | Primary; no candidate invariant found |
| Anti-checker selector | The circuit that, from a hard truth table, emits inputs hitting every smaller circuit | OPS already constructs this object under the negation of the desired separation | A target-specific lower bound on selector size that transfers to the separator | The selector lower bound can be equivalent to O-1 in disguise; locality oracles may trivialize known techniques | Active as a bridge audit, not yet independent progress |
| Feasible proof witnesses | A bounded-arithmetic proof that a uniform function finds counterexamples to wrong SAT circuits | The statement quantifies semantically over arbitrary circuit descriptions; the proof system provides a logic-level transfer | Verify the exact Pich–Santhanam condition and prove a sufficient EF non-p-boundedness statement | Standard-model search under \(\mathrm P=\mathrm{NP}\) does not give the required \(S^1_2\) proof; the EF premise is major | Conditional alternative |
| Time-slice communication | Information crossing cuts in an arbitrary polynomial computation or its circuit | A simulation theorem could extract a protocol from every circuit, regardless of representation | A size-\(S\) separator-to-protocol theorem with a Gap-MCSP protocol lower bound | Truth-table block cuts may have large boundaries or permit massive sharing; without lossless simulation this is only a restricted model | Speculative; test immediately |
| Self-referential NP diagonal | A verifier that embeds a clocked solver's behavior while retaining polynomial certificate checking | It attacks the solver's semantic answer rather than its gates | A size-controlled fixed point whose ordinary SAT instance is polynomially verifiable | Full tableau grows superlinearly; the constant-size anti-answer map has a 2-cycle, not a fixed point | Current versions falsified |
| Fixed-clock incompressibility | A coNP language of strings with high time-bounded Kolmogorov complexity | If \(\mathrm P=\mathrm{NP}\), decision gives a polynomial selector for accepted strings | A selector or batched search below the defining clock, or a different fixed NP verifier handling every polynomial degree | The selector may have degree \(q\) or higher; existential search cannot force it below its own clock | Clock gap remains open |

## Route choice

Prioritize the direct acyclic target because it is exactly the missing premise and has no extra representation assumption. Continue the cover route only when a proposed lemma improves the bound on \(D\), rather than merely elaborating a selected family of semi-filters. The anti-checker route is the next most promising transfer to inspect because it is the actual mechanism inside magnification, but accept it only if its new lemma does not simply restate the separator lower bound.

The claimed \(2N-o(N)\) result has been withdrawn. The corrected high-anchor interpolation lemma is recorded as C-13; it does not improve the leading \(N-o(N)\) circuit lower bound. No candidate proof or separation has been obtained.

## Sources checked

- Oliveira, Pich, and Santhanam, [Hardness Magnification Near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and the anti-checker construction.
- Cavalar and Oliveira, [Boolean Circuit Complexity and Two-Dimensional Cover Problems](https://arxiv.org/abs/2503.14117), Definitions of \(D_\cap\), fusion bounds, and cyclic characterization.
- Chen et al., [Beyond Natural Proofs: Hardness Magnification and Locality](https://arxiv.org/abs/1911.08297), the locality barrier.
- Pich and Santhanam, [Towards P\(\ne\)NP from Extended Frege Lower Bounds](https://arxiv.org/abs/2312.08163), exact feasible-witnessing conditions.

## Adaptive anti-checker selector: exact next object

Let $N=2^n$, $s_2=2^{\beta n}$, $s_1=s_2/(10n)$, and $t=2^{10\beta n}$. OPS Lemma 4.1 constructs, under $NP\subseteq Circuit[poly]$, a circuit $A_{n,\beta}$ of size $N^{1+O(\beta)}$ which reads the full truth table $f$ and outputs $t$ query points. For every $f$ with $CC(f)>s_2$, every circuit $D$ of size at most $s_1$ disagrees with $f$ on at least one output point. The theorem then feeds those labeled points into a succinct-MCSP decider obtained from the same circuit assumption.

A direct counting attack rules out only nonadaptive samples. Fix any $Q$ with $|Q|\le t$. There are $2^{N-|Q|}$ functions zero on $Q$, while at most $2^{O(s_2\log(n+s_2))}=2^{O(n2^{\beta n})}$ functions have size at most $s_2$. When $\beta<1/10$, $t+n2^{\beta n}=o(N)$, so a high-complexity completion exists that is zero on all of $Q$. The constant-zero circuit passes the fixed sample. Thus the selector must use the truth-table contents to choose its addresses.

This is a useful narrowing, not a separation: it disposes of fixed-set arguments and exposes the genuine object as an adaptive near-linear circuit. A theorem ruling out all such selectors at the OPS exponents would suffice for $NP\not\subseteq P/poly$, but must quantify over arbitrary circuits and remain aligned with the unknown polynomial exponent in the $NP\subseteq Circuit[poly]$ assumption. No lower bound for the adaptive selector has been proved here. The named static Anti-Checker Hypothesis refuted by Chen et al. asks for a fixed family of $2^{(2-\epsilon)n}$ sets of size $2^{n^{1-\epsilon}}$ against functions above circuit size $2^{n^\lambda}$, with comparison circuits of size $2^{n^\lambda}/(10n)$. OPS Lemma 4.1 uses $s_2=2^{\beta n}$ and $t=2^{10\beta n}$ and computes a sample from the input. The selector's range can contain up to $2^{tn}$ sets; the known refutation of the smaller, differently parameterized family does not by itself bound this range.

C-17 gives a first range bound: $q\ge(1-o(1))N^{1-10\beta}$, by taking a high-complexity truth table zero on the union of all candidate coordinates. C-18 strengthens it using sparse hard truth tables: for all sufficiently small fixed $\beta$, $q\ge2^{\eta s_2/n}$. The proof bounds the probability that any fixed sample contains enough sparse positive points to be interpolated by a size-$s_1$ DNF, then unions over candidate samples and uses circuit counting to retain a hard support. For the named static Anti-Checker Hypothesis, $s=2^{n^\lambda}$ and $0<\lambda<1$ give sparse-support entropy $(1-o(1))ns$, which dominates the $O(sn^\lambda)=o(ns)$ circuit descriptions. The same argument therefore recovers its refutation for every fixed $\lambda$ in the published range, with the hypergeometric tail dominating the $2^{O(n)}$ candidate family.

These are range lower bounds, not selector circuit lower bounds. A selector's $tn$ output-address bits can encode $2^{\Theta(tn)}$ different samples by direct wiring, and $tn\gg s_2/n$ for OPS. C-19 extracts a further necessary condition: on each sparse hard table the sample must hit $\Omega(s_2/n^2)$ positive coordinates. A sorting network can output all positive coordinates of such a table in $O(Nn^3)$ size, so this positive-capture condition does not bound selector size. C-20 represents anti-checking as a table-conditioned transversal for all error sets of low circuits; the generic random-sample estimate is only $O(nN)$ and hence vacuous for the OPS target $t=s_2^{10}$. The unresolved computation is routing each hard input to a sample whose full label pattern defeats every small circuit. C-18 sharpens the adaptation constraint but is not O-1 progress.

## Sources added in this reset

- Lipton and Young, [Simple Strategies for Large Zero-Sum Games with Applications to Complexity Theory](https://www.cs.ucr.edu/~neal/Lipton94Simple.pdf), the minimax anti-checker theorem.
- Oliveira, Pich, and Santhanam, [Hardness Magnification Near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and constructive Anti-Checker Lemma 4.1.
- Pich and Santhanam, [Towards P != NP from Extended Frege Lower Bounds](https://arxiv.org/abs/2312.08163), feasible anti-checkers and EF conditions.
- Atserias and Müller, [Simple General Magnification of Circuit Lower Bounds](https://arxiv.org/abs/2503.24061), sparse distinguishers and the uniform MCSP route to $P\ne NP^{\oplus P}$.

## Follow-up adversarial check: simple low-density regions

C-24 tests a natural counterexample to C-23's fixed dense-circuit hitting set. If the sparse support lies inside an axis-aligned subcube of size at most the allowed sample length, random positives reveal the subcube as their coordinatewise hull with probability $1-o(1)$. Counting shows that almost every such support is globally above $s_2$ and that no size-$s_1$ circuit matches its full restriction to the subcube. Outputting the hull is therefore a valid anti-checker on this distribution, again in $O(Nn^3)$ circuit size.

This eliminates axis-aligned subcubes as a hard sparse family. Q10 should now target regions whose low-density structure is not exposed by coordinate hulls or similarly cheap canonical closure. The broad open node is unchanged: lower-bound selector size on all high-complexity tables.

## Addendum — relative-density and affine-closure audit

C-25 tightens the known-region argument with the exact probabilistic requirements $M\eta^m=o(1)$, $M(1-\eta)^w=o(1)$, and $wm/a=o(1)$. A fixed region-relative sample then catches every candidate circuit with high probability for a random support in that region. This corrects the tempting but insufficient condition $m\ge(\ln M+1)/\ln(1/\eta)$, which only bounds one failure probability by a constant.

C-26 extends the recoverable-region subcase from axis-aligned subcubes to affine subspaces. Random positives span an affine $d$-flat except with probability at most $2^{d+1-w}$. Counting gives both high circuit complexity of the sparse table and the absence of a low circuit agreeing throughout the flat. The selector computes the affine hull and outputs all its points in $O(Nn^3)$ size.

**Research consequence.** Simple closure families are poor worst-case candidates. The open reduction is still absent: a selector might use a non-region-based sample, so hard recovery of a chosen region would not alone lower-bound all selectors. Continue only if the version-space transversal formulation yields a universal, quantitatively useful obstruction.
## Addendum — version-space transversal formulation

C-27 proves that sparse-support anti-checking is exactly a transversal problem over low-circuit false-positive extensions of the positive set. This makes the distinction between existence and synthesis precise: minimax proves a fractional transversal, and sampling yields a short integral one, but neither computes it from an arbitrary truth table in the required circuit size. Region-relative arguments (C-25) are one construction, not a universal form of every selector.

**Next target.** Prove a near-linear circuit upper or lower bound for transversal synthesis itself, with the full promise and OPS exponent dependence. Do not call the search NP-hard absent a reduction; do not claim a region-recovery lower bound from the failure of natural closure constructions.
## Addendum — majority-overlap stress test

C-28: hardness rules out a small subfamily of accepting circuits whose residual false-positive sets have no majority-overlap point, since their majority would compute the sparse table. But the family of all subsets of size greater than half a universe has a majority point in every subfamily and still needs a transversal of size about half the universe. The generic overlap-to-cover route is therefore insufficient; any continuation needs structure unique to circuit-induced extensions.
## Addendum — known-region size dichotomy

C-29 shows that, conditional on knowing A and assuming support entropy enough to make the sparse table high-complexity, every size regime has a near-linear selector: output A if it fits the list budget; otherwise use R plus a fixed region-relative hitting set. Thus any remaining region-based adversary has to hide A from the selector or defeat a different construction. This remains a distributional/known-A result and supplies no worst-case selector lower bound.
## Addendum — bounded-degree closure

C-30 uses the vanishing-ideal viewpoint: the degree-$d$ closure generated by positives is the set whose feature vectors lie in their span. For bounded-degree graphs, random positives span that space with high probability because the restricted evaluation code has constant relative distance. A near-linear circuit recovers and outputs the region. This is a broader observable-closure family, still only a structured promise result.
## Addenda — Hamming balls and hidden product spectra

C-31 shows that fixed-degree closure may return the entire cube for a low-circuit Hamming ball, but maximum positive weight recovers the radius. C-32 shows that secret linear coordinates of a product region are recovered by a Walsh transform, thresholded Fourier peaks, and the matroid of their minimal dependencies. Both are constructive anti-checker selectors for structured promise families. Neither constrains arbitrary selectors.
## Addendum — Fourier-matroid criterion

C-33 generalizes the explicit C-32 Fourier learner to any fixed block alphabet with a connected, spanning set of maximal nonzero Fourier frequencies. Such product regions remain easy under unknown linear coordinates. The remaining block-alphabet test is disconnected or nonspanning peaks; no universal selector lower bound follows from this audit.

## Reset after the full quantifier audit — 25 September 2026

The highest unresolved node remains O-1, not one of its structural descendants: a slightly superlinear lower bound against arbitrary nonuniform circuits for the exact OPS Gap-MCSP parameters. The theorem is already a major unrestricted lower-bound statement. Calling the missing step a “universal selector theorem” does not make it a technical bridge; OPS's selector construction is the mechanism showing how a hypothetical $NP\subseteq P/poly$ assumption would solve the gap problem.

A new adversarial-completion argument (C-34) proves that any valid selector depends on $N-o(N)$ truth-table bits. C-38's circuit-graph connectivity count sharpens the gate bound to $N-o(N)$ for fan-in-two circuits with $tn=o(N)$ output bits. This remains linear and stops at the same asymptotic scale as the project coordinate trace. The target is still superlinear **routing complexity**, beyond essential-input dependence and connectivity. No existing C-17/C-18 output-range count, C-19 positive-capture condition, or C-23--C-33 region-recovery method supplies this.

**Route choice.** Prioritize O-1 directly and use selector synthesis as its concrete proof interface. Do not continue adding structured support families unless they yield a theorem constraining every selector. The two alternative proof routes are the feasible-proof-complexity route (still requires the formal $S^1_2$ condition and an EF lower bound) and self-referential NP diagonalization (still lacks a polynomial-size tableau construction). Neither currently has a smaller open core.

**Recent literature check.** OPS Theorem 1.4 and Lemma 4.1 give the exact Gap-MCSP implication and conditional selector sizes. Goldberg, Juvekar, and Kabanets (June 2026) obtain conditional NP-hardness for implicit MCSP and full-support learning using subexponentially secure iO and the nonexistence of optimal proof systems; this does not prove the unconditional circuit lower bound O-1. See [their ECCC report](https://eccc.weizmann.ac.il/report/2026/091/download/). Pich and Santhanam's feasible proof-complexity route remains conditional on Extended Frege non-boundedness and exact bounded-arithmetic witnessing, as recorded in Q7.

## Further frontier update — conditional fibers and proof-claim audit

C-35 quantifies why uniform random tables do not expose the selector bottleneck: any fixed $t$-point sample anti-checks all size-$s_1$ circuits with probability $1-2^{-t+O(2^{\beta n})}$, while almost every table is above $s_2$. The worst-case work is concentrated in atypical cylinders with a low-circuit trace on the candidate sample.

C-36 rigorously eliminates one compact-summary route. If addresses factor through a rank-$k$ linear sketch with row-space distance greater than $t$, fixing any sketch value and setting its selected labels to zero leaves $2^{N-|Q|-k}$ completions. When this exceeds $M_2$, one completion is high complexity and defeats the selector via the constant-zero circuit. For OPS parameters this holds for $k=o(N)$, including $k\le tn$. Combined with C-38, the universal selector lower bound is now $N-o(N)$ gates. The general address-map condition is that every fiber paired with a low-circuit trace has at most $M_2$ members. Nonlinear label feedback remains the unresolved case; C-36/C-38 give no superlinear circuit lower bound.

C-37 audits the June 2026 pedigree-polytope P=NP claim. The public Lean repository assumes `QuickProtocol (LayeredPoint n)` and the MCF necessity direction as axioms, uses a `Unit` placeholder for the projected polytope, and axiomatizes parts of the membership-to-optimization-to-STSP chain. The verified theorem is therefore conditional on the missing algorithmic bridge; it is not an axiom-free formal resolution. The [Clay problem page](https://www.claymath.org/millennium/p-vs-np/) still lists P vs NP as unsolved. This route is closed as a claimed formal breakthrough unless the axioms are replaced by full proofs and the oracle/resource model is made concrete.

C-39 stress-tests the new $N-o(N)$ gate bound: a linear-size priority encoder finds first-one and first-zero positions, so the two constant circuits are anti-checked on every nonconstant table. This does not handle any nonconstant hypothesis class, but it shows that a selector can use nonlinear feedback between queried labels and address choices at linear cost. The unresolved lower bound must account for the simultaneous need to hit all $M_1$ small-circuit traces.

**Research decision.** Keep O-1 as the central mathematical target. Use fiber shrinkage and query-label feedback as the next concrete route, while treating C-37 as a proof-audit lesson: names like “Tardos algorithm” or “Lean-verified” do not discharge a theorem unless the exact complexity statement follows from explicit definitions and axiom-free derivations.

## Long-horizon methodology reset — dual-witness audit

The O-1 dependency was rechecked from the top. It is the first open statement on the magnification path and already quantifies over arbitrary nonuniform circuits; there is no unresolved representation-transfer lemma above it. The selector formulation is a proof interface for that same major lower bound, not a technical bridge that can be polished independently.

C-40 makes the constructive bottleneck precise. For a high-complexity table, finite minimax gives a distribution with constant disagreement against every size-$s$ circuit. A random support of $O(s\log(s+n))$ points is then a valid anti-checker. A rational fractional witness can be found with an NP separation oracle; sampling gives a randomized $\mathrm{FBPP}^{\mathrm{NP}}$ selector on promised high inputs. But a proposed list is valid only if no size-$s$ circuit matches it (a coNP predicate), and finding such a list is naturally a $\Sigma_2^P$ search relation. The statistic $\Delta_s(f)$ is zero exactly on size-$s$ circuit tables and bounded away from zero on the high side, so distinguishing its low and high promise cases merely reformulates Gap-MCSP. This is a sharper diagnosis, not a breakthrough.

**Adversarial check.** On most random tables a fixed sample already works; C-35. Its exceptional set is small as a fraction but exponentially large in absolute size. Any worst-case selector must route those tables to a sample with a non-realizable low-circuit trace. The minimax LP explains why one exists but does not identify it. No counting bound on output range or on the LP value forces superlinear gates.

C-41 extends that check from one fixed list to any fixed menu of $m=o(N/w)$ distributions: a sparse random support of weight $w=\Theta(N^\beta)$ can be both high circuit complexity and have $o(1)$ mass under every menu member. This proves genuine table dependence is necessary for the dual witness. It still does not constrain the selector's exponentially large input-dependent output range, so O-1 remains unchanged.

**Route choice.** Continue attacking the simultaneous routing problem directly at O-1. Keep dual-witness extraction as the concrete interface, but do not pursue the LP value as a new invariant. The next useful theorem would either (i) construct the exact list from $f$ without weighted circuit fitting or a $\Sigma_2$ search, or (ii) prove that every fan-in-two circuit implementing that map has superlinear size in OPS's exact quantifiers. The logic/EF and self-reference branches remain alternatives only if they produce a first lemma below O-1's difficulty.

**Fresh wacky-literature audit (C-42).** Isong's August 2026 Loop-theoretic manuscript defines internal archival complexity notions; its SSRN abstract explicitly conditions the classical conclusion on a finite-transition capacity principle and Loop-to-complexity bridge axioms. The source PDF returned 403 here, so exact axiom types remain unaudited. The immediate implication is methodological: any new language must prove a resource-preserving bridge to standard Turing machines before its internal lower bound bears on P vs NP. No new theorem for the active route was extracted.

## Final proof-path audit — 25 September 2026

**Strongest proved results.** The published OPS magnification implication from a slightly superlinear Gap-MCSP circuit lower bound to $NP\not\subseteq P/poly$; project proofs of only a linear $N-o(N)$ selector lower bound; C-40 short anti-checker existence by minimax and sampling; and C-43's source-verified conditional EF theorem. None is a P-vs-NP proof.

**First open node.** O-1 is the first unresolved node on the shortest established route: prove that the exact OPS Gap-MCSP promise has no size-$N^{1+\epsilon}$ arbitrary-circuit family. This is a major circuit lower bound itself, not a technical generalization. It is stronger than the desired uniform P-vs-NP separation through $NP\not\subseteq P/poly$, but the published magnification theorem makes it a direct route.

**Adversarial route checks.** (i) Direct selector construction: C-40 removes anti-checker existence as an obstacle, but finding a table-dependent transversal remains a $\Sigma_2$ search and the minimax LP's separation is weighted circuit fitting. (ii) P=NP/PH collapse: C-44 gives polynomial-time search and polynomial circuits with no controlled degree; by contraposition, OPS already provides the near-linear bound for an appropriate small-$\beta$ choice under $NP\subseteq P/poly$, so this does not circumvent O-1. (iii) Feasible proof complexity: C-43 requires an $S^1_2$-provable generator plus EF not p-bounded; KPT's existential variant has adaptive witnesses and no known polynomial flattening. (iv) Self-reference/diagonalization: no construction was found that encodes an arbitrary polynomial-time solver's self-simulation in an NP instance without a tableau-size/exponent blowup. (v) New internal languages: C-42's abstract makes the classical implication conditional on capacity and bridge axioms; no standard-model resource-preserving bridge was verified.

**Classification.** O-1: OPEN, arbitrary circuits, known-hard lower bound in disguise rather than a tractable bridge. C-43: PROVED conditional implication; its generator and EF premises are OPEN. C-44: PROVED conditional search lemma; not a lower bound and quantitatively weaker than OPS. Self-reference: current route FAILED at preserving NP with a uniform polynomial exponent, not disproved in general. Loop-theoretic route: CONDITIONAL / full text unaudited.

**Choice.** Keep O-1 primary and attack the nonlinear input-dependent routing cost directly. Retain the feasible-antichecker route only for a concrete witness-independent KPT composition or a route to EF non-p-boundedness. Every future candidate must state the new fact that forces an arbitrary algorithm/circuit and show the resource exponent; quantifier collapse or per-table existence is insufficient.

## Version-space attack — 25 September 2026 (C-45)

The anti-checker is exactly a transversal of the circuit disagreement sets $E_D(f)$. The residual family after querying $Q$ is $V_f(Q)=\{D:E_D(f)\cap Q=\emptyset\}$. This makes the minimax result operationally sharper: every residual circuit has $\mu_f$-mass at least $\gamma$ on its error set, so a short random sample kills all residual circuits. A naive deterministic loop finds one survivor and one mismatch, but only proves a $2^{O(s\log s)}$ iteration bound.

**Adversarial test.** An abstract family $E_i=H\cup\{p_i\}$ has a one-point hitting set yet an oracle that returns the private $p_i$ can force $m$ single-counterexample rounds. This establishes only that an arbitrary survivor oracle is not enough for the naive loop. It says nothing negative about algorithms that exploit the explicit circuit representation.

**New target.** The combinatorial contraction is now proved: a margin distribution ensures some query removes a constant fraction of every current residual version space. C-47 shows exact #P counts can find that query, with near-linear-in-$N$ oracle-call count at small fixed $\beta$. The remaining task is to replace those counts by ordinary circuits of size $N^{1+\epsilon}$ or prove no such replacement exists. Neither #P necessity nor a circuit lower bound has been established. O-1 remains the first unresolved theorem on the path to separation.

**Learning-theory literature check (C-46).** Compton et al.'s one-point greedy lower bound is $\Omega(\log|\mathcal C|)$, which matches C-45's $O(\log|\mathcal C_s|)$ ideal query count under constant margin. So it does not challenge the balanced-contraction existence proof. The paper studies a different target/class problem and says nothing about computing a constant-fraction error point for circuit hypotheses. The missing piece remains computational extraction, not combinatorial list length.

**Constructive oracle result (C-47).** The contraction point can be found by #P queries: count the surviving descriptions $Z_Q$ and, for each input $x$, the survivors disagreeing at $x$, $G_{Q,x}$. The dual margin proves $\max_xG_{Q,x}\ge\gamma Z_Q$, so a maximizing sequence outputs a valid list in $O(\gamma^{-1}s\log(s+n))$ rounds and uses $O(Ns\log(s+n))$ #P calls. This is a genuine algorithmic sharpening of the existence proof, but it is only in $\mathrm{FP}^{\#P}$ and does not give ordinary circuits or a separation. It narrows the next target to a near-linear circuit implementation/surrogate for the contraction score, or a lower bound ruling one out.

## Reset and conditional score reconstruction — 25 September 2026

**C-48.** A constant-factor relative approximation to each residual score $G_{Q,x}$ is enough: selecting the largest estimate still contracts the survivor count by a constant factor. The score is #P on the current transcript. Stockmeyer's approximate-counting procedure places its approximation in BPP$^{NP}$. Under $NP\subseteq P/poly$, the approximation has deterministic polynomial-size circuits on the transcript input length after amplification and nonuniform fixing of random bits. With $K=O(s\log(s+n))$ rounds and transcript length $O(Kn)=N^{\beta+o(1)}$, evaluating all $N$ scores per round and reading the chosen table bit yields an $N^{1+O(\beta)}$ selector. This reconstructs the known OPS conditional upper bound from C-45's potential; it is not an unconditional breakthrough.

**Important correction to the route diagnosis.** C-47's exact #P oracle is only one implementation. C-48 shows approximate counting is enough under the same nonuniform NP assumption already used in magnification. Therefore the unresolved theorem is not “prove approximate counts are hard” and no lower bound on this greedy computation would suffice without proving that every valid selector must use it. The highest open node remains O-1: a slightly-superlinear circuit lower bound for Gap-MCSP / its universal puncturing-certificate selector.

**Reset classification.** The direct selector target is unrestricted but is itself a major lower bound, not a technical bridge. The affine-fiber and simple-region routes constrain only restricted mechanisms; their failure to cover nonlinear selectors is not a proof gap that notation can fix. Self-reference still fails to provide a single NP verifier exponent, and the feasible proof-complexity route still needs both the formal generator condition and EF non-p-boundedness. The detailed dependency and route audit is in [`RESET_AUDIT_2026-09-25.md`](RESET_AUDIT_2026-09-25.md).

