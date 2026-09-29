# C-329 - Positional policies expose the lane-selector obstruction

Date: 28 September 2026  
Route: Q186 / test a near-linear universal-circuit verifier against the exact C-319 game.  
Classification: **EXACT POLICY NORMAL FORM + FAILED NEAR-LINEAR CONSTRUCTION; NO Q IMPROVEMENT.**

## 1. The exact strategy normal form

Fix a native list Q and a table w. At state i, the universal player chooses E or H. The existential player then chooses either a true seed literal on that side or one predecessor from the fixed set P_i^E or P_i^H. This is a finite reachability game with the least-fixed-point winning region from C-319.

If w is accepted, the existential player has a positional winning strategy from some empty-consequence root. Choose, for every reachable state and side, its strategy action. A seed action is recorded as one particular literal that is true on w; a transition action is recorded as one predecessor. The selected predecessor graph reachable from the root is well-founded: along each selected edge the standard attractor rank strictly decreases. Let S_sigma be the set of selected seed literals.

For every table w' matching all literals in S_sigma, the same positional strategy still wins. Its transition choices are unchanged, and each terminal seed choice remains true. Conversely, every table accepted by Q has such a rooted policy. Therefore

```text
Accept_Q = union over rooted well-founded policies sigma of Cube(S_sigma).
```

If Q is sound for Gap-MCSP, each policy cube is itself contained in SIZE(s2). It has at most 2q selected literals, one for each state-side obligation on which the policy stops at a seed. The number of policies is at most

```text
q * (q + 2N + 1)^(2q),
```

since there are at most q predecessor choices and 2N signed-literal choices per state-side, plus a dummy choice for unreachable positions. This is an exact cube-cover view of the fixed-point game; it does not count those cubes as separate native states.

## 2. Why policy counting does not break the linear barrier

Every sound cube has at most log2 |SIZE(s2)| free coordinates. Circuit counting gives log2 |SIZE(s2)|=N^(beta+o(1))=o(N). Thus C-112's constant-distance family of 2^(Omega(s1)) low tables, with pairwise distance Omega(N), has at most one codeword in any one sound policy cube. The policy count then implies only

```text
log2 |K| <= log2 q + 2q log2(q+2N+1),
```

or q = Omega(s1/log N) in the relevant range. This is much weaker than the already established q >= N-o(N). The code-family hostile check therefore rejects raw policy counting. The memoryless form sharpens the description of the missing compression theorem, but does not supply a new lower bound.

## 3. Direct test of the q=O(N+s1) shared-gate construction

Try one native state per truth-table address plus one shared state per gate of a guessed size-s1 circuit. The intended verifier universally challenges addresses and reuses the same gate states so that every address is checked against one globally fixed circuit description.

This fails at an OR gate. Consider two challenged addresses a,b at which its children have values

```text
u(a)=1, v(a)=0;       u(b)=0, v(b)=1.
```

The OR output is 1 at both addresses. A positional strategy at one shared gate state must choose the same existential child whenever that state is reached. Choosing u fails at b; choosing v fails at a. The ordinary cofactor/SIMD circuit is allowed to select a different true child in each lane, but one shared reachability-game state has one action per side. Copying the gate state for address contexts repairs this example and leads to the familiar address-by-gate cost in the direct construction.

This is a counterexample to the **shared positional gate-witness construction**, not a lower bound for arbitrary native covers. A cover might represent the address-dependent selector through more complicated endpoint sets or compatible-support families. C-306 rules out treating support tags as a free address register, but does not prove that every possible semantic encoding pays N*s1.

## 4. What the attempt teaches

The ordinary circuit and the native game both act over all cofactor lanes, but the relevant operation differs. A Boolean circuit OR is coordinatewise: each lane may use a different child witness. The native game chooses one predecessor action when a shared state is visited; its support product combines partial assignments by compatible union and conflict deletion. That product does not itself provide a lane-indexed selector.

The remaining construction question is no longer merely “can one gate state be reused?” It is:

```text
Can an address-dependent selector for a shared circuit gate be encoded
inside the compatible-support grammar with o(N*s1) native states,
while retaining one globally coherent circuit description?
```

A positive encoding with an explicit all-input soundness proof would give a full-promise cover; a lower-bound-preserving theorem ruling out all such encodings could contribute to Q186. Neither is proved here. C-257 parity and C-258 equality remain mandatory checks; the policy normal form accommodates both and does not separate the full OPS promise from them.

## 5. Checkpoint and disposition

1. Actual Gap-MCSP lower bound improved beyond N-o(N): **no**.
2. Valid N^(1+o(1)) full-promise cover: **no**.
3. State-sensitive synchronization theorem: **no**.
4. Positive CohEnc transfer or general reconstruction compiler: **no**.

Classify C-329 as **LOCAL / route filter**, not a breakthrough. Stop raw policy counting and the one-state-per-gate positional verifier. Keep Q186 active on an actual lane-selector encoding or an actual q-sensitive obstruction under C-281 reuse.

Reachability games are memoryless determined; here that standard fact also follows directly by choosing rank-decreasing actions in the finite attractor iteration. See, for background, [Finkbeiner's reachability-game notes](https://finkbeiner.groups.cispa.de/teaching/automata-games-verification-11/downloads/notes10.pdf).
