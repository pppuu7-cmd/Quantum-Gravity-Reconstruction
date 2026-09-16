# Iter057AA terminal result — corrected dodecic-seed Weyl3 eighth source jet

Date: 2026-09-16
Gate: `ITER057AA-CORRECTED-DODECIC-SEED-WEYL3-EIGHTH-SOURCE-JET`
Preregistration: `84a6a3f060b28bace577ea76eadc0aed2c429014`
Exact implementation: `29e6fb029f2d468b81e8d7b4e6dbe18d22baedd4`
Frozen pre-production payload digest: `c0ca2735df70d1c35397ecd13496b04ebc5b62b3`
Canonical degree-eight source: `1c9235cd89deafab5c2d6c2daea794e0a1d2f5dd`
Parent background: Iter057Z terminal `bb4fa6ccbf21e2a063467a1b0839223744866995`
Parent lower source: Iter057X terminal `4ab5592cfc6ef5fb69d3a96fa4433ef22d51af8b`

## Terminal classification

**`PASS_SCOPED_ITER057AA_CORRECTED_DODECIC_EINSTEIN_SEED_WEYL3_SOURCE_EXACT_THROUGH_EIGHTH_EVEN_ORDER__O_C6_Q10_RESPONSE_GATE_CAN_NOW_BE_PREREGISTERED`**

This is exactly the prospectively frozen maximum scoped PASS.

## Exact reproducibility

The frozen problem was executed twice as separate exact sparse-rational processes after the optimized four-step index-raising contraction was introduced. The optimization is algebraically identical to direct four-index raising and changes only contraction order. Both executions produced an identical full JSON object and an identical ordered source coefficient list.

The frozen scientific payload is canonical sorted compact JSON of exactly **50,963 UTF-8 bytes** with

`sha256:908baddad1138611869582c08d6d4069d591b7e840d606bb397a34bec57719c7`.

The complete repo-native result JSON is 109,576 UTF-8 bytes with

`sha256:989999ab44c37ccb5212ac34202bee669228ed3cd1a703ad95cb277a89f4ea24`.

Prospective supplemental GitHub Actions reproductions were launched after the payload and coefficient authority were frozen: Windows run `35043996274` and Ubuntu run `35044007266`. At terminalization both were still queued and therefore were not used to select, tune, or reinterpret the PASS classification.

## Background replay

The canonical even seed

`eta + G2 + R4 + R6 + R8 + R10 + R12`

is reconstructed from frozen authorities. Before source extraction, exact controls give:

- inverse identity through coordinate degree ten: pass;
- Ricci tensor through degree ten: exact zero;
- scalar curvature through degree ten: exact zero;
- Einstein tensor through degree ten: exact zero;
- canonical Iter057Z R12 provenance and all 469 R12 coefficients: exact.

No lower seed coefficient is mutated or refit.

## Weyl-cubic Euler controls

The Weyl/Riemann cubic construction is recomputed directly from the full dodecic seed through the required orders. Every preregistered exact identity passes:

- `P.R = 3 I3` through coordinate degree eight;
- lower-index Euler tensor symmetry through degree eight;
- four-dimensional trace Ward identity `g^{ab}E_W3,ab = -I3` through degree eight;
- covariant Noether divergence through coordinate degree seven;
- odd source degrees 1, 3, 5 and 7 vanish exactly;
- `I3(0)/kappa^3 = 96`.

The source is computed directly; no degree-eight coefficient is inferred from Ward/Noether identities or extrapolated from lower orders.

## Lower-source replay

Every authoritative canonical source coefficient at degrees 0, 2, 4 and 6 from Iter057U/Iter057X is replayed coefficient-by-coefficient.

Lower replay mismatch count: **0**.

Thus the new metric twelve-jet changes only the newly source-owned layer and does not disturb any established lower source coefficient.

## New exact degree-eight source

The complete symmetric-tensor degree-eight basis contains

`10*C(11,3)=1650`

possible normalized slots. The exact source is sparse:

- degree 8 nonzero coefficients: **260**;
- degree 8 time-containing nonzero coefficients: **170**;
- degree 8 off-diagonal nonzero coefficients: **120**.

The complete source counts through degree eight are

`degree 0: 4`,
`degree 1: 0`,
`degree 2: 22`,
`degree 3: 0`,
`degree 4: 64`,
`degree 5: 0`,
`degree 6: 140`,
`degree 7: 0`,
`degree 8: 260`.

All 260 nonzero normalized degree-eight coefficients, including both `Shat/kappa^7` and their exact value at the frozen kappa used by the local construction, are frozen in `data/ITER057AA_CANONICAL_SOURCE_DEGREE8.csv`.

No floating-point zero test, tolerance, numerical fitting, restricted source ansatz, seed mutation or historical degree-eight source substitution is used.

## Consequence

The corrected Weyl3 source is now source-owned through coordinate degree eight on the canonical dodecic Einstein seed. The next admissible gate is therefore an unrestricted pure degree-ten trace-reversed first-order `O(c6)` response `Q10`, extending the fixed Iter057Y `Q2+Q4+Q6+Q8` response against the canonical source through degree eight.

Its affine consistency is not implied by this source PASS and must be tested with the complete degree-ten response space, fresh curved-background degree-nine gauge residual, fresh degree-eight field residual, the complete exact 480-dimensional Bianchi compatibility family, and independent reduced/unreduced replay.

## Scope ceiling

This PASS establishes only one additional finite local source Taylor layer on one canonical finite-order Einstein seed. It does not establish an all-orders or convergent Einstein+Weyl3 solution, an open-neighborhood/global/asymptotic solution, a value/sign/running of `c6`, `beta=1`, physical characteristics, strong hyperbolicity, ghosts/stability, quantum unitarity, regulator removal, a global interacting measure, UV completion, experimental confirmation, new physics, or QGR correctness.

`c6` remains symbolic/unfixed and theory established remains `0%`.
