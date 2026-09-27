# Research reset and route choice — 25 September 2026

## Reconstructed state

### Strongest rigorously established results

- **Published route:** OPS Theorem 1.4 turns a slightly-superlinear arbitrary-circuit lower bound for the prescribed Gap-MCSP promise into \(NP\not\subseteq P/poly\), hence \(P\ne NP\).
- **Project lower bound:** the current semi-filter/cover argument gives only \(N-o(N)\) gates. No superlinear arbitrary-circuit bound is proved.
- **Selector existence:** for each high table, minimax and sampling give a short valid anti-checker list. This is pointwise existence \(\forall f\,\exists Q\), not a circuit selecting Q for all high tables.
- **Selector lower bound baseline:** every valid selector depends on \(N-o(N)\) truth-table inputs; local patching and dual margin also constrain list length and simple encodings. No \(N^{1+\delta}\) selector lower bound is proved.
- **Transfer audits:** C-58–C-62 rule out common-list local payloads, the simple disjoint-region/mux gadget, many mandatory disjoint regions, and parity-padding arguments that count shared dual-heavy changes as independent.

### Dependency graph

```text
OPEN O-1: arbitrary-circuit Gap-MCSP lower bound N^(1+epsilon)
  -> OPS Theorem 1.4
  -> NP not-subset P/poly
  -> P != NP

Separate sufficient route:
ASSUME NP subset P/poly
  -> OPS gives a near-linear anti-checker selector for small beta
  -> OPEN S-1: every valid selector on all high tables needs N^(1+delta)
  -> contradiction
  -> P != NP

Inside either route:
pointwise short-list existence (proved)
  -> OPEN: uniformly select a valid list with a small circuit
```

### First unresolved statement and classification

The first open node on the shortest path is O-1 itself. It is a major unrestricted circuit lower bound, not a technical transfer lemma. The nearest constructive target is S-1, or equivalently the adversarial-completion statement: for each candidate selector circuit S, find a high table f and low circuit D with D agreeing with f on every address output by S(f). S-1 is a separate sufficient route; no equivalence with O-1 has been proved.

## Attack on the selected target: agreement fibers

For a fixed selector S and low circuit D, define

\[
A_D^S=\{f: \forall a\in S(f),\ f(a)=D(a)\}.
\]

S is valid on every high table exactly when \(A_D^S\subseteq SIZE(s_2)\) for every \(D\in SIZE(s_1)\). The adversarial-completion target is therefore exactly: for every proposed small S, some one of its low-circuit agreement fibers contains a table outside \(SIZE(s_2)\).

Membership in \(A_D^S\) has a circuit of size

\[
O\bigl(|S|+t(N+s_1+n)\bigr),
\]

by computing S's at most t addresses, multiplexing the corresponding input-table bits, evaluating D at those addresses, and comparing. At OPS parameters the overhead is \(N^{1+10\beta}\) (up to lower-order terms). This translates selector failure into a precise circuit-supported-fiber question, but does not prove that any fiber contains a high table.

### Adversarial falsification

There is no class-independent theorem that every such agreement fiber contains a hard target. On a domain of N points, take the low class \(C=\{0^N,1^N\}\), and let S output one zero-labeled and one one-labeled position on every nonconstant table. Then S is a valid selector for all nonconstant tables, while the two agreement fibers are exactly the two constant tables. S has an \(O(N)\)-gate priority-encoder implementation. Thus any proof must exploit specific structure of the full small-circuit class; class size, short witness length, and dual-margin sampling alone cannot force a hard point into an agreement fiber.

## Fundamentally different routes considered

1. **Direct O-1 lower bound.** Shortest formal path, but this is already the major open lower bound. Continue only with a new semantic invariant or construction that yields a superlinear bound for arbitrary circuits.
2. **S-1 / agreement-fiber adversary — selected active attack.** It exposes the exact quantifiers and avoids hiding the issue in a reduction. The generic version is false by the two-constant-class example; the next step must use circuit-class closure, counting, or a self-consistency property absent from arbitrary concept classes.
3. **Kannan-style hard-language transfer.** C-58–C-62 identify concrete obstacles: common witnesses, patch-switching, mandatory-region mass, decoder dependence on x, and exponent loss. No all-valid-output reduction survives these checks.
4. **Bounded-arithmetic / KPT extraction.** The needed generator correctness and EF lower bound remain separate unproved premises; flattening adaptive witnesses is not justified.
5. **Diagonalization and self-reference.** The fixed NP-verifier exponent cannot simulate diagonal targets whose polynomial exponent grows with the enumerated machine. Padding has not repaired the membership bound.
6. **Generic hypergraph, VC, or sampling arguments.** The margin proves a short witness exists, but does not give a circuit-efficient Skolem function. C-61 limits mandatory regions; the toy class above shows generic set-system structure is insufficient.

## Route choice and next attack

Keep O-1 as the formal primary goal, and use S-1's agreement-fiber formulation as the next proof attack because it names a concrete counterexample object for every candidate selector. First investigate whether small-circuit closure under patching forces a large agreement fiber, while stress-testing priority encoders, shared parity, and input-dependent addresses. A theorem about the selector's architecture alone is insufficient unless every arbitrary circuit S is covered.

**Status:** no proof-level breakthrough. `CANDIDATE_PROOF.md` remains empty. The active target is substantially more explicit, but its crucial high-member lemma is open and appears to encode a major circuit lower bound.
### Additional adversarial quantifier check (C-64)

A fixed low circuit D is too weak an adversary: a priority encoder finds a mismatch in O(N) gates, and a fixed menu of m circuits is handled in O(mN). Hence the high completion in C-63 must evade the selector's simultaneous handling of the full low-circuit class. This rules out one-baseline patch arguments without claiming a lower bound for the full class.