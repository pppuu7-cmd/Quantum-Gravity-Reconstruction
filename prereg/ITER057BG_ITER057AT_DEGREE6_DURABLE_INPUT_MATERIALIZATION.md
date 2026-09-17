# Iter057BG — Iter057AT Corrected Degree-Six Durable Input Materialization

Status: **PROSPECTIVELY PREREGISTERED / NOT YET PRODUCED**  
Date: 2026-09-17

## Purpose

Iter057BF authorizes a corrected Iter057Y science-first replay bundle, but the corrected Iter057AT 840-slot degree-six source currently exists authoritatively in Actions lane artifacts rather than as a reusable machine-readable repository input. This gate materializes that already-authoritative source as a durable sparse CSV without changing its science.

No Iter057Y solve or descendant replay is permitted in this gate.

## Frozen parent authority

Iter057AT:

- preregistration `6039cb2ed1380b549bced3d33634362ef57345d4`;
- production head `c4e7ccc05ea1b8f4967379fc370812dfa99cce03`;
- Actions run `35198813733`;
- primary artifact `10486378527`, digest `sha256:7e923b6b3124d3bd8a95488a8c7b184ce86bb683a0076a8fb26098424ac838e7`;
- independent artifact `10486998588`, digest `sha256:29a01128e1561c42fa15e06989c1967089d40bd9d960935215a412c1ce226f2f`;
- terminal artifact `10486973737`, digest `sha256:bdb5affc949803e692d3680864746daa0c4175324d85e1ce7426d1b719621bb6`;
- terminal classification `PASS_SCOPED_ITER057AT_CORRECTED_HOMOGENEOUS_DEGREE6_SOURCE_INDEPENDENTLY_REPRODUCED`;
- ordered 840-vector SHA256 `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`;
- slot count 840;
- nonzero normalized coefficient count 140;
- `c6 = SYMBOLIC_UNFIXED_FACTORED_OUT`.

A local pre-registration extraction diagnostic from the two immutable AT lane artifacts established that their ordered vectors are bit-for-bit identical and that the deterministic sparse CSV representation defined below has SHA256 `1cae5a82d1345b9d9a77bcd3d6a91f6d5747629b5ac9e091bbb6c5a7ade3025b`. This diagnostic does not itself create repository authority; the exact bytes/hash are frozen here before the repository candidate is committed.

## Frozen repository object

Candidate path:

`data/ITER057AT_CANONICAL_SOURCE_DEGREE6.csv`

Exact representation:

1. UTF-8/LF text;
2. metadata comment lines `# key=value` recording the frozen AT identifiers above;
3. CSV header exactly `a,b,t,x,y,z,value`;
4. exactly the 140 nonzero entries of the AT ordered 840-vector, in the same order as the full vector;
5. `pair=[a,b]`, `alpha=[t,x,y,z]`, `value` is the exact normalized rational coefficient string from the AT vector;
6. zero slots are omitted only from the sparse CSV representation, never from reconstruction of the full 840-vector;
7. candidate file SHA256 must equal `1cae5a82d1345b9d9a77bcd3d6a91f6d5747629b5ac9e091bbb6c5a7ade3025b`.

## Frozen reconstruction

The full 840-vector is reconstructed using the exact Iter057AT ordering:

- ten frozen symmetric `PAIRS` in the AT implementation order;
- all homogeneous four-variable multi-indices of total degree six in the AT `alphas(6)` order;
- sparse CSV value where present, otherwise exact zero;
- record shape `{pair:[a,b], alpha:[t,x,y,z], value:<canonical rational string>}`.

The canonical sorted compact JSON SHA256 of that reconstructed list must be exactly:

`5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`.

## Independent reproduction requirement

Two fresh pinned reconstructions from Iter057AT production head `c4e7ccc...` are required:

- primary AT constructor mode;
- independent AT constructor mode.

Each must run from the pinned production tree, without reading the candidate CSV during source construction, and must reproduce the same 840-vector SHA256 `5d070732...`. After construction, each lane independently compares its full ordered vector bit-for-bit with the full vector reconstructed from the committed sparse CSV.

## Frozen terminal classifier

`PASS_SCOPED_ITER057BG_ITER057AT_CORRECTED_DEGREE6_DURABLE_INPUT_INDEPENDENTLY_REPRODUCED` requires all of:

- candidate file SHA256 exact `1cae5a82...`;
- metadata identifiers exact;
- 140 unique nonzero rows, all homogeneous degree six, all exact rationals;
- sparse-to-full reconstruction yields exactly 840 slots and vector SHA `5d070732...`;
- pinned primary AT reconstruction yields exactly the same 840-vector;
- pinned independent AT reconstruction yields exactly the same 840-vector;
- primary and independent fresh vectors agree bit-for-bit;
- no historical target/source substitution, no Y/descendant science consumed/recomputed, no claim-lock promotion.

`FAIL_TECHNICAL_ITER057BG_MATERIALIZATION_OR_INDEPENDENT_REPRODUCTION_MISMATCH` applies if bytes, metadata, reconstruction or independent reproduction disagree.

`BLOCKED_ITER057BG_PINNED_AT_REPRODUCTION_NOT_REALIZED` applies if the pinned exact constructors cannot execute.

`INVALID_ITER057BG_HISTORY_TARGET_OR_DESCENDANT_SCOPE_VIOLATED` applies to historical mutation, target fitting or descendant replay.

## Authority semantics

A scoped PASS creates only a durable repository representation of the already-terminal Iter057AT corrected degree-six source. It does not create a new physical claim. Only after PASS may a separately preregistered corrected Iter057Y bundle replay consume this CSV.

## Claim locks

Theory established remains 0%; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
