# QGR Iteration 007 — All-Orders Local Gravity and Distinguishability

Date: 2026-09-12
Status: `ACTIVE / MODEL_SIDE_BROADBAND_OBSERVABLE_CLOSED_SCOPED / ABSOLUTE_MICROSCOPIC_SCALE_BLOCKED`
Current task completion: **98%**
Candidate-program readiness: **86%**
Active candidate: **QGR-L1**
Theory established: **0%**

Readiness is an internal construction-roadmap metric, not a probability of correctness or fraction of quantum gravity solved.

## Objective

1. Close the local nonlinear gravitational action in the metric-only two-derivative class.
2. Derive the first QGR-specific finite-refinement correction without adding a novelty coefficient.
3. Derive network composition, overlapping-region gluing and physical two-mode transport/readout from the same realization.
4. Produce a normalized curved broadband comparator.
5. Determine whether its absolute physical magnitude is fixed by the current microscopic normalization chain.

## G1 — all-orders local two-derivative action

Within the metric-only local class with at most two derivatives, the unique nontrivial action density is

`a sqrt(|det G|) R[G]`

modulo a boundary term and the zero-cosmological active branch. This is the all-orders continuation of the independently derived QGR quadratic/cubic/quartic terms.

Classification:
`PASS_SCOPED_UNIQUE_ALL_ORDERS_LOCAL_METRIC_ONLY_TWO_DERIVATIVE_ACTION_WITH_ZERO_COSMOLOGICAL_BRANCH`.

Record: `results/ITER007_G1_ALL_ORDERS_TWO_DERIVATIVE_LOCAL_ACTION.md`.

## G2-G5 — first finite-history correction and network scaling boundary

For the 24 B4 orderings the exact ordering covariance has spectrum

`1/3 x3 ; 5/3 x3`,

and after tracing the normalized history register

`Delta E(rho)=(h^4/8) C_ab [K_a,[K_b,rho]] + O(h^5)`.

The finite-cell covariance is only microscopic S4, not exact continuous Lorentz. On a fixed causal path the accumulated correction is `O(L h^3)` and the normalized purity-loss form is positive.

A naive same-carrier four-volume accumulation is only a stress bound. Later path-groupoid analysis proves that face-neighbour B4 cells are overlapping supports rather than serial history-channel steps.

Records:
- `results/ITER007_G2_HISTORY_ORDERING_QUANTUM_CORRECTION.md`
- `results/ITER007_G3_MICROSCOPIC_LORENTZ_BREAKING_OF_ORDERING_CORRECTION.md`
- `results/ITER007_G4_POSITIVE_NOISE_LORENTZ_NOGO.md`
- `results/ITER007_G5A_PATH_SCALING_AND_PURITY_OBSERVABLE.md`
- `results/ITER007_G5B_PARALLEL_NETWORK_RG_AND_READOUT_AUDIT.md`

## G6A-G6C — history composition, finite local net and physical quotient

Runs `34653478008`, `34654604762`, and `34655130571` close the relevant finite-network structure in scope.

Key results:

- local `1/24` marginals alone do not determine arbitrary overlap correlations, but true serial B4 diagonals have the exact product-uniform `24^-n` branch law;
- face-neighbour B4 cells share a complete B3 face but their opposite-vertex 24-history morphisms are not serially composable;
- the minimal regular two-cell configuration glues as the exact fiber product
  `352+352-152=552` over the common B3 data;
- cylindrical multiplication algebras intersect on the shared B3 subalgebra;
- quantum boundary matching is relative/direct-integral gluing rather than an independent tensor product duplicating the boundary;
- finite frame pullback maps `ker H / im R` canonically between the two-dimensional physical characteristic fibers;
- no arbitrary phenomenological 2x2 polarization projector is permitted or required.

Records:
- `results/ITER007_G6A_HISTORY_COMPOSITION_AND_LOCAL_GLOBAL_SCALING.md`
- `results/ITER007_G6B_OVERLAPPING_CELL_GLUING_AND_CURVED_HISTORY_SPREAD.md`
- `results/ITER007_G6C_LOCAL_NET_AND_PHYSICAL_QUOTIENT_DESCENT.md`

## G6E — same-realization convention repair and positive physical pairing

Run `34657301235`: five lanes plus aggregate `SUCCESS`.

The earlier `C` versus `C^-1` convention boundary was repaired explicitly. With

`C=J-I`, `E=C^-1`, `S=I-J/6`,

one has

`S^T C S = E`.

The finite torsion/history calculation was rerun with the covariant seed `E`, not merely relabeled. Repaired G9 history slopes remain approximately four:

- relative trace: `4.0705480`;
- common-target null Gram: `4.0984388`;
- branch-pair barycentric rapidity scalar: `4.0685627`.

The trace-reversed covariant bilinear has the four derivative-gauge directions as its exact radical on the six-dimensional characteristic kernel and leaves a positive two-dimensional quotient. A regular positive boundary measure admits disintegration over the shared B3 pushforward without assuming conditional independence.

## G6F — normalized common characteristic Hilbert

Run `34657631926`: three lanes plus aggregate `SUCCESS`.

The future-null-cone measure and positive two-mode quotient pairing define a common target direct-integral characteristic Hilbert space on the regular one-particle/readout domain.

Two normalized packet families have exact overlaps

`A0(gamma)=2/(1+gamma)`

and

`A1(gamma)=4(2+gamma)/(3(1+gamma)^2)`.

Their repaired-G9 history-mixture losses scale with exponents `4.0707806` and `4.0707012`. The coefficient ratio tends to `4/3`, proving explicitly that the coefficient depends on preparation while the `h^4` order is robust in this test.

## G6G — physical polarization holonomy

Run `34657905251`: three lanes plus aggregate `SUCCESS`.

Relative branch Lorentz generators scale as `O(h^2)`. Their quadratic Lorentz-algebra Casimirs and finite trace defect scale as `O(h^4)`.

In a specified relational standard section, central-ray Wigner-angle spread scales as `O(h^2)` and fixed linear spin-2 polarization overlap loss as `O(h^4)`. A specified narrow-packet combined envelope+polarization comparator has fitted loss exponent `4.0050639`.

This is preparation/readout dependent and is not promoted as a universal coefficient.

## G6H — cutoff-free full broadband two-mode comparator

Run `34658915788`: four lanes plus aggregate `SUCCESS`.

The radial future-null-cone integral is analytic; no arbitrary UV momentum cutoff enters the normalized comparator. For every target null direction and every history, the source momentum, little-group element and spin-2 rotation are recomputed, removing the G6G narrow-packet approximation.

Broadband coherent two-mode history-mixture loss exponents:

- profile `m0`: `4.0342370`;
- profile `m1`: `4.0347357`.

For `m0`, changing polarization preparation gives

- envelope-only: `4.0923625`;
- linear spin-2: `4.0549234`;
- helicity: `4.0591959`.

Classification:
`PASS_SCOPED_CONVENTION_REPAIRED_CURVED_TWO_MODE_POSITIVE_PAIRING_COMMON_CHARACTERISTIC_HILBERT_AND_CUTOFF_FREE_BROADBAND_24_HISTORY_COMPARATOR_WITH_ROBUST_H4_REFINEMENT_ORDER`.

Record:
`results/ITER007_G6E_G6H_CURVED_BROADBAND_OBSERVABLE_CLOSURE.md`.

## G7A — absolute microscopic scale identifiability

Initial run `34659076333` failed closed because one lightweight script unnecessarily imported NumPy; no physical criterion was changed. After removing that dependency, run `34659176245` completed four lanes plus aggregate `SUCCESS`.

For the current dimensionless metric/response variable,

`Dq ~ h partial q`,

and in four dimensions

`kappa sum_cells (Dq)^2 -> (c_geom kappa/h^2) integral d^4x (partial q)^2`.

Hence

`a_cont = c_geom kappa/h^2`.

The logarithmic normalization Jacobian with respect to `(log kappa, log h)` is `[1,-2]`, rank one. The exact unresolved direction is

`h -> lambda h`,
`kappa -> lambda^2 kappa`.

The continuum GR normalization is unchanged along this direction, but the leading history correction changes as `lambda^4`.

The authoritative microscopic action still explicitly retains `kappa` as one free overall normalization, and no later QGR result derives an absolute physical `h`.

Classification:
`BLOCKED_SCOPED_ABSOLUTE_MICROSCOPIC_SCALE_NOT_IDENTIFIABLE_FROM_CURRENT_QGR_NORMALIZATION_CHAIN`.

Record:
`results/ITER007_G7A_MICROSCOPIC_SCALE_IDENTIFIABILITY.md`.

## Active blocker / next gate

`MISSING_DERIVED_MICROSCOPIC_NORMALIZATION_OR_SECOND_INDEPENDENT_PHYSICAL_SCALE_OBSERVABLE`

Active gate:
`QGR-ITER007-G7B-MICROSCOPIC-NORMALIZATION-OR-MATTER-SECOND-SCALE`

Prospective routes:

1. derive `kappa` from the same microscopic quantum/amplitude/measure normalization, with no phenomenological fit; or
2. derive a universal matter/detector coupling that supplies a second independent physical-scale relation.

Fail closed if the route requires declaring `h=l_P`, setting `kappa` physically by convention, or fitting the scale solely to obtain a desired history effect.

## KMQGB synchronization

Latest observed KMQGB head: `d14e48f6790c49cca5b202dc227a179a9577819a`, Iter353-355 bundle. A GFT condensate child obtained a scoped dispersion-rigidity result, but its own scope guard keeps the parent family nonterminal and explicitly forbids D7 promotion. `NEW_REQUIRED` remains unauthorized.

## Claim locks

- theory established remains `0%`;
- no experimental confirmation;
- no universal QGR decoherence coefficient;
- no absolute physical prediction until `h/kappa` is separated;
- no identification `h=l_P` by convention;
- no arbitrary 2x2 polarization projector;
- no face-neighbour cells treated as serial history channels;
- no independent KMQGB pass;
- no claim all known models fail;
- no KMQGB `NEW_REQUIRED` authorization;
- no claim QGR is unique/correct as a full quantum-gravity theory.

## Progress accounting

- Iter007 completion: **98%**.
- Candidate-program readiness: **86%**.
- Theory established: **0%**.
