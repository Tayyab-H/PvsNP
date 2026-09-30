# C-407 — Random coordinate restrictions have a sparse low trace

**Status:** proved counterconstruction to a specific hardness-transfer route. For every fixed `0<beta<1/2`, a coordinate subspace of dimension `N^(1-beta/2)` has an easy separator for the entire induced Gap-MCSP promise. This does not improve or refute the full-promise circuit lower-bound target.

## Question and mechanism tested

Could a large coordinate subspace provide a hard promised restriction of Gap-MCSP? The restricted input varies only on a set `P` of truth-table coordinates, with all other entries fixed to zero. We test the strongest natural version of this route: choose `P` so that every small-circuit table supported inside `P` has small Hamming weight, while every table of weight below a slightly larger cutoff is automatically non-High.

Use the OPS parameters `N=2^n`, `s1=N^beta/(10n)`, `s2=N^beta`, with fan-in-two AND/OR/NOT circuit complexity. Fix `beta in (0,1/2)`. Choose any fixed `gamma` satisfying

`beta < gamma < 1-2 beta/5`,

and set `m=floor(N^gamma)`. Let `P` be a uniformly random `m`-subset of the `N` truth-table coordinates. Write `V_P={f in {0,1}^N : supp(f) subseteq P}`.

## Theorem

For all sufficiently large `N`, there exists a set `P` of size `m` such that the following holds:

1. Every `f in V_P` with `CC(f)<=s1` has `wt(f)<5s1`.
2. Every `f` with `wt(f)<=8s1` has `CC(f)<s2`, so every High table (`CC(f)>=s2`) has weight `>8s1`.

Consequently, the restricted promise on `V_P` is separated by the threshold predicate `wt(f)<=6s1`. As a circuit on the `m` free coordinates, this separator has `O(m log^2 m)=N^(gamma+o(1))` fan-in-two gates. Taking `gamma=1-beta/2` is valid and gives a sublinear-in-`N` restricted separator for every fixed `beta in (0,1/2)`.

The statement is promise-correct: all low tables in `V_P` are accepted, all high tables in `V_P` are rejected, and the middle remains unrestricted. It is not a separator on all `N`-bit truth tables.

This induced promise has both sides nonempty. The zero table is low. Also `|V_P|=2^m`, while the number of tables with complexity below `s2` is at most `2^(O(N^beta n))`; since `gamma>beta`, `m=N^gamma` eventually exceeds that exponent, so `V_P` contains high tables.

## Proof

There are at most

`(s1+1)(3(n+s1+2)^2)^s1 = 2^((2beta+o(1)) s1 n)`

circuits of size at most `s1`. This overcounts: order the gates topologically, choose one of three gate types, then choose each input from the `n` variables, constants, or earlier gates. The output choice contributes only a lower-order term. Since `s1=N^beta/(10n)`, `log2(n+s1+2)=beta*n+o(n)`.

For a fixed table `g` of weight `w`, the probability that its support lies in `P` is

`Pr[supp(g) subseteq P] = (m)_w/(N)_w <= (m/N)^w`.

For `w>=5s1`, this is at most `2^(-(5(1-gamma)+o(1))s1 n)`. The union bound over all circuits of size at most `s1` is therefore at most

`2^((2beta-5(1-gamma)+o(1))s1 n) = o(1)`,

because `gamma<1-2beta/5`. Hence some `P` contains no support of weight at least `5s1` from any low table. This proves item 1.

For item 2, a truth table of weight `w` can be computed by OR-ing its `w` address minterms. Share the `n` input negations; each minterm takes `n-1` AND gates, and the final OR takes `w-1` gates. The total is at most `wn+n-1`. At `w<=8s1`, this is at most `0.8N^beta+O(n) < s2` for all sufficiently large `N`. Thus every High table (`CC(f)>=s2`) has weight greater than `8s1`.

The two supports leave a strict interval: low tables in `V_P` have weight below `5s1`, while high tables have weight above `8s1`. A fan-in-two sorting network followed by a fixed threshold comparison uses `O(m log^2 m)` gates and accepts at weight at most `6s1`. This proves the restricted-promise separator.

## Resource accounting and scope

- **Total Boolean gates:** `O(m log^2 m)` for the restricted separator.
- **Wires:** `O(m log^2 m)` for a fan-in-two sorting network.
- **Description bits:** `O(m log^3 m)` for a standard indexed-gate description, plus `O(m log N)` bits to describe `P` and the restriction.
- **Restriction map:** each free input is wired to one selected truth-table coordinate; all other coordinates are constants. It costs zero Boolean gates when constants and wires are free, but its description is not free if a uniform reduction must output `P`.
- **Construction time for `P`:** the proof is probabilistic and nonuniform. Exhaustively checking the condition against all size-`s1` circuits takes exponential time in `N^beta`; no efficient deterministic construction is established.
- **Native fusion:** no native cover or paid-AND bound is inferred. This is an ordinary circuit on the restricted input coordinates, with no C-319 endpoint construction or least-fixed-point transfer.

## Adversarial checks

- **Parity truth table:** its support has size `N/2`, so it is outside `V_P` because `m=o(N)`. It remains a low table the restricted separator says nothing about.
- **Repeated-block equality and dense block relations:** dense members are likewise absent from `V_P`; sparse members that do lie in it are covered by the weight threshold. These examples are not counterexamples to the theorem.
- **Sparse parity checks and copy/XOR relations:** if their truth-table support lies in `P` and they are low, item 1 forces their support below `5s1`; no global circuit-complexity claim is made about them.
- **Full-promise threshold test:** accepting all tables of weight at most `6s1` is sound against every High table, but incomplete on the full promise: it rejects dense low tables, including parity.
- **Full-promise enumeration attempt:** enumerate the `M<=2^(O(N^beta))` low-circuit descriptions, compare the input table against each candidate over all `N` coordinates, and OR the equality outputs. This accepts every promised YES and rejects every promised NO, but costs `O(NM)` gates and wires, `O(NM log(NM))` indexed-description bits, and direct construction time `O(MNs1)`. A prefix trie still has `O(NM)` worst-case nodes; no sharing argument improved this upper bound.

## What this changes

This is a project-derived random-support lemma, not a claimed new general circuit theorem. It gives a concrete easy trace on a large polynomial-dimensional coordinate subspace, with a gate bound below `N`. Therefore, restriction arguments that merely select a sparse coordinate support and count low circuits cannot furnish the desired hard promised trace. This is distinct from C-404's near-full-dimensional quotient whose trace was a coordinate subspace: here the support itself is random, and counting forces every low table on it to have small Hamming weight.

The result is consistent with the locality warnings in Murray–Williams: their theorem concerns reductions to MCSP with very local access, and does not rule out arbitrary nonlinear promise-preserving maps. Recent gate-elimination refuters address explicit total functions; this trace construction provides no explicit hard target for such a refuter. These are scope checks, not universal barriers.

**Quantitative frontier:** no change to `S>=N-O(N^beta log N)` or to the OPS `N^(1+epsilon)` target. No change to native `rho_GapMCSP>=N-o(N)`. The next restriction route must encode low anchors by a nonlinear trace that is not captured by sparse-support or linear-subspace tests, while keeping every other image point High. Otherwise return to full-promise coverage directly.

### Primary sources checked

- Oliveira, Pich, Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorems 1.4 and 1.5 for the OPS thresholds and formula frontier.
- Murray and Williams, [*On the (Non) NP-Hardness of Computing Circuit Complexity*](https://theoryofcomputing.org/articles/v013a004/), for the limits of very local reductions to MCSP.
- Carmosino, Dang, Jackman, [*Constructive Separations from Gate Elimination*](https://arxiv.org/abs/2604.23958), checked as an adjacent technique; it does not directly address promise separators.
