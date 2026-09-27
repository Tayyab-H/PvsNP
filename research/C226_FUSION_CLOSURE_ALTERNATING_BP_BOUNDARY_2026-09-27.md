# C-226 - Fusion closure as alternating reachability; the BP transfer gap

Date: 27 September 2026
Scope: Continue the C-74/C-75 shared-DAG route from C-225. Test whether standard branching-program lower bounds can charge fusion closure states. This is a model-identification result and route filter, not a Gap-MCSP lower bound.

## 1. Exact alternating-reachability form

Let `Q=((E_i,H_i))_{i=1}^q`, `T_i=E_i intersect H_i`, and `L_{k,b}={v:v_k=b}` be signed literal slices on the promise domain. Set `A_i(v)=1` iff a true literal slice is contained in `E_i`, and `B_i(v)=1` iff one is contained in `H_i`. Let `D_i^E={j:T_j subset E_i}` and `D_i^H={j:T_j subset H_i}`. The least activation fixed point is

`x_i^0=0`,

`x_i^{t+1}=(A_i(v) OR OR_{j in D_i^E} x_j^t) AND (B_i(v) OR OR_{j in D_i^H} x_j^t)`.

It stabilizes after at most `q` strict rounds. Let `h_Q(v)=1` iff an empty-consequence state activates.

### Proposition 1 - exact alternating reachability representation

`h_Q(v)` is the winning predicate of a finite-state reachability game:

1. An existential root chooses a rule `i` with `T_i=empty`.
2. At rule state `i`, a universal move chooses side `E_i` or `H_i`.
3. At side state `(i,S)`, an existential move chooses a seed literal `L_{k,b} subset S` and tests `v_k=b`, or a predecessor `j` with `T_j subset S` and moves to rule state `j`.
4. A true seed test accepts; a false test rejects. Infinite plays reject.

**Proof.** The reachability attractor starts with rules having a seed support for both sides. Each later attractor round adds exactly rules whose two sides each have either a true seed or a predecessor already in the attractor. This is the displayed least-fixed-point recurrence. The root accepts exactly when an empty-carrier rule enters the attractor. Infinite plays rejecting selects the least, rather than greatest, fixed point.

The game has `O(q)` control states and at most `O(q(N+q))` transitions: each of the `2q` side states has at most `2N` seed options and `q` predecessor options. On the active OPS cover, `q>=N-o(N)`, so this is `O(q^2)` transitions. This is an exact compact **alternating cyclic program** for a fusion cover. Its rule dependency graph may contain cycles, although every winning strategy has an input-dependent decreasing activation rank.

Layering by a rank bound `r<=q` removes cycles at a cost of `O(q^2)` control states and `O(q^2(N+q))` transitions. That yields an acyclic alternating program, not an ordinary NBP or standard Sokolov rect-DAG. A straightforward conversion costs `O(q^3)`; batching support ORs gives the best recorded ordinary rect-DAG compiler, `O(q^3/log q)` vertices (C-100).

## 2. Why the q alternating states are not a q-vertex rect-DAG

The rule-state semantics has an AND/OR alternation at each rule: both sides must be supported, and each side may choose one of many seeds or predecessor rules. A standard NBP certifies one accepting path; a standard rect-DAG is acyclic and has rectangle-splitting constraints. Neither model includes a universal fork at a node with the least-reachability semantics above.

For a particular low input, an activation certificate can be compressed to a ranked proof DAG with at most `q` rule vertices and at most two selected support edges per vertex. Checking that certificate from the table requires validating both support branches and that support targets are genuinely earlier. A single BP path cannot fork to check both branches while preserving shared proof state. Unfolding can duplicate a shared predecessor many times; storing the active set or rank/support assignment directly takes `q` bits of control state and gives a generic deterministic-BP simulation of size `2^{O(q)} poly(N,q)`, not a useful polynomial in `q`.

This is a failure of the proposed transfer, not a lower bound against every possible compression. No polynomial-size conversion from this closure system to NBP/co-NBP is established here, and no impossibility of such a conversion is claimed.

## 3. A nearby MCSP lower bound and its promise consequence

Cheraghchi, Hirahara, Myrisiotis, and Yoshida prove an `N^{1.5-o(1)}` lower bound for standard nondeterministic, co-nondeterministic, and parity branching programs computing MCSP. Their proof uses a PRG for these BP models with seed length `S^{2/3+o(1)}` for size `S`, together with local low-circuit outputs. The same local-generator argument applies to a **promise separator** when thresholds fit:

Let `Y={v:CC(v)<=s1}` and `Z={v:CC(v)>s2}`, with `s1,s2=o(N/n)`. If co-NBP `h` is 1 on `Y` and 0 on `Z`, then `g=NOT h` is an NBP that is 0 on every locally generated table of circuit complexity at most `s1`, but is 1 on a `1-o(1)` fraction of uniform tables, since a random table has complexity above `s2` with probability `1-o(1)`. A local HSG/PRG for the NBP class with range complexity at most `s1` rules this out. With the cited seed-vs-size tradeoff, this gives

`size(co-NBP separator for Gap-MCSP[s1,s2]) >= s1^{3/2-o(1)}`.

This is an inference from the paper's local-PRG proof, not a claim that the paper states this exact two-threshold formulation. For OPS parameters `s1=N^beta/(c n)`, `s2=N^beta`, it gives `N^{3 beta/2-o(1)}`. It is superlinear only when `beta>2/3`; the project's magnification target requires sufficiently small fixed `beta`, so even a lossless route to this standard BP model would not by itself meet the target throughout the needed range.

Primary source: [Cheraghchi, Hirahara, Myrisiotis, and Yoshida, *One-Tape Turing Machine and Branching Program Lower Bounds for MCSP* (STACS 2021)](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2021.23); full version: [ECCC TR20-103](https://eccc.weizmann.ac.il/report/2020/103/).

## 4. Exact transfer status

- A successful q-pair fusion cover is exactly a q-state cyclic least-intersection/alternating-reachability construction (Cavalar-Oliveira; C-74/C-77).
- It yields an acyclic binary rect-DAG for the two-party mismatch relation; the best recorded compiler has size `O(q^3/log q)` (C-100).
- An L-vertex rect-DAG for that promise mismatch relation yields an `O(L)` promise-separator circuit and hence an `O(L)` fusion cover (C-89/C-90).
- It yields an `O(q)`-state alternating cyclic reachability program, but the cited MCSP lower bounds concern ordinary nondeterministic/co-nondeterministic/parity branching programs, not this alternating cyclic model.

There is no justified inequality `NBP-size <= poly(q)` to combine with the `N^{1.5-o(1)}` theorem. Substituting the alternating program into that theorem would be a model error. Treating the q alternating states as an acyclic rect-DAG would ignore universal branching and cycles.

## 5. Disposition and next target

**Proved:** exact alternating least-reachability normal form with `O(q)` states and `O(q(N+q))` transitions; local-PRG promise-separator consequence for standard co-NBPs in its valid threshold range.

**Rejected transfer:** standard MCSP BP lower bounds do not currently lower-bound fusion q, because no small alternating-to-NBP or closure-to-NBP compiler is known. Even the direct promise NBP bound reaches the superlinear range only for `beta>2/3`, outside the active small-beta magnification regime.

**Live target:** obtain a direct lower bound for this cyclic alternating reachability model on the low/high Gap-MCSP promise, or prove a special closure-to-standard-BP compilation whose overhead and parameter range imply `q>N^{1+epsilon}` at small fixed `beta`. In parallel, a near-linear rect-DAG construction remains the falsification test. O-141/O-149 remain open; C-225's one-cell concentration result does not resolve global reuse.

No superlinear `rho`, DAG lower bound, or P-vs-NP proof is obtained.
