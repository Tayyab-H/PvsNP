# C-478 ? First-principles audit of the OPS lower-bound frontier

**Date:** 2 October 2026  
**Status:** cumulative research assessment and route reset. It identifies the exact remaining proof obligation and closes both published Korten mirror-set initializations on every rectangle of the forced OPS relation. It proves no new circuit lower bound.

## 1. Exact target and its consequence

Let $N=2^n$, and for fixed $0<\beta<1$ let
$$s_1=\left\lfloor\frac{2^{\beta n}}{10n}\right\rfloor,\qquad s_2=2^{\beta n}.$$
Write $U=L_{s_1}$ and $V=\{T:CC_n(T)>s_2\}$. A total separator is any circuit $F:\{0,1\}^N\to\{0,1\}$ satisfying $F(u)=1$ for all $u\in U$ and $F(v)=0$ for all $v\in V$; values in the middle are unrestricted.

OPS Theorem 1.4 uses these thresholds in its proof. Its quantifiers are: if there exist constants $\epsilon>0$ and $\beta_0>0$ such that for every fixed $\beta\in(0,\beta_0)$, the corresponding promise family is not in $\mathrm{Circuit}[N^{1+\epsilon}]$, then $\mathrm{NP}\not\subseteq\mathrm{Circuit}[\mathrm{poly}]$. The same $\epsilon$ must work throughout the sufficiently small fixed-$\beta$ range. Under the standard circuit-family meaning of nonmembership, each such $\beta$ has arbitrarily large hard lengths; the theorem does not require a lower bound at every length. This would imply $P\ne NP$, but is stronger than that conclusion. [OPS, Theorem 1.4 and proof](https://www.theoryofcomputing.org/articles/v017a011/v017a011.pdf)

## 2. What the accumulated work establishes

The forced-pair circuit-to-Karchmer--Wigderson translation is exact and preserves sharing: an $S$-gate separator induces at most $2S+2N+O(1)$ distinct oriented gate/terminal states on $U\times V$. This is a useful accounting model, not a state lower bound. Rectangle area is subadditive over child edges, but summing it over a DAG counts a shared state once per incoming path. The only proved ordinary floor remains $N-O(N^\beta\log N)$ essential inputs, with C-406's logarithmic reconvergence refinement; no $N^{1+\epsilon}$ lower bound is known here.

The paired complete construction is the exact Low-description enumerator, of total size $O(N\,2^{O(N^\beta)})$. No near-linear full-promise separator has been found. A balanced sketch must retain $N-O(N^\beta\log N)$ bits, but that width statement does not charge the unrestricted computation after the bits are read.

C-477 now rules out more than the raw endpoint initialization: neither Korten's original $p$-limit lemma nor its strengthened $(p,k)$-limit lemma can start on **any nonempty rectangle** $X\times Y$ with $X\subseteq U$, $Y\subseteq V$, in either orientation. On the Low side, the entropy deficit is $N-o(N)$, while successful random subcubes must be nonempty; the lemma's parameter constraint makes such subcubes too rare. On a dense High side, a far High table remains in any sufficiently large subset, and the sparse Low codebook cannot supply the required mirror set. This closes those specific invariant transfers, not all adversary methods.

## 3. First-principles diagnosis

The core object is not a particular algorithm for MCSP. It is the minimum total-gate size over **all** Boolean interpolants between a sparse codebook $U$ and the larger low-complexity codebook $L_{s_2}$. Any claimed proof must work for every allowed middle-band labeling and every fan-in-two DAG with unlimited fan-out.

The record's failed mechanisms fall into four proof gaps:

1. **Semantic evidence without an operation charge.** Description counts, entropy, Fourier support, robustness, essential inputs, and certificate/query width constrain the accepted set or its boundary. None yet forces more than linear total gates after intermediate values can be shared.
2. **Easy restricted witnesses.** Parity, repeated-block equality, sparse parity checks, and simple global block relations have linear shared checkers on their induced families. They refute generic incidence or witness-count charges, but do not meet full Low-completeness and High-soundness.
3. **Transfers with missing margin.** Existing source maps either fail one promised endpoint, generate tables already Low on both source cases, or spend the source-hardness margin in generator/decoder cost. A reduction must map every source YES into $U$ and every source NO into $V$, and account for all gates in the multi-output generator.
4. **Model changes without a compiler.** Formula, bounded-depth, comparator, local-tree, oracle, implicit-table, and fusion results do not imply an ordinary total-gate lower bound unless the translation preserves sharing and budgets gates, wires, descriptions, and runtime separately.

This is why hundreds of local counterchecks have not accumulated into an asymptotic proof: they reject proxy quantities, while the target asks for superlinear work by an arbitrary shared computation. C-477 adds a concrete geometric restriction: even the stronger published coordinate-subcube mirror invariant cannot be seeded inside the forced relation.

## 4. A concrete theorem shape that remains valid

There are two legitimate ways to force the missing work; neither is currently completed.

**Direct shared-DAG charge.** Prove an operation-wise potential $\Phi$ on the actual Low--High rectangle states such that each allowed gate transition increases total charge by at most a proved constant and the root/output requirements force $\Phi\ge N^{1+\epsilon}$. The potential must be defined on distinct states, so reuse is paid once, and it must handle arbitrary semantic endpoints and all fan-out patterns. Rectangle area fails at this exact merge step; relabeling the desired inequality as ?non-shareability? is not a proof.

**Promise-saturated source map.** For a source problem with a proved circuit lower bound $h$, construct a multi-output map $E$ of total ordinary-gate cost $J$ such that YES instances map into $U$ and NO instances into $V$. Then a separator of size $S$ yields a source circuit of size at most $J+S+O(1)$, so $S\ge h-J-O(1)$. To reach OPS, prove $h-J>N^{1+\epsilon}$ under the actual parameters. No such map and residual margin are known. This is a valid transfer mechanism, not an assumed oracle or free decoder.

The next research cycle should select one of these two only after writing the exact quantity to be charged and testing it against the sharing canaries and the complete enumerator. Do not return to the two Korten mirror lemmas, rectangle-area unfolding, balanced-sketch width, or one-sided structured recognizers without a changed mathematical mechanism.

## 5. Literature boundary and originality

OPS is the primary hardness-magnification implication above. Chen--Hirahara--Oliveira--Pich--Rajgopal--Santhanam's locality barrier limits particular localizable lower-bound methods for magnification; it is not an impossibility theorem for all MCSP lower bounds. Korten's September 2026 preprint proves strong parity wire lower bounds at each fixed depth. C-477 is a parameterized transfer audit of its stated mirror-set invariants on the OPS relation; it does not improve Korten's theorem or prove an OPS bound. [Locality paper](https://arxiv.org/abs/1911.08297), [Korten preprint](https://arxiv.org/abs/2609.38677).

## 6. Frontier

**Unchanged.** Ordinary lower bound: $N-O(N^\beta\log N)$ essential inputs, with the known additive reconvergence refinement. Exact full-promise upper: $O(N\,2^{O(N^\beta)})$. Fixed-$\epsilon$ OPS magnification target: open. Native $\rho_{GapMCSP}\ge N-o(N)$: separate and open. No near-linear full-promise separator and no P-vs-NP proof.

### Project references

- [C-477: Korten mirror invariants fail on every OPS subrectangle](C477_KORTEN_MIRROR_INVARIANT_CANNOT_START_ON_OPS_PAIR_2026-10-02.md)
- [C-476: DAG state charge and top-down transfer audit](C476_DAG_KW_STATE_CHARGE_AND_TOP_DOWN_TRANSFER_AUDIT_2026-10-02.md)
- [C-475: promise-saturated restriction synthesis](C475_FIRST_PRINCIPLES_SYNTHESIS_AND_PROMISE_SATURATED_RESTRICTION_2026-10-01.md)
- [C-442: source composition budget](C442_FIRST_PRINCIPLES_REASSESSMENT_2026-10-01.md)
