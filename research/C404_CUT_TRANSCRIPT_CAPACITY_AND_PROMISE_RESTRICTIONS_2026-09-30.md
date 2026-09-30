# C-404 — Cut transcripts, shared computation, and promise-preserving restrictions

Date: 30 September 2026  
Status: the proposed cut-capacity mechanism is proved and closed at the linear scale; the OPS frontier is unchanged.

## 1. Exact target and magnification check

Let `N=2^n`. Oliveira–Pich–Santhanam, Theorem 1.4, uses a universal constant `c>=1` and the promise

```text
YES: circuit complexity at most s1 = 2^(beta n)/(c n) = N^beta/(c log2 N)
NO:  circuit complexity at least s2 = 2^(beta n) = N^beta.
```

The theorem states the threshold with a universal `c`; its displayed proof instantiates `c=10`. I retain the theorem's stated universal-constant form here and do not silently alter the low threshold.

The magnification premise is: there is one `epsilon>0` such that for every sufficiently small fixed `beta>0`, no circuit family of size `N^(1+epsilon)` solves this promise. It implies `NP not subseteq P/poly`, hence `P != NP`. The non-membership convention is asymptotic (failure of a size-`N^(1+epsilon)` family); a lower bound at every sufficiently large length is stronger than the theorem requires. The middle band remains unrestricted. This is the ordinary total-gate model, with unrestricted fanout. [OPS, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).

## 2. Mechanism tested: cut-transcript capacity

For a Boolean function `f` on `N` bits and a partition `pi=(X,Y)` of its inputs, let `D_pi(f)` be deterministic two-party communication complexity. Alice receives `x` on `X`, Bob receives `y` on `Y`, and together they must output `f(x,y)` on every input.

### Lemma (circuit-to-cut protocol)

If a fan-in-two circuit `C` with `S` AND/OR/NOT gates computes `f`, then for every partition `pi`,

```text
D_pi(f) <= 2S+1.
```

**Proof.** Assign each primary input to its owner and each internal gate to either party. Topologically simulate `C`. Whenever a wire from a node owned by one party enters a gate owned by the other, the first party sends that wire's one-bit value. There are at most `2S` wires entering gates, since fan-in is at most two. The owner of the output sends one bit if needed. Each party can evaluate its assigned gates once it has received the crossing-wire values. This computes exactly `f` and uses at most `2S+1` communicated bits. Gate reuse is respected: each crossing wire value is sent once and then reused. Therefore `S >= (D_pi(f)-1)/2`. ∎

The strongest possible `D_pi` is at most `min(|X|,|Y|)+1 <= N/2+1`, by sending the smaller input side. Thus any single-cut consequence is at most linear in `N`. Using `k` partitions and summing does not amplify this: the proof gives `sum_pi D_pi(f) <= k(2S+1)`, and one wire may cross every one of those partitions. Without a proved restriction on how often a shared wire can be charged, the factor `k` cancels. Such a restriction would be a new assumption about the circuit or an unproved non-shareability principle, so it cannot be used here.

### Strong counterconstructions to local-interaction charging

These are counterexamples to the mechanism, not separators for Gap-MCSP.

* **Parity:** `XOR` of `N` bits has an `O(N)` fan-in-two AND/OR/NOT circuit: implement each XOR with a constant number of allowed gates and reuse each prefix. Expanded pairwise incidence counts can be quadratic while total gates stay linear.
* **Repeated-block equality:** on `m` blocks of `L` bits, compare every block with the first and AND the `mL` equality tests. This is `O(mL)=O(N)` gates. Equality has deterministic communication complexity `Theta(L)` across a split of two `L`-bit strings, so maximal linear cut demand is compatible with linear circuit size.
* **Sparse parity checks:** for an `r x N` binary matrix of bounded row weight, compute every syndrome bit using `O(nnz(H)+r)` gates and AND them. If `r=O(N)` and row weight is constant, even the whole syndrome and its zero test cost `O(N)` gates.
* **Simple global block relations:** if adjacent blocks must satisfy a fixed linear-size relation (including equality, cyclic shift, or a sparse XOR map), compute and check each relation once. For `m` blocks of length `L`, a relation circuit of size `O(L)` gives `O(mL)=O(N)` gates.

These constructions separate **expanded incidences**, **crossing wires**, and **total gates**. Counting each block interaction as fresh work is false under arbitrary DAG reuse. Input wires, a hardwired matrix's description bits, and the circuit-construction time are not paid gates; the gate bounds above count only AND/OR/NOT gates. The block and code examples use nonuniform hardwired relation data, as ordinary circuit lower bounds must allow.

## 3. Attempted transfer to the actual separator

For any valid Gap-MCSP separator `C`, the cut lemma applies to its total Boolean function, including its arbitrary middle-band behavior. It says that a superlinear cut lower bound on a particular partition would suffice, but no cut can exceed `N/2+1`. Summing cuts only returns `S=Omega(N)`. It does not distinguish low tables from high tables and yields no bound beyond C-403's `N-O(N^beta log N)`.

This is an exact failure point, not evidence that a separator has a cheap computation. The required statement would have to control the *joint* use of many cut transcripts by one DAG, while allowing a gate or wire to be reused in arbitrarily many contexts. No such joint potential is proved here.

## 4. Paired full-promise upper attempt: compress equality checks by linear fingerprints

The direct full-promise construction enumerates all `K1 <= 2^(O(s1 log(s1+n)))=2^(O(N^beta))` candidate low circuits and compares the input table with each candidate at all `N` positions, costing `O(N K1)` gates. I tried replacing each `N`-bit equality check by an `r`-bit linear fingerprint.

Let `H:F_2^N -> F_2^r` be linear. A fingerprint-only union accepts `x` if `H(x)=H(T)` for some low candidate table `T`. Since `0^N` is low, validity requires the entire fiber `ker(H)` to contain no high table. Every non-High table has circuit size below `s2`, and there are at most

```text
K2 <= 2^(O(s2 log(N+s2))) = 2^(O(N^beta log N))
```

such tables. Hence `|ker(H)|=2^(N-r) <= K2`, giving

```text
r >= N - O(N^beta log N).
```

So any linear fingerprint sufficient for this separator retains almost all `N` bits. In the straightforward OR-of-equalities construction, candidate comparisons still cost `O(r K1)=O(N K1)` gates, so the fingerprint gives no per-candidate savings; computing `H(x)` is an additional circuit cost (at most `O(Nr)` by naive linear-algebra evaluation) and must also be counted. This refutes the proposed short-linear-fingerprint compression, not arbitrary DAG compression of the candidate family, arbitrary nonlinear fingerprints, or the existence of a near-linear full-promise separator. It keeps gate count separate from hash description length and from construction runtime.

The promised near-linear upper bound is still unknown. The sparse-weight threshold from C-403 remains a separator only for a restricted YES subfamily; it rejects dense low tables and therefore is not a full-promise construction.

## 5. Replacement mechanism: promise-preserving hard restrictions

This route has an exact sharing-safe transfer lemma rather than an assumed no-sharing principle.

### Lemma (restriction composition)

Let `phi:{0,1}^m -> {0,1}^N` be computed by a fan-in-two circuit of `T` gates. Suppose every `phi(x)` is promised for Gap-MCSP and its YES/NO label equals a Boolean function `F(x)`. If `C` is any valid `S`-gate separator, then `C o phi` computes `F` with at most `S+T` gates. Therefore

```text
S >= Ckt(F) - T.
```

This composition preserves arbitrary sharing and requires no assumptions about C's internal organization. It would prove the OPS target if one could give, for each sufficiently small fixed `beta`, a map `phi` of cost `T=o(N^(1+epsilon))`, with a total image contained in the two promise sides, and a function `F` whose *unrestricted Boolean-circuit* lower bound exceeds `N^(1+epsilon)+T`.

### Adversarial construction: a large all-promised slice with an easy label

This tests the restriction route with an actual map into the exact promise. Let `B` be all truth tables with circuit complexity below `s2`; then `|B|<=K2`. Choose

```text
k = floor(s1/(10n)),   W = span{e_1,...,e_k} subset F_2^N,
```

where `e_i` is the table with a single 1 at coordinate `i`. Every vector of `W` has Hamming weight at most `k`; its minterm DNF has size `O(kn+n)<s1` for all sufficiently large `n`, so `W` consists entirely of YES tables.

Pass to the quotient `F_2^N/W`. The image of `B` has at most `K2` cosets. Choose a uniformly random subspace `Vbar` of codimension `d=ceil(log2 K2)+2` in this quotient. Each fixed nonzero coset lies in `Vbar` with probability at most `2^-d`, so the expected number of nonzero cosets from `B` that lie in `Vbar` is below 1. Therefore some `Vbar` avoids every such coset. Let `V` be its preimage. Then

```text
dim(V)=N-d,       V intersect B = W.
```

Thus every table in `V` is promised: the `2^k` tables in `W` are YES, and all other tables in `V` have circuit complexity at least `s2` and are NO. This uses the full low and high promise and puts no restrictions on the middle outside `V`.

The map can be encoded as an ordinary circuit. Because `W` is spanned by coordinate unit vectors contained in `V`, their coordinate functionals extend to an information set for `V`. After ordering these `m=N-d` coordinates first, write `V={(u,Au):u in F_2^m}`. Each of the `d` parity outputs in `Au` costs `O(m)` AND/OR/NOT gates (replace each XOR by a constant-size De Morgan circuit), so

```text
T = O(dm) = O(N^(1+beta) log N).
```

For any fixed target `epsilon` and sufficiently small fixed `beta<epsilon`, `T=o(N^(1+epsilon))`. The chosen nonuniform matrix has `O(dm)` coefficient bits; an explicit gate-list encoding may use up to `O(dm log(N+T))` wire-description bits. The random-existence proof does not give an efficient construction algorithm, and description/runtime are separate from gate count.

But the induced label is

```text
F(u)=1 iff u_{k+1}=...=u_m=0,
```

which has an `O(m)` circuit. Restriction composition therefore gives no positive lower bound on the separator size. This is a sharp counterexample to the idea that a large, promise-preserving slice or many low anchors alone forces a difficult computation. To obtain a useful restriction lower bound, the intersection `V intersect SIZE(s1)` must induce a hard (non-subspace-like) label while all remaining image points stay above `s2`; merely making the slice avoid non-High tables makes the label easy.

An explicit-hard-function transfer still inherits the general-circuit lower-bound bottleneck: published explicit Boolean-circuit lower bounds remain linear in input length (for example, the `3.1m-o(m)` result over the full binary basis), not `m^(1+delta)`. [Li and Yang, STOC 2022](https://doi.org/10.1145/3519935.3519976). The next avenue is therefore not just to find a cheap promise-preserving map; it is to make its low-side trace computationally hard without paying for that trace in the map.

## 6. Barriers, originality, and quantitative effect

The cut-transcript lemma is standard communication simulation; the application to an arbitrary Gap-MCSP separator is a proved project observation, not a new lower bound. The direct examples above are standard shared computations, not new constructions. The restriction-composition lemma and random-quotient slice are project-derived applications of elementary composition and subspace counting; originality relative to the full literature is not established. The slice construction is a geometry counterexample, not a new lower bound.

**Resource ledger:** throughout the circuit arguments, `S` counts all AND, OR, and NOT gates; OR gates are ordinary paid gates. Communication bits and circuit wires are separate measures. The quotient encoder's gate count, matrix/wire description length, and existence-search runtime are reported separately. No paid-AND-state or native cyclic-closure quantity is inferred, no `q^2` compiler is used, and no semi-filter extension is claimed. The native `rho>=N-o(N)` frontier remains as recorded in earlier closure reports; C-404 makes no claim to improve its treatment of arbitrary endpoints, wide seeds, reuse, cycles, or semi-filter extensions.

**Recent primary-literature check.** Carmosino, Dang, and Jackman's 2026 preprint *Constructive Separations from Gate Elimination* turns several gate-elimination lower-bound arguments for XOR, MUX, and affine dispersers into algorithms that find a counterexample to a proposed small circuit. The results remain linear-scale and concern fixed functions. They suggest testing promise-preserving gate substitutions, but provide no map whose every table is Gap-MCSP-YES or Gap-MCSP-NO, and therefore no transfer to O-1. This is a relevant technique lead, not an OPS lower bound. [2026 preprint](https://arxiv.org/abs/2604.23958).

OPS's magnification theorem is based on constructing anti-checkers under `NP subseteq P/poly`. Chen, Hirahara, Oliveira, Pich, Rajgopal, and Santhanam's locality barrier shows that for several magnification frontiers, the problem has small circuits augmented with bounded-fan-in oracle gates, while weak-model lower-bound methods can extend to those oracle gates. The paper also records an OPS Gap-MCSP local-oracle implementation. This warns against a proof that silently assumes a local access architecture; it does not rule out all lower-bound methods and does not invalidate the exact OPS theorem. The cut method here neither analyzes those oracle circuits nor crosses that barrier. [Chen et al., JACM 2022](https://doi.org/10.1145/3538391).

**Strongest proved statements for this cycle:** the cut-transcript simulation lemma `D_pi(f)<=2S+1`; the fingerprint width bound `r>=N-O(N^beta log N)` for the specified linear-hash separator attempt; and the existence of a codimension-`O(N^beta log N)` subspace `V` whose promise trace is exactly a `k=Theta(N^beta/(log N)^2)`-dimensional low subspace `W` plus high points, with a systematic encoder of `O(N^(1+beta)log N)` gates. The last construction is an obstruction to count-only restriction arguments, not a lower bound.

**Exact effect on the frontier:** none. C-403 remains the strongest ordinary total-gate lower bound, `S>=N-O(N^beta log N)-1=(1-o(1))N`. The OPS `N^(1+epsilon)` premise remains open for one fixed epsilon and every sufficiently small fixed beta. The native full-promise `rho>=N-o(N)` bound is separate and unchanged. No full-promise near-linear separator, native improvement, or P-vs-NP proof was obtained.

## Sources

* I. C. Oliveira, J. Pich, R. Santhanam, [Hardness Magnification Near State-of-the-Art Lower Bounds](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), Theorem 1.4 and the anti-checker proof.
* L. Chen et al., [Beyond Natural Proofs: Hardness Magnification and Locality](https://doi.org/10.1145/3538391), locality-barrier analysis.
* M. Carmosino, N. Dang, T. Jackman, [Constructive Separations from Gate Elimination](https://arxiv.org/abs/2604.23958), 2026 preprint.
* K. Iwama, O. Lachish, H. Morizumi, R. Raz, [An Explicit Lower Bound of 5n-o(n) for Boolean Circuits](https://www.wisdom.weizmann.ac.il/~ranraz/publications/P5nlb.pdf); and [A Better-Than-3n Lower Bound for the Circuit Complexity of an Explicit Function](https://doi.org/10.1145/3519935.3519976). These use different bases and both remain linear-scale results.
