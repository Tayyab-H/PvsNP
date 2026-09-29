# C-391 - Hard-core selector search by prefix-extension queries

Date: 29 September 2026  
Route: make the search-to-decision gap in C-388 exact by writing the self-reduction for the hard-core sample relation.  
Classification: **PROVED ORACLE UPPER BOUND AND BRIDGE REQUIREMENT; NO SELECTOR CIRCUIT BOUND.**

## 1. Relation

Keep C-388's parameters: `N=2^n`, `T=ceil(1.515 s1)`, and `L=ceil(c N^beta)`. Encode a variable-length sample by a length field `ell` and `L` address slots, where `1<=ell<=L`; slots after ell are forced to zero in the canonical encoding and are ignored in the empirical sample. This gives a fixed-length encoding of `O(L log N)` bits. For a sample `Q=(x_1,...,x_ell)`, let

$$
R(f,Q) \iff \text{for every } C \in \mathrm{CIRCUIT}_{n,T},\quad
\frac{1}{\ell}\sum_{i=1}^{\ell}[C(x_i)\ne f(x_i)]\ge0.259.
$$

A counterexample is one size-T circuit with error below 0.259. Its description length is polynomial in N and its error on Q is computable in polynomial time from the explicit table f. Hence `R is in coNP`, as established in C-388.

## 2. Prefix-extension language

For any bit prefix `p` of the canonical encoding of a sample, define

$$
\mathrm{EXT}(f,p) \iff \text{there exists a canonical valid sample encoding } Q
\text{ extending } p \text{ such that } R(f,Q).
$$

The prefix relation is polynomial-time checkable and R is coNP. Therefore EXT has the quantifier form `exists Q for all C: phi(f,p,Q,C)`, with polynomially bounded Q and C descriptions and a polynomial-time matrix `phi`. Thus

$$
\mathrm{EXT}\in\Sigma_2^P.
$$

For the empty prefix, `EXT(f,empty)` is exactly the witness-existence predicate from C-388. For a nonempty prefix, it is a *different restricted search question*.

## 3. Canonical selector upper bound

Define `S_lex` as follows. Query `EXT(f,empty)`. If false, output a fixed default encoding. If true, construct a witness one encoding bit at a time: at each prefix `p`, query whether `p` followed by bit 0 has an extension; take 0 if yes, and otherwise take 1. After `O(L log N)` bit decisions, the resulting canonical sample `Q` satisfies `R(f,Q)`. Thus the total selector function belongs to

$$
\mathrm{FP}^{\Sigma_2^P}.
$$

This is an unconditional oracle-algorithm upper bound, not a Boolean circuit upper bound. The number of oracle queries is polynomial in N, but the oracle answers are `Sigma_2^P` queries. Replacing them with free calls would hide exactly the search/verification cost at issue.

## 4. Why the unconditioned decision predicate does not self-reduce by itself

The unconditioned decision predicate is just `EXT(f,empty)`. Prefix self-reduction needs the family of predicates `EXT(f,p)` for all prefixes encountered. A circuit that decides only `EXT(f,empty)` supplies no answers to these conditioned queries. No encoding of an arbitrary prefix constraint into the original f-only decision instance is known in this project. Therefore C-346/C-388's existential promise separator alone does not extract Q, and this section proves no impossibility of a more clever reduction.

There is a useful conditional composition statement. If `S` is a selector circuit correct on every high table and `V` is an exact circuit for the total relation `R(f,Q)`, then `V(f,S(f))` separates low from high: high tables have valid selected Q, and low tables have no valid Q at all. The resulting circuit has size at most `|S|+|V|+O(1)`. The missing verifier is coNP in the direct formulation; supplying S alone is not enough. This makes an explicit selector-to-decision bridge depend on a verifier or a separate structural shortcut.

## 5. Scope

- The lexicographically first valid selector has an unconditional `FP^Sigma_2^P` oracle upper bound by standard prefix self-reduction.
- This does not prove its circuit size is large, and does not imply every valid selector is hard.
- It does not improve `q>=N-o(N)`, construct a near-linear selector, or yield a q-preserving reduction to C-319.
- The next selector attack must either lower the complexity of EXT for the structured hard-core relation or prove a lower bound applying to all valid selectors. Do not claim search-to-decision from EXT(f,empty) alone.
