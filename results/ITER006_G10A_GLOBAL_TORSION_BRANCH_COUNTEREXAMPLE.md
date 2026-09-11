# QGR Iter006-G10A — global torsion-branch finiteness counterexample

Date: 2026-09-12
Status: `REFUTED_IN_SCOPE_ALL_TORSION_ROOTS_FINITE / IDENTITY_CONNECTED_BRANCH_NOT_REFUTED`

## Objective

Test the G10 hypothesis that the finite-cell torsion equations have only finitely many regular connection roots and no noncompact runaway branches.

## Exact reduction at the symmetric flat seed

At the flat `B4` seed write

`y_ij=L_i^{-1} e_j`.

The finite torsion equations imply exactly

`y_ij-y_ji=e_j-e_i`.

For every unordered pair `i<j` choose `z_ij=y_ij`.  The reverse orientation is then fixed linearly.  Lorentz compatibility of `L_i` is equivalent to requiring that, for every fixed `i`, the three vectors `y_ij` with `j!=i` have the same Gram matrix as the three seed null directions `e_j`.

This produces exactly

- 6 unordered edge vectors;
- 24 real unknown components;
- 24 quadratic Gram constraints.

No matrix exponential or Lorentz-coordinate chart is needed for this reduction.

## Identity-connected branch

The identity solution is

`y_ij=e_j`.

Its exact integer Jacobian has

- rank `24/24`;
- determinant `47,775,744 = 2^16 * 3^6`.

Thus the identity branch is isolated and locally unique, consistent with the earlier G5 implicit-function result.

## Disconnected singular branch

A broad numerical search found distant exact solutions of the same reduced quadratic system.  After correction to the variety, one representative has

- residual below `1e-10`;
- Jacobian rank `22`;
- local nullity `2`.

Reconstruction of the corresponding Lorentz transports shows that the distant branch can lie in the proper, time-oriented Lorentz component; it is not merely an improper reflection artifact.

## Predictor/corrector continuation

The rank-22 point was continued using the two-dimensional Jacobian null space.  At each step, 22 independent quadratic constraints plus two normal-plane constraints were solved, and the full 24-equation residual was rechecked.

Over 50 continuation steps:

- solution norm grew from about `10.93` to above `30.2`;
- full residual remained of order `1e-14`;
- Jacobian rank remained `22`.

Therefore the flat symmetric seed itself contains a disconnected, noncompact two-dimensional torsion solution manifold.

## Physical interpretation

This **refutes** the statement that all finite-cell torsion roots are generically a finite set suitable for indiscriminate branch summation.

It does **not** refute the QGR connection construction already fixed before G10.  QGR had independently derived the infinitesimal torsion-free compatible connection from `G,DG`.  On the exact flat seed `DG=0`, so the same-realization finite connection must approach the identity.  The distant manifold does not satisfy that refinement/continuum matching condition.

The result therefore changes the physical prescription:

- do **not** sum every algebraic finite-cell torsion root;
- treat the connection as a derived object;
- select the branch analytically connected to `L=I` and matching the previously derived infinitesimal Levi-Civita connection under refinement;
- define strong-curvature coarse transport by composition/refinement of that principal branch, not by re-solving the coarse torsion polynomial and summing all roots.

This selector is prospective: it follows from the already frozen same-realization and first-jet connection requirements, not from observing the unwanted distant roots.

Classification:

`REFUTED_IN_SCOPE_ALL_TORSION_ROOTS_FINITE__DISCONNECTED_NONCOMPACT_FINITE_CELL_BRANCH_EXISTS__PHYSICAL_REFINEMENT_CONNECTED_BRANCH_REMAINS_VIABLE`.

## Reproducibility

`code/qgr_iter006_g10a_seed_runaway_branch.py`
