# Exact control — exact higher-derivative versus perturbative solution spaces

Date: 2026-09-14

Status: mathematical control / downstream preparation only. Not a QGR dynamical-treatment choice.

## Schematic equation

Let `Box` denote a linear second-order hyperbolic operator and consider

`Box phi + eps*lambda*Box^2 phi = 0`,

with `eps != 0`, `lambda != 0`.

This is the operator analogue of the frozen Iter054A/E polynomial

`P(z)=z+eps*lambda*z^2`.

## Exact finite-eps treatment

The equation factorizes exactly:

`Box (1 + eps*lambda*Box) phi = 0`.

Therefore the exact solution space contains two algebraic sectors:

1. `Box phi_0 = 0`;
2. `(1 + eps*lambda*Box) phi_HD = 0`, equivalently `Box phi_HD = -1/(eps*lambda) phi_HD`.

The second sector is non-analytic in `eps` at `eps=0` because its characteristic scale diverges as the coefficient is removed.

This factorization alone does not assign norm, residue, gauge status, physical weight or validity domain to the second sector.

## Perturbative branch analytic at eps=0

Now impose a formal analytic expansion

`phi = sum_{n=0}^N eps^n phi_n + O(eps^(N+1))`.

At leading order,

`Box phi_0 = 0`.

At first order,

`Box phi_1 + lambda Box^2 phi_0 = Box phi_1 = 0`.

Inductively, if `Box phi_j = 0` for all lower coefficients in this simple homogeneous control, then the higher-derivative source built from `Box^2 phi_j` vanishes and the next coefficient remains on the `Box`-kernel branch.

Thus no finite Taylor expansion analytic at `eps=0` can generate the exact sector with

`Box phi_HD = -1/(eps*lambda) phi_HD`.

The singular branch is genuinely outside the perturbative analytic solution space.

## Why this matters for QGR object definition

The same local higher-derivative operator can therefore support two different admissible-history prescriptions:

- **exact finite-coefficient dynamics:** retain the full factorized solution space and supply the extra initial-data/evolution structure;
- **perturbative/order-reduced dynamics:** retain only the branch continuously analytic in the small correction within a declared expansion domain.

These are not interchangeable interpretations of a root table. A QGR-specific principle must decide which prescription is physical, or explicitly retain both as separate candidate versions.

## Strong-hyperbolicity implication

The principal/evolution system to be tested depends on that choice. An exact fourth-order formulation and an order-reduced second-order formulation have different state vectors and potentially different constraint/gauge systems. A single determinant proxy cannot certify strong hyperbolicity for both.

## Claim ceiling

This is a schematic exact control. It does not establish that the QGR Weyl3 tensor equations factorize this way, does not select a QGR treatment, and does not prove any physical extra mode, ghost, stability, unitarity, cutoff, `c6`, `beta=1`, UV completion, GR recovery, experiment or new physics.
