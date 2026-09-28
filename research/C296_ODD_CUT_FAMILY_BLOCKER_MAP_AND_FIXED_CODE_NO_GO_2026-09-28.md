# C-296 - Odd-cut family blockers give a valid map, then the fixed-code decoder kills the route

Date: 28 September 2026

Classification: VALID C-125 MAP TEMPLATE / SCOPED NO-GO. An arbitrary incidence code on odd cuts gives monotone outputs with high NO completions. The construction is not a useful transfer because every YES image contains the same low code, and every NO image excludes it; the source is recovered by one N-rail conjunction.

## 1. Odd-cut incidence labels

Let the source be bipartite ODDFACTOR on two sides of size v. Let C be the set of odd cut classes [T], identifying T and its complement. Its size is M=2^(2v-2). For each table coordinate j in [N], choose a subset U_j of C and define

    z_T(j) = 1 iff [T] belongs to U_j.

If each membership bit is chosen independently and uniformly, every z_T is a uniform N-bit table. Therefore

    Pr[some z_T is in SIZE(s2)]
        <= M |SIZE(s2)| / 2^N
        = 2^(2v-2 + O(s2 log N) - N).

This is o(1) whenever v+s2 log N=o(N), which includes the project range v=polylog(N) and also v=N^delta for fixed delta<1. Hence one incidence family labels every odd cut by a high table simultaneously.

## 2. The blocker map

For an odd cut T, let delta(T) be its crossing-edge set, and define

    X_T(G) = OR over e in delta(T) of the input bit x_e.

Set the dual-rail map outputs to

    F_(j,0)(G) = AND over T in U_j of X_T(G),
    F_(j,1)(G) = 0.

An empty conjunction is true. Each X_T is monotone, so every output rail is monotone.

If G is ODDFACTOR-YES, every connected component has even order. An odd set T cannot be a union of these components, so at least one graph edge crosses every odd cut. Thus X_T(G)=1 for every odd cut T, all F_(j,0)(G)=1, and the zero table is below F(G).

If G is NO, choose an odd-order connected component T. No edge crosses T, so T is a compatible odd cut. Whenever F_(j,0)(G)=1, every cut in U_j is crossed; in particular T is not in U_j, so z_T(j)=0. The only active rail at coordinate j therefore agrees with z_T. Hence F(G)<=e(z_T), and z_T is high by Section 1.

This is a valid C-125 map for any incidence family whose cut labels are all high. It gives an explicit construction beyond the full-consensus map: each output coordinate blocks a selected family U_j of odd cuts.

## 3. Direct circuit cost and the random-family setting

The displayed formula computes each output with at most max(|U_j|-1,0) binary AND gates; the cut-crossing disjunctions are OR gates. Thus a direct implementation costs

    a_direct = sum over j of max(|U_j|-1,0).

For independent random U_j, |U_j| has distribution Binomial(M,1/2), and

    E[a_direct] = N (M/2 - 1 + 2^(-M)).

This is only the cost of the direct formula implementation. It is not a lower bound against a shared circuit that factors different U_j sets.

## 4. Fixed-low-code decoder: the decisive obstruction

Every YES image contains the same low code, the all-zero table. Every NO image excludes that code: choose its compatible cut T as above. Since z_T is high, it is not the zero table, so some coordinate j has z_T(j)=1. At that coordinate F_(j,0)(G)=0; F_(j,1) is identically zero. Therefore no complete table lies below F(G).

Consequently,

    ODDFACTOR(G) = AND over j in [N] of F_(j,0)(G).

If the map has g binary AND gates, composing this N-way conjunction adds N-1 gates. The monotone AND-count A(ODDFACTOR_v) therefore satisfies

    g >= A(ODDFACTOR_v) - N + 1.

The matching-sunflower lower bound gives ordinary monotone size 2^(v^c) for some fixed c>0. If a circuit has g binary AND gates, flattening its OR-only regions gives ordinary size O((g+1)(v^2+g)); hence A(ODDFACTOR_v)=2^(Omega(v^c)). At v=(log N)^K for sufficiently large fixed K this exceeds every polynomial in N. Thus no implementation of this blocker map can be cheap enough for the desired transfer, even if its random cut-family formula could be factored dramatically.

This is the fixed-polarity case already isolated by C-293. The new information is that a large, input-dependent NO-label family does not help when every YES input still shares one fixed low table.

Primary source for the ODDFACTOR monotone lower bound: Cavalar, Goeos, Riazanov, Sofronova, and Sokolov, "Monotone Circuit Complexity of Matching," ECCC TR25-102, Theorem 2: https://eccc.weizmann.ac.il/report/2025/102/revision/1/download

## 5. Finite low-code envelope decoder

The fixed-code obstruction has a general form. Let W={w^1,...,w^r} be any family of low tables that covers all YES images: every YES input G has e(w)<=F(G) for some w in W. No NO image can contain a low table. Indeed, if e(w)<=F(G)<=e(z) for a high completion z, then the one-hot rail order forces w=z, contradicting low versus high.

Consequently the monotone predicate

    OR over w in W of (AND over j in [N] of F_(j,w_j)(G))

computes the source. If the map has g AND gates, this decoder has at most g+r(N-1) AND gates. Writing A(f) for the source's minimum monotone AND-count gives

    g >= A(f) - r(N-1).

Thus the codeword decoder is a second envelope bottleneck, dual to the high-label conflict decoder in C-295. For C-296, r=1 and w=0, recovering g>=A(ODDFACTOR)-N+1. To transfer a large source lower bound, a useful map must avoid a small fixed family of low witnesses as well as a small fixed family of high completions.

## 6. Next proof target

A useful ODDFACTOR encoder must avoid a small low-code witness envelope, or otherwise defeat the codeword decoder. Merely making NO completions vary is insufficient. The next construction must keep the positive and negative witness rails from exposing ODDFACTOR by a free OR, while the NO-side rails remain below high completions and the YES-side images contain a low table. Continue under O-173 and test C-258 equality, C-278 source-decoder, and C-281 owner-mask constraints.

C-296 gives no CohEnc separation, no fusion q improvement, and no P-vs-NP proof.
