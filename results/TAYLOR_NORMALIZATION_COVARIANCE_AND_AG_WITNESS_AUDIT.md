# Exact Taylor-normalization covariance and AG-witness audit

Date: 2026-09-16

Status: **INDEPENDENT REPRODUCIBLE EXACT PASS — RESEARCH-BRANCH AUDIT, NOT A REWRITE OF HISTORICAL MAIN RESULTS**

Branch point: `bc09581da51fc9ad0e04a4cc8b1eb6a66def60dd` on `main`. At that point the raw/mixed-convention obstruction line had terminalized Iter057AI and opened Iter057AJ. Historical Iter057AF/AG/AH/AI results remain preserved exactly as recorded.

## Question

Determine whether the Einstein-seed principal affine complex is representation-covariant between ordinary monomial coefficients and normalized Taylor coefficients, and whether the canonical Iter057AG dual obstruction witness still produces a contradiction after all matrix, RHS and left-null objects are transformed consistently into the same Taylor convention.

## Exact normalization theorem

For a pure degree-d trace-reversed correction, let

- ordinary monomial coefficients satisfy `q(x)=sum_beta c_beta x^beta`,
- normalized Taylor coefficients satisfy `q(x)=sum_beta R_beta x^beta/beta!`, so `R_beta=beta! c_beta`.

Let `D_col` be diagonal with column entry `beta!` and `D_row` diagonal with the factorial of the target row multi-index. Direct exact differentiation gives

`M_normalized = D_row * M_ordinary * D_col^{-1}`,

`r_normalized = D_row * r_ordinary`,

and, if `y_normalized^T M_normalized=0`, then

`y_ordinary^T = y_normalized^T D_row`

satisfies `y_ordinary^T M_ordinary=0`.

Therefore affine compatibility is representation invariant only when matrix, RHS and left-null vectors are transformed consistently.

Concrete entries:

- gauge: ordinary coefficient `eta_m*(alpha_m+1)` becomes normalized coefficient `eta_m`;
- field `-1/2 Box`: ordinary coefficient `-eta_m*(alpha_m+2)*(alpha_m+1)/2` becomes normalized coefficient `-eta_m/2`.

This identity was machine-checked with exact rational arithmetic for every even correction degree `d=4,6,...,24`. All operator-entry checks and all transformed raw Bianchi annihilation checks are exactly zero-failure.

## Canonical R4..R14 replay

The actual frozen seed sequence was replayed through target correction degrees 4, 6, 8, 10, 12 and 14.

For every layer, the independently recomputed ordinary nonlinear Einstein residual multiplied by the target multi-index factorial reproduces the normalized RHS coefficient-for-coefficient, with mismatch count zero. The normalized Bianchi/Noether compatibility count is zero at every layer.

If the same ordinary monomial RHS is intentionally fed directly into the normalized Taylor matrix/left family, the spurious nonzero compatibility counts are

`3, 15, 39, 79, 139, 223`

for `R4, R6, R8, R10, R12, R14` respectively.

Thus the historical Iter057AC count 223 is the degree-14 member of a deterministic mixed-convention false-obstruction sequence, not a new feature unique to degree 14.

Classification:

`PASS_INDEPENDENT_EXACT_TAYLOR_NORMALIZATION_COVARIANCE_FOR_EINSTEIN_SEED_PRINCIPAL_COMPLEX_AND_R4_TO_R14_REPLAY`

Scientific payload SHA-256:

`0e93de765a93caafcf90e657a793b3066ded8756512ecafbae9a45a91f108552`

Complete theorem-result JSON SHA-256:

`ae70ad9cb735d12f1120de237a97f237f339ae47d53d8e5a77774ee1e8402398`

## Canonical Iter057AG witness cross-check

The exact canonical Iter057AG witness `y` frozen at `79f447491834eaa67c2516d50433be619f098dd2` has 56 nonzero compatibility coordinates and was not rescaled, reordered or modified.

Using the historical mixed-convention obstruction reconstructed from the same canonical R12 seed:

- `O_raw` nonzero count = 223;
- exact `y^T O_raw = 1`.

This independently reproduces the terminal Iter057AG contradiction value.

Using the factorial-normalized RHS in the same normalized Taylor system:

- `O_normalized` nonzero count = 0;
- exact `y^T O_normalized = 0`.

Classification:

`PASS_INDEPENDENT_EXACT_AG_DUAL_WITNESS_NULLIFIED_BY_CONSISTENT_TAYLOR_NORMALIZATION`

Cross-check JSON SHA-256:

`98b57d4cce31c01c560d8695e6d26a40407240484c4abdd742fdb01fc1ef4865`

This does not invalidate the algebra of Iter057AG/AH/AI on their inherited raw/mixed object. It shows that their exact certificate is a certificate for that representation-mismatched affine object; the same canonical witness does not obstruct the consistently normalized Iter057AC scientific object.

## Reproducibility

The normalization theorem was executed twice in separate clean processes and produced byte-identical JSON. A self-contained bundle was then unpacked in a fresh directory. The theorem output reproduced byte-for-byte, and the AG witness cross-check independently reproduced byte-for-byte.

Self-contained reproduction ZIP SHA-256:

`6b250fdd464ba5b4062e459c8ab15d46d9936531a5911c9e970ee4d6331f35d0`

## Consequence

The clean corrective path is to prospectively freeze one coefficient convention for future seed gates and apply the diagonal basis conversion to every affine matrix, RHS and left-null certificate consistently. On the normalized convention already used by the canonical correction data, the corrected R14 gate remains compatible and its previously reproduced 721-coefficient particular remains the relevant provisional continuation.

A direct Weyl3 source-degree-10 computation on the corrected R14 background was attempted as the next physics-facing gate, but the straightforward unreduced tensor evaluator exceeded the current local resource gate before completion. No source-degree-10 claim is made from that partial run.

## Scope ceiling

This is an exact representation/correctness theorem for the finite local Einstein-seed principal affine complex plus finite canonical replays. It does not establish all-orders nonlinear convergence, global/asymptotic existence, physical characteristics, strong hyperbolicity, ghost/stability claims, quantum unitarity, regulator removal, a global interacting measure, UV completion, experimental confirmation, new physics or QGR correctness.

`c6` remains symbolic/unfixed, `beta=1` remains unauthorized, and theory-established remains `0%`.
