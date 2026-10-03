# C-471 — thresholded Fourier support rank cannot give the OPS separator

**Status:** a proved obstruction to one concrete global-spectral mechanism. The exact low-dimensional-linear-junta recognizer is near-linear; every threshold that robustifies it enough for the forced Low neighborhood either rejects a forced-YES table or accepts a genuinely High table. This is not a lower bound for arbitrary separators.

## 1. Targeted mechanism

Represent an n-input truth table `T` by the sign function `chi_T(x)=(-1)^{T(x)}` and its unnormalized Walsh transform

```text
W_T(u) = sum_{x in {0,1}^n} chi_T(x) * (-1)^(u dot x).
```

If `T(x)=g(Ax)` for a linear map `A:F_2^n -> F_2^m`, then the Walsh support lies in the row space `W=row(A)`, so its linear span has dimension at most m. Conversely, support contained in an m-dimensional subspace implies invariance under that subspace's orthogonal complement, hence dependence on at most m linear forms. This makes support-span rank an exact recognizer for linear juntas.

Choose even `m` so `2^m` is a sufficiently small constant fraction of `s1`. Since `mn=o(s1)` for fixed beta, every function depending on at most m linear forms has an n-input circuit of size at most `s1/4`: compute the m parities and use a mux tree for the arbitrary m-variable truth table. Thus a valid OPS separator must accept the radius

```text
r = floor(a*s1/n) = Theta(N^beta/n^2)
```

around every such function, for sufficiently small constant `a>0`, by address patching.

For an integer threshold `lambda>=0`, define the proposed predicate

```text
P_lambda(T)=1 iff dim span{u : |W_T(u)| > lambda} <= m.
```

## 2. The predicate has a small ordinary circuit

The Walsh transform is computed by n butterfly stages. There are `O(Nn)` additions/subtractions of signed integers with `O(n)` bits, giving `O(Nn^2)` fan-in-two Boolean gates. Marking coefficients above the fixed threshold and forming the corresponding `N x n` binary matrix takes `O(Nn)` further gates. Standard Gaussian elimination with conditional row selection computes its rank in `O(Nn^3)` gates. Thus `P_lambda` has an ordinary AND/OR/NOT circuit of size `O(Nn^3)=N polylog N`, with arithmetic, comparisons, and rank computation all charged. This is below `N^(1+epsilon)` for every fixed `epsilon>0` and sufficiently large N.

At `lambda=0`, this recognizes the exact linear-junta class. The class contains `2^{Theta(s1)}` distinct truth tables and consists entirely of Low tables, but is not the full Low class.

## 3. No threshold handles both robustness and soundness

Fix a dimension-m subspace W and an m-variable bent function `g` (m is even); put `T0(x)=g(Ax)` with row space W. Its unnormalized Walsh coefficient has magnitude `N/2^(m/2)` at every frequency in W and is zero outside W. Since `m=O(n)` and `r=N^beta/poly(n)` with `beta<1/2`, these nonzero coefficients are much larger than `2r`.

### Case A: `lambda < 2r` — a forced Low input is rejected

Choose any `u notin W`. Because `T0` is constant on each fiber of A and u is not in its row space, exactly half the addresses have `chi_T0(x)(-1)^(u dot x)=+1`. Flip `T0` on r such addresses. This is a radius-r perturbation, so its circuit complexity remains at most `s1`; every valid separator must accept it. Its Walsh coefficient at u has magnitude `2r>lambda`. The coefficients spanning W remain above lambda because their original magnitude is `N/2^(m/2)>>2r`. Consequently the large-coefficient frequencies span dimension at least `m+1`, and `P_lambda` rejects this forced-YES table.

### Case B: `lambda >= 2r` — a High input is accepted

Let

```text
t = floor(r^2/(C*n))
```

for a sufficiently large absolute constant C. For each `u notin W`, the N signs `chi_T0(x)(-1)^(u dot x)` are balanced, because the Walsh coefficient of T0 at u is zero. Choose a uniform t-subset E of addresses. Hoeffding's bound for sampling without replacement and a union bound over at most N frequencies show that, for sufficiently large C, at least half of all E satisfy

```text
|sum_{x in E} chi_T0(x)(-1)^(u dot x)| <= r   for every u notin W.
```

Let `T_E` be `T0` with its output flipped on E. Then `|W_{T_E}(u)|<=2r<=lambda` for every `u notin W`, so all frequencies counted by `P_lambda` lie inside W. Hence `P_lambda(T_E)=1`.

There are at least `0.5*binom(N,t)` such good sets. Since

```text
r = Theta(N^beta/n^2),
t = Theta(N^(2*beta)/n^5),
log2 binom(N,t) = Theta(N^(2*beta)/n^4),
```

and fixed `beta>0` gives `N^(2*beta)/n^4 >> N^beta*n`, the good perturbation family is larger than the number `2^{O(s2*log(n+s2))}=2^{O(N^beta*n)}` of tables computable by circuits of size at most `s2`. Thus at least one accepted `T_E` has `CC_n(T_E)>s2`. The predicate accepts a promised High input.

Together, these cases prove that no threshold lambda makes this support-span test both accept all forced radius-r Low perturbations and reject every OPS-High table.

## 4. Canaries and scope

- Parity and every function of at most m linear forms are recognized; coordinate block repetitions are included.
- The Low function `AND_{j=1}^{m+1} (a_j dot x)` for m+1 independent address parities has Fourier support spanning dimension m+1, so the exact rank test rejects it. Its circuit has only `O((m+1)n)` gates, illustrating the missing Low-completeness direction.
- The thresholded version repairs that kind of point perturbation only by admitting High perturbations with small Walsh tails, as the counting argument proves.

The failure is specific to thresholded Fourier-support span rank. Other spectral quantities, nonlinear invariants, and arbitrary DAG arguments are not ruled out. In particular, the proof does not say that every small separator has a Fourier description or uses this test.

The known hardness-magnification locality barrier concerns the extension of existing weak-model lower-bound methods to oracle-augmented circuits for magnification targets; C-471 is a specific failed spectral construction, not a new barrier or a consequence of that barrier. Primary reference: [Oliveira et al., ECCC TR19-168](https://eccc.weizmann.ac.il/report/2019/168/).

## 5. Paired full-promise construction and exact frontier

This predicate remains incomplete, and Case B proves it is unsound for every threshold that includes the required robust Low balls. Completing it by OR-ing exact membership tests for all size-s1 circuit tables returns to the known `O(N*2^(O(N^beta)))` enumerator. No near-linear full-promise separator or new lower bound follows.

The ordinary gate lower bound remains `N-O(N^beta log N)` with the C-406 additive logarithmic reconvergence refinement. The common-fixed-epsilon OPS target, native `rho_GapMCSP>=N-o(N)`, and P-vs-NP remain open.
