# C-359 - Fixed-circuit selector rectangles have a linear ceiling

Date: 29 September 2026  
Route: test whether monochromatic rectangles, fooling sets, or ordinary deterministic communication complexity of the proposed address-by-gate selector matrix can force a superlinear native state count.  
Classification: **EXACT MEASURE CEILING; FIXED-CIRCUIT MATRIX CANNOT CROSS LINEAR.**

## 1. Selector matrix

Fix one circuit description C and let X be its truth-table addresses, |X|=N. Let G be any finite set of gate/configuration locations. For each (x,g), record the forced local action at a binary OR gate: L when only its left child is 1, R when only its right child is 1; omit or assign a third symbol when the action is not forced. Write M_C:X x G -> Sigma, where |Sigma|=k is a constant (k=2 on the forced-only domain, at most 4 if both and undefined are retained).

## 2. Row-partition lemma

For every such matrix, its monochromatic rectangle partition number satisfies

```text
prt(M_C) <= k N.
```

For each row x and symbol a in Sigma, let G_(x,a)={g in G : M_C(x,g)=a}. The nonempty sets `{x} x G_(x,a)` are monochromatic rectangles, are pairwise disjoint, and cover the matrix. There are at most kN of them. Equivalently, Alice can send the address x to Bob using ceil(log2 N) bits; Bob computes the entry using his column g and sends its symbol using ceil(log2 k) bits. Hence deterministic communication complexity is at most `ceil(log2 N)+ceil(log2 k)`.

For a binary forced-choice matrix this gives at most 2N rectangles and communication at most log2(N)+1 bits. A standard single-color fooling set also has size at most N: two fooling pairs in the same row would have their crossed cells equal to the same required color. These bounds hold for every matrix, regardless of how complicated its entries are or how hard they were to compute.

## 3. Consequence for the proposed state-capacity route

Therefore no lower bound on the ordinary monochromatic rectangle partition number or standard fooling-set size of a fixed-circuit address-by-gate matrix can prove `q >= N g(N)` for an unbounded `g`. This is a cardinality ceiling, stronger than the earlier representation-dependence objection in C-349. Finding an inner-product, pointer, ISA, or other selector with complicated entries cannot evade it while the matrix rows remain the N addresses and the output is a constant-size local action.

This does **not** show that a q-state cover induces such a partition, nor does it bound arbitrary native covers. A lifted relation with low-table descriptions/anchors as additional row coordinates can have many more than N rows, but a proof must first derive a sound embedding of every valid C-319 cover into that relation. It may not assume that an arbitrary cover evaluates one chosen circuit. C-281 same-anchor splicing and C-342's seed-signature factorization remain possible tools for such a derivation, not substitutes for it.

### Column-only lifting does not escape the ceiling

Replacing G by pairs `(C,g)`—so columns now include every circuit description as well as the gate—still leaves X as the N-row side. The same row-slice proof gives `prt(M) <= kN`, with no dependence on how many descriptions occur as columns. A communication route can exceed the linear ceiling only if the row side itself carries additional context, such as `(w,x)` or `(C,x)`.

That lift has a quantifier trap. The local relation `for every x, there exists C_x with C_x(x)=w_x` is satisfied by every table, using the appropriate constant circuit at each address. The relevant condition is `there exists one C, for every x, C(x)=w_x`. Thus an anchor-indexed relation must enforce a single description across all address rows. A valid C-319 cover decides a promise; it need not output a circuit witness. No extraction of such a coherent selector from an arbitrary cover is currently proved.

## 4. Updated research direction

Retire fixed-description, address-by-gate monochromatic rectangle partition, ordinary deterministic communication complexity, and standard fooling sets as routes to the first superlinear q bound. Merely adding circuit descriptions to the column side does not reopen them. A surviving selector theorem must put anchor/context on the row side, preserve the one-description-across-all-addresses quantifier, and prove that every arbitrary q-state cover induces the resulting relation (or prove a sound witness-extraction theorem for this promise). Alternatively, work directly with the full-promise C-319 support grammar or construct the full-promise near-linear cover. C-343's C-109 bridge remains a warning that a superlinear full-promise lower bound is itself a general circuit lower bound at that scale.

## Status

This is an exact negative result for one proposed measure, not progress on the Gap-MCSP lower bound. The verified bound remains `rho_GapMCSP >= N-o(N)`. There is no arbitrary-cover state-capacity theorem, full-promise near-linear cover, superlinear lower bound, or P-vs-NP proof.
