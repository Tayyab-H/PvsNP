# C-482 - ANF testing defeats affine-scrambled polynomial-trace ensembles

Date: 2 October 2026  
Status: complete proof of a distribution-specific obstruction; no frontier change.

## Candidate construction

Continue the C-481 distributional branch with a concrete attempt to repair C-480. Let N=2^n, s1=floor(N^beta/(10n)), and s2=N^beta. Choose k=floor(s1/(C n^2)) for a sufficiently large constant C. Sample a degree-<k polynomial P over GF(2^n), and apply an address transformation A before evaluating:

    T_(P,A)(x) = Tr(P(A(x))).

For affine bijections A, each output table has an ordinary circuit of O(k n^2+n^2) gates, hence lies in L_s1. The proposed purpose of randomizing A is to remove the fixed low-dimensional linear-subspace structure that C-481 exposed. It fails: all such outputs still lie in the common degree-at-most-d space V_d described below.

## Algebraic-degree lemma

**Lemma.** The Boolean algebraic degree of x -> Tr(P(x)) is at most

    d = floor(log2(k-1))+1.

**Proof.** Write a monomial exponent j in binary as j=sum_(i in B) 2^i. Frobenius maps x -> x^(2^i) are linear over GF(2) in the n address bits. Since field multiplication is bilinear, each coordinate of x^j = product_(i in B) x^(2^i) has Boolean degree at most |B|=wt_2(j). Trace and multiplication by a field coefficient are linear maps, so they do not increase degree. Summing monomials with j<k gives degree at most max_(j<k) wt_2(j) <= floor(log2(k-1))+1.

An affine address substitution preserves this degree bound: composing a degree-d Boolean polynomial with affine linear forms does not increase degree. More generally, if every coordinate of A has Boolean degree at most e, then deg(T_(P,A))<=e*d. Thus every fixed-degree address scrambler with e*d<n leaves a proper low-degree function space; if e*d<n/2, the explicit ANF test below also rejects almost every uniform table.

Because log2 k=beta*n-O(log n), for every fixed beta<1/2 the affine-scrambled ensemble has d<n/2 for all sufficiently large n. Mixing over affine A does not remove the linear-subspace obstruction: every output remains in V_d, the linear space of all Boolean functions of degree at most d. Its dimension is M_low=sum_(j=0)^d binom(n,j)<N.

## Explicit distinguisher and resource accounting

Given an arbitrary N-bit truth table T, compute its algebraic normal form by the Boolean Mobius transform. For each of n variables, update N/2 coefficient pairs by XOR, for at most N*n/2 XOR operations. Compile each XOR to a constant number of AND/OR/NOT gates, then OR all coefficients whose monomial degree exceeds d.

Call the resulting circuit Q_d. It has O(N*n)=O(N log N) total gates and accepts exactly the tables of algebraic degree at most d. It accepts every T_(P,A) for affine A. The ANF transform is an invertible linear map on the N table bits, so for a uniform table its coefficients are uniform; if

    M = sum_(j=d+1)^n binom(n,j),

then Pr[Q_d(U)=1]=2^(-M). Since d<n/2, M>=N/2 and the acceptance probability is at most 2^(-N/2). Therefore Q_d distinguishes the entire affine-scrambled trace distribution from uniform with advantage 1-2^(-N/2), using O(N log N) gates. For every fixed epsilon>0, this is below N^(1+epsilon) for sufficiently large N.

**Resource distinctions.** The distribution has seed entropy kn+log2|AGL(n,2)|=kn+n^2+O(n) bits. A simple exact sampler for the affine map uses rejection sampling with constant expected trials. Each resulting n-input Boolean function has circuit size O(kn^2+n^2). A straightforward sampler that materializes all N output bits uses N evaluations, at most O(N(kn^2+n^2)) gate operations/time; this is separate from the distinguisher and is not claimed to save a source-map budget. Q_d has O(N log N) paid AND/OR/NOT gates and O(N log N) wires for its Mobius layers plus the final OR. Under standard gate-address encoding, its gate list is O(N log^2 N) description bits and can be printed in polynomial time in N; both are separate from gate count. For a fixed address permutation, its inverse can be wired into the input order without gates. Random affine substitutions need no inverse-selection circuit because affine changes preserve degree. No native fusion states or OR-rule measure are inferred from this ordinary-gate calculation.

## Strongest counterconstruction and what it defeats

The C-481 lemma already gives a nonuniform parity test on at most M_low+1 table coordinates, with O(M_low) gates, accepting every member of V_d and half of uniform tables. Since M_low<N, this is at most linear and below N^(1+epsilon). The explicit ANF circuit gives the stronger uniform acceptance estimate 2^(-N/2). Thus random affine changes of basis do not even remove the fixed proper linear space of truth tables.

Q_d is **not** a full-promise separator:

1. It rejects forced YES tables such as the truth table of AND_n, whose circuit size is O(n) but whose algebraic degree is n.
2. It accepts some High tables. There are 2^M_low functions of degree at most d, where M_low=sum_(j=0)^d binom(n,j)=2^(n H_2(beta)+o(n)) and H_2 is binary entropy. For 0<beta<1/2, H_2(beta)>beta, so M_low grows faster than the circuit-description exponent O(s2 log N)=O(N^beta*n). Thus the degree-at-most-d family is larger than L_s2 for sufficiently large n.

This defeats the proposed distribution and its natural ANF recognizer. A single fixed permutation of truth-table coordinates is also harmless to the test: its inverse is a permutation of the N input wires and costs no gates. A mixture over hidden, high-degree address permutations is a different candidate and is not covered by this proof. More generally, bounded-degree scramblers with e*d<n remain in a proper degree space and have an O(N)-gate parity distinguisher by C-481; when e*d<n/2 they also have the explicit near-perfect ANF distinguisher. For other scramblers, the generator and per-table circuit costs must be charged, and each simpler invariant requires separate analysis. Nothing here refutes the OPS lower-bound target or arbitrary nonlinear ensembles.

## Paired full-promise construction attempt

The exact Low-description enumerator remains the only complete separator established in this project: enumerate each circuit of size at most s1, compare all N table bits, and OR the equality tests, for O(N*2^(O(N^beta))) total gates. Q_d improves no complete upper bound: it misses low-degree-exception tables such as AND_n and accepts some tables above s2. No near-linear full-promise separator was found.

## Literature and originality

The degree argument and Mobius-circuit distinguisher are elementary project-specific calculations, not claimed as a new general lower-bound technique. They are a stronger audit of one candidate ensemble beyond C-481's affine dual checks. Existing local-PRG results establish MCSP lower bounds for formulas, branching programs, AC0, and comparator circuits, but those circuit models do not transfer to unrestricted ordinary DAG circuits without a compiler and full cost analysis. See [Cheraghchi et al., ECCC TR19-022](https://eccc.weizmann.ac.il/report/2019/022/) and [Cavalar and Lu, ECCC TR21-171](https://eccc.weizmann.ac.il/report/2021/171/).

## Exact frontier effect

**Strongest proved statement this cycle:** every affine-scrambled degree-<k polynomial-trace table has Boolean degree at most floor(log2(k-1))+1, and a nonuniform O(N log N)-gate circuit distinguishes this ensemble from uniform with advantage 1-2^(-Omega(N)).

**No quantitative frontier change:** the ordinary total-gate lower bound remains N-O(N^beta log N), with C-406's additive logarithmic reconvergence refinement. The fixed-epsilon OPS N^(1+epsilon) target remains open. The exact full-promise upper remains O(N*2^(O(N^beta))); no near-linear construction was found. The separate native rho_GapMCSP>=N-o(N) target is unchanged. No P-vs-NP proof follows.
