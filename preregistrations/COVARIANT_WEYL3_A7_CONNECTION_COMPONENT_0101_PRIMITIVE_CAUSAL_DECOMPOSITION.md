# Preregistration — COVARIANT_WEYL3_A7_CONNECTION_COMPONENT_0101_PRIMITIVE_CAUSAL_DECOMPOSITION

Date: 2026-09-19

## Frozen parent evidence

Parent terminal gate: `COVARIANT_WEYL3_A7_CONNECTION_TENSOR_COMPONENT_LOCALIZATION`, run `35407870461`, terminal payload `5dbf6ec1ed1fa41f42c1e8187432090bb6571595ecb2c655611ba77f38a6ff16`.

Frozen witness remains `OFFSHELL_A / d=7 / (i,j)=(0,0)`. Frozen first divergent connection-tensor component is `(a,b,c,d)=(0,1,0,1)`.

Parent tensor relations are frozen: A is the exact negative of B as a complete 256-component tensor; neutral C equals neither sign. These facts are evidence to explain, not targets to fit.

## Question

At component `(0,1,0,1)`, which primitive algebraic/contraction contribution is the first exact point at which the three independently frozen constructions cease to represent the same tensor object?

## Prospective method

Each lane must emit a target-blind ordered ledger before cross-lane comparison. The ledger must expose primitive terms before summation, including all nonzero contributions from:

1. metric and inverse-metric contractions used to place indices;
2. Christoffel/connection factors and their ordered index placements;
3. Hessian / second-metric-derivative contributions where present;
4. Gamma-Gamma product contributions with each dummy-index channel serialized separately;
5. neutral dual-polynomial coefficient channels contributing to `[eps*x]` for this component;
6. permutation/antisymmetrization factors, with signs recorded from the generating expression rather than inferred from another lane.

The comparator must canonicalize only exact rational arithmetic and dummy-index naming. It must not multiply a lane by -1, permute free indices, change Riemann/Weyl conventions, alter orientation, or refit a normalization.

## Frozen comparison order

Compare in this order:

`FREE_INDEX_PLACEMENT` -> `METRIC_INVERSE_METRIC_CONTRACTIONS` -> `CONNECTION_FACTOR_CHANNELS` -> `HESSIAN_CHANNELS` -> `GAMMAGAMMA_DUMMY_CHANNELS` -> `DUAL_POLYNOMIAL_CHANNELS` -> `PERMUTATION_ANTISYMMETRY_FACTORS` -> `FINAL_COMPONENT_SUM`.

The terminal must record the first class and first lexicographic primitive channel where exact equality fails, plus exact pairwise values and relations.

## Controls

- Exact rational arithmetic only; no tolerance.
- Frozen component `(0,1,0,1)` only for causal decomposition; no search for a more favorable component.
- Each lane serializes its ledger before comparator access.
- Parent scalar controls and full-tensor hashes from run `35407870461` must reproduce exactly.
- `c6=SYMBOLIC_UNFIXED` and corrected Q10 locked.
- No parent formula edit or sign/convention repair in this gate.

## Terminal classifications

- `COMPONENT_0101_PRIMITIVE_DIVERGENCE_LOCALIZED`
- `COMPONENT_0101_PRIMITIVE_LEDGER_ALL_THREE_MATCH_BUT_SUM_DIVERGES`
- `BLOCKED_EXECUTION_OR_PROVENANCE`

The second classification is a fail-closed diagnostic indicating serialization/comparator inconsistency; it does not authorize criterion changes.

## Claim locks

This finite exact causal audit is not a complete 4D covariant Weyl^3 Euler-Lagrange certificate and is not a global theorem. `theory_established=0%`; no experimental confirmation; beta matching/calibration and beta=1 are unauthorized; c6 remains unfixed; G45 does not prove absolute energy positivity or quantum unitarity; G35-G37 distant roots do not authorize physical weights; KMQGB `NEW_REQUIRED` is not authorized; no new-physics claim is authorized.
