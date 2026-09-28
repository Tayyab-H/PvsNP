# C-286 - Shared-DAG Rao approximation gives the needed directional polarity theorem

Date: 28 September 2026  
Classification: **GLOBAL-STRUCTURAL / ROUTE-TEST.**  
Numbering note: C-282 is already attached to the withdrawn bottom-NO collision argument, corrected by C-283. This result uses the next unused claim number; C-282 is preserved.

## 1. Correct statement

Let `Phi` be a monotone multi-output DAG with `a` distinct fan-in-two AND nodes. Outputs may be any number of signed table rails and may reuse arbitrary internal gates. Fix Rao's matching YES/NO distributions and parameters `t,epsilon`.

Rao's construction does **not** prove the literal two-sided claims `Pr_X1[tilde(Phi)!=Phi]<=a*2^(-t)` and `Pr_X0[tilde(Phi)!=Phi]<=a*4^t*epsilon`. It bounds only these directional errors at an AND node `g`:

```text
N_g^1 = {x in X1: g(x)=1, tilde(g)(x)=0},   Pr[N_g^1] <= 2^(-t),
N_g^0 = {x in X0: g(x)=0, tilde(g)(x)=1},   Pr[N_g^0] <= 4^t*epsilon.
```

These are exactly the directions C-125 needs. No opposite-disagreement bound follows from Rao's proof.

## 2. Multi-output accounting on a shared DAG

Give each distinct node one matching-family approximator. An input edge is its singleton term; constants use the empty family or empty matching. At a free OR node, take the union of child families. At an AND node, use Rao's truncation construction on compatible pairwise term unions. Every output is a matching-DNF with terms of size at most `t`.

For an output root `r`, monotonicity gives

```text
{X1: Phi_r=1, tilde(Phi_r)=0} subseteq union_{g AND ancestor of r} N_g^1,
{X0: Phi_r=0, tilde(Phi_r)=1} subseteq union_{g AND ancestor of r} N_g^0.
```

At OR, a missed true output has a missed true child; a false positive on a zero output has a false-positive child. At AND, either a child already has the relevant error or Rao's new error occurs. Induction proves both inclusions. Taking the union over every root yields

```text
Pr_X1[exists rail r: Phi_r=1 and tilde(Phi_r)=0] <= a*2^(-t) = delta1,
Pr_X0[exists rail r: Phi_r=0 and tilde(Phi_r)=1] <= a*4^t*epsilon = delta0.
```

There is no `2N` factor. A shared AND node is charged once however many outputs reuse it. OR flattening adds no error event, and fan-out creates no new node. Thus the requested full-equality approximation is not established, but its required directional replacement is.

## 3. Matching amplification threshold

Let the source have `v` vertices, `k=v/2`, YES distribution `X1` uniform over perfect matchings, and `X0=G(W)` for a uniform `h=v/4` vertex set `W`. Put `gamma=h/v=1/4`. Rao's spread bound gives `R=v^2/(8k)=v/4` for matching terms of size at most `k/2`.

For a rail DNF firing on a `p` fraction of `X1`, choose one deterministic contained term `Z(X1)` on each firing input. For any matching `m` of size `s>=1`,

```text
Pr[m subseteq Z | rail fires] <= Pr[m subseteq X1]/p <= R^(-s)/p <= (pR)^(-s).
```

So the conditional certificate distribution is `pR`-spread. Rao's lemma says it hits `X0` with probability at least `1-xi` if

```text
pR >= alpha_M*(t+log2(1/xi))/gamma^2.
```

The exact sufficient threshold is

```text
theta_M = alpha_M*(t+log2(1/xi))/(gamma^2*R)
        = 64*alpha_M*(t+log2(1/xi))/v.
```

An empty certificate fires always and is an immediate special case. Thus `p>=theta_M` implies `Pr_X0[tilde(rail)=1]>=1-xi`.

## 4. Polarity concentration

Write `p_jb=Pr_X1[tilde(phi_{j,b})=1]`. On an exact NO input, `Phi(X0)<=e(z)` prevents both polarities at one coordinate. If both approximated polarities had YES density at least `theta_M`, amplification and a union bound would make both fire on `X0` with probability at least `1-2xi`. On the good directional NO event `tilde(Phi)<=Phi`, this is impossible. Hence

```text
min(p_j0,p_j1) < theta_M, provided delta0 < 1-2*xi.
```

Each exact YES input has a low witness `w_X` with `e(w_X)<=Phi(X1)`. Except on the directional YES error event, `Phi(X1)<=tilde(Phi(X1))`; therefore

```text
p_j0+p_j1 >= 1-delta1.
```

If `2*theta_M+delta1<1`, each coordinate has a unique dominant bit `b*_j` satisfying

```text
p_{j,b*_j} > 1-delta1-theta_M >= theta_M.
```

This is global across the `N` coordinates: it uses one simultaneous directional event, not `N` separately charged rail errors.

## 5. Canonical table and complete contradiction

Set `w*_j=b*_j`. Choose one low witness `w_X` for each YES input. If `w_X[j]!=w*_j`, its minority rail is true in `Phi(X1)` and, on the good directional YES event, also in `tilde(Phi(X1))`. Therefore

```text
E[d_H(w_X,w*)] <= N*(theta_M+delta1).
```

Some witness is within `r=ceil(N*(theta_M+delta1))` of `w*`. C-275 gives absolute constants `A,B` with

```text
CC(w*) <= s1 + A*r*n/log2(r+1) + B*n,
```

where the `r=0` case is covered by the `B*n` term. Thus the table is low if

```text
s1 + A*r*n/log2(r+1) + B*n <= s2.                 (P)
```

Each dominant approximated rail fires on `X0` with probability at least `1-xi`. The simultaneous good directional NO event `tilde(Phi)<=Phi` then puts all `N` dominant rails in `Phi(X0)` with positive probability whenever

```text
N*xi + delta0 < 1.                                  (N)
```

For such an exact NO input, `e(w*)<=Phi(X0)<=e(z)` for a high table `z`. One-hotness forces `w*=z`, contradicting (P). So no C-125 encoder exists whenever (P), `2*theta_M+delta1<1`, `delta0<1-2*xi`, and (N) hold. This completes the canonical-table contradiction rather than stopping at an almost-fixed table.

## 6. Matching source selection criterion

Take `xi=1/(8N)`. Then

```text
theta_M = 64*alpha_M*(t+log2(8N))/v.
```

In Rao's regime, `u=h/sqrt(k)=sqrt(v)/(2*sqrt(2))`, `t=eta_M^2*u`, and `epsilon=exp(-eta_M*u)`. Hence

```text
theta_M = Theta(1/sqrt(v)) + O(log N/v).
```

For `v=A(log N)^2`, `N*theta_M=Theta(N/log N)`, much larger than C-275's patchable radius `Theta_beta(s2)=Theta_beta(N^beta)` for every fixed `beta<1`. More generally patchability requires, up to source/interpolation constants,

```text
v >= Omega_beta(N^(2*(1-beta))).
```

The direct matching-indicator YES table costs `O(v*log N/log v)` and fits `s1=N^beta/(c0 log N)` only for `v` at most about `N^beta` up to constants. These conditions are incompatible for every sufficiently small fixed `beta` (in particular `beta<2/3`). Retire the **polylogarithmic matching source plus direct matching-indicator witness** as the main LowExt route. This does not rule out all possible matching encoders using a different witness family. At very large `v`, the canonical argument rules out polynomial-cost maps, but a cost between its error threshold and the cyclic source lower bound is not excluded absent a constant comparison.

## 7. Status

C-286 proves a shared-DAG, multi-output, **directional** Rao approximation and completes its polarity-to-canonical-table consequence. The full two-sided inequality is not established; the exact correction is that its directional replacement is sufficient and has no output-multiplicity loss. Matching fails the desired small-`beta` source-selection criterion for direct witness coding. The actual Gap-MCSP bound remains `q=N-o(N)`; no map, superlinear `q` bound, or P-vs-NP proof is obtained.

Primary source: Rao, [*Monotone Circuit Lower Bounds from Spread Matchings*, ECCC TR26-129 rev. 5](https://eccc.weizmann.ac.il/report/2026/129/revision/5/download), especially Lemma 5, equations (6)-(7), and the gatewise approximation in Section 3.1.
