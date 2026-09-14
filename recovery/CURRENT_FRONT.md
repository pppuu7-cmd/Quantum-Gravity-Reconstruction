# QGR Current Research Front

Updated: 2026-09-14
Primary active gate: `Iter054D / Weyl3 principal-order gauge fixing and characteristic audit`
Project phase: `MODEL_CONSTRUCTION / WEYL3 HYPERBOLICITY`

## Canonical claim locks

- Repository infrastructure readiness: **100%**.
- Candidate-program roadmap readiness: **99% internal bookkeeping only**, not probability of correctness.
- Theory established: **0%**.
- `beta=1`: not authorized.
- `c6`: symbolic/unfixed.
- Full covariant Weyl3 metric EOM as a global theorem: **not established**.
- Gauge-fixed covariant Weyl3 metric principal symbol: **not established**.
- Weyl3 well-posedness/hyperbolicity: **not established**.
- Quantum amplitude/measure transition: **not authorized**.
- No physical ghost/spectrum, unitarity, UV completion, full GR recovery, experimental confirmation or new-physics claim.

GitHub main + terminal Actions/results are authoritative. Historical FAIL/INVALID results are immutable.

## Iter053U — TERMINAL SCOPED PASS

Run `34797463832`; classification `PASS_SCOPED_ITER053U_CORRECTED_SOURCE_FAITHFUL_WEYL3_COMPACT_SUPPORT_ACTION_VARIATION_CERTIFICATE`.

Finite genuinely-4D compact-support computational certificate only; not a global functional-derivative theorem.

## Iter054A — TERMINAL SCOPED PASS

Run `34800952154`; classification `PASS_SCOPED_ITER054A_WEYL3_DERIVATIVE_ORDER_AND_REGIME_SEPARATION`.

Derivative-order/regime bookkeeping only; no physical mode/ghost/well-posedness claim.

## Iter054B — TERMINAL SCOPED PASS

Run `34804198271`; classification `PASS_SCOPED_ITER054B_WEYL3_PRINCIPAL_HESSIAN_ACTIVATION_WELLPOSEDNESS_NOT_AUTHORIZED`.

Finite algebraic Weyl3 Hessian activation only; not a metric PDE hyperbolicity result.

## Iter054C — TERMINAL SCOPED PASS

Gate: `ITER054C-WEYL3-LOCAL-METRIC-PRINCIPAL-SYMBOL-AND-GAUGE-DEGENERACY`.

Initial run `34808083077` is implementation/control invalid and diagnostic-only because frozen witness `[3,2,1,2]` is exactly null in Minkowski signature despite the preregistered non-null requirement. Authority record `e971882d77954749d6f951eacc5b659f73dfb660`; control-only fix `ac7cc14e111cf0d81aab4b205b255de41463a99d` changed that witness to `[3,2,1,3]` without changing formulas, backgrounds, thresholds, or scientific interpretation.

Authoritative corrected production:

- preregistration `3bc563b2aa0c691a78b57c4e7c53fd0ad9a51ba3`
- production head `f6d64a34fd5413ac199088f7cabd74749b62870d`
- run `34808147191`
- aggregate job `103864172231`
- summary artifact `10334205656`
- digest `sha256:e595bac7673d1ab2f33c78e054b904bf3cb70c676c5d33bd166a777b75f4aa0f`
- classification `PASS_SCOPED_ITER054C_WEYL3_LOCAL_METRIC_PRINCIPAL_SYMBOL_GAUGE_DEGENERACY_CONFIRMED_HYPERBOLICITY_NOT_AUTHORIZED`

Raw frozen evidence: A0 passes 4/4 exact curvature/Weyl principal-map and k^2-homogeneity probes with negative controls; A1 passes 48/48 exact symmetry, k^4-scaling, Weyl-flat zero, Weyl-active nonzero, held-out reconstruction cases; B0 passes 12/12 exact four-pure-gauge-null tests with non-gauge nontrivial controls; B1 explicitly leaves principal-order gauge fixing, characteristic real-root audit, strong hyperbolicity/equivalent estimate, constraint/gauge propagation, and energy/physical-mode interpretation unresolved.

Durable terminal note: `results/ITER054C_TERMINAL_RESULT.md` at commit `5d49cef868514e71de535b298a4ba166ad81d3a6`.

Interpretation lock: finite exact local fourth-order Weyl3 metric principal-symbol certificate only, with diffeomorphism principal degeneracy retained. This does not establish a justified gauge-fixed principal symbol, hyperbolicity, well-posedness, or physical ghost/spectrum content.

## Active blocker / Iter054D

Next gate must be prospectively frozen before outputs: `ITER054D-WEYL3-PRINCIPAL-ORDER-GAUGE-FIXING-CHARACTERISTIC-AUDIT`.

Required design obligations:

1. specify a genuine fourth-order principal gauge-fixing completion, not ordinary second-order de Donder pasted onto a fourth-order symbol;
2. prove on a frozen exact panel that the gauge completion removes the four diffeomorphism principal null directions while leaving quotient/physical symbol observables invariant across at least two nonzero gauge parameters;
3. include exact negative controls showing a deliberately wrong gauge-completion tensor fails the invariance/removal predicates;
4. freeze timelike, spacelike and null covector panels before execution and audit characteristic polynomial/root structure without post-output witness selection;
5. fail closed on strong hyperbolicity, energy estimate, constraint propagation, ghost sign, and physical spectrum unless the gate explicitly proves the corresponding obligation.

## Locked next sequence

1. Prospectively preregister Iter054D with frozen gauge completion, covectors, backgrounds, quotient observables, exact controls, and classifier.
2. Implement and run it exactly as frozen; no post-output witness or threshold changes.
3. If it passes only algebraic characteristic predicates, open a separate strong-hyperbolicity/energy/constraint gate rather than overclaiming.
4. Only after those survive may a physical Weyl-active spectrum/stability gate be opened.
5. Quantum amplitude/measure remains downstream.
