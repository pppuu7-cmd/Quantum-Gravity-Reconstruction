# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter007`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / ALL_ORDERS_LOCAL_GRAVITY_FIXED / NETWORK_HISTORY_GLUING_AND_OBSERVABLE_CLOSURE`
Active roadmap stage: `R7 observable closure / R9 prediction-discrimination precursor`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **78%**
- Iter005 completion: **100%**
- Iter006 completion: **100%**
- Iter007 completion: **84%**
- Lead architecture: `A / CCRC`
- Active candidate: `QGR-L1`
- Local metric-only two-derivative action: **all-orders PASS_SCOPED**
- Local action: `a integral sqrt(|det G|) R[G]`, zero-cosmological active branch
- Physical local modes: **2** on the characteristic cone
- Regular state/measure/composition/refinement layer: **PASS_SCOPED**
- Strong-curvature path-groupoid transport: **PASS_SCOPED**
- First QGR-specific history correction: **PASS_SCOPED, O(h^4)**
- Finite-cell history covariance: `1/3 x3 ; 5/3 x3`, microscopic `S4`
- Fixed causal-path accumulated effect: **O(L h^3)**
- Local reduced-purity refinement in spatial-factor toy: **b^-3**
- Extensive/global `-log purity` in same toy: **O(1) marginal**
- Local cross-cell history correlations: **NOT DERIVED**
- Natural serial/disjoint Boolean completions: **product-uniform local orders**
- Numerical beyond-GR local prediction: **OPEN**
- Independent KMQGB pass: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

Readiness is an internal construction-roadmap metric, not probability of correctness.

## Established realization chain

`B4 relational seed`
`-> derived four directions + Lorentzian incidence form`
`-> Sym^2(W4) ten-component response`
`-> derivative gauge closure / protected masslessness`
`-> two physical characteristic modes`
`-> unique cubic + quartic self-coupling`
`-> all-orders metric-only two-derivative local action`
`-> Lorentzian configuration Hilbert/BRST operational physical algebra`
`-> refinement-connected finite connection + path-groupoid transport`
`-> normalized 24-history instrument`
`-> fixed O(h^4) curvature/history channel`
`-> network-history gluing gate`.

No separate continuum theory or phenomenological noise coefficient has been spliced into this chain.

## Iter006 closure reminder

All algebraic torsion roots are **not** globally finite: G10A found a disconnected noncompact rank-22 branch even at the flat seed. The physical connection survives because it had already been prospectively defined as the refinement-connected branch matching the infinitesimal Levi-Civita connection. Iter006 is complete on the regular Lorentzian refinement domain.

Records:

- `results/ITER006_G10A_GLOBAL_TORSION_BRANCH_COUNTEREXAMPLE.md`
- `results/ITER006_G10B_REFINEMENT_CONNECTED_PRINCIPAL_CONNECTION.md`

## Iter007 local gravity and finite-history result

Within the metric-only local class with at most two derivatives,

`S_local[G]=a integral sqrt(|det G|) R[G]`

is the unique all-orders completion on the active zero-cosmological branch.

The 24 local B4 orderings generate the leading coarse history channel

`Delta E(rho)=(h^4/8) C_ab [K_a,[K_b,rho]] + O(h^5)`

with exact covariance spectrum

`1/3 x3 ; 5/3 x3`.

The nonzero positive covariance is not invariant under the full continuous Lorentz two-form representation; finite-cell symmetry is microscopic `S4`.

For a fixed causal path the accumulated leading effect is `O(L h^3)` and normalized purity loss has the positive form

`1-P_out=(h^4/4) C_ab Tr([H_a,rho]^dagger[H_b,rho]) + O(h^5)`.

## Parallel G5B audit — Actions run 34653064309

Five lanes and the fail-closed aggregate passed.

### Full-network stress

Sequentially applying one `O(h^4)` cell channel to the same carrier over `O(h^-d_eff)` cells gives `h^(4-d_eff)`. The exact toy reproduces `b^-3,b^-2,b^-1` for `d_eff=1,2,3` and an `O(1)` plateau for the sequential four-dimensional stress construction.

Classification:

`PASS_SCOPED_PATH_IRRELEVANT_BUT_LOCAL_TRACE_4D_BULK_MARGINAL`.

This is an integrated-channel stress result, not a local field-observable theorem.

### Seed representation

The exact four-cover physical seed representation is

`8 = 2 + 3 + 3prime`,

while ordering commutators form

`6 = 3 + 3prime`.

For the isolated physical `2`, `End(2)=1+sign+2`, so there is no linear S4-equivariant map `3+3prime -> End(2)`. A concrete two-mode readout therefore needs directional/fiber transport or a quadratic contraction.

### Competing unitary operators

Parity-even curvature-squared unitary action terms cannot change purity and therefore cannot fake the history-channel purity-loss signature.

### Delayed trace

For independent product history registers, tracing only after two cells gives exactly the same reduced channel as local tracing. Delaying the partial trace alone cannot create cancellation.

### Scale

Newton matching fixes only the combination `kappa/h^2`; the present construction does not separately predict the dimensionless microscopic normalization `kappa` and length `h` for path observables.

Record:

- `results/ITER007_G5B_PARALLEL_NETWORK_RG_AND_READOUT_AUDIT.md`

## Parallel G6A audit — Actions run 34653478008

Three further lanes and aggregate passed.

### Joint-history law is not fixed by local 1/24 marginals

Three exact two-cell laws with identical uniform local marginals produce variance traces for the summed ordering displacement:

- product: `12`;
- synchronized: `24`;
- reversed: `0`.

Therefore local history normalization alone cannot determine a network correction. Choosing anticorrelation now to cancel the finite-cell effect is forbidden post-hoc tuning.

Classification:

`BLOCKED_LOCAL_1_OVER_24_HISTORY_NORMALIZATION_DOES_NOT_FIX_CROSS_CELL_CORRELATIONS`.

### Natural non-overlapping Boolean compositions

- serial `B4` ordinal sum: `24^2=576` histories;
- disjoint concurrent `B8`: `8!=40320` histories with exactly `C(8,4)=70` interleavings for each pair of local orders.

Both give product-uniform local order pairs and no automatic cancellation.

### Local versus global purity

In a tensor-factor toy with `b^3` spatial sites and `b` causal steps per site:

- local reduced purity loss scales as `b^-3`;
- global extensive `-log P` tends to a nonzero constant.

Hence four-volume marginality is an extensive/global warning, not by itself a surviving local Lorentz-violating decoherence probability.

Record:

- `results/ITER007_G6A_HISTORY_COMPOSITION_AND_LOCAL_GLOBAL_SCALING.md`

## Active blocker

`BLOCKED_MISSING_DERIVED_OVERLAPPING_CELL_HISTORY_GLUING_AND_FIELD_SUPPORT_MAP`

The local B4 model does not yet state how adjacent cells sharing microscopic events/faces form one relational complex. Without that object QGR cannot derive the joint history law, decide which cells act on the same physical quotient fiber versus spacelike tensor factors, or close a local numerical observable.

## Active gate — Iter007 G6B

`QGR-ITER007-G6B-DERIVE_OVERLAPPING_CELL_GLUING_AND_FIELD_SUPPORT_FROM_CCRC`

1. define shared events/faces for neighboring B4 cells in one CCRC complex;
2. derive the induced global partial order and joint history measure;
3. derive the field-support/factorization map;
4. derive the projective coarse trace from that gluing;
5. map `2+3+3prime` to a concrete local two-mode preparation/readout;
6. evaluate the first local normalized prediction on a curved background;
7. accept any surviving anisotropic channel; do not tune cross-cell correlations to erase it.

## KMQGB synchronization

Latest observed head: `a55eed66b399c212083e6e1283aaa641817e769b` (Iter342b portability recovery workflow); Iter344 fakeon NNLL scoped work is also present.

RQCP scientific values remain reproducible within quantified platform drift but the family is still `PARTIAL_SUBFAMILY_ONLY`, with no autonomous gravity-sector derivation and no D7 promotion. Iter344 provides a scoped fakeon NNLL sign certificate in the tested source domain, while the parent family remains nonterminal (`0/5` material quantization branches terminal). `NEW_REQUIRED` remains unauthorized.

## Claim locks

- no experimental Lorentz-violation claim;
- no local continuum decoherence prediction yet;
- no derived overlapping-cell joint history law;
- no identification of extensive global purity with local experiment;
- no arbitrary anticorrelation/cross-cell weight may be added to cancel the effect;
- no independent KMQGB pass;
- no claim all known models fail;
- no `NEW_REQUIRED` authorization;
- no claim QGR is unique/correct as a full quantum-gravity theory.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `iterations/ITERATION_007.md`
4. `results/ITER007_G6A_HISTORY_COMPOSITION_AND_LOCAL_GLOBAL_SCALING.md`
5. `results/ITER007_G5B_PARALLEL_NETWORK_RG_AND_READOUT_AUDIT.md`
6. `results/ITER007_G5A_PATH_SCALING_AND_PURITY_OBSERVABLE.md`
7. `results/ITER007_G4_POSITIVE_NOISE_LORENTZ_NOGO.md`
8. `results/ITER007_G3_MICROSCOPIC_LORENTZ_BREAKING_OF_ORDERING_CORRECTION.md`
9. `results/ITER007_G2_HISTORY_ORDERING_QUANTUM_CORRECTION.md`
10. `results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md`
11. `iterations/ITERATION_006.md`
12. `results/ITER006_G10B_REFINEMENT_CONNECTED_PRINCIPAL_CONNECTION.md`
13. `results/ITER006_G10A_GLOBAL_TORSION_BRANCH_COUNTEREXAMPLE.md`
14. `docs/CONSTITUTION.md`
15. current KMQGB scoped deltas + authoritative benchmark front
