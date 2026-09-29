# C-360 - Formula leaf weighting does not charge shared C-319 states

Date: 29 September 2026  
Route: test a literature-derived route from formula search-to-decision to the C-319 anchor-selector problem.  
Classification: **TECHNIQUE TRANSFER TEST; THE NAIVE WEIGHTING TRANSFER FAILS AT FAN-OUT.**

## 1. The candidate technique

Ilango's search-to-decision reduction for minimum formula size uses a partial-to-total encoding and leaf weighting. Informally, replacing a variable z by an OR of s fresh variables makes each occurrence of z cost s leaves. The formula tree has no shared subcomputation, so the weighted cost can expose the structure of an optimal decomposition. The result is specific to De Morgan formulas and is explicitly nonrelativizing. See [Ilango, *The Minimum Formula Size Problem is (ETH) Hard*](https://www.rahulilango.com/papers/MFSP-hard.pdf).

The tempting C-319 adaptation is to replace each address/context occurrence by a weighted family of seed literals, hoping that reuse of one state across many addresses becomes expensive.

## 2. Exact fan-out obstruction

Take a Boolean subcomputation `z = OR(a_1,...,a_s)` used by r callers. In a formula, these callers require r separate copies of the subformula; after replacing each occurrence by the weighted OR, the leaf cost is multiplied by r. In a circuit, compute z once with s-1 binary OR gates and fan the same wire out to all r callers. The cost is s-1, independent of r.

The C-319 closure has the circuit behavior relevant here: each state has one activation bit at each round, and every parent transition can reuse that bit. A seed clause is also evaluated once per state, no matter how many incoming proof histories or address interpretations later use the activated state. Therefore ordinary leaf weighting charges formula occurrences, but it does not charge C-319 state reuse. This is precisely the sharing operation that the attached selector plan needs to control.

## 3. What survives and what fails

The formula result suggests a useful *shape* for a future theorem: encode partial local obligations into total instances and make inconsistent witness reuse expensive. But the formula lemma cannot simply be quoted for circuits or the native game. Circuit sharing nullifies its per-occurrence cost, and the known C-319 splice law alone does not restore that cost: same-anchor context/proof supports form a full compatible product, while cross-anchor supports may conflict and protect the repeated-equality subpromise.

Ren and Santhanam construct relativized worlds where MCSP decision is easy but search-MCSP is hard, even approximately, so a generic decision-to-circuit-witness extraction is not available by relativizing arguments. Their result says nonrelativizing techniques are required; it does not rule out an extraction theorem for the specific C-319 promise. See [Ren and Santhanam, ECCC TR21-089](https://eccc.weizmann.ac.il/report/2021/089/download). A randomized approximate search reduction from MCSP decision is known under stronger algorithmic hypotheses, but it outputs a poly(s)-size approximator and does not directly give an exact size-s1 witness from this fixed-gap native separator; see [Carmosino et al., CCC 2016](https://doi.org/10.4230/LIPIcs.CCC.2016.10).

## 4. Next precise attempt

Any surviving weighting must charge **state incidence**, not syntactic occurrences. A candidate must assign address/context-specific tags to weighted supports so that if one activated state serves two incompatible tags, C-281 produces a cross-context completion in a C-320-forbidden region. The missing forcing statement is still global: completeness over all low tables must make some state serve enough independently tagged contexts, or a theorem must charge the graph for preventing that reuse. C-258 equality and C-257 parity are mandatory counterchecks.

## Status

The naive leaf-weighting transplant is closed. No state-incidence weighting theorem, arbitrary-cover embedding, q improvement, full-promise near-linear cover, or P-vs-NP proof has been obtained. The proved native bound remains `rho_GapMCSP >= N-o(N)`.
