# Iter057W terminal result — unrestricted decic Einstein-seed completion

Date: 2026-09-16
Gate: `ITER057W-DECIC-EINSTEIN-SEED-COMPLETION`
Preregistration: `7e6336d195985b2059966eda64859da86c9e9d15`
Implementation architecture: `cb2709b79ab1365c39c8cc20e5c3455aad241e0e`
Primary exact implementation: `365fbfc6594e8ac844529409addb06a80544d755`
Independent sparse-Fraction implementation: `ad14ccd72a1a3ca75ab95acb0e294c6707b14627`
Structural audit: `7f924e55e66fb56dabdb94d4d7df929f5e35049c`
Frozen diagnostic payload digest: `e2f774482f1f888575281d5641526159f33bd23b`
Canonical R10 data: `e8982c84cc3b4baa0ca40ed8ff7876164b728880`

## Terminal classification

**`PASS_SCOPED_ITER057W_DECIC_EINSTEIN_SEED_COMPLETES_VACUUM_THROUGH_COORDINATE_DEGREE_EIGHT__HIGHER_SEED_ORDERS_REMAIN_OPEN`**

This is exactly the prospectively frozen maximum scoped PASS.

## Production evidence

Two independent GitHub Actions production environments reproduced the complete exact scientific payload:

- Ubuntu sparse-Fraction run `35034092694`, job `104599070221`, artifact `10423276358`, artifact digest `sha256:37473c79152559aafa58ddce3026c696e2ce064d8940fa31d9184b6c9fad947f`;
- Windows sparse-Fraction run `35034524501`, job `104600467919`, artifact `10423176041`, artifact digest `sha256:7ac4dc88f8e6d25954e2efe34adee271e9cb1958f2d4e875d41e1974d1a49c29`.

The two raw JSON objects are exactly equal. Their preregistered scientific sub-payload is 18,252 UTF-8 bytes and reproduces the pre-production frozen digest exactly:

`sha256:359b27d478b5b4927bc7df0c98a361f0177bba57e5550433662cd21138f75571`.

The older full-SymPy production run `35033341661` remains a non-authoritative heavy diagnostic lane and is not needed for this terminal classification.

## Exact unrestricted decic system

The pure degree-ten trace-reversed correction contains

`10*C(13,3)=2860`

normalized coefficients. The frozen homogeneous polynomial complex contains

- 880 degree-nine de Donder rows;
- 1650 degree-eight Einstein rows;
- 2530 rows total.

Exact production gives

`shape(M)=(2530,2860)`,

`nnz(M)=10120`,

`rank(M)=2050`,

`rank([M|r])=2050`,

`left-nullity(M)=480`,

`nullity(M)=810`.

All 480 canonical Bianchi compatibility vectors annihilate the principal matrix exactly, and all 480 affine contractions with the actual degree-eight residual vanish exactly. No numerical rank tolerance is used.

## Nonlinear degree-eight residual and exact correction

Before adding the decic layer, the canonical Iter057T seed has a directly computed nonzero homogeneous coordinate-degree-eight Einstein residual in all 10 independent tensor components. Thus the decic correction is genuinely required.

With all 810 homogeneous directions retained as unfixed freedom and set to zero only for the deterministic canonical particular solution, the exact affine solve gives one unrestricted pure degree-ten correction with **283 nonzero normalized coefficients**. The complete production-owned coefficient list is frozen in `data/ITER057W_CANONICAL_R10_NORMALIZED.csv`.

The exact affine residual vanishes in all 2530 rows, and the combined trace-reversed perturbation satisfies de Donder gauge through degree nine exactly.

## Independent unreduced nonlinear replay

The sparse-Fraction evaluator independently reconstructs the canonical quartic, sextic and octic seed layers, adds the solved metric decic correction, and recomputes the inverse metric, Levi-Civita connection, Ricci tensor, scalar curvature and Einstein tensor through coordinate degree eight.

Every frozen replay control is exact:

- lower Einstein degrees 0, 2, 4 and 6 remain zero;
- inverse identities hold through degree eight before and after the new correction;
- the directly computed degree-eight contracted Bianchi control vanishes;
- `Ric_ab=0` through degree eight;
- `R=0` through degree eight;
- `G_ab=0` through degree eight in all 10 independent components;
- the decic correction is pure degree ten and therefore preserves every canonical seed derivative through order nine.

All preregistered obligations A-I are true.

## Consequence

The canonical zeroth-order Einstein seed is now source-owned through the metric ten-jet / Einstein coordinate degree eight. This is precisely the background information needed before a corrected-seed Weyl3 Euler source coefficient through coordinate degree six can be claimed as source-owned.

The next scientifically admissible local-series gate is therefore a prospective exact reconstruction of the corrected-decic-seed Weyl3 Euler source through coordinate degree six, with lower Iter057U source degrees 0/2/4 replayed exactly and full Ward/Noether/parity controls.

## Scope ceiling

This PASS is only a finite local Taylor certificate. It does not establish an all-orders or convergent Einstein seed, an open-neighborhood/global/asymptotic solution, the Weyl3 degree-six source by itself, a higher `O(c6)` response layer, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghost/stability statements, quantum unitarity, regulator removal, a global interacting measure, UV completion, experiment, new physics, or QGR correctness.

`c6` remains symbolic/unfixed and theory established remains `0%`.
