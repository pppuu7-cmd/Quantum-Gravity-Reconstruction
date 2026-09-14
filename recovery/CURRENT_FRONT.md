# QGR Current Research Front

Updated: 2026-09-14
Primary active gate: `Iter053T / weighted support-parameter pushforward covariance`
Companion active gate: `Iter053T-GJ / nodewise pushforward covariance hstep audit`
Project phase: `MODEL_CONSTRUCTION / WEYL3 WEIGHTED PUSHFORWARD LOCALIZATION`

## Canonical status

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99%** — internal construction bookkeeping only, not correctness probability.
- Theory established: **0%**.
- `beta` remains a matching/calibration parameter; `beta=1` is not authorized.
- `c6` remains **symbolic/unfixed**.
- Full covariant Weyl3 metric EOM established as a global theorem: **false**.
- Weyl3 exact-vs-perturbative/order-reduced dynamical treatment established: **false**.
- Transition to quantum amplitude/measure closure: **not authorized**.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID results are never rewritten by replacements.

## Preserved terminal history

- G51C run `34741060700`: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, 12/18 PASS.
- G51C-D2 run `34741924103`: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS.
- Iter052 run `34748813339`: `PASS_SCOPED_ITER052_WEYL3_4D_COVARIANT_DIRECTIONAL_VARIATION_CERTIFICATE`; finite computational certificate only.
- Original Iter053: `ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL`.
- Fresh original-contract Iter053 retry `34769958632`: `ITER053_IMPLEMENTATION_OR_CONTROL_INVALID`.
- Iter053R `34782291893`: `SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`.

Historical FAIL/INVALID entries above remain immutable.

## Iter053R -> Iter053S localization

Iter053R A4+B2 passed; both C covariance lanes failed only in weighted H5 bulk:

- worst direct covariance residual `3.2076700199377417e-12`;
- worst weighted-H5 bulk covariance residual `0.6925581291599372`;
- transformed C0/C1 GJ2->GJ3 changes approximately `0.2924` and `0.2921`.

Iter053S then terminally confirmed pointwise H5 tensor-density covariance in its frozen scope:

`ITER053S_POINTWISE_H5_TENSOR_DENSITY_COVARIANCE_CONFIRMED`.

Thus pointwise H5 object identity is not the source of the historical C failure in that panel.

## Exact transformed weighted-wrapper defect

Gauss-Jacobi `alpha=beta=4` already supplies the compact-support factor

`B(u)=prod_i(1-(u_i/A)^2)^4`.

Base extraction reaches the unfactored polynomial `p(u)`. The historical transformed wrapper exposes the full `CompactPerturbation`, so the legacy reducer extracts `B(u)p(u)` and the external GJ measure supplies a second `B(u)`. The historical transformed object is therefore `B(u)^2`, not the same single-weight integral as the base path.

Independent exact GJ moments give:

- GJ2 extra-weight suppression `0.21762913579014877...`;
- GJ3 suppression `0.30638519893528289...`;
- GJ2->GJ3 relative drift `0.28968782909086243...`.

Historical C fine suppressions `0.3075515202` / `0.3074418708` and drifts `0.2924102251` / `0.2921168408` closely follow this parameter-free fingerprint. This is mechanism localization, not reclassification of Iter053R.

## Iter053T primary — ACTIVE

Gate: `ITER053T-WEIGHTED-SUPPORT-PARAMETER-PUSHFORWARD-COVARIANCE`

- prereg `4a8e523753996c1b6c3756f5e19eac301c73f1c5`
- implementation `d996463e53aaa3a7a736488bd393f01beb56f162`
- head `df76ae7e59c92a30958572d963e6c4204f9c163b`
- run `34788261104`

Latest operational status:
- structural success;
- C0-GJ2 success;
- C1-GJ2 success;
- C0-GJ3 in progress;
- C1-GJ3 in progress;
- aggregate pending.

No partial numeric result has scientific authority.

Exact PASS string required for any Iter053U execution:

`ITER053T_LEGACY_DOUBLE_WEIGHT_CONFIRMED_SOURCE_FAITHFUL_PUSHFORWARD_COVARIANT_SCOPED`.

## Iter053T-GJ nodewise companion — ACTIVE

Gate: `ITER053T-GJ-NODEWISE-PUSHFORWARD-COVARIANCE-AUDIT`

- prereg `74d033551f0eb4060f9621cd9e9e10b00e57700a`
- implementation `bfa059335b44eb6ac730e8b98d04a08fcb243bb0`
- aggregate `a2ae31c436161d1f8458e822be5e1c7f5ccbbded`
- trigger `75a30221c9a61d4a2484a9d0181cb3330d2104c0`
- run `34788222635`

Frozen matrix: C0/C1 × `h={1e-3,5e-4,2.5e-4}`, all 81 GJ3 nodes, six independent lanes and one aggregate.

Latest operational status:
- C0-h5e-4 terminal success;
- other five matrix lanes in progress;
- aggregate pending.

No partial numeric result has scientific authority.

Exact PASS string required for any Iter053U execution:

`ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE_CONFIRMED`.

Primary and companion are separate preregistrations. No evidence pooling, threshold transfer, majority vote or selection of the more favorable verdict is allowed.

## Non-authoritative algebra/control matrix

Original orthogonal-control run `34792340429` remains permanently `ORTHOGONAL_CONTROLS_INVALID` because its own frozen copied WEIGHT reference digits were insufficient for its `5e-13` reference tolerance.

A separately preregistered exact-rational retry R1 terminally passed:

- run `34792534325`;
- aggregate `103819407020`;
- classification `ORTHOGONAL_CONTROLS_R1_PASS`;
- summary artifact `10327693945`;
- digest `sha256:12ea26f978112f9219105743000a1f9b3e40a513bfeaacb3f4d4f553d1cdb5b3`.

This is implementation/algebra support only and cannot classify either scientific Iter053T gate.

## Parallel GitHub architecture — terminal infrastructure PASS

A fully independent synthetic sharding fixture tested canonical per-node GitHub Actions parallelism:

- run `34793130860`;
- aggregate job `103821043118`;
- classification `SHARDED_CANONICAL_REDUCER_EQUIVALENCE_PASS`;
- summary artifact `10328758601`;
- digest `sha256:fb2e25c42ffbfcf5395a88d67925a5be26f65891123760d1c3e2f514ec3d298f`.

The sharded and independently regenerated baseline `math.fsum` were exactly binary64-identical (`0x1.bd8affa2eacf2p-11`). Missing-node, duplicate-node and mixed-identity negative controls were all rejected.

Scientific consequence: none. Infrastructure consequence: a future gate may prospectively distribute canonical quadrature nodes over many GitHub jobs without changing the frozen discrete observable, provided it retains complete/unique node coverage, code/input hashes and canonical deterministic reduction.

Durable result: `results/SHARDED_CANONICAL_REDUCER_EQUIVALENCE_RESULT.md`.

## D5 canonical-lattice cache equivalence — ACTIVE non-scientific matrix

Static audit found that one historical H5 evaluation requests about 290 expensive Weyl-P evaluations although the exact nested five-point stencil contains 129 unique canonical lattice points. Ideal expensive-call reduction is approximately `290/129 = 2.248`.

A prospective 16-lane implementation-equivalence matrix is running:

- contract `a336ff7d3698aed4c203ba0ea9a6c9cbd3322736`;
- implementation `41555417ea8cd9f597a8dda76ad9a164c3452ca4`;
- workflow `3fd4b64646689a4f41e6c1e79608870aedce65a8`;
- trigger `43b844f691a716c0f678b9ed20c7ddb3fa140140`;
- run `34793411230`;
- matrix A4+B2+C2 × two fixed points, `h=5e-4`.

Latest status: **all 16 raw lanes terminal success; aggregate queued/pending**. Raw success is not the frozen equivalence verdict. Cache use in Iter053U remains unauthorized until aggregate classification is terminal `D5_CANONICAL_CACHE_EQUIVALENCE_PASS`.

## Conditional Iter053U — preregistered/prepared, NOT AUTHORIZED, NOT TRIGGERED

Gate:

`ITER053U-CORRECTED-SOURCE-FAITHFUL-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION`

Prospective preregistration was frozen while both Iter053T productions were still non-terminal, before their terminal GJ3 evidence:

- prereg `dbb306d68e6d1fc332a73eccb88f52df0cc5859a`;
- current reference implementation `c3dfadd976fc7a340ac59c83b56ca7813e38971a`;
- durable execution guard `6d2e5062f459b9683a6068ca9a65ef7883d2888e`;
- aggregate classifier `7f48ff24371e69e6bc0602406d704b242586fd6d`;
- prepared workflow `b98ed50b748480e53e930f8101e82c32157f067f`.

**No `status/ITER053U_PRODUCTION_TRIGGER.txt` exists. Iter053U has not been launched.**

The authorization guard reads only durable `recovery/state.json` and requires both exact terminal PASS strings above. It does not inspect partial Actions results or green CI.

Iter053U freezes all original Iter053R scientific inputs/thresholds and recomputes all A4+B2+C2 lanes fresh. The sole scientific correction is the C transformed **weighted polynomial-source extraction**; C direct transformed full compact-support path stays historical/object-identical. Historical evidence is not pooled.

The prepared workflow currently uses the historical D5 implementation. If and only if the separate D5 cache equivalence aggregate passes before final Iter053U implementation freeze, the validated cache may be adopted prospectively and the final implementation identity must be frozen before trigger creation.

## Post-Iter053 classical stability dependency

Existing Iter005/043/044/045 already cover the two-derivative weak/flat characteristic and TT sector in their stated scopes. Iter046 covers a special nonlinear pp-wave sector of two-derivative dynamics. Iter047-050 establish Weyl3 activation/variation prerequisites, not physical characteristics of the corrected dynamics.

For curvature-only `Weyl^3`, the action operator is six-derivative in EFT counting while its raw metric equation is generically fourth differential order. Curvature-Hessian structure gives schematically

`d^2 Tr(C^3)[D,D] = 6 Tr(C D^2)`,

so the raw Weyl-active high-frequency correction scales as

`P4(k) ~ c6 Cbar k^4`.

Clean high-derivative null: exactly conformally flat `Cbar=0`. Type-N `W3=0` is not automatically a null for the quadratic/principal correction when `Cbar !=0`.

## Object-definition blocker: physical treatment of higher derivatives

Repository authority treats `c6 Weyl^3` as a six-derivative Wilson/correction direction, power-counted in the regular refinement regime, but has not derived either:

- exact fundamental fourth-order evolution, or
- perturbative/order-reduced/well-posed-EFT evolution with explicit validity and initial-data prescription.

Current classification:

`MISSING_WEYL3_DYNAMICAL_TREATMENT_AUTHORITY`.

A raw quartic root is therefore neither automatically a physical ghost/new mode nor automatically disposable as an EFT artifact.

External methodology review is stored separately as **background only, not QGR authority**:
`analysis/EXTERNAL_EFT_HIGHER_DERIVATIVE_DYNAMICS_METHODOLOGY.md`.

It records perturbative-constraint/reduction-of-order and modern well-posed EFT approaches only to define controls/options that a future QGR-specific derivation must distinguish prospectively.

## Locked gate order

1. Terminalize primary Iter053T and nodewise companion independently.
2. Iter053U execution becomes admissible only if **both exact PASS strings** are durably recorded.
3. Before final U implementation freeze, consume the D5-cache equivalence aggregate only as an infrastructure choice; never as scientific evidence.
4. Trigger and recompute fresh Iter053U A4+B2+C2 only after authorization; no historical pooling.
5. If Iter053U passes, derive QGR-specific exact-vs-EFT/order-reduced/well-posed dynamical treatment.
6. Only then run the physically interpreted Weyl-active stability/spectrum gate.
7. Only after the classical stability layer survives may the main line move toward quantum amplitude/measure and the projective coherent-phase bridge.

## Claim locks

- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` unauthorized;
- finite computational panels are not global theorems;
- generic nonlinear/radiative stability of the Weyl3-corrected dynamics is not established;
- exact-vs-order-reduced/well-posed Weyl3 dynamics is not established;
- physical higher-derivative mode count is not established;
- absolute energy positivity is not established;
- classical consistency is not quantum unitarity;
- exact globally unique finite-cell coherent phase is not established;
- no quantum amplitude/measure transition is currently authorized;
- no full GR recovery, UV completion or new-physics claim.
