# QGR Iter005-G2 — quartic uniqueness from affine-shift rank

Date: 2026-09-11
Status: `PASS_SCOPED_QUARTIC_UNIQUE_MODULO_KINEMATIC_NULLS`

## Objective

After the exact existence certificate for

`delta_0 S4 + delta_1 S3 = 0`,

determine whether a nonzero physical homogeneous quartic deformation `Delta S4` can satisfy

`delta_0 Delta S4 = 0`

at total derivative degree two.

## Cheap strict subtest

Full linear gauge invariance implies invariance under the affine subgroup of the already derived transformation

`delta_0 h_ij = D_i xi_j + D_j xi_i`.

For affine `xi`, `delta_0 h_ij` is an arbitrary constant symmetric shift in the ten-dimensional field space `Sym^2(W4)`.

Therefore any homogeneous quartic Noether vertex must lie in the kernel of the constant-shift variation map.

In momentum space this is equivalent to evaluating the fully symmetrized quartic vertex with one external field leg carrying zero momentum and arbitrary field polarization, while the other three momenta obey momentum conservation.

## Exact modular construction

Domain:

- 2,066 raw local bosonic `S4` quartic orbit directions `h h (D h)(D h)`;
- exact physical action quotient dimension already established independently: **1,694**;
- kinematic/IBP nullity: **372**.

The constant-shift variation is built exactly over a finite field with prime

`p = 1,000,003`.

Momentum conservation is imposed algebraically as

`r = -p-q`.

The resulting variation columns are sparse: each raw quartic orbit produces at most a few hundred nonzero coefficient entries, and the full target support is generated without numerical approximation.

Sparse modular Gaussian elimination gives

`rank_p(affine_shift_map) = 1694`.

A nonzero 1694-rank minor modulo a prime proves

`rank_Q >= 1694`.

But the physical quartic domain quotient has dimension exactly 1694, so

`rank_Q <= 1694`.

Hence

`rank_Q = 1694`.

Therefore the physical kernel of the affine-shift map is zero. Since full `delta_0` invariance implies affine-shift invariance, the homogeneous physical quartic Noether kernel is also zero.

## Conclusion

`dim Ker(delta_0 at quartic two-derivative level) / kinematic_nulls = 0`.

Combined with the exact inhomogeneous existence certificate, the quartic self-coupling is unique modulo kinematic/IBP null directions.

Classification:

`PASS_SCOPED_QUARTIC_NOETHER_EXISTENCE_AND_UNIQUENESS_MODULO_KINEMATIC_NULLS`.

## Scope guard

This closes the local quartic two-derivative Noether problem. It does not by itself establish:

- all-orders nonlinear completion;
- weak-background causal stability;
- same-realization continuum/refinement closure;
- finite interacting quantum amplitudes;
- equivalence principle or experiment;
- independent KMQGB passage.

## Reproducibility

`code/qgr_iter005_g2_quartic_affine_rank.py`
