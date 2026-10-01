# C-444 — Feasible-interpolation audit and proof-certified high subfamilies

**Date:** 1 October 2026  
**Status:** one direct certificate route is quantitatively ruled out; a promise-preserving NP-subfamily reduction is formalized. No Gap-MCSP separator lower bound follows.

## 1. Object and exact formula

For a table `T` of length `N=2^n`, define the quantified circuit-consistency formula

```text
Φ_T := exists description d of a fan-in-two circuit of size at most s2,
       for every a in {0,1}^n, Eval(d,a)=T[a].
```

The description length and the evaluation relation are polynomial in `N`; the address block has only `n=log N` bits. `T` is NO exactly when `Φ_T` is false. Equivalently,

```text
YES(T) iff exists d, |d|<=s1, for every a: Eval(d,a)=T[a],
NO(T)  iff for every d, |d|<=s2, there exists a: Eval(d,a)!=T[a].
```

The YES endpoint is in NP and the NO endpoint is in coNP. The free middle band remains essential.

## 2. Direct mismatch-list certificates do not fit NP

A natural proposed NP witness for NO is one mismatch address for every circuit description of size at most `s2`. This direct witness is too long.

Let `s=s2=N^β` for any fixed `0<β<1`, and let `D_s` be the syntactic, topologically ordered circuit descriptions. Restrict to circuits where each gate after the first takes the preceding gate as its first input, and chooses its second input from the earlier wires. This makes every gate structurally feed the output. At gate `j`, there are at least `j` choices for that second input, so

```text
|D_s| >= product_{j=2}^s j = s! = 2^{Ω(s log s)}.
```

A list containing one `log N`-bit mismatch address for every such description has length at least `2^{Ω(N^β log N)} log N`, which is superpolynomial in `N`. This refutes the explicit all-descriptions certificate, not every possible compression.

Indeed, the logarithm of that witness length is `Θ(s log s)=Θ(N^β log N)`. For fixed `β>0`, this eventually exceeds `k log N` for every fixed polynomial degree `k`, proving superpolynomial length directly.

A circuit `H(T,d)` can scan all `N` addresses and return the first mismatch, or a sentinel if none exists; its size is polynomial in `N` for fixed `β`. But giving the description of `H` is not a certificate of NO: checking that it returns a genuine mismatch for **every** `d` is the same universal condition. The efficient per-description selector does not remove the quantifier.

## 3. A sound NP subfamily of NO tables

Although NO itself has no known NP certificate, one can isolate high tables whose lower bound has a short sound proof. Fix any sound QBF proof system `P` with a polynomial-time proof checker and a polynomial bound `q(N)`. Define

```text
W_{P,q} = { T : there is a P-refutation of Φ_T of length at most q(N) }.
```

`W_{P,q}` is an NP language: the refutation is a polynomial-length certificate and the proof checker verifies it in polynomial time. Soundness gives `W_{P,q} subseteq NO`, and because `s1<s2`, `W_{P,q}` is disjoint from YES.

Let `SepCC(A,B)` be the minimum total fan-in-two circuit size separating `A` from `B`. Every full Gap-MCSP separator also separates YES from `W_{P,q}`. Therefore

```text
SepCC(YES, NO) >= SepCC(YES, W_{P,q}).
```

**Proof:** every circuit satisfying the full promise satisfies the weaker label requirements on the subset `W_{P,q}`. The circuit family for the full promise is contained in the family for the subpair, so its minimum size is no smaller. Consequently, a lower bound for this particular disjoint NP pair would transfer to every separator extension, without assuming the separator outputs a witness.

This gives a precise alternate entry point for proof complexity: construct a sound, efficiently checkable proof-certified high subfamily and prove that it is hard to separate from the Low tables. It is only a framework. `W_{P,q}` could be empty or easy, and no superlinear lower bound for `SepCC(YES,W_{P,q})` is known.

## 4. Why standard feasible interpolation is not yet that lower bound

Feasible interpolation extracts a separator circuit **from a short refutation** of an unsatisfiable formula split into two disjoint witness relations. It does not convert an arbitrary small separator circuit into a short proof. The desired implication here would need the reverse direction, or an independent lower bound for the pair in Section 3.

The direct full-promise encoding also fails the usual pair hypotheses: YES has an NP witness, while NO is coNP. To place NO itself in an NP pair by listing mismatches requires a superpolynomial-size list; a succinct selector still needs a proof of its universal correctness. Müller and Pich study succinct tautologies expressing circuit lower bounds, including anti-checker formulations, and prove feasible formalizations for restricted lower-bound methods. Those results do not certify every high table here or lower-bound unrestricted ordinary separators. [Müller–Pich, ECCC TR17-144](https://eccc.weizmann.ac.il/report/2017/144/download)

QBF proof-complexity work also transfers circuit lower bounds into proof-size lower bounds using strategy extraction. That direction is useful background but does not furnish the reverse separator-to-proof compiler required for this target. [Beyersdorff, Bonacina, and Chew](https://eprints.whiterose.ac.uk/id/eprint/91400/)

## 5. Counterchecks and precise status

Parity, repeated-block equality, sparse parity checks, and simple global block relations still have `O(N)` shared implementations. They do not refute the proof-certified-subfamily lemma: if any such table has `CC(T)<=s2`, soundness prevents it from entering `W_{P,q}`. They do refute any attempt to infer superlinear work merely from the number of constraints or potential mismatch sites.

Counting shows that many tables are High, but it does not show that those individual tables have short QBF refutations. Conversely, a proof system with short proofs for a useful family would only create the NP subfamily; the circuit lower bound for separating that family from YES remains a separate theorem. No assumption that a separator reconstructs a description or mismatch list is used.

## 6. Next action

Retire direct standard feasible interpolation as a route to the ordinary OPS bound unless a separator-to-proof reduction is supplied. Keep the proof-certified subfamily as the live logic candidate. The next meaningful test is to instantiate `P` (for example, a named QBF proof system), give an explicit family of tables `T` with polynomial-size sound refutations of `Φ_T`, and then either prove `SepCC(YES,W_{P,q})>N^(1+ε)` for the OPS quantifiers or exhibit a small shared separator. If the proof family cannot be shown both nontrivial and separator-hard, retire it.

**Frontier unchanged:** ordinary `N-O(N^β log N)-1` plus C-406 refinement; OPS `N^(1+ε)` open; exact full-promise separator `O(N·2^{O(N^β)})`; native `ρ≥N-o(N)` separate. The result here is a route-specific certificate-size calculation and a reduction lemma, not a circuit lower bound.

### Primary sources checked

- [Oliveira, Pich, and Santhanam, Theorem 1.4](https://theoryofcomputing.org/articles/v017a011/v017a011.pdf).
- [Müller and Pich, Feasibly Constructive Proofs of Succinct Weak Circuit Lower Bounds](https://eccc.weizmann.ac.il/report/2017/144/download).
- [Beyersdorff, Bonacina, and Chew, Lower Bounds: From Circuits to QBF Proof Systems](https://eprints.whiterose.ac.uk/id/eprint/91400/).
- [Feasible interpolation overview](https://eccc.weizmann.ac.il/report/2017/106/download/).
