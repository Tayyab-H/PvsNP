# C-340 - The gate-address evaluator is not a full-promise cover

Date: 29 September 2026  
Route: audit whether C-305's N*s1 verifier supplies a full-promise cover and conflicts with the fixed-epsilon OPS target.  
Classification: **QUANTIFIER AUDIT / NO COVER UPPER BOUND.**

## 1. The target quantifiers

Oliveira, Pich, and Santhanam Theorem 1.4 states: there is a fixed epsilon>0 such that for every sufficiently small fixed beta>0, Gap-MCSP[2^(beta*n)/(c*n), 2^(beta*n)] is not in Circuit[N^(1+epsilon)]. This is circuit-family nonmembership, and the parameters are s1=N^beta/(c log N), s2=N^beta. The primary theorem is [Theorem 1.4 in Hardness Magnification Near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).

If a genuine full-promise native cover had q=O(N*s1)=O(N^(1+beta)/log N) for all sufficiently small beta, then choosing beta<epsilon would give q=o(N^(1+epsilon)). That would refute the project's proposed superlinear lower bound on rho. It would kill this sufficient rho-route; it would not itself contradict Theorem 1.4's ordinary-circuit nonmembership, because the current q-to-circuit unrolling costs q^2.

## 2. Why C-305 does not supply that cover

C-305 counts (gate,address) positions for evaluating a supplied size-s1 circuit on all N addresses. The construction is parameterized by that circuit description. It is not one fixed Q that accepts every table in SIZE(s1) and rejects every table above s2.

The needed quantifiers are:

    one fixed Q:
      for every w in SIZE(s1), there exists a winning strategy encoding some C_w;
      for every z with CC(z)>s2, no winning strategy exists.

The verifier for one supplied C establishes only the inner consistency check. Taking a separate Q_C for each circuit does not produce the one Q required by the cover definition. Combining all Q_C requires a global description selector and must preserve the same circuit wiring across every universal address challenge.

The address-product evaluator exposes the obstruction. If each (gate,address) state chooses its own predecessor, the strategy can use different gate wiring at different addresses and certify a piecewise table. If one gate state is shared across addresses, it no longer carries the challenged address needed to query w_x. C-306 rules out storing that address only in proof/context supports: state activation forgets support provenance, and all same-anchor supports are compatible.

Thus N*s1 is an architecture cost for a fixed-description evaluator, not an upper bound on rho_GapMCSP. The missing operation is a single global circuit-description choice whose consistency survives all address branches. C-305/C-306 identify this as the same unresolved synchronization problem as O-167/O-168.

## 3. Disposition

There is no contradiction between the fixed-epsilon target and the C-305 parameter count. No valid full-promise cover of size O(N*s1) has been constructed, and no new upper bound or lower bound follows. Continue only if the description selector is implemented as one sound fixed state graph or a q-sensitive theorem proves that this cannot be done.

## 4. Checkpoint

- OPS fixed-epsilon quantifier: verified from the published theorem.
- C-305 as a fixed-description evaluator: verified from its construction.
- Valid full-promise q=O(N*s1) cover: absent.
- Actual proved lower bound: rho_GapMCSP >= N-o(N).
- Superlinear q bound, near-linear full-promise cover, and P-vs-NP proof: absent.
