# Iter051B2 — Initial Frozen Production Result and Causal Audit

Date: 2026-09-13

## Frozen gate
`ITER051B2-WEYL3-P-CONNECTION-RESPONSE`

Prospective provenance:
- preregistration: `cffde199b9cd885f4d07238b8c46fdee3f966143`
- implementation: `467425bb30fcf410940bb5627c5adeb7f2e9d963`
- aggregate implementation: `8a33fa56922e519185ae264acaa5621783547f6a`
- authoritative initial workflow/head: `a9884403a7969d53f284f3195bea37f4ad5bbc62`

## Initial authoritative production
- run: `34736978191`
- aggregate job: `103670192517`
- summary artifact: `10311148731`
- summary digest: `sha256:c12216eac614c0105420f83e5fceb73d937cd9f429d5e2d0eb095020e33c1131`
- frozen aggregate classification: `SCIENTIFIC_FAIL_G51B2_WEYL3_P_CONNECTION_RESPONSE`
- valid: `1/4`
- pass: `1/4`

Raw lane artifacts were all consumed by the aggregate with verified digests:
- lane 0 artifact `10311078901`, digest `sha256:972e5241cc5321e800f5abd066ab6e970d403f0fa524e69b598067b018cdd229`
- lane 1 artifact `10311123880`, digest `sha256:b9881cf01899690f4e8dc00cb043ff843edc518d9877e7cbdbdcef9cb1cd34ad`
- lane 2 artifact `10310674690`, digest `sha256:5311cd1dc4104a5225c0ac306586819f7fb12daec172d9d7da417e25f90df1e3`
- lane 3 artifact `10311256736`, digest `sha256:7a7d2dfe0ec5ebee82000fb4ad48edfc57b5203947c92f41e9c3d1109a749a85`

## Frozen aggregate diagnostics
The only failing aggregate structural predicate was the algebraic-Riemann residual of finite-difference-extracted P derivative jets:
- worst P-jet algebraic residual: `1.609823385706477e-09` vs frozen `2e-10`;
- all other frozen scientific/numerical metrics were comfortably inside thresholds:
  - worst direct-vs-reference finest residual `2.5076338423438444e-07` vs `2e-5`;
  - worst direct final step change `2.0962669356580043e-07` vs `1e-5`;
  - worst extracted-reference convergence `2.4933117531487735e-07` vs `2e-5`;
  - worst D covariance `5.351292093284897e-16` vs `2e-7`;
  - worst direct P0 covariance `3.4830092046971933e-15` vs `2e-9`;
  - inverse residual `4.440892098500626e-16` vs `1e-11`;
  - zero-curvature P norm `2.7216552697590953e-61` vs `2e-10`;
  - minimum nonzero D norms remained about `4.43e-2`.

Direct inspection of failing raw lanes showed the same pattern. For lane 1 the three P-jet residuals were approximately `4.16e-11, 1.67e-10, 6.66e-10`; for lane 2 they were `1.49e-10, 4.44e-10, 1.50e-9`, while the actual connection-response comparisons and covariance controls passed by large margins.

## Causal diagnosis
The first causal failure is numerical subspace drift from subtractive cancellation in second finite differences of a pointwise P tensor that is already exactly projected into the algebraic-Riemann subspace. Because the algebraic-Riemann projector is linear, the exact derivative of a subspace-valued P field remains in the same subspace. Reapplying that same fixed projector to the extracted finite-difference derivative tensors is therefore a numerical stabilization of an exact algebraic identity, not a change to the scientific model, witness family, thresholds, seeds, target, or interpretation.

The initial frozen aggregate remains permanently recorded as `SCIENTIFIC_FAIL_G51B2_WEYL3_P_CONNECTION_RESPONSE`; it is not overwritten or reclassified retroactively.

## Authorized repair
A separate authoritative retry may make exactly one implementation-only change: reproject each finite-difference `partial P` and `partial partial P` tensor with the same algebraic-Riemann projector already frozen for pointwise P. All production seeds, stencils, thresholds, controls, and terminal interpretation remain unchanged.
