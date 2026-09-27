# C-230 — Exact safe-splice threshold is the subcube dimension of SIZE(s2)

Date: 27 September 2026  
Scope: sharpen the cylinder condition in C-227 and test whether certificate width can be improved. It identifies the correct geometric parameter and shows it is already of order `s2 log s2`; it yields no superlinear fusion bound.

## The parameter

Define the largest full-coordinate subcube contained in the non-high class:

\[
\kappa_\square(s_2)=\max\{|F|:\exists a\in\{0,1\}^{[N]\setminus F}\ \forall y\in\{0,1\}^{F},\ \mathrm{CC}(a\cup y)\le s_2\}.
\]

Here F is the set of truth-table addresses left free and a fixes every other table bit. A consistent support C fixes `r(C)` coordinates, so its cylinder has free set of size `N-r(C)`. For a successful Gap-MCSP closure every accepted cylinder lies in `SIZE(s2)`. The exact soundness condition is therefore

\[
\boxed{N-r(C)\le\kappa_\square(s_2).}
\]

The counting bound used in C-221 is the immediate estimate

\[
\kappa_\square(s_2)\le\log_2|\mathrm{SIZE}(s_2)|=O(s_2\log(s_2+n)).
\]

Thus a splice contradicts soundness as soon as its consistent support leaves more than `kappa_square(s2)` coordinates free. This is the sharp threshold for this cylinder argument; requiring more than `log |SIZE(s2)|` free coordinates is sufficient but can be unnecessarily strong.

## Structured lower bound on safe-cube dimension

Use Lupanov's synthesis theorem: every Boolean function on k input bits has a fan-in-two circuit of size `O(2^k/k)`. Fix an `(n-k)`-bit prefix p and let

\[
F=\{x\in\{0,1\}^n:x_{1..n-k}=p\},\qquad |F|=2^k.
\]

For any labeling g of F, the full n-variable function that equals g on F and zero outside F is `1[x_{1..n-k}=p] AND g(x_{n-k+1..n})`. It has circuit size `O(n+2^k/k)`. Choose k so `2^k/k` is a sufficiently small constant times s2. At OPS scales `s2=N^beta`, fixed `0<beta<1`, this has k<n and

\[
|F|=2^k=\Theta(s_2\log s_2)=\Theta(N^\beta n),
\]

while every one of the `2^|F|` extensions has circuit size at most s2. Hence

\[
\boxed{\kappa_\square(s_2)=\Theta(s_2\log s_2)=\Theta(\log|\mathrm{SIZE}(s_2)|)}
\]

up to constants for the fixed-beta OPS regime. The lower bound is the structured-prefix subcube above; the upper bound is circuit counting. The underlying classical synthesis result is Lupanov 1958, *On the possibilities of synthesis of circuits from arbitrary elements* ([MathNet record and scan](https://www.mathnet.ru/php/archive.phtml?jrnid=tm&option_lang=rus&paperid=1277&wshow=paper)).

In particular, the all-zero low table has a safe partial-assignment cylinder fixing every coordinate outside F and leaving `Theta(s2 log s2)` truth-table bits free, with every completion still in `SIZE(s2)`. This support need not occur in any particular fusion grammar; it shows soundness alone cannot force every certificate to pin more coordinates than `N-Theta(s2 log s2)`.

## Consequence for O-151

The exact splice target should be stated using `kappa_square`, not only the loose counting ceiling:

> Find a shared state context K and replacement support C such that K union C is consistent and leaves more than `kappa_square(s2)` coordinates free.

That produces a high-complexity extension immediately. The safe-cylinder obstruction is already tight to within constants, so a proof cannot get a major improvement by sharpening certificate width alone. It must show that a small closure forces a splice whose free set is too large, or use a different global readout invariant. This is a structural refinement of C-227, not a new lower bound.

**Status:** exact geometric obstruction defined; `kappa_square=Theta(s2 log s2)` at OPS scales by counting and Lupanov synthesis. No forced splice or superlinear q bound follows.
