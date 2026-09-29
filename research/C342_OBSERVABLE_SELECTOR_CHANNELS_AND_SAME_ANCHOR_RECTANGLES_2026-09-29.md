# C-342 - Observable selector channels in the exact native game

Date: 29 September 2026  
Route: Q199 / turn the C-341 address-loss observation into an exact input/readout theorem.  
Classification: **SYNTHESIS OF C-281/C-306/C-319 + STATE-ONLY SELECTOR LOWER BOUND; NO GENERAL q IMPROVEMENT.**

## 1. Question

C-341 rules out a shared positional action as a way to return to the address that entered a shared state. That leaves a possible loophole: perhaps a global circuit description is carried either by a proof support or by the activation vector. This note identifies exactly what the native game can observe and proves that support provenance cannot maintain caller/description correlation on one fixed accepted table.

## 2. The seed-signature factorization

For a fixed native list Q with q pairs, let

```text
sigma_Q(w) = (A_1(w), B_1(w), ..., A_q(w), B_q(w)) in {0,1}^{2q},
```

where A_i and B_i are the two C-319 seed-clause truth values. Once this vector is fixed, the transition predecessor sets are fixed as well. Define y^0=0 and

```text
y_i^(t+1) =
  (sigma_Ei OR OR_{j in P_i^E} y_j^t)
  AND
  (sigma_Hi OR OR_{j in P_i^H} y_j^t).
```

The output is the OR of y_i^q over empty-consequence roots. Therefore there is a fixed Boolean map G_Q such that

```text
Accept_Q(w) = G_Q(sigma_Q(w)).
```

**Proof.** At round zero the activation vector is independent of w. If two tables have the same seed signature, their round-t activation vectors agree; substituting into the recurrence shows their round-(t+1) vectors agree. Induction through q rounds proves the claim. The same argument shows that the set of winning positional policies is determined by the seed signature and the fixed graph. A policy's choice is a certificate of why a state wins; it is not an output that another state can read.

Each signature coordinate is an OR of a fixed, consistent collection of signed input literals (or a constant for an all-universe endpoint). Thus the only input observations available to the graph are 2q such disjunctions. This is an exact factorization, not an information-theoretic lower bound: at q=N, unit-literal clauses can expose all N table bits.

### Fiber consequence

If Q accepts w, then every table w' with sigma_Q(w')=sigma_Q(w) is accepted. Soundness therefore forces

```text
sigma_Q^{-1}(sigma_Q(w)) subseteq SIZE(s2).
```

This fiber statement by itself gives no useful q lower bound. Rejected signature fibers may contain many high tables, and the crude ratio `|SIZE(s1)|/|SIZE(s2)|` is below one. The linear policy-CNF bound in C-334 uses more structure than this partition. The important consequence here is architectural: any *readable* circuit selector implemented by this graph must be a function of sigma_Q(w). A strategy choice by itself cannot carry the selected description to another state.

## 3. Same-anchor context/proof rectangles

Fix one accepted table w and one state i. Let K_i(w) be any family of outside-context supports from accepting derivations with a marked occurrence of i, and let P_i(w) be any family of finite proof supports rooted at i, with every support in both families matched by w.

Every such support is a subset of the one-sided literal set ell(w). Hence, for every K in K_i(w) and P in P_i(w), K union P is consistent. By the C-281 substitution law, plugging P into K gives an accepting proof. Soundness then gives

```text
Cube(K union P) subseteq SIZE(s2)  for every (K,P) in K_i(w) x P_i(w).
```

So a reused state does not preserve an observed matching between a caller context and one particular proof payload. It exposes the full same-anchor Cartesian product. In particular, support provenance cannot be used as an exclusive address/description register: if two payloads both match w, the state must tolerate either payload with every context at that state. A proposed encoding may survive this only if all those cross-completions are low, or if its proof does not actually place the corresponding context and payload at a shared state.

This is the precise splice form of the C-341 obstruction. It does not say that supports carry no information at all; they carry partial assignments and compatibility can detect opposite literals. It says that compatibility cannot distinguish two proof payloads that both match the same anchor, because they are then automatically compatible.

## 4. Selector-channel trichotomy

The exact model now has three possible ways a circuit description could influence address checks:

1. **Path/caller history.** Unavailable after two histories merge at one state; continuation depends only on the state and seed signature (C-341).
2. **Proof-support provenance.** Not an exclusive channel on one accepted anchor; same-anchor context/proof substitution creates a full safe rectangle (C-281/C-306 and Section 3 here).
3. **Readable state values.** Still possible. Any selector must be encoded in the seed signature and/or the resulting activation vector, and every address-check state must read that code through its fixed predecessor incidence. The code cannot be written by choosing a positional action. If a description d is already explicitly stored in the table, two marker states per description bit can expose a one-hot pair `D_(j,0),D_(j,1)`; predecessor incidence can then test either value. For arbitrary low tables the missing step is to *select and activate* one globally valid d. The activation vector is deterministic from sigma, so this selector must be a canonical/input-determined function of w, not an unobservable existential choice.

This corrects an overly broad “the game has no memory” description. A q-bit activation profile can carry up to q raw bits, and the 2q seed signature can carry up to 2q input-derived bits. At q around N, raw capacity is not the obstacle. The unresolved cost is **coherent readout**: how a fixed q-state graph uses a globally selected description while each address check evaluates the appropriate local behavior, without a gate-by-address product and without accepting a high cross-splice.

## 5. Residual-context test on a multiplexer

Here is the precise Myhill-Nerode-style test for a proposed shared-subroutine verifier. Let c be a context that enters state v, and let `R_c(d)` be the required Boolean answer of the continuation for description d. If after entry the graph has no return edge or other caller-dependent continuation, the residual behavior is a function `R_v(d)` of v and d alone. Therefore contexts c,c' may share v only if

```text
R_c(d) = R_c'(d) for every description d under consideration.
```

If a specified verifier architecture requires a set C of such residual queries, it needs at least the number of distinct functions in `{R_c : c in C}` continuation states. This is a valid state-capacity theorem for that architecture; it is not a lower bound on arbitrary native covers, which need not materialize these residual queries.

**Multiplexer calibration.** For `Mux(d,a)=d_a`, the address-a residual is `R_a(d)=d_a`. For a not equal to a', choose d with d_a=1 and d_a'=0; hence these N residual functions are pairwise distinct. A shared address-free mux continuation cannot answer all N queries; this explicit verifier needs N address-distinguishable continuation states. For a circuit-evaluation architecture, the analogous candidate family is `R_(g,a)(d)`, with one residual per gate/address pair. If those functions are pairwise distinct, that architecture needs the full product number of residual states.

The last sentence is conditional twice: one must exhibit a succinct low-circuit family with many distinct residual functions, and one must prove an arbitrary valid native cover induces those functions. The multiplexer example validates the state-memory diagnosis but does not establish either premise for the full Gap-MCSP cover.

### Many low descriptions defeat a path-only register

The residual count can be made much larger than N for the exact circuit-description verifier. Let `s=s1`, and take `r=floor(s/(3n))`. For each r-element subset A of the N addresses, let `f_A` be the indicator of A, written as an OR of r address minterms. Sharing the n input negations, this takes at most `n+r(n-1)+(r-1) <= n+rn <= s` gates for sufficiently large N. These functions are pairwise distinct. Moreover,

```text
M = binomial(N,r) >= (N/r)^r,
log2 M >= r log2(N/r) = Omega(s1)
```

for each fixed `0<beta<1` at OPS scale, since `r=Theta(N^beta/(log N)^2)` and `log(N/r)=Theta(log N)`. Thus `M=2^(Omega(s1))=N^omega(1)`.

If an architecture commits to one selected `f_A` solely by its current graph position and then checks the full table, the continuation from that position must compute `Eq_A(w)=[w=TT(f_A)]`. Distinct A give distinct residual predicates: choose an address in the symmetric difference and a table agreeing with one function there. Histories that merge at one state have identical continuation predicates, so every A needs a distinct post-selection state. This path-only exact verifier therefore requires at least `M` states, superpolynomially more than the OPS target range.

**Scope.** This lower bound applies when the chosen circuit is stored only in the current state/history and the continuation verifies exact agreement. It does not apply if the choice is encoded in the input-derived activation profile, if supports provide a different sound global coupling, or if a native cover accepts by certificates unrelated to a circuit-by-circuit equality verifier. C-342's earlier channel analysis rules out support provenance as a private same-anchor register, but does not rule out activation-code readout.

## 6. Conditional state-capacity criterion

Suppose a future verifier reduction assigns to each required address/configuration context a context support K_a at state i, and to each candidate description d a proof support P_d at the same state. If all these supports match one anchor w, then the realized relation contains the full rectangle

```text
{a : K_a in K_i(w)} x {d : P_d in P_i(w)}.
```

If a hybrid completion h(a,d) is high for any pair in that rectangle, Q is unsound. Therefore every rectangle induced at a shared state must have only low hybrid completions. If one can prove that the forced address/description relation of an explicit low family needs more than N*g(N) such sound rectangles, and also prove that every valid Q induces a cover of that relation, then q >= N*g(N).

The second premise is the missing one. An arbitrary C-319 cover need not evaluate a circuit gate-by-gate; it can use a different cube/policy certificate. Thus the selector matrix by itself does not yet imply any q bound. No monochromatic-rectangle or communication lower bound has been transferred to the full native cover.

## 7. Adversarial checks and literature boundary

- **C-257 parity:** it remains possible for all compatible cross-completions to lie in the parity promise. Rectangularity alone does not force a high output.
- **C-258 repeated equality:** shared descriptions can generate many local rows while a linear cover stays sound. Distinct rows or raw product count are not enough.
- **C-336/C-337:** an independent block product can contain high tables, but a near-linear restricted activity selector can avoid that product. A q-charge still needs the obligation to cover every low table.
- The 2026 monotone-learning result of Cavalar, de Rezende, Gray, and Santhanam establishes rETH-conditional hardness for monotone learning and partial labelled-example circuit-size approximation; it does not provide an unconditional full-truth-table C-319 selector lower bound. See the [primary arXiv paper](https://arxiv.org/abs/2607.12331). The magnification target and its quantifiers remain those of [OPS Theorem 1.4](https://www.theoryofcomputing.org/articles/v017a011/).

## 8. Status and next proof obligation

C-342 combines three exact facts: observable behavior factors through 2q seed tests, same-anchor support reuse is rectangular, and merged states have one residual continuation function. The multiplexer gives the simplest example; counting small indicator functions strengthens the path-only verifier lower bound to `2^(Omega(s1))`. Among these explicit channels, input-derived seed/activation readout remains possible. This does **not** establish a state-capacity theorem for arbitrary covers or produce a near-linear full-promise cover.

**Novelty boundary.** The seed-signature factorization is an immediate reformulation of C-319, and the same-anchor product law is already present in C-281/C-306. The new quantitative result is restricted to path-only exact circuit selectors: their residual-state count is at least `2^(Omega(s1))`. The contribution does not extend this lower bound to arbitrary covers and is not a general q theorem.

The next valid advance must do one of the following:

1. Construct a readable, input-derived selector code (or a different global mechanism) and prove its all-input C-281 soundness, with an explicit total q bound; or
2. Build a low-circuit family plus a reduction from arbitrary valid Q to a safe-rectangle cover, then prove that cover needs N*g(N) rectangles for an unbounded g.

The second route must prove the reduction from Q's arbitrary proof grammar; it may not assume that Q evaluates the chosen circuit. The actual bound remains `rho_GapMCSP >= N-o(N)`. No P-vs-NP conclusion follows.
