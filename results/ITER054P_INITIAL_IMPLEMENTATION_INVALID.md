# Iter054P initial production — implementation invalidity

Date: 2026-09-14

Gate: `ITER054P-INTERACTING-MEASURE-REGULATOR-REFINEMENT-REMOVAL`

Preregistration: `61e77c3576b428ab774e7caf1b6e27436e969364`

Initial implementation: `49445dccd394dba4118f1c6ebe8139668272c337`

Initial production head: `ceb42896b8654817ef7d64a1b14d943fd4135f06`

Initial run: `34859186155`

Initial job: `104026586110`

Initial artifact: `10354880624`

Initial artifact ZIP digest: `sha256:46c75c6310136fd6e1ed65c98d7ac8c1ff00b1e73cbeee22ab4b80f2551ad162`

Initial raw summary digest: `sha256:33ab2316f8db05c49862fe21f5b38efd5924d192c6a4eb31837e2a882e2beaa3`

## Classification

`INVALID_ITER054P_CYLINDRICAL_COMPATIBILITY_WRONG_POWER_OBJECT`

The green GitHub Actions status and emitted PASS string are not scientific authority. The initial implementation did not evaluate the frozen cylindrical-compatibility predicate on the actual frozen positive witness family.

## Exact defect

The preregistration requires `parent correction = sum of two prospectively frozen child corrections at each tested dyadic split`.

The frozen witnesses include

`P1_m = P1_inf - (7/6) epsilon_m^2`, with `epsilon_{m+1}=epsilon_m/2`.

Therefore the actual P1 correction is

`delta_m = a epsilon_m^2`, with `a=-7/6`.

Two equal dyadic children give

`delta_{m+1}+delta_{m+1} = 2 a (epsilon_m/2)^2 = (1/2) a epsilon_m^2 = delta_m/2`,

which is not equal to the parent correction for nonzero `a` and `epsilon_m`.

The implementation instead evaluated

`a epsilon_m = a epsilon_{m+1}+a epsilon_{m+1}`

for the coefficient list `[3/5,-7/6,2/3,-5/4]`. That linear identity is true, but for the `-7/6` entry it is not the P1 correction appearing in the frozen positive panel. Thus the implementation substituted a linear-in-epsilon object for the frozen quadratic P1 object.

## Scope

This is an implementation/object-identity invalidity, not a scientific FAIL of the regulator-removal hypothesis. The preregistered objects, witness sequences, thresholds, negative controls, and interpretation ceiling remain frozen and unchanged.

A control-only exact retry is authorized by replacing only the cylindrical-compatibility implementation so that it evaluates the actual correction sequences `P0-P0_inf`, `P1-P1_inf`, `GR-GR_inf`, and `W3-W3_inf`. The historical initial run remains immutable and cannot be reclassified as PASS.

If the corrected implementation finds one or more frozen convergence/compatibility requirements false, the preregistered terminal classification is `BLOCKED_OBJECT_DEFINITION_ITER054P_REGULATOR_REMOVAL_INCOMPLETE`.