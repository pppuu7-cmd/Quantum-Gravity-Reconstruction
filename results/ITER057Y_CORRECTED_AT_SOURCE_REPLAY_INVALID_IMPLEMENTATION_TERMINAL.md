# Corrected Iter057Y first production — terminal INVALID_IMPLEMENTATION

Date: 2026-09-17
Gate: `ITER057Y_CORRECTED_AT_SOURCE_Q2_Q4_Q6_Q8_REPLAY`
Preregistration: `a6466be9dd3b2ce47bba5be1cacbd184b2161c8f`
Primary implementation: `acba870009f4c16309b599b130fa0f876f7df0aa`
Critic implementation: `b2436b13b126ef82abd653652887205a9c33c0c7`
Workflow: `5c60389abde0b0b3ae74c4b6463f98930048c728`
Execution PR: #24, closed unmerged
Execution head: `2230db4030ec9694ec80d032ce75b5d931b98bcc`
Actions merge ref: `d25cb4fa4a8ce228dbd4e493d35568b47d1814a4`
Actions run: `35266737571` (`completed/success`)

Artifacts:
- primary science `10516084813`, digest `sha256:a6df20e6d7d42aa943da3101eb1ef44b0ab43f5b16a0506ee81a4fc50f61065a`;
- outcome-blind Critic `10516249758`, digest `sha256:e786efee48d3493777eb58e0dfe62a92b7a8061d98b85092eaefee6ac565c0e0`;
- terminal `10516773069`, digest `sha256:3759cbd2f06aa523ac66c7e01fcc6cd35fb7ffeb8fb49511c88b210210ab3c30`;
- supplemental audit `10516828146`, digest `sha256:bcd40dec5dbaa8cb063b54aed5acf3652ab8b8dfdc6a5d539e8270ce5aeed26e`.

## Frozen terminal classification

`INVALID_IMPLEMENTATION_ITER057Y_CORRECTED_AT_SOURCE_REPLAY_CONTROL_FAILURE`

Terminal payload SHA256: `099c1f22257ab760a888afe963c9e7596846b97f6a4fdd0498f11a63c416f20e`.

This run is not reclassified post hoc.

## Diagnostic scientific ceiling

The source convention was the frozen Iter057BJ result `MAP_MINUS`, i.e. degree-six source `-AT`, with exact AT file/vector controls passing. The pinned historical Iter057Y evaluator was byte-identical to ref `98c82292885cec9a38fa400a5e08b1272104f8b8`.

Before the implementation control invalidated promotion, the primary exact calculation produced:

- matrix shape `1320 x 1650`;
- `rank(M)=1096`;
- `rank([M|b])=1096`;
- left nullity `224`;
- nullity `554`;
- canonical Bianchi rank `224`;
- all 224 primary compatibility contractions exactly zero;
- exact affine residual zero;
- 180 nonzero exact Q8 particular coefficients;
- full de Donder residual through degree seven zero;
- reduced `DG-source` through degree six zero;
- unreduced `DG-source` through degree six zero.

The outcome-blind Critic independently obtained canonical Bianchi rank `224` and zero nonzero compatibility contractions without reading the primary result artifact.

These values are diagnostic only because both lanes failed the same frozen V-parent provenance predicate.

## Causal implementation defect

Both primary and Critic required the canonical Iter057V Q6 JSON to contain:

`terminal_commit = 0d98273f8a1ec6071692571518f4faec1af8fa7b`.

The authoritative canonical V file `data/ITER057V_CANONICAL_Q6_RESPONSE.json`, frozen at commit `85b53cb708deec75f3d745ffdcebc80020761481`, has no `terminal_commit` field. Its authoritative serialization instead records the correct terminal scientific payload/provenance through:

- classification `PASS_SCOPED_ITER057V_UNRESTRICTED_ONSHELL_O_C6_Q2_Q4_Q6_RESPONSE_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_FOURTH_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN`;
- `production_head = 723598530f1c42cdc12eef25cd3e6fe169e807dd`;
- Actions run `35017363408`;
- job `104544061621`;
- artifact `10416157241`;
- source digest `sha256:3a0767e620d7609ffe24e37db1392c5c5904eb60b2c7eb2b19eeda744d3d0685`;
- matrix shape `574 x 840`;
- ranks `494/494`;
- 88 nonzero Q6 coefficients.

Separate terminal commit `0d98273f8a1ec6071692571518f4faec1af8fa7b` records the Iter057V terminal PASS and identifies the same production run/artifact/digest and canonical-data commit.

Therefore the failure is a provenance-validator representation defect: the evaluator required a field absent from the authoritative canonical serialization. It is not a Q8 scientific contradiction and does not authorize a PASS from this run.

A prospective repair may change only the V-parent authority predicate so that it verifies the actually frozen canonical V serialization plus the separate terminal V authority. No source, sign, lower response coefficient, Q8 evaluator, exactness criterion, solver, compatibility criterion or allowed scientific outcome may change.

`c6 = SYMBOLIC_UNFIXED`.

`beta = 1` remains unauthorized.

`theory_established = 0`.
