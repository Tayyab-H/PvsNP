# C-463 â€” First-principles audit through C-462 and a structured self-embedding test

**Date:** 1 October 2026  
**Status:** cumulative diagnosis plus one exact restriction lemma and one complete-separator construction check. No superlinear circuit lower bound, near-linear separator, or P-vs-NP proof.

## 1. The object, with the formal endpoints

Let `N=2^n`, and let `L_t^(n)` denote truth tables of `n`-input Boolean functions with fan-in-two AND/OR/NOT circuit complexity at most `t`. OPS Theorem 1.4 uses

```text
s1 = 2^(beta*n)/(c*n) = N^beta/(c log_2 N),
s2 = 2^(beta*n)       = N^beta,
```

for a universal constant `c`; the displayed proof takes `c=10`. The formal definition of Gap-MCSP has **YES** `CC(T)<=s1` and **NO** `CC(T)>s2`; values in between are unrestricted. Thus a total separator `F` satisfies

```text
L_s1^(n) subseteq F^(-1)(1) subseteq L_s2^(n).
```

The project quantity is the minimum total ordinary gate count over *all* such extensions, including arbitrary middle-band labels. The magnification implication asks for one fixed `epsilon>0` such that for every sufficiently small fixed `beta>0`, this minimum exceeds `N^(1+epsilon)`; OPS then conclude `NP` is not contained in `P/poly`. The implication is sufficient, not an equivalence with `P != NP`. [OPS, Theorem 1.4 and Definition 2.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf)

## 2. What the record proves, and which failures are actually different

C-460 already consolidated the record through C-459. C-461 and C-462 add a failed ordinary-circuit lookup shortcut and an easy common random coordinate slice. The evidence falls into four distinct proof obligations:

| Route | Established fact | Exact missing step |
|---|---|---|
| Direct ordinary-circuit lower bound | Every separator depends on `N-O(N^beta log N)` inputs; C-406 adds only logarithmic reconvergence surplus. Patch robustness, support/degree/rank/certificate statistics, and one-sided sound filters have been tested against explicit counterexamples. | A property of the *full sandwich* whose value is forced large for every valid extension and whose growth is charged to every AND/OR/NOT DAG despite unrestricted reuse. This is the shared-gate gap. |
| Promise-preserving restriction or source map | Composition is sharing-safe: if a map of `T` gates sends a source promise into the exact target promise, an `S`-gate separator induces a source separator of at most `S+T`. | A source label with an unrestricted-circuit lower bound above the map cost, while every promised source point maps to the correct YES/NO side. Prior maps fail an endpoint, leak the source answer, or spend the required margin. |
| Complete full-promise construction | Enumerating the `M=2^(O(s1 log(n+s1)))=2^(O(N^beta))` low descriptions gives `O(NM)` gates. | No compression of this structured codebook membership test has a proved ordinary-gate cost near `N`. C-461's sorted lookup counted RAM comparisons while omitting circuit data access. |
| Alternate computational models | Formula, monotone, comparator, native fusion, and closure bounds are meaningful in their own models. | No compiler transfers the needed statement to arbitrary ordinary shared DAGs. In particular, native `rho` and ordinary total gates remain separate. |

These are not all instances of one failure. The direct route has a missing gate-charge theorem. The transfer route has endpoint and composition-budget problems. The construction route lacks a compressed membership circuit. Model transfer is a fourth issue. By contrast, support, algebraic degree, incidence, communication rank, Hamming radius, certificate width, and similar scalar proposals often repeat the *same* direct-route failure: they prove a semantic or geometric fact without a gate inequality for arbitrary sharing. Locality and natural-proofs barriers constrain particular proof methods; neither is an impossibility theorem for all ordinary-circuit proofs.

## 3. Structured coordinate subcubes: exact self-embedding, no exponent gain

A useful test of the random-slice conclusion is a deliberately structured subcube that preserves a smaller MCSP instance instead of making all Low completions sparse.

Choose `k<n`. Let `M=2^k`, and let `B` be the truth-table addresses whose first `n-k` address bits are zero. For a `k`-variable table `y` encoding `g`, define the `n`-variable function

```text
f_y(a,z) = 1 iff (a=0^(n-k) and g(z)=1).
```

Its truth table is `y` on `B` and zero outside `B`. Put `h=n-k+1`; a prefix-zero test and one final AND give

```text
CC_n(f_y) <= CC_k(g)+h,
CC_k(g)   <= CC_n(f_y).
```

The second inequality follows by fixing the prefix inputs to zero in any circuit for `f_y`.

Therefore any valid `N`-bit separator, restricted by fixing the `N-M` outside coordinates to zero, solves the smaller promise

```text
YES: CC_k(g) <= s1-h,
NO:  CC_k(g) > s2,
```

with no increase in gate count. The extension is well-defined on the source promise; middle source tables remain unrestricted. This is an exact promise-to-promise self-embedding and requires no assumption about how the large separator works.

It does not improve the exponent. If `delta=k/n` and `beta'=beta/delta`, then `M=N^delta`, `s2=M^beta'`, while

```text
s1-h = (1-o(1))*N^beta/(c*n)
     = (delta-o(1))*M^beta'/(c*k).
```

So the inner threshold corresponds to effective denominator constant about `c/delta`, not exactly the `c` in the OPS statement. No theorem transfer across this changed constant is assumed. More fundamentally, the known linear-scale lower bound at input length `M` lifts only to `Omega(M)=Omega(N^delta)`, weaker than the direct `N-o(N)` bound. A hypothetical inner `M^(1+eta)` result would lift to `N^(delta(1+eta))`, which is superlinear in `N` only if `delta(1+eta)>1`; no such unrestricted-circuit inner result is known. This identifies the structured-slice route as self-similar rather than an amplifier. It is consistent with C-289's safe-cylinder calculation and C-404's all-promised-slice test: a hard induced label remains the missing ingredient.

## 4. Paired construction check: the robust union of Low-centered balls

C-458's patching lemma gives a universal `K0` with

```text
CC(T) <= CC(T0)+K0*(n+1)*dist(T,T0).
```

Set `r=floor((s2-s1)/(2*K0*(n+1)))` and define

```text
U = union over T0 in L_s1^(n) of {T : dist(T,T0)<=r}.
```

Every YES table lies in `U`. Every `T in U` has `CC(T)<=s1+(s2-s1)/2<s2`, so `U` contains no promised NO table (`CC>s2`). Hence `1_U` is a valid full-promise separator.

This is a complete, robust alternative to exact low-codebook membership. It does not improve the upper bound: there are `K1=2^(O(s1 log(n+s1)))=2^(O(N^beta))` candidate Low descriptions, and checking Hamming distance to each with an ordinary population counter costs at most `O(N log N)` gates and wires per description. The resulting `O(N log N*K1)` bound is still `N*2^(O(N^beta))` after absorbing logarithmic factors, the same exponential scale as exact enumeration. The circuit hardwires each candidate truth table. With `G=O(N log N*K1)` gates and wires, an indexed gate-list description costs `O(G log(N*K1))` bits. A direct offline construction enumerates and evaluates descriptions in `O(K1*N*s1)` time. OR operations are included in the ordinary total-gate count; no native paid-state bound follows. No lower bound of `Omega(NM)` is claimed; shared circuit compression remains possible and unproved.

## 5. A more precise certificate lens: anti-checkers are not automatically searchable

The OPS anti-checker lemma gives a concrete semantic characterization at these parameters. For every `T` with `CC(T)>s2`, there is a set `A` of `O(s2)` addresses such that every circuit of size at most `s1` disagrees with `T` somewhere on `A`. A YES table has no such set, since its own size-`s1` circuit agrees everywhere. Thus, on the promise,

```text
T is NO iff there exists A, |A|=O(s2), such that
           for every size-s1 circuit C, some a in A has C(a) != T(a).
```

Equivalently, `T|A` defines a cylinder containing no Low table. This frames the selector as recognizing the existence of a short low-free certificate. The O(s2)-size existence statement is distinct from the constructive Anti-Checker Lemma proved by OPS under `NP subseteq Circuit[poly]`: their constructed list has `t=2^(10*beta*n)=s2^10` addresses, not O(s2), and is generated with near-linear circuit size only under that class assumption. Neither existence result implies that an arbitrary decision circuit outputs a certificate. Brute-force enumeration over candidate address sets already has `Q=2^(O(s2 log(N/s2)))=2^(O(N^beta log N))` possibilities. More explicitly, for each set `A` define `P_A(T)=AND_(C in D_s1) OR_(a in A) [T[a] != C(a)]`, and let `HighCert(T)=OR_A P_A(T)`. The complement is a valid separator on the promise: no Low table has a certificate, and every High table has one. Its direct circuit costs `O(Q*K1*s2)=2^(O(N^beta log N))` gates and wires, since each mismatch value `C(a)` is a hardwired constant. This is larger than the existing `N*2^(O(N^beta))` enumerator at the exponent scale; an indexed gate-list description is `O(G log(N+G))` bits for `G` gates, and offline generation/evaluation is a separate cost. Thus the certificate view is not a better upper construction. The missing bridge would be a search-to-decision reduction whose queries remain inside the Gap-MCSP promise, or a reduction showing that every valid extension computes a hard restriction forced to agree with this certificate predicate. Merely lower-bounding its canonical total extension is insufficient because middle-band labels are free. Queries on arbitrary partially specified tables are not licensed: the separator's behavior there is unconstrained.

This is a useful model for new ideas because it names the precise hidden operation: selecting a low-free coordinate certificate, while preventing the unsupported inference that every correct decider has to reveal one.

## 6. Exact status and next research filter

**Strongest proved statement this cycle:** the prefix-subcube composition lemma above, plus the full-promise robust-ball extension. Both have complete proofs and no asymptotic frontier gain.

**Frontier unchanged:** ordinary lower bound `N-O(N^beta log N)` with C-406's additive logarithmic reconvergence refinement; full-promise upper `O(N*2^(O(N^beta)))`; OPS common-fixed-`epsilon` target open; native `rho>=N-o(N)` separate; no P-vs-NP proof.

Future direct candidates must begin with the exact interpolation problem over *all* total extensions and supply both sides of a gate-potential inequality. Future restriction candidates must prove a hard induced promise under the exact thresholds and account for the effective constant `c`; a smaller copy of the same problem is not amplification. Future certificate ideas must prove a promise-preserving search-to-decision bridge, or a lower bound that applies to every total extension rather than only the canonical certificate predicate. A complete upper-bound idea must account for every low table and all data access in ordinary gates.

**Literature check:** the primary OPS theorem and anti-checker proof were checked directly. The locality barrier is method-specific and supplies no general impossibility result ([Chen et al.](https://eccc.weizmann.ac.il/report/2019/168/download)). Two 2026 adjacent results do not transfer directly: Goldberg, Juvekar, and Kabanets prove conditional non-Levin hardness for implicit MCSP under cryptographic and proof-complexity assumptions, but their input is a sampling circuit rather than an explicit full truth table ([ECCC TR26-091](https://eccc.weizmann.ac.il/report/2026/091/)); Ben Daniel rules out certain randomized polynomial-size witness-pruning procedures under iO/OWF assumptions, but an anti-checker verifies disagreement against every size-`s1` circuit and is not the same NP witness-isolation relation ([ECCC TR26-201](https://eccc.weizmann.ac.il/report/2026/201/)). These sharpen the scope warning against assuming witness recovery; neither changes the unconditional ordinary or native frontier.

## 7. Boundary convention audit

Write `tau2=N^beta` for the real upper threshold. Since `CC` is integer-valued, the formal OPS NO set is `CC>tau2`, equivalently `CC>=floor(tau2)+1`. This equals `CC>=ceil(tau2)` only when `tau2` is nonintegral. A separator may reject the boundary `CC=tau2` when it is integral because that point is in the free middle band; a source reduction that relies on the target circuit being forced to reject must map to `CC>tau2`, not merely `CC>=tau2`.

The C-463 prefix embedding and robust-ball construction use the strict formal target. C-462's auxiliary distance implication is proved for the stronger condition `CC>=tau2`, so it remains valid for every formal NO input and even handles the boundary. C-457's sound filter also rejects a superset of the formal NO set. C-417 previously wrote `ceil(tau2)` as the first NO size; it now uses `floor(tau2)+1`. C-408 uses boundary-inclusive complexity only as a stronger auxiliary rejection property. C-418's circuit count now excludes every nonconstant trace below `floor(tau2)+1`, so its source map sends all nonzero inputs to the strict formal NO side. These corrections change no quantitative frontier.
