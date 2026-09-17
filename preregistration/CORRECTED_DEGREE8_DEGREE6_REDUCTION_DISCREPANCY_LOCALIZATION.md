# Preregistration — corrected degree-eight constructor degree-six reduction discrepancy localization

Date: 2026-09-17

Gate: `CORRECTED_DEGREE8_DEGREE6_REDUCTION_DISCREPANCY_LOCALIZATION`

Parent terminal record: `results/CORRECTED_DEGREE8_WEYL3_SOURCE_RECONSTRUCTION_RUN_35268357568.md`.

## Frozen question

Why do two independent generalized corrected Frechet constructors, when extended through degree eight, agree on degree-six SHA256 `2f15c55c0b326966c821141e43e245e3715f93fc9f4b9ee720179f31b1e28b6d` rather than the authoritative Iter057AT ordered 840-vector SHA256 `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`?

This is a localization gate, not a repair gate.

## Frozen authorities

- Iter057AT ordered 840-vector SHA256: `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b`.
- Durable AT source file SHA256: `1cae5a82d1345b9d9a77bcd3d6a91f6d5747629b5ac9e091bbb6c5a7ade3025b`.
- `c6 = SYMBOLIC_UNFIXED`.
- Corrected-Y convention `MAP_MINUS` is not changed by this diagnostic.

## Prospective diagnostic decomposition

Before loading the AT coefficient target, each diagnostic lane must independently serialize and freeze the generalized constructor's degree-six projection and a decomposition of its Euler-source pieces at degree six:

1. algebraic `P·R` / curvature-contraction contribution;
2. double-covariant-divergence contribution;
3. metric-times-I3 contribution;
4. index-lowering contribution from the contravariant Euler object;
5. the final assembled standard `Edown` degree-six vector.

Each lane must record exact rational coefficients, ordered-slot SHA256 values, nonzero counts, and all intrinsic P/seed controls. No tolerance is permitted.

Only after those diagnostic payloads and hashes are frozen may the lane load the durable Iter057AT 840-vector and compute exact slotwise differences.

## Frozen localization outputs

The terminal classifier may report only one of:

- `LOCALIZED_SINGLE_OPERATOR_COMPONENT` if all AT disagreement is exactly attributable to one prospectively named decomposition component while the remaining components agree under an independently reconstructed AT-side decomposition;
- `LOCALIZED_TRUNCATION_ORDER_COUPLING` if exact recomputation at multiple sufficient truncation orders shows the degree-six projection changes with the higher-order truncation boundary and converges exactly to AT under the mathematically sufficient boundary;
- `LOCALIZED_SERIALIZATION_OR_BASIS_MISMATCH` if the underlying exact polynomial tensors agree but ordered serialization differs for a prospectively identified basis/order convention;
- `LOCALIZED_GENERALIZED_CONSTRUCTOR_FORMULA_MISMATCH` if the tensor/polynomial discrepancy is already present before serialization and is not a truncation-boundary effect;
- `UNRESOLVED_DEGREE6_REDUCTION_DISCREPANCY` otherwise.

No outcome authorizes changing Iter057AT, sign fitting, scale fitting, normalization fitting, or post-hoc threshold changes.

## Independence requirement

Use two independently implemented diagnostic paths. One may instrument the current primary assembly; the second must instrument the AO-style independent assembly. They must not read each other's diagnostic payloads before terminal aggregation.

## Prohibitions

- Do not run corrected Q10.
- Do not classify historical Iter057AA survival/difference.
- Do not start another symmetry reduction.
- Do not change scientific witnesses/targets/thresholds.
- Do not set beta=1 or fix c6.
- Do not infer global covariance, unitarity, UV completion, experimental confirmation, or theory correctness.

A terminal localization result is diagnostic evidence only. Theory established remains 0%.
