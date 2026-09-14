# Iter055R preregistration — radial-profile identifiability on spacelike B3

Date: 2026-09-14
Gate: `ITER055R-SPACELIKE-B3-RADIAL-PROFILE-IDENTIFIABILITY`

## Frozen question
On the Iter055P spacelike-B3 scope, where `(h,n)` already supports a normalized covariant class `phi_(h,n)(k)=h f(h n.k)`, do existing QGR covariance/refinement/locality constraints uniquely select the dimensionless radial shape `f`, or do operationally distinct admissible shapes survive?

## Frozen authority and admissibility
- G6F physical characteristic Hilbert and finite-frame action;
- Iter055P norm/refinement scaling;
- G6G/G6H profile examples only as controls, preserving their preparation/readout scope;
- existing locality/refinement statements, without inventing a new compact-support or analyticity requirement.

Admissible radial shapes must be nonzero and satisfy `integral_0^infinity s |f(s)|^2 ds < infinity`. Overall normalization is fixed to unit radial norm. No profile width/shape may be fitted to a desired result.

## Frozen obligations
1. Determine whether Lorentz covariance and the Iter055P dilation/refinement law impose any equation on the dimensionless shape beyond weighted square-integrability/normalization.
2. Determine whether existing QGR locality/refinement authority adds a source-defined shape constraint.
3. Construct at least two explicit normalized inequivalent profiles satisfying all source-defined class-level constraints if possible.
4. Distinguish externally specified G6G/G6H preparation profiles from candidate-owned bridge selection.
5. A nonuniqueness result must not promote either witness profile to QGR dynamics/bridge authority.

## Frozen classifications
- `PASS_SCOPED_UNIQUENESS_ITER055R_EXISTING_QGR_CONSTRAINTS_SELECT_ONE_RADIAL_PROFILE_CLASS` only if current authority reduces the normalized radial shape to one equivalence class.
- `PASS_SCOPED_NONUNIQUENESS_ITER055R_RADIAL_PROFILE_REMAINS_INFINITE_DIMENSIONAL_NEW_PROFILE_INPUT_REQUIRED` if at least two inequivalent normalized profiles satisfy all source-defined covariance/refinement/locality constraints and no source selector exists.
- `BLOCKED_ITER055R_LOCALITY_OR_REFINEMENT_CONSTRAINT_NOT_DEFINED_ENOUGH_TO_TEST_PROFILE_IDENTIFIABILITY` if the relevant source conditions are too incomplete even to certify multiple admissible profiles.
- `INVALID_PROVENANCE_ITER055R_PROFILE_SCOPE_INCONSISTENT` only if the frozen source objects conflict.

## Interpretation ceiling
Nonuniqueness would identify profile shape as explicit new bridge input; it would not select a profile, fix h, define the complete sector bridge or interacting dynamics, or establish beta/c6/Weyl3/regulator/unitarity/UV/GR/experiment/theory claims.

No GitHub Actions run is preregistered; this is exact function-space/refinement analysis.
