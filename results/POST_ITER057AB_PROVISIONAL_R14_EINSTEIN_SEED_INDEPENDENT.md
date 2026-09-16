# Post-Iter057AB provisional R14 Einstein-seed completion — independent exact reproduction

Date: 2026-09-16

Status: **INDEPENDENT REPRODUCIBLE PROVISIONAL PASS — NOT CANONICAL UNTIL AN OFFICIAL POST-AB SEED GATE IS PREREGISTERED/TERMINALIZED**

Main state at branch point: `d74a8849cb36fded69c7e4fc3169b5185be27e61`. At that point Iter057AB had an implementation, a frozen pre-production payload, and launched Windows/Ubuntu reproductions, but no terminal Iter057AB commit and no official next seed preregistration.

The frozen official Iter057AB payload (`9caf398f0a9af15c14715f290d78261ec2242f0d`) matches the prior independent AB result in all reported structural and source-specific invariants: matrix `2530x2860`, nnz `10120`, rank/augmented rank `2050`, Bianchi/left-nullity `480`, nullity `810`, compatibility zero, fresh residual counts `139/260`, Q10 particular count `320`, and both reduced/unreduced final residuals zero.

## Independent question

On the terminal canonical Einstein seed

`eta + G2 + R4 + R6 + R8 + R10 + R12`,

compute the fresh nonlinear Einstein residual at coordinate degree twelve and test whether a completely unrestricted pure coordinate-degree-fourteen trace-reversed correction `R14` exists such that flat de Donder gauge vanishes through degree thirteen and the exact nonlinear vacuum Einstein tensor vanishes through coordinate degree twelve.

This is deliberately not assigned an official iteration name.

## Frozen correction space and principal complex

The pure degree-14 symmetric trace-reversed correction has

- degree-14 monomials per symmetric component: `C(17,3)=680`;
- unknowns: `10*680=6800`;
- degree-13 de Donder rows: `4*C(16,3)=2240`;
- degree-12 Einstein rows: `10*C(15,3)=4550`;
- total affine system: `6790 x 6800`;
- matrix nnz: `27160`.

The source-independent exact complex predicts and the computation verifies

- rank `5334`;
- left-nullity/Bianchi rank `1456`;
- nullity `1466`.

## Fresh nonlinear residual

The fixed canonical seed through R12 replays exactly before the new solve:

- inverse identity through degree 10: exact;
- Ricci/scalar/Einstein through degree 10: exact zero;
- de Donder through degree 11: exact zero.

The directly recomputed degree-12 Einstein residual is nontrivial:

- **665** nonzero normalized slots;
- all **10** independent symmetric components represented;
- all target coefficients have the expected `kappa^7` grading;
- ordered residual digest: `8416a8800206a151e8c50a3c3de7b8f2c0363f92434ad64bc6ca3294062f5296`.

No historical or inferred right-hand side is substituted.

## Exact unrestricted R14 solve

For the actual fresh residual:

- `rank(M)=5334`;
- `rank([M|r])=5334`;
- left-nullity `1456`;
- nullity `1466`;
- complete canonical Bianchi family count/rank `1456/1456`;
- Bianchi family annihilates the principal matrix exactly;
- all `1456/1456` compatibility contractions with the actual residual vanish exactly.

Setting the 1466 homogeneous directions to zero only to choose a deterministic particular representative gives **721 nonzero normalized R14 coefficients**. All 1466 homogeneous directions remain unfixed mathematical freedom.

The deterministic particular row digest is

`e24d13bc2110d842e48ac475511b7ca1a33fb445cf5a5598ccedd08921864192`.

Every affine row vanishes exactly.

## Full nonlinear replay

After inserting only the pure degree-14 correction:

- inverse identity through coordinate degree 12: exact;
- Ricci tensor through coordinate degree 12: exact zero;
- scalar curvature through coordinate degree 12: exact zero;
- Einstein tensor through coordinate degree 12: exact zero;
- flat de Donder through coordinate degree 13: exact zero;
- all previously fixed seed data through degree 13 are preserved.

Research classification:

`REPRODUCIBLE_PROVISIONAL_PASS_POST_ITER057AB_UNRESTRICTED_R14_EINSTEIN_SEED_COMPLETES_VACUUM_THROUGH_COORDINATE_DEGREE_TWELVE__NOT_CANONICAL_UNTIL_OFFICIAL_GATE`

## Reproducibility

Two clean executions produced byte-identical complete result JSON and byte-identical ordered R14 coefficient JSON. A self-contained bundle was then unpacked in a fresh directory and rerun using only bundle-relative inputs; it reproduced both files byte-for-byte.

Stable hashes:

- complete result JSON SHA-256: `f045c7426ae758b279d1513ba62b0dbbbf6a7c2524fc7badf882a2cd18fdca08`;
- ordered R14 JSON SHA-256: `71e104d95dd266bd4b466e582d5dad149b65910849642c23e7de8afd95e0659b`;
- R14 CSV SHA-256: `fb3a173cd375481ef504ce57de67908abc0a8ac9336445942ea8e0c29506365e`;
- evaluator SHA-256: `f699d3ac7f6de34b5b760f5ad316ce7e363eb65c037e16fb8d6ac686735e1ffc`;
- self-contained reproduction ZIP SHA-256: `9025b90d53c4ceb91f07d0a91e57c34f188e54be2a6a16c34b81494f650560d7`;
- scientific payload SHA-256: `663230d89b15f792c3a9b91864d6e483ec6b9d034eeca7ad9466a4605bcf3dc7`.

## Promotion lock

This result must remain provisional until the official research front terminalizes Iter057AB and prospectively preregisters the next seed gate. If that official gate uses the same canonical lower seed and unrestricted pure degree-14 correction space, the first operation should be coefficient-for-coefficient comparison with this R14 prediction rather than assuming promotion.

## Scope ceiling

This establishes only one further finite local zeroth-order Einstein Taylor layer through coordinate degree 12, conditional on the current terminal lower seed authorities. It does not establish the next Weyl3 source layer, the next first-order response, all-orders convergence, open-neighborhood/global/asymptotic existence, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghost/stability claims, quantum unitarity, regulator removal, a global interacting measure, UV completion, experimental confirmation, new physics, or QGR correctness.

`c6` remains symbolic/unfixed and theory-established remains `0%`.
