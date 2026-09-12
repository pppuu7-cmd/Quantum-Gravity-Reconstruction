# Iteration 042R — frame-completion audit of boosted curvature/Weyl observables

Date: 2026-09-12
Status: `PREREGISTERED / CORRECTIVE DIAGNOSTIC`

## Why this corrective gate exists

The original Iter042 frozen production remains authoritative and its criteria are not changed. During production, lane B3 (`G0`, v=(0.15,0,0)) produced valid boost/torsion/metric controls but failed the frozen scalar-covariance condition: finest W2 discrepancy ~2.01% passed while finest W3 discrepancy ~10.33% failed and did not show the required refinement trend.

A code-level audit identified a concrete structural ambiguity that was harmless in the unboosted G40/G41 setup but matters after a coordinate boost: the finite-cell curvature object entering the old `weyl_proxy` has its first Lorentz-index pair in the internal Minkowski frame while the last two curvature-form indices have already been mapped into the boosted coordinate Minkowski axes. The old scalar contraction then treats these four indices as if they belonged to a single common frame.

Iter042R prospectively tests whether this mixed-frame contraction is the source of the G42 scalar-covariance defect. It does **not** retroactively change G42's frozen classification.

## Frozen frame-completion rule

Let the finite-cell curvature after the existing lattice/base conversion be

`R_{AB cd}`,

where A,B are internal Minkowski-frame indices and c,d are boosted-coordinate indices. At the base point x=0, let

`F0^A_a = F_boost(y_new=0)^A_a`.

Define the frame-completed all-coordinate curvature

`Rcoord_{ab cd} = F0^A_a F0^B_b R_{AB cd}`.

At the flat base point of the frozen weak tidal backgrounds, `g_ab(0)=eta_ab`, so the existing Ricci/Weyl decomposition may then be applied consistently to `Rcoord` with eta.

No fitting is allowed. `beta` and `c6` are absent from this diagnostic.

## Stream A — exact tensor-contraction Lorentz audit (8 lanes)

Use H0 and G0, each with boosts V0,V1,V2,V3 from Iter042. For each lane:
1. obtain an unboosted finite-cell Weyl tensor at h=0.05, kappa=0.04;
2. transform **all four covariant indices** exactly with the frozen Lorentz coordinate map;
3. recompute W2 and W3 using the existing scalar contraction routines.

PASS requires relative changes in both W2 and W3 `<1e-10` and Lorentz-matrix error `<1e-12`.

Interpretation:
- if Stream A fails W3, the scalar contraction itself is not a Lorentz scalar and must be repaired before any boosted physics claim;
- if A passes, the contraction is algebraically sound and the defect lies in mixed-frame reconstruction / finite-cell covariance.

## Stream B — frame-completed scalar refinement covariance (6 lanes)

Use the same six (H,V) pairs and h=[0.10,0.075,0.05] as original G42-B.
For each h compare unboosted and **frame-completed boosted** W2/W3.

PASS per lane requires inherited numerical controls plus:
- finest W2 relative discrepancy `<0.05`;
- finest W3 relative discrepancy `<0.05`;
- each discrepancy decreases coarse -> fine, or both coarse/fine values for that invariant are already `<1e-3`.

These are intentionally the same scientific tolerances as original G42-B; they are not weakened after seeing B3.

## Stream C — attribution on the observed failing pair (4 lanes)

Use G0 with V0,V2,V3 plus H0 with V0, h=[0.10,0.075,0.05]. For each lane compute both:
- original mixed-frame W2/W3 discrepancies;
- frame-completed W2/W3 discrepancies.

PASS requires valid controls, frame-completed finest W3 discrepancy `<0.05`, and either:
- frame-completed finest W3 discrepancy is less than one-half the mixed-frame finest W3 discrepancy; or
- frame-completed finest W3 discrepancy `<1e-3`.

The G0/V0 lane is the frozen primary attribution control because it is the already-observed G42-B3 failure; the other three are prospectively frozen replication lanes.

## Stream D — corrected magnetic emergence and parity (6 lanes)

Use four emergence cases `(H0,V0),(H0,V3),(G0,V0),(G0,V3)` at h=0.05 plus two parity cases `(H0,V0),(G0,V3)` over h=[0.10,0.075,0.05]. Compute E/B only from the frame-completed coordinate Weyl tensor.

Emergence lane PASS:
- controls valid;
- `||B||>1e-8`;
- `||B||/max(||E||,1e-30)>0.01`.

Parity lane PASS:
- controls valid for +v and -v;
- finest `||B(+v)+B(-v)||/[0.5(||B(+v)||+||B(-v)||)] <0.10`;
- error decreases coarse->fine or both coarse/fine `<1e-3`.

## Production matrix

- A exact tensor contraction: 8 lanes;
- B corrected scalar refinement: 6 lanes;
- C mixed-vs-completed attribution: 4 lanes;
- D corrected magnetic diagnostics: 6 lanes;
- total **24 scientific lanes + aggregate**;
- fail-fast false.

## Terminal classifications

Full diagnostic PASS:
`PASS_SCOPED_G42_COVARIANCE_DEFECT_ATTRIBUTED_TO_MIXED_FRAME_RECONSTRUCTION_AND_FRAME_COMPLETION_VALIDATED`
if all 24 lanes pass.

Deeper scalar-contraction defect:
`FAIL_SCOPED_EXISTING_WEYL_SCALAR_CONTRACTION_NOT_LORENTZ_INVARIANT`
if any valid Stream-A lane fails its exact W2/W3 invariance check.

Partial diagnostic:
`PARTIAL_SCOPED_G42_FRAME_COMPLETION_DIAGNOSTIC`
if Stream A is valid/pass but one or more B/C/D scientific relations fail.

Control-invalid:
`CONTROL_INVALID_OR_INCOMPLETE_ITER042R` if expected lanes are missing or numerical/boost controls invalidate interpretation.

## Claim locks

- original Iter042 frozen result is never rewritten from this corrective audit;
- a successful repair may explain the G42 proxy failure but does not prove full QGR Lorentz covariance;
- boosted static geometry is still not an independent dynamical spacetime;
- theory established remains 0%;
- beta remains an external matching/calibration parameter; beta=1 unauthorized as physics;
- c6 remains unfixed;
- no experimental confirmation;
- no KMQGB NEW_REQUIRED authorization.
