# C-332 — MCSP branching-program hardness is promising, but the native game alternates

Date: 28 September 2026  
Route: transfer recent MCSP lower bounds through the exact C-319 game.  
Classification: **PROMISE-SIDE ARGUMENT TRANSFERS; PARAMETER AND NATIVE-MODEL TRANSFERS FAIL.**

## Literature result

Cheraghchi, Kabanets, Lu, and Myrisiotis prove that exact MCSP on N-bit truth tables needs general branching programs of size `N^2 / 2^(O(sqrt(log N))) = N^(2-o(1))`. Their proof uses a local PRG against size-S branching programs whose output tables have circuit complexity about `S^(1/2) * 2^(O(sqrt(log S)))`. [Primary paper, Theorem 2 and Section 5](https://www.cs.sfu.ca/~kabanets/papers/MCSP_lower_bounds.pdf).

## What survives for the low/high promise

The PRG argument only uses two sets of inputs: its outputs must be accepted as low-complexity tables, and uniform random tables must be rejected as high-complexity tables. It does not need correctness on the middle interval. Hence, for an ordinary branching-program separator of `SIZE(s1)` versus tables outside `SIZE(s2)`, the same argument gives the conditional implication

    local-output-complexity(S) <= s1
        and Pr_U[CC(U) > s2] = 1-o(1)
        => no size-S BP separator.

For fixed `s2=N^beta polylog(N)` with `beta<1`, the random-table condition follows from circuit counting. The known local-output bound is roughly `S^(1/2+o(1))`, and the paper's local-PRG construction is stated for `S>=N`. At the project's sufficiently small fixed beta, every such S has local output complexity much larger than `s1=N^beta`; the PRG condition needed for a contradiction never holds. The formal relation `S >= s1^(2-o(1))` would itself be below N and therefore gives no useful lower bound. Thus the low/high promise argument is logically compatible with the proof method, but its current parameters do not improve even the native `q=N-o(N)` floor.

## Exact model mismatch

C-319's q-state equations are not an ordinary branching program. Each state has two universal obligations, each followed by an existential choice among predecessor states or true seed literals, and cycles use least-fixed-point semantics. This is a cyclic alternating branching program (equivalently, a positive Boolean equation system), not a single input-labelled path model.

The existing q-to-circuit unrolling costs `q^2` AND gates. It does not give a near-linear general branching program: evaluating the fixed point can require retaining the active-state set, and removing alternation by enumerating strategies can be exponential. No semantics-preserving compiler from this exact game to a general BP of `O(q polylog N)` size is established. The known `N^(2-o(1))` BP lower bound therefore cannot be applied to q directly.

## New technical target

This identifies a concrete route distinct from raw state statistics:

1. Prove a local-PRG/shrinkage theorem directly for q-state positive alternating reachability systems, with every PRG output table of circuit size below `s1` when q is near-linear; or
2. prove an alternation-elimination compiler of size `q polylog N` for sound full-promise covers; or
3. show such a compiler is impossible and quantify the additional commitment/alternation resource.

The existing BP shrinkage exponent `1/2` is insufficient for sufficiently small fixed beta, even if it transferred. Any direct native-game shrinkage theorem must do materially better and pass C-257 parity, which has a linear native cover and remains nonconstant under ordinary restrictions leaving free bits.

## Disposition

The BP paper gives a useful model boundary and a conditional promise-transfer template, not a P-vs-NP result and not a q lower bound. Keep Q186/O-181 active only for the alternating-model PRG theorem or a valid near-linear compiler. Actual `rho_GapMCSP=N-o(N)` is unchanged; no near-linear cover, positive CohEnc margin, or reconstruction compiler was found.
