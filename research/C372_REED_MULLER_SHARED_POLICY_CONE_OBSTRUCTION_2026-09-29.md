# C-372 - Reed-Muller anchors force exponentially large shared safe certificates

Date: 29 September 2026  
Route: use dual distance to make a low-circuit anchor family that no polynomial-size single policy-CNF can safely contain in its entirety.  
Classification: **PROVED SINGLE-CONE OBSTRUCTION; NO ARBITRARY-COVER STATE CHARGE.**

## 1. Low-circuit anchor code

Let the truth-table length be N=2^n. Fix the OPS exponent beta and choose a constant 0<delta<1/2 such that H_2(delta)<beta and delta<1-beta, where H_2 is binary entropy. Set t=floor(delta n), and let F=RM(t,n), the binary Reed-Muller code obtained by evaluating all multilinear polynomials of degree at most t on GF(2)^n. Write r=dim(F)=sum_(i<=t) binom(n,i).

The standard parameters are:

- r=N^(H_2(delta)+o(1));
- minimum distance d(F)=2^(n-t)=N^(1-delta+o(1));
- dual distance d(F-perp)=2^(t+1)=:D=N^(delta+o(1)).

Each codeword is a truth table of one degree-t polynomial. Summing its at most r monomials with fan-in-two Boolean gates gives circuit size O(r n)=N^(H_2(delta)+o(1))=o(s1). Thus F is a family of 2^r tables in SIZE(s1). Since delta<1-beta, its minimum distance exceeds h+2 eventually, where h=log2|SIZE(s2)|=N^(beta+o(1)). The Reed-Muller dimension, distance, and dual-code identities are standard; see the cited coding-theory references below.

## 2. Single-cone theorem

Let Phi be a satisfiable CNF on the N table bits, with consistent clauses, such that:

1. every member of F satisfies Phi; and
2. every model of Phi lies in SIZE(s2).

If C is any clause of Phi and W_C is its set of table coordinates, then |W_C| >= D.

Indeed, if |W_C|<D, projection of F onto W_C is the full Boolean cube. This follows because a failure of surjectivity would give a nonzero dual-code word supported on W_C, contrary to dual distance D. In particular, some member of F would realize the pattern falsifying C, contradicting F subseteq Mod(Phi).

A consistent clause of width w falsifies exactly 2^(N-w) tables, hence at most 2^(N-D). Every table outside SIZE(s2) must falsify at least one clause of Phi. If M2=|SIZE(s2)| and Phi has m clauses, then

2^N - M2 <= sum over C in Phi of 2^(N-|W_C|) <= m * 2^(N-D).

Therefore

m >= (1-M2/2^N) * 2^D = (1-o(1)) * 2^(N^(delta+o(1))).

So one sound CNF region cannot contain this entire low-circuit code unless it has superpolynomially many clauses. In particular, one positional-policy certificate region of a q-state C-319 list has at most 2q seed clauses, so no polynomial-q policy region can contain all of F.

## 3. What this does and does not charge

This is a stronger common-cone obstruction than the pairwise C-371 condition: every pair of distinct codewords is far, and yet the obstruction follows from a global projection property. It rules out a single shared positional policy for the whole family.

It does not imply a lower bound for an arbitrary C-319 cover. Different tables may use different positional policies and therefore different subsets of the fixed 2q seed clauses. There are up to 2^(2q) distinct seed-clause subsets; at the existing q=N-o(N) scale this crude policy count is already much larger than |F|=2^r, since r=o(N). The code can therefore be partitioned among many safe cones without violating this theorem. C-319's transition graph may also correlate those regions in ways the cone argument ignores.

The next missing lemma is a state-sensitive bound on how many Reed-Muller anchors one fixed q-state transition graph can distribute among its sound policy cones, or a proof that such distribution creates a forbidden compatible splice. A raw count of anchors, clauses, or policies will not do it. No superlinear q bound or full-promise cover is obtained here.

## 4. Audit and calibration

- Every table in F is low: proved by the degree-t circuit upper bound.
- Every single safe CNF containing all of F needs at least (1-o(1))*2^D clauses: proved by dual distance and high-table counting.
- This theorem applies to one common certificate cone, not to the union of policy cones for an arbitrary cover.
- The native lower bound remains q>=N-o(N); there is no P-vs-NP proof or breakthrough claim.
- C-257 parity and C-258 repeated equality remain required hostile calibrations for any attempted state-charge extension.

## 5. References

- Noam Elkies, Harvard course notes, *The Theory of Error-Correcting Codes*, Reed-Muller section. The notes state the dimension and minimum-distance formulas and prove RM(t,n)^perp=RM(n-t-1,n): https://people.math.harvard.edu/~elkies/M256.13/index.html
- Elia Santi, Christian Hager, and Henry D. Pfister, *Decoding Reed-Muller Codes Using Minimum-Weight Parity Checks* (2018), background on the dual RM code and minimum dual-check weight: https://doi.org/10.1109/ISIT.2018.8437637

