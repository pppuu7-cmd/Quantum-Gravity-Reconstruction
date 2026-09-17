# Iter057AP target-blind constructor defect — cubic Weyl contraction

Date: 2026-09-17
Preregistration: `6de62a559381a7c86e01c58a62ea7d8c91606884`
Constructor run: `35175792085`
Artifact: `10478635340`, digest `sha256:2f6bcb6ea3ba4dc34e9b616a14f408df45b9e7e1daf96baa3b00678b28ceb410`
Invalid constructor payload SHA256: `e238ecc2184c357e0fa7ab3a68827f1a88d2a0fb34dc6b7b55a56499bc16464f`

## Target-blind failure

No Iter057U/X source coefficient file or comparator had been opened or created. The constructor's own frozen controls reported:

- `I3_origin_over_kappa3 = 0` instead of the preregistered convention/provenance value `96`;
- `P_dot_R_equals_3I3 = false` while the independent Frechet-direction check itself remained exact/nonzero;
- trace Ward and Noether source controls false.

All seed, inverse, Ricci-flat, Weyl=Riemann, source symmetry and 2100-slot completeness controls passed.

## Defect source

The independent AP helper `cubic_and_Q` did not implement the frozen AO invariant

`I3 = C_ab^{ cd} C_cd^{ ef} C_ef^{ ab}`.

It formed the intermediate quadratic tensor with one all-lowered `C` factor. The AO phase-2 functional, frozen before AP, uses the mixed/raised tensor `Cup[a,b,c,d] = C_ab^{ cd}` in all three factors. The correct source-faithful contraction is therefore

`Q[a,b,c,d] = sum_{e,f} Cup[c,d,e,f] Cup[e,f,a,b]`,

`I3 = sum_{a,b,c,d} Cup[a,b,c,d] Q[a,b,c,d]`.

This correction is dictated entirely by the pre-existing AO functional and by the target-blind `I3(0)/kappa^3=96` control; it is not chosen by comparison with Iter057U/X coefficients.

## Allowed repair

The execution wrapper may replace only `cubic_and_Q` by the exact contraction above, while preserving the frozen seed, P projection, divergence order, convention map, degree, target firewall and classifier. The constructor must again pass all internal controls and freeze a new payload hash before any U/X comparator is created or run.
