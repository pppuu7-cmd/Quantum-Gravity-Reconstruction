# QGR — Finite-cylinder action-phase map v1

## Scope and frozen dependency

This source realizes only the object prospectively frozen by `QUANTUM_FINITE_CYLINDER_ACTION_PHASE_MAP_V1` at preregistration commit `055926862c096b8d2aa93daa647003c92fe1e60c`.

Its sole dependency is the authoritative kinematic source `theory/quantum/QGR_KINEMATIC_METRIC_CYLINDER_V1.md` at commit `1fe80cdb6cde0866d251b5c2d4c1d106f577d4d7`.

For every integer `N >= 1`, retain exactly the dependency object

`Q_N^kin = (V_N, X_N, mu_N, H_N)`,

with

`V_N = {1,...,N}`,

`L_4 = { g in Sym_4(R) : det(g) != 0 and inertia(g) = (1 negative, 3 positive) }`,

`X_N = product_{v in V_N} L_4`,

`dmu_N = product_{v=1}^N product_{0<=a<=b<=3} dg_ab^(v)` restricted to `X_N`, and

`H_N = L^2(X_N, mu_N; C)`.

The measure `mu_N` remains only the same nonphysical coordinate reference measure. Nothing in this source changes, gauge-reduces, normalizes, or physically interprets it.

## External action input

Let

`S_N : X_N -> R`

be an externally supplied real-valued Borel-measurable function that is finite `mu_N`-almost everywhere. No formula for `S_N` is selected, inferred, fitted, reconstructed, calibrated, or derived here.

Let `hbar` be retained symbolically as a fixed nonzero real action scale appearing only in the dimensionless phase ratio `S_N/hbar`.

For arbitrary `Psi_N in H_N`, define

`(U[S_N] Psi_N)(g) = exp(i S_N(g)/hbar) Psi_N(g)`

for `mu_N`-almost every `g in X_N`.

## Well-definedness on the reference Hilbert space

Because `S_N` is real, Borel measurable, and finite almost everywhere, the multiplier

`M_N(g) = exp(i S_N(g)/hbar)`

is measurable and satisfies

`|M_N(g)| = 1`

for `mu_N`-almost every `g`.

Therefore multiplication by `M_N` respects almost-everywhere equivalence classes. For every `Psi_N in H_N`,

`integral_{X_N} |M_N(g) Psi_N(g)|^2 dmu_N = integral_{X_N} |Psi_N(g)|^2 dmu_N < infinity`,

so `U[S_N] Psi_N` is again in `H_N`.

Hence

`U[S_N] : H_N -> H_N`

is a well-defined linear multiplication map.

## Exact reference-norm preservation

For every `Psi_N in H_N`,

`||U[S_N] Psi_N||_{H_N}^2`

`= integral_{X_N} |exp(i S_N(g)/hbar) Psi_N(g)|^2 dmu_N`

`= integral_{X_N} |Psi_N(g)|^2 dmu_N`

`= ||Psi_N||_{H_N}^2`.

Thus exactly

`||U[S_N] Psi_N||_{H_N} = ||Psi_N||_{H_N}`.

No normalization of `Psi_N` is assumed or introduced.

## Inverse phase map

Define

`(U[-S_N] Psi_N)(g) = exp(-i S_N(g)/hbar) Psi_N(g)`.

Pointwise almost everywhere,

`exp(-i S_N/hbar) exp(i S_N/hbar) = 1`.

Consequently

`U[-S_N] U[S_N] = U[S_N] U[-S_N] = I_{H_N}`,

so the inverse of this reference-space phase multiplier is exactly

`U[S_N]^{-1} = U[-S_N]`.

## Frozen exclusions

This source does not choose or infer a physical action functional. It introduces no Hamiltonian, time parameter, clock/update rule, transfer matrix, constraint algebra, gauge quotient, gauge fixing, Faddeev-Popov determinant, BRST structure, physical measure, source normalization, state normalization, vacuum, boundary condition, observable/extraction map, Born/probability rule, regulator, continuum-limit rule, or regulator-removal prescription.

No classical QGR residual, Weyl^3 mismatch, corrected Q10 value, `c6`, `beta`, fitted target, or historical FAIL/BLOCKED result is used to define `S_N` or the map. `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; corrected Q10 remains locked; `theory_established=0%`; there is no experimental confirmation.

## Interpretation ceiling

This file establishes only a generic mathematical phase-multiplication map on the already-defined nonphysical reference Hilbert space for an externally supplied real measurable `S_N`, together with exact preservation of the existing `mu_N` reference norm and the inverse phase multiplier.

Reference-norm preservation here is not establishment of physical quantum unitarity. This source does not establish physical dynamics, a physical action, physical state, physical path-integral measure, gauge reduction, physical normalization, observables, probabilities, reflection positivity, quantum constraint closure, regulator removal, continuum limit, UV completion, experimental prediction, new physics, or quantum-gravity closure.