# C-450 — First-principles codebook-sandwich audit

**Date:** 1 October 2026  
**Scope:** cumulative ordinary Gap-MCSP record through C-449, with a fresh diagnostic of description-space pullbacks and a paired full-promise separator check.  
**Status:** exact reformulation and route-specific obstruction proved; no new circuit lower bound, no improved upper bound, and no P-vs-NP proof.

## 1. The exact target

Let `N=2^n`, let `L_t` be the set of truth tables of `n`-input fan-in-two Boolean circuits of at most `t` AND/OR/NOT gates, and set

```text
s1 = 2^(βn)/(c n) = N^β/(c log_2 N),     s2 = 2^(βn) = N^β.
```

A total circuit `F` separates the promise exactly when

```text
L_s1 ⊆ F^{-1}(1) ⊆ L_s2.
```

The second inclusion is equivalent to rejecting every table of circuit complexity greater than `s2`. The separator may choose either answer throughout the middle band. Thus the ordinary target is

```text
SepCC(N,β) = min { CC(F) : L_s1 ⊆ F^{-1}(1) ⊆ L_s2 }.
```

The set geometry is extreme but not enough by itself. Circuit counting gives `|L_s2|≤2^{O(s2 log(N+s2))}=2^{O(N^β log N)}=2^{o(N)}` for fixed `β<1`; hence every separator's accepting set is exponentially sparse among the `2^N` possible tables. At the same time, `L_s1` contains every table supported on at most `r=Θ(N^β/(log N)^2)` coordinates: an OR of `r` address minterms costs `O(r log N)` gates. This yields at least `binom(N,r)=2^{Θ(N^β/log N)}` forced accepting tables. These counts explain the sparse-codebook picture, but neither the size nor sparsity of the accepting set pays for a superlinear shared circuit.

The Oliveira–Pich–Santhanam theorem requires one universal `c≥1` and one fixed `ε>0` such that, for every sufficiently small fixed `β>0`, `SepCC(N,β)>N^(1+ε)`; it then implies `NP ⊄ P/poly`. The same `ε` must work as `β` varies. A gain `ε(β)>0` that shrinks with `β` is insufficient. This is already a major nonuniform circuit lower bound, stronger than `P≠NP`. [OPS, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf).

## 2. The shared missing term, stated quantitatively

Let `E(F)` be the number of essential table inputs and define the surplus beyond the fan-in-two support tree by

```text
Δ(F) = CC(F) - E(F) + 1.
```

The accumulated project proof gives `E(F) ≥ N-a_N`, where `a_N=O(N^β log N)`, hence `CC(F) ≥ N-a_N-1`. The formula/reconvergence transfer forces only logarithmic surplus in its near-linear regime. Since `E(F)≤N`, any separator with `CC(F)>N^(1+ε)` necessarily has

```text
Δ(F) > N^(1+ε)-N+1.
```

Conversely, using `E(F)≥N-a_N`, it suffices to prove `Δ(F)>N^(1+ε)-N+a_N+1` for every valid extension. Either way, the missing surplus is genuinely superlinear at scale `N^(1+ε)-N`. It cannot be obtained by refining the number of relevant table bits, witnesses, constraints, pairwise disagreements, or proof states unless that refinement is shown to charge gates of the actual shared AND/OR/NOT DAG.

The project’s failures group by the missing implication, not by topic:

| What a route controls | Why it has not delivered the target |
|---|---|
| Essential inputs, sensitivity, subcubes | Forces almost all `N` leaves, hence a linear floor; it does not price combining them. |
| Certificates, anti-checkers, local constraints, transcript fibers | Describes semantic evidence, but a separator need not output it; an `O(N)` front end can expose the entire table to an unrestricted decoder. |
| Communication rank, rectangles, gate paths | Sharing can be represented faithfully, but the known dimension/cover ceilings are linear or the relaxed model is just the original circuit problem. |
| Formulas, comparator circuits, monotone circuits, fixed depth | Proved bounds are real in those models; no cost-preserving compiler from an arbitrary shared DAG is known. Comparator gains also shrink with `β`. |
| Source hardness and implicit encodings | Either an endpoint is missing, the source label is cheaply decoded from the table, or generator and decoder costs consume the hardness margin. Serial substitution is only an upper bound when joint sharing is allowed. |
| Native cyclic fusion | `ρ≥N-o(N)` is a separate measure; the available compiler losses do not yield an ordinary total-gate OPS bound. |

These are route audits, not impossibility theorems. The Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam locality barrier rules out specified locality-based transfers; it is not a blanket barrier to global or nonlocal arguments. [Primary paper](https://eccc.weizmann.ac.il/report/2019/168/).

## 3. Fresh diagnostic: pullback to circuit descriptions

Let `d` encode an `n`-input circuit `C_d` of at most `t` gates, and write `T_d` for its `N`-bit truth table. For one fixed address, evaluate the description gate by gate; each description-controlled predecessor lookup can be implemented by a fan-in-two multiplexer over the at most `n+t` available signals, using `O(n+t)` gates. Repeating for `t` gates and then for all `N` addresses gives the safe fan-in-two upper bound

```text
g_table(t) = O(N t(n+t)),
CC(F∘T_d) ≤ CC(F) + g_table(t).
```

Here `g_table` counts distinct gates in a shared fan-in-two multi-output circuit; its `N` output wires are connected to the `N` inputs of `F` without adding gates. Wires, description bits, and construction runtime are separate measures. This is an upper bound for an explicit composition, not a lower bound against more efficient joint circuits.

The endpoint audit is decisive:

* If `|C_d|≤s1`, then `F(T_d)=1` is forced.
* If `s1<|C_d|≤s2`, the promise forces no value on `T_d`; it lies in the middle band.
* If `|C_d|>s2`, that description size still does **not** imply `CC(T_d)>s2`: a padded or redundant description may compute a small function. To force `F(T_d)=0`, one must independently prove that the function computed by `d` has complexity greater than `s2`.

Therefore the naive pullback over descriptions up to size `s2` has no forced NO examples at all. It can be constantly one on that restricted image without violating any promise condition. Enlarging the description domain supplies NO points only after a genuine hard-output construction is proved; description length alone is not a hardness certificate. The map must also pay the full-table generator cost. For `t≈s2=N^β`, the generic `O(Nt(n+t))` upper is `N^(1+2β+o(1))`, which can fit below `N^(1+ε)` when `2β<ε` with fixed slack. So the cost estimate does not itself kill the idea; the missing object is a total source map whose generated functions satisfy both exact endpoints and whose source hardness survives that cost.

**Disposition:** retain description-space pullback as an endpoint and budget diagnostic, not as a lower-bound mechanism. This sharpens the source obligation but proves no bound for arbitrary separators.

## 4. Strongest counterchecks and paired construction attempt

The direct mechanism tests remain decisive against generic charges: parity, repeated-block equality, sparse parity-check systems with linear total incidence, and simple globally related blocks all admit `O(N)` shared checkers. They refute “many coordinates/constraints/violations force many gates,” but they do not satisfy the full Low/High separator condition and are not counterexamples to Gap-MCSP.

The exact full-promise separator remains

```text
F_enum(T) = OR_{d: |d|≤s1} AND_{a∈{0,1}^n} [ T[a] = Eval(d,a) ],
```

with size `O(N·2^(O(N^β)))`. Prefix/trie sharing may help particular description families, but no worst-case compression of the disjunction over all Low functions has been proved. This attempt does not give a near-linear separator. Its existence as a general construction also does not establish that the displayed enumeration cost is optimal.

## 5. Research decision from the audit

There is no omitted elementary fact in the checked record that turns counting, symmetry, or local consistency into the required gate charge. The repeated failure was to treat a semantic witness as if the separator had to compute or preserve it. The exact unresolved object is the complexity of recognizing a codebook sandwich: include every truth table generated by size-`s1` circuits while accepting no table outside the size-`s2` codebook, with arbitrary behavior in between.

Two legitimate routes remain:

1. **Direct:** prove a numerical gate potential on actual total Boolean functions, bound its growth for AND/OR/NOT with unrestricted fan-out, then force the superlinear `Δ(F)` above from the exact codebook sandwich. Do not posit a non-shareability axiom or introduce a potential without both inequalities.
2. **Source map:** give an explicit multi-output generator `G_x` and prove `YES→L_s1`, `NO→CC(T_x)>s2`, and a source lower-bound margin exceeding `CC(G)+N^(1+ε)`. Audit both endpoints before investing in source hardness.

If the goal is specifically `P≠NP`, OPS is a stronger sufficient target, not a necessary reformulation. Retain OPS as the active priority, but do not mistake its stronger consequence for evidence that an easier P-vs-NP route is impossible.

## 6. Exact frontier and novelty

**Strongest established ordinary bound used:** `N-O(N^β log N)-1`, with the C-406 logarithmic reconvergence refinement. **Known restricted-model result used:** comparator lower bound `N^(1+0.455β)` for fixed `β<1/2`; it does not transfer to unrestricted fan-out. **Native result:** `ρ≥N-o(N)` in its separate model. **Full-promise upper:** `O(N·2^(O(N^β)))`.

C-450 adds a proved description-space endpoint diagnostic and an integrated explanation for why the previous route families stop. It does not add a superlinear lower bound, a near-linear upper bound, or a P-vs-NP proof. The ordinary OPS, native, and P-vs-NP frontiers are unchanged.
