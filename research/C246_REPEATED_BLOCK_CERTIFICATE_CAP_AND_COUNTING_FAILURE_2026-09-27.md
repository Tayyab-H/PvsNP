# C-246 — Repeated-block certificate capacity and why counting stops

Date: 27 September 2026  
Route: O-153, test whether C-245's marked grammar yields a q-charge by counting safe proof supports.  
Status: exact restricted-family capacity bound and an explicit failure of the counting step.

## 1. Family and parameters

Use the C-234 repeated-block anchors. Index the N table coordinates as [r] x [m], with N=rm, and let

    w_g(p,u) = g(u),  p in [r], u in [m],

for a family G of size 2^(Theta(m)) whose diagonal tables all lie in SIZE(s1). Take m=Theta(s2), r=N/m. Let kappa=kappa_square(s2)=Theta(s2 log s2)=o(N), the maximum dimension of a full coordinate subcube contained in SIZE(s2).

## 2. Capacity of one safe support cylinder

Let C be a consistent output-proof support. Every table extending C is accepted, so soundness puts Cyl(C) inside SIZE(s2); hence |free(C)|<=kappa.

For a suffix coordinate u, the anchor value g(u) can vary among tables w_g matching C only if all r copies (p,u) are free. If any copy is fixed, consistency forces g(u) to that fixed bit; conflicting fixed copies make the intersection empty. Therefore

    |{g in G : C subset ell(w_g)}|
      <= 2^( number of u for which all r copies are free )
      <= 2^(kappa/r).

Since kappa/r = kappa*m/N = o(m), one proof support covers at most 2^(o(m)) of the 2^(Theta(m)) diagonal anchors. Any family of output proof supports covering all these anchors must contain at least

    2^(Theta(m) - kappa/r) = 2^(Theta(m))

distinct supports.

This is a genuine global certificate-cover requirement for the repeated family; it does not improve the safe-cube dimension from C-230.

## 3. What the q-state grammar can generate

For each low anchor, choose a ranked accepting proof DAG. It has at most q active rule states. Encode it by:

- its output root: at most q choices;
- its active-state set: at most 2^q choices;
- for each active state and each of its two sides, one selected witness: a seed literal (at most 2N choices) or a predecessor state (at most q choices).

Thus the number of canonical ranked proof DAG certificates available in a fixed q-state system is at most

    q * 2^q * (2N+q)^(2q).

Every low anchor is covered by one of these certificates, and each such certificate is a sound support cylinder. Consequently any successful q-state cover of the repeated family must satisfy

    2^(Theta(m) - kappa/r)
       <= q * 2^q * (2N+q)^(2q),

or, taking logarithms,

    Theta(m) - kappa/r
       <= log2(q) + q + 2q log2(2N+q).

The encoding is deliberately generous: it overcounts invalid witness DAGs and duplicate supports, so it is a valid upper bound on the chosen certificate family.

## 4. First failed implication

The inequality gives at most q=Omega(m/log(N+q)). For the OPS regime m=Theta(s2)=N^beta with fixed beta<1, this is weaker than the already-known q>=N-o(N) floor. At q=Theta(N), the grammar has enough possible witness choices—exp(O(N log N))—to encode far more than the exp(Theta(s2)) certificates demanded by this family.

Therefore the marked-grammar certificate count does not force q above linear. The first broken implication is exactly:

    exponentially many safe certificates required
       -/-> superlinear number of states.

The grammar can generate exponentially many certificates with only q=O(N) state labels. This failure is independent of whether the actual endpoints realize all those choices; a successful lower bound must exploit their *semantic cross-join geometry*, not raw certificate cardinality.

## 5. Learning and next target

The repeated-block family remains useful for testing a profile invariant: its diagonal has exp(Theta(s2)) low anchors, but a safe cylinder can contain only exp(o(s2)) of them. The new result shows that this separation is not enough because a linear-size cyclic grammar can have exp(O(N log N)) witness descriptions.

Do not refine this route by improving the local free-coordinate estimate. Move to the C-245 joint context/proof tensor: identify a property of its compatible entries that cannot be realized by an arbitrary collection of exponentially many supports at q=O(N). The property must distinguish the full SIZE(s1) class from the C-234 diagonal equality cover and survive C-80/C-160/C-228. In parallel, keep the full-promise N polylog N / N^(1+o(1)) cover search active.

No superlinear q lower bound, near-linear full-promise cover, or P-vs-NP proof follows from C-246.
