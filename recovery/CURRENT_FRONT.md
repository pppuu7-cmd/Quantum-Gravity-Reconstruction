# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter049`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / WEYL3 SPHERICALLY-REDUCED VARIATIONAL RESPONSE`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program readiness: **97%** — internal construction-roadmap readiness only, not probability of correctness and not fraction of quantum gravity solved. The increase 96 -> 97 is credited specifically to terminal Iter048 variational activation.
- Iter005–Iter048: completed in their stated scopes.
- Iter049: preregistered and implemented; authoritative retry production active, 24 scientific lanes + aggregate.
- Theory established: **0%**.
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`.
- `beta`: explicit matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6`: **unfixed**; current gates compute only its coefficient.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Terminal Iter048 — first actual reduced variational response of `Weyl^3`
Durable record: `results/ITER048_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE.md`.

Authoritative run `34719396082`, aggregate job `103622629715`, artifact `10305449033`, digest `sha256:2d183a735d97408c1145b077cb9817ec6f4456aaa7d3e405de916ff596cafb97`.

Classification: `PASS_SCOPED_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE`, **24/24**, controls valid.

On exact Ricci-flat Kasner after generic lapse-retaining Bianchi-I variation:
- `W3=256/(243 t^6)`;
- `L6=256/(243 t^5)`;
- `E_N=1024/(243 t^5)`;
- `E_a=4096/(243 t^(14/3))`;
- `E_b=-5632/(243 t^(17/3))`.

All three reduced responses are nonzero. Curved conformally-flat controls gave exact zero `W3` and zero reduced response. This is a real variational result, but only in the stated symmetry reduction, not the full covariant 4D equation.

## Active Iter049 — independent static-spherical variational sector
Preregistered before implementation in `status/ITERATION_049.md`, commit `72b21197d594ab6c5f36a34dfbd18a68b97d0a1d`.

Generic radial-gauge-unfixed metric:
`ds^2=-F(r)^2 dt^2+N(r)^2 dr^2+S(r)^2 dOmega^2`.

The code derives curvature, `Weyl^3`, reduced density `L6=F N S^2 W3`, and generalized `E_F,E_N,E_S` before imposing Schwarzschild or any areal-radius relation.

Frozen Schwarzschild targets:
- `W3=96 M^3/r^9`;
- `L6=96 M^3/r^7`;
- `E_F=-48 M^2(-32M+15r)/(r^(13/2)sqrt(r-2M))`;
- `E_N=-48 M^2(-8M+3r)sqrt(r-2M)/r^(15/2)`;
- `E_S=96 M^2(-22M+9r)/r^8`.

Frozen exact radial Noether identity:
`E_F F' + E_S S' - N(E_N)' = 0`.

Frozen 24-lane matrix:
- A6 Schwarzschild/Petrov-D reduced variational activation;
- B6 de Sitter/anti-de Sitter conformally-flat constant-curvature controls;
- C6 radial-reparameterization controls;
- D6 generic-profile Noether identity audits.

### Initial production diagnostic
Initial trigger/head `237cd84006afa867352c27fa274c8aa7c25d14ae`, run `34719814120`.

Early valid evidence:
- A0 reproduced all frozen Schwarzschild formulas exactly and had all three reduced responses nonzero;
- D3 passed the exact generic radial Noether identity with all three reduced responses nonzero.

B0 returned `W3=L6=E_F=E_N=E_S=0`, but default symbolic simplification left one apparent Weyl component
`r*(sin(2 theta) tan(theta)+cos(2 theta)-1)/(2 tan(theta))`, which is identically zero. `trigsimp(method='fu')` reduces it exactly to zero.

This is recorded in `status/ITERATION_049_RUN_AUTHORITY.md`, commit `83a5d538b4d2987bae304d0396c96d644bf24810`, as
`ITER049_INITIAL_PRODUCTION_SYMBOLIC_CONTROL_INVALID_REQUIRES_CANONICAL_TRIG_RETRY`.

No scientific criterion, witness, analytic target, threshold, or interpretation lock was changed. Only exact-zero trigonometric canonicalization was strengthened in commit `73298317eaf5a401caf4dea3fe8eee3808727042`.

### Authoritative retry
- trigger/head `c8e574b2a78ae02c3e1476ef1daf7efc8268c342`;
- authoritative run **`34719948722`**;
- 24 scientific jobs are queued/executing under the unchanged frozen gate;
- terminal classification pending frozen aggregate.

Frozen full-PASS class:
`PASS_SCOPED_WEYL3_SPHERICALLY_REDUCED_VARIATIONAL_RESPONSE`.

## Current frontier
If authoritative G49 passes, `Weyl^3` will have nonzero variational response in two genuinely independent curved symmetry classes, with independent covariance controls. The next high-value gate should then leave symmetry reduction and target a genuinely covariant directional-variation/full functional-derivative certificate, or quantum amplitude/measure closure if that covariant derivation is not yet technically ready. A third repetitive symmetry reduction should not be launched merely to add compute.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` remains unfixed;
- G48/G49 reduced variations are not the full 4D covariant six-derivative field equation;
- finite panels and symmetry-reduced calculations are not global theorems;
- beta remains matching/calibration parameter and `beta=1` is not physics;
- G45 does not establish absolute energy positivity or quantum unitarity;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority.
