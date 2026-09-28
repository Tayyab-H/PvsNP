# C-311 - Universal dual-consensus rails are a valid map but give away the source

Date: 28 September 2026  
Classification: **SPAN-PROGRAM CONSTRUCTION AUDIT / EXACT ROUTE NO-GO.** The universal family of dual separators can be encoded by monotone consensus rails with arbitrary high completion labels. The construction is logically valid, but any one table coordinate's opposite rails AND together to compute the source. It cannot give a reconstruction-versus-decision gap.

## 1. Start from the exact ODDFACTOR span program

For a bipartite graph with vertex set V and edge columns `a_e=u_i+u_j` over GF(2), let `t=1_V` and

```text
L_X = span{a_e : e is present in X}.
f(X)=1 iff t is in L_X.
Y_X = {y in GF(2)^V : y dot a_e=0 for every present edge e, y dot t=1}.
```

The span-program duality theorem gives `Y_X` nonempty exactly when `t` is not in `L_X`. In a graph, its elements are odd-total vertex colorings constant on every connected component; these are precisely the odd cuts avoided by the graph. Adding edges only adds orthogonality constraints, so `Y_X` shrinks monotonically and becomes empty on YES inputs.

This is the natural place to try to put a high table on the NO side: assign every dual witness y an arbitrary truth table `c(y)` outside `SIZE(s2)`. If `v=polylog N`, a random independent assignment works by a union bound: the failure probability is at most `2^(2v) * |SIZE(s2)| / 2^N <= 2^(2v+O(s2 log s2)-N)`, which tends to zero for each fixed `beta<1`.

## 2. The universal-consensus map

For each address j and polarity b, define

```text
Phi_(j,b)(X)=1 iff c_j(y)=b for every y in Y_X.
```

The universal statement is true when `Y_X` is empty. This map has all three C-125 properties:

1. **Monotonicity.** If `X subseteq X'`, then `Y_X' subseteq Y_X`. A universal label condition that holds on `Y_X` continues to hold on its subset.
2. **YES completion.** On YES, `Y_X` is empty, so both rails at every coordinate are 1. Any low table w is dominated by `Phi(X)`.
3. **NO completion.** On NO, choose any `y in Y_X`. Every active rail `(j,b)` has `b=c_j(y)`. Hence `Phi(X) <= e(c(y))`, and this is a high completion if the codebook labels are all high.

The coding obstacle is therefore not the high-table count, nor monotonicity, nor NO-side completion.

## 3. Exact decoder hidden in the map

Fix any coordinate j. On YES, both `Phi_(j,0)` and `Phi_(j,1)` equal 1 because `Y_X` is empty. On NO, `Y_X` is nonempty, and a function `c_j` cannot be constantly 0 and constantly 1 on the same nonempty set. Thus

```text
f(X) = Phi_(j,0)(X) AND Phi_(j,1)(X).
```

If the multi-output map uses a shared DAG with a binary-AND count a, this is an exact monotone separator with at most `a+1` AND gates. Therefore

```text
CohEnc_(s1,s2)(f) >= CycAnd(f)-1
```

for every map of this universal-consensus form. The implication holds even if the labels `c(y)` are random, mutually unrelated, and individually have very high circuit complexity. The output rails themselves reveal emptiness of the dual-witness family in one conjunction.

This is the precise failure of the proposed span-program-to-LowExt mechanism: existential global reconstruction is not doing hidden work; the fixed-coordinate opposite-polarity test already performs the source decision.

## 4. Explicit monotone formula for the rails and its cost

For the graph incidence program, a dual y is valid exactly when every present edge has endpoints of equal y-label and `y dot t=1`. Therefore

```text
Phi_(j,b)(X) = AND over odd y with c_j(y) != b
               [ OR over edges e crossing y of x_e ].
```

The formula confirms monotonicity, but naively has up to `2^(2v-1)` clauses per rail. More importantly, even a compact implementation cannot improve on the decision cost because of the exact two-rail decoder above. Replacing the universal family by a selected subfamily does not help if it remains empty on every YES input and nonempty on every NO input: vacuity still activates both YES rails, so the same decoder applies. A surviving variant must make the YES-side witness family nonempty and label-compatible, while preserving monotonicity and both C-125 completion conditions.

## 5. General saturation lemma

The key statement does not depend on span programs. If a C-125 map has any coordinate j such that both polarity rails are 1 on every source-YES input, and every source-NO image is dominated by a one-hot high code, then

```text
f = Phi_(j,0) AND Phi_(j,1).
```

NO soundness forbids both rails at that coordinate, while YES saturation supplies both. The map's AND cost is consequently within one gate of exact source decision. This subsumes the fixed-pair decoder obstruction for the universal dual construction. A candidate with a positive reconstruction gap must avoid universal YES-side saturation at every fixed coordinate; low completions must vary across YES inputs in a way the map does not expose as a cheap coordinate test.

## 6. Research consequences

- The linear-size GF(2) span program for ODDFACTOR does not by itself give a cheap C-125 map. Its dual witnesses offer plausible high completions, but universal monotone consensus makes the source immediately decidable.
- A random high codebook is not enough. Any encoding must also hide source membership from every fixed output-polarity conjunction.
- The next algebraic attempt should use a mixed primal/dual family with non-vacuous YES labels, or a reconstruction rule not expressible as universal consensus over a shrinking witness family. It must prove monotonicity directly and test the output-pair decoder before optimizing AND count.
- The actual OPS bound remains `rho_GapMCSP=N-o(N)`. No positive `CohEnc/CycAnd` gap, q exponent increase, near-linear full-promise cover, or P-vs-NP result follows.

Background source for the exact ODDFACTOR span program and monotone-circuit separation: Babai, Gal, and Wigderson, [*Superpolynomial Lower Bounds for Monotone Span Programs*](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/GAL/SPAN/COMBINATORICA/final.pdf). The C-125 definitions and transfer interface are recorded in C-288.
