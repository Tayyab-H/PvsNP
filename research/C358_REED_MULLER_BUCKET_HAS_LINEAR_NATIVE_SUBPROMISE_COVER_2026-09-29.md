# C-358 - The C-355 Reed-Muller bucket has an O(N) native subpromise cover

Date: 29 September 2026  
Route: test the exact high-distance low code used in C-355, not only an equality-code family with matching coarse parameters.  
Classification: **EXPLICIT O(N)-RULE SUBPROMISE COVER; NO FULL-PROMISE q IMPROVEMENT.**

## 1. Family and low-circuit budget

Use C-354's one-suffix column with `r=2^m=Theta(N/s2)` prefix addresses. Let `RM(d,m)` be the truth tables of degree-at-most-d polynomials over `F_2`, with dimension

```text
D = sum_{j=0}^d binomial(m,j).
```

Choose d with enough constant-factor slack that every `mu in RM(d,m)` has a De Morgan circuit of size at most `s1/2`. The standard shared monomial DAG uses O(D) gates, then an XOR chain combines the selected monomials using O(D) more; the suffix equality test adds O(n). The C-355 correction chooses the degree under the `s1/2` budget, so all

```text
z_mu(p,u) = 1 iff (u=u0 and mu(p)=1)
```

lie in `SIZE(s1)` for sufficiently large n. The family has `2^D=2^(Theta(s1))` members and minimum distance `2^(m-d)`, as in C-355.

## 2. A circuit recognizes the entire code subpromise

On the r column bits, compute the algebraic-normal-form coefficients of `mu` by the fast Boolean Möbius transform. In-place, each of the m stages performs `r/2` XOR updates, so this takes O(rm) XOR gates. The table is in `RM(d,m)` exactly when every coefficient indexed by a set of size greater than d is zero. OR these coefficients and negate the result. Also test that all `N-r` table bits outside the selected column are zero. The resulting Boolean circuit accepts exactly the code family

```text
Y_RM = {z_mu : mu in RM(d,m)}.
```

Its size is `O(N + r m)`. Since `r=Theta(N/(N^beta n))` and `m=Theta(n)`, we have `r m=Theta(N^(1-beta))=o(N)`, so the total is O(N). XOR gates expand to constant-size De Morgan circuits.

Every member of `Y_RM` is in `SIZE(s1)`, while every table of circuit complexity above s2 lies outside `Y_RM`. This is therefore a valid size-O(N) circuit separator for the subpromise `Y_RM` versus the actual OPS high set. By the existing C-109 circuit-to-fusion compiler, it yields a valid native fusion list with `q=O(N)` for that subpromise.

## 3. What this rules out, and what it does not

The high-distance Reed-Muller family in C-355 cannot by itself force a superlinear native state count. Its complete membership test costs O(N), and the existing circuit-to-fusion compiler gives a native cover of that low subfamily. Thus the large codeword bucket from C-355 is explicitly compatible with linear q, even at the exact family used in the tree dichotomy.

The construction accepts only `Y_RM`, not every table in `SIZE(s1)`. It does not improve the full Gap-MCSP lower bound `rho_GapMCSP>=N-o(N)` and does not provide a full-promise near-linear cover. It teaches that high minimum distance and large code dimension are insufficient: a candidate hard low family must also resist a short *membership separator*.

## 4. Broader compiler boundary

The exact C-319 game still has to be studied directly. Pauly's reachability graph-game forms represent monotone functions and are closed under least fixed points; his paper explicitly leaves the circuit cost of these representations open. C-357 supplies only a bounded-fan-in total-size lower bound for generic readouts, and it does not settle the project's paid-AND measure. See [Pauly, *Parameterized Games and Parameterized Automata*, EPTCS 277 (2018), DOI 10.4204/EPTCS.277.3](https://doi.org/10.4204/EPTCS.277.3) and `research/C357_GENERIC_GAME_TO_BOUNDED_FANIN_CIRCUIT_BARRIER_2026-09-29.md`.
