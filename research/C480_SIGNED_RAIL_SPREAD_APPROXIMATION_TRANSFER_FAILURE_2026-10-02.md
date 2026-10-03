# C-480 - signed-rail spread approximation does not yet charge shared gates

Date: 2 October 2026  
Status: proof attempt, explicit obstruction, no frontier change.

## Question and proposed mechanism

Can the 2026 spread-matching method be adapted to the signed-rail monotone lift of an arbitrary Gap-MCSP separator, so its approximation argument charges ordinary AND/OR/NOT gates while preserving unrestricted DAG sharing?

For an ordinary separator F, C-451 constructs a monotone circuit G on rails x_i_plus and x_i_minus, with legal encoding e(T)=((T_i,1-T_i)) for i=1,...,N. It preserves correctness on every legal table and uses at most 2*CC(F) internal gates. Thus G accepts every e(T) for T in L_s1 and rejects every e(T) for which CC(T)>s2.

The candidate is a Rao-style gate approximation with explicit distributions. Let X be e(f_P) for a uniform low-degree polynomial trace table. Let Y be a partial signed assignment obtained by choosing a uniform truth table T, then independently retaining each of its N legal rails with probability gamma. Circuit counting makes T OPS-High with probability 1-o(1); on that event, monotonicity and Y subset e(T) force G(Y)=0. The distribution of Y is a product over N three-state blocks (blank, plus, minus), not independent Bernoulli inclusion of the 2N rails.

Set t<=k/2 so any union term of width at most 2t lies in the k-wise independence range. For each gate g, maintain A_g, a family of consistent signed terms of width at most t, and approximate g by f_Ag(z)=1 iff some term in A_g is contained in z. Define E_g as the union of X inputs where g=1 but f_Ag=0 and Y inputs where g=0 but f_Ag=1. Input gates use their singleton literal. At an OR gate use A_g=A_h1 union A_h2; this adds no new errors beyond E_h1 union E_h2. At an AND gate first form A'_g from all consistent unions S1 union S2 with S1 in A_h1 and S2 in A_h2. Let N_g=E_g minus (E_h1 union E_h2). For each X in N_g, choose a witness term Z(X) in A'_g contained in X; it has width at most 2t. Borrow Rao's greedy extraction: while N_g has positive X-mass, choose a largest partial assignment S for which Pr[S subset Z(X) | X in N_g] >= r^(-|S|). Add S to A_g if |S|<=t; if the largest such S is wider than t, stop and charge the remaining positive error using the YES-side spread bound. This is a concrete DAG gate recurrence; shared gates are processed once. In the usual Rao calculation, if |S|=w>t, an input-side bound Pr[S subset X]<= (2r)^(-w) and the greedy condition imply Pr[N_g]<=2^(-w). Here the polynomial-trace family supplies only Pr[S subset X]=2^(-w), so the same calculation gives only Pr[N_g]<= (r/2)^w, which is useless for the required r>2.

To make this imply a lower bound, one must prove both that the extracted witness distributions are r-spread strongly enough and that a product-space spread lemma makes f_Ag(Y)=1 with probability at least 1-zeta for each new AND error. If every gate contributes at most zeta error, a circuit with m internal gates has total error at most m*zeta by a union bound; choosing zeta=N^(-1-delta) would contradict correctness for m below N^(1+delta)/3. The spread lemma would require r on the order of log(t/zeta)/gamma. This would directly improve the ordinary gate lower bound if the two missing estimates held.
## Serious transfer attempt

Take a hard YES subfamily from traces of degree-(k-1) polynomials over GF(2^n): f_P(x)=Tr(P(x)). Horner evaluation with field operations gives each table a circuit of O(k*n^2) Boolean gates, so k can be chosen below the OPS YES budget by a polynomial-in-n factor. Uniform random coefficients give k-wise independent output bits at every k distinct addresses. For every consistent signed pattern S on at most k table coordinates,

    Pr[e(f_P) contains S] = 2^(-|S|).

Use uniform random tables for the NO-side calibration: circuit counting makes all but a 2^(-N+O(s2*log(N+s2))) fraction OPS-High. This gives a concrete, high-entropy Low ensemble and a nearly uniform High ensemble rather than assuming arbitrary Low tables behave randomly.

The standard approximation proof still does not close. Its selected short witness Z(T) is only known to satisfy Z(T) subset e(T). Conditioning on the event that the gate approximation is correct transfers the YES pattern bound only as

    Pr[S subset Z(T) | good] <= 2^(-|S|) / Pr[good]    for |S| <= k.

That certifies at best a constant spread parameter near 2, whereas the spread-set lemma needs a parameter growing with log(t/epsilon)/gamma for growing t. The obstruction appears at the AND gate too: choosing a witness subset with conditional probability at least r^(-w) and charging its mass against the 2^(-w) input bound gives (r/2)^w, not a small error. The proof has no reason that its witness term can be sparsified: deleting literals can make it stop witnessing acceptance. Switching to a sparse random restriction of a YES table is also invalid, because the separator is forced to accept the complete legal encoding only; monotonicity gives no lower bound on its value on a subset of that encoding. The signed-rail NO input is not an independent Bernoulli subset either. A product-space spread lemma might address that last distribution mismatch, but even granting one would not fix the missing YES-witness spread bound.

This is the decisive obstruction to this mechanism, not a proof that a different signed-slice method is impossible. The candidate would need a new theorem forcing every useful gate witness to have stronger spread than the low-table distribution itself, without assuming a particular separator algorithm. No such theorem was found.

## Counterconstructions and canaries

The zero table is the sharp small counterexample to any claim that dense legal encodings or wide terms alone imply superlinear computation: on signed rails, the monotone minterm AND_{i=1}^N x_i_minus accepts exactly the legal encoding of 0^N, costs N-1 AND gates, and rejects every other legal table. This is not a separator for the full OPS promise; it defeats only a generic density/term-width charge.

The C-451 canaries also survive this mechanism audit. Parity has an O(N)-gate ordinary circuit and an at-most-2x signed-rail lift; repeated-block equality costs O(N); sparse parity checks cost O(I+q) for incidence I and q checks; bounded-arity global block relations cost O(I+q). These rule out charges based only on global dependence, repeated structure, check count, or occurrence count. They are not full-promise separators and do not refute the OPS lower-bound target.

## Model, promise, and quantitative accounting

The target is total fan-in-two ordinary circuit size: AND, OR, and NOT internal gates are paid; wires, fan-out, and description bits are not gates. C-451's lift preserves DAG sharing and has at most twice the source internal-gate count. No unrolling is used. A proof that bounds only AND states, OR fan-ins, wires, formula leaves, description length, or a chosen evaluator would not establish the requested ordinary bound.

For N=2^n, OPS Theorem 1.4 has a universal constant c, YES threshold s1=2^(beta*n)/(c*n), and NO threshold s2=2^(beta*n)=N^beta; the promise convention is complexity at most s1 versus complexity greater than s2. The proof's anti-checker lemma instantiates the low threshold with 2^(beta*n)/(10*n). The magnification quantifier is one fixed epsilon>0 that works for every sufficiently small fixed beta>0; the conclusion is NP not contained in P/poly. A cycle-specific lower bound must preserve that common epsilon, not choose it after beta.

## Paired full-promise construction attempt

The exact enumerator remains a valid total separator: list the D distinct truth tables computed by circuits of size at most s1, compare the input table against each hardwired table, and OR the equality tests. Circuit counting gives D <= 2^(O(s1*log(N+s1))) = 2^(O(N^beta)); the fan-in-two total-gate cost is O(N*D) = O(N*2^(O(N^beta))). It accepts every forced YES and rejects every forced NO (indeed every table outside the exact Low codebook). A trie or shared prefix comparator can share particular descriptions, but no uniform near-linear bound follows for this codebook; the worst-case direct construction still has N*D comparison work. No near-linear full-promise separator or native cover was constructed. C-474 independently rules out compressing this problem through a balanced sketch of width below N-O(N^beta*log(N)), but does not constrain arbitrary circuits.

## Literature, originality, and exact frontier

Rao's primary result proves exp(Omega(q/sqrt(k*log(n)))) monotone gates for distinguishing bipartite graphs with a k-matching from graphs with no q-matching, using a spread-matching approximation. Its positive witnesses are sparse matchings, and its negative distribution is tailored to that structure. The signed-rail lift is a correct constant-factor simulation, but it does not transfer the matching theorem to the MCSP promise: its inputs are truth-table encodings, not matchings, and a monotone lower bound for one monotone function is not a lower bound for every monotone extension of an antichain promise. This cycle's DNF-approximation transfer is a project-specific attempt and failure, not a new theorem. The Chen-Hirahara-Oliveira-Pich-Santhanam locality barrier concerns specified magnification techniques; neither it nor this failure is a universal impossibility result.

Strongest proved statement this cycle: an exact signed-rail lift preserves arbitrary sharing within a factor of 2, but the Rao-style approximation route has no proved spread parameter for useful YES witnesses.  
Counterexample scope: the zero-table minterm refutes a density/term-width charge only; the parity, equality, sparse-check, and block-relation canaries refute generic incidence charges only.  
Frontier: unchanged. The ordinary lower bound remains N-O(N^beta*log(N)) essential inputs, with C-406's reconvergence refinement; the exact full-promise upper remains O(N*2^(O(N^beta))). The fixed-epsilon OPS target, native rho_GapMCSP >= N-o(N), and P-vs-NP remain open.

Primary sources: [OPS, Theorem 1.4 and Anti-Checker Lemma](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf); [Rao, ECCC TR26-129](https://eccc.weizmann.ac.il/report/2026/129/); [Chen et al., ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/). Signed-rail accounting and the canaries: [C-451](C451_SIGNED_RAIL_MONOTONE_LIFT_AUDIT_2026-10-01.md).

## Changed next action

Do not sharpen the same spreadness transfer. Re-evaluate the project from first principles around the exact all-extension problem: every valid output is an arbitrary total Boolean interpolant between the Low and High codebooks, and the missing fact is a total-gate cost for computing after the complete table is available with unrestricted sharing. The next candidate must identify a semantic invariant whose recurrence is proved for every AND/OR/NOT gate and whose superlinear output value follows from both promise endpoints, or provide a costed promise-saturated source map. Keep the full-promise construction attempt paired with that proof.
