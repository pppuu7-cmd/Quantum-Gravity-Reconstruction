# Canonical sharded reducer equivalence control

Date: 2026-09-14

Status: **NON-SCIENTIFIC INFRASTRUCTURE CONTROL**. It cannot classify any QGR scientific gate.

## Purpose

Validate the deterministic reduction architecture proposed for a future sharded Iter053U/full-replacement computation without running QGR physics.

## Frozen synthetic object

Canonical node IDs are exactly integers `0..4095`.

For node `i`, define the deterministic binary64 contribution in Python as

`v_i = (-1 if i%2 else 1) * (i+1) / float((i+17)*(i+17))`.

Freeze `nshards=4`; shard `s` owns exactly nodes satisfying `i % 4 == s`.

Every shard artifact must include:
- gate ID;
- shard ID and nshards;
- frozen implementation identity string `CANONICAL_REDUCER_FIXTURE_V1`;
- all owned `(node_id,value)` pairs in ascending node order.

## Frozen aggregate controls

The reducer must:

1. load exactly 4 shard artifacts;
2. reject mixed `nshards`, gate or implementation identity;
3. reject any duplicate node ID;
4. reject any missing or out-of-range node ID;
5. sort all contributions by canonical node ID;
6. compute `math.fsum(values)` over the full sorted per-node sequence;
7. independently regenerate all 4096 frozen values in canonical order and compute a baseline `math.fsum`;
8. require exact binary64 identity via `float.hex(sharded_sum) == float.hex(baseline_sum)`.

## Frozen negative controls

Inside aggregate validation, deliberately construct three invalid copies of the completed synthetic artifact set:

- remove node 0: coverage verifier must reject;
- duplicate node 1: uniqueness verifier must reject;
- alter one shard implementation identity: identity verifier must reject.

All three rejections are mandatory.

## Terminal infrastructure classifications

- `SHARDED_CANONICAL_REDUCER_EQUIVALENCE_PASS`
- `SHARDED_CANONICAL_REDUCER_EQUIVALENCE_INVALID`

## Interpretation ceiling

A PASS establishes only that per-node GitHub Actions shards can be reassembled into the frozen canonical synthetic sum with exact node coverage/identity enforcement. It does not validate H5, quadrature physics, cached D5, Iter053T, Iter053U, c6, or any QGR scientific claim.