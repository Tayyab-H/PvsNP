# C-309 - When a distributional decoder becomes an exact monotone separator

Date: 28 September 2026  
Classification: **EXACT SYMMETRIZATION THEOREM / SOURCE-SELECTION CRITERION.** A one-sided monotone separator that accepts almost all minimal YES witnesses can be made exact with a controlled AND-count loss when those witnesses form one transitive symmetry orbit. The criterion explains why the matching distribution yields an exact decision route for MATCH but not for all of ODDFACTOR.

## 1. Orbit symmetrization lemma

Let `f:2^E -> {0,1}` be a monotone function invariant under a finite group `G` acting on the ground set `E`. Let `M(f)` be the family of inclusion-minimal true inputs. Assume `G` acts transitively on `M(f)`, and write `L=|M(f)|`.

Suppose a monotone circuit `Q` with `a` binary AND gates and free OR gates is one-sided sound,

```text
Q(y)=0 for every f(y)=0,
```

and accepts at least a `1-eta` fraction of `M(f)` under the uniform distribution, where `0<eta<1`. Choose

```text
t = floor(log(L)/log(1/eta)) + 1
```

independent uniform group elements `g_1,...,g_t`, and let `Q* = OR_i Q(g_i x)`. For each fixed minimal true input `M`, transitivity makes `g_i M` uniform on `M(f)`, so

```text
Pr[Q*(M)=0] <= eta^t.
```

Since `L*eta^t<1`, the union bound shows that some choice of `g_1,...,g_t` makes `Q*` accept every member of `M(f)`. Each relabeled copy remains zero on every NO input because `f` is G-invariant. Every YES input contains a minimal YES subset, and monotonicity then makes `Q*` accept every YES input. Thus `Q*` computes `f` exactly with at most `t*a` paid AND gates:

```text
CycAnd(f) <= t * a.
```

For `eta<=1/2`, `t<=O(log L)`. If `M(f)` is one orbit of labeled witnesses on `m` input variables, then `log L<=m`, so exactification costs at most an `O(m)` factor. OR is free, which is essential to this accounting.

## 2. Consequence for C-125 maps for MATCH

For bipartite `MATCH_v`, the inclusion-minimal YES inputs are exactly the perfect matchings. The group `S_v x S_v` acts transitively on them. C-308's canonical-polarity extraction applies to a C-125 map for MATCH using the same perfect-matching/odd-cut distributions: the extracted conjunction `Q` rejects every NO graph by C-125 soundness and accepts `1-o(1)` of uniformly random perfect matchings. Taking `eta=o(1)` in the orbit lemma gives an exact monotone separator with

```text
CycAnd(MATCH_v) <= O(v log v) * (a+N-1),
```

where `a` is the map's paid-AND cost. Thus a cheap encoder for MATCH would imply a comparably cheap exact separator up to a polynomial-in-v symmetrization factor. This is a reconstruction-versus-decision comparison that uses the *whole* minimal YES orbit, rather than only an average input.

## 3. Why the same step does not exactify ODDFACTOR

The odd-cut distribution in C-308 is supported on NO inputs, but its YES distribution is only the perfect-matching subfamily. Inclusion-minimal ODDFACTOR YES inputs are not one orbit. For example, besides perfect matchings, for every `v>=4` there is a minimal spanning odd-degree forest consisting of a `K_(1,3)` star, a disjoint `K_(3,1)` star, and `v-4` disjoint matching edges. All degrees are odd; the forest is inclusion-minimal because it has no cycle. Its degree sequence differs from that of a perfect matching, so no vertex permutation maps it to a matching.

Consequently, the C-308 separator is certified to accept almost every member of one minimal-witness orbit, not every minimal YES orbit. Symmetrizing it can yield exact MATCH acceptance while still missing odd-factor inputs with no perfect matching. This is the precise point at which the ODDFACTOR distributional route stops short of an exact source separator.

## 4. Source-selection implication

A useful hard source for the reconstruction route should satisfy at least one of these:

1. its minimal YES witnesses form one manageable transitive orbit and a spread distribution covers that orbit; or
2. there are few witness orbits and the distributional decoder has high acceptance on each orbit; or
3. a separate monotone argument shows that the selected witness orbit generates every YES input under upward closure.

When there are many unrepresented orbits, a low-error decoder on one hard distribution can certify only a hard subfunction. The C-125 map's global YES condition still has to cover every YES input. This source filter is independent of raw certificate count: it tracks which minimal-witness types the approximation distribution sees.

## 5. Disposition

C-309 gives an exact theorem and explains the MATCH/ODDFACTOR distinction. It does not construct a C-125 encoder or improve `rho_GapMCSP=N-o(N)`. The next step is to seek a hard source whose minimal-witness orbit structure is compatible with the C-125 all-YES requirement, or find a proof that handles every ODDFACTOR minimal-witness orbit within one shared approximation scheme. Preserve the OPS quantifiers and the C-257/C-258 native calibrations.

