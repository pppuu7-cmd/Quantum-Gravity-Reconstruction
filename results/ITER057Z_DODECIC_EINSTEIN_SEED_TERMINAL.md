# Iter057Z terminal result — unrestricted dodecic Einstein seed completion

Date: 2026-09-16
Gate: `ITER057Z-DODECIC-EINSTEIN-SEED-COMPLETION`
Preregistration: `f1c04bbfdb7848ab79708beb902ccdb315fbd5ed`
Exact implementation: `a7f8198bdb41c5667ea47b2689731e238307fc94`
Artifact-output-only fix: `b259568db5c37154043cb1b913393b82f93b2765`
Frozen pre-production scientific payload: `8ccccdea0954e70b0337d2db39470699e7342957`
Canonical R12 coefficients: `5bfe62e887dd627c76c41080187eadc3d95e0c45`
Windows production head: `60ac2237697030b0bca58e52483f4ccef703161e`
Actions run: `35042867768`
Job: `104626289820`
Artifact: `10426246424` (`iter057z-dodecic-einstein-seed-windows`)
Artifact digest: `sha256:1941ca647e20d428cb4feb2d891bca8b9ab89e23b39596c531d49d03f752bbc7`

## Terminal classification

**`PASS_SCOPED_ITER057Z_DODECIC_EINSTEIN_SEED_COMPLETES_VACUUM_THROUGH_COORDINATE_DEGREE_TEN__HIGHER_SEED_ORDERS_REMAIN_OPEN`**

This is exactly the prospectively frozen maximum scoped PASS.

## Reproducibility and evidence chain

Before production evidence was available, the frozen problem was evaluated twice with exact sparse rational polynomial arithmetic: once in an independent artifact-based implementation and once in the repository-native canonical-authority implementation. The complete ordered R12 particular solution and all structural/nonlinear controls agreed exactly.

The scientific payload was frozen before successful production evidence as canonical sorted compact JSON of exactly **45,661 UTF-8 bytes** with

`sha256:e62c84d0ad586322d588093ddbf067c0ad185478a042e3c877d24e7809122c6b`.

The successful Windows Actions artifact reproduces that exact 45,661-byte scientific payload hash. Its complete ordered 469-coefficient R12 list and all controls are identical to the pre-production result.

The first Windows run `35042590865` completed the mathematical `compute()` and then failed only when attempting to write `artifacts/iter057z.json` because the parent directory had not been created. Commit `b259568d...` adds only parent-directory creation before output and does not alter any scientific computation, coefficient, matrix, or decision rule. The corrected production run `35042867768` then completed successfully and uploaded raw evidence.

## Fixed seed and fresh nonlinear residual

The computation reconstructs the canonical zeroth-order seed

`eta + G2 + R4 + R6 + R8 + R10`

from frozen coefficient authorities. The already established vacuum equations through coordinate degree eight replay exactly, and the inverse identity through the required order is exact.

The directly recomputed coordinate-degree-ten Einstein residual of the fixed R10 seed is nontrivial: all **10 independent symmetric tensor components** contain nonzero degree-ten coefficients before R12 is added. Thus the new solve is not a vacuous extension and no inferred or historical right-hand side is substituted for the nonlinear residual.

## Exact unrestricted degree-twelve complex

The frozen pure degree-twelve trace-reversed correction contains

`10*C(15,3)=4550`

unknown normalized coefficients. The exact affine complex contains

- 1456 degree-eleven de Donder rows;
- 2860 degree-ten Einstein rows;
- 4316 rows total;
- 17,264 nonzero principal-matrix entries.

Exact arithmetic gives

`shape(M)=(4316,4550)`,

`rank(M)=3436`,

`rank([M|r])=3436`,

`left-nullity(M)=880`,

`nullity(M)=1114`.

The complete canonical Bianchi family has exact rank **880**, annihilates the principal matrix exactly, and all **880/880** affine compatibility contractions with the actual nonlinear residual vanish exactly.

## Exact R12 particular solution and nonlinear replay

Setting the 1114 homogeneous directions to zero only to select a deterministic particular representative gives **469 nonzero normalized R12 coefficients**. The complete ordered coefficient authority is frozen in `data/ITER057Z_CANONICAL_R12_NORMALIZED.csv`. The 1114 homogeneous directions remain mathematically unfixed.

Every affine row vanishes exactly after the R12 correction is inserted. The correction is pure coordinate degree twelve, so every already fixed seed coefficient/derivative through order eleven is preserved.

Independent reconstruction of the corrected full metric gives:

- inverse identity through coordinate degree ten: exact;
- flat de Donder through degree eleven: exact zero;
- Ricci tensor through coordinate degree ten: exact zero;
- scalar curvature through coordinate degree ten: exact zero;
- Einstein tensor through coordinate degree ten: exact zero.

No floating-point rank, tolerance, finite difference, restricted ansatz, or lower-seed mutation is used.

## Consequence

The canonical local zeroth-order Einstein seed is now explicitly completed through a metric twelve-jet / Einstein coordinate degree ten. This supplies the previously missing background information needed before the corrected Weyl-cubic Euler source can be treated authoritatively at coordinate degree eight.

The next scientifically admissible gate is therefore a prospectively frozen corrected-dodecic-seed Weyl3 source reconstruction through coordinate degree eight. It must consume the canonical R12 authority above and replay all lower source coefficients before the degree-eight source is accepted.

## Scope ceiling

This PASS establishes only one additional finite local zeroth-order Einstein seed layer. It does not establish the next Weyl3 source layer by itself, the next `O(c6)` response, an all-orders or convergent solution, an open-neighborhood/global/asymptotic solution, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghosts/stability, quantum unitarity, regulator removal, a global interacting measure, UV completion, experimental confirmation, new physics, or QGR correctness.

`c6` remains symbolic/unfixed and theory established remains `0%`.
