# QGR Iter019 G19 — conformal refinement authority

Date: 2026-09-12
Status: `PASS_SCOPED / FAIL_SCOPED_JOINT_G16_G18_TRAJECTORY / R_UNSELECTED`

## Reproducibility

GitHub Actions run `34695443798`: 24 exact-rational lanes plus aggregate, all `SUCCESS`.

Audit classes, six lanes each:

- `conformal-reduction`;
- `weight-uniqueness`;
- `character-tension`;
- `normalization-inheritance`.

## 1. Existing QGR action supplies the G18 bulk functional in the common conformal sector

The already-derived local all-orders two-derivative action is, in its scoped metric-only sector,

`S_local = a integral sqrt(|G|) R[G]`.

Restrict to

`G = s^2 C`,

where `C=J-I` is constant and flat. In dimension `d`, the conformal reduction, modulo a boundary term, has the bulk form

`(d-1)(d-2) s^(d-4) (D s)^2`.

For the derived QGR dimension `d=4`, the power is exactly zero and the coefficient is exactly six:

`S_conf,bulk = 6 a integral (D s)^2`.

Thus the G18 Dirichlet functional is not an independent new coupling in this scoped sector: its normalization is inherited as `lambda=6a` from the existing QGR action.

Classification:
`PASS_SCOPED_EXISTING_ALL_ORDERS_QGR_TWO_DERIVATIVE_ACTION_RESTRICTED_TO_G_EQUALS_S2_C_REDUCES_IN_FOUR_DIMENSIONS_TO_SIX_TIMES_DIRICHLET_DS2_MODULO_BOUNDARY`.

## 2. Refinement weight

For a local quadratic increment contribution on a segment of size `h`, write the weight as `w(h)` and define

`y(h)=w(h) h^2`.

Exact split/refinement additivity for the linear endpoint profile requires on positive rational refinements

`y(h1+h2)=y(h1)+y(h2)`.

The exact rational rank audits on all six grids leave a one-dimensional solution space. After one overall normalization,

`y(h)=h`,

so

`w(h) proportional to 1/h`.

Classification:
`PASS_SCOPED_ON_POSITIVE_RATIONAL_REFINEMENTS_LOCAL_QUADRATIC_INCREMENT_ACTION_PLUS_EXACT_LINEAR_PROFILE_REFINEMENT_ADDITIVITY_FORCES_W_H_PROPORTIONAL_TO_ONE_OVER_H_WITH_ONLY_ONE_OVERALL_NORMALIZATION`.

The scope is local quadratic-in-increment/two-derivative; this does not rule out genuinely nonlocal or higher-derivative microscopic terms.

## 3. G16 versus G18

G16's scoped repeated-event composition hypothesis produced a multiplicative character

`s(n+m)=s(n)s(m)`.

For exact rational bases `b` and endpoint `r=b^N`, this gives the trajectory

`s_k=b^k`.

The Dirichlet extremal with the same endpoints is instead linear in `s`:

`s_k=1+(k/N)(r-1)`.

For every nontrivial tested endpoint `r != 1`, exact arithmetic gives

`S_character > S_linear`,

and the linear extremal has a nonzero multiplicativity defect. Therefore these two auxiliary hypotheses cannot both describe the same nontrivial fundamental refinement trajectory.

Classification:
`FAIL_SCOPED_JOINT_NONTRIVIAL_HYPOTHESIS_G16_MULTIPLICATIVE_EVENT_CHARACTER_AND_G18_LINEAR_S_DIRICHLET_EXTREMAL_PROFILE_CANNOT_BOTH_DEFINE_THE_SAME_REFINEMENT_TRAJECTORY_FOR_R_NOT_EQUAL_ONE`.

This is **not** a FAIL of QGR. G16 explicitly treated the repeated-event character rule as a scoped hypothesis; that rule is retired as a fundamental trajectory unless a distinct event variable or clock map is derived.

## 4. What remains free

The existing action fixes the bulk functional and its normalization relative to `a`; it does not supply a bulk equation selecting the final endpoint `r`.

Therefore:

- `r fixed = NO`;
- finite pair/triple coherent amplitudes derived = **NO**;
- `c6 fixed = NO`.

## Consolidated classification

`PASS_SCOPED_G18_DIRICHLET_BULK_FUNCTIONAL_AND_ONE_OVER_H_REFINEMENT_WEIGHT_ARE_DERIVED_WITHIN_THE_EXISTING_QGR_LOCAL_TWO_DERIVATIVE_COMMON_CONFORMAL_SECTOR_UP_TO_THE_ALREADY_EXISTING_OVERALL_ACTION_NORMALIZATION__FAIL_SCOPED_G16_MULTIPLICATIVE_CHARACTER_AND_G18_LINEAR_S_PROFILE_AS_SIMULTANEOUS_NONTRIVIAL_REFINEMENT_LAWS__R_REMAINS_UNSELECTED_BOUNDARY_DATUM`.

## Decision

`RETIRE_G16_MULTIPLICATIVE_CHARACTER_AS_FUNDAMENTAL_REFINEMENT_TRAJECTORY_UNLESS_A_DISTINCT_EVENT_VARIABLE_OR_CLOCK_MAP_IS_DERIVED__PROMOTE_G18_DIRICHLET_PRINCIPLE_ONLY_IN_SCOPED_COMMON_CONFORMAL_LOCAL_TWO_DERIVATIVE_SECTOR`.

## Next gate

`QGR-ITER020-G20-ENDPOINT-R-AUTHORITY-FROM-BOOLEAN-EVENT-BOUNDARY-DATA-OR-DISTINCT-COMPOSITION-VARIABLE`.

The next step must decide whether a nontrivial endpoint is supplied by a microscopic event/boundary insertion from the same Boolean incidence realization, rather than continuing to search for a bulk scale equation that the derived variational problem does not contain.
