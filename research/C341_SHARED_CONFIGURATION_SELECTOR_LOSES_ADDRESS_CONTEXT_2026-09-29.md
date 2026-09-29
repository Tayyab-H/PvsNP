# C-341 — A shared configuration selector loses its address context

Date: 29 September 2026  
Route: Q199 / audit a proposed shared positional selector for circuit-gate configurations.  
Classification: **CONSTRUCTION-SPECIFIC NO-GO; NO GENERAL LOWER BOUND.**

## 1. Exact question

The proposed compression had one shared selector state per circuit gate. Its positional existential choice would select a gate configuration (operation and predecessor wires), while address-specific verifier states would query that selector and then evaluate the chosen configuration. A rough count suggested one address layer plus a polynomial number of configuration states, rather than one state per gate and address.

The unresolved point is not the count of configurations. It is whether the selected configuration can be used later while retaining the address that caused the query.

## 2. State-merging lemma

Fix an input table `w` and a state `v` in the C-319 reachability game. Any two play histories that end at `v` have the same continuation game: the available actions and all later states depend on `v` and `w`, not on the incoming history. Equivalently, in the least-fixed-point equations, the winning value of `v` at every round is a function only of `v`, the fixed seed clauses evaluated on `w`, and predecessor values from the previous round. It has no argument for the caller or its address.

Consequently, if address-query states `V_(g,a)` and `V_(g,b)` both enter one selector state `S_g`, then after the visit to `S_g` the continuation cannot distinguish whether it came from address `a` or `b`. A positional strategy chooses an action for each of the two side-obligations at `S_g`; fixing the same side, that action cannot depend on whether the caller was `a` or `b`. It can select a configuration `c`, and the successor can retain `c`; that successor does not thereby retain `a` or `b`.

This rules out a return-to-caller interpretation of the shared selector. A graph edge has no stack frame that restores the incoming address after the selector acts.

## 3. Selecting the gate configuration is not enough

Even if a route state `R_(g,c)` remembers the selected configuration, evaluating a circuit OR gate requires a witness that may depend on the challenged address. For example, let

```text
u(x)=x_1,   v(x)=not x_1,   g(x)=u(x) OR v(x)=1.
```

To certify `g(x)=1` for every address, the local OR witness must choose `u` when `x_1=1` and `v` when `x_1=0`. If the two lanes reach the same OR-state side-obligation, its single positional action cannot make both choices. Selecting the gate's operation and wires once globally does not provide this separate lane-dependent witness choice.

Thus the proposed selector misses two distinct pieces of information flow:

1. the address must survive a visit to a shared configuration selector; and
2. the evaluation witness for a fixed OR gate may vary with that address.

This is consistent with C-329's two-lane obstruction and C-331's observation that a selected game action is not a value another state can read. C-341 isolates why adding configuration-specific route states does not repair either issue by itself.

## 4. Scope and repair cost

One can preserve both indices explicitly with states such as `R_(g,c,a)`, or add a new mechanism that transmits the address and makes selected configuration data readable in every address context. The first option restores a gate/configuration/address product in the direct architecture. The second needs an explicit construction and a proof that its readout remains globally coherent under every universal challenge and sound under C-281-compatible substitutions.

No lower bound is proved for arbitrary endpoint-induced graphs or compatible-support encodings. In particular, the state-merging argument does not show that every native cover needs `N*s1` states, or any superlinear number. It refutes only the proposed shared-positional-selector architecture and its unsubstantiated `O(N+s^3)` count.

## 5. Research consequence

Keep Q199 open, but require any positive selector proposal to identify a concrete communication channel from the globally chosen description to every address check. A positional action alone is not such a channel; support annotations alone are ruled out by C-306; an active marker would need an exclusivity, persistence, and readout proof. Then price that mechanism and verify the full promise.

The result is local route-filter progress only. The proved native bound remains `rho_GapMCSP >= N-o(N)`. No full-promise near-linear cover, positive `CycAnd-CohEnc` margin, superlinear state lower bound, or P-vs-NP proof follows.
