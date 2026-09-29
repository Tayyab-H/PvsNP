# C-356 - A linear equality cover matches the C-355 code bucket's size and distance

Date: 29 September 2026  
Route: hostile calibration of the C-355 large-low-codeword bucket, using the one-suffix slice from C-354.  
Classification: **PARAMETER-MATCHED SUBPROMISE COVER; NO FULL-PROMISE OR q IMPROVEMENT.**

## 1. A low code family with the same entropy and large distance

Use C-354's prefix column of length `r=Theta(N/s2)`. Choose `d=2^k=Theta(s1)` with a sufficiently small constant, and partition the prefix addresses `p` into d equal blocks by their first k bits. Each block has

```text
b = r/d = Theta(N^(1-2 beta))
```

addresses, since `s1*s2=Theta(N^(2 beta))` up to the fixed parameter constants. For each Boolean function `g:{0,1}^k->{0,1}`, define

```text
mu_g(p) = g(p_1,...,p_k)
z_g(p,u) = 1 iff (u=u0 and mu_g(p)=1).
```

A decision tree for g has O(d) gates; adding the suffix equality test costs O(n). Taking d small enough gives `CC(z_g)<=s1/2` for all sufficiently large n. The family has `2^d=2^(Theta(s1))` members. Two distinct g values differ on at least one k-bit block, so

```text
dist(z_g,z_h) >= b = Theta(N^(1-2 beta)).
```

For every fixed `beta<1/3`, this distance is asymptotically larger than `kappa_square(s2)=O(s2 log s2)=O(N^beta n^2)`. Thus this family matches C-355's relevant coarse parameters: exponentially many low anchors in s1 and pairwise distance much larger than the sound-cylinder free-coordinate allowance.

## 2. The matching family has a linear native subpromise cover

Partition all N table coordinates into product-code blocks as follows:

- each of the `N-r` coordinates outside the selected suffix column is a singleton block with local codebook `{0}`;
- the d prefix blocks inside the selected column each have local codebook `{0^b,1^b}`.

The resulting product code is exactly `{z_g}`. Its tables have size at most s1. C-258's product-code construction applies to this family against the **actual** high set `U={w:CC(w)>s2}`. Singleton blocks contribute `N-r` rules up to an absolute constant, and the repeated two-word blocks contribute `2db=2r`; the merge rules add O(N). Hence the native list has `q=O(N)`, covers every `z_g`, and rejects every member of U. This is a subpromise cover only; it does not cover all of `SIZE(s1)`.

The same proof-tree dichotomy from C-355 applies to accepting proofs in this linear cover. Therefore large codeword count, large minimum distance, nearly complete certificate supports, and a q^3 bucket of repeated rule labels do not by themselves force a high cross-splice or a superlinear q bound. The equality fingerprint records the shared description and prevents the naive splice argument.

## 3. Consequence for the active route

C-355's proof-tree dichotomy survives the audit for the canonical finite proof trees: each seed leaf chooses one true signed literal, and the LCA/mass partition is valid. The dichotomy is nevertheless structural. The matched C-356 calibration shows that its code-family size/distance bucket cannot be converted to a q charge without using finer information about which state transitions and seed clauses generate the equality fingerprint.

Per the current priority, do not continue strengthening support-width, code-distance, or proof-tree bucket statements. A viable continuation must either (i) prove a transition/seed-clause complexity bound for implementing an arbitrary low-circuit description relation, stable under C-257/C-258/C-307/C-317, or (ii) construct a full-promise `N^(1+o(1))` cover. No result here improves `rho_GapMCSP>=N-o(N)`, constructs a full-promise near-linear cover, or proves P vs NP.
