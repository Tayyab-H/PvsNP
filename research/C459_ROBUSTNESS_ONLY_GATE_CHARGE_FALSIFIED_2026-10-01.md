# C-459 — Robustness alone cannot charge shared gates

**Date:** 1 October 2026  
**Question:** Does the Hamming-neighborhood formulation from C-458 itself force superlinear ordinary circuit size?  
**Result:** No. A linear-size counterexample shows that the two forced-radius conditions, even with the same radii, contain too little information. C-458 remains a correct promise lemma; retire it as a standalone lower-bound mechanism.

## 1. Candidate mechanism under attack

C-458 proves that changing `r` truth-table entries changes circuit complexity by at most `K r(n+1)`. Thus any OPS separator accepts a radius

```text
rL = floor(s1/(4K(n+1)))
```

ball around every table of complexity at most `s1/2`, and rejects a radius

```text
rH = floor(s2/(2K(n+1)))
```

ball around every table of complexity at least `2s2`. The proposed hope was that these robust obligations might themselves constrain the number of gates.

## 2. Counterconstruction: two separated Hamming balls

Consider a different partial Boolean function on `{0,1}^N`. Its YES set is `B_{rL}(0^N)` and its NO set is `B_{rH}(1^N)`. For all sufficiently large `N`, `rL+rH<N`, so the sets are disjoint. The total circuit

```text
H(x) = [weight(x) <= rL]
```

accepts every YES point and rejects every NO point. A binary population counter and comparison use `O(N log N)` fan-in-two AND/OR/NOT gates.

This promise has exactly the same two Hamming radii and the same `N` input coordinates as the forced-neighborhood information in C-458, yet its extension complexity is at most `O(N log N)`. Therefore no argument that uses only these radii, their volumes, separation of centers, or the count of forced local repairs can prove a superlinear OPS lower bound. The obstruction is the missing structure of the *entire* circuit codebook and how neighborhoods of its many centers overlap.

The counterexample is to a proposed generic lower-bound mechanism, not to Gap-MCSP. It says nothing about the true minimum circuit size of a full OPS separator.

## 3. Stronger calibration from the actual promise

C-457 already supplies a sharper warning on the actual Low/High labels: an `O(N log N)` circuit is sound against every High table, has every table input essential, and accepts sparse/co-sparse Low tables plus a full low-degree Reed-Muller family. It still misses the `O(n)`-gate Low function that ANDs `d+1` disjoint pair parities. Thus even actual-High soundness and several rich Low families do not force the needed computation. This report adds the precise point that C-458's *robust geometry by itself* cannot be the missing gate charge.

Parity, repeated-block equality, sparse parity checks, and simple global block relations remain tests against local interaction counts: each has an `O(N)` shared readout when its total representation is linear. They are not counterexamples to an OPS separator lower bound.

## 4. Literature/source-route check

The recent Ren–Williams near-maximum lower bound for `E^{prMA}/1` was already audited in C-437–C-442. Its smart Range Avoidance reconstruction is a real near-maximum source, but the project has no exact map from its verifier queries to Low/High explicit tables. The obvious verifier table is Low on both outcomes, and oracle-query substitution has only a proved serial upper bound, not a small joint compiler. The new audit finds no missing transfer in that route. [Ren–Williams, ECCC TR26-118](https://eccc.weizmann.ac.il/report/2026/118/download)

OPS Theorem 1.4 still has the common-fixed-`epsilon`, every-sufficiently-small-fixed-`beta` quantifiers; the required conclusion is `NP not subseteq P/poly`. The locality barrier remains method-specific, not a universal no-go. [OPS](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), [Chen et al.](https://eccc.weizmann.ac.il/report/2019/168/download)

## 5. Research decision and exact frontier

Retire the claim that robust-ball geometry, center counts, or patching cost can by themselves yield a superlinear total-gate bound. Keep C-458's robustification as a useful semantic fact. Any replacement must use a property of the full Low-circuit codebook—particularly interactions or overlap among neighborhoods—and then prove its growth under every AND/OR/NOT gate with unrestricted fanout. Do not assume centers are independently charged.

**Strongest statement:** C-458's patching inequality and its robust-neighborhood containment remain proved; C-459 proves those generic neighborhood constraints admit an `O(N log N)` circuit in an unrelated promise.  
**Paired full-promise upper:** exact circuit-description enumeration remains `O(N*2^(O(N^beta)))`.  
**Quantitative effect:** none. The ordinary lower bound remains `N-O(N^beta log N)` plus C-406's additive logarithmic reconvergence refinement; the OPS exponent target, native `rho>=N-o(N)`, and `P != NP` remain open.
