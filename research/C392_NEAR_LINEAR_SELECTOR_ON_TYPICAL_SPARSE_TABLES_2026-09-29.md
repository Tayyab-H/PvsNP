# C-392 - A near-linear selector works on almost every sparse support

Date: 29 September 2026  
Route: strengthen C-23 against the exact coNP-verified relation R from C-388.  
Classification: **PROVED DISTRIBUTIONAL PARTIAL SELECTOR; NO ALL-HIGH SELECTOR, NATIVE BRIDGE, OR P-VS-NP RESULT.**

## 1. Statement

Let `N=2^n`, `S=ceil(N^beta)`, `s1=N^beta/(10n)`, and `T=ceil(1.515*s1)`, with a sufficiently small fixed `0<beta<1/10`. Use a standard fan-in-two circuit basis and choose a constant `A` such that the number `M_u` of n-input circuits of size at most `u` satisfies

```text
log2 M_u <= A*u*log2(u+n+2).
```

For a uniformly random `S`-element set `W` of addresses, write `f=1_W`. There is a fixed permutation `pi` of the N addresses such that, with probability `1-o(1)` over W:

1. `CC(f)>S`;
2. if B is the first S addresses outside W in pi-order, then `Q=(W,B)` has length `2S` and every circuit C of size at most T has empirical error at least `0.45` on Q.

Consequently, for the C-388 relation `R(f,Q)` with its error threshold `0.259`, a nonuniform family of circuits of size `O(N log^3 N)` outputs a valid Q on a `1-o(1)` fraction of uniformly random weight-S tables. If C-388's sample cap is smaller than `2S`, raise it to `max(L,2S)`; this remains `O(N^beta)` and preserves C-346's all-high witness-existence statement.

## 2. Proof

Choose a uniformly random permutation pi independently of W. The block W is uniformly distributed among the S-subsets of `[N]`. Conditional on W, B is uniformly distributed among the S-subsets of its complement. By symmetry, B is also marginally uniform among the S-subsets of `[N]`; independence between W and B is unnecessary.

For a fixed circuit C, let `p_C` be its fraction of 1s on the full address domain. Hoeffding's sampling-without-replacement inequality gives, for either block `X` in `{W,B}` and any fixed `epsilon>0`,

```text
Pr[ | average_X C - p_C | > epsilon ] <= 2 exp(-2 epsilon^2 S).
```

Set `epsilon=0.05` and union-bound over both blocks and all size-T circuits. The failure probability is at most

```text
4 M_T exp(-0.005 S).
```

Since `T <= 0.1515*S/n + O(1)` and `log2(T+n+2)=beta*n+o(n)`,

```text
log2 M_T <= (0.1515*A*beta + o(1))*S.
```

Choose beta small enough that `(ln 2)*0.1515*A*beta < 0.005`. The union-bound failure probability is then `exp(-Omega(S))`.

On the complementary event, every such C satisfies

```text
err_Q(C)
  = (1 - average_W C + average_B C)/2
  >= 1/2 - epsilon
  = 0.45.
```

Separately, circuit counting gives

```text
log2 M_S <= (A*beta + o(1))*n*S,
log2 binom(N,S) = (1-beta+o(1))*n*S.
```

If `A*beta < 1-beta`, the fraction of weight-S tables with circuit complexity at most S is `o(1)`. Combining this with the sampling event proves that a `1-o(1)` fraction of W are high and satisfy the exact C-388 relation, since `0.45>0.259`.

## 3. Selector circuit

Hardwire a permutation pi with success probability `1-o(1)`; one exists by averaging over pi. On input table f, sort its N address records by the key `(f_i descending, pi-rank ascending)`, and output the addresses in positions 1 through S and S+1 through 2S. When f has weight S, these are exactly W in pi-order followed by the first S zero addresses in pi-order.

A sorting network has `O(N log^2 N)` compare-exchanges. Each compares and routes an `O(log N)`-bit record, costing `O(log N)` fan-in-two gates, for a total `O(N log^3 N)` circuit size. This is `N^(1+o(1))`. The circuit is total, but its validity is proved only on the stated `1-o(1)` distribution of weight-S high tables; the permutation is nonuniformly hardwired and no efficient method for finding it is claimed.

The concentration inequality used here is the standard Hoeffding bound for sampling without replacement; see [Hoeffding (1963), *Probability inequalities for sums of bounded random variables*](https://www.tandfonline.com/doi/pdf/10.1080/01621459.1963.10500830).

## 4. What this establishes and what it does not

- It upgrades C-23's one-disagreement anti-checker on typical sparse supports to a constant empirical-error margin against the larger size-T class in C-388.
- It refutes any proposed all-selector lower bound whose hard inputs are only a `1-o(1)` fraction of uniformly random weight-S supports.
- The exceptional sparse supports remain uncontrolled. This is not a selector valid on every high table and does not refute O-230's worst-case target.
- The fixed permutation is obtained by averaging. No uniform procedure for finding it is provided.
- A near-linear partial selector is not a decision circuit: checking `R(f,Q)` remains coNP, and no q-preserving conversion to an arbitrary C-319 cover is known.

**Status:** distributional partial selector proved; no change to the native `q>=N-o(N)` bound, O-230's all-high selector problem, or the P-vs-NP status.
