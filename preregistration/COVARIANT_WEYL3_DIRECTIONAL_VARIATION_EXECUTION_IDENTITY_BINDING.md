# COVARIANT_WEYL3_DIRECTIONAL_VARIATION_EXECUTION_IDENTITY_BINDING

Date: 2026-09-18
Status: PROSPECTIVE / FROZEN BEFORE SCIENTIFIC PRODUCTION
Parent scientific preregistration: `8c21ee233423deaff52d0fa552c027fa065a53a7`
Frozen panel: `1642dc7ca4204a4240635be68522f1731c8a9c50`

## Frozen panel identity

- neutral generator commit: `03377afec95801b5a49f47b85ddd9c9bf3326ac0`
- neutral generator blob: `68d5f96f3b93a729533887d871be2c3d01f90d61`
- frozen six-cell panel manifest SHA256: `f1390bc406d0db37fe10cc908db51c2eabcf5105904e4a71cc707d2dd3137c5f`

## Researcher identity

- path: `scripts/qgr_covariant_weyl3_researcher.py`
- implementation commit: `e7e36ee1b42ea5c9c685c1e44e4948619f72c880`
- Git blob: `e5426c9b0fc4edd5b6ac905f394bfec01e473cd6`
- role: exact direct directional variation of `sqrt(-g) I3`, explicit scalar-test `h/dh/d2h` decomposition, mechanical integration by parts, bulk witness.
- science imports: neutral panel generator only.

## Critic identity

- path: `scripts/qgr_covariant_weyl3_critic.py`
- implementation commit: `d3b56aa891cd0b505720564d367c143138ad4862`
- Git blob: `eae177a0f8fefc6b8abe83c07a40aede366823ad`
- role: independent exact covariant Euler source from algebraic Frechet/Weyl projection plus covariant double divergence.
- science imports: neutral panel generator only.

## Comparator and audit identity

- terminal comparator commit: `33615223896e575d7db51259f7cf5d10c627f546`
- terminal comparator blob: `14c2e77d84ce1a26612d11aaa98e25f3c5e96e25`
- static audit commit: `73c2f342dcc19346019687f8dba3d163aee39106`
- static audit blob: `e96f6d43f401a3f2eedd19911c6eccf12a5f87fe`

The comparator is the only component authorized to read both lane payloads. It performs no sign, scale, normalization, seed, or convention fitting.

## Workflow identity

- workflow path: `.github/workflows/qgr-covariant-weyl3-directional-variation.yml`
- workflow commit: `53355de38a1b21128f30595de56500e04b0a4db5`
- workflow blob: `24423a99c01151b1dd1576dffa9cefe8c46b3f38`

Production topology is frozen as source-lock/static-audit -> six Researcher matrix cells + six Critic matrix cells -> terminal comparator. Each scientific cell serializes and uploads its own immutable witness before the terminal job can read cross-lane outputs.

## Firewalls

- No corrected-Y, BJ/BH/BI, QF degree-flow, corrected-Q10, or symmetry-reduced gate is rerun.
- `c6 = SYMBOLIC_UNFIXED`.
- corrected Q10 remains LOCKED.
- no tolerance equality.
- green CI is not scientific PASS.
- a valid exact nonzero discrepancy is retained as scientific localization evidence and cannot trigger post-hoc sign/scale/normalization repair.
- execution defects remain BLOCKED and require a new prospective execution-only repair.

This binding authorizes exactly one production using the identities above.
