# Iter051A-D1 — finite-difference roundoff localization diagnostic

Date: 2026-09-13

## Status
Prospectively preregistered after terminal G51A classification and before implementation.

## Purpose
Localize the cause of the 7/12 frozen G51A lane failures without changing or reopening the G51A scientific classification. This is a numerical diagnostic only.

## Frozen object
Use exactly the same 12 deterministic metric/curvature/direction lanes as G51A (`seed = 4001 + 131*lane`), the same local density `sqrt(-g) C^3`, the same complex-step reference, and the same signature/algebraic/covariance controls.

## Frozen diagnostic grid
Centered finite-difference step sizes:
`[1.6e-3, 8e-4, 4e-4, 2e-4, 1e-4, 5e-5, 2.5e-5, 1.25e-5]`.

For each lane record absolute FD-vs-complex-step error at every step, the minimum-error step, the final-step error, and whether the error curve has a pre-final minimum followed by an increase of at least factor `1.5` by the final step.

## Frozen interpretation
A lane is `ROUND_OFF_TURNOVER_LOCALIZED` iff:
1. all inherited validity/signature/covariance controls pass;
2. the minimum relative FD-vs-complex-step discrepancy over the frozen grid is `<= 2e-6` OR minimum absolute discrepancy is `<= 1e-9`;
3. the minimum occurs before the final two grid points;
4. final absolute error is at least `1.5 * minimum absolute error`.

A lane is `DERIVATIVE_DISCREPANCY_NOT_LOCALIZED_AS_ROUNDOFF` otherwise.

Aggregate classifications are frozen as:
- `DIAGNOSTIC_FD_ROUNDOFF_TURNOVER_DOMINANT` if at least 6 of the 7 original G51A-failing lanes satisfy the roundoff-turnover rule and all 12 inherited validity/covariance controls pass;
- `DIAGNOSTIC_MIXED_NUMERICAL_BEHAVIOR` if 3–5 of those 7 lanes satisfy it;
- `DIAGNOSTIC_G51A_FAILURE_NOT_EXPLAINED_BY_FD_ROUNDOFF` if 0–2 satisfy it;
- `INVALID_DIAGNOSTIC_CONTROLS` if inherited controls fail or lane count is not 12.

## Claim lock
No outcome changes terminal G51A=`SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION`. A positive diagnostic only authorizes designing a new, separately preregistered high-precision derivative certificate; it cannot weaken, reinterpret, or post-hoc repair the frozen G51A gate.
