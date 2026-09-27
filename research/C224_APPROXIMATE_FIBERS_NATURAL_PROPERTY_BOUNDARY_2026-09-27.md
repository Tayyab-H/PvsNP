# C-224 — Approximate signature fibers and the natural-property boundary

Date: 27 September 2026  
Scope: continue the C-75 shared-DAG route. Test whether natural-property learning or approximate circuit signatures turn a small low/high separator into a useful shared-DAG theorem. No separator lower bound or P-vs-NP result is claimed.

## 1. Separator polarity and the proposed bridge

Let `N=2^n`, `Y=SIZE(s1)`, and `Z={0,1}^N minus SIZE(s2)`, with `s1=N^beta/(c n)`, `s2=N^beta`, and fixed `0<beta<1`. Let `h` be a separator: `h=1` on `Y` and `h=0` on `Z`. Its complement `D=1-h` rejects every low table and accepts every high table. Circuit counting gives `|Z|/2^N=1-o(1)`, so this predicate has the largeness expected of a natural-property test.

There is a uniformity gap. Carmosino–Impagliazzo–Kabanets–Kolokolova's Theorem 5.1 assumes a **P-natural** property. A rect-DAG/separator for each input length gives a nonuniform family of Boolean circuits for `D`; even if each has size polynomial in `N`, that alone does not give a uniform P algorithm constructing/evaluating the family. The theorem also needs the predicate at every smaller truth-table length used in its generator, not only one isolated parameter. Therefore the theorem cannot be applied directly to one C-75 separator or to an arbitrary nonuniform separator family.

Even granting a suitably uniform natural-property family, the theorem outputs a randomized learner for low-complexity functions with oracle access to the target. It does not output a smaller separator, a product-rectangle DAG, or a fusion cover. The separator is used inside the learner. No complexity of the original separator is removed by that implication.

The exact theorem says: for `R` a P-natural property of largeness at least `1/5`, useful against `Λ[u]`, and `Λ` containing `AC0[p]`, a randomized algorithm given oracle access to `f in Λ[s_f]` outputs an `epsilon`-approximating circuit in time
\[
\operatorname{poly}\bigl(n,1/\epsilon,2^{u^{-1}(\operatorname{poly}(n,1/\epsilon,s_f))}\bigr).
\]
Its compression corollary patches the approximation errors at additional cost `O(epsilon 2^n n)`, subject to the stated inverse-usefulness condition. These are learning/compression conclusions, not lower bounds on the separator or its DAG. Primary source: Carmosino et al., [Learning Algorithms from Natural Proofs](https://drops.dagstuhl.de/storage/00lipics/vol050-ccc2016/LIPIcs.CCC.2016.10/LIPIcs.CCC.2016.10.pdf), Theorem 5.1 and Corollary 5.2.

## 2. Robust approximate-fiber lemma

This is a local extension of the exact C-115 signature argument.

Let `w:{0,1}^n->{0,1}` be low, let `C` be a Boolean circuit of size `r`, and suppose `C(x)=w(x)` on all but `e` addresses. Let `G={x:C(x)=w(x)}` be the good addresses. Select `k` internal wire values of `C`, including its output, and write their joint signature as `sigma(x) in {0,1}^k`. For each signature cell `p`, consider the values of a second table `z` on `G intersect sigma^{-1}(p)`. Let `m` be the total number of good addresses that disagree with a majority value chosen separately in each nonempty cell (ties may be settled arbitrarily).

**Lemma.** There is a circuit for `z` of size
\[
  r+O(k2^k+(e+m)n).
\]

**Proof.** Build the lookup `g(p)` from the chosen majority bit for each cell, at cost `O(k2^k)`, and compose it with the selected wires of `C`. This agrees with `z` on all but at most `e+m` addresses: at most `e` bad addresses, plus the `m` minority good addresses. Correct those exceptional addresses by XORing point indicators, each of size `O(n)`. The circuit for the selected wires reuses `C`, so the total is as claimed.

**Prior-result calibration.** C-120 already shows that in the exact-circuit case, for `k=floor((1/2)log2(s2))` and `beta<2/3`, a high completion can concentrate all its `Omega(s2/n)` disagreements inside one signature cell. Thus C-224 does not imply many mixed cells or a count-of-cells lower bound. Its addition is the explicit approximation-error term `e` and the residual circuit-size inequality; the global selector/state-sharing problem remains.

Consequently, if `CC(z)>=s2`, then
\[
  r+O(k2^k+(e+m)n)\ge s2.
\]
More precisely, fixing constants in the `O` notation, every high `z` satisfies `e+m >= (s2-r-c1*k2^k)/(c2*n)` whenever the numerator is positive. This is an `Omega(s2/n)` bound when `r+c1*k2^k <= s2/2`; with a smaller margin, only the corresponding residual gap is forced. If a good signature cell contains both `z`-values, it supplies a pair `x,y` with `sigma(x)=sigma(y)`, `z(x)\ne z(y)`, and `w(x)=w(y)`; the last equality follows because the signature contains `C`'s output and both addresses are good. Thus approximation errors are the exact escape hatch from the C-115 within-fiber mismatch witness.

In particular, to force a nonzero fiber-variation alternative using this lemma, an approximate learner would need `r+c1*k2^k+c2*e*n<s2`. To force `m=Omega(s2/n)`, leave a constant fraction of the `s2` budget after paying `r+c1*k2^k+c2*e*n`. Since `e<=epsilon N`, the natural error scale is `epsilon < s2/(N n)=N^(beta-1)/n`, with a constant-factor margin, along with `r+k2^k` below `s2`. Merely learning to error `1/poly(n)` is far too inaccurate for this purpose at fixed `beta<1`.

## 3. Why this still does not charge shared DAG states

The lemma is per selected circuit and per selected signature. To use it as a C-75 DAG lower bound, one still needs to produce or identify those circuits/signatures from the low table and then prove that the resulting within-fiber obligations cannot be routed through shared product rectangles. A randomized learner that queries `w` and uses a separator as an oracle does not give a small circuit selector: its runtime/output circuit can be much larger than the DAG whose size we are trying to bound, and the lemma has no cross-history product-hull charge.

There is also a polarity/model distinction. `D=1-h` is a large separator-derived property, but the C-75 relation is search for a mismatch on `Y x Z`. Natural-property learning reconstructs a low target approximately; C-75 needs a shared DAG that routes every promised pair to an actual differing address. No cited theorem converts the former task to the latter with a near-linear or subcubic size loss.

## 4. Disposition and live frontier

**Proved:** the approximate-fiber circuit bound above. It precisely quantifies the tradeoff between a circuit's errors and residual variation inside its signature fibers.

**Route filter:** the natural-property idea does not currently improve the shared-DAG/fusion transfer. Its direct use has a uniformity mismatch; even under a uniformity strengthening it supplies approximate learning, not a DAG compiler or lower bound. Approximate learning only feeds the local lemma if its error count satisfies `e n < s2-r-O(k2^k)`.

The C-75 transfer chain is unchanged:
\[
  \rho_{\rm prom}\le O(S_{\rm rect}),\qquad
  S_{\rm rect}=O(q^3/\log q)
\]
for the best recorded generic compiler from a `q`-pair fusion cover. The active goal remains O-141: either charge product-hull-safe residual separator reuse across arbitrary acyclic rect-DAG states strongly enough to beat `N^(3+3epsilon)/log N`, or construct a near-linear separator for the full low/high promise. C-224 yields neither result.
