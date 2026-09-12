# Iteration 041 — held-out Weyl^3 generalization and prediction-contract stress

Date: 2026-09-12
Status: `PREREGISTERED / READY FOR PRODUCTION`

## Motivation

Iter040 terminally established a calibration-free Weyl^3 response manifold on four frozen diagonal training Hessians plus rotations. A stronger test must now be **out of sample**: the numerical code may not select or tune shapes after looking at production results, and neither `beta` nor `c6` may be fitted.

Iter041 asks whether the same response law transfers to preregistered generic **off-diagonal trace-free symmetric tidal Hessians**, plus held-out rotated cubic-null controls. This tests generalization inside the same weak static vacuum tidal family rather than repeating the G40 training set.

## Frozen held-out nonzero-cubic Hessians

All six matrices are symmetric and trace-free and are frozen before implementation/production:

```text
G0 = [[ 1.00,  0.35, -0.20],
      [ 0.35, -0.25,  0.15],
      [-0.20,  0.15, -0.75]]

G1 = [[ 0.70, -0.40,  0.30],
      [-0.40,  0.80, -0.10],
      [ 0.30, -0.10, -1.50]]

G2 = [[ 1.40,  0.25,  0.45],
      [ 0.25, -0.90, -0.35],
      [ 0.45, -0.35, -0.50]]

G3 = [[ 0.45,  0.55, -0.25],
      [ 0.55,  0.35,  0.40],
      [-0.25,  0.40, -0.80]]

G4 = [[ 1.10, -0.20,  0.50],
      [-0.20, -0.30,  0.25],
      [ 0.50,  0.25, -0.80]]

G5 = [[ 0.90,  0.45,  0.10],
      [ 0.45, -1.20, -0.30],
      [ 0.10, -0.30,  0.30]]
```

Their frozen cubic traces are approximately
`[+0.737625, -1.965, +1.77975, -0.263625, +0.75675, -1.44225]`, all nonzero. No one of these matrices appeared in Iter040.

The G40 training reference `H0=diag(1,1,-2)` may be evaluated only as a fixed normalization control; it may not be used to retune thresholds or choose held-out shapes.

## Frozen held-out cubic-null family

Let `N0=diag(1,-1,0)` (the algebraic null shape), but do **not** reuse its G40 identity orientation as a scientific lane. Four new proper rotations are frozen:

- `Rz(17°) N0 Rz(17°)^T`;
- `Ry(31°) N0 Ry(31°)^T`;
- `(Rz(23°) Ry(19°)) N0 (...)^T`;
- `(Rz(47°) Ry(28°)) N0 (...)^T`.

Each has nonzero quadratic tidal norm and exact zero cubic trace by similarity.

## Stream A — held-out shape-transfer at fixed scale (6 lanes)

For each `Gi`, compute the existing G40 finite-cell torsion/holonomy/Weyl proxy at `h=0.05`, `kappa=0.04` and compare

`q(Gi)=W3(Gi)/tr(Gi^3)`

to the fixed H0 normalization control at the same `(h,kappa)`.

PASS per lane requires:
- torsion residual `<3e-9`, connection minimum singular value `>1e-8`, metric/Lorentz controls within inherited G40 tolerances;
- finite nonzero Weyl norm and finite nonzero `q`;
- relative difference `|q(Gi)-q(H0)|/|q(H0)| < 0.02`.

No held-out matrix may be dropped after production.

## Stream B — held-out refinement transfer (6 lanes)

For each `Gi`, evaluate `h=[0.10,0.075,0.05]`, fixed `kappa=0.04`, and compare q to H0 at each same h.

PASS requires all inherited solver/geometry controls and either:
- the held-out relative q error decreases from h=0.10 to h=0.05, **or** both errors are already `<1e-4`;
- finest relative q error `<0.02`.

This is numerical refinement evidence only, not an analytic arbitrary-background theorem.

## Stream C — held-out amplitude law (4 lanes)

For `G0,G1,G2,G5`, at fixed `h=0.05`, evaluate `kappa=[0.025,0.04,0.06,0.08,0.10]`.

PASS requires inherited solver controls and log-log slopes:
- Weyl norm vs kappa in `[0.85,1.15]`;
- `|W3|` vs kappa in `[2.70,3.30]`.

## Stream D — held-out rotated cubic-null falsifiers (4 lanes)

For the four new rotated N0 profiles, evaluate `h=[0.10,0.075,0.05]`, `kappa=0.05`.

PASS requires:
- inherited solver controls;
- finest Weyl norm `>1e-8`;
- finest `|W3|/||W||^3 < 0.02`;
- normalized absolute cubic residual decreases from h=0.10 to h=0.05, or both are already `<1e-5`.

A failure here is scientifically important: it would show the G40 null law does not transfer cleanly out of sample at the frozen discretization.

## Stream E — held-out rotation covariance of G0 (4 lanes)

Rotate the new off-diagonal `G0` by four new proper rotations:
`Rz(13°)`, `Ry(29°)`, `Rz(37°)Ry(21°)`, `Rz(53°)Ry(34°)`.
For each, compare against unrotated G0 at `h=[0.10,0.075,0.05]`, `kappa=0.04`.

PASS requires inherited solver controls, finite/nonzero responses, and for the normalized signed cubic response `W3/||W||^3`:
- finest relative rotation discrepancy `<0.02`;
- discrepancy decreases from coarse to fine, or both are already `<1e-4`.

## Production matrix

- A held-out shape transfer: 6 lanes;
- B held-out refinement transfer: 6 lanes;
- C held-out amplitude law: 4 lanes;
- D rotated null falsifiers: 4 lanes;
- E held-out rotation covariance: 4 lanes;
- total **24 scientific lanes** + aggregate;
- `fail-fast:false`;
- safe maximum parallelism up to 24.

## Terminal classifications

Full PASS:
`PASS_SCOPED_HELDOUT_WEYL3_GENERALIZATION_AND_PREDICTION_CONTRACT_STRESS` if all 24 frozen lanes pass.

Partial/scientific non-promotion:
`PARTIAL_SCOPED_HELDOUT_WEYL3_GENERALIZATION` if controls are valid but one or more frozen scientific relations fail.

Control-invalid:
`CONTROL_INVALID_OR_INCOMPLETE_ITER041` if expected lanes are missing or numerical/geometry controls are invalid such that the scientific comparison cannot be interpreted.

## Decision logic after terminal result

- Full PASS: do **not** add denser static-electric tidal scans. Promote the calibration-free static tidal response law as held-out scoped support and move to a genuinely new sector, preferably a dynamical/magnetic-Weyl or other non-static covariance test, while keeping absolute amplitudes parameterized by `c6`.
- Partial: localize which transfer property fails (shape, refinement, amplitude, null or rotation); do not weaken thresholds post hoc.
- Control invalid: repair controls only, without scientific interpretation.

## Claim locks

- theory established remains **0%**;
- this is same-field-content weak static tidal-sector evidence, not arbitrary spacetime;
- finite numerical refinement is not an analytic continuum theorem;
- `beta` remains an explicit matching/calibration parameter under Iter039 authority;
- `beta=1` is not authorized as physics;
- `c6` remains unfixed and is not fitted here;
- response ratios/nulls are not absolute quantum phases;
- no experimental confirmation;
- no physical multiple-branch weights from G35–G37 distant algebraic roots;
- KMQGB `NEW_REQUIRED` remains unauthorized absent independent benchmark authority.
