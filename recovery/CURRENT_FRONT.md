# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter044`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / END_TO_END_LINEARIZED_RADIATIVE_DYNAMICS`
Active roadmap stage: `principal refinement closure -> absolute-scale no-go -> calibration-free Weyl3 manifold -> held-out generalization -> boosted covariance stress -> frame completion -> independent TT geometry -> QGR-L1 dynamical TT contract`

## Canonical status
- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **94%**
- Iter005–Iter043 completion: **100%**
- Iter044: **PREREGISTERED / IMPLEMENTED / READY FOR PRODUCTION**
- Theory established: **0%**
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`
- Primitive additive source-law shape: **PASS_SCOPED `J(n)=beta*n`**
- Principal projective refinement / fixed-path-loop blocking: **PASS_SCOPED (G38)**
- Absolute source normalization `beta`: **EXPLICIT MATCHING/CALIBRATION PARAMETER (G39)**; `beta=1` not authorized as physics
- `c6` fixed: **NO**
- Calibration-free static Weyl^3 response manifold: **PASS_SCOPED (G40)**
- Held-out generic off-diagonal static Weyl^3 transfer: **PASS_SCOPED (G41)**
- Original boosted G42: **PARTIAL**, preserving scalar-covariance Stream-B negative result
- G42R frame completion: **PASS_SCOPED 24/24**, localizing the G42 scalar defect to mixed internal/coordinate reconstruction on the frozen family
- Independent TT radiative tensor/observable geometry: **PASS_SCOPED 24/24 (G43)**
- End-to-end QGR-L1 dynamical TT radiation contract: **ACTIVE G44**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

## Terminal Iter042 / Iter042R boundary
Iter042 head `b6e1c31c961f2536f10e3f9480053b2a62138253`; run `34712954629`; aggregate job `103606707505`; artifact `10304692021`; digest `sha256:c762dbe4532ec9adca18043c42e2d9a8768f85c7c2cec44c0a00fc359b351844`.
Classification: `PARTIAL_SCOPED_NONSTATIC_MAGNETIC_WEYL_COVARIANCE`.

Iter042R head `650a7424d0377388619ca975496c12edf702ddfd`; run `34713234061`; aggregate job `103610525399`; artifact `10303868886`; digest `sha256:8790997c6ad28eb68d8342d0092d2b6fc5c2f20dcf567819463fe05cd7277f56`.
Classification: `PASS_SCOPED_G42_COVARIANCE_DEFECT_ATTRIBUTED_TO_MIXED_FRAME_RECONSTRUCTION_AND_FRAME_COMPLETION_VALIDATED`.

Durable record: `results/ITER042_042R_TERMINAL.md`. The original G42 Stream-B failure remains a preserved discovery record and is not rewritten by the corrective diagnostic.

## Terminal Iter043 — independent analytic TT radiative geometry
Preregistered before production in `status/ITERATION_043.md`.

Authoritative production:
- head: `79b7325179aab34e83bbbc998152b81398221ef5`;
- run: `34715559793`;
- aggregate job: `103613094190`;
- artifact: `10303724918`;
- digest: `sha256:bd74de5bd2b0b17a9a0e043954f5f97e8fc964e1e64da1bb3d137b01f0286b83`.

Classification:
`PASS_SCOPED_INDEPENDENT_TT_RADIATIVE_WEYL_COVARIANCE`.

All **24/24** frozen lanes passed with valid controls. Aggregate extrema include maximum Lorentz error `4.681459141485685e-16`, W2 covariance error `2.0872426177969475e-16`, W3 covariance error `2.9099380740141584e-17`, E/B balance error `2.220446049250313e-16`, type-N W3 null `7.972433079490845e-19`, with exact-zero TT trace/transversality, Ricci/scalar and Weyl reconstruction in the frozen analytic construction.

Scientific meaning: the corrected observable layer reproduces and Lorentz-transports an independent held-out linearized TT vacuum geometry. This is **not** yet a derivation of radiation from QGR equations. Durable record: `results/ITER043_TT_RADIATIVE_WEYL_COVARIANCE.md`.

## Existing dynamical authority permitting Iter044
The next gate is not based on inserting Einstein equations by hand. Existing repository authority already gives:

- Iter004: exact reconstruction/selection of QGR-L1 from the complete S4-invariant quadratic two-derivative Noether family, with exactly two non-gauge null modes on the internal incidence cone and no allowed S4-invariant onsite mass term;
- Iter005: exact cubic and quartic Noether continuation under the independently derived relational pullback law;
- Iter007: unique all-orders local metric-only at-most-two-derivative action within its scoped domain, with the Einstein-Hilbert identification only a posteriori.

Therefore it is prospectively legitimate to ask whether the **QGR-L1 dynamical Hessian itself** generates the TT modes validated independently in G43.

## Active Iter044 — end-to-end QGR-L1 linearized radiative dynamics
Preregistered before implementation in `status/ITERATION_044.md`.

Frozen production design: **48 scientific lanes + aggregate** in four mutually independent streams:

1. **A / dynamics -> TT curvature, 24 lanes:** reconstruct QGR-L1 from its exact S4/Noether Hessian, solve/test the frozen null TT modes, verify four gauge nulls and exactly two non-gauge null directions, and map the QGR incidence-frame curvature to the direct G43 orthonormal TT curvature.
2. **B / off-shell dispersion, 12 lanes:** frozen frequency ratios `0.8,0.9,1.0,1.1,1.2`; require rank drop and unique residual minimum only at the internal incidence/null cone.
3. **C / gauge end-to-end robustness, 8 lanes:** add deterministic nonzero pure-gauge perturbations and require both QGR equation and radiative curvature to remain invariant within frozen tolerance.
4. **D / flat-background c6 decoupling, 4 lanes:** verify prospectively that the authorized `c6 Weyl^3` direction is cubic in perturbation and has zero quadratic Hessian at the flat branch; this does not fix c6.

Frozen full-PASS class:
`PASS_SCOPED_QGR_L1_END_TO_END_LINEARIZED_TT_RADIATION_CONTRACT`.

No threshold may be retuned after production.

## Strongest positive result
The programme now has an independently held-out TT radiative observable geometry (G43) plus pre-existing internally reconstructed QGR-L1 dynamics. G44 is the first gate that joins those two chains end-to-end rather than validating them separately.

## Strongest blocker
`QGR_L1_END_TO_END_LINEARIZED_RADIATIVE_DYNAMICAL_CLOSURE`, followed by genuinely nonlinear/higher-background radiation, quantum amplitudes/measure closure, and absolute matching/calibration (`beta`, `c6`).

## Claim locks
- theory established `0%`;
- G43 is tensor/observable validation, not QGR dynamical derivation;
- even a G44 PASS is scoped linearized end-to-end closure, not a nonlinear/global radiation theorem;
- finite numerical panels are not global theorems;
- beta remains explicit matching/calibration parameter and `beta=1` is not physics;
- c6 remains unfixed without a genuine independent Weyl-active absolute matching datum;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority;
- no experimental confirmation.
