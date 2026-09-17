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

## Iter057AW — active preregistered byte-safe provenance-reader repair

Gate: `ITER057AW_BYTE_SAFE_PROVENANCE_READER_REPAIR`.
Preregistration: `4a137c9cc17858fb8e43875d169dc0a28ae3bb1d`.
Repair implementation: `1c4963a4bcc84a5bf331f0173c76b05d7a6a1864` (`scripts/qgr_iter057aw_bytesafe_reader.py`).
Workflow launch head: `c9f6422245e652caaecfbaa8cef8e91b1361af85` (`.github/workflows/qgr-iter057aw-bytesafe-reader.yml`).
Status: **ACTIVE — terminal workflow result not yet consumed**.

The repair is confined to byte-safe Git provenance reading: `git show` stdout is captured as bytes, valid candidate text is decoded with strict UTF-8, and undecodable bytes fail closed as deterministic `NON_UTF8_PROVENANCE` carrying only ref/path/raw-byte SHA256. No descendant dependency adjudication is executed in this gate. Two isolated technical reproductions use synthetic UTF-8 and `0x8a` fixtures, `fail-fast:false`, and a terminal aggregate named `iter057aw-terminal`.

Iter057AU remains historically BLOCKED. No descendant scientific payload may be replayed, consumed or reclassified by Iter057AW.

## Next bounded step

Resolve only the Iter057AW workflow launched from head `c9f6422245e652caaecfbaa8cef8e91b1361af85`. If non-terminal, check status/provenance only and stop. If terminal, consume only the frozen Iter057AW preregistration and `iter057aw-terminal` aggregate, record PASS/FAIL/BLOCKED/INVALID exactly under the frozen criteria, update recovery, and stop. Do not rerun Iter057AU and do not consume descendant science.

## Frozen KMQGB interface

KMQGB commit `d23f34cba57b220dd29474c0651bc727d6d85eae`, Candidate Gravity record v1.3, RQIR Core `1.0 / FROZEN`. Drift fails closed as `KMQGB_INTERFACE_VERSION_DRIFT`.

## Claim locks

Theory established: **0%**. Experimental confirmation, `beta=1`, fixed/running `c6`, strong-hyperbolicity, ghost, quantum-unitarity, interacting-measure, regulator-removal, UV-completion, new-physics and KMQGB `NEW_REQUIRED` claims all remain unauthorized/false.

Finite/local classical certificates remain finite/local classical certificates; infrastructure completion cannot promote their scientific scope. Finite certificate != theorem; classical != quantum; diagnostic != closure.
