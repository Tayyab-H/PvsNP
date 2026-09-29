# C-335 — Native internal states outrun monotone span programs; output remains the barrier

Date: 29 September 2026  
Route: Q195 / test whether empty-root output plus promise soundness admits a native-specific span-program bridge.  
Classification: **INTERNAL-STATE SEPARATION + EMPTY-ROOT BARRIER; NO ACTUAL Gap-MCSP RESULT.**

## 1. A concrete counterexample to a generic compiler

Consider the abstract q-state least-fixed-point recurrence

\[
x_i^{t+1}=
(a_i\vee\bigvee_{j\in P_i}x_j^t)
\wedge
(b_i\vee\bigvee_{j\in R_i}x_j^t),
\]

where the predecessor sets are fixed and the seed predicates are positive input variables or constants. This looks close to the state equation in C-319, but it omits the semantic requirement that predecessor sets arise from endpoint containment.

Use the monotone function GEN_n. Its input is a set of triples \(T\subseteq[n]^3\); point 1 is initially generated, and a point \(w\) becomes generated when the input contains a triple \((u,v,w)\) whose two antecedents have already been generated. The output is whether n is eventually generated.

There is a direct abstract recurrence with \(O(n^3)\) states:

1. A point state \(p_1\) is the constant 1.
2. For every possible triple \(e=(u,v,w)\), create a state \(r_e\) with seeds \(a_e=x_e,b_e=0\), and predecessor sets \(P_e=\varnothing,R_e=\{p_u\}\). It computes \(x_e\wedge p_u\).
3. Create a state \(s_e\) with zero seeds and predecessor sets \(P_e=\{r_e\},R_e=\{p_v\}\). It computes \(x_e\wedge p_u\wedge p_v\).
4. For each point \(w\ne1\), let \(p_w\) have zero left seed, left predecessors all \(s_e\) whose triple ends at w, right seed 1, and no right predecessors. It computes the OR of those triple witnesses.

The least fixed point prevents circular triples from generating points without a derivation. Thus the designated output state \(p_n\) computes GEN_n exactly. The state count is \(q=O(n^3)\).

Robere, Pitassi, Rossman, and Cook prove that GEN_n is a monotone polynomial-time function but every monotone span program for it, over every field, has size \(2^{n^{\Omega(1)}}\); the result is restated as Theorem 12 in the primary 2026 ECCC report TR26-070. GEN_n also has polynomial-size monotone circuits: iterate the displayed generation rule for n rounds. Consequently this abstract closure recurrence has q polynomial in n while its monotone span program complexity is superpolynomial in q.

Therefore no polynomial-size compiler from arbitrary abstract q-state recurrences with a designated output state to monotone span programs can exist, even nonuniformly. This is an unconditional counterexample to the broad compiler proposal. Section 3 strengthens it to actual endpoint-induced internal states; the empty-root output remains unrepresented.

## 2. The generic formula route also misses the target scale

The exact C-319 recurrence stabilizes after at most q strict rounds. Unrolling those rounds gives \(O(q^2)\) paid conjunction gates and OR fan-in at most q. Expanding shared subcomputations into a monotone formula has a safe bound

\[
F(q)\le (O(q))^{O(q)}=2^{O(q\log q)}.
\]

Monotone formulas have span programs of size linear in formula size. After substituting seed clauses over N table bits, the generic bound remains at most \(N2^{O(q\log q)}\).

This cannot improve the native linear q floor. Any N-variable monotone function has a monotone DNF with at most \(2^N\) terms and hence an MSP of size at most \(N2^N=2^{O(N)}\). Even maximal possible MSP lower bounds therefore invert the generic formula compilation only to \(q=\Omega(N/\log N)\), weaker than the proved \(N-o(N)\) native bound.

## 3. Endpoint incidence still permits GEN in the internal state vector

The preceding abstract example can be strengthened: endpoint-containment semantics alone do not prevent a q-state list from carrying the GEN computation in its internal activation bits.

Let U be the actual high-table universe and let m=o(N). For OPS s2=N^β with fixed β<1, circuit counting gives |SIZE(s2)|≤2^{O(s2 log(s2+n))}=2^{o(N)}. A cylinder fixing the first m coordinates and one additional coordinate has 2^{N-m-1}=2^{N-o(N)} completions, so it contains a high table. Thus U projects onto all assignments to the m source coordinates, even after fixing one extra bit.

Take any monotone circuit with gates g on those m coordinates, and define

\[
S_g=\{z\in U:g(z_1,\ldots,z_m)=1\}.
\]

Use the following actual semantic endpoints:

* Input gate x_j: (E_g=U, H_g=S_g).
* AND gate g=u AND v: (E_g=S_u, H_g=S_v).
* OR gate g=u OR v: (E_g=S_u\cup S_v, H_g=U).
* Constant-one gate: (E_g=H_g=U).

In every case (T_g=E_g\cap H_g=S_g). The endpoint seed clause is sound for the indicated gate-side condition: if a signed literal slice is contained in S_u (or S_u union S_v), full projection of U implies that the literal forces that condition on every assignment to the m source bits. Likewise, (T_j\subseteq E_g) means the function at state j implies the required side function on every source assignment. Induction on closure rounds proves that every active state computes a true gate, and induction through the circuit order proves completeness. Hence the internal activation bit of each state equals its gate value, including the GEN_n point states, with only O(n^3) actual pairs.

This does **not** make a native separator. Every gate consequence S_g is nonempty (the all-one source assignment extends to U), so these pairs have no empty-consequence output rule and the native output is constantly false. Adding an empty root that fires exactly when p_n is active while keeping endpoint intersection empty is the unresolved step; this construction does not do it.

Actual C-319 pair lists still impose

\[
P_i^E=\{j:T_j\subseteq E_i\},\qquad
P_i^H=\{j:T_j\subseteq H_i\},\qquad T_i=E_i\cap H_i,
\]

and accept only through empty-consequence states. A valid Gap-MCSP separator must additionally accept every low table and reject every high table. C-335 realizes the GEN computation in native **internal states**, but not in the native output and not with the full promise.

Thus the counterexample has a precise scope: neither an arbitrary recurrence compiler nor endpoint incidence alone suffices. A specialized theorem must use the empty-root output and soundness on the entire high universe, together with C-281's compatible context/proof splice law. C-304's scalar-field homomorphism route remains impossible because support alternative is idempotent while field addition is cancellative.

## 4. Source-selection implication

GEN_n is now a candidate **MSP-hard access structure** for a native-specific reverse compiler. Its state recurrence is cheap in the abstract grammar and its MSP is huge, so it also serves as a calibration: a proposed compiler must explain exactly which native semantic restriction excludes this recurrence.

For OPS scale, choosing \(n=(\log N)^K\) makes the number \(n^3\) of source variables polylogarithmic in N. GEN witnesses need at most n triples, so sparse witness descriptions are also polylogarithmic. If the known exponent in the lower bound is c>0, taking Kc>1 makes \(2^{n^c}\) superpolynomial in N. These parameter facts do **not** produce a LowExt map: C-125 still requires a monotone dual-rail image with low YES codes, no contained low code on NO inputs, and a high completion for every NO image.

The actual native bound remains \(q=N-o(N)\). C-335 gives no full-promise cover, positive CohEnc margin, superlinear q lower bound, or P-vs-NP proof.

## References

- Robere, Pitassi, Rossman, and Cook, [Exponential Lower Bounds for Monotone Span Programs](https://www.cs.utoronto.ca/~toni/Papers/rprc-span.pdf).
- Primary 2026 source restating the all-fields GEN lower bound: [ECCC TR26-070](https://eccc.weizmann.ac.il/report/2026/070/download), Theorem 12.
- C-304: research/C304_IDEMPOTENT_SUPPORT_ALGEBRA_AND_SPAN_PROGRAM_BRIDGE_2026-09-28.md.
- C-288/C-291/C-301: the ODDFACTOR reconstruction and map audits.
- C-287/C-290: the CLIQUE transfer and parameter audits.
