# Iter057BC — Same-Iteration Edge Pollution Causal Diagnostic

Status: **PROSPECTIVELY PREREGISTERED / NOT YET PRODUCED**  
Date: 2026-09-17

## Motivation

Iter057BB terminally classified `FAIL_TECHNICAL_ITER057BB_INDEPENDENT_REPRODUCTION_OR_DAG_CONTROL_FAILURE` while its two separately authored lanes agreed exactly on the 23-record census, ordered dependency classes, replay queue, byte-safe undecodable-provenance identities, and scientific normalized SHA256. Both lane payloads alone reported `dag_acyclic=false`. A read-only post-terminal audit observed only equal-rank non-earlier iteration references and no later-rank references.

This new gate does **not** reclassify Iter057BB. It tests a narrow causal hypothesis derived from that terminal evidence.

## Frozen hypothesis

The Iter057BB DAG-control failure is caused solely by admitting same-iteration provenance mentions into the dependency-edge set before the acyclicity test, even though the original Iter057AU/BB frozen method permits transitive dependency only along explicit **earlier-result dependencies**.

## Frozen parents

- Iter057AU census/preregistration snapshot: `616859890df95057556d265612c53da839a5848a`.
- Iter057BB preregistration: `eb864872be1db63d0588296c606b759b7b1495c8`.
- Iter057BB production head: `6cbae90b3c6d93cbc0b1569d846f805b2e2a2553`.
- Iter057BB Actions run: `35251292539`.
- Iter057BB primary artifact: `10508709546`, digest `sha256:860d59d95f073844025687d4378200565ca5d7239c7825f441c2b9935b5a4a2a`.
- Iter057BB independent artifact: `10508704797`, digest `sha256:b058ab6b1dc9b478c6b9e8216d59abd483e7ebdc438d8b3d741da8d4a6db9a67`.
- Iter057BB terminal artifact: `10509760965`, digest `sha256:8198245f204af5dc479ba1b84637af77051e4400ba950e41754c087e3cd564b1`.
- Iter057BB terminal payload SHA256: `05e93f9031a8875ea513456cfbbe4bbcb5c6f0972c3cafce70d62cd9ccd0ea6e`.
- Iter057BB scientific normalized SHA256: `5cba0b3b3e8475b974d8cf8f633875a7a1ab63f92b1503cbb353633ca2ac9189`.

Historical Iter057AU/BB classifications remain immutable.

## Frozen intervention

For each of the two independently implemented Iter057BB provenance classifiers, reproduce its lane payload on the unchanged frozen AU census, then partition every explicit iteration dependency candidate `(child, parent_iteration)` by iteration rank:

- `EARLIER`: `rank(parent) < rank(child)`;
- `EQUAL`: `rank(parent) == rank(child)`;
- `LATER`: `rank(parent) > rank(child)`.

Construct a diagnostic graph using **only `EARLIER` candidates**. No other dependency/parser/classification rule may change.

Recompute transitive classes from the original lane's `DIRECT_LOAD_BEARING_DEPENDENT` seeds using only the `EARLIER` graph. Direct-legacy classifications are not refit. Independent/unresolved decisions are not target-fit. Produce the resulting ordered classes and replay queue.

## Independent reproduction

The primary diagnostic consumes only a freshly reproduced Iter057BB-primary lane payload. The independent diagnostic consumes only a freshly reproduced Iter057BB-independent lane payload. Diagnostic implementations are separately authored and may not import/call/read each other's payloads.

## Frozen acceptance criteria

`PASS_SCOPED_ITER057BC_SAME_ITERATION_EDGE_POLLUTION_CAUSALLY_LOCALIZED` requires all of:

1. both reproduced BB lane payloads retain the exact frozen AU census and their original parser styles;
2. every dependency candidate is partitioned exactly once as EARLIER/EQUAL/LATER;
3. each lane has zero `LATER` candidates;
4. each lane has at least one `EQUAL` candidate;
5. the `EARLIER`-only graph is acyclic in each lane;
6. filtering only non-earlier candidates leaves each lane's ordered dependency classes unchanged from its own BB lane payload;
7. filtering only non-earlier candidates leaves each lane's replay queue unchanged from its own BB lane payload;
8. primary and independent diagnostics agree exactly on the set of `(child record, equal parent iteration)` candidates;
9. primary and independent filtered ordered classes agree exactly;
10. primary and independent filtered replay queues agree exactly;
11. byte-safe undecodable-provenance identities/load-bearing flags remain exactly those produced by the corresponding BB lane; no new decoding policy is introduced;
12. no descendant scientific computation is replayed, no historical result is modified, and no claim lock is promoted.

If a `LATER` candidate exists, earlier-only filtering does not restore acyclicity, or filtering changes ordered classes/replay queue, classify `FAIL_TECHNICAL_ITER057BC_CAUSAL_HYPOTHESIS_NOT_ESTABLISHED`.

If required frozen payload reproduction cannot be realized, classify `BLOCKED_ITER057BC_CAUSAL_DIAGNOSTIC_NOT_REALIZED`.

Green CI alone is not PASS.

## Authority semantics

A scoped PASS would establish only that the Iter057BB DAG failure was caused by admitting same-iteration candidates into a graph whose frozen semantics were earlier-only. It would authorize a **separately preregistered** corrected dependency-adjudication gate using strict earlier-only edge admissibility. It would not itself authorize descendant replay and would not reclassify Iter057AU or Iter057BB.

## Claim locks

Theory established remains 0%; no experiment; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
