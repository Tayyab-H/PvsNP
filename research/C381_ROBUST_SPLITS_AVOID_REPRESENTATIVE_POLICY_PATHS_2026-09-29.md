# C-381 - A robust splice split can avoid all selected policy paths

Date: 29 September 2026  
Route: Combine C-380 same-root acyclic switching paths with the C-320 robust owner-mask balls.  
Classification: **EXACT QUANTIFIER / ENTROPY OBSTRUCTION TO THE REPRESENTATIVE-PATH ARGUMENT.**

## 1. Setup

Let F be a family of K low tables with pairwise distance at least d = Omega(N), as in the C-320 code instantiation. Let Q be a valid C-319 cover with q polynomial in N. For each f in F, select one empty-consequence root r_f and one winning positional policy pi_f at that root.

For every ordered pair (f,g) with r_f = r_g, apply C-380 to the selected policies. Its acyclic switching path has at most 2q action changes and therefore at most 2q+1 intermediate hybrids.

For each *consistent* hybrid tau on this path, its selected seed literals define a sound cube. On D(f,g) = {a : f[a] != g[a]}, assign owner 0 to coordinates whose selected literal agrees with f and owner 1 to coordinates whose selected literal agrees with g. Give an arbitrary owner to coordinates in D(f,g) on which tau selected no literal. Consistency ensures no coordinate is assigned contradictory owners. On coordinates outside D(f,g), canonically set owner 0; those choices do not affect the splice because f and g agree there. The resulting full mask mu_tau has the property that h_(f,g,mu_tau) lies in tau's cube, so soundness implies h_(f,g,mu_tau) is in SIZE(s2).

There are at most
    M = K^2 (2q+1)
such representative-path masks, counting all same-root pairs and all their consistent hybrids.

## 2. Random splits almost surely miss these masks

Let P be uniform in {0,1}^N. For a fixed mask mu and radius r < N/2,

    Pr[dist(mu,P) <= r or dist(mu,P-complement) <= r]
       <= 2 * 2^(-N) * sum_(j=0)^r binom(N,j)
       <= 2^(-N + 1 + N H_2(r/N)).

By a union bound, the probability that P is within distance r of any representative-path mask or its complement is at most

    2 M * 2^(-N + N H_2(r/N)).

At the C-320 scale, r = Theta(N^gamma / n) for fixed beta < gamma < 1, so N H_2(r/N) = O(N^gamma) = o(N). Also log K = O(s1 log(s1+n)) = O(N^beta) = o(N), and log q = O(log N). Hence

    log M + N H_2(r/N) = o(N),

and the probability above is 2^(-N+o(N)).

Meanwhile, C-320's robust-split estimate says that the fraction of P for which *some* off-diagonal code splice lands in SIZE(T), T = N^gamma, is at most

    K^2 |SIZE(T)| / 2^d = 2^(-Omega(N)),

because log K = O(N^beta), log |SIZE(T)| = O(N^gamma n), and d = Omega(N). Thus almost every P is robust for all codeword pairs, and almost every P also avoids every representative-path mask. In particular, there exists a split satisfying both properties.

This also gives a necessary covering threshold for these canonical full masks. If a P-independent mask family were to hit every robust split through a radius-r ball or its complement, its Hamming neighborhoods would have to cover a 1-2^(-Omega(N)) fraction of the split space. Since one mask covers at most 2^(-N+1+N H_2(r/N)) of that space, the family would need size at least

    2^(N - N H_2(r/N) - O(1)) = 2^(N-O(N^gamma)).

Thus a forcing argument based only on a preselected list of path masks needs essentially full-N-bit mask dispersion; the representative family is exponentially too small.

If an argument may choose arbitrary owners outside D(f,g) *after seeing P*, use the projection onto D instead. For a fixed owner pattern on D, the probability that P restricted to D is within radius r of that pattern or its complement is at most 2^(-d+1+d H_2(r/d)) = 2^(-Omega(N)), since d=Omega(N) and r=Theta(N^gamma/n). Union-bounding over the same 2^(o(N)) selected path patterns still shows that almost every split avoids all of them, even under this more permissive extension convention.

For this split, C-320 makes every owner mask within radius r of P or its complement high, while every consistent hybrid on the chosen C-380 paths has its owner mask outside those two balls. Therefore the selected acyclic paths do not force a forbidden splice.

## 3. What this proves, and what it does not

This is a quantifier-order obstruction, not a counterexample to C-320 or C-380. The code family has only 2^(o(N)) members, and one representative policy per member yields only 2^(o(N)) path patterns. Each full-mask radius-r ball occupies only a 2^(-N+o(N)) fraction of the split space; even allowing P-dependent extension on common coordinates leaves a 2^(-d+o(N)) fraction for each fixed disagreement-set pattern. The robust-split property holds for almost all splits, so it can coexist with avoidance of the entire representative-path family.

Consequently, the route

    choose one policy per low anchor
    -> connect same-root policies by C-380 paths
    -> invoke the C-320 forbidden balls

cannot by itself force a soundness contradiction, even when Q has polynomially many states. It cannot establish a superlinear q bound without an additional theorem that forces substantially more mask coverage or ties the split to state-generated data.

There is also a semantic boundary: every consistent vertex on a C-380 path is already a globally winning acyclic policy, so its splice is in SIZE(s2) by soundness. C-320's robust split is designed to put high tables near a chosen split; it cannot turn one of these already-sound policy cubes into a high accepted table. A useful C-281/C-320 contradiction must therefore splice a context and continuation that do *not* form one globally well-founded policy, while proving that their compatible product is nevertheless accepted.

This does *not* rule out arguments using all winning policies, multi-anchor compatible products, a nonrandom split tied to Q, or a direct full-promise cover. The all-policy family may have as many as 2^(O(q log N)) action tables, which is already too large for the above entropy estimate at q >= N. The missing mathematical step is to constrain that family by endpoint incidence and transition semantics rather than count it generically.

## 4. Relevant branching-program result and transfer boundary

Glinskih and Riazanov prove that every read-once nondeterministic branching program for total BP-MCSP, k-BP-MCSP, or OBDD-MCSP has size N^(Omega(log log N)) (Corollary 4 of their [ECCC 2024 report](https://eccc.weizmann.ac.il/report/2024/117/download/)). This is a genuine superlinear result for those total minimization predicates and makes the one-sided/read-once boundary worth tracking.

It does not transfer here: the target is a gap separator for general circuit size, while C-319 is an alternating least-fixed-point game with two obligations per state and may have cycles. No size-preserving conversion from an arbitrary C-319 cover to a read-once NBP is known. The result is therefore a lead only if a new OPS- and endpoint-preserving bridge is proved; it is not evidence for a q lower bound in the current model.

## 5. Checkpoint

- C-380's same-root acyclic path lemma: unchanged and valid.
- C-320's robust split: unchanged and valid.
- Their combination for one chosen policy per low anchor: proved insufficient to force a forbidden mask.
- Native lower bound: still q >= N-o(N).
- No state-capacity theorem, full-promise near-linear cover, or P-vs-NP proof follows.

The next mechanism must force mask dispersion from the full endpoint-realizable policy/continuation grammar, or abandon the robust-split route for a construction/measure that is not avoidable by a generic split.
