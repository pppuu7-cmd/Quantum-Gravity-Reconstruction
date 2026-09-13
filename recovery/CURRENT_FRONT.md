# QGR Current Research Front

Updated: 2026-09-14
Primary active gate: `Iter053T / weighted support-parameter pushforward covariance`
Project phase: `MODEL_CONSTRUCTION / WEYL3 WEIGHTED PUSHFORWARD LOCALIZATION`

## Canonical status

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established as a global theorem: **false**.
- Transition to quantum amplitude/measure closure: **not authorized**.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID results are never rewritten by replacements.

## Preserved terminal history

- G51C run `34741060700`: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, 12/18 PASS.
- G51C-D2 run `34741924103`: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS.
- Iter052 run `34748813339`: `PASS_SCOPED_ITER052_WEYL3_4D_COVARIANT_DIRECTIONAL_VARIATION_CERTIFICATE`; finite computational certificate only.
- Original Iter053: `ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL`.
- Fresh original-contract Iter053 retry `34769958632`: `ITER053_IMPLEMENTATION_OR_CONTROL_INVALID`; aggregate `103800868498`, artifact `10325874510`, digest `sha256:ed377d0dad4958eda95992db0efc6cfa4808739befcacfedbc377a8b1fd07b3e`.
- Iter053R `34782291893`: `SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`; aggregate `103804601776`, artifact `10326722690`, digest `sha256:4ad7ad0190ea50a8928bbf9ef47b22f80616e7810513ba778ea3f1058c0023a9`.

## Iter053R failure localization

A4 and B2 passed; both C covariance lanes failed only in weighted H5 bulk:

- worst direct covariance residual `3.2076700199377417e-12`;
- worst weighted-H5 bulk covariance residual `0.6925581291599372`;
- transformed C0/C1 GJ2->GJ3 changes approximately `0.2924` and `0.2921`.

Durable note: `results/ITER053R_WEIGHTED_H5_COMPACT_SUPPORT_TERMINAL.md`.

## Iter053S — terminal scoped PASS

Gate: `ITER053S-H5-TENSOR-DENSITY-COVARIANCE-LOCALIZATION`.

- prereg `71c077d34dba1749d0d34dc6dd0173648e82f60f`
- implementation `60532767595c38e92fbc9a8a35bf9b0c59b3600c`
- primary head `514c4785ad500299a797281cb39a2eee7ffa7f0c`, run `34787788933`
- aggregate-recovery head `91086222bb20ec665a653dabde3c3811f98a09f1`, run `34787959341`
- aggregate job `103806786112`
- summary artifact `10326344492`, digest `sha256:ded3e5fa26af5754033103790384ad12a275ebaeaf0e47c1de1d544950119ddd`

Classification: **`ITER053S_POINTWISE_H5_TENSOR_DENSITY_COVARIANCE_CONFIRMED`**.

All 12 frozen pointwise probes plus algebraic control passed. Worst finest-step residuals: direct density `1.7620525013236046e-13`, `A+I` `1.1234468712818426e-14`, `D5` `3.834671241411767e-08`, total `H5` `3.8507299553315486e-08`, `H:h` `5.67809665333841e-08`.

Durable note: `results/ITER053S_H5_TENSOR_DENSITY_COVARIANCE_RESULT.md`.

Scientific consequence: pointwise H5 object identity is not the source of the Iter053R C failure within the frozen scope.

## Deterministic wrapper-depth defect motivating Iter053T

Iter053R's Gauss-Jacobi rule with `alpha=beta=4` already supplies the compact-support factor

`B(u)=prod_i(1-(u_i/A)^2)^4`.

For base `CompactPerturbation`, `.base.jets(u)` returns unfactored polynomial `p(u)`. For transformed `pt=TransformPerturbation(pert,L)`, `pt.base` is the whole `CompactPerturbation`, so the same legacy extraction returns `B(u)p(u)`. Applying `L^T(...)L` and then the external Gauss-Jacobi weight therefore makes the transformed legacy path carry `B(u)^2` while the base path carries `B(u)` once.

This static diagnosis is not itself a replacement PASS.

## Iter053T — prospectively frozen production ACTIVE

Gate: **`ITER053T-WEIGHTED-SUPPORT-PARAMETER-PUSHFORWARD-COVARIANCE`**.

- preregistration: `4a8e523753996c1b6c3756f5e19eac301c73f1c5`
- implementation: `d996463e53aaa3a7a736488bd393f01beb56f162`
- workflow/production head: `df76ae7e59c92a30958572d963e6c4204f9c163b`
- production run: **`34788261104`**

Frozen architecture:

- 1 structural wrapper/factorization lane;
- 4 independent numerical lanes: `(C0,C1) x (GJ2,GJ3)` with `fail-fast:false`, up to four numerical jobs in parallel;
- corrected path uses source parameter `u=x`, transformed point `y=L^-1 u`, exactly one external GJ support weight, and polynomial factor `L^T p(u)L`;
- legacy `B(u)^2` path is retained as mandatory negative control;
- one aggregate after all required lanes.

While run `34788261104` is non-terminal, do not use partial numeric values as scientific evidence, do not change thresholds, and do not launch a competing corrected-pushforward production.

## Exact current blocker

Compact-support Weyl3 functional-variation closure is **not established**. The immediate blocker is whether the prospectively defined single-weight source-faithful pushforward restores weighted C covariance and GJ2->GJ3 convergence while the frozen legacy path remains discrepant.

If Iter053T terminally passes, the next admissible step is a **distinct prospectively frozen full A4+B2+C2 replacement gate** using the corrected pushforward. A later replacement PASS would not rewrite Iter053R.

## Claim locks

- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite computational panels are not global theorems;
- classical consistency is not quantum unitarity;
- no quantum amplitude/measure transition is currently authorized;
- no full GR recovery, UV completion or new-physics claim.
