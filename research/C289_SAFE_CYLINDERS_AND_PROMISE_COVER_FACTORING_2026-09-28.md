# C-289 - Crosswalk: safe-cylinder terms, C-230, and C-244

Date: 28 September 2026  
Classification: **SYNTHESIS / ELEMENTARY COROLLARY; NOT A NEW CORE THEOREM.**  
Scope: the full `SIZE(s1)` versus outside-`SIZE(s2)` promise, with medium tables unconstrained.

## 1. Correct promise object

Write `Y=SIZE(s1)`, `Z={z: CC(z)>s2}`, and `M=SIZE(s2) minus Y`. A promise separator is required to output 1 on `Y` and 0 on `Z`; its value on `M` is free. This is the active promise cover. The separate full-domain cover also rejects `M` and therefore computes exact membership in `Y`. The two must not be conflated.

Encode a table `w` by its one-hot dual-rail vector `e(w)`, with rails `x_(i,w_i)=1`. A consistent partial assignment `P` fixes a subset of coordinates to specified bits. Its cylinder is

```text
[P] = {w in {0,1}^N : w extends P}.
```

Call `P` **gap-safe** if `[P]` contains no high table, equivalently `[P] subseteq SIZE(s2)`. It may contain medium tables.

## 2. Safe-cylinder term lemma

Let `C` be any monotone dual-rail circuit whose output is 1 on `Y` and 0 on `Z`. Expand its positive computation into proof terms: at an OR choose one true input, at an AND retain both inputs, and continue to literals/constants. Ignore terms containing both rails of a coordinate, since they are false on every one-hot code. Every remaining term is a consistent partial assignment `P`.

**Lemma.** Every consistent proof term `P` of `C` is gap-safe, and these terms cover `Y`.

**Proof.** If a low table `y` is accepted, at least one proof term is true on `e(y)`; its partial assignment is therefore contained in `y`, so the terms cover `Y`. For any consistent term `P`, every one-hot code `e(z)` with `z in [P]` makes the same conjunction of rails true, hence makes `C` output 1. Since `C` rejects every `z in Z`, no such `z` lies in `[P]`. Therefore `[P] subseteq SIZE(s2)`. No claim is made about medium values. This proves the lemma.

This is a direct DNF expansion, not a new structural lemma. At the native cyclic level it is already encompassed by [C-244](C244_STATE_ZONE_FACTORISATION_AND_GLOBAL_READOUT_2026-09-27.md): the accepted set is the union of q state zones `P_i intersect K_i`, and each compatible proof/context support pair gives a sound cylinder.

Conversely, any family of gap-safe partial assignments covering `Y` gives a valid promise separator by ORing their literal conjunctions. This converse may use many AND gates; it is a semantic characterization, not a size bound.

For a cyclic fusion cover with `q` states, the associated least-fixed-point separator can be unrolled for at most `q` rounds into an acyclic dual-rail circuit with `O(q^2)` AND gates. Thus its accepting proof terms form a gap-safe cylinder cover. This conversion keeps the already-known quadratic loss; it does not identify `q` with the number of terms.

## 3. Exact dimension bounds for a safe cylinder

If `P` leaves `r` coordinates free, its cylinder contains `2^r` distinct tables, all in `SIZE(s2)`. For a fixed finite fan-in circuit basis, the number of Boolean functions on `n` inputs with circuit size at most `s` is at most

```text
|SIZE(s)| <= 2^(C s log2(s+n))
```

for an absolute basis-dependent constant `C`: encode a topological list of at most `s` gates by gate type and two predecessor indices. Therefore

```text
r <= log2 |SIZE(s2)| <= C s2 log2(s2+n) = O_beta(N^beta log N).
```

This is an upper bound on the number of free coordinates in **every** consistent proof term of a promise separator. It is weaker than the corresponding exact-low bound, which uses `SIZE(s1)`; that stronger bound is not valid for the active promise because a term may safely include medium tables.

The maximum-cylinder calculation below is [C-230](C230_HIGH_FREE_SUBCUBE_DIMENSION_CALIBRATION_2026-09-27.md), restated here to make the promise-term comparison explicit. Choose `k` so that

```text
k = floor(log2(s2) + log2(log2(s2)) - log2(8*C_L)),
```

where `C_L` is a constant for Lupanov's bound: every Boolean function `h` on `k` bits has a fan-in-two circuit of size at most `C_L*2^k/k`. Fix a prefix `a` of length `n-k`; leave the `2^k` truth-table positions with that prefix free and fix every other table bit to zero. Every completion is

```text
g_h(x) = [x_(1..n-k)=a] AND h(x_(n-k+1..n)).
```

It has circuit size at most `C_L*2^k/k + O(n) <= s2` for sufficiently large `N`, since `s2=N^beta` dominates `n`. The cylinder is therefore gap-safe and has `2^k=Theta(s2*log s2)=Theta_beta(N^beta log N)` free coordinates. The counting upper bound above is `O(s2*log(s2+n))=O_beta(N^beta log N)`. Consequently,

```text
max_free_coordinates among gap-safe cylinders = Theta_beta(N^beta log N).
```

The dimension of the largest allowed cylinder is already pinned down by C-230; it is not new progress here. The cited Lupanov bound is stated, for example, in Lozhkin and Shiganov, [ECCC TR11-130](https://eccc.weizmann.ac.il/report/2011/130/), which reviews and sharpens the classical construction. C-230 also gives the original Lupanov source.

## 4. What this says about the attempted universal cover

The direct description formula

```text
OR_(d in D_s1) AND_(i in [N]) x_(i,C_d(i))
```

uses one full assignment term per circuit description. C-271 correctly found its cost `N*|D_s1|=2^(O(N^beta))` is too large. The safe-cylinder lemma identifies the exact permitted compression: replace full assignment terms by cylinders whose every completion remains below the high threshold `s2`. A term that merges local restrictions from two circuit descriptions without proving this cylinder condition can leak a high table; that is the hybrid failure in C-229/C-271.

An elementary consequence is that the maximal safe-cylinder volume exceeds the entire low class for every fixed OPS gap constant `c` and fixed `beta>0`, once `N` is large. Circuit-description counting gives `log2|Y| <= C_d s1 log2(s1+n)=O_beta(N^beta)`, while C-230's Lupanov cylinder has dimension `Theta_beta(N^beta log N)`. Thus it contains more tables than `Y`; the additional completions are medium, which promise soundness permits. This explains why raw volume alone cannot lower-bound the promise cover. It is a corollary of C-230 plus counting, not a new lower-bound barrier. Exact full-domain terms must stay inside `Y`; active-promise terms may contain a much larger medium region.

The volume comparison does not mean one cylinder covers the low class: this Lupanov cylinder fixes every table bit outside its chosen address block to zero, so it misses the all-one table, which is also in `Y`. The placement of low tables inside safe zones, not total zone volume, is the relevant quantity. This is precisely the low-mass issue already isolated by C-244.

This does not itself yield a compact cover. The address space has `K=N/2^k=Theta_beta(N^(1-beta)/log N)` such prefix blocks. Choosing unrelated size-`s1` circuits independently on `R` blocks costs `R*s1+O(R logN)`; the `s2/s1=Theta(logN)` budget permits only `R=O(logN)`, while `K` is polynomially larger for every fixed `beta<1`. This is the same global-description obstruction audited in C-265/C-271, now at the maximum safe-cylinder scale. The remaining compression must preserve one circuit identity across far more blocks than the size gap can independently pay for.

The lemma does not construct a small factorization. Counting cylinders is not enough: `|Y|/2^r` may be trivial because `r` can be as large as `log |SIZE(s2)|`, and a single AND gate can multiply two large term families. The desired bound must charge **shared generation of all gap-safe cylinders**, not their raw number, width, or per-anchor coverage.

## 5. Notation for the existing joint-zone obligation

For a partial assignment `P`, one can write

```text
RobustCC(P) = max { CC(w) : w extends P }.
```

Then `P` is an allowed promise implicant exactly when `RobustCC(P)<=s2`. A successful cover is a shared compatible-union program generating such implicants that cover every member of `SIZE(s1)`. This is just a notation for the existing C-244/O-244 question of bounding how much low-circuit mass a grammar-generated safe zone can contain; it does not separate a new theorem problem.

1. **Geometry:** which partial truth-table specifications have all completions of complexity at most `s2`?
2. **Coherent generation:** how many shared AND/intersection states are required to cover all `SIZE(s1)` tables by those specifications?

C-275 gives a sufficient construction for some cylinders, and C-230 pins down the maximum cylinder dimension. Neither gives a useful bound on how many low tables a cylinder covers or on coherent generation. Any common-circuit-core plus patch-budget characterization must be proved complete; otherwise it reintroduces C-271's coherence gap. Keep this under the existing O-153/O-168/O-244 frontier rather than opening a duplicate obligation.

## 6. Literature boundary and status

Published MCSP lower bounds against `AC^0[p]` concern constant-depth circuits and do not imply a lower bound for the unrestricted-depth cyclic/monotone cover model here ([Golovnev et al., ECCC TR19-018](https://eccc.weizmann.ac.il/report/2019/018/)). The safe-cylinder characterization therefore supplies no known-model hardness transfer.

**Novelty audit.** The maximum safe-cylinder dimension is C-230; the native q-zone factorization is C-244; the missing low-mass/joint-grammar charge is already O-153/O-168 and O-244. C-289 is a crosswalk and records the elementary `safe-cylinder volume > |Y|` corollary. It proves no lower bound on `q`, no `N^(1+o(1))` cover, and no P-vs-NP result. The actual bound remains `q=N-o(N)`. No new core theorem was obtained in this pass.
