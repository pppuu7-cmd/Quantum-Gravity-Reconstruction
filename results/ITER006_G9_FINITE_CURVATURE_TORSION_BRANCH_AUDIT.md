# QGR Iter006-G9 — finite-curvature nonlinear torsion branch audit

Date: 2026-09-11
Status: `NUMERICALLY_VERIFIED_FINITE_CURVATURE_REGULAR_BRANCH / GLOBAL_BRANCH_FINITENESS_OPEN`

## Objective

Test whether the locally unique discrete torsion-free connection found infinitesimally near the symmetric seed survives on a finite, genuinely curved toy configuration, rather than only on an almost-flat/pure-gauge perturbation.

## Toy configuration

Use the same exact `C=J-I` internal bilinear form and the same six-generator basis of `o(C)` as in G5.

Choose a noninfinitesimal conformal frame field

`F(x)=Omega(x) I`

on a small four-direction lattice, with

`log Omega(x)=a.x + (1/2) x^T Q x`,

where the recorded deterministic coefficients in the reproducibility script contain nonzero mixed quadratic terms.

The mixed terms make neighboring connection solutions path dependent and generate nonzero plaquette holonomy.

Each outgoing edge holonomy is parameterized as

`L_i=exp(sum_m omega_(i,m) B_m)`

and the full finite torsion equations

`e_i(v)+L_i^-1 e_j(v+i)=e_j(v)+L_j^-1 e_i(v+j)`

are solved numerically for all 24 connection parameters at the central vertex and its four nearest neighbors.

## Nonlinear solve

At the central vertex the solved branch has

- residual norm approximately `2.0e-14`;
- connection-parameter norm approximately `0.468`;
- smallest singular value of the nonlinear torsion Jacobian approximately `0.349`;
- Jacobian condition number approximately `23.1`.

Thus this root is well separated from a local Jacobian singularity.

All four neighboring vertex solves also converge with residuals below `1e-13` in the recorded run.

## Nonzero curvature / holonomy

For every coordinate plaquette `(i,j)`, compare the two path transports from the origin to the opposite plaquette corner and form the relative holonomy.

The six values of

`||H_ij-I||`

lie approximately in the interval

`[0.129,0.249]`.

The corresponding holonomies satisfy

- `det H_ij = 1` to numerical precision;
- `H_ij^T C H_ij = C` with maximum recorded error of order `1.7e-15`.

Therefore the tested finite branch has genuine nontrivial Lorentz holonomy and is not merely an identity/pure-frame relabeling test.

## Local basin test

Twelve deterministic random starts were generated around the central nonlinear root. All 12 converged to a solution with residual below `1e-8`.

Comparing the resulting finite transport matrices, the maximum distance from the reference branch was below

`4e-11`.

This is evidence for a single robust local solution basin for this finite-curvature toy.

## Classification

`NUMERICALLY_VERIFIED_FINITE_CURVATURE_REGULAR_TORSION_BRANCH_WITH_NONZERO_HOLONOMY_AND_STABLE_LOCAL_BASIN`.

## What this improves

The G5 implicit-function result is no longer supported only at the identity connection. A finite-amplitude curved example exists in which

- the nonlinear torsion equations solve accurately;
- the connection Jacobian remains nonsingular;
- loop holonomy is nonzero;
- nearby initial conditions return to the same branch.

## Boundary

This is **not** a proof that arbitrary strong-curvature data have a finite number of regular branches. In particular it does not exclude

- distant additional branches outside the tested basin;
- singular roots;
- continuous solution components;
- runaway solutions in noncompact connection directions.

Those remain the dominant global Iter006 measure/finiteness blocker.

## Reproducibility

`code/qgr_iter006_g9_finite_curvature_torsion_toy.py`
