# C-306 - Compatible proof supports cannot act as an address-control register

Date: 28 September 2026  
Classification: **SCOPED NO-GO / CORRECTION TO C-305'S COMPRESSION CANDIDATE.** The C-281 supports can record which literals a proof uses, but they cannot make a reused state respond conditionally to that support. On one anchor all matching supports are mutually compatible, and the activation recurrence forgets support contents. This kills the specific proposal to use support compatibility as the address register in a universal-circuit game. It is not a lower bound for arbitrary native covers.

## 1. Diagonal compatibility lemma

For a complete table w, let `ell(w)={(k,w_k):k in [N]}`. Fix a rule state i. Let `K_i(w)` be the context supports rooted at i that match w, and `P_i(w)` the replacement proof supports rooted at i that match w.

**Lemma.** For every `K in K_i(w)` and `P in P_i(w)`, the union `K union P` is consistent and matches w.

**Proof.** Matching means `K subseteq ell(w)` and `P subseteq ell(w)`. Their union is therefore a subset of the consistent full support `ell(w)`. QED.

By the C-281 substitution law, every such pair gives an accepting output proof, and soundness puts the whole cylinder of `K union P` inside `SIZE(s2)`. In particular, for one fixed anchor w, the context/proof compatibility matrix at state i is complete bipartite: it contains every pair in `K_i(w) x P_i(w)`. No two support annotations for different internal address branches can be made incompatible while they both match this same table.

## 2. The state transition cannot read the support annotation

The actual activation recurrence for state i is a Boolean equation in:

1. whether at least one fixed seed literal matches w on the left;
2. whether at least one fixed seed literal matches w on the right; and
3. which predecessor state bits are active.

It does not inspect which support or proof tree activated a predecessor. The antichain support is provenance for the derived carrier, not mutable state visible to the next rule. Hence putting an address tag into K or P does not make a shared native state choose a different transition for different tags. Since all tags that are true in w are pairwise compatible, splice consistency cannot restore that missing conditional read.

## 3. Consequence for the stationary-circuit-strategy proposal

The desired low-table predicate has the quantifier pattern

```text
exists one description d, for every address x, C_d(x)=w_x.
```

A gate-address game with a separate choice of description at each address can instead certify

```text
for every address x, there exists a description d_x with C_(d_x)(x)=w_x,
```

which is vacuous: a constant-zero or constant-one circuit can match each individual table bit. To keep one d across all x, an address-dependent subproof must be conditioned on a shared description choice. C-306 shows that a support annotation alone cannot provide this conditioning at a shared state: the state sees only its active bit, while all same-anchor support combinations remain compatible.

Therefore the C-305 proposal cannot be repaired just by declaring proof supports to be an address register. A viable construction must enforce the common description through the **state-level activation pattern itself**, or use a different global semantic object that does not implement per-address circuit evaluation. The straightforward explicit gate-address product still costs `Theta(Ns1)=N^(1+beta-o(1))`.

## 4. Scope and next target

This is not a generic lower bound on q. It does not rule out a compact monotone separator for the gap promise, nor does it rule out a proof that every successful native grammar has a unique low-description policy encoded by its fixed state graph. It rules out the support-only control-memory mechanism proposed after C-305.

C-258's repeated-block cover remains consistent with the lemma: it uses fixed prefix/equality carriers to recognize a special product code; it does not make support metadata alter a state's transition. C-257 parity likewise confirms that every support pair on one anchor can splice safely while a linear cover handles the promise.

The next O-168 attempt must either construct a state-level global selector with a near-linear number of states, or prove that representing a coherent description selector requires superlinear q. Do not continue developing support tags as a control register. Actual q remains `N-o(N)`; no full-promise cover or P-vs-NP proof follows.
