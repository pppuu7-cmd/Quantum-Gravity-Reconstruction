# QGR Iter007-G5A — path-level refinement scaling and normalized purity observable

Date: 2026-09-12
Status: `PASS_SCOPED_PATH_LEVEL_SCALING_AND_OBSERVABLE_FORM / PHYSICAL_SCALE_OPEN`

## Objective

Determine whether the finite-cell `O(h^4)` history-ordering correction survives or disappears under repeated refinement, and identify a normalized operational quantity in which the correction can be expressed without introducing a new phenomenological coefficient.

## Fixed-path refinement scaling

From G2, one sufficiently small cell has an interaction-frame channel of the form

`E_h = I + h^4 D + O(h^5)`,

where `D` is the fixed curvature-commutator double-commutator superoperator determined by the exact 24-history covariance.

Consider a physical causal path of fixed length `L` subdivided into

`N=L/h`

cells. For a smooth bounded connection/curvature field, sequential composition gives at leading order

`sum_(n=1)^N h^4 D_n`.

Therefore

`||Delta E_path|| = O(N h^4)=O(L h^3)`.

The cross terms from multiplying two local corrections are `O(N^2 h^8)=O(L^2 h^6)`, and the accumulated local `O(h^5)` remainder is `O(L h^4)`. Hence the `L h^3` term is the leading path-level scaling.

Under uniform refinement

`h -> h/b`

at fixed physical path length,

`Delta E_path -> b^(-3) Delta E_path`

at leading order.

Thus the history-ordering correction is an **irrelevant path-level refinement effect** in the regular continuum limit.

This is deliberately not promoted to a full four-dimensional RG eigenvalue: generic network/volume blocking can have different combinatorics and remains to be audited separately.

## Normalized operational observable: purity loss

Let the six anti-Hermitian curvature generators be written

`K_a=-i H_a`,

with Hermitian `H_a`. G2 gives

`delta rho = -(h^4/8) C_ab [H_a,[H_b,rho]] + O(h^5)`.

For a density matrix, purity is the normalized dimensionless operational quantity

`P=Tr(rho^2)`, `0<P<=1`.

Using cyclicity of the trace,

`Delta P = 2 Tr(rho delta rho)`

becomes

`Delta P = -(h^4/4) C_ab Tr([H_a,rho]^dagger [H_b,rho]) + O(h^5)`.

The exact ordering covariance `C` is positive definite, so the quadratic form is nonnegative. Therefore

`Delta P <= 0`

at leading order.

For a pure input state (`P_in=1`), the normalized purity loss is

`1-P_out = (h^4/4) C_ab Tr([H_a,rho]^dagger[H_b,rho]) + O(h^5)`.

No new decoherence coefficient appears: the tensor coefficient is the exact 24-history covariance already derived in G2.

## What is now closed

Scoped closure:

- local history-ordering channel starts at `h^4`;
- accumulated correction along a fixed smooth physical path scales as `L h^3`;
- the correction is irrelevant under one-dimensional causal-path refinement, scaling as `b^-3`;
- a normalized operational observable exists: physical-state purity loss;
- the leading purity-loss coefficient is a positive quadratic form fixed by the microscopic ordering covariance and the derived curvature generators.

## Remaining blocker

The absolute magnitude is **not yet a prediction**, because QGR has not yet fixed the physical microscopic/refinement scale `h` in standard units.

Also still open:

- full graph/4D RG scaling of the correction;
- a concrete source/preparation/readout protocol that maps the physical two-mode QGR quotient to an experimentally accessible density matrix;
- the numerical value of the derived curvature-generator quadratic form for a specified physical background;
- comparison to Lorentz-violation/decoherence constraints.

Therefore the result closes the **observable form**, not the scale map.

Classification:

`PASS_SCOPED_FIXED_PATH_H3_REFINEMENT_IRRELEVANCE_AND_NORMALIZED_PURITY_LOSS_OBSERVABLE_FORM__PHYSICAL_MICRO_SCALE_OPEN`.

## Reproducibility

`code/qgr_iter007_g5_path_scaling_and_purity.py`
