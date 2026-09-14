# Iter054P Preregistration — Interacting-Measure Regulator/Refinement Removal Audit

Date: 2026-09-14
Gate: `ITER054P-INTERACTING-MEASURE-REGULATOR-REFINEMENT-REMOVAL`
Parent state: Iter054O category-E scoped PASS; Iter054M category-C regulator removal incomplete; category-D `c6` identity missing.

## Objective

Test whether already-authorized normalized coherent-history amplitudes support a controlled **relative** interacting regulator/refinement-removal object. The gate is deliberately narrower than a construction of a global infinite-dimensional path-integral measure.

## Frozen finite-regulator object

For equal-primitive-count history pairs define the normalized finite-refinement log-ratio data

`R_m = log(K_a^(m)/K_b^(m))`

only through its already-authorized relative phase/coefficient representation, so any common nonzero normalization and the common source-calibration contribution `beta*n` cancel. `c6` remains symbolic on the IR side.

The refinement parameter is frozen as `epsilon_m = 2^(-m)`, with `m = 1,...,8` for the positive panel.

## Frozen convergence family

Three positive witnesses are fixed prospectively at coefficient level:

- `P0`: `R_m = R_inf + (3/5) epsilon_m`;
- `P1`: `R_m = R_inf - (7/6) epsilon_m^2`;
- `P2`: IR symbolic pair with `GR_m = GR_inf + (2/3) epsilon_m` and `W3_m = W3_inf - (5/4) epsilon_m`, keeping the full limit `GR_inf + c6*W3_inf` symbolic.

These are not claimed as uniquely physical sequences; they are a controlled existence/compatibility panel for the already-defined relative observable class.

## Frozen acceptance criteria

All must pass:

1. `FINITE_OBJECT_DEFINED`: finite-regulator normalized relative object is explicit on microscopic and symbolic-`c6` IR sides;
2. `COMMON_SCALE_CANCELLED`: arbitrary common normalization and equal-count `beta*n` direction cancel exactly;
3. `CAUCHY_POSITIVE_PANEL`: each positive witness satisfies exact monotone Cauchy contraction under refinement, with final increment no larger than `1/128` times the corresponding first-step linear scale (or the exact stronger bound implied by its power);
4. `LIMIT_IDENTIFIED`: exact finite `R_inf` / `(GR_inf,W3_inf)` coefficient limit exists for the frozen witnesses;
5. `CYLINDRICAL_COMPATIBILITY`: parent correction equals the sum of two prospectively frozen child corrections at each tested dyadic split;
6. `NEGATIVE_CONTROLS_REJECTED`: at least one oscillatory nonconvergent sequence and one constant-mismatch refinement sequence fail the positive criterion;
7. `BLOCKED_GLOBAL_ROUTE_REJECTED`: the globally normalized oscillatory partition route blocked by Iter009 is not used or promoted;
8. `NO_PARAMETER_FIXING`: `beta=1` is not set and `c6` remains symbolic/unfixed.

## Frozen negative controls

- `N0`: `R_m = (-1)^m`, which must fail Cauchy contraction;
- `N1`: parent correction `1` split into children `1/3 + 1/3`, which must fail cylindrical compatibility;
- global oscillatory partition normalization remains authority-rejected.

## Terminal classifications

- `PASS_SCOPED_ITER054P_RELATIVE_INTERACTING_REGULATOR_REMOVAL_OBJECT_DEFINED__GLOBAL_MEASURE_NOT_AUTHORIZED` only if all eight requirements pass.
- `BLOCKED_OBJECT_DEFINITION_ITER054P_REGULATOR_REMOVAL_INCOMPLETE` if the finite object exists but one or more convergence/compatibility requirements fail.
- `INVALID_ITER054P` only for provenance/procedure/control failure.

## Interpretation locks

Even PASS establishes only a scoped relative-observable regulator-removal object for the frozen normalized coherent-history class. It does **not** establish a global interacting path-integral measure, absolute probability measure, unitarity, UV completion, full continuum QGR, theory correctness, experimental confirmation, `beta=1`, an absolute `c6` identity, physical branch weights, or KMQGB `NEW_REQUIRED`.
