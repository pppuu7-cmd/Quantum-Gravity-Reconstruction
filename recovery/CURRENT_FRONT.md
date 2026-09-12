# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter044`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / END_TO_END_LINEARIZED_RADIATIVE_DYNAMICS`
Active roadmap stage: `principal refinement closure -> absolute-scale no-go -> calibration-free Weyl3 manifold -> held-out generalization -> boosted covariance stress -> frame completion -> independent TT geometry -> QGR-L1 dynamical TT contract`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **94%**
- Iter005–Iter043 completion: **100%**
- Iter044: **PRODUCTION ACTIVE**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Principal projective refinement / fixed-path-loop blocking: **PASS_SCOPED (G38)**
- Absolute source normalization `beta`: **EXPLICIT MATCHING/CALIBRATION PARAMETER (G39)**; `beta=1` not authorized as physics
- `c6` fixed: **NO**
- Calibration-free static Weyl^3 response manifold: **PASS_SCOPED (G40)**
- Held-out generic off-diagonal static Weyl^3 transfer: **PASS_SCOPED (G41)**
- Original boosted G42: **PARTIAL**, preserving scalar-covariance Stream-B negative result
- G42R frame completion: **PASS_SCOPED 24/24**
- Independent TT radiative tensor/observable geometry: **PASS_SCOPED 24/24 (G43)**
- End-to-end QGR-L1 dynamical TT radiation contract: **ACTIVE G44**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Terminal G42 / G42R boundary
G42 head `b6e1c31c961f2536f10e3f9480053b2a62138253`, run `34712954629`, aggregate job `103606707505`, artifact `10304692021`, digest `sha256:c762dbe4532ec9adca18043c42e2d9a8768f85c7c2cec44c0a00fc359b351844`.
Classification: `PARTIAL_SCOPED_NONSTATIC_MAGNETIC_WEYL_COVARIANCE`.

G42R head `650a7424d0377388619ca975496c12edf702ddfd`, run `34713234061`, aggregate job `103610525399`, artifact `10303868886`, digest `sha256:8790997c6ad28eb68d8342d0092d2b6fc5c2f20dcf567819463fe05cd7277f56`.
Classification: `PASS_SCOPED_G42_COVARIANCE_DEFECT_ATTRIBUTED_TO_MIXED_FRAME_RECONSTRUCTION_AND_FRAME_COMPLETION_VALIDATED`.
Durable record: `results/ITER042_042R_TERMINAL.md`. The original G42 Stream-B failure remains a preserved discovery record.

## Terminal G43 — independent analytic TT radiative geometry
Preregistered in `status/ITERATION_043.md` before production.

Authoritative production:
- head `79b7325179aab34e83bbbc998152b81398221ef5`;
- run `34715559793`;
- aggregate job `103613094190`;
- artifact `10303724918`;
- digest `sha256:bd74de5bd2b0b17a9a0e043954f5f97e8fc964e1e64da1bb3d137b01f0286b83`.

Classification: `PASS_SCOPED_INDEPENDENT_TT_RADIATIVE_WEYL_COVARIANCE`.
All **24/24** frozen lanes passed with valid controls. Max Lorentz error `4.681459141485685e-16`, W2 covariance error `2.0872426177969475e-16`, W3 covariance error `2.9099380740141584e-17`, E/B balance error `2.220446049250313e-16`, type-N W3 null `7.972433079490845e-19`.
Scientific meaning: corrected observable layer reproduces and Lorentz-transports an independent held-out linearized TT vacuum geometry. It is not by itself a derivation of radiation from QGR equations.
Durable record: `results/ITER043_TT_RADIATIVE_WEYL_COVARIANCE.md`.

## Existing dynamical authority permitting G44
The next gate does not insert Einstein equations by hand. Existing repository authority already gives:
- Iter004: exact reconstruction/selection of QGR-L1 from the complete S4-invariant quadratic two-derivative Noether family, exactly two non-gauge null modes on the incidence cone, no allowed S4-invariant onsite mass term;
- Iter005: exact cubic/quartic Noether continuation under the independently derived relational pullback law;
- Iter007: unique all-orders local metric-only at-most-two-derivative action within its scoped domain, with Einstein-Hilbert identification only a posteriori.

## Active G44 — end-to-end QGR-L1 linearized radiative dynamics
Preregistered before implementation in `status/ITERATION_044.md`.
Production implementation: `code/qgr_iter044_end_to_end_radiative.py` plus frozen aggregate `code/qgr_iter044_aggregate.py`.
Workflow: `qgr-iter044-end-to-end-radiative`.
Production head/trigger: `e27602b367acffbc9473df95607278042fce5e02`.
Production run: `34716363645`.

Frozen production matrix: **48 scientific lanes + aggregate**:
- A: 24 dynamics -> TT-curvature lanes;
- B: 12 off-shell dispersion falsification lanes;
- C: 8 gauge end-to-end robustness lanes;
- D: 4 flat-background `c6 Weyl^3` linearization/decoupling lanes.
Fail-fast is disabled; max useful matrix parallelism target is 24.

Early non-terminal diagnostics only, not aggregate authority:
- A0 passed frozen lane criteria: Hessian rank 4, gauge rank 4, TT QGR residual `2.8864167148346014e-17`, curvature bridge error `5.206173234540566e-16`;
- C3 passed: pure-gauge QGR residual `8.96229702303301e-18`, shifted QGR residual `1.673496586579566e-17`, curvature errors below `4e-14`;
- D1 passed: exact cubic scaling `W3(2)/W3(1)=8`, exact oddness and zero centered second variation in the tested arithmetic.
These partial lanes do not authorize terminal classification.

Frozen full-PASS class: `PASS_SCOPED_QGR_L1_END_TO_END_LINEARIZED_TT_RADIATION_CONTRACT`.
No threshold may be retuned after production.

## Strongest positive result
The programme now has independently held-out TT radiative observable geometry (G43), internally reconstructed QGR-L1 dynamics, and an active end-to-end gate joining the two chains without inserting the G43 curvature as a dynamical input.

## Strongest blocker
`QGR_L1_END_TO_END_LINEARIZED_RADIATIVE_DYNAMICAL_CLOSURE`, followed by genuinely nonlinear/higher-background radiation, quantum amplitudes/measure closure, and absolute matching/calibration (`beta`, `c6`).

## Claim locks
- theory established `0%`;
- G43 is tensor/observable validation, not QGR dynamical derivation;
- even G44 PASS is scoped linearized end-to-end closure, not a nonlinear/global radiation theorem;
- finite numerical panels are not global theorems;
- beta remains explicit matching/calibration parameter and `beta=1` is not physics;
- c6 remains unfixed without a genuine independent Weyl-active absolute matching datum;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority;
- no experimental confirmation.
