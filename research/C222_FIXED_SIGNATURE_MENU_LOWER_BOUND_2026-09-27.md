# C-222 — A fixed menu cannot universalize circuit-wire signatures

Date: 27 September 2026  
Scope: test a direct repair to the C-115 gate-signature witness. This proves a strong obstruction to that architecture, not a lower bound for arbitrary rect-DAGs or fusion covers.

## C-115 candidate being tested

Given a particular low circuit `C`, C-115 selects `k=Theta(log s2)` of its wire values. The table `w=C(x)` is a function of that signature, and the lookup cost `O(k 2^k)` is kept below the circuit-size gap. If a high table `z` were constant on every signature cell, it would also be a cheap lookup of `C`; therefore some cell contains a mismatch. The obstacle is that this signature depends on C. Test whether a fixed menu of small address signatures can replace the C-dependent choice.

## Theorem: every polynomial-size fixed menu misses a low sparse indicator

Set `N=2^n`, `s2=N^beta`, `s1=N^beta/(c n)`, for fixed `0<beta<1`. By the C-212 point-patching bound, there is a constant `eta>0` such that every indicator `1_S` of a set `S subseteq [N]` with `|S|=t=floor(eta N^beta/n)` belongs to `SIZE(s1)` for all sufficiently large n. Fix any address signature `G:[N]->[K]`; its fibers partition `[N]` into at most K cells. A support indicator `1_S` factors through G (that is, `1_S(x)=g(G(x))` for some lookup g) exactly when S is a union of whole fibers.

For any one signature, the number of t-subsets that are unions of its fibers is at most `sum_(j=0)^t binom(K,j)` because a union of total size t uses at most t cells. If `K>=t`, this is at most `(eK/t)^t`, so the fraction of t-subsets represented is at most

`(eK/t)^t / binom(N,t) <= (eK/N)^t`.

If `K<t`, the number is at most `2^K<=2^t`, and the represented fraction is at most `2^t (t/N)^t`; this is also `2^(-Omega(N^beta))`. In particular, for every `K<=N^beta`, one fixed signature represents at most a `2^(-Omega(N^beta))` fraction of the low t-sparse indicators. Therefore any menu covering all these low tables needs

`L >= 2^(Omega(N^beta))`,

which is superpolynomial in N.

The bound applies to the C-115 signature budget: if the lookup cost `O(K log K)` must remain below `s2-s1`, then `K=O(N^beta/n)` (up to constants), well inside `K<=N^beta`.

## Proof details and limits

The cell-union characterization is exact: a function of G is constant on every fiber, and conversely any union of fibers is the preimage of a set of signature values. The counting bound is independent of how signatures are computed; even arbitrary maps with K outputs need an exponential-size menu. The sparse indicators are all low by shared point-indicator circuits, with t chosen as a sufficiently small constant fraction of `s1`.

This kills only the plan “choose one public low-dimensional address partition from a polynomial-size menu, then apply the C-115 fiber-variation lemma.” It does **not** rule out a signature chosen adaptively from the actual circuit, an implicit selector whose states share across signatures, or a general separator that never factors its low tables through one address signature. C-219's coordinate-certificate menu is different: its items are mismatch-hitting sets, not partitions through which every low table must factor. No general DAG or fusion lower bound follows.

## Next target

The witness needs a C-dependent partition, but enumerating such partitions is exponential. The live question is whether an adaptive DAG can expose only the part of a circuit's signature that a given high column needs while preserving product-hull correctness across low circuits. Any proposed sharing must survive C-80/C-160 and the C-209 merge law. The current C-75 transfer thresholds are unchanged.



## C-222-A: menu cardinality is not adaptive selector complexity

The theorem lower-bounds the number of fixed signatures in a menu. It does **not** lower-bound the circuit size of a selector that computes an appropriate signature from the table. For the sparse-indicator subfamily used in the proof, such a selector is near-linear: on input `w` of Hamming weight t, sort the N records `(w_i,i)` with a fixed bitonic sorting network, then output the t addresses whose marker is 1. The network uses `O(N log^2 N)` comparators; each comparator on an address payload costs `O(log N)` Boolean gates, so the selector has size `O(N log^3 N)` and output length `t log N=O(N^beta)`. Those addresses specify a fixed-topology point-indicator circuit for `w`, of size `O(n+t n/log(t+1))<=s1` when eta is sufficiently small. Thus an exponentially large menu can have an efficiently computed choice on this structured subfamily.

This construction does not extend to arbitrary `SIZE(s1)` truth tables: finding a small circuit for a general low table is a search-MCSP task, and no small selector is known here. It does show that the C-222 menu count cannot be promoted to a lower bound on adaptive selector circuit size without an additional argument. The live target remains either a selector lower bound for the full low class or product-hull-safe sharing of C-dependent signatures in a general DAG.

