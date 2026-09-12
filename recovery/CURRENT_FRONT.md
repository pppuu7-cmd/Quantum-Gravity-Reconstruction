# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter049`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / WEYL3 SPHERICALLY-REDUCED VARIATIONAL RESPONSE`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program readiness: **97%** — internal construction-roadmap readiness only, not probability of correctness and not fraction of quantum gravity solved. The increase 96 -> 97 is credited specifically to terminal Iter048 variational activation, not compute volume.
- Iter005–Iter048: completed in their stated scopes.
- Iter049: preregistered, implemented and production queued, 24 scientific lanes + aggregate.
- Theory established: **0%**.
- Active candidate: `QGR-L1 / Sym^2(W4) second-moment branch`.
- `beta`: explicit matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6`: **unfixed**; Iter049 computes only its coefficient.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Terminal Iter048 — actual reduced variational response of `Weyl^3`
Durable record: `results/ITER048_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE.md`.

Authority:
- preregistration `278ec25f089430a09d8b64540cbc57ed481f4fce`;
- implementation `b618e848785e96ed6968e5ca06282d84c7925950`;
- frozen aggregate `4da8340f0dbc1a2ff1a51a55ff1fb8061592b992`;
- first run `34719340456` = `ITER048_PREPRODUCTION_WORKFLOW_INVALID_ZERO_SCIENTIFIC_EVIDENCE`, zero jobs / zero scientific evidence;
- authoritative trigger/head `68cf38c745f146039cf63ed0f345e24bd87d5f01`;
- authoritative run `34719396082`;
- aggregate job `103622629715`;
- summary artifact `10305449033`;
- digest `sha256:2d183a735d97408c1145b077cb9817ec6f4456aaa7d3e405de916ff596cafb97`.

Terminal aggregate: **24/24 PASS**, fails 0, controls valid.

Classification:
`PASS_SCOPED_WEYL3_SYMMETRY_REDUCED_VARIATIONAL_RESPONSE`.

For exact Ricci-flat Kasner `N=1, a=t^-1/3, b=t^2/3`, after deriving the generic generalized Euler-Lagrange operators before substitution:
- `W3=256/(243 t^6)`;
- `L6=256/(243 t^5)`;
- `E_N=1024/(243 t^5)`;
- `E_a=4096/(243 t^(14/3))`;
- `E_b=-5632/(243 t^(17/3))`.

All three reduced responses are nonzero. In curved conformally-flat isotropic controls, `W3=E_N=E_a=E_b=0` exactly despite nonzero Riemann curvature. Generic anisotropic power-law certificates and time-reparameterization density controls also passed exactly.

Scientific meaning: the QGR-selected `Weyl^3` term has now crossed from invariant activation to an **actual nonzero variational response** in one lapse-retaining curved anisotropic symmetry sector. This still does not constitute the full 4D covariant six-derivative equation and does not determine `c6`.

## Active Iter049 — independent static spherical variational sector
Preregistered before implementation in `status/ITERATION_049.md`.

Frozen generic metric, with radial gauge deliberately not fixed before variation:
`ds^2=-F(r)^2 dt^2+N(r)^2 dr^2+S(r)^2 dOmega^2`.

The code constructs curvature and `Weyl^3` directly from generic `F,N,S`, forms the angular-factor-stripped density `L6=F N S^2 W3`, and derives `E_F,E_N,E_S` before any Schwarzschild substitution.

Frozen exact Schwarzschild targets, imposed only after generic variation:
- `W3=96 M^3/r^9`;
- `L6=96 M^3/r^7`;
- `E_F=-48 M^2(-32M+15r)/(r^(13/2)sqrt(r-2M))`;
- `E_N=-48 M^2(-8M+3r)sqrt(r-2M)/r^(15/2)`;
- `E_S=96 M^2(-22M+9r)/r^8`.

The generic radial diffeomorphism/Noether certificate is frozen as
`E_F F' + E_S S' - N(E_N)' = 0` exactly.

Frozen matrix: **24 scientific lanes**:
- A6 Schwarzschild/Petrov-D reduced variational activation;
- B6 de Sitter/anti-de Sitter conformally-flat constant-curvature negative controls;
- C6 exact radial-reparameterization anti-artifact controls;
- D6 generic-profile radial Noether-identity audits.

Authority:
- preregistration commit `72b21197d594ab6c5f36a34dfbd18a68b97d0a1d`;
- implementation commit `2e6e8d527bb81e415c3eb5c93526e5eb0a127673`;
- aggregate commit `939353319ac7158f27d2841323c1e34b6d491fc9`;
- workflow commit `1ef0baf2d96fba9187a409e1108b433fd5cb072b`;
- trigger/head `237cd84006afa867352c27fa274c8aa7c25d14ae`;
- production run **`34719814120`**.

Frozen full-PASS class:
`PASS_SCOPED_WEYL3_SPHERICALLY_REDUCED_VARIATIONAL_RESPONSE`.

Interpretation lock: even a full Iter049 PASS is a second independent symmetry-reduced variational sector, not the complete 4D covariant `Weyl^3` Euler-Lagrange tensor and not a determination of `c6`.

## Current frontier
After G48, the important question is no longer whether `Weyl^3` can influence dynamics at all — it can in the tested reduced Kasner sector. G49 tests whether that conclusion survives a genuinely independent curved symmetry class with an exact radial Noether covariance certificate. If it does, the next high-value gate should be a genuinely covariant directional-variation/full functional-derivative certificate or quantum amplitude/measure closure, rather than a third repeated reduction.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` remains unfixed;
- G48/G49 reduced variations are not the full covariant six-derivative field equation;
- finite panels and symmetry-reduced calculations are not global theorems;
- beta remains matching/calibration parameter and `beta=1` is not physics;
- G45 does not establish absolute energy positivity or quantum unitarity;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority.
