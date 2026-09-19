# QGR — Finite-cylinder action-phase map v1

Status: PROSPECTIVELY PREREGISTERED, NOT YET PRODUCED

## Gate

`QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_V1`

## Frozen question

Can the already-authoritative finite-cylinder kinematic object be extended by one exact, bounded action-to-amplitude map that is mathematically well-defined on the existing reference Hilbert space while introducing no Hamiltonian, clock/update rule, gauge reduction, physical normalization, source normalization, observable map, continuum limit, or claim of physical quantum unitarity?

## Frozen dependency

Use only the already-authoritative kinematic source:

- `theory/quantum/QGR_KINEMATIC_METRIC_CYLINDER_V1.md`
- defining commit `1fe80cdb6cde0866d251b5c2d4c1d106f577d4d7`
- terminal classification `PASS_SCOPED_QUANTUM_KINEMATIC_METRIC_CYLINDER_AMPLITUDE_SPACE_DEFINED`

The dependency object is exactly `Q_N^kin=(V_N,X_N,mu_N,H_N)` with `H_N=L^2(X_N,mu_N;C)` and `mu_N` remaining a nonphysical coordinate reference measure.

## Frozen hypothesis/object

For each `N >= 1`, let `S_N : X_N -> R` be an externally supplied real-valued Borel-measurable function that is finite `mu_N`-almost everywhere. No formula for `S_N` is inferred, fitted, reconstructed, or selected by this gate.

Define the phase multiplier

`U[S_N] Psi_N (g) = exp(i S_N(g) / hbar) Psi_N(g)`

for `Psi_N in H_N`, with `hbar` retained symbolically as the ordinary nonzero action scale appearing only in the phase ratio. No numerical value or additional normalization is introduced.

The frozen mathematical claim is only that, under the stated input conditions on `S_N`, multiplication by the unit-modulus phase is a well-defined map `H_N -> H_N`, preserves the `mu_N` reference norm, and has inverse multiplication by `exp(-i S_N/hbar)`.

## Frozen inputs

1. `N >= 1`.
2. `Q_N^kin` exactly as defined at commit `1fe80cdb6cde0866d251b5c2d4c1d106f577d4d7`.
3. An external `S_N` satisfying the frozen measurability/reality/finiteness conditions.
4. An arbitrary `Psi_N in H_N`.

No classical QGR residual, Weyl^3 mismatch, corrected Q10 value, `c6`, `beta`, Hamiltonian, clock, source normalization, gauge fixing, Jacobian, or fitted target may be used as an input.

## Frozen controls

1. The source must preserve `V_N`, `X_N`, `mu_N`, and `H_N` byte-semantically from the authoritative kinematic dependency; `mu_N` must remain explicitly nonphysical.
2. `S_N` must remain an external symbolic input. The source must not choose or infer a physical action functional.
3. The phase factor must have modulus one `mu_N`-almost everywhere from the frozen real-valued input condition.
4. The source must establish exactly `||U[S_N]Psi_N||_{H_N}=||Psi_N||_{H_N}` and the inverse phase map, and no stronger physical claim.
5. No state normalization is introduced or required; the map acts on arbitrary `Psi_N in H_N`.
6. No Hamiltonian, time parameter, clock/update rule, transfer matrix, constraint algebra, gauge quotient, Faddeev-Popov determinant, BRST structure, physical measure, source normalization, observable/extraction map, probability rule, regulator, or continuum limit may be introduced.
7. No historical FAIL/BLOCKED result may be reclassified or used as fitted evidence.
8. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; corrected Q10 remains locked; theory established remains `0%`.

## Frozen source target

If the gate is realizable without violating the controls, the only defining source for the result is to be:

`theory/quantum/QGR_FINITE_CYLINDER_ACTION_PHASE_MAP_V1.md`

No GitHub Actions computation is required unless implementation introduces nontrivial executable verification not present in this preregistration.

## Frozen classification

`PASS_SCOPED_QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_DEFINED` only if the defining source exactly realizes the frozen map, dependency, controls, norm-preservation statement, inverse map, and interpretation ceiling.

`FAIL_QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_CONTROL_VIOLATION` if a produced source contradicts any frozen control or promotes the construction beyond its allowed scope.

`BLOCKED_QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_MISSING_REQUIRED_OBJECT` if the map cannot be defined without inventing an unstated action, Hamiltonian, clock/update rule, gauge prescription, physical normalization, source normalization, or other missing object.

`INVALID_QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_DEPENDENCY_DRIFT` if the frozen kinematic dependency cannot be reproduced exactly at the cited authority.

## Interpretation ceiling

A PASS establishes only a generic finite-cylinder phase-multiplication map on the already-defined nonphysical reference Hilbert space for an externally supplied real measurable `S_N`. It does **not** select a physical action, physical state, vacuum, boundary condition, time evolution, Hamiltonian dynamics, gauge reduction, physical path-integral measure, source normalization, observable, Born rule, reflection positivity, physical quantum unitarity, regulator removal, continuum limit, UV completion, experimental prediction, or quantum-gravity closure.

Mathematical norm preservation of this reference-space multiplier must not be reported as establishment of physical quantum unitarity.
