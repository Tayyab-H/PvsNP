# C-443 — First-principles audit and a logic-facing research pivot

**Date:** 1 October 2026  
**Status:** project-wide synthesis through C-442, plus a precise quantifier reformulation and literature check. No new separator lower bound or near-linear upper bound.

## Scope

This report consolidates the durable claim ledger, current state, open obligations, the C-430–C-442 ordinary-circuit cycles, and the native-model distinction. It does not claim to re-prove every historical lemma. The current numerical frontier is unchanged.

## 1. The exact object

Let `N=2^n`, and let `CC(T)` be the total number of fan-in-two AND/OR/NOT gates in an ordinary circuit for the `N`-bit truth table `T`, with arbitrary fanout. For the OPS promise,

```text
s1 = N^β/(c log2 N),       s2 = N^β,
YES = {T : CC(T) ≤ s1},    NO = {T : CC(T) > s2}.
```

A separator is any Boolean circuit `F` on the `N` table bits that is 1 on YES and 0 on NO; its values in the middle band are unconstrained. OPS Theorem 1.4 asks for one fixed `ε>0` such that, for every sufficiently small fixed `β>0`, no such separator has at most `N^(1+ε)` gates. Its conclusion is `NP ⊄ P/poly`, which implies `P ≠ NP` but is stronger than that desired separation. This is a sufficient route, not an equivalence. The exact theorem uses a universal constant `c`; the proof instantiates `c=10`. [OPS, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)

An immediate consequence of the definition is easy to overlook: `F_low(T)=1[CC(T)≤s1]` and `F_high(T)=1[CC(T)≤s2]` are both valid extensions. A lower bound on one canonical threshold function alone does not lower-bound the minimum over all valid extensions. Any direct proof must handle the free middle band.

## 2. What the accumulated work establishes

- **Ordinary total gates:** the strongest recorded unconditional separator floor is `N-O(N^β log N)-1`, with C-406's additive logarithmic refinement. It is essentially a dependence/readout floor. It is not superlinear.
- **Exact full-promise upper bound:** enumerate every description of a circuit of size at most `s1`; for each, compare its `N` output bits with `T`, then OR the equality tests. There are `K=2^{O(s1 log s1)}=2^{O(N^β)}` candidates, so this is an exact separator of `O(N·2^{O(N^β)})` gates and wires. This proves completeness on all YES and NO inputs; its behavior on the middle band is allowed. No near-linear full-promise construction is known in the project.
- **Source composition:** C-442 proves that if a `J`-gate map generates `T_x` and a `B`-gate decoder recovers an `h`-hard source bit from `T_x`, then `h≤J+B+O(1)`. If a separator of size `S` also recovers that bit, `h≤J+S+O(1)`. Thus a cheap table decoder consumes the post-generator source-hardness margin. C-441's complete prefix table has `B=O(N)` and is closed as a route to a superlinear OPS bound.
- **Restricted models and native measures:** comparator-circuit, formula, monotone, paid-state, and fusion results are useful diagnostics but do not automatically lower-bound unrestricted ordinary DAG gates. The comparator MCSP bound has a gain depending on its size parameter and does not supply the OPS fixed-`ε` quantifier as `β` becomes small. Native `ρ≥N-o(N)` remains a distinct frontier.

The project has not found an argument that makes an arbitrary separator reconstruct a circuit description, enumerate witnesses, expose caller history, or check addresses one at a time. Such claims would need a separate theorem.

## 3. First-principles diagnosis

Write `d` for a circuit description and `Eval(d,i)` for its output on address `i`. Then the endpoint sets have the exact quantifier forms

```text
YES(T)  ⇔  ∃d, |d|≤s1  ∀i<N : Eval(d,i)=T[i],
NO(T)   ⇔  ∀d, |d|≤s2  ∃i<N : Eval(d,i)≠T[i].
```

Thus the object is a promise interpolant between an existential circuit-synthesis set and the complement of a larger existential set. The positive endpoint is NP and the negative endpoint is coNP. Ordinary feasible-interpolation theorems for disjoint NP pairs do not directly apply: the polarity is wrong on the NO side, and a separator is not required to reveal a witness. This is a useful logical formulation, but not yet a lower-bound mechanism.

The common failure behind the project’s many distinct experiments is now precise. Semantic facts—many coordinates read, many certificates, many constraints, large transcript families, or many source queries—do not imply a corresponding number of **new shared DAG gates**. Once all `N` bits are exposed, the unresolved object is the cost of the residual Boolean computation. The identity front end, muxes, parity, and full-rank linear-size predicates show why generic readout, incidence, and one-cut rank charges stop at linear scale.

Three different claims must stay separate:

1. **A semantic object exists.** Anti-checkers, hard cores, and large witness families often satisfy this.
2. **A circuit must output or reconstruct that object.** This is not implied by one-bit decision correctness.
3. **Every valid separator costs superlinear total gates.** This is the actual OPS lower-bound theorem required.

Repeatedly moving from (1) to (2), or from a wire/certificate count to (3), explains much of the historical churn. The same audit applies to source maps: the map's promise, ordinary gate cost, table-side decoder cost, and remaining hardness margin must all be proved before the separator is analyzed.

## 4. Counterconstruction calibration

These constructions defeat generic charging principles, not the Gap-MCSP target:

- **Parity:** a chain of `N-1` XORs, each implemented by a constant-size AND/OR/NOT gadget, costs `O(N)` total gates.
- **Repeated-block equality:** compare one representative per block, or compare corresponding bits of two blocks; the whole computation costs `O(N)` regardless of repeated occurrences.
- **Sparse parity checks:** with `L=O(N)` total incidences, compute each check by a constant-size XOR implementation per incidence and AND the results, for `O(L+r)=O(N)` gates.
- **Simple global block relations:** compute each shared block signal once and reuse it; output multiplicity does not force a separate charge per check.

The strongest single counterexample to a generic communication-rank charge is `AND_i(x_i OR y_i)`: its balanced GF(2) communication matrix has full rank `2^(N/2)`, yet it has `N-1` gates. C-435 proves the general rank-to-gates inequality and also proves its dimension ceiling is only linear.

## 5. Research pivot from the audit

The most useful change is a stricter proof funnel, not another proposed scalar called non-shareability:

**Direct route.** State a numerical invariant on the actual Boolean function computed by an arbitrary acyclic AND/OR/NOT DAG. Prove a gate-by-gate upper bound in terms of total gates, including unrestricted fanout. Then prove its value exceeds `N^(1+ε)` for *every* valid extension of the full promise, with the same fixed `ε` as `β` tends to zero. If either inequality is missing, the candidate is not a mechanism.

**Source route.** Before studying a proposed encoding, write down the exact YES/NO image conditions, the full multi-output generator gate count `J`, every ordinary postprocessor cost, and the best table-side decoder cost `B`. Require the residual margin `h-J>N^(1+ε)` for a fixed `ε`; if `B=O(N)`, C-442 shows plain source composition cannot supply that margin. Do not use oracle answers or wires as uncharged gates.

**Logic-facing candidate, exploratory only.** Investigate whether proof-complexity or interpolation ideas can say something about this specific NP/coNP gap-interpolant problem. The first test is polarity: can the standard theorem actually produce a separator circuit for `YES` versus `NO`, without changing the promise or assuming the separator emits a witness? If not, retire the transfer before trying to prove a proof-size bound. Feasible interpolation is normally a bridge from proof systems to restricted separator circuits, not an automatic lower bound for unrestricted circuits. [Feasible interpolation survey/report](https://eccc.weizmann.ac.il/report/2017/106/download/)

This is a new organizing lens for the ordinary target, not a claimed breakthrough. The project already explored interpolation extensively in native-cover settings; no transfer from those native results to ordinary total gates has been established.

## 6. Barriers and limits

The locality barrier rules out direct combinations of certain localizable magnification theorems with lower-bound techniques that remain valid in the corresponding small-fan-in-oracle models. It is method-specific, not an impossibility theorem for every ordinary-circuit proof. [Chen et al., ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/)

Work on MCSP also explains why a seemingly easy source reduction is dangerous: even strong NP-hardness claims under local reductions would imply major circuit lower bounds. This supports the project rule that an exact promise-preserving map must be costed and audited rather than assumed. [Murray and Williams, On the (Non) NP-Hardness of Computing Circuit Complexity](https://cims.nyu.edu/~regev/toc/articles/v013a004/index.html)

## 7. Verdict and next state

Nothing in the accumulated work shows that a short diagonalization, a missing elementary counting trick, or a new name for sharing will settle P versus NP. The strongest diagnosis is that the desired OPS statement is itself a major unrestricted circuit lower bound, strong enough to imply `NP ⊄ P/poly`. The missing bridge remains either (a) a promise-forced superlinear cost for residual shared computation, or (b) an exact source map whose generation leaves a superlinear hardness margin. The first-principles review found no proof of either.

**Frontier unchanged:** ordinary `N-O(N^β log N)-1` plus C-406 refinement; OPS `N^(1+ε)` open with its fixed-`ε`/small-`β` quantifiers; exact full-promise separator `O(N·2^{O(N^β)})`; native `ρ≥N-o(N)` separate. No near-linear full-promise construction, P≠NP proof, or breakthrough.

### Primary literature checked

- Oliveira, Pich, Santhanam, [Hardness Magnification near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4.
- Chen et al., [Beyond Natural Proofs: Hardness Magnification and Locality](https://eccc.weizmann.ac.il/report/2019/168/).
- Cavalar and Lu, [Algorithms and Lower Bounds for Comparator Circuits from Shrinkage](https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.34/LIPIcs.ITCS.2022.34.pdf).
- Murray and Williams, [On the (Non) NP-Hardness of Computing Circuit Complexity](https://cims.nyu.edu/~regev/toc/articles/v013a004/index.html).
