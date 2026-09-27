# C-281 — Native certificate reuse as a cylinder grammar and the owner-mask frontier

Date: 27 September 2026  
Classification: **CALIBRATION / GLOBAL-STRUCTURAL.** This adds an exact table-space form of C-260's splice law. It gives no new lower bound on the actual fusion measure.

## 1. Priority reset and frozen target

The active target remains

```text
rho_GapMCSP(n,beta) > N^(1+epsilon)
```

for a fixed `epsilon>0` and sufficiently small fixed `beta>0`. The proved actual lower bound remains `N-o(N)`. Per the latest research directive, the main route is native cyclic closure sharing and readout; matching-to-LowExt (C-261--C-280), ordinary rect-DAGs, local width, and feature counts are secondary unless they yield a global theorem or near-lossless transfer.

C-260 already supplied the antichain certificate grammar, blocker dual, and context/proof substitution law. This note translates that structure into partial truth tables and pushes the general owner-selector consequence. It does not repeat or replace C-260.

## 2. The cylinder-grammar algebra

Use the signed-feature set `Lambda=[N] x {0,1}`. A table `x` supplies `ell(x)={(k,x_k):k in[N]}`. A support `S subseteq Lambda` is consistent when it contains no opposite literals at one coordinate. It represents the partial assignment

```text
pi(S)_k = 0 or 1, if (k,that value) is in S;
          *,    if neither literal is in S;
          bottom if both are in S.
```

For consistent supports, define the partial-assignment join `pi(S) join pi(T)=pi(S union T)` when there is no conflict, and `bottom` otherwise. The cylinder `[S]` is the set of full tables extending `pi(S)`. Then

```text
[S union T] = [S] intersect [T]       when S union T is consistent;
[S union T] = empty                   when S union T is inconsistent.
```

Each native closure state `i` has the C-260 antichain `C_i` of minimal proof supports. In this notation the rule grammar is:

```text
left_i  = seed alternatives on E_i  OR predecessor states admitted by E_i
right_i = seed alternatives on H_i  OR predecessor states admitted by H_i
C_i     = Min( { L join R : L in left_i, R in right_i } )
```

Equivalently, on antichains of consistent supports define `A plus B = Min(A union B)` and `A times B = Min({a union b : a in A, b in B, a union b consistent})`. The empty family is zero and `{{empty}}` is one. Then each native rule is one multiplication of two sums, and the q-state closure is a cyclic circuit with q paid multiplications over this idempotent compatible-support semiring; fixed-point meaning selects the least solution. Output alternatives are the minimal members of the sum of the empty-carrier output-state families. This gives the project a concrete algebraic readout model: sharing is reuse of a semiring subexpression, and a splice is multiplication by a context polynomial.

The equations are interpreted by the least fixed point. A consistent output support `S` is sound exactly in the following strong sense:

```text
Cube(S) subseteq SIZE(s2).
```

This is the table-space obligation that every reusable proof/context splice must preserve.

## 3. Exact reuse law, with the table splice made explicit

Fix an accepting proof with a marked occurrence of state `i`. Cutting at that occurrence gives a context `K` and a replacement proof support `P` rooted at `i`. More generally let `K` range over all output contexts with a hole at `i`, and let `P` range over all finite proof supports rooted at `i`. By substitution,

```text
K union P is an accepting output support whenever K union P is consistent.
```

Consequently every such compatible join has its whole completion cylinder in `SIZE(s2)`. This is the full cross-product law: every context can be combined with every replacement proof at that state, subject only to literal consistency. Reuse does not force a join when the supports conflict.

Now label the chosen context by a low table `w` it matches (`K subseteq ell(w)`) and the replacement by a low table `w'` it matches (`P subseteq ell(w')`). For a compatible pair define its **owner mask**

```text
mu(K,P) = Var(P) minus Var(K),
```

where `Var(S)` is the set of coordinates mentioned by support `S`. Define the full table

```text
h_mu = (mu ? w' : w), coordinate by coordinate.
```

This is a completion of `K union P`: coordinates owned by `K` take `w`; coordinates owned only by `P` take `w'`; shared coordinates agree by compatibility; unmentioned coordinates take `w`. Therefore

```text
h_mu belongs to SIZE(s2).
```

This generalizes the disagreement-selector calculation from repeated anchors in C-236 to every compatible pair of low-table context and proof anchors. If `CC(mu)` is the circuit complexity of the owner mask as a Boolean function on the address, then

```text
CC(h_mu) <= CC(w) + CC(w') + CC(mu) + O(1).
```

So simple ownership masks are automatically safe at the OPS gap scale, while a useful contradiction must produce a *compatible* ownership mask whose hybrid is high. The mere fact that `w` and `w'` differ on many coordinates is insufficient.

For a fixed pair `(w,w')`, let `D={k:w_k != w'_k}`. The map from `mu restricted to D` to `h_mu` is injective. Hence the compatible owner masks generated at one state obey the exact cap

```text
| { mu(K,P) restricted to D : K,P compatible at i } |
    <= |SIZE(s2)|.
```

This is a safe-image bound, not a state lower bound. For typical distant anchors the set of all masks on `D` is exponentially larger than `SIZE(s2)`, but no theorem yet forces a small grammar to realize one of the unsafe masks.

## 4. What positive closure does and does not force

On arbitrary feature sets, each activation predicate is monotone: if `X subseteq X'` and state `i` activates on `X`, it activates on `X'`. Therefore a state-activating feature set is upward closed. On legal truth tables, however, the coordinatewise union of two anchors may contain both polarities at one coordinate and need not name any table. The only valid table-space operation is a consistent partial-assignment join. This distinction blocks a tempting but invalid argument from `sigma(w),sigma(w')` to an accepted Boolean hybrid.

The strongest automatic operation is therefore not “union two low tables.” It is:

1. take a context derivation and any replacement proof at their shared state;
2. reject the combination if their signed supports conflict;
3. otherwise accept every completion of the joined partial assignment.

The whole completion cylinder, rather than only its canonical owner-mask table, must stay inside `SIZE(s2)`. This is stronger than checking one selected hybrid, but C-221 already limits its free dimension to `log |SIZE(s2)|=O(s2 n)`. A q-sensitive theorem must exploit how the grammar organizes the compatible joins, beyond their width or their count.

## 5. Hostile checks and the exact failed implication

**Parity lock (C-257).** Even anchors versus odd high objects have dense high-side projections, full-width output certificates, and a linear native cover. Every compatible splice is still even. Thus the inference “state reuse plus full-width certificates forces a high hybrid” is false for arbitrary promises.

**Repeated-block equality (C-258).** An exponentially large repeated-table family has an `O(N)` native cover. Equality fingerprints make the compatible owner masks simple across the repeated blocks. Thus anchor abundance and raw mask counts do not charge states.

**Forced reuse does not fill the gap.** C-260 already pigeonholes the repeated-block low family so that one internal state serves at least `2^d/q` selected anchors. C-258 covers that same family in `O(N)` rules, showing that the collision can be protected by an equality fingerprint. The missing step is not proving reuse; it is proving a dangerous compatible product from reuse.

**One-anchor and fractional-cover ceilings.** A context/proof pair can have many compatible joins hit by the same blocker, and a low table can have many certificates. Neither incidence multiplicity nor a fractional cover yields an aggregate q-charge without a structural constraint on the mask family.

The gap is now stated precisely:

```text
small q
  => a constrained family of state-indexed context/proof owner masks
  => [missing] either an unsafe hybrid or a q-sensitive synchronization cost.
```

Counting all possible masks fails: even `q=Theta(N)` permits vastly more than `|SIZE(s2)|` syntactic support pairs. Counting low tables also fails because `log |SIZE(s1)|=N^(beta+o(1))` while q is already about N. The needed argument has to exploit incompatibility of global circuit descriptions, not cardinality alone.

## 6. Candidate next invariant: owner-mask product rank

For state `i` and a family `A` of low descriptions, form the relation `R_i` whose pairs `(d,d')` are joined by some compatible context for `TT(C_d)` and replacement proof for `TT(C_d')`. Attach the owner-mask set `M_i(d,d')` to each related pair. A candidate **owner-mask product rank** would measure the largest collection of coordinates/description slots for which:

1. replacement choices can be made independently in one state context product;
2. their owner masks act independently on those slots;
3. the resulting hybrid tables are distinct.

If a state exposes `t` independent binary switches on a pair that differs on every switch, then those joins yield `2^t` distinct tables, all in `SIZE(s2)`, and therefore `t<=log_2 |SIZE(s2)|=O(s2 n)`. If each switch instead has `2^m` choices, the same argument gives `tm<=O(s2 n)`. This is only a per-product entropy budget; it does not imply a lower bound on the number of states.

The missing theorem must force this rank across the full class of size-s1 circuits. A useful form would say that any grammar covering all `SIZE(s1)` tables must either (a) expose more than `O(s2 n)` independent owner choices in one compatible state/context product, contradicting soundness, or (b) use `N g(N)` states to keep the owner masks synchronized. C-258 and C-257 are mandatory counterchecks. No proof of this dichotomy is known.

## 7. Literature boundary

Paturi and Pudlák's *Circuit Lower Bounds and Linear Codes* studies the minimum number of sparse vectors needed to generate a linear space and derives bounds from code distance. That is a possible model for an artificial linear-code family, but no map from native context/proof grammars to sparse linear generators is known, so none of its bounds transfers here: [paper](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/PaturiPudlak_2006_jms.pdf).

Knowledge-compilation lower bounds for DNNF/d-DNNF and expander CNFs charge decomposable conjunction structure. A native state join may reuse the same table coordinates on both sides; decomposability is not part of the fusion definition. Those results become relevant only after proving a sound conversion that charges overlap: [Mengel, *Expander CNFs have Exponential DNNF Size*](https://www.lix.polytechnique.fr/~mengel/papers/cnf-to-dnnf-lower-bound.pdf). This is a direct technique boundary, not an exhaustive literature claim.

## 8. Result and continuation

The new exact formulation is the state-indexed **owner-mask product**, constrained by the condition that every compatible join cylinder is low. It unifies circuit-description synchronization with native proof reuse and gives a canonical table hybrid for every compatible splice. The attempted inference from many reused anchors to a high hybrid still fails without a q-dependent bound on the owner-mask product rank.

No change to the actual fusion lower bound: `q=N-o(N)`. No full-promise `N^(1+o(1))` cover, near-lossless transfer, superlinear actual-promise bound, or P-vs-NP proof has been obtained. Continue with a concrete product-rank lemma for one rich low-circuit subfamily and an explicit near-linear cover attack; do not spend the next phase sharpening local certificate width.
