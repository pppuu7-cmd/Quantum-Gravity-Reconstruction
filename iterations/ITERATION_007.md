# QGR Iteration 007 — All-Orders Local Gravity and Distinguishability

Date: 2026-09-12
Status: `ACTIVE / ALL_ORDERS_LOCAL_ACTION_FIXED / FINITE_HISTORY_CORRECTION_DERIVED / FINITE_LOCAL_NET_GLUING_CLOSED_SCOPED / CURVED_COMMON_TARGET_READOUT_BLOCKED`
Current task completion: **93%**
Candidate-program readiness: **82%**
Active candidate: **QGR-L1**

Readiness is an internal construction-roadmap metric, not a probability of correctness or fraction of quantum gravity solved. `theory established` remains false.

## Objective

1. Close the local nonlinear gravitational action in the metric-only two-derivative class.
2. Derive the first QGR-specific finite-refinement correction without adding a novelty coefficient.
3. Determine its refinement/Lorentz structure and a normalized observable form.
4. Derive network composition, overlapping-region gluing and the physical two-mode transport/readout from the same realization.

## G1 — all-orders local two-derivative action

The unique local metric-only density with at most two derivatives is

`a sqrt(|det G|) R[G] + b sqrt(|det G|)`

modulo a boundary term. The flat/no-potential active branch fixes `b=0`; the previously selected quadratic normalization fixes `a`.

Therefore

`S_local[G] = a integral sqrt(|det G|) R[G]`

is the unique completion in the scoped class.

Classification:
`PASS_SCOPED_UNIQUE_ALL_ORDERS_LOCAL_METRIC_ONLY_TWO_DERIVATIVE_ACTION_WITH_ZERO_COSMOLOGICAL_BRANCH`.

Record: `results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md`.

## G2 — exact 24-history correction

For the 24 B4 orderings the BCH ordering displacement has zero mean at `O(h^2)`. The exact six-dimensional sign covariance has spectrum

`1/3 x3 ; 5/3 x3`.

After tracing the normalized history register,

`Delta E(rho)=(h^4/8) C_ab [K_a,[K_b,rho]] + O(h^5)`.

No independent decoherence coefficient is introduced.

Classification:
`PASS_SCOPED_EXACT_24_HISTORY_ORDERING_COVARIANCE_FIXES_LEADING_H4_CURVATURE_DEPENDENT_COARSE_QUANTUM_CORRECTION`.

## G3/G4 — finite-cell Lorentz boundary

The finite-cell positive ordering covariance has microscopic `S4` symmetry and is not invariant under the full continuous Lorentz two-form representation. A nonzero positive covariance on that noncompact representation cannot be exactly full-Lorentz invariant.

This does not imply a surviving local continuum violation; refinement/network support must be treated correctly.

## G5A — fixed causal-path observable

For one cell `E_h=I+h^4 D+O(h^5)`. A fixed smooth causal path with `N=L/h` serial cells gives

`Delta E_path=O(L h^3)`.

Purity satisfies

`Delta P=-(h^4/4) C_ab Tr([H_a,rho]^dagger[H_b,rho])+O(h^5) <= 0`.

Thus the normalized observable form is closed but its physical numerical magnitude is not.

Record: `results/ITER007_G5A_PATH_SCALING_AND_PURITY_OBSERVABLE.md`.

## G5B — parallel network/readout stress audit

GitHub Actions run `34653064309`: five lanes plus aggregate successful.

Key results:

- sequential same-carrier accumulation over `O(h^-d_eff)` cell channels gives stress scaling `h^(4-d_eff)`;
- the naive `d_eff=4` same-carrier construction is marginal `h^0`, but this was only a stress bound;
- seed physical representation is `8=2+3+3prime`, ordering sector `6=3+3prime`;
- no linear S4-equivariant map `3+3prime -> End(2)` exists, forbidding an arbitrary direct 2x2 noise insertion;
- unitary curvature-squared action terms preserve purity and cannot fake the history-channel purity loss;
- delaying the trace over independent history registers does not cancel the reduced channel;
- Newton matching fixes only a combination of microscopic normalization and `h`; absolute `h` is not independently predicted for path observables.

Record: `results/ITER007_G5B_PARALLEL_NETWORK_RG_AND_READOUT_AUDIT.md`.

## G6A — joint-history identifiability and local/global scaling

GitHub Actions run `34653478008`: three lanes plus aggregate successful.

Uniform local `1/24` history marginals alone do not fix arbitrary cross-cell correlations: exact countermodels can produce cancellation, product accumulation or enhancement. However this ambiguity must be applied only where a joint law is actually required.

A spatial-factor toy separates observables:

- local reduced purity loss recovers as `b^-3`;
- extensive global `-log P` can remain `O(1)`.

Hence the earlier four-volume marginality is not itself a local continuum decoherence theorem.

Record: `results/ITER007_G6A_HISTORY_COMPOSITION_AND_LOCAL_GLOBAL_SCALING.md`.

## G6B — overlapping-cell gluing and path-groupoid correction

GitHub Actions run `34654604762`: five lanes plus aggregate successful.

### Exact B3 overlap

Minimal incidence-preserving gluing of two direction-labelled face-neighbour B4 cells identifies one complete B3 face:

- 8 shared vertices;
- 12 shared oriented edges;
- 6 shared plaquettes.

Only six discrete B3 atom relabelings remain; inherited direction labels select the identity representative.

### Face neighbours are not serial history-channel steps

A one-cell 24-history instrument is the coarse morphism from one B4 corner to its opposite corner. For a cell based at `n`, its endpoint is `n+(1,1,1,1)`.

A translated cell diagonal is serially composable only for shift

`(1,1,1,1)`.

Those serial cells share one endpoint but no fine edges or plaquettes. Face-neighbour B4 cells share a B3 face but their opposite-vertex history morphisms are **not serially composable**.

Therefore the earlier G5B `h^0` same-carrier four-volume construction is retained only as a stress upper bound and is not an authorized path-groupoid interpretation of all face-adjacent cells.

### Serial branch law is fixed

For truly serial composable blocks, G8A gives `K_alpha^dagger K_alpha=I/24`, so `n` blocks have exactly `24^n` equal-norm branches with probability `24^-n`. No cross-block correlation coefficient is available.

### Global overlap paths do not factor

The `2x1x1x1` union of two face-neighbour B4 cells has only

`5!/2! = 60`

monotone global paths, not `24^2=576` independent local-diagonal pairs. Only 6/60 global paths are unions of two complete overlapping-cell diagonals.

### Concrete curved history spread

On the pre-existing Iter006 G9 regular finite-curvature branch, all 24 opposite-vertex transports were constructed for `h=1,1/2,1/4,1/8`. The gauge-conjugation-invariant pairwise quantity

`delta_(q,p)=tr(A_q^-1 A_p)-4`

has nonzero RMS with fitted refinement exponent

`3.9786`,

and `RMS(delta)/h^4` remains approximately constant (`0.0475...0.0496`).

Classification:
`NUMERICALLY_VERIFIED_SCOPED_CURVED_B4_PAIRWISE_HISTORY_HOLONOMY_TRACE_SPREAD_IS_NONZERO_AND_SCALES_AS_H4`.

This is a classical/path-holonomy diagnostic, not decoherence.

Record: `results/ITER007_G6B_OVERLAPPING_CELL_GLUING_AND_CURVED_HISTORY_SPREAD.md`.

## G6C — finite local net and physical quotient descent

GitHub Actions successful run `34655130571`: four lanes plus aggregate successful. The first run failed closed because of a local exact-arithmetic implementation bug; after restoring all inputs/pivots to exact `Fraction` arithmetic and changing no criterion, the rerun passed.

### Regular configuration fiber product

One B4 regular path-groupoid configuration has dimension

`10*16 + 6*32 = 352`.

The common B3 boundary has dimension

`10*8 + 6*12 = 152`.

The two-cell union has

`10*24 + 6*52 = 552`.

Exactly,

`352+352-152=552`.

The finite regular configuration net therefore glues canonically as

`X_(A union B) = X_A x_(X_F) X_B`,

with equality of the shared B3 data.

Classification:
`PASS_SCOPED_REGULAR_PATH_GROUPOID_CONFIGURATION_NET_GLUES_AS_FIBER_PRODUCT_OVER_SHARED_B3_AND_HAS_EXACT_CYLINDRICAL_ISOTONY`.

### Boundary-relative quantum gluing

The quantum matching analogue is fiberwise/relative tensoring over one shared boundary label,

`H_glued ~ direct_integral dmu_F(b) [H_A(b) tensor H_B(b)]`,

not a naive independent tensor product duplicating the B3 boundary. A finite exact surrogate explicitly removes the cross-boundary sectors `b_A != b_B`.

Classification:
`PASS_SCOPED_BOUNDARY_MATCHING_REQUIRES_RELATIVE_TENSOR_DIRECT_SUM_OR_DIRECT_INTEGRAL_STRUCTURE_NOT_NAIVE_INDEPENDENT_TENSOR_PRODUCT`.

Analytic disintegration of the full interacting QGR measure remains open.

### Cylindrical algebra intersection

In the regular finite coordinate model,

`C_A intersect C_B = C_F`

for primitive coordinate sets, and the polynomial/cylindrical multiplication subalgebras obey

`Alg_cyl(A) intersect Alg_cyl(B) = Alg_cyl(F)`.

This establishes finite isotony/intersection for that subalgebra, not the complete constrained AQFT net.

### Canonical two-mode quotient descent

The physical characteristic fiber is

`P_(G,k)=ker H_G(k)/im R(k)`,

with dimension 2 on the QGR-L1 characteristic cone.

For finite regular frame pullback `h -> A^T h A` and `k -> A^T k`, exact rational tests on 3 nontrivial frame maps x 3 characteristic covectors verify

`Sym2(A) R(k) = R(A^T k) A^T`

and map every Hessian-null vector to a Hessian-null vector. Hence `Sym2(A)` descends canonically to an isomorphism between the two-dimensional physical quotient fibers.

Classification:
`PASS_SCOPED_FINITE_FRAME_PULLBACK_CANONICALLY_DESCENDS_TO_ISOMORPHISM_BETWEEN_TWO_DIMENSIONAL_QGR_L1_PHYSICAL_CHARACTERISTIC_QUOTIENT_FIBERS`.

A free phenomenological 2x2 polarization projector is therefore not needed and must not be inserted.

Record: `results/ITER007_G6C_LOCAL_NET_AND_PHYSICAL_QUOTIENT_DESCENT.md`.

## Active blocker / next gate — G6D

`BLOCKED_MISSING_COMMON_TARGET_CURVED_WAVEPACKET_READOUT_AND_INTERACTING_BOUNDARY_MEASURE_DISINTEGRATION`

`QGR-ITER007-G6D-CURVED-WAVEPACKET-QUOTIENT-READOUT-AND-LOCAL-PURITY`

1. transport one characteristic wavepacket/fiber through all 24 curved G9 histories using the canonical quotient descent;
2. quantify branch-dependent target characteristic-fiber separation and its refinement order;
3. construct a branch-symmetric common-target readout without selecting a branch-dependent polarization basis;
4. derive the local two-mode reduced density matrix and normalized purity from the same history instrument;
5. separately establish or bound the interacting boundary-relative measure/disintegration needed for overlapping regions;
6. only after this close a numerical beyond-GR local prediction and compare with data.

## KMQGB synchronization

Latest observed KMQGB head remains `a55eed66b399c212083e6e1283aaa641817e769b`. RQCP remains `PARTIAL_SUBFAMILY_ONLY`; Iter344 fakeon work is scoped and the parent family is nonterminal. D7 promotion and `NEW_REQUIRED` remain unauthorized.

## Claim locks

- no experimental Lorentz-violation claim;
- no numerical beyond-GR local prediction yet;
- no arbitrary correlated histories for non-composable overlapping cells;
- no sum of one history channel per face-neighbour cell as if those cells were serial;
- no naive Hilbert tensor product across a shared B3 boundary;
- no arbitrary 2x2 polarization/readout projector;
- the G6B `h^4` holonomy trace spread is not called quantum decoherence;
- absolute microscopic `h/kappa` separation remains open for phenomenology;
- no independent KMQGB pass;
- no claim that all known models fail;
- no `NEW_REQUIRED` authorization;
- QGR is not claimed unique/correct as a full quantum-gravity theory.

## Progress accounting

- Iter007 completion: **93%**.
- Candidate-program readiness: **82%**.
- Theory established: **0%**.
