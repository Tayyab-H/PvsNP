# Route audit: robust puncturing and sparse magnification — 25 September 2026

## Objective

Test whether the anti-checker selector route can be sharpened by converting its one-error guarantee into a robust code-distance statement, then use that statement with recent sparse-distinguishing magnification. The question is whether this reaches an unrestricted circuit lower bound, or merely changes the formulation of O-1.

## Lemma: local correction makes anti-checkers robust

Use fan-in-two Boolean circuits over a fixed complete basis. There is a constant a such that changing a circuit's truth table on r inputs costs at most a*n*r+a gates: for each changed input x in {0,1}^n, build its minterm indicator with O(n) gates and use these indicators to patch the output. In particular:

    CC(f) <= CC(g) + a*n*d_H(f,g) + a.

Let Q be a set of distinct queried inputs, and suppose Q anti-checks every circuit of size at most s1 against f. For any circuit D of size at most s0<s1, if D|Q differs from f|Q on r points, patching only those r points gives a circuit of size at most s0+a*n*r+a that agrees with f on all of Q. This contradicts anti-checking whenever that size is at most s1. Therefore:

    d_H(f|Q, D|Q) > (s1-s0-a)/(a*n)

for every such D, up to integer rounding. Taking s0=floor(s1/2), each valid OPS anti-checker is at distance Omega(s1/n) from every size-s1/2 circuit trace. A minimax-length list with |Q|=O(s1*log(s1)) has relative distance Omega(1/(n*log(s1)))=Omega(1/n^2) for fixed beta>0. This short-list corollary is not automatically a property of every output of an OPS selector: the selector interface allows up to t=2^(10*beta*n) queries. For an output of q distinct queries the universal relative bound is only Omega(s1/(n*q)); at the maximum budget it is Omega(N^(-9*beta)/n^2).

The same correction argument applies to the full truth table: if CC(f)>s2, then its Hamming distance from every size-s1 circuit is greater than (s2-s1-a)/(a*n)=Omega(N^beta/n), where N=2^n, s1=N^beta/(c*n), and s2=N^beta.

### What this adds

The selector does not merely find a puncturing whose label vector falls outside the projected low-circuit code. It finds one separated from the traces of circuits of size about half the threshold by Omega(s1/n) coordinates. This is a universal necessary condition and holds for every selector, including arbitrary nonlinear, nonuniform circuits. It is not sufficient by itself: a trace can be far from every size-s1/2 circuit and still be exactly realized by a size-s1 circuit.

## Stress test against sparse distinguishers

Atserias and Muller give explicit distinguishers that amplify relative Hamming distance q^(-alpha) to a constant fraction using polynomially many parities of at most O(q^alpha) input bits; see their Theorem 8. On a minimax-length trace of q=O(s1*log(s1)), the distance above is about 1/(log(q)^2), so alpha=Theta(log(log(q))/log(q)) gives polylogarithmic parity weight. For a selector output as long as the full OPS budget, the radius yields a weaker relative distance and may require polynomial-weight parities. In either case, this fingerprints the already selected trace.

This does not lower-bound the selector. The distinguisher acts after the input-dependent query set Q_f has been found; it supplies no method for choosing Q_f, and no known theorem charges the circuit for that nonlinear routing. The central O-1 obstruction remains unchanged.

## Parameter check against 2025 general magnification

Let Q=MCSP[s1], the language of truth tables with a circuit of size at most s1. The OPS high promise CC(f)>s2 is, by the correction bound, inside the NO promise for an approximate-Q problem with relative distance at least N^(-(1-beta+eta)) for any fixed 0<eta<beta, once N is large enough. The YES promise is unchanged. Thus a circuit for that approximate problem would decide the OPS gap promise.

The generic circuit-description count gives at most 2^(O(s1*log(s1)))=2^(O(N^beta)) YES tables. This bound does not establish the 2^(N^(o(1)))-sparsity premise used by Atserias-Muller's general formula magnification theorem for fixed beta>0. Their uniform MCSP theorem says that a specified lower bound for P-uniform circuits computing approximate MCSP would imply P != NP^{oplus P}, not P != NP; no implication from that conclusion to the target separation is established here. Even if the sparsity hypothesis were improved, the paper's general theorem yields formula lower bounds, which do not by themselves rule out polynomial-size circuits for NP.

Source: Atserias and Muller, [*Simple general magnification of circuit lower bounds*](https://arxiv.org/html/2503.24061), especially Theorems 8-11.

## Derived structural attack: majority-error overlap

There is another consequence of the correction bound that can be used to test direct reductions. Fix an odd tuple of k distinct circuits D_i, each of size at most s1, and let E_i be the set where D_i differs from f. Their pointwise majority has size O(k*s1+k^2), and it errs exactly on H={x: x lies in at least (k+1)/2 of the E_i}. Since CC(f)>s2, H must have size Omega(s2/n)=Omega(N^beta/n) whenever the majority size is below s2. For OPS parameters this remains true uniformly through k<=kappa*n for a sufficiently small constant kappa.

For 3<=k<=kappa*n, each point of H contributes at least binom((k+1)/2,2) pair intersections. Averaging over the binom(k,2) pairs shows that some pair E_i,E_j intersects on Omega(N^beta/n) points. This rules out a simple SAT-to-selector gadget in which a constant number of low circuits have almost-disjoint error regions and one hidden marker is the only common way to hit them: the majority would then be correct except at the marker and one minterm correction would make f small.

The result is only a finite-subfamily constraint. It does not give a small hitting set for all low circuits. In fact, the generic family of all subsets of an N-point universe larger than N/2 has majority-error region larger than N/(k+1) for every odd k-tuple, yet needs a transversal of size about N/2. For k=O(n), this region is larger than the circuit-derived N^beta/n bound. Thus even the quantitative C-50 property cannot yield a small transversal by incidence arguments alone; the open target is a circuit-specific way to organize these regions across exponentially many hypotheses.

## Verdict and next use

1. **Proved:** every valid selector outputs a robust puncturing certificate, with explicit correction radius Omega(s1/n) against size-s1/2 traces.
2. **Not proved:** any superlinear lower bound on the circuit that routes f to this certificate.
3. **Route limit:** sparse distinguishers can amplify certificate distance after routing, but the project has no bridge from that amplified fingerprint to a lower bound for arbitrary routing circuits. The sparsity and formula/circuit conclusions also do not align with the P-vs-NP target.
4. **Next mathematical target:** prove a circuit-size lower bound for the map from a high truth table to a robust puncturing certificate, allowing full label feedback and arbitrary sharing; use the C-50 majority-overlap constraint only if it yields a global organization of the full error family. Do not treat either invariant alone as progress on O-1.
