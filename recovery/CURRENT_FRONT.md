# QGR Current Research Front

Updated: 2026-09-14
Primary active front: `Iter053T / weighted support-parameter pushforward diagnosis`
Project phase: `MODEL_CONSTRUCTION / WEYL3 WEIGHTED PUSHFORWARD LOCALIZATION`

## Canonical status

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — roadmap readiness only, not correctness probability.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant six-derivative EOM established as a global theorem: **false**.
- Transition to quantum amplitude/measure closure: **not authorized**.

GitHub main + terminal Actions/results are authoritative.

## Preserved historical failures / invalids

- G51C run `34741060700`: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, 12/18 PASS.
- G51C-D2 run `34741924103`: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS.
- Original Iter053: `ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL`.
- Fresh original-contract retry run `34769958632`: `ITER053_IMPLEMENTATION_OR_CONTROL_INVALID`; aggregate job `103800868498`, artifact `10325874510`, digest `sha256:ed377d0dad4958eda95992db0efc6cfa4808739befcacfedbc377a8b1fd07b3e`.
- Iter053R run `34782291893`: `SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`; aggregate job `103804601776`, artifact `10326722690`, digest `sha256:4ad7ad0190ea50a8928bbf9ef47b22f80616e7810513ba778ea3f1058c0023a9`.

None is rewritten by later replacement gates.

## Iter052 — terminal genuinely-4D scoped PASS

Run `34748813339`; classification `PASS_SCOPED_ITER052_WEYL3_4D_COVARIANT_DIRECTIONAL_VARIATION_CERTIFICATE`. Finite computational certificate only.

## Iter053R — failure localization

A4 and B2 passed; both C covariance lanes failed only in weighted H5 bulk:

- worst direct covariance residual: `3.2076700199377417e-12`;
- worst weighted-H5 bulk covariance residual: `0.6925581291599372`;
- transformed C0/C1 GJ2->GJ3 changes: approximately `0.2924` and `0.2921`.

Durable note: `results/ITER053R_WEIGHTED_H5_COMPACT_SUPPORT_TERMINAL.md`.

## Iter053S — terminal scoped PASS

Gate: `ITER053S-H5-TENSOR-DENSITY-COVARIANCE-LOCALIZATION`.

- preregistration: `71c077d34dba1749d0d34dc6dd0173648e82f60f`
- implementation: `60532767595c38e92fbc9a8a35bf9b0c59b3600c`
- primary workflow head: `514c4785ad500299a797281cb39a2eee7ffa7f0c`
- primary substantive run: `34787788933`
- infrastructure-only aggregate-recovery head: `91086222bb20ec665a653dabde3c3811f98a09f1`
- aggregate-recovery run: `34787959341`
- aggregate job: `103806786112`
- summary artifact: `10326344492`
- digest: `sha256:ded3e5fa26af5754033103790384ad12a275ebaeaf0e47c1de1d544950119ddd`

Frozen terminal classification:

**`ITER053S_POINTWISE_H5_TENSOR_DENSITY_COVARIANCE_CONFIRMED`**

All 12 pointwise probes plus the algebraic control passed. Worst finest-step residuals:

- direct density `1.7620525013236046e-13`;
- algebraic `A+I` `1.1234468712818426e-14`;
- derivative-density `D5` `3.834671241411767e-08`;
- total `H5` `3.8507299553315486e-08`;
- `H:h` contraction `5.67809665333841e-08`.

Durable note: `results/ITER053S_H5_TENSOR_DENSITY_COVARIANCE_RESULT.md`.

Scientific consequence: the Iter053R C failure is not localized to pointwise H5 tensor-density object identity, `A+I`, or `D5` transformation within the frozen shear/probe scope.

## Newly localized implementation-path defect

The exact Iter053R weighted implementation now exposes a deterministic wrapper-depth error in the transformed C branch.

The Gauss-Jacobi rule `roots_jacobi(order,4,4)` already absorbs the compact-support factor

`B(u)=prod_i (1-(u_i/A)^2)^4`

into the quadrature weight.

For the base branch, `weighted_bulk(metric, pert, ...)` receives `pert=CompactPerturbation`, so

`base_pert.base.jets(u)[0]`

correctly returns the unfactored polynomial tensor `p(u)`.

For the transformed branch, Iter053R passes `pt=TransformPerturbation(pert,L)`. Here `pt.base` is the entire `CompactPerturbation`, not its polynomial base. Therefore the same expression

`base_pert.base.jets(u)[0]`

returns `B(u)p(u)`, after which `p_transform` applies `L^T (...) L`. Because the Gauss-Jacobi weight already supplies `B(u)`, the transformed legacy branch effectively integrates with `B(u)^2` rather than `B(u)`.

This is a concrete implementation-path diagnosis, not yet a replacement scientific PASS. It explains why the direct transformed integral is covariant while the weighted transformed branch is suppressed and poorly converged.

## Exact current blocker

Compact-support Weyl3 functional-variation closure is **not established**. The highest-information next gate is a prospectively frozen test of the source-parameter-faithful weighted pushforward:

- retain original source parameter `u=x`;
- evaluate transformed geometry at `y=L^{-1}u`;
- use the same single Gauss-Jacobi support weight `B(u)`;
- transform only the unfactored polynomial tensor `p(u)` as `L^T p(u)L`;
- compare nodewise and integrated base/transformed weighted values;
- retain the legacy double-weight path as a negative control.

This prospective gate is Iter053T. Iter053R remains historical FAIL regardless of the Iter053T outcome.

## Claim locks

- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite computational panels are not global theorems;
- classical consistency is not quantum unitarity;
- no quantum amplitude/measure transition is currently authorized;
- no full GR recovery, UV completion or new-physics claim;
- historical FAIL/INVALID results remain visible and are never rewritten by replacements.
