# Frontier checkpoint after C-396

Date: 29 September 2026

## Required five-part checkpoint

| Front | Status after C-396 |
|---|---|
| Native quantitative bound | **Unchanged.** The proved full-promise C-319 state lower bound remains `q>=N-o(N)`. No superlinear lower bound or `N^(1+o(1))` full-promise construction is known. |
| Hard-core selector | **Still open.** C-392 handles `1-o(1)` of random sparse supports only. There is no all-high selector and no lower bound for every selector. |
| Selector/native bridge | **None.** No size-controlled reduction transfers selector synthesis or lower bounds to arbitrary valid C-319 covers. |
| Collectively hard low subclass | **None.** No individually easy but collectively hard low family with an OPS-preserving native transfer has been established. |
| Local-seed LFP readout | **New structural restriction, no cost lower bound.** C-395/C-396 prove promise-specific AC0 lower bounds, and the C-393 compiler then forces `k=Omega(log N/log log N)` escape-source carriers in every polynomial-size valid cover. There is still no lower bound on `A_cap` or q from this k bound. |

## What changed

C-395 handles the gap promise's unrestricted middle interval directly: a locally computable restriction has a low zero-star completion, and counting guarantees a completion above `s2`. C-396 applies CKLM Lemma 31 in its all-depth form to extend the separator contradiction to depths up to a small constant times `log N/log log N` at polynomial size. Composing with C-393 gives a quantitative lower bound on the number of distinct one-sided escape-source carriers.

The result excludes bounded and sub-`log N/log log N` escape-source macro-round counts in polynomial-size covers. It does **not** exceed the linear state-count barrier: the forced diversity is compatible with `q=Theta(N)`, and C-393 is an upper compiler. Do not reverse it into a paid-AND lower bound.

## Next proof obligation

Either derive a representation-independent state/readout charge from the forced escape-source diversity, or construct a valid near-linear full-promise cover that realizes it cheaply. Preserve the common-description/address requirement and C-258 repeated-equality calibration. Do not restart raw certificate-width, safe-cone count, or selector-only arguments without a transfer. The overall P-vs-NP goal remains active; no breakthrough has been obtained.
