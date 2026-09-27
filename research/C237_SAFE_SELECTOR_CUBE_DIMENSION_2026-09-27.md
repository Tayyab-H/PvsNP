# C-237 — Safe selector cubes saturate the universal width on random anchor differences

Date: 27 September 2026  
Scope: test whether the disagreement-selector set from C-236 has a smaller safe-subcube dimension than the full low-circuit class. It does not: for every fixed OPS exponent beta in (0,1), typical repeated anchors contain a selector subcube of dimension Theta(s2 n), matching C-230 up to constants. This closes the local-width refinement of C-236.

## Statement

Use the repeated anchors and parameters of C-236. Suppose the two suffix functions differ on a set U of at least m/3 suffix inputs. Then the disagreement-selector safe set

    L_{g,h}={mu subset D : w_h XOR mu is in SIZE(s2)}

contains an axis-aligned Boolean subcube of dimension at least c_beta s2 n for some constant c_beta>0. On the other hand, C-230 gives the universal upper bound kappa_square(s2)=O(s2 n). Therefore

    max safe selector-subcube dimension in L_{g,h} = Theta_beta(s2 n).

For independent uniform g,h, the hypothesis |U|>=m/3 holds with probability 1-exp(-Omega(m)).

## Proof for beta below 1/2

Here r=Theta(N^(1-beta)) is much larger than s2 n. Choose one u0 in U. Inside its prefix column {(p,u0):p in {0,1}^(n-k)}, choose a prefix subcube F of size t= floor(c_beta s2 n); this fits because r/(s2 n)->infinity.

For any assignment delta on F and zero off F, the modified table w_h XOR delta is computable by first testing the fixed address bits specifying F and u0, then evaluating an arbitrary Boolean function on the remaining j=log2(t) prefix bits. Lupanov synthesis gives circuit size

    CC(delta) <= O(n + 2^j/j) = O(n + t/log t).

Since log t=Theta_beta(n), choosing c_beta small makes this at most s2/3 for large n. Also CC(w_h)<=s1/4=o(s2), and XOR costs only a constant factor/additive basis overhead. Hence every assignment on F gives a table in SIZE(s2). As F is contained in D, these are selectors in L_{g,h}; they form a subcube of dimension t=Theta_beta(s2 n).

## Proof for beta at least 1/2

Let a=n-k=Theta_beta(n), so r=2^a. Choose q=floor(c_beta s2 a/r) distinct suffixes U0 subset U and let

    F = {(p,u): p in {0,1}^a, u in U0}.

For fixed beta<1 and sufficiently large n, q>=1 and q<=|U|: indeed q/m=O(a/r)=o(1), while s2 a/r grows at least on the order of n when beta=1/2 and faster above it.

An arbitrary delta supported on F can be written as q independent functions delta_u(p), one on each selected suffix. For each u, Lupanov synthesis on a prefix of a variables computes delta_u with O(r/a) gates. Testing u=u_j costs O(k) gates per selected suffix. Therefore

    CC(delta) <= O(q r/a + q k + n).

By the choice q=Theta(c_beta s2 a/r), the first term is O(c_beta s2). The second term is o(s2), since qk/s2=O(ak/r)=o(1) for fixed beta<1. Choose c_beta small; adding w_h and the XOR still gives CC(w_h XOR delta)<=s2. Thus the entire selector cube on F is safe and has dimension

    |F|=q r=Theta_beta(s2 a)=Theta_beta(s2 n).

This proves the lower bound for beta>=1/2 as well.

## Upper bound and interpretation

Any selector cube contained in L_{g,h} maps injectively under mu -> w_h XOR mu to a full truth-table subcube contained in SIZE(s2). Its dimension is therefore at most kappa_square(s2)=Theta(s2 log s2)=Theta_beta(s2 n), by C-230. This matches the constructions above.

So random disagreement geometry does not sharpen the safe-free-coordinate threshold. Even for a typical pair of low repeated anchors, one can choose a structured set F inside the disagreement coordinates on which every Boolean patch remains size-s2. The distinction that matters is not only the number of free selector bits, but whether the proof grammar generates a safe set F of this structured form or a high-complexity mixed profile. The O(N) diagonal equality cover remains a hostile example: its output intervals are singletons and its actual profiles are prefix-constant, despite the much larger ambient safe selector cubes.

**Status:** the safe selector cube dimension is pinned to Theta(s2 n); no stronger local dimension charge is available. No bound on q, full-promise cover, or P-vs-NP proof follows. The next target is a grammar-wide theorem charging the geometry/description of free selector sets and the cross-block ownership masks they permit, or an explicit near-linear full-promise cover.
