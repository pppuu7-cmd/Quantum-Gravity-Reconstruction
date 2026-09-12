# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter042`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / NONSTATIC_MAGNETIC_WEYL_COVARIANCE_BRIDGE`
Active roadmap stage: `principal refinement closure -> absolute-scale no-go -> calibration-free Weyl3 manifold -> held-out generalization -> boosted non-static magnetic-Weyl bridge -> independent radiative/magnetic geometry -> absolute matching/validation`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **93%**
- Iter005–Iter041 completion: **100%**
- Iter042 completion: **PREREGISTERED / READY FOR IMPLEMENTATION**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Principal projective refinement / fixed-path-loop blocking: **PASS_SCOPED (G38)**
- Principal compact-domain small-h regularity: **PASS_SCOPED (G38)**
- Finite nonlinear torsion multiplicity: **VERIFIED_SCOPED (G35–G37)**
- Additional physical distant branches under G10B: **NOT SUPPORTED (G37C)**
- Absolute source normalization `beta`: **EXPLICIT MATCHING/CALIBRATION PARAMETER (G39)**
- Current absolute authority rank on `(beta^2,c6)`: **0 (G39)**
- `c6` fixed: **NO**
- Calibration-free static Weyl^3 response manifold: **PASS_SCOPED (G40)**
- Held-out generic off-diagonal static Weyl^3 transfer: **PASS_SCOPED (G41)**
- Non-static / magnetic-Weyl boosted observer covariance: **ACTIVE G42**
- Physical Weyl-active absolute phase target: **NOT DERIVED**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Iter038 terminal
Run `34709394158`, head `ae8f365ea1ad9e92cdeaed8fefa81a9f05e152d9`, aggregate job `103595441181`, artifact `10303065332`, digest `sha256:26bf51ad50a90cc42b8ee92ba997a237df25aa82dc0ffedeb538170d9997a432`.
Classification: `PASS_SCOPED_PRINCIPAL_COMPACT_REFINEMENT_REGULARITY_AND_FINE_TO_COARSE_BLOCKING`.
29/29 PASS; exact h=0 torsion Jacobian rank 24, determinant 11664.

## Iter039 terminal
Run `34709657749`, head `15cedcd3507f0223dc50827a2f72e3d0762ec901`, aggregate job `103596064182`, artifact `10302389728`, digest `sha256:11d4f47b32e269573e491d06d188d1ee90da92a9f5000377876e498d037b23e3`.
Classification: `PASS_SCOPED_INTERNAL_ABSOLUTE_SCALE_NONIDENTIFIABILITY_AND_MINIMAL_CALIBRATION_RANK_DERIVED`.
30/30 PASS; source-scale nullity 1; current rank on `(beta^2,c6)` is 0; two independent absolute matching directions are needed for local rank 2.

## Iter040 terminal
Run `34709914980`, head `b990644250a4df7d29ddec467629c56956fd83e9`, aggregate job `103596975475`, artifact `10302927388`, digest `sha256:898899c85f7c304b9f0032e6138f55dd7dc12339fa07f03728b0f774e1e03fe9`.
Classification: `PASS_SCOPED_CALIBRATION_FREE_WEYL3_RESPONSE_MANIFOLD_ESTABLISHED`.
20/20 PASS. Static weak-tidal response shows cubic amplitude law, H2 cubic-null, rotational recovery and calibration-free H0:H1:H3=`1:3:-1` up to a common convention/c6 factor.

## Iter041 terminal — held-out generalization
Run `34712571244`, head `3c4d96d2658c2bd1aff6565c0f2cbc43595502bf`, aggregate job `103604189849`, artifact `10303324187`, digest `sha256:289bbbbe42b1f089f0c933423b4b026f53aa1b95296d85e823c643bfe0e8f735`.

Classification: `PASS_SCOPED_HELDOUT_WEYL3_GENERALIZATION_AND_PREDICTION_CONTRACT_STRESS`.
All **24/24** preregistered held-out lanes passed with valid controls:
- A 6/6 fixed-scale generic off-diagonal shape transfer;
- B 6/6 refinement transfer;
- C 4/4 amplitude law;
- D 4/4 rotated cubic-null falsifiers;
- E 4/4 held-out rotation covariance.

Strongest frozen diagnostics:
- maximum fixed-scale held-out q error: `2.769683280777905e-04`;
- maximum finest refinement q error: `2.7696835073143515e-04`;
- maximum finest held-out rotation discrepancy: `2.9473460146349044e-05`;
- maximum finest rotated-null normalized cubic: `1.8275144691009777e-05`;
- Weyl norm amplitude slopes `[0.999941304636997,1.0000103050279203]`;
- Weyl^3 amplitude slopes `[2.9997228598916252,3.0000742431607224]`.

Interpretation: the G40 calibration-free response law transfers prospectively to generic off-diagonal held-out static tidal tensors and new null/rotation controls. The present weak static electric-tidal family is now saturated for this research question; further nearby Hessian scans are not the preferred next use of compute.

Record: `results/ITER041_HELDOUT_WEYL3_GENERALIZATION.md`.

## Active gate — Iter042
`QGR-ITER042-NONSTATIC-MAGNETIC-WEYL-LORENTZ-COVARIANCE-BRIDGE`.

Preregistered before implementation in `status/ITERATION_042.md`.
It applies global Lorentz boosts to the already-authorized weak static vacuum tidal geometry, creating a time-dependent/off-diagonal coordinate metric and an observer-dependent nonzero magnetic Weyl component without adding fields. Frozen scalar W2/W3 invariants must recover boost covariance under refinement.

Frozen production plan: **24 scientific lanes + aggregate**, fail-fast disabled:
- A 6 magnetic-Weyl emergence lanes;
- B 6 scalar Lorentz-invariance/refinement lanes;
- C 4 boost-reversal magnetic-parity lanes;
- D 4 boosted amplitude-law lanes;
- E 4 small-velocity magnetic-response lanes.

Full PASS classification: `PASS_SCOPED_NONSTATIC_MAGNETIC_WEYL_LORENTZ_COVARIANCE_BRIDGE`.
A full PASS is only a covariance bridge: the subsequent gate must use a genuinely independent time-dependent/radiative or magnetic-Weyl geometry, not more boosted copies of the same static spacetime.

## Strongest positive result
Within the frozen same-field weak static tidal family, QGR now has principal refinement authority plus a calibration-free Weyl^3 response law that has survived prospective held-out off-diagonal shapes, nulls and rotations.

## Strongest blocker
`NONSTATIC_MAGNETIC_WEYL_COVARIANCE_THEN_INDEPENDENT_RADIATIVE_GEOMETRY_AND_ABSOLUTE_MATCHING_AUTHORITY`.

## Claim locks
- theory established `0%`;
- beta is an explicit matching/calibration parameter under G39; `beta=1` is not physics;
- c6 remains unfixed;
- a boosted static spacetime is not a new dynamical solution;
- finite numerical covariance/refinement evidence is not a global theorem;
- G40/G41 static tidal authority is scoped, not arbitrary spacetime;
- G35–G37 distant roots do not authorize physical branch weights under G10B;
- no experimental confirmation;
- no KMQGB `NEW_REQUIRED` authorization.
