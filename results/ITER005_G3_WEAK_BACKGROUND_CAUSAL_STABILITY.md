# QGR Iter005-G3 — weak-background causal stability

Date: 2026-09-11
Status: `PASS_SCOPED_LOCAL_WEAK_BACKGROUND_CHARACTERISTIC_STABILITY`

## Objective

After exact quartic Noether closure, test whether weak nonzero backgrounds preserve a controlled Lorentzian characteristic structure and exactly two physical propagating modes, rather than generating extra high-frequency branches or losing the incidence cone.

## Background response

The QGR-L1 field is the symmetric second-moment response. Write

`G_down = E + hbar`,

with

`E = C^{-1}`

and the previously derived incidence contravariant form

`C = J-I`.

The inverse response expands as

`G_up = C - C hbar C + C hbar C hbar C + O(hbar^3)`.

Because Iter005-G2 fixed `S4` as the next coefficient of the same local two-derivative pullback-covariant connection density, the quadratic fluctuation operator about a weak background uses this same inverse response in its principal part through the order controlled by `S2+S3+S4`.

Thus the predicted local characteristic polynomial is

`K_hbar(k) = k_i G_up^{ij} k_j`.

At first order,

`delta K = -(C k)^a hbar_ab (C k)^b`.

No independent cone-deformation coefficient is introduced.

## Lorentzian inertia

For sufficiently small `hbar`, `G_down` remains nondegenerate with the same Lorentzian inertia as `E`. Equivalently, under a nonsingular local frame deformation `A`,

`G_down = A^T E A`,

so

`G_up = A^{-1} C A^{-T}`.

By congruence, the signature is unchanged. The causal cone therefore deforms continuously rather than changing signature under a sufficiently small regular perturbation.

## Exact rational rank certificates

Three nontrivial rational frame deformations were tested exactly. For each background the quadratic connection-density Hessian was reconstructed directly from `G_up`, with no floating-point coefficients.

Tested null covectors included transformed versions of the four elementary covers and transformed versions of the previously used nontrivial incidence-null vectors

- `(1,1,1,-1)`;
- `(1,2,3,-11/6)`;
- `(2,-1,3,-1/4)`.

For every tested `G_up`-null covector:

- `K_hbar(k)=0` exactly;
- the 10x4 derivative gauge map has rank **4**;
- the 10x10 kinetic Hessian has rank **4**;
- the Hessian annihilates all four gauge directions exactly;
- total nullity is 6, hence non-gauge physical nullity is **2**.

For representative transformed non-null covectors:

- `K_hbar(k) != 0`;
- the Hessian rank is **6**;
- nullity is exactly the four gauge directions.

Classification:

`PASS_SCOPED_LOCAL_PRINCIPAL_SYMBOL_PRESERVES_ONE_LORENTZIAN_CONE_AND_TWO_PHYSICAL_MODES_ON_WEAK_REGULAR_BACKGROUNDS`.

## Why this extends beyond constant test backgrounds at principal-symbol level

The interacting local action is second order in derivatives. Derivatives of a slowly varying background enter lower-derivative terms of the linearized equations; the highest-derivative principal symbol at a point depends on the local value of `G` itself. Therefore the constant-background calculation is the local principal-symbol model for a smooth weak background.

This statement is local and perturbative. It does not establish global hyperbolicity on arbitrary curved configurations.

## What remains open

Not established here:

- global causal stability on large/strong backgrounds;
- absence of caustics or global topology problems;
- all-orders nonlinear Noether completion;
- same-realization refinement/coarse-graining;
- finite interacting quantum amplitudes;
- equivalence principle as an operational matter-coupling theorem;
- normalized observables or independent KMQGB passage.

## Reproducibility

`code/qgr_iter005_g3_weak_background_cone.py`
