# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter007`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / ALL_ORDERS_LOCAL_GRAVITY_FIXED / DISTINGUISHABILITY_AND_OBSERVABLE_CLOSURE`
Active roadmap stage: `R7 — normalized observable closure; R9 precursor — prediction/discrimination`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **76%**
- Iter005 completion: **100%**
- Iter006 completion: **100%**
- Iter007 completion: **55%**
- Lead architecture: `A / CCRC`
- Active candidate: `QGR-L1`
- Local metric-only two-derivative action: **all-orders PASS_SCOPED**
- Local action: `a integral sqrt(|det G|) R[G]`, zero-cosmological active branch
- Physical local modes: **2** on the characteristic cone
- State/measure/composition layer: **PASS_SCOPED on regular Lorentzian refinement domain**
- Strong-curvature coarse observable algebra: **PASS_SCOPED path-groupoid**
- Normalized 24-history instrument: **PASS_SCOPED**
- First finite-refinement beyond-GR correction: **PASS_SCOPED, O(h^4)**
- Finite-cell continuous Lorentz invariance of that correction: **FAIL_SCOPED; microscopic S4 only**
- Physical microscopic scale `h`: **OPEN**
- Normalized beyond-GR observable: **OPEN**
- Independent KMQGB pass: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

Readiness is an internal construction-roadmap metric, not probability of correctness.

## Iter006 closure — state / measure / composition / refinement

Iter006 is complete on the explicit regular Lorentzian refinement domain.

Established chain:

`Q_13 response configurations`
`-> positive H_kin=L2(Q_13, |det G|^(-5/2)d^10G)`
`-> physical quotient / BRST algebra`
`-> finite frame-holonomy lift`
`-> exact path-groupoid blocking`
`-> normalized 24-history isometry / CPTP coarse channel`
`-> refinement-connected Levi-Civita transport`.

### G10A — important negative result retained

The hypothesis that all finite-cell torsion roots form a finite isolated set is false even on the exact flat seed.

After eliminating Lorentz matrices, the flat torsion problem reduces to `24` quadratic Gram equations in `24` variables. The identity root is regular, with reduced exact Jacobian determinant

`47,775,744 = 2^16 * 3^6`.

However a disconnected rank-22 root was found and continued for 50 predictor/corrector steps while maintaining residual of order `1e-14`; the solution norm grew from about `10.93` to above `30.2`.

Classification:

`REFUTED_IN_SCOPE_ALL_TORSION_ROOTS_FINITE__DISCONNECTED_NONCOMPACT_FINITE_CELL_BRANCH_EXISTS`.

Record:

- `results/ITER006_G10A_GLOBAL_TORSION_BRANCH_COUNTEREXAMPLE.md`
- `code/qgr_iter006_g10a_seed_runaway_branch.py`

### G10B — physical connection remains well-defined

The physical connection was already fixed before G10 by the same-realization chain

`G,DG -> infinitesimal compatible connection -> finite transport`.

Thus disconnected coarse algebraic roots are not independent quantum branches. The physical branch is the identity-connected root satisfying

`L_e(h)=I+h omega_e[G,DG]+O(h^2)`.

For regular Lorentzian fields with bounded jets on a compact patch, the seed Jacobian plus the parameter-dependent implicit-function theorem gives a unique local principal root at sufficiently fine resolution. Coarse strong-curvature transport is the ordered product of those fine roots.

Numerical refinement audit on the curved conformal family gives

`max ||L-I|| ~= 0.5692, 0.2906, 0.1485, 0.07519, 0.03785`

for `h=1,1/2,1/4,1/8,1/16`, and fixed-path successive product differences

`~0.0338, 0.0185, 0.00972, 0.00499`.

Classification:

`PASS_SCOPED_REGULAR_REFINEMENT_CONNECTED_DISCRETE_LEVI_CIVITA_TRANSPORT`.

Record:

- `results/ITER006_G10B_REFINEMENT_CONNECTED_PRINCIPAL_CONNECTION.md`
- `code/qgr_iter006_g10b_refinement_connected_transport.py`

## Iter007 G1 — all-orders local gravity

With `G`, exact pullback covariance, and the unique compatible torsion-free connection already fixed, classify local metric-only scalar densities with at most two derivatives.

- zero derivatives: only `sqrt(|det G|) Lambda`; the active flat/no-potential branch fixes `Lambda=0`;
- one derivative: no metric-compatible scalar;
- two derivatives: one Riemann tensor. Its three naive double-metric contractions reduce to `R`, `-R`, and `0`.

Therefore the nonzero two-derivative scalar space is one-dimensional and, modulo a boundary term,

`S_local[G]=a integral sqrt(|det G|) R[G]`.

The previous independently derived `S2`, unique `S3`, and unique `S4` are the perturbative coefficients of this same all-orders local action.

Classification:

`PASS_SCOPED_UNIQUE_ALL_ORDERS_LOCAL_METRIC_ONLY_TWO_DERIVATIVE_ACTION_WITH_ZERO_COSMOLOGICAL_BRANCH`.

Record:

- `results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md`
- `code/qgr_iter007_g1_curvature_scalar_count.py`

## Iter007 G2 — first model-specific finite-refinement correction

For the 24 ordering histories, the ordering-dependent BCH displacement is

`delta_pi=(h^2/2) sum_(i<j) s_pi(ij)[X_i,X_j]`.

Exact permutation averaging gives zero sign mean. The six-dimensional ordering-sign covariance has exact spectrum

- `1/3` with multiplicity `3`;
- `5/3` with multiplicity `3`.

After history tracing, the first nonunitary term in the common-unitary interaction frame is

`Delta E(rho)=(h^4/8) sum_(a,b) C_ab [K_a,[K_b,rho]] + O(h^5)`

with `K_(ij)=[X_i,X_j]`.

Thus the first QGR-specific coarse quantum correction is curvature controlled, starts at `O(h^4)`, and has a fixed `1:5` relative strength between its two three-dimensional `S4` sectors.

Record:

- `results/ITER007_G2_HISTORY_ORDERING_QUANTUM_CORRECTION.md`
- `code/qgr_iter007_g2_history_ordering_covariance.py`

## Iter007 G3/G4 — finite-cell Lorentz boundary

An explicit rational continuous `C`-preserving boost leaves the correct induced two-form metric invariant but does **not** preserve the ordering covariance. At `r=2`, `33` covariance-difference entries are nonzero and the largest exact difference is `8/3`.

More generally, a nonzero positive-definite covariance invariant under the full noncompact represented Lorentz group would conjugate that representation into compact `O(6)`, contradicting the existence of unbounded boosts. The two-form representation has no trivial scalar subrepresentation that could carry a nonzero positive invariant covariance.

Therefore a nonzero positive ordering-noise correction cannot be exactly full-Lorentz invariant at finite cell scale. Lorentz recovery must occur by suppression of the correction as `h->0`, or finite `h` predicts a suppressed preferred-frame effect.

Records:

- `results/ITER007_G3_MICROSCOPIC_LORENTZ_BREAKING_OF_ORDERING_CORRECTION.md`
- `results/ITER007_G4_POSITIVE_NOISE_LORENTZ_NOGO.md`

## Active blocker / next gate

`QGR-ITER007-G5-REFINEMENT_SCALE_AND_NORMALIZED_OBSERVABLE_CLOSURE`

1. derive repeated-blocking scaling of the `O(h^4)` history-ordering channel;
2. determine whether the correction is irrelevant in the refinement limit;
3. identify the physical microscopic scale `h` or prove it remains a free parameter;
4. construct one normalized operational observable sensitive to the fixed curvature covariance;
5. map the six commutator components into that observable without arbitrary matching functions;
6. compare to experimental/phenomenological constraints only after the observable map is fixed;
7. do not introduce orientation weights or noncompact averaging to erase the finite-scale anisotropy.

## KMQGB synchronization

Latest observed KMQGB head: `c806465e255dbbf87675b5c03d235851c6f5ce0b` (Iter342-343 RQCP independent reproduction and cutoff-stress workflow).

Scoped result: a fixed-band RQCP payload was independently reproduced and cutoff-stressed in KMQGB CI. Classification remains `PARTIAL_SUBFAMILY_ONLY`; it does not remove the fixed-band restriction or derive an autonomous gravity sector. D7 promotion remains unauthorized and `NEW_REQUIRED` remains false.

## Claim locks

- no experimental Lorentz-violation claim yet;
- physical microscopic scale `h` not yet fixed;
- no normalized beyond-GR observable yet;
- higher-derivative/refinement operators not yet fully classified;
- no independent KMQGB pass;
- no claim that all known models fail;
- no `NEW_REQUIRED` authorization;
- no claim that QGR is unique as a full quantum-gravity theory.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `iterations/ITERATION_007.md`
4. `results/ITER007_G4_POSITIVE_NOISE_LORENTZ_NOGO.md`
5. `results/ITER007_G3_MICROSCOPIC_LORENTZ_BREAKING_OF_ORDERING_CORRECTION.md`
6. `results/ITER007_G2_HISTORY_ORDERING_QUANTUM_CORRECTION.md`
7. `results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md`
8. `iterations/ITERATION_006.md`
9. `results/ITER006_G10B_REFINEMENT_CONNECTED_PRINCIPAL_CONNECTION.md`
10. `results/ITER006_G10A_GLOBAL_TORSION_BRANCH_COUNTEREXAMPLE.md`
11. `docs/CONSTITUTION.md`
12. current KMQGB scoped deltas + authoritative benchmark front
