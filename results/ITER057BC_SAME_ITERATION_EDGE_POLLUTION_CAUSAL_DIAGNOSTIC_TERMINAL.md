# Iter057BC terminal result — same-iteration edge pollution causal diagnostic

Date: 2026-09-17
Gate: `ITER057BC_SAME_ITERATION_EDGE_POLLUTION_CAUSAL_DIAGNOSTIC`
Preregistration: `e8c7e1d95c2b12b0b513e5431d053a92d8141455`
Primary diagnostic implementation: `4d218fbc1a5c25052c684596f9b5f2399132978e`
Independent diagnostic implementation: `64db5a91f4ba8804bad4c7f377d3de0395a45cea`
Production head: `e2f3b4708279d3cac6295ae0874d5857a287d441`
Workflow: `.github/workflows/qgr-iter057bc-same-iteration-edge-diagnostic.yml`
Actions run: `35252341127` (`completed/success`)

Artifacts:
- primary `10510585584`, digest `sha256:f0de75d9a03ecfe57d41d594f5db641a6c8aae0466d3feac8e9ab714beea6af0`;
- independent `10509604965`, digest `sha256:b1552d5cbadee32d0e7b6a517e6bcd13f05974e4166a6e62d0f452549f3e8551`;
- terminal `10510560753`, digest `sha256:75ce27cf3f66fbc5d7d4b3d2df7ade1c4c5ef8e88f4826dfbbb1d40aa580ee49`.

## Frozen classification

`PASS_SCOPED_ITER057BC_SAME_ITERATION_EDGE_POLLUTION_CAUSALLY_LOCALIZED`

Terminal payload SHA256: `5ebe5d0891a5f3aec8d4faa9e84684b4650b925ca6125142dd292807a4c4f6cf`.
Frozen reproduced Iter057BB scientific normalized SHA256: `5cba0b3b3e8475b974d8cf8f633875a7a1ab63f92b1503cbb353633ca2ac9189`.

## Exact causal result

Both separately authored diagnostics reproduced the exact frozen Iter057BB parser authorities before intervention. The primary parser exposed 86 iteration-dependency candidates: 63 EARLIER, 23 EQUAL and 0 LATER. The independent parser exposed 85 candidates: 62 EARLIER, 23 EQUAL and 0 LATER.

The 23 EQUAL pairs agree exactly between implementations. Every EQUAL pair is a self-reference from a censused record to its own iteration label. There are no later-iteration edges in either implementation.

Restricting the diagnostic graph to strict EARLIER candidates only:

- restores exact acyclicity in both lanes;
- leaves the ordered 23-record dependency classifications unchanged in both lanes;
- leaves the complete 23-record replay queue unchanged in both lanes;
- leaves the byte-safe undecodable-provenance census unchanged;
- preserves exact cross-lane agreement of the filtered scientific outputs.

The only non-UTF8 provenance object remains `c1616a7ba5d540e14c667ad49c53f873ae21a0cc:scripts/iter057ao_phase2_parts/part00.txt`, raw SHA256 `41af87477aa367978af6656abb5b84a75c8b11489dc40a9254e905cd5f69d162`, and it remains non-load-bearing for classification.

Thus the Iter057BB `dag_acyclic=false` control failure is causally localized to admitting same-iteration provenance mentions into a graph whose frozen transitive-dependency semantics require earlier-result dependencies. The one-edge difference in the two EARLIER candidate sets is redundant for all ordered classifications and replay-queue membership and does not affect this causal result.

## Authority semantics

Iter057BB remains historical terminal technical FAIL and Iter057AU remains historical BLOCKED. Iter057BC itself does not authorize descendant replay. It authorizes only a separately preregistered corrected dependency-adjudication gate whose sole graph repair is strict earlier-only iteration-edge admissibility.

## Claim locks

Theory established remains 0%; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
