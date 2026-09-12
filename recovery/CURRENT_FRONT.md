# QGR Current Research Front

Updated: 2026-09-12
Primary active iteration: `Iter046`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / EXACT_NONLINEAR_CURVED_RADIATIVE_SECTOR`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **95%** — internal construction-roadmap readiness only, not probability of correctness and not fraction of quantum gravity solved.
- Iter005–Iter045 completion: **100%**
- Iter046: **PREREGISTERED / IMPLEMENTED / PRODUCTION QUEUED**, 34 scientific lanes + aggregate.
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- `beta`: explicit matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6`: unfixed.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Terminal G44 — end-to-end QGR-L1 linearized TT radiation
Durable record: `results/ITER044_QGR_L1_END_TO_END_LINEARIZED_TT_RADIATION.md`.

Authoritative production:
- run `34716363645`;
- head `e27602b367acffbc9473df95607278042fce5e02`;
- aggregate job `103616604387`;
- summary artifact `10305230612`;
- digest `sha256:48e15c3872ae6963582b4cada787b5c54e74e6654f1de6565d5c3b373062fadb`.

Classification: `PASS_SCOPED_QGR_L1_END_TO_END_LINEARIZED_TT_RADIATION_CONTRACT`.

All **48/48** frozen scientific lanes passed with valid controls:
- A 24/24 QGR-L1 dynamics -> TT curvature;
- B 12/12 off-shell dispersion falsification;
- C 8/8 gauge robustness;
- D 4/4 flat-background `c6 Weyl^3` quadratic decoupling.

Key aggregate metrics:
- max curvature bridge error `5.340208237110733e-16`;
- max TT QGR residual `2.507048651523522e-16`;
- max gauge QGR residual `3.829588338046111e-17`;
- minimum tested off-shell residual `0.017486179466437605`;
- max shifted-curvature gauge error `3.769148233304873e-14`;
- tested `Weyl^3` oddness and centered quadratic variation exactly zero in Stream D.

Scientific meaning: within the frozen flat-background linearized domain, the internally reconstructed QGR-L1 kernel generates the massless two-mode TT sector and bridges to the independently validated G43 curvature without inserting G43 curvature as dynamics. This is **not** a generic nonlinear/curved-background radiation theorem.

## Terminal G45 — relative TT residue/signature
Durable record: `results/ITER045_QGR_L1_RELATIVE_TT_RESIDUE_SIGNATURE.md`.

Authoritative production:
- run `34716924227`;
- head `cad39c37bfdc56e8b66d0d45e907eb2a33d18d09`;
- aggregate job `103616970603`;
- summary artifact `10305091648`;
- digest `sha256:3a80f6865140410aadc521d6b5e7eb8f612c30ff4b2c062656632513faff56d4`.

Classification: `PASS_SCOPED_QGR_L1_TWO_POLARIZATION_RELATIVE_RESIDUE_DEGENERACY`.
All **18/18** frozen held-out lanes passed with valid controls.

Key metrics:
- max polarization mixing `5.775329183325975e-16`;
- max plus/cross relative coefficient difference `1.4432899320127063e-15`;
- max coefficient spreads around `5.1e-15`;
- minimum relative sign product `0.24999999999999853 > 0`.

The workflow-definition push accidentally generated run `34716911042`; it remains `+0 / NON_AUTHORITATIVE_DUPLICATE` and is never combined with the authoritative evidence.

Interpretation lock: G45 establishes relative two-polarization degeneracy/sign only. It does not fix the overall action sign, absolute energy positivity or quantum unitarity.

## Why G46 is new rather than a repeat of Iter005-G3
Iter005-G3 already proved scoped local weak-background **principal-symbol** stability: deformed Lorentzian cone, four gauge directions and exactly two physical high-frequency modes on tested regular weak backgrounds.

Therefore G46 does not rerun that result. It asks whether the already reconstructed **all-orders** local two-derivative QGR-L1 action admits a nontrivial **exact curved finite-amplitude radiative vacuum sector** without flat-background linearization.

## Active G46 — exact nonlinear pp-wave radiative sector
Prospectively preregistered before implementation in `status/ITERATION_046.md`.

Authority/provenance:
- preregistration commit `125d030e90ac86697710c9ed0cee432c5ff54596`;
- lane implementation `bd7ea711e8f1f98e5727321f77bc90841510b440`;
- frozen aggregate `d625cb2f636ef6781513c30600572156b7c806d3`;
- path-triggered workflow `0a4c93cae719379ca4b38c10047fc6a41e92ed0b`;
- production trigger/head `37ff955a57b6822d800b6755282a6bc557c3a0e2`;
- run **`34718135187`**.

Frozen production matrix: **34 scientific lanes + aggregate**:
- A: 12 exact finite-amplitude harmonic pp-wave vacuum lanes;
- B: 6 deliberately non-harmonic falsification controls;
- C: 6 held-out plus/cross superposition lanes;
- D: 6 exact finite-amplitude full-Riemann scaling lanes;
- E: 4 independent constant-linear coordinate-chart anti-artifact lanes.

The production implementation reconstructs inverse metric, Levi-Civita connection, Riemann, Ricci, scalar curvature and the Euler-Lagrange/Einstein tensor symbolically from the already fixed all-orders two-derivative action. It does not use a pre-solved pp-wave field equation as the solver.

Frozen full-PASS classification:
`PASS_SCOPED_QGR_L1_EXACT_FINITE_AMPLITUDE_NONLINEAR_PPWAVE_RADIATIVE_SECTOR`.

Negative-control invalidity has its own frozen class `CONTROL_INVALID_NONLINEAR_PPWAVE_GATE`; any other scientific failure gives `PARTIAL_OR_FAIL_QGR_L1_NONLINEAR_PPWAVE_RADIATIVE_SECTOR`. No profile/threshold retuning is allowed after trigger.

`c6` is deliberately excluded from G46 dynamics because its coefficient remains unfixed. A later independent curved-radiation correction gate may keep `c6` symbolic and ask whether the higher-derivative operator vanishes, deforms or obstructs this special exact sector.

## Strongest positive result
The programme now has independent radiative geometry (G43), an end-to-end internally reconstructed linearized QGR-L1 TT dynamical contract (G44), and a held-out relative two-polarization residue/signature closure (G45).

## Strongest blocker
The frontier has moved to exact/generic nonlinear curved-background dynamics, then higher-derivative curved-radiation effects, quantum amplitude/measure closure, and absolute matching (`beta`, `c6`). G46 attacks the first of these only on a special exact radiative family.

## Claim locks
- theory established = `0%`;
- no experimental confirmation;
- G44 is linearized/scoped, not a nonlinear/global theorem;
- even a full G46 PASS is a special pp-wave family, not generic nonlinear stability;
- finite computational panels are not global theorems;
- beta remains matching/calibration parameter and `beta=1` is not physics;
- c6 remains unfixed without a genuine independent Weyl-active absolute matching datum;
- G45 does not establish absolute energy positivity or quantum unitarity;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority.
