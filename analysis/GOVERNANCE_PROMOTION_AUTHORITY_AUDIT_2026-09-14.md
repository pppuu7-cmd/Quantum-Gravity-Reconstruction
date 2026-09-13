# QGR candidate-promotion authority audit

Date: 2026-09-14
Status: governance/provenance audit only. No scientific gate is reclassified by this note.

## Question

`docs/ROADMAP.md` and `README.md` still contain bootstrap-era current-status text saying, respectively, that R1 is active / R2 is not promoted and that the project is Iter001 with no promoted physical ansatz and 24% candidate-program readiness. Current recovery instead records an active QGR-L1 second-moment/Weyl3 model-construction line and a much later internal readiness marker.

Does the repository contain a prospective, durable authority chain that actually crossed the pre-ansatz boundary and selected the QGR-L1 candidate, or did later work silently outrun the roadmap?

## Bootstrap documents are historical snapshots, not current gate state

`docs/ROADMAP.md` was introduced by commit `c10de330115826afadf1dca6820b5f80ea0275cf` (`QGR Iter001: add staged construction roadmap`) on 2026-09-11 and has no later commit in its path history as of this audit.

Its normative staged obligations remain useful, but its `Current position` block is therefore an Iter001 snapshot.

Likewise, current `README.md` still says:

- `QGR iteration: Iter001`;
- canonical candidate-program readiness `24%`;
- promoted physical ansatz `none`;
- immediate target `QGR-G0` minimum viable ontology.

Those statements are plainly historical relative to the later durable iteration/results/recovery chain.

## Explicit pre-ansatz crossing authority — Iter003

`iterations/ITERATION_003.md` is explicit:

- status `COMPLETE / PROPOSED_LINEARIZED_ANSATZ / MASS_GAUGE_BLOCKED`;
- `Physical ansatz promoted: YES — LINEARIZED L0 ONLY`;
- candidate-program readiness moved from 24% to 30%;
- the iteration states that QGR **crossed the pre-ansatz boundary** and possessed an explicit, low-freedom, reproducible linearized candidate action.

The promoted chain was same-realization within its finite/linearized scope:

`Boolean causal order -> derived d=4 -> rank-2 pair incidence -> 2D physical quotient -> Lorentzian pair form -> hyperbolic pair-action`.

The promotion was not a declaration of a complete model: protected masslessness, nonlinear closure, GR, refinement, observables and quantum completion were explicitly left open.

Therefore Iter003 supplies the first durable explicit repository authority superseding the bootstrap statement `physical ansatz promoted: none`.

## QGR-L1 branch selection authority — Iter004 G6

Commit `425232121b2f525cd1ee56371187be1da2f52a19`, `Iter004 G6: select gauge-closed causal two-mode QGR-L1 branch`, prospectively selects QGR-L1 from the frozen derivative-gauge-compatible family using previously derived QGR-internal data:

- the incidence causal form `C=J-I`;
- its characteristic cone;
- an independently derived exact two-dimensional physical quotient.

The selection rejects the three-physical-mode branch and retains the two-mode branch `t=1/2`.

The result explicitly says QGR-L1 is promoted **only** as

`PROPOSED_LINEARIZED_GAUGE_CLOSED_CAUSAL_TWO_MODE_CANDIDATE`.

The standard Fierz-Pauli comparison was performed only a posteriori and was not a selection criterion.

Thus Iter004 provides a durable anti-overfitting-compliant selection authority for QGR-L1 while preserving a strict interpretation ceiling.

## Nonlinear / composition continuation authority

`iterations/ITERATION_005.md` then tests whether QGR-L1 can move beyond the linear candidate without inserting Einstein-Hilbert by hand. It records:

- exact cubic Noether solution;
- exact quartic Noether existence and uniqueness modulo kinematic/IBP nulls;
- weak-background two-mode characteristic stability;
- a same-realization kinematic refinement tower;
- an explicit blocker that dynamic coarse-graining requires a primitive measure/amplitude/composition object.

Its decision states that local nonlinear bootstrap is closed through quartic order and hands the project to construction of the primitive quantum measure/amplitude/composition object.

`iterations/ITERATION_006.md` then records QGR-L1 as the active candidate and constructs a scoped regular-Lorentzian state/measure/composition/refinement layer, while retaining explicit negative results for disconnected all-root torsion summation.

This establishes a continuous durable candidate-construction chain rather than an unexplained jump from Iter001 to the current Weyl3 programme.

## Later Weyl3 authority

The commit history continues prospectively through later stages, including:

- Iter010 same-field-content Weyl-active background and c6 identifiability audit;
- Iter041 held-out Weyl3 generalization;
- Iter047 exact Weyl3 activation;
- Iter048/049 variational response gates;
- Iter050 covariant curvature-direction gate;
- Iter051 full covariant metric-variation programme;
- Iter052 genuinely-4D directional variation;
- Iter053/053R/053S/053T compact-support functional-variation closure/localization.

These later gates do not retroactively change the scoped status of the earlier promotions, but they show that current model-construction work has a versioned repository ancestry.

## Governance conclusion

Classification:

`PASS_GOVERNANCE_EXPLICIT_PRE_ANSATZ_AND_QGR_L1_PROMOTION_AUTHORITY_EXISTS__BOOTSTRAP_ROADMAP_AND_README_CURRENT_STATUS_BLOCKS_ARE_STALE`

Interpretation:

1. Current QGR-L1/Weyl3 work is **not** blocked merely because the Iter001 `Current position` text in `docs/ROADMAP.md` and `README.md` was never updated.
2. The normative scientific obligations in `docs/ROADMAP.md` and `docs/CONSTITUTION.md` remain binding; only their bootstrap-era mutable status/readiness text is stale.
3. `recovery/CURRENT_FRONT.md`, `recovery/state.json`, terminal results and the durable iteration chain are the appropriate current operational state sources.
4. The internal 99% candidate-program/readiness marker in recovery remains bookkeeping only. This audit does not derive or independently validate that percentage and it must never be interpreted as probability of correctness, fraction of quantum gravity solved, or roadmap-stage completion.
5. No downstream scientific transition is authorized by this governance audit. The current compact-support Weyl3 closure blocker and all claim locks remain in force.

## Recommended documentation repair after active scientific productions are terminal

A later non-scientific documentation update should preserve the original roadmap criteria while marking the `Current position` and README status blocks as historical bootstrap snapshots and directing current-state recovery to `recovery/CURRENT_FRONT.md` / `recovery/state.json` / terminal iteration records.

That repair should not rewrite the original Iter001 history and should not assign a new R-stage without a separate explicit mapping audit of the later iteration chain against R2-R9 exit criteria.
