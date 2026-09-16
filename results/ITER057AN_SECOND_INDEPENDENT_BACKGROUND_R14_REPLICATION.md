# Iter057AN — second independent background R14 replication

Status: **TERMINAL SCOPED PASS — exact production independently reproduced**

Preregistration: `b40e9949932c9698a08a099bde8cfb920eb5feff`.
Candidate: `AL-R1-3` (prospectively selected independent additional finite-local R12 background; no coefficient/parity/S3 matching criterion).

## Windows independent reproduction authority

- production head: `1ebd5b3a5eb40b7f719e371baed548181e6894fa`
- Actions run: `35155313141`
- aggregate job: `105000595560`
- aggregate artifact: `10472087110`
- artifact digest: `sha256:0020947b85d14a0e202e52df84bc0ea5287fac41716eb9910b5d102b9e759595`
- scientific payload SHA256: `a40d06867eec92bd2b2d7b4f08a9eab318fcd52c2e26298b8125a53f032d2fd2`

The raw aggregate log, not CI color, is the scientific authority.

## Exact result

- `B_shape = (1456,1114)`
- `B_nnz = 81061`
- `O0_nonzero_count = 223`
- `rank(B) = 1114`
- `rank([B|-O0]) = 1115`
- `dim ker(B^T) = 342`
- `dim(ker(B^T) cap O0^perp) = 341`
- obstruction quotient dimension = **1**

Frozen controls passed exactly: baseline exact; complete unique 1114-column coverage; exact rational Flint rank; fixed direct controls at columns `0,557,1113`; normalized witness replay; rank increment <=1; no numerical tolerance.

Classification:

`PASS_SCOPED_ITER057AN_SECOND_INDEPENDENT_BACKGROUND_REPRODUCES_ONE_DIMENSIONAL_R14_OBSTRUCTION_CLASS`

## Interpretation lock

This reproduces the one-dimensional finite-local R14 compatibility obstruction on a second independent additional R12 background without refit. Together with the original AF realization and the first held-out replication, this is robustness evidence against a single-background accident. It is **not** an all-orders/global no-go theorem and does not establish the complete covariant Weyl^3 Euler-Lagrange tensor, quantum unitarity, regulator removal, UV completion, experimental confirmation, or new physics.

`c6` remains symbolic/unfixed. `beta=1` remains unauthorized. Theory established remains 0%. KMQGB `NEW_REQUIRED` remains unauthorized.
