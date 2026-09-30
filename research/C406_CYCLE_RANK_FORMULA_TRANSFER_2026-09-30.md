# C-406 — Formula hardness forces logarithmic DAG reconvergence, not superlinear gates

**Status:** unconditional structural theorem for every ordinary Gap-MCSP separator, with a lower-order additive gate refinement but no superlinear or exponent improvement. The mechanism survives arbitrary fan-out by measuring only gate-to-gate reconvergence; repeated primary-input literals are free formula leaves. Its logarithmic gain is dominated by the existing input-support slack in the leading asymptotic frontier.

## Exact target and model

Let `N=2^n`. Fix the OPS promise with low threshold `s1=N^beta/(c n)` and high threshold `s2=N^beta`, where `c` is the universal constant in Oliveira–Pich–Santhanam Theorem 4. Their theorem says: if one fixed `epsilon>0` gives `Gap-MCSP[s1,s2]` no fan-in-two circuit of size `N^(1+epsilon)` for **every sufficiently small fixed** `beta>0`, then `NP` is not in `P/poly`. Their proof instantiates `c=10`. This is the unchanged target.

Circuits here have AND, OR, and NOT gates, total gate count `S`, fan-in at most two, free wires, and unrestricted fan-out. Wire count, description length, runtime, and native fusion states are distinct resources.

## Mechanism: reconvergence rank

Take any valid total separator `C`. Remove gates not in the output ancestor DAG; let `G` be the remaining gates. Form the **gate graph** whose vertices are these gates and whose edges are wires from one gate output to an input pin of another gate. Primary-input and constant pins are treated as separate formula leaves, even when the same primary input feeds many pins. Let `E_g` be the number of gate-to-gate wires, counted with multiplicity, and define

`mu(C) = E_g - G + 1`.

The gate graph is connected to the output gate. Its cycle rank counts reconvergence among computed gate values; primary-input fan-out does not count as shared intermediate work. It is not a count of paid AND states.

**Unfolding lemma.** The DAG computes a De Morgan formula with at most `2G 2^mu(C)` leaves.

**Proof.** Orient gate-to-gate wires toward the output gate. Every other gate has outdegree at least one. If `d_v` is its outdegree, then

`sum_(v != output)(d_v-1) = E_g-(G-1) = mu(C)`.

Unfold the DAG by making one copy of a gate for each directed path from it to the output. The number of paths from any gate is at most `product_v d_v`. Since `d <= 2^(d-1)` for every integer `d>=1`, this product is at most `2^mu(C)`. Thus there are at most `G 2^mu(C)` gate copies, and each copy contributes at most two primary-input or constant leaves. The formula has at most `2G 2^mu(C)` leaves.

Let `L_ext` be the number of gate input pins fed by primary inputs or constants. There are at most `2G` gate input pins, and each essential table input must feed at least one such pin, so `L_ext>=E(C)`. Therefore `E_g<=2G-L_ext<=2G-E(C)`, whence `mu(C)<=G-E(C)+1` and

`S >= G >= E(C)+mu(C)-1`.

This separates total gates, gate-to-gate reconvergence, primary-input fan-out, and unused input coordinates.

## Theorem from the OPS formula lower bound

For every fixed `0<alpha<2`, OPS Theorem 5 supplies a constant `d>1` such that no `U2` formula with at most `N^(2-alpha)` leaves separates

`Gap-MCSP[n^d, 2^((alpha/2-o(1))n)]`.

Fix any `beta<alpha/2`. Eventually `n^d <= N^beta/(c n)` and `2^((alpha/2-o(1))n) >= N^beta`. Thus every separator for the OPS promise is also a separator for that formula-hard promise: its YES instances are a subset of the OPS YES set, and its NO instances are a subset of the OPS NO set. The middle remains unconstrained in both problems. Applying the unfolding lemma gives, for all sufficiently large `N`,

`2S 2^mu(C) > N^(2-alpha)`.

Consequently, for every fixed `delta<1-alpha`, any OPS separator with `S<=N^(1+delta)` must have

`mu(C) > (1-alpha-delta) log_2(N) - O(1)`.

For example, choose `alpha=1/2`, `beta=1/8`, and `delta=1/8`. Any separator of size at most `N^(9/8)` then has at least `(3/8) log_2 N - O(1)` gate-to-gate cycles. This is an unconditional restriction on every separator in that parameter regime and allows arbitrary shared DAGs. More generally, fix any `0<beta<1/2` and any `gamma<1-2 beta`. Choose fixed `alpha>2 beta` and `delta>0` with `alpha+delta<1-gamma`. If `S<=N^(1+delta)`, the cycle inequality gives `mu>gamma log_2 N-O(1)`; if `S>N^(1+delta)`, then `S-E(C)>gamma log_2 N-O(1)` directly since `E(C)<=N`. In either case, `S>=E(C)+gamma log_2 N-O(1)`. Thus the formula transfer proves a logarithmic gate surplus over the essential-input count for every fixed `beta<1/2`.

The basis conversion causes at most a constant factor if the MCSP circuit basis is stated as arbitrary fan-in-two Boolean gates; the strict exponent slack `beta<alpha/2` absorbs that factor. The formula theorem measures leaves, as required above.

## Where the attempted superlinear gate charge fails

The gate-to-gate cycle bound alone gives only `mu=Omega(log N)` in the near-linear case. C-403 separately gives `E(C)>=N-O(N^beta log N)` essential inputs, so the gate inequality becomes

`S >= N-O(N^beta log N) + Omega(log N)`.

Since `N^beta log N` dominates `log N` for every fixed `beta>0`, this does **not** change the leading asymptotic order `N-O(N^beta log N)` of the proved total-gate lower bound. It does give the formal additive refinement `S>=E(C)+gamma log_2 N-O(1)` stated above. The formula lower bound creates only a polynomial formula-to-circuit ratio, and `log_2(N^(2-alpha)/N^(1+delta))` is logarithmic. A superlinear total-gate result would need a much stronger formula lower bound, a sharper unfolding theorem that exploits this promise, or a direct charge of cycle rank beyond the number of dispensable input variables. None is proved here.

This is the decisive obstruction for this mechanism. Retain it as a structural calibration; do not report it as an OPS lower bound or keep sharpening the same cycle lemma without a new bridge.

## Adversarial checks and full-promise upper attempt

- **Parity and repeated-block equality:** both have `O(N)`-gate ordinary circuits, so dependence on many inputs does not force superlinear total gates. Repeated-block equality has an `O(N)` De Morgan formula, hence a gate graph with `mu=0` (input literals can repeat as separate leaves). A standard chained parity circuit over AND/OR/NOT uses `O(N)` gates but has `Theta(N)` gate-to-gate cycles because each running parity feeds both arms of the next XOR. Sparse parity checks and simple copy/XOR block relations likewise have `O(N)`-gate implementations when their total relation size is `O(N)`; they can use linear reconvergence while staying linear in total gates. These are counterexamples to generic superlinear charges from global dependence or constraint counts, not Gap-MCSP separators, and do not refute the logarithmic cycle theorem.
- **Single-anchor Hamming ball:** every `r`-sparse modification of `0^N` is low whenever its patching circuit is within `s1`. A weight threshold can accept that whole sparse subpromise using `O(N)` gates. It rejects other low tables, including parity truth tables. Therefore robustness around one low anchor cannot give the full-promise lower bound; this is an explicit failed separator construction.
- **Full-promise enumeration attempt:** enumerate the `M<=2^(O(s1 log(s1+n)))=2^(O(N^beta))` descriptions of circuits below `s1`, compare the input against each full `N`-bit table, and OR the equality bits. This accepts every promised YES and rejects every promised NO, costing `O(NM)` total gates, `O(NM)` wires, and `O(NM log(NM))` indexed-description bits. Direct construction time is `O(MNs1)` by simulating each candidate on all addresses. It is a valid upper bound but not near-linear; no trie or universal-circuit factorization with a proved near-linear gate bound was found.

OPS's conditional Anti-Checker Lemma is the strongest existing counterconstruction to a claim that adaptive selection must pay separately for each score. Under `NP subseteq P/poly`, it produces `t=N^(10 beta)` anti-check points. The selector circuit has size at most `2^(n+k beta n)=N^(1+k beta)`; labeling the points and building the Succinct-MCSP instance costs `O(tN)=O(N^(1+10 beta))`; its assumed NP/poly verifier circuit has size `m^ell=N^(10 beta ell) polylog(N)`, where `m=poly(n)N^(10 beta)`. Choosing `beta=epsilon/(100 ell k)` puts each term below `N^(1+epsilon/3)` for large N, giving the published full-promise `N^(1+epsilon)` separator. This conditional construction uses shared DAG computation, not an unconditional upper bound or refutation of the desired lower bound. The selector route was already explored in this project and is not reopened here.

## Native cyclic fusion is a separate model

This cycle proves a theorem only for ordinary acyclic fan-in-two AND/OR/NOT circuits. Its `S` counts total gates and `mu` counts gate-to-gate reconvergence. It does not count native paid AND states, OR rules, wires, description bits, or runtime. In particular, no `q^2` total-gate compiler or lower bound is inferred from a paid-AND unrolling.

The C-319/C-258 native model permits arbitrary semantic endpoint sets, wide seed clauses, unrestricted reuse, and cyclic rules interpreted by least-fixed-point closure. A cycle in that transition graph is not an ordinary DAG path and cannot be unfolded by the path-count proof above; unsupported cycles also do not become true without finite derivations from the semantics. This report neither restricts endpoint width nor deletes wide seeds, and it claims no native cover bound. Since no native lower-bound route is attempted here, no semi-filter extension or subpromise-to-full-promise transfer is being asserted. The native full-promise frontier remains `rho_GapMCSP>=N-o(N)`.

## Barriers, originality, and status

The formula theorem used above is a published result, and the gate-graph unfolding argument is an elementary project-specific transfer; neither is claimed as a new circuit-complexity theorem. OPS Theorem 5 is explicitly in the `U2` formula model and has different low/high parameters from its ordinary-circuit magnification theorem. The parameter containment above is proved; it is the circuit-to-formula transfer that loses almost all quantitative force.

Cavalar–Oliveira's 2025 ECCC survey states that the strongest known gate lower bounds for explicit single-output functions against unrestricted Boolean circuits are linear with constant at most five (basis-dependent). This contextualizes the gap but is not a theorem that blocks the Gap-MCSP promise target. Chen et al.'s locality barrier remains technique-specific; the present unfolding argument neither evades nor contradicts it.

**Strongest proved statement this cycle:** for each fixed `alpha` and `beta<alpha/2`, every OPS separator satisfies `2S2^mu>N^(2-alpha)`; hence a separator with `S<=N^(1+delta)` for `delta<1-alpha` has `mu>(1-alpha-delta)log_2 N-O(1)` cycles.

**Exact frontier effect:** the input-support gate bound strengthens additively to `S>=E(C)+gamma log_2 N-O(1)` for every fixed `beta<1/2` and `gamma<1-2 beta`; since `E(C)>=N-O(N^beta log N)`, the main asymptotic floor remains `N-O(N^beta log N)`. The OPS `N^(1+epsilon)` target remains open. The full-promise enumeration upper remains `O(N2^(O(N^beta)))`; no near-linear separator was found. Native `rho_GapMCSP>=N-o(N)` remains unchanged. No P-vs-NP proof follows.

### Primary sources

- Oliveira, Pich, Santhanam, [*Hardness Magnification near State-of-the-Art Lower Bounds*, Theorem 4 and Theorem 5](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).
- Cavalar, Oliveira, [*Boolean Circuit Complexity and Two-Dimensional Cover Problems*, ECCC TR25-033](https://eccc.weizmann.ac.il/report/2025/033/download).
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://doi.org/10.1145/3538391).
