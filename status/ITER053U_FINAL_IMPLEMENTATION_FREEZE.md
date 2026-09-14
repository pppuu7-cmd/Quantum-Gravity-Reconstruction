# Iter053U final implementation freeze

Date: 2026-09-14

Gate:
`ITER053U-CORRECTED-SOURCE-FAITHFUL-WEIGHTED-H5-COMPACT-SUPPORT-ACTION-VARIATION`

Status: **FINAL IMPLEMENTATION FROZEN / EXECUTION NOT AUTHORIZED / NO TRIGGER EXISTS**.

This freeze occurs after the separately preregistered non-scientific cache-equivalence gate terminally classified

`D5_CANONICAL_CACHE_EQUIVALENCE_PASS`

and while both prerequisite Iter053T scientific productions remain non-terminal. No substantive Iter053U scientific result has been computed.

## Frozen authority chain

Conditional scientific preregistration:
- `dbb306d68e6d1fc332a73eccb88f52df0cc5859a`
- `preregistration/ITER053U_CORRECTED_FULL_COMPACT_SUPPORT_VARIATION_CONDITIONAL.md`

Validated cache authority:
- equivalence run `34793411230`
- aggregate job `103822309604`
- classification `D5_CANONICAL_CACHE_EQUIVALENCE_PASS`
- result note commit `01858349a461c97e6f2ed349b7b8d0099c848b9f`
- summary artifact `10327914830`
- digest `sha256:e4fdb3ce144cb5f9621eaa5c4548e2202a3ff8ed081313cc479adc9b80741472`

Validated cache backend wrapper:
- commit `29cc9136c071b4f9900c4da630b80920f62989ab`
- `code/qgr_d5_validated_cache_backend.py`
- directly reuses the tested `build_cache/reduce_cache` functions from `code/qgr_d5_canonical_cache_equivalence.py`;
- hard-fails for any H5 step other than the validated `5e-4`;
- hard-fails unless the canonical cache contains exactly 129 unique points.

Final monolithic reference implementation:
- commit `7250362b0120e1b5873fe1f7a45940aff8833643`
- `code/qgr_iter053u_corrected_full.py`

Provenance-hardened v1 split/reducers:
- commit `34c7b355467103aec9c9e1c5d599fe0034cb9ace`
- `code/qgr_iter053u_parallel_parts.py`

Final v2 cached dispatcher:
- commit `f1f42d7242426b6e754acf55f9b00cd0047f974d`
- `code/qgr_iter053u_parallel_parts_v2.py`

Fail-closed durable authorization guard:
- commit `6d2e5062f459b9683a6068ca9a65ef7883d2888e`
- `code/qgr_iter053u_authorization_guard.py`

Final provenance-hardened aggregate classifier:
- commit `cc92b09fba57bf03ef7382ba9a8d425cdb584657`
- `code/qgr_iter053u_aggregate.py`

Final prepared production graph:
- commit `c365d3f02d0d0f93a8c01f34873bfb2f668de37f`
- `.github/workflows/qgr-iter053u-corrected-full.yml`

## Frozen execution graph

1. one durable authorization job;
2. 20 independent integration parts:
   - A0-A3: base direct + base weighted = 8;
   - B0-B1: base direct + base weighted = 4;
   - C0-C1: base/transformed × direct/weighted = 8;
3. eight scientific lane reducers A4+B2+C2;
4. one frozen aggregate classifier.

Direct parts use the historical Iter053R direct compact-support object.

Weighted parts use the separately validated canonical H5 cache at `h=5e-4`.

The only scientific object correction relative to Iter053R is the C transformed weighted polynomial source:

`u=x`, `y=L^-1 u`, one external GJ support weight, `p_y=L^T p(u)L`.

C transformed direct action remains the historical full transformed compact perturbation.

## Provenance firewall

Every integration part is frozen to carry:

- production `GITHUB_SHA`;
- SHA-256 of the durable authorization `recovery/state.json` read by that run;
- conditional preregistration commit;
- exact required primary/companion PASS classification strings.

Lane reducers reject mixed part provenance and seed identities.

Final aggregate rejects mixed lane provenance and requires the common production SHA to equal the current workflow head. Missing lanes become frozen infrastructure classification rather than being silently ignored.

No historical Iter053R/T/T-GJ raw scientific lane may be pooled into Iter053U.

## Execution lock

No `status/ITER053U_PRODUCTION_TRIGGER.txt` exists at this freeze.

Execution remains forbidden unless durable recovery contains exactly:

1. primary:
   `ITER053T_LEGACY_DOUBLE_WEIGHT_CONFIRMED_SOURCE_FAITHFUL_PUSHFORWARD_COVARIANT_SCOPED`;
2. companion:
   `ITER053T_GJ_NODEWISE_PUSHFORWARD_COVARIANCE_CONFIRMED`.

The authorization guard reads durable repository state only. It does not inspect partial Actions values or infer PASS from green CI.

If either prerequisite is FAIL, INVALID, non-terminal, or differently scoped, this frozen implementation remains unused. A different scientific question requires a new preregistration.

## No-more-edits lock

From this commit onward, do not alter Iter053U scientific code, cache backend, thresholds, source extraction, lane graph, classifier, negative controls or interpretation ceiling before the production trigger.

Allowed before trigger:
- recovery/status bookkeeping;
- independent adversarial code review that does not alter the frozen implementation;
- recording terminal prerequisite authorities;
- infrastructure-only documentation.

Any defect requiring scientific implementation changes after this freeze requires a new prospective implementation version / preregistration rather than silently editing this frozen gate.

## Claim ceiling

This freeze is readiness/provenance only, not a scientific result. Iter053R remains historical FAIL. Iter053T gates remain authoritative prerequisites. `theory established=0%`; `c6` remains symbolic/unfixed; `beta=1` remains unauthorized; no stability, quantum, UV, GR-recovery, experimental or new-physics claim follows.