# C-373 - A polynomial C-319 cover needs many Reed-Muller policy regions

Date: 29 September 2026  
Route: extend C-372 from one shared policy cone to arbitrary policy switching using bounded-independence fooling for CNFs.  
Classification: **PROVED POLICY-DIVERSITY LOWER BOUND; STILL BELOW LINEAR q.**

## 1. Setup

Use the code family F=RM(t,n) from C-372, with 0<delta<1/2, H_2(delta)<beta, and delta<1-beta. Its dual distance is D=2^(t+1)=N^(delta+o(1)). Thus a uniformly random codeword of F is (D-1)-wise independent: projection to any set of fewer than D coordinates is uniform.

Fix any sound C-319 cover with q polynomial in N. By the positional-policy normal form in C-334, every accepting policy region is a CNF of at most m=2q seed clauses, and each region is contained in SIZE(s2). Completeness means these policy regions cover every member of F.

## 2. Per-region bound

Let R be one such policy region. Under a uniform N-bit table, soundness gives

Pr_U[R] <= |SIZE(s2)|/2^N = 2^(h-N),

where h=log2|SIZE(s2)|=N^(beta+o(1)).

Bazzi's theorem says that every k-wise independent distribution fools any m-clause CNF to error at most O(m^2.2 * 2^(-sqrt(k)/10)). Take k=D-1. Since m is polynomial in N, the polynomial factor is absorbed by the exponential term, giving

|Pr_F[R] - Pr_U[R]| <= 2^(-Omega(sqrt(D))).

Therefore

Pr_F[R] <= 2^(-Omega(sqrt(D))).

This estimate is uniform over every policy region of the fixed cover; it does not assume the region is the same for different codewords.

## 3. Policy-diversity consequence

If R_Q is the number of distinct policy regions realized by the cover, their union contains all of F. The union bound and the per-region estimate imply

R_Q >= 2^(Omega(sqrt(D))) = 2^(N^(delta/2+o(1))).

C-334 shows that a region depends only on the subset of the 2q fixed seed clauses used at policy stops, so R_Q <= 2^(2q). Consequently,

q >= Omega(sqrt(D)) = Omega(N^(delta/2+o(1))).

This is a genuine multi-cone restriction on any polynomial-size cover: it must realize exponentially many distinct sound CNF regions on this low-circuit family. It is not a superlinear state bound. Since delta<1/2, the resulting q lower bound is weaker than the established q>=N-o(N).

## 4. What remains open

The argument quantifies policy switching but charges it only through the crude subset count 2^(2q). The central open step is to exploit the fixed transition graph to show it cannot realize the required 2^(Omega(sqrt(D))) sound regions at linear q, or that its region transitions combine into a forbidden compatible splice. Neither C-372 nor C-373 supplies that step.

The class of policies is restricted by one shared transition graph, but this proof does not use that restriction beyond the seed-clause count. A successful continuation must derive a sharper graph-sensitive region-capacity bound, not just repeat the CNF-fooling estimate.

## 5. Checkpoint and source

- Each safe policy cone captures at most 2^(-Omega(sqrt(D))) of the uniform Reed-Muller family: proved using bounded independence.
- Any complete cover needs at least 2^(Omega(sqrt(D))) distinct sound policy regions: proved.
- The induced state lower bound is only q=Omega(sqrt(D)), below q>=N-o(N).
- No full-promise near-linear cover or P-vs-NP proof follows.

Primary pseudorandomness source: Louay M. J. Bazzi, *Polylogarithmic Independence Can Fool DNF Formulas*, SIAM Journal on Computing 38(6), 2009. Its theorem gives error O(m^2.2 * 2^(-sqrt(k)/10)) for k-wise independent distributions against m-clause CNFs/DNFs: https://doi.org/10.1137/070691954. See also C-334 for the policy-CNF normal form and C-372 for the code construction.
