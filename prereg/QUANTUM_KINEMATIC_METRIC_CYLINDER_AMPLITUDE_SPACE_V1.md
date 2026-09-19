# QGR — Quantum kinematic metric-cylinder amplitude-space object v1

Status: PROSPECTIVELY PREREGISTERED, NOT YET IMPLEMENTED

## Purpose

Construct exactly one minimal quantum kinematic object that supplies an explicit configuration domain, reference measure semantics, and amplitude/state space without importing any classical certificate as quantum closure and without inventing dynamics, a Hamiltonian, clock/update rule, physical normalization, gauge quotient, observable map, probability/unitarity theorem, or continuum-limit claim.

This gate is a source/object construction only. It is not a physics closure gate.

## Frozen hypothesis

A mathematically exact finite-cylinder kinematic amplitude-space object can be durably defined for labelled Lorentzian metric variables while leaving every dynamical, gauge, normalization, observable, unitarity, and continuum-limit question explicitly BLOCKED.

## Frozen target source authority

Implementation may create exactly one new defining source file:

`theory/quantum/QGR_KINEMATIC_METRIC_CYLINDER_V1.md`

No repository search, recursive tree scan, historical artifact scan, residual fitting, or external derivation is required or authorized for this gate.

## Frozen object

For each integer `N >= 1`, define the finite labelled set

`V_N = {1,...,N}`.

Let

`L_4 = { g in Sym_4(R) : det(g) != 0 and inertia(g) = (1 negative, 3 positive) }`.

Define the finite-cylinder configuration domain

`X_N = product_{v in V_N} L_4`.

At each label `v`, use the ten independent symmetric matrix entries `g_ab^(v)` with `0 <= a <= b <= 3` as coordinates. Define the kinematic reference measure

`dmu_N = product_{v=1}^N product_{0<=a<=b<=3} dg_ab^(v)`, restricted to `X_N`.

Define the kinematic amplitude/state space

`H_N = L^2(X_N, mu_N; C)`.

A kinematic amplitude is any equivalence class `Psi_N in H_N`.

The tuple

`Q_N^kin = (V_N, X_N, mu_N, H_N)`

is the complete object of this gate.

## Frozen semantic restrictions

1. `mu_N` is only a coordinate reference measure on the finite labelled cylinder. It is not claimed to be diffeomorphism invariant, gauge reduced, Faddeev-Popov corrected, physical, unique, dynamically selected, or derived from a path integral.
2. `N` is only a finite-cylinder label. It is not a physical UV/IR regulator and no `N -> infinity` limit is defined or implied.
3. No particular nonzero `Psi_N` is selected by this gate. Therefore no state normalization, vacuum, boundary condition, transition amplitude, partition function, or Born probability is established.
4. No Hamiltonian, action-to-amplitude map, clock/update rule, transfer operator, constraint operator, BRST complex, gauge fixing, Jacobian, or source normalization is introduced.
5. No observable/extraction map is introduced.
6. No positivity, reflection positivity, unitarity, quantum constraint closure, regulator removal, continuum limit, UV completion, experimental prediction, or new-physics claim is authorized.
7. Classical finite certificates, corrected Q10, Weyl3 diagnostics, and residuals are not inputs to this object and cannot promote its interpretation.
8. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; `theory_established=0%`.

## Frozen dependency contract

Required durable inputs are only:

- this preregistration commit;
- the current recovery lock that the quantum closure object was previously missing.

The implementation must be target-blind with respect to any desired physical conclusion. It may only instantiate the exact mathematical definitions frozen above.

## Frozen controls

PASS requires all of the following:

1. exactly one source file is created at the frozen target path;
2. the source file defines `V_N`, `L_4`, `X_N`, `mu_N`, `H_N`, and `Q_N^kin` exactly with the semantics frozen above;
3. Lorentz signature is explicit and degenerate matrices are excluded;
4. the measure is explicitly the 10N-coordinate product Lebesgue reference measure restricted to `X_N`;
5. the amplitude/state object is explicitly `L^2(X_N,mu_N;C)` and no particular physical state is smuggled in;
6. all gauge/dynamics/normalization/observable/unitarity/continuum semantics remain explicitly BLOCKED;
7. no classical certificate or residual is used as a quantum input;
8. all claim locks remain preserved.

## Frozen classification

- `PASS_SCOPED_QUANTUM_KINEMATIC_METRIC_CYLINDER_AMPLITUDE_SPACE_DEFINED` iff every frozen control passes and the source object is durably committed.
- `FAIL_TECHNICAL_QUANTUM_KINEMATIC_OBJECT_DEFINITION_DRIFT` if a source file is produced but differs from the frozen object or semantic restrictions.
- `BLOCKED_QUANTUM_KINEMATIC_OBJECT_NOT_DURABLY_REALIZED` if the exact source object cannot be durably created without adding an unpreregistered assumption.
- `INVALID_QUANTUM_KINEMATIC_OBJECT_SCOPE_VIOLATION` if the implementation imports dynamics, physical normalization, gauge reduction, observable/probability semantics, or claims quantum closure.

Green CI, if any, is not sufficient for PASS.

## Interpretation ceiling

A PASS establishes only a finite-cylinder **kinematic amplitude/state space with explicit domain and reference measure semantics**. It does not establish a physical quantum state, a physical path-integral measure, gauge invariance, dynamics, normalization, observables, probabilities, unitarity, continuum limit, or quantum gravity. At most it fills a narrowly scoped portion of the previously missing quantum-object tuple and provides a durable source authority for subsequent separately preregistered gates.