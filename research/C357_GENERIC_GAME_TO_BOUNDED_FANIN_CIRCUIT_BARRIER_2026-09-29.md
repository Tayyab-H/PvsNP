# C-357 - A q-state reachability readout can require near-quadratic ordinary circuit size

Date: 29 September 2026  
Route: audit whether the generic C-319 least-fixed-point readout admits a subquadratic bounded-fan-in circuit compiler.  
Classification: **GENERIC MODEL LOWER BOUND; DOES NOT CHARGE GAP-MCSP q.**

## 1. Abstract recurrence

Consider q states with independent Boolean seed inputs `a_i,b_i` and fixed predecessor sets `P_i,Q_i`:

```text
x_i = (a_i OR OR_{j in P_i} x_j) AND (b_i OR OR_{j in Q_i} x_j),
```

interpreted as the least fixed point, with one designated output state. This is the abstract q-state readout part of C-319 before imposing endpoint realizability and before substituting the table-literal seed clauses.

## 2. Many functions represented by O(h)-state recurrences

Fix h variables `y_1,...,y_h`, let `k=floor(h/2)`, and let `M=binomial(h,k)`. For each choice `C` of h distinct k-subsets of `[h]`, define the monotone CNF

```text
f_C(y) = AND_{S in C} OR_{i in S} y_i.
```

These functions are distinct. For a k-subset T, set `y_i=0` exactly for i in T. Then a k-literal clause indexed by S is false exactly when S=T, so `f_C(y)=0` iff `T in C`. The number of functions is therefore

```text
binomial(M,h) = 2^(Omega(h^2)).
```

Each `f_C` is computed by a q-state recurrence with `q=3h-1` states: h states activate directly from the h seed inputs y_i; h clause states OR the selected predecessor variable states; and h-1 states form a binary AND tree over the clauses. At each variable state one obligation has seed y_i and the other has constant-true seed. At a clause state one obligation is constant true and the other is the OR of its selected variable-state predecessors. At an AND-tree state the two obligations are its two child states. The designated output is the tree root. Unused seed inputs are fixed constants.

## 3. Counting lower bound for bounded-fan-in circuits

The number of bounded-fan-in Boolean circuits of S gates on h inputs is at most `2^(O(S log(S+h)))`. If all the `2^(Omega(h^2))` functions above had circuits of size at most `c h^2/log h`, the circuit count would be `2^(O(c h^2))`. Choosing c sufficiently small contradicts the number of functions. Hence some O(h)-state reachability readouts require

```text
Omega(h^2/log h) = Omega(q^2/log q)
```

ordinary bounded-fan-in circuit gates, even allowing NOT gates.

This rules out a generic compiler that converts every q-state reachability readout into a bounded-fan-in circuit of size `O(q^(2-epsilon))` for any fixed epsilon>0. It explains why direct graph-game readout is not automatically a near-linear standard-circuit route.

## 4. Scope limits and literature check

This is not a lower bound for the actual Gap-MCSP acceptance function and does not charge the q of a valid cover. The constructed seed predicates are independent inputs; C-319 seeds in an actual cover are signed-literal disjunctions tied to the same table, and its predecessor sets must come from endpoints. Moreover, the lower bound counts **all** fan-in-two gates. In the project's `A_cap` measure, unbounded OR fan-in is free and these CNFs need only O(h) paid AND gates. Thus C-357 does not prove that the existing q-squared paid-AND unrolling is tight, nor that improving that compiler is impossible in the specialized model.

Pauly's *Parameterized Games and Parameterized Automata* identifies reachability graph-game forms as a concise representation of monotone functions, notes that tree-unfolding can produce a significantly larger circuit, and explicitly asks what circuit size is required for the least-fixed-point operation (Open Question 11). This is the relevant generic model boundary, not a transfer theorem for Gap-MCSP: [Pauly, EPTCS 277 (2018), DOI 10.4204/EPTCS.277.3](https://doi.org/10.4204/EPTCS.277.3).

**Decision:** retire attempts to obtain a general subquadratic *bounded-fan-in total-gate* compiler as the route to the project target. Keep the exact C-319 game primary. A specialized `A_cap` compiler remains open only if it uses the endpoint/seed structure and yields a result for the actual promise; otherwise return to a direct q-sensitive theorem or a full-promise near-linear cover. No checkpoint changes: `rho_GapMCSP>=N-o(N)` and no P-vs-NP proof.
