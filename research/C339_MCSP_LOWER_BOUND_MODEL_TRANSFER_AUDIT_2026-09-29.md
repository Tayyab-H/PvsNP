# C-339 - Known MCSP lower bounds do not reach the C-307 separator measure

Date: 29 September 2026  
Route: test whether current MCSP lower bounds on formulas, branching programs, or proof systems imply the ordinary-circuit threshold needed to lower-bound native q.  
Classification: **MODEL-TRANSFER AUDIT / NO Q IMPROVEMENT.**

## 1. The exact threshold required by C-307

For a q-pair separator, the established unrolling compiler gives a signed monotone acyclic separator with A_cap <= q^2 paid AND gates. Therefore a lower bound A_cap >= L implies only

    q >= sqrt(L).

A superlinear target q >= N^(1+epsilon) requires L >= N^(2+2epsilon). C-307 also gives the reverse construction: an A_cap separator yields a native cover with at most A_cap pairs when every signed half-cube meets the high set. The unresolved quantity is thus a promise-specific lower bound on the signed monotone shared-DAG AND measure A_cap itself.

## 2. Why the known MCSP bounds do not imply that threshold

Cheraghchi, Kabanets, Lu, and Myrisiotis prove for exact MCSP lower bounds of N^(3-o(1)) for De Morgan formulas and N^(2-o(1)) for arbitrary-basis formulas and general branching programs; depth-two CNF/DNF has a much larger lower bound. Their paper is [Circuit Lower Bounds for MCSP from Local Pseudorandom Generators](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.39).

The formula bounds would exceed the C-307 threshold if the compiled separator were a formula of comparable size. It is a shared DAG, however. Expanding an acyclic monotone circuit or the q-state fixed point into a formula can duplicate a state exponentially many times; the project's safe generic fixed-point formula expansion is already 2^(O(q log q)). No near-linear formula compiler for the exact separator is known. Thus N^(3-o(1)) formula complexity gives no useful q lower bound here.

The N^(2-o(1)) branching-program bound is also in the wrong model. The C-319 recurrence is a cyclic, universally alternating least-fixed-point system, not an ordinary branching program. C-332 established that the known promise-compatible local-PRG argument has no parameter win at small beta and that no q-preserving alternation-elimination compiler is available. A branching-program lower bound cannot be applied to A_cap without such a compiler.

Austrin-Risse prove strong Sum-of-Squares proof-degree lower bounds for MCSP and analogous statements for minimum monotone circuit size of monotone slice functions; these concern proof complexity, not the circuit size of a full-promise Gap-MCSP separator. See [their CCC 2023 paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2023.31). The July 2026 monotone-learning result is conditional rETH hardness for sample-based learning/partial size, not an unconditional lower bound on A_cap; see [arXiv:2607.12331](https://arxiv.org/abs/2607.12331) and C-338.

C-307's direct CNF lower bound does apply to the promise, but only when the separator is itself a CNF. It does not extend through arbitrary sharing of AND subexpressions, which is exactly what A_cap allows.

## 3. Route decision

No cited bound gives A_cap > N^2 for unrestricted signed monotone shared-DAG separators on the full OPS promise, and no lower-bound-preserving compiler places the exact q-state game in one of the cited stronger models. Repackaging these bounds would not establish a q gain. Keep the requirement explicit: either prove a new lower bound directly for the signed monotone shared-DAG measure, or prove a near-linear full-promise separator. The activity/prototype selectors in C-337 remain restricted calibrations, not full covers.

The proved lower bound remains rho_GapMCSP >= N-o(N). No superlinear q bound, full-promise N^(1+o(1)) cover, positive CohEnc margin, or P-vs-NP proof follows from this audit.
