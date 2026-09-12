# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter047`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / SIX_DERIVATIVE_WEYL3_CURVATURE_CLASS_ACTIVATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program readiness: **96%** — internal roadmap readiness only, not probability of correctness and not fraction of quantum gravity solved. The increase 95 -> 96 is credited specifically to terminal Iter046 exact finite-amplitude nonlinear pp-wave closure.
- Iter005–Iter046: completed in their stated scopes.
- Iter047: preregistered, implemented and production launched, 24 scientific lanes + aggregate.
- Theory established: **0%**.
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`.
- `beta`: explicit matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6`: **unfixed** and remains symbolic in Iter047.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Terminal Iter046 — exact finite-amplitude nonlinear pp-wave radiation
Durable record: `results/ITER046_QGR_L1_EXACT_NONLINEAR_PPWAVE_RADIATIVE_SECTOR.md`.

Authority:
- preregistration commit `125d030e90ac86697710c9ed0cee432c5ff54596`;
- production head `37ff955a57b6822d800b6755282a6bc557c3a0e2`;
- run `34718135187`;
- aggregate job `103621013033`;
- aggregate artifact `10305972518`;
- digest `sha256:ca1cfb10420cb4e79f4324f009c0a664317098b7bb08b717f052d82397961a89`.

Terminal classification:
`PASS_SCOPED_QGR_L1_EXACT_FINITE_AMPLITUDE_NONLINEAR_PPWAVE_RADIATIVE_SECTOR`.

Frozen aggregate consumed all **34/34** unique scientific lanes with valid controls:
- A 12/12 exact finite-amplitude harmonic pp-wave vacuum witnesses;
- B 6/6 deliberately non-harmonic non-vacuum falsification controls;
- C 6/6 held-out polarization mixtures;
- D 6/6 exact full-Riemann amplitude-scaling witnesses;
- E 4/4 transformed-coordinate anti-artifact witnesses.

The aggregate reports minimum nonzero Riemann-component count 8 in Stream A. A raw negative-control witness gave exactly `G_uu=-u/5-1/5` and transverse Laplacian `2u/5+2/5`, with the exact relation `G_uu=-1/2 Laplacian(H)`, so the vacuum PASS is not a trivial zero-return artifact.

Scientific meaning: the already reconstructed all-orders local two-derivative QGR-L1 action admits a nontrivial exact finite-amplitude curved radiative pp-wave family. This is genuinely nonlinear within that action, but remains a **special algebraically structured pp-wave family**. It does not establish generic nonlinear/strong-field stability, quantum unitarity, or physical distinctness from GR in the two-derivative sector.

## Active Iter047 — exact `Weyl^3` curvature-class activation map
Preregistered before implementation in `status/ITERATION_047.md`.

Authority so far:
- preregistration commit `dbd3745ad1082141790502b8423240771112ee03`;
- implementation commit `bb44a0b2721dca861c84e7de55b482cd79bc9b25`;
- frozen aggregate commit `cb018321e7a061e2d82f558c68ed0e14d051ceb2`;
- workflow commit `84280ed3fef58d10e3759e63b5b7277c08dc9497`;
- trigger/head `2c731e9a14c288e6e359c160476bc4bb0e78b801`;
- production run **`34719070003`**.

Frozen matrix: **24 scientific lanes + aggregate**:
- A6: exact harmonic pp-wave/type-N curvature with nonzero Riemann but `W2=W3=0`;
- B6: exact Schwarzschild/Petrov-D activation with frozen targets `W2=48 M^2/r^6`, `W3=96 M^3/r^9` and exact mass/radius scaling;
- C6: exact vacuum Kasner activation with `W2~t^-4`, `W3~t^-6`;
- D6: conformally-flat FLRW controls with nonzero curvature but exact zero Weyl, `W2=W3=0`.

Frozen full-PASS class:
`PASS_SCOPED_EXACT_WEYL3_CURVATURE_CLASS_ACTIVATION_MAP`.

Interpretation lock: Iter047 is a metric-level **operator activation** map only. It does not derive the six-derivative Euler-Lagrange tensor, does not show Schwarzschild/Kasner remain solutions after nonzero `c6`, and does not determine `c6`.

## Current scientific frontier
The linear TT sector (G43–G45) and one exact nonlinear special radiative family (G46) are now closed in scope. The active frontier has moved to the QGR-specific beyond-two-derivative sector. Iter047 asks where `Weyl^3` is actually visible or algebraically blind. If it passes, the next decisive gate should move from invariant activation to the **actual curved-background Euler-Lagrange response of `c6*Weyl^3` with `c6` symbolic**, or to another genuinely generic/non-special curved-background dynamical problem.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- finite panels and exact special families are not global theorems;
- Iter046 is special pp-wave closure, not generic nonlinear stability;
- Iter047 cannot fix `c6` or substitute for six-derivative EOM;
- beta remains a matching/calibration parameter and `beta=1` is not physics;
- `c6` remains unfixed absent independent Weyl-active absolute matching authority;
- G45 does not establish absolute energy positivity or quantum unitarity;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority.
