# Gemini Salvaged Results — Sound and Useful Only

**Date:** 28 September 2026  
**Source:** Audit of the `Gemini/` research files added in commit `7ef4e185c541913af52eceb3376f0c608317fb0b`  
**Status:** **AUDITED / SAFE TO RETAIN**  
**Important:** This file intentionally removes the unsupported breakthrough claims from the original Gemini reports. It does **not** prove a superlinear Gap-MCSP fusion lower bound, `NP \not\subseteq P/poly`, or `P \ne NP`.

---

## 1. Current project status

The active target remains

[
\rho_{\mathrm{GapMCSP}}(n,\beta)>N^{1+\varepsilon},
\qquad N=2^n,
]

for one fixed (arepsilon>0) and all sufficiently small fixed (eta>0), at the OPS parameters

[
s_1=\frac{N^\beta}{c\log N},
\qquad
s_2=N^\beta.
]

The strongest established lower bound on the **actual** Gap-MCSP fusion measure remains essentially

[
\rho_{\mathrm{GapMCSP}}\ge N-o(N).
]

Nothing in the audited Gemini folder changes that bound.

The useful material from Gemini consists of:

1. a correct **Universal Decoder inequality** for C-125/LowExt maps;
2. exact **single-hole and multi-hole consistency criteria** for proof/context splicing;
3. a useful clarification of what a successful native multi-hole argument would still have to prove;
4. a useful research hypothesis around global synchronization / grammatical entanglement, provided it is treated as an **open programme**, not a theorem.

---

# 2. Universal Decoder inequality for C-125 maps

## 2.1 Setup

Let

[
f:\{0,1\}^m\to\{0,1\}
]

be monotone.

Let

[
\phi=(\phi_{j,0},\phi_{j,1})_{j\in[N]}
]

be a monotone C-125 rail map computed with (a) binary AND gates and arbitrary uncharged OR gates, satisfying:

### YES completeness

For every (x\in f^{-1}(1)), there exists

[
w_x\in\mathrm{SIZE}(s_1)
]

such that

[
e(w_x)\le\phi(x).
]

### NO soundness

For every (x\in f^{-1}(0)), there exists

[
z_x\notin\mathrm{SIZE}(s_2)
]

such that

[
\phi(x)\le e(z_x).
]

Choose one witness (w_x) for each YES input and let

[
\mathcal W=\{w_x:x\in f^{-1}(1)\}.
]

Define the coordinate set on which the selected witnesses vary:

[
S=
\{j\in[N]:
\exists u,v\in\mathcal W, u_j\ne v_j\},
\qquad
\delta=|S|.
]

Outside (S), all selected witnesses agree. Let (w_0) denote that common restriction.

Let

[
\mathcal W_S=
\{w|_S:w\in\mathcal W\},
\qquad
M=|\mathcal W_S|.
]

---

## 2.2 Theorem — Universal Decoder inequality

Every such map satisfies

[
\boxed{
\operatorname{CycAnd}(f)
\le
a+M\delta+N.
}
]

Equivalently,

[
\boxed{
\operatorname{CycAnd}(f)-a
\le
M\delta+N.
}
]

### Proof

For each pattern (sigma\in\mathcal W_S), choose one selected witness
(w^{(\sigma)}\in\mathcal W) whose restriction to (S) is (sigma).

Define

[
H(x)=
\left(
\bigvee_{\sigma\in\mathcal W_S}
\bigwedge_{j\in S}
\phi_{j,\sigma_j}(x)
\right)
\wedge
\left(
\bigwedge_{k\notin S}
\phi_{k,(w_0)_k}(x)
\right).
]

If (x) is a YES input, the selected witness (w_x) supplies all of the rails in one of the (sigma)-terms and all common rails outside (S), so (H(x)=1).

Now let (x) be a NO input. If (H(x)=1), some (sigma\in\mathcal W_S) has every rail of the corresponding witness (w^{(\sigma)}) active. Thus

[
e(w^{(\sigma)})\le\phi(x).
]

NO soundness supplies a high table (z_x) with

[
\phi(x)\le e(z_x).
]

Therefore

[
e(w^{(\sigma)})
\le
e(z_x).
]

Since both are complete one-hot truth-table encodings, this forces

[
w^{(\sigma)}=z_x,
]

contradicting

[
CC(w^{(\sigma)})\le s_1<s_2<CC(z_x).
]

Hence (H=f).

The extra AND cost beyond the (a) gates of (phi) is at most

[
M(\delta-1)+(N-\delta-1)+1
\le
M\delta+N.
]

This proves the claim.

---

## 2.3 What the theorem genuinely implies

This theorem gives a real obstruction to LowExt transfers in the **low witness-diversity** regime.

If

[
M\delta+N
\ll
\operatorname{CycAnd}(f),
]

then

[
a
\ge
\operatorname{CycAnd}(f)-M\delta-N,
]

so the map itself pays almost all of the source complexity and little transfer margin remains.

This cleanly subsumes several previously observed failures:

- one fixed witness / fixed witness pattern;
- small rank palettes;
- low-entropy witness menus;
- fixed-baseline constructions with only a small number of possible selected low codes.

---

## 2.4 What the theorem does **not** imply

The theorem does **not** prove Route A impossible.

The unresolved branch is

[
M\delta
\gtrsim
\operatorname{CycAnd}(f).
]

A large number (M) of possible witness restrictions does **not**, by itself, imply that the multi-output encoder requires large AND complexity.

In particular, the following implication is **not proved**:

[
M\text{ large}
\Longrightarrow
a\text{ large}.
]

A small monotone multi-output circuit can, in principle, realize many output patterns across its inputs. Any future attempt to close Route A must prove an additional theorem charging the cost of this high-diversity witness routing.

### Correct Route A frontier

The valid dichotomy is therefore:

[
\boxed{
\text{small }M\delta
\Rightarrow
\text{decoder kills the transfer},
}
]

while

[
\boxed{
\text{large }M\delta
\Rightarrow
\text{high-diversity witness-coherence problem remains open}.
}
]

---

# 3. Exact proof/context splice consistency

The Gemini files gave a useful clean formulation of consistency for proof splicing. This is sound and worth preserving.

Let (K_w) be an accepting context with a hole at state (i), obtained from a proof matching a low table (w). Let (P_{w'}) be a replacement proof rooted at the same state (i), matching another low table (w').

Write

[
V_K=\operatorname{Var}(K_w),
\qquad
V_P=\operatorname{Var}(P_{w'}).
]

Then the joined support

[
K_w\cup P_{w'}
]

is consistent iff the two tables agree on every variable used by both pieces:

[
\boxed{
K_w\cup P_{w'}\text{ consistent}
\iff
w|_{V_K\cap V_P}
=
w'|_{V_K\cap V_P}.
}
]

This is immediate from the signed-literal representation: a conflict occurs exactly when the context contains ((k,w_k)), the replacement contains ((k,w'_k)), and (w_k\ne w'_k).

If the join is consistent, the native substitution law from the existing project applies: substituting the replacement proof into the context gives an accepting proof support.

Therefore every full truth table extending the resulting support lies in (mathrm{SIZE}(s_2)), by soundness of a valid Gap-MCSP fusion closure.

---

# 4. Exact multi-hole consistency criterion

Suppose an accepting proof has (t) pairwise cut occurrences with a (t)-hole context (K_w).

For each hole (r\in[t]), let (P_r) be a replacement proof matching low table (w^{(r)}), and let

[
V_K=\operatorname{Var}(K_w),
\qquad
V_r=\operatorname{Var}(P_r).
]

Then

[
K_w\cup P_1\cup\cdots\cup P_t
]

is consistent iff all pairwise overlaps agree:

[
\boxed{
w^{(r)}|_{V_r\cap V_K}
=
w|_{V_r\cap V_K}
\quad
\forall r,
}
]

and

[
\boxed{
w^{(r)}|_{V_r\cap V_s}
=
w^{(s)}|_{V_r\cap V_s}
\quad
\forall r\ne s.
}
]

This is a useful exact formulation of the multi-hole compatibility problem.

It does **not** imply that useful private-coordinate holes, independent replacements, or high hybrids automatically exist.

Those remain the hard part.

---

# 5. Correct owner-mask statement

For a compatible single-hole splice, define the owner mask

[
\mu=
\operatorname{Var}(P_{w'})
\setminus
\operatorname{Var}(K_w).
]

The canonical hybrid

[
h_\mu=(\mu?w':w)
]

is a completion of the joined support and therefore, if the closure is sound,

[
h_\mu\in\mathrm{SIZE}(s_2).
]

A direct circuit upper bound is

[
\boxed{
CC(h_\mu)
\le
CC(w)+CC(w')+CC(\mu)+O(1).
}
]

Thus if the owner mask itself has low complexity, for example

[
CC(\mu)=O(n),
]

then

[
CC(h_\mu)
\le
2s_1+O(n)
<s_2
]

at the OPS parameters for large enough (N).

This explains why many **simple-mask** two-way splices are harmless.

However there is no general theorem that every owner mask generated by an arbitrary context/proof cut is simple.

Indeed, with (w=0^N) and (w'=1^N),

[
h_\mu=\mu,
]

so a complex owner mask can produce a complex hybrid even though both source tables are trivial.

Therefore the following stronger statement must **not** be retained:

> every two-way splice has circuit complexity (2s_1+O(n)).

The correct statement is conditional on owner-mask complexity.

---

# 6. Correct multi-piece patching statement

There is a sound conditional observation behind Gemini's multi-hole discussion.

Suppose a truth table is assembled from (t) low circuits (w^{(1)},\ldots,w^{(t)}) using a partition

[
A_1,\ldots,A_t
]

whose ownership/selection predicates themselves have low circuit complexity.

Then a multiplexer gives roughly

[
CC(h)
\le
\sum_{r=1}^{t}CC(w^{(r)})
+
\text{cost of the ownership decoder}.
]

For standard prefix/cofactor partitions, the ownership decoder is cheap, yielding the existing C-259 phenomenon:

[
t=O(n)
]

independently selected (s_1)-size cofactors can remain within the (s_2=\Theta(ns_1)) budget.

This is useful as a **calibration**.

It is not a universal statement about arbitrary native proof holes. An arbitrary owner partition may itself have high circuit complexity, so a two-piece or constant-piece hybrid can already be high.

The native lower-bound problem therefore cannot be reduced to the number of holes alone. It must jointly control:

1. the number/entropy of replacement choices;
2. the compatibility of those choices;
3. the complexity of their ownership masks/partition.

---

# 7. What remains useful from the “grammatical entanglement” idea

The phrase **grammatical hypergraph entanglement** can be retained as a research direction, but not as a proved invariant.

The sound intuition is:

> A small native cyclic grammar may have to coordinate many proof occurrences so that arbitrary compatible substitutions do not generate too many high-complexity hybrids.

A potentially useful abstract object is a multi-hole compatibility hypergraph:

- vertices: closure states or marked proof occurrences;
- hyperedges: collections of simultaneously cut occurrences;
- labels: families of compatible replacement proofs / owner masks;
- soundness condition: every compatible reconstructed cylinder must remain inside (mathrm{SIZE}(s_2)).

A genuine breakthrough theorem would need to prove something like:

[
\boxed{
q\text{ small}
\Longrightarrow
\text{a high-entropy compatible product of replacements}
}
]

or else

[
\boxed{
\text{suppressing all such products costs }N^{1+\varepsilon}
\text{ states}.
}
]

This is still open.

The existing repeated-block equality cover, parity calibration, and C-281 owner-mask examples must remain mandatory hostile tests.

---

# 8. A corrected fingerprint principle

One Gemini argument attempted to prove that if a context conflicts with every alternative low table in a family (mathcal F), then the overlap set must have size at least (log|\mathcal F|).

That is false in that form.

If a fixed (w) differs from every (w'\in\mathcal F\setminus\{w\}) somewhere on overlap set (mathcal O), this proves only

[
w'|_\mathcal O\ne w|_\mathcal O
\quad
\forall w'\ne w.
]

It does **not** imply that distinct alternatives have distinct restrictions from one another.

A valid (log|\mathcal F|) bound would require the stronger property

[
u|_\mathcal O\ne v|_\mathcal O
\qquad
\forall u\ne v\in\mathcal F.
]

Under that stronger assumption, restriction to (mathcal O) is injective and therefore

[
|\mathcal O|\ge\log_2|\mathcal F|.
]

This corrected form may be useful if a future theorem can genuinely force pairwise separation of an entire active family.

At present, no such forcing theorem is known.

---

# 9. State count versus proof-tree leaf count

A second important audit lesson should be preserved.

A proof tree containing (L) leaf occurrences does **not** imply that the underlying cyclic/shared grammar has (L) distinct rules.

A small shared DAG or cyclic grammar can unroll to a proof tree with exponentially many occurrences.

Therefore one cannot infer

[
q\ge L
]

from a large unrolled proof leaf count without an additional **non-sharing** theorem.

This is one of the core obstacles already visible in C-246 and the earlier shared-DAG work.

Any future fingerprint/entanglement argument must charge **distinct reusable states**, not merely occurrences in one proof tree.

---

# 10. Asymptotic caution required for OPS magnification

The following asymptotic distinctions are mandatory.

For fixed (0<\beta<1),

[
N^\beta\log N=o(N).
]

So a lower bound of order

[
N^\beta\log N
]

is not superlinear in (N).

Likewise

[
N\log N=o(N^{1+\varepsilon})
]

for every fixed (arepsilon>0).

And

[
q=\omega(N)
]

does not imply

[
q>N^{1+\varepsilon}
]

for a fixed (arepsilon>0).

The OPS magnification target requires the latter fixed-exponent improvement. Future reports must not conflate these scales.

---

# 11. Corrected strategic conclusions

## Route A — LowExt transfer

**Not closed.**

What is established is the decoder inequality

[
\operatorname{CycAnd}(f)-a
\le
M\delta+N.
]

Therefore any successful transfer must live in a regime with sufficiently rich witness diversity (Mdelta).

The open task is to determine whether that high-diversity regime can be realized by a low-AND map, or whether witness-coherence itself forces large AND complexity.

This remains a legitimate research route.

---

## Route B — Native cyclic fusion

The exact useful structures are:

- least-fixed-point proof grammar;
- blocker duality;
- context/proof substitution;
- single- and multi-hole overlap consistency;
- owner-mask hybrids;
- safe-cylinder soundness.

The missing arrow remains:

[
\boxed{
\text{small }q
\Longrightarrow
\text{dangerous compatible product}
\text{ or provably expensive synchronization}.
}
]

No theorem in the Gemini folder proves this arrow.

---

# 12. Claims from the deleted Gemini reports that must NOT be reused

The following statements are unsupported or false as stated and should not be treated as project theorems:

1. **“P ≠ NP has been proved.”**
2. **“The actual Gap-MCSP fusion measure is superlinear.”**
3. **“Route A is universally closed.”**
4. **“Every compatible two-way splice has complexity (2s_1+O(n)).”**
5. **“Every high hybrid requires (Theta(\log N)) proof holes.”**
6. **“If one context rejects every alternative in a family of size (M), its overlap has size (Omega(\log M)).”**
7. **“(L) proof-tree leaves imply (L-1) distinct closure rules.”**
8. **“(Omega(N^\beta\log N)) is superlinear in (N) for OPS (eta<1).”**
9. **“(N\log N) implies (N^{1+\varepsilon}) for fixed (arepsilon>0).”**
10. **“Being multi-hole/non-local automatically bypasses the locality barrier.”**

These should be treated as audited dead ends unless a future proof supplies the missing hypotheses.

---

# 13. Recommended retained frontier

The Gemini audit leaves two useful concrete questions.

### A. High-diversity decoder branch

Given a C-125 map with

[
M\delta
\gtrsim
\operatorname{CycAnd}(f),
]

can one lower-bound its shared multi-output AND complexity from the geometry of the (M) selected witness restrictions?

A positive answer could genuinely close or exploit Route A.

### B. Native synchronization-versus-product theorem

Can one prove, for the **full** low-circuit class, that a (q=O(N)) native grammar must either:

- expose enough compatible owner-mask choices to generate a high table; or
- use a family of synchronization states whose representation cost exceeds (N), ideally (N^{1+\varepsilon})?

This must survive:

- parity locking;
- repeated-block equality fingerprints;
- simple cofactor patching;
- proof-tree sharing;
- arbitrary semantic endpoints.

---

## Final audited status

Gemini contributed one useful general decoder theorem and a clean formulation of multi-hole consistency. Its claimed superlinear fusion lower bound and P-vs-NP proof do not survive audit.

The correct project frontier remains:

[
\boxed{
\rho_{\mathrm{GapMCSP}}\ge N-o(N)
}
]

with the key unresolved problem still being **global witness coherence / shared-state synchronization**.
