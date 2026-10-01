# C-430 — Hyperedge addresses block the direct OPS transfer

**Status:** proved a shared-gate composition lemma and the exact gap condition for ignored-variable padding, then checked the Hirahara–Ilango FOCS 2025 and Huang–Ilango–Ren TR23-046 routes. Both source results are genuine in their stated settings; neither transfers to an ordinary OPS lower bound through the tested bridge. No quantitative-frontier change.

## 1. Exact target and transfer mechanism

Write an OPS target table as a Boolean function on `D` input bits, of truth-table length `N=2^D`. The published Theorem 1.4 states its denominator as a universal constant `c>=1`; Section 4.1 of the proof gives the concrete parameter setting `c=10` (up to integer rounding). Keep both forms distinct. The general thresholds are

```text
YES: CC(f) <= s1 = 2^(beta D)/(cD)
NO:  CC(f) >  s2 = 2^(beta D)
```

The quantifier is one fixed `epsilon>0` such that, for every sufficiently small fixed `beta>0`, the promise is outside `Circuit[N^(1+epsilon)]`; Theorem 1.4 then implies `NP` is not contained in polynomial-size circuits. This is the ordinary total fan-in-two gate measure. The concrete proof instantiation uses `c=10`, so the denominator is `10D`; the theorem statement itself only promises a universal constant `c`.

**Shared-gate composition lemma.** Let a source predicate `L(x)` be computed as `P(A(G_1(x),...,G_t(x)))`, where every `G_j(x)` is a promised OPS truth table, all table-generation circuits together use `R` gates, `A` is an arbitrary `S`-gate separator, and `P` is a `b`-gate postprocessor receiving only the separator outputs (plus constants). Then `L` has an ordinary circuit of at most `R+tS+b` gates. Connecting separate copies proves the upper bound; common gates may then be merged, so unrestricted reuse only lowers the actual cost. Consequently, if every circuit for `L` needs at least `H` gates, then `S >= (H-R-b)/t`. If `P` or another part of the reduction reads raw source bits or performs additional work, those gates must be included as well. This theorem makes the sharing accounting explicit, without assuming any internal representation of `A`. It improves an OPS lower bound only when a source lower bound `H` exceeds all generator/postprocessor costs and the query multiplicity is small enough.

### The exact missing inequality for the OPS target

This is a complete composition theorem, but it yields the requested lower bound only if one supplies a source predicate with an ordinary circuit lower bound `H` and a promise-preserving reduction satisfying `H > R+b+t*N^(1+epsilon)` for the same fixed `epsilon` and every sufficiently small fixed `beta`. Then `R+tS+b` contradicts `H` whenever `S<=N^(1+epsilon)`. Neither cited route meets this condition: the HI direct/padded promise misses the required gap-to-dimension ratio, and the HIR oracle route has no proved ordinary YES evaluator below its hard-side threshold. I do not assume an unproved direct-sum or non-shareability theorem to fill this gap. The complete OPS lower-bound attempt therefore stops at this explicit inequality, with no frontier improvement.
For the simplest proposed bridge, let a source promise on `k`-bit functions have YES `CC(f)<=s` and NO `CC(f)>=g s`. Pad a source function by ignored variables:

```text
f'(x,z) = f(x),   x in {0,1}^k, z in {0,1}^{D-k}.
```

Then `CC(f')=CC(f)` under the usual free-constant convention; if constants are charged, fixing `z=0` costs at most `O(1)` shared gates. To place this source promise inside OPS at dimension `D`, thresholds must satisfy

```text
c D s <= 2^(beta D) < g s.
```

Therefore **a necessary condition for any such padding transfer is `g>cD`**. For the concrete `c=10` instantiation this is `g>10D`. Since `D>=k`, the needed multiplicative gap is already greater than `c k`; for fixed small `beta`, the first inequality also requires

```text
D >= (log2(c D s))/beta.
```

Thus padding increases the required gap and never amplifies it.

## 2. Parameter audit of Hirahara–Ilango (FOCS 2025)

Theorem V.7 proves, under its stated NIWI and circuit-hardness assumptions, NP-hardness of a promise `Pi` with a constant-factor circuit-size gap and additional time-bounded Kolmogorov-complexity conditions. A valid MCSP separator at matching circuit thresholds would decide `Pi`; the Kt side conditions need not be inferred from the separator. Remark V.8 gives a growing polylogarithmic approximation factor for a growing hypergraph-uniformity parameter.

In the reduction, the function `f_{psi,E}` takes an edge `e in [n]^tau` as part of its input, together with per-vertex ciphertext coordinates and a proof coordinate. With ordered tuple encoding this costs `tau*log2(n)` bits; even if the edge is canonically represented as an unordered subset, its name needs at least `log2(binomial(n,tau)) = Omega(tau*log2(n/tau))` bits. In the theorem's polylogarithmic range for `tau`, this is `Theta(tau log n)`. Thus its input dimension `k_HI` satisfies

```text
k_HI >= Omega(tau * log2(n/tau)) = Theta(tau * log2(n)).
```

The other coordinates only increase `k_HI`. The YES circuit bound is

```text
CC(f_{psi,E}) <= O(gamma*n*lambda/(tau*log(lambda)) + tau^3*Q)
                 + poly(n^tau),
```

and the soundness proof derives a circuit-complexity gap proportional to `tau` (its final parameter comparison is `CC(f_{psi,E}) >= Omega(delta*tau*S)`). The polylogarithmic-factor remark is consistent with this scaling. The proof chooses `lambda=n^(c*tau)` to dominate the `poly(n^tau)` costs.

But a direct/padded OPS transfer would require `g>cD` (or `g>10D` at the concrete instantiation), with `D>=Omega(tau*log2(n/tau))`, whereas the displayed proof guarantees a factor on the order of `tau` up to constants. In the allowed regime this is short by a factor of order `log n`, before accounting for the extra ciphertext and proof bits or the stronger `D` forced by small `beta`. Choosing larger `tau` does not remove the factor: it increases both the achieved gap and the edge-address width linearly, while retaining the `log n` tax.

This is a **failed transfer**, not a refutation of the conditional MCSP hardness theorem. It rules out only using its existing circuit gap, with ignored-variable padding or direct threshold inheritance, as an OPS-gap reduction. A new encoding could still avoid exposing an edge as a `tau`-tuple, but it must preserve the soundness step that turns successful prediction on every edge into a large vertex cover.

## 3. Second literature route: near-optimal oracle-MCSP hardness

Huang–Ilango–Ren's primary ECCC TR23-046 gives a stronger-looking starting promise than the ordinary HI reduction: Theorem 4.1 has YES `CC^O(f)<=2^(epsilon*n)` and NO approximate oracle-circuit complexity above `2^(0.3n)`. The NO condition implies ordinary exact `CC(f)>2^(0.3n)`, since every ordinary circuit is also an `O`-oracle circuit. This initially appears to supply the required high side.

The YES side is the failure. In the reduction, `n=ceil(3k log2(M)/epsilon)`, `lambda=10kn`, and the combined oracle is queried on `r=1+k*lambda=1+10k^2*n` bits. Its truth table has `2^r=2^(1+10k^2*n)` entries, while the NO lower bound is only `2^(0.3n)`. Replacing one arbitrary oracle lookup by a generic ordinary circuit costs `O(2^r)` gates; batching shared lookups avoids a separate copy for each query, but still pays a dictionary term of order `2^r` per dependency layer. No special small ordinary circuit for this constructed oracle is proved. The fallback ordinary truth-table synthesis for the random `f` costs `O(2^n/n)`, also far above the NO scale `2^(0.3n)`.

Thus the random-oracle result does not furnish an ordinary OPS promise by de-oracling. This is an exact resource mismatch, not a claim that the oracle function must have `Omega(2^r/r)` gates: the paper's structured oracle distribution may admit a special representation, but obtaining one below the NO threshold is a new theorem. This route is distinct from the HI edge-address tax and reaches the same transfer failure for a different reason: its apparent hardness uses oracle computation whose ordinary implementation cost overwhelms its hard-side scale.

## 4. Serious attempts to remove the address tax

1. **Fix the edge coordinate.** This destroys the quantifier used in soundness. The proof obtains, for each `e in E`, a vertex of `e` whose key is recoverable; the contradiction comes from this set meeting every edge. One fixed `e` gives information about only that edge and cannot establish a global vertex-cover lower bound.
2. **Encode `e` more compactly.** An injective name for every possible `tau`-tuple in `[n]^tau` requires `tau*log2(n)-O(tau)` bits. Naming only edges of the actual `E` could be shorter if `E` has special structure, but the reduction needs a representation-specific theorem and a circuit for the edge-name decoder. No such bound in the cited theorem removes the `tau log n` coordinate cost.
3. **Amplify the gap by repeating instances.** This needs a proved lower bound under unrestricted circuit sharing. Repeated copies alone do not provide one: the function `F(x_1,...,x_t)=f(x_1)` has exactly the complexity of `f`, and coordinatewise repeated outputs can reuse the same computation. The direct-product route therefore has no gate-additivity theorem here.

These failures change the mechanism: retain black-box composition as the right way to account for arbitrary sharing, but require the reduction's achieved gap to be compared with its *actual target input dimension*, not just with the source's key length or output-table entropy.

## 5. Shared-computation countertests

The usual incidence charges do not repair this gap mismatch. Parity on `N` bits has an `O(N)` shared readout (constant-size AND/OR/NOT gadgets per XOR); repeated-block equality uses `O(N)` gates; `m` sparse parity checks with `O(N)` total incidences use `O(N)` gates; and copy/complement or other fixed simple block relations can be computed and checked in `O(N+R)` gates. These are not Gap-MCSP separators and do not refute the FOCS reduction. They refute charging its apparent number of uses or constraint incidences as independent gates. C-429 contains the explicit implementations and full-promise caveats.

## 6. Paired full-promise separator construction attempt

For every OPS table, enumerate all `K=2^(O(s1*log(s1+D)))=2^(O(N^beta))` circuit descriptions of size at most `s1`. For each description, compare its complete truth table with the input using `O(N)` gates; OR the equality flags. This accepts every promised YES and rejects every promised NO, with behavior in the middle irrelevant. Its ordinary total-gate count is

```text
O(N K) = O(N * 2^(O(N^beta))).
```

Trying to share across candidates with a prefix trie only shares common prefixes of their truth tables; the worst-case trie has up to `N*K` labeled positions. No structural bound on the low-circuit family giving a near-linear trie or another complete separator was proved. The OPS anti-checker construction gives an `N^(1+epsilon)`-scale full-promise separator only conditionally under `NP subseteq P/poly`; it is not an unconditional upper bound.

## 7. Model, assumptions, barriers, and originality

- **Gates:** `CC` is ordinary Boolean circuit size, counted in gates. Any basis normalization costs a constant factor; the comparison here is between multiplicative gaps that miss by a growing `log n` factor. This report proves no paid-AND, OR-only, wire, or native fusion bound.
- **Other resources:** the FOCS reduction is deterministic quasipolynomial-time; its runtime and description length are not gate costs. Composing an OPS separator with a fully specified table-generation circuit must add the generator gates and all queries/postprocessing. The failed parameter match means no such composed SAT circuit is claimed.
- **Assumptions:** Hirahara–Ilango's reduction is conditional on the assumptions in Theorem V.7. This cycle proves no new cryptographic or complexity assumption and no unconditional hardness.
- **Related literature:** Huang–Ilango–Ren TR23-046 proves a near-optimal gap for oracle circuit complexity in its oracle model. Its truth-table oracle has input width `1+10k^2*n` in their parameter setting, so generic de-oracling does not yield an ordinary OPS YES circuit below the NO scale.
- **Known barriers:** the Chen et al. locality barrier is technique-specific. This global reduction audit neither bypasses nor strengthens it.
- **Originality:** the padding equality and ratio condition are elementary project-level lemmas. The FOCS reduction is established literature. The address-width comparison is an application/audit, not a new hardness theorem.

## 8. Result and frontier

**Strongest proved statement this cycle:** any source MCSP promise transferred by ignored-variable padding into the OPS thresholds must have multiplicative gap `g>cD` (and `g>10D` for the explicit `c=10` instantiation); Hirahara–Ilango's edge-indexed construction has `D>=tau log2(n)` but a proved gap scaling with `tau`, so the direct transfer fails by at least a logarithmic factor in `n` (and more at small `beta`).

**Decisive obstruction:** the reduction's soundness needs all hyperedges, but its target function pays `Omega(tau log(n/tau))=Theta(tau log n)` input bits merely to name one edge. Its guaranteed gap grows only with `tau`. The missing mathematical step is an edge-address-efficient encoding or a different hard source whose circuit gap grows at least as fast as the final target's input dimension, with full circuit-composition costs proved.

**Quantitative frontier: unchanged.** The ordinary unconditional lower bound remains `S>=N-O(N^beta log N)-1` with C-406's additive logarithmic refinement. The OPS `N^(1+epsilon)` target remains open. The exact unconditional full-promise upper is `O(N*2^(O(N^beta)))`. Native `rho_GapMCSP>=N-o(N)` remains separate.

### Primary sources

- Hirahara and Ilango, [*NP-hardness of the Minimum Circuit Size Problem from Well-Studied Assumptions* (FOCS 2025)](https://www.rahulilango.com/papers/MCSP-Proceedings-2025.pdf), Theorem V.7, Lemmas V.2–V.3, Remark V.8.
- Huang, Ilango, and Ren, [*NP-Hardness of Approximating Meta-Complexity: A Cryptographic Approach* (ECCC TR23-046)](https://eccc.weizmann.ac.il/report/2023/046/download), Theorem 4.1 and the de-oracling parameters in Theorem 4.5.
- Oliveira, Pich, and Santhanam, [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Definition 2.4 and Theorem 1.4.
- Dinur, Guruswami, Khot, and Regev, [*A New Multilayered PCP and the Hardness of Hypergraph Vertex Cover*](https://cims.nyu.edu/~regev/papers/hyper_vc.pdf), for the variable-uniformity vertex-cover hardness used by the reduction.
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://eccc.weizmann.ac.il/report/2019/168/download/), for the scope of the locality barrier.
