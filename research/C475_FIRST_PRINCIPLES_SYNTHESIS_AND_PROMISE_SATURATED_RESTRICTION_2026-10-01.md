# C-475 — First-principles synthesis: the missing object is an all-extension lower bound

**Date:** 1 October 2026  
**Status:** cumulative audit and proof target; no new asymptotic theorem or P-vs-NP result.

## 1. Exact problem being attacked

Let `N=2^n`, `L_t={T in {0,1}^N : CC_n(T)<=t}`, and fix `0<beta<1`. The OPS instance has

```text
s1 = N^beta/(10 n),      tau2 = N^beta,
YES = L_s1,               NO = {T : CC_n(T)>tau2}.
```

The integer boundary is literal: the forced-zero side is `CC_n(T)>tau2`; if `tau2` is integral, tables of size exactly `tau2` are in the free middle. Define

```text
GapSep(N,beta) = min CC_N(F)
  over all total Boolean F such that
    F(T)=1 for every T in L_s1,
    F(T)=0 for every T with CC_n(T)>tau2.
```

The OPS target is one fixed `epsilon>0` such that, for every sufficiently small fixed `beta>0`, `GapSep(N,beta)>N^(1+epsilon)`. This is the ordinary total-gate model with arbitrary fan-out. The published magnification theorem says this target would imply `NP not subseteq P/poly`, and hence `P != NP`; it is a strong sufficient route, not a reformulation of the bare P-vs-NP question. See [Oliveira–Pich–Santhanam, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf).

## 2. What the accumulated work actually establishes

1. **A linear information floor.** Counting the size-`tau2` codebook gives `log |L_tau2|=O(N^beta log N)=o(N)`. Every valid separator depends on `N-O(N^beta log N)` table coordinates. The C-406 reconvergence refinement adds only `Omega(log N)` gates in the near-linear regime. This controls reading/essentiality, not post-read work.
2. **A valid complete upper bound.** Enumerating size-`s1` descriptions and testing agreement gives a full-promise separator with `O(N*2^(O(N^beta)))` gates. Safe coordinate projection has the same decoder scale. No near-linear full-promise separator is known.
3. **Robustness is semantic, not computational.** Address patching proves forced Hamming neighborhoods around Low and sufficiently High tables. C-459/C-470 show that radius, support size, anchor count, and one-sided soundness can coexist with `O(N)` recognition on a structured subfamily or a different promise.
4. **Many global statistics stop at linear scale.** Essential variables, ANF degree/support, Walsh rank/energy, local-query depth, certificate width/count, communication rank, transcript fibers, and balanced sketch width either yield at most the near-linear floor or admit an `O(N)` sharing counterexample. These are method-specific failures; they do not rule out an arbitrary DAG lower bound.
5. **Source transfers need exact endpoints and a real margin.** Several reductions preserve only one endpoint, induce an easy source label, or lose the hardness after generator/decoder costs. A general map from a hard source is not free: the entire table generator, separator, and any postprocessor must be composed in the model being lower-bounded.
6. **Alternate models do not transfer automatically.** Formula, comparator, local-tree, oracle, monotone, paid-AND, and native-fusion conclusions are not ordinary total-gate conclusions without a proved compiler. The resource ledgers must remain separate.

The primary failure pattern is therefore not “we need more anchors,” “a stronger certificate count,” or “a wider sketch.” It is the absent implication

```text
F accepts every size-s1 circuit output and rejects every size->tau2 output
                         =>
the actual shared ordinary DAG for F has superlinear total size.
```

No project argument proves that implication. The middle labels are free, so a lower bound for one natural extension (including the proximity extension) is insufficient.

## 3. First-principles model to use from here

Treat the task as a **partial-function extension-complexity problem**. The codebook is the image of the map

```text
description d  ->  truth table T_d,
```

and a separator is a one-bit classifier of the entire codebook sandwich. There are two logically different proof routes:

### Route A: force a hard function on a promise-saturated image

Let `E:{0,1}^m -> {0,1}^N` be a multi-output Boolean circuit with `J` internal gates, and let `h:{0,1}^m->{0,1}`. If one proves, for every source input,

```text
h(x)=1  =>  E(x) in L_s1,
h(x)=0  =>  CC_n(E(x))>tau2,
```

then every valid separator `F` computes `h=F o E`, using at most `J+CC_N(F)` internal gates (plus any explicitly required output-routing/postprocessing gates). Hence

```text
CC_m(h) <= J + GapSep(N,beta) + B,
```

where `B` is the fully charged postprocessor. This does not assume that F reconstructs a circuit, lists witnesses, or checks addresses separately. It handles arbitrary sharing by literal circuit composition. To prove the OPS target this way, exhibit `h,E` with `CC_m(h)>J+B+N^(1+epsilon)` and verify both endpoint implications. An addressable evaluator `G(x,a)` and an `N`-output table generator are different models: fixing `x` makes the former a circuit for `E(x)` of size `|G|`, while the latter may use free output labels and needs a separately charged address router to yield a single-output table circuit. Never conflate their costs.

This criterion is exact and useful, but it is not itself a new lower bound. The existing block, codeword, source, and self-embedding audits show why simple choices of `E` make `h` easy, leave the promise, or spend the hardness margin in the map. A new attempt must give a concrete source and a concrete generator, then calculate all costs before invoking the composition inequality.

### Strongest existing counterconstruction against the source-map shortcut

C-420 chooses a linear code/subspace whose nonzero table codewords avoid the small-circuit codebook, then maps source words so kernel elements produce the Low zero table and nonkernel elements produce High tables. This genuinely gives a promise-saturated image, but the source label is just `h(x)=1[Hx=0]`, computable by the syndrome circuit and a zero test. The hard output codewords do not make the source predicate hard; in fact the source map has already exposed a short decision rule. This refutes the inference “High outputs or a hard code imply a hard induced label,” not the composition criterion.

The required canaries expose the same issue in simple families: parity labels use `m-1` XOR/Boolean gates; repeated-block equality is checked by comparing each block with a representative; `q` sparse parity checks of width `w` use `O(qw)` gates plus an AND; and a block family produced by a simple global relation is decided by computing that relation on its representatives. These may make valid Low/High image families, but the induced `h` is still too easy to yield a superlinear source lower bound. A candidate must make the *source label itself* hard while preserving every promised output label. None of these examples refutes a more complicated generator.

### Route B: charge the all-extension classifier directly

Find a quantity on the actual AND/OR/NOT DAG that (i) has a proved per-gate growth bound under unrestricted fan-out and reconvergence, and (ii) is forced to exceed `N^(1+epsilon)` for **every** valid extension. A support, width, influence, certificate, spectral, or semantic statistic does not qualify unless both inequalities are proved. Do not insert a “non-shareability” axiom under another name.

## 4. The strongest construction-side check

Keep the exact full-promise description enumerator as the baseline. A proposed better separator must be complete on every size-`s1` table and reject every table above `tau2`; accepting a hand-picked Low family is not enough. C-470's linear-size robust recognizer and C-472's spectral recognizer are useful counterconstructions against broad but incomplete lower-bound mechanisms. Neither is a separator for the full promise. Balanced sketches below `N-log|L_tau2|` are impossible by C-474, while the safe coordinate projection already attains that width scale and still pays the enumerative decoder cost.

## 5. Barriers, originality, and limits of the audit

The published hardness-magnification locality barrier concerns adapting specified local lower-bound techniques to specified magnification frontiers; it is not a theorem ruling out nonlocal ordinary-circuit proofs. The cited OPS implication is the exact reason a successful fixed-`epsilon` result would be a major breakthrough. The recent cycles are a large exploration of candidate mechanisms, not an exhaustive proof that no other mechanism exists. Distinguish a proved counterexample to a proposed invariant from a counterexample to the P-vs-NP program.

Primary references: [OPS, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf); [Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam, *Beyond Natural Proofs: Hardness Magnification and Locality*](https://arxiv.org/abs/1911.08297). The latter explicitly frames locality as a barrier to adapting the techniques under discussion; it does not establish a universal impossibility theorem.

## 6. Decision for the next research cycle

Stop refining scalar input statistics and low-width sketching. The next lower-bound cycle should begin only after choosing either (A) one explicit promise-saturated generator and proving its source hardness with the full composition budget, or (B) one genuinely new gate-semantic quantity with both operation-wise and forced-value lemmas. In parallel, try one complete separator construction that beats description enumeration. Screen each candidate immediately against parity, repeated-block equality, sparse parity checks, simple global block relations, unrestricted fan-out, exact endpoints, and the fixed-`epsilon` quantifier.

**Quantitative result of C-475:** none. Ordinary frontier remains `N-O(N^beta log N)` essential inputs, with only C-406's additive logarithmic reconvergence refinement; the complete upper remains `O(N*2^(O(N^beta)))`; OPS fixed-`epsilon`, native `rho`, and P-vs-NP remain open.
