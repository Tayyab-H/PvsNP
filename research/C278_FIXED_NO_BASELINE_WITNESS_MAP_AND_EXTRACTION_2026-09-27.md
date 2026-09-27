# C-278 — A fixed NO scaffold makes witness-only LowExt maps pay full source cost

Date: 27 September 2026  
Classification: **ROUTE-KILL.** Scope: fixed-scaffold witness-union maps.  
Route: A4, monotone source map into signed partial tables.

## Claim

Let `f:X->{0,1}` be a source function with nonempty NO and YES sets, and let `Y` be a class of low tables. Consider a coordinatewise-monotone multi-output map `phi` into `2N` signed rails. Suppose there is one fixed partial rail vector `P` such that:

1. `phi(x)=P OR psi(x)` for every source input, where OR is coordinatewise and `psi` is the excess vector (copy `phi` on rails where `P=0`, and set the `P=1` rails to zero; thus `psi` is also monotone);
2. `psi(x)=0` on every NO input;
3. every YES input has a low witness `w in Y` with `e(w)<=phi(x)`.

Suppose also that `P` is a valid NO image lying below a high code, as required by C-125. Then `P` contains no low code: if `e(u)<=P` for some `u in Y`, the same low code would lie below the NO image and contradict the high-completion condition, since distinct complete one-hot codes are incomparable.

Now define the monotone predicate

```text
g(x) = OR over all 2N output rails of psi(x).
```

On NO inputs, `g=0` by condition 2. On a YES input, choose its C-125 witness `w`. Since `e(w)<=P OR psi(x)` but `e(w)` is not below `P`, at least one rail of `psi(x)` is set, so `g=1`. Hence `g=f` exactly.

If the whole map `phi` uses `a` AND gates, `g` has a monotone acyclic circuit using at most those same `a` AND gates: remove the fixed baseline outputs and OR the remaining outputs, which costs no AND gates. Therefore

```text
CycAnd(f) <= a.
```

Such a map cannot transfer a lower bound `L=CycAnd(f)` into `q>=L-a` with any positive margin.

## Construction classes eliminated

This covers the canonical witness-union map

```text
psi_(i,b)(G) = 1 iff G contains a YES witness M whose low code w_M has w_M[i]=b,
```

with `P=0`: NO graphs have no witness terms, while any YES witness contributes its full low code. It also covers adding any fixed NO scaffold `P`, including a fixed high one-hot baseline, provided all input-dependent additions vanish on NO inputs. The particular circuits used to recognize the witness family do not matter; the obstruction follows from the output semantics alone.

This is stronger than a term-count estimate: even if the witness ORs are factored into a compact shared positive-AND circuit, that very circuit already computes the source by ORing its excess rails.

## Scope and surviving requirement

The argument does not apply when the NO-side partial image varies with the source input. A useful map must leave nontrivial, input-dependent decoy rails on NO instances, yet those rails must remain below some high completion and must not create a low completion. It must also activate low codes on every YES input, have `a<L-N^(1+epsilon)`, and have global YES conflict support above the C-275 threshold. This pins down a concrete asymmetry needed by Route A; it does not prove that no such map exists.

The actual fusion lower bound remains `q=N-o(N)`. No P-vs-NP result follows.
