# C-473 — First-principles reset: the missing object is shared codebook recognition

**Date:** 1 October 2026  
**Status:** cumulative assessment through C-472, with a more precise candidate object for the next construction/lower-bound cycle. This adds no new asymptotic lower bound and does not claim a breakthrough.

## 1. The exact problem

Let `N=2^n`, fix `0<beta` sufficiently small, and use the OPS thresholds

```text
s1 = floor(N^beta/(10 n)),   s2 = floor(N^beta)
L_t = {T in {0,1}^N : CC_n(T) <= t}.
```

A total ordinary fan-in-two AND/OR/NOT circuit `F` is a valid separator exactly when

```text
L_s1 subseteq F^(-1)(1) subseteq L_s2.
```

The middle band is free. The research quantity is the minimum total number of gates over **all** such extensions. The OPS target is one fixed `epsilon>0` for every sufficiently small fixed `beta>0`, with this minimum greater than `N^(1+epsilon)` (up to the paper's rounding conventions). OPS show this would imply `NP not subseteq P/poly`; that is stronger than `P != NP`, and the implication is a sufficient magnification route, not an equivalence. The exact theorem and constants are audited in C-463 and the primary OPS citation there.

## 2. What the project has established

The work through C-472 is substantial as a set of proof audits and falsification tests, but has **not moved the quantitative frontier**.

| Track | Strongest retained result | Why it does not settle the target |
|---|---|---|
| Ordinary-gate lower bound | Near-linear input-dependence/gate floor `N-O(N^beta log N)`, with C-406's logarithmic reconvergence refinement. | There are only N table inputs. The known argument charges access/dependence; it does not price the post-read shared computation. |
| Complete separator upper bound | Exact low-description enumeration, `O(N*2^(O(N^beta)))` total gates. | It checks candidates separately; no compression of the full low-circuit codebook is proved. |
| Sound partial separators | C-457 and C-472 give `O(N polylog N)` recognizers for large structured Low families and reject every actual High table. | They omit Low tables. C-472 specifically rejects the Low function `AND` of `m+1` independent parities. Soundness over a subfamily is not completeness over `L_s1`. |
| Shared-computation calibrations | Parity, repeated-block equality, sparse parity checks, simple global block relations, and the C-470 repetition-code neighborhood all admit linear-scale shared checks. | Local incidence, many repairs, support, radius, and anchor count do not alone force extra gates. These examples do not refute a full separator lower bound. |
| Source and model transfers | Several exact composition, endpoint, and parameter audits; comparator/native bounds remain meaningful in their own models. | No source map has both exact OPS endpoints and a charged total cost leaving the common fixed-epsilon margin. No ordinary-DAG compiler supplies the missing transfer. |

The C-471/C-472 Fourier work is a useful positive calibration: a global transform plus a Parseval certificate gives a real near-linear sound recognizer, including robustness, without reconstructing a circuit description. Its failure is also informative: a compact invariant that recognizes only one family of circuit forms does not satisfy the universal Low endpoint.

## 3. The first-principles diagnosis

There are four different proof jobs here; conflating them caused many apparent cycles of progress to repeat the same missing step.

1. **Direct extension lower bound.** Prove a superlinear total-gate lower bound for every `F` in the sandwich above, with arbitrary fan-out and arbitrary middle labels. A proposed potential must be defined on the actual DAG, have a proved change bound for each gate despite reuse, and have a superlinear value forced by the two endpoints.
2. **Complete construction.** Build one small circuit that accepts every low-circuit table and rejects every high-circuit table. A fast recognizer for selected Low families does not address this.
3. **Hard-source transfer.** Map both sides of a source promise to the correct OPS sides and prove `source hardness > generator + separator + decoder + postprocessor`. Hard witnesses, descriptions, or query transcripts do not imply that their table outputs are High.
4. **Model transfer.** Any formula, local-query, monotone, comparator, or native-state result needs a proved cost-preserving compiler to unrestricted ordinary circuits. A `q^2` paid-state bound does not count all gates unless the compiler does.

Most explored scalar statistics—support, degree, rank, sensitivity, local certificates, Hamming volume, and one-cut communication—reach a linear scale or admit a small shared counterexample. Their common defect is not that the statistic is false; it is that it forgets the interaction among the whole Low codebook, the whole High region, and a reusable gate DAG. The locality barrier and natural-proofs results constrain specific methods. They are not universal impossibility theorems.

This is the key pushback: the record does **not** point to one overlooked elementary identity that can be forced into a proof. The requested fixed-epsilon OPS bound itself implies a major nonuniform class separation. First-principles work can identify the missing theorem and reject invalid shortcuts, but logic alone does not make that theorem follow from ZFC axioms by exhaustion or contradiction.

## 4. A sharper object: robust proximity to the circuit codebook

Let `d_s(T)=min_{C in L_s1} dist_H(T,C)`. Address patching gives a universal constant `K` such that

```text
CC(T) <= CC(C) + K (n+1) dist_H(T,C).
```

Consequently, with

```text
r = floor((s2-s1)/(2 K (n+1))),
P_r(T) = 1 iff d_s(T) <= r,
```

every `T in L_s1` is accepted and every `T` with `CC_n(T)>s2` is rejected: if `d_s(T)<=r`, patching a nearest Low table would give `CC_n(T)<s2`. Thus `P_r` is a valid **complete** extension. This is a clean common object behind robust balls and the codebook viewpoint.

The proof is elementary and its limits are important:

- Enumerating the `M=2^(O(s1 log(n+s1)))=2^(O(N^beta))` Low descriptions and checking Hamming distance costs `O(N log N * M) = O(N*2^(O(N^beta)))` gates, matching the current upper scale.
- A generic random sample does not compress this check. A High table differs from each Low table on at least `r` positions, a fraction about `N^(beta-1)/poly(n)`. A union bound over `M` descriptions needs on the order of `(N/r) log M = Theta(N poly(n))` sampled addresses even to hit every candidate's disagreement set; this gives no sublinear address test, and testing each candidate still has its own computation cost.
- The C-470 detector proves that proximity to a large structured subcode can be recognized in `O(N)` gates. It does **not** recognize proximity to the union of every size-`s1` circuit table.
- Hardness of `P_r` alone would only lower-bound this particular extension. It would not lower-bound the minimum over all valid extensions, because another extension may label the middle band differently.

So this is not a new lower-bound theorem. It is a more exact paired research target: (a) try to compress robust codebook proximity; (b) separately prove extension-hardness for all possible middle-band labelings. A construction on (a) could overturn the proposed lower-bound target. A proof on (b) would establish the desired result.

## 5. What the counterexamples teach us to demand next

Any next mechanism should be written as a theorem candidate with all three items present **before** its proof is expanded:

```text
Object:      a precise quantity or source map for the actual promise.
Gate rule:   an inequality charging every allowed AND/OR/NOT gate under arbitrary reuse,
             with wires, description bits, runtime, and native paid states kept separate.
Endpoint:    a proved superlinear value for every valid total extension,
             or a complete circuit for every promised YES and NO input.
```

Then attack it immediately with:

- parity and functions of a few global linear forms;
- repeated-block equality and repetition-code neighborhoods;
- sparse parity-check systems;
- blocks generated by simple global relations;
- an arbitrary post-read decoder after an `O(N)` identity/copy front end;
- the actual middle-band freedom.

The canaries falsify a mechanism only when they satisfy its stated premises and violate its conclusion. An easy structured recognizer is not a counterexample to a theorem about all separators; an omitted Low function is fatal to a claimed full separator.

## 6. The next productive research cycle

Use **robust circuit-codebook proximity** as the construction-side target, not as a disguised lower-bound assumption. Attempt a concrete compression using shared computation across candidate circuit descriptions. Every proposed shortcut must account for candidate routing, address selection, all table comparisons, and fan-out. If it fails, name the missing compression step and do not merely count more anchors or refine the same distance bound.

In parallel, the only acceptable direct lower-bound lead is a promise-forced operation-wise potential or a proved source reduction. C-472's Fourier-DAG identities are a representation to investigate only if they produce a gate inequality for arbitrary compositions; convolution is not free and the separator need not reconstruct a source circuit. If no such inequality appears, retire that route rather than describing its missing inequality as “non-shareability.”

## 7. Exact frontier and originality

**Frontier unchanged:** ordinary lower bound `N-O(N^beta log N)` with C-406's refinement; complete upper `O(N*2^(O(N^beta)))`; OPS common-fixed-epsilon lower bound open; native `rho_GapMCSP >= N-o(N)` separate; no P-vs-NP proof. C-473 is an integrative audit and a reformulation of C-458/C-463, not an asymptotic theorem or literature discovery. No numerical tests were run because the relevant claim is asymptotic and the request was a first-principles evaluation.

