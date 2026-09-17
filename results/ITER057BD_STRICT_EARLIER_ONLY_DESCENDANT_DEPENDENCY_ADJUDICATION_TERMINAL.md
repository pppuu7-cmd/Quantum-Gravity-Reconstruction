# Iter057BD terminal result — strict-earlier-only descendant dependency adjudication

Date: 2026-09-17
Gate: `ITER057BD_STRICT_EARLIER_ONLY_DESCENDANT_DEPENDENCY_ADJUDICATION`
Preregistration: `79ef5b0182bd8d4c90284c2cb95b110c8ed412f3`
Primary implementation: `478df6dd06f2a89df95571a0c0d9ae272acc1de6`
Independent implementation: `08c626d1a63c3ac405ecdbe4d0596e9ff186e84e`
Production head: `c0b38c7608b3d1e854842017bfce3040d1d09ceb`
Workflow: `.github/workflows/qgr-iter057bd-strict-earlier-dependency-adjudication.yml`
Actions run: `35252743698` (`completed/success`)

Artifacts:
- primary `10511895326`, digest `sha256:248a4eeb97887fa42ee73d46ee6793f534262816115ea1c128416e3ca93be398`;
- independent `10512320337`, digest `sha256:5db068888fbf82bb5e4b452ad1162bf93f4e783b0c055ea26c6295c760465986`;
- terminal `10511980653`, digest `sha256:b34e02c9ce9b1b4fe42c52060a9f493ad7989f277276efa4fdaf179d5e3af8ad`.

## Frozen classification

`PASS_SCOPED_ITER057BD_STRICT_EARLIER_ONLY_DESCENDANT_DEPENDENCY_ADJUDICATION_INDEPENDENTLY_REPRODUCED`

Terminal payload SHA256: `023c3798991c80665d0f20aae35e95d9de3185cfc6c83a655ec883a0c5e4bd76`.
Scientific normalized SHA256: `d7b714683f6909d3fa36fb265686317edb866b68b646c50687994b14a026aa8c`.

## Exact authority

Both separately authored full adjudicators independently reconstructed the same frozen 23-record post-Iter057X census from Iter057AU snapshot `616859890df95057556d265612c53da839a5848a` using byte-safe provenance acquisition and strict earlier-only DAG edge admissibility.

Terminal controls all pass:

- exact parent authorities;
- 23 unique records in both lanes;
- every accepted DAG edge strictly earlier;
- exact 23-record rejected same-iteration self-pair set in both lanes;
- zero later-rank candidates;
- acyclic DAG in both lanes;
- zero unresolved records;
- zero classification-load-bearing undecodable provenance objects;
- exact ordered classification agreement;
- exact replay-queue agreement;
- exact undecodable-provenance identity/load-bearing agreement;
- exact scientific normalized SHA agreement;
- distinct implementation paths and implementation SHA256 values (`2aade5aec7fbe74a0498269e2d4b1172a8840b6ccf736e5463d32acc9983ac58` vs `a445554bfb6c3391f50cafe78c6bc0be4e85b0d8594b72e0ce962b5172e3539d`);
- stable tracked-tree digest in both lanes;
- no descendant science consumed/recomputed, no target leakage, no historical mutation, no claim-lock promotion.

The only non-UTF8 provenance object remains the non-load-bearing Iter057AO part00 object with raw SHA256 `41af87477aa367978af6656abb5b84a75c8b11489dc40a9254e905cd5f69d162`.

## Certified replay queue

All 23 censused records are load-bearing dependents under the frozen definitions. The deterministic queue begins:

1. `results/ITER057Y_ACTIONS_PROVENANCE_AUDIT.md`
2. `results/ITER057Y_ONSHELL_FIRST_ORDER_Q2_Q4_Q6_Q8_RESPONSE_TERMINAL.md`
3. `results/ITER057Z_DODECIC_EINSTEIN_SEED_TERMINAL.md`
4. `results/ITER057AA_CORRECTED_DODECIC_SEED_WEYL3_EIGHTH_SOURCE_TERMINAL.md`
5. `results/ITER057AB_ONSHELL_FIRST_ORDER_Q2_Q4_Q6_Q8_Q10_RESPONSE.md`

then the transitive AC through AO chain, followed by direct AP/AQ/AR/AS records exactly as frozen in the terminal artifact.

The certified earliest replay record is:

`results/ITER057Y_ACTIONS_PROVENANCE_AUDIT.md`

## Authority semantics

This PASS adjudicates dependency only. It does not reclassify any historical descendant result. It authorizes prospectively preregistering a replay gate for the earliest certified queue item and nothing later until that replay is terminalized according to its own frozen criteria.

Historical Iter057AU remains BLOCKED and Iter057BB remains technical FAIL; Iter057BC remains its causal diagnostic PASS.

## Claim locks

Theory established remains 0%; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
