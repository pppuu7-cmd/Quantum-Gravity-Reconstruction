# Iter057BF terminal result — Iter057Y replay-order literal-extraction repair

Date: 2026-09-17
Gate: `ITER057BF_ITER057Y_REPLAY_ORDER_LITERAL_EXTRACTION_REPAIR`
Preregistration: `f80032eb7f346d57205e858cd2a55be1eeb42649`
Repaired primary implementation: `a5f0b5fa3fa3bddb8761e457528f7ab1feea90f4`
Independent implementation: unchanged Iter057BE `f199b96607d21b8adf1d03ddcf68ef7a24f0e8a5`
Production head: `6bd1a84662b7b0c71da500fdadb66406253c6057`
Workflow: `.github/workflows/qgr-iter057bf-y-replay-order-repair.yml`
Actions run: `35253961967`

Artifacts:
- repaired primary `10511677316`, digest `sha256:2b92cc6b002abe1d1ee442a682d2c08ad05235380133a60009cb88a5812c0060`;
- unchanged independent `10512042094`, digest `sha256:ca3c54981d0a1e34f785522ecc02708cd73d9b27fc503b35566ae289f136a538`;
- terminal `10512346968`, digest `sha256:0700236f8c61cb28c3ec9d98e4997cc07afe0080b282756324396e4556303804`.

## Frozen classification

`PASS_SCOPED_ITER057BF_ITER057Y_REPLAY_BUNDLE_ORDER_SCIENCE_BEFORE_AUDIT_REPAIRED_PRIMARY_AND_INDEPENDENTLY_REPRODUCED`

Terminal payload SHA256: `e5956cb7535e080f775432c68b3c02f6b8fffe39eb06c7c2d634411b1062f818`.

## Exact authority

Both lanes consumed the exact same five Iter057BE evidence objects and reproduced their frozen SHA256 values. All frozen controls pass.

The repaired primary extracted `supplemental_reproduction_note` from exactly two adjacent Python STRING literals and reconstructed the exact semantic value:

`Corrected only Iter057V provenance metadata validation; scientific inputs, coefficients, affine system, solve and replay are unchanged.`

The unchanged independent lane retained implementation SHA256 `ea42d3fafece8ee8bb22ca5c832c4334625b872c5eda77c1478ef4b8dda6c62b` and again independently established the wrapper call flow and Git ancestry.

The authoritative same-iteration replay unit is:

1. `results/ITER057Y_ONSHELL_FIRST_ORDER_Q2_Q4_Q6_Q8_RESPONSE_TERMINAL.md` — science first;
2. `results/ITER057Y_ACTIONS_PROVENANCE_AUDIT.md` — supplemental provenance audit second.

Ordering relation: `SCIENCE_BEFORE_AUDIT`.

The two records form one atomic replay bundle for scheduling. This refines replay order only; Iter057BD dependency membership is unchanged.

## Authority semantics

Iter057BE remains historical BLOCKED. Historical Iter057Y remains unchanged. Iter057BF does not itself recompute Q8 or create a corrected Y result. It authorizes only a separately preregistered replay gate for the atomic Iter057Y bundle using the corrected Iter057AT degree-six source authority.

## Claim locks

Theory established remains 0%; no experimental confirmation; `beta=1` unauthorized; `c6` symbolic/unfixed; no hyperbolicity/ghost/unitarity/global-measure/regulator-removal/UV-completion/new-physics/KMQGB-NEW_REQUIRED claim is authorized.
