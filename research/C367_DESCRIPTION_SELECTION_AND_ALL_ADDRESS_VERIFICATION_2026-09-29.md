# C-367 - Description selection and all-address verification are separate costs

Date: 29 September 2026  
Route: Continue the C-341 description/address-multiplexing question using the exact C-319 input/readout model.  
Classification: **EXACT SEARCH-THEN-VERIFY DECOMPOSITION; STANDARD VERIFIER COST IS SUPERLINEAR; NO NEW q LOWER BOUND.**

## 1. The precise task a circuit witness would solve

Put \(N=2^n\), \(s=s_1=N^\beta/(c\log N)\), and let \(d\) encode a Boolean circuit of at most \(s\) gates. Let \(U_s(d,x)\) be a universal evaluator, with description length and one-address evaluation size \(O(s\log s)\). Consider

\[
\operatorname{Eq}_{n,s}(d,w)
=
[d\text{ is valid}]\wedge
\bigwedge_{x\in\{0,1\}^n}[U_s(d,x)=w_x].
\]

This is the *all-address checker*: the candidate description is already supplied, and the output says whether it computes the explicit truth table \(w\).

If a circuit \(S\) maps every \(w\in\mathrm{SIZE}(s)\) to a valid description \(d=S(w)\) of a size-\(s\) circuit computing \(w\), then

\[
F(w)=\operatorname{Eq}_{n,s}(S(w),w)
\]

is a sound separator: it accepts every size-\(s\) table and accepts no table outside size \(s\), hence in particular rejects every table of complexity greater than \(s_2\). The standard direct construction has size

\[
|S|+O(Ns\log s).
\]

At the OPS parameters, \(s\log s=\Theta_\beta(N^\beta)\), so this is \(|S|+O_\beta(N^{1+\beta})\). This computes a stronger exact-membership predicate than the promised gap separator. It does not meet a near-linear target.

The two costs are logically distinct:

1. **selection:** compute a valid description from the whole table;
2. **verification:** compare that one description against all \(N\) table entries.

The first is MCSP search/readout. The second is the address-multiplexing problem. A decision cover need not perform either operation separately.

## 2. Why the naive state product appears, and why it is not a lower bound

The direct verifier evaluates the selected circuit at every address. For each address it uses a universal circuit of size \(O(s\log s)\), giving \(O(Ns\log s)\) gates. In the C-319 game, making every intermediate gate value separately available at every address uses an address-by-gate product. C-341 explains why a shared positional configuration state cannot return to its caller; C-349 explains why a chosen circuit's local OR witnesses are representation-dependent.

Those facts explain the cost of the *explicit trace architecture*. They do not prove that \(\operatorname{Eq}_{n,s}\) needs that many gates. A Boolean circuit has one output, while the \(Ns\) gate/address values are only an intermediate representation. A different computation could compress them. The only immediate general circuit lower bound here is \(\Omega(N)\): after fixing \(d\) to any valid description, equality with its truth table depends on each of the \(N\) input bits \(w_x\), so a bounded-fanin circuit needs at least \(N-1\) gates. No \(\Omega(Ns^\delta)\) lower bound for this checker has been established.

Thus the correct statement is not “all-address verification inherently costs \(Ns\).” It is:

\[
\boxed{\text{The known direct verifier costs }O(Ns\log s);
\quad\text{a sub-}Ns\text{ exact checker is an open compression target.}}
\]

Any proposed compression must work for every description \(d\) and every explicit \(w\), including adversarial high tables. There is an exact lower bound for all deterministic linear-sketch verifiers. Fix a low table \(f\). Along its accepting transcript, suppose the verifier learns \(r\) independent binary linear constraints on \(w\). The tables giving the same transcript form an affine subspace of size \(2^{N-r}\). If

\[
N-r>\log_2|\mathrm{SIZE}(s_2)|=O(s_2\log s_2)=o(N),
\]

then the transcript fiber contains a table \(z\) of complexity greater than \(s_2\). It has the same answers as \(f\), so an adaptive deterministic verifier follows the same branch and accepts \(z\), contradicting soundness. Therefore the transcript must reveal rank at least

\[
r\ge N-\log_2|\mathrm{SIZE}(s_2)|=N-O(s_2\log s_2)=N-o(N).
\]

Coordinate queries are the special case in which each answer gives at most one independent bit. A multilinear-extension evaluation at a fixed field point is linear in the truth-table vector; a field-valued answer contributes at most \(\log_2|F|\) binary rank bits. Thus deterministic exact fingerprint schemes based on fewer than \(N-o(N)\) independent linear measurements cannot certify equality against all high tables. Randomized fingerprinting is not covered, and a general nonlinear map is not ruled out by its output length alone: it could isolate the candidate, but computing that map is already the equality/separation problem.

This remains only a linear information lower bound, not a superlinear circuit lower bound, and it does not cover C-319's arbitrary ORs of signed literals as measurements.

### Low-degree transcript theorem

The same proof extends beyond linear measurements. Suppose a deterministic adaptive fingerprinting verifier, on the accepting path for a fixed low table \(f\), receives \(t\) Boolean answers \(\phi_1(w),\ldots,\phi_t(w)\), where the query chosen at each step may depend on previous answers. Let \(d_i\) be the algebraic degree over \(\mathbb F_2\) of the answer function chosen along \(f\)'s path, and put \(D=\sum_i d_i\).

For each answer define

\[
R_i(w)=1+\phi_i(w)+\phi_i(f).
\]

Then \(R_i(w)=1\) exactly when that answer matches the answer on \(f\). The product \(R(w)=\prod_i R_i(w)\) is the indicator of the full transcript fiber: it is 1 precisely on tables that follow the same adaptive path and receive the same answers. It is a nonzero Boolean polynomial because \(R(f)=1\), and its degree is at most \(D\).

The minimum-distance theorem for the binary Reed-Muller code says that every nonzero Boolean polynomial of degree at most \(D\le N\) is 1 on at least \(2^{N-D}\) inputs. One proof is induction on \(N\): write \(R=R_0+x_N R_1\). If \(R_1=0\), the support doubles that of \(R_0\); otherwise every assignment with \(R_1=1\) contributes exactly one 1 across the two choices of \(x_N\), and \(\deg R_1\le D-1\). Thus the transcript fiber has size at least \(2^{N-D}\). Soundness forces that fiber to contain no table above size \(s_2\), so

\[
D\ge N-\log_2|\mathrm{SIZE}(s_2)|
=N-O(s_2\log s_2)
=N-o(N).
\]

This is a degree-budget theorem, not a gate-count theorem. It rules out deterministic exact fingerprint interfaces whose total answer degree is below \(N-o(N)\), including linear/multilinear-extension sketches as the degree-one case. A circuit may instead compute a nonlinear, high-degree predicate directly; the result neither lower-bounds that circuit nor applies to C-319's unrestricted OR-of-literals feature map, whose individual degree may be N.

A short *linear* fingerprint also has a nontrivial kernel and can collide with a high completion; the fixed-query counting argument gives this directly for coordinate samples. A general nonlinear map to a short output is not ruled out by its output length alone: it could isolate the candidate, but computing such a map is already the equality/separation problem.

## 3. Connection to the native state graph

For a fixed C-319 list \(Q\), the table is observed through the \(2q\) signed-literal seed values \(\sigma_Q(w)\), and its least-fixed-point activation vector is a deterministic function of that signature. A positional strategy is not an output wire. Hence a circuit description encoded by activation bits would need a specified decoder from the signature/activation vector; it cannot be read directly from an existential choice at a shared state.

If such a decoder of size \(r\) did output \(d(w)\) on every low table, then the explicit search-then-verify circuit above would have size at most

\[
O(q(N+q)+r+Ns\log s),
\]

using the safe ordinary-circuit size \(O(q(N+q))\) for computing the C-319 seed tests and unrolling its fixed point. The \(O(q^2)\) bound applies only to the paid-AND measure when unbounded ORs are free. This is a conditional consequence, not an extraction theorem: arbitrary sound covers need not encode descriptions at all. Ren-Santhanam's relativized decision/search separation, recorded in C-366, is a direct warning against inferring this decoder from acceptance.

This sharpens the C-341 question. A valid construction may:

- provide an input-derived, globally coherent description decoder and compress the exact all-address checker;
- avoid descriptions and directly compute the promised decision predicate in the native readout; or
- use proof supports, in which case C-281 same-anchor products still impose full cross-compatibility.

The first option has enough raw storage at \(q=\Theta(N)\), but neither the decoder nor a sub-\(Ns\) checker follows from that capacity. The second and third options remain open.

## 4. What was actually learned

- The standard circuit-witness route factors into a search map and an all-address equality check; neither should be conflated with native decision acceptance.
- A gate-by-address trace is an upper-bound architecture, not a universal lower-bound certificate.
- The exact checker has an \(\Omega(N)\) input-dependence floor and an \(O(Ns\log s)\) direct upper bound. This leaves a large, explicit circuit-complexity question.
- Deterministic adaptive Boolean-polynomial fingerprints need total answer degree \(N-o(N)\), by applying Reed-Muller minimum distance to the transcript fiber. This closes low-degree algebraic compression below that budget, but is not a gate or native-state lower bound.
- This audit does not exceed the proved native lower bound \(\rho_{\mathrm{GapMCSP}}\ge N-o(N)\), construct a full-promise near-linear cover, or prove \(P\ne NP\).

## 5. Next concrete proof target

Study \(\operatorname{Eq}_{n,s}\) itself under ordinary bounded-fanin circuit size:

1. Can its universal evaluation be compressed to \(N^{1+o(1)}\) gates by an exact algebraic, transform, or shared-readout construction?
2. Can one prove a superlinear lower bound that is strong enough at \(s=N^\beta/(c\log N)\)?
3. If neither applies, can the native seed-signature/support grammar decide the Gap promise without implementing \(\operatorname{Eq}_{n,s}\)?

The third question is essential: a lower bound for this witness-checking architecture is not automatically a lower bound for arbitrary C-319 covers. The actual q checkpoint remains \(N-o(N)\); no breakthrough is claimed.
