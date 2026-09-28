# C-294 - Odd-cut NO-extension consensus yields hard rails for affine cut labels

Date: 28 September 2026  
Classification: **NEW ENCODER TEMPLATE / SCOPED OBSTRUCTION.** It gives valid LowExt completion conditions by construction, then proves that the cut-consensus map for affine cut labels has a superpolynomially hard output rail. It does not rule out cheaper submaps or nonlinear labels.

## 1. The odd-cut NO-extension template

Let the source be ODDFACTOR on a bipartite graph with sides of size v, so the graph has 2v vertices and v^2 edge inputs. A graph is NO exactly when it has an odd-order connected component. For any odd cut S|V\S, let M_S contain every bipartite edge that does not cross the cut. Since each side has odd total order, at least one connected component of M_S inside each side has odd order, so M_S is NO. Conversely, if G is NO, choose an odd-order connected component S. No edge crosses from S to its complement in G, and the complement also has odd order, so G is a subgraph of M_S. Thus odd-cut NO completions cover every NO input; they need not be maximal.

Fix any offset label r_[S] in {0,1}^N for each complementary cut class. Choose R uniformly from {0,1}^N and set z_[S]=R xor r_[S]. Each z_[S] is uniform, so a union bound over at most 2^(2v) cut classes shows that all labels are outside SIZE(s2) simultaneously whenever N-O(v)-log2|SIZE(s2)| tends to infinity. Since log2|SIZE(s2)|=O(s2 log N), this holds for v=polylog(N) and every fixed beta<1.

For an input graph G, let C(G) be the set of odd cuts S that cross no edge of G. Equivalently, S is a union of connected components of G with odd total order. Define the cut-consensus rails
  Psi_(j,b)(G)=1 iff z_[S](j)=b for every S in C(G).

This is monotone: adding edges only removes compatible cuts, so a unanimous bit remains unanimous. If G is YES, every component has even order, so C(G) is empty and both rails at every coordinate are 1; any low table is below Psi(G). If G is NO, C(G) is nonempty. For every S in C(G), each active rail agrees with z_[S], hence Psi(G)<=e(z_[S]) and Psi(G) has a high completion. Thus this gives a valid C-125 map at the semantic level for any chosen family of high labels.

## 2. Affine cut-code labels and their consensus rule

Take a coordinate j indexed by a balanced vertex subset A_j, meaning |A_j intersect L|=|A_j intersect R|, and set
  z_[S](j) = R_j xor (|S intersect A_j| mod 2),
where R is a uniformly random N-bit string. Since |A_j| is even, the label is invariant under replacing S by V\S. For each cut class, z_[S] is uniform; the random-choice argument above makes every label high simultaneously.

Fix a NO graph G with connected components C_1,...,C_c. Let p_i=|C_i| mod 2 and q_i=|A_j intersect C_i| mod 2. A compatible odd cut is a component union encoded by x in {0,1}^c with p dot x=1. The code bit is R_j xor q dot x. A linear form q dot x is constant on the affine hyperplane p dot x=1 exactly when q=0 or q=p. Therefore:
- q=0 pins the bit R_j;
- q=p pins the bit R_j xor 1;
- otherwise both bit values occur among compatible cuts and the consensus leaves coordinate j blank.

This is an exact description of the map's NO rails.

## 3. Each polarity has an ODDFACTOR hard restriction

Let A=A_j have a vertices on each bipartition side, so its complement also has equal sides. The larger of A and V\A has h>=v/2 vertices on each side. Leave an arbitrary bipartite graph H on that larger side and place a fixed perfect matching on the smaller side, with no edges between the two parts. Call the resulting source graph G_H. Then ODDFACTOR(G_H)=ODDFACTOR(H), because the fixed matching contributes only even components.

If the free side is A, then q=p on components of H and q=p=0 on the fixed matching components. Hence q=0 exactly when H is ODDFACTOR-YES. The R_j rail, restricted to this graph family, is precisely ODDFACTOR_h.

If the free side is V\A, then q=0 on components of H and q=p=0 on the fixed matching components. Hence q=p exactly when H is ODDFACTOR-YES. The R_j xor 1 rail, restricted to this graph family, is precisely ODDFACTOR_h.

Thus, for every balanced-subset coordinate, at least one output rail of the cut-consensus map restricts to ODDFACTOR_h for some h>=v/2.

The cited monotone lower bound is stated in ordinary total gate size. To translate it to the project's AND-only cost, collapse each OR-only region in a rail circuit with paid-AND count a. Each of its a AND gates has two OR inputs, and the output is one more OR; each flattened OR has at most m+a distinct inputs, where m is the source edge count. This yields an ordinary monotone circuit of size at most C(a+1)(m+a). Since ODDFACTOR_h needs 2^(h^(c-o(1))) ordinary monotone gates for a fixed c>0, the rail's AND count is at least 2^(h^(c-o(1))/2) up to polynomial factors. For v=(log N)^K and K sufficiently large, this is superpolynomial in N.

## 4. What this establishes

The odd-cut NO-extension consensus construction cleanly separates the two completion obligations: YES images become fully conflicting, and each NO image is contained in a chosen hard code. But the natural affine labeling of odd cuts does not provide a cheap encoder. Its forced consensus predicates contain an ODDFACTOR restriction in one polarity at every coordinate.

This is a scoped no-go for the affine cut-consensus realization, not for all maps using the same high labels: a valid map may omit some unanimous rails while still covering each YES input with a low code. The next proof target is to characterize whether any such lower submap can avoid both hard polarities while retaining YES totality. A second option is a nonlinear label family whose consensus predicates have low AND cost and whose high labels have no fixed scaffold or source-decoding side channel.

No CohEnc separation, positive q transfer, superlinear fusion bound, or P-vs-NP proof follows. The actual fusion lower bound remains q=N-o(N).

Primary source for the ODDFACTOR monotone lower bound: Cavalar, Göös, Riazanov, Sofronova, and Sokolov, [Monotone Circuit Complexity of Matching, ECCC TR25-102](https://eccc.weizmann.ac.il/report/2025/102/download), Theorem 2. Project measure conventions and the C-125 transfer are in C-288 and the bridge file.
