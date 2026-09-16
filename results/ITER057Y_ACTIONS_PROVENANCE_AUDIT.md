# Iter057Y supplemental Actions provenance audit

Date: 2026-09-16
Terminal Iter057Y authority: `cb2758238daba9ecf9c86e01e171f6c6d31c72b9`
Corrected provenance wrapper: `8d5936b988c57d44e8a279b9d5fd4f6238a071e4`
Windows audit run: `35042607692`
Job: `104625496484`
Artifact: `10425691771` (`iter057y-q8-response-fixed-windows`)
Artifact digest: `sha256:1d0019346597fc7d645a493cf23a20075f0a619afa220453387d6cba22fb3a48`

The original supplemental Iter057Y Actions execution produced the already-terminal scientific ranks, compatibility result, Q8 coefficients and reduced/unreduced zero replays, but exited nonzero because its provenance predicate required a `terminal_commit` field that is absent from the historical frozen `data/ITER057V_CANONICAL_Q6_RESPONSE.json` schema.

The canonical Iter057V authority instead contains the exact production head/run/job/artifact/digest, terminal classification, ranks and 88-coefficient Q6 particular solution. The supplemental wrapper changes only that metadata validation predicate; it does not change source coefficients, response coefficients, the affine matrix, right-hand side, solve, or scientific decision rules.

The corrected Windows reproduction completed successfully with all authority subcontrols `S/U/V/X=true` and reproduced:

- matrix shape `1320 x 1650`;
- `rank(M)=rank([M|r])=1096`;
- all 224 compatibility contractions zero;
- 180 nonzero Q8 particular coefficients;
- reduced `DG-source` through degree six exactly zero;
- unreduced `DG-source` through degree six exactly zero;
- the same terminal PASS classification.

Therefore the earlier supplemental Actions failure is classified as a metadata-validation defect, not a scientific discrepancy. Historical failed runs are preserved; the terminal Iter057Y classification is unchanged.
