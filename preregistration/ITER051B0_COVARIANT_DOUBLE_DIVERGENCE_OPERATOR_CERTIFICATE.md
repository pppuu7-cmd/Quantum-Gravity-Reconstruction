# Iter051B0 — Covariant double-divergence operator certificate

## Purpose
Before inserting the Weyl^3-specific momentum tensor P=d(sqrt(-g) I3)/dR into the full metric functional derivative, independently validate the tensor-calculus implementation of the covariant double-divergence operator on generic rank-4 Riemann-symmetry test fields.

This is a G51B implementation prerequisite only. PASS does not establish the Weyl^3 Euler-Lagrange tensor.

## Frozen test object
For each lane construct a smooth polynomial contravariant tensor field P^{a m b n}(x) with exact antisymmetry in (a,m) and (b,n), pair exchange symmetry, and a nonzero generic quadratic coordinate dependence. Construct a smooth Lorentz-signature metric g_ab(x) with small affine/quadratic perturbations and guaranteed nondegeneracy on the frozen stencil.

Evaluate at x=0 the ordered covariant double divergence D^{mn}=nabla_a nabla_b P^{a m b n} in two independent implementations:
1. direct nested covariant derivative evaluated by centered finite differences of the first covariant derivative;
2. explicit expanded second-derivative implementation using Christoffel symbols and their coordinate derivatives.

The two implementations may share only the frozen metric/P samples; they must not call each other's derivative routine.

## Frozen lanes and stencils
- lanes: 0..7, deterministic seeds `51000 + 137*lane`;
- coordinate dimension: 4;
- metric perturbation scale <= 0.015;
- P coefficient scale <= 0.08;
- centered steps h in {2e-3, 1e-3, 5e-4};
- two constant Lorentz-frame controls per lane: x-boost v=0.17 and composed x-boost v=-0.13 with yz rotation theta=0.29.

## Frozen criteria
Each lane is valid only if:
- metric determinant remains negative on every stencil sample;
- inverse residual max|g g^{-1}-I| <= 1e-11;
- P algebraic symmetry residual <= 1e-11;
- direct and expanded D are nonzero with Frobenius norm >= 1e-8.

Scientific PASS requires all of:
- finest-step relative direct-vs-expanded discrepancy <= 3e-5;
- step refinement is non-worsening within factor 1.20 from h=1e-3 to 5e-4, OR finest absolute discrepancy <= 2e-8;
- constant-frame covariance residual for D <= 3e-7 for both frozen controls;
- all 8 lanes valid and PASS.

## Frozen classifications
- `PASS_G51B0_COVARIANT_DOUBLE_DIVERGENCE_OPERATOR_CERTIFICATE`
- `SCIENTIFIC_FAIL_G51B0_DOUBLE_DIVERGENCE_OPERATOR`
- `NUMERICAL_OR_INFRASTRUCTURE_FAIL_G51B0` only when the scientific predicate was not evaluable because of implementation/runtime failure.

## Interpretation lock
A PASS certifies only the generic covariant double-divergence implementation layer. It does not certify Weyl^3-specific P, the metric variation of P, full EOM assembly, absolute energy positivity, quantum unitarity, experimental confirmation, beta=1, or any value of c6.

No threshold, lane, witness, step, or interpretation rule may be changed after production results are viewed.
