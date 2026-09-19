# QGR Current Research Front

Updated: 2026-09-19

## Programme status

`candidate_program_roadmap_readiness = 100%` is infrastructure/roadmap readiness only. `theory_established = 0%`. No experimental confirmation. `c6=SYMBOLIC_UNFIXED`; `beta=1` unauthorized.

## Preserved authority

Iter049 `ITER049-WEYL3-SPHERICALLY-REDUCED-VARIATIONAL-RESPONSE` remains authoritative at retry run `34719948722`, preregistration `72b21197d594ab6c5f36a34dfbd18a68b97d0a1d`, retry head `c8e574b2a78ae02c3e1476ef1daf7efc8268c342`; initial run `34719814120` remains diagnostic/non-authoritative. Iter048 terminal PASS 24/24 remains do-not-repeat. Historical covariant parent run `35367461999` remains `SCIENTIFIC_FAIL_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_DISCREPANCY`; corrected six-cell run `35412692881` remains finite-panel only. Generic-P diagnostics and the curvature-P-jet BLOCKED result remain immutable.

## Quantum kinematic metric-cylinder amplitude-space object v1 — terminal scoped PASS

Gate: `QUANTUM_KINEMATIC_METRIC_CYLINDER_AMPLITUDE_SPACE_V1`.
Preregistration: `9c62c5a6e5d1f97908fbb42141bfc1bfedf39cd9`.
Defining source: `theory/quantum/QGR_KINEMATIC_METRIC_CYLINDER_V1.md`, commit `1fe80cdb6cde0866d251b5c2d4c1d106f577d4d7`.
Durable result: `results/QUANTUM_KINEMATIC_METRIC_CYLINDER_AMPLITUDE_SPACE_V1.md`, commit `17ea22e9ddb3e054f07c2960c7c5a87bf97a7b9e`.
Classification: `PASS_SCOPED_QUANTUM_KINEMATIC_METRIC_CYLINDER_AMPLITUDE_SPACE_DEFINED`.

The source defines only `Q_N^kin=(V_N,X_N,mu_N,H_N)` with finite labelled Lorentzian metric cylinder domain, explicit coordinate reference measure, and `H_N=L^2(X_N,mu_N;C)`. The measure remains nonphysical and non-gauge-reduced. No dynamics, physical state, normalization, observable, probability/unitarity theorem, regulator removal, or continuum limit is established.

## Active preregistered gate — finite-cylinder action-phase map v1

Gate: `QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_V1`.
Preregistration: `055926862c096b8d2aa93daa647003c92fe1e60c` (`prereg/QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_V1.md`).
Status: `PROSPECTIVELY_PREREGISTERED_NOT_YET_PRODUCED`.

Frozen dependency: exactly the kinematic source at commit `1fe80cdb6cde0866d251b5c2d4c1d106f577d4d7`.

Frozen object: for externally supplied real Borel-measurable `S_N:X_N->R`, finite `mu_N`-almost everywhere, define only the phase multiplier

`U[S_N] Psi_N(g) = exp(i S_N(g)/hbar) Psi_N(g)`

on `H_N`, with `S_N` remaining entirely symbolic/external. The gate may establish only well-definedness on `H_N`, preservation of the existing `mu_N` reference norm, and the inverse phase multiplier. It may not choose a physical action or introduce any Hamiltonian, clock/update rule, source normalization, gauge prescription, physical measure, observable, probability rule, regulator, or continuum limit.

Frozen PASS: `PASS_SCOPED_QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_DEFINED`.
Frozen FAIL: `FAIL_QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_CONTROL_VIOLATION`.
Frozen BLOCKED: `BLOCKED_QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_MISSING_REQUIRED_OBJECT`.
Frozen INVALID: `INVALID_QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_DEPENDENCY_DRIFT`.

Interpretation ceiling: even a PASS is only a generic mathematical phase-multiplication map on the nonphysical reference Hilbert space. Reference-norm preservation is not physical quantum unitarity and does not establish dynamics or quantum-gravity closure.

## Remaining quantum closure front

The earlier authority-pointer audit remains `BLOCKED_MISSING_QUANTUM_CLOSURE_OBJECT_DEFINITION`. The kinematic source fills only configuration-domain/reference-measure/amplitude-space structure. The active gate, if it passes later, would add only a generic externally supplied action-phase map. Still undefined are at least: a physical/dynamically selected action, gauge/Jacobian treatment, physical normalization/renormalization, observable/extraction map, positivity/unitarity/probabilistic criterion, and regulator-removal/continuum-limit rule.

## Next bounded step

Inspect only the active preregistration `055926862c096b8d2aa93daa647003c92fe1e60c` and its single frozen dependency source `theory/quantum/QGR_KINEMATIC_METRIC_CYLINDER_V1.md` at commit `1fe80cdb6cde0866d251b5c2d4c1d106f577d4d7`. If dependency provenance is exact, create only `theory/quantum/QGR_FINITE_CYLINDER_ACTION_PHASE_MAP_V1.md` according to the frozen controls and terminally classify the gate. No Actions run is required unless nontrivial executable verification is newly required by the frozen gate. Do not open another gate in the same run.

## Locks

`theory_established=0%`; no experimental confirmation; `c6=SYMBOLIC_UNFIXED`; corrected Q10 LOCKED; `beta=1` unauthorized; finite panels are not global theorems; G45 does not prove absolute energy positivity or quantum unitarity; G35-G37 distant roots do not authorize physical weights; KMQGB `NEW_REQUIRED` unauthorized; classical != quantum; kinematic state space != dynamics; reference-space norm preservation != physical unitarity; diagnostic != closure.