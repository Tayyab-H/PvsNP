# C-273 - Recent monotone example hardness: the direct LowExt encoding has the wrong rail order

Date: 27 September 2026  
Classification: **ROUTE-KILL (direct example-list encoding only); POSITIVE CALIBRATION for the NO side.**  
Route: A, monotone lower bounds transferred to exact unrestricted-circuit LowExt.

## Candidate source and exact promise

Cavalar, de Rezende, Gray, and Santhanam (arXiv:2607.12331, submitted July 2026) prove rETH-hardness for learning monotone formulas/circuits and approximating monotone circuit size from labelled examples. Their partial-gap problem receives `m` examples `(x_i,b_i)`, where `x_i` has `d` bits. In the YES case, a small monotone formula fits every example. In the NO case, every small monotone circuit disagrees on a constant fraction of the sample. Their reduction is randomized from a sampler-circuit problem, and the hardness is conditional on rETH.

This appears relevant because C-125 transfers a hard monotone promise function through a monotone map into signed truth-table rails. The exact one-hot order in C-125 is asymmetric:

```text
YES: e(w) <= phi(x) for some w in SIZE(s1)
NO:  phi(x) <= e(z) for some z outside SIZE(s2).
```

## What the example list does give

For a consistent example list, write `P` for the set of signed rails specifying its labels. If a circuit `w` fits all examples, then `P <= e(w)`: the sample constraints are a *partial lower code*, and a completion lies above them. Thus the natural sample encoding has the reverse order from C-125's YES condition `e(w) <= phi(x)`.

The NO-side high completion is not the problem. If `m` distinct table positions are specified in an `N=2^d`-entry table, the list has `2^(N-m)` completions. In the OPS regime,

```text
log2 |SIZE(s2)| = O(s2 log N) = O(N^beta log N) = o(N),
m = poly(log N) = o(N).
```

So every consistent polynomial-size example list has many completions outside `SIZE(s2)`. This is a useful calibration: sparse examples can supply the C-125 NO-side high completion by counting. The fact that they also have a small unrestricted interpolant does **not** invalidate C-125, which only needs a high completion on NO inputs and does not require that NO images have no low completion.

## Exact failure of the direct encoding

The unmodified partial-example vector `P` cannot serve as `phi(YES)`: its fitted low code satisfies `P <= e(w)`, whereas the transfer needs `e(w) <= phi(YES)`. One might reverse the order by using the vector that contains every completion of the partial sample: at each specified location it retains the sample's rail, and at each unspecified location it contains both rails. This does put every completion code below that vector, but it cannot also lie below any one-hot high code `e(z)`, because the two opposite rails at each unspecified location are both present.

Therefore these two standard sample encodings do not provide the *same monotone map* with the C-125 YES and NO order. A more elaborate map might switch from lower to upper information as the source input changes, but it must compute those rail activations monotonically from the hard source and have AND cost below its cyclic lower bound. The cited work does not give such a map: its source is SAT/sampler hardness under rETH, not the unconditional monotone matching promise, and its sample-generation reduction is not an AND-costed monotone rail map.

## Disposition and surviving idea

Retire only the direct sample-list-to-rails encoding. Keep the new structural hint: the NO completion condition can be discharged by entropy for sparse consistent sample sets, while all nontriviality must be carried by the YES upper-code condition and by source-monotone computation of the rails. A next attempt should seek a monotone map that turns a YES witness into a rail *superset* of its low one-hot code while keeping every NO rail vector below at least one high completion; it must explicitly handle the tension at unspecified coordinates and preserve the exact AND-cost accounting.

No matching-to-LowExt map has been constructed. The actual fusion lower bound remains `q=N-o(N)`; this is not a P-vs-NP result.

## Audit correction retained for future attempts

An initial draft treated the existence of a low unrestricted interpolant for a sparse NO sample list as disqualifying. That inference was wrong: C-125 only asks for a high completion above a NO rail vector, and it permits that vector to have low completions too. Counting actually shows high completions are abundant. Keep the real failure at the one-hot order and the absence of a source-monotone rail map; do not reintroduce the stronger, false requirement that NO images have no low completion.

## Source

- Cavalar, de Rezende, Gray, and Santhanam, [*ETH-Hardness of Learning Monotone Circuits and Approximating Their Size*](https://arxiv.org/abs/2607.12331), especially Definitions 4.1 and 4.7, Theorem 4.8, and Corollary 4.9. It establishes conditional hardness for monotone agreement on examples, not the C-125 rail map.
