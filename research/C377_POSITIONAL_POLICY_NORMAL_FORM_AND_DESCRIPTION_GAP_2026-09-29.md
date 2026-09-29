# C-377 - Positional policies give global proof choices, but not circuit descriptions

Date: 29 September 2026  
Route: strengthen C-376's paired mismatch interaction using positional determinacy of finite reachability games.  
Classification: **EXACT POLICY NORMAL FORM + CUBE CEILING; NO q IMPROVEMENT.**

## 1. A winning policy can be fixed globally for each low table

Fix a valid q-pair C-319 cover and a low table w. The closure is a finite reachability game: at state i the universal player chooses E or H, then the existential player selects either a true signed-literal seed on that side or an allowed predecessor. Since the objective is reachability of a seed, positional determinacy gives a winning existential strategy whenever an empty-consequence root is active on w.

Fix one such root and strategy pi. For every state-side pair reached under pi, the strategy chooses exactly one action: a signed-literal seed, a constant-true seed when the endpoint is the whole universe, or a fixed predecessor state. There are at most 2q relevant choices. The graph of chosen predecessor actions reachable from the root is acyclic: if it contained a reachable cycle, the universal player could follow the corresponding side choices forever, contradicting that pi wins a reachability game.

Conversely, any root and positional action table whose reachable predecessor graph is acyclic and whose selected seed literals are true on w certifies that the root is active. Thus the accepted set of a fixed native graph is a union of regions indexed by root-policy pairs.

## 2. Each fixed policy gives a safe coordinate cube

Let C_pi be the set of all truth tables satisfying every nonconstant signed literal selected by pi at its seed exits. The predecessor choices, constant seeds, and reachable policy graph are fixed. For every u in C_pi, the same finite policy still terminates at true seeds, so the same root is active on u.

Soundness of the cover rejects every table with circuit complexity greater than s2. Therefore C_pi is contained in SIZE(s2), including when the promise itself omits the medium band. If t_pi is the number of distinct table coordinates fixed by the selected literals, then

    2^(N-t_pi) <= |SIZE(s2)|,
    t_pi >= N - log2 |SIZE(s2)| = N-o(N).

Since a policy has at most 2q seed exits, this yields q >= (N-o(N))/2. It is weaker than the existing q >= N-o(N) bound. It also recovers the basic safe-cube certificate interpretation without using the larger seed-clause CNF regions of C-368.

## 3. Why the global policy does not yet solve description coherence

Positional determinacy is a genuine strengthening of C-376: for each fixed low table, one policy is consistent across all opponent histories and all branches of that game. But the policy may vary with the low table, and its actions need not encode any small circuit for that table. A policy can simply select many raw table literals. No theorem extracts a size-s1 circuit description from it.

The number of possible root-policy pairs is at most

    q * (q + 2N + 1)^(2q),

which is far too large near q=N. Nor can policy counting alone help: a complete cover can choose one policy per low table, while log2 |SIZE(s1)| = N^(beta+o(1)) = o(N). C-374 already closes cardinality-only charging.

The universal-circuit strategy idea therefore reaches a precise unresolved step: a positional policy could serve as a shared description register, but a valid cover is not required to use that register as a circuit description. Turning this possibility into a proof needs a state-graph theorem that forces coherent circuit information, or a C-281-compatible cross-policy splice that charges reuse. Merely fixing a winning strategy gives only a sound cube.

## 4. Checkpoint

- Exact result: every accepted low table has a globally positional winning policy for the C-319 reachability game.
- Exact geometric consequence: each fixed policy accepts a safe coordinate cube fixing at least N-o(N) bits.
- Route limit: this recovers at most q >= (N-o(N))/2 and does not improve the known bound.
- Missing theorem: force the policy action table to encode one circuit description, or charge cross-anchor policy reuse through the native transition graph.
- Native lower bound remains q >= N-o(N). No full-promise near-linear cover, positive LowExt transfer, or P-vs-NP proof has been obtained.
