# Iter051A-D2 — complex-step comparator stability audit

Date: 2026-09-13

Prospectively preregistered after terminal D1=`DIAGNOSTIC_MIXED_NUMERICAL_BEHAVIOR` and before implementation.

## Scope
Audit only the three D1-unlocalized original G51A failing lanes `[0,2,9]`. The physical object, deterministic seeds, local density `sqrt(-g) C^3`, metric directions, algebraic controls and covariance transformations are unchanged.

## Frozen complex-step grid
`eps = [1e-16, 1e-20, 1e-24, 1e-28, 1e-30]`.

For each epsilon compute `Im L(g+i eps h)/eps`. No finite-difference values are used in the gate.

## Frozen lane criterion
A lane is `COMPLEX_STEP_STABLE` iff:
1. signature/algebraic/Weyl-trace controls inherited from G51A are valid;
2. all five complex-step derivatives are finite;
3. relative spread `(max-min)/max(abs(median),1e-12) <= 1e-10`;
4. the `1e-30` value obeys the inherited two-transform directional covariance tolerance `<=1e-8`.

## Frozen aggregate interpretation
- `DIAGNOSTIC_COMPLEX_STEP_STABLE_3_OF_3` if all three lanes pass;
- `DIAGNOSTIC_COMPLEX_STEP_INSTABILITY_PRESENT` if 1–2 pass;
- `DIAGNOSTIC_COMPLEX_STEP_UNSTABLE_3_OF_3` if none pass;
- `INVALID_DIAGNOSTIC_CONTROLS` if lane count/IDs or inherited controls are invalid.

## Claim lock
This diagnostic cannot change terminal G51A from FAIL to PASS. A 3/3 stability result only authorizes designing a separately preregistered replacement G51A-class certificate with a numerically independent high-precision derivative comparator; it does not establish the full Weyl3 Euler-Lagrange tensor.
