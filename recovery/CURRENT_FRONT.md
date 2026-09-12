# QGR Current Research Front

Updated: 2026-09-12
Primary active iteration: `Iter044`
Parallel independent audit: `Iter045`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / END_TO_END_LINEARIZED_RADIATIVE_DYNAMICS + RELATIVE_TT_RESIDUE_AUDIT`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **94%** — unchanged; launching more compute does not earn rubric credit.
- Iter005–Iter043 completion: **100%**
- Iter044: **PRODUCTION ACTIVE**, 48 scientific lanes + aggregate.
- Iter045: **PREREGISTERED / IMPLEMENTED / PRODUCTION QUEUED**, 18 scientific lanes + aggregate.
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- `beta`: explicit matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6`: unfixed.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Terminal G43
Run `34715559793`, head `79b7325179aab34e83bbbc998152b81398221ef5`, aggregate job `103613094190`, artifact `10303724918`, digest `sha256:bd74de5bd2b0b17a9a0e043954f5f97e8fc964e1e64da1bb3d137b01f0286b83`.

Classification: `PASS_SCOPED_INDEPENDENT_TT_RADIATIVE_WEYL_COVARIANCE`, **24/24** frozen lanes with valid controls. This is independent radiative tensor/observable geometry, not by itself QGR dynamical derivation.

## Primary active G44 — end-to-end QGR-L1 linearized radiative dynamics
Preregistered before production in `status/ITERATION_044.md`.
Production run: **`34716363645`**, head `e27602b367acffbc9473df95607278042fce5e02`.
Frozen matrix:
- A: 24 QGR-L1 dynamics -> TT-curvature lanes;
- B: 12 off-shell dispersion falsification lanes;
- C: 8 gauge end-to-end robustness lanes;
- D: 4 flat-background `c6 Weyl^3` quadratic-decoupling lanes;
- aggregate after all prerequisites.

Frozen full-PASS class: `PASS_SCOPED_QGR_L1_END_TO_END_LINEARIZED_TT_RADIATION_CONTRACT`.

### Non-terminal evidence observed so far
These are early lane-level observations only; they do not authorize terminal classification.
- A0: Hessian rank 4, gauge rank 4, TT QGR residual `2.8864167148346014e-17`, curvature bridge error `5.206173234540566e-16`.
- B0: scientific lane PASS. At shell ratio `r=1`, Hessian rank 4 and TT residual `9.041084098513864e-17`; at `r=0.8,0.9,1.1,1.2` rank returns to 6, with unique residual minimum at the null shell. Minimum tested off-shell residual `0.017486179466437605`.
- C3: pure-gauge QGR residual `8.96229702303301e-18`, shifted residual `1.673496586579566e-17`, curvature invariance within frozen tolerance.
- D1: exact tested cubic scaling `W3(2)/W3(1)=8`, exact oddness and zero centered second variation.
- Additional completed-success matrix jobs have appeared, but green CI is not promoted to scientific PASS without reading the frozen lane output or terminal aggregate.

G44 remains nonterminal and is the primary blocker.

## Parallel independent G45 — relative two-polarization residue/signature
Scientific object preregistered **before implementation** in `status/ITERATION_045.md`, preregistration commit `d08b131bc94007460b9ea517460f4d57e432fc16`.
Implementation commits:
- `a483681222a93eac73d9ce92365b19bbf90c9969` — lane code;
- `6d368ac30bdeff1bfa1671cb3f15c57fe53e02a9` — frozen aggregate;
- `a4f03fb58105042a775f7940a33d628e98782901` — workflow.
Explicit trigger commit: `cad39c37bfdc56e8b66d0d45e907eb2a33d18d09`.

Authoritative production run: **`34716924227`**, 18 frozen lanes (6 held-out generic directions × 3 wave-number scales) + aggregate. At the latest check, all 18 scientific lanes are queued because the runner pool is occupied by earlier useful work; no third heavy stream should be launched merely to create load.

The workflow-definition push also generated accidental duplicate run `34716911042`. Authority lock `status/ITERATION_045_RUN_AUTHORITY.md` (commit `3562b3b93a46f6dfd4dfa84a5e59375129aaaba2`) marks it `+0 / NON_AUTHORITATIVE_DUPLICATE`; its evidence must never be combined with the authoritative run.

Frozen full-PASS class: `PASS_SCOPED_QGR_L1_TWO_POLARIZATION_RELATIVE_RESIDUE_DEGENERACY`.

Interpretation lock: even a full G45 PASS establishes only same-sign/equal **relative** TT pole/kinetic coefficients and absence of polarization mixing on the frozen panel. It does **not** fix the overall action sign, prove absolute energy positivity, prove quantum unitarity, or establish nonlinear stability.

## Strongest positive result
G43 independently validates the TT radiative observable layer. G44 is actively testing whether the internally reconstructed QGR-L1 dynamical kernel itself produces that massless TT sector. Early A/B/C/D lanes are consistent with that contract, including an explicit off-shell rank/residual falsification lane.

## Strongest blocker
`QGR_L1_END_TO_END_LINEARIZED_RADIATIVE_DYNAMICAL_CLOSURE` (G44 terminal aggregate). After that, the highest-value dependent frontier is genuinely nonlinear/curved-background radiation rather than another duplicate linear TT panel. Quantum amplitude/measure closure and absolute matching (`beta`, `c6`) remain separate blockers.

## Claim locks
- theory established = `0%`;
- no experimental confirmation;
- G43 alone is not QGR dynamical derivation;
- even G44 PASS would be scoped linearized closure, not a nonlinear/global radiation theorem;
- finite numerical panels are not global theorems;
- beta remains matching/calibration parameter and `beta=1` is not physics;
- c6 remains unfixed without a genuine independent Weyl-active absolute matching datum;
- G45 cannot establish absolute energy positivity or quantum unitarity;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority.
