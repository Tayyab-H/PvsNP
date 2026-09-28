# C-318 - Prefix restrictions are an ensemble circuit, and native fusion is lane-wide

Date: 28 September 2026  
Route: Q177/Q179; cofactor-description coherence and C-281 compatible products.  
Classification: **EXACT MODEL REFORMULATION; NO q BOUND.**

## 1. Cofactor-vector model

Split the `n` input bits of a truth-table function into an `r`-bit prefix `a` and an `m=n-r`-bit suffix `y`. Let `k=2^r`, and write the k block restrictions as

```text
F(y) = (f_a(y))_{a in {0,1}^r},    f_a(y)=f(a,y).
```

Define `V_k(F)` as the minimum number of gates in a vector Boolean circuit that computes all k outputs simultaneously under these rules:

- each wire carries a k-bit vector;
- suffix input `y_j` is supplied diagonally as `(y_j,...,y_j)`;
- each prefix input is supplied as its fixed k-bit lane-mask listing that bit across the k prefix strings;
- scalar constants `0` and `1` are supplied diagonally as `0^k` and `1^k`;
- AND, OR, and NOT gates act coordinatewise and each vector gate costs one.

The vector circuit is the **cofactor ensemble** of one scalar truth-table circuit. It is not k independent copies: a single gate simultaneously updates all prefix restrictions.

## 2. Equivalence to global circuit size

For the standard fan-in-two basis with NOT gates counted and matching constants,

```text
V_k(F) = CC(f).
```

**Scalar-to-vector.** Take a scalar circuit for `f(a,y)`. Replace each suffix input by its diagonal k-vector, each prefix input by the fixed lane-mask listing that input bit across all prefixes, and each scalar gate by its coordinatewise vector gate. By induction through the DAG, the output vector is exactly `(f(a,y))_a`. This uses one vector gate per original gate.

**Vector-to-scalar.** For each vector wire v, form the scalar wire `v_a` by selecting the lane indexed by the scalar prefix input a. A diagonal suffix input becomes `y_j`; the fixed prefix mask for bit i becomes scalar input `a_i`; and coordinatewise AND/OR/NOT become the corresponding scalar gate on the selected lane. Induction through the vector DAG gives the same gate count and output `f(a,y)`.

Thus the C-315 global MCSP question on prefix blocks is exactly a **shared cofactor-ensemble circuit complexity** question in this SIMD model. The local sum `sum_a CC(f_a)` is only the cost of computing every lane independently. It can exceed `V_k(F)` greatly when the restrictions share one circuit description. This ensemble is more structured than an arbitrary multi-output Boolean function: its lanes are precisely the restrictions obtained by fixing prefix inputs of one scalar function.

## 3. Two exact calibrations

### Shared diagonal

If every block is the same function g, then `F(y)=(g(y),...,g(y))` has `V_k(F)<=CC(g)` by computing g once and broadcasting its output. The scalar global table ignores the prefix and has size at most `CC(g)+O(1)`, although the independent-copy budget is k times the local cost. This is the repeated-equality/shared-description mechanism in circuit form.

### Independent moderate-hard blocks

The C-315 family `F'_u` supplies local functions with complexity in `(B*s1,A*s1]`. Choose its constants so `|F'_u|^k>|SIZE(s2)|` by a factor `2^(Omega(s2 log N))`. For a uniform tuple `F in (F'_u)^k`,

```text
Pr[CC(f)<=s2] <= |SIZE(s2)|/|F'_u|^k
                 <= 2^(-Omega(s2 log N)).
```

By the exact equivalence above, all but that fraction of these cofactor ensembles have `V_k(F)>s2`. This is an exact distributional statement about shared cofactor-ensemble circuit complexity. It does not imply that a particular separator or native closure spends k separate operations: the ensemble circuit is allowed to reuse gates across every lane.

## 4. Native fusion in the same lane language

Partition a C-281 support by prefix blocks:

```text
S = (S_1,...,S_k),
```

where `S_a` is a consistent partial assignment to the table coordinates in block a. A state is an antichain/family of such support vectors. Alternative proofs use family union. A paid fusion state combines two families by the single operation

```text
A * B = Min{ (S_1 union T_1,...,S_k union T_k) :
              S in A, T in B, and every lane-wise union is consistent }.
```

If any coordinate conflicts in any lane, that pair contributes zero; otherwise one rule has joined the entire k-lane support vector. So the native grammar is also SIMD across the prefix blocks. The direct-sum proposal `q_global >= k*q_local` is not built into the semantics: one paid state can join all k lanes at once, while the compatible-product filter may remove cross terms.

The source-side SIMD circuit and native-side SIMD support grammar are not the same algebra. The first computes a vector of Boolean functions using coordinatewise Boolean gates. The second computes families of partial assignments using idempotent union and compatibility-filtered support join. The missing theorem is a lower-bound-preserving bridge between them, or a direct lower bound for the native SIMD grammar on the Gap-MCSP cofactor ensemble.

This gives an exact reindexing of the promise as a **cofactor-SIMD interpolation cover**. Let `E_s={F:V_k(F)<=s}`. A support vector `S=(S_a)_a` defines the box `B_S=product_a [S_a]` of all cofactor ensembles extending its local partial tables. Native soundness is exactly `B_S subseteq E_s2`; completeness requires every `F in E_s1` to lie in some generated box. The q-state grammar generates a family of such boxes using alternative family union and the compatible product above. This is a coordinate reindexing of the original cover problem, not a complexity reduction, but it states the comparison target without conflating k independent scalar separators with one global separator.

## 5. Why available direct-sum theorems do not close the bridge

The literature calls the simultaneous computation of multiple Boolean functions **ensemble computation**. Järvisalo, Kaski, Koivisto, and Korhonen study minimum circuit synthesis for multiple outputs, including monotone OR/SUM variants, and give SAT encodings for finite instances. That terminology matches `V_k(F)`; the paper does not prove the needed asymptotic lower bound for these MCSP cofactor ensembles or for native support grammars. [Järvisalo et al., SAT 2012 paper](https://www.cs.helsinki.fi/u/mjarvisa/papers/jarvisalo-kaski-koivisto-korhonen.sat12.pdf).

Find et al.'s direct-sum theorem is for monotone OR/SUM complexity of tensor-product Boolean matrices, a structured linear-map task. C-281 endpoints can be arbitrary subsets of the global high-table universe, so they may couple the lanes rather than factor as a tensor product. C-257's prefix-parity carriers give a concrete linear-size globally coupled grammar; no factorization theorem is available. [Find et al. 2013](https://arxiv.org/abs/1304.0513); see also the C-257 hostile calibration.

Paul's nonadditivity result for unrestricted combinational circuits reinforces that disjoint blocks alone do not justify additivity. It concerns vector-valued functions and unrestricted combinational complexity, not a lower bound for `V_k` in this particular promise or for the native compatible-support grammar. [Paul 1976](https://www.sciencedirect.com/science/article/pii/030439757690089X).

## 6. Next proof target and limits

The improved question is not whether k blocks cost k times one block. The scalar-side target is now exact: lower-bound shared cofactor-ensemble complexity for hard independent block tuples relative to correlated tuples with a common circuit. The native-side target is the compatible-box interpolation cover:

> How large must q be for a compatible-box grammar to cover `E_s1` while every generated box stays inside `E_s2`, when one product gate acts across all k lanes and endpoints may encode arbitrary cross-lane correlations?

A useful answer must preserve the exact OPS parameters, account for arbitrary globally coupled endpoints, and pass the parity and repeated-equality checks. The present derivation adds an exact circuit-side cofactor representation and a native-side lane algebra; it gives neither a q-sensitive lower bound nor a cover construction. The proved Gap-MCSP bound remains `rho_GapMCSP=N-o(N)`, with no P-vs-NP proof.
