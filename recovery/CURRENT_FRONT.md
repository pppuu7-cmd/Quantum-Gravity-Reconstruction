# QGR Current Research Front

Updated: 2026-09-11
Active iteration: `Iter005`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / LINEARIZED_GAUGE_CLOSED_CANDIDATE`
Active roadmap stage: `R4->R5 bridge — nonlinear constraint/self-coupling and same-realization refinement`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **36%**
- Iter004 completion: **100%**
- Iter005 completion: **0%**
- Lead architecture: `A / CCRC`
- Active candidate: `QGR-L1`
- Candidate state: `PROPOSED_LINEARIZED_GAUGE_CLOSED_CAUSAL_TWO_MODE / NONLINEAR_OPEN`
- Linearized masslessness protected: **YES, scoped**
- Full nonlinear theory established: **NO**
- Einstein equations derived: **NO**
- Independent benchmark passed: **NO**
- KMQGB `NEW_REQUIRED` authorization: **NO**

Readiness is an internal construction-roadmap metric, not probability of correctness.

## Iter004 closed result

The original six-component QGR-L0 arena fails a complete `S4`-invariant local two-derivative derivative-gauge audit: the natural symmetric coboundary admits only the zero Hessian. This identified the six-field realization as too strongly pre-reduced for derivative Noether closure.

A natural unreduced arena was then derived without adding repeated Boolean events:

`four rank-1 relational directions W4 -> Sym^2(W4) -> 10 second-moment components`.

The old six Boolean pair responses remain the canonical off-diagonal subspace; four self-response components supply the missing unreduced sector.

On this 10D arena:

- complete local `S4`-invariant two-derivative Hessian family: 38 orbit coefficients;
- derivative Noether identity leaves a 2D nonzero Hessian family;
- exact embedding of old QGR-L0 kinetic operator is impossible except trivially;
- incidence-cover characteristic condition reduces the family to two discrete branches;
- the independently derived 2D physical quotient selects one branch uniquely up to normalization;
- selected `QGR-L1` has rank 4 on tested incidence-null covectors and rank 6 off cone;
- all seven `S4`-invariant onsite quadratic mass deformations are forbidden by the derivative Noether identity.

A posteriori only, the selected quadratic Hessian coincides up to scale with the standard massless Fierz-Pauli kinetic operator in the tetrahedral null frame with contravariant form `C=J-I`. This was not used as a selection criterion.

Authoritative records:

- `iterations/ITERATION_004.md`
- `results/ITER004_G4_DERIVATIVE_CONSTRAINT_AUDIT.md`
- `results/ITER004_G5_SECOND_MOMENT_ARENA.md`
- `results/ITER004_G6_SELECT_L1.md`

Reproducibility:

- `code/qgr_iter004_g4_derivative_constraint_audit.py`
- `code/qgr_iter004_g5_second_moment_arena.py`
- `code/qgr_iter004_g6_select_l1.py`

## What is genuinely closed

At linearized level, QGR-L1 now has:

- an independently motivated unreduced tensor-response arena;
- a derivative gauge/Noether identity;
- a uniquely selected causal two-mode kinetic branch;
- a characteristic cone matching the earlier incidence cone on tested nontrivial rational null covectors;
- structural exclusion of onsite quadratic mass terms.

## What is not closed

No claim is made yet for:

- nonlinear gauge algebra;
- nonlinear self-coupling;
- finite exact transformation law beyond linear response;
- Einstein equations;
- equivalence principle;
- continuum/refinement theorem;
- finite interacting quantum measure/amplitude;
- normalized observables;
- experimental prediction;
- independent KMQGB pass.

## Active blocker

`BLOCKED_MISSING_NONLINEAR_RELATIONAL_CONSTRAINT_ALGEBRA_AND_SELF_COUPLING_COMPLETION_OF_QGR_L1_WITHOUT_POST_HOC_EINSTEIN_HILBERT_INSERTION_PLUS_SAME_REALIZATION_REFINEMENT_CONTROL`

## Active gate — Iter005

`QGR-ITER005-NONLINEAR-CONSTRAINT-AND-SELF-COUPLING-CLOSURE`

1. Start from QGR-L1 and the finite relational/second-moment ontology, not from continuum GR.
2. Enumerate the lowest-order local cubic deformations compatible with `S4`, incidence locality, and the existing derivative gauge identity.
3. Derive the first nonlinear correction to the gauge transformation from relational composition if it exists.
4. Test Noether consistency order-by-order.
5. Determine whether self-coupling is unique/low-dimensional or underdetermined.
6. Check whether the incidence causal cone survives weak nonlinear backgrounds.
7. Reject any branch whose justification is simply “use Einstein-Hilbert because it works.”
8. Begin same-realization refinement/coarse-graining only after a nonlinear candidate survives the local closure gate.

## KMQGB synchronization

Last inspected KMQGB head: `f503c39177012879a80bf767282a15d0c441e2f9` (Iter324-325 merge). Global D7 remains unauthorized in the inspected snapshot.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `iterations/ITERATION_005.md`
4. `iterations/ITERATION_004.md`
5. `results/ITER004_G6_SELECT_L1.md`
6. `docs/CONSTITUTION.md`
7. newest Iter005 results/code
8. current KMQGB front and recent commits
