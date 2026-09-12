# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter042 + Iter042R corrective audit`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / BOOSTED COVARIANCE DIAGNOSTIC`
Active roadmap stage: `principal refinement closure -> absolute-scale no-go -> calibration-free Weyl3 manifold -> held-out generalization -> boosted covariance stress -> frame-completion diagnostic -> independent radiative geometry only if covariance diagnostic resolves`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **93%**
- Iter005–Iter041 completion: **100%**
- Iter042: **PRODUCTION ACTIVE; at least one valid frozen scientific failure observed in scalar-covariance Stream B**
- Iter042R: **PREREGISTERED / IMPLEMENTED / PRODUCTION QUEUED**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Principal projective refinement / fixed-path-loop blocking: **PASS_SCOPED (G38)**
- Principal compact-domain small-h regularity: **PASS_SCOPED (G38)**
- Absolute source normalization `beta`: **EXPLICIT MATCHING/CALIBRATION PARAMETER (G39)**
- Current absolute authority rank on `(beta^2,c6)`: **0 (G39)**
- `c6` fixed: **NO**
- Calibration-free static Weyl^3 response manifold: **PASS_SCOPED (G40)**
- Held-out generic off-diagonal static Weyl^3 transfer: **PASS_SCOPED (G41)**
- Boosted magnetic-Weyl emergence/amplitude/parity: **PARTIAL POSITIVE EVIDENCE IN ACTIVE G42**
- Boosted scalar W2/W3 covariance: **NOT CLOSED; G42-B3 valid scientific failure observed**
- Physical Weyl-active absolute phase target: **NOT DERIVED**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Stable terminal results
### Iter038
Run `34709394158`, aggregate job `103595441181`, artifact `10303065332`, digest `sha256:26bf51ad50a90cc42b8ee92ba997a237df25aa82dc0ffedeb538170d9997a432`.
Classification: `PASS_SCOPED_PRINCIPAL_COMPACT_REFINEMENT_REGULARITY_AND_FINE_TO_COARSE_BLOCKING`; 29/29 PASS; exact h=0 torsion Jacobian rank 24, determinant 11664.

### Iter039
Run `34709657749`, aggregate job `103596064182`, artifact `10302389728`, digest `sha256:11d4f47b32e269573e491d06d188d1ee90da92a9f5000377876e498d037b23e3`.
Classification: `PASS_SCOPED_INTERNAL_ABSOLUTE_SCALE_NONIDENTIFIABILITY_AND_MINIMAL_CALIBRATION_RANK_DERIVED`; 30/30 PASS; source-scale nullity 1; current absolute rank on `(beta^2,c6)` is 0.

### Iter040
Run `34709914980`, aggregate job `103596975475`, artifact `10302927388`, digest `sha256:898899c85f7c304b9f0032e6138f55dd7dc12339fa07f03728b0f774e1e03fe9`.
Classification: `PASS_SCOPED_CALIBRATION_FREE_WEYL3_RESPONSE_MANIFOLD_ESTABLISHED`; 20/20 PASS.

### Iter041
Run `34712571244`, aggregate job `103604189849`, artifact `10303324187`, digest `sha256:289bbbbe42b1f089f0c933423b4b026f53aa1b95296d85e823c643bfe0e8f735`.
Classification: `PASS_SCOPED_HELDOUT_WEYL3_GENERALIZATION_AND_PREDICTION_CONTRACT_STRESS`; 24/24 PASS.
Strongest held-out diagnostics: max fixed-scale q error `2.769683280777905e-04`; max finest rotation discrepancy `2.9473460146349044e-05`; W3 amplitude slopes `[2.9997228598916252,3.0000742431607224]`.

## Active original gate — Iter042
Preregistration: `status/ITERATION_042.md`.
Workflow: `qgr-iter042-boosted-magnetic-weyl`.
Production run: `34712954629`.
Frozen matrix: 24 scientific lanes + aggregate.

Already observed from raw terminal lane outputs:
- G42-E1 PASS: G0/y-direction magnetic response is monotonic with `B(0.24)/B(0.08)=3.0791994798062874`;
- G42-A5 PASS: G0 with v=(0.16,0.12,0.08) gives magnetic/electric ratio `0.24086383352122614`;
- G42-C0 PASS: H0, v=(0.15,0,0), boost-reversal parity error improves `0.005569940023953098 -> 0.0013934547915806722`;
- G42-D0 PASS: H0/V0 gives W3 kappa slope `2.9997071028479483`, magnetic slope `0.999809693602646`;
- G42-D1 PASS: H0/V3 gives W3 kappa slope `2.999523706583185`, magnetic slope `1.0001492864551422`;
- **G42-B3 scientific FAIL with valid controls**: G0, v=(0.15,0,0), finest W2 error `0.020130752262185782` but finest W3 error `0.10325268252592992`; frozen W3 <5% criterion and refinement-trend condition fail.

Do not infer the final Iter042 aggregate until all lanes are terminal. The already observed B3 failure means full G42 PASS is impossible under the frozen criteria unless the original artifact is found invalid; its controls were reported valid, so the expected final category is at most PARTIAL.

## Active corrective diagnostic — Iter042R
Preregistration committed before production: `status/ITERATION_042R.md` (`1058f1113987c826635bab898431b0fb906f0a89`).
Implementation: `code/qgr_iter042r_frame_completion.py`.
Aggregate: `code/qgr_iter042r_aggregate.py`.
Workflow: `qgr-iter042r-frame-completion`.
Trigger/head: `650a7424d0377388619ca975496c12edf702ddfd`.
Production run: `34713234061`.
Frozen matrix: **24 scientific lanes + aggregate**.

The diagnostic tests a concrete reconstruction issue: after the boost, the old finite-cell curvature entering `weyl_proxy` carries its first pair in an internal Minkowski frame while its last pair has already been mapped to boosted coordinate axes. G40/G41 did not expose this because the frames coincided at the unboosted base point. Iter042R freezes a frame-completion `Rcoord_abcd = F0^A_a F0^B_b R_ABcd` and tests:
- exact all-four-index Lorentz invariance of existing W2/W3 scalar contractions (8 lanes);
- frame-completed scalar covariance with the **same** 5% thresholds as original G42-B (6 lanes);
- mixed-vs-completed attribution including the already-observed G0/V0 failure (4 lanes);
- corrected magnetic emergence/parity (6 lanes).

Full corrective classification is `PASS_SCOPED_G42_COVARIANCE_DEFECT_ATTRIBUTED_TO_MIXED_FRAME_RECONSTRUCTION_AND_FRAME_COMPLETION_VALIDATED`.
If exact Stream A fails, the deeper classification is `FAIL_SCOPED_EXISTING_WEYL_SCALAR_CONTRACTION_NOT_LORENTZ_INVARIANT`.

## Current decision lock
Do **not** launch the independent radiative/TT-wave gate while G42/G42R are unresolved. If G42R validates frame completion, preserve original G42 as the discovery/partial record, adopt the corrected observable reconstruction prospectively, then preregister an independent radiative geometry. If G42R fails, remain on covariance/observable reconstruction rather than masking the defect with new physics scans.

## Strongest positive result
The static G40/G41 prediction manifold remains strongly supported and the boosted sector already shows nonzero magnetic response, odd boost-parity tendency and correct kappa scaling in several valid lanes.

## Strongest blocker
`BOOSTED_SCALAR_COVARIANCE / INTERNAL-TO-COORDINATE FRAME COMPLETION`, before any independent radiative geometry.

## Claim locks
- theory established `0%`;
- original frozen G42 result cannot be rewritten post hoc by G42R;
- beta remains an explicit matching/calibration parameter; `beta=1` is not physics;
- c6 remains unfixed;
- boosted static geometry is not a new dynamical solution;
- finite numerical covariance/refinement evidence is not a global theorem;
- no experimental confirmation;
- no physical branch weights from G35–G37 distant roots;
- no KMQGB `NEW_REQUIRED` authorization.
