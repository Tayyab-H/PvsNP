# C-317 - Blockwise safe cylinders saturate the global splice entropy

Date: 28 September 2026  
Route: Q177 / C-281 native direct-sum and owner-mask coherence.  
Classification: **EXACT SAFE-CYLINDER CALIBRATION; NO q BOUND.**

## 1. Question

C-315 leaves open whether `k=Theta(log N)` prefix blocks force a direct-sum charge in the native closure. Before trying to charge k independent pieces, test the strongest simple splice statistic: how many table coordinates can vary independently inside a sound completion cylinder while each prefix block contributes its own local circuit?

Let `N=2^n`, `s2=N^beta` for fixed `0<beta<1`, and partition the addresses by `r=ceil(log2 k)` prefix bits into `k=2^r=Theta(n)` blocks. Each block has `n_b=n-r` remaining address bits. Set

```text
t = alpha*s2/k
```

for a sufficiently small constant `alpha>0`.

## 2. Product-subcube construction

Choose an integer `u<n_b` so that

```text
2^u = Theta(t*log t),
```

with the implicit constant small enough for Lupanov synthesis. In each prefix block `a`, fix all but a common `u`-dimensional subcube of its suffix addresses. Let `F_a` be those `2^u` table coordinates, and let `F=disjoint_union_a F_a`.

For every arbitrary labeling of `F`, define the full truth table to equal that labeling on `F` and zero outside `F`. On block `a`, its restriction is zero outside `F_a` and is an arbitrary Boolean function of the last `u` address bits on `F_a`. Lupanov synthesis computes the arbitrary local function in `O(2^u/u)` gates; testing the fixed prefix and suffix pattern costs `O(n)`. A prefix multiplexer over all blocks therefore gives

```text
CC(w) <= O(k*n + k*2^u/u) <= s2
```

for a small enough fixed `alpha`; here `k*n=O(n^2)=o(s2)` for every fixed beta. Thus the entire partial-assignment cylinder leaving the coordinates F free is sound, and

```text
|F| = k*2^u = Theta(k*t*log t)
     = Theta(s2*log(s2/k))
     = Theta(s2*log s2).
```

The final equality uses `k=Theta(log N)` and fixed beta, so `log(s2/k)=Theta(log s2)`. The same free coordinates are distributed across every one of the k blocks, with `Theta(t log t)` independent bits per block. Hence this is not merely C-230's one-block safe cube relocated: it is a product of k independently variable local subcubes, and every combined labeling still has one global circuit of size at most `s2`.

## 3. Exact consequence for C-281 splices

Every completion of this support is in `SIZE(s2)`. Consequently, a state/context argument cannot derive an unsafe owner-mask hybrid merely from having independent choices in all k blocks unless those choices exceed `Theta(s2 log s2)` in total or the argument uses additional information about how the grammar selects them. In particular:

1. counting blockwise switches up to `Theta(s2 log s2)` is compatible with soundness;
2. dividing the switch count by k does not create a new per-block obstruction, since `Theta((s2/k) log(s2/k))` choices per block tensorize safely;
3. C-281's full-cylinder soundness condition already permits this product family, so a proposed q-sensitive direct-sum law must measure circuit-description synchronization, not just the number of independent table coordinates exposed by compatible joins.

The scale is tight up to constants: circuit counting gives `kappa_square(s2)<=log2|SIZE(s2)|=O(s2 log(s2+n))`, while the construction above gives a safe cylinder with `Theta(s2 log s2)` free coordinates. This agrees with C-230, but identifies a blockwise product realization of the extremal scale.

## 4. C-315 counting yields a distributional refinement, not a direct-sum theorem

The C-315 product family of moderately hard local blocks has size greater than `|SIZE(s2)|` once its fixed constants are chosen with a margin. Therefore, for uniform independent block choices from that family,

```text
Pr[assembled table belongs to SIZE(s2)]
  <= |SIZE(s2)| / |F'_u|^k
  <= 2^(-Omega(s2*log N)).
```

So independent local block choices are globally high with overwhelming probability, even though every local restriction has complexity between fixed multiples of `s1`. There is also a large correlated diagonal subfamily: if every block repeats the same local function g, the assembled table ignores its prefix and has global circuit complexity `O(CC(g)+n)`. For `CC(g)=Theta(s1)`, this is far below `s2` even though every block has the same locally moderate complexity.

This pair of facts pinpoints the missing distinction. Local hardness does not add under arbitrary correlation; independent choices usually escape every size-`s2` global description, while a shared block description can compress all blocks at once. Any usable reduction must force enough *description independence* on the hard side and track how a native q-state grammar distinguishes it from shared-description correlations. Cardinality establishes the distributional gap but does not show that the grammar pays k separate costs.

## 5. Literature boundary

Paul's theorem gives arbitrarily complex vector-valued switching functions whose two disjoint copies have combinational complexity at most `(1+epsilon)` times the one-copy complexity. This confirms that variable-disjointness alone cannot justify generic circuit additivity. The theorem concerns unrestricted combinational complexity and multi-output composition, not the present signed-literal monotone AND-count or C-281's compatible-support least-fixed-point grammar. [Paul 1976, publisher record and abstract](https://www.sciencedirect.com/science/article/pii/030439757690089X).

Find, Göös, Järvisalo, Kaski, Koivisto, and Korhonen prove a direct-sum-type result for monotone OR/SUM circuit complexity of tensor-product Boolean matrices. Its structured linear-map setting suggests a possible algebraic model for block composition, but it does not cover nonlinear promise separators or compatible-support products. A transfer would need an explicit representation of the C-281 grammar as the relevant matrix/tensor computation. [Find et al. 2013](https://arxiv.org/abs/1304.0513).

There is a specific obstruction to treating that representation as automatic. A C-281 endpoint is an arbitrary subset of the full high-table universe and may couple all blocks in one global predicate. The parity-lock construction C-257 uses prefix-parity carriers and has a `4N-4`-rule cover; those carriers are not products of independent block predicates. Thus any tensor-product theorem would currently apply only to a restricted block-factorized endpoint grammar. To use it for unrestricted q, one must either prove a semantics-preserving factorization for Gap-MCSP covers or quantify how the grammar pays for nonfactorizing global couplings. C-257 rules out simply assuming such factorization.

## 6. Disposition and next obligation

**Proved:** the safe-cylinder dimension `Theta(s2 log s2)` can be realized as a product of independent free subcubes across all `Theta(log N)` blocks; independent moderately hard blocks are globally high with overwhelming probability after the C-315 constant calibration; perfectly correlated repeated blocks can remain globally small.

**Not proved:** a direct-sum law for local MCSP separators, a q-sensitive native lower bound, a shared selector, a near-linear full-promise cover, or any improvement over `rho_GapMCSP=N-o(N)`.

Retire the specific proposal to charge q from blockwise free-coordinate count or raw product entropy. Keep Q177 open only for a description-coherence theorem that distinguishes independent block descriptions from shared/global circuit descriptions and controls every compatible C-281 splice. It must still pass the parity and repeated-equality calibrations. No P-vs-NP conclusion follows.
