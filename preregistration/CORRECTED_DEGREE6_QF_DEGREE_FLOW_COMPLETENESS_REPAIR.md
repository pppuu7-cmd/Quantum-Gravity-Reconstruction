# Preregistration — corrected degree6 QF degree-flow completeness repair

Date: 2026-09-18

Parent: terminal `UNRESOLVED_QF_DEGREE_BUDGET`, run `35293395248`, durable result `3df530ed46d1ed9fed100ba204601a2454b28f1a`.

Gate: `CORRECTED_DEGREE6_QF_DEGREE_FLOW_COMPLETENESS_REPAIR`.

## Frozen purpose

Complete the evidence explicitly required by preregistration `10643a75f85da4ea447d00115006d78714ecfa24` without changing its scientific question, q=6..10 ladder, target, signs, normalization, source operator, or terminal thresholds.

The parent run produced a provisional q=8 plateau but lacked the required contribution decomposition and derivative degree-flow provenance. This repair may not promote that plateau unless the missing evidence independently validates it.

## Frozen implementation requirements

Two independent lanes must, before loading the Iter057AT target, construct the same canonical exact R10 seed and for q=6..10 emit exact hashes for: cubic invariant/QF, P before divergence, algebraic P·R, double-covariant-divergence, metric×I3, index-lowering contribution, and the complete ordered 840-vector source.

For every nonzero final homogeneous degree-six monomial, each lane must record the maximum upstream P/QF polynomial degree contributing after zero, one and two derivative stages. The terminal certificate must identify which contribution(s) change between q=7 and q=8 and verify whether the change is permitted by the two-derivative degree descent.

The two lanes must agree exactly on the source ladder, contribution-hash ladder, first stable budget, and degree-flow classification. They must not read each other's artifacts before aggregation.

The prior `ricci_zero`/`scalar_zero` booleans are not silently removed or reinterpreted. The repair must first diagnose why they were false on the canonical R10 seed and report whether those booleans were scientifically required by the original frozen gate. If they indicate a seed mismatch, terminal outcome is unresolved. If they are merely inapplicable diagnostics for the intentionally generic canonical seed, that fact must be established from pre-existing seed semantics/code, not inferred from the desired q=8 outcome; the terminal artifact must preserve the raw values.

## Frozen outcomes

Only the original outcome vocabulary is allowed: `QF6_SUFFICIENT_FOR_DEGREE6_SOURCE`, `QF8_REQUIRED_FOR_DEGREE6_SOURCE`, `HIGHER_THAN_QF8_REQUIRED_FOR_DEGREE6_SOURCE`, `DEGREE_BUDGET_NOT_STABLE_THROUGH_QF10`, or `UNRESOLVED_QF_DEGREE_BUDGET`.

No sign/scale fit, normalization change, target modification, post-hoc threshold change, retroactive reclassification, degree-eight coefficient authorization, or corrected-Q10 solve is allowed.

## Locks

`c6=SYMBOLIC_UNFIXED`; `beta=1` unauthorized; corrected Q10 LOCKED; theory established 0%; no experimental confirmation; finite/symmetry-reduced panels are not global theorems; G45 does not prove absolute energy positivity/quantum unitarity; G35-G37 distant roots do not authorize physical weights; KMQGB `NEW_REQUIRED` unauthorized.
