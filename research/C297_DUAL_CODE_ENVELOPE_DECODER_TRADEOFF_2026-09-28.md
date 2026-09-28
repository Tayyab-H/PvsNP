# C-297 - Dual code-envelope decoders constrain every C-125 map

Date: 28 September 2026

Classification: PROVED MAP LOWER-BOUND TRADEOFF / ROUTE FILTER. A small family of high NO completions or a small family of low YES witnesses yields a monotone source decoder. This makes the two sides of a proposed C-125 transfer quantitatively symmetric.

## 1. Setup

Let f be a monotone source function on m input bits. A monotone map F outputs N dual-rail pairs F_(j,0), F_(j,1), and uses g binary AND gates; OR gates are free in the project measure.

Assume the C-125 order conditions:

- for every YES input x, some low table w in SIZE(s1) satisfies e(w)<=F(x);
- for every NO input x, some high table z outside SIZE(s2) satisfies F(x)<=e(z).

Let W be a family of low tables that covers all YES images, meaning every YES has some w in W below its image. Let H be a family of high tables that covers all NO images, meaning every NO image lies below some z in H. Write r=|W| and k=|H|.

No NO image can contain a low table: if e(w)<=F(x)<=e(z), then e(w)<=e(z). Since both are complete one-hot dual-rail codes, this forces w=z, impossible for low w and high z.

## 2. Decoder from the high completion envelope

For each z in H, define its conflict OR

    C_z(x) = OR over j in [N] of F_(j, 1-z_j)(x).

On a YES input, choose its covered low table w. Since w differs from every high z, at least one coordinate has w_j=1-z_j, so C_z=1 for every z in H.

On a NO input, choose a high completion z in H. Because F(x)<=e(z), every rail conflicting with z is 0, so C_z=0. Therefore

    f(x) = AND over z in H of C_z(x).

This uses at most k-1 additional binary AND gates. If A(f) is the minimum monotone AND-count of f, then

    g >= A(f)-k+1.

This is the finite-high-envelope decoder from C-295.

## 3. Decoder from the low witness envelope

For each w in W, define its code-containment test

    P_w(x) = AND over j in [N] of F_(j,w_j)(x).

On a YES input, one member w of W is below F(x), so P_w=1. On a NO input, no low table is below F(x), as shown in Section 1; hence every P_w=0. Therefore

    f(x) = OR over w in W of P_w(x).

The OR is free, and the conjunctions use at most r(N-1) additional binary AND gates. Thus

    g >= A(f)-r(N-1).

For r=1 this is the fixed-low-code decoder behind C-293 and C-296.

## 4. Combined consequence and ODDFACTOR parameters

Both decoders compute the source, so

    g >= A(f) - min(k-1, r(N-1)).

For ODDFACTOR_v, the matching-sunflower theorem and OR-flattening give A(f)=2^(v^Omega(1)). A map with g=poly(N) therefore cannot have a high completion envelope of size k substantially below A(f), and cannot cover its YES images by fewer than about A(f)/N low tables. In particular, increasing NO-label diversity alone does not repair a fixed low witness, and varying low witnesses alone does not repair a small high envelope.

This is a necessary condition only. At the active polylogarithmic source scale, both the full high-table universe and SIZE(s1) are much larger than these thresholds, so the inequality does not rule out a general map. The unresolved task is to build a cheap shared map while both code families are large and their respective conflict/containment decoders remain hard.

Primary source for the ODDFACTOR lower bound: Cavalar, Goeos, Riazanov, Sofronova, and Sokolov, "Monotone Circuit Complexity of Matching," ECCC TR25-102, Theorem 2: https://eccc.weizmann.ac.il/report/2025/102/revision/1/download
