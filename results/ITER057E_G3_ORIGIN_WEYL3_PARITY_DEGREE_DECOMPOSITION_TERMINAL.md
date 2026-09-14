# Iter057E terminal result — G3-origin Weyl3 parity/degree decomposition

Date: 2026-09-15
Gate: `ITER057E-G3-ORIGIN-WEYL3-LINEARIZATION-PARITY-DEGREE-DECOMPOSITION`
Prospective preregistration: `c6ff3a2cdc5d2fc4ad45e397aa838827eb2aff2c`
Analytic derivation: `ccabe4bf4d0e9800063adc345fa7bd9766a79b5b`

## Terminal classification

**`PASS_SCOPED_ITER057E_G3_ORIGIN_WEYL3_LINEARIZATION_HAS_ONLY_K4_K2_K0_BLOCKS__K2_CONSTRUCTION_REQUIRED`**

## Exact structural result

The source-owned G3/H0 background is invariant under the exact inversion isometry

`P:y -> -y`

and the frozen origin is a fixed point with `dP=-I`.

The Iter056X Weyl3 Euler tensor is a natural rank-two metric differential operator. Linearizing naturality about the `P`-invariant background implies that at the fixed point an `m`-derivative input term acquires the parity factor `(-1)^m`, while the two input tensor indices and two output tensor indices each contribute an even sign.

Therefore every odd-derivative coefficient must equal its own negative and vanish.

The exact local homogeneous covector decomposition is consequently

**`L_W3(k) = L4(k) + L2(k) + L0`**

with

**`L3(k)=L1(k)=0`.**

This is a local theorem at the G3/H0 inversion-fixed origin, not a generic-background theorem.

## Degree-four identity

The degree-four block comes uniquely from the curvature-Hessian part of the double-divergence term and is the same `k4` Weyl3 principal block already certified by Iter054B/C and reused in Iter057A-C:

`L4 = M4_Weyl3`

up to the locked convention and global symbolic multiplier `c6`.

No new degree-four surrogate is introduced.

## Degree-two dependency map

The missing `L2_Weyl3` block is genuine and source-determined. It receives contributions from:

1. `delta R_principal ~ partial^2 h` inside the algebraic Euler terms `1/2 g I3 - P.R`;
2. the metric-explicit part of `delta P` acted on by the two outer derivatives;
3. background connection-curvature terms in the second covariant derivative acting on the curvature-response part of `delta P`;
4. second derivatives of the curvature Hessian `partial^2 I3/partial R^2`, equivalently the source-owned second Weyl/curvature coefficient jet, multiplying `delta R_principal`;
5. variation of the outer Levi-Civita connections, including `partial delta Gamma * P`.

The potential degree-three coefficient terms are proportional to first background coefficient derivatives and vanish consistently with `nabla C=nabla P=0`. Degree-one terms vanish by the same parity/naturality theorem.

## Consequence for Iter057C

Iter057C remains a valid exact statement about the two highest selected blocks

`M2_Einstein + lambda M4_Weyl3`.

However, the full source-owned G3-origin mixed-order linearization contains

`M2_Einstein + c6 L2_Weyl3 + c6 L4_Weyl3`

plus degree-zero terms.

On high-order-rank-deficient directions, `L2_Weyl3` competes at the same derivative order as the Einstein block. Therefore Iter057C alone cannot determine the full local characteristic operator.

The next high-information construction is the source-faithful exact `L2_Weyl3` matrix on the frozen G3/H0 origin, with `c6` kept symbolic.

## Production decision

No GitHub Actions production was launched. The result is an exact consequence of a prospectively frozen source isometry and natural tensor-operator equivariance; numerical CI would not strengthen the parity theorem.

## Interpretation ceiling

This PASS does not compute `L2_Weyl3`, the complete characteristic variety, strong/symmetric hyperbolicity, a symmetrizer, physical cone splitting, mode/ghost content, energy, stability, treatment choice, unitarity or UV completion.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains `0%`.