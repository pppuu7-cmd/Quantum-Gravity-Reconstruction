# QGR Iter034 G34 — nonlinear torsion runaway / distant-branch stress

Date: 2026-09-12
Status: `NUMERICAL_COUNTEREXAMPLE_CANDIDATE / VERIFICATION REQUIRED`

## Reproducibility

Authoritative GitHub Actions run: `34705929851`.

- head: `46423cb63a899b4c5a4077be81b003edc2d95280`
- 12 heavy SciPy jobs + aggregate, all workflow jobs `SUCCESS`
- aggregate job: `103585911907`
- aggregate artifact: `10300838970`
- aggregate digest: `sha256:05b0ee793eac19e50f89774fc24af6d619479d07825e4a16ba36fd4808d740de`

The solver uses the same 24 nonlinear finite-torsion equations, `C`, `o(C)` generator basis, and conformal finite-curvature frame family as Iter006 G9.

## Parallel scans

### 1. Distant-start basin scan

Six deterministic directions were tested, each at four start distances from the G9 reference root.

- total distant-start trials: **24**
- converged to residual-qualified roots: **22**
- candidates whose finite transport matrices differ from the G9 reference by the preregistered transport-distance threshold: **10**

This is the first direct numerical evidence in QGR that the full nonlinear finite torsion equations may admit distant branches not visible in the original local-basin G9 test.

### 2. Stronger-background continuation

Six continuation lanes strengthened the same G9 conformal frame family, with maximum target amplitude `gamma=4`.

- requested continuation steps: **30**
- completed residual-qualified steps: **25**
- minimum observed torsion-Jacobian singular gap among successful steps: `0.18363503160521438`

The successful segment did not show a near-zero Jacobian gap, but five requested steps were not completed. Solver nonconvergence is not evidence that a root is absent and must be localized before interpretation.

## Terminal scientific classification

`NUMERICAL_COUNTEREXAMPLE_CANDIDATE_DISTINCT_FINITE_TRANSPORT_ROOT_FOUND_FROM_LARGE_START_SCAN__REQUIRES_HIGH_PRECISION_AND_BRANCH_EQUIVALENCE_VERIFICATION_BEFORE_PROMOTION`.

## Strongest positive / most important finding

The global-branch question is no longer only abstract. Ten residual-qualified large-start solutions produced transport matrices separated from the reference branch in the tested coordinates. If even one survives independent polishing, gauge/invariant comparison, and extension to neighboring cells, the old assumption of a single global finite torsion branch would be false in this realization.

## Strongest blocker

The current scan does **not** yet prove ten distinct physical branches. Possible explanations still include numerical basin artifacts, an equivalence not captured by raw transport distance, or local roots that cannot be extended consistently across neighboring cells.

## Decision

Freeze all candidate distant roots and run an independent branch-verification gate. A branch may be promoted only if it has small independent residual, preserves the metric constraint, differs in gauge-invariant edge/holonomy data from the reference, and extends consistently to the neighboring-cell patch.

## Claim locks
- distinct physical global branches established = **NO**;
- global torsion uniqueness disproved = **NO, candidate counterevidence only**;
- finite numerical scans are not global compactness/uniqueness theorems;
- solver nonconvergence is not proof of no root;
- tower-wide uniform gap remains unproved;
- `c6` fixed = **NO**;
- theory established = **0%**;
- KMQGB `NEW_REQUIRED` remains unauthorized unless benchmark authority changes.

## Next gate
`QGR-ITER035-G35-DISTANT-TORSION-BRANCH-INVARIANT-EQUIVALENCE-AND-NEIGHBOR-CELL-EXTENSION-VERIFICATION`.
