# Iter040 — calibration-free Weyl^3 response manifold

Date: 2026-09-12
Status: `PASS_SCOPED_CALIBRATION_FREE_WEYL3_RESPONSE_MANIFOLD_ESTABLISHED`

## Authoritative production provenance

- workflow: `qgr-iter040-weyl-response`
- run: `34709914980`
- launch head: `b990644250a4df7d29ddec467629c56956fd83e9`
- aggregate job: `103596975475`
- aggregate artifact: `10302927388` (`qgr-iter040-summary`)
- aggregate digest: `sha256:898899c85f7c304b9f0032e6138f55dd7dc12339fa07f03728b0f774e1e03fe9`
- frozen preregistration: `status/ITERATION_040.md`

All **20/20** preregistered scientific lanes passed: A 4/4, B 3/3, C 3/3, D 4/4, E 6/6.

## Terminal aggregate

The production aggregate returned:

`PASS_SCOPED_CALIBRATION_FREE_WEYL3_RESPONSE_MANIFOLD_ESTABLISHED`.

Key frozen diagnostics:

- H2 finest normalized absolute cubic residual: `1.875882416525863e-05`;
- finest relative sign pattern for nonzero cubic shapes: H0 `+`, H1 `+`, H3 `-` in the common finite-cell convention;
- maximum finest rotation discrepancy: `5.168073699081922e-08`;
- relative spread of `q(H,h)=W3/tr(H^3)` across H0/H1/H3:
  - h=0.10: `9.853846896674696e-04`;
  - h=0.075: `5.530346909482158e-04`;
  - h=0.05: `2.453977185447458e-04`;
- Weyl-norm amplitude-slope range: `[0.9998691592541441, 1.000002740132653]`;
- Weyl-cubic amplitude-slope range: `[2.999514418717107, 3.0000081778357783]`.

## Scoped prediction contract established by this gate

Within the frozen same-field-content weak static vacuum tidal realization:

1. `||W|| ~ kappa` and the Weyl-cubic response kernel scales as `kappa^3`.
2. The nonzero tidal-shape cubic responses obey the calibration-free ratio
   `H0:H1:H3 = 1:3:-1`, up to one common convention/c6 multiplier.
3. H2 has nonzero Weyl curvature but vanishing leading cubic tidal invariant and passes the finite-cell cubic-null test toward refinement.
4. Proper spatial rotations recover the same normalized cubic response toward refinement with the strongest tested finest discrepancy about `5.17e-08`.
5. `beta` does not enter the pure Weyl^3 response-kernel ratios.
6. Multiplying by an arbitrary nonzero `c6` rescales the absolute six-derivative response but leaves the frozen ratios, signs and null relations unchanged.

## Scientific interpretation

This is a parameterized and falsifiable **shape-level** prediction manifold inside the tested weak static tidal sector. It is stronger than the earlier single-background Weyl-sensitivity witness because several independent shapes, a cubic-null profile, amplitude scaling and rotations pass the same frozen response law.

It does **not** determine the absolute six-derivative phase amplitude. Under Iter039 authority, `beta` remains an explicit matching/calibration parameter and `c6` remains an unfixed Wilson coefficient until a genuine independent Weyl-active absolute matching datum exists.

The result is not an analytic theorem for arbitrary spacetime and not an experimental confirmation. The finite-cell convergence evidence is scoped to the tested same-field-content weak tidal family.

## Decision

The next useful gate must not repeat the four training Hessians. It should test the frozen response law out of sample on preregistered generic off-diagonal trace-free tidal tensors, including independent null and rotation controls, while preserving `beta`/`c6` as unfitted directions. If that held-out transfer passes, the next frontier should move to an end-to-end parameterized prediction contract and/or a genuinely new dynamical/magnetic Weyl sector rather than denser repeats of G40.

## Claim locks

- theory established: **0%**;
- `beta=1` is not authorized as physics;
- `beta` is an explicit matching/calibration parameter under current Iter039 authority;
- `c6` remains unfixed;
- response-kernel ratios are not absolute quantum phases;
- no experimental confirmation;
- no arbitrary-spacetime/global Weyl theorem;
- no physical branch weights from G35–G37 distant algebraic roots;
- KMQGB `NEW_REQUIRED` remains unauthorized absent independent benchmark authority.
