# Iter057Z independent artifact-only reproduction

Date: 2026-09-16

Gate: `ITER057Z-DODECIC-EINSTEIN-SEED-COMPLETION`

Frozen preregistration: `f1c04bbfdb7848ab79708beb902ccdb315fbd5ed`.

## Independence

This reproduction was completed while `main` recovery still marked Iter057Z as `PROSPECTIVELY_PREREGISTERED__IMPLEMENTATION_NOT_YET_LAUNCHED`. It did not consume an official Iter057Z implementation or payload.

The standalone evaluator reconstructed the canonical zeroth-order seed only from already-terminal coefficient authorities for Iter057O/Q/T/W: 21 R4, 69 R6, 153 R8 and 283 R10 normalized coefficients. All tensor algebra used exact Python `Fraction`; the principal matrix and exact RREF used SymPy `QQ`. No floating rank/zero tolerance was used.

## Exact result

Classification:

`PASS_SCOPED_ITER057Z_DODECIC_EINSTEIN_SEED_COMPLETES_VACUUM_THROUGH_COORDINATE_DEGREE_TEN__HIGHER_SEED_ORDERS_REMAIN_OPEN`

Fresh nonlinear degree-ten Einstein residual before R12:

- 427 nonzero normalized slots;
- all 10 independent symmetric components represented;
- all target terms have the expected `kappa^6` grading;
- canonical source digest: `5411ee1e6e63013502ee83fcaf274e16bfef967ef4fc8389cce5b07de5328731`.

Complete unrestricted degree-twelve complex:

- shape `4316 x 4550`;
- matrix nonzeros `17264`;
- `rank(M)=3436`;
- `rank([M|r])=3436`;
- left nullity `880`;
- nullity `1114`;
- canonical Bianchi count/rank `880/880`;
- `880/880` source compatibility contractions vanish exactly.

Canonical deterministic particular R12:

- 469 nonzero normalized coefficients;
- particular digest `7fef0029470cd15e252d1e9073990c84ddd98a59c0d3b9a8f03bdb29c63fb0f7`;
- every affine row vanishes exactly;
- all 1114 homogeneous directions remain unfixed.

Independent nonlinear replay after inserting R12:

- inverse identity through degree 10: exact;
- Ricci tensor through degree 10: exact zero;
- scalar curvature through degree 10: exact zero;
- Einstein tensor through degree 10: exact zero;
- de Donder through degree 11: exact zero;
- pure degree twelve preserves every lower seed jet through order eleven.

Scientific payload SHA-256 reported by the evaluator:

`16b5bf3f85fc3721fcc7fc097cb42077fe1473bd8a5f3f530476ed5860766378`

The complete result JSON file SHA-256 is:

`4bf91f50a017e1ad83d9c85d231ca116d83f968bdda6dc2c142abfd563fb20b4`

The complete exported R12 coefficient JSON file SHA-256 is:

`f030a326fe19a289c27fb2617665621dc2124434b61b62812867508323fe1c43`

A second clean execution produced byte-identical result and R12 JSON files.

## Scope

This is an independent reproducibility certificate, not an official `main` terminalization. A PASS establishes only the finite local zeroth-order Einstein seed through coordinate degree ten. It does not by itself establish the Weyl3 source degree eight, any higher O(c6) response, convergence, a global solution, a value/sign/running of `c6`, or any physical/quantum completion claim. `c6` remains symbolic/unfixed and theory established remains `0%`.
