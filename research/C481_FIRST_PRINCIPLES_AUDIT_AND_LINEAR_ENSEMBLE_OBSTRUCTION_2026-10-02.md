# C-481 - First-principles audit and a linear-ensemble obstruction

Date: 2 October 2026  
Status: proved diagnostic lemma and project-wide route audit; no frontier change.

## Exact problem and quantitative target

Let N=2^n, s1=floor(N^beta/(10n)), and s2=N^beta. Write L_t for the set of n-variable truth tables with ordinary fan-in-two AND/OR/NOT circuit size at most t. A valid total separator F has

    L_s1 subseteq F^-1(1) subseteq L_s2.

Its labels inside L_s2 minus L_s1 are unconstrained. The requested magnification route seeks one fixed epsilon>0 such that, for every sufficiently small fixed beta>0, every such separator needs more than N^(1+epsilon) total gates. OPS Theorem 1.4 says this would imply NP is not in P/poly. Gates are paid; fan-out, wires, and description bits are not gates.

The direct optimization target is therefore the minimum total-gate size over every Boolean extension of this codebook sandwich. It is not the complexity of one preferred membership test. No proof here changes that target.

## Project-wide diagnosis from the accumulated attempts

The durable record now covers support and cylinders, entropy and counting, local constraints, robust Hamming geometry, Fourier and algebraic tests, anchors and block restrictions, sketches and fibers, certificates and anti-checkers, formula unfolding, gate-path/rectangle views, proof interpolation, average-case formulations, and promise-preserving source maps.

The strongest direct theorem remains C-403: every separator depends on at least N-O(N^beta log N) table bits and hence uses at least N-O(N^beta log N)-1 gates. C-406 adds a logarithmic reconvergence surplus over essential inputs, but this does not overcome the N^beta log N support slack. The repeated obstruction is precise: the methods force a lot of information to matter, but do not prove that a shared ordinary DAG must spend superlinear total gates to combine it.

The source-map branch has a clean standard composition test: if E has J gates and maps source YES to L_s1 and source NO to {T: CC(T)>s2}, then F composed with E computes the source label with at most J+CC(F)+B gates, where B is the fully charged postprocessing. No accumulated construction leaves the required hard-source margin after proving both endpoints and paying J and B. The paired complete upper remains exact Low-description enumeration at O(N*2^(O(N^beta))) gates. No near-linear full-promise separator has been constructed.

These are route diagnoses, not impossibility theorems. OPS's requested lower bound is itself strong: it implies NP is not in P/poly. We should expect a genuinely new lower-bound ingredient or endpoint-correct reduction, rather than infer that one elementary missing lemma is imminent.

## New proved diagnostic: low-dimensional linear YES ensembles have cheap parity distinguishers

**Lemma.** Let C be an affine subspace of {0,1}^N of dimension d<N. There is a nonzero parity check supported on at most d+1 coordinates that is constant on C. Consequently, an ordinary fan-in-two circuit with O(d+1) gates accepts every member of C and accepts exactly half of a uniform table.

**Proof.** Write C=a+Im(G), where G is an N-by-d binary generator matrix. Any d+1 rows of G are linearly dependent. Choose nonzero coefficients lambda supported on those rows with G^T lambda=0. Then lambda dot (a+Gz)=lambda dot a for every z. The parity of those at most d+1 coordinates is therefore fixed throughout C. Test whether it equals lambda dot a. A parity of w bits has an AND/OR/NOT implementation using O(w) gates. Since lambda is nonzero, the same parity is balanced on a uniform N-bit table, so the test accepts exactly half of all tables. The affine translate changes only the tested constant.

This is a diagnostic for a chosen YES distribution, not a separator for the full promise: the test need not accept Low tables outside C and accepts many High tables.

### Application to the C-480 polynomial-trace ensemble

For addresses x in GF(2^n), consider tables T_P(x)=Tr(P(x)) where P has degree less than k and coefficients are uniform in GF(2^n). The map from the kn coefficient bits to the N output bits is linear over GF(2), so its image is a linear subspace of dimension d<=kn. Horner evaluation with fixed-basis field arithmetic gives each table an ordinary circuit of O(kn^2) gates. Taking k<=s1/(C n^2) for a sufficiently large implementation constant C puts the whole family inside L_s1 and gives d<=kn=O(s1/n).

The lemma supplies a parity distinguisher of O(kn)=O(s1/n) gates: it accepts every trace table and half of uniform tables. The family is k-wise independent at distinct addresses, but that property does not prevent a parity check on at most kn+1 coordinates. Thus this ensemble is unsuitable as a pseudorandom hard-YES distribution against circuits at the target scale. This explains a concrete failure mode in C-480; it does not refute other distributions or the all-extension lower-bound program.

More generally, any proposed affine/linear family of Low tables with dimension d substantially below N is immediately vulnerable to an O(d)-gate parity test. Full affine span is only a necessary screening condition for this particular route, not evidence of circuit pseudorandomness.

Full affine span is not sufficient either. Let A_r be all tables of Hamming weight at most r, where r=floor(s1/(C n)) for a sufficiently large constant C. Every member has a minterm DNF of O(rn) gates and is therefore Low. A_r contains 0^N and every unit vector, so its affine span is all of {0,1}^N. Yet an O(N)-gate population-count threshold accepts every member of A_r: a carry-save tree reduces the N one-bit summands with O(N) constant-size full adders, followed by an O(log N)-size comparison with r. A uniformly random table passes with probability at most 2^(-N+O(r log(N/r)))=2^(-N+o(N)). Thus even full affine span and near-perfect distinguishability from uniform do not imply hardness; this is a structured Low subfamily recognizer, not a full separator.

The test is nonuniform: its support and parity constant are hardwired. It uses O(d) gates and O(d) selected input connections; describing or finding the check is a separate resource. This matches the target circuit model, where wires and description bits are not gates. It is an existence statement, not a uniform preprocessing algorithm for the ensemble.

### Exact distributional target that a replacement ensemble would need

For any separator F, circuit counting gives

    Pr_U[F(U)=1] <= |L_s2|/2^N <= 2^(-N+O(N^beta log N))

for uniform U, since every accepted table lies in L_s2. If D is any distribution supported entirely on L_s1, then Pr_D[F(D)=1]=1. Therefore every valid separator distinguishes D from uniform with advantage 1-o(1). A sufficient distributional route to the OPS lower bound would be a family D_beta supported on L_s1 that no N^(1+epsilon)-gate circuit distinguishes from uniform, with the same fixed epsilon for every sufficiently small fixed beta.

This is a precise target, but not a shortcut or an established result. It is stronger than simply choosing a random low circuit, and the C-480 trace distribution fails it by the parity check above. Existing local-PRG MCSP lower bounds address restricted circuit models; they do not supply this unrestricted-circuit security statement.

## Counterconstruction checks and scope

- **Parity:** a parity of any selected table coordinates has a linear-size shared ordinary circuit. It defeats charges based on the number of relevant coordinates alone.
- **Repeated-block equality:** block equality is a linear subspace with constant-size parity checks between repeated coordinates; the complete equality detector uses O(N) gates.
- **Sparse parity-check constraints:** each check is a parity circuit, and all checks can be ANDed for O(I+q) gates when I is total incidence and q is the number of checks. Check count alone does not price shared computation.
- **Simple global block relations:** copy/XOR constructions have O(I+q) shared implementations when their total relation size is O(N). Nonlinear block families still need an explicit full-gate analysis; the linear lemma does not cover them.
- **Full-span sparse Low family:** all weight-at-most-r tables have full affine span, but a weight threshold recognizes the family with O(N) gates and separates it from uniform. This directly shows why affine-span screening is weak.

Each example defeats only a generic incidence, independence, or linear-ensemble charge. None is a separator for all Low tables and all High tables, so none is a counterexample to the OPS lower-bound target.

## Why pairwise disagreement alone cannot be the missing charge

For any separator F, the Karchmer-Wigderson pair relation consists of pairs (x,y) with x in L_s1, CC(y)>s2, and F(x)=1,F(y)=0; an output coordinate i must satisfy x_i!=y_i. If an abstraction remembers only this required relation, it has an O(N)-state scan protocol: test coordinates in order, advance when the two bits agree, and output the first coordinate where they differ. This protocol works for every disjoint pair of endpoint sets.

Therefore a superlinear proof cannot use only the fact that every Low/High pair differs somewhere, nor only a generic cover of the pair relation. Any useful circuit-state argument must preserve additional one-sided gate semantics and show how those semantics interact with shared intermediate gates. C-476's rectangle DAG records such gate states, but its area potential does not charge reuse; C-477 closes the tested Korten mirror initializations. Neither result rules out a different potential.

## What the next proof attempt must contain

The audit narrows the live work to two mathematically distinct paths:

1. **Direct extension lower bound.** Define a quantity on the actual total AND/OR/NOT DAG, prove its change under every gate with unrestricted fan-out, and force a superlinear value using both promise endpoints and completeness for every table in L_s1. It may not assume a reconstructed circuit, witness enumeration, address-by-address checking, caller history, or a chosen algorithm. A pairwise relation statistic or a renamed non-shareability principle is not enough.
2. **Promise-saturated source map.** Give a concrete multi-output map E, prove every source YES maps to CC<=s1 and every source NO maps to CC>s2, and prove the source circuit lower bound exceeds the complete generator and postprocessing cost by N^(1+epsilon). The composition must be literal and all gates must be counted.

Pair either path with the actual complete-separator upper attempt. Preserve the exact enumerator as the baseline and do not call an incomplete sound recognizer a separator. For the direct route, use parity, repeated blocks, sparse checks, and global block relations as hostile tests. For a distribution route, first rule out a cheap support test such as the parity-check lemma above. If pursuing the route further, state the exact D_beta-versus-uniform distinguishing bound; k-wise independence or large seed entropy alone is insufficient.

## Literature and novelty check

The threshold and quantifier statement is OPS Theorem 1.4; it is a sufficient route to NP not in P/poly, not an equivalence with P != NP. Rao's spread-matching theorem is specifically a monotone lower bound for bipartite perfect matching and relies on matching-specific witness/distribution structure; C-480 did not transfer that structure to the signed-rail codebook promise. The locality barrier of Chen, Hirahara, Oliveira, Pich, Rajgopal, and Santhanam limits specified hardness-magnification techniques; it is not a universal impossibility theorem. Work on local PRGs for MCSP already studies output truth tables whose generated functions have small circuits, so local generation by itself is not a new source of hardness.

The affine-subspace lemma above is elementary linear algebra. Its project-specific value is to give a proof-level reason to retire the C-480 trace ensemble as a hard distinguisher candidate. No novelty claim is made for the lemma.

Primary sources: [Oliveira, Pich, and Santhanam, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf); [Rao, ECCC TR26-129](https://eccc.weizmann.ac.il/report/2026/129/); [Chen et al., ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/); [Cheraghchi et al., ECCC TR19-022](https://eccc.weizmann.ac.il/report/2019/022/).

## Exact frontier after C-481

**Strongest proved statement:** the affine-subspace parity-check lemma and its application to the polynomial-trace family. This retires that family only as a pseudorandom distinguisher candidate; it does not lower-bound a full separator.

**No quantitative frontier change:** ordinary total gates remain at least N-O(N^beta log N)-1, with C-406's additive logarithmic reconvergence refinement. The fixed-epsilon OPS N^(1+epsilon) target remains open. The exact full-promise upper remains O(N*2^(O(N^beta))); no near-linear full-promise construction was found. The separately reviewed native target rho_GapMCSP>=N-o(N) is unchanged. No P-vs-NP proof follows.
