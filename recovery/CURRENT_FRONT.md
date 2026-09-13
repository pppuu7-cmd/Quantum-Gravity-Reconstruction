# QGR Current Research Front

Updated: 2026-09-14
Primary active gate: `Iter053T / weighted support-parameter pushforward covariance`
Companion active gate: `Iter053T-GJ / nodewise pushforward covariance hstep audit`
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

This static diagnosis is not itself a replacement PASS. Source-level derivation: `analysis/ITER053T_LEGACY_DOUBLE_WEIGHT_DERIVATION.md`.

## Iter053T primary — prospectively frozen production ACTIVE

Gate: **`ITER053T-WEIGHTED-SUPPORT-PARAMETER-PUSHFORWARD-COVARIANCE`**.

- preregistration: `4a8e523753996c1b6c3756f5e19eac301c73f1c5`
- implementation: `d996463e53aaa3a7a736488bd393f01beb56f162`
- workflow/production head: `df76ae7e59c92a30958572d963e6c4204f9c163b`
- production run: **`34788261104`**

Frozen architecture:

- 1 structural wrapper/factorization lane;
- 4 independent numerical lanes: `(C0,C1) x (GJ2,GJ3)` with `fail-fast:false`;
- corrected path uses source parameter `u=x`, transformed point `y=L^-1 u`, exactly one external GJ support weight, and polynomial factor `L^T p(u)L`;
- legacy `B(u)^2` path is retained as mandatory negative control;
- GJ2->GJ3 convergence is a scored predicate;
- one aggregate after all required lanes.

## Independently preregistered Iter053T-GJ companion — ACTIVE

A second gate was prospectively frozen and launched before the primary Iter053T preregistration was committed. Preserve it as an independent companion diagnostic rather than merging or selecting between verdicts post hoc.

Gate: **`ITER053T-GJ-NODEWISE-PUSHFORWARD-COVARIANCE-AUDIT`**.

- preregistration: `74d033551f0eb4060f9621cd9e9e10b00e57700a`
- implementation: `bfa059335b44eb6ac730e8b98d04a08fcb243bb0`
- aggregate classifier: `a2ae31c436161d1f8458e822be5e1c7f5ccbbded`
- workflow: `491db03d919b18ddfbaabb9115e3a2a850710b20`
- trigger/head: `75a30221c9a61d4a2484a9d0181cb3330d2104c0`
- production run: **`34788222635`**

Frozen companion scope:

- exactly GJ3, all 81 nodes for C0 and C1;
- three independent H5 derivative steps `1e-3`, `5e-4`, `2.5e-4`;
- 6 matrix lanes with `fail-fast:false`;
- primary predicate is nodewise contraction covariance, with weighted GJ3 sum as a consistency control;
- deliberately wrong congruence is the negative control.

This companion overlaps the primary gate at the corrected GJ3 contraction but has a different frozen scientific object: hstep robustness over all GJ3 nodes. The primary gate uniquely tests the `B -> B^2` causal diagnosis, legacy negative control, GJ2/GJ3 convergence and corrected-vs-legacy improvement. Therefore:

- do not pool raw lanes across the two classifiers;
- do not let either run alter the other's thresholds or terminal classification;
- do not choose the more favorable terminal verdict;
- terminalize each under its own preregistration;
- only after both are terminal may their jointly consistent scoped facts inform a new prospective replacement gate.

While either run is non-terminal, partial substantive numeric values have no scientific authority. Do not launch a third corrected-pushforward production.

## Exact current blocker

Compact-support Weyl3 functional-variation closure is **not established**. The immediate blocker is the corrected transformed weighted representation:

1. whether source-faithful single-weight pushforward restores nodewise and integrated C covariance;
2. whether that result is stable across the frozen H5 derivative steps in the companion gate;
3. whether GJ2->GJ3 convergence is restored while the legacy double-weight control remains discrepant in the primary gate.

If both companion results are terminal and compatible with corrected pushforward covariance, the next admissible step is a **distinct prospectively frozen full A4+B2+C2 replacement gate** retaining all original Iter053R scientific thresholds, seeds and negative controls while fixing only the transformed weighted reducer. A later replacement PASS would not rewrite Iter053R.

## Claim locks

- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite computational panels are not global theorems;
- classical consistency is not quantum unitarity;
- no quantum amplitude/measure transition is currently authorized;
- no full GR recovery, UV completion or new-physics claim.
