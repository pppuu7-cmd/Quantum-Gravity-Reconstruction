# Iter053-QD3 prospective diagnostic — weighted Gauss-Jacobi bulk pilot

Frozen before QD3 implementation or QD3 production evidence.

## Gate
`ITER053-QD3-WEIGHTED-BULK-GAUSS-JACOBI-PILOT`

## Prior authority
Iter053-QD `34770383463` established outer-box compact-support aliasing. QD2 is independently evaluating high-order support-domain direct-action convergence. QD3 does not alter either diagnostic and cannot reclassify Iter053.

## Mathematical reduction
For the frozen compact perturbation `h_ab(x)=B(x) p_ab(x)`, with
`B(x)=prod_i (1-(x_i/a)^2)^4`, `a=0.24`,

the bulk action variation is exactly

`∫ H^{ab}(x) h_ab(x) d^4x = a^4 ∫_{[-1,1]^4} prod_i(1-u_i^2)^4 [H^{ab}(a u) p_ab(a u)] d^4u`.

Therefore a tensor Gauss-Jacobi rule with `alpha=beta=4` directly integrates against the known compact-support weight and concentrates every expensive H5 evaluation inside the informative region. This is an exact reparameterization of the bulk integral, not a coefficient fit.

## Frozen pilot witness
Only the original Iter053 generic A0 witness:
- metric seed `302071`;
- perturbation seed `312083`;
- H5 coordinate derivative step `5e-4`;
- H5 formula unchanged: `A + I - 2 sqrt(-g) D5`;
- wrong-sign negative control unchanged: `A + I + 2 sqrt(-g) D5`.

## Frozen quadrature
- weighted Gauss-Jacobi `alpha=beta=4` tensor orders `n=2` and `n=3` (16 and 81 H5 nodes);
- direct action reference is independently evaluated on support-domain Gauss-Legendre `n=7` and `n=8` with epsilon `5e-5` only;
- no H5 order, node, seed, threshold, step, or sign may be changed after production evidence.

## Frozen controls and diagnostic thresholds
Valid iff all H5-node metrics are Lorentzian, inverse residual `<=3e-11`, all numbers finite, and direct GL7/8 controls are valid.

Pilot is `promising` iff:
- direct GL7->GL8 relative change `<=5e-4`;
- weighted bulk GJ2->GJ3 relative change `<=2e-2`;
- GJ3 bulk vs direct GL8 relative residual `<=1e-2`;
- correct-sign residual is smaller than the wrong-sign GJ3 residual;
- direct GL8 magnitude `>=1e-10`.

Classes:
- `PASS_DIAGNOSTIC_ITER053_WEIGHTED_GJ3_BULK_PILOT_PROMISING`
- `DIAGNOSTIC_ITER053_WEIGHTED_GJ3_BULK_PILOT_NOT_YET_RESOLVED`
- `ITER053_QD3_CONTROL_INVALID`

## Interpretation lock
Diagnostic/pilot only. A PASS does not establish Iter053 scientific PASS and does not authorize pooling with historical runs. It may only justify prospectively preregistering a fresh scientific replacement gate using a weighted quadrature strategy. `c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains 0%.
