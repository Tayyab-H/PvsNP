# C-295 - Two-code affine consensus forces hard submaps

Date: 28 September 2026

Classification: SCOPED ENCODER NO-GO. Every pointwise submap of one coherent affine odd-cut consensus map that covers all YES inputs with low tables computes ODDFACTOR with only one extra AND gate. The known monotone lower bound therefore makes the encoder superpolynomially expensive at the project parameter scale.

## 1. Coherent two-code labels

Use bipartite ODDFACTOR on sides X and Y, each of size v. Choose a nonempty balanced vertex set A with r vertices on each side, and let B be its complement, with h=v-r vertices on each side. Choose r so that h is at least v/2. For an odd cut class [S], label its NO extension by

    z_[S] = R if |S intersect A| is even,
            complement(R) if |S intersect A| is odd.

The labels are well-defined on complementary cut classes because |A|=2r is even. There are only two possible tables, R and complement(R), across all cuts.

Choose R uniformly from {0,1}^N. Each of R and complement(R) is uniform. Since the number of SIZE(s2) tables is at most 2^(O(s2 log N)) and s2 log N=o(N) in the OPS parameter range, the union bound gives

    Pr[R or complement(R) is in SIZE(s2)]
        <= 2 |SIZE(s2)| / 2^N = o(1).

Thus there exists R for which both labels are high, simultaneously for every odd cut. This improves the counting burden in C-294: no union bound over the cut family is needed.

Let Psi be the odd-cut consensus map from C-294: a signed bit (j,b) is active at G iff every odd cut compatible with G has label bit b at coordinate j. On YES inputs the compatible-cut family is empty, so Psi has every rail active.

## 2. Exact shape of every NO image

Every NO graph G has at least one compatible odd cut. Its compatible cuts receive labels from the two-element set {R, complement(R)}.

- If every compatible cut is labeled R, then Psi(G)=e(R).
- If every compatible cut is labeled complement(R), then Psi(G)=e(complement(R)).
- If both labels occur, then at each coordinate both bit values occur, so Psi(G) is the all-zero dual-rail vector.

Consequently, on every NO input, Psi(G) is one of these two one-hot code vectors or zero. This is the key coherence property; it does not hold for arbitrary independently chosen labels at each coordinate.

## 3. Any valid pointwise submap has a one-AND decoder

Let F be any monotone map satisfying both:

1. F(G) is coordinatewise at most Psi(G) for every graph G; and
2. for every ODDFACTOR-YES graph G, some w in SIZE(s1) has e(w) at most F(G).

Define two monotone ORs of output rails:

    A_F(G) = OR over j of F_(j, 1-R_j)(G)
    B_F(G) = OR over j of F_(j, R_j)(G).

On a YES input, choose the low table w guaranteed by condition 2. Since both R and complement(R) are outside SIZE(s2), and SIZE(s1) is contained in SIZE(s2), w differs from each of them. A coordinate where w differs from R makes A_F=1. A coordinate where w differs from complement(R) makes B_F=1. Hence A_F(G)=B_F(G)=1.

On a NO input, F(G) is at most Psi(G). If Psi(G)=e(R), then A_F(G)=0. If Psi(G)=e(complement(R)), then B_F(G)=0. If Psi(G)=0, both are zero. Therefore

    ODDFACTOR(G) = A_F(G) AND B_F(G)

on every bipartite graph input.

This decoder uses only one additional AND gate beyond the AND gates already present in F. In particular, omitting any chosen set of unanimous consensus pins cannot evade the source lower bound while preserving YES coverage.

## 4. AND-count consequence

The source has m=v^2 edge variables. The cited matching-sunflower theorem gives monotone circuit size 2^(v^c) for ODDFACTOR for some fixed c>0. If F uses g binary AND gates, the decoder above uses at most g+1 AND gates. Flatten each OR-only region: its leaves are among the m source variables and the at most g+1 AND outputs. Rebuilding the at most 2(g+1) OR inputs to AND gates and the two decoder ORs with fan-in two yields an ordinary monotone circuit of size O((g+1)(m+g)).

Therefore

    (g+1)(v^2+g) >= 2^(v^c) / O(1),

which implies g >= 2^(Omega(v^c)) after absorbing polynomial factors in v. Set v=(log N)^K with a fixed K>1/c. Then g exceeds every fixed polynomial in N. Thus this coherent affine consensus map has no polynomial-AND pointwise submap satisfying complete low-code coverage.

The ordinary monotone lower bound is Theorem 2 of Cavalar, Goeos, Riazanov, Sofronova, and Sokolov, "Monotone Circuit Complexity of Matching," ECCC TR25-102, revision 1. The paper states an exponential-in-a-power lower bound for ODDFACTOR and obtains it by applying the matching lower-bound proof on its odd-cut distribution: https://eccc.weizmann.ac.il/report/2025/102/revision/1/download

## 5. General finite-envelope decoder

The two-code proof extends to any fixed family H={z^1,...,z^k} of high tables. Suppose a monotone map F covers every YES input with a SIZE(s1) code, and every NO image is below at least one e(z) for z in H. For each z define

    C_z(G) = OR over j of F_(j, 1-z_j)(G).

On YES, the covered low table differs from every z in H, so every C_z is 1. On NO, choose a high completion z with F(G)<=e(z); then C_z(G)=0. Therefore the source is computed by AND over z in H of C_z. If F uses g AND gates, this decoder uses at most g+k-1 binary AND gates.

Let A(f) denote the minimum number of binary AND gates in an acyclic monotone circuit for source f, with OR gates free. The finite-envelope condition implies

    g >= A(f)-k+1.

The ordinary monotone size lower bound and the same OR-flattening argument give A(ODDFACTOR_v)=2^(Omega(v^c)) for some fixed c>0. If k is at most half of A(ODDFACTOR_v), the encoder still needs at least half of that exponential-in-a-power AND budget. Odd-cut families can have 2^(Theta(v)) distinct cuts, which may exceed this source lower-bound scale; label count alone therefore does not settle the general affine or nonlinear cases. Any further attack must exploit the structure of the label family or prove a harder conflict-decoder lower bound.

## 6. Scope and next frontier

C-295 closes the strict-submap escape for the coherent affine labeling that uses one balanced set A at every table coordinate. The reason is not that one individual hard rail must survive: two global conflict ORs followed by one AND recover the source.

This does not rule out a general C-125 map that is not pointwise below this consensus map, coordinate-dependent affine labels, or nonlinear high labels whose NO images are not confined to one complementary pair of codes. It gives no C-125 transfer, no improvement to the actual fusion lower bound q=N-o(N), and no P-vs-NP proof.

The next useful experiment is to characterize label families by the monotone decoder complexity of their NO-image envelope: if all allowed NO partial vectors are contained in a small family of high codes, ask how many AND gates are needed to test that a YES image conflicts with every code in the family. For two complementary codes, the answer is one AND gate after OR aggregation; larger families need a genuine lower bound or a counterexample. Preserve C-258 equality and C-278 source-decoder checks.
