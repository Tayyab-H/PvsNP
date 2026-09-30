# C-422 - Fractional anti-checkers are short, but do not charge separator gates

**Status:** proved structural statement; the core anti-checker theorem is established prior work (Lipton--Young, used by OPS). This cycle makes the exact fan-in-two gate accounting and the failed separator transfer explicit. No ordinary, native-fusion, or P-vs-NP frontier changes.

## Exact target and model

Write `N=2^n`, `s1=N^beta/(10n)`, and `s2=N^beta`, for fixed `0<beta<1` and sufficiently large `n`. The OPS theorem uses a universal constant `c` in place of 10; its proof instantiates 10. It states that there is one fixed `epsilon>0` such that, if for every sufficiently small fixed `beta>0` the promise problem `Gap-MCSP[s1,s2]` has no fan-in-two Boolean circuit of `N^(1+epsilon)` total gates, then `NP` is not contained in `P/poly`. The promise accepts every table of circuit size at most `s1`, rejects every table of circuit size at least `s2`, and leaves the middle band unrestricted. Gates, wires, circuit-description bits, and construction time are distinct measures.

The result below concerns functions on the `n`-bit address domain, with their truth tables viewed as `N`-bit strings. It is not a lower bound on the separator circuit whose input is that `N`-bit string.

## Mechanism: fractional disagreement forces a short anti-checker

Let `L1` be the set of distinct truth tables of fan-in-two AND/OR/NOT circuits of size at most `s1`. For a table `f` with `CC(f)>=s2`, define the finite zero-sum game

`lambda(f) = max_mu min_{g in L1} Pr_{a~mu}[f(a) != g(a)]`,

where `mu` ranges over distributions on the `N` addresses. For all sufficiently large `n`,

`lambda(f) >= 1/4`.

This is a genuine composition-cost statement: it accounts for how many low circuits can be combined before their majority computes `f`, with no assumption about disjointness or lack of sharing.

### Proof

Suppose `lambda(f)<1/4`. Finite minimax gives a distribution `nu` over `L1` such that, at every address `a`, a random `g~nu` disagrees with `f(a)` with probability less than `1/4`.

Take an odd `k >= 8 ln(2N)`. Independently sample `g1,...,gk` from `nu`. At each address, Hoeffding's inequality bounds the probability that their majority is wrong by `exp(-k/8)`. A union bound over all `N` addresses is at most `N exp(-k/8) <= 1/2`. Thus some sampled majority computes `f` exactly on all addresses.

The majority has an ordinary fan-in-two implementation: use `k` copies of the low circuits, then sort their `k` Boolean outputs using a sorting network of `O(k log^2 k)` AND/OR gates and take the middle bit. Its total size is

`k*s1 + O(k log^2 k) = (8 ln(2)/10 + o(1))*s2 < s2`.

Here `k=8 ln(2N)+O(1)=8n ln 2+O(1)`, and `O(n log^2 n)=o(N^beta)` for fixed `beta>0`. This contradicts `CC(f)>=s2`, proving `lambda(f)>=1/4`.

Choose a maximizing `mu`, and sample `q` addresses independently from it. Each `g in L1` has mismatch probability at least `1/4`; Hoeffding gives probability at most `exp(-q/32)` that it disagrees on fewer than a `1/8` fraction of the sample. Circuit counting gives

`|L1| <= 2^(O(s1 log(s1+n))) = 2^(O(N^beta))`.

Taking `q >= 32(ln |L1|+1)` and union-bounding over `L1` proves that there is a multiset of `q=O(N^beta)` addresses on which every size-`s1` circuit disagrees with `f` on at least a `1/8` fraction. In particular, it is an anti-checker in the weaker sense that every low circuit disagrees at some listed address. The list stores `O(N^beta log N)` address bits; this is a semantic existence result, not a circuit that computes the list from `f`.

## Initial mechanism and adversarial repair

An initial integer-packing observation is also valid. If three low circuits `g1,g2,g3` have pairwise disjoint disagreement supports `D_i={a:f(a)!=g_i(a)}`, then `e12=g1 XOR g2` and `e13=g1 XOR g3` have supports `D1 union D2` and `D1 union D3`. Consequently `e12 AND NOT e13` is the indicator of `D2`, and `f=g2 XOR (e12 AND NOT e13)`. Implementing each XOR with three fan-in-two gates gives `CC(f)<=3s1+11<s2` for large `n`, a contradiction. So the disagreement hypergraph has matching number at most two.

That integer packing condition alone is too weak. The lines of a finite projective plane have matching number one but require `Theta(sqrt(N))` points to hit them. This would miss the OPS sample scale `N^(10 beta)` for sufficiently small `beta`. We therefore changed the mechanism from ordinary packing to the fractional game value `lambda(f)`. The majority argument proves a constant fractional hitting value for the actual low-circuit disagreement family and rules out projective-plane behavior at that level. This repairs the combinatorial mechanism, but it does not by itself give a separator-gate lower bound.

## Exact failed transfer to a separator

For an arbitrary `S`-gate separator `C`, C-421 extracts from the evaluated DAG on a High input `f` a set `Q_C(f)` of at most `min(N,2S)` coordinates whose agreement forces `C=0`. C-422 proves independently that a much shorter set `Q(f)` of `O(N^beta)` coordinates anti-checks all Low tables. There is no proved transformation from the first object to the second using `O(S+N^(1+O(beta)))` total gates.

The quantifiers explain the gap. A Low anti-checker only rules out Low completions agreeing with `f` on `Q`. A zero-certificate for `C` must force `C=0` on **every** completion, including middle-band tables that `C` is allowed to accept. For a fixed mask `Q`, checking that it is a zero-certificate is coNP; selecting a short valid mask is a `Sigma_2^P` search. The minimax proof supplies a distribution by existence, but its best response is the search for a size-`s1` circuit maximizing weighted agreement with `f`. Enumerating the candidates costs `2^(O(N^beta))`, and the selector circuit is not obtained from `C`.

This is also why the sample-length improvement does not improve the actual OPS gate lower bound: the sample has the right short length, but no separator-sensitive algorithm or gate inequality computes it. OPS already gives a conditional near-linear selector under `NP subseteq P/poly`; its constructive Lemma 4.1 uses a list of `N^(10 beta)` addresses and a selector circuit of size `N^(1+k beta)`. The existence theorem below that construction is classical, not a new lower bound.

## Shared-computation countertests

These constructions refute generic incidence-to-gate charges; none is a full-promise Gap-MCSP separator.

| Pattern | Cheapest relevant shared computation | What it defeats |
|---|---|---|
| Parity | On an `N`-bit separator input, a prefix-XOR DAG computes all prefixes with `N-1` XOR gates (`O(N)` AND/OR/NOT gates), despite quadratic expanded prefix incidence. As an address function on `n` bits, parity has `O(n)` gates and is Low. | Charging every coordinate occurrence or every prefix incidence separately. It also has width-`N` ordinary zero-certificates, so small gate count alone does not shorten C-421 certificates. |
| Repeated-block equality | Compare each block with one representative and reduce the mismatch bits: `O(N)` gates with free fanout of representatives. | Charging each repeated copy as independent work. |
| Sparse parity checks | For `m` checks and `L` total incidences, compute row parities in at most `L-m` XOR gates, then OR the violations in `O(m)` gates; shared prefixes or duplicate subchecks can reduce this further. | Charging each local inconsistency independently of a shared parity DAG. |
| Simple global block relations | Reuse shared seed bits and compute each copy/XOR relation once per output bit, then reduce violations: `O(N+B)` gates for `N` output positions and `B` constant-size relations. | Multiplying the number of relations by block length when their values factor through shared signals. |

The fractional anti-checker theorem survives these tests because it is a statement about a genuinely High truth table versus **all** circuits below `s1`. The small pattern recognizers do not solve that full promise.

## Paired full-promise separator attempt

The short anti-checker suggests testing whether some Low circuit matches `f` on the selected sample. If a selector `f -> Q(f)` were available and anti-checked every High table, this would accept every Low table and reject every High table; the middle band could be arbitrary. But the two needed computations remain uncharged: producing `Q(f)` is the minimax/selector search, and checking for a Low circuit agreeing on `Q` is an NP search over descriptions. An `O(N log^3 N)` shared multiquery lookup can supply `f(a)` values once `Q` is known (C-410), but it does not perform either search.

The explicit unconditional full-promise construction still enumerates every size-`s1` circuit description and compares its hardwired truth table against all `N` input bits. With `M1<=2^(O(s1 log(s1+n)))=2^(O(N^beta))` candidate descriptions, this uses `O(N M1)` total gates and wires. A direct indexed gate-list description takes `O(N M1 log(NM1))` bits, and constructing the list takes `O(M1*N*poly(s1,n))` time. It accepts every Low table and rejects every High table; middle inputs may be rejected. The bound is exponential in `N^beta`, not near-linear.

The sample filter does not automatically compress this circuit. For any fixed sample `Q`, the Low table `0^N` has many Low extensions that vanish on `Q`: every support of size at most `floor(s1/(2n))` outside `Q` has a minterm-DNF of size at most `s1`. Thus a simple sample filter can leave exponentially many candidate descriptions even on a trivial YES input. This is an algorithmic counterexample, not a circuit lower bound; a different shared decision circuit may exist.

## Literature and originality check

- Lipton and Young, *Simple Strategies for Large Zero-Sum Games with Applications to Complexity Theory* (1994), Theorem 6, already proves anti-checker existence from a minimax game and majority boosting. OPS explicitly cites this result as giving `O(s)` listed inputs against size about `CC(f)/n`; see [Lipton--Young](https://www.cs.ucr.edu/~neal/Lipton94Simple.pdf) and [OPS, Theorem 1.4 and Lemma 4.1](https://theoryofcomputing.org/articles/v017a011/). C-422 is a parameter-matched, gate-accounted derivation and transfer audit, not a claim of a new anti-checker theorem.
- OPS Theorem 1.4 has the quantifiers `there exists one epsilon>0` and `for every sufficiently small fixed beta>0`, with low threshold `2^(beta n)/(c n)` for a universal `c` and high threshold `2^(beta n)`. The proof uses denominator `10n`. Circuit size counts ordinary total gates.
- Chen, Oliveira, Pich, Rajgopal, and Santhanam identify a technique-specific locality barrier and refute the stated Anti-Checker Hypothesis for local-oracle formula settings; see [ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/). This does not rule out a direct lower bound for arbitrary total-gate circuits, and C-422 does not bypass it.

## Frontier effect and next mechanism

**Strongest proved change:** every OPS-High table has a constant fractional disagreement distribution against all OPS-Low circuits and hence a semantic anti-checker multiset of `O(N^beta)` addresses. This is shorter than C-421's generic `N`-coordinate certificate, but it is not a certificate that forces an arbitrary separator to reject every completion.

**Quantitative frontier:** unchanged. The ordinary total-gate lower bound remains `S >= N-O(N^beta log N)-1` with C-406's additive logarithmic refinement; the OPS `N^(1+epsilon)` target remains open. The full-promise upper remains `O(N*2^(O(N^beta)))`. Native fusion remains `rho_GapMCSP >= N-o(N)` with no transfer from this ordinary-circuit argument. No paid-AND-state, OR-operation, wire, description-bit, runtime, wide-seed, arbitrary-endpoint, cycle, or semi-filter-extension bound is proved here.

**Changed next question:** stop trying to shorten a separator's zero-certificate as a purely combinatorial object. Determine whether an arbitrary separator DAG can compute a fractional anti-checker strategy (or a short sample) without outputting a circuit description and without checking addresses one by one. Any claimed conversion must include its total-gate cost and handle accepted middle-band completions. If it fails, the next mechanism must be a direct potential on the separator's shared evaluation DAG.

## O-242 attack: synthesize the minimax strategy by an explicit LP

I attempted to turn the existence proof into an input-dependent selector without assuming a witness output from the separator. Enumerate the M distinct Low tables and form the N-by-M payoff matrix, with entry 1 exactly when a candidate Low circuit disagrees with f at an address. Exact finite minimax is a linear program on this matrix; an optimal address strategy exists, and conditional expectation can select an O(log M)-sample that anti-checks every Low circuit.

This is a valid synthesis algorithm, but not a useful gate bound. The candidate count is M=2^(O(N^beta)); materializing the payoff matrix already costs O(NM) total gates, and a generic exact LP circuit is polynomial in NM, hence still 2^(O(N^beta)) gates with an uncontrolled constant in the exponent. The sample verifier also searches the Low descriptions. It does not produce N^(1+epsilon) gates for any fixed epsilon uniformly over small beta. This is an algorithmic upper bound for the selector, not a lower bound and not a near-linear full-promise separator.

The direct LP route is therefore closed as a magnification mechanism. A successor must use separator-sensitive structure or a constructive approximate-counting method that avoids the full Low-circuit matrix; OPS already gives a conditional construction of a larger list under NP subseteq P/poly. Do not report the O(N^beta) semantic sample as a computed output of C.