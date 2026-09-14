# Iter056S preregistration — balanced B4 pair tensor to tidal cubic-shape held-out validation

Date: 2026-09-14

Gate: `ITER056S-BALANCED-B4-PAIR-TENSOR-TO-TIDAL-CUBIC-SHAPE-HELDOUT-VALIDATION`

## Chronology / hypothesis source

Hypothesis-generation note, committed before this held-out validation:

`e89913217b12ff37cadcf7510d77e954fac55ecb`

The note froze the candidate formulas derived from the Iter003-G2 balanced pair basis. This gate must not change them after seeing held-out outputs.

## Frozen source authority

Use only the Iter003-G2 pair perturbation sector and its conditional Lorentzian generator-space decomposition:

- edge order `(01,02,03,12,13,23)`;
- `TT1=(0,1,-1,-1,1,0)`;
- `TT2=(1,0,-1,-1,0,1)`;
- pair tensor `H` is symmetric 4x4, zero diagonal, `H_ij=x_ij`;
- balanced sector annihilates `t=(1,1,1,1)`;
- the conditional B4 Lorentzian seed distinguishes `t` from the sum-zero 3D spatial subspace.

The conditional status of the G2 null-link/Lorentzian hypothesis is retained throughout.

## Frozen parameterization and predicted identities

For

`x = a TT1 + b TT2`,

predict exactly:

1. `H t = 0`;
2. the characteristic polynomial is
   `lambda (lambda-2a)(lambda-2b)(lambda+2(a+b))`;
3. the nonzero/spatial eigenvalue multiset is
   `{2a, 2b, -2(a+b)}`;
4. `Tr(H)=0` and the spatial restriction is traceless;
5. `Tr(H^3) = -24 a b (a+b)`;
6. all 24 generator permutations preserve the balanced-sector condition and the cubic invariant;
7. on the special frozen H0 lane `a=b`, the spatial eigenvalue ratios are exactly `1:1:-2`.

No formula may be weakened after the held-out lanes run.

## Frozen held-out lanes

Generic non-null lanes:

- G0: `(a,b)=(1,2)`
- G1: `(2,-3)`
- G2: `(-2,5)`
- G3: `(3,4)`
- G4: `(5,-1)`
- G5: `(7/3,-2/5)`

Special lanes:

- H0-shape: `(a,b)=(3/2,3/2)`
- cubic-null: `(a,b)=(5/3,-5/3)`

These values were not used in the hypothesis-generation note's algebraic examples.

## Frozen exact tests per lane

Every lane must pass:

A. all four row-balance equations exactly;
B. exact `H t=0`;
C. exact characteristic-polynomial identity;
D. exact `Tr(H^3)=-24ab(a+b)`;
E. exact invariance of `Tr(H^2)` and `Tr(H^3)` under all 24 S4 generator permutations;
F. exact preservation of `t` as the zero mode under all 24 permutations;
G. rank of the spatial restriction equals the number predicted by the three frozen spatial eigenvalues.

Special predicates:

- H0-shape lane: after dividing by the common nonzero factor, sorted spatial eigenvalues must be exactly proportional to `(-2,1,1)`.
- cubic-null lane: `Tr(H^3)=0` exactly while `H` is nonzero.

## Frozen basis-independence test

Use the fixed orthonormal spatial basis

`u1=(1,-1,0,0)/sqrt(2)`

`u2=(1,1,-2,0)/sqrt(6)`

`u3=(1,1,1,-3)/sqrt(12)`.

Let `Q=[u1 u2 u3]` and `K=Q^T H Q`.

Require exactly/symbolically:

- `Tr(K)=0`;
- `Tr(K^2)=Tr(H^2)`;
- `Tr(K^3)=Tr(H^3)`;
- `det(K)` equals the product `2a*2b*(-2(a+b))`.

This ensures the cubic is genuinely the invariant of the 3D spatial restriction, not an artifact of the 4x4 coordinate representation.

## Frozen negative control

For each lane form

`H_bad = H + delta (E_01+E_10)`, `delta=1/7`.

Do not rebalance any other edge.

Require the control to fail the balanced zero-mode condition:

`H_bad t != 0`.

The control is not required to violate cubic invariance under coordinate conjugation; its purpose is to distinguish the G2 balanced physical sector from an arbitrary zero-diagonal symmetric pair matrix.

## Frozen terminal classifications

1. `PASS_SCOPED_CONDITIONAL_ITER056S_BALANCED_PAIR_SECTOR_HAS_EXACT_TIDAL_CUBIC_SHAPE_BRIDGE`
   - iff all 8 held-out lanes, all 24 permutation tests, spatial-basis checks and negative controls pass exactly.

2. `SCIENTIFIC_FAIL_ITER056S_BALANCED_PAIR_CUBIC_SHAPE_HYPOTHESIS`
   - iff implementation/provenance are valid but any predicted exact identity fails.

3. `INVALID_IMPLEMENTATION_OR_PROVENANCE_ITER056S`
   - iff source basis, edge order, permutation action, fixed spatial basis or exact arithmetic implementation is wrong/incomplete.

## Interpretation ceiling

PASS establishes only a **conditional kinematic representation/invariant bridge**:

- the source-owned G2 balanced pair tensor is canonically a traceless symmetric tensor on the G2 sum-zero spatial subspace;
- it carries an exact cubic invariant;
- the G3/Iter040 H0 tidal eigenvalue shape occurs inside that pair sector.

PASS does **not** establish that a microscopic pair perturbation physically equals the G3 tidal Hessian on one realized geometry, does not identify amplitudes, `beta`, `kappa` or `c6`, does not derive Weyl curvature from the pair sector, does not select exact versus order-reduced dynamics, and does not establish a global micro→continuum map.

Theory established remains 0%; `c6` symbolic/unfixed; `beta=1` unauthorized.