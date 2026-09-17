# Preregistration — corrected degree6 QF degree-budget causal adjudication

Date: 2026-09-18

Gate: `CORRECTED_DEGREE6_QF_DEGREE_BUDGET_CAUSAL_ADJUDICATION`

Parent terminal diagnostic: `LOCALIZED_CUBIC_QF_CEILING_MISMATCH`, authoritative run `35280241071`, durable record commit `785192ba589cc79ef6656413adc7970d24f641dd`.

## Frozen question

For the homogeneous degree-six Euler source of `sqrt(-g) Weyl^3` on the canonical exact R10 seed, what minimum upstream cubic/QF/P jet degree is mathematically sufficient to make every contribution to the final degree-six source invariant under further degree-budget increases, accounting explicitly for the two coordinate derivatives in the double-covariant-divergence term?

This gate adjudicates degree bookkeeping only. It does not repair or reclassify Iter057AT or corrected Iter057Y, and cannot authorize degree-eight source coefficients or Q10.

## Prospective interventions

Before loading the durable Iter057AT target, two independent lanes must construct the same canonical R10 seed and evaluate a monotone upstream budget ladder `q = 6,7,8,9,10` while holding the final requested source projection fixed at homogeneous degree six. For each q, retain sufficient P jet order for the double divergence and freeze exact hashes for: cubic invariant/QF, P before divergence, algebraic P·R contribution, double-divergence contribution, metric×I3 contribution, index-lowering contribution, and complete ordered 840-vector source.

The lanes must additionally perform a degree-flow audit: for every nonzero final degree-six monomial, record the maximum upstream P/QF degree that contributes after zero, one, and two derivative operations. No numerical tolerance, fitting, sign flip, scale fit, or normalization change is permitted.

Only after the complete ladder and degree-flow tables are frozen locally may the Iter057AT target hash `5d070732d90b864f6167e03da85b86ce531d127dc9442fdbb928fd1b6153ee6b` and parent generalized hash `2f15c55c0b326966c821141e43e245e3715f93fc9f4b9ee720179f31b1e28b6d` be compared.

## Independent lanes

Researcher: direct exact polynomial bookkeeping from the corrected Frechet constructor.

Critic: independently reconstruct contribution degree flow and final degree-six source without reading Researcher artifacts before terminal aggregation.

## Frozen terminal outcomes

Terminal aggregation may emit only:
- `QF6_SUFFICIENT_FOR_DEGREE6_SOURCE` if q=6 is already invariant under all q=7..10 increases and both lanes reproduce the same full source;
- `QF8_REQUIRED_FOR_DEGREE6_SOURCE` if q=6/7 are not invariant but q=8 is the first stable budget through q=10, with the causal change carried by terms allowed to descend through the double divergence;
- `HIGHER_THAN_QF8_REQUIRED_FOR_DEGREE6_SOURCE` if stability begins only at q=9 or q=10;
- `DEGREE_BUDGET_NOT_STABLE_THROUGH_QF10` if no stable plateau exists through q=10;
- `UNRESOLVED_QF_DEGREE_BUDGET` for lane disagreement, failed exact controls, missing degree-flow provenance, or any other pattern.

No outcome is a theory PASS. If a higher budget is required, historical Iter057AT remains historical authority until a separate prospectively preregistered corrected-source reconstruction and descendant replay are completed; no retroactive reclassification is allowed.

## Frozen controls and locks

Same exact canonical seed; exact Fraction arithmetic; complete ordered 840-vector at every budget; target-blind construction; explicit derivative degree-flow accounting; two independent implementations; `c6=SYMBOLIC_UNFIXED`; `beta=1` unauthorized; corrected Q10 LOCKED; theory established 0%; no experimental, global-theorem, unitarity, measure, regulator-removal, UV-completion, unique-theory, or KMQGB NEW_REQUIRED claim.