# C-336 — Multiple-hole splice products impose a block-coherence constraint

Date: 29 September 2026  
Route: O-167 / test whether C-281 reuse can expose independent block choices in one accepting context.  
Classification: **PRIMARY-ROUTE INTERMEDIATE; NO q IMPROVEMENT.**

## 1. Multiple-hole substitution

Represent a finite accepting derivation by its signed seed support. A context is such a derivation with one or more state occurrences cut out and replaced by labeled holes. The hole at position `a` is labeled by its required state `i_a`.

**Lemma.** Let `K` be an output context with holes labeled `i_1,...,i_h`. For each `a`, let `P_a` be any finite proof rooted at `i_a`. If

```text
S = K union P_1 union ... union P_h
```

is consistent, then `S` is an accepting output support. Consequently every full truth table extending `S` is accepted by the same q-pair system. For a sound Gap-MCSP separator,

```text
Cube(S) subseteq SIZE(s2).
```

**Proof.** Substitute the proof trees into all their designated holes. The resulting finite derivation has support `S`. Any full table extending `S` makes every selected seed literal true, so induction up the finite derivation activates its root. Soundness rejects every table of circuit complexity greater than `s2`, proving the cylinder inclusion.

This is the simultaneous version of C-281's context/proof law. It applies to distinct hole states as well as repeated occurrences of one state. Compatibility is essential: an inconsistent union has no truth-table completion and gives no constraint.

## 2. A forbidden product at the OPS block scale

Write `n=log2 N`, `s2=N^beta`, and `s1=N^beta/(c0 n)`, for fixed `0<beta<1`. Partition addresses into `k=K n` prefix blocks, where `K` is a sufficiently large fixed constant. In each block choose a function supported on a fixed `u`-dimensional suffix subcube and arbitrary on that subcube. If `t=alpha*s1` for a fixed small `alpha>0`, Lupanov synthesis permits

```text
2^u = Theta(t log t),   u=(beta+o(1))n,
CC(f) <= t.
```

The table that places one such function in a designated block and is zero elsewhere has circuit size at most `t+O(n) <= s1`; the `O(n)` term tests all fixed address bits defining the subcube (it is only `O(log k)` if the subcube geometry has no additional fixed suffix bits). Choose `t` with constant slack below `s1`. Since `s1 >> n`, each block choice has a low-table anchor. There are `2^(2^u)` choices per block. The full independent product has logarithmic cardinality

```text
k*2^u = Theta(K*n*s1*log s1) = Theta(K*s2*log N).
```

Circuit counting gives `|SIZE(s2)| <= 2^(C*s2*log(s2+n))` for a basis-dependent constant `C`. Choosing `K` large enough makes the independent product larger than `SIZE(s2)`. Therefore at least one assembled table with independently chosen block functions is high.

It follows that no sound accepting context can expose `k=K log N` block-local replacement menus with all of these properties at once:

1. one replacement proof per block is available at a designated hole;
2. all choices from the block families are mutually compatible with the context and with one another;
3. the canonical completions reproduce the independent block tuple.

Otherwise multiple-hole substitution would make every tuple in a family larger than `SIZE(s2)` a low table, a contradiction. This is a genuine OPS-scale restriction on the **joint** reuse product, not just on one owner mask.

## 3. The missing q-charge

The lemma does not show that a q-state cover must expose such a context. A valid system may avoid the product because different block proofs use incompatible supports, a context fixes some would-be replacement coordinates, state choices across blocks are correlated through the common proof graph, or there is no common accepting context containing the relevant holes.

The parameter check confirms that a width-only argument cannot rule out the first two evasions. Each local choice varies on only `M=2^u=Theta(s1 log s1)=Theta(s2)` coordinates, so all `k` block choice coordinates total `kM=Theta(s2 log N)=o(N)` for fixed `beta<1`. A context or replacement support could pin those coordinates with fewer than N signed literals; the existing `2q` seed-clause budget at `q=Theta(N)` does not preclude it. Moreover `log |SIZE(s1)|=O(s1 log N)=O(s2)`, below the `2q=Theta(N)` policy-subset exponent. Thus neither low-table counting nor the number of possible policy regions charges these local pinning patterns. To obtain a q gain, one must show that the full game cannot realize the required pinning patterns coherently across every low circuit, or construct a state-priced global selector.

C-281 allows arbitrary semantic endpoints, so no current argument rules out these evasions from q alone. The missing theorem is now specific: prove that covering all low tables with fewer than `N g(N)` states either realizes a forbidden independent block product or pays for a global selector that itself costs `N g(N)` states. C-336 proves neither side of that dichotomy.

## 4. Hostile calibrations

- **C-257 parity:** compatible substitutions can stay inside the even-parity set. The lemma only forbids products whose tuple family exceeds the sound low class; it does not claim that all reuse creates a high hybrid.
- **C-258 repeated equality:** repeated-block choices are globally correlated by the equality fingerprint. It avoids the independent-menu hypothesis, consistent with its O(N) cover.
- **C-315 block count:** the parameter choice is compatible with `k=Theta(log N)`; the new point is choosing each single-block anchor below `s1`, then using a sufficiently large number of independent blocks to exceed the `SIZE(s2)` count.

## 5. Status

C-336 tightens O-167 to a multiple-hole product constraint and gives a concrete family of low replacement anchors. It does **not** prove that native proofs provide the needed holes, a superlinear q lower bound, a near-linear full-promise cover, or P-vs-NP. The actual bound remains `rho_GapMCSP=N-o(N)`. Continue only by proving the product-or-selector dichotomy from the exact q-state game or by constructing a valid cover.
