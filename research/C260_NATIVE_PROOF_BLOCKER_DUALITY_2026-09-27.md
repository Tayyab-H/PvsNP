# C-260 — Native proof–blocker duality and the exact splice join

Date: 27 September 2026  
Route: O-153, global sharing/readout in the native cyclic fusion closure.  
Status: exact two-sided grammar and splice law; no q-sensitive charge, superlinear bound, near-linear full-promise cover, or P-vs-NP result.

## 1. Closure as a monotone system on seed features

Let \(\Lambda=[N]\times\{0,1\}\) be the signed-literal feature set. A table \(x\in\{0,1\}^N\) supplies the one-hot feature set

\[
\ell(x)=\{(k,x_k):k\in[N]\}.
\]

For rule-state \(i\), let \(I_i^S\subseteq\Lambda\) be the seed features whose matching high-side slices lie in endpoint \(S_i\), and let \(D_i^S\subseteq[q]\) be the predecessor states whose carriers lie in \(S_i\), for \(S\in\{E,H\}\). On an arbitrary feature set \(X\subseteq\Lambda\), the least fixed point is

\[
 a_i^{(0)}(X)=0,\qquad
 a_i^{(t+1)}(X)=
 \left(\bigvee_{\lambda\in I_i^E}[\lambda\in X]\vee\bigvee_{j\in D_i^E}a_j^{(t)}(X)\right)
 \land
 \left(\bigvee_{\lambda\in I_i^H}[\lambda\in X]\vee\bigvee_{j\in D_i^H}a_j^{(t)}(X)\right).
\]

Because there are q state bits, this iteration stabilizes in at most q strict rounds for every X. The monotonicity is in X: adding seed features cannot deactivate a state.

## 2. Present-feature certificates

Let \(\mathcal P_i\) be all finite proof-support sets rooted at i. A side support is either one seed feature from \(I_i^S\), or a proof support rooted at a predecessor in \(D_i^S\). The two side supports are united at a rule. Let

\[
\mathcal C_i=\min_{\subseteq}\mathcal P_i
\]

be the inclusion-minimal certificates. Equivalently, use the antichain semiring: alternatives are minimized unions, and an E-side/H-side conjunction takes minimized set unions. Cycles are interpreted by the least fixed point, not by arbitrary solutions of the cyclic equations. Then

\[
a_i(X)=1\quad\Longleftrightarrow\quad
\exists C\in\mathcal C_i\; C\subseteq X.
\]

For the empty-carrier output states O,

\[
\mathcal C_{\rm out}=\min_{\subseteq}\bigcup_{o\in O}\mathcal C_o.
\]

This is the explicit minimal-certificate grammar requested in the priority reset. It is the same least-fixed-point antichain construction as C-242, now paired with the dual below; antichains may be exponentially large and are not being enumerated.

## 3. Absent-feature blockers and transversal duality

Define \(\mathcal B_i\) as the inclusion-minimal absent-feature sets that force state i to be inactive:

\[
B\in\mathcal B_i\quad\Longleftrightarrow\quad
a_i(\Lambda\setminus B)=0
\quad\text{and no proper subset of B has this property.}
\]

There is an explicit cyclic grammar for these blockers. Initialize \(\mathcal B_i^{(0)}=\{\varnothing\}\). For a side S, a blocker must suppress every seed on that side and block every predecessor on that side, so set

\[
\mathcal D_i^{S,(t+1)}=
\min_{\subseteq}\left\{
I_i^S\cup\bigcup_{j\in D_i^S}B_j:
B_j\in\mathcal B_j^{(t)}\text{ for every }j\in D_i^S
\right\},
\]

with an empty predecessor product equal to \(\{\varnothing\}\), and

\[
\mathcal B_i^{(t+1)}=
\min_{\subseteq}\left(\mathcal D_i^{E,(t+1)}\cup\mathcal D_i^{H,(t+1)}\right).
\]

Then \(\mathcal B_i=\mathcal B_i^{(q)}\). The recurrence is the De Morgan dual of the proof recurrence: a state is inactive if at least one side has no matching seed and every predecessor on that side is inactive.

For a family \(\mathcal F\subseteq 2^\Lambda\), let \(\operatorname{Tr}(\mathcal F)\) be its inclusion-minimal hitting sets. The exact monotone duality is

\[
\boxed{\mathcal B_i=\operatorname{Tr}(\mathcal C_i)},\qquad
\boxed{\mathcal B_{\rm out}=\operatorname{Tr}(\mathcal C_{\rm out})}.
\]

For the output blocker family, the grammar is also explicit: rejection requires every output state inactive, so take one blocker from each \(\mathcal B_o\), union them, and minimize. To prove the transversal identity, if a certificate C and blocker B were disjoint, then C would be contained in \(\Lambda\setminus B\), making that feature set both activating and blocking. Conversely, any hitting set of all minimal certificates leaves no certificate in its complement, hence blocks the monotone predicate. This is a standard monotone-function duality; the project-specific content is that both antichains come from the same native cyclic rule grammar.

## 4. Exact context/proof convolution

Let \(\mathcal K_i\) be all finite outside-supports of accepting contexts with one marked occurrence of state i. Let \(\mathcal C_{\rm out}^{\rm cons}\) be the consistent members of the abstract antichain \(\mathcal C_{\rm out}\); inconsistent abstract certificates match no table and are omitted here. Define the compatible join

\[
\mathcal K_i\Join\mathcal P_i=
\{K\cup P:K\in\mathcal K_i,\ P\in\mathcal P_i,\ K\cup P\text{ is consistent}\}.
\]

Cutting any consistent accepting proof at an occurrence of i gives such a pair. Conversely, substituting any proof rooted at i into any matching context gives an accepting proof. Therefore the consistent minimal output certificates obey the exact formula

\[
\boxed{\mathcal C_{\rm out}^{\rm cons}=\min_{\subseteq}\bigcup_{i=1}^q(\mathcal K_i\Join\mathcal P_i).}
\]

The same statement holds for a context with several pairwise disjoint marked holes: any tuple of replacement proofs is accepted whenever the union of the context and all replacement supports is consistent. This is the strongest general reuse law. It is a compatibility law, not a guarantee that two arbitrary anchor supports can be mixed.

Every compatible join support S is hit by every output blocker B:

\[
S=K\cup P\in\mathcal K_i\Join\mathcal P_i,\ B\in\mathcal B_{\rm out}
\quad\Longrightarrow\quad S\cap B\ne\varnothing.
\]

This follows because S is an output proof support and \(\mathcal B_{\rm out}\) is the transversal family of all minimal output proofs. The candidate global object is thus not only the C-244 state zone \([\mathcal K_i]\cap[\mathcal P_i]\), but the joint incidence of (i) context/proof joins and (ii) the output grammar's dual blocker family.

## 5. Translation to table space

For a consistent support S, let \(\operatorname{Cube}(S)=\{x:S\subseteq\ell(x)\}\). Every output proof support has

\[
\operatorname{Cube}(S)\subseteq\mathrm{SIZE}(s_2)
\]

by soundness. For a blocker B, let

\[
\operatorname{Avoid}(B)=\{x:B\cap\ell(x)=\varnothing\}.
\]

Every table in \(\operatorname{Avoid}(B)\) is rejected, so \(\operatorname{Avoid}(B)\cap\mathrm{SIZE}(s_1)=\varnothing\). A blocker with inconsistent polarities may have an empty avoidance set; such blockers are harmless and can be ignored when covering actual tables.

For every low x and high z, choose \(C\in\mathcal C_{\rm out}\) with \(C\subseteq\ell(x)\), and \(B\in\mathcal B_{\rm out}\) with \(B\subseteq\Lambda\setminus\ell(z)\). Transversality gives \(\lambda=(k,b)\in C\cap B\), so \(x_k=b\ne z_k\). Thus the two antichains yield a full promise-side mismatch certificate system. This is an exact native analogue of a primal/dual cover pair, though it does not bound the number of supports or states.

## 6. Attempted q-charge and exact failure

The tempting step is: if many low descriptions share a state, their proof/context joins must expose many different ownership patterns; an output blocker then has to hit each pattern, making the grammar expensive. The proof above establishes only that each individual join intersects every blocker. It gives no lower bound on the number of independent intersections: even a one-rule closure for the promise \(Y=\{x:x_1=0\}\), \(U=\{x:x_1=1\}\) has the common literal \((1,0)\) in every accepting certificate and in a one-element blocker. For a less degenerate calibration, C-248's one-rule nonconstant-versus-two-constants promise has \(N(N-1)\) two-literal certificates, all hit by one blocker support for each of the two high anchors. Thus transversal incidence alone is not a q-charge. C-257 parity and C-258 repeated-block equality further show that full-width certificates or many anchors can have safe, linearly sized fingerprint organizations.

There is nevertheless a genuine forced-*state*-reuse fact on a large actual low subfamily. Choose a power of two \(d\) with \(d\log d\leq c s_1\), partition the N coordinates into d equal blocks, and take the \(2^d\)-member repeated-block family \(\mathsf{Rep}_{d,N/d}\subseteq\mathrm{SIZE}(s_1)\). For every anchor, choose a minimum-rank active empty root and a canonical first predecessor in its accepting proof. C-249's actual-high-side shattering argument ensures this predecessor exists. Mapping each anchor to that internal state, pigeonholing over q labels gives one state used by at least \(2^d/q\) anchors. Since \(d=\Theta(s_1/\log s_1)=N^{\beta-o(1)}\), this is superpolynomial in N for any polynomial q. The implication stops exactly there: it does not give a compatible context/replacement product at that state. C-258's explicit O(N) cover of this same family shows how block-equality fingerprints can protect the forced reuse.

C-236 adds a sharper table-specific limit: for two repeated-function anchors, every compatible disagreement selector must map to a size-s2 hybrid, so only \(|\mathrm{SIZE}(s_2)|=2^{O(s_2n)}\) selectors are allowed. But it still does not force the grammar to realize a forbidden selector or charge q for restricting its image. C-247/C-259 show that \(\Theta(n)\) independent low-choice slots are the right entropy scale; the present proof–blocker duality does not derive those slots from the rule grammar.

**Exact missing arrow:** bound, as a function of q, the *jointly generated incidence geometry* of \((K,P,B)\) with \(K\in\mathcal K_i\), \(P\in\mathcal P_i\), \(B\in\mathcal B_{\rm out}\), and \(K\cup P\) consistent. It must show either a compatible product with more than \(\Theta(n)\) independent high-entropy choices, a high ownership selector, or a superlinear number of rules needed to prevent both. The transversal identity alone is not that theorem.

## 7. Near-linear cover counter-program

The direct full-promise construction still enumerates low circuit descriptions d and checks all N output literals of \(\mathrm{TT}(C_d)\). A literal-prefix trie shares common output prefixes but has at most

\[
q_{\rm trie}\leq\sum_{t=1}^{N}|\pi_t(\mathrm{SIZE}(s_1))|,
\]

and C-212 shattering makes the fixed-order early levels exponential. A universal-circuit grammar that lets each address branch choose its own small cofactor is compact only if it preserves the same circuit description across every address; otherwise it accepts mixed tables. C-259 says up to a small constant times n simple low cofactors can still be patched into size s2, while a large independent product would exceed the size-s2 entropy budget. This identifies the exact coherence issue but yields neither a near-linear cover nor a lower bound. The explicit C-258 equality-fingerprint list remains an O(N) cover only for its repeated-block subfamily.

## 8. Status and next tests

The first two immediate actions are now formalized: the minimal-certificate grammar and the strongest compatible-splice closure law. The dual blocker grammar turns the residual question into a q-sensitive incidence/transversal problem. Before promoting any candidate, test it against C-80, C-121, C-134, C-160, C-161, C-213, C-228, C-234, C-257, and C-258, and against the one-anchor and fractional-cover ceilings.

A finite sanity check generated 800 random cyclic systems with q in {1,2,3} over four abstract seed features. For every system it exhaustively compared all 16 seed subsets: the least-fixed-point truth values agreed with both antichain recurrences, and each blocker family equaled the explicit minimal-transversal family of its certificate antichain. This checks the recurrence bookkeeping only; it is not evidence for an asymptotic bound.

A targeted literature search found the known exact characterization of finite cover complexity by cyclic intersection complexity in Cavalar and Oliveira. It confirms that the native model is exact; it supplies no q-sensitive theorem for the circuit-size promise. The search did not surface a direct code-membership result, which is not a claim that the literature has been exhaustively ruled out. [Cavalar and Oliveira, *Boolean Circuit Complexity and Two-Dimensional Cover Problems* (2025)](https://www.dcs.warwick.ac.uk/~igorcarb/documents/papers/CO25.pdf).

Next: (i) seek an incidence-compression or transversal-slack inequality from the shared cyclic rule grammar; (ii) try an artificial low family of succinctly generated codewords with several independent global checks, since codimension-one parity is safely linear; and (iii) continue the full-promise universal-circuit/cofactor cover search with description identity represented explicitly. Until one branch yields a q-sensitive theorem or a full-promise cover, the project remains at the existing `N-o(N)` lower bound. No Gap-MCSP breakthrough or P-vs-NP proof has been obtained.
