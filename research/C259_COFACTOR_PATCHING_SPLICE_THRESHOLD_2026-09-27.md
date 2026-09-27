# C-259 — Cofactor patching calibrates the multi-hole splice threshold

Date: 27 September 2026  
Scope: connect the C-116 cofactor fragmentation lemma and C-247's splice-entropy bound. The required number of independent high-entropy splice slots is `Theta(n)=Theta(log N)`, matching the number of cofactors whose simple patching still fits below `s2`. This calibrates O-153 but does not force slots from q.

## 1. Patching lemma for low circuit descriptions

Work with `n`-input Boolean circuits and `N=2^n`. Let `t=2^k`. For every prefix `a in {0,1}^k`, choose an arbitrary circuit `G_a` on the remaining `n-k` inputs, each of size at most `s1`. Define

\[
F(x,y)=G_x(y),\qquad x\in\{0,1\}^k,\ y\in\{0,1\}^{n-k}.
\]

A complete binary multiplexer tree on the k prefix bits has t leaves and t-1 internal selectors. Each selector costs O(1) gates in a fixed complete Boolean basis. Therefore

\[
CC(F)\leq t s_1+O(t).
\]

More generally, if the `G_a` are restrictions of t size-`s1` circuits on n inputs, substituting the prefix constants gives the same bound. Since the OPS parameters satisfy `s2=c n s1`, every prefix-selected hybrid of at most `t<=c'n` size-`s1` circuits is still in `SIZE(s2)` for a sufficiently small fixed `c'>0` and large n.

This is a direct obstruction to a one-hole or bounded-hole proof that produces only a simple prefix-selected hybrid: even if the pieces come from different low anchors, the result is still low at the target threshold.

## 2. Matching entropy threshold for private splice slots

Circuit counting gives

\[
\log_2|\mathrm{SIZE}(s_2)|=O(s_2\log(s_2+n))=O(s_2 n)
\]

at the OPS scale. The C-234 local family can be chosen with `m=Theta(s2)` suffix bits and all `2^m` functions of size at most `s1` (choose the constant in m small enough using the standard `O(2^k/k)` synthesis bound). Thus each independent replacement slot can carry `2^{Theta(s2)}` choices.

Under C-247's private-coordinate hypotheses, t such slots create a Cartesian product of distinct accepted tables of size `2^{Theta(t s2)}`. Soundness requires this to be at most `|SIZE(s2)|`, so

\[
t=O(n).
\]

Conversely, the patching lemma shows that `t=O(n)` prefix blocks can be mixed while staying in `SIZE(s2)`. Thus the natural component threshold from both direct construction and circuit counting is `Theta(n)`, up to constants.

## 3. Relation to C-116 and C-247

C-116 proves the complementary cofactor statement: partition into `m=Theta(n)` prefix cofactors; if every restriction of a high table had size at most a sufficiently small constant multiple of `s1`, a mux tree would compute the whole table below `s2`. Hence some cofactor must be hard. C-259 uses the same accounting in the forward direction: at most a small constant fraction of n independently chosen low cofactors remain safely patchable.

C-247 supplies the proof-semantic half: if a sound accepting derivation exposes t mutually independent replacement slots, their product of distinct completions cannot exceed `SIZE(s2)`. Combining the two results gives an exact conditional scale:

- every sufficiently small constant multiple `t<=c n` of prefix-selected low pieces can be recombined without leaving `SIZE(s2)`;
- more than a sufficiently large constant multiple `t>C n` of high-entropy private slots in a sound accepting proof are impossible.

On C-234's repeated-function family this is especially concrete. Fix a default k-bit function `g_0` and change only t prefix blocks to independently chosen functions `g_1,...,g_t`, each from the `2^{Theta(s2)}`-member low family. A circuit computes `g_0(u)` by default and muxes in the exceptional cofactor circuits on the t selected prefix values, for total size at most

\[
(t+1)s_1/4+O(t n).
\]

For `t<=c'n` this is at most `s2` for small enough `c'` and large n, so all such partial block hybrids are safe. If a proof exposes all tuples for `t>Cn` private blocks, there are `2^{Theta(t s2)}` distinct accepted hybrids, more than the entire `SIZE(s2)` class. This puts the safe-patching and unsafe-product sides on the same explicit family.

## 4. What this teaches the global-sharing programme

The local splice count is now calibrated. A useful O-153 proof cannot stop at finding two compatible low proofs or a constant number of holes. It needs either:

1. to force more than `C n` independent replacement slots with `2^{Theta(s2)}` choices each; or
2. to show that a compatible ownership selector is recoverable from the hybrid and source anchors and has complexity above `s2+O(s1)`, even with few source circuits; or
3. to prove that suppressing both phenomena costs `q>N g(N)` states.

The blocker remains the transfer from the q-state cyclic grammar to one of these alternatives. A q-state proof can reuse states in nested contexts, and C-247 gives no lower bound on how many independent slots it must expose. C-236's selector cap says compatible selectors must land in a set of size at most `|SIZE(s2)|`, but likewise does not charge q for restricting that image. C-258's equality fingerprints are a concrete low-cost way to keep simple block splices safe.

C-258 also prevents a count-only interpretation of the threshold: its repeated-block cover has `d` independent one-bit choices, potentially with `d>>n`, but their total entropy is only `d`, far below `log |SIZE(s2)|=Theta(s2 n)`. C-234's conditional contradiction instead needs about `Theta(s2)` bits of replacement entropy per slot, so more than `Theta(n)` such slots exceed the soundness budget. The missing invariant must aggregate *choice entropy and compatibility*, not merely count holes or states.

**Scope:** the mux inequality and the private-slot entropy bound each come from earlier project results (C-116 and C-247); C-259's contribution is to align them as one calibrated splice threshold. It is not a superlinear fusion lower bound, a full-promise upper bound, or a P-vs-NP proof. The exact next obligation is to relate the q-state grammar's overlap/conflict structure to the number of independent slots or selector complexity.
