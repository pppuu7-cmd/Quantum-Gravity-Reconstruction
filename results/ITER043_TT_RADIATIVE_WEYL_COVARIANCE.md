# QGR Iter043 — independent TT radiative Weyl covariance

Date: 2026-09-12
Status: `PASS_SCOPED_INDEPENDENT_TT_RADIATIVE_WEYL_COVARIANCE`

## Frozen gate

Preregistered in `status/ITERATION_043.md` before implementation/production. The scientific object was an analytic linearized TT vacuum plane-wave curvature tensor independent of the earlier static Hessian families. The 24-lane matrix covered 3 propagation directions x 4 polarization mixtures x 2 phases with a held boost panel.

This gate tested the corrected all-coordinate observable layer after G42R. It did **not** assume or test that QGR dynamics generates the TT wave.

## Authoritative production

- trigger/head: `79b7325179aab34e83bbbc998152b81398221ef5`
- workflow: `qgr-iter043-tt-radiative`
- run: `34715559793`
- aggregate job: `103613094190`
- aggregate artifact: `10303724918`
- artifact digest: `sha256:bd74de5bd2b0b17a9a0e043954f5f97e8fc964e1e64da1bb3d137b01f0286b83`
- expected/found scientific lanes: `24/24`
- lane passes: `24/24`
- controls valid: `true`

## Frozen aggregate outcome

Classification:

`PASS_SCOPED_INDEPENDENT_TT_RADIATIVE_WEYL_COVARIANCE`

Strongest aggregate diagnostics:

- maximum TT trace: `0.0`;
- maximum TT transverse norm: `0.0`;
- maximum Ricci ratio: `0.0`;
- maximum scalar-curvature ratio: `0.0`;
- maximum Weyl reconstruction error: `0.0`;
- maximum Lorentz-matrix error: `4.681459141485685e-16`;
- maximum W2 covariance error: `2.0872426177969475e-16`;
- maximum W3 covariance error: `2.9099380740141584e-17`;
- maximum electric/magnetic balance error: `2.220446049250313e-16`;
- maximum type-N W2 null: `0.0`;
- maximum type-N W3 null: `7.972433079490845e-19`;
- minimum electric norm: `0.012754981117797543`;
- minimum magnetic norm: `0.012754981117797543`.

## Scientific interpretation

The frame-completed observable layer reproduces and Lorentz-transports a held-out analytic linearized TT radiative geometry over the entire frozen 24-lane panel. This is a materially independent generalization beyond the G40–G42 static/boosted tidal families.

It closes the preregistered `INDEPENDENT_RADIATIVE_GEOMETRY_HELDOUT_VALIDATION` blocker **in this scoped tensor/observable sense**.

It does **not** yet show that the QGR-L1 dynamical equations generate those radiative modes. That requires a separate end-to-end gate beginning from the already-derived QGR-L1 kinetic/action authority and ending at the TT curvature observable without inserting the TT field as an input solution.

## Claim locks

- this is a held-out analytic linearized tensor/observable test, not an end-to-end radiation derivation;
- no nonlinear radiation theorem follows;
- finite panels are not global theorems;
- `beta` remains an explicit matching/calibration parameter; `beta=1` is not physics;
- `c6` remains unfixed;
- no experimental confirmation;
- theory established remains `0%`;
- KMQGB `NEW_REQUIRED` remains unauthorized.
