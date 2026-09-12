# QGR Current Research Front

Updated: 2026-09-13
Primary active iteration: `Iter050`
Project phase: `MODEL_CONSTRUCTION / COVARIANT WEYL3 VARIATION PREREQUISITE`

## Canonical status
- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **98%** — internal construction-roadmap readiness only, not correctness probability and not fraction of quantum gravity solved. The increase 97 -> 98 is credited only to terminal Iter049 closure of a second independent curved symmetry-reduced variational sector.
- Iter005–Iter049: completed in their stated scopes.
- Theory established: **0%**.
- `beta`: explicit matching/calibration parameter; `beta=1` is not authorized as physics.
- `c6`: **unfixed**; current gates compute only its coefficient.
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**.

## Terminal Iter049 — independent static-spherical variational sector
Durable record: `results/ITER049_WEYL3_SPHERICALLY_REDUCED_VARIATIONAL_RESPONSE.md`.

Frozen gate preregistered at `72b21197d594ab6c5f36a34dfbd18a68b97d0a1d`. Initial run `34719814120` is diagnostic/non-authoritative because a symbolic exact-zero trig simplifier produced a false-negative control. Authority record `83a5d538b4d2987bae304d0396c96d644bf24810`; control-only canonical-trig repair `73298317eaf5a401caf4dea3fe8eee3808727042`. No scientific target, threshold, witness or interpretation changed.

Authoritative retry:
- head `c8e574b2a78ae02c3e1476ef1daf7efc8268c342`;
- run `34719948722`;
- aggregate job `103624666186`;
- aggregate artifact `10306068977` (`qgr-iter049-summary`);
- digest `sha256:d474a1eeb41b2a56c74ec5266794b0362c26560bdcb062e232ae564c2381ce22`;
- 24/24 frozen scientific lanes consumed; controls valid.

Terminal classification:
`PASS_SCOPED_WEYL3_SPHERICALLY_REDUCED_VARIATIONAL_RESPONSE`.

This is a real second independent symmetry-reduced variational response of the coefficient of `c6`. It is **not** the complete four-dimensional covariant Weyl^3 Euler–Lagrange tensor.

## Current frontier — Iter050
Do not start a third repetitive symmetry reduction. The next high-information gate is a genuinely covariant, non-symmetry-reduced variation prerequisite for the local Weyl-cubic scalar.

Planned gate: `ITER050-WEYL3-COVARIANT-CURVATURE-DIRECTIONAL-VARIATION-PREREQUISITE`.

The gate must be prospectively preregistered before implementation. It may test the curvature-direction derivative/P-tensor of `I3=C_{mu nu}^{ rho sigma} C_{rho sigma}^{ alpha beta} C_{alpha beta}^{ mu nu}` on generic four-dimensional algebraic-curvature data, with independent finite-difference convergence, Lorentz-basis covariance and conformally-flat/null controls. Passing such a gate is only a prerequisite to the full metric functional derivative: it does not certify the metric variation of the Weyl projectors/measure nor the covariant double-divergence term in the full f(Riemann) Euler–Lagrange tensor.

## Claim locks
- theory established = **0%**;
- no experimental confirmation;
- `c6` remains unfixed;
- G48/G49 reduced variations are not the full 4D covariant six-derivative field equation;
- a future Iter050 curvature-direction certificate is also not the full metric field equation;
- finite panels and symmetry-reduced calculations are not global theorems;
- beta remains matching/calibration parameter and `beta=1` is not physics;
- G45 does not establish absolute energy positivity or quantum unitarity;
- no physical multiple-branch weights from G35–G37;
- no KMQGB `NEW_REQUIRED` without independent benchmark authority.
