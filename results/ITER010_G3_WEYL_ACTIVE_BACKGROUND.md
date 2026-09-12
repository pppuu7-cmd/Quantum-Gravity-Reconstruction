# Iter010 G3 — Weyl-active same-field microscopic background

Run: `34665317072` — 6 lanes + aggregate SUCCESS.

Aggregate classification:

`PASS_SCOPED_WEYL_ACTIVE_SAME_FIELD_CONTENT_MICROSCOPIC_BACKGROUND_ESTABLISHED_WITH_STABLE_TORSION_CLOSURE_NONZERO_CONTINUUM_WEYL_CUBED_AND_CORRECT_H4_CELL_SCALING`

## Construction

The special repaired-G9 conformal tetrad `F(x)=Omega(x) I` was generalized to a local invertible tetrad `F(x)` while retaining:

- the same ten-component symmetric second-moment metric sector `g=F^T E F`;
- the same six-generator `E`-Lorentz connection;
- the same discrete torsion parallelogram closure;
- no additional field components.

The test profile is a weak static harmonic tidal field

`Phi=(kappa/2)(x^2+y^2-2 z^2)`,

with linearized weak-field metric `g00=1+2Phi`, `gij=-(1-2Phi) delta_ij`. The spatial Hessian trace is `1+1-2=0`, so this is a weak vacuum tidal profile rather than the conformally-flat G9 family.

## Numerical/structural checks

- torsion closure remains at numerical residuals far below the gate tolerance and the tested connection Jacobians retain a positive singular-value margin;
- adjacent-swap relative holonomy logarithms continue to scale as `h^2`;
- Ricci and scalar proxies vanish approximately as `h^2` toward refinement;
- the Weyl norm extrapolates to a nonzero continuum value;
- the Weyl-cubed invariant extrapolates to a nonzero continuum value;
- `h^4 W_h^3` has the required nonzero `h^4` cell scaling, in contrast to the `h^7` artifact suppression on conformally-flat repaired-G9;
- Weyl curvature scales linearly and `Weyl^3` cubically with the tidal amplitude.

## Scientific interpretation

The previous G2 obstruction was a background-identifiability obstruction, not a field-content obstruction. QGR's already-established second-moment/torsion arena admits a same-field-content weak-curvature background that is genuinely sensitive to the unique six-derivative Ricci-flat operator.

This removes the need to add new fields merely to expose `c6` sensitivity.

It does **not** fix `c6`: the background is a sensitivity witness. A nonhomogeneous absolute microscopic action, phase or refinement normalization condition is still required.

## Decision

`USE_THIS_BACKGROUND_ONLY_AS_A_C6_SENSITIVITY_WITNESS__NEXT_TEST_MUST_SUPPLY_A_NONHOMOGENEOUS_ABSOLUTE_MICROSCOPIC_ACTION_PHASE_OR_REFINEMENT_MATCH`

Next gate:

`QGR-ITER010-G4-ABSOLUTE-MICROSCOPIC-C6-MATCHING-OR-NO-GO`
