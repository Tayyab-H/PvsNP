# C-399 - Padding the direct finite hard-core list makes it easy for CircCons's NO class

Date: 29 September 2026  
Route: O-232 / test whether Xia's circuit-consistency promise removes the C-388 coNP verifier.  
Classification: **ROUTE NO-GO FOR THE DIRECT TABLE-DRIVEN, PADDED C-388 LIST ENCODING; SUCCINCT SAMPLERS REMAIN OPEN; NO CHANGE TO THE NATIVE STATE BOUND.**

## 1. CircCons promise relevant to the proposal

Xia's definition takes as input a size-`s` circuit sampling labeled examples `(X,Y)`, where `X` has domain `{0,1}^m`, subject to `m>sqrt(s)`. For a concept class `F`, a YES instance has error below `alpha` against `F`; a NO instance must have error greater than `beta` against the much larger class `SIZE(m^{log log m})`. Under `(1-2 alpha)^2 > 1-2 beta`, the cited theorem places this promise in `SZK^A` (not plain SZK). See [Xia, *New Perspectives on the Complexity of Computational Learning*](https://www.cs.princeton.edu/techreports/2009/866.pdf), Definition 3.4.1 and Theorem 4.3.7.

The tempting application was to use the C-388 hard-core list `Q` as the sampler's support and take `F=SIZE(T)`. The thresholds have a numerical gap, but that is not enough: the CircCons NO side requires hardness against `SIZE(m^{log log m})`, not just against `SIZE(T)`.

## 2. Finite-support interpolation lemma

Let a labeled distribution be supported on `K` distinct examples `(x_j,y_j)`, where `x_j in {0,1}^m` and labels are consistent whenever an address repeats. Then it has a zero-error predictor of size `O(Km+K)`:

```text
h(x) = OR_{j : y_j=1} [x = x_j].
```

Each equality test uses `O(m)` bounded-fan-in gates. If the same address appears with conflicting labels, discard the CircCons application: no deterministic concept can have zero error on all supported examples, whereas C-388's labels are always the single-valued labels `f(x)` and hence consistent.

For C-388, `K<=L=O(N^beta)`. Therefore every proposed sample has an exact predictor of size `O(Lm)`. The standard table-driven sampler hardwires the list and uses `O(Ln)` gates (plus `O(m)` if output-padding wires are charged). At the original address dimension `m=n=log N`, this upper bound is too large to certify `m>sqrt(s)` for that implementation. A specially structured Q might admit a smaller sampler, but C-346 does not provide one. If we pad the domain to dimension `m` large enough to meet the condition using the table-driven encoding's size bound, the same lookup predictor still fits the sample. For the natural polynomial padding `m=N^gamma` with `gamma>beta/2`,

```text
log(Lm) = O(log N),
log(m^(log log m)) = gamma*log N*Theta(log log N),
```

so `O(Lm) <= m^(log log m)` for all sufficiently large `N`. In fact, for this encoding any padding dimension above a sufficiently large constant times `sqrt(Ln)` already has `log m=Omega(log L)`, so `log(m^(log log m))=log m*log log m` eventually dominates `log(Lm)=log L+log m`. The padded list is consequently not a NO instance of CircCons: its error against the comparison class is zero. Increasing the padded domain only makes its NO-side circuit class larger.

More generally, the obstruction is exact: any empirical distribution on `K` consistently labeled points is perfectly fit by a circuit of size `O(Km)`. A finite sample can be hard against the C-388 predictor class `SIZE(T)` while being easy for the vastly larger CircCons comparison class.

## 3. Consequence for the proposed transfer

The relation `R(f,Q)` from C-388 remains coNP-verified: it asserts that no size-`T` circuit fits at least `0.741` of the listed examples. The CircCons theorem does not make this universal condition efficiently checkable for the direct list encoding padded to meet its sampler-size side condition, because its NO promise then cannot hold. A particularly structured Q with a much smaller sampler would need separate analysis; C-346 does not provide such a sampler. A different, succinct sampler for a genuinely large-support labeling relation is not ruled out. The theorem's `SZK^A` classification is also not itself a deterministic polynomial-time validity test or a short certificate for `R(f,Q)`. The constants satisfying Xia's gap inequality do not repair these gaps.

This closes only the proposed *direct finite empirical list -> padded CircCons* route. It does not rule out a different succinct sampler with large support and a genuinely hard labeling relation, and it gives no lower bound on the circuit size of `BAD`. Such a sampler would need an explicit, size-accounted mechanism for labels that cannot be memorized by `SIZE(m^{log log m})`.

## 4. Main-line checkpoint

The exact C-319 paired recurrence remains the primary state-count target. A shared state has no caller/address-history argument, as C-341 proves, but this local state-merging fact does not by itself force incompatible choices, a forbidden C-320 owner mask, or more than `N-o(N)` states. C-384 also shows that a chosen circuit's internal selector matrix is representation-dependent and can be bypassed by direct equality to its truth table. Thus the unresolved theorem is still a graph/readout statement about arbitrary valid endpoint lists, not a gate-by-address count for one selected circuit.

**Status:** native lower bound remains `q>=N-o(N)`; no full-promise `N^(1+o(1))` cover, selector, or P-vs-NP proof is obtained.
