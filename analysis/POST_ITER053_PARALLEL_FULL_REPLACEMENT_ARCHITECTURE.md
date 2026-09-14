# Outcome-independent architecture — deterministic sharded full corrected Iter053 replacement

Date: 2026-09-14

Status: compute-architecture preparation only. **Not a preregistration, not an active gate, and not authorization to launch a replacement.** A replacement is admissible only after the active Iter053T diagnostic authority permits it.

## Motivation

The current diagnostic productions show that monolithic GJ3/nodewise jobs can occupy one runner for a long time. A future full A4+B2+C2 corrected replacement should preserve the exact scientific object and frozen criteria while distributing independent quadrature nodes across many GitHub Actions jobs.

The central rule is:

**parallel execution may change wall-clock time, but must not change the mathematical sum, lane identity, frozen inputs, thresholds, or terminal classifier.**

## Deterministic reduction rule

Every quadrature node receives a canonical integer `node_id` defined solely by lexicographic tensor-product index. A shard is a deterministic subset selected by

`node_id mod nshards == shard_id`.

Each shard writes per-node contributions rather than only an already-summed scalar. The reducer:

1. verifies exact expected node IDs with no duplicates/missing nodes;
2. sorts by canonical `node_id`;
3. reconstructs every additive integral using `math.fsum` in that canonical order;
4. reduces controls by exact Boolean AND / maximum / minimum operations;
5. records the shard count and all artifact digests but excludes shard count from scientific predicates.

Thus a 1-shard and N-shard execution are representations of the same frozen discrete quadrature object, not distinct scientific gates.

## Proposed independent work graph

For a future full A4+B2+C2 replacement with the original scientific lane identities retained:

### A stream — 4 lane identities
For each A0..A3:
- direct GL7 node shards;
- direct GL8 node shards;
- weighted GJ2 shards;
- weighted GJ3 shards;
- deterministic lane reducer.

### B stream — 2 lane identities
For each B0..B1:
- direct GL7 node shards;
- direct GL8 node shards;
- weighted GJ2 shards;
- weighted GJ3 shards;
- deterministic lane reducer.

### C stream — 2 lane identities, base/transformed preserved
For each C0..C1:
- base direct GL7 shards;
- base direct GL8 shards;
- transformed direct GL7 shards;
- transformed direct GL8 shards;
- base weighted GJ2 shards;
- base weighted GJ3 shards;
- corrected transformed weighted GJ2 shards;
- corrected transformed weighted GJ3 shards;
- deterministic base/transformed lane reducer.

The corrected transformed weighted path must transform only the unfactored polynomial source and must not change the direct transformed full-perturbation path.

## Suggested shard counts

These are implementation defaults, not scientific parameters:

- GL7 (`7^4=2401` nodes): 8 shards per integral;
- GL8 (`8^4=4096` nodes): 8 shards per integral;
- GJ2 (`2^4=16` nodes): 4 shards per integral;
- GJ3 (`3^4=81` nodes): 9 shards per integral.

The exact number may be reduced for runner availability **before launch** without changing the scientific object, because canonical per-node reconstruction is shard-count invariant. After launch, changing shard topology is allowed only as infrastructure recovery if the same canonical node set and reduction identity are preserved and no substantive node outputs are selectively rerun/pooled.

## Parallelism scale

A fully expanded graph would expose many dozens of independent shard jobs. GitHub Actions can execute them subject to account concurrency. To avoid unnecessary queue pressure, a practical first production may cap the matrix while still separating the most expensive GL8 and GJ3 work.

A balanced design is approximately:
- 10 physical side objects for direct work (A4+B2+C base/transformed 4) x GL7/GL8 sharded independently;
- 10 physical side objects for weighted work, with GJ3 receiving the largest shard count;
- reducers per scientific lane;
- one frozen aggregate over exactly A4+B2+C2 lane results.

## Anti-pooling / provenance requirements

- every shard artifact must contain gate ID, stream/index/side/order, canonical node IDs, code commit and frozen input hashes;
- reducers reject mixed code commits or input hashes;
- reducers reject duplicate/missing node IDs;
- no successful shards from a superseded scientific contract may be reused;
- infrastructure retry may rerun a missing shard only if the exact gate/object/code/input identity is unchanged;
- scientific lane verdict is emitted only by its reducer after all frozen nodes are present;
- terminal aggregate consumes only the eight current-run lane reducers.

## Regression firewall

The future full replacement must preserve from Iter053R:
- A4 and B2 lane definitions;
- C direct path and coordinate/collar controls;
- original seeds, shears, support, EPS ladder, HSTEP, GL/GJ orders;
- original PASS/FAIL/INVALID thresholds unless a new preregistration explicitly freezes a scientifically distinct contract;
- wrong-sign control;
- historical Iter053R FAIL.

Only the transformed weighted polynomial-source extraction is eligible for the source-faithful correction already localized by the diagnostic chain.

## Required prelaunch equivalence control

Before any authoritative sharded replacement, a small non-substantive fixture should compare 1-shard versus multi-shard canonical reduction on a synthetic deterministic integrand and require bitwise-identical node coverage and `math.fsum` result (or exact agreement within a prospectively frozen machine-roundoff bound if serialization changes representation).

This checks the compute architecture, not QGR physics.

## Claim ceiling

This architecture does not authorize the future full replacement and does not consume partial Iter053T evidence. It exists solely to make the next admissible gate faster and more reproducible if terminal authority opens it.