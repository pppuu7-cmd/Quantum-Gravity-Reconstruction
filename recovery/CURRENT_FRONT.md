# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter048`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / WEYL3 SYMMETRY-REDUCED VARIATIONAL RESPONSE`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program readiness: **96%** — internal construction-roadmap readiness only, not probability of correctness and not fraction of quantum gravity solved.
- Iter005–Iter047: completed in their stated scopes.
- Iter048: preregistered, implemented, authoritative production active, 24 scientific lanes + aggregate.
- Theory established: **0%**.
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`.
- `beta`: explicit matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6`: **unfixed**; Iter048 computes only the symbolic coefficient multiplying `c6`.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Terminal Iter046 — exact finite-amplitude nonlinear pp-wave radiation
Durable record: `results/ITER046_QGR_L1_EXACT_NONLINEAR_PPWAVE_RADIATIVE_SECTOR.md`.
Run `34718135187`, aggregate `103621013033`, artifact `10305972518`, digest `sha256:ca1cfb10420cb4e79f4324f009c0a664317098b7bb08b717f052d82397961a89`.

Classification: `PASS_SCOPED_QGR_L1_EXACT_FINITE_AMPLITUDE_NONLINEAR_PPWAVE_RADIATIVE_SECTOR`, **34/34** with valid controls. This is an exact finite-amplitude special pp-wave family of the two-derivative QGR-L1 action, not generic nonlinear/strong-field stability.

## Terminal Iter047 — exact `Weyl^3` curvature-class activation map
Durable record: `results/ITER047_EXACT_WEYL3_CURVATURE_CLASS_ACTIVATION_MAP.md`.

Authority:
- preregistration `dbd3745ad1082141790502b8423240771112ee03`;
- trigger/head `2c731e9a14c288e6e359c160476bc4bb0e78b801`;
- run `34719070003`;
- aggregate job `103621600017`;
- artifact `10305937870`;
- digest `sha256:7249e022a4b39241a5d61234c982e7b932b2eb9245c468c36f9ca1b54a35d2fb`.

Classification: `PASS_SCOPED_EXACT_WEYL3_CURVATURE_CLASS_ACTIVATION_MAP`, **24/24**, controls valid, `c6=SYMBOLIC_UNFIXED`.

Representative exact witnesses:
- type-N pp-wave: nonzero Weyl/Riemann but `W2=W3=0` exactly;
- Schwarzschild/Petrov-D: `W2=48 M^2/r^6`, `W3=96 M^3/r^9` exactly;
- Kasner `(-1/3,2/3,2/3)`: `W2=64/(27 t^4)`, `W3=256/(243 t^6)` exactly;
- conformally-flat FLRW: nonzero curvature controls but Weyl, `W2`, `W3` exactly zero.

Scientific consequence: Iter046's type-N pp-wave sector is algebraically blind to the scalar `Weyl^3` correction, so it cannot by itself constrain `c6` dynamics. `Weyl^3` is active on the tested Petrov-D and Kasner sectors. This is still only an invariant/operator map, not an Euler-Lagrange result.

## Active Iter048 — lapse-retaining Bianchi-I reduced variation of `Weyl^3`
Preregistered before implementation in `status/ITERATION_048.md`.

Frozen reduced metric:
`ds^2=-N(t)^2 dt^2+a(t)^2 dx^2+b(t)^2(dy^2+dz^2)`.

The production code constructs curvature and `Weyl^3` from the generic metric, forms `L6=N a b^2 W3`, derives the generalized higher-derivative Euler-Lagrange operators for `N,a,b` **before background substitution**, and then tests the coefficient multiplying symbolic/unfixed `c6`.

Frozen power-law certificate for `N=1,a=t^p,b=t^q` is preregistered analytically. On the exact vacuum Kasner point `p=-1/3,q=2/3`, the frozen targets are:
- `L6=256/(243 t^5)`;
- `E_N=1024/(243 t^5)`;
- `E_a=4096/(243 t^(14/3))`;
- `E_b=-5632/(243 t^(17/3))`.

Thus Iter048 tests a real variational prediction: the `c6*Weyl^3` term should be dynamically active in this reduced Kasner sector for nonzero `c6`, while the isotropic conformally-flat controls should give zero reduced response.

Frozen matrix: **24 lanes**:
- A6 exact Kasner activation;
- B6 conformally-flat/isotropic negative controls;
- C6 generic anisotropic power-law analytic-certificate audit;
- D6 exact Kasner time-reparameterization/action-density controls.

### Run authority
The first trigger run `34719340456` created **zero jobs and zero scientific artifacts** because the workflow YAML was invalid. It is permanently classified `ITER048_PREPRODUCTION_WORKFLOW_INVALID_ZERO_SCIENTIFIC_EVIDENCE` and has no scientific authority. No scientific criteria were changed.

Workflow serialization only was fixed in commit `3513818d3f50a93c1d62743d7013cae1bc7f4b61`, with authority record `status/ITERATION_048_RUN_AUTHORITY.md` commit `9ddba17221e83ca96255a8a382a82692462eb21d`.

Authoritative production:
- trigger/head `68cf38c745f146039cf63ed0f345e24bd87d5f01`;
- run **`34719396082`**;
- scientific jobs are now actively executing/queued.

Frozen full-PASS class:
`PASS_SCOPED_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE`.

Interpretation lock: even full PASS is **axisymmetric Bianchi-I symmetry-reduced variation only**. It is not the complete 4D covariant six-derivative field equation, does not determine `c6`, and does not establish a corrected Kasner solution.

## Current frontier
The project has moved beyond asking merely whether `Weyl^3` is nonzero. The current blocker is whether its coefficient gives an actual variational response on a curved Weyl-active background. If Iter048 passes, the next scientifically stronger frontier is the full covariant `Weyl^3` Euler-Lagrange tensor / independent covariant directional-variation certificate, or quantum amplitude/measure closure — not another repeated invariant panel.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` remains unfixed;
- Iter048 cannot be promoted to full covariant six-derivative dynamics;
- finite panels and symmetry-reduced calculations are not global theorems;
- beta remains matching/calibration parameter and `beta=1` is not physics;
- G45 does not establish absolute energy positivity or quantum unitarity;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority.
