# Research reset audit — 25 September 2026

## Objective and standard

The target remains an assumption-free proof of either $P\ne NP$, $P=NP$, or a genuinely new theorem that reduces the unrestricted core. A route counts only if every implication is proved and the resulting resource bound applies to arbitrary nonuniform circuits / polynomial-time machines. A new notation for the missing lower bound does not count as progress by itself.

## Strongest established facts

1. **Published magnification implication.** OPS show that the specified slightly-superlinear circuit lower bound for Gap-MCSP implies $NP\not\subseteq P/poly$, hence $P\ne NP$. This is the shortest established path.
2. **Project lower bounds.** The literal-slice/selector arguments prove only $N-o(N)$ gates. The output dependence is nearly total, but fan-in-two connectivity converts it to only a linear gate bound.
3. **Per-table witness existence.** Minimax gives a constant-margin distribution and an $O(s\log(s+n))$ anti-checker for each sufficiently high-complexity table. This settles existence, not a circuit that selects one for every table.
4. **C-45/C-47.** The margin gives a deterministic greedy existence proof; exact residual counts implement it in FP$^{\#P}$.
5. **C-48.** Relative approximate residual counts suffice. Under $NP\subseteq P/poly$, Stockmeyer counting on the short transcript gives a nonuniform $N^{1+O(\beta)}$ selector, reconstructing the known conditional OPS upper-bound mechanism. It does not establish any unconditional lower bound.

## Shortest dependency DAG

```text
OPEN O-1: Gap-MCSP has no circuit family of size N^(1+epsilon)
    -- published OPS magnification theorem -->
NP is not contained in P/poly
    --> P is not NP
```

O-1 is already a major unrestricted circuit lower bound, not a technical bridge. Its selector formulation is: for every high table $f$, a circuit maps $f$ to a short coordinate set $Q_f$ such that $f|_{Q_f}$ is outside the projection of every low-circuit truth table. This is a table-dependent puncturing certificate for a nonlinear code. The coding formulation is exact, but no lower bound beyond the existing $N-o(N)$ baseline follows from it.

## Highest unresolved statement and adversarial classification

The first unresolved statement is the O-1 lower bound. It is:

- **unrestricted:** yes, arbitrary nonuniform circuits with sharing and negation;
- **representation-dependent:** no in its formal target, though many proposed subarguments are;
- **technical:** no; it is essentially the desired magnification lower bound itself;
- **known open lower bound in disguise:** yes, via OPS it implies $NP\not\subseteq P/poly$;
- **currently tractable:** not established.

## Independent attacks and what kills each one

| Attack | Smallest target | Adversarial result | Status |
|---|---|---|---|
| Direct puncturing-certificate lower bound | Superlinear size for every map $f\mapsto Q_f$ that separates high tables from all low circuits | This is exactly O-1 in selector form; no proof mechanism beyond linear dependence/connectivity is known | Primary, unresolved |
| Greedy version-space scoring | Find a constant-fraction contraction coordinate | It exists by the dual margin; #P computes it; approximate counts reconstruct the conditional OPS selector under $NP\subseteq P/poly$ | Construction route completed conditionally; no universal necessity |
| Fiber entropy / affine sketch | Turn small fibers into superlinear circuit size | The general capacity condition is necessary, but affine-sketch exclusions do not control nonlinear label feedback; essential-input argument stops at $N-o(N)$ | Restricted branch closed at current strength |
| Diagonalization / self-reference | Build one NP language opposing every polynomial-time SAT decider | A machine-indexed diagonal can use an exponent depending on the index; no single polynomial verifier exponent has been obtained, and complementing the solver does not automatically preserve NP | Fails at uniform exponent / NP membership |
| Feasible proof complexity | Supply the Pich–Santhanam generator and EF non-p-boundedness | Existential data only yields adaptive KPT witnesses; no polynomial flattening or EF premise is known | Secondary, conditional |
| Fixed distributions / simple hidden regions | Defeat all universal menus or recover every sparse hard support | Fixed menus and many structured regions are handled, but an arbitrary selector depends on the full table and need not recover a region | Not a universal route |

**Additional adversarial check (C-16).** For a fixed low circuit $D$, overwrite the selector's queried bits with $D$'s labels. Hamming distance to $D$ strictly decreases on every high table, so the process reaches a table of complexity at most $s_2$ in at most $N$ rounds. This does not produce a contradiction: the endpoint may remain in the gap, a single round can overwrite many bits, and composing the selector for as many as $N$ dependent rounds loses the near-linear circuit-size bound. The descent is a valid dynamical consequence of selector correctness, but no selector lower bound follows from it.

## Method change recorded

Do not spend further effort making the greedy score itself more elaborate. C-48 shows it is a conditional implementation tool, not a property every selector is known to share. Do not infer a general lower bound from affine fibers, fixed samples, a particular region family, or a proof system. The active mathematical object is the universal selector/puncturing map, and any useful new lemma must constrain every such map or reduce it to a known target with an explicit size-preserving proof.

## Next high-value attacks

1. Try a direct adversarial construction of a sparse high table defeating an arbitrary near-linear selector circuit, with no assumption that its addresses are linear, local, or greedy. Explicitly count the candidate selector family and explain why the construction survives circuits larger than the number of truth-table inputs.
2. Seek a representation-independent invariant for adaptive coordinate puncturing that is stronger than essential-input count and survives nonlinear feedback. First test whether it can even rule out the priority-encoder selector for a fixed finite hypothesis class.
3. Check whether a prospective construction can be converted to a SAT/NP language while preserving a single polynomial time bound; do this before refining its diagonal details.
4. Keep the proof-complexity branch dormant unless a concrete $S^1_2$-provable generator or EF lower-bound theorem appears.

No candidate proof is ready. `research/CANDIDATE_PROOF.md` remains empty. No computational experiment was needed for this reset, and no tests were run.
