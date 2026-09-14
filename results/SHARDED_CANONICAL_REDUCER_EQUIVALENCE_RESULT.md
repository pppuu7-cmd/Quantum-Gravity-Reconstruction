# Canonical sharded reducer equivalence — terminal infrastructure PASS

Date: 2026-09-14

Gate: `SHARDED-CANONICAL-REDUCER-EQUIVALENCE`
Run: `34793130860`
Head: `94290a63a05f2a1370401d9ce0777f2e90185d38`
Aggregate job: `103821043118`
Scientific authority: **none**

## Frozen classification

`SHARDED_CANONICAL_REDUCER_EQUIVALENCE_PASS`

The prospectively frozen synthetic fixture used canonical node IDs `0..4095`, four deterministic shards, per-node artifacts and one canonical aggregate.

The aggregate established all required controls:

- input shard set valid: `true`;
- exact node coverage / identity: valid;
- canonical sharded `math.fsum` and independently regenerated baseline have exactly the same binary64 representation:
  `0x1.bd8affa2eacf2p-11`;
- missing-node negative control rejected: `true`;
- duplicate-node negative control rejected: `true`;
- mixed-implementation-identity negative control rejected: `true`.

Thus GitHub Actions sharding by canonical node ID can be used as an infrastructure representation of the same frozen discrete sum, provided a future scientific gate retains the same fail-closed coverage/hash controls and canonical reducer.

## Artifact provenance

Raw shard artifacts:

- shard 0: artifact `10327819275`, digest `sha256:54c584a42bf3ee42c7d0f2dcc58ccc014c4f7e32e14f810f1a1b027cdd9947d5`;
- shard 1: artifact `10328709072`, digest `sha256:3f90f8e09fad833192e7e06c1209894e959e0a17e36c6fcdd7a578d3fc74066b`;
- shard 2: artifact `10328639416`, digest `sha256:e41513393f74c218a0552dced5e9a34ecdbde847301360c9600f979375a8433d`;
- shard 3: artifact `10327998782`, digest `sha256:e685ff4669319f892ced9a50689ada6c363f70abe86755019630eb4f19d28577`.

Aggregate summary artifact:

- artifact `10328758601`;
- digest `sha256:fb2e25c42ffbfcf5395a88d67925a5be26f65891123760d1c3e2f514ec3d298f`.

## Scope

This PASS validates only the infrastructure proposition that deterministic per-node shards can reconstruct the exact frozen synthetic canonical sum while rejecting missing, duplicate and mixed-identity inputs.

It does **not** validate H5, D5, Weyl3 physics, cached stencils, Iter053T, Iter053U, any QGR scientific lane, `c6`, `beta`, stability, quantization or any physical prediction.

## Future use lock

A future sharded scientific workflow must still prospectively freeze its own:

- canonical node set and node-ID map;
- code/input identity included in every artifact;
- deterministic shard assignment;
- fail-closed complete/unique coverage verification;
- canonical summation/reduction rule;
- scientific thresholds and lane identity independent of shard topology.

No historical scientific artifacts may be pooled merely because this infrastructure fixture passed.