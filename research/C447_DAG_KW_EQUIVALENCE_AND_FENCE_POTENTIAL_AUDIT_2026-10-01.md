# C-447 — Rechecking DAG-KW and auditing a fence-potential transfer

**Date:** 1 October 2026
**Frontier:** unchanged. Correction after repository audit: the DAG-game/circuit correspondence and its AND/OR/copy rectangle induction were already recorded in C-159 and C-232. C-447 rechecks that result against C-446; it is not a new model or theorem. The cycle's target-specific work is the fence-transfer check on complement-closed endpoint cores and a failed fixed-projection construction.

## 1. Known DAG-game characterization, rechecked on the OPS promise

Put `U=L_s1` and `V=H={y:CC(y)>s2}`. A Boolean DAG game for `Bit_{U,V}` has a root state valid on every pair in `U×V`; each state `v` is valid on a rectangle `R_v=X_v×Y_v`; every valid pair at a nonterminal state is valid at at least one child, so `R_v⊆R_a∪R_b`; and every terminal state is labelled by a coordinate `i` on which all pairs in its rectangle differ.

Every separator circuit with `S` gates induces such a game with `O(S+N)` states: use two oriented states per gate (the endpoint values are `1,0` or `0,1`) and at most two terminal orientations per table coordinate. Shared gates remain shared states.

Conversely, any such game with `K` states yields a total Boolean circuit of `O(K)` gates that is `1` on `U` and `0` on `V`. Here is the partial-function extension argument. At a terminal rectangle, all pairs differ in one coordinate in a single orientation, so the corresponding literal separates its two sides. Inductively, suppose a state rectangle `X×Y` is covered by child rectangles `X_0×Y_0` and `X_1×Y_1`. The rectangle-cover condition implies one of: `X⊆X_0∩X_1`, `Y⊆Y_0∩Y_1`, or the parent rectangle is contained in one child. Use AND in the first case, OR in the second, and reuse the child circuit in the third. This constructs a separating Boolean function at the root; its values off `U∪V` are unconstrained, exactly as the promise allows.

Thus, up to constant/additive-linear overhead for literal terminals, lower-bounding this DAG game for `(L_s1,H)` is equivalent to lower-bounding ordinary separator circuits. This is a faithful language for sharing, but not a new computational model or an independent source of hardness. C-159 already recorded the AND/OR/copy rectangle trichotomy; C-232 recorded the promise-specific circuit/rect-DAG equivalence and its limits. Sokolov's Theorem 3.2 supplies the published DAG-game/circuit correspondence; the short induction here checks its partial-promise form, where values on the middle band are free. [Sokolov, ECCC TR16-202](https://eccc.weizmann.ac.il/report/2016/202/), especially Theorem 3.2.

## 2. Candidate A: rectangle area does not charge shared states

For `R_v=X_v×Y_v`, define `A(v)=|X_v||Y_v|`. The validity condition gives

```text
A(v) ≤ A(a)+A(b).
```

This is useful on trees: recursively expanding it charges the root area to terminal rectangles. On a DAG, expansion counts a shared child once per incoming path, not once per state. The resulting bound is on a path-unfolding, not on the number of paid gates/states. Unrestricted fan-out is exactly where this potential loses the relevant measure.

Counting only terminal labels cannot repair it. There are `2N` canonical coordinate-orientation rectangles
`{x∈U:x_i=b} × {y∈V:y_i=1-b}` covering `U×V`. Hence any argument that uses only the fact that every pair has a differing coordinate has at most a linear terminal-certificate budget. This cover is **not** a valid `O(N)` DAG game by itself: arbitrary unions of coordinate rectangles need not be rectangles, so it omits the internal-state condition. This distinction rules out both overclaiming an easy separator and using a bare pair-cover count as a superlinear lower bound.

## 3. Candidate B: fixed-low fences give only logarithmic game depth

For a state rectangle `X_v×Y_v` and `x∈X_v`, define its fence width

```text
w_v(x) = min{|I| : every y∈Y_v differs from x on some coordinate i∈I}.
```

At the root, a fence `I` fixes `x` on `I`; all `2^(N-|I|)` completions then avoid `H` and so lie in `L_s2`. Circuit counting gives `|L_s2|≤2^{O(N^β n)}`, hence

```text
w_root(x) ≥ N-O(N^β n).
```

At any nonempty terminal rectangle, one differing coordinate is a fence, so `w_leaf(x)=1`. For a two-child state, the rectangle-cover condition implies, for each fixed `x`, either the parent high-side is contained in one child's high-side or it is covered by the union of both child high-sides. Therefore

```text
w_v(x) ≤ w_a(x)+w_b(x).
```

If the game has depth `d`, induction from the leaves gives `w_root(x)≤2^d`, so `d=Ω(log N)`. This is a valid potential calculation but does not improve the existing `S≥N-O(N^β n)` gate bound; it also cannot reach a superlinear **size** bound. The logarithmic scale is already met by balanced parity circuits: parity of N bits has fan-in-two size `O(N)` and depth `O(log N)`. A universal path-depth lower bound for all valid extensions is capped at `N`: the exact separator can be implemented by a depth-`N` decision tree (with exponential size). Separately, the pair relation itself has an `N+O(log N)`-bit protocol by sending one table and returning a differing coordinate; those communication bits do not count DAG states. Retire fence width and path length as standalone OPS mechanisms. Sokolov's published fence argument proves lower bounds for a specially structured **monotone** BMS relation; its monotone hypotheses and combinatorial fence-capacity lemma do not establish the required capacity bound for arbitrary nonmonotone GapMCSP states. The direct rare-literal step and its distribution-specific hypothesis are visible in the BMS proof, Section 5, especially Lemma 5.2: [Sokolov, ECCC TR16-202](https://eccc.weizmann.ac.il/report/2016/202/).

## 4. Shared-computation canaries

The listed structured readouts remain counterexamples to local-load charges only: parity of `N` table bits has an `O(N)` circuit; repeated-block equality has an `O(N)` circuit; `O(N)` total-incidence parity checks can be evaluated and combined with `O(N)` gates; and simple global block relations such as repeated parity summaries have linear circuits. By the DAG-game equivalence these restricted functions also have linear-size state DAGs. These constructions do not classify the full pair relation `L_s1×H` and therefore do not refute the GapMCSP lower-bound programme.

## 5. Full-promise construction attempt: fixed projections fail

I tested a compact sample-signature separator. Fix any `q` table coordinates and one `g∈L_s1`. There are `2^(N-q)` tables agreeing with `g` on those coordinates. If `2^(N-q)>|L_s2|`, at least one such table lies in `H`. A decision based only on those `q` coordinates therefore cannot accept every Low table and reject every High table. Since `log|L_s2|=O(N^β n)`, every fixed-projection separator needs `q≥N-O(N^β n)` coordinates. This recovers the support/cylinder limitation; it is not a new circuit lower bound and does not rule out a near-linear circuit that uses all coordinates jointly.

The explicit exact baseline remains enumeration of all descriptions of size at most `s1`, comparing each generated table against the complete input, at cost `O(N·2^{O(N^β)})` (absorbing description factors into the exponent). No near-linear full-promise separator was found.

## 6. A symmetry-normalized core blocks the direct rare-literal fence transfer

The key step in Sokolov's monotone BMS fence proof is not just that fences shrink: its capacity argument uses a family property that each edge literal occurs in fewer than a `1/m` fraction of minimal-good graphs. A short disjunction then covers fewer than a `k/m` fraction of that family, forcing many endpoints to be assigned to states. This incidence estimate is specific to the chosen graph families.

For GapMCSP there is a useful exact core on which no table coordinate is rare. Write `t1=floor(s1)` and `t2=floor(s2)` (circuit sizes are integers), and let

```text
U* = L_{t1-1} ∪ {¬f : f∈L_{t1-1}}
V* = {g : CC(g)>t2+1 and CC(¬g)>t2+1}.
```

Complement costs at most one NOT gate, so `U*⊆L_s1`; `V*⊆H`. Both are closed under complement. Also `|V*|≥2^N-2|L_{t2+1}|=2^N-2^{o(N)}` for fixed `β<1`. Uniform distributions on either complement-closed family give each table coordinate exactly marginal `1/2`. Thus the BMS proof's rare-positive-literal union bound cannot be transferred to these natural Low/High cores: neither polarity has small marginal. This refutes the **direct rare-edge adaptation**, not every possible nonmonotone fence-capacity theorem. The source fence argument and its BMS counting step are in [Sokolov, ECCC TR16-202](https://eccc.weizmann.ac.il/report/2016/202/).

Any separator `F` for the original promise yields

```text
F*(x) = F(x) ∧ F(¬x)
```

of size at most `2S(F)+N+1`, which is complement-invariant and separates `U*` from `V*`. The additive and constant-factor costs preserve any fixed polynomial exponent after a small exponent slack. This is a valid normal form for future analysis, but parity, repeated-block equality, and complement-invariant global relations still have linear or near-linear circuits; symmetry alone supplies no superlinear charge.

## 7. Research decision and quantitative effect

Do not continue treating the gate-path/DAG-KW translation itself as novel; C-159/C-232 already contain it. The direct Sokolov fence transfer is also retired: its rare-literal capacity step fails on complement-balanced endpoints. C-160 separately shows that generic class-count, local-richness, patch-stability, and Boolean-recombination statistics plus the local trichotomy can coexist with an `O(N log N)` separator on a different promise. These facts rule out the current generic charges, not an OPS-specific theorem. Do not replace the missing lower bound by an assumed “joint state-capacity” axiom. At the user's direction, the next cycle is an integrated first-principles audit of the recorded attempts; it must identify a distinct, explicit mechanism before a new proof branch is selected.

**Frontier unchanged:** ordinary separator lower bound `S≥N-O(N^β log N)-1`, with only the known logarithmic surplus; OPS common-`ε` target remains open; exact full-promise upper remains `O(N·2^{O(N^β)})`; native `ρ≥N-o(N)` remains a separate measure. No proof of `P≠NP` or `P=NP` has been obtained.
