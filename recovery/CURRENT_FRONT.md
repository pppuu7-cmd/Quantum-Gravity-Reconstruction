# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter034`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / GLOBAL-BRANCH REGULARITY STRESS`
Active roadmap stage: `projective refinement limit -> uniform torsion regularity -> compactness/runaway control`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **93%**
- Iter005–Iter033 completion: **100%**
- Iter034 completion: **ACTIVE**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Projective refinement-limit action mechanism: **PASS_CONDITIONAL_SCOPED**
- Local weak-cell principal curvature lift: **PASS_SCOPED**
- Local/compact-patch torsion regularity mechanism: **PASS_SCOPED**
- Tower-wide uniform torsion-Jacobian gap: **NOT DERIVED**
- Global branch compactness/finiteness: **NOT DERIVED**
- Absolute source normalization `beta`: **NOT DERIVED**
- Physical Weyl-active same-realization finite absolute phase target: **NOT DERIVED**
- `c6` fixed: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Iter031 terminal
Run `34705471500`, head `2c2a4b3c345bf4918c961cb710b501121d63edb8`, aggregate job `103584720153`, artifact `10301339284`, digest `sha256:7d49a935fa5f59fe47df3164dde96797202debce3c73ea07015ae770e35074f0`.

Classification: `PARTIAL_SCOPED_WEAK_CELL_CONTINUITY_SELECTS_A_UNIQUE_LOCAL_PRINCIPAL_CURVATURE_LIFT__BLOCKED_EXACT_FINITE_CELL_ACTION_PHASE_DESCENT_BECAUSE_GLOBAL_HOLONOMY_LOG_BRANCH_FINITE_SAMPLE_QUADRATURE_AND_ABSOLUTE_PHASE_NORMALIZATION_ARE_NOT_FIXED_BY_THE_EXISTING_DISCRETE_DATA`.

Record: `results/ITER031_G31_FINITE_CELL_ACTION_PHASE_DESCENT.md`.

## Iter032 terminal
Run `34705619389`, head `2d2419e6319b10645c61315c16bd1eec85fb85ef`, aggregate job `103585190521`, artifact `10300629276`, digest `sha256:342102a6163c5f5b250aeff82b52f7977ed0cb3b322f0e2f9117e788be4198b2`.

Classification: `PASS_CONDITIONAL_SCOPED_RESOLVED_WEAK_CELL_REFINEMENT_PLUS_UNIFORM_REGULARITY_REMOVES_LOCAL_LOG_AND_FINITE_QUADRATURE_AMBIGUITIES_IN_THE_PROJECTIVE_LIMIT_AND_THE_LIMITING_LOCAL_ACTION_IS_CYLINDRICALLY_ADDITIVE__BLOCKED_QGR_UNIFORM_REFINEMENT_REGULARITY_AND_ABSOLUTE_PHASE_NORMALIZATION_NOT_YET_DERIVED`.

Record: `results/ITER032_G32_PROJECTIVE_REFINEMENT_LIMIT_ACTION_PHASE.md`.

## Iter033 terminal
Run `34705779959`, head `4770da374c40b5120c70eefd20d3cdce1a69693e`, aggregate job `103585488589`, artifact `10301294722`, digest `sha256:f377cb8d95af49c05ef42161678ec26e2036369b36cfd1c6c22f120da1e55cc3`.

Classification: `PARTIAL_SCOPED_LOCAL_TORSION_REGULARITY_AND_QUANTITATIVE_IFT_SUPPLY_THE_G32_REGULARITY_MECHANISM_ON_ANY_COMPACT_NONDEGENERATE_BRANCH_PATCH__BLOCKED_NO_DERIVED_COMPACTNESS_OR_TOWER_WIDE_UNIFORM_TORSION_JACOBIAN_GAP_AND_POINTWISE_FINITE_LEVEL_REGULARITY_IS_INSUFFICIENT`.

Strongest positive: G32's regularity condition is now tied to a concrete torsion-Jacobian gap, with real G5/G9 finite regular anchors.

Strongest blocker: compactness/noncompact escape and a tower-wide positive gap are not established.

Record: `results/ITER033_G33_REFINEMENT_TOWER_UNIFORM_REGULARITY_AUTHORITY.md`.

## Active gate — Iter034 G34
`QGR-ITER034-G34-QGR-SPECIFIC-COERCIVITY-COMPACTNESS-OR-RUNAWAY-BRANCH-COUNTEREXAMPLE`.

Workflow head: `46423cb63a899b4c5a4077be81b003edc2d95280`.
GitHub Actions run: `34705929851`.

This gate uses the actual Iter006 G9 nonlinear 24-equation finite torsion system, not only algebraic controls.

Parallel numerical streams:
1. six deterministic `large-start` lanes: four increasingly distant initial conditions per lane around the finite-curvature G9 root, comparing converged transport matrices to the reference branch;
2. six `background-continuation` lanes: continuation of the same G9 conformal finite-curvature frame family to stronger background amplitudes up to `gamma=4`, recording residuals and the smallest torsion-Jacobian singular value.

The aggregate distinguishes:
- a distinct finite transport-root candidate;
- branch degeneration / Jacobian-gap collapse candidate;
- no candidate found in the scanned domain.

None of those finite numerical outcomes is promoted to a global theorem without further authority.

## Active blocker
`GLOBAL_STRONG_CURVATURE_BRANCH_COMPACTNESS_AND_TOWER_WIDE_UNIFORM_TORSION_REGULARITY_NOT_DERIVED`.

## Claim locks
- theory established `0%`;
- finite numerical scans are not global uniqueness/compactness theorems;
- solver nonconvergence is not proof that a root does not exist;
- G5/G9 finite anchors do not imply a tower-wide gap;
- `beta=1` unauthorized;
- `c6` unfixed;
- no physical same-realization Weyl-active finite absolute phase target yet;
- no experimental confirmation;
- no KMQGB `NEW_REQUIRED` authorization.
