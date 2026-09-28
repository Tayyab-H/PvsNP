# C-312 - A one-input guard still yields a constant-factor decision compiler

Date: 28 September 2026  
Classification: **GENERAL DECODER LEMMA / GUARDED DUAL ROUTE BOUND.** Masking universal dual-consensus rails by one source input avoids C-311's global fixed-pair decoder, but the two input cofactors recover exact source decision at at most twice the map's AND cost.

## 1. Abstract statement

Let `f:{0,1}^m -> {0,1}` be monotone, and let `Phi` be a C-125 map with `a` binary AND gates and `2N` one-hot rails. Suppose there is an input coordinate r and a fixed output coordinate j such that:

1. on the slice `x_r=0`, every NO input has `Phi(x)=0`;
2. on the slice `x_r=1`, both rails `Phi_(j,0)` and `Phi_(j,1)` are 1 on every YES input.

Then an exact monotone circuit for f has at most `2a+2` AND gates.

## 2. Proof by monotone Shannon decomposition

Restrict the map circuit to `x_r=0`. Constant substitution cannot increase its AND count. The free OR of all `2N` outputs computes the cofactor `f_0`: on a NO input in this slice all outputs vanish; on a YES input a complete one-hot low code is below `Phi`, so at least one output is 1. Hence `CycAnd(f_0)<=a`.

Restrict the map circuit to `x_r=1`. The conjunction

```text
g_1 = Phi_(j,0) AND Phi_(j,1)
```

rejects every NO input by the C-125 one-hot high-completion condition and accepts every YES input by assumption 2. It computes `f_1` with at most `a+1` AND gates.

Since f is monotone, `f_0 <= f_1` pointwise and

```text
f(x) = f_0(x without r) OR (x_r AND f_1(x without r)).
```

This circuit uses at most `a+(a+1)+1=2a+2` AND gates. Thus `CycAnd(f)<=2a+2`.

## 3. Application to a guarded dual-consensus proposal

Let `P_(j,b)` be monotone primal-solution rails that vanish on NO inputs and contain a low one-hot table on every YES input. Let `U_(j,b)` be the universal dual-consensus rails from C-311: they are monotone, both polarities are active on YES, and any NO output is compatible with a high dual code. For a fixed source variable x_r define

```text
Phi_(j,b) = P_(j,b) OR (x_r AND U_(j,b)).
```

This map is monotone. YES inputs are covered by P; NO inputs with `x_r=0` map to zero, and NO inputs with `x_r=1` are bounded by a high dual code. It avoids C-311's global saturation because some YES inputs can have `x_r=0`.

But it meets the two hypotheses above exactly. Therefore

```text
CycAnd(f) <= 2*AND(Phi)+2.
```

The guard removes the one-gate exact decoder but cannot make reconstruction exponentially cheaper than decision. This is a construction-class bound, not a general theorem about all C-125 maps.

## 4. What remains open

The factor-two bound still leaves a possible constant-factor transfer: if a map with cost close to half the source decision cost exists, composition could retain a large lower bound. No such guarded map is known. For ODDFACTOR, the obvious primal rails are costly because their OR already decides odd-factor existence; the guarded dual half does not currently reduce that cost.

More generally, a guard depending on several source variables may require a larger cofactor decomposition. A useful next theorem would quantify the decision cost by the number/structure of guard cofactors and identify whether any low-description guard allows a genuine `CohEnc << CycAnd` gap. The actual OPS fusion bound remains `q=N-o(N)`.

## 5. r-bit version

Let R be a set of r guard variables. Suppose every exact restriction `f_A(y)=f(x_R=1_A,y)` has a monotone source circuit of at most `a+1` AND gates obtained from the restricted map (for example, by an output OR or one output-pair AND). For any input whose guard bits have support T, monotonicity gives the exact identity

```text
f(x_R,y) = OR over A subseteq R of
           [(AND over i in A of x_i) AND f_A(y)].
```

If a term fires, then `A subseteq T`, so monotonicity implies `f_A(y)<=f_T(y)=f(x_R,y)`. Conversely, when `f(x_R,y)=1`, the term `A=T` fires. Compiling the identity gives

```text
CycAnd(f) <= 2^r*(a+1) + r*2^(r-1).
```

When the empty-guard cofactor has the bottom-NO/output-OR decoder, its cost is at most a rather than `a+1`, saving one gate. This extension is useful only when the decoder condition is proved for every guard cofactor; it is not a theorem for arbitrary maps. Fixed r gives a constant-factor reconstruction/decision bound. Growing r leaves an exponential guard-cover loss, which reconnects to the unresolved global-selector problem in O-168.

## 6. ODDFACTOR remains hard after deleting the guard edge

Fix a forbidden edge `e=(l*,r*)` in the `x_e=0` cofactor of `ODDFACTOR_v`. Choose four left and four right vertices including `l*` and `r*`. Make `l*` and `r*` leaves in two opposite stars `K_(1,3)` and `K_(3,1)`, so e is not used. Put an arbitrary `ODDFACTOR_(v-4)` instance on the remaining vertices and set every cross-block edge to zero. The fixed star forest has odd degree at every vertex, and the blocks are disconnected, so the resulting graph has an odd factor exactly when the smaller instance does. This is a monotone projection inside the `x_e=0` slice.

Consequently, the output-OR decoder on that slice, and hence any guarded map satisfying the lemma, must have

```text
a >= A_ac(ODDFACTOR_(v-4)) = 2^((v-4)^Omega(1)),
```

using the known ordinary monotone-circuit lower bound for ODDFACTOR. The guarded map's zero-decoy branch remains source-hard at the same superpolynomial scale. This still does not compare `a` with the full `CycAnd(ODDFACTOR_v)` by a sharp additive margin, so it is not a transfer result. See C-291 for the source lower bound and its parameterization.

The source lower bound used here is the odd-factor consequence of Cavalar et al.'s matching/odd-cut approximation theorem: [*Monotone Circuit Complexity of Matching*](https://eccc.weizmann.ac.il/report/2025/102/revision/1/download).
