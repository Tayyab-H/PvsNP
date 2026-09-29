# C-330 — Derandomized sunflowers do not reopen the C-327 transfer

Date: 28 September 2026  
Route: bounded-independence matching source; audit of ECCC TR26-220.  
Classification: **USEFUL HYPOTHESIS CHECK; NO SOURCE OR ENCODER GAIN.**

## Question

Does Cavalar–Fabris–Mukhopadhyay–Srinivasan–Yehudayoff, “Derandomized Sunflowers and Radical Lower Bounds” (ECCC TR26-220, 28 September 2026), let the C-327 almost-independent matching source retain the C-310 one-sided approximation at independence order O(log N), or otherwise create a positive C-125 map?

## Exact hypothesis in the new theorem

Theorem 1.1 concerns a width-W monotone DNF F under a distribution D whose every marginal on at most k coordinates is a convex mixture of product distributions. In each product component, each coordinate has bias within a relative ε of a common marginal q. If F has size at least (W/q · log(1/δ))^W, then parameters k=O(W log(1/δ)) and ε=Ω(1/W) suffice for a robust sunflower under D. The proof uses high moments, not a claim that D fools every DNF. The paper applies this to monotone arithmetic radical separations; it does not discuss C-125 maps or the native fusion measure. [Official ECCC report](https://eccc.weizmann.ac.il/report/2026/220/).

## Why edge variables do not satisfy the hypothesis

There are two direct failures.

1. Under the odd-cut distribution D0, edge indicators come from equalities of vertex colors. On a four-cycle, the XOR of its four edge indicators is always zero. The marginal on those four edge variables has zero mass on half of the Boolean cube. A mixture of product Bernoulli distributions with all biases strictly between zero and one has full support, so this marginal is not of the required form.
2. Under the uniform perfect-matching distribution D1, two incident edges are mutually exclusive. If q=1/v is their marginal, then Pr[e1=e2=1]=0. In any allowed product-mixture with ε<1, this probability is E[p1p2]≥(1−ε)^2q^2>0. Thus even the two-edge marginal fails the exact product-mixture condition.

Consequently the theorem cannot be applied directly to the C-310 matching DNF over graph-edge variables. This is a structural mismatch, not just a choice of k.

## Vertex-color lift and parameter check

The C-310 matching-sunflower proof first makes a family of matchings blocky and then applies a robust sunflower argument to their endpoint sets. The associated event is a monotone DNF in vertex-color bits, so an exactly k-wise independent color distribution would meet the new theorem’s local hypothesis (away from the global odd-parity condition, which can be imposed by an affine k-wise-uniform sample space when k is below the number of vertices).

That lift does not improve the needed matching bound. An ℓ-edge matching becomes an endpoint set of width at most 2ℓ. At q=1/2, Theorem 1.1’s size threshold is of order (W log(1/δ))^W, which is weaker here than the matching-specific bound (cℓ log²(ℓ/δ))^ℓ already used in C-310. Moreover C-310 takes δ at approximately v^(−10w), so the theorem’s independence order is k=O(w log(1/δ))=O(w² log v), not O(log N). At v=(log N)^K this order is still polylogarithmic for fixed K, but it does not meet C-327’s specified logarithmic-order target.

The new theorem could derandomize the vertex-color side of a future variant. It does not control the large-width tail under a k-wise permutation family on D1: preserving each matching-term probability through width k does not bound probabilities of wider terms or the union of those terms. The original C-310 proof already has exact uniform D0 and D1 distributions, so replacing either distribution by a succinct one is not itself a lower-bound improvement.

## Disposition

The C-327 parameter audit remains closed as specified. TR26-220 provides a useful future tool for robust sunflowers under local pseudo-independence, but its edge-variable hypotheses fail here; its vertex-color lift has weaker matching parameters and requires independence order above O(log N); and it supplies no new all-input CohEnc architecture. The C-310 ODDFACTOR reconstruction lower bound and the native bound q=N−o(N) are unchanged. No positive transfer or P-vs-NP result follows.

Primary comparison: Cavalar et al., [“Monotone Circuit Complexity of Matching,” ECCC TR25-102](https://eccc.weizmann.ac.il/report/2025/102/revision/1/download), supplies the matching-specific sunflower bound used by C-310. The new paper’s exact local-pseudorandomness statement is in Theorem 1.1 of [TR26-220](https://eccc.weizmann.ac.il/report/2026/220/).
