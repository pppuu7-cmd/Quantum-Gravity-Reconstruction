# QGR Iter007-G4 — finite-scale Lorentz no-go for positive ordering noise

Date: 2026-09-12
Status: `PASS_SCOPED_NO_GO_FOR_NONZERO_POSITIVE_FULL_LORENTZ_INVARIANT_ORDERING_COVARIANCE`

## Question

Could the finite-cell `S4` history-ordering covariance from G2 be made exactly continuous-Lorentz invariant by a derived orientation average while remaining a nonzero positive coarse quantum channel correction?

## Input

The exact 24-history covariance on the six pair/commutator components is positive definite, with spectrum

`1/3 x3` and `5/3 x3`.

The continuous Lorentz stabilizer of the incidence form `C=J-I` has a noncompact six-dimensional representation on the two-form/pair space.

## General finite-dimensional argument

Suppose a positive-definite covariance `Q` were invariant under the full represented continuous Lorentz group:

`R(L)^T Q R(L)=Q`.

Then, after the change of basis `Q^(1/2)`, every `R(L)` would be an ordinary orthogonal matrix. The image of the group in this finite-dimensional representation would therefore be bounded/compact.

But the two-form representation of Lorentz boosts is unbounded. Hence no **nonzero positive-definite** covariance on the full nontrivial two-form representation can be invariant under the full continuous Lorentz group.

For a positive-semidefinite covariance the only possible invariant support would have to lie in a Lorentz-trivial subrepresentation. The ordinary two-form representation contains no scalar/trivial sector, so the fully Lorentz-invariant positive covariance is zero.

## Exact QGR witness

Using the explicit rational `C`-preserving boost family from Iter004 and its induced wedge representation, the squared Frobenius norm of the transformed G2 ordering covariance grows exactly as follows:

- unboosted: `26/3`;
- `r=2`: `973/18`;
- `r=4`: `111811/96`;
- `r=8`: `110905033/4608`;
- `r=16`: `10973870467/24576`.

Thus the positive covariance cannot be made invariant under this already-derived continuous subgroup unless its coefficient is sent to zero.

## Consequence

Exact continuous Lorentz symmetry at finite cell scale is **not** compatible with a nonzero positive ordering-noise covariance of the G2 type.

Therefore QGR has only two currently admissible routes:

1. the correction vanishes in the refinement/continuum limit (`h->0`), restoring Lorentz symmetry;
2. at a finite physical microscopic scale the model predicts a suppressed preferred-frame/tetrahedral correction whose size must satisfy observations.

A normalized average over the full noncompact Lorentz group cannot be introduced to erase this effect: that would both violate the earlier noncompact-Haar rule and contradict the positive-covariance no-go.

## Relation to G2/G3

G2 established that the nonunitary coarse correction begins at `O(h^4)`.

G3 established explicitly that its fixed covariance has only microscopic `S4` invariance.

G4 strengthens this to a structural statement: **nonzero positive finite-cell ordering noise cannot be exactly continuous-Lorentz invariant in this representation**.

Thus Lorentz recovery requires suppression of the effect under refinement, not a post-hoc isotropization prescription.

## Open phenomenological gate

The next required task is to map `h` and the curvature commutators to a normalized observable and derive a bound/prediction. Until then, no experimental Lorentz-violation claim is promoted.

Classification:

`PASS_SCOPED_NONZERO_POSITIVE_ORDERING_CHANNEL_CORRECTION_CANNOT_HAVE_EXACT_FULL_CONTINUOUS_LORENTZ_INVARIANCE_AT_FINITE_CELL_SCALE`.

## Reproducibility

`code/qgr_iter007_g4_positive_covariance_lorentz_nogo.py`
