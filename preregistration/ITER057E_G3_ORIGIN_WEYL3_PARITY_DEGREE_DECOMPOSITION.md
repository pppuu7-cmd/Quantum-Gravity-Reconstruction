# Iter057E preregistration — G3-origin Weyl3 linearization parity/degree decomposition

Date: 2026-09-15
Gate: `ITER057E-G3-ORIGIN-WEYL3-LINEARIZATION-PARITY-DEGREE-DECOMPOSITION`

## Motivation

Iter057D establishes that the source-owned G3/H0 metric is exactly even under `y -> -y`, with `Gamma(0)=0`, `nabla C(0)=0`, and all required background coefficient jets source-determined. Before constructing the full lower-degree Weyl3 symbol, determine exactly which perturbation-derivative degrees are allowed at the inversion-fixed origin.

## Frozen question

Does covariance/naturality of the Iter056X local metric Euler operator, together with the exact inversion symmetry of the G3/H0 background, force the local linearized Weyl3 operator at `y=0` to contain only even perturbation derivative orders `4,2,0`, with the degree-three and degree-one blocks vanishing identically?

## Frozen obligations

A. Establish the exact background isometry/involution `P:y -> -y` and verify that the frozen origin is a fixed point.

B. Treat the Iter056X Euler tensor as a natural rank-two metric differential operator. Linearize equivariance about the `P`-invariant background; do not assume a coordinate scalar proxy.

C. Track the parity of a rank-two input perturbation and rank-two output under the Jacobian `dP=-I`. Show or refute that an `m`-derivative local coefficient at the fixed point changes by `(-1)^m` while input/output tensor-index signs cancel pairwise.

D. Classify the possible homogeneous covector degrees of the fourth-order linearized Weyl3 operator. Maximum PASS requires an exact result

`L_W3(k) = L4(k) + L2(k) + L0`,

with

`L3=L1=0`.

E. Identify `L4` with the already-authorized curvature-Hessian `k4` block used in Iter054C/057A-C, up to the already-locked convention/overall symbolic `c6` multiplier.

F. Give a source-dependency map for `L2`: identify which background tensors/coefficient derivatives can enter. Do not invent or numerically fit them. In particular distinguish algebraic curvature/P contributions from second derivatives of background curvature-Hessian/P coefficients.

G. State the exact consequence for Iter057C: determine whether the two-block result `M2_E + lambda M4_W3` is sufficient or insufficient for the **full** mixed-order local characteristic operator at the G3 origin.

H. Preserve all claim locks and do not infer physical cone splitting, hyperbolicity, ghost content, treatment selection or a value of `c6`.

## Frozen classifications

Maximum PASS:

`PASS_SCOPED_ITER057E_G3_ORIGIN_WEYL3_LINEARIZATION_HAS_ONLY_K4_K2_K0_BLOCKS__K2_CONSTRUCTION_REQUIRED`.

Scientific FAIL if a valid naturality/parity derivation permits a nonzero odd-degree block at the inversion-fixed origin:

`SCIENTIFIC_FAIL_ITER057E_ODD_DEGREE_WEYL3_BLOCK_SURVIVES_G3_ORIGIN_PARITY`.

INVALID if source background, inversion action, or tensor transformation law is not fixed consistently.

## Interpretation ceiling

PASS is only a local structural theorem at the G3/H0 inversion-fixed origin. It is not a statement for arbitrary points/backgrounds and does not compute `L2` or the full characteristic variety.

`c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains 0%.