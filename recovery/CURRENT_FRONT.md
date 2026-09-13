# QGR Current Research Front

Updated: 2026-09-14
Primary active gate: `Iter053S / H5 tensor-density covariance localization`
Project phase: `MODEL_CONSTRUCTION / WEYL3 COVARIANCE IMPLEMENTATION LOCALIZATION`

## Canonical status

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established as a global theorem: **false**.
- Transition to quantum amplitude/measure closure: **not authorized**.

GitHub main + terminal Actions/results are authoritative. Older recovery text that described Iter053 retry as in progress or Iter053R as unimplemented is superseded by the terminal records below.

## Preserved historical failures

- G51C run `34741060700`: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, 12/18 PASS.
- G51C-D2 run `34741924103`: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS.

Neither is rewritten by later replacement gates.

## Iter052 — terminal genuinely-4D scoped PASS

Run `34748813339`; aggregate job `103702164522`; artifact `10315226969`; digest `sha256:b4b8c4b75046541f25b6a5f3f469e2d59e94c2b6571a6f1645b6e94f53f82009`; result commit `a4ef2219c60d55dc0913e1a7c696ed949028c7bc`.

Classification: `PASS_SCOPED_ITER052_WEYL3_4D_COVARIANT_DIRECTIONAL_VARIATION_CERTIFICATE`, 12/12 valid PASS. Finite computational certificate only.

## Iter053 original gate — historical authority preserved

Initial production preregistration `bb0b755f25f14b89dd44b6f16da309d0d0796d05`, run `34750610751`.

Permanent original classification: `ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL` because frozen C lanes hit hosted-runner wall-clock cancellation.

### Fresh original-contract retry — terminal

Wall-clock-only repair `4e95a8dbba3967d18f86206681bbfda46b54699e`; retry head `cf3466b3f0394952c384f7cfcc5bc445e7bbd4b5`; run `34769958632`; aggregate job `103800868498`; summary artifact `10325874510`; digest `sha256:ed377d0dad4958eda95992db0efc6cfa4808739befcacfedbc377a8b1fd07b3e`.

Terminal classification: **`ITER053_IMPLEMENTATION_OR_CONTROL_INVALID`**.

All 8 artifacts were present, but only 6 were control-valid and 2 passed. The retry supplies no scientific PASS/FAIL closure credit and is not pooled with the first production. Durable terminal note: `results/ITER053_FRESH_RETRY_TERMINAL.md`.

## Diagnostic chain before Iter053R

- QD `34770383463`: `PASS_DIAGNOSTIC_ITER053_OUTER_BOX_QUADRATURE_ALIASING_CONFIRMED`.
- QD2 `34770521310`: `PASS_DIAGNOSTIC_ITER053_SUPPORT_DIRECT_QUADRATURE_CONVERGED_BY_GL8`.
- QD3M `34771761543`: `PASS_DIAGNOSTIC_ITER053_QD3_GAUSS_JACOBI_MOMENTS_EXACT`.
- QD3 `34770675902`: `PASS_DIAGNOSTIC_ITER053_WEIGHTED_GJ3_BULK_PILOT_PROMISING`.

These remain diagnostics only and are not retroactive scored evidence for Iter053R.

## Iter053R — terminal scientific FAIL

Gate: `ITER053R-WEYL3-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION`.

- preregistration: `952c6321bbb54530a6881ae357c149256249187f`
- implementation: `d8481ae49a093626740e71c6b0c233ca74641819`
- production head: `6946680a5261eeb56a4496ae36a99098853d33d8`
- run: `34782291893`
- aggregate job: `103804601776`
- summary artifact: `10326722690`
- digest: `sha256:4ad7ad0190ea50a8928bbf9ef47b22f80616e7810513ba778ea3f1058c0023a9`

Frozen terminal classification:

**`SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`**

Evidence localization:

- all A4 generic lanes PASS;
- both B2 null lanes PASS;
- both C covariance lanes FAIL;
- worst C direct covariance residual: `3.2076700199377417e-12`;
- worst C weighted-H5 covariance residual: `0.6925581291599372`;
- transformed C0/C1 GJ2->GJ3 changes are approximately `0.2924` and `0.2921`;
- wrong-sign A controls behave as frozen.

Durable terminal note: `results/ITER053R_WEIGHTED_H5_COMPACT_SUPPORT_TERMINAL.md`.

Iter053R is not to be rerun or reinterpreted as PASS. A later replacement can only be a distinct prospectively frozen gate.

## Active gate — Iter053S

Gate: **`ITER053S-H5-TENSOR-DENSITY-COVARIANCE-LOCALIZATION`**.

Purpose: determine whether the numerical `H5=A+I-2 sqrt(-g)D5` implementation obeys the tensor-density law required by

`delta S = integral H^{ab} h_ab d4x`

under the two frozen determinant-one Iter053R C shears, and localize any defect between `A+I` and the derivative-density `D5` term.

Prospective preregistration: `71c077d34dba1749d0d34dc6dd0173648e82f60f`.
Implementation: `60532767595c38e92fbc9a8a35bf9b0c59b3600c`.
Workflow/production head: `514c4785ad500299a797281cb39a2eee7ffa7f0c`.
Production run: `34787788933`.

Frozen production architecture:

- 1 algebraic transformation-law control;
- 12 independent pointwise lanes = `2 C indices x 2 probes x 3 derivative steps`;
- `fail-fast:false`;
- up to 12 pointwise jobs in parallel;
- one aggregate only after all required lanes.

Do not consume partial lane values or alter thresholds while run `34787788933` is non-terminal.

## Exact current blocker

Compact-support Weyl3 functional-variation closure is **not established**. The highest-information blocker is now object identity/covariance of the implemented H5 bulk under coordinate change. Until Iter053S is terminal, do not launch a competing H5 covariance gate or brute-force retune the failed Iter053R quadrature.

## Next admissible logic after terminal Iter053S

- If `ITER053S_POINTWISE_H5_TENSOR_DENSITY_COVARIANCE_CONFIRMED`: prospectively test transformed weighted quadrature/pushforward convergence independently; Iter053R remains historical FAIL.
- If `ITER053S_D5_COVARIANCE_DEFECT_LOCALIZED`: prospectively audit/correct the covariant double-divergence `D5` implementation and validate against independent tensor transformation controls before any replacement compact-support gate.
- If `ITER053S_ALGEBRAIC_H5_COVARIANCE_DEFECT_LOCALIZED`: audit the algebraic `A+I` variational-density construction before any D5 or quadrature work.
- If INVALID: repair implementation/reference controls without changing the frozen scientific question.

## Claim locks

- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite computational panels are not global theorems;
- classical consistency is not quantum unitarity;
- no quantum amplitude/measure transition is currently authorized;
- no full GR recovery, UV-completion or new-physics claim;
- historical FAIL/INVALID results remain visible and are never rewritten by replacements.
