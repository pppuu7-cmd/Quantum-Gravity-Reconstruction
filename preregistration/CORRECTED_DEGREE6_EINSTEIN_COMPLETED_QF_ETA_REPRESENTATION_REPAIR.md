# Prospective preregistration — eta-representation execution-only repair

Parent gate: `CORRECTED_DEGREE6_EINSTEIN_COMPLETED_QF_DEGREE_FLOW_ADJUDICATION`
Parent preregistration: `8a5e1e9186d8b8b81f401158b8ca04b38f05de66`
Blocked production: run `35308873605`, head `e0820a7df927f0f5ea5e52000819a63700a6d183`.

## Frozen diagnosis before repair

Both independent lanes fail at the same line constructing background eta because historical `b.ETA` is the diagonal signature vector `(-1,1,1,1)`, while the new helper incorrectly indexes it as a matrix with `b.ETA[i][j]`.

## Only authorized change

Replace only the eta background construction with the mathematically identical diagonal matrix representation derived from the frozen signature vector: entry `(i,j)` is constant `b.ETA[i]` when `i==j`, and zero otherwise.

No other implementation, scientific criterion, q ladder (`6..10`), R12 seed, geometry boundary, source operator, term decomposition, derivative-flow witness, Iter057AT target, sign, scale, normalization, threshold, classifier, or coefficient may change in this repair.

The repaired attempt is authoritative for this gate only if both independent lanes produce complete payloads and the pre-existing frozen aggregate criteria are applied unchanged. Green CI alone is not scientific PASS.

Claim locks remain unchanged: theory established 0%; no experimental confirmation; beta=1 unauthorized; c6 symbolic/unfixed; corrected degree-eight/Q10 locked; finite/symmetry-reduced panels are not global theorems; no quantum-unitarity, UV-completion, physical-weight, KMQGB NEW_REQUIRED, or new-physics claim is authorized.
