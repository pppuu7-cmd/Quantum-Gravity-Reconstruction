# Iter053T orthogonal control matrix — frozen non-authoritative contract

Date: 2026-09-14

Status: **NON-AUTHORITATIVE CONTROL ONLY**. This contract cannot classify, reclassify, replace, pool evidence with, or modify either active Iter053T scientific gate. It is outcome-independent support work while the authoritative productions are non-terminal.

## Purpose

Run four independent low-cost controls in parallel to validate algebra/code-path facts that will be useful regardless of the terminal Iter053T outcomes.

## Frozen lanes

### STENCIL
Verify the exact moment conditions of the five-point first-derivative stencil used by `d2n.derivative5`:

`[-f(x+2h)+8f(x+h)-8f(x-h)+f(x-2h)]/(12h)`.

Required exact normalized stencil moments:
- m=0: 0
- m=1: 1
- m=2,3,4: 0
- m=5: -4

Hence the leading truncation term is `-h^4 f^(5)/30`.

### WEIGHT
Independently compute the constant-reduced-integrand Gauss-Jacobi double-weight fingerprint for the tensor-product `alpha=beta=4` rule. Frozen reference values from the prior analytic derivation are:
- GJ3 extra-weight suppression: `0.3063851988551639`
- GJ2->GJ3 relative drift of the extra-weight constant-integrand estimate: `0.2896878290952537`

Both must reproduce within `5e-13` absolute error.

### WRAPPER
Using frozen C0 perturbation object and source point `u=(0.05,-0.04,0.03,-0.02)`, instantiate `pert=CompactPerturbation(C_PERT[0])` and `pt=TransformPerturbation(pert,shear(0))`. Verify:
- `pt.base is pert`;
- `pt.base.jets(u)[0] = B(u) * pert.base.jets(u)[0]` to relative Frobenius residual `<=2e-12`;
- the legacy wrapped tensor differs nontrivially from the unfactored polynomial tensor by relative Frobenius difference `>=1e-3`.

### TENSOR
For a fixed determinant-one shear and fixed symmetric test tensors, verify the exact contraction identity

`(L^-1 H L^-T) : (L^T p L) = H:p`

to relative residual `<=1e-13`, and require a deliberately wrong congruence to differ by `>=1e-3`.

## Aggregate
All four lanes must be present, finite, and individually pass. Aggregate classification is only one of:
- `ORTHOGONAL_CONTROLS_PASS`
- `ORTHOGONAL_CONTROLS_INVALID`

Neither string is a scientific Iter053T PASS/FAIL.

## Interpretation ceiling

A PASS validates only the frozen algebra/stencil/object-wrapper controls. It does not use or authorize partial Iter053T numerical evidence, does not change either Iter053T preregistration, does not establish compact-support functional-variation closure, does not authorize a full replacement gate, and does not change any QGR claim lock. `theory established=0%`; `c6` remains symbolic/unfixed; `beta=1` remains unauthorized.