# Iter057BB terminal result — byte-safe descendant dependency adjudication retry

Date: 2026-09-17
Gate: `ITER057BB_CONDITIONAL_BYTE_SAFE_DESCENDANT_DEPENDENCY_ADJUDICATION_RETRY`
Preregistration: `eb864872be1db63d0588296c606b759b7b1495c8`
Frozen AU census: `616859890df95057556d265612c53da839a5848a`
Primary implementation: `605e0ff44496e4792618602dd0819b4ca599eb80`
Independent implementation: `12947c2cc7788f98d6a47df0457d235cf6715791`
Production head: `6cbae90b3c6d93cbc0b1569d846f805b2e2a2553`
Workflow: `.github/workflows/qgr-iter057bb-byte-safe-dependency-adjudication.yml`
Actions run: `35251292539` (`completed/success`)

Artifacts:
- primary `10508709546`, digest `sha256:860d59d95f073844025687d4378200565ca5d7239c7825f441c2b9935b5a4a2a`;
- independent `10508704797`, digest `sha256:b058ab6b1dc9b478c6b9e8216d59abd483e7ebdc438d8b3d741da8d4a6db9a67`;
- terminal `10509760965`, digest `sha256:8198245f204af5dc479ba1b84637af77051e4400ba950e41754c087e3cd564b1`.

## Frozen terminal classification

`FAIL_TECHNICAL_ITER057BB_INDEPENDENT_REPRODUCTION_OR_DAG_CONTROL_FAILURE`

Terminal payload SHA256: `05e93f9031a8875ea513456cfbbe4bbcb5c6f0972c3cafce70d62cd9ccd0ea6e`.
Scientific normalized SHA256: `5cba0b3b3e8475b974d8cf8f633875a7a1ab63f92b1503cbb353633ca2ac9189`.

## What did reproduce exactly

The two separately authored implementations agree exactly on all dependency-science outputs:

- complete census: 23 records;
- ordered classifications: exact agreement;
- deterministic replay queue: exact agreement;
- undecodable provenance identities/load-bearing flags: exact agreement;
- scientific normalized SHA256: exact agreement;
- distinct implementation SHA256 values (`0f1a760b99b78a9482dda83dc6dbc9f3411dcfcf278e425a2fd307f5ce991b43` vs `475320d515fee801b2dff9a8266e7bdf2f7ed844ab9ba7df21b2bb3ba77eb124`);
- tracked-tree digest stable in both lanes;
- no descendant science consumed/recomputed and no target-outcome use.

There are **zero unresolved census records** and **zero classification-load-bearing undecodable provenance objects**.

Exactly one non-UTF8 provenance content object is observed in both lanes:

- source `c1616a7ba5d540e14c667ad49c53f873ae21a0cc:scripts/iter057ao_phase2_parts/part00.txt`;
- raw length 5976;
- raw SHA256 `41af87477aa367978af6656abb5b84a75c8b11489dc40a9254e905cd5f69d162`;
- owner `results/ITER057AO_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_TERMINAL.md`;
- classification-load-bearing: `false`.

Thus the historical UTF-8 execution blocker is removed at this gate; the terminal FAIL is not caused by unresolved UTF-8 provenance or independent-classification disagreement.

## Failed frozen control

Both lane payloads report `dag_acyclic=false`, making both terminal lane-integrity controls false. Under the prospectively frozen classifier this is a technical FAIL, not a PASS, despite exact agreement elsewhere. Historical Iter057AU remains BLOCKED and no replay is authorized by Iter057BB.

## Post-terminal causal localization

A read-only forensic audit of both frozen lane artifacts partitions every non-earlier graph edge by iteration rank. In both independently produced payloads:

- non-earlier edges: 23;
- equal-rank edges: 23;
- later-rank edges: 0;
- every one of the 23 equal-rank edges is an iteration self-reference `ITER057N -> ITER057N` for the child record's own iteration label.

This is consistent with a narrowly testable defect hypothesis: same-iteration provenance mentions were admitted into the dependency-edge set before the acyclicity check, although the frozen AU/BB method says transitive propagation is only along explicit **earlier-result dependencies**. This forensic observation does not reclassify Iter057BB; it motivates a separate prospective diagnostic/repair gate.

## Authority ceiling

Iter057BB does not authorize descendant replay. Iter057AU remains historical BLOCKED. Iter057BB remains historical technical FAIL. Theory established remains 0%; no experiment; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
