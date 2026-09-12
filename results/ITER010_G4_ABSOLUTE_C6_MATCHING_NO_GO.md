# QGR Iter010-G4 — absolute microscopic c6 matching or no-go

Date: 2026-09-12
Status: `BLOCKED_SCOPED_NO_EXISTING_QGR_NORMALIZATION_PHASE_LOOP_OR_HOMOGENEOUS_REFINEMENT_RULE_FIXES_C6__THE_WEYL_ACTIVE_BACKGROUND_IS_SENSITIVE_BUT_THE_REQUIRED_ABSOLUTE_MICROSCOPIC_TARGET_IS_MISSING`

GitHub Actions run `34665566358`: **6 lanes + aggregate SUCCESS**.

## Question

After Iter010-G3 constructed a same-field-content Weyl-active microscopic background with nonzero continuum `Weyl^3`, do any already-frozen QGR normalization, phase, loop, or refinement principles determine the absolute coefficient `c6` of the unique on-shell Ricci-flat parity-even six-derivative operator?

## Results

### 1. Two-derivative normalization does not propagate to c6

The frozen QGR convention fixes the Einstein-Hilbert/two-derivative conversion, including the previously derived signed `c_geom=-1/2` in that convention. This fixes the normalization of the two-derivative operator only. `c6` is an independent six-derivative Wilson direction and remains free.

Classification:
`PASS_SCOPED_FROZEN_TWO_DERIVATIVE_ACTION_NORMALIZATION_FIXES_ONLY_THE_EINSTEIN_HILBERT_CONVERSION_AND_LEAVES_THE_INDEPENDENT_SIX_DERIVATIVE_C6_DIRECTION_FREE`.

### 2. History normalization and projective phase composition do not fix c6

For branch amplitudes of the form

`K_alpha = 24^(-1/2) exp(i S_alpha) U_alpha`,

Kraus completeness depends on the modulus and is unchanged by adding an arbitrary real `c6` contribution to `S_alpha`. Additive/projective phase composition also remains exact for arbitrary real `c6`.

Classification:
`FAIL_SCOPED_HISTORY_KRAUS_NORMALIZATION_AND_ADDITIVE_PROJECTIVE_PHASE_COMPOSITION_REMAIN_EXACT_FOR_ARBITRARY_REAL_C6_AND_CANNOT_SELECT_ITS_VALUE`.

### 3. Continuous loop phases cannot quantize a nonzero c6

The G3 Weyl-active family has continuously variable small curvature and therefore continuously variable small coherent action phases. Requiring every such phase to be a root of unity would force the winding to remain zero near the flat point and cannot select a nonzero universal `c6` without a separately derived discrete flux spectrum.

Classification:
`FAIL_SCOPED_ROOT_OF_UNITY_OR_LOOP_SINGLE_VALUEDNESS_CANNOT_SELECT_A_NONZERO_C6_ON_THE_CONTINUOUS_WEYL_ACTIVE_BACKGROUND`.

### 4. Homogeneous refinement conditions cannot select an absolute coefficient

Pure additive or homogeneous blocking/refinement equations are homogeneous in an overall `c6`. If the geometric identity closes, every scalar multiple closes; if it does not close, the condition can kill the operator but cannot select a unique nonzero normalization.

Classification:
`BLOCKED_SCOPED_ADDITIVE_OR_HOMOGENEOUS_REFINEMENT_CONSISTENCY_CANNOT_SELECT_A_UNIQUE_NONZERO_C6_WITHOUT_AN_INDEPENDENT_NONHOMOGENEOUS_MICROSCOPIC_TARGET`.

### 5. G3 provides sensitivity, not a target

On the G3 Weyl-active same-field-content background,

`d Phi_abs / d c6 proportional to h^4 Weyl^3 != 0`.

Therefore one genuinely derived absolute microscopic action/phase target on this background would be sufficient to fix the single remaining scalar coefficient direction. Nonzero sensitivity alone is not that target.

Classification:
`PASS_SCOPED_G3_WEYL_ACTIVE_BACKGROUND_HAS_NONZERO_ABSOLUTE_ACTION_PHASE_SENSITIVITY_TO_C6_AND_ONE_DERIVED_ABSOLUTE_PHASE_TARGET_WOULD_FIX_THE_SCALAR_COEFFICIENT`.

### 6. Canonical authority still contains no such nonhomogeneous target

The repository authority contains exact lower-order/local dynamics, finite history normalization, torsion/holonomy geometry, and the G3 Weyl-active sensitivity witness, but no canonical nonhomogeneous microscopic action phase or refinement target that fixes `c6`.

Classification:
`BLOCKED_SCOPED_NO_CANONICAL_QGR_RECORD_SUPPLIES_A_NONHOMOGENEOUS_ABSOLUTE_MICROSCOPIC_ACTION_PHASE_OR_REFINEMENT_TARGET_THAT_FIXES_C6`.

## Consolidated decision

`ITER010_CAN_CLOSE_100_PERCENT_WITH_C6_EXPLICITLY_UNFIXED_AND_THE_MISSING_NONHOMOGENEOUS_UV_DATUM_ISOLATED`.

The correct next question is not whether another symmetry can be imposed on the same coefficient. The next stage must derive a primitive finite-cell action/phase/measure principle that supplies an **absolute nonhomogeneous microscopic datum**. The first internal candidate to audit is the already-derived torsion coarea/Jacobian branch measure, because its normalization follows from the constraint reduction rather than from an arbitrary new coupling.

## Claim lock

Do not set `c6` by convention, by external continuum two-loop coefficients, by the leading history loss, or by root-of-unity assumptions. Iter010 does not establish a numerical `c6`.
