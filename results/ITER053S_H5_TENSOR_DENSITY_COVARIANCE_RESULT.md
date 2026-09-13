# Iter053S — H5 tensor-density covariance localization result

Date: 2026-09-14

## Gate

`ITER053S-H5-TENSOR-DENSITY-COVARIANCE-LOCALIZATION`

This gate was prospectively frozen after the terminal Iter053R scientific FAIL. It does not rerun, replace, or reclassify Iter053R.

## Authority

- preregistration: `71c077d34dba1749d0d34dc6dd0173648e82f60f`
- implementation: `60532767595c38e92fbc9a8a35bf9b0c59b3600c`
- primary workflow/production head: `514c4785ad500299a797281cb39a2eee7ffa7f0c`
- primary run: `34787788933`
- substantive artifacts: 1 algebraic control + 12 independent pointwise probes, all terminal successful

The original primary-run aggregate did not execute the classifier because its aggregate job environment omitted NumPy. No substantive lane was recomputed. A separate infrastructure-only recovery workflow downloaded exactly the 13 frozen artifacts from run `34787788933`, installed the classifier dependencies, and reran the unchanged frozen aggregate:

- aggregate-recovery head: `91086222bb20ec665a653dabde3c3811f98a09f1`
- aggregate-recovery run: `34787959341`
- aggregate job: `103806786112`
- summary artifact: `10326344492`
- summary artifact digest: `sha256:ded3e5fa26af5754033103790384ad12a275ebaeaf0e47c1de1d544950119ddd`

## Frozen terminal classification

`ITER053S_POINTWISE_H5_TENSOR_DENSITY_COVARIANCE_CONFIRMED`

## Aggregate evidence

All frozen predicates required for the covariance-confirmed classification passed:

- complete: `true`
- valid: `true`
- probe count: `12/12`
- direct reference density covariance: PASS
- algebraic `A+I` tensor-density covariance: PASS
- derivative-density `D5` covariance: PASS
- total `H5` tensor-density covariance: PASS
- pointwise `H:h` contraction covariance: PASS

Worst frozen finest-step residuals:

- direct density: `1.7620525013236046e-13` vs threshold `2e-6`
- algebraic `A+I`: `1.1234468712818426e-14` vs threshold `2e-5`
- derivative-density `D5`: `3.834671241411767e-08` vs threshold `2e-3`
- total `H5`: `3.8507299553315486e-08` vs threshold `2e-3`
- `H:h` contraction: `5.67809665333841e-08` vs threshold `2e-3`

The frozen algebraic negative control also behaved as required: the correct tensor-density contraction identity was satisfied near machine precision, while the deliberately wrong congruence produced order-one disagreement.

## Step behavior

The covariance residuals did not strictly decrease as the coordinate finite-difference step was reduced from `1e-3` to `2.5e-4`; at the smallest step they rose to the `~2e-8–4e-8` level. This does not affect the frozen PASS classification because every finest-step residual is still roughly five orders of magnitude below the `2e-3` target. The pattern is consistent with entering finite-difference roundoff/cancellation rather than a covariance defect, but that interpretation is not itself a new theorem.

## Scientific consequence

The pointwise numerical object

`H5 = A + I - 2 sqrt(-g) D5`

obeys the required tensor-density transformation law under both frozen determinant-one Iter053R C shears at both preregistered probe points and all three preregistered coordinate derivative steps.

Therefore the terminal Iter053R C-lane failure (`~0.6925` weighted-bulk covariance residual while direct covariance was `~1e-12`) is **not localized to pointwise H5 object identity or its A+I/D5 tensor transformation** within this tested scope.

The highest-information remaining localization is the transformed weighted support-parameter / Gauss-Jacobi pushforward representation used by Iter053R. A new prospective gate may test whether the weighted factorization and quadrature nodes represent the same physical compact-support integral after a general determinant-one shear.

## Historical integrity

Iter053R remains permanently:

`SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`

A later pushforward/quadrature repair or replacement PASS would be a distinct prospectively defined result, not a rewrite of Iter053R.

## Claim ceiling

This is a pointwise numerical tensor-density covariance certificate only. It does not establish the integrated compact-support Weyl3 functional-variation identity, a global six-derivative EOM theorem, quantum amplitude/measure, quantum consistency/unitarity, RG/UV completion, GR recovery, a physical value of `c6`, `beta=1`, new physics, or theory establishment. `theory established = 0%` remains locked.