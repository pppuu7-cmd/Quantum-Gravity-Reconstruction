# QGR — Quantum kinematic metric-cylinder amplitude-space object v1

## Scope

This source defines only the finite-cylinder kinematic object prospectively frozen by `QUANTUM_KINEMATIC_METRIC_CYLINDER_AMPLITUDE_SPACE_V1`. It is not a quantum-gravity closure, dynamics, gauge-reduction, normalization, observable, probability, unitarity, regulator-removal, or continuum-limit construction.

## Frozen object

For each integer `N >= 1`, define the finite labelled set

`V_N = {1,...,N}`.

Let

`L_4 = { g in Sym_4(R) : det(g) != 0 and inertia(g) = (1 negative, 3 positive) }`.

Thus every matrix in `L_4` is real, symmetric, nondegenerate, and has Lorentz signature with one negative and three positive eigenvalues.

Define the finite-cylinder configuration domain

`X_N = product_{v in V_N} L_4`.

At each label `v`, use the ten independent symmetric entries `g_ab^(v)`, `0 <= a <= b <= 3`, as coordinates. Define the reference measure

`dmu_N = product_{v=1}^N product_{0<=a<=b<=3} dg_ab^(v)`,

restricted to `X_N`. Equivalently, `mu_N` is the restriction to `X_N` of the product Lebesgue reference measure in these `10N` coordinates.

Define

`H_N = L^2(X_N, mu_N; C)`.

A kinematic amplitude is any equivalence class `Psi_N in H_N`; this definition selects no particular nonzero state.

The complete object defined here is

`Q_N^kin = (V_N, X_N, mu_N, H_N)`.

## Semantic restrictions and blocked structure

`mu_N` is only a coordinate reference measure on the finite labelled cylinder. It is not claimed to be diffeomorphism invariant, gauge reduced, Faddeev-Popov corrected, physical, unique, dynamically selected, or derived from a path integral.

`N` is only a finite-cylinder label. It is not a physical UV/IR regulator, and no `N -> infinity` limit is defined or implied.

No particular physical state, state normalization, vacuum, boundary condition, transition amplitude, partition function, or Born probability is established. No Hamiltonian, dynamics, action-to-amplitude map, clock/update rule, transfer operator, constraint operator, BRST complex, gauge fixing, Jacobian, source normalization, or observable/extraction map is introduced.

Gauge reduction, dynamics, physical normalization, observables, positivity, reflection positivity, unitarity, quantum constraint closure, regulator removal, continuum limit, UV completion, experimental prediction, and new-physics claims therefore remain explicitly BLOCKED.

Classical finite certificates, corrected Q10, Weyl^3 diagnostics, and residuals are not inputs to this object and do not promote its interpretation. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; `theory_established=0%`; there is no experimental confirmation.

## Interpretation ceiling

This file establishes only the mathematical definition of a finite-cylinder kinematic amplitude/state space with an explicit domain and a nonphysical coordinate reference measure. It does not establish a physical quantum state, physical path-integral measure, gauge invariance, dynamics, normalization, observables, probabilities, unitarity, continuum limit, or quantum gravity.