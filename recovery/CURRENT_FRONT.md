# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter041`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / HELDOUT_WEYL3_GENERALIZATION`
Active roadmap stage: `principal refinement closure -> absolute-scale no-go -> calibration-free Weyl3 manifold -> held-out generalization -> genuinely new dynamical/magnetic Weyl sector -> independent matching/validation`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **93%**
- Iter005–Iter040 completion: **100%**
- Iter041 completion: **PREREGISTERED / IMPLEMENTED / AWAITING PRODUCTION TRIGGER**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Projective refinement-limit action mechanism: **PASS_SCOPED on frozen principal smooth compact realization after G38**
- Principal identity/refinement-connected connection: **PASS_SCOPED / G10B physical branch rule**
- Principal compact-domain small-h uniform regularity: **PASS_SCOPED (G38)**
- Actual principal fixed-path/loop fine-to-coarse blocking: **PASS_SCOPED (G38)**
- Finite nonlinear torsion equation multiplicity: **VERIFIED_SCOPED (G35–G37)**
- Additional physical connection branches from strongest distant roots: **NOT SUPPORTED UNDER FROZEN G10B (G37C)**
- Absolute source normalization `beta`: **EXPLICIT MATCHING/CALIBRATION PARAMETER UNDER CURRENT AUTHORITY (G39)**
- Current absolute authority rank on `(beta^2,c6)`: **0 (G39)**
- Minimal local rank for `(beta^2,c6)` identification: **2 independent absolute directions (G39)**
- Physical Weyl-active same-realization finite absolute phase target: **NOT DERIVED**
- Calibration-free Weyl^3 response manifold: **PASS_SCOPED (G40)**
- Held-out/off-diagonal Weyl^3 transfer: **ACTIVE G41**
- `c6` fixed: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Iter038 terminal — principal refinement regularity and actual blocking
Authoritative run `34709394158`, head `ae8f365ea1ad9e92cdeaed8fefa81a9f05e152d9`, aggregate job `103595441181`, artifact `10303065332`, digest `sha256:26bf51ad50a90cc42b8ee92ba997a237df25aa82dc0ffedeb538170d9997a432`.

Classification: `PASS_SCOPED_PRINCIPAL_COMPACT_REFINEMENT_REGULARITY_AND_FINE_TO_COARSE_BLOCKING`.

All **29/29** frozen scientific lanes passed. Exact common scaled-residual h=0 torsion Jacobian has rank **24**, determinant **11664**, numerical minimum singular value `0.3742889790499052`. This supplies scoped small-h IFT/refinement authority on the frozen smooth compact principal realization, not arbitrary field space.

Record: `results/ITER038_PRINCIPAL_REFINEMENT_REGULARITY_AND_BLOCKING.md`.

## Iter039 terminal — absolute source/action-phase identifiability
Authoritative run `34709657749`, head `15cedcd3507f0223dc50827a2f72e3d0762ec901`, aggregate job `103596064182`, artifact `10302389728`, digest `sha256:11d4f47b32e269573e491d06d188d1ee90da92a9f5000377876e498d037b23e3`.

All **30/30** authority lanes passed.
Classification: `PASS_SCOPED_INTERNAL_ABSOLUTE_SCALE_NONIDENTIFIABILITY_AND_MINIMAL_CALIBRATION_RANK_DERIVED`.

Scoped conclusions:
- source-scale nullity = **1**;
- current absolute identifying rank on `(u=beta^2,c6)` = **0**;
- G38 refinement/blocking is beta-blind in the frozen audit;
- one genuine absolute datum gives rank 1; independent conformal + Weyl-active absolute directions give rank 2.

Decision: beta is an explicit matching/calibration parameter under current authority, not an internally missing numerical root. `beta=1` is not physics. `c6` remains unfixed until a genuine independent Weyl-active absolute phase/matching equation exists.

Record: `results/ITER039_ABSOLUTE_SCALE_IDENTIFIABILITY.md`.

## Iter040 terminal — calibration-free Weyl^3 response manifold
Authoritative run `34709914980`, head `b990644250a4df7d29ddec467629c56956fd83e9`, aggregate job `103596975475`, artifact `10302927388`, digest `sha256:898899c85f7c304b9f0032e6138f55dd7dc12339fa07f03728b0f774e1e03fe9`.

All **20/20** preregistered scientific lanes passed.
Classification: `PASS_SCOPED_CALIBRATION_FREE_WEYL3_RESPONSE_MANIFOLD_ESTABLISHED`.

Frozen strongest diagnostics:
- H2 finest normalized cubic null residual `1.875882416525863e-05` with nonzero Weyl curvature;
- maximum finest rotation discrepancy `5.168073699081922e-08`;
- q-spread for `q=W3/tr(H^3)` across nonzero training shapes drops from `9.853846896674696e-04` at h=0.10 to `2.453977185447458e-04` at h=0.05;
- Weyl norm amplitude slopes `[0.9998691592541441,1.000002740132653]`;
- Weyl^3 amplitude slopes `[2.999514418717107,3.0000081778357783]`;
- calibration-free nonzero tidal shape ratio `H0:H1:H3 = 1:3:-1` up to one common convention/c6 factor.

Scientific scope: a parameterized/falsifiable response-shape manifold inside the same-field weak static tidal family. It does not fix the absolute phase amplitude, beta or c6 and is not an arbitrary-spacetime theorem.

Record: `results/ITER040_CALIBRATION_FREE_WEYL3_RESPONSE_MANIFOLD.md`.

## Active gate — Iter041
`QGR-ITER041-HELDOUT-WEYL3-GENERALIZATION-AND-PREDICTION-CONTRACT-STRESS`.

Preregistered before implementation in `status/ITERATION_041.md`.
Implementation: `code/qgr_iter041_heldout_weyl.py`.
Aggregate: `code/qgr_iter041_aggregate.py`.
Workflow: `qgr-iter041-heldout-weyl`.

Frozen matrix: **24 scientific lanes** + aggregate, fail-fast disabled:
- A: 6 generic off-diagonal trace-free held-out Hessians, fixed-scale q transfer;
- B: same 6 shapes under refinement transfer;
- C: 4 held-out amplitude-law lanes;
- D: 4 new rotated cubic-null falsifier profiles;
- E: 4 new rotation-covariance lanes for an off-diagonal held-out profile.

Full PASS classification is `PASS_SCOPED_HELDOUT_WEYL3_GENERALIZATION_AND_PREDICTION_CONTRACT_STRESS`.
No held-out shape or frozen threshold may be removed/relaxed after production.

If full PASS occurs, do not spend the next gate densifying static electric-tidal scans. Move to a genuinely new dynamical/magnetic-Weyl or non-static covariance sector, preserving beta/c6 as external matching directions.

## Strongest positive result
QGR now has, within a scoped same-field weak static tidal realization, both a mathematically supported principal refinement mechanism and a calibration-free Weyl^3 response law with signs, nulls, cubic amplitude scaling, tidal-shape ratios and rotational recovery. G41 asks whether that response law transfers prospectively out of sample.

## Strongest blocker
`OUT_OF_SAMPLE_WEYL3_TRANSFER_THEN_GENUINELY_NEW_DYNAMICAL_MAGNETIC_WEYL_SECTOR_AND_ABSOLUTE_MATCHING_AUTHORITY`.

## Claim locks
- theory established `0%`;
- beta is an explicit matching/calibration parameter under current G39 authority; `beta=1` is not physics;
- c6 remains unfixed;
- response-kernel ratios/nulls are not absolute quantum phases;
- G38 authority remains scoped to the frozen smooth compact principal realization;
- G40/G41 weak static tidal evidence is not arbitrary-spacetime authority;
- G35–G37 distant algebraic roots do not authorize physical branch weights under current G10B evidence;
- no experimental confirmation;
- no KMQGB `NEW_REQUIRED` authorization.
