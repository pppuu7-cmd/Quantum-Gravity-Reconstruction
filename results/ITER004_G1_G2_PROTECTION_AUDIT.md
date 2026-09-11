# QGR Iter004 G1-G2 — Mass-Protection and Symmetry-Enhancement Audit

Date: 2026-09-11
Status: `M2_FAIL_SCOPED / M5_BLOCKED_SINGLE_CELL`

## G1 — refinement-fixed does not imply stationary

The surviving TT-like transfer found in Iter003 is

`T=I_2`,

with exact idempotency `T^2=T`.

This is a kinematic refinement statement. The current refinement equation contains no onsite mass coefficient.

An explicit logical counterexample is immediate: candidate dynamics with `m^2=0`, `m^2=1`, or any other value all retain exactly the same kinematic `T=I_2` refinement map unless an additional rule ties refinement to the dynamical stationary condition.

Therefore current CCRC refinement alone does **not** imply

`uniform refinement-fixed q => stationary physical q`.

M2 classification:

`FAIL_SCOPED_CURRENT_REFINEMENT_DATA_DO_NOT_FORCE_MASSLESSNESS`.

This does not prove refinement can never protect mass. It proves the current QGR refinement object is insufficient without an additional dynamical/refinement theorem.

## G2 — continuous Lorentz stabilizer exists, but not as exact B4 automorphism

The pair-incidence bilinear form is

`C=J-I`,

with signature `(1,3)` up to overall sign.

Its continuous real stabilizer satisfies

`L^T C L=C`.

At infinitesimal level,

`X^T C + C X=0`.

The exact linear system on the 16 entries of `X` has rank `10`, leaving a six-dimensional Lie algebra. This is the expected dimension of the Lorentz algebra `so(1,3)`.

However the exact automorphism group of the finite Boolean poset `B_4` is determined entirely by permutations of its four atoms. Therefore

`Aut(B_4)=S_4`,

with exactly `4!=24` elements.

Every such permutation preserves `C`, but there is no continuous one-parameter subgroup among exact finite-poset automorphisms.

M5 single-cell classification:

`BLOCKED_CONTINUOUS_O1_3_STABILIZER_EXISTS_FOR_EMERGENT_BILINEAR_FORM_BUT_IS_NOT_REALIZED_AS_EXACT_FINITE_B4_AUTOMORPHISM`.

## Scientific consequence

The model now exhibits a precise symmetry-enhancement problem rather than a vague requirement for Lorentz invariance:

`finite microscopic automorphisms S4 -> ? refinement/coarse limit -> continuous local O(1,3)`.

This gap must be closed by an actual refinement theorem or an explicitly derived coarse representation. Merely observing that `C` has Lorentzian signature does not establish local Lorentz symmetry.

## Updated mechanism matrix

- M1 local frame/constraint redundancy: `PARTIAL`, current form does not forbid `q^2`.
- M2 refinement fixed-background protection: `FAIL_SCOPED` in current form.
- M3 microscopic Goldstone shift: `FAIL_SCOPED` in current ontology.
- M4 cohomological origin alone: `FAIL_SCOPED` as mass protection.
- M5 symmetry enhancement under refinement: `BLOCKED / ACTIVE HIGH-VALUE FRONT`.

No valid mass-protection mechanism has yet passed.

## Next gate

`QGR-ITER004-G3-REFINEMENT-SYMMETRY-ENHANCEMENT`

Construct the smallest multi-cell/refined Boolean complex and determine the representation induced on coarse pair observables. Test whether the effective transformation group grows beyond the microscopic finite `S_4` action in a controlled sequence and whether its Lie closure approaches the six generators preserving `C`.

A numerical appearance of approximate isotropy is insufficient; the mapping between microscopic transformations and the coarse continuous generators must be explicit.

Reproducibility: `code/qgr_iter004_g1_g2_protection_audit.py`.
