# QGR Current Research Front

Updated: 2026-09-12
Active iteration: `Iter007`
Project phase: `MODEL_CONSTRUCTION_ACTIVE / ALL_ORDERS_LOCAL_GRAVITY_FIXED / FINITE_LOCAL_NET_CLOSED_SCOPED / CURVED_WAVEPACKET_READOUT`
Active roadmap stage: `R7 observable closure / R9 prediction-discrimination precursor`

## Canonical status

- Repository infrastructure readiness: **100%**
- Candidate-program readiness: **82%**
- Iter005 completion: **100%**
- Iter006 completion: **100%**
- Iter007 completion: **93%**
- Theory established: **0%**
- Lead architecture: `A / CCRC`
- Active candidate: `QGR-L1`
- Local metric-only two-derivative action: **all-orders PASS_SCOPED**
- Local action: `a integral sqrt(|det G|) R[G]`, zero-cosmological active branch
- Physical characteristic quotient: **2 modes**
- Regular state/measure/composition/refinement layer: **PASS_SCOPED**
- Strong-curvature path-groupoid transport: **PASS_SCOPED**
- Normalized 24-history instrument: **PASS_SCOPED**
- First history correction: **PASS_SCOPED, O(h^4)**
- Fixed causal-path accumulated correction: **O(L h^3)**
- Minimal two-cell B3 incidence gluing: **PASS_SCOPED**
- Serial history branch measure: **exact product-uniform 24^-n**
- Face-neighbour history diagonals serially composable: **NO**
- Regular finite overlapping-region configuration gluing: **fiber product over shared B3 — PASS_SCOPED**
- Cylindrical multiplication-algebra isotony/B3 intersection: **PASS_SCOPED**
- Canonical finite-frame descent to 2D physical quotient: **PASS_SCOPED**
- Curved common-target wavepacket/readout: **OPEN / active blocker**
- Numerical beyond-GR local purity prediction: **OPEN**
- Independent KMQGB pass: **NO**
- KMQGB `NEW_REQUIRED`: **NOT AUTHORIZED**

Readiness is an internal construction-roadmap metric, not probability of correctness.

## Established same-realization chain

`B4 relational seed`
`-> four derived directions + Lorentzian incidence form`
`-> Sym^2(W4) ten-component response`
`-> derivative gauge closure / no onsite mass`
`-> two physical characteristic modes`
`-> unique cubic + quartic self-coupling`
`-> all-orders metric-only two-derivative local action`
`-> Lorentzian configuration Hilbert/BRST operational physical algebra`
`-> refinement-connected finite connection + path-groupoid transport`
`-> normalized 24-history instrument`
`-> fixed O(h^4) curvature/history channel`
`-> exact serial branch law`
`-> finite B3 overlap fiber-product local net`
`-> canonical two-mode quotient descent`
`-> curved common-target wavepacket/readout gate`.

No separate continuum theory, phenomenological noise coefficient, free cross-cell correlation, or arbitrary 2x2 polarization projector has been inserted.

## Iter007 core local result

Within the scoped metric-only local class,

`S_local[G]=a integral sqrt(|det G|) R[G]`

is the unique all-orders two-derivative completion on the active zero-cosmological branch.

The 24 B4 orderings generate

`Delta E(rho)=(h^4/8) C_ab [K_a,[K_b,rho]] + O(h^5)`

with exact covariance spectrum

`1/3 x3 ; 5/3 x3`.

The finite-cell covariance has microscopic `S4`, not exact continuous Lorentz invariance. Along a fixed smooth causal path the accumulated correction is `O(L h^3)` and the normalized purity-loss form is positive.

## G5B/G6A correction to naive four-volume reasoning

Actions runs `34653064309` and `34653478008` established:

- a same-carrier `O(h^-4)` sequential stress construction is `O(1)`, but this is not a local field observable theorem;
- local reduced purity can recover as `h^3` while extensive/global `-log P` remains marginal;
- local `1/24` marginals alone do not fix arbitrary cross-cell correlations.

G6B then identified which cells are actually serial in the already-derived path groupoid, removing the ambiguity from the serial sector.

## G6B — overlap gluing and curved history spread

Actions run `34654604762`: five lanes + aggregate SUCCESS.

### Minimal face gluing

Two direction-labelled face-neighbour B4 regions identify a full B3 face:

- 8 shared vertices;
- 12 shared oriented edges;
- 6 shared plaquettes.

The abstract B3 face has only six discrete S3 atom relabelings; inherited direction labels select the identity representative.

### Serial-versus-overlap distinction

One 24-history cell instrument is an opposite-vertex diagonal morphism `n -> n+(1,1,1,1)`. A translated next cell is serially composable only when its base shift is exactly `(1,1,1,1)`. Such serial cells share one endpoint and no fine edges/plaquettes.

Therefore **face-neighbour B4 cells are overlapping local supports, not serial history-channel steps**. The old `h^0` all-face-cell same-carrier stress is not an authorized path-groupoid evolution law.

### Serial branch law

For actual serial coarse blocks, G8A fixes

`K_alpha^dag K_alpha = I/24`,

so `n` blocks have `24^n` equal-norm branches with probability `24^-n`. No serial cross-block correlation coefficient remains free.

### Overlap global paths

A `2x1x1x1` two-cell union has only `60` monotone global paths. Only `6` are unions of two complete overlapping local diagonals. Hence treating the overlap as `24^2=576` independent local history registers overcounts the physical path alternatives.

### Curved history spread

On the pre-existing G9 regular finite-curvature branch, all 24 path transports were computed for `h=1,1/2,1/4,1/8`. For

`delta_(q,p)=tr(A_q^-1 A_p)-4`,

the RMS refinement exponent is `3.9786`, and `RMS/h^4` is approximately constant (`0.0475...0.0496`). This is a dimensionless gauge-conjugation-invariant path-holonomy diagnostic, not decoherence.

Record: `results/ITER007_G6B_OVERLAPPING_CELL_GLUING_AND_CURVED_HISTORY_SPREAD.md`.

## G6C — finite local net and physical quotient descent

Actions run `34655130571`: four lanes + aggregate SUCCESS after correcting an exact-arithmetic implementation bug without changing criteria.

### Configuration fiber product

Regular coordinate dimensions:

- one B4: `352 = 10*16 + 6*32`;
- shared B3: `152 = 10*8 + 6*12`;
- two-cell union: `552 = 10*24 + 6*52`.

Exactly,

`352+352-152=552`.

Thus, on the finite regular path-groupoid domain,

`X_(A union B) = X_A x_(X_F) X_B`

with equality of common B3 data.

Classification:
`PASS_SCOPED_REGULAR_PATH_GROUPOID_CONFIGURATION_NET_GLUES_AS_FIBER_PRODUCT_OVER_SHARED_B3_AND_HAS_EXACT_CYLINDRICAL_ISOTONY`.

### Quantum boundary matching

The valid quantum gluing analogue is relative/fiberwise tensoring over the same boundary label,

`H_glued ~ direct_integral dmu_F(b) [H_A(b) tensor H_B(b)]`,

not an unconstrained tensor product duplicating the boundary. Analytic interacting-measure disintegration remains open.

### Cylindrical intersection

For the finite regular multiplication/cylindrical subalgebra,

`Alg_cyl(A) intersect Alg_cyl(B) = Alg_cyl(F)`.

This is not yet a full theorem for constrained derivative/operator algebras.

### Physical two-mode descent

For

`P_(G,k)=ker H_G(k)/im R(k)`,

`dim P=2` on the QGR-L1 characteristic cone. Exact rational tests verify

`Sym2(A) R(k)=R(A^T k) A^T`

and map Hessian nullspaces into the transformed Hessian nullspaces. Hence finite frame pullback descends canonically to an isomorphism of the two-dimensional physical quotient fibers. No arbitrary 2x2 polarization projector is permitted or needed.

Record: `results/ITER007_G6C_LOCAL_NET_AND_PHYSICAL_QUOTIENT_DESCENT.md`.

## Active blocker / next gate

`BLOCKED_MISSING_COMMON_TARGET_CURVED_WAVEPACKET_READOUT_AND_INTERACTING_BOUNDARY_MEASURE_DISINTEGRATION`

Active gate:
`QGR-ITER007-G6D-CURVED-WAVEPACKET-QUOTIENT-READOUT-AND-LOCAL-PURITY`

Tasks:

1. propagate one physical characteristic wavepacket through all 24 curved G9 histories with the canonical quotient descent;
2. quantify the branch-dependent target characteristic-fiber separation and its refinement scaling;
3. construct a branch-symmetric common-target bundle/readout without choosing a polarization basis per branch;
4. derive the local two-mode reduced density matrix and purity from the normalized history instrument;
5. separately derive or bound the interacting boundary-relative measure/disintegration;
6. only after that produce a numerical phenomenological comparator.

## KMQGB synchronization

Latest observed KMQGB head remains `a55eed66b399c212083e6e1283aaa641817e769b`. RQCP remains `PARTIAL_SUBFAMILY_ONLY`; Iter344 fakeon work is scoped and its parent family is nonterminal. D7 and `NEW_REQUIRED` remain unauthorized.

## Claim locks

- no experimental Lorentz-violation claim;
- no numerical beyond-GR local prediction yet;
- no sum of one history channel per face-neighbour cell as if serial;
- no arbitrary correlated histories for non-composable overlaps;
- no naive independent Hilbert tensor product across shared B3 data;
- no arbitrary 2x2 polarization/readout projector;
- G6B `h^4` holonomy trace spread is not quantum decoherence;
- absolute `h/kappa` separation remains open for phenomenology;
- no independent KMQGB pass;
- no claim all known models fail;
- no `NEW_REQUIRED` authorization;
- no claim QGR is unique/correct as a full quantum-gravity theory.

## Recovery order

1. `recovery/state.json`
2. `recovery/CURRENT_FRONT.md`
3. `iterations/ITERATION_007.md`
4. `results/ITER007_G6C_LOCAL_NET_AND_PHYSICAL_QUOTIENT_DESCENT.md`
5. `results/ITER007_G6B_OVERLAPPING_CELL_GLUING_AND_CURVED_HISTORY_SPREAD.md`
6. `results/ITER007_G6A_HISTORY_COMPOSITION_AND_LOCAL_GLOBAL_SCALING.md`
7. `results/ITER007_G5B_PARALLEL_NETWORK_RG_AND_READOUT_AUDIT.md`
8. `results/ITER007_G5A_PATH_SCALING_AND_PURITY_OBSERVABLE.md`
9. `results/ITER007_G4_POSITIVE_NOISE_LORENTZ_NOGO.md`
10. `results/ITER007_G3_MICROSCOPIC_LORENTZ_BREAKING_OF_ORDERING_CORRECTION.md`
11. `results/ITER007_G2_HISTORY_ORDERING_QUANTUM_CORRECTION.md`
12. `results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md`
13. `iterations/ITERATION_006.md`
14. `docs/CONSTITUTION.md`
15. current KMQGB scoped deltas and authoritative front
