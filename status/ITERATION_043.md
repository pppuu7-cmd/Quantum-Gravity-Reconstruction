# Iter043 — Independent radiative TT-wave covariance / reconstruction gate

Status: PREREGISTERED BEFORE IMPLEMENTATION/PRODUCTION
Date: 2026-09-12

## Motivation
Iter042R terminally localized the original G42 scalar-covariance defect to mixed internal/coordinate curvature frames and validated all-coordinate frame completion on the frozen boosted-static family. The next recovery-authorized step is an independent radiative geometry that does not reuse the G40–G42 static Hessian family.

## Frozen scientific object
A linearized transverse-traceless vacuum plane gravitational wave in Minkowski background. For propagation direction `n`, plus/cross polarization tensors are built from a deterministic orthonormal transverse basis. The perturbation is
`h_ij(q) = A [cos(psi) eplus_ij + sin(psi) ecross_ij] cos(k q + phi)`, `q=t-n.x`.
The linearized all-lowered Riemann tensor is evaluated analytically from second derivatives of `h`; because the source is a TT vacuum wave, Ricci/scalar curvature must vanish to numerical precision and `weyl_proxy` must reproduce the Riemann tensor within control tolerance.

No event-source normalization, beta choice, c6 value, distant-root branch weight, or KMQGB conclusion enters this gate.

## Frozen matrix — 24 independent lanes
Cartesian propagation directions `n`: x, y, z (3).
Polarization mixing angles `psi`: 0, pi/8, pi/4, 3pi/8 (4).
Wave phases `phi`: 0.23, 1.07 (2).
Total: 3 x 4 x 2 = 24 lanes.
Fixed amplitude A=0.013 and wavenumber k=1.7. These only set a nonzero test scale.

Each lane also uses a held boost vector selected deterministically from a preregistered panel:
`[(0.11,0.03,-0.04),(-0.06,0.12,0.02),(0.04,-0.05,0.14),(0.09,-0.08,0.05)]`, cycling by lane index.

## Frozen controls and thresholds
1. TT controls: `|tr(e)| < 1e-13`, `||n_i e_ij|| < 1e-13`.
2. Vacuum control: Ricci Frobenius norm / max(Riemann norm,1e-30) < `1e-11`; |scalar| / max(Riemann norm,1e-30) < `1e-11`.
3. Weyl reconstruction: `||W-R|| / max(||R||,1e-30) < 1e-11`.
4. Lorentz matrix control: `||Lambda^T eta Lambda-eta|| < 1e-12`.
5. All-index scalar covariance under boost: absolute normalized differences of W2 and W3 < `1e-10`, where normalization is `max(||W||^2,1e-30)` for W2 and `max(||W||^3,1e-30)` for W3. This absolute-normalized rule is frozen because type-N scalar invariants are expected to vanish.
6. Radiative nontriviality: electric norm > `1e-8`, magnetic norm > `1e-8`.
7. Radiative balance: `| ||E||/||B|| - 1 | < 1e-10`.
8. Type-N scalar-null check: `|W2|/max(||W||^2,1e-30) < 1e-10` and `|W3|/max(||W||^3,1e-30) < 1e-10`.

## Frozen interpretation
- `PASS_SCOPED_INDEPENDENT_TT_RADIATIVE_WEYL_COVARIANCE`: all 24 lanes controls valid and all scientific relations pass.
- `PARTIAL_SCOPED_TT_RADIATIVE_WEYL_COVARIANCE`: all controls valid, at least one but not all scientific relations/lanes pass.
- `FAIL_SCOPED_TT_RADIATIVE_WEYL_COVARIANCE`: all controls valid and no lane passes or a common scientific relation fails broadly.
- `ITER043_CONTROL_OR_IMPLEMENTATION_INVALID`: any lane fails TT/vacuum/Weyl reconstruction/Lorentz controls; no physical interpretation until repaired without changing frozen science.

## Claim locks
A PASS is only a held-out tensor/observable reconstruction and Lorentz-covariance test on analytic linearized TT waves. It is not an end-to-end derivation of gravitational radiation from QGR dynamics, not a nonlinear wave theorem, not experimental validation, and does not fix beta or c6. Theory established remains 0%.
