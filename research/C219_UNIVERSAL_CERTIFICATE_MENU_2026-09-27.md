# C-219 - A redundant universal menu of mismatch certificates

Date: 27 September 2026

## Question

C-218 gives a sublinear certificate Q_z separately for each high table z. Can these certificates be selected from one short, input-independent menu, and does that resolve the product-rectangle routing problem?

Write `N=2^n`, fix `0<gamma<beta<1`, and let `Y'=SIZE(N^gamma)` and `Z={0,1}^N \ SIZE(N^beta)`. Let `M=|Y'|`, `H=ln M`, and let `d` be an integer such that every low/high pair has Hamming distance at least d. C-212 gives `d=Omega(N^beta)`.

Circuit counting gives `H=O(N^gamma n)`. There is also a matching lower bound `H=Omega(N^gamma n)`: choose `r=alpha N^gamma` for a sufficiently small constant alpha. By the C-212 sparse-indicator lemma, every r-point indicator has size at most `N^gamma`; the `binom(N,r)` distinct indicators all belong to Y', and `ln binom(N,r)=Theta(N^gamma n)`. Hence

`H = Theta(N^gamma n) = o(d)`.

## The redundant certificate-menu theorem

There are absolute constants `C_0,C_1` and a list of coordinate sets

`Q_1,...,Q_L subseteq [N]`

such that

- `L <= C_0 N/H = O(N^(1-gamma)/n)`;
- `|Q_j| <= C_1 N H/d = O(N^(1-beta+gamma)n)` for every j;
- for every `z in Z`, at least `L/2` indices j satisfy
  
  `dist_H(z|Q_j, pi_Qj(Y')) >= 16H`.

In particular, each such Q_j is a common mismatch certificate for every low row, with a margin of at least `16H` mismatches. Both the menu size and each menu item are sublinear in N for fixed `0<gamma<beta`.

### Proof

Choose a uniformly random m-subset Q of `[N]`, where

`m = ceil(32 N H/d)`.

For fixed `z in Z` and `w in Y'`, put `D={i:w_i != z_i}` and `X=|Q intersect D|`. Then X is hypergeometric, with mean `mu=m|D|/N >= 32H`. The hypergeometric Chernoff bound gives

`Pr[X < 16H] <= Pr[X < mu/2] <= exp(-mu/8) <= exp(-4H)`.

A union bound over M low tables shows that a random Q fails the margin condition for z with probability at most

`M exp(-4H)=exp(-3H)`.

Now draw L independent sets Q_j, with `L=ceil(2N/H)`. For a fixed z, the number of sets failing its margin condition is stochastically dominated by `Bin(L,exp(-3H))`. Thus

`Pr[at least L/2 failures] <= 2^L exp(-3HL/2) <= exp(-HL)`

for all sufficiently large H. Union-bounding over at most `2^N` tables gives failure probability at most

`2^N exp(-HL) <= exp(N ln 2 - 2N) < 1`.

So there exists a menu for which every high table has at least L/2 good indices. Since `H=Theta(N^gamma n)` and `d=Omega(N^beta)`, the asserted size bounds follow; also `m/N=O(N^(gamma-beta)n)=o(1)`, so these are proper sublinear samples.

## What the menu buys

For each menu item define its low projection

`P_j = pi_Qj(Y')`.

A high table z has at least L/2 projections at distance at least `16H` from P_j. The menu removes the need to invent an arbitrary Q_z at runtime: one can hardwire a polynomial-size catalog, and a Bob-side selector can choose the first index meeting the local distance condition. The index-selection skeleton uses O(L) stages in the abstract communication graph.

The menu also yields a precise separator normal form. Define a Boolean function on full truth tables by

`g_j(x)=1 iff dist_H(x|Q_j,P_j) < 16H`,

and put

`G(x)=AND_{j=1}^L g_j(x)`.

Every x in Y' has distance zero from every P_j, so G(x)=1. Every z in Z has at least one j with distance at least 16H, so G(z)=0. Thus G separates the reduced promise.

## Why this does not yet give a small circuit or DAG

The unresolved object is the circuit complexity of each projected robust-consistency predicate `g_j`. Even the radius-zero predicate

`q in P_j iff some size-N^gamma circuit agrees with q on all addresses in Q_j`

is a partial circuit-synthesis / range-membership predicate. Its succinct description is not a small Boolean circuit for its membership function. The generic sparse-indicator implementation costs

`O(m + R_j*m/log(R_j+1))`,

where `R_j` is the number of m-bit strings within distance `<16H` of P_j; the elementary bound `R_j <= min(2^m, M*sum_{a<16H} binom(m,a))` is still far above polynomial in the parameters here. No small implementation or lower bound for these particular g_j has been established.

There is a second logical limit: proving that this particular conjunction G is large would not prove that every separator is large. It is one separator construction, not a normal form theorem for arbitrary separators. Conversely, a small circuit for the g_j would only give a separator for Y'; that would imply a lower bound on the original promise only if one proved such a lower bound, not by monotonicity in the other direction.

The top-level menu therefore closes only the certificate-addressing subproblem. A standard rect-DAG still needs to solve the local mismatch relation inside a chosen Q_j, equivalently implement a separator for the projected row set against the selected high projection set. Product-hull-safe state reuse and the existing C-80/C-160 calibrations remain mandatory.

## Literature boundary

Hirahara, Oliveira, and Santhanam prove NP-hardness results for minimum-size OR-AND-MOD circuits, including a partial-function variant. Those results concern that restricted circuit basis and an optimization objective; they do not give a general Boolean circuit lower bound for the projection predicates g_j. See [their CCC 2018 paper](https://wrap.warwick.ac.uk/id/eprint/129370/1/WRAP-NP-hardness-minimum-circuit-size-problem-OR-AND-MOD-circuits-Oliveira-2018.pdf).

## Disposition and next proof target

C-219 proves a redundant universal certificate menu and a separator decomposition into projected consistency predicates. It materially improves the C-218 certificate-selector formulation, but it is not a C-75 separator lower bound or construction of polynomial size. No q lower bound or P-vs-NP proof follows. The next test is to study the circuit complexity and product-rectangle search cost of `g_j`, and to determine whether a theorem can force every separator to pay for such projected consistency checks. Keep O-141 and the transfer threshold `S_rect > N^(3+3epsilon)/log N` under the current cubic compiler unchanged.

