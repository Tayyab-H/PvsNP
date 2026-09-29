# C-384 — Fixed-description selector hardness collapses to the table coordinates

Date: 29 September 2026  
Route: user-directed C-341 continuation; test whether a circuit's address-dependent local OR witnesses can force a state-capacity lower bound or a C-320 splice.  
Classification: **SYNTHESIS OF C-349/C-342/C-367 PLUS A FIXED-SINGLETON CALIBRATION; NO NEW ROUTE.**

**Novelty audit.** C-349 already proves representation dependence of the local witness matrix and explicitly requires an arbitrary-cover transfer; C-342 identifies the activation profile as the only remaining readable selector channel; C-367 separates circuit selection from all-address verification. This note is a synthesis of those prior results, with one incremental calibration: for a fixed table, equality itself has native complexity between `N-o(N)` and `N+O(1)` by C-01/C-03. It does not open a new route or improve q.

## 1. The fixed-description subproblem

Fix one circuit description `d` and write `f_d(x)=C_d(x)`. The table-verification predicate is

```text
V_d(w) = 1 iff for every x, w_x = f_d(x).
```

As a Boolean function of the table bits, this is exactly

```text
V_d(w) = AND over x of ell_(d,x)(w),
ell_(d,x)(w) = w_x if f_d(x)=1, and NOT w_x otherwise.
```

It has an N-literal De Morgan circuit. By the project's C-01 bridge from De Morgan circuits to cyclic intersection complexity, the fixed-description separator has native complexity at most `N+O(1)`. C-03 supplies a matching `N-o(N)` floor when this singleton low table is separated from the actual high set. So the fixed-description problem itself sits at the linear scale, regardless of how many gate/address witness contexts a chosen implementation of `C_d` has.

This gives a direct obstruction to the proposed inference

```text
many forced gate/address actions in M_C  =>  more than N native states.
```

For fixed `d`, the extensional verification predicate has only the N coordinate conditions `ell_(d,x)`. A verifier may have more intermediate residuals, but they are not forced by the function: an O(N)-size separator bypasses the gate trace entirely. A Myhill–Nerode argument based only on this fixed-description predicate therefore cannot charge `N * |C_d|` independent state conditions.

## 2. The selector matrix is not a function invariant

The proposed matrix `M_C(x,g)` depends on the chosen circuit, not just on its truth table. This is not only a concern about relabeling equivalent gates.

For any circuit `C_f` computing `f`, and any circuit `H` computing `h`, form

```text
C'(x) = C_f(x) AND (H(x) OR NOT H(x)).
```

`C'` computes exactly `f`. Yet at the tautological OR gate `g=H OR NOT H`, the forced witness is left when `h(x)=1` and right when `h(x)=0`. Thus the same truth table can be equipped with an address-varying selector pattern of any pattern `h` that fits the available circuit-size slack, while a direct circuit for `f` can omit that gate entirely. Any lower bound based on one selected representation's `M_C` can be inflated without changing the separator's truth function.

Restricting to minimum or canonical circuits would remove this particular padding, but it would introduce a new obligation: prove that every valid C-319 cover uses, or can be converted to, that canonical description. C-319 acceptance is a decision predicate and its positional policy is not known to reveal a minimum circuit. C-367 and C-377 record this decision/search gap. The robust object would have to quantify over all small descriptions of every accepted table and still be extracted from an arbitrary cover.

## 3. Why the universal quantifier is the real target

The target low-table condition is

```text
EXISTS one description d  FOR ALL x: C_d(x)=w_x.
```

If a different description can be chosen at each address, the condition becomes

```text
FOR ALL x  EXISTS d_x: C_(d_x)(x)=w_x,
```

which accepts every table: choose the constant-zero circuit at zero coordinates and the constant-one circuit at one coordinates. Therefore any selector construction must preserve the same `d` across all address challenges.

A C-319 positional strategy does provide one fixed action per state-side pair for a given input table. That can encode a globally consistent configuration at shared configuration states. But it does not make the selected action readable as a register by a different state, and a shared gate state cannot choose opposite OR witnesses for different address callers. C-306, C-329, and C-341 establish those local facts. The missing object is a **joint-description/address continuation**: retain the same selected `d` while the universally challenged address changes, without making every continuation state a `(d-or-gate, x)` product.

For a *supplied* description, the standard universal-circuit checker materializes gate-by-address work and costs `O(N s1 log s1)` ordinary circuit gates (C-367). A native graph that both selects a description and supplies that description coherently to every check has not been constructed; merely duplicating address contexts does not settle global commitment. Compressing the supplied-description work would be construction progress, but `M_C` alone does not prove any product necessary, because (i) it is representation-dependent, and (ii) fixed-description equality has an O(N) separator that bypasses the gates.

## 4. The C-320 splice connection: exact direction of the gap

For one anchor `w`, every context support `K` and replacement proof support `P` at a state that match `w` are mutually compatible. The C-281 substitution law makes `K union P` an accepted output support. Soundness then puts every completion of that support in `SIZE(s2)`. Consequently a genuinely compatible C-281 product cannot itself be a C-320 forbidden high splice; this is the C-382 quantifier correction.

Thus the needed implication is not merely “reuse produces a compatible product.” It would have to prove that completeness forces a particular high owner pattern to occur as a compatible context/proof product. C-320 supplies high patterns once such an owner pattern is forced; it does not force a pattern from a circuit's internal witness matrix. C-384's representation-instability example shows why the matrix cannot supply that forcing on its own.

An incompatible product is not enough either: the support grammar deletes contradictory joins, so it creates no accepting derivation. The decisive missing lemma is a state-capacity theorem connecting (a) an arbitrary cover's actual context/proof families, (b) one-description coherence, and (c) a forced compatible owner pattern. It must handle all alternative small circuits for the same table.

## 5. Construction branch pushed to its current limit

The fixed-circuit verifier is compact: choose the N signed literals `ell_(d,x)` and conjoin them. The obstacle appears only when one fixed graph must cover every low table and ensure all N signs came from one shared circuit description. The standard supplied-description circuit checker costs `O(N s1 log s1)`; that estimate is not itself a C-319 full-cover construction because the description must be selected and remain readable throughout the checks.

Two tempting shortcuts fail exactly:

1. **Local address witnesses.** Allowing each address to choose its own circuit changes `exists d for all x` to `for all x exists d_x`, which is vacuous.
2. **Shared gate selector.** A positional action at a shared gate state is fixed across its callers. It cannot witness `u(x) OR v(x)` by `u` on one address and `v` on another. Duplicating the state by address repairs the toy example but restores the product cost.

An actual near-linear cover still might avoid circuit evaluation altogether and recognize the promise by another recurrence. No such construction follows from C-384. A positive address-multiplexing proposal now has to exhibit its state graph and answer, in the recurrence itself: where the selected description is represented; how an address challenge reaches the appropriate coordinate; how the description remains coherent after that routing; and why every accepting support remains inside `SIZE(s2)`.

## 6. Literature check

The literature search found formula-versus-circuit separations in restricted bases and time-space tradeoffs for branching programs. These establish that sharing and state/time resources can separate computation models, but neither result is a lower bound for the exact C-319 least-fixed-point recurrence or its Gap-MCSP promise. In particular, restricted formula lower bounds cannot be imported without a size-preserving C-319-to-formula compiler; C-339/C-362 already show the current generic compiler loses too much. Examples: [Rossman and Srinivasan, *Separation of AC0[⊕] Formulas and Circuits*](https://theoryofcomputing.org/articles/v015a017/) and [Beame, Saks, and Thathachar, *Time-Space Tradeoffs for Branching Programs*](https://homes.cs.washington.edu/~beame/papers/branch.pdf).

## 7. Checkpoint and next proof obligation

- Native lower bound above `N-o(N)`: **NO**.
- State-capacity theorem from the raw fixed-circuit matrix: **NO; this representation-level route is closed**.
- Selector family forcing a C-320-compatible high splice: **NO**.
- Full-promise `N^(1+o(1))` cover: **NO**.
- P-versus-NP proof: **NO**.

The next useful theorem concerns the remaining **activation-code channel**, not another raw selector matrix: either prove that every arbitrary valid cover's seed-signature/activation profile admits a coherent small-circuit decoder on low inputs, then bound the resources for that decoder and all-address check; or prove a state-sensitive obstruction to such a decoder that does not assume one exists. C-363/C-383 show raw profile capacity is enough at q=Theta(N), while C-342/C-366 show capacity does not supply an observable selector or a search-to-decision extraction. No canonical-circuit extraction may be assumed. The state lower bound remains `rho_GapMCSP >= N-o(N)` and the research goal remains active.
