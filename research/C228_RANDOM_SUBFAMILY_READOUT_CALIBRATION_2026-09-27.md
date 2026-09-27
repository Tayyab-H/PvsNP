# C-228 — A random subfamily of easy tables has hard global readout without dangerous splicing

Date: 27 September 2026  
Scope: hostile artificial-model test for O-151. This proves a superpolynomial native readout lower bound for some promises whose YES tables are individually small-circuit, but the hardness comes from arbitrary global labeling and certificate isolation, not from forced high-complexity splices. It is not a Gap-MCSP result.

## Construction

Write (N=2^n). Fix constants (0<\delta<\alpha<1), set (s_0=\lfloor N^\alpha\rfloor), and choose (k=\lfloor s_0/(C n)\rfloor) for a sufficiently large absolute constant C. Fix k input addresses (a_1,\ldots,a_k\in\{0,1\}^n). For each (S\subseteq[k]), let (w_S\in\{0,1\}^N) be the truth table of

\[
f_S(x)=1\quad\Longleftrightarrow\quad x\in\{a_j:j\in S\}.
\]

An OR of at most k equality minterms computes each (f_S) with (O(kn)\le s_0) gates. Thus the family E of these tables has size (M=2^k), and every member is individually in SIZE(s0).

Let (R=2^{\lfloor N^\delta\rfloor}), so 

\[
\log_2 M=k=\Theta(N^\alpha/n)\gg\log_2R.
\]

Choose an R-element subset W of E with no two tables at Hamming distance one. Such a W exists: the induced hypercube graph on E has at most NM/2 edges, and a uniform R-subset contains an expected at most

\[
\frac{NM}{2}\frac{R(R-1)}{M(M-1)}=O(NR^2/M)=o(1)
\]

internal edges, since k grows faster than (N^\delta).

Use the total artificial promise (Y=W), (Z=\{0,1\}^N\setminus W). A successful closure must compute exactly the indicator of W on the whole cube.

## Native readout lower bound by counting

The C-75 recurrence has at most

\[
2^{4Nq+2q^2+q}
\]

effective q-rule descriptions: choose the 2q seed clauses over 2N signed literals, the two predecessor subsets per state, and the empty-output subset. This upper count includes unrealizable descriptions, so it safely bounds the number of q-rule output functions.

There are \(\binom MR\) distinct choices of W, with

\[
\log_2\binom MR\ge R(\log_2M-\log_2R)=:A,
\qquad A=\Theta(RN^\alpha/n).
\]

Set (Q=\lfloor\sqrt{A/16}\rfloor). For large N,

\[
\log_2\left(\sum_{q\le Q}2^{4Nq+2q^2+q}\right)<A,
\]

because (2Q^2\le A/8) and (4NQ+Q+\log_2(Q+1)=o(A)). Hence some W is not represented by any q-rule closure with (q\le Q). Its minimum native readout size is

\[
q>Q=2^{\frac12N^\delta+O(\log N)},
\]

which exceeds (N^{1+\epsilon}) for every fixed epsilon for sufficiently large N.

The seed-feature floor remains only linear: monotonicity forces at least (N-\log_2R=N-o(N)) true seed clauses at any fixed accepted table, while all 2N signed literals give the universal linear feature ceiling. Thus a linear seed floor and even individually easy YES tables coexist with superpolynomial global readout complexity.

## What happens to certificates and splices

Every consistent output-proof support C has its entire cylinder inside W. If C leaves any coordinate free, that cylinder contains two adjacent tables, contradicting the choice of W. Therefore every accepting certificate fixes all N coordinates and identifies one table in W.

For any shared state context K and replacement support C, a consistent union (K\cup C) is itself an output certificate. It too must fix all N coordinates and identify a member of W. So every *safe* splice is either inconsistent or collapses to one of the already accepted isolated anchors; this example does not force a splice to create a forbidden table. The lower bound above is purely a counting argument about which global subsets W can be represented.

## Learning for the actual problem

This is not Gap-MCSP: Z contains many tables of circuit complexity at most s0. It is a calibration showing that “many individually easy anchors + linear feature floor + wide certificates” does not identify the source of superlinear readout cost. Global hardness can come from a randomly chosen sparse subset of easy objects whose certificates are isolated, with no useful cross-splice at all.

Therefore O-151 must be explicitly OPS-specific. A valid proof needs a property of the actual full class SIZE(s1) versus the full high class CC>s2 that forces compatible proof contexts, or it must use a different readout invariant. It cannot derive dangerous splicing from certificate width, anchor count, and easy individual descriptions alone. Conversely, the existence of this artificial counterexample does not rule out O-151 for Gap-MCSP.

**Status:** proved artificial superpolynomial readout lower bound and its non-splicing mechanism. No actual-promise lower bound, forced splice theorem, or P-vs-NP proof follows.
