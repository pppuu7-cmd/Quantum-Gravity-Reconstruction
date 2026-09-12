# QGR Iter009-G2 — finite operator dynamics and first effective-action redundancy audit

Date: 2026-09-12
Status: `PARTIAL_SCOPED_FINITE_DEPTH_INTERACTING_OPERATOR_DYNAMICS_WELL_DEFINED / CURVATURE_SQUARED_VACUUM_REDUNDANT / SIX_DERIVATIVE_AND_INFINITE_LIMIT_OPEN`

GitHub Actions run: `34663104103` — 6 lanes + aggregate SUCCESS.

An earlier run `34663065413` had five successful lanes and one technical failure caused by floating-point equality in the finite-depth completeness check. The criterion was unchanged; the calculation was replaced by exact rational arithmetic and the second run passed.

## G2A — normalized states on an infinite reference measure

Along the scale orbit write `t=log s`. The invariant scale measure is `dt`, which has infinite total volume. This does not prevent normalized `L2` states. For example

`psi(t)=(2a/pi)^(1/4) exp(-a t^2)`, `a>0`,

has exact norm one.

Thus G1 blocks interpreting the reference measure itself as a normalized vacuum probability, not the existence of normalized state vectors.

Classification:
`PASS_SCOPED_INFINITE_REFERENCE_MEASURE_VOLUME_DOES_NOT_PREVENT_NORMALIZED_L2_STATES`.

## G2B — arbitrary finite-depth history composition

At depth `n` there are `24^n` histories. Each branch has completeness weight `24^-n`, so exactly

`24^n * 24^-n = 1`.

With unitary/quasi-invariant branch lifts this recursively preserves the finite-depth isometry/CPTP normalization at every finite `n` without using a normalized global vacuum measure.

Classification:
`PASS_SCOPED_ARBITRARY_FINITE_DEPTH_HISTORY_COMPOSITION_REMAINS_NORMALIZED_CPTP_ISOMETRIC_GIVEN_UNITARY_BRANCH_LIFTS`.

## G2C — finite-cell action authority audit

The authoritative repository was scanned for a declared exact microscopic finite-cell action closure beyond the local/continuum action and scoped branch-action evaluation. No positive closure marker was found.

This is a repository-authority result, not a mathematical impossibility theorem. Current authority therefore remains: exact local all-orders two-derivative action plus finite branch operators in their verified scope, but no independently frozen exact higher-derivative finite-cell action from which all effective coefficients can yet be expanded.

Classification:
`BLOCKED_SCOPED_NO_AUTHORITATIVE_EXACT_FINITE_CELL_HIGHER_DERIVATIVE_ACTION_CLOSURE_FOUND_IN_CURRENT_REPOSITORY`.

## G2D — curvature-squared field-redefinition rank

G1 counted two parity-even four-derivative bulk directions modulo Euler/topological and total-derivative identities. They must not automatically be counted as two new physical vacuum parameters.

For the pure vacuum EH/QGR local branch, perform the first-order local field redefinition

`delta g^{mu nu} = a R^{mu nu} + b g^{mu nu} R`.

Using the vacuum Einstein tensor in four dimensions,

`G_munu delta g^munu`

maps `(a,b)` to coefficients of `(R_munu R^munu, R^2)` as

`(a, -(a/2+b))`.

The exact coefficient matrix is

`[[1,0],[-1/2,-1]]`,

with determinant `-1` and rank **2**.

Therefore both parity-even curvature-squared bulk directions are EOM-redundant for pure vacuum on-shell physics at first correction order, modulo the already separated topological/boundary terms.

Classification:
`PASS_SCOPED_BOTH_PARITY_EVEN_CURVATURE_SQUARED_BULK_DIRECTIONS_ARE_EOM_REDUNDANT_FOR_PURE_VACUUM_EH_BRANCH_AT_FIRST_CORRECTION_ORDER`.

Boundary: this does not remove their possible relevance from off-shell effective actions, matter coupling, boundaries/topology, or measure/Jacobian questions.

## G2E — first order not removed by the current redundancy argument

G1 power counting gives `omega=2L+2`. The `L=1` four-derivative vacuum bulk directions are removed from the physical on-shell quotient by G2D. The first power-counting level not eliminated by that argument is therefore

`six derivatives`,

i.e. curvature-cubed and/or derivative-curvature structures.

This is only a target class. G2 does not prove a coefficient is nonzero, divergent or unique.

Classification:
`PARTIAL_SCOPED_FIRST_POTENTIALLY_PHYSICAL_LOCAL_VACUUM_CORRECTION_MOVES_TO_SIX_DERIVATIVES_BUT_COMPLETE_SIX_DERIVATIVE_CENSUS_AND_MICROSCOPIC_COEFFICIENTS_REMAIN_OPEN`.

## G2F — infinite-refinement criterion

A sufficient channel convergence condition is, for example,

`sum_n ||Phi_{n+1}-Phi_n||_diamond < infinity`.

If a **uniform channel bound** of order `h_n^4` existed on a dyadic sequence `h_n=2^-n`, the geometric series would be summable. QGR currently has `O(h^4)` convergence only for specified normalized observables/comparators, not a uniform diamond or strong operator bound on the full interacting channel family.

Therefore exact finite-depth normalization cannot yet be promoted to an infinite-refinement interacting operator limit.

Classification:
`BLOCKED_SCOPED_FINITE_DEPTH_CHANNELS_ARE_EXACTLY_NORMALIZED_BUT_CURRENT_OBSERVABLE_H4_SCALING_DOES_NOT_PROVE_AN_INFINITE_REFINEMENT_OPERATOR_LIMIT`.

## Consolidated result

`PARTIAL_SCOPED_FINITE_DEPTH_INTERACTING_OPERATOR_DYNAMICS_IS_WELL_DEFINED_WITH_NORMALIZED_L2_STATES__CURVATURE_SQUARED_VACUUM_BULK_DIRECTIONS_ARE_FIELD_REDEFINITION_REDUNDANT__SIX_DERIVATIVE_MICROSCOPIC_MATCHING_AND_INFINITE_REFINEMENT_LIMIT_REMAIN_OPEN`.

The scientifically important correction to G1 is that the two curvature-squared directions are not two physical pure-vacuum parameters at the first correction order. The next physical local target moves to six derivatives.

## External sanity only — not a selection input

This scoped result is consistent with the classic perturbative-gravity pattern: pure Einstein gravity is on-shell finite at one loop after the four-dimensional identities/EOM are used, while a genuine curvature-cubed counterterm appears at two loops. This historical fact is used only as an a posteriori sanity check; QGR may not import the continuum two-loop coefficient as its microscopic prediction.

## Next gate

`QGR-ITER009-G3-SIX-DERIVATIVE-PHYSICAL-OPERATOR-CENSUS-AND-FINITE-REFINEMENT-MATCHING`

Required:

1. identify the parity-even on-shell pure-vacuum six-derivative basis in four dimensions;
2. reduce derivative-curvature structures by Bianchi/integration-by-parts/EOM rather than double-counting them;
3. construct a nonzero Ricci-flat witness for any surviving curvature-cubed invariant;
4. derive its refinement scaling in terms of `Gamma`;
5. audit whether current QGR microscopic data fix its coefficient;
6. determine whether it enters at the same `O(h^4)` order as the existing finite-history broadband effect.
