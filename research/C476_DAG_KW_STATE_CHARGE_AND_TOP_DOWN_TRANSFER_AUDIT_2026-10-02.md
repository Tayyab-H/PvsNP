# C-476 — A sharing-faithful state model, and why the new top-down parity bound does not magnify

**Date:** 2 October 2026  
**Status:** exact circuit-to-state reduction plus a failed size-potential and failed OPS transfer. No new asymptotic lower bound, near-linear full-promise separator, or P-vs-NP result.

## 1. Exact target and theorem quantifiers

Write $N=2^n$, $s_1=\lfloor N^\beta/(10n)\rfloor$, and $s_2=N^\beta$. Let

$$U=\{T:CC_n(T)\le s_1\},\qquad V=\{T:CC_n(T)>s_2\}.$$

A valid separator is any total fan-in-two Boolean circuit $F$ with $F|_U=1$ and $F|_V=0$; values on the middle band are free. Its size $S$ counts all AND, OR, and NOT gates after conversion to a fixed basis, with unrestricted fan-out. The quantitative OPS target is one fixed $\epsilon>0$ such that for every sufficiently small fixed $\beta>0$, every such separator has more than $N^{1+\epsilon}$ gates. The primary Theorem 1.4 uses $2^{\beta n}/(cn)$ versus $2^{\beta n}$ for a universal $c\ge1$ and one $\epsilon$ uniform over all sufficiently small fixed $\beta$; the proof instantiates $c=10$. This exact lower bound would imply $NP\not\subseteq P/poly$, hence $P\ne NP$; it is a sufficient magnification route, stronger than the bare P-vs-NP question. [OPS, Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf)

## 2. Explicit mechanism: a rectangle-state DAG for shared computation

For a gate $g$ and orientation $(a,b)\in\{(1,0),(0,1)\}$, define its pair-state rectangle

$$R_{g,a,b}=\{x\in U:g(x)=a\}\times\{y\in V:g(y)=b\}.$$

This is a rectangle because the first coordinate depends only on $x$ and the second only on $y$. At the output gate, the valid-pair set is $U\times V$ in orientation $(1,0)$. If a pair in $R_{g,a,b}$ reaches a fan-in-two gate, at least one of the gate's two input wires has different values on $x$ and $y$. Therefore the parent rectangle is covered by a constant number of child rectangles, one for each differing child wire and orientation. A differing primary-input wire terminates at the corresponding coordinate and orientation. NOT gates only reverse orientation; constants can be removed or treated as trivial states.

**Lemma (sharing-faithful routing).** Every size-$S$ valid separator induces an acyclic rectangle-state graph with at most $2S+2N+O(1)$ states and constant outdegree, such that the root covers $U\times V$, every pair at a nonterminal state reaches a child state, and every terminal rectangle consists only of pairs differing at its labelled table coordinate.

**Proof.** Use one state for each gate and each of its two possible disagreement orientations. Preserve the circuit's fan-out by pointing all parent states to the same child state whenever they use that gate. For each pair in a state rectangle, the two endpoint evaluations at the parent gate differ. If both gate-input values agreed across the pair, the gate outputs would agree, a contradiction. Thus some child wire differs; assign the pair to the child's disagreement orientation. A primary input that differs supplies a terminal coordinate. The gate DAG is acyclic, so this routing terminates. Each gate creates only a constant number of oriented states and transitions; at most two terminal orientations are needed per table coordinate. This argument uses only the forced endpoints $U,V$ and leaves all middle-band labels unused. ∎

This is an actual handle on arbitrary reuse: the number of states counts distinct gates once, regardless of how many parents use them. Consequently, if every such state graph for the particular pair $(U,V)$ needs $K\ge N^{1+\eta}$ states for one fixed $\eta>0$ uniform over sufficiently small fixed $\beta$, then $S\ge (K-2N-O(1))/2=\Omega(N^{1+\eta})$. Choose any fixed $\epsilon<\eta$ (for example $\eta/2$) to absorb the constant and obtain the exact OPS non-membership at $N^{1+\epsilon}$. The implication does not assume that a separator reconstructs descriptions, enumerates witnesses, checks addresses, or retains a caller's history.

The representation itself is not a new circuit lower bound. Circuit-to-state routing is the exact model interface already audited in C-159/C-232/C-447. The missing theorem is a state-count lower bound for this specific Low-versus-High pair.

## 3. Serious potential attempt and its obstruction

For each state rectangle $R_v=X_v\times Y_v$, try its area $A(v)=|X_v||Y_v|$. If a state is covered by child rectangles $R_1,\ldots,R_k$, then

$$A(v)=|R_v|\le\left|\bigcup_jR_j\right|\le\sum_j A(j).$$

On a tree, recursively applying this inequality charges root area to leaves. It does not charge distinct DAG states: the same child rectangle may serve many parents, and unfolding the graph counts that child repeatedly. The inequality therefore controls a path-unfolding or a tree certificate, not the ordinary gate count. Replacing the sum by a maximum yields a depth bound, not a size bound. No argument in this cycle turns the area decrease into a per-state charge under reuse.

The tempting extension is to charge each gate by the number of contexts or paths that use its state. That quantity can be exponential in the DAG size and is not a gate measure. Counting it would silently replace the user's unrestricted-sharing model by a formula/tree model. A valid replacement must be a numeric potential on the distinct states themselves, prove its operation-wise growth bound despite merges, and show that every valid separator forces a superlinear total. No such potential was found here.

## 4. Counterconstruction attack

These are hostile tests of a *generic* incidence, constraint, or path charge. None is a full OPS separator or a counterexample to the requested lower bound.

| Pattern | Cheapest shared computation | What it defeats |
|---|---|---|
| Parity of $m$ bits | An XOR chain or balanced XOR tree uses $m-1$ XOR gates; a fixed AND/OR/NOT basis simulates it with $O(m)$ gates. | Counting many constraints, incidences, or path length as additional work. It also shows the new fixed-depth parity theorem cannot itself be an unrestricted-size source lower bound. |
| Repeated-block equality | Compare each coordinate in each block with its representative; use $O(N)$ gates total and reuse the representative signals. | Charging each repeated equality or each block independently after shared summaries exist. |
| Sparse parity checks | For a system with $I$ total nonzero incidences and $r$ checks, compute each check from its listed inputs and combine results using $O(I+r)$ Boolean gates. | Charging constraint multiplicity when total incidence is linear; dense or many-check instances can of course cost more. |
| Simple globally related blocks | Compute the small set of generator bits or block summaries once, then fan them out to every dependent table position. | Charging the number of output positions or violations instead of the size of the shared generator. |

The decisive scope distinction is that each row describes a simple induced family. It does not classify every size-$s_1$ table while rejecting every table with circuit size $>s_2$. These examples refute generic local-load mechanisms, not a promise-specific lower bound on the actual state graph.

## 5. Fresh literature lead: Korten's top-down parity lower bound

Oliver Korten's preprint, submitted 30 September 2026, proves that for every fixed depth $d\ge2$, parity needs more than $\exp(\epsilon_d n^{1/(d-1)})$ wires in depth-$d$ De Morgan circuits, for a constant $\epsilon_d>0$ depending on $d$. Its proof is a top-down Karchmer-Wigderson rectangle adversary with entropy/projection lemmas. The KW correspondence here charges communication rounds and per-round message width; it does not directly charge the number of distinct states in an arbitrary shared circuit DAG. [Korten, *Top-Down Lower Bounds for All Depths*](https://arxiv.org/abs/2609.38677)

There are two independent gaps to OPS:

1. The theorem is for each fixed depth. An arbitrary size-$S$ fan-in-two circuit can have depth as large as $S$; setting $d=S$ is invalid because the theorem's constants and threshold depend on fixed $d$. Even parity has an $O(N)$-gate circuit of depth $O(\log N)$, so these fixed-depth size bounds cannot give a superlinear unrestricted-gate lower bound for parity.
2. A reduction from a hard source would need both promised endpoints and an explicit total-gate budget. Parity is not such a source: its induced label itself costs only $O(m)$ gates. The new paper supplies no map from arbitrary Low/High truth tables to its parity KW game.

Thus the top-down method is an interesting restricted-depth result, not a transfer to OPS's all-depth, unrestricted-sharing state count. Chen et al.'s locality barrier is also method-specific; it neither forbids this rectangle-state route nor supplies the missing state-capacity inequality. [Chen et al., *Beyond Natural Proofs: Hardness Magnification and Locality*](https://arxiv.org/abs/1911.08297)

## 6. Paired full-promise separator attempt

The exact candidate-list circuit remains the control: OR over every size-$s_1$ circuit description $C$ of the equality test $T=C$ on all $N$ truth-table positions. It accepts every promised YES and rejects every promised NO because no NO table equals any listed candidate. With $K=2^{O(N^\beta)}$ descriptions, direct implementation costs $O(NK)=O(N\,2^{O(N^\beta)})$ total gates. This counts the comparisons, AND reductions, and OR combination; no wires, ROM lookup, output labels, or RAM operations are treated as free gates.

I also checked the plausible compression knobs against the exact promise. A fixed or balanced $q$-bit sketch must have $q\ge N-\log|L_{s_2}|=N-O(N^\beta\log N)$ to avoid a fiber containing both a Low and a High table (C-474). A fingerprint that can collide on any Low/High pair is unsound; a distributional collision estimate does not give worst-case promise separation. No circuit-specific trie or shared-codebook decoder with a proved near-linear gate count emerged. This is a failed construction attempt, not a proof that no such circuit exists.

## 7. Resource ledger, barriers, and exact effect

| Quantity | Treatment here |
|---|---|
| Ordinary total gates | $S$ counts every AND, OR, and NOT gate in the separator. This is the magnification measure. |
| Paid AND states / native fusion | Not used and not inferred. Any native $\rho$ theorem remains a separate model. |
| OR operations | Charged as ordinary gates; state outdegree is constant only because circuit fan-in is two. |
| Wires / fan-out | Wires do not replace gates in the lower-bound claim. Each gate has at most two input pins; arbitrary output fan-out is preserved by shared state identity. |
| State labels and descriptions | The state graph has $O(S+N)$ nodes, but bits needed to describe node labels are not ordinary gate count. |
| Runtime | Building or searching a graph/table is not charged as circuit gates and gives no size bound by itself. |

The locality barrier in Chen et al. constrains specified local techniques, not every nonlocal proof of ordinary circuit lower bounds. Korten's new result is primary literature for fixed-depth parity, not a new barrier and not an all-depth circuit lower bound. The exact OPS implication and its fixed-$\epsilon$/small-fixed-$\beta$ quantifiers are as stated in Section 1.

**Strongest proved statement in C-476:** a valid total separator of $S$ gates yields a rectangle-state DAG with $O(S+N)$ distinct states while preserving arbitrary gate reuse; an area potential is subadditive across outgoing edges but fails to charge distinct DAG states. The fresh top-down parity lower bound does not fill this gap.

**Quantitative effect: none.** Ordinary lower bound remains $N-O(N^\beta\log N)$ essential inputs, with only the previously recorded C-406 logarithmic reconvergence refinement. The fixed-$\epsilon$ OPS target remains open. Exact full-promise upper remains $O(N\,2^{O(N^\beta)})$. Native $\rho_{GapMCSP}\ge N-o(N)$ is separate. No P-vs-NP proof or near-linear full-promise separator was obtained.

## 8. Route decision

Retire the direct use of fixed-depth parity/KW lower bounds as an ordinary OPS total-gate mechanism, and do not count path-unfolding area, paths, OR branches, or messages as distinct paid gates. Keep the state-DAG representation as a faithful accounting language only. Resume its lower-bound use only with a concrete theorem about the distinct states of the actual pair relation, not a restatement that sharing is difficult. The full-promise enumeration upper stays as the paired construction baseline. This closes one literature transfer and one area-potential route; it does not close the project.
