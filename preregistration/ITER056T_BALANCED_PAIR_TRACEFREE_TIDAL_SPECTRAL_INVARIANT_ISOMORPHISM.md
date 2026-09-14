# Iter056T preregistration — balanced-pair / trace-free tidal spectral-invariant bridge

Date: 2026-09-14

Gate: `ITER056T-BALANCED-PAIR-TO-TRACEFREE-TIDAL-SPECTRAL-INVARIANT-ISOMORPHISM`

## Parent authority

Iter056S exact conditional PASS establishes that the source-owned G2 balanced pair tensor restricts to a trace-free symmetric tensor on the G2 spatial subspace with spectrum

`(2a, 2b, -2(a+b))`

and cubic invariant

`I3_B4=-24ab(a+b)`.

Iter040/041 use real symmetric trace-free 3x3 weak-tidal Hessians `H` and calibrate the continuum-proxy Weyl3 response against `Tr(H^3)` and rotation-invariant normalized cubic information.

## Frozen question

At the level of basis-independent **spectral shape invariants**, is the G2 balanced pair sector exactly equivalent to the full eigenvalue-shape space of a real symmetric trace-free 3x3 tidal Hessian, without amplitude calibration or continuum dynamics?

## Frozen theorem candidate

For any real symmetric trace-free 3x3 `T`, let its real eigenvalues be `(lambda1,lambda2,lambda3)` in any order. Since

`lambda1+lambda2+lambda3=0`,

define

`a=lambda1/2`, `b=lambda2/2`.

The G2 balanced pair tensor from Iter056S then has spatial spectrum

`(2a,2b,-2(a+b))=(lambda1,lambda2,lambda3)`.

Conversely every `(a,b)` gives a real trace-free 3-eigenvalue spectrum. Thus, modulo spatial orthogonal rotations and eigenvalue permutations, the two spectral shape spaces are candidate-isomorphic.

## Frozen invariant tests

For corresponding spectra require exactly:

1. `I2_B4 = Tr(H_sp^2) = lambda1^2+lambda2^2+lambda3^2 = Tr(T^2)`;
2. `I3_B4 = Tr(H_sp^3) = lambda1^3+lambda2^3+lambda3^3 = Tr(T^3)`;
3. `I3 = 3 det` on both sides;
4. for nonzero tensors the scale-free shape coordinate

   `chi = I3 / I2^(3/2)`

   is identical (including sign), while the algebraic squared invariant

   `chi2 = I3^2 / I2^3`

   is exactly rational/algebraic and identical without square-root convention;
5. cubic-null shape iff `I3=0`, including the eigenvalue pattern `(lambda,-lambda,0)`;
6. the H0 shape `(1,1,-2)` corresponds to `a=b=1/2` up to overall scale, as a previously known special case but not the only one.

## Frozen scope of equivalence

The proposed equivalence is **spectral/invariant only**:

- spatial orientation is quotiented by `O(3)`;
- eigenvalue labels are quotiented by `S3` permutations;
- overall amplitude may be kept or quotiented depending on whether `(I2,I3)` or `chi` is used.

No orientation-level tensor map from microscopic B4 to a realized G3 spatial frame is claimed.

## Frozen held-out repository validation

After this preregistration, inspect the Iter041 held-out off-diagonal trace-free Hessian panel (not read before freezing this gate).

For every Iter041 held-out `T`:

A. verify symmetry and trace zero;
B. compute its characteristic polynomial / eigenvalue invariants;
C. construct the corresponding G2 spectral pair `(a,b)` from any two eigenvalues;
D. verify `I2`, `I3`, determinant and `chi2` agreement;
E. verify that a rotated version of the same `T` has the same mapped invariant data.

Because floating eigensolvers can obscure exact identities, if Iter041 matrices use rational/algebraic entries, prefer exact symbolic characteristic-polynomial/invariant comparison. Numerical eigenvalues may be used only as display aids.

## Frozen negative controls

1. A symmetric 3x3 matrix with nonzero trace must be rejected by the map unless its trace part is first removed; silently projecting it to trace-free form is prohibited.
2. An antisymmetric perturbation must be rejected as outside the tidal symmetric-tensor domain.
3. Orientation information must not be reconstructed from `(a,b)`; doing so would exceed the spectral quotient and invalidate the claimed scope.

## Frozen terminal classifications

1. `PASS_SCOPED_CONDITIONAL_ITER056T_G2_BALANCED_PAIR_CUBIC_IS_EXACT_TRACEFREE_TIDAL_SPECTRAL_SHAPE_INVARIANT`
   - iff the generic theorem candidate is proved and all inspected Iter041 held-out matrices satisfy the frozen invariant checks.

2. `SCIENTIFIC_FAIL_ITER056T_SPECTRAL_INVARIANT_ISOMORPHISM`
   - iff the generic algebra or a valid held-out trace-free symmetric Iter041 matrix contradicts the theorem candidate.

3. `INVALID_AUDIT_ITER056T_HELDOUT_SOURCE_OR_DOMAIN_MISMATCH`
   - iff Iter041 held-out objects cannot be inspected or are not the advertised trace-free symmetric Hessians.

## Interpretation ceiling

PASS would establish an exact **conditional kinematic spectral-shape/invariant bridge** between the source-owned G2 balanced pair sector and the trace-free weak-tidal Hessian shape space used by Iter040/041.

It would not establish:

- orientation-level same-realization identification;
- amplitude map `a,b ↔ kappa`;
- `beta=1` or any beta value;
- equality of the microscopic pair cubic coefficient with continuum `c6`;
- Weyl curvature emergence from B4;
- a microscopic→continuum dynamical map;
- physical treatment selection, global measure/regulator removal, quantum unitarity, UV completion, GR recovery, experiment, new physics or QGR correctness.

The conditional G2 null-link/Lorentzian assumption remains explicit. Theory established remains 0%; `c6` remains symbolic/unfixed; `beta=1` unauthorized.