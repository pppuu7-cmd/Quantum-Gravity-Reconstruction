# Iter051C-D1 — Full-EOM assembly term localization diagnostic

Date: 2026-09-13
Gate: `ITER051C-D1-ASSEMBLY-TERM-LOCALIZATION`

## Prospective status
This diagnostic is preregistered after the terminal frozen G51C result `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY` and before D1 implementation/production. It does not rewrite G51C and is not a replacement EOM certificate.

## Question
Which linear assembly convention among the already independently computed pieces causes the exact G48 reduced-Euler–Lagrange mismatch?

For each witness define reduced 3-vectors obtained from the G51C tensors by the same frozen chain rule:
- `a = reduce(A)`;
- `i = reduce(I)`, `I = sqrt(-g) sym(P.R)`;
- `j = reduce(J)`, `J = sqrt(-g) D` before any factor of 2;
- exact target `e = (E_N,E_a,E_b)` from the independently derived G48 formulas.

The historical frozen G51C hypothesis is `e ?= a + i + 2 j` and remains failed regardless of D1 outcome.

## Frozen witnesses — 6 parallel lanes
Use exactly the G51C/G48 pairs and witness times:
`(-1/2,1/3) @ 1/2`, `(1/4,3/4) @ 2/3`, `(-2/3,1/2) @ 1`, `(2/5,-1/5) @ 3/2`, `(3/2,1/4) @ 2`, `(-1/4,5/6) @ 3`.

Each lane evaluates `A,I,J` at `h=[1e-3,5e-4,2.5e-4]`, reports the finest reduced vectors and final-step changes. Required controls:
- Lorentz signature valid on frozen stencil;
- inverse residual <= `2e-11`;
- every exact target component nonzero (`>1e-10` absolute);
- final-step relative change of each of reduced `a,i,j` <= `5e-4`.

## Frozen aggregate diagnostics
Concatenate all 18 reduced component equations into `M c = e`, with columns `a,i,j` and coefficient vector `c=(c_A,c_I,c_J)`.

Report only; do not use the fit as replacement authority:
- matrix rank and condition number;
- least-squares coefficient vector;
- relative global fit residual;
- six leave-one-lane-out coefficient vectors and their maximum relative spread;
- residuals of frozen reference hypotheses:
  - H0 historical: `(1,1,2)`;
  - H1: `(1,1,-2)`;
  - H2: `(1,-1,2)`;
  - H3: `(1,-1,-2)`;
  - H4 global sign: `(-1,-1,-2)`.

Diagnostic localization class requires all 6 valid lane artifacts, rank=3, condition number <= `1e6`, global fit residual <= `1e-5`, and leave-one-lane-out coefficient spread <= `5e-4`:
`DIAGNOSTIC_LOCALIZED_STABLE_G51C_ASSEMBLY_COEFFICIENT_PATTERN`.
Otherwise:
`DIAGNOSTIC_INCONCLUSIVE_G51C_ASSEMBLY_TERM_LOCALIZATION`.
Missing/invalid controls:
`CONTROL_INVALID_G51C_D1`.

## Interpretation lock
Even a stable fitted coefficient pattern is **diagnostic only**. It cannot establish the correct covariant Weyl^3 EOM or authorize changing the failed G51C formula. A corrected replacement assembly requires an independent variational derivation of sign/index/coefficient conventions, a new prospective preregistration, and held-out validation not used to infer the correction.

`c6` remains symbolic/unfixed; `beta=1` unauthorized; theory established remains `0%`; no experimental, positivity/unitarity, or KMQGB `NEW_REQUIRED` claim follows.
