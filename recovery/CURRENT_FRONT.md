# QGR Current Research Front

Updated: 2026-09-17

## Programme infrastructure — terminal 100%

- Repository infrastructure: **100%**.
- Candidate-program / research-programme infrastructure: **100%**.
- Semantics: **Research-program / roadmap infrastructure readiness only; not probability of correctness, not theory completion, and not fraction of quantum gravity solved.**
- Frozen completion contract: `cf528fb6cd9f21611ca7f04ca5fb488fcd506359`.
- Promotion authorization: run/job `35181866332 / 105075552227`; artifact `10480172555`; artifact digest `sha256:99c60d2239ad6bc3115c1cc40561a0dee7c618f6d3b3a262064ac1ca002b5ea4`.
- A–P obligations: **16/16 PASS** independently in primary validator and Critic.
- Negative controls: **18/18 PASS**.
- Synthetic QGR->KMQGB handshake: infrastructure PASS, scientific state preserved as `BLOCKED`.
- Deterministic authorization bundle SHA256: `a3e27b16c2168aff836e5aae4e88f895d4ab6955afbde6d473fa94ee13e42720`.

This 100% does not promote any scientific R-stage and does not authorize any physical/quantum claim.

## Last terminal science — Iter057AT

`ITER057AT` remains terminal `PASS_SCOPED_ITER057AT_CORRECTED_HOMOGENEOUS_DEGREE6_SOURCE_INDEPENDENTLY_REPRODUCED`.

Preregistration: `6039cb2ed1380b549bced3d33634362ef57345d4`.
Implementation: `d45c6ba67459e2702909c2b864f5a5c24f104015`.
Production head: `c4e7ccc05ea1b8f4967379fc370812dfa99cce03`.
Actions run: `35198813733` (`completed/success`).
Terminal artifact: `10486973737` (`iter057at-terminal`).
Artifact digest: `sha256:bdb5affc949803e692d3680864746daa0c4175324d85e1ce7426d1b719621bb6`.
Corrected ordered 840-vector SHA256: `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`.
Adversarial referee review: `5d03f13fbc08004159ad8cbc7aa8c0eb20a035c1` — `CONFIRMED_SCOPED`.

Iter057AR remains historically BLOCKED on its frozen 2100-slot object. Historical Iter057AO/AQ authority and Iter057AP FAIL remain preserved. Historical Iter057X is not rewritten. Historical FAIL/BLOCKED results remain preserved.

## Iter057AU — preserved terminal BLOCKED

Gate: `ITER057AU_CORRECTED_DEGREE6_DESCENDANT_DEPENDENCY_ADJUDICATION`.
Preregistration: `616859890df95057556d265612c53da839a5848a`.
Implementation: `30aa968631d3c7f0ea82ea054b2abb14492748b3`.
Production head: `683b5f79899fc4a5677168cd7fd90d098cbc411e`.
Actions run: `35204162456` (`completed/failure`).
Terminal artifact: `10488818748` (`iter057au-terminal`).
Artifact digest: `sha256:2a8734dbc27fec1787318f017117fd82f8b2a433d346327a989892bdd10d33fc`.
Durable result: `c299683e28289788c53797e5ede1cafaf09f5431`.
Classification: `BLOCKED_ITER057AU_UNRESOLVED_PROVENANCE`.

Both dependency-reconstruction jobs reached the frozen classifier step and failed before producing the required primary/independent JSON payloads. No descendant scientific result was replayed or recomputed, and no partial lane evidence is promoted to authority.

## Iter057AV — terminal technical FAIL, referee confirmed scoped

Gate: `ITER057AV_TARGET_BLIND_ITER057AU_EXECUTION_REPAIR`.
Preregistration: `bfb6f31b9385d076695d7c3d199bf7da7b06bcc4`.
Frozen AU implementation: `30aa968631d3c7f0ea82ea054b2abb14492748b3`.
Frozen AU census head: `616859890df95057556d265612c53da839a5848a`.
Production head: `f92d67e6f1c8f619c8f0c8292bbd313ca6c7fdb7`.
Actions run: `35214572158` (`completed/success`).
Terminal artifact: `10493153837` (`iter057av-terminal`).
Artifact digest: `sha256:c1d2543242706c0792f7be4aa9a688dd204bf27b38967759b897c3ed1fc14668`.
Classification: `FAIL_TECHNICAL_ITER057AV_REPRODUCIBLE_FROZEN_AU_EXECUTION_DEFECT_IDENTIFIED`.
Adversarial referee review: `0a4a4ea8aa1ce4b88bdd83b501c4c9db321e92a6` — `CONFIRMED_SCOPED`.

Both isolated unchanged frozen Iter057AU executions used matching frozen provenance, exited `1`, produced no lane JSON, preserved a clean historical tree, and emitted identical stderr SHA256 `5517e7214732554985e70e5b8e208f9b25a3cd2679e47349ec28866a92926ef0` and normalized error fingerprint `2e83cbb6d0067e4b904632c372571ead9243f9a04b12e289e770f9bdbac84be1`. Common terminal error: `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8a in position 287: invalid start byte`.

Iter057AV establishes only a reproducible execution/provenance-reader defect. It does not reclassify Iter057AU, does not consume descendant science, and does not authorize replay.

## Iter057AW — terminal technical FAIL, referee confirmed scoped

Gate: `ITER057AW_BYTE_SAFE_PROVENANCE_READER_REPAIR`.
Preregistration: `4a137c9cc17858fb8e43875d169dc0a28ae3bb1d`.
Repair implementation: `1c4963a4bcc84a5bf331f0173c76b05d7a6a1864` (`scripts/qgr_iter057aw_bytesafe_reader.py`).
Production head: `c9f6422245e652caaecfbaa8cef8e91b1361af85`.
Actions run: `35220098375` (`completed/success`).
Terminal artifact: `10496493918` (`iter057aw-terminal`).
Artifact digest: `sha256:c85315aa4e396fe77d8e828f00ffdd0303f2557716a2c9f7688febb4f9d85d11`.
Classification: `FAIL_TECHNICAL_ITER057AW_BYTE_SAFE_REPAIR_CONTROL_FAILURE`.
Adversarial referee verdict: `CONFIRMED_SCOPED`.

Both isolated technical lanes reproduced the same invalid-fixture raw SHA256 `6d7c3014de78db7dc381089a15b61920d5831e36f5b4ef2fa175bf55db0eab61` and the same deterministic `NON_UTF8_PROVENANCE` sentinel. In both lanes `valid_utf8_roundtrip`, `non_utf8_sentinel`, `strict_decode_policy`, `missing_provenance_fail_closed`, `repair_scope_confined`, and `descendant_science_produced_or_consumed=false` passed. The sole reported failed frozen control in both lanes was `historical_result_tree_clean=false`, so `all_controls_pass=false` reproducibly and the preregistered technical FAIL classification is confirmed only at that scope.

This does not establish that the byte-safe decode mechanism itself is defective: the terminal failure is specifically the frozen historical-tree-cleanliness control. Iter057AU remains historically BLOCKED; no descendant science was replayed, consumed or reclassified. A replacement AU adjudication is not authorized by this FAIL.

## Iter057AX — terminal technical FAIL

Gate: `ITER057AX_HISTORICAL_TREE_CLEANLINESS_DIAGNOSTIC`.
Preregistration: `c81223eec7c972a2643a564ec99e9684766eeee4`.
Production head: `03472765cf27ac2a1534ac3546f17ed4d9e3bbc6`.
Actions run: `35223711465` (`completed/success`).
Terminal artifact: `10498825822` (`iter057ax-terminal`).
Artifact digest: `sha256:8217927c0bf3ce21f61e9733b98d2ac10e46073d69a77c1cb0439170d6efca2a`.
Durable result: `62b003f636f5a71072cb187d9791d203886d3063`.
Classification: `FAIL_TECHNICAL_ITER057AX_CLEANLINESS_ATTRIBUTION_NOT_ESTABLISHED`.

The terminal aggregate contains both independent lanes (`lane_count=2`) but reports that the frozen attribution controls or independent reproduction failed. The terminal aggregate does not expose which individual frozen control failed; therefore no narrower causal diagnosis is inferred and no partial lane evidence is promoted.

Iter057AX does not reclassify Iter057AW or Iter057AU and consumed/replayed no descendant science.

## Iter057AY — terminal scoped PASS

Gate: `ITER057AY_EMPTY_DIRECTORY_GIT_STATUS_SEMANTICS_DIAGNOSTIC`.
Preregistration: `b4f252298e4821b93b0ad01e797a1e6d41c5f58d`.
Implementation: `9d81441b06d62b12a983693c7bf9e8f715d21961`.
Production head: `0fdab1e5bcd91dd2018249a18a3b40739d2982e1`.
Actions run: `35232316613` (`completed/success`).
Terminal artifact: `10502222783` (`iter057ay-terminal`).
Artifact digest: `sha256:2fde0094b549c202eb6d7d0cd0761020802e37ae3eae7008629958a931b017a8`.
Durable result: `defd025becf22b9087a4f66f13d2a38dc20880fc`.
Classification: `PASS_SCOPED_ITER057AY_EMPTY_DIRECTORY_GIT_STATUS_SEMANTICS_REPRODUCED`.

The terminal aggregate contains two lane payloads, `all_controls_pass=true`, bit-for-bit normalized agreement, and identical normalized SHA256 `ce448d6807e8861e0708bafcacb644eb3cbb465a472f9086d12ac111835d6123` in both lanes. Thus the frozen technical hypothesis is reproduced: the empty harness-owned untracked directory is omitted by Git porcelain until a sentinel file is present, while tracked-tree integrity is preserved under the frozen controls.

This is a technical scoped PASS only. Iter057AU remains BLOCKED; Iter057AW and Iter057AX remain terminal technical FAILs; no descendant science was consumed or reclassified.

## Iter057AZ — preregistered, not yet produced

Gate: `ITER057AZ_BYTE_SAFE_REPAIR_CLEANLINESS_REDESIGN`.
Preregistration: `31def60c38017c8fd9595e1a2772bc75cad42aba` (`prereg/ITER057AZ_BYTE_SAFE_REPAIR_CLEANLINESS_REDESIGN.md`).
Status: `PROSPECTIVELY PREREGISTERED, NOT YET PRODUCED`.

Frozen object: a new byte-safe provenance-reader repair certificate using strict byte acquisition/UTF-8 handling and a prospectively defined cleanliness predicate over tracked historical/scientific files, with harness-owned untracked outputs reported separately. Two independently implemented lanes are required; descendant science remains forbidden. A scoped PASS may authorize only a separately preregistered future dependency-adjudication retry and does not itself reclassify Iter057AU/AW/AX.

## Next bounded step

No authoritative workflow is active. `ITER057AZ` is already prospectively frozen by commit `31def60c38017c8fd9595e1a2772bc75cad42aba`. The next run may implement exactly that frozen gate and, because its two-lane certificate computation is nontrivial, launch one `fail-fast:false` GitHub Actions matrix and stop without waiting. Do not alter the frozen Iter057AZ controls, rerun Iter057AU, or consume descendant science.

## Frozen KMQGB interface

KMQGB commit `d23f34cba57b220dd29474c0651bc727d6d85eae`, Candidate Gravity record v1.3, RQIR Core `1.0 / FROZEN`. Drift fails closed as `KMQGB_INTERFACE_VERSION_DRIFT`.

## Claim locks

Theory established: **0%**. Experimental confirmation, `beta=1`, fixed/running `c6`, strong-hyperbolicity, ghost, quantum-unitarity, interacting-measure, regulator-removal, UV-completion, new-physics and KMQGB `NEW_REQUIRED` claims all remain unauthorized/false.

Finite/local classical certificates remain finite/local classical certificates; infrastructure completion cannot promote their scientific scope. Finite certificate != theorem; classical != quantum; diagnostic != closure.
