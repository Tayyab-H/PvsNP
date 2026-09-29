# C-386 — Positional strategy is not a caller-readable description register

Date: 29 September 2026  
Route: Recheck whether existential positional choices in the C-319 game can hold a global circuit description and later supply it to address checks.  
Classification: **CLOSED ARCHITECTURE CHECK; NO NEW q BOUND OR COVER.**

## Question

Could the winning positional strategy itself encode one circuit description (d), then let the universal player challenge an address (a) and have the existential player evaluate (d(a)), avoiding explicit gate-by-address states?

## Exact state-merging fact

Fix a table (w) and a C-319 graph. The continuation from position ((i,E)) or ((i,H)) depends only on that position, the fixed graph, and the seed-clause values on (w). If two histories end at the same position, they have identical winning continuations. Equivalently, the least-fixed-point value (x_i(w)) is one Boolean for the whole input; it has no caller/address argument. A positional strategy also assigns one action to that same state-side pair, regardless of the history that reached it.

Therefore, if address contexts (a) and (a') enter one shared selector state-side, the selector cannot later return to different callers. Its chosen successor can carry a new state label, but that state does not inherit the incoming address. Keeping both labels explicitly requires product states or a separate, proved readout channel. This is exactly the construction-specific obstruction already established in C-341/C-342; this recheck adds no stronger statement.

## Why a strategy can encode bits without making them readable

A positional action table has enough choices to encode a description. That is only storage in the strategy. To validate the description, the game must make its selected bits affect later continuations. The C-319 recurrence exposes only seed predicates and fixed predecessor incidence to those continuations; it has no operation that reads an earlier action as a value while restoring the address/caller that requested it. A successor state makes the selected action observable on that play, but merging routes through that state again erases their distinct callers. Thus a path-only description register does not solve the all-address check.

The input-derived activation profile remains a different possibility: it is an actual vector of Boolean values determined by (w), and at (q=\Theta(N)) its raw capacity is not the obstacle (C-342/C-383). No method has been found to select a valid circuit description in that profile and make every address check read it coherently. This audit does not rule that channel out.

## Why this does not imply a native lower bound

The state-merging argument applies only when a proposed verifier asks a shared state to perform specified residual queries. An arbitrary sound C-319 cover need not evaluate a supplied circuit gate-by-gate or extract any circuit witness. For a fixed circuit (C), equality (w=\mathrm{tt}(C)) already has an (O(N))-literal check, and a gate/address matrix depends on the chosen representation (C-384). So neither the caller-loss fact nor a product count for one evaluator architecture charges arbitrary covers.

The generic game-form compiler also leaves a genuine model gap: unrolling q least-fixed-point states gives an (O(q^2)) monotone-circuit upper bound, but no converse lower bound. Pauly’s *Parameterized Games and Parameterized Automata*, Open Question 11, explicitly asks about the monotone-circuit size of least-fixed-point functions defined by graph-game forms: https://arxiv.org/abs/1809.03093. The paper supplies no Gap-MCSP-specific estimate.

## Research consequence

Retire another attempt to use positional choices alone as a persistent circuit register. Reopen that architecture only with an explicit activation-profile/readout construction whose seed predicates and endpoint-induced transitions are fully specified and whose soundness is proved on every high table. Otherwise continue on the promise-specific least-fixed-point readout lower bound or an endpoint-realizable (q=N^{1+o(1)}) cover.

Checkpoint: the native lower bound remains (q\ge N-o(N)). No superlinear lower bound, full-promise near-linear cover, positive transfer, or P-vs-NP proof is established.
