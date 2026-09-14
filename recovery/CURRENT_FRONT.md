# QGR Current Research Front

Updated: 2026-09-14
Primary active gate: `Iter053U / corrected source-faithful weighted H5 compact-support action variation`
Project phase: `MODEL_CONSTRUCTION / WEYL3 CORRECTED COMPACT-SUPPORT FUNCTIONAL VARIATION`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Weyl3 exact-vs-perturbative/order-reduced/well-posed dynamical treatment: **not established**.
- Quantum amplitude/measure transition: **not authorized**.
- No unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID results are immutable.

## Iter053T primary — TERMINAL SCOPED PASS

Gate: `ITER053T-WEIGHTED-SUPPORT-PARAMETER-PUSHFORWARD-COVARIANCE`

- prereg `4a8e523753996c1b6c3756f5e19eac301c73f1c5`
- implementation `d996463e53aaa3a7a736488bd393f01beb56f162`
- run `34788261104`
- aggregate job `103828912630`
- summary artifact `10329638555`
- digest `sha256:312079d2cc1a07b7af12763aedb0f980879117bfda3185be34ca096321bf7faa`
- classification `ITER053T_LEGACY_DOUBLE_WEIGHT_CONFIRMED_SOURCE_FAITHFUL_PUSHFORWARD_COVARIANT_SCOPED`

Frozen aggregate is valid/complete. Worst corrected integrated covariance residual: `2.0590650746290315e-09`; worst corrected nodewise covariance residual: `3.4581493704057676e-08`. C0 corrected GJ3 covariance residual `1.2518957930421278e-09` versus legacy `0.6924484798485422`; C1 corrected `2.2171978395835512e-10` versus legacy `0.6925581291599372`. GJ2→GJ3 convergence and legacy negative controls passed.

## Iter053T-GJ companion — TERMINAL SCOPED PASS

Gate: `ITER053T-GJ-NODEWISE-PUSHFORWARD-COVARIANCE-AUDIT`

- prereg `74d033551f0eb4060f9621cd9e9e10b00e57700a`
- implementation `bfa059335b44eb6ac730e8b98d04a08fcb243bb0`
- run `34788222635`
- aggregate job `103828894352`
- summary artifact `10329224173`
- digest `sha256:1c330cf704500654659a653bce9fac397b9b7b00495172935702cac3f626b9a0`
- classification `ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE_CONFIRMED`

All 6/6 frozen lanes pass and are valid. Minimum nontrivial nodes: 81. Worst nodewise contraction residual `8.409160670944214e-08`; worst weighted-GJ3 sum covariance residual `6.140021540682663e-09`; minimum wrong-congruence residual `0.13608019032461305`.

The two PASS classifications were obtained under independent preregistrations and are now durably recorded. No evidence pooling or post-hoc threshold changes were used. Historical Iter053R remains `SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION` and is not rewritten.

Durable terminal note: `results/ITER053T_TERMINAL_RESULT.md`.

## Iter053U — FROZEN AND AUTHORIZED FOR PRODUCTION

Gate: `ITER053U-CORRECTED-SOURCE-FAITHFUL-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION`.

- preregistration `dbb306d68e6d1fc332a73eccb88f52df0cc5859a`
- validated cache backend `29cc9136c071b4f9900c4da630b80920f62989ab`
- reference implementation `7250362b0120e1b5873fe1f7a45940aff8833643`
- authorization guard `6d2e5062f459b9683a6068ca9a65ef7883d2888e`
- cached dispatcher v2 `f1f42d7242426b6e754acf55f9b00cd0047f974d`
- aggregate classifier `cc92b09fba57bf03ef7382ba9a8d425cdb584657`
- prepared workflow `c365d3f02d0d0f93a8c01f34873bfb2f668de37f`
- final implementation freeze `0739f2ede212e5144c771aae5e71f7f1075ea4ed`

Execution graph: durable authorization guard → 20 independent integration parts → 8 fresh A4+B2+C2 lane reducers → frozen aggregate. Direct parts retain the historical Iter053R compact-support object. Weighted parts use the separately validated 129-point D5/H5 cache at `h=5e-4`. The only scientific correction is the C transformed weighted source extraction: one support weight with `u=x`, `y=L^-1u`, polynomial factor `L^T p(u)L`.

No scientific-code edit is permitted before production trigger. Green CI alone will not count as scientific PASS; raw part/lane artifacts and the frozen aggregate must be consumed.

## Locked next sequence

1. Trigger the already-frozen Iter053U production workflow with no code changes.
2. Consume all 20 part artifacts, all 8 fresh lane artifacts and the frozen aggregate.
3. Classify Iter053U under its preregistered thresholds; do not weaken criteria post hoc.
4. Only after an Iter053U PASS, derive QGR-specific exact-vs-perturbative/order-reduced/well-posed Weyl3 dynamical treatment.
5. Only then open a physically interpreted Weyl-active stability/spectrum gate.
6. Quantum amplitude/measure remains downstream of surviving classical dynamics/stability.
