# C-423 — A separator-boundary pivot can miss a Low table

**Status:** the proposed pivot selector is false as a generic consequence of separator behavior, small Low-family entropy, and High-to-Low Hamming distance. A concrete sparse-table toy gives an exponentially small hit probability. This does **not** refute the statement for actual OPS-High truth tables: the toy's rejecting endpoint is itself Low. It closes this pivot route unless actual circuit hardness supplies a new property beyond those three inputs. No asymptotic Gap-MCSP frontier changes.

## Target and model

The ordinary target remains OPS hardness magnification. With `N=2^n`, the promise is YES for `CC(w)<=N^beta/(c n)`, NO for `CC(w)>=N^beta`, with middle inputs unrestricted. The published theorem asks for one `epsilon>0` such that, for every sufficiently small fixed `beta>0`, this promise problem is not in `Circuit[N^(1+epsilon)]`; it then implies `NP not subseteq P/poly`. The proof uses denominator `10n`. The exact statement and quantifiers are in [OPS, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/).

All gate counts below use total fan-in-two AND/OR/NOT gates. Wires, description bits, and construction time are reported separately. Native fusion `rho` is a different measure.

## Candidate mechanism: first-acceptance pivots

Let `C:{0,1}^N->{0,1}` be a separator, let `f` satisfy `C(f)=0`, and let `L` be its accepted Low set, so `C(g)=1` for every `g in L`. Choose an endpoint distribution `nu` on distinct members of `L`. For each sampled `g`, choose a uniformly random ordering of the disagreement set `D_g={i:f_i!=g_i}` and walk from `f` to `g`, flipping those coordinates in that order. Let `a` be the coordinate whose flip first makes `C` equal 1. This is defined because `C(f)=0` and `C(g)=1`.

The proposed claim was that a natural endpoint distribution, especially uniform over distinct Low tables, would make the pivot law `mu` a constant anti-checker:

`for every h in L,   Pr_{a~mu}[f_a != h_a] >= 1/8.`

If true, a union bound over `|L|=2^(O(N^beta))` would turn `O(N^beta)` independent pivots into a short anti-checker. This would use the separator's own boundary instead of synthesizing the minimax distribution from C-422. The argument would still need a charged implementation: naively constructing all `N` prefix tables for each of `M=|L|` endpoints and evaluating an `S`-gate `C` on them costs `O(M(NS+N^2))` gates, with list storage/construction separate; writing `q` addresses costs `O(q log N)` output bits. No near-linear compiler for the pivot computation was assumed.

## Decisive counterconstruction to the generic claim

Take `N=2^n`, and let `r=t=floor(N^beta/(1000 n^2))`. Choose disjoint coordinate sets `A,B,T` of sizes `r,r,t`, with `R` the remaining coordinates. Define

`L_A={x: x_A=1^r, x_B=0^r, x_R=0, x_T arbitrary}`

and the special table `h=1_B` (all other bits zero). Let `f=0^N`. The circuit

`C(x) = [AND(A) AND NOR(B union R)] OR [AND(B) AND NOR(A union T union R)]`

accepts exactly `L_A union {h}` and rejects `f`. Its total size is `O(N)` gates; the large `R` check is shared between the two branches. Every table in `L_A union {h}` is sparse, with at most `r+t` ones, and has a minterm DNF of size `O((r+t)n)<N^beta/(10n)` for sufficiently large `n`. Thus the endpoints really are Low truth tables at the OPS scale, and `log |L|=t+o(1)=O(N^beta)`.

Choose `g` uniformly among the `2^t+1` distinct members. If `g in L_A`, the path never changes `B` or `R`; the first branch becomes true exactly on the last flip in `A`. By permutation symmetry its pivot is uniform on `A`, which is disjoint from `D_h=B`. If `g=h`, the pivot lies in `B`. Therefore

`Pr[pivot in D_h] = 1/(2^t+1)`,

which tends to zero, contradicting the proposed `1/8` guarantee. The counterexample isolates the failure: most Low endpoints can make the boundary pivot land on one coordinate region, while a valid Low endpoint disagrees with `f` only in another region.

**Scope:** `f=0^N` is Low for MCSP, so this `C` is not a valid Gap-MCSP separator. The construction refutes only a generic lemma based on separator values, Low-family cardinality, sparse Low encodings, and endpoint distance. It does not refute a stronger theorem that uses the actual fact `CC(f)>=s2`; finding a way for that fact to control pivot coverage is now the missing statement. Nor does it disprove C-422's minimax anti-checker, which chooses a maximin address distribution rather than the boundary distribution above.

## Four shared-computation stress tests

These are cost calibrations, not full-promise separators.

| Pattern | Shared implementation on an `N`-bit input | What it invalidates |
|---|---|---|
| Parity | Prefix XOR uses `N-1` XOR operations, or `4N+O(1)` fan-in-two AND/OR/NOT gates, with `O(N)` wires and `O(N log N)` indexed description bits. Take odd `r=Theta(N^beta/n^2)` and endpoints of weight `r`; each has a minterm DNF below `s1`. Parity flips on the first path step, so a uniform pivot lies in a uniform support coordinate; a fixed weight-`r` Low table is hit with probability `r/N=o(1)`. | A constant pivot-coverage claim from endpoint distance or endpoint entropy alone; charging expanded prefix occurrences. The example is still a toy with `f=0` Low. |
| Repeated-block equality | For `k` copies of a `d`-bit block (`N=kd`), compare each of the other `k-1` blocks to one shared representative and OR the `N-d` mismatch bits: `O(N)` gates and wires. | Charging each duplicate block or each repeated comparison as independent work. |
| Sparse parity checks | For `m` checks with `L` total incidences, compute each row parity in `L-m` XOR operations and OR the `m` violations: `O(L+m)` gates, `O(L+m)` wires. Duplicate rows/prefixes can be reused. | Charging each failed check independently of its shared parity DAG. |
| Simple global block relations | If blocks are copies or fixed simple transforms of one seed, compute each seed-derived coordinate once and compare the `N` observed bits against the shared predictions: `O(N+T)` gates, where `T` is the seed-transform cost, with `O(N+T)` wires. | Multiplying each global relation by the block length when its signals can be reused. |

None computes membership in the full Low circuit class or separates every promised High table. They show why an incidence charge is not a total-gate charge.

## Paired near-linear full-promise separator attempt: linear sketch plus Low-image lookup

Try a fixed linear sketch `H:{0,1}^N -> {0,1}^k` over `GF(2)`, and output YES iff `H(w)` lies in the hardwired set `H(L_1)`, where `L_1` is the set of distinct YES tables. This accepts every YES and may accept middle tables. For soundness, no High table may collide with a Low image.

Since `0^N` is Low, if `ker(H)` contains a High table then it collides with `0^N`. Circuit counting gives `|SIZE(<s2)| <= 2^(O(s2 log(s2+n))) = 2^(O(N^beta n))`. If `N-k` exceeds that exponent, `ker(H)` has more vectors than all non-High tables and hence contains a High table. Therefore any such linear sketch must have

`k >= N-O(N^beta n)`.

This rules out a dimension-saving linear fingerprint; it does not rule out nonlinear separators. Taking `H` to be injective leaves the original Low-membership problem in the image. Enumerating all `M=2^(O(N^beta))` Low tables and comparing all `N` coordinates gives the explicit exact upper bound `O(NM)` total gates (and `O(NM)`-scale wires; table/list description and construction time are separate). This is still exponential in `N^beta`, so the paired construction attempt does not yield a near-linear full-promise separator.

## Literature and originality

- OPS Theorem 1.4 has the exact fixed-`epsilon`, sufficiently-small-fixed-`beta` quantifiers stated above; it is the relevant ordinary total-gate target, not a native-fusion bound. See [the primary article](https://theoryofcomputing.org/articles/v017a011/).
- The published locality barrier concerns lower-bound techniques that extend to short-query oracle circuits; it is technique-specific and does not refute a nonlocal total-gate potential or this path idea. See [Chen et al., ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/).
- Gal and Robere obtain superlinear lower bounds in the distinct comparator-circuit model, which restricts copying and is not an unrestricted fanout circuit lower bound. See [their primary ECCC report](https://eccc.weizmann.ac.il/report/2019/128/).
- The boundary-pivot selector and its sparse counterexample are project work in this cycle. They are not claimed as a published lemma or a Gap-MCSP counterexample.

## Result and next mechanism

**Strongest proved result:** the first-acceptance pivot law can have exponentially poor coverage even when the accepted Low family has `2^(O(N^beta))` members, each endpoint is an OPS-Low sparse truth table, the rejected reference is Hamming-separated from every endpoint, and the separator uses `O(N)` total gates. The proof above is exact. It invalidates the proposed generic pivot selector; it does not change any Gap-MCSP lower bound.

**Changed direction:** do not repair the uniform endpoint law with a sharper concentration estimate. Any successful boundary mechanism must prove an actual-High-specific inequality that forces the pivot mass to cover every Low table, or compute the C-422 maximin distribution directly while charging its optimization. The current counterexample says the separator's first boundary crossing does not supply that optimization for free.

**Quantitative frontier unchanged:** ordinary total-gate lower bound remains `S>=N-O(N^beta log N)-1` with C-406's additive logarithmic refinement; the OPS `N^(1+epsilon)` lower bound is open. Native `rho_GapMCSP>=N-o(N)` remains separate. The exact unconditional full-promise upper remains `O(N*2^(O(N^beta)))`. No paid-AND, OR-operation, wire, description-bit, runtime, wide-seed, arbitrary-endpoint, cycle, or semi-filter-extension bound is improved. No P-vs-NP result follows.
