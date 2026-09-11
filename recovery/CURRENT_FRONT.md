# QGR Current Research Front

Updated: 2026-09-11
Active iteration: `Iter004`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / LINEARIZED_ANSATZ_PROPOSED`
Active roadmap stage: `R4 — local mathematical / gauge-constraint closure`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **30%**
- Iter003 completion: **100%**
- Iter004 completion: **55%**
- Lead architecture: `A / CCRC`
- Active candidate: `QGR-L0`
- Candidate state: `PROPOSED_LINEARIZED / MASS_GAUGE_BLOCKED`
- Full theory established: **NO**
- Independent benchmark passed: **NO**
- KMQGB `NEW_REQUIRED` authorization: **NO**

Readiness is an internal construction-roadmap metric, not probability of correctness.

## Iter003 closed result

The same finite `B_4` realization now supplies the chain

`Boolean causal order -> derived d=4 -> six rank-2 pair variables -> exact 2D physical quotient -> Lorentzian pair-incidence form -> hyperbolic linearized pair action`.

Key exact results:

- `B_4` has 16 events, rank profile `(1,4,6,4,1)`, 24 maximal chains;
- exact symmetric path normalization `w_4=1/24`;
- pair representation `6=1+3+2`;
- rank-1 redefinition image has dimension 4, leaving exact 2D quotient;
- rank-2 pair incidence `C=J-I` has spectrum `(3,-1,-1,-1)`;
- proposed linearized action `S2=(kappa/2) Dq^T (J-I) Dq` is hyperbolic;
- both physical pair components share the same kinetic tensor;
- current lower-rank redundancy does **not** forbid `m^2 q^2`.

Iter003 therefore promoted the first explicit linearized candidate `QGR-L0` but ended with mass/gauge protection open.

Authoritative record: `iterations/ITERATION_003.md`.

## Iter004 results so far

### Protection mechanism audit

- M1 local lower-rank/frame redundancy: `PARTIAL`; current form allows `q^2`.
- M2 refinement-fixed background protection: `FAIL_SCOPED`; kinematic `T=I` does not imply dynamical stationarity.
- M3 microscopic Goldstone/shift protection: `FAIL_SCOPED`; no continuous microscopic shift generator derived.
- M4 cohomological origin alone: `FAIL_SCOPED`; physical `q` is gauge invariant, so `q^2` is too.
- M5 Lorentz symmetry enhancement: `BLOCKED`; `C` has continuous `O(1,3)` stabilizer, but exact `B_4` automorphisms are only finite `S_4`.

### Exact tensor representation audit

The six Boolean pair variables satisfy

`pair6 ~= Sym^2(V3)`

for the standard 3D `S_4` representation `V3`.

Exact decomposition:

`6=1+3+2`.

The rank-1 redefinition image is

`4=1+3`,

leaving the exact two-dimensional quotient.

This means the correct arena for a future gauge/constraint theorem is the **full six-component tensor-like pair field plus four lower-rank constraint directions**, not only the reduced 2D field.

## Current blocker

`BLOCKED_MISSING_DERIVED_DERIVATIVE_FIRST_CLASS_OR_NOETHER_LIKE_CONSTRAINT_ALGEBRA_ON_FULL_6_PLUS_4_RELATIONAL_STRUCTURE_THAT_FORBIDS_MASS_DEFORMATION_WITHOUT_POST_HOC_CONTINUUM_GAUGE_INSERTION`

## Active gate — Iter004-G4

`QGR-ITER004-G4-DERIVATIVE-CONSTRAINT-CLOSURE`

1. Work with full `x_ij(n)` pair data plus four rank-1 relational-frame variables.
2. Generate transformations only from neighboring relational redefinitions and existing incidence/composition maps.
3. Derive the most general first-neighbor derivative transformation compatible with `S_4`.
4. Test the QGR-L0 Hessian for a Noether/first-class-like null identity.
5. Determine whether the unique onsite mass deformation is forbidden.
6. Fail closed if the needed transformation must simply be copied from continuum linearized diffeomorphisms.

## KMQGB synchronization

Last inspected KMQGB head: `f503c39177012879a80bf767282a15d0c441e2f9` (Iter324-325 merge). Global D7 remains unauthorized in the inspected snapshot.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `iterations/ITERATION_004.md`
4. `iterations/ITERATION_003.md`
5. `docs/CONSTITUTION.md`
6. newest files under `results/` and `code/` for Iter004
7. current KMQGB front and recent commits
