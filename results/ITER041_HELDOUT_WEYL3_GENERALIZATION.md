# Iter041 — held-out Weyl^3 generalization and prediction-contract stress

Date: 2026-09-12
Status: `PASS_SCOPED_HELDOUT_WEYL3_GENERALIZATION_AND_PREDICTION_CONTRACT_STRESS`

## Authoritative production provenance

- workflow: `qgr-iter041-heldout-weyl`
- run: `34712571244`
- launch head: `3c4d96d2658c2bd1aff6565c0f2cbc43595502bf`
- aggregate job: `103604189849`
- aggregate artifact: `10303324187` (`qgr-iter041-summary`)
- aggregate digest: `sha256:289bbbbe42b1f089f0c933423b4b026f53aa1b95296d85e823c643bfe0e8f735`
- frozen preregistration: `status/ITERATION_041.md`

All **24/24** preregistered held-out scientific lanes passed with valid controls:
- A fixed-scale held-out shape transfer: **6/6**;
- B held-out refinement transfer: **6/6**;
- C held-out amplitude law: **4/4**;
- D rotated cubic-null falsifiers: **4/4**;
- E held-out rotation covariance: **4/4**.

## Terminal aggregate diagnostics

- maximum fixed-scale held-out `q=W3/tr(H^3)` relative error: `0.0002769683280777905`;
- maximum finest refinement held-out q relative error: `0.00027696835073143515`;
- maximum finest held-out rotation discrepancy: `2.9473460146349044e-05`;
- maximum finest rotated-null normalized cubic residual: `1.8275144691009777e-05`;
- held-out Weyl-norm amplitude-slope range: `[0.999941304636997, 1.0000103050279203]`;
- held-out Weyl-cubic amplitude-slope range: `[2.9997228598916252, 3.0000742431607224]`.

Representative independent lanes:
- off-diagonal `G1`: `||W|| ~ kappa^0.9999413`, `|W3| ~ kappa^2.9997229`;
- G1 refinement q-error: `2.0232737201269663e-05 -> 4.8560256777000495e-06` from coarse to fine;
- rotated null `Rz23 Ry19`: normalized absolute cubic `3.0294321512728057e-05 -> 7.588240371216409e-06`;
- held-out G0 rotation `Rz13`: normalized signed-cubic discrepancy `9.59395902007507e-05 -> 2.3999453791648947e-05`.

## Scientific interpretation

The calibration-free static tidal response law discovered in Iter040 transfers prospectively to six generic off-diagonal trace-free held-out tidal tensors and to rotations/nulls not used to construct the G40 training set. Within this same-field weak static tidal realization, the evidence therefore supports a common continuum-proxy cubic response kernel controlled by the tidal cubic invariant, rather than an accident of the original diagonal training profiles.

This strengthens the **shape-level prediction contract** but does not add absolute normalization authority. `beta` remains an explicit matching/calibration parameter under Iter039 and `c6` remains an unfixed overall six-derivative coefficient.

The static electric-tidal family is now computationally saturated for the present purpose: more nearby static Hessian scans would mostly duplicate G40/G41. The next information-gain frontier is a genuinely new same-field non-static / magnetic-Weyl covariance sector.

## Decision

Do **not** densify the weak static electric-tidal scans next. Move to a preregistered non-static / magnetic-Weyl test that introduces time-space metric/tetrad components or an equivalent observer-boosted sector, while keeping the same ten-component symmetric metric arena and existing torsion closure.

A suitable first gate is a Lorentz-boosted version of the already-authorized weak vacuum tidal geometry: the same underlying curvature is described in a boosted frame, producing time-dependent/off-diagonal metric components and a nonzero magnetic Weyl part for the boosted observer. Scalar Weyl invariants must remain the same in the continuum limit. This is a strong covariance test and a bridge toward genuinely dynamical magnetic-Weyl backgrounds.

## Claim locks

- theory established: **0%**;
- held-out PASS is scoped to the weak static tidal family and is not an arbitrary-spacetime theorem;
- finite refinement evidence is not an analytic continuum theorem;
- `beta=1` is not authorized as physics;
- `beta` remains an explicit matching/calibration parameter under current authority;
- `c6` remains unfixed;
- response-kernel ratios/nulls are not absolute quantum phases;
- no experimental confirmation;
- no physical multiple-branch weights from G35–G37 distant roots;
- KMQGB `NEW_REQUIRED` remains unauthorized absent independent benchmark authority.
