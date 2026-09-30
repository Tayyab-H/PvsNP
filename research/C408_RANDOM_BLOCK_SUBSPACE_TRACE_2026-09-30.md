# C-408 — Random block-constant restrictions have an easy low trace

**Status:** proved counterconstruction for the repeated-block / random-partition restriction route. On a block-constant subspace of dimension `N^gamma`, the full induced Gap-MCSP promise is separated by distance to the two constant patterns, using `O(N^gamma log^2 N)` gates. This is not a full-promise separator and does not change either quantitative frontier.

**OPS calibration:** Theorem 1.4 of Oliveira–Pich–Santhanam states: for a universal `c>=1`, if one fixed `epsilon>0` gives `Gap-MCSP[N^beta/(c n),N^beta]` circuit complexity greater than `N^(1+epsilon)` for every sufficiently small fixed `beta>0`, then `NP` is not contained in `P/poly`. The paper's promise is YES for `CC<=s1` and NO for `CC>=s2`; their proof exhibits the concrete denominator `10n`. This cycle uses `s1=N^beta/(10n)` and `s2=N^beta` and proves a separator for the stronger NO side `CC>=s2`. It makes no magnification claim.

## Question

C-407 showed that random coordinate-support slices expose only sparse low tables. This cycle tests a distinct, denser restriction: choose a random balanced partition of table coordinates and allow each block to vary as one bit. This includes both sparse tables and tables close to all ones, and directly stress-tests repeated-block equality examples.

Fix `N=2^n`, `0<beta<1/2`, `s1=N^beta/(10n)`, `s2=N^beta`, and any fixed `gamma` with `beta<gamma<1`. The promised YES tables have `CC<=s1`; take promised NO tables to have `CC>=s2`, and leave the middle unpromised. Let

`m=2^floor(gamma*n)`, `r=N/m`.

Choose a uniformly random labeled partition `P=(B_1,...,B_m)` of the `N` coordinates into `m` blocks of size `r`. Define the `m`-dimensional subspace

`V_P={f_x : x in {0,1}^m}`, where `f_x` is constant with value `x_j` on block `B_j`.

## Theorem

For all sufficiently large `N`, some such partition `P` has the following property:

1. If `f in V_P` and `CC(f)<=s1`, then
   `min(wt(f),N-wt(f))<5s1`.
2. If `min(wt(f),N-wt(f))<=6s1`, then `CC(f)<s2`.

Thus the entire induced promise on `V_P` is separated by

`T_P(x)=1 iff r * min(wt(x),m-wt(x)) <= 6s1`.

This threshold circuit has `O(m log^2 m)=N^(gamma+o(1))` fan-in-two gates. Both YES and NO occur in the restriction: zero is YES, and `|V_P|=2^m` exceeds the number `2^(O(N^beta n))` of non-High tables because `gamma>beta`.

## Proof

The number of fan-in-two AND/OR/NOT circuits on `n` inputs with at most `s1` gates is at most

`(s1+1)(3(n+s1+2)^2)^s1 = 2^((2beta+o(1))s1 n)`.

For a fixed support set `S` of size `w=kr`, the probability that it is a union of exactly `k` blocks of a uniformly random balanced partition is

`Pr[S is a block union] = binom(m,k)/binom(N,w)`.

Writing `p=w/N=k/m` and `H_2` for binary entropy, standard binomial bounds give

`Pr[S is a block union] <= (N+1) * 2^(-(N-m)H_2(p))`.

For `5s1<=w<=N-5s1`, we have `5s1/N<=p<=1-5s1/N`. Since `H_2` is symmetric and increasing up to `1/2`, the exponent loss is at least

`(N-m)H_2(5s1/N) = (5(1-beta)+o(1))s1 n`,

using `m=o(N)` and `s1=N^beta/(10n)`. A union bound over all low circuits has exponent

`(2beta-5(1-beta)+o(1))s1n = (7beta-5+o(1))s1n < 0`,

for every fixed `beta<1/2`. Thus some partition has no low circuit table whose support is a union of blocks with weight in `[5s1,N-5s1]`. Any low table in `V_P` must be within fewer than `5s1` coordinates of either the all-zero or all-one table. This proves item 1.

For item 2, a table at Hamming distance `d` from zero has an address-minterm DNF with at most `dn+n-1` gates. A table at distance `d` from one has the same bound by complementing such a DNF. At `d<=6s1`, the cost is at most `0.6N^beta+O(n)<s2` for sufficiently large `N`. Hence every High table lies outside both radius-`6s1` balls.

The pattern threshold computes the union of two Hamming balls in `{0,1}^m`, centered at `0^m` and `1^m`. A sorting network and fixed threshold comparisons use `O(m log^2m)` gates. This proves the restricted-promise separator.

## Explicit sharing-control mechanism on the current frontier

C-406 remains the strongest proved mechanism here that actually measures unrestricted gate sharing. For a fan-in-two output-ancestor DAG with `S=G` gates, let `E_g` be its number of gate-to-gate dependency edges and `mu=E_g-G+1` its connected undirected cycle rank (primary-input occurrences are separate formula leaves). Unfolding the DAG yields a De Morgan formula with at most `2S*2^mu` leaves. OPS's U2-formula lower bound says that every formula for `Gap-MCSP[n^d,N^(alpha/2-o(1))]` has more than `N^(2-alpha)` leaves. For fixed `beta<alpha/2`, its YES set is contained in the target YES set because `n^d<=N^beta/(10n)` eventually, and its NO set is contained in the target NO set because `N^(alpha/2-o(1))>=N^beta` eventually. Thus the target separator also separates that formula-hard promise, so `2S*2^mu>N^(2-alpha)`. If `S<=N^(1+delta)`, this forces `mu>(1-alpha-delta)log_2 N-O(1)`. The input-pin count gives `S>=E(C)+mu-1`; optimizing fixed `alpha>2beta` and small `delta` proves `S>=E(C)+gamma log_2 N-O(1)` for each fixed `beta<1/2` and `gamma<1-2beta`. This is a proved sharing-aware gate charge, and it assumes no description reconstruction or witness enumeration.

This is a real sharing constraint but only an additive logarithmic gate improvement over essential-input count `E(C)>=N-O(N^beta log N)`. The `N`-input parity function has an `O(N)` AND/OR/NOT circuit with `Theta(N)` gate-graph reconvergence, so the forced `Omega(log N)` cycle rank alone cannot imply superlinear gates. Repeated-block equality can be a linear formula; sparse parity-check predicates and simple global XOR relations have linear-size shared implementations when their total descriptions are linear. These examples refute generic interaction or reconvergence charges; they are not counterexamples to the Gap-MCSP separator lower bound. C-408 does not improve this mechanism.

## Resource and scope audit

- **Total gates and wires:** `O(m log^2m)` for the restricted separator and its sorting network.
- **Description:** `O(m log^3m)` bits for the threshold circuit; `O(N log m)` bits describe the block assignment and coordinate embedding.
- **Wires and map:** `x -> f_x` uses no Boolean gates when wires are free, but has `N` output incidences and unrestricted fanout. The selected partition is nonuniform; no efficient deterministic construction is proved. Exhaustive verification against all low circuits costs `2^(O(N^beta))` time up to polynomial factors.
- **Native fusion:** no endpoint list, paid-AND bound, OR-rule bound, or least-fixed-point compiler is provided. No native `rho` claim follows. Any future transfer must preserve arbitrary semantic endpoints, wide seeds, unrestricted reuse, cycles, and every required semi-filter extension; C-408 imposes none of those restrictions and proves no native cost bound.

## Adversarial checks and full-promise attempt

- **Repeated-block equality:** this is precisely a block-constant restriction. For a good random partition, its low tables lie near `0^m` or `1^m` in pattern space; the induced label is read by the stated Hamming-ball threshold. This gives no expensive readout mechanism.
- **Parity:** the address-parity table is low, has weight `N/2`, and cannot be constant on every block of the selected partition, or it would contradict item 1. It lies outside this restriction, which is why the theorem is not full coverage.
- **Sparse parity checks and simple global block relations:** if the resulting address table is low and block-constant for this selected partition, item 1 forces it within `5s1` table entries of a constant. Otherwise it is outside the restricted promise. This argument does not establish a cost for computing a syndrome vector or checking correlated addresses; shared parity/XOR circuits can reuse intermediate parities. For a structured partition into address-prefix fibers, a block pattern generated by a small circuit on the prefix can be read with that circuit's cost; this random-partition theorem does not claim otherwise.
- **Full-promise distance test:** accepting every table within `6s1` of zero or one is sound against High by minterm construction, but it rejects other dense low tables such as parity.
- **Full-promise exact attempt:** enumerating the `M<=2^(O(N^beta))` low-circuit descriptions and comparing each against all N entries still costs `O(NM)` gates/wires and `O(MNs1)` direct construction time. No near-linear factorization emerged.

## Frontier effect and route change

This is an elementary project-derived counting lemma, not a claim of a new general circuit lower-bound theorem. The proposed lever was to force every low trace on a large block-constant slice near a constant, then use that geometry to control shared computation. The entropy/counting proof establishes the trace property, but it does **not** force extra gates in a full-promise separator: the restricted promise has the explicit `O(m log^2 m)` threshold separator above. The mechanism fails at the transfer-to-computation step. Its strongest counterconstruction is the exact repeated-block trace with a cheap separator; ordinary `O(n)` parity and structured-prefix readouts also show that repeated values or global correlations alone do not imply expensive gate work. C-258's native repeated-block cover remains a separate model-specific result; no native cost transfer is made here.

The result gives no lower bound on full-promise separators. The ordinary leading lower bound remains `N-O(N^beta log N)` with C-406's additive refinement; the OPS `N^(1+epsilon)` target is open. Native `rho_GapMCSP>=N-o(N)` is unchanged. Retire random support and random block-constant embeddings as hard-trace routes. The next cycle returns to the full promise: seek a direct gate-work invariant or construct a separator that handles every promised YES and NO table.

### Primary source checked

- Oliveira, Pich, Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf), for the OPS threshold conventions and circuit basis.
- Chen, Hirahara, Oliveira, Pich, Rajgopal, Santhanam, [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://arxiv.org/abs/1911.08297), and Pich, [*Localizability of the Approximation Method*](https://arxiv.org/abs/2212.09285), for the method-level locality barrier. That barrier concerns known lower-bound methods that remain valid against circuits with small-fan-in, arbitrarily powerful local oracle gates. C-408's restriction-counting lemma is not such a lower-bound method and does not derive a circuit lower bound. C-406 imports formula hardness and obtains only logarithmic reconvergence, so neither result contradicts or bypasses the barrier.
- Project calibration: [C-258 repeated-block native cover](C258_REPEATED_BLOCK_NATIVE_COVER_2026-09-27.md).
