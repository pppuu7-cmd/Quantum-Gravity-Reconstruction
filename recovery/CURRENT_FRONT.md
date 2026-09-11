# QGR Current Research Front

Updated: 2026-09-11
Active iteration: `Iter005`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / LINEARIZED_GAUGE_CLOSED_CANDIDATE`
Active roadmap stage: `R4->R5 bridge — nonlinear constraint/self-coupling and same-realization refinement`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **36%**
- Iter004 completion: **100%**
- Iter005 completion: **15%**
- Lead architecture: `A / CCRC`
- Active candidate: `QGR-L1`
- Candidate state: `PROPOSED_LINEARIZED_GAUGE_CLOSED_CAUSAL_TWO_MODE / NONLINEAR_OPEN`
- Linearized masslessness protected: **YES, scoped**
- Zero-derivative cubic potential sector: **CLOSED / 20 of 20 S4 directions excluded**
- Full nonlinear theory established: **NO**
- Einstein equations derived: **NO**
- Independent benchmark passed: **NO**
- KMQGB `NEW_REQUIRED` authorization: **NO**

Readiness is an internal construction-roadmap metric, not probability of correctness.

## Iter004 closed result

The original six-component QGR-L0 arena fails the complete local `S4` two-derivative derivative-gauge audit. A natural unreduced response arena was then derived from the existing four rank-1 relational directions:

`W4 -> Sym^2(W4) -> 10 components`.

Within this arena, derivative Noether closure leaves a two-dimensional quadratic Hessian family. Prior QGR data — the incidence cone and exact two-mode quotient — uniquely select QGR-L1 up to normalization. The selected branch has exactly two physical null modes on the incidence cone and forbids every `S4`-invariant onsite quadratic mass deformation.

A posteriori only, QGR-L1 coincides up to scale with the standard massless Fierz-Pauli quadratic operator in the tetrahedral null frame `C=J-I`. This was not used to select it.

Authoritative record: `iterations/ITERATION_004.md`.

## Iter005 G1A result

The ten-component QGR-L1 field `H=Sym^2(W4)` admits exactly **20** `S4`-invariant zero-derivative cubic invariants before gauge constraints.

For constant `h` and affine gauge parameter `xi`,

`delta_0 h_ij = D_i xi_j + D_j xi_i`

spans arbitrary constant symmetric shifts in all ten field components. Since the quadratic action is derivative-only, no local variation of `S2` can cancel an arbitrary algebraic cubic variation on constant fields.

Therefore

`V_3(h)=0`,

and all **20/20** zero-derivative cubic directions are excluded.

Classification:

`PASS_SCOPED_20_S4_CUBIC_POTENTIALS_CENSUSED_AND_ALL_EXCLUDED_BY_DERIVED_AFFINE_GAUGE_SHIFT`.

Records:

- `results/ITER005_G1A_CUBIC_POTENTIAL_CENSUS.md`
- `code/qgr_iter005_g1a_cubic_potential_census.py`

## Active blocker

`BLOCKED_MISSING_COMPLETE_TWO_DERIVATIVE_CUBIC_CENSUS_AND_ORDER_BY_ORDER_NOETHER_SOLUTION_FOR_QGR_L1_WITHOUT_POST_HOC_EINSTEIN_HILBERT_INSERTION`

## Active gate — Iter005-G1B

`QGR-ITER005-G1B-TWO_DERIVATIVE_CUBIC_CENSUS_AND_NOETHER_SYSTEM`

1. Enumerate local `S4`-invariant cubic terms with exactly two first-neighbor derivatives.
2. Remove integration-by-parts / field-permutation redundancies.
3. Derive the most general first nonlinear gauge correction allowed by relational frame composition.
4. Solve `delta_0 S_3 + delta_1 S_2 = 0` exactly.
5. Count surviving coupling directions before any comparison with Einstein-Hilbert.
6. If no internal QGR principle selects among multiple surviving directions, record `BLOCKED_UNDERDETERMINED` rather than choosing the GR-like interaction.

## Subsequent gates

- G2: nonlinear gauge-algebra closure;
- G3: weak-background causal-cone stability;
- G4: same-realization refinement/coarse-graining handoff.

## KMQGB synchronization

Last inspected KMQGB head: `f503c39177012879a80bf767282a15d0c441e2f9` (Iter324-325 merge). Global D7 remains unauthorized in the inspected snapshot.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `iterations/ITERATION_005.md`
4. `results/ITER005_G1A_CUBIC_POTENTIAL_CENSUS.md`
5. `iterations/ITERATION_004.md`
6. `results/ITER004_G6_SELECT_L1.md`
7. `docs/CONSTITUTION.md`
8. newest Iter005 results/code
9. current KMQGB front and recent commits
