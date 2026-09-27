# C-253 — Conflict-profile fibres lie in marker subcubes

Date: 27 September 2026  
Route: push C-252's state-conflict readout through the fibres of the activation map.  
Status: exact fibre lemma and entropy corollary proved; the resulting count does not improve the linear q floor.

## 1. Profile and marker definitions

Use the C-252 state-conflict relation `G` and state/literal incidence set `S`. For a table `x`, its activation profile is

\[
\sigma(x)=\{j\in[q]:x\in A_j\}.
\]

For each q-bit profile `sigma`, let `F_sigma = {x : sigma(x)=sigma}` be its fibre. Call sigma G-independent if it contains no pair from G. For a G-independent profile define its marker vocabulary

\[
B_\sigma=\{(\ell,b):\exists j\in\sigma\ (j,\ell,b)\in S\},
\]

and let `r_sigma` be the number of distinct coordinates appearing in `B_sigma`.

## 2. Theorem: fibre localization

For every profile sigma:

1. If sigma contains a G-edge, then `F_sigma subseteq L`.
2. If sigma is G-independent, then

   \[
   Y\cap F_\sigma\subseteq\{x:\exists(\ell,b)\in B_\sigma,\ x_\ell=b\},
   \]

   while

   \[
   U\cap F_\sigma\subseteq\{x:\forall(\ell,b)\in B_\sigma,\ x_\ell=1-b\}.
   \]

   If `B_sigma` contains both polarities of one coordinate, the high fibre is empty. Otherwise every marked coordinate is fixed to one polarity throughout the high fibre, so

   \[
   |U\cap F_\sigma|\le 2^{N-r_\sigma}.
   \]

### Proof

If sigma contains an edge `(j,k) in G`, every table in its fibre activates j and k, so C-252's high-free pair lemma puts the whole fibre in L.

Otherwise, for any `x in Y intersect F_sigma`, C-252's readout cannot be witnessed by an edge; it must be witnessed by some active state `j in sigma` and an incidence `(j,ell,b) in S`. Thus x matches a marker in `B_sigma`. For any `z in U intersect F_sigma`, the same incidence is forbidden by C-252, so z matches none of the marker literals. If a coordinate has both polarities in `B_sigma`, no Boolean z can avoid them both. If it has exactly one marked polarity, all high tables in this fibre must take the opposite bit there. The r_sigma fixed coordinates leave at most `2^(N-r_sigma)` possible tables. \(\square\)

## 3. High-side entropy corollary

Let `I` be the number of G-independent profiles with a nonempty high fibre, and let `r_min` be the minimum `r_sigma` over those profiles. Since the high fibres partition U,

\[
1-\frac{|L|}{2^N}=\frac{|U|}{2^N}
\le \sum_{\sigma:U\cap F_\sigma\ne\varnothing}2^{-r_\sigma}
\le I\,2^{-r_{\min}}.
\]

Therefore

\[
r_{\min}\le\log_2 I-\log_2\left(1-\frac{|L|}{2^N}\right)\le q+1
\]

once `|L|/2^N < 1/2`, as in the OPS regime. More generally, the relevant count is the number I of independent profiles actually realized on high inputs, not all `2^q` profiles.

## 4. Exact failure and next target

The inequality only guarantees that at least one high profile has a small marker set. It does not say this profile is used by any low input, and it gives no lower bound on `r_min`: an independent high profile with no markers has `r_sigma=0`. Profiles containing a conflict edge may have arbitrary low-fibre size up to `|L|`; marker-bearing independent profiles can partition high inputs among many subcubes. Two-coordinate shattering of U does not help by itself, because one unmarked profile can support all four bit patterns on every coordinate pair.

Thus the graph/fibre route still needs a closure-specific link between profiles used by low proofs and profiles carrying most of U. A viable next result would constrain how the positive cyclic equations move between these fibre types under coordinate flips or partial assignments, using C-74/C-75 activation semantics rather than graph counts alone. C-253 yields no superlinear lower bound, near-linear full-promise cover, or P-vs-NP proof.
