# QGR Iter005-G1B — complete two-derivative cubic vertex count

Date: 2026-09-11
Status: `PASS_SCOPED_KINEMATIC_CUBIC_SPACE_COUNTED / NOETHER_KERNEL_OPEN`

## Question

How large is the complete local two-derivative cubic interaction space before imposing nonlinear Noether consistency?

## Representation setup

The QGR-L1 field is

`H = Sym^2(W4)`,

with ten components.

At cubic order there are three identical bosonic field legs. Their permutation group is `S3`.

For each of the four relational derivative directions, the three leg momenta satisfy

`k1 + k2 + k3 = 0`.

Therefore, after momentum conservation, leg momentum lives in the two-dimensional standard representation `U` of `S3` rather than the full three-dimensional permutation representation.

The complete degree-two momentum-polynomial representation is

`Sym^2(W4 tensor U)`.

This formulation incorporates translation invariance and the integration-by-parts quotient through momentum conservation before the invariant count is taken.

## Exact invariant count

The bosonic cubic field part is `H^tensor3` with `S3` permuting the legs. The trace of a simultaneous `S4 x S3` element is evaluated cycle-by-cycle.

Averaging the product of

- the cubic field character;
- the degree-two momentum-polynomial character

over the full `S4 x S3` group gives exactly

`317`.

Thus the complete kinematic space of local, bosonic, `S4`-invariant, total-two-derivative cubic vertices is **317-dimensional** before nonlinear gauge consistency.

Classification:

`PASS_SCOPED_COMPLETE_KINEMATIC_TWO_DERIVATIVE_CUBIC_VERTEX_COUNT_317`.

## Interpretation

This is deliberately a large number. It shows that `S4`, locality, Bose symmetry, and two-derivative power counting alone do **not** select the nonlinear theory.

The real discriminator is the already fixed nonlinear frame transformation from

`results/ITER005_G1B_FRAME_PULLBACK_ALGEBRA.md`.

The active problem is now the linear Noether map

`N: cubic_317 -> gauge_variation_space`

with inhomogeneous source `-delta_1 S_2`.

A successful self-coupling requires solving

`delta_0 S_3 = - delta_1 S_2`.

The size of the homogeneous kernel will determine whether the interaction is unique, low-dimensional, or underdetermined.

## Important guard

The number 317 is **not** the number of physically allowed couplings. It is only the complete pre-Noether kinematic basis dimension.

No Einstein-Hilbert interaction has been inserted or used in obtaining this number.

## Reproducibility

`code/qgr_iter005_g1b_two_derivative_cubic_count.py`
