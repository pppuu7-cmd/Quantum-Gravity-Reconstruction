# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter051`
Project phase: `MODEL_CONSTRUCTION / FULL COVARIANT WEYL3 METRIC VARIATION`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — internal construction-roadmap readiness only, not correctness probability and not fraction of quantum gravity solved.
- Iter005–Iter050: completed in their stated scopes.
- Iter051 current completion: **20%**.
- Theory established: **0%**.
- `beta`: explicit matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6`: **unfixed**.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Terminal Iter050
Iter050 remains `PASS_SCOPED_COVARIANT_WEYL3_CURVATURE_DIRECTIONAL_VARIATION_PREREQUISITE` on 12/12 generic non-symmetry-reduced fixed-metric curvature-direction lanes. It is a prerequisite only, not the complete metric functional derivative.

## Terminal Iter051A — frozen scientific failure
Durable record: `results/ITER051A_WEYL3_METRIC_DENSITY_VARIATION_SCIENTIFIC_FAIL.md`.

Parent preregistration: `bf5615dd36b533ba536c85f4c8d7658cd7e3568c`.
Implementation: `307b4bd66a54a03fb7162c069e9d3e5fc4928d53`.
Frozen aggregate: `4cbe7971910d3108472e4ce08026a783fecca82f`.
Authoritative production head: `55e4c099516cbfe9a76ab826994cc5f28cae69c0`.

Authoritative terminal provenance:
- run `34724233650`;
- aggregate job `103635469747`;
- aggregate artifact `10307431104` (`qgr-iter051a-summary`);
- digest `sha256:17b0d975691abdee5e7cbf4fa45198f7f6b3c8e0136a017c7b3cb8c5902e8a33`;
- expected/found lanes `12/12`;
- frozen lane PASS `5/12`;
- nonzero calibration `12/12`.

Aggregate extrema:
- max algebraic residual `8.326672684688674e-17`;
- max Weyl-trace residual `1.1102230246251565e-16`;
- max density-covariance relative discrepancy `1.4471991837432272e-14`;
- max directional-covariance relative discrepancy `3.355094633829336e-14`;
- max finest-step complex-step/FD relative discrepancy `1.6407915760785562e-09`.

Terminal classification:
`SCIENTIFIC_FAIL_G51A_ALGEBRAIC_METRIC_VARIATION`.

The aggregate failure is scientifically binding for this frozen gate. At least one raw failing lane is localized to the preregistered finite-difference convergence predicate despite excellent algebraic/covariance controls and small complex-step/FD discrepancy. This does not authorize post-hoc weakening of the convergence rule.

## Active diagnostic — Iter051A-D1
A separate numerical diagnostic was prospectively preregistered after terminal G51A and before implementation:
- preregistration commit `5536412cc6b5a82535737bc60228fc8259320707`;
- implementation commit `ea474bafa31ecb31bbc19d103706307427e45001`;
- aggregate commit `7bcadb5cdc7869ac1ffd294d1436d2698288d889`;
- workflow trigger/head `9a20884caa150dce0852b6c173174d33847d37f8`.

Purpose: test whether the seven original G51A failures are predominantly centered-FD roundoff turnover on a broader frozen step ladder while retaining exactly the same physical lanes, complex-step reference and inherited controls. No diagnostic outcome can retroactively change G51A from FAIL to PASS.

## Frontier lock
Full 4D covariant Weyl3 Euler-Lagrange promotion is blocked. A valid G51A-class algebraic metric/measure/projector certificate and an independent G51B covariant double-divergence/connection-response certificate are both required. G51B may be designed in analysis, but no full-EOM promotion is allowed while G51A is failed.

If Iter051A-D1 confirms dominant FD roundoff turnover, the next admissible step is a newly preregistered high-precision algebraic metric-variation certificate using an independently controlled derivative comparator. If it does not, the algebraic metric-variation formulation itself must be audited before further promotion.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` remains unfixed;
- finite panels and symmetry-reduced calculations are not global theorems;
- beta remains matching/calibration parameter and `beta=1` is not physics;
- G45 does not establish absolute energy positivity or quantum unitarity;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority.
