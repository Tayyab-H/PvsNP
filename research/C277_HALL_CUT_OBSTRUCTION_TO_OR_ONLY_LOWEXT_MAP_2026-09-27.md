# C-277 — Hall cuts rule out OR-only matching-to-LowExt maps

Date: 27 September 2026  
Classification: **ROUTE-KILL (zero-AND rail maps).**  
Route: A4, explicit YES-witness encoding for matching.

## Candidate construction tested

Try to use one truth-table coordinate for each monotone clause that is true on every perfect matching. Let its rail be the OR of a chosen set of graph edges. A YES matching would activate the same full low table, and a NO graph would miss at least one coordinate. This would give a zero-AND map and a monotone CNF separator with at most `N` clauses.

The construction cannot work when `v=A(log N)^2`.

## Why a zero-AND rail map yields a fixed low code

Assume `v` is divisible by four and the source is `f_v(G)=1` iff the bipartite graph has a matching of size at least `v/4`. Every graph with fewer than `v/4` matching edges is a NO input under C-125, so every such image must be consistent and lie below a high one-hot code.

If a rail has zero AND-cost, it is an OR of source edge variables and possibly a constant. At any truth-table coordinate, both polarities cannot be activated by source edges: choosing one supporting edge for each polarity gives a graph with at most two edges, hence a NO input for `v/4>2`, whose image would contain both rails. Likewise, a constant rail forbids any nonconstant support for the opposite polarity. Thus at each coordinate only one polarity can ever occur.

Every YES image contains a full low one-hot code, so its bit at every coordinate must equal that globally available polarity. All YES witnesses are therefore one fixed table `w`. The `N` monotone rail predicates `phi_{i,w[i]}` form a monotone CNF separator:

```text
F(G) = AND_{i in [N]} phi_{i,w[i]}(G).
```

Every YES graph satisfies all clauses. A NO graph cannot satisfy them all, since that would give `e(w)<=phi(G)<=e(z)` for a high completion `z`, forcing `w=z`.

## Hall-cut lower bound on the number of clauses

Write `v=2m` and `k=v/4=m/2`. For every vertex subset `W` of size `k-1`, let `G_W` contain all edges incident to `W`. It has matching number at most `k-1`, so the CNF must reject `G_W`. Hence some clause edge set `E` is disjoint from `G_W`.

Every clause must nevertheless accept every perfect matching, so its edge set `E` intersects every perfect matching. By Hall's theorem, the complete bipartite graph with the edges in `E` removed has no perfect matching. There are `A subseteq L` and `T subseteq R` with `|T|<|A|` such that every edge from `A` to `R without T` belongs to `E`. If `E` is disjoint from `G_W`, then this entire rectangle avoids `W`, requiring

```text
W_L subseteq L without A,       W_R subseteq T.
```

For this fixed clause, the number of vertex subsets satisfying those restrictions is at most

```text
2^(m-|A|) 2^|T| <= 2^(m-1) = 2^(v/2-1).
```

There are `binom(v,k-1)=2^(H_2(1/4)v-o(v))` candidate sets `W`, where `H_2(1/4)=0.811...`. Therefore any such monotone CNF needs at least

```text
binom(v,k-1) / 2^(v/2-1)
  = 2^((H_2(1/4)-1/2)v-o(v))
  = 2^(0.311...v-o(v))
```

clauses. At `v=A(log_2 N)^2`, this is `2^Omega((log N)^2)`, which is larger than the available `N=2^(log_2 N)` coordinates for sufficiently large N.

## Route decision

This rules out the OR-only Hall-blocker encoding, and in fact every zero-AND C-125 map for this source parameter: NO consistency forces a common YES code, and Hall cuts show that `N` fixed OR clauses cannot separate the source. Any transfer map must introduce AND interactions that let the selected low code vary across YES inputs or otherwise escape a fixed-code CNF. The argument says nothing about maps with positive AND-cost, where gates can synchronize edge combinations.

This is not a new matching lower bound or a q improvement. It is a construction-class route filter. The actual fusion lower bound remains `q=N-o(N)`.
