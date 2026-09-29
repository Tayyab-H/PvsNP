# C-365 — Universal-circuit lifting exposes the missing description channel

Date: 29 September 2026  
Route: push the circuit-description/address-multiplexing proposal through a universal circuit, then audit its promise parameters and reduction direction.  
Classification: **EXACT ARCHITECTURE / PARAMETER AUDIT; NO q IMPROVEMENT.**

## 1. Candidate lift

Let the source table be \(f:\{0,1\}^n\to\{0,1\}\), with \(N=2^n\),
\[
s_1=N^\beta/(c n),\qquad s_2=N^\beta.
\]
Take a universal circuit \(U_s(d,x)\) whose control string \(d\) selects a circuit of size at most \(s=s_1\). Standard universal-circuit constructions use \(O(s\log s)\) control bits and \(O(s\log s)\) gates. Choose a padded control string of length \(L=\Theta(s\log s)\); unused padding does not change the evaluator. Define a larger truth table
\[
G_f(d,x)=U_s(d,x)\oplus f(x).
\]
The zero-circuit description \(d_0\) gives \(G_f(d_0,x)=f(x)\).

This is the natural way to put both a candidate global description and the address into the same input: \(d\) is shared across all \(x\), and the universal circuit evaluates the selected description at each address.

## 2. What the lift preserves

If \(\mathrm{CC}(f)\le s_1\), then
\[
\mathrm{CC}(G_f)\le O(s_1\log s_1)+s_1
=O_\beta(N^\beta).
\]
For fixed \(c,\beta\), \(s_1\log s_1=(\beta/c+o(1))N^\beta\). Thus for sufficiently small fixed \(\beta\), the lifted YES tables fit below the high threshold \(s_2=N^\beta\), with a constant-factor gap. If \(\mathrm{CC}(f)>s_2\), restriction to \(d=d_0\) gives
\[
\mathrm{CC}(G_f)\ge \mathrm{CC}(f)>s_2.
\]
So the map sends the source YES and NO promises into a target gap with low threshold \(a=O(s_1\log s_1)\) and high threshold \(b=s_2\).

There is also a useful circuit-composition fact. For each fixed table coordinate \((d,x)\), \(U_s(d,x)\) is a constant, so \(G_f(d,x)\) is either \(f(x)\) or its negation. A target separator circuit of size \(S\), restricted to these coordinates, yields a source separator circuit of size at most \(S+O(N)\).

The direction matters: this says **a target separator gives a source separator**. A lower bound for the target separator does not imply a lower bound for the source separator. The reduction is source-to-target, so target hardness alone cannot establish the desired source hardness.

## 3. Why the ambient native lower bound does not transfer

The lifted input dimension is
\[
m=n+L=n+O(s_1\log s_1)=\Theta_\beta(N^\beta),
\]
and its truth-table length is \(M=2^m\), far larger than \(N\). The target promise ranges over all \(M\)-bit tables. The image \(\{G_f:f\in\{0,1\}^N\}\), however, has only \(N\) independent input bits: every output coordinate is a copy or complement of one source bit.

Consequently, a one-anchor lower bound for the full target promise that charges its \(M\) table coordinates cannot be pulled back by simply restricting to this image. On the image, repeated coordinates reveal the same source bit; they do not create \(M\) independent address contexts. Substituting repeated/complemented coordinates into a target recurrence can create tautological seed clauses, while the same endpoints also determine the recurrence's state-to-state containment relations. But even an endpoint-valid restriction of a target cover would only give a source cover from a target cover; it would not transfer a target lower bound to the source. That transfer needs either a lower bound proved directly for the image-restricted promise in a native model that contains every source cover at no greater q, or a reduction in the reverse direction from the full target promise to the source.

This is the precise point where the apparently large target lower bound stops: its promise contains tables outside the image, and its coordinate count is not a source q-charge.

## 4. What the activation-register version would require

Instead of supplying \(d\) as an input, a native construction could try to compute a description code from the C-319 activation vector and then feed that code to a fixed evaluator. The code has \(L=O(s_1\log s_1)=O_\beta(s_2)\) bits, which is well below the available \(q=\Theta(N)\) state-bit scale. Therefore memory capacity does not rule it out.

The unsolved requirement is computation: for every \(f\in\mathrm{SIZE}(s_1)\), the coupled least fixed point must produce a valid description \(d_f\) of a circuit agreeing with all \(N\) entries. The fixed evaluator can then preserve one description while checking every address. This is a circuit-search witness-extraction task; it does not follow from the fact that a C-319 system decides the low/high promise. The minimum-formula search-to-decision theorem is specifically nonrelativizing, while the cited paper describes search-to-decision for ordinary MCSP as a long-standing open question. No theorem currently turns arbitrary C-319 acceptance into this description code.

Thus the universal-circuit idea identifies three distinct architectures:

1. **Description in the input:** evaluation works, but the control length is \(\Theta(s_1\log s_1)=\Theta_\beta(s_2)\), the original logarithmic gap collapses to a constant-factor gap, and the ambient table grows to \(2^{\Theta_\beta(s_2)}\).
2. **Description stored only in a path/policy:** C-342's residual-function argument rules out a polynomial-size path-only register for the full family.
3. **Description in the activation vector:** q-state capacity is ample, but generating a valid code is the unresolved search/readout problem. A direct separator may bypass circuit witnesses entirely, so no general extraction can be assumed.

## 5. Checkpoint and next proof obligation

- The proved native lower bound remains \(\rho_{\mathrm{GapMCSP}}\ge N-o(N)\).
- No superlinear q lower bound, full-promise near-linear cover, positive CohEnc margin, or P-vs-NP proof follows.
- The fixed-circuit lane-selector matrix is not reopened: C-349/C-359 already show representation dependence and a linear ceiling for ordinary rectangles.
- A meaningful continuation must do one of two things: (i) prove a lower bound directly for the image-restricted promise in a native model that contains every source cover at no greater q; or (ii) analyze the coupled C-319 readout directly, without assuming it outputs a circuit witness. A reverse reduction from the full target promise to the source would also make ambient target hardness relevant.

The new model refinement is that description/address multiplexing has an **input channel, a path channel, and an activation channel**. The first loses the target parameters, the second has the C-342 state explosion, and the third is the only remaining witness-based option but requires search-level readout. This is a classification of the bottleneck, not progress beyond the linear lower bound.

## Sources

- L. G. Valiant, [Universal circuits (Preliminary Report)](https://doi.org/10.1145/800113.803649), STOC 1976: universal simulation with \(O(s\log s)\) size.
- S. Ilango et al., [The Minimum Formula Size Problem is (ETH) Hard](https://epubs.siam.org/doi/10.1137/22M1481579): the formula search-to-decision result is nonrelativizing; the article notes that MCSP search-to-decision remains open.
- A. Pauly, [Parameterized Games and Parameterized Automata](https://cronfa.swan.ac.uk/Record/cronfa46098/Download/0046098-26112018112133.pdf), 2018, Open Question 11: quantitative circuit size for least-fixed-point graph-game forms remains open.
