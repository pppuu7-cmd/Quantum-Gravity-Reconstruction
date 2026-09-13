# Iter051B0-R1 — independent replacement covariant double-divergence certificate

## Purpose
The historical Iter051B0 remains terminal `SCIENTIFIC_FAIL_G51B0_DOUBLE_DIVERGENCE_OPERATOR`. Post-terminal audit identified a candidate defect in the constant-frame control transformation of contravariant P indices. This replacement certificate is a new gate and does not alter the historical result.

## Frozen witnesses
Reuse exactly lanes 0..7, seeds `51000 + 137*lane`, metric/P polynomial jets, scales and centered steps `{2e-3,1e-3,5e-4}` from Iter051B0.

## Frozen correction
For a constant coordinate/frame map `x'=L x`, covariant metric indices transform with `M=L^{-1}`, while every contravariant P index transforms with `L`: `P'^{imkn}=L^i_a L^m_j L^k_b L^n_l P^{ajbl}`. Derivative indices transform with M. No other scientific object or threshold changes.

## Added independent control
For each frozen Lorentz transform, at x=0 verify the transformed P tensor against direct four-index contraction with residual <=1e-12 and verify Lorentz metric preservation <=1e-12. These are validity controls, not tunable fit criteria.

## Frozen scientific criteria
Each lane valid only if the original determinant/inverse/P-symmetry/nonzero conditions hold and the added frame controls hold. PASS requires exactly the original thresholds:
- finest direct-vs-expanded relative discrepancy <=3e-5;
- refinement non-worsening within factor 1.20 OR finest absolute discrepancy <=2e-8;
- both constant-frame covariance residuals for D <=3e-7;
- all 8 lanes valid and PASS.

## Frozen classifications
- `PASS_REPLACEMENT_G51B0_COVARIANT_DOUBLE_DIVERGENCE_CERTIFICATE`
- `SCIENTIFIC_FAIL_REPLACEMENT_G51B0_DOUBLE_DIVERGENCE`
- `NUMERICAL_OR_INFRASTRUCTURE_FAIL_G51B0_R1` only if predicates cannot be evaluated.

## Interpretation lock
PASS would certify only the generic operator implementation prerequisite. It would not erase historical G51B0, would not insert Weyl^3-specific P, and would not establish the full 4D covariant Weyl^3 EOM, c6, beta=1, positivity, unitarity or experiment.