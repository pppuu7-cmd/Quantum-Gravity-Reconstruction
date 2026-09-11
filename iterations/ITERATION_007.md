# QGR Iteration 007 — All-Orders Local Gravity and Distinguishability

Date: 2026-09-12
Status: `ACTIVE / ALL_ORDERS_LOCAL_ACTION_FIXED / HISTORY_CORRECTION_DERIVED / NETWORK_GLUING_BLOCKED`
Current task completion: **84%**
Candidate-program readiness: **78%**
Active candidate: **QGR-L1**

Readiness is an internal construction-roadmap metric, not a probability of correctness.

## Starting authority

Iter006 closed the regular state/measure/composition/refinement layer while preserving the G10 negative result:

- all algebraic finite-cell torsion roots are not finite/isolated;
- the physical connection is the refinement-connected principal branch matching the already-derived infinitesimal Levi-Civita connection;
- coarse strong-curvature transport is built from fine principal transports, not by summing every coarse torsion root.

Records:

- `results/ITER006_G10A_GLOBAL_TORSION_BRANCH_COUNTEREXAMPLE.md`
- `results/ITER006_G10B_REFINEMENT_CONNECTED_PRINCIPAL_CONNECTION.md`

## Iter007 objective

1. Close the local nonlinear gravitational action to all orders in the metric-only two-derivative class.
2. Derive the first QGR-specific finite-refinement effect without adding a novelty coefficient.
3. Determine its Lorentz/refinement properties and normalized observable content.
4. Derive the full-network history composition and physical support/readout map rather than extrapolate a single-path result.

## G1 — all-orders local two-derivative action

With Lorentzian `G`, exact pullback covariance and the unique torsion-free compatible connection already fixed, the metric-only local scalar-density space with at most two derivatives is

`a sqrt(|det G|) R[G] + b sqrt(|det G|)`

modulo a boundary term.

The active flat/no-potential branch fixes `b=0`; the previously selected quadratic normalization fixes `a`. Therefore

`S_local[G] = a integral sqrt(|det G|) R[G]`

is the unique all-orders local metric-only two-derivative completion in the scoped class. The independently derived `S2`, unique `S3`, and unique `S4` are its perturbative coefficients.

Classification:

`PASS_SCOPED_UNIQUE_ALL_ORDERS_LOCAL_METRIC_ONLY_TWO_DERIVATIVE_ACTION_WITH_ZERO_COSMOLOGICAL_BRANCH`.

Records:

- `results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md`
- `code/qgr_iter007_g1_curvature_scalar_count.py`

## G2 — exact 24-history ordering correction

For directional generators `X_i`, the ordering-dependent BCH displacement begins at

`delta_pi=(h^2/2) sum_(i<j) s_pi(ij)[X_i,X_j]`.

Across all 24 permutations the pair-sign mean is exactly zero. The exact six-dimensional covariance spectrum is

- `1/3` with multiplicity `3`;
- `5/3` with multiplicity `3`.

After tracing the history label,

`Delta E(rho)=(h^4/8) C_ab [K_a,[K_b,rho]] + O(h^5)`,

where `K_(ij)=[X_i,X_j]`.

The two three-dimensional S4 sectors have fixed relative strength `1:5`; no independent decoherence coefficient is introduced.

Classification:

`PASS_SCOPED_EXACT_24_HISTORY_ORDERING_COVARIANCE_FIXES_LEADING_H4_CURVATURE_DEPENDENT_COARSE_QUANTUM_CORRECTION`.

## G3/G4 — finite-cell Lorentz boundary

The exact covariance is not invariant under the already-derived continuous `C`-preserving boost, although the correct induced two-form metric is invariant.

A nonzero positive covariance on the nontrivial two-form representation cannot be invariant under the full noncompact Lorentz group. Thus the finite-cell history channel has microscopic `S4` rather than exact continuous Lorentz symmetry.

Classification:

- `PASS_SCOPED_FINITE_CELL_HISTORY_ORDERING_CORRECTION_HAS_ONLY_MICROSCOPIC_S4_SYMMETRY`;
- `PASS_SCOPED_NONZERO_POSITIVE_ORDERING_CHANNEL_CORRECTION_CANNOT_HAVE_EXACT_FULL_CONTINUOUS_LORENTZ_INVARIANCE_AT_FINITE_CELL_SCALE`.

## G5A — fixed-path scaling and purity observable

For one small cell,

`E_h=I+h^4 D+O(h^5)`.

Along a smooth fixed causal path of length `L`, `N=L/h` sequential cells give

`Delta E_path=O(L h^3)`.

Hence path-level refinement suppresses the leading effect as `b^-3` under `h->h/b`.

For `K_a=-iH_a`, normalized purity `P=Tr(rho^2)` obeys

`Delta P=-(h^4/4) C_ab Tr([H_a,rho]^dagger[H_b,rho])+O(h^5) <= 0`.

This gives a normalized observable **form**, but not yet a numerical prediction.

Record:

- `results/ITER007_G5A_PATH_SCALING_AND_PURITY_OBSERVABLE.md`

## G5B — five-lane GitHub Actions network/readout audit

GitHub Actions run `34653064309` executed five lanes in parallel and the aggregate passed.

### Full-network power-counting warning

If the same locally traced `O(h^4)` cell channel is sequentially accumulated over `O(h^-d_eff)` cells acting on one carrier, the leading integrated scaling is

`h^(4-d_eff)`.

Thus a naive four-dimensional count is marginal (`h^0`) even though the fixed path is irrelevant (`h^3`). The exact toy stress test reproduces `b^-3`, `b^-2`, `b^-1` for `d_eff=1,2,3` and a nonzero plateau for the sequential `d_eff=4` stress construction.

Classification:

`PASS_SCOPED_PATH_IRRELEVANT_BUT_LOCAL_TRACE_4D_BULK_MARGINAL`.

This is a stress result, **not** a local-field observable theorem.

### Exact physical representation

The four-cover physical seed mode space has

`8 = 2 + 3 + 3prime`

under `S4`, while the six ordering-commutator directions have

`6 = 3 + 3prime`.

The covariance eigenspaces are `3prime` at eigenvalue `1/3` and `3` at `5/3`.

For the isolated two-dimensional polarization irrep `E`,

`End(E)=1 + sign + 2`,

so there is no linear S4-equivariant map

`3 + 3prime -> End(E)`.

Therefore a physical two-mode readout must use directional/fiber transport or an allowed quadratic contraction. An arbitrary `2x2` noise matrix is forbidden.

### Competing four-derivative unitary operators

Modulo Gauss-Bonnet, parity-even metric-only curvature-squared actions have two dynamical bulk directions. Such Hamiltonian/unitary corrections preserve purity exactly and therefore cannot fake the positive history-channel purity loss.

### Delayed trace

For two independent product history registers, retaining coherence through both cells and tracing both registers only at the end yields exactly the same reduced two-cell Kraus channel as sequential local tracing. Delayed trace alone cannot cancel the effect.

### Microscopic scale

Writing a dimensionless cell coupling `kappa=a h^2`, Newton matching gives

`h^2=16 pi kappa G_N`

in the conventional normalization. The current reconstruction does not independently fix the dimensionless `kappa`, so `h` is not separately predicted for path observables.

Record:

- `results/ITER007_G5B_PARALLEL_NETWORK_RG_AND_READOUT_AUDIT.md`
- `.github/workflows/qgr-iter007-parallel-g5b-g6.yml`

## G6A — three-lane joint-history and local/global audit

GitHub Actions run `34653478008` executed three further lanes and the aggregate passed.

### Joint-history non-identifiability from local marginals

Three exact two-cell joint laws have identical uniform `1/24` local marginals but different covariance of the summed ordering displacement:

- product: variance trace `12`;
- synchronized: `24`;
- reversed: `0`.

Hence local `1/24` normalization does not determine cross-cell correlations. Choosing the anticorrelated/reversed law now solely to cancel the effect would be post-hoc tuning.

Classification:

`BLOCKED_LOCAL_1_OVER_24_HISTORY_NORMALIZATION_DOES_NOT_FIX_CROSS_CELL_CORRELATIONS`.

### Natural Boolean compositions

A serial ordinal sum of two `B4` cells has `24^2=576` maximal chains. A disjoint concurrent `B8` completion has `8!=40320` global chains, with exactly `C(8,4)=70` interleavings for every pair of local orders. Therefore the local restrictions are exactly product-uniform in both natural non-overlapping constructions; no cancellation is generated automatically.

Classification:

`PASS_SCOPED_NATURAL_SERIAL_AND_DISJOINT_BOOLEAN_COMPOSITIONS_DO_NOT_GENERATE_CANCELLING_LOCAL_ORDER_CORRELATIONS`.

### Local versus extensive purity

A spatial-factor toy with `b^3` spatial subsystems and `b` causal time cells per subsystem separates local and global observables:

- local reduced purity loss scales as `b^-3`;
- extensive global `-log P_global` approaches an `O(1)` constant.

Thus the earlier `h^0` four-volume count is an **extensive/global warning**, not by itself evidence of a finite local continuum decoherence probability.

Classification:

`PASS_SCOPED_LOCAL_REDUCED_PURITY_RECOVERS_AS_H3_WHILE_EXTENSIVE_GLOBAL_LOG_PURITY_IS_MARGINAL`.

Record:

- `results/ITER007_G6A_HISTORY_COMPOSITION_AND_LOCAL_GLOBAL_SCALING.md`
- `.github/workflows/qgr-iter007-g6a-history-composition.yml`

## Current scientific interpretation

The local gravitational sector is substantially closed within the scoped class. The first QGR-specific finite-refinement channel is also mathematically specified.

The remaining obstacle is now **microscopic network completion**:

- local `B4` history weights do not fix correlations between overlapping cells;
- natural non-overlapping Boolean compositions favor product-uniform local histories;
- local reduced observables and extensive global observables have different continuum scaling;
- the field-support/factorization map is not yet derived from CCRC.

Therefore a local continuum Lorentz-violation prediction is **not authorized**, but neither is a cancellation of the finite-cell anisotropy.

## Active blocker / next gate — G6B

`BLOCKED_MISSING_DERIVED_OVERLAPPING_CELL_HISTORY_GLUING_AND_FIELD_SUPPORT_MAP`

`QGR-ITER007-G6B-DERIVE_OVERLAPPING_CELL_GLUING_AND_FIELD_SUPPORT_FROM_CCRC`

1. define how neighboring `B4` cells share boundary/events in one relational complex;
2. derive the global partial order and the induced joint history law;
3. determine which cells act sequentially on the same physical quotient fiber and which represent spacelike/tensor-factor support;
4. derive the projective coarse trace from that microscopic gluing;
5. map the `2+3+3prime` seed representation to a concrete physical preparation/readout;
6. compute the first normalized local observable on at least one curved background;
7. if a finite anisotropic channel survives, accept it and confront phenomenology; do not tune history correlations to erase it.

## KMQGB synchronization

Latest observed KMQGB head: `a55eed66b399c212083e6e1283aaa641817e769b` (Iter342b portability recovery workflow), with Iter344 fakeon NNLL scoped domain work also present.

- RQCP scientific headlines remain reproducible within quantified platform drift, but the upstream absolute `5e-15` release-integrity check is not portable on the tested runner; the family remains `PARTIAL_SUBFAMILY_ONLY` and no D7 promotion is authorized.
- Iter344 gives a scoped robust fakeon NNLL sign certificate in its tested source domain, while its parent family remains nonterminal (`0/5` material quantization branches terminal) and D7 promotion remains unauthorized.

`NEW_REQUIRED` remains unauthorized.

## Claim locks

- no experimental Lorentz-violation claim;
- no numerical beyond-GR prediction yet;
- no derived overlapping-cell joint history law yet;
- no claim that extensive global purity equals a local experimental decoherence observable;
- microscopic `h`/`kappa` absolute normalization remains open for path observables;
- no independent KMQGB pass;
- no claim that all known models fail;
- no `NEW_REQUIRED` authorization;
- QGR is not claimed unique as a full quantum-gravity theory.

## Progress accounting

- Iter007 completion: **84%**.
- Candidate-program readiness: **78%**.
