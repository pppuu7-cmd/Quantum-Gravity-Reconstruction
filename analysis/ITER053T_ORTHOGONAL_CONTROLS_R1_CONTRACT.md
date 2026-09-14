# Iter053T orthogonal controls R1 — exact-reference non-authoritative retry

Date: 2026-09-14

Status: **PROSPECTIVELY FROZEN NON-AUTHORITATIVE CONTROL-ONLY RETRY**.

The original run `34792340429` remains terminal `ORTHOGONAL_CONTROLS_INVALID` because its WEIGHT lane used insufficiently precise copied reference digits. R1 changes only the independent reference representation; it does not change either active Iter053T scientific contract and cannot pool evidence with them.

## Exact WEIGHT reference derivation frozen before R1 execution

For the one-dimensional Jacobi weight `(1-z^2)^4`:

### GJ2
The exact Jacobi polynomial is proportional to `11 z^2 - 1`, so the two nodes obey `z^2=1/11` and equal weights suffice by symmetry. For a constant reduced integrand with one extra support factor, the one-dimensional suppression is exactly

`r2 = (1-1/11)^4 = 10000/14641`.

The four-dimensional tensor-product suppression is

`S2 = r2^4 = 10000000000000000 / 45949729863572161`

`= 0.217629135790148771261279540743...`.

### GJ3
The exact Jacobi polynomial is proportional to `z(13 z^2-3)`, so the nodes are `0, +/-sqrt(39)/13`, with side weight `1664/10395` and central weight `1024/2079`. The exact normalized one-dimensional extra-support ratio is

`r3 = 17980/24167`.

Thus the exact four-dimensional suppression is

`S3 = r3^4 = 104510217024160000 / 341107264278244321`

`= 0.306385198935282886141651590283...`.

The exact relative GJ2->GJ3 drift, using `S3` as the larger denominator, is

`D23 = (S3-S2)/S3`

`= 593856122131774300241121 / 2049986442286836800241121`

`= 0.289687829090862431311582933837...`.

## R1 frozen lanes

Same four independent lanes as the original control matrix: STENCIL, WEIGHT, WRAPPER, TENSOR. Only WEIGHT reference constants are replaced by the exact rational values above.

## Frozen R1 criteria

- STENCIL, WRAPPER, TENSOR: unchanged from the original contract.
- WEIGHT: computed SciPy GJ values must agree with exact rational `S2`, `S3`, and `D23` to absolute error `<=5e-13` each.
- all required outputs finite.
- aggregate requires all four lanes present and passing.

Terminal control-only classifications:
- `ORTHOGONAL_CONTROLS_R1_PASS`
- `ORTHOGONAL_CONTROLS_R1_INVALID`

## Interpretation ceiling

R1 remains non-authoritative support work. It cannot classify either scientific Iter053T gate, cannot reclassify Iter053R, cannot authorize the full A4+B2+C2 replacement, and cannot alter QGR claim locks.