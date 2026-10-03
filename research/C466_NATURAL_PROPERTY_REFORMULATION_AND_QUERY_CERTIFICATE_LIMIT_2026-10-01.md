# C-466 - the average-case route is a natural property, and its query charge stops short of gates

**Status:** exact reformulation and a restricted-model lemma proved; no ordinary-circuit lower-bound improvement.

## Parameters and exact separator implication

Let `N=2^n`, fix `0<beta<1`, let `t=floor(N^beta/(10n))`, and let `u=floor(N^beta)`. An OPS separator is a total Boolean function `F` on `N` table bits satisfying

`CC_n(T)<=t => F(T)=1`, and `CC_n(T)>N^beta => F(T)=0`.

The middle band is unrestricted. Put `R_F={T:F(T)=0}`. Then `R_F` is disjoint from every truth table of circuit complexity at most `t`. Circuit counting gives

`|{T:CC_n(T)<=u}|/2^N <= 2^(O(u log(n+u))-N) = 2^(-N+O(N^beta*n))`.

Consequently `R_F` has density at least `1-2^(-N+O(N^beta*n))`. Its membership circuit has exactly the size of `F` (one output negation if the convention requires it). Equivalently, the partial algorithm that says `NO` on `R_F` and abstains elsewhere is zero-error for threshold MCSP at `t` and succeeds on almost every uniform table.

This is an exact direct equivalence between the relevant one-sided partial solvers and dense properties disjoint from the Low circuit codebook: a sound `NO/?` solver defines such a property by its `NO` set; any such property defines the solver by answering `NO` on that set and `?` elsewhere. A full OPS separator gives one such property, but a general dense property need not reject every OPS-High table. Therefore proving a lower bound for all these properties would suffice, while finding one does not furnish a full-promise separator.

Hirahara--Santhanam formalize closely related equivalences for their stated threshold family `s(k)=2^k/k^{omega(1)}` and all constant rescalings, with polynomially small or near-one average success. That theorem should not be described as an exact parameter identity for OPS `t=2^(beta*n)/(10n)`: at rescaling `beta*n`, their displayed threshold is smaller by a superpolynomial factor. The direct property/partial-solver equivalence above needs no imported theorem. Source: [Hirahara--Santhanam, Proposition 12](https://drops.dagstuhl.de/storage/00lipics/lipics-vol079-ccc2017/LIPIcs.CCC.2017.7/LIPIcs.CCC.2017.7.pdf).

## A proved charge in the decision-tree model

Suppose a deterministic adaptive decision tree reads truth-table coordinates and outputs `1` exactly on a property `R` disjoint from all tables of size at most `t`. Every accepting path must query more than `(t-n)/(n+1)` distinct coordinates. Indeed, for any path fixing `q` distinct coordinates to prescribed bits, interpolate those values by

`g(x)=OR_{i:b_i=1} AND_{j=1}^n literal_{i,j}(x)`,

where the `i`th minterm selects the address of the `i`th prescribed `1` bit. Share the `n` negated input literals across terms. This uses at most `qn+n+O(1)` fan-in-two AND/OR/NOT gates and matches every queried bit. If `q<= (t-n-O(1))/(n+1)`, then `CC_n(g)<=t`. The low table `tt(g)` follows the same path and would be accepted, contradicting usefulness. Since `R_F` is nonempty (indeed dense), its decision-tree depth is therefore `Omega(t/n)=Omega(N^beta/n^2)`.

This lemma is query-specific. It does not charge ordinary shared-DAG gates: `OR_N` has decision-tree depth `N` and only `N-1` gates. That example is not a useful property because it accepts Low tables; it refutes only the generic inference from certificate/query width to superlinear gate count. The four project canaries—parity, repeated-block equality, sparse parity checks, and simple global block relations—make the same sharing warning concrete: their checks can be implemented in `O(N)` gates, but they do not satisfy the global Low-exclusion property and are not full OPS separators.

## What this cycle rules in and rules out

- **Established:** the separator-to-one-sided-average-solver implication, dense-property interpretation, circuit-counting density, and the decision-tree path lower bound above.
- **Not established:** a total-gate lower bound for arbitrary circuits computing a dense property disjoint from all size-`t` truth tables; a near-linear full-promise separator; or any improvement to OPS magnification.
- **Mechanism verdict:** retain the natural-property language as a precise restatement of the target. Retire it as an independent reduction that by itself simplifies the gate-charging problem. Retain certificate width only for query/read-once models; it does not survive unrestricted sharing as a superlinear total-gate charge.
- **Counterconstruction check:** decision-tree depth and density alone are compatible with `O(N)` circuits (`OR_N`), though that function fails the useful-property side condition. The Low-exclusion condition is exactly the missing structure that a future argument must exploit.
- **Quantitative frontier:** unchanged. Ordinary lower bound remains `N-O(N^beta log N)` with C-406's additive logarithmic reconvergence refinement; exact full-promise upper remains `O(N*2^(O(N^beta)))`; the fixed-epsilon OPS target and native `rho` target remain open.

