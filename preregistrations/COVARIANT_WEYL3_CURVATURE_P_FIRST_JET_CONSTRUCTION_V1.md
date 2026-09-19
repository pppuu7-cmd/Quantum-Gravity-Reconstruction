# Preregistration — COVARIANT_WEYL3_CURVATURE_P_FIRST_JET_CONSTRUCTION_V1

Date: 2026-09-19

## Purpose
Construct, without consulting any historical residual target, an exact curvature-dependent P object and its covariant first jet for the cubic Weyl invariant. This gate is object-definition only; it does not test or repair the historical generic-P mismatch.

## Frozen convention
Let the local scalar interaction be L6 = c6 I3 with c6 symbolic/unfixed and
I3 = C_{ab}{}^{cd} C_{cd}{}^{ef} C_{ef}{}^{ab}.
Define the Weyl projection as a linear metric-dependent map Pi_g from algebraic Riemann tensors to Weyl tensors: C = Pi_g[R]. Define its adjoint Pi_g^* by the contraction pairing. Define P_R as the Frechet derivative with respect to an algebraic-Riemann variation delta R:

delta L6 = P_R : delta R

for every delta R obeying the algebraic Riemann symmetries. This variational definition fixes all pair-symmetry normalization conventions and avoids component derivative ambiguities.

## Frozen derivation target
By cyclicity of the cubic contraction, the candidate object must be derived as
P_R = 3 c6 Pi_g^*[C o C],
where (C o C) is the pair-endomorphism square under the same contraction used in I3.

Using Levi-Civita metric compatibility, nabla g=0, hence nabla Pi_g=0 and nabla Pi_g^*=0. The first jet must therefore be derived by the covariant product rule:

nabla_e P_R = 3 c6 Pi_g^*[(nabla_e C) o C + C o (nabla_e C)].

No commutativity of the pair-endomorphism product may be assumed unless proved under the contraction pairing.

## Frozen controls
1. P_R has algebraic Riemann pair antisymmetries and pair exchange symmetry after Pi_g^*.
2. P_R is trace-free in the Weyl-projected slots.
3. Euler homogeneity control: P_R : R = 3 L6.
4. First-jet product rule is linear in nabla C and quadratic overall in curvature/curvature jet.
5. c6 remains symbolic and factored.
6. No Lane-D residual, mismatch coefficient, target monomial, or post-hoc correction may be read or used.
7. No third symmetry reduction; no quantum claim; no global theorem.

## Frozen taxonomy
PASS_SCOPED_CURVATURE_WEYL3_P_AND_FIRST_JET_DEFINED iff the variational derivation and all six intrinsic controls close exactly at the abstract tensor-map level.
BLOCKED_CONVENTION_OR_PROJECTOR_DEFINITION iff the exact map cannot be defined without importing an unstated convention.
FAIL_INTRINSIC_P_OR_JET_CONTROL iff an intrinsic control fails.

A PASS authorizes only a later separately preregistered comparison gate. It does not reclassify any historical FAIL/BLOCKED result and does not establish the full 4D Euler-Lagrange tensor.

Claim locks: theory_established=0%; no experimental confirmation; beta=1 unauthorized; c6 symbolic/unfixed; finite panels are not global theorems; G45 does not prove absolute energy positivity/quantum unitarity; G35-G37 do not authorize physical weights; KMQGB NEW_REQUIRED unauthorized.