# QGR Current Research Front

Updated: 2026-09-14
Primary active gate: `Iter053T / weighted support-parameter pushforward covariance`
Companion active gate: `Iter053T-GJ / nodewise pushforward covariance hstep audit`
Project phase: `MODEL_CONSTRUCTION / WEYL3 WEIGHTED PUSHFORWARD LOCALIZATION`

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

## Preserved history

- G51C: `SCIENTIFIC_FAIL_G51C_FULL_WEYL3_EOM_ASSEMBLY`, 12/18 PASS.
- G51C-D2: `SCIENTIFIC_FAIL_G51C_D2_SIGN_OR_HELDOUT_VALIDATION`, 19/20 PASS.
- Iter052: `PASS_SCOPED_ITER052_WEYL3_4D_COVARIANT_DIRECTIONAL_VARIATION_CERTIFICATE`.
- Original Iter053: `ITER053_NUMERICAL_OR_INFRASTRUCTURE_FAIL`.
- Fresh original-contract Iter053 retry: `ITER053_IMPLEMENTATION_OR_CONTROL_INVALID`.
- Iter053R run `34782291893`: `SCIENTIFIC_FAIL_ITER053R_WEYL3_WEIGHTED_H5_COMPACT_SUPPORT_ACTION_VARIATION`.
- Iter053S: `ITER053S_POINTWISE_H5_TENSOR_DENSITY_COVARIANCE_CONFIRMED`.

## Iter053R failure mechanism now localized

Iter053R A4+B2 passed. C direct covariance was excellent (`3.2076700199377417e-12` worst), while weighted H5 C covariance failed (`0.6925581291599372` worst).

The historical transformed weighted path double-counts the compact-support factor:

- GJ `alpha=beta=4` measure already supplies `B(u)`;
- transformed wrapper extraction reaches a full `CompactPerturbation`, supplying another `B(u)`;
- legacy transformed effective path is `B(u)^2`, unlike the base single-weight path.

Exact GJ moment fingerprint:

- GJ2 extra-weight suppression `0.21762913579014877...`;
- GJ3 suppression `0.30638519893528289...`;
- GJ2->GJ3 relative drift `0.28968782909086243...`.

This quantitatively tracks historical transformed C behavior without fitting. Historical Iter053R remains FAIL.

## Iter053T primary — ACTIVE / non-terminal

Gate: `ITER053T-WEIGHTED-SUPPORT-PARAMETER-PUSHFORWARD-COVARIANCE`

- prereg `4a8e523753996c1b6c3756f5e19eac301c73f1c5`
- implementation `d996463e53aaa3a7a736488bd393f01beb56f162`
- run `34788261104`

Latest operational state:
- structural success;
- C0-GJ2 success;
- C1-GJ2 success;
- C0-GJ3 in progress;
- C1-GJ3 in progress;
- aggregate pending.

No partial substantive values have scientific authority.

Exact PASS string required for successor execution:
`ITER053T_LEGACY_DOUBLE_WEIGHT_CONFIRMED_SOURCE_FAITHFUL_PUSHFORWARD_COVARIANT_SCOPED`.

## Iter053T-GJ nodewise companion — ACTIVE / non-terminal

Gate: `ITER053T-GJ-NODEWISE-PUSHFORWARD-COVARIANCE-AUDIT`

- prereg `74d033551f0eb4060f9621cd9e9e10b00e57700a`
- implementation `bfa059335b44eb6ac730e8b98d04a08fcb243bb0`
- run `34788222635`

Frozen matrix: C0/C1 × h=`1e-3,5e-4,2.5e-4`, all 81 GJ3 nodes, six lanes + aggregate.

Latest state:
- C0-h1e-3 success;
- C0-h5e-4 success;
- remaining four lanes in progress;
- aggregate pending.

No partial substantive values have scientific authority.

Exact PASS string required for successor execution:
`ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE_CONFIRMED`.

The two Iter053T gates are independent preregistrations. No pooling, majority vote, threshold transfer or favorable-verdict selection.

## Independent controls already terminal

### Orthogonal controls R1

Run `34792534325`:
`ORTHOGONAL_CONTROLS_R1_PASS`.

Non-authoritative algebra/stencil/wrapper/tensor support only.

### Deterministic GitHub sharding

Run `34793130860`:
`SHARDED_CANONICAL_REDUCER_EQUIVALENCE_PASS`.

Canonical sharded and baseline `math.fsum` were exactly binary64-identical. Missing-node, duplicate-node and mixed-identity negative controls all rejected.

This validates multi-job node sharding as infrastructure, not QGR science.

### D5 canonical-lattice cache

Run `34793411230`, aggregate job `103822309604`:
`D5_CANONICAL_CACHE_EQUIVALENCE_PASS`.

- 16/16 lanes valid and PASS;
- worst D relative residual `3.0138740385466435e-12`;
- worst H5 relative residual `3.0062091790262304e-12`;
- minimum corrupted-cache negative-control difference `7.985885551649203e-4`;
- summary artifact `10327914830`;
- digest `sha256:e4fdb3ce144cb5f9621eaa5c4548e2202a3ff8ed081313cc479adc9b80741472`.

The validated cache uses 129 unique P/Weyl stencil points instead of approximately 290 repeated historical requests per H5 evaluation, ideal expensive-call reduction ~2.248×. Scientific object/thresholds unchanged.

Result: `results/D5_CANONICAL_CACHE_EQUIVALENCE_RESULT.md`.

## Conditional Iter053U — FINAL IMPLEMENTATION FROZEN / NOT AUTHORIZED / NOT TRIGGERED

Gate:
`ITER053U-CORRECTED-SOURCE-FAITHFUL-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION`

Conditional preregistration was frozen before terminal Iter053T evidence:
`dbb306d68e6d1fc332a73eccb88f52df0cc5859a`.

Final implementation freeze:
`0739f2ede212e5144c771aae5e71f7f1075ea4ed`.

Frozen implementation identities:

- validated cache backend `29cc9136c071b4f9900c4da630b80920f62989ab`;
- monolithic reference `7250362b0120e1b5873fe1f7a45940aff8833643`;
- provenance-hardened split/reducers `34c7b355467103aec9c9e1c5d599fe0034cb9ace`;
- cached v2 dispatcher `f1f42d7242426b6e754acf55f9b00cd0047f974d`;
- authorization guard `6d2e5062f459b9683a6068ca9a65ef7883d2888e`;
- final aggregate `cc92b09fba57bf03ef7382ba9a8d425cdb584657`;
- prepared workflow `c365d3f02d0d0f93a8c01f34873bfb2f668de37f`.

Execution graph:

1. durable authorization guard;
2. 20 independent integration parts;
3. 8 scientific lane reducers A4+B2+C2;
4. one frozen aggregate.

Direct parts keep the historical Iter053R full compact-support object.
Weighted parts use the validated 129-point H5 cache at `h=5e-4`.
The sole scientific correction is C transformed weighted source extraction:
`u=x`, `y=L^-1u`, one external support weight, `L^T p(u)L`.

Each part carries production SHA + SHA-256 authorization-state identity + prereg commit + required PASS strings. Reducers and aggregate fail closed on mixed provenance/seed identity. Missing artifacts terminalize as frozen infrastructure failure.

**No `status/ITER053U_PRODUCTION_TRIGGER.txt` exists. U has never run.**

Execution is allowed only if durable recovery contains BOTH exact Iter053T PASS strings above. From the final freeze onward, no Iter053U scientific-code edits are allowed before trigger; any required change demands a new prospective implementation version/preregistration.

## Post-functional-variation stability blocker

Raw Weyl-cubic high-frequency structure is generically quartic in covector despite six-derivative EFT counting:

`P4(k) ~ c6 Cbar k^4`,

with curvature Hessian schematically
`d^2 Tr(C^3)[D,D] = 6 Tr(C D^2)`.

Exactly conformally-flat `Cbar=0` is a clean high-derivative null. Type-N `W3=0` is not automatically a null when `Cbar != 0`.

But repository authority has not derived how the higher-derivative correction is physically evolved:

`MISSING_WEYL3_DYNAMICAL_TREATMENT_AUTHORITY`.

The unresolved alternatives include exact fourth-order evolution, perturbative/order-reduced EFT, and well-posed regularized EFT formulations. External literature was reviewed only as background methodology; it is explicitly **not QGR authority**.

Thus a raw quartic root is neither automatically a physical ghost/new mode nor automatically discardable as an EFT artifact.

## Locked next sequence

1. Terminalize primary Iter053T and nodewise companion independently.
2. If either is FAIL/INVALID/nonterminal: do not run Iter053U.
3. Only if both exact PASS strings are durable: create the already-defined Iter053U trigger, with no code changes.
4. Recompute all fresh Iter053U A4+B2+C2 through the frozen cached 20-part graph.
5. If Iter053U passes: derive QGR-specific higher-derivative dynamical treatment.
6. Only then run physically interpreted Weyl-active stability/spectrum gate.
7. Quantum amplitude/measure remains downstream of surviving classical dynamics/stability.
