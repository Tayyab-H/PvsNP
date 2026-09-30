# C-400 - Address-varying multiplexer witnesses do not force superlinear native states

Date: 29 September 2026  
Route: continue C-341's requested mux/ISA toy model and test whether address-dependent OR witnesses force a state-capacity cost.  
Classification: **EXPLICIT LOW FAMILY WITH MANY LOCAL WITNESS CONTEXTS; VALID `N-o(N) <= q <= 2N` SUBPROMISE COVER; NO FULL-PROMISE RESULT.**

## 1. Family and parameters

Let `N=2^n`, fix a constant `0<beta<1`, and set

```text
r = floor(beta*n/2),   M=2^r,   K=2^(n-r),   N=M*K.
```

Index the N table coordinates by `(a,z) in {0,1}^r x {0,1}^{n-r}`. For each `y in {0,1}^M`, define

```text
f_y(a,z)=y_a.
```

This is an address multiplexer: `a` selects one of M data bits, and `z` is ignored. A bounded-fan-in DNF with one minterm for each `a` such that `y_a=1` computes `f_y`, so

```text
CC(f_y) = O(M*r) = O(N^(beta/2) log N) <= s1=N^beta/(c log N)
```

for every fixed c and all sufficiently large N. Hence the family `F={f_y:y in {0,1}^M}` lies wholly in the low set. It contains `2^M` distinct tables.

In this DNF representation, if `y_a=1`, then on input `(a,z)` the term for `a` is the unique true minterm. Thus a table with many 1s in y exhibits many different forced OR-witness locations across its address contexts. This is a property of the chosen representation; C-384 already warns that representation-dependent matrices cannot by themselves lower-bound arbitrary separators.

## 2. Exact separator by fiber consistency

The family has a direct extensional description:

```text
w in F  iff  for every a and every z != 0,  w_(a,z)=w_(a,0).
```

There are `N-M` such equalities. For each pair of table bits `u=w_(a,z)` and `v=w_(a,0)`, write

```text
u=v  iff  (not u OR v) AND (u OR not v).
```

This yields a monotone circuit over signed-literal inputs with one binary AND per equality and `N-M-1` more binary ANDs to conjoin all equalities. Its total paid-AND count is

```text
A_cap <= 2(N-M)-1 < 2N.
```

The circuit accepts exactly F, so it accepts every member of `F` and rejects every high table; its behavior on other low or medium tables is irrelevant to this subpromise. Every signed literal half-cube meets the high set because the high set has size `2^N-2^{o(N)}`. C-307 therefore compiles this separator into a valid native cover with

```text
q <= A_cap < 2N.
```

Conversely, any cover accepting at least one member of F and rejecting all high tables obeys the project's one-anchor bound `q>=N-o(N)`. Thus the native complexity of this mux-family subpromise is pinned to the linear scale:

```text
N-o(N) <= rho_prom(F, HIGH) < 2N.
```

## 3. What this resolves and what it does not

This answers the toy question in one direction: a large set of address-varying OR witnesses does **not** force a superlinear native state count. The endpoint-valid cover avoids evaluating the chosen circuit's gate witnesses entirely; it tests the repeated-fiber invariant of the resulting truth tables. The recurrence's semantic endpoints can therefore bypass the particular address-memory bottleneck in the evaluator architecture.

This is not a full-promise `q=O(N)` cover. The family has only `M=N^(beta/2)` free bits and a simple O(N)-size consistency test. The construction establishes neither a global circuit-description selector nor coverage of all `SIZE(s1)`. It also does not refute a selector-capacity theorem for a family whose truth-table membership has no such linear separator.

## 4. Updated family-design requirement

A selector-hard low family cannot be selected merely for rich gate/address witness variation. Before trying C-320 owner-mask forcing, first rule out an O(N) signed local-constraint separator for membership in the family. In particular, avoid repeated fibers, sparse checks, and other directly testable coordinate redundancies. The remaining challenge is to construct a sufficiently rich low-circuit family with no such simple extensional test, then prove that reuse in an arbitrary valid C-319 graph creates a **compatible** high splice. C-400 supplies no such forcing lemma.

### Required checkpoint

- Actual full-promise q bound above `N-o(N)`: **No.**
- General state-capacity theorem from C-341: **No.** This family shows local witness diversity alone is insufficient.
- Selector-hard low family forcing C-320 high splices: **No.** The chosen mux family is easy to recognize by fiber equalities.
- Near-linear full-promise cover: **No.** Only this subpromise has a linear-size separator.
- Lower-bound-preserving communication/rectangle formulation: **No.**

The next attack must change mechanism: construct a low family whose extensional membership is itself hard for linear signed local constraints, or derive a graph-specific state/readout charge directly on the whole promise. The proven full-promise bound remains `q>=N-o(N)`.
