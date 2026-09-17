# Iter057BD — Strict-Earlier-Only Descendant Dependency Adjudication

Status: **PROSPECTIVELY PREREGISTERED / NOT YET PRODUCED**  
Date: 2026-09-17

## Purpose

Produce a corrected authoritative dependency adjudication for the historical post-Iter057X lineage after Iter057BC causally established that the Iter057BB DAG-control failure came solely from admitting same-iteration provenance mentions into a graph whose frozen AU/BB transitive-dependency semantics require explicit **earlier-result dependencies**.

This is a new gate. Historical Iter057AU remains BLOCKED and Iter057BB remains technical FAIL; neither is reclassified.

## Frozen parents

- Iter057AU frozen census/preregistration snapshot: `616859890df95057556d265612c53da839a5848a`.
- Iter057AT corrected degree-six source vector SHA256: `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`.
- Iter057BA byte-safe/canonical authority: durable result `9315d4a987698fc502958235b2c9ec011e097244`, classification `PASS_SCOPED_ITER057BA_NEUTRAL_CANONICAL_BYTE_SAFE_CERTIFICATE_INDEPENDENTLY_REPRODUCED`.
- Iter057BB terminal technical FAIL: durable result `9f693a06f4ec16f06b32f427469beef2eb671844`, terminal payload SHA256 `05e93f9031a8875ea513456cfbbe4bbcb5c6f0972c3cafce70d62cd9ccd0ea6e`.
- Iter057BC causal authority: durable result `4175032db3d74e3939996fe44309724142a6cbf6`, classification `PASS_SCOPED_ITER057BC_SAME_ITERATION_EDGE_POLLUTION_CAUSALLY_LOCALIZED`, terminal payload SHA256 `5ebe5d0891a5f3aec8d4faa9e84684b4650b925ca6125142dd292807a4c4f6cf`.
- `c6` remains symbolic/unfixed.

## Frozen census and target blindness

The censused result set is exactly the Iter057AU preregistration snapshot `616859890df95057556d265612c53da839a5848a`. Results created after that snapshot are not members of the scientific dependency census and may not alter dependency classification.

No descendant scientific outcome may be recomputed or used as a target while classifying dependency. Historical result files are immutable.

## Frozen dependency classes

Each censused post-Iter057X result record receives exactly one unchanged AU class:

- `DIRECT_LOAD_BEARING_DEPENDENT`;
- `TRANSITIVE_LOAD_BEARING_DEPENDENT`;
- `INDEPENDENT_OF_LEGACY_DEGREE6_SOURCE`;
- `UNRESOLVED_PROVENANCE`.

Direct legacy-source detection remains unchanged. `UNRESOLVED_PROVENANCE` remains fail-closed.

## Sole corrected graph rule

The only graph-semantic repair authorized by Iter057BC is:

**An iteration dependency candidate may enter the transitive dependency DAG iff `rank(parent_iteration) < rank(child_iteration)`.**

Equal-rank and later-rank iteration mentions are recorded diagnostically but are not DAG edges and cannot propagate dependency.

No dependency keyword, deny rule, context radius, line-neighborhood rule, legacy anchor, provenance-sufficiency rule, census rule, ordering rule, normalization rule, target rule, or byte-decoding rule may be changed from the corresponding Iter057BB implementation.

## Byte-safe provenance semantics

Each implementation must independently:

1. acquire Git provenance as bytes without implicit decoding;
2. decode textual provenance using strict UTF-8 only;
3. represent every non-UTF8 provenance object by deterministic raw SHA256/identity and never silently coerce it;
4. infer no textual dependency statement from undecodable bytes;
5. classify fail-closed if an undecodable/insufficient object is classification-load-bearing and unresolved;
6. verify tracked historical/scientific tree integrity using the Iter057BA canonical serialization or an exactly equivalent reproduction.

## Independent reproduction

Two separately authored full adjudicators are required:

- a primary implementation preserving the Iter057BB primary context-radius parser;
- an independent implementation preserving the Iter057BB independent line-neighborhood parser.

They may share only frozen specifications/constants. They may not import/call/read each other's classifier or payload.

## Frozen outputs

Each lane must freeze:

- complete ordered 23-record census;
- ordered dependency classification of every record;
- classification evidence paths;
- accepted strict-EARLIER iteration edges;
- rejected EQUAL and LATER iteration candidates;
- DAG acyclicity;
- deterministic replay queue containing only direct/transitive dependents;
- complete undecodable provenance object list with load-bearing flags;
- unresolved-record list;
- canonical tracked-tree before/after digest;
- implementation SHA256 and scientific normalized SHA256.

## Frozen terminal classifier

`PASS_SCOPED_ITER057BD_STRICT_EARLIER_ONLY_DESCENDANT_DEPENDENCY_ADJUDICATION_INDEPENDENTLY_REPRODUCED` requires all of:

1. exact frozen AU census in both lanes and 23 unique records;
2. exact BA byte-safe authority and BC strict-earlier-only graph rule respected;
3. all accepted DAG edges are strictly earlier;
4. no later-rank candidate exists in either lane;
5. the rejected equal-rank candidate set agrees exactly between lanes and matches the 23 self-pairs certified by Iter057BC;
6. DAG is acyclic in both lanes;
7. every record is classified exactly once;
8. zero unresolved records;
9. zero classification-load-bearing undecodable provenance objects;
10. exact ordered classification agreement between lanes;
11. exact replay-queue agreement between lanes;
12. exact undecodable-provenance identity/load-bearing agreement;
13. historical tracked-tree integrity in both lanes;
14. two distinct implementation paths and SHA256 values;
15. no descendant scientific computation consumed/replayed, no target leakage, no historical mutation, no claim-lock promotion.

`BLOCKED_ITER057BD_UNRESOLVED_PROVENANCE` applies when execution and independent agreement are valid but one or more classifications remain genuinely unresolved.

`FAIL_TECHNICAL_ITER057BD_INDEPENDENT_REPRODUCTION_OR_GRAPH_CONTROL_FAILURE` applies when implementations disagree or a frozen graph/integrity/control criterion fails.

`INVALID_ITER057BD_CRITERIA_HISTORY_OR_TARGET_BLINDNESS_VIOLATED` applies to census/criteria mutation, target leakage, descendant replay, or historical mutation.

Green CI alone is not PASS.

## Authority ceiling and next action

A terminal scoped PASS adjudicates dependency only. It authorizes prospectively preregistering a replay gate for the earliest item in the certified replay queue; it does not itself replay or reclassify any descendant result.

## Claim locks

Theory established remains 0%; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
