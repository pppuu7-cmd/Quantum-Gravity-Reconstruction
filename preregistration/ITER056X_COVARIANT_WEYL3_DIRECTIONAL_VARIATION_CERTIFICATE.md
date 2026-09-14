# Iter056X preregistration — covariant Weyl3 directional-variation certificate

Date: 2026-09-15
Gate: `ITER056X-COVARIANT-WEYL3-DIRECTIONAL-VARIATION-CERTIFICATE`

## Motivation

Iter056W closes the balanced-pair refinement route at a missing source-owned microscopic parent-to-child tensor map. The next gate returns to the standing priority: a genuinely four-dimensional covariant certificate for the variation of the local operator

`S_W3[g] = c6 ∫ d^4x sqrt(-g) I3`,

with

`I3 = C_{mu nu}^{  rho sigma} C_{rho sigma}^{  alpha beta} C_{alpha beta}^{  mu nu}`

(or the repository's canonically equivalent Weyl-cubic contraction), keeping `c6` symbolic and unfixed.

This gate must not use a third static/spherical symmetry reduction.

## Frozen object

Construct a manifestly covariant directional variation under a compactly supported symmetric test tensor `h_{mu nu}`:

`g_{mu nu}(epsilon)=g_{mu nu}+epsilon h_{mu nu}`,

and certify

`d/d epsilon S_W3[g+epsilon h]|_{epsilon=0}`

as a covariant bulk term plus an explicitly identified boundary/divergence term. If integration by parts is used, every derivative transfer must be explicit enough to identify the differential order of the bulk Euler-Lagrange response.

`c6` remains a global symbolic multiplier throughout.

## Frozen requirements

A. **Determinant variation.** Include the exact variation of `sqrt(-g)` with sign/index convention stated.

B. **Weyl variation.** Derive the variation of the Weyl tensor from the metric/Riemann/Ricci/scalar variations, rather than importing a symmetry-reduced Weyl response.

C. **Covariant integration by parts.** Separate the compact-support/boundary term from the bulk response without assuming a particular coordinate ansatz.

D. **Bulk response tensor.** Produce an explicit covariant tensor expression `E^(W3)_{mu nu}` or an equivalent directional-variation kernel such that

`delta S_W3 = c6 ∫ sqrt(-g) E^(W3)_{mu nu} h^{mu nu} + boundary`

within the declared index convention.

E. **Highest-derivative accounting.** Identify the highest metric-derivative order in the bulk response after covariant integrations by parts. Do not infer the EOM order solely from the EFT mass dimension/six-derivative operator label.

F. **Diffeomorphism identity control.** Check the covariant Noether identity/divergence constraint expected from diffeomorphism invariance, at least algebraically/formally at the tensor-expression level.

G. **Independent controls.** Include at minimum:
1. conformally flat control `C=0`, for which the Weyl-cubic first variation must vanish;
2. constant overall symbolic rescaling control sufficient to catch missing determinant/index-raising contributions;
3. agreement, only as a downstream control, with at least one already-authorized symmetry-reduced/weak-field response when specialized after the covariant derivation.

H. **No coefficient/treatment promotion.** The gate may not fix `c6`, set `beta=1`, choose exact vs order-reduced physical dynamics, infer quantum unitarity, or promote a finite control to a global theorem.

## Frozen terminal classifications

Maximum PASS:

`PASS_SCOPED_ITER056X_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_CERTIFIED__C6_SYMBOLIC_UNFIXED`

BLOCKED if the exact covariant tensor object cannot be represented/verified with current source and symbolic infrastructure without adding an unregistered identity:

`BLOCKED_OBJECT_DEFINITION_ITER056X_COVARIANT_WEYL3_VARIATION_CERTIFICATE_NOT_YET_EXECUTABLE`

Scientific FAIL if a fully specified implementation satisfying A-H produces a reproducible contradiction in one of the frozen exact controls:

`SCIENTIFIC_FAIL_ITER056X_COVARIANT_WEYL3_VARIATION_CONTROL_FAILURE`

INVALID if provenance, conventions, or frozen control definitions are incomplete:

`INVALID_ITER056X_COVARIANT_WEYL3_VARIATION_PROVENANCE_OR_CONVENTION_INCOMPLETE`

## Orchestration lock

1. Do not use a third static-spherical or other repetitive symmetry reduction as the primary derivation.
2. A symmetry-reduced sector may appear only after the covariant derivation as an independent control.
3. Do not weaken requirements or alter contractions after observing outputs.
4. If symbolic expansion is technically too large, preserve the exact tensor/operator representation rather than substituting sampled numerical agreement.
5. Only launch GitHub Actions after an exact implementation and frozen controls exist; green CI alone is not scientific PASS.

## Claim locks

Theory established remains `0%`; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; finite/symmetry-reduced panels are not global theorems; G45 does not prove absolute energy positivity/quantum unitarity; G35-G37 distant roots do not authorize physical weights; KMQGB `NEW_REQUIRED` unauthorized.