# C-361 - Output-index serialization does not transfer the Multi-MCSP gap

Date: 29 September 2026  
Route: test whether the NP-hard multi-output circuit-minimization reduction can be serialized into one explicit truth table and then used on the actual single-output Gap-MCSP promise.  
Classification: **EXACT ENCODING LEMMA; THIS PAPER'S REDUCTION DOES NOT SUPPLY THE REQUIRED SINGLE-OUTPUT GAP.**

## 1. The serialization itself is length-preserving

Let `F : {0,1}^a -> {0,1}^b`, with component functions `F_1,...,F_b`. Pad `b` to `b'=2^ceil(log b)` by adding zero components and define

```text
h(x,i) = F_i(x),    x in {0,1}^a, i in {0,1}^{log b'}.
```

The truth-table length of `h` is `b' 2^a`, within a factor two of the concatenated multi-output truth-table length `b 2^a`. In particular, the naive concern that adding `log b` index bits causes an exponential blow-up is mistaken: the new domain has exactly one slice per old output.

The circuit-size comparison is asymmetric. For fan-in-two circuits,

```text
CC(h) <= CC(F) + O(b),
CC(F) <= b * CC(h) + O(b log b).
```

The first inequality computes `F` once and adds a binary multiplexer over its output wires. The second fixes the index to each of its `b` values and takes `b` copies of the resulting circuit; fixed constants contribute at most the displayed convention-dependent additive term. Thus a multi-output YES instance of size `A` gives a scalar circuit of size `A+O(b)`, but a scalar circuit of size `s` only gives the generic multi-output upper bound `O(bs)`.

Consequently, this wrapper transfers a source YES/NO pair `(A,B)` to a target gap `(s1,s2)` only if the source NO lower bound is strong enough to force `B > b*s2` (up to additive encoding terms), while `A+O(b) <= s1`. The published result does not give such a gap.

## 2. What the Ilango-Loff-Oliveira reduction actually controls

The paper constructs a random truth table `T` of length `m0 = Theta(nu^3)` on `log m0` inputs, and an auxiliary multi-output function `g` formed by concatenating the evaluation functions of canonical DNFs for set windows. It proves `CC(g)=k`, where `k` is the number of distinct non-input components of `g`, and studies the *increment*

```text
Delta = CC(T • g) - k.
```

Their bounds relate `Delta` to set-cover number (in the paper, `cover/4 - 4 <= Delta <= cover` with high probability). The decision query is at the total-size threshold `k+ell`. This is an additive increment above a shared baseline, not a multiplicative gap for `CC(T • g)` itself. In fact, with high probability one nonempty set window has `Theta(m0/nu)=Theta(nu^2)` one-input minterms in its canonical DNF, so `k=Omega(nu^2)`, whereas a feasible cover uses at most `nu` sets and hence `Delta<=nu`. The total YES/NO sizes therefore differ only by an `O(1/nu)` relative amount at this scale. This is far short of the OPS Gap-MCSP ratio `s2/s1 = Theta(log N)`.

The mult-output-to-scalar inequalities lose another factor equal to the number of output slices. No theorem in the reduction controls that loss. The exact formal gap of Multi-MCSP is an optimization/additive-above-baseline statement; it must not be silently substituted for the multiplicative single-output promise.

## 3. A direct small-beta obstruction for the paper's fixed parameters

There is an even earlier failure for the direct serialization of the paper's construction. The index `i=0` slice of `h` is `T`, so restriction gives

```text
CC(h) >= CC(T) = Omega(m0/log m0)
```

with high probability over `T`, by the standard circuit-counting bound for a random truth table. The number `b` of output components in `T • g` is at most `O(|S| m0 log m0)`. For fixed set-size bound `r`, the family of distinct `r`-bounded sets has `|S|=O(nu^r)`, hence

```text
N = b*m0 <= O(nu^r * m0^2 * log m0)
  = nu^(r+6) * polylog(nu).
```

For every fixed `beta < 3/(r+6)`, `CC(h) > N^beta` for all sufficiently large `nu`. Thus these serialized outputs are already on the Gap-MCSP NO side even when the source set-cover instance is a YES instance. This closes the straightforward serialization for the fixed-`r`, `m0=Theta(nu^3)` reduction at the small-beta regime required by magnification.

Changing polynomial exponents can move this particular exponent comparison, so this is not an impossibility theorem for every possible multi-output reduction. It only establishes that the published construction, serialized in the direct way above, is not the needed single-output reduction.

## 4. Variants tested

* **Add repeated/padded output slices.** This increases the explicit table length and the target thresholds but does not amplify `Delta` or remove the output-index cofactor loss. Padding alone supplies no low/high separation.
* **Use the mult-output NO threshold as a scalar lower bound.** Invalid without a reverse theorem: low `CC(h)` gives only `CC(F)<=b*CC(h)`, not `CC(F)<=CC(h)+o(CC(F))`.
* **Ignore the shared baseline `k`.** Invalid because the source decision is about `CC(T • g)-CC(g)`. The target asks for an absolute threshold on one function.

## 5. What a surviving variant would have to prove

A useful successor would need a single-output encoding that simultaneously:

1. absorbs or cancels the shared baseline `k` without making the truth table superpolynomial;
2. keeps the source low case at `CC(h)<=N^beta/(c log N)`;
3. forces the source high case to `CC(h)>N^beta` despite the output-index cofactor loss; and
4. works for arbitrarily small fixed `beta` with the OPS constants.

That is a substantive new reduction, not a routine serialization of Multi-MCSP. Unless such a construction appears, do not continue this literature branch. Resume the frozen C-319 objective directly: prove a state-sensitive synchronization theorem on the actual promise or construct a full-promise `N^(1+o(1))` cover. No output-index rectangle, representation-count, or generic circuit-selector lemma is promoted to a q bound.

## 6. Five-question checkpoint

1. **Did the actual native lower bound improve beyond `N-o(N)`?** No.
2. **Was a valid near-linear full-promise cover constructed?** No.
3. **Was a state-sensitive theorem proved for the exact C-319 game?** No.
4. **Was a positive CohEnc transfer constructed?** No.
5. **Was a general reconstruction-to-decision compiler proved?** No.

This is a route audit, not a P-vs-NP result. The actual native lower bound remains `rho_GapMCSP >= N-o(N)`.

## Primary source

Rahul Ilango, Bruno Loff, and Igor C. Oliveira, [*NP-Hardness of Circuit Minimization for Multi-Output Functions*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2020.22), CCC 2020, especially Sections 4.1-4.2.
