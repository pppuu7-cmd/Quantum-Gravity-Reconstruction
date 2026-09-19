# QGR Current Research Front

Updated: 2026-09-19

## Programme status

`candidate_program_roadmap_readiness = 100%` is infrastructure/roadmap readiness only. `theory_established = 0%`. No experimental confirmation. `c6=SYMBOLIC_UNFIXED`; `beta=1` unauthorized.

## Preserved authority

Historical covariant parent remains `SCIENTIFIC_FAIL_COVARIANT_WEYL3_DIRECTIONAL_VARIATION_DISCREPANCY` (run `35367461999`, result `e26208cec90566001b65640775d2e58d0429bf5c`) and is immutable. Corrected six-cell run `35412692881` remains only a finite-panel certificate. Generic tensor-only run `35413068305` and tensor-density run `35420685309` remain immutable diagnostics. Iter049 authority and Iter048 24/24 do-not-repeat lock remain preserved by project policy.

## Generic P primitive mismatch decomposition — terminal durable

Gate: `COVARIANT_WEYL3_GENERIC_P_PRIMITIVE_MISMATCH_DECOMPOSITION`.

Preregistration `c37f4381a7876385592a74d8bc1dbade2725e03a`; production head `fa5693f1aa055df2f5f178d316e8995726cb89d8`; Actions run `35423448758` completed/success. Jobs: source-lock `105845184722`; independent `105845209411`; primary `105845209417`; reference `105845209477`; terminal `105845234516`.

Terminal artifact `10578781346` (`generic-p-primitive-terminal`), digest `sha256:65be0265270a5eeb6c24063425e2e9698b1f4cded08f4d0cc935598766900066`. Independent artifact `10578661421`, digest `sha256:0eac4153eeb8a9bb0c8faae5922112d97b03bfe877622fc1c890c5b47bdcf652`; primary `10578456495`, digest `sha256:b4fd38535f2a79820f549471a7771e9b5a87bc5eb591f03586edcf390b9cf632`; references `10578331548`, digest `sha256:e0d10f0e92523c7bd1dc0f7b33f72667ed3cec4c2763944ac561711dd427a78d`.

Frozen classification: `GENERIC_P_PRIMITIVE_DECOMPOSITION_OTHER_LOCALIZED`. First residual anchor is `P[0,1|0,1]*g2[0,0|1,1]*h[0,0]`: Lane D=`2`, primitive aggregate=`1`, residual=`1`; primitive contributions `T_a=1`, `T_d=1`, `W=-1`, all other frozen channels zero. Durable result commit: `42dfe4fe4d03ebe1d421e425753335948be493f2`. Adversarial referee commit `c4f5f3111a0f14903d635f55e3f9a072546daffd`, verdict `CONFIRMED_SCOPED`.

The result is diagnostic only. In particular `DP=0` is a preregistered source-class restriction (`partial P=0` at the normal-coordinate point), not a theorem for arbitrary curvature-derived P. No Bianchi reduction was used. The residual does not authorize a new correction or historical reclassification.

## Curvature-dependent P-jet object-definition audit — terminal BLOCKED

Gate: `COVARIANT_WEYL3_CURVATURE_P_JET_OBJECT_DEFINITION_AUDIT`.

Preregistration: `83445aa5d73d36a948b23cae4485d855831f6eb9`.
Durable terminal result: `bfe468e5d823e2fe9d31e01f4b349b10721a770a`.
Classification: `BLOCKED_MISSING_CURVATURE_P_JET_OBJECT_DEFINITION`.
Adversarial referee commit: `b9540a1df1e64d2e5b89b8ffa31e24feb6e5a25c` (`CONFIRMED_SCOPED`).

The audit was prospectively restricted to exactly two frozen source-definition files: the tensor-density preregistration at `7a62dd856aec084add16af8e6793d157ef32637b` and the primitive-decomposition preregistration at `c37f4381a7876385592a74d8bc1dbade2725e03a`. No repository search, historical artifact scan, Lane-D payload, residual payload, or external derivation was consumed.

The tensor-density source defines `P^{abcd}` only as an abstract pair-symmetric tensor and explicitly takes ordinary derivatives of the abstract source coefficients to vanish for that source class. The primitive decomposition consequently freezes `DP=0`. Neither source definition supplies an explicit curvature-dependent formula for `P` or a first-jet rule for `partial_e P^{abcd}` sufficient to construct a nonzero `DP` channel without a new assumption. Therefore the missing required object is a valid terminal BLOCKED result; inventing a derivative channel to match the residual is forbidden.

This BLOCKED result does not prove that a curvature-dependent `P` jet cannot be derived in principle. It proves only that the current authoritative source definitions do not already contain it. Historical covariant FAIL/diagnostic results remain unchanged.

## Quantum amplitude/measure closure authority-pointer audit — terminal BLOCKED

Gate: `QUANTUM_AMPLITUDE_MEASURE_CLOSURE_AUTHORITY_POINTER_AUDIT`.

Preregistration: `647ce4c5e56650c4fb4d451af1b9095afd1515a7`.
Durable terminal result: `7c67eb0744b3445db1e0758f5fd85e4bcbf8216a`.
Classification: `BLOCKED_MISSING_QUANTUM_CLOSURE_OBJECT_DEFINITION`.
Adversarial referee commit: `ab089740c383e00fe3bded50bb34e72c411ee7c5` (`CONFIRMED_SCOPED`).

The gate was prospectively frozen after the mandatory run-start recovery read and audited only the two frozen recovery authorities already required by the orchestrator. Under the frozen criterion, a quantum-closure tuple element counts as present only when recovery supplies an explicit durable repository path plus immutable commit/ref (or equivalent immutable GitHub authority identifier) for its definition. The result is `0/9 PRESENT`: no durable defining authority pointer is supplied for the quantum amplitude/state object, configuration/integration domain, measure/construction rule, gauge/Jacobian treatment, regulator/cutoff, normalization/renormalization, observable/extraction map, positivity/unitarity/probabilistic criterion, or regulator-removal/continuum-limit rule.

Negative claim locks are not object definitions. This BLOCKED result therefore does not prove impossibility; it establishes only that the prior recovery authority did not already name a complete quantum closure object. It does not authorize inventing a Hamiltonian, clock/update rule, physical normalization, regulator, observable map, or probability/unitarity semantics.

## Quantum kinematic metric-cylinder amplitude-space object v1 — preregistered

Gate: `QUANTUM_KINEMATIC_METRIC_CYLINDER_AMPLITUDE_SPACE_V1`.
Preregistration: `9c62c5a6e5d1f97908fbb42141bfc1bfedf39cd9` (`prereg/QUANTUM_KINEMATIC_METRIC_CYLINDER_AMPLITUDE_SPACE_V1.md`).
Status: `PROSPECTIVELY_PREREGISTERED_NOT_YET_IMPLEMENTED`.

The frozen target is exactly one source file: `theory/quantum/QGR_KINEMATIC_METRIC_CYLINDER_V1.md`. The object is a finite labelled cylinder of nondegenerate Lorentz-signature symmetric `4x4` metric matrices, its explicit 10N-coordinate product Lebesgue reference measure restricted to that domain, and the kinematic amplitude/state space `L^2(X_N,mu_N;C)`. The reference measure is explicitly nonphysical and non-gauge-reduced; no particular state, dynamics, Hamiltonian, clock/update rule, source normalization, gauge/Jacobian treatment, observable map, probability/unitarity theorem, regulator-removal rule, or continuum limit is introduced.

Frozen PASS is only `PASS_SCOPED_QUANTUM_KINEMATIC_METRIC_CYLINDER_AMPLITUDE_SPACE_DEFINED`; it establishes a finite-cylinder kinematic amplitude/state space with domain and reference-measure semantics, not quantum closure. All stronger quantum semantics remain BLOCKED.

## Next bounded step

`QUANTUM_KINEMATIC_METRIC_CYLINDER_AMPLITUDE_SPACE_V1` is the sole preregistered gate. The next run must inspect only its preregistration and implement exactly the frozen target source file if the definitions can be realized without adding assumptions. No repository search, historical artifact scan, classical-certificate import, or Actions computation is needed. After source creation, classify strictly under the frozen PASS/FAIL/BLOCKED/INVALID taxonomy and update recovery. Do not open a second quantum gate in the same run.

## Locks

`theory_established=0%`; no experimental confirmation; `c6=SYMBOLIC_UNFIXED`; corrected Q10 LOCKED; `beta=1` unauthorized; finite panels are not global theorems; G45 does not prove absolute energy positivity or quantum unitarity; G35-G37 distant roots do not authorize physical weights; KMQGB `NEW_REQUIRED` unauthorized; classical != quantum; diagnostic != closure.