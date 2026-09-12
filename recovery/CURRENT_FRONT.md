# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter036`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / DISTINCT-BRANCH PERSISTENCE STRESS`
Active roadmap stage: `finite branch nonuniqueness -> persistence/deformation stress -> global/tower authority`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **93%**
- Iter005–Iter035 completion: **100%**
- Iter036 completion: **ACTIVE**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Projective refinement-limit action mechanism: **PASS_CONDITIONAL_SCOPED**
- Local weak-cell principal curvature lift: **PASS_SCOPED**
- Local/compact-patch torsion regularity mechanism: **PASS_SCOPED**
- Distinct finite torsion branch patches in the tested G35 realization: **PASS_SCOPED NUMERICAL COUNTEREXAMPLE TO LOCAL FINITE-PATCH UNIQUENESS**
- Branch persistence under larger patches/background deformation/refinement proxy: **ACTIVE G36**
- Tower-wide uniform torsion-Jacobian gap: **NOT DERIVED**
- Global branch compactness/finiteness/nonuniqueness theorem: **NOT DERIVED**
- Absolute source normalization `beta`: **NOT DERIVED**
- Physical Weyl-active same-realization finite absolute phase target: **NOT DERIVED**
- `c6` fixed: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Iter034 terminal — runaway / distant-root stress
Run `34705929851`.

Classification:
`NUMERICAL_COUNTEREXAMPLE_CANDIDATE_DISTINCT_FINITE_TRANSPORT_ROOT_FOUND_FROM_LARGE_START_SCAN__REQUIRES_HIGH_PRECISION_AND_BRANCH_EQUIVALENCE_VERIFICATION_BEFORE_PROMOTION`.

The 24 distant starts produced 22 residual-qualified roots and 10 transport-separated candidates.
Record: `results/ITER034_G34_NONLINEAR_TORSION_RUNAWAY_STRESS.md`.

## Iter035 terminal — invariant branch verification
Run `34706686021`, head `faec0f17c49c43d97984b16cf048dc4a52a8f247`,
aggregate job `103588230856`, artifact `10301772238`.

Classification:
`SCIENTIFIC_PASS_SCOPED_DISTINCT_EXTENDABLE_BRANCH_COUNTEREXAMPLE`.

Frozen result:
- 24/24 lanes present;
- 22 residual-qualified origin candidates;
- reference controls valid;
- 8 verified distinct extendable finite branch patches;
- verified `(lane, scale_index, start_scale)`:
  `(0,3,6.0), (1,2,3.0), (1,3,6.0), (2,2,3.0), (2,3,6.0), (3,1,1.5), (4,2,3.0), (5,3,6.0)`.

Interpretation: the single-branch assumption is numerically false on the tested finite realization/patch,
with invariant holonomy separation. This is not a global branch-count or tower nonuniqueness theorem.

Record: `results/ITER035_G35_DISTANT_BRANCH_VERIFICATION.md`.

## Active gate — Iter036 G36
`ITER036-G36-EXPANDED-PATCH-PERSISTENCE`.

Preregistration: `status/ITERATION_036.md`.
Workflow: `.github/workflows/qgr-iter036-g36-expanded-patch-persistence.yml`.
Production trigger head: `0d5a0be6b5d7336f42747a2b3010013f1aa51ab7`.
GitHub Actions run: `34708104944`.

Frozen computation:
- seed set: the 8 verified G35 branch starts;
- background family: 8 seeds x gamma `[0.8, 1.0, 1.2]`;
- shrinking-cell proxy family: 8 seeds x h `[0.75, 0.50, 0.35]`;
- total: **48 production lanes**, `max-parallel=24`;
- every target is tested on a 15-cell two-shell patch;
- promotion requires small residuals, metric compatibility, invariant origin separation,
  complete 15-cell extension, and expanded plaquette-holonomy separation.

Aggregate promotion requires the **same seed** to survive all three background targets and all three
shrinking-cell targets for the strongest scoped PASS.

The h-family is explicitly a local shrinking-cell/background-sampling proxy, not the full projective
refinement map.

## Active blocker
`GLOBAL_BRANCH_STRUCTURE_AND_TOWER_WIDE_PERSISTENCE_NOT_DERIVED`.

G35 removes the old assumption that one tested finite branch is unique on the local realization,
but it does not by itself supply a global branch theorem, compactness, a tower-wide regularity gap,
or a physical normalization/observable.

## Claim locks
- theory established `0%`;
- finite numerical branch scans are not global uniqueness/nonuniqueness/compactness theorems;
- solver nonconvergence is not proof that a root does not exist;
- G36 refinement proxy is not the full projective refinement limit;
- G5/G9/G35 finite anchors do not imply a tower-wide gap;
- `beta=1` unauthorized;
- `c6` unfixed;
- no physical same-realization Weyl-active finite absolute phase target yet;
- no experimental confirmation;
- no KMQGB `NEW_REQUIRED` authorization.
