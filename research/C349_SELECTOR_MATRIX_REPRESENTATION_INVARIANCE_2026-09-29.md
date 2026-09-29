# C-349 - A chosen circuit's lane-selector matrix is not a cover invariant

Date: 29 September 2026  
Route: C-341 continuation; audit whether a hard local-witness matrix can force state cost for an arbitrary C-319 cover.  
Classification: **EXACT CIRCUIT NORMALIZATION + TRANSFER GAP; NO q IMPROVEMENT.**

## 1. The quantifier the proposed selector argument needs

For a circuit description `C`, address `x`, and gate `g`, one can define a local witness action `M_C(x,g)` when a claimed gate value is proved by choosing a true child of an OR gate. A rich matrix `M_C` is a plausible obstruction to sharing one positional state across many addresses.

But the cover accepts tables, not circuit descriptions. Completeness says that each low table has *some* small circuit; it does not require a proof to use a selected description or its gate witnesses. Therefore a lower bound on `M_C` for one chosen representation only transfers if the property is invariant over all equivalent size-`O(s1)` representations and is connected to every valid native proof grammar. Neither transfer is currently established.

## 2. Exact representation changes

Two elementary normalizations show why an OR-witness matrix alone is not invariant.

**Output padding.** For any circuit `C` computing `f`, append the output gate

```text
f' = f OR 0.
```

This adds one gate. On every address where the output is 1, the new OR has the unique true child on the left. Thus the output-gate selector can always be made constant, regardless of the truth table. Conversely, the same constant function 1 has the small representation `x_1 OR not x_1`, whose unique true child varies with `x_1`, as well as the constant-one circuit. The output selector is a property of the chosen representation, not of the table.

**Disjoint-OR normalization.** Replace every binary OR `u OR v` by

```text
u OR (v AND NOT u).
```

The children are disjoint on every input, the function is unchanged, and at most two gates are added per original OR gate. Hence a size-`s` circuit has an equivalent size-at-most-`3s` circuit in which each OR witness is unique whenever the gate output is 1. The witness is then a deterministic function of the address and the left-child value. In addition, replacing `u OR v` by `NOT((NOT u) AND (NOT v))` eliminates OR gates entirely with at most a constant-factor size increase. A proposed complexity measure that counts only positive-OR witness choices can therefore change or disappear under a standard basis change.

These transformations do **not** prove that all address dependence disappears. They prove that the particular local witness labels are not canonical. A basis-robust version must include gate values/polarities and all equivalent small descriptions, rather than only the OR choices in one topology.

## 3. What survives the audit

Circuit evaluation has a unique gate-value vector `V_C(x)` for each `(C,x)`. One may encode a verifier by guessing or computing that vector and checking each local gate relation. This removes the arbitrary existential choice of a true OR child, but the full evaluation object is still the address-by-gate matrix

```text
T_C[x,g] = V_C(x)_g.
```

The unresolved compression question is whether one fixed C-319 graph can use the same global description across all rows of this matrix while exposing the right row/gate entry at each check. C-341 shows that the proposed shared selector state loses the row address. Replacing local witnesses by the unique value trace changes the interface; it does not construct the missing readout or imply that `N*s1` states are necessary.

There is also a quantifier boundary: an arbitrary valid cover need not verify any circuit, so even a lower bound on every circuit-evaluation encoding is not a lower bound on `q` without a reduction from arbitrary covers to that interface. C-342's input-derived activation code remains a possible channel because at `q=Theta(N)` its raw capacity is sufficient; its coherent circuit-description readout is still open.

## 4. Revised theorem target

Retire the claim that hardness of `M_C(x,g)` for a selected circuit description alone forces many native states. A viable result must do at least one of the following:

1. define a representation-invariant description/address measure and prove a lower bound for every size-`O(s1)` representation of an explicit low-table family, then show arbitrary sound C-319 covers induce that measure; or
2. avoid circuit representations and derive a direct state-sensitive bound from the C-319 seed signature, least-fixed-point graph, and C-281 compatible context/proof products; or
3. give an explicit full-promise near-linear cover whose activation/readout implements a circuit choice coherently.

Any proposed family still needs to pass C-257 parity, C-258 repeated equality, C-307 local constraints, C-317 safe cylinders, and C-320's owner-mask splice tests. The next concrete construction test is to replace the OR-witness matrix by the canonical gate-value relation, then identify exactly what state in the native graph can read a selected `(address,gate)` value without a product state or caller history.

## 5. Checkpoint

The proof establishes a limitation of the proposed selector-matrix argument, not a lower bound. It does not refute every shared-description construction. The actual native lower bound remains `q >= N-o(N)`; no superlinear full-promise bound, near-linear full-promise cover, positive CohEnc transfer, general reconstruction compiler, or P-vs-NP proof follows.

## 6. Required A-E checkpoint and mechanism change

- **A.** Native lower bound above `N-o(N)`? **No.**
- **B.** General state-capacity theorem from C-341? **No.** The mux/path results remain architecture-specific.
- **C.** Selector-hard low family forcing a C-320 forbidden splice? **No.** A hard matrix for one chosen circuit does not bind an arbitrary cover.
- **D.** Full-promise near-linear cover? **No.**
- **E.** Lower-bound-preserving communication, rectangle, or residual-state formulation? **No.** No reduction from arbitrary covers to the circuit-evaluation interface is known.

All five answers are negative, so the next phase changes mechanism. Stop refining circuit-local selector matrices. Work directly with the C-281 support grammar: for each reused state, relate low-table context supports to replacement-proof supports by compatibility, label each compatible pair with its owner mask and splice cylinder, and seek a state-capacity theorem from the *grammar that generates these supports*. Support geometry alone cannot supply the theorem: assigning `K=P=ell(w)` for each anchor makes every distinct-anchor cross-pair incompatible, regardless of how many anchors reuse the state. The missing charge must come from the number and arrangement of native rules needed to generate such anchor-specific full supports while excluding high tables. This is the forced-splice branch (Outcome 3), not a new selector normal form.
