# Iter053-QD2 prospective diagnostic — support-domain direct-action quadrature convergence

Frozen before implementation or production evidence.

## Gate
`ITER053-QD2-SUPPORT-DIRECT-QUADRATURE-CONVERGENCE`

## Authority/context
Iter053-QD run `34770383463` established `PASS_DIAGNOSTIC_ITER053_OUTER_BOX_QUADRATURE_ALIASING_CONFIRMED`: outer-box GL3 has 1 nonzero compact-support tensor node and GL4 has 16, while support-domain GL5 integrates the pure polynomial bump to machine precision. QD also showed that generic direct-action integrals can still change materially from support GL4 to GL5. Therefore no scientific replacement gate is authorized yet.

## Purpose
Determine a numerically resolved Gauss-Legendre order for the cheap **direct action directional derivative only**, before spending H5 compute. This diagnostic cannot reclassify Iter053 and cannot authorize a scientific PASS by itself.

## Frozen panel
Same eight independent Iter053 witness seed pairs: A4+B2+C2. Use the untransformed/base member for each C pair. Integrate only over the exact compact-support cube `[-0.24,0.24]^4`; no outer-box nodes and no H5 bulk assembly.

Support-domain tensor Gauss-Legendre orders are frozen at `n = 5,6,7,8`. Direct action derivative uses the existing fixed epsilon `5e-5`. All metric/perturbed-metric signature and inverse controls remain required.

## Frozen convergence classifier
For generic streams A and C, a lane is `converged` iff:
- all controls valid and finite;
- relative change `GL6 -> GL7 <= 2e-3`;
- relative change `GL7 -> GL8 <= 5e-4`;
- `|GL8| >= 1e-10`.

For null stream B, a lane is `converged` iff:
- all controls valid and finite;
- `|GL7|, |GL8| <= 5e-8`;
- absolute `|GL8-GL7| <= 1e-9`.

Aggregate PASS requires all A4+B2+C2 lanes converged and no parse/control failures. Classes:
- `PASS_DIAGNOSTIC_ITER053_SUPPORT_DIRECT_QUADRATURE_CONVERGED_BY_GL8`
- `DIAGNOSTIC_ITER053_SUPPORT_DIRECT_QUADRATURE_NOT_CONVERGED_BY_GL8`

## Interpretation lock
Diagnostic only. No H5 bulk identity is tested. No coefficient/sign fitting, no threshold changes, and no scientific Iter053 reclassification are allowed. If convergence is established, a separate replacement scientific gate must be prospectively preregistered before implementing any new H5 quadrature strategy. `c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established 0%.
