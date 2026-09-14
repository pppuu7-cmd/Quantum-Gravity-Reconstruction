# Iter054G preregistration — Weyl3 dynamical-treatment selection authority

Date: 2026-09-14

Gate: `ITER054G-WEYL3-DYNAMICAL-TREATMENT-SELECTION-AUTHORITY`

Status at freeze: **PREREGISTERED BEFORE TERMINAL TREATMENT-SELECTION VERDICT**

Frozen source snapshot: `3398cd5a195d3d6b05fad01715ab5b79a880c4f1`

## Scientific question

Does QGR authority already present in the frozen source snapshot derive a non-post-hoc physical rule selecting how the later symbolic `c6 * Weyl^3` correction is to be used dynamically:

1. **EXACT** — finite-`c6` higher-derivative dynamics with the complete exact Euler-Lagrange solution space and its corresponding additional initial-data/evolution structure; or
2. **ORDER_REDUCED** — perturbative/effective dynamics retaining the branch analytic at `c6=0`, with an independently derived expansion parameter/validity domain/cutoff and a rule for eliminating higher derivatives order by order;

or is neither treatment selected by existing microscopic authority?

The gate does **not** choose a treatment because one later gives a preferred stability, spectrum or hyperbolicity result.

## Dependency

Iter054F terminally classified

`BLOCKED_OBJECT_DEFINITION_ITER054F_MIXED_ORDER_EVOLUTION_REDUCTION_NOT_FIXED`.

A preferred first-order reduction cannot be constructed prospectively until QGR specifies which dynamical solution space it is reducing. Exact fourth-order and order-reduced effective formulations are not the same admissible-history prescription.

The QGR constitution forbids hidden branch selection after observing outcomes. Therefore treatment selection is an upstream model-definition obligation.

## Frozen authority domain

All scientific authority consumed by this gate must exist in source snapshot

`3398cd5a195d3d6b05fad01715ab5b79a880c4f1`.

Later commits cannot retroactively satisfy Iter054G.

Primary frozen authorities include, but the source-census lane is not limited to:

- `docs/CONSTITUTION.md`;
- `iterations/ITERATION_006.md`;
- `iterations/ITERATION_010.md`;
- `iterations/ITERATION_011.md`;
- `status/ITERATION_047.md`;
- `preregistration/ITER054A_WEYL3_DERIVATIVE_ORDER_AND_REGIME_SEPARATION.md`;
- `results/ITER054A_TERMINAL_RESULT.md`;
- `results/ITER054E_TERMINAL_RESULT.md`;
- `results/ITER054F_TERMINAL_RESULT.md`;
- current `recovery/CURRENT_FRONT.md` and `recovery/state.json` at the frozen snapshot.

`analysis/` notes are explicitly **non-authoritative** and may not supply the selector.

## What counts as a valid selector

### Exact-treatment selector

`EXACT_SELECTED` requires an already-derived QGR authority that explicitly supplies all of:

1. finite nonzero `c6` is to be treated as an exact dynamical coupling, not only as a symbolic/operator/finite-order correction;
2. the physical admissible history/solution space includes the complete higher-derivative Euler-Lagrange solution space or an explicitly equivalent formulation;
3. any additional initial-data/state content is mapped to the QGR physical state/measure/composition structure rather than silently added;
4. a validity domain is stated for this exact use;
5. the selection predates this gate and is not inferred from a preferred stability/spectrum outcome.

Anything less is `EXACT_NOT_SELECTED`.

### Order-reduced selector

`ORDER_REDUCED_SELECTED` requires an already-derived QGR authority that explicitly supplies all of:

1. a controlled small derivative/coupling/scale expansion for the Weyl3 correction;
2. a QGR-derived validity domain or cutoff/matching scale, not an external guessed EFT scale;
3. an explicit order-reduction prescription eliminating higher derivatives using lower-order equations to the declared order;
4. an explicit reason the non-analytic singular branch lies outside the admissible domain, rather than dropping it after inspecting its behavior;
5. mapping of the reduced equations back to the QGR microscopic/state/composition structure and GR limit;
6. the selection predates this gate and is not inferred from a preferred stability/spectrum outcome.

Anything less is `ORDER_REDUCED_NOT_SELECTED`.

A source merely mentioning `EFT`, `order-reduced`, `perturbative`, `exact`, `Weyl^3` or `c6` is not a selector.

## Frozen streams

### S0 — frozen repository authority census

At the frozen source snapshot, enumerate textual authority under `docs/`, `iterations/`, `status/`, `results/`, `recovery/`, `prereg/`, and `preregistration/` for treatment-related terms including:

- `order-reduc*`;
- `effective field` / `EFT`;
- `cutoff` / `validity domain` / `matching scale`;
- `exact` near `c6`/`Weyl3`/higher-derivative dynamics;
- `additional initial data` / `solution space` / `branch selection`.

The lane records every matching file/path and excerpt deterministically. It does not promote keyword hits to authority.

Unexpected candidate selector text not covered by A0/A1 must make the aggregate fail closed as `REQUIRES_SOURCE_AUTHORITY_REVIEW`, not silently ignore it.

### A0 — exact finite-c6 treatment authority

Audit the frozen authority against all five exact-selector obligations.

Output exactly one of:

- `EXACT_SELECTED`;
- `EXACT_NOT_SELECTED`;
- `INVALID_PROVENANCE`.

Report each obligation separately with source paths.

### A1 — order-reduced/EFT treatment authority

Audit the frozen authority against all six order-reduced-selector obligations.

Output exactly one of:

- `ORDER_REDUCED_SELECTED`;
- `ORDER_REDUCED_NOT_SELECTED`;
- `INVALID_PROVENANCE`.

Report each obligation separately with source paths.

### B0 — exact solution-space distinction control

Use the exact schematic operator equation

`D phi + eps*lambda*D^2 phi = 0`

with nonzero symbolic `eps,lambda` and commuting scalar eigenvalue variable `z`.

Require exactly:

1. characteristic/operator polynomial factorization `z*(1+eps*lambda*z)`;
2. exact branches `z=0` and `z=-1/(eps*lambda)`;
3. the second branch is singular/non-analytic at `eps=0`;
4. a finite Taylor ansatz connected to the `z=0` branch cannot equal the singular root;
5. with `eps=0`, only the GR-connected factor remains.

This proves only that exact and analytic perturbative solution spaces can differ; it is not a QGR treatment choice.

### B1 — anti-posthoc / claim firewall

Require the frozen governance conclusions:

- no treatment may be selected because it gives a preferred later hyperbolicity/spectrum result;
- a missing selector is `BLOCKED_OBJECT_DEFINITION`, not candidate failure;
- no ghost, physical extra-mode, stability, unitarity or quantum conclusion follows;
- `c6` remains symbolic/unfixed;
- `beta=1` remains unauthorized;
- theory established remains 0%.

## Frozen aggregate classifier

All S0/A0/A1/B0/B1 artifacts must be present and valid.

If an unexpected plausible selector source is discovered by S0 and not adjudicated by the frozen A0/A1 source mapping:

`REQUIRES_SOURCE_AUTHORITY_REVIEW_ITER054G`

Otherwise:

- A0=`EXACT_SELECTED`, A1=`ORDER_REDUCED_NOT_SELECTED` -> `ITER054G_EXACT_DYNAMICAL_TREATMENT_SELECTED_READY_FOR_PROSPECTIVE_EXACT_EVOLUTION_REDUCTION`;
- A0=`EXACT_NOT_SELECTED`, A1=`ORDER_REDUCED_SELECTED` -> `ITER054G_ORDER_REDUCED_DYNAMICAL_TREATMENT_SELECTED_READY_FOR_PROSPECTIVE_REDUCED_EVOLUTION_CONSTRUCTION`;
- both selected -> `BLOCKED_OBJECT_DEFINITION_ITER054G_MULTIPLE_DYNAMICAL_TREATMENTS_AUTHORIZED_WITHOUT_SELECTION_RULE`;
- neither selected -> `BLOCKED_OBJECT_DEFINITION_ITER054G_WEYL3_DYNAMICAL_TREATMENT_NOT_SELECTED`;
- provenance/control failure -> `INVALID_IMPLEMENTATION_OR_PROVENANCE_ITER054G`.

No result in this gate is called a scientific PASS merely because a source exists. A selector result only authorizes a separate prospective construction of the corresponding evolution object.

## Interpretation ceiling

Iter054G can establish only whether the existing QGR authority selects a dynamical treatment. It cannot establish strong hyperbolicity, well-posedness, physical mode count, residue/ghost sign, energy positivity, quantum unitarity, a quantum amplitude/measure, fixed `c6`, `beta=1`, UV completion, full GR recovery, experimental confirmation or new physics.

A terminal BLOCKED outcome is valid progress and must not be repaired by inventing a preferred treatment inside the same gate.
