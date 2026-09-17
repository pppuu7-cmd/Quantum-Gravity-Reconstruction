# Iter057BH — Iter057Y Source / Equation Convention Adjudication

Status: **PROSPECTIVELY PREREGISTERED / NOT YET PRODUCED**  
Date: 2026-09-17

## Purpose

Before any corrected Iter057Y replay, determine prospectively and exactly how the corrected Iter057AT Euler/source vector maps into the historical Iter057Y `source` object and field equation. The sign/convention must be fixed from frozen code semantics and exact legacy/corrected coefficient reconstruction, never from corrected-Y solvability, rank, Q8 coefficients, or comparison outcome.

No corrected Iter057Y solve is permitted in this gate.

## Frozen parents

Historical Iter057X source lineage:

- implementation `920b73f8430983255081b9bcd3ec6d222b737b08`;
- canonical source file `data/ITER057X_CANONICAL_SOURCE_DEGREE6.csv`;
- terminal result `4ab5592cfc6ef5fb69d3a96fa4433ef22d51af8b`;
- historical degree-six source payload SHA256 `7a85a8b78e6876810ecefc6e1b37efea956caa41f26d54f4f8b9dcf16ca45249`.

Historical Iter057Y equation lineage:

- preregistration `e372123b622bd1bb94e641b82097687a29416f65`;
- implementation `98c82292885cec9a38fa400a5e08b1272104f8b8`;
- historical terminal `cb2758238daba9ecf9c86e01e171f6c6d31c72b9`.

Corrected operator/source authority:

- Iter057AQ implementation `23435e772cf82c985ed919aa2411d59667ffb3ff`;
- Iter057AQ production head `c04cc004b9ef5aadcef70fd25d5129a80670335d`;
- Iter057AQ terminal classification `PASS_SCOPED_ITER057AQ_DISCREPANCY_LOCALIZED_TO_LEGACY_P_CONSTRUCTION`;
- Iter057AQ establishes `O_X(P_L)=O_AO(P_L)` and `O_X(P_F)=O_AO(P_F)` with the legacy-vs-Frechet source difference confined to degree six.

Iter057AT/BG corrected degree-six authority:

- Iter057AT production head `c4e7ccc05ea1b8f4967379fc370812dfa99cce03`;
- Iter057AT ordered 840-vector SHA256 `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`;
- durable source file `data/ITER057AT_CANONICAL_SOURCE_DEGREE6.csv`;
- durable source file SHA256 `1cae5a82d1345b9d9a77bcd3d6a91f6d5747629b5ac9e091bbb6c5a7ade3025b`;
- Iter057BG durable PASS result commit `c9474e2f0c50268f314c4001acc3834f80ee7294`;
- Iter057BG terminal payload SHA256 `3491c1c9efa27e39127905d209c4b1c365d63038d639bece41cb1224d5939151`.

`c6` remains symbolic/unfixed.

## Frozen convention question

Let `AT` denote the ordered corrected degree-six vector serialized by Iter057AT/BG, i.e. the degree-six coefficients of the corrected `Edown = O_X(P_F) = O_AO(P_F)` object.

Determine exactly which mapping is inherited by the historical Iter057Y `source` variable:

- `MAP_PLUS`: `S_std_corrected = +AT`; or
- `MAP_MINUS`: `S_std_corrected = -AT`.

No third sign/scale/basis map is authorized. If neither exact map is established, the gate fails closed.

## Lane A — static semantic/dataflow adjudication

A target-blind analyzer must inspect the exact frozen source files and establish, without executing corrected Y science:

1. Iter057X constructs `Edown` and then defines the serialized historical source from a syntactically explicit transformation of `Edown`;
2. identify whether that transformation is identity or unary negation;
3. Iter057AT primary serializes `aq.x_operator(P_F,...)`, while its independent constructor serializes AO `Edown`;
4. Iter057AQ `x_operator` returns `Edown`;
5. Iter057Y loads the historical X CSV values into its `source` tensor;
6. Iter057Y defines its residual as `DG - source` (both initial and terminal reduced/unreduced controls), and its affine RHS is built as the negative of the current residual rather than by redefining source sign;
7. no corrected-Y rank, solvability, Q8 coefficient, or descendant outcome is read.

The lane must output one of `MAP_PLUS`, `MAP_MINUS`, or `UNRESOLVED` and the implied corrected field convention.

## Lane B — exact coefficient adjudication

Freshly execute the pinned Iter057AQ production implementation at `c04cc004b9ef5aadcef70fd25d5129a80670335d` with exact rational arithmetic and target coefficients still forbidden during operator construction.

Using the produced complete cells:

- reconstruct the full 840-slot degree-six historical X vector from `data/ITER057X_CANONICAL_SOURCE_DEGREE6.csv` in the exact `OX_PL` degree-six ordering;
- classify its relation to the freshly computed `OX_PL` degree-six vector as `SAME`, `NEGATIVE`, or `NEITHER` by exact rational equality over all 840 slots;
- reconstruct the full 840-slot corrected AT vector from `data/ITER057AT_CANONICAL_SOURCE_DEGREE6.csv` in the exact `OX_PF` degree-six ordering;
- require the AT vector to equal freshly computed `OX_PF` bit-for-bit and have SHA256 `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`;
- require the historical X vector to match its canonical CSV exactly with 140 nonzero rows and no fitting.

The inherited corrected source map is determined solely by the historical relation:

- historical X `SAME` to `OX_PL` => `MAP_PLUS`;
- historical X `NEGATIVE` to `OX_PL` => `MAP_MINUS`;
- otherwise `UNRESOLVED`.

This lane may not execute the Iter057Y response solve.

## Frozen terminal classifier

Two positive terminal classifications are prospectively allowed:

- `PASS_SCOPED_ITER057BH_Y_SOURCE_CONVENTION_MAP_PLUS_AT_INDEPENDENTLY_ESTABLISHED`;
- `PASS_SCOPED_ITER057BH_Y_SOURCE_CONVENTION_MAP_MINUS_AT_INDEPENDENTLY_ESTABLISHED`.

A PASS requires all of:

1. static lane and exact coefficient lane independently return the same map;
2. map is exactly `MAP_PLUS` or `MAP_MINUS`;
3. pinned AQ controls pass and `OX_PL=OAO_PL`, `OX_PF=OAO_PF` remain exact;
4. exact historical X relation is SAME or NEGATIVE over all 840 degree-six slots, never a fitted ratio;
5. corrected AT equals fresh `OX_PF` over all 840 slots;
6. historical Iter057Y equation semantics `DG - source = 0` are established from frozen code;
7. no corrected-Y rank/solvability/Q8 output is computed or consumed;
8. no historical file is modified and no claim lock is promoted.

`BLOCKED_ITER057BH_Y_SOURCE_CONVENTION_UNRESOLVED` applies if exact frozen evidence cannot distinguish the two maps.

`FAIL_TECHNICAL_ITER057BH_STATIC_AND_EXACT_CONVENTION_EVIDENCE_DISAGREE` applies if valid lanes disagree or a frozen integrity/exactness control fails.

`INVALID_ITER057BH_CORRECTED_Y_OUTCOME_LEAKAGE_HISTORY_MUTATION_OR_POSTHOC_MAP` applies if corrected-Y response outcomes influence the map, if historical records are mutated, or if a sign/scale map is fitted post hoc.

## Post-PASS authorization

Only after terminal PASS may the corrected Iter057Y atomic replay bundle be preregistered. The replay must consume `S_std_corrected` with the exact map certified here, run science first, and run the supplemental Actions provenance audit second as certified by Iter057BF.

The replay's PASS/FAIL/BLOCKED criterion must be based on exact response-system mathematics, not agreement with historical Y.

## Claim locks

Theory established remains 0%; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
