# Iter055Z preregistration — is GR-limit continuity sufficient to select the regular branch?

Date: 2026-09-14
Gate: `ITER055Z-GR-LIMIT-CONTINUITY-SELECTOR-SUFFICIENCY`

## Frozen question
Is the seemingly natural future treatment principle

> “physical exact mixed-order solutions are those that converge to solutions of the GR/lower-order equation as the higher-derivative parameter tends to zero”

mathematically sufficient by itself to exclude the singular fast branch?

This is a selector-sufficiency control, not a QGR physical treatment rule.

## Frozen control equation
Use the exact scalar mixed-order control

`u''(t) + eps u''''(t) = 0`, `eps>0`,

whose characteristic polynomial is

`r^2(1+eps r^2)=0`.

The lower-order/GR-limit equation is `u''=0`; the exact equation has the lower-order branch plus fast roots `r=+- i/sqrt(eps)`. This reproduces the same regular-plus-singular scale structure used in Iter054E at control level.

## Frozen obligations
1. Write the exact general solution and identify the lower-order and fast branches.
2. Test ordinary uniform convergence on compact time intervals to a fixed lower-order solution while retaining a nonzero fast component for every `eps>0`.
3. Strengthen the test to `C^m` convergence for arbitrary fixed finite `m`.
4. Test whether a nonzero fast component can survive while the family converges in the `C^infinity` Frechet topology on every compact time interval.
5. If continuity fails as a selector, identify what extra condition would be logically needed (for example analyticity/asymptotic-series membership, a uniform high-derivative/energy bound, a projection/initial-data rule, or explicit order reduction), without selecting one post hoc.
6. Do not infer any QGR tensorial mode, ghost, instability, well-posedness or physical treatment from the scalar control.

## Frozen classifications
- `PASS_SCOPED_ITER055Z_GR_LIMIT_CONTINUITY_UNIQUELY_EXCLUDES_FAST_BRANCH_IN_CONTROL` only if convergence to the lower-order solution forces the fast-branch coefficients to vanish identically for every `eps`.
- `FAIL_SCOPED_ITER055Z_GR_LIMIT_CONTINUITY_ALONE_DOES_NOT_EXCLUDE_SINGULAR_BRANCH__STRONGER_ASYMPTOTIC_SELECTION_REQUIRED` if a nonzero fast branch can remain for every `eps>0` while the exact solutions converge to a GR/lower-order solution, including in smooth compact topology if possible.
- `INVALID_ITER055Z_CONTROL_DOES_NOT_HAVE_FROZEN_MIXED_ORDER_STRUCTURE` only if the control fails to realize the preregistered regular-plus-fast branch structure.

## Interpretation ceiling
A FAIL rejects only vague GR-limit continuity as a sufficient future treatment selector. It does not select analyticity/order reduction, prove exact QGR has fast physical modes, or establish instability/ghost/unitarity/UV/GR/experiment/theory claims.

No GitHub Actions run is preregistered; this is exact ODE/asymptotic analysis.
