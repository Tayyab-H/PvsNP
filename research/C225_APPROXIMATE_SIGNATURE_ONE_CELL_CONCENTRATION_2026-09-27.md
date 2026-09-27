# C-225 — Approximate signature variation can concentrate in one cell

Date: 27 September 2026  
Scope: continue the C-75 adaptive-signature/shared-DAG route. Stress-test C-224's aggregate minority-mass bound and C-120's exact-signature concentration result. No arbitrary-DAG lower bound or P-vs-NP proof is claimed.

## Theorem: one-cell concentration persists under approximation

Let `N=2^n`, let `w` be a table with `CC(w)<=s1`, and let `C` be a circuit of size `r` satisfying `C(x)=w(x)` on a set `G` of at least `N/2` addresses. Choose a `k`-bit address signature `sigma(x)` from wires of `C`, including C's output. For a signature value `p`, put
\[
F=G\cap\{x:\sigma(x)=p\}.
\]
There is a signature value with `t=|F|>=N/2^{k+1}`. Choose up to k wire values, allowing input wires or repeated wires if necessary, and include C's output; padding can only decrease the number of cells.

Assume `t > A s2 log(s2+n)` for a sufficiently large basis-dependent constant `A`, and
\[
s1+r+O(k)\le s2/2.
\]
Then there is a table `z` of circuit complexity at least `s2` such that:

1. `z=w` outside this one set `F`;
2. `w` is constant on `F`, while `z` is nonconstant on `F`;
3. at least `Omega(s2/n)` points of `F` have the minority value of `z` on `F`.

### Proof

The output wire is included in `sigma`. On `F`, all signature bits agree and `C=w`, so `w` is constant on `F`.

For each subset `A subseteq F`, define `z_A=w xor 1_A`. These are `2^t` distinct truth tables. At most `2^{O(s2 log(s2+n))}` Boolean tables have circuits of size at most `s2`. The assumed lower bound on `t` therefore gives at least one `A` for which `z_A` lies outside `SIZE(s2)` and is high.

The two endpoint completions are both low. The empty endpoint is `z_empty=w`. For the full endpoint, the indicator of `F` has a circuit of size `s1+r+O(k)`: compute `w`, compute `C` and its selected wires, test `C(x)=w(x)`, and test `sigma(x)=p`. Thus `z_F=w xor 1_F` has size at most `s1+r+O(k)<=s2/2`. Since both endpoints are low, a high `z_A` has `A` neither empty nor all of `F`; hence it varies on `F`.

Finally, point-minterm patching gives `CC(v xor 1_S)<=CC(v)+O(n|S|)`. Applying this to the high table `z_A` and each low endpoint `z_empty,z_F` yields
\[
|A|=dist(z_A,z_empty)=\Omega(s2/n),\qquad
|F\setminus A|=dist(z_A,z_F)=\Omega(s2/n),
\]
because both endpoint circuits have size at most `s2/2`. Since `w` is constant on `F`, the minority count of `z_A` on `F` is `min(|A|,|F\\setminus A|)`, proving the claim.

### OPS parameter range

For fixed `0<beta<1`, take `s2=N^beta`, `s1=N^beta/(c n)`, and any fixed
\[
0<\kappa<\min\{\beta,1-\beta\},\qquad k=\lfloor\kappa n\rfloor.
\]
Then `N/2^{k+1}=Omega(N^{1-kappa})`, whose exponent is strictly greater than `beta`; consequently `t >> s2 log(s2+n)`. Also `k=O(n)` and `s1=o(s2)`. Thus the theorem applies whenever the approximate circuit has `r<=s2/4` and its good set has size at least `N/2`, for all sufficiently large `n`.

This strengthens C-120 in two ways: it permits an approximating circuit with up to half of all addresses wrong, and it works throughout fixed `0<beta<1` by choosing `k` below both exponent thresholds. The construction of the full-cell endpoint uses the exact good set `G`, so it composes the circuits for `w` and `C`; it does not incorrectly treat `G` as directly computable from `C` alone.

## Consequence for C-224 and the DAG route

C-224's total minority mass cannot be spread-counted across signature cells: an adversarial high table can put all of its required `Omega(s2/n)` minority mass in one good cell. Therefore any lower-bound argument that needs many mixed cells, or sums a per-cell charge over this signature partition, fails even for approximate signatures. The surviving task is to identify a pair-dependent varying cell without an explicit low-circuit selector and then charge its routing across product-hull-safe merged states. A protocol given the circuit `C` can enumerate its cells and scan addresses in `O(N)` work; that does not give a shared DAG for all low tables because the partition is C-dependent.

This does **not** show that all high tables vary in one cell. The counting construction finds a high completion tailored to the chosen `w,C`; for an arbitrary high `z`, C-224 still gives only its error/minority alternative.

## 2026 literature check: nearby extension and implicit-MCSP results

Two current results were checked for a possible bridge:

* Goldberg, Juvekar, and Kabanets, *Non-Levin NP-Hardness of Implicit MCSP and PAC Learning under Few Assumptions* (ECCC TR26-091, June 2026), proves conditional hardness for sampler-encoded, full-support, average-case learning/implicit-MCSP promises under subexponentially secure indistinguishability obfuscation and a proof-complexity assumption. Its instance is a sampler rather than an explicit full truth table, and its reductions are randomized half-Levin reductions. No size-preserving map to the C-75 explicit low/high promise or its deterministic rect-DAG is supplied.
* Carmosino, Dang, and Jackman, *Simple Circuit Extensions for XOR in PTIME* (STACS 2026), gives a polynomial-time algorithm for the XOR simple-extension problem under its stated circuit measure; the paper presents MUX as a candidate for ETH-hardness of total MCSP extension, not as a proved hardness result. This concerns completion of partial specifications for a fixed function and gives no C-75 shared-DAG lower bound.

These papers provide useful boundaries on circuit search and succinct representations, but neither changes the C-75 transfer chain. Primary sources: [ECCC TR26-091](https://eccc.weizmann.ac.il/report/2026/091/download/) and [STACS 2026 paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.23).

## Disposition

**Proved:** approximate signature-cell concentration with explicit parameter range and endpoint-size accounting.

**Falsified:** deriving a superlinear shared-DAG cost by requiring many signature cells to be mixed or by summing minority mass across cells.

**Still open:** a selector-free way to route to one varying cell for every promised pair, with a global product-hull-safe charge across arbitrary acyclic rect-DAGs. Keep O-141 active and preserve the existing `q -> S_rect=O(q^3/log q)` loss. C-225 yields no `S_rect` or `rho_prom` lower bound.
