# C-272 - Expander-overlap low code with high independent hybrids

Date: 27 September 2026  
Classification: **CALIBRATION.**  
Route: primary B, explicit CSP-style candidate family for synchronization versus splicing.

## Construction

Fix `N=2^n`, `s2=N^beta`, `s1=s2/(c n)` for a fixed `0<beta<1`. Choose a small constant `alpha>0` and a power of two `V=2^b` with `V=Theta(alpha s2)`. Choose alpha so that Lupanov's bound `O(V/b)` is at most `s1/8`. Then every Boolean labeling

```text
C : [V] -> {0,1}
```

has an `O(s1)`-gate circuit on the `b=log V` vertex-address bits.

Take a strongly explicit, connected, constant-degree expander `H` on `[V]`, with rotation map `Gamma(u,i)` for `i in [d0]`. For each directed incidence `(u,i)`, allocate `r` table coordinates, with

```text
E = V d0 r.
```

At every copy coordinate `(u,i,j)`, define the table

```text
w_C(u,i,j) = C(u) XOR C(Gamma(u,i));
```

and set any unused table coordinates to zero. The table is computed by two copies of the `C` circuit, an XOR, the expander's polylogarithmic neighbor circuit, and address decoding. For every fixed beta, the latter costs `poly(n)=o(s1)`, so `w_C in SIZE(s1)` after reducing the constant alpha if needed.

This is an overlapping-view family: each vertex label is shared by all incident edge constraints, and expansion gives

```text
dist(w_C,w_C') >= r h min(|supp(C XOR C')|, V-|supp(C XOR C')|)
```

for an expansion constant `h>0`. Independent choices on the edge-copy coordinates generally violate the cycle/coboundary constraints.

## Hybrid entropy calculation

Every assignment `y in {0,1}^E` defines a hybrid table `H_y` that writes `y_(u,i,j)` at each allocated coordinate and zero elsewhere. These `2^E` tables are distinct. Circuit counting gives

```text
log2 |SIZE(s2)| <= C0 s2 log2(s2+n) = O(beta s2 n).
```

Taking `r=K n` for a sufficiently large fixed K gives `E=Theta(s2 n)` and can make `E > log2 |SIZE(s2)|` by any desired constant factor. Hence all but at most `2^{log2|SIZE(s2)|}` of the hybrids are outside `SIZE(s2)`. The low family `{w_C}` therefore has a large, highly overlapped set of local views, while unconstrained edge-copy recombinations are almost all high.

If the construction is padded to use `E=Theta(N)` slots, an explicit equality/cycle-consistency checker costs `O(N)` states. If kept at the minimum entropy scale `E=Theta(s2 n)`, it costs only `o(N)` states. Thus one fixed expander does **not** imply superlinear q. It is a calibration object for a multi-family synchronization theorem, not a lower bound.

## Exact missing implication

For a native q-rule grammar, the construction alone does not show that an accepting proof for `w_C` contains independently replaceable occurrences for the `E` edge-copy coordinates. A reused state may carry a shared context that enforces cycle consistency, and C-247's multi-hole theorem requires private support regions that are not forced. In addition, one explicit expander's potential constraints admit a compact `O(N)` consistency check.

To turn this into Route B, one needs a family of many *incompatibly wired* explicit expanders/projection systems, all evaluated by size-s1 circuits, such that a q-state grammar either (i) exposes a product of edge choices exceeding `|SIZE(s2)|`, or (ii) represents enough distinct graph-dependent consistency relations to force `q>=N g(N)`. The complete missing arrow is from `q=O(N)` state reuse to simultaneous independent edge-copy replacements or to a superlinear cost for selecting among the expander systems. No proof of that arrow is known.

## Sources and project calibration

- Strongly explicit constant-degree expander families and neighbor/rotation maps: Reingold, Vadhan, and Wigderson, [*Entropy Waves, the Zig-Zag Graph Product, and New Constant-Degree Expanders*](https://arxiv.org/abs/math/0406038).
- The circuit-count and splice threshold are the OPS estimates already used in C-230/C-247.
- Mandatory hostile checks: the repeated-block equality fingerprint C-258 and parity lock C-257.

No fusion bound changes. The actual q lower bound remains `N-o(N)`.
