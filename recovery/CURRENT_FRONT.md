# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter007`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / ALL_ORDERS_LOCAL_GRAVITY_FIXED / DISTINGUISHABILITY_AND_OBSERVABLE_CLOSURE`
Active roadmap stage: `R7 — normalized observable closure; R9 precursor — prediction/discrimination`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **78%**
- Iter005 completion: **100%**
- Iter006 completion: **100%**
- Iter007 completion: **65%**
- Lead architecture: `A / CCRC`
- Active candidate: `QGR-L1`
- Local metric-only two-derivative action: **all-orders PASS_SCOPED**
- Local action: `a integral sqrt(|det G|) R[G]`, zero-cosmological active branch
- Physical local modes: **2** on the characteristic cone
- Regular state/measure/composition/refinement layer: **PASS_SCOPED**
- Strong-curvature coarse observable algebra: **PASS_SCOPED path-groupoid**
- First QGR-specific finite-refinement correction: **PASS_SCOPED, O(h^4)**
- Fixed-path accumulated correction: **O(L h^3)**
- Normalized purity-loss observable form: **PASS_SCOPED**
- Finite-cell continuous Lorentz invariance of correction: **FAIL_SCOPED; microscopic S4 only**
- Physical microscopic scale `h`: **OPEN**
- Full graph/4D RG scaling: **OPEN**
- Numerical beyond-GR prediction: **OPEN**
- Independent KMQGB pass: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

Readiness is an internal construction-roadmap metric, not probability of correctness.

## Iter006 closure — critical negative and repair

### G10A

The statement “all finite-cell torsion roots are finite/isolated” is false. At the exact flat seed, after exact reduction to `24` quadratic Gram constraints in `24` variables, the identity root is regular with reduced determinant

`47,775,744 = 2^16 * 3^6`,

but a disconnected rank-22 branch exists. Predictor/corrector continuation keeps residual about `1e-14` while its norm grows beyond `30.2`.

Classification:

`REFUTED_IN_SCOPE_ALL_TORSION_ROOTS_FINITE__DISCONNECTED_NONCOMPACT_FINITE_CELL_BRANCH_EXISTS`.

### G10B

This does not invalidate the physical QGR connection because the connection had already been derived as a function of `G,DG`. Same-realization requires the finite branch to match the infinitesimal Levi-Civita connection as the mesh is refined.

For regular Lorentzian fields on compact patches, the seed Jacobian and parameter-dependent implicit-function theorem give a unique identity-connected principal root at sufficiently fine resolution,

`L_e(h)=I+h omega_e[G,DG]+O(h^2)`.

Strong-curvature coarse transport is the product limit of the fine principal roots, not a sum over every coarse polynomial root.

Iter006 is therefore **100% complete on the regular refinement domain**, while degenerate/singular configurations remain outside its theorem.

Records:

- `results/ITER006_G10A_GLOBAL_TORSION_BRANCH_COUNTEREXAMPLE.md`
- `results/ITER006_G10B_REFINEMENT_CONNECTED_PRINCIPAL_CONNECTION.md`

## Iter007 G1 — all-orders local gravity

With `G`, exact pullback covariance, and the unique compatible connection fixed, the metric-only local invariant space with at most two derivatives is

`a sqrt(|det G|) R[G] + b sqrt(|det G|)`

modulo a boundary term. The active flat/no-potential branch fixes `b=0`; the already selected quadratic action fixes `a`.

Thus

`S_local[G]=a integral sqrt(|det G|) R[G]`

is the unique all-orders local metric-only two-derivative completion. The independently derived `S2`, unique `S3`, and unique `S4` are its perturbative coefficients.

Classification:

`PASS_SCOPED_UNIQUE_ALL_ORDERS_LOCAL_METRIC_ONLY_TWO_DERIVATIVE_ACTION_WITH_ZERO_COSMOLOGICAL_BRANCH`.

## Iter007 G2 — first beyond-classical-GR correction

For 24 orderings,

`delta_pi=(h^2/2) sum_(i<j) s_pi(ij)[X_i,X_j]`.

The exact sign mean is zero and the six-dimensional covariance spectrum is

`1/3 x3`, `5/3 x3`.

After tracing the history label, the first nonunitary term is

`Delta E(rho)=(h^4/8) C_ab [K_a,[K_b,rho]] + O(h^5)`.

The correction is curvature controlled, has no fitted relative coefficient, and the two `S4` three-dimensional sectors have fixed relative strength `1:5`.

## Iter007 G3/G4 — Lorentz boundary

The exact ordering covariance is not invariant under the already-derived continuous `C`-preserving boost, although the correct induced two-form metric is invariant.

More generally, a nonzero positive covariance cannot be invariant under the full noncompact Lorentz representation on the nontrivial two-form sector. Therefore finite-scale positive ordering noise has only microscopic `S4` symmetry. Lorentz recovery requires the correction to vanish under refinement, or finite `h` produces a preferred-frame signature.

## Iter007 G5A — refinement scaling and normalized observable

One small cell has

`E_h=I+h^4 D+O(h^5)`.

For a fixed smooth physical causal path of length `L`, `N=L/h` cells give

`Delta E_path=O(L h^3)`.

Thus uniform refinement `h->h/b` suppresses the path-level effect as `b^-3`.

For `K_a=-iH_a`, purity

`P=Tr(rho^2)`

obeys

`Delta P=-(h^4/4) C_ab Tr([H_a,rho]^dagger[H_b,rho])+O(h^5) <= 0`.

For a pure input,

`1-P_out=(h^4/4) C_ab Tr([H_a,rho]^dagger[H_b,rho])+O(h^5)`.

This closes a normalized **observable form** with no free decoherence coefficient, but not its numerical magnitude because the physical scale `h` is still unknown.

Record:

- `results/ITER007_G5A_PATH_SCALING_AND_PURITY_OBSERVABLE.md`

## Active blocker / next gate

`QGR-ITER007-G5B-PHYSICAL_SCALE_AND_FULL_NETWORK_RG_CLOSURE`

1. determine whether the microscopic scale `h` is predicted, bounded, or remains one dimensionful parameter;
2. derive full graph/four-dimensional blocking rather than extrapolating the fixed-path `b^-3` result;
3. map the six curvature generators to the physical two-mode quotient in a specified preparation/readout protocol;
4. evaluate the purity-loss coefficient on at least one concrete physical background;
5. classify competing higher-derivative/refinement operators;
6. only then compare to Lorentz-violation/decoherence data;
7. do not add orientation weights, noncompact averaging, arbitrary scale matching, or free noise coefficients.

## KMQGB synchronization

Latest observed KMQGB head: `c806465e255dbbf87675b5c03d235851c6f5ce0b` (Iter342-343 independent RQCP reproduction and cutoff stress).

The RQCP fixed-band payload was independently reproduced and cutoff-stressed, but remains `PARTIAL_SUBFAMILY_ONLY`: the fixed-band restriction and absence of an autonomously derived gravity sector remain. D7 promotion is not authorized and `NEW_REQUIRED` remains false.

## Claim locks

- no experimental Lorentz-violation claim yet;
- physical microscopic scale `h` not fixed;
- normalized purity-loss **form** closed, numerical prediction not closed;
- full network/4D RG scaling open;
- no independent KMQGB pass;
- no claim that all known models fail;
- no `NEW_REQUIRED` authorization;
- no claim that QGR is unique as a full quantum-gravity theory.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `iterations/ITERATION_007.md`
4. `results/ITER007_G5A_PATH_SCALING_AND_PURITY_OBSERVABLE.md`
5. `results/ITER007_G4_POSITIVE_NOISE_LORENTZ_NOGO.md`
6. `results/ITER007_G3_MICROSCOPIC_LORENTZ_BREAKING_OF_ORDERING_CORRECTION.md`
7. `results/ITER007_G2_HISTORY_ORDERING_QUANTUM_CORRECTION.md`
8. `results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md`
9. `iterations/ITERATION_006.md`
10. `results/ITER006_G10B_REFINEMENT_CONNECTED_PRINCIPAL_CONNECTION.md`
11. `results/ITER006_G10A_GLOBAL_TORSION_BRANCH_COUNTEREXAMPLE.md`
12. `docs/CONSTITUTION.md`
13. current KMQGB scoped deltas + authoritative benchmark front
