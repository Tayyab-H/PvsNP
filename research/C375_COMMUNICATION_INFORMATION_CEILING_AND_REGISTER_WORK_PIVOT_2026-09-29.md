# C-375 - Communication information saturates; the live resource is recurrent work

Date: 29 September 2026  
Route: audit whether a communication-complexity formulation of the C-341 address/description relation can yield a superlinear native state bound.  
Classification: **EXACT ROUTE CEILING + MECHANISM PIVOT; NO q IMPROVEMENT.**

## 1. The bit-communication ceiling

Let a truth table be split between two parties on coordinate sets (X,Y), with (|X|+|Y|=N). For any fixed promise separator on the table, deterministic communication is at most

\[
\min(|X|,|Y|)+O(1)\le N/2+O(1):
\]

the party holding the smaller block sends it, and the other evaluates the separator. This applies to the Gap-MCSP promise predicate regardless of its computational difficulty. If a proposed description/address relation additionally gives one party a circuit description of length (d=O(s_1\log s_1)=o(N)), the same send-the-input argument is still (O(N)).

Therefore a reduction whose only conclusion is

\[
q\ge c\,\mathrm{CC}(F)-O(1)
\]

for ordinary deterministic bit communication cannot prove (q>N^{1+\epsilon}). This is a ceiling on that transfer, not on all communication-inspired arguments: rectangle partition counts, state capacity, or a nonlinear conversion from communication to q would need their own proof and are not ruled out here.

## 2. Why the ceiling matters for the current selector plan

The fixed-circuit address-by-gate selector already has a trivial row-slice partition with at most (O(N)) rectangles (C-359). Adding the explicit low-table/description coordinate avoids that particular row-only defect, but it does not evade the information ceiling: the whole table and a succinct description contain only (O(N)) bits. Thus ordinary communication bits can at most recover a linear-scale obstruction. They do not measure the extra computation needed to preserve one circuit description while evaluating it at every address.

The attachment's Myhill-Nerode, fooling-set, and communication suggestions remain viable only if they yield a **direct state-count** theorem, or a measure whose conversion to q is demonstrably superlinear. A protocol-bit lower bound by itself is now retired as the primary route.

## 3. The computational object left after information is exhausted

For a C-319 list, let (a_i(w),b_i(w)) be its (2q) endpoint-selected OR-of-literal seed values. These are an input channel, not free wires. Nevertheless, (N) singleton positive-literal seeds can make the conceptual seed signature injective on all (N)-bit tables (C-363). So the unresolved issue is not how many bits of the table are visible; it is what the fixed paired recurrence can compute from those bits.

Unrolling the exact least-fixed-point equations for at most q strict rounds gives at most (q^2) AND occurrences, plus unbounded-fan-in OR operations and the endpoint-induced literal exits. Hence a theorem that every such separator needs (A(N)) paid AND gates would imply

\[
q\ge\sqrt{A(N)}.
\]

To cross (q=N^{1+\epsilon}) by this compiler would require (A(N)>N^{2+2\epsilon}). The parameterized SCC compiler C-323 can improve this only if one proves a suitable root-free SCC profile; C-339 explains why known formula, branching-program, CNF/DNF, and SoS bounds do not supply the needed unrestricted (A_{\rm cap}) bound. This is a target specification, not a new lower bound.

The precise remaining object is the **registered monotone decoder**: (2q) fixed OR-of-signed-literal observations feed q paired state equations, iterated to their least fixed point. A successful attack must lower-bound its register/state count on the actual OPS promise, not just its observation count, ordinary communication, or unrolled gate count. An equally decisive alternative remains an explicit (N^{1+o(1)}) full-promise construction for that decoder.

## 4. Checkpoint

- Native lower bound: still (q\ge N-o(N)).
- C-341 state-capacity theorem: not proved.
- Selector-induced C-320 forbidden splice: not proved.
- Full-promise near-linear cover: not constructed.
- Ordinary communication-bit route: closed for a superlinear conclusion under a linear q-to-communication transfer.
- Live mechanism: direct computational/state-reuse lower bound for the recurrent readout, or a full-promise construction.

No P-vs-NP proof follows. The goal remains active.
