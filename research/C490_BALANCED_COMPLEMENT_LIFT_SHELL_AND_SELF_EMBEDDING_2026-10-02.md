# C-490 — balanced complement lifts preserve a high shell, but embed the same MCSP task

**Date:** 2 October 2026  
**Status:** exact balanced subfamily and shell-count theorem proved; no circuit lower-bound improvement.

## 1. Exact target and OPS quantifiers

Write (N=2^n). The OPS Gap-MCSP promise accepts tables with circuit size at most

\[
s_1=\left\lfloor\frac{N^\beta}{10n}\right\rfloor
\]

and rejects tables with size strictly greater than (s_2=N^\beta); the middle is unrestricted. Their magnification theorem requires one fixed \(\epsilon>0\) such that the lower bound against total fan-in-two Boolean circuits of size (N^{1+\epsilon}) holds for every sufficiently small fixed \(\beta>0\). This premise implies \(\mathrm{NP}\not\subseteq\mathrm{P/poly}\). The paper states the universal low-threshold constant as (c\), and its proof uses the displayed (10n) threshold. These are the exact parameters used here. [OPS, Theorem 1.4 and its proof](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)

## 2. Mechanism: lift an arbitrary table to an exactly balanced table

For (g:\{0,1\}^{n-1}\to\{0,1\}), define

\[
\Lambda(g)(x,z)=g(x)\oplus z.
\]

Every output table has exactly (N/2) ones and obeys the paired-coordinate relation

\[
\Lambda(g)(x,0)\oplus\Lambda(g)(x,1)=1\quad\text{for every }x.
\]

For AND/OR/NOT fan-in-two circuits, with constants not supplied for free,

\[
CC_(n-1)(g) - 2 <= CC_n(Lambda(g)) <= CC_(n-1)(g) + 5.
\]

For the lower inequality, restrict z=0; if constants are not free, produce 0 as x_1 AND NOT x_1 using two gates. For the upper inequality, compute g XOR z=(g AND NOT z) OR (NOT g AND z), using at most two NOT, two AND, and one OR gates. Thus base size at most s_1-5 lifts to a promised YES table; base size greater than s_2+2 lifts to a promised NO table. If constants are supplied for free, the lower-side additive 2 is unnecessary.

### Balanced high-shell theorem

Let M=N/2=2^(n-1), and take r=ceil(2s_2+4). Around every base table g in {0,1}^M, the Hamming sphere of radius r has

\[
\binom Mr\geq(M/r)^r=2^{(2(1-\beta)+o(1))s_2n}
\]

points. Counting ordered descriptions with at most five gate types, two predecessor indices among n+s_2+2 earlier nodes per gate, and one output choice gives the following upper bound. Since log2(n+s_2+2)=beta n+o(n), its base-two logarithm is at most (2 beta+o(1))s_2 n:

\[
(s_2+3)(n+s_2+3)[5(n+s_2+2)^2]^(s_2+2).
\]

The shell exponent exceeds the circuit-count exponent by 2-4 beta+o(1), which is at least 1+o(1) for beta<=1/4. Dividing the number of low tables by the shell size therefore gives a bad fraction of 2^(-Omega(s_2 n)). Thus, for each fixed 0<beta<=1/4, a uniform radius-r neighbor g-prime has CC_(n-1)(g-prime)>s_2+2 except with probability 2^(-Omega(s_2 n)), uniformly for every center g. Each difference in the base table flips both entries of its lifted pair, so

\[
d_H(\Lambda(g),\Lambda(g'))=2r=(4+o(1))s_2.
\]

Conditioning the shell on CC_(n-1)(g-prime)>s_2+2 therefore yields an exact promise-supported pair of balanced lifted tables under the no-free-constants convention. Both sides obey the same paired-coordinate relation, so the O(N) test for that relation does not distinguish the pair. This refines the unrestricted balanced shell of C-489 by keeping the noise inside the lift image.

### Exact mechanism for unrestricted sharing: pair error

Choose any distribution D-plus on lifted tables Lambda(g) with base complexity at most s_1-5. Generate D-minus by drawing g from the same source, drawing g-prime from its radius-r shell conditioned on CC(g-prime)>s_2+2, and outputting Lambda(g-prime). For a total circuit A on the N table bits, define

\[
\operatorname{Err}(A)=\tfrac12\Pr_{T\sim D_+}[A(T)=0]+\tfrac12\Pr_{T\sim D_-}[A(T)=1].
\]

If every AND/OR/NOT DAG with at most S total gates has Err(A)>0, then no size-S full-promise separator exists: a valid separator must accept every support point of D-plus and reject every support point of D-minus, hence has zero error. This statement counts total gates and quantifies over arbitrary fan-out and reuse; it assumes no witness reconstruction, address-by-address algorithm, or retained caller history. The shell theorem proves only that D-minus is supported on High tables. It does not establish the required error bound. For a k-junta D-plus, the repeated-block membership circuit has zero error with O(N) gates, which disproves this mechanism for that source. The unrestricted choice of D-plus still carries the full unresolved lower-bound burden; the criterion itself is not a shortcut. Conditioning on circuit complexity also gives no efficient sampler for D-minus.

### Counterconstruction theorem for parity-check and global-relation sources

Let h be a fixed parity check on the M base-table coordinates, and suppose every g in the support of D-plus has h dot g=b over F_2. For each center g, let E be a uniformly random r-subset of coordinates and set g-prime=g XOR 1_E. Write p=Pr[h dot g-prime differs from b]. If p is larger than the shell's bad fraction delta=2^(-Omega(s_2 n)), then conditioning on both h dot g-prime not equal to b and CC(g-prime)>s_2+2 defines a nonempty modified distribution D-minus-h supported entirely on High tables. The linear test h dot T(.,0) has zero error on the modified pair and costs O(|supp(h)|) total gates, using a constant-size AND/OR/NOT circuit for each XOR. This is a genuine zero-error counterconstruction to the proposed distribution, not merely a distinguisher with constant advantage.

The required violation probabilities hold for the requested canaries:

- **Parity and affine tables.** For m=n-1>=4, take h(x)=x_1 x_2, viewed as a parity check on the base truth table. Its support has size M/4 and h dot g=0 for every affine g: its inner product with each affine basis function is an even integer. For a uniform r-subset, p=1/2+o(1), by coupling sampling without replacement to r independent samples; the coupling error is O(r^2/M)=o(1). Each affine g has O(n) gates and is below s_1-5 for sufficiently large n; the h-parity test over M/4 table bits uses O(N) AND/OR/NOT gates. Thus even the affine Low source can be perfectly separated from a conditioned High shell by one shared parity check.
- **Sparse parity checks and repeated blocks.** If a Low source obeys g_i=g_j on a repeated block, use h=e_i+e_j. A shell neighbor violates the check exactly when it flips one of i,j, which has probability 2r(M-r)/(M(M-1))=Theta(r/M). This is polynomially larger than delta. Conditioning on high violators leaves a nonempty support; a constant-size AND/OR/NOT parity test separates the pair. The full repeated-block membership test also costs O(N).
- **Blocks generated by simple global relations.** If all Low tables obey g(a,b) XOR g(a',b) XOR g(a,b') XOR g(a',b')=0 for a fixed rectangle (as happens for a block family g(a,b)=u(a) XOR v(b)), the four-coordinate check is violated by a uniform radius-r perturbation with probability Theta(r/M). Conditioning on violation and High again gives a promise-supported D-minus; the four-input parity test costs O(1) gates. Requiring the test on every rectangle still costs only O(M) gates when the relation is checked across a table.

These examples retire Low sources defined by such cheaply testable relations. They do not refute the pair-error criterion for a different D-plus whose support avoids every low-cost exact signature.

## 3. Serious lower-bound attempt: this is a self-embedding, not a gate charge

Let F solve the promise on every lift of a base YES or NO table at the stated shifted thresholds. Given a base truth-table input (y=(g(x))_x\in\{0,1\}^M), form (E(y)) with coordinates

\[
E(y)_{(x,0)}=y_x,\qquad E(y)_{(x,1)}=\neg y_x.
\]

This map uses (M) NOT gates and wires. The composed circuit (G(y)=F(E(y))) has at most \(\mathrm{CC}(F)+M\) gates and separates the base promise

\[
\mathrm{CC}_{n-1}(g)\leq s_1-5
\quad\text{from}\quad
CC_(n-1)(g) > s_2+2.
\]

All resources are charged: (F)'s total gates are retained, (M) complement gates are added, and wires/description length are not treated as gates. This reduction preserves any superlinear lower bound up to an additive (M=O(N)), but supplies no such lower bound. Its thresholds are expressed using (N), so this exact statement alone does not identify them with the standard OPS thresholds at input length (M).

The shell count proves only that most nearby lifted tables are High. It does not prove that every (N^{1+\epsilon})-gate circuit errs on a chosen endpoint distribution. For (k)-junta Low sources, repeated-block equality on the base coordinates still separates all Low samples from all High shell samples in (O(N)) gates. Affine sources retain the face-parity tests from C-489. Sparse parity-check or simple global-block sources also have linear-size shared tests when the total check description is linear. These defeat those candidate distributions, not the whole promise or the lift theorem.

## 4. Full-promise separator construction attempt

The lift-image predicate is checkable in (O(N)) gates by testing all (M) coordinate pairs. On that image, the problem reduces to base Gap-MCSP. This does not extend to all promised tables: for example, (f(x,z)=x_1) is a balanced Low table but is outside the lift image because its two entries in each (z)-pair are equal. There are also High tables outside the image: for fixed \(\beta<1\), the lift image has (2^{N/2}) tables, the size-(s_2) class has (2^{o(N)}) tables, and their union is smaller than (2^N) for sufficiently large (N). Thus either constant default label off the image violates one promise endpoint. The exact all-promise fallback remains Low-description enumeration at \(O(N2^{O(N^\beta)})\); the lift reduces that bound by only a constant factor and gives no near-linear separator.

## 5. Barriers, novelty, and resource scope

The complement lift and restricted shell are elementary project-level constructions; no novelty over standard restriction/reduction methods is claimed. The mechanism is not an ordinary-circuit lower bound, and it gives no paid-AND, OR-only, wire, description, runtime, fusion, or cyclic-closure bound. It does not directly instantiate the formal locality barrier: Chen et al.'s results concern specified magnification frontiers and restricted models, including oracle-augmented formula models. This work neither applies one of those lower-bound techniques to the OPS ordinary-circuit target nor demonstrates an escape from the barrier. [Chen et al., ITCS 2020](https://drops.dagstuhl.de/storage/00lipics/lipics-vol151-itcs2020/LIPIcs.ITCS.2020.70/LIPIcs.ITCS.2020.70.pdf)

## 6. Exact frontier effect

**Strongest proved statement:** every base table has a radius-ceil(2 s_2+4) shell in which all but a 2^(-Omega(s_2 n)) fraction have circuit size greater than s_2+2; the paired complement lift turns that shell into exactly balanced YES/NO tables satisfying one common global relation.

**Strongest counterconstruction:** for the affine Low source, the fixed parity check h(x)=x_1x_2 separates the lift-shell pair in O(N) gates after conditioning the High shell on the opposite syndrome. Sparse repeated-block checks cost O(1) gates, and a fixed four-coordinate global-block check also costs O(1). The lift itself adds only M NOT gates to a restricted separator.

**Quantitative change:** none. The ordinary lower bound remains N-O(N^beta log N) essential inputs, with the existing additive refinement. The OPS fixed-epsilon lower bound is unproved; the exact full-promise upper remains O(N 2^(O(N^beta))). Native rho, fusion, and cyclic-closure claims are unchanged and separate. No P-vs-NP proof follows.

## 7. Next changed mechanism

Do not pursue balance, Hamming shells, or source-family entropy as gate charges. The next test must attack the residual *decision* in the self-embedding: whether there is a promise-saturated partial-table extension predicate whose circuit lower bound survives arbitrary reuse and whose fixed-beta parameters transfer to the OPS theorem. It must come with a complete all-promise construction attempt and a proof that the purported source map does not simply hide the same Gap-MCSP decision.
