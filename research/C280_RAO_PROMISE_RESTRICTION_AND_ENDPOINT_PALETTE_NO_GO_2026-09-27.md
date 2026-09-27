# C-280 — Rao's hard matching promise permits an antichain NO palette, but fixed-left two-half support palettes fail

Date: 27 September 2026  
Classification: **ROUTE-KILL.** Scope: fixed-left two-half palettes whose rail supports are exact q-matchings saturating the corresponding left block; arbitrary selected bijection subfamilies are allowed.  
Route: A4, promise-source refinement.

## A hard promise supported only on perfect matchings and vertex-cover graphs

Take a bipartite graph with `2q` vertices on each side. Let the YES promise be all perfect matchings, and let the NO promise be

```text
Z = { G(W) : W subseteq L union R, |W|=q },
```

where `G(W)` contains every edge incident to `W`. Every NO graph has matching number at most `q`.

Rao's proof of the spread-matching lower bound uses only two input distributions: `X1`, a uniformly random perfect matching, and `X0=G(W)` for a uniformly random `q`-vertex set `W`. The gatewise approximants are analyzed only for errors on these two distributions; correctness elsewhere is never invoked in the proof. Consequently the same proof establishes a monotone circuit lower bound `exp(Omega(q/sqrt(2q)))=exp(Omega(sqrt(q)))` for this restricted promise itself. The explicit cyclic unrolling from C-266 carries the same exponential lower bound into the cyclic AND measure. This is a proof-level promise restriction, not an assertion that every smaller NO subset preserves the bound.

The restriction matters for reductions: one need only make the images of the `G(W)` inputs high-completable. Small graphs and other low-matching inputs are outside this promise, so C-277's one/two-edge consistency premise no longer applies directly.

## Fixed-left two-half palette tested, including pairing-sensitive families

Split `L=A disjoint-union B` with `|A|=|B|=q`. For each truth-table coordinate `i`, consider rail predicates of the following form:

- rail 0 is activated by a `q`-matching saturating `A`; for right endpoint set `C`, its selected bijections form an arbitrary family `F0_i(C)`;
- rail 1 is activated by a `q`-matching saturating `B`; for right endpoint set `D`, its selected bijections form an arbitrary family `F1_i(D)`.

No endpoint-set-only assumption is made: either family may select an arbitrary proper subset of the bijections.

For a `q`-subset `C` of the right side, the NO graph `G(C)` contains every matching from `A` to `C` and every matching from `B` to `C`. NO consistency therefore requires that at most one of the two rail families is nonempty at the same right set `C`.

Now take any perfect matching whose `A` block is matched onto `C` and whose `B` block is matched onto `C^c`. To contain a full one-hot low code, at least one rail must be active. This must hold for **every pair** of bijections `A->C` and `B->C^c`:

```text
F0_i(C) is full  OR  F1_i(C^c) is full.
```

This universal product condition implies that either `F0_i(C)` contains every bijection `A->C` or `F1_i(C^c)` contains every bijection `B->C^c`: otherwise choose a missing bijection from each family and obtain a perfect matching with neither rail active. Apply the same condition with `C` and `C^c` swapped. Together with the NO consistency conditions at `G(C)` and `G(C^c)`, these force exactly one of the following:

```text
F0_i(C), F0_i(C^c) are both full;   F1_i(C)=F1_i(C^c)=empty,
or
F1_i(C), F1_i(C^c) are both full;   F0_i(C)=F0_i(C^c)=empty.
```

Therefore, on every perfect matching with this endpoint split, the active polarity at coordinate `i` is exactly the same polarity pinned by the NO input `G(C)`. This holds independently at every coordinate. The complete YES low table is consequently identical to the complete NO table `phi(G(C))`. C-125 would require that table both lie in `SIZE(s1)` and outside `SIZE(s2)`, impossible when `s1<s2`.

Thus even pairing-sensitive selection collapses to a full endpoint-set family or the opposite full family. This kills every fixed-left two-half exact-matching palette of the stated form, regardless of AND-cost. Its obstruction is not the circuit size: NO all-right covers force a consistency condition that propagates to the matching code.

## Surviving branch

The proof does not cover more than two witness blocks, partial rather than complete NO codes, terms that are not exact q-matchings saturating the fixed left blocks, or support systems that encode a matching through a different global decomposition. The next precise target is a cross-cover theorem for those broader support families, or a construction that evades the fixed-left collapse while keeping AND-cost below the matching lower bound.

This promise restriction opens a genuinely different map search, but the fixed-left two-half attempt produces no transfer and no q improvement. The actual fusion bound remains `q=N-o(N)`.

**Primary source:** Anup Rao, [*Monotone Circuit Lower Bounds from Spread Matchings*, ECCC TR26-129 rev. 5](https://eccc.weizmann.ac.il/report/2026/129/revision/5/download), Section 3 and especially the distributions `X1`, `X0` and error analysis in Section 3.1.
