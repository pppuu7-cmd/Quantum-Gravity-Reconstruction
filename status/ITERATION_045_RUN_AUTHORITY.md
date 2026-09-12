# Iter045 production-run authority lock

Date: 2026-09-12

The workflow definition itself matched its initial push path and created an unintended first queued run:
- run `34716911042`, head `a4f03fb58105042a775f7940a33d628e98782901`.

The explicit preregistered production trigger then created:
- **authoritative run `34716924227`**, head `cad39c37bfdc56e8b66d0d45e907eb2a33d18d09`.

## Frozen authority rule
Only run `34716924227` may supply the Iter045 scientific terminal classification and durable result record.

Run `34716911042` is an accidental infrastructure duplicate caused by the workflow-file path trigger. If it executes or becomes terminal, classify it `+0 / NON_AUTHORITATIVE_DUPLICATE`; do not combine its lanes, metrics, artifacts, or PASS/FAIL count with the authoritative run and do not use it to increase readiness.

The science, thresholds, parameters, directions, and classifier remain exactly those preregistered in `status/ITERATION_045.md`; this authority lock changes no scientific criterion.
