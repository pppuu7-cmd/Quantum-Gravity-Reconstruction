# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter008`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / INTRINSIC_RELATIONAL_CLOCK_DERIVED / PHYSICAL_SCALE_CALIBRATION_OPEN`
Active roadmap stage: `R9 prediction-discrimination / physical-scale and relational-matter reconstruction`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **87%**
- Iter005 completion: **100%**
- Iter006 completion: **100%**
- Iter007 completion: **100%**
- Iter008 completion: **25%**
- Theory established: **0%**
- Lead architecture: `A / CCRC`
- Active candidate: `QGR-L1`
- Local metric-only two-derivative action: **all-orders PASS_SCOPED**
- Physical characteristic quotient: **2 modes**
- Full cutoff-free broadband two-mode history comparator: **PASS_SCOPED**
- Leading tested finite-history refinement order: **O(h^4)**
- Intrinsic relational clock `tau(S)=|S|`: **PASS_SCOPED**
- Clock-conditioned sequential history/isometry factorization: **PASS_SCOPED**
- Physical duration of one rank tick: **OPEN**
- Remaining microscopic normalization: `g=kappa/hbar`, **unfixed**
- Independent KMQGB pass: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED by latest authoritative recovery state**

Readiness is an internal construction-roadmap metric, not probability of correctness.

## Established same-realization chain

`B4 relational seed`
`-> four derived directions + Lorentzian incidence form`
`-> Sym^2(W4) ten-component response`
`-> derivative gauge closure / no onsite mass`
`-> two physical characteristic modes`
`-> unique cubic + quartic self-coupling`
`-> all-orders metric-only two-derivative local action`
`-> Lorentzian configuration Hilbert / BRST operational algebra`
`-> refinement-connected finite torsion-free connection`
`-> path-groupoid transport`
`-> normalized 24-history instrument`
`-> O(h^4) finite-history correction`
`-> finite overlapping-region local net`
`-> positive two-mode characteristic pairing`
`-> cutoff-free broadband comparator`
`-> scale identifiability boundary g=kappa/hbar`
`-> intrinsic Boolean rank clock tau=|S|`
`-> exact clock-conditioned one-tick branch/isometry factorization`.

No Planck-scale identification, `g=1`, arbitrary noise coefficient, arbitrary polarization projector, or external matter normalization has been inserted.

## Iter007 closed boundary

Iter007 is complete. The model-side observable problem closed positively, while the absolute physical-scale problem closed negatively in the current realization.

The continuum matching is

`a_cont = c_geom kappa/h^2`.

Restoring `hbar` gives

`g=kappa/hbar`, `ell_Q^2=hbar/a_cont`,

and therefore

`h^2=c_geom g ell_Q^2`.

The current QGR chain fixes neither `g` nor a nonzero refinement stop scale. If `h` is only a regulator and is removed with continuum normalization fixed, the finite-history correction vanishes as `h^4`.

Authoritative records:

- `iterations/ITERATION_007.md`
- `results/ITER007_G7B_G7D_SCALE_BOUNDARY.md`
- `results/ITER007_G7A_MICROSCOPIC_SCALE_IDENTIFIABILITY.md`
- `results/ITER007_G6E_G6H_CURVED_BROADBAND_OBSERVABLE_CLOSURE.md`

## Iter008 G1 — intrinsic Boolean clock

Actions run `34660061343`: four lanes + aggregate SUCCESS.

Within the tested `S4`-invariant, zero-at-empty, disjoint-additive scalar class, unit elementary increment fixes uniquely

`tau(S)=|S|`.

Its symmetric gradient is the timelike direction of the already-derived `1+3` Lorentzian seed; the sum-zero transverse sector is three-dimensional with opposite sign. Fixed-rank levels are antichains, and all 24 maximal histories share the exact profile

`0 -> 1 -> 2 -> 3 -> 4`.

Rank composes across true serial B4 cells. Its dual quasi-frequency is compact but dimensionless; no physical tick duration follows yet.

## Iter008 G2 — sequential clock-conditioned quantum instrument

Actions run `34660219520`: four lanes + aggregate SUCCESS.

At rank `r`, the exact conditional next-direction law is

`P(next | r)=1/(4-r)`.

The one-step coherent moduli are

`1/sqrt(4), 1/sqrt(3), 1/sqrt(2), 1`,

whose product is exactly `1/sqrt(24)`. Thus the global normalized 24-history amplitude is the product of intrinsic-clock one-step isometries.

Clock-conditioned prefixes/suffixes are compatible with the established path-groupoid composition law.

A clock-only `S4`-invariant edge phase is removable by rank-slice vertex rephasing, so the intrinsic scalar clock does not by itself create a physical Hamiltonian phase or fix `g`.

Record:
`results/ITER008_G1_G2_INTRINSIC_BOOLEAN_CLOCK_AND_SEQUENTIAL_HISTORY.md`.

## Active blocker / G3

`MISSING_DERIVED_PHYSICAL_TICK_CALIBRATION_OR_NONTRIVIAL_MICROSCOPIC_QUANTIZATION_PRINCIPLE_FIXING_OR_BOUNDING_G`

Active gate:
`QGR-ITER008-G3-CLOCK-GEOMETRY-TOPOLOGICAL-QUANTIZATION-AND-MATTER-CALIBRATION`

Parallel tests:

1. distinguish rank increment from proper time and test whether the derived Lorentzian geometry supplies a non-arbitrary tick/lapse calibration;
2. audit the topology of the Lorentzian configuration space for a continuous two-form class capable of quantizing the microscopic action normalization;
3. derive the minimal rank-translation-invariant clock dynamics and determine whether its frequency normalization is fixed or is a new free coupling;
4. derive the minimal relational matter principal operator from the same incidence/metric structure and test whether operational normalization gives an independent scale relation.

Fail closed if the answer requires `g=1`, `h=l_P`, one rank tick = Planck time, or phenomenological fitting.

## KMQGB synchronization

Latest observed KMQGB head: `d812ccd09f93defb5b407d5cc2cc970764d8ffe6`, message `Iter374-378: launch parallel DSI parity observable audit`.

Its latest authoritative `recovery/state.json` is older than that head but still records `Paper-IV global_decision=NOT_YET_AUTHORIZED`, `new_required_authorized=false`, and `D7=NOT_CLOSED`. Until KMQGB itself updates that authoritative decision, QGR may not infer `NEW_REQUIRED` from later commits.

## Claim locks

- no experimental confirmation;
- theory established remains `0%`;
- no absolute numerical phenomenology until `g`/clock-matter calibration is derived or independently bounded;
- no `g=1`, `h=l_P`, Planck-time tick, or minimum length by convention;
- no independent KMQGB pass;
- no claim all known models fail;
- no `NEW_REQUIRED` authorization;
- no claim QGR is unique/correct as a full quantum-gravity theory.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `iterations/ITERATION_008.md`
4. `results/ITER008_G1_G2_INTRINSIC_BOOLEAN_CLOCK_AND_SEQUENTIAL_HISTORY.md`
5. `iterations/ITERATION_007.md`
6. `results/ITER007_G7B_G7D_SCALE_BOUNDARY.md`
7. `results/ITER007_G7A_MICROSCOPIC_SCALE_IDENTIFIABILITY.md`
8. `results/ITER007_G6E_G6H_CURVED_BROADBAND_OBSERVABLE_CLOSURE.md`
9. `iterations/ITERATION_006.md`
10. `docs/CONSTITUTION.md`
11. current KMQGB authoritative benchmark decision and latest scoped deltas
