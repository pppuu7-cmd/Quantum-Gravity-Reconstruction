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
- Fresh original-contract Iter053 retry `34769958632`: `ITER053_IMPLEMENTATION_OR_CONTROL_INVALID`; aggregate `103800868498`, artifact `10325874510`, digest `sha256:ed377d0dad4958eda95992db0efc6cfa4808739befcacfedbc377a8b1fd07b3e`.
- Iter053R `34782291893`: `SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`; aggregate `103804601776`, artifact `10326722690`, digest `sha256:4ad7ad0190ea50a8928bbf9ef47b22f80616e7810513ba778ea3f1058c0023a9`.

Historical FAIL/INVALID entries above remain immutable.

## Iter053R failure localization

A4 and B2 passed; both C covariance lanes failed only in weighted H5 bulk:

- worst direct covariance residual `3.2076700199377417e-12`;
- worst weighted-H5 bulk covariance residual `0.6925581291599372`;
- transformed C0/C1 GJ2->GJ3 changes approximately `0.2924` and `0.2921`.

Retrospective raw C audit showed both base C frames were clean generic PASS while only transformed weighted branches failed. Fine transformed/base weighted ratios were approximately `0.3075515202` and `0.3074418708`.

Durable notes:
- `results/ITER053R_WEIGHTED_H5_COMPACT_SUPPORT_TERMINAL.md`
- `analysis/ITER053R_C_FAILURE_RETROSPECTIVE_LOCALIZATION.md`

## Iter053S — terminal scoped PASS

Gate: `ITER053S-H5-TENSOR-DENSITY-COVARIANCE-LOCALIZATION`.

- prereg `71c077d34dba1749d0d34dc6dd0173648e82f60f`
- implementation `60532767595c38e92fbc9a8a35bf9b0c59b3600c`
- primary run `34787788933`
- aggregate-recovery run `34787959341`
- aggregate job `103806786112`
- summary artifact `10326344492`, digest `sha256:ded3e5fa26af5754033103790384ad12a275ebaeaf0e47c1de1d544950119ddd`

Classification: **`ITER053S_POINTWISE_H5_TENSOR_DENSITY_COVARIANCE_CONFIRMED`**.

Worst finest-step total H5 covariance residual `3.8507299553315486e-08`; H:h residual `5.67809665333841e-08`.

Scientific consequence: pointwise H5 tensor-density object identity is not the source of the historical Iter053R C failure within the frozen panel.

## Deterministic wrapper-depth defect and analytic fingerprint

The Iter053R Gauss-Jacobi rule with `alpha=beta=4` already supplies the compact-support factor

`B(u)=prod_i(1-(u_i/A)^2)^4`.

Base extraction reaches the unfactored polynomial `p(u)`. The historical transformed wrapper instead exposes the full `CompactPerturbation`, so the same reducer extracts `B(u)p(u)` and the external Jacobi measure supplies a second `B(u)`. Thus the transformed legacy weighted path represents `B(u)^2`, not the same single-weight object as the base path.

Independent exact Gauss-Jacobi moments give the parameter-free constant-reduced-integrand fingerprint:

- GJ2 extra-weight suppression `0.21762913579014877...`;
- GJ3 suppression `0.30638519893528289...`;
- GJ2->GJ3 relative drift `0.28968782909086243...`.

The historical fine C0/C1 suppressions `0.3075515202` / `0.3074418708` and drifts `0.2924102251` / `0.2921168408` are quantitatively close without fitting. This is strong retrospective mechanism localization, not reclassification of Iter053R.

Durable analyses:
- `analysis/ITER053T_LEGACY_DOUBLE_WEIGHT_DERIVATION.md`
- `analysis/ITER053R_DOUBLE_WEIGHT_GJ_MOMENT_FINGERPRINT.md`
- `analysis/ITER053T_EXACT_SOURCE_PARAMETER_COVARIANCE_LEMMA.md`

## Iter053T primary — prospectively frozen production ACTIVE

Gate: **`ITER053T-WEIGHTED-SUPPORT-PARAMETER-PUSHFORWARD-COVARIANCE`**.

- preregistration `4a8e523753996c1b6c3756f5e19eac301c73f1c5`
- implementation `d996463e53aaa3a7a736488bd393f01beb56f162`
- workflow/production head `df76ae7e59c92a30958572d963e6c4204f9c163b`
- run **`34788261104`**

Frozen obligations:
- structural wrapper/factorization identity;
- C0/C1 x GJ2/GJ3 corrected source-faithful weighted covariance;
- GJ2->GJ3 convergence;
- historical legacy B^2 path retained as negative control;
- corrected-vs-legacy improvement;
- one frozen aggregate.

Latest operational status checked in this session:
- structural: terminal success;
- C0-GJ2: terminal success;
- C1-GJ2: terminal success;
- C0-GJ3: `in_progress`;
- C1-GJ3: `in_progress`;
- aggregate: pending.

These job statuses are operational only. No partial numeric values are scientific evidence.

## Independently preregistered Iter053T-GJ companion — ACTIVE

Gate: **`ITER053T-GJ-NODEWISE-PUSHFORWARD-COVARIANCE-AUDIT`**.

- preregistration `74d033551f0eb4060f9621cd9e9e10b00e57700a`
- implementation `bfa059335b44eb6ac730e8b98d04a08fcb243bb0`
- aggregate classifier `a2ae31c436161d1f8458e822be5e1c7f5ccbbded`
- workflow `491db03d919b18ddfbaabb9115e3a2a850710b20`
- trigger/head `75a30221c9a61d4a2484a9d0181cb3330d2104c0`
- run **`34788222635`**

Frozen scope: all 81 GJ3 nodes for C0/C1 at hsteps `1e-3`, `5e-4`, `2.5e-4`, six independent lanes plus aggregate, with wrong-congruence negative control.

Latest operational status: C0 at `h=5e-4` is terminal success; the other five matrix lanes remain `in_progress`; aggregate pending. No partial substantive values have authority.

Primary and companion are independent preregistrations. Do not pool raw lanes, alter one from the other, or select the more favorable verdict.

## Non-authoritative parallel orthogonal controls

To use otherwise idle independent work without contaminating active scientific gates, a separate four-lane control matrix tested STENCIL / WEIGHT / WRAPPER / TENSOR facts only.

Original run `34792340429` is permanently **`ORTHOGONAL_CONTROLS_INVALID`** because its frozen copied WEIGHT reference digits were not precise enough for its own `5e-13` reference tolerance. That history is preserved.

A separately prospectively frozen exact-rational reference retry R1 then ran:

- run `34792534325`;
- aggregate job `103819407020`;
- all four independent lanes PASS;
- classification **`ORTHOGONAL_CONTROLS_R1_PASS`**;
- summary artifact `10327693945`;
- digest `sha256:12ea26f978112f9219105743000a1f9b3e40a513bfeaacb3f4d4f553d1cdb5b3`.

This result is implementation/algebra support only. It cannot classify either scientific Iter053T gate or authorize a replacement by itself.

Durable result: `results/ITER053T_ORTHOGONAL_CONTROLS_R1_RESULT.md`.

## Outcome-independent future full-replacement architecture

If and only if both scientific Iter053T gates terminally support a compatible corrected pushforward, the next admissible classical gate is a **distinct full A4+B2+C2 corrected replacement**. Every lane must be recomputed fresh; no historical PASS pooling.

A deterministic GitHub Actions sharding design is already prepared so expensive GL7/GL8/GJ3 node sets can be distributed across many independent jobs while reconstructing the same canonical discrete sum by node ID and `math.fsum`. Parallel topology is infrastructure only and may not change the scientific object.

Durable architecture: `analysis/POST_ITER053_PARALLEL_FULL_REPLACEMENT_ARCHITECTURE.md`.

Required regression/adversarial plans:
- `analysis/ITER053_CORRECTED_FULL_REPLACEMENT_IMPLEMENTATION_PLAN.md`
- `analysis/ITER053_FULL_REPLACEMENT_REGRESSION_FIREWALL.md`
- `analysis/ITER053_FULL_REPLACEMENT_ADVERSARIAL_CHECKLIST.md`

## Post-Iter053 stability dependency — corrected interpretation

Existing Iter005/043/044/045 results already cover the at-most-two-derivative weak/flat characteristic and TT sector in their stated scopes. Iter046 covers a special exact nonlinear pp-wave sector of the two-derivative dynamics. Iter047-050 establish Weyl3 activation and variational prerequisites, not the physical characteristic structure of the corrected dynamics.

For a curvature-only `Weyl^3` action, the operator is six-derivative in EFT counting, while its metric Euler-Lagrange equation is generically **fourth differential order**. The curvature Hessian obeys schematically

`d^2 Tr(C^3)[D,D] = 6 Tr(C D^2)`,

so on a nonzero-Weyl background the raw high-frequency linearized correction has schematic structure

`P4(k) ~ c6 * Cbar * k^4`.

Consequences:
- exact conformally-flat `Cbar=0` is the clean highest-derivative null control;
- `W3=0` on a type-N pp-wave does **not** imply the quadratic/principal correction vanishes when `Cbar != 0`;
- Petrov-D/Schwarzschild, Kasner and type-N are distinct useful algebraic classes, not interchangeable controls.

Durable analyses:
- `analysis/POST_ITER053_WEYL3_PRINCIPAL_SYMBOL_GAP_AUDIT.md`
- `analysis/WEYL3_PRINCIPAL_SYMBOL_HESSIAN_LEMMA.md`

## Newly isolated object-definition blocker: exact dynamics versus EFT/order reduction

Historical authority treats `c6 Weyl^3` as the unique scoped parity-even six-derivative **Wilson/correction direction**, power-counted as `O(h^4)` / `O(Gamma^2)`, and keeps `c6` as an unfixed UV-matching parameter. It establishes flat Hessian decoupling and curved-background quadratic activation.

However, reviewed authority does **not** yet derive either:

- exact nonperturbative fourth-order evolution with all additional characteristic branches treated as physical candidate modes, or
- a perturbative/order-reduced evolution prescription with explicit reduction, initial-data rule and validity domain.

Therefore the current dependency classification is:

**`MISSING_WEYL3_DYNAMICAL_TREATMENT_AUTHORITY`**.

A raw quartic characteristic root cannot automatically be called a physical ghost/new degree of freedom; equally, it cannot be discarded as an EFT artifact without a prospectively derived order-reduction authority.

For a perturbative interpretation, the schematic local control parameter is

`epsilon_HD(k) ~ |c6| h^4 ||Cbar|| ||k||^2`.

Nonperturbative roots appearing only when `epsilon_HD ~ 1` are not automatically controlled by the six-derivative truncation. Because `c6` is unfixed, no universal numerical k-cutoff is currently authorized.

Durable analyses:
- `analysis/WEYL3_DYNAMICAL_TREATMENT_AUTHORITY_GAP.md`
- `analysis/WEYL3_EXACT_VS_ORDER_REDUCED_STABILITY_SEMANTICS.md`

## Exact current blocker and gate order

Compact-support Weyl3 functional-variation closure is **not established**. Current obligations are still the two active Iter053T scientific productions. While either is non-terminal, partial values have no authority and a third corrected-pushforward production is forbidden.

If compatible terminal Iter053T scoped results are obtained, the allowed sequence is:

1. prospectively freeze and run a **distinct full corrected A4+B2+C2 functional-variation replacement**, recomputing all lanes fresh;
2. only after that full object passes, resolve **`MISSING_WEYL3_DYNAMICAL_TREATMENT_AUTHORITY`** from QGR construction principles;
3. only then run the physically interpreted Weyl-active stability/spectrum gate appropriate to the derived treatment;
4. only after surviving the classical stability layer may the main line proceed toward quantum amplitude/measure and the scoped projective coherent-phase bridge.

No gate may skip these dependencies.

## Claim locks

- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite computational panels are not global theorems;
- generic nonlinear/radiative stability of the Weyl3-corrected dynamics is not established;
- exact-vs-order-reduced Weyl3 dynamics is not established;
- physical higher-derivative mode count is not established;
- absolute energy positivity is not established;
- classical consistency is not quantum unitarity;
- exact globally unique finite-cell coherent phase is not established;
- no quantum amplitude/measure transition is currently authorized;
- no full GR recovery, UV completion or new-physics claim.
