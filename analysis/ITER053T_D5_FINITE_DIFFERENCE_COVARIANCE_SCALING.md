# D5 finite-difference covariance scaling fingerprint for Iter053T

Date: 2026-09-14
Status: analytic implementation audit aid. No partial substantive values from active Iter053T productions are used. This note does not alter the frozen companion thresholds or imply a PASS/FAIL.

## Question

The active nodewise Iter053T companion evaluates the numerical Weyl3 variational tensor at three frozen double-divergence coordinate steps

`h = 1e-3, 5e-4, 2.5e-4`

under non-orthogonal determinant-one shears.

Even when the exact continuum `H5` is a covariant tensor density, a coordinate-axis finite-difference approximation need not transform exactly at finite `h`. What scaling should an ordinary truncation-induced covariance defect have for the actual repository implementation?

## Repository stencil

`qgr_iter051c_d2n_near_null.py` defines

`derivative5(func,x,axis,h)`

by the standard symmetric five-point first-derivative stencil

`[f(x-2h)-8 f(x-h)+8 f(x+h)-f(x+2h)]/(12 h)`.

Expanding a smooth scalar/vector/tensor component in Taylor series gives

`D_h f = f' - (h^4/30) f^(5) - (h^6/252) f^(7) + O(h^8)`.

All terms of orders `h`, `h^2`, and `h^3` in the derivative error cancel; the leading truncation error is fourth order.

## Nested double divergence remains fourth order

The numerical `direct_D5` construction first computes a covariant first divergence of the exact algebraic `P` tensor with coordinate derivatives supplied by `derivative5`. Schematically,

`R_h = nabla P + h^4 E1[P,g] + O(h^6)`.

It then differentiates `R_h` with the same five-point stencil and adds the exact-at-node connection terms required for the second covariant divergence. For a smooth metric/P field over the stencil neighborhood,

`D5_h = D5_exact + h^4 E2[P,g] + O(h^6)`.

The nesting does not introduce an `O(h^2)` term: differentiating the existing `h^4 E1` contribution preserves its explicit `h^4` factor, while the outer stencil contributes its own `O(h^4)` error.

The full numerical variational tensor is

`H5_h = A + I - 2 sqrt(-g) D5_h`.

`A` and `I` are evaluated algebraically at the central point, so the coordinate-step truncation is localized to the `D5` contribution.

## Why finite-h coordinate covariance is not exact

For a constant linear coordinate transform `x=L y`, the exact continuum `D5`/`H5` transforms tensorially.

However, the leading stencil-error operator is built from fifth derivatives along the coordinate axes. Under a non-orthogonal shear, an x-axis finite-difference direction becomes a linear combination of y-coordinate directions. The separate axis-aligned fifth-derivative error terms therefore do not themselves form the exact transformed tensor-density law at finite `h`.

Consequently, after exact continuum pieces cancel in a base/transformed covariance comparison, an ordinary truncation-dominated discrepancy has the form

`Delta_cov(h) = C(L,g,P,u) h^4 + O(h^6) + roundoff/conditioning terms`.

The coefficient depends on the shear, metric, P tensor and node. The exponent does not, as long as the smooth-stencil regime applies and no lower-order implementation defect is present.

## Frozen h-ladder fingerprint

The companion gate uses successive halvings:

`1e-3 -> 5e-4 -> 2.5e-4`.

If a node/lane is in the clean leading-truncation regime, the expected covariance-error ratios are therefore approximately

`Delta(1e-3) / Delta(5e-4) ~= 2^4 = 16`,

`Delta(5e-4) / Delta(2.5e-4) ~= 16`,

and

`Delta(1e-3) / Delta(2.5e-4) ~= 4^4 = 256`.

This is a diagnostic prediction only. The active preregistration does not require these ratios, so they must not be turned into post-hoc PASS criteria.

## Interpretation of possible terminal patterns

After the companion run is terminal, the frozen verdict must be applied first. Only then may this scaling fingerprint help localize behavior.

### Pattern A — all frozen lanes PASS and residuals decrease roughly as h^4

This is consistent with exact continuum covariance plus ordinary axis-stencil truncation under shear.

### Pattern B — all frozen lanes PASS but residuals reach an h-independent floor

This can still be consistent with the frozen scoped PASS if the floor remains below threshold. Candidate sources include floating-point cancellation, conditioning, complex-step/algebraic evaluation noise or a higher-level implementation floor. It would justify a later independent numerical audit only if scientifically needed; it would not invalidate the frozen PASS by itself.

### Pattern C — covariance residual remains O(1) or nearly h-independent well above threshold

That would not look like ordinary five-point truncation and would support a mapped-object/contraction/transformation defect within the frozen gate scope.

### Pattern D — apparent divergence as h decreases

This would suggest roundoff/catastrophic cancellation, invalid stencil conditioning or another numerical implementation issue and should be separated from a physical non-covariance claim.

## Relation to terminal Iter053S evidence

Iter053S already established pointwise H5 covariance on its separate frozen probe panel with finest-step H5 residual of order `3.85e-8`. That historical terminal result is qualitatively compatible with a small finite-difference covariance floor/error, but it cannot be pooled as scored evidence for the active all-81-node companion gate.

## Claim ceiling

- no active Iter053T scientific outcome is inferred here;
- no companion threshold is changed;
- no node or hstep may be selected after the fact;
- Iter053R remains historical scientific FAIL;
- no full corrected compact-support certificate is claimed;
- `c6` remains symbolic/unfixed;
- `beta=1` remains unauthorized;
- theory established remains `0%`.
