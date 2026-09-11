# QGR Iter007-G3 — microscopic Lorentz breaking of the history-ordering correction

Date: 2026-09-12
Status: `PASS_SCOPED_MICROSCOPIC_S4_ONLY / CONTINUUM_LORENTZ_RESTORED_AS_H_TO_ZERO`

## Question

The G2 history-ordering correction is fixed by the exact 24-permutation covariance. Does that covariance respect the continuous Lorentz symmetry of the emergent local QGR action, or only the microscopic `S4` symmetry of one `B4` cell?

## Exact test

Use the incidence form

`C=J-I`

and the explicit rational continuous `C`-preserving transformation already found in Iter004,

`L(r)=`

`[[r,0,r-1,r-1],`
` [0,1/r,(1-r)/r,(1-r)/r],`
` [0,0,1,0],`
` [0,0,0,1]]`.

At `r=2`, exactly

`L^T C L=C`.

Lift `L` to the six-dimensional antisymmetric pair/two-form representation `R=Lambda^2 L`.

As a control, construct the natural two-form bilinear form induced from `C`,

`G2_(ij,kl)=C_(ik)C_(jl)-C_(il)C_(jk)`.

The exact calculation gives

`R^T G2 R=G2`.

So the induced representation is being handled correctly.

Now apply the same transformation to the exact 24-history ordering covariance `Cov` from G2. The result is

`R^T Cov R != Cov`.

For the recorded `r=2` witness:

- `33` matrix entries of the covariance difference are nonzero;
- the maximum exact absolute difference is `8/3`.

Therefore the finite-cell history-ordering covariance is **not** invariant under the full continuous `O(C)` group.

## Interpretation

The local all-orders two-derivative QGR action has emergent continuous Lorentz covariance, but the first finite-cell quantum ordering correction retains only the microscopic `S4` symmetry of the `B4` cell.

This is not inconsistent with Lorentz recovery because the correction is already known to begin at

`O(h^4)`

in the traced coarse channel and therefore vanishes as the refinement scale tends to zero.

However, at finite physical cell scale it represents a genuine Lorentz-violating microscopic effect unless an additional orientation/refinement average removes it.

## Consequence for model viability

This result creates a new prospective gate rather than being hidden:

1. either repeated refinement/orientation averaging restores Lorentz covariance faster than the correction accumulates;
2. or the microscopic cell scale must be small enough that the residual `O(h^4)` Lorentz violation lies below observational constraints;
3. or the candidate fails if a finite unsuppressed preferred-frame effect survives the normalized observable map.

No post-hoc isotropization rule may be added merely because Lorentz violation is phenomenologically inconvenient.

## Scientific significance

G2/G3 together provide the first clear candidate distinction between QGR and classical GR:

- classical local sector: exact Lorentz-covariant two-derivative gravity;
- finite-cell quantum coarse sector: fixed `S4` ordering covariance with an `O(h^4)` curvature-dependent random-unitary correction;
- continuous Lorentz symmetry is recovered only in the refinement limit unless a derived averaging mechanism closes the finite-scale anisotropy.

## Classification

`PASS_SCOPED_FINITE_CELL_HISTORY_ORDERING_CORRECTION_HAS_ONLY_MICROSCOPIC_S4_SYMMETRY_AND_BREAKS_CONTINUOUS_LORENTZ_AT_O_H4`.

## Reproducibility

`code/qgr_iter007_g3_lorentz_covariance_audit.py`
