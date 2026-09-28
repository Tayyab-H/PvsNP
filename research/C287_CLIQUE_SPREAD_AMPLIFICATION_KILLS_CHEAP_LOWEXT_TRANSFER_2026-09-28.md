# C-287 - Clique spread amplification gives a canonical-table map-cost obstruction

Date: 28 September 2026  
Classification: **CONDITIONAL ROUTE TEST; transfer window unresolved (corrected by C-290).**  
Depends on: C-286 directional simultaneous approximation; C-275 sparse-support interpolation; C-125 composition.

## 1. Source distributions

Let the source graph have `m=N^2` vertices. Choose a no-clique threshold `ell=ceil(D*(ln m)^2)` and positive clique size `k=2*ell`. This safely satisfies the disjoint-promise requirement `ell<k`, as well as Rao's parameter conditions `ln m < eta_0*ell < k` and `k*ell <= eta_0*m`, for sufficiently large `N` and fixed `D` large enough. (The earlier choice `k=ceil(2*eta_0*ell)` did not explicitly ensure `k>ell`.)

```text
ln m < eta_0*ell < k,       k*ell <= eta_0*m.
```

Let `X1=C_W` for a uniform `k`-vertex set `W`. Let `X0` be `G(m,p_e)` with `p_e=m^(-2/(ell-1))`. Rao's union bound gives

```text
Pr[X0 has an ell-clique] <= binom(m,ell)*m^(-ell) <= 1/2.
```

Conditioning on `Q={X0 has no ell-clique}` produces a distribution supported entirely on source NO inputs, with `Pr(Q)>=1/2`. The source may be the total monotone function `CLIQUEn,ell`; `X1` is YES and `X0|Q` is NO.

## 2. Exact certificate amplification threshold

Rao's rail approximators are clique-DNFs with terms `S` of size at most `t`; a term fires if the graph contains a clique `C_T` with `S subseteq T` and `|T|>=2`. If a rail fires on a `p` fraction of `X1`, choose a deterministic contained term `S(X1)` for each firing input. Since `W` is uniform among `k`-sets, for each set `A` of size `s>=1`,

```text
Pr[A subseteq S(X1) | rail fires] <= (k/m)^s/p = (p*m/k)^(-s).
```

The conditional term law is therefore `p*m/k`-spread. Rao's spread-clique lemma with fixed base set empty implies firing on `X0` with probability at least `1-xi` if

```text
p*m/k >= alpha_C*ln(t/xi)/p_e^t.
```

Thus a sufficient threshold is exactly

```text
theta_C = alpha_C*(k/m)*ln(t/xi)*p_e^(-t).
```

Terms of size zero or one are easier: `G(m,p_e)` contains an edge through any fixed vertex, and contains some edge, with probability `1-exp(-Omega(p_e*m))`; here `p_e=1-O(1/ln m)`.

## 3. Approximation errors and NO conditioning

Rao's parameters are

```text
t = eta_1^2*(ell-1)/ln m,
epsilon_R = exp(-eta_1*ell),
```

for sufficiently small fixed `eta_1`. For `a` shared AND gates, C-286 gives directional errors

```text
delta1 = a*(m/(k*ell))^(-t),
delta0 = a*m^(t+1)*epsilon_R.
```

Conditioning from `X0` to `X0|Q` multiplies a NO error probability by at most 2. An amplified rail's firing failure similarly rises from `xi` to at most `2*xi` on `Q`.

## 4. Canonical table contradiction at the full transfer range

Set `xi=1/(16N)`. Since `m=N^2`, `ell=Theta((ln N)^2)`, and `k=Theta((ln N)^2)`,

```text
p_e^(-t) = exp(2*eta_1^2) = Theta(1),
theta_C = Theta((ln N)^3/N^2),
N*theta_C = Theta((ln N)^3/N) = o(1).
```

The gatewise Rao proof rules out a monotone separator with at most

```text
L0 = (m/(k*ell))^(t/3) = exp(Omega((ln N)^2))
```

AND gates. It also rules out a C-125 encoder with any AND cost `a<=L0/4`: its directional errors obey

```text
delta1 <= (1/4)*(m/(k*ell))^(-2t/3) = o(1),
delta0 <= (1/4)*(m/(k*ell))^(t/3)*m^(t+1)*exp(-eta_1*ell)
       <= exp(-c*ell+O(ln m)) = o(1),
```

for a fixed `c>0`. For the second estimate, take logs, use `t*ln m=eta_1^2*(ell-1)`, and bound the exponent by `(4*eta_1^2/3-eta_1)*ell+O(ln m)`; it is negative for Rao's sufficiently small `eta_1`.

On `X0|Q`, all inputs are exact NO. Each dominant rail fires with probability at least `1-2*xi`. The union bound over `N` rails and the simultaneous directional NO error leave positive probability that every dominant true rail occurs together on one NO graph. On YES, `N*(theta_C+delta1)=o(1)`, so the canonical table is within distance at most one of a low witness for all large `N`. C-275 patches one coordinate for `O(log N)` gates, and

```text
s1 + O(log N) < s2
```

for every fixed `0<beta<1`, with `s1=N^beta/(c0 log N)` and `s2=N^beta`. The canonical table is therefore low, but the NO image places it below a high one-hot code, contradiction.

## 5. What the map obstruction does and does not imply

The `L0` lower bound above is for ordinary monotone AND cost. Unrolling an `r`-state cyclic separator for `r` rounds uses at most `C*r^2` AND gates, so

```text
CycAnd(CLIQUE_{m,k} vs no-ell-clique) >= sqrt(L0/C)
```

for an absolute unrolling constant `C`. This is a **lower bound** on `CycAnd`, not an upper bound. Although `sqrt(L0/C)<L0/4`, that comparison does not show `CycAnd<L0/4`; the inference in the original version of this section was invalid. C-290 audits the remaining transfer interval and gives a color-coding monotone upper bound. The only established route statement is that any valid C-125 map has cost `a>L0/4`; this leaves open a useful interval if `CycAnd>L0/4`.

This does not rule out another source or a transfer not using C-125. It does not change the actual Gap-MCSP bound, which remains `q=N-o(N)`.
## References

- Rao, [*Monotone Circuit Lower Bounds from Spread Matchings*, ECCC TR26-129 rev. 5](https://eccc.weizmann.ac.il/report/2026/129/revision/5/download), Theorem 8 and Section 4.
- C-275: `research/C275_SPARSE_SUPPORT_INTERPOLATION_STRENGTHENS_MAP_OBSTRUCTION_2026-09-27.md`.
- C-125/C-266: `research/DAG_FUSION_BRIDGE_2026-09-26.md` and `research/C266_CYCLIC_MATCHING_LOWEXT_AND_SYNCHRONIZATION_AUDIT_2026-09-27.md`.
