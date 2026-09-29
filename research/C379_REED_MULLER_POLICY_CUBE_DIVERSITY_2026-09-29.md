# C-379 - Far-apart low codewords require distinct positional policies

Date: 29 September 2026  
Route: apply C-377's safe policy cubes to the C-372 Reed-Muller family, including the root selector.  
Classification: **EXACT POLICY-DIVERSITY BOUND; COUNTING STILL SUBLINEAR.**

## 1. Low code family and distance scale

Let N=2^n and choose delta>0 with H_2(delta)<beta and delta<1-beta. The degree-t Reed-Muller evaluation code F=RM(t,n), t=floor(delta n), has dimension

    r = N^(H_2(delta)+o(1)).

Each codeword has an n-variable circuit of size O(r n)=o(s1), so F is contained in SIZE(s1). Its minimum distance is

    d_min = N^(1-delta+o(1)).

Let h=log2|SIZE(s2)|=N^(beta+o(1)). Since 1-delta>beta, d_min>h for sufficiently large n.

## 2. One positional policy cube covers at most one codeword

For each f in F choose a winning positional policy and an empty root. By C-377, its selected seed literals define a sound coordinate cube fixing at least N-h coordinates; the cube has at most h free coordinates.

If one root-policy pair were winning for two distinct codewords f,g in F, both would lie in that same cube. They could differ only on its at most h free coordinates, so dist(f,g)<=h, contradicting d_min>h. Therefore the selected root-policy pairs are distinct across F. In particular, some root class contains at least |F|/q=2^r/q codewords.

## 3. Why this still does not charge q superlinearly

There are at most q root choices. At each of the 2q state-side slots, an action can select one of at most 2N signed literals, one of at most q predecessor states, or a constant-true seed. Hence the total number of root-policy pairs is at most

    q * (q + 2N + 1)^(2q).

Completeness and the one-codeword-per-policy property imply

    2^r <= q * (q + 2N + 1)^(2q),

so r <= log2(q)+2q log2(q+2N+1). For polynomial q this gives only

    q = Omega(r/log N)
      = N^(H_2(delta)+o(1))/log N
      = o(N),

because H_2(delta)<beta<1. This is an exact strengthening of policy diversity, but it is weaker than the known q>=N-o(N) floor. It confirms that root selection does not erase a large code family, while also confirming that raw action-table counting cannot cross linear.

## 4. Checkpoint

- One root-policy pair can cover at most one member of this far-apart low code: proved.
- A root class contains at least |F|/q selected policies: proved.
- The action-table count yields only a sublinear q bound: route cap, no improvement.
- The next target remains the graph-sensitive acyclic-hybrid theorem in C-378/O-226, not a stronger policy-count argument.

Full derivation uses the Reed-Muller parameters and C-377's positional-policy cube lemma. No full-promise near-linear cover or P-vs-NP proof follows.
