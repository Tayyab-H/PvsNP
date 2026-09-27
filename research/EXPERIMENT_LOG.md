# Experiment log

No experiment was run during this reconstruction turn. Computation remains counterexample search and implementation checking, not proof.

## E-01   Proof-DAG leaf checker

- **Hypothesis:** Small pair lists  first empty-intersection derivations have at most m+1 generator leaves.
- **Construction / parameters:** experiment_proof_dag_leaf_bound.py checked all 263,168 one- and two-rule cases in a four-point toy.
- **Result:** All 45,606 empty derivations had empty leaf intersection and at most k+1 leaves for k rule nodes.
- **Interpretation:** Supports the trace implementation and the linear lower-bound argument.
- **Theorem suggested:** General per-anchor matching-literal leaf bound.
- **Why not a theorem by itself:** Finite check only; even the asymptotic lemma yields N-o(N), not superlinear.

## E-02   Canonical and feature-span cover searches

- **Hypothesis:** Canonical literal, graph, majority, Reed Muller, affine-orbit, and q-ary features can force many pairs.
- **Construction / parameters:** Exhaustive small closure checks and algebraic arguments in synthesis  14 and 23 25.
- **Result:** These candidate families admit one-pair covers under stated conditions; the unrestricted row/column proxy has cover at most one.
- **Interpretation:** These families do not prove the desired bound.
- **Theorem suggested:** A successful family must evade disjoint information-set and sparse-generator covers.
- **Why not a general obstruction:** Arbitrary noncanonical semi-filters remain.

## E-03   Affine control algorithm

- **Hypothesis:** Enumerating a low-rank affine projection of selected AND inputs decides SAT in time 2^r poly(N).
- **Construction / parameters:** experiment_affine_control_rank.py and related project proof.
- **Result:** Exact algorithm for XOR/NOT/AND circuits; optimal control selection is Rank Vertex Cover and is FPT in r.
- **Interpretation:** Useful on structured circuits.
- **Theorem suggested:** A universal small-rank bound would imply polynomial SAT.
- **Why not a separation:** No such bound holds for arbitrary circuits; native structure is required.

## E-04   Current turn: circuit-transfer audit

- **Hypothesis:** Does fusion transfer the project promise-cover measure to arbitrary separators?
- **Method:** Match Gamma=Y union Z, A=Y, U=Z, B=restricted input literals and apply rho<=D_cap.
- **Result:** Yes, for this exact definition. The local one-way compiler is not needed for the lower-bound direction.
- **Interpretation:** Closes a potential bridge objection; isolates the open work at the superlinear lower bound.
- **Why not a breakthrough:** This verifies a published implication and does not improve the linear bound.
