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

Durable terminal note: `results/ITER053R_WEIGHTED_H5_COMPACT_SUPPORT_TERMINAL.md`.

Retrospective raw C audit additionally shows both base C frames were clean generic PASS while only transformed weighted branches failed. Fine transformed/base weighted ratios were approximately `0.3075515202` and `0.3074418708`. Durable analysis: `analysis/ITER053R_C_FAILURE_RETROSPECTIVE_LOCALIZATION.md`.

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

Scientific consequence: pointwise H5 object identity is not the source of the Iter053R C failure within the frozen scope.

## Deterministic wrapper-depth defect motivating Iter053T

Iter053R's Gauss-Jacobi rule with `alpha=beta=4` already supplies

`B(u)=prod_i(1-(u_i/A)^2)^4`.

For base `CompactPerturbation`, `.base.jets(u)` returns unfactored polynomial `p(u)`. For transformed `pt=TransformPerturbation(pert,L)`, `pt.base` is the whole `CompactPerturbation`, so the same legacy extraction returns `B(u)p(u)`. Applying `L^T(...)L` and then the external Jacobi weight therefore makes the transformed legacy path carry `B(u)^2` while the base path carries `B(u)` once.

Durable derivation: `analysis/ITER053T_LEGACY_DOUBLE_WEIGHT_DERIVATION.md`.

## Exact retrospective Gauss-Jacobi fingerprint of the defect

The accidental extra support factor has a parameter-free analytic quadrature fingerprint even for a constant reduced integrand.

For the frozen 4D tensor Jacobi rule:

- pure-extra-B GJ2 legacy/correct suppression `R2 = (10/11)^16 = 0.21762913579014878...`;
- pure-extra-B GJ3 suppression `R3 = (17980/24167)^4 = 0.3063851989352829...`;
- predicted GJ2->GJ3 relative change `0.28968782909086244...`.

Historical Iter053R C0/C1 observed fine suppression ratios `0.3075515202` / `0.3074418708` and transformed GJ2->GJ3 changes `0.2924102251` / `0.2921168408`.

Thus the frozen support-weight error alone reproduces the historical C signature to substantially better than one percent in the fine suppression ratio, with no fitted parameter. This is strong retrospective mechanistic localization, not an active-gate PASS.

Durable analysis: `analysis/ITER053R_DOUBLE_WEIGHT_GJ_MOMENT_FINGERPRINT.md`.

## Iter053T primary — prospectively frozen production ACTIVE

Gate: **`ITER053T-WEIGHTED-SUPPORT-PARAMETER-PUSHFORWARD-COVARIANCE`**.

- preregistration `4a8e523753996c1b6c3756f5e19eac301c73f1c5`
- implementation `d996463e53aaa3a7a736488bd393f01beb56f162`
- workflow/production head `df76ae7e59c92a30958572d963e6c4204f9c163b`
- production run **`34788261104`**

Frozen architecture:

- one structural wrapper/factorization lane;
- four independent numerical lanes `(C0,C1) x (GJ2,GJ3)`, `fail-fast:false`;
- corrected source path `u=x`, `y=L^-1u`, one external GJ support weight, `L^T p(u)L`;
- legacy `B(u)^2` mandatory negative control;
- GJ2->GJ3 convergence scored;
- one aggregate after all required lanes.

Latest checked state in this session: structural lane terminal-success; all four numerical lanes still `in_progress`; no partial substantive values consumed.

## Independently preregistered Iter053T-GJ companion — ACTIVE

Gate: **`ITER053T-GJ-NODEWISE-PUSHFORWARD-COVARIANCE-AUDIT`**.

- preregistration `74d033551f0eb4060f9621cd9e9e10b00e57700a`
- implementation `bfa059335b44eb6ac730e8b98d04a08fcb243bb0`
- aggregate classifier `a2ae31c436161d1f8458e822be5e1c7f5ccbbded`
- workflow `491db03d919b18ddfbaabb9115e3a2a850710b20`
- trigger/head `75a30221c9a61d4a2484a9d0181cb3330d2104c0`
- production run **`34788222635`**

Frozen scope:

- GJ3 all 81 nodes for C0/C1;
- hsteps `1e-3`, `5e-4`, `2.5e-4`;
- six independent matrix lanes, `fail-fast:false`;
- primary nodewise contraction covariance plus weighted-sum control;
- wrong congruence negative control.

Latest checked state in this session: all six substantive matrix lanes still `in_progress`; no partial substantive values consumed.

The companion and primary gate remain independent. Do not pool raw lanes, modify one gate from the other, or choose the more favorable verdict.

## Outcome-independent finite-difference diagnostic

The actual `derivative5` stencil has leading first-derivative error

`D_h f = f' - h^4 f^(5)/30 + O(h^6)`.

The nested D5 construction therefore remains fourth-order in the smooth-stencil regime. Under a non-orthogonal shear, finite-h axis truncation is generically noncovariant at `O(h^4)`, so a truncation-dominated covariance residual should fall approximately by a factor `16` under each frozen hstep halving before hitting a numerical floor.

This is a diagnostic fingerprint only and is not an added active-gate criterion. Durable analysis: `analysis/ITER053T_D5_FINITE_DIFFERENCE_COVARIANCE_SCALING.md`.

## Exact current blocker

Compact-support Weyl3 functional-variation closure is **not established**. Current obligations are:

1. source-faithful single-weight pushforward must restore nodewise/integrated C covariance under the primary gate;
2. the all-GJ3-node companion must independently confirm the mapped contraction over the three frozen hsteps;
3. primary GJ2->GJ3 convergence must be restored while the legacy double-weight control remains discrepant.

While either gate is non-terminal, partial values have no authority and a third corrected-pushforward production is forbidden.

## Next admissible gate if both Iter053T companions terminally agree

Prospectively freeze a **distinct full corrected A4+B2+C2 replacement** that:

- recomputes every lane fresh;
- retains all original Iter053R seeds, quadrature orders, epsilon/H5 steps, scientific thresholds and wrong-sign controls;
- changes only the transformed weighted polynomial-source extraction;
- treats unexpected movement of unchanged A/B/C-base/direct paths as implementation invalidity;
- does not pool historical PASS lanes.

Outcome-independent plans:

- `analysis/ITER053_CORRECTED_FULL_REPLACEMENT_IMPLEMENTATION_PLAN.md`
- `analysis/ITER053_FULL_REPLACEMENT_PARALLELIZATION_AUDIT.md`
- `analysis/ITER053_FULL_REPLACEMENT_REGRESSION_FIREWALL.md`
- `analysis/ITER053_FULL_REPLACEMENT_ADVERSARIAL_CHECKLIST.md`

Historical runtime evidence supports Actions-level decomposition into up to 20 independent direct/weighted/frame components plus deterministic combiners and one aggregate, if frozen prospectively.

## Downstream priority after a future full corrected replacement PASS

Do **not** jump immediately to a quantum phase gate.

Existing flat/weak-background TT results do not establish the physical mode structure of the activated `c6 Weyl^3` correction on Weyl-active curved backgrounds. Iter045 explicitly leaves overall sign, energy positivity, unitarity and nonlinear stability open; flat background is linearly blind to cubic Weyl.

Therefore the next fatal-consistency priority is a prospectively frozen **Weyl-active curved-background principal-symbol / mode-structure / hyperbolicity gate** with `c6` symbolic. See `analysis/POST_ITER053_FATAL_STABILITY_PRIORITY.md`.

Only if that layer survives should the main line proceed to the scoped principal-branch projective coherent relative-phase bridge based on G32/G38. Exact absolute finite-cell Weyl-active phase normalization is not currently derived; `beta` and `c6` normalization null directions remain explicit. See `analysis/POST_ITER053_DEPENDENCY_BRIDGE_MAP.md`.

## Governance note

The `Current position` blocks in `docs/ROADMAP.md` and `README.md` are stale Iter001 bootstrap snapshots. The durable iteration chain contains explicit pre-ansatz crossing and QGR-L1 promotion authority. Normative roadmap/constitution criteria remain binding; only bootstrap mutable status text is stale. Durable audit: `analysis/GOVERNANCE_PROMOTION_AUTHORITY_AUDIT_2026-09-14.md`.

## Claim locks

- theory established = **0%**;
- no experimental confirmation;
- `c6` unfixed;
- `beta=1` not authorized;
- finite computational panels are not global theorems;
- generic nonlinear/radiative stability of the Weyl3-corrected dynamics is not established;
- absolute energy positivity is not established;
- classical consistency is not quantum unitarity;
- exact globally unique finite-cell coherent phase is not established;
- no quantum amplitude/measure transition is currently authorized;
- no full GR recovery, UV completion or new-physics claim.
