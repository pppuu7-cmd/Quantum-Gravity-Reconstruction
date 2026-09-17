# Iter057BG terminal result — Iter057AT corrected degree-six durable input materialization

Date: 2026-09-17
Gate: `ITER057BG_ITER057AT_CORRECTED_DEGREE6_DURABLE_INPUT_MATERIALIZATION`
Preregistration: `180be23933c9cc4f78dbf8e1fea6cb76b9c74fc8`
Candidate commit: `6fcde386155fc3b9b1ec6ec98cdca5a01f25c468`
Verifier implementation: `411eac070d762197180b961663c58057483ff312`
Production head: `18e631c98896260bf62aea053278985574ec96d5`
Workflow: `.github/workflows/qgr-iter057bg-at-source-materialization.yml`
Actions run: `35254397613` (`completed/success`)

Artifacts:
- primary `10512108086`, digest `sha256:c1b06f1c37a5d8b9083d0000d2a0b0b77c678cfe3c7f612220e5ceed43d58147`;
- independent `10511678379`, digest `sha256:80cd5fbef9d80639dfa89cf13150a70a74daa0be3560ff45e21d7f6dbf25d992`;
- terminal `10511953237`, digest `sha256:26d639e7af3e22d6cc0b1507d23189ac127a14b67a22977303a63f98226e75a1`.

## Frozen classification

`PASS_SCOPED_ITER057BG_ITER057AT_CORRECTED_DEGREE6_DURABLE_INPUT_INDEPENDENTLY_REPRODUCED`

Terminal payload SHA256: `3491c1c9efa27e39127905d209c4b1c365d63038d639bece41cb1224d5939151`.

## Exact authority

The committed candidate `data/ITER057AT_CANONICAL_SOURCE_DEGREE6.csv` has exact SHA256:

`1cae5a82d1345b9d9a77bcd3d6a91f6d5747629b5ac9e091bbb6c5a7ade3025b`.

It contains exactly 140 unique nonzero homogeneous total-degree-six normalized coefficients. Sparse reconstruction into the frozen Iter057AT pair/alpha order yields exactly 840 slots and canonical ordered-vector SHA256:

`5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`.

Both fresh pinned Iter057AT constructor modes were recomputed from production head `c4e7ccc05ea1b8f4967379fc370812dfa99cce03` and independently yielded that exact same 840-vector. The sparse reconstruction agrees bit-for-bit with both fresh vectors. All frozen terminal controls pass and no descendant science was consumed.

## Authority semantics

This PASS creates only a durable repository representation of the already-terminal Iter057AT corrected degree-six source. It does not resolve the source-vs-equation sign convention needed by the historical Iter057Y response equation and therefore does not by itself authorize substituting the file into the Y RHS.

A separate prospective convention-adjudication gate is required before Y replay.

## Claim locks

Theory established remains 0%; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
