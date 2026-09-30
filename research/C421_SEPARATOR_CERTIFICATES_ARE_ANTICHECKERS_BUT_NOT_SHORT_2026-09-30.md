# C-421 - A separator proof DAG yields an anti-checker, but not a short one

**Status:** proved certificate extraction for arbitrary fan-in-two separators, including unrestricted sharing. From a size-`S` separator `C` and any High table `f`, a uniform `O(S)`-gate extractor produces a coordinate mask `Q_f` with at most `min(N,2S)` positions; fixing those positions to `f` forces `C=0`, so no Low circuit agrees with `f` on `Q_f`. The proof is representation-independent and does not infer a circuit witness or enumerate circuits. Its length ceiling is still `N`, far above OPS's `N^(10 beta)` anti-checker scale for small fixed `beta`. No lower-bound frontier changes.

## 1. Target and certificate definition

Let `N=2^n`; use the OPS promise `s1=floor(N^beta/(10n))`, `s2=ceil(N^beta)`, with Low tables accepted and High tables rejected. The separator's output on the middle band is unrestricted. Fix any ordinary fan-in-two Boolean circuit `C` with `S` total gates, fixed basis, and free unrestricted fanout.

A 0-certificate for `f` is a coordinate set `Q subseteq [N]` such that every table `g` agreeing with `f` on Q satisfies `C(g)=0`. Since every Low table has `C(g)=1`, any such Q is an anti-checker against all circuits of size at most `s1`: a Low circuit agreeing with f on Q would be a completion on which C outputs both 0 and 1.

## 2. Proof-DAG extraction theorem

**Theorem.** There is a circuit `Extract_C` of `O(S)` fan-in-two gates that, on every input table `f` with `C(f)=0`, outputs an N-bit mask for a 0-certificate `Q_f` of size at most `min(N,2S)`. A fixed-length explicit address-list encoding can be produced with at most an additional `O(N polylog N)` gates; the mask representation itself is N output bits and does not charge N gates.

**Construction and proof.** First evaluate every gate of C on f. Starting from the output gate, traverse the gate DAG backward. At a marked gate v, let b be its evaluated output. Select a minimum subset of its at-most-two input pins whose evaluated values force v's output to equal b for every setting of the unselected pins. Such a subset always exists: fixing both inputs suffices. Mark the selected predecessor gates, or record the corresponding primary-input coordinates. If a shared gate is reached more than once, its evaluated value is the same on every route, and its predecessor certificate is computed once and reused.

Let Q_f be the distinct primary-input coordinates recorded. Inductively in the resulting acyclic marked subgraph, fixing Q_f to f's values forces each marked gate to its evaluated value, and hence forces the output to zero. Each marked gate contributes at most two selected pins, so there are at most `2S` recorded input occurrences and `|Q_f|<=min(N,2S)` distinct coordinates. Thus Q_f excludes every Low table, including every truth table of a circuit of size at most s1.

The extractor is a circuit, not a search procedure. It computes the gate values in one forward pass, then propagates marks in reverse topological order. Each gate uses constant-size logic to choose its certificate pins and aggregate marks from its fanouts; input-coordinate masks are ORed over the at most `2S` recorded occurrences. The total gate count is `O(S)` for a mask output (or `O(S+N polylog N)` if a particular explicit-list output format charges its N address slots). Fanout, output bits, and the list's description are kept separate from total gates.

## 3. Where this improves the frontier, and where it stops

This is an unconditional way to obtain an anti-checker from an arbitrary separator's *own computation*. It makes no assumption that the separator outputs a circuit description, evaluates all addresses separately, or stores caller history. The extracted object is a certificate for the separator's 0-region; it is stronger than needed for Low exclusion because it also rejects every completion in the separator's accepted-middle extension.

The length guarantee is only `min(N,2S)`. At the relevant lower-bound scale `S>=N-o(N)`, it can be N. OPS's Anti-Checker Lemma uses `t=2^(10 beta n)=N^(10 beta)` points and, under `NP subseteq Circuit[poly]`, constructs their selector in size `N^(1+k beta)`. For every sufficiently small fixed beta, `N^(10 beta)` is sublinear; C-421's generic certificate can be larger by `N^(1-10 beta)`. The extractor alone therefore does not enter the magnification reduction or yield a stronger lower bound.

A smaller certificate might be found by deleting coordinates while preserving `C=0` on the remaining subcube. For a fixed Q, validity says that the circuit obtained by fixing Q has no satisfying input, a coNP predicate. Existence of a valid Q of size at most t is therefore a Sigma2^P search relation. No near-linear circuit bound for that optimization follows from the extraction. In particular, simply citing the OPS anti-checker existence lemma does not show that its short set is a 0-certificate of this particular C: C may accept middle-band completions that the anti-checker is not required to reject.

## 4. Countertests

- **Parity:** a fan-in-two circuit of `O(N)` gates computes parity of the N table bits. At any zero-output input, every 0-certificate has all N coordinates, since leaving one bit free permits a completion of opposite parity. This rules out a general theorem that circuit evaluation certificates are sublinear. Parity is a calibration of the extraction mechanism, not a Gap-MCSP separator.
- **Repeated-block equality:** the predicate that all q block representatives agree has an `O(q)` circuit. A zero-certificate needs only a mismatching pair of representatives; repeated coordinates do not increase its size.
- **Sparse parity checks:** for a syndrome-zero predicate, a zero-output certificate can select one violated check and its support. A bounded-weight check uses a bounded number of input coordinates; computing all checks costs `O(nnz(H)+r)` gates.
- **Simple global relations:** a copy/XOR relation can be proved false by exposing one violated relation after the shared generator is evaluated once. No charge proportional to the number of repeated table uses follows.

These tests reject an unconditional short-certificate charge while preserving the exact proof-DAG theorem.

## 5. Paired full-promise construction attempt

The certificate extractor is a transformation from a hypothesized separator, not a new separator. For a direct upper bound, the exact construction still enumerates all descriptions of size at most s1, compares each complete truth table with the input, and ORs the equality tests. There are `2^(O(s1 log(s1+n)))=2^(O(N^beta))` candidates, so the total cost is `O(N 2^(O(N^beta)))` gates. It handles every promised Low and High input; no near-linear full-promise implementation was found.

## 6. Model, literature, and status audit

- **Total gates:** forward evaluation, mark propagation, and mask aggregation are all counted; every gate is in the fixed fan-in-two basis.
- **Sharing:** each DAG gate is evaluated and marked once; fanout does not duplicate its proof subgraph. The output certificate may still mention as many as N distinct table coordinates.
- **AND/OR/wires/descriptions/runtime:** no paid-AND surrogate is used. ORs used to combine marks count as gates. The N-bit mask is output length, not N gates; an explicit serialized address list has separate encoding cost. Circuit description bits and the runtime to print the list are not gate counts.
- **Promise:** only Low and High correctness is used; middle outputs are never presumed. In fact the extracted certificate controls the separator's actual output extension on middle tables, which may make it larger than an OPS anti-checker.
- **Prior literature:** OPS Theorem 1.4 and Anti-Checker Lemma 4.1 use a selector of `N^(10 beta)` sample points under `NP subseteq P/poly`; they do not state that an arbitrary separator's evaluation proof supplies that short selector. C-421 proves only the unconditional length-`N` certificate above. The locality barrier of Chen et al. is not implicated by this circuit-model certificate argument.
- **Originality:** the local forcing certificate for a circuit gate and backward proof propagation are standard circuit reasoning. The contribution here is the exact promise-separator consequence and its size audit; no new general circuit lower-bound theorem is claimed.

**Strongest proved statement:** every fan-in-two Gap-MCSP separator yields, with `O(S)` gates, an anti-checker mask of size at most `min(N,2S)` for each High input.

**Quantitative frontier: unchanged.** Ordinary lower bound remains `S>=N-O(N^beta log N)-1` plus C-406's additive logarithmic term; OPS `N^(1+epsilon)` remains open; native `rho_GapMCSP>=N-o(N)` remains separate. The mask-size bound can be `N`, not `N^(10 beta)`, so it gives no magnification or superlinear lower bound. Exact full-promise upper remains `O(N 2^(O(N^beta)))`.

**Next mechanism:** do not assume or rederive a short anti-checker selector from a certificate. The unresolved question is whether the endpoint set of an arbitrary separator admits a *small* zero-certificate on every High input despite unrestricted acceptance of middle tables, or whether some direct gate potential bypasses certificate minimization. Any answer must handle parity and the other countertests above.

### Primary sources

- Oliveira, Pich, Santhanam, [*Hardness Magnification Near State-of-the-Art Lower Bounds*](https://theoryofcomputing.org/articles/v017a011/), Theorem 1.4 and Anti-Checker Lemma 4.1.
- Chen et al., [*Beyond Natural Proofs: Hardness Magnification and Locality*](https://arxiv.org/abs/1911.08297), for the locality barrier scope.
- Project baselines: C-406 formula-to-DAG reconvergence and C-420 codeword-hard trace accounting.
