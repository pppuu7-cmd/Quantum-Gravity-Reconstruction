# Iter056O preregistration — G3 Weyl3 parent→child local action-kernel refinement

Date: 2026-09-14

Gate: `ITER056O-G3-WEYL3-PARENT-CHILD-LOCAL-ACTION-KERNEL-REFINEMENT`

## Parent authority

- Iter056M: no pre-existing single object simultaneously supplied source identity, treatment blindness, cross-level structure and Weyl3 sensitivity.
- Iter056N: the physical lattice spacing `h` used by Iter054S transport and Iter040/041 Weyl-response calculations is already the same G3 finite-geometry scale; what is missing is a Weyl3 parent→children rule.
- Original G3 / Iter040 authority supplies the same weak-static H0 tidal realization and finite-cell Weyl3 proxy.
- The continuum candidate action already contains the local Weyl3 density `sqrt(|g|) W3`, with `c6` retained as an external symbolic multiplier.

This gate constructs only the **geometric/action-kernel** cross-level object. It does not construct a microscopic quantum phase, history amplitude, measure, or dynamical treatment selector.

## Frozen realization

Use exactly the G3/H0 weak-static tidal family

`H0 = diag(1,1,-2)`

`Phi(y) = (kappa/2) y_spatial^T H0 y_spatial`

with frozen `kappa=0.08`, the same `RM/RMI`, `E`, six-generator Lorentz connection, torsion parallelogram solve, holonomy-log curvature construction and Weyl proxy used by the existing G3/Iter040 line.

No new field component, background deformation, source strength, branch weight, `beta`, `c6` value, or dynamical treatment may be introduced.

## Frozen translated finite-cell object

For physical cell base `b`, cell side `h`, define the translated G3 cell by evaluating the existing tetrad on index points

`x_index = b/h + n`,

where `n` is the local unit-cell index. This is the same physical-coordinate convention already used in Iter054S.

From the solved local connection, construct the same G3 holonomy-log curvature and Weyl-cubic proxy `W3_h(b)`.

Define the local finite-cell Weyl3 action-kernel contribution

`A_h(b) = h^4 * sqrt(abs(det(g_h(b)))) * W3_h(b)`.

The `h^4` factor is the coordinate 4-cell volume and `sqrt(abs(det g))` is the already-authorized local action density measure. `c6` is intentionally omitted because it would multiply parent and children uniformly and remains symbolic/unfixed.

Freeze the metric determinant at the same physical cell base `b` used to anchor the curvature proxy; do not change quadrature convention after output.

## Frozen parent→children partition

A parent 4-cell of side `H` at base `b` is subdivided into exactly 16 children of side `h=H/2`, with child bases

`b_q = b + (H/2) q`, `q in {0,1}^4`.

Define

`A_parent(H,b) = A_H(b)`

and

`A_children(H,b) = sum_{q in {0,1}^4} A_{H/2}(b_q)`.

This uses the exact geometric 2×2×2×2 partition; no fitted child weights exist.

## Frozen panel

Two physical bases inherited from Iter054S:

- `B0=(0,0,0,0)`
- `B1=(0.10,0.10,0.10,0.10)`

Two parent scales:

- `H=0.10` with children `h=0.05`
- `H=0.05` with children `h=0.025`

This gives four independent parent/child scientific lanes.

The H=0.10 → 0.05 split directly overlaps the already-authorized common G3 resolution points identified by Iter056N.

## Frozen validity controls

Every required local finite-cell solve must satisfy:

- torsion residual norm `<3e-9`;
- minimum connection-solve Jacobian singular value `>1e-8`;
- Lorentz/metric error `<1e-7`;
- finite Weyl norm and finite Weyl-cubic proxy;
- nonzero parent/children action-kernel magnitude sufficient to form the frozen relative residual (`max(|A_parent|,|A_children|) > 1e-14`).

A missing/invalid child invalidates the whole lane; no child may be dropped.

## Frozen scientific residual

For each lane define

`R(H,b) = |A_children(H,b)-A_parent(H,b)| / max(|A_children(H,b)|, |A_parent(H,b)|)`.

For each base, PASS requires:

1. `R(0.05,b) < R(0.10,b)`;
2. finest `R(0.05,b) < 0.10`.

These thresholds are frozen before computation. They test finite-panel convergence toward local action additivity; they do not assert exact finite-cell equality.

## Frozen controls

### Volume-weight negative control

For every H=0.10 lane, form a deliberately wrong child sum using parent volume `H^4` for each child instead of child volume `(H/2)^4`.

Require its discrepancy from the correctly weighted child sum, normalized by the correct child magnitude, to exceed `5.0`.

This verifies that PASS cannot be obtained by ignoring the physical 4-volume scaling.

### Missing-child negative control

For every lane, omit the lexicographically last child from the correctly weighted sum. Require

`|A_children-A_children_missing| / max(|A_children|,1e-30) > 0.02`.

This verifies sensitivity to actual child content rather than a tautological normalization.

## Frozen parallelization

Run the four parent/child lanes independently with `fail-fast:false`:

- B0-H0.10
- B0-H0.05
- B1-H0.10
- B1-H0.05

Aggregate only after all four lane artifacts are terminal and provenance-compatible.

## Frozen terminal classifications

1. `PASS_SCOPED_ITER056O_G3_WEYL3_PARENT_CHILD_ACTION_KERNEL_REFINEMENT`
   - iff all four lanes are valid, both bases satisfy the frozen residual contraction/final threshold, and all negative controls pass.

2. `SCIENTIFIC_FAIL_ITER056O_G3_WEYL3_PARENT_CHILD_ACTION_KERNEL_REFINEMENT`
   - iff implementation/provenance/controls are valid but one or more frozen scientific residual predicates fail.

3. `INVALID_IMPLEMENTATION_OR_CONTROL_ITER056O`
   - wrong realization, wrong partition, missing child/lane, altered quadrature convention, invalid local solve, failed negative control, mixed provenance, or other object/procedure error.

## Interpretation ceiling

PASS would establish only a finite-panel parent→children refinement certificate for the **local geometric Weyl3 action kernel** on the frozen G3/H0 weak-tidal family.

It would not establish:

- a microscopic history/amplitude/measure→continuum map;
- physical branch phases `S_alpha` or Koopman maps `U_alpha`;
- global interacting measure/regulator removal;
- a microscopic→IR identity fixing `c6`;
- exact versus order-reduced treatment selection;
- exact-theory hyperbolicity or all-order convergence;
- quantum unitarity, UV completion, full GR recovery, experiment, new physics, or QGR correctness.

`c6` remains symbolic/unfixed; `beta=1` remains unauthorized; theory established remains 0%.