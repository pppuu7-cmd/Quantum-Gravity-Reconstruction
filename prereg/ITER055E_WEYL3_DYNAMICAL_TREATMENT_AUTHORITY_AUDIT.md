# Iter055E preregistration — Weyl3 dynamical-treatment authority audit

Date: 2026-09-14

## Target hypothesis

A pre-existing QGR source/authority may already specify how the `c6 * Weyl^3` six-derivative term is to be used dynamically on the same realization: either as exact higher-derivative equations, as a perturbative/order-reduced EFT correction, or by another explicit source-faithful prescription. If no such same-realization rule exists, physical pole/ghost/hyperbolicity interpretation remains BLOCKED even though the operator itself is defined.

## Exact object

The object is **not** the existence of a Weyl3 effective-action term. The object is an explicit QGR dynamical-treatment rule that fixes which equations/generator are physically authoritative when `c6 != 0`, including whether extra higher-derivative solution branches are retained or perturbatively eliminated.

## Dependency tested

`Weyl3 operator and symbolic c6 -> physically defined evolution equations -> interpretable characteristic/spectrum/hyperbolicity gate`.

## Frozen source scope

Audit the pre-existing Iter009 six-derivative/effective-action/decoupling/strong-limit layer and any directly referenced later QGR stability/spectrum authority needed to interpret it. Do not introduce external EFT assumptions or a post-hoc order-reduction rule.

## Positive control

The audit must recover that QGR already defines a finite-operator/effective-action Weyl3 correction with symbolic `c6` in its stated scope.

## PASS

PASS only if a pre-existing QGR authority explicitly selects a dynamical treatment for the same Weyl-active `c6` realization and specifies how the physical evolution/characteristic problem is formed, sufficiently to decide whether higher-derivative branches are physical or order-reduced away.

## BLOCKED

BLOCKED if the repository defines the operator/effective action and its scaling/decoupling properties but does not select exact-vs-order-reduced (or equivalent) dynamics for the same realization.

## FAIL

FAIL only if an explicit pre-existing treatment rule exists but is internally inconsistent with another already-authoritative same-realization QGR rule.

## INVALID

INVALID if the audited files concern a different object (for example only coefficient scaling, Euclidean effective action bookkeeping, or flat-background operator existence) and are mistakenly promoted to a physical dynamical-treatment selector.

## Interpretation ceiling

This gate can establish or deny source authority for the treatment rule. It cannot by itself prove strong hyperbolicity, ghost-freedom, quantum unitarity, UV completion, or fix `c6`.

## Claim locks

- `c6` remains symbolic/unfixed.
- `beta=1` unauthorized.
- theory established = 0%.
- no physical ghost/spectrum verdict without a treatment rule.
