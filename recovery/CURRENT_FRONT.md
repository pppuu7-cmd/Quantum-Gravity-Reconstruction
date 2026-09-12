# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter043`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / INDEPENDENT RADIATIVE GEOMETRY`
Active roadmap stage: `principal refinement closure -> absolute-scale no-go -> calibration-free Weyl3 manifold -> held-out generalization -> boosted covariance stress -> frame-completion correction -> independent radiative geometry`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **94%**
- Iter005–Iter042R completion: **100%**
- Iter043: **PREREGISTERED / IMPLEMENTED / PRODUCTION QUEUED**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Principal projective refinement / fixed-path-loop blocking: **PASS_SCOPED (G38)**
- Absolute source normalization `beta`: **EXPLICIT MATCHING/CALIBRATION PARAMETER (G39)**; `beta=1` not authorized as physics
- `c6` fixed: **NO**
- Calibration-free static Weyl^3 response manifold: **PASS_SCOPED (G40)**
- Held-out generic off-diagonal static Weyl^3 transfer: **PASS_SCOPED (G41)**
- Original boosted G42: **PARTIAL**, with scalar-covariance Stream B 0/6 while A/C/D/E passed
- G42R frame completion: **PASS_SCOPED 24/24**, localizing the G42 scalar defect to mixed internal/coordinate index frames on the frozen family
- Independent radiative geometry: **ACTIVE G43**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Terminal Iter042 — original frozen boosted gate
Head `b6e1c31c961f2536f10e3f9480053b2a62138253`; run `34712954629`; aggregate job `103606707505`; artifact `10304692021`; digest `sha256:c762dbe4532ec9adca18043c42e2d9a8768f85c7c2cec44c0a00fc359b351844`.
Classification: `PARTIAL_SCOPED_NONSTATIC_MAGNETIC_WEYL_COVARIANCE`.
All 24 lanes present and controls valid. Passes: A 6/6, B 0/6, C 4/4, D 4/4, E 4/4. Maximum finest W2 boost discrepancy `0.032577275796710214`; W3 `0.14757516443418453`. Preserve this as the discovery record; it is not retroactively rewritten by G42R.

## Terminal Iter042R — corrective frame-completion diagnostic
Preregistration `1058f1113987c826635bab898431b0fb906f0a89`; head `650a7424d0377388619ca975496c12edf702ddfd`; run `34713234061`; aggregate job `103610525399`; artifact `10303868886`; digest `sha256:8790997c6ad28eb68d8342d0092d2b6fc5c2f20dcf567819463fe05cd7277f56`.
Classification: `PASS_SCOPED_G42_COVARIANCE_DEFECT_ATTRIBUTED_TO_MIXED_FRAME_RECONSTRUCTION_AND_FRAME_COMPLETION_VALIDATED`.
All 24 lanes pass: A 8/8, B 6/6, C 4/4, D 6/6. Exact all-index Lorentz tests show maximum W2 relative change `4.0759329624925397e-16`, W3 `5.365683119828423e-15`. Frame-completed maximum finest discrepancies are W2 `4.216879646694534e-05`, W3 `6.326024551781252e-05`; the original mixed-frame W3 discrepancy reached `0.14757516443312207`.
Scientific meaning is scoped: on the frozen tested geometries the failure came from mixing an internal first curvature index-pair with coordinate last-pair indices. This closes that implementation/observable blocker, not global QGR Lorentz covariance.

Durable terminal note: `results/ITER042_042R_TERMINAL.md`.

## Active Iter043 — independent analytic TT radiative geometry
Preregistered before implementation in `status/ITERATION_043.md` at commit `25e60cb2cbb0f7f05fcb5a993ec61450661211fa`.
Implementation `code/qgr_iter043_tt_radiative.py`; aggregate `code/qgr_iter043_aggregate.py`; workflow `qgr-iter043-tt-radiative`.
Trigger/head: `79b7325179aab34e83bbbc998152b81398221ef5`.
Production run: `34715559793`.
Frozen matrix: 24 lanes = 3 propagation directions x 4 polarization mixtures x 2 phases, with a held boost panel.

Scientific object: analytic linearized TT vacuum plane-wave Riemann/Weyl tensor, independent of the G40–G42 static Hessian family. Frozen controls require TT transversality/tracelessness, vacuum Ricci/scalar nullity, Weyl reconstruction, Lorentz-matrix validity. Scientific tests require all-index W2/W3 covariance under boost, nonzero electric/magnetic Weyl parts, E/B radiative balance, and type-N scalar null relations.

Possible aggregate classes are frozen as `PASS_SCOPED_INDEPENDENT_TT_RADIATIVE_WEYL_COVARIANCE`, `PARTIAL_SCOPED_TT_RADIATIVE_WEYL_COVARIANCE`, `FAIL_SCOPED_TT_RADIATIVE_WEYL_COVARIANCE`, or `ITER043_CONTROL_OR_IMPLEMENTATION_INVALID`.

## Current decision lock
Do not call an Iter043 PASS an end-to-end derivation of gravitational radiation from QGR dynamics. It is a held-out tensor/observable reconstruction gate. Only after terminal interpretation may the next gate target a genuine QGR dynamical/radiative prediction contract.

## Strongest positive result
G42R closes the concrete mixed-frame observable-reconstruction blocker with 24/24 preregistered passes while preserving the original G42 negative Stream-B record.

## Strongest blocker
`INDEPENDENT_RADIATIVE_GEOMETRY_HELDOUT_VALIDATION`, followed by the still-unclosed end-to-end dynamical prediction contract and absolute calibration (`beta`, `c6`).

## Claim locks
- theory established `0%`;
- finite/local numerical scans are not global theorems;
- beta remains explicit matching/calibration parameter and `beta=1` is not physics;
- c6 remains unfixed without a genuine independent Weyl-active absolute matching datum;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority;
- no experimental confirmation.
