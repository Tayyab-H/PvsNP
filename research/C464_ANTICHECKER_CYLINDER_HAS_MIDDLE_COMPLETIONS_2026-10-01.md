# C-464 — Anti-checker cylinders contain middle-band and true NO completions

**Date:** 1 October 2026  
**Status:** complete proof of a certificate/cylinder obstruction; no new lower bound or complete near-linear separator.

## 1. Exact promise and target

Let `N=2^n`, `tau=N^beta`, and use the OPS parameters

```text
s1 = tau/(10n),       s2 = tau.
YES: CC_n(T) <= s1.
NO:  CC_n(T) > tau  (integer size at least floor(tau)+1).
```

The middle band is unrestricted. The published OPS theorem uses the factor `10` in `s1`; one fixed `epsilon>0` must work for every sufficiently small fixed `beta>0` to obtain `NP not subseteq P/poly`. [OPS, Theorem 1.4 and Definition 2.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)

The mechanism tested here is the proposed anti-checker search-to-decision bridge: a High table has a small set of addresses that defeats every Low circuit, and perhaps a separator could be queried on a completion of the resulting partial table. The proof below shows exactly what this certificate guarantees—and why a completion query is not promise-safe.

## 2. Theorem: a mid-band table has a short anti-checker shared with a High completion

For every fixed `0<beta<1` and all sufficiently large `n`, there are tables `g,f in {0,1}^N` and an address set `A subseteq {0,1}^n` such that

1. `s1 < CC_n(g) <= floor(tau)` and `CC_n(g) >= (1/2-o(1))*tau`;
2. `CC_n(f)>tau`;
3. `f|A = g|A`, and every circuit `C` of size at most `s1` disagrees with `g` (and hence `f`) on at least one address in `A`;
4. `|A|=O(tau)`.

Thus the partial table `g|A` is Low-free, yet its cylinder contains both a middle-band table and a formally promised NO table.

### Proof

Let `L(k)` be the maximum fan-in-two AND/OR/NOT circuit complexity of a Boolean function on `k` variables. The Shannon–Lupanov theorem gives

```text
L(k)=(1+o(1))*2^k/k,
L(k+1)/L(k)=2+o(1).
```

Choose the largest `k` for which `L(k)<=q`, where `q=floor(tau)`. Then `L(k+1)>q` and the ratio estimate gives `L(k) >= (1/2-o(1))*tau`. Also `k=beta*n+O(log n)<n` for fixed `beta<1`. Let `g` be a `k`-variable function of complexity `L(k)`, padded to `n` variables by ignoring `n-k` variables. Its `n`-variable complexity remains exactly `L(k)`: the upper bound ignores those inputs, and fixing them in any alleged smaller circuit would give a smaller `k`-variable circuit. Since `s1=tau/(10n)`, this `g` is strictly in the middle band for large `n`.

Now consider the finite zero-sum game whose rows are addresses `a in {0,1}^n`, whose columns are circuits `C` of size at most `s1`, and whose payoff is `1[C(a)!=g(a)]`. If every address distribution had some Low circuit with expected error below `1/4`, minimax would give a distribution over Low circuits for which each address has error below `1/4`. Sample an odd number

```text
r = (ln N + O(1))/D(1/2 || 1/4) = (4.82+o(1))*n
```

of circuits independently and take their majority. Chernoff's bound and a union bound over all `N` addresses show that some sample's majority computes `g` exactly. The resulting ordinary circuit has at most

```text
r*s1 + O(r^2) = (0.482+o(1))*tau
```

gates, contradicting `CC(g)>=(0.5-o(1))*tau`. Here `D(1/2 || 1/4)=0.14384...`; OR and AND gates in the majority are included in the total-gate bound. Therefore some address distribution makes every size-`s1` circuit err with probability at least `1/4`.

Sample `t=O(log K)=O(tau)` addresses independently from this distribution, where `K` is the number of Low circuit descriptions. Chernoff's lower-tail bound plus a union bound over those `K` circuits gives a sample on which every Low circuit disagrees with `g` at least once. Let `A` be its support, so `|A|<=t=O(tau)`.

Finally, there are `2^(N-|A|)` completions agreeing with `g|A`. The number of circuits of size at most `floor(tau)` is at most `2^(O(tau log(tau+n)))=2^(O(tau*n))=2^o(N)` for fixed `beta<1`; also `|A|=o(N)`. Hence some completion `f` is not computed by any circuit of size at most `floor(tau)`, so `CC(f)>tau` exactly. It agrees with `g` on `A`, as required. ∎

The proof is existential. It does not provide an efficient algorithm for finding `g`, the minimax distribution, `A`, or `f`.

## 3. What this falsifies, and what it does not

On the cylinder fixing `A` to `g|A`, a separator's value at an arbitrary completion is not determined by the certificate. For example, both total extensions below satisfy the exact promise:

```text
F_low(T)  = 1 iff CC(T)<=s1,
F_upper(T)= 1 iff CC(T)<=floor(tau).
```

They both reject the High completion `f`, but they disagree on the middle table `g`. Therefore “query a completion and read the separator bit” is not a generic promise-preserving search-to-decision rule. An alternative reduction may still work if it proves its queries land on forced YES/NO inputs or proves a separator-independent extraction. This is a counterexample to the generic certificate bridge, not to every non-black-box route and not to the Gap-MCSP lower-bound program.

The construction is also a direct attack on the tempting claim that a large anti-checker or many local inconsistencies themselves charge the separator. The certificate controls how every Low circuit behaves on `A`; it says nothing about the gate count of every total extension of the promise.

## 4. Canary constructions: shared checks do not become gate charges

These examples are calibration tests, not full-promise separators.

| Structure on the `N` table bits | Shared ordinary check | Why it defeats a generic local-count claim | Scope |
|---|---|---|---|
| Global parity | XOR all `N` bits in `O(N)` gates | One global statistic has `N` incidences but linear total cost. Both parities contain Low tables and, by counting, High tables. | Not a Gap-MCSP separator. |
| Repeated-block equality | Compare each bit in one half with its copy in the other half; `O(N)` gates | `N/2` equalities share the block wiring; the relation class has `2^(N/2)` members and therefore contains High tables by circuit counting, as well as Low tables. | Not a sound Low-only filter. |
| Sparse parity checks | Partition bits into triples and test even parity in each triple; `O(N)` gates | There are `2^(2N/3)` codewords and only `2^(o(N))` circuits of size at most `tau`, so this sparse linear code contains High tables as well as the zero Low table. | Not a separator; it refutes incidence-to-cost inference. |
| Simple global block relation | Set each of a constant number of blocks to a copy of a base block, optionally XORed with a fixed mask; verify all coordinates in `O(N)` gates | The base block is reused, while the number of degrees of freedom remains `Omega(N)`; circuit counting again places High tables inside this structured family. | Not a full-promise separator. |

The constructions show why reuse matters: many coordinate constraints can be checked by a linear shared DAG. They do not construct a cheap separator for *all* promised tables and do not contradict any full-promise lower bound.

## 5. Paired full-promise construction attempt and resource accounting

The canonical certificate predicate explicitly enumerates all candidate address sets `A` and all Low circuit descriptions. Its literal, unrolled gate expansion has size on the scale

```text
2^(O(tau log(N/tau))) = 2^(O(N^beta*n))
```

before any attempt to compress it, which is worse than the existing complete Low-codebook enumerator `O(N*2^(O(N^beta)))`. The existing robust union of Low-centered Hamming balls is also a valid complete separator, but its direct candidate-by-candidate implementation has the same enumerative scale as the codebook upper. No near-linear full-promise separator is obtained.

Resource distinctions for this cycle:

* **Total gates:** the majority reconstruction uses `r*s1+O(r^2)` gates; the repeated circuits are separate copies, so no additivity assumption is needed. The structured canary checkers count every AND/OR/NOT/XOR implementation gate.
* **Paid AND states / fusion / cycles:** not used. No native-model conclusion follows.
* **OR operations:** counted as ordinary gates throughout; an OR is never free.
* **Wires:** every listed ordinary circuit has fan-in at most two, so its internal wire count is at most twice its gate count, up to input/output conventions. The canary checkers use `O(N)` gates and wires; no wire-only lower bound is claimed.
* **Description bits:** an address set of size `O(tau)` has an explicit list encoding of `O(tau*n)` bits. This is certificate length, not a circuit lower bound.
* **Runtime / construction:** minimax and completion counting prove existence only. They do not give a poly-time (or low-circuit) method to construct the witness certificate.

## 6. Literature, novelty, and barrier scope

The anti-checker idea and the exact `tau/(10n)` versus `tau` thresholds are due to Oliveira–Pich–Santhanam; their Theorem 1.4 establishes the hardness-magnification implication. This report combines that certificate perspective with Shannon–Lupanov maximum circuit complexity and a completion count to prove the specific middle-cylinder obstruction above. The combination is project-derived; it is not an unconditional lower bound or a claim that anti-checkers themselves are new. [OPS, Theorem 1.4 and Section 4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)

The Shannon lower bound and Lupanov upper bound give `L(k)=(1+o(1))2^k/k`; the asymptotic factor-two step is what places a hard function in the middle band with complexity at least about `tau/2`. See Shannon's original [1949 paper](https://doi.org/10.1002/j.1538-7305.1949.tb03624.x) and Lupanov's [1958 method of circuit synthesis](https://radiophysics.unn.ru/issues/1958/1/120). The hardness-magnification locality barrier is a limitation on certain locality-robust lower-bound methods, not an impossibility theorem for arbitrary-depth shared circuits or for all promise-preserving reductions. [Chen et al., *Beyond Natural Proofs: Hardness Magnification and Locality*](https://eccc.weizmann.ac.il/report/2019/168/download)

## 7. Claim, assumptions, and frontier effect

**Strongest proved statement this cycle:** for every fixed `beta<1`, a size-near-`tau/2` middle-band function has an `O(tau)` anti-checker against all size-`s1` circuits, and some true High completion agrees with it on that anti-checker. This is a proved obstruction to generic completion-query extraction.

**Assumptions:** classical Shannon–Lupanov maximum-complexity asymptotics; finite minimax; Chernoff bounds; standard circuit-description counting; ordinary fan-in-two AND/OR/NOT gate size. The theorem is nonuniform and existential.

**Exact frontier change:** none. The ordinary lower frontier remains `N-O(N^beta log N)` essential inputs with C-406's additive logarithmic reconvergence refinement. The full-promise upper remains `O(N*2^(O(N^beta)))`. The OPS common-fixed-`epsilon` lower bound is open; native `rho>=N-o(N)` is separate. No P-vs-NP result follows.

**Next mechanism:** retire arbitrary-completion querying from the anti-checker route. Continue only with (i) a query gadget whose every completion is forced to a promise side, or (ii) a direct gate inequality that applies to every total extension, regardless of certificate output. Do not sharpen anti-checker length or incidence as a proxy for separator gates.
