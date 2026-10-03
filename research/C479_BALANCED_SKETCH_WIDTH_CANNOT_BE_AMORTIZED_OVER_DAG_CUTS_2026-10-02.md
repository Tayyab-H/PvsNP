# C-479 - balanced-sketch width does not amortize over arbitrary circuit cuts

**Date:** 2 October 2026  
**Status:** proof attempt and route-specific failure. It clarifies why the balanced-fiber theorem does not yet charge shared gates. No ordinary lower-bound or upper-bound frontier change.

## Candidate mechanism

C-474 proves that if a valid separator factors through a balanced map $\sigma:\{0,1\}^N\to\{0,1\}^q$ (all fibers have equal size), then
$$q\ge N-\log_2|L_{s_2}|=N-O(N^\beta\log N).$$
A natural attempt is to apply this at multiple topological cuts of a separator circuit and sum the widths, hoping to charge more than $N$ distinct gates.

## The balanced-cut lemma is valid

If a balanced sketch factors the separator, any fiber containing a forced-YES table must receive output 1 throughout that fiber. It therefore contains no forced-NO table and is a subset of $L_{s_2}$. Every fiber has size $2^{N-q}$, so $2^{N-q}\le|L_{s_2}|$. This recovers C-474 with the correct exact promise and an unrestricted decoder.

## Why the cut-to-gates step fails

**Unbalanced signals are free to the argument.** The separator output itself is a one-bit sketch $\sigma(T)=F(T)$. Its 1-fiber is a subset of $L_{s_2}$, but its 0-fiber contains almost all tables, so the map is extremely unbalanced. It separates the promise with one sketch bit. This is not a one-gate separator construction; it shows that C-474's fiber argument cannot lower-bound an arbitrary cut unless balance is independently proved. Intermediate gate values can be just as biased. For example, an AND chain has exponentially shrinking 1-fibers and only linear total gates.

**Widths do not add to gate count.** A topological cut may contain untouched primary inputs together with gate outputs. Signals can persist across many cuts through unlimited fan-out. Counting the frontier at each stage repeatedly counts the same input wires or shared states; wires are not gates, and the same gate cannot be charged once per cut. A valid summation would require a proved family of disjoint gate frontiers, each carrying a balanced sketch, with all bypass wires excluded. No such property follows from the circuit model or from separator correctness.

Attempting to rebalance each cut does not repair the proof: constructing a balanced refinement may require extra outputs or computation, and no size-preserving compiler from arbitrary separator cuts to balanced sketches is known. A presumed compiler would be an additional theorem, not a consequence of C-474.

## Paired full-promise construction check

The strongest concrete upper in this architecture remains C-426's coordinate projection: erase a common safe block of $m=\Theta(s_2\log s_2)$ table positions, retain $q=N-m$ coordinates, and accept exactly when the projection agrees with a projected Low table. C-231 proves every completion of this block around a Low anchor remains in $L_{s_2}$, so this is a valid full-promise separator. The projected Low-codebook decoder is still enumerative and costs $O(N\,2^{O(N^\beta)})$ total gates. C-474 shows this balanced width is already at the necessary fiber scale. No near-linear decoder or full-promise separator was found. This construction pairs with the failed cut-width lower-bound attempt, but does not alter the frontier.

## Counterchecks and scope

The output-bit example is a counterexample to the generic claim that every promise-separating cut must have near-$N$ sketch width. AND of all $N$ inputs is a linear-size circuit with a one-point 1-fiber, illustrating the same unbalanced phenomenon; it is not a separator for the OPS promise. Parity, repeated-block equality, sparse parity checks, and simple global block relations remain linear shared-computation canaries, but none is a full Low-complete/High-sound separator. Thus these constructions refute the proposed width-amortization mechanism, not the OPS target.

The balanced-sketch theorem itself remains correct and useful for architectures that prove balancedness at a specific interface. It says nothing about arbitrary unbalanced nonlinear computation after the input is read. Do not sum C-474 widths over circuit cuts unless both balance and non-reuse have independent proofs.

## Frontier and next action

**No change.** The ordinary lower bound remains $N-O(N^\beta\log N)$ with C-406's additive reconvergence refinement. The exact full-promise upper remains $O(N\,2^{O(N^\beta)})$. The fixed-$\epsilon$ OPS target and native $\rho_{GapMCSP}\ge N-o(N)$ remain open and distinct; no P-vs-NP proof follows.

The direct route still requires a merge-stable potential on distinct semantic gate states. A cut measure that assumes balanced fibers is insufficient. The source-map alternative still requires every YES image in $L_{s_1}$, every NO image above $s_2$, and a complete gate budget with residual source hardness. Full context: [C-478](C478_FIRST_PRINCIPLES_FRONTIER_AUDIT_AND_ROUTE_RESET_2026-10-02.md); balanced-sketch proof: [C-474](C474_BALANCED_SKETCH_FIBERS_FORCE_HIGH_COLLISIONS_2026-10-01.md).
