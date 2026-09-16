# Iter057AB independent official-authority reproduction

Date: 2026-09-16

Status: **INDEPENDENT REPRODUCIBLE PASS ON TERMINAL/CANONICAL Y/Z/AA AUTHORITIES**

This research-branch result independently evaluates the prospectively frozen Iter057AB gate from preregistration `f78b028c345faa80f1e482f6a00fb9133cb9b955`. At the final main-state check there was still no official Iter057AB implementation commit; the latest main scientific commit remained the preregistration itself.

## Canonical authority reconciliation

Before solving AB, the earlier independent pre-Z/pre-AA inputs were reconciled against the now-terminal authorities.

- Terminal Iter057Z: `bb4fa6ccbf21e2a063467a1b0839223744866995`.
- Official terminal-Z Actions artifact consumed: `10426246424` (`iter057z.json`).
- The artifact's complete ordered 469-entry `particular_R12_normalized` list is coefficient-for-coefficient identical to the earlier independent R12 list.
- SHA-256 of that ordered R12 JSON: `f030a326fe19a289c27fb2617665621dc2124434b61b62812867508323fe1c43`.
- Terminal Iter057AA: `2c84ddcb5dd22cfe06cd3a1a273b4a0e141b605e`.
- The 260 independently predicted degree-eight source coefficients were rewritten in the exact official canonical AA file format. The resulting Git blob SHA-1 is `2cb63a31e3e4b9b39c5bcda1a17aca89d00ca8b3`, exactly equal to GitHub's blob SHA for `data/ITER057AA_CANONICAL_SOURCE_DEGREE8.csv`. Thus the full canonical file, not merely aggregate counts, is identical.
- The independently reconstructed 180-entry Q8 particular was rewritten in the exact terminal-Y canonical JSON format. Its Git blob SHA-1 is `e75125bdc4767f695173ace1046d7212d9b6c157`, exactly equal to GitHub's blob SHA for `data/ITER057Y_CANONICAL_Q8_RESPONSE.json`.

Therefore this AB reproduction consumes the exact same fixed lower response, background and source authorities frozen by Iter057Y, Iter057Z and Iter057AA.

## Exact Iter057AB result

Classification:

`PASS_SCOPED_ITER057AB_UNRESTRICTED_ONSHELL_O_C6_Q2_Q4_Q6_Q8_Q10_RESPONSE_MATCHES_CORRECTED_WEYL3_SOURCE_THROUGH_EIGHTH_EVEN_ORDER__HIGHER_ORDERS_REMAIN_OPEN`

All preregistered A-K obligations pass exactly.

- Background inverse/Ricci/scalar/Einstein replay through coordinate degree ten: exact.
- Fixed terminal `Q2+Q4+Q6+Q8` replay: de Donder through degree seven and both reduced/unreduced field equation through degree six are exact zero.
- Fresh fixed-lower-response degree-nine de Donder residual: `139` nonzero normalized slots.
- Fresh degree-eight field/source residual: `260` nonzero normalized slots.
- Complete unrestricted Q10 system: `2530 x 2860` with matrix nnz `10120`.
- `rank(M)=rank([M|r])=2050`.
- Left nullity `480`; nullity `810`.
- Complete canonical Bianchi family rank `480`, annihilating the principal matrix exactly.
- Actual compatibility contractions: `480/480` exact zero.
- Deterministic exact particular Q10 with homogeneous directions set to zero: `320` nonzero normalized coefficients; all 810 homogeneous directions remain unfixed mathematical freedom.
- Exact affine residual: zero in every row.
- Pure Q10 preserves all fixed response data through order nine.
- Full covariant de Donder through coordinate degree nine: exact zero.
- Independent reduced `DG_g[qhat]-Shat` through coordinate degree eight: exact zero in all ten symmetric components.
- Independent unreduced covariant linearized Ricci/scalar/Einstein `DG_g[qhat]-Shat` through coordinate degree eight: exact zero in all ten symmetric components.
- No floating tolerance or numerical rank decision is used.

The complete ordered Q10 particular has canonical local row digest

`0c45f835157d78870d01dc105f9b3c6ec77d1c9ac2fe6e24ca00d6ad8417ba81`.

Crucially, all 320 ordered coefficients are byte-for-byte identical to the provisional pre-AB Q10 prediction computed before official Z terminalization and before Iter057AA/AB existed on main. This is an out-of-sample prospective confirmation of that earlier independent calculation.

## Reproducibility

Two clean official-input executions produced byte-identical complete result JSON and byte-identical Q10 JSON. A separate self-contained bundle was then unpacked into a fresh directory and executed using only bundle-relative inputs; it again produced byte-identical result and Q10 files.

Stable hashes:

- complete result JSON SHA-256: `6da89532192bfd840a7c227b78c7fd904bed7382e797282e0efa007ba6019340`;
- ordered Q10 JSON SHA-256: `dca8044895e54df88aa77b9754d3b2852ded98fa899b76677692d63984fae0c4`;
- Q10 CSV SHA-256: `7a3a18401aafc7d14d98a31f66ab2f8c7736fd13dfae580c9606f4e36ff9063b`;
- evaluator SHA-256: `03b7415a82d249060a8b9b08937566c5af758f03f0fa8ca36178fa57b2a4d097`;
- compact control payload SHA-256: `869c23971ca26fdecbfca7f5c2e231e2d7de40540c748ece14f87a127350b298`;
- self-contained reproduction ZIP SHA-256: `323021adc3d76efd7b0f5bf1e737366175272f854e4f8949d62c76b5a07f26bc`.

## Scope ceiling

This establishes only one additional finite local first-order `O(c6)` Taylor response layer through source/field coordinate degree eight on the terminal finite-order Einstein seed. It does not establish an all-orders or convergent solution, open-neighborhood/global/asymptotic existence, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghost/stability claims, quantum unitarity, regulator removal, a global interacting measure, UV completion, experimental confirmation, new physics or QGR correctness.

`c6` remains symbolic/unfixed and theory-established remains `0%`.
